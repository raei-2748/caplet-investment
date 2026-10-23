# Laura's 2031 contribution range: the numbers

AI-generated research (Claude Code), 17 Oct 2026, for Team Caplet. **Not submission text.** It gives the team the
numbers and the reasoning to write the range themselves (Final Report, due 4 Dec; the IPS is not expected to carry
it). Log it in the AI-use record. Everything below is a MODEL unless marked VERIFIED.

Reproduce: `python3 range_2031.py ../assistant_review_2026-10/checks/par_to_16Oct.csv 10/16/2026`
(numpy only; ~10 s; fixed seed). Output table: `range_2031_results.csv`.

## The answer in one line

On today's (16 Oct 2026) Treasury curve and our "Roots First" plan, Laura would most likely tell co-sponsors in 2031:
**"at least $145,000, and up to about $170,000"**, with the bottom already bought and about a **3 in 4** chance
the gift reaches the top. The bottom is the $150,000 floor rounded down, because IBTM is a fund and its payout is
not fixed (median about $148,300, worst about $146,300). The top is not knowable today: it is set by the stock
fund's value in Jan 2031, so it could be anywhere from about $145,000 to $195,000 (5th to 95th percentile).

## How the range is built (the plan as it stands, competition/COMPETITION.md s7)

| Step | What happens | Number today |
|---|---|---|
| Jan 2027 | $300k buys the ladder for the ten $50k payments | costs **$298,087** on the 16 Oct curve (VERIFIED curve, model price) |
| Jan 2028 | $150k: fill any ladder gap, then IBTM sized to pay back the remainder in Dec 2032 = **the floor** | floor $150,000, costs about $114,600 |
| Jan 2028 | the rest + the 2027 leftover goes into VT, untouched to 2033 | about $35,000 |
| Jan 2031 | quote **bottom = floor's worst-case payout, rounded down to $5k**; **top = floor's expected payout + half of VT that day** | $145k to ~$169k-171k |
| Jan 2033 | gift = IBTM's actual payout + half of VT, **capped at the top**; Laura keeps the rest | gift median ~$168k |

## Results (200,000 paths each; rates move 90bp a year)

| Equity model | Bottom | Top (p5 / median / p95) | Gift reaches the top | Gift at least halfway | Gift (p5 / median / p95) | Laura keeps (p5 / median) |
|---|---|---|---|---|---|---|
| Normal returns (JPM 2026 LTCMA world: 7.0%, 16.8% vol) | $145k | $145k / $169k / $192k | 76% | 100.0% | $144k / $168k / $191k | $12k / $29k |
| Fat tails (crashes more often) | $145k | $145k / $169k / $192k | 79% | 99.9% | $144k / $168k / $191k | $12k / $29k |
| History (real world-stock returns 1872-2025, in order) | $145k | $146k / $171k / $195k | 85% | 100.0% | $145k / $170k / $194k | $15k / $33k |

IBTM's payout is modelled as the amount it was sized for less a drift of 0.4% +/- 0.8% (calibrated to the earlier WS2
result: median ~$149.4k on $150k, below face ~69% of the time, worst ~$146.3k; `archive/rab/decisions/D_range_confidence_2031.md`).
The 2031 bottom uses a 2.5% worst-case drift, then rounds down to $5k. (Added after the Codex review on PR #9; the
first version assumed IBTM paid the floor exactly and quoted $150k.)

The gift never falls below the quoted bottom in any path of any model. That is by construction, not luck: the floor
is a Treasury fund Laura already owns, and the gift is capped. It holds if (1) the $150k arrives in 2028 (the case
says it does), (2) IBTM pays out close to its yield (iShares says the fund "does not seek to return any
predetermined amount"; this is why the bottom is rounded down to $145k), and (3) the ladder needs no top-up after 2031 (earlier work
found a gap of about $500-1,500 at today's yields, covered by Laura's half: `archive/rab/decisions/D6_cap_share.md`).

