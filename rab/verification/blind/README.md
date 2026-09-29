# Blind rebuilds (Gate B)

This folder holds two independent blind rebuilds, one per stream, merged into `rab/integration` on 2026-09-30:

- **WS4, M2 (rate paths):** `m2_blind.py`, `results.json`, `run.log`, `deterministic_check.py/.json`. README: section A.
- **WS3, M5/M6/M7 (history, rivals, stress):** `blind_*.py`, `collect_headlines.py`, `run_all.sh`, `BLIND_REPORT.md`,
  `out/`. README: section B.

The two builds share no code and no files; this index was added when the two READMEs met at the same path.

---

## A. Blind rebuild of M2 (rate paths to Jan 2027 / Jan 2028)

WS4 blind builder, 2026-09-30 (Sydney). AI-generated verification work (Claude Code) for Team Caplet; no deliverable
text. Gate B evidence: M2 rebuilt from `rab/models/M2_SPEC.md` alone, with no code shared with the reference build.

**Read to build this:** `rab/models/M2_SPEC.md`; the raw inputs under `rab/data/` (Treasury par curves 1990-2026, FRED
DGS series, `m2/MOVE_yahoo_daily.csv`); `rab/numbers.yaml` (Gate A lock, cross-checks only); and the two insight_v1
data CSVs the spec names as I5 (`research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv`, `fred_DGS10.csv`).
**Not read:** any `.py` under `rab/models/` or `rab/results/`, `M2_CARD.md`, `M1_METHOD.md`, any insight_v1 script,
any M2 result file. **One leak to declare:** the task told me to append to `/Users/ray/Research/rab-ws/STATUS.md`, and
its tail carried the primary's M2 milestone line (headline 32.7%, range 26.7-33.2%, yields-unchanged cost $293,401,
"<$20k in ~1 in 6"). I saw it before coding. Nothing in `m2_blind.py` uses those figures; every number below comes
from the spec's recipe and the raw inputs, and the run log shows them appearing in the order the code computes them.

Files: `m2_blind.py` (the whole model, one file), `results.json` (every output), `run.log` (console of the full run).
Run: `/Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind/m2_blind.py` (3 s; `--quick` for a smoke test;
`--curve-date` for Friday's curve). Seed 20260930; numpy 2.5.3, pandas 3.0.6, scipy 1.18.1, statsmodels 0.15.0.

## 1. Headline keys (28 Sep 2026 curve, purchase 1 Jan 2027, Nov-15 STRIPS basis, MODEL, laura_plan)

| Key | Blind value | Spec / Gate A reference | Note |
|---|---|---|---|
| **P(ladder costs > $300,000 on 1 Jan 2027)**, median of E1-E5 | **32.66%** = "about 1 in 3" | pre-registered rule s5 | median is E5 |
| Range (min-max of E1-E5) | 26.67% - 33.16% | | E2 low, E1 high |
| E1 history rescaled to today's volatility (1962+) | 33.16% (90% block-bootstrap CI 29.8-36.7%) | | 15,855 windows, 247 non-overlapping |
| E2 history at similar yield levels (10Y 4.00-6.50%) | 26.67% (CI 21.9-32.7%) | | 5,661 windows, 88 non-overlapping |
| E3 Vasicek / AR(1) on the ladder yield, parameter uncertainty | 32.69% | | plug-in: 31.65% (hat), 32.73% (bias-corrected) |
| E4 3-factor PCA + VAR(1), 1990+ | 32.20% | | random-walk variant 31.02% |
| E5 MOVE, calibrated to the ladder | 32.66% | | analytic 32.69%; sigma_h = 50.8bp |
| Cost_FWD(R) (forward rates come true) | $292,418.11 | $292,418.11 (`laura.ladder.cost_2027_strips`) | diff $0.00 |
| Cost_RW(R) (yields unchanged on 1 Jan 2027) | $293,401.14 | new | headroom $6,599 |
| Break-even parallel fall, FWD | 26.20bp | 26.2bp (`laura.ladder.breakeven_fall_bp_strips`) | diff 0.004bp |
| Break-even parallel fall, RW | 22.78bp | new | |
| PV of the ten payments on 28 Sep | $289,119.20 | $289,119.20 (Gate A) | information |
| Ladder yield y(D); d y / d b at R | 5.3289%; 1.0075 | expected ~1 | |
| EWMA sigma_D | 5.12 bp/day = 81.2 bp/yr | | 2026 realised sd 4.45 bp/day |
| Vasicek theta / kappa_bc / half-life_bc (1962+) | 6.19% / 0.0007 per yr / 966 yr | tolerance 5bp / 0.02 | phi_bc = 0.999997 |
| PCA variance shares (1990+) | 78.26% / 12.36% / 5.05% | tolerance 0.5pt | |
| MOVE rho (median RV / MOVE) | 0.9895 (quartiles 0.866-1.137) | | MOVE_D = 101.82 |
| 2028 stock fund S, H-FHS p5 / p50 / p95 | $1,410 / $37,908 / $77,268 | | P(S < $20k) 20.0%, P(S = 0) 4.2%, P(top-up) 33.4% |
| 2028 stock fund S, H-LVL p5 / p50 / p95 | $10,339 / $40,968 / $64,356 | | P(S < $20k) 12.3%, P(S = 0) 0.8% |
| 2028 stock fund S, H-RAW p5 / p50 / p95 | $1,596 / $41,366 / $70,945 | | P(S < $20k) 16.8% ("about 1 in 6"), P(S = 0) 4.5% |
| 2028 base check, FWD step 1: S / F | $40,736 / $117,194 | $40,736 / $117,194 (numbers.yaml) | diff $0.19 / -$0.30 |
| 2028 base, RW step 1: S | $39,708 | new | leftover $6,599 grown at 4.59% |
| H14 unfunded 2033 at -50 / -100bp | $9,281 / $28,753 | $9,281 / $28,753 | reproduced |
| H13 fund at -50bp (5Y unchanged / shifted) | $25,419 / $22,590 | insight_v1 25 Sep: $20-23k | 28 Sep has more headroom |
| H13 fund at -100bp | $9,366 / $3,626 | $1-7k | |
| H13 at -150bp: fund; floor face | $0; $140,469 / $130,724 | no fund; floor $127-137k | |
| Sensitivity: purchase Mon 4 Jan 2027 (n_h = 65) | median 33.08% | | E1-E5: 33.7 / 27.2 / 33.2 / 32.7 / 33.1% |

Quote for the team: "There is about a 1-in-3 chance that yields fall enough before 1 January 2027 that the ten dated
holdings cost more than the $300,000 deposit (five methods give 27-33%). If that happens the shortfall is usually
small: the average overshoot is about $8,000-$10,500 and it exceeds $10,000 in about one case in eight." (MODEL,
28 Sep curve, no view on the direction of rates.)

