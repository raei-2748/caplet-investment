"""Plain-English insight text for the client report (build_client_brief.py).

Distilled from the phase A, C, D and E files of the insight_v1 run (numbers exactly as there; E6_final_spec.md and
audit corrections win where files differ; "model" = a computer estimate, not a forecast).
"""


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def block(title, items):
    return f"<h2>{title}</h2>" + ul(items)


PHASE1_EXTRA = block("Surprises and traps in the case", [
    "Laura puts in $450,000 and must pay out $500,000, yet the ten payments cost only about $294,000 today, because bonds earn interest until each payment is due.",
    "\"A high degree of certainty\" is never defined. We define it by price: the payments are bought, not forecast.",
    "The reserve is \"set aside\" in 2033, the day the first payment is due. We explain why we buy it in 2027.",
    "No currency is named, although the residency is in Taiwan. The rules on permitted investments apply to both deposits, so we read them as ruling out currency contracts.",
    "The case says she \"will\" add $150,000. Testing a missing deposit is our own stress test, and we label it that way.",
    "In the story an advisor \"decides\"; the real rules say advisors may not make decisions. Every choice is the students'.",
    "Gains in the trading game never count toward Laura's money, and trade notes can never be edited.",
    "There is no approved fund list this year, so the platform may accept trades the rules ban. Older rules found online (a sector minimum, other cash amounts) are wrong.",
    "Wharton's sample trading note will be widely copied. Ours must carry facts only Laura's plan has.",
]) + block("People we might forget", [
    "The residency's staff live on fixed $50,000 payments that buy less each year and stop after 2042.",
    "Taiwanese partners think in Taiwan dollars, and \"dollar\" is ambiguous in Taiwan, so we always write \"U.S. dollars\".",
    "Book advances come in instalments, so the 2028 deposit could be late, not only smaller. The plan's rules handle both.",
    "Laura's credibility is part of her income. A missed public number would hurt her twice.",
    "Funders dislike paying running costs. Because operations are already funded, partners' money can go to the building.",
    "After 2033 she may earn less while running the residency: another reason to keep some money back.",
])