Why a p5 top ($145k) is below $150k: in about 44% of paths yields fall before Jan 2027, the ladder costs more than
$300k, and the 2028 deposit fills the gap first, so the floor is smaller (p5 $131k). The bottom then falls with it
(p5 $125k). The table's gift p5 ($144k) sits below $145k for the same reason: those are paths with a smaller floor.
The rule "floor rounded down" already handles this; the 2031 quote just uses whatever floor was bought.

## Three things the team should know

1. **The headroom almost disappeared this week.** The ladder cost $292,327 on 6 Oct, $294,336 on 13 Oct and
   $298,087 on 16 Oct (yields fell ~10bp). Only $1,913 (about 7bp) is left under $300k. A 0.5-point fall in
   yields by January means a ~$13k top-up from 2028 and a floor of about $136k, not $150k. So **never quote
   "$150,000" as fixed** in the IPS or report; say the floor is "what is left of the 2028 deposit after the
   payments are complete" (as IPS V5 already does) and give $150k as today's estimate.
2. **The half share does not change the odds of reaching the top.** The gift reaches the top whenever stocks do not
   fall between Jan 2031 and Jan 2033 (about 3 in 4), whatever share is promised. Promising 1/3, 1/2, 2/3 or all of
   VT gives the same ~74-76%. What the share changes is the size of the top (median $162k / $169k / $176k / $190k)
   and Laura's cushion (bad-case $16k / $12k / $8k / $0). So "half" is a choice about **Laura's cushion for cost
   overruns**, not about credibility. That is a cleaner argument for the report than "a narrower range is riskier".
3. **"Halfway" is almost certain.** The gift lands at least halfway up the range unless world stocks halve in two
   years (99.7-100% of paths). That gives Laura a second, very strong confidence statement.

## What a confidence statement could contain (ingredients, not wording)

- The bottom, and why it is safe: already bought in Treasuries, matures before 2033.
- The top, and what it depends on: half of a stock fund's value on the quote date.
- Two odds, rounded and labelled as model estimates: reaching the top ~3 in 4; at least halfway ~99 in 100.
- What happens in a bad market: the gift slides toward the bottom, never below it; the payments are untouched.
- Out of scope / not promised: taxes, facility cost, Taiwan currency.

Judges reward simple: one range, two odds, one sentence on why the bottom is safe. Avoid "guaranteed" and
"risk-free" (competition/COMPETITION.md s7 wording rules).

## Sensitivity

| Change | Effect |
|---|---|
| Rates move 60 / 90 / 120bp a year | median top unchanged ($169-170k); floor p5 $138k / $131k / $124k |
| Yields today 1pt lower | ladder $328,699, top-up $28,699, floor ~$120k |
| Yields today 0.5pt lower | ladder $312,972, top-up $12,972, floor ~$136k |
| Yields today 0.5pt higher | ladder $283,993, no top-up, floor $150k, more left for VT |

## Limits (be ready for a judge's devil's-advocate question)

- One parallel rate shock for 2027 and 2028; the ladder's price change uses its duration (DV01 $289/bp).
- Equity returns are annual; the history model reuses real 5-year windows (150 of them), so it is not independent.
- Fees: VT 0.06%, IBTM 0.07% (issuer pages, insight_v1). One $25 trade for VT; bond commissions ignored.
- The 2028 deposit is assumed to arrive in full (the case says it does).
- Older STRIPS-based range work (`archive/rab/results/M3/`, `keel/library/insight_v1/`) found the same shape (~$150k to ~$175k,
  ~73% to reach the top); those numbers are superseded by this WInS-only basis.

## What this teaches (for Ray)

A range is two different promises. The bottom is a **matched** promise: you buy something today that pays that
amount on the date. The top is a **market** promise: it depends on prices you cannot know. Separating them is what
lets Laura sound confident without overpromising, and "rounding down" plus a "cap" are the two small rules that
make the range impossible to miss.

## Decisions for the team

- [ ] Accept the floor definition "the remainder of the 2028 deposit" (not a fixed $150k) in all texts.
- [ ] Keep "half" and state the reason as Laura's cushion (point 2).
- [ ] Choose which odds to quote (top only, or top + halfway) and which model to cite (suggest: the normal model,
      with history as a check).
- [ ] Re-run this script on the last curve before the Final Report (and in the report, date the numbers).
