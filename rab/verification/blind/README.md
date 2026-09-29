# WS2 blind rebuild: M3 (branch), M4 (cap share, D6), M8 (sensitivity)

Gate B dual computation for the RAB Kit (RUN_PLAN s2, s3). Built 2026-09-30 (Sydney) from the SPEC files only.
AI-generated research (Claude Code) for Team Caplet; no deliverable text. Nothing here changes the strategy.

## Blind protocol

Read: `rab/models/M3_SPEC.md`, `M4_SPEC.md`, `M8_SPEC.md`; `rab/models/M1_METHOD.md` sections 1, 2 and A only (the D1
curve recipe that M8_SPEC section 1 incorporates by reference; its numbers are Gate A locked and were reproduced here
to the cent before anything else ran); `rab/numbers.yaml`; `rab/data/`. Not opened: any `.py` under `rab/models/` or
`rab/results/`, the model cards, the D6 memo, insight_v1 scripts. One unavoidable exposure: the WS2 primary's one-line
summary in `/Users/ray/Research/rab-ws/STATUS.md` (which every stream must append to) was on screen before this build
started. It gives four rounded headlines (2031 top about $175k, 90% $165k-$191k; gift at top 72-75%; robust s* 0.47;
floor $145k) and no detail. Every number below was computed independently; none was tuned to it.

