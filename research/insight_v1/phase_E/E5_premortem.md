# E5 Pre-mortem: "It is January 2027 and Team Caplet was not selected for the Top 50. Why?"

Agent E5 (pre-mortem analyst), insight_v1 run, Phase E. Written 2026-09-28 (the first official WInS trading day).
AI-generated research for Team Caplet: causes, rough ratings, preventions, owners and dates. **None of it is text to
submit.** It drafts no note, reflection, pitch or IPS sentence; where a short phrase names an idea it is a content
label, not wording to copy. The six students decide every change and write every word; AI use goes in the Final
Report's Works Cited (Wharton AI policy, R-W46).

**Serves:** the Trading Notes Analysis (**TN**, due Oct 23) and the IPS (**IPS**, due Nov 6) only, with WInS trading
in scope only as the source of the notes (brief section 17). Rules the Final Report will later apply are listed under
"IPS: rules to fix before Nov 6" (section 4). Pure Final Report items are one line each in section 7.
**Relayed messages:** none arrived during this task.

**Status labels** (brief section 3): **VP** = VERIFIED-PRIMARY; **VRF** = VERIFIED-REPO-FILE; **SNIP** =
SNIPPET-UNVERIFIED; **ASM** = ASSUMPTION; **MODEL** = an ASSUMPTION-based model output, not a forecast; **DER** =
derived by a script from labelled inputs; **INT** = E5's judgement. **Every likelihood and impact rating in this file
is INT/ASM**: a rough ranking for deciding where to spend the team's hours, not a measured probability. Ids: R- case
register, F- fact register, SH-/BS- stakeholder map, P- E1 proposals, F1-F10 E2 fixes, E3-n E3 changes (all under
`research/insight_v1/`).

**New script:** `.venv/bin/python research/insight_v1/scripts/E5_premortem_checks.py` (under a second, no network;
docstring lists inputs and labels). It prints [1] every deadline in Australian time, [2] U.S. trading hours in
Australian time on the dates that matter, [3] the ranked risk register, [4] a robustness check of the ranking under
two other impact weightings.

**Evidence read** (audit corrections override the text above them): the brief; CLAUDE.md;
`phase_E/E1_change_proposals.md` (the plan being attacked), `E2_judge.md`, `E3_laura.md`;
`wins_now/securities_and_allocation_v1.md` (the ticket), `phase_D/trading_now_brief.md`, `wins_now/T2_red_team.md`;
`phase_D/D10_compliance.md` (+AX2), D7 (+AY2), D9 (+AY2), D12 (+AY1), the summaries and audit sections of D1-D6, D8,
D3_model_v2_results, D13c sections 3-5, all five audit files; `phase_A/wins_week1_guardrails.md` (the G list),
`case_register.md` (R-W, R-AN), `stakeholder_map.md` (SH-16 to SH-26, BS-01 to BS-20); the official case, IPS guide,
TN guide, Competition Guide, Infographic and SMApply page; the council chair memo (history only).

**Terms (defined once):**
- **Pre-mortem:** imagine the project has already failed, then list the reasons. It finds risks that optimistic
  planning hides.
- **Likelihood (L):** rough chance the failure happens by its deadline if the team does nothing beyond what exists on
  2026-09-28. Bands: VL ≈2%, L ≈6%, LM ≈11%, M ≈20%, MH ≈30%, H ≈40% (ASM).
- **Impact (I):** what the failure does to the chance of a Top-50 place. **Fatal** = excluded or disqualified;
  **Severe** = a whole deliverable or two criteria badly hurt, or an integrity question; **Major** = about 1-2 points on
  a criterion; **Moderate** = under a point; **Minor** = cosmetic (ASM).
- **Expected harm:** L × impact weight (Fatal 1.0, Severe 0.6, Major 0.3, Moderate 0.15), used only to rank.
- **Owner-type:** a role, not a named student: team leader, trader (the one student who places orders, plus a
  backup), note writer, second reader, log keeper (decision log and AI-use log), IPS lead writer, format checker, rates
  analyst, growth/risk analyst, client lead, admin liaison (roster and school paperwork, with the advisor for admin
  only). Roles follow CLAUDE.md's suggested list; the team assigns people.
- **Book (ii) / (iii):** the two candidate WInS books in the ticket: (ii) the plan's mix after both deposits, scaled to
  $300,000; (iii) Laura's literal January 2027 book (about 98% Treasury funds).
- **Swap test:** put another client's name into a sentence; if it still works, the sentence is generic (D13c, INT).
- **AEDT / AEST:** Sydney summer time (UTC+11, from Sun 4 Oct 2026) / standard time (UTC+10). ET = U.S. Eastern.

---

## 0. Summary

### 0.1 The most likely failure story (INT, written from January 2027)

