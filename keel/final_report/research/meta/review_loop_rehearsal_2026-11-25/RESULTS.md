# The review loop, rehearsed on Caplet's IPS with five planted faults (Wed 25 Nov 2026, 06:43-06:50 Sydney)

Day 18's task (README row 18; HOW_STRATEGISTS_PLAN 2d): run the writing session's review loop once, on a text whose
faults are known, never on Final Report prose, so the loop is fixed before Fri 27 Nov. The text: a copy of Caplet's
submitted IPS (`../../../FINAL_IPS_as_submitted.txt`, unchanged) with five faults planted by the lead
(`planted_IPS.txt`; the key in `lead_only/KEY.md`, opened by no reviewer). The rubric: `RUBRIC.md` (one page, from
EXPECTATIONS and Wharton's five criteria). The shared instructions: `PREAMBLE.md`. Every reviewer worked alone on
Sonnet, saw only the files its role names, and wrote to `outputs/`.

## The five faults

| # | Kind | Planted |
|---|---|---|
| F1 | A wrong number | "6 years to wait" became "5 years" |
| F2 | A contradiction with the TNA | the late-2032 fund's "payout" became its "fixed payout" (TNA l.13: "the final payout is not fixed") |
| F3 | An undefined term | "only the rung gap to cover", never defined |
| F4 | A buried point | the paragraph's point (no payment rests on a share price) moved to the tail of a 70-word sentence |
| F5 | A banned pattern | "Markets move. Promises don't." after the last real point |

## Who caught what

C = named as a fault with the right reason (an "unsure" with the right reason counts); P = flagged, but as merely odd
or for a wrong reason; - = not raised. Scores: C 1, P 0.5.

| Step and reviewer (what it read) | F1 number | F2 TNA | F3 term | F4 buried | F5 pattern | Score of 5 |
|---|---|---|---|---|---|---|
| 2. Fresh reader (text and case only; read once, then from memory) | P | P | C | C | C | 4.0 |
| 3. Bible reviewer (RUBRIC A, EXPECTATIONS 3.x and 5.x, D35 list) | - | - | C | C | C | 3.0 |
| 3. Investment Strategy (RUBRIC B, the TNA) | C | C | C | - | - | 3.0 |
| 3. Client Knowledge (RUBRIC B, the case closely) | C | - | - | - | - | 1.0 |
| 3. Portfolio Analysis (RUBRIC B, the TNA) | P | C | C | - | - | 2.5 |
| 3. Creativity and Presentation (RUBRIC B) | - | - | C | C | C | 3.0 |
| 3. Brilliance reader (text and case only) | - | - | C | C | - | 2.0 |
| 4. Red team (RUBRIC, the TNA) | C | C | C | - | C | 4.0 |
| 5. Killer items, K1-K7 (TNA extract of CANON, NUMBERS 0-5, D35, WORDS) | C | C | C | - | C | 4.0 |
| Reader test (the page only; answers the fresh reader's eight questions, then three checks) | C | C | C | P | P | 4.0 |
| 8. Blind compare (planted copy against the clean text, unlabelled) | C | C | C | C | C | 5.0 |
| **Reviewers who named it (C) of the ten in steps 2-5 and the reader test** | **5** | **5** | **9** | **4** | **5** | |

- **Every fault was caught by at least four independent reviewers.** The cheapest complete pair was the fresh reader
  and the killer-item checker (between them all five); the reader test alone caught four.
- **The blind compare caught all five** in 13 seconds and chose the clean text (confidence 4 of 5): with two versions
  side by side, every change shows. In the session it compares version N with N+1, so it is the regression catch, not
  a fault finder on a first draft.
- **What each kind of reviewer is for.** Faults of fact and agreement (F1, F2) were caught by reviewers who held a
  second document (the case, the TNA, the register): strategy, analysis, red team, killer items. Faults of reading
  (F4) were caught only by reviewers who read as a reader: the fresh reader, Bible, presentation, brilliance. F3 was
  caught by nearly everyone. F5 by the voice-minded and the checklist.
- **The weakest return: the Client Knowledge reviewer** (one fault, marked unsure, though F1 was a case fact). Its
  slots went to real but unplanted points (the case's own words for the residency missing from the text).
- **Noise.** About half of each reviewer's three slots went to points in Caplet's own text that were not planted:
  "barring a US default" (5 reviewers; Book 19 retired the guard for the report, the IPS is frozen), "immune to
  markets" and "pay what they say" for funds that pay a net asset value (5), no dollar range or confidence (6; the
  case asks the Final Report for it, so in the session that is a real fault), "hedge" for diversification (1). None
  was false. In the session they are exactly what the writer must weigh.

## Times (the lead's clock, launch to return; the reviewers' own clocks were unreliable)

| Step | Wall clock |
|---|---|
| Building the planted copy, key, rubric and preamble (once only) | about 6 minutes |
| Steps 2-5, nine reviewers in parallel | 19-59 seconds each; the step about 1 minute |
| Reader test (after the fresh reader's questions) | 37 seconds |
| Consolidation by the lead (counting mentions per fault and per non-planted point) | about 4 minutes |
| Blind compare | 13 seconds |
| **One review round, end to end, excluding the rewrite** | **about 7 minutes** |

Each reviewer used about 97,000-130,000 tokens (mostly its instructions and the files it read); the eleven together
about 1.1 million. A Final Report draft is about four times the IPS's length, so a round's reviews will take longer and
cost more, and a round of eleven reviewers twelve times over is about 13 million tokens before the writers.

## What changes in the protocol (recorded in `../../../WRITING_SESSION.md`)

1. **Four steps every round, cheap and complete together:** the fresh reader (who also writes the judge's questions),
   the killer-item checker, the reader test on the fresh reader's questions, and the blind compare of N against N+1.
2. **The rubric reviewers rotate, merged into three:** a reading reviewer (Bible and Creativity and Presentation,
   which caught the reading faults), a bond reviewer (Investment Strategy and Portfolio Analysis, with the TNA and the
   register), and the red team. They run on alternate rounds; a round in which any core step finds a K1 or K2 failure
   also calls the bond reviewer.
3. **Client Knowledge folds into the killer list and one role reader.** K1 already checks every case fact against the
   case; a co-sponsor reader reads 3d only, in rounds 6-9 (the co-sponsor text's phase).
4. **Three killer items added:** K8, every ask in CASE_MAP section E is answered on the page (six reviewers named the
   missing range, which in the report would be fatal); K9, "we" per 100 words in each part (voice round 19: 0.9 and
   0.4 against Caplet's IPS); K10, every name a part uses is set up in that part or earlier (round 19's stops were
   "the floor" and IBTM unexplained).
5. **Consolidation rule:** points are ranked by how many reviewers named them, except that any K1 (number) or K2
   (contradiction with what was submitted) failure is fixed whatever its count, since F1 was raised by only half the
   reviewers.
6. **Timing by the lead's clock**, never the reviewers' (one gave a finish 90 seconds late; the fresh reader could not
   separate start from finish).
7. **Reviewers run on Sonnet** with one page of rubric, not the whole of EXPECTATIONS: every planted fault was found
   at least four times, and the main model's budget goes to the writers.
8. **Fault seeding twice (rounds 3 and 8):** two known faults planted in a copy the reviewers see, the writer keeps the
   clean text; if a core step misses a seeded fault at the report's full length, the rotating reviewers run every
   round from then on (error seeding, Mills 1972: the share of seeded faults found estimates the share of real ones
   found).

What the rehearsal could not test: the report's length, the writer's rewrite, and the phases (structure, then
evidence, then sentences). Day 19's pre-mortem takes those.
