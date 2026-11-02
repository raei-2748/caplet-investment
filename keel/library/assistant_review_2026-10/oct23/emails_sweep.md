# Wharton emails sweep: what the 15 Sep - 19 Oct emails change in the pack and the repo

Claude Code, Fri 23 Oct 2026, about 15:00 Sydney. This covers process documents only and contains no deliverable wording.
The repo files were read, not edited.

**Source.** `SP/oct23/EMAILS.md` items 1-9 (cited **EM1-EM9**, file lines 6-14). These are official Wharton emails to
another Knox team's leader, pasted by a Caplet student. All are general sends except EM3, EM6 and EM8, which are
"team-specific but standard". The recipient's name, email and team ID are not recorded here, and neither is the 8-digit number.
SP = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad`. Repo =
`/home/user/caplet-investment` (read only). Times were converted with Python `zoneinfo`.

**Caveat.** EMAILS.md holds excerpts, not full texts. "The emails say nothing about X" means only that the excerpts say
nothing about it. Caplet's own copies should still be checked by a student for exact text and arrival time, but a
general send arrives at about the same time for every leader.

## 0. Bottom line

1. **The IPS form cannot be opened before Mon 26 Oct ET** (EM3). That is Mon 26 Oct 15:00 Sydney at the earliest, or Tue
   27 Oct 00:00 if it opens at 9 am ET. Every "open the IPS form on Thu 22 Oct" instruction is wrong. On 22-23 Oct you
   can only see the task-list status. The first real look is Tue 27 Oct 07:00, before M5 at 20:00.
2. **The freeze time is answered.** "Trading ends on November 6 at 5:00 p.m. ET" (EM9) = **Sat 7 Nov 09:00 Sydney**, the
   same minute as the IPS deadline. The market closes at 4:00 pm ET (08:00 Sydney), so an order entered after 4:00 pm
   will probably never fill. The team's last-order rule (Wed 4 Nov close) is unchanged. Seven places still say the
   freeze is at 4:00 pm or call it UNVERIFIED.
3. **The "6 Oct email" was sent Mon 5 Oct 08:07 EDT = Mon 5 Oct 23:07 Sydney** (EM5). "6 Oct" is wrong in both time zones,
   in 9 files (about 40 lines). It went out about 38 h before the IBTM order (6 Oct 10:01:41 PM ET). So the condition
   for the IBTM "refined" label set in Login Checks row 4 is met on the send time.
   - Also, the restriction to WInS-listed securities "for BOTH contributions" was already in the **Week 1 email of Mon 28 Sep**
     (EM4), before any trade.
4. **Three-case Submit rule.** The "Advanced to Next Stage" email did **not** come right after the roster submit.
   - It came 18 days after that team's "Roster Submitted" email, about 56 h after the roster deadline, at 01:17 ET on
     the day TNA submissions opened (EM3, EM6).
   - So stages open by date and are moved by Wharton, not by the team's Submit.
   - For the TNA, Case 3 cannot occur, because the IPS and Final Report stages are not open yet. **Case 1 is expected:
     the TNA's Submit is the delivery.** See section 2.
5. **Now confirmed by official email:**
   - Wharton office hours are Mon-Fri 9-5 ET (EM4). That is 00:00-08:00 Sydney until Sun 1 Nov, then 01:00-09:00.
   - Final Report instructions come Mon 9 Nov 9:00 am ET = **Tue 10 Nov 01:00 Sydney**. Both EM7 (12 Oct) and EM9 (19
     Oct) say so, so this is not just "team-reported".
   - The IPS is a form, not a PDF. EM9 is a general Wharton send of Mon 19 Oct 08:46 EDT, so `week4_impact.md` can drop
     its "TEAM-REPORTED, not public" label.
6. **Privacy.** The 8-digit number in Caplet's WInS username is shared with at least one other Knox team (EM8), so it is a
   school or advisor number, not a Caplet secret. Because "Caplet" is public in the repo, anyone who sees that number on
   any Knox team's ID can rebuild Caplet's likely username. Keep the number out of every public file **whichever team it
   appears with**, and check usernames by the full string, never by the number alone.
7. **Participation credential.** It needs "all requirements" and "all deliverables" (EM4). EM3 lists School Documentation
   as a deliverable (opens 9 Nov, due 4 Dec), so a missing school letter costs the credential too. That raises ops R12.

## 1. Times (zoneinfo)

| Event | ET | Sydney |
|---|---|---|
| EM1 SMApply invitation | Mon 15 Sep 19:23 EDT | Tue 16 Sep 09:23 AEST |
| EM3 Roster Submitted (other team) | Thu 24 Sep 07:44 EDT | Thu 24 Sep 21:44 AEST |
| EM4 Week 1 | Mon 28 Sep 09:07 EDT | Mon 28 Sep 23:07 AEST |
| EM5 Week 2 | **Mon 5 Oct 08:07 EDT** | **Mon 5 Oct 23:07 AEDT** |
| First Caplet order / IBTM order | Tue 6 Oct 7:55 PM / 10:01:41 PM EDT | Wed 7 Oct 10:55 / 13:01 AEDT (IBTM is 37 h 55 min after EM5) |
| EM6 Advanced to Next Stage | Mon 12 Oct 01:17 EDT | Mon 12 Oct 16:17 AEDT |
| EM7 Week 3 / EM8 reminder / EM9 Week 4 | Mon 12 Oct 08:44 / Fri 16 Oct 08:45 / Mon 19 Oct 08:46 EDT | 23:44 / 23:45 / 23:46 AEDT the same day |
| IPS submissions open (EM3) | Mon 26 Oct (hour not given) | from Mon 26 Oct 15:00 (00:00 ET) or Tue 27 Oct 00:00 (9 am ET) |
| Market close, last fill (6 Nov) | Fri 6 Nov 4:00 pm EST | Sat 7 Nov 08:00 |
| Trading ends (EM9) = IPS due | Fri 6 Nov 5:00 pm EST | Sat 7 Nov 09:00 |
| FR instructions (EM7, EM9) | Mon 9 Nov 9:00 am EST | **Tue 10 Nov 01:00** |
| Wharton office hours (EM4) | Mon-Fri 9:00-17:00 | Tue-Sat 00:00-08:00 AEDT until Sun 1 Nov; then Tue-Sat 01:00-09:00 |
| Weekly emails (EM4; observed ~08:07-08:46 ET) | Mondays | Mon ~23:00-23:50 until 1 Nov (Week 5 ~Mon 26 Oct 23:30); from Week 6, Tue ~00:10-00:50 (INFERENCE from the pattern) |

## 2. Fact (c) in detail: what the stage emails imply for the three-case rule

Rule as written: `oct20/verify_runbook/runbooks_checked.md:51-63` and `:393-412`; `oct20/master/master_playbook_checked.md:157-171`;
`oct20/out/Caplet_M1_Meeting_Pack_v2_20Oct2026.md:78-88`; `oct20/out/Caplet_Login_Checks_v2_20Oct2026.md:60`.

- **The premise needs a fix.** EM6 is not "right after the roster submit".
  - That team's on-submit email was EM3 (24 Sep), "Team Roster Submitted". It still said "You can edit your team
    information ... until 5:00 p.m. ET on October 9".
  - The stage move (EM6) came Mon 12 Oct 01:17 ET, outside office hours and on the day "Teams can submit beginning Monday,
    October 12" (EM3).
  - So the runbook's model "On submit -> Move to stage" (`runbooks_checked.md:55-58`) is not how the roster stage worked.
    Wharton moved applications on a date after the stage deadline (INFERENCE: a scheduled or bulk move).
- **What follows for the TNA (Thu 22 or, at the fallback, Fri 23 Oct):**
  1. **Case 3 cannot occur.** IPS submissions open Mon 26 Oct and the Final Report on 9 Nov (EM3), so neither can be
     "open and editable" on 22-23 Oct. Delete Case 3 for the TNA, or mark it "not possible before 26 Oct".
  2. **Case 1 is the expected case.** The TNA is the only open task in its stage. Wharton's own words are "Return to
     SurveyMonkey Apply to submit your team's Trading Notes Analysis" (EM6) and "had not submitted" (EM8), so it counts
     a *submit*. **Press the Submit.** Not pressing it is the real risk (runbooks `:61-62` already says so; this makes it
     the main case).
  3. **Case 2 stays as a fallback** (Submit missing or blocked), with the Contact Us confirmation.
  4. **An early Submit probably does not lock the text before the deadline.** The roster stayed editable after its Submit
     until the stage deadline (EM3). Whether the TNA form behaves the same is UNVERIFIED, so still treat the first Submit
     as final (QV2 Q5 default), but the "pressing too early" risk (`runbooks_checked.md:59-60`) is smaller than written.
  5. **What to expect after Submit.** A "submitted" confirmation email like EM3 is the sign to look for. An "Advanced to Next
     Stage" email will probably come only when the IPS stage opens (on or after Mon 26 Oct ET), so its absence on 22-24
     Oct is **not** a failure sign. If Caplet gets a "Remember to Submit" email (like EM8) *after* its submit, that is a
     red flag: Contact Us at once.
- **IPS (Thu 5 Nov):** the FR stage opens 9 Nov, so again Case 1.
- **FR (Wed 2 Dec):** the Final Report and the School Documentation both open 9 Nov and are both due 4 Dec (EM3), so they
  are probably tasks in one stage (INFERENCE). Submit may stay blocked until both are complete. Upload the school letter
  first, then Submit.

## 3. The sweep table

Verdicts: **CONFIRMS** (the email backs the line; any fix only adds the source), **CONTRADICTS** (the line is wrong),
**OBSOLETE** (the line was true or open before and is now overtaken). "v1" files (`Caplet_Login_Checks_20Oct2026.md`,
`Caplet_M1_Meeting_Pack_20Oct2026.md`) are superseded by v2. Their hits are listed once, and the fix is "use v2".
Hits that `oct21/tna/week4/week4_impact.md` already listed (the IPS-as-form sweep) are not repeated. Only new places and
status changes are given.

| Fact | Email quote (source) | File:line → what changes | Verdict | Exact fix |
|---|---|---|---|---|
| (a) IPS opens Mon 26 Oct | "Investment Policy Statement - Friday, November 6 ... Teams can submit beginning Monday, October 26" (EM3) | `oct21/tna/week4/week4_impact.md:158` ("Do this on Thu 22 Oct during the TNA session if the task is visible") and `:260-261` ("Best time: Thu 22 Oct ... Latest: before M5 on Tue 27 Oct") | CONTRADICTS | Replace both with: "IPS submissions open Mon 26 Oct ET (EM3) = from Mon 26 Oct 15:00 Sydney at the earliest. On Thu 22 Oct record only the IPS task's status (absent or 'cannot be started'). Open the form Tue 27 Oct 07:00, before M5 (20:00)." |
| (a) | same | `week4_impact.md:262` ("re-check daily from Mon 26 Oct") | CONFIRMS | Add "(EM3)". |
| (a) | same | `oct21/tna/TNA_Teardown_v2_21Oct2026.md:56` ("Open the IPS form during the TNA session") | CONTRADICTS | Change it to "Note the IPS task status during the TNA session; the form opens Mon 26 Oct ET (EM3); open it Tue 27 Oct 07:00." |
| (a) | same | `oct20/out/Caplet_Login_Checks_v2_20Oct2026.md:60` (row 2: "Open the IPS task if it is visible (PDF only, 5 MB, encrypted files refused)"); v1 `:48` | CONTRADICTS (date) + OBSOLETE (PDF) | Change it to "IPS task: screenshot its status only; it cannot be started before Mon 26 Oct ET (EM3). Form check (fields, limits) on Tue 27 Oct 07:00 as a new row 2b." |
| (a) | same | `oct20/askwharton2/questions_v2.md:141` (self-check C: "Do the same for the IPS form (PDF, 5 MB, IPS:120-122)", due Tue 20 Oct) | CONTRADICTS | Split it: TNA part unchanged; IPS part "from Tue 27 Oct 07:00 Sydney; it is a form (EM9), no PDF". |
| (a) | same | `oct20/ops/operating_plan.md:324` (R7 early sign "Form not seen by Tue 20") | CONTRADICTS for the IPS | Make the IPS early sign "IPS form not seen by Tue 27 Oct 12:00" (it cannot be seen before Mon 26 Oct ET). |
| (a) | same | `/home/user/caplet-investment/COMPETITION.md:22`; `office/workstreams/2_IPS.md:3` | CONFIRMS (deadline) | Add "submissions open Mon 26 Oct ET (from Mon 26 Oct 15:00 Sydney)". |
| (b) TNA opened 12 Oct | "Teams can submit beginning Monday, October 12" (EM3); "You may now return ... to submit your Trading Notes Analysis" (EM7) | `office/workstreams/1_TNA.md:31` (open the TNA form Sun 18 Oct); `Caplet_Login_Checks_v2_20Oct2026.md:60` (row 2, Tue 20 Oct); `oct20/compliance/compliance_matrix.md:118` (row 16) | CONFIRMS | No change; the form existed from Mon 12 Oct ET. |
| (b) | same | `COMPETITION.md:20`; `oct20/timeline/timeline.md` Phase 5 (rows 58-64, `:154-160`) | missing | Add "opened Mon 12 Oct ET". Add timeline rows: "Mon 12 Oct 16:17 AEDT 'Advanced to Next Stage' (general pattern, EM6)" and "Mon 12 Oct 23:44 AEDT Week 3 email". |
| (c) stage automation | "Advanced to Next Stage" Mon 12 Oct 16:17 (EM6) vs "Team Roster Submitted" 24 Sep, "You can edit ... until 5:00 p.m. ET on October 9" (EM3) | `oct20/verify_runbook/runbooks_checked.md:51-63` (§0 item 2), `:393-408` (decision rule), `:5-6` (banner); `master_playbook_checked.md:157-171` (§3d); `Caplet_M1_Meeting_Pack_v2_20Oct2026.md:78-88`; v1 `:55`; `Caplet_Login_Checks_v2_20Oct2026.md:60` (row 2 cases), `:76` (row 17), `:85` (row 26), `:88` (row 29); `week4_impact.md:293` | CONFIRMS "an early lock is unlikely"; OBSOLETE: Case 3 for the TNA and IPS; CONTRADICTS the "On submit -> Move to stage" model | Apply section 2: (i) Case 3 "not possible before 26 Oct (TNA) / 9 Nov (IPS)"; (ii) Case 1 is the default: press Submit; (iii) expect a "submitted" email like EM3; no stage-advance email until the next stage opens; a reminder email after the submit means Contact Us; (iv) FR: upload the school letter before Submit. |
| (c) | "Return to SurveyMonkey Apply to submit your team's Trading Notes Analysis" (EM6); reminder because the team had "not submitted" (EM8) | `runbooks_checked.md:390-391` (item 7: "how the roster submission worked" UNVERIFIED), `:562-563` (§6); `master_playbook_checked.md:688` | OBSOLETE (partly) | Mark it answered for a standard team: Submit → instant "Team Roster Submitted" email → still editable to the stage deadline → stage move on the next stage's opening date (EM3, EM6). Caplet's own buttons still go in the leader's note. |
| (c) | same | `office/workstreams/1_TNA.md:53-54` ("check what it locks") | CONFIRMS | Add "a roster Submit left edits open until the deadline (EM3)". |
| (d) Weekly emails Mondays + WInS | "Weekly emails will be sent on Mondays. We will also post them on the Wharton Investment Simulator (WInS)" (EM4) | `questions_v2.md:22-25`, `:112`; `Caplet_Login_Checks_v2_20Oct2026.md:61` (row 3), `:62` (row 4); `Caplet_M1_Meeting_Pack_v2_20Oct2026.md:94`; `week4_impact.md:35`; `timeline.md:120` (row 34, the Week 1 PDF on WInS) | CONFIRMS | Add "Mondays (EM4)". Add a recurring check: leader reads the inbox **Tue 07:00 Sydney** each week (Week 5 ~Mon 26 Oct 23:30; Week 6 ~Tue 3 Nov 00:30, INFERENCE from the 08:07-08:46 ET pattern). Put it in `oct20/ops/operating_plan.md` §4b (`:205-220`). |
| (d) | same | `timeline.md:33-35` ("only one [Wharton email] is quoted anywhere ... No Wharton email is stored") | OBSOLETE | Change it to "Nine Wharton emails (15 Sep - 19 Oct) are now in `SP/oct23/EMAILS.md` (another Knox team's copies, excerpts)". |
| (e) 7,300+ teams | "more than 7,300 teams this year" (EM4) | `/home/user/caplet-investment/CLAUDE.md:171` (2025-26: 6,300+ registered, ~2,300 final reports); `oct20/semis/semis_playbook.md:452` ("selected from 2,339") | CONFIRMS the history; new fact missing | Add "2026-27: more than 7,300 teams (Week 1 email, 28 Sep)". If the submit share matches last year (~37%), about 2,700 final reports (CALC from 2,339/6,300; an estimate, not a fact). |
| (f) $5 rule, later dropped | Week 1: "Any stock on WInS priced at $5 (or the equivalent of $5 in the local currency) or higher" (EM4, 28 Sep); Week 4 list: any stock "available on WInS", no price floor (EM9, 19 Oct) | `COMPETITION.md:80`, `:101`; `CLAUDE.md:26`; `compliance_matrix.md:75`, `:77` (Δ2, Δ6); `questions_v2.md:114`; `master_playbook_checked.md:605` | CONFIRMS | Add: "the $5 floor was also in the official Week 1 email (28 Sep); EM9 (19 Oct) drops it". Note that on 28-29 Sep the email said $5 while the session rules said $3 (`timeline.md:120`, row 34). No effect: Caplet holds no single stocks. |
| (f) | same | `CLAUDE.md:160` ("allowed: cash, stocks >= $5") | OBSOLETE | Change it to "stocks available on WInS (public $5 floor dropped by 19 Oct; session rules showed $3 on 29 Sep)". |
| (f) related: Week 1 already restricted BOTH contributions | "Approved securities (for BOTH contributions): ... Any Government/Treasury Bond available on WInS." (EM4, 28 Sep) | `COMPETITION.md:91-94` (the Week-2 email made Laura's real plan WInS-only); `CLAUDE.md:23`; `office/CHARTER.md:34`; `oct20/out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md:645-652`, `:692` ("The email changed Laura's real plan"); `TNA_Teardown_v2_21Oct2026.md:29` (#7 "The email changed Laura's real plan"); `timeline.md:226` (TP5) | CONTRADICTS (first date) | Add: "first stated in the Week 1 email, Mon 28 Sep 09:07 EDT (= 23:07 AEST), before any trade; Week 2 (5 Oct) repeated it more strictly: 'Teams may not recommend or assume investments ... outside the approved competition universe'". The fact kit's 14 Oct FAQ point (`:649-650`) is consistent. |
| (f) related: "US Treasuries" | "Any Government/Treasury Bond available on WInS" (EM4, EM9); "Treasury bonds available on WInS" (EM5) | `COMPETITION.md:81` ("the 6 Oct email say US Treasuries"); `office/CHARTER.md:34` ("US Treasuries ... (6 Oct Wharton email)") | CONTRADICTS | Change it to "Government/Treasury bonds available on WInS (EM4, EM5, EM9). Caplet uses only US Treasuries; that is a team choice, not a Wharton rule." |
| (g) Credential | "To receive a participation credential, teams must meet all requirements and submit all deliverables" (EM4); "School Documentation – Friday, December 4 ... Teams can submit beginning November 9" (EM3) | `compliance_matrix.md:186` (row 69, "ON TRACK"); `questions_v2.md:231` | CONFIRMS | Add EM4 as a source. Add that School Documentation is a listed deliverable (EM3), so a missing letter costs the credential. |
| (g) | same | `oct20/ops/operating_plan.md:329` (R12, impact "H"); `:226` (letter request Fri 23 Oct); `office/workstreams/3_FINAL_REPORT.md:17`, `:29`; `COMPETITION.md:141-144` ("not yet requested as of 13 Oct") | CONFIRMS (raises the stakes) | R12: add "costs the participation credential (EM4) as well as the Final Report". The Fri 23 Oct request is today. Check it was sent. |
| (h) No client contact | "Teams are not permitted to contact the client." (EM7) | `CLAUDE.md:14`; `COMPETITION.md:50`; `office/CHARTER.md:20`; `compliance_matrix.md:120` (row 18); `questions_v2.md:68-69`, `:114`; `Caplet_Login_Checks_v2_20Oct2026.md:122`; `Caplet_M1_Meeting_Pack_v2_20Oct2026.md:123`; `master_playbook_checked.md:544`; `oct20/out/Caplet_Wharton_Questions_SendToday_20Oct2026.md:3` | CONFIRMS | Add EM7 as a third source next to RR:232 and SMC:25. |
| (i) Projections | "use the cash flows provided in the Client Case Study and reasonable return assumptions that are consistent with your investment strategy"; "Gains and losses in WInS should not be added to or subtracted from Laura's long-term portfolio projections" (EM5; repeated in EM7); "The $300,000 is your team's WInS simulator balance. The additional $150,000 ... will not be added to WInS." (EM5) | `COMPETITION.md:38-39`, `:74`; `CLAUDE.md:81`, `:159`; `office/CHARTER.md:35`; `office/workstreams/3_FINAL_REPORT.md:12-13`; `compliance_matrix.md:181` (row 64); `questions_v2.md:104`, `:441` | CONFIRMS | Add EM5/EM7 as sources. No change. |
| (i) related: not scored on WInS | "You are not being evaluated based on: Your portfolio ranking; How many trades you make; Whether you outperform other teams; Whether your portfolio makes money" (EM7) | `questions_v2.md:111`; `COMPETITION.md:38` | CONFIRMS | Add EM7. |
| (j) Freeze 5:00 pm ET | "Trading ends on November 6 at 5:00 p.m. ET, and your portfolio will be final." (EM9); "Official trading will end on November 6, when your Investment Policy Statement is due" (EM7) | `COMPETITION.md:21` ("Fri 6 Nov, 4:00 pm \| Sat 7 Nov 08:00"), `:76` ("to 6 Nov 4:00 pm ET"); `office/workstreams/2_IPS.md:4` ("at the 4:00 pm ET close, probably about Sat 7 Nov 08:00 Sydney (an inference)") | CONTRADICTS | Change it to "Trading ends Fri 6 Nov 5:00 pm ET = Sat 7 Nov 09:00 Sydney (EM9), with the IPS deadline. The US market closes 4:00 pm ET = 08:00 Sydney, so an order entered after that probably never fills. The team's last order stays the Wed 4 Nov close (Thu 5 Nov 08:00)." |
| (j) | same | `master_playbook_checked.md:95` ("Freeze at the 4:00 pm EST close (exact cut-off UNVERIFIED)"), `:690` ("the exact freeze time"); `runbooks_checked.md:130` (row "4:00 pm ET; exact freeze time UNVERIFIED"), `:572`; `oct20/ops/operating_plan.md:38`, `:341`, `:346`; `timeline.md:190-191`; `compliance_matrix.md:50`, `:150` (row 38, SESS "ends 4:00 pm ET"); `Caplet_Login_Checks_v2_20Oct2026.md:28`, `:78` (row 19 "End time shown: replace the UNVERIFIED freeze time"); v1 `:22`; `oct20/verify_frblue/fr_prep_v2_checked.md:572` (W0 "exact WInS cut-off UNVERIFIED"); `questions_v2.md:142` (D), `:228` ("freeze (Fri 6 Nov 4:00 pm ET = Sat 7 Nov 08:00)"), `:502` | OBSOLETE (the UNVERIFIED label) / CONTRADICTS ("freeze = 4:00 pm") | Change it everywhere to "trading ends 5:00 pm EST (EM9) = Sat 7 Nov 09:00; last market fill at the 4:00 pm close = 08:00". Keep row 19's Session Rules screenshot, because the team's 29 Sep transcription said "ends 6 Nov 2026 4:00 pm ET" and conflicts with EM9. If WInS still shows 4:00 pm, record both. Whether a bond order placed 4:00-5:00 pm gets an end-of-day fill is UNVERIFIED; do not use that window. |
| (j) | same | `START_HERE.md:59`; `CLAUDE.md:30`, `:87`; `oct20/verify_frblue/fr_prep_v2_checked.md:306` (valuation date = 6 Nov close) | CONFIRMS | Add "5:00 pm ET = Sat 7 Nov 09:00". The FR valuation date (6 Nov close) is unchanged. |
| (k) FR instructions 09:00 ET | "Monday, November 9, 9:00 a.m. ET: Instructions and requirements for the Final Report posted" (EM7, 12 Oct; again EM9) | `COMPETITION.md:23` ("~Tue 10 Nov"), `:139`; `CLAUDE.md:87`; `office/workstreams/3_FINAL_REPORT.md:4`, `:38`; `compliance_matrix.md:185` (row 68); `questions_v2.md:89`, `:122-123` (release hour "not worth asking"), `:408`; `semis_playbook.md:282` | OBSOLETE (hour unknown) / CONFIRMS (date) | Change it to "Mon 9 Nov 9:00 am EST = **Tue 10 Nov 01:00 Sydney** (EM7, EM9)". Remove the release hour from the not-worth-asking list: it is answered. |
| (k) | same | Already in `week4_impact.md` §3 (master `:53`, `:96`, `:488`; Login v2 `:87`; ops `:37`, `:230`; fr_prep `:30`, `:575`, `:644`, `:704`) | CONFIRMS week4_impact | Upgrade the source in `week4_impact.md:23`, `:53`, `:108`, `:162`, `:170`, `:185`, `:192` from "Week 4 email, team copy" to "Week 3 (12 Oct) and Week 4 (19 Oct) emails, general sends". The time was known from 12 Oct. Also `master_playbook_checked.md:689` ("the instructions' release hour") and `operating_plan.md:346-347` ("the hour the Final Report instructions are released") become answered. `TNA_Teardown_v2_21Oct2026.md:57` CONFIRMS. |
| (l) Week 2 = Mon 5 Oct | "Week 2" sent Mon 5 Oct 23:07 Sydney = Mon 5 Oct 08:07 EDT (EM5) | Every "6 Oct email": `CLAUDE.md:23`; `COMPETITION.md:81`, `:91`; `office/CHARTER.md:34`; `master_playbook_checked.md:66`, `:181`, `:498`, `:691`; `Caplet_Login_Checks_v2_20Oct2026.md:61`, `:62`, `:63`, `:91` (v1 `:49`, `:50`, `:78`); `Caplet_M1_Meeting_Pack_v2_20Oct2026.md:66`, `:76` (v1 `:44`, `:62`); `Caplet_TNA_Fact_Kits_v2_20Oct2026.md:265`, `:645`, `:685`, `:689`, `:708`, `:721`; `timeline.md:140` (row 49), `:226` (TP5), `:252` (G7); `operating_plan.md:111`; `compliance_matrix.md:28` (EM2), `:217`; `fr_prep_v2_checked.md:412`, `:498`; `questions_v2.md:112`, `:140`, `:504`; `TNA_Teardown_v2_21Oct2026.md:29` | CONTRADICTS (date) | Replace "6 Oct email" with "Week 2 email (Mon 5 Oct, 08:07 EDT = 23:07 Sydney)". In `timeline.md`, move row 49 before row 48 and set its time to "Mon 5 Oct 23:07 AEDT \| 5 Oct 12:07 UTC", strength "strong (general send; Caplet copy to confirm)". The team's own "week 2 email" label is right. The fact kit's `:689` note on the accepted reflection ("6 October guidance") carries the same wrong date. |
| (l) | same | Arrival-time gaps: `Caplet_TNA_Fact_Kits_v2_20Oct2026.md:267`, `:647`, `:693`; `timeline.md:252` (G7); `compliance_matrix.md:217` (§5 item 5); `Caplet_Login_Checks_v2_20Oct2026.md:62` (row 4, condition "arrived before the IBTM order") | OBSOLETE | Mark them answered: "sent 37 h 55 min before the IBTM order (EM5). The row-4 condition is met on the send time. A student confirms Caplet's own copy (sender/time screenshot) before the label is used." The text matches `COMPETITION.md:91-92` word for word, so the row-4 branch "Text differs from COMP" does not apply. |
| (m) Office hours | "office hours Mon-Fri 9-5 ET" (EM4) | `runbooks_checked.md:74-76`, `:114-117`, `:126-129` ("hours UNVERIFIED"), `:569-570` | OBSOLETE (the label) | Drop "UNVERIFIED" from the working-day rows: Mon-Fri 9-5 ET (EM4). The Sydney windows already shown (00:00-08:00 before 1 Nov; 01:00-09:00 after) are right. |
| (m) | same | `Caplet_Wharton_Questions_SendToday_20Oct2026.md:5`; `Caplet_Login_Checks_v2_20Oct2026.md:73` (row 14), `:85` (row 26: "Contact Us before Sat 7 Nov 01:00 Sydney = Fri 6 Nov 9:00 am EST"); `Caplet_M1_Meeting_Pack_v2_20Oct2026.md:7`, `:101`; v1 `:49`, `:85`; `questions_v2.md:73-76` | CONFIRMS | Add EM4. A reply can only land in Sydney 00:00-08:00 (01:00-09:00 from 2 Nov), Tue-Sat. Read the inbox each morning before school. |
| (m) | same | `Caplet_Login_Checks_v2_20Oct2026.md:99` ("Excluded: ... Wharton's office hours"); `questions_v2.md:515` | OBSOLETE (hours) | Hours answered (EM4). Reply speed is still unknown. |
| (n) Shared number in TEAM USER ID | TEAM USER ID "<TeamName>-<number>", "the SAME 8-digit number as Caplet's WInS username (so the number is shared across the school's teams)" (EM8) | `office/CHARTER.md:21` ("the WInS username or account number"); `Caplet_Login_Checks_v2_20Oct2026.md:46`, `:117` ("Crop the WInS username, account number"); `operating_plan.md:220`; `office/workstreams/2_IPS.md:45`; `fr_prep_v2_checked.md:568` | CONFIRMS (keep the rule), with a scope change | Add: "The number is not Caplet's own. It is shared by Knox teams (EM8; INFERENCE: the advisor or school account; an advisor may register up to five teams, `compliance_matrix.md:195` row 78). With 'Caplet' public, the number plus the team name rebuilds the likely username, so the number stays out of every public file and screenshot **for any Knox team**, including copies of other teams' emails." |
| (n) | same | `runbooks_checked.md:527` (F4: copy the username from WInS; sample "sample_team-1234567", IPS:131); `Caplet_Login_Checks_v2_20Oct2026.md:83` (row 24); `week4_impact.md:89`, `:251` | CONFIRMS (still exact copy), plus a new check | Add: "Compare the **whole** string (team-name part, separator, number) with the WInS login screen. A matching number proves nothing, because every Knox team has it." |
| (n) | same | `questions_v2.md:62`; `runbooks_checked.md:441`; `Caplet_Wharton_Questions_SendToday_20Oct2026.md:35` ("Are any team identifiers needed?"), `:43` | OBSOLETE (partly) | Wharton keys teams by "Team User ID" "<TeamName>-<number>" (EM8). In Contact Us, fill the optional Team User ID from **Caplet's own** Wharton email (e.g. its 16 Oct reminder, if received), from the private record, never from another team's email. Whether it is identical to the WInS username is UNVERIFIED. |
| (o) TNA requirements Box link | "Requirements for the Trading Notes Analysis can be found here: https://upenn.app.box.com/s/3pxn798a1lnlifkikj4g56srmg2ijuo6" (EM6) | Fetched 23 Oct 2026 04:05:20 UTC (HTTP 200; `SP/oct23/emails_sweep/fetch/box_tna.html`). Box metadata: "2026_WGY_Trading Notes Analysis-FINAL.pdf", 62,427 bytes, sha1 `b7fa353d153ad93d525fee20ac4609476373acbf`. Identical to repo `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.pdf` | CONFIRMS | Note in `runbooks_checked.md:46-50` (§0 item 1, "no published TNA format rule") and `office/workstreams/1_TNA.md:9`: "the requirements link Wharton emailed on 12 Oct is this same file (sha1 match, 23 Oct)". |
| (o) | same | `master_playbook_checked.md:139` ("the complete TNA requirements are on the logged-in Pages → Deliverables page ..., which nobody has read yet"); `runbooks_checked.md:476` (P1 "§0 item 1 rests on the public copy only"); `Caplet_Login_Checks_v2_20Oct2026.md:59` (row 1(a)) | OBSOLETE | Mark row 1(a) and the P1 caveat "answered by EM6: the emailed requirements = the public TNA PDF". Row 1(b) (trading activity) stays. |
| (p) Removal = DQ | "Teams may not add members. Requests to remove a team member ... must be submitted in writing by the Advisor and approved ... Teams that remove a member without prior approval will be disqualified." (EM7); "Team rosters are now finalized" (EM9) | `compliance_matrix.md:161` (row 49); `CLAUDE.md:74`; `Caplet_M1_Meeting_Pack_v2_20Oct2026.md:33` | CONFIRMS | Add EM7. |
| (p) | same, plus "You can edit your team information ... until 5:00 p.m. ET on October 9" (EM3) | `COMPETITION.md:19` ("Team roster (locked once submitted)"); `CLAUDE.md:20` ("Roster submitted (locked)"); `timeline.md:147` (row 56 "submitted and locked") | CONTRADICTS (mechanism) | Change it to "submitted; editable until Fri 9 Oct 5:00 pm ET (EM3); final since (EM7, EM9)". Add the removal rule to `COMPETITION.md` §5 "Roster". |
| (p) | same | `operating_plan.md:39`, `:331` (R14 "the advisor contacts Wharton if needed"); `:318` (R1 author ill) | CONFIRMS | R14 mitigation: add "Never drop or sideline a member informally. Any removal needs the advisor's written request **and** Wharton's approval first (EM7)". |
| (q) IPS is a form | "Update: The Investment Policy Statement will now be submitted as a form on SurveyMonkey Apply. You will not submit a PDF. All other requirements remain the same." (EM9, Mon 19 Oct 08:46 EDT, general send) | `week4_impact.md:11-12`, `:37-42` ("The change is not public ... TEAM-REPORTED ... date and arrival UNVERIFIED"); `:203` (timeline row "date and arrival UNVERIFIED") | OBSOLETE (status) | Change it to "Official Wharton email to all team leaders, sent Mon 19 Oct 08:46 EDT = 23:46 Sydney (EM9; seen in another Knox team's inbox). Still not on the public pages as of 21 Oct 07:12 UTC." The instruction to follow the email stands. |
| (q) | same | Not in week4_impact's sweep: `compliance_matrix.md:111` (row 9 fix "Pass a PDF format gate"), `:112` (row 10 "2-page maximum ... A PDF exported now runs to 4 strategy pages"); `questions_v2.md:141` (C "IPS form (PDF, 5 MB)"); `Caplet_Login_Checks_v2_20Oct2026.md:60` (row 2 "PDF only, 5 MB"); `office/workstreams/2_IPS.md:16`, `:43`, `:55`; `COMPETITION.md:130-131`; `CLAUDE.md:86` ("TNR 12 double-spaced") | OBSOLETE (PDF, 5 MB, export) / UNCHECKABLE (TNR, spacing, page caps) | Use week4_impact's wording: row 9 → "form-text gate on the paste files (Tue 3 Nov)"; row 10 → "page cap UNVERIFIED in a form; the word caps are the binding test"; 2_IPS `:43` → "form-text gate on the paste files"; `:55` → "pitch ≤45 / IPS ≤470 on the paste files; form limits from the Tue 27 Oct screenshots". (week4_impact already lists `COMPETITION.md:131`, 2_IPS `:16`, `:43`, `:55` and `CLAUDE.md`; this adds the compliance rows, QV2 C and Login row 2.) |
| (r) Advisors can view teams in WInS | **Not in the nine emails.** Nearest: SMApply registration uses "the email address your advisor provided on WInS" (EM1); the shared number (EM8) | `Caplet_Login_Checks_v2_20Oct2026.md:63` (row 4a cites GYF:268 "The advisor will be able to see team login information and their activity report" and RR:245) | CONFIRMS by inference only | Keep row 4a's public-page sources. Add EM1 (the advisor set up the WInS accounts) and EM8 (one number across Knox teams) as consistent evidence. "Advisors can view **all** teams in WInS" (beyond their own) is UNVERIFIED. Don't add it as a fact. Impact: the advisor already sees Caplet's login information, so the privacy rules concern public files, not the advisor. |
| (r) related: advisor as sounding board | "Know your client ... If anything is unclear, discuss it with your advisor." (EM9) | `COMPETITION.md:157`, `CLAUDE.md:70` ("the advisor handles administrative work only") | CONFIRMS (with nuance) | Add: Wharton invites client questions to the advisor (EM9); the advisor still "may not make decisions" (`compliance_matrix.md:164`, row 52). "Admin only" is the team's practice, not a Wharton limit. |
| extra: "Team leaders are final" | "Team leaders are final" (EM4) | `compliance_matrix.md:160` (row 48); `Caplet_M1_Meeting_Pack_v2_20Oct2026.md:54`; `operating_plan.md:319` (R2); `runbooks_checked.md:449` | CONFIRMS | Add EM4. A leader swap is not a fallback. R2's "submit 36-48 h early" stays the main defence. |
| extra: TIPS/STRIPS ban timing | Week 4 permitted list "(for BOTH contributions, the Investment Policy Statement and Final Report)"; NOT permitted adds "TIPS" and "STRIPS" (EM9, 19 Oct 12:46 UTC) | `Caplet_TNA_Fact_Kits_v2_20Oct2026.md:651` ("When the STRIPS line was added is UNVERIFIED"); `timeline.md:187` (row 81, change time UNVERIFIED), `:229` (TP8); `compliance_matrix.md:76` (Δ3); `questions_v2.md:124-125`; `COMPETITION.md:82`, `:96-101`; `CLAUDE.md:24-26` | CONFIRMS / OBSOLETE (partly) | Add: "Wharton announced it in the Week 4 email, sent 19 Oct 12:46 UTC. The FAQ showed it by 13:04 UTC." The FAQ edit time is still only bounded (after 16 Oct 02:46 UTC). |
| extra: 16 Oct reminder | Sent to a team that had "not submitted the Trading Notes Analysis"; "We will not accept any late submissions." (EM8) | `Caplet_Login_Checks_v2_20Oct2026.md:62` (row 4 inbox search), `:70` (row 11 opt-in) | missing | Add to row 4: "Caplet should also hold a 16 Oct 'Remember to Submit' email (Fri 16 Oct 23:45 Sydney) carrying its own Team User ID. If it is absent, check spam and the opt-in (row 11)." |
| extra: WInS as evidence | "WInS provides evidence of how your team implemented its strategy ... Be sure to document your research, decision-making, and reasoning throughout the competition." (EM5); "your portfolio provides evidence of the decisions your team made" (EM7) | `operating_plan.md:227` (weekly journal and decision log); `oct20/verify_frblue/fr_prep_v2_checked.md:306`; `compliance_matrix.md:188` (row 71) | CONFIRMS | Add EM5 as the source for the weekly journal and decision log. |

## 4. Wharton questions the emails now answer

| Question (file:line) | Answer (source) | What changes |
|---|---|---|
| Release hour of the 9 Nov FR instructions (`questions_v2.md:122-123`; `master_playbook_checked.md:689`; `operating_plan.md:346-347`; `fr_prep_v2_checked.md:704`) | 9:00 a.m. ET Mon 9 Nov = Tue 10 Nov 01:00 Sydney (EM7, EM9) | Drop it from every list. First look Tue 10 Nov 07:00. |
| Exact WInS freeze time (`questions_v2.md:142` D, `:502`; `master_playbook_checked.md:690`; `runbooks_checked.md:572`; `operating_plan.md:38`, `:346`) | "Trading ends on November 6 at 5:00 p.m. ET" (EM9) | 5:00 pm ET = Sat 7 Nov 09:00. Last fill at the 4:00 pm close. Keep the Session Rules screenshot because of the 4:00 pm transcription. |
| Wharton office hours (`Caplet_Login_Checks_v2_20Oct2026.md:99`; `runbooks_checked.md:569`) | Mon-Fri 9-5 ET (EM4) | The working-day rows lose "UNVERIFIED". |
| Week-2 ("6 Oct") email text and arrival time (self-check B, `questions_v2.md:140`; Login row 4; fact kit D7 `:265-267`; `timeline.md:252` G7; `compliance_matrix.md:217`) | Sent Mon 5 Oct 08:07 EDT. The text matches `COMPETITION.md:91-92` (EM5) | Before the IBTM order by about 38 h. A student confirms Caplet's own copy. The "refined" label condition is met on the send time. |
| Where the complete TNA requirements are (self-check A part (a), Login row 1; `master_playbook_checked.md:139`; `runbooks_checked.md:476`) | EM6's Box link = the public TNA PDF (sha1 match, fetched 23 Oct) | No hidden TNA format rule exists. |
| How the roster submission worked (`runbooks_checked.md:390-391` item 7; `master_playbook_checked.md:688`) | Submit → "Team Roster Submitted" email → editable until the deadline → stage advanced on 12 Oct (EM3, EM6; standard team) | The three-case rule is simplified (section 2). |
| When the TIPS/STRIPS lines were added (`questions_v2.md:124-125`) | Announced in the Week 4 email, 19 Oct 12:46 UTC (EM9) | It is history only. Cite EM9. |
| Weekly emails: where and when (`questions_v2.md:112`) | Mondays, also posted on WInS (EM4) | Add a Tuesday-morning inbox check. |
| Non-US government bonds (`questions_v2.md:126-128`) | "Any Government/Treasury Bond available on WInS" for BOTH contributions (EM4, EM9) | The test is "listed on WInS". Caplet plans none. Fix "US Treasuries" wording (table, (f) related). |
| Does WInS performance count (`questions_v2.md:111`) | Not ranking, number of trades, outperformance or profit (EM7) | Already answered; one more source. |

**Partly answered (defaults strengthened, question still open):**
- **Q3 "required trading activity"** (`questions_v2.md:225-249`; SendToday item 3 `:25-28`; `compliance_matrix.md:115` row 13, `:213`). None of
  the excerpts (Weeks 1-4) defines a minimum. EM7 says teams are not evaluated on "How many trades you make". EM9 says
  "Use WInS to demonstrate your strategy". The default (hold; never trade for a count) is stronger. Login row 3 (read
  the Week 1 copy on WInS in full) is still useful, because EMAILS.md is excerpts.
- **Q5 confirmation / reopening** (`questions_v2.md:270-284`; SendToday item 5 `:33-37`). By the roster precedent, a
  confirmation email follows Submit and edits stay open until the stage deadline (EM3). Not confirmed for the TNA form.
- **SendToday item 5 "Are any team identifiers needed?"** (`:35`). Wharton identifies teams by "Team User ID"
  "<TeamName>-<number>" (EM8), so use Caplet's own one in Contact Us.
- **Q6 leader cannot submit** (`questions_v2.md:288-306`). "Team leaders are final" (EM4) rules out a swap as a fallback.
  Who else may press Submit is still unanswered.
- **Q8 uninvested cash** (`questions_v2.md:326-344`). Weeks 1, 2 and 4 list only stocks, ETFs and Government/Treasury
  bonds "available on WInS" for both contributions, and Week 2 says "Teams may not recommend or assume investments in
  securities or asset classes outside the approved competition universe" (EM5). That strengthens the default (no cash
  holding; a WInS-listed short Treasury ETF). Cash is still not named either way.
- **Q9 TIPS/STRIPS scope** (`questions_v2.md:346-361`). The ban for both contributions is confirmed (EM9). Whether it
  covers WInS-listed ETFs built on them is still open.

## 5. Still open

From `questions_v2.md` and `week4_impact.md`, after this sweep:
1. **Q1** (`questions_v2.md:165-194`): where AI use for the TNA is recorded. Not addressed by the emails.
2. **Q2** (`:196-223`): word counting (headings, hyphens, numbers, whether the quoted note counts).
3. **Q3** (`:225-249`): a written definition of "required trading activity" and the "portfolio management guidelines".
4. **Q4** (`:251-268`): what to paste with each note (date, time, security). The requirements PDF is unchanged, so the form decides.
5. **Q5** (`:270-284`): whether the TNA (and IPS) form stays editable after Submit until the deadline.
6. **Q6** (`:288-306`): who may submit if the leader cannot.
7. **Q7** (`:308-324`): WInS login and export after the freeze. EM7 and EM9 say only "frozen" and "final".
8. **Q8** (`:326-344`): cash in Laura's plan, if the team still wants it asked.
9. **Q9** (`:346-361`): TIPS/STRIPS-based ETFs.
10. **Q10** (`:363-384`): software or browser tools on WInS screens.
11. **S1** (`:388-404`): the volume rule for bond orders.
12. **Q11-Q14** (`:411-466`): wait for the Tue 10 Nov 01:00 instructions.
13. **Q15-Q19** (`:470-476`): Top 50 only.
14. **week4_impact Q1-Q4** (`week4_impact.md:281-285`): whether TNR, spacing, margins and page caps apply to the IPS form;
    where the title-page items go; whether headings count and are typed; whether the form's counters define the limits.
    Opening the form on Tue 27 Oct may answer Q2-Q4 without asking.
15. **TNA vs semifinal selection** (`questions_v2.md:117-121`; `compliance_matrix.md:187` row 70). EM9 ("connects every
    part of the competition ... to your Investment Policy Statement and Final Report") is not decisive.

New questions from this sweep (team checks first; ask Wharton only if a check fails):
16. At what hour on Mon 26 Oct ET does the IPS task open, and does an "Advanced to Next Stage" email announce it? Check
    the task list Tue 27 Oct 07:00.
17. Is Caplet's Team User ID string identical to its WInS username? Compare the strings privately, from Caplet's own email.
18. Does the WInS Session Rules page now show 5:00 pm or 4:00 pm ET as the end time (Login row 19)? If 4:00 pm, record
    both; EM9 is the newer official source.
19. Does a WInS bond order entered between 4:00 and 5:00 pm ET on 6 Nov fill at end-of-day prices? Don't plan on it. The
    last order stays Wed 4 Nov.

## 6. Files

- `SP/oct23/emails_sweep/emails_sweep.md` (this file).
- `SP/oct23/emails_sweep/fetch/box_tna.html` and `fetch_time.txt`: the TNA Box page fetched 23 Oct 2026 04:05:20 UTC.
- `SP/oct23/files.txt`: the list of files swept.
