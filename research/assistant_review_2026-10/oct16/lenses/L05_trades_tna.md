# L05: Trades and Trading Notes Analysis (TNA), forensic review

Prepared Fri 16 Oct 2026 (Sydney) for Team Caplet. AI-prepared research for planning only. It is not submission
text and contains no drafted reflections. Students write every word they submit, and this review goes in the team's
AI-use log.

Basis: repo at /home/user/caplet-investment (read-only), the 15 Oct brief and its TNA merge (scratchpad
`oct14/final.md`, `oct14/tna_merge.md`), live web pages fetched 16 Oct 2026, and the US Treasury par curve to the
15 Oct 2026 close (downloaded 16 Oct 2026). "MODEL" means a computed estimate, not a fact. Each finding is marked
**new**, **known-deeper** (the 15 Oct brief touched it; this goes further) or **known-repeat** (re-verified only).

---

## 0. Bottom line (read this if nothing else)

1. **The IBTR note's safety margin is almost used up (new, high).** On the 15 Oct curve the ten payments cost
   **$298,624**, which leaves **$1,376**, or **about 0.05 percentage points (4.7bp)** of room. On 6 Oct the room was
   22.7bp, and on 14 Oct it was 13.9bp. Long yields are down **0.20 points** since 6 Oct, which is exactly the size of
   fall the note names. MODEL: about a **1-in-4 to 1-in-3** chance that the cost is above $300,000 on the day the
   team takes its figure (20-22 Oct). The IBTR reflection has to work whichever way this goes. "The room is now about
   0.16" (the 15 Oct brief's figure) is no longer true.
