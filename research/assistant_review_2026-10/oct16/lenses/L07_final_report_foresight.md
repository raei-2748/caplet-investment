# L07: Final Report and finale foresight

Prepared Fri 16 Oct 2026 (Sydney) for Team Caplet. AI-generated analysis (Claude). It is knowledge for the team, not
text to submit. It contains no Trading Notes reflections, IPS text, pitch or Final Report prose. If the team uses any of
it, record that use in the Final Report's Works Cited (Wharton AI policy).

**Labels.** VERIFIED = read in the primary file or page. FORECAST = my prediction from past years; replace it with
Wharton's instructions on Mon 9 Nov ET (Tue 10 Nov Sydney). MODEL = a computed estimate. UNVERIFIED = not confirmed.
Repo paths are in `/home/user/caplet-investment` unless marked `caplet-latest/` (branch claude/fervent-edison-sqk1ry,
commit 412e9e3). Web pages were accessed 16 Oct 2026. "Evidence pack" = `oct16/research/KB_what_wins.md` (its
UNVERIFIED items stay unverified here).

**Privacy.** First names only. No usernames, account numbers or surnames. The public fork is called "a team member's
fork".

---

## 0. Bottom line (eight points)

1. **The Final Report (FR) carries three of the five criteria almost alone.** Portfolio Analysis (projections "under
   varying market outcomes"), Articulation (teamwork, growth, challenges) and the co-sponsor half of Creativity cannot be
   shown in a 500-word IPS that bans charts and calculations (IPS:51-52, 68-70, 123). The Top 50 is picked on the IPS
   and FR (Rules page, evidence pack [W2]). So the FR is where Caplet wins or loses the Top 50.
2. **The writing window is 25 days, and the school year ends inside it.** Instructions come Mon 9 Nov ET; the FR is due
   Sat 5 Dec 09:00 Sydney. Knox Term 4 ends Thu 3 Dec (Presentation Day) and Fri 4 Dec is a staff day (Knox term-dates
   page, accessed 16 Oct 2026). Last year 30 of 63 dated comments in the Knox FR doc were made in the final two days,
   including "Make up stories" (`team/google_drive/2025_knox_wharton.md:3827`). This year that pattern would fail.
3. **Most of the FR can be built before 9 Nov,** because the case already lists what it must contain
   (`Laura_Gao_2026_Client_Profile.txt:94-124, 146-149`). What cannot wait is the evidence: dated decisions, WInS
   records, the AI-use record and the sources. Several of these do not exist yet (trade log empty, journal stops 7 Oct,
   AI log has no entries 1-15 Oct).
4. **FORECAST shape:** title page; a summary/reflection page (team reflection of about 150 words, maybe an advisor
   reflection); Portfolio-at-a-Glance with two snapshots (WInS and the recommended plan) and a "same or different"
   answer; 5-8 pages of report details; a separate APA Works Cited that records AI use. A page range with a **minimum as
   well as a maximum** is likely ("Reports that go over or under this range will not be reviewed", 2023-24).
5. **Pick one valuation date and one basis for every FR number.** I recommend the 6 Nov freeze close and the holdings
   basis. The 15 Oct ladder cost was $297.8k (forward) or $298.6k (yields unchanged) on Caplet's real holdings, against
   the number sheet's $294.5k, which prices dates Caplet does not own. Over 25 Sep-15 Oct the holdings-basis cost moved
   between $291.4k and $297.8k (MODEL, my re-run). The room under $300k ($1.4k-$2.2k) is smaller than one day's move and
   smaller than the gap between two reasonable pricing methods. Say "about break-even, and here is the rule if it costs
   more", not a precise surplus.
6. **Measure the WInS book against the payments, not against the market.** Wharton does not score returns
   (Guide:74-78). The right evidence of good implementation is that the ladder's value moved with the value of the
   payments it covers. Start a weekly record now. Expect about $1,539 of Treasury coupons on 15 Nov to pile up as cash
   in the frozen book (my arithmetic), which conflicts with V5's "income reinvested".
7. **The AI kit has parked a backlog of "note-in-Final-Report" items** (10 triage items, 7 decision memos). At least
   three memos the FR is told to use are on the banned STRIPS basis and the 28 Sep curve, with no banner. Importing them
   would put superseded numbers and AI work into the FR.
8. **Finale readiness is low today.** The key calls were deferred to AI (CLAUDE.md:75), V5 is "Best version that AI
   generated" (V5 comment, `01_version_5.md:36`), and every number is AI-built. Section 7 lists 30 hard questions with
   what a good answer must cover, and a "no-laptop" test.

---

## 1. What is already fixed (VERIFIED) and what commit 412e9e3 changes

### 1.1 Fixed by official text

| Requirement for the FR | Exact source |
|---|---|
| Purpose: "Evaluate implementation of the IPS strategy and present the team's analysis and recommendations for the client's operating commitment, facility contribution, financial flexibility, and communication with co-sponsors across varying outcomes." | `2026_WGY_Investment_Competition_Guide.txt:146-152` |
| Hindsight rule: "You may identify decisions you would make differently, but you may not redesign your strategy after observing the results." | Guide:158-159 |
| "Your portfolio and Final Report should reflect the strategy established in your IPS." | Guide:60-61; IPS:75 |
| Operating reserve: recommend "its size and initial asset composition and explain how its composition should change"; "define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions" | case:94-99 |
| Facility contribution: "recommend and justify the extent to which Laura can responsibly contribute" | case:104-106 |
| 2031: "recommend the dollar range ... and state how confident they are"; favourable and unfavourable outcomes; the range "must also protect" the payments | case:117-120 |
| "draft part of Laura's fundraising materials" | case:123-124 |
| Assumptions on performance, cash-flow timing, outside funding, inflation (projections and facility costs), flexibility | case:146-149 |
| Projections start at $300,000 (2027) + $150,000 (2028); WInS gains or losses are not added | case:129-133; Guide:70-73 |
| "Relevant sources and supporting evidence must be included in the Final Report." (the IPS's sources too) | IPS:124-125 |
| School documentation "submitted along with your Final Report as a separate file"; "Do not wait until the last minute" | `smapply_public_2026-10-14/deliverables.txt:52` |
| "Evaluators will consider the three deliverables together." | case:161 |
| Criteria text (five) | deliverables.txt:55-59 |
| Out of scope: facility cost, budget, funding gap, business plan, taxes, Taiwan law | case:164-169 |

### 1.2 What the 16 Oct commit changes for the FR

- **Numbers.** `caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md` gives FR-type numbers: the 2031 range
  (about $145k-$168k), "about 99%" confidence, the coupon-reinvestment table ($11k / $21k / $31k shortfall at 1 / 2 / 3
  points lower), allocation by date. These are FR material, not IPS material (IPS:68-70). Its headline ladder cost
  ($294k, room $5.5k, "1 case in 3") is on the payment-date basis, not Caplet's holdings (section 4). The 2031 range is
  mostly unaffected by that basis while the ladder still costs under $300k, because the floor and the stock fund come
  from the 2028 deposit; the 2027 leftover (first buffer) is smaller on the holdings basis.
- **The October curve file** (`caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`) is a
  usable official source for FR numbers. It must be extended to the chosen valuation date.
- **The [AI] suggestion rule** (`caplet-latest/CLAUDE.md:26-30`; `caplet-latest/COMPETITION.md:141-143`). The FR is
  where "authentic team voice" (deliverables.txt:59) and true teamwork stories (Ethics: do not "invent teamwork and
  experiential stories", Rules page, evidence pack R2 1.6) matter most. Accepted [AI] wording in the Articulation or
  co-sponsor sections is the highest-risk use of the rule. The Works Cited must then record it exactly. This lens does
  not draft any FR text.
- **Unchanged:** the FR forecast, the evidence gaps and the finale risks below.

---

## 2. FORECAST: what this year's Final Report will most likely require

Built from Wharton's own past FR specifications (2022-23, 2023-24, WordPress page 3768, re-read 16 Oct 2026 from
`oct16/research/KB_verify/wp_3768.json`), last year's Knox FR doc, and this year's case and criteria.

| Element | Evidence | Likelihood | What Caplet must have ready |
|---|---|---|---|
| Five criteria apply as written | deliverables.txt:55-59 | Very high | Self-check each section against the exact words |
| TNR 12, double-spaced, 1-inch margins, PDF, 5 MB, no external links | 2023-24 ("12-point font; Times New Roman Double spaced 1-inch margins ... not exceeding 5MB"; "Do NOT include external links"); IPS:110-123 | Very high | A blank template set up now |
| Audience = the portfolio manager (teacher/advisor) | 2023-24: "Your report should be directed to Wharton Global Asset Management's (WGAM) portfolio manager (your team's teacher/advisor)"; this case: "Your portfolio manager (your team's teacher/advisor ...)" (case:4) | Medium-high | Write to the PM; the fundraising part is written for co-sponsors |
| Page range with a minimum and a maximum | 2022-23: 9-12 pages, outside the range "will be disqualified"; 2023-24: 10-13 pages + Works Cited, "Reports that go over or under this range will not be reviewed", Report Details "must be a minimum of 5 pages" and "a maximum of 8 pages" | High that a range exists; numbers UNVERIFIED | Modules that can grow or shrink; do not plan a 6-page report because "less is more" |
| Title page: team name, names as "First Name, Last Initial", WInS username | IPS:84-100; 2025-26 midterm (evidence pack) | High | Copy exactly from the roster; keep the username out of the repo |
| Team reflection, about 150 words | Last year's Knox doc: "Section 2: Describe in 150 words or less, your takeaways from this team's competition experience." (`2025_knox_wharton.md:247`); 2022-23/2023-24 summary pages had 75 + 75 + 150-word boxes | Medium | Real takeaways from the learning log |
| Advisor reflection, about 150 words, written by the advisor | 2022-23, 2023-24 (page 3768); last year's doc "SECTION 2: ADVISOR AND TEAM REFLECTIONS" (`2025_knox_wharton.md:84-86`) | Medium | Advisor told now; give the advisor the evidence log; the advisor writes it |
| Portfolio-at-a-Glance with two snapshots: the WInS portfolio and the recommended portfolio | 2023-24: "Page 4 must include two graphic/visual portfolio snapshots: Your team's WInS Portfolio [and] Your team's Final Re[commended Portfolio]"; 2025-26 email: "Portfolio-at-a-Glance" (evidence pack [X2]) | High | Freeze-day WInS capture; a plan table by date (section 5) |
| "Same or different" answer, about 150 words | 2023-24: "Why are your WInS Portfolio and Recommended Portfolio for Hilary the same? ... different?" | Medium | One mapping, stated one way (section 5) |
| Report details: strategy; analysis and decision-making; growth and learning; challenges; takeaways | 2025-26 team docs (evidence pack R2 2.1); last year's Knox Section 5 A-E (`2025_knox_wharton.md:174-235`) | High-medium | The decision log, challenges log and learning log (section 6) |
| The case analytics (reserve, certainty, facility, 2031 range, fundraising draft, assumptions, good/bad outcomes) | case:94-124, 146-149 | Very high | Numbers from IPS principles only, on one valuation date |
| Evaluation of implementation; "decisions you would make differently" without redesign | Guide:146-159 | Very high | Implementation scorecard (finding FR-05) |
| Separate Works Cited, APA, including AI with "1-2 sentences on how you used that AI tool" | 2023-24 (page 3768); AI Policy: "how you use it must be recorded in your Works Cited pages" | High | A true AI record (finding FR-11) and an APA source list |
| A Trading Notes section again | 2022-23 to 2025-26 had one; this year it is separate (TNA) | Low | Refer to the TNA trades; do not re-quote at length |
| Pitch / "what makes us unique" box | 2022-23, 2023-24 (75 + 75 words) | Medium-low | Keep the IPS pitch as the single version |
| Cash allowed in the recommended plan | 2025-26 list began "Aside from cash"; 2026-27 list omits cash (evidence pack 6.1) | UNVERIFIED | Say where waiting money sits using a WInS-listed fund if cash is not allowed |

**Release-day drill (Tue 10 Nov Sydney).** Within 24 hours: map every instruction line to an existing module; list
anything new; re-check page limits, word limits per box, and whether charts are allowed; assign each section one
student owner.

---

## 3. How the five criteria are likely to be read in the FR, and how the three deliverables are judged together

### 3.1 The FR criterion by criterion (INFERENCE from the criterion words)

| Criterion (exact words abbreviated) | Where a reader looks in the FR | Caplet's material today | Gap to close before 9 Nov |
|---|---|---|---|
| **Investment Strategy**: "clear and creative investment thesis", "disciplined planning across Laura's changing time horizons and cash-flow needs", "appropriate diversification", "consistency with the team's IPS" | Opening page; strategy section; timeline chart | One idea (each deposit has one job; payments first); a dated ladder | The diversification case (93% one issuer) is not argued in student words; FR must use IPS words and numbers exactly |
| **Client Knowledge**: "circumstances, priorities, risk considerations, and residency goals"; "recommendations that can earn her confidence" | Client section; reserve and facility recommendations; co-sponsor draft | Case facts; willingness vs capacity notes | Client Portrait is a placeholder (`client_portrait.md:14-15`); residency never described in team files (L02 CLIENT-16) |
| **Portfolio Analysis**: "concepts and tools"; "quantitative and qualitative"; "reasonable assumptions and projections ... funding reliability, the facility contribution, and financial flexibility under varying market outcomes" | Projections, scenarios, sensitivity tables, assumptions box | AI-built models and number sheet | Student-owned rebuild of at least the ladder cost and coupon table; one valuation date; stated return/inflation/FX assumptions |
| **Articulation**: "teamwork, communication, and learning"; "research and decision-making process"; "growth and response to challenges" | Report details (decision-making, growth, challenges); team reflection | Journal of 10 bullets to 7 Oct (`final_report.md:16-27`) | Dated decision log, meeting notes, roles, the 7 Oct incident told truthfully, AI role told truthfully |
| **Creativity and Presentation**: "compelling, well-organized narrative in an authentic team voice"; "uses data effectively"; "original thinking and meaningful reflection"; co-sponsor communication "clearly and credibly" | Whole report; charts; fundraising draft | A strong single idea; co-sponsor research (`strategy_notes.md:16-22`) | Charts that answer client questions; a fundraising draft written by students; no AI voice |

Note on Creativity. The 2022-24 wording "visually pleasing presentation of data; many creative elements" is gone
(evidence pack 2.3). "Uses data effectively" rewards fewer, purposeful charts, not decoration.

### 3.2 How the three deliverables are judged together

- **Weight.** The Rules page names the IPS and FR for the Top 50 (evidence pack [W2]); SMApply says all three are
  evaluated (deliverables.txt:27); the case says "together" (case:161). Safest reading: the TNA is evidence read beside
  the other two; its weight is UNVERIFIED.
- **What each deliverable proves.** TNA: decisions at trade time (uneditable notes). IPS: the rules of the strategy.
  FR: the numbers, the evaluation and the story. A reader can check each claim three times.
- **The joints a reader will test** (each must read the same in all three): the plan's name; the floor (face $150,000
  vs quoted $145,000); the ladder-cost basis and date; the shortfall order; the stock share (about 7-9%); "hold"; the
  2031 range method and its valuation date; what the WInS book represents.
- **IPS hooks the FR needs.** Every FR computation must rest on a principle already in the IPS, because the strategy
  freezes on 6 Nov (IPS:72-74). Checked against V5 (`team/google_drive/ips_report/01_version_5.md`):

| FR must compute | Hook in V5? | Line |
|---|---|---|
| Reserve size and composition, how it changes | Partial: "In 2033 the payment Treasuries become the operating reserve, shrinking as each payment is made" | 01_version_5.md:26 |
| Definition and test of "high degree of certainty" | No definition, no test ("with high certainty"; "depends mainly on the US government") | :20 |
| Facility contribution rule | Yes: floor + half the fund, capped | :30 |
| 2031 range method | Yes, but no valuation date ("value then") | :30 |
| Shortfall order | Yes ("2027 leftover, then the half Laura keeps, then the contribution above the floor") | :26 |
| Return assumption for projections | No | - |
| Inflation and FX assumptions | Named, not quantified | :28 |
| Flexibility kept | Yes ("The other half stays with Laura as a cushion") | :30 |

- **Sources for IPS claims land in the FR.** IPS:124-125 sends IPS evidence to the FR. Any IPS sentence the team cannot
  source (for example the pitch's claim that co-sponsors "rarely pay to run it", 01_version_5.md:16) becomes an
  unsourced claim in December. Keep only claims the team can cite.

---

## 4. The ladder-cost conflict, resolved for FR use

Re-run on the 15 Oct treasury.gov par curve with the same bootstrap as the evidence pack
(`oct16/research/KB_verify/num/reconcile.py`), output below (MODEL, VERIFIED reproduction):

| Dates priced to | Forward value at 1 Jan 2027 | Today's curve held unchanged |
|---|---|---|
| Payment dates 1 Jan 2033-2042 (number sheet basis) | $294,461, room $5,539 (19.0bp) | $295,246, room $4,754 (16.3bp) |
| Maturities Caplet owns (iBonds 15 Dec 2032-36; T-bonds Feb-2037, May-2038, Nov-2039/40/41) | $297,847, room $2,153 (7.4bp) | **$298,628, room $1,372 (4.7bp)** (the lenses' $298,624) |

- **Reason.** Same curve, same ten $50,000 payments. About $3.4k of the gap is dates: Caplet's bonds mature 0.5 to 10.5
  months before each payment, so each $50,000 is bought for an earlier date and costs more
  (`caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:70-89` prices to `dt.date(y, 1, 1)`). The rest (~$0.8k)
  is forward vs unchanged.
- **Which is right for which claim.** For anything about Caplet's plan or WInS book (FR, IPS, TNA reflections): the
  holdings basis, with the date and method stated. The $294.5k figure is the price of an ideal ladder Caplet does not
  own. The number sheet's "1 case in 3" is scaled to the wrong basis (`ips_numbers.py:122`).
- **New: the room is inside the noise.** My series (`oct16/lenses/L07/series.py`, output `series_out.txt`) shows the
  holdings-basis forward cost at $291,389 on 5 Oct and $297,847 on 15 Oct, a $6.5k range in ten days; it rose $2.7k on
  15 Oct alone. A student-level check (each $50,000 discounted at the 15 Oct par yield for its maturity,
  `oct16/lenses/L07/simple.py`) gives $299,995, about $1.4k above the bootstrap. So the room is smaller than one day's
  move and smaller than the gap between two sensible methods. The honest FR and finale claim is "about break-even at
  mid-October yields; if it costs more on 1 Jan 2027, the 2028 deposit completes the ladder first and the floor is
  lower by that amount" (V5's own rule, 01_version_5.md:24), not a dollar surplus.
- **Valuation date for the FR.** Use the 6 Nov close (the freeze), state it once, and give a sensitivity line (about
  $290 per 0.01 point, holdings basis; my calc from the same run). Laura buys on 1 Jan 2027, after the FR is
  submitted, so every cost in the FR is a forecast and must say so.

---

## 5. Portfolio-at-a-Glance: three dated portfolios and one WInS book

- **Caplet's plan is not one portfolio.** It has a Jan 2027 book ($300k: ladder plus leftover), a Jan 2028 book ($450k:
  ladder, IBTM floor, VT) and a 2033 operating reserve that shrinks yearly (number sheet section 4,
  `IPS_number_sheet.md:56-62`). The FR snapshot of "the recommended portfolio" must say which date it shows. FORECAST:
  show Jan 2028 (both deposits), with a one-line note on Jan 2027.
- **What the WInS book represents.** The team sheet says: "Laura's plan on 2 Jan 2028, after both deposits, scaled to
  WInS's $300,000 starting cash" (`team/google_drive/sheets/portfolio_and_trading_notes/portfolio.csv:2`); IBTM 32.6%
  does two jobs (Jan 2033 payment + floor; 1,142 + 3,361 shares, portfolio.csv:38-39); VT 8.7%. L08 found three
  different mappings in team files (COH-06). The "same or different" box must give one.
- **The WInS screen will mislead.** WInS labels the iBond ETFs "Long Equities" (61.6%) though they hold Treasuries
  (COMPETITION.md:98). A pasted WInS pie chart would tell a first-time reader the book is about 70% stocks. Build
  the snapshot as a team table (holding, job, payment year, value, weight) from WInS numbers, and say why it differs
  from the WInS label.

---

## 6. What to START COLLECTING NOW (evidence ledger)

Store on the team Drive, not the public repo (names, usernames and the school letter must stay private). Each row: what,
why (criterion or forecast element), source, owner role, first date. Owners are roles; the team assigns students.

| # | Item | Why | Source / how | Owner role | Start |
|---|---|---|---|---|---|
| 1 | **Decision log** (date ET + Sydney, decision, options, evidence file, who proposed, who challenged, vote, AI involvement, result, what we would do differently) | Articulation "decision-making process"; Q&A | Back-fill from 27 Sep using chat logs, emails, Doc histories; never invent | Historian | Now |
| 2 | **Evidence file per decision** (the number or page used, saved as dated PDF/screenshot) | "Supporting evidence must be included" (IPS:124-125) | Treasury curve CSV for the date; WInS screens; iShares pages | Each decision owner | Now |
| 3 | **Meeting notes** (date, length, who attended by first name, decisions, actions) | Teamwork, communication | Zoom/chat; 5 lines each | Historian | Every meeting |
| 4 | **Roles and artefacts** (who owned what, with one artefact each) | Articulation; every member must speak at semifinals ("All team members must participate", faqs.txt:89) | Team sheet | Lead | This week |
| 5 | **Challenges log**: 7 Oct cancelled-order incident (time, order, how found, response, rule changed); stale WInS bond prices (29-30 Sep); IBTN mix-up; sector-rule myth (5 Oct); 6 Oct email; night trading from Sydney; ladder cost swings | "response to challenges" | `final_report.md:17-27`; COMPETITION.md:87-100, 192-193 | Historian | Now |
| 6 | **Learning log** ("what this taught me", one line per student per week) | "learning", "growth", "meaningful reflection"; team reflection | Each student writes their own | Every student | Weekly |
| 7 | **AI-use record** (date, tool and model, task, output, what students kept or rejected, exact accepted [AI] wording, who read which AI example) | Works Cited ("in any way"); authenticity | Back-fill 1-15 Oct gap; add the 16 Oct reviews | AI-log keeper | Now |
| 8 | **Source list, APA, with access dates** (case, Guide, treasury.gov curves by date, iShares iBond pages and fact sheets, Vanguard VT, JPM 2026 LTCMA, Taiwan CPI and construction index, FX source, the seed-gift study behind `strategy_notes.md:22`) | Works Cited; IPS evidence moves here | One sheet | Rules lead | Now |
| 9 | **WInS capture**: Portfolio Summary, holdings (values, %), Order History (filled and cancelled), Transaction History (fills, accrued interest, commissions, distributions, coupons), Trade Notes, Session Rules | Portfolio-at-a-Glance; implementation scorecard | Weekly from now; full capture after 4:00 pm ET Fri 6 Nov (08:00 Sat 7 Nov Sydney); crop out username and account number | Recorder | Now |
| 10 | **Trade log filled** (the sheet's Trade Log is empty, `trade_log.csv:2-60`) | Evaluate implementation | From item 9 | Recorder + checker | This week |
| 11 | **Trigger checks and "decisions not to trade"** (date, rule, numbers, answer) | "disciplined decisions" (Guide:181-182) | IBTR note test; October rule | Rates analyst | Each week to 6 Nov |
| 12 | **Post-freeze tracking** (weekly 7 Nov-4 Dec): WInS value, cash, income received, ladder value vs value of the payments it covers, VT value, 10-year yield | Implementation evaluated "across varying outcomes" without return-chasing | WInS + treasury.gov | Rates analyst | 7 Nov |
| 13 | **Valuation-date data pack** (6 Nov curve; prices; iBond yields) | One basis for all FR numbers | treasury.gov CSV; WInS | Rates analyst | 7 Nov |
| 14 | **Chart data** (5 charts, section 8) | "uses data effectively" | From items 12-13 | Chart owner | 1 Nov |
| 15 | **Co-sponsor facts checklist** (US$ range, confidence, cap, who bears FX, no matching offer, no invented quotes; research behind each claim) | Fundraising draft is judged in Creativity | `strategy_notes.md:16-22`; `notes_and_discussions.md` | Client/co-sponsor lead | Before 9 Nov |
| 16 | **School documentation letter** | Required with the FR | Template fields (section 9) | Lead via advisor | Ask now |
| 17 | **Advisor heads-up** (possible 150-word advisor reflection) | Forecast | Advisor writes it | Lead | Now |
| 18 | **Availability calendar** (exams, travel) for 10 Nov-4 Dec and late Jan-Apr 2027 | Writing plan; semifinal | Team sheet | Lead | Now |

---

## 7. Finale readiness and 30 hard questions (FORECAST)

No list of real judge questions is public (evidence pack R3; `R3_outside_coverage.md:422`). These are forecasts built
from the case, the criteria, and past panels (an Aberdeen fixed-income or credit judge sat on every finale panel
2024-2026; finales gave 10 minutes of pitch and about 5 minutes of questions; evidence pack 2.2, 2.5). The answers must
be the students' own; this list says what an answer must cover, not what to say.

**Readiness today.** Low. "The team deferred to the assistant's evidence-based calls" (CLAUDE.md:75); the IPS draft's
own comment says "Best version that AI generated" (01_version_5.md:36); every number is AI-built (L01 JUDGE-11). Past
semifinals required every member to "briefly explain how they contributed value to the team" and banned "completely
new material" (2025-26 Semifinalists Next Steps PDF, evidence pack [D1]).

**No-laptop test (suggested).** Every second week, each student answers five of the 30 aloud, without notes or AI, in
60 seconds, with the right number to within 10% and its date and basis. Anything that fails goes into the learning log.

**Numbers every student should know** (date and basis always stated):

| Number | Value | Source |
|---|---|---|
| Deposits | $300,000 Jan 2027; $150,000 Jan 2028 | case:43-45 |
| Payments | 10 x $50,000, each 1 January 2033-2042, fixed | case:88-90 |
| Ladder cost, holdings basis, 15 Oct | $297.8k forward / $298.6k yields unchanged; room $1.4-2.2k (4.7-7.4bp) | section 4 (MODEL) |
| Ladder cost range, 25 Sep-15 Oct | $291.4k to $297.8k (forward, holdings) | `L07/series_out.txt` (MODEL) |
| Sensitivity | about $290 per 0.01 point | section 4 (MODEL) |
| Floor | $150,000 face; quoted $145,000 | `IPS_number_sheet.md:14` (MODEL) |
| Stock fund in Jan 2028 | about $32,000 (90% band $20k-$43k) | `IPS_number_sheet.md:15` (MODEL; L08 gives $33.5k on its basis) |
| 2031 range | about $145k-$168k (15 Oct) | `IPS_number_sheet.md:16` (MODEL) |
| Coupon shortfall if yields stay lower | $11k / $21k / $31k at 1 / 2 / 3 points | `IPS_number_sheet.md:30-36` (MODEL) |
| Global stock assumption | JPM 2026 LTCMA AC World 7.00% compound, 16.78% vol | CLAUDE.md key facts (VERIFIED there) |
| WInS book | 11 trades of 200; commissions $200; cash $3,513.79; about $301,950 on 13 Oct | COMPETITION.md:174, 188; `rb_tickets.csv` summary |

**The 30 questions**

| # | Question | A good answer must cover |
|---|---|---|
| 1 | In one sentence, what is your strategy and why does Laura need it? | Each deposit has one job; payments first because the case demands "a high degree of certainty" with no outside money (case:91-92); growth only with money not needed for payments |
| 2 | Why lock almost all of the first $300k into Treasuries instead of a growth portfolio with a glide path? | The cost of certainty vs the cost of a missed payment; what the growth-first test showed (re-run on WInS-listed instruments, not STRIPS); why waiting is a bet on rates |
| 3 | What does "high degree of certainty" mean to you, in numbers, and how did you test it? | Definition; test method; assumptions (case:97-99); what is not certain (coupon reinvestment, iBond payouts); US default as the residual risk |
| 4 | Your bonds pay coupons. What happens if yields fall to 2% and stay there? | Reinvestment risk; size (about $21k at -2 points, MODEL); who covers it in what order; the part that arrives after 2033 |
| 5 | Why iBond ETFs for 2033-2037 and not individual Treasuries? | WInS lists no Treasury maturing Feb 2031-Feb 2036 (COMPETITION.md:92-93); iShares funds "do not seek to return any predetermined amount"; final months in cash; fee |
| 6 | Your Feb-2037 bond matures 10.5 months before the payment it funds. What does that cost and where does the money wait? | Holdings vs ideal dates ($298.6k vs $294.5k); where cash waits (cash allowed or not, UNVERIFIED) |
| 7 | Your room under $300k is about $1.4k. What if the ladder costs more on 1 January? | "About break-even"; the 2028 deposit completes the ladder first; the floor is lower by the same amount; why the room is within model noise |
| 8 | What is the interest-rate sensitivity of your ladder, and why does a price fall not hurt Laura? | Matched cash flows held to maturity; about $290 per 0.01 point on the cost; prices and the payments' value move together |
| 9 | Laura has taken "thoughtful risks" all her career (case:69-71). Only about 7-9% of her money is in stocks. Too timid? | Willingness vs capacity; the price of certainty in dollars; what more stocks would buy and risk; Darren's 5 Oct challenge and how it was settled |
| 10 | Why VT and not the S&P 500, Taiwan stocks or gold? | Diversification; her career and residency already tie her to Taiwan and publishing; the team's actual comparison (re-run, not the STRIPS-era memo) |
| 11 | IBTM does two jobs. If it pays out 2% less than expected, which job loses? | The payment comes first; the floor is quoted rounded down ($145k vs $150k face) |
| 12 | About 93% of the portfolio relies on one issuer. How is that "appropriate diversification"? | The criterion's words; diversification by purpose; a dollar liability; what would happen in a US default; the US credit rating (check the current rating before quoting) |
| 13 | A fixed $50,000 loses buying power, and Taiwan building costs rose 6.5% last year. How does your plan handle inflation? | Payments fixed by the case (case:90); facility costs; Laura's kept half; numbers with dates (Taiwan CPI +2.04%, construction +6.53% y/y Aug 2026, CLAUDE.md) |
| 14 | Laura's costs are in Taiwan dollars. Who carries the currency risk? | The range is in US$; co-sponsors may judge in NT$; FX volatility; the kept half |
| 15 | What exactly would Laura tell co-sponsors in 2031, and how confident are you? | The range and its basis date; the confidence statement; what it does and does not promise |
| 16 | You say about 99%. Isn't that true by construction? What number actually tells Laura something? | Yes, the cap and floor make it so; the informative numbers are the chance of reaching the top and of landing below the middle |
| 17 | Markets crash in 2032 after she quoted the range. What does she say to co-sponsors? | The top was fixed in 2031; the gift falls toward the floor but not below it (barring a coupon shortfall); credibility |
| 18 | Why half of the fund to the facility and half kept? Why not 80/20? | The "responsible" test; flexibility the case names (case:101-103); the trade-off in dollars |
| 19 | How big is the operating reserve in 2033 and what does it hold each year to 2042? | The ladder is the reserve; it shrinks by $50,000 a year; composition does not change; each holding matures before its payment |
| 20 | What if the 2028 deposit is late or only $75,000? | The case says she "will" contribute (case:43-44); payments rest on the 2027 deposit; the floor and stock fund shrink |
| 21 | Why not rebalance when markets move? | The hold rule; review triggers; Guide:156-157 (planned adjustments vs rewriting); the "decisions not to trade" log |
| 22 | Your WInS book is $300k; her plan is $450k. How does one represent the other, and why does WInS call your bond funds "Long Equities"? | One mapping (Jan 2028 plan scaled to $300k); the IBTM split; the platform label vs the holdings |
| 23 | Walk us through one trade note: what did you know then, and what changed? | The IBTR note's "about 0.2 percentage points" (true on 6 Oct, 22.7bp) vs 4.7bp on 15 Oct; what the rule said; why the team held |
| 24 | Tell us about a mistake. What happened on 7 Oct? | An AI browser click cancelled the wrong order (COMPETITION.md:192-193); how it was found; what changed (only one student places or cancels; the rule on AI); what it cost; Wharton's "run with it" advice (faqs.txt:66) |
| 25 | How did you use AI, and how do we know this work is yours? | What AI did (models, memos, reviews, example notes, the WInS click); what students decided and wrote; the Works Cited record; a student re-derives a number live |
| 26 | Who made the decisions? What did your advisor do? | Students decide; "Advisors may not make decisions on behalf of students" (Rules page); the case's PM role-play (case:4) is fiction |
| 27 | What did each of you contribute? | One artefact per student; honest, no ranking |
| 28 | What would you do differently, without changing the strategy? | Implementation-level lessons only (Guide:158-159); see finding FR-16 |
| 29 | If Laura asked for more risk and a bigger gift, what would you change and what would it cost her? | The floor-vs-stocks trade-off in dollars (re-run on current inputs); which number she gives up; the review rule |
| 30 | Why should Laura choose your plan over a team that promises a bigger gift? | Credibility with co-sponsors (case:114-116); payments that cannot depend on markets; plain, checkable numbers |

---

## 8. Charts the FR will likely need (data to collect now)

Each chart answers one client question. None go in the IPS (IPS:123).

| Chart | Client question | Data |
|---|---|---|
| Cash-flow timeline 2027-2042 | "When does money come in and go out, and what pays each payment?" | Deposits; ten payments; maturity of each holding |
| 2031 range | "What can I promise co-sponsors?" | Floor; distribution of half the fund on the valuation date (p5 / p50 / p95) |
| Coupon-reinvestment sensitivity | "What could still go wrong with the payments?" | Shortfall at 0 / -1 / -2 / -3 points; who covers it |
| Ladder vs payments during WInS | "Did the implementation do its job?" | Weekly ladder value vs value of the payments it covers (item 12) |
| Allocation over time | "How does my portfolio change as payments approach?" | Jan 2027, Jan 2028, 2033, then the reserve shrinking yearly |

Students build every chart from data they can explain. The kit's PNG charts are AI work and partly STRIPS-era.

---

## 9. Calendar to 5 Dec (Sydney)

| Date | Step |
|---|---|
| Now-Sun 18 Oct | Start items 1, 5, 7, 8, 18; ask the advisor for the school letter; set up the FR template |
| Sat 24 Oct 08:00 | TNA due |
| By Wed 4 Nov | IPS hooks in place (section 3.2); "decisions not to trade" log current |
| Sat 7 Nov 08:00 | Trading freezes (4:00 pm ET Fri 6 Nov). Full WInS capture (item 9). IPS due 09:00 |
| Sat 7-Mon 9 Nov | Download the 6 Nov curve; rebuild FR numbers on the holdings basis |
| Tue 10 Nov | Instructions out (Mon 9 Nov ET). Release-day drill (section 2) |
| Sun 15 Nov | Outline and numbers frozen; chart drafts; coupons of about $1,539 expected on 15 Nov (finding FR-06) |
| Fri 20 Nov | School letter in hand |
| Sun 22 Nov | Full student draft; one human outside reader (unpaid, guidance only) |
| Sun 29 Nov | Works Cited complete; format and page check |
| Wed 2 Dec | Submit (target). Thu 3 Dec is Presentation Day and the last day of term; Fri 4 Dec is a staff day |
| Sat 5 Dec 09:00 | Hard deadline (5:00 pm ET Fri 4 Dec) |

School documentation template fields (VERIFIED, `2026_27_School_Documentation_Template.txt:1-28`): official letterhead;
date; the administrator's position; school name, country and full address; the advisor's first and last name; team
name; each student's first and last name, team leader first (up to six); the administrator's signature and date. It is
a separate file and contains full names, so it never goes in the repo. Later, semifinalists must also send letterhead
documentation and a signed Consent and Waiver of Liability, with a parent or guardian's signature for students under 18
(Rules page, evidence pack R4 5.1).

---

## 10. Findings

Severity: critical = likely blocks a Top-50 place or risks disqualification; high = materially lowers the score; medium =
noticeable weakness; low = polish. "New / known-deeper / known-repeat" is relative to the 15 Oct brief
(`oct14/final.md`).

### FR-01 (critical, known-deeper): The FR window is 25 days, ends after term, and last year's FR was written in two days
- **Problem.** Instructions arrive Tue 10 Nov Sydney; the FR is due Sat 5 Dec 09:00. Knox Term 4 concludes Thu 3 Dec
  (Presentation Day) and Fri 4 Dec is a staff day, so the advisor and the school administrator are hardest to reach in
  the last 48 hours. Last year's Knox FR doc shows 30 of 63 dated comments on 11-12 Dec 2025 (the deadline was 12 Dec),
  including "Make up stories, and make them sound realistic" and "that's how our make-up story goes" (lines 3827,
  3844). Last year's window was 46 days; this year's is 25.
- **Evidence.** deliverables.txt:51 ("shared on November 9"); Knox term dates page (accessed 16 Oct 2026): "Thursday 3
  December Presentation Day and Term 4 Concludes", "Friday 4 December Staff Professional Development Day";
  `2025_knox_wharton.md:3800-3890` (comment list; my count by date); evidence pack 1.2 (27 Oct to 12 Dec in 2025-26).
- **Fix.** Pre-build every module that does not depend on the instructions before 9 Nov (sections 2, 6, 8); target
  submission Wed 2 Dec; no section written in its owner's exam week. What it must achieve: on 10 Nov the team edits and
  fits, it does not start.

### FR-02 (high, new): Forecast the page range as a floor as well as a ceiling
- **Problem.** Wharton's past FR specs disqualified or ignored reports outside a page range at both ends. A team whose
  lesson is "complexity must earn its place" (CLAUDE.md:40) may write too little.
- **Evidence.** Page 3768, 2023-24 block (re-read from `KB_verify/wp_3768.json`): Report Details "must be a minimum of 5
  pages" and "a maximum of 8 pages"; "Reports that go over or under this range will not be reviewed. Reports that do not
  meet the minimum page requirement will not be eligible to receive participation certificates." 2022-23: 9-12 pages,
  outside the range "will be disqualified" (evidence pack [D6]).
- **Fix.** Plan modules for about 10-13 pages that can shrink or grow by a page (FORECAST). Depth fills pages, not
  extra frameworks: assumptions box, good/bad cases, implementation scorecard, decision story. Replace with the real
  range on 10 Nov.

### FR-03 (high, known-deeper): Portfolio-at-a-Glance needs two snapshots and one mapping; Caplet's plan has three dates
- **Problem.** The forecast snapshot of "the recommended portfolio" is ambiguous for Caplet (Jan 2027, Jan 2028, 2033
  reserve). The WInS book mirrors the Jan 2028 plan scaled to $300k, but team files state the mapping three ways. A
  pasted WInS chart shows the iBond funds as 61.6% "Long Equities".
- **Evidence.** 2023-24: "two graphic/visual portfolio snapshots: Your team's WInS Portfolio [and] ... Final
  Re[commended Portfolio]"; "Why are your WInS Portfolio and Recommended Portfolio ... the same? ... different?" (page
  3768); portfolio.csv:2, 38-39; COMPETITION.md:98; L08 COH-06; `IPS_number_sheet.md:56-62`.
- **Fix.** One table per snapshot (holding, job, payment year, value, weight), built from WInS numbers; one sentence on
  the scale and the IBTM split; a note on why WInS's label is wrong. Decide which date "recommended" means and use it
  everywhere.

### FR-04 (high, known-deeper): One valuation date and the holdings basis for every FR number; the room is inside the noise
- **Problem.** Two ladder costs on the same 15 Oct curve ($294.5k vs $298.6k) differ because they price different
  dates. Even on the right basis, the room under $300k ($1.4k-$2.2k) is smaller than one day's move ($2.7k on 15 Oct),
  the ten-day range ($6.5k) and the gap between a bootstrap and a simple par-yield method ($1.4k). Any precise
  "surplus" claim in the FR can be wrong by the time a judge reads it.
- **Evidence.** reconcile.py re-run (section 4); `L07/series_out.txt` (5 Oct $291,389; 14 Oct $295,163; 15 Oct
  $297,847); `L07/simple.py` ($299,995); `caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:70-89, 122`;
  `IPS_number_sheet.md:12-13`.
- **Fix.** Use the 6 Nov close as the FR's single valuation date and the holdings basis; state the method once; give a
  sensitivity line (about $290 per 0.01 point); describe January's purchase as "about break-even" with V5's top-up rule.
  Re-derive "1 case in 3" on the holdings basis or drop it.

### FR-05 (high, known-deeper): "Evaluate implementation" needs a plan-vs-actual scorecard, and its raw records are not captured
- **Problem.** The FR must "evaluate how effectively it implemented that strategy" (IPS:75-77), but the sheet's Trade
  Log is empty; fill prices are recorded only in COMPETITION.md's table (172-186), and accrued interest, commissions and cash after each trade are not recorded; fills slipped from the target
  (Fri 2 Oct ET) to 6-8 Oct; four notes sit on cancelled orders. Whether the team can still open WInS records after the
  season is UNVERIFIED.
- **Evidence.** `team/google_drive/sheets/portfolio_and_trading_notes/trade_log.csv:2-60` (blank rows); CLAUDE.md open
  items ("target fills Fri Oct 2 ET, hard stop Oct 9"); CLAUDE.md:9 (filled 7-8 Oct); 15 Oct brief section 2 (four notes
  on cancelled orders); COMPETITION.md:172-188 (fills; "Every weight is within 0.2 pt of target").
- **Fix.** Capture WInS records now and at the freeze (item 9). Build a scorecard: each order's target vs actual (weight,
  fill, time, commission), what went wrong and the rule it produced. What it must achieve: an evaluation built on
  WInS records a judge could check, not memory.

### FR-06 (medium, new): Track the book against the payments after the freeze; expect cash to build up
- **Problem.** The FR must evaluate the implementation without return-chasing. The informative measure for a matched
  ladder is whether its value moved with the value of the payments it covers. Separately, the frozen book will collect
  income it cannot reinvest: the four bonds paying in May and November (May-2038 4.500% on $20k face, Nov-2039 4.375% on
  $18k, Nov-2040 4.250% on $18k, Nov-2041 3.125% on $20k) pay about $1,539 on 15 Nov (my arithmetic: $450 + $393.75 +
  $382.50 + $312.50), plus iBond monthly distributions (amounts UNVERIFIED). V5 says income is "reinvested in the holding
  that paid it", which the frozen book cannot do. WInS also shows the May-2038 bond's last coupon as 15 Aug, so its
  payment date in WInS may differ (UNVERIFIED).
- **Evidence.** Guide:70-78; faqs.txt:59, 63 (bond coupons paid every six months; corporate actions reflected);
  COMPETITION.md:97, 172-188 (the coupon-date quirk; holdings and faces); portfolio.csv:25-29 (coupons);
  01_version_5.md:26.
- **Fix.** Weekly record from now to 4 Dec (item 12): WInS value, cash, income received, ladder value vs the value of
  the payments it covers on the same day's curve, VT. In the FR, explain the cash build-up as a feature of the freeze,
  and use wording on income that matches what WInS actually does.

### FR-07 (high, known-deeper): The AI kit's "note-in-Final-Report" backlog is partly on the banned STRIPS basis
- **Problem.** The kit parks material for the FR: 10 triage items marked "note-in-Final-Report" and 7 decision memos
  with a "Final Report: note-in-Final-Report" line. D_rivals and D_stress_bad_year model every payment as STRIPS and say
  to put their tables in the FR "with 'STRIPS basis' in the heading"; D_range_confidence_2031 is on the 28 Sep curve.
  None of these three carries the 14 Oct superseded banner that D_certainty_definition has. The 6 Oct email limits
  Laura's plan to WInS-listed securities. The FR outline still points to the abandoned plan.
- **Evidence.** `rab/redteam/triage.md` (10 rows "note-in-Final-Report", e.g. :54-62); `rab/decisions/D_rivals.md:12,
  14, 61`; `rab/decisions/D_stress_bad_year.md:14, 72`; `rab/decisions/D_range_confidence_2031.md:1-8, 75`;
  `rab/decisions/D_certainty_definition.md:1` (banner present); `deliverables/final_report_outline.md:5, 16`;
  COMPETITION.md:87-90.
- **Fix.** Before 9 Nov, the team lists which backlog items it actually wants, re-runs any number it keeps on
  WInS-listed holdings and the valuation date, and cites the AI origin. What it must achieve: no STRIPS-basis or 28 Sep
  number in the FR, and no AI table presented as student work.

### FR-08 (high, known-deeper): The FR carries three criteria almost alone; plan each section against the exact criterion words
- **Problem.** Portfolio Analysis, Articulation and the co-sponsor part of Creativity can only be shown in the FR (IPS
  bans projections, charts and citations; the TNA has 100-word reflections). Caplet's material for these three is the
  thinnest: AI-built projections, a 10-bullet journal, no student fundraising notes.
- **Evidence.** deliverables.txt:57-59; IPS:51-52, 68-70, 123; `final_report.md:14-27`; `client_portrait.md:14-15`;
  L01 JUDGE-10/11; L02 CLIENT-12.
- **Fix.** Use the table in section 3.1 as the FR plan; one owner per criterion checks the draft against its exact
  words. What it must achieve: each phrase of each criterion has a place in the FR where a reader finds it.

### FR-09 (high, known-deeper): The IPS must contain a hook for every FR computation, and only claims the team can source
- **Problem.** After 6 Nov, anything new is a strategy change (IPS:72-74; semifinal rule "Do NOT introduce completely new
  material", evidence pack [D1]). V5 has no definition or test of "high degree of certainty", no return assumption, no
  valuation date for the 2031 top, and only a partial reserve path. IPS sources must appear in the FR (IPS:124-125), so
  an unsourced IPS claim becomes a visible gap in December.
- **Evidence.** 01_version_5.md:16, 20, 24, 26, 28, 30 (table in section 3.2); case:94-99, 146-149.
- **Fix.** Before 6 Nov, check the hook table; add principles (not numbers) where missing; drop claims the team cannot
  cite. What it must achieve: every FR number reads as the IPS rule applied, never as a new rule.

### FR-10 (high, known-deeper): Articulation needs a true, dated record; the 7 Oct incident must be told as it happened
- **Problem.** Articulation scores "research and decision-making process" and "response to challenges". The team's best
  material is real (stale prices, IBTN, the sector-rule myth, night trading, the 7 Oct cancelled order), but the journal
  stops at 7 Oct with blanks, the key calls were deferred to AI, and last year's FR used quoted dialogue and votes under
  an instruction to make stories up. The 7 Oct click was made by an AI browser tool, so a truthful account names AI.
- **Evidence.** `final_report.md:16, 23` ("[who argued what]", "[fill in]"), :27; CLAUDE.md:14, 75; COMPETITION.md:192-193;
  `2025_knox_wharton.md:190, 214, 3827` (vote "4-2", the FMC story, "Make up stories"); Rules page Ethics ("invent
  teamwork and experiential stories", evidence pack R2 1.6).
- **Fix.** Items 1, 3, 5, 6 of section 6, back-filled only from records. For the 7 Oct story keep: time, order, how found,
  what changed, what it cost, what the team learned about tools in trading. What it must achieve: every story in the FR
  can be traced to a dated record.

### FR-11 (high, known-deeper): The Works Cited AI entry must be true, complete and specific
- **Problem.** Wharton requires that AI use "in any way" be recorded in the Works Cited; 2023-24 asked for "1-2 sentences
  on how you used that AI tool". Caplet's AI use is large (councils, 472 questions, models, decision memos, exemplar IPS
  v3-v12, 23 example notes, mock judges, the WInS click, these reviews, and from 16 Oct [AI] suggestions). The log has
  24 dated rows, none from 1 to 15 Oct, and its template disclosure says "Students ... made all decisions, and wrote all
  submitted text", which is not true if any [AI] wording is accepted. Sections 1-4 describe a DCF/skfolio platform the
  strategy never used.
- **Evidence.** AI Policy page (evidence pack [W5]); page 3768 2023-24 ("1-2 sentences on how you used that AI tool");
  `caplet-latest/docs/AI_USE.md:45-53` (template), :60-77 (log rows dated 24 Sep-30 Sep and 16 Oct only), :91; CLAUDE.md
  insight_v1 section ("472 questions"); 15 Oct brief item 24.
- **Fix.** Keep the AI record (item 7) from now; write the Works Cited entry from it, by tool and task, including exact
  accepted [AI] wording and the WInS browser use. What it must achieve: a reader of the Works Cited could predict what AI
  did and did not do, and every sentence is literally true.

### FR-12 (medium, new): Prepare for a team reflection and an advisor reflection, each about 150 words
- **Problem.** Last year's Knox FR had "Section 2: Describe in 150 words or less, your takeaways from this team's
  competition experience" and an advisor paragraph; 2022-23 and 2023-24 had 150-word advisor reflections. Last year's
  advisor paragraph in the team doc sat in the same student-edited doc as the rest; who wrote it is UNVERIFIED.
- **Evidence.** `2025_knox_wharton.md:84-86, 247`; page 3768 (2022-23, 2023-24 summary pages).
- **Fix.** The learning log (item 6) feeds the team reflection; the advisor gets the evidence log in November and writes
  their own paragraph if asked. What it must achieve: a ready, true reflection that does not depend on the last weekend.

### FR-13 (medium, known-deeper): Five purposeful charts, built by students from data collected now
- **Problem.** "Uses data effectively" replaced "visually pleasing ... many creative elements". The kit's charts are AI
  work and partly STRIPS-era; the WInS pie chart mislabels the bond funds.
- **Evidence.** deliverables.txt:59; evidence pack 2.3; COMPETITION.md:98; `deliverables/final_report_outline.md:7-15`
  (charts 01-05 of the abandoned plan).
- **Fix.** The five charts in section 8, each answering one client question, built from items 12-14. What it must
  achieve: a reader understands the plan from the charts alone.

### FR-14 (medium, known-deeper): The school letter must be signed before Thu 3 Dec, with names exactly as on the roster
- **Problem.** The letter is required with the FR, needs a school administrator's signature on letterhead and lists the
  advisor and every student by full name. It was "not yet requested as of 13 Oct". Term ends Thu 3 Dec; Fri 4 Dec is a
  staff day.
- **Evidence.** `2026_27_School_Documentation_Template.txt:1-28`; deliverables.txt:26, 52; COMPETITION.md:128-132;
  Knox term dates page.
- **Fix.** Ask through the advisor now; aim to hold it by Fri 20 Nov; check every name against the private roster note;
  store it off the repo. Note the later semifinal letterhead and consent forms (section 9).

### FR-15 (high, known-deeper): Students cannot yet defend the numbers and decisions live without AI
- **Problem.** Semifinal and finale questions test ownership. Today the strategy calls, the numbers and the IPS draft are
  AI-built, and five of six students have no recorded role. Past semifinals required each member to explain their
  contribution.
- **Evidence.** CLAUDE.md:75; 01_version_5.md:36; L01 JUDGE-11, JUDGE-17; L10 TP-01, TP-03; 2025-26 Semifinalists Next
  Steps (evidence pack [D1]); faqs.txt:89.
- **Fix.** The no-laptop test and the numbers table in section 7; each student owns five of the 30 questions and rebuilds
  at least one number in a spreadsheet. What it must achieve: any student can answer any of the 30 in their own words
  with the right number, date and basis.

### FR-16 (medium, new): Draw the line between "what we would do differently" and redesign before writing it
- **Problem.** The Guide allows "decisions you would make differently" but forbids redesign after the results. Some
  tempting lessons are strategy changes (for example "more stocks" or "a dedicated reserve"), which would read as
  redesign; others are implementation lessons (order timing, after-hours iBond spreads, AI in WInS, roles set late,
  logging decisions).
- **Evidence.** Guide:156-159; `final_report.md:19-20` (stale prices; after-hours spreads); COMPETITION.md:100, 192-193;
  2025-26 semifinal rule allowing reflection on "strategic weaknesses, limitations, or missed opportunities without
  changing the original strategy" (evidence pack [D1]).
- **Fix.** A two-column list (implementation lesson vs strategy question), agreed by the team before drafting. Strategy
  weaknesses are stated as limitations with their size, not as changes.

### FR-17 (medium, known-deeper): Anything the semifinal or finale will show must already be in the FR
- **Problem.** Past semifinals banned "completely new material" and required "a case study of one stock or ETF" in the
  portfolio. Caplet's natural case study is IBTM (or VT). Alternatives considered, the price of certainty and the
  co-sponsor logic also need to be in the FR to be usable later.
- **Evidence.** Evidence pack 2.4 and [D1]; L04 UNIQ-15.
- **Fix.** The FR contains a plain IBTM explanation (what it holds, its two jobs, why its payout is not fixed, its final
  months) and the alternatives table on WInS-listed instruments. What it must achieve: a semifinal deck can be built from
  the FR with nothing new.

### FR-18 (medium, new): The public repo and the fork collide with the semifinal/finale posting ban and the title-page username
- **Problem.** Wharton bans "posting presentations or participants online during the Semifinals or Global Finale". The
  repo is public and a team member's fork exists (created 15 Oct). Semifinal slides, recordings, screenshots or notes of
  judges' questions committed there would be posted online. The FR title page will also carry the WInS username (IPS:98-100),
  so an FR PDF or draft in the repo would publish it.
- **Evidence.** Rules page, quoted in evidence pack R4 section 5.1 ("Video recording, audio recording, photography,
  screenshots, or posting presentations or participants online during the Semifinals or Global Finale is strictly
  prohibited"); CLAUDE.md working rules ("Repo is public"); task context (fork created 15 Oct 2026 22:10 UTC).
- **Fix.** Keep FR drafts, the title page, the school letter and any semifinal or finale material on the private Drive
  only. What it must achieve: nothing judged or presented is published by the team before or during judging.

### FR-19 (low, new): Finale logistics from Sydney
- **Problem.** The Global Finale is 29-30 April 2027. Knox Term 2 2027 starts Tue 27 April, so an in-person trip falls in
  week 1 of term; Wharton does not fund travel; in-person teams need an accompanying adult. Virtual attendance is
  allowed; after Australian daylight saving ends (4 Apr 2027) Sydney is 14 hours ahead of Philadelphia, so a 9:00 am
  EDT session is 11:00 pm in Sydney (my conversion).
- **Evidence.** Main page "April 29 & 30" (evidence pack [W1]); faqs.txt:86-87; Rules page (evidence pack R4 5.1:
  "At least one adult ... must accompany the team"); Knox term dates page ("Tuesday 27 April Term 2 Commences", 2027).
- **Fix.** None needed now beyond noting it in the availability calendar (item 18). Decide in March only if selected.

---

## 11. Sources

Repo (read-only, 16 Oct 2026):
- `competition/official/2026_27/2026_WGY_Investment_Competition_Guide.txt:60-61, 70-78, 115-118, 146-159, 181-188`
- `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt:4, 43-45, 69-74, 88-124, 129-149, 161-169`
- `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt:51-52, 68-77, 82-125`
- `competition/official/2026_27/smapply_public_2026-10-14/deliverables.txt:26-27, 51-59`; `faqs.txt:59-66, 76-89`
- `competition/official/2026_27/2026_27_School_Documentation_Template.txt:1-28`
- `CLAUDE.md:9, 14, 40, 75`; `COMPETITION.md:87-100, 128-132, 172-193`
- `team/google_drive/final_report.md:14-27`; `strategy_notes.md:16-22`; `client_portrait.md:14-15`;
  `ips_report/01_version_5.md:16-36`; `2025_knox_wharton.md:76, 84-86, 174-235, 247, 3800-3890`;
  `sheets/portfolio_and_trading_notes/portfolio.csv`, `trade_log.csv`, `rb_tickets.csv`
- `rab/redteam/triage.md`; `rab/decisions/D_rivals.md`, `D_stress_bad_year.md`, `D_range_confidence_2031.md`,
  `D_certainty_definition.md`; `deliverables/final_report_outline.md`
- `caplet-latest/CLAUDE.md:26-30`; `caplet-latest/COMPETITION.md:141-143`; `caplet-latest/docs/AI_USE.md:45-91`;
  `caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md`, `ips_numbers.py:70-89, 122`;
  `caplet-latest/competition/official_market_data/daily-treasury-rates_2026-09.csv`, `daily-treasury-rates_2026-10.csv`

Scratchpad: `oct16/research/KB_what_wins.md` (evidence pack) and R1-R4; `oct16/research/KB_verify/wp_3768.json`
(Wharton page 3768, 2022-23 and 2023-24 FR specs); `oct16/research/KB_verify/num/reconcile.py`; my scripts
`oct16/lenses/L07/series.py` (+ `series_out.txt`) and `oct16/lenses/L07/simple.py`; other lenses L01-L10 (cited by id);
the 15 Oct brief `oct14/final.md`.

Web (accessed 16 Oct 2026): Knox term dates, https://www.knox.nsw.edu.au/about/public-information/term-dates (2026 Term 4
concludes Thu 3 Dec; Fri 4 Dec staff day; 2027 Term 1 commences Fri 29 Jan, concludes Fri 9 Apr; Term 2 commences Tue
27 Apr). Wharton pages as cited in the evidence pack (Rules & Roles, FAQ, AI Policy, main page, page 3768).

UNVERIFIED: this year's FR page range, boxes and whether charts are allowed; whether an advisor or team reflection is
required; whether cash may appear in the plan; whether WInS records stay accessible after the season; iBond distribution
amounts and dates in WInS; the 2027 semifinal format; who wrote last year's advisor paragraph.
