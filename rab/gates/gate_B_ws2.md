# Gate B, WS2 (M3 branch, M4 cap share D6, M8 sensitivity): primary build vs blind rebuild

WS2 Gate B reconciler, 30 Sep 2026 (Sydney). This is an AI-generated verification record (Claude Code) for Team
Caplet. It contains MODEL outputs, not deliverable text. The strategy is not reopened (RUN_PLAN s0). Nothing was
executed externally, and `rab/numbers.yaml` is untouched (sha256 `492ed320...`, the Gate A lock).

**Verdict: PASS.** Every headline key reconciles, and none is UNRECONCILED.
- **Blind keys:** all 307 were compared. 53 MATCH, 247 are WITHIN TOL, 7 are REPORT (Pareto diagnostics, which have no
  tolerance and feed no decision), and 0 are outside tolerance.
- **Primary headline keys:** all 29 were compared, as 36 rows. 10 MATCH, 25 are WITHIN TOL and 1 is REPORT.
- **The decision numbers are identical in both builds:**
  - largest passing share s*: 0.50 / 0.47 / 0.47, so the robust s* is 0.47;
  - PR-7 keeps half;
  - h* = 0.025, so the floor is announced as $145,000;
  - the same three IPS assumptions: the curve on 1 Jan 2027, the 5-year yield on 2 Jan 2028, and costs;
  - the floor readings agree to the cent.
- **No decision number in the primary build was wrong.** Fixed at this gate:
  - one wrong line in a primary log;
  - five wording errors in the D6 memo and the cards;
  - three spec ambiguities, now written into the specs.

**In plain English.** Two separately written programs give the same answers. The 2031 top is about $175,000
(1 in 20 below about $165,000, 1 in 20 above about $190,000). The gift reaches the top about 3 times in 4. Half is
about the largest share that still leaves Laura a tenth of her gift in 19 of 20 outcomes, so the pre-registered
rule keeps half. Each program's rule code gives the other program's published numbers exactly when run on the other
program's random paths. The small gaps between the builds are therefore dice, not method.

## 1. What was compared

- **Primary build:**
  - code: `rab/models/m3_branch.py`, `m4_cap.py`, `m8_sensitivity.py` (commits 46e8a89 and 591f938);
  - specs: 3d98ce0, where the M4 decision rule was committed before any M4 code was written;
  - outputs: `rab/results/`.
- **Blind build:** `rab/verification/blind_ws2/` (ef2beae), built from the three specs and the raw inputs only. Its README
  discloses that the builder saw the primary's STATUS line before building.
