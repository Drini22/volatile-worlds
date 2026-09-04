# Stellar X-ray / EUV / XUV evolution ingredients

Extracted 2026-09-04 from the three PDFs in `/Users/drinorcacaj/Documents/Phd_Bern/papers/evolution/`.
All coefficients copied verbatim from the text layer (pdftotext); page numbers are PDF page numbers of the arXiv versions.
Values marked **[FIG]** are read by eye from a figure and carry roughly +/-0.1-0.15 dex uncertainty. Values marked **[DERIVED]** are my arithmetic from the paper's coefficients, not numbers printed in the paper.

Symbols: L_X, L_EUV in erg s^-1; t = age; R_X = L_X/L_bol; Ro = P_rot/tau_c (Rossby number); Omega_sun = solar rotation rate.

---

## 1. Jackson, Davis & Wheatley 2012, MNRAS (arXiv:1111.0031) - coronal X-ray-age relation

Sample: 717 stars in 13 open clusters, ages 5-740 Myr, 0.29 <= (B-V)_0 < 1.41 (F, G, K). ROSAT/Chandra/XMM L_X (bands not homogenised). Fits are broken power laws in (B-V)_0 colour bins, saturated part forced flat.

### 1.1 Master formula (Eq. 1, p. 7)

```
L_X / L_bol = (L_X/L_bol)_sat                       for t <= tau_sat
L_X / L_bol = (L_X/L_bol)_sat * (t / tau_sat)^(-alpha)   for t >  tau_sat
```
with (L_X/L_bol)_sat, tau_sat, alpha per colour bin from Table 2. L_bol assumed constant in time (they note this underestimates the saturated-phase energy of PMS stars by up to ~2x, p. 11-12).

### 1.2 Table 2 (p. 6) - verbatim

| (B-V)_0 bin | N stars | log(L_X/L_bol)_sat (+/-fit +/-scatter) | log tau_sat [yr] (+/-fit +/-scatter) | alpha (power-law index) |
|---|---|---|---|---|
| 0.290 <= (B-V)_0 < 0.450 | 67  | -4.28 +/- 0.05 +/- 0.40 | 8.00 +/- 0.09 +/- 0.28          | 1.19 +/- 0.23 |
| 0.450 <= (B-V)_0 < 0.565 | 97  | -4.24 +/- 0.02 +/- 0.36 | 8.35 +/- 0.03 +/- 0.17  (8.30)  | 1.22 +/- 0.03 |
| 0.565 <= (B-V)_0 < 0.675 | 92  | -3.67 +/- 0.01 +/- 0.41 | 7.59 +/- 0.02 +/- 0.22          | 0.91 +/- 0.05 |
| 0.675 <= (B-V)_0 < 0.790 | 79  | -3.71 +/- 0.05 +/- 0.45 | 8.03 +/- 0.04 +/- 0.31          | 1.29 +/- 0.04 |
| 0.790 <= (B-V)_0 < 0.935 | 109 | -3.36 +/- 0.02 +/- 0.36 | 7.87 +/- 0.03 +/- 0.28          | 1.30 +/- 0.05 |
| 0.935 <= (B-V)_0 < 1.275 | 220 | -3.34 +/- 0.01 +/- 0.36 | 8.25 +/- 0.07 +/- 0.27  (8.27)  | 0.93 +/- 0.24 |
| 1.275 <= (B-V)_0 < 1.410 | 55  | -3.15 +/- 0.02 +/- 0.30 | 8.21 +/- 0.02 +/- 0.22  (8.21)  | 1.18 +/- 0.04 |

Values in parentheses: alternative turn-off age when the unsaturated slope is fixed at alpha = 1 (used for bins with few unsaturated clusters). Second error = intrinsic scatter about the mean.

tau_sat in Myr **[DERIVED]**: 100, 224, 39, 107, 74, 178, 162 Myr respectively (top to bottom).
Mean alpha over all bins: 1.19 +/- 0.05 (p. 7). No trend of alpha or tau_sat with colour; tau_sat "consistent with a scatter around an age of ~100 Myr" (p. 6). Saturated ratio falls from 10^-3.15 (late K) to 10^-4.28 (early F).