2. **Holding is still the rule's answer, even if the line is crossed (new).** At WInS scale the trade that trigger B
   would make is below the kit's own $2,500 minimum, unless yields fall about another 18bp (under the fixed-floor
   reading) or about 69bp (under IPS V5's "sized to return that remainder" reading). So: record the check, don't trade.
3. **The three picks are still right (IBTR, IBTM, VT).** Each note is real, filled, under 300 characters and plain
   ASCII. But the trio never mentions *liquidity*, one of Wharton's named themes. It also reads as one burst of buying
   unless each reflection shows a different *kind* of decision. Wharton's own example note assumes a gradual
   "glide path", so the team must say in plain words why it locked the payments early.
4. **11 trades and "hold" is a strength only if the team can show the monitoring.** WInS shows all 11 orders placed
   within 25 hours and nothing since. Wharton calls WInS evidence of decisions "as market conditions changed". Keep a
   dated log of every check, each with the rule, the number and the "hold" result. Do not trade for show, and do not
   add notes later to old trades.
5. **Submission mechanics are still unseen.** Nobody has recorded the SMApply TNA form: its fields, its limits, or
   whether it takes text or an upload. SurveyMonkey Apply's own help says "Mark as Complete" is a task step, separate
   from submitting the application. Ray should open the task this weekend.
6. **The TNA may count less toward the Top 50 than the IPS.** Wharton's live Rules page says the Top 50 are chosen
   "based on the strength of their Investment Policy Statement (IPS) and Final Reports". The TNA is still "evaluated"
   and judged with the others. So make it correct and consistent, cap the time spent, and protect IPS time.

---

## 1. Every requirement in the TNA instructions, and whether the picks meet it

Source: `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` (2 pages, no format rules; PDF
created 10 Sep 2026, no annotations or images, checked with pypdf).

| # | Requirement (exact words, line) | Hard rule or guidance | IBTR (7 Oct 4:42:53 AM ET) | IBTM (6 Oct 10:01:41 PM ET) | VT (7 Oct 8:27:19 PM ET) |
|---|---|---|---|---|---|
| R1 | "Select three (3) Trading Notes from trades your team executed in WInS." (:42) | Hard | Filled (per the export at `05_...md:15`; ETF fill 7 Oct) | Filled (`05_...md:19`) | Filled (`05_...md:14`; fill 8 Oct) |
| R2 | "Include each Trading Note exactly as it appears in WInS." (:44) | Hard | 294 chars, ASCII only | 292 chars, ASCII only | 288 chars, ASCII only |
| R3 | "a reflection of 100 words or fewer" for EACH (:46) | Hard | to write | to write | to write |
| R4 | "Why your team made the investment decision." (:48) | Hard (content) | the note gives the test, not the reason for an iBond (see F-08) | two jobs; why one fund (no WInS bond 2031-36) is missing from the note | breadth and fee given; *sizing* missing |
| R5 | "How the decision aligned with your overall investment strategy." (:50) | Hard (content) | pre-set rule linked to the 2028 deposit | floor plus payment | above-floor growth |
| R6 | "How the decision supported the client's goals, funding needs, or risk considerations." (:52) | Hard (content) | payment certainty (case: "high degree of certainty", Client Profile:91) | 2031 co-sponsor credibility (Client Profile:114-116) | "thoughtful risks" and balance (Client Profile:70-72) |
| R7 | "The Trading Notes must correspond to trades executed in WInS. Yes, we will verify this." (:53) | Hard | never quote the cancelled IBTR note (`05_...md:37`, "0.3") | OK | OK |
| R8 | Submit "via the SurveyMonkey Apply form" (:54) | Hard | form fields UNVERIFIED (F-11) | | |
| G1 | Show how decisions "aligned with, tested, or refined" the strategy (:12, :29) | Guidance (not in the instruction bullets) | tested (its threshold is now live, F-01) | refined (only if gate G3 confirms the order of events) | aligned |
| G2 | Cover "growth, risk, liquidity, funding reliability, financial flexibility, and future cash-flow needs" (:4-6) | Guidance (purpose) | risk, reliability, cash flow | reliability, flexibility (floor) | growth, flexibility (Laura's half) |
| G3 | "Collectively ... a cohesive portfolio strategy" (:14-15) | Guidance | see F-08 | | |
| G4 | "quality of your reasoning ... not simply whether an investment gained or lost value" (:15-16) | Guidance | never cite a WInS gain | | |
| G5 | Not expected to give reserve size, projections, facility contribution or co-sponsor text (:20-23) | Guidance (leave them out) | the ladder cost is not the reserve size; give no 2031 dollar figure | | |
| G6 | "consistent with the strategic approach ... will later articulate in its IPS" (:30-31) | Guidance, but binding in effect | the dated number must match the IPS (F-02) | the floor wording must match the IPS | the role of "Laura's half" must match IPS V5:30 |

**What is *not* required:** no format, font, page or file rules. No category mix (earlier years demanded one stock
plus one ETF; F-18). No label heading such as "Tested:" (F-06). No citations rule either way (F-15).

---

## 2. Findings

### F-01. The IBTR threshold is almost used up (high, new)
**Problem.** The filled IBTR note says: "On the 6 Oct Treasury curve, her first $300,000 is enough to buy Treasuries
for all ten payments. If yields fall more than about 0.2 percentage points by January, the 2028 deposit would top up
the ladder" (`team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:15`). I re-ran the
team's own method: end-date sizing with the curve rolled to 1 Jan 2027. That is the method that reproduces the 6 Oct
$293,448 and 22.7bp in `ops/routines/MONITOR.md:22`. Results:

| Curve date | Ladder cost (MODEL) | Room under $300k | Break-even fall |
|---|---|---|---|
| 6 Oct | $293,448 | $6,552 | 22.7bp |
| 13 Oct | $295,290 | $4,710 | 16.3bp |
| 14 Oct | $295,988 | $4,012 | 13.9bp |
| **15 Oct** | **$298,624** | **$1,376** | **4.7bp** |

Par yields, 6 Oct to 15 Oct: 7y 5.15 to 5.00; 10y 5.27 to 5.10; 20y 5.68 to 5.48; 30y 5.64 to 5.43 (treasury.gov CSV,
accessed 16 Oct 2026). So the long end has already fallen by the note's "about 0.2 percentage points". A judge who
reads the note next to the public curve will see this.

The cost moves by about $1,367 a day (one standard deviation over 2026, which is 4.71bp at a DV01 of $290/bp). That
means the room left is about one ordinary day's move. As a random-walk MODEL with no drift, the chance that the cost
is above $300k on that day is: 20 Oct about 28%; 22 Oct about 33%; 6 Nov about 40%. The ladder cost more than $300k on
182 of 198 trading days in 2026; it has fit only since about September.

**Why it costs us.** IBTR is the strongest pick, and its whole story rests on this number. If a reflection says "the
room is now about 0.16" (`oct14/tna_merge.md:78`) or "the rule did not fire", it may be false by the time a judge reads
it. The IPS then has to agree with it.

**Fix (what it must achieve).**
- Fix one curve date for the figure. Suggested: the 20 Oct close, which is posted before a Thu 22 Oct Sydney
  submission.
- Re-run the script and save both the script and its dated output: `oct16/lenses/L05/code/ladder_series.py` (which
  uses the team's `m1copy`), or the rates analyst's own copy.
- Students prepare the reflection logic for **both** outcomes before 20 Oct. Below the line: "not yet; here is how much
  room is left on [date]". Above the line: "the rule we wrote before trading now applies: the 2028 deposit completes
  the earliest payment first and the facility gets less".
- Present a crossing as **the rule working**, not the plan failing. Treat the 0.2 in the note as a dated forecast,
  not a promise.
- Never present the WInS bond gains from falling yields as good news. In Laura's real plan, lower yields make her
  January purchase dearer.

**Evidence:** `oct16/lenses/L05/ladder_series_out.txt`; `oct16/lenses/L05/data/par2026.csv`
(https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv,
accessed 16 Oct 2026); `oct14/wins4/code/variants.py`.

### F-02. Knock-on effects: IPS figures and the "2027 leftover" (high, new)
**Problem.**
- IPS V5 says the ten payments "cost about $292,000" at late-September yields (`01_version_5.md:24`), and so does the
  pitch (`:16`). Tab 15 repeats it (`15_tab_15.md:7`, `:14`). That figure is now about $6.6k too low.
- V5's shortfall order starts "first from the 2027 leftover" (`01_version_5.md:26`). On the IBTR note's basis, that
  leftover was about $6.6k on 6 Oct and about $1.4k on 15 Oct. If the line is crossed, it is **zero**, so the first
  real backstop becomes "the half Laura keeps".
- The IBTO note already says IBTO "is one of the first payments we would top up if yields fall"
  (`05_...md:20`). That is consistent with the rule, so it is a strength to use.

**Why it costs us.** All three deliverables are judged together (`deliverables.txt:27`). A TNA that says one thing
about the ladder cost and an IPS that says another is a visible inconsistency. "Maintains consistency with the team's
IPS" is in the Investment Strategy criterion (`deliverables.txt:55-56`).

**Fix.** Vote set A (Sun 18 Oct) adds one item: "the dated ladder figure and what the IPS says if the line is
crossed". The IPS then uses the same date, or a newer date that is clearly labelled. It must also say plainly
whether the 2027 leftover may be zero. Do not rely on a buffer that has disappeared.

### F-03. Trigger B: even if the line is crossed, the rule says hold (medium, new)
**Problem.** The October rule's trigger B ("sell VT down ... buy IBTM", `rab/trades/october_trade.md:42`) is written
on the **zero-coupon (STRIPS) basis**, which the 6 Oct email superseded. It was also never ratified (G4 in the 15 Oct
brief). On the WInS-listed basis:
- The WInS book is Laura's plan scaled by 300/450, which is 2/3 (`notes_and_discussions.md:308`).
- Under the "fixed floor" reading the stock fund absorbs the whole gap. The VT sale reaches the kit's $2,500 minimum
  (`october_trade.md:42`) only when the gap reaches $3,750. That is about **17.7bp more** fall from 15 Oct. MODEL
  chance by the 20 Oct window close: about 1.5%.
- Under IPS V5's reading ("sized to return that remainder", `01_version_5.md:24`) the stock fund takes only "about a
  fifth" of the gap (`october_trade.md:62-63`). The minimum is then reached only after about **69bp** more fall.
- The trade window closes Tue 20 Oct 3:30 PM EDT, which is Wed 21 Oct 06:30 Sydney (`october_trade.md:20`).

**Why it costs us.** Without a logged decision, a crossing creates panic and the temptation to trade. A trade made
for the TNA would break the kit's own rule against staged trades (`october_trade.md:12`). It would also go against
Wharton's "should not be rewritten simply because markets move" (Guide:156-157).

**Fix.** By Sun 18 Oct, either restate trigger B on the WInS-listed basis, with the floor reading the IPS uses, or
retire it. Log the 14, 15 and 20 Oct checks with the numbers and "hold". This log becomes the IBTR reflection's
monitoring evidence and the Final Report's implementation story.

### F-04. 11 trades and "hold": strength or weakness? (high, known-deeper)
**For (official text).**
- Teams are not evaluated on "How many trades you make" (`smapply_public_2026-10-14/wins.txt:23`).
- "you should not be doing a lot of buying and selling" (`faqs.txt:39`).
- "The competition does not require frequent or same-day trading" (`trading.txt:53`).
- A strategy "should not be rewritten simply because markets move" (Guide:156-157).
- Wharton's legacy guide page complains "We see teams buying lots of stocks and selling just as many"
  (`oct16/research/R1_wharton_archive.md:390-395, legacy guidebook page [S29]`).

**Against.**
- WInS "provides evidence of how your team implemented its strategy and made decisions **as market conditions
  changed**" (`wins.txt:41`).
- "Complete a Trading Note when your team makes an investment decision ... at the time it is made" (`wins.txt:43`).
- All 11 orders were placed between 6 Oct 7:55 PM and 7 Oct 8:27 PM ET (`05_...md:14-24`). Since then WInS shows
  nothing, so a judge sees no evidence of monitoring.
- Earlier years asked how trades "informed your understanding and design of your final strategy" as it "evolved"
  (2023-24 deliverables page, `oct16/research/R2_pages/wp_2024_deliverables.txt:143-145`, :532-534).
- Last year's Caplet lesson was too much complexity and off-list trades (CLAUDE.md). This year's risk is the
  opposite: looking passive.

**Fix (framing, not trading).**
- Hold is a **decision taken repeatedly, by rule**. Show the dated checks: the 14 Oct close, 15 Oct (room down to
  4.7bp), 20 Oct. Each has the rule, the number and the result.
- The IBTR reflection is the natural place for one clause of this. The Final Report gets the full log.
- Show that the single build was deliberate. Every payment holding went in before the stock fund (IBTM 6 Oct 10:01 PM;
  VT last, 7 Oct 8:27 PM).
- Never say or imply that trades happened when they did not.

### F-05. "Add Note" exists, but don't use it on the picks (medium, new)
**Problem.** WInS lets the team add notes to executed trades from Order History or Transaction History:
"Notes are added in Preview Order and can also be added or viewed from Order History or Transaction History
(Add/View Notes)" (`team/google_drive/sheets/portfolio_and_trading_notes/wins_notes.csv:17`; COMPETITION.md:84).
It is tempting to add a "15 Oct review" note to IBTR. But Wharton wants notes recorded "at the time it is made"
(`wins.txt:43`). A later note on the same trade blurs which note is "the Trading Note" being quoted (R2). It can also
look retro-fitted when Wharton verifies (R7).

**Fix.** No added notes on IBTR, IBTM or VT before the TNA is submitted. Keep monitoring in the team's dated decision
log instead. If the team ever adds a WInS note later, it should only record a real review, and never "correct" a
quoted note.

### F-06. The instruction bullets are the checklist; labels are optional; liquidity is missing (medium, new)
**Problem.**
- The required content is the three bullets at TNA:46-52 (why, alignment, client link). "Tested/refined" appears only
  in the purpose text (:12, :29). A label heading spends words on something no rule asks for.
- The purpose list names six themes (:4-6). The Guide names four note roles: "growth, liquidity, risk management, or
  future funding" (Guide:84-86).
- The team's notes use those role words as opening labels ("Growth:", "Future funding:") (`05_...md:14-24`;
  `rab/trades/note_rules.py:50`). But **no note and no planned reflection mentions liquidity**.

**Why it costs us.** Liquidity is the one Wharton theme the trio leaves blank. It is also easy to show, because the
plan is about cash arriving on time.

**Fix.** Use the verbs naturally inside the sentences, without headers. Let one reflection show the liquidity point:
cash arrives before each 1 Jan payment. For example, IBTM's fund ends about 15 Dec 2032, 17 days before the
1 Jan 2033 payment (the 15 Oct brief verified the 17-day gap). That is liquidity timing, not just "certainty".

| Wharton theme (TNA:4-6) | IBTR | IBTM | VT |
|---|---|---|---|
| Growth | | | yes |
| Risk | yes (interest rates) | yes (payout not fixed) | yes (stock fall) |
| Liquidity | | **add** (cash ready before 1 Jan) | |
| Funding reliability | yes | yes | |
| Financial flexibility | yes (2028 deposit as backstop) | floor to co-sponsors | yes (Laura's half) |
| Future cash-flow needs | yes | yes | |

### F-07. Wharton's example note models a glide path; Caplet locks early, so say why (medium, new)
**Problem.** Wharton's only example is an intermediate Treasury ETF bought "to reduce portfolio volatility and begin
preparing" ... "to balance continued growth with reliable future cash flows **as the residency funding date
approaches**" (TNA:36-39). That is a gradual de-risking picture. Caplet does the reverse: it buys the whole payment
set at once, six years early, and keeps about 9% in stocks.

**Why it costs us.** A judge primed by the example may ask "why lock now, not gradually?" The notes never answer it.

**Fix.** IBTR or IBTM must give the reason in one plain clause. The payments are fixed in dollars (Client
Profile:90). Waiting would leave them exposed to falling yields, which is exactly the risk the IBTR test measures and
which F-01 shows is real. This is the team's most distinctive idea, so it is worth the words.

### F-08. "Cohesive" and "decision-making": make three different kinds of decision visible (medium, known-deeper)
**Problem.** The deliverable's title is "What Was Your Team's Decision-Making Process?" (TNA:3). The three picks are
three buys placed within 22 hours, so they can read as one decision: "build the book".

**Fix.** Give each pick a different decision type, with evidence:
- **IBTR, a rule set in advance:** the threshold and the response were written into the note before the trade
  filled.
- **IBTM, a change forced by new information:** on 5 Oct the team kept "never below the floor" because the floor was
  to be STRIPS (`final_report.md:24`). The 6 Oct email then limited the real plan to WInS-listed holdings, and IBTM
  became the real floor. This depends on G3: when the email arrived versus 10:01 PM ET.
- **VT, a choice among alternatives:** on 5 Oct Darren argued the world fund is a "copout" and proposed stock and ETF
  picking, with EWT and GLD also raised (`final_report.md:23`). The outcome is still "[fill in]". This is the most
  authentic decision-process material the team has. **Record the outcome and reasons by Sun 18 Oct**, or VT's
  reflection has no "why not something else".

Give each reflection one link to the others, for example "payments first, then the floor, then growth", so the
three read as one strategy (TNA:14-15).

### F-09. The TNA's weight in Top 50 selection is unclear, so budget time (medium, new)
**Evidence.** Rules & Roles (live, accessed 16 Oct 2026): "The top 50 teams will be selected as semifinalists based
on the strength of their Investment Policy Statement (IPS) and Final Reports."
(https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/). SMApply says "Your Trading
Notes Analysis, Investment Policy Statement and Final Report are evaluated" (`deliverables.txt:27`).
COMPETITION.md:41 says the Top 50 are chosen "on the written deliverables", which is less precise.

**Implication.** The TNA is still scored and judged together with the IPS, and it commits the team to facts the IPS
must repeat. But the IPS carries named Top 50 weight and has hard compliance gates. **Fix:** finish the TNA by Thu 22
Oct with a fixed time budget, and start the IPS rewrite (vote set B) on schedule. Correct COMPETITION.md:41 to quote
the Rules page.

### F-10. "Required trading activity" is still undefined, and the Week-One email is still unread (medium, known-deeper)
**Evidence.**
- Rules & Roles has a section headed "Trading Requirements" containing only: "Teams must meet the required trading
  activity and portfolio management guidelines throughout the competition." (live, 16 Oct 2026). The FAQ says the
  same (`faqs.txt:76`).
- The Week-One email is logged as "opens as a download, not read here ... Someone on the team should read it"
  (`wins_notes.csv:19`). The repo has no later record that anyone read it.
- Advisors are responsible for "Monitoring team engagement and portfolio activity" (Rules & Roles, live 16 Oct).
- Earlier years had a "first trade by" date (2025-26: 10 Oct; `oct16/research/R2_past_rules_rubrics.md:234`). The
  first 2026-27 orders on 6 Oct would meet a similar rule, but none has been found for 2026-27 (UNVERIFIED).

**Why it matters.** This is the only rule that could make an 11-trade "hold" book non-compliant, and it is the one
nobody has read.

**Fix.** Ray, or another student in a read-only login, reads the Week-One email and the logged-in Trading Details by
**Sat 17 Oct** and records the exact words privately. If a minimum exists, meet it only through a trade that has its
own strategy reason under a pre-set rule. Never trade just to reach a count.

### F-11. SMApply: "Mark as Complete" is not the same as submitting (medium, new)
**Evidence.** SurveyMonkey Apply's applicant FAQ (accessed 16 Oct 2026,
https://help.surveymonkey.com/en/apply/faqs/application-faq/):
- "To be able to submit your application you will first need to complete all required tasks within your
  application."
- "If you have previously pressed Marked as Complete on a form, but have not yet Submitted your application, you can
  choose to make Edits to your task."

How Wharton's portal handles each deliverable is UNVERIFIED. The TNA form's fields, its limits and whether it takes
text or an upload are recorded nowhere. The 15 Oct brief made recording them item 9; still open.

**Why it costs us.** If the TNA is only "marked complete" while some other step is expected, it might not count. And
pressing a whole-application "Submit" might lock later tasks (the IPS, the Final Report). Both are UNVERIFIED risks,
but cheap to rule out.

**Fix.** By Sat 17 Oct, Ray opens the TNA task without submitting. He records the field list, any word or character
counter, and whether it wants text or a file, and looks at how the already-submitted roster task's status reads now.
On submission day, screenshot the final status and keep the screenshot on the team Drive only. Do not press any
application-wide button without first checking what it locks.

### F-12. Identify each trade outside the reflection (medium, known-deeper)
**Problem.** The instructions don't ask for identifiers, but Wharton "will verify" (TNA:53). The WInS timestamp is
the **order** time in ET, not the fill. Fills: iBonds 7 Oct, VT 8 Oct (15 Oct brief §5; not yet confirmed from WInS
Transaction History).

**Fix.** If the form allows, put one identifier line above each reflection, outside the 100 words: security, buy,
quantity, and the order date and time exactly as WInS shows them. Quantities are IBTR 853 sh, IBTM 4,503 sh, VT 167 sh
(COMPETITION.md:176-186). Never convert times to Sydney time. Never call the order date the execution date.

### F-13. Copy fidelity: straight vs curly apostrophes, table rows, retyping (low, known-deeper)
**Evidence.** All 15 exported notes are plain ASCII with straight apostrophes (character scan of `05_...md`). The
team's Google Doc text uses curly ones elsewhere, for example "Laura’s" in `15_tab_15.md:7`. Google Docs turns a
typed ' into ’, which would make "Laura's" in a note no longer an exact copy. The Markdown export also mangles some
formatting (`05_...md:28-30`).

**Fix.** Copy each note from the WInS Trade Notes page itself and paste it as plain text (Ctrl+Shift+V). Never retype
it, and never "tidy" it. If you copy a table row, delete the date and ticker cells. A second student compares the
pasted note with WInS character by character: apostrophes, "%", "$", hyphens and the space count. Lengths to check
against: IBTR 294, IBTM 292, VT 288 characters.

### F-14. VT note faults, re-verified (medium, known-repeat)
- The note's "They only set how far her gift rises above her promised minimum" (`05_...md:14`) is wrong under IPS V5.
  V5 also gives Laura's half a cushion role (`01_version_5.md:28`, `:30`).
- "Promised" overclaims, and "They" has no clear subject.
- The note says nothing about **sizing** (about 9% of all money; 8.84% at cost in WInS).
- The facts still hold: Vanguard VT expense ratio 0.06%, 10,180 holdings (https://stockanalysis.com/etf/vt/,
  accessed 16 Oct 2026), so "about 10,000 stocks at a 0.06% fee" is fine.
- The overlap with the AI example (a 12-word clause) is in the 15 Oct brief.
- **New check:** compared with the 6 Oct "Proposed note, AI draft" column in `trading_notes.csv`, the three picked
  notes share few words (4-word overlap: IBTR 0%, IBTM 4-9%, VT 2-4%). So the AI-overlap issue is limited to the
  30 Sep examples already flagged.

**Fix.** The reflection corrects the role honestly and states the size and the trade-off. Keep VT as the growth pick.

### F-15. Where to disclose AI in the TNA itself (medium, new)
**Problem.** Wharton: "If you include material generated by an AI program, it should be cited like any other
reference material" (Rules & Roles, live 16 Oct 2026). The IPS bans citations; the **TNA instructions do not**. The
plan so far is to disclose only in the Final Report's Works Cited on 4 Dec. Yet two of the quoted notes share wording
with AI examples (VT, IBTM; 15 Oct brief §6). The TNA may well be scored before then, and it is judged as a separate
deliverable.

**Fix (team decision).** If the form has a spare field, consider a short factual AI-use acknowledgement outside the
reflections. If it doesn't, the team may ask Wharton through the official Contact Us form whether one is expected.
That is the team's choice and the team's message; the assistant contacts no one. Either way, record the decision in
the AI-use log.

### F-16. The volume rule differs between public and WInS text (low, new)
Public: "no more than twice a security's current daily trading volume" (`trading.txt:41`). WInS Portfolio FAQ as
recorded by the team: "Orders can take at most half of a security's market volume; larger orders wait"
(`wins_notes.csv:14`). This only matters for a further trade, such as trigger D's bond swap, where WInS bond volume
is unknown. **Fix:** follow the stricter half-volume reading before any order, and check that "larger orders wait"
does not leave a part-filled order open at the 6 Nov freeze.

### F-17. The date of the dated figure versus the submission plan (medium, known-deeper)
Submitting on Thu 22 Oct Sydney is Wed 21 Oct ET. The latest close the team can use is then 20 Oct. The exact time
treasury.gov posts the curve is UNVERIFIED; it is after the US close, so Sydney morning the next day. **Fix:** name
the figure "on the 20 Oct curve". Run it on Wed 21 Oct Sydney morning. The writer drops the figure in last, with the
two-outcome logic from F-01 already written. If the deadline slips to Fri 23 Oct ET, still use 20 Oct; don't chase a
newer figure.

### F-18. Past years' trading component, and the lesson (low, new)
- **2022-23:** three notes on one page, inside the Final Report. **2023-24:** "two (2) Trading Notes ... one related
  to a stock and the other to an ETF ... 150 words or less", reflecting on "how they informed your understanding and
  design of your final strategy" (`oct16/research/R2_pages/wp_2024_deliverables.txt:141-145`, :530-536; source page
  https://globalyouth.wharton.upenn.edu/investment-competition/deliverables/, accessed 16 Oct 2026).
- **2025-26:** an ETF / Stock / Team Choice section inside the Final Report (`R2_past_rules_rubrics.md:44-46`).
  Knox's own 2025-26 reflections were heavy with valuation jargon ("P/E", "supercycle") and the team traded off-list
  (`team/google_drive/2025_knox_wharton.md:90-110`, 1568-1590; CLAUDE.md). It did not reach the semifinals; the cause
  is unknown because Wharton gives no feedback.
- **2026-27** drops the stock-plus-ETF categories, so holding no individual stock is not a gap.
- Past winners' trading notes are not public (UNVERIFIED).

**Lesson:** Wharton has always rewarded notes that show learning (how a trade "informed" the strategy), not just
execution. Hence F-08.

### F-19. Wharton's trading role versus "only Ray trades" (low, new)
Rules & Roles: "All team members are responsible for: ... collaborating with teammates and placing trades through the
team's shared WInS account" (live 16 Oct 2026). FAQ: "It should be a team decision" (`faqs.txt:34`). The repo rule is
"only Ray places or cancels WInS orders" (CLAUDE.md, COMPETITION.md:193). That is not a breach; it is a sensible
control after the 7 Oct mis-click. **Fix:** in the Articulation section, describe it as team decisions (who voted),
one trader and one checker, and say why. Keep the vote records.

### F-20. Scale: a verifier sees about $197k of ladder in WInS, not $300k (medium, known-deeper)
The IBTR note says "her first $300,000 is enough" for all ten payments. In WInS the payment holdings cost about
**$197k**. That is the iBonds less IBTM's floor shares: $183,850.85 minus 3,361 × $21.65 = $111,085, plus bonds
$84,801 and about $1.3k of accrued interest. It is two-thirds of the real-plan ladder, because WInS shows Laura's plan
after both deposits, scaled by 300/450 (`notes_and_discussions.md:308`). **Fix:** one scale clause, once, in IBTR (as
the 15 Oct brief decided). Never call the WInS book "Laura's portfolio".

---

## 3. What can still be done in WInS before the 6 Nov freeze (without trading for show)

| Action | Allowed? | Worth it? | Verdict |
|---|---|---|---|
| Do nothing; log each check | yes | yes: the rule says hold (F-03) | **Default** |
| Trigger B (sell VT, buy IBTM) | yes (2 trades, $50) | below the $2,500 minimum unless yields fall another 18bp+ (fixed floor) or 69bp+ (V5 reading) | Restate or retire by 18 Oct; probably no trade |
| Trigger D (1.375% Nov-2040 swap) | yes (sell day 1, buy day 2; not day trading) | only if WInS now lists it and its price passes the 25bp check; the window closes Wed 21 Oct 06:30 Sydney | Check the listing by Sat 17 Oct; it is too late to make it a TNA pick safely |
| Trigger C (spare cash into VT) | yes | cash about $3.5k, below the $6.3k threshold (`october_trade.md:44`); the iBond distribution around 6 Nov adds roughly $600 | No |
| Add notes to old trades | technically yes (`wins_notes.csv:17`) | risks "at the time" (`wins.txt:43`) and quote ambiguity | No, not before the TNA (F-05) |
| Buy a T-bill ETF with spare cash | yes | about $12 of interest a month against a $25 commission, and it looks staged | No |
| Screenshot Trade Notes (all 15), Order History, Transaction History, Session Rules | yes | essential: WInS access after the freeze is UNVERIFIED; the Final Report needs evidence | **Yes**, by Sun 18 Oct, team Drive only (they show the username) |

Rules that apply to any further trade: commissions $25 per ETF and $10 per bond; no day trading; the volume rule
(F-16); position limits are not binding (200% per ETF, `wins_notes.csv:13`); trading ends Fri 6 Nov 4:00 pm ET (Sat
7 Nov 08:00 Sydney); after 1 Nov Sydney is 16 hours ahead.

---

## 4. Submission day: what could go wrong

| Risk | Guard |
|---|---|
| Only the team leader can submit (Rules & Roles) | Ray submits **Thu 22 Oct Sydney**. That leaves a one-day buffer before Sat 24 Oct 08:00 (= Fri 23 Oct 5:00 pm ET). |
| The form is not what we expect (an upload, separate boxes, a word counter) | Ray records the form by Sat 17 Oct (F-11) |
| The SMApply word count differs from Google Docs | Aim for 95 words or fewer by the strictest counter; hyphenated names and "$300,000" count differently |
| A note is altered by paste or autocorrect | Plain-text paste from WInS plus a character check (F-13) |
| The cancelled IBTR note is quoted | Quote the 7 Oct 04:42:53 AM ET note only. Its text has "about 0.2"; the cancelled one has "0.3" |
| A stale number in IBTR | F-01 and F-17: use a fixed date and logic for both outcomes |
| "Mark as Complete" is mistaken for submission, or a whole-application submit locks later tasks | F-11; screenshot the status |
| Times given in Sydney time | Use WInS ET times as shown |
| An AI tool types into SMApply or WInS | Students only. The 15 Oct brief item 2 still stands. |

---

## 5. Checklist for the next 7 days (Sydney dates)

- **Fri 16 Oct**
  - Ray: read the Week-One email and the logged-in Trading Details, read-only; record the exact words of any
    activity rule (F-10).
  - Rates analyst: re-run the ladder on the 15 Oct curve and log "4.7bp left" (F-01).
- **Sat 17 Oct**
  - Ray: open the SMApply TNA task without submitting; record fields, limits, text or upload, and how the roster
    task's status looks (F-11).
  - Trader and checker: check whether WInS lists the 1.375% Nov-2040 bond (trigger D).
- **Sun 18 Oct (vote set A, logged)**
  - Restate or retire trigger B on the WInS basis (F-03).
  - Agree what the TNA and IPS say if the line is crossed, and about the 2027 leftover (F-02).
  - Record the outcome of the VT "copout" debate (F-08).
  - Decide on AI disclosure in the TNA (F-15).
  - Confirm the picks: IBTR, IBTM, VT; alternate the Feb-2037 bond.
  - Recorder: screenshot Trade Notes (all 15), Order History, Transaction History and Session Rules to the team Drive
    only. Fill the Trade Log (G5).
- **Mon 19 Oct**
  - Each writer outlines (bullets, own words) covering: the three bullets (R4-R6); one distinct decision type (F-08);
    one link to the other picks.
  - IBTR adds the why-lock-early clause (F-07) and the scale clause (F-20).
  - IBTM adds liquidity timing (F-06) and the floor wording agreed in vote set A.
  - VT adds sizing, the honest role and the alternative rejected (F-14).
- **Tue 20 Oct**
  - Writers draft the reflections. IBTR is drafted with both branches ready (F-01).
  - Log the trigger check on the 20 Oct close after the window closes (06:30 Sydney Wed 21 Oct).
- **Wed 21 Oct**
  - Rates analyst: run the 20 Oct-curve figure and commit the script and output. The writer inserts it.
  - The outside reader scores the drafts. The editor checks: 95 words or fewer by two counters; no "guaranteed /
    secure / never / promised / locked / matched / risk-free"; no 2031 dollar range, reserve size or WInS gain; every
    number dated; the same floor wording and ladder date as the IPS plan.
- **Thu 22 Oct**
  - Ray pastes each note from WInS as plain text. A second student checks it character by character (294 / 292 / 288).
  - Add the identifier lines if the form allows (F-12).
  - Submit. Screenshot the status. Log it, with the AI-use entry.
  - Then: **no new WInS notes and no trades** unless a logged pre-set rule fires.

---

## 6. Still UNVERIFIED
- The SMApply TNA form's fields and limits, and whether "Mark as Complete" is the submission for this programme.
- The contents of the Week-One email and of any "required trading activity" rule.
- When the 6 Oct email arrived relative to the IBTM order (G3).
- The fill (execution) dates in WInS Transaction History.
- Whether WInS remains viewable after 6 Nov.
- What time treasury.gov posts each day's curve.
- How much the TNA counts in Top 50 selection.
- Whether WInS now lists the 1.375% Nov-2040 or 2.000% Nov-2041 bonds.
- The random-walk probabilities in F-01 and F-03 are MODEL, assuming 2026's daily volatility and no drift.

Working files: `oct16/lenses/L05/code/ladder_series.py`, `oct16/lenses/L05/ladder_series_out.txt`,
`oct16/lenses/L05/data/par2026.csv` (all under the scratchpad).
