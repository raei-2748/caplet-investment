# The writing session, Fri 27 Nov 2026: how it runs

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

## 3. Still to write on Thu 26 Nov (Day 19)

The frozen inputs and their versions; the pre-mortem on the session; the phases' timetable (rounds 2-5 structure,
6-9 evidence and the co-sponsor text, 10-12 sentences); the stop rule (two rounds the blind compare cannot tell apart,
with the fresh reader recovering all three points, or hour 20); the page template; the round log's form (After Action
Review: what we meant to fix, what changed, why, what next); the Sat 28 handover pack.

As they stand after Wed 25 Nov (the candidates to freeze on Thu 26 Nov): `ARGUMENT_TREE.md` with today's card
verdicts; `SECTION_NOTES.md` (the checkers' brief for each part: its job, criteria, ideas by store id, aha, turn,
numbers, exhibit, sources, Canon lines and trap; the writers never see it); `voice/FACTS_PLAIN.md` version 13 (the
writers' facts); `NUMBERS.md` with 8za (the freeze check of Wed 25 Nov); `WORDS.md`; `CANON.md`;
`research/WORKS_CITED_DRAFT.md` with cards Q242-Q253 to add (card Q252's fix list first); `NAME_ORDER.md`.