We never learned why: "Teams will not receive individual feedback" (R-W40, VP), the same silence as last season
(CLAUDE.md, VRF). Looking back, the likeliest story is not a bad strategy. The substance was of Top-50 quality (E2
verdict, INT). The failure was in **ownership, packaging and process**:
1. The six students adopted a plan whose main calls they had deferred to an AI and never argued over (CLAUDE.md: "The
   team has not read the memos yet"; "the team deferred to the assistant's evidence-based calls", VRF). The notes,
   pitch and IPS carried AI-coined labels and a density no student would write, so the "authentic team voice" and
   "reflects meaningfully" parts of two criteria (SMApply criteria, VRF) scored low.
2. The IPS tried to carry about 55 ideas in about 480 words (E2 3.2, INT) and read as a rulebook, not a strategy a
   reader could restate.
3. Under book (ii) the day-one world-stock purchase appeared to contradict a pitch worded as a ban on stock risk (AY2
   rank 1, VRF), and the scaling sentence that explained it was cut for space.
4. Nobody owned the PDF test, so the last draft's layout was never checked on Word's line height (D9/AX2, MODEL).
   This one is fatal, and cheap to prevent.
5. The work was squeezed into the last weekend. If any member sat NSW HSC exams (13 Oct to 5 Nov 2026, VP), that
   period covered both deadlines; the team's state and year levels are not recorded (UNVERIFIED whether it applies).

Against about 2,300 teams that finished last season (R-W99, VP), the Top 50 is roughly the top 2% (arithmetic; INT
that the share is similar this year). At that margin, several "Major" losses together are enough to miss.

### 0.2 The top 10 causes (ranked by expected harm; E5 script [3]; ratings INT/ASM)

| Rank | Id | Cause | Serves | L | Impact | The prevention in one line | Owner-type | By (Australian time unless ET) |
|---|---|---|---|---|---|---|---|---|
| 1 | PM-01 | Strategy not owned by the students; voice reads AI-made | TN + IPS | H | Severe | Own-words gate before every vote; devil's-advocate pairs; blank-page drafting | team leader | before the gate vote (Wed Sep 30 AEST); IPS draft Mon Oct 26 AEDT |
| 2 | PM-02 | IPS format breach (third page overflows; word cap by another counter; font; banned items) | IPS | M | Fatal | Fit on Letter at Word "Double"; ≤470 IPS words by two counters; PDF check by two students | format checker | every draft from Oct 26; final Wed Nov 4 AEDT |
| 3 | PM-03 | Over-complex, jargon-dense pitch and IPS | IPS | H | Major | ≤12 ideas; dated 2027-2028-2031-2033 spine; no codes; 6-reader paraphrase test | IPS lead writer | idea list Sat Oct 24; tests Oct 26-30 and Nov 2-3 |
| 4 | PM-04 | AI wording in permanent WInS notes or in reflections | TN | M | Severe | Notes drafted offline from elements only; text search of `research/` for copied runs; no AI "polish" | note writer + second reader | before every order (first fills by Fri Oct 2 ET); reflections Oct 21-22 AEDT |
| 5 | PM-05 | Team process breakdown (no roles, one login, holidays and exams, late drafting) | TN + IPS | H | Major | Roles and a shared exam/travel calendar this week; internal deadlines two days early | team leader | roles Tue Sep 29 AEST; calendar Wed Sep 30 AEST |
| 6 | PM-08 | AI use not logged, or logged inaccurately | TN + IPS | M | Severe | Dated AI-use log from today, reconciled with the repo's commit history | log keeper | start Tue Sep 29 AEST; weekly |
| 7 | PM-06 | Notes contradict the pitch/IPS (book date, scaling, split, labels) | TN + IPS | MH | Major | Central idea worded as a split of jobs; scaling marker inside (ii) notes; two-reader check; consistency table | log keeper + IPS lead writer | before the first order; checks Oct 22 and Nov 3 AEDT |
| 8 | PM-07 | Plan reads timid or as analysing her; residency missing | TN + IPS | MH | Major | Purpose first in the pitch; forced vs chosen caution; stocks' purpose; one stress clause for the $150k | client lead | pitch elements Sat Oct 24; draft check Fri Oct 30 AEDT |
| 9 | PM-09 | Generic thesis (fails the swap test; the hedge note is Wharton's example) | TN + IPS | MH | Major | Swap test on every note and IPS paragraph; lead with three Laura-specific decisions | client lead | each note; IPS Oct 26-Nov 3 |
| 10 | PM-14 | WInS rule breach (instrument, day trade, position cap, negative cash) | TN (WInS) | LM | Severe | One trader plus backup; A4 checklist read aloud; Session Rules screenshot; never a same-day sell | trader + second reader | Session Rules by Thu Oct 1 AEST; every order |

- **Robustness (E5 script [4], DER on ASM weights):** PM-01 to PM-08 stay in the top 10 under all three weightings.
  Several ranks are ties at the same score (ranks 3-6, ranks 7-9), so read the order inside a tie as arbitrary. Rank 10
  is a **tie** between PM-14 (rule breach), PM-15 (undefined activity minimum) and PM-16 (fewer than three executed
  trades). E5 puts PM-14 first because last year's team actually "traded assets outside the trading rules" (CLAUDE.md,
  VRF), a base-rate reason (INT). Under an exclusion-heavy weighting, PM-13 (missed deadline) and PM-18 (title-page
  mismatch) enter the top 10 in place of PM-09 and PM-14; under a quality-heavy weighting, PM-10 (overclaiming) enters
  in place of PM-14.
- **Cheap-and-fatal box (do these whatever the ranking; each costs under an hour, INT):** PM-02 PDF test, PM-13
  deadline plan, PM-18 title page copied from the roster, PM-19 roster submitted early, PM-26 no contact with Laura,
  PM-27 no paid help, PM-28 membership kept at six.

### 0.3 What this file adds to E1-E3 (so the synthesis can merge it)

- It turns E2's scoring worries and E3's client worries into **owned, dated preventions**, and adds causes none of E1-E3
  covers: ownership of the strategy by the students (PM-01), the accuracy of the AI-use record against a public repo
  (PM-08, PM-30), the Australian school calendar (PM-05), an undefined trading-activity rule (PM-15), unread SMApply
  submission forms (PM-23), who can submit on SMApply (PM-13), roster-to-title-page exactness (PM-18, PM-19), and
  shared-login discipline (PM-14).
- Its format stance is stricter than E1 P16: make the IPS fit under **Word's "Double" on U.S. Letter**, the strictest
  reading, so no interpretation of "double-spaced" or paper size is ever needed (INT). "Exactly 24 pt" (AY2, INT) stays
  a documented last resort, not a plan.

---

## 1. How the ratings were made (and their limits)

- **Likelihood** is E5's judgement of the chance, given the repo's state on 2026-09-28: no roles assigned, no trade
  placed, no vote taken, no IPS draft, the team "has not read the memos yet" (CLAUDE.md, VRF). It falls as preventions
  are done. It is not a model output (INT).
- **Impact** reads the official consequences literally where they exist: IPS format breaches mean "will not be
  considered for semifinal selection" (IPS guide L82-83, VRF); contact with the client, team size and paid help mean
  disqualification (R-W16, R-W17, R-W21, VP via A1/A4); missed deadlines lose eligibility ("To remain eligible for the
  Semifinals ... submit the competition deliverables by the published deadlines", Rules & Roles, VP via A4). Quality
  losses are scaled to E2's criterion scores (INT).
- **Which deliverables count for selection** is itself uncertain: the Rules page names "the strength of their
  Investment Policy Statement (IPS) and Final Reports" (R-W24, VP), while SMApply says the TN, IPS and Final Report "are
  evaluated" (VRF). The safe reading is that all three are scored (R-AN41, INT). This file treats TN failures as real
  losses, and the IPS as the heavier deliverable.
- **Robustness:** the ranking was re-run with an exclusion-heavy and a quality-heavy set of impact weights (script [4]).
  The top 8 do not move out of the top 10 in any of the three runs. Treat ranks 9-18 as roughly equal.

---

## 2. The top 10 in detail

Each entry: what failed (January 2027 view); why it was plausible (evidence); ratings; **tripwires** (early warning
signs to watch); **prevention** (specific steps); owner-type; dates. All dates are 2026.

### PM-01. The strategy was not the students' own, and it showed (TN + IPS; L = H, Impact = Severe)

**What failed.** The key calls (lock early; book (ii) or (iii); the growth split; the 2031 slices; where kept money
sits) were taken by accepting AI recommendations. The notes and IPS used AI-coined labels and research-file phrasing.
Reflections described decisions the students could not explain in their own words. Readers scoring "an authentic team
voice" (Creativity and Presentation) and "reflects meaningfully on the team's growth" (Articulation) marked the team
down (SMApply criteria, VRF). In the worst case a reader read it as AI-generated work "submitted as your own" (R-W26, VP).

**Why it was plausible.**
- The current state: "NOT YET DECIDED BY THE TEAM. The team has not read the memos yet"; "the team deferred to the
  assistant's evidence-based calls, provisionally" (CLAUDE.md, 2026-09-27, VRF).
- All team members are responsible for "Developing and implementing the team's investment strategy" (R-W15, VP via
  A1). Students "must use their voice and words" (R-W49, VP). Wharton's own self-check: "Did I come to my current
  conclusion before or after using generative AI tools?" (R-W51, VP).
- The research behind the plan is overwhelmingly AI-produced, with a risk of "artificial sophistication" (E2 2.4, INT;
  SH-16 "readers fear AI-written text", ASM).

**Tripwires.** A student cannot explain a rule without opening a file. A vote is logged with no student's own reason.
Nobody argued the other side before a vote. Draft sentences use the research files' labels ("promise money", "three
slices", "funded ratio").

**Prevention.**
1. **Own-words gate before every vote** (lock early, book, split; later the 2031 slices and kept money): each student
   writes 3-5 lines on the question with no AI file open, *then* reads the research, *then* votes. The log keeps both,
   dated. This is the order R-W51 asks about. Owner: team leader. By: the gate vote (target Wed Sep 30 AEST); IPS
   parameters by Mon Oct 26 AEDT.
2. **Devil's-advocate pairs:** for each of the five calls above, one student argues against it in the meeting; the log
   records why the team kept or changed it. Owner: team leader. By: the gate meeting; one IPS meeting about Oct 24-25.
3. **Explain-back check (internal learning, not finale preparation):** each student explains the central idea and the
   four dated decisions (2027, 2028, 2031, 2033) in two minutes without notes. Anyone who cannot, re-reads and retries.
   Owner: second reader. By: Sun Oct 25 AEDT, again Tue Nov 3 AEDT.
4. **Blank-page drafting:** the IPS and every reflection start from a blank page with research files closed; the
   research is used only afterwards to check facts and numbers. Owner: IPS lead writer. By: first IPS draft Mon Oct 26.
5. **The team names its own labels** for the parts of the portfolio in a meeting and logs that the proposals came from
   an AI source (T2 finding 8; E2 F10). Owner: note writer. By: before the first note.

### PM-02. The IPS broke a format rule and was never read (IPS; L = M, Impact = Fatal)

**What failed.** The exported PDF spilled onto a fourth page, or the pitch counted 51 words in Wharton's counter, or a
typed web address became a live link, or the file was set in a substitute font. "Submissions that do not meet the
requirements below will not be considered for semifinal selection" (IPS guide L82-83, VRF).

**Why it was plausible.**
- Rules: title page 1 page; pages 2-3 "2-page maximum"; pitch "maximum 50 words"; IPS "maximum 500 words"; Times New
  Roman 12, double-spaced, 1-inch margins; PDF ≤5 MB; "Graphics, charts, images, attachments, external links,
  footnotes, and formal citations are not permitted" (IPS guide L84-123, VRF).
- At Word's "Double" line (27.6 pt for Times New Roman 12, ASM) on U.S. Letter, 50 + 500 words leave 0-2 spare lines;
  with 7 paragraphs and 0 pt paragraph spacing the text "does not reliably fit" (D9; AX2 on D10 C3; MODEL). Wharton's
  own sample is set at 24 pt (VRF, measured).
- E1's budget is 270-435 words before connecting words (P16, INT) and E2/E3 each add clauses (diversification,
  liquidity, forced vs chosen caution, cost principle). The pressure is upward.
- Word processors count "U.S.", "$50,000", hyphens and slashes differently (D10 checklist, ASM).

**Tripwires.** Any draft above 470 IPS words. Any draft never exported to PDF. An addition after the last PDF check.
Two students reporting different word counts.

**Prevention** (owner: format checker; a second student repeats every check independently):
1. Target **≤470 IPS words and ≤48 pitch words**, counted in Word **and** a second counter; if they disagree, use the
   higher count. By: every draft from Mon Oct 26 AEDT.
2. Lay out on **U.S. Letter at Word's "Double"**, paragraph spacing 0, no blank lines, at most 7 paragraphs, headings in
   Times New Roman 12. If it fits there it fits under any reading (INT). A4 is allowed by "Formatting choices not
   specified below are left to the team's discretion" (IPS guide L101, VRF; INT reading), but should not be relied on
   to make a long draft fit.
3. Export the PDF; open the exported file; confirm **exactly 3 pages**, the text ending on page 3 with at least 2 spare
   lines, 1-inch margins, file ≤5 MB, and the PDF's font list showing Times New Roman (a font substitution by Google
   Docs or LibreOffice is cheap to catch; whether a reader would treat it as a breach is ASM).