PHASE4_BODY = """<p>Twelve specialists answered the 48 questions, and five auditors re-ran the maths and re-opened the sources.
Here is everything they found, in plain words.</p>""" + "".join([
    block("Interest rates and the January 2027 purchase", [
        "The ten bonds cost about $294,387 at 25 September prices, $5,613 under $300,000. A fall in interest rates of just 0.19 percentage points would use up that cushion; the model puts the chance at about 1 in 3.",
        "Buy all ten as soon as the money arrives and keep any leftover in short-term government bills. Waiting for better prices or buying in stages gives no reliable gain and a 27-35% chance (model) of needing the 2028 deposit.",
        "If money is short, buy the latest payments first. After a one-point rate fall with no second deposit, $31,400 would be missing instead of $47,700. The cost: the first operating year is the one that waits.",
        "How big the gap could get (model): $9,169 after a half-point fall, $24,793 after a one-point fall, $27,631 on 2026's worst day. A repeat of late 2008's sharp fall would need $48,600, a third of the second deposit, so we never promise an \"at most\" figure.",
        "The 2028 deposit finishes the payments before anything else. About $43,000 of it covers a 1.5-point fall, and $51,000 the worst three-month fall since 1990.",
        "Considered and rejected: a \"funding below 100%\" alarm. It can never go off once every payment is bought; the right question is simply \"is every payment bought?\"",
    ]),
    block("Stocks and AI", [
        "Stocks must beat about 5.2% a year, what U.S. government bonds pay for Laura's 2028-2033 dates, not zero.",
        "Forecasters disagree about how much extra stocks will earn: JPMorgan about 1.5 to 1.8 points a year above bonds, Vanguard about zero, all sources between -1.2 and +2.4. Stocks are there for upside, not to meet the goals.",
        "U.S. shares look very expensive against ten years of average profits (second only to December 1999) but normal against next year's expected profits, because profits are expected to rise 32%, led by AI chips. The plan must work either way.",
        "The world stock fund's ten biggest holdings (21.7%, all AI-linked) are far less concentrated than the S&amp;P 500's (38.8%), but it still owns Asian AI chipmakers. We never claim it \"halves AI exposure\", and we use no Taiwan, AI or theme funds.",
        "Moving the growth money between 50% and 60% in stocks barely changes the typical result (-$1,500 to +$400). The final plan simply puts all spare money in one world stock fund.",
    ]),
    block("The computer model and stress tests", [
        "If the 2028 deposit arrives, even at $75,000 or a year late, the payments are never short (model). The biggest swings come from that deposit ($75,000 instead of $150,000 cuts the typical result by $98,000), from fees, and from which forecaster you believe (Vanguard's view: -$6,000).",
        "Fees matter: a 0.5% yearly fee on the growth money wipes out most of what stocks add. So all costs come only from the stock fund.",
        "The model has too few crashes (big falls in 0.3% of years, against 3.1% in reality), so we always show real history beside it. Replaying past crashes: before the floor is bought, building money falls 19-48%; after, only about 4-6%. The payments stay bought.",
        "Buying only 80-90% of the payments fails in 13-26% of futures if the second deposit never comes. Buying all ten costs just $900 to $5,200 of typical building money. Full certainty is cheap.",
        "The \"safe floor in 2028, rest in stocks\" design beat locking growth in 2031 on bad cases, at the same stock risk, so it became the final plan.",
        "Considered and rejected: locking 80-90% in 2031 and giving \"90%, capped\" (it announced about $17,000 less than was owned); a model-based \"80% confident\" range (right only 62-93% of the time); locking the floor in three steps (a $2,000-6,000 gain, not worth a second rule).",
    ]),
    block("Taiwan, currency and building costs", [
        "Building costs in Taiwan are expected to rise about 2-3.5% a year, so each U.S. dollar buys roughly 12-20% less building by 2033. 2026's +6.53% jump is a spike to mention, not the trend.",
        "\"Certain\" means certain in U.S. dollars. At 2.5% inflation, $50,000 is worth $42,063 in 2033 and $33,681 in 2042 in today's money. We name this gap once.",
        "Any Taiwan-dollar figure is an illustration only (NT$31.82 per U.S. dollar on 18 September 2026). By 2031 the exchange rate could move about 11-13% either way.",
        "No currency conversion or hedge before the building decision: a currency contract is a banned derivative, and it would cost about 5.9% now.",
        "Cushions: the Taiwan dollar tends to weaken when U.S. stocks fall, which helps; the 1995-96 missile crisis moved it by at most 4.4%. War is outside all the data. It would threaten the project, not the bought payments.",
    ]),
    block("Who Laura is", [
        "She holds two attitudes to risk: leaps whose cost she carries herself are fine, but letting down the people who backed her is worse. So money others rely on takes no risk. (Her public phrases are background for the team only, not text for the IPS or notes.)",
        "Bold in her career does not mean bold with investments. We never use her career story as a reason to own stocks, and since she has made no public statement about investing, we never describe her \"investment philosophy\".",
        "She has taught financial literacy to teenagers and interned in trading and in consumer protection. Expect plain words and named costs: she dislikes a show-off finance tone, not finance.",
        "Her public projects put access first and grew once the community backed them. \"Operations first, partners invited later\" fits her.",
        "She would welcome: purpose first, costs and gaps named, discarded drafts shown, rounded numbers, and what is secured (\"10 of 10 years funded\") before any dollar amounts.",
        "She would reject on sight: the case's pull quote presented as hers; puns on her book titles; her identity or Taiwan as a reason for a holding; false precision; hidden costs; one-sided risk stories; wrong facts about her work.",
        "Dropped: \"floor first, then leap\" as a trait of hers. It came from a reporter's sentence, not her own words.",
    ]),
    block("Co-sponsors and the 2031 range", [
        "Funders count only unconditional pledges and cash. So Laura leads with what is bought: in U.S. dollars, not forecast, barring a U.S. government default. Never \"guaranteed\": she only \"expects\" to give more.",
        "Confidence both ways: below the bottom only if the U.S. government defaults; the top is reached if stocks are no lower two years later (true in 84% of U.S. two-year periods since 1928; 73% in the model).",
        "Words: \"owned\", \"expected if stocks hold their value\", \"kept\". Never \"promised\". Strong markets add to the money she keeps, not to the gift, though she may still choose to give more.",
        "Flexibility needs a rule, not leftovers. Keeping half the fund gives about $32,000 in the typical case, roughly three to four years of Taiwan building-cost rises.",
        "Considered and rejected: a model-based top with no cap; converting to Taiwan dollars early; a \"10% of wealth\" rule of thumb; giving three-quarters or all of the fund.",
    ]),
    block("Behaviour and risk, goal by goal", [
        "Judge risk one goal at a time, not as \"moderate\" overall. The payments need no risk and can bear none. The stock fund can bear losses: her living costs are covered elsewhere and nothing is withdrawn before 2033.",
        "Her ability to take risk is lowest before the 2028 deposit, which depends on her career, and the plan holds no stocks then.",
        "The payments need only about 1.05% a year to be met. More stocks would add about $11,000-14,000 in the typical case but cost $41,000-56,000 in a bad case (model).",
        "The stock fund falls in about a quarter of years (model). In the worst tenth of 2031-32 outcomes, the typical gift is still about $169,000, and never below the floor.",
        "Decide in advance: never sell stocks to protect a gain or to \"wait for a recovery\". Rules change only when her circumstances change, never because markets move.",
        "Her big bets are already her career and books, so the portfolio holds only broad funds, and the money she keeps sits in short-term government bills.",
    ]),
    block("What the judges and the case designers test", [
        "The three written deliverables are judged together, the notes are quoted exactly, and the game's ranking counts for little.",
        "This year's case is about certainty and credibility: \"certainty\" appears 4 times, \"credible\" or \"credibility\" 3 times, \"growth\" once. None of the five \"must\" tests mentions growth.",
        "Creativity means fit to Laura, not clever investments. Rivals using AI may reach the same design, so our edge is Laura-specific reasons and real evidence of the team's own process.",
        "Simplicity wins: a past semifinal judge praised \"simple, elegant ideas\", and the 2022-23 champions said \"less is more\".",
        "\"Supported, tested or refined\" is a menu, not a quota. A note may say \"refined\" only if the team's log shows the change was decided before the trade.",
        "The strategy freezes on 6 November, so every rule must be fixed by then. Changes based on research before that date are fine.",
        "Breaking the format rules means exclusion, so the IPS stays well inside its limits. The working checklists hold the details.",
    ]),
    block("What professional investors do", [
        "Pension funds \"lock down the benefits promised, then grow surplus assets\". Our design is standard professional practice.",
        "Professional policy statements fix rules for market turmoil in advance, and can even state a policy of not rebalancing. Ours never rebalances.",
        "The competition points to a professional code: know the client, follow the stated rules, disclose fees plainly, keep records.",
        "A typical adviser charges about 1% a year. Charging costs only to the stock fund costs about $3,000 (typical); charging them on everything, about $31,000 (model).",
        "Returns are stated as a range from two published forecasters, never as a target.",
        "Considered and rejected: inflation-linked U.S. bonds (they track U.S. prices, not Taiwan's), and buying only part of the payments.",
    ]),
    block("How to talk about the plan", [
        "Central idea: a split of jobs. Money others rely on is bought when it arrives; money nobody relies on is fully in world stocks.",
        "Pitch: purpose first; each deposit buys a promise; she tells partners only what she owns. No numbers, and never \"bought in January 2027\", which fails in about 1 case in 3.",
        "One word per job: \"certainty\" for the payments, \"confident\" for the range, \"credibility\" for her standing. Avoid \"guaranteed\", \"risk-free\", \"100%\", jargon, return targets and \"innovative\".",
        "Name the two gaps plainly (the January price, and what fixed dollars buy in Taiwan) and keep risk talk to about 15% of the words.",
        "In the trading game, funds never mature, so say \"moves like\" or \"stands in for\", never \"matched\" or \"locked\". Measured against fixed payments, cash is actually the riskier choice: a 0.1-point rate move changes the payments' value by about $2,900.",
        "Name three trade-offs as \"gives up X to get Y\", and test the text on six outside readers, three with a finance background and three without.",
    ]),
    block("What the auditors corrected", [
        "The chance that the bonds cost more than $300,000 is about 1 in 3, not 1 in 4.",
        "\"At most\" promises and a \"0.01% chance\" were dropped: the model's 1-in-10,000 event actually happened in 2008.",
        "About $26,000, not $25,000, covers a one-point rate fall.",
        "The back-up fund for the building floor repays no fixed amount, so we never say it \"repays $150,000\".",
        "Building costs are \"expected\", not \"certain\", to rise; one +8.1% figure was construction wages only.",
        "JPMorgan's bond assumption is 0.5 to 1 point out of date, so results are shown with Vanguard's view too.",
    ]),
])

