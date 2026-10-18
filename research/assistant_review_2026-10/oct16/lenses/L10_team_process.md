# L10 - Team, process and human factors (Team Caplet)

Prepared Fri 16 Oct 2026 (Sydney) by an AI reviewer. This is knowledge for the team, not submission text. Log it in the
AI-use record. Nothing here judges or ranks any student. First names appear only where a team document already uses
them. Every claim cites a repo file and line, or a web page accessed 16 Oct 2026. "caplet-latest/" means the copy of
branch claude/fervent-edison-sqk1ry (commit 412e9e3, 16 Oct 01:24 UTC, not merged).

Lens: an experienced competition coach looking at the people side. Do the six students own the plan? Who does what?
Will the calendar hold? What did last year teach? What does "Articulation of Competition Experience" need?

---

## 0. Bottom line

1. **The plan is strong on paper but not yet owned by six people.** Key calls were "deferred to the assistant"
   (CLAUDE.md:75); "The team has not read the memos yet" (CLAUDE.md:74); the team's own doc says "The idea came from our
   AI council run on 27 September" (notes_and_discussions.md:69). The strategy can still change until the 6 Nov freeze,
   so there is still time to make it truly the team's.
2. **The semifinal will test exactly this.** Last year every member had to speak "and briefly explain how they
   contributed value to the team", no new strategy was allowed, and the written answers had to be in an "authentic team
   voice, not generated or generic responses". The video was due 13 days after the Top 50 was announced, in the
   Australian summer holidays. Roles that exist only on paper will show.
3. **One person carries almost everything**: leader, only trader, only student committer (98 of 98 student commits on
   main), the Mac that runs all 10 routines, the only person alerted, and the submitter. The leader cannot be replaced
   without Wharton approval.
4. **The 16 Oct commit makes the human problems worse, not better.** One day after a brief whose first action was
   "Agree that students write every word that is submitted", the leader alone changed the team rule so the AI may edit
   all three deliverables as "[AI]" suggestions (caplet-latest/CLAUDE.md:27-30). No team vote is recorded. START_HERE.md
   still says "The team writes all deliverables", so the onboarding page and the AI's rulebook now disagree.
5. **Nobody owns the numbers.** Two AI pipelines gave the ladder cost on the same 15 Oct curve as $294,453 and $298,624.
   Both are correct for different questions (Section 4, TP-10). The $294k figure is now in the AI's "Current status".
   A student "rates analyst" who owns one dated basis is the fix.
6. **The calendar is tighter than it looks.** All trading happened in the Knox holidays. Term 4 began Tue 13 Oct. The
   TNA falls at the end of Term 4 week 2, the IPS at the end of week 4, and the Final Report two days after Knox's last
   day of term (Thu 3 Dec). HSC written exams run 13 Oct to 5 Nov (whether any member sits them: UNVERIFIED).
7. **Too much advice, too few meetings.** About 745,000 words of AI research sit in the repo (about 50 hours of reading
   each). The 28 Sep pre-mortem predicted this exact process failure and its fixes were not done. Eight short meetings,
   real roles and an evidence ledger will help more than another report.

---

## 1. Summary table

| ID | Finding | Severity | New / known |
|---|---|---|---|
| TP-01 | Key strategy calls were deferred to AI; the six have not yet argued them through | critical | known-deeper |
| TP-02 | Articulation needs a real record; the journal is thin; last year's comments said "make up stories" | critical | known-deeper |
| TP-03 | Semifinal format (last year): each member speaks and explains their contribution; no new strategy; video due ~13 days after the announcement | high | new |
| TP-04 | Single point of failure: leader = trader = repo = routines = alerts = submitter | high | known-deeper |
| TP-05 | Roles still blank on 16 Oct; the pre-mortem's tripwires have fired | high | known-deeper |
| TP-06 | School calendar: deadlines land in Term 4 weeks 2 and 4 and the day after term ends; HSC window overlaps | high | new |
| TP-07 | At least eight open team decisions, no meeting booked; "settled" decisions do not spread | high | new |
| TP-08 | Decision rights: team-wide rules changed by one person in the AI's memory file, reversing the 15 Oct advice within a day | high | new |
| TP-09 | The team's rule documents now contradict each other on who writes the deliverables | high | new |
| TP-10 | Nobody owns the numbers: $294k vs $298k on the same curve; the reason and which to use | high | new |
| TP-11 | Advice overload: AI output far exceeds reading time; advice is not turning into action | high | new |
| TP-12 | Information reaches one person; the other five see snapshots | medium | new |
| TP-13 | Darren's challenge and "too timid" were answered by an "AI recommendation"; the team vote was never logged | high | known-deeper |
| TP-14 | The written "lessons from last year" leave out every process lesson | high | known-deeper |
| TP-15 | The team's idea of "what judges want" does not match its own strategy | medium | new |
| TP-16 | 24 project techniques listed; PM Dashboard is 0 bytes; Trade Log rows empty | medium | new |
| TP-17 | The decision story is murky but salvageable, and better than the team thinks | medium | new |
| TP-18 | Real, specific experience material exists and is not being captured | medium | new |
| TP-19 | The self-scoresheet drops two of three parts of the Articulation criterion; the AI judges inherit the gap | medium | new |
| TP-20 | Advisor: school letter before term ends, a possible advisor reflection, one advisor may serve 21 students | medium | known-deeper |
| TP-21 | Outside readers: last year an outside reviewer steered the story on deadline eve | medium | known-deeper |
| TP-22 | The school's information pack has the wrong portfolio size and leaves out the TNA | low | new |

---

## 2. Official text that matters for this lens (quoted exactly)

- **Articulation criterion:** "Articulation of Competition Experience: Demonstrates teamwork, communication, and
  learning; clearly explains the team's research and decision-making process; and reflects meaningfully on the team's
  growth and response to challenges." (competition/official/2026_27/smapply_public_2026-10-14/deliverables.txt:58)
- **Voice:** "Presents a compelling, well-organized narrative in an authentic team voice" (deliverables.txt:59).
- **Roles and trades (FAQ):** "Students should place trades on WInS, NOT the advisor. A key component of the
  Investment Competition is teamwork and communication. It should be a team decision. We strongly encourage teams to
  identify different roles for each team member." (smapply_public_2026-10-14/faqs.txt:34)
- **How teams win (FAQ):** "Strong teams understand the client, work effectively together, conduct thoughtful research
  and analysis ..." (faqs.txt:83)
- **Semifinal (FAQ, this year):** "a short presentation (via video conference for the Semifinals ...) about your team's
  strategy, analysis and experience over the past 10 weeks to a live panel of judges. All team members must
  participate." (faqs.txt:89)
