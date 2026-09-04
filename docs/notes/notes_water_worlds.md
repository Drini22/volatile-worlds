# Quantitative ingredients for the "planet evolution" page — water worlds, steam layers, H/He envelopes, radiogenic heating, XUV water loss
Extracted 2026-09-04 from the six PDFs in /Users/drinorcacaj/Documents/Phd_Bern/papers/evolution/. Every equation carries the paper's equation number and page; numbers marked "READ FROM FIGURE" are eyeballed from plots (±5-10 %), all others are copied from tables/text. Units as printed (cgs in Luger & Barnes, Valencia, Mordasini; SI in Turbet; Earth/Jupiter units elsewhere).

Quick index
1. Luger & Barnes 2015 — PMS luminosity decline, XUV saturation/decay, energy-limited escape, crossover mass / O drag, O2 build-up, water-loss maps.
2. Aguichine et al. 2021 — irradiated ocean-planet M-R, steam inflation, analytic fit log R = a log M + b + exp(−d(log M + c)) (coefficients only on Zenodo).
3. Turbet et al. 2020 — runaway-greenhouse steam-atmosphere thickness: full polynomial fits with all coefficients, inflation numbers.
4. Valencia et al. 2013 — R(t) for water vs H/He envelopes on sub-Neptunes, opacity fit, mass loss.
5. Baraffe et al. 2008 — R(0.5, 1, 5 Gyr) tables for Z = 2-90 % water, core vs mixed.
6. Mordasini et al. 2012 (Paper II) — radiogenic heating (Q0, λ), boundary conditions, origin of time, super-Earth R(t), population M-R.

## 1. Luger & Barnes 2015, Astrobiology 15, 119 (arXiv:1411.7412v2) — Extreme water loss and abiotic O2 buildup on planets throughout the HZ of M dwarfs
(page numbers = printed page numbers of the arXiv preprint, 24 pp.)

### 1.1 Pre-main-sequence luminosity decline (Sect. 2.2.1, pp. 2-3; Sect. 4, pp. 9-12)
- Stellar model: Baraffe et al. (1998) solar-metallicity tracks give L_bol(t), T_eff(t); HZ limits from Kopparapu et al. (2014) (RV/EM empirical, RG/MG theoretical) recomputed each timestep. No explicit analytic PMS formula is used — they read L_bol(t) from the tracks. Text: "while a star like the Sun reaches the MS in ≲ 50 Myr, M dwarfs can take several hundred Myr to fully contract and reach the MS ... a decrease in its luminosity by one or even two orders of magnitude" (pp. 2-3). Formation time of planets set to 10 Myr; integrations run to 5 Gyr (p. 7).
- Fig. 3 (p. 9, READ FROM FIGURE): position of the RV (inner HZ) limit a_RV(t) for M★ = 0.08-1.0 M☉. Approximate values: 0.08 M☉: 0.17 AU at 1 Myr → 0.015 AU flat after ~1 Gyr; 0.10 M☉: 0.22 → 0.025 AU (flat after ~0.7 Gyr); 0.20 M☉: ≈0.35 → 0.06 AU (flat after ~0.3 Gyr); 0.30 M☉: ≈0.5 → 0.10 AU (~0.2 Gyr); 0.50 M☉: ≈0.65 → 0.19 AU (~0.1 Gyr); 0.70 M☉: ≈0.8 → 0.32 AU (bump at 30-100 Myr); 1.0 M☉: ≈1.0 → 0.75 AU (min ~0.6 AU near 20-30 Myr, then outward). Text (p. 9): inner edge moves in by nearly an order of magnitude for the lowest-mass M dwarfs; monotonic inward for up to 1 Gyr for M dwarfs; for K dwarfs (0.6-0.9 M☉) only planets forming in the first ~10 Myr see a significant change; for > 0.8 M☉ the HZ moves inward during PMS then outward on the MS. Right panel: contours of a_RV at 3, 10, 30, 100, 300 Myr and 1 Gyr vs M★.
- Fig. 8 (p. 12, READ FROM FIGURE): bolometric flux at the 5-Gyr inner edge of the theoretical HZ, normalized to the runaway-greenhouse flux: 0.1 M☉: ≈70× at 1 Myr → 1 at ≈1 Gyr; 0.5 M☉: ≈15× at 1 Myr → 1 at ≈0.15 Gyr; 0.7 M☉: ≈5× → 1 at ≈30 Myr, then a second bump ≈1.2-1.3× at 50-100 Myr (two runaway episodes for K dwarfs, because stars > 0.6 M☉ switch from convective to radiative transport before the MS); 1.0 M☉: ≈1.6× at 1 Myr, < 1 after ≈5 Myr. Runaway duration (Fig. 4, p. 10, planets formed at 10 Myr): tens to hundreds of Myr throughout the HZ of all M dwarfs; a few Myr for K dwarfs (only if formed early); negligible above ~0.8 M☉ except near the RG boundary.

### 1.2 XUV prescription (Sect. 2.2.2, p. 3; Sect. 3, p. 9)
- Eq. (1), p. 3 (Ribas et al. 2005 form):
  L_XUV/L_bol = f0                       for t ≤ t0
              = f0 (t/t0)^{−β}           for t > t0,     with "β = −1.23" as printed (the intended behaviour is the Ribas 2005 decline F_XUV ∝ t^{−1.23}; the printed sign of β is inconsistent with the exponent −β — implement a decline).
  f0 = 10⁻³ (saturation fraction, all stars); t0 = t_sat = 1 Gyr for M dwarfs (M★ ≤ 0.6 M☉), 0.1 Gyr for K dwarfs (M★ > 0.6 M☉) (p. 9). (Jackson et al. 2012 give t_sat ≈ 100 Myr, f0 ≈ 10⁻³ for 0.6-0.9 M☉; West et al. 2008: activity lifetime ≲ 1 Gyr for early-M, ≳ 7 Gyr for late-M.)
- Present Earth XUV flux (reference): F⊕ = 4.64 erg cm⁻² s⁻¹ (Ribas et al. 2005) (Fig. 1 caption, p. 3).
- Fig. 1 (p. 3, READ FROM FIGURE): log10(F_XUV/F⊕) at the inner HZ edge, Baraffe tracks + this prescription: 0.1 M☉: 4.3 at 1 Myr → 2.4 by ~0.1 Gyr (flat to 1 Gyr) → 1.5 at 10 Gyr; 0.2 M☉: 4.1 → 2.4 → 1.3; 0.3 M☉: 3.9 → 2.4 → 1.2; Sun: 2.4 at 0.1 Gyr → 0 at 4.5 Gyr. I.e. HZ planets of M dwarfs see F_XUV ≳ 300 F⊕ for ~1 Gyr and 10⁴ F⊕ at 1 Myr. Penz & Micela (2008) dashed lines are ~×3-10 higher for 0.1 M☉ (single luminosity curve, overestimates late M).
- XUV absorption efficiency ε_XUV = 0.15-0.30, default 0.30 (p. 9). 1 TO ≡ 1.39×10²⁴ g (≈ 270 bar) of H2O (p. 4). Initial water 1-100 TO. Planet radii from Fortney et al. (2007), Earth-like (2/3 rock, 1/3 iron): 5 M⊕ → 1.52 R⊕ (p. 14).

### 1.3 Energy-limited escape (Sect. 2.4.1, p. 5)
  Ṁ_EL = ε_XUV π F_XUV R_p R_XUV² / (G M_p K_tide)                       (2)
  R_XUV = R_p (assumed); K_tide = 1 (tidal correction ≈ 0.88 for 1 M⊕/1 R⊕ at the RV limit of a 0.1 M☉ star → ≤ 10 % underestimate of Ṁ). F_XUV in erg cm⁻² s⁻¹ (cgs throughout).
- Diffusion limit for H through a static O background (Eq. 13, p. 6; Hunten 1973; Zahnle 1990):
  F_H^diff = b g (m_O − m_H) / [k T (1 + X_O/X_H)]   → = 10 b g m_H/(k T) for X_O/X_H = 1/2.
  In the diffusion-limited case the H flux is min(Eq. 7, Eq. 13), O flux = 0, ocean loss = 9× H loss (p. 6, p. 8).

### 1.4 H/O fractionation — crossover mass (Sect. 2.4.2, p. 5; Hunten et al. 1987; Chassefière 1996b)
  m_c = m_H + k T F_H / (b g X_H)                                            (3)
  F_O = (X_O/X_H) F_H (m_c − m_O)/(m_c − m_H)   valid for m_c ≥ m_O, else F_O = 0   (4)
  F_H^ref ≡ ε_XUV F_XUV R_p / (4 G M_p K_tide m_H)   (H particle flux with no O drag)   (5)
  m_H F_H^ref = Ṁ_EL/(4π R_p²) = m_O F_O + m_H F_H                          (6)
  F_H = F_H^ref                                                         if m_c < m_O
      = F_H^ref [1 + (X_O/X_H)(m_O/m_H)(m_c − m_O)/(m_c − m_H)]⁻¹        if m_c ≥ m_O   (7)
  m_c = m_H + 3 k T F_H^ref/(2 b g)                if F_H^ref < 10 b g m_H/(k T)
      = (43/3) m_H + k T F_H^ref/(6 b g)          if F_H^ref ≥ 10 b g m_H/(k T)        (8)
  with m_O = 16 m_H, X_H = 2/3, X_O = 1/3 (all H and O from photolysed water, atomic at base of flow).
  Critical XUV flux for O to be dragged along (m_c > m_O):
  F_crit ≡ 180 (M_p/M⊕)² (R_p/R⊕)⁻³ (ε_XUV/0.30)⁻¹ erg cm⁻² s⁻¹             (9)   [≈ 39 F⊕ for Earth]
  using b = 4.8×10¹⁷ (T/K)^0.75 cm⁻¹ s⁻¹ (Zahnle & Kasting 1986), T = 400 K (thermospheric), K_tide = 1.
  F_O = (η/2) F_H                                                           (10)
  η ≡ 0 for x < 1;  (x − 1)/(x + 8) for x ≥ 1                                (11)
  x ≡ k T F_H^ref / (10 b g m_H)                                             (12)
  η ∈ [0, 1]: η → 1 (high F_XUV) O flux → half the H flux (no O accumulation); η → 0 no O escape. x ≥ 1 ⇔ F_XUV ≥ F_crit ⇔ m_c ≥ m_O.
