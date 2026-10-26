# Ideation ladder: how Keel looks for an idea (Ray, 23 Oct 2026)

Ray's method for brainstorms, debates and "aha" hunts: quantity first on a light model, then go deeper only if
nothing good came out. Every kept idea records the rung that produced it. Caplet still decides; this is Keel's
working method, not a deliverable.

## Two standards (Ray, 23 Oct)
- **Ideas: a scalpel.** Insights are cheap. An idea reaches a deliverable only if it ticks a judging criterion or an
  official requirement (`keel/library/ips_road_2026-10/03_CRITERION_MAP.md`); everything else is cut.
- **Writing: nuance.** Voice, growth, teamwork and values are the scarce part, and the reason Keel is a simulation.
  The episodes give the six real dynamics (disagreements, small wins, people changing their minds) so Caplet's
  writing carries learning and collaboration. The ladder is for ideas; the episodes are for voice.

## The three rungs
| Rung | Model | Job | Output |
|---|---|---|---|
| 1. Wide | Haiku 5.5 (`claude-haiku-5-5`) | Quantity. Many ideas, outside the box, persona voices arguing, analogies from anywhere (cooking, birds, sport, weather) | 30-50 one-line ideas, each with the one fact it rests on |
| 2. Deep | Sonnet 5.5 (`claude-sonnet-5-5`) | Only if rung 1 has no keeper. Narrow to the 5 best, push each further, kill the weak | 3-5 developed ideas, each with the strongest objection |
| 3. Far | Opus 5.5 (`claude-opus-5-5`) | Only if rung 2 has no keeper. Wide reading, unexpected cross-domain connections, combinations of two ideas that react well | 1-3 ideas, each traced to sources |

## The filter (applied by Nora after every rung, before escalating)
An idea is a **keeper** only if all four hold:
1. **It explains a real mechanism** of Laura's plan (the analogy maps part for part; a judge could not say "so what?").
2. **It rests on the case or a verified fact** (case line, official file, sourced number). No invented events.
3. **It fits the spine** (`keel/library/ips_road_2026-10/00_SPINE.md`) and contradicts no locked line.
4. **It survives Kai** ("who says?") and Amara ("would Laura underline it?").
A recipe that teaches something about birds is fine if it makes sense; a clever image that maps nothing is a gimmick.
No keeper: escalate one rung. Keeper found: stop (token rule). Never force an aha; "nothing yet" is a valid result.

## Running it
- One subagent per rung, `model` set as above; brief it with the question, the spine and the filter, nothing else.
- Quiet period (CHARTER 4, until 7 Nov): use the ladder only on wording and framing of what is already decided
  (pitch idea, analogies, debate positions), not on new strategy research.
- Record each run in `keel/office/ideation_log.md`: question, rung reached, keepers (with their rung), and what was
  killed and why. Keepers can surface in episodes and meetings as the team's own discoveries.