- **Rules & Roles page** (https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/,
  accessed 16 Oct 2026; saved text lenses/L10/rules_roles.txt):
  - Leader: "Team leaders may not be changed after the Competition begins on September 28, 2026 unless the Advisor
    submits a written request due to extenuating circumstances and receives approval" (line 367). The leader is
    responsible for "receiving Competition communications and notifications; submitting team deliverables through
    SurveyMonkey Apply" (line 391).
  - "All team members are responsible for: Developing and implementing the team's investment strategy; conducting
    research and analysis; collaborating with teammates and placing trades through the team's shared WInS account; and
    remaining actively engaged throughout the Competition and meeting all deadlines." (line 393)
  - Advisors "may not make decisions on behalf of students or actively participate in team activities, trading
    decisions, or strategy development" (line 411); duties include "Monitoring team engagement and portfolio activity"
    (line 421) and "Serving as a sounding board without completing work on behalf of students" (line 423). "An Advisor
    may oversee a maximum of five teams" (line 425).
  - Secondary advisers allowed, but "the use of paid advisors, education consultants, or other agents is prohibited"
    (line 427).
  - AI: "Beware that use may also stifle your own independent thinking and creativity. You may not submit any work
    generated by an AI program as your own." (line 551)
  - Ethics: "We trust that you will not lie about your investment decisions and outcomes, fabricate analyses, invent
    teamwork and experiential stories, compensate advisors ... or plagiarize existing strategies." (line 557)
  - "a student's work must be their own, and not be plagiarized from any other source, including advisors or
    'unofficial' advisors" (line 559).
  - Recording: "Video recording, audio recording, photography, screenshots, or posting presentations or participants
    online during the Semifinals or Global Finale is strictly prohibited." (line 497)
- **Last year's semifinal instructions** ("2025-2026 Semifinalists - Next Steps",
  https://globalyouth.wharton.upenn.edu/wp-content/uploads/2026/01/25%E2%80%9326-Semifinalists-%E2%80%93-Next-Steps-FINAL.pdf,
  accessed 16 Oct 2026; text at research/R4_pages/wg_2025_26_semifinalists_next_steps.txt):
  - "Every team member must have a speaking role and briefly explain how they contributed value to the team." (lines 40-41)
  - "Do NOT introduce completely new material, or your team will be disqualified." "Teams are not permitted to present
    a partially or entirely new strategy." (lines 47-51)
  - "Practice your presentation with someone who has no prior investing knowledge." (line 70)
  - "Your video is due no later than 8:00 a.m. ET on Monday, February 9." (line 90); four written answers of 250 words
    or fewer, due 23 Feb (lines 99-103): "We are looking for your authentic team voice, not generated or generic
    responses." (line 106)

---

## 3. The real calendar (Sydney time)

Sources: Knox 2026/2027 term dates (https://www.knox.nsw.edu.au/about/public-information/term-dates, accessed
16 Oct 2026; saved lenses/L10/knox_terms.txt:416-452); NSW public schools 2026
(https://education.nsw.gov.au/schooling/calendars/2026, accessed 16 Oct 2026: spring holidays "Monday 28 September to
Friday 9 October", Term 4 "Tuesday 13 October to Thursday 17 December"); NESA: "123 written HSC exams will run over an
18-day window, starting with English Paper 1 on Tuesday 13 October and finishing with Physics in the morning of
Thursday 5 November" (https://www.nsw.gov.au/education-and-training/nesa/news/all/2026-hsc-timetables-released,
accessed 16 Oct 2026; lenses/L10/a0074582.txt:113). Deadlines: COMPETITION.md:15-24. The six students' year levels are
not in the repo (removed for privacy), so whether the HSC applies is UNVERIFIED. Knox's internal Term 4 assessment dates
are not public (UNVERIFIED); Year 11 end-of-year exams in Term 4 are common in NSW schools (general, not Knox-specific).

| Knox week (Term 4 2026) | Dates | Competition event | School pressure |
|---|---|---|---|
| holidays | Sat 26 Sep - Mon 12 Oct | Trading opened 28 Sep; all 11 orders filled 6-8 Oct; roster due Sat 10 Oct 08:00 | Knox Term 3 ended Fri 25 Sep; staff day Mon 12 Oct |
| week 1 | Tue 13 - Fri 16 Oct | (today) | HSC written exams start Tue 13 Oct |
| week 2 | Mon 19 - Fri 23 Oct | **TNA due Sat 24 Oct 08:00** | HSC exams continue |
| week 3 | 26 - 30 Oct | IPS drafting | HSC exams continue |
| week 4 | Mon 2 - Fri 6 Nov | US clocks change Sun 1 Nov; **WInS freezes Sat 7 Nov 08:00; IPS due Sat 7 Nov 09:00** | HSC exams end Thu 5 Nov (morning) |
| week 5 | 9 - 13 Nov | Final Report instructions Mon 9 Nov ET (about Tue 10 Nov Sydney) | |
| weeks 6-7 | 16 - 27 Nov | Final Report drafting | end-of-year assessments common (general; UNVERIFIED for Knox) |
| week 8 | Mon 30 Nov - Thu 3 Dec | Thu 3 Dec = Knox "Presentation Day and Term 4 Concludes"; Fri 4 Dec staff day | school letter must be signed before staff leave |
| summer | from Fri 4 Dec | **Final Report + school letter due Sat 5 Dec 09:00** | holidays, travel |
| summer | late Jan 2027 | Last year the Top 50 was announced 27 Jan 2026 (Wharton news, below); this year TBD | Knox 2027 Term 1 starts Fri 29 Jan 2027 |
| Term 1 2027 | Feb - Mar | Last year: video due Mon 9 Feb 8:00 ET (= Tue 10 Feb 00:00 Sydney), written answers due 23 Feb, results week of 9 Mar | |
| | 29-30 Apr 2027 | Global Finale, Philadelphia ("April 29 & 30", Wharton competition page; lenses/L10/ic_main.txt:370) | Knox Term 1 2027 ends Fri 9 Apr |

Wharton news (https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/,
dated 27 Jan 2026, accessed 16 Oct 2026; lenses/L10/top50_2026.txt:354, :466): "On December 12, some 2,300 teams from
79 countries submitted final reports"; semifinalists "compete in the semifinals over the next several weeks and meet
virtually the week of March 9".

Derived timing facts: until Sun 1 Nov, US markets open 00:30 and close 07:00 Sydney; after it, 01:30 and 08:00. Every
Wharton deadline lands on a **Saturday morning** in Sydney, so Friday night is the real last working window and the
leader must be reachable on Saturday morning.

---

## 4. Findings

### TP-01 - Key strategy calls were deferred to AI; the six have not yet argued them through (critical, known-deeper)

**What is wrong.**
- "Interview part 2 (2026-09-27): the team deferred to the assistant's evidence-based calls, provisionally" (CLAUDE.md:75).
- "NOT YET DECIDED BY THE TEAM. The team has not read the memos yet." (CLAUDE.md:74)
- "The assistant has freedom to make decisions and choose its workflow" (CLAUDE.md:32-33).
- The team's strategy tab: "The idea came from our AI council run on 27 September." (notes_and_discussions.md:69);
  "During the run you narrowed the scope" (:91, an AI talking to one student); a tab titled with a pasted AI reply,
  "I'll go through the phase files on the branch and..." with the heading "Most Impressive Points from Claude" (:131-139).
- Student-written lines in that doc are short questions: "Is it implying that there are not many stocks in the
  portfolio?" (:238), "Income sources cancel out the stock?" (:239), "Barbell strategy (generic?)" (:254). Good
  questions, but they show the plan is still being absorbed, not owned.
- IPS V5 carries the comment "Best version that AI generated; We cannot submit as it is" (ips_report/01_version_5.md:36).

**Why it costs us.** Two scored phrases need ownership: "authentic team voice" and "clearly explains the team's research
and decision-making process". A team that did not make the decisions cannot honestly explain how it made them. At the
semifinal, the strategy cannot change (TP-03), so the frozen 6 Nov plan must be one all six can defend. Wharton warns AI
"may also stifle your own independent thinking" (Rules & Roles:551).

