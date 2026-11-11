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

### N-06: A funder asked which number to count
- Date (Sydney): Wed 11 Nov
- Origin: KEEL
- What happened: We gave our plan for Laura's words to co-sponsors to a reader playing a foundation program officer who funds artist residencies, and asked one question: would you take the meeting? The answer was yes, decided by one fact: ten years of the residency's operations already owned in Treasuries before the doors open ("who keeps the lights on in year three" is the question that kills most proposals). But the reader also found what three research cards and a panel of three judges had missed: after the 2031 move both ends of the range are owned and the gift reaches the top in every tested path, so a funder "will count $95,000 and ask why there is a range". The same reader said the ask "has no limit".
- Stakes: The co-sponsor words are the part the case asks the team to draft. A funder who does not know which figure to count, or what is being asked, does not pledge.
- Decision or response: Co-sponsors count the stated bottom, pledged in writing, which only a US default can lower; the top is owned and is what Laura intends to give. The ask now has two parts: capital pledged on condition that the facility's total is reached by one close date, with Laura's figure first and unconditional; and yearly programme money from 2033.
- What changed afterwards: The co-sponsor plan was rebuilt the same morning, and the scorecard's "what it asks" target now waits for a second funder's reading. Our method changed too: each part now gets a reader who must act on it, asked "what would you do with this?", not "is it good?".
- Vivid detail: One question from someone with money to give did what three research cards had not.
- Strand: research and decision process
- Related: N-04, N-07
- Evidence: `keel/final_report/research/panel/2026-11-11_funder_reader_3d.md` (section A); `keel/pm/ASK_HUMANS.md` (Wed 11 Nov, 06:54); `keel/final_report/SKELETON.md` row 3d; `keel/final_report/LESSONS.md` (Wed 11 Nov, morning)

### N-07: Taiwan's own rules changed what Laura asks for
- Date (Sydney): Wed 11 Nov
- Origin: KEEL
- What happened: Our earlier cards had assumed Taiwanese funders behave like American and British ones, matching a founder's gift with promised capital. We then read Taiwan's own rules in Chinese at the source: the Ministry of Culture's grant directions and the law on foundations. The Ministry approves multi-year work only "year by year", funds buildings only through city and county governments with local matching, and its venue grant says the owner may not ask for more money when costs overrun. Corporate foundations are funded by their parent companies each year.
- Stakes: An ask shaped for the wrong funders would ask Taiwanese co-sponsors for something their own rules do not let them give.
- Decision or response: The ask changed from matched promises of capital to two parts: capital pledged on condition of the facility's total by one close date, and yearly programme money from 2033 in New Taiwan dollars.
- What changed afterwards: The co-sponsor plan, the assumptions (co-sponsor money comes year by year in NT$; only Laura's figure is fixed before 2033) and the monitoring table (the co-sponsors' January budget filings) all changed. The rule that overruns are the owner's, not the funder's, supports the IPS's own reason for the half kept.
- Vivid detail: One line of a Ministry rule, "no request for extra subsidy" (不得要求追加補助數額), said in ten characters what the IPS's half kept is for.
- Strand: research
- Related: N-06
- Evidence: `keel/final_report/research/cards/Q11d_taiwan_funders_primary.md` (verdict 1, row 7); `keel/final_report/SKELETON.md` rows 3d and 3e; `keel/final_report/LESSONS.md` (Wed 11 Nov, morning)