### 1.3 Colour -> mass mapping for the web page (my assignment, NOT in the paper)
- 1.0 Msun (G2, (B-V)_0 ~ 0.65): bin 0.565-0.675 -> log(L_X/L_bol)_sat = -3.67, tau_sat = 10^7.59 yr = 39 Myr, alpha = 0.91.
- 0.6 Msun (~K5-K7, (B-V)_0 ~ 1.15-1.3): bin 0.935-1.275 -> -3.34, tau_sat = 10^8.25 yr = 178 Myr, alpha = 0.93 (or fixed alpha = 1 with log tau_sat = 8.27).
- 0.3 Msun (M3-M4, (B-V)_0 ~ 1.5-1.6): OUTSIDE the fitted range. Nearest bin 1.275-1.410 -> -3.15, tau_sat = 10^8.21 yr = 162 Myr, alpha = 1.18. Paper (p. 8) notes P03 found early-mid M dwarfs have saturated ratios "very similar to that of late K stars" but with "significantly longer saturated periods". Use Johnstone 2021 for M dwarfs instead.

### 1.4 Integrated X-ray energy (Eqs. 6-8, p. 11)
```
E_X^sat   = L_bol (L_X/L_bol)_sat tau_sat                                          (6)
E_X^unsat = 1/(alpha-1) L_bol (L_X/L_bol)_sat tau_sat [1 - (tau_sat/t0)^(alpha-1)]  (7)
E_X^tot   = 1/(alpha-1) L_bol (L_X/L_bol)_sat tau_sat [alpha - (tau_sat/t0)^(alpha-1)]  (8)
```
t0 = present age. Saturated phase typically ~30 % of lifetime X-ray energy; ~75 % of the total is emitted in the first Gyr for a 4 Gyr star (p. 14).

### 1.5 EUV in Jackson 2012
**None.** They explicitly consider X-rays only: "we concentrate here solely on evaporation induced by stellar X-ray emission, but note that neglecting EUV emission may result in the underestimation of the total energy" (Sec. 3.3, p. 12). No X-ray -> EUV conversion is applied. (Their energy-limited mass-loss Eq. 2/5 uses L_X alone: mdot = eta 4 L_X R_P^3 / (3 G M_P <a>^2 K(eps)).)

---

## 2. Tu, Johnstone, Guedel & Lammer 2015, A&A 577, L3 (arXiv:1504.04546) - XUV Sun in time

Solar-mass star (0.9-1.1 Msun), rotational evolution model + Rossby-activity relation; three tracks = 10th / 50th / 90th percentiles of the rotation distribution (slow / medium / fast).

### 2.1 Activity relation used (Eq. 1, p. 2) - from Wright et al. 2011 (W11)
```
R_X = L_X/L_bol = C Ro^beta        if Ro >= Ro_sat
R_X = R_X,sat                       if Ro <= Ro_sat
Ro_sat = 0.13,  R_X,sat = 10^-3.13,  beta = -2.7
```
Continuity gives C = R_X,sat Ro_sat^(-beta) = 10^-3.13 * 0.13^2.7 = 3.00e-6 **[DERIVED]**.
Ro = P_rot / tau_star, tau_star from Spada et al. 2013 renormalised so the MS value matches W11 (they are ~2x too large for 1 Msun). L_bol(t), R_star(t), I(t) from Spada et al. 2013. Omega_sun = 2.9e-6 rad s^-1 (p. 2).

### 2.2 EUV conversion (p. 2) - from Sanz-Forcada et al. 2011
```
log L_EUV = 4.8 + 0.86 log L_X          (L_X: 5-100 A;  L_EUV: 100-920 A;  erg s^-1)
```

