# Pre-mortem 2: it is Sat 5 Dec 2026 and Caplet is not in the Top 50. Why? (written Tue 20 Oct 2026, about 11:05 Sydney)

> **Checked copy (20 Oct 2026): this file applies fixes E1-E23 of `oct20/verify_pm2/verify_pm2.md` (each marked "[fixed 20 Oct, E#]") and replaces the Top-10 actions with its corrected table, except that E5's SMApply rule is overridden by the three-case rule in `oct20/verify_runbook/runbooks_checked.md` (§0 item 2, §3.5).**

**AI-generated research (Claude Code, wave H) for Team Caplet. Not text to submit.** It lists failure modes, the evidence for each, and actions with owners (roles) and deadlines. It drafts no TNA reflection, IPS sentence, pitch, Final Report or co-sponsor wording, and it ranks no teammate. If the team uses it, log the use in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy: "If you use AI to assist you in any way during the competition, how you use it must be recorded in your Works Cited pages", `oct20/compliance/web/ai_policy.txt:224`). Every likelihood and impact score below is AI judgement built on cited evidence. It is not a probability.

**Read only Section 0 and the two tables in Sections 1 and 5.** The rest is the evidence. This file is itself part of the volume problem it describes (failure mode F15).

**Sources** (all read on 20 Oct 2026; the "Verified 20 Oct" banner of each file was applied first, and corrected facts are used throughout):
- R16 = `/home/user/snap/main/research/assistant_review_2026-10/04_What_Stops_Us_Winning_16Oct2026.md` (Part 1 items 1-25; Part 15 pre-mortem PM items).
- U19 = `oct19/out/Caplet_Update_19Oct2026.md` (fact-checked 19 Oct).
- 20 Oct files (`oct20/<folder>/<file>`): RUB `rubric/rubric_scoring.md` + VRA `verify_rub_alt/verify_rub_alt.md`; SP `semis/semis_playbook.md`; PW `pastwinners/past_winners_deep.md` + VPW `verify_pw/verify_pw.md`; CM `compliance/compliance_matrix.md` + VAD `verify_admin/verify_admin.md`; AIR `ailog/ai_use_register.md`; ART `artic/artic_bank.md`; EXP `exposure/exposure_audit.md` + VTE `verify_tl_exp/verify_tl_exp.md`; IFX `ipsfix/ips_fix_list.md` + VIF `verify_ipsfix/verify_ipsfix.md` (and its checked copy); CR `clientread/client_readers.md`; REC `reconcile3r/reconcile_3r.md`; LCK `lockin/lockin_2031.md`; TC `tradecheck/trade_check_pack.md` + VTR `verify_trade/verify_trade.md`; OPS `ops/operating_plan.md`; DLT `delta/delta.md`; AW2 `askwharton2/questions_v2.md` + VA2 `verify_ask2/verify_ask2.md`; RBC `verify_runbook/runbooks_checked.md` (the checked runbook; its three-case SMApply rule overrides verify_pm2 E5) and VPM2 `verify_pm2/verify_pm2.md` (the check applied here) [fixed 20 Oct, E5]. Numbers register H-rows: NRG `numreg/numbers_register.md`.
- `oct19/`, `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`. Official rules: `/home/user/caplet-investment/competition/official/2026_27/`. Live-page copies: `oct20/compliance/web/` (RR = `rules_roles.txt`, SMF = `sm_faqs.txt`, AIP = `ai_policy.txt`, GYF = `gy_faq.txt`, TOU = `trading_outside_us.txt`). STT = Stock-Trak terms as quoted in VA2. SDT = the official school documentation template. NS26 = the 2025-26 semifinal "Next Steps" PDF (SP short form). TL = `oct20/timeline/timeline.md` (row numbers). ND = `oct19/drive/notes_and_discussions_live.md`. FAQ:83 is RUB's FAQ copy.

**Times** are Sydney (AEDT, UTC+11) unless marked ET. Sydney is 15 hours ahead of ET until Sun 1 Nov 17:00 Sydney, then 16 hours ahead. Deadlines: TNA Sat 24 Oct 08:00; trading freeze about Sat 7 Nov 08:00 (the 4:00 pm EST close; exact freeze time UNVERIFIED); IPS Sat 7 Nov 09:00; Final Report and school letter Sat 5 Dec 09:00. "We will not grant any deadline extensions" (`smapply_public_2026-10-14/deliverables.txt:29`).

**Baseline.** Nothing has changed since 18 Oct. The delta check (DLT, Tue 20 Oct 10:08-10:15) found no commit, PR comment, Drive edit or Doc comment by the team after the IPS Report's last edit (Sun 18 Oct 11:49:32). The pending AI suggestions are neither accepted nor rejected, and there is no student-written TNA or IPS text anywhere.

---

## 0. Bottom line

1. **The most likely story of failure is authorship, not strategy.** Today every word the team could submit is AI text: the accepted IPS is 97% AI exemplar v11, the three reflections are v11 word for word and still tagged "[AI]", and the pending suggestions are v12 exactly (U19 §4a; DLT §2). The TNA is due in under four days. F1 and F2 together are the top risk, and both are fully preventable until the moment of submission.
2. **The record risk is next.** No vote, role, author or meeting is on record. The journal stopped 27 minutes before the first trade (ART §1). The AI-use log misses the source of today's text. Articulation and the "is this yours?" question (drill K9) depend on records that only students can create, starting tonight (F3, F5, F6).
3. **Most of the 16 Oct list did not move.** Of the 23 failure modes here, 7 are worse than on 16 Oct, 12 are unchanged, 1 is improved (the coupon analysis, though not the decision) and 3 are new (one of them, F22, only partly) [fixed 20 Oct, E7]. Every 16 Oct weekend task (Sat 17 / Sun 18 Oct) has no record of being done, including making the repo private and reading the Week-One email.
4. **Some damage is already locked in and can only be disclosed:** the VT and Nov-2040 WInS notes each contain a 13-word clause copied verbatim from public AI example notes (VTE T12, X8); the pre-20 Oct decision record is missing; and the repo, the fork and git history have been public since 19 Sep (a client contact blob since 27 Sep). Honest disclosure is the only fix for these.
5. **The strategy is still the asset, but its claims are fragile.** "Certainty" has no defined standard. The accepted text covers shortfalls with "her other assets", which reads as outside money (case:91-92). The live "three of four reach the top" is false under coupon option 3r as written (under half) [fixed 20 Oct, E2]. The 3r study headline of "0.02% short" is on a basis REC says not to quote; the current plan (option 1) is about 1 in 7 short, or about 1.4% if Laura's retained half stays on call (REC banner 2) [fixed 20 Oct, E4, E1]. These are fixable by the Tue 27 Oct votes and student-rebuilt numbers (F7, F9, F10, F11).
6. **The structure is unforgiving.** About 2% of submitting teams reach the Top 50 (49 of 2,339 in 2025-26, SP intro). Selection rests on the IPS and the Final Report ("based on the strength of their Investment Policy Statement (IPS) and Final Reports", RR:264). There is no feedback ("Teams will not receive individual feedback", SMF:81-82) and there are no extensions. The Final Report gets a 25-day window and must already hold everything a semifinal could use (F12, S).

---

## 1. Ranked list

**Scoring (AI judgement, from the evidence cited in Section 2).**
- **L (chance that this mode happens and costs the Top 50 if nothing more is done):** 5 = near certain (already happening, and nothing on record stops it); 4 = likely; 3 = plausible; 2 = possible if a check is skipped; 1 = remote. Whether a fix has an owner or a record of action is shown in the Status column, not in L; only F18 changes under this reading (E5) [fixed 20 Oct, E14].
- **I (impact on Top-50 selection):** 5 = can remove the entry from consideration (disqualification, "not considered for semifinal selection", a conduct finding); 4 = pulls a whole criterion below competent across the IPS and Final Report, or fails a required element; 3 = loses several criterion lines; 2 = minor marks.
- **Preventable after today?** Yes / Partly (part is already locked in) / No (disclosure only).
- **Rank** is by L × I. Ties are broken by the earliest date the mode becomes irreversible; equal dates keep the earlier order (re-checked with Python after the 20 Oct fixes) [fixed 20 Oct, E5, E8].
- **Status vs 16 Oct** compares with R16 Part 1 (items) and Part 15 (PM codes).

