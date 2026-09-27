# B7a Competition Meta & Judges: questions from the evidence on past semifinalists, winners and readers

Agent B7a (Phase B, lens "Competition Meta & Judges"), insight_v1 run, written 2026-09-27 (about 12:00-12:40 UTC).
Starting angle: what past semifinalists and winners did in their WRITTEN work, and what the semifinal readers of
written deliverables have said they reward. Semifinals only: nothing here is for the finale pitch or Q&A. Finale
articles are used only where a judge comments on the quality of analysis or writing, and they are labelled as such.

This file is AI-generated research for Team Caplet. It contains questions, evidence and checklists. It contains no
text meant for submission. The team decides and writes every deliverable in its own words, and must record AI use in
the Final Report's Works Cited (R-W46).

---

## 0. Summary (read this first)

1. **NEW OFFICIAL DOCUMENTS the repo and Phase A do not have.** The public SMApply page "Investment Competition Guide"
   (https://wghsinvcomp.smapply.us/res/p/guide/, read 2026-09-27, VERIFIED-PRIMARY) links two 2026-27 PDFs:
   - "2026-2027 Investment Competition Guide", 5 pages,
     https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf (downloaded with curl, text read with
     pypdf, key quotes checked verbatim with `fetch_text.py --grep`; full SHA-256 in section 3.1).
   - "2026_WGY_Competition Inforgraphic-FINAL.pdf", 1 page, Box shared link
     https://upenn.box.com/s/l2p0l26svbbptmcizhmswyq5f7rbyp44 (downloaded via the Box shared-file download).

   They add scoring signals that are in no other official file. Examples (all VERIFIED-PRIMARY, exact words):
   - "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and
     tradeoffs behind those decisions." (Guide p.5)
   - "The competition recognizes thoughtful strategy, research and analysis, client understanding, disciplined
     decisions, management of risk and uncertainty, communication, and creativity." (Guide p.5)
   - A WInS trade note "should capture the reasoning behind the decision, including its alignment with your strategy,
     the supporting research or analysis, and its expected role in growth, liquidity, risk management, or future
     funding." (Guide p.3)
   - "Do not treat Trading Notes as an afterthought." (Guide p.3)
   - "A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten
     simply because markets move or hindsight reveals a different outcome. You may identify decisions you would make
     differently, but you may not redesign your strategy after observing the results." (Guide p.5)
   - "Strong submissions connect the client’s goals, research, portfolio decisions, and final recommendations through
     one clear and cohesive investment strategy." and "CORE PRINCIPLE Strategy guides every decision." (Infographic)
   These should join the official set (main loop's decision; I wrote nothing outside my file). Several questions
   below hang on them (anchor "R-new").
2. **Who reads the written work.** The 2025-26 Top 50 were picked "with the help of our Wharton School student
   evaluators, as well as a professional review panel of asset managers from Aberdeen Investments in Philadelphia"
   (Wharton news, 27 Jan 2026, VERIFIED-PRIMARY). abrdn (now Aberdeen) has supplied semifinal-round evaluators "from
   across the investment spectrum" since 2012 (abrdn press release, 30 Jan 2023, VERIFIED-PRIMARY). In 2018, 14
   Aberdeen professionals from "equity, fixed-income and alternative investing, as well as marketing and distribution"
   read 160 reports (about 11 each) (Wharton news, 4 Apr 2018, VERIFIED-PRIMARY). With about 2,300 reports now, a
   student first screen is likely (INTERPRETATION). So there are two reader types with different eyes: Wharton
   students applying the rubric, then asset managers, some of them fixed-income specialists.
3. **The deliverable format looks new this season.** Wharton said in 2024 and 2025 it was "doing some reimagining of
   our signature competition" (VERIFIED-PRIMARY). The 2025-26 season had a "mid-term report" (Wharton news, 27 Jan
   2026: "Teams that competed at least through the mid-term report submissions will receive a participation badge",
   VERIFIED-PRIMARY). A third-party tracker lists 2025-26 stages as "required trade; roster; midterm report; final
   report" (CompeteMap, SNIPPET-UNVERIFIED). INTERPRETATION: the 3-note Trading Notes Analysis + 500-word IPS + freeze
   structure is probably new in 2026-27, so past winners' written reports are weak templates, and the 2026-27 rubric
   and Guide are the best evidence of what is rewarded.
4. **What readers have said, verified verbatim.** Semifinal judge Melissa Ko Hahn, who read "written reports and the
   videos" in 2025: "one of the tendencies of people who are just starting out is to fall into this trap of hiding
   behind fancy terms and formulas... Oftentimes, the best solutions are made up of simple, elegant ideas." The 2023
   champions (DMV's Finest), about drafting the final report: "we really needed to cut things down... less is more,
   and having an explainable strategy makes a lot more sense than going for so many different things at once." The
   competition's academic director, Prof. Michael Roberts (2022 interview): "the jargon and acronyms are just
   obfuscating the elegant simplicity of finance". Older Wharton guidance: a strategy "buried somewhere in your
   experience, rather than clearly stated, defined and articulated up front" will "not be among the strongest teams".
5. **The only full past final report I could read is a useful anti-model.** A 2023-24 report published on Teen Ink
   (team not in that year's Top 50) is a sector-by-sector stock tour. It maps the client's hobbies to tickers and
   cites short-term gains as proof ("The team’s decision was proven with great success", "our portfolio grew 4.2%,
   affirming our updated strategy"). This year's rubric scores against both habits (R-T11, R-W75).
6. **The odds and the field.** Top 50 share of final reports fell from 3.9% (2022-23) to 2.1% (2025-26: 49 listed of
   about 2,339). One slot per year goes automatically to a team from the previous winner's school (Stuyvesant this
   season, INTERPRETATION from the stated rule). Most semifinal schools are new each year: 7 of 49 schools in the 2026
   list were also in the 2025 list; 11 of 50 in 2025 were in 2024 (DERIVED from the official lists). Only one
   Australian team appears in the five Top-50 lists 2022-2026 (Gryphon Group, Brisbane State High School, 2022).
7. **26 questions follow** (section 2), ranked by deadline tier within each group. The five I rate highest for
   "99% of teams will miss": Q2 (trade-note contents from the Guide), Q12 (grade implementation by tracking the
   liability, not by P&L; start collecting data now), Q15 (the hindsight rule means every "if rates move" rule must be
   in the IPS), Q4 (fixed-income readers will check the hedge), Q20 (whether readers see the WInS holdings).

---

## 1. Method

- Read the brief, v4 Parts 1-3, 5, 6, CLAUDE.md, Phase A (case_register R-ids, fact_register F-ids, stakeholder_map,
  wins_week1_guardrails), the council's winners.md and judge panel, and the Trading Notes blueprint.
- Web: WebSearch to find URLs; every page quoted here was opened with
  `.venv/bin/python research/insight_v1/scripts/fetch_text.py URL` and key quotes were checked with `--grep`
  (all returned "PHRASE FOUND VERBATIM: YES"). Box PDFs were downloaded with curl and read with pypdf.
- Blocked or unreadable: Scribd (all three documents return a JavaScript wall), Medium (HTTP 403), The Croton
  Chronicle (paywall stub). Their content is not used beyond search snippets, which are labelled.
- Derived numbers (selection rates, repeat-school overlap) come from counting the official lists; method in section 3.
- Privacy: no student surnames recorded; winners are named by team and school only, as Wharton publishes them.

---

## 2. The questions

Format per question: text; anchors; anchor quote; hypothesis (a GUESS, with evidence); what would change; deliverables;
domain; seed; north star. Anchors "R-new" point to the 2026-27 Guide or Infographic (section 0 item 1).

### Group A: what the semifinal readers are told to look for (tier 1-2)

**Q1. Should the 2026-27 Investment Competition Guide and Infographic be added to the official set, and which of their
sentences change our checklists?**
- Anchors: R-new (Guide, Infographic); R-S24 to R-S28; R-W43.
- Anchor quote: "Judges want to understand not only what your team decided to do, but also the reasoning,
  assumptions, and tradeoffs behind those decisions." (Guide p.5)
- Hypothesis (guess): yes. The Guide is an official 2026-27 document linked from the public SMApply page and uses the
  same vocabulary as the IPS and Trading Notes guides. It adds four things the other files lack: a note-content list
  (Q2), a hindsight rule (Q15), a seven-item "recognizes" list that names "disciplined decisions" and "management of
  risk and uncertainty" separately from the five criteria, and the word "tradeoffs" as something judges want shown.
- Would change: decision (the main loop adds the two PDFs, with hashes, to `competition/official/2026_27/` and the
  case register) and sentences (each deliverable checklist gains "state the tradeoff" and "state the assumption").
- Deliverables: WInS-now, TN, IPS, FR. Domain: D10. Seed: null.
- North star: Laura chooses the firm that shows her the tradeoffs it made for her; the Guide says judges score exactly
  that.

**Q2. Does every WInS trade note from now on contain the four elements the Guide lists (strategy link, supporting
research or analysis, and a named role in growth, liquidity, risk management or future funding), and does our Trading
Notes blueprint match?**
- Anchors: R-new (Guide p.3); R-T28; R-AN43; R-W82.
- Anchor quote: "the Trading Note should capture the reasoning behind the decision, including its alignment with
  your strategy, the supporting research or analysis, and its expected role in growth, liquidity, risk management, or
  future funding."
- Hypothesis (guess): the council blueprint (`research/blueprints/01_trading_notes_blueprint.md` section 3) covers
  purpose and the link to Laura but not "the supporting research or analysis" as an explicit element. Notes cannot be
  edited (A4 guardrails), and the three chosen notes are quoted verbatim, so a note that lacks the evidence element
  cannot be repaired later. Most teams will copy Wharton's 59-word example, which names a role and a risk but no
  research. A note that names one checked fact (e.g., the fund's duration from the issuer page, or the Treasury curve
  date) would stand out.
- Would change: sentence-level spec for every WInS note written from today (four-element checklist), and the TN
  blueprint section 3.
- Deliverables: WInS-now, TN. Domain: D10. Seed: 13.
- North star: a note that shows its evidence proves to Laura that our firm decides on research, not on mood.

**Q3. Who reads our submission first (Wharton student evaluators or Aberdeen professionals), how long do they spend on
it, and what do they see first?**
- Anchors: R-W24; R-W8; F-609; R-AN60.
- Anchor quote: "with the help of our Wharton School student evaluators, as well as a professional review panel of
  asset managers from Aberdeen Investments in Philadelphia" (Wharton news, 27 Jan 2026, VERIFIED-PRIMARY).
- Hypothesis (guess): a two-stage screen. Student evaluators apply the rubric to all ~2,300 submissions; Aberdeen
  professionals read a shortlist. Evidence: 14 Aberdeen readers handled 160 reports in 2018 (about 11 each, VERIFIED-
  PRIMARY); 2,300 reports at that load would need ~200 professionals (DERIVED, ASSUMPTION that the load per reader is
  similar). If so, the first reader may spend minutes, not an hour, and may read the 2-page IPS and the first page of
  the Final Report most closely.
- Would change: decision on Final Report structure (strategy, certainty definition and headline numbers on page 1; a
  student evaluator must be able to tick each criterion without hunting) and how much effort goes into the IPS pitch.
- Deliverables: IPS, FR. Domain: D7. Seed: 31.
- North star: if the first reader cannot see in two minutes why Laura would choose us, the second reader never will.

**Q4. What would an Aberdeen fixed-income professional check first in our Treasury-matching story, and which of our
current claims would they mark wrong or loose?**
- Anchors: F-203 to F-206; brief section 8 items 11-13; R-T23, R-T24.
- Anchor quote: Aberdeen readers came "from different areas of the company, including equity, fixed-income and
  alternative investing, as well as marketing and distribution" (Wharton news, 4 Apr 2018, VERIFIED-PRIMARY). Recent
  Aberdeen judges were "U.S. Credit Investment Manager" (2026) and "senior investment manager, North American fixed
  income" (2024) (VERIFIED-PRIMARY, finale articles).
- Hypothesis (guess): they will look for three things: (a) the difference between a bond fund (constant duration, never
  matures) and a ladder held to maturity; our WInS book of IEF/TLH-type funds matches duration today but drifts, and
  saying "locked" about a fund would be marked loose; (b) reinvestment of coupons; (c) the precision of "certain":
  nominal USD, barring U.S. default, if held to maturity. Individual Treasuries are allowed in WInS (R-W69), so a
  professional may ask why a liability-matching team did not buy any.
- Would change: sentences in the IPS and FR ("duration-matched in WInS; cash-flow-matched in Laura's real plan"), and
  possibly a WInS decision to hold at least one individual Treasury (see Q24).
- Deliverables: WInS-now, IPS, FR. Domain: D1. Seed: 29.
- North star: the professional reader is a stand-in for the adviser Laura would ask to check our work; passing that
  check is what makes the plan trustworthy.

**Q5. Is the 2026-27 deliverable structure (three-note Trading Notes Analysis, 500-word IPS, strategy freeze at the
IPS) new this season, and if so how much weight should past winners' reports get as templates?**
- Anchors: R-AN40; R-AN36; X-8; R-new.
- Anchor quote: "The Wharton Global Youth team is doing some reimagining of our signature competition" (Wharton news on
  the 2025 winners, VERIFIED-PRIMARY; the same sentence appears in the 2024 winners article).
- Hypothesis (guess): yes, new. 2025-26 had a mid-term report and a final report (VERIFIED-PRIMARY mention of
  "mid-term report submissions"; stage list SNIPPET-UNVERIFIED). A 2023-24 report shows the old structure: two
  trading notes with reflections, a "WInS Portfolio and Recommended Portfolio" section, and an advisor's comment
  (Teen Ink, VERIFIED-PRIMARY as a page, content is one team's report). The Rules page wording "based on the strength
  of their Investment Policy Statement (IPS) and Final Reports" (R-W24) may therefore be new text, not stale text.
- Would change: decision to weight the 2026-27 Guide and rubric above any past-winner pattern; and it removes a feared
  disadvantage: repeat schools have no practice with a 500-word frozen IPS either.
- Deliverables: TN, IPS, FR. Domain: D7. Seed: 29.
- North star: this year every team starts equal on the new formats; the team that reads the new rules most closely
  gains the most.

**Q6. Should the IPS state Laura's risk tolerance explicitly, split into ability (low for the promise) and willingness
(higher for the surplus), even though the case never states one?**
- Anchors: R-I2; R-W22; X-11; R-AN17; R-new (Guide p.2).
- Anchor quote: "Your team will need to consider the client’s goals, time horizons, required cash flows, funding
  commitments, liquidity needs, desired degree of funding certainty, risk tolerance, and communication with potential
  co-sponsors." (Guide p.2). The Rules page defines the IPS as "Define your client’s investment objectives, risk
  tolerance, and overall investment strategy." (R-W22)
- Hypothesis (guess): yes. Three official texts use "risk tolerance" (IPS guide definition, Rules page, Guide), while
  the case gives only "thoughtful risks" and "an appropriate balance". Readers trained on standard IPS templates will
  look for a stated risk tolerance; a split statement shows client understanding and explains why the plan is
  cautious with $292k and bolder with the surplus.
- Would change: one IPS sentence (content spec, not wording) and the FR client section.
- Deliverables: IPS, FR. Domain: D6. Seed: null.
- North star: Laura has said she takes thoughtful risks; naming where she can and cannot afford risk shows we heard
  both halves.

### Group B: what the typical team will submit, and where we can differ (tier 1-2)

**Q7. What will the median and the top-decile 2026-27 report look like, now that the case has an explicit liability and
Wharton's own example note buys a Treasury ETF?**
- Anchors: R-AN44; R-T23; SH-18; BS-10.
- Anchor quote: "We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce portfolio
  volatility and begin preparing for Laura’s future operating commitment." (TN guide p.2, VERIFIED-REPO-FILE)
- Hypothesis (guess): the median team will write "safe bucket + growth bucket" with a Monte Carlo percentile and buy a
  Treasury ETF because the example does; many will still add a stock-picking tour (the pre-2026 habit in the Teen Ink
  report). The top decile will have liability matching too (AI tools suggest it readily). So "lock early" alone will
  not separate us; the separator is Laura-specific reasoning, honest uncertainty and clarity (supports SH-18).
- Would change: where the team invests its writing effort (Laura-fit and co-sponsor credibility over architecture).
- Deliverables: IPS, FR. Domain: D7. Seed: 29.
- North star: if 6,000 firms offer Laura the same bond ladder, she chooses the one that explains it in her terms.

**Q8. When the right answer (match the payments with Treasuries) is textbook, what counts as "clear and creative" to
the readers?**
- Anchors: R-S24; R-S28; R-W43.
- Anchor quote: "Presents a clear and creative investment thesis" (R-S24) and "demonstrates original thinking and
  meaningful reflection" (R-S28).
- Hypothesis (guess): creativity is scored on the thesis and its fit to Laura, not on exotic instruments. Candidate
  sources of genuine originality: the 2031 co-sponsor rule (a bought floor plus a stated stretch), a certainty
  definition that needs no model, and reporting the plan as a funded ratio. Older Wharton guidance: "Your strategy
  should be unique to your team" and "Be creative as you develop your unique team strategy!" (developing-strategy
  page, older season, VERIFIED-PRIMARY). The 2018 readers' "memorable moments" were metaphors and honest reflections
  (Wharton news, 4 Apr 2018).
- Would change: the pitch's central idea (which one creative element leads), and which idea gets a Final Report chart.
- Deliverables: IPS, FR. Domain: D9. Seed: 29.
- North star: an idea Laura has not seen from other firms, which is also correct, is the reason to choose us.

**Q9. Do readers reward mapping the client's interests to holdings (a Taiwan ETF, publishing or media stocks), or does
that read as tokenism, and should the team drop the EWT/Taiwan tilt for that reason?**
- Anchors: R-S25; brief section 4 (identity rule); brief section 9 (EWT open item); R-AN34.
- Anchor quote: "Tailors the strategy to Laura's circumstances, priorities, risk considerations, and residency goals"
  (R-S25).
- Hypothesis (guess): the rubric names circumstances and goals, not interests. The Teen Ink report bought Nike and
  Marriott because the client liked sports and travel; it did not reach the Top 50 (list checked). Past clients praised
  being understood ("not just about the numbers, but about understanding and connecting with people", Ladi Ayoola,
  2025, VERIFIED-PRIMARY; finale context). INTERPRETATION: tailoring that changes the risk plan (lumpy book income,
  the co-sponsor audience) is rewarded; tailoring that only changes the ticker list is not, and for Laura it risks
  tokenism.
- Would change: decision on the EWT/Taiwan tilt (keep only if it earns its place on risk grounds, e.g., facility costs
  in TWD) and one FR sentence on why no interest-based picks.
- Deliverables: WInS-now, IPS, FR. Domain: D6. Seed: null.
- North star: Laura would recognise a plan built around her promise; she might resent one built around her ethnicity.

**Q10. Do the readers reward quantitative sophistication (algorithms, optimisation, machine learning) or restraint, and
how many quantitative tools should the Final Report show?**
- Anchors: R-S26; R-I23; R-I46.
- Anchor quote: "Demonstrates understanding and effective use of investment concepts and tools; integrates
  quantitative and qualitative analysis" (R-S26).
- Hypothesis (guess): mixed signals, resolved by depth. For: finale articles praise "customized algorithms, AI
  innovations, portfolio optimizations" (2025) and "next level" algorithms (2024). Against: Hahn's "fancy terms and
  formulas" (a semifinal judge who read the written reports); DMV's Finest's "less is more"; Roberts' "elegant
  simplicity"; the IPS guide's "Keep the presentation simple". The 2024 finale judge Vikas Keswani said the
  differentiator was sometimes "a little bit of it, but a lot of depth and accuracy" (VERIFIED-PRIMARY, finale
  context). Guess: one deeply checked analysis (the ladder priced on the official curve, with a rate-sensitivity
  table) plus one honest simulation for the surplus beats five methods.
- Would change: decision on the FR analysis list (keep, appendix, drop), e.g., whether bootstrapped forwards,
  Vasicek-type models or four-model comparisons appear at all.
- Deliverables: FR. Domain: D3. Seed: 29.
- North star: Laura studied statistics; she will trust one analysis she can check over five she cannot.

**Q11. What is our "cut list": which of our concepts stay in the Final Report's main text, which go to an appendix, and
which are dropped, and what test decides?**
- Anchors: R-I46; R-S28; brief section 8 (concepts already settled); Part 2 lesson 1.
- Anchor quote: "we laid everything out in a rough draft of our final report and everything clicked — we really needed
  to cut things down. It also led us to reflect: less is more, and having an explainable strategy makes a lot more
  sense than going for so many different things at once." (DMV's Finest, 2023 champions; Wharton news, VERIFIED-
  PRIMARY)
- Hypothesis (guess): the test is "does this change a recommendation for Laura or a number a co-sponsor will hear?"
  Terms like DV01, bootstrapping, forward zeros and wrong-way risk fail the test in the main text; the idea behind each
  can survive in plain words. The council list of 12 concepts is probably too many for the main text.
- Would change: decision on FR structure; the IPS vocabulary list (words allowed and banned).
- Deliverables: IPS, FR. Domain: D9. Seed: 14.
- North star: last year's report lost the insight in the packaging; a plan Laura can repeat to a co-sponsor in one
  breath is the plan she will choose.

### Group C: how to show a 16-year strategy through six weeks of trades (tier 1)

**Q12. How should the Final Report evaluate implementation, if not by P&L: can we grade the WInS book by how closely its
value tracked the value of Laura's ten payments, and must we start recording the data now?**
- Anchors: R-I37; R-W76; R-W60; R-new (Guide p.4: "Evaluate implementation of the IPS strategy").
- Anchor quote: "In the Final Report, your team will evaluate how effectively it implemented that strategy" (R-I37).
- Hypothesis (guess): yes. The natural implementation test for a matching strategy is tracking error against the
  liability: each day, WInS bond-sleeve value versus the present value of the ten payments on that day's official
  curve. If the ratio stayed near constant while rates moved, the hedge worked, whatever the P&L. Few teams will
  think of this. It needs daily data from Sept 28 (WInS values, Treasury par curves), which cannot be rebuilt
  exactly later if the team does not save WInS values as it goes.
- Would change: WInS-now process decision (save a daily or weekly WInS value snapshot and the curve date); a FR chart
  specification (funded ratio of the WInS book over the six weeks; data: WInS values, treasury.gov daily par curves,
  the verified PV script).
- Deliverables: WInS-now, FR. Domain: D3. Seed: 30.
- North star: showing that the promise stayed funded while markets moved is the proof Laura needs, far better than a
  return number.

**Q13. Which three trades best show strategic thinking, given that hundreds of teams will copy Wharton's Treasury-ETF
example, and should at least one be a decision that "tested or refined" the strategy?**
- Anchors: R-T8; R-T9; R-T20; R-AN40; R-AN44; R-new (Infographic).
- Anchor quote: "Show how three investment decisions supported, tested, or refined the developing strategy."
  (Infographic) and "Your research, analysis, Trading Notes, and experience implementing your strategy should all
  contribute to the IPS." (Guide p.2)
- Hypothesis (guess): a set of three that covers three roles (the promise, the surplus, a rule in action) and includes
  one genuine "refined" decision (for example a change forced by the position limit or by a rate move) reads as a
  living process. Three "supported" notes read as a shopping list. The refinement must be real: invented stories are
  banned (R-W28).
- Would change: decision on the trade plan to Oct 23; the selection rule for the three notes.
- Deliverables: WInS-now, TN. Domain: D7. Seed: 13.
- North star: Laura hires a process, not a portfolio; three notes that show the process working are the evidence.

**Q14. Can one WInS trade before Oct 23 be a pre-set rule firing (a rebalancing band or a rate trigger), so the notes
show time and discipline, not just a starting allocation?**
- Anchors: R-I3; R-I12; R-new (Guide p.5 "planned adjustments"); R-W73.
- Anchor quote: "It helps investors stay focused on long-term objectives and make disciplined decisions during
  changing market conditions." (R-I3)
- Hypothesis (guess): yes, if a band is set now and the market happens to cross it; it must not be forced. A trade
  that says "our rule said X, so we did X" is the best six-week evidence of a 16-year plan. If no band is crossed, a
  written "no trade, because the rule did not trigger" record is still Articulation evidence for the FR.
- Would change: decision to set and record bands before the next trade; the note spec for a rule-triggered trade.
- Deliverables: WInS-now, TN, IPS. Domain: D3. Seed: 30.
- North star: pre-commitment is how an adviser protects a client from panic; showing it in real time is proof.

**Q15. Because the Guide forbids redesigning the strategy after seeing results, must every contingency rule we might
want in the Final Report (rates fall before January 2027; 2028 deposit smaller or late; 2031 floor rule; 2033 reserve
rule) already be named in the IPS?**
- Anchors: R-new (Guide p.5); R-I35; R-I32; brief section 9 (rule if rates fall).
- Anchor quote: "you may not redesign your strategy after observing the results." (Guide p.5) and "These elements will
  be developed and supported in the Final Report using the strategy established in the IPS." (R-I32)
- Hypothesis (guess): yes. The ladder cost more than $300k on 173 of 185 trading days of 2026 (F-111), and the chance
  it costs more on 2027-01-01 is about 24% (F-112, ASSUMPTION-based). If rates fall between Nov 6 and Dec 4 and the
  FR then introduces a "buy long rungs first" rule that the IPS never mentioned, a reader may see a post-hoc redesign.
  Named in the IPS as a planned adjustment, the same rule is evidence of foresight.
- Would change: decision on the IPS rule list (which rules appear, in plain words, within 500 words).
- Deliverables: IPS, FR. Domain: D10. Seed: 31.
- North star: Laura needs to know what we will do before it happens; the rules say so too.

**Q16. Which single statement reconciles the WInS book with Laura's 16-year plan, so a reader does not see two
different strategies?**
- Anchors: R-W59; F-605; R-AN14; X-7; brief section 9 (WInS mirror open item); R-I36.
- Anchor quote: "Your portfolio and Final Report should reflect the strategy established in your IPS." (R-I36)
- Hypothesis (guess): the new evidence is that WInS cash ($300k) equals the 2027 deposit exactly (F-605), so a reader
  may expect WInS to be the 2027 portfolio. If WInS instead mirrors the post-2028 target, one sentence in the IPS or
  FR must say which date WInS represents and why. The allocation work (wins_now v0) shows the post-2028 mirror and
  the plan's total equity can be the same portfolio once "65/35" is read as hedge/sleeve (F-409).
- Would change: decision on which snapshot WInS shows; one reconciling sentence (spec) in the IPS and FR.
- Deliverables: WInS-now, IPS, FR. Domain: D7. Seed: 30.
- North star: one strategy told the same way three times is what the rubric calls cohesive, and what makes Laura
  confident.

**Q17. Should at least one WInS holding be an individual U.S. Treasury bond maturing near a payment date, to show
cash-flow matching rather than only duration matching?**
- Anchors: R-W69; R-W91; R-AN52; F-206; brief section 8 items 11-13.
- Anchor quote: "Treasury Bonds: Bonds available on WInS. The list includes Treasury bonds from the United States"
  (R-W69).
- Hypothesis (guess): yes, if WInS lists a suitable maturity: it is rare (most teams will use ETFs), it answers the
  fixed-income reader's first question (Q4), and it turns "we would buy a ladder in 2027" into a demonstrated action.
  Costs: $10 commission, daily-updated bond prices, the position limit. It could also make a strong trading note.
- Would change: WInS trade plan decision (PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK).
- Deliverables: WInS-now, TN. Domain: D1. Seed: 30.
- North star: showing, not telling, that the promise can be bought today.

### Group D: process evidence and honesty (tier 1-3)

**Q18. What real process evidence should the team start capturing this week (dated decision log with disagreements,
roles, a mistake we "ran with", why we did not trade), so the Articulation criterion has true material in December?**
- Anchors: R-S27; R-W28; R-W94; R-W87; SH-20.
- Anchor quote: "Demonstrates teamwork, communication, and learning; clearly explains the team's research and
  decision-making process; and reflects meaningfully on the team's growth and response to challenges." (R-S27)
- Hypothesis (guess): readers value the journey; the 2018 Aberdeen lead reader "enjoyed reading about their
  educational journey over the course of the competition" (VERIFIED-PRIMARY). Invented stories are banned, so only
  logged, dated events can be used. Teams that start logging in November will have thin evidence.
- Would change: WInS-now process decision (who keeps the log, what fields, weekly).
- Deliverables: WInS-now, FR. Domain: D7. Seed: 31.
- North star: Laura is hiring people; the log is the evidence of how those people decide.

**Q19. How detailed and honest should the Final Report's record of AI use be, and could a specific, verified disclosure
become a trust signal rather than a weakness?**
- Anchors: R-W46; R-W47; R-W49; R-W26; X-17.
- Anchor quote: "If you use AI to assist you in any way during the competition, how you use it must be recorded in
  your Works Cited pages." (R-W46)
- Hypothesis (guess): many teams will under-disclose. A specific record (tool, date range, purpose: brainstorming and
  fact-finding; what the team checked itself; that all text is the students') fits "treat AI as a weak source"
  (R-W47) and supports "authentic team voice". No public evidence on how readers score disclosures (UNKNOWN).
- Would change: WInS-now decision to keep an AI-use log from today; FR Works Cited spec.
- Deliverables: WInS-now, FR. Domain: D10. Seed: 31.
- North star: Laura's first book answered misinformation (R-AN33); a firm that is honest about its own tools earns her
  trust.

**Q20. Can the semifinal readers see our WInS holdings and transaction history, and if so, must every open position at
the freeze have a stated purpose?**
- Anchors: R-T34; R-W80; R-AN42; R-S6.
- Anchor quote: "Your portfolio should reflect a cohesive strategy designed around the client’s goals. Each
  investment decision should have a clear purpose within that strategy." (R-W80) and "Yes, we will verify this."
  (R-T34)
- Hypothesis (guess): Wharton can see every team account (it verifies notes), so readers can probably check the frozen
  book. Any leftover test position, odd lot or unexplained cash balance on Nov 6 becomes an inconsistency.
- Would change: WInS-now decision (a pre-freeze clean-up check in the week of Nov 2; every position mapped to a role).
- Deliverables: WInS-now, IPS, FR. Domain: D10. Seed: 31.
- North star: a tidy book is the visible proof that the strategy runs the portfolio.

### Group E: pre-mortem (why a correct strategy could still miss the Top 50) (tier 2-3)

**Q21. What are the realistic odds, and what does the pattern of past semifinal schools say about which controllable
features matter most?**
- Anchors: F-609; R-AN60; R-W8; R-W24.
- Anchor quote: "On December 12, some 2,300 teams from 79 countries submitted final reports" (R-W99).
- Hypothesis (guess): about 49 open slots among ~2,300 finishers (~2.1%, DERIVED), with one automatic slot for a team
  from Stuyvesant (INTERPRETATION of the stated rule). Most semifinal schools are new each year (7 of 49 repeated from
  2025; 11 of 50 from 2024; DERIVED), so pedigree is not decisive; controllable features (rubric coverage, clarity,
  consistency, format compliance) are. A correct strategy can still miss by failing a format rule (R-I39), burying the
  strategy, or being inconsistent across the three deliverables.
- Would change: decision on where the last two weeks before each deadline go (compliance and consistency review, not
  new analysis).
- Deliverables: TN, IPS, FR. Domain: D7. Seed: 31.
- North star: Laura never sees a plan that was screened out on format; compliance is the entry ticket.

**Q22. Is there any sign that non-U.S. teams are disadvantaged in the written round, and does anything in our writing
(spelling, date format, currency labels, Australian references) create avoidable friction for U.S. readers?**
- Anchors: R-AN10; Part 2 lesson 4; R-W72.
- Anchor quote: "You are not expected to stay awake during the night to trade." (R-W72; written with non-U.S. teams in
  mind)
- Hypothesis (guess): no structural disadvantage: the 2025-26 list includes teams from Turkey, India, China, the
  Czech Republic, Italy, Thailand, Singapore, Germany and Brazil. But only one Australian team appears in five years
  of lists (2022). Low Australian participation is the likelier cause (UNKNOWN). Small frictions are cheap to remove:
  "US$" on every dollar figure (the case never names a currency), unambiguous dates (4 December 2026), and one
  consistent spelling standard.
- Would change: a style-sheet decision for all three deliverables.
- Deliverables: TN, IPS, FR. Domain: D9. Seed: 31.
- North star: nothing in the writing should make a reader work harder to see why Laura would choose us.

**Q23. Does the Final Report open with the strategy "clearly stated, defined and articulated up front", so a reader who
reads only page 1 can state our strategy, our certainty definition and our facility range?**
- Anchors: R-S28; R-I30; R-W41.
- Anchor quote: "if you provide us with a team strategy that is buried somewhere in your experience, rather than
  clearly stated, defined and articulated up front, you will not be among the strongest teams." (developing-strategy
  page, older season text, VERIFIED-PRIMARY)
- Hypothesis (guess): this is the most common failure among strong teams that write chronologically ("first we
  researched, then we traded"). A page-1 test with someone outside the team would catch it.
- Would change: decision on FR structure; a page-1 test before Dec 4.
- Deliverables: FR (also the IPS pitch). Domain: D9. Seed: 31.
- North star: Laura (and a co-sponsor) will read the first page; it must answer her question.

**Q24. Which Final Report content must be collected during trading because it cannot be recreated after the Nov 6
freeze, given the instructions arrive only on Nov 9?**
- Anchors: R-S19; R-C93; R-AN36; R-I57.
- Anchor quote: "Detailed Final Report instructions and requirements will be shared on November 9." (R-S19)
- Hypothesis (guess): past final reports had a fixed format (a search snippet says 7-11 pages, double-spaced, Times
  New Roman 12, with a portfolio breakdown graphic including "team member responsibilities"; SNIPPET-UNVERIFIED) and
  included trading notes, a WInS vs recommended portfolio and an advisor comment (Teen Ink 2023-24 report). Items that
  are lost if not captured now: WInS value snapshots (Q12), screenshots of Session Rules, the decision log (Q18), the
  AI-use log (Q19), sources with access dates (R-I57). Teacher advice: "Chunk the final report... have students begin
  working on the final report as early as you can" (Wharton Essential Educator blog, VERIFIED-PRIMARY).
- Would change: a WInS-now collection checklist and owners.
- Deliverables: WInS-now, FR. Domain: D7. Seed: 31.
- North star: the Final Report proves the process; the proof must be gathered while the process happens.

**Q25. Can we find any public account of what FigCapital, HHA Investments or other 2025-26 semifinalists wrote for the
Barwin case, to calibrate the most recent "strong team" before our IPS is frozen?**
- Anchors: F-610; R-W52.
- Anchor quote: "Stuyvesant High School (New York City, NY) — FigCapital" (2026 champions article, VERIFIED-PRIMARY).
- Hypothesis (guess): unlikely to exist in readable form. FigCapital was a 2025 top-10 finalist ("Fig Capital",
  VERIFIED-PRIMARY) and won in 2026, so repeat experience helps. Scribd holds documents titled "Updated Investment
  Strategy For Connor Barwin" and "Wharton Competition - Final Report" (titles only; pages blocked; SNIPPET-UNVERIFIED;
  authorship and ranking unknown). If a verified semifinal report is found, it recalibrates Q7; if not, Q5's
  conclusion stands (use the 2026-27 rubric). Never copy: "plagiarize existing strategies" is banned (R-W28).
- Would change: the benchmark in Q7 (a number: how common liability matching was among 2025-26 finalists).
- Deliverables: IPS, FR. Domain: D7. Seed: 29.
- North star: knowing the strongest rival lets us make sure our difference is about Laura, not about fashion.

**Q26. Should the Final Report explain how the team would keep Laura on plan in a bad market (a behavioural rule), and
treat her whole financial picture (book income) as part of the risk plan?**
- Anchors: R-I3; R-S25; BS-03 (human capital); SH-04.
- Anchor quote: "urging them (as investment advisors) to consider behavioral finance and their clients’ emotions
  during a market downturn" and "When analyzing someone’s investments, take a look at this person holistically"
  (2024 winners article; judges Balchunas and McCormick; finale context; VERIFIED-PRIMARY).
- Hypothesis (guess): yes, one rule each. McCormick worked in North American fixed income at abrdn, the firm that
  supplies semifinal readers, so her view probably reflects theirs (INTERPRETATION). For Laura, "holistically" means
  her income depends on her reputation and publishing cycles, so the 2028 deposit can be late or smaller; the portfolio
  should not add risk that moves with her career.
- Would change: an IPS principle (discipline in downturns) and an FR section spec (human-capital paragraph; behaviour
  rule).
- Deliverables: IPS, FR. Domain: D6. Seed: null.
- North star: Laura chooses an adviser who plans for the bad year before it comes and sees her as more than an
  account.

---

## 3. Evidence found (with status)

### 3.1 New official 2026-27 documents (VERIFIED-PRIMARY, read 2026-09-27)
- SMApply page "Investment Competition Guide": https://wghsinvcomp.smapply.us/res/p/guide/ : "Start by reviewing the
  Investment Competition Guide with your entire team." It links:
  - Guide PDF https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf, 5 pages, 1,715 words
    extracted, SHA-256 `3638e84692ed0d826660a65e89cad0ce7eea8c1907b6a8f00ce02c0d51fb7add`.
  - Infographic https://upenn.box.com/s/l2p0l26svbbptmcizhmswyq5f7rbyp44 (file "2026_WGY_Competition
    Inforgraphic-FINAL.pdf", 1 page), SHA-256 `2827f92a989d6d72fbc253d80d975eb06bd00c86f631e83850ae17eec544ed10`.
  - Neither file is in `competition/official/2026_27/`, and neither appears in the Phase A registers (checked with
    grep).
- Other Guide sentences worth registering (exact):
  - "The goal is to develop a cohesive strategy in which your investment decisions work together to support the
    client’s objectives across a range of possible market outcomes." (p.2)
  - "WInS is a tool for implementing your investment strategy. It is not the competition scorecard" (p.3)
  - "The Trading Notes Analysis is due at the end of Week 4 (October 23), two weeks before your IPS is due." (p.3)
  - ARTICULATE step: "Clearly communicate the investment strategy your team developed, including how it addresses risk
    and uncertainty, as well as the framework that guides its investment decisions." (p.4)
  - "The competition deliverables are not separate assignments." (p.4)
  - Key dates: "September 15: Competition Materials Released" (p.5).
  - Infographic: "There is no single correct strategy. Strong teams explain the reasoning, assumptions, and tradeoffs
    behind their decisions."

### 3.2 Who reads the written deliverables
- 2025-26: "with the help of our Wharton School student evaluators, as well as a professional review panel of asset
  managers from Aberdeen Investments in Philadelphia" (news, 27 Jan 2026). VERIFIED-PRIMARY (grep).
- 2024-25: "After careful consideration by our internal reviewers and a group of professional asset managers" (news,
  2025 semifinalists). 2023-24: "our internal reviewers and a group of professional asset managers from abrdn in
  Philadelphia". 2022-23: "internal reviewers and a group of professional asset managers from abrdn". 2021-22:
  "internal reviewers and a group of professional asset managers from Aberdeen Standard Investments". All
  VERIFIED-PRIMARY.
- abrdn press release, 30 Jan 2023: abrdn "provides evaluators from across the investment spectrum for the
  competition’s semifinal round, reviewing more than 1,400 investment strategy proposals"; Eli Lesser: "our investment
  competition mission to promote client-focused objectives, a long-term-investing mindset, thoughtful analysis, and
  strategic decision-making." VERIFIED-PRIMARY.
- 2018 Region 3: "assembled a group of 13 other Aberdeen professionals to read and evaluate the Region 3 reports"; 160
  reports; readers from "equity, fixed-income and alternative investing, as well as marketing and distribution";
  "we enjoyed reading about their educational journey over the course of the competition." VERIFIED-PRIMARY (news,
  4 Apr 2018).
- Semifinal judge who read written reports (2025): Melissa Ko Hahn quotes in section 0 item 4. VERIFIED-PRIMARY.

### 3.3 Winners, semifinalists and the field (all from official Wharton news pages, VERIFIED-PRIMARY)
| Season | Final reports | Semifinalists | Share (DERIVED) | Winner (1st) |
|---|---|---|---|---|
| 2021-22 | ~1,300 | 50 | 3.8% | Sailing to Success (Arizona) |
| 2022-23 | ~1,400 | 55 | 3.9% | DMV's Finest (Thomas Jefferson HS, VA) |
| 2023-24 | >1,600 | 50 | ≤3.1% | Spark Investments (Bergen County Academies, NJ) |
| 2024-25 | >1,800 | 50 | ≤2.8% | BAM Investing (Deerfield Academy, MA) |
| 2025-26 | ~2,300 (counter 2,339) | 49 listed ("Top 50"; "49 semifinalist teams advanced") | 2.1% | FigCapital (Stuyvesant HS, NY) |
- Automatic slot: "one team from Deerfield Academy will automatically advance to next year’s semifinals (as long as
  they submit all the deliverables)" (2025 winners article); same rule stated in 2023 and 2024. For 2026-27 the rule
  implies a Stuyvesant team (INTERPRETATION; not announced).
- Repeat schools (DERIVED by matching school names in consecutive official lists): 2026 vs 2025: 7 of 49 (Amity
  International, Deerfield, Lycée Français de Chicago, Nový PORG, Richard Montgomery, Stuyvesant, Western Canada);
  2025 vs 2024: 11 of 50. Repeat teams can climb: DMV's Finest reached the 2022 final, won in 2023; Fig Capital was a
  2025 finalist and won in 2026.
- Australia: Gryphon Group, Brisbane State High School (2022 list) is the only Australian team in the 2022-2026 lists
  (grep of all five lists). New Zealand: Kristin School in 2022 and 2023.
- Minor anomaly: the Jan 2026 "Top 50" list has 49 entries (count of list markers), matching the March article's "49
  semifinalist teams advanced". No decision rests on it.

### 3.4 What past winners and readers said about written work and analysis quality (VERIFIED-PRIMARY)
- DMV's Finest (2023 champions) on the final report draft: quoted in Q11.
- Alex Lamon (teacher-advisor): "It is easier to develop a strategy first and buy stocks second... Remember, winning
  isn’t about portfolio gains. It is about having a coherent strategy." (Tales from the 2023 Teams). Also, from his
  Essential Educator blog: "The final report is the most important deliverable students produce." and "Chunk the
  final report." The same blog is the likely origin of the false "sector minimum = team size" claim: "Students need to
  invest in as many industries as they have team members" (an older-season rule; this season has no sector minimum,
  R-W70).
