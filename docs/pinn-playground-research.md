# A PINN playground for Volatile Worlds: research report

*Prepared 2026-09-02 for the design of a new "PINN playground" tab. No code; this is the study that precedes it.*

*Method: six parallel research agents, one per dimension (the ladder of smallest problems; loss construction; architecture; optimisation and failure modes; astrophysics and exoplanet connections; pedagogy and browser feasibility). Every arXiv ID or DOI cited below was fetched and confirmed by the agent that cites it unless marked "unverified". Two full texts were read end to end: the FBPINN paper (Moseley, Markham, Nissen-Meyer 2023) and "An expert's guide to training PINNs" (Wang, Sankaran, Wang, Perdikaris 2023). One correction was applied during synthesis: an agent conflated Moseley, Nissen-Meyer & Markham 2020 (Solid Earth, the supervised seismic surrogate already on the site) with Moseley's separate PINN wave-equation preprint (arXiv 2006.11894); they are different papers.*

---

## 0. The short answer

**The simplest possible PINN problem is `u'(x) = cos(ωx), u(0) = 0` with ω = 1 on [−2π, 2π].** The residual `û' − cos(ωx)` does not contain `û` itself, so the network is only being asked to be an antiderivative: nothing couples the output to its own derivative, the loss is convex in the output function, and nothing can go wrong conceptually. A 2×16 tanh network with 200 collocation points and Adam converges quickly. It is the opening problem of the FBPINN paper (arXiv 2107.07871 §3), and it has a second life: turn ω up to 15 and the same network fails, 4×64 fails too, and only a 5×128 network (66 433 parameters) resolves all the cycles. That single dial is the cleanest demonstration of spectral bias in the literature.

**The simplest problem with real PINN content is exponential decay, `y' = −k y, y(0) = 1`.** It is the first problem where the residual couples `ŷ` and `ŷ'`, and the first with a trivial solution: `y ≡ 0` satisfies the ODE exactly, so the initial-condition term is the only thing preventing collapse. It is the class of problem Lagaris, Likas & Fotiadis solved in 1998 with the trick it motivates, the trial solution `ŷ = 1 + t·N(t)` that satisfies the initial condition by construction.

Everything else on the ladder adds exactly one ingredient at a time: fixed-point attraction (logistic), competing loss terms (Poisson), data plus physics (damped oscillator), spectral bias (frequency sweep), "converged loss, wrong answer" (pendulum), a singular point (Lane–Emden, already built), stiffness, a first PDE, curriculum (convection), sharp fronts (Burgers).

The report's proposal is a **14-station tab** (Section 6) organised along the five places physics can be injected into a neural network: the problem statement, the data, the architecture, the loss, and the optimiser. Each station has one dial, one trick, a before/after switch, and an honest metric (true error against a reference solution, never the training loss alone). Everything in stations 1–12 trains in seconds with the hand-written 2×20 jet-propagating MLP the site already has; Section 5 gives measured step rates.

---

## 1. The ladder of smallest problems

### 1.1 The rungs

All rungs are 1-D or (1+1)-D. "Trick" is the single new idea each rung motivates. The numbers in the "pathology" column are the published thresholds.