- Ocean O2 sink (Eq. 14, p. 6): mass of dissolved O2 / mass of O2 in atmosphere = 0.015 (m_ocean/1 TO) (Henry's law; 70 TO needed to absorb half of the atmospheric O2). Earth surface O2 sinks: ~150 bar/Gyr total (Catling 2014), Fe³⁺ subduction 3-12 bar/Gyr, volcanic reductants ~15 bar/Gyr (p. 6).
- Model loop (Fig. 2, p. 8): halts at t > 5 Gyr, planet enters HZ (runaway ends), or desiccation; if F_XUV < F_crit H escapes per (A6) with no O escape; if diffusion-limited H escapes per (13); else H per (A6), O per (A7). Two HZ-boundary cases: runaway interior to RG limit (default) or interior to RV limit.
- Venus validation (p. 10): f0 = 10⁻³, t_sat = 0.1 Gyr, formation 50 Myr, 1 TO → complete desiccation, O2 ≈ 120 bar (energy-limited) / ≈ 240 bar (diffusion-limited); 10 TO → 1800-2400 bar O2; with RV-limit runaway Venus loses ≤ 0.5 TO, ≤ 120 bar O2.
- Figs. 5-7 (pp. 11-12, 1 M⊕, energy-limited): 1 TO — most of the M-dwarf HZ completely desiccated; above ~0.2 M☉ planets near the outer edge keep some water; even the centre of the HZ is desiccated for M★ ≲ 0.4 M☉; K dwarfs (≳ 0.6 M☉) lose significant water only near the RG limit; O2 absorbed ~100 bar (max ~200 bar, peaking in the centre of the HZ for mid-to-high M dwarfs and near the outer edge for low-mass M dwarfs). 10 TO — most M-dwarf HZ planets lose ≥ 1 TO, ≳ 5 TO close to the RG limit, up to 10 TO for low-mass M dwarfs near the inner edge; O2 several hundred to ~1000 bar.

### 1.5 Hydrogen/oxygen partitioning in the energy-limited regime (Appendix A, pp. 19-20)
Let η be the oxygen escape "efficiency" of Eq. (11) (0 = no O escapes, 1 = O dragged in stoichiometric ratio). All hydrogen escapes (ṁ_H = ṁ_H↑); water photolysis gives ṁ_O = 8 ṁ_H by mass (A2).

- (A1) Ṁ_EL = ṁ_H↑ + ṁ_O↑
- (A3) ṁ_O↑ + ṁ_O^atm = 8 ṁ_H↑
- (A4) F_O/F_H = (1/16) ṁ_O↑/ṁ_H↑ (particle vs mass flux)
- (A5) ṁ_O↑ = 8 ṁ_H↑ η
- (A6) ṁ_H↑ = Ṁ_EL / (1 + 8η)
- (A7) ṁ_O↑ = 8η/(1 + 8η) · Ṁ_EL
- (A8) ṁ_O^atm = (8 − 8η)/(1 + 8η) · Ṁ_EL   (rate of O2 build-up in atmosphere / at surface)
- (A9) ṁ_ocean = ṁ_H↑ + ṁ_O↑ + ṁ_O^atm = 9/(1 + 8η) · Ṁ_EL  → Ṁ_EL for η→1 (H+O escape), 9·Ṁ_EL for η→0 (H-only escape).

### 1.6 Explicit F_XUV dependence (Appendix B, pp. 20-21)
- (B1) F_XUV = [40 G² m_H² b M_p² K_tide / (k T ε_XUV R_p³)] · (1 + 8η)/(1 − η)
- (B2) Ṁ_EL = [40 π G m_H² b M_p / (k T)] · (1 + 8η)/(1 − η)
- (B3) ṁ_O^atm = 320 π G m_H² b M_p / (k T)   — independent of η and of F_XUV (for F_XUV > F_crit): the O2 build-up rate is constant in time.
- (B4) ṁ_H↑ = Ṁ_EL/9 + C ; (B5) ṁ_O↑ = (8/9) Ṁ_EL − C ; (B6) ṁ_ocean = Ṁ_EL + C ; (B7) C = ṁ_O^atm/9 = 320 π G m_H² b M_p/(9 k T)
- (B8) F_O^atm = 5 b g m_H / (k T)  [O-atom flux into atmosphere; = one-half the H diffusion limit when X_O/X_H = 1/2]
- (B9) φ_O = b g (m_H − m_O) / [k T (1 + X_H/X_O)] = −5 b g m_H/(k T) (B10)  (O diffusing downward through the H flow ⇒ O retained at its diffusion limit)
- (B11) Ṗ_O2 ≈ G M_p / (4π R_p⁴) · ṁ_O^atm
- (B12) / Eq. (15), p. 14 and p. 21:
  Ṗ_O2 = 5.35 (M/M⊕)² (R/R⊕)⁻⁴ bar Myr⁻¹                              if F_XUV ≥ F_crit
  Ṗ_O2 = 0.138 (F_XUV/F⊕) (R/R⊕)⁻¹ (ε_XUV/0.30) bar Myr⁻¹              if F_XUV < F_crit
  (b = binary diffusion coefficient of O in H, T = flow temperature; X_O/X_H = 1/2 assumed). Earth: ~5 bar/Myr; 5 M⊕ super-Earth (R = 1.52 R⊕, Fortney et al. 2007): ~25 bar/Myr (p. 15, Fig. 15).
- Fig. 15 (p. 22, read from figure): 1 M⊕, ε_XUV = 0.30: η rises from 0 at F_XUV ≈ 20-50 F⊕ to ≈0.55 at 500 F⊕; ṁ_ocean ≈ 22 TO/Gyr at the knee (≈ diffusion limit, dashed) growing linearly to ≈52 TO/Gyr at 500 F⊕. 5 M⊕: knee at ≈250-500 F⊕, ṁ_ocean ≈ 110 TO/Gyr (diffusion limit) → ≈190 TO/Gyr at 2000 F⊕. For ε_XUV = 0.15 the knee is at twice the flux and slopes are half.
- Diffusion-limited case: planet losing 1 TO builds up (16/18)·270 = 240 bar O2 (Fig. 9 caption, p. 13). Diffusion-limited escape rate scales inversely with the atmospheric scale height → on a 5 M⊕ super-Earth the limit is higher by a factor ≈2.2 (p. 14).

### 1.7 Headline water-loss numbers (Figs. 6-12, Sect. 5 & 7; all colour-map values are read from figures/captions or text)
- Runaway greenhouse duration set by PMS contraction: ~10 Myr (high-mass M dwarfs) to ~1 Gyr (lowest-mass M dwarfs) (p. 18 Conclusions); planets around M dwarfs remain in runaway for 0.1-1 Gyr, during which F_XUV ≳ 300 F⊕ for a 1 Gyr saturation time (p. 16).
- Energy-limited, 1 M⊕ (p. 19 summary): for M★ ≲ 0.3 M☉ nearly all Earth-mass HZ planets lose ≥ 1 TO; tens of TO typically lost for M★ ≲ 0.15 M☉; for 0.3 ≲ M★ ≲ 0.6 M☉ several TO are lost in the centre of the HZ and close to the inner edge; surfaces absorb hundreds-thousands of bar O2.
- Energy-limited, 1 M⊕, 1 TO (Fig. 6, referenced): most of HZ desiccated for M★ ≲ 0.4 M☉; 10 TO (Fig. 7): several TO lost.
- Diffusion-limited, 1 M⊕, 1 TO (Fig. 9, p. 13): water-loss amounts slightly lower, but HZ planets still desiccated over a large fraction of the HZ of M dwarfs; ~240 bar O2 retained throughout a large part of HZ. 10 TO (Fig. 10): > 1 TO lost around low-mass M dwarfs and near inner edge of higher-mass M dwarfs; O2 up to ~2000 bar for lowest-mass M dwarfs.
- 5 M⊕, 10 TO (Figs. 11-12, p. 15): complete desiccation (10 TO lost) in lower-left of HZ (low M★, inner HZ); elsewhere several TO lost; thousands of bar O2 (energy-limited) or several hundred to a few thousand bar (diffusion-limited). GJ 667Cc could have lost ~10 TO and built ~2000 bar O2 (p. 14, 19). Fig. 13: O2 contours 0-2000 bar across the HZ for 5 M⊕, 10 TO, diffusion-limited.
- Fig. 14 (M★ = 0.4 M☉ cross-section, 1 M⊕, 1 TO, energy-limited, p. 16): water lost = 1 TO (complete desiccation) interior to ≈55 % of the HZ; O2 pressure peaks ≈ 120 bar at that critical distance, declining to ≈ 0 at the outer edge (RG phase short there) and to ≈ 40 bar at the RV limit.
- All plots use ε_XUV = 0.30; with 0.15, O2 pressures increase by a factor ~2 (p. 18).
- Neglected: flares, tidal heating/orbital evolution, cold-trapping, moist-greenhouse loss (p. 18).

## 2. Aguichine, Mousis, Deleuil & Marcq 2021, ApJ — Mass-radius relationships for irradiated ocean planets
(page numbers = printed page numbers of the ApJ preprint, 19 pp.)

### 2.0 Abstract-level statements (pp. 1-2)
- "the use of non appropriate EoSs can lead to the overestimation of the planetary radius by up to ~10 %"; "assuming an adiabatic temperature gradient produces very shallow P(T) profiles ... water is not in condensed phase, but rather in supercritical state in most of their hydrospheres, making ocean planets way more inflated with an adiabatic prescription compared to an isothermal one (Turbet et al. 2020; Mousis et al. 2020; Haldemann et al. 2020)". Interior equations: dg/dr = 4πGρ − 2Gm/r³ (1); dP/dr = −ρg (2); dT/dr = −gγT dρ/dP (3); P = f(ρ,T) (4).


### 2.1 Model set-up (Sect. 2-3, pp. 2-9)
- Interior: up to five layers (Fe/FeS core, bridgmanite+periclase lower mantle, olivine+enstatite upper mantle, ice VII, hydrosphere). Vinet EoS with thermal Debye correction, Eq. (6)-(7) p. 3; parameters in Table 1 p. 4 (e.g. core: ρ0 = 8340 kg m⁻³, K0 = 135 GPa, K0' = 6, θ0 = 474 K, γ0 = 1.36, q = 0.91; olivine: ρ0 = 4404, K0 = 128 GPa, K0' = 4.3, γ0 = 1.11, q = 0.54). Water EoS: Mazevet et al. 2019 (Ma19); Grüneisen parameter γ+ from Ma19 (Eq. 19) rather than γ− from Wagner & Pruß (Eq. 18); adiabatic gradient ∇_ad = γ P/(ρ c²) (Eq. 5).
- Interior/atmosphere interface at P_b = 300 bar (just above P_crit = 220.67 bar); atmosphere integrated upward with the Kasting (1988) moist adiabat then isothermal mesosphere at T_top = 200 K; transit radius at P_top = 0.1 Pa. Varying T_top from 200 K to T_skin = T_eff/2^0.25 changes R by ≤ 200 km (≤ 2 %, mostly < 1 %) (p. 5).
- Atmosphere grid (Marcq et al. 2019): g_b = 3-30 m s⁻², M_b = 0.2-20 M⊕, T_b = 750-4500 K (p. 8). Planet grid: M_p = 1-20 M⊕, T_irr = 400-1300 K (only T_irr > 400 K to avoid the two-solution degeneracy in T_p, p. 9). Water blanketing gives T_b > 2000 K at 300 bar for almost all cases, even at T_irr = 400 K (pp. 9, 12).
- Irradiation temperature definitions (p. 5):
  (8)  T_p = (OLR/σ_sb)^{1/4}
  (9)  T_irr = T_eff √(R★/(2a))                        [= T_eq for A = 0, full redistribution]
  (10) T_irr = [OLR/((1−A) σ_sb)]^{1/4} = T_p/(1−A)^{1/4}   (A = Bond albedo computed by the atmosphere model)
  (11) x'_core = x_core/(1 − x_H2O)   (core fraction of the rocky part; Earth-like x'_core = 0.325)