- Developing-strategy page (older season; mentions an approved stock list and "He is introduced in the Case Study"):
  "Evaluators want to understand why you are doing what you are doing" and the "buried" warning (Q23).
- Prof. Michael Roberts (academic director; 2022 interview): "It rests on two intuitive principles: costs and benefits,
  and risk."; "to get 90% of it you really only need basic arithmetic and maybe a little bit of probability and
  statistics."
- Finale-context judge remarks (used only for what they say about analysis quality): Chirag Jain (Aberdeen, 2025):
  "What distinguished managers was clear thoughtfulness and reasoning behind all the decisions that they put
  together."; Vikas Keswani (2024): "a little bit of it, but a lot of depth and accuracy"; Balchunas and McCormick
  (2024): Q26.

### 3.5 A typical (non-semifinal) past report
- "Profiteering Peninsula Panthers 2023-2024 Wharton Global High School Investment Competition Final Report", Teen Ink,
  https://www.teenink.com/opinion/all/article/1215809/ (page states "This is the final report submitted to Wharton
  Global High School Investment Competition 2023-2024."). The team is not in the 2024 Top 50 list (checked).
  Features: sector-by-sector stock descriptions; picks justified by the client's interests ("caters to Ms. Ash’s love
  of sports"); results used as proof ("The team’s decision was proven with great success"; "our portfolio grew 4.2%,
  affirming our updated strategy"); two trading notes with reflections; a WInS vs recommended portfolio section; an
  advisor comment; a works-cited list. VERIFIED-PRIMARY as a page; it is one team's work, so treat it as an example,
  not a statistic.

