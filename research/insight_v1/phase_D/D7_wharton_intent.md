# D7 Wharton Intent Historian: M002 (how the three Trading Notes show a developing strategy) and M011 (what only our thesis can truthfully claim)

Agent D7, insight_v1 run, Phase D, written 2026-09-27. Lens: the client trend, Wharton's official framing, past case
designs compared with this one, and what semifinal readers reward. This is AI-generated research for Team Caplet:
evidence, numbers, specs and checklists. **None of it is text to submit.** The team decides and writes every word,
including every WInS note, and records AI use in the Final Report's Works Cited (R-W46). Nothing here is for the
finale.

Script: `research/insight_v1/scripts/D7_rule_trigger_odds.py` (run from the repo root:
`.venv/bin/python research/insight_v1/scripts/D7_rule_trigger_odds.py`). Seed 20260927, 200,000 paths.

Terms used: **band** = a range around a target weight; the team trades only when a weight leaves it. **bp (basis
point)** = 0.01 percentage point. **Hedge** = the Treasury funds whose value moves like the cost of Laura's ten
payments. **Funded ratio** = hedge value divided by the value of the payments on the same day.

---

## Summary of top findings (ranked by effect on reaching the semifinals and on making the plan Laura's)

1. **(M011, tier 2 IPS, strongest wording finding) The pitch must not claim "her ten payments are bought in January
   2027".** That is false in roughly 1 in 4 to 1 in 3 modelled rate paths: the ladder costs more than $300k if rates
   fall more than about 27bp before January (D7 script: ~23%; A2: 24.3%; S4: 30.7%; all ASSUMPTION-based). The claim
   only our plan can make truthfully *in every path* is a **rule**: *no dollar of Laura's money takes stock-market
   risk until all ten payments are bought* (with the 2028 deposit finishing the ladder first if rates fall). A rule is
   true by construction; a date is a forecast. The case's credibility test ("overpromising could damage her
   credibility", case p.3) applies to our own pitch first.
