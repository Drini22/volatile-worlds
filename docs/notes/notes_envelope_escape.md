# Envelope structure + escape ingredients (extracted from four PDFs)

Source PDFs: `/Users/drinorcacaj/Documents/Phd_Bern/papers/evolution/` — Lopez & Fortney 2014 (arXiv:1311.0329v1, LF14), Owen & Wu 2017 (arXiv:1705.10810v2, OW17), Owen & Wu 2016 (arXiv:1506.02049v1, OW16), Ginzburg, Schlichting & Sari 2018 (arXiv:1708.01621v2, GSS18). Page numbers below are the PDF/preprint page numbers. Coefficients copied verbatim; `⊕` = Earth, `☉` = Sun.

---

## 1. Lopez & Fortney 2014 — radius of a sub-Neptune (Rp = Rcore + Renv + Ratm)

### Model assumptions (p. 2)
- Isothermal rock/iron core, Earth-like 2:1 rock/iron (ANEOS olivine + SESAME 2140 Fe). Fully adiabatic H/He envelope (Saumon et al. 1995 EOS). Radiative atmosphere on top, isothermal at Teq.
- Planet radius defined at **20 mbar** (transit slant geometry). Radiative-convective boundary at ~100–1000 bar for sub-Neptunes at several Gyr.
- Hot start: models begin at **1 Myr** with entropy 10 k_b baryon⁻¹; results insensitive to initial entropy after ~10–100 Myr (initial radii can be ≳10 R⊕ at 1 Myr). Results presented for ages >10 Myr.
- Includes radioactive heating and core heat capacity. Ignoring them makes the planet 30–100× less luminous at late times and underestimates the final radius by ~0.5 R⊕ (p. 5, Fig. 3). Core cooling dominates luminosity at all ages; ⁴⁰K radiogenic heating comparable at ≳1 Gyr.
- Two atmosphere grids: solar metallicity and 50× solar ("enhanced opacity").

### Eq. (1), p. 3 — core radius (Earth-like composition, error ~2%; ~10% if iron fraction varied)
```
R_core = (M_core/M⊕)^0.25  R⊕  ≈  (M_p/M⊕)^0.25  R⊕
```
(M_core ≈ M_p for sub-Neptunes since 90–99% of mass is in the core.)

### Eq. (2), p. 4 — radiative-atmosphere thickness (RCB ~100 bar → transit radius ~20 mbar, ≈8–10 scale heights)
```
R_atm ≈ log(100 bar / 20 mbar) · H ≈ 9 · k_b T_eq / (g μ_H/He)
```
H = k_b T_eq/(g μ_H/He) is the isothermal scale height at T_eq, g = planet surface gravity, μ_H/He = mean molecular weight of H/He. "Typically ~0.1 R⊕ except at the very highest levels of irradiation."

### Eq. (3), p. 4 — envelope radius power-law fit (ENHANCED-OPACITY models; fit to ages >100 Myr; matches full models to ~0.1 dex)
```
R_env = R_p − R_core − R_atm
      = 2.06 R⊕ · (M_p/M⊕)^(−0.21) · (f_env/5%)^(0.59) · (F_p/F⊕)^(0.044) · (age/5 Gyr)^(−0.18)
```
- Age exponent: enhanced opacity R_env ∝ t^(−0.18); **solar metallicity R_env ∝ t^(−0.11)** (text on p. 4 writes "Renv ∼ t^0.11 / t^0.18" — magnitude of exponent; radius decreases with age). Solar-metallicity models cool faster early (already cold by ~100 Myr) so later contraction is slower; by several Gyr the two grids converge.
- Quoted sensitivities (p. 4): doubling f_env has ~10× larger effect on R_p than doubling F_p and >2× that of doubling age.
- Flat mass–radius curves for f_env ≳ 1% or R_p ≳ 2.5 R⊕ because the R_env mass decrease (M^−0.21) is balanced by R_core ∝ M^0.25.
- Caveat (p. 4): fits are "only meant to be a rough approximation of the full models… not to be used in place of the full models."

### Validity ranges of the parameter study (p. 2–3, abstract)
- Mass 1–20 M⊕; incident flux 0.1–1000 F⊕; H/He fraction 0.01–20% in tables (grid ran to 60%); ages 10 Myr–10 Gyr (tables at 100 Myr, 1 Gyr, 10 Gyr); >1300 models.
- Panel b) Fig. 1: varying flux over 4 orders of magnitude changes radius by <~30%.
- Panel c) Fig. 1: at early times low-mass planets are larger than high-mass ones; curves flatten by ~1 Gyr.

### Super-Earth / sub-Neptune boundary (p. 8–9)
- 2.0 R⊕ = hard upper limit for a bare rocky planet (needs 16.5 M⊕ Earth-like, or 11 M⊕ iron-free). A 5 M⊕ Earth-like core needs only 0.5% H/He to reach 2.0 R⊕ (≈20 kbar at envelope base, >3000 K).
- ≲1.5 R⊕ can be explained without H/He; if present, H/He ≲0.1%.
- Suggested dividing line: **1.75 R⊕**.

### Tabulated radii (R⊕) — Tables 2–7, pp. 12–17
Columns = f_env (H/He mass fraction). Rows: (flux F⊕, mass M⊕).

