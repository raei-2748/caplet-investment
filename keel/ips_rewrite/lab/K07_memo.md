# K07: the R07 synergy tests (the Lab, Jun), Tue 27 Oct 2026

> AI-generated research (Claude Code), not for submission. Keel recommends, Caplet decides. **Every number is MODEL.**
> STAMP: curve 22 Oct 2026 (ladder $298,861, headroom $1,139) | J.P. Morgan 2027 world stocks 7.5%, 16.78% vol |
> 100,000 paths per world | seeds: house 20261027, storms 20261028, deposit noise 20261107 | engine = the Model Suite
> (`keel/models/xr_core.py`, unchanged; `xr_plus` in the script is a copy of it that reproduces it exactly when the new
> switches are off). Code `K07_synergy_tests.py`, numbers `K07_results.json`. Questions: `../research/R07_synergies/FUSIONS.md` s.4-5.
> **The 2031 lock is a Courtroom recommendation (28 Oct), not part of V25.** "Champion" = V25 + lock + rule G
> ($7,500 cushion in 2033). "V25+G" = the cushion without the lock. Short = a cheque more than $1,000 short.
> **Run:** T1, T5, T2+T3 (same paths, side by side, and combined, as Tess asked), T4, T8, T7. **Not run:** T6, T9, T10.

