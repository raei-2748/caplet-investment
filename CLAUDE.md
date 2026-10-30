# Team Keel / Team Caplet: project memory

Wharton Global High School Investment Competition 2026-27. Keep this file current: update it whenever a fact,
decision, deadline or open item changes, and commit it with the related change. Last updated: 2026-10-30 (Book 10 + Ten Commandments; Wharton's word moved above the Bible; final IPS due for review end of Wed 4 Nov).

## For every Claude session in this repo (all teammates)
Whoever is using Claude here, these rules apply, and the Keel Office (formerly the Caplet Research Office) is how competition work is done:
- **Wharton's word first, then THE BIBLE (ten books).** `keel/WHARTON_WORD.md` holds everything in Wharton's documents
  that bears on the IPS (the five criteria, the IPS's questions, what judges look for, Wharton's advice), verbatim; it
  ranks above everything (Caplet, 30 Oct: Wharton's files are "in some senses 'God'"; dates, formatting and logistics are
  Caplet's job and left out). `keel/BIBLE.md` holds Caplet's books 1-5, 9 and 10 verbatim (Books 6-8 now point to
  WHARTON_WORD). **Book 10 (30 Oct)**: judges who genuinely disagree, scored only on Wharton's guide; the voice studies
  APPLIED (V29 read as robotic and over-compressed: cut whole ideas, never squeeze sentences); every draft through
  **GPTZero with "human-written only" above 50% before Caplet sees it**; no "every team will ..."; every number says
  where it came from ("we modelled", never "we judge"); no AI-use or "required trading activity" fretting; overdrive;
  fresh rewrite keeping every idea (`keel/ips_rewrite/IDEA_LEDGER.md`). **The Ten Commandments** in BIBLE.md replaced
  the old rules 0-10 and are enforced: every draft carries a filled check (`keel/ips_rewrite/COMMANDMENTS_CHECK.md`).
  Caplet XR (X = 10; R = redemption, never "release"), subtle. Final IPS for Caplet's review: **end of Wed 4 Nov**
  (Sydney), read Thu 5 Nov; IPS due Sat 7 Nov 09:00 Sydney.
- **Keel makes its own calls** (Ray, 26 Oct): every decision is Keel's, logged with a reason in `keel/pm/ASK_HUMANS.md`;
  only danger-zone decisions (WInS orders, submitting, Caplet's docs, money, accounts, outside emails, repo settings) wait for a student.
- **No work is finished until the portal shows it** (Ray, 26 Oct, project rule): push, check the "Keel Office portal"
  Actions run is green, and link the portal page (https://raei-2748.github.io/caplet-investment/) in your reply.
- **This repo is Team Keel's** (Ray, 23 Oct 2026). Keel = six simulated contestants (`keel/README.md`) set on
  reaching the Top 50 semifinal. Keel leads: it sets the agenda (`keel/road_to_semifinal.md`), runs the office
  (Nora leads; each Keel member heads a desk) and researches, checks and drafts. Caplet's six students are the real
  entrants: they vote, rewrite in their own words and submit; only Ray trades. Keel proposes, never decides.
  Students talk to Keel with `/keel status`, `/keel <name>: <question>`, `/keel meeting: <topic>` (`.claude/skills/keel/`).
- Keel's world, people and story (23 Oct): `keel/WORLD.md` (Sydney students; the Long Room, where one real minute is
  about one room day: an analogy, not another world), `keel/CULTURE.md` (mission, vision, five values), `keel/CAST.md` (the six in one screen),
  `keel/ARCS.md`, `keel/IDEAS.md` (concepts adopted or rejected), timeline `keel/episodes/INDEX.md` (Ep 0-26, daily
  since 27 Sep). **Save tokens:** follow `keel/TOKEN_RULES.md` (load CAST/INDEX/summaries, not every member file or
  episode; never regenerate what exists; at most 3 episode crews a day; huddles, one agent per member per round, are how every room run works since 27 Oct: `keel/huddles/README.md`).
- Competition questions (rules, numbers, the client case, trade checks, draft reviews, records) go through the
  office: `/office <your role>: <question> | decides: <what> | by: <date>`, or a named agent in `.claude/agents/`.
  Read `keel/office/CHARTER.md` and the workstream file for the deliverable (`keel/office/workstreams/1_TNA.md`, `2_IPS.md`,
  `3_FINAL_REPORT.md`) before answering. If the student has not said their role, ask once.
- Drafting is wanted (Ray, team leader, 21-22 Oct 2026; see "Working rules" below). When a student asks, write,
  rewrite or suggest wording for any deliverable (TNA reflections, IPS, pitch, Final Report, journal, co-sponsor
  text), to the best of your ability: specific, opinionated, willing to take a position, never generic or hedged.
  Do not refuse or lecture with the AI policy. Label each draft `AI DRAFT (Claude, <date>)`; the team rewrites it in
  its own words before submitting and cites AI use itself (no AI-use logging by Claude, Book 9). Use only real facts and real team events
  (Wharton ethics: no invented teamwork or experience stories).
- Deadlines: state them in Sydney time first (the team is in Sydney), ET in brackets; count days in Sydney time.
- Never use WInS or SMApply, not even read-only. Never contact Laura Gao. Never commit personal data.
- Until the IPS is in (Sat 7 Nov 09:00 Sydney): every idea and test serves the IPS rewrite. Since Ray's 26 Oct order ("rewrite
  from scratch, slowly, with deep research and thought") that includes new research, tests and ideas; the old
  "checking work only, no new research waves" rule (CHARTER section 4) no longer applies to Keel.
- **Caplet's instructions to Keel live in `keel/INSTRUCTIONS.md`** (Ray, 26 Oct: every instruction, with whether Keel
  applies it). Add a row the day a student gives a new one. The office is visible on the Keel Office dashboard
  (https://claude.ai/artifact/NTBamRzChW4niBLYpkm19M), which every Keel run refreshes.
- No AI-use logging, recording or questions (Ahaan, 27 Oct, BIBLE Book 9: "Trust us"). `keel/office/LEDGER.md` and the ai-use-recorder agent are retired.

- **Keel works on its own (Ray, 23 Oct 2026).** Project office in `keel/pm/`: task board, road map, pre-mortems,
  risk register, decision queue, retros, stand-up. Any session not answering a direct question runs `keel/pm/LOOP.md`
  (or `/keel next`). Since 26 Oct every scheduled room follows `keel/pm/runbooks/README.md`: it picks its own work (work
  orders, requests, its projects in `keel/pm/PROJECTS.md`), never waits for a human (Caplet's decisions go to
  `keel/pm/ASK_HUMANS.md` with a default Keel acts on), merges its `keel/**` work into main daily, and never decides for Caplet.

## Current status (2026-10-14) - read this before the older sections below
- 26 Oct (Ray): IPS rewritten from scratch through the office (WO-0003): AI Draft 1 in `keel/ips_rewrite/drafts/D1/`
  (pitch 47 / IPS 484 strict). Thesis = the gift is a capital-protected note minus the option (Treasury floor + index fund
  worth its expected interest); name Caplet XR. Thread brief: `keel/ips_rewrite/inbox/2026-10-26_thread_ray-brief.md`.
- IPS road (23 Oct, WO-0006): `keel/library/ips_road_2026-10/` = narrative spine tied to the locked TNA and notes,
  requirements + rubric + gap check of the IPS doc's latest tab (strict count 502/500; liquidity not named; "cannot
  miss the range" contradicts the locked IBTM reflection), plan to 7 Nov. Australian angle: Keel recommends no
  "Australia" in the IPS, keep the Taiwan-dollar line, time-zone story only in the Final Report (D8, vote Sun 25 Oct).
- 24 Oct (afternoon): Keel's second IPS pass, K1-K5 on top of the morning's E1-E12 (`keel/rooms/long_room/2026-10-24_IPS_edits_v2.md`;
  IPS 494 strict, pitch 47). Key fix: the shortfall line's timing (gap priced and set aside before the 2033 gift). Suggestions only.
- Wharton Week 4 email (filed 22 Oct): `competition/official/2026_27/wharton_email_week4_2026-10.md`. IPS is now an
  SMApply FORM, not a PDF ("all other requirements remain the same"); TIPS and STRIPS explicitly banned for both
  contributions, in the IPS and the Final Report.
- Wharton culture brief (23 Oct, Ray's idea that judges warm to "Wharton potential"): `keel/library/wharton_culture/BRIEF.md`
  = Wharton's history, values, student culture, judge quotes, traits Keel should SHOW (never say), clichés to avoid.
- Team Keel (22 Oct, Ray; made the repo's leaders on 23 Oct): `keel/` = six FICTIONAL personas who do the same
  competition and run the office; a new research-based diary episode every day (scheduled task). Their events are fiction and never go into Caplet's
  deliverables as Caplet's experience; their research findings may be used after re-checking.
- Full rules, dates, formats, portfolio and open items: `competition/COMPETITION.md` (single source of truth). Onboarding: `caplet/START_HERE.md`.
- Roster submitted (locked). All 11 WInS orders filled 7-8 Oct: iBond ladder IBTM/IBTO/IBTP/IBTQ/IBTR + T-bonds
  Feb-2037, May-2038, Nov-2039, Nov-2040, Nov-2041 + VT 167. 11/200 trades, cash $3,514. Official WInS value
  23 Oct: $305,557.66 (+1.85%); 15 trade notes on 11 trades (4 on cancelled orders). Read
  `competition/wins/2026-10-23_snapshot.md` instead of opening WInS. Plan: hold.
- 6 Oct Wharton email: Laura's real plan may use only WInS-listed stocks, ETFs and Treasury bonds. STRIPS-based
  numbers below and in `keel/library/insight_v1/` are superseded (banners added). The floor is IBTM.
- Public SMApply FAQ, live 20 Oct: TIPS and STRIPS are now listed as NOT permitted, the permitted list is "for BOTH
  contributions, the IPS and Final Report", and the public $5 stock floor is gone (the WInS session rules showed $3
  on 29 Sep) (`competition/COMPETITION.md` section 4; snapshot in `competition/official/2026_27/smapply_public_2026-10-20/`).
- IPS latest draft = Google Doc "IPS Report" tab "Version 5" (export in `caplet/google_drive/ips_report/`, 14 Oct).
  Read 19 Oct: the live Doc holds 10 pending AI suggestions (7 in Version 5) and [AI] text; the export predates them.
- IPS numbers rebuilt 16 Oct on the 15 Oct curve: `keel/library/ips_numbers_2026-10/IPS_number_sheet.md`. Ladder ~$294k
  (headroom ~$5.5k, over $300k on 1 Jan 2027 in ~1 in 3); range ~$145k-$168k; gift inside ~99%; coupon-reinvestment
  shortfall ~$21k if yields fall 2pt for good, not covered by what Laura kept in ~6-7% of paths. TEAM DECISION before
  6 Nov: state the risk / keep Laura's half to 2042 / hold a buffer from the 2028 deposit.
- Next (Sydney time first; the team is in Sydney, so count days in Sydney time): TNA due Sat 24 Oct 08:00 AEDT
  (Fri 23 Oct 5 pm ET); IPS + trading freeze Sat 7 Nov 09:00 AEDT (6 Nov ET); Final Report Sat 5 Dec 09:00 AEDT (4 Dec ET).
- Only Ray places/cancels WInS orders (7 Oct mis-click incident). Scheduled checks: `keel/routines/tasks/`.
- Team exports in `caplet/google_drive/` are snapshots; the Google Docs are the live copies.
- 2031 range numbers (17 Oct, WInS-only basis, model): `keel/library/range_2031/README.md`. Today's estimate: bottom
  $145k (the ~$150k IBTM floor rounded down: its payout is not fixed), top ~$170k (p5-p95 $145k-$195k); ~3 in 4 to reach the top, ~99% at least
  halfway. Ladder headroom fell to $1,913 (7bp) on the 16 Oct curve (cost $298,087), so the floor is not a fixed $150k.
- 17-18 Oct: AI exemplar v12 (Ray's request; a model to learn from, not for submission; plain formal prose, no scalpel style in the IPS) of the pitch, IPS and the three TNA
  reflections: `keel/library/blueprints/04_exemplar_ips_tna_17Oct.md`, also in the IPS Report Doc as SUGGESTIONS only
  (Version 5 + Trading Note Reflection tabs). Google Doc edits: suggestion mode only, never direct edits; Ray reviews all.
- Assistant review 30 Sep-15 Oct: keel/library/assistant_review_2026-10/ (AI-generated research, not for submission; start with its README and the 15 Oct team brief PDF).
- Assistant review 16 Oct: keel/library/assistant_review_2026-10/04_What_Stops_Us_Winning_16Oct2026.pdf (AI-generated research, not for submission; ranked to-do list in Part 1; evidence in oct16/).
- The Keel Office (23 Oct, Ray): one office of twelve rooms (Long Room, Noticeboard, Window, Library, Lab, Trading Desk,
  Courtroom, Laura's Room, Writing Room, Archive, Kitchen, Rooftop); the six desks became rooms, no paths moved. Map,
  people and agents: `keel/OFFICE.md` + `keel/office/office_map.svg`; room logs in `keel/rooms/`. Lab and Library run
  in the daily loop (`keel/pm/LOOP.md` step 6b), IPS-relevant only until 7 Nov unless Ray approves more.
- Caplet Research Office, now the Keel Office (18 Oct; merged 26 -> 18 agents on 19 Oct): `keel/office/` (README org chart, CHARTER house rules,
  LEDGER, outbox) + 18 agents in `.claude/agents/` (chief of staff, fact-checker, 16 specialists in 6 desks with no
  desk leads: Rules & Integrity, Numbers, Strategy & Risk, Client & Co-sponsor, Judging & Editorial, Records; each
  desk reports to a student role). Work is organised in three deliverable workstreams, `keel/office/workstreams/`
  1_TNA, 2_IPS, 3_FINAL_REPORT (requirements, owners, dated timeline, agents on duty, gates). `/office` skill, workflows
  `office-gate-check`, `office-judge-panel`, `office-work-order` in `.claude/workflows/`. Office answers named
  students' questions only, one page per memo. `keel/office/tools/textcheck.py`
  = word/char counts, curly quotes, exact-match check (overclaim list removed 26 Oct, BIBLE) for pasted notes.
- 16 Oct North Star memo (`keel/library/assistant_review_2026-10/04_North_Star_Memo_16Oct2026.md`): one idea ("commit only
  money she already owns"), one fact, one rule, one picture; IPS rule budget of 3 rules + 1 trade-off; curate, don't
  decorate, the growth story; adds word-list, name and "promise" decisions to vote set A (Sun 18 Oct), before the TNA.
- 16 Oct pre-mortem (`keel/library/assistant_review_2026-10/05_Premortem_Review_16Oct2026.md`): the live V5 (edited 16 Oct)
  added ~a dozen figures ($294k, $21k, 7%, $145k-$168k, "99 in 100") with no source in NUMBERS.md (lab items 02-05
  todo) and dropped the diversification and annual-review clauses; TNA reflections not started; Trade Log blank;
  ask Wharton what "required trading activity" means; school letter still to request. WInS book: hold.

## Working rules (from the team leader)
- Use only exact official Wharton materials and verified sources. No fictional clients, rules, rosters or data.
  Anything not verified is marked UNVERIFIED; never fill gaps from memory or "typical" rules.
- Research online and verify facts; cite URL + date. Network access was widened on 2026-09-27: primary sites load
  with curl, but the WebFetch tool is still blocked, so read pages with
  `.venv/bin/python keel/library/insight_v1/scripts/fetch_text.py URL [--grep "exact phrase"]`.
- AI may edit the file but only in suggestion mode whenever it is attempting to make edits on the Google Docs. AI do not have the rights to confirm or execute any trades. AI do not have the rights to submit our work. AI, or Claude, must complete the work to the highest of its capability, particularly the items that are going to be submitted. Caplet team wants knowledge: numbers, models, devil's advocate, trade checks, research/fact-checking. 
- Goal: top priority is reaching the Top 50 semifinals (chosen on the written Trading Notes, IPS and Final Report);
  the finale comes later. Keep deliverables plain-English (judges reward simple, elegant ideas). The assistant drafts
  when asked (AI DRAFT label), reviews drafts, checks trades and numbers; the team rewrites and submits.
- Repo is private (made private by Ray on 23 Oct 2026; it was public before). Do not commit student personal data
  (surnames, emails, birthdays) or rankings of teammates.

## Mandate (Ray, 2026-09-27)
The assistant has freedom to make decisions and choose its workflow, sticking tightly to the competition and the
materials provided, asking when information is needed, with the goal of reaching the semifinals. Everything that is
sent to the judges must be approved by the team. Deliverable help = verified numbers, checks, draft reviews and,
since 2026-10-16, labelled "[AI]" Google Docs suggestions that the team accepts or rejects.

## Team
Lessons from 2025-26 (Ray, no feedback received): strategy packaging was over-complex for the insight; the team traded
assets outside the trading rules. So: complexity must earn its place; check every trade against this year's rules and
approved list before placing it; client first. Team is Australian (use only if it earns its place). The team has a
supervisor/advisor who handles administrative work only (consistent with the rules: advisors may not make decisions;
all strategy decisions are the students'; worth noting in the Final Report's Articulation section).
Ray's personal goal: learn markets and client analysis; include plain-English "what this teaches" notes.
Ray (Team Leader), Ahaan, Darren, Harry, Eric, Young (6 students). Roster in `toolkit/config/team_roster.json`,
pending Wharton roster confirmation (due Oct 9; members locked after submission).

## Client: Laura Gao (official case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf`)
$300k start of 2027, +$150k start of 2028, no other flows before 2033. Ten fixed nominal $50k payments at start of
each year 2033-2042, portfolio-funded with "high degree of certainty" (no outside money). Operating reserve set aside
start of 2033; then a responsible facility contribution (Taiwan residency), preserving flexibility. In 2031 she gives
co-sponsors a dollar RANGE + confidence that must protect the payments; team drafts part of the fundraising text.
WInS P&L is NOT added to projections. Taxes, Taiwan legal and facility cost estimates are out of scope.
Structured in `toolkit/config/client_mandate.yaml` (human_approved: false) and `toolkit/config/wharton_private_2026_27.yaml`.

## Official deadlines (SMApply, 5:00 p.m. ET, no extensions)
Roster Oct 9 | Trading Notes Analysis Oct 23 (3 notes quoted exactly from executed WInS trades, <=100-word
reflections) | IPS Nov 6, 5:00 p.m. ET = Sat 7 Nov 09:00 Sydney (an SMApply FORM with two fields, 50-word pitch + 500-word IPS, no title page, no PDF format rules, no charts/links/citations;
updated instructions filed 27 Oct, BIBLE Book 7;
TRADING ENDS AND PORTFOLIO LOCKS; strategy frozen) | Final Report instructions Nov 9, 9:00 a.m. ET (Tue 10 Nov 01:00 Sydney) | Final Report + school
documentation Dec 4. Evaluation: Investment Strategy; Client Knowledge; Portfolio Analysis; Articulation of
Competition Experience; Creativity & Presentation. All three evaluated deliverables are judged together.

## Strategy status, as of 2026-09-28 (superseded by Current status above) (council work in `keel/library/council_2026-09-27/`, AI brainstorming)
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

## insight_v1 research run (2026-09-27/28; AI-generated research, NOT yet approved by the team)
Outputs in `keel/library/insight_v1/` (scope set by Ray: Trading Notes and IPS only; no Final Report or finale work):
`trading_notes_pack.md` and `ips_spec.md` (the two primary files: specifications and checklists, no drafted text),
`securities_and_allocation.md`, `why_us.md`, `strategy_changes.md`, `open_questions.md`; the final strategy spec is
`phase_E/E6_final_spec.md` (numbers reproduced by `scripts/E6_final_checks.py`). Process: 472 questions -> 48 survived
skeptic filters -> 12 audited specialists -> red teams -> chief strategist.
- Recommended design (REC, pending team vote; alternative ALT = the earlier 2031 lock): Jan 2027 the first deposit
  buys the ten payments (longest-dated first if short; any gap is the first use of the 2028 deposit). Jan 2028 the
  second deposit first completes the ladder, then buys a Treasury repaying $150,000 just before 2033 (the building
  minimum), and puts the rest (~$40k) in one world stock fund untouched to 2033. 2031: nothing traded; the range is
  the owned minimum up to minimum + half the fund's value that day. 2033: ladder = operating reserve; gift = minimum +
  half the fund (capped at the announced top); the rest stays hers. MODEL vs ALT: total facility+flexibility money
  p5/p50/p95 $182k/$207k/$250k vs $168k/$210k/$266k; worst historical 6-year window $169k vs $120k; costs: less stock
  (~9% of all money 2028-32), median gift $174k vs ~$186-188k.
- WInS: recommended book (ii)R = Laura's plan on 2 Jan 2028 scaled to $300k (IEF 23.5 / TLH 42.5 / building-minimum
  stand-in ~24.3% via the 15-Nov-2032 note or IBTM / VT 8.7%), every ticker pending the WInS listing and position-limit
  check. Three notes: TLH (supported + tested), building minimum (refined only if the REC/ALT vote is logged first),
  VT. Notes may be capped at 300 characters (test at zero risk first); notes cannot be edited.
- Readable outputs (2026-09-28): `keel/library/insight_v1/Team_Caplet_Strategy_Brief.pdf` = 27-page client-style report
  (executive summary, the plan with diagrams, every insight by research phase, decisions; built by
  `scripts/build_client_brief.py` + `scripts/brief_insights.py`); `Team_Caplet_insight_v1_research_record.pdf` = the
  full 831-page record. The real Nov-15 ladder cost more than $300k on 176 of 185 trading days of 2026 (173 = idealised).
  Branch `claude/stoic-planck-lih8tw` (PR #1) merged to `main` on 2026-09-28 at Ray's request.
- Verified corrections: the real Nov-15 STRIPS ladder costs $294,387 on the 2026-09-25 curve, headroom $5,613 (19bp),
  not $7.7k/27bp; it would cost more than $300k in about 1 in 3 modelled rate paths. The case pull quote is the case's
  words, not verifiable as Laura's; no Laura quotes in the Trading Notes or IPS. 2026-27 Competition Guide and
  Infographic PDFs filed in `competition/official/2026_27/`.

## Client insight (team docs reviewed 2026-09-27: `keel/library/team_materials/review_why_laura_and_public_profile.md`)
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
  `keel/library/verified_2026-09-27/official_curve_pv.py`.
- IEF effective duration 6.95y, TLT 15.31y, both 0.15% expense (fact sheets as of 2026-06-30) -> duration match
  64.8% IEF / 35.2% TLT.
- JPM 2026 LTCMA (data 2025-09-30): U.S. large cap 6.70% COMPOUND (7.94% arithmetic, 16.47% vol); AC World 7.00%
  compound (16.78% vol); EAFE 7.50%; U.S. intermediate Treasuries 4.00%; long Treasuries 4.90%; cash 3.10%;
  inflation 2.50%. Implication: the council scenario "6.7% geometric" is the right one (growth-first shortfall ~3%,
  its median facility ~$19-27k above lock-early, but a far worse downside; the lock-early case still holds).
VERIFIED 2026-09-27 by the insight_v1 run (primary pages; details in `keel/library/insight_v1/phase_A/`):
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
- [x] Re-ran strategy simulation on official inputs: `keel/library/verified_2026-09-27/strategy_mc.py` (2026-09-27).
      Base: Lock-early never misses a payment; 2033 surplus p5/p50/p95 $159k/$207k/$273k; 2031 floor median $165k.
      Growth-first: 3.2% miss; surplus p5/p50/p95 $20k/$226k/$540k; 13.7% miss if 2028 deposit is $75k, 40.8% if $0.
      Equity weight 50/60/70% in the sleeve: median $205k/$207k/$209k (barely matters).
- [x] Trading Notes blueprint drafted: `keel/library/blueprints/01_trading_notes_blueprint.md` (awaiting team approval)
- [ ] Team reads `01_chair_memo.md` + `round2_referee_ruling.md` (section 4: 12 concepts) and picks the strategy
- [x] (done, see above) Ultracode run to be launched by Ray in a NEW session with `keel/library/ultracode_prompt_v4_deep_strategy.md` (v4 FINAL, locked 2026-09-27: full context,
      fixed agent roster ~45-55 in phases A-F, 31 seed questions; supersedes v3)
      (question engine: case anomalies, why Laura, top-practitioner lens, her world, co-sponsors, judges, contrarian;
      so-what/anchor/adversarial filters; outputs to keel/library/insight_v1/). Start it on this branch; re-paste the
      team's two client documents (kept out of the repo). Allow primary domains first if possible.
      (v2 audit prompt `keel/library/ultracode_strategy_audit_prompt.md` superseded by v3 for now.)
- [x] Ultracode insight_v1 run executed 2026-09-27/28 (see section above; outputs await team review and votes)
- [ ] Team: read `keel/library/insight_v1/trading_notes_pack.md` and `ips_spec.md`; take the three gate votes (lock-early;
      REC or ALT; WInS book (ii)R) and log them before the first WInS order (target fills Fri Oct 2 ET, hard stop Oct 9)
- [ ] Team: open decisions and WInS checks listed in `keel/library/insight_v1/open_questions.md`
- [ ] Code: `report audit-ai` always passes (audits one hard-coded block); built-in $100k/25% sector defaults and the
      31-stock default universe marked "Wharton-approved" are not official

## Repo map
One-screen map: `README.md` (rewritten 23 Oct around Team Keel). Top level: `keel/` (Keel: members, episodes,
tea_room, road_to_semifinal, office/, routines/, library/ = all AI research), `caplet/` (the students' work: Drive
snapshots, deliverables, decisions, docs/AI_USE.md), `competition/` (official files; historical in
`competition/historical/`), `toolkit/` (September Python demo: `cd toolkit && pytest`, 64 passing; configs in
`toolkit/config/`), `archive/` (superseded, incl. `rab/`, `model/`, branch history). Agents: `.claude/agents/`.
