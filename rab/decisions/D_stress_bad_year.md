# Stress: what a bad year does, and Laura's bad-year clause

WS3, 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws3.md`). Keys: `rab/numbers_ws3.yaml`
(W) `ws3.stress.*`, `rab/numbers.yaml` (N), WS2's `rab/numbers_ws2.yaml` (W2). Results: `rab/results/M7/`, `M5/`.

**Question.** The case asks teams to "explain how favorable and unfavorable market outcomes could affect" the gift.
What can a bad year do to the payments, the floor and the gift, and what should Laura do when one comes?

**Options.** (A) Hold everything; the adopted rules work. (B) Cut risk after a fall. (C) Buy stocks after a fall with
floor money. (D) Sell Treasuries whose prices fell. (E) Hedge before January 2027 (WS4 memo: do not hedge).

**Evidence.**
- **Payments, STRIPS basis** (zero-coupon, as M5-M7 model them): paid in all 13 replayed episodes and all 149 start
  years at today's yields; at risk only after a fall of more than about 4.3 points (428bp) before investing.
- **Yields fall before investing.** Beyond 26bp the 2028 deposit finishes the payments (N
  `laura.ladder.breakeven_fall_bp_strips`); up to 109bp the floor stays $150,000. Worst replay: Japan plus a 1-point
  fall leaves a floor of $147,189 and no fund.
- **Yields fall after investing** (outside M5-M7). The WInS book's income must be reinvested: the ten holdings deliver
  about $503,000 at today's yields, $466,000 at 2%, $447,000 at 0% (N `reinvest.bookL_delivered`). A 2007-style
  replay leaves them about $24,000 short with coupons matched to payments, $49,000 in bills (WS7, one build, W `ws3.external`).
- **Stocks and yields often fall together**, when Laura's half is smallest. Last column: WS2's 2% coupon gap valued in
  2033 (about $30,000, W2 `ws2.d6.ladder_gap`, both builds) less M7's kept half, paired by hand (W
  `ws3.stress.coupon_gap_vs_laura_half`; M7 has no coupons).

| Episode replayed from 2028 | 2031 range | 2033 gift | Laura keeps | Coupons at 2%: gap beyond her half |
|---|---|---|---|---|
| Base (JPM 7% stocks) | $150k-$175k | $174,952 | $32,183 | none |
| 2008 happens in 2028 | $150k-$164k | $164,302 | $18,446 | $12,047 |
| Japan 1990-95 (falls again after 2031) | $150k-$163k | $161,659 | $11,659 | $18,834 |
| Great Depression 1928-33 | $150k-$159k | $159,298 | $17,333 | $13,160 |

  With yields 2 points lower instead (gap about $18,000) only Japan (about $6,300) and 1929 (about $700) exceed her
  half; at today's yields (about $1,600) none does.
- **Against B:** CPPI, which sells after falls, has less typical 2033 money ($199k against $207k) and misses the $150k
  in 2.0% of paths. **C** makes the quoted bottom uncertain. **D** changes nothing: a held Treasury pays in full.
- **Inflation** stays with Laura: at the market's 2.34% the 2042 payment buys what $35,342 buys in 2027; in a
  1970s-style decade, $18,414.

**Decision: option A. In a bad year Laura sells nothing**, as a six-line clause (the team chooses the words):
1. Never sell in a bad year: Treasuries are held to maturity and the fund to 2033.
2. Each bond's coupons buy a Treasury maturing before the same payment: not bills, not stocks (halves the 2007 gap).
3. One order for any payment shortfall: Laura's half first, then the gift above the floor, then the floor. In 2031,
   value the holdings against the payments and lower the range's top by any gap her half cannot cover. From the 2033
   gift to the last payment she holds her half in Treasuries, not stocks; beyond it, she adds her own money.
4. Stocks fall: before 2031 the range narrows, its bottom fixed; after 2031 the gift slides toward the floor, never
   below it, and Laura's half takes the rest.
5. Yields fall before investing: buy at once, latest payments first; the 2028 deposit completes the payments, then the
   floor; the stock fund gets what is left.
6. Inflation: the payments stay $50,000 as promised; Laura's half, not the payments or the floor, meets higher costs.

Rule 3 (was "fill the gap from the whole fund") gives one first owner before and after 2033, as WS2's range memo
(condition 5) and WS6's IBTM_R do.

**Confidence.** High on the payments (STRIPS basis) and the bottom: both builds agree to the cent. Medium on the
coupons: the gaps are locked (N `reinvest.*`) and built twice (WS2), but their pairing with episodes is by hand.
Medium on the gifts: parallel yield moves, a world fund fixed at 62% U.S., annual steps.

**What would change it.** A fall of more than about 1 point before January 2027 (smaller floor; the clause stands).
Coupons near 2% for years in a bad stock market: rule 3 then reaches the gift or Laura's own money. Keeping every
payment whole at 2% costs about $20,000 more of the same holdings today (N `reinvest.bookL_buffer_cost`), above the
$7,582 headroom: a Gate D question for the holdings (lower coupons, or part of the 2028 fund), not for this clause.
A U.S. payment delay beyond the 47 days from 15 Nov to 1 Jan (UNVERIFIED for iBond ETFs). Fees charged to the floor.

**Implications.**
- **IPS: fix-before-6-Nov (wording only).** Rules 1-2 join the Gate A fix of "needs no rebalancing" (about 8 words).
  Rule 3 adds 3: "a cushion if coupons earn less, costs rise or co-sponsors fall short". 17 words are spare (483 of
  500), shared with WS2's items. The coupon caveat on "depends essentially on the US government" is WS7's triage.
- **Final Report: note-in-Final-Report.** The stress table with its coupon column, real values, rule 3, and "STRIPS
  basis" on every "never short" figure. Rules 3-4 are the co-sponsor message.
- **Trading Notes:** a stock fall triggers no trade. The only bad-year trade is WS6's October trigger B (payments cost
  over $300,000: part of VT moves into IBTM), i.e. rule 5. Low-coupon swaps (SW40/SW41) shrink the coupon gap. IBTM_R
  names Laura's half as the first cover, never as covering "any gap" (false at 2%). Never write that a Treasury
  "cannot fall in price" or a payment is guaranteed; write that it pays in full at maturity.