4. Search the PDF for "http", "www", a year inside brackets, and quotation marks: no links, no "(Source, year)"
   citations, no quotes of anyone's words; then look for tables, bullet lists and footnotes (D9 format checklist; D13
   rules).
5. Freeze the words **Tue Nov 3 AEDT**; final PDF check **Wed Nov 4 AEDT**; nothing is added after it.

### PM-03. The IPS was right but unreadable (IPS; L = H, Impact = Major)

**What failed.** Four rules, a governance clause, three 2031 slices with letters, bands, two named gaps, a joint tail,
four bad-year pre-commitments and three trade-offs in about 480 words. The reader could restate the first rule but not
the 2031 method, and no single sentence stuck. Last year's lesson, "strategy packaging was over-complex for the
insight" (CLAUDE.md, VRF), repeated at the level of words.

**Why it was plausible.** E1 specifies about 55 distinct ideas for the pitch plus IPS, about one per 9 words (E2 3.2,
INT). E2's two-minute test predicts the 2031 method is "likely missed" (INT). A past-season Wharton judging page:
"Excessive investing jargon doesn't necessarily dazzle the judges" (VP, retired page, via D9/AY2). A 2025 semifinal
judge praised "simple, elegant ideas" (VP via D7/AY2, past season).

**Tripwires.** More than about 12 distinct ideas in the draft. Any code or term from E2's jargon table (3.3): "80/10/10",
"p90", "a/s/q", band numbers, "funded ratio", "duration", "STRIPS", "LDI", "DV01", "glide path". Headings of the form
"Rule 1-4 + G" rather than dates. A non-finance reader cannot restate the 2031 method.

**Prevention.**
1. **Pick at most 12 ideas before drafting** (E2 F1's list is a starting menu); everything else goes to the team's
   "later" list. Owner: IPS lead writer. By: Sat Oct 24 AEDT (after the TN is in).
2. **Dated spine:** January 2027, January 2028, January 2031, January 2033, each with one action and one "because" tied
   to the case (E2 F2); branches become "if" clauses. Owner: IPS lead writer. By: first draft Mon Oct 26.
3. **One plain phrase per parameter**, used once; no letters or codes (E2 3.3; E3 4a). Owner: second reader. By: each
   draft.
4. **Paraphrase test** with 6 unpaid readers (3 without finance, 3 with), who restate and never supply words; change
   any sentence that 2 or more misread; target questions: the 2031 method, why longest-dated first, what could still
   stop a payment (D12 M234; E1 P16; digital.gov method VP via D12). Unpaid adult help is allowed; paid help is not
   (R-W21, VP). Owner: IPS lead writer. By: rounds Oct 26-30 and Nov 2-3.

### PM-04. AI wording reached a permanent WInS note or a reflection (TN; L = M, Impact = Severe)

**What failed.** At a late-night gate session a note writer typed a phrase from the ticket, or lightly edited one, into
the WInS note box. Notes cannot be edited and are quoted "exactly as it appears in WInS" in the TN, so the AI wording
became part of a submitted deliverable. Reflections were then "tidied" in an AI chat.

**Why it was plausible.**
- "Include each Trading Note exactly as it appears in WInS" (TN guide L44, VRF); notes cannot be edited or deleted,
  only added to (Stock-Trak 2017 blog, VP vendor page via A4; not season-specific).
- The ticket and specialist files contained near paste-ready clauses (T2 finding 8; AY2 section 7, VRF); the ticket
  was since recast as elements, but several phrases remain short enough to copy (INT).
- Wharton's pre-baccalaureate AI guidance says "Don't use AI for personal reflection or opinion-based tasks" (R-W50,
  VP; written for another programme, a strong signal only, INT). Running the D9 draft checker counts as AI use (AY2 D9
  C12, VRF).

**Tripwires.** A draft note with no paper or offline draft in the log. A draft note that shares any five-word run with
a file in `research/`. A reflection drafted inside an AI chat.

**Prevention.**
1. Each note drafted by one student **offline, from the element list only** (role word, Laura's dated need, one dated
   checkable fact, the risk or rule; ticket section 5), with no research file open. Owner: note writer. By: before each
   order (first fills by Fri Oct 2 ET = 23:30 Fri Oct 2 AEST at the open).
2. **Copy check:** the second reader takes every run of five consecutive words in the draft and searches the
   `research/` folder for it (a plain text search, not an AI tool); any hit is rewritten by the note writer. Owner: second
   reader. By: before each order.
3. The draft is pasted into the decision log first, then into WInS; the saved note is copied back character for
   character with a screenshot (A4 checklist items 16-17). Owner: log keeper. By: each order.
4. **Reflections:** written by students without AI; any later AI use (for example checking a number) is logged.
   Owner: note writers. By: drafts Wed Oct 21, final Thu Oct 22 AEDT.

### PM-05. The team's process broke down (TN + IPS; L = H, Impact = Major)