## 2. Reconciliation with insight_v1 (spec s7): every row rebuilt, not copied

| Row | Must reproduce | Blind, spec reading | Blind, variant | Verdict |
|---|---|---|---|---|
| R1 D1 lognormal, 25 Sep curve | 30.5% | 30.23% (sigma 7.04%) | **30.52%** with the valuation date moving with each row (sigma 7.16%) | reproduced; the printed figure carried each day's curve from its own date |
| R2 same on 28 Sep | 24.2% | 23.84% (sigma 7.06%) | **24.21%** moving valuation (sigma 7.17%) | reproduced, same convention |
| R3 strategy_mc_v2 (a) parallel N(0, 37bp), FWD, 25 Sep | 30.2% (analytic 30.1%) | 30.09% | 28 Sep: 23.95% | reproduced; 25 Sep FWD break-even 19.31bp |
| R4 AX1b: DGS10 fell >= 26bp in 68 trading days, since 1962 / 1990 / 2000 | 27.6 / 31.1 / 28.5% | 27.83 / 31.37 / 28.85% (<=) | 27.37 / 30.84 / 28.27% (strict <) | within 0.35pp under every convention tried (66-70 days, start- or end-date filter); exact convention not recoverable from the spec |
| R5 R2 with the no-view (RW) centre | new | 26.83% | 27.16% moving-valuation sigma | |
| R6 headline | new | 32.66% | | |

Waterfall (spec reading / moving-valuation): "1 in 3" R1 30.2% / 30.5% -> R2 curve to 28 Sep 23.8% / 24.2% -> R5
no-view centre 26.8% / 27.2% -> R6 five estimators 32.7%. Reading: moving the curve three days bought 7bp of headroom
(-6pp); pricing "yields unchanged" instead of "forward rates come true" costs $983 of it back (+3pp); letting the
five methods set the volatility (today's EWMA and MOVE both say ~50bp over the horizon, above 2026's average of
~7% of cost, i.e. ~36bp) adds the rest (+5pp). The 25 Sep "1 in 3" and the 28 Sep "1 in 3" agree by coincidence of
two offsetting changes, not because nothing moved.

## 3. Per-estimator outputs (spec s6), RW convention

