# The Genius Lab -> the rewrite, Mon 26 Oct 2026: WO-R1, the dedicated ladder in 200,000 paths

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Full write-up:
`../../rooms/lab/L-09_dedicated_ladder.md`; script `../lab/R01_mc.py`; results `../lab/R01_mc_results.json`.
MODEL, 15 Oct 2026 curve, the number sheet's 200,000 paths and seed.

For the synthesis memo (Thu 29 Oct):
1. **Dedication halves the coupon tail.** Shortfall p95 $25,112 -> $14,832, p99 $32,429 -> $17,584; rates fall 2
   points for good: $21,385 -> $9,616. Cost +$1,486 (R01 basis). The gain is the sizing: pooling coupons without
   re-sizing makes it worse (p95 $41,957).
2. **What is left.** $85,025 of coupons paid before 2033 waits in short Treasuries and pays most of 2033-35; the worst
   single-year gap is bounded at $7,923 (2033). In 9% of paths dedication ends shorter (rates fall early, then rise).
3. **Price beyond dollars.** Longer ladder (8.6 vs 7.7 yrs), and the chance the 2028 deposit must top it up rises
   from 41% to 47% (1pp/yr walk to 1 Jan).
4. **WInS.** Mirroring it needs ~10 trades, ~$52k each way (17% of the book), before the freeze. Keel default: no
   trades; Caplet asked (ASK_HUMANS); Courtroom rules on coherence (WO-R2).
5. **One true line** (cold panel, three judges): "We size the ladder from 2042 backwards, so every coupon pays a named
   payment and a fall in rates has less to spoil." Binned: "every coupon is a dose, not a leak" (AI template, false).
   Investing idea underneath (north star 4, uncited in the IPS): cash-flow dedication beats rung-by-rung matching
   on reinvestment risk; the Final Report can name the technique.