**What failed.** Six students, one shared login, no roles. The gate meeting slipped during the school holidays; the first
fills came in week 2, shrinking the "tested" window; one student wrote every note at 1 a.m.; the IPS was drafted by one
person over the last weekend while others had exams; nobody owned the PDF test; the second reader never saw the final
version.

**Why it was plausible.**
- "No roles assigned yet" (CLAUDE.md, VRF). "All team members must play a contributing role" (R-W38, VP). "We strongly
  encourage teams to identify different roles for each team member" (SMApply FAQ, VP via A4).
- NSW public-school spring holidays are Mon 28 Sep to Fri 9 Oct 2026, and Term 4 starts Tue 13 Oct
  (https://education.nsw.gov.au/schooling/calendars/2026, read 2026-09-28, VP). The whole WInS gate week falls in those
  holidays, and the roster deadline (Sat Oct 10, 08:00 AEDT) falls the morning after they end. The team's state and
  school type are not recorded, so this may not apply (UNVERIFIED for the team).
- The 2026 HSC written exams run from Tue 13 Oct to the morning of Thu 5 Nov
  (https://www.nsw.gov.au/education-and-training/nesa/news/all/2026-hsc-timetables-released, read 2026-09-28, `--grep`
  found verbatim, VP). That window covers the TN deadline and ends the day before the IPS deadline. It matters only if
  a member sits the HSC; year levels are not recorded (UNVERIFIED for the team).
- U.S. trading opens at 23:30 AEST before Oct 4 and 00:30-01:30 AEDT after it (E5 script [2], DER), so "watching the
  fill" means staying up.

**Tripwires.** The gate is not passed by Thu Oct 1 AEST. A week with no logged meeting. One student's name on more than
half the log entries. No full IPS draft circulated by Mon Oct 26.

**Prevention.**
1. **Assign roles now**: trader (+ backup), note writer(s), second reader, log keeper, format checker, IPS lead writer,
   rates analyst, growth/risk analyst, client lead, admin liaison. Every student drafts at least one note or reflection
   and one IPS section. Owner: team leader. By: Tue Sep 29 AEST.
2. **Shared calendar** of each student's exams and travel; internal deadlines move around them. Owner: team leader. By:
   Wed Sep 30 AEST.
3. **Internal deadlines two days early**: gate passed Thu Oct 1 AEST; roster submitted Wed Oct 7 AEDT; TN submitted Thu
   Oct 22 AEDT; IPS first draft Mon Oct 26; words frozen Tue Nov 3; IPS submitted Thu Nov 5 AEDT. Owner: team leader.
4. **Weekly 30-minute check-in** with a written log line (who did what). Owner: log keeper. By: every Sunday.
5. **Time split:** after Oct 23, most hours go to the IPS (it may be the heavier deliverable for selection, R-W24 vs
   SMApply; R-AN41). Owner: team leader.

### PM-08. AI use was not recorded, or was recorded inaccurately (TN + IPS process; L = M, Impact = Severe)

**What failed.** In December the Works Cited said only "AI was used for brainstorming". The team's public repository
shows a multi-agent research run that specified note elements, pitch elements and rule parameters. The record
understated the use; or it omitted the draft checker and the fetch tool. An honest record made late looked worse than
a clear dated one (INT).

**Why it was plausible.** "If you use AI to assist you in any way during the competition, how you use it must be
recorded in your Works Cited pages" (R-W46, VP) and "including how and where students used AI-generated information"
(R-W49, VP). AI use not recorded is treated as misuse (A4 e8, INT). The repository is public on GitHub (git remote,
VRF; CLAUDE.md "Repo is public", VRF), so anyone can compare the record with the files. The Works Cited itself is
Final Report work (later); the log that feeds it starts now.

**Tripwires.** No AI-use log entry by Sunday Oct 4. Entries that say what the AI produced but not what the team decided
or verified itself.

**Prevention.**
1. **Start the AI-use log today** with columns: date; tool; which student; purpose (brainstorm, fact-check, number
   check, draft check); what the AI produced (file path); what the team decided and whether before or after seeing the
   AI output (R-W51); what the team verified independently. Owner: log keeper. By: Tue Sep 29 AEST, then weekly.
2. **Backfill** the council, the blueprints, this research run (`research/insight_v1/`), the D9 draft checker and the
   fetch helper. Owner: log keeper. By: Sun Oct 4 AEDT.
3. **Reconcile** the log with the repository's commit history, which is itself a dated record. Owner: log keeper. By:
   Oct 23 (before the TN) and Nov 6 (before the IPS).

### PM-06. The notes contradicted the pitch and the IPS (TN + IPS; L = MH, Impact = Major)

**What failed.** Under book (ii) the reader met the notes first: a world-stock fund bought on day one beside a hedge worth
about two-thirds of the book, while the pitch was worded as a ban on stock risk until the payments are bought. The IPS
sentence that explained the scaling had been cut for words. The growth note said one split and the IPS another, with no
logged change, and the same holding had two labels. The reader saw two strategies.

**Why it was plausible.** AY2 rank 1 and E2 C1 flag exactly this (VRF). "Your portfolio and Final Report should reflect
the strategy established in your IPS" (IPS guide L75, VRF); the Investment Strategy criterion "maintains consistency
with the team's IPS" (VRF); "The analysis should be consistent with the strategic approach your team is developing
and will later articulate in its IPS" (TN guide L30-31, VRF). Under (ii) WInS holds about 17.0 points more stock than
Laura's real January 2027 money at 50/50, or 20.5 at 60/40 (D10 with AX2 C7, MODEL).

**Tripwires.** A pitch draft worded as a ban tied to time. No sentence in the IPS draft naming the date or state WInS
shows. A (ii) hedge or growth note without its "after both deposits" / "after her 2028 deposit" marker. A split in the
growth note that differs from the IPS rule. Two labels for one holding.

**Prevention.**
1. Word the central idea as a **split of jobs**, true of both books (E2 F4); keep the ordering (payments first) in the
   2027/2028 rule. Owner: IPS lead writer. By: pitch elements Sat Oct 24.
2. Under (ii): the scaling marker **inside** each hedge and growth note, within the note-box limit; one IPS sentence with
   the elements: post-2028 mix, scaled to $300,000, stand-in funds rather than the ladder, and that in January 2027
   almost all of her real $300,000 buys the ladder (D10 1.5; T2 16a; ticket section 5). Owner: note writer; IPS lead
   writer. By: before the first order; IPS draft.
3. **Two-reader check** before the first order: two readers outside the team read the note drafts and say what Laura's
   real money holds in January 2027; if either says "stocks", fix the drafts (E3-10). Owner: second reader. By: gate
   session.
4. **Consistency table** in the decision log (note → IPS rule name → label), checked before each submission. Owner: log
   keeper. By: Thu Oct 22 and Tue Nov 3 AEDT.
5. A split change before Nov 6 is allowed only as a logged, research-based decision with a trade, never because prices
   moved (AX2 D2 C3, VRF). Owner: growth/risk analyst. By: Fri Oct 16 ET if the split was provisional (ticket calendar).

### PM-07. The plan read as timid, or as a study of her rather than a plan for her (TN + IPS; L = MH, Impact = Major)

**What failed.** The reader saw almost no stocks (about 98% Treasury funds under (iii), about 17% stocks under (ii)) for a
client who "has been willing to take thoughtful risks", no stated purpose for the stocks, the $150,000 deposit doubted
in three places, a long list of caveats, trap vocabulary about her ("loss tolerance", "house money"), and a pitch that
never mentioned the residency. "Presents recommendations that can earn her confidence" (Client Knowledge, VRF) scored
low.

**Why it was plausible.** Case L69-74 (VRF). The payments cost 97.4-98.1% of her first deposit at the Sept 25 curve, so
little stock in 2027 is forced by prices, not chosen (E3 [1], MODEL on VRF inputs); the whole-portfolio stock share
averages about 9.7% over 2027-2032 at 50/50 (E3 [2], MODEL). E2 2.2 finds the residency missing from the pitch spec, the
$150k doubted too often and the statistics degree used as a lever (INT). E3 findings 2, 3, 6 and 10 (SIM/INT).

**Tripwires.** No "residency" in the pitch draft. Any sentence about her temperament. "Risk-averse", "loss tolerance",
"trap" or "composure" in a draft. More than about 15% of IPS words on what could go wrong (E3-11, ASM ceiling). The
$150k called uncertain more than once.

**Prevention.**
1. **Pitch order:** what the plan secures for the residency, then the rule, then what the rest is for (E3-5; E2 F3).
   Owner: client lead. By: Sat Oct 24.
2. **Forced vs chosen caution** stated in the risk passage, with at most one dated, rounded price fact (E3-2). Owner:
   client lead. By: first IPS draft Mon Oct 26.
3. **What the stocks are for** in the growth rule's "because" (E3-3; E2 F6). Owner: growth/risk analyst. By: Oct 26.
4. **One labelled stress clause** for the $150,000; the case says she "will" contribute (case L43, R-AN35, VRF). Owner:
   IPS lead writer. By: Oct 26.
5. **No behavioural diagnosis** of her in any note, reflection or the IPS; pre-commitments framed as the firm's own
   discipline (E3-6). Owner: second reader. By: every draft.
6. Under (iii): one reflection answers "why so little equity" with the forced-vs-chosen content (ticket section 4).
   Owner: note writer. By: Thu Oct 22.

### PM-09. The thesis read as generic (TN + IPS; L = MH, Impact = Major)

**What failed.** "Buy the payments with Treasuries, invest the rest" is standard pension practice, and many AI-assisted
rivals reached it. The hedge note was Wharton's own example trade in different words. The Laura-specific reasons sat
in the middle of rule 3.

**Why it was plausible.** Wharton's example note buys "an intermediate-term U.S. Treasury bond ETF ... for Laura's future
operating commitment" (TN guide L36-39, VRF; R-AN44). Rivals using the same AI tools may reach the same architecture
(BS-10, ASM). The surplus approach is named industry practice (Russell 2026, VP via D8/AY2). "Presents a clear and
creative investment thesis" (Investment Strategy, VRF). D13c N7: do not call the plan "innovative" (INT).

**Tripwires.** A draft sentence that still works with another client's name. A hedge note with no dated need and no
checkable fact. A pitch with no benefit only Laura gets.

**Prevention.**
1. **Swap test** on every note, reflection and IPS paragraph; failures are rewritten or cut (D13c, INT). Owner: client
   lead. By: each note; IPS drafts Oct 26-Nov 3.
2. Lead with the **three Laura-specific decisions**: the payments are bought before her career-income deposit can matter
   (case L43-45); nothing is announced to co-sponsors that is not already bought (L114-116); certainty is defined by a
   price she can check (L97-99) (E1 North Star; D7 M011; VRF case lines, INT selection). Owner: IPS lead writer. By: Oct
   24 idea list.
3. **Hedge note:** her dated need, one checkable fact and the never-sell rule; no "reduce volatility" (ticket section 5;
   D9 M012). Owner: note writer. By: the first order.
4. Show originality through fit, never by claiming novelty. Owner: second reader. By: every draft.

### PM-14. A trade broke a WInS rule (TN via WInS; L = LM, Impact = Severe)

**What failed.** Someone on the shared login bought a stock under $5, a leveraged, inverse or crypto-linked fund, or an
exchange-traded note; or sold a fund the same day to "fix" a mistake; or a Treasury fund crossed an unseen position
limit after rates fell; or an order at the open pushed cash below zero. Last year's lesson repeated.

**Why it was plausible.**
- Last season the team "traded assets outside the trading rules" (CLAUDE.md, VRF).
- Permitted: cash, stocks ≥$5, "Any Exchange-Traded Funds (ETFs) available on WInS", government/Treasury bonds on WInS;
  banned: margin, short selling, stock-secured debt, crypto, derivatives, "Anything other than the approved
  investments listed above" (SMApply FAQ, VP via A4). "Day Trading: This is not permitted." (2026-27 WInS User Guide,
  VP via A4). Leveraged and inverse funds use derivatives internally (R-AN49, INT). The position limit is visible only
  in Session Rules; the Stock-Trak default is 25% (VP, generic page).