Environment: `/Users/ray/Research/rab-ws/.venv` (numpy 2.5.3, scipy 1.18.1, pandas 3.0.6, pymc 6.3.2, arviz 1.3.0,
pymoo 0.6.2, SALib 1.6.0, matplotlib 3.11.2). pytensor's C compiler fails on this Mac (Apple clang 21: `ld: library
'd64' not found`), so `blind_common.py` sets `PYTENSOR_FLAGS=cxx=` and pymc runs pure-Python ops: same model, slower,
still 2 s for the 155-point fit. arviz 1.x renamed `hdi_prob`; the summary call uses defaults. Seed 20260930 through
`numpy.random.SeedSequence([20260930, hash(model tag)])`, one independent stream per model, 200,000 paths each.

Run everything: `./run_all.sh` (about 4 minutes; M3 4 s, M4 85 s, M8 104 s). Outputs in `out/` (paths in `out/paths/`
are gitignored and regenerate from the seed).

## Files

| File | What |
|---|---|
| `blind_common.py` | D1 curve (vectorised over parallel shifts), ladder, the four return models, the rule; `python blind_common.py` prints the Gate A reproduction |
| `blind_m3.py` | M3: L, T, BOOT (+raw, b1, b60), BAYES (+hist); `out/M3/summary.csv`, `range_confidence.csv`, `conditional_top.csv`, `bayes_posterior.csv`, `reconcile_E6.csv`, `numbers_proposed_blind.yaml`, 3 figures |
| `blind_m4.py` | M4: floor delivery, PR-3..PR-7, s-profile, rule sensitivity, NSGA-II fronts (+ grid check), narrower range; `out/M4/*.csv`, 3 figures |
| `blind_m8.py` | M8: curve-shift model, tornado, Sobol A (luck included) and B (assumptions only), the pre-registered top-3, floor reading; `out/M8/*.csv`, 2 figures |
| `collect_headlines.py` | 307 headline keys with their Gate B tolerance -> `out/blind_headlines.json`, `out/BLIND_HEADLINES.md` |

## Checks that had to pass before the models ran

- Gate A curve: V0 $289,119.20, V_A $292,418.11, headroom $7,581.89, break-even 26.20 bp; exact basis $287,016.47 /
  $290,291.38 / 33.22 bp; V_2028 $306,524.65 / $304,295.32; floor cost $117,193.70; B0 $40,736.19. All equal the locked
  values (`out/common_check.log`).
- T-model scale from the spec's definition: c = 0.1162464, 0.268% of raw draws discarded (spec: 0.1162464, 0.268%).
- Floor delivery: phi(r = y5) = 0.9965, phi(r = 0) = 0.9755 (spec 0.9965, 0.9755).
- L analytic: median top $174,988 vs $174,952 analytic; P(top) 0.7328 vs 0.7325.
- BAYES fit converged: r_hat 1.00, bulk ESS about 2,600 for m_h, sigma, nu.
- M8 base: V_A(0) = $292,418.11, B0 = $40,736.19 exact.

## Headline results (all MODEL, seed 20260930, N = 200,000; B0 = $40,736.19, F = $150,000, s = 1/2)

### M3: the 2031 range and the 2033 gift

| model | 2031 top p5 / p50 / p95 | 2033 gift p5 / p50 / p95 | kept p50 | P(top reached) | P(upper half) | P(fund below cost 2031) |
|---|---|---|---|---|---|---|
| T (fat tails) | 166,147 / 174,966 / 188,638 | 165,123 / 174,257 / 187,904 | 32,106 | 75.5% | 99.9% | 20.7% |
| BOOT (Shiller blocks) | 165,182 / 175,472 / 189,200 | 163,705 / 174,550 / 188,233 | 33,297 | 74.4% | 99.2% | 21.9% |
| BAYES (uncertain mean) | 165,308 / 175,001 / 190,687 | 164,142 / 174,046 / 189,735 | 32,230 | 71.8% | 99.9% | 24.3% |
| L (reference) | 166,088 / 174,988 / 188,742 | 165,133 / 174,196 / 187,933 | 32,228 | 73.3% | 100.0% | 22.4% |

Plain words: the top Laura announces in 2031 is about $175,000 in every model (90% band about $165,000 to $190,000);
the 2033 gift lands at that top about three times in four and in the upper half of the range in over 99% of paths.
The bottom, $150,000, is certain by construction under the four M3_SPEC s5 conditions; P(G >= F) = 1 in every model.
Variants: BOOT-raw (history's own 8.95% mean) median top $177,196; BAYES-hist (US history as the forecast) $177,051;
block length 1 vs 60 months moves the top's p5 by about $1,100 and P(top) by 1.5 points. Serial dependence in BOOT
(24-month blocks) does not make the top harder to reach after a weak first three years: P(top | B3 below median)
0.744 vs 0.743 above. BAYES posterior: m_h 0.0946 (sd 0.013), sigma 0.157 (sd 0.012), nu 18.1 (sd 11.5).
E6 reconciliation (L, B0 $40,400, seed 20260927): total p5/p50/p95 $182,115 / $206,744 / $249,872 against insight_v1's
$182,000 / $207,000 / $250,000.

### M4: the cap share (D6), pre-registered rule

- Floor delivery: 8,565 thirty-month changes of the 1-year yield since 1990 (2.5% to 97.5%: -4.71 to +4.90 points);
  phi p0.5 / p5 / p50 / p95 / max = 0.9757 / 0.9776 / 0.9961 / 1.0162 / 1.0214 (min 0.9755); P(phi < 0.98) = 9.1%,
  P(phi < 0.975) = 0; r is floored at 0 in 0.4% of paths.
- **PR-3:** h* = 0.025, announced floor **A = $145,000**; P(phi F < A) = 0.000%.
- **PR-6:** s*_T = 0.50, s*_BOOT = 0.47, s*_BAYES = 0.47 (L 0.50); **robust s* = 0.47**. PR-4 (credibility) never
  binds; PR-5 (keep at least 10% of the gift with 95% confidence) binds in every model.
- **PR-7: keep s = 1/2** (0.40 <= 0.47 <= 0.60). No deviation from the rule.
- Adopted half, per model: E[G] $174,110-$174,242; P(K >= 0.1 G) 93.2% (BAYES), 93.7% (BOOT), 95.4% (T); P(G < A) = 0;
  E[width] about $31,000; median top $175,000.
- Rule sensitivity (robust s*): flexibility 5% -> 0.76 / 0.72 / 0.59 at 90 / 95 / 99%; 10% -> 0.53 / **0.47** / 0.20;
  15% -> 0.32 / 0.23 / none; 20% -> 0.13 / 0.01 / none. PR-7 would still say "keep half" for (5%, 99%), (10%, 90%) and
  (10%, 95%); it would say 2/3 or 3/4 at a 5% threshold with 90-95% confidence, and 1/4 or less at 15-20%.
- NSGA-II (120 x 200, first 50,000 paths, re-evaluated on 200,000): fronts span s = 0 to 0.51 (T), 0.47 (BOOT), 0.47
  (BAYES); the largest feasible E[G] sits at s = s*_m, as PR-6 implies. Grid check: 2 / 3 / 17 of 120 front points are
  dominated by a coarse grid point (NSGA-II is close but not exact; no decision rests on it).
- Narrower range at s = 1/2, h = h*: putting l = 50% of the stretch into the low end halves the width (about $16,500)
  at P(G < L) of 0.01-0.26%; l = 90% gives a $6,300-wide range at 4.4-6.5% disappointment.

### M8: which assumptions move the 2031 range

- Inputs from data: X4 (95-day change of the 10-year, n = 9,123) 2.5% / 97.5% = -93 / +92 bp; X5 (365-day change of the
  5-year, n = 8,940) = -1.95 / +2.27 points. A fall of more than the 26.2 bp headroom happened in 30.5% of windows.
- Tornado (median 2031 top; base $174,950): X4 curve shift $143,309 to $194,187 (swing $50,878); X5 5-year yield in
  2027 $167,901 to $182,227 ($14,325); X6 fee $174,950 to $166,586 ($8,364); X1 return $172,963 to $175,656 ($2,694);
  X2, X3, X7 about $0. Reference bars: s = 1/3 vs 2/3 $166,633 to $183,267; return-model choice $174,966 to $175,472.
- Sobol B (assumptions only, ST for the median top): **X4 0.898, X5 0.067, X6 0.033**, X1 0.003, X2 and X3 0.000.
  For the 5th percentile: X4 0.917, X5 0.045, X6 0.030, X2 0.009.
- **The three assumptions the IPS must state (pre-registered rule): X4 the Treasury curve on 1 Jan 2027 (the ladder's
  cost against $300,000), X5 the 5-year yield on 2 Jan 2028 (the floor's cost), X6 yearly costs.** The p5 ranking and
  the tornado give the same three. The stock-return assumptions (X1-X3) barely move the 2031 top because the fund is
  about 9% of the plan and the top counts only half of it.
- Sobol A (luck included, first-order shares): the 2031 top is 79% assumptions (X4 alone ST 0.73) and 17% market luck;
  the 2033 gift 77% assumptions and 18% luck (five years of luck ST 0.06-0.07 each).
- Floor reading (`out/M8/floor_reading.csv`): at d = -50 bp the IPS reading gives F $142,612 and B0 $28,501, the E6
  reading F $150,000 and B0 $22,590; at -100 bp: IPS $126,560 / $22,836 vs E6 $150,000 / $3,626 (insight_v1 H13 said
  "$1-7k" for -100 bp under E6). This is flag F4 in `rab/inventory.md`, unchanged: which reading the IPS means decides
  whether a 2027 yield fall cuts the floor or the stock fund.

## Gate B comparison (for WS0; this builder did not open the primary's results)

**Done (30 Sep, WS2 Gate B reconciler): PASS, 0 UNRECONCILED; see `rab/gates/gate_B_ws2.md`.**

`out/BLIND_HEADLINES.md` lists 307 keys with the tolerance from the spec beside each: M3 range ends and gift
percentiles 2%, probabilities 2 points, BAYES posterior means 10%; M4 s* 0.02, h* and A identical; M8 base exact,
tornado medians 1%, Sobol ST 0.05 or the 95% interval, top-3 identical. Monte Carlo noise alone at N = 200,000 is
about 0.05% on medians and 0.1 point on probabilities, so any gap beyond that is a method difference to explain.

## Contradiction triage (RUN_PLAN s0; nothing applied)

- Nothing here contradicts the adopted strategy or the IPS. PR-7 keeps s = 1/2.
- Note-in-Final-Report: (1) the IPS should state the three assumptions above, the curve on 1 Jan 2027 first; (2) with
  an iBond floor the gift is "at the top" in the fund sense (B5 >= B3) about 75% of the time but equals the face-based
  top U in only about 25% of paths, because phi < 1 (M4 A1): the wording "capped at the top" should say the top is
  floor face + half the fund and the floor pays what its holding delivers; (3) the announced low end $145,000
  (h* = 2.5%) keeps P(G < low end) at 0 in every model.
- Fix-before-6-Nov: none new from this stream.

## Limits

Model prices and returns, one curve, nominal dollars. The stationary bootstrap re-centres history to the JPM 7.00%
median; BOOT-raw shows what US history's own mean would give. BAYES learns the shape from 155 US years and takes the
centre from published forecasts; BAYES-hist shows the alternative. M8's model of the fund uses the IPS reading of the
2028 deposit (floor repays the whole remainder); the E6 reading is in `floor_reading.csv`. Fees in M8 are taken from
the fund at the start of each year on all assets (the IPS cost principle); M3 and M4 have no fees (M8 varies them).

## Second session: end-to-end rerun and commit (30 Sep 2026, Sydney, about 09:00)

- Why: the first session built and ran everything but its final `run_all.sh` rerun was cut off inside M4's Pareto
  stage (`pareto_BOOT.csv` was being written at 02:56:41; the M4 and run_all logs ended at "Pareto T"), and nothing
  had been committed. The files on disk were from the complete 02:43-02:53 run.
- This session re-read the three specs, `M1_METHOD.md` (sections 1, 2, A), `numbers.yaml` (hash equals
  `rab/numbers.lock`, 492ed320...) and `rab/data/`, reviewed every script line by line against its spec, then re-ran
  `./run_all.sh` end to end. `out/determinism_before.txt` and `out/determinism_after.txt` hold the md5 of every CSV,
  JSON, YAML and Markdown output before and after the rerun: 26 of 29 files byte-identical (every CSV, YAML and Markdown table); the three `headline_*.json` files differ only in their `elapsed_s` and `log` fields (run timings), and `BLIND_HEADLINES.md`, which lists all 307 values taken from those JSONs, is identical. Timings this run: M3 6 s, M4 97 s, M8 116 s, about 4 minutes in all.
- Disclosure, as in the first session: the `STATUS.md` tail (the WS2 primary's one-line summary, plus WS3, WS4-blind
  and WS6 lines) was on screen before any work here. No file under `rab/results/`, no model card, no D6 memo and no
  `rab/models/*.py` was opened in either session.
- M4_SPEC section 9 lists the primary's post-run additions A1-A4 (none used by a decision). Built here: A1
  (`P_top_fund` in `s_profile.csv`) and A3 (the brute-force grid check). Not built: A2 (the `U_A = A + s B3` variant)
  and A4 (`fig_M4_narrower.png`); `narrower_range.csv` carries the same numbers as a table.
- Figures were re-inspected after the rerun (Okabe-Ito palette, direct labels, no clipped or overlapping text).
