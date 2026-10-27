# Keel on Keel: how Keel improves itself

> Ray, 24-25 Oct 2026: Keel should be "self-recursive without our supervision". Keel works every day; once a week it
> looks at what its own runs achieved and rewrites its own playbooks. Hard limits: `INVARIANTS.md`.

Two loops, one inside the other (from Wed 28 Oct 2026; Ray, 27 Oct: "every round, but loop is never repetitive"):
- **The inner loop, daily: Out and Back** (`../loop/README.md`). Each Sydney day is one research round: Nora gathers,
  the Window gates, scouts go out across the web, the Lab connects what they bring back, the rooms work it, the
  evening room hunts the flaw, repairs, judges head to head against the best-so-far and discusses, the Archive
  records, and the night room reflects and sends the next scouts off. Five memories make every round differ
  (`../loop/TERRITORY.md`, `LENSES.md`, `CHAMPIONS.md`, `FRONTIER.md`, `LESSONS.md`) and a lesson learned in a round
  is read by the next one (Reflexion-style).
- **The outer loop, weekly: Keel on Keel** (below). It improves the inner loop itself, the way autoresearch's human
  improves `program.md`: **rooms run** (runbooks in `runbooks/`) -> **each run logs a line** (`RUNLOG.md`) and **each
  round a health row** (`../loop/HEALTH.md`) -> **Sunday: the newest draft is scored** (`SCORECARD.md`) -> **Keel
  changes at most 3 rules** (`SELF_CHANGES.md`) -> the next rounds follow them.

## 1. The scorecard sets the goal (Courtroom, before Sun 17:00)
Score the newest IPS draft (the Final Report after 7 Nov) 1-7 on the five Wharton criteria and Ray's four north stars (equal);
rubric at the top of `SCORECARD.md`. The two lowest scores are next week's targets: every run names the one it aims at.

## 2. The weekly self-review (weekly plan, Sun 17:00; Nora runs it, Kai attacks)
1. Read this week's `RUNLOG.md` rows, the week's rounds (`../loop/rounds/`) and `../loop/HEALTH.md`, and the newest
   `SCORECARD.md` row next to last week's. Check the loop's warning lights (`../loop/README.md`, "The loop's health").
2. For each room, count runs, outputs used later (a request closed, a line kept in a draft, a student's answer) and score moves.
3. Undo any change from last week that moved no score, unless its log entry says why it needs longer.
4. Make **at most 3** changes, the most useful first:
   - a room whose output nobody used for two weeks: merge it into another room, slow it down, or pause it (`SCHEDULE.md`);
   - a runbook rule that kept causing rework (the same fix made twice): rewrite it;
   - a room that keeps moving the lowest score: give it an extra run (`SCHEDULE.md`), inside the token ceiling;
   - `SELF_DIRECTION.md` or `LOOP.md` when the problem is shared by several rooms;
   - the inner loop itself: a lesson in `../loop/LESSONS.md` broken twice becomes a runbook rule; a lens that produced
     nothing in three draws is retired; the explore-vs-deepen dial is re-set for the week; a beat that adds nothing
     to the rounds is merged into another room's beat.
5. Log each change in `SELF_CHANGES.md` (date, file, change, evidence, score it should move) and in the runbook's own change log.
6. Two lines in the Sunday stand-up: what Keel changed about itself, and why.

## 3. The watchdog (daily loop, 07:00)
Read `SCHEDULE.md` for the rooms due yesterday and look for each one's line in `RUNLOG.md` (or its commit on the day branch).
- Count only the tasks whose "Now" schedule in `SCHEDULE.md` fell on yesterday (daily, Tue-Sat, Sunday, odd or even dates), so a room that wasn't due is never a miss.
- The brief opens with the health line: "<ran> of <due> rooms ran yesterday", naming any that didn't (e.g. "8 of 9; the Library didn't, so I've put it on the board").
- A missed room gets one Ready card for its job today, done by the daily loop if nothing scores higher.
- Two misses in a row: add a question to `ASK_HUMANS.md` ("the <room> scheduled task may be broken"), default: the
  daily loop covers that room's job until a student fixes it.

## 4. The merge (Archive 19:10; daily loop sweeps at 07:00)
Merge the day's PR into `main` under `INVARIANTS.md` section 3. Tomorrow's day branch is created from the new `main`,
so every run starts from everything Keel has learned. Non-keel files go to a separate PR for Ray.