**Table 2: 100 Myr, solar metallicity**
| F⊕ | M⊕ | 0.01% | 0.02% | 0.05% | 0.1% | 0.2% | 0.5% | 1% | 2% | 5% | 10% | 20% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 1 | 1.22 | 1.16 | 1.18 | 1.21 | 1.32 | 1.65 | 2.17 | 2.75 | 4.32 | 6.81 | 11.7 |
| 0.1 | 1.5 | 1.30 | 1.24 | 1.26 | 1.30 | 1.40 | 1.71 | 2.15 | 2.65 | 3.97 | 6.18 | 10.6 |
| 0.1 | 2.4 | 1.41 | 1.36 | 1.40 | 1.42 | 1.53 | 1.79 | 2.17 | 2.58 | 3.66 | 5.36 | 9.05 |
| 0.1 | 3.6 | 1.53 | 1.49 | 1.51 | 1.54 | 1.64 | 1.89 | 2.21 | 2.56 | 3.49 | 4.93 | 7.86 |
| 0.1 | 5.5 | 1.66 | 1.63 | 1.66 | 1.69 | 1.79 | 2.01 | 2.28 | 2.60 | 3.37 | 4.58 | 6.96 |
| 0.1 | 8.5 | 1.81 | 1.79 | 1.82 | 1.85 | 1.95 | 2.14 | 2.39 | 2.67 | 3.36 | 4.35 | 6.32 |
| 0.1 | 13 | 1.97 | 1.97 | 1.98 | 2.02 | 2.11 | 2.30 | 2.52 | 2.78 | 3.41 | 4.29 | 5.94 |
| 0.1 | 20 | 2.15 | 2.15 | 2.17 | 2.20 | 2.29 | 2.47 | 2.67 | 2.93 | 3.52 | 4.32 | 5.75 |
| 10 | 1 | 1.32 | 1.24 | 1.27 | 1.31 | 1.44 | 1.82 | 2.40 | 3.06 | 4.72 | 7.13 | 11.1 |
| 10 | 1.5 | 1.36 | 1.32 | 1.35 | 1.38 | 1.50 | 1.84 | 2.32 | 2.88 | 4.31 | 6.47 | 10.4 |
| 10 | 2.4 | 1.46 | 1.43 | 1.48 | 1.50 | 1.59 | 1.88 | 2.26 | 2.71 | 3.88 | 5.67 | 9.14 |
| 10 | 3.6 | 1.57 | 1.55 | 1.58 | 1.60 | 1.71 | 1.95 | 2.27 | 2.64 | 3.61 | 5.13 | 8.11 |
| 10 | 5.5 | 1.69 | 1.68 | 1.71 | 1.73 | 1.84 | 2.05 | 2.33 | 2.66 | 3.46 | 4.70 | 7.13 |
| 10 | 8.5 | 1.84 | 1.83 | 1.86 | 1.89 | 1.98 | 2.18 | 2.43 | 2.72 | 3.42 | 4.43 | 6.39 |
| 10 | 13 | 1.99 | 2.01 | 2.02 | 2.05 | 2.14 | 2.32 | 2.55 | 2.82 | 3.46 | 4.35 | 5.96 |
| 10 | 20 | 2.17 | 2.18 | 2.19 | 2.23 | 2.31 | 2.49 | 2.69 | 2.95 | 3.56 | 4.37 | 5.77 |
| 1000 | 1 | 1.59 | 1.63 | 1.70 | 1.75 | 1.83 | 2.30 | 3.12 | 3.99 | 6.21 | 8.88 | 11.3 |
| 1000 | 1.5 | 1.63 | 1.67 | 1.72 | 1.77 | 1.89 | 2.31 | 3.02 | 3.83 | 6.01 | 9.41 | 14.0 |
| 1000 | 2.4 | 1.70 | 1.72 | 1.77 | 1.81 | 1.93 | 2.32 | 2.90 | 3.55 | 5.35 | 8.59 | 15.4 |
| 1000 | 3.6 | 1.77 | 1.79 | 1.83 | 1.87 | 1.99 | 2.34 | 2.81 | 3.36 | 4.82 | 7.27 | 13.4 |
| 1000 | 5.5 | 1.87 | 1.88 | 1.92 | 1.96 | 2.08 | 2.37 | 2.76 | 3.22 | 4.39 | 6.25 | 10.3 |
| 1000 | 8.5 | 1.99 | 2.00 | 2.03 | 2.08 | 2.19 | 2.50 | 2.76 | 3.15 | 4.12 | 5.56 | 8.48 |
| 1000 | 13 | 2.12 | 2.12 | 2.15 | 2.21 | 2.31 | 2.58 | 2.81 | 3.16 | 3.99 | 5.18 | 7.43 |
| 1000 | 20 | 2.27 | 2.27 | 2.30 | 2.35 | 2.45 | 2.68 | 2.90 | 3.21 | 3.94 | 4.97 | 6.80 |

**Table 3: 1 Gyr, solar metallicity**
| F⊕ | M⊕ | 0.01% | 0.02% | 0.05% | 0.1% | 0.2% | 0.5% | 1% | 2% | 5% | 10% | 20% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 1 | 1.07 | 1.09 | 1.12 | 1.15 | 1.28 | 1.55 | 1.79 | 2.13 | 2.98 | 4.26 | 6.74 |
| 0.1 | 1.5 | 1.18 | 1.19 | 1.22 | 1.26 | 1.38 | 1.62 | 1.82 | 2.13 | 2.87 | 3.96 | 6.10 |
| 0.1 | 2.4 | 1.32 | 1.33 | 1.36 | 1.39 | 1.52 | 1.72 | 1.90 | 2.16 | 2.81 | 3.75 | 5.52 |
| 0.1 | 3.6 | 1.45 | 1.46 | 1.49 | 1.52 | 1.65 | 1.82 | 1.99 | 2.23 | 2.81 | 3.65 | 5.21 |
| 0.1 | 5.5 | 1.60 | 1.61 | 1.64 | 1.67 | 1.79 | 1.95 | 2.11 | 2.34 | 2.87 | 3.62 | 5.00 |
| 0.1 | 8.5 | 1.77 | 1.78 | 1.80 | 1.83 | 1.94 | 2.10 | 2.25 | 2.47 | 2.97 | 3.67 | 4.91 |
| 0.1 | 13 | 1.94 | 1.95 | 1.97 | 2.00 | 2.11 | 2.25 | 2.40 | 2.61 | 3.11 | 3.77 | 4.92 |
| 0.1 | 20 | 2.12 | 2.13 | 2.16 | 2.19 | 2.30 | 2.42 | 2.57 | 2.78 | 3.28 | 3.92 | 5.00 |
| 10 | 1 | 1.18 | 1.20 | 1.23 | 1.27 | 1.47 | 1.81 | 2.12 | 2.58 | 3.63 | 5.07 | 7.45 |
| 10 | 1.5 | 1.27 | 1.29 | 1.32 | 1.36 | 1.52 | 1.82 | 2.08 | 2.47 | 3.40 | 4.68 | 6.96 |
| 10 | 2.4 | 1.40 | 1.41 | 1.44 | 1.48 | 1.63 | 1.86 | 2.08 | 2.41 | 3.18 | 4.26 | 6.24 |
| 10 | 3.6 | 1.51 | 1.53 | 1.55 | 1.59 | 1.72 | 1.93 | 2.12 | 2.40 | 3.07 | 4.02 | 5.73 |
| 10 | 5.5 | 1.65 | 1.66 | 1.69 | 1.72 | 1.85 | 2.02 | 2.19 | 2.45 | 3.04 | 3.86 | 5.34 |
| 10 | 8.5 | 1.81 | 1.82 | 1.84 | 1.88 | 1.99 | 2.15 | 2.31 | 2.54 | 3.08 | 3.81 | 5.09 |
| 10 | 13 | 1.97 | 1.98 | 2.01 | 2.04 | 2.15 | 2.29 | 2.44 | 2.67 | 3.18 | 3.86 | 5.02 |
| 10 | 20 | 2.15 | 2.16 | 2.18 | 2.22 | 2.32 | 2.45 | 2.60 | 2.82 | 3.33 | 3.99 | 5.07 |
| 1000 | 1 | 1.61 | 1.65 | 1.71 | 1.77 | 1.81 | 2.15 | 2.50 | 3.01 | 4.24 | 6.04 | 8.75 |
| 1000 | 1.5 | 1.65 | 1.68 | 1.73 | 1.78 | 1.87 | 2.18 | 2.50 | 2.98 | 4.14 | 5.91 | 9.34 |
| 1000 | 2.4 | 1.71 | 1.73 | 1.78 | 1.82 | 1.93 | 2.21 | 2.50 | 2.91 | 3.93 | 5.50 | 8.76 |
| 1000 | 3.6 | 1.78 | 1.80 | 1.84 | 1.87 | 1.99 | 2.24 | 2.50 | 2.87 | 3.77 | 5.11 | 7.86 |
| 1000 | 5.5 | 1.87 | 1.89 | 1.92 | 1.94 | 2.10 | 2.30 | 2.52 | 2.85 | 3.65 | 4.79 | 7.00 |
| 1000 | 8.5 | 1.99 | 2.00 | 2.02 | 2.05 | 2.19 | 2.38 | 2.58 | 2.88 | 3.59 | 4.58 | 6.39 |
| 1000 | 13 | 2.12 | 2.13 | 2.15 | 2.19 | 2.31 | 2.48 | 2.66 | 2.94 | 3.59 | 4.48 | 6.05 |
| 1000 | 20 | 2.27 | 2.27 | 2.29 | 2.34 | 2.45 | 2.61 | 2.78 | 3.04 | 3.65 | 4.47 | 5.85 |

