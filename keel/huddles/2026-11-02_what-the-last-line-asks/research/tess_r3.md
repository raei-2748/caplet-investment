# Tess, round 3 check: what only the order line does (H-019, Mon 2 Nov 2026)
> FICTION (the speaker is simulated; the sources, counts and readers' words are real). (Keel is a simulated team, AI-written.)
> No new model calls. Counts: `keel/office/tools/textcheck.py`, strict (split on hyphens), scratch copies only.

## 1. Does the majority D say the floor holds before the top?
| Where | Words | What it ranks |
|---|---|---|
| P5 | "first finishes any rung ... Most of the rest buys a Treasury fund ... That is her floor. The remainder ... one world index fund" | build order in 2028 (rung, floor, stocks), not a shortfall order |
| P6 | "The bottom is her floor, rounded down: money she already owns. The top adds half her stocks, valued that day." | the floor is built safer; no rule on who gives way |
| P7 | "We could put the floor into stocks ... cannot be quietly halved if markets turn." | the floor is not risked for a bigger gift; no floor/top ranking |
| P8 | "so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range." | flexibility, then the whole range (both ends together); cheques safe |
| Probe P2 (`../blind/probe_RQWN.md`) | "Laura's flexibility gives way first ... then 'Whatever the stocks can't cover lowers the whole range.' What is protected to the very end is the ten cheques" | two tiers above the cheques; the floor never a tier of its own |

Result: floor-before-top is gone from D. But the design only has it after naming day:
- Naming day: "slide the whole range: the top is cut by the same uncovered gap as the bottom (one mark, both ends)"
  (`../../../rooms/lab/L-13_slide_the_range/run.py:7`; L-13 md :14-15; current design per L-15 md :9 and
  `../../../ips_rewrite/IDEA_LEDGER.md:215`, "the top falls with the floor"). The floor drops; the half above keeps its width.
- After naming (Jan 2033 set-aside): "first the stocks Laura kept, then the gift ... the gift can land under the top but
  stays inside the range" (`../../../ips_rewrite/inbox/2026-11-02_window.md:53`, MODEL).
So A's "The order never changes" was true after naming and inverted on naming day, two lines under P8.

## 2. The afternoon readers' own words (H-018)
- Sonnet, `../../2026-11-02_beside-the-champion/posts/r2_reader1_sonnet.md:7`: "fixes the priority ('the cheques, then
  the floor, then everything above it'). Those are the two things portfolio construction and the time-horizon discipline
  need." :8, on Amara's D1 (no order line, both P8 sentences kept, `arms/C_amara_D1.txt:15`): "no priority order".
  :39: "It doesn't say the order of what".
- Haiku, `r2_reader2_haiku.md:9`: "It states the order rule, the stock size and the client trade-off". :11: "without the
  order rule the planned changes are less concrete". :6 shows a diff read ("only Y lacks 'The order never changes'").
- Confound: the text without the line also cut "That is under a tenth of her money." (Sonnet's other named reason).

## 3. Wharton's IPS questions (`../../../WHARTON_WORD.md`)
Q5 (:62-63) has the line's three things (operating commitment, facility contribution, flexibility); P8 + P3 answer it in
D (probe P2). Not expected in the IPS: "a final facility-contribution range" (:92-93). s3 (:109-110) "not be rewritten
simply because markets move": P7 and P3 carry it.

## 4. Commandment III (`../../../BIBLE.md:358-362`)
"No slogans, no triads, no fact-sheet runs." The line is a triad after a colon. VII (:377-379): "sums, edge cases and
mechanisms go to the Final Report".

## Counts (scratch: `/tmp/claude-0/-home-user-caplet-investment/03dc3032-2d9e-57f6-91b4-70cc152ed434/scratchpad/r3/tess/`)
| Copy | Change to the majority D | Strict | sha256 (16) |
|---|---|---|---|
| D.txt | none (= `../arms/D_round2_majority.txt`) | 495 | fb9c9a8463ce9ddd |
| c1 | P6 + "Once named, the top gives way before the bottom." | 504 | 105e60ed050be43c |
| c2 | P8 "...lowers the whole range; once she names it, only the top can give." | 504 | 88dcc85084183eac |
| c6 | P6 + "After that, only the top can slip." | 502 | e708eaf01124ecc6 |
| c4 | P6 "money she already owns, kept last." (unclear: fails IV) | 497 | e6cfd91607f0eeb0 |
| c3 | order line back in P9 | 508 | d0bbd75da1a56a47 |
| c5 | order line back, minus the flexibility clause, "the money set aside" (my r2 D) | 497 | 72d7069d5b47fee5 |
