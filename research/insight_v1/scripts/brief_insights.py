"""Plain-English insight sections for the client report (Phases 1, 4, 5 and the open decisions).

Distilled on 2026-09-28 from phase_A, phase_C, phase_D (specialists and audits), phase_E (red teams, final spec) and
open_questions.md. The final spec (phase_E/E6_final_spec.md) and the audit corrections win over earlier figures.
"Model" marks a computer estimate, not a forecast. Background points about Laura come from her checked public
professional record only; none is for quoting in the IPS or the Trading Notes.
"""


def sections(hbars, bullets):
    B = bullets

    phase1_extra = f"""
<h2>Traps hidden in the case</h2>
{B(["$450,000 goes in and $500,000 is promised, yet the ten payments cost only about $294,000 today: the difference is interest.",
    "\"High degree of certainty\" is never defined. We define it by price: bought, not forecast.",
    "The reserve is \"set aside\" in 2033, when the first payment is due; buying it in 2027 is safer.",
    "No currency is named, though the residency is in Taiwan. The rules effectively ban currency contracts, so there is no hedge.",
    "The story's advisor \"decides\"; the real rules forbid it. All decisions are the students'."])}"""

    rates = ("Phase 4 · Research: interest rates and the first purchase", f"""
<p>Twelve specialists answered the 48 questions, and five auditors re-ran their numbers. The first question was the
most urgent: what if the ten bonds cost more than $300,000 when the money arrives?</p>
<h2>How much money would be missing in January 2027 if rates fall first</h2>
{hbars([("Rates fall 0.5 percentage points", 9169, False, "$9,169"), ("Rates fall 1 point", 24793, False, "$24,793"),
        ("Repeat of 2026's worst day", 27631, False, "$27,631"), ("Repeat of late 2008", 48600, False, "about $48,600")],
       55000, label_w=250, bar_w=380)}
<p class="cap">Model estimates. In every case the $150,000 deposit in 2028 covers the gap; about $51,000 covers the
worst three-month fall since 1990.</p>
{B(["<b>Buy everything on arrival.</b> Waiting for better prices, or buying in stages, gives no reliable gain and a 27-35% chance of needing the 2028 deposit (model).",
    "<b>If short, buy the latest payments first.</b> After a 1-point fall with no second deposit, $31,400 would be unfunded, against $47,700 the other way round. The cost: part of the first year waits for the 2028 deposit.",
    "<b>Never promise \"at most\".</b> A repeat of late 2008 would need a third of the second deposit. The honest wording is \"when the second deposit arrives\".",
    "<b>The one stress case we name:</b> if rates fall and the second deposit never comes, $11,957 (0.5-point fall) or $31,413 (1-point fall) of the 2033 payment is unfunded.",
    "<b>Useless alarms are dropped.</b> A \"below fully funded\" warning can never fire once all payments are bought; the right check is simply \"is every payment bought?\""])}""")

    stocks = ("Phase 4 · Research: stocks and our computer model", f"""
<h2>Stocks: worth owning, but only with money nobody relies on</h2>
{B(["<b>The hurdle is not zero.</b> Government bonds for her 2028-2033 dates earn about 5.2% a year, so stocks must beat that to be worth their risk.",
    "<b>The extra reward is small and uncertain:</b> JPMorgan expects stocks to beat bonds by 1.5-1.8 points a year; Vanguard by about zero; all sources range from -1.2 to +2.4 points.",
    "<b>Prices look high on past profits but normal on next year's</b>, because 2026 profits are expected to jump about 32%, led by AI chips. The plan must work either way.",
    "<b>A world fund spreads the AI bet.</b> Its ten largest companies are 21.7% of it, against 38.8% for the main U.S. index. It still owns Asian chipmakers, so we never claim it removes AI risk."])}
<h2>Share of the fund in its ten largest companies</h2>
{hbars([("World stock fund (our choice)", 21.7, True, "21.7%"), ("Main U.S. index (S&amp;P 500)", 38.8, False, "38.8%")],
       45, label_w=250, bar_w=380)}
<h2>What the model taught us</h2>
{B(["<b>Payments are never short if the 2028 deposit arrives</b>, even if it is only $75,000 or a year late (model).",
    "<b>The biggest drivers of the building money</b> are the size of the second deposit (a $75,000 deposit cuts the typical result by $98,000), fees (1% on everything costs about $32,000) and which forecaster is right (Vanguard's view: -$6,000).",
    "<b>Buying only part of the payments</b> never fails if the deposit arrives, but fails in 13-26% of futures without it. Buying all ten costs just $900-5,200 of typical building money.",
    "<b>The model has too few crashes</b> (big falls in 0.3% of years versus 3.1% in history), so we always show real history beside it. In history replays, the payments stayed secure every time."])}""")

    taiwan = ("Phase 4 · Research: Taiwan, currency and the competition rules", f"""
<h2>What a fixed $50,000 is worth in today's money</h2>
{hbars([("Today", 50000, False, "$50,000"), ("2033 payment", 42063, True, "$42,063"), ("2042 payment", 33681, True, "$33,681")],
       55000, label_w=250, bar_w=380)}
<p class="cap">At 2.5% a year inflation. The payments are certain in U.S. dollars, but they buy less each year; we name this gap once.</p>
{B(["<b>Building costs in Taiwan</b> are expected, not certain, to rise about 2-3.5% a year, so a fixed U.S. dollar buys roughly 12-20% less building by 2033. The +6.53% jump of 2026 is named but not projected forward.",
    "<b>The exchange rate</b> is about 31.82 Taiwan dollars per U.S. dollar (18 September 2026). Any Taiwan-dollar figure is dated and illustrative; U.S. dollars are what we commit to.",
    "<b>No currency hedge.</b> A contract to swap later is a derivative, banned in the competition, and would cost about 5.9% today.",
    "<b>Natural cushions:</b> the Taiwan dollar tends to weaken when U.S. stocks fall, which helps a U.S.-dollar gift. The 1995-96 crisis moved it at most 4.4%. A war threatens the project, not the payments."])}
<h2>The competition's rules, in practice</h2>
{B(["<b>Format mistakes mean exclusion.</b> At the required double spacing, 550 words nearly fill two pages, so we plan for at most 470 words plus a 48-word pitch.",
    "<b>Notes are permanent</b> and may be cut at 300 characters. Test the box safely first. Never use \"guaranteed\", \"risk-free\", \"safe\", \"match\" or Laura quotes.",
    "<b>The advisor handles administration only.</b> Written rules decide; rules change only if Laura's circumstances change, never because markets move.",
    "<b>Trading basics:</b> no same-day buying and selling, orders fill at the next open, keep at least $1,000 in cash, and only students place trades."])}""")

    client = ("Phase 4 · Research: Laura, her partners and her attitude to risk", f"""
<h2>What we learned about Laura</h2>
{B(["In her public interviews she separates two kinds of risk: leaps whose cost she carries herself are fine, but letting down early supporters is worse. So money other people rely on takes no risk.",
    "Being bold in a career does not predict being bold with investments. We never use her career story as a reason to own stocks.",
    "She has taught financial literacy and expects plain words and clearly stated costs. She would reject a show-off tone, hidden fees, false precision and one-sided risk stories.",
    "Her public projects put access first and grew once a community backed them. \"Operations first, partners invited later\" fits how she works.",
    "We found no public statement of hers about investing, so we never describe her \"investment philosophy\".",
    "A popular reading, that she only leaps once a floor is secured, comes from a reporter, not from her. We dropped it."])}
<h2>What her partners will look for</h2>
{B(["Funders count only money that is actually committed, so we lead with what is bought, in U.S. dollars.",
    "Three words, one meaning each: <i>owned</i> (the floor), <i>expected if stocks hold their value</i> (the top), <i>kept</i> (her flexibility). Never \"promised\".",
    "Because her operations are fully funded, partners' money can go to the building, which funders prefer to running costs."])}
<h2>Risk, one goal at a time</h2>
{B(["The payments need no risk and can bear none. The stock fund can bear losses: her living costs are covered elsewhere and nothing is withdrawn before 2033.",
    "Her ability to take risk is lowest before the 2028 deposit, which depends on her career. The plan holds no stocks until then.",
    "Rules decided in advance: never sell stocks to protect a gain or to \"wait for a recovery\". The stock fund falls in about a quarter of years (model); even in the worst tenth of outcomes the gift stays near $169,000."])}""")

    craft = ("Phase 4 · Research: what judges look for and how to say it", f"""
<h2>What the judges and the case are really testing</h2>
{B(["The case's words have shifted toward certainty and credibility: \"certainty\" appears 4 times, \"credible/credibility\" 3 times, \"growth\" once.",
    "Creativity means fit to Laura, not clever investments. Rivals using AI may reach a similar design, so our edge is reasons that are true only of her, plus real evidence of our process.",
    "Simplicity wins. A past judge praised \"simple, elegant ideas\"; past champions said \"less is more\".",
    "All three deliverables are judged together and notes are quoted exactly, so the notes must never contradict the IPS."])}
<h2>What professional investors do</h2>
{B(["Pension funds \"lock down the benefits promised, then grow surplus assets\". Our design is standard professional practice, applied to one person.",
    "Professional policies set rules for bad markets in advance, each with a trigger, an action and a record, and may choose never to rebalance, as we do.",
    "A typical adviser charges about 1% a year. Charging costs only to the stock fund costs Laura about $3,000; charging them on everything, about $31,000 (model)."])}
<h2>How to say it</h2>
{B(["<b>The central idea is a split of jobs:</b> money others rely on is bought when it arrives; money nobody relies on is fully invested in world stocks.",
    "<b>The pitch:</b> purpose first; each deposit buys a promise; she tells partners only what she owns. No numbers, no dates that could turn out wrong.",
    "<b>Name trade-offs plainly</b> as \"gives up X to get Y\", and keep talk of risk to about 15% of the words.",
    "<b>Test it on people:</b> six outside readers restate the plan in their own words; anything two or more misread gets rewritten."])}""")

    judge = ("Phase 5 · Stress tests: the judge and \"Laura\"", f"""
<p>Four teams were asked to attack the draft plan. Their findings changed the final design.</p>
<h2>The judge's scores for the draft plan (out of 10)</h2>
{hbars([("Investment strategy", 7, False, "7"), ("Client knowledge", 7, False, "7"), ("Portfolio analysis", 7, False, "7"),
        ("Articulation", 5, True, "5"), ("Creativity and presentation", 6, False, "6")], 10, label_w=250, bar_w=380, h_row=28)}
<p class="cap">32 of 50: "Top-50 substance, not yet Top-50 presentation". The ten fixes it proposed lift this to about 38.</p>
{B(["<b>Too dense:</b> about 55 ideas in 550 words. Now at most 12 ideas in 10 short blocks.",
    "<b>The pitch led with a rule, not a purpose</b>, and skipped the residency. Now: purpose first, \"each dollar has one job\".",
    "<b>The best story was unused:</b> we dropped the 75%-stock plan after testing showed missed payments. One reflection now tells it."])}
<h2>\"Laura\" (a simulation based on her public words)</h2>
{B(["<b>Would likely choose us:</b> once bought, the payments stop depending on markets or her future earnings; the 2031 figure never needs taking back; gaps are named; she keeps her own two decisions.",
    "<b>Would push back on:</b> rules before purpose, \"promised\" for money still at risk, unstated fees, and labels such as \"loss tolerance\". All fixed.",
    "<b>Felt it was timid.</b> Our answer: the payments cost about 98% of her first deposit, so the caution is arithmetic, not a judgement of her. Stocks are there for a bigger gift and more flexibility in good markets.",
    "<b>Her likely questions:</b> which residency year waits if bond prices rise (2033); what she pays; what stays hers; whether a crash changes the plan (no)."])}""")

    rival = ("Phase 5 · Stress tests: the rival and the pre-mortem", f"""
<h2>The rival team's best attack, and what we did</h2>
<p>A rival strategist proposed buying the $150,000 building floor in 2028 instead of locking stocks in 2031. It was
better: the floor is fixed three years earlier ($150,000, against $134,000 in a bad case or $93,000 after a 1929-style
crash), and the worst historical result improves from $120,000 to $169,000. <b>We adopted it.</b></p>
{B(["What we accept in return: a smaller typical gift ($174,000 against about $186,000-188,000) and a lower best case.",
    "Where the old design still wins: if a crash fully recovers before 2031, as in 1973-78. It remains the documented alternative for the team's vote.",
    "The rival's own figures for falling rates were wrong and were corrected before use."])}
<h2>The pre-mortem: imagine we failed, then ask why</h2>
<table><tr><th style="width:38%">How we could fail</th><th>Prevention</th></tr>
<tr><td>The team does not own the plan</td><td>Each student writes 3-5 lines in their own words, with no AI open, before each vote; two-minute explain-backs.</td></tr>
<tr><td>A format breach (fatal)</td><td>Letter size, Word "Double" spacing, at most 470 + 48 words counted twice, PDF checked; freeze 3 November.</td></tr>
<tr><td>Too many ideas</td><td>At most 12 ideas; six outside readers restate it.</td></tr>
<tr><td>AI wording in permanent notes</td><td>Draft offline; search every five-word phrase against the research folder; keep a dated AI-use log.</td></tr>
<tr><td>Notes contradict the IPS</td><td>One vocabulary and one set of labels, fixed before the first note.</td></tr>
<tr><td>Missed deadlines</td><td>Roles set now, submit a day early (22 October, 5 November), watch exam clashes.</td></tr>
<tr><td>Breaking a trading rule</td><td>No same-day selling, no tidy-up trades, check the holding limit first.</td></tr></table>""")

    decisions = """
<p>These choices belong to the team. For each, we give our recommendation.</p>
<table><tr><th style="width:40%">Decision</th><th>Our recommendation</th></tr>
<tr><td>Secure all ten payments first?</td><td>Yes. Each student writes why, in their own words, before the vote.</td></tr>
<tr><td>Building floor in 2028, or lock growth in 2031?</td><td>2028. Choose the design all six students can explain in two minutes.</td></tr>
<tr><td>What the trading game shows</td><td>Laura's plan in January 2028, scaled to $300,000; switch to her 2027 portfolio only if outside readers are twice confused.</td></tr>
<tr><td>How much of the stock fund is given in 2033</td><td>Half. The kept half is about three to four years of Taiwan building-cost rises.</td></tr>
<tr><td>More stocks, given "too cautious" feedback?</td><td>No by default. If yes, a smaller floor ($100,000-134,000), and state what certainty costs.</td></tr>
<tr><td>Roles</td><td>Every student owns a note or reflection and a block of the IPS; one trader plus a backup.</td></tr>
<tr><td>Keep the research folder public until 4 December?</td><td>The team leader decides and records the copying risk.</td></tr></table>
<h2>Checks still needed on the trading platform</h2>
<ul><li>Screenshot the session rules: holding limit, trades allowed, fees. If the limit is under about 17%, pause and ask Wharton.</li>
<li>Confirm each fund and a Treasury maturing in the second half of 2032 is listed; check any activity minimum.</li>
<li>Test the note box length without saving; record the exact username for the title page.</li></ul>"""

    return phase1_extra, [rates, stocks, taiwan, client, craft], [judge, rival], decisions
