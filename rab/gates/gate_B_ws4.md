# Gate B, WS4 (M2 rate paths): reference build vs blind rebuild

WS4 Gate B reconciler, 30 Sep 2026 (Sydney). AI-generated verification record (Claude Code) for Team Caplet. MODEL
outputs, not deliverable text. The strategy is not reopened (RUN_PLAN s0). Nothing was executed externally, and
`rab/numbers.yaml` is untouched (sha256 `492ed320...`, Gate A lock, identical to `rab-kit/rab/numbers.yaml`).

**Verdict: PASS.** Every headline key of both builds reconciles and none is UNRECONCILED:
- The decision-relevant keys agree to 0.005pp (probabilities) and $0.00 (deterministic dollars).
- The only differences above Monte Carlo noise are on cross-check or sensitivity rows (at most 0.43pp), and each has a
  named cause.
- No bug was found in the reference build's numbers.
- Five spec ambiguities and one spec erratum are now written into the `M2_SPEC.md` changelog.
- One bug in the blind build (`--curve-date`) and one wording error in `M2_CARD.md` are fixed.

**Re-check, same day (second reconciler session).** The blind builder added a commit after this gate first passed
(97c3467: a standard-library third pricer and five new headline keys). This session:
- reran both builds and every check;
- compared the new keys, rerunning the reference code on a 4 Jan purchase to do so;
- compared the third pricer with the reference build, which the third pricer never saw.

All 93 original rows are unchanged to the byte. The table now has 115 rows (94 MATCH, 21 WITHIN TOL, 0 UNRECONCILED).
The third pricer agrees with the reference build on all 29 of its comparisons. The verdict stands.

**Third session, same day ("Continue").** Nothing in M2 had changed since the re-check. The only new WS4 commit
(e95e48b) adds the hedge memo and `rab/numbers_ws4.yaml`. This session:
- reran the check script: the 115-row table is byte-identical, still 0 UNRECONCILED;
- rebuilt the two insight_v1 figures in the inventory's M2 rows that s5 had not yet rebuilt (s5): the 25 Sep
  exact-date 24.3% and the 25 Sep "+3.4 points". Both reproduce;
- checked that every figure in `numbers_ws4.yaml` and the hedge memo rests on a reconciled row (s6b). All 17 do.

The verdict stands.

**In plain English.** "About 1 in 3" (32.7%, MODEL, 28 Sep curve) holds up. Two separately written programs get the
same answer, a noise-free recomputation gets 32.6%, and a third program with no maths libraries gets the same dollar
figures. The chance is that the ten dated holdings cost more than the $300,000 deposit on 1 Jan 2027.

## 1. What was compared

- **Reference build:** `rab/models/m2_rate_paths.py` (commit 5cb00be; spec 88e7f4a written before any estimator ran),
  with outputs in `rab/results/M2/`.
- **Blind build:** `rab/verification/blind/m2_blind.py` (commit 9d1545c), built from `M2_SPEC.md` and the raw inputs
  only. Its README declares one leak: it saw the reference build's STATUS line before coding.
- **Third pricer:** `rab/verification/blind/deterministic_check.py` (commit 97c3467). It uses the standard library
  only and covers the keys that need no simulation. Its author compared it with numbers.yaml and the blind build
  (23 checks, 0 failures). This gate compares it with the reference build (s4b).
- **Evidence the builds are independent:**
  - The code differs throughout: pandas loaders against csv, a curve class against functions, bisection against
    Newton, a per-replicate bootstrap loop, and an eigendecomposition sampler.
  - At all five points where the spec was ambiguous, the blind build chose differently from the reference build (see
    s3). A builder steering towards known answers would not do that.
  - E3 and E5 give identical draws in both builds. That is expected, because the spec fixes their seeds and draw order,
    so their precision was checked separately (s4).
- **Reruns today:** both builds reproduce their committed outputs. The CSVs are byte-identical, and the JSON is
  identical apart from time stamps.
- **Check script:** `rab/verification/gateB_ws4/gateB_ws4_checks.py`. It writes `gateB_ws4_results.json`, a 115-row
  table (`gateB_ws4_table.csv` / `.md`) and `gateB_ws4_third_pricer.md`.

## 2. Key-by-key table (every headline key of both builds)