- Earth test: x_core = 0.325, x_H2O = 0.0005, M = 1 M⊕ → R_b = 0.992 R⊕ (p. 3).

### 2.2 Escape criteria used (Sect. 4, pp. 9-10) — NB: ε ≃ 1 (Owen & Jackson 2012; Bolmont et al. 2017)
- Jeans: (20) Φ_J = n_e v_esc/(2√π) · (1/√λ)(1+λ) e^{−λ}; condition to lose x_lost = 0.1 of water in Δt = 1 Gyr (21) gives λ ≤ 100 → (22) R_p > (1/λ) G μ M_p/(R_g T_irr) with T_exo = T_irr.
- Hydrodynamic (energy-limited): (23) Ṁ = ε L_XUV R_p³ / (G M_p (2a)²).
  XUV history (Sanz-Forcada et al. 2011): (24) L_EUV = 10^{3.8} L_X^{0.86}; (25) L_X = 6.3×10⁻⁴ L★ for τ < τ_sat, = 1.89×10²¹ τ^{−1.55} for τ > τ_sat; τ_sat = 5.72×10¹⁵ L★^{−0.65} (τ in Gyr, L in erg s⁻¹ presumably; L★ held constant). Integrated E_XUV = ∫₀^∞ L_XUV dt = 1.8×10³⁹ W (sic; units as printed) for a solar-type star.
  (26) ε E_XUV R_p³/(G M_p (2a)²) ≥ x_lost M_p ; (27) (2a)² = L★/(4π σ_sb T_irr⁴) ; (28) R_p ≥ M_p^{2/3} [x_lost G/(ε 4π σ_sb T_irr⁴ E_XUV)]^{1/3}.
  Bolmont et al. 2017 fractionation gives r_F ~ 0.2 (O atoms per escaping H), i.e. substantial loss of both H and O (p. 11).

### 2.3 Results: how much steam/supercritical water inflates the radius (Sect. 5, pp. 11-13)
- Using WP02 or DZ06 EoS outside their validity ranges overestimates R by up to ~10 %; Ma19+ vs Ma19− (γ choice) differ by ≤ 10 % (Fig. 6, p. 13: −1 % to −10 %, largest at low mass and high WMF/high T_irr).
- KEY STATEMENTS (p. 13, Sect. 5.2): "steam atmospheres are very extended (Mousis et al. 2020), allowing to compute compositions without invoking small H2-He envelopes (1-5 % by mass)"; "In the 10-20 M⊕ range, the radius of a planet with a WMF of 50 % made of liquid H2O is equal to that of a planet with a WMF of 20 % constituted of supercritical H2O. Also, the radius of a planet fully made of liquid H2O is equivalent to that of a planet with half its mass constituted of supercritical H2O." With Ma19, a 100 % water Neptune-mass (17 M⊕) planet has R = 3.25 R⊕ at T_irr = 400 K and 3.6 R⊕ at T_irr = 1300 K (p. 13).
- Fig. 8 (p. 15; Ma19+, no metallic core; values READ FROM FIGURE, ±0.1 R⊕):
  | WMF | T_irr | R at 1 M⊕ | R at 2-3 M⊕ (min) | R at 20 M⊕ |
  | 20 % | 400 K | ≈1.7 | ≈1.65 | ≈2.75 |
  | 50 % | 400 K | ≈2.0 | ≈1.95 | ≈2.9 |
  | 100 % | 400 K | ≈2.3 | ≈2.2 | ≈3.2 |
  | 20 % | 1000 K | ≈2.3 (starts at 1 M⊕) | ≈2.05 (at 3 M⊕) | ≈2.85 |
  | 50 % | 1000 K | – (starts ≈1.5 M⊕ at ≈2.5) | ≈2.45 | ≈3.05 |
  | 100 % | 1000 K | – (starts ≈3 M⊕ at ≈3.1) | ≈3.1 | ≈3.5 |
  Condensed (Zeng et al. 2016, thin cyan lines): 100 % liquid H2O ≈1.25 R⊕ at 1 M⊕, ≈2.9 at 20 M⊕; 50 % liquid ≈1.15 at 1 M⊕, ≈2.55 at 20 M⊕. ⇒ steam inflation ≈ +10 % at 20 M⊕/400 K, ≈ +40-45 % at 2 M⊕/400 K, more at higher T_irr; curves are non-monotonic (radius minimum near 1-3 M⊕ because low gravity puffs the steam layer).
- Fig. 5 (p. 12): full grid at T_irr = 400/600/800/1000 K for WMF 10/20/50/100 %, 0.5-20 M⊕, with Earth-like x'_core; grey/pink shading = H2 / H2O escape regions from Eqs. 22 & 28.
- Derived sub-Neptune radii (1.75-3.5 R⊕) match the second peak of the Fulton et al. (2017) bimodal distribution (p. 15). "Due to its greater density, water is much less subject to atmospheric escape than H/He" (p. 15).
- GJ 9827 (Table 3, p. 13): b: 4.91±0.49 M⊕, 1.58±0.03 R⊕, T_irr 1184 K → WMF 0-5 %; c: 0.84±0.66 M⊕, 1.24±0.03 R⊕, 820 K → 1-5 %; d: 4.04±0.83 M⊕, 2.02±0.05 R⊕, 686 K → 5-30 % (20±10 %).

