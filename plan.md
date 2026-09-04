# Interior characterisation from first principles: a plan

Drinor Cacaj, University of Bern. Drafted 3 September 2026 after a close reading of Egger et al. 2024 and the Volatile Worlds companion; revised 4 September 2026 after Leleu 2021, Mishra 2023 and Davoult 2024. This is a working plan, not a proposal: it says what to build, in what order, what each piece must prove before the next one starts, and what would show it was wrong.

**Change log, 4 September 2026.**
- Added principle 9: statistics are the object of inference, individual systems are not.
- Added section 2b, the fixed-versus-improvable split of the pipeline, which is what an automated search is allowed to touch.
- Added WP6, a metric for scoring formation models: a penalised, bias-forwarded population likelihood validated on held-out surveys, with mutual information as the usefulness measure. Old WP6 to WP8 are now WP7 to WP9.
- WP2: BICEPS is not public; the structure integration is to be reimplemented on the public equations of state, and TOI-178 d becomes a test case for the evolution surrogate.
- Section 6 updated: the three formerly unread papers and what they actually contribute.
- Section 7: question 1 answered; two questions added.
- Timeline: WP3 given its own phase; the scoring package placed in phase IV.

---

## 0. Purpose

Answer, for a transiting planet with a measured mass, radius, period and host star, the question *what is it made of*, and in particular *how much water does it hold*, in a way that

- separates what the data determine from what the assumptions supply, in the structure of the result rather than in a caveat;
- counts every measurement exactly once;
- can absorb a new observable without a new method;
- scales from one planet to the population that answers the radius-valley question;
- is calibrated, meaning its stated uncertainties are the uncertainties it actually has.

The Egger et al. pipeline reaches most of these goals in its discussion. The plan makes them the form of the analysis.

---

## 1. The problem, stated precisely

**Observables.** Transit depth δ (from the light curve, marginalised over systematics), RV semi-amplitude K, period P, and the host star's radius, mass, effective temperature, age and Fe, Si, Mg abundances. Optionally: an atmospheric spectrum, an asteroseismic age, a measured stellar density from the transit shape.

**Parameters, per planet.** Mass fractions of core, mantle, water and H/He; water share of the envelope Z; core iron fraction; mantle Si and Mg fractions; intrinsic luminosity; equilibrium temperature. Nine numbers reach the forward model.

**Forward model.** A hydrostatic structure integration with temperature transport and an irradiated atmosphere, closed by tabulated equations of state, returning the transit radius at chord optical depth 2/3. BICEPS is the reference implementation but is not public; the working reference will be a reimplementation on the public equations of state (AQUA, Chabrier 2019, Sotin 2007, Hakim 2018), validated against the published plaNETic surrogate. A neural surrogate of that reimplementation is the working model.

**The degeneracy.** The map from composition to (M, R) has a null direction: water can be traded for H/He at almost constant radius. It is structural, not instrumental. No radius precision closes it. Along that direction the likelihood is flat and any posterior statement is the prior.

**What is nonetheless determined.** Bulk density, hence the mass of rock plus core to a few percent; whether a volatile layer is required at all; the total volatile thickness under a given envelope composition; and, for hot super-Earths, an upper limit on H/He that is orders of magnitude below what accretion supplies.

---

## 2. Principles

1. **Identifiability before inference.** Compute what the data can constrain before asking what they say. Report the constrained combinations prior-free, then the conditional posteriors.
2. **Every measurement is used once.** A datum is either in the likelihood or in the prior, never both. Priors are fixed and logged before the planet's data are opened.
3. **A prior is a model with an error budget.** Hard cutoffs are replaced by distributions with a source; every informative prior is run beside a reference prior; the evidence of each is reported.
4. **The forward model must be cheap and differentiable.** Ten to a hundred million evaluations per planet, with gradients, so that brute-force sampling, Hamiltonian sampling and Fisher analysis are all available.
5. **Correlations are kept.** Siblings share a star; depth trades against impact parameter; the light-curve posterior is joint. Nothing is summarised into independent Gaussians unless shown to be harmless.
6. **The population is the object.** Single planets sit on the ridge; the fraction of planets born beyond the iceline is measurable only across many. The individual analysis must be designed so that a hierarchical layer can be placed on top without rewriting it.
7. **Calibration is a deliverable.** Credible intervals are tested by injection and recovery. A method that cannot be calibrated is not finished.
8. **Say what is toy and what is real,** in every figure and every table.
9. **Statistics are the object, systems are not.** The map from a disk to one system passes through a chaotic phase whose outcome is a random draw; the map from disk properties to the distribution of systems is smooth and compressible. No gate in this plan may depend on reproducing a particular system, and no prior may be tuned to one.