### 2.3 Saturation
- Saturation level: L_X,sat ~ 10^-3.13 L_bol,sun -> **log L_X,sat = 30.46** (L_X,sat = 2.88e30 erg s^-1) assumed constant in time (p. 3). **[DERIVED]** L_EUV,sat = 10^(4.8+0.86*30.46) = 9.9e30 erg s^-1.
- Saturation time vs initial rotation (Eq. 2, p. 3):
```
t_sat = 2.9 Omega_0^1.14      [t_sat in Myr, Omega_0 = rotation rate at 1 Myr in Omega_sun units]
```
- Initial rotation percentiles (p. 3): Omega_0 ~ 1.8, 6.2, 45.6 Omega_sun for 10th, 50th, 90th -> t_sat ~ 5.7, 23, 226 Myr. (Fig. 2b model curves leave saturation at ~6, ~20, ~300 Myr respectively.)
- Model ingredients (p. 2): Mdot_star ∝ R_star^2 Ro^-2, B_dip ∝ Ro^-1.32 (Vidotto+2014), core-envelope coupling times 30/20/10 Myr and disk-locking 10/5/2 Myr for 10th/50th/90th; Fig. 3 caption fits tau_CE = 38 Omega_0^-0.34 Myr, t_disk = 13.5 Omega_0^-0.5 Myr.

### 2.4 Power-law tracks (Eqs. 3-4 and the unnumbered system on p. 3)
```
L_X = L_X,sat                 if t <= t_sat
L_X = a t^b                   if t >= t_sat                                  (3)
b^-1 = 0.35 log Omega_0 - 0.98,     a = L_X,sun t_sun^(-b)                    (4)
```
anchored on the Sun: L_X,sun = 10^27.2 erg s^-1 at t_sun = 4570 Myr. For the three percentiles (t in Myr, L in erg s^-1, valid for t > t_sat):

| track | Omega_0 | t_sat | L_X(t) | L_EUV(t) |
|---|---|---|---|---|
| 10th (slow)   | 1.8 Omega_sun  | 5.7 Myr | 2.0e31 t^-1.12 | 7.4e31 t^-0.96 |
| 50th (medium) | 6.2 Omega_sun  | 23 Myr  | 2.6e32 t^-1.42 | 4.8e32 t^-1.22 |
| 90th (fast)   | 45.6 Omega_sun | 226 Myr | 2.3e36 t^-2.50 | 1.2e36 t^-2.15 |

Median slope b = -1.42 agrees with Sun-in-Time regressions (Guedel+1997, Ribas+2005).

### 2.5 Track values at representative ages **[DERIVED from the power laws above; saturated value where t < t_sat]**

| age | L_X slow | L_X medium | L_X fast | L_EUV slow | L_EUV medium | L_EUV fast |
|---|---|---|---|---|---|---|
| 10 Myr  | 1.5e30 | 2.9e30 (sat) | 2.9e30 (sat) | 8.1e30 | 9.9e30 (sat) | 9.9e30 (sat) |
| 100 Myr | 1.2e29 | 3.8e29 | 2.9e30 (sat) | 8.9e29 | 1.7e30 | 9.9e30 (sat) |
| 1 Gyr   | 8.7e27 | 1.4e28 | 7.3e28 | 9.8e28 | 1.1e29 | 4.3e29 |
| 4.57 Gyr| 1.6e27 | 1.6e27 | 1.6e27 | 2.3e28 | 1.6e28 | 1.6e28 |

Note: the power laws are straight lines from (t_sat, L_sat) to the Sun; the actual model curve in Fig. 2b (p. 3) dips below them at intermediate ages. **[FIG 2b read-off]** slow track: ~1e30 at 10 Myr, ~1.2e29 at 20 Myr, ~5e28 at 100 Myr, ~2e28 at 620 Myr; medium: ~5e29 at 30 Myr, ~3e29 at 100 Myr, ~8e28 at 620 Myr; fast: plateau ~2e30-2.5e30 to ~250 Myr, ~1.3e29 at 620 Myr. All converge to ~1.5e27 at 4.5 Gyr. Observed solar range over the cycle: 6e26-5e27 erg s^-1 (p. 3). Spread between tracks up to 1.5 dex for several 100 Myr.

