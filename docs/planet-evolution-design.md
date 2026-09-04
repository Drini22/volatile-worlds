# Planet evolution — concept tab design spec

Status: design, no code yet. Written 2026-09-04 after reading Alibert (2016) and the papers listed in §9.
Tab id `evo`, JS/state prefix `ae`/`AE` (checked free on commit a41dcba; `ev`, `pv`, `pe` are taken).
Concept row: button right after **Frost line**, subtitle "after Alibert · cooling, escape and the star's clock".
`page-evo` sits right after `page-frost`. `TABS` gains `"evo"`, init calls `aeDrawAll()`.

## 1. Purpose

Alibert (2016) shows that composition sets a planet's energy budget, and the energy budget sets how its radius
shrinks with time. Kubyshkina (2022) and the Gas escape tab show that the star's XUV strips envelopes on the same
clock. No tab shows both acting on one planet under a star that is itself evolving. This tab does that, with one
time knob, and then lets the reader watch a whole population slide across the mass–radius diagram as the knob turns.

The three things the reader should take away:

1. A planet's radius is a function of age, not a constant. Cooling contracts the envelope; escape thins it.
2. The star's history is half the model. An M dwarf stays bright and XUV-saturated for hundreds of Myr,
   a Sun for tens. Same planet, different star, different fate.
3. The radius valley is not put in by hand. It opens by itself when the population is evolved.

## 2. Sections

### §0 Hero
Eyebrow "Concept tab · after Alibert 2016". Standfirst: "A planet's radius is a clock. This page runs it."
Reuse the Alibert layer key (iron core, silicate mantle, icy mantle, H/He envelope).

### §1 The star's clock
Controls: star mass (buttons 0.3 / 0.6 / 1.0 M☉), rotation (slow / medium / fast, i.e. 5th / 50th / 95th
percentile as in Johnstone 2021), orbital distance slider (log, 0.02–1 AU, default 0.1 AU). These three are the
tab's global inputs; §2–§4 read them.

Chart A: log L_bol(t) and stellar radius, 1 Myr–10 Gyr, with the pre-main-sequence end marked.
Chart B: log L_XUV(t) for the three rotation tracks with the selected one bold; saturation end marked.
Readout row at the §2 knob time: L_bol, T_eq at the planet, F_XUV at the planet (erg cm⁻² s⁻¹ and ×F⊕).

### §2 One planet through time
Controls: total mass 1–15 M⊕, water fraction of the solid 0–0.7, initial H/He fraction 0–0.3, and the **time
knob** (log 1 Myr–10 Gyr, default 5 Gyr). Toggles: cooling only / cooling + escape; boil-off on/off.

Left: the Alibert cross-section (`drawPlanet`) at the knob time, envelope scaled to the current transit radius.
Right: R(t) track with two curves (cooling only dashed grey, cooling + escape solid ice) and the knob marker;
below it the remaining envelope fraction f_gas(t). Vertical guides at pre-MS end and saturation end from §1.
Readouts: R, f_gas, T_eq, F_XUV, Ṁ now, cumulative loss in M⊕ and % of the initial envelope, "bare since".
One extra readout that answers the question that started this tab: "if the envelope were gone, water lost so
far: N Earth oceans (of M available)", energy-limited with ε = 0.3 (Luger & Barnes 2015), shown greyed while
the envelope is present.

