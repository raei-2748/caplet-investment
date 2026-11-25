# The writing session, Fri 27 Nov 2026: how it runs

**Caplet's working doc (Wed 25 Nov 2026, late evening; `CAPLET_DOC_2026-11-25.md`).** Caplet is drafting in its own doc. Caplet answered Wed 25 Nov 23:22 Sydney ("keep doing what you're doing"): the session writes a complete draft to Caplet's v2 map and opening, with the restrained pencil and ink, for the team to rewrite. Section 4 below (Thu 26 Nov) is the session's plan and wins over sections 1-3 where they differ.

Started Wed 25 Nov (Day 18) with the review loop, rehearsed that morning; Day 19 (Thu 26 Nov) adds the frozen inputs,
the pre-mortem, the phases' timetable, the page template and the round log (README row 19). The plan it comes from:
`research/meta/HOW_STRATEGISTS_PLAN.md` section 2d. The sentences are written by fresh writers who have read only
Caplet's own writing and the plain facts for their part (README, "What Book 17 changed"); the main session plans,
supplies the facts, runs this loop and sends every fix back to a writer.

## 1. The review loop (rehearsed Wed 25 Nov on Caplet's IPS with five planted faults)

Evidence: `research/meta/review_loop_rehearsal_2026-11-25/RESULTS.md`. Every planted fault was caught by at least four
of ten independent reviewers; the fresh reader and the killer-item checker together caught all five; the blind
compare caught all five; one review round took about seven minutes of wall clock and about 1.1 million tokens.

**Every round, in order** (the lead times each step by its own clock):
1. **Freeze** version N (a file per round: `drafts/session/vN.md`).
2. **Core reviews, in parallel, each alone:**
   - **Fresh reader** (a reader who has seen no earlier version; the case and the draft only). Reads once, then from
     memory: the plan in one sentence; the range and how sure; what the team learned; where it got lost. Then, reading
     again, six to eight questions a judge would ask that the draft ought to answer.
   - **Killer-item checker** (the draft, the case, `CANON.md`, `NUMBERS.md`, `WORDS.md`, the D35 list,
     `CASE_MAP.md` section E). PASS or FAIL with the words quoted:
     K1 every number and date matches the register or the case; K2 nothing contradicts the IPS, the Trading Notes or
     the portfolio as submitted; K3 only real facts and real events; K4 no banned pattern or word; K5 within Wharton's
     limits (pages measured in the template); K6 only permitted investments; K7 every term a reader needs is defined
     where first used; K8 every ask in CASE_MAP section E is answered on the page; K9 "we" per 100 words in each part,
     against Caplet's IPS; K10 every name a part uses is set up in that part or before it; plus every fix in the
     regression log still holds.