- "Each team shares one WInS account" (R-W14, VP): anyone can place an order.
- A holding placed one point under a 25% cap crosses it after about a 101-128bp rate move, or a 20-24% stock fall, or a
  10-12% stock fall with a 50bp rally (D10; T2 [5]; MODEL, ASM that WInS re-checks the limit).
- Orders entered while the market is closed fill at the next open (SMApply Trading Details, VP), so a thin cash float
  can be overrun (T2 finding 1, MODEL).

**Tripwires.** More than one person placing orders. An order that was not in the log before it was placed. Any holding
within one point of the cap. The cash float under $1,000.

**Prevention.**
1. **One trader and one backup** place every order; others never do (a team convention; the account itself stays
   shared, R-W14). Owner: team leader. By: Tue Sep 29 AEST.
2. The A4 **"before every trade" checklist** (guardrails section c) read aloud by the trader and ticked by a second
   student. Owner: trader + second reader. By: every order.
3. **Session Rules screenshot** (both position-limit lines, the day-trading tooltip, trades allowed) and the cap branch
   chosen in advance (ticket section 3). Owner: trader. By: Thu Oct 1 AEST, before the first order.
4. **Never sell the same security on the day it was bought**; an error is logged and lived with ("run with it", SMApply
   FAQ, VP). Owner: trader. By: every order.
5. Recompute share counts from the last close; keep at least $1,000 in cash; never add to a holding near the cap
   (ticket). Owner: trader. By: every order; weekly cap check by the log keeper.

---

## 3. The other 20 causes

Ratings INT/ASM; expected-harm ranks from E5 script [3]. "Owner" is a role, not a student.

