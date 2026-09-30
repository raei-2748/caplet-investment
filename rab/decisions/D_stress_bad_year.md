# Stress: what a bad year does, and Laura's bad-year clause

WS3, 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws3.md`). Keys: `rab/numbers_ws3.yaml`
(W) `ws3.stress.*`, `rab/numbers.yaml` (N). Results: `rab/results/M7/`, `rab/results/M5/`; card `rab/models/M7_CARD.md`.

**Question.** The case asks teams to "explain how favorable and unfavorable market outcomes could affect" the gift.
What can a bad year do to the payments, the floor and the gift, and what should Laura do when one comes?

**Options.** (A) Hold everything; the adopted rules work. (B) Cut risk after a fall. (C) Buy stocks after a fall with
floor money. (D) Sell Treasuries whose prices fell. (E) Hedge before January 2027 (WS4 memo: do not hedge).

**Evidence.**
- **Payments, STRIPS basis** (zero-coupon Treasuries, as M5-M7 model them): paid in all 13 replayed episodes and all 149
  start years at today's yields; at risk only if yields fall more than about 4.3 points (428bp) before investing.
- **Yields fall before the money is invested.** Beyond 26bp the 2028 deposit finishes the payments (N
  `laura.ladder.breakeven_fall_bp_strips`); up to 109bp the stock fund pays and the floor stays $150,000. Worst of 13
  replays: Japan plus a 1-point fall leaves a floor of $147,189 and no fund. A 2011-style downgrade rally (-56bp) lifts
  the ladder to $308,897 and cuts the fund to $20,357.
- **Yields fall after the money is invested** (outside M5-M7). The WInS book holds coupon bonds and iBond ETFs whose
  coupons must be reinvested. WS7 (W `ws3.external`, MODEL, not Gate-B checked): the payments total the full $500,000
  only if coupons earn about 4.97% or more; a 2007-style fall leaves them about $24,000 short in total if each coupon
  buys a Treasury dated to its payment, about $49,000 if coupons sit in 1-year bills.
- **Stocks fall after the floor is bought:** the gift moves only inside the range; Laura's kept half takes half the fall.

| Episode replayed from 2028 | 2031 range | 2033 gift | Laura keeps |
|---|---|---|---|
| Base (JPM 7% stocks) | $150k-$175k | $174,952 | $32,183 |
| 2008 happens in 2028 | $150k-$164k | $164,302 | $18,446 |
| Japan 1990-95 (falls again after 2031) | $150k-$163k | $161,659 | $11,659 |
| Great Depression 1928-33 | $150k-$159k | $159,298 | $17,333 |

  At today's yields the worst gift in 149 start years is $158,969 (fund bought in 1929).
- **Against B:** CPPI, which sells after falls, ends with less typical 2033 money ($199k against $207k) and misses the
  $150k in 2.0% of paths. **C** makes the quoted bottom uncertain. **D** changes nothing: a held Treasury pays in full.
- **Inflation** stays with Laura: at the market's 2.34% the 2042 payment buys what $35,342 buys in 2027; in a
  1970s-style decade, $18,414.

**Decision: option A. In a bad year Laura sells nothing**, written as a six-line clause (the team chooses the words):
1. Never sell in a bad year: Treasuries are held to maturity and the fund to 2033.
2. Each bond's coupons buy a Treasury maturing before the same payment: not bills, not stocks (halves the 2007 gap).
3. In 2031, first value the dated holdings against the ten payments at that day's prices and fill any gap from the stock
   fund; then set the range from the fund that is left. After a stock fall it is narrower; its bottom does not move.
4. Stocks fall after 2031: the gift slides toward the floor, never below it; Laura's half takes the rest of the fall.
5. Yields fall before the money is invested: buy at once anyway, latest payments first; the 2028 deposit completes the
   payments, then the floor; the stock fund gets what is left.
6. Inflation: the payments stay $50,000 as promised; Laura's kept half, not the payments or the floor, meets higher costs.

**Confidence.** High on the payments (STRIPS basis) and the bottom: deterministic, both builds agree to the cent. Medium
on the coupons: WS7's check is one build. Medium on the gifts: parallel yield moves, a world fund fixed at 62% U.S.,
annual steps; WS2's D6 memo finds a coupon floor typically pays slightly under $150,000.

**What would change it.** A fall of more than about 1 point before January 2027 (smaller floor; the clause stands). A
coupon gap larger than the 2031 fund (rule 3's bottom would then move). A U.S. payment delay beyond the 47 days between
the 15 Nov maturities and the 1 Jan payments (UNVERIFIED for the iBond ETFs). Fees charged to the floor.

**Implications.**
- **IPS: fix-before-6-Nov (wording only).** Merge rules 1-2 into the Gate A fix of "needs no rebalancing" (about 8 more
  words: nothing is sold after a fall; coupons buy Treasuries dated to the same payment). The 30 Sep text has 483
  words, 17 spare, shared with WS2's items. Whether "depends essentially on the US government" needs the coupon caveat
  is WS7's triage. Rules 3-6 fit the IPS as written ("not below the floor"; inflation "erodes the floor's real value").
- **Final Report: note-in-Final-Report.** The stress and real-value tables; rule 3 as how the range "protects" the
  payments; "STRIPS basis" on every "never short" figure. Rules 3-4 are the co-sponsor message for varying outcomes.
- **Trading Notes:** a stock fall triggers no trade (no selling or buying VT after a drop). The only bad-year trade is
  WS6's October trigger B (the ten payments cost more than $300,000: part of VT moves into IBTM), i.e. rule 5. WS6's
  trigger D (a low-coupon 2040 bond) shrinks the coupon gap and waits for the IPS coupon wording above. Never write
  that a Treasury "cannot fall in price" or that a payment is guaranteed; write that it pays in full at maturity.