PHASE4 = [("Phase 4 · Research: what the specialists found", PHASE4_BODY)]

_JUDGE_ROWS = [("Investment strategy", 7), ("Client knowledge", 7), ("Portfolio analysis", 7),
               ("Articulation", 5), ("Creativity and presentation", 6)]


def _judge_chart():
    out = []
    for i, (lab, v) in enumerate(_JUDGE_ROWS):
        y = 6 + i * 30
        w = v / 10 * 400
        out.append(f'<text x="238" y="{y + 15}" class="n" text-anchor="end">{lab}</text>')
        out.append(f'<rect x="250" y="{y + 3}" width="400" height="16" fill="none" stroke="#e2e2e2"/>')
        out.append(f'<rect x="250" y="{y + 3}" width="{w:.0f}" height="16" fill="#c4c4c4"/>')
        out.append(f'<text x="660" y="{y + 15}" class="b">{v} / 10</text>')
    return f'<svg viewBox="0 0 800 {12 + len(_JUDGE_ROWS) * 30}" class="fig">{"".join(out)}</svg>'


PHASE5_BODY = f"""<p>Four teams read the draft plan and tried to break it. Everything they found was either fixed or
answered in the final plan.</p>
<h2>A Wharton judge</h2>
{_judge_chart()}
<p class="cap">The judge's scores for the earlier draft: 32 of 50. With ten fixes, about 38 of 50. The Top 50 is roughly
the top 2% of finishing teams.</p>""" + ul([
    "Too dense: about 55 ideas in 550 words. Fixed: about 12 ideas in 10 short blocks, on four dates.",
    "The pitch opened with a ban on stocks that the trading game breaks on day one, and it skipped the residency. Fixed: purpose first, and \"each dollar has one job\".",
    "A bond expert's red pen: short bonds used for dated money, no reason given for buying the latest payments first, and a withdrawn number. All fixed.",
    "Six named risks read as defensive. Fixed: two gaps plus a U.S. default, named once.",
    "The best story was unused: \"we tested a 75%-stock plan and dropped it\" (it missed payments in about 3% of model futures, and about 40% without the 2028 deposit). It is now one of the trading notes.",
]) + block("\"Laura\" (a simulation grounded in the case and her checked public words)", [
    "Would likely choose us: once bought, the payments stop depending on markets or her future earnings; the 2031 figure never needs taking back; gaps are named; she keeps her own decisions; no identity-based holdings.",
    "Pushed back on: codes and bans before purpose, \"promised\" for money still at risk, unstated fees, and personality labels. All fixed.",
    "Found it timid. Fixed by explaining (the payments cost about 98% of her first deposit), not by adding stock, and by saying what stocks are for: a bigger gift and flexibility in good markets. A fall costs only the extra.",
    "The questions she would ask: which year waits if 2027 prices are high (2033); what she pays; what stays hers; whether a crash changes the plan (no).",
]) + block("A rival team's best strategist", [
    "The attack: \"Buy a bond in January 2028 that repays the full $150,000 by 2033, put the rest in one world stock fund, and trade nothing in 2031.\" We adopted it.",
    "Why it is better: the lowest number she announces is fixed three years early ($150,000, against $134,000 in a bad case, or $93,000 after a 1929-style crash, for the old design); the worst six-year stretch leaves $169,000 against $120,000; the typical result is the same.",
    "What we accept in return: a typical gift of $174,000 instead of about $186,000-188,000; a best case $16,000 lower; strong markets grow her kept money rather than the gift.",
    "Where the old design still wins: if a crash recovers before 2031, as in 1973-78.",
]) + block("Pre-mortem: imagine we failed. Why?", [
    "The likeliest failure is ownership, presentation and process, not the strategy.",
    "The team does not own the plan: each student writes their own reasons, without AI, before every vote; devil's-advocate pairs; two-minute explain-backs.",
    "A format breach, which is fatal: strict limits, finish early, check the final PDF.",
    "Too dense: about 12 ideas, tested on six outside readers.",
    "AI wording in permanent notes: draft offline, check for copied phrases, keep a dated log of AI use.",
    "Process: roles agreed now, deadlines two days early, weekly check-ins. School holidays and exams (13 October to 5 November) may clash.",
    "Cheap but fatal: submit a day early (22 October, 5 November); roster in by 7 October; no contact with the client; no paid help; all six members involved.",
])