**Table 4: 10 Gyr, solar metallicity**
| F⊕ | M⊕ | 0.01% | 0.02% | 0.05% | 0.1% | 0.2% | 0.5% | 1% | 2% | 5% | 10% | 20% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 1 | 1.08 | 1.10 | 1.13 | 1.17 | 1.22 | 1.37 | 1.53 | 1.75 | 2.25 | 2.94 | 4.14 |
| 0.1 | 1.5 | 1.19 | 1.20 | 1.23 | 1.27 | 1.31 | 1.45 | 1.60 | 1.81 | 2.28 | 2.93 | 4.05 |
| 0.1 | 2.4 | 1.32 | 1.34 | 1.37 | 1.40 | 1.45 | 1.58 | 1.71 | 1.90 | 2.35 | 2.95 | 3.98 |
| 0.1 | 3.6 | 1.45 | 1.47 | 1.49 | 1.53 | 1.58 | 1.70 | 1.82 | 2.01 | 2.44 | 3.01 | 3.97 |
| 0.1 | 5.5 | 1.60 | 1.62 | 1.64 | 1.67 | 1.75 | 1.84 | 1.96 | 2.15 | 2.56 | 3.11 | 4.03 |
| 0.1 | 8.5 | 1.77 | 1.78 | 1.80 | 1.84 | 1.91 | 2.00 | 2.13 | 2.31 | 2.72 | 3.25 | 4.14 |
| 0.1 | 13 | 1.94 | 1.95 | 1.97 | 2.00 | 2.09 | 2.17 | 2.30 | 2.48 | 2.90 | 3.44 | 4.31 |
| 0.1 | 20 | 2.12 | 2.14 | 2.16 | 2.19 | 2.25 | 2.36 | 2.49 | 2.68 | 3.10 | 3.65 | 4.53 |
| 10 | 1 | 1.23 | 1.25 | 1.28 | 1.31 | 1.44 | 1.68 | 1.87 | 2.17 | 2.84 | 3.70 | 5.11 |
| 10 | 1.5 | 1.31 | 1.33 | 1.36 | 1.40 | 1.49 | 1.72 | 1.90 | 2.19 | 2.83 | 3.66 | 5.03 |
| 10 | 2.4 | 1.43 | 1.44 | 1.47 | 1.51 | 1.60 | 1.78 | 1.96 | 2.21 | 2.80 | 3.58 | 4.89 |
| 10 | 3.6 | 1.54 | 1.55 | 1.58 | 1.62 | 1.73 | 1.87 | 2.03 | 2.27 | 2.81 | 3.53 | 4.75 |
| 10 | 5.5 | 1.67 | 1.69 | 1.71 | 1.75 | 1.85 | 1.98 | 2.13 | 2.35 | 2.86 | 3.52 | 4.64 |
| 10 | 8.5 | 1.82 | 1.84 | 1.86 | 1.90 | 1.98 | 2.11 | 2.25 | 2.47 | 2.95 | 3.58 | 4.61 |
| 10 | 13 | 1.98 | 1.99 | 2.02 | 2.05 | 2.13 | 2.26 | 2.40 | 2.61 | 3.07 | 3.68 | 4.66 |
| 10 | 20 | 2.16 | 2.17 | 2.20 | 2.23 | 2.32 | 2.43 | 2.56 | 2.77 | 3.23 | 3.83 | 4.77 |
| 1000 | 1 | 1.76 | 1.81 | 1.88 | 1.96 | 2.01 | 2.08 | 2.18 | 2.31 | 2.70 | 3.49 | 4.88 |
| 1000 | 1.5 | 1.77 | 1.81 | 1.88 | 1.94 | 1.99 | 2.08 | 2.17 | 2.33 | 2.91 | 3.76 | 5.36 |
| 1000 | 2.4 | 1.82 | 1.85 | 1.90 | 1.95 | 2.00 | 2.08 | 2.22 | 2.49 | 3.10 | 3.94 | 5.55 |
| 1000 | 3.6 | 1.87 | 1.90 | 1.94 | 1.98 | 2.03 | 2.12 | 2.30 | 2.58 | 3.20 | 4.03 | 5.54 |
| 1000 | 5.5 | 1.95 | 1.97 | 2.01 | 2.04 | 2.10 | 2.21 | 2.38 | 2.64 | 3.26 | 4.08 | 5.49 |
| 1000 | 8.5 | 2.05 | 2.07 | 2.10 | 2.12 | 2.19 | 2.31 | 2.48 | 2.73 | 3.31 | 4.10 | 5.44 |
| 1000 | 13 | 2.17 | 2.18 | 2.21 | 2.23 | 2.34 | 2.43 | 2.59 | 2.83 | 3.38 | 4.13 | 5.40 |
| 1000 | 20 | 2.31 | 2.32 | 2.34 | 2.36 | 2.47 | 2.57 | 2.72 | 2.95 | 3.49 | 4.20 | 5.38 |

