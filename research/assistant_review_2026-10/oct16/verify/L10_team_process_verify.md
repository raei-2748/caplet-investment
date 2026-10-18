# L10 Team, process and human factors: verification (16 Oct 2026)

**Scope.** I re-opened every cited source myself:
- repo files and line numbers;
- `git show 412e9e3` and `git log`;
- the GitHub forks API (owner not named);
- the live Rules & Roles page and the 2025-26 Semifinalist PDF, both re-fetched with page.py on 16 Oct 2026;
- the cached Knox term-date and NESA pages;
- a re-run of `lenses/L10/calc/basis.py` on the official 15 Oct curve.

**Result.** 22 findings checked:
- 8 confirmed;
- 14 adjusted;
- 0 refuted.

I added 3 findings. Severity changes:
- critical to high: TP-01, TP-02;
- high to medium: TP-03, TP-06, TP-09, TP-11, TP-13, TP-14, TP-21;
- medium to low: TP-16.

**Personal data.** The final JSON contains no surnames, no surname initials, no reviewer or advisor names, no home-folder path and no fork owner.

**Overlap with other lenses** (fine to keep, but merge when writing the team brief):
- TP-01 overlaps L09 INT-04.
- TP-08 overlaps L09 INT-01.
- TP-13 overlaps L05 TNA-08.
- TP-10 overlaps L08 COH-01 and L03 STRAT-01.

## Number conflict ($294k vs $298.6k)

Both figures use the same official 15 Oct par curve. I re-ran `basis.py`:

| Method | Cost on 1 Jan 2027 |
|---|---|
| $50k discounted to each 1 Jan payment date, forward rates (the number sheet) | **$294,453** (matches results.json exactly) |
| Same curve, priced at the WInS holdings' earlier maturity dates, early cash earning **0%**, forward rates | $297,841 |
| Same, yields unchanged (L08) | $298,624 |

**Why they differ.** The gap comes from two things:
- about $3.4k is cash sitting idle between each maturity and its payment;
- about $0.8k is the forward vs unchanged convention.

**L10's mistake.** L10 said "use about $298k for Laura's real ladder". But the team's own WInS notes say early proceeds wait in a short-term Treasury ETF (`05_trading_note_reflection_wins_trading_notes.md:16-17`). Cash that earns short Treasury rates brings the cost back to about the payment-date figure.

**Which figure for which claim:**
- **"What the ten payments cost"** (IPS, Final Report): about $294.5k-$295.3k, with about $4.7k-$5.5k of room (16-19bp).
- **IBTR note's "about 0.2 percentage points" trigger** (TNA reflection): use the holding-date basis the note was written on. On that basis the room fell from 22.7bp (6 Oct) to 4.7bp ($1,376) on 15 Oct.
- **$298.6k:** a cautious bound, not the headline.
- **Top-up odds:** "about 1 in 3" is fair on market-rate bases (the L08 verifier got 28-33%). The 45% figure applies only if early cash earns 0%.

## Verdicts

**TP-01: ADJUSTED (critical to high).**
- The quotes exist.
- But CLAUDE.md:74-75 sit in a section marked "as of 2026-09-28 (superseded)". Since then:
  - the journal records "1 Oct: model check backed the $150k floor and 50/50 split; IPS content locked" (final_report.md:21);
  - trades were placed on 6-8 Oct.
- So "the team has not read the memos" is stale.
- **Still true:**
  - no reasons, options or dissent are recorded in students' words;
  - the team's own doc credits the AI council (notes:69);
  - the gate box is unticked.
- I added the live plagiarism wording: "the use of another's words or ideas as if they are one's own".
- No breach has happened yet, so it is high, not critical.

**TP-02: ADJUSTED (critical to high).**
- All evidence is verified:
  - the journal stops at 7 Oct, with blanks at :16 and :23;
  - the dashboard export is 0 bytes;
  - the trade log is empty;
  - last year's logs are empty tabs;
  - the 2025-12-11 "Make up stories" comment exists;
  - four of this year's six were on last year's team.