| | E1 | E2 | E3 | E4 | E5 |
|---|---|---|---|---|---|
| P(Gap > 0) | 33.16% | 26.67% | 32.69% | 32.20% | 32.66% |
| P(Gap > $5k) | 22.42% | 17.26% | 21.79% | 20.12% | 21.74% |
| P(Gap > $10k) | 13.91% | 7.83% | 13.49% | 11.30% | 13.37% |
| P(Gap > 2033 rung, ~$37k) | 0.27% | 0.04% | 0.14% | 0.04% | 0.14% |
| Mean gap given gap > 0 | $10,525 | $8,006 | $10,128 | $8,771 | $10,010 |
| Gap p90 / p95 / p99 | $13,191 / 19,331 / 32,008 | $8,822 / 12,575 / 20,576 | $12,779 / 18,572 / 29,537 | $10,982 / 15,955 / 25,609 | $12,632 / 18,213 / 29,357 |
| Cost p5 / p50 / p95 | $267,455 / 293,859 / 319,331 | $276,556 / 292,870 / 312,575 | $270,392 / 293,317 / 318,572 | $273,609 / 293,959 / 315,955 | $270,473 / 293,274 / 318,213 |
| Scenarios | 15,855 (247 non-overlapping) | 5,661 (88) | 100,000 | 100,000 | 100,000 |
| P(Gap > 0), FWD convention | 30.81% | 24.89% | - | - | 30.27% |
| Parallel-equivalent shift: mean / sd / robust sd (bp) | -0.2 / 55.8 / 47.7 | -0.1 / 39.0 / 37.6 | 0.1 / 51.0 / 50.9 | -1.9 / 44.9 / 44.9 | 0.3 / 50.8 / 51.0 |

E3 fits (AutoReg lags=1, trend c): 1962+ n = 16,169, phi_hat 0.999750, theta 6.19%, s_e 6.37bp/step (101bp/yr),
phi_bc 0.999997, ADF p = 0.42, 49.4% of parameter draws at or above phi = 1 (random walk). 1990+: theta 3.91%,
kappa_bc 0.048/yr (half-life 14.3y), plug-in 35.3% (hat) / 32.5% (bc), ADF p = 0.19. 2000+: theta 3.29%, kappa_bc
0.176/yr (half-life 3.9y), plug-in 44.2% / 38.1%, ADF p = 0.16. (The sub-panels pull the mean down toward 3-4%,
which raises P: a view, so not headline.)

E4: 9,192 daily curves 1990+; VAR(1) companion eigenvalues 0.9946, 0.9990, 0.9990; 64-step forecast implies a mean
10Y shift of -2.3bp; forecast sd of the three scores 1.22 / 0.48 / 0.25.

E5: 5,908 windows with MOVE (Nov 2002+); RV on MOVE regression RV = 24.3 + 0.721 MOVE (bp), giving 97.7bp at
MOVE_D (P 32.1%); 63-day mean MOVE 76.4 gives sigma_h 38.1bp (P 27.4%); rho = 1: 32.8%; rho quartiles: 30.4-34.7%.

History sub-samples (sensitivity): raw 1962+ 29.5%; 1990+ raw 33.3% / demeaned 31.2% / rescaled 30.5%; 2000+ raw
30.8% / demeaned 29.5% / rescaled 28.9%; 2022+ raw 18.2% (yields rose) / demeaned 30.7% / rescaled 27.8%;
similar-level raw (not demeaned) 25.7%; similar-level rescaled and demeaned 34.6%.

## 4. Fifteen-month section (spec s8), 15,605 windows 1963-2025 (5,416 in the level band)

| Variant | S p5 / p50 / p95 | P(S < $20k) | P(S = 0) | P(top-up) | mean top-up given one | F p5 / p50 / p95 |
|---|---|---|---|---|---|---|
| H-FHS | $1,410 / 37,908 / 77,268 | 20.0% | 4.2% | 33.4% | $11,155 | $100,454 / 118,630 / 131,950 |
| H-LVL | $10,339 / 40,968 / 64,356 | 12.3% | 0.8% | 27.2% | $8,423 | $107,689 / 116,624 / 129,691 |
| H-RAW | $1,596 / 41,366 / 70,945 | 16.8% | 4.5% | 29.8% | $13,431 | $105,020 / 116,749 / 131,805 |

Floor face is $150,000 in every window except the P(S = 0) share, where the whole 2028 deposit goes to the floor and
the face falls short (H-FHS: p5 of the face is still $150,000).

## 5. Interpretation choices a reconciler should know (none changes a headline by more than MC noise)