**Table 5: 100 Myr, enhanced opacity**
| F⊕ | M⊕ | 0.01% | 0.02% | 0.05% | 0.1% | 0.2% | 0.5% | 1% | 2% | 5% | 10% | 20% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 1 | 1.25 | 1.17 | 1.19 | 1.24 | 1.43 | 1.89 | 2.57 | 3.00 | 4.32 | 6.81 | 11.7 |
| 0.1 | 1.5 | 1.31 | 1.25 | 1.28 | 1.31 | 1.47 | 1.93 | 2.58 | 3.17 | 3.97 | 6.18 | 10.6 |
| 0.1 | 2.4 | 1.42 | 1.37 | 1.41 | 1.44 | 1.60 | 2.14 | 2.51 | 3.11 | 4.30 | 5.36 | 9.05 |
| 0.1 | 3.6 | 1.53 | 1.49 | 1.52 | 1.57 | 1.71 | 2.18 | 2.51 | 3.02 | 4.31 | 5.57 | 7.86 |
| 0.1 | 5.5 | 1.66 | 1.63 | 1.67 | 1.72 | 1.84 | 2.23 | 2.53 | 2.97 | 4.09 | 5.69 | 7.25 |
| 0.1 | 8.5 | 1.82 | 1.79 | 1.82 | 1.87 | 2.00 | 2.33 | 2.57 | 2.95 | 3.90 | 5.29 | 7.73 |
| 0.1 | 13 | 1.97 | 1.96 | 1.99 | 2.04 | 2.16 | 2.45 | 2.67 | 3.00 | 3.81 | 4.99 | 7.25 |
| 0.1 | 20 | 2.15 | 2.14 | 2.17 | 2.23 | 2.33 | 2.58 | 2.79 | 3.10 | 3.82 | 4.82 | 6.68 |
| 10 | 1 | 1.34 | 1.25 | 1.29 | 1.35 | 1.53 | 2.05 | 2.79 | 3.12 | 4.72 | 7.13 | 11.1 |
| 10 | 1.5 | 1.38 | 1.33 | 1.37 | 1.41 | 1.58 | 2.07 | 2.80 | 3.41 | 4.31 | 6.47 | 10.4 |
| 10 | 2.4 | 1.47 | 1.44 | 1.48 | 1.51 | 1.68 | 2.25 | 2.67 | 3.32 | 4.50 | 5.67 | 9.14 |
| 10 | 3.6 | 1.58 | 1.54 | 1.58 | 1.64 | 1.77 | 2.26 | 2.62 | 3.17 | 4.55 | 5.71 | 8.11 |
| 10 | 5.5 | 1.70 | 1.67 | 1.71 | 1.77 | 1.89 | 2.30 | 2.60 | 3.07 | 4.27 | 5.94 | 7.30 |
| 10 | 8.5 | 1.85 | 1.83 | 1.86 | 1.92 | 2.04 | 2.37 | 2.63 | 3.01 | 4.01 | 5.50 | 7.98 |
| 10 | 13 | 1.99 | 1.99 | 2.02 | 2.08 | 2.19 | 2.48 | 2.70 | 3.04 | 3.88 | 5.12 | 7.50 |
| 10 | 20 | 2.17 | 2.17 | 2.19 | 2.25 | 2.35 | 2.61 | 2.82 | 3.13 | 3.87 | 4.90 | 6.81 |
| 1000 | 1 | 1.59 | 1.63 | 1.70 | 1.75 | 1.88 | 2.42 | 3.13 | 3.99 | 6.21 | 8.88 | 11.3 |
| 1000 | 1.5 | 1.63 | 1.67 | 1.72 | 1.77 | 1.90 | 2.46 | 3.25 | 3.84 | 6.01 | 9.41 | 14.0 |
| 1000 | 2.4 | 1.70 | 1.72 | 1.77 | 1.81 | 1.97 | 2.63 | 3.13 | 3.89 | 5.35 | 8.59 | 15.4 |
| 1000 | 3.6 | 1.77 | 1.79 | 1.83 | 1.87 | 2.02 | 2.57 | 3.01 | 3.67 | 5.23 | 7.27 | 13.4 |
| 1000 | 5.5 | 1.87 | 1.88 | 1.92 | 1.96 | 2.10 | 2.54 | 2.90 | 3.46 | 4.89 | 6.68 | 10.3 |
| 1000 | 8.5 | 1.99 | 2.00 | 2.03 | 2.08 | 2.21 | 2.56 | 2.86 | 3.31 | 4.48 | 6.23 | 8.82 |
| 1000 | 13 | 2.12 | 2.12 | 2.15 | 2.21 | 2.32 | 2.63 | 2.89 | 3.27 | 4.22 | 5.64 | 8.36 |
| 1000 | 20 | 2.27 | 2.27 | 2.30 | 2.36 | 2.47 | 2.73 | 2.95 | 3.30 | 4.12 | 5.28 | 7.38 |

**Table 6: 1 Gyr, enhanced opacity**
| F⊕ | M⊕ | 0.01% | 0.02% | 0.05% | 0.1% | 0.2% | 0.5% | 1% | 2% | 5% | 10% | 20% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 1 | 1.07 | 1.09 | 1.12 | 1.15 | 1.37 | 1.68 | 1.98 | 2.43 | 3.11 | 4.26 | 6.74 |
| 0.1 | 1.5 | 1.18 | 1.19 | 1.22 | 1.26 | 1.45 | 1.74 | 1.99 | 2.38 | 3.27 | 3.96 | 6.10 |
| 0.1 | 2.4 | 1.32 | 1.33 | 1.36 | 1.39 | 1.60 | 1.82 | 2.05 | 2.38 | 3.22 | 4.23 | 5.52 |
| 0.1 | 3.6 | 1.45 | 1.46 | 1.49 | 1.52 | 1.71 | 1.90 | 2.10 | 2.42 | 3.15 | 4.25 | 5.62 |
| 0.1 | 5.5 | 1.60 | 1.61 | 1.64 | 1.67 | 1.85 | 2.02 | 2.19 | 2.47 | 3.16 | 4.13 | 5.84 |
| 0.1 | 8.5 | 1.77 | 1.78 | 1.80 | 1.84 | 1.99 | 2.15 | 2.32 | 2.57 | 3.19 | 4.09 | 5.74 |
| 0.1 | 13 | 1.94 | 1.95 | 1.97 | 2.01 | 2.15 | 2.30 | 2.46 | 2.70 | 3.28 | 4.11 | 5.58 |
| 0.1 | 20 | 2.12 | 2.13 | 2.16 | 2.21 | 2.32 | 2.46 | 2.62 | 2.86 | 3.42 | 4.17 | 5.56 |
| 10 | 1 | 1.18 | 1.20 | 1.23 | 1.27 | 1.50 | 1.84 | 2.20 | 2.72 | 3.63 | 5.07 | 7.45 |
| 10 | 1.5 | 1.27 | 1.29 | 1.32 | 1.36 | 1.56 | 1.87 | 2.16 | 2.60 | 3.58 | 4.68 | 6.96 |
| 10 | 2.4 | 1.40 | 1.41 | 1.44 | 1.48 | 1.68 | 1.92 | 2.17 | 2.54 | 3.47 | 4.52 | 6.24 |
| 10 | 3.6 | 1.51 | 1.53 | 1.55 | 1.59 | 1.77 | 1.98 | 2.20 | 2.54 | 3.34 | 4.53 | 5.85 |
| 10 | 5.5 | 1.65 | 1.66 | 1.69 | 1.72 | 1.90 | 2.07 | 2.27 | 2.56 | 3.31 | 4.36 | 6.14 |
| 10 | 8.5 | 1.81 | 1.82 | 1.84 | 1.89 | 2.03 | 2.20 | 2.37 | 2.64 | 3.31 | 4.27 | 5.99 |
| 10 | 13 | 1.97 | 1.98 | 2.01 | 2.05 | 2.18 | 2.34 | 2.50 | 2.76 | 3.37 | 4.24 | 5.76 |
| 10 | 20 | 2.15 | 2.16 | 2.18 | 2.24 | 2.36 | 2.49 | 2.65 | 2.90 | 3.49 | 4.27 | 5.68 |
| 1000 | 1 | 1.61 | 1.65 | 1.71 | 1.77 | 1.85 | 2.20 | 2.60 | 3.09 | 4.24 | 6.04 | 8.75 |
| 1000 | 1.5 | 1.65 | 1.68 | 1.73 | 1.78 | 1.88 | 2.24 | 2.59 | 3.10 | 4.14 | 5.91 | 9.34 |
| 1000 | 2.4 | 1.71 | 1.73 | 1.78 | 1.82 | 1.96 | 2.26 | 2.57 | 3.02 | 4.13 | 5.50 | 8.76 |
| 1000 | 3.6 | 1.78 | 1.80 | 1.84 | 1.87 | 2.02 | 2.27 | 2.54 | 2.96 | 3.94 | 5.34 | 7.86 |
| 1000 | 5.5 | 1.87 | 1.89 | 1.92 | 1.94 | 2.11 | 2.32 | 2.54 | 2.90 | 3.80 | 5.05 | 7.13 |
| 1000 | 8.5 | 1.99 | 2.00 | 2.02 | 2.05 | 2.21 | 2.39 | 2.59 | 2.90 | 3.68 | 4.81 | 6.84 |
| 1000 | 13 | 2.12 | 2.13 | 2.15 | 2.19 | 2.32 | 2.49 | 2.67 | 2.96 | 3.65 | 4.65 | 6.41 |
| 1000 | 20 | 2.27 | 2.27 | 2.29 | 2.34 | 2.46 | 2.61 | 2.78 | 3.06 | 3.70 | 4.57 | 6.14 |