**Fix (what it must achieve).** Two "ratification" meetings before 6 Nov (M1, M2 in Section 6). For each core decision
(buy the ten payments first; iBond/T-bond ladder; floor size; 2031 range rule; stock share; hold in WInS): one student
explains it in 60 seconds with no notes; a second argues the best alternative; the team votes; the historian logs vote,
reasons and dissent in students' words. Test of success: every IPS decision has a student owner who can name the option
the team rejected and why. A decision that fails the test is learned properly or changed before 6 Nov.

---

### TP-02 - Articulation needs a real record; the journal is thin; last year's comments said "make up stories" (critical, known-deeper)

**What is wrong.**
- This year's experience journal (Final Report doc, exported 14 Oct) has 10 dated entries and stops at 7 Oct.
  "[who argued what]" (final_report.md:16) and "Outcome and reasons: [fill in]" (:23) are still blank. Missing: the
  6 Oct email, the 7 Oct mis-click, the 13 Oct V5 decision, everything since.
- No meeting minutes exist in any export. The PM Dashboard export is 0 bytes (sheets/pm_dashboard/sheet1.csv) and the
  Trade Log tab has headers and empty rows only (sheets/portfolio_and_trading_notes/trade_log.csv).
- **Last year:** the "LOGS", "Recording Summary" and "Meeting Minutes" tabs were empty (2025_knox_wharton.md:3393-3412).
  Comments dated 11 Dec 2025, the day before the 12 Dec deadline, say "Make up stories, and make them sound realistic"
  (:3827), "that's how our make-up story goes, include challenges, problems, debates, leadership, dilemma" (:3844), and
  a 12 Dec comment says "added more details about the conflict to show the challenges faced in our journey" (:3898).
  Whether the submitted scenes were real is UNVERIFIED; the instructions to invent them are on the record.
- Four of this year's six were on last year's team (2025_knox_wharton.md:76).

**Why it costs us.** Wharton's Ethics text names this exact act: teams will not "invent teamwork and experiential
stories" (Rules & Roles:557), and Wharton may use "forensic analysts" (:561). The same deadline squeeze is coming (25
days from 9 Nov to 4 Dec, ending the day after term ends). Without a record the team writes something generic (low score)
or reconstructs from memory (errors).

**Fix.** Rule: **no artefact, no story.** Every experience claim in the Final Report points to something that existed at
the time: a WInS timestamp, Doc version or comment, chat message, meeting note, screenshot (kept on the private Drive).
The historian keeps the ledger (Section 9), 10 minutes after each meeting, and back-fills 27 Sep to 16 Oct from Doc
version history and chat logs by Sun 25 Oct. Real disagreements and mistakes (TP-18) are worth more than invented ones.

---

### TP-03 - The semifinal tests ownership directly; last year it came 13 days after the announcement (high, new)

**What is wrong.**
- Last year's semifinal: a 10-minute video; "Every team member must have a speaking role and briefly explain how they
  contributed value to the team"; it had to "Build upon information and insights presented in your midterm and final
  competition reports" and "Teams are not permitted to present a partially or entirely new strategy"; then four
  written answers in an "authentic team voice, not generated or generic responses" (Next Steps PDF lines 40-51, 99-106).
- This year's FAQ says "a live panel of judges" (faqs.txt:89). The exact 2027 format is UNVERIFIED. Either way, every
  member presents and the strategy is fixed.
- Timing: last year's Top 50 was announced 27 Jan 2026 and the video was due 9 Feb, 13 days later. If this year is
  similar (UNVERIFIED), the announcement lands in the Australian summer holidays, just before Knox Term 1 2027 starts
  (Fri 29 Jan 2027).
- Today, five of the six have no recorded role (TP-05) and no visible hands-on part in trades, numbers or repo (TP-04).

**Why it costs us.** "Explain how you contributed value" cannot be answered well by a student whose role was nominal.
And the written answers would be written under time pressure, exactly where AI temptation is strongest.

**Fix (what it must achieve).**
- Each student's role (Section 7) must produce something they can point to on video: a section, a number sheet, a
  check, a decision record.
- Rehearse "what was your job and what did you learn" now, in the 60-second test (Section 8, Q14).
- At M8 (after 4 Dec) collect every student's availability for late Jan to Mar 2027 and agree how the team will
  meet in the holidays.