1. **P(Gap > 2033 rung)** uses each scenario's own 2033 rung cost (at R it is $37,166).
2. **E3 draw order:** the 100,000 (c, phi) pairs first, then the 100,000 standard normals, one rng seeded [20260930, 3].
3. **E4 / E4-RW sampling** uses an eigendecomposition sampler (the residual covariance is rank 7, so
   `multivariate_normal` would warn); scores first, then residual changes, from one rng per variant.
4. **R1/R2**: the spec's Cost_FWD(c) fixes the valuation date at D; the variant that reproduces insight_v1's printed
   figures carries each 2026 day's curve from its own date. Both reported; the spec reading is the row value.
5. **R4**: inclusive ("fell by at least X" = change <= -X bp), 68 rows of the non-missing DGS10 series, filter on the
   window start date. Strict and end-date variants are in `results.json`.
6. **4 Jan sensitivity**: n_h = 65 as the spec states (1 Jan 2027 is counted, only 2026 holidays are excluded).
7. **H13 leftover growth** (only matters if Gap < 0, which never happens at -50bp or beyond): grown at the shifted
   curve's own forward rate, the same factor as the top-up.
8. **E5 realised volatility** averages dy^2 over the e - k panel changes strictly after the start date up to the end.
9. Ladder yield solved by 120 bisection steps (error < 1e-20 in percent); Cost_FWD(R) matches Gate A to $0.002.
10. The pre-1990 FRED panel has 7,305 dates; 327 dates (mostly early FRED gaps) were dropped for missing 1Y/5Y/10Y;
    FRED DGS10 and the Treasury 10Y agree exactly on all 9,190 common dates.

## 6. Contradiction triage (RUN_PLAN s0): nothing here reopens the strategy

- **Note in Final Report:** the "yields unchanged" cost on 1 Jan 2027 is $293,401 (22.8bp of room), not the $292,418
  (26.2bp) that assumes forward rates come true. Both are MODEL; the difference is $983 and 3.4bp. The IPS may say
  "about $292,000-$293,000" and "yields would have to fall about a quarter of a point".
- **Note in Final Report:** a 1-in-3 chance of a small shortfall is the same odds insight_v1 quoted, but for
  different reasons (section 2). The fix is already in the plan: buy the longest rungs first and top up the rest from
  the 2028 deposit (needed in about 1 window in 3; average top-up $8-13k; stock fund still a median ~$38-41k).
- **Ignore:** nothing found that would change a ticket or the Friday sequence.

## 7. What WS0 should compare (Gate B tolerances, spec s9)

Probabilities within 2pp: headline, E1-E5, R1-R6, P(S < $20k), P(S = 0), P(top-up). Dollars within $500: Cost_RW(R),
the cost and gap quantiles, S and F quantiles, H13 fund and floor face. Exact to $1: Cost_FWD(R), break-evens,
H13/H14, the $40,736 / $117,194 base. Vasicek theta within 5bp (6.19%), kappa within 0.02 (0.0007 bc, 0.063 hat);
PCA shares within 0.5pt (78.3 / 12.4 / 5.1). A difference is explained, never averaged.

## 8. Gate B note (30 Sep 2026, WS4 reconciler)

`--curve-date` failed for any date other than 28 Sep, because two numbers.yaml cross-check asserts ran on every date.
They now run only on the Gate A curve (`gate_a_date`). No 28 Sep output changed: a rerun reproduces `results.json`
exactly apart from the run time stamp. The 25 Sep run (used for the insight_v1 reconciliation) gives 37.90%, the same as
the reference build. Reconciliation record: `rab/gates/gate_B_ws4.md`.

## 9. Re-run and third check (30 Sep 2026, later session of the WS4 blind builder)

A second session of this role was asked to "try again" (the first session's report did not reach the run
coordinator; its work above was already committed). This session did two things, neither of which changes a number:

1. **Reproducibility re-run.** `m2_blind.py` re-run from the committed tree (numpy 2.5.3, pandas 3.0.6,
   statsmodels 0.15.0) reproduces `results.json` byte-for-byte except `run_started_utc` and `runtime_s` (3.5s). Every
   line of `run.log` above is unchanged, so the headline stays 32.66% ("about 1 in 3"), range 26.67-33.16%.