**Table 7: 10 Gyr, enhanced opacity**
| F⊕ | M⊕ | 0.01% | 0.02% | 0.05% | 0.1% | 0.2% | 0.5% | 1% | 2% | 5% | 10% | 20% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 1 | 1.08 | 1.10 | 1.13 | 1.17 | 1.24 | 1.37 | 1.53 | 1.75 | 2.32 | 2.97 | 4.14 |
| 0.1 | 1.5 | 1.19 | 1.20 | 1.23 | 1.27 | 1.34 | 1.46 | 1.61 | 1.82 | 2.33 | 3.04 | 4.05 |
| 0.1 | 2.4 | 1.32 | 1.34 | 1.37 | 1.40 | 1.47 | 1.57 | 1.71 | 1.92 | 2.40 | 3.07 | 4.13 |
| 0.1 | 3.6 | 1.45 | 1.47 | 1.49 | 1.53 | 1.59 | 1.70 | 1.83 | 2.01 | 2.49 | 3.12 | 4.23 |
| 0.1 | 5.5 | 1.60 | 1.62 | 1.64 | 1.67 | 1.76 | 1.85 | 1.97 | 2.16 | 2.59 | 3.22 | 4.27 |
| 0.1 | 8.5 | 1.77 | 1.78 | 1.80 | 1.84 | 1.88 | 2.02 | 2.14 | 2.32 | 2.75 | 3.34 | 4.37 |
| 0.1 | 13 | 1.94 | 1.95 | 1.97 | 2.00 | 2.10 | 2.18 | 2.30 | 2.50 | 2.93 | 3.50 | 4.51 |
| 0.1 | 20 | 2.12 | 2.14 | 2.16 | 2.19 | 2.27 | 2.37 | 2.49 | 2.69 | 3.13 | 3.71 | 4.66 |
| 10 | 1 | 1.23 | 1.25 | 1.28 | 1.31 | 1.39 | 1.55 | 1.75 | 2.02 | 2.72 | 3.70 | 5.11 |
| 10 | 1.5 | 1.31 | 1.33 | 1.36 | 1.40 | 1.48 | 1.62 | 1.79 | 2.05 | 2.66 | 3.57 | 5.03 |
| 10 | 2.4 | 1.43 | 1.44 | 1.47 | 1.51 | 1.58 | 1.70 | 1.85 | 2.10 | 2.65 | 3.44 | 4.89 |
| 10 | 3.6 | 1.54 | 1.55 | 1.58 | 1.62 | 1.69 | 1.80 | 1.94 | 2.15 | 2.69 | 3.41 | 4.67 |
| 10 | 5.5 | 1.67 | 1.69 | 1.71 | 1.75 | 1.84 | 1.93 | 2.07 | 2.27 | 2.75 | 3.44 | 4.61 |
| 10 | 8.5 | 1.82 | 1.84 | 1.86 | 1.90 | 1.98 | 2.08 | 2.21 | 2.41 | 2.86 | 3.51 | 4.62 |
| 10 | 13 | 1.98 | 1.99 | 2.02 | 2.05 | 2.14 | 2.23 | 2.36 | 2.56 | 3.02 | 3.63 | 4.70 |
| 10 | 20 | 2.16 | 2.17 | 2.20 | 2.23 | 2.31 | 2.41 | 2.54 | 2.74 | 3.21 | 3.81 | 4.81 |
| 1000 | 1 | 1.76 | 1.81 | 1.88 | 1.96 | 2.01 | 2.08 | 2.16 | 2.29 | 2.60 | 3.49 | 4.88 |
| 1000 | 1.5 | 1.77 | 1.81 | 1.88 | 1.94 | 1.99 | 2.05 | 2.15 | 2.28 | 2.83 | 3.72 | 5.36 |
| 1000 | 2.4 | 1.82 | 1.85 | 1.90 | 1.95 | 1.99 | 2.05 | 2.14 | 2.36 | 3.01 | 3.89 | 5.55 |
| 1000 | 3.6 | 1.87 | 1.90 | 1.94 | 1.98 | 2.02 | 2.09 | 2.18 | 2.42 | 3.10 | 3.97 | 5.48 |
| 1000 | 5.5 | 1.95 | 1.97 | 2.01 | 2.04 | 2.09 | 2.15 | 2.31 | 2.54 | 3.14 | 4.01 | 5.47 |
| 1000 | 8.5 | 2.05 | 2.07 | 2.10 | 2.12 | 2.15 | 2.28 | 2.43 | 2.67 | 3.21 | 4.01 | 5.40 |
| 1000 | 13 | 2.17 | 2.18 | 2.21 | 2.23 | 2.28 | 2.40 | 2.55 | 2.79 | 3.33 | 4.05 | 5.35 |
| 1000 | 20 | 2.31 | 2.32 | 2.34 | 2.36 | 2.45 | 2.55 | 2.69 | 2.92 | 3.45 | 4.15 | 5.32 |

Note: the 100 Myr tables are already sensitive to the opacity choice (enhanced-opacity radii larger at 0.5–5%); the 10 Gyr tables of the two grids nearly coincide.

---

## 2. Owen & Wu 2017 — photoevaporation valley (minimal analytic model)

Notation: core mass M_c, core radius R_c, envelope fraction **X ≡ M_env/M_c**, ΔR = R_p − R_c, R_rcb radiative–convective boundary, τ_KH cooling time. Ideal-gas envelope, γ = 5/3, μ = 2.35, no self-gravity (valid X < 1). Photosphere ≈ 6 scale heights above R_rcb (p. 2).

### Eq. (1), p. 2 — isothermal-layer scale height
```
H/R_c = k_B T_eq / (μ m_H g R_c) ≈ 0.017 (a/0.1 AU)^(−1/2) (M_c/5 M⊕)^(−3/4) (R_p/1.5 R⊕)^2
```
(Sun-like host: 1 M☉, 1 R☉, 5780 K; μ = 2.35; Earth-like core.)

### Eq. (15), p. 4 — core mass–radius relation (Fortney+07, Valencia+10, LF14)
```
M_c ∝ R_c^4   ⇔   ρ_c = ρ_M⊕ (M_c/1 M⊕)^(1/4)
ρ_M⊕ = 5.5 g cm⁻³ (terrestrial); 11 (pure iron); 4 (silicate); 1.4 (water/ice)  [1.3 used in Fig. 7]
```
Bare 1.3 R⊕ ↔ M_c = 3 M⊕ (Earth-like); 1.18 R⊕ ↔ 2 M⊕.