- Practise explaining the plan to a non-investor (last year's own advice, line 70). This also improves the written work
  now, because saying it out loud exposes weak logic.

---

### TP-04 - Single point of failure: leader = trader = repo = routines = alerts = submitter (high, known-deeper)

**What is wrong.**
- "Only Ray places/cancels WInS orders" (CLAUDE.md:14; COMPETITION.md:193; START_HERE.md:28).
- `git log` on main (16 Oct 2026): 98 commits by Ray, 45 by "Claude", none by any other student. To push, "Ray needs to
  add your GitHub username as a collaborator" (START_HERE.md:42-43).
- The 10 scheduled routines "run on Ray's Mac" (ops/README.md:3); the task files point to `/Users/ray/...`
  (ops/routines/scheduled_tasks/caplet-judge-tna.md:6); the watcher "send[s] Ray a push notification"
  (ops/routines/WATCHER.md:21); "Ray places all trades himself" (ops/routines/MONITOR.md:6).
- The leader receives Wharton communications and submits (Rules & Roles:391) and cannot be changed without approval
  (:367). Whether another student can log into SMApply is UNVERIFIED.
- Yet the rules make **every** member responsible for "placing trades through the team's shared WInS account"
  (Rules & Roles:393), and the FAQ says "It should be a team decision" (faqs.txt:34).

**Why it costs us.** Illness, an exam, a flat laptop or a missed alarm on a Saturday morning can sink a deadline with "no
extensions" (COMPETITION.md:12). It also weakens the teamwork story and the semifinal "contributed value" answers.

**Fix.** Keep one person on the WInS keyboard for safety (the 7 Oct incident was real), but make each trade a logged
team decision with a second student reading the ticket back. Name a **deputy** who holds copies of all final files and
the submission checklist and is on call at each deadline. **Submit 36-48 hours early** (Thursday evening Sydney). Send
alerts and digests to the team chat, not one phone. Check now whether a second student can see the SMApply forms; if not,
the deputy watches each submission live on a call.

---

### TP-05 - Roles are still blank on 16 Oct; the pre-mortem's tripwires have fired (high, known-deeper)

**What is wrong.**
- The Team List "Roles" column is empty for all six (team_list.md:30-45).
- The newest branch still says "(4) no roles assigned yet" and keeps "Team: assign roles" open
  (caplet-latest/CLAUDE.md:83, :153).
- The school's own pack told teams to have "Agreement on team responsibilities and availability during
  September–December" before registering (team_list.md:129).
- The 28 Sep pre-mortem (research/insight_v1/phase_E/E5_premortem.md:85) set roles "Tue Sep 29" and a calendar "Wed Sep
  30". Its imagined failure reads like a diary of what then happened: "The gate meeting slipped during the school
  holidays; the first fills came in week 2 ... one student wrote every note at 1 a.m." (:271-273). Compare the journal:
  fills 6-8 Oct, and "Oct7: Eric fall in sleep because our time is freaking 12:30 AM that the market would open"
  (final_report.md:27). Its tripwires (:290-291): "A week with no logged meeting" (no minutes exist: fired); "One
  student's name on more than half the log entries" (git history: fired). The next one is "No full IPS draft
  circulated by Mon Oct 26".

**Why it costs us.** Wharton "strongly encourage[s]" roles (faqs.txt:34); the Final Report must describe teamwork
truthfully; every member must speak about their contribution at the semifinal (TP-03).

**Fix.** Assign roles at M1 (Sun 18 Oct) from Section 7. Every student owns one TNA reflection or IPS section, one Final
Report section, and one "60-second" topic. Keep the role table on the private Drive, not the public repo.

---

### TP-06 - The school calendar: deadlines in Term 4 weeks 2 and 4, and two days after term ends (high, new)

**What is wrong.** See Section 3.
- The best working time (Knox holidays, 26 Sep to 12 Oct) is over. Trading, the notes and most research happened then.
- The TNA (Sat 24 Oct) ends week 2; the IPS (Sat 7 Nov) ends week 4, in the same week US clocks change.
- The Final Report is due Sat 5 Dec, two days after Knox's last day of term (Thu 3 Dec) and the morning after a staff
  day. The school letter needs a signature from "a school administrator" on letterhead (COMPETITION.md:129-131) and was
  "not yet requested as of 13 Oct" (COMPETITION.md:132).
- HSC written exams (13 Oct to 5 Nov) cover both the TNA and IPS weeks. UNVERIFIED whether any member sits them; if one
  does, that student is in exams right now.
- After 1 Nov, US markets open 01:30 Sydney. The cost of night trading is already in the journal (final_report.md:27).

**Fix.** At M1, each student enters exams, assessments, sport/music and travel into one shared calendar for 18 Oct to
5 Dec and for late Jan to Mar 2027. Internal deadlines are two days early (Section 6). No one gets a writing task in an
exam week. Ask the advisor to request the school letter now, aiming to have it by Fri 20 Nov. No trades after 1 Nov
unless forced; if forced, set the limit order in Sydney daylight to fill at the next open, never one tired person at
1:30 am.

---

### TP-07 - At least eight open team decisions, no meeting booked, and "settled" decisions do not spread (high, new)

**What is wrong.** Open decisions found in the repo and prior briefs:
1. Which three notes for the TNA ("Our suggested picks (team decides)", COMPETITION.md:110).
2. Vote set A (15 Oct brief item 11: name, floor wording, "rounded down", shortfall order, ladder-cost basis, the
   October rule).
3. Vote set B (15 Oct brief item 19: floor size, where spare cash waits, certainty standard, review triggers).
4. The new "TEAM DECISION before 6 Nov: state the risk / keep Laura's half to 2042 / hold a buffer from the 2028
   deposit" on the coupon-reinvestment shortfall (caplet-latest/CLAUDE.md:15-16).
5. Darren's 5 Oct challenge: "Outcome and reasons: [fill in]" (final_report.md:23).
6. The "Team vote needed (D2/D6)" on the floor size after the "timid" test (notes_and_discussions.md:303).
7. The AI rule for deliverables, changed 16 Oct (TP-08).
8. The three insight_v1 "gate votes", still unticked (CLAUDE.md:165-166).

Decisions that were "made" do not reach the records. The journal says on 1 Oct: "Strategy name settled as
Root-and-Branch (earlier 'Roots First')" (final_report.md:21). Two weeks later the "single source of truth" heads its
strategy section "Our strategy ("Roots First")" (COMPETITION.md:147) and asks to "Make the Messy Roots -> 'Roots First'
link visible" (COMPETITION.md:204), while the 16 Oct number sheet says "Root-and-Branch"
(caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md:5).

**Why it costs us.** Undecided items get decided by default, by whoever edits last or by the AI. That is the opposite of
"clearly explains the team's research and decision-making process". The TNA reflections (due in 8 days) may describe a
plan the team later changes.

**Fix.** Items 1, 2, 5, 7 at M1 (Sun 18 Oct); 3, 4, 6, 8 at M2 (Sun 25 Oct). Each gets a half-page options note
written by its owning student (options, numbers from the rates analyst, recommendation, strongest objection). Five
decisions at most per meeting. After each vote, the historian updates one "decisions register" on the Drive, and the
rules lead updates COMPETITION.md and the AI's memory file to match (same day).

---

### TP-08 - Team-wide rules are changed by one person in the AI's memory file (high, new)

**What is wrong.**
- "Deliverable edits (Ray, 2026-10-16; replaces the old 'do not write the deliverables' rule): the assistant may edit
  the IPS, Trading Notes and Final Report, but only as Google Docs SUGGESTIONS ... each labelled '[AI]'"
  (caplet-latest/CLAUDE.md:27-30). The same commit deleted "Assistant outputs are for inspiration and research; the
  team does not submit them as they are" and "not submission-ready prose" from the mandate (diff of CLAUDE.md:35-37
  against caplet-latest/CLAUDE.md:39-40), and changed COMPETITION.md to "Since 16 Oct (Ray's decision)"
  (caplet-latest/COMPETITION.md:142).
- This came about 24 hours after the 15 Oct brief's item 1: "Agree that students write every word that is submitted ...
  Do not edit or 'humanise' them. Whole team" (scratchpad oct14/final.md:33). The same commit added 13 AI rewrites of
  IPS V5 sentences (caplet-latest/research/ips_numbers_2026-10/IPS_v5_suggestions.md).
- Earlier one-person rules: "Mandate (Ray, 2026-09-27)" (CLAUDE.md:32); "Only Ray places/cancels WInS orders"
  (CLAUDE.md:14). No record shows a team vote on any of them.

**Why it costs us.** An integrity problem lands on the whole team, not one person ("grounds for dismissal", Rules &
Roles:559). Five students carry the risk of a rule they may not know about. (The integrity side is L09 INT-01; this
finding is about who decides.) It is also a weak teamwork story, and it pulls the AI further into the centre just as the
semifinal will ask each student what they did.

**Fix.** A one-page team charter, agreed at M1 and kept on the private Drive:
- whole-team vote, logged: strategy, any trade, the AI-use rule, what gets submitted, the name;
- section owner decides: wording inside their own section;
- leader decides: submission timing inside the agreed window.
The AI's memory file then only records what the team decided, with date and vote count. The M1 vote on the AI rule
should be taken with all six present and the Wharton AI text (Rules & Roles:551) read aloud first.

---

### TP-09 - The team's own rule documents now contradict each other (high, new)

**What is wrong.** On the 16 Oct branch:
- START_HERE.md (the onboarding page for teammates) is unchanged: "**The team writes all deliverables** (TNA, IPS,
  Final Report). AI output here is research and checking only" (caplet-latest/START_HERE.md:26).
- CLAUDE.md and COMPETITION.md say the AI may now edit all three deliverables as "[AI]" suggestions
  (caplet-latest/CLAUDE.md:27-30; caplet-latest/COMPETITION.md:142-144).
- Old AI-use rows still say "Exemplar only; team writes its own IPS" (caplet-latest/docs/AI_USE.md:65).

**Why it costs us.** A student who follows START_HERE believes no AI wording reaches the deliverables; the AI follows
CLAUDE.md and suggests wording. When the Works Cited is written on 4 Dec, the team will not agree on what happened. That
is how honest teams end up with dishonest disclosures.

**Fix.** One rule, in one place, chosen by team vote (TP-08), copied word for word into START_HERE, COMPETITION and
CLAUDE.md the same day. Whatever the rule is, the AI-use log must record every AI suggestion and whether it was accepted,
so the Works Cited can be exact.

---

### TP-10 - Nobody owns the numbers: $294k vs $298k on the same curve (high, new)

