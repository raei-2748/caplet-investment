# The final-night team (Thu 5 – Fri 6 Nov 2026, Sydney)

Set up Thu 5 Nov, 23:40 Sydney, at Ray's request ("setup an exceptional local agent team for wharton"), using the
`team-agent-orchestration` and `task-coordination-strategies` skills (found with /find-skills, installed from
affaan-m/ECC and wshobson/agents). Mission: Book 12. One absolute final pitch and IPS by **Fri 6 Nov, 08:00 Sydney**,
reviewed and rewritten many times. Live state is in `BOARD.md`.

## House rules (every member, no exceptions)
0. **Rounds are the Writer's alone (added 02:05 after an overwrite).** Nobody but the Writer ("Lead") creates or edits `rounds/R*_ips.txt`, `rounds/R*_pitch.txt`, `rounds/blind/`, `ROUNDS_LOG.md`, `README.md` or `FINAL_REPORT_BANK.md`. Suggestions go in a message to the Writer or a review file `rounds/RN_<seat>.md`.
1. **One writer.** Only the Writer writes pitch or IPS prose. Everyone else reads, researches, checks or reviews,
   and may quote, critique and propose ideas, never sentences meant for the page.
2. **Own your file.** Each member writes only the file(s) listed against their name, in this folder. Never edit
   another member's file, `BOARD.md`, `TEAM.md` or anything outside `final_night/`.
3. **No git.** The checkout is shared by 17 sessions. Nobody runs `git checkout`, `switch`, `commit`, `merge`,
   `pull`, `stash` or `reset` except the Repo Steward. Branch: `claude/book12-final-night`.