### Eqs. (2)–(13), pp. 3–4 — envelope structure
- ρ ≃ ρ_rcb [∇_ab (G M_c/(c_s² R_p)) (R_p/r − 1)]^(1/(γ−1)), ∇_ab = (γ−1)/γ (eq. 3).
- M_env ≃ 4π R_p³ ρ_rcb (∇_ab G M_c/(c_s² R_p))^(1/(γ−1)) I_2(R_c/R_p, γ) (eq. 4); I_2 ≈ ∇_ab (ΔR/R_c)^(γ/(γ−1)) for thin envelopes (eq. 6).
- L ≈ (1/τ_KH) (G M_c M_env/R_p) I_1/I_2 (eq. 11); I_1/I_2 varies 1→~3.
- ρ_rcb ≈ (μ/k_b) [ (I_2/I_1) 64πσ T_eq^(3−α−β) R_p τ_KH / (3 κ_0 M_c X) ]^(1/(1+α)) (eq. 13), opacity κ = κ_0 P^α T^β with **α = 0.68, β = 0.45** (Rogers & Seager 2010), κ = 1.29×10⁻² cm² g⁻¹ at 1 bar, 1000 K.
- Eq. (14): X ∝ (I_2/I_1)^n_I μ^n_μ κ_0^n_κ T_eq^n_T τ_KH^n_τ ρ_M⊕^n_ρ M_c^n_M × (ΔR/R_c)^n_a [ΔR/R_c<1] or (ΔR/R_c)^n_b [ΔR/R_c>1].
- Eq. (16) exponents (γ=5/3, α=0.68, β=0.45): n_I = n_τ = 1/(α+2) ≈ 0.37; n_μ = (1+1/(γ−1))(α+1)/(α+2) ≈ 1.57; n_κ = −1/(α+2) ≈ −0.37; n_T = ((3−α−β)/(α+1) − 1/(γ−1))(α+1)/(α+2) ≈ −0.24; n_ρ = −[(1/3)(1/(γ−1) − 1/(α+1)) + 1](α+1)/(α+2) ≈ −0.82; n_M = (2/3)(1/(γ−1) − 1/(α+1))(α+1)/(α+2) + n_ρ/4 ≈ 0.17; n_a = γ(α+1)/((γ−1)(α+2)) ≈ 1.57; n_b = ((3γ−4)/(γ−1) + 1/(α+1))(α+1)/(α+2) ≈ 1.31.

### Eq. (17), p. 4 — envelope fraction that doubles the radius (ΔR = R_c)
```
X_2 ≈ 0.027 (P/10 days)^0.08 (M_*/M☉)^(−0.15) (τ_KH/100 Myr)^0.37 (ρ_M⊕/5.5 g cm⁻³)^(−0.82) (M_c/5 M⊕)^0.17
```
with T_eq = (L_*/16π a²)^(1/4), L_*/L☉ = (M_*/M☉)^3.2. True X_2 slightly smaller when the isothermal layer is included; "a few percent at an age of a Gyr". MESA: peak of mass-loss time at X ≈ 0.02–0.03.

### Eqs. (18)–(19), p. 4 — energy-limited mass loss
```
t_Ẋ ≡ X/Ẋ = M_env/Ṁ_env                                   (18)
Ṁ_env = η π R_p³ L_HE / (4π a² G M_p)                       (19)
```
η defined w.r.t. cross-section π R_p²; **constant η = 0.1** adopted (order 0.1 from radiation-hydro models for low-mass planets). No "effective absorption radius"; no tidal (Roche) enhancement.

### Eq. (20), p. 5 — mass-loss timescale (solar metallicity; f = R_p/R_rcb ≈ 1.2)
```
t_Ẋ ≈ 210 Myr (η/0.1)^(−1) (L_HE/10^(−3.5) L☉)^(−1) (P/10 days)^1.41 (M_*/M☉)^0.52 (f/1.2)^(−3) (τ_KH/100 Myr)^0.37
      × (ρ_M⊕/5.5 g cm⁻³)^0.18 (M_c/5 M⊕)^1.42
      × { (ΔR/R_c)^1.57   if ΔR/R_c < 1 ;   (ΔR/R_c)^(−1.69)   if ΔR/R_c > 1 }
```
Peaks at ΔR ≈ R_c (X = X_2). Discontinuity smoothed numerically by using R_p = R_c + ΔR. Below X_2 the radius is core-dominated → runaway stripping; above X_2 radius grows faster than mass → timescale shortens. Peak exists for any n_b > 3 requirement failing only if −7/3 < α < −2 (unphysical).

### Eq. (21), p. 6 — evolution: dX/dt = −X/t_Ẋ, from t = 1 Myr (disk dispersal), integrated to 3 Gyr.

### Eq. (22), p. 6 — high-energy luminosity history (Jackson et al. 2012 form)
```
L_HE = L_sat                       for t < t_sat
     = L_sat (t/t_sat)^(−1−a_0)    for t ≥ t_sat
a_0 = 0.5,  t_sat = 100 Myr,  L_sat ≈ 10^(−3.5) L☉ (M_*/M☉)
```
Exposure dominated by first 100 Myr; exact a_0 has little effect.

### Eq. (25), p. 7 — cooling time prescription (post boil-off)
```
τ_KH = 10^8 yr   for t < 10^8 yr ;   τ_KH = t   for t ≥ 10^8 yr
```
Thermal evolution and mass loss treated as independent (no boil-off feedback).

### Initial conditions / population (pp. 6–7)
- Host mass Gaussian, 1.3 ± 0.3 M☉ (CKS-like); results "not particularly sensitive to stellar mass".
- Period: dN/dlogP ∝ const for P > 7.6 d, ∝ P^1.9 for P ≤ 7.6 d (eq. 23).
- Core mass: Rayleigh dN/dM_c ∝ M_c exp(−M_c²/2σ_M²), σ_M = 3 M⊕ (eq. 24); Earth-like ρ_M⊕ = 5.5.
- **Initial envelope X_0: log-flat in [X_min, X_max] = [0.01, 0.3]**; X_max matters little if ≫1%.
- Fig. 3 inference: progenitors are either M_c > 3 M⊕ with ≥ a few % H/He, or M_c < 3 M⊕ born bare; planets < 2 M⊕ disfavoured if they have ≥ few % H/He.