---

## 2b. What is fixed and what may be improved

The pipeline has parts that no amount of work changes and parts that are legitimately open. Stating the split once makes an automated search over the open parts well posed: a proposal that touches a fixed box is rejected before it is scored.

| Fixed | Improvable |
|---|---|
| The measurements and their published errors, for a given instance | The noise models and systematics treatment that turn raw fluxes into likelihoods |
| The number and meaning of the composition parameters (nine per planet) | The priors on them, their sourcing, their tempering |
| The physics equations: hydrostatic balance, energy transport, the equations of state as published | The prescriptions inside the forward model: atmosphere boundary, mixing, escape efficiency, migration and capture laws |
| The detection function of a survey, treated as an instrument property | The surrogate that emulates the forward model, its architecture, its domain, its error contract |
| The definition of the observables entering the likelihood | The summary statistics used to compare populations, and their weights |
| The rejection-sampling and Bayesian machinery | The formation model that supplies population priors, and its free constants |

Everything in the right column has a score in WP6 or a gate in its own work package. Everything in the left column is a boundary condition.

---

## 3. Work packages

Each package lists its deliverable, the check that gates the next package, and the risk that would make it fail.

### WP1 · Identifiability analysis

**Build.** For a given planet and forward model, the Jacobian of the observables with respect to all composition parameters, and from it the Fisher information, its eigen-decomposition, the null space and the well-conditioned combinations. A map of the null direction across the (M, R, T_eq) plane.

**Deliverable.** A short paper-style note: which combinations of composition are measured by (M, R) alone, to what precision, for the observed sub-Neptune population; and a figure of the ridge orientation as a function of location on the mass–radius diagram.

**Gate.** The prior-free constrained combinations for HIP 29442 b, c, d agree with the Egger posteriors where the posteriors are prior-independent (bulk rock mass, envelope required or not, H/He upper limits on c and d).

**Risk.** The Jacobian of a tabulated-EoS model is noisy at phase boundaries. Mitigation: compute it on the surrogate, which is smooth, and check against finite differences of the full model at a handful of points.

**Prototype.** The cancellation map of the Photobombing tab is this object in two dimensions with a toy model.

### WP2 · A differentiable, evolving forward model

**Build.** A neural surrogate of the structure model, as in plaNETic, with three additions.

- *Gradients.* The surrogate returns dR/dθ by automatic differentiation; gradient correctness is tested against finite differences on the full model.
- *Time.* The surrogate, or a second one chained to it, emulates thermal evolution plus escape, so that the envelope today is a function of the envelope at disk dispersal, the stellar XUV history and the age. The "initial envelope" and "rotation history" become parameters with formation and stellar priors, and today's envelope stops being a free log-uniform knob.
- *Domain and error contract.* A stated range of validity in mass, temperature, composition; an error histogram measured on the *posterior region* of real planets, not on held-out training draws; a hard refusal outside the domain.

**Deliverable.** A versioned surrogate with a data card: training set, priors used to generate it, error percentiles inside the domain, gradient test results, cost per call.

**Gate.** Error below 0.5 percent at the 84th percentile on 100 posterior structures per planet, rerun through the full model, for a set of at least five well-measured systems; gradient agreement to one part in a thousand. For the evolution part, a qualitative test on TOI-178: planets b and c stripped, planet d marginal with its nominal mass, e to g retained, with the K-dwarf XUV history; if d's hydrogen envelope survives comfortably, the escape prescription is too weak.

**Access.** BICEPS itself is not needed for this package. The structure integration is a shooting solution of a boundary-value problem with published equations of state; reimplementing it is a few weeks of work, and the plaNETic surrogate is a public check on the result. The ask to the group is the training set, not the code.

**Risk.** Emulating evolution multiplies the input dimension and the training cost. Mitigation: emulate the evolved envelope fraction as a separate small network conditioned on core mass, orbit, initial fraction and XUV dose, then feed it to the structure surrogate.

**Prototype.** The plaNETic tab's §3 network and the Radius valley tab's evolution engine, joined.

### WP3 · Joint inference from raw data

**Build.** One sampler over the composition, the stellar parameters and the light-curve and RV nuisance parameters, with the flux points and RV points as the data. The transit depth is an intermediate quantity computed from the composition through WP2. Hamiltonian Monte Carlo, made feasible by WP2's gradients. The stellar density from the transit shape enters as a second constraint on the star alongside the flux-method radius and the isochrone mass.

