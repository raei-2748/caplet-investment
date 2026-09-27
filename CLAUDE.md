# Team Caplet: project memory

Wharton Global High School Investment Competition 2026-27. Keep this file current: update it whenever a fact,
decision, deadline or open item changes, and commit it with the related change. Last updated: 2026-09-27.

## Working rules (from the team leader)
- Use only exact official Wharton materials and verified sources. No fictional clients, rules, rosters or data.
  Anything not verified is marked UNVERIFIED; never fill gaps from memory or "typical" rules.
- Research online and verify facts; cite URL + date. Primary sites (treasury.gov, FRED, iShares, JPM, Wharton,
  SMApply) are blocked by this environment's network policy; only WebSearch snippets and GitHub work unless the
  user allows those domains.
- Do NOT write the Trading Notes, IPS or Final Report. The team wants knowledge: numbers, models, devil's advocate,
  trade checks, research/fact-checking. Wharton AI policy: AI for brainstorming; AI-generated work may not be
  submitted as the students' own and must be cited.
- Goal: top priority is reaching the Top 50 semifinals (chosen on the written Trading Notes, IPS and Final Report);
  the finale comes later. Keep deliverables plain-English (judges reward simple, elegant ideas). Semis-first does not
  change the rule that the team writes the deliverables; the assistant reviews drafts, checks trades and numbers.
- Repo is public; the team leader accepted putting competition materials in it. Do not commit student personal data
  (surnames, emails, birthdays) or rankings of teammates.

## Mandate (Ray, 2026-09-27)
The assistant has freedom to make decisions and choose its workflow, sticking tightly to the competition and the
materials provided, asking when information is needed, with the goal of reaching the semifinals. Everything that is
sent to the judges must be approved by the team. Assistant outputs are for inspiration and research; the team does
not submit them as they are. Deliverable help = blueprints (content, arguments, verified numbers, checklists) and
draft reviews, not submission-ready prose.

## Team
Lessons from 2025-26 (Ray, no feedback received): strategy packaging was over-complex for the insight; the team traded
assets outside the trading rules. So: complexity must earn its place; check every trade against this year's rules and
approved list before placing it; client first. Team is Australian (use only if it earns its place). The team has a
supervisor/advisor who handles administrative work only (consistent with the rules: advisors may not make decisions;
all strategy decisions are the students'; worth noting in the Final Report's Articulation section).
Ray's personal goal: learn markets and client analysis; include plain-English "what this teaches" notes.
Ray (Team Leader), Ahaan, Darren, Harry, Eric, Young (6 students). Roster in `config/team_roster.json`,
pending Wharton roster confirmation (due Oct 9; members locked after submission).

## Client: Laura Gao (official case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf`)
$300k start of 2027, +$150k start of 2028, no other flows before 2033. Ten fixed nominal $50k payments at start of
each year 2033-2042, portfolio-funded with "high degree of certainty" (no outside money). Operating reserve set aside
start of 2033; then a responsible facility contribution (Taiwan residency), preserving flexibility. In 2031 she gives
co-sponsors a dollar RANGE + confidence that must protect the payments; team drafts part of the fundraising text.
WInS P&L is NOT added to projections. Taxes, Taiwan legal and facility cost estimates are out of scope.
Structured in `config/client_mandate.yaml` (human_approved: false) and `config/wharton_private_2026_27.yaml`.

## Official deadlines (SMApply, 5:00 p.m. ET, no extensions)
Roster Oct 9 | Trading Notes Analysis Oct 23 (3 notes quoted exactly from executed WInS trades, <=100-word
reflections) | IPS Nov 6 (title page + 50-word pitch + 500-word IPS, TNR 12 double-spaced, no charts/citations;
TRADING ENDS AND PORTFOLIO LOCKS; strategy frozen) | Final Report instructions Nov 9 | Final Report + school
documentation Dec 4. Evaluation: Investment Strategy; Client Knowledge; Portfolio Analysis; Articulation of
Competition Experience; Creativity & Presentation. All three evaluated deliverables are judged together.