| # | Problem | Equation, domain | Conditions | Exact / reference | Derivatives | Pathology exposed | Trick motivated | Reference |
|---|---|---|---|---|---|---|---|---|
| 0 | Integrator | u' = cos(ωx), x ∈ [−2π, 2π], ω = 1 | u(0) = 0 | sin(ωx)/ω | u' | none: the residual has no u | the autodiff residual itself; input normalisation to [−1, 1]; output scaling 1/ω | arXiv 2107.07871 §3.1 |
| 1 | Exponential decay | y' = −ky, k = 1, t ∈ [0, 5] | y(0) = 1 | e^{−kt} | y' | the trivial solution y ≡ 0; IC weight vs residual weight | hard IC via ŷ = 1 + t·N(t) | Lagaris 1998 (DOI 10.1109/72.712178); arXiv 2112.05620 |
| 2 | Logistic, fixed points | y' = r y(1−y) or y(1−y²), horizon T = 2.5 → 7.5 | y(0) = y₀ small | closed form | y' | fixed-point attraction: success rate 100 % at T = 2.5, 0–14 % at T ≥ 5 | shorten or curriculum in T; time-marching | arXiv 2203.13648 Table 4 |
| 3 | 1-D Poisson | u'' = −(aπ)² sin(aπx), x ∈ [0, 1], a = 1 → 4 | u(0) = u(1) = 0 | sin(aπx) | u'' | BC/residual imbalance: 24 % error at λ_b = 1, 0.16 % at λ_b ≈ 100 | NTK weighting, or hard BC x(1−x)·N(x) | arXiv 2007.14527 §7.2 |
| 4 | Damped oscillator (Moseley's tutorial) | u'' + 2δu' + ω₀²u = 0, δ = 2, ω₀ = 20, t ∈ [0, 1] | u(0) = 1, u'(0) = 0 | e^{−δt}·2A cos(φ + ωt) | u', u'' | a data-only net cannot extrapolate; the physics term needs weight 1e-4; "very sensitive to the relative weighting" | data + physics loss; loss weighting; 3×32, Adam 1e-4, 20 000 steps, 30 collocation points | benmoseley.blog; github.com/benmoseley/harmonic-oscillator-pinn |
| 5 | Frequency sweep | rung 0 with ω = 15, or rung 4 with ω₀ = 80 | as above | as above | u', u'' | spectral bias: 2×16 fails at ω = 15; 5×128 barely works, unstable | sinusoidal ansatz N(t)·sin(αt + β); Fourier features; domain decomposition | arXiv 2107.07871 §3.2; Moseley workshop Task 3; arXiv 2012.10047 |
| 6 | Nonlinear pendulum | y'' + ω₀² sin y = 0, ω₀ = 25 (Baty) or g/l = 9.81, T ≤ 7.5 | y(0), y'(0) | RK4 | y', y'' | converged loss but a phase-shifted wrong solution; 0 % success at T ≥ 5, capture by the unstable upright fixed point at y₀ = 175° | energy-conservation loss; first-order system form | arXiv 2302.12260 §IV.B; arXiv 2203.13648 Table 1 |
| 7 | Lane–Emden (built) | θ'' + (2/ξ)θ' + θⁿ = 0, n = 0, 1, 5 | θ(0) = 1, θ'(0) = 0 | 1 − ξ²/6; sin ξ/ξ; (1 + ξ²/3)^{−1/2} | θ', θ'' | singular coefficient at ξ = 0; θⁿ for θ < 0; the first zero ξ₁ unknown | multiply the residual by ξ; hard vs soft IC; ξ₁ as a trainable eigenvalue | DOI 10.1016/j.ascom.2023.100734; arXiv 2307.07302; arXiv 2507.03961 |
| 8 | Stiff two-scale system (own construction) | y₁' = −y₁, y₂' = −λ(y₂ − y₁), λ = 10³, t ∈ [0, 10] | y₁(0) = 1, y₂(0) = 0 | y₁ = e^{−t}, y₂ = λ/(λ−1)·(e^{−t} − e^{−λt}) | y' | stiffness: the fast transient is never resolved, the loss plateaus | log-spaced collocation; multi-output net; eliminate the fast variable (QSSA) | arXiv 2011.04520 (ROBER) |
| 9 | Transient heat | u_t = u_xx − e^{−t}(sin πx − π² sin πx), x ∈ [−1, 1], t ∈ [0, 1] | u(x,0) = sin πx, u(±1,t) = 0 | e^{−t} sin πx | u_t, u_xx | none: the first PDE that just works | two-input network; space–time sampling; three loss terms | DeepXDE diffusion.1d demo |
| 10 | Convection | u_t + βu_x = 0, x ∈ [0, 2π), t ∈ [0, 1], β = 1 → 30 | u(x,0) = sin x, periodic | sin(x − βt) | u_t, u_x | error 0.8 % at β = 1, 1.1 % at 10, 75 % at 20, 90 % at 30, 96 % at 40 | curriculum in β; sequence-to-sequence time marching; periodic input layer | arXiv 2109.01050 |
| 11 | Burgers (capstone, minutes) | u_t + uu_x = (0.01/π)u_xx, x ∈ [−1, 1], t ∈ [0, 1] | u(0,x) = −sin πx, u(t,±1) = 0 | Cole–Hopf | u_t, u_x, u_xx | a shock: needs 10⁴ collocation points and L-BFGS (Raissi: 6.7e-4 with 9×20) | residual-based adaptive resampling; L-BFGS | DOI 10.1016/j.jcp.2018.10.045 |

Beyond the ladder, too heavy for seconds in a browser but each the canonical exhibit of one more trick: the 1-D wave equation with a mixed-frequency initial condition (NTK-adaptive weights, 45.2 % → 0.17 %, arXiv 2007.14527 §7.3); Allen–Cahn (causal training, 49.8 % → 0.14 %, arXiv 2203.07404); reaction–diffusion at ρ = 5 (curriculum, arXiv 2109.01050).

### 1.2 Candidates deliberately left out

- Steady 1-D heat, u'' = 0: the solution is a straight line; teaches nothing Poisson does not.
- The undamped oscillator alone: subsumed by rung 4, whose exponential envelope is what the ansatz trick in rung 5 exploits.
- Kepler two-body as a *failure* benchmark: no paper uses it that way (the closest is three-body periodic orbits, arXiv 2607.23501); its pathologies are the pendulum's in a costlier package. It returns in Section 4 as an exoplanet-flavoured demo of conservation losses and Hamiltonian networks.
- Bernoulli/Riccati: no verified benchmark; a Riccati equation is rung 2 without the fixed-point story.
- Lane–Emden as rung 0: a good destination, a poor start, because three things (singular point, nonlinearity, eigenvalue) arrive at once.

### 1.3 The lesson the ladder teaches

Rungs 1, 2 and 6 all show "the loss is small but the answer is wrong": trivial solution, fixed-point parking, phase-shifted pendulum. Baty's phrase from the tutorial (arXiv 2302.12260), "a wrong solution even if the loss function displays convergence", is the lesson of the whole ladder, and the reason every station must plot true error against a reference, never the training loss alone.

---

## 2. The trick catalogue

Organised by where the physics enters. Steve Brunton's framing of five injection points (problem, data, architecture, loss, optimiser) is a useful spine; the catalogue below follows it.

### 2.1 The problem statement: non-dimensionalisation

Step 1 of the expert's guide's pipeline (arXiv 2308.08468) and practice 1 of NVIDIA's recommended practices: rescale x, t and u so every variable is O(1). Glorot initialisation assumes O(1) inputs; FBPINN shows a large domain and a high frequency are the *same* optimisation problem after normalisation. Output scaling matters equally (multiply N by the expected solution scale, e.g. 1/ω in rung 0). It is "indispensable but not a silver bullet": residual and boundary scales can still differ, which is why loss balancing (2.4) remains necessary.

*Demo:* the heat equation on x ∈ [0, 100] m, t ∈ [0, 3600] s in raw SI units versus dimensionless form. Before: loss frozen or NaN. After: converges in ~2000 steps.

### 2.2 The data: collocation sampling

- **Fixed strategies.** Wu et al. 2023 (arXiv 2207.10289, > 6000 runs) compared equispaced grid, uniform random, Latin hypercube, Halton, Hammersley, Sobol; in 1-D a regular grid beats Latin hypercube for the trivial-solution problem (arXiv 2112.05620).
- **Resampling.** Random-R: resample every N steps (N ~ 200 for diffusion, < 100 for Burgers). The expert's guide "strongly recommends random sampling in all PINN simulations": full-batch fixed points let the network overfit the residual *at* the points; resampling acts as a regulariser.
- **Residual-based adaptive sampling.** RAR-G (DeepXDE, arXiv 1907.04502): every k steps add the m points of largest |r| from a dense candidate set. RAD (Wu et al.): resample all points from p(x) ∝ ε(x)^k / E[ε^k] + c, defaults k = 1, c = 1, recommended as the default for any new PDE (Burgers: 1.69 % → 0.02 % with 2000 points). RAR-D (k = 2, c = 0) adds points incrementally. R3 (Daw et al., arXiv 2207.02338): retain points whose residual exceeds the mean, release the rest, resample uniformly; designed against propagation failure. Importance sampling: arXiv 2104.12325.
- **How many points.** Mishra & Molinaro (arXiv 2006.16144) bound generalisation error by training error plus a quadrature term, so more points help only once training error is small; where the points are matters more than how many.

*Demo:* a steep front (Burgers at t = 0.5, or a reaction front). Toggle Grid / Sobol / Random-R / RAD; animate the collocation set clustering at the front; add a c-slider to show that c = 0 collapses all points onto the shock and the smooth parts degrade.

### 2.3 The architecture

**Hard constraints through the output transformation.**
- Trial functions (Lagaris, Likas, Fotiadis 1998; arXiv physics/9705023): ŷ = A(x) + B(x)·N(x), with A satisfying the conditions and B vanishing where they are imposed. Two-point BVP: ŷ = (1−x)y₀ + x·y₁ + x(1−x)N. IVP with two conditions: ŷ = y₀ + v₀x + x²N. FBPINN uses ŷ = tanh(ωx)·N(x), with the tanh width deliberately matched to the solution wavelength so N needs little compensation near the boundary. Generalisation: Theory of Functional Connections (arXiv 1812.08625).
- Approximate distance functions (Sukumar & Srivastava 2022, arXiv 2104.08426): B becomes a distance-to-boundary function built from R-functions; Neumann/Robin data via transfinite interpolation. Demo: mixed BC u(0) = a, u'(1) = b; or the clamped beam u'''' = q with φ = x²(1−x)².
- Exact periodicity (Dong & Ni 2021, arXiv 2007.07442): a first layer mapping x to (cos ωx, sin ωx), ω = 2π/L, makes any network on top C^∞-periodic; the expert's guide uses it in every periodic benchmark. Demo: rung 10 convection.
- Positivity via exp or softplus outputs (folklore); symmetry via N_even(x) = ½(N(x) + N(−x)); for Lane–Emden, θ = 1 + ξ²·N_even(ξ) enforces θ(0) = 1, θ'(0) = 0 and the regularity at the singular origin exactly.
- Conservation by construction: divergence-free 2-D fields from a stream function (arXiv 2002.10558); the general differential-form construction (arXiv 2210.01741, NeurIPS 2022).
- Hamiltonian neural networks (Greydanus et al. 2019, arXiv 1906.01563), Lagrangian neural networks (Cranmer et al. 2020, arXiv 2003.04630), SympNets (arXiv 2001.03750): the network learns a scalar H(q, p) and the dynamics follow from autodiff, so energy is conserved exactly or the flow map is symplectic. Demo: harmonic oscillator or pendulum; baseline MLP dynamics spiral, HNN gives closed orbits and a flat energy trace.
- Augmented Lagrangian (hPINN, arXiv 2102.04626) as the principled version of "increase λ_b over time".

An honest note: Baty (arXiv 2307.07302) found hard constraints on Lane–Emden n = 1 gave errors "not smaller and even slightly worse" than soft ones. Hard constraints remove a failure mode; they do not guarantee more accuracy.

**Input features against spectral bias.**
- Spectral bias itself: MLPs learn low frequencies first (Rahaman et al. ICML 2019, arXiv 1806.08734; the F-Principle, arXiv 1901.06523).
- Random Fourier features (Tancik et al. 2020, arXiv 2006.10739; for PINNs Wang, Wang, Perdikaris 2021, arXiv 2012.10047): γ(x) = [cos Bx, sin Bx], B ~ N(0, σ²) fixed. Expert's guide: σ ∈ [1, 10]; too small blurs, too large gives salt-and-pepper artefacts. In their Allen–Cahn ablation, removing Fourier features was the single most damaging change (5.84e-4 → 4.35e-1). Multi-scale variant: several embeddings with different σ_i in separate branches.
- Moseley's ansatz for the oscillator at ω₀ = 80: û = N(t)·sin(αt + β) with learnable α, β, so the network learns only the envelope (workshop Task 3).
- SIREN (Sitzmann et al. 2020, arXiv 2006.09661): sin(ω₀(Wx + b)) with a specific initialisation; derivatives of a SIREN are SIRENs. Sensitive to ω₀ and input scale; Wong et al. (arXiv 2109.09338) on why sinusoidal spaces help PINNs.
- Random weight factorisation (arXiv 2210.01274): W = diag(exp s)·V, s ~ N(μ, σ), μ = 0.5–1.0, σ = 0.1; a per-neuron learning rate. Ablation: 5.84e-4 → 6.62e-3 without it.

*Demo:* rung 5. Before: a 2×16 tanh net fits only the first cycles near the boundary. After: the same net with Fourier features fits every cycle.

**Activation functions.** The activation must have non-trivial derivatives up to the PDE order: ReLU's second derivative is zero, so u_xx of a ReLU network is zero almost everywhere and second-order residuals cannot train (expert's guide §4.1; Maczuga & Paszyński ICCS 2023, DOI 10.1007/978-3-031-35995-8_6). Tanh is the default; sin and GELU/Swish are alternatives; no activation dominated everywhere on the 1-D wave equation, sin was worst in one of three settings, tanh never the worst. Adaptive activations (Jagtap, Kawaguchi, Karniadakis 2020, arXiv 1906.01170): σ(n·a·z) with a trainable slope. *Demo:* u'' = f with ReLU (converges to a straight line) versus tanh; then plot the learned slope.

**Modified MLP, depth and width.** The modified MLP (arXiv 2001.04536): two encoders U, V and gated layers g ← g⊙U + (1−g)⊙V; generally outperforms the standard MLP on residual minimisation at roughly double cost. PirateNets (arXiv 2402.00326): residual blocks with a gate initialised at zero, so the network starts shallow; plain deep MLPs *degrade* with depth under standard initialisation. For 1-D playground problems 2–4 layers of 16–64 units suffice (FBPINN's ω = 1 case converges with 2×16, 321 parameters); with a Levenberg–Marquardt optimiser 2-hidden-layer networks beat the deep networks of the original PINN paper on 1-D Burgers and Schrödinger with 4–25× fewer parameters (arXiv 2602.08515).

**Domain decomposition.** cPINN/XPINN (Jagtap, Kharazmi, Karniadakis 2020, DOI 10.1016/j.cma.2020.113028; DOI 10.4208/cicp.OA-2020-0164): a network per subdomain, continuity enforced by interface loss terms. FBPINN (Moseley, Markham, Nissen-Meyer 2023, arXiv 2107.07871): û = C[Σ_i w_i(x)·unnorm∘N_i∘norm_i(x)], with overlapping sigmoid window functions w_i, each subnet seeing inputs normalised over *its* subdomain, and the hard-constraint operator C outside; no interface loss because the sum is smooth by construction. On u' = cos 15x: 30 subdomains × (2×16) = 9630 parameters converge quickly where a single 5×128 PINN with 66 433 parameters barely does; on the multi-scale u' = cos x + 15 cos 15x the FBPINN error is two orders of magnitude below the best PINN; on the second-order u'' = sin 15x both struggle until a "learning outwards" schedule trains the subdomains adjacent to the boundary first. Placing an interface on a Burgers shock made FBPINN slightly *worse* than a single PINN.

**Time-dependent architecture tricks.** Time-marching windows (Wight & Zhao, arXiv 2007.04542); sequence-to-sequence at one Δt per window (Krishnapriyan et al.); bc-PINN (Mattey & Ghosh 2022, arXiv 2106.07606), one network retrained window by window with a backward-compatibility loss. Parametric PINNs: a physical parameter as an extra input, u_θ(x, n); the site's Lane–Emden family network is exactly this. First-order reformulation (FO-PINN, arXiv 2210.14320): q = u' as an extra output, u'' → q', with q − u' as an added residual; largest gains reported for parametric and higher-order problems.

**Operator learning, for positioning only.** DeepONet (Lu, Jin, Karniadakis 2021, arXiv 1910.03193) maps an input *function* and a query point to an output; FNO (Li et al. 2021, arXiv 2010.08895) learns integral kernels in Fourier space. The parametric PINN is the cheapest scalar-parameter version of the idea; DeepONet is the next step when the parameter becomes a function.

### 2.4 The loss

The baseline composite loss is

L(θ) = λ_r·mean|N[u_θ](x_i)|² + λ_b·mean|B[u_θ](x_j) − g_j|² + λ_0·mean|u_θ(x_k, 0) − u₀(x_k)|² + λ_d·mean|u_θ(x_m) − u_m|²

(residual, boundary, initial, data; Raissi, Perdikaris, Karniadakis 2019, DOI 10.1016/j.jcp.2018.10.045). The key fact the playground must teach: these terms have different units, different gradient magnitudes, and different NTK eigenvalues. Almost every trick below is a response to that mismatch.

**Loss weighting.**
- Manual weights: for Poisson at a = 4, λ_b ∈ {1, 10, 100, 1000}; "bigger is better" is false, λ_b = 1000 with Adam at lr 1e-3 stalls because the boundary gradient dominates the update direction. Scaling every λ by 100 changes nothing with Adam but everything with SGD: the ratios matter, not the absolute values.
- Learning-rate annealing (Wang, Teng, Perdikaris 2021, arXiv 2001.04536): λ̂_i = max_θ|∇L_r| / mean_θ|∇L_i|, λ_i ← (1−α)λ_i + αλ̂_i, α = 0.9, every ~10 steps. Diagnostic: the boundary-loss gradients are sharply concentrated around zero compared with the residual's, so the boundary is simply not being trained. Their Fig. 2 histograms make a good panel.
- NTK weighting (Wang, Yu, Perdikaris 2022, arXiv 2007.14527): λ_b = Tr(K)/Tr(K_uu), λ_r = Tr(K)/Tr(K_rr). For u'' = f the residual kernel's eigenvalues dwarf the boundary kernel's, so the residual converges much faster than the boundary. The 1-D Poisson u = sin(4πx): 2.40e-1 → 1.63e-3.
- Inverse-Dirichlet weighting (Maddu et al. 2022, arXiv 2107.00940): weight by inverse gradient *variance*, α ≈ 0.5; effective for multi-scale problems and against forgetting in sequential training.
- Self-adaptive PINNs (McClenny & Braga-Neto, arXiv 2009.04544): one trainable weight per point, gradient ascent on the weights, descent on θ; a soft attention that finds sharp fronts. Allen–Cahn: 0.96 → 0.021. A sharp sigmoid mask can saturate and kill the weight gradient.
- GradNorm (arXiv 1711.02257), SoftAdapt (arXiv 1912.12355), ReLoBRaLo (arXiv 2110.09813, relative loss balancing with random lookback; beats the others on Burgers/Helmholtz/Kirchhoff at lower cost), uncertainty weighting λ_i = 1/(2σ_i²) with a Σ log σ_i regulariser (arXiv 1705.07115; without the log term all weights go to zero).
- Pitfall common to all ratio schemes: blow-up when a term's gradient or variance is near zero; the moving average and ReLoBRaLo's random lookback exist for this.

**Causal training** (Wang, Sankaran, Perdikaris, arXiv 2203.07404): w_i = exp(−ε Σ_{k<i} L_r(t_k)), ε annealed through [1e-2, 1e-1, 1, 10, 100], stop when min_i w_i > 0.99, which doubles as a convergence certificate. A plain PINN minimises the residual at all times at once and typically finds a smooth wrong solution consistent at late times but violating the initial condition; causal weights force information forward in time like a time-stepper. Allen–Cahn: 49.8 % → 1.43e-3 (1.39e-4 with the modified MLP). The expert's guide uses causal weights *inside* each time-marching window too. *Demo:* plot the weight vector as a front advancing from t = 0 to T.

**Gradient-enhanced PINNs** (gPINN, Yu et al. 2022, arXiv 2111.02801): also penalise the derivative of the residual. Needs one derivative order higher. w = 0.01 best for 1-D Poisson; w = 1 is *worse* than a plain PINN, so a w-slider is the honest demo. Fewer collocation points suffice (Poisson with ~15 points).

**Weak forms.** VPINN and hp-VPINN (Kharazmi et al., arXiv 1912.00873, arXiv 2003.05385): test the residual against sin(kπx) or Legendre polynomials, integrate by parts to lower the derivative order; tolerates kinks and discontinuous forcing. Deep Ritz (E & Yu 2018, arXiv 1710.00211): minimise the energy ∫(½|∇u|² − fu) + β∫u² with fresh Monte Carlo points each step; convex, no second derivatives, only for problems with a variational principle (not Burgers).

**Extra physics terms.** Conservation as an extra loss: the undamped oscillator plus |½u'² + ½ω²u² − E₀|²; a plain PINN's amplitude decays over long horizons, the energy-penalised one stays on the circle in phase space. Baty's pendulum needed this. Symmetry losses. Flux continuity across subdomains (cPINN).

**Inverse problems.** Unknown coefficients become trainable scalars beside θ and a data term is mandatory (Raissi 2019 §4.1: Burgers λ₁ = 1, λ₂ = 0.01/π from ~2000 noisy samples). Parametrise positive quantities as exp(s); the parameter estimate lags until u_θ is decent, so plot λ(t); too large a residual weight lets the network "explain" the data by adjusting λ instead of u. Moseley's workshop Task 2 recovers the damping μ from 40 noisy observations (σ = 0.04) by making μ a trainable parameter.

### 2.5 The optimiser

- **Adam then L-BFGS**, the two-stage recipe from Raissi 2019 and DeepXDE. Rathore et al. (arXiv 2402.01868) explain why: the loss Hessian is ill-conditioned because the differential operator is; Adam escapes saddles but crawls along the ill-conditioned valley; L-BFGS approximates Newton and cuts the top Hessian eigenvalue by ≥ 10³ but is attracted to saddles if started cold. Convection β = 40: Adam 5.96e-2, L-BFGS 8.26e-3, Adam + L-BFGS 4.19e-3. L-BFGS fails when the strong-Wolfe line search returns step 0 with gradient norm still 1e-2; in FP32 the convergence test trips prematurely ("set float64"); Xu et al. 2025 (arXiv 2505.10949) argue many Krishnapriyan-style failures are precision stalls.
- **Schedules.** Expert's guide: Adam lr 1e-3, exponential decay ×0.9 every 2000 steps, no weight decay.
- **Second-order and natural-gradient methods.** Energy natural gradient (Müller & Zeinhofer, arXiv 2302.13163): precondition with the Gram matrix of the residual Jacobian in function space; errors several orders below Adam on the same budget. Gauss–Newton natural gradient (arXiv 2402.10680). NysNewton-CG after Adam + L-BFGS (Rathore): convection 4.19e-3 → 1.94e-3, wave 5.52e-2 → 1.27e-2. SOAP / gradient alignment (arXiv 2502.00604, NeurIPS 2025): quasi-second-order methods implicitly align the conflicting loss-term gradients. Frozen random-feature PINNs with a linear solve (arXiv 2405.20836). For a 2×20 network the Gram matrix has a few hundred rows, so energy natural gradient is browser-feasible: Adam 1e-3 relative L² after 10 000 steps versus ~1e-6 after ~100 natural-gradient steps.
- **Curriculum and continuation.** Warm-start from an easy parameter (β, ω, n) and increase it (Krishnapriyan; frequency transfer arXiv 2401.02810); time-marching; multi-fidelity (arXiv 1903.00104).
- **Initialisation.** Glorot with tanh; input and output scaling as in 2.1.
- **Uncertainty.** Ensembles (arXiv 2204.05108: member disagreement as an epistemic band and as the criterion for growing the domain where the residual is applied; NeuralUQ arXiv 2208.11866). Bayesian PINNs (Yang, Meng, Karniadakis 2021, arXiv 2003.06097): HMC over weights and PDE parameters, posterior means beat plain PINNs under large noise; browser-feasible only for a tiny net and a 1-D problem with ~10 noisy observations.

**The expert's guide default recipe, as a checklist** (arXiv 2308.08468, Algorithm 1 and the jaxpi defaults):
1. Non-dimensionalise so inputs, outputs and coefficients are O(1).
2. MLP of 3–6 layers, 128–512 wide (jaxpi 4×256), tanh, Glorot; never ReLU.
3. Random Fourier features, σ ∈ [1, 10].
4. Random weight factorisation μ = 0.5 or 1, σ = 0.1.
5. Loss λ_ic L_ic + λ_bc L_bc + λ_r L_r with weights initialised to 1; hard boundary conditions when possible.
6. Gradient-norm balancing every 1000 steps with EMA α = 0.9 (NTK-trace variant if gradients are noisy); weights stop-gradient'd.
7. Temporal causal weights over 32 chunks, ε = 1; reduce ε if the last weights do not reach 1.
8. Curriculum or time-marching for hard problems, with causal weights inside each window.
9. Adam (0.9, 0.999, 1e-8), lr 1e-3, decay 0.9 every 2000 steps, no weight decay, up to 2e5 steps.
10. Random mini-batch resampling every step, batch 4096; never full-batch fixed points.
Ablation on Allen–Cahn (relative L²): all on 5.84e-4; no Fourier features 4.35e-1; no weight factorisation 6.62e-3; no gradient-norm balancing 7.51e-3; no causal weights 1.59e-3; plain PINN ~5.

---

## 3. Failure modes, with numbers, and the diagnostics that reveal them

| Failure | Where it sets in | Diagnosis | Fix | Source |
|---|---|---|---|---|
| Trivial solution u ≡ 0 | homogeneous ODE with few points or a small IC weight; m u'' = −k u snaps to zero between points | prediction flat between collocation points; IC violated | hard IC; more points; penalise the residual gradient | arXiv 2112.05620 |
| Fixed-point parking | pendulum, T ≥ 5, y₀ = 25°: 0 % success; logistic-type ẏ = y(1−y²) at T ≥ 5: 0–14 % | solution sits on an equilibrium; loss converged | shorter windows; time-marching; curriculum in T | arXiv 2203.13648 |
| BC/residual imbalance | Poisson u = sin(4πx): 24 % error at equal weights | boundary-loss gradients concentrated near zero; K_rr ≫ K_uu | gradient-norm or NTK weighting; hard BC | arXiv 2001.04536; 2007.14527 |
| Spectral bias | u' = cos 15x with 2×16; oscillator at ω₀ = 80 | only the first cycles fit; flat elsewhere | Fourier features; sinusoidal ansatz; FBPINN | arXiv 2107.07871; 1806.08734 |
| Propagation failure | convection β > 10; reaction ρ = 5–10; Allen–Cahn | a wall of large residual just after t = 0 that never moves; smooth wrong late-time solution | causal weights; R3 sampling; time-marching; curriculum in β | arXiv 2109.01050; 2203.07404; 2207.02338 |
| Ill-conditioning | top Hessian eigenvalue 10³ (reaction), 10⁴ (convection), 10⁵ (wave) | Adam plateaus at ~1e-4 while L2RE stays near 1 | L-BFGS after Adam; natural gradient; preconditioning of L*L | arXiv 2402.01868; 2310.05801 |
| Stiffness | ROBER k₂ = 3e7: PINN diverges after t ≈ 10 s; adaptive weights do not help | loss stays high regardless of weighting | log-spaced points; eliminate the fast variable | arXiv 2011.04520 |
| Sharp fronts | Burgers shock | residual concentrated on the front | RAD/RAR; L-BFGS; 10⁴ points | DOI 10.1016/j.jcp.2018.10.045; arXiv 2207.10289 |
| Wrong branch, converged loss | pendulum ω₀ = 25 with 3×32: phase-shifted solution; double-well near the separatrix | true error large while loss is small | energy loss; bigger net; data | arXiv 2302.12260 |
| Adaptive-weight blow-up | any ratio scheme when a term's gradient ≈ 0 | weight traces explode | EMA; random lookback; caps | arXiv 2110.09813 |

**Live diagnostics the tab can show for a 2×20 network, all cheap:**
1. Per-term loss curves on a log axis, with the Adam→L-BFGS switch marked.
2. True error (relative L² and max-abs) against RK4 or the analytic solution on a dense test grid, next to the loss.
3. The residual map |r(x)| (or |r(x, t)| as a heat map); the input to RAD and the first thing to look at.
4. Gradient-norm bars per loss term and the current λ_i.
5. NTK spectra: with 481 parameters and 32 points, K = JJᵀ is 32×32; a Jacobi eigen-solve is trivial, so the eigenvalues of K_uu and K_rr can be plotted live.
6. Stiffness: the top Hessian eigenvalue by power iteration on Hessian-vector products, and the largest stable learning rate 2/σ_max.
7. The causal weight vector as a bar chart; the L-BFGS step size and line-search failure counter.
8. Gradient-alignment cosine between ∇L_r and ∇L_bc.
9. A before/after overlay of the vanilla run for every trick.

---

## 4. Where this touches exoplanets

### 4.1 What has been published

- **Stellar structure and Lane–Emden.** Baty 2023 (Astron. Comput. 44, 100734): polytropes, the isothermal sphere, the Chandrasekhar white-dwarf equation, soft and hard boundary treatments. Baty arXiv 2307.07302: Emden–Fowler equations, soft versus hard. Baty 2024 (arXiv 2403.00599): the hands-on tutorial with Lane–Emden and Grad–Shafranov, *parametric* and *inverse* examples with released code; the closest published template for the site's parametric-n tab. Joel, Harley & Momoniat 2025 (arXiv 2507.03961): the first zero ξ₁ as a trainable eigenvalue, relative errors below 1e-5 for n = 0–3. Ballester et al. 2026 (arXiv 2604.06255): full stellar structure (mass, pressure, density, temperature, luminosity) solved self-supervised, with the equation of state and opacity tables replaced by auxiliary networks, 3.06 % mean error against MESA. Li, Jian, Ting & Green 2025 (arXiv 2507.06357, Kurucz-a1): an emulator of ATLAS-12 atmospheres with hydrostatic equilibrium in the loss, reported to satisfy hydrostatic equilibrium better than ATLAS-12 itself. Bezerra, Dexheimer & Negreiros 2026 (arXiv 2605.31198): a neutron-star analogue of the interior problem, one network for the equation of state and one solving TOV, trained on NICER mass–radius posteriors; the cleanest "PINN as interior inverse solver".
- **Planetary interiors.** No published PINN solves the planetary structure equations for exoplanets. Everything is on the surrogate side: BICEPS (Haldemann et al. 2024, A&A 681, A96); plaNETic (Egger et al. 2024, A&A 688, A223): a feed-forward network with nine inputs to transit radius, trained on 1.5×10⁷ BICEPS structures per envelope case, radius error median within ±0.13 %, 0.035 s per 100 structures versus 23–38 min, at a database cost of ~5 CPU-days × 280; the conditional invertible network of Haldemann et al. 2023 (A&A 672, A180, 5.6×10⁶ structures, pays off only above ~10 planets); ExoMDN (Baumeister & Tosi 2023, A&A 676, A106); and De Wringer, Dorn, Garvin & Marelli 2025 (arXiv 2512.17626), a polynomial-chaos-Kriging surrogate needing only a few hundred forward runs per planet, ×320 inside MCMC, which shows that for a *single* planet a Gaussian-process-type surrogate beats a big network on data efficiency.
- **Atmospheric escape and winds.** Moschou et al. 2023 (MLST 4, 035032): the Euler equations with gravity and a polytropic closure at the heliospheric termination shock. The inverse problem recovered γ exactly from 1500 steady-state points; the forward time-dependent problem *failed* in raw variables (12–168 % errors) until rescaled variables y₁ = r^{2γ}P, y₂ = r²ρ absorbed the inverse-square gravity, and shocks and long integrations remained problematic. This is the best documented "what did not work" for a Parker-like wind. No PINN solving the isothermal Parker/Bondi transonic ODE through the critical point was found. The surrogate side is the site's own reading: Kubyshkina et al. 2018 (A&A 619, A151) is a ~7000-model hydrodynamic grid with a polynomial fit; Kubyshkina & Fossati 2022 evolves planets by interpolating it; MLink (Reza et al. 2025, arXiv 2502.01510) replaces the interpolation with a network over ~11 000 models; Rogers et al. 2023 (MNRAS 519, 6028) emulate atmospheric evolution at ~10³ speed-up. The mass-loss fit in the escape tab *is* an emulator.
- **Orbits.** Hamiltonian neural networks with the two-body problem as the headline test (arXiv 1906.01563); Wisdom–Holman splitting with a neural interaction Hamiltonian for 10⁵-step three-body integrations (arXiv 2111.15631); matched-integrator evaluations on 3-D Kepler (arXiv 2608.10235); PINNs recovering periodic three-body orbits from sparse noisy data, with the authors' caveat that PINNs remain slower than integrators on well-posed initial-value problems (arXiv 2607.23501).
- **Radiative transfer, MHD, cosmology.** PINNs for forward and inverse radiative transfer (Mishra & Molinaro 2021, JQSRT 270, 107705); nonlinear force-free coronal fields (Jarolim et al. 2023, Nat. Astron. 7, 1171); Grad–Shafranov and reconnection equilibria with "modest accuracy compared to FEM" (Baty & Vigon 2024, MNRAS 527, 2575); cosmological "solution bundles", one network over a parameter range for several dark-energy models (Chantada et al. 2023, PRD 107, 063523) and a PINN Friedmann solver inside an emcee likelihood (arXiv 2508.12032). No PINN of the lens equation was found.

### 4.2 The three paradigms, side by side

| | PINN | Supervised surrogate / emulator | Neural operator |
|---|---|---|---|
| What is learned | one solution u(x), or a family u(x; λ) with λ as input | parameters → outputs of a simulator | an input *function* → a solution function |
| Training data | none (the residual), optionally sparse observations | millions of runs (plaNETic 1.5×10⁷; cINN 5.6×10⁶), or hundreds for GP/PCK | thousands of function pairs; physics-informed DeepONet removes the need (Wang, Wang, Perdikaris 2021, Sci. Adv. 7, eabi8605) |
| Cost | training per problem is usually *slower* than an ODE/FEM solve (Grossmann et al. 2024, arXiv 2302.04107) | expensive offline, microseconds online | expensive offline, milliseconds online, resolution-invariant |
| Accuracy | 1e-3 to 1e-5 relative on smooth ODEs; degrades at shocks, stiffness, multi-scale | bounded by training coverage; plaNETic ±0.5 % in radius | ~1–3 % typical; fails outside the input-function distribution |
| Generalisation | inside the trained domain and parameter range only | interpolation only; silent failure at grid edges (MLink was built to fix this) | across functions within the training measure |
| Wins when | few or no data; a differentiable solution is needed; a parameter or eigenvalue is wanted jointly with the solution; an inverse problem with sparse noisy data | a fixed forward model must be called 10⁴–10⁷ times inside MCMC (the Dorn 2017 setting) | the input is itself a function (an EoS table, an opacity profile, an XUV time series) |
| Examples on this site | Baty tab | Moseley tab; plaNETic in the Egger tab; the escape fit | (none yet) |
| Hybrids | physics-informed DeepONets; Kurucz-a1 (emulator + hydrostatic loss); a PINN as the forward model inside MCMC (arXiv 2508.12032) | | |

The Bern reading of this table: plaNETic and the cINN are emulators because the expensive part is the repeated forward call inside Bayesian sampling. A PINN helps there only in the emulator slot, where the residual becomes a consistency regulariser guaranteeing hydrostatic equilibrium (the Kurucz-a1 pattern) rather than a replacement for the training set.

### 4.3 Exoplanet-flavoured 1-D demo problems

| Problem | Equation | Reference solution | Trick it demonstrates | Link to the reading list |
|---|---|---|---|---|
| Lane–Emden family (built) | θ'' + (2/ξ)θ' + θⁿ = 0 | n = 0, 1, 5 analytic | parametric input n; hard constraint 1 + ξ²N kills the origin singularity; ξ₁ as an eigenvalue | Baty 2023 |
| Polytropic planet, mass–radius | dP/dr = −Gmρ/r², dm/dr = 4πr²ρ, P = Kρ^{1+1/n} | Lane–Emden by rescaling; R ∝ M^{(1−n)/(3−n)} | two coupled *first-order* outputs; loss balancing between equations; scan K or n to draw the M–R curve | Alibert 2016; Egger 2024 (a miniature BICEPS) |
| Isothermal scale height | dP/dz = −ρg, P = ρkT/μm_H | P₀ e^{−z/H} | the trivial baseline; log-output parametrisation for exponential range | Kubyshkina & Fossati 2022 |
| Isothermal Parker wind | (v² − c_s²)(1/v)dv/dr = 2c_s²/r − GM/r² | Lambert-W closed form (Cranmer 2004, AJP 72, 1397) | a singular critical point: the plain residual admits breeze and unphysical branches; pin v(r_s) = c_s as a hard constraint or transform variables as Moschou did | Kubyshkina & Fossati 2022 |
| Kepler two-body | r'' = −r/|r|³ | ellipse | extra conservation losses (E, L); compare with an HNN that conserves by construction | Greydanus 2019 |
| Newton cooling / decay | dT/dt = −k(T − T_env) | exponential | inverse problem: recover k from 5 noisy points; stiffness at large k | Kubyshkina & Fossati 2022 |
| 1-D thermal diffusion in a sphere | ∂T/∂t = κ r⁻² ∂_r(r² ∂_r T) | Bessel/sine series | space–time collocation; causal training; spectral bias against a sharp initial profile | Dorn 2017 |
| Jeans escape flux | closed form | closed form | not an ODE: shows when a PINN is the wrong tool | Gas escape tab |
| Toy envelope radius evolution | dR/dt = −(R − R_core)/τ_KH(R) + escape | numerical | two regimes; parametric family in the initial envelope fraction | Kubyshkina & Fossati 2022; Rogers 2023 |

The Parker wind is the one to feature: it is the only 1-D problem on this list where the naive PINN *genuinely* fails (several branches through the critical point), it has an exact Lambert-W answer to plot against, and it is the physical core of the escape models on the site.

### 4.4 Inverse problems and the Bayesian link

Standard PINN inversion adds the unknown scalars (n, K, γ, Ṁ) to the trainable parameters and a data misfit to the loss. The output is a point estimate; the degeneracies of Dorn 2017 are invisible to it. Bayesian PINNs (Yang, Meng, Karniadakis 2021, JCP 425, 109913) put a prior on the weights and the parameters and sample with HMC. The efficient path, taken by the cosmology papers, is to train one parametric PINN bundle over (n, K, Ṁ) and then run MCMC over the bundle's inputs: that reproduces the Dorn/BICEPS architecture with the PINN in the emulator slot, and makes the trade-off of Section 4.2 explicit.

---

## 5. Feasibility in the hand-written browser network

### 5.1 The cost model

With forward-mode jets each neuron carries 1 + K numbers, K being the number of tracked derivative components. One input to second order: K = 2 (what the Baty tab does). Third order in one variable: K = 3. Two inputs to second order: K = 5 (u_x, u_t, u_xx, u_xt, u_tt), or K = 3 for heat and Burgers (u_x, u_t, u_xx). Forward cost is roughly (1 + K) × parameters per point and the hand-derived backpropagation through the jets costs a similar multiple. Third-order mixed derivatives (gPINN on a 2-D PDE) would need K = 9, which is where hand-derived jets stop being pleasant.

### 5.2 Measured step rates

A reimplementation of the site's setup (2×20 tanh, Lane–Emden residual, Adam) run in JavaScriptCore; browser JITs land within a factor of ~2.

| Configuration | Steps per second |
|---|---|
| 2×20, N = 32, K = 2 (the current page) | ~7 000 |
| 2×20, N = 200, K = 2 | ~1 200 |
| 2×20, N = 32 / 200, K = 3 (third derivative) | ~6 000 / ~1 000 |
| 2×20, N = 32 / 200, K = 5 (two inputs, full Hessian) | ~4 300 / ~700 |
| 2×40, N = 200, K = 2 | ~350 |
| 2×20, N = 1000, K = 2 | ~250 |

A station can therefore afford 10⁴–10⁵ steps within seconds at 32–200 points, more than Baty's 32 000 steps. Anything at ≥ 1000 points or 4+ layers of 40 becomes a "watch for a minute" demo.

### 5.3 Feasibility per trick

| Trick | Derivatives needed | Extra machinery | Browser cost | Feasible |
|---|---|---|---|---|
| Manual loss weighting | y', y'' | none | 1× | yes |
| Hard constraints (Lagaris ansatz) | chain rule through the ansatz | none | 1× | yes (already done) |
| More / resampled / RAR / RAD collocation | y', y'' | residual on a dense grid every k steps | ~1× | yes |
| Fourier or sin features; the sin(αt+β) ansatz | derivatives of the embedding | none | 1× | yes |
| Adaptive activation; input and output scaling | same | none | 1× | yes |
| Gradient-norm balancing | per-term gradient norms | one backward pass per term | ~2× | yes |
| NTK weighting and spectra | per-sample gradients of residual and BC | K = JJᵀ is 32×32 for 481 parameters; Jacobi eigen-solve | ~1.5× every 10–100 steps | yes, including live eigenvalues |
| Self-adaptive per-point weights | y', y'' | one weight per point, gradient ascent | 1× | yes |
| Causal weights; time-marching; curriculum in a parameter | y', y'' | ordering of points; continuation | 1× | yes |
| gPINN | y''' (K = 3) | one more jet term (Faà di Bruno for tanh) | ~1.2× | yes, 1-D only |
| Adam → L-BFGS | y', y'' | two-loop recursion, history 10–20, backtracking or Wolfe line search (5–20 extra loss evaluations per iteration) | ~10× per iteration, far fewer iterations | yes |
| Energy natural gradient | per-sample residual Jacobian | dense Gram solve, a few hundred rows | moderate | yes, for a 2×20 net |
| Domain decomposition (2–4 subnets, FBPINN windows) | y', y'' per subnet | window functions; interface continuity for XPINN | ~N_sub× | yes |
| Parametric input (x, n) | y', y'' in x only | none | 1× | yes (already done) |
| Inverse problem: learn n from noisy data | ∂residual/∂n = ξ·θⁿ ln θ | one extra parameter; clamp θ > 0 | 1× | yes |
| (x, t) PDE: heat, Burgers (K = 3), wave (K = 5) | u_x, u_t, u_xx (, u_tt) | two-input jets, hand-derived mixed chain rule | 0.6–0.8× of the K = 2 rate | yes, a second derivation effort |
| Hamiltonian NN for the oscillator | ∂H/∂q, ∂H/∂p through the net | first derivatives only, plus an integrator | 1× | yes |
| Bayesian PINN by HMC | gradients of the log posterior | leapfrog sampler over 481 weights | slow but tolerable for one panel | marginal |
| Higher-order mixed derivatives; 4th-order PDEs in (x, t) | K ≥ 9 | heavy jet algebra | slow, error-prone | not recommended |
| Large nets (≥ 4×64), > 2000 points, 2-D + time | | | minutes to hours | no |

Two implementation notes from the site's own experience. First, the Baty tab already propagates (a, da/dx, d²a/dx²) triples per neuron with hand-derived backpropagation; every trick above marked 1× reuses that machinery unchanged. Second, the polytropic-planet capstone is two coupled *first-order* ODEs, so it needs K = 1 and is cheaper than anything on the Lane–Emden page.

---

## 6. The proposed tab: fourteen stations

The order follows the sources: every course puts a plain ODE first, failures before fixes, weighting and sampling before architecture tricks, the optimiser and decomposition late, and the inverse problem last as the bridge to the surrogate tabs. Each station: one problem, one dial, one trick, one before/after switch, and true error beside the loss.

| # | Station | Problem and dial | Trick, and the before/after | What the learner sees | Sources |
|---|---|---|---|---|---|
| 1 | The simplest PINN | u' = cos ωx, ω = 1; then y' = −ky | the residual as the only supervisor; hard IC ŷ = 1 + t·N | loss and true error side by side; the seed control; the trivial solution when the IC weight is dropped | arXiv 2107.07871; Lagaris 1998; arXiv 2112.05620 |
| 2 | What autodiff is doing | one neuron of the Lane–Emden net | expose the jets (y, y', y''); toggle finite differences vs exact jets | noise in y'' from finite differences; why tanh and never ReLU | expert's guide §4.1 |
| 3 | Why it fails I: wrong answer, small loss | logistic with horizon T = 2.5 → 7.5; pendulum | curriculum in T; energy loss | success-rate collapse from 100 % to 0 %; the fixed-point trap; the phase-shifted pendulum | arXiv 2203.13648; 2302.12260 |
| 4 | Why it fails II: unbalanced gradients | Poisson a = 1 → 4 with soft BCs | gradient-norm balancing; NTK weights | per-term gradient-norm bars; the NTK eigenvalue bars for K_uu vs K_rr; 24 % → 0.2 % | arXiv 2001.04536; 2007.14527 |
| 5 | Where to put the points | Poisson or a steep-front ODE, N = 8 → 200 | Random-R, RAD, self-adaptive weights | the residual map; points and weights migrating to the front | arXiv 2207.10289; 2009.04544 |
| 6 | Spectral bias | u' = cos ωx, ω = 1 → 15; oscillator ω₀ = 20 → 80 | Fourier features; the sin(αt+β) ansatz | 2×16 fails, same net with features fits; error per frequency band | arXiv 1806.08734; 2006.10739; 2012.10047; Moseley Task 3 |
| 7 | Many small nets beat one big one | u' = cos 15x; u' = cos x + 15 cos 15x | FBPINN with 4–8 windowed subnets vs one net | the window functions; parameters vs error | arXiv 2107.07871 |
| 8 | Curriculum and causality | convection β = 1 → 30 (K = 3), or Lane–Emden n stepped 0 → 4 | curriculum in β or n; causal weights along t or ξ | the causal weight front advancing; relative error vs β with and without curriculum | arXiv 2109.01050; 2203.07404 |
| 9 | The optimiser | any of the above at fixed wall-clock | Adam vs Adam + L-BFGS; energy natural gradient | loss vs wall-clock *and* vs step; the top Hessian eigenvalue; the FP32 stall | arXiv 2402.01868; 2302.13163 |
| 10 | Gradient-enhanced loss | Poisson with 15 points | gPINN with a w-slider | fewer points suffice at w = 0.01; w = 1 hurts | arXiv 2111.02801 |
| 11 | Non-dimensionalise or die | a planet's hydrostatic ODE in SI units | rescale to O(1) | Adam stalls in metres and kg m⁻³, converges dimensionless | expert's guide step 1 |
| 12 | The singular point | isothermal Parker wind | v(r_s) = c_s as a hard constraint; transformed variables | breeze and unphysical branches vs the transonic Lambert-W solution | Cranmer 2004; Moschou 2023 |
| 13 | Capstone A: a parametric planet | polytropic hydrostatic planet, (r, n) or (r, K) as inputs, two first-order outputs | parametric PINN; loss balancing between equations | the mass–radius curve vs RK4; interpolation inside the trained range, failure outside | Alibert 2016; Egger 2024; Baty 2024 |
| 14 | Capstone B: the inverse problem | recover n, or the core-mass fraction, from noisy θ(ξ) or (M, R) samples | a trainable parameter with a data loss; an ensemble over seeds as a poor man's posterior | λ(t) lagging then locking; identifiability as loss-vs-n; the spread across seeds vs Dorn's MCMC | Moseley Task 2; Yang 2021; Dorn 2017 |

Stations 1–7 and 9–14 need only the K = 2 jets already on the site (station 10 needs K = 3, station 8's convection variant needs the two-input jets or can use the Lane–Emden n-curriculum instead). Station 12 is the exoplanet-specific highlight; station 13 is the miniature BICEPS that closes the loop to the Egger tab; station 14 hands over to the surrogate discussion in the Moseley and Egger tabs.

**Rules for honest demos**, distilled from PINNacle, Rathore et al. and the tutorials:
- Always show true error (relative L² and max-abs against RK4 or the analytic solution on a dense test grid, not on the collocation points) beside the training loss. Loss must reach ~1e-4 or lower before the true error drops; PINNacle lists cases where the loss is near zero and the relative error near one.
- Compare at equal step counts *and* equal wall-clock; per-iteration costs differ across optimisers.
- Fix the seed and show the median of five seeds; both PINNacle and Rathore plot per-seed scatter.
- Change one thing at a time; tune the "before" branch as carefully as the "after".
- Build the trivial-solution and fixed-point traps into the first stations on purpose, so the learner meets "converged loss, wrong answer" before meeting any fix.
- Keep Chuang & Barba (SciPy 2022, arXiv 2205.14249) in the footer as the cautionary tale: 32 hours of PINN training to match a 20-second 16×16 finite-difference run.

---

## 7. Existing material, annotated

| Material | Teaches | Lacks |
|---|---|---|
| Moseley, "So, what is a physics-informed neural network?" (benmoseley.blog) and the notebook github.com/benmoseley/harmonic-oscillator-pinn | damped oscillator, 3×32 tanh, 30 physics points, physics weight 1e-4, 20 000 Adam steps; a data-only net extrapolates badly; "very sensitive to the relative weighting" | one trick only; no error metric; no failure analysis |
| Moseley workshop (github.com/benmoseley/harmonic-oscillator-pinn-workshop), same content as the ETH DLSC 2023 lecture "PINNs, applications" (Mishra & Moseley) | Task 1 simulate; Task 2 invert for μ from 40 noisy points; Task 3 ω₀ = 80 and spectral bias, fixed by the sin(αt+β) ansatz; loss terms have different units | no Fourier features, adaptive weights or L-BFGS |
| DeepXDE demos (deepxde.readthedocs.io) and Lu et al. 2021, SIAM Rev. 63, 208 | order: ODE systems → Poisson/beam/Helmholtz → Burgers, heat, Allen–Cahn, wave, Schrödinger; hard BCs via output transform, RAR, Fourier features, resampling, Adam→L-BFGS; the Lotka–Volterra demo is a compact "all tricks" example | the library hides the derivatives; no before/after |
| Brown APMA 2070 (Karniadakis; github.com/raj-brown/APMA_2070_ENGN_2912_SPRING_2024) | DL basics → optimisation → equation discovery → PINNs I/II → DeepXDE → DeepONet → multi-fidelity → UQ | no interactive component |
| NVIDIA PhysicsNeMo recommended practices | non-dimensionalise; integral continuity; SDF-based loss weighting near sharp gradients; denser points where variation is expected; exact continuity via vector potential; symmetry | GPU-scale, nothing in a browser |
| Thuerey et al., *Physics-based Deep Learning* (physicsbaseddeeplearning.org) | Burgers PINN with 8×20 tanh, 1000 collocation points: "the shock in the center is not well represented", "a surprisingly large number of iterations"; the discussion chapter calls PINNs "a step backwards in some way" relative to differentiable physics | deliberately sceptical; teaches no fixes |
| Reviews: Karniadakis et al. 2021 Nat. Rev. Phys. 3, 422; Cuomo et al. 2022 J. Sci. Comput. 92 (arXiv 2201.05624); Cai et al. 2021 (fluids, heat transfer); Wang et al. 2023 "An expert's guide" (arXiv 2308.08468) | the expert's guide is the closest thing to a syllabus of tricks, with the ablation table quoted in Section 2.5 | JAX and large networks |
| Baty 2023 Astron. Comput. 44, 100734; arXiv 2307.07302; arXiv 2403.00599 | Lane–Emden, soft vs hard, Emden–Fowler, Grad–Shafranov, parametric and inverse examples; "a too large architecture can even degrade the precision" | no systematic trick comparison |
| In-browser: Lane–Emden PINN Lab (saoneenandi.github.io/lane-emden-pinn) | TF.js, tanh MLP, forward-mode jets exactly like the Baty tab, equation multiplied by x, sliders for n and network size, eigenvalue mode for the first zero | no before/after stations |
| TensorFlow Playground (Smilkov & Carter 2016) | the design precedent: a tiny hand-written network trained in real time | not physics |
| Explorables: Tancik et al. Fourier features project page (bmild.github.io/fourfeat); Distill "Why momentum really works" | NTK bandwidth visual; optimiser intuition | no Distill-style PINN explorable exists |
| Courses: MIT 18.337 (PINNs in lecture 1, then AD and neural ODEs); Oxford "Physics Informed Neural Networks" (Kay); Steve Brunton's PINN video (the five injection points: problem, data, architecture, loss, optimiser) | the organising axis used in Section 2 | |

---

## 8. Consolidated references

Foundations and tutorials: Lagaris, Likas & Fotiadis 1998, IEEE TNN 9, 987 (DOI 10.1109/72.712178; arXiv physics/9705023). Raissi, Perdikaris & Karniadakis 2019, JCP 378, 686 (DOI 10.1016/j.jcp.2018.10.045; arXiv 1711.10561). Karniadakis et al. 2021, Nat. Rev. Phys. 3, 422. Cuomo et al. 2022, J. Sci. Comput. 92 (arXiv 2201.05624). Wang, Sankaran, Wang & Perdikaris 2023, "An expert's guide to training PINNs" (arXiv 2308.08468). Lu et al. 2021, DeepXDE, SIAM Rev. 63, 208 (arXiv 1907.04502). Hao et al. 2023, PINNacle (arXiv 2306.08827). Baty 2023, Astron. Comput. 44, 100734; Baty arXiv 2302.12260, 2307.07302, 2403.00599.

Failure modes: Rahaman et al. 2019 (arXiv 1806.08734); Xu et al. (arXiv 1901.06523); Wang, Teng & Perdikaris 2021, SISC 43, A3055 (arXiv 2001.04536); Wang, Yu & Perdikaris 2022, JCP 449, 110768 (arXiv 2007.14527); Krishnapriyan et al. 2021, NeurIPS (arXiv 2109.01050); Leiteritz & Pflüger (arXiv 2112.05620); Rohrhofer et al. 2023, TMLR (arXiv 2203.13648); Daw et al. 2023, ICML (arXiv 2207.02338); Ji et al. 2021, Stiff-PINN (arXiv 2011.04520); Rathore et al. 2024 (arXiv 2402.01868); De Ryck et al. (arXiv 2310.05801); Mishra & Molinaro (arXiv 2006.16144); Xu et al. 2025 (arXiv 2505.10949); Chuang & Barba 2022 (arXiv 2205.14249); Grossmann et al. 2024 (arXiv 2302.04107).

Loss: Sukumar & Srivastava 2022 (arXiv 2104.08426); Lu et al. hPINN (arXiv 2102.04626); McClenny & Braga-Neto (arXiv 2009.04544); Maddu et al. 2022 (arXiv 2107.00940); Chen et al. GradNorm (arXiv 1711.02257); Heydari et al. SoftAdapt (arXiv 1912.12355); Bischof & Kraus ReLoBRaLo (arXiv 2110.09813); Kendall, Gal & Cipolla (arXiv 1705.07115); Wang, Sankaran & Perdikaris causal training (arXiv 2203.07404); Yu et al. gPINN (arXiv 2111.02801); Kharazmi et al. VPINN (arXiv 1912.00873), hp-VPINN (arXiv 2003.05385); E & Yu Deep Ritz (arXiv 1710.00211); Wu et al. 2023 sampling (arXiv 2207.10289); Nabian et al. (arXiv 2104.12325); Jagtap, Kharazmi & Karniadakis cPINN (DOI 10.1016/j.cma.2020.113028).

Architecture: Leake & Mortari TFC (arXiv 1812.08625); Dong & Ni 2021 (arXiv 2007.07442); Rao, Sun & Liu (arXiv 2002.10558); Richter-Powell, Lipman & Chen (arXiv 2210.01741); Greydanus et al. HNN (arXiv 1906.01563); Cranmer et al. LNN (arXiv 2003.04630); Jin et al. SympNets (arXiv 2001.03750); Tancik et al. (arXiv 2006.10739); Wang, Wang & Perdikaris 2021 (arXiv 2012.10047); Sitzmann et al. SIREN (arXiv 2006.09661); Wong et al. (arXiv 2109.09338); Wang et al. RWF (arXiv 2210.01274); Jagtap, Kawaguchi & Karniadakis (arXiv 1906.01170, 1909.12228); Maczuga & Paszyński 2023 (DOI 10.1007/978-3-031-35995-8_6); Wang, Li, Chen & Perdikaris PirateNets (arXiv 2402.00326); Shahab et al. (arXiv 2602.08515); Jagtap & Karniadakis XPINN (DOI 10.4208/cicp.OA-2020-0164); Moseley, Markham & Nissen-Meyer FBPINN (arXiv 2107.07871); Wight & Zhao (arXiv 2007.04542); Mattey & Ghosh bc-PINN (arXiv 2106.07606); Gladstone et al. FO-PINN (arXiv 2210.14320); Schiassi et al. (arXiv 2005.10632); Lu, Jin & Karniadakis DeepONet (arXiv 1910.03193); Li et al. FNO (arXiv 2010.08895); Wang, Wang & Perdikaris PI-DeepONet (arXiv 2103.10974).

Optimisation and uncertainty: Müller & Zeinhofer (arXiv 2302.13163); Jnini, Vella & Zeinhofer (arXiv 2402.10680); Wang et al. SOAP (arXiv 2502.00604); Datar et al. (arXiv 2405.20836); Mustajab et al. (arXiv 2401.02810); Meng & Karniadakis MPINN (arXiv 1903.00104); Haitsiukevich & Ilin (arXiv 2204.05108); Zou et al. (arXiv 2503.06320, 2208.11866); Yang, Meng & Karniadakis B-PINN (arXiv 2003.06097).

Astrophysics and exoplanets: Joel, Harley & Momoniat 2025 (arXiv 2507.03961); Ballester et al. 2026 (arXiv 2604.06255); Li, Jian, Ting & Green 2025 (arXiv 2507.06357); Bezerra, Dexheimer & Negreiros 2026 (arXiv 2605.31198); Haldemann et al. 2024, A&A 681, A96; Egger et al. 2024, A&A 688, A223 (arXiv 2406.18653); Haldemann et al. 2023, A&A 672, A180 (arXiv 2202.00027); Baumeister & Tosi 2023, A&A 676, A106 (arXiv 2306.09002); De Wringer et al. 2025 (arXiv 2512.17626); Moschou et al. 2023, MLST 4, 035032; Kubyshkina et al. 2018, A&A 619, A151 (arXiv 1809.06645); Kubyshkina & Fossati 2022, A&A 668, A178 (arXiv 2211.10166); Reza et al. 2025 (arXiv 2502.01510); Rogers et al. 2023, MNRAS 519, 6028 (arXiv 2110.15162); Cai, Portegies Zwart & Podareanu 2021 (arXiv 2111.15631); Nyabuto et al. 2026 (arXiv 2608.10235); Kollias & Matzakos 2026 (arXiv 2607.23501); Mishra & Molinaro 2021, JQSRT 270, 107705 (arXiv 2009.13291); Jarolim et al. 2023, Nat. Astron. 7, 1171; Baty & Vigon 2024, MNRAS 527, 2575; Chantada et al. 2023, PRD 107, 063523 (arXiv 2205.02945); Verma et al. 2025 (arXiv 2508.12032); Flores et al. 2025 (arXiv 2505.06459); Cranmer 2004, AJP 72, 1397 (arXiv astro-ph/0406176); Dorn et al. 2017, A&A 597, A37 (arXiv 1609.03908); Alibert 2016, A&A 591, A79.

## 9. Open items and unverified claims

- The internal numbers of Baty 2023 (Astron. Comput.) were taken from abstracts and search snippets; the DOI is confirmed, the n range and error percentages are not.
- The stiff two-scale system of rung 8 is this report's own construction, not a published benchmark; ROBER is the published one.
- No Kepler, Riccati or Parker-wind PINN benchmark exists in the literature as far as the search found; the Parker station would be original work.
- NVIDIA PhysicsNeMo's PINN-specific loss-weighting details, the physics content of Johnson et al. 2023 (LNCS 13645), and the details of Nakao et al. 2026 (JGR-MLC) could not be opened.
- Exact venues for Müller & Zeinhofer (ICML 2023) and Rathore et al. (ICML 2024) were cited from the arXiv listings, not the proceedings.
- The step rates in Section 5.2 come from an untuned JavaScriptCore reimplementation of the Baty tab's network and should be re-measured in the real page once a station exists.