**Engine note.** FUSIONS quotes 7.7% for "the coupon gap is bigger than what Laura kept" (K_overnight's lab engine).
In the Suite engine the same measure is **4.4%** for V25. Read every T1 number against 4.4%, not 7.7%.

## Results
**T1 joint storm (A).** The deposit is $150k × f. f falls with 2027 stocks and yields, can only shrink, and is
**$84k in a 1-in-20 year**. Rho is also the stock-yield link. Each cell runs rho 0 / 0.5 / 0.8.
- V25 cheques short: **2.6% / 3.5% / 4.0%** (2.0% with a fixed $150k).
- V25 gift below the bottom: **2.0% / 3.6% / 4.9%** (1.3%).
- V25 gap bigger than what Laura kept: **5.5% / 6.7% / 7.4%** (4.4%).
- Champion cheques short: **0.35% / 0.58% / 0.82%** (0.20%).
- Champion gift below the bottom: same as V25, **up to 4.9%**.
- **2008 replay** (yields -1.9pt by Jan 2027, deposit $75k, stocks -40% in one year):
  - The ladder costs **$361,003**, and the deposit closes the $61,003 gap. Only $13,997 is left for floor and VT.
  - Cheques short afterwards: **14-18%** (champion 13.8%, V25 17.8%). The median shortfall is about **$2,600 over the decade**.
  - If yields fall another 1.9pt during 2028: **43-46%**.

**T5 implied ratio (Conflict 4).** P(top) is shown as house / storms / history (2027-33 window), with k = P/(1-P).
- **V25, no lock:** 75.4% / 78.3% / 83.9%, **k = 3.1 / 3.6 / 5.2**.
- **Lock only:** 90.6% / 91.0% / 99.5%, k = **9.7 / 10.1** / 194.
- **Champion:** 83.9% / 84.5% / 96.8%, **k = 5.2 / 5.5** / 30.
- **V25+G:** 70.9% / 73.9% / 82.1%.

There are two ways back to about 75% under the lock:
- **Route 1:** the gift owns and locks **70% of VT**, not 50%. P(top) is 75.3% (house) and 76.4% (storms); history
  needs 80%. The top median rises +$7.1k, but Laura's kept median falls **$17.0k → $9.0k**.
- **Route 2:** lock half, but quote the top at **0.54 × VT**, the half plus most of its 2-year interest. P(top) is
  73.8% (house) and 75.9% (storms), for only +$1.4k of top. It is a **cliff**: at 0.58 the odds are 43%.

**T2 + T3 on the same paths.** House world, champion or V25+G. Cells read "base → T2 hold-back / T3 re-measure / both".
- Cheques short: **0.20% → 0.00% / 0.00-0.01% / 0.00%**.
- Gift below the bottom: **1.3% → 0.0% / 0.0% / 0.0%**.
- **Mean gift:** $163.2k → **$154.1k** / **$163.1k** / $154.1k.
- Mean bottom: $139.7k → $130.1k / **$137.3k** / $131.8k.
- Laura kept in 2033 (mean): +$8.6k with the hold-back (its spare money lands with her), unchanged with the re-measure.
- In the **joint storm** (rho 0.8 plus the linked deposit), with the champion:
  - cheques short: 0.82% → 0.02% / **0.03%** / 0.01%
  - gift below the bottom: 4.9% → 0.19% / **0.03%** / 0.01%
- **T3 needs the cushion.** V25 with no cushion keeps **2.0%** of cheques short under T3. The 2031 date fixes the
  range; the 2033 cushion pays the cheques.
- In the 2008 replay neither rule rescues it (about 9% short either way). There is no money to reserve.

**T4 survivorship (C, D).** The equity return is cut by 0 / 0.6 / 2.0pt.
- V25's top odds: house 75.4 / 74.0 / 70.9%; storms 78.3 / 77.3 / 74.8%; US history window 83.9 / 82.7 / 80.5%.
- Champion cheques short: 0.20 / 0.21 / 0.25%. V25's median gift: $165.3k / $164.9k / $164.1k.
- Rivals' broken promises (house): 29-36% / 31-39% / 35-44%. The 60/40's median gift: $159k / $147k / **$118k**.
- History stays kinder than house even after -2pt. Its tilt comes from its path (smooth pre-1953 yields, A34), not
  only its level.
- History-world figures that rest on US-only data (A07):
  - M1b: 0 broken promises in 1,756 starts; 84% / 97% top reached
  - M6: the history odds of 5:1
  - M7: the history column
  - M8: the 1923 start
  - every bootstrap_raw figure
  - M1 and M3 use yields only, so survivorship does not apply to them.

**T8 the short rung (Conflict 2).** The ladder costs more than $300k in **46%** of paths. The median gap is **$8.4k**
(p95 $25.9k); R06 K2 said $9.8k in the lab engine.
- Buying the longest rungs first, the **2033 rung (IBTM) is short in 100%** of those paths, and 2034 as well in 0.3%.
- Buying the missing part on 2 Jan 2028 costs a median **+$22** more than the 2027 gap plus a year's interest
  (p5 -$898, p95 +$1,204).
- Buying the shortest rungs first leaves 2042 short, with **about 3× the tail** (p5 -$2,458, p95 +$3,466).

**T7 deposit × yields (Conflict 1).** V25 with L-10's coverage test. The smallest deposit with no cheque more than
$1k short:
- yields unchanged: **$40k** ($25k: 0.1%)
- yields -1pt: **$65k** ($50k: 0.2%)
- yields -2pt: **$85k** ($75k: 1.5%; $65k: 11.9%)

Without the test, even $150k leaves 2.5-4.2% short.

## What it means
| | Verdict | Why (MODEL) |
|---|---|---|
| **A** one storm | **Keeps the argument; changes the fix** | The joint hole is real: at rho 0.8 every V25 risk grows 1.7-3.8×, and the range breaks 4.9%. A's own fix (the 2028 hold-back) works, but it costs about **$9k of mean gift**. B's 2031 re-measure gets the same safety for $160. Name the shared cause; use B's date. |
| **B** reserve on a date | **Keeps; becomes the plan change** | Re-measuring the gap in January 2031 and deducting it before the range is named turns the range's 1.3% (joint storm 4.9%) into about 0.0%, at a mean bottom $2.4k lower. It adds no new date: 2031 is when the range is named anyway. It works only alongside the 2033 cushion (rule G). |
| **C** two standards | **Keeps** | The top's "about 3 in 4" survives a 0.6pt haircut everywhere and a 2pt haircut in house and storms (71-75%). Keep the bar on quoting the history odds. T1 shows the bottom holds in the bad case only with T3. |
| **D** one plane | **Keeps, stronger** | A 2pt haircut costs our median gift $1k and the 60/40's $41k. The rivals' broken promises rise to 35-44%. Certainty does not depend on the equity forecast. |
| **E** lead gift | **Untested (T6 not run); one link found** | Under the lock the implied k is 5-10. That is E's 5-10× pyramid multiplier. If E is right, the lock's odds are the right fractile. |
| **F** standby, called last | **Keeps; vetoes T5 route 1** | Route 1 halves Laura's standby ($17k → $9k median). The hold-back adds +$8.6k to her standby, but only by taking it from the gift. |
| **Conflict 1** | **Confirmed; the sentence changes** | "More than halves" covers only the build. Counting the coupon backstop, the cheques break at yields -2pt when the deposit is under about **$85k (a fall of more than about 43%)**. The 2008 replay at $75k leaves 14-18% short. The honest claim: the deposit's first dollar goes to the cheques, and its next ones are the coupons' backstop. |
| **Conflict 2** | **Confirmed** | It is always the 2033 rung. Waiting a year costs about $0 at the median and about $1.2k at p95. Longest-first is the cheaper order. |
| **Conflict 3** | Not tested | T6 not run. |
| **Conflict 4** | **Confirmed** | Under the lock, "about three times in four" is untrue: the top is reached 84-91% of the time (champion/lock, house-storms), k 5-10. The fix is to **restate** ("about five times in six"), or keep V25 with no lock. Do not re-size: route 2 is a cliff and route 1 costs F. |
| **Conflict 5** | Respected | T2 buys an IBTM-like Treasury. The Suite's 2033 "bills" are a modelling convention, not wording. |
| **Conflicts 6, 7** | Not a numbers question | The model uses the 22 Oct curve. |
