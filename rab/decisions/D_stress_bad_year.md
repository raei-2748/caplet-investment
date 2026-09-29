# Stress: what a bad year does, and Laura's bad-year clause

WS3, 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws3.md`). Keys: `rab/numbers_ws3.yaml`
(W) `ws3.stress.*`, `rab/numbers.yaml` (N). Results: `rab/results/M7/`, `rab/results/M5/`; card `rab/models/M7_CARD.md`.

**Decision: in a bad year Laura does nothing.** Nothing is sold and no money moves between the floor and the stock
fund; the adopted rules absorb the year. Written below as a five-line bad-year clause.

**Question.** The case asks teams to "explain how favorable and unfavorable market outcomes could affect" the gift.
What can a bad year do to the payments, the floor and the gift, and what should Laura do when one comes?

**Options.** (A) Hold everything; the adopted rules work. (B) Cut risk after a fall. (C) Buy stocks after a fall with
floor money. (D) Sell Treasuries whose prices fell. (E) Hedge before January 2027 (WS4 memo: do not hedge).

**Evidence.**
- **Payments:** paid in all 13 replayed episodes and all 149 start years at today's yields. A payment is at risk only
  if yields fall more than about 4.3 points (428bp) before the money is invested.
- **The one bad year that reaches the bottom** is a fall in yields before the money is invested. Beyond 26bp the 2028
  deposit finishes the payments (N `laura.ladder.breakeven_fall_bp_strips`); up to 109bp the stock fund pays and the
  floor stays $150,000. The worst of the 13 replays, Japan plus a 1-point fall, leaves a floor of $147,189 and no fund.
  A 2011-style downgrade rally (-56bp) would lift the ladder to $308,897 and cut the fund to $20,357.
- **Bad years after the floor is bought** only move the gift inside the range; Laura's kept half takes half the fall.

| Episode replayed from 2028 | 2031 range | 2033 gift | Laura keeps |
|---|---|---|---|
| Base (JPM 7% stocks) | $150k-$175k | $174,952 | $32,183 |
| 2008 happens in 2028 | $150k-$164k | $164,302 | $18,446 |
| Japan 1990-95 (falls again after 2031) | $150k-$163k | $161,659 | $11,659 |
| Great Depression 1928-33 | $150k-$159k | $159,298 | $17,333 |

  At today's yields the worst gift in 149 start years is $158,969 (fund bought in 1929).
- **Against B:** CPPI, the rival that sells after falls, ends with less typical 2033 money ($199k against $207k) and
  misses the $150k in 2.0% of paths (W `ws3.rivals.R5`). **C** makes the quoted bottom uncertain. **D** changes nothing:
  a held Treasury pays in full whatever its price did.
- **Inflation** is the risk left with Laura: at the market's 2.34% the 2042 payment buys what $35,342 buys in 2027; in
  a 1970s-style decade, $18,414.

**Decision: option A, as a bad-year clause** (the rules; the team chooses the words):
1. Never sell in a bad year: Treasuries are held to maturity and the fund to 2033; only coupons are reinvested.
2. Stocks fall before 2031: the range is set from the fund's value then. It is narrower; its bottom does not move.
3. Stocks fall after 2031: the gift slides toward the floor, never below it; Laura's half takes the rest of the fall.
4. Yields fall before the money is invested: buy at once anyway, latest payments first; the 2028 deposit completes the
   payments, then the floor; the stock fund gets what is left.
5. Inflation: the payments stay $50,000 as promised; Laura's kept half, not the payments or the floor, meets higher costs.

**Confidence.** High on the payments and the bottom (held Treasuries; deterministic; both builds agree to the cent).
Medium on the gifts (parallel yield moves, a world fund fixed at 62% U.S., annual steps, a STRIPS-style floor; WS2's D6
memo finds a coupon floor typically pays slightly under $150,000).

**What would change it.** A fall of more than about 1 point before January 2027 (the range starts from a smaller floor;
the clause stands). A U.S. payment delay beyond the 47 days between the 15 Nov maturities and the 1 Jan payments (not
modelled; UNVERIFIED for the iBond ETFs). Fees charged to the floor.

**Implications.**
- **IPS: fix-before-6-Nov (wording only).** It gives the outcome ("A market decline can reduce the facility contribution,
  but not below the floor") but not rule 1. Merge rule 1 into the Gate A fix of "needs no rebalancing" (coupons are
  reinvested), in about 15 words: the 30 Sep text has 483 words, 17 spare, shared with WS2's items. Rules 2-5 are there.
- **Gate B open items** ("certain by construction if..."; inflation as Laura's risk): the 30 Sep IPS covers both
  ("cannot fall outside it"; "Inflation leaves the fixed payments unchanged but ... erodes the floor's real value"), so
  they drop to **note-in-Final-Report**, with the stress and real-value tables. Rules 2-3 are the co-sponsor message for
  "varying outcomes": the bottom is already owned; a bad market moves the gift only toward it.
- **Trading Notes:** a stock fall triggers no trade (no selling or buying VT after a drop). The only bad-year trade is
  WS6's October trigger B (yields fall so the ten payments cost more than $300,000: part of VT moves into IBTM), i.e.
  rule 4. Never write that a Treasury "cannot fall in price"; write that it pays in full at maturity.