### Valley location (pp. 8–10)
- Eq. (26): t_Ẋ(X = X_2, t = t_sat) ∼ t_sat.
- Eq. (27): G M_p² X_2/(8π R_c³) ∼ η t_sat L_HE/a² ≈ η 𝒳_HE (high-energy exposure).
- **Eq. (28): R_valley^bot ∝ η^0.18 𝒳_HE^0.19 ρ_M⊕^(−0.24)**; with 𝒳_HE ∝ M_*/a² → **R_valley^bot ∝ P^(−0.25)** (constant η). Largest strippable core: no bare 3 M⊕ (1.3 R⊕) beyond ~30 d, no bare 1 M⊕ beyond ~60 d.
- **Eq. (29): R_valley ∼ 1.85 R⊕ (ρ_M⊕/5.5 g cm⁻³)^(−1/3) (M_c/3 M⊕)^(1/4)** (valley at √2 R_c between R_c and 2R_c). Observed gap 1.8 ± 0.2 R⊕, peaks 1.3 and 2.6 R⊕. 10× change in ρ_M⊕ shifts valley by 2×; icy cores excluded.
- Eq. (30): core heat capacity: L = L_core + L_env ≈ (1 + 1/(17X)) L_env (core: 10⁷ erg g⁻¹ K⁻¹, SiO₂ μ=76, ~7 k_B/particle; envelope H atoms 3/2 k_B). Minor effect on valley.
- Eq. (31): variable efficiency η = 0.1 (v_esc/15 km s⁻¹)^(−2) (v_esc at photosphere) → R_valley^bot ∝ P^(−0.16); extends bare 3 M⊕ to ~50 d, 1 M⊕ to ~100 d. (Footnote: illustrative only, narrow validity.)
- Eq. (32): t_Ẋ ∝ P^1.41 M_*^(−0.48) (with L_sat ∝ M_*). Eq. (33): vs. insolation I ∝ L_*/a²: t_Ẋ ∝ I^1.06 M_*^2.2; vs. semi-major axis t_Ẋ ∝ a^2.12 M_*^(−1.19).
- Metallicity (4.4): ≤ factor 2 in timescale at 10× solar, vanishes at 100× solar; water/steam envelopes (μ≈18) push X_2 → ~0.5 and valley to P ~ 2 d → ruled out.
- Hydrodynamic outflow ceases beyond ~30 d (Jeans regime, Owen & Jackson 2012).

---

## 3. Owen & Wu 2016 — "boil-off" after disk dispersal

Notation: R_B Bondi radius, c_s isothermal sound speed of the (T_eq) gas, X_env = M_env/M_c, 𝓜_p Mach number at photosphere, κ opacity, α (this paper) = initial radius in units of R_B.

### Eq. (1)/(3), p. 2 — Bondi radius = Parker-wind sonic radius
```
R_B = G M_p / (2 c_s²) = R_s
```

### Eq. (2), p. 2 — equilibrium temperature
```
T_eq = 886 K (T_*/5800 K) (R_*/1 R☉)^(1/2) (a/0.1 AU)^(−1/2)
```

### Eq. (4), p. 2 — mass-loss rate of a planet inflated to R_B
```
Ṁ_p ∼ 4π R_B² ρ_surf c_s = 4π R_B² P_surf/c_s ≈ 1×10⁻² M⊕ yr⁻¹ (M_p/10 M⊕) (κ/0.1 cm² g⁻¹)^(−1)
```
(P_surf ≈ g/κ.)

### Eq. (5), p. 3 — Kelvin–Helmholtz time (M_env < M_c)
```
t_KH ≈ G M_c M_env / (R_p L)
```
Cooling is bottlenecked by the outer isothermal/radiative blanket: thicker for higher X_env, higher insolation, smaller R_p/R_B (Fig. 2).

### Criterion for boil-off (pp. 3, 5; Fig. 2)
- Compare t_KH against disk-dispersal time: inner-disk clearing ~10⁵ yr (local viscous time; "two-timescale" dispersal), full disk lifetime 3–10 Myr.
- From Fig. 2 (MESA): a **5 M⊕** planet stays at R_p ∼ R_B after disk removal if **X_env ≳ 10%**; **3 M⊕: ≳ 5%**; **10 M⊕ cannot** remain inflated for any relevant X_env. With t_KH = 1 Myr, embedded accretion would give X ≈ 7% for 5 M⊕ at 0.1 AU.
- Planetesimal accretion luminosity (Rafikov 2006, MMSN) overwhelms cooling luminosity unless solid density reduced by >10⁴ → planets remain isentropic with disk, i.e. inflated at R_B when disk vanishes.
- Summary: newly emerged planets with M < 10 M⊕ and X_env ∼ 5–30% have R_p ∼ R_B and boil off.

### Eqs. (6)–(9), p. 5 — Parker-wind mass-loss rate for R_p < R_B
```
Ṁ = 4π R_p² ρ_surf u_surf = 4π R_p² 𝓜_p (P_surf/c_s) = (4π G M_p/(κ c_s)) 𝓜_p        (6)
𝓜_p = sqrt(−W_0[−f(R_p/R_B)])                                                        (7)
    ≈ (R_p/R_B)^(−2) exp(−2 R_B/R_p)   when R_p ≪ R_B                                (8)
f(x) = x^(−4) exp(3 − 4/x)                                                            (9)
```
(W_0 = principal real branch of Lambert function.)

### Eq. (10), p. 5 — mass-loss timescale
```
t_ML ≡ M_env/Ṁ = (κ c_s/(4πG)) X_env 𝓜_p^(−1)
     ≈ 10³ yr · X_env · 𝓜_p^(−1) · (T_eq/886 K)^(1/2) · (κ/0.1 cm² g⁻¹)^(−1)
```

### Eq. (11), p. 5 — stalling radius (exponential sensitivity → R_p/R_B ∼ 0.1 always)
```
(R_p/R_B)² exp(2 R_B/R_p) ≈ X_env^(−1) (t_ML/10³ yr) (T_eq/886 K)^(−1/2) (κ/0.1 cm² g⁻¹)
```
Mass loss effectively shuts off once R_p ∼ 0.1 R_B; final radius only logarithmically sensitive to parameters.

### Eq. (12), p. 6 — advected luminosity (why it cools fast)
```
L_adv ≈ (γ/(γ−1)) Ṁ c_s² ∼ 10²⁶ erg s⁻¹ (Ṁ/1×10⁻⁵ M⊕ yr⁻¹) (c_s/3×10⁵ cm s⁻¹)²
```
≫ internal cooling luminosities (Fig. 1: 10²²–10²⁷ erg s⁻¹ for 5 M⊕). Contraction to ∼0.1 R_B within a few t_ML.

### Eqs. (13)–(16), p. 6 — final envelope mass from energy budget
```
U_i = −A_i G M_c M_env^i/(α R_B)          (13)   [initial radius α R_B, α ≤ 1]
U_e = −10 A_e G M_c M_env^f/R_B           (14)   [final radius 0.1 R_B]
U_lost ≈ G M_c (M_env^i − M_env^f)/(α R_B) (15)
M_env^f = ((A_i + 1)/(10 α A_e + 1)) M_env^i ≈ 0.1 α^(−1) M_env^i   (16)   [A_i ∼ A_e ∼ 1]
```
→ **~10% of the initial envelope survives** (starting at R_B, α = 1).

### Numerical results (MESA, §4; pp. 7–10)
- Setup: start hydrostatic at R_p = R_B (α = 1), X_0 = 10% or 30%, M_c = 3, 5, 10 M⊕ (pure rock, Fortney+07 M–R), T_eq = 500 K or 900 K; Parker rate capped at **10% of the energy-limited rate** when it exceeds it; run to 3 Myr (mass loss ceased in all cases).
- Mass loss ceases after a few 10⁵ yr when R_p ∼ 0.1 R_B; final envelope ∼10% of initial (consistent with eq. 16). Fig. 4 shows X(t) from 10⁰ to 10⁸ yr; envelope fractions drop from 0.1/0.3 to ∼0.01–0.05 within ∼1 Myr.
- 900 K models lose ~2× more than 500 K models. Lower-mass cores lose more; 3 M⊕ can be stripped to "naked" cores. Final X scales roughly with core mass (Fig. 8: final X ∼ 10⁻³–10⁻¹ over 3–10 M⊕; order 1% for Kepler-like planets inward of ∼0.5 AU, T_eq ≈ 400 K).
- After 3 Myr all planets have cooling time **4×10⁷–10⁸ yr**, ~20× longer than pure gravitational contraction would give; a 5 M⊕, X_0 = 10%, 500 K planet at 1 Myr "looks like one that has cooled for ∼50 Myr" (Fig. 6). Luminosity drops 100× within 1 Myr.
- Fig. 10: radii at 10 Gyr cluster around **2.5 R⊕** for M_c < 10 M⊕.
- Three mass-loss stages (conclusion): embedded (∼10⁵ yr), boil-off (∼10⁶ yr), photoevaporation (∼10⁸ yr) [paper prints "Myrs" — evidently a typo for yr]. Boil-off is the initial condition for photoevaporation; explains lack of planets > 2.5 R⊕ inward of ~0.5 AU; predicts more Neptunes beyond ≳1 AU; planets > 10 M⊕ immune.

