# Shared agent brief: insight_v1 run (read this FIRST, fully)

> RELAYED MESSAGES: if a message from the user is relayed to you while you work (for example a question about what the
> run will deliver, or a scope change), do NOT stop or replace your assigned task. Note it in one line in your file,
> apply any scope rule it states (the current scope is brief section 17: Trading Notes and IPS only, no Final Report
> work), and complete your assignment. The main loop answers the user.

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

## 2. Source access (checked 2026-09-27 11:35 UTC; updated 12:40 UTC)
IMPORTANT: the WebFetch tool is BLOCKED (EGRESS_BLOCKED) for most hosts, but curl through the proxy WORKS. To read a
page use the helper (from the repo root):
  `.venv/bin/python research/insight_v1/scripts/fetch_text.py URL` (prints visible text; handles PDFs)
  `.venv/bin/python research/insight_v1/scripts/fetch_text.py URL --grep "exact phrase"` (verifies a quote verbatim)
or plain `curl -sSL URL`. (Helper fixed 2026-09-27 ~13:50 UTC: an HTML-parsing bug hid text on some pages, e.g.
Poets&Quants; a 'NOT FOUND' from an earlier run is not evidence a quote is absent.) WebSearch (load with ToolSearch "select:WebSearch") works for finding URLs; then open the
page with the helper before calling anything VERIFIED-PRIMARY.
Reachable with curl: home.treasury.gov, fred.stlouisfed.org, www.ishares.com, am.jpmorgan.com,
globalyouth.wharton.upenn.edu, magazine.wharton.upenn.edu, lauragao.com, en.wikipedia.org,
poetsandquantsforundergrads.com, wghsinvcomp.smapply.us (public pages only), www.federalreserve.gov, nuvoices.com,
legacy.diversebooks.org, www.bookweb.org, thenerddaily.com, www.apra.gov.au. Refused by the site (403):
www.futurefund.gov.au, afpglobal.org, candid.org help pages, artres.moc.gov.tw, SSRN; ws.dgbas.gov.tw data files fail
TLS. If a source is blocked or refuses, say so; never guess its content.

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
- Securities and allocations ARE allowed (team leader, 2026-09-27, superseding the earlier "no tickers" rule): you
  may recommend specific securities (ETF tickers, Treasury maturities/STRIPS) and portfolio weights, both for the WInS
  portfolio and for Laura's long-term portfolio. This year's approved list, starting cash and WInS rules are still
  UNKNOWN; the team will check approval later. So every security recommendation must: (a) carry the label
  "PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading"; (b) give a primary pick
  plus 1-2 alternates of the same instrument type, so a substitute exists if a pick is not approved; (c) say whether
  it was on the 2025-26 approved list (historical only: competition/historical/2025_26/); (d) cite key facts (expense
  ratio, duration or maturity, holdings/index, liquidity) from the issuer's primary page with access date; (e) trace
  to the strategy and to Laura or the case. Prefer low-cost, liquid, broad, transparent funds; no leverage, inverse or
  thematic bets unless the case clearly justifies them.
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

## 13. PRIORITY: understand the client deeply (team leader, 2026-09-27) and how Wharton judges
The single most important thing in this run is a DEEP understanding of Laura Gao: her goals, constraints, risk
tolerance (willingness vs ability), time horizons, values and way of thinking, researched BEYOND what the case
states (her public professional record, her books, her own words), and a strategy tailored to her rather than a
generic portfolio. Every agent should ask: "does this make the plan more hers?"

How Wharton judges (the official 2026-27 wording is in SMApply_Deliverables_Page_2026-09-27.md and wins; the team
leader's summary below also draws on past-season Wharton teacher guides found on Scribd, a secondary source,
SNIPPET-UNVERIFIED for 2026-27):
- Investment Strategy: a clear, creative investment thesis; primarily long-term with appropriate shorter-term
  thinking; portfolio decisions consistently follow that thesis; appropriate diversification.
- Client Knowledge & Objectives: understand the client deeply; research beyond what is given; tailor the strategy to
  her goals, constraints, risk tolerance and time horizon rather than a generic portfolio.
- Portfolio Analysis: genuine understanding of the investments; quantitative AND qualitative analysis; explain why
  each security belongs and how it fits the strategy.