- **Evidence the builds are independent:**
  - different random streams (SeedSequence spawn against per-tag hashes);
  - different loaders (pandas reindex against searchsorted);
  - different curve code (a 1bp grid with interpolation against a vectorised exact curve);
  - separate MCMC runs;
  - at the one real ambiguity (s3 #4), the two builders read the spec differently.
- **Reruns today:**
  - Primary: `make -f rab/models/ws2.mk all` took 57 s. Every CSV, PNG and YAML came out byte-identical; only the
    run-log time stamps changed, plus the one line fixed in s3 #5.
  - Blind: its rerun this morning was byte-identical (`rab/verification/blind_ws2/README.md`).
- **Check script:** `rab/verification/gateB_ws2/gateB_ws2_checks.py` (about 20 s, seed 20260930).
  - `gateB_ws2_table.csv` / `.md`: all 307 keys;
  - `gateB_ws2_primary_headlines.csv`: 36 rows;
  - `gateB_ws2_results.json`, `noise_band.csv`, `numbers_proposed_M4_M8.yaml`.

## 2. Key-by-key table (the primary's headline keys and every decision key)

(D) marks a decision-relevant key. Tolerances come from the specs:
- range ends and dollar outcomes +-2% (M8 tornado +-1%);
- probabilities +-2 points;
- s* within 0.02;
- h*, A, PR-7 and the top 3 identical;
- Sobol ST within 0.05;
- deterministic dollars to the cent.

| Key | Primary | Blind | Diff | Verdict |
|---|---|---|---|---|
| M3 median 2031 top: T / BOOT / BAYES (D) | $174,938 / $175,487 / $174,966 | $174,966 / $175,472 / $175,001 | -$28 / +$15 / -$34 (0.02%) | WITHIN TOL |
| 2031 top p5, lowest of 3 (BOOT) (D) | $165,204 | $165,182 | +$22 | WITHIN TOL |
| 2031 top p95, highest of 3 (BAYES) (D) | $190,727 | $190,687 | +$40 | WITHIN TOL |
| P(gift reaches the top) T / BOOT / BAYES (D) | 75.47 / 74.37 / 71.96% | 75.49 / 74.36 / 71.84% | -0.02 / +0.01 / +0.12 pts | WITHIN TOL |
| P(gift in upper half), lowest (BOOT) (D) | 99.23% | 99.24% | -0.01 pts | WITHIN TOL |
| Gift inside the range, 8 models x 200,000 paths (D) | 1 (0 of 1.6M outside) | 1 | 0 | MATCH |
| 2033 gift, BAYES p5 / p50 / p95 | $164,143 / $174,023 / $189,749 | $164,142 / $174,046 / $189,735 | +$1 / -$23 / +$14 | WITHIN TOL |
| P(fund below its 2028 cost in 2031), range of 3 | 20.71-24.28% | 20.65-24.31% | <= 0.06 pts | WITHIN TOL |
| L analytic median top / P(top) | $174,952 / 73.25% | same formula | 0 | MATCH |
| L simulated median top / P(top) | $174,988 / 73.45% | $174,988 / 73.28% | $0 / +0.17 pts | WITHIN TOL (s3 #2) |
| BAYES posterior means m_h / sigma / nu | 0.0952 / 0.1567 / 17.80 | 0.0946 / 0.1566 / 18.12 | at most 1.8% | WITHIN TOL (10%) |
| E6 reconciliation, largest gap to insight_v1 H8 | $400 | $256 | - | REPORT (exact on E6's draws, s4) |
| M4 h* and announced floor A (D) | 0.025, $145,000 | 0.025, $145,000 | 0 | MATCH |
| s* T / BOOT / BAYES; robust s* (D) | 0.50 / 0.47 / 0.47; 0.47 | 0.50 / 0.47 / 0.47; 0.47 | 0 | MATCH |
| PR-7 recommendation (D) | keep 1/2 | keep 1/2 | - | MATCH |
| P(keep >= 10% of gift) at 1/2, T / BOOT / BAYES (D) | 95.30 / 93.59 / 93.25% | 95.38 / 93.71 / 93.22% | at most 0.12 pts | WITHIN TOL |
| P(gift < $145,000) at 1/2, every model (D) | 0 | 0 | 0 | MATCH |
| Kept at 1/2: p5 / p50, range of 3 | $15,483-16,720 / $32,504-33,608 | $15,495-16,781 / $32,451-33,633 | <= 0.4% | WITHIN TOL |
| Floor pays: median / worst | $149,404 / $146,330 | $149,410 / $146,330 | -$7 / $0 | WITHIN TOL / MATCH |
| P(floor pays < $150,000) | 69.29% | 68.95% | +0.34 pts | WITHIN TOL (exact list: 69.11%) |
| Rule sensitivity, robust s*: 5% / 15% / 10% at 99% (all 12 cells) | 0.72 / 0.23 / 0.20 | 0.72 / 0.23 / 0.20 | 0 | MATCH (15%/99%: none in both) |
| P(gift = face-based top) at 1/2, T | 25.11% | 25.56% | -0.45 pts (3.3 s.e.) | WITHIN TOL (s3 #3) |
| Narrower range: breach at a ~$160k low end, BOOT | 0.42% (at $160,292) | 0.46% (same low end) | -0.05 pts | WITHIN TOL (s3 #4) |
| Top announced from $145k (M4 A2, exploratory) | 90.4-93.0% reached | 90.5-93.0% (computed here on blind paths) | <= 0.1 pts | WITHIN TOL |
| Pareto points dominated by the grid, T / BOOT / BAYES | 8 / 8 / 7 | 2 / 3 / 17 | - | REPORT (s3 #7) |
| M8 base V_A(0) and B0 (D) | $292,418.11 and $40,736.19 | same | $0.00 | MATCH |
| M8 base median 2031 top | $174,941 | $174,950 | -$10 | WITHIN TOL |
| X4 and X5 ranges from the data | -93 / +92 bp; -1.95 / +2.27 pts | same | 0 | MATCH |
| Sobol B ST, median top: X4 / X5 / X6 / X1 (D) | 0.898 / 0.068 / 0.033 / 0.003 | 0.898 / 0.067 / 0.033 / 0.003 | <= 0.001 | WITHIN TOL |
| Three assumptions the IPS must state (D) | X4, X5, X6 (p5 and tornado agree) | same | - | MATCH |
| Tornado swing, median top: X4 / X5 / X6 / X1 | $50,866 / $14,320 / $8,357 / $2,692 | $50,878 / $14,325 / $8,364 / $2,694 | <= $11 | WITHIN TOL |
| Sobol A luck share (sum of S1 / sum of ST) | 0.169 / 0.217 | 0.169 / 0.217 | 0 | MATCH (s3 #8) |
| Floor reading at -50bp: IPS / E6 reading (D) | $142,612 + $28,501 / $150,000 + $22,590 | same | $0.00 | MATCH |
| Floor reading at -100bp: IPS / E6 reading | $126,560 + $22,836 / $150,000 + $3,626 | same | $0.00 | MATCH |

Tally:
- 307 blind keys: 53 MATCH, 247 WITHIN TOL, 7 REPORT, 0 UNRECONCILED.
- 36 primary rows: 10 MATCH, 25 WITHIN TOL, 1 REPORT.
- Largest gaps inside tolerance:
  - dollars: 0.55% (the BAYES-hist kept p50, s3 #1);
  - probabilities: 0.45 points (s3 #3);
  - decision dollars: 0.4% (kept p5 at 1/2).

## 3. Every difference, its cause and what was done

1. **Sampling noise, shown directly.**
   - **The rule code agrees exactly.** The primary's rule code on the blind's paths and floor draws reproduces the
     blind's published M3 summary to rounding ($0.005) and its M4 measures to 1e-16. The blind's code on the
     primary's paths does the same in reverse. s* comes out the same both ways.
   - **The inputs are identical.** Both builds use the same 8,565 historical 30-month changes of the 1-year yield.
   - **The paths come from the same distribution.** A KS test compared the 3-year and 2-year growth, model by model
     (16 tests). 14 give p >= 0.05.
   - **BOOT-b1 (p 0.01) is chance.** Re-seeded runs give p 0.12-0.94, and the primary against its own other seeds
     gives p as low as 0.02.
   - **BAYES-hist (p 0.01-0.02) is a real but tiny shift.** Its forward centre is the posterior m_h, which came out
     0.0952 and 0.0946 in two separate MCMC runs (both converged). The effect on its median top is $89 (0.05%). BAYES,
     the decision model, passes (p 0.78). Class: ignore (M3_SPEC C2).
   - **Why BOOT-b60's median top matches to the cent.** With 60-month mean blocks, many paths are one unbroken
     stretch of history, so the median sits on a value both builds share.
2. **Noise band ("increase simulations").** The primary code was rerun with 10 more seeds, which adds 2,000,000 paths
   per model (`noise_band.csv`).
   - s*: T 0.50 in every seed; BOOT and BAYES 0.47 in every seed; L 0.49-0.50. The robust s* is 0.47 in all 10
     seeds, and pooling the 2,000,000 paths gives the same.
   - P(keep >= 10%) at half, pooled: T 95.30%, BOOT 93.64%, BAYES 93.20%.
   - Band widths: the median top moves only +-$30 between seeds, and P(top) +-0.2 points.
   - Of 48 published figures (both builds, 4 models, 6 figures), 38 sit inside the 10-seed range and 10 just outside.
     That is close to what chance predicts: a new draw lands outside the range of 10 others about 2 times in 11. Four
     of the 10 are the primary's P(gift = face-based top), because one floor draw serves all four models and it fell
     slightly low (s3 #3). The largest dollar case is the blind BAYES median top, $29 (0.02%) above the band.
   - The simulated L P(top) is 73.45% in the primary against the analytic 73.25%. That is 2.0 standard errors, and
     inside the band of 73.11-73.47%.
3. **P(gift = face-based top) differs by 3.3 standard errors.**
   - The cause is the floor draws. Each build samples phi separately, and the samples happened to fall below 1 in
     69.29% and 68.95% of cases.
   - With phi averaged over the whole historical list, T gives 25.33% (primary paths) and 25.35% (blind paths).
   - Class: ignore; M4_SPEC C3 records it.
4. **Narrower range: a spec ambiguity.**
   - The spec text, read literally, puts the low end at $146,250 + l x half the fund. The primary used the announced
     floor, $145,000 + l x half the fund.
   - The `narrower_range.csv` rows for the same l therefore differ by construction. At the same typical low end,
     P(gift below it) agrees to within 0.04 points in one build and 0.08 points across builds:
     - at $160k: T 0.03%, BOOT 0.38-0.40%, BAYES 0.03-0.04%;
     - at $165k: 0.89-0.92%, 1.85-1.93% and 1.11-1.16%.
   - The primary's reading is the right one for the IPS, because it is what Laura would say. Clarified in M4_SPEC
     C1. No decision uses it (PR-1).
5. **Bug in the primary: one log line.** `run_log.txt` gave the robust rule-sensitivity s* at 15% / 99% as 0.03,
   because pandas `min()` skipped BOOT, which has no passing share. It should be "none", as the blind build has it.
   - Fixed in `m4_cap.py` and rerun.
   - The CSV was always right, and no memo or card figure used that line.
6. **Wording errors in the primary's files, now fixed:**
   - D6 memo and M4 card: "15% reserve gives about 1/4". The largest passing share is 0.23, and PR-7 never rounds up,
     so the rule gives 0.20 ("about 1/5").
   - A2 (top announced from $145k): the gift is about $3,500 lower on average, not $3,000 (both builds $3,399-3,530).
   - D6 memo: "all but 5 of 200,000 history paths" becomes "a handful (3 to 5)", since the blind build has 3.
   - D6 memo: 42 becomes about 40 in 10,000 at a $160k low end.
   - M3 card: the 1-in-20 low top moves by about $1,000 across models. The $2,000 it quoted is the 1-in-20 high top.
   - Not in any file: the primary's WS2 summary message said "an iBond or coupon floor pays $146.3k-$151k". The
     correct range is $146,330 to $153,207 (p95 $152,431, median $149,410 on the full list).
7. **Pareto grid counts (REPORT).**
   - The counting rules agree: the blind's rule on the primary's front gives 8 / 8 / 7, and the primary's rule on
     the blind's front gives 3 / 3 / 17.
   - The gap therefore comes from the NSGA-II runs themselves, which use different paths.
   - The front sizes also differ: the primary keeps 116 points for T, only those feasible on 200,000 paths; the blind
     keeps all 120 and reports that 115 are feasible.
   - Both builds call the front indicative, and no decision uses it.
8. **Sobol luck share.** The primary quoted the sum of ST (0.22) and the blind quoted the sum of S1 (0.17). Both
   builds give identical values under each definition. Quote "about a fifth" and name the index used (M8_SPEC C1).
9. **E6 reconciliation basis.** The primary used E6's exact fund, $40,443. The blind used the spec's $40,400 on its
   own stream. Both land within $0.4k of H8. The check here reproduces H8 exactly on E6's own draws (s4; M3_SPEC C1).

## 4. Reconciliation with insight_v1 (`rab/inventory.md` s2)

The first column after the figure reuses E6's own random draws (`default_rng(20260927)`) and runs them through both
rule codes. The next column is the 28 Sep basis in both builds.

| Ref | insight_v1 figure | Rebuilt on E6's draws | 28 Sep basis, both builds | Why it differs |
|---|---|---|---|---|
| H8 | gift $165k / $174k / $188k<br>kept $16k / $32k / $66k<br>total $182k / $207k / $250k<br>top $175k, P(top) 73% | gift 165.0 / 174.0 / 187.7k<br>kept 16.4 / 31.9 / 66.0k<br>total 182.1 / 206.7 / 250.2k<br>top 174.8k, 73.26%<br>(every printed figure) | total 182.4 / 207.2 / 250.7k<br>top 175.0k<br>P(top) 73.45% (primary) / 73.28% (blind) | The fund rises $293, from $40,443 to $40,736: the floor is cheaper at a 5.06% 5-year yield than at 4.98%, which outweighs the smaller 2027 leftover ($7,582 vs $7,736). That moves the figures by up to $0.8k (the p95 total); the seed changes them by up to $0.3k and 0.2 points |
| H11 | Vanguard-like 5.08%: total $179k / $202k / $242k, P(top) 67% | 179.2 / 201.8 / 242.0k, 67.3% | 179.4 / 202.2-202.3 / 242.4-242.7k<br>67.3-67.6%<br>top $173.6-173.7k | Same fund effect. M8's X1 low end (4.08%) gives $173k, consistent |
| H12 | Bad 2031-32: gift median $169k, never below the bottom | 169.5k (bad 2028-30: 165.5k) | 168.4-169.6k in all 4 models and both builds; 100% at or above $150k | The history-shaped models (BOOT, BAYES) are about $1k lower, because their left tail is fatter |
| H13 | Rates fall first (E6 [8], 25 Sep), "5-year also lower": fund $20k (-50bp), $1k (-100bp) | - | M8 floor reading, E6 reading: $22,590 / $3,626, both builds to the cent | On 28 Sep yields are higher and the ladder is cheaper, so the top-ups are smaller ($7,388 / $23,440 against $10k / $26k). WS4 Gate B reconciled every H13 variant. New here: the IPS reading (F4) |
| H15 | Each $25k less floor: median +$2-3k, p5 -$9-10k | $125k floor: +$2,492 / -$9,434 | +$2.4k to +$3.1k / -$9.4k to -$10.6k | The BOOT and BAYES p5 fall about $10.5k: fatter tails make a smaller floor cost a little more in bad cases |
| E4 / E6 D6 | s = 3/4 keeps about $8k at p5; s = 1 keeps nothing when stocks fall | $8,277; nothing in 26.7% of paths | $7.8-8.5k; 24.5-28.2% | - |

**What this changes: nothing.** Every insight_v1 figure that WS2 must reconcile (H8, H11, H12, H15 and E4's s tests)
holds on the 28 Sep basis to within about $1k. E6's printed H8 is reproduced exactly from its own draws.

## 5. Triage (contradiction rule: strategy unchanged, nothing applied to the IPS or the Sheet)

**Fix before 6 Nov (IPS wording, the team's call):**
1. State the three assumptions that move the range: Treasury yields when the 2027 deposit buys the ladder, the 5-year
   yield when the floor is bought (Jan 2028), and costs paid from the stock fund. The primary triaged this as
   fix-before and the blind as a Final Report note. It is reconciled as fix-before, because the case asks for the
   assumptions to be stated and these three are what move the range.
2. Pick one floor reading (F4, already flagged): after a 50bp fall, "the whole remainder" gives $142,612 + $28,501
   and "keep $150,000" gives $150,000 + $22,590.
3. Optional: word the floor as "rounded down to the nearest $5,000" ($145,000).

**Fix before 6 Nov (RAB files, WS1/WS0):**
- Add the reconciled entries to numbers.yaml, with a changelog line and a new lock:
  - `rab/results/M3/numbers_proposed.yaml` (7 entries);
  - `rab/verification/gateB_ws2/numbers_proposed_M4_M8.yaml` (15 entries).
- Until then, the D6 memo's numbers trace to those files, not to numbers.yaml.
- Friday: rerun both builds and this check after the curve refresh, because the fund B0 moves with the curve.

**Note in the Final Report:**
- Announcing the top from $145k is an option: the top is reached 9 times in 10, with a gift about $3,500 lower.
- The price of a narrower range: a low end of $160k breaks about 4 times in 1,000, and $165k about 2 in 100.
- The return model barely matters.
- With an iBond floor, "capped at the top" means floor face + half the fund. The gift equals that face-based top only
  about 1 time in 4, while the fund holds its value about 3 times in 4 (the blind's note 2).

**Ignore:**
- s = 1/2 stays (D6: ratify on 26 Oct);
- the sampling noise in s3 #1-3;
- the Pareto counts;
- the BAYES-hist centre.

## 6. What Gate B cannot catch

Both builds follow the same specs, so the blind rebuild does not test the assumptions they share:
- the JPM 7.00% centre;
- stock returns independent of yields;
- U.S. history standing in for VT;
- the stylised floor-delivery model;
- one curve (28 Sep);
- fees only in M8;
- independent M8 inputs;
- the 10% / 95% value judgements in PR-5.

These are the cards' stated limits. WS7 should challenge them.

## 7. Files and rerun

- **Record:** this file.
- **Checks:** `rab/verification/gateB_ws2/gateB_ws2_checks.py`, with its outputs in the same folder.
- **Changed at this gate:**
  - `rab/models/m4_cap.py` (s3 #5) and `rab/results/M4/run_log.txt`. The M3 and M8 run logs were re-stamped by the
    rerun.
  - `rab/models/M3_CARD.md`, `M4_CARD.md` and `rab/decisions/D6_cap_share.md`: the wording in s3 #6, plus a Gate B line
    in each.
  - Spec clarifications: `rab/models/M3_SPEC.md` s8, `M4_SPEC.md` s10 and `M8_SPEC.md` s6. The decision rule is
    untouched.
- **Rerun from the worktree root:** `make -f rab/models/ws2.mk all` (about 1 minute), then
  `/Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws2/gateB_ws2_checks.py` (about 20 s). The
  check needs the blind paths; `rab/verification/blind_ws2/run_all.sh` regenerates them.

## 8. Re-check after the merge (30 Sep, 14:28 AEST)

- **The verdict still holds: PASS, 0 UNRECONCILED.**
  - `make -f rab/models/ws2.mk all` was rerun. Every output was byte-identical; only the three run-log time stamps
    changed, and those were reverted.
  - `gateB_ws2_checks.py` was rerun on the moved blind folder. All six outputs were byte-identical; only the log time
    stamp changed.
  - The WS2 files on `rab/integration` match `rab/ws2` (ac258db).
  - `numbers.yaml` is still `492ed320...`.
- **A red-team challenge that Gate B cannot settle (for Gate D, not a discrepancy).**
  - WS7 (`rab/redteam/ws7_devils_advocate_checks.py` [1], commit 913c4f1 on rab/ws7) reran the primary M4 code. It
    took the Book L coupon-reinvestment shortfall (`numbers.yaml` `reinvest.rung.*`) out of Laura's kept money.
  - Its "as run" rows reproduce the primary exactly, because they use the same code (T s* 0.50, 95.3%; BOOT 0.47,
    93.6%).
  - With the shortfall at today's yields minus 2 points, no share passes PR-5, not even share 0 (T 94.9%).
  - This is a different question from M4_SPEC, whose K has no ladder term. It is one of the shared assumptions in s6
    (one curve, the stylised floor), which the two builds cannot test against each other.
  - The D6 numbers above are reconciled on the spec's basis. Whether that basis is the right one for Book L is WS7's
    item at Gate D. It is not reopened here, and the strategy is unchanged.

## 9. Coupon check for WS7's challenge (30 Sep, after s8)

- **What was added.** `rab/models/m4_ladder_gap.py` (make target `m4-gap`). It is a sensitivity, not part of the
  pre-registered rule. It reruns the D6 rule with Laura's kept money reduced by the Book L rung gaps
  (`numbers.yaml` `reinvest.rung.*`), on both builds in one run: primary code and paths, and blind code and paths.
  Outputs: `rab/results/M4/ladder_gap*.csv` and `ladder_gap_log.txt`. Keys: `ws2.d6.ladder_gap` and
  `ws2.d6.ladder_gap_tolerance` in `rab/numbers_ws2.yaml`.
- **Reconciliation.** The primary rows equal WS7's output (913c4f1) line for line. Primary against blind is WITHIN TOL
  on every probability. The robust share is the same in every scenario (0.47 / 0.42 / none / none / none). The
  tolerances are within 1.4%. The only split is T at yields 2 points lower and share 0: 94.9% against 95.0%, a
  knife-edge on the 95% line. Both builds still give "none" as the robust share, because BOOT and BAYES fail.
- **Result.** Under rule reading R1, Laura's real ladder is Book L. At today's yields the gap is about $1,613 (valued
  1 Jan 2033), and PR-7 still keeps half (robust 0.42). Half survives gaps up to about $2,352. At yields 2 points
  lower no share passes. Decision memos updated; the strategy and the D6 decision are unchanged. The coupon fix stays
  the Gate A / Gate D item.
- Every earlier output is unchanged: the new script writes only new files. `numbers.yaml` is still `492ed320...`.
