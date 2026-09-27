# Shared agent brief: insight_v1 run (read this FIRST, fully)

Run started 2026-09-27 (today). Team Caplet (six Australian high-school students: Ray (team leader), Ahaan, Darren,
Harry, Eric, Young) in the 2026-27 Wharton Global High School Investment Competition. This run executes the locked
prompt `research/ultracode_prompt_v4_deep_strategy.md`. Read that file's PART 1 (context), PART 2 (lessons from
last year), PART 3 (mission), PART 5 (rules) and PART 6 (seed questions) in addition to this brief. Also read
`CLAUDE.md` (project memory). The official case wins over every other source.

NORTH STAR: "Why would Laura choose our firm's strategy over 6,000 others?" Every output must answer to it. Skill
and a correct strategy are necessary but not sufficient; the winning strategy also reflects who she is, what she
values and how she thinks, in ways she would recognise as hers.

DESIGN PRINCIPLE (last year's main failure): complexity must earn its place. Best insight, highest value, least
complexity. Compliance with this year's WInS rules comes before any strategy idea. Every decision must trace back to
Laura or the case.

## 1. Where things are (all paths relative to repo root /home/user/caplet-investment)
Official (authority order: case > guides > criteria page):
- Client case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (4 pages; PDF alongside)
- IPS guide: `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` (6 pages; PDF alongside)
- Trading Notes guide: `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` (2 pages)
- Deliverables + evaluation criteria: `competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md`
- Manifest (SHA-256 verified 2026-09-27): `competition/official/2026_27/manifest.yaml`
Market data (team downloads, primary): `competition/official_market_data/` (Treasury par curve Sept 2026 CSV,
IEF and TLT fact sheets 2026-06-30, JPM 2026 LTCMA USD matrix PDF). Historical only (NOT this year's list):
`competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt`.
Verified scripts: `research/verified_2026-09-27/official_curve_pv.py`, `strategy_mc.py` (both re-run 2026-09-27 and
reproduce: $292,264; lock-early surplus p5/p50/p95 $159k/$207k/$273k; growth-first 3.2% miss).
Prior AI council work (brainstorming, lower authority, many numbers superseded): `research/council_2026-09-27/`
(start with `01_chair_memo.md`, `round2_referee_ruling.md`), `research/blueprints/01_trading_notes_blueprint.md`,
`research/team_materials/review_why_laura_and_public_profile.md`.
Team's two client documents (NOT in the repo, never copy their text into the repo; read-only):
- `/tmp/claude-0/-home-user-caplet-investment/4ef462a5-52dd-5480-b22c-ecbc4432d179/scratchpad/team_docs/team_client_profile.md`
- `/tmp/claude-0/-home-user-caplet-investment/4ef462a5-52dd-5480-b22c-ecbc4432d179/scratchpad/team_docs/team_why_wharton_chose_laura.md`
  These are team research from public sources; many claims are unverified (e.g. CCA-Vanderbilt acquisition,
  festival figures). Treat them as leads to verify, never as facts. Where they conflict with the case, the case wins.
Python: use `/home/user/caplet-investment/.venv/bin/python` (numpy, scipy, pandas, matplotlib, pypdf installed).
Run scripts from the repo root. Save any new script under `research/insight_v1/scripts/` with a docstring that lists
inputs (with status labels) and how to run it.

## 2. Source access (checked 2026-09-27 11:35 UTC)
Reachable with WebFetch/curl: home.treasury.gov, fred.stlouisfed.org, www.ishares.com, am.jpmorgan.com,
globalyouth.wharton.upenn.edu, magazine.wharton.upenn.edu, lauragao.com, en.wikipedia.org,
poetsandquantsforundergrads.com, wghsinvcomp.smapply.us (public pages only), www.federalreserve.gov, nuvoices.com,
legacy.diversebooks.org, www.bookweb.org, thenerddaily.com, www.apra.gov.au. Blocked/refused: www.futurefund.gov.au
(HTTP 403 from the site). Load web tools with ToolSearch ("select:WebFetch,WebSearch"). If a source is blocked or
refuses, say so; never guess its content.

## 3. Status labels (use on EVERY factual claim and number)
- VERIFIED-PRIMARY: you read it on the primary source page/file yourself (give URL + access date or repo path).
- VERIFIED-REPO-FILE: from an official or primary file in this repo (give path + page/line).
- SNIPPET-UNVERIFIED: from a search result snippet or secondary source you could not confirm on the primary page.
- ASSUMPTION: a modelling or judgement input we chose; say why.
- PARAPHRASE-UNVERIFIED: wording attributed to a person that you could not confirm verbatim on a primary source.
Quotes: exact wording only, from the primary source, with URL, date of the piece, and context. Never invent, trim
into new meaning, or polish a quote.

## 4. Hard rules (v4 Part 5 + CLAUDE.md)
- SCOPE = SEMIFINALS ONLY (team leader, 2026-09-27). The Top 50 is chosen on the written deliverables (Trading Notes
  Oct 23, IPS Nov 6, Final Report Dec 4). Do NOT produce anything for the finale round: no finale pitch prep, no
  judge Q&A or defence question banks. Questions that fail the filters are simply "parked" (logged), not turned
  into a Q&A bank. "Judges" below means the semifinal readers of the written deliverables.
- Official materials and verified data only; never invent facts; label assumptions.
- NO submission-ready prose: no drafted elevator pitch, IPS paragraphs, trading notes, reflections, report text or
  fundraising paragraphs. Produce specifications, evidence, numbers, checklists and "what a strong sentence must
  contain" guidance that the team turns into its own writing. Wharton AI policy: AI for brainstorming; AI-generated
  text may not be submitted as students' work; AI use must be credited.
- Privacy: Laura's PUBLIC PROFESSIONAL record only. Do not record family members, partner, birth name, home/address,
  personal-life details or anything not bearing on her professional/public work, even if a source or the team docs
  contain it. Never suggest contacting her. No student personal data (no surnames, emails, birthdays).
- Identity: her books and public work are about identity, belonging, immigration and community; you may cite these
  themes as her public work. Never use identity as decoration or as a reason to pick investments (tokenism).
- No ticker selection: this year's approved list, starting cash and WInS rules are UNKNOWN (team confirmed
  2026-09-27). Speak in instrument types. IEF/TLT appear only as the verified duration data already in the repo.
  Never recommend a trade not confirmed as permitted; every trade-related item carries "confirm against this year's
  WInS list/rules before trading".
- Write only under `research/insight_v1/` (your assigned path). Do not edit official files, configs, CLAUDE.md,
  src/ or tests/. Do not commit or push (the main loop does that).
- Plain English for high-school students who want to learn; define each technical term the first time it appears;
  end every file you write with a short "What this teaches" note.
- Deadline priority: tier 1 = WInS trading now + Trading Notes (Oct 23); tier 2 = IPS (Nov 6, trading ends and the
  strategy freezes); tier 3 = Final Report (Dec 4; instructions released Nov 9).

## 5. The case in brief (verify against the case file; the case wins)
- $300,000 in at start of 2027 (Year 1); $150,000 at start of 2028 from publishing advances, speaking, licensing,
  other ventures. No other additions/withdrawals before 2033. Living costs outside the portfolio. Year = calendar
  year - 2026; all flows at the beginning of the year.
- Ten fixed $50,000 payments (NOT inflation-adjusted) at the start of each year 2033-2042 to the residency's
  operating expenses; funded by the portfolio alone with "a high degree of certainty"; teams may not rely on
  co-sponsors, grants, fees etc. for them.
- Start of 2033, BEFORE the first payment or any facility contribution: set aside an "operating reserve". Teams
  recommend its size and initial asset composition, how composition changes as payments approach/are made; define
  "high degree of funding certainty", explain how it was evaluated, and state assumptions.
- Facility contribution: no preset amount; recommend and justify what she can responsibly contribute after the
  reserve; "committing all remaining assets could limit her financial flexibility as the project develops". Teams
  need not size a separate contingency fund/endowment, estimate facility cost, budget, funding gap or business plan.
- 2031 (two years before): she approaches co-sponsors and must describe how much she expects to contribute in 2033,
  as a credible dollar RANGE plus the team's confidence that the 2033 contribution falls in it; explain favourable and
  unfavourable outcomes; the range "must also protect the portfolio's ability to fund the ten-year operating
  commitment". Overpromising damages credibility. Teams draft part of her fundraising materials.
- Co-sponsors etc. may fund the facility and operating support beyond her commitment, but not her commitment.
- She "has been willing to take thoughtful risks" and wants "an appropriate balance between pursuing growth and
  protecting the capital required for her goals".
- WInS portfolio = implementation of the strategy during the competition; WInS gains/losses NOT added to projections.
- Teams should explain assumptions about investment performance, timing of cash flows, outside funding, the effect of
  inflation on portfolio projections AND FACILITY COSTS, and financial flexibility.
- Taxes, Taiwan legal/regulatory issues and funding beyond 2042 are out of scope.
- Framing fiction: "You are a team of young analysts at an asset management company. Your portfolio manager (your
  team's teacher/advisor who makes the final investment decisions for your firm's portfolio)…" Real rules: advisors
  may not make decisions or trade; the team's advisor handles admin only.
