# D6: what share of the stock fund Laura promises in 2031

WS2, 30 Sep 2026. AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws2.md`; the Book L check in s9 was run
on both builds). Keys: `rab/numbers_ws2.yaml` (W), `rab/numbers.yaml` (N).

**Decision: keep half.** Ratify at the 26 Oct meeting. IPS: no change.

**Question.** In 2031 the top of the range is the floor plus a share of the stock fund (about $41,000 in 2028,
N `laura.stock_fund_2028_usd.strips`). The 2033 gift is capped at that top, and Laura keeps the rest. Is half right?

**Options** (low to high across three return models: fat tails, history, uncertain mean; W `ws2.d6.options`)

| Share promised | Expected gift | Laura keeps at least 10% of her gift | She keeps, in a 1-in-20 bad case |
|---|---|---|---|
| 1/3 | about $166k | 98-99% of paths | about $21k-$22k |
| 0.47 (rule's exact answer) | about $173k | 95-97% | about $16k-$18k |
| **1/2 (adopted)** | **about $174k** | **93-95%** | **about $15k-$17k** |
| 2/3 | about $183k | 69-71% | about $10k-$11k |
| all | about $199k | 17-21% | $0 |

**Evidence**
- **The rule was fixed before any result** (`M4_SPEC.md` s5, commit 3d98ce0):
  - the gift stays above the announced $145,000 in 99.5% of paths;
  - Laura keeps at least 10% of her gift in 95% of paths (about three years of Taiwan building-cost rises);
  - take the largest share that passes in all three models;
  - change "half" only if that share falls outside 0.40-0.60.
- **Result.** The largest passing share is 0.50, 0.47 and 0.47, so the robust answer is 0.47 (W `ws2.d6.s_star`),
  confirmed by the blind rebuild and 10 more seeds.
- **More promised does not mean more broken promises.** No path puts the gift below $145,000 at any share
  (W `ws2.d6.p_gift_below_145k_any_share`). The share only moves the upside between the building and Laura's cushion.
- **Half sits at the edge.** It adds about $1,500 of expected gift over 0.47 (W `ws2.d6.half_vs_047_expected_gift`).
  It passes the 10% test only under fat tails (93-94% in the other two models). The 0.40-0.60 band stops a 0.03 gap
  from replacing a rule co-sponsors can follow.

**Decision.** Keep half. It is the simple share nearest the rule's answer, it never breaks the promise, and it matches
the IPS: "The other half remains with Laura as a cushion".

**Confidence.** High that the rule gives half on its own zero-coupon basis (two builds, 11 seeds). Medium for the
WInS-listed ladder that our rule reading requires (`rab/assumptions.md` R1): it gives half at today's yields, but only
just. Medium on the rule itself: "10% in 95% of cases" is a value judgement, not a fact about Laura.

**What would change it**
- **Coupons on Laura's real ladder** (WS7 red team; W `ws2.d6.ladder_gap`, `ws2.d6.ladder_gap_tolerance`; a check
  added after the rule, run on both builds). The rule assumes zero-coupon STRIPS: nothing to reinvest. Under R1 her
  real ladder is Book L, which pays coupons, and any reinvestment shortfall comes out of her cushion.
  - At today's yields the gap is about $1,600. The rule still keeps half (robust share 0.42).
  - The rule keeps half for gaps up to about $2,400.
  - At yields 2 points lower, the gap is about $18,000. No share passes, not even zero, which covers about $15,000 at
    most. The fix belongs in the ten holdings (Gate D), not in the share.
- **Laura's cushion** (W `ws2.d6.rule_sensitivity`). A 5% cushion gives 2/3. A 15% cushion gives 1/5, and so does 10%
  at 99% confidence. The stock model barely matters.
- **Costs** over 1% a year, or any cost charged to the floor.
- **Stocks and yields falling together.** This is not modelled (WS3/M7).
- **Counting the top from $145,000** (range memo, option D): half would pass the 10% test in every model (96-97%, primary build only).

**Implications**
- **IPS: none from D6.** Coupon reinvestment is already a fix-before-6-Nov item (Gate A; `rab/assumptions.md` C3): the
  IPS phrase "needs no rebalancing". Gate D owns it.
- **Final Report: note-in-Final-Report.** Use the options table as the reason for half. Raise the cushion as the
  question to ask Laura. Say that half still holds with the WInS-listed ladder at today's yields, but not if coupons
  earn much less.
- **Trading Notes.** Keep shares, odds and ranges out of WInS notes. The VT note may say in words that only half the
  stock fund is ever promised.

Version 3: adds the Book L check (re-derives WS7's figures). Version 2 corrected "19 in 20 at half" to 93-95%.