2. **(M002, tier 1 WInS-now/TN) No sensible rebalancing band will fire before Oct 23, so do not plan a "discipline
   trade".** With the ticket's weights, the chance that any band fires by Oct 20 is about 0% (55-65 growth band;
   whole-book equity +/-3 or +/-5 points) to 0.1-0.3% (a +/-2 to +/-3 point band). The hedge-duration band
   (9.65-10.15 years) drifts about 0.08 years at most in three weeks. Blueprint 01 section 7 ("Oct 1-16: at least one
   discipline/rebalance decision") should be dropped: planning it invites a staged trade, which R-W28 forbids and
   R-W88 discourages. Under lock-early the characteristic discipline is *not* trading, and a non-trade cannot be a
   Trading Note.
3. **(M002, tier 1) "Tested" does not need a new trade: it can live in the reflection of the hedge purchase.** The
   reflection (written ~Oct 20) may say how the decision was tested by a real market move. A 10-year yield move of
   10bp or more between an Oct 1 fill and Oct 20 has a ~53% chance at the end date and ~83% at some close (realised
   2026 volatility 4.45bp/day, VERIFIED-PRIMARY data, driftless ASSUMPTION). 10bp moves the payments' value about 1%.
   The test: did the hedge's % change track the payments' % change? This needs **data captured from the fill date**
   (WInS hedge values + treasury.gov curve on the same dates). The official wording is "supported, tested, *or*
   refined" in all four official texts: there is **no quota** of one note per type.
4. **(M002, tier 1) The only honest source of a "refined" note is a pre-announced planned adjustment or a real
   discovery.** Candidates, in order: (a) the Session Rules position limit forcing TLH to be split with SPTL (a real
   rule discovered at the first trade); (b) the growth split, which is genuinely undecided (60/40 provisional;
   CLAUDE.md calls the equity weight the weakest call) *if* the first growth note says so and names the date the team
   will decide; the Guide allows "planned adjustments" (p.5) and older Wharton guidance says of the strategy "Can you
   tweak it? Absolutely!" (VERIFIED-PRIMARY). If neither happens, three "supported" notes with honest "tested"
   reflections are fine.
5. **(M011, tier 2) Creativity this season is scored on the thesis's fit to a new kind of case, not on instruments.**
   Past cases (2021-22 to 2025-26) were growth or return targets with hobby hooks; this case is the first with a fixed
   liability larger than the deposits (111%), the first to use "certainty" and "co-sponsor", and it has no hobbies at
   all (B2a/B1b, VERIFIED-PRIMARY past case pages; my re-check of the 2021-22 wording below). Three Laura-specific,
   checkable decisions carry the thesis: promise-before-growth (her 2028 money comes from career income she herself
   called "unstable", FR only); a 2031 floor that is bought, plus a stretch with a stated probability (the case's
   co-sponsor task); certainty defined as "bought at market prices, not forecast" (a statistics-trained client can
   check it). The premise that "AI tools will all say lock early" is **untested** and the decision does not depend
   on it.
6. **(M002, tier 1) Dated events in the window move rates but create no trade under our rules**: September jobs report
   Fri Oct 2 and September CPI Wed Oct 14 (both SNIPPET-UNVERIFIED; bls.gov refused access); the next FOMC meeting is
   **Oct 27-28, after the Oct 23 deadline** (VERIFIED-PRIMARY, federalreserve.gov). These are the moments to snapshot
   the hedge and the curve, not to trade.

---

## M002 (tier 1: WInS-now and Trading Notes, Oct 23; also one IPS clause)

**Question (canonical).** Should the three Trading Notes be one "supported", one "tested" and one "refined" decision,
and which pre-written rule (a WInS rebalancing band or rate trigger) and which dated market events between Sept 28 and
Oct 20 can make a genuine rule-triggered trade happen before the Oct 23 deadline?

**One-sentence answer.** No quota applies and no sensible band will fire before Oct 23, so the team should choose three
real trades (promise, growth, and either a real refinement or a third funding purpose), show "tested" inside the hedge
note's reflection using a real rate move measured from data saved at the fill date, and never create a trade to fill a
category.

**Part-mis-posed.** The question assumes a rule-triggered *trade* is the way to show "tested". Under lock-early the rules
say "do not trade" after rate moves (ticket "never" rules 1-2), so the realistic rule-triggered event is a check with no
trade. The better route to "tested" is the reflection, which the guide allows to be written after the fact (only the
WInS note itself is frozen).

### Evidence
| Claim | Source | Status |
|---|---|---|
| The TN guide uses both "aligned with, tested, or refined" (instructions, L12) and "supported, tested, or refined" (L29-30); the Guide p.3 and the Infographic say "supported, tested, or refined"; the case says "reflected, tested, or refined" (L152). "Or" in every version: no one-of-each requirement | `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` L12, L29-30; `2026_WGY_Investment_Competition_Guide.txt` L89; `2026_WGY_Competition_Infographic.txt` L24-25; `Laura_Gao_2026_Client_Profile.txt` L152 | VERIFIED-REPO-FILE |
| "A decision can still demonstrate thoughtful analysis and strategic thinking even if your team later sells the investment or changes its approach." | TN guide p.1 (R-T18) | VERIFIED-REPO-FILE |
| "A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten simply because markets move" | Guide p.5 L156 | VERIFIED-REPO-FILE |
| "The competition does not require frequent or same-day trading." / "you should not be doing a lot of buying and selling of the stocks designated for the long-term portion of your portfolio" | SMApply Trading Details and FAQ (R-W73, R-W88), read by Phase A 2026-09-27 | VERIFIED-PRIMARY (via case_register) |
| Teams must not "fabricate analyses, invent teamwork and experiential stories" | Rules page (R-W28) | VERIFIED-PRIMARY (via case_register) |
| Trade notes cannot be edited; the three notes are quoted "exactly as it appears in WInS" | TN guide p.2 L44; Stock-Trak blog via `phase_A/wins_week1_guardrails.md` item 6 | VERIFIED-REPO-FILE / VERIFIED-PRIMARY (vendor, not season-specific) |
| Older Wharton guidance on strategy: "Defining your strategy early is essential to doing well. Can you tweak it? Absolutely!" and "if you provide us with a team strategy that is buried somewhere in your experience, rather than clearly stated, defined and articulated up front, you will not be among the strongest teams." | https://globalyouth.wharton.upenn.edu/developing-strategy/ (undated, older season; accessed 2026-09-27, `fetch_text.py --grep` YES) | VERIFIED-PRIMARY (older-season page) |
| 2026 FOMC meetings: "September 15-16*", "October 27-28", "December 8-9*" | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm (accessed 2026-09-27) | VERIFIED-PRIMARY |
| Employment Situation for September 2026: Oct 2, 8:30 a.m. ET; CPI for September 2026: Oct 14, 8:30 a.m. ET | WebSearch snippet of bls.gov schedule pages (bls.gov returned HTTP 403 to the fetch helper) | SNIPPET-UNVERIFIED |
| Ticket plan: VT 60% / VGSH 40% of the growth money, band 55-65; hedge duration band 9.65-10.15y; duration refresh Oct 19-23; "Do not create a decision just to get a note" | `research/insight_v1/wins_now/securities_and_allocation_v0.md` sections 4-5 | VERIFIED-REPO-FILE (a plan, not a fact) |
| Blueprint timeline: "Oct 1-16: at least one discipline/rebalance decision" | `research/blueprints/01_trading_notes_blueprint.md` section 7 | VERIFIED-REPO-FILE (superseded by this finding) |

### Numbers (D7 script; all probabilities are ASSUMPTION-based model outputs, not forecasts)
| Rule | Move needed | P(fires by Oct 20), weekly / daily checks |
|---|---|---|
| VT share of growth money, 55-65 (ticket) | VT vs VGSH -18.5% / +23.8% | 0.00% / 0.00% |
| VT share of growth money, 57-63 | -11.6% / +13.5% | 0.12% / 0.15% |
| VT share of whole book 20.5%, +/-5 points | -28.9% / +32.7% | 0.00% / 0.00% |
| VT share of whole book, +/-3 points | -17.7% / +19.1% | 0.00% / 0.00% |
| VT share of whole book, +/-2 points | -12.0% / +12.6% | 0.29% / 0.33% |
| Hedge duration band 9.65-10.15y | drift > 0.25y | worst case ~0.08y in 3 weeks (weight drift +/-0.03y for +/-50bp; issuer-duration drift ~-0.05y at the Jun-Sep pace) -> essentially 0 |

Inputs: realised 10-year daily change sd **4.45bp/day** (185 trading days of 2026, live treasury.gov CSV,
VERIFIED-PRIMARY); equity vol 16.78% (JPM AC World, used as ASSUMPTION for short-run vol); correlation 0 (ASSUMPTION;
JPM -0.01). Window: 19 U.S. trading days Sep 28-Oct 22; 13 days of market moves after an Oct 1 fill to Oct 20.

Rate moves available to a "tested" reflection (Oct 1 fill to Oct 20): |move| >= 5bp: 76% at end date; >= 10bp: 53%
(83% touched at some close); >= 15bp: 35% (55%); >= 25bp: 12% (18%). Median |move| 10.8bp. A 10bp move changes the
payments' value about 1.0% (~$2,890 on the 2027 value; DV01 $289/bp, VERIFIED via the verified script). Because the
WInS hedge is scaled ($198k of $300k in option (ii)), compare **percentage** changes, never dollars.

### Implication (decisions and specs; the team writes every word)
- **Decision (WInS-now + TN):** drop the planned "discipline/rebalance trade" from blueprint 01 section 7. Plan the
  three notes from trades that will happen anyway: (1) the hedge purchase, (2) the growth purchase, (3) either a real
  refinement (below) or the third funding purpose (VGSH, or SPTL if the position limit forces a split).
- **Decision (WInS-now, before the growth order):** if the team really has not settled the equity share of the growth
  money, the growth note should say the split is provisional and name the week the team will decide (e.g. "decide by
  Fri Oct 16 after our own research"). If the decision then changes the split, that one VT-against-VGSH trade is a
  genuine, pre-announced "refined" note (Guide p.5 "planned adjustments"). If the decision confirms 60/40, there is no
  trade and the log records "decided not to trade". **Never** buy at a split the team already considers wrong in order
  to "refine" it later: that is staging (R-W28).
- **Decision (WInS-now, data capture, owner needed):** on the fill date and on Oct 2, Oct 9, Oct 14, Oct 16 and Oct 20,
  save a screenshot of WInS position values (IEF, TLH/SPTL, VT, VGSH) and download that day's treasury.gov par curve.
  Then value the ten payments on each date with `research/verified_2026-09-27/official_curve_pv.py` (spot value).
  This feeds the "tested" reflection now and the Final Report's funded-ratio chart later (B7a Q12).
- **"Tested" reflection spec (hedge note, <=100 words, team's words):** must contain the rate move over the period
  (bp, from treasury.gov); the hedge's % change; the payments' % change on the same dates; what the rule told the team
  to do (hold); one sentence on what it means for Laura (the promise stayed funded while prices moved). If the move is
  under ~5bp, say the test was small rather than overstate it.
- **"Tested" reflection spec (growth note):** the growth money's % change and the fact that the payments were
  unaffected ("a fall shrinks the facility range, never the payments", ticket checklist 2).
- **IPS clause (tier 2):** one rebalancing sentence in the IPS (CFA IPS guidance says even a no-rebalance policy should
  be documented, per B4b, VERIFIED-PRIMARY by that agent). Content: bands exist for the growth money only; the hedge is
  never traded because rates moved.
- **Events calendar (check, never trade):** Oct 2 jobs report; Oct 14 CPI; Oct 12 Columbus Day (U.S. bond market
  closed while stocks trade, ASSUMPTION that WInS ETF prices still update); Oct 23 TN due; FOMC Oct 27-28 after the
  deadline (its effect can only appear in the IPS/FR, not in the notes).

- Deliverables: WInS-now, TN (and one IPS clause). Deadline tier: 1. Confidence: high on the band odds and on the
  "no quota" reading; medium on the value of a "tested" reflection (no public evidence of how readers score it).
- Changes current strategy? **No** to the strategy; **yes** to the TN plan (drop the planned rebalance; add a
  provisional-split sentence with a decision date to the growth note checklist; add a data-capture step to ticket
  step 1).
- Criterion served most: **Articulation of Competition Experience** ("clearly explains the team's research and
  decision-making process", R-S27), with Investment Strategy's "disciplined planning" (R-S24).
- What this teaches: a rule that almost never fires in three weeks is working as designed; you show discipline by
  measuring what the market did to your plan, not by inventing a trade.

---

## M011 (tier 2: IPS pitch Nov 6; tier 3: Final Report)

**Question (canonical).** Since lock-early is now the textbook answer that AI tools and hundreds of teams will give,
which 2-3 Laura-specific, checkable decisions make our "clear and creative thesis" different, and what one claim can
only our strategy truthfully make in the 50-word pitch?

**One-sentence answer.** Lead the pitch with a rule, not a date: "no dollar takes stock-market risk until all ten
payments are bought" is true in every rate path and is something growth-first and "balanced bucket" plans cannot
say, and it is carried by three Laura-specific decisions (promise before growth, a bought 2031 floor with a stated
stretch, certainty defined as bought rather than forecast).

**Partly mis-posed.** The premise ("AI tools and hundreds of teams will give lock-early") is **untested**. No public
discussion of the Laura Gao case was found (two WebSearch queries, 2026-09-27, returned only official pages and
third-party competition listings). The recommended claim does not depend on the premise: it is chosen because it is
true, checkable and tied to Laura, so it holds whether rivals converge or not.

### Evidence: what Wharton's framing and past cases say is "creative" this year
| Claim | Source | Status |
|---|---|---|
| Criterion: "Presents a clear and creative investment thesis" | SMApply deliverables page (R-S24), `SMApply_Deliverables_Page_2026-09-27.md` | VERIFIED-REPO-FILE |
| Pitch: "Clearly communicate the central idea behind your approach and how it is designed to support your client's financial goals and future funding needs." (50 words max) | IPS guide p.1 L35-36 (R-I17) | VERIFIED-REPO-FILE |
| "There is no single correct strategy. Strong teams explain the reasoning, assumptions, and tradeoffs behind their decisions." | Infographic | VERIFIED-REPO-FILE |
| Case: overpromising could "damage her credibility and lose the confidence or participation of co-sponsors" | Case p.3 (R-AN30) | VERIFIED-REPO-FILE |
| Case: 2028 deposit comes from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures"; she wants "an appropriate balance between pursuing growth and protecting the capital required for her goals"; degree in "Statistics & Information Decisions Management" | Case L44-45, L70-74, L16 | VERIFIED-REPO-FILE |
| Laura on leaving her job: "let me give up my incredibly cushy, paying job with health insurance to be self-employed, with unstable income." (Overachiever Magazine, 2021-03-15) | `phase_D/D13a_laura_quotes_verified.md` row B8b-Q18 | VERIFIED-PRIMARY per D13a. **Final Report only**; never in the TN or IPS (D13 rule) |
| 2021-22 case (Nichole Jordan): a $5,000 scholarship "for at least 10 years. Should she keep $50,000 in cash? Should she invest in stocks that pay dividends? Another option?" | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/ (accessed 2026-09-27, `--grep` YES) | VERIFIED-PRIMARY |
| Case trend 2021-2026: payment stream was 50% of assets in 2021-22, 111% of deposits now; "certainty" 0 hits in past cases, 6 now; "co-sponsor" 0 before, 9 now; no hobby hooks this year; 2025-26 had a $1.5m growth target and a values rule | `phase_B/B2a_why_laura_intent.md` summary 1-4; `phase_B/B1b_case_anomalies.md` section 1 | VERIFIED-PRIMARY per those agents (past-case pages; 2025-26 text from a secondary copy, SNIPPET-UNVERIFIED) |
| "Your strategy should be unique to your team." | https://globalyouth.wharton.upenn.edu/developing-strategy/ (older season) | VERIFIED-PRIMARY |
| "Oftentimes, the best solutions are made up of simple, elegant ideas." (Melissa Ko Hahn, judge of the 2025 semifinal presentation videos) | https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/ (accessed 2026-09-27, `--grep` YES) | VERIFIED-PRIMARY (context: semifinal videos, not the written round) |
| "less is more, and having an explainable strategy makes a lot more sense than going for so many different things at once." (DMV's Finest, 2022-23 champions, on their final report) | https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/ (`--grep` YES) | VERIFIED-PRIMARY |
| Distinctive elements already listed (model-free certainty; 2031 range as a rule; "buys range, not median") | `research/council_2026-09-27/01_chair_memo.md` section 7; `phase_A/stakeholder_map.md` BS-10, SH-18 | VERIFIED-REPO-FILE (AI council brainstorming) |

INTERPRETATION (D7): the designers moved the scoring weight from picking investments to reliability, flexibility and
credibility. So a thesis is "creative" this year if it answers *when and how certainty is created, and how it is
communicated to people who must believe her*, in a way a reader has not seen from other teams. Instruments are
expected to be plain (Wharton's own example note buys an intermediate Treasury ETF, R-AN44).

### Numbers: which candidate pitch claims are true in every path?
| Candidate claim | True when | Source |
|---|---|---|
| "Her ten payments are bought in January 2027 with her first deposit" | Only if the ladder costs <= $300k on the purchase date: false in ~23% (D7 one-factor), 24.3% (A2), 30.7% (S4) of modelled paths; the ladder cost more than $300k on 173 of 185 trading days of 2026 | D7 script [6]; brief section 14; ticket section 8 (ASSUMPTION-based) |
| "The payments are fully funded before any money is invested for growth" / "no dollar takes stock-market risk until all ten payments are bought" | Every path, because it is a rule (if rates fall first, the 2028 deposit completes the ladder before any growth buy). In the joint tail (rates fall **and** the 2028 deposit is missing) the rule still holds but some payments stay unfunded: the pitch must not add "guaranteed" | Brief section 7; ticket section 8; joint tail open (brief section 9) |
| "Her 2031 promise to co-sponsors is a floor already bought, plus an upside with a stated probability" | Every path by rule (the floor is whatever the bought note will pay); the stretch is a model number | Brief section 8 item 7; strategy_mc.py floor p5/p50/p95 $127k/$165k/$217k |
| "95% certain" | Model-dependent; a statistics-trained reader can challenge it (brief section 8 item 6) | Avoid |

### The 2-3 Laura-specific, checkable decisions (content spec; the team chooses and words them)
1. **Promise before growth (lead idea).** Laura hook: her second deposit depends on career income (case L44-45; her
   own "unstable income", FR only). Checkable: WInS order sequence (hedge first, ticket step 1) and the 2027/2028 rule
   in the IPS. Truth test: passes in every path.
2. **A bought 2031 floor, plus a stretch with a stated probability.** Laura hook: the case's co-sponsor task and its
   credibility warning; criterion 5 scores exactly this communication (R-S28). Checkable in the FR. IPS gets only the
   principle (the guide says the final range is not expected in the IPS).
3. **Certainty = bought at market prices, not forecast** (nominal US$, barring U.S. default). Laura hook: a
   statistics-trained client can check a price, not a model. Checkable by anyone with a Treasury price.
   Optional fourth for the FR only: report progress as a funded ratio (uses the M002 data capture).

### Implication
- **Pitch content spec (IPS, tier 2; words are the team's; 50-word hard cap):** must contain (a) the central idea as a
  rule (promise bought before any growth risk); (b) what it does for Laura (payments certain in US$; the growth money
  serves the facility contribution and flexibility); (c) optionally the 2031 idea (floor bought, upside stated
  honestly). Must **not** contain: a date-certain claim ("bought in January 2027"), "guaranteed"/"100%"/"95%", jargon
  (LDI, duration, DV01), any Laura quote, identity imagery or book-title puns (D13 rules), more than one number.
- **IPS first paragraph:** repeats the same central idea and states the if-rates-fall rule, because the Guide forbids
  redesign after results (p.5) and the chance of needing it is ~1 in 4 to 1 in 3.
- **FR (tier 3):** main chart for the lead idea = the funded ratio over the WInS period (data from M002) or the 2027-2033
  "promise bought first, growth second" timeline; the one Laura quote allowed, if any, from D13a with outlet and year.
- **Optional AI comparison test (only if the team wants it; low priority):** after the team has drafted its own pitch
  (R-W51: "Did I come to my current conclusion before or after using generative AI tools?"), paste the public-facing
  parts of the case into 2-3 AI tools with one neutral prompt, record the architecture each suggests, and log tool,
  date and purpose in Works Cited (R-W46). It measures the premise; it does not change the recommended claim.

- Deliverables: IPS (pitch + first paragraph), FR; TN only as consistency (same words for the three jobs). Deadline
  tier: 2 (IPS Nov 6), FR parts tier 3. Confidence: high that the date-certain claim is unsafe and the rule claim is
  true; medium that it is *distinctive* (the field is unobserved).
- Changes current strategy? **No** to the strategy; **yes** to its wording: replace "bought in January 2027" with the
  rule wherever it is used as a headline (brief section 7 and chair memo sentences are internal; the pitch and IPS
  must use the rule).
- Criterion served most: **Investment Strategy** ("a clear and creative investment thesis", R-S24), with Client
  Knowledge ("recommendations that can earn her confidence", R-S25).
- What this teaches: the most distinctive claim is often the most honest one; a rule you control can be promised, a
  market price you do not control cannot.

---

## Sources (accessed 2026-09-27 unless stated)
Primary web (VERIFIED-PRIMARY, read with `research/insight_v1/scripts/fetch_text.py`, quotes checked with `--grep`):
- Federal Reserve FOMC calendar: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- Treasury daily par yield curve 2026 CSV (via the D7 script): https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
- 2021-22 case (Nichole Jordan): https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/
- Developing a Strategy (older season): https://globalyouth.wharton.upenn.edu/developing-strategy/
- 2025 top-10 article (Hahn): https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/
- Tales from the 2023 teams (DMV's Finest): https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/

Snippets and blocked (SNIPPET-UNVERIFIED / not used as fact):
- bls.gov schedule pages (HTTP 403 to the helper): https://www.bls.gov/schedule/2026/10_sched_list.htm ,
  https://www.bls.gov/schedule/news_release/empsit.htm (dates from the WebSearch summary only).
- WebSearch for public discussion of the Laura Gao case (two queries): only official pages and third-party listings
  (e.g. https://www.aralia.com/helpful-information/guide-to-the-wharton-global-high-school-investment-competition/ ,
  https://competemap.com/competitions/cmrw8ls8y0001vnne2cnjon1n); nothing on case strategy.

Repo files (VERIFIED-REPO-FILE): `competition/official/2026_27/{Laura_Gao_2026_Client_Profile,2026_WGY_Trading_Notes_Analysis-FINAL,2026_WGY_Investment_Policy-FINAL,2026_WGY_Investment_Competition_Guide,2026_WGY_Competition_Infographic}.txt`,
`SMApply_Deliverables_Page_2026-09-27.md`; `research/insight_v1/_context/brief.md`;
`research/insight_v1/phase_A/{case_register,stakeholder_map,wins_week1_guardrails}.md`;
`research/insight_v1/phase_B/{B7a_competition_meta,B2a_why_laura_intent,B1b_case_anomalies}.md`;
`research/insight_v1/phase_C/survivors.json` (M002, M011); `research/insight_v1/phase_D/D13a_laura_quotes_verified.md`;
`research/insight_v1/wins_now/securities_and_allocation_v0.md`; `research/blueprints/01_trading_notes_blueprint.md`;
`research/council_2026-09-27/01_chair_memo.md`; script `research/insight_v1/scripts/D7_rule_trigger_odds.py`.

---

## What this teaches
1. **Read the small words in the rules.** "Supported, tested, *or* refined" is a menu, not a checklist. Reading it as a
   quota would have pushed the team toward a staged trade, which the rules forbid.
2. **Measure before you plan.** A five-minute simulation shows a +/-5 point band has essentially no chance of firing in
   three weeks. Plans that depend on the market "doing something" by a deadline are wishes.
3. **Evidence has to be collected on the day.** A test of the hedge needs the hedge's value and the Treasury curve on
   the same dates; you cannot rebuild WInS values later.
4. **Say what you control.** "Bought in January 2027" depends on interest rates; "no stock risk until the payments are
   bought" depends only on the team. Laura's case warns that overpromising costs credibility; the pitch is the first
   place that warning applies.