### §3 The population on the mass–radius diagram
A synthetic sample of 400 planets around the §1 star, evolved once per star/rotation choice, drawn at the knob
time (§3 has its own knob, initialised from §2's). Composition presets: all dry / all 70 % water / mixed.
Draw: points coloured rust (bare) vs ice (envelope kept), the rocky and 70 %-water iso-composition lines at
the knob age, the archive planets from `RV_DATA` in grey behind them, and a radius histogram at the right edge
where the valley opens. Chip: valley position (minimum of the histogram between 1.3 and 2.5 R⊕) and its
Owen & Wu (2017) prediction 1.85 R⊕ (ρ/5.5)^(−1/3) (M_c/3 M⊕)^(1/4) for the sample's median core.

### §4 Same planet, three stars
The §2 planet placed at the distance that gives the same T_eq today around each of the three stars, three R(t)
tracks overlaid. This is the Luger & Barnes point: at equal present-day irradiation the M-dwarf planet saw a
brighter, longer-saturated star when it was young. Chips: envelope kept (%) per star, bare-since per star.

### §5 What's real and what's a toy
Same style as the frost tab: one paragraph of what each curve is, then the not-modelled list (steam inflation,
core-powered mass loss, water–H/He miscibility, magma-ocean solubility, migration, late accretion), then the
reference line.

## 3. Physics

### 3.1 Star
- **L_bol(t), R★(t), T_eff(t)**: BHAC15 tracks (Baraffe et al. 2015), resampled every 0.25 dex in log age for
  0.3, 0.6, 1.0 M☉ (`scratchpad/baraffe_coarse.txt`, 18 rows each), log-log interpolation via the frost tab's
  `flInterp`. The 1 M☉ track ends at 8.3 Gyr; extend with Gough (1981) scaled to match at the join. The 0.3 and
  0.6 tracks reach 10 Gyr. Check: 1 M☉ gives L = 1.00 ± 0.02 L☉ at 4.57 Gyr; 0.3 M☉ drops ×60 from 0.5 Myr
  to 300 Myr.
- **L_X(t)**: saturated `L_X = 5.135e-4 · L_bol(t)` (Johnstone 2021 R_X,sat) until t_sat(M★, rot), then
  `L_X,sat(t_sat) · (t/t_sat)^(−1.23)`. t_sat table (Johnstone 2021 Fig. 10 read-offs), Myr:

  | M★ | slow | medium | fast |
  |---|---|---|---|
  | 0.3 | 1000 | 1600 | 1900 |
  | 0.6 | 40 | 350 | 700 |
  | 1.0 | 5 | 22 | 280 |

  The 1.23 decay index is the Jackson (2012) mean 1.19 and Luger & Barnes 1.23; it also lands the 1 M☉ medium
  track on the solar value below.
- **L_EUV from L_X**: Johnstone 2021 eqs. 19 and 21 on surface fluxes, F_X = L_X/(4πR★²):
  `log F_EUV1 = 2.04 + 0.681 log F_X`, `log F_EUV2 = −0.341 + 0.920 log F_EUV1`, `L_XUV = L_X + L_EUV1 + L_EUV2`.
- **Normalisation**: rescale the whole 1 M☉ family by one constant so the medium track gives
  F_XUV(1 AU, 4.57 Gyr) = 4.6 erg cm⁻² s⁻¹ (Ribas 2005, the F⊕ used by Lopez & Fortney and by the escape tab).
  Report the constant on the page; it should be within the 0.36 dex scatter Johnstone quote.
- **F_XUV(a, t) = L_XUV(t)/(4πa²)**, **T_eq(a, t) = 278.6 K · L_bol^(1/4) · a^(−1/2)** (zero albedo, full
  redistribution, same as the frost tab's bare-body line).
- Before 3 Myr the disk is present: hatch the region and freeze escape (planet is embedded).

### 3.2 Planet structure at (M, f_water, f_gas, F, t)
- Solid radius: `egRsolid(Ms, cmf = 0.325, f_ice)` as in the Egger tab (Zeng-type rock with Alibert's ice
  factor). Water is treated as condensed, i.e. Alibert's ice-VII layer; see §6 for the steam caveat.
- Envelope: Lopez & Fortney 2014 eq. 3 (enhanced opacity)
  `R_env = 2.06 R⊕ (M/M⊕)^(−0.21) (f_env/0.05)^0.59 (F/F⊕)^0.044 (t/5 Gyr)^(−0.18)`,
  with F the **bolometric** flux from §1 (it changes with time here, unlike in the Egger tab), and an age
  floor of 10 Myr (LF14 validity 10 Myr–10 Gyr; the Egger tab's floor is 100 Myr). f_env is the envelope
  mass over total mass. New helper `aeRenv`, not `egRenv`, because the floor differs.
- Radiative skin: LF14 eq. 2, `R_atm ≈ 9 k T_eq / (g μ)` with μ = 2.35 m_H (~0.1 R⊕). The Egger tab omits it.
- Transit radius R = R_solid + R_env + R_atm. Alibert's own cooling comes in through the LF14 age term, which
  already includes core heat capacity and radiogenic heat (LF14 §2.2; Mordasini 2012 Table 1 isotopes).

### 3.3 Escape
- Reuse the Gas escape tab engine: `escHBA` (Kubyshkina 2018 hydro-based approximation, needs F, a, R, Λ),
  `escEL` energy-limited fallback with ε = 0.1 (Owen & Wu 2017), `escRelax` boil-off at disk dispersal
  (Owen & Wu 2016 criterion Λ vs e^Σ). Replace `escFxuv(a, t, rot)` by the §1 flux and `escRadius` by §3.2.
- Integration: log grid 1 Myr–10 Gyr, 300 steps, adaptive sub-steps capped at 5 % of the envelope per step
  (copy the loop shape of `escEvolve`). Cost target: one track < 5 ms, so the 400-planet population is < 2 s
  and runs in an idle callback after init.
- Water does not escape in v1. The "oceans lost if bare" readout integrates ε π F_XUV R³/(G M) with ε = 0.3
  over the bare-planet history and divides by 1.4 × 10²⁴ g; it is a bound, labelled as such.

### 3.4 Population (§3)
- Cores: Rayleigh with σ = 3 M⊕, truncated to 1–15 M⊕ (Owen & Wu 2017).
- Initial envelope fraction: log-flat in 0.01–0.3 (Owen & Wu 2017), then boil-off at 3 Myr.
- Water fraction: preset; "mixed" = uniform 0–0.7.
- Periods log-uniform 1–100 d converted to distance for the selected star mass (Kepler's law with M★).
- Fixed random seed so the picture is reproducible between publishes.

## 4. State and helpers

`AE = { mstar: 1.0, rot: "med", a: 0.1, m: 8, fw: 0, fg0: 0.05, t: 5000, esc: true, boil: true }` (t in Myr),
`AE3 = { t, preset, seed }`. Consts `AEC` (cgs + Earth/Sun units), `AE_STAR` (three BHAC15 tables),
`AE_TSAT`, `AE_TS` (time grid). Helpers `aeLbol, aeRstar, aeLx, aeLxuv, aeFxuv, aeTeq, aeRenv, aeRadius,
aeEvolve, aePop, aeDraw1..4, aeReadouts, aeDrawAll`. Grep for every new top-level name before committing.

## 5. Validation targets (all must pass headlessly before the first publish)

| check | target | tolerance |
|---|---|---|
| L_bol 1 M☉ at 4.57 Gyr | 1.00 L☉ | 2 % |
| F_XUV 1 AU today, 1 M☉ medium | 4.6 erg cm⁻² s⁻¹ | by construction |
| L_X 0.3 M☉ saturated plateau | 2 × 10²⁸ erg s⁻¹ (Johnstone Fig. 5) | 0.3 dex |
| L_X 1 M☉ at 10 Myr, fast | 2.5 × 10³⁰ (Johnstone Fig. 11) | 0.3 dex |
| LF14 5.5 M⊕, 10 F⊕, 1 % H/He, enhanced opacity | 2.60 / 2.27 / 2.07 R⊕ at 0.1 / 1 / 10 Gyr | 5 % |
| Mordasini 2012 4.2 M⊕ + 1 % H/He at 0.1 AU, cooling only | 2.37 / 2.31 / 2.17 R⊕ at 0.1 / 1 / 10 Gyr | 7 % |
| Alibert Fig. 3 pair (12 M⊕: dry + 10 % gas vs 70 % water + 4 % gas), cooling only | equal R at 5 Gyr within 3 %; dry larger at 100 Myr | qualitative |
| boil-off, 5 M⊕ core, 10 % initial, 1 M☉ | survives with ~1–3 % (Owen & Wu 2016) | range |
| population valley, 1 M☉ medium, all dry | minimum between 1.5 and 2.0 R⊕ | range |
| valley vs period | shallower (P^−0.25 slope sign) | sign |
| Luger & Barnes: bare 1 M⊕ at the 0.3 M☉ HZ distance | ≥ 1 Earth ocean lost by 5 Gyr | bound |
| slider sweep | no NaN / Infinity / undefined in any node's innerHTML | strict |

Plus the standing harness: `./tools/check.sh`, the jsc concatenated test, the headless slider sweep, and a
Chrome screenshot of the tab at the default state.

## 6. Known simplifications (goes on the page in §5)

- Water is condensed (ice-VII equation of state through the Alibert ice factor). A hot water layer carries a
  steam skin that inflates the radius by roughly 10 % per 1 % of steam (Turbet 2020) and by up to 10 % more
  for supercritical layers at 1300 K (Aguichine 2021). Not modelled in v1; phase 2 could add the Aguichine
  fit once its Zenodo coefficient table is fetched.
- H/He and water are treated as separate layers; at these temperatures they are miscible and hydrogen
  dissolves in a magma ocean.
- Escape is photoevaporation only. Core-powered mass loss (Ginzburg 2018) is a bolometric-flux effect with a
  similar valley and is mentioned, not computed.
- No migration, no late accretion, no planet-to-planet variation in stellar age within the population.
- Below 10 Myr the LF14 fit is extrapolated; the disk era is hatched.

## 7. Reuse map

| need | existing helper | tab |
|---|---|---|
| cross-section drawing | `drawPlanet(svg, m, fv, fg, radius5, xIron)` | Alibert |
| solid radius with ice factor | `egRsolid` | Egger |
| escape rate, boil-off, Jeans | `escHBA, escEL, escRelax, escJeans, escSigma, escLam, ESCC` | Gas escape |
| log-log table interpolation | `flInterp` | Frost line |
| axes, scales, paths, ticks | `makeScales, axes, linePath, niceTicks, el, fmt` | shared |
| archive planets | `RV_DATA` | Radius valley |

## 8. Build order

1. Star model + §1 charts, validate the star rows of §5.
2. Structure + cooling-only track, validate LF14 / Mordasini / Alibert rows.
3. Escape coupling, boil-off, §2 complete.
4. Population + histogram + valley chip.
5. §4 three-star overlay.
6. §5 text, references, README row, memory note.
Commit after each step passes `check.sh`; ping the other sessions before committing `index.html`.

## 9. Papers used (all in `papers/evolution/` except the two already in `papers/`)

Alibert 2016, A&A 591, A79 · Kubyshkina & Fossati 2022, A&A 668, A178 · Lopez & Fortney 2014, ApJ 792, 1 ·
Owen & Wu 2016, ApJ 817, 107 · Owen & Wu 2017, ApJ 847, 29 · Ginzburg, Schlichting & Sari 2018, MNRAS 476, 759 ·
Jackson, Davis & Wheatley 2012, MNRAS 422, 2024 · Tu et al. 2015, A&A 577, L3 · Johnstone et al. 2021, A&A 649, A96 ·
Baraffe et al. 2015, A&A 577, A42 (BHAC15 tracks file alongside) · Luger & Barnes 2015, Astrobiology 15, 119 ·
Baraffe et al. 2008, A&A 482, 315 · Valencia et al. 2013, ApJ 775, 10 · Mordasini et al. 2012, A&A 547, A112 ·
Aguichine et al. 2021, ApJ 914, 84 · Turbet et al. 2020, A&A 638, A41 · Ribas et al. 2005, ApJ 622, 680 (F⊕ XUV).
Extraction notes with every coefficient: `notes_envelope_escape.md`, `notes_stellar_xuv.md`, `notes_water_worlds.md`
(`docs/notes/`, with `baraffe_coarse.txt`).