**Deliverable.** Joint posteriors for multi-planet systems that preserve the correlations between siblings and between depth and geometry; a comparison with the two-stage pipeline on HIP 29442 showing where the summaries lost information.

**Gate.** On simulated systems the joint fit recovers the injected compositions with correct coverage, and its sibling-difference posteriors are narrower than the two-stage ones by the amount the correlations predict.

**Risk.** A single chain over hundreds of nuisance parameters and a surrogate may mix slowly. Mitigation: keep the rejection sampler as the reference for the composition marginal and use the joint fit for the correlations; use the two-stage pipeline with joint depth samples as an intermediate step.

**Prototype.** §7 of the plaNETic tab shows the stellar correlation; the rest is new.

### WP4 · Priors as models

**Build.** Replace each hand-set prior with a sourced distribution and a switch.

- *Water in solids.* A distribution of ice fraction versus formation distance from disk-chemistry models, in place of the 50 percent cliff.
- *Formation distance.* A continuous parameter with the formation model's distribution over it, in place of the inside/outside binary. Case A and case B become the two ends of one axis.
- *Envelope.* From WP2: the distribution of survivors under the formation model's initial envelopes and the stellar XUV history, in place of the log-uniform prior.
- *Chemistry.* Keep the three Si/Mg/Fe options; add the measured scatter of the stellar-to-planet relation as a prior width rather than a switch.
- *Temper.* A hyperparameter λ in [0, 1] interpolating between the formation-model prior and a flat reference prior in each parameter. λ is fixed at 0 and 1 for reporting and estimated in WP5.

**Deliverable.** A prior library with provenance for each distribution and a sensitivity table: posterior medians and widths for each planet under each prior, with the evidence of each.

**Gate.** For HIP 29442 b, the upper edge of the envelope posterior is set by the likelihood, not by a prior cutoff, under every prior in the library.

**Risk.** Formation-model priors import the model's own biases, the same models that are compared to the posteriors afterwards. Mitigation: the tempering hyperparameter and the reference prior make the dependence visible; never compare a posterior to the formation model that generated its prior without saying so.

### WP5 · The population layer

**Build.** A hierarchical model over all systems with masses to 15 percent and radii to 5 percent that straddle the radius valley. Population hyperparameters: the fraction born beyond the iceline, the parameters of the initial-envelope distribution, the tempering λ of WP4. A detection model for transit and RV completeness. Each planet's likelihood from WP2 and WP3 enters once.

**Deliverable.** Posterior on the water-world fraction of the sub-Neptune population with a credible interval, and the individual posteriors after shrinkage, with the shrinkage reported.

**Gate.** Injection of a synthetic catalogue from the formation model with a known water-world fraction, through the detection model and the hierarchy, recovers that fraction within its interval.

**Risk.** The prior family is too flexible for the sample and fits noise. Mitigation: few hyperparameters, hyperpriors from the formation model's own spread, and a held-out subset of systems for validation.

**Prototype.** Alibert's census in the first tab, the two-composition station of the Radius valley tab.

### WP6 · Scoring formation models

**Why.** WP4 takes priors from a formation model and WP5 injects from one, but nothing in the plan says how a formation model is judged. Mishra 2023 and Davoult 2024 make the point sharply: their tables are the Bern model's statistics, and a different model would change every number. Two models with different physics can produce the same period–radius histogram; the plan needs a score that separates them and penalises complexity.

**Build.** A population likelihood. A candidate model produces a synthetic population; a fixed detection function per survey turns it into an expected density λ(x) of detections in observable space, where x is system-level: multiplicity against period, period-ratio distribution, radius-valley slope with period, inner super-Earth versus outer giant occurrence, the Mishra coefficients per system, all as a function of stellar mass and metallicity. The observed catalogue is scored as an inhomogeneous Poisson process: the sum of log λ at each observed system minus the expected total. The density is estimated by simulation-based inference, with the synthetic sample kept much larger than the catalogue so the estimate's noise is not a free parameter.

**Parsimony.** Two terms are reported: the evidence, or its BIC approximation, over the model's free constants; and the description length of the model itself, which for an evolved prescription is its code length. A prescription that adds fitted constants for a small likelihood gain loses.