---

## 4. Ginzburg, Schlichting & Sari 2018 — core-powered mass loss

Notation: f ≡ M_atm/M_c, ΔR = R_rcb − R_c (convective-layer thickness; R_rcb ≈ observed radius), g ≡ G M_c/R_c², γ = 7/5 (diatomic), μ = m(H₂). Core M–R: **M_c/M⊕ = (R_c/R⊕)^4**. Thin regime R_c/R_B ≲ ΔR/R_c ≲ 1 (reached a few Myr after disk dispersal, GSS16/OW16).

### Eq. (1), p. 2 — atmosphere mass (thin regime)
```
M_atm = ((γ−1)/γ) 4π R_c² ρ_rcb ΔR (R'_B ΔR/R_c²)^(1/(γ−1))
```
### Eq. (2), p. 2 — modified Bondi radius
```
R'_B ≡ ((γ−1)/γ) G M_c μ/(k_B T_rcb),   T_rcb ∼ T_eq;   R_B ≡ G M_c μ/(k_B T_eq) ≫ R_c
```
### Eq. (3), p. 2 — core (bottom-of-atmosphere) temperature, valid R_c/R'_B ≲ ΔR/R_c ≲ 1
```
k_B T_c = ((γ−1)/γ) (G M_c μ/R_c²) ΔR
```
### Eq. (4), p. 2 — cooling luminosity (radiative-layer bottleneck)
```
L = −Ė_cool = (64π/3) σ T_rcb⁴ R'_B/(κ ρ_rcb)
```
### Eq. (5), p. 2 — available cooling energy (envelope + isothermal core)
```
E_cool = g ΔR [ (γ/(2γ−1)) M_atm + (1/γ)((γ−1)/(γ_c−1))(μ/μ_c) M_c ]
```
Ratio core/envelope heat capacity ∼ (μ/μ_c) f⁻¹; adopted as **17 f** (i.e. envelope/core = 17 f) for comparison with OW17 eq. (30).

### Criterion, §2.1, p. 3
- Energy to unbind atmosphere: **E_loss = G M_c M_atm/R_c = M_atm g R_c**. Compare with E_cool.
- **Heavy atmospheres, f > μ/μ_c ∼ 5%**: at ΔR = R_c, E_cool ∼ E_loss, but as ΔR shrinks E_cool < E_loss → cooling time < mass-loss time → survive intact.
- **Light atmospheres, f < μ/μ_c ∼ 5%**: core heat dominates, E_cool > E_loss → mass-loss time < cooling time; since E_cool ∝ M_c ΔR the envelope loses mass by lowering ρ_rcb while ΔR barely changes → runaway stripping to bare core.
- Threshold: envelopes with f ≳ 5% "regulate their own cooling and survive."

### Eqs. (6)–(7), p. 3 — Bondi-limited escape (the thing that gives the T_eq/period dependence)
```
|Ṁ_atm| < Ṁ_atm^B ≡ 4π R_B² ρ(R_B) c_s,   c_s ≃ (k_B T_eq/μ)^(1/2)         (6)
ρ(R_B)/ρ_rcb = exp(−R_B/R_rcb + 1)                                             (7)
```
Exponential dependence on R_B/R_rcb ∝ M_c^(3/4)/T_eq separates light/hot planets (lose atmospheres within a few Gyr) from massive/cold ones (retain). Allows rare survivors with 0 < f < 5%.

### Eq. (8), p. 3 — time-stepping scheme
```
E_cool → E_cool − L Δt                               (8a)
M_atm → M_atm − min(L/(g R_c), Ṁ_atm^B) Δt            (8b)
```
Δt = 1% of min(cooling time, mass-loss time); ρ_rcb and ΔR updated from eqs. (1),(5) each step; radius = R_c + ΔR. Efficiency is order unity (~1/2 of L radiated when Bondi-limited); coefficient omitted. Photoevaporation deliberately excluded.

### Eq. (9), p. 4 — opacity at RCB (Freedman+08; valid 500 K < T_rcb < 2000 K)
```
κ/(0.1 cm² g⁻¹) = (ρ_rcb/10⁻³ g cm⁻³)^0.6
```

### Population setup (§3, pp. 4–5)
- Demonstration: M_c = 3 M⊕, T_rcb = 10³ K, start at ΔR = R_c (R = 2.6 R⊕), f log-flat 10⁻⁵–1, 3 Gyr → valley at **1.5–2.0 R⊕**; even without mass loss a log-flat f gives a valley (light envelopes cool/shrink fast), core-powered loss deepens it.
- Nominal: dN/dlog T_eq ∝ const (500–1000 K), ∝ T_eq^(−6) (1000–2000 K) (eq. 10; P ∝ T_eq^(−3)); dN/dM_c ∝ const (M_c < 5 M⊕), ∝ M_c^(−2) (M_c > 5 M⊕) (eq. 11) [vs OW17 Rayleigh eq. 12, σ_M = 3 M⊕]; **initial f = 0.05 (M_c/M⊕)^(1/2)** (from GSS16 eq. 24, includes accretion + thick-regime loss); evolved 3 Gyr; >6500 tracks.
- Atmospheres with f < 10⁻⁶ counted as fully lost.

### Predicted valley dependence (§3.3, p. 6; Fig. 5)
- No closed-form R_valley(P) is given. Dependence enters through eq. (7): mass loss more prominent at high T_eq (short P or hot stars). **T_eq > 10³ K (P ≲ 10 d): distribution dominated by stripped cores; T_eq < 10³ K (P ≳ 10 d): surviving-atmosphere peak dominates.** Trend with period/flux similar to photoevaporation.

### Difference from photoevaporation (abstract; §4, pp. 6–7)
- Energy source is the planet's own cooling luminosity (core-dominated), not stellar high-energy photons. Depends on **bolometric** flux via T_eq (sets both cooling rate, eq. 4, and Bondi escape rate, eqs. 6–7), "regardless of the high-energy incident flux".
- Distinguishing tests: planet populations around different stellar types (photoevaporation ∝ high-energy tail; core-powered ∝ L_bol/T_eq); XUV has large scatter at fixed stellar mass (Tu+15) → photoevaporation "desert" less distinct than the core-cooling one; the two act on different timescales (photoevaporation first ~100 Myr; core-powered over Gyr).
- Both models' T_eq scalings are similar except at high temperatures and masses (GSS16 Fig. 3). Each side argues the other only strips envelopes already doomed.