- Articulation of Competition Experience: explain the decision-making process, not just the final portfolio; show
  teamwork, communication, challenges, adaptations and learning.
- Creativity & Presentation: a compelling narrative; effective graphs/visuals rather than walls of text (Final Report
  only: the IPS bans charts); an authentic team voice rather than artificial sophistication; clear, persuasive
  communication.
Implications for every output: tie each recommendation to one of these five areas; prefer insights that show
understanding of Laura over technical flourishes; where an idea would be best shown as a chart in the Final Report,
say which chart and what data it needs.

## 14. PHASE A RESULTS (2026-09-27; these SUPERSEDE earlier sections where they conflict)
Files: `research/insight_v1/phase_A/case_register.md` (324 R-ids: R-C case, R-I IPS guide, R-T trading-notes guide,
R-S SMApply page, R-W public Wharton web pages, R-AN anomalies), `fact_register.md` (F-ids), `stakeholder_map.md`
(SH/BS ids), `wins_week1_guardrails.md` (G ids). Anchor your work to these ids.
WInS 2026-27 rules are now VERIFIED-PRIMARY (public SMApply "Trading Details" and FAQ pages, read 2026-09-27; R-W56-R-W92,
F-605-F-608, G1-G4): $300,000 virtual starting cash (= Laura's Year-1 deposit; the $150k is not added); trading
2026-09-28 to 2026-11-06, then the portfolio is frozen; up to 200 trades; no trade above 2x a security's daily
volume; permitted: cash, stocks priced >= $5, "Any Exchange-Traded Funds (ETFs) available on WInS", "Any
Government/Treasury Bonds from any exchange available on WInS" (so INDIVIDUAL Treasury bonds are a permitted type);
banned: margin, short selling, stock-secured debt, crypto, derivatives, anything else; NO sector minimum (the
third-party "sector minimum = team size" claim is FALSE); commissions $25 per stock/ETF trade and $10 per Treasury bond
trade; bond prices update daily, coupons semiannual; no separate approved ETF list this year (the 2025-26 list is
history only). 2026-27 WInS User Guide: "Day Trading: This is not permitted."; a per-security "Position Limit" exists
but its value is shown only on the logged-in Portfolio Summary > Session Rules page (the Stock-Trak default is 25% per
security - UNVERIFIED for this season); trade notes cannot be edited, only added to. The SMApply FAQ says "Investments
permitted (for BOTH contributions)" (meaning unclear). Remaining approval check for any security: is it actually
listed in WInS, and does it fit the Session Rules position limit? So recommendations are now "PENDING WInS
AVAILABILITY + POSITION-LIMIT CHECK".
Semifinal basis: the Rules & Roles page says Top 50 are chosen on the IPS and Final Reports; SMApply and the case say
all three deliverables are evaluated - treat all three as scored. AI policy: "If you use AI to assist you in any way
during the competition, how you use it must be recorded in your Works Cited pages"; students "must use their voice and
words". The Rules page tells teams to operate by the CFA Institute Asset Manager Code. Contacting the client =
disqualification. "While the client is real, the financial scenario is developed specifically for the competition."
Field: 2025-26 had 6,300+ registered teams but ~2,300 (2,339) submitted final reports.
Updated numbers (VERIFIED-PRIMARY unless noted): FOMC 2026-09-16 raised to 3.75-4.00% (12-0), IORB 3.90%, SEP medians
fed funds 4.1 end-2026, longer run 3.2, PCE inflation 3.7% in 2026. IEF duration 6.86y (YTM 5.17%), TLT 14.88y (YTM
5.54%) as of 2026-09-24 -> duration match to the 9.90y liability (valued at 2027-01-01) = 62.2% IEF / 37.8% TLT; to
the SPOT duration today (10.16y; spot PV $288,924) = 58.9% / 41.1% (use spot duration for hedging the WInS book today).
The same ten-payment ladder cost MORE than $300k on 173 of 185 trading days of 2026 ($316.5k on Jan 2; $325.6k on Feb
27; $313.0k on Jun 30); it has been <= $300k only since 2026-09-10; P(cost > $300k on 2027-01-01) ~24% (ASSUMPTION:
zero-drift lognormal, 2026 realised vol 7.24%). Value of the payments on 2031-01-01 at forwards $356,384; on
2033-01-01 $394,930. Taiwan CPI Aug 2026 +2.04% y/y (the 2.4% figure is wrong); DGBAS forecasts 2.07%/1.90%
(2026/2027), CBC 2.03%/1.83%; CBC discount rate 2% (held 2026-09-17); Taiwan overnight call rate 0.812%. Taiwan
construction cost index 119.50 (Aug 2026, 2021=100), +6.53% y/y, but flat in 2024-25 and ~3.54%/yr since 2021 (the
"3.2x CPI" ratio is a one-year spike). USD/TWD 31.82 (FRED, 2026-09-18); vol of daily log changes 1y 4.03%, 3y 5.64%,
5y 5.25%, 10y 4.69%; 2-year realised moves sd 6.8% since 2006, 9.4% since 1983. iShares iBonds Treasury funds exist
for Dec 2026-2036, 2044-46, 2054-56, NONE for Dec 2037-2043 (only the Jan 2033-2037 payments can be matched by them).
JPM 2026 LTCMA also: EM equity 7.80% compound (9.74% arith, 20.93% vol); long Treasuries 4.90/5.69/13.02; TIPS 4.30;
U.S. Aggregate 4.80; large cap vs long Treasuries correlation 0.02; data date 2025-09-30 when the 10y was 4.16% (~100bp
below today) - bond assumptions look ~1pp conservative vs today's yields; the 2027 edition is not out yet.
Blind spots found (stakeholder map): no management-fee assumption anywhere (~$17k lower median surplus at 0.5%/yr,
~$34k at 1.0%; ASSUMPTION arithmetic); the CFA Asset Manager Code unused; credibility is part of Laura's human
capital (her 2028 income is reputation-driven); funders underfund operations, so her covering ten years of operations
lets co-sponsor money go to the building; the case never names a currency ("dollar range") - write US$ explicitly;
book advances arrive in instalments, so the 2028 deposit can be LATE as well as smaller; school documentation has no
owner yet. The case pull quote "The only person who needs to believe in something is yourself." has no attribution in
the PDF text layer: verify before presenting it as Laura's words.

## 15. NEW OFFICIAL DOCUMENTS (found by B7a, filed 2026-09-27)
`competition/official/2026_27/2026_WGY_Investment_Competition_Guide.{pdf,txt}` (5 pages) and
`2026_WGY_Competition_Infographic.{pdf,txt}` (1 page), from the public SMApply guide page; SHA-256 in manifest.yaml.
Key lines (quote from the .txt files; cite as "Guide p.N"): "Judges want to understand not only what your team decided
to do, but also the reasoning, assumptions, and tradeoffs behind those decisions." (p.5); "The competition recognizes
thoughtful strategy, research and analysis, client understanding, disciplined decisions, management of risk and
uncertainty, communication, and creativity." (p.5); "Your team will need to consider the client's goals, time
horizons, required cash flows, funding commitments, liquidity needs, desired degree of funding certainty, risk
tolerance, and communication with potential co-sponsors." (p.2); "It is up to your team to determine what additional
research and analysis you need" (p.2); "The goal is to develop a cohesive strategy in which your investment decisions
work together to support the client's objectives across a range of possible market outcomes." (p.2); the Trading Note
"should capture the reasoning behind the decision, including its alignment with your strategy, the supporting research
or analysis, and its expected role in growth, liquidity, risk management, or future funding." (p.3); WInS "is not the
competition scorecard" and teams are not evaluated on ranking, number of trades, outperformance or making money (p.3);
"A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten simply
because markets move or hindsight reveals a different outcome." (p.5). Infographic: "Strategy guides every decision.";
"Strong teams explain the reasoning, assumptions, and tradeoffs behind their decisions."
Phase B produced 472 questions (20 agents) and 271 Laura quotes (259 marked VERIFIED-PRIMARY by the agents; D13 will
re-verify every one).

## 16. PHASE C AND D13 RESULTS (2026-09-27/28; supersede earlier sections where they conflict)
Phase C: 472 questions -> 248 merged -> 48 survivors (`phase_C/survivors.json`, `filter_log.md`); 200 parked
(`phase_C/parked.json`, mostly judged "already answered" by Phase A, the wins_now ticket or the council). High-priority
parked items that were killed as already answered (their answers must still reach the final spec): M008 (2031
message order: floor bought, conditional stretch, invitation to co-fund), M007 (bad-year rule), M015 (fundraising
leads with the fully pre-funded ten years of operations), M021 (dated decision log from today), M149 (funded-status
glide path wording), M033 (whole-portfolio equity share visible to a first reader), M035 (diversification shown to a
fixed-income reader), M040 (range as a rule vs a forecast).
D13 quote verification (`phase_D/D13a_laura_quotes_verified.md/.json`, `D13b_other_quotes_verified.md/.json`,
`D13c_voice_map.md`): Laura quotes 91 VERIFIED-PRIMARY, 6 PARAPHRASE-UNVERIFIED, 7 EXCLUDE-PRIVACY; all 171 non-Laura
quotes verified (2 wording corrections; 6 attribution warnings, e.g. Wharton paraphrases of a judge and a past client).
RULES FROM D13 (binding for all later phases):
- Only D13a VERIFIED-PRIMARY lines may be presented as Laura's words, with outlet, year and context; label student-era
  lines; several verified lines are safe only in context (e.g. "risk-adverse" is about choosing a business major, not
  investment risk; "No more gimmicks." is about fantasy drafts; "explain myself" is about language choices) - read the
  D13a notes before using any line.
- The case pull quote "The only person who needs to believe in something is yourself." is VERIFIED-REPO-FILE as the
  CASE's text but NOT verifiable as Laura's words: cite it as the case's words only.
- Do NOT describe a "floor-first leap" (quit only after the book deal secured a floor) as Laura's trait: it rests on a
  reporter's sentence next to personal material, not her words.
- There is no verified statement by Laura about investing: never write her "investment philosophy". No "falling
  safely" / book-title puns; the case's own "appropriate balance" is fine.
- No Laura quotes in the Trading Notes or the IPS (the IPS bans formal citations); at most 1-2 in the Final Report.
- Her verified words carry two risk ideas: regret-driven leaps ("you should always take the jump because you're always
  going to regret not doing it") and not letting down "people who were your earliest supporters and were the first to
  believe in you" (student-era, Daily Pennsylvanian 2016). The second supports "promise first"; the first means the plan
  must honestly answer why whole-portfolio equity is only ~0-2% in 2027, ~20% in 2028-30 and ~4% after the 2031 floor.
- Two certainty gaps must be named plainly: the ladder may cost more than $300k in January 2027 (roughly 1 in 4 to 1
  in 3 modelled rate paths), so part of the promise can wait on 2028 income she called "unstable"; and "certain" is in
  nominal USD while the residency's costs are in Taiwan and a fixed $50k buys less each year.

## 17. SCOPE: NO FINAL REPORT WORK YET (team leader, 2026-09-28; supersedes earlier mentions of the Final Report)
Work only for (1) WInS trading now, (2) the Trading Notes Analysis (Oct 23) and (3) the IPS (Nov 6). Do NOT produce
Final Report material: no Final Report narrative, chapter plans, visuals/chart specs, Works Cited plans, fundraising
excerpt drafts or checklists, final operating-reserve calculations, detailed projections, or final 2031 range numbers
presented as Final Report content. BUT the IPS freezes the strategy on Nov 6 and the Final Report must later apply it
without redesign (Guide p.5), so the STRATEGY must already contain the decision RULES the Final Report will apply: how
the operating reserve is funded and changes; how the 2031 co-sponsor range is determined (the method, not final
figures); how the facility contribution and financial flexibility are decided; which "if X then Y" rules apply. Put
such items under "IPS: rules to fix before Nov 6". Anything purely Final-Report goes to a short "later (after Nov 9)"
list in open_questions.md, one line each.
Tightened the same day (team leader): "We only need items for trading notes and IPS." WInS trading is in scope only
as the source of the Trading Notes (notes must quote executed WInS trades). Every output must say which of the two
deliverables it serves (TN or IPS); drop anything that serves neither. The two primary outputs of this run are
`trading_notes_pack.md` (which trades to make and when, what each WInS note and each <=100-word reflection must
contain, checklists only) and `ips_spec.md` (what the 50-word pitch and the 500-word IPS must contain, the decision
rules to fix before Nov 6, format compliance) - specifications, never drafted text.