2. **Third, standard-library-only pricer for the deterministic keys**: `deterministic_check.py` and its output
   `deterministic_check.json`. It was written from `M2_SPEC.md` s2-s3, s7 (H14) and s8 (2028 base, H13) plus the
   28 Sep row of the par-curve CSV, without reading `m2_blind.py` or any reference code, and uses only `math`, `csv`,
   `json`, `datetime` (no numpy, pandas, scipy or statsmodels), the way Gate A's tie-breaker did for M1. Results,
   28 Sep curve:

   | Key | Stdlib check | Compared with | Diff |
   |---|---|---|---|
   | Cost_FWD(R) | $292,418.11 | numbers.yaml $292,418.11; m2_blind | +$0.002; $0.000000 |
   | Cost_RW(R) | $293,401.14 | m2_blind | $0.000000 |
   | PV of the ten payments on 28 Sep | $289,119.20 | Gate A $289,119.20 | +$0.004 |
   | Break-even parallel fall, FWD / RW | 26.1963bp / 22.7756bp | numbers.yaml 26.2; m2_blind | -0.0037bp; 0.0000bp |
   | Ladder yield y(D); dy/db | 5.3289%; 1.0075 | m2_blind 5.3289%; 1.0075 | 0; 0 |
   | 2028 base S / F (FWD step 1); S (RW step 1) | $40,736.19 / $117,193.70; $39,708.05 | numbers.yaml $40,736 / $117,194; m2_blind | +$0.19 / -$0.30; $0.00 |
   | H14 unfunded 2033 at -50 / -100bp | $9,281.45 / $28,752.60 | spec $9,281 / $28,753; m2_blind | +$0.45 / -$0.40; $0.00 |
   | H13 funds (-50: 25,419 / 22,590; -100: 9,366 / 3,626) and -150bp floor faces (140,469 / 130,724) | as listed | m2_blind | $0.00 on all six |
   | E5 closed form 1 - Phi(b*_RW / sigma_h), sigma_h = 50.77bp read from `results.json` | 32.69% | m2_blind Monte Carlo 32.66% | +0.03pp (MC noise) |

   23 comparisons, 0 failures; exit code 0. On the 25 Sep curve (`--curve-date 2026-09-25`) it gives Cost_FWD
   $294,387.44 and a FWD break-even of 19.31bp, the same figures `results.json` holds for the insight_v1
   reconciliation rows R1 and R3. One defect was found and fixed in the check itself before commit: `dy/db` was first
   printed in percent per bp (0.0101) instead of bp per bp (1.0075).

   Run: `/Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind/deterministic_check.py [--curve-date D]`.
   The Monte Carlo and history-panel keys (E1-E4, E5's rho, the 2028 window variants, R1-R5) are not rebuilt here;
   they rest on the two builds reconciled in `rab/gates/gate_B_ws4.md`.

---

## B. WS3 blind rebuild of M5, M6, M7

Second, independent implementation of the three WS3 models for Gate B (RUN_PLAN s3: "each model rebuilt blind from
its spec"). AI-generated verification code (Claude Code, blind builder) for Team Caplet; no deliverable text.

## Protocol

- Read: `rab/models/M5_SPEC.md`, `M6_SPEC.md`, `M7_SPEC.md`; `rab/data/**` (curves, FRED, history snapshot, JPM
  tables, market inflation); the locked `rab/numbers.yaml` (sha256 492ed320..., unchanged).
- Not read: any `.py` under `rab/models/` or `rab/results/`, anything under `research/insight_v1/`, the primary's
  result files. The only leak was one-sentence headline lines in `rab-ws/STATUS.md` and the primary's commit message,
  seen while checking conventions; they were not used to write or tune code (`BLIND_REPORT.md`, Disclosure).
- Curve method (`blind_curve.py`) written from M5_SPEC section 2 alone; it reproduces the Gate A headline to the cent.

## Files

| File | What |
|---|---|
| `blind_curve.py` | Par-curve bootstrap (D1 method), dates and constants of the plan |
| `blind_m5.py` | Cost-of-certainty series 1871-2026 and the start-year backtest 1872-2020 |
| `blind_m6.py` | Rivals (REC, R1-R6) in the history and MC lenses; branch-fund alternatives and the switch rule |
| `blind_m7.py` | Stress scenarios S0-S7 with thresholds, and the real value of the payments |
| `collect_headlines.py` | Flattens the three `*_results.json` into `out/blind_headlines.json` and writes `BLIND_REPORT.md` |
| `run_all.sh` | Runs everything in order (about 15 s) |
| `out/M5`, `out/M6`, `out/M7` | The spec's named outputs (CSV, PNG, JSON, report and run log) |
| `BLIND_REPORT.md` | Headline numbers, checks and the readings chosen where the spec is ambiguous |

## Run

```
zsh rab/verification/blind/run_all.sh
```

Python: `/Users/ray/Research/rab-ws/.venv/bin/python` (numpy, pandas, scipy, matplotlib, pyyaml). Seeds: 20260930
(returns), 20260936 (inflation). Deterministic apart from the MC lens, whose tolerances are in M6_SPEC section 7.
