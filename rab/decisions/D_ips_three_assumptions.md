# The three assumptions the IPS must state

WS2, 30 Sep 2026. AI-generated (Claude Code) for Team Caplet; the team ratifies and writes every deliverable.
Laura's plan, MODEL, 28 Sep 2026 curve, Gate B reconciled. Keys: `rab/numbers_ws2.yaml` (W), `rab/numbers.yaml` (N).

**Decision.** Three assumptions move the 2031 range, so the IPS names them:
1. **Treasury yields when the 2027 deposit buys the ten holdings** (early January 2027).
2. **The 5-year Treasury yield when the floor is bought** (January 2028).
3. **Costs, and the rule that the stock fund pays them.**

The stock-return assumption is not among them. The IPS names them in words; the Final Report gives the numbers.

**Question.** The case asks teams to "identify and explain their assumptions". Which ones actually move Laura's range,
and what must the IPS say about them?

**Options**
- **A. Lead with the stock return (7% a year).** Rejected: it moves the typical top by under $3k.
- **B. Put all three in the IPS with numbers.** Rejected, for two reasons:
  - The IPS guide leaves projections and the final range to the Final Report.
  - The IPS body has about 17 spare words (483 of 500 by `wc`, W `static.ips_word_count`).
- **C. Name them in the IPS, quantify them in the Final Report.** **Chosen.**

**Evidence** (the typical 2031 top; base about $175,000)

| Assumption (range tested) | Share of variation (Sobol) | Typical top across the range |
|---|---|---|
| Yields at the Jan 2027 purchase (-93 to +92bp, 95% of 95-day moves since 1990) | about 90% | about $143k to $194k |
| 5-year yield in Jan 2028 (-1.95 to +2.27 points, 95% of 1-year moves) | about 7% | about $168k to $182k |
| Yearly costs from the stock fund (0 to 1% of all assets) | about 3% | about $175k down to $167k |
| Stock expected return (4.1% to 8%) | under 1% | about $173k to $176k |

- Sources: W `ws2.assume.sobol_total_index_median_top` and `ws2.assume.tornado_median_top`.
- The rule was pre-registered (`M8_SPEC.md` s3.4). The tornado, the 1-in-20 ranking and the blind rebuild all pick the
  same three (W `ws2.assume.must_state`).
- Stock-market luck in 2028-2030 explains only about a fifth of the uncertainty (W `ws2.assume.luck_share_top2031`).
- Stocks matter little for two reasons. They are only about 9% of Laura's money in 2028
  (N `laura.plan_split_2028.strips`), and only half of that is promised.

**What the IPS says today** (Google Doc, read-only, 30 Sep)
1. **Jan 2027 yields: already covered.** The IPS says that at September 2026 yields the payments cost less than
   $300,000, and that a fall would leave some payments for the 2028 deposit to complete.
2. **Jan 2028 5-year yield: not stated.** It is a projection input.
3. **Costs: not stated.** This is a policy, not a projection. "Cannot fall outside" and the payments' certainty both
   depend on no cost being taken from the floor or the dated holdings. The M8 card said "the IPS already charges costs
   to the stock fund"; the text does not say this, and the card is corrected in this commit.

**Confidence**
- High on the ranking: two builds and three methods agree, and the first assumption explains about 90%.
- Medium on the dollar ranges: the inputs are treated as independent, and the ranges for costs and returns are
  judgements.

**What would change it**
- A model that links 2027 and 2028 yields, or stocks and yields. This could raise the weight of assumption 2.
- A fee far above 1% a year.
- Friday's curve will not change the ranking. Re-run M8 before quoting any dollars.

**Implications**
- **IPS: fix-before-6-Nov, costs only.** About ten words, paid for by trimming elsewhere.
- **IPS: none for assumption 1**, which is already covered. **Assumption 2 is optional** if words allow.
- **Not a range assumption, but stated anyway: coupon reinvestment** on the ten holdings, with who pays a shortfall.
  With Laura's half paying first (D6 v5, WS3 rule 3), it never moves the 2031 top at today's yields and lowers it in
  7-10% of paths if coupons earn 2 points less. It decides whether Laura's cushion survives (W `ws2.d6.gap_owner`).
  It is already fix-before-6-Nov (Gate A, `rab/assumptions.md` C3: "needs no rebalancing"); the owner adds WS3's
  "if coupons earn less" to the cushion sentence. With the cost clause and WS3's rules 1-2 this may need more than
  the 17 spare words: the team trims elsewhere.
- This refines Gate B triage item 1, which marked all three fix-before. Reasons: the IPS text read today, and the
  500-word limit.
- **Final Report: note-in-Final-Report.** Include the table above, and the stock-return assumption with why it hardly
  matters. The source is JPM 2026 LTCMA, AC World 7.00%, data to 30 Sep 2025 (`rab/assumptions.md` E1).
- **Trading Notes: none.** Keep Sobol shares and yield scenarios out of WInS notes.

v5: coupon bullet names the kit's one owner (Laura's half first; D6 v5 = WS3 rule 3).
