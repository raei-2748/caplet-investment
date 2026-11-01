# L-15 results, for round 2 (MODEL; run after round 1's posts and sealed guesses were written)

> Keel is a simulated team, AI-written. Script `../../../rooms/lab/L-15_hold_it_then_say_it/run.py`, results
> `results.json` beside it. STAMP: curve 22 Oct 2026 | J.P. Morgan 2027 world stocks 7.5% | 200,000 paths, seed
> 20261016 (bridge draws 20261101) | V47's design (L-13 slide + lock, via L-14 and Archive A26's k = 0.76 match) |
> worlds S0 (independent), S1 (rates and stocks linked), S6 (yields fall 2 points for good) | MODEL.
> Controls: same-day top reached = L-14's XR row exactly (97.90 / 97.60 / 96.02%); A26's mean lead reproduced
> ($14,917 / $15,399); the year-late arm uses L-12's "delayed 1y" lock rule exactly (an identity, asserted in the script; not a reproduction of L-12's number, which was on V29's design).

## A. Order and lock timing (top reached, %; S0 / S1 / S6)
| Arm | S0 | S1 | S6 |
|---|---|---|---|
| Same day (V47) | 97.9 | 97.6 | 96.0 |
| Name first, move a week late | 97.7 | 97.4 | 95.9 |
| ... a month late | 97.1 | 96.9 | 95.6 |
| ... a month late, fat-tailed month (Student t, 3 df) | 97.3 | 96.9 | 95.7 |
| ... a quarter late | 95.6 | 95.3 | 94.7 |
| ... six months late | 93.6 | 93.0 | 93.7 |
| ... a year late (L-12's delayed-lock rule, on V47's design; L-12 ran V29's: 73.6%) | 90.9 | 89.8 | 92.1 |
| Wait while it rises (move after the first down week; median 2 weeks) | 97.6 | 97.4 | 95.9 |
| A quarter late, only after a top-fifth 2030 | 97.3 | 97.1 | 95.7 |
| Skipped after a top-fifth 2030 (all paths) | 95.4 | 94.9 | 94.6 |
| ... inside the skipped paths (v 98.5 / 98.6 / 96.4 had she moved) | 85.8 | 85.1 | 89.2 |
| Skipped everywhere (no lock at all) | 87.9 | 86.9 | 91.0 |
| **Move first, name a month / quarter / six months later** | **97.9** | **97.6** | **96.0** (identical, path for path) |
- Cheques short by more than $1,000: 0.03 / 0.03 / 0.05% in **every** arm. The quoted bottom: under 1 path in 20,000 in
  every arm (the arms report it rounded to 0.00%); counted exactly for the same-day arm, 0 / 0 / **1** of 200,000
  (S6). CORD (Kai, round 2): this line first said "never broken in any arm", which S6's one path contradicts.
- What a slip does to money: almost nothing to the average gift (-$8 for a month, -$29 for a quarter, S0); what it
  does is hand Laura the rises (+$80 / +$262 mean by 2042) and the co-sponsors the falls (the misses).
- 2030's top fifth averaged +36.5% for stocks (S0). Yearly draws have no memory in our model, so "after a boom" costs
  about what a skip at random costs, on a bigger promised half.

## B. Where the rival's lead sits (A09 matched to our $145k median bottom; lead = gift + Laura's 2042 money)
Mean lead $14,917 (S0), $15,399 (S1), $27,114 (S6). Rival ahead in 62.5 / 62.3 / 71.0% of paths.
| Fifth of 2028-30 stock markets (Jun's primary sort, set before the run) | S0 mean lead | share of the lead | rival ahead |
|---|---|---|---|
| 1 (worst) | -$27,896 | -37% | 1.2% |
| 2 | -$5,352 | -7% | 26% |
| 3 | +$11,069 | +15% | 86% |
| 4 | +$29,929 | +40% | 99% |
| 5 (best) | +$66,837 | **+90%** | 99.8% |
- S1 is the same within $3k a cell (best fifth +90%). **S6 differs:** best fifth +68%, fifth 2 +$1,737 (rival ahead).
- Sorted by 2028-32 stocks instead: best fifth carries 77.8 / 77.5 / 60.9%; worst fifth -$22k / -$23k / -$18k.
- Sorted by our plan's own outcome (Jun: "sorts on the answer"): the lead rises with her wealth, +$3.5k in her worst
  fifth to +$30.3k in her best (S0).
- When 2028-32 stocks beat the 2028 five-year Treasury yield (62% of paths), the rival is ahead 86% of the time by
  +$32k on average; when they don't, it is behind by $13.7k on average (ahead 24%). Same sign in 82% of paths.

## C. The miss, sized (V47, same day)
| | S0 | S1 | S6 |
|---|---|---|---|
| Top missed | 2.1% | 2.4% | 4.0% |
| Miss when missed: median / p90 / p99 / largest | $865 / $3,057 / $5,320 / $8,312 | $948 / $3,095 / $5,348 / $8,331 | $1,062 / $3,189 / $5,572 / $9,768 |
| Misses under $5,000 | 98.4% | 98.7% | 98.2% |
| Paths short of the top by more than $1,000 | 0.95% | 1.16% | 2.07% |
| **Inside the quoted range** (bottom to top) | 200,000 of 200,000 | 200,000 of 200,000 | 199,999 of 200,000 |

## Sealed guesses v the result
| Guess | Kai | Nora | Jun | Result (S0 unless stated) |
|---|---|---|---|---|
| Top reached, a month late | 97.5% | 95.4% | 97.4% | **97.1%** |
| Best fifth's share of the lead (2028-32 sort / 2028-30 sort) | 82% | 95% | 76% | **77.8% / 89.6%** |
| S6 median miss | $1,900 | $2,800 | $1,062 | **$1,062** |
Kai's bet ("A dies: a month's slip costs under 1 point"): a month costs 0.8 / 0.75 / 0.4 points. **Kai wins the bet.**
Nora's hypothesis for A (at least 3 points for a month) is **false**; B's holds in S0 and S1, fails in S6; C's holds
in all three.