- "Deadline eve" is UNVERIFIED, so I removed it.
- A thin record costs marks. It only becomes a disqualification risk if stories are invented. The 15 Oct brief already asked for this (item 23).
- Keep last year's commenter unnamed.

**TP-03: ADJUSTED (high to medium).**
- I re-fetched the PDF. The quotes are exact:
  - speaking role for every member;
  - "Do NOT introduce completely new material";
  - video due 9 Feb;
  - "authentic team voice".
- 27 Jan to 9 Feb is 13 days.
- This year's FAQ says "via video conference ... to a live panel of judges" (faqs.txt:89), so the format may differ.
- It matters only after the Top 50 cut. Its main fix is already in TP-05.

**TP-04: ADJUSTED (minor fix).**
- Main has **96** Ray commits and 45 Claude commits (all branches: 100 and 68), not 98. No other student appears.
- Everything else is verified:
  - the routines run on Ray's Mac (10 task files);
  - alerts go to Ray as push notifications;
  - Rules & Roles lines 367, 391 and 393 (live);
  - FAQ:34 "It should be a team decision."
- The 15 Oct brief already raised it (final.md:101, :608).

**TP-05: CONFIRMED.**
- The Roles column is empty.
- The branch's CLAUDE.md still says "no roles assigned yet".
- The pre-mortem quotes are exact. Its failure story matches the journal.
- The fix is fine. Keep the role table on the private Drive.

**TP-06: ADJUSTED (high to medium; not new).**
- The Knox dates and the NESA quote are verified.
- Every deadline is a Saturday morning in Sydney: correct.
- But the 28 Sep pre-mortem already flagged the holidays and the HSC window (E5_premortem.md:276-283). The 15 Oct brief already set the school-letter target of Fri 20 Nov.
- Whether any member sits the HSC is UNVERIFIED.

**TP-07: ADJUSTED (known-deeper).**
- The count double-counts:
  - floor size is part of vote set B;
  - the "timid" floor question got a 1 Oct outcome;
  - the gate votes are settled in practice by the 6-8 Oct trades.
- About six decisions are really open.
- Vote sets A and B were already scheduled in the 15 Oct brief:
  - picks on Mon 19 Oct;
  - set B on Tue 27 Oct.
- L10 proposes Sun 18 and Sun 25 instead. The team must pick one schedule.
- IPS V5 already says Root-and-Branch. Only COMPETITION.md lags.

**TP-08: CONFIRMED.**
- `git show 412e9e3` shows both sentences removed:
  - "Do NOT write the Trading Notes, IPS or Final Report";
  - "the team does not submit them as they are".
- COMPETITION.md:142 says "Since 16 Oct (Ray's decision)".
- The suggestions file has 13 rows (its own text says "twelve").
- No vote is recorded anywhere. The finding is about decision rights only; L09 INT-01 covers integrity.

**TP-09: ADJUSTED (high to medium).**
- The START_HERE vs CLAUDE.md/COMPETITION.md contradiction is confirmed.
- I dropped docs/AI_USE.md:65 as evidence: it is a dated log entry, not a rule.
- **Added:**
  - the new rule exists only on the unmerged branch, so main still says "Do NOT write";
  - the routines read a third rules file in a private memory folder on Ray's Mac (JUDGE.md:10, WATCHER.md:19).

**TP-10: ADJUSTED (stays high).**
- The diagnosis and the reproduction are correct.
- The recommendation was backwards (see the number section above).
- I corrected the problem, evidence and fix. The fix now keeps two named lines: plan cost, and the IBTR trigger check.

**TP-11: ADJUSTED (high to medium).**
- All word counts reproduced exactly.
- Reading load does not itself block the Top 50.
- This lens itself adds 22 findings, 11 of them due Sun 18 Oct (see V-02).