**What is wrong.** On 16 Oct two AI pipelines gave the cost on 1 Jan 2027 of the ten $50k payments, both on the 15 Oct
official curve (competition/official_market_data/daily-treasury-rates_2026-10.csv, 15 Oct row: 5y 4.91, 7y 5.00,
10y 5.10, 20y 5.48):
- **$294,453, headroom $5,547** (results.json `ladder_cost_bootstrap_headline`, 2026-10-15; quoted as "about $294,000"
  and "about $5,500" in caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md:13-14, and now in the AI's
  "Current status", caplet-latest/CLAUDE.md:13-14).
- **$298,624, headroom $1,376 (4.7bp)** (lenses/L08_coherence_numbers.md:33; L08/series_live.csv row 34).

**The reason (recomputed; script lenses/L10/calc/basis.py).** Same curve, different question:
- The number sheet discounts each $50k to its **payment date (1 Jan 2033 ... 1 Jan 2042)**, as if a zero-coupon bond
  matured exactly then. Its code says so: "the verified 27-Sep method (bootstrapped zero curve, forward value at 1 Jan
  2027)" (caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:70-71) and "zero-coupon view, as in the IPS's
  $292k" (:99). I reproduced **$294,453** exactly.
- The WInS holdings mature **before** the payment dates: IBTM-IBTR in mid-December, and the T-bonds in Feb 2037,
  May 2038 and November 2039-41 for the 2038-42 payments (COMPETITION.md:176-185). That is 2 weeks to 10.5 months early.
  Pricing $50k at each holding's maturity date, with the cash then waiting idle, on the same curve and method gives
  **$297,841** (my run). L08's independent pricer gives $297,778 on the forward basis and **$298,624** on the "yields
  unchanged to 1 Jan 2027" basis (the basis of the IBTR trade note's "about 0.2 percentage points").
- So about $3.4k of the gap comes from the maturity dates (money that comes back early) and about $0.8k from the forward
  vs yields-unchanged convention.

**Which figure is right for which claim.**
- "What would the ten payments cost if bonds matured exactly on each payment date?" $294k. That is a theoretical ladder.
  The 6 Oct email allows only WInS-listed securities (COMPETITION.md:87-90), and no listed holding matures on 1 Jan.
- "How much room is left under $300k for Laura's real, WInS-only ladder, without counting on reinvesting early cash?"
  About **$298k, room about $1.4-2.2k (5-8bp)** on 15 Oct. This is the one for the IPS and the IBTR reflection.
- The $294k figure is honest only if paired with the number sheet's own reinvestment section (early cash and coupons
  reinvested at today's forward rates; the shortfall if yields fall is shown separately, IPS_number_sheet.md:26-34).
  Quoting "$5.5k headroom" alone overstates the room by about four times.
- The number sheet's "1 case in 3" odds of a top-up (IPS_number_sheet.md:14) are anchored to the $294k headline
  (ips_numbers.py:122), so they understate the odds on the WInS basis. L08's rough model gives about 45% (MODEL).
- Either way, all figures move about $290 per basis point (CLAUDE.md:121-122), so any figure must carry its date.

**Why this is a human-factors problem.** The maths is fine on both sides. The failure is that no student owns the number,
so two AI runs a day apart produced two "headline" figures, and the optimistic one went into the file the AI reads first.
The judges read all three deliverables together; three slightly different ladder costs read as three plans.

**Fix.** The rates analyst (a student) owns one dated numbers sheet with one named basis ("WInS holdings, priced on the
[date] curve, carried to 1 Jan 2027, early cash idle"), re-runs it on fixed dates (20 Oct for the TNA, 6 Nov close for
the IPS and Final Report), and is the only source the writers quote. The rates analyst can explain the $294k vs $298k
difference in 60 seconds (Section 8, Q2).

---

### TP-11 - Advice overload: far more AI output than six students can read (high, new)

**What is wrong.** Word counts (wc over .md/.txt/.yaml, 16 Oct 2026): research/ 537,267; rab/ 181,418; docs/ 26,616.
That is about 745,000 words in 162 markdown files under research/ and rab/ alone, plus the 831-page research record and
27-page Strategy Brief, the 30 Sep review (5,659 words), the 15 Oct brief (10,761 words, 30 numbered actions), the
16 Oct number sheet and suggestions (1,867 words), and today's review lenses. At 250 words a minute, 745,000 words is
about 50 hours per reader. The good advice was largely given already on 28 Sep (pre-mortem PM-05: roles, calendar,
internal deadlines) and not acted on.

**Why it costs us.** Every new report adds reading nobody will do and makes the AI more central. The binding limit is
meeting time and ownership, not ideas.

**Fix.** Each role gets at most one page of AI input a week, chosen by that student. Five team actions a week, picked at
the weekly meeting. AI work is "pull, not push": it answers a question a named student asks, with a number, a check or a
list of problems. Nobody needs to read the 831-page record; each analyst reads the one page behind the numbers they own.

---

### TP-12 - Information reaches one person; the other five see snapshots (medium, new)

**What is wrong.** Wharton's emails go to the leader (Rules & Roles:391); the rules watcher alerts one phone
(WATCHER.md:21); the Drive exports are "snapshots from 14 Oct" (START_HERE.md:29); the routines' live copies sit on one
Mac (ops/README.md:9). The 6 Oct email that removed STRIPS is quoted in COMPETITION.md:87-89, but its full text and
arrival time are not in the team's records (15 Oct brief item 9). The only sign of another student working in GitHub is
a public fork made 15 Oct 22:10 UTC with no later pushes (GitHub API: pushed_at 22:10:24, four seconds after creation;
accessed 16 Oct 2026); its owner is not named here.

**Why it costs us.** A student who did not see a change cannot explain it at the semifinal, and the journal misses it.

**Fix.** The rules lead posts a five-line digest in the team chat every Sunday: what changed, what was decided, what is
due, who owns it, any Wharton email forwarded in full. The historian copies it into the ledger.

---

### TP-13 - Darren's challenge and "too timid" were answered by an "AI recommendation"; no team vote logged (high, known-deeper)

**What is wrong.**
- "5 Oct: Darren argued the world fund is a 'copout' and proposed normal stock and ETF picking; Taiwan (EWT) and gold
  (GLD) were also raised. Outcome and reasons: [fill in]" (final_report.md:23).
- The simulated Lauras called the plan "too timid" (notes_and_discussions.md:101). The team asked the right question:
  "Would buying a smaller floor in 2028 and putting more in stocks give Laura a better deal?" (:282). The answer in the
  team doc is "**AI recommendation:** keep the $150k floor ... **Team vote needed (D2/D6).**" (:303). No vote is
  recorded anywhere.
- Note: that table is on the old basis (JPM 2026 inputs, earlier curve); refresh before use (see L08).

**Why it costs us.** This is the team's best real, documented internal debate. Left blank it is wasted; left unresolved
it is a live risk if a judge asks "did everyone agree?". And the record currently says the AI settled it.

**Fix.** At M2: whoever holds the "more stock / EWT / GLD" view now presents it; the growth/risk analyst presents the
case against with refreshed numbers; the team votes and records "disagree and commit" if not unanimous. Success: every
student can state the strongest case for more stock and the team's answer in their own words. If the team is persuaded,
change the plan before 6 Nov. That is allowed and is itself a strong Articulation story.

---

### TP-14 - The written "lessons from last year" leave out every process lesson (high, known-deeper)

**What is wrong.** CLAUDE.md:40-42 records two lessons: packaging "over-complex for the insight" and trading "assets
outside the trading rules". The 15 Oct brief §13 listed more (drift, "make up stories", ChatGPT drafts, outside
reviewer). The process patterns visible in last year's doc, and whether they are back:

