# Gate B, WS4 (M2 rate paths): reference build vs blind rebuild

WS4 Gate B reconciler, 30 Sep 2026 (Sydney). AI-generated verification record (Claude Code) for Team Caplet. MODEL
outputs, not deliverable text. The strategy is not reopened (RUN_PLAN s0). Nothing was executed externally, and
`rab/numbers.yaml` is untouched (sha256 `492ed320...`, Gate A lock).

**Verdict: PASS.** Every headline key reconciles and none is UNRECONCILED:
- The decision-relevant keys agree to 0.005pp (probabilities) and $0.00 (deterministic dollars).
- The only differences above Monte Carlo noise are on cross-check rows (at most 0.43pp), and each has a named cause.
- No bug was found in the reference build's numbers.
- Four spec ambiguities and one spec erratum are now written into the `M2_SPEC.md` changelog.
- One bug in the blind build (`--curve-date`) and one wording error in `M2_CARD.md` are fixed.

**In plain English.** "About 1 in 3" (32.7%, MODEL, 28 Sep curve) holds up. Two separately written programs get the
same answer, and a noise-free recomputation gets 32.6%. The chance is that the ten dated holdings cost more than the
$300,000 deposit on 1 Jan 2027.

## 1. What was compared

- **Reference build:** `rab/models/m2_rate_paths.py` (commit 5cb00be; spec 88e7f4a written before any estimator ran),
  with outputs in `rab/results/M2/`.
- **Blind build:** `rab/verification/blind/m2_blind.py` (commit 9d1545c), built from `M2_SPEC.md` and the raw inputs
  only. Its README declares one leak: it saw the reference build's STATUS line before coding.
- **Evidence the builds are independent:**
  - The code differs throughout: pandas loaders against csv, a curve class against functions, bisection against
    Newton, a per-replicate bootstrap loop, and an eigendecomposition sampler.
  - At all four points where the spec was ambiguous, the blind build chose differently from the reference build (see
    s3). A builder steering towards known answers would not do that.
  - E3 and E5 give identical draws in both builds. That is expected, because the spec fixes their seeds and draw order,
    so their precision was checked separately (s4).
- **Reruns today:** both builds reproduce their committed outputs. The CSVs are byte-identical, and the JSON is
  identical apart from time stamps.
- **Check script:** `rab/verification/gateB_ws4/gateB_ws4_checks.py`. It writes `gateB_ws4_results.json` and a
  93-row table, `gateB_ws4_table.csv` / `.md`.

## 2. Key-by-key table (every headline key of the reference build)

(D) marks a decision-relevant key. Tolerances: probabilities +-2pp; dollar outcomes +-2% and the spec's $500;
deterministic figures $1; Vasicek theta 5bp. The blind build's 14 headline keys are all in this table or in the
93-row file.

