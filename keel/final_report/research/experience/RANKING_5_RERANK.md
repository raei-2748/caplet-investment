# The blind re-rank of Mon 16 Nov 2026: do the three moments hold?

Notes for the Final Report store, not report prose. Answers SKELETON 3f's open question (do `RANKING_4_PURPOSE.md`'s
three moments hold when fresh readers score them blind against the strongest challengers?) and the day-9 order: add any
real event since the last ranking, re-rank blind with fresh readers, and work out how each of the strongest is told
vividly and without corniness.

## Method

- **New events since Sun 15 Nov night:** none passes the Book 18 gate (card `../cards/Q13_how_the_team_learned.md`
  section (c): everything since is Caplet's instructions, Keel's own process, or the invented diary, which is never told
  as real).
- **The pack** (`BLIND_POOL_3.md`, key `blind_key_3.json`, seed 20261116): RANKING_4's three moments and the three
  RANKING_2 challengers that pass the gate, each on a corrected fact sheet of about 300 words, roles not names, every
  figure from the register or dated as that day's model.
- **Three fresh readers**, none of whom had read the earlier rankings, the key or card Q13: a Wharton finance professor
  marking criterion by criterion, a former finalist reading as a first-round volunteer, and a portfolio manager who edits
  nonfiction. Each read the rubric (`RERANK_RUBRIC.md`), the submitted IPS and TNA, and the pack; scored the gate and
  criteria A-E on their own; and wrote, for each event, the one detail that carries it and what would make it corny.
  Files: `judge3_1.md` to `judge3_3.md` and their `.csv`; aggregated by `aggregate3.py`.

## Scores (mean of three readers; A influence, B reasoning, C disagreement, D uncertainty and learning, E new and checkable)

| Rank | Event | Mean | A | B | C | D | E | Readers' totals | In readers' chosen sets |
|---|---|---|---|---|---|---|---|---|---|
| 1 | "A copout": the world fund against its strongest objection (RANKING_4 moment 1) | 21.7 | 4.0 | 5.0 | 4.0 | 5.0 | 3.7 | 21-22 | 3 of 3 |
| 2 | "Too timid": the plan priced from the other side (challenger) | 21.3 | 4.3 | 5.0 | 4.0 | 4.3 | 3.7 | 20-23 | 3 of 3 |
| 3 | A knife edge: what $300,000 could buy (challenger) | 20.7 | 5.0 | 4.0 | 2.3 | 5.0 | 4.3 | 20-22 | 2 of 3 |
| 4 | The promise called certain was the weakest one (challenger) | 20.3 | 4.7 | 5.0 | 2.0 | 4.7 | 4.0 | 19-21 | 1 of 3 (a fourth for one more) |
| 5 | The first plan failed its own test (RANKING_4 moment 2) | 19.3 | 4.7 | 4.0 | 3.0 | 4.0 | 3.7 | 19-20 | 1 of 3 |
| 6 | Buying it: from a plan to a portfolio (RANKING_4 moment 3) | 17.7 | 3.0 | 4.0 | 1.7 | 4.0 | 5.0 | 17-18 | a fourth for 1 of 3 |

All six passed the gate with every reader. No criterion split by two or more points. The top four sit within 1.4
points, so the rubric's tie rule (gap under 1.0: D, then A, then E) orders them only loosely; the set rules decide.

## The answer: one moment holds, two change shape

- **Moment 1, "a copout", holds**, first with all three readers and in every reader's set. It also carries Book 18's
  order that the case for keeping the world fund is the report's place for investing erudition.
