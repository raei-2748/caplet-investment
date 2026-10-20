# Team Caplet operating plan, Tue 20 Oct to Sat 5 Dec 2026

> **Verified 20 Oct (`oct20/verify_admin/verify_admin.md`): all time conversions and weekdays correct; fixes applied in this copy:** Fri 4 Dec is a Knox staff PD day (Thu 3 Dec = last student day); the backup trader is no longer the trade-log keeper (two-person rule); DL-06 (decision rule) is voted first at M1; AIP:465 ("Don't use AI for personal reflection") is Wharton advice for Pre-baccalaureate courses, NOT a competition rule - use AIP:377 and AIP:370. Not yet applied: the FOMC 2:00 pm time is the usual time (not on the calendar page); "9 Nov ET" can land Mon 9 Nov 16:00 Sydney onward; exam clashes under the plan's own rule also hit M4 (Business Studies next morning), M7 (Legal Studies next morning) and the Thu 5 Nov text lock (Physics exam) - anyone sitting them votes in the chat. Also add "deputy ≠ historian".


AI-generated process plan (Claude Code, Tue 20 Oct 2026). It contains roles, dates, agendas, blank templates and
checklists only. It drafts no sentence for the TNA, IPS, pitch, Final Report, journal or co-sponsor text. If the team
uses it, log it in the AI-use record (row "L21" in `oct20/timeline/timeline.md:294`) and later in the Final Report's
Works Cited (Wharton AI Policy: "If you use AI to assist you in any way during the competition, how you use it must be
recorded in your Works Cited pages", `oct19/office/web/ai_policy_2026-10-19.txt:377`).

**All times are Sydney** unless marked ET. Sydney is 15 hours ahead of ET until **Sun 1 Nov 17:00 Sydney** (02:00 EDT,
when US clocks go back), then 16 hours ahead. US market hours in Sydney: 00:30-07:00 until then, 01:30-08:00 after.
Checked with Python `zoneinfo` (`oct20/ops/scripts/tz.py`). Every Wharton deadline lands on a **Saturday morning** in
Sydney. Nobody needs to stay up for the US open: "You are not expected to stay awake during the night to trade"
(`OFF/smapply_public_2026-10-14/trading.txt:52`).

**Short forms.** `oct19/`, `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`.
`U19` = `oct19/out/Caplet_Update_19Oct2026.md` (the fact-checked 19 Oct update). `TL` = `oct20/timeline/timeline.md`.
`DLR` = `oct19/notes/decision_log.md` (decision log rebuilt from records). `OFF` =
`/home/user/caplet-investment/competition/official/2026_27/` (`TNA:n`, `IPS:n` = the instruction texts;
`deliv:n` = `smapply_public_2026-10-14/deliverables.txt`). `AIP:n` = `oct19/office/web/ai_policy_2026-10-19.txt`.
`L10` = `/home/user/snap/main/research/assistant_review_2026-10/oct16/lenses/L10_team_process.md` (quotes from the
Wharton Rules & Roles page, accessed 16 Oct).

---

## 0. The calendar this plan sits in (verified 20 Oct)

| Fact | Source (accessed 20 Oct 2026) |
|---|---|
| Knox Term 4: starts Tue 13 Oct; **Thu 3 Dec "Presentation Day and Term 4 Concludes"**; Fri 4 Dec staff day | https://www.knox.nsw.edu.au/about/public-information/term-dates (saved `oct20/ops/web/knox_terms.txt:528-532`) |
| HSC written exams: **Tue 13 Oct to Thu 5 Nov** (four weeks; no exams Fri 6 Nov) | NESA timetable page (`oct20/ops/web/hsc_tt.txt`); PDF https://www.nsw.gov.au/sites/default/files/noindex/2026-05/2026-hsc-written-exam-timetable-01-05-26.pdf (`oct20/ops/web/hsc_tt.pdf`) |
| HSC subjects near competition work (from the PDF's column positions, `hsc_tt_layout.txt`): Maths Advanced/Standard and Maths Ext 2 Mon 19 Oct; **Maths Ext 1 Fri 23 Oct pm**; **Business Studies Mon 26 Oct am**; **Economics Tue 27 Oct pm (1:55-5:00)**; Legal Studies Mon 2 Nov am; Physics Thu 5 Nov am | same PDF |
| Whether any Caplet member sits the HSC: **UNVERIFIED** (year levels are not in the repo, `L10:129-130`) | - |
| Knox internal (Year 10/11) exam dates: **not public, UNVERIFIED**. The Knox term-dates page lists none. Each student enters their own in the availability grid (§2, M1) | Knox page above |
| Deadlines (5:00 pm ET): TNA Fri 23 Oct = **Sat 24 Oct 08:00**; IPS Fri 6 Nov = **Sat 7 Nov 09:00**; Final Report instructions "shared on November 9" (Tue 10 Nov Sydney; hour UNVERIFIED); Final Report + school documentation Fri 4 Dec = **Sat 5 Dec 09:00**; "We will not grant any deadline extensions" | `deliv:21-29, 51-53`; conversions `oct20/ops/scripts/tz.py` |
| Trading "ends on November 6, 2026"; the market closes 4:00 pm ET = **Sat 7 Nov 08:00**. The exact freeze time is UNVERIFIED | `OFF/smapply_public_2026-10-14/trading.txt:24, 31` |
| FOMC meets Oct 27-28: statement 2:00 pm EDT Wed 28 Oct = **Thu 29 Oct 05:00** | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm (`oct20/ops/web/fomc.html`) |
| Wharton needs "at least four active members at all times to compete" | `AIP:370` |

**Week view**

| Knox T4 week | Dates | HSC | Competition | Meetings (§2) | Internal deadlines |
|---|---|---|---|---|---|
| 2 | Mon 19 - Sun 25 Oct | week 2 | TNA due Sat 24 08:00 | M1 Tue 20, M2 Wed 21, M3 Thu 22, M4 Sun 25 | **TNA submitted Thu 22 20:00** (36 h early) |
| 3 | 26 Oct - 1 Nov | week 3 | IPS votes and drafting; FOMC Thu 29 05:00; US clocks change Sun 1 Nov | M5 Tue 27, M6 Thu 29 (only if needed), M7 Sun 1 | Options notes Mon 26 18:00; outlines Wed 28 22:00; any voted order entered by **Fri 30 Oct 22:00** |
| 4 | 2 - 8 Nov | week 4 (ends Thu 5) | IPS due Sat 7 09:00; WInS freezes | M8 Tue 3, M9 Thu 5, M10 Sun 8 | Fallback last order Wed 4 22:00; text lock Thu 5 09:00; **IPS submitted Thu 5 20:00** (37 h early) |
| 5 | 9 - 15 Nov | - | Final Report instructions Tue 10 | M11 Tue 10, M12 Sun 15 | Wharton questions by Fri 13 |
| 6-7 | 16 - 29 Nov | - | Final Report drafting | M13 Sun 22, M14 Sat 28 | Draft 1 Sat 21 20:00; draft 2 + signed school letter Fri 27 20:00 |
| 8 | 30 Nov - 5 Dec | - | Final Report due Sat 5 09:00 | M15 Tue 1, M16 Wed 2 | **Submit Wed 2 Dec 20:00** (61 h); hard stop Thu 3 Dec 18:00 (39 h) |

Why the Final Report target is earlier than 36-48 h: the 36-48 h window is Thu 3 Dec, which is Presentation Day and the
last day students attend (Fri 4 Dec is a staff PD day; whether staff will sign then is UNVERIFIED, so get the letter signed earlier). Thu 3 Dec 18:00 is kept as the hard internal stop.

---

## 1. Role map (roles only: each student picks)

**Picking rules.**
1. Fixed already: **Ray is team leader** (Wharton: leaders "may not be changed after the Competition begins ... unless
   the Advisor submits a written request", and the leader submits deliverables, `L10:87-90`). **Ray is trader** by the
   team rule after the 7 Oct mis-click (`TL:141`; `snap/main/START_HERE.md:29`). The team may re-vote the trader rule at
   M1. So Ray picks at most one more role.
2. Everyone else picks **at most 3 primary roles** and **at most 2 backups**. Six students x 3 = 18 slots for 12 roles.
3. Each student writes their top four roles privately on the pick sheet before M1. At M1: fixed roles first, then
   uncontested picks, then any clash is settled by the two students each giving a 30-second reason and a vote. Picks
   follow preference and workload, never "who is best" (no ranking of teammates).
4. Pick roles you will really do. Last year's semifinal asked every member to "briefly explain how they contributed
   value to the team" (`L10:111`); your role is that answer (see `oct20/semis/semis_playbook.md` §7).

**Cannot be combined (two-person checks):** deputy ≠ leader; historian ≠ chair; trade-log keeper ≠ trader; paste
checker ≠ submitter and ≠ author of the text checked; a scorer never scores their own text.

| # | Role | Does (the whole job) | Busiest | Primary (first name) | Backup |
|---|---|---|---|---|---|
| 1 | **Team leader / chair** (fixed: Ray) | Chairs meetings; Wharton's named contact; sends Contact Us questions; submits on SMApply | submit days | Ray | Deputy (chairing only; see risk R2 for submitting) |
| 2 | **Trader** (Ray by team rule) | Places/cancels WInS orders only after a logged vote; reads fills; no AI near WInS | any voted trade; 4-7 Nov | Ray | Deputy or rates analyst (not the trade-log keeper; the trade-log keeper then checks the preview) |
| 3 | **Deputy / process lead** | Owns this plan; posts agendas 24 h ahead; sets phone alarms for every deadline; submit watcher; chairs if the leader is absent | every week | | |
| 4 | **Historian / recorder** | Writes the decision log within 12 h of each meeting; keeps the AI-use log; prompts weekly journals; owns the Works Cited AI record | after every meeting; FR | | |
| 5 | **Editor** | Owns each deliverable's Doc; moves AI text out of it; assembles drafts; word counts; exports the PDF | 21-22 Oct; 31 Oct - 5 Nov; 21 Nov - 2 Dec | | |
| 6 | **Rules & format lead** | Official-rules checklist; screenshots the SMApply forms; format gate; drafts Wharton questions (a student's words); WInS listing screenshots | 20 Oct; 3 Nov; 10 Nov | | |
| 7 | **Rates analyst** | Owns every bond and ladder number on one dated basis; re-prices once when the plan says; the numbers card | 22 Oct; 29 Oct; 7-12 Nov | | |
| 8 | **Growth & risk analyst** | VT's role, Laura's kept half, shortfall order, stress tests, 2031 range method | 26-27 Oct; FR | | |
| 9 | **Client & co-sponsor lead** | Case knowledge; "certainty", "responsible", "flexibility"; 2031 range messaging; currency risk | 26-27 Oct; FR | | |
| 10 | **Trade-log keeper** | Fills the Sheet's Trade Log from WInS history; saves WInS records before and after the freeze; checks every order preview with the trader | 21 Oct; 6-8 Nov | | |
| 11 | **Paste & numbers checker** | TNA: exact-match paste check. IPS/FR: every number traced to the numbers card | 22 Oct; 3-5 Nov; 30 Nov - 2 Dec | | |
| 12 | **Advisor & school liaison** | Requests the school documentation letter; keeps the advisor informed (advisors "may not make decisions on behalf of students", `L10:94-95`); keeps the exam/availability grid | 23 Oct; 27 Nov | | |

**Per-deliverable assignments (not roles, logged at the meetings):** TNA authors (one per pick, M1); two TNA scorers
(non-authors); IPS paragraph owners (M4); every student drafts their own pitch alone (M4); Final Report section
owners (M11); two scorers per draft.

---

## 2. Meetings (each 30 minutes or less)

**Standing rules.**
- Video call. The deputy posts the agenda 24 h ahead (TNA week: the same morning). The timer is visible.
- Pre-reads are 15 minutes or less. If you have not read it, say so; don't fake it.
- The historian logs each decision (template §3) within 12 h. At the end of each meeting the chair reads every
  decision back.
- **Decision rule (proposed; vote it at M1):** quorum 4 of 6. A motion passes when more of the six vote for than
  against, with at least 4 votes cast. Absent members vote in the team chat by 22:00 the same night in TNA week, within
  12 h otherwise. Dissent is written down with the student's own reason. A logged decision is reopened only with new
  evidence and 4 votes.
- A student with an exam the next morning is excused and votes in the chat.

| # | When (Sydney) | Length | Agenda (minutes) | Decisions to log | Pre-read | Outputs |
|---|---|---|---|---|---|---|
| **M1** | **Tue 20 Oct 20:00** | 30 | 0-2 recorder named and **vote the decision rule (DL-06) first** · 2-10 read aloud AIP:377 (competition AI policy) and AIP:370 (ethics), then **vote the AI rule** · 10-17 roles from the pick sheets · 17-24 TNA picks, order and people · 24-30 housekeeping owners | DL-01 **AI rule** (options: (a) main `CLAUDE.md:12-13` "never write, rewrite or suggest wording", plus AI checks that return issues only; (b) no AI at all on deliverables; (c) the 16 Oct "[AI] suggestions" rule, which conflicts with AIP:377) · DL-02 role map and backups · DL-03 the three picks and their order (on record: IBTM, IBTR from the 04:42:53 AM ET re-placed order, VT; `U19` §3a item 3) · DL-04 TNA authors, 2 scorers, paste checker, submit watcher · DL-05 what happens to the AI text in the IPS Doc (reject the v12 suggestions; move V5 and the [AI] reflections into an "AI reference" tab, or delete them; never just strip the tag, `U19` §3a item 2) · DL-06 decision rule | AIP:370, 377, 465; `snap/main/CLAUDE.md:6-17`; this plan §1 and §5 | Pick sheet filled; availability grid link; housekeeping owners: Doc clean-up (editor, deputy watching), repo and fork private (their owners), SMApply TNA form screenshots (rules lead + Ray), 6 Oct email arrival time (rules lead), Wharton question batch 1 (Ray sends), school letter request by Fri 23 (liaison) |
| **M2** | **Wed 21 Oct 20:00** | 30 | 0-20 **D0** four wordings (5 each) · 20-26 four smaller items · 26-30 trader reports the 11 fills | DL-07 **D0-1** what VT is for · DL-08 **D0-2** floor anchor and rounding · DL-09 **D0-3** why the ladder starts at 2042 (describe Laura's January 2027 purchase, not the WInS order sequence) · DL-10 **D0-4** "sized for" vs the IBTR top-up rule (options: `U19` §7a) · DL-11 who absorbs a top-up · DL-12 IBTR number rule (no dollar level, or one re-price Thu 22 morning) · DL-13 IBTM "refined" label (only if the email time is verified) and the "0.3 to 0.2" story (only if a student remembers it) · DL-14 whether "owned" stays · DL-16a **TNA AI-disclosure decision** (moved from M3: decide here, or by a logged chat vote by Thu 22 Oct 12:00 after any Wharton reply; any line is student-written before the 16:00 text lock; M3 only confirms) [consistency fix 20 Oct, G1] | `U19` §7a; your own pick's kit in `out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md` (v2; Part 0 + your kit) [consistency fix 20 Oct, D-6] | Authors revise tonight; drafts to scorers by 22:00 |
| **M3** | **Thu 22 Oct 19:00** | 20 | 0-5 paste-checker report · 5-10 scorers' marks and fixes done · 10-15 approve vote; each author confirms "my own words" · 15-20 Ray submits on screen-share, deputy watches | DL-15 TNA final text approved · DL-16 TNA AI-use rows complete (the disclosure decision is DL-16a at M2 or a chat vote by Thu 22 Oct 12:00; M3 only confirms it) [consistency fix 20 Oct, G1] | Final texts (locked 16:00) | **Submitted by 20:00** (36 h early); confirmation screenshot; PDF/text copy saved in Drive |
| **M4** | **Sun 25 Oct 17:00** | 30 | 0-8 TNA debrief (each student: one thing learned, for the journal) · 8-14 editor's list of TNA claims the IPS must keep · 14-22 IPS paragraph owners; pitch drafted by all six · 22-27 set B options-note owners · 27-30 is D9 (floor size) on the 27 Oct agenda? | DL-17 IPS paragraph owners · DL-18 options-note owners (rates analyst; growth & risk analyst; client lead; rules & format lead, `U19` §3b item 3) · DL-19 D9 in or out · DL-20 outside-reader rule: scores and questions only, never sentences (`DLR` row 21) | Editor's TNA-claims list (Sat 24) | Journal entries; owners logged |
| **M5** | **Tue 27 Oct 20:00** | 30 | D1 6 · D2 3 · D3 3 · D4 3 · D5 3 · D6 3 · D7 2 · D8 3 · D9 2 (if on) · smaller choices 2. Anything unsettled goes to M6 | DL-21 to DL-30 = **vote set B** D1 coupon-risk cover; D2 Laura's kept half; D3 one certainty standard; D4 one floor definition and name; D5 shortfall order to 2042; D6 "responsible" and "flexibility"; D7 what the IPS says about WInS; D8 2031 valuation date, re-quote rule, currency; D9 floor size; smaller choices (strategy name, 2027 leftover, parking ETF) (options and evidence: `U19` §7b). Any vote that needs a WInS order → trader writes a ticket | The four half-page options notes, written by students (posted Mon 26 18:00) | Votes with dissent; order tickets (if any); outlines due Wed 28 22:00. *Economics HSC is that afternoon: anyone sitting it votes in the chat* |
| M6 | Thu 29 Oct 20:00 (**only if needed**) | 20 | 0-10 carry-overs from M5 · 10-20 rates analyst's post-FOMC re-price of kept figures | DL-31 carry-overs · DL-32 go/no-go for any WInS order (entered by Fri 30 Oct 22:00) | Rates analyst's one-page number check | Order placed, or "no trades" logged |
| **M7** | **Sun 1 Nov 17:00** | 30 | 0-2 clock change reminder (from 17:00 today ET is 16 h behind) · 2-12 scorers' marks on the assembled IPS · 12-20 **pitch vote** (students' own drafts) · 20-27 cut list · 27-30 run an AI issues-only check? | DL-33 pitch chosen or merged (whose words) · DL-34 cuts · DL-35 AI issues-only check yes/no (only if DL-01 allows) | Assembled draft (Sat 31 Oct 20:00); `oct19/ipskit/ips_writing_kit.md` §7 rubric (scorers only) | Revised draft due Mon 2 Nov 22:00 |
| **M8** | **Tue 3 Nov 20:00** | 30 | 0-8 format gate on the exported PDF · 8-24 each paragraph owner explains their paragraph aloud, 1 min, no notes · 24-30 approve vote | DL-36 IPS approved · DL-37 WInS: no further orders, or the status of the last one | Exported PDF (18:00) | Fixes only; text lock Thu 5 Nov 09:00 |
| M9 | Thu 5 Nov 19:00 | 15 | Ray submits on screen-share; deputy and paste checker watch; plan the WInS saves | DL-38 submitted (time) | Locked PDF | **IPS submitted by 20:00** (37 h early); screenshot |
| **M10** | **Sun 8 Nov 17:00** | 30 | 0-8 freeze debrief (journal) · 8-15 WInS records saved? · 15-22 roles for the release-day drill · 22-30 Final Report evidence owners; each student marks which story candidates they remember (`oct19/frprep/final_report_prep.md`, 21 candidates) | DL-39 FR evidence owners · DL-40 release-day drill roles · DL-41 numbers rebuild owners (6 Nov close) | Evidence plan section of the prep pack | Evidence task list |
| **M11** | **Tue 10 Nov 20:00** (Wed 11 if the instructions are not out by 18:00 Tue) | 30 | 0-5 rules lead's requirement checklist · 5-17 **vote the Final Report structure** (sections mapped to the five criteria, `deliv:55-59`) · 17-24 section owners and backups · 24-30 charts and tables list; questions for Wharton | DL-42 **FR structure** · DL-43 section owners · DL-44 charts/tables, and who builds each from their own computations · DL-45 Contact Us questions (sent by Fri 13) | Official FR instructions, read in full by everyone (15 min) | Checklist replaces every FORECAST row in the prep pack |
| M12 | Sun 15 Nov 17:00 | 25 | outlines read · numbers card · 2031 range figures · Articulation stories | DL-46 numbers card approved (each number re-derived by a student) · DL-47 2031 range figures to present · DL-48 Articulation story list (each story confirmed by the student in it) | Owners' outlines (bullets, own words) | Drafting starts |
| M13 | Sun 22 Nov 17:00 | 30 | scorers' marks on draft 1 · gaps · cut list · school letter status | DL-49 change list · DL-50 AI issues-only check on draft 1, yes/no | Draft 1 (Sat 21 20:00) | Draft 2 due Fri 27 20:00 |
| M14 | Sat 28 Nov 10:00 | 30 | draft 2 review · provenance check result (§5) · Works Cited and AI record · letter scanned? | DL-51 final cuts · DL-52 each student approves their own AI-use rows | Draft 2; historian's AI record | Final text Mon 30 Nov 20:00 |
| M15 | Tue 1 Dec 20:00 | 30 | format gate · each owner confirms "my own words" · approve vote | DL-53 Final Report approved | Exported PDF + letter file | Locked files |
| M16 | Wed 2 Dec 19:00 | 15 | Ray submits the report and the letter as a separate file (`deliv:52`); deputy watches | DL-54 submitted (time) | - | **Submitted by 20:00**; screenshot. Sat 5 Dec 09:30: Ray checks SMApply status (no meeting) |

Total: 16 meetings, about 7 hours over seven weeks. M6 is conditional.

---

## 3. Templates (fields only)

### 3a. Decision log (one page; one row or card per decision)

Keep it in one place the whole team can see, for example a "Decision Log" tab in Notes & Discussions or the empty PM
Dashboard Sheet. A student creates it; no AI tool edits Drive.

| Field | Fill with |
|---|---|
| ID | DL-NN |
| Date and time (Sydney) | |
| Meeting / channel | M# or "chat vote" |
| Question decided | one line |
| Options considered | letters + one line each |
| Evidence used | file or link + date; mark **AI-made: Y/N** |
| Proposed by | first name |
| Argued for (name: reason, in their words) | |
| Argued against (name: reason, in their words) | |
| Vote | for / against / abstain, with names; absent members and how they voted |
| Dissent recorded | Y/N + the text |
| Decision | one line |
| Affects | TNA / IPS / FR / WInS / notes already filed |
| Consistent with filed TNA notes and reflections? | Y/N + why |
| Action, owner, due | |
| AI involvement | none / AI options / AI numbers / AI check (link to AI-log ID) |
| Recorded by / confirmed by | two first names |
| Reopen only if | the new evidence that would justify it |

### 3b. Personal journal (each student, weekly by Sunday 21:00, plus same day after any big event)

Wharton bans invented "teamwork and experiential stories" (`AIP:370`). Write it the same day. A blank stays blank.

| Field | Fill with |
|---|---|
| Date / week | |
| Name (first) | |
| Time spent this week | hours |
| What I did | tasks, with links to the files |
| A decision I influenced, supported or disagreed with | DL-ID + my reason |
| What I learned (what this teaches) | |
| A challenge or mistake, and what we did next | |
| What surprised me (market, client, process) | |
| AI use this week | AI-log IDs, or "none" |
| Evidence | screenshots, commits, Doc versions |
| Question for the team | |

---

## 4. Work calendar per deliverable (Sydney time)

### 4a. Trading Notes Analysis (due Sat 24 Oct 08:00; internal submit Thu 22 Oct 20:00 = 36 h)

| When | Step | Owner (role) | Done when |
|---|---|---|---|
| Tue 20, by 18:00 | Pick sheet and availability grid filled (include your own exam dates) | every student | 6 of 6 |
| Tue 20 | M1; Doc cleaned (v12 suggestions rejected, AI text moved out); SMApply TNA form screenshotted (fields; does it lock on submit?) | editor + deputy; rules lead + Ray | screenshots in Drive |
| Tue 20 night - Wed 21 18:00 | First drafts, written from your own notes (protocol §5) | 3 authors | drafts in the student-draft tab |
| Wed 21, by 12:00 | 11 fills confirmed in WInS Order and Transaction History; Trade Log rows entered | trader reads; trade-log keeper enters | 11 rows |
| Wed 21 20:00 | M2 (D0) | all | DL-07 to DL-14 |
| Wed 21 22:00 | Revised drafts to scorers; scorers mark them before any AI check | authors; 2 scorers | marks returned by Thu 22 12:00 |
| Thu 22 morning | IBTR number rule applied (no level, or one re-price on the latest published curve) | rates analyst | logged |
| **Thu 22 16:00** | **Text lock** (40 h before) | editor | no edits after |
| Thu 22 16:00-18:30 | Each note pasted from the WInS Trade Notes page as plain text; `python3 office/tools/textcheck.py paste.txt --compare wins_note.txt` until "exact match: YES" (IBTM 292, IBTR 294, VT 288 characters; the IBTR note must say "about 0.2", not "0.3"); word counts twice; check against TNA:42-53 | paste checker; rules lead | signed off (`U19` §3a item 10; `out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md` 2A, :433-436) [consistency fix 20 Oct, D-6] |
| **Thu 22 19:00-20:00** | M3; **submit** | Ray; deputy watching | confirmation screenshot |
| Fri 23 18:00 | Team's absolute latest if Thursday slips. Never plan to submit on Saturday morning | Ray | - |
| Sat 24 09:00 | SMApply shows "submitted"; editor lists every TNA claim the IPS must keep (TNA:30-31) | Ray; editor | list posted |
| Sat 24-Tue 27 [consistency fix 20 Oct, row 34 / D-7] | Wharton questions batch 2 (TIPS/STRIPS ETFs, cash, WInS after the freeze, AI on WInS screens, `U19` §9) | rules lead drafts; Ray sends | sent |

### 4b. IPS (due Sat 7 Nov 09:00; internal submit Thu 5 Nov 20:00 = 37 h)

| When | Step | Owner | Done when |
|---|---|---|---|
| Sun 25 | M4: paragraph owners, options-note owners | all | DL-17, DL-18 |
| Sun 25 | Back-fill the AI-use log (rows L1-L22, `TL` §5) and the journal; banner the false "100% student" line (`snap/main/docs/AI_USE.md:49`) | historian; each student checks their own rows | log has no gap after 30 Sep |
| Mon 26 18:00 | Four half-page options notes, in students' words | rates; growth & risk; client lead; rules & format | posted |
| Tue 27 20:00 | M5: vote set B | all | DL-21 to DL-30 |
| Wed 28 22:00 | Outlines in bullets, with V5 and every exemplar closed; each student's own pitch draft | paragraph owners; all six | posted |
| Thu 29 05:00 / 20:00 | FOMC; re-price any kept market figure once; M6 if needed | rates analyst | number check posted |
| **Fri 30 Oct 22:00** | **Last planned time to enter a voted WInS order** (it fills in the Fri 30 Oct ET session; check the fill after 07:00 Sat 31). Yield-check, preview checked by a second student, a new note for each order | trader + trade-log keeper | fill confirmed |
| Fri 30 22:00 | Paragraph drafts | owners | in the student-draft tab |
| Sat 31 20:00 | Assembled draft; two scorers mark it with the rubric before any AI check | editor; 2 scorers | marks by Sun 1 16:00 |
| Sun 1 17:00 | M7 (clock change today) | all | pitch chosen |
| Mon 2 22:00 | Revised draft | owners; editor | - |
| Tue 3 18:00 | PDF export and format gate: title page, pitch ≤50 words, IPS ≤500 (aim 45 and 470; headings counted), TNR 12, double-spaced, 1-inch margins, no charts, links, footnotes or citations (IPS:107-123), ≤5 MB (IPS:122), names exactly as on the roster; open the PDF on a second device to check no suggestion or comment prints | rules lead + one more | gate passed |
| Tue 3 20:00 | M8: approve | all | DL-36 |
| Wed 4, by 22:00 | Fallback only: last voted order (fills in the Wed 4 Nov ET session, confirmed Thu 5 08:00). No trades after that | trader | - |
| **Thu 5 09:00** | **Text lock** (48 h before) | editor | - |
| **Thu 5 19:00-20:00** | M9; **submit** | Ray; deputy watching | screenshot |
| Fri 6 evening and Sat 7 after 08:00 | Save WInS Order History (including cancelled orders), Transactions, Trade Notes, Portfolio Summary, Session Rules, before and after the freeze, with the username cropped | trade-log keeper | files in Drive |

### 4c. Final Report + school documentation (due Sat 5 Dec 09:00; submit target Wed 2 Dec 20:00; hard stop Thu 3 Dec 18:00)

| When | Step | Owner | Done when |
|---|---|---|---|
| **Fri 23 Oct** | Ask the school for the documentation letter ("Do not wait until the last minute", `deliv:52`; sample linked at `deliv:53`). Ask who signs it | advisor & school liaison | request sent |
| Weekly from Sun 25 Oct | Journal (§3b); decision log; AI-use log; evidence captures | each student; historian | weekly check |
| Sat 7 - Thu 12 Nov | Rebuild every number to be quoted, on the 6 Nov close (`U19` §3c item 5) | rates analyst + checker | numbers card |
| Sun 8 | M10 | all | evidence owners |
| Tue 10 | Instructions out (Mon 9 Nov ET): paste them verbatim into a checklist by 18:00; replace every FORECAST row of the prep pack | rules lead | checklist |
| Tue 10 20:00 | M11: structure vote | all | DL-42 |
| Fri 13 | Contact Us questions sent (a student words them) | Ray | sent |
| Sun 15 | M12: outlines, numbers card | owners | DL-46 to DL-48 |
| **Sat 21 20:00** | **Draft 1**; 2 scorers mark it before any AI check | owners; editor | marks by Sun 22 16:00 |
| Sun 22 | M13 | all | change list |
| **Fri 27 20:00** | **Draft 2**; **school letter signed and scanned** (students finish Thu 3 Dec) | owners; liaison | letter file saved |
| Sat 28 10:00 | M14; provenance check (§5 step 9) | editor; historian | clean |
| Mon 30 20:00 | Final text; Works Cited, including the full AI record | owners; historian | - |
| Tue 1 Dec 20:00 | M15: format gate per the official instructions; approve | rules lead; all | DL-53 |
| **Wed 2 Dec 19:00-20:00** | M16; **submit** report + letter (separate file) | Ray; deputy | screenshot |
| Thu 3 Dec 18:00 | Hard internal stop (Presentation Day) | Ray | - |
| Sat 5 Dec 09:30 | Status check | Ray | - |

---

## 5. No-AI writing protocol

**The rule from Wharton:** "You may not submit any work generated by an AI program as your own" (`AIP:377`). (Wharton's
Pre-baccalaureate advice "Don't use AI for personal reflection or opinion-based tasks", `AIP:465`, is not a
competition rule, but it is good practice for the reflections.) The ethics page bans passing "AI generated writing or
work off as your own" (`AIP:370`). Rewording AI text ("humanising") does not make it yours (`U19` §2).

**A. Set-up (once, by Tue 20 Oct)**
- [ ] AI rule voted (DL-01) and pasted at the top of every deliverable Doc.
- [ ] AI text out of the writing space: v12 suggestions rejected by a person in Suggesting view; V5 and the [AI]
      reflections in a separate "AI reference, do not copy" tab or file, which authors do not open while writing
      (`U19` §3a item 2).
- [ ] Each student writes in the Doc **signed in as themselves**, so version history shows who typed what. Don't paste
      large blocks; typed history is your evidence of authorship.
- [ ] AI writing features off: Google Docs "Help me write"/Gemini, Grammarly's generative features, any rewrite
      button. Plain spell-check is fine. Whether grammar suggestions count as AI help: decide at M1 and log it.
- [ ] AI tools cannot touch Drive, Docs, Gmail, WInS or SMApply: deny rules in `.claude/settings.json` (none exists
      today, `U19` §3a item 11). Repo and fork private.

**B. Writing a section (every author, every deliverable)**
1. **Decide first.** The substance comes from a logged team vote (D0, set B, FR structure), not from a kit.
2. **Read the fact kit once** (your part only), for facts, numbers and traps. Then **close it and every AI file and
   chat**.
3. **Wait at least 10 minutes.** Then write your own bullet notes from memory: what, why, so what for Laura.
4. **Check the facts only.** Reopen the kit to check numbers, dates and names in your bullets. Don't copy any phrase.
5. **Draft from your bullets** with everything else closed. Numbers come only from the team's numbers card, each
   with its source and date. Exact quotes are allowed only where a rule requires them (the WInS note in the TNA, TNA:44).
6. **Self-test aloud:** you can explain each sentence without notes (the kit's six self-test questions for the TNA).
   If you can't, you are not ready to write.
7. **Human check first:** two students score the draft before any AI check.
8. **AI check (only if DL-01 allows it):** the AI gets the draft and returns **issues only**: factual errors, rule
   breaches, word counts, line numbers, with **no replacement wording**. Suggested prompt: "List factual, number or rule
   errors only, by line. Do not suggest any wording." Save the prompt and the output. The student fixes each issue in
   their own words. Never ask an AI to improve, rewrite, shorten, "humanise", or remove "AI tells", and never use an
   AI-detector to edit text.
9. **Provenance check before sign-off:** the editor runs a word-overlap script (for example `oct19/exemplars/overlap.py`,
   a 5-word-run comparison, no AI) of the final text against every AI file (exemplars v1-v12, kits, the AI reference
   tab, AI chats). Any shared 5-word run that is not an official quote → the author rewrites it from their own notes,
   or cuts it.
10. **Sign-off:** each author confirms "written by me from my own notes" in the decision log (DL-15, DL-36, DL-53).

**C. Recording AI use (AI-use log, the source for the Works Cited)**

| Field | Fill with |
|---|---|
| AI-ID / date and time (Sydney) | |
| Student (first name) | |
| Tool and version; mode | chat / code agent / connector / browser agent |
| Purpose | brainstorm / research / numbers / fact check / rules check / format check / other |
| Prompt | the exact text, or a link to the saved file |
| Output | link |
| What the student did with it | read only / checked a fact at its primary source / changed a decision (DL-ID) / not used |
| Deliverable affected | TNA / IPS / FR / none |
| Words from the output in a deliverable | **must be 0**; if not, stop and rewrite |
| Verified by (student) + primary source | |
| In the Works Cited draft? | Y/N |

- Log the same day. The historian checks the log every Sunday. Back-fill rows L1-L22 from `TL` §5 by Sun 25 Oct.
- The IPS bans "formal citations" (IPS:123). Keep the record in the log and the Final Report's Works Cited. Ask Wharton
  whether the TNA or IPS needs a disclosure line (batch-1 Q1, `U19` §9). Until they answer, add no citation line to
  the IPS.
- Logging AI text does not make it the students' work. The only fix is rewriting from your own understanding
  (`TL:297-299`).

---

## 6. Risk register

L/I = likelihood / impact (H, M, L).

| # | Risk | L/I | Early sign | Mitigation (before) | If it happens | Owner |
|---|---|---|---|---|---|---|
| R1 | An author is ill or busy with exams in TNA week | M/H | No draft by Wed 21 18:00 | Backup author named at M1; authors post their bullet notes daily | The backup writes a fresh reflection from their own notes; the absent author is not credited for words they did not write | deputy |
| R2 | **Leader unreachable at submission** (only the leader submits, `L10:89-90`) | L/H | No reply 24 h before the internal deadline | Submit 36-48 h early; deputy watches every submit; ask Wharton (batch 1, item 4, Tue 20 Oct) what happens if the leader is ill [consistency fix 20 Oct, row 34 / D-7]; don't share passwords until Wharton answers | The advisor contacts Wharton through Contact Us at once (a leader change needs the advisor's written request, `L10:87-88`) | deputy; liaison |
| R3 | Exams squeeze work (HSC to Thu 5 Nov; Knox internal exams UNVERIFIED) | H/M | Grid shows clashes | Availability grid by Tue 20; no more than 2 tasks per student per exam week; drafts timed for evenings and weekends; chat votes allowed | Swap the task with the backup; move the internal date, never the 36 h buffer | deputy; liaison |
| R4 | **Single points of failure**: leader = trader = submitter; one school account owns every Drive file (`U19` §3a item 3); routines run on one machine (`TL:153`) | H/H | - | Backup for every role; the owner gives all six edit access; after each milestone, download a copy of each deliverable to a second student's drive; pause routines nobody watches | The backup acts; the historian logs it | leader; deputy |
| R5 | WInS error (mis-click, stale price, order after the vote window) | L/H | An order without a DL-ID | No order without a logged vote; trader + second student check the preview; yield-check every bond; no AI near WInS; no orders after Wed 4 Nov ET | "Run with it" (Wharton FAQ advice, `TL:141`); log it; a new note explains it | trader; trade-log keeper |
| R6 | AI wording enters a deliverable | M/H | Shared 5-word runs; text appears in a big paste | §5 protocol; AI text moved out of the Docs; provenance check | Rewrite from your own notes before submitting; log it | editor; historian |
| R7 | **Submission tech**: unknown form fields; locks on submit; the PDF prints suggestions (today 4 pages, `U19` §3a item 2); file >5 MB; wrong file | M/H | Form not seen by Tue 20 | Screenshot each form early; accept/reject all suggestions; export and open the PDF on a second device; check the file name and size; screenshot the confirmation | Use Contact Us at once with the screenshot; don't resubmit blindly | rules lead; Ray |
| R8 | Time-zone slip (US clocks change 1 Nov; Saturday-morning deadlines) | M/H | Anyone quoting ET without Sydney | Every date in Sydney time; alarms set by the deputy; internal deadlines 36-48 h early | The Fri 18:00 fallback (TNA) or the Thu 3 Dec 18:00 hard stop (FR) | deputy |
| R9 | Word-count dispute | M/M | Two counts differ | Strictest reading (headings count; hyphenated words split); `textcheck.py` plus a second counter, by two people | Cut to the lower count | paste checker |
| R10 | Public repo and fork hold AI exemplar reflections for the same three notes | H/H | GitHub shows "public" | Make both private Tue 20 (the fork has a different owner) | - | repo and fork owners |
| R11 | Late strategy reopen (floor size; the outside judge's view) | M/H | New ideas after Tue 27 | The decision rule; any trade-dependent change by the Fri 30 Oct order window; outside readers give scores and questions only | Stay with the logged decision; record the dissent honestly | leader |
| R12 | School letter not signed before Knox closes (Thu 3 Dec) | M/H | No reply by Fri 6 Nov | Request Fri 23 Oct; chase at M10; signed by Fri 27 Nov | Liaison asks the advisor to escalate inside the school | liaison |
| R13 | FR instructions late or different from the forecast | M/M | Not out by Tue 10 18:00 | Release-day drill roles; FORECAST rows marked | Move M11 to Wed 11; send questions by Fri 13 | rules lead |
| R14 | Fewer than four active members ("at least four active members at all times", `AIP:370`) | L/H | A member misses two meetings and skips the journal | Real roles; workload balanced; the advisor kept informed | Talk early; the advisor contacts Wharton if needed | leader; liaison |
| R15 | Overload: too much AI material (about 745,000 words, `L10:36`), too little time | H/M | Pre-reads skipped | Pre-reads 15 minutes or less; no new AI research waves before 7 Nov (`snap/main/CLAUDE.md:15`) | Cut agendas to the decisions only | deputy |
| R16 | Record gaps weaken Articulation (journal silent since 7 Oct, `TL:138`) | H/M | Missing Sunday journals | Weekly journal; decision log within 12 h | Leave the gap blank; never reconstruct it from AI files | historian |
| R17 | Internet or device failure at submit | L/H | - | Submit early; final PDF on two devices; a second network ready | Use the hotspot or school network; screenshot errors | Ray; deputy |

---

## 7. Checks run on this plan

- All Sydney/ET conversions were checked with `zoneinfo` (`oct20/ops/scripts/tz.py`): TNA Sat 24 Oct 08:00; IPS Sat 7
  Nov 09:00; 6 Nov close Sat 7 Nov 08:00; Wed 4 Nov close Thu 5 Nov 08:00; FOMC Thu 29 Oct 05:00; FR Sat 5 Dec 09:00.
  Lead times: TNA 36 h, IPS 37 h, FR 61 h (target) and 39 h (hard stop); text locks 40 h (TNA) and 48 h (IPS). The
  offset is 15 h on Sun 1 Nov at noon and 16 h from Sun 1 Nov 17:00.
- The Knox and NESA dates were fetched live on 20 Oct and saved in `oct20/ops/web/`. Subject days were read from the
  PDF's column positions, re-checked against each page's day headers.
- **UNVERIFIED:** members' year levels and exam timetables; Knox internal exam dates; the exact WInS freeze time; the
  hour the Final Report instructions are released; whether the SMApply forms lock on submit; whether anyone but the
  leader may submit.
