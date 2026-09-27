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
- Goal: win the Global Finale, keep deliverables plain-English (judges reward simple, elegant ideas).
- Repo is public; the team leader accepted putting competition materials in it. Do not commit student personal data
  (surnames, emails, birthdays) or rankings of teammates.

## Team
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
  (~$292-295k at 2026-09-25 yields, UNVERIFIED); shortfall topped up from 2028 deposit (buy long rungs first); all
  risk in the surplus growth sleeve; 2031 range = floor bought in a 2-yr Treasury + upside with stated model
  probability; "high certainty" = market-priced full funding, cash-flow/duration matched, residual risk US default.
  Keep the team's two-clock sleeve management and pre-mortem discipline.
- Growth-first (team's original ~75% equity + later reserve) failed: 3-8% payment shortfall, ~50% if the 2028
  deposit is missing.
- Assistant's view (not a council consensus): 60% equity in the growth sleeve, lock 80% of the sleeve as the 2031
  floor, WInS mirrors post-2028 target (~65% Treasuries / 35% equity), only two rules in the IPS.
- NOT YET DECIDED BY THE TEAM. The team has not read the memos yet.

## Key facts (verification status)
- 10y Treasury 5.17% close 2026-09-25 (snippets, UNVERIFIED primary); Fed hiked to 3.75-4.00% on 2026-09-16.
- CONFLICT (re-searched 2026-09-27): a search summary claiming to quote Treasury's official Sep 25 par curve gave
  10y 4.22% (2y 3.72, 5y 3.77, 7y 3.97, 20y 4.77, 30y 4.78), contradicting the 5.17% from several other snippets.
  Search summaries are not reliable for this; the official CSV must be checked by hand before any number is used.
- Ladder PV at 2027-01-01 $292.3k (Curve A); a stale-looking Curve B gives $314.5k. DV01 ~$289/bp.
  Flat-rate check: 5.26% -> $295k, 4.8% -> $308k, 4.5% -> $317k, 4.3% -> $324k. If the lower curve is right the
  ladder does NOT fit in the $300k deposit (2028 deposit must top it up).
- IEF effective duration: snippets say 6.89y (Sep 2026) and ~7.5y (earlier 2026); TLT: not found. UNVERIFIED.
- Last year's approved ETF list (`competition/historical/2025_26/`): Treasury IEF, TLT, GOVT, SHY, SHV, BIL, VGSH,
  USFR; TIPS TIP, VTIP; no iBonds/STRIPS. IEF/TLT ~65/35 duration-matches ~9.9y (durations UNVERIFIED).
- Taiwan: construction costs +6.54% y/y (Aug 2026), CPI ~2.0%; USD/TWD ~31.8, ~5% annual volatility.
- JPM 2026 LTCMA US large cap 6.7%: arithmetic vs geometric UNVERIFIED (matters: 6.7% arithmetic ~5.5% compound).
- Sector minimum = team size (6), 200-trade cap, first trade by Oct 10: third-party sources only, UNVERIFIED.

## Open items
- [ ] Team: this year's WInS rules, approved list, starting cash, trading-note location/limits (Ray checking)
- [ ] Team: interview part 2: Laura's risk appetite, 2031 promise trade-off, post-2033 leftover use, who does what
- [ ] Verify from primary sources: Treasury par curve CSV, IEF/TLT fact-sheet durations, JPM LTCMA basis
      (needs the user to allow the domains, or upload files)
- [ ] Team reads `01_chair_memo.md` + `round2_referee_ruling.md` (section 4: 12 concepts) and picks the strategy
- [ ] Final run: decision pack + first-week trade plan + defence Q&A (after the items above)
- [ ] Code: `report audit-ai` always passes (audits one hard-coded block); built-in $100k/25% sector defaults and the
      31-stock default universe marked "Wharton-approved" are not official

## Repo map
Official materials: `competition/official/2026_27/` (+ `manifest.yaml`). Historical: `competition/historical/`.
Configs: `config/`. Council/research: `research/council_2026-09-27/`. Tests: `pytest` (59 passing); demo runs
write only to `outputs/demo/` and `decisions/demo/` (git-ignored).
