# FICTION (the room) + real work. L-01: one dial ($289 per 0.01%)

Run Sat 24 Oct 2026 (Sydney) by Jun; Kai roasted first. MODEL. Criterion: Portfolio Analysis; Creativity & Presentation.

1. **Hypothesis.** "The cost of Laura's ten payments moves about $289 for every 0.01% move in the 10-year yield"
   (DV01 $289/bp, 25 Sep curve, `CLAUDE.md` key facts) predicts the full repricing on every close since 24 Sep within $1,500.
2. **Kai's roast.** "One number for a curve that twists? The short end and the long end don't move together."
3. **Test.** `keel/scripts/ladder_history.py` (payment-date basis, bootstrapped) on all 20 U.S. closes 24 Sep-22 Oct
   (`assistant_review_2026-10/checks/tsy_202610_22oct.csv`). Prediction A: from the 24 Sep cost, -$289 x change in the
   10-year (bp). Prediction B: the same rule day on day. Wrong if any day misses by more than $1,500.
4. **Result.** A: worst miss **$652** (7 Oct), 22 Oct miss $452. B: worst miss **$269** (20 Oct); 22 Oct predicted
   $298,841 vs $298,861 actual ($20). The 10-year fell 17bp on 22 Oct and the cost rose $4,933; the rule said $4,913.
   Limits: one month of mostly parallel moves; the true DV01 drifts with the level ($289 -> $296 as yields fell), so
   for a 100bp fall the rule underestimates by about 1% (range model, deterministic -100bp: $333,197 holdings basis).
5. **Verdict: ADOPT** (for explaining, not for the IPS text, which carries no numbers): the whole promise has one dial
   a judge can follow. Kai's roast lost, and Kai wrote the verdict line himself.
