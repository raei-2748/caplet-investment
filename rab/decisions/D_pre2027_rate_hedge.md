# Pre-2027 rate hedge: hedge or not?

WS4, 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws4.md`). Keys: `rab/numbers_ws4.yaml`
(W), `rab/numbers.yaml` (N); results `rab/results/M2/m2_results.json`.

**Decision: do not hedge.** Buy all ten holdings at once on the first trading day of 2027 (Mon 4 Jan; 1 Jan is a
bond-market holiday), latest payments first; any shortfall is the first call on the 2028 deposit. No hedge trade in WInS.

**Question.** Laura's $300,000 arrives in January 2027. If yields fall first, the ten holdings cost more. Should she,
or our WInS book, act now?

**Options.**

| Option | Verdict |
|---|---|
| A. Nothing now; buy at once, latest first; the 2028 deposit completes any gap (the IPS design) | **Chosen** |
| B. Lock prices with futures, a forward purchase, swaps or options | Out: derivatives are banned in WInS and, under our reading of "for BOTH contributions" (`assumptions.md` R1), in her real plan |
| C. Borrow now, buy early, repay from the 2027 deposit | Out: margin and borrowing banned; no money in or out except the two deposits |
| D. Ask Laura to deposit early | Out: the case fixes the dates |
| E. Wait or stage purchases in 2027 for better yields | Rejected: a rate bet; insight_v1 found no reliable gain (D1 [7], 25 Sep, not re-checked) |
| F. WInS: a long-bond fund "as a hedge" | Rejected: WInS money is not Laura's; the book shows the plan after both deposits, scaled (IPS) |

**Evidence.**
- Cost on 1 Jan 2027: about $292,000 if forward rates come true, leaving about $7,600 of room; a fall of about 26bp
  uses it up (N). With yields unchanged: about $293,000 and 23bp (W).
- Chance it costs more than $300,000: **about 1 in 3** (median of five methods, roughly 25-35%); a 4 Jan purchase
  too (W).
- If short, typically about $10,000; about $18,000 or more in 1 path in 20; a whole payment waits under 0.3% (W).
- The gap lands on the stock fund, not the payments: on 1 Jan 2028 typically about $41,000, under $20,000 in about
  1 path in 6 (W). Even a 1.5-point fall needs only about $40,000 of the $150,000 deposit (W).
- Payments are at risk from the price only if rates fall *and* the 2028 deposit never comes (our stress case): after
  a 1-point fall, about $29,000 of the 2033 payment is unfunded (W).
- Basis: these figures are for zero-coupon STRIPS. Under our rule reading (`assumptions.md` R1) Laura's real ladder
  is the WInS-listed one (Book L: five iBonds ETFs, five coupon bonds). It costs about $292,900 today with commission,
  against about $289,000 for STRIPS (N), so its odds are likely higher (not computed). A lasting fall also cuts what
  its coupons earn: about $20,000 more today keeps every payment whole if coupons earn only 2% (N
  `reinvest.bookL_buffer_cost`). No allowed trade hedges this either; see the coupon fix under Implications.
- A perfect hedge fixes about $292,000; with no view on rates the expected price is about $293,000, so it gains $0 to
  about $1,000 in expectation (W) and gives away the fund's upside if rates rise.
- The rate move is settled by January 2028, three years before the 2031 range: it sizes the range but cannot break a promise.

**Decision.** Option A. The plan's hedge is its order of operations, not a trade: at once, latest first, 2028 deposit
completes the ladder before any stocks, range announced only after both purchases are known.

**Confidence.** High on the decision (every hedging tool is outside the rules; the design absorbs the risk). Medium on
the odds: a three-month figure that moves with volatility (MOVE 101.8 on 28 Sep, 106.3 on 29 Sep; W), on a STRIPS
basis; Book L's odds are not computed and likely higher. The decision does not depend on the exact figure.

**What would change it.** (1) Wharton says the investment limits do not bind her real plan *and* the 2028 deposit
becomes doubtful: a futures hedge would then protect payments, not just the fund (Final Report discussion; no
strategy change). (2) Friday's curve (M2 `--curve-date`) is more than about 26bp lower: a gap becomes likely; the
decision stands, but re-run the range and fund figures.

**Implications.**
- **IPS: none from this memo.** It already says the January 2027 deposit buys "latest payments first" and a fall
  leaves payments "for the 2028 deposit to complete". Optional: add "at once". Keep the odds out. The coupon wording
  ("needs no rebalancing") is already fix-before-6-Nov (Gate A; `assumptions.md` C3; `D_stress_bad_year.md`), with
  the cost of a coupon buffer as a Final Report note.
- **Final Report: note-in-Final-Report.** One paragraph, "Why Laura does not hedge before January 2027": the rules, about
  1 in 3 for a zero-coupon ladder (likely higher for the WInS-listed one), typically about $10,000 from the 2028
  deposit, range announced after the risk has passed.
- **Trading Notes:** no hedge trade; no note says WInS trades lock in Laura's 2027 prices; no odds or gap figure in a
  WInS note. The note on the latest rung (the 15-Nov-2041 bond, for the 2042 payment) can say "latest payments first".
