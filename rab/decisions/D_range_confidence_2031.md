# Stated confidence for the 2031 range

WS2, 30 Sep 2026. AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled (coupon checks: `gate_B_ws2.md` s9-s10). Keys:
`rab/numbers_ws2.yaml` (W), `rab/numbers_ws4.yaml` (W4, on `rab/integration`).

**Decision.** Say the 2033 gift lands inside the range **by construction, if five things hold**, and add where in the
range it will probably land. Quote the bottom as **the floor holding's worst case, rounded down to $5,000** ($145,000
today).

**Question.** The case asks how confident the team is that the 2033 contribution falls within the 2031 range.

**Options**

| Option | Verdict |
|---|---|
| A. A model percentile ("90% sure of $165k-$190k") | Rejected: the ends are an owned bond and Laura's cap, so a model adds nothing to *whether* the gift lands inside (PM-25) |
| B. "Cannot fall outside", floor quoted at $150,000 face | Rejected: the iBond-fund floor pays under $150,000 about 2 times in 3 |
| C. "By construction, if...", floor rounded down, plus where the gift lands | **Chosen** |
| D. As C, top also counted from $145,000 | Not pre-registered: top reached about 9 in 10 (not 3 in 4), gift about $3,500 lower on average (W `ws2.range.option_top_from_145k`). Final Report option |

**Evidence**
- **The floor** pays about $149,000 typically and at least about $146,000 (W `ws2.range.floor_delivery`). Rounding
  down to $145,000 covers the worst shortfall, about $3,700 (W `ws2.range.floor_shortfall_vs_face`).
- **Inside the range.** No gift fell outside the range in 1.6 million paths (W `ws2.range.gift_inside_range`), and
  none fell below $145,000 (W `ws2.d6.p_gift_below_145k_any_share`).
- **Coupons.** Under rule reading R1 (`rab/assumptions.md`) Laura's ladder is Book L, which pays coupons. The stock
  fund fills any shortfall in 2031, before the range is set (D6 v4), so the range allows for it. The gift falls below
  $145,000 never at today's yields, at most 1 path in 400 at yields 2 points lower, and 1-2% of paths at 2%; the
  fund is smaller than the shortfall never, at most 1 in 150, and 3-4% (W `ws2.d6.gap_owner`, both builds).
- **Where the gift lands.**
  - About 3 times in 4, the gift is at the top or within about $3,700 of it (W `ws2.range.p_fund_holds_2031_to_2033`).
  - On average it is about $2,000 below the top (W `ws2.range.expected_short_of_top`).
  - It falls below the middle at most about 1 time in 200 (W `ws2.range.p_below_middle`).
- **Today's projection** (Final Report, not a promise). Typical top about $175,000; 90% of paths about $165,000 to
  $190,000 (W `ws2.range.top2031`). January 2027 yields move the typical top from about $143k to $194k
  (W `ws2.assume.tornado_median_top`); coupons 2 points lower take about $8,500 off it (W `ws2.d6.gap_owner`).

**Decision.** Option C. The five conditions:
1. The floor holding pays at least the quoted bottom. It is Treasuries in an iBond fund, and the bottom is rounded down.
2. The 2028 deposit has arrived. This is known before 2031.
3. The gift is capped at the top. This is Laura's rule.
4. No cost comes out of the floor; costs come from the stock fund.
5. Any coupon shortfall on the ten holdings is smaller than the stock fund, which fills it before the floor (D6 v4
   owner chain; none arises with zero-coupon STRIPS).

By 2031 only conditions 1 and 5 depend on markets, and condition 5 is measured before the range is announced. The
statement holds under either floor reading (flag F4): F4 only decides whether the floor or Laura's
stock fund absorbs a pre-2027 fall in yields (W `ws2.range.floor_reading`). F4 stays the team's pick.

**Confidence**
- **High that the gift lands inside the range.** Conditions 2-4 are policy or known facts. Condition 1 rests
  on Treasuries, plus the small risk that an iBond fund closes early or drifts (`rab/assumptions.md` C5). Condition 5
  fails only if coupons earn far below today's yields for years.
- **Medium on where it lands.** The three models agree but share untested assumptions: U.S. history stands in for
  VT, and stocks move independently of yields.
- **Low to medium on today's dollar projection.** The ladder costs more than $300,000 on 1 Jan 2027 in about 1 case in
  3 (W4 `ws4.gap_odds_2027`).

**What would change it**
- **The iBond fund closes early or drifts.** Re-quote from the holding and round down again.
- **A cost is charged to the floor, or the 2028 deposit fails to arrive.**
- **Coupons earn 2% or less for years.** The gift then falls below $145,000 in 1-2% of paths.
- **Yields fall after 2031** (not modelled). A new shortfall comes from Laura's part, then moves the gift toward the
  floor; WS7's Japan-style case (not Gate-B checked) is the test.
- **The curve moves.** Friday's curve and the January 2027 yields change the numbers, not the statement. Re-run WS2
  on Friday.

**Implications**
- **IPS: fix-before-6-Nov (the team words both edits).**
  - Add "rounded down" where the IPS says Laura quotes the floor. This keeps "cannot fall outside it" true.
  - Settle F4 in the same sentence.
  - The coupon fix to "needs no rebalancing" (Gate A; `rab/assumptions.md` C3), with D6's owner words, also protects
    condition 5. No extra item.
- **Final Report: note-in-Final-Report.** Cover the five conditions, where the gift lands, today's projection with
  the yield caveat, the coupon figures, and option D.
- **Trading Notes.** The IBTM note must pass the PM-14 word check: no fixed-repayment or certainty claims. It may say
  that IBTM also carries Laura's facility floor. Put no range, odds or $145,000 in a WInS note.

v4: condition 5 now names one owner (the stock fund, before the range; D6 v4). v3 added the Book L coupon check.
