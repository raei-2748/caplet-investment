# Ultracode prompt v4: "Leave nothing unconsidered" (for a NEW session; Ray approves before launch)

How to use: start a new Claude Code session on branch `claude/zealous-turing-l19aqc` (or after merging it to main).
If possible, first allow primary domains in the environment's network settings (home.treasury.gov,
fred.stlouisfed.org, www.ishares.com, am.jpmorgan.com, globalyouth.wharton.upenn.edu, magazine.wharton.upenn.edu,
lauragao.com, en.wikipedia.org). Paste everything below the line, then paste the team's two client documents
("Why Wharton chose Laura" and "Client Profile: Laura Gao"), which are deliberately not stored in the public repo.

---

ultracode

# PART 1: CONTEXT (read fully; also read CLAUDE.md, which is the project memory)

## Who we are and what we want
Team Caplet: six high-school students (Ray, team leader; Ahaan; Darren; Harry; Eric; Young) in the 2026-27 Wharton
Global High School Investment Competition. Priority: reach the Top 50 semifinals, which are chosen on our written
deliverables. Today is late September 2026; WInS trading started Sept 28.

## Official deadlines (5:00 p.m. ET, no extensions; submitted via SurveyMonkey Apply)
- Oct 9: team roster (members locked afterwards).
- Oct 23: Trading Notes Analysis: 3 notes quoted exactly from executed WInS trades, each with a reflection of 100
  words or fewer (why; fit with strategy; how it serves Laura's goals, funding needs or risk).
- Nov 6: Investment Policy Statement: title page, 50-word elevator pitch, 500-word IPS; Times New Roman 12,
  double-spaced, 1-inch margins; no charts, images, links, footnotes or citations; non-compliance = not considered
  for semifinals. TRADING ENDS AND THE PORTFOLIO LOCKS; the strategy may not be revised after this.
- Nov 9: Final Report instructions released. Dec 4: Final Report + official school documentation.
- Evaluation criteria (all three deliverables judged together): Investment Strategy; Client Knowledge and Objectives;
  Portfolio Analysis; Articulation of Competition Experience; Creativity and Presentation (including clear, credible
  communication of Laura's potential facility contribution and uncertainty to prospective co-sponsors).

## The client (official case: competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt; the case wins over
## any other source)
- Laura Gao, Wharton 2018 (Statistics & Information Decisions Management), former tech product manager, author of
  "The Wuhan I Know" (2020) and the graphic memoir "Messy Roots"; bestselling author, illustrator, entrepreneur,
  educator. Born in Wuhan, raised in Texas. Quote: "The only person who needs to believe in something is yourself."
- Framing: we are young analysts at an asset management firm; our portfolio manager (the team's teacher/advisor)
  makes final investment decisions; we hope to develop "the investment strategy that Laura ultimately chooses".
- Money in: $300,000 at the start of 2027 (Year 1); $150,000 at the start of 2028 from publishing advances, speaking,
  licensing and other ventures. No other additions or withdrawals before 2033. Living costs are covered outside the
  portfolio. Year number = calendar year - 2026; all flows at the beginning of the year.
- Operating commitment: ten fixed $50,000 payments (not inflation-adjusted) at the start of each year 2033-2042 to a
  collaborative creative residency she establishes in Taiwan in 2033. Must be funded by the portfolio alone with "a
  high degree of certainty". Start of 2033: set aside an operating reserve BEFORE the first payment or any facility
  contribution. Teams recommend its size, initial composition and how it changes; define "high degree of funding
  certainty", how it was evaluated, and the assumptions.
- Facility contribution: no preset amount; recommend and justify what she can responsibly contribute after the
  reserve, preserving financial flexibility. Teams need not size a separate contingency fund or estimate facility cost.
- Co-sponsors: in 2031 she communicates a dollar RANGE for her 2033 contribution and how confident the team is;
  overpromising damages her credibility; the range must protect the operating commitment. Teams draft part of her
  fundraising materials. Co-sponsors may fund the facility but not the operating commitment.
- Laura is willing to take thoughtful risks and wants a recommended balance between growth and protecting the capital
  her goals require. WInS gains/losses are NOT added to projections. Taxes and Taiwan legal/regulatory issues are out
  of scope. Funding beyond 2042 is out of scope.

## Verified numbers (primary files in competition/official_market_data/; scripts in research/verified_2026-09-27/)
- Treasury par curve 2026-09-25: 1y 4.50, 2y 4.81, 3y 4.94, 5y 4.98, 7y 5.06, 10y 5.17, 20y 5.54, 30y 5.49.
- Ten payments valued at 2027-01-01: $292,264; each 0.01% rate move ~ $289; duration 9.90 years; cushion under the
  $300k deposit $7.7k (~0.27%).
- IEF duration 6.95y, TLT 15.31y (fact sheets 2026-06-30) -> 64.8% / 35.2% matches the payments' duration.
- JPM 2026 LTCMA (data 2025-09-30): U.S. large cap 6.70% compound (7.94% arithmetic, 16.47% vol); AC World 7.00%;
  EAFE 7.50%; U.S. intermediate Treasuries 4.00%; long Treasuries 4.90%; cash 3.10%; inflation 2.50%; correlation
  U.S. large cap vs intermediate Treasuries -0.01.
- Simulation (strategy_mc.py): lock-early never misses a payment; 2033 surplus p5/p50/p95 $159k/$207k/$273k; 2031
  floor median $165k. Growth-first: 3.2% miss (13.7% if the 2028 deposit is $75k, 40.8% if $0); surplus
  $20k/$226k/$540k. Growth-sleeve equity 50/60/70% barely changes the median ($205k/$207k/$209k).
- UNVERIFIED (search snippets only): Fed hike to 3.75-4.00% on 2026-09-16; Taiwan construction costs +6.54% y/y
  (Aug 2026), CPI ~2.0%; USD/TWD ~31.8 with ~5% annual volatility. Last year's approved ETF list (historical only)
  is in competition/historical/2025_26/; this year's list and WInS trading rules are still unknown.

## Current strategy ("lock early"; team has not formally approved it yet)
Buy Treasuries matching the ten payments in January 2027 (fits inside $300k at today's curve; top up from the 2028
deposit if needed, buying the longest-dated payments first); take market risk only with the surplus (growth sleeve
~60% equity); in 2031 promise co-sponsors a floor already bought in a 2-year Treasury plus an upside with a stated
probability; "high certainty" = fully funded at market prices, cash-flow/duration matched, residual risk U.S.
default; after 2033 keep leftover money mainly as project flexibility. In WInS, mirror the post-2028 target (~65%
Treasuries in an IEF/TLT duration mix, ~35% broad equity). Prior council work: research/council_2026-09-27/.

## Team client research (provided in the chat, not in the repo)
Two team documents on why Wharton chose Laura and her public professional profile. Assistant review:
research/team_materials/review_why_laura_and_public_profile.md (keeps: client trend toward funding community
infrastructure; willingness vs capacity; human-capital hedge; low-cost transparency; framing from her books;
rejects: facility as a dated liability, income-gap cash buffer, values screens as a decision, residency = home).

# PART 2: MISSION
NORTH STAR: "Why would Laura choose our firm's strategy over 6,000 others?" Every phase must answer to it. Skill and a
correct strategy are necessary but not sufficient; the winning strategy also reflects who she is, what she values and
how she thinks, in ways she would recognise as hers.

Make our strategy one that no judge, no co-sponsor, no statistician and no rival can poke a hole in, and that shows
an understanding of Laura, of the case designers' intent, and of the 2026 investing world that 99% of teams will
miss. Surface every anomaly, blind spot and "why is it like this?" question; answer the ones that matter with
evidence; turn the answers into specific, approved-by-team strategy improvements.

# PART 3: TEAM OF AGENTS (about 50-60 agents; follow this roster)

## Phase A: Foundations (3 agents, parallel)
- A1 Case Lawyer: extract every requirement, instruction, number, definition and notable word choice from the four
  official documents into a numbered register (quote + location).
- A2 Fact Registrar: re-run research/verified_2026-09-27/*.py, confirm outputs, list every number with its source and
  status (verified / snippet / assumption).
- A3 Blind-spot Mapper: list stakeholders (Laura, co-sponsors, residency participants, the teacher-PM, judges, rival
  teams, Wharton as organiser) and what each would care about.

## Phase B: Question generation (8 lenses x 2 independent agents = 16; parallel)
Each lens gets two agents with different starting angles; each must produce 15-30 questions, each tagged with the
official requirement or verified fact it anchors to. Use the seed bank in Part 5 but go beyond it.
- B1 Case Anomalies (every unusual word, number, omission, ordering, design choice in the official documents).
- B2 Why Laura / Case-Designer Intent (client history 2021-2027: Jordan, Hjemdahl, Ash, Ayoola, Barwin, Gao; what
  Wharton is testing; what she represents; how it connects to investing).
- B3 Laura's World & Human Capital (her public professional record, values, books and their lessons; income risks:
  publishing cycles, book challenges, AI and illustration, US-China; privacy respected; no tokenism).
- B4 Top-Practitioner Benchmark (how the best goals-based wealth managers, pension CIOs, endowment CIOs and private
  bankers, e.g. at Goldman Sachs, BlackRock, JPMorgan, Vanguard, would approach this exact client; their published
  frameworks; governance, rebalancing, behavioural coaching, reporting of uncertainty).
- B5 2026 Macro & Markets Landscape (rates and why they are high; Fed path; inflation regimes; U.S. fiscal position and
  Treasury credit; equity valuations and AI concentration of indices; dollar; China; Taiwan Strait; Taiwan inflation
  and construction costs; what this means for a 2027-2042 liability).
- B6 Co-sponsors & Philanthropy (how foundations and co-funders assess a founder's pledge; seed and matching gifts;
  credibility; what a strong pledge range and fundraising paragraph must contain).
- B8 Voice of Laura (2 agents): collect Laura's OWN words from public sources beyond the case (her website, published
  interviews, podcasts/talk transcripts, Q&As, Wharton Magazine, Poets&Quants, book pages and her books' public
  excerpts). For each quote: exact wording, source URL, date, context. Then map quotes to values, to how she makes
  decisions and handles risk, and to implications for the strategy and for how we communicate with her. Questions to
  generate: what would she find inauthentic, what would earn her trust, which of her own ideas does our strategy echo.
- B7 Competition Meta & Judges (what past semifinalists and winners did; judge commentary; what a "typical strong
  team" will submit this year; how deliverable mechanics shape scoring; how to show a 16-year strategy in 6 weeks).

## Phase C: Filter (code dedupe + 6 skeptic agents in batches)
A question survives only if it passes all three:
- So-what: its answer would change a decision, a number, or a sentence in a deliverable (Oct 23, Nov 6, Dec 4).
- Anchor: tied to the official case/criteria or to a verified fact bearing on them.
- Adversarial: at least 2 of 3 skeptics fail to show it is trivial, already answered in Part 1, or wrong.
Failed-but-interesting questions go to a Finale Q&A bank. Log counts dropped at each step.

## Phase D: Research & answer (10-12 specialist agents; each takes the surviving questions in its domain)
- D1 Rates & Fixed-Income Analyst (curve, ladder, pre-funding gap to Jan 2027, reinvestment, Treasury credit).
- D2 Equity & AI-Concentration Analyst (index concentration, valuations, what a broad fund really owns in 2026).
- D3 Quant Modeler (extend strategy_mc.py: correlation between a bad 2027 market and a smaller 2028 deposit;
  pre-funding rate risk; confidence statements for the 2031 range; save scripts).
- D4 Taiwan, FX & Geopolitics Analyst (TWD costs vs USD payments; construction inflation; contingency thinking).
- D5 Philanthropy & Co-sponsor Analyst.
- D6 Client Psychologist / Behavioural Finance (what Laura will feel and do in a bad year; pre-commitment rules).
- D7 Wharton Intent Historian (client trend, official Wharton framing, past case designs vs this one).
- D8 Professional-Practice Benchmarker (map our strategy against named industry frameworks, with sources).
- D9 Communication Analyst (can each idea be said in plain English within 550 words; jargon and overclaim risks).
- D13 Quote Verifier: checks every Laura quote against its primary source; a quote that cannot be verified verbatim is
  marked PARAPHRASE/UNVERIFIED and must not be presented as her words.
- D10 Compliance Officer (AI policy, format rules, eligibility, anything disqualifying).
- D11-D12 Overflow researchers for heavy topics.
Every answer: evidence with sources (primary first; snippets labelled UNVERIFIED), Python for numbers, and the
concrete implication (decision / number / sentence) and which deliverable it affects.

## Phase E: Strategy integration & red team (6 agents)
- E1 Strategy Architect: turns answers into specific change proposals to the current strategy, with side effects.
- E2-E4 Red team: a Wharton judge, Laura herself, a rival team's best strategist; each attacks the revised strategy.
- E5 Pre-mortem analyst: "It is January 2027 and we missed the semifinals. Why?" List causes and fixes.
- E6 Chief Strategist: resolves conflicts, ranks changes by impact, writes the final specification.

## Phase F: Completeness loop (1-2 agents)
Completeness critic asks: which lens, stakeholder, source, risk or requirement was not covered? Anything found becomes
another round of Phases B-E for that gap. Stop when two consecutive rounds add nothing that passes the filters.

# PART 4: RULES
- CLAUDE.md working rules apply. Official materials and verified data only; never invent facts; label assumptions.
- No submission-ready prose (no drafted pitch, IPS paragraphs, notes or report text). Produce specifications,
  evidence, numbers and checklists that the team turns into its own writing. Nothing goes to judges without team
  approval.
- Quotes: exact wording from primary sources only, with URL and date; never invent or polish a quote.
- Respect privacy: use Laura's public professional record only; no personal-life details; never suggest contacting
  her. No student personal data.
- No ticker selection (this year's approved list is unknown); instrument types only.
- Report blocked sources rather than guessing. Write outputs only under research/insight_v1/; commit and push; update
  CLAUDE.md with the key results and open items.

# PART 5: SEED QUESTION BANK (start here, go beyond)
Case design:
1. "The investment strategy that Laura ultimately chooses": she is comparing firms. What makes her choose us?
2. Why does the case say the teacher-PM "makes the final investment decisions"? What governance must the IPS set?
3. Ten x $50k = $500k, equal to last season's WInS starting cash. Coincidence, and does it matter?
4. The money arrives Jan 2027 but rates move until then; our cushion is ~0.27%. What is the rule if rates fall first?
5. "Before making the first operating payment or contributing to the facility": is this ordering the intended
   priority rule (promise first, dream second)?
6. Co-sponsors may fund the facility but not operations. Why that asymmetry, and what does it imply?
7. Funding beyond 2042 is out of scope, but co-sponsors will ask about 2043. Role of the flexibility money?
8. Why is the co-sponsor conversation exactly two years before 2033 (a 2-year Treasury exists)?
9. Is a "credible range" a prediction interval, a commitment floor, or both? What confidence would a statistician
   accept, and how wide can it be before it is useless to co-sponsors?
10. Why state "not adjusted for inflation" explicitly? (nominal Treasuries match; TIPS mismatch)
11. Why must teams not size a contingency fund, yet preserve flexibility? How should flexibility be expressed?
12. Why no ESG/values preference this year when 2025-26 was impact-led?
13. Why are Trading Notes due before the IPS? What "developing strategy" story do judges want to see?
14. Why no charts or citations in the IPS? What must the words alone prove?
Laura:
15. "The only person who needs to believe... is yourself" vs co-sponsors who must believe her: is the case built on
    turning private conviction into public proof?
16. Wrong-way risk: a 2027 market crash also shrinks advances, speaking and licensing. Is the 2028 deposit most
    likely to shrink exactly when the portfolio is down?
17. Her books are about messy identity and learning to fall safely: what investment principles would she recognise
    as hers?
18. A statistics graduate chosen in the year certainty must be defined: what will she reject on sight?
19. A Wuhan-born, Texas-raised founder building a residency in Taiwan: what does belonging across borders imply for
    currency, costs and communication, without tokenism?
20. Does generative AI threaten her income, and does a 2026 index fund make her an AI investor? Whose choice is that?
2026 world:
21. Why are U.S. rates the highest since 2007, and what regime shift would hurt or help this plan?
22. "Certain barring U.S. default": after U.S. credit downgrades, how certain is certain? Honest answer?
23. If inflation re-accelerates, fixed $50k payments are easier to fund but buy less: who bears that?
24. Taiwan Strait risk: what if the residency cannot operate in Taiwan? Where do committed payments go?
25. USD/TWD and Taiwan construction costs: how should the co-sponsor range be quoted?
Professional practice:
26. At ~103% funded, a pension would lock almost everything. Why would a professional take any risk with the promise?
27. How would a top private banker coach Laura through a 2029 bear market? What pre-commitment rules?
28. Which named frameworks (goals-based wealth management, liability-driven investing, wealth allocation framework,
    endowment spending rules) fit which part of the plan, and which would a judge recognise?
Competition:
29. What will 6,000 teams submit, and what is distinctive yet correct about ours?
30. How do we show a 16-year strategy through 6 weeks of trades?
31. Pre-mortem: why might a strong team with a correct strategy still miss the Top 50?

Laura's voice:
32. Why would Laura choose our firm over 6,000 others? What would make her feel understood rather than analysed?
33. Which of her own public statements about risk, failure, belonging, money or success does our strategy embody?
34. What would she find inauthentic or "finance-bro" in a typical team's pitch?

# PART 6: OUTPUTS (research/insight_v1/)
1. insights.md: top 15-25 insights ranked by impact: question -> answer -> evidence -> what changes -> deliverable.
2. anomaly_register.md: every case anomaly, likely purpose, our response.
3. why_laura.md: verified facts vs interpretation; the one-sentence thesis it supports.
4. practice_benchmark.md: how top practitioners would handle this client vs our strategy; gaps closed.
5. landscape_2026.md: the macro/market facts that bear on the plan, with sources and status.
6. strategy_changes.md: proposed changes (for team approval) with reasons, numbers and side effects.
7. risk_register.md: every risk, size, handling, residual risk.
8. premortem.md and finale_qa_bank.md.
9. open_questions.md: what only the team can answer; data still needed; sources blocked.
10. scripts/: all Python used, runnable.
11. laura_in_her_own_words.md: verified quotes (exact wording, URL, date, context) -> value -> implication for
    strategy and communication; unverified paraphrases listed separately.
12. why_us.md: the answer to the North Star, with the evidence behind each reason.