**Validation.** Held-out surveys. Select on one survey and score on another that probes different planets: Kepler for small transiting planets, the radial-velocity legacy surveys for cold giants, TESS and CHEOPS multis, PLATO when it comes. A model tuned to one survey and failing the next is over-fitted, whatever its penalty says.

**Usefulness.** Separately from correctness, the mutual information between the observed part of a system and its hidden part under the model, in bits. A model can be right and useless if the diversity it predicts is irreducible; the spread of its conditional probabilities away from the base rate, of which Davoult's Table 8 is one instance, is the measure. The survey-level version is the lift in Earths per observing hour when targets are ranked by the model.

**Deliverable.** A scoring harness that takes a population and returns likelihood per survey, penalties, held-out score and mutual information; applied first to the Bern model against the current catalogues, as a baseline for any evolved variant.

**Gate.** The harness ranks a deliberately degraded Bern model (migration switched off, or escape removed) below the full one on held-out data, and does not reward a model that widens its initial-condition distributions to absorb the catalogue's scatter.

**Risk.** The detection functions are the weak point; if they are wrong, every model is scored on the wrong data. Mitigation: they are fixed, shared, and checked against the surveys' own injection tests, and they are never part of what is being scored.

**Prototype.** §4 of the Mishra tab and §1 and §4 of the Davoult tab: a survey floor applied to a system, and a class read off the survivors.

### WP7 · From sensitivity to observing strategy

**Build.** For each candidate future measurement, a hypothetical likelihood factor added to the posterior: a transmission spectrum at given precision and wavelength coverage, an emission measurement, an asteroseismic age, a refined abundance, a sibling's improved mass. The expected information gain on the water content for each, computed from WP2's gradients and WP4's posteriors.

**Deliverable.** A ranked table per planet: which measurement, at what precision, collapses which direction of the degeneracy by how much. For HIP 29442 b, the transmission-spectrum precision at which the water-rich and hydrogen-rich stories separate at a Bayes factor of 100.

**Gate.** The ranking reproduces the known cases: radius precision buys nothing on the ridge; a spectrum sensitive to mean molecular weight buys nearly everything.

**Risk.** Spectral forward models add their own degeneracies, clouds above all. Mitigation: treat cloud-top pressure as a nuisance parameter with a broad prior and report the gain marginalised over it.

### WP8 · Validation and calibration

**Build.** A closed-loop harness: draw synthetic systems from the formation model, generate light curves and RVs with realistic noise, run the full pipeline blind, compare recovered posteriors with truth.

**Deliverable.** Coverage plots: the fraction of injected truths inside the 68 and 95 percent intervals, per parameter, per prior. Surrogate error measured inside the recovered posteriors. A mechanical check that no datum entered both a prior and a likelihood.

**Gate.** Coverage within statistical error of nominal for every constrained combination from WP1; deviations along the ridge explained by the prior in use. Injections must also come from a population the WP6 harness scores poorly, to measure how much a wrong formation prior costs.

**Risk.** Calibration against the same formation model that supplies the priors is circular. Mitigation: inject from a second, independent formation model, and from ad hoc distributions that violate the prior, to measure robustness.

### WP9 · Reporting standard

Every result, for every planet, in three layers:

1. **What the data say alone.** The WP1 constrained combinations with prior-free intervals.
2. **What they say under each stated scenario.** Posteriors per prior with the evidence ratio between priors.
3. **What would settle the rest.** The WP7 table for that planet.

Plus, in every figure caption, what is emulated, what is toy, and the domain of validity.

---

## 4. Order and timeline

The packages are sequential in their gates but overlap in their build.

| Phase | Months | Packages | Milestone |
|---|---|---|---|
| I | 1 to 4 | WP1, WP2 structure reimplementation and surrogate | Identifiability note; surrogate data card |
| II | 4 to 9 | WP2 evolution surrogate, WP4 prior library | Prior sensitivity table for HIP 29442 and four other systems; TOI-178 escape test |
| III | 8 to 15 | WP8 harness, then WP3 joint inference | Coverage plots for the two-stage pipeline first; joint-versus-two-stage comparison |
| IV | 13 to 21 | WP5 population layer, WP6 scoring harness | Water-world fraction with interval; Bern model baseline score against current catalogues |
| V | 19 to 24 | WP7 sensitivity, WP9 write-up | Observing-strategy table; method paper; first population paper |

Phase I needs nothing from the group but the equations of state, which are public; the plaNETic surrogate is the check. Phase II is faster with the BICEPS training set. WP3 is the most uncertain package and is deliberately placed after the calibration harness exists, so that the two-stage pipeline is a calibrated fallback if the joint sampler does not mix. WP6 can be started early by anyone, since it needs only synthetic populations and catalogues, and it is the prerequisite for any automated search over the improvable column of section 2b.