### N-08: The first outside reader lowered our own score
- Date (Sydney): Wed 11 Nov
- Origin: KEEL
- What happened: We had scored the clarity of our report plan's opening idea 4 out of 5. The first fresh reader, playing a first-round judge with a stack of fifty reports and five minutes each, read it once and scored it 3: the governing thought alone was clear, but the six points under it were not. The same reader could not reconcile two totals in the exhibits ($268,652 in the holdings table against $302,287 in the notes; $444,080 in the reserve figure against $444,500), because one figure was on the $300,000 trading book and the other on Laura's whole $450,000 plan.
- Stakes: Clarity is the weakest score in nine of the plan's ten weak parts, and only readers can move it.
- Decision or response: Every exhibit now states its scale (the $300,000 book or the $450,000 plan) and its basis (at cost, at forward rates, at zero interest) in its title or note; the holdings table gained a column saying what each holding pays for.
- What changed afterwards: The scorecard's mean fell from 3.25 to 3.17, the first fall since scoring began. From that run on, readers set every clarity score and Keel stopped scoring its own clarity upward.
- Vivid detail: The first honest outside number made our average go down.
- Strand: research and decision process
- Related: N-06
- Evidence: `keel/final_report/research/panel/2026-11-11_fresh_reader_exhibits.md` (items 2, 3 and 4); `keel/final_report/SCORECARD.md` (log, Wed 11 Nov, morning); `keel/final_report/exhibits/`

### N-09: Three judges said "right, but too dense", and we cut instead of adding
- Date (Sydney): Thu 12 Nov
- Origin: KEEL
- What happened: A second blind panel of three judges (a finance professor, a wealth manager who writes investment policies for authors and artists, and a former finalist reading as a first-round volunteer) read our report plan. They scored its content about 4 out of 5, up from about 3.3 three days earlier, but its clarity about 3. All three put the facility contribution and the 2031 range at 2 for clarity. The former finalist wrote that after reading the contribution part "I could not say afterwards what the recommended contribution was"; the professor counted six to twelve figures in front of each point.
- Stakes: Every fix we had taken from a reader had been added to a part; none had been taken out. A first-round judge who cannot repeat the answer marks two criteria down together.
- Decision or response: The same morning each part of the plan was cut to one answer and one headline number, with no probability rarer than 1 in 100 in the prose; the rest went to the exhibits' notes or stayed in the research store. The plan lost 170 words.
- What changed afterwards: The contribution now leads with one figure, about $115,000, and the range with three sentences. Our own scorecard fell from 3.17 to 2.75 because the readers, not Keel, now set every clarity score.
- Vivid detail: "Top 50: yes, likely. Top 10: not as planned. The plan is written for the three hardest readers it has met, not for me at minute four."
- Strand: research and decision process
- Related: N-08
- Evidence: `keel/final_report/research/panel/2026-11-12_judge_finalist.md` (sections 4 and 5); `keel/final_report/research/panel/2026-11-12_judge_faculty.md` (section 4); `keel/final_report/SKELETON.md` ("Panel 2's density cut"); `keel/final_report/SCORECARD.md` (log, Thu 12 Nov, morning)

### N-10: A true sentence that read as a contradiction
- Date (Sydney): Thu 12 Nov
- Origin: KEEL
- What happened: Our plan said the ladder was "maturity-matched, not duration-matched", which is the precise description. A blind judge set it beside the team's submitted trading-note reflection, which says the bonds "remove uncertainty, through duration-matching", and read it as the team contradicting its own submitted work. The same judge read the standard we set on 10 Nov (every payment paid even if interest earns nothing) as the IPS being revised, where the IPS had said the ten cost "roughly $300,000".
- Stakes: Wharton requires the report to stay consistent with the IPS; a judge who sees a revision can mark the whole strategy down.
- Decision or response: The report will say the true thing positively ("matched payment by payment") and never negate a submitted phrase; the top-up is said as the IPS's own clause ("we'll simply complete it with the 2028 deposit"), dated from January 2028.
- What changed afterwards: A seventh way the report could fail was added to the plan ("it reads as the IPS changed"), and our coherence checks now ask how a judge reads two texts side by side, not only whether a claim is true.
- Vivid detail: Both of our checks had passed both sentences, because both were true.
- Strand: research and decision process
- Related: N-09
- Evidence: `keel/final_report/research/panel/2026-11-12_judge_finalist.md` (section 3 and the hand-back); `keel/final_report/INTENT.md` (failure 7); `keel/final_report/CANON.md` C12; `keel/final_report/LESSONS.md` (Thu 12 Nov, morning)