### 2.6 Solar XUV today
Stated: L_X,sun = 10^27.2 erg s^-1 at 4570 Myr (p. 3). Via the Sanz-Forcada relation L_EUV,sun = 10^28.19 = 1.6e28 erg s^-1 **[DERIVED]**.
At 1 AU **[DERIVED, not stated in paper]**: F_X = 0.56, F_EUV = 5.5, F_X+EUV ~ 6.1 erg s^-1 cm^-2. (The paper's escape example uses F_EUV = 100 erg s^-1 cm^-2 with Mdot_pl = 5.9e6 F_EUV g s^-1 for a 0.5 M_earth planet at 1 AU, p. 4.)

---

## 3. Johnstone, Bartel & Guedel 2021, A&A 649, A96 (arXiv:2009.07695) - Active lives of stars

Masses 0.1-1.2 Msun, 1 Myr to end of MS. Code + full track grid: https://github.com/ColinPhilipJohnstone/Mors . Bands (Sec. 4.1, p. 15): X-ray = 0.1-2.4 keV = 0.517-12.4 nm; EUV = 10-92 nm (EUV1 = 10-36 nm, EUV2 = 36-92 nm); "XUV" = 0.1-92 nm. Omega_sun = 2.67e-6 rad s^-1 (p. 2). Stellar structure (L_bol, R, tau_c, I) from Spada et al. 2013.

### 3.1 Rossby-X-ray relation (Eq. 17, p. 7; fit constants p. 8, Appendix C)
As printed (Eq. 17): R_X = C1 Ro^beta1 if Ro >= Ro_sat ; R_X = C2 Ro^beta2 if Ro <= Ro_sat, with
```
beta1  = -0.135 +/- 0.030      (this is the SATURATED-regime slope; see note)
beta2  = -1.889 +/- 0.079      (unsaturated slope)
Ro_sat = 0.0605 +/- 0.00331
R_X,sat = 5.135e-4 +/- 3.320e-5   (= R_X at Ro = Ro_sat)
C1, C2 fixed by continuity:  R_X,sat = C1 Ro_sat^beta1 = C2 Ro_sat^beta2
```
Note on assignment: the text says "It is common ... to assume R_X has a constant value R_X,sat in the saturated regime, meaning that beta1 = 0" - so beta1 (-0.135) is the saturated-branch slope and beta2 (-1.889) the unsaturated-branch slope, i.e. the printed case order in Eq. 17 should be read as C1 Ro^beta1 for Ro <= Ro_sat and C2 Ro^beta2 for Ro >= Ro_sat. Fig. 4 confirms (flat-ish plateau at low Ro, steep at high Ro).
**[DERIVED]** C1 = 5.135e-4 * 0.0605^(+0.135) = 3.52e-4 ;  C2 = 5.135e-4 * 0.0605^(+1.889) = 2.57e-6.
So: R_X = 3.52e-4 Ro^-0.135 (Ro <= 0.0605), R_X = 2.57e-6 Ro^-1.889 (Ro >= 0.0605).
Ro = P_rot / tau_c with tau_c from Spada et al. 2013 (Fig. 5 upper: tau_c on the MS ~ 400 d at 0.1 Msun, ~500 d at 0.3, ~100 d at 0.6, ~30 d at 1.0, ~7 d at 1.2 **[FIG]**). Their beta2 is shallower than Wright+2011 (-2.18/-2.7) and Reiners+2014 (-2) because of different tau_c.
Spread about the relation: Delta log R_X ~ normal, sigma = 0.359 dex (Sec. 3.2, p. 9); tracks in Fig. 11 are shaded +/-1 sigma.

### 3.2 L_bol dependence
L_X = R_X(Ro) * L_bol(M, t) with L_bol from Spada et al. 2013 tracks. Fig. 17 (p. 19) shows L_bol(t)/L_bol(5 Gyr) **[FIG]**: 0.1 Msun ~ 40x at 1 Myr; 0.3 Msun ~ 20x at 1 Myr -> 1 by ~200-300 Myr; 0.6 Msun ~ 10x at 1 Myr -> 1 by ~100 Myr; 1.0 Msun ~ 2x at 1 Myr, dips to ~0.7 at ~10-20 Myr, ~1 by ~50 Myr.
Consequences (Fig. 5, p. 8, **[FIG]**): saturation L_X,sat = R_X,sat L_bol falls on the PMS and plateaus on the MS at roughly
- 0.1 Msun: 1e29 (1 Myr) -> 3e27 (>=300 Myr)
- 0.3 Msun: ~5e29 (1 Myr) -> ~1e29 (10 Myr) -> ~2e28 plateau (>=200 Myr)
- 0.4 Msun: ~7e29 (1 Myr) -> ~4e28 plateau
- 0.6 Msun: ~1.3e30 (1 Myr) -> ~2.5e29 (10 Myr) -> ~1.5e29 plateau (>=100 Myr)
- 0.8 Msun: ~2e30 (1 Myr) -> ~5e29 plateau
- 1.0 Msun: ~2.5e30 (1 Myr) -> ~1e30 min at ~10 Myr -> bump ~2e30 at ~30 Myr -> ~1.5e30 plateau
- 1.2 Msun: ~4e30 (1 Myr) -> ~3e30 plateau
Saturation rotation rate (Fig. 5 middle **[FIG]**): ~1 Omega_sun for all masses at 1 Myr; MS values ~1 (0.3 Msun), ~2.3 (0.4), ~5 (0.6), ~8 (0.8), ~15 (1.0), ~25 (1.1), ~50 (1.2) Omega_sun. Text (p. 7): "for main-sequence solar mass stars, the saturation threshold is at a rotation rate of approximately 15 Omega_sun".

### 3.3 EUV and Ly-alpha relations (all fluxes are SURFACE fluxes in erg s^-1 cm^-2; F = L / (4 pi R_star^2))
```
T_cor = 0.11 F_X^0.26   [MK]                                        (18), p. 15  (from Johnstone & Guedel 2015)
log F_EUV,1 = 2.04 + 0.681 log F_X          (EUV1 = 10-36 nm)        (19), p. 17
F_EUV,1 / F_X = 110 F_X^-0.319                                        (20), p. 17
log F_EUV,2 = -0.341 + 0.920 log F_EUV,1    (EUV2 = 36-92 nm, Sun only, L_X > 1e27)   (21), p. 17
F_EUV,2 / F_EUV,1 = 0.924 F_EUV,1^-0.0798                             (22), p. 17
log F_Lya = 3.97 + 0.375 log F_X                                      (23), p. 18
F_Lya / F_X = 1.96e4 F_X^-0.681                                       (24), p. 18
```
Total EUV (10-92 nm) = F_EUV,1 + F_EUV,2; EUV2 is ~30-45 % of the total EUV for the Sun, less for active stars (p. 17). Fit method: OLS bisector on the EUVE sample (Table 3, p. 16) plus the Sun binned into 3 activity states. Resulting L_EUV/L_X ratios (Sec. 4.3, p. 19): ~1 at 2 Myr (most stars X-ray dominated), rising to 1.5-4 at 5 Gyr (Sun at maximum 4-7). Flare rate: N(>1e32 erg) = 1.9e-27 L_X^0.95 day^-1 (Eq. 25, p. 22, Audard+2000).

### 3.4 Rotation model essentials (for reproducing tracks)
- Initial (1 Myr) distribution: 1-50 Omega_sun, mass independent above 0.4 Msun (Sec. 7). Slow / medium / fast tracks = **5th / 50th / 95th percentiles of the observed 150 Myr rotation distribution** (all stars within 0.1 Msun of the target mass; Fig. 3 caption, p. 6). (Tu 2015 used 10th/50th/90th.) 0.25 Msun: dashed alternative tracks through NGC 6530 (2 Myr) percentiles.
- Saturation Ro for wind and B_dip too: Ro_sat = 0.0605; B_dip = B_dip,sun (Ro/Ro_sun)^-1.32 with B_dip,sun = 1.35 G (Eq. 6, p. 3); Mdot = f Mdot_sun (R/Rsun)^2 (Ro/Ro_sun)^a_w (M/Msun)^b_w, Mdot_sun = 1.4e-14 Msun/yr, a_w = -1.76, b_w = 0.649 (Eq. 7, p. 3). Wind torque Matt+2012 with K1 = 1.3, K2 = 0.0506, m = 0.2177, K_tau = 11 (Eqs. 4-5, p. 2). Core-envelope coupling t_ce = a_ce |Omega_env - Omega_core|^b_ce (M/Msun)^c_ce, a_ce = 25.6, b_ce = -3.25e-2, c_ce = -0.448 (Eq. 12, p. 4). Disk locking t_disk = 13.5 (Omega_0/Omega_sun)^-0.5 Myr, capped at 15 Myr (Eq. 15, p. 4). Gyrochronology check at 4.5 Gyr: P_rot = a[(B-V)_0 - c]^b t^n, a = 0.407, b = 0.325, c = 0.495, n = 0.566 (Eq. 16, p. 5, Mamajek & Hillenbrand 2008).

### 3.5 Saturation (drop-out) ages by mass - Fig. 10 (p. 13) **[FIG]** and text
| mass | slow (5th) | medium (50th) | fast (95th) |
|---|---|---|---|
| 0.25 Msun | ~1200 Myr | ~1800 Myr | ~2100 Myr |
| 0.3 Msun  | ~1000 Myr | ~1600 Myr | ~1900 Myr |
| 0.5 Msun  | ~100 Myr  | ~500 Myr  | ~900 Myr |
| 0.6 Msun  | ~40 Myr   | ~350 Myr  | ~700 Myr |
| 0.75 Msun | ~20 Myr   | ~50 Myr   | ~500 Myr |
| 1.0 Msun  | ~5 Myr    | ~20-25 Myr | ~250-300 Myr |
Text (p. 14): "By 1 Gyr, most stars with masses > 0.4 Msun and almost all stars with masses > 0.6 Msun are unsaturated. By 5 Gyr, almost all stars are unsaturated, except those with masses of ~0.1 Msun." Solar mass: slow and fast tracks diverge in the first 10 Myr and differ by a factor ~50 for most of the first ~500 Myr. For 0.5 and 0.25 Msun the slow and fast tracks are almost identical until 200 Myr and 2 Gyr respectively. In the first ~10 Myr all stars are saturated regardless of rotation (p. 7).

### 3.6 XUV evolution tracks - Fig. 11 (p. 13) L_X read-offs **[FIG]** (erg s^-1; slow / medium / fast)
Fig. 11 plots 1.0, 0.75, 0.5, 0.25 Msun only. No 0.3 or 0.6 Msun panel; interpolate in log M between 0.25/0.5 and 0.5/0.75, or use Fig. 5 saturation values (Sec. 3.2 above) for the saturated phase.

**1.0 Msun**
| age | slow | medium | fast |
|---|---|---|---|
| 1 Myr   | ~4e30 | ~4e30 | ~6e30 |
| 10 Myr  | ~3e29 | ~1e30 | ~2.5e30 |
| 30 Myr  | ~1.6e29 | ~5e29 (just after drop) | ~2.5e30 (bump) |
| 100 Myr | ~1.3e29 | ~4e29 | ~1.6e30 (sat) |
| 500 Myr | ~8e28 | ~2e29 | ~5e29 |
| 1 Gyr   | ~6e28 | ~9e28 | ~1.6e29 |
| 5 Gyr   | ~1.1e28 | ~1.1e28 | ~1.3e28 |

**0.75 Msun**
| age | slow | medium | fast |
|---|---|---|---|
| 1 Myr   | ~2.5e30 | ~2.5e30 | ~3.7e30 |
| 10 Myr  | ~4e29 | ~4.5e29 | ~4.5e29 |
| 100 Myr | ~1e29 | ~2.5e29 | ~5.6e29 |
| 500 Myr | ~4e28 | ~7e28 | ~4e29 (end of sat) |
| 1 Gyr   | ~2.5e28 | ~3.5e28 | ~8e28 |
| 5 Gyr   | ~5e27 | ~5e27 | ~5e27 |

**0.5 Msun**
| age | slow | medium | fast |
|---|---|---|---|
| 1 Myr   | ~1e30 | ~1.2e30 | ~1.4e30 |
| 10 Myr  | ~3.5e29 | ~4e29 | ~4.3e29 |
| 100 Myr | ~7.5e28 | ~1e29 | ~1.2e29 |
| 500 Myr | ~2.2e28 | ~7e28 | ~8e28 |
| 1 Gyr   | ~1.3e28 | ~2e28 | ~3e28 |
| 5 Gyr   | ~2.2e27 | ~2.2e27 | ~2.2e27 |

**0.25 Msun**
| age | slow | medium | fast |
|---|---|---|---|
| 1 Myr   | ~4.3e29 | ~4.7e29 | ~5e29 |
| 10 Myr  | ~1.4e29 | ~1.4e29 | ~1.4e29 |
| 100 Myr | ~3.5e28 | ~3.5e28 | ~3.5e28 |
| 500 Myr | ~2e28 | ~2e28 | ~2e28 |
| 1 Gyr   | ~1.1e28 | ~1.6e28 | ~1.8e28 |
| 5 Gyr   | ~1.3e27 | ~1.3e27 | ~1.3e27 |

Suggested interpolations for the requested masses **[DERIVED, my log-interpolation of the above]**: 0.3 Msun ~ 0.25 Msun values x 1.2 (saturated plateau ~2e28 per Fig. 5, drop-out 1-2 Gyr); 0.6 Msun ~ geometric mean of 0.5 and 0.75 rows (saturated plateau ~1.5e29 per Fig. 5, drop-out 40 / 350 / 700 Myr).

### 3.7 HZ flux and integrated XUV (Figs. 9, 12, 18; text p. 19-20)
- HZ X-ray flux at 5 Gyr is ~2 orders of magnitude higher for HZ planets of low-mass M dwarfs than for G dwarfs (HZ defined half-way between moist and maximum greenhouse limits at 5 Gyr stellar properties).
- Solar-mass HZ F_X drops below 100 erg s^-1 cm^-2 at ~10 Myr (slow) vs ~700 Myr (fast); modern Earth receives 0.15-1.15 erg s^-1 cm^-2 of X-rays (p. 19).
- Integrated XUV (<100 nm) energy 1-1000 Myr (Fig. 18, **[FIG]**): 1.0 Msun ~5e45 (slow) to ~5e46 erg (fast); 0.5 Msun ~5e45-1e46; 0.3 Msun ~2e45-3e45; 1000-5000 Myr: 1.0 Msun ~1.5e46-3e46, 0.5 Msun ~4e45, 0.3 Msun ~1.5e45. Text: a 0.2 Msun star emits 2 dex less than a rapidly rotating solar-mass star and 1 dex less than a slowly rotating one over the first Gyr.

---

## 4. Quick comparison / consistency notes for the design spec
- Saturation level: Jackson (G bin) 10^-3.67; Tu/Wright 10^-3.13; Johnstone 5.135e-4 = 10^-3.29 at Ro_sat (rising to ~10^-3.1 at Ro ~ 0.005 because beta1 = -0.135). Jackson is a cluster-mean (includes slowly-rotating unsaturated members), the other two are rotation-selected.
- Solar-mass drop-out age: Jackson 39 Myr (cluster mean, colour bin 0.565-0.675); Tu 5.7 / 23 / 226 Myr; Johnstone ~5 / ~22 / ~280 Myr (5th/50th/95th).
- Post-saturation decay for the Sun: Jackson alpha = 0.91 (bin) or 1.19 (mean); Tu -1.12 / -1.42 / -2.50 (steeper for fast rotators because they start later from the same L_sat and must reach the same L_X,sun).
- Solar anchor: Tu L_X,sun = 10^27.2 erg s^-1 at 4570 Myr; Johnstone Fig. 11 gives ~1.1e28 at 5 Gyr for 1 Msun (their relation makes the Sun appear less X-ray active than average; sigma = 0.36 dex).
- EUV: Tu (Sanz-Forcada 2011, luminosities) log L_EUV = 4.8 + 0.86 log L_X; Johnstone (surface fluxes) log F_EUV,1 = 2.04 + 0.681 log F_X plus Eq. 21 for 36-92 nm. Jackson: none.