### 2.4 THE ANALYTIC MASS-RADIUS FIT (Sect. 5.3, Eq. 29, p. 13)
  log R_p = a · log M_p + b + exp( −d (log M_p + c) )            (29)
  log = decimal logarithm; R_p, M_p in Earth units; a, b, c, d fitted separately for each (x_core, x_H2O, T_irr) grid point.
  Accuracy: MAE (Eq. 30, p. 14) = (1/N) Σ |R_model − R_fit|/R_model = 0.01-1 % for all fits; largest single-point deviation 2.3 %. Coefficients vary smoothly in (x_core, x_H2O, T_irr) so interpolation is allowed.
  VALIDITY: M_p = 1-20 M⊕ (grid 0.2-20 M⊕ for M_b), T_irr = 400-1300 K, WMF up to 100 %, CMF up to Earth-like or Mercury-like; only the "valid"/"extended" points (Fig. 5 markers) should be trusted; extrapolated cases (crosses) are marked incorrect.
  IMPORTANT: the paper does NOT print the coefficient table. The numerical (a, b, c, d) per composition/temperature and the tabulated M-R curves are on Zenodo, doi:10.5281/zenodo.4552188 (also https://archive.lam.fr/GSP/MSEI/IOPmodel) — p. 16. Any coefficients for the web page must be fetched from there.

## 3. Turbet, Bolmont, Ehrenreich, Gratier, Leconte, Selsis, Hara & Lovis 2020, A&A 638, A41 — Revised mass-radius relationships for water-rich rocky planets more irradiated than the runaway greenhouse limit
(page numbers = printed "page N of 11")

### 3.1 Threshold and set-up (Abstract, Sect. 1-2, pp. 1-2)
- Irradiation threshold: the runaway greenhouse limit, "around 1.1 times the insolation at Earth for planets orbiting a Sun-like star" (Kasting 1993; Goldblatt & Watson 2012; Kopparapu 2013); for TRAPPIST-1 (ultra-cool), the three inner planets b, c, d are beyond the threshold (Kopparapu 2013; Wolf 2017; Turbet 2018). Above the threshold, all water is in the steam atmosphere and the planet suffers the "runaway greenhouse radius inflation effect" (Turbet et al. 2019): larger total atmospheric mass, higher atmospheric temperature, higher optical thickness at low P, lower mean molecular mass.
- Method: (i) dry-rock M-R from Zeng et al. 2016 (pure MgSiO3, terrestrial core composition, pure Fe); (ii) for each (M_core, R_core) compute steam-atmosphere transit thickness z_atm and mass M_atm with the 1-D inverse radiative-convective LMD Generic model (non-dilute moist lapse rate of Marcq 2017, Leconte 2013 absorption); (iii) M_planet = M_core + M_atm, R_planet = R_core + z_atm (R_core computed neglecting the atmosphere's mass load, valid while M_atm ≪ M_core); (iv) logarithmic interpolation in water-to-rock ratio.
- Grid of the atmospheric calculations: surface T 300-4300 K, irradiation ≈ 1-40× Earth's, surface gravity 2-50 m s⁻², water vapour pressure 2.7×10⁵ - 2.7×10⁹ Pa.
- Headline (Abstract): traditional condensed-water M-R relations overestimate bulk water content of irradiated planets "by several orders of magnitude"; TRAPPIST-1 b, c, d can accommodate water mass fractions of at most 2 %, 0.3 % and 0.08 %, respectively (terrestrial-composition core).

### 3.2 Empirical fit for the surface temperature of a steam atmosphere — Eq. (1), Table 1 (p. 3)
  log10 T_surf(x,y,z) = c1 + c2 x + c3 y + c4 z + c5 x² + c6 x y + c7 y² + c8 z² + c9 y³ + c10 z³        (1)
  x = (log10 P_H2O − k1)/k2  [P_H2O = water partial (surface) pressure in bar]
  y = (log10 g − k3)/k4      [g = surface gravity at the interior-atmosphere boundary, m s⁻²]
  z = (log10 S_eff − k5)/k6  [S_eff = irradiation in Earth units, 1 = 1366 W m⁻²]
  k1 = 2.688, k2 = 1.019, k3 = 1.099, k4 = 4.683×10⁻¹, k5 = 7.664×10⁻¹, k6 = 4.224×10⁻¹
  c1 = 3.401, c2 = 1.501×10⁻¹, c3 = −3.146×10⁻², c4 = 4.702×10⁻², c5 = −4.911×10⁻³, c6 = 8.519×10⁻³, c7 = −1.467×10⁻², c8 = −7.091×10⁻³, c9 = −7.627×10⁻³, c10 = 8.348×10⁻³
  Validity: S_eff ≈ 1-30 S⊕ (must exceed the runaway threshold), g = 0.2-6 g⊕, P_H2O = 2.7 bar - 27 kbar, and only while T_surf stays within 300-4300 K. Mean error ~2.5 %, max ~10 % (Fig. B.2: residual σ = 0.013 dex in log T_surf, 0.012 dex in log T_eff; 16 488 1-D simulations).

### 3.3 Steam-atmosphere thickness — Eq. (2) (p. 4) with Eq. (3) & Table 2
  z_atmosphere = { 1 / [ ln( (x_H2O/(1 − x_H2O)) · g_core² / (4π G P_transit) ) · (R T_eff / (M_H2O g_core)) ]  −  1/R_core }⁻¹        (2)
  (paper writes "log"; from the derivation C.4-C.8 it is the natural log of the pressure ratio P_surf/P_transit). R_core, g_core = core (surface) radius and gravity; R = 8.314 J K⁻¹ mol⁻¹; M_H2O = 1.8×10⁻² kg mol⁻¹; G = 6.67×10⁻¹¹ m³ kg⁻¹ s⁻²; x_H2O = water mass fraction of the planet (0-1); P_transit ≈ 10⁻¹ Pa (varies little); T_eff = effective (isothermal-equivalent) atmospheric temperature from Eq. (3).
  Derivation (Appendix C, p. 10): hydrostatic (C.1) dP + ρ g dr = 0; g(r) = g_core (R_core/r)² (C.2); ideal gas ρ = P M_H2O/(R T_eff) (C.3); ⇒ ln(P/P_surf) = (M_H2O g_core/(R T_eff)) R_core² (1/r − 1/R_core) (C.5); R_p = [ (R T_eff/(M_H2O g_core)) (1/R_core²) ln(P_transit/P_surf) + 1/R_core ]⁻¹ (C.7); z = R_core [ R_core / ( ln(P_surf/P_transit) · R T_eff/(M_H2O g_core) ) − 1 ]⁻¹ (C.8); P_surf = M_atm g_core/(4π R_core²) (C.9); M_atm = M_core x_H2O/(1 − x_H2O) = (g_core R_core²/G) · x_H2O/(1 − x_H2O) (C.10).
  log10 T_eff(x,y,z) = β1 + β2 x + β3 y + β4 z + β5 x y + β6 y² + β7 x³ + β8 x² y + β9 x y² + β10 y⁴        (3)
  x = (log10 x_H2O − α1)/α2 ; y = (log10 g − α3)/α4 [m s⁻²] ; z = (log10 S_eff − α5)/α6 [Earth units]
  α1 = −3.550, α2 = 1.310, α3 = 1.099, α4 = 4.683×10⁻¹, α5 = 7.664×10⁻¹, α6 = 4.224×10⁻¹
  β1 = 2.846, β2 = 1.555×10⁻¹, β3 = 8.777×10⁻², β4 = 6.045×10⁻², β5 = 1.143×10⁻², β6 = 1.736×10⁻², β7 = 1.859×10⁻², β8 = 4.314×10⁻², β9 = 3.393×10⁻², β10 = −1.034×10⁻²
  Validity of (2)-(3): S_eff = 1-30 S⊕, g = 0.2-6 g⊕, P_H2O = 2.7 bar - 27 kbar, T_surf 300-4300 K; max error ~10 %.
  Recipe (Appendix D, p. 11): pick core composition → (M_core, R_core) from Zeng et al. 2016 tables → g_core → choose x_H2O, S_eff (> runaway limit, Kopparapu 2013/2014) → z_atm from (2)+(3) → R_planet = R_core + z_atm, M_planet = M_core/(1 − x_H2O). R_core+z approximation: ≤ 1 % error for 5 % water on a 2 M⊕ core (Appendix A, p. 9); valid while basal pressure ≪ 10¹⁰ Pa.

### 3.4 Radius-inflation numbers (Sect. 3, pp. 4-7; Fig. 2 p. 5, Fig. 3 p. 7 — values READ FROM FIGURES unless stated)
- Fig. 2 right (steam, terrestrial core; 0.2-2 M⊕): at 1 M⊕ radius ≈ 1.00 (dry terrestrial), ≈1.02 (0.01 % H2O), ≈1.05 (0.1 %), ≈1.10 (1 %), ≈1.16 (3 %), ≈1.22 (5 %, dashed). At 0.5 M⊕: dry ≈0.86, 1 % ≈0.98, 5 % ≈1.20 (U-shape: the 5 % curve is nearly flat/rising toward low mass). At 2 M⊕: dry ≈1.20, 1 % ≈1.27, 5 % ≈1.35.
- Fig. 2 left (condensed water, Zeng 2016, pure-MgSiO3 interior): at 1 M⊕: dry silicate ≈1.04, 5 % ≈1.06, 25 % ≈1.11, 50 % ≈1.17, 75 % ≈1.22, 100 % ≈1.27.
  ⇒ For a ~1 M⊕ planet, 1 % steam ≈ +10 % radius (≈ same as 25 % condensed water); 5 % steam ≈ +20-22 % (≈ same as 75-100 % condensed water). This is the "several orders of magnitude" overestimate of water content (Abstract, Sect. 3.1, Sect. 4).
- Text (p. 4): planets with M_planet ≲ 0.5 M⊕ above the runaway threshold cannot retain more than a few % water — e.g. 0.3 M⊕ pure-silicate core + 5 % water gives transit radius ≈ 1.2 R⊕ and gravity at the transit radius ≈ 20 % of Earth's (~2 m s⁻²) ⇒ gravitationally unbound upper atmosphere / efficient escape; U-shaped M-R curves.
- Fig. 3 (p. 7): terrestrial core + 6 % H2O steam: R ≈ 1.14 R⊕ at 0.4 M⊕ (curve minimum region), ≈ 1.28 at 1.2 M⊕; 0.6 % steam ≈ 1.17 at 1.2 M⊕; 0.06 % steam ≈ 1.13 at 1.2 M⊕; 6 % condensed ≈ 1.13 at 1.2 M⊕ (nearly coincident with the 10 % Fe + 90 % MgSiO3 dry line). Note (caption): steam M-R curves change only slightly with irradiation level once above the threshold.
- Table 3 (p. 5): maximum H2O mass fraction: pure-silicate core — T-1b 0.4 %, T-1c 0.01 %, T-1d 0.01 %; terrestrial core — 2 %, 0.3 %, 0.08 %; pure-iron core — >10 %, >10 %, 2 %. Bourrier et al. 2017 present water-loss rates for T-1 b, c, d: 0.19, 0.06, 0.18 % of planet mass per Gyr (p. 6).
- Fig. 1 (p. 3): T_surf map vs S_eff (1-40) and P_H2O (10⁶-10¹⁰ Pa) for 0.3, 1, 3 g⊕; e.g. at 1 g⊕, T_surf = 2000 K reached at P ≈ 3×10⁷ Pa (S_eff = 2) or ≈ 4×10⁶ Pa (S_eff = 40); 3000 K at ≈ 10⁹ Pa (S_eff 2) to 10⁸ Pa (S_eff 40).
- No time dependence: the model gives the instantaneous inflated radius for a given (M_core, R_core, x_H2O, S_eff); the "irradiation threshold" itself is the Kopparapu et al. (2013) runaway limit (~1.1 S⊕ for a Sun-like star, lower S_eff for cooler stars), and the planet's interior thermal state is not modelled (Sect. 4: future work should include core cooling, greenhouse feedback on the interior).

## 4. Valencia, Guillot, Parmentier & Freedman 2013, ApJ 775, 10 (arXiv:1305.2629) — Bulk composition of GJ 1214b and other sub-Neptune exoplanets
(page numbers = arXiv manuscript pages, 38 pp.)

### 4.1 Model (Sect. 2, pp. 5-15)
- Earth-like nucleus (33 % Fe core + 67 % Mg-silicate mantle, Valencia et al. 2006; Vinet EoS) + CEPAM envelope (Guillot & Morel 1995) of H/He (SCVH, Y = 0.27) and H2O (French et al. 2009 above 1000 K + NIST Saul & Wagner 1989). Continuity of mass and pressure (not T) at the solid surface. Transit radius = slant optical depth unity. Cases: grain-free T_eq = 500 K, grainy 500 K, grain-free 600 K. Masses 5.09, 6.36, 7.63, 8.90, 10.2 M⊕ (0.016-0.032 M_Jup); envelope from 100 % H/He to 100 % H2O; R = R(M, nf, wf), nf = nucleus fraction, wf = water fraction of envelope.
- Rosseland opacity fit (Sect. 2.2, Eqs. 1-3, p. 6; Table 1, p. 8) — T in K, P in dyn cm⁻², met = [M/H], κ in cm² g⁻¹ (paper prints "g cm⁻²"):
  κ_gas = κ_lowP + κ_highP                                                   (1)
  log10 κ_lowP = c1 (log10 T − c2 log10 P − c3)² + (c4 met + c5)              (2)
  log10 κ_highP = (c6 + c7 log10 T + c8 log10 T²) + log10 P (c9 + c10 log10 T) + met c11 [1/2 + (1/π) arctan((log10 T − 2.5)/0.2)]   (3)
  all T: c1 = −37.50, c2 = 0.00105, c3 = 3.2610, c4 = 0.84315, c5 = −2.339
  T < 800 K: c6 = −14.051, c7 = 3.055, c8 = 0.024, c9 = 1.877, c10 = −0.445, c11 = 0.8321
  T > 800 K: c6 = 82.241, c7 = −55.456, c8 = 8.754, c9 = 0.7048, c10 = −0.0414, c11 = 0.8321
  Fitted to Freedman et al. 2008 tables (75-4000 K, 10⁻⁶-300 bar; solar, 0.5×, 2×, 30×, 50× solar); extrapolated beyond. Grains (Eq. 4, p. 7): κ = κ_gas + κ_grains for T < T1*, log10 κ_grains = 0.430 + 1.3143 (log10 T − 2.85); κ = κ_gas for T > T2*; log10 T1* = 0.0245 log R̄ + 1.971, log10 T2* = 0.0245 log R̄ + 3.221, R̄ = ρ/T6³ (linear interpolation between).
- Metallicity ↔ ices (Sect. 2.3, p. 14): Z_ices = (N_O μ_H2O + N_C μ_CH4 + N_N μ_NH3)/(N_H μ_H + N_He μ_He + N_O μ_O + N_C μ_C + N_N μ_N); c = Y/(X+Y) = 0.27; N_O/N_H = [1/(1−c)] μ_H Z_ices/(a − b Z_ices); 10^met = (N_O/N_H)/(N_O/N_H)_solar; N_C/N_O = 0.501, N_N/N_O = 0.138, (N_O/N_H)_solar = 4.898×10⁻⁴ (Lodders 2003) → Z_ices = 1 ⇔ 457× solar (met = 2.66).
- Atmosphere: Guillot (2010) analytic model, γ = κ_v/κ_IR = 0.032 → T ≈ 1000 K at 1 bar for GJ 1214b (matches Miller-Ricci & Fortney 2010). Intrinsic temperature T_int (p. 15): solar-composition envelope 62 K (0.1 Gyr), 40 K (1 Gyr), 35 K (2.5 Gyr), 24 K (10 Gyr); water-rich envelope 80 K (0.1 Gyr), 50 K (1 Gyr), 42 K (2.5 Gyr), 35 K (10 Gyr). Fig. 3 (p. 16): 10-Gyr P-T profiles — ~450-500 K isothermal above 10⁻² bar, ~1000 K plateau at 0.1-1 bar (solar) / 0.3-3 bar (water), reaching 1400-1600 K at 10³ bar.

### 4.2 Thermal evolution: water vs H/He envelopes (Sect. 3.1, pp. 15-20; Fig. 4 p. 18, Fig. 5 p. 20)
- Fig. 4 bottom-left (0.020 M_Jup = 6.36 M⊕, 50 % Earth-like nucleus, grain-free; T_eq = 500 K solid, 600 K dashed) — R(t) READ FROM FIGURE (log axes):
  | envelope (50 % of mass) | 30 Myr | 100 Myr | 1 Gyr | 10 Gyr |
  | 100 % H2O | ≈1.9 | ≈1.9 | ≈1.87 | ≈1.85 R⊕ (essentially flat) |
  | 50 % H2O + 50 % H/He | ≈8 | ≈6.5 | ≈5.0 | ≈4.0 R⊕ (600 K: ≈8.5 → 4.3) |
  | 100 % H/He | ≈17 | ≈12.5 | ≈8.5 | ≈6.3 R⊕ (600 K: ≈19 → 7) |
  Top-left: envelope density at the base ≈3.5 g cm⁻³ (H2O) vs ≈0.9 (50/50) vs ≈0.5 (H/He). T_eq 500 → 600 K "has little effect on the interior structure or evolution" (p. 17).
- Text (p. 17): "envelopes that have lower molecular weight yield the largest radii, while at the same time suffer the most contraction" — except that 100 % H/He envelopes are slightly SMALLER than 90 % H/He + 10 % H2O (higher opacity slows cooling; density effect dominates at larger water fractions).
- Text (p. 19): "The effect of contraction is most significant in the early stages of evolution (< 1 Gy) and for H/He dominated envelopes, and less important as the age of the planet increases or its envelope is H2O dominated."
- Fig. 5 (p. 20; 0.020 M_Jup, T_eq = 500 K, envelope = 3 % of mass) — R(t) READ FROM FIGURE:
  | envelope composition | 10 Myr | 100 Myr | 1 Gyr | 3 Gyr | 10 Gyr |
  | 99.9 % H/He + 0.1 % H2O | 3.6 | 3.05 | 2.8 | 2.68 | 2.62 R⊕ |
  | 75 % H/He + 25 % H2O | 3.9 | 3.2 | 2.85 | 2.68 | 2.60 |
  | 90 % H/He + 10 % H2O | 4.3 | 3.5 | 3.05 | 2.9 | 2.75 |
  The first two cross at ≈3 Gyr at the GJ 1214b radius (horizontal line at ≈2.68 R⊕ in the figure; the text says "6.55 R_E", an evident inconsistency — the figure value is consistent with GJ 1214b). Degeneracy: same envelope mass, different composition → same radius at one age but different tracks.
- Opacity-extrapolation sensitivity (p. 12): with c8 = 5 (weaker T dependence) the RCB moves 10-20 % shallower and R changes by 0.2 % (100 % water) and 5 % (90 % H/He + 10 % water) at 2.5 Gyr, < 0.1 % at 10 Gyr. Relevant regime for warm sub-Neptunes: RCB at < 5 kbar and < 2000 K (p. 13).
- Grains: step-like opacity increase below ~2000 K, > 1 dex for solar composition, only tens of % for water-rich envelopes (κ already ≥ 10 cm² g⁻¹) (p. 9).

### 4.x Late sections (pp. 21-38 of the arXiv manuscript)
- Radiative-convective boundary (Fig. 6, p. 22; 0.020 M_Jup = 6.36 M⊕, T_eq = 500 K, Earth-like nucleus = 50 % of planet). Boundary pressure ranges from 4600 bar (solar envelope) to 138 bar (pure water/ice envelope) and moves deeper with age (p. 21). Triplets (Z_ices, T_rcb [K], log S):
  2.5 Gyr: (0.01, 1478, 8.7), (0.2, 1438, 9.1), (0.4, 1391, 9.3), (0.6, 1357, 9.4), (0.8, 1278, 9.5), (1, 1211, 9.6)
  10 Gyr:  (0.01, 1454, 8.7), (0.2, 1452, 9.1), (0.4, 1417, 9.3), (0.6, 1307, 9.4), (0.8, 1235, 9.5), (1, 1163, 9.6)
  Bottom panel (read from figure): RCB pressure at 10 Gyr ≈ 10^2.2 bar (Z=1) → 10^3.65 bar (Z=0.01); at 2.5 Gyr ≈ 10^1.9 → 10^3.3 bar; κ_rcb ≈ 13 cm² g⁻¹ (Z=1) to ≈1 (Z=0.01).
- Grain opacity matters for H/He (gas κ 0.1-1 cm² g⁻¹, grains 10× more) and is negligible for water envelopes (gas κ already ~10 cm² g⁻¹) (p. 21).
- "the mass and radius data for GJ 1214b is consistent with a pure H2O/ices composition ... regardless of the uncertainty in age, as contraction is negligible for water dominated atmospheres" (p. 21).
- Temperature sensitivity: a 100 K increase in T_eq (≈ +200 K at 10 bar) increases the radius of GJ 1214b-like planets by only ~2 % (p. 24).
- Age sensitivity: "For planets older than ~1 Gy with water-dominated envelopes, age has an effect of less than 1 % in the inference of envelope composition"; older planets admit more H/He for a given radius (p. 25-27). GJ 1214b: H/He < 7 % by mass (10 Gyr); solar-metallicity envelope case ~3 % by mass (3 Gyr) (p. 27-28). Fig. 9 (p. 29): M_HHe/M_p peaks ≈0.05 (±0.01) at M_core/M_p ≈ 0.7 or M_H2O/M_p ≈ 0.2.
- Fig. 7 (p. 23; MR at 4.6 Gyr, T_eq = 500 K solid / 600 K dashed, envelope 5/10/20/50/100 % over Earth-like nucleus). Values READ FROM FIGURE (km): 100 % H2O/ices envelope: ≈9 500 km at 1 M⊕, ≈15 000 at 5 M⊕, ≈17 500 at 10 M⊕, ≈20 000 at 20 M⊕; 50 %: ≈8 000 / 12 500 / 14 500 / 17 000; 20 %: ≈7 300 / 11 000 / 12 800 / 15 000; 5 %: ≈6 800 / 10 000 / 11 500 / 13 500; Earth-like rock: 6 371 / 9 700 / 11 300 / 13 000. Right panel (50 % H2O + 50 % H/He envelopes): far larger and flaring to low mass, e.g. 20 % envelope ≈ 25 000 km at 2 M⊕, ≈ 20 000 km at 10 M⊕; 5 % envelope ≈ 13 000-15 000 km at 5-10 M⊕. T_eq 500→600 K changes R by a few %.
- Thermal-inertia / radiogenic prescription of the rocky nucleus (p. 28, quoted verbatim, units as printed): "The lower boundary heat flux entering the envelope is L̇_sol = ε̇_rad + C_v dT/dt ... We used a chondritic value for the heat generation (2 × 10^20 J/s/g) which is a factor of ~2 lower than the Earth's bulk silicate value, and a heat capacity of 7 × 10^7 J/K/g which is appropriate for the Earth (Stacey 1981)." [The printed exponents look like typos — chondritic heating is ~10⁻¹² W kg⁻¹; treat numbers with caution.] Increasing ε̇_rad ×5 → 2 % radius discrepancy at 3 Gyr; C_v ×10 → ~6 % for planets with 3-20 % H/He envelopes ⇒ "the radius of a sub-Neptune planet is not very sensitive to the thermal evolution of its rocky nucleus" (contrast to Nettelmann 2011, Lopez 2012).
- Evolutionary degeneracy (p. 34): two envelope compositions of the same mass around the same nucleus may yield the same radius at a given age while differing in the rest of their tracks.
- Mass loss (Sect. 3.2, pp. 30-31): Eq. (5) Ṁ = π ε R_XUV² R F_XUV/(G M K_tide) → with R_XUV ~ R: Ṁ = 3 ε F_XUV/(4 G ρ K_tide); ε = 0.1-0.4 commonly. Eq. (6) (Ribas 2010): F_XUV = 4.04×10⁻²⁴ L_bol^0.79 a⁻² erg s⁻¹ cm⁻² for t9 < t9*; = 29.7 t9^{−1.72} a⁻² for t9 > t9*; t9* = 1.66×10²⁰ L_bol^{−0.64} Gyr (t9 in Gyr; L_bol = 0.00328 L☉ for GJ 1214 → t* = 2 Gyr). Present flux at GJ 1214b: 39 W m⁻²; present loss 2.4×10⁸ ε kg s⁻¹ ≈ 1.25 ε M⊕ Gyr⁻¹; cumulative 100 Myr-3 Gyr: 0.6 M⊕ (ε=0.1) to 2.5 M⊕ (ε=0.4) = 9-27 % of mass (density held constant, K_tide = 1).
- Kepler-11e needs 10-25 % bulk H/He; all other volatile low-mass planets < 10 % H/He (p. 32); Lopez et al. 2012 give 17.2 % for Kepler-11e at 8 Gyr, <8 % others (p. 33).

## 5. Baraffe, Chabrier & Barman 2008, A&A 482, 315 (arXiv:0802.1810) — Structure and evolution of super-Earth to super-Jupiter exoplanets: I. heavy element enrichment in the interior
(page numbers = arXiv manuscript pages, 20 pp.) Full grid 10 M⊕ - 10 M_Jup: http://perso.ens-lyon.fr/isabelle.baraffe/PLANET08

### 5.1 Set-up (Sects. 2-3, pp. 2-5; Sect. 7.2, p. 16)
- Heavy-element EoS: ANEOS (Thompson & Lauson 1972) and SESAME (Lyon & Johnson 1992) for water, "rocks" (dunite/olivine, drysand) and iron, with full T dependence; compared to Seager et al. 2007 zero-T EoS (Fig. 1, p. 4). H/He: SCVH with Y = 0.275. Mixture in the envelope: additive volume law (AVL): 1/ρ(P,T) = (1−Z)/ρ^{H/He} + Z/ρ^Z (1); U = (1−Z)U^{H/He} + Z U^Z (2); S = (1−Z)S^{H/He} + Z S^Z + S_mix (3); ∇_ad = (∂log S/∂log P)_T/(∂log S/∂log T)_P (4). Alternative: Y_equiv = Y + Z in SCVH (valid for Z_env ≲ 20 %). Mixing entropy 10-20 % of S (affects structure, not evolution).
- Boundary conditions (p. 6, p. 16): Barman et al. 2001 irradiated solar-metallicity atmosphere grids with F_inc = (f/4)(R★/a)² F★, f = 2 (day-side redistribution); "irradiated" grid = Sun at 0.045 AU, "non-irradiated" grid otherwise. Core-envelope boundary: density jump, continuity of P and T. Irradiated radii in Table 5 are NOT corrected for atmospheric extension (adds ~4 % for this irradiation; Baraffe et al. 2003).
- Grid choice of heavy-element distribution (Sect. 7.2, p. 16): heavy material = water (SESAME); Z = 0.02 solar-like; Z = 10 %: all in core; Z = 50-90 %: "light planets" M_p ≲ 20 M⊕ — all in a core; more massive — distributed over the entire planet (AVL). For M > 1 M_Jup only Z = 0.02 and 0.10.

### 5.2 Radius vs age — Table 4 (non-irradiated) and Table 5 (irradiated by a Sun at 0.045 AU), p. 17. R in R_Jup (1 R_J = 71 492 km = 11.21 R⊕). Columns: M_p/M⊕ | R(0.5 Gyr) | R(1 Gyr) | R(5 Gyr)
Table 4 (no irradiation):
  Z = 0.02: 10 | 0.828 | 0.811 | 0.758 ; 20 | 0.858 | 0.839 | 0.800 ; 50 | 0.923 | 0.905 | 0.876 ; 100 | 0.980 | 0.963 | 0.937 ; 159 | 1.017 | 0.995 | 0.968 ; 318 | 1.057 | 1.032 | 0.998
  Z = 0.10: 10 | 0.779 | 0.763 | 0.716 ; 20 | 0.813 | 0.797 | 0.762 ; 50 | 0.878 | 0.862 | 0.836 ; 100 | 0.935 | 0.919 | 0.896 ; 159 | 0.971 | 0.951 | 0.926 ; 318 | 1.012 | 0.990 | 0.958
  Z = 0.50: 10 | 0.598 | 0.586 | 0.555 ; 20 | 0.632 | 0.621 | 0.598 ; 50 | 0.683 | 0.665 | 0.635 ; 100 | 0.717 | 0.697 | 0.670 ; 159 | 0.739 | 0.718 | 0.690 ; 318 | 0.781 | 0.756 | 0.721
  Z = 0.90: 10 | 0.382 | 0.375 | 0.357 ; 20 | 0.420 | 0.414 | 0.403 ; 50 | 0.503 | 0.474 | 0.439 ; 100 | 0.543 | 0.512 | 0.469 ; 159 | 0.568 | 0.538 | 0.492 ; 318 | 0.607 | 0.578 | 0.524
Table 5 (irradiated, Sun at 0.045 AU):
  Z = 0.02: 10 | – | – | – (expands, "meaningless") ; 20 | 1.441 | 1.391 | 1.229 ; 50 | 1.258 | 1.192 | 1.084 ; 100 | 1.201 | 1.155 | 1.074 ; 159 | 1.186 | 1.151 | 1.085 ; 318 | 1.160 | 1.137 | 1.089
  Z = 0.10: 10 | 1.517 | 1.506 | 1.428 ; 20 | 1.416 | 1.326 | 1.147 ; 50 | 1.173 | 1.120 | 1.021 ; 100 | 1.131 | 1.091 | 1.020 ; 159 | 1.120 | 1.089 | 1.032 ; 318 | 1.106 | 1.086 | 1.042
  Z = 0.50: 10 | 1.095 | 1.050 | 0.927 ; 20 | 0.935 | 0.890 | 0.800 ; 50 | 0.841 | 0.798 | 0.725 ; 100 | 0.812 | 0.787 | 0.737 ; 159 | 0.813 | 0.790 | 0.747 ; 318 | 0.830 | 0.810 | 0.772
  Z = 0.90: 10 | 0.545 | 0.528 | 0.492 ; 20 | 0.517 | 0.502 | 0.474 ; 50 | 0.575 | 0.534 | 0.469 ; 100 | 0.594 | 0.560 | 0.498 ; 159 | 0.601 | 0.574 | 0.522 ; 318 | 0.628 | 0.604 | 0.552
  In Earth radii: e.g. 10 M⊕, Z = 0.90, non-irradiated: 4.28 / 4.20 / 4.00 R⊕ at 0.5/1/5 Gyr; irradiated: 6.11 / 5.92 / 5.52 R⊕; 20 M⊕, Z = 0.50, irradiated: 10.5 / 9.98 / 8.97 R⊕. NB: no 10 Myr or 100 Myr tabulated values exist in the paper; figures start at log t = 8 (100 Myr) and tables at 0.5 Gyr.
- Fig. 3a (p. 8; 20 M⊕, Z = 0.5 in a 10 M⊕ core, Z_env = 0, ANEOS), READ FROM FIGURE: water core 1.10 R_J at 100 Myr → 0.89 at 1 Gyr → 0.75 at 10 Gyr; rock core 1.03 → 0.84 → 0.71; iron core 0.98 → 0.80 → 0.68. Fig. 12 (p. 17) shows M-R at 0.5/1/5 Gyr for 10-318 M⊕ with observed transits.
- Table 1 (p. 7; 20 M⊕, Z = 0.5, 1 Gyr): M_core = 10 M⊕ water(ANEOS)/Z_env = 0: R = 0.890 R_J (T_c = 1.1×10⁴ K, ρ_c = 4.11 g cm⁻³); water(SESAME) 0.901; rock(ANEOS) 0.836; rock(SESAME) 0.838; iron(ANEOS) 0.799. No core, Z_env = 0.5: SCVH Y_equiv = 0.775: 0.953; AVL SESAME+water: 0.858; AVL ANEOS+water: 0.669. M_core = 8 M⊕ water + Z_env = 0.166: Y_equiv(0.441) 0.876; AVL SESAME 0.862; AVL ANEOS 0.811.
- Table 2 (p. 9; 1 M_Jup, 1 Gyr): Z = 0.5, core 159 M⊕ water(ANEOS) 0.861 R_J; water(SESAME) 0.841; rock 0.802/0.789; iron 0.746; no core Z_env = 0.5: Y_equiv 0.782, ANEOS-AVL 0.765, SESAME-AVL 0.811. Z = 0.2: core 63.6 M⊕ water: 1.026; no-core Y_equiv 0.994, ANEOS-AVL 0.986, SESAME-AVL 1.006.

### 5.3 Water in the core vs mixed in the envelope (Sect. 4, pp. 5-11; Sect. 8, pp. 17-18)
- Neptune-mass (20 M⊕) conclusions (p. 7): (i) for core mass < 50 % of the planet, changing the core from pure water to pure iron changes R by < ~10 % after 1 Gyr (rock: 6 %, iron: 11 % smaller than water at 1 Gyr); (ii) Z_env ≲ 20 % can be mimicked with Y_equiv; (iii) for Z ≲ 15 % (global or in the envelope) the distribution (all in core vs mixed) changes R by ≲ 2 % — except with the ANEOS EoS which gives ~10 % (ANEOS-AVL cools much faster: ~10× larger −T dS/dt initially, ~6-10 % smaller R at 1 Gyr); (iv) for Z ≳ 15 % the distribution and the mixture thermodynamics change R by > 10 % after 1 Gyr (e.g. 0.953 vs 0.669 R_J in Table 1; with AVL+SESAME core vs mixed differ by ~4 % at 1 Gyr, 7 % at 5 Gyr).
- Jupiter-mass: core composition water→rock(iron) changes R by ≲ 7 % (15 %); Z = 20 % — treatment < 2 %, distribution up to 4 %; Z = 50 % up to 12 % (core vs mixed with ANEOS) (p. 9). A 10 M⊕ core + rest mixed in the envelope evolves like "all mixed, no core".
- Core heat release (Sect. 4.3, pp. 10-11): water heat capacity in cores C_v ~ 3×10⁷-5×10⁷ erg g⁻¹ K⁻¹ (T ~ 5000-5×10⁴ K, P ~ 10¹²-10¹⁴ dyn cm⁻²), about 1/3 of H/He; release of core gravitational (P dV/dt) + internal (dU/dt) energy never exceeds 40 % of the total for 20 M⊕-1 M_Jup with cores < 50 % of the mass. Imposing a cold (300 K) isothermal core: < 2 % on R for 1 M_Jup, up to 6 % (SESAME, 10 M⊕ core in 20 M⊕) at 1 Gyr; ~10 % for GJ 436b-like Z > 90 %. Conduction (K_c ∝ ρ^{4/3}) may dominate in the core after a few Gyr; forcing an isothermal core changes R by ≤ 3 %.
- GJ 436b (Table 3, p. 14; 22.6 M⊕ with 21 M⊕ water core + 1.6 M⊕ H/He, 2 Gyr): no irradiation — ANEOS 0.396 R_J, ANEOS T=300 K 0.379, SESAME 0.381, SESAME T=300 K 0.358, Seager 2007 pure water 22.6 M⊕ 0.285; irradiated at 6× F_inc(GJ 436b) — ANEOS 0.452, ANEOS T=300 K 0.421, SESAME 0.446, SESAME T=300 K 0.397 (cold core ⇒ 7-11 % smaller). Core T ranges 5000 → 2×10⁴ K (irradiated), 3000 → 10⁴ K (non-irradiated). Fig. 10: the core supplies ~90 % of the gravothermal energy of GJ 436b at all ages.
- p. 18: "a 10 M⊕ mass planet retaining a 10 % H/He envelope is ~1.5 times larger than its pure icy counterpart (Seager et al. 2007)"; "even a modest fraction (~10 %) of H/He already severely modifies the evolution and thus the radius". Water in these interiors is mostly supercritical/liquid; ANEOS predicts liquid→solid transition in an iron core at ~1 Gyr (T ~ 1.7×10⁴ K, ρ ~ 30 g cm⁻³) (p. 6).

## 6. Mordasini, Alibert, Georgy, Dittkrist, Klahr & Henning 2012, A&A 547, A112 (arXiv:1206.3303, "Paper II") — Characterization of exoplanets from their formation II: the planetary mass-radius relationship
(page numbers = arXiv manuscript pages, 35 pp. Companion "Paper I" = Mordasini et al. 2012b, A&A 547, A111, contains the envelope structure equations, cooling scheme and the atmospheric boundary conditions.)

### 6.1 Solid core model (Sect. 2.1, pp. 3-5)
- Modified polytropic EoS (Seager et al. 2007): ρ(P) = ρ0 + c P^n (1), with the Seager parameters for iron, MgSiO3 (perovskite) and water ice; differentiated core: iron/nickel, silicates, and ice (if accreted outside the ice line); silicate:iron = 2:1 by mass ("rocky", Earth-like); "icy" = 75 % ice + 25 % rocky (Hayashi 1981). No internal temperature profile (≲ 1.5 % on R for rock; ≲ 3 % in density for ice, i.e. ~1 % in R, since R ∝ ρ̄^{−1/3}). External pressure of the envelope compresses the core (Lane-Emden with P_ext).
- Fig. 1 (p. 4, READ FROM FIGURE): rocky planets, no P_ext: 0.1 M⊕ ≈ 0.45 R⊕, 1 M⊕ = 0.96 R⊕ (text), 10 M⊕ ≈ 1.85, 100 M⊕ ≈ 2.95, maximum ≈ 3.25 R⊕ near 500 M⊕ (then decreasing). 50 % ice: 1 M⊕ ≈ 1.15, 10 ≈ 2.2, 100 ≈ 3.7; pure ice: 1 M⊕ ≈ 1.4, 10 ≈ 2.65, 100 ≈ 4.15, 1000 M⊕ ≈ 4.8 R⊕. Fig. 2 (p. 5): R rises ~linearly with f_ice; R(f_ice = 1)/R(f_ice = 0) = 1.44 without external pressure (Fortney 2007 agrees), 1.19 inside a Jupiter (P_ext = 4×10¹³ dyn cm⁻²) and 1.15 inside a 10 M_Jup planet (6×10¹⁵ dyn cm⁻²); R is independent of P_ext up to ~10¹⁰ Pa (low core mass) - 10¹² Pa (high core mass), then drops. A 10 M⊕ core inside Jupiter has R ≈ 1.6 R⊕ (ρ̄ ≈ 12-14 g cm⁻³); inside a 10 M_Jup planet ≈ 0.75 R⊕ (ρ̄ ≈ 130 g cm⁻³). Agreement with Seager et al. 2007: 1-2 % for M < ~200 M⊕ (rocky) and < ~60 M⊕ (ice); 3 % smaller for pure ice at 100 M⊕.

### 6.2 Radius uncertainties and gray-atmosphere check (Sect. 2.2, pp. 5-7)
- All solids in the core vs. mixed: ~10 % on R for a Neptunian planet with Z = 20 % (Baraffe 2008); 4 % / 12 % for Jovian Z = 20 % / 50 %; solids-in-core gives the larger radius.
- Fig. 3 (p. 6; equilibrium models with intrinsic L/M = 10^{−6.5} erg g⁻¹ s⁻¹ as in Rogers et al. 2011; icy core f_ice = 0.67 in left/middle panels, rocky right): envelope mass fractions f = M_XY/M = 0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5. Total radii vs Rogers et al. 2011 (two-stream Guillot 2010 atmosphere): at 20 M⊕ 2 % larger; at 4 M⊕ f = 0.05: 7 % larger, f = 0.5: ~25 % larger. Gray atmosphere error ≲ 15 % right of the dotted line (T_eq = 250 K panels). READ FROM FIGURE (T_eq = 500 K, icy core): core alone ≈ 1.3 R⊕ (1 M⊕) → 2.8 (20 M⊕); f = 0.01: ≈ 3.3 R⊕ at 3 M⊕, ≈ 3.2 at 10 M⊕, ≈ 3.3 at 20 M⊕ (nearly flat); f = 0.05: ≈ 5 R⊕ at 3 M⊕, ≈ 4.5 at 10 M⊕; f = 0.1: ≈ 6.5 at 3 M⊕, ≈ 5.5 at 10 M⊕; f = 0.2: ≈ 8 at 5 M⊕, ≈ 7 at 20 M⊕; f = 0.5: > 10 R⊕ for M ≲ 10 M⊕ (unbound at low mass). In the synthesis, mean f ≈ 0.05 at 4 M⊕ and no planet has f > 0.2 there (gray-atmosphere overestimate ~10 %).

### 6.3 Radiogenic heating prescription (Sect. 2.3, pp. 7-8) — THE KEY EQUATIONS
- Core luminosity during planetesimal accretion: L_core,acc = G M_Z Ṁ_Z / R_core (2). Once accretion stops, L_core = L_radio (cooling/contraction of the core and impact heat neglected; surface loss assumed in equilibrium with instantaneous production — "no delayed secular cooling").
- Q(t) = Q0 e^{−λt} (3), λ = ln2/t_1/2; Q_tot(t) = Q_{0,K} e^{−λ_K t} + Q_{0,U} e^{−λ_U t} + Q_{0,Th} e^{−λ_Th t} (4); L_radio(t) = Q_tot(t) · f_mantle · f_rocky · M_Z (5), with f_mantle = 2/3, f_rocky = 1 − f_ice, M_Z = total core mass; chondritic composition (Wasserburg et al. 1964), data from Lowrie (2007); compatible with Prialnik et al. 1987.
- Table 1 (p. 7): nuclide | Q0 [erg g⁻¹ s⁻¹ per gram of chondritic material at t = 0] | λ [Gyr⁻¹]
  ⁴⁰K   | 3.723×10⁻⁷ | 0.543
  ²³⁸U  | 2.899×10⁻⁸ | 0.155
  ²³²Th | 1.441×10⁻⁸ | 0.0495
  ²⁶Al  | 2.13×10⁻³  | 966.732   (NOT included in the model; given for reference: ²⁶Al/²⁷Al = 5×10⁻⁵, 1.2 wt % Al in silicates; a fully assembled rocky 1 M⊕ at t = 0 would have L ≈ 2.5 L_Jup and T_surf ≈ 414 K)
  ²³⁵U (t_1/2 = 0.47 Gyr) is not included (explains why Nettelmann 2011 get 2.7×10²¹ erg s⁻¹ at t = 0 vs 1.65×10²¹ here).
- Checks: Earth-like planet (f_mantle = 2/3, f_rocky = 1, M_Z = 1 M⊕) → L_radio = 2.26×10²⁰ erg s⁻¹ at 4.5 Gyr (Valencia 2009 agree; Nettelmann 2011: 2.3×10²⁰) and 1.65×10²¹ erg s⁻¹ at t = 0 (factor 7.3; Wasserburg 1964: 4.5-8.2). Fig. 4 (p. 8): Q_tot ≈ 4.2×10⁻⁷ erg g⁻¹ s⁻¹ at t = 0 (K dominant by ~1 dex), ≈ 3×10⁻⁸ at 4.5 Gyr, ≈ 1.6×10⁻⁸ at 10 Gyr; K crosses below Th at ~6.5 Gyr and below U at ~7 Gyr.
- Origin of time (p. 8, quoted): "The time corresponding to t = 0 is not very well defined in our simulations. For example, the distribution of initial disk masses is based on observations of YSO in ρ Ophiuchi, which is about 1 Myr old (Andrews et al. 2009)." t = 0 = start of the formation calculation (disk + 0.6 M⊕ embryo); the radiogenic clock runs from t = 0 of the formation simulation; total simulation length 10 Gyr (Table 2, p. 14).

### 6.4 Boundary conditions and model settings (Sect. 6, pp. 12-13; Sect. 7.1 & Table 2, p. 14)
- Envelope: Paper I structure equations with a simple gray atmosphere; "cold start" (accretion shock radiates all liberated energy); constant luminosity within the envelope (dl/dr = 0); grain opacity 0.003× interstellar (Mordasini 2012c), gas opacity Freedman 2008; no deuterium burning, no envelope evaporation, no outgassing, no atmospheric mass loss; stellar mass 1 M☉; inner edge of the computational disk 0.1 AU (no planets inside 0.1 AU); disk viscosity α = 7×10⁻³; embryo 0.6 M⊕; core density variable; radioactive luminosity included; type I migration non-isothermal, transition to type II by Crida et al. 2006 criterion; one embryo per disk; 10 Gyr duration.
- Stellar irradiation: at 0.1 AU around a solar-like star with the albedo assumed in Paper I, the planet's surface (outer boundary) temperature during the evolutionary phase is ≈ 790 K, "virtually constant" (intrinsic contribution negligible; temporal variation of stellar luminosity NOT considered, p. 13). T_eq = 500 K ≈ 0.3 AU, T_eq = 250 K farther out (Fig. 3 caption).
- Core-envelope: variable core density (10-15 g cm⁻³ for Jupiter's core vs the old constant 3.2 g cm⁻³) — R_core differs by 0.13 R_J, total Jupiter radius by 0.06 R_J at late times (Fig. 5, p. 11). Jupiter's radius decreases by ≈ 0.4 R⊕ between 1 and 5 Gyr (p. 18).

### 6.5 Worked super-Earth evolution with radiogenic heating (Sect. 6, Fig. 6, pp. 12-13)
- Case: M_Z = 4.2 M⊕ rocky core (R_core = 1.46 R⊕), M_XY = 0.045 M⊕ (≈ 1 % H2/He), migrated to ≈ 0.1 AU, T_surf ≈ 790 K, no mass loss. Time-line: accretion of solids and gas ceases at ≈ 4 Myr (disk gone); radius in the attached phase ~15-20 R⊕ (READ FROM FIGURE) collapses rapidly to ≈ 3.5 R⊕, then slow contraction: 2.34 R⊕ at the epoch where L/M = 10^{−6.5} erg g⁻¹ s⁻¹; 2.2 R⊕ at 4.6 Gyr; inset (READ FROM FIGURE): ≈ 2.37 R⊕ at 10⁸ yr, ≈ 2.31 at 10⁹ yr, ≈ 2.25 at 3×10⁹ yr, ≈ 2.17 at 10¹⁰ yr. Contraction visibly slowed between ~0.2 and 2 Gyr by L_radio.
- Luminosity: L/M = 6.6×10⁻⁶, 5.2×10⁻⁷, 1.7×10⁻⁷, 1.1×10⁻⁸ erg g⁻¹ s⁻¹ at 0.01, 0.1, 1, 10 Gyr (the 1 and 10 Gyr values are just Eq. 5). L_radio becomes the dominant luminosity source at ≈ 400 Myr → plateau of roughly constant L ≈ 10^{−2.7} L_Jup ≈ 10^{22.2} erg s⁻¹ (READ FROM FIGURE; L_Jup = 8.7×10⁻¹⁰ L☉ ≈ 3.35×10²⁴ erg s⁻¹) until a few Gyr, then declines with the decay law. Core-envelope interface temperature 6700 K at 5 Myr → ≈ 1500 K at 16 Gyr; envelope fully radiative after ≈ 7 Gyr (Fig. 7, p. 13).
- Comparison with Rogers et al. 2011 (4 M⊕ + 1 % envelope, L/M = 10^{−6.5}): they get 2.7 R⊕ (T_eq = 500 K) and 3.3 R⊕ (1000 K) with an icy core (R_core ≈ 1.9 R⊕); Mordasini gets 2.34 R⊕ with a rocky core (1.46 R⊕): agreement to ≈ 0.2 R⊕ (~7 %) once the core radii are accounted for. H2 outgassing potential for such a rocky planet: 0.2 wt % = 0.0084 M⊕, i.e. ~5× less than the primordial envelope.

### 6.6 Population synthesis M-R evolution (Sect. 7.2-7.4, pp. 14-20; Figs. 8-10)
- Formation phase (Fig. 8): attached low-mass planets at 1 Myr have R ≈ R_Hill ~ 100-1000 R⊕; smallest R for M < 10 M⊕ at 1 Myr ≈ 7 R⊕; at 2 Myr some low-mass planets have already contracted to 2-3 R⊕ after their disk disappeared; by 8 Myr nearly all have. Giant planets in runaway: 20-30 R⊕ (2-3 R_J). Low-mass planets (M ≲ 10 M⊕) contain less than ~20 % gas; transition to giants at 40-60 M⊕.
- Evolution phase (Fig. 9: 10 Myr, 50 Myr, 100 Myr, 500 Myr, 1 Gyr, 5 Gyr): at 10 Myr close-in low-mass gas-rich planets (up to 20 % gas) still 5-10 R⊕, sometimes > 15 R⊕; the characteristic "S" shape appears by 50 Myr; between 500 Myr and 5 Gyr the relative shape hardly changes. At 5 Gyr: 40 M⊕ planets span 3-9 R⊕ (factor 3); giant-planet maximum ≈ 12 R⊕ near 4 M_Jup. Radius spread at fixed mass at late times reflects heavy-element content Z (diagonal colour bands).
- Table 3 (p. 20; derived Z = M_Z/M at 5 Gyr, closest synthetic planet): Kepler-11f (2 M⊕) ~0.95; Kepler-11d (6 M⊕) 0.88; Kepler-20d ~0.96; Kepler-11e (8 M⊕) ~0.78; Kepler-10c ~0.99; Kepler-11c 0.98; Uranus 0.88; Kepler-18d (16.4 M⊕) ~0.50 (Z range 0.43-0.52); Neptune 0.90; Kepler-35b ~0.37; Kepler-9c 0.25; Kepler-34b 0.35; Kepler-9b 0.30; Saturn 0.27; Jupiter 0.10; CoRoT-10b 0.17; HD 17156b ~0.08; HD 80606b 0.09. Kepler-11 planets reproduced with ~1-20 % envelopes.

### 6.x Population-level radius statistics (Sect. 7.5-7.10, pp. 21-30) — all planets have primordial H2/He envelopes
- Table 4 (p. 21): normalized radius distribution for R > 2 R⊕ at 1, 5, 10 Gyr (bins in R⊕ | fraction 1 / 5 / 10 Gyr): 2.11|0.134/0.219/0.202; 2.31|0.157/0.137/0.134; 2.54|0.134/0.113/0.135; 2.78|0.101/0.105/0.088; 3.05|0.082/0.077/0.060; 3.34|0.078/0.055/0.053; 3.66|0.059/0.047/0.052; 4.02|0.050/0.037/0.039; 4.41|0.037/0.026/0.027; 4.83|0.023/0.019/0.022; 5.30|0.017/0.016/0.019; 5.81|0.014/0.017/0.020; 6.37|0.014/0.013/0.013; 6.98|0.009/0.009/0.010; 7.66|0.008/0.007/0.008; 8.39|0.007/0.009/0.011; 9.20|0.008/0.009/0.012; 10.09|0.009/0.018/0.022; 11.07|0.022/0.041/0.056; 12.13|0.039/0.024/0.017; 13.30|0/0/0.
- Evolution of radii at t ≳ 1 Gyr is slow; between 1 and 5 Gyr the giant-planet peak shifts by ~0.1 R_Jup (p. 22). Low-mass planets with even tenuous H2/He (0.1-1 % of core mass) have R ≥ 2 R⊕ at a < 0.27 AU (p. 22). A 1 % H2/He envelope strongly increases the radius; with f_opa = 0.003, 5 M⊕ cores accrete ~15 % envelopes (p. 27).
- Eq. (23) p. 25: R/R⊕ = k (M/M⊕)^β. Mean radius fit (Traub 2011 form), Eq. (24) p. 26:
  R̄(M) = b / (1 + |log(M/M0)/w|^p)   (log10; Earth units; fitted at 5 Gyr, M > 2 M⊕)
  Table 5: 0.1 < a/AU: b = 11.684 R⊕, M0 = 1756.7 M⊕, w = 1.646, p = 2.489; 0.1 < a/AU ≤ 1: b = 11.858, M0 = 1308.7, w = 1.635, p = 2.849. Extrapolated to 1 M⊕ gives 1.8 / 1.6 R⊕ (envelope-bearing planets only).
  Eq. (25): β(M) = p (|log(M/M0)|/w)^p / [ln(M0/M) (1 + (|log(M/M0)|/w)^p)]. β ≈ 0.3-0.33 for M ≲ 30 M⊕ (all a), 0.35-0.4 inside 1 AU; β → 0 at ~4 M_Jup; negative beyond.
- Table 6 (p. 27; radius statistics at 5 Gyr, 0.1 < a/AU ≤ 3): mass bin M⊕ | mean R⊕ | σ | skewness: 2-5|2.58|0.36|1.21; 5-10|3.15|0.55|−0.12; 10-20|4.23|0.74|1.04; 20-30|5.89|0.75|−0.09; 30-50|7.13|0.64|−0.01; 50-100|8.69|0.76|−0.52; 100-300|9.85|0.74|−0.36; 300-3000|11.39|0.58|−1.15; >3000|11.06|0.46|−0.72.
- p. 29: Baraffe et al. 2008 cited: for low core-mass fractions it is not important for the evolution whether solids sit in the core or are mixed in the envelope (Sect. 2.2.2). Compression of the core by the envelope becomes visible for 10-100 M⊕ (Fig. 16).
- Summary p. 30: "simple model for the core luminosity due to the decay of long-lived radionuclides. We assume a chondritic composition of the mantle and take into account the temporal decay of the nuclides (Sect. 2.3) ... for a low-mass, close-in super-Earth planet with a ~1 % primordial H2/He atmosphere, the radioactive decay becomes the dominant intrinsic heat source at late times"; compared with Rogers et al. 2011 (Sect. 6).
- Appendix A (p. 31): disk profile Σ(r,0) = Σ0 (r/5.2 AU)^{−0.9} exp[−(r/30 AU)^{1.1}]; M_d(0) = 0.012 (Σ0/100 g cm⁻²) M☉.

## 7. Cross-paper cheat-sheet for the web page (what to wire where)
- Star/time axis: L_bol(t) from Baraffe tracks (Luger & Barnes use Baraffe 1998; BHAC15 file is in the same folder); XUV: L_XUV/L_bol = 10⁻³ until t_sat (1 Gyr for M ≤ 0.6 M☉, 0.1 Gyr for K/G), then ∝ (t/t_sat)^{−1.23}; F⊕(XUV, today) = 4.64 erg cm⁻² s⁻¹. Alternative (Aguichine, Sanz-Forcada 2011): L_X = 6.3×10⁻⁴ L★ until τ_sat = 5.72×10¹⁵ L★^{−0.65} Gyr, then 1.89×10²¹ τ^{−1.55}; L_EUV = 10^{3.8} L_X^{0.86}.
- Water loss: Ṁ_EL = ε π F_XUV R_p³/(G M_p K_tide) with ε = 0.30 (0.15); O-drag switch at F_crit = 180 (M/M⊕)² (R/R⊕)⁻³ (ε/0.30)⁻¹ erg cm⁻² s⁻¹; H/O split via η = (x−1)/(x+8), x = kT F_H^ref/(10 b g m_H), b = 4.8×10¹⁷ T^0.75 cm⁻¹ s⁻¹, T = 400 K; O2 build-up 5.35 (M/M⊕)² (R/R⊕)⁻⁴ bar/Myr when F ≥ F_crit; 1 TO = 1.39×10²⁴ g = 270 bar.
- Runaway threshold (steam vs condensed): S_eff ≈ 1.1 S⊕ for Sun-like (Turbet, Kopparapu 2013); above it use Turbet Eq. (2)+(3) (coefficients in Sect. 3.2-3.3) for z_atm, or Aguichine's grid/fit (T_irr 400-1300 K, 1-20 M⊕) for WMF 10-100 %.
- Radius inflation magnitudes: 1 % steam on 1 M⊕ ≈ +10 % R (≈ 25 % condensed water); 5 % steam ≈ +20 % (≈ 100 % condensed) (Turbet Fig. 2). Supercritical 100 % water at 17 M⊕: 3.25 R⊕ (400 K) → 3.6 R⊕ (1300 K); 20 % supercritical ≡ 50 % liquid at 10-20 M⊕ (Aguichine).
- Thermal evolution: water-dominated envelopes barely contract (< 1 % after 1 Gyr; Valencia), H/He envelopes contract by ~×2 in R from 30 Myr to 10 Gyr at 6 M⊕ with 50 % envelope, or 3.6 → 2.6 R⊕ for a 3 % envelope (Valencia Fig. 5); Baraffe tables give R(0.5/1/5 Gyr) for 10-318 M⊕ at Z = 2-90 % water (irradiated and not).
- Radiogenic floor: L_radio(t) = M_Z f_mantle f_rocky Σ Q0,i e^{−λ_i t} with (Q0, λ) = K (3.723×10⁻⁷, 0.543), U (2.899×10⁻⁸, 0.155), Th (1.441×10⁻⁸, 0.0495) [erg g⁻¹ s⁻¹, Gyr⁻¹]; 1 M⊕ Earth → 1.65×10²¹ erg s⁻¹ (t = 0), 2.26×10²⁰ (4.5 Gyr); dominates the intrinsic luminosity of a 4 M⊕ + 1 % H/He planet after ~400 Myr (Mordasini).
