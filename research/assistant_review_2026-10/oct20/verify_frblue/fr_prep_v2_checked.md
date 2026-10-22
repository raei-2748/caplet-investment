# Final Report prep pack v2 (Team Caplet, written Tue 20 Oct 2026, about 10:40 Sydney)

> **CHECKED COPY (`oct20/verify_frblue/verify_frblue.md`, wave H, Tue 20 Oct 2026, about 11:15-12:30 Sydney).** An AI verifier
> (Claude Code) adversarially checked v2 and changed it only where it was wrong or stale; each change is marked **[checked]**.
> Official quotes, criteria, case lines, all §10 dates (zoneinfo) and most numbers hold; the live SMApply Deliverables and FAQ
> pages were re-fetched with cache-busting (byte-identical to the 19 Oct copies). Main changes: (1) five inputs got verifier
> banners after v2 was written (REC, ALT, RUB, AW2, CS) and AB was verified "fix before the team sees it" (VAA); (2) REC's
> banner caveats now carried into N2/N8/N9/N12 and §0 (top-reach % convention-dependent; V5 "equity Laura retains" reading
> gives option 1 about 1.4% / 3r about 0.07%; fee puts the agreed ladder at about $300.4k); (3) the fourth shortfall point is
> a **4.5-point** fall ($40,247), with VIN's $19,488 / $28,234; (4) privacy: the "two students named in no record" line and
> the per-student coverage table are replaced (VAA P1-P4); (5) R1's order is partly plan choice (VR §1h); (6) "judges told
> not to open links" and "no sentences on the glance page" are in BOTH 2022-23 and 2023-24; (7) shared 2025-26 headings
> narrowed to what two reports share; (8) case-study slot updated from `verify_case` (IBTM's own SAI, fee margin, IEF row);
> (9) fee stated as nominal vs today's value; (10) fork deleted (not "made private") before the repo goes private.

AI-generated research and planning (Claude Code, wave F). This pack is requirements, evidence locations, checklists and a
schedule. It is **not text to submit**. It holds no drafted Final Report, co-sponsor, reflection or Works Cited wording, and
no sample paragraphs. If the team uses any of it, record that use in the AI-use register now and in the Final Report's Works
Cited later (Wharton AI Policy: "If you use AI to assist you in any way during the competition, how you use it must be
recorded in your Works Cited pages", https://globalyouth.wharton.upenn.edu/ai-policy/, `oct20/ailog/web/ai_policy_20Oct.txt:377`).
Owners are roles from the operating plan; the team writes names against them in its own sheet. First names only; nothing
here ranks teammates.

**Supersedes** `oct19/frprep/final_report_prep.md` (v1, 19 Oct). Section 11 lists what changed and every v1 statement that
is now stale. v1 sections not repeated here (1.5 "do differently vs redesign", 4.5 source-list columns, 4.6 log fields)
still stand except where section 11 says otherwise.

**Every structural item is FORECAST.** The official Final Report instructions are "shared on November 9"
(`deliverables.txt:51`); the case says "released at the beginning of Week 7" (case:162-163), which is the same week (Mon
9 Nov is six weeks after the 28 Sep trading start). 9 Nov ET runs from **Mon 9 Nov 16:00 to Tue 10 Nov 16:00 Sydney**
(`oct20/verify_admin/verify_admin.md` §1b P6; re-checked with zoneinfo for this pack). Replace every FORECAST row on release.

**Short names**
- `S/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/`; `oct19/`, `oct20/` = folders under it.
- `case:n` = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`.
- `crit:n` = `/home/user/caplet-investment/competition/official/2026_27/smapply_public_2026-10-14/deliverables.txt` (criteria :55-59).
- `IPS:n`, `TNA:n`, `Guide:n` = the 2026-27 instruction texts in the same official folder.
- **[checked]** `WP3768` / `WP3778` = Wharton WordPress pages 3768 (2022-23 and 2023-24 Final Report specs) and 3778 (judging), as saved in `oct19/frprep/web/wp_3768_deliverables.txt` / `wp_3778_judging.txt` (VPW's copies in `oct20/verify_pw/txt/` have other line numbers). `VAA` = `oct20/verify_art_att/verify_art_att.md`; `VC` = `oct20/verify_case/verify_case.md`; `VREC` = `oct20/verify_reconcile/verify_reconcile.md`.
- File short names used below (all under `oct20/` unless marked):

| Short | File | Verification status (20 Oct) |
|---|---|---|
| PW | `pastwinners/past_winners_deep.md` | **Verified 20 Oct banner**; apply `verify_pw/verify_pw.md` E1-E19 |
| VPW | `verify_pw/verify_pw.md` | verifier |
| CH | `charts/charts_data_pack.md` + CSVs | **Verified 20 Oct banner**; apply `verify_charts_cr/verify_charts_cr.md` C-1, C-2, C-3, C-5, C-8, C-9, P21, P24 |
| VCC | `verify_charts_cr/verify_charts_cr.md` | verifier |
| RS | `reserve/reserve_schedule.md` | **Verified 20 Oct banner**; apply `verify_reserve/verify_reserve.md` §2 items 1-10 |
| VR | `verify_reserve/verify_reserve.md` | verifier |
| SE | `sensitivity/sensitivities.md` | **Verified 20 Oct banner**; apply `verify_ldi_sens/verify_ldi_sens.md` §4 |
| LDI | `ldi/ldi_second_opinion.md` | **Verified 20 Oct banner** (reserve rows WRONG; see banner) |
| VLS | `verify_ldi_sens/verify_ldi_sens.md` | verifier |
| CR | `clientread/client_readers.md` | **Verified 20 Oct banner** (VCC §C) + `verify_cosponsor/verify_cosponsor.md` E1-E12 |
| VCO | `verify_cosponsor/verify_cosponsor.md` | verifier |
| CD | `client/client_deep.md` | verifier note; apply `verify_client/verify_client.md` (version labels, privacy, two glosses) |
| VCL | `verify_client/verify_client.md` | verifier |
| REG | `ailog/ai_use_register.md` + `.csv` (33 rows R01-R33) | **Verified 20 Oct banner**; apply `verify_admin/verify_admin.md` §1a A1-A11 |
| OPS | `ops/operating_plan.md` | **Verified 20 Oct banner**; P1-P4 now applied in the file (AIP:465 relabelled as Pre-baccalaureate advice); P5-P7 not yet applied (see §10) **[checked]** |
| CM | `compliance/compliance_matrix.md` | **Verified 20 Oct banner**; apply VA §1c C1-C6 |
| VA | `verify_admin/verify_admin.md` | verifier |
| SP | `semis/semis_playbook.md` | **Verified 20 Oct banner** (VPW); note its judge-fit row still says "2022 to 2026" (should be 2024-2026) |
| TR | `tradecheck/trade_check_pack.md` | **Verified 20 Oct banner** (`verify_trade/verify_trade.md`) |
| IFX | `verify_ipsfix/ips_fix_list_checked.md` | checked copy (sound) |
| LG | `verify_learn/learn_guide_checked.md` | checked copy (uses the reconciled numbers) |
| DR2 | `verify_drill2/drill_v2_checked.md` | checked copy |
| NR | `numbers/numbers_refresh.md` | **verified** by `verify_infl_num/verify_infl_num.md` (VIN): confirmed with one correction (E1: 2-point holdings-basis gap $19,488, not $18,952) and caveats E2-E5 (±$500 curve-method uncertainty; WInS bond prices update once daily at US open) |
| NREG | `numreg/numbers_register.md` (63 rows) | no banner; re-run identical; **two rows superseded by VCC C-3 and reconcile** (see §4) |
| INF | `inflation/inflation.md` | **verified** by VIN: data confirmed; apply I1 (FX and building costs reinforce, not offset), I2 (VT $33,515 → $47,007 → $40,534), I3 (ladder real yield about 2.7-2.9%), I4-I7 |
| VIN | `verify_infl_num/verify_infl_num.md` | verifier (finished 20 Oct, after this pack's first pass) |
| TL | `timeline/timeline.md` | **verified** by `verify_tl_exp/verify_tl_exp.md` (VTE): sound; apply T1-T13 (shallow clone: 208 commits on 22 branches, 103 Claude cloud commits; insight_v1 run 50 commits from Sun 27 Sep 21:38 AEST; case PDF on the team Drive Thu 24 Sep 21:55 AEST; comment times are "last modified"; VT and Nov-2040 notes each hold a 13-word AI clause) |
| VTE | `verify_tl_exp/verify_tl_exp.md` | verifier (finished 20 Oct) |
| AB | `artic/artic_bank.md` (E01-E26) | **verified by VAA: "FIX BEFORE THE TEAM SEES IT"**: all quotes and 38 time conversions confirmed; apply privacy rewrites P1-P7 (no named "who has no record" lines, no pre-filled per-student table, they/them) and facts F1-F7, C1-C7 **[checked]** |
| ALT | `alternatives/alternatives.md` | **Verified 20 Oct banner** (`verify_rub_alt/verify_rub_alt.md`): numbers reproduce; re-base the "0.02% / 0 of 690" headline to REC §5; totals add undiscounted 2042 money (flatters ladder rows about $7k at the median); IEF/VGIT/SPTI and SGOV seen on WInS (team read 29 Sep) **[checked]** |
| LOCK | `lockin/lockin_2031.md` | no banner; self-validated (LOCK §0) |
| REC | `reconcile3r/reconcile_3r.md` | **Verified 20 Oct banner** (VREC, independent engine, two seeds): payment numbers confirmed within about 0.4 points; apply banner caveats (1)-(6): top-reach % convention-dependent, V5 retained-equity reading, fee, bug 9, 2042 return, timing **[checked]** |
| RT, RA | `redteam3r/redteam_3r.md`, `rangeaudit/range_audit.md` | superseded for headline figures by REC §5 |
| RUB | `rubric/rubric_scoring.md` | **Verified 20 Oct banner** (`verify_rub_alt`): quotes exact; scoring inconsistent in 6 lines; no Wharton scoring sheet exists; its line codes IS1-CP6 are AI labels, not Wharton's **[checked]** |
| AW2 | `askwharton2/questions_v2.md` | **Verified 20 Oct banner** (`verify_ask2/verify_ask2.md`): use its corrected batch-1 list (§9); Q11-Q14 and batch 4 (Q15-Q19) unchanged **[checked]** |
| EXP | `exposure/exposure_audit.md` | **verified** by VTE §2: facts sound; clean-up plan fixes X1-X4 (exemplar commits fetchable through the public fork by SHA; no "Allow forking" setting on a personal repo; Traffic data may vanish once private); also cites AIP:465 as competition policy, which VA P3 says is wrong |
| CS | `casestudy/casestudy_pack.md` (IBTM main, VT fallback) | **Verified 20 Oct banner** (VC): sound; apply E1-E16 (see §6) **[checked]** |
| v1 | `oct19/frprep/final_report_prep.md` | superseded by this file |

---

## 0. Read this first (what is new since v1)

1. **The evidence now exists for every case requirement, but almost all of it is AI MODEL output, unrebuilt by any student.**
   The reserve (RS), the range and gift (CH, REC), sensitivities (SE), alternatives (ALT), inflation (INF), client (CD) and
   co-sponsor readers (CR) were all built on 20 Oct on the 19 Oct curve. The index in §3 says where each fact is and which
   correction applies. None of it is report content until a student rebuilds the number on the 6 Nov close (§4).
2. **The "certainty" numbers changed meaning, not just value.** Three engines gave 0.02%, 0.41% and 6.2% for option 3r. The
   reconciliation (REC §0, §5) shows each rests on unstated plan rules. On one agreed basis: option 1 about 14.4-14.5% of
   paths with a short payment; 3r about 0.6%, worst about $3.3k; reach the 2031 top about three in four / under half (3r as written) / about three in four (3r with
   the top fix) [consistency fix 20 Oct, row 31]. Two plan rules decide which number is true (REC §7): rung sizing to own maturity with waiting interest as
   extra, and the 2033 reserve keeping the dollar shortfall plus $5k. These must be in the IPS by 6 Nov or the Final Report
   cannot use the low figure. **[checked]** REC is now verified (VREC), with caveats in its banner: the reach-top percentages
   rest on two unstated conventions (72 / 40 / 72.5% without them), so say "about three in four" / "under half"; V5 para 4
   ("an uncovered payment is funded from the equity Laura retains") read literally cuts option 1 to about 1.4% and 3r to
   about 0.07%, so the team must settle that reading on 27 Oct before quoting 14% or 0.6%; counting the 0.07% fee puts the
   agreed-basis ladder at about $300.4k and option 1's median minimum on the $140k/$145k edge; falls before 2033 never
   short a payment under the plan as written (they cost the gift and Laura's money).
3. **A model bug moved the reinvestment numbers by about 3%.** iBond funds were credited with their own yield as coupon (VCC
   C-3; VR §2 item 7; REC §6 bug 1; VIN E1 confirms $19,488 at -2 independently). Holdings-basis shortfalls for a permanent fall of 1/2/3/**4.5** points become **$10,095 /
   $19,488 / $28,234 / $40,247** (VIN E1; VCC rounds $1 lower) (not $9,537 / $18,952 / $27,718 / $39,759) **[checked]**, and option 1's short-payment chance 16.2% (not 15.6%) on
   the study basis. No option ranking changes.
4. **Past-winner evidence was corrected** (VPW E1-E4): two qualifier reports are public (Mochi 2024 Top 50 and InvestIQ 2024
   Global Finalist), with opposite styles, so "what the qualifier did" is not a rule; the 2022-23 page order differed from
   2023-24 (Portfolio-at-a-Glance was page 2); "Be creative!" is 2023-24 only; "disqualified for new material" is 4 of 5
   years. Structure must wait for 9 Nov.
5. **The 2025-26 Final Report section names look like an official template** (VPW §3b: two unrelated non-qualifier reports
   share Team Reflection, Portfolio-at-a-Glance, Report Details and Biggest Takeaways; "Team Decision-Making", "Team Growth
   and Learning" and "Challenges and Roadblocks" are confirmed in one of them (C3) only) **[checked]**. Raise the likelihood of an Articulation-style block in 2026-27 (F11).
6. **The rules text changed after v1 was written** (CM §2 Δ1-Δ6, confirmed by VA §0): the permitted list governs "BOTH
   contributions, the IPS and Final Report"; TIPS and STRIPS are named "NOT permitted"; the $5 stock floor is gone. v1 quoted
   `oct19/office/web/faqs_2026-10-19.txt` as "live", but that copy is the 16 Oct cache (CM §2 last paragraph; VA C5). Cash is
   on neither list (VCC P25). **SGOV was seen on WInS on 29 Sep** (team WInS Notes tab; VR §1g) but has no screenshot.
7. **The articulation record is mapped and thin.** AB lists 26 dated events with evidence strength (TL rows now verified
   with fixes, VTE); the journal stops 27
   minutes before the first trade (AB §1.1); no decision on record has a vote, attendance or dissent outcome (AB §1.3); named
   mentions of students are rare in team-written records, and no member has a per-student dated record yet **[checked:
   AB §1.2's named "no record" comparison is withdrawn (VAA P1, P4); it is also wrong, since the Team List and roster name
   every member]**. The back-fill session (AB §6) must run before Sun
   25 Oct.
8. **The AI record is ready to become a Works Cited**: 33 rows, 8 sessions, a tool inventory and a recommended structure
   (REG §3, §6; verified with fixes). Its commit counts came from a shallow clone: use **208 commits on 22 branches, 103
   Claude cloud commits** (VTE T1, "Same errors in the AI-use register"). Main's `docs/AI_USE.md:49` still holds the false "100% student"
   line and `:92` an untrue closing line (REG §4 items 1, 7).
9. **The schedule is now the operating plan's** (OPS §4c): Draft 1 Sat 21 Nov 20:00, Draft 2 and signed school letter Fri 27
   Nov 20:00, submit Wed 2 Dec 20:00, hard stop Thu 3 Dec 18:00. Fri 4 Dec is a Knox staff PD day, not a teaching day (VA P1).

---

## 1. Fixed facts (not forecast)

| Item | Source |
|---|---|
| Due Fri 4 Dec 5:00 pm ET = **Sat 5 Dec 09:00 Sydney**; no extensions; SMApply | crit:25, :28-29; zoneinfo |
| School documentation is a separate file, submitted with the report; "Do not wait until the last minute" | crit:52; template `SDT:1-28` (CM row 37: signed by a school administrator on letterhead, team leader listed first) |
| Purpose: "evaluate how it implemented its investment strategy and present its analysis and recommendations for achieving Laura's goals" | crit:50; case:157-160 |
| May say what you would do differently; may not redesign the strategy after observing results; strategy frozen at the IPS deadline | Guide:156-159; IPS:73-74; CM row 31 |
| Three deliverables evaluated together; one consistent strategy across all three | crit:27; case:161-162 |
| Projections start at $300k (2027) + $150k (2028); WInS gains and losses excluded | case:129-133; Guide:70-73; CM rows 39, 64 |
| Five criteria (Investment Strategy; Client Knowledge and Objectives; Portfolio Analysis; Articulation of Competition Experience; Creativity and Presentation) | crit:55-59 (re-fetched identical 19 Oct, v1 header) |
| Semifinal selection rests on "the strength of their Investment Policy Statement (IPS) and Final Reports" | Rules & Roles RR:459 (VPW §3d) |
| Permitted securities "for BOTH contributions, the IPS and Final Report": WInS-available stocks, ETFs, government/Treasury bonds; TIPS and STRIPS "NOT permitted"; "Anything other than the approved investments" not permitted | live FAQ SMF:44-47, :54-56 (CM Δ1, Δ3; VA §0) |
| AI use recorded in the Works Cited; AI work may not be submitted as the students' own | AIP:377 (competition section); RR:467-475 (REG §6.1); AIP:370 ethics (VA P3: AIP:465 is Pre-baccalaureate advice, not a competition rule) |
| Sources for IPS claims belong in the Final Report | IPS:123-125 |
| Out of scope: facility cost, budget, funding gap, business plan, taxes, Taiwan law | case:164-169 |

---

## 2. FORECAST: structure, with likelihoods (judgement, not data)

Built from WP3768 (2022-23 and 2023-24 blocks, re-read by VPW), WP3778 (judging), the two 2025-26 non-qualifier reports'
shared headings (VPW §3b), the 2026-27 case, Guide and criteria. Changes from v1 are marked **(v2)**.

| # | Element | Past evidence (corrected) | Likelihood | Prepare now | If wrong |
|---|---|---|---|---|---|
| F1 | TNR 12, double-spaced, 1-inch margins, PDF, size cap | 2022-23 and 2023-24 specs (doc or PDF, 5 MB) **[checked]**; 2026-27 IPS:112-122 (5 MB) | 95% | Template file set up by Sat 7 Nov | Reformat |
| F2 | No external links | 2026-27 IPS bans "external links" (IPS:123); the 2022-23 and 2023-24 specs both say judges are "instructed not to open any links" (WP3768; VPW copy `wp3768.txt:101`, `:466`); VA A11's "2023-24 only" is wrong **[checked]** | 90% | Every needed fact inside the report or Works Cited | none |
| F3 | Page range with floor and ceiling; out of range not reviewed or disqualified | 2022-23: 9-12 pp, "will be disqualified"; 2023-24: 10-13 pp excluding Works Cited, "will not be reviewed" (VPW §3b); Mochi 11 pp; 2025-26 range UNVERIFIED | 80% a range exists; 50% within 9-15 pp | Modules sized to grow or shrink (§2.1) | Cut to strongest modules |
| F4 | Title page: team name, First Name + Last Initial, WInS username; maybe school, advisor | IPS:84-100; 2023-24 spec | 85% | Team name exactly as on the roster; each first name as on the roster plus the roster surname's initial (IPS:96, sample IPS:130; verify_ask2 E11) (private; never in the repo) **[checked]** | Add fields |
| F5 | Separate "Works Cited", APA, AI cited with 1-2 sentences on how it was used | 2023-24 only (REG §6.1) | 75% | §7 structure | Same content, other style |
| F6 | Portfolio-at-a-Glance: WInS and recommended portfolio, tables or charts, no sentences | 2022-23 "tables or charts" (page 2); 2023-24 "visual tables or charts", "do not include information about your investment strategy on this page" (pp. 4-5) **(v2: order differs by year, VPW E4)** | 75% | Freeze-day capture; plan table by date; one scale factor | Tables inside the analysis |
| F7 | "Same or different" box on WInS vs recommended | 2023-24 | 50% | The mapping (CH §5; NREG H5) | One table note |
| F8 | "Report Details" as the bulk; "Be creative!" | 2022-23 pp. 5-12 (no "Be creative!"); 2023-24 pp. 6-13 with "Be creative!" **(v2, VPW E4)** | 70% | Modules (§2.1) | Rebalance |
| F9 | Summary page: 75-word pitch and 75-word uniqueness | 2022-23 and 2023-24 | 30% (pitch now in the IPS) | Re-use the IPS pitch idea only; students write any new limit | none |
| F10 | Advisor reflection (150 words), written by the advisor | 2022-23, 2023-24; Mochi had one | 50% | Tell the advisor now; give them the dated journal; advisor writes their own | none |
| F11 | Team reflection / growth / decision-making / challenges / takeaways headings | 2025-26: Team Reflection and Biggest Takeaways (plus Portfolio-at-a-Glance, Report Details) shared by two unrelated reports; decision-making / growth / challenges headings in one (C3) only (VPW §3b) **(v2: raised)** **[checked]** | 65% | AB event bank; journal from now on | Fold into Articulation |
| F12 | A Trading Notes section inside the Final Report | 2022-23 three notes; 2023-24 two; 2025-26 "Trading Notes Analysis (an ETF, a stock and a 'Team Choice')" in the report (PW §4.1); 2026-27 has a separate TNA | 15% | Nothing extra; never contradict the submitted TNA | Re-use the TNA picks |
| F13 | Audience: the portfolio manager; co-sponsor excerpt addressed to co-sponsors | 2022-23 and 2023-24 specs **[checked]**; case:4, :123-124 | 70% | Decide voice per part | Adjust |
| F14 | Charts and tables allowed in the body | 2022-24 specs; crit:59 "uses data effectively" | 90% | §5 | Convert to tables |
| F15 | Gate: required elements present and in range | WP3778:43 (2023-24), :83 (2022-23) **[checked]** | 85% | Release-day checklist (§10, Tue 10 Nov) | n/a |
| F16 | Instructions out Mon 9 Nov ET | crit:51; case:162-163 | 85% | Release-day drill; M11 Tue 10 Nov 20:00, fallback Wed 11 (OPS M11) | Keep building modules |
| F17 | Semifinal case study of "one stock or ETF", with no new material allowed | "one stock or ETF" 2023-24 to 2025-26; "disqualified" for new material 4 of 5 years (2022-23 on) (VPW E2, §3a) **(v2 count)** | 60% (2026-27 format UNVERIFIED) | §6 case-study slot in the report | none |
| F18 **(v2)** | Prohibited securities named in the report make it ineligible | 2022-23 and 2023-24 "Teams that include prohibited securities in their final report are not eligible for the Semifinals" (WP3778:41, :81) **[checked]**; 2026-27 permitted list covers the FR (CM row 22) | 70% | WInS search screenshot for every security named (§3B R27) | none |

### 2.1 Page budget (FORECAST; assumes a 2023-24-like 10-13 page range)

One double-spaced TNR 12 page holds about 250-280 words (v1 §0 item 8, R2 3.2). Unchanged from v1 except: the case-study
module is new (§6), and the reserve module grows because RS supplies a run-off table.

| Module | Pages | Contents (requirements only) | Owner role |
|---|---|---|---|
| Title | 1 | F4 fields | rules & format lead |
| Summary / reflections (if asked) | 0-1 | F9-F11 | editor; advisor writes own box |
| Portfolio-at-a-Glance | 1-2 | WInS book by holding and job; Laura's plan by date; one scale factor; "Long Equities" label explained once | trade-log keeper + rates analyst |
| A. Strategy and how it was implemented | 1-1.5 | thesis (from the submitted IPS); implementation scorecard against each IPS rule; C1 | team leader |
| B. Operating reserve and certainty | 1.5 | size, composition, run-off table, certainty standard and test, assumptions; C5 or a run-off table | rates analyst |
| C. Facility contribution and flexibility | 1 | the rule applied in named cases; what Laura keeps, its job, its bad-case size | growth & risk analyst |
| D. 2031 range, confidence, co-sponsor excerpt | 1.5 | C2; one confidence figure with method; currency; excerpt (students' text) | client & co-sponsor lead |
| E. Case-study holding | 0.5-1 | §6 (IBTM, with a shorter VT section) | rates analyst + client lead |
| F. Stress tests and alternatives | 0.5-1 | C3; one alternatives table | growth & risk analyst |
| G. Team process, challenges, growth | 1-1.5 | from AB and the decision log | historian |
| H. What we would do differently (no redesign) | 0.5 | v1 §1.5 two-column test | editor |
| Works Cited + AI record | separate (counted? UNVERIFIED; AW2 Q11) | §7 | historian |

---

## 3. Evidence index

How to read: each row says **what the report must show** (a requirement, not wording), **where the verified fact is**
(file and section), **which correction to apply** before use, the **decision it waits on** (D-codes from the 27 Oct vote set
B, `oct19/out/Caplet_Update_19Oct2026.md` §7b; DL-codes from OPS §2), and **status**. Status key: **MODEL** = AI model
output, unrebuilt; **CASE** = case text; **VERIFIED** = primary source checked by a verifier; **RECORD** = dated team
record; **NONE** = nothing yet; **STUDENT** = rebuilt or written by a student (none yet).

### 3A. By criterion (crit:55-59). Line codes IS/CK/PA/AR/CP are RUB §3 labels (AI opinion), used only as handles.

**Investment Strategy (crit:55)**

| Code | Phrase | What the FR must show | Evidence (file §) | Correction to apply | Waits on | Status |
|---|---|---|---|---|---|---|
| IS1 | "clear ... investment thesis" | The thesis exactly as the submitted IPS states it, followed by why only this design serves Laura (the portfolio alone funds fixed payments, case:91-92) | Required return 5.087% on the 2027 deposit alone, 1.046% with both (VCL §3 #1; NREG B2); "strategy up front, as rules" (PW §4.2) | "set of rules and guidelines" is 2023-24 only (VPW E3); compare 5.087% (annual) with a yield only on the same convention (NREG B2) | IPS text (students) | CASE + MODEL |
| IS2 | "creative" | One design idea that resolves a stated client tension, credited to its real origin | Floor + share of fund, capped (IFX §1.7 G5; G2 is the shortfall deduction) **[checked]**; the cap decides who carries the stock risk, not how much money there is (LOCK verdict 1, paraphrase); meaningful vs credible (CD §3 #4, VCL §3 #5) | AI-originated ideas must be credited (AB E04; REG R04, S14 strategy-name origin) | D6, D8 | MODEL / AI idea |
| IS3 | "disciplined planning across ... time horizons" | A rule and trigger for Jan 2027, Jan 2028, each January, 2031, Jan 2033, 2033-42, applied to the record; the two likeliest events (ladder over $300k; late/small 2028 deposit); decisions not to trade | Build-up T2-T3 (RS §3, VR §1a confirmed); deposit late/small (SE §4.1, VLS §2 confirmed); IBTR note line not crossed to 19 Oct (NREG C9); trade go/no-go cards (TR, verified) | RS test M is wrong ($3.0k not $4.2k; VR §2 item 1); add test G0, a fall during 2027 (VR §2 item 4) | D1, D5; DL-32/37 hold records | MODEL |
| IS4 | "... and cash-flow needs" | Each payment's money ready by its 1 January; where waiting money sits; reinvestment risk with its cover inside the portfolio | Waits 17 / 320 / 231 / 47 days (CH §1 table; VCC P3 confirmed); three standing rules (RS §0 item 5); SGOV seen on WInS 29 Sep (VR §1g) | Live V5 has no income-reinvestment rule (RS §2 conv. 4; VR §3 #10) and no parking rule (IFX S3) | IPS hooks S3, H5; D5 | MODEL + RECORD (WInS Notes tab) |
| IS5 | "appropriate diversification" | Diversification by funding purpose; one issuer stated as deliberate with its residual risk; one broad fund; alternatives weighed; WInS label quirk | Mix about 90% Treasuries (NREG H3); 2033 reserve 42.7% funds / 43.5% T-bonds / 1.2% 3r / 12.6% cash (VR §3 #6); Wharton feedback "Don't be afraid of diversification" 3/3 years (PW §5 #6, VPW §3b); alternatives table (ALT §3) | ALT verified with a re-base (its banner: totals add undiscounted 2042 money, about $7k at the median) **[checked]**; WInS pie "Long Equities" 61.6% date not recorded (NREG H3) | D7 | MODEL |
| IS6 | "maintains consistency with the team's IPS" | Joints check: one name, one floor definition, one shortfall order, one VT job list, one number basis, one scale statement; implementation evaluated rule by rule | Joints list (IFX §1.0 X5; CM row 21); "three in four reach the top" true for option 1 and 3r-with-fix only (REC §7); scale 0.644/0.645 not 0.667 (NREG H5; VCC P18) | v1's 0.645 was 16 Oct; TK2:246 "x 300/450" is wrong (NREG §2) | D0 (TNA), all of set B | NONE (student check) |

**Client Knowledge and Objectives (crit:56)**

| Code | Phrase | What the FR must show | Evidence | Correction | Waits on | Status |
|---|---|---|---|---|---|---|
| CK1 | "Tailors the strategy to Laura's circumstances" | Each key case fact linked to a design choice | Living costs outside the portfolio (case:61-63), no flows before 2033 (case:63-65), 2028 deposit "will contribute" (case:43-44) (VCL §3 #1-#3) | The deposit is timing, not doubt: V5's "depends on publishing and speaking income" drops two sources (VCL §3 #2) | none | CASE |
| CK2 | "priorities" | Payments first, then a responsible contribution, then flexibility, each with its rule, and what gives way first under stress | case:84-85 (the stronger priority cite) plus case:94 (VCL C7) | Cite case:84-85 with :94 | D2, D5, D6 | CASE |
| CK3 | "risk considerations" | Capacity and willingness, goal by goal | Two risk capacities (VCL §3 #3); "thoughtful risks", "appropriate balance" (case:68-74; VCC R1 confirmed) | Do not build willingness from her degree (CD §3 #2 trap) | none | CASE + INFERENCE |
| CK4 | "residency goals" | The payments as "reliable support for its early operations" (case:83) of a community place for five groups; 2031 credibility | VCL §3 #6; CD §3 #10 (community place); case:76-80, 83, 88 | Payments go "toward the residency's operating expenses" (case:88): not artist wages (CD §3 #10 trap) | none | CASE |
| CK5 | "thoughtful understanding of the client" | One or two sourced facts beyond the case that change a choice, never imported as plan inputs | Public facts re-fetched and confirmed (VCL §1g); "While the client is real, the financial scenario is developed specifically for the competition" (VCL §3 framing rules) | Privacy: never her residence, a sexuality label or pronouns (VCL §2); "Harvey Award finalist", not winner; never "fictional"; no Laura quotes (pull quote is the case's words, CLAUDE.md) | none | VERIFIED (public) |
| CK6 | "recommendations that can earn her confidence" | Explicit recommendations with number, date, basis, confidence and trade-off; she chooses, the team recommends one setting | CR §6 ranks 1-15 (with VCC §C and VCO fixes); "she chooses; we recommend" (VCL §3 #9); ALT §3 | CR R2 (NT$ is INFERENCE), R3 ("outside the plan's scope", not "not funded by her"), R6-R9 citation fixes (VCC §C) | D6, D9 | MODEL + CASE |

**Portfolio Analysis (crit:57)**

| Code | Phrase | What the FR must show | Evidence | Correction | Waits on | Status |
|---|---|---|---|---|---|---|
| PA1 | "understanding and effective use of investment concepts and tools" | Cash-flow matching, rate sensitivity, reinvestment risk, defined-maturity fund payouts, scenario and Monte Carlo methods, each answering one client question, each explainable by its owner | LG chapters 1-8 (checked copy with agreed numbers); ladder bases A-E (NREG §0a); DV01 about $290 per 0.01 point (NREG C4; VCC A1 $288.7/bp) | LG banner: duration definitions and VT-as-cover fixes | none | MODEL (study material) |
| PA2 | "integrates quantitative and qualitative analysis" | Each key number paired with a judgement (credibility, Taiwan costs, income timing) that visibly changes a choice | CR §6; INF §4d; VCO §3 | VCO E4 (matching claim), E5 (grants paid in stages) | D6, D8 | MODEL + VERIFIED |
| PA3 | "reasonable assumptions" | One assumptions table, each with source, date and basis | RS §6d A1-A15; INF §6 items 1-12; NREG I1-I5 | VR §2 items 2-3 (SGOV seen; fee omission about $1.4k ladder + $0.5k floor in nominal terms, about $0.93k today for the ladder, VLS §4 item 9 **[checked]**); JPM 2027 LTCMA figures UNVERIFIED (NREG I1) | DL-46 numbers card | MODEL + VERIFIED inputs |
| PA4 | "projections to evaluate funding reliability" | One certainty standard, how tested, assumptions, what absorbs each remaining risk; students' rebuild | RS §4-§5 (T4, T5A, T8) and §6b C1-C3, confirmed (VR §3 #2-#5); REC §5 agreed numbers; VCC C-3 fix | Quote REC §5/§7 forms, not 0.02% or 6% (REC §7); REC verified: apply banner caveats (2) retained-equity reading and (3) fee **[checked]** | D1, D3, two plan rules (REC §7) | MODEL |
| PA5 | "... the facility contribution" | Range + confidence + what good and bad markets do + protection of the payments | CH §2 seven cases (VCC P6 confirmed); NREG F1-F7; REC §5; LOCK (alternative) | VCC C-2 (one floor-yield convention), C-5 (cover order in the -2 row) | D1, D4, D8 | MODEL |
| PA6 | "... and financial flexibility" | What Laura keeps, why, where held, bad-case size, trade-off with the gift | NREG F8 (define first); LOCK §0 accounting fix (kept includes above-cap money); REC §5 kept medians; RS §7 R6 | Two "kept" definitions in use; pick one (VCC P21, C-5) | D2, D6 | MODEL |
| PA7 | "under varying market outcomes" | Named favourable / middle / unfavourable cases with every input; rates down for good; equity fall before 2031/2033; inflation; currency; joint stress | SE §2-4 (VLS §2 arithmetic confirmed); RS T9 stresses (VR §1d); ALT §5-6 (joint stress, history) | SE tornado framing (VLS §2; SE banner); 1984 path "about at the bottom", not "holds" (VR §2 item 6) | team defines cases (DL-47) | MODEL |

**Articulation of Competition Experience (crit:58)**

| Code | Phrase | What the FR must show | Evidence | Correction | Waits on | Status |
|---|---|---|---|---|---|---|
| AR1 | "teamwork, communication, and learning" | Who owned what, how disagreements were settled, working across time zones, what each student learned: true and dated | AB E01, E13, E16, E17, E22; OPS §1 role map; AB §4 coverage table (each student fills own row) | No roles on record yet (AB E01); consent before naming anyone (AB §2 rule 4) | DL-02 roles | RECORD (thin) |
| AR2 | "clearly explains the team's research ... process" | What was checked against primary sources and what changed; AI's role honestly | AB E02, E05, E06, E07, E12; REG §1 | "We discovered" stories flagged by AI first: iBond ETFs, sector myth, core idea (AB §1.4), and the yield-check rule (VAA F3) **[checked]** | none | RECORD + AI |
| AR3 | "... and decision-making process" | Options, evidence, who argued what, vote, date; decisions not to trade | AB E03, E04, E10, E17, E20; OPS §3a template | No vote on record anywhere (AB §1.3) | every DL row from M1 | NONE for votes |
| AR4 | "reflects meaningfully on the team's growth" | Before/after with cause; do-differently without redesign | AB E23, E24, E26; TL §3 TP1-TP8 | TL "often claimed but not turning points" (1 Oct "locked"; 13 Oct "LOCKED"; 2 Oct trades) (TL §3) | real student rewrite | RECORD + AI |
| AR5 | "... and response to challenges" | Challenge, response, result, lesson applied later | AB E07, E08, E11, E12, E15, E18, E19, E25 | E15 email arrival time unknown (TL G7); E19 rests on one AI-written line (AB strength) | back-fill session | RECORD (mixed) |

**Creativity and Presentation (crit:59)**

| Code | Phrase | What the FR must show | Evidence | Correction | Waits on | Status |
|---|---|---|---|---|---|---|
| CP1 | "compelling, well-organized narrative" | One storyline (problem, idea, proof, trade-off), order per the 9 Nov instructions | PW §4.1-4.2, §5 ("say less, plainly, and show why"); VPW §4 #8 | Page order changes by year; two qualifiers had opposite styles (VPW E1, E4) | 9 Nov | FORECAST |
| CP2 | "in an authentic team voice" | Student-written text; every author defends every sentence; true AI record | CM T1 rows 1-3; OPS §5 protocol; EXP §0.2 (47-63% of 12-word runs match a public AI file) | OPS now relabels AIP:465 as Pre-baccalaureate advice (fixed after v2) **[checked]**; use AIP:377 and AIP:370; EXP:97, :151 still quote that line as Wharton policy | DL-01 AI rule | NONE |
| CP3 | "uses data effectively to support conclusions" | Few numbers, each dated with basis; each chart answers one client question | CH (with VCC fixes); NREG golden rule (§0 item 2) | §4 re-price rule | D1 | MODEL |
| CP4 | "demonstrates original thinking" | An insight the team can show is its own (votes, reasoning), AI help credited | AB E04 (core idea AI-originated); REG S14 (name origin) | Claim originality only where the record supports it | votes | RECORD |
| CP5 | "and meaningful reflection" | Specific lessons tied to dated events | AB §7 weekly prompts; SP §4 N10 | none | journal | NONE |
| CP6 | "communicates Laura's potential facility contribution and investment uncertainty clearly and credibly to prospective co-sponsors" | §9 checklist met | CR §3-§4, §6; VCO §3; INF §4 | §9 corrections | D1, D8 | NONE (students write) |

### 3B. By case requirement (case:91-120, 129-169)

"IPS hook" = what must already be in the student IPS by Thu 5 Nov (internal) / Sat 7 Nov 09:00 (deadline), because the
strategy freezes (IPS:73-74). Codes refer to IFX (checked IPS fix list).

| # | Requirement (case line) | What the FR must show | Verified evidence (file §) | Correction to apply | IPS hook (IFX) | Status 20 Oct |
|---|---|---|---|---|---|---|
| R1 | Reserve set aside at the start of 2033, before the first payment or any facility contribution (94-95) | Order on 1 Jan 2033: reserve ring-fenced, then the $50k payment, then the gift, then what Laura keeps | RS §1 table row 1, §2 conv. 7, T3; RS §8 checklist | **[checked]** VR §1h: case:94-95 requires only that the reserve comes before the payment and the gift; case:101-103 puts the gift after the reserve; paying before giving and what Laura keeps are plan choices, so label them | H5 | MODEL |
| R2 | Recommend its **size** (96) | Size two ways: the holdings (which fund or bond pays which year) and the value on 1 Jan 2033 at two or more stated yields, with the payments' value beside it | RS T4: reserve $439,481 / $410,137 / $384,044 at 3/5/7% (no 3r), +$5,000 with 3r; payments $438,909 / $404,422 / $374,093 (VR §1b) | Use VR's 3% and 7% totals, not RS's $439,526 / $383,999 (VR §2 item 8); name the compounding convention (NREG B4) | H5 | MODEL |
| R3 | Recommend its **initial asset composition** (96) | Holdings on 1 Jan 2033 by type and share; why funds for 2033-36 and bonds after | RS T4/T6b: 42.7% funds / 43.5% T-bonds / 1.2% 3r / 12.6% cash (VR §3 #6); no WInS Treasury Feb 2031-Feb 2036 (RS §8) | IBTR is used because it matures closer than the Feb-2036 bond, not because WInS has no bond (VR §2 item 9) | H5, S4 | MODEL |
| R4 | Explain how composition **changes, if at all** (96-97) | Run-off with no trading; yearly maturity; where income goes; the 10.5- and 7.5-month waits in a named WInS-listed short-term Treasury ETF; replace-if-unavailable; duration falls; no move into stocks | RS T5A, T5-5a/5b, T6, T6b, T7 (VR §1c all confirmed); duration 3.48 to 0.40 years **including waiting cash** (3.96 to 0.86 bonds only) | "Duration" needs "including waiting cash" (VR §1c); SGOV listing: screenshot (VR §2 item 2) | S3 parking rule; income-reinvestment rule (absent from V5) | MODEL |
| R5 | **Define** a high degree of funding certainty (97-98) | One standard in plain words, consistent with reinvested coupons; no absolutes | RS §6b options C1 (matched + named residual risks), C2 (funded ratio passes at 3%), C3 (probability with history); banned words list (RS §6b) | C2 passes at 3% only with cover from 2028 (RS §6b); "covered at purchase" overstates (IFX O3) | O3; D3 vote | MODEL + options |
| R6 | Explain **how they evaluated** it (98) | Name the tools (ledger at flat yields, stress paths, Monte Carlo, history replay, funded ratio); say AI wrote the code; say which numbers students rebuilt | RS §5-§6; REC §5 and §8 limits; REG G1 grouping | Do not quote "0.02%", "zero in history" or "6%" (REC §7) | "name the test in principle" (v1 C6) | MODEL |
| R7 | **Identify the assumptions** (98-99) | Assumptions table with source, date, status | RS §6d A1-A15 | A5 fee omitted (about $1.4k + $0.5k, VR §2 item 3); A6 test M figure; A7 SGOV seen on WInS | S7 (return/inflation stated in words) | MODEL + VERIFIED inputs |
| R8 | How much she can **responsibly** contribute after the reserve (101-102) | The gift rule applied in named cases; share of non-reserve money given; the "responsible" test the team chose | CH §2 scenario table; NREG F3 (median gift about $165-170k, MODEL); CD §3 #4 | VCC C-2 floor convention | D6 | MODEL |
| R9 | Committing everything could limit **flexibility as the project develops** (102-103) | What she keeps, in which cases, what it is for (the project, not living costs) | VCL §3 #7; NREG F8; LOCK §0 kept definition; CR §6 rank 3 | V5 gives the kept half two jobs (VCL §3 #7) | D2 | MODEL |
| R10 | Recommend and **justify** the extent from strategy, projected outcomes, assumptions and goals (104-106) | Each of the four bases named; trade-off against a bigger promise; one recommended setting | SE §0, §4; ALT §3-4; REC §5 | ALT verified; re-base per its banner **[checked]** | D6, D9 | MODEL |
| R11 | No need to size a contingency fund or endowment (106-107) | A principle only; no sizing | CD §3 #5 trap | none | — | OK |
| R12 | In 2031 the 2033 value is uncertain; range, not one amount; overpromising damages credibility (109-116) | Range as a projection made now and re-set in 2031 by the IPS method; one valuation date; a re-quote rule | VCL §3 #4, #10; CR §6 rank 10 | none | G2, D8 | CASE |
| R13 | Recommend the **dollar range** (117) | Bottom by rule (named), top by rule; dated illustration | Bottom = (R - $3,700) rounded down to $5k: $145k (option 1) / $135k (3r) on 19 Oct; $145k survives to 2031 in 61-72% of paths (NREG F1); top median about $165k / $164k / $159k (REC §5) | Freeze the rule, not "$145,000" (NREG F1); top rule under 3r decides the reach-top chance (LOCK §8; REC §0); with the 0.07% fee counted option 1's median minimum sits on the $140k/$145k edge (REC banner (3)) **[checked]** | G2, G7 | MODEL |
| R14 | **State how confident** the 2033 contribution falls within the range (117-118) | One confidence figure, its method, kept separate from payment certainty | Gift inside the range 99.33-99.46% (number sheet, with the net-minimum rule; NREG F4); gift below the minimum 0.04% / 0.01% / 0.01% (REC §5); reach the top 77% / 45% / 76% (REC §5) | "Inside the range" and "reaches the top" are different statistics; "three in four" is false for 3r as written (REC §7); exact reach-top % depend on two unstated conventions (72 / 40 / 72.5% without them): say "about three in four" / "under half" (REC banner (1)) **[checked]** | G1 (no figure in IPS) | MODEL |
| R15 | Explain how **favourable and unfavourable** outcomes affect the amount (118-119) | Gift in named cases | CH §2 seven cases (middle top $169,686; 40% fall in 2032 gift $162,631; -0.5 point before Jan 2027 bottom $130,000; combined bad gift $132,129) (VCC P6 confirmed); NREG F7 (typical gift about -$7k after a 2032 crash) | Spot vs forward floor yield (VCC C-2); the -2 row's cover order (VCC C-5) | G4 (words only in IPS) | MODEL |
| R16 | The range must **protect the ten payments** (119-120) | The cover order runs before the gift, including after 2033; the post-2033 gap case | REC §5 payment-short figures; RS T5-G2 (fall to 3% in 2029); VR §2 item 4 (a fall during 2027 still takes $4.8k from Laura with 3r) | Soften "nothing is taken from her" to "for falls after January 2028" (VR §2 item 4); under the plan as written, falls before 2033 never short a payment (they cost the gift and Laura's money); payment gaps come from falls after Jan 2033 (REC banner (6)) **[checked]** | O1, K2, D5 | MODEL |
| R17 | **Draft part of Laura's fundraising materials** (123-124) | Students' excerpt, checked against §9 | §9 | §9 | — | NONE (correctly) |
| R18 | Assumptions on **investment performance** (146) | Return and volatility per asset, source and edition | VT 7.00% compound, 16.78% vol, JPM 2026 LTCMA AC World (NREG I1) | JPM 2027 edition out; figures UNVERIFIED (NREG I1); ask the advisor for the 2027 matrix | S7 | VERIFIED (2026 file) |
| R19 | **Timing of cash flows** (146) | Start-of-year flows; maturity waits; December fund payouts vs 1 Jan payments; WInS scale | case:59-60; CH §1 waits; RS A10 | iBond final-year cash not modelled (RS A4) | S3 | CASE + MODEL |
| R20 | **Outside funding** (147) | None relied on for payments; co-sponsors only for the facility | case:91-92; CM row 14 | Ban "her other assets/holdings" (CM row 14 as corrected by VA C2: accepted V5 says "her other assets") | O1 | CASE |
| R21 | Effect of **inflation on portfolio projections** (147) | Assumption, base date, nominal vs real | Ten payments $386,777 in Jan-2027 dollars at 2.5%; 2042 payment $40,036 in 2033 dollars (NREG B3; VCC A6); floor real loss 11.6% from Jan 2028 / 13.8% from Jan 2027 (INF §4c) | Name the base year and start date every time (INF §6 items 2, 7); VT illustration is $33,515 → $47,007 → $40,534 in Jan-2027 dollars, not the 16 Oct $33,170 (VIN I2); ladder real yield about 2.7-2.9% (VIN I3) | K6 (FR only) | MODEL / CALC (VIN confirmed) |
| R22 | Effect of **inflation on facility costs** (147) | A separate Taiwan building-cost assumption with source and date; what a fixed-US$ range buys by 2033; currency; who bears FX | Taiwan CPI +2.73% y/y Sep 2026; CCI +7.29% y/y, 3.63%/yr since the 2021 base; building group +5.93% (NREG I3-I4; INF §2); 2031 to 2033 drift about 4-7% at 1.9-3.6%/yr; FX + CCI 2-year band p5 -22% / median -5.2% / p95 +12.5% (INF §4a-4b) | "Facility costs are in NT$" is INFERENCE, not case text (VCC R2); FX and building costs **reinforce** each other (the correlation widens the band), they do not offset (VIN I1) | D8 currency | VERIFIED (DGBAS; VIN re-fetched) / HIST |
| R23 | **Financial flexibility** to preserve (147-148) | Principle plus model numbers for what she keeps | NREG F8; CR §6 rank 3 | Define "kept" once | D2 | MODEL |
| R24 | How outcomes affect the **recommendations** (148-149) | Whether any recommendation changes in a bad case; show the rules absorb it, or say which one changes | SE §0, §6; ALT §1 | none | — | MODEL |
| R25 | Projections from $300k + $150k; WInS P&L excluded (129-133) | Laura's figures never include WInS gains; WInS shown as implementation only | CM rows 39, 64; CH §0 item 2 | Never call the bond gain good news (CH §4 traps) | S8 (WInS clause) | CASE |
| R26 | The five "must" bullets (134-145) | Each bullet met and visible | CM row 63 | none | all | — |
| R27 | Permitted securities in the FR ("for BOTH contributions, the IPS and Final Report") | Every security named is WInS-listed, screenshotted; no TIPS, STRIPS, cash as a holding, derivatives, "STRIPS basis" | CM rows 22-23; AW2 §3 self-check H; SGOV seen 29 Sep (VR §1g) | Cash is on neither list (VCC P25); whether the ban covers TIPS/STRIPS-based ETFs is UNVERIFIED (AW2 Q9) | S4 | AT RISK in text |
| R28 | Out of scope (164-169) | No facility cost, budget, funding gap, business plan, taxes, Taiwan law | CM row 65 | none | — | OK |

---

## 4. Numbers the Final Report needs, and the 6 Nov re-price rule

### 4.1 The rule (one page)

1. **One valuation date: the Fri 6 Nov close** (the freeze). Every market-based figure in the report is re-run on that
   curve and stated once with that date (v1 §6; NREG §0 item 2; CH §8). The treasury.gov curve for 6 Nov publishes on the
   evening of 6 Nov ET, which is Sat 7 Nov morning Sydney; check the row exists before running (CH §8 step 1).
2. **No figure from another close in the same report.** 16 Oct, 19 Oct and 6 Nov values never mix. A normal day moves the
   ladder cost about $1.4-1.6k (NREG §0 item 4); 16 to 19 Oct moved it $1,778 (NREG C6).
3. **One named basis per quantity**, written once, used everywhere:
   - ladder cost and any "covered/enough" claim: basis D (NREG §0a), unless the team adopts maturity sizing, in which case
     the REC agreed basis (about $300k on 19 Oct, about $300.4k with the 0.07% fee counted; top-up about a coin flip, REC §7 and
     banner (3)) **[checked]**;
   - reinvestment shortfalls: the holdings basis **with the iBond coupon fix** (VCC C-3), or basis E, named;
   - the Jan 2028 floor yield: forward or spot, named on every chart (VCC C-2);
   - payment-short odds and reach-top: the REC §5 agreed basis for the option voted on 27 Oct, with the two plan rules
     stated (REC §7), plus the team's reading of V5's "funded from the equity Laura retains" (REC banner (2)) **[checked]**; seed and
     path count named;
   - scale factor: one value, defined as "WInS $300k / Laura's plan value after the 2028 deposit" (0.645 number sheet,
     0.644 charts; use **0.644** per the VCC banner **[checked]**; never 0.667) (NREG H5; VCC P18).
4. **Fees counted or the omission stated**: the 0.07% iBond fee is missing from the models (about $1.4k ladder + $0.5k
   floor on the same date in nominal terms; about $0.93k in today's money for the ladder, VR §2 item 3, VLS §4 item 9 **[checked]**). Every ladder basis also carries about ±$500 of curve-building uncertainty
   (treasury.gov uses a monotone convex method; the models interpolate linearly; VIN E3): one more reason to quote the
   rule, not the level.
5. **Students rebuild before quoting** (OPS §4c: Sat 7 - Thu 12 Nov, rates analyst + checker). Hand checks that must
   reproduce within a few dollars (CH §8 step 3; 19 Oct check values): C1 simple total ($298,641), C2 middle row ($169,686),
   C3 one rung (-2 points: $3,018); plus the annuity value ($405,391 at 5%, annual) and the required return (5.087%).
6. **Rounding and labels**: dollars to the nearest $1,000 in text; every model figure labelled MODEL with the model named
   once; probabilities in "about N in 100" form with their meaning (NREG §0b).
7. **After the 6 Nov re-price, Laura's projections do not move again.** Later closes appear only in the weekly WInS tracking
   (implementation evidence, C4). Real January 2027 prices are never analysis (SP §4 grey zones).
8. **Re-run commands exist**: CH §8 (refresh, number sheet, coupon study, charts_data), RS §2 "Reproduce", NREG §3, REC §9.
   Apply the VCC C-3 one-line fix (`coupon_options.py:141`) before the run, or label the output.

### 4.2 Numbers card spec (what to re-run on 6 Nov; 19 Oct values for orientation only, MODEL unless marked)

| # | Quantity | 19 Oct value (do not quote) | Source and correction | Re-run on 6 Nov? |
|---|---|---|---|---|
| N1 | Required return, 2027 deposit alone / both deposits | 5.087% / 1.046% a year (CALC) | NREG B2; VCC A6 | no (case-derived) |
| N2 | 1 Jan 2027 ladder cost and room | $297,162 / $2,838 (basis D); coupon-study basis $298,446 / $1,554; REC agreed about $299.9k (about $300.4k with the fee counted, REC banner (3)) **[checked]** | NREG C1; VR §1a (curve method alone moves it up to about $500); REC §5 | yes |
| N3 | Odds the ladder costs more than $300k on 1 Jan | 41% (D, sigma 1.0 point/yr); 43-45% coupon basis (45.3% at sigma 1.0) **[checked]**; 50% REC basis | NREG C3; REC §5 | yes, name sigma |
| N4 | Rate sensitivity | about $290 per 0.01 point | NREG C4 | yes |
| N5 | Jan 2028 floor cost (R = $150k) | $116,485 at 5.12% fwd (NR) / $116,843 at 5.108% (VCC) / $117,807 at 4.938% spot (CH) | VCC C-2: pick one | yes |
| N6 | Floor after a half-point fall before Jan 2027 | about $138,000 (D); bottom then $130k | NREG E2 | yes |
| N7 | Shortfall if reinvestment yields fall for good (1/2/3/**4.5** points) **[checked]** | $10,095 / $19,488 / $28,234 / $40,247 (holdings, fixed; VIN E1; VCC rounds $1 lower); basis E $11,005 / $21,287 / $30,902 / $43,731 | VCC C-3; VIN E1 (old $9,537 / $18,952 / $27,718 / $39,759 retired) | yes |
| N8 | Chance some payment is short (voted option) | option 1 14.4-14.5%; 3r 0.62-0.63% (worst about $3.3k); study engine 3r 0.010% | REC §5, §7 (plan rules a and b); if V5's "funded from the equity Laura retains" is read literally: option 1 about 1.4%, 3r about 0.07% (REC banner (2); decide 27 Oct) **[checked]** | yes |
| N9 | 2031 bottom | $145k (option 1) / $135k (3r); survives 61-72%; option 1's median on the $140k/$145k edge once the fee is counted (REC banner (3)) **[checked]** | NREG F1; REC §5 | yes (rule frozen) |
| N10 | 2031 top and 2033 gift medians, 1-in-20 low | top about $165k / $164k / $159k; gift $165k / $162k / $159k; low $135k / $133k / $131k | REC §5 | yes |
| N11 | Gift inside the range | 99.33-99.46% (number sheet); below-minimum 0.04% / 0.01% (REC) | NREG F4; REC §5 | yes |
| N12 | Gift reaches the top | 77% / 45% / 76% (72 / 40 / 72.5% without two unstated conventions: quote "about three in four" / "under half", REC banner (1)) **[checked]** | REC §5 | yes |
| N13 | 40% world-stock fall during 2032 | typical gift about -$7k (single path $170.5k to $163.2k) | NREG F7 | yes |
| N14 | What Laura keeps in 2033 | define first; REC medians $25.9k / $22.4k / $23.0k; number sheet p5 $0 | NREG F8; LOCK §0 | yes |
| N15 | Reserve value 1 Jan 2033 at 3/5/7% and funded ratios | $439.5k / $410.1k / $384.0k; rungs 99.65% / 100.90% / 102.10% | VR §3 #2-#3 | yes |
| N16 | Reserve mix 2033 and duration path | 42.7 / 43.5 / 1.2 / 12.6%; 3.48 to 0.40 years incl. cash | VR §3 #6 | yes |
| N17 | Plan mix 2 Jan 2028 | 66.5% payment Treasuries / 24.4% floor / 1.2% leftover / 6.9% VT of about $465k | NREG E5 | yes |
| N18 | Funded ratio with both deposits | 108.5-110.4% (basis-dependent) | LDI banner; VLS §0 item 3 | yes |
| N19 | WInS book at the freeze | the WInS screen value with its date; accrued-interest treatment UNVERIFIED; WInS bond prices "are updated once daily at U.S. market open" (FAQ), so the screen may lag the curve | NREG H1; AW2 Q12; VIN E5 | capture, not model |
| N20 | Income near and after the freeze | iBond payout about $600, ex/record Mon 2 Nov, pay Thu 5 Nov; T-bond coupons $1,538.75 on Mon 16 Nov | NREG H8; VCC A4 | record from WInS |
| N21 | Inflation figures (US 2.5%; real values) | $386,777; $40,036; 11.6% / 13.8% | NREG B3; INF §3-4 | no (assumption); re-check JPM 2027 |
| N22 | Taiwan CPI, CCI, FX | 2.73%; +7.29% y/y, 3.63%/yr; NT$32.445 per US$ (CBC 19 Oct) vs 32.40 (FRED 16 Oct) in CR | NREG I3-I5; VCC R17 (pick one dated rate) | yes (latest DGBAS release and one FX date) |
| N23 | 2028 deposit sensitivity | $75k: payment risk unchanged, median gift about halves; $0: payments short in about 55% of paths | SE §0 items 1-2 (VLS §0 item 4 confirmed) | yes (robustness test, not a forecast) |

---

## 5. Chart list (data pack `oct20/charts/` and its verifier)

Rules (CH §0; VCC §E; PW §4.4): each chart answers one client question; date and basis on the chart; MODEL labelled; built by
a student from data they can explain; no WInS pie chart; no performance chart; none in the IPS (IPS:123 bans charts and
citations, not numbers; IPS:68-70 says detailed projections are not expected: VCC P24). Core = C1-C3; optional = C4-C5
(page budget, §2.1).

| # | Client question | Form | Data files | Numbers it needs (§4.2) | Verifier fixes before building | 6 Nov action | Builder | Status |
|---|---|---|---|---|---|---|---|---|
| C1 (core) | "What pays each $50,000, and when?" | Dumbbell timeline, one row per payment, purchase to holding end to payment date; two money-in markers | `c1_payment_map.csv`, `c1_cash_flow_timeline.csv` | holding end dates; waits 17/320/231/47 days; optional rung costs (N2) | P21: the $25,340 "Laura keeps" excludes the $3,806 leftover; move the 2032-12-15 150,000 out of `money_in` (summing gives $600k, not $450k); Feb-2037 is 4.750% (CUSIP 912810PT9), two same-date CUSIP traps (VCC A4) | re-run costs if shown; dates do not move | rates analyst | Data VERIFIED (arithmetic); fixes pending |
| C2 (core) | "What can I tell co-sponsors in 2031, and how sure is it?" | Horizontal range bars from $0 per named case; dot for the 2033 gift; confidence beside it with its method | `c2_range_scenarios.csv` (14 rows), `c2_range_model_distribution.csv` | N9-N13 for the voted option | C-2 (one floor-yield convention, named on the chart); C-5 (decide whether above-cap money covers a shortfall before the gift is cut); show only the voted option; team defines its own cases (CH §2 traps) | full re-run | client & co-sponsor lead + growth & risk analyst | Data VERIFIED; method fixes pending |
| C3 (core) | "What could still go wrong with the payments, and who covers it?" | Paired columns per permanent fall (0/-1/-2/-3): shortfall vs stacked cover (leftover, reserve if voted, Laura's half; crash dash) | `c3_shortfall_and_cover.csv`, `c3_rungs_at_minus2.csv`, `c3_one_rung_rebuild_Nov2041.csv` | N7, N14; leftover; reserve value | C-3: shortfalls $10,095 / $19,487 / $28,233; uncovered option 1 at -2 $1,572 / $7,765 and at -3 $14,871 / $19,066 (VCC P10); the cover is not a flat line (VCC P13 confirmed) | full re-run with the fix | rates analyst | Data needs C-3 fix |
| C4 (optional) | "Did the bonds do their job while we held them?" | Two indexed lines (ladder + income vs value of payments covered), 8 Oct to 1 Dec; or the tracking ratio alone | `c4_wins_backfill_8-19Oct.csv`, `wins_tracking_template.csv`, `wins_tracking_pv_helper.csv` | weekly WInS captures; par yields each Friday | C-1: table and template use different PV methods (helper: 16/19 Oct tracking 99.75 / 99.85; bootstrap 99.64 / 99.77); size the lag as 0.15-0.36 points; replace `DATEVALUE` with plain date subtraction (C-8); Yahoo back-fill is not official and was rate-limited (VCC §F) | weekly rows from the 6 Nov freeze; add coupons back (16 Nov) | trade-log keeper | Template VERIFIED; method fix pending |
| C5 (optional) | "How does my portfolio change as the payments approach?" | Stacked columns from $0 on a true time axis: 2027, 2028, 2031, 2033 before/after, run-off to 2042 | `c5_plan_composition.csv`, `c5_wins_vs_plan_mapping.csv` | N15-N17; scale | inherits C-2; "held-to-maturity value at purchase yields (MODEL)"; the 2033 drop is the gift and release, not a loss | full re-run | growth & risk analyst | Data VERIFIED |
| T1 (table, not chart) | Portfolio-at-a-Glance mapping | Table | `c5_wins_vs_plan_mapping.csv` | WInS freeze capture; scale factor | one scale factor (C-9) | capture | trade-log keeper | — |

**Considered and not recommended as charts** (use a table or one line instead):
- SE tornado: mixes Monte Carlo medians, single paths and a real-dollar line, and ranks a case-fixed deposit cut against
  market moves (VLS §2; SE banner). If used, rank market drivers at comparable 1-in-20 settings and show the deposit as a
  robustness test.
- Reserve run-off: RS T5A/T6b already give a table; C5 covers the picture.
- LOCK "asymmetry" picture: an alternative considered, not the plan; one table row in the alternatives table.
- FX band: a dated footnote or one table row (CH §2 trap: do not convert the bars).

---

## 6. Case-study slot

**Why the slot exists (FORECAST).** Past semifinals required "a case study of one stock or ETF in your portfolio and how it
aligns with your overall strategy" (2023-24 to 2025-26; "and explain how" is the 2025-26 wording; VPW §3a; VC E11) **[checked]** and banned completely new material (4 of 5 years,
VPW E2). So the analysis must already be in the Final Report (SP §4 N1-N2). The 2026-27 semifinal format is UNVERIFIED (AW2
Q14, Q15). An individual Treasury is probably not eligible under "stock or ETF" (SP §5; AW2 Q18).

**Source: `oct20/casestudy/casestudy_pack.md` (CS), finished 20 Oct, verified by VC ("sound; apply these fixes", E1-E16) [checked].** It recommends IBTM as the main
case study and VT as the fallback; the students decide (CS §0 item 1). Its facts card (CS §2), prospectus quotes (CS §3a)
and holdings parse (CS §3b) are labelled VERIFIED against iShares pages "as of Oct 16, 2026"; its alternatives and risk
sizes are MODEL. Its consistency table (CS §12) agrees with NREG and LDI (floor $116.7k on CS's convention vs NREG E1
$116,485: a $213 convention difference; quote one).

**Slot requirements (no wording). The report section must already hold each item by 4 Dec (CS §11 C1-C11):**

| # | Item the report must hold (students' words) | Facts and where they are | Corrections / cautions |
|---|---|---|---|
| C1 | What IBTM is: index, end date, "does not seek to return any predetermined amount" | CS §2 (0.07% fee; 15 Treasury notes maturing 31 Jan-30 Nov 2032; ends "on or about December 15, 2032"; YTM 4.94%, SEC 4.98%, 12-month trailing 4.05% on 16 Oct); VCC A5 | Date every yield (DRILL's 14 Oct yields differ, CS §12); the Board "may extend the termination date" (CS §0 item 3) |
| C2 | The life of a share, from the 2027/2028 purchases to the 1 Jan 2033 payment, including where the cash waits | CS §3d (about half the notes mature by 30 Jun 2032; payout about 18 Dec on the precedent; 14-17 days before 1 Jan) | Name the start of the wait (17 days from 15 Dec, about 14 from the precedent payout); matured 2032 notes are mostly rolled into the remaining 2032 notes before cash, so the yield is locked on average to about 1 Jul 2032, not a cash cliff (VC E4) **[checked]** |
| C3 | The two jobs and the share split, payment first | CS §4b: 1,142 payment / 3,361 floor of 4,503 WInS shares; in Laura's plan about $37.1k (Jan 2027) and about $116.5k (Jan 2028) | One floor convention (VCC C-2); $37.1k assumes money earns its yield to 1 Jan ($37.2k at 0%; LDI basis $37.6k): name the basis (VC E16); 1,142 shares ≈ $26.6k at $23.33 face per share (VC E8) **[checked]** |
| C4 | Why there is no single 2032 Treasury | CS §4c (WInS lists none strictly between 15 Feb 2031 and 15 Feb 2036; the 15 Feb 2036 bond itself is listed, VC E7 **[checked]**; team check 29 Sep, not re-checked: UNVERIFIED today; the 6 Oct email removed STRIPS); IBTN is INSCORP, not an iBond | Re-check the WInS listing before 5 Nov (AW2 check H) |
| C5 | An alternatives table: Nov-2032 note, STRIPS (as excluded by the rules), a short Treasury ETF, an intermediate Treasury ETF such as IEF/VGIT (VC E6), the Feb-2036 bond, CDs **[checked]** | CS §5a-5c (all Treasury options within about $0.8k of each other on one curve; the differences are eligibility and what can vary; CD at the 1.41% national average costs about $23k more) | MODEL; best-market CD rates UNVERIFIED; STRIPS and TIPS are "NOT permitted" for both contributions (live FAQ SMF:54-55; VC E2); IEF-type fund about -$9k per 1-point rise just before the 2032 sale (VC E6, MODEL) **[checked]** |
| C6 | Payout drivers with sizes, and why the bottom is rounded down | CS §6 R3-R5 (floor reinvestment -$821 to -$3,166 at -1 to -4 points; final-year cash about -$1.4k if bills are 2 points lower); NREG F1 | The $3,700 margin is the model's choice, not a decision (CH §8 limits); with the 0.07% fee the margin at -2 points leaves only about $0.2-0.4k spare, and the $145k bottom still holds by about $1.6k (VC E3; VLS 1f) **[checked]** |
| C7 | Fund-level risks and the trigger (extension, closure, timing) | CS §6 R6-R7; LDI §9 T3 | **[checked]** VERIFIED in IBTM's own combined iShares Trust SAI dated 27 Feb 2026 (SEC 485BPOS 0001193125-26-064179), which also lets the Board merge or reorganise funds without a shareholder vote (VC E1); the iShares-site SAI covers no iBonds fund |
| C8 | One dated performance line and the rule that WInS P&L does not count | CS §7 (IBTM +0.99% since the 7 Oct fill to the 19 Oct close; VT -1.08%) | TRD:27; never good news for Laura (falling yields made her ladder dearer) |
| C9 | The "Long Equities" label explained once | CS §6 R12; NREG H3 | Date the WInS pie screen |
| C10 | A shorter VT section whose job list matches the IPS | CS §10 (Vanguard fact sheet as of 30 Jun 2026) | VT job list = D0-1 / D2 vote |
| C11 | The decision-log entry: why IBTM (or VT) | SP §5; OPS DL log | Log by early December (SP §14a item 1) |

**Team decisions this slot depends on** (CS §11): VT's job list (D0-1/D2); a reinvestment rule (LDI §6a); 3r yes or no (it
changes the floor's repayment to about $140k and the bottom to $135k); which holding is the case study.

---

## 7. Works Cited and AI record structure

**What Wharton has said** (REG §6.1, verified VA §0): AIP:377 "how you use it must be recorded in your Works Cited pages";
AIP:347 "including how and where students used AI-generated information"; RR:467-475 "Any AI-generated material included in
your report must be properly cited"; 2023-24 only: APA, a separate "Works Cited" page, "1-2 sentences on how you used that AI
tool", page count excluding Works Cited. The 2026-27 format comes on 9 Nov (AW2 Q11 if silent).

**Recommended structure until 9 Nov (REG §6.3 option D):** style entries per tool (A) plus a compact AI-use table (C).

| Part | Contents (fields, not wording) | Source in the record |
|---|---|---|
| 1. Sources | One entry per source: author/organisation, year, title, publisher/site, URL (no live link the reader must open), date accessed (Sydney), claim and FR section supported | v1 §4.5 columns; source types: case and official documents, treasury.gov CSV per date, iShares and Vanguard pages, JPM 2026 LTCMA, DGBAS CPI/CCI, CBC/FRED FX, List & Lucking-Reiley (2002) and any donor study used (VCO §3), Taiwan grant texts only with scope |
| 2. AI tool entries | Developer, year, tool, version/model or "not recorded", descriptor per style guide, 1-2 sentences of how (students write) | REG §3 tool inventory; §6.4 field table |
| 3. AI-use table | Entry, tool and version, dates, category, deliverable and section informed, kept/changed/rejected and how verified, register rows | REG §6.4 columns; grouping key G1-G9 + admin |

**Grouping key** (REG §6.4; students decide the final grouping): G1 Claude Code research/strategy/modelling; G2 Claude Code
exemplar and suggested wording; G3 Claude Code reviews, checks, mock judges; G4 Claude Cowork; G5 ChatGPT; G6 ChatGPT Codex
review; G7 AI browser agent in WInS; G8 Claude chat and artifact; G9 tools not yet identified; admin rows R01, R23, R25.

**Corrections before any row is copied** (VA §1a; VTE "Same errors in the AI-use register"): commit totals are 208 on 22
branches with **103** Claude cloud commits (the register's 202 / 97 came from a shallow clone); R05 (insight_v1) is **50
commits** from Sun 27 Sep 21:38 AEST; the executed VT and Nov-2040 WInS notes each hold a 13-word clause verbatim from the
30 Sep AI EXAMPLE notes, and two other notes share 8-9-word runs (VTE T12): these are YES-LOCKED rows; R29 has no row in any `docs/AI_USE.md` but is recorded in the branch
CLAUDE.md:19-21 and the PR #9 description (A1); PR #10 was merged by the same account that opened it (A2); 22 remote
branches (A3); 71 local trailer commits + 1 web squash-merge (A4); 3 rows YES-LOCKED and R19 possibly (A10); the "judges
will not open links" line is in the 2022-23 and 2023-24 specs, not in any 2026-27 text (A11 corrected) **[checked]**. Do not copy "Opus 5.5" to the Cowork entry (VA §1a note).

**Fixes to the existing log** (REG §4): retire `docs/AI_USE.md:49` ("100% student") and `:9`; fix `:25` (automatic logging
claim; the file holds 242 mock rows, VA A7); re-date rows 77-78 to Mon 19 Oct AEDT; add R27, R29 and every missing row
(REG §4 item 6); `:92` is untrue until the students' rewrite happens.

**Gaps only students can fill** (REG §5 S1-S17): which tools wrote IPS tabs V3/V4/Tab 10/V2 and Tab 15; the 6 Oct audit; the
WInS browser agent product and who supervised it; who typed each WInS note and which AI example notes were open (needed
before the TNA paste); who accepted each AI insertion; each student's own AI use on their own accounts; the strategy-name
origin. A blank is truer than a guess.

**Status markers** to carry into the table: YES-LOCKED (WInS notes and the mis-click; permanent), YES-DRAFT (IPS V5 and the
TNA reflections as AI exemplar v11), INDIRECT, NO (REG §0). The Works Cited is the only place the TNA and IPS AI use can be
recorded; logging AI text does not make it the students' work (REG §6.2 item 1; OPS §5C).

**Two-person check:** historian builds the table from the register; each student approves their own rows (OPS M14 DL-52).
Run the 5-word provenance overlap on the final text before sign-off (OPS §5B step 9).

---

## 8. Articulation evidence

**Source of events:** AB (26 events, each with record, AI role, "must confirm", "must NOT claim", strength), verified by VAA: apply its privacy rewrites and fact fixes before the team uses it **[checked]**. Cross-check with
TL §3 turning points TP1-TP8 (verified by VTE with fixes: T3 the ND "Big Idea" entry was written on or after 27 Sep, not 25
Sep; T4 the case PDF was on the team Drive from Thu 24 Sep 21:55 AEST, uploader not recorded; T6 Doc-comment times are
"last modified/resolved", so the 13 Oct comment order is not proven; T11 14 orders on the night of 6-7 Oct ET, 15 with VT) and the "often claimed, not a turning point" list (TL §3: 1 Oct "IPS
content locked", 13 Oct "content LOCKED", the 2 Oct trades that never happened).

**Five rules for any event** (AB §2): record first; memory second; AI role stated with a matching register row; consent of
any named teammate; no upgrading "a team member" to a name or an AI recommendation to a team decision.

| Event (AB) | Criterion tags (AB) | Evidence strength | Missing before use |
|---|---|---|---|
| E01 Team allocated; roles never filled | TW, GR | SYS + DOC | roles assigned and dated (DL-02) |
| E02 Benchmarking past semifinalists | RP, LE | SYS + DOC | who did it |
| E03 First plan and pre-mortem | RP, GR, DM | DOC (copied by AI) | authors; where the doc is |
| E04 Core idea from an AI council; the team "deferred" | RP, DM, GR | SYS + DOC / AI | who agreed and why; credit AI |
| E05 Students questioning AI output | RP, LE, AV, VS | DOC | whether the HAR model exists |
| E06 Session rules differ from the public guide | RP, LE | DOC | who found it |
| E07 No 2031-36 Treasuries, so iBond ETFs; IBTN is not an iBond | RC, RP | DOC | who found it; AI files proposed IBTM-IBTR by Sun 27 Sep 20:15 AEST (`5429887`); memo D3 (committed 29 Sep) repeats it; the IBTN trap is also in the AI run plan of 30 Sep (`35d2c3a`) (VAA F2) **[checked]** |
| E08 Stale prices, yield-check rule | LE, GR, RC | DOC + SYS | who; the rule and its 25bp threshold are also in AI files of 30 Sep (`282fa97`, `93a347e`), origin unrecorded (VAA F3) **[checked]** |
| E09 IBTR ticket error, after-hours spreads | LE | DOC | who |
| E10 2031 lock-in to floor + world fund | DM, GR | DOC / AI origin | "[who argued what]" (J:16) |
| E11 Planned Friday trades did not happen | RC, TW | SYS (by absence) | the remembered reason |
| E12 Sector-minimum myth traced | RP, LE, RC | DOC + SYS | who; AI fact check came first |
| E13 Darren's "copout" challenge | TW, DM, RC, VS | DOC (named, dated) | outcome and reasons |
| E14 Floor counted inside the reserve: wording fixed | LE, DM | DOC | who |
| E15 6 Oct email: WInS-listed only | RC, LE | AI (quote only) | arrival time, who read it (TL G7) |
| E16 The 12:30 AM open | CO, TW, LE | SYS + DOC | consent of the teammate in it |
| E17 First order pass, longest-dated first | DM, TW, VS | SYS / AI (who) | who typed and submitted |
| E18 Four orders cancelled and re-placed | LE, RC, DM | SYS | reasons for each re-placement |
| E19 AI mis-click; "only Ray trades" | RC, LE, GR, DM | AI + SYS (indirect) | how it was found; what it cost |
| E20 World-fund order, then "hold" | DM, LE | SYS / AI | who decided "hold" |
| E21 Roster; advisor's role | TW | AI | advisor admin only (CM row 52) |
| E22 Dashboard created, then empty | TW, GR | SYS | what it was for |
| E23 "Rewrite by ourselves" comments | AV, GR | SYS | usable only if a real, dated student rewrite follows |
| E24 "AI never writes" rule merged; no vote | GR, DM, AV | SYS / AI | a logged vote (DL-01) |
| E25 Outside judge feedback reported | RC, GR, CO | AI (second-hand) | who, when, what was shown; unpaid secondary adviser (CM row 26) |
| E26 Last year's lessons vs this year's trades | GR, LE | DOC + AI | last year's member list is at `2025_knox_wharton.md:76`; confirm with those students what they remember; name no one in the bank (VAA F6) **[checked]** |

**Before Sun 25 Oct:** the back-fill session (AB §6, 13 questions, 30-40 minutes, all six; answers marked "recalled on
<date>"). **From now on:** the weekly journal (AB §7 prompts; OPS §3b fields), the decision log within 12 h of each meeting
(OPS §3a), and a blank per-student record template, identical for all six in roster order, each student filling only their
own row (VAA P2 replaces AB §4's pre-filled table) **[checked]**; needed for any semifinal value statement, SP §7.

**Not usable as stories:** anything only in AI files without a team record; Laura "quotes"; any ranking of teammates; the
advisor making decisions (advisors may not, CM row 52); invented feelings or conversations (AIP:370, "invent teamwork and
experiential stories").

---

## 9. Co-sponsor excerpt: facts checklist (students write the text)

v1 X1-X15 stand with these changes. The excerpt is students' own text; this list is what it must get right.

| # | Check | Source / correction |
|---|---|---|
| X1 | Range in US$, with the date and basis of the projection; re-set in 2031 by the IPS method only if that re-set is in the IPS | case:109-117; IPS:73-74 |
| X1b (new) | A dated NT$ equivalent beside the US$ range, with its rate and date | CR §6 additions; pick one rate (VCC R17: 32.40 FRED 16 Oct vs 32.445 CBC 19 Oct vs 31.94 in CO) |
| X2 | Bottom set by a rule (rounded down because a fund's payout is not fixed); top by the stated rule | NREG F1; IFX G7 |
| X3 | One confidence figure for "the gift lands in the range", its method, kept apart from payment certainty | case:117-118; NREG F4 |
| X3b/X4b (new) | The reach-the-top chance must belong to the voted option: about 3 in 4 for option 1 or 3r with the top fix; under half for 3r as written (exact % are convention-dependent, REC banner (1)) **[checked]** | REC §5, §7 (v1 X4's "about 3 of 4" is option-1-only) |
| X5 | What a bad market does (2032 crash case) | CH §2; NREG F7 |
| X6 | Payments funded first and not by co-sponsors | case:91-92 |
| X7 | "Meaningful" as well as "credible", with no facility-cost estimate and no multiplier claim | case:110-112, 164-166; VCL §3 #5 |
| X8 | No facility cost, budget, funding gap or business plan | case:164-167 |
| X9 | No quote attributed to Laura | CLAUDE.md "Verified corrections" |
| X10 | No promise to exceed the top; no "guaranteed", "secure", "risk-free", "cannot miss" | case:114-116; RS §6b |
| X11 | Who bears USD/TWD moves, stated once; FX and Taiwan building costs reinforce each other (no natural offset) | CR §6 rank 8; INF §4d; VIN I1 |
| X12 | Research only with scope. List & Lucking-Reiley (2002): US households, a university campaign. Matching: raised giving in two US tests, larger ratios added nothing; where compared directly (Canada, Germany) matching did no better than announcing the lead gift; Karlan & List 2007 was inside a capital campaign | VCO E3, E4 (v1's and CR's "matching adds little" is wrong) |
| X12b (new) | Public Taiwan grants are paid in contract stages, with final settlement against receipts (not "reimbursement") | VCO E5 |
| X12c (new) | Never "16 times the largest NCAF grant" (it is about 5 times); the hccc.gov.tw reposts are Hualien County, not Hsinchu City | VCC §C note; VCO E1, E2 |
| X13 | Same numbers as the analysis sections and the IPS | crit:55 |
| X14 | Plain words, tested on an adult with no finance background | PW §5 (semifinal tips, 4/5 years) |
| X15 | Do not say the range "can't break"; the model figure is about 99 in 100, not 100 | NREG F4 |
| X16 (new) | When the contribution is paid (January 2033); the receiving organisation is outside the plan's scope; never imply Laura herself qualifies for Taiwan grants | CR §6 additions |
| X17 (new) | One valuation date and one re-quote rule for the 2031-33 campaign | CR §6 rank 10; D8 |
| X18 (new) | No matching offer, for a design reason (her gift does not depend on others), not "evidence says matching adds little" | VCO E4 |
| X19 (new) | What is not covered: operations above $50k a year, beyond 2042 (the case says "outside the scope of the competition", case:92-93; "outside the plan's scope" is VCC R3's paraphrase, not case text) **[checked]**, the falling real value of fixed payments | CR §6; VCC R3 |
| X20 (new) | If a Chinese version is made: identical numbers; "residency" as 駐村 / 藝術村, never 居留 (legal residence); fluent-speaker check | VCC R24 (UNVERIFIED register suitability) |
| X21 (new) | A central value beside the range is a team judgement (INFERENCE), not a finding of Du et al. | VCO §1, E10 (Du did not test central values) |
| X22 (new) | No slogan copied from CR (CR:192 "donor-tested message" label dropped) | VCO E12 |

---

## 10. Week-by-week build plan, Sat 7 Nov to Sat 5 Dec (Sydney), aligned with OPS

All times Sydney (AEDT). Sydney is 16 hours ahead of ET from Sun 1 Nov. Weekdays and conversions re-checked with zoneinfo for
this pack. Meeting numbers and DL codes are OPS §2. Where this plan differs from v1 §9, OPS wins (listed in §11).

**Dependencies that must be met before 7 Nov** (otherwise the Final Report cannot use the evidence in §3):
- Sun 25 Oct: AB back-fill session; AI register back-fill and banner on `docs/AI_USE.md:49` (OPS §4b); Traffic screenshotted,
  then the fork **deleted**, then the repo made private (EXP §0 item 5; VTE X1, X4) **[checked]**.
- Fri 23 Oct: school letter requested; ask who signs (OPS §4c; CM rows 28, 37).
- Tue 27 Oct: vote set B D1-D9 (which numbers and charts exist; the two REC plan rules if 3r is chosen).
- Thu 5 Nov: IPS hooks in the student IPS (§3B column "IPS hook"); WInS search screenshot for every security the IPS or
  report will name, including the waiting-cash ETF (AW2 §3 check H).
- Fri 6 - Sat 7 Nov: WInS records saved before and after the freeze, username cropped (OPS §4b last row).

| Week (Sydney) | Dates | Work (owner role) | Gate / output | OPS link |
|---|---|---|---|---|
| **W0 freeze weekend** | Sat 7 Nov from 08:00 (6 Nov 4 pm EST close; exact WInS cut-off UNVERIFIED, VAA C7) **[checked]** | Capture WInS Portfolio Summary, positions, Order and Transaction History (incl. cancelled orders), Trade Notes, Session Rules, May-2038 detail (trade-log keeper); download the 6 Nov treasury.gov row once published (rates analyst) | Freeze files in Drive; C4 row 6 Nov | OPS §4b, §4c |
| | Sat 7 - Sun 8 | Start the 6 Nov re-price (§4.1) with the VCC C-3 fix applied; checker re-derives the CH §8 hand checks | First numbers card draft | OPS §4c "Sat 7 - Thu 12" |
| | Sun 8 17:00 | **M10**: freeze debrief; FR evidence owners; release-day drill roles; numbers rebuild owners | DL-39, DL-40, DL-41 | OPS M10 |
| **W1 instructions** | Mon 9 16:00 onward | Instructions may appear from Mon 9 Nov 16:00 (9 Nov 00:00 EST); rules & format lead watches SMApply | Verbatim copy in Drive with fetch time | VA P6 |
| | Tue 10 by 18:00 | Release-day drill: line-by-line checklist of every "must", number and ban; map each line to §2.1 modules; list anything with no module; replace every FORECAST row of §2 | Checklist | v1 §1.4; OPS §4c |
| | Tue 10 20:00 | **M11** (Wed 11 if not out by Tue 18:00): structure vote mapped to the five criteria; section owners and backups; charts and tables list; Contact Us questions | DL-42 to DL-45 | OPS M11 |
| | Wed 11 | No 11 Nov ET curve (Veterans Day; it would have reached Sydney on Thu 12); immaterial, since the card uses the 6 Nov close **[checked]** | — | VCC A9 |
| | Thu 12 | Numbers card finished on the 6 Nov close; checked by a second student | One basis, one date | OPS §4c |
| | Fri 13 | Contact Us questions sent (AW2 batch 3, Q11-Q14, only for gaps), worded by a student | Sent | OPS §4c; AW2 |
| | Sat 14 from 08:00 | Weekly WInS capture (13 Nov close) | C4 row 13 Nov | CH §7 |
| | Sun 15 17:00 | **M12**: outlines (owners' own bullets); numbers card approved; 2031 range figures; Articulation story list confirmed by the students in each story | DL-46 to DL-48 | OPS M12 |
| **W2 drafting** | Mon 16 - Fri 20 | Section drafts from own bullets (OPS §5B); C1, C2, C3 built by owners; Portfolio-at-a-Glance tables; case-study section (§6); T-bond coupons paid Mon 16 Nov ET (in WInS from Tue 17 Sydney; crediting UNVERIFIED) | All section drafts in | OPS §4c |
| | Fri 20 | School letter target "in hand" (CM row 28); hard date stays Fri 27 | Letter status | §11.2 (v1 line 513) |
| | Sat 21 from 08:00 | Weekly capture (20 Nov close; first after the coupons; add income back) | C4 row 20 Nov | CH §7 |
| | **Sat 21 20:00** | **Draft 1** assembled; page count against the range; two scorers mark it before any AI check | Draft 1 | OPS §4c |
| | Sun 22 17:00 | **M13**: scorers' marks; gaps; cut list; letter status; AI issues-only check yes/no; co-sponsor excerpt v1 (students) checked against §9 | DL-49, DL-50 | OPS M13 |
| **W3 revision** | Mon 23 - Thu 26 | Revisions; joints check against the submitted IPS and TNA (IS6); "do differently" list (v1 §1.5); Works Cited and AI table drafted from REG; US Thanksgiving Thu 26 (markets closed) | No contradictions | OPS §4c |
| | **Fri 27 20:00** | **Draft 2**; **school letter signed and scanned** (students finish Thu 3 Dec) | Draft 2; letter file | OPS §4c; VA P1 |
| | Sat 28 morning | Weekly capture after the 27 Nov early close (time UNVERIFIED; a 1:00 pm ET close would be Sat 05:00 Sydney) | C4 row 27 Nov | CH §7 |
| | Sat 28 10:00 | **M14**: draft 2 review; provenance check (5-word overlap vs every AI file); each student approves their own AI-use rows | DL-51, DL-52 | OPS M14 |
| **W4 submit** | Mon 30 20:00 | Final text; Works Cited including the full AI record | Final text | OPS §4c |
| | Tue 1 Dec 20:00 | **M15**: format gate against the official checklist; each owner confirms "my own words"; approve | DL-53 | OPS M15 |
| | Wed 2 from 08:00 | Last weekly capture (Tue 1 Dec close) | C4 row 1 Dec | CH §7 |
| | **Wed 2 Dec 19:00-20:00** | **M16**: Ray submits the report and the school letter as a separate file; deputy watches; confirmation screenshot | Submitted (61 h early) | OPS M16 |
| | Thu 3 Dec 18:00 | Hard internal stop (Presentation Day; last student day) | — | OPS §0 |
| | Fri 4 Dec | Knox staff PD day (no student day); buffer only | — | VA P1 |
| | Sat 5 Dec 09:00 / 09:30 | Deadline (Fri 4 Dec 5 pm EST) / status check | — | OPS §4c |

**Schedule risks** (OPS §6): R12 letter not signed before Thu 3 Dec; R13 instructions late or different; R4 single points of
failure (leader = trader = submitter; one account owns the Drive); R6 AI wording entering the text; R16 record gaps; R15
overload ("no new AI research waves before 7 Nov"). Exam clashes flagged by VA P7 (M4, M7, the Thu 5 Nov text lock) are
before this window.

---

## 11. What changed vs v1, and every v1 statement now stale

### 11.1 What changed (summary)

| # | Change | Why | Source |
|---|---|---|---|
| 1 | Evidence index rebuilt on the 20 Oct verified files (§3), with a correction column | v1 pointed to 16-19 Oct files and "AI ONLY / NONE" statuses | §3 |
| 2 | Certainty and range figures moved to the REC agreed basis and the iBond coupon fix | Three engines disagreed; one model bug | REC §5; VCC C-3 |
| 3 | Structure forecast corrected for page order, "Be creative!", the 4/5 disqualification count, two public qualifier reports; F11 raised; F18 added | VPW E1-E4, §3b | §2 |
| 4 | Charts: C3 redrawn as paired bars; C4 method fix; one floor convention; data pack exists | CH; VCC | §5 |
| 5 | Case-study slot added, filled from the finished case-study pack (IBTM main, VT fallback) | SP §4-5; CS §11; F17 | §6 |
| 6 | Works Cited structure from the verified register | REG §6; VA §1a | §7 |
| 7 | Articulation evidence from AB E01-E26 instead of v1 S1-S21 | AB maps v1 S-codes; adds gaps and must-not-claim lines | §8 |
| 8 | Co-sponsor checklist extended (X1b-X22) and corrected | CR; VCO | §9 |
| 9 | Schedule aligned with OPS | OPS §4c; VA P1, P6 | §10 |
| 10 | Re-price rule and numbers card spec made explicit | NREG; CH §8; REC | §4 |

### 11.2 Every v1 statement now stale (v1 line numbers are `oct19/frprep/final_report_prep.md`)

| v1 line | v1 statement | Now | Source |
|---|---|---|---|
| 9-10 | crit "Re-fetched live 19 Oct ... identical" | Still true; but the FAQ copy v1 calls live is the 16 Oct cache | CM §2 last para; VA C5 |
| 22 | `FAQ19` = "live FAQ, 19 Oct" | `oct19/office/web/faqs_2026-10-19.txt` holds the 16 Oct text (lacks Δ3, Δ4, Δ6); cite the live FAQ (SMF) | CM §2; VA C5 |
| 37-40 | "for BOTH contributions" and "Any stock ... $5 ... or higher" (14 Oct snapshot) | The $5 floor is removed; TIPS and STRIPS are now named NOT permitted | CM Δ2, Δ3, Δ6 |
| 41-43 | Short-term Treasury ETF "must be WInS-listed and screenshotted"; cash UNVERIFIED | Still required; SGOV was seen on WInS on 29 Sep (no screenshot); cash is on neither list | VR §1g; VCC P25 |
| 44-47 | Ladder cost $298,940, room $1,060 (0.036 points), 47% odds (16 Oct) | 19 Oct: $297,162 / $2,838 / 41% (basis D); $298,446 / $1,554 / 45% (coupon basis); about $300k / 50% on the REC basis. Re-run on 6 Nov | NREG C1, C3; REC §5 |
| 48-53 | Post-2033 shortfall exceeds kept money in 7.7% of paths (median $3,181); kept p50 $23,999, p5 $0 | 6.5-8.0% (median about $3.2k); kept median $25.6k (D), p5 $0, and the definition must be chosen; the bigger fact is option 1's short-payment chance (14.4% agreed) | NREG F8, F9; REC §5 |
| 54-59 | Authorship evidence "got worse"; no AI-log rows 1-15 Oct | Unchanged on the record; register now lists 33 rows; R29 is in no AI_USE.md but is in a branch CLAUDE.md and PR #9 | REG §1; VA A1 |
| 60-62 | OFR full draft Sun 29 Nov vs this pack's Draft 1 Sat 21 / Draft 2 Fri 27 | Settled: OPS uses Draft 1 Sat 21, Draft 2 Fri 27 | OPS §4c |
| 63-67 | List & Lucking-Reiley verified | Still true; plus matching evidence corrected (raises giving in two US tests) | VCO E3, E4 |
| 92 | AI policy cite `oct19/office/web/ai_policy_2026-10-19.txt` | Fine; use AIP:377 and AIP:370; not AIP:465 (Pre-baccalaureate) | VA P3 |
| 93 | "FAQ19:59-62" for the permitted list | Cite SMF:44-47, :54-56 (live) | CM row 22 |
| 99 | F2 "judges are instructed not to open any links" as a 2026-27 expectation | 2026-27 IPS bans external links; the "instructed not to open" line is in the 2022-23 and 2023-24 specs, not in any 2026-27 text **[checked]** | WP3768; VA A11 (corrected) |
| 103 | F6 "please do not use sentences" as both years | **Still true [checked]:** both years say "please do not use sentences or paragraphs"; only the page position differs (2022-23 page 2; 2023-24 pp. 4-5) | WP3768 (VPW copy :171, :330, :502); VPW E4 |
| 105 | F8 "Be creative!" (both years implied) | 2023-24 only | VPW E4 |
| 108 | F11 likelihood 55% | Raised to 65% (2025-26 shared headings confirmed in two unrelated reports) | VPW §3b |
| 114 | F17 "no new material" and "one stock or ETF"; "One plain analysis of VT or one iBond fund" | "Disqualified" 4 of 5 years (not 5/5); "one stock or ETF" from 2023-24; the case-study pack recommends IBTM with a shorter VT section and lists 11 items the report must hold | VPW E2, §3a; CS §0, §11 |
| 132 | Release-day drill "Tue 10 Nov" | Instructions may appear from Mon 9 Nov 16:00 Sydney; drill still Tue 10 | VA P6 |
| 158 | "No 'decisions not to trade' log" | Still true; TR go/no-go cards and NREG C9 give the evidence for hold checks | TR; NREG C9 |
| 159 | Diversification evidence "VT's ~10,000 stocks" | 10,242 holdings, secondary source; re-check on Vanguard | VPW §3e |
| 168 | "residency goals" NONE | Evidence now in CD/VCL (insights 6, 10) | VCL §3 |
| 170 | Alternatives "AI floor tests ND:276-303 (STRIPS basis)" | AI alternatives table on the WInS basis exists (ALT §3; unverified); STRIPS-basis tests must not be cited | ALT; CM row 23 |
| 179 | `gift_2033` p5/p50/p95 $136,922 / $165,614 / $182,333 (16 Oct) | 19 Oct number sheet $139,260 / $166,411 / $182,868; REC agreed median $165k / $162k / $159k | CH §2; REC §5 |
| 180 | `laura_kept_2033` p50 $23,999 | $25,605 (D, 19 Oct); define first | CH §3; NREG F8 |
| 214 | C2 "$439k at 3%, $405k at 5%, $376k at 7%" as the reserve size | These are the **payments'** value (annual compounding). The reserve's holdings value is $439.5k / $410.1k / $384.0k (semiannual, VR) | NREG B4; VR §1b |
| 215 | C3 "no 2033 composition table" | RS T4/T6b gives one (42.7 / 43.5 / 1.2 / 12.6%) | VR §3 #6 |
| 216 | C4 "parking rule missing" | Still missing; also the income-reinvestment rule is missing from V5 | RS §2 conv. 4; VR §3 #10 |
| 226 | C14 "about $145k to $166k typical"; "$145k bottom held in 56-67%" | 61-72% (19 Oct); top medians about $165k / $164k / $159k by option | NREG F1; REC §5 |
| 227 | C15 "MODEL 99.25-99.4%"; "three of four" a different statistic | 99.33-99.46%; reach-top 77% / 45% / 76% by option | NREG F4; REC §5 |
| 228 | C16 "floor about $136k after a half-point fall" | about $138k (19 Oct, basis D) | NREG E2 |
| 235 | C23 Taiwan CPI +2.04% (Aug), CCI +6.53% y/y, 3.54%/yr | Sep 2026: CPI +2.73%; CCI +7.29% y/y, 3.63%/yr since the 2021 base; building group +5.93% | NREG I3-I4; INF §2 |
| 251-284 | Decision log back-fill rows (DL A1-A21) and missing decisions | Superseded for stories by AB E01-E26; new decisions use OPS DL-01..DL-54 | AB; OPS §2 |
| 297 | W6 "$3 vs $5" | Public $5 floor removed; re-screenshot Session Rules (the $3 may have changed, UNVERIFIED) | CM row 43 |
| 300 | W9 short-term ETF listing | SGOV seen 29 Sep; BIL, SHV unchecked | VR §1g |
| 303-305 | Coupons "on 15 Nov"; iBond distributions "dates UNVERIFIED" | Coupons paid Mon 16 Nov (15 Nov is a Sunday); iBond ex/record Mon 2 Nov, pay Thu 5 Nov, about $600; WInS crediting UNVERIFIED | NREG H8; VCC A9 |
| 308-326 | Weekly tracking template (v1 §4.3) | Replaced by CH §7 template with formulas; fix C-1 and C-8 first | CH §7; VCC |
| 330-348 | AI-use record fields and back-fill list | Replaced by REG (33 rows) and OPS §5C log fields | REG; OPS |
| 388 | C3 "lines for what Laura keeps" | Paired bars; the cover shrinks as the shortfall grows | CH §3; VCC P13 |
| 390 | C5 allocation 66.9 / 24.4 / 0.8 / 6.8% | 66.5 / 24.4 / 1.2 / 6.9% (19 Oct) | NREG E5 |
| 406 | P1 "simple method about $1.4k above the bootstrap on 15 Oct" | 19 Oct: simple $298,641 vs D $297,162 (about $1.5k) | CH §1 |
| 408 | P3 floor "$116,830 on the 16 Oct forward yield 5.06%" | $116,485 at 5.12% (NR) / $116,843 at 5.108% (VCC) / $117,807 spot (CH): pick one convention | VCC C-2 |
| 409 | P4 VT 2 Jan 2028 p5/p50/p95 $19.7k / $31.8k / $42.4k | $20.3k / $32.3k / $42.8k (19 Oct, D) | NREG E6 |
| 410 | P5 inside the range 99.25-99.4% | 99.33-99.46% | NREG F4 |
| 411 | P6 shortfalls $10,952 / $21,185 / $30,753 | Basis E $11,005 / $21,287 / $30,902; holdings basis (fixed) $10,095 / $19,488 / $28,234 **[checked]** | NREG D1; VCC C-3 |
| 412 | P7 "$439k / $405k / $376k" as the reserve value | Payments' value (annual); reserve holdings $439.5k / $410.1k / $384.0k | NREG B4; VR §1b |
| 415 | P10 7.7% / $3,181 | 6.5-8.0% / about $3.2k | NREG F9 |
| 416 | P11 p50 $23,999 | $25.6k (D); definition first | NREG F8 |
| 417 | P12 scale "$464,817; factor about 0.645" (16 Oct) | 0.645 ($464,973, 19 Oct) or 0.644 (charts $465,797); never 0.667 | NREG H5 |
| 421-422 | Fund fees "VT 0.06%" only | Add the omitted 0.07% iBond fee (about $1.4k + $0.5k nominal; about $0.93k today for the ladder) **[checked]** | VR §2 item 3; VLS §4 item 9 |
| 433 | History check "June 1984: $38,581" | Do not quote one "worst in history" figure; values range $26.9k-$49.2k by method, and the large ones are artefacts of applying 1984's fall to a 5% curve | NREG D2 |
| 446 | X4 "at the top in about 3 of 4 paths" | Option-dependent (§9 X3b/X4b) | REC §5 |
| 454 | X12 study scope list | Extended (§9 X12-X12c) | VCO |
| 457 | X15 "99.25-99.4%" | about 99 in 100 (99.33-99.46%) | NREG F4 |
| 476 | S9 "Darren challenged ... EWT and GLD" | Still true (AB E13); outcome still blank | AB E13 |
| 478 | S11 "AI re-ran numbers (unrecorded in AI log)" | Arrival time of the email unknown; whether it came before the IBTM order decides the "refined" label | TL G7; AB E15 |
| 481 | S14 mis-click rule "only Ray places or cancels" | Strength: one AI-written line plus an identical re-placement (indirect) | AB E19 |
| 484 | S17 "true mix about 91% Treasuries" | about 90.2% of the 19 Oct book | NREG H3 |
| 485 | S18 AI rule "merged 19 Oct" | Still no team vote on record (DL-01 due M1) | AB E24 |
| 513 | D11 "Fri 20 School letter in hand" | OPS hard date Fri 27 Nov (signed and scanned); keep Fri 20 as a target | OPS §4c; CM row 28 |
| 518 | D16 "Wed 25 Works Cited and AI record complete" | OPS: drafted in W3, approved at M14 Sat 28, final Mon 30 | OPS §4c |
| 524 | D22 "Tue 1 Dec gate"; D23 Wed 2 submit | Same in OPS (M15, M16) | OPS |
| 526-527 | D24 "Thu 3 Dec buffer (Knox term ends)"; D25 Fri 4 buffer | Thu 3 Dec = Presentation Day, last student day, hard stop 18:00; Fri 4 Dec = staff PD day | VA P1 |

---

## 12. Still UNVERIFIED or open (affects how the report is built)

- The 2026-27 Final Report structure, page range, Works Cited format and whether it counts (all F-rows; AW2 Q11, Q13).
- The 2026-27 semifinal format and case-study rule (AW2 Q14, Q15, Q18).
- Whether WInS counts accrued interest in its total and when it credits coupons and iBond payouts (NREG §4; AW2 Q12).
- SGOV / BIL / SHV listing screenshots; whether the 2.000% Nov-2041 or 5.000% May-2037 bonds are listed (AW2 check H).
- Whether cash may appear in Laura's plan (AW2 Q8); whether the TIPS/STRIPS ban covers ETFs built on them (AW2 Q9).
- JPM 2027 LTCMA AC World and inflation figures (NREG I1-I2).
- **[checked]** REC §5 payment numbers are verified (VREC), but two items stay open: the V5 "equity Laura retains" reading and the
  top-reach conventions (REC banner). RUB (AI opinion; 6 lines scored inconsistently), ALT, CS and AB are verified with fixes
  (verify_rub_alt, VC, VAA). LOCK has no verifier. INF, NR and TL are verified with corrections (VIN, VTE).
- Whether WInS still lists no Treasury strictly between 15 Feb 2031 and 15 Feb 2036 (team check 29 Sep only; CS §13; VC E7).
- Release hour of the 9 Nov instructions; the 27 Nov early-close time.
- Whether staff will sign the school letter on Fri 4 Dec (PD day) (VA P1).

## 13. Files

- This pack: `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/frblue/fr_prep_v2.md`.
- Inputs: every file in the short-name table at the top (all under `oct20/`), plus `oct19/frprep/final_report_prep.md` (v1),
  `oct19/out/Caplet_Update_19Oct2026.md` §7 (vote set B), and the official texts in
  `/home/user/caplet-investment/competition/official/2026_27/`.
- Checks run for this pack: all Sydney/ET conversions and weekdays in §10 with Python zoneinfo; $386,777, $40,036, $33,681,
  11.6% / 13.8%, 0.6452 / 0.6441 / 0.6667 and the Week-7 date recomputed (match the sources).