| Rank | ID | Failure mode | L | I | L×I | Preventable after today? | Irreversible from (Sydney) | Status vs 16 Oct |
|---|---|---|---|---|---|---|---|---|
| 1 | F1 | AI-written text submitted as the students' own (TNA, then IPS) | 4 | 5 | **20** | Yes | TNA submit (target Thu 22 Oct 20:00; hard Sat 24 Oct 08:00); IPS Sat 7 Nov 09:00 | **Worse** |
| 2 | F3 | No recorded votes, roles or reasons; key calls not demonstrably the students' own | 4 | 4 | **16** | Partly | Already, for everything before 20 Oct; D0 by Wed 21 Oct; vote set B Tue 27 Oct; IPS Sat 7 Nov | Unchanged |
| 3 | F2 | Disguise: the "[AI]" tag stripped, or AI text "humanised" | 3 | 5 | **15** | Yes | TNA submit Thu 22 Oct | **Worse** |
| 4 | F18 | Submission mechanics fail (form fields, lock, wrong file, leader unreachable; a Submit pressed too early, or the TNA's real Submit never pressed) | 3 | 5 | **15** | Yes | Thu 22 Oct 20:00 (first submit) | Unchanged; score raised L2 → L3 [fixed 20 Oct, E5, E14] |
| 5 | F12 | Final Report built in the last days, or missing what the semifinal rules require | 3 | 5 | **15** | Yes | Pre-freeze WInS saves before Sat 7 Nov 08:00; pre-built modules Mon 9 Nov; due Sat 5 Dec 09:00 | Unchanged |
| 6 | F4 | TNA, IPS and filed notes contradict each other, or state false facts | 4 | 3 | **12** | Yes, until TNA submit | TNA submit Thu 22 Oct; IPS Sat 7 Nov | Unchanged |
| 7 | F6 | AI-use disclosure incomplete or false | 3 | 4 | **12** | Yes (evidence decays) | TNA AI rows before Thu 22 Oct; Works Cited Sat 5 Dec | **Worse** |
| 8 | F11 | Numbers and bases inconsistent (ladder cost, scale factor, odds, WInS vs plan) | 4 | 3 | **12** | Yes | TNA Thu 22 Oct (if a level is quoted); IPS; FR | **Worse** |
| 9 | F5 | Journal gap: Articulation has no dated, true stories | 4 | 3 | **12** | Partly | Practical: back-fill by Sun 25 Oct; FR Sat 5 Dec | Unchanged (gap 9 → 13 days) |
| 10 | F7 | No defensible certainty standard; "her other assets"; coupon gap undecided | 3 | 4 | **12** | Yes | Vote Tue 27 Oct; voted orders by Thu 5 Nov 08:00; IPS Sat 7 Nov | Improved analysis; decision unchanged; "her other assets" new |
| 11 | F13 | Competent but not memorable (an expected answer, an AI-originated idea) | 3 | 4 | **12** | Partly | IPS Sat 7 Nov (the principle must be in it) | Unchanged |
| 12 | F8 | Public repo and fork expose AI exemplars, history and personal data | 2 | 5 | **10** | Partly | Already, in part; next: TNA submit Thu 22 Oct | **Worse** |
| 13 | F14 | Single points of failure (leader = trader = submitter = contact; one Drive owner) | 2 | 5 | **10** | Yes | Each submit: Thu 22 Oct, Thu 5 Nov, Wed 2 Dec | Unchanged |
| 14 | F17 | IPS PDF fails the format gate (suggestions print, length, page fit, title page) | 2 | 5 | **10** | Yes | Sat 7 Nov 09:00 (internal Thu 5 Nov 20:00) | **Worse** |
| 15 | F15 | Exam weeks plus AI-material overload starve the students' writing time | 3 | 3 | **9** | Partly | Fri 23 Oct (Maths Ext 1 pm); Tue 27 Oct (Economics pm); Thu 5 Nov (Physics am) | Exams unchanged; overload **worse** |
| 16 | F9 | 2031 range odds misstated or the top rule left undefined | 3 | 3 | **9** | Yes | Vote Tue 27 Oct; IPS Sat 7 Nov; FR | **New** |
| 17 | F10 | Client knowledge thin: "flexibility", "responsible", willingness, currency | 3 | 3 | **9** | Yes | IPS Sat 7 Nov | Unchanged |
| 18 | F20 | 13-word verbatim AI clauses in the VT and Nov-2040 WInS notes go undisclosed | 2 | 4 | **8** | Yes (disclose); the note wording itself is locked since 7-8 Oct ET [fixed 20 Oct, E8] | Notes fixed since 7-8 Oct ET; disclose before Thu 22 Oct 19:00 [fixed 20 Oct, E8] | **New** |
| 19 | F16 | Note paste mismatch in the TNA | 2 | 4 | **8** | Yes | Thu 22 Oct 20:00 | Unchanged (more collisions found) |
| 20 | F19 | School documentation letter missing or wrong | 2 | 4 | **8** | Yes | Thu 3 Dec (last student day) | Unchanged |
| 21 | F21 | Late strategy reopen or a trade-execution error near the freeze | 2 | 3 | **6** | Yes | Team cutoff Thu 5 Nov 08:00 (Wed 4 Nov close); WInS itself freezes about Sat 7 Nov 08:00; IPS Sat 7 Nov [fixed 20 Oct, E18] | Unchanged |
| 22 | F22 | Text names a non-permitted or unlisted security (TIPS/STRIPS ban; "for BOTH contributions, the IPS and Final Report") | 2 | 3 | **6** | Yes | IPS Sat 7 Nov; FR | **Partly new** (the TIPS/STRIPS ban) [fixed 20 Oct, E7] |
| 23 | F23 | Eligibility edge cases: undefined "required trading activity", a paid outside reader, AI operating WInS | 1 | 5 | **5** | Yes | Freeze Sat 7 Nov 08:00; each submit | Unchanged; paid-reader angle new |
| - | S | Structural base rate: about 2% selected, no feedback, no extensions, FR instructions only on 9 Nov ET | - | - | n/a | Mitigate only | Each deadline | Unchanged |

**Already irreversible (disclose, don't hide):** the wording of all 15 WInS notes (F20); the absence of any decision record before 20 Oct (F3, F5); the public exposure since 19 Sep, including the client contact blob since 27 Sep and the commit-metadata email (F8); the 14-day git silence and the 13-day journal silence (F5).

---

## 2. Failure-mode cards

Each card gives: **Mechanism** · **Evidence** · **Hits** (deliverable / criterion) · **Irreversible from** · **Leading indicator** · **Cheapest prevention** (action, owner role, deadline) · **Status vs 16 Oct**.

### A. Authorship and integrity

#### F1. AI-written text is submitted as the students' own (L4 × I5 = 20)
- **Mechanism.** With no student text two days before the internal TNA deadline, the easiest path is to submit the [AI] reflections (or the IPS V5) after light edits. That breaks "You may not submit any work generated by an AI program as your own" (AIP:224) and the voice rule (AIP:208). At best it zeroes "authentic team voice" (deliverables.txt:59); at worst it is a conduct finding ("dealt with severely", AIP:224).
- **Evidence.** The accepted V5 is 97% exemplar v11, with about 10-14 new words; the reflections are identical to v11 once "[AI]" is removed; the pending text is v12 exactly (U19 §2, §4a). Nothing has changed since 18 Oct (DLT §2). RUB scores the live drafts as failing gate G5, "not scoreable" (RUB §4a). CM rows 1-3 class this as the only T1 (critical) cluster.
- **Hits.** TNA, IPS and FR; gate G5; Creativity line CP2 (scoring CP2 0 for AI text is a RUB convention, not a Wharton rule) [fixed 20 Oct, E22]; every criterion if the entry is removed.
- **Irreversible from.** The TNA submit click (team target Thu 22 Oct 20:00; hard deadline Sat 24 Oct 08:00). For the IPS, Thu 5 Nov 20:00 internal and Sat 7 Nov 09:00 hard.
- **Leading indicator.** By Wed 21 Oct 18:00 there is no student draft with its own revision history (a fresh Doc or tab typed by the author), and the IPS Report's modifiedTime is still 2026-10-18T00:49:32Z (re-run the DLT §5 check).
- **Cheapest prevention.** The three named authors write fresh reflections from their own notes, with every AI file, exemplar and kit closed: drafts Tue 20 Oct night, finals Wed 21 Oct 22:00 (OPS §2 M1-M3). Two non-authors score them before any AI check. Owners: the three authors; editor; deputy.
- **Status vs 16 Oct: Worse.** On 16 Oct V5 had 19% three-word overlap with the AI exemplar (R16 item 12). Since then it has been replaced by v11 (97%), and AI text was added to the reflections (U19 §4a).

#### F2. Disguise: the "[AI]" tag is stripped or the text "humanised" (L3 × I5 = 15)
- **Mechanism.** Under time pressure, someone deletes the "[AI]" label or reworks AI sentences until they no longer look AI-written. That turns a disclosed problem into "pass[ing] AI generated writing or work off as your own" (AIP:220). Wharton "reserves the right to engage ... forensic analysts" (RR:315), and the public exemplars make a comparison easy (F8).
- **Evidence.** A branch file says the [AI] label "must be deleted before export" (U19 §5b). A 17 Oct style study applies an AI-detection paper (StoryScope) to strip "AI tells" from "the whole text" (U19 §2; CM row 2). The [AI] tags were already removed once, on 16 Oct, while suggestions 5-13 were undecided; only an unmerged branch records it (AIR §4 item 4). The process slid from outlines to disguise in about 6 hours on 17 Oct (U19 §2).
- **Hits.** All deliverables; conduct (RR:313-315).
- **Irreversible from.** TNA submit (Thu 22 Oct).
- **Leading indicator.** "[AI]" disappears from the Doc while the text underneath is unchanged, or about 50% of its 12-word runs still match a public AI file (EXP §0 item 2 measured 47-63% for the live reflections).
- **Cheapest prevention.** At M1 tonight, the editor (with the deputy watching) rejects the 10 pending suggestions in Suggesting view and moves the accepted V5 and the three [AI] reflections into a tab labelled "AI reference", or deletes them from the live text only; version history stays, and nobody uses "Delete version history" or "Make a copy" to get a clean Doc (RBC §0 item 4) [fixed 20 Oct, E11]. Never strip only the tag (U19 §3a item 2). The team votes that no style study, detector loop or "humanise" pass is used. Owners: editor, deputy, whole team. Deadline: Tue 20 Oct 22:00.
- **Status vs 16 Oct: Worse.** R16 Part 16 said "Stop running AI detectors or 'humanising' passes". The style study came on 17 Oct.

#### F6. AI-use disclosure is incomplete or false (L3 × I4 = 12)
- **Mechanism.** The Works Cited has to record "how" AI was used "in any way" (AIP:224). A log that misses the main uses, or keeps the false template line, misrepresents the work. A judge comparing the Works Cited with the public repo would see the gap.
- **Evidence.** AIR finds 33 AI uses. Main's `caplet/docs/AI_USE.md` logs 7 fully and 1 partly (AIR §1). R29 (exemplars v1-v12, the style study, the Doc suggestions) has no row in any AI_USE.md; it is recorded only in a branch CLAUDE.md and the PR #9 description (VAD A1). The 16 Oct tag-removal rows exist only on the unmerged fervent-edison branch (AIR §4 item 4). AIU:49 ("authored 100% by student team members") and AIU:92 ("wrote all submitted text") are false today (AIR §4 items 1, 7). True totals: 208 commits on 22 branches, 103 by Claude cloud sessions (VTE T1). There are 17 gaps only students can fill, including each student's own AI accounts (AIR §5 S1-S17). Where to record AI use for the TNA is UNVERIFIED (AW2 Q1; VA2 §9 item 1).
- **Hits.** FR Works Cited; TNA disclosure; conduct if misrepresented (CM row 6).
- **Irreversible from.** The TNA's AI rows must be settled before the Thu 22 Oct submit. The Works Cited is due Sat 5 Dec. The evidence decays sooner: the branch rows would be lost if that branch were deleted, and student memory fades week by week.
- **Leading indicator.** By Thu 22 Oct 16:00 (text lock) there is no TNA AI-use row (OPS DL-16); AIU:49 is still unbannered on Sun 25 Oct.
- **Cheapest prevention.** The historian copies the AIR rows into the team's own log (students check them; no line is pasted into the Works Cited) and fills S1-S17 from memory at the Sun 25 Oct back-fill. They banner AIU:49 and AIU:92. They log the TNA rows before submission, including the 13-word note clauses (F20). Owner: historian / AI-log keeper; every student checks their own rows. Deadlines: Thu 22 Oct (TNA rows); Sun 25 Oct (back-fill).
- **Status vs 16 Oct: Worse.** R16 item 16 found a gap from 1-16 Oct. Since then: 12 exemplar versions, a style study, the Doc suggestions, the Research Office (about 10,200 words of AI instructions, U19 §5a) and these waves, all unlogged.

#### F20. 13-word verbatim AI clauses sit in two executed WInS notes (L2 × I4 = 8)
- **Mechanism.** The TNA must quote each note "exactly as it appears in WInS" (TNA:44). VT is a pick. Its note contains a clause copied from public AI example notes, so the TNA will submit AI words by rule. Undisclosed, that reads as passing AI work off; disclosed, it is a documented, honest limitation.
- **Evidence.** VT and the Nov-2040 Treasury note (B-T-4.250-15112040) each contain a 13-word run copied verbatim from the 30 Sep AI EXAMPLE notes (`archive/rab/trades/notes.md`, `archive/rab/sheets/rab_notes.csv`, public on main and last changed before the orders). IBTP and IBTO share 9- and 8-word runs (VTE T12, X8). The exposure audit's "reassuring check" was wrong (EXP banner). The notes were drafted from AI "Exemplar note" columns (CM row 46).
- **Hits.** TNA (CP2 capped, RUB §5b C2; a RUB convention, not a Wharton rule) [fixed 20 Oct, E22]; Works Cited.
- **Irreversible from.** Already: notes are treated as final: whether a saved note can be edited is not confirmed (WInS Notes tab R17; VTR E12) [consistency fix 20 Oct, row 17], and they were filed 7-8 Oct ET. Disclosure must be decided before Thu 22 Oct.
- **Leading indicator.** The TNA AI-use row (OPS DL-16) does not mention the VT clause at the M3 approval.
- **Cheapest prevention.** Record the clause and its source in the AI-use log, and decide at M2 (Wed 21 Oct 20:00), or by a logged chat vote by Thu 22 Oct 12:00, whether the TNA submission carries a one-line factual disclosure (AW2/VA2 batch-1 item 1(b) asks Wharton; the default favours a plain, factual line if the form has space, VA2 §0). Swapping VT for another pick does not remove the problem: IBTO and IBTP share runs too. Owner: historian; whole team decides. Deadline: Thu 22 Oct 12:00 (any line student-written before the 16:00 text lock; M3 only confirms) [consistency fix 20 Oct, G1].
- **Status vs 16 Oct: New.** 19 Oct found a 12-word match for VT against the Sheet exemplar (U19 §4c). 20 Oct found a 13-word source match and a second note.

#### F8. Public repo and fork expose AI exemplars, history and personal data (L2 × I5 = 10)
- **Mechanism.** Anyone, including Wharton reviewers, rivals or a search crawler, can fetch the exemplar reflections for the exact three TNA notes, the "humanise" tabs and the style study, then compare them with what Caplet submits. Personal data (the client's personal phone and email; a student's personal email and full name in commit metadata; a full name in .xlsx metadata) is exposed, against the team rule and against the spirit of the contact ban.
- **Evidence.** The repo and its fork are both public (EXP §0; VTE confirmed 19 Oct 22:50 UTC). While the fork is public, every commit in the network can be fetched through it by SHA, including the exemplar branch and the client-contact commit; this was tested anonymously (VTE X1, High). The client contact blob is reachable from 19 of 22 upstream and 16 of 19 fork branches (VTE X7). A personal email and a full name sit in commit author fields on main's history (EXP §2.2). Other 2026-27 teams' Laura Gao repos are indexed, which shows such repos are findable (PW §0 item 8). The fork account self-merged PR #10 four minutes after opening it (VAD A2). [fixed 20 Oct, E10] The WInS username or account number also sits in current public files (`competition/COMPETITION.md:3` and `:117`, `MONITOR.md:33`, `WATCHER.md:13`), on the five exemplar .docx title pages, in `caplet/ips_drafts/` PDF file names and in the .xlsx snapshot, plus two other branches (EXP §2.1 and banner); R16 item 6.6 (remove it from text files) is not done. Three Google files linked from the repo open for anyone with the link, one of them a copy of another school's Doc whose text mentions usernames and passwords (EXP §2.6). `team_list.md:32-51` names 15 students from the other Knox teams (EXP §2.2). VTE §2 also recommends GitHub's "Keep my email addresses private" and "Block command line pushes that expose my email".
- **Hits.** Conduct (RR:315 forensic review; RR:313-314 plagiarism, which also covers others copying Caplet); team data rule; CP2/CP4 perception (RUB §5b C9).
- **Irreversible from.** Partly already: public since 19 Sep, the client blob since 27 Sep, the fork since 16 Oct, and clones cannot be recalled. No Wayback or Software Heritage copy was found (EXP §0 item 4). The next step that cannot be undone is submitting the TNA while the exemplars are public (Thu 22 Oct).
- **Leading indicator.** The GitHub API still shows `"private": false` for the repo or the fork after Tue 20 Oct.
- **Cheapest prevention.** In order: (1) the repo owner screenshots Insights > Traffic (on GitHub Free it disappears once the repo is private, VTE X4) and saves a private bundle backup plus the PR JSON (VTE X13); (2) the fork owner deletes the fork; (3) the repo owner makes the repo private; (4) after it is private, by Sun 25 Oct: remove the WInS username from current files (no history rewrite needed while private), the owners of the three link-open Google files set them to restricted (owners UNVERIFIED), and the committer turns on the two GitHub email-privacy settings [fixed 20 Oct, E10]. "Allow forking" cannot be unticked on a personal repo; that step is not needed (VTE X2). Do not rewrite history to remove AI evidence (EXP §0 item 5; CM row 19). Owners: repo owner; fork owner. Deadline: Tue 20 Oct, before M1 if possible.
- **Status vs 16 Oct: Worse.** R16 item 6 was due Sat 17 Oct and is not done. The 20 Oct audit added the network-by-SHA exposure, the client contact blob and the commit-metadata email.

### B. Process and record

#### F3. No recorded votes, roles or reasons; key calls not demonstrably the students' own (L4 × I4 = 16)
- **Mechanism.** Articulation scores the "decision-making process" and "response to challenges" (deliverables.txt:58). With no logged vote, the core idea traced to "our AI council" (ART §1 item 4; ND:62), and "the team deferred" to the AI (CLAUDE.md, Strategy section), a judge (or drill question K9, "how do we know this is yours?") finds no evidence of student decisions. Wharton bans name-only membership ("in name only. That is cheating", GYF:228; CM row 17) and plagiarising ideas (RR:314).
- **Evidence.** "No decision on record has a vote, a list of who was present, or a dissent with an outcome" (ART §1 item 3). There is no record that the Sun 18 Oct meeting happened (TL row 76; DLT). The roles column has been blank since 20 Aug (ART §5). CM rows 15 and 17 are UNKNOWN. The team-written record names few students; each student fills their own row from their own memory (ART §4; a blank is not evidence of no work) [fixed 20 Oct, E21].
- **Hits.** FR Articulation (AR lines); IPS Strategy IS2 and Creativity CP4 (originality, RUB §5b C6-C7); semifinal value statements (NS26:42-43).
- **Irreversible from.** Already, for everything before 20 Oct: it can now only be back-filled as "recalled on <date>". The TNA-freezing D0 choices are due Wed 21 Oct; vote set B Tue 27 Oct; the strategy freezes Sat 7 Nov 09:00 (IPS:73-74).
- **Leading indicator.** No decision-log entry DL-01 to DL-06 within 12 hours of M1 (by Wed 21 Oct 08:30).
- **Cheapest prevention.** M1 tonight at 20:00, 30 minutes (OPS §2): vote the decision rule first (DL-06), then the AI rule (DL-01), roles with a deputy (DL-02), and the picks, authors, paste checker and submit watcher (DL-03, DL-04). The historian logs who argued what and any dissent. Owner: the team leader chairs; historian. Deadline: Tue 20 Oct 20:30; log by Wed 21 Oct 08:30.
- **Status vs 16 Oct: Unchanged.** R16 items 1-5 (Sun 18 Oct) have no record; PM-09.

#### F5. Journal gap: Articulation has no dated, true stories (L4 × I3 = 12)
- **Mechanism.** The Final Report needs true stories of growth and challenge. With the journal silent since before the first trade, the team either has nothing to tell or reconstructs stories from AI files, which risks "invent[ing] teamwork and experiential stories" (RR:313).
- **Evidence.** The journal's last edit was Wed 7 Oct 10:28, 27 minutes before the first order. None of the 14 order events, the mis-click, the 6 Oct email, the "hold" decision, the roster or the AI rules is in it (ART §1 item 1). Several "we discovered" stories were flagged first by AI (ART §1 item 4). Wharton's own feedback told teams to keep "a journal of all your team's activities" in all three years published (PW §5 row 13).
- **Hits.** FR Articulation (all AR lines); semifinal value statements; Creativity CP5.
- **Irreversible from.** It gets worse every week. Back-fill by Sun 25 Oct while the trading night is three weeks old; the FR is due Sat 5 Dec.
- **Leading indicator.** No back-fill entries dated "recalled on" by Sun 25 Oct 17:00 (M4), and no Sunday journal entries after that.
- **Cheapest prevention.** One 30-40 minute back-fill session with all six, using the 13 questions in ART §6, each person in their own words and with "recalled on" dates. Then weekly Sunday entries (ART §7; OPS §3b). Owner: historian; every student. Deadline: before or at M4, Sun 25 Oct 17:00.
- **Status vs 16 Oct: Unchanged** (R16 item 17). The silent stretch has grown from 9 to 13 days.

#### F14. Single points of failure (L2 × I5 = 10)
- **Mechanism.** One person is leader, trader, submitter and Wharton contact, and one account owns the repo and Drive [consistency fix 20 Oct, row 28]. Illness, an exam, a lost login or a lost device near a Saturday-morning deadline means no submission, and there are no extensions.
- **Evidence.** OPS R2 and R4 (H/H); U19 §3a item 3 (single Drive owner); R16 Part 13 (account names on commits never prove who typed, TL:48-52) [consistency fix 20 Oct, row 28]. The deputy is not yet named (R16 item 3 open). Only the leader may submit (GYF:252), and a change needs the advisor's written request (RR:218).
- **Hits.** Any deliverable (gate G1).
- **Irreversible from.** Each submit: Thu 22 Oct, Thu 5 Nov, Wed 2 Dec (internal targets).
- **Leading indicator.** No deputy logged at M1; the leader's SMApply login not tested from a second device by Wed 21 Oct (AW2 check L).
- **Cheapest prevention.** Name the deputy at M1. The leader tests the login from a second device and network by Wed 21 Oct. Send the "if the leader cannot submit" question in batch 1 (VA2 §9 item 4). The Drive owner gives all six edit access, and a copy of each final file goes to a second student. Owner: leader; deputy. Deadline: Wed 21 Oct.
- **Status vs 16 Oct: Unchanged** (R16 item 3).

#### F15. Exam weeks plus AI-material overload starve the students' writing time (L3 × I3 = 9)
- **Mechanism.** Writing time is the scarce input for F1, F3, F5 and F12. HSC exams run to Thu 5 Nov, and whether any member sits them is UNVERIFIED. Meanwhile AI output keeps growing, so the students' reading time goes to AI files instead of writing.
- **Evidence.** HSC dates (VAD §2b): Maths Ext 1 Fri 23 Oct pm; Business Studies Mon 26 Oct am; Economics Tue 27 Oct pm (the vote-set-B day); Legal Studies Mon 2 Nov am; Physics Thu 5 Nov am (the IPS text-lock day). OPS R3 (H/M) and R15 (H/M: about 745,000 words of AI material). On 19 Oct, 30 of 35 commits since 16 Oct were Claude's, and the Research Office added about 10,200 words of AI instructions (U19 §5a). The 20 Oct waves added more than 60 research folders. R16 had asked for "No new waves of AI research until the TNA and IPS are in".
- **Hits.** All three deliverables, indirectly.
- **Irreversible from.** The exam dates above.
- **Leading indicator.** Pre-reads skipped at M1/M2; authors say they "haven't had time to write".
- **Cheapest prevention.** Fill the availability grid at M1, marking the known clashes by name: M4 Sun 25 Oct (Business Studies Mon 26 Oct am), M5 Tue 27 Oct (Economics pm), M7 Sun 1 Nov (Legal Studies Mon 2 Nov am) and the Thu 5 Nov text lock (Physics am); whether any member sits the HSC is UNVERIFIED [fixed 20 Oct, E19]. No student gets more than two tasks in an exam week, and anyone with an exam votes in the chat. The team reads only one synthesis, and the AI produces nothing unasked until 7 Nov. Whoever runs the routines on the leader's machine pauses the scheduled AI routines (`caplet-judge-ips`, `caplet-evidence-lab` and the WInS/SMApply readers; see F23) until the team votes otherwise (DL-01) [fixed 20 Oct, E9]. Owner: deputy; whoever runs the routines. Deadline: Tue 20 Oct (grid; routine pause); standing.
- **Status vs 16 Oct:** exams **unchanged**; overload **worse**.

#### F12. The Final Report is built in the last days, or misses what the semifinal will need (L3 × I5 = 15)
- **Mechanism.** The Final Report is half the Top-50 basis (RR:264) and carries most of Portfolio Analysis, Articulation and the co-sponsor part of Creativity (R16 Part 10). The instructions come only on 9 Nov ET, leaving a 25-day window. If students start drafting on 10 Nov, quality collapses into the final days. Past semifinal rules also disqualified "completely new material" in 4 of 5 years (VPW E2), so anything the semifinal might need has to be in the report already.
- **Evidence.** Last year 30 of 63 dated comments came in the final two days (R16 item 18). There are no student-built modules yet. The SP §4 checklist N1-N15 is mostly "not started" or "needs students' own memories". Past page ranges were a floor as well as a ceiling ("will be disqualified" in 2022-23; "will not be reviewed" in 2023-24; R16 item 21; PW §4.5). Whether WInS stays viewable after the freeze is UNVERIFIED (AW2 Q7). There is a hindsight trap: real January 2027 prices must not become new analysis (SP §1 item 6; Guide:158-159).
- **Hits.** FR, all five criteria.
- **Irreversible from.** WInS records must be saved before and after the freeze (Sat 7 Nov 08:00), or they may be gone. The modules must be pre-built by Mon 9 Nov. Due Sat 5 Dec 09:00.
- **Leading indicator.** On Sun 8 Nov (M10): no saved WInS records, no student-rebuilt numbers card on the 6 Nov close, no section owners.
- **Cheapest prevention.** Not this week, except protecting the evidence: the decision log and the back-fill (F3, F5), and the Trade Log filled from WInS history by Wed 21 Oct (U19 §3a item 7). From 7 Nov: WInS saves, a rebuilt numbers card, module owners (OPS M10), and the release-day drill on Tue 10 Nov. Owner: trade-log keeper; rates analyst; editor. Deadlines: Wed 21 Oct (Trade Log); Sat 7-Sun 8 Nov; Mon 9 Nov.
- **Status vs 16 Oct: Unchanged** (R16 items 17-21; PM-02). New since: the SP N1-N15 checklist and the hindsight trap.

### C. Strategy communication

#### F7. No defensible certainty standard; "her other assets"; coupon gap undecided (L3 × I4 = 12)
- **Mechanism.** The case requires the team to "define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions" (case:96-99), with no outside money (case:91-92). If the IPS freezes a mechanism with no stated level, leans on money outside the portfolio, or quotes a number that does not hold on the plan as written, judges see the core claim fail.
- **Evidence.** The accepted V5 reads "any reinvestment shortfall is covered by her other assets, with the floor used last" (VAD C2; ambiguous, it may mean VT, VIF). V5 gives a mechanism, not a level (IFX #4). Under option 1 (state the risk only), about 1 path in 7 leaves a payment short, typically about $1.5k and at worst about $10k, and those gaps fall on money Laura has already taken out (REC §7). The "0.02%" headline for 3r is not defensible. The honest 3r range on the plan as written is about 0.01-0.6% of paths short, never more than about $3.3k, and only if two rules are written down (sizing to maturity; the 2033 reserve keeps the dollar shortfall plus $5k); otherwise 2-6% (REC §0, §5, §7). [fixed 20 Oct, E1] Both figures assume Laura's retained half is released in 2033. V5 (accepted and pending) funds uncovered payments from her retained equity. If that half stays on call to 2042, option 1 is about 1.4% short and 3r about 0.07% (REC banner 2). Decide this reading first on Tue 27 Oct. The fix list contradicts itself on whether any percentage may appear in the IPS (VIF medium problem 1).
- **Hits.** IPS and FR; Strategy IS4, Client CK6, Analysis PA4 (RUB §5e: these fixes are worth about +0.8 Strategy and +0.4 Analysis, VRA corrected, AI opinion) [fixed 20 Oct, E6].
- **Irreversible from.** Vote set B on Tue 27 Oct. Any option that needs a trade (3r option B, option 4) must fill by the Wed 4 Nov close (Thu 5 Nov 08:00 Sydney); TC/VTR plan the sale for Thu 29 Oct 22:00 and the bond for Fri 30 Oct 22:00. IPS Sat 7 Nov 09:00.
- **Leading indicator.** No students' half-page options notes posted by Mon 26 Oct 18:00 (OPS M5 pre-read); "other assets" or "other holdings" still in any draft.
- **Cheapest prevention.** Ban "her other assets/holdings" in every draft now. Put "is Laura's retained half on call after 2033?" on the 27 Oct agenda before D1 [fixed 20 Oct, E1]. The rates analyst and the growth/risk analyst write options notes for D1 (coupon cover), D3 (certainty standard) and D5 (shortfall order inside the portfolio to 2042). They decide whether any percentage goes in the IPS, and quote certainty only with its conditions (REC §7). Owners: rates analyst; growth/risk analyst; whole team votes. Deadlines: notes Mon 26 Oct 18:00; vote Tue 27 Oct.
- **Status vs 16 Oct: analysis improved** (five options compared, then red-teamed and reconciled), **decision unchanged** (R16 item 11). The "her other assets" wording is **new** (it arrived with v11 on 17 Oct).

#### F9. The 2031 range odds are misstated, or the top rule is left undefined (L3 × I3 = 9)
- **Mechanism.** The case warns against overpromising (case:114), and Creativity now scores communicating "investment uncertainty clearly and credibly to prospective co-sponsors" (deliverables.txt:59). If 3r is adopted but the top keeps counting the reserve, the live claim that the gift reaches the top "in about three of four paths" becomes false.
- **Evidence.** On the agreed basis the gift reaches the top in about three in four paths under option 1 (72-77%), under half under 3r as written (40-45%), and about three in four under 3r with the top fix (72.5-76%); the exact figures depend on two unstated conventions, the $1k rounding of the top and 17 days of floor interest missing from the 2031 projection (REC §5; REC banner 1) [fixed 20 Oct, E2]. CR finds 75% vs 49% on the study engine (CR §0 item 2); LCK's validation run gives 68.4% (option 1) and 73.0% (3r with the fix) (LCK §0). If the top excludes the reserve, the figure is 79% (CR 3a_10k) to 92% (LCK Verdict item 5; §8), by engine [fixed 20 Oct, E2, E16]. Different engines give different figures, so one owner must pick one.
- **Hits.** FR Portfolio Analysis and co-sponsor excerpt; Client (overpromising); IPS if the top rule is stated.
- **Irreversible from.** Vote Tue 27 Oct (decide the top rule together with D1); IPS Sat 7 Nov; FR Sat 5 Dec.
- **Leading indicator.** The D1 vote record names an option but no top rule; any draft carries a reach-the-top percentage with no engine or basis.
- **Cheapest prevention.** Put "how the top is set" on the Tue 27 Oct agenda next to D1 (LCK §8). Keep odds out of the IPS (IFX #6, #11). The rates analyst owns the single FR figure. Owner: rates analyst; growth/risk analyst. Deadline: Tue 27 Oct.
- **Status vs 16 Oct: New.**

#### F11. Numbers and bases are inconsistent (L4 × I3 = 12)
- **Mechanism.** "One claim, one figure, in all three documents" (R16 Part 14). A judge who sees two values for the same quantity, or a WInS figure presented as Laura's, marks down Analysis and trusts the rest less. At a semifinal only Final Report numbers may be used, and every student must explain them (U19 §3c item 5).
- **Evidence.** The ladder cost varies by basis and date: 19 Oct basis D $297,162 with 41% odds above $300k (CR §1); the agreed maturity-sizing basis about $300.4k with the 0.07% iBond fee counted ($299.9k without it), so a Jan-2028 top-up is slightly more likely than not on that basis, and option 1's median minimum is on the $140k/$145k edge (REC §5 and banner 3; REC says to stop quoting "$293k" and "her first $300,000 is enough") [fixed 20 Oct, E3]. The scale factor appears as 0.643, 0.644, 0.645 and 0.667; 0.667 is not valid (NRG H5; VTR E4). VT is about 7% of Laura's money but about 9% of the WInS book (NRG H4). V5 carries an undated "about 5.15%" (IFX #12). competition/COMPETITION.md still says the Feb-2037 bond pays 5.000%; it is 4.750% (CM row 30). On the reach-the-top odds, see F9.
- **Hits.** TNA (if a level is quoted), IPS, FR; Analysis PA3; Creativity CP3.
- **Irreversible from.** TNA submit (Thu 22 Oct) for any figure in a reflection; IPS Sat 7 Nov; FR.
- **Leading indicator.** A draft figure with no date or basis beside it; two students quote different values for the same thing.
- **Cheapest prevention.** The TNA and IPS quote no ladder dollar level; state the rule instead (CM row 66; U19 §3a item 8). The rates analyst keeps one student-built numbers card (date, basis and type for each figure) and fixes the scale at about 0.644 (0.643-0.645 by basis; never 0.667) (NRG H5; VTR E4) [fixed 20 Oct, E17]. Owner: rates analyst; paste and numbers checker. Deadlines: Wed 21 Oct (the IBTR number rule at M2); card rebuilt on the 6 Nov close.
- **Status vs 16 Oct: Worse.** More competing figures now exist (R16 Part 12 listed 22 contradictions; since then there are three 3r payment figures, four reach-the-top figures and four scale factors).

#### F4. TNA, IPS and filed notes contradict each other, or state false facts (L4 × I3 = 12)
- **Mechanism.** "Evaluators will consider the three deliverables together" (case:161-162). The notes are frozen; the reflections freeze at TNA submission; the IPS must agree with both. False facts copied from the AI text become permanent.
- **Evidence.** The four TNA-freezing choices are undecided: VT's job, the floor and its rounding, why 2042 first, and "sized for" vs the top-up rule (U19 §7a; CM row 21). The VT note says stocks "only" set how far her gift rises, while the accepted IPS gives the equity two jobs (U19 §4a). False statements in the AI text: "first warned of a 0.3-point fall" (the executed note says "about 0.2"); "from 2042 backwards" (true only of the first entry pass); "Maturing bonds, not sales, supply every payment" (false for 2038 and 2039); "announce in 2031" (the contribution comes in 2033); an invented VT industry reason (U19 §4a; CM row 4). RUB caps IS6 in the TNA at 3 because of the VT "only" (RUB §5b C1). [fixed 20 Oct, E12] Each reflection must also cover the three TNA:46-52 elements (why the team made the decision; how it aligned with the overall strategy; how it supported the client's goals, funding needs or risk considerations) in "100 words or fewer"; the Doc prompt says "goals, objectives, or constraints", not TNA:52's wording (U19 §3a item 9), and none of the 11 notes mentions flexibility, liquidity or the residency, so the reflections must carry the client link (R16 item 8). [fixed 20 Oct, E13] Calling IBTM "refined" by the 6 Oct email depends on when that email arrived relative to the IBTM order (10/06 10:01:41 PM ET = Wed 7 Oct 13:01 Sydney); the arrival time is recorded nowhere (U19 §3a item 6a).
- **Hits.** TNA and IPS; Strategy IS6 ("maintains consistency with the team's IPS", deliverables.txt:55).
- **Irreversible from.** TNA submit (Thu 22 Oct); IPS Sat 7 Nov.
- **Leading indicator.** The D0 mini-vote is not logged before finals are written (Wed 21 Oct 20:00 at M2).
- **Cheapest prevention.** Hold the D0 mini-vote at M2 on Wed 21 Oct (OPS DL-07 to DL-14). Tell a story (such as "0.3 to 0.2") only if a student remembers it and it is logged. Use the "refined by the 6 Oct email" story only if the email's arrival time is found and is before the IBTM order (U19 §3a item 6a) [fixed 20 Oct, E13]. At M3 a non-author checks each reflection against the three TNA:46-52 elements and ≤100 words (strict counter), and the Doc prompt is corrected to TNA:52's words [fixed 20 Oct, E12]. On Sat 24 Oct the editor lists every submitted TNA claim as a constraint on the IPS. Owners: whole team; authors; a non-author checker; editor. Deadlines: Wed 21 Oct; Thu 22 Oct 19:00 (M3 element check); Sat 24 Oct.
- **Status vs 16 Oct: Unchanged** (R16 items 4 and 8; PM-05, PM-06).

#### F10. Client knowledge stays thin (L3 × I3 = 9)
- **Mechanism.** Client Knowledge is one of the weak criteria (U19 §2). If students rewrite from V5's ideas, they inherit its gaps.
- **Evidence.** The accepted text uses "flexibility", "responsible" and "liquidity" 0 times (VIF theme counts; the case uses "flexibility" 5 times). Willingness to take risk was cut, and only "capacity for risk is high" remains (IFX #7, #9). The kept money doubles as the payment backstop and is $0 at the 5th percentile under option 1 (CR §0 item 3). Currency is the largest unsized risk: a fixed US$ amount moved between −15% and +17% in NT$ terms over two-year windows since 2000 (U19 §8). The two co-sponsor readers would ask "how much, in what currency, when, paid to whom, how firm, and what is not covered" (CR §0 item 4). RUB's best realistic IPS still has Client at only 7.1 (AI opinion).
- **Hits.** IPS and FR; Client CK2-CK5; Creativity CP6.
- **Irreversible from.** IPS Sat 7 Nov.
- **Leading indicator.** No D6 ("responsible" and "appropriate flexibility") options note by Mon 26 Oct.
- **Cheapest prevention.** The client/co-sponsor lead writes the D6 options note, split by goal: willingness vs capacity, the kept money's job, home and bad-case size, and who bears currency risk (D8). Owner: client/co-sponsor lead. Deadline: Mon 26 Oct 18:00.
- **Status vs 16 Oct: Unchanged** (R16 Part 6).

#### F13. Competent but not memorable (L3 × I4 = 12)
- **Mechanism.** Only about 2% get through. A correct liability-matching answer is an "expected kind of answer" (RUB §5b C5, citing a 2021-22 fixed-payment case), and the core idea came from an AI council run (C6). Without one visibly team-own resolution, the entry sits in "contention, not a safe place" (RUB §5d). Score note: I4 is by judgement. Being not memorable does not by itself pull a criterion below competent (I3 on the scale above), but with about 2% selected a competent-only entry misses, and the I scale understates that [fixed 20 Oct, E15].
- **Evidence.** The best realistic student IPS scores about 7.3/10 (range 6.5-8.6) and reaches level 4 on no phrase at its middle estimate (RUB §0 item 3, §6; AI opinion). The live text scores 4.4-4.7 corrected (RUB banner). The most repeated official message is "say less, plainly, and show why" (PW §5). The 19 Oct review called the "range built to hold" mechanism the most original idea on any branch (U19 §5b; RUB §6 gap 3).
- **Hits.** IPS and FR; Strategy IS2; Creativity CP1 and CP4.
- **Irreversible from.** IPS Sat 7 Nov: after that the strategy is frozen and the semifinal bans new material.
- **Leading indicator.** The vote-set-B log names no choice the students argued for in their own words; the pitch drafts restate "ladder + floor + growth".
- **Cheapest prevention.** At M5 the students pick, argue and log the one resolution they will own (for example how the 2031 range holds, with a downward-only re-quote rule, D8), and credit its AI origin honestly. No new AI idea is added. Owner: whole team; every student drafts a pitch alone (OPS M4/M7). Deadline: Tue 27 Oct; pitch vote Sun 1 Nov.
- **Status vs 16 Oct: Unchanged** (PM-07).

### D. Hard gates and submission mechanics

#### F17. The IPS PDF fails the format gate (L2 × I5 = 10)
- **Mechanism.** "Submissions that do not meet the requirements below will not be considered for semifinal selection" (IPS:82-83). Pending suggestions print, headings push the pitch over 50 words, blank lines push the strategy onto a third page, or the title-page names don't match the roster.
- **Evidence.** A whole-document export prints both wordings: about 77 + 939 words over 4 strategy pages. Whether a single-tab export also prints suggestions is UNVERIFIED but likely (VAD C1). Counting the heading, the pending pitch is 51 words (VA2 §0). The page still shows "[AI]", the tab title and the meta-line "Name the residual risks." (RUB §4a). The roster wording is not in the repo, by design (CM row 35). The two-page fit of any draft is UNVERIFIED until exported (IFX T4).
- **Hits.** IPS; gate G2.
- **Irreversible from.** Sat 7 Nov 09:00 (internal Thu 5 Nov 20:00).
- **Leading indicator.** No exported single-tab PDF opened on a second device by Tue 3 Nov 18:00.
- **Cheapest prevention.** Reject the pending suggestions today (F2). On Tue 3 Nov the rules lead and one other student run the IFX §4 15-item checklist on the exported PDF: strict word count with headings, 2 pages, no colour, roster names, 5 MB or smaller. Owner: rules and format lead + one student. Deadline: Tue 3 Nov.
- **Status vs 16 Oct: Worse.** The doubled text has existed since 18 Oct (R16 item 14).

#### F18. Submission mechanics fail (L3 × I5 = 15) [fixed 20 Oct, E5, E14]
- **Mechanism.** Unknown form fields, a form that locks, a wrong file or an unreachable leader on a Saturday-morning ET deadline. The SMApply buttons can also fail in two directions (RBC §0 item 2): (a) a Submit pressed too early locks the TNA text, and it could lock the IPS and Final Report tasks only if they are optional tasks in the same stage; (b) the bigger risk is the reverse: a Submit that is the TNA's real delivery is never pressed, or "Mark as Complete" is pressed and nobody confirms receipt, so the TNA is never delivered [fixed 20 Oct, E5, overridden by the runbook check].
- **Evidence.** The form's fields and lock behaviour are UNVERIFIED (CM row 16; AW2 check C; OPS R7 "Form not seen by Tue 20" is the early warning). On SurveyMonkey Apply, "Mark as Complete" is not the same as submitting (R16 item 7; SMA:233 vs SMA:208-210). [fixed 20 Oct, E5] Submit only works once "you ... complete all required tasks within your application" (SMA:205); "It's not possible to delete an application after you submit" (SMA:191); and a new stage's default automation is "On submit -> Move to stage", after which "the applicants will no longer be able to make edits" (RBC §0 item 2, from SMApply's help on application stages). So one Submit on 22 Oct is unlikely to lock the IPS and Final Report: if they are required tasks in the same stage, Submit stays blocked; if they sit in later stages, Submit is the TNA's delivery. The roster was already "submitted (locked)", which fits a staged set-up (UNVERIFIED; RBC §3.5 item 7). Both the 16 Oct and 19 Oct reviews asked for the form to be opened (R16 item 7; U19 §3a item 6b); neither has a record, so L is 3, not 2.
- **Hits.** TNA first, then IPS and FR (gate G1).
- **Irreversible from.** Thu 22 Oct 20:00 (TNA internal submit).
- **Leading indicator.** No screenshots of the TNA form on the private Drive by Tue 20 Oct 23:59, including each task's status (TNA, IPS, Final Report) and whether Review & Submit is shown and active [fixed 20 Oct, E5].
- **Cheapest prevention.** The leader opens the TNA form without submitting, with the rules lead watching, and screenshots every field and button (AW2 check C). [fixed 20 Oct, E5, overridden by the runbook check] The screenshots include each task's status and whether Review & Submit is shown and active, and the leader writes down which buttons the roster submit took and what My Applications shows now (RBC §3.5 items 1-7). On Thu 22 Oct the leader presses only the button the three-case rule in RBC §3.5 picks: **Case 1** (the TNA is the only open task and Review & Submit is active): Submit, because that Submit is the TNA's delivery; **Case 2** (Review & Submit absent or blocked): Mark as Complete, check that the TNA status changes to complete, and use Contact Us in the same session to confirm receipt; **Case 3** (IPS/FR tasks open and editable **and** Review & Submit active): Mark as Complete only, ask Wharton (VA2 batch-1 item 5) and vote at M3 (DL-15). If the form's own wording says how the TNA is submitted, follow the form. Submit 36 hours early, on screen-share, with the deputy watching, and screenshot the confirmation (OPS M3). Owner: leader; rules lead; deputy. Deadline: Tue 20 Oct (form check); Thu 22 Oct 20:00 (submit).
- **Status vs 16 Oct: Unchanged** (R16 items 7 and 10); the score rises from L2 × I5 = 10 to L3 × I5 = 15 [fixed 20 Oct, E5].

#### F16. A note is pasted wrongly in the TNA (L2 × I4 = 8)
- **Mechanism.** "Include each Trading Note exactly as it appears in WInS ... Yes, we will verify this" (TNA:44, :53). The wrong order's note, curly quotes from a Google Doc, or a length-only check would fail it.
- **Evidence.** The cancelled IBTR note says "0.3"; the filled one says "about 0.2". The lengths collide: 288 characters for VT, the cancelled IBTR and the filled Nov-2041; 294 for both the filled IBTR and IBTO (AW2 check K, citing VK2 error #1).
- **Hits.** TNA (gate G3).
- **Irreversible from.** Thu 22 Oct 20:00.
- **Leading indicator.** The paste checker signs off on length alone, or no `textcheck.py --compare` "exact match: YES" is recorded for each note.
- **Cheapest prevention.** Copy each note as plain text from the WInS Trade Notes page. Check the ticker, the order time (IBTR 04:42:53 AM ET) and "about 0.2", not just the length. Run `textcheck.py --compare` until it reports an exact match. Owner: paste checker (not the submitter or an author); leader. Deadline: Thu 22 Oct 19:00.
- **Status vs 16 Oct: Unchanged.** More length collisions were found on 20 Oct.

#### F19. The school documentation letter is missing or wrong (L2 × I4 = 8)
- **Mechanism.** It is one of the "four REQUIRED Deliverables" (CM row 28). It needs letterhead, an administrator's signature, the advisor's full name and every student's name (SDT:1-28). Knox Term 4 ends Thu 3 Dec. Fri 4 Dec is a staff PD day, and whether anyone will sign on that day is UNVERIFIED (VAD P1).
- **Evidence.** It was "Not yet requested as of 13 Oct" (`competition/COMPETITION.md:132`), and there is no later record (CM row 28). The 16 Oct deadline for the request was Fri 23 Oct (R16 item 10b).
- **Hits.** FR submission (eligibility).
- **Irreversible from.** Thu 3 Dec (the last student day). In practice, by Fri 27 Nov (OPS R12).
- **Leading indicator.** No request is logged by Fri 23 Oct, or no reply by Fri 6 Nov.
- **Cheapest prevention.** One email to the school office or advisor. Owner: advisor and school liaison. Deadline: Fri 23 Oct; signed by Fri 27 Nov. Never commit the letter to the repo.
- **Status vs 16 Oct: Unchanged.**

#### F22. The text names a non-permitted or unlisted security (L2 × I3 = 6)
- **Mechanism.** The permitted list now governs "BOTH contributions, the IPS and Final Report", and TIPS and STRIPS are listed as "NOT permitted" (CM Δ1, Δ3; SMF:44, :54-55). The plan parks 2038/2039 proceeds in "a short-term Treasury ETF" that must be WInS-listed. Stale STRIPS-era files invite a "STRIPS basis" number or a TIPS "option".
- **Evidence.** SGOV was seen on WInS on 29 Sep but never screenshotted, and BIL and SHV were not checked (AW2 check H). 66 repo files carry STRIPS-era text without a banner (CM row 23). In 2023-24, prohibited holdings were excluded (UNVERIFIED for this year, CM row 22). All 11 WInS holdings comply (CM rows 22, 23, 30).
- **Hits.** IPS and FR (gate G4).
- **Irreversible from.** IPS Sat 7 Nov; FR Sat 5 Dec.
- **Leading indicator.** A draft names a fund with no dated WInS search screenshot.
- **Cheapest prevention.** Screenshot a WInS search for every security the IPS or FR names (AW2 check H). Discuss TIPS only as excluded by the rules, and never value anything on a "STRIPS basis". Owner: rules lead; rates analyst. Deadline: Thu 5 Nov.
- **Status vs 16 Oct: Partly new** [fixed 20 Oct, E7]. The TIPS/STRIPS ban (CM Δ3, 16 Oct 02:46 → 19 Oct 13:04 UTC) is new; "for BOTH contributions" (CM Δ1, 14 → 16 Oct) and the screenshot list were already in R16 (Part 2 item 4; item 18).

#### F21. A late strategy reopen, or a trade-execution error near the freeze (L2 × I3 = 6)
- **Mechanism.** A floor-size re-vote pushed by an AI memo or a second-hand "former judge" view, made after the TNA, contradicts the IBTM and VT notes (D9b). Or a two-order trade (3r option B) is done in a rush around the FOMC and the US clock change: the bond is bought before the sale fills, or is priced off a stale WInS bond price.
- **Evidence.** Office WO-0002 pushes a floor re-vote 18 days before the freeze (CM row 31; U19 §5a). The plan sizes the IBTM sale at 295 shares, but 231 keeps the plan's IBTM gap (VTR E1). WInS bond prices update once a day at the US open, so a pre-open check on Thu 29 Oct shows a price set before the FOMC (VTR E8). An under-funded buy may be shrunk or "System Cancelled" (VTR E9). Timing: sale Thu 29 Oct 22:00, bond Fri 30 Oct 22:00; fallback sale Mon 2 or Tue 3 Nov, bond the next evening; nothing after Wed 4 Nov 22:00 (VTR banner).
- **Hits.** IPS (strategy frozen after Sat 7 Nov); TNA consistency; Articulation if mishandled.
- **Irreversible from.** Team cutoff Thu 5 Nov 08:00 Sydney (Wed 4 Nov close) for any order, so that the IPS submitted Thu 5 Nov describes a filled book; WInS itself freezes about Sat 7 Nov 08:00 [fixed 20 Oct, E18].
- **Leading indicator.** A new idea raised after Tue 27 Oct; a voted trade with no size or no DL-ID.
- **Cheapest prevention.** Decide at M4 (Sun 25 Oct) whether D9 is on the agenda at all. If a trade is voted, the vote fixes its size (295 or 231) and the VTR §5 go/no-go card is used. No order without a logged vote. Only the trader enters orders, and the trade-log keeper checks each preview. Owner: leader; trader; trade-log keeper. Deadlines: Sun 25 Oct; Thu 29-Fri 30 Oct.
- **Status vs 16 Oct: Unchanged** (R16 item 11.8, Part 16). The WO-0002 push is new detail.

#### F23. Eligibility edge cases (L1 × I5 = 5)
- **Mechanism.** Three low-likelihood ways an entry could be ruled ineligible:
  - an undefined "required trading activity" that an 11-trade hold portfolio fails;
  - an outside reader who turns out to be paid (paid advisors mean disqualification);
  - AI operating WInS or SMApply.
- **Evidence.**
  - "Teams must meet the required trading activity and portfolio management guidelines" (RR:260) has no public definition. The legacy page says "We do expect you to do some trading once you have built your portfolio" (TOU:228). The Week-One email is still unread ("opens as a download, not read here", wins_notes.csv:19).
  - A "former Wharton judge" was shown V5; who, and whether paid, is UNVERIFIED (CM row 26; RR:248).
  - On 7 Oct an AI browser click cancelled the wrong order. competition/COMPETITION.md:193 still says "AI may fill a ticket up to Preview", and there is no deny list (CM row 32). Stock-Trak's terms bar robots (VA2, STT:200).
  - [fixed 20 Oct, E9] The scheduled routines on the leader's machine may read a logged-in WInS session ("you may READ the portfolio and order pages", `keel/routines/tasks/MONITOR.md:23`) and logged-in SMApply ("only if a session is already logged in", `WATCHER.md:12`). Scheduled tasks exist for `caplet-judge-ips` (about 1 Nov), `caplet-evidence-lab` (AI-built Final Report evidence each run) and `caplet-wharton-monitor` (a twice-weekly WInS portfolio read) (`keel/routines/tasks/scheduled_tasks/*.md`). U19 §3b item 9 asked to pause them, and TL row 63 lists mock-judge panels on 19 Oct, 1 Nov, 22 and 30 Nov. Whether they still run is UNVERIFIED (U19 §11b).
- **Hits.** Eligibility; conduct.
- **Irreversible from.** Freeze about Sat 7 Nov 08:00 (activity); each submission (reader); any AI session near WInS.
- **Leading indicator.** The Week-One email is still unread on Wed 21 Oct; there is no written note that the reader is unpaid.
- **Cheapest prevention.**
  - The rules lead reads the Week-One email and the logged-in Trading Details today (AW2 checks A-B).
  - The leader sends batch-1 item 3. Never trade just to reach a count.
  - The leader records in the team log that any outside reader is unpaid and gives scores and questions only (by Fri 23 Oct).
  - Delete competition/COMPETITION.md:193 and add deny rules, so that no AI goes near WInS or SMApply.
  - Whoever runs the routines on the leader's machine pauses `caplet-wharton-monitor` (WInS read), `caplet-rules-watcher` (logged-in SMApply), `caplet-judge-ips` and `caplet-evidence-lab` until the team votes otherwise (DL-01), and logs that they were paused or had already stopped (Tue 20 Oct) [fixed 20 Oct, E9].
  - Owners: rules lead; leader; whoever runs Claude Code. Deadlines: Tue 20 to Fri 23 Oct.
- **Status vs 16 Oct: Unchanged** (R16 items 6.4 and 7). The paid-reader angle is new (CM row 26).

### E. Competition structure (mitigate; cannot be prevented)

#### S. Base rate and rules of the game
- **Facts.**
  - In 2025-26, 49 of 2,339 submitting teams reached the semifinal, about 2% (SP intro).
  - Selection is "based on the strength of their Investment Policy Statement (IPS) and Final Reports" (RR:264), while all three deliverables "are evaluated" (deliverables.txt; CM row 70). The TNA's weight is UNVERIFIED, so treat it as scored.
  - "Teams will not receive individual feedback" (SMF:81-82), so there is no signal between the IPS and the Final Report.
  - "We will not grant any deadline extensions" (deliverables.txt:29).
  - The Final Report instructions come on 9 Nov ET, which can be Mon 9 Nov 16:00 Sydney or later (VAD P6).
  - Past page ranges were enforced at both ends (PW §4.5).
  - Non-US teams make up 40-51% of each Top 50, but no Australian team has made one since 2021-22 (RUB §6).
- **What it means.** A good entry can still miss. The only levers are: no gate failures (F17, F18, F16, F19), no conduct risk (F1, F2, F8, F20, F23), two documents that score well on all five criteria ("score exceptionally well on all five components", FAQ:83, RUB §0), and a Final Report built before 9 Nov.
- **Leading indicator.** Any deadline met with less than 24 hours to spare.
- **Mitigation.** Submit 36-48 hours early (Thu 22 Oct; Thu 5 Nov; Wed 2 Dec). Run the release-day drill on Tue 10 Nov and check the page count against the real range on 10 Nov and 29 Nov (R16 item 21).

---

## 3. Status against the 16 Oct list (R16 Part 1 items and Part 15)

| R16 item / PM | Due (Sydney) | Record that it was done? | Failure mode here | Status |
|---|---|---|---|---|
| 1 AI-rule vote | Sun 18 Oct | None (TL row 76) | F1, F3 | Unchanged; three AI rules still in force on different branches (U19 §3a item 1) |
| 2 Picks and authors | Sun 18 Oct | Picks entered in the Sheet on 17 Oct by an unrecorded author; no authors, no vote (U19 §2) | F1, F3 | Unchanged |
| 3 Deputy and roles | Sun 18 Oct | None | F14 | Unchanged |
| 4 Ladder basis and owner | Sun 18 Oct | None | F11 | Worse (more figures) |
| 5 Book the Tue 27 Oct meeting | Sun 18 Oct | None in the team record; OPS proposes M5 | F7 | Unchanged |
| 6 Repo and fork private; file fixes | Sat 17 Oct | None; both still public (VTE) | F8, F22, F23 | Worse (new exposure found) |
| 7 Week-One email; open the TNA form | Sat 17 Oct | None (wins_notes.csv:19) | F18, F23 | Unchanged |
| 8 Students write reflections | Mon 19-Wed 21 Oct | No student words (DLT §2) | F1 | Worse (AI text added 17-18 Oct) |
| 9 Decision log | Sun 18 Oct | None (ART §5) | F3 | Unchanged |
| 10 Exact-paste submit | Thu 22 Oct | Not due yet | F16 | Unchanged |
| 10b School letter | Fri 23 Oct | None after 13 Oct | F19 | Unchanged |
| 11 Vote set B | Tue 27 Oct | Not due yet; analysis improved (REC, LCK, TC) | F7, F9, F21 | Improved analysis |
| 12-14 Fresh IPS; [AI] list; format gate | 28 Oct-5 Nov | Not due; the doubled text has made the gate worse | F1, F17 | Worse |
| 16 AI-log back-fill | Sun 25 Oct | Not due; the gap has grown | F6 | Worse |
| 17 Journal back-fill | Sun 25 Oct | Not due; silence now 13 days | F5 | Unchanged |
| 18-21 FR modules, banners, co-sponsor, page range | 9 Nov onwards | Not due | F12 | Unchanged |
| 22-25 Defend without a laptop, humans score first, CFA Code, finale | Ongoing | No record | F3, F13 | Unchanged |
| PM-02 FR late; PM-03 AI voice; PM-04 rules protect the range more than the payments; PM-05/06 inconsistency; PM-07 not memorable; PM-09 calls not the students'; PM-12 gate fails | - | - | F12; F1/F2; F7; F4/F11; F13; F3; F16-F19 | PM-03 and PM-12 worse; PM-04 improved analysis (3r reconciled); the rest unchanged |

New since 16 Oct: F9 (odds and the top rule), F20 (13-word note clauses), F22 (the TIPS/STRIPS ban) [fixed 20 Oct, E7], the paid-reader angle in F23, and "her other assets" in F7.

---

## 4. Leading indicators to check daily this week (two minutes; any student)

| Check | Green | Red | Mode |
|---|---|---|---|
| A student draft exists with its own revision history | By Tue 20 night | None by Wed 21 Oct 18:00 | F1 |
| IPS Report Doc: pending suggestions | Rejected, and AI text moved to "AI reference" | Still pending, or "[AI]" gone with the text unchanged | F2, F17 |
| Decision log | DL-01 to DL-06 logged by Wed 21 Oct 08:30 | No entries | F3 |
| Repo and fork visibility (GitHub API, `private` field) | true | false | F8 |
| TNA form screenshots on the private Drive, including each task's status and whether Review & Submit is shown and active [fixed 20 Oct, E5] | By Tue 20 Oct | None, or no task-status screenshot | F18 |
| D0 mini-vote logged | Wed 21 Oct 20:30 | Finals written before it | F4 |
| TNA AI-use rows, including the VT clause | By Thu 22 Oct 16:00 | Missing at M3 | F6, F20 |
| Paste check "exact match: YES" × 3, with ticker and time | Thu 22 Oct 19:00 | Length-only check | F16 |
| School letter request logged | By Fri 23 Oct | None | F19 |
| Back-fill entries with "recalled on" dates | By Sun 25 Oct 17:00 | None | F5 |

---

## 5. Top 10 actions this week (Tue 20 to Sun 25 Oct)

[fixed 20 Oct: table replaced by VPM2 §7's corrected table (E9-E13, E19, E20, E23), with actions 5 and 8 changed to the three-case SMApply rule of RBC §3.5 instead of VPM2 E5's rule.] Changes from the original are in **bold**. Owners are roles. No cell is deliverable wording.

| # | Action | Owner (role) | Deadline (Sydney) | Prevents | Done when |
|---|---|---|---|---|---|
| 1 | Hold M1 (30 min). **Name a recorder at minute 0.** Vote the decision rule (DL-06), then the AI rule (DL-01). **The AI rule also covers the scheduled AI routines and any detector or humanise pass.** Assign roles with a deputy (**deputy ≠ historian; paste checker ≠ submitter or author**). Confirm the picks, the three authors, the paste checker and the submit watcher. Fill the availability grid, **marking any HSC clash (Fri 23, Mon 26, Tue 27 Oct; Mon 2, Thu 5 Nov)**. [fixed 20 Oct, E9, E19, E20] | Leader chairs; **recorder, then historian** | Tue 20 Oct 20:00-20:30; log by Wed 21 Oct 08:30 | F3, F14, F15, F1, F2 | DL-01 to DL-06 written, with who argued what and any dissent |
| 2 | Reject the 10 pending suggestions by hand in Suggesting view. Move the accepted V5 and the three [AI] reflections to a tab labelled "AI reference", or remove them from the live text. **Never "Delete version history" and never "Make a copy" to get a clean Doc.** Never strip only the tag. [fixed 20 Oct, E11] | Editor, with the deputy watching | Tue 20 Oct 22:00 | F2, F17, F1 | No green text; the AI text sits under its label; **version history is intact** |
| 3 | Write the three reflections fresh, from your own notes, with every AI file closed. **A non-author checks each one against the three TNA:46-52 elements and ≤100 words (strict counter). Use the "refined by the 6 Oct email" story only if its arrival time is found and is before the IBTM order.** Two non-authors score before any AI check. [fixed 20 Oct, E12, E13] | Three authors; two scorers | Drafts Tue 20 Oct night; finals Wed 21 Oct 22:00 | F1, F4 | Each author can explain every sentence aloud; scores **and element checks** are recorded |
| 4 | **Lock down.** (a) Screenshot Traffic; save a private bundle and the PR/comments JSON. (b) The fork owner deletes the fork. (c) The repo owner makes the repo private; no history rewrite of AI evidence. **(d) Pause the scheduled routines that read WInS or logged-in SMApply, or that generate AI judging or evidence (`caplet-wharton-monitor`, `caplet-rules-watcher`, `caplet-judge-ips`, `caplet-evidence-lab`), and add deny rules (WInS, SMApply, Drive/Docs writes, Gmail, browser); delete `competition/COMPETITION.md:193`. (e) After going private: remove the WInS username from current files; turn on the GitHub email-privacy settings; ask the owners of the three link-open Google files to restrict them.** [fixed 20 Oct, E9, E10] | Repo owner; fork owner; **whoever runs the routines / Claude Code** | Tue 20 Oct (a-d); **Sun 25 Oct (e)** | F8, F23, F15 | The API shows both repos private or gone; **the routine pause is logged; the username grep of the current files is clean** |
| 5 | Open the SMApply TNA form without submitting and screenshot every field and button. **Record each task's status (TNA, IPS, Final Report), whether Review & Submit is shown and active, which buttons the roster submit took and what My Applications shows now (RBC §3.5 items 1-7).** Read the Week-One email and the logged-in Trading Details. Test the leader's login on a second device. **Send Wharton batch 1 (VA2 §9 items 1-5, reworded by a student, advisor copied).** [fixed 20 Oct, E5 as overridden by RBC; E23] | Leader + rules lead | Tue 20 Oct (form, email, **batch 1 by 22:00**); Wed 21 Oct (login) | F18, F23, F14, F6 | Screenshots **(fields, buttons, task statuses, Review & Submit state)** and the email's words on the private Drive; **the batch-1 text and send time logged** |
| 6 | Hold the D0 mini-vote (VT's job; floor rule; reason for 2042 first; "sized for"). Set the IBTR rule (quote no dollar level). Ban "her other assets/holdings". **Put on the 27 Oct agenda: is Laura's retained half on call after 2033 (REC banner 2), and how the top is set.** [fixed 20 Oct, E1] | Whole team; rates analyst | M2, Wed 21 Oct 20:00 | F4, F11, F7, F9 | DL-07 to DL-14 logged before finals; **the 27 Oct agenda posted** |
| 7 | Log the TNA's AI use: exemplars v1-v12, the [AI] Doc text, the 13-word clauses in the VT and Nov-2040 notes, the ticket tool, the 7 Oct browser click, **the scheduled routines**, and these reviews. Decide the disclosure line (default: a plain factual line if the form has space, VA2 §0). [fixed 20 Oct, E9] | Historian; whole team decides | Thu 22 Oct 16:00 | F6, F20 | DL-16 logged; the disclosure decision is recorded |
| 8 | Paste-check and submit the TNA. Plain-text copy from WInS; `textcheck.py --compare` exact match; check ticker, time and "about 0.2"; count words twice. **Read the task statuses and the Review & Submit state first, then press only the button the three-case rule in RBC §3.5 picks. Case 1 (the TNA is the only open task and Review & Submit is active): Submit, because that Submit is the TNA's delivery. Case 2 (Review & Submit absent or blocked): Mark as Complete, check that the TNA status changes to complete, and use Contact Us in the same session to confirm receipt. Case 3 (IPS/FR tasks open and editable and Review & Submit active): Mark as Complete only, ask Wharton, and vote at M3 (DL-15). If the form's own wording says how to submit, follow the form.** Submit on screen-share and screenshot the confirmation. [fixed 20 Oct, E5 overridden by RBC §0 item 2 and §3.5] | Paste checker; leader submits; deputy watches **and reads the rule aloud** | Thu 22 Oct 19:00-20:00 | F16, F18, F14 | Confirmation screenshot on the private Drive; **the case (1, 2 or 3), the button pressed and the status page are logged; in Case 2, the Contact Us receipt request is logged** |
| 9 | Request the school documentation letter: letterhead, administrator signature, the advisor's full name and every student's name, as the template requires. It must be signed by Fri 27 Nov (Fri 4 Dec is a staff PD day). [fixed 20 Oct, VPM2 §7] | Advisor and school liaison | Fri 23 Oct | F19 | The request and its date are logged |
| 10 | Back-fill session (30-40 min, all six) using the ART §6 questions, in your own words, with "recalled on" dates. Fill AI-log gaps S1-S17 from memory. The editor lists the submitted TNA claims as IPS constraints. **Anyone with a Mon 26 Oct exam answers in writing instead.** [fixed 20 Oct, E19] | Historian; every student; editor | Sun 25 Oct 17:00 (M4) | F5, F3, F6, F4 | Journal entries exist from 7 Oct onward; the claims list is posted |

**Also this week, cheap** (Wharton batch 1 moved into action 5 [fixed 20 Oct, E23]):
- The leader records that any outside reader is unpaid and gives scores only (Fri 23 Oct).
- The trade-log keeper fills the Trade Log from WInS history (Wed 21 Oct).
- The four options-note owners are named at M4 for the Mon 26 Oct 18:00 pre-read. **The rates analyst's note covers the retained-half reading and the $300.4k fee-counted ladder** [fixed 20 Oct, E1, E3].

---

## 6. Do NOT do

- Do not submit, paste, reword or "humanise" any sentence from V5, exemplars v1-v14, the [AI] reflections, the kits or this file. Do not use the StoryScope style study, an AI detector or any rewording loop.
- Do not strip the "[AI]" label from text that stays. Move the text or delete it.
- Do not rewrite git history to hide AI evidence (remove personal data only, and only if the repo will ever be public again). Do not delete the fervent-edison branch before its AI_USE rows 77-79 are copied into the team log.
- Do not let any AI tool operate WInS or SMApply, even read-only. Do not share the leader's SMApply password to work around F14 until Wharton answers (OPS R2).
- Do not add WInS notes or trades before the TNA is in. Never trade to reach a count. No order without a logged vote, and nothing entered after Wed 4 Nov 22:00.
- Do not quote: "0.02%", "zero in history", "three of four reach the top" (under 3r as written), "$293k" or "$294k" as the cost, "her first $300,000 is enough", "guaranteed", "locked", "secured", "cannot miss", "risk-free", "her other assets/holdings", or an undated "about 5.15%".
- Do not use 300/450 (0.667) as the WInS scale. Do not present WInS gains or the WInS value as performance, or as good news for Laura.
- Do not name TIPS or STRIPS as part of Laura's plan, or value anything on a "STRIPS basis". Do not name any security without a WInS search screenshot.
- Do not reopen floor size or the strategy after Tue 27 Oct without new evidence and four votes. Add nothing new to the strategy after Thu 5 Nov.
- Do not invent or "upgrade" a story, vote, attendance or who-did-what. Blanks stay blank, and nothing is reconstructed from AI files.
- Do not start new AI research waves or AI mock-judge runs before 7 Nov. Do not let an outside reader write sentences or story ideas.
- Do not quote "Don't use AI for personal reflection" as a competition rule. It is Pre-baccalaureate guidance (VAD P3). Quote AIP:224 and AIP:220.
- Do not contact Laura, use her personal contact details, or open rivals' Laura Gao repos.
- Do not commit the title page, roster names, the school letter, the IPS PDF or the WInS username to the repo.
- Do not delete version history, and do not "Make a copy" for a clean start. Move the AI text out; students type in the existing Doc or a new tab (RBC §0 item 4) [fixed 20 Oct, E11].
- Do not leave scheduled AI routines running that can read WInS or logged-in SMApply [fixed 20 Oct, E9].
- Do not quote exact top-reach percentages; use "about three in four" or "under half" [fixed 20 Oct, E2].

---

## 7. Limits and UNVERIFIED

- Every L and I score is AI judgement. No outcome data exists: Wharton publishes no scoring sheet and gives no feedback (RUB §1; SMF:81-82).
- The state of the team is read from Drive, GitHub and files only, as of Tue 20 Oct 10:15 (DLT). Work done offline, in chats or in personal accounts is invisible here. A blank in the record is not evidence that work was not done.
- UNVERIFIED and material: whether any member sits the HSC; the TNA form's fields and whether it locks; whether a single-tab PDF export prints suggestions; any "required trading activity"; how Wharton counts words; where the TNA's AI use should be recorded; whether WInS stays viewable after the freeze; the exact freeze time; the 2026-27 semifinal format; whether the outside reader is unpaid; the TNA's weight in Top-50 selection.
- The model figures (REC, LCK, CR) share one model family: parallel yield shifts with no mean reversion. Re-price on the 6 Nov close (REC §8).