| Rank | Id | Cause (January 2027 view) | Serves | L | Impact | Evidence (labels) | Prevention | Owner-type | By |
|---|---|---|---|---|---|---|---|---|---|
| 11 | PM-15 | A "required trading activity" minimum existed on a logged-in page and the low-trade plan (4-5 orders) missed it | TN (WInS) | LM | Severe | "Teams must meet the required trading activity and portfolio management guidelines" is undefined on public pages (R-W23, VP; D10 s3); "first trade by Oct 10" is a 2023-24 claim (SNIP, A4) | Read the logged-in Trading Details, Getting Started and weekly emails before the first order; if a minimum exists, ask Wharton (Contact Us) and meet it with plan-consistent trades logged with the rule as the reason; if none, log "none found" with a screenshot. Never stage a trade to fill a note category (T2 finding 13) | team leader | Thu Oct 1 AEST; weekly emails checked each Monday |
| 12 | PM-16 | Only two usable executed trades by Oct 23 (under (iii) the T-bill leg vanished after a rate fall; an order was rejected; indecision delayed the fills) | TN | LM | Severe | "Select three (3) Trading Notes from trades your team executed in WInS"; "Yes, we will verify this" (TN L42, L53, VRF); (iii) T-bill leg under $1,000 after a ~12bp fall, about 11% by Oct 2 and 19% by Oct 9 (T2 finding 1, MODEL) | Under (iii), apply the ticket's pre-set rule (leg under $1,000 and no listed dated rung → revert to (ii)); market orders at the gate session; confirm "Filled" in Order History and a note on each trade | trader | fills by Fri Oct 2 ET; verified Mon Oct 5 AEDT; hard stop Fri Oct 9 ET |
| 13 | PM-10 | Overclaiming words: "guaranteed", "safe", "risk-free", "95%", "bought in January 2027" or "fits inside $300,000" as flat facts, "matched" or "operating reserve" for WInS funds, "locked"/"known" 2028 rates, "promised" for the 2031 stretch, "only the facility shrinks" (false in the joint tail), "innovative" | TN + IPS | H | Moderate (Major if in the pitch or a permanent note) | Ticket s5 and brief s2 banned lists; D7 M011 (date claim false in about 1 path in 3, MODEL); E3 finding 1 ("promised"); AY2 rank 2 (joint tail); the chair memo itself used "only the facility shrinks" (VRF, history) | A banned-word list pinned beside the note box and the IPS; the second reader searches every draft for each word; certainty words used only for their objects (D9 M062 with AY2 C2) | second reader | every note; IPS drafts Oct 26-Nov 3 |
| 14 | PM-11 | A required IPS element was missing: the definition of "high degree of funding certainty" and how it was evaluated; diversification; liquidity; reserve composition over time; facility approach; flexibility; the inflation and facility-cost assumption; the "funded 2027, set aside 2033" reconciliation | IPS | M | Major | Case L94-99 and L146-148 (VRF); IPS guide L45-50 and L53-65 (VRF); E2 E-6: diversification and liquidity have no budget line in E1 (INT) | Checklist of every IPS-guide and case "should" item, ticked against the draft with the sentence number that covers it | IPS lead writer | Fri Oct 30 AEDT |
| 15 | PM-12 | The IPS left decision rules open, so the Final Report had to choose parameters after the freeze and looked like a redesign | IPS | M | Major | "Your team may not revise its investment strategy after the submission deadline" (IPS guide L73-74, VRF); "you may not redesign your strategy after observing the results" (Guide p.5, VRF); open choices in E1 C1-C12, E2 5, T2 finding 5 | Fix every parameter in section 4 below by vote, in the log, before the first full draft | team leader (vote); IPS lead writer | Mon Oct 26 AEDT |
| 16 | PM-13 | A deadline was missed: the team planned to submit on Saturday morning, then an upload failed; or the only person with the SMApply login was unavailable; or someone read "5 p.m." as Australian time for the lock | TN + IPS | L | Fatal | Deadlines 5:00 p.m. ET, "We will not grant any deadline extensions" (SMApply, VRF). In Sydney: roster Sat Oct 10 08:00, TN Sat Oct 24 08:00, IPS Sat Nov 7 09:00 AEDT (one hour later because U.S. clocks change on Nov 1); Brisbane an hour earlier, Perth three hours earlier (E5 script [1], DER). Last U.S. session before the lock opens 01:30 and closes 08:00 Sat Nov 7 AEDT (script [2]) | Internal submission two days early (Thu evening AEDT); never plan to use Saturday morning; confirm who can submit in SMApply and that a second student can reach that person; keep the submitted PDF and a screenshot of the confirmation | team leader | TN Thu Oct 22; IPS Thu Nov 5 AEDT |
| 17 | PM-18 | IPS title page mismatch: team name not exactly as on the roster; names not "First Name, Last Initial" or not as on the roster; the team name given instead of the WInS username | IPS | L | Fatal | IPS guide L84-100 (VRF); "Your team username is NOT the same as your team name"; the username cannot be changed (SMApply FAQ and User Guide, VP via A4) | Copy the team name and six names from the submitted roster (screenshot at submission) and the username from the WInS login screen, character for character; two students check the final PDF | admin liaison + format checker | capture Wed Oct 7; check Wed Nov 4 AEDT |
| 18 | PM-17 | A wrong, stale or mislabelled number: 10y 4.22%, Taiwan CPI 2.4%, a $295k ladder, $500k WInS cash, "6,000 teams competed", "the rule picks 50% under both forecasts" (true only with a fee of 0.5% or more), the withdrawn $101k/$165k barbell figure, "111%" without "face value", "1 in 4" for the real ladder (about 1 in 3), a model ladder price shown as a quote, a "tested" figure computed with `official_curve_pv.py` (fixed to Sept 25) or distorted by a fund distribution | TN + IPS | MH | Moderate (Major if in a permanent note) | Brief s10 inconsistencies; T2 findings 2, 19; E2 E-1; AY2 D7 C5; D7 M011; ticket header (VRF) | Every number carries its date and kind (price, history, assumption) and comes from a primary source or a re-run script on the day; "tested" numbers from `A2_curve_recheck.py` or `D9_numbers.py` [3], with IEF/TLH ex-dividend dates checked; the list above pinned as "never use"; read the latest audit corrections before using any research number | rates analyst + second reader | each note; TN numbers Oct 21-22; the IPS's one number re-dated in the week of Nov 2 |
| 19 | PM-22 | The frozen Nov 6 book did not reflect the IPS: a tidy-up trade in the last days, a split change never traded, a drift outside the band, a final order that never filled | IPS | LM | Major | IPS guide L75 (VRF); ticket s8 "never tidy up in the last days"; orders after the close do not execute (A4 item 7, INT) | No discretionary trade after the words freeze; holdings compared with the IPS sentence about WInS on Nov 4; any rule-driven trade done by Fri Oct 30 ET | trader + IPS lead writer | freeze Tue Nov 3; check Wed Nov 4 AEDT |
| 20 | PM-23 | The SMApply submission forms had fields or format rules the team first saw on the deadline night | TN + IPS | LM | Major | "All deliverables must be submitted via your team's SurveyMonkey Apply account" (VRF); the TN form's contents are not in the repo (A4 b4: logged-in pages unread) | Open the TN and IPS forms in SMApply; record fields, file types, limits and who can submit | team leader | Mon Oct 12 AEDT |
| 21 | PM-20 | Trading-note mechanics: a note cut off by an unseen limit, a typo, a note on the wrong order, a second "added" note to finish a sentence, curly quotes changing the "exact" text | TN | M | Moderate | 300-character cap on a sister product (VP for that product, UNVERIFIED for WInS); Wharton's example is 413 characters (VRF count); added notes carry a later time stamp (Stock-Trak 2017, VP) | Zero-risk note-box test before the first real note (type about 450 characters on the review screen, do not confirm); draft to 300 characters until tested; paste plain text; check the saved note against the draft; ask Wharton whether an added note counts | trader + note writer | Thu Oct 1 AEST |
| 22 | PM-21 | Reflections weak or non-compliant: over 100 words by Wharton's count; the three official questions not all answered; six jobs in 100 words; a "tested" window chosen after the fact; a trade staged to show "refined" | TN | M | Moderate | TN L46-52 (VRF); AY2 D7 C2 (pre-registered window); E2 3.2 point 5 and F9; R-W28 bans fabricated analyses (VP; staging reading is INT) | ≤95 words by two counters; each reflection answers the three questions plus one extra job; WInS screenshots on the fill date and at the Oct 20 close (Wed Oct 21 07:00 AEDT); report small moves as they are; "refined" only if it really happened; the true "growth-first tested and dropped" history in one reflection if told truthfully (E2 F8) | note writers + log keeper | screenshots on the fill day and Oct 21; drafts Oct 21; final Oct 22 AEDT |
| 23 | PM-19 | Roster missed or wrong; members lock and names must match the IPS | IPS | VL | Fatal | Roster due Oct 9 5:00 p.m. ET; unique email per student; "Once your official team roster is submitted, teams may not change their members" (SMApply, VRF) | Each student confirms name spelling and email; submit early; screenshot the confirmation; full names, emails and birthdays never stored in the repo (CLAUDE.md, VRF) | admin liaison | Wed Oct 7 AEDT (deadline Sat Oct 10 08:00 AEDT) |
| 24 | PM-26 | Someone on the team contacted Laura (a message, a comment on her posts, a question at an event, an email to her publisher about the case) | all | VL | Fatal (disqualification) | "Teams may not contact the Competition client. Teams that violate this rule will be disqualified." (R-W16, VP) | Team rule announced in writing: no interaction of any kind with Laura or her representatives until the competition ends; research uses only public pages | team leader | Tue Sep 29 AEST |
| 25 | PM-27 | Paid help, or a member enrolled in a non-Wharton course that "claims to teach" the competition; a paid tutor edited a draft | all | VL | Fatal | R-W21 and R-W28 (VP) | Each student confirms no such course or paid help; paraphrase readers unpaid and restate-only | team leader | Wed Sep 30 AEST |
| 26 | PM-28 | Membership or team-leader rule breached (a member removed without approval; size outside 4-6; leader under 16 on Sep 28) | all | VL | Fatal | R-W11, R-W13, R-W17 (VP) | Keep six members; any change only with Wharton's prior approval; confirm the leader's eligibility before the roster | team leader | Wed Oct 7 AEDT |
| 27 | PM-24 | A visible case misread: buying in 2027 not reconciled with "set aside at the beginning of 2033"; WInS gains mentioned as if they count; living costs taken from the portfolio; the facility treated as a dated liability | IPS | L | Major | Case L61-63, L94-95, L104, L132-133 (VRF); Guide p.3 "not the competition scorecard" (VRF); brief s8 item 19 | One reconciling clause (bought 2027, designated the reserve on 1 Jan 2033; E1 P9); no WInS gain, loss or rank in any note, reflection or the IPS | client lead | Fri Oct 30 AEDT |
| 28 | PM-30 | The public repository exposed the work: another team copied it, a reader found AI-written specifications that matched the submission, or student data leaked | TN + IPS | L | Major | Repo public (git remote; CLAUDE.md "Repo is public; the team leader accepted putting competition materials in it", VRF); "plagiarize existing strategies" is an ethics breach (R-W28, VP) | Team leader revisits the visibility decision until after Dec 4, or records why public stays; the PM-04 copy check covers phrasing; no student personal data in the repo | team leader | Fri Oct 2 AEST |
| 29 | PM-25 | Laura misused: her quotes in the TN or IPS, the case pull quote attributed to her, an identity or Taiwan tilt, a book-title pun, a private detail, the statistics degree used as flattery | TN + IPS | LM | Moderate | Brief s16 D13 rules (VRF); D13c R1-R3, R10 (INT); E3 4c | Check every line against D13a and the brief's rules; statistics degree zero or one use (conflict K4) | client lead | every draft |
| 30 | PM-29 | The advisor made or placed a decision, or a note or the IPS said "our portfolio manager approved" (the case's fictional framing) | TN + IPS | L | Moderate | "Advisors may not make decisions on behalf of students" (R-W19, VP); "Students should place trades on WInS, NOT the advisor" (SMApply FAQ, VP); D10 M013 cut list | Advisor for admin only; no such wording in notes or the IPS; governance names who decides (E1 P10; E3-8) | team leader | now; IPS draft Oct 26 |

---

## 4. IPS: rules to fix before Nov 6 (from PM-12; the Final Report must later apply them without redesign)

Each is a vote recorded with first names, date and reason (brief s17; E1 P11; E2 section 5; E3 section 9). The content is
in the cited files; this list only makes the deadline and owner explicit. **Owner: team leader runs the vote; IPS lead
writer records the outcome in the draft. By: Mon Oct 26 AEDT, before the first full draft.**

1. **Completion rule:** buy on arrival; which payments first if money is short (longest-dated first, with its "because"
   and the first-operating-year counterpoint, E3-7); the 2028 deposit completes the ladder before any growth; one
   labelled joint-tail clause (E1 P3-P4).
2. **Growth mix:** 50/50 or 60/40, its band, a yearly reset, and a reason whose yardstick is stated (money put in, or
   the all-Treasury alternative; E2 F6; T2 finding 2 on the fee dependence).
3. **Growth money's bond half:** short Treasuries or dated to 2031/2033 (AX1 C18 via E2 R1).
4. **Floor timing:** bought in January 2028 or January 2031 (AX1 C6 via E2 R2).
5. **2031 range method:** the bought share, the share of the rest added to the gift, the top percentile, cap or no cap,
   two-sided confidence, no announcement before the ladder is complete; the parts named by what each dollar does
   (E1 P7; E3-1).
6. **2033 order of use:** the reserve is the ladder, held to maturity, designated on 1 Jan 2033; the gift; kept money in
   US$ short Treasuries; US$ binding; no NT$ conversion or hedge before the facility decision (E1 P8-P9).
7. **Governance:** what stays Laura's decision; rules change only if her circumstances change, never because markets
   moved; no rebalancing between the reserve and the growth money (E1 P10; E3-8).
8. **Cost principle:** keep or cut (conflict C2 below), decided before words are counted.
9. **The WInS sentence:** the date or state the book shows, and stand-in funds rather than the ladder (D10 1.5).

---

## 5. Master calendar of preventions (Australian Eastern time unless marked ET; internal targets are ASM team rules)

| When | What | Owner-type | Causes |
|---|---|---|---|
| Tue Sep 29 AEST | Roles assigned; one trader + backup; no-contact rule written down; AI-use log started | team leader; log keeper | PM-05, PM-14, PM-26, PM-08 |
| Wed Sep 30 AEST | Shared exam/travel calendar; own-words notes and devil's-advocate pairs for the gate votes; paid-help confirmation | team leader | PM-05, PM-01, PM-27 |
| Thu Oct 1 AEST | Gate: Session Rules screenshot (both limit lines), logged-in activity rules read, note-box test at zero risk, Bonds list, labels chosen by the team, book and split votes, note drafts copy-checked, two-reader check | trader; second reader; team leader | PM-14, PM-15, PM-20, PM-01, PM-04, PM-06 |
| Fri Oct 2 ET (opens 23:30 AEST) | Target fills; screenshot positions (start of the "tested" window) | trader; log keeper | PM-16, PM-21 |
| Fri Oct 2 AEST | Repo-visibility decision revisited and logged | team leader | PM-30 |
| Sun Oct 4 AEDT | AI-use log backfilled (council, blueprints, this run, tools) | log keeper | PM-08 |
| Mon Oct 5 AEDT | Every order "Filled" with a note; hard stop Fri Oct 9 ET | trader | PM-16 |
| Wed Oct 7 AEDT | Roster submitted; names, team name and WInS username captured for the title page | admin liaison | PM-19, PM-18, PM-28 |
| Mon Oct 12 AEDT | SMApply TN and IPS forms opened and recorded; who can submit | team leader | PM-23, PM-13 |
| Fri Oct 16 ET | Split decided if it was provisional (trade once or log "decided not to trade") | growth/risk analyst | PM-06, PM-12 |
| Wed Oct 21, 07:00 AEDT | Oct 20 close: screenshot positions (end of the "tested" window); reflections drafted | log keeper; note writers | PM-21 |
| Thu Oct 22 AEDT | TN consistency table, word counts, number check; TN submitted (deadline Sat Oct 24 08:00 AEDT) | log keeper; team leader | PM-06, PM-17, PM-21, PM-13 |
| Sat Oct 24 AEDT | IPS idea list (≤12 ideas), pitch elements, dated spine | IPS lead writer; client lead | PM-03, PM-07, PM-09 |
| Sun Oct 25 AEDT | Explain-back check, round 1 | second reader | PM-01 |
| Mon Oct 26 AEDT | Section 4 votes recorded; first full IPS draft from a blank page; first PDF test | team leader; IPS lead writer; format checker | PM-12, PM-01, PM-02 |
| Oct 26-30 | Paraphrase round 1; required-elements checklist (Fri Oct 30); case-misread check | IPS lead writer; client lead | PM-03, PM-11, PM-24 |
| Fri Oct 30 ET | Any remaining rule-driven WInS trade completed | trader | PM-22 |
| Nov 2-3 | Paraphrase round 2; the IPS's one number re-dated; explain-back round 2; words frozen Tue Nov 3 | IPS lead writer; rates analyst | PM-03, PM-17, PM-01 |
| Wed Nov 4 AEDT | Final PDF check by two students; title page against the roster; holdings against the IPS sentence | format checker; admin liaison; trader | PM-02, PM-18, PM-22 |
| Thu Nov 5 AEDT | IPS submitted (deadline Sat Nov 7 09:00 AEDT; the portfolio locks at the U.S. close, 08:00 AEDT the same morning) | team leader | PM-13 |

---

## 6. Conflicts the pre-mortem cannot settle (both sides; the team decides)

| # | Conflict | Side A | Side B | Pre-mortem reading (INT) |
|---|---|---|---|---|
| C1 | WInS book (ii) vs (iii) | (ii): three roles and a visible growth decision (E1, T1, D12, E2); lower PM-16 risk | (iii): true at a stated date, shortest IPS sentence (D10; E3 slightly toward (iii) on credibility) | (ii) carries PM-06 (contradiction) risk; (iii) carries PM-07 (timid) and PM-16 (only two decisions) risk. Neither is safer overall; each is safe only with its own prevention done before the first order |
| C2 | Cost clause in the IPS | Cut first (E1 P12; AY2): lowers PM-02 page risk | Keep and extend (E3-4): a missing cost answer reads as selling, and the 50/50 reason rests on a fee assumption | Decide before the word count; if cut, the growth-mix reason must not depend on a fee |
| C3 | Statistics degree | Once, in the certainty definition (E1 P17; D7) | Zero (E3-9; D3 audit C19) | Zero lowers PM-07 and PM-25 risk at no cost to substance |
| C4 | "Double-spaced" reading | Word's "Double" (27.6 pt) | "Exactly 24 pt" matches Wharton's sample (AY2, INT) | Fit under the stricter reading; use 24 pt only as a documented last resort (PM-02) |
| C5 | Paper size | U.S. Letter (Wharton's PDFs) | A4 (Australian default; more room; allowed by the discretion clause, INT) | Either is defensible; fitting on Letter removes the question |
| C6 | Growth split | 50/50 (E1, D2; better bad case) | 60/40 (D6, D13c; less timid) | PM-07 pushes up, PM-17 warns the "50% under both forecasts" reason needs its fee; own the choice as a choice of spread (E2 F6) |
| C7 | Semifinal basis | IPS and Final Reports only (Rules page, R-W24, VP) | All three deliverables evaluated (SMApply, VRF) | Treat all three as scored, but weight hours toward the IPS after Oct 23 (PM-05) |
| C8 | Public repository | Public, accepted by the team leader (CLAUDE.md) | Private until Dec 4 lowers PM-30 | A team-leader decision; E5 only asks that it be revisited and logged |

---

## 7. Later (after Nov 9), one line each (Final Report; not worked here)

- School documentation on letterhead: request through the advisor in October, as SMApply says "Do not wait until the
  last minute" (VRF; BS-11); submitted with the Final Report on Dec 4.
- Works Cited with the AI-use record built from the PM-08 log (R-W46).
- Final Report format rules, released Nov 9: a fresh format pre-mortem then.
- The Final Report applies the section 4 rules "as written" (no parameter chosen after Nov 6).
- Deadline: Sat Dec 5 09:00 AEDT (E5 script [1]).

---

## Sources

**Official, in the repo (VERIFIED-REPO-FILE):** `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`
(L43-45, L61-63, L69-74, L91-99, L104, L114-116, L129-133, L146-148, L161-162); `2026_WGY_Investment_Policy-FINAL.txt`
(L45-75, L82-125); `2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L11-31, L36-53); `2026_WGY_Investment_Competition_Guide.txt`
(L70, L89, L156-159, L183); `2026_WGY_Competition_Infographic.txt` (L42); `SMApply_Deliverables_Page_2026-09-27.md`
(deliverables, roster fields, criteria).

**Primary web, read by E5 on 2026-09-28 with `research/insight_v1/scripts/fetch_text.py` (VERIFIED-PRIMARY):**
- NSW Department of Education, 2026 term dates: https://education.nsw.gov.au/schooling/calendars/2026 ("Term 4: Tuesday
  13 October to Thursday 17 December"; "Spring: Monday 28 September to Friday 9 October").
- NSW Government / NESA, "2026 HSC Timetables released":
  https://www.nsw.gov.au/education-and-training/nesa/news/all/2026-hsc-timetables-released (`--grep "13 October"`
  found verbatim: "starting with English Paper 1 on Tuesday 13 October and finishing with Physics in the morning of
  Thursday 5 November").
- Found first through WebSearch (2026-09-28); the snippets were then confirmed on the pages above.

**Primary web, as carried by the cited files (VP there; not re-opened by E5):** Wharton Rules & Roles, FAQ and AI policy
(R-W11 to R-W51 via `phase_A/case_register.md` and A4); SMApply Trading Details and FAQ (via A4, D10, AX2); 2026-27 WInS
User Guide and Stock-Trak pages (via A4, D12); retired Wharton judging page and 2025 top-10 article (via D9, D7, AY2);
digital.gov paraphrase testing (via D12); Russell 2026 (via D8/AY2).

**Research files (lower authority; audit corrections applied):** `research/insight_v1/phase_E/E1_change_proposals.md`,
`E2_judge.md`, `E3_laura.md`; `wins_now/securities_and_allocation_v1.md`, `T2_red_team.md`; `phase_D/trading_now_brief.md`,
`D10_compliance.md` (+AX2), `D7_wharton_intent.md` (+AY2), `D9_communication.md` (+AY2), `D12_overflow_client.md` (+AY1),
`D13c_voice_map.md`, `audit_markets_rules.md`, `audit_judges_practice_comms.md`; `phase_A/wins_week1_guardrails.md`,
`case_register.md`, `stakeholder_map.md`; CLAUDE.md; `research/council_2026-09-27/01_chair_memo.md` (history).

**Scripts:** `research/insight_v1/scripts/E5_premortem_checks.py` (new; deadline clock via Python zoneinfo, ranking from
the ASM ratings above). Figures quoted from other scripts are as reproduced by their auditors (T2, AX2, AY1, AY2, E2,
E3).

---

## What this teaches

1. **Most projects fail at the joints, not in the engine.** The strategy survived every audit; the likely failures are
   in who owns it, how densely it is written, whether two documents tell the same story, and whether a PDF has three
   pages. A pre-mortem looks at the joints on purpose.
2. **Rank by likelihood times impact, then do the cheap fatal ones anyway.** A missed deadline or a fourth page is
   unlikely, but it ends everything and costs an hour to prevent. Low-probability, high-cost risks with cheap fixes are
   the best deals in risk management, in markets as well as in competitions.
3. **Every risk needs an owner and a date.** "The team should check the PDF" means nobody will. A named role and a day
   turn a worry into a task.
4. **Watch for tripwires, not just outcomes.** You cannot see a lost semifinal place until January, and Wharton gives no
   feedback. You can see today whether anyone can explain the 2031 rule without notes, or whether a draft is 510 words.
   Early signs are the only feedback you will get.
5. **Honesty about how you worked is part of the work.** An AI-use record written as you go costs minutes; one
   reconstructed later, against a public record anyone can read, costs credibility. That is the same lesson the case
   teaches about Laura's 2031 promise: say only what you can stand behind.