---

## 5. Risks to the whole plan

- **The degeneracy is worse than a null direction.** If mixed versus separated water and hydrogen layers, or water dissolved in magma, add further unmodelled dimensions, the identifiability analysis must include them as model-choice parameters, and the priors on them will be weak. Accept it; report it in layer 1.
- **Surrogate drift.** A surrogate trained on one version of the structure model becomes wrong when the equations of state are updated. Version everything; retrain on a schedule; treat the surrogate as a dated instrument.
- **Priors from a single formation model.** The Bern model is one model. Use at least one alternative for injection and, if possible, as a second prior library.
- **Data quality is uneven.** Hierarchical shrinkage is only fair if the noise models are right for every planet. The harness must include heterogeneous data.
- **The interesting planets are the outliers.** HIP 29442 b sits above the radius cliff; shrinkage toward the population is exactly wrong for such objects. Report individual posteriors at λ = 0 alongside the population-informed ones.

---

## 6. What the reading list and the site already provide

| Need | Where it exists | State |
|---|---|---|
| The degeneracy and how time breaks it | Alibert 2016, Alibert tab | toy, calibrated |
| Bayesian interior inference, sensitivity map | Dorn 2017, Dorn tab | toy |
| Escape and evolution over a population | Kubyshkina 2022, Kubyshkina and Gas escape tabs | toy engines |
| Learning an equation, surrogate limits | Baty 2023, Moseley 2020, their tabs | real networks in browser |
| The full pipeline on one system | Egger 2024, Egger and plaNETic tabs | grid transcribed, forward model toy |
| The population view | Radius valley tab, catalogue embedded | real data, toy synthesis |
| Model selection under a parsimony cost | Cacaj 2025, Photobombing tab | criterion transcribed |
| Orbits as a formation record; a planet whose envelope should not have survived | Leleu 2021, Leleu tab | real ephemerides, real N-body, toy interiors |
| Every way a period changes, and the fidelity ladder from Kepler to the disk | Changing periods tab | standard formulas, toy migration |
| A system-level statistic and its limits; what detection does to a class | Mishra 2023, Mishra tab | exact coefficients, Table 2 embedded, toy survey |
| Bias-forwarded conditional probabilities; the innermost detectable planet as a witness | Davoult 2024, Davoult tab | paper's tables embedded, floor recomputed exactly, toy survey |

What the three last papers turned out to contribute is not a prior on formation distance. Leleu contributes a dynamical constraint and a test case for escape (WP2). Mishra contributes system-level summary statistics for the population likelihood, and the lesson that a coefficient built from two planets is not a system statistic (WP6). Davoult contributes the construction of a conditional probability after a fixed detection bias, which is the template for both the usefulness measure of WP6 and the population layer of WP5.

---

## 7. Questions to settle in the first month

1. Answered: BICEPS is not public. The structure surrogate will be trained on a reimplementation; the training set is the ask. Remaining question: can the group release the training set, and in what form?
2. Which formation model outputs can be obtained as joint distributions of composition versus mass and period, and at what resolution?
3. What is the identifiability of Z, the water share of the envelope, once mixed and separated envelopes are both allowed? If it is not identifiable from (M, R), WP7 must lead with it.
4. How many systems pass the precision cuts today, and how many will PLATO add with asteroseismic ages? This sets whether WP5 is a 2026 or a 2028 result.
5. What is the acceptable computational budget per planet for the joint fit, and does it force the two-stage pipeline to remain the default?
6. Which survey detection functions are available in a form that can be fixed and shared for WP6: Kepler's completeness products certainly, radial-velocity legacy surveys less certainly, CHEOPS and TESS multis least of all?
7. Is there a second formation model, with outputs in the same format as the Bern populations, that can serve as the independent injection source of WP8 and the second contender of WP6?

---

## 8. What success looks like

A planet's water content is never reported as a number. It is reported as: the rock mass the data fix; the volatile thickness they fix; the water-versus-hydrogen split under each formation scenario with the evidence for each; and the spectrum that would decide. Across the population, one number with an interval: the fraction of sub-Neptunes that are water worlds. And every one of those statements survives injection and recovery. For formation models, success is a score: a likelihood after the bias, a penalty for size, a held-out survey passed, and a number of bits of information about the planets not yet seen.
