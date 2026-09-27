# B7b Competition Meta & Judges: simulate the field, then find where we can be different and still right

Agent B7b, insight_v1 run, Phase B (question generation), written 2026-09-27. Lens: Competition Meta & Judges
(semifinals only: the written Trading Notes Analysis, IPS and Final Report). Starting angle: first write down what a
typical strong team will submit for the Laura Gao case, then ask where readers will see sameness, what distinctive but
correct moves exist, and how each deliverable's mechanics reward or punish each approach.

This file is research for the team. It contains questions, evidence and specifications. It contains no text meant for
submission. Every factual claim carries a status label (brief section 3). Anything about Laura is limited to the case
and her public professional record.

---

## 0. Summary (read this first)

1. **Two official 2026-27 documents are missing from the repo and from Phase A.** The public SMApply page
   "Investment Competition Guide" (https://wghsinvcomp.smapply.us/res/p/guide/) links two Box PDFs:
   - a 5-page **"2026–2027 Investment Competition Guide"** (created 2026-09-09);
   - a 1-page **"Competition Phases" infographic** (created 2026-09-14).

   I downloaded and read both (VERIFIED-PRIMARY, 2026-09-27). They contain the clearest official statements yet of
   what readers want. Four examples:
   - "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and
     tradeoffs behind those decisions."
   - "Do not treat Trading Notes as an afterthought."
   - The Trading Note should capture the decision's "expected role in growth, liquidity, risk management, or future
     funding."
   - "A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten
     simply because markets move or hindsight reveals a different outcome. You may identify decisions you would make
     differently, but you may not redesign your strategy after observing the results."

   The main loop should add both files to `competition/official/2026_27/` with their hashes (section 6). I did not
   write outside my assigned file.
2. **Who reads the written deliverables is now known for last season (VERIFIED-PRIMARY).** The 2026 Top 50 were
   picked "with the help of our Wharton School student evaluators, as well as a professional review panel of asset
   managers from Aberdeen Investments in Philadelphia". The 2025 Top 50 used "internal reviewers and a group of
   professional asset managers from abrdn". A 2026 finale judge from Aberdeen held the title "U.S. Credit Investment
   Manager". So a bond professional may read our reports, and a Wharton student may read them first. Nobody has
   published this season's reader panel yet.
3. **The rubric changed since 2023-24, and the changes point away from decoration.** A third-party transcription of the
   2023-24 criteria (SNIPPET-UNVERIFIED as to Wharton's wording) included "visually pleasing presentation of data; many
   creative elements" and "would win him/her over as a client". The 2026-27 criteria (VERIFIED-REPO-FILE) instead say
   "uses data effectively to support conclusions; demonstrates original thinking", "recommendations that can earn her
   confidence", "disciplined planning across Laura's changing time horizons and cash-flow needs", and "maintains
   consistency with the team's IPS". The sector-count rule was dropped.
4. **The deliverable format is new this season, so nobody has a template.** In 2025-26 the deliverables were a
   mid-term report (Oct 31) and a final report (Dec 12), plus a first trade by Oct 10 (SNIPPET-UNVERIFIED, Scribd
   search summary). A 2025-26 semifinalist described "the required 15-page report" (VERIFIED-PRIMARY news article; the
   rule itself is secondary). The Trading Notes Analysis, the 50-word pitch and the 500-word IPS appear to be new for
   2026-27. Repeat schools cannot copy last year's structure for these two deliverables.
5. **What a strong rival looked like last year (VERIFIED-PRIMARY, KXAN via Yahoo).** Vandegrift's 2025-26 semifinalist
   team used a four-part stock screen, "thousands of Monte Carlo simulations", stress tests against the dot-com crash,
   2008 and COVID, and reported "a 70% chance of reaching the long-term goal". Expect this year's strong teams to bring
   the same toolkit to a case that asks for "a high degree of certainty". Many will print a Monte Carlo "95%".
6. **Field arithmetic (DERIVED from VERIFIED-PRIMARY pages).**
   - About 2,339 teams finished in 2025-26.
   - The Rules page lets the 2026 champion school (Stuyvesant) fast-track one team to this season's semifinals, so
     about 49 seats are open, roughly 2.1% of finishers.
   - About 9 of the 2026 Top 50 teams came from schools that were also in the 2025 Top 50, so repeat schools matter.
   - No Australian school appears in either year's Top 50 list.
7. **The field simulation (section 2) finds the sameness hot-spots.** Expect a "three buckets + glide path" structure,
   a Monte Carlo "95%", a p10-p90 range, clones of Wharton's own Treasury-ETF example note, puns on her book titles,
   a Taiwan-ETF "connection" trade, and WInS return measured against the S&P 500. Our lock-early architecture is correct
   but may not be rare, because AI tools at 5% yields may also suggest a Treasury ladder (BS-10). The durable edge is
   therefore likely to be proof: rules executed in WInS, a hedge that visibly tracked the promise, and an evaluation
   measured against the liability.
8. **27 questions follow (section 4)**, ranked by deadline tier. The top five for WInS now:
   - Q8: log the value of the promise against the WInS hedge daily, from now on.
   - Q27: write each WInS note in Wharton's own role vocabulary.
   - Q6: plan one note each for "supported", "tested" and "refined".
   - Q7: a decision *not* to trade can never become a Trading Note.
   - Q25: check the unpublished "required trading activity" rule.

---

## 1. Method

- Read the brief, the v4 prompt Parts 1-3, 5 and 6, CLAUDE.md, all official files, and the Phase A files (case register,
  fact register, stakeholder map, WInS guardrails). Also read the council judge panel (`02_judge_panel.md`), the
  winners groundwork (`groundwork/winners.md`), the Trading Notes blueprint and the S1 securities file.
- Web: WebSearch to find URLs, then `research/insight_v1/scripts/fetch_text.py` or curl to read each page. Every quote
  marked VERIFIED-PRIMARY was read on the page itself, and the key ones were checked with `--grep`. Scribd,
  SlideShare, web.archive.org and KXAN refused or needed JavaScript. Those items are marked accordingly.
- Field simulation: my judgement (ASSUMPTION), built from:
  - last season's semifinalist evidence (KXAN, HW Chronicle);
  - finale descriptions ("sentiment, SWOT and Pestel analyses, customized algorithms, AI innovations, portfolio
    optimizations");
  - third-party prep guides (Aralia, Lumiere);
  - what a generic AI answer to this case would likely contain.

  It has not been tested. Q1 proposes the test.

---

## 2. Simulating the field: what a typical strong team will submit (ASSUMPTION unless labelled)

### 2.1 The obvious strategy
- **Three buckets:** growth now (60-80% equity until about 2030), a glide path from 2030 to 2033, and a bond reserve
  bought in 2031-2033 or built gradually.
- **Reserve method:** present value of ten $50k payments at a flat 4-5%, which gives about $395-420k at 2033 (compare
  F-110). Often the timing is wrong, with no annuity-due and no check on when the first payment falls.
- **Certainty:** "Monte Carlo, 10,000 simulations, 95% probability of funding all payments". Evidence: last season's
  semifinalist used Monte Carlo and quoted a 70% probability (VERIFIED-PRIMARY, KXAN via Yahoo).
- **2031 range:** the 10th to 90th, or 25th to 75th, percentile of simulated 2033 surplus. Confidence stated as the
  percentile width (80% or 50%).
- **Holdings:**
  - 15-40 individual stocks, often with SWOT or PESTEL write-ups, because third-party guides teach this: Aralia's
    "Investment Thesis → Evidence → Risks → Expected Outcome → Client Fit" (VERIFIED-PRIMARY Aralia page, a
    third-party source);
  - sector ETFs;
  - one or two bond ETFs, copying Wharton's example note;
  - a Taiwan ETF or TSMC as the "Laura connection";
  - AI and big-tech names;
  - possibly an ESG screen carried over from last year's impact-led case.
- **Tools:** efficient frontier, Sharpe ratio, beta, stress tests on 2008, COVID and 2022.

### 2.2 The obvious story
- "Balance her entrepreneurial risk-taking with the certainty her promise needs."
- Metaphors from her book titles ("messy roots", "deep roots", "next chapter"), from storytelling, and from Taiwan or
  belonging.
- In the fundraising draft: an emotional paragraph about community, plus a percentile range.

### 2.3 The obvious charts (Final Report only; the IPS bans charts)
Allocation pies, a Monte Carlo fan chart, a glide-path area chart, sector bars, an efficient frontier, and WInS
performance against the S&P 500.

### 2.4 The obvious Trading Notes
- Note 1 is a near-copy of the official example: "intermediate-term Treasury ETF to reduce volatility and prepare for
  the operating commitment".
- Note 2 is a tech or AI stock.
- Note 3 is a Taiwan ETF.
- Many teams will have written short or empty notes on early trades, not knowing they must quote them "exactly as it
  appears in WInS" (R-T28).

### 2.5 Where readers will see sameness (hot-spots)
| Hot-spot | Why it will be common | Is our current plan inside it? |
|---|---|---|
| "Three buckets + glide path" | Standard goals-based advice; natural AI answer | Partly (ladder + sleeve reads like two buckets) |
| Monte Carlo "95%" | Taught in prep guides; used last season | No: we define certainty by what is bought (brief 8.6). Risk: a checklist reader may want a number (Q5) |
| p10-p90 range | Default percentile output | No: floor bought + stretch (brief 8.7) |
| Clone of Wharton's Treasury-ETF example note | The official example (R-T23, R-AN44) | Yes, unless our note names payment years and the match (Q12) |
| Book-title puns and identity metaphors | Easy "Client Knowledge" signal | Risk if we add them (Q20) |
| Taiwan ETF as "connection" | Easy tie-in | Open (brief 9: EWT keep or drop) |
| WInS return vs S&P 500 in the FR | Default benchmark | Not yet decided (Q11) |
| Treasury ladder / lock-in at 5% yields | AI tools at today's rates may suggest it (BS-10) | Yes: our core. The edge must come from evidence and client fit, not the idea alone |

### 2.6 Distinctive but correct moves (candidates, each tied to an official requirement)
1. Evaluate implementation against the promise, not the S&P 500. Case: "evaluates how that strategy was implemented"
   (R-C90); criterion: "funding reliability" (R-S26). (Q8, Q11)
2. Execute the plan's own rules inside WInS and quote them in notes. Infographic core principle: "Strategy guides every
   decision" (VERIFIED-PRIMARY). (Q6, Q9)
3. Pre-declare in the IPS the rules that will produce the FR numbers, so the FR is an application, not a redesign.
   Guide p.5. (Q10)
4. Use few holdings, each with a job, and show look-through diversification. Trading Details: "not simply to own a large
   number of securities" (R-W71). (Q13)
5. Keep the vocabulary identical across all three deliverables, in Wharton's own words (X-16; Guide p.3). (Q27)
6. Tell a true, well-evidenced learning story, including an honest AI-use record (R-W46, R-W28). (Q21, Q22)

---

## 3. How each deliverable's mechanics reward or punish approaches

| Mechanic (official) | Rewards | Punishes | Status |
|---|---|---|---|
| 3 notes quoted "exactly as it appears in WInS"; "Yes, we will verify this" (R-T28, R-T34) | Notes written well at trade time; teams that planned which trades would become notes | Teams that wrote weak notes in week 1; any edit; notes on unfilled or practice trades | VERIFIED-REPO-FILE |
| Notes must correspond to **executed** trades (R-T33) | Discipline shown by a rule-triggered trade | Discipline shown only by *not* trading (cannot be a note) (Q7) | VERIFIED-REPO-FILE; inference |
| Reflection ≤100 words, three required parts (R-T29 to R-T32) | One concrete need of Laura's per note; one trade-off | Generic "diversification"; justification by gain (R-T11) | VERIFIED-REPO-FILE |
| "supported, tested, or refined" (R-T20; Guide; infographic) | A set of notes that shows development | Three "supported" notes that look like a shopping list | VERIFIED-REPO-FILE + VERIFIED-PRIMARY |
| TN due end of Week 4, "two weeks before your IPS" (Guide p.3) | Teams with a strategy before trading | Teams whose strategy changes after Oct 23 without explanation | VERIFIED-PRIMARY |
| 50-word pitch; 500-word IPS; TNR 12, double-spaced, 2 pages; no charts, citations, footnotes or links; breach = "will not be considered" (R-I16 to R-I55) | Plain words; if-then rules; one central idea | Numbers that need a chart to believe; jargon; any format slip | VERIFIED-REPO-FILE |
| "Focus on the strategy and decision-making framework… rather than describing individual investments or presenting detailed financial calculations" (R-I23) | A rulebook | A ticker list | VERIFIED-REPO-FILE |
| "may not revise its investment strategy after the submission deadline" (R-I35) + Guide p.5 "may not redesign your strategy after observing the results" | Rules pre-declared in the IPS that later produce the FR numbers | A FR whose range or reserve method was not foreshadowed in the IPS (Q10) | VERIFIED-REPO-FILE + VERIFIED-PRIMARY |
| WInS frozen Nov 6; FR written about a frozen portfolio (R-AN36) | A FR that evaluates the frozen book against the IPS and the liability | A FR that apologises for P&L | VERIFIED-PRIMARY |
| FR rules published Nov 9; due Dec 4; last year "15-page report" (KXAN) | Pre-built components | A four-week crunch during school exams | FR rules UNKNOWN; 15 pages = secondary |
| Readers: Wharton student evaluators + Aberdeen asset managers (2026) | Clear first page; bond terms used precisely | Loose bond language ("risk-free", "matched" for a duration mix) (Q4) | VERIFIED-PRIMARY (last season) |

---

## 4. The questions (27), with reasoning

Ordering: tier 1 (WInS now + TN) first, then IPS, then FR. "Anchor" uses Phase A ids. "R-new" means the anchor is a
newly found official text quoted in full.

### Tier 1: WInS now and Trading Notes (Oct 23)

**Q1. Sameness test: if a team pastes this case into a mainstream AI tool, how much of our architecture comes back, and
which of our elements come back rarely or never?**
- Anchor: R-S24 ("clear and creative investment thesis"); R-W28 (no plagiarising "existing strategies"); BS-10.
- Reasoning: the council's claim that "most strong teams will write safe bucket + growth bucket" was never tested
  (SH-18, BS-10). At a 5.17% 10-year yield (F-001), an AI answer may well say "lock in a Treasury ladder". If so,
  lock-early is not our differentiator. The differentiators then have to be evidence, rules and fit to Laura.
- Method: 5-10 fresh prompts with the case text, no steering. Tabulate each answer's certainty definition, range
  method, reserve timing and WInS mix. Record this AI use for Works Cited (R-W46).
- Hypothesis (guess): about half will propose buying bonds only in 2030-2033. A minority will propose locking early.
  Almost none will propose a bought 2031 floor or liability-relative evaluation.
- Would change: which one or two ideas lead the pitch and the IPS's first paragraph.

**Q6. Should the three Trading Notes be chosen as one "supported", one "tested" and one "refined" decision, and does the
team need to plan now for a "tested" or "refined" trade to happen before about Oct 20?**
- Anchor: R-T20; R-C88; R-AN40; Guide p.3 (R-new): "reflect on how those decisions supported, tested, or refined your
  strategy".
- Reasoning: all three official texts repeat the same three verbs. A typical team will submit three "we bought X
  because…" notes, which show support only. A "tested" note needs something to happen, such as a band breach or a rate
  move that triggers a rule. So the trigger has to be written before the event.
- Hypothesis (guess): readers reward visible development. One note per verb is the cleanest way to show it.
- Would change: the TN selection plan (`research/blueprints/01_trading_notes_blueprint.md` section 2) and the week 2-3
  trade calendar.

**Q7. A decision not to trade cannot be a Trading Note. How do we evidence discipline-by-inaction inside the three notes,
for example not selling Treasuries as yields rose?**
- Anchor: R-T33 ("must correspond to trades executed in WInS"); R-W73; R-W88 (low turnover).
- Reasoning: the most professional behaviour for a liability hedge is to hold still. Holding still leaves no trade, so
  it leaves no quotable note. Options:
  - a small rule-driven rebalance whose note states the rule and what was deliberately not done;
  - keep a dated decision log and use it in the FR's Articulation section.
- Hypothesis (guess): write the rebalancing rule into the first note now. Later rebalance notes can then quote it.
  Inaction goes in the FR log.
- Would change: the wording of the next WInS notes; the start of a decision log today.

**Q8. Should the team start today a daily log of (a) the value of Laura's ten payments on that day's Treasury curve and
(b) the WInS hedge's value, so the FR can show that the hedge tracked the promise over the six weeks?**
- Anchor: R-C90; R-S26 ("funding reliability… under varying market outcomes"); F-001; F-105 (spot value $288,924,
  duration 10.16y); R-W76 ("your portfolio provides evidence").
- Reasoning: rates moved 38bp in September alone (F-003). A bond-heavy WInS book may show a loss that a student reader
  misreads. A chart of hedge value against the liability value shows whether the gap stayed small. That converts
  profit and loss into evidence that the strategy worked. It is also a way to show a 16-year strategy through six weeks:
  the six weeks are literally the "rates move before January 2027" risk (brief section 9).
- Data risk: the Treasury curve can be rebuilt later. WInS position-level daily values may not be recoverable, so the
  log must start now.
- Hypothesis (guess): tracking gap within about $1-4k on a roughly $289k liability (S1 twist numbers). Readers who are
  bond professionals would find this persuasive.
- Would change: a WInS-now logging task; one FR chart; a number in the FR ("the promise's cost moved $X; our hedge
  moved $Y").

**Q9. Which of the plan's future decision points can be rehearsed by a real WInS trade in six weeks, and which only in
words?**
- The decision points: January 2027 lock; the rule if rates fall; the 2028 top-up; the rebalancing band; the 2031 floor
  in a 2-year Treasury; the 2033 reserve.
- Anchor: seed 30; R-C75 ("implementation of its investment strategy"); R-I12; R-W69 (individual Treasuries allowed);
  infographic "Strategy guides every decision" (R-new).
- Reasoning: the $150k deposit never enters WInS (R-W59), so the 2028 top-up cannot be rehearsed. A 2-year Treasury
  bought for the floor can be, and so can a band rebalance. Each rehearsal must earn its complexity; the design
  principle says one clear rehearsal beats five token ones.
- Hypothesis (guess): two rehearsals are worth doing (the lock and the floor purchase). The rest go in words in the IPS
  and FR.
- Would change: the WInS trade list; which trades become notes.

**Q12. The official example note is a Treasury ETF bought for the operating commitment, and hundreds of teams will clone
it. What must our Treasury note contain so that a reader who has seen many clones recognises ours as different?**
- Anchor: R-T23; R-AN44; R-T28 (quoted verbatim, so the note text is permanent).
- Reasoning: note text written now is frozen. It is also the reader's first impression, because the TN is the first
  deliverable.
- Hypothesis (guess). Elements (not wording):
  - which payment years it protects;
  - how its sensitivity to rates compares with the promise's;
  - the rule it follows;
  - one honest limit (for example, "moves like the payments, but is not a date-by-date match").
- Would change: the text of the next Treasury trade's WInS note.

**Q27. Should every WInS note name its role using Wharton's own words ("growth, liquidity, risk management, or future
funding") and the same labels the IPS and FR will use, so the reader's cross-check is effortless?**
- Anchor: X-16 (shared vocabulary); R-C92 ("clear and consistent investment strategy across all three"); Guide p.3
  (R-new): the note should capture its "expected role in growth, liquidity, risk management, or future funding".
- Reasoning: readers compare the deliverables. Identical labels (for example one fixed name each for the promise
  holdings, the growth sleeve and the floor) make consistency visible at a glance. Labels that drift ("hedge", "safe
  bucket", "reserve", "ladder") look like three strategies.
- Hypothesis (guess): yes. Choose three labels now and never vary them.
- Would change: every note from today; a glossary line in the FR.

**Q25. What is the "required trading activity" in the Rules, and could a low-turnover, few-holding portfolio fail an
unpublished eligibility gate?**
- Anchor: R-W23 / F-608 ("Teams must meet the required trading activity and portfolio management guidelines");
  R-W33; X-18.
- Reasoning: pre-mortem item. A correct strategy is worthless if the team becomes ineligible. Earlier seasons had a
  first-trade deadline ([PRIOR], A4 b3). The logged-in Trading Details page may set a minimum.
- Hypothesis (guess): at most a first-trade-by date. Still unverified.
- Would change: a WInS-now check today; possibly the timing of the first trade.

**Q28. Which dated market events fall between Sept 28 and Oct 20 and could fire a pre-written rule, so that a "tested"
note can exist before the Oct 23 deadline?**
- Examples: U.S. CPI release, Treasury auctions, a band breach. The next FOMC meeting is probably Oct 27-28, after the
  TN deadline but before the IPS (UNVERIFIED; D1 to check on federalreserve.gov).
- Anchor: R-T8; R-T13; Guide p.3.
- Reasoning: the calendar decides whether a test can happen in time. If nothing fires, the team needs a fallback
  "refined" note, for example switching IEF+TLT to IEF+TLH after checking durations (S1).
- Hypothesis (guess): a rate or equity band trigger is more likely to fire in three weeks than any macro event.
- Would change: the trigger thresholds written into the first notes.

### Tier 2: IPS (Nov 6)

**Q10. Which decision rules must the IPS pre-declare, so that the FR's reserve size, 2031 range and facility share read as
"applications" of the IPS, not as a "redesign after observing the results"?**
- Anchor: R-I32; R-I35; X-5; Guide p.5 (R-new): "it should not be rewritten simply because markets move or hindsight
  reveals a different outcome. You may identify decisions you would make differently, but you may not redesign your
  strategy after observing the results."
- Reasoning: the FR numbers will be computed after Nov 6. If the IPS never mentions a bought 2031 floor or a
  liability-first reserve rule, the FR's range looks new. The IPS has 500 words, so every pre-declared rule costs
  words.
- Hypothesis (guess): four rules are enough:
  - the promise is priced and bought first;
  - risk is taken only in the surplus, within a stated band;
  - the 2031 statement is a bought floor plus a stated stretch;
  - the facility contribution is a share of what is left after the reserve, with a flexibility margin.

  Each needs roughly 30-50 words.
- Would change: the IPS word budget and outline.

**Q18. With no charts or citations, what must the IPS words alone prove, and which (if any) numbers survive?**
- Anchor: seed 14; R-I55; R-I23; R-AN38; R-I6 ("desired degree of funding certainty").
- Reasoning: the reader cannot check a source in the IPS. So any number must be believable on its face or carry its
  own method in a clause. If-then rules can be checked later against the WInS record and the FR. Prior guidance says
  "at most one rounded number" (SH-16). The new point is that the IPS is the anchor the FR is audited against (Q10).
- Hypothesis (guess): the IPS proves three things in words:
  - the priority order (promise before facility);
  - the certainty definition in plain English;
  - the rules for change as dates approach.

  One number, the promise's cost against the first deposit, is worth its words.
- Would change: the IPS outline and number policy.

**Q19. In 50 words, most pitches will say "balance growth and security". What is the one claim only our strategy can make
truthfully, and does it need a clause specific to Laura to avoid being generic?**
- Anchor: R-I16, R-I17 ("central idea… how it is designed to support your client's financial goals"); R-S24
  ("creative investment thesis"); North Star.
- Reasoning: the pitch is the first thing a screening reader sees on page 2. Sameness is most visible there.
- Hypothesis (guess): the distinctive, true claim is about when certainty is achieved (bought at the start, not hoped
  for at the end). The Laura clause should tie to her stated wish for "an appropriate balance". Book-title imagery
  should not stand in for it (Q20).
- Would change: the pitch content specification (not its wording).

**Q16. Will a reader see about 20% total equity after 2028 (F-409) as ignoring Laura's "thoughtful risks", and does the
IPS need one explicit sentence saying where her risk appetite lives?**
- Anchor: R-C37, R-C38, R-AN16; R-S25 ("risk considerations"); F-409; brief section 9 (equity weight open).
- Reasoning: this is a "correct strategy misses the Top 50" risk. A student evaluator skimming a WInS book that is
  about two-thirds Treasuries may score "creative thesis" and "diversification" low. The case's "Although…" wording
  supports protection, but only if the IPS says so explicitly.
- Hypothesis (guess): one sentence is enough. It should say that all risk-taking sits in the money the promise does
  not need, and that the extra equity there "buys range, not median" (brief 8.5).
- Would change: one IPS sentence; possibly the sleeve equity weight if Phase D finds readers penalise low equity.

**Q17. Which word counter will Wharton use for the 50/500/100-word limits, and what internal caps protect us from a
counting dispute?**
- Anchor: R-I16, R-I18, R-I39 ("will not be considered for semifinal selection"); R-T29; R-T36 (does the quoted note
  count toward 100?).
- Reasoning: numbers ("$292,264"), year ranges ("2033-2042"), hyphenated words and headings count differently in
  different tools. A breach disqualifies. Nobody publishes the counting rule.
- Hypothesis (guess): Wharton will use a word-processor count. An internal cap of about 475 words (IPS), 46 words
  (pitch) and 95 words (reflection) is a cheap margin (ASSUMPTION).
- Would change: the internal caps and a pre-submission checklist line.

**Q5. Last season's strong teams reported Monte Carlo probabilities, and readers rewarded them. Will this season's
readers expect a probability when the case says "explain how they evaluated that level of certainty", and should a
number sit beside our model-free definition?**
- Anchor: R-C54, R-C55; R-AN1; R-AN32; brief 8.6 (model-free certainty).
- What is new against brief 8.6: evidence of reader behaviour, which is not a modelling argument. A 2025-26
  semifinalist's headline was "a 70% chance" (VERIFIED-PRIMARY, KXAN via Yahoo). Readers may use a checklist in which
  "a stated confidence level" is a box.
- Hypothesis (guess): keep the model-free definition as the definition. Add one evaluated number that a checklist
  reader can tick, for example the share of payment dollars matched by bonds held to maturity, or zero misses across
  all simulated paths labelled "by construction". Do not add a 95% forecast.
- Would change: one IPS sentence ("desired degree of funding certainty", R-I6); the FR certainty section.

### Tier 3: Final Report (Dec 4; instructions Nov 9)

**Q2. The rubric moved from "visually pleasing presentation of data; many creative elements" (2023-24, third-party
transcription) to "uses data effectively to support conclusions; demonstrates original thinking" (2026-27). Should our
FR use a few analytic charts, each carrying a conclusion, instead of many decorative ones?**
- Anchor: R-S28; R-S24; Lumiere 2023-24 transcription (SNIPPET-UNVERIFIED as Wharton's text).
- Reasoning: rubric deltas show designer intent more reliably than the rubric's absolute words.
- Hypothesis (guess): yes. About 4-6 charts, each with a one-line takeaway. Candidates: liability against hedge (Q8);
  surplus range; the bought 2031 floor against the stretch; the effect of the 2028-deposit risk.
- Would change: the FR chart plan and page budget.

**Q3. Who reads first, and what is the screening surface?**
- Anchor: F-611; R-W8; R-W24; 2026 news (R-new): "with the help of our Wharton School student evaluators, as well as a
  professional review panel of asset managers from Aberdeen Investments in Philadelphia"; 2025 news (R-new): "internal
  reviewers and a group of professional asset managers from abrdn".
- Reasoning: about 2,300 reports go to a small panel. If Wharton students screen first, the pitch, the FR's first page
  and the section headings do most of the work. The reading order is not published.
- Hypothesis (guess):
  - two stages, students first, then professionals on a shortlist;
  - the FR's first page should answer the case's must-list in order: reserve size, composition, certainty,
    facility, range with confidence, fundraising draft.
- Would change: FR page 1 and heading structure.

**Q4. If an Aberdeen fixed-income professional reads our work, which bond statements would lose credibility, and which
would gain it?**
- Loses: "risk-free"; "matched" used for a duration-only ETF mix; ignoring reinvestment; confusing par and zero yields.
- Gains: a real ladder of Treasury STRIPS; a stated tracking gap; nominal-only certainty with its caveats.
- Anchor: R-new (Aberdeen review panel); F-610 (finale judge "U.S. Credit Investment Manager", VERIFIED-PRIMARY);
  brief 8.11, 8.13.
- Reasoning: a specialist reader turns small wording errors into large credibility losses, and turns precise wording
  into a signal of real understanding (criterion "Portfolio Analysis").
- Hypothesis (guess): use precise words ("duration-matched, not cash-flow-matched"). Show the twist gap honestly.
- Would change: sentences in the TN, IPS and FR; a bond-terms checklist for D9.

**Q11. What benchmark should the FR use to evaluate implementation: WInS return against the S&P 500 (what most teams will
do), or funded status and hedge tracking against Laura's promise, plus an audit of whether we followed our own IPS
rules?**
- Anchor: R-C90 ("evaluates how that strategy was implemented"); R-I37; R-W75 (not judged on outperforming); Guide p.4
  "Evaluate your implementation".
- Reasoning: benchmarking against equities makes a liability-first plan look like a loser for the wrong reason. A
  rule-compliance audit ("we set N rules; we followed N; here is the one we broke and why") is rare and fits the
  Articulation criterion.
- Hypothesis (guess): make the primary metric liability-relative. Give the S&P comparison one line with the reason it
  is not the test.
- Would change: FR section structure and charts.

**Q13. How do we show "appropriate diversification" and "understanding of the investments" with a WInS book of 3-6
positions, when rivals hold 20-40?**
- Anchor: R-S24 ("uses appropriate diversification"); R-W70, R-W71 ("not simply to own a large number of securities";
  "funding purposes"); R-AN45; F-409.
- Reasoning: a skimming reader may equate the number of holdings with diversification. Look-through facts (companies,
  countries and bond maturities inside each fund) and the "funding purposes" wording, which is Wharton's own, answer
  that. In the FR, the rule can be quoted; in the IPS it can only be paraphrased.
- Hypothesis (guess): one FR table of look-through counts, with a column naming each position's job.
- Would change: an FR table; the growth-note reflection wording.

**Q14. Should the team pre-build FR components before Nov 9, assuming a page cap near last year's 15 pages?**
- Components: the liability chart, the surplus distribution, the 2031 floor table, the fundraising-draft elements, and
  the assumptions list including inflation's effect on facility costs.
- Anchor: R-C93; R-S19; KXAN (2025-26 "required 15-page report", VERIFIED-PRIMARY article, secondary on the rule); a
  search summary citing "7–11 pages, double-spaced" (SNIPPET-UNVERIFIED, older season).
- Reasoning: instructions arrive with only 25 days left. A page cap forces triage. Pre-built parts reduce the crunch,
  which is the pre-mortem's most likely execution failure.
- Hypothesis (guess): yes. Build parts so they can be cut to 10 or 15 pages.
- Would change: the team's October-November work plan.

**Q15. Pre-mortem (seed 31): if we miss the Top 50 with a correct strategy, which single cause is most likely, and what
dated countermeasure prevents it?**
- Anchor: R-I39; R-C92; R-W43; R-AN60; F-609.
- Candidates (my ranking, ASSUMPTION):
  1. The report reads as "too conservative / only bonds" to a skimming reader (Q16, Q13).
  2. Jargon or "fancy terms and formulas". The judge's exact warning, VERIFIED-PRIMARY: "hiding behind fancy terms and
     formulas".
  3. FR crunch after Nov 9 (Q14).
  4. Visible inconsistency between week-1 notes, the IPS and the frozen WInS book (Q27, Q10).
  5. Missing one of the case's must-items (for example, inflation's effect on facility costs, R-C85).
  6. An IPS format breach (Q17).
  7. A voice that sounds like AI (R-W49).
  8. Client research about the wrong "Laura Gao" (Q23).
- Hypothesis (guess): #1 and #2 together are the largest risk, because they hit the screening reader.
- Would change: the team's risk checklist and deadlines.

**Q20. Book-title puns and identity metaphors will be common. Will readers, and Laura, read them as tokenism? What is the
most our deliverables should use?**
- Anchor: R-C10, R-C16; brief 4 (identity never as decoration); R-S28 ("authentic team voice"); seed 34.
- Reasoning: sameness plus risk. A reader who has seen 50 "messy roots" portfolios discounts the 51st. Laura's public
  work is about identity, which is exactly why decoration can offend.
- Hypothesis (guess): zero puns. At most one functional reference, tied to a decision rather than to decoration.
- Would change: a style rule for all three deliverables.

**Q21. Should the FR's Articulation section tell the true story of a past-season rule violation and the compliance
routine built in response?**
- Anchor: R-S27 ("reflects meaningfully on the team's growth and response to challenges"); R-W28 (no invented
  stories); v4 Part 2 lessons.
- Reasoning: true, specific failure-and-response stories are rare and authentic. The risk is that a reader focuses on
  the violation. Only part of the team was involved last season, so the story must be told accurately.
- Hypothesis (guess): one short, factual mention helps if it is linked to a verifiable routine (the pre-trade
  checklist) and the team agrees to include it.
- Would change: an FR Articulation sentence (a team decision).

**Q22. Could a detailed, honest AI-use record become an Articulation strength rather than a risk?**
- The record would say what AI did (brainstorming, checking), what the students decided, and what they redid by hand.
- Anchor: R-W46 ("how you use it must be recorded in your Works Cited pages"); R-W49; R-W51; X-9.
- Reasoning: many teams will under-disclose. Readers who suspect AI voice may discount a whole report. A specific
  record builds trust in the student voice. That fits "Did I come to my current conclusion before or after using
  generative AI tools?" (R-W51).
- Hypothesis (guess): yes, if concise (for example a half-page Works Cited subsection) and backed by a decision log.
- Would change: the FR Works Cited design; a logging habit starting now.

**Q23. Every external fact about Laura must trace to the case's Laura. Do all team sources match the case identifiers
(Wharton 2018, Statistics & Information Decisions Management, author of *The Wuhan I Know* and *Messy Roots*)?**
- Anchor: R-C10, R-C12, R-C13; R-W4 (the scenario is invented); brief 13.
- Reasoning: a web search for her name returns other people with the same name, including a different student profile
  linked to Penn (search results, 2026-09-27; not opened, not recorded, for privacy). One misattributed fact in
  "Client Knowledge" is the kind of error a reader never forgives.
- Hypothesis (guess): the team docs already contain unverified claims (brief section 1). A source-match check is
  cheap.
- Would change: a verification step before any external Laura fact enters a deliverable.

**Q24. Which pricing date should the IPS and FR numbers use, since rates will have moved by the time they are read
(Dec-Jan)?**
- Candidates: the Sept 25 curve, the Nov 6 freeze date, or the latest curve before Dec 4.
- Anchor: F-001, F-002, F-111 (the ladder was above $300k on 173 of 185 days in 2026); R-C77.
- Reasoning: "fits inside $300k" is a September 2026 fact (F-111). If rates fall 30bp before Nov 6, an IPS claim built
  on Sept 25 is wrong on the day it is submitted. A dated number with its rule ("if the cost exceeds the deposit, then
  …") survives either way.
- Hypothesis (guess): state the rule, not the number, in the IPS. Re-price in the FR on the freeze date and show the
  six-week path (Q8).
- Would change: the IPS number policy and the FR's valuation date.

**Q26. Where will readers look for the three-deliverables-together check, and what single table would let a reader verify
consistency in one minute?**
- A candidate table: rule in the IPS → WInS trade that applied it → note quoted → FR evaluation.
- Anchor: R-C91, R-C92; R-S24 ("maintains consistency with the team's IPS"); infographic (R-new): "Strong submissions
  connect the client's goals, research, portfolio decisions, and final recommendations through one clear and cohesive
  investment strategy."
- Reasoning: readers are told to consider the deliverables together but get no tool for it. Giving them one is
  distinctive and low-complexity.
- Hypothesis (guess): one FR table of about 6 rows replaces pages of narrative on consistency.
- Would change: one FR table (and it disciplines the notes now).

---

## 5. Evidence found this pass (all accessed 2026-09-27)

### 5.1 New official 2026-27 documents (VERIFIED-PRIMARY; not in repo)
- **Investment Competition Guide 2026-2027**, 5 pages.
  - URL: https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf, linked from
    https://wghsinvcomp.smapply.us/res/p/guide/.
  - PDF created 2026-09-09 (InDesign 21.4). SHA-256 3638e846…51fb7add (full hash in section 6).
  - Key text (exact):
    - p.2: "Your team will need to consider the client's goals, time horizons, required cash flows, funding
      commitments, liquidity needs, desired degree of funding certainty, risk tolerance, and communication with
      potential co-sponsors."
    - p.2: "The goal is not simply to identify investments you think will perform well. The goal is to develop a
      cohesive strategy in which your investment decisions work together to support the client's objectives across a
      range of possible market outcomes."
    - p.2: "Your research, analysis, Trading Notes, and experience implementing your strategy should all contribute to
      the IPS."
    - p.3: "When your team executes a trade in WInS, the Trading Note should capture the reasoning behind the decision,
      including its alignment with your strategy, the supporting research or analysis, and its expected role in
      growth, liquidity, risk management, or future funding."
    - p.3: "The Trading Notes Analysis is due at the end of Week 4 (October 23), two weeks before your IPS is due."
    - p.3: "Do not treat Trading Notes as an afterthought. They provide a record of how your team put its strategy into
      practice."
    - p.4: "The competition deliverables are not separate assignments. Together, they show how your team developed,
      implemented, articulated, and evaluated its investment strategy."
    - p.5: "A long-term strategy may include planned adjustments as funding dates approach, but it should not be
      rewritten simply because markets move or hindsight reveals a different outcome."
    - p.5: "You may identify decisions you would make differently, but you may not redesign your strategy after
      observing the results."
    - p.5: "The competition recognizes thoughtful strategy, research and analysis, client understanding, disciplined
      decisions, management of risk and uncertainty, communication, and creativity."
    - p.5: "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and
      tradeoffs behind those decisions."
- **Competition Phases infographic**, 1 page.
  - URL: https://upenn.box.com/s/l2p0l26svbbptmcizhmswyq5f7rbyp44. PDF created 2026-09-14.
  - Key text: "CORE PRINCIPLE Strategy guides every decision."; "ONE STRATEGY CONNECTS THE COMPETITION"; "Strong
    submissions connect the client's goals, research, portfolio decisions, and final recommendations through one clear
    and cohesive investment strategy."; "There is no single correct strategy. Strong teams explain the reasoning,
    assumptions, and tradeoffs behind their decisions."

### 5.2 Readers and judges (VERIFIED-PRIMARY)
- 2026 Top 50 article (Jan 27, 2026):
  - "with the help of our Wharton School student evaluators, as well as a professional review panel of asset managers
    from Aberdeen Investments in Philadelphia".
  - "Teams that competed at least through the mid-term report submissions will receive a participation badge".
  - https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/
- 2025 Top 50 article (Jan 30, 2025): "After careful consideration by our internal reviewers and a group of professional
  asset managers from abrdn in Philadelphia".
  https://globalyouth.wharton.upenn.edu/news/announcing-the-semifinalists-in-the-2025-wharton-global-high-school-investment-competition/
- 2025 finalists article (published about March 2025; the text dates the semifinals to the week of March 17, 2025).
  Melissa Ko Hahn, semifinal judge:
  - "A lot of work went into putting your written reports and the videos together, and it clearly came across,"
  - "Overall, one of the tendencies of people who are just starting out is to fall into this trap of hiding behind
    fancy terms and formulas. I would encourage you to fight against that. Oftentimes, the best solutions are made up
    of simple, elegant ideas."

  Checked with `--grep`. This upgrades the winners.md paraphrase to VERIFIED-PRIMARY.
  https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/
- 2025 champions article. Chirag Jain, then "U.S. credit research analyst at Aberdeen Standard Investments": "What
  distinguished managers was clear thoughtfulness and reasoning behind all the decisions that they put together."
  (Context: finale, not semifinal; used here only as a signal of the Aberdeen reviewers' values.)
  https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/
- 2026 champions article (Apr 30, 2026): finale judges included "Chirag Jain, U.S. Credit Investment Manager, Aberdeen
  Investments".
  https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/
- 2026 finalists article (Mar 20, 2026): "49 semifinalist teams advanced to the virtual semifinal rounds, where they
  presented their strategies to panels of Wharton alumni and industry experts." Note 49, not 50.
  https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/
- Rules page: "The Global Champion school will be permitted to fast-track one team to the semifinal round of the
  2027-2028 competition." (This season's text. By the same practice the 2026 champion school fast-tracks one team in
  2026-27; INTERPRETATION.) https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/

### 5.3 What past winners and semifinalists did (written work)
- Vandegrift ("The Compounders", 2026 semifinalist). KXAN article mirrored on Yahoo, read on the page (VERIFIED-PRIMARY
  for the article; the team's claims are self-reported):
  - "built a four-part screening system that focused on U.S.-traded securities, high-growth potential, low volatility,
    and alignment with the non-profit's mission";
  - "ran their portfolio through thousands of Monte Carlo simulations and stress-tested it against historic downturns,
    including the dot-com crash, the 2008 recession and COVID-19 market conditions";
  - "Their model showed a 70% chance of reaching the long-term goal";
  - "All four worked together on the required 15-page report."
  - https://www.yahoo.com/news/articles/female-vandergrift-team-advances-wharton-174003734.html (the KXAN original
    returned 403)
- Harvard-Westlake Chronicle (VERIFIED-PRIMARY article):
  - advisor Rob Levin on the 2025-26 case: "His goal was to invest money for ongoing community recreation programs and
    long-term facilities construction."
  - a student: "I formulated the idea for our strategy and programmed our model."
  - Last season's case also paired ongoing operations with a facility, so returning teams and AI tools carry templates
    for this structure.
  - https://hwchronicle.com/112806/news/students-compete-in-yearly-wharton-stock-competition/
- 2023 "tales" article (VERIFIED-PRIMARY):
  - Brian Z, DMV's Finest (2022-23 champions): "less is more, and having an explainable strategy makes a lot more
    sense than going for so many different things at once."
  - Alex Lamon: "Remember, winning isn't about portfolio gains. It is about having a coherent strategy."
  - https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/
- Wharton "developing strategy" page (undated legacy page, VERIFIED-PRIMARY): "if you provide us with a team strategy
  that is buried somewhere in your experience, rather than clearly stated, defined and articulated up front, you will
  not be among the strongest teams." https://globalyouth.wharton.upenn.edu/developing-strategy/
- 2025 finale: teams showed "sentiment, SWOT and Pestel analyses, customized algorithms, AI innovations, portfolio
  optimizations, performance and readiness indices" (VERIFIED-PRIMARY, BAM article). This is finale content, used only
  as a picture of the field's toolkit.
- Posted past reports (Scribd "Wharton Competition - Final Report", "Mid-Term Report", "Final Report template";
  SlideShare "Wharton final report") could not be read: the sites need JavaScript. Status: NOT READ.

### 5.4 Rubric history
- Lumiere Education (third party, page published for 2023-24, read directly) quotes the then-current criteria, for
  example:
  - "Creativity and presentation: compelling narrative and visually pleasing presentation of data; many creative
    elements; clearly presented with an authentic team voice."
  - "Client knowledge and objectives: strategy is tailored uniquely to the client's financial goals; would win him/her
    over as a client."

  Status: VERIFIED-PRIMARY as Lumiere's text; SNIPPET-UNVERIFIED as Wharton's wording (the Wayback Machine was
  unreachable).
  https://www.lumiere-education.com/post/wharton-global-youth-program-s-investment-competition-a-comprehensive-guide
- 2025-26 schedule (Scribd "25-26 Week One Email", search summary only): mid-term report due Oct 31, final report due
  Dec 12, first trade by Oct 10, roster Oct 17. SNIPPET-UNVERIFIED.

### 5.5 Field arithmetic (DERIVED)
- 2025-26: 2,339 finishers (F-609). With one fast-track seat, about 49 open seats, about 2.1%.
- School overlap: 7 schools appear in both the 2025 and the 2026 Top 50 lists (Amity International, Deerfield, Nový
  PORG, Lycée Français de Chicago, Richard Montgomery, Stuyvesant, Western Canada HS). They account for about 9 of the
  2026 Top 50 teams. My parser matched 49 of the 50 2026 lines, so treat the count as approximate.
- 27 of the parsed 2026 lines are U.S. schools. There are 0 Australian schools in either list.
- The 2025 list includes one Taiwanese school (Kang Chiao International School).

---

## 6. Sources (all accessed 2026-09-27; status as marked)

| Source | URL | Status |
|---|---|---|
| Investment Competition Guide 2026-27 (5 pp) | https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf; SHA-256 3638e84692ed0d826660a65e89cad0ce7eea8c1907b6a8f00ce02c0d51fb7add | VERIFIED-PRIMARY |
| Competition Phases infographic (1 p) | https://upenn.box.com/s/l2p0l26svbbptmcizhmswyq5f7rbyp44; SHA-256 2827f92a989d6d72fbc253d80d975eb06bd00c86f631e83850ae17eec544ed10 | VERIFIED-PRIMARY |
| SMApply Guide page | https://wghsinvcomp.smapply.us/res/p/guide/ | VERIFIED-PRIMARY |
| 2026 Top 50 article | https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/ | VERIFIED-PRIMARY |
| 2025 Top 50 article | https://globalyouth.wharton.upenn.edu/news/announcing-the-semifinalists-in-the-2025-wharton-global-high-school-investment-competition/ | VERIFIED-PRIMARY |
| 2025 top-10 article (Hahn quote) | https://globalyouth.wharton.upenn.edu/news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/ | VERIFIED-PRIMARY |
| 2025 champions article | https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/ | VERIFIED-PRIMARY |
| 2026 finalists article | https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/ | VERIFIED-PRIMARY |
| 2026 champions article | https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/ | VERIFIED-PRIMARY |
| Rules & Roles | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ | VERIFIED-PRIMARY |
| Developing strategy page | https://globalyouth.wharton.upenn.edu/developing-strategy/ | VERIFIED-PRIMARY (undated) |
| 2023 tales article | https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/ | VERIFIED-PRIMARY |
| KXAN/Yahoo Vandegrift article | https://www.yahoo.com/news/articles/female-vandergrift-team-advances-wharton-174003734.html | VERIFIED-PRIMARY (article); team claims self-reported |
| Harvard-Westlake Chronicle | https://hwchronicle.com/112806/news/students-compete-in-yearly-wharton-stock-competition/ | VERIFIED-PRIMARY (article) |
| Stuyvesant blog (FigCapital) | https://talos.stuy.edu/cms/pages/stuyvesant-blog/stuyvesant-high-school-wins-the-2026-wharton-global-high-school-investment-competition-26/ | VERIFIED-PRIMARY; no strategy detail |
| Aralia 2026-27 guide (third party) | https://www.aralia.com/helpful-information/guide-to-the-wharton-global-high-school-investment-competition/ | VERIFIED-PRIMARY as third-party text |
| Lumiere 2023-24 guide (third party) | https://www.lumiere-education.com/post/wharton-global-youth-program-s-investment-competition-a-comprehensive-guide | VERIFIED-PRIMARY as third-party text; Wharton wording SNIPPET-UNVERIFIED |
| Scribd 25-26 week-one email; mid-term report; final report template; SlideShare final report | scribd.com/document/934687491, /842933720, /820640088, /942363888; slideshare.net/slideshow/wharton-final-report/262037395 | NOT READ (JavaScript wall); summaries SNIPPET-UNVERIFIED |
| Web search summary "7–11 page Final Report, double-spaced" | search result, 2026-09-27 | SNIPPET-UNVERIFIED (older season) |
| Wayback Machine | web.archive.org | BLOCKED (connection reset) |
| KXAN original | kxan.com | REFUSED (HTTP 403) |

Repo files used: the official case, IPS guide, Trading Notes guide and SMApply page; the Phase A files
(`case_register.md`, `fact_register.md`, `stakeholder_map.md`, `wins_week1_guardrails.md`); `02_judge_panel.md`;
`groundwork/winners.md`; `01_trading_notes_blueprint.md`; `wins_now/securities_and_allocation_v0.md`;
`wins_now/S1_treasury_sleeve.md`.

---

## 7. Leads for the specialists

- **D10 / main loop:** add the two new official PDFs (section 6 hashes) to `competition/official/2026_27/` and
  `manifest.yaml`, and register their text as new R-ids. Several of my anchors are "R-new" because of them.
- **D10:** the logged-in "Trading Details" and Session Rules pages are needed for Q25 ("required trading activity") and
  for the note character limit. Also check the SMApply TN form for word-count enforcement and whether the quoted note
  counts toward the 100 words (Q17).
- **D7:**
  - The 2026 reader panel is not yet announced. Watch the SMApply updates.
  - Past reports on Scribd and SlideShare need a human with a browser to read (team members can open them). Priority:
    "Wharton Competition - Final Report" (document 942363888), which is likely 2025-26.
  - Compare 2024-25 and 2025-26 semifinalist news items (school papers) for any description of written reports.
- **D1:** confirm the Oct 2026 FOMC dates and the CPI and Treasury auction calendar for Sept 28 to Oct 20 (Q28).
  Draft the precise bond-wording checklist for a credit-professional reader (Q4).
- **D3:** build the daily "promise value vs WInS hedge" log. The inputs are the Treasury curve CSV (daily) and WInS
  position values (manual daily capture). Report the tracking gap (Q8, Q24).
- **D9:**
  - the sameness test protocol (Q1), with the AI use recorded for Works Cited;
  - the fixed three-label vocabulary (Q27);
  - pitch and IPS content specifications (Q18, Q19);
  - a no-pun style rule (Q20).
- **D6:** whether ~20% total equity reads as ignoring "thoughtful risks" (Q16). Any evidence on how readers see
  conservative plans.
- **D5:** none from this lens beyond the Q3 note that readers include asset managers, not philanthropy specialists.
- **Source-match check (Q23):** every external Laura fact must match the case identifiers. Do not record other people's
  details.

---

## 8. Parked (logged, not pursued)

- Team names that reference the client: several 2026 semifinalists and 2 of 11 finalists had names referencing the
  client's NFL career. Correlation only, and the roster name is set by Oct 9. Parked.
- Finale presentation format, judge Q&A: out of scope (semifinals only).
- Spelling (Australian vs U.S.): the case uses U.S. spelling; a minor style choice for D9, not a question.

---

## What this teaches

- **Before trying to be different, write down what "normal" looks like.** Only then can you see where readers will be
  bored (a Monte Carlo "95%", book-title puns, a copy of the official example) and where they will stop and read.
- **The rules of a deliverable are part of the strategy.** A Trading Note is frozen when you type it. It must come from a
  trade that actually executed. A decision not to trade can never be one. The IPS cannot show a chart. The Final Report
  cannot "redesign" after results. Each rule changes what you should do today, not just what you write later.
- **Know your reader.** Last year the written reports were screened with help from Wharton students and read by
  professional asset managers, including bond specialists. Simple, precise words beat "fancy terms and formulas". The
  winning 2022-23 team's own lesson was "less is more".
- **Look for the missing documents.** Two official guides were sitting one click away on a public page, and nobody had
  read them. Checking every link on an official page is cheap, and it can change the whole plan.