| Key | Primary | Blind | Diff | Verdict |
|---|---|---|---|---|
| `laura.rates.gap_odds_2027` (D) | 32.66% | 32.66% | 0.00pp | MATCH |
| `gap_odds_range_min` (E2) (D) | 26.67% (90% range 21.6-33.2%) | 26.67% (21.8-32.7%) | 0.00pp (range ends +0.28 / -0.43pp) | MATCH (range ends: bootstrap seeding, s3 #2) |
| `gap_odds_range_max` (E1) (D) | 33.16% (29.8-36.7%) | 33.16% (29.8-36.7%) | 0.00pp | MATCH |
| `E3_vasicek_1962` (D) | 32.69% | 32.69% | 0.00pp | MATCH |
| `E4_pca_var_1990` (D) | 32.21% (no mean reversion 30.89%) | 32.20% (31.02%) | -0.005pp (+0.14pp) | WITHIN TOL: Monte Carlo noise, s3 #1 |
| `E5_move_calibrated` (D) | 32.66% (MOVE 63-day average 27.43%) | 32.66% (27.43%) | 0.00pp | MATCH |
| `cost_2027_yields_unchanged` (D) | $293,401.14 | $293,401.14 | $0.00 | MATCH |
| Cost_FWD(R), numbers.yaml $292,418.11 (D) | $292,418.11 | $292,418.11 | $0.00 | MATCH |
| `breakeven_fall_bp_yields_unchanged` (D) | 22.78bp (FWD 26.20bp) | 22.78bp (26.20bp) | <0.0001bp | MATCH |
| `recon_R1_insight_v1_25sep` | 30.52% | 30.23% spec reading / 30.52% same convention | -0.29pp / 0.00pp | WITHIN TOL: valuation date, s3 #3 |
| `recon_R2_D1_28sep` | 24.21% | 23.84% / 24.21% | -0.37pp / 0.00pp | WITHIN TOL: s3 #3 |
| `recon_R5_no_view_centre_2026_vol` | 27.16% | 26.83% / 27.16% | -0.34pp / 0.00pp | WITHIN TOL: s3 #3 |
| `recon_AX1b_26bp_since1962` (1990, 2000) | 27.55% (31.06, 28.54) | 27.83% (31.37, 28.85) | +0.28pp (+0.31, +0.30) | WITHIN TOL: float ties, s3 #4 |
| `m2_on_25sep_curve` | 37.90% | 37.90% (rerun here) | 0.00pp | MATCH |
| `gap_if_any_typical` (D) | $10,010 (p95 $18,213) | $10,010 ($18,213) | $0 | MATCH |
| `P_whole_payment_waits_max` (D) | 0.27% | 0.27% | 0.00pp | MATCH |
| `stock_fund_2028_median` (H-LVL) (D) | $40,968 (FHS $37,908, RAW $41,366; FWD base $40,736.19) | same, all four | $0 | MATCH |
| `P_stock_fund_below_20k_2028` (D) | 16.84% (variants 12.3-20.0%) | 16.84% (12.3-20.0%) | 0.00pp | MATCH |
| `H13_fund_minus100bp_low` (D) | $3,625.72 (all six H13 funds and both floor faces) | $3,625.72 (same) | $0.00 | MATCH |
| `H14_unfunded_2033_minus50bp` (D) | $9,281.45 (-100bp $28,752.60) | $9,281.45 ($28,752.60) | $0.00 | MATCH |
| `vasicek_theta_1962_vs_2000` | 6.190% (1990+ 3.905, 2000+ 3.295; ADF p 0.42) | same | 0.00bp | MATCH |
| `ewma_vol_today` | 81.2bp/yr (1962-2026 101.1; sigma_h 50.77bp) | same | 0.0 | MATCH |

Tally: 17 MATCH and 5 WITHIN TOL with a named cause (the Cost_FWD anchor row is counted with the headline keys).
The full 93 rows give 76 MATCH, 17 WITHIN TOL and 0 UNRECONCILED. They also cover every E1-E5 detail, the 25 Sep
per-estimator runs, the 2028 p5 figures and P(no fund) / P(top-up), and all H13 top-ups.

## 3. Every difference, its cause and what was done

1. **E4 and its dollar rows.** The gaps are 32.21% vs 32.20%; 30.89% vs 31.02% without mean reversion; mean gap
   $8,802 vs $8,771; cost p50 $294,051 vs $293,959.
   - Cause: Monte Carlo noise. The two builds draw normals differently (numpy SVD vs eigendecomposition).
   - Check: with 4,000,000 draws per sampler the two give 32.30% and 32.31%. Both 100,000-draw runs sit 0.1pp lower,
     within one standard error (0.15pp).
   - Class: ignore. No fix.
2. **E2's 90% bootstrap range** (21.6-33.2% vs 21.8-32.7%).
   - Cause: how the random generator is seeded. The reference build creates `[20260930, 9]` afresh for each estimator.
     The blind build carries one generator from E1 into E2, which is why the E1 ranges are identical.
   - Check: over 50 seeds the ends run 21.0-21.9% and 32.1-33.5%, so both builds sit inside the noise.
   - Class: spec ambiguity, now clarified. Quote the range as "about 22-33%".
3. **R1 / R2 / R5.** The blind build's spec reading gives 30.2 / 23.8 / 26.8%; the reference build gives
   30.5 / 24.2 / 27.2%.
   - Cause: which date each 2026 curve is valued on. insight_v1 values each 2026 row on that row's own date
     (`D1_purchase_rule.py` line 68, `v = row["_date"]`), and so does the reference build. The blind build's same-date
     variant matches it to 0.00pp.
   - The reference build is right: it reproduces what insight_v1 actually computed.
   - Class: spec ambiguity, now clarified.
4. **R4, the AX1b history check.** The reference build gives 27.55 / 31.06 / 28.54%; the blind build's inclusive
   count gives 27.83 / 31.37 / 28.85%.
   - Cause: floating-point ties. AX1b tests `cc <= -x / 100` on raw floats (line 100). Since 1962, 74 windows fell by
     exactly 26bp, and float arithmetic counts only 29 of them.
   - The reference build follows AX1b's convention and reproduces the printed 27.6 / 31.1 / 28.5%. A fully inclusive
     count is 0.3pp higher.
   - Class: ignore. It is a cross-check row, not a decision input. The spec is clarified.
5. **The blind build's `--curve-date` option failed for any date except 28 Sep.** Two numbers.yaml asserts ran on
   every date.
   - Class: bug in the blind build. Fixed: the asserts now run only on the Gate A curve.
   - Check: the 28 Sep rerun is identical, so both builds can be rerun on Friday.
6. **Spec erratum.** The 4 Jan sensitivity should use n_h = 64, not 65, because 1 Jan 2027 is a bond-market holiday.
   - Effect: E5 in closed form gives 33.0% (64 days) vs 33.1% (65 days).
   - Class: ignore (sensitivity only). Noted in the spec.
7. **Card wording.** `M2_CARD.md` said "34% vs 33%", which compared E1 on 4 Jan with the five-method median on 1 Jan.
   Like for like, E1 is 33.7% vs 33.2% and the blind build's median is 33.1% vs 32.7%. Fixed.

## 4. Monte Carlo precision: is 32.7% really 32.7%?

| Estimator | 100,000-draw run | Without noise |
|---|---|---|
| E5 | 32.66% | 32.69% (closed form) |
| E3 | 32.69% | 32.55% (averaged exactly over 2,000,000 parameter draws) |
| E4 | 32.21% | 32.31% (8,000,000 draws) |
| E1, E2 | 33.16%, 26.67% | no draws involved |

- The median with the noise removed is 32.55%.
- Leaving any one estimator out, the median is 32.43-32.68%.
- The headline's noise is therefore about +-0.15pp, and "about 1 in 3" holds under every version.
- Quote it as "about 1 in 3" (or "about 33%"), never to a decimal.

## 5. Reconciliation with insight_v1 (`rab/inventory.md` s2)

| Ref | insight_v1 figure | Rebuilt here | Why the M2 answer differs |
|---|---|---|---|
| H5 (25 Sep, "about 1 in 3") | D1 [6] 30.5%<br>S4 30.7%<br>strategy_mc_v2 30.2% / 34.4%<br>AX1b 19bp: 31.8 / 36.1 / 34.0% | 30.52%<br>30.73%<br>30.09% (analytic) / 34.37%<br>31.80 / 36.11 / 34.04% | On the same 25 Sep curve, M2 gives 37.9% in both builds. Two reasons: yields-unchanged pricing ($295,432, 15.7bp of room against 19.3bp) and today's higher volatility |
| H6 (28 Sep) | 24.2% Nov-15<br>18.7% exact dates<br>history 27.6 / 31.1% | 24.21%<br>18.70% (recomputed with the blind build's curve code)<br>27.55 / 31.06% | 24.2% becomes 27.2% (+3.0pp, yields-unchanged pricing), then 32.7% (+5.5pp, the five methods' volatility and curve shape) |
| H7 (2026 days over $300k) | 173/185 exact, 176/185 Nov-15; worst 27 Feb, $327,631 | Identical to 25 Sep. To 28 Sep: 173/186 and 176/186. The last Nov-15 day over $300k was 22 Sep | Not an M2 output. Context: the ladder cost more than $300k on almost every 2026 trading day up to 22 Sep |
| H13 (E6 [8], 25 Sep) | -50bp: fund $20-23k<br>-100bp: fund $1-7k<br>-150bp: no fund; floor $127-137k | Both builds on 25 Sep: top-ups $9,555 / $25,711 / $42,633 (the figures E6 hard-codes)<br>funds $19,962-22,804 / $881-6,648 / none<br>floor $127,395-136,900 | On 28 Sep: $22,590-25,419 / $3,626-9,366 / none; floor $130,724-140,469. Yields rose, so the top-ups are smaller and the floor is cheaper |
| H14 | 25 Sep: $11,957 / $31,413<br>28 Sep: $9,281 / $28,753 | Exact on both dates, both builds | - |

**What this changes.** Inventory F2 and row H6 said the model odds "fell to about 1 in 4" by 28 Sep. That came from
assuming forward rates come true and using 2026's calm volatility. With no view on direction and today's volatility,
the odds are still about 1 in 3. The line survives, but for new reasons.

## 6. Triage (contradiction rule: strategy unchanged, nothing applied to the IPS or the Sheet)

**Fix before 6 Nov (RAB files only):**
- WS1: add the six proposed entries in `rab/results/M2/m2_proposed_numbers.yaml` to numbers.yaml; they are now
  Gate B reconciled. Record a changelog line and a new lock. Retire `ref.H5` and mark `ref.H6` "reproduced, not quoted".
- WS0: `rab/assumptions.md` C2 and `rab/premortem.md` PM-32 still give 24.2% as the model figure. Replace it with
  `laura.rates.gap_odds_2027`.
- Friday: rerun both builds with `--curve-date` and then this check. MOVE was 106.29 on 29 Sep (Yahoo ^MOVE,
  `rab/data/m2/MOVE_yahoo_daily.csv`), against 101.82 on 28 Sep, so E5 may move. Do not quote the odds before the
  rerun.

**Note in the Final Report:**
- "About 1 in 3 (MODEL, 28 Sep curve, no view on the direction of rates; five methods give 27-33%)". State the basis:
  Nov-15 STRIPS, MODEL prices, one purchase day. Never put it in a WInS note.
- The 1 Jan 2027 cost has two versions: $292,418 if forward rates come true (26.2bp of room, numbers.yaml) and
  $293,401 if yields stay unchanged (22.8bp).
- The 1 in 3 now rests on different reasons from insight_v1's (s5).

**Ignore:** E4 sampler noise, bootstrap seeding, AX1b float ties, and the 4 Jan n_h erratum.

## 7. What Gate B cannot catch

Both builds follow the same spec, so the assumptions they share are not tested by the blind rebuild:
- MODEL STRIPS prices with no dealer mark-up (a mark-up raises the odds).
- A single purchase day.
- History as the guide to the future.
- MOVE taken from Yahoo, a secondary source.
- E4's mean reversion is not bias-corrected.
- No odds are computed for a ladder built from WInS-listed instruments.

These are the reference card's stated limits. WS7 should challenge them.

## 8. Files and rerun

- **Record:** this file.
- **Checks:** `rab/verification/gateB_ws4/gateB_ws4_checks.py`, which writes `gateB_ws4_results.json`,
  `gateB_ws4_table.csv` and `gateB_ws4_table.md`.
- **Changed at this gate:**
  - `rab/models/M2_SPEC.md` (changelog)
  - `rab/models/M2_CARD.md` (s3 #7 and a Gate B line)
  - `rab/verification/blind/m2_blind.py` (s3 #5)
  - `rab/verification/blind/README.md` (s8)
- **Rerun** from the worktree root (about 25 s, seed 20260930; it reruns both builds on 25 Sep in a temporary folder):
  `/Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws4/gateB_ws4_checks.py`
