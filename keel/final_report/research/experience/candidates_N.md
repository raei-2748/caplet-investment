# New events after the first blind ranking (added from Mon 9 Nov 2026)

Same format as `candidates_W.md` and `candidates_K.md`. Real events only, each with its evidence. They join the pool at
the next blind re-rank (scheduled Mon 16 Nov), so that one panel reads every week's additions together.

### N-01: Laura's own market fell while shares rose
- Date (Sydney): Mon 9 Nov
- Origin: KEEL (research on the team's submitted idea)
- What happened: Two days after the IPS went in, we went through Laura's income one source at a time to test the idea it opens with, that her career behaves like shares she cannot sell. Most of it held: school book budgets fell hard in 2011 and 2012, years after the crash, and new advances shrank for most authors in 2009. But her own market broke the simple version. US graphic novel sales fell 22.4% in 2023 and 11.5% in 2024, the two years the S&P 500 rose about 26% and 25%.
- Stakes: The first sentence of our IPS, which is frozen and cannot be changed.
- Decision or response: We kept the idea and changed how we will explain it: her career is a risky asset with its own cycles as well as the market's, and the plan protects the payments from both, because no payment depends on her income after the deposits or on a share price.
- What changed afterwards: The Final Report will state the refined idea and the 2023-24 numbers rather than the simple version.
- Vivid detail: The year shares rose 26%, her genre had "the biggest decline" in US print sales.
- Strand: research and decision process
- Related: K-14 (the same idea, first tested on 8 Nov)
- Evidence: `keel/final_report/research/cards/Q12_lauras_working_life.md` rows 17-20 and 18 (Publishers Weekly, 5 Jan 2024 and 10 Jan 2025); `keel/final_report/ARGUMENT_LOG.md` (Mon 9 Nov, midday)

### N-02: A fact we had used was one day wrong
- Date (Sydney): Mon 9 Nov
- Origin: KEEL
- What happened: One of our favourite facts said that before this autumn, $300,000 had not bought all ten of Laura's payments on any day since 2008. We re-ran it on the one engine behind every number in the report, against 16,198 daily Treasury curves since 1962. It was off by one day: on 19 October 2023, when 20-year yields closed at 5.30%, the ten would have cost $299,293. The rest held: on 5 October 2026 they were the cheapest since 21 May 2002, and since 1871 $300,000 could have bought them in about one month in four, nearly all of those months between 1966 and 1999.
- Stakes: A single wrong number in the report would let a judge doubt all the others.
- Decision or response: Every number an event quotes now comes from the number register, not from the notes of the day it happened.
- What changed afterwards: The register gained the full price history (section 8e), and two older event numbers were corrected.
- Vivid detail: One day in more than four thousand.
- Strand: research and decision process
- Evidence: `keel/final_report/NUMBERS.md` section 8e; `keel/final_report/numbers/price_history.py`; `keel/final_report/research/EXPERIENCE_RECORD.md` section 5, item (c)

### N-03: Three separate checks found the same weak spot in the payments
- Date (Sydney): Tue 10 Nov
- Origin: KEEL
- What happened: We had sized the ten payments so that all ten would be paid if the bonds' interest could be reinvested at up to 3 points below today's forward rates. Three research workers, each checking a different promise (the payments, the 2031 range, the half of the shares kept back), came back with the same weakness from three sides: a promise sized on a guess about future interest rates failed somewhere in history, and a promise sized on "what it pays if interest earns nothing" never did. On the old sizing, the payments were short in 35 of 585 historical rate stretches (worst $12,117 short, from a July 2007 start) and $22,192 short if interest earned nothing.
- Stakes: The IPS says none of the ten payments will depend on a share price. Where the payments came up short, the only money left to cover them was shares.
- Decision or response: We adopted the standard escrow verifiers use for defeased bonds, "sufficient without reinvestment": the 2028 deposit adds extra Treasuries so all ten are paid even if no coupon earns a cent. Each of the ten bonds still funds its own payment, as the Trading Notes say.
- What changed afterwards: All ten are paid in all 585 stretches and in all seven of New York's regulatory interest-rate scenarios. It costs $13,220 more (1 Jan 2027 money, with a small cushion for the waiting fund's fee), and the central 2031 range falls from about $110,000-$130,000 to about $95,000-$115,000; about $45,000 comes back to Laura in 2033 if today's forward rates hold (2033 money). The same "if interest earns nothing" rule now sets both ends of the range, so one standard runs through the plan.
- Vivid detail: Three workers who never saw each other's notes wrote the same sentence in different words.
- Strand: research and decision process
- Related: N-04, N-05
- Evidence: `keel/pm/ASK_HUMANS.md` (Tue 10 Nov, 07:04); `keel/final_report/research/cards/Q20_pooled_book_or_margin.md`; `keel/final_report/NUMBERS.md` sections 2 (cost $336,656), 4 and 8h (overflow $45,456); `keel/final_report/LESSONS.md` (Tue 10 Nov)

### N-04: The test that could not fail
- Date (Sydney): Tue 10 Nov
- Origin: KEEL
- What happened: Our numbers said the 2031 range Laura states is owned in every modelled path. An outside reviewer, reading the numbers the way a bond portfolio manager would, found that the formula used to set the range's two ends was the same one used to test them, so the test could never fail. The reviewer also showed that our simple stand-in for the 2032 Treasury fund would overstate what it pays if yields fell about a point before Laura buys it.
- Stakes: The 2031 range is what Laura tells co-sponsors. If its bottom is not truly owned, her stated confidence is not true.
- Decision or response: Each end is now worked out from the fund's actual holdings on the day it is bought, cut by 0.5% for the fund's own frictions, and rounded down to $5,000. It is then tested by a different calculation from the one that sized it.
- What changed afterwards: Measured at zero interest from each trade day, the smallest margin between what is owned and what is stated is $458 at the bottom and $532 at the top, across 585 historical windows. The rule is written down, so no figure is stated before it is owned.
- Vivid detail: A test that passed every time, for a reason that had nothing to do with whether the range was safe.
- Strand: research and decision process
- Related: N-03, N-05
- Evidence: `keel/final_report/research/panel/2026-11-10_bond_desk_register_check.md` (finding 1); `keel/final_report/NUMBERS.md` sections 0, 3, 4 and 8i; `keel/pm/ASK_HUMANS.md` (Tue 10 Nov, 07:04)

### N-05: One word in the IPS became a rule
- Date (Sydney): Tue 10 Nov
- Origin: KEEL
- What happened: The submitted IPS says "Most of the 2028 deposit will fund a Treasury fund maturing in late 2032". Once the payments needed more of the 2028 deposit (N-03), our fixed split of what was left would have put less than half of the deposit in that fund in about 1 modelled path in 7, the paths where yields fall before January 2028.
- Stakes: The IPS is frozen. A Final Report whose numbers break one of its words would contradict what the team already submitted.
- Decision or response: The frozen word wins over our own split: the 2032 fund gets the larger of 73.3% of what is left and just over half the deposit ($75,001), and the world share fund takes the rest.
- What changed afterwards: The constraint binds in 16.9% of modelled paths and in 30 of 585 historical windows. Where it binds, the share fund is smaller by a median $3,104. Every quantity word in the IPS ("most", "half") is now checked as a rule in every path.
- Vivid detail: A four-letter word decided where tens of thousands of dollars go.
- Strand: research and decision process
- Related: N-03, N-04
- Evidence: `keel/pm/ASK_HUMANS.md` (Tue 10 Nov, 08:01); `keel/final_report/NUMBERS.md` section 4; `keel/final_report/research/panel/2026-11-10_bond_desk_register_check.md`
