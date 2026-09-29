# Stated confidence for the 2031 range

WS2, 30 Sep 2026. AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled. Keys: `rab/numbers_ws2.yaml` (W), `rab/numbers_ws4.yaml`
(W4, on `rab/integration`).

**Decision.** Say the 2033 gift lands inside the range **by construction, if four things hold**, and add where in the
range it will probably land. Quote the bottom as **the floor holding's worst case, rounded down to $5,000** ($145,000
today).

**Question.** The case asks the team to "state how confident" it is that the 2033 contribution falls within the 2031
range. What should the team say?

**Options**

| Option | Verdict |
|---|---|
| A. A model percentile ("90% sure of $165k-$190k") | Rejected: the ends are an owned bond and Laura's own cap, so a model cannot add to *whether* the gift lands inside (PM-25) |
| B. "Cannot fall outside", floor quoted at $150,000 face | Rejected: the iBond-fund floor pays under $150,000 about 2 times in 3 |
| C. "By construction, if...", with the floor rounded down, plus where the gift lands | **Chosen** |
| D. As C, top also counted from $145,000 | Not chosen (not pre-registered): top reached about 9 in 10 instead of 3 in 4, gift about $3,500 lower on average (W `ws2.range.option_top_from_145k`); a Final Report option |

**Evidence**
- **The floor.** It pays about $149,000 in a typical case and at least about $146,000 (W `ws2.range.floor_delivery`).
  Rounding down to $145,000 covers the worst shortfall, about $3,700 (W `ws2.range.floor_shortfall_vs_face`).
- **Inside the range.** No gift fell outside the range in 1.6 million paths (W `ws2.range.gift_inside_range`), and
  none fell below $145,000 (W `ws2.d6.p_gift_below_145k_any_share`).
- **Where the gift lands.**
  - About 3 times in 4, the gift is at the top or within about $3,700 of it (W `ws2.range.p_fund_holds_2031_to_2033`).
  - On average it is about $2,000 below the top (W `ws2.range.expected_short_of_top`).
  - It falls below the middle at most about 1 time in 200 (W `ws2.range.p_below_middle`).
- **Today's dollar projection** (Final Report, not a promise). The typical top is about $175,000, and 90% of paths lie
  between about $165,000 and $190,000 (W `ws2.range.top2031`). Yields at the January 2027 purchase move the typical
  top from about $143k to $194k (W `ws2.assume.tornado_median_top`, IPS floor reading).

**Decision.** Option C. The four conditions:
1. The floor holding pays at least the quoted bottom. It is Treasuries in an iBond fund, and the bottom is rounded down.
2. The 2028 deposit has arrived. This is known before 2031.
3. The gift is capped at the top. This is Laura's rule.
4. No cost comes out of the floor; costs come from the stock fund.

By 2031 only condition 1 still depends on markets. The statement holds under either floor reading (flag F4), because
the floor is known before the range is announced. F4 only decides who absorbs a pre-2027 fall in yields: the facility
floor or Laura's stock fund (W `ws2.range.floor_reading`). F4 stays the team's pick.

**Confidence**
- **High that the gift lands inside the range.** Three of the conditions are policy or known facts. The fourth rests on
  Treasuries, plus the small risk that an iBond fund closes early or drifts (`rab/assumptions.md` C5).
- **Medium on where it lands.** The three models agree, but they share assumptions that have not been tested: U.S.
  history stands in for VT, and stocks move independently of yields.
- **Low to medium on today's dollar projection.** The ladder costs more than $300,000 on 1 Jan 2027 in about 1 case in
  3 (W4 `ws4.gap_odds_2027`).

**What would change it**
- **The iBond fund closes early or drifts.** Re-quote from the holding and round down again.
- **A cost is charged to the floor, or the 2028 deposit fails to arrive.**
- **The curve moves.** Friday's curve and the January 2027 yields change the numbers, not the statement. Re-run WS2
  on Friday.

**Implications**
- **IPS: fix-before-6-Nov (the team words both edits).**
  - Add "rounded down" where the IPS says Laura quotes the floor. This keeps "cannot fall outside it" true.
  - Settle F4 in the same sentence.
- **Final Report: note-in-Final-Report.** Cover the four conditions, where the gift lands, today's projection with the
  yield caveat, and option D.
- **Trading Notes.** The IBTM note must pass the PM-14 word check: no fixed-repayment or certainty claims. It may say
  that IBTM also carries Laura's facility floor. Put no range, odds or $145,000 in a WInS note.