- **Moment 2, the first plan's failure, holds only as the first clause of the "too timid" moment.** On its own it
  scored fifth: the IPS already opens with the same switch (l.9, for its own reason, a writer's income), so it adds
  less than the readers wanted (one reader: "E6 stays out because the IPS already opens with that switch"). Told
  together, the two are one story about the share weight in two turns: a first plan too bold, priced and dropped; then
  a plan called too timid, priced and kept. Kahneman and Lovallo's title names both turns ("Timid choices and bold
  forecasts", 1993, card Q13 row 9), and their cure for timidity, adding many bets together, is the thing ten fixed
  promises cannot do. That pairing scores where the parts did not: C 4 from the timid charge, A and D high from both.
- **Moment 3, buying it, moves to 2.5 as one or two clauses and to the knife edge's tail in 3f.** It scored last: no
  one held a second view (C 1.7) and its lesson concerns operating the trading platform more than Laura's plan. Its
  details stay where they do work: the curve check (two bonds 111 and 92 basis points off the curve, then a 0.25-point
  rule) and the one-owner rule after the click belong to 2.5's implementation; the 00:30 open can close the knife edge
  in one clause. Caplet's Book 18 named the mis-click as possibly worth including; it is kept, told without attribution,
  in 2.5.
- **The knife edge enters 3f.** It scored highest on A and D: the team's own headline ("fits inside $300,000") was
  dropped before any order because the ten cost more than $300,000 on 173 of 185 closes to 25 Sep, and the completion
  rule the IPS carries was written for that reason. The reflection tells why the rule was written, never the rule
  itself (IPS l.13), and says the fills near the year's cheapest close were timing, not skill (NUMBERS 8b). Its history
  figure is 2.5's aha (8e); in 3f it carries the 2026 figure (8b), never both bases in one paragraph.
- **The weakest promise (27 Oct) is the reserve.** Strong on A and D, weak on C. Its finding (interest must be earned
  before 2033, so the extra Treasuries pay the ten even if waiting cash earns nothing) is 3a's evaluation already; in
  3f it would tell the same tranche of the 2028 deposit as the knife edge, which the set rules forbid. It returns only
  if a part loses an event.

## The set for 3f (the lead's choice, against the rubric's set rules)

| Place | Moment | Words | Part of what Laura was told | Set rule it meets |
|---|---|---|---|---|
| 1 | The knife edge, ending on the 00:30 open in one clause | about 150 | The payments and their cost; the completion rule | A decision kept after a dated test, with what was luck |
| 2 | Too bold, then too timid (the first plan's failure as its opening clause) | about 190 | The bottom of the range: the floor | C at 4 (an objection from outside the plan) |
| 3 | "A copout" | about 220 | The top of the range: the world fund | C at 4 (an objection inside the team); the erudition |
| | A closing paragraph: which recommendation each moment changed or held | about 40 | | |

Three moments walk Laura's order of claims, the payments, then the bottom, then the top. No two tell one story, and
none retells the Trading Notes (the copout is told through the objection and the bar, never through Trading Note 3's
argument for the fund).

## How each is told, vividly and without corniness (the readers' details, merged with card Q13's notes)

**The knife edge.**
- Carries it: more than $300,000 on 173 of the 185 Treasury closes to 25 Sep, fitting only from 10 Sep (two readers);
  or the two pricings of the 28 Sep curve $204 apart, reconciled to the cent by changing the day count and the
  one-to-three-month rates (the professor). Pick one; the first is the one a tired reader keeps.
- Corny if: "knife edge" is said in the report as a heroic frame; the near-cheapest fill is credited to judgement; a
  slogan closes it ("certainty is bought, not assumed").

**Too bold, then too timid.**
- Carries it: the share weight argued over (50, 60 or 70%) moved the median by about $2,000, while putting the
  payments first took misses from one simulated market in thirty to none (27 Sep model); then the readers who put the
  plan first and still called it too timid, "with only about 9% in stocks", and the price of their view: each $25,000
  less floor added about $2,000-3,000 in the middle and cost about $9,000-10,000 in a bad market (29 Sep model).
  Today's version of the same trade is NUMBERS 8n (three-quarters shares: the bottom she could name falls from $95,000
  to $30,000).
- Who the readers were is never said (a blind test of six anonymous plans; the record does not support "teachers" or
  "friends", so neither is written).
- Corny if: a slogan flip ("timid was the point", "timid is just careful"); a journey "from gamblers to guardians";
  ending on "our first plan failed so Laura's wouldn't".

**"A copout".**
- Carries it: the bar written on 30 Sep, five days before the objection, before any number was run, and the closest
  rival (the world fund with 10% gold and 10% property trusts) stopping at 0.8991 against 0.90, passing about four
  runs in five when the bar asked for every run (30 Sep model).
- The teammate who said "copout" is never the fool of the story; the objection is put so its holder would accept it.
  Leave out the journal's "[fill in]" (an outsider reads it as untidiness). The reasons the team gives now are "what we
  understand now", one sentence of evidence at most (Q46).
- Corny if: "our copout was our conviction"; "we chose humility over stock picking"; Trading Note 3's "vain illusion"
  reused as the moral.

**Across all three** (the readers' closing paragraphs agree): each names a belief, the dated test that broke or kept
it, the part of the plan that came out of it, and one honest line on luck, with a single number a reader can carry
away. No moral is spelled out; each ends on the part of the plan it explains.

## What changes elsewhere

- SKELETON 3f: the set above replaces RANKING_4's three moments; "names who did what" becomes "says what was done and
  when, in the roles the record supports".
- SKELETON 2.5: the curve check and the one-owner rule after the click, as implementation facts in one or two clauses.
- EXPERIENCE_RECORD section 2 points here.