**TP-12: CONFIRMED.**
- The leader receives all communications (Rules & Roles line 391).
- The live routine copies are on one Mac.
- The team sees 14 Oct snapshots.
- The 6 Oct email survives only as a one-sentence quote.
- The fork's pushed_at is 4 seconds after its creation.

**TP-13: ADJUSTED (high to medium; known).**
- The floor question did get an outcome: the test is dated 29 Sep, and the journal records the 1 Oct "model check backed the $150k floor".
- That outcome has no reasons or vote count recorded.
- Darren's 5 Oct challenge is the truly open item.
- Already raised in the 15 Oct brief (final.md:613) and in L05 TNA-08.

**TP-14: ADJUSTED (high to medium).**
- All quotes are verified.
- But each repeating pattern is already its own finding. This one is the summary.

**TP-15: CONFIRMED.** notes:270-271 are verbatim.

**TP-16: ADJUSTED (medium to low).**
- The 24 techniques, the empty dashboard and the blank log are verified.
- But "none in use" is false: a pre-mortem, red teams, gates A-D and an assumption map all exist. AI ran them.
- What is missing are the student-run ones: decision journal, retrospectives and RAID log.

**TP-17: CONFIRMED.** The quotes are verbatim. Authorship of the 27 Sep notes is correctly marked UNVERIFIED.

**TP-18: CONFIRMED.**
- results.json: $289,893 (9 Oct) to $294,453 (15 Oct), a rise of $4,560.
- The 7 Oct incident was an AI browser click, so log it honestly as AI.

**TP-19: CONFIRMED.**
- The scoresheet's Articulation part has only 2 questions.
- The official criterion text is verified (deliverables.txt:58).
- The scoresheet is itself AI-drafted (see V-01).

**TP-20: CONFIRMED.**
- Last year's advisor section is verified.
- Four Knox teams, 21 students.
- The letter was not requested as of 13 Oct.
- The advisor duties and the five-team cap are verified live.
- The unverified parts are labelled.

**TP-21: ADJUSTED (high to medium).**
- The comments are verified, all dated 2025-12-11.
- An outside reader is planned this year (scoresheet:121; final.md item 17), so the guardrail is timely.
- But unpaid secondary advisors are allowed (line 427), and there is no sign of steering this year.

**TP-22: ADJUSTED (known).**
- Verified: the $500,000 figure and the missing TNA date.
- Already in the 15 Oct brief (item 29, line 248). Kept at low as a reminder.

## Findings this lens missed (verifier-added)

**V-01 (medium): Closed AI loop.**
- Claude drafted the self-scoresheet (AI_USE.md:63).
- Five scheduled AI judges score against it (JUDGE.md:11, :22).
- Since 16 Oct, AI may also suggest the wording.
- So the same system sets the bar, writes the text and marks it.
- **What a fix must achieve:** humans score first, against the official criterion text. Students rewrite the Articulation questions. AI judges list problems only.

**V-02 (medium): The fixes are too many for one meeting, and two schedules disagree.**
- 11 of L10's 22 findings are due Sun 18 Oct.
- That breaks L10's own "five actions a week" rule.
- The 15 Oct brief and L10 give different meeting dates.
- **What a fix must achieve:** one agreed calendar, and a Sun 18 agenda of at most five items, with the TNA first.

**V-03 (high): The TNA critical path has no named students.**
- Both TNA reflection tabs held only Wharton's instructions in the 14 Oct export.
- The picks are not decided.
- Every TNA step needs a role, and no roles are assigned.
- The live Doc may have moved on since 14 Oct (UNVERIFIED).
- **What a fix must achieve:** a named student owns every step by Sun 18 Oct, with an internal submit time of Thu 22 Oct evening, Sydney.

## Files
- Final JSON: `oct16/verify/L10_team_process.final.json` (25 items)
- Build script: `oct16/verify/L10w/build.py`
- Re-fetched semifinal PDF text: `oct16/verify/semis_pdf.txt`
