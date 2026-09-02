# Volatile Worlds

An interactive reading companion for a PhD paper list on exoplanet interiors and
machine-learning methods (Universität Bern). One tab per paper; every station is a
live, playable model — sliders, samplers, and in some cases genuine neural networks
training in the browser.

**Everything is a single self-contained HTML file** — no build step, no dependencies.
Open `index.html` in a browser, or serve it from anywhere.

## Tabs

| Tab | Paper | What you can play with |
|---|---|---|
| break the degeneracy | Alibert 2016, A&A 591, A79 | Build a planet and meet its "impostor" (same M, R — different interior); the 55 Cnc e radius→water inversion; evolution tracks; the PLATO two-step population experiment (calibrate on old, test on young) with CDF/histogram views |
| map the degeneracy | Dorn et al. 2017, A&A 597, A37 | A live importance-sampling Bayesian interior inference: posteriors for iron/ice/gas, stellar-abundance constraint toggle, Neptune validation preset, the water–gas degeneracy cloud, and a "which measurement buys which knowledge" budget |
| photobombing → interiors (concept tab) | Cacaj et al. 2025, AJ 169, 244 | The paper's target-confusion and cancellation criteria transcribed onto the (M, R) plane: a dictionary between point sources and planet layers, the interior confusion map (which truths a two-layer modeller misreads, with the scorched-bare assumption as default), the cancellation map (Dorn's ridge with the noise blob cut out), and the uncorrelation age with the number of planets needed to expose the impostor |
| evolve the population | Kubyshkina & Fossati 2022, A&A 668, A178 | Atmospheric escape + thermal evolution: one planet around slow/moderate/fast rotators, a synthetic mass–radius diagram carved by escape through time, and the radius-spread budget |
| gas escape (concept tab) | — not a paper; Kubyshkina et al. 2018 ApJL 866 L18, Zahnle & Catling 2017 | Every way gas leaves a planet, including the ones Kubyshkina's models skip: a Maxwellian tail explorer (exact Jeans flux, λ meter), the hydrodynamic regime map (the published 2018 analytic fit, boil-off vs XUV-driven), the cosmic shoreline for solar-system bodies and exoplanets, and a three-mechanism envelope evolution you can switch off one at a time |
| learn the equation | Baty 2023, Astron. Comput. 44, 100734 | A real PINN (tanh MLP, exact hand-derived backprop through the Lane–Emden residual) training live; plus the two-input "solution family" network demonstrating interpolation vs. extrapolation |
| emulate the simulator | Moseley et al. 2020, Solid Earth 11, 1527 | A live 2-D finite-difference seismic wavefield; a surrogate MLP trained in-browser on FD simulations generated at page load; an out-of-distribution error scan and a measured speed benchmark |

Planned: Egger et al. 2024 (plaNETic), Leleu et al. 2021 (TOI-178), Mishra et al.
2023 (architecture framework), Davoult et al. 2024 (Earth-like planet hosts).

## Honesty notes

The physics engines are **calibrated toy models**, not the papers' codes. Each tab's
footer states exactly what is real (the neural networks and their training are) and
what is a parametrization tuned to reproduce the paper's published figures. The
lessons are the papers'; the numbers are illustrative.

## Development

The whole app is `index.html`: markup, styles, and one `<script>` block sharing a
small chart/scale/tooltip toolkit and one seeded RNG. Before committing changes:

```bash
./tools/check.sh
```

This extracts the inline script and executes it headlessly with macOS
JavaScriptCore (`jsc`) against `tools/dom_shim.js` — catching syntax errors,
missing element ids, and runtime init failures without opening a browser.
`tools/pinn_check.py` is a pure-Python port of the PINN used to verify the
hand-derived backpropagation against finite differences.

Two conventions that have already bitten once: every tab's state object needs a
unique top-level name (a duplicate `const` is a syntax error that blanks the whole
page), and never call `.map` on a `Float64Array` to build coordinate pairs — wrap
with `Array.from` first.

Two more from later bugs: a leapfrog finite-difference update must write into a
separate buffer (an in-place update is unconditionally unstable), and log-axis
tick formatters must round `Math.pow(10, Math.log10(v))` before printing.

Beyond the init-only harness, sweep the sliders headlessly (set the state objects,
call the draw functions, scan every node's innerHTML for NaN/Infinity/undefined)
and take one headless-Chrome screenshot per new tab: copy `index.html` to a
scratch file, append `<script>showTab('<id>')</script>`, and run
`Google Chrome --headless=new --virtual-time-budget=6000 --window-size=1100,6000 --screenshot=...`.