| Last year (2025_knox_wharton.md) | This year |
|---|---|
| Hub and spoke: "I will pool the candidates here and you guys filter" (:3870); roles set in comments (:3832) | One person trades, commits, runs routines, sets rules (TP-04, TP-08) |
| AI-iterated drafts: "Report version 3 is developed from report version 2 with critiques and feedbacks provided by ChatGPT" (:3846); "Copy paste this into chatgpt and your report" (:3896) | V5 "Best version that AI generated" (01_version_5.md:36); 13 AI rewrites (TP-08) |
| An AI judge tab ("Final Report AI Judge", :3128) | 5 AI mock-judge routines (ops/routines/JUDGE.md:24) |
| Empty LOGS / Minutes tabs (:3393-3412) | No minutes; PM Dashboard 0 bytes (TP-02, TP-16) |
| An AI post-mortem said "Assign a dedicated 'Editor' role" (:3389) | No roles (TP-05) |
| Deadline-eve crunch and invented-story comments, 11-12 Dec (:3827-3898) | Same calendar squeeze coming (TP-06) |
| Strategy drift after the midterm ("ALL FUTURE TRADES MUST BE ALIGNED", :2967; 50/35/15 at :2977 vs final sleeves at :434-438) | Strategy still open until 6 Nov (TP-07) |

**Why it costs us.** A team repeats what it does not name. Four patterns are already back.

**Fix.** At M1 the six students write their own short "process lessons" list (not AI), each with a tripwire (Section 6).

---

### TP-15 - The team's idea of "what judges want" does not match its own strategy (medium, new)