### 3.6 Snippet-only or blocked
- 2025-26 stages "required trade; roster; midterm report; final report" (CompeteMap, third party, "last checked 22 Jul
  2026"). SNIPPET-UNVERIFIED as a description of official rules.
- 2025-26 "trade execution by October 10... midterm and final reports by December 12" (search summary of a Scribd
  "25-26 Welcome Email"). SNIPPET-UNVERIFIED.
- Past final report "7–11 page document (double-spaced, 12-point Times New Roman, 1-inch margins...)" with a
  "portfolio breakdown graphic (sectors, team member responsibilities, stock holdings, client-specific allocations)"
  (search summary, source not identified). SNIPPET-UNVERIFIED.
- "Nearly 6,000 teams competed" is on the Stuyvesant school blog (talos.stuy.edu, read 2026-09-27), a school source,
  not a Wharton page. It explains the origin of the North Star's "6,000".
- Blocked: Scribd documents 979966514, 832434822, 977481046 (JavaScript wall); Medium (403); Croton Chronicle (paywall).

---

## 4. Sources (all accessed 2026-09-27)

| # | Source | URL | Date of piece | Status |
|---|---|---|---|---|
| 1 | SMApply "Investment Competition Guide" page | https://wghsinvcomp.smapply.us/res/p/guide/ | 2026-27 | VERIFIED-PRIMARY |
| 2 | 2026-27 Investment Competition Guide (PDF) | https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf | 2026-27 | VERIFIED-PRIMARY |
| 3 | 2026-27 Competition Infographic (PDF) | https://upenn.box.com/s/l2p0l26svbbptmcizhmswyq5f7rbyp44 | 2026-27 | VERIFIED-PRIMARY |
| 4 | Top 50 2026 article | https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/ | 2026-01-27 | VERIFIED-PRIMARY |
| 5 | 11 teams advance 2026 | https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/ | 2026-03-20 | VERIFIED-PRIMARY |
| 6 | 2026 champions | https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/ | 2026-04-30 | VERIFIED-PRIMARY |
| 7 | 2025 semifinalists | https://globalyouth.wharton.upenn.edu/news/announcing-the-semifinalists-in-the-2025-wharton-global-high-school-investment-competition/ | 2025 (Jan) | VERIFIED-PRIMARY |
| 8 | 2025 top 10 (Hahn quote) | https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/ | 2025 (Mar) | VERIFIED-PRIMARY |
| 9 | 2025 winners (BAM) | https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/ | 2025 (Apr) | VERIFIED-PRIMARY |
| 10 | 2024 semifinalists | https://globalyouth.wharton.upenn.edu/news/here-are-the-top-50-teams-advancing-to-wharton-global-youths-2024-investment-competition-semifinals/ | 2024 | VERIFIED-PRIMARY |
| 11 | 2024 winners (Spark) | https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/ | 2024 (Apr) | VERIFIED-PRIMARY |
| 12 | 2023 semifinalists | https://globalyouth.wharton.upenn.edu/news/congratulations-to-our-2023-investment-competition-semifinalists/ | 2023 | VERIFIED-PRIMARY |
| 13 | 2023 winners (DMV's Finest) | https://globalyouth.wharton.upenn.edu/news/the-2023-investment-competition-global-finale-ends-in-sweet-victory-for-dmvs-finest/ | 2023 (Apr) | VERIFIED-PRIMARY |
| 14 | Tales from the 2023 teams | https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/ | 2023 (Jun) | VERIFIED-PRIMARY |
| 15 | 2022 semifinalists | https://globalyouth.wharton.upenn.edu/news/introducing-the-2022-semifinalists-in-the-wharton-global-high-school-investment-competition/ | 2022 | VERIFIED-PRIMARY |
| 16 | 2022 finale | https://globalyouth.wharton.upenn.edu/news/top-teams-sail-to-success-in-the-2022-wharton-investment-competition-global-finale/ | 2022 (Apr) | VERIFIED-PRIMARY |
| 17 | Developing a Strategy (older-season page) | https://globalyouth.wharton.upenn.edu/developing-strategy/ | undated | VERIFIED-PRIMARY |
| 18 | Essential Educator: 10 tips (Lamon) | https://globalyouth.wharton.upenn.edu/essential-educator-blog/the-essential-educator-10-tips-for-teaching-the-wharton-investment-competition/ | undated (after 2019-20) | VERIFIED-PRIMARY |
| 19 | Prof. Michael Roberts interview | https://globalyouth.wharton.upenn.edu/news/prof-michael-roberts-wants-global-youth-students-to-discover-the-elegant-simplicity-of-finance/ | 2022 | VERIFIED-PRIMARY |
| 20 | Region 3 finalists (Aberdeen readers) | https://globalyouth.wharton.upenn.edu/news/kwhs-investment-competition-region-3-finalists/ | 2018-04-04 | VERIFIED-PRIMARY |
| 21 | abrdn press release | https://www.aberdeenplc.com/en-gb/news/all-news/abrdn-enters-second-decade-supporting-wharton-investment-competition-for-students | 2023-01-30 | VERIFIED-PRIMARY |
| 22 | Teen Ink 2023-24 final report | https://www.teenink.com/opinion/all/article/1215809/Profiteering-Peninsula-Panthers-2023-2024-Wharton-Global-High-School-Investment-Competition-Final-Report | 2024 | VERIFIED-PRIMARY (page) |
| 23 | Stuyvesant blog | https://talos.stuy.edu/cms/pages/stuyvesant-blog/stuyvesant-high-school-wins-the-2026-wharton-global-high-school-investment-competition-26/ | 2026 | VERIFIED-PRIMARY (school source) |
| 24 | Wharton story (2026 finale) | https://www.wharton.upenn.edu/story/wharton-global-high-school-investment-competition-hosts-future-business-leaders/ | 2026 | VERIFIED-PRIMARY |
| 25 | Delbarton news (2025 finalist) | https://www.delbarton.org/about-us/news-detail/~board/homepage/post/delbarton-is-finalist-in-whartoninvestment-competition | 2025 | VERIFIED-PRIMARY (school source) |
| 26 | CompeteMap listing | https://competemap.com/competitions/cmrw8ls8y0001vnne2cnjon1n | checked 2026-07-22 | SNIPPET-UNVERIFIED (third party) |
| 27 | Scribd documents 979966514, 832434822, 977481046, 942363888, 820640088 | scribd.com | various | BLOCKED (titles from search only) |
| 28 | Medium "My experience with the Wharton..." | abhinav-penagalapati.medium.com | unknown | BLOCKED (403) |

Repo files used: `research/insight_v1/_context/brief.md`; `research/ultracode_prompt_v4_deep_strategy.md`; `CLAUDE.md`;
`research/insight_v1/phase_A/{case_register,fact_register,stakeholder_map,wins_week1_guardrails}.md`;
`research/council_2026-09-27/groundwork/winners.md`; `research/council_2026-09-27/02_judge_panel.md`;
`research/blueprints/01_trading_notes_blueprint.md`; `research/insight_v1/wins_now/securities_and_allocation_v0.md`.

Corrections to winners.md (council): the Hahn quote is now VERIFIED-PRIMARY and comes from the 2025 top-10 article
(source 8), not the 2022 finale page; "Less is more" is verified for DMV's Finest (source 14) and, separately, for
judge Andrea Vittorelli at the 2022 finale ("Cut slides, cut words, cut minutes", source 16, finale context). The
Aquino quote was not found on any page I read (still UNVERIFIED).

---

## 5. Leads for the specialists

- **D10 (compliance) / main loop:** add sources 2 and 3 (hashes in section 3.1) to the official set and the case
  register; re-check every checklist against the Guide's note-content list (Q2) and hindsight rule (Q15). The Guide
  says the Evaluation Criteria are "located under the Pages tab => Deliverables" (same as R-S24 to R-S28).
- **D7 (competition history):** the official news archive has Top-50 lists for every season since 2021-22 (sources 4,
  7, 10, 12, 15). The 2018 Region 3 page (source 20) quotes a dozen passages from final papers that the organisers
  found memorable: the only public sample of what readers liked in written reports. Try a school-news search for each
  2025-26 finalist (Hooke Investments, Westminster; Perse Capital Group; Asgard Assets; Better Future Fund; Malo
  Management) for descriptions of their written strategy. The Wharton "Meet the Experts" videos include a past winner
  (2018 champion), per source 18.
- **D1 (fixed income):** expect Aberdeen fixed-income readers (sources 11, 20, 6). Prepare the fund-versus-ladder
  distinction and check which individual U.S. Treasuries appear in WInS (R-W69) and their maturities near 2033-2042
  payment dates.
- **D3 (quant):** specify the implementation-tracking chart (Q12): daily WInS bond-sleeve value divided by the PV of the
  ten payments on the same day's official par curve (reuse `research/verified_2026-09-27/official_curve_pv.py`). The
  team must save WInS values from Sept 28 onward.
- **D9 (plain English):** use the verified quotes of Hahn, DMV's Finest and Roberts (section 3.4) as the editing
  standard; build the cut list (Q11) and page-1 test (Q23).
- **D6 (client psychology):** the rubric's "earn her confidence" (R-S25) plus the 2024 judges' "clients’ emotions
  during a market downturn" and "holistically" (source 11) support a behaviour rule and a human-capital paragraph.
- **Everyone:** the Teen Ink report (source 22) is a clear picture of the habits this year's rubric penalises: returns
  as proof, hobbies as tickers, many shallow stock descriptions.

---

## What this teaches

A competition is judged by people, and the best evidence of what they reward is what they have written down, not what
people guess. Here, the readers (Wharton students first, then professional asset managers, some of them bond
specialists) and the organisers keep repeating the same few ideas: state the strategy up front, show the reasoning,
assumptions and tradeoffs, keep it simple, and let every decision follow from one idea about the client. Checking the
official site closely also found two official 2026-27 documents nobody had filed yet, which is a reminder that the
cheapest insight is often reading the rules one more time. Finally, the numbers teach humility: about 2 in every 100
finishing teams reach the Top 50, and most of them are new schools each year. The teams that make it are not the ones
with the fanciest maths, but the ones whose written work a busy reader can understand, check and trust.
