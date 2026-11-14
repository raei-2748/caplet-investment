# How each daily Final Report run works (Keel's protocol, from Sun 8 Nov 2026)

Every scheduled run of the Final Report thread follows this page. It turns Ray's standing orders of 8 Nov (top of
`../EXPECTATIONS.md`, INSTRUCTIONS I94-I100) and Caplet's of 9 Nov (I101-I102) into steps, and borrows from the methods in
`research/meta/HOW_STRATEGISTS_PLAN.md`. It never overrides the day's own instructions or Caplet's word.

## How hard (Caplet, Mon 9 Nov, INSTRUCTIONS I102)
"I am expecting you to have burned through almost every last one of your tokens by the end of each and every week ...
that doesn't mean wasting tokens. You must be efficient. And EVEN THEN, you should burn through all of them. Quality AND
quantity." So every run, morning and evening, works in parallel: at least four research workers on separate claims,
each reading primary sources in full (papers, theses, essays, filings, data), never summaries of summaries; every find
carded; the day's volume logged in the RUNLOG row (sources read, cards added, claims kept, killed or changed). Waste is
re-reading what the store already holds, regenerating what exists, or research that feeds no section of the report.

## Book 17 (Caplet, Sat 14 Nov, INSTRUCTIONS I104-I113): three things every run now does
- **Voice, on the round days** (Mon 16, Wed 18, Fri 20, Sun 22, Tue 24; rehearsal Thu 26): run the round in
  `voice/README.md`. Fresh writers read only Caplet's own writing (`voice/CORPUS.md`) and the plain facts; readers judge
  whole passages blind, with Caplet's real passages mixed in. Never a rule list, never word-level comparison.
- **Evaluate, never describe again:** any new note for the report says what it judges, against what
  (`research/meta/EVALUATE_NOT_DESCRIBE.md`).
- **Nothing lost:** a new card's strong rows get a place in SKELETON, a named line that carries them, or a written
  reason, the same day (`research/GEM_LEDGER.md`, `research/gem2/`); its investing sources go to the references
  (`research/REFERENCES_PLAN.md`, Keel's call of Sat 14 Nov: cite it all, APA-clean).
- **The conceit (Caplet, Sat 14 Nov evening, I114):** a note that changes a figure, a date or a part checks
  `CONCEIT.md` sections 3 and 6 the same day, so the dates of inking and the image placed in each part stay true to the
  register. A new parallel goes into CONCEIT only with its craft fact sourced (card Q40) and its number in NUMBERS.

## The loop (Ray, Mon 9 Nov: "running automically self-reinforcing to produce the BEST final report")
Every run makes the next one better (`BEST_IN_COMPETITION.md` section 3):
- **Start** from `LESSONS.md` (how to work) and `SCORECARD.md` (where the report is weakest). The two or three lowest
  cells, and any part where the judges disagree, are the run's first claims; breadth research waits for a cell that
  needs it.
- **End** by re-scoring every cell the run's evidence touched, with the reason and what would make it a 5; a score
  rises only when evidence lands, never for wording. Add the run's method lessons to `LESSONS.md`. The RUNLOG row
  carries the scorecard's lowest cell and mean.
- **Twice a week** (Mon and Thu, and after any large change to `INTENT.md` or `SKELETON.md`), a panel of three judges
  scores the plan blind: different personas, methods and models (EXPECTATIONS 4.3), each reading only Wharton's
  instructions, the case, the frozen submissions and the plan, never the scorecard or Keel's notes. Their files go to
  `research/panel/`; their disagreements become targets.

## Before work
1. Read `../EXPECTATIONS.md` (Ray's standing orders first), `WHARTON_NORTH_STAR.md`, this page, the last five lines of
   `ARGUMENT_LOG.md`, and any message from Caplet since the last run. A student's word overrides everything below.
2. Name the day's questions as **claims to keep, kill or change**, not topics to read about (Story-Based Inquiry,
   Tetlock). Example: not "authors' incomes" but "Laura's 2028 deposit falls when share prices fall".
3. For each hard problem, **classify it at its core** (strategy, writing, persuasion, forecasting communication, project
   management, computing, knowledge management) and look first at how the field that owns it has solved it, finance or
   not (`research/meta/HOW_STRATEGISTS_PLAN.md` section 3).

## During work
4. **Read widely** and send research workers where the work is broad. Real sources only, with URL and access date;
   anything not read at the source is UNVERIFIED.
5. **Every find goes into the store** as a card row in `research/cards/` (harvest table format, `research/HARVEST_BRIEF.md`),
   with the five-question card for the strong ones: what is it; did it work; how Laura's case is like it; how it is not;
   what Caplet takes. Nothing is lost; weaker ideas are ranked lower, never deleted.
6. **Coherence.** Check every note against `CANON.md` (what the submitted IPS, Trading Notes, reflections and frozen
   portfolio commit Caplet to) and every number against `NUMBERS.md`. A clash with what is frozen is a risk to record,
   never a change to the strategy.
7. **Wharton's test.** Put each note, number and plan decision through the seven questions in `WHARTON_NORTH_STAR.md`
   section 7.
8. **At a bottleneck**, step back before pushing harder: a skill (`TOOLS.md`), the in-product skill and plugin search,
   or the field that solved this kind of problem. Note what was tried in the RUNLOG row.
9. **No Final Report prose before Fri 27 Nov.** Notes, numbers, tables and exhibit designs only; nothing a reader could
   paste into the report.

## After work
10. One line in `ARGUMENT_LOG.md`: the date, which claims were kept, killed or changed today, and how the argument in
    `INTENT.md` moved (or "unchanged"). This is the day's output in one place, for Caplet and for the next run.
11. Rebuild the store if cards changed (`research/store/build_store.py`), one RUNLOG row, commit, open and merge the
    PR, check that the portal run is green.
12. Reply to Caplet only with a result, a blocker or a question. Otherwise the checklist carries progress.