**What is wrong.** "Final report / IPS = simple textbook models e.g., monte carlo, modern portfolio theory, company
metrics (sharpe, D/E, etc) (interpretible ones)" and "Personally → Eric's HAR model or some random ass quant model to see
if we are right (don't show on the report)" (notes_and_discussions.md:268-271). The plan is a held Treasury ladder plus
one world fund; company D/E ratios and stock metrics have no role; a volatility model has no decision to inform while
the plan is "hold".

**Why it costs us.** Last year's own lesson was "over-complex for the insight" (CLAUDE.md:40). Adding textbook tools to
look rigorous is the same trap, and it hints some students still picture a stock-picking contest.

**Fix.** A "tools we actually used to decide" list: each tool names the decision it changed. Anything that changed no
decision stays out. A student's own model can be a one-line honest mention if it truly tested something.

---

### TP-16 - 24 project techniques listed, none visibly in use (medium, new)

**What is wrong.** The Strategy Notes "Project Management Techniques" tab lists 24, including "Decision Journal",
"Dependency Mapping — ... Especially useful for finding single points of failure", "RAID Log" and "Post-mortem /
Retrospective" (strategy_notes.md:30-53). The PM Dashboard export is 0 bytes; the Trade Log has empty rows; no
retrospective exists; the single point of failure is unaddressed.

**Fix.** Run three, for real: the decision journal (the ledger, Section 9); a 10-minute retrospective after each
deliverable (worked / failed / change); a RAID-lite list reviewed each meeting. Each leaves an artefact for the Final
Report. A judge rewards "we did X and it caught Y", not a list of method names.

---

### TP-17 - The decision story is murky, but salvageable and better than the team thinks (medium, new)

**What is wrong.** Two records disagree on where the core idea came from:
- "The idea came from our AI council run on 27 September" (notes_and_discussions.md:69).
- The 27 Sep notes, labelled "Student-authored brainstorming" (research/council_2026-09-27/team_notes_2026-09-27.md:2),
  already framed the case as liability matching ("DEDICATION (cash-flow matching)", :8), listed "lock everything early
  / lock part now and raise it by rules (author leans to this) / wait until 2033" (:38) and "In 2031 promise a floor
  then protect it" (:40). Who wrote them is UNVERIFIED.
- The switch away from growth-first came from a test: "Growth-first ... failed: 3-8% payment shortfall"
  (CLAUDE.md:70).

**Why it matters.** "We started growth-first, tested it, found it could miss payments, and changed" is exactly the
"decision-making process" and "response to challenges" the criterion asks for, if it is true and AI's part is stated
at each step.

**Fix.** The historian rebuilds 27 Sep to 7 Oct from Doc version history, chat logs and commit dates: who proposed what,
what AI produced, which test changed minds, what was rejected. AI labelled at each step. Success: a one-page true
timeline all six agree with.

---

### TP-18 - Real, specific experience material exists and is not being captured (medium, new)

Genuine, checkable moments most teams will not have:
- Night trading from Sydney; a student fell asleep waiting for the 00:30 open (final_report.md:27).
- The 7 Oct incident: an AI browser click cancelled the wrong order because the page scrolled; the team made a new rule
  (COMPETITION.md:192-193).
- WInS quirks found by checking: no Treasury maturing Feb 2031 to Feb 2036; "IBTN" is an unrelated company; stale bond
  prices; the May-2038 coupon date; the pie chart calling iBonds "Long Equities" (COMPETITION.md:92-100;
  final_report.md:17-20).
- The sector-rule false alarm traced to a mislabelled third-party site (final_report.md:22).
- The 5 Oct catch that the floor was counted inside the reserve (final_report.md:24).
- The 6 Oct email that forced a rebuild without STRIPS (COMPETITION.md:87-90).
- The ladder cost moving from $289.9k (9 Oct) to $294.5k (15 Oct) on one basis in a week
  (caplet-latest/research/ips_numbers_2026-10/results.json): a real "response to challenges" lesson about locking early.

**Fix.** The historian logs each: date, who found it (student or AI, honestly), what the team did, what it taught, the
artefact link. Pick two or three for the Final Report; depth beats a list.

---

### TP-19 - The self-scoresheet drops two of three parts of the Articulation criterion (medium, new)

**What is wrong.** "Winning Team Portrait and Scoresheet.md" scores Articulation with two questions only: "Do the
reflections show a decision that supported, tested or refined the strategy?" and "Is there a real change or discovery
the team can point to, with its reason?" (lines 103-107). The official criterion also needs "teamwork, communication,
and learning" and "reflects meaningfully on the team's growth and response to challenges" (deliverables.txt:58). The AI
mock judges load this scoresheet (ops/routines/JUDGE.md:11, :30), so they will not test those parts either.

**Fix.** Add questions on how work was divided and communicated, one real conflict and how it was resolved, what each
student learned, and how the process changed after a mistake. Score against the official words.

---

### TP-20 - Advisor: letter before term ends, possible reflection, one advisor may serve 21 students (medium, known-deeper)

**What is wrong.**
- Last year's Final Report had "SECTION 2: ADVISOR AND TEAM REFLECTIONS" with an advisor paragraph
  (2025_knox_wharton.md:84-86). Whether this year's 9 Nov instructions ask for one is UNVERIFIED.
- The team list shows four Knox teams with 21 students (team_list.md:32-52). Whether they share one advisor is
  UNVERIFIED (the limit is five teams, Rules & Roles:425). If so, one teacher faces four letters and possibly four
  reflections in the last busy week of term.
- The letter was "not yet requested as of 13 Oct" (COMPETITION.md:132). No record shows any update sent to the advisor,
  whose duties include "Monitoring team engagement" (Rules & Roles:421).

**Fix.** The lead sends the advisor a five-line update every second Sunday. Ask for the letter now; aim to hold it by
Fri 20 Nov. If an advisor reflection is required, give the advisor the evidence ledger to read; the advisor writes it,
not the team and not AI.

---

### TP-21 - Outside readers: last year an outside reviewer steered the story on deadline eve (medium, known-deeper)

**What is wrong.** Last year an outside reviewer (role unknown; whether paid is UNVERIFIED) left content-steering
comments on 11 Dec 2025: "elaborate specifics" (2025_knox_wharton.md:3802), "work on a strategy that aims to
overdeliver on the goal" (:3864), "the long story of how a leader eventually decided to step up" (:3886); drafts were
marked "explicitly developed from" that feedback (:3812, :3816).

**Why it costs us.** Unpaid secondary advisers are allowed (Rules & Roles:427), but work must not be "plagiarized from
any other source, including advisors or 'unofficial' advisors" (:559). A reader who tells you what story to tell steers
authorship.

**Fix.** Outside readers score against the official criteria and ask questions ("I didn't understand X"). No suggested
sentences or story ideas. Keep a list: who, when, what they saw, confirmation they were unpaid.

---

### TP-22 - The school's information pack has the wrong portfolio size and leaves out the TNA (low, new)

**What is wrong.** The pack in the Team List doc says teams "manage a **$500,000 virtual portfolio**"
(team_list.md:69); this year's WInS account is $300,000 (CLAUDE.md, Key facts; COMPETITION.md). Its key dates list the
roster, IPS and Final Report but not the Trading Notes Analysis on 23 Oct (team_list.md:101-103).

**Why it costs us.** Small for Caplet, which tracks the TNA in COMPETITION.md. But any student, parent or the advisor
reading the school pack would miss a scored deliverable, and other Knox teams may rely on it.

**Fix.** The rules lead tells the advisor, so the shared pack can be corrected for all Knox teams.

---

## 5. What "Articulation of Competition Experience" needs that only a real process produces

| Part of the criterion (deliverables.txt:58) | What a judge looks for | What only a real process gives | Caplet today |
|---|---|---|---|
| "teamwork, communication" | Who did what; how the team talked and split work | Roles, meeting notes, a digest, a handover | Roles blank; no minutes |
| "learning" | Something each student did not know before, and how they found out | Each student's own example, with a date | Journal has examples, few names |
| "research and decision-making process" | Options, evidence, the choice, the reason | A decisions register with votes and dissent | Votes not logged; AI "recommendation" in place of a vote |
| "growth and response to challenges" | A real setback and what changed after it | Retrospectives; before/after rules | Good raw material (TP-18), not yet written up |
| "authentic team voice" (deliverables.txt:59) | Students' own words, specific details | Students who did the work writing it | AI suggestions now allowed (TP-08, TP-09) |

---

## 6. Operating rhythm to 4 Dec (minimum version)

Eight meetings of 45-60 minutes on video, about seven hours per student in total, plus short solo tasks. Sydney times.
The deputy chairs; the historian takes live notes; every meeting ends with "decisions, owners, dates" read aloud.

| # | When | Length | Agenda (decisions in bold) | Pre-read (max) | Outputs |
|---|---|---|---|---|---|
| M1 | **Sun 18 Oct** | 60 min | Roles (Section 7); charter and decision rights (TP-08); **the AI rule for deliverables**, one copy in all three files (TP-09); shared calendar; process lessons and tripwires (TP-14); **TNA picks**; **name**; **vote set A essentials**; 60-second round 1 | 1 page per role | Role table, charter, calendar, logged votes |
| solo | Mon 19 - Tue 20 Oct | | Three reflection writers draft alone; rates analyst issues the 20 Oct dated figure (TP-10); trader + checker confirm each pick shows "Filled" | | 3 drafts |
| solo | Wed 21 Oct | | Editor checks word counts, numbers, match with M1 votes; outside reader scores only | | Marked drafts |
| solo | **Thu 22 Oct evening** | | Notes pasted exactly from WInS, a second student checks character by character; leader submits, deputy on call | | TNA in (deadline Sat 24 Oct 08:00) |
| M2 | **Sun 25 Oct** | 60 min | TNA retrospective (10 min); ratification (TP-01); **Darren's challenge / floor size** (TP-13); **vote set B**; **coupon-reinvestment option**; 60-second round 2 | half-page options notes by owners | Votes and dissent logged; IPS section owners |
| solo | Mon 26 Oct | | Full IPS draft circulated (the pre-mortem tripwire date) | | Draft |
| M3 | **Sun 1 Nov** (US clocks change) | 60 min | IPS read aloud; each owner defends their part; freeze-day plan (no trades); 60-second round 3 | the draft | Final edit list |
| solo | Wed 4 Nov | | Format check by two students (PDF, word counts by two counters, pages, font) | | PDF |
| solo | **Thu 5 Nov evening** | | Leader submits IPS, deputy on call; two students screenshot WInS after the freeze (Sat 7 Nov) | | IPS in (deadline Sat 7 Nov 09:00) |
| M4 | **Tue 10 or Wed 11 Nov** | 45 min | Read the Final Report instructions together; assign sections; check the ledger; letter status | the instructions | Section owners and dates |
| M5 | Sun 15 Nov | 45 min | Section outlines; rates analyst freezes the 6 Nov-close numbers sheet; 60-second round 4 | outlines | Agreed outline |
| M6 | Sun 22 Nov | 60 min | Full draft read; outside reader 23-25 Nov; school letter in hand (target Fri 20 Nov) | full draft | Fix list |
| M7 | Sun 29 Nov | 45 min | Final edits; Works Cited and AI-use entry from the real log; format | final draft | Submission pack |
| solo | **Wed 2 Dec evening** | | Leader submits Final Report + letter, deputy on call (before Presentation Day Thu 3 Dec) | | In (deadline Sat 5 Dec 09:00) |
| M8 | week of 7 Dec | 45 min | Retrospective; Jan-Mar 2027 availability; semifinal skeleton from the submitted reports only (TP-03) | | Retro notes |

Every Sunday: the five-line digest (TP-12); the historian updates the ledger and the decisions register.

**Tripwires** (if one fires, the deputy calls a 15-minute catch-up within two days):
- a week with no logged meeting;
- one student's name on more than half of a week's ledger entries;
- no full draft five days before a deadline;
- any sentence in a draft that its owner cannot say they wrote;
- any comment asking someone to "expand the story" or "make up" detail;
- a rule changed without a logged team vote;
- two different figures for the same number in team files;
- the leader unreachable 48 hours before a deadline.

---

## 7. Roles (owners by role, not by person; one student may hold more than one)

The team chooses who holds what. Nobody holds more than three; the leader holds no more than two; every role has a
backup.

| Role | Owns | Deliverable link | Backup |
|---|---|---|---|
| Lead and submitter (fixed: the team leader, Rules & Roles:391) | Submissions, Wharton contact, advisor updates | All | Deputy |
| Deputy / operations | Calendar, internal deadlines, chairs meetings, copies of every final file, on call at each submission | All | Lead |
| Trader + checker (two people) | WInS keystrokes; ticket read-back; freeze-day screenshots; Trade Log | TNA; Final Report (implementation) | Each other |
| Historian and AI-log keeper | Evidence ledger, decisions register, meeting notes, AI-use log, true timeline (TP-17) | Final Report (experience, Works Cited) | Editor |
| Rates analyst | One dated numbers sheet, one basis (TP-10); explains duration and the curve | IPS numbers; Final Report projections | Growth/risk analyst |
| Growth/risk analyst and devil's advocate | VT sleeve, stress cases, the "timid" answer, the 2028-deposit risk | IPS; Final Report analysis | Rates analyst |
| Client and co-sponsor lead | Laura's goals in the case's words, the 2031 range, co-sponsor draft | IPS pitch; Final Report co-sponsor part | Editor |
| Rules, format and privacy lead | SMApply/FAQ watch, weekly digest, word/page/format checks, keeps the three rule files in sync (TP-09) | All | Deputy |
| Editor | One voice across all three deliverables; consistency table (TNA vs IPS vs Final Report) | All | Historian |

Plus, for every student: one TNA reflection or IPS section, one Final Report section, one 60-second topic, and one thing
they can show on a semifinal video as "how I contributed value".

---

## 8. The 60-second test (every student, no notes)

At each meeting draw three questions at random. A student answers in 60 seconds. The others score 0-2 each on
"correct", "plain", "own words". Anything scored 0 by two people goes on next week's list. Answers come from the student,
not from a script; this table lists what a full answer covers, not the words.

| # | Question | A full answer covers |
|---|---|---|
| 1 | What does Laura need, in order? | Ten $50k payments 2033-42 with "high degree of certainty", from the portfolio; then a facility contribution; a 2031 range that protects the payments; flexibility |
| 2 | Why buy the ten payments first, and now? What do they cost? | Yields near 5% make them cost close to $300k; the cost moves about $290 per basis point; on 15 Oct about $298k for the WInS holdings (about $294k only for idealised bonds maturing on payment dates), so the room is small; always give the date and basis |
| 3 | What is a ladder and why does a crash not break it? | One maturity per payment year held to maturity; prices move but payments do not; remaining risks: US default, iBond funds' final payout not fixed, reinvesting coupons and early cash |
| 4 | Why iBonds for 2033-37 and bonds for 2038-42? | WInS lists no Treasury maturing Feb 2031 to Feb 2036; IBTM-IBTR fill the gap; IBTN in WInS is not an iBond |
| 5 | What if yields fall before January 2027? | The ladder costs more than $300k; the gap comes from the 2028 deposit first; the floor shrinks by the same amount; payments still bought |
| 6 | What is the floor, and how is the 2031 range set? | IBTM sized from the 2028 deposit; range = floor up to floor + half the stock fund; why the bottom must be owned, not forecast |
| 7 | Why so little in stocks? Isn't that timid? | The price of certainty; what each step down in the floor adds to the middle and costs in bad years (refreshed numbers); what the team voted and why |
| 8 | What if the $150k in 2028 is late or smaller? | Payments already bought from the first deposit; the facility range shrinks; how the team would tell co-sponsors |
| 9 | Why does our WInS portfolio look like this? | It mirrors Laura's plan after both deposits, scaled to $300k; WInS profit is not scored or added to projections; why we hold; the pie-chart mislabel |
| 10 | What about Taiwan inflation and the NT dollar? | Payments are fixed US dollars; building costs and exchange rates change what the gift buys; what the team says about them |
| 11 | Which words do we never use, and why? | "Guaranteed", "risk-free"; cash-flow matching, not immunisation; floor-plus-cushion, not CPPI |
| 12 | How did we use AI, and what did we decide ourselves? | Honest and specific; matches the AI-use log, the team's AI rule and the Works Cited |
| 13 | What did we change our minds about, and why? | A real change with date and evidence (growth-first to lock-first; a WInS quirk; the outcome of Darren's challenge) |
| 14 | What was your job, and what value did you add? | The student's role, one thing they produced, one thing it taught them (last year's semifinal asked exactly this) |
| 15 | What is the strongest argument against our plan? | The best counter-case (more stock; wait for better yields; one fund only) and the team's answer |

---

## 9. Evidence ledger for the Articulation criterion (checklist)

Each row needs all of these, or it does not go in the Final Report:
- [ ] Date (and time zone if it matters).
- [ ] What happened, in one line.
- [ ] Who was involved (first names; "AI" if an AI found or did it).
- [ ] Options considered.
- [ ] Decision and the reason; vote count.
- [ ] Any dissent, in that student's words.
- [ ] Artefact link: WInS timestamp, Doc version/comment, chat message, screenshot (private Drive, never the public repo).
- [ ] Which criterion part it shows: teamwork/communication/learning; research and decision process; growth and
      response to challenges.

Before submission, the historian and one other student check that every experience claim in the Final Report maps to a
ledger row. Anything that does not map is cut.

---

## 10. UNVERIFIED (could not confirm)

- The six students' year levels, and whether any sits the 2026 HSC exams.
- Knox's internal Term 4 assessment and exam dates.
- Whether a student other than the leader can open the SMApply submission forms.
- Whether this year's Final Report instructions require an advisor reflection.
- Whether the four Knox teams share one advisor.
- Who wrote the 27 Sep "student-authored" notes and the polished journal entries.
- Whether last year's submitted experience scenes were real (the doc shows instructions to invent them).
- Whether last year's outside reviewer was paid.
- This year's semifinal format and dates (FAQ says live panel; last year it was a recorded video plus written answers,
  announced 27 Jan, video due 9 Feb).