3. **Reader test** (adapted from the Reader Testing stage of Anthropic's doc-coauthoring skill): a reader with the draft
   only answers the fresh reader's questions, each ANSWERED, PARTLY or NOT ANSWERED with the words it rests on, then
   says what is ambiguous, what the draft assumes the reader knows, and where it contradicts itself.
4. **Rotating reviews, on alternate rounds** (each scores 1-5 and names at most three problems, ranked, quoted, never
   rewriting; one page of rubric, `research/meta/review_loop_rehearsal_2026-11-25/RUBRIC.md`, adapted to the report's
   parts):
   - the **reading reviewer** (EXPECTATIONS, then Creativity and Presentation; found every reading fault in the
     rehearsal);
   - the **bond reviewer** (Investment Strategy and Portfolio Analysis, with the TNA and the register; found the
     contradiction and the wrong number);
   - the **red team** (the three reasons a judge marks it down);
   - in rounds 6-9 only, a **co-sponsor reader** on 3d, and an **Articulation reader** on 3f.
   A round in which K1 or K2 fails also calls the bond reviewer.
5. **Consolidate** (the lead): one list, ranked by how many independent reviewers named each point and which
   criterion it hits; every K1 or K2 failure goes to the top whatever its count. The writer decides what to take;
   reviewers have no authority. One logged line per decision.
6. **Rewrite**: whole paragraphs or parts, by a writer in the voice; cut whole ideas, never squeeze sentences.
7. **Blind compare** of N and N+1, unlabelled and in random order. If N+1 loses, revert and try a different fix.

**Paired measures.** Fewer problems counts only if the fresh reader still recovers the plan, the range and the lesson,
and the reader test answers at least as many questions as the round before.

**Fault seeding, rounds 3 and 8.** The lead plants two known faults in a copy the core reviewers see (the writer keeps
the clean text). If a core step misses one at the report's full length, the rotating reviewers run every round after.

**Models.** Reviewers on Sonnet with one page of rubric each; the writers and the lead on the main model.

## 2. What the voice rounds add to the checks (rounds 11-20)

- A sentence two readers stop at is rewritten whole; the stops are almost always a name or a date that arrives
  before what it names (round 11's third failure; round 19's "the floor", IBTM, "in 1 January 2033 money").
- One date per figure in prose; a figure's dating basis goes to the exhibit's note.
- The team is the actor where a step is the team's (round 19: "we" fell to 0.4-0.9 per 100 words once a writer wrote
  about the plan's money).
- Round 20 (Wed 25 Nov evening, Section 2 whole): nine stops by all three readers, every one a name or a reason
  missing (WInS, "the floor", why the 2033 piece waits, why 2037 is a fund, the extra Treasuries' job). So every round
  checks each part against `NAME_ORDER.md` (the order in which names are first used, with the lead's sixteen decisions):
  a name used before it is set up in its part is a killer item. The watch list prints as Table 2 (APA numbering);
  Keel's files call it Table 3, so every brief says "the watch list (Table 2 in print)".
- A writer copies the fact sheet's reasons word for word (round 20's two sense faults were version 12's own), so the
  fact sheet is checked for sense like report prose.

## 3. Thu 26 Nov (Day 19): what was still to write

All of it is now in section 4. The inputs as they stood after Wed 25 Nov are listed there with the versions frozen.

## 4. The session plan (written Thu 26 Nov, Day 19)

Built from `research/day19_2026-11-26/PREMORTEM.md` (twenty causes, each with a guard), `CAPLET_MAP.md` (Caplet's v2
map against every Wharton and case ask) and voice round 21 (`voice/ROUND21.md`: Section 2 written whole to Caplet's
map, read blind by three readers: plan recovered 3/3, clarity 3 of 5, every shared stop a name or a reason missing).

### 4.1 Frozen inputs (no new research during the session)
Writers see only: `voice/CORPUS.md`, `FINAL_IPS_as_submitted.txt`, Caplet's own text from its doc (re-read at 06:00
Fri, read only, saved under `drafts/session/caplet_v2_<time>.md`), and their part of `voice/FACTS_PLAIN.md` version 15.
Checkers see: `SECTION_NOTES.md` (its "Caplet's v2 map" table first), `NUMBERS.md` through the numbers extract
(`drafts/session/NUMBERS_EXTRACT.md`, every figure the report may print with its one basis and one date), `CANON.md`,
`WORDS.md`, `NAME_ORDER.md`, `CASE_MAP.md` E with `research/day19_2026-11-26/CAPLET_MAP.md`'s E1-E21, the exhibits
(`exhibits/`, Figure 1 on the fee-and-margin basis), `research/WORKS_CITED_DRAFT.md`, the D35 list. Nothing else is
read for content; any gap found is a note for the handover, not research.

### 4.2 Shape and timetable (Sydney time)
- **06:00-10:00, round 1:** a whole rough draft. Caplet's Section 2 opening and Table 1 are kept as Caplet wrote them;
  one writer per part continues it (Section 2's remainder; Section 3's five parts in Caplet's order; the title page
  from Caplet's doc, never copying the WInS username into the repo). Then one core review.
- **Rounds 2-4, structure and argument.** Structure freezes after round 4: a point reversed once is decided by the
  lead and logged, never reversed again.
- **Rounds 5-7, evidence:** numbers, the co-sponsor words (inside "Before Laura gives her word", set off), the
  operating reserve as a recommendation, the watch list (Table 2 in print), the Team Reflection last.
- **Rounds 8-9, sentences and voice** against Caplet's own writing; the join between Caplet's opening and the
  continuation is checked by name (round 21: all three readers heard it).
- **Final checks**, then the handover by Sat 09:00. Nine rounds in all; the stop rule may end it earlier and nothing
  adds a round beyond nine. Two to four hours of margin stay unplanned.

### 4.3 Budget
About 1.8 million tokens a review round, 2.4 million for round 1, 1.5 million for final checks (PREMORTEM section 3).
Soft cap 15 million after round 6 (above it, rotating reviewers run only when K1 or K2 fails); hard cap 21 million
(stop rewriting, final checks on the best version, build the handover). The lead logs agents and an estimate after
every round. Every frozen version is pushed, so a stop at any hour leaves a deliverable.

### 4.4 Guards from the pre-mortem (the eight highest)
1. Names before they are set up: each writer's brief lists the names its part may use, in `NAME_ORDER.md` order, with
   the plain description that comes first; K10 runs on Caplet's text too; a sentence two readers stop at is rewritten
   whole by its writer. Round 21's fixes: who the payments are paid to, the building and the co-sponsors come before
   Table 1.
2. Readers who pass what the students fail: each fresh reader first marks Caplet's seventeen failed version-61 lines
   mixed with Caplet's own IPS lines, and is used only if it stops at most of the seventeen. "Followed first time" per
   part is counted and held at 80% or more by round 9.
3. One basis and one date per figure: the numbers extract, Figure 1 on fee-and-margin; K1 fails on any figure with two
   values.
4. Churn: structure frozen after round 4; at most five fixes a round, ranked by the number of reviewers naming them.
5. A tour of the research: every paragraph names its branch in Caplet's map; anything without a home stays out and
   goes to the cut list.
6. Voice: writers read all of Caplet's own writing first; K4 and K9 every round; one blind check a round against a
   paragraph of Caplet's.
7. The fact sheet's reasons are copied word for word, so version 15 was checked for sense on Thu 26 Nov and is frozen.
8. The usage limit: whole draft by hour 4, every version pushed, the caps above.
Also: the draft keeps to Caplet's choices (v2 map, restrained pencil and ink, no make-up promise, "committed" never
"secured"); Caplet's own sentences are never rewritten silently, and the stops in them go to the handover note; the
draft is laid out in `template/` after round 1 and held to eleven pages so the last page is margin; the lead never
writes report sentences.

### 4.5 Stop rule
Stop when two rounds in a row cannot be told apart in the blind compare, the fresh reader recovers the plan, the range
and the lesson, and every killer item passes; or at round 9; or at the hard cap.

### 4.6 Round log (After Action Review), one block per round in `drafts/session/ROUND_LOG.md`
Round N, start and end time, agents and estimated tokens. What we meant to fix. What changed (parts, with the fix
taken and by whom). Why (the reviewers who named it; the criterion). What did not change and why. Measures: fresh
reader's three recoveries, reader-test answers, "followed first time" per part, killer items, page count. Blind
compare result. Regressions found (added to the regression log). Next round's aim.

### 4.7 Handover, Sat 28 Nov 09:00 (on the portal and in the thread; no Artifacts or Claude Docs)
The draft as markdown on the portal, ready to paste into Caplet's doc; a one-page plain-English note (what it argues,
what changed in the rounds, the stops found in Caplet's own sentences, what Caplet must decide); the works cited; a
claims-and-sources sheet; a cut list; open risks; the round log.