(D) marks a decision-relevant key. Tolerances: probabilities +-2pp; dollar outcomes +-2% and the spec's $500;
deterministic figures $1; Vasicek theta 5bp. Each of the blind build's 21 reported keys is in this table, in the
115-row file, or in s4b.

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
| `pv_today_R_usd`, numbers.yaml $289,119.20 (D) | $289,119.20 | $289,119.20 | $0.00 | MATCH (new) |
| `breakeven_fall_bp_yields_unchanged` (D) | 22.78bp (FWD 26.20bp) | 22.78bp (26.20bp) | <0.0001bp | MATCH |
| `recon_R1_insight_v1_25sep` | 30.52% | 30.23% spec reading / 30.52% same convention | -0.29pp / 0.00pp | WITHIN TOL: valuation date, s3 #3 |
| `recon_R2_D1_28sep` | 24.21% | 23.84% / 24.21% | -0.37pp / 0.00pp | WITHIN TOL: s3 #3 |
| R3 strategy_mc_v2 (a), analytic, 25 / 28 Sep | 30.09% / 23.95% | 30.09% / 23.95% | 0.00pp | MATCH (new) |
| `recon_R5_no_view_centre_2026_vol` | 27.16% | 26.83% / 27.16% | -0.34pp / 0.00pp | WITHIN TOL: s3 #3 |
| `recon_AX1b_26bp_since1962` (1990, 2000) | 27.55% (31.06, 28.54) | 27.83% (31.37, 28.85) | +0.28pp (+0.31, +0.30) | WITHIN TOL: float ties, s3 #4 |
| `m2_on_25sep_curve` | 37.90% | 37.90% (rerun here) | 0.00pp | MATCH |
| `gap_if_any_typical` (D) | $10,010 (p95 $18,213) | $10,010 ($18,213) | $0 | MATCH (label, s3 #9) |
| `P_whole_payment_waits_max` (D) | 0.27% (2033 rung $37,166.35) | 0.27% ($37,166.35) | 0.00pp ($0.00) | MATCH |
| `stock_fund_2028_median` (H-LVL) (D) | $40,968 (FHS $37,908, RAW $41,366; FWD base $40,736.19) | same, all four | $0 | MATCH |
| `P_stock_fund_below_20k_2028` (D) | 16.84% (variants 12.3-20.0%; mean top-up $8,423-13,431) | same | 0.00pp ($0) | MATCH |
| `H13_fund_minus100bp_low` (D) | $3,625.72 (all six H13 funds and both floor faces) | $3,625.72 (same) | $0.00 | MATCH |
| `H14_unfunded_2033_minus50bp` (D) | $9,281.45 (-100bp $28,752.60) | $9,281.45 ($28,752.60) | $0.00 | MATCH |
| `vasicek_theta_1962_vs_2000` | 6.190% (1990+ 3.905, 2000+ 3.295; ADF p 0.42) | same | 0.00bp | MATCH |
| `ewma_vol_today` | 81.2bp/yr (1962-2026 101.1; sigma_h 50.77bp) | same | 0.0 | MATCH |
| `sensitivity_purchase_4jan2027_median` | 33.07% (reference code rerun at the spec's n_h = 65; 32.95% at n_h = 64) | 33.08% (n_h = 65) | +0.01pp (+0.13pp) | WITHIN TOL: s3 #8 (new) |
| `stdlib_deterministic_check_failures` | 0 of 29 against the reference build | 0 of 23 against numbers.yaml and the blind build | - | MATCH, s4b (new) |

Tally for this table: 20 MATCH and 6 WITHIN TOL with a named cause. It counts the two anchor rows (Cost_FWD and PV
today) and the third-pricer row. The full 115-row file gives 94 MATCH, 21 WITHIN TOL and 0 UNRECONCILED. It also
covers:
- every E1-E5 detail and the 25 Sep per-estimator runs;
- the window counts (15,855 / 247 / 5,661 / 15,605, all exact);
- the 2028 p5 figures, P(no fund), P(top-up) and all H13 top-ups;
- the per-estimator 4 Jan runs.

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
   Like for like, E1 is 33.7% vs 33.2% and the median is 33.0-33.1% vs 32.7%. Fixed (and updated at the re-check).
8. **The 4 Jan five-estimator median (new at the re-check).** The blind build gives 33.08%. The reference build only
   ran E1 on 4 Jan. Its own code was therefore rerun with the purchase on 4 Jan (`primary_4jan_variant.py`, patched
   in memory; the source file is untouched). It gives 33.07% at the spec's n_h = 65 and 32.95% at the correct 64.
   - Matching points: E1, E2, E3, Cost_RW on 4 Jan ($293,536.88) and the break-even (22.32bp) are identical.
   - E4 differs by 0.03pp. Cause: sampler noise, as in #1.
   - E5 differs by 0.01pp. Cause: the reference code recalibrates rho over 98-day windows (0.9888), while the blind
     build reused the 95-day rho (0.9895).
   - Class: spec ambiguity. It is written into the spec changelog as a fifth reading. Ignore: sensitivity only.
9. **Wording in the blind builder's report (not in any deliverable).**
   - "21.9-32.7%" for E2's range: the low end is 21.85%, which rounds to 21.8%.
   - "a shortfall exceeds $10,000 in about one case in eight": the median of E1-E5 is 13.4%, so about 1 in 7.
   - `gap_if_any_typical` is called "E5's mean gap" there and "the median of E1-E5" here. These are the same number
     ($10,010), because E5 is the middle estimator (range $8,006-10,525).
   - 2026 volatility: the reference report says 71bp/yr (root mean square) and the blind build 70.6 (standard
     deviation).
   - Class: ignore. If any of these is quoted, use this record's wording.

## 4. Monte Carlo precision: is 32.7% really 32.7%?

| Estimator | 100,000-draw run | Without noise |
|---|---|---|
| E5 | 32.66% | 32.69% (closed form, which the third pricer also gets) |
| E3 | 32.69% | 32.55% (averaged exactly over 2,000,000 parameter draws) |
| E4 | 32.21% | 32.31% (8,000,000 draws) |
| E1, E2 | 33.16%, 26.67% | no draws involved |

- The median with the noise removed is 32.55%.
- Leaving any one estimator out, the median is 32.43-32.68%.
- The headline's noise is therefore about +-0.15pp, and "about 1 in 3" holds under every version.
- Quote it as "about 1 in 3" (or "about 33%"), never to a decimal.

## 4b. Third pricer vs the reference build (new at the re-check)

`gateB_ws4_third_pricer.md` has the full list. The third pricer uses the standard library only and was written from
the spec and the 28 Sep curve row. On 28 of the 29 comparisons it reproduces the reference build's deterministic
figures to rounding error:
- Cost_FWD $292,418.11, Cost_RW $293,401.14 and PV today $289,119.20.
- Break-evens of 26.20bp and 22.78bp.
- Ladder yield 5.3289% and its sensitivity to a parallel shift, 1.0075.
- The 2033 rung, $37,166.35.
- The 2028 fund $40,736.19 (RW $39,708.05) and the floor $117,193.70.
- All six H13 funds, floor faces and top-ups, and H14's $9,281.45 and $28,752.60.

The largest dollar difference is $0.00000000008 and the largest basis-point difference is 0.0000000013bp. The 29th
comparison is E5: the closed form gives 32.69% against the reference build's Monte Carlo 32.66%. So the dollar
figures behind the decisions have now been computed three ways, with no shared code.

## 5. Reconciliation with insight_v1 (`rab/inventory.md` s2 and the M2 inventory rows)

| Ref | insight_v1 figure | Rebuilt here | Why the M2 answer differs |
|---|---|---|---|
| H5 (25 Sep, "about 1 in 3") | D1 [6] 30.5%<br>S4 30.7%<br>strategy_mc_v2 30.2% / 34.4%<br>AX1b 19bp: 31.8 / 36.1 / 34.0% | 30.52%<br>30.73%<br>30.09% (analytic, both builds) / 34.37%<br>31.80 / 36.11 / 34.04% | On the same 25 Sep curve, M2 gives 37.9% in both builds. Two reasons: yields-unchanged pricing ($295,432, 15.7bp of room against 19.3bp) and today's higher volatility |
| D1 [6] exact dates, 25 Sep (M2 inventory row; third session) | 24.3% (30.5% on the Nov-15 basis) | 24.29% (exact-date cost $292,263.85, volatility 7.24%/yr); the same code gives 30.52% on the Nov-15 basis | Reproduced. Payment-date pricing is not buyable (nothing matures on 1 Jan), so it is a secondary figure, as at Gate A |
| AX1b [B] (M2 inventory row) | An "unchanged curve" adds about $1.0k to the January cost (inventory: +$1,044) and lifts the odds about 3 points (+3.4 on 25 Sep) | +$1,044 on 25 Sep and +$983 on 28 Sep (Cost_RW - Cost_FWD); odds +3.42pp on 25 Sep (third session) and +2.95pp on 28 Sep (R2 24.2% to R5 27.2%) | Reproduced. This is waterfall step 3: M2 takes no view on direction, so it prices the ladder at unchanged yields |
| H6 (28 Sep) | 24.2% Nov-15<br>18.7% exact dates<br>history 27.6 / 31.1% | 24.21%<br>18.70% (recomputed with the blind build's curve code)<br>27.55 / 31.06% | 24.2% becomes 27.2% (+3.0pp, yields-unchanged pricing), then 32.7% (+5.5pp, the five methods' volatility and curve shape). strategy_mc_v2 on 28 Sep: 23.95% |
| H7 (2026 days over $300k) | 173/185 exact, 176/185 Nov-15; worst 27 Feb, $327,631 | Identical to 25 Sep. To 28 Sep: 173/186 and 176/186. The last Nov-15 day over $300k was 22 Sep | Not an M2 output. Context: the ladder cost more than $300k on almost every 2026 trading day up to 22 Sep |
| H13 (E6 [8], 25 Sep) | -50bp: fund $20-23k<br>-100bp: fund $1-7k<br>-150bp: no fund; floor $127-137k | Both builds on 25 Sep: top-ups $9,555 / $25,711 / $42,633 (the figures E6 hard-codes)<br>funds $19,962-22,804 / $881-6,648 / none<br>floor $127,395-136,900 | On 28 Sep: $22,590-25,419 / $3,626-9,366 / none; floor $130,724-140,469. Yields rose, so the top-ups are smaller and the floor is cheaper |
| H14 | 25 Sep: $11,957 / $31,413<br>28 Sep: $9,281 / $28,753 | Exact on both dates, in all three pricers on 28 Sep | - |
| H18 (WS3/WS4) | A payment partly unfunded on 197 of 6,688 days, all 2020-2021 | Not rebuilt here | A history-of-yields result owned by WS3 M5; M2 does not compute it |

**What this changes.** Inventory F2, row H6 and the M2 gaps note said the model odds "fell to about 1 in 4" by
28 Sep, and that "every method gives lower odds". That was true of insight_v1's methods, which assume forward rates
come true and use 2026's calm volatility. With no view on direction and today's volatility, the odds are still about
1 in 3. The line survives, but for new reasons.

## 6. Triage (contradiction rule: strategy unchanged, nothing applied to the IPS or the Sheet)

**Fix before 6 Nov (RAB files only):**
- WS1: add the six proposed entries in `rab/results/M2/m2_proposed_numbers.yaml` to numbers.yaml; they are now
  Gate B reconciled. Record a changelog line and a new lock. Retire `ref.H5` and mark `ref.H6` "reproduced, not quoted".
- WS0: `rab/assumptions.md` C2 and `rab/premortem.md` PM-32 still give 24.2% as the model figure. Replace it with
  `laura.rates.gap_odds_2027`.
- Friday: rerun both builds with `--curve-date`, then this check. MOVE was 106.29 on 29 Sep (Yahoo ^MOVE,
  `rab/data/m2/MOVE_yahoo_daily.csv`), against 101.82 on 28 Sep, so E5 may move. Do not quote the odds before the
  rerun. Rerun the third pricer too (`deterministic_check.py --curve-date`); this check reads its 28 Sep output.

**Note in the Final Report:**
- "About 1 in 3 (MODEL, 28 Sep curve, no view on the direction of rates; five methods give 27-33%)". State the basis:
  Nov-15 STRIPS, MODEL prices, one purchase day. Never put it in a WInS note.
- The 1 Jan 2027 cost has two versions: $292,418 if forward rates come true (26.2bp of room, numbers.yaml) and
  $293,401 if yields stay unchanged (22.8bp).
- The 1 in 3 now rests on different reasons from insight_v1's (s5).
- Buying on Mon 4 Jan instead of 1 Jan changes nothing that matters (about 1 in 3 either way: 33.0% vs 32.7%).

**Ignore:**
- E4 sampler noise.
- Bootstrap seeding.
- AX1b float ties.
- The 4 Jan n_h erratum and the rho-window reading.
- The wording points in s3 #9.

## 6b. Downstream use of M2 numbers (third session)

The rule is that no decision may rest on an unreconciled number. The hedge memo (`rab/decisions/D_pre2027_rate_hedge.md`)
and its key file (`rab/numbers_ws4.yaml`, 17 entries) were written after this gate first passed, so both were checked
against the table here.
- **Numbers in the file:** 15 of the 17 entries point to a MATCH or WITHIN TOL row, or to a locked numbers.yaml entry.
  - The 4 Jan figure, 32.95%, is the row "4 Jan median, primary at strict n_h = 64" (WITHIN TOL).
  - `perfect_hedge_expected_gain` ($983.02) is the difference of two MATCH rows.
- **The two entries without a row of their own:**
  - `stock_fund_2028_p95`: $70,944.66 in both builds (`m2_2028_horizon.csv` H-RAW and the blind build's
    `results.json`), identical.
  - `move_index`: an input, not a result. The 29 Sep value (106.29) is data that has not yet been run through M2.
- **Numbers in the memo:** each is one of those entries, a numbers.yaml entry, or the insight_v1 staging result
  (D1 [7]). The memo labels that result "not re-checked".
  - The memo does not rest on D1 [7]. It rejects staged buying as a rate bet, which is a reason and not a figure.
- **Verdict:** nothing downstream rests on an unreconciled number.
- **Wording (ignore; for the memo's owner):** the memo says "Medium on the odds: a one-quarter figure". This could be
  read as "1 in 4". "A three-month figure" says what is meant.
- **Memo revision (30 Sep, after this check):** the wording is fixed ("a three-month figure"). The memo now carries the
  coupon-reinvestment caveat required by numbers.yaml's rules: its odds are STRIPS basis, and the WInS-listed ladder
  (Book L, the real ladder under `assumptions.md` R1) is not computed. Three entries were added, so the key file has
  20: `bookL_cost_today` ($292,914.11) and `bookL_coupon_buffer_2pct` ($20,399) are locked numbers.yaml entries
  (`wins.bookL.cost_model_accrued`, `reinvest.bookL_buffer_cost`); `gap_odds_2027_bookL` is `null`, NOT COMPUTED.
  None of the three is an M2 result, so this gate's table is unchanged, and the decision rests on none of them.
- **Second memo revision (30 Sep, after WS7's fact-audit; 6b609b0):** the memo's "Book L odds likely higher" was
  wrong. The Sheet sizes Book L to each holding's end date and rounds up, so it delivers $507,479 at forward rates,
  not $500,000 (numbers.yaml `reinvest.bookL_delivered.at_curve_forwards`). Rescaled rung by rung to pay exactly
  $50,000 at forwards, it costs $289,175.75 with commission ($289,000.75 without), against $289,119.20 for STRIPS
  (`rab/results/M2/bookL_basis_check.py`, reads the Gate-A-passed `m1_results.json`; stdlib and venv runs identical).
  So the odds should be about the same on either basis; still not computed. `bookL_coupon_buffer_2pct` was removed
  (the memo no longer uses it; the coupon-gap owner belongs to D6/D_range/D_stress) and `bookL_cost_resized` added
  (DERIVED, not an M2 result): still 20 entries. This gate's table is unchanged and the decision rests on none of them.

## 7. What Gate B cannot catch

Both builds (and the third pricer) follow the same spec, so the assumptions they share are not tested:
- MODEL STRIPS prices with no dealer mark-up (a mark-up raises the odds).
- A single purchase day.
- History as the guide to the future.
- MOVE taken from Yahoo, a secondary source.
- E4's mean reversion is not bias-corrected.
- No odds are computed for a ladder built from WInS-listed instruments.

These are the reference card's stated limits. WS7 should challenge them.

## 8. Files and rerun

- **Record:** this file.
- **Checks:**
  - `rab/verification/gateB_ws4/gateB_ws4_checks.py`, which writes `gateB_ws4_results.json`,
    `gateB_ws4_table.csv`, `gateB_ws4_table.md` and `gateB_ws4_third_pricer.md`.
  - `primary_4jan_variant.py`, which runs the reference code on a 4 Jan purchase (in memory; output to a temp folder
    only).
- **Changed at this gate:**
  - `rab/models/M2_SPEC.md` (changelog, two entries)
  - `rab/models/M2_CARD.md` (s3 #7, a Gate B line and the re-check)
  - `rab/verification/blind/m2_blind.py` (s3 #5)
  - `rab/verification/blind/README.md` (s8)
- **Changed in the third session:** `gateB_ws4_checks.py` now also rebuilds the two inventory figures in s5 (its
  output gains the key `insight_v1.third_session_25sep`; the 115-row table is unchanged) and this record (s5, s6b).
- **Not changed:** any reference result in `rab/results/M2/`, `rab/numbers.yaml`, and the third pricer.
- **Rerun** from the worktree root (about 40 s, seed 20260930; it reruns both builds on 25 Sep and the reference build
  on 4 Jan, in temporary folders):
  `/Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws4/gateB_ws4_checks.py`