## Strategy status (council work in `research/council_2026-09-27/`, AI brainstorming)
- Leading option after 2 council rounds: "Lock early". Jan 2027 buy Treasuries matching the ten payments
  ($292k at the official 2026-09-25 curve); shortfall topped up from 2028 deposit (buy long rungs first); all
  risk in the surplus growth sleeve; 2031 range = floor bought in a 2-yr Treasury + upside with stated model
  probability; "high certainty" = market-priced full funding, cash-flow/duration matched, residual risk US default.
  Keep the team's two-clock sleeve management and pre-mortem discipline.
- Growth-first (team's original ~75% equity + later reserve) failed: 3-8% payment shortfall, ~50% if the 2028
  deposit is missing.
- Assistant's view (not a council consensus): 60% equity in the growth sleeve, lock 80% of the sleeve as the 2031
  floor, WInS mirrors post-2028 target (~65% Treasuries / 35% equity), only two rules in the IPS.
- NOT YET DECIDED BY THE TEAM. The team has not read the memos yet.
- Interview part 2 (2026-09-27): the team deferred to the assistant's evidence-based calls, provisionally:
  (1) growth sleeve ~60% equity (weakest call: 50-70% barely changes the median);
  (2) 2031: guaranteed floor + upside with stated probability (case p.3: overpromising damages credibility);
  (3) post-2033 leftover mainly as project flexibility/overrun buffer, ventures second (case p.3 "flexibility as the
  project develops"; living costs covered elsewhere); principle only, no contingency sizing required;
  (4) no roles assigned yet; suggested roles: lead, trader, rates analyst, growth/risk analyst, client/co-sponsor
  lead, Taiwan/inflation researcher. The team must be able to defend these in its own words.

## Client insight (team docs reviewed 2026-09-27: `research/team_materials/review_why_laura_and_public_profile.md`)
Keep: client trend toward community-infrastructure funding; willingness vs capacity (career risk -> portfolio should
not add correlated risk; bites via the 2028 deposit); human-capital hedge; low-cost transparency; framing from her
books. Rejected as conflicting with the case: facility as a dated liability, income-gap cash buffer, values screens
as a decision, residency = where she lives.

## Key facts (verification status)
VERIFIED from primary files in `competition/official_market_data/` (team download 2026-09-27):
- Treasury par curve 2026-09-25 (treasury.gov): 1y 4.50, 2y 4.81, 3y 4.94, 5y 4.98, 7y 5.06, 10y 5.17, 20y 5.54,
  30y 5.49. (A search summary claiming 10y 4.22% was wrong.)
- Ten payments valued at 2027-01-01 from that curve: $292,264; DV01 $289/bp; duration 9.90y; headroom under the
  $300k deposit $7.7k = 27bp (a 25bp rally costs +$7.3k, -100bp +$30.6k). Script:
  `research/verified_2026-09-27/official_curve_pv.py`.
- IEF effective duration 6.95y, TLT 15.31y, both 0.15% expense (fact sheets as of 2026-06-30) -> duration match
  64.8% IEF / 35.2% TLT.
- JPM 2026 LTCMA (data 2025-09-30): U.S. large cap 6.70% COMPOUND (7.94% arithmetic, 16.47% vol); AC World 7.00%
  compound (16.78% vol); EAFE 7.50%; U.S. intermediate Treasuries 4.00%; long Treasuries 4.90%; cash 3.10%;
  inflation 2.50%. Implication: the council scenario "6.7% geometric" is the right one (growth-first shortfall ~3%,
  its median facility ~$19-27k above lock-early, but a far worse downside; the lock-early case still holds).
VERIFIED 2026-09-27 by the insight_v1 run (primary pages; details in `research/insight_v1/phase_A/`):
- WInS 2026-27 rules (public SMApply Trading Details + FAQ): $300,000 virtual cash (= Laura's 2027 deposit; the $150k
  is not added); trading Sep 28 - Nov 6 then frozen; up to 200 trades; no trade above 2x a security's daily volume;
  allowed: cash, stocks >= $5, any ETF available on WInS, government/Treasury bonds available on WInS (individual
  Treasuries allowed); banned: margin, shorting, stock-secured debt, crypto, derivatives, anything else; NO sector
  minimum (the "sector minimum = team size" claim is false); commissions $25/stock-ETF trade, $10/bond trade; no
  separate approved ETF list this year; day trading not permitted (2026-27 User Guide); a per-security position limit
  exists, shown only in WInS Portfolio Summary > Session Rules (check before the first trade); trade notes cannot be
  edited, only added to. "First trade by Oct 10" still unverified (check the logged-in Trading Details page).
- Fed raised to 3.75-4.00% on 2026-09-16 (12-0). Taiwan CPI Aug 2026 +2.04% y/y; construction cost index +6.53% y/y
  but ~3.5%/yr since 2021; USD/TWD 31.82 (Sep 18), daily-change vol 4.0-5.6% depending on window.
- IEF 6.86y / TLT 14.88y durations (2026-09-24): match to 9.90y = 62.2/37.8; to today's spot duration 10.16y = 58.9/41.1.
- The ladder cost more than $300k on 173 of 185 trading days in 2026; it fits under $300k only since Sep 10.
- AI policy: any AI use must be recorded in the Final Report's Works Cited; students must use their own voice and words.
- 2025-26: 6,300+ teams registered but ~2,300 submitted final reports.

## Open items
- [ ] Team: log into WInS before the first trade: screenshot Session Rules (position limit), check each security is listed,
      read the logged-in Trading Details page (activity minimums), and note the trade-note character limit
- [x] Interview part 2 answered (team deferred; provisional calls recorded above)
- [ ] Team: assign roles; check SMApply for a trading-rules page, search tickers in WInS, ask advisor/Wharton for list
- [x] Verified from primary files: Treasury curve, IEF/TLT durations, JPM LTCMA compound basis (2026-09-27)
- [x] Re-ran strategy simulation on official inputs: `research/verified_2026-09-27/strategy_mc.py` (2026-09-27).
      Base: Lock-early never misses a payment; 2033 surplus p5/p50/p95 $159k/$207k/$273k; 2031 floor median $165k.
      Growth-first: 3.2% miss; surplus p5/p50/p95 $20k/$226k/$540k; 13.7% miss if 2028 deposit is $75k, 40.8% if $0.
      Equity weight 50/60/70% in the sleeve: median $205k/$207k/$209k (barely matters).
- [x] Trading Notes blueprint drafted: `research/blueprints/01_trading_notes_blueprint.md` (awaiting team approval)
- [ ] Team reads `01_chair_memo.md` + `round2_referee_ruling.md` (section 4: 12 concepts) and picks the strategy
- [ ] Ultracode run to be launched by Ray in a NEW session with `research/ultracode_prompt_v4_deep_strategy.md` (v4 FINAL, locked 2026-09-27: full context,
      fixed agent roster ~45-55 in phases A-F, 31 seed questions; supersedes v3)
      (question engine: case anomalies, why Laura, top-practitioner lens, her world, co-sponsors, judges, contrarian;
      so-what/anchor/adversarial filters; outputs to research/insight_v1/). Start it on this branch; re-paste the
      team's two client documents (kept out of the repo). Allow primary domains first if possible.
      (v2 audit prompt `research/ultracode_strategy_audit_prompt.md` superseded by v3 for now.)
- [ ] Final run: decision pack + first-week trade plan + defence Q&A (after the items above)
- [ ] Code: `report audit-ai` always passes (audits one hard-coded block); built-in $100k/25% sector defaults and the
      31-stock default universe marked "Wharton-approved" are not official

## Repo map
Official materials: `competition/official/2026_27/` (+ `manifest.yaml`). Historical: `competition/historical/`.
Configs: `config/`. Council/research: `research/council_2026-09-27/`. Tests: `pytest` (59 passing); demo runs
write only to `outputs/demo/` and `decisions/demo/` (git-ignored).