4. **Hard limits** (`../../pm/INVARIANTS.md`, Ray's boundaries): no WInS, no SMApply, no trades, no submitting, no
   edits to Caplet's Google Docs, no emails or messages to people, no student personal data, no room runs (Book 12).
5. **Wharton's word ranks first**, then the twelve books (`../../BIBLE.md`), then Ray's I80-I88
   (`../../INSTRUCTIONS.md`). Case words only (I83): no "floor", "cheques", "building gift". No GPTZero, no
   "AI DRAFT" labels (I88). No "if a judge asks" (I82).
6. **Hand-off.** When your file is done, send one short message (SendMessage) to the Chief of Staff (session
   `local_0c243b27-2662-4a17-97a2-1bc57cb936ba`) and to the Writer (`local_ea5d3b0f-a3fd-4fc0-a2b1-11ec02552525`): file path, three-line summary,
   anything that blocks the Writer. Readers finish by **01:30**; reviewers turn a round around in **20 minutes**.

## The roster

| Seat | Session (title) | Role | Owns (writes only this) | Due |
|---|---|---|---|---|
| Writer | Lead | Sole author of pitch + IPS; decides every word | `rounds/R*_ips.txt`, `rounds/R*_pitch.txt`, `ROUNDS_LOG.md`, `README.md`, `FINAL_REPORT_BANK.md`, final `ips.txt` + `pitch.txt` | rounds all night; final 07:30 |
| Chief of Staff | Chief of Staff (this session) | Runs the board, routes rounds to reviewers, chases blockers, merge gate | `TEAM.md`, `BOARD.md`, `READING.md` (index) | ongoing |
| Repo Steward | Repo Steward | The only git operator: periodic commits of `final_night/`, merges, push, portal check | git history only | commits on request |
| **Readers** (Phase 1) | | | | |
| R1 | Harvest – Drafts | Every draft V1-V58 + the students' own versions: best line, worst flaw, vanished ideas | `HARVEST_DRAFTS.md` | 01:00 |
| R2 | Harvest – Rooms | Every room, memo, idea bank, ladder, huddle: strategy-level ideas the IPS never used | `HARVEST_ROOMS_TEAM.md` | 01:00 |
| R3 | Fact-Checker | Case words, WInS holdings, the submitted TNA notes, every usable number with source, never-say list; then checks every number in each round | `FACTS_ADDENDUM.md`, `rounds/R*_facts.md` (FACTS.md is the Writer's) | 01:00, then per round |
| R4 | Library – Damodaran | NYU corporate finance lectures (cflect.htm): concepts that fit this strategy | `READING_DAMODARAN.md` | 01:30 |
| R5 | Library – Shiller | Yale ECON 252, all 26 lectures/transcripts: concepts that fit | `READING_SHILLER.md` | 01:30 |
| R6 | Library – Beyond | LDI, defeasance, Redington, Leibowitz, Merton, Bodie, Roy, Lintner, newsvendor, donor studies, endowment rules | `READING_BEYOND.md` | 01:30 |
| R7 | Idea-List Judge | Item-by-item verdict on the pasted list in Book 12, with the maths checked | `IDEA_LIST_MATHS.md` | 01:30 |
| R8 | Strategist | Ray's I86: what is the strategy, its biggest strength, why very strong, what is most creative; plus the opponent's best case | `STRATEGY_SPINE.md` | 01:00 |
| **Reviewers** (Phase 2, each round) | | | | |
| V1 | Bible Auditor | First builds the checklist of every expectation in Wharton's word, Books 1-12, the Commandments and I80-I88; then scores each round line by line (review (a), the one that decides) | `BIBLE_CHECKLIST.md`, `rounds/R*_bible.md` | checklist 00:45 |
| V2 | Wharton Marker | First builds the rubric (five criteria + the IPS's five questions + "not expected in the IPS"); then marks each round | `WHARTON_RUBRIC.md`, `rounds/R*_wharton.md` | rubric 00:45 |
| V3 | Voice Coach | First a one-page writer's card distilled from `voice/` (laws, F-moves, how humans cut); then reads each round aloud for machine tells and unreadable sentences | `VOICE_CARD.md`, `rounds/R*_voice.md` | card 00:45 |
| V4 | Archivist | Each round against the submitted TNA, the WInS trade notes and the locked holdings: any contradiction is a stop | `CONSISTENCY.md`, `rounds/R*_archive.md` | per round |
| V5 | Judge – Practitioner | Blind judge: a fixed-income portfolio manager, sceptical, rewards rigour and correct terms | `rounds/R*_judge_practitioner.md` | per round |
| V6 | Judge – Cold Reader | Blind judge: a Wharton undergraduate evaluator who knows the case but not the jargon; paraphrases every paragraph, flags any sentence not clear on one reading | `rounds/R*_judge_cold.md` | per round |
| G | Genius Lab (`local_8f5f8876`, kept by Ray 02:40) | Creativity lab: strategy-level ideas (I84: in the plan and its reasoning, never metaphor), each checked against the locked record and the books; never writes IPS sentences meant for the page | `GENIUS_LAB.md`, `rounds/R*_genius_lab.md` | on call |
| V7 | Judge – Contrarian (R7's second shift, from 01:30) | Blind judge: an equity-minded industry judge who thinks the plan is too timid for a client "willing to take thoughtful risks"; scores creativity and conviction | `rounds/R*_judge_contrarian.md` | per round |

Every session was forked from the same thread, so blindness is a discipline, not a guarantee. Judges read blind (Commandment IX): they see only the round's pitch and IPS and `WHARTON_WORD.md`, never the
change notes, never which round is newest, never each other's reviews.

## The flow (dependency graph)

```
Readers R1-R8  ─┐
Rubrics V1-V3  ─┼─→ Writer round N ─→ Chief of Staff pings V1-V7 + R3 ─→ reviews in rounds/ ─→ Writer round N+1
                ┘                         (loop until the merge gate passes; final 07:30)
```

Critical path: readers' rankings → Writer's cut to 500 words → at least three full review rounds → final.

## Merge gate (the final draft ships to Caplet only when all hold)
- Pitch ≤ 50 and IPS ≤ 500 words (`../../office/tools/textcheck.py`, strict count).
- Bible Auditor: no failed line on the checklist.
- Wharton Marker: every criterion and every IPS question answered; nothing from the "not expected" list.
- Archivist: no contradiction with the submitted TNA, trade notes or holdings.
- Fact-Checker: every number has a source; nothing on the never-say list.
- Cold Reader: every paragraph paraphrased correctly on one reading.
- Writer signs off in `ROUNDS_LOG.md`; Repo Steward commits and pushes; the portal run is green.

## Card schema (BOARD.md)
Owner · state (backlog / ready / running / review / blocked / done) · file · acceptance · last heartbeat.
