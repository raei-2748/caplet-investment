# D6: what share of the stock fund Laura promises in 2031

WS2, 30 Sep 2026. AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (`rab/gates/gate_B_ws2.md`). Keys: `rab/numbers_ws2.yaml`
(W), `rab/numbers.yaml` (N).

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
- **Result.** The largest passing share is 0.50, 0.47 and 0.47, so the robust answer is 0.47 (W `ws2.d6.s_star`). The
  blind rebuild and 10 more seeds agree.
- **More promised does not mean more broken promises.** No path puts the gift below $145,000 at any share
  (W `ws2.d6.p_gift_below_145k_any_share`). The share only moves the upside between the building and Laura's cushion.
- **Half sits at the edge.** It adds about $1,500 of expected gift over 0.47 (W `ws2.d6.half_vs_047_expected_gift`).
  It keeps a tenth in 95% of paths under fat tails, but in 93-94% under the other two models. The band stops a 0.03
  gap from replacing a rule co-sponsors can follow.

**Decision.** Keep half. It is the simple share nearest the rule's answer, it never breaks the promise, and it matches
the IPS: "The other half remains with Laura as a cushion".

**Confidence.** High that the rule gives half (two builds, 11 seeds). Medium on the rule itself: "10% in 95% of
cases" is a value judgement, not a fact about Laura.

**What would change it**
- **Laura's cushion** (W `ws2.d6.rule_sensitivity`). A 5% cushion gives 2/3. A 15% cushion gives 1/5, and so does 10%
  at 99% confidence. The stock model barely matters.
- **Costs** over 1% a year, or any cost charged to the floor.
- **Stocks and yields falling together.** This is not modelled (WS3/M7).
- **Counting the top from $145,000** (range memo, option D). Half would then pass the 10% test in every model, at
  96-97% (primary build only).

**Implications**
- **IPS: none.**
- **Final Report: note-in-Final-Report.** Use the options table as the reason for half, and raise the cushion as the
  question to ask Laura.
- **Trading Notes.** Keep shares, odds and ranges out of WInS notes. The VT note may say in words that only half the
  stock fund is ever promised.

Replaces this memo's first version. Two corrections: "19 in 20 at half" becomes 93-95%, and the untraced "3 to 5
history paths below $150,000" is dropped.