- Whether any of the 15 Oct brief's 30 actions were done after the 14 Oct export (no repo evidence either way; the
  only later commit is 412e9e3).
- Whether the team has seen or agreed to the 16 Oct AI rule change.

---

## 11. Sources

Repo files (read 16 Oct 2026): CLAUDE.md; COMPETITION.md; START_HERE.md; team/google_drive/{notes_and_discussions,
final_report, strategy_notes, team_list, README, 2025_knox_wharton}.md; team/google_drive/ips_report/01_version_5.md;
team/google_drive/sheets/{pm_dashboard/sheet1.csv, portfolio_and_trading_notes/trade_log.csv};
team/Winning Team Portrait and Scoresheet.md; ops/README.md; ops/routines/{WATCHER,MONITOR,JUDGE}.md and
scheduled_tasks/; research/insight_v1/phase_E/E5_premortem.md; research/council_2026-09-27/team_notes_2026-09-27.md;
competition/official/2026_27/smapply_public_2026-10-14/{deliverables,faqs}.txt; `git log` on main.
New branch (caplet-latest/, commit 412e9e3): CLAUDE.md, COMPETITION.md, START_HERE.md, docs/AI_USE.md,
research/ips_numbers_2026-10/{IPS_number_sheet.md, IPS_v5_suggestions.md, ips_numbers.py, results.json},
competition/official_market_data/daily-treasury-rates_2026-10.csv.
Recomputation: lenses/L10/calc/basis.py (reproduces $294,453; WInS-maturity basis $297,841).
Other lenses cross-checked: L08 (ladder series), L09 (integrity), R4 (2026-27 specifics).

Web pages (accessed 16 Oct 2026; text saved under lenses/L10/ or research/R4_pages/):
- Wharton Rules & Roles: https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/
- Wharton competition page (finale "April 29 & 30"): https://globalyouth.wharton.upenn.edu/competitions/investment-competition/
- Wharton news, 27 Jan 2026: https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/
- 2025-26 Semifinalists Next Steps: https://globalyouth.wharton.upenn.edu/wp-content/uploads/2026/01/25%E2%80%9326-Semifinalists-%E2%80%93-Next-Steps-FINAL.pdf
- Knox term dates: https://www.knox.nsw.edu.au/about/public-information/term-dates
- NSW public school calendar 2026: https://education.nsw.gov.au/schooling/calendars/2026
- NESA 2026 HSC timetable news: https://www.nsw.gov.au/education-and-training/nesa/news/all/2026-hsc-timetables-released
- GitHub API, forks of the repo (metadata only; owner not named).