- Case quote: "The only person who needs to believe in something is yourself."

Deliverables (official): Trading Notes Analysis Oct 23 (3 notes quoted exactly from executed WInS trades - "Yes, we
will verify this" - each with a reflection of 100 words or fewer: why, fit with strategy, how it serves Laura's goals,
funding needs or risk; focus on reasoning, not gains; the note trades need not still be held; must be consistent with
the later IPS; not expected: reserve size, projections, facility amount, co-sponsor draft). The guide's own example
note buys "an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin preparing for Laura's
future operating commitment". IPS Nov 6: title page (official team name, members "First Name, Last Initial", WInS
username) + 50-word elevator pitch + 500-word IPS on pages 2-3 (2-page maximum), Times New Roman 12, double-spaced,
1-inch margins, PDF <=5 MB; no graphics, charts, images, attachments, external links, footnotes or formal citations;
non-compliance = "will not be considered for semifinal selection"; IPS "becomes the official record"; "may not revise
its investment strategy after the submission deadline"; not expected in IPS: final reserve calculations, detailed
projections, final facility range, co-sponsor draft; focus on "strategy and decision-making framework … rather than
describing individual investments or presenting detailed financial calculations". Final Report Dec 4 (instructions
Nov 9, "beginning of Week 7"). Evaluators consider the three deliverables together.
Evaluation criteria (verbatim headings; no weights published): Investment Strategy; Client Knowledge and Objectives;
Portfolio Analysis; Articulation of Competition Experience; Creativity and Presentation (the last includes "an
authentic team voice" and communicating "Laura's potential facility contribution and investment uncertainty clearly
and credibly to prospective co-sponsors").

## 6. Verified numbers (reproduced 2026-09-27)
- Treasury par curve 2026-09-25 (treasury.gov CSV in repo): 1m 4.04, 3m 4.24, 6m 4.33, 1y 4.50, 2y 4.81, 3y 4.94,
  5y 4.98, 7y 5.06, 10y 5.17, 20y 5.54, 30y 5.49. The 10y rose ~38bp during September 2026 (4.79 on 9/1).
- Ten payments valued at 2027-01-01 on that curve: $292,264; -25bp $299,596; -50bp $307,135; -100bp $322,864;
  +50bp $278,198; +100bp $264,890. DV01 $289/bp; duration 9.90y; headroom under $300k: $7,736 (27bp). Forward zeros
  2027->2033/2037/2042: 5.08%/5.24%/5.48%. Same payments valued at 2033-01-01 on forwards: ~$394.9k.
- IEF effective duration 6.95y, TLT 15.31y, 0.15% expense each (fact sheets 2026-06-30) -> 64.8% IEF / 35.2% TLT
  duration match (duration match only; NOT a cash-flow match).
- JPM 2026 LTCMA (data 2025-09-30): U.S. large cap 6.70% compound (7.94% arithmetic, 16.47% vol); AC World 7.00%;
  EAFE 7.50%; U.S. intermediate Treasuries 4.00%; long Treasuries 4.90%; cash 3.10%; inflation 2.50%; correlation
  U.S. large cap vs intermediate Treasuries -0.01.
- strategy_mc.py (200k paths, seed 20260927): lock-early never misses (BY CONSTRUCTION); 2033 surplus p5/p50/p95
  $159k/$207k/$273k; 2031 floor (80% of sleeve in 2y at 4.81%) p5/p50/p95 $127k/$165k/$217k. Growth-first 3.2% miss
  (13.7% if 2028 deposit $75k; 40.8% if $0); surplus $20k/$226k/$540k. Sleeve equity 50/60/70%: median
  $205k/$207k/$209k, p5 $164k/$159k/$154k. Equities 5.0% compound: L median $200k; G miss 5.5%.
- UNVERIFIED (snippets): Fed hike to 3.75-4.00% on 2026-09-16; Taiwan construction costs +6.54% y/y (Aug 2026);
  Taiwan CPI Aug 2026 2.04% (another snippet says 2.4%); USD/TWD ~31.8 (FRED mirror; 10y daily vol 4.7%); last
  year's list is historical only; "sector minimum = team size", "200-trade cap", "first trade by Oct 10" are
  third-party claims only; 2025-26 starting cash $500k (this season's unknown).

## 7. Current strategy ("lock early"; NOT yet approved by the team)
Buy Treasuries matching the ten payments in January 2027 (fits inside $300k at today's curve; if rates fall first,
buy the longest-dated payments first and top up the rest from the 2028 deposit); take market risk only with the
surplus ("growth sleeve", ~60% equity); in 2031 promise co-sponsors a floor already bought in a 2-year Treasury plus
an upside with a stated probability; "high certainty" = fully funded at market prices, cash-flow/duration matched,
residual risk U.S. default ("certain in nominal USD, barring U.S. Treasury default"); after 2033 keep leftover money
mainly as project flexibility. In WInS, mirror the post-2028 target (~65% Treasuries in an IEF/TLT duration mix,
~35% broad equity).

## 8. Already answered convincingly by prior work (do NOT re-ask as open questions; you may challenge them only
## with NEW evidence, and say what is new)
1. Lock early beats growth-first / wait-until-2033 (G shortfall 3-8%, 13.7-17% at a $75k 2028 deposit, ~41-55% at $0;
   partial locks 50/80/90/95% still fail 35/26/14/3.4% with no 2028 deposit).
2. Rolling 2037-42 payments short ("tiering") is rejected (+$20k cost per -100bp, +$43k per -200bp).
3. Risk is measured on the surplus; the equity weight applies to the sleeve only.
4. Price off one bootstrapped zero curve: ladder $292,264 (not $295k/$297k/$333k).
5. More sleeve equity buys range, not median (+$0-10k median vs -$11-47k at p5).
6. Certainty is market-consistent/model-free (3-part definition); a model "95%" is fragile (no-lock 3.3-9.3% spread
   comes from rate-drift assumptions).
7. The 2031 floor must be bought (2y Treasury), not a model percentile; a missing 2028 deposit means "aspiration
   only".
8. Missing 2028 deposit under lock-early: payments safe, facility ~$7-11k ("correct failure mode").
9. Which number is the reserve (cost ~$292k in 2027 / market value ~$395k on 2033-01-01 / face $500k): report market
   value on 1/1/2033; reconcile "funded 2027, set aside 2033" in one sentence.
10. TIPS are not the core hedge (liability is nominal).
11. STRIPS (zero-coupon) beat coupon Treasuries for matching (coupon reinvestment risk ~$5k).
12. iBonds Dec-20XX Treasury ETFs cover 2033-37 payments only; nothing found for 2038-42 (snippets).
13. IEF/TLT ~64.8/35.2 duration match; twist gap ~$3-4k cannot be closed with two funds.
14. JPM 6.7% is compound (7.94% arithmetic).
15. Taiwan construction costs ran ~3.2x CPI (snippets): don't inflate facility cost at CPI; TWD risk cannot be hedged
    inside a USD promise: disclose, quote in two currencies.
16. Diagnosed bugs: actuary DF(0) bug; Vasicek drift bias; team's "$626k" implies 5.99%.
17. List & Lucking-Reiley (2002) seed-money effect: a mechanism, not a prediction for institutions.
18. Judging is not on P&L; Top 50 chosen on written deliverables; three deliverables judged together.
19. Case-reading errors in team docs already corrected: facility is not a dated fixed liability; no income-gap cash
    buffer (living costs outside); residency is a creative residency in Taiwan, not her home; no ESG preference is
    named in the case; teaching income is not part of the case.

## 9. Open or disputed (good territory for questions and research)
- Sleeve equity weight 50/60/70% (is ~20-24% total equity after 2028 Laura's "thoughtful risk"?).
- 2031 rule parameters (share of sleeve locked as floor; USD-only vs also TWD quote; convert part of floor to TWD?).
- WInS mirror: post-2028 ~65/35 vs literal 2027 book (~99% bonds); the mirror implies ~35% total equity while the
  plan implies ~20-24% (inconsistency).
- WInS rules unknown: approved list, capital, trade limits, sector minimum and whether broad ETFs count, whether
  Treasury/defined-maturity/STRIPS funds are allowed.
- Rule if rates fall before January 2027 (P(cost > $300k) estimated 23-38%, ASSUMPTION-based): long-rungs-first vs
  nearest-first vs staged purchase.
- Joint tail: rates fall AND the 2028 deposit is missing/cut (up to ~$23-33k of the 2033 payment unfunded) -
  UNANSWERED.
- Real erosion of the fixed $50k operating budget (inflation/construction) - UNANSWERED; must be said aloud.
- Case interpretation: does "set aside at the beginning of 2033" allow economic funding in 2027? Is "high certainty"
  a number or "bought, not forecast"?
- Probability and correlation of a smaller 2028 deposit with a bad 2027 market (wrong-way risk).
- Stock-rate correlation relevant to the 2033 reserve cost.
- EWT/Taiwan tilt keep or drop; human-capital underweight of publishing/media; how to present AI exposure (her
  choice).
- Coupon-reinvestment rule if STRIPS unavailable; facility "scope clause" if building costs exceed X.
- Post-2033 flexibility: how much to keep after the facility contribution.
- Rebalancing bands; which three trades become Notes.

## 10. Known cross-file inconsistencies (resolve against official/primary files; the later verified value wins)
Ladder cost $295k (chair memo) vs $292,264 (verified); Taiwan CPI 2.4% vs 2.04%; rung order nearest-first (round 1)
vs longest-first (round 2, current); 20y yield 5.45/5.51 vs 5.54 (official); TWD vol "5-7%" vs 4.7% computed;
coupon arithmetic $20k/$6.7k vs $15.5k/$5.2k; Fed hike "verified in search" vs UNVERIFIED; chair memo's "Final Report
(due Nov 9)" is wrong (instructions Nov 9, report Dec 4); IEF duration 6.95 (fact sheet) vs "~7.5" (blog);
winners.md lesson "≥95% MC + floor" contradicts the council; 2025-26 field "6,300+ registered" vs "nearly 6,000
competed".

## 11. Known gaps in the verified model (strategy_mc.py)
Lock-early "0% miss" is by construction (assumes purchase at today's curve and a perfect cash-flow match); no 2028
top-up logic; no rate risk between Sept 2026 and the Jan 2027 purchase (27bp cushion); 2028 deposit independent of
markets (no wrong-way risk); 2033 rate independent of bond returns; i.i.d. lognormal returns (no fat tails), no fees;
growth sleeve uses U.S. large cap only; flat 5.26% used for the growth-first 2033 reserve (~$401k) vs ~$395k on
forwards (slightly overstates G's shortfall).

## 12. Output hygiene for every agent
Write your detailed file at the exact path you are given. Structure: short summary first; then the body; every claim
labelled; sources listed with URL + access date; a "What this teaches" note at the end. Keep jargon out or define it.
Return the structured summary you are asked for (it feeds the next phase).