PHASE5 = [("Phase 5 · Stress tests: four teams tried to break the plan", PHASE5_BODY)]

OPEN_DECISIONS = """<p>The team decides every one of these. Our recommendation is shown for each.</p>
<table><tr><th style="width:36%">Decision</th><th>Our recommendation</th></tr>
<tr><td>Buy all ten payments first?</td><td>Yes. Each student writes why, in their own words, before the vote, and the vote is recorded.</td></tr>
<tr><td>Floor bought in 2028, or growth locked in 2031?</td><td>2028. Choose the design all six students can explain in two minutes.</td></tr>
<tr><td>What the trading game shows</td><td>Laura's plan in January 2028, scaled to $300,000. If outside readers think her real 2027 money holds stocks, show her first-year portfolio instead.</td></tr>
<tr><td>Share of the stock fund given to the building</td><td>Half. The half she keeps is about three years of Taiwan building-cost rises.</td></tr>
<tr><td>More stock, since reviewers found the plan cautious?</td><td>No, by default. If wanted, a smaller floor (about $100,000-134,000) is the option. Either way, state what certainty costs.</td></tr>
<tr><td>Labels and roles</td><td>The team's own labels, identical everywhere, before the first note. Every student owns a note or reflection and a part of the IPS.</td></tr>
<tr><td>Keep the repository public until 4 December?</td><td>The team leader decides by 2 October, weighing the risk of copying.</td></tr>
<tr><td>Checks on the trading platform</td><td>Record the holding limit, confirm each fund is listed, test the note box without saving, and check for any minimum-activity rule. Never add trades just to reach a count.</td></tr></table>"""
