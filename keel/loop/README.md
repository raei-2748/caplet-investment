# Out and Back: Keel's research loop (from Wed 28 Oct 2026)

> **Read `../BIBLE.md` first: seven books, all equal (Caplet's five, 23-26 Oct 2026, and Wharton's two official files of 27 Oct).** They beat every rule on this page.
> Extraordinary above all; a distinctive, deeply human voice (Ray's, never AI's); one subtle motif, Caplet XR (extended
> release; X = 10; R never "release"); breathtaking investing knowledge, applied, not name-dropped; no hedging; and the
> IPS rewrite is slow, deep thinking, never rushed. No work is finished until the portal shows it.

> Ray, Tue 27 Oct 2026: the scheduled tasks "should not be repetitive ... It should be a loop ... Nora gathers her
> team to work, after working they find their flaw and they work on it, they judge it, they discuss it, then send off
> and then come back, then go out, come back ... every round, but loop is never repetitive. Because humans have much
> richer experiences, and this gives them much richer exposure and thus creativity ... Agents does not have senses.
> But it does have much stronger access to the internet ... So agents should browse the internet widely and scout for
> interesting ideas to form interesting connections. And thus give a strongest version of IPS ... creativity is
> usually like an unexpected connection." Designed by Claude at Ray's request (thread "Build Keel's self-improving
> research loop"); Keel may improve it through `../pm/SELF_IMPROVEMENT.md`.

## The problem it fixes
Until 27 Oct every room had a fixed job and ran it every day: the Window swept, the Library read two concepts, the
Archive checked locked text. The work was good, but nothing stopped a room from walking the same ground twice, and
nothing made today's round start where yesterday's ended. Research on AI research agents finds the same thing at
scale: left alone, a model repeats itself (of 4,000 ideas one agent generated, only about 200 were not duplicates),
and different models converge on the same answers (the "Artificial Hivemind"). Ray's fear of AI groupthink in Book 2
is a measured effect, not a hunch. The loop below is built to break it.

## One round a day, nine beats
Every Sydney day is one **round**, written into one file, `rounds/YYYY-MM-DD.md` (copy `rounds/TEMPLATE.md`). Each
scheduled run is one beat: it reads the round so far, does its beat, and adds its section. The times are the existing
scheduled tasks; no prompt changes.

| # | Beat (Ray's words) | Who, when (Sydney) | What happens |
|---|---|---|---|
| 1 | **Gather** ("Nora gathers her team") | Noticeboard, Nora, 07:00 | Reads last night's verdict, `LESSONS.md` and `FRONTIER.md`; sets **today's question**, draws a **lens** (`LENSES.md`), assigns three **scouts** to three fields (`TERRITORY.md`), names the **champion** to beat (`CHAMPIONS.md`). Writes the difference test (below). |
| 2 | **Gate** | Window, Felix, 08:40 | Truth-checks everything yesterday's scouts brought back before anyone builds on it: real source, real quote, and the "so" read beside the source. Brings back one primary-source find of his own. |
| 3 | (markets) | Trading Desk, Tue-Sat 10:30 | Its rules and markets check, unchanged; adds a line to the round only if a market fact bears on today's question. |
| 4 | **Go out** ("browse the internet widely and scout") | Library, 12:10 | The expedition. Three scouts, each to their assigned field: one **near** (finance), one **adjacent**, one **far**. Each comes back with 2-3 **finds**: a real source (title, URL, access date, a quoted line), the mechanism in two plain sentences, and a first guess at what it could touch in Laura's plan. |
| 5 | **Come back** ("come back ... form interesting connections") | Genius Lab, Jun (Kai roasts), 13:40 | Lays every find against today's question and forces pairings (find x problem, find x find, find x a binned idea). At least three **challengers** come out; the strongest is tested in the model or against the case. |
| 6 | **Work** ("Nora gathers her team to work") | Laura's Room, Amara, 15:10 | The second angle on the challengers: what a co-sponsor, a judge, or a practitioner from the scouted field would make of them. Kills or sharpens. |
| 7 | **Work** | Writing Room, Tess, 16:20 | Puts each surviving challenger in a form the champion can be compared with: the claim in at most 15 plain words, and, once the voice thread's guide lands, the line in Ray's voice. |
| 8 | **Find the flaw, fix it, judge it, discuss it** | Courtroom, Kai (odd dates) / Long Room, Nora (even dates), 18:20 | Flaw hunt by someone who did not build it; one repair by the builder; then **judged head to head against the champion** by a cold judge; then the members' discussion and a Keel vote: promote, park, or bin. The Courtroom leads with the trial, the Long Room with the argument; both do all four. |
| 9 | **Record** | Archive, Tess, 19:10 | Updates `TERRITORY.md`, `CHAMPIONS.md`, `FRONTIER.md`; moves anything the IPS can use to `../ips_rewrite/inbox/`; merges the day. |
| 10 | **Reflect and send off** ("then send off") | Kitchen (odd) / Rooftop (even), 20:20 | Rooftop: the round's lesson (what went wrong in *how* we worked) into `LESSONS.md`. Kitchen: off-duty talk, where each member says one thing they bumped into outside the competition; anything with a mechanism becomes a field for tomorrow. Both end by writing **tomorrow's scouting orders** in `FRONTIER.md`. |
| - | **Loop on the loop** | Weekly plan, Nora + Kai, Sun 17:00 | Reads the week's rounds and the loop's health numbers; changes at most 3 rules of the loop itself (`../pm/SELF_IMPROVEMENT.md`). |

The order is Ray's: gather, work, find the flaw, fix it, judge, discuss, send off, come back, go out. It runs as a
ring: tonight's send-off is tomorrow's expedition, tomorrow's return is the next round's work.

A deep question may run for more than one round, but never in place: day two must start from day one's endpoint and
go one step further (a new field, a harder test, a sharper claim). That is the "first return, then explore" rule from
Go-Explore: go back to the most promising spot you reached, then explore from *there*, rather than starting over.

## Why no two rounds are the same: five memories
| File | Holds | Borrowed from | How it stops repetition |
|---|---|---|---|
| `TERRITORY.md` | Every field Keel has scouted, when, by whom, what came back, how rich it was | MAP-Elites and novelty search (keep an archive of *where* you've been, not just what scored best) | A scout may not return to a field marked mined; unvisited fields go first; a "promising" field is revisited only with a named deeper question. |
| `LENSES.md` | A deck of ways to look at a problem, with the date each was last drawn | Oblique Strategies; STORM's perspective-guided questions | No lens may be drawn twice in five rounds. |
| `CHAMPIONS.md` | The best-so-far for each part of the IPS (thesis, certainty line, R, the 2031 range rule ...) | autoresearch's keep-or-discard ratchet | A round only counts if it beats or sharpens a champion, or kills a challenger for a reason worth recording. Work that does neither is visible as such. |
| `FRONTIER.md` | Open questions, open flaws, and stepping stones (ideas that lost but left something) | Go-Explore's archive of stepping stones; AI Scientist's idea archive | Tomorrow's question comes from here, so it is always the next unknown, never yesterday's job. |
| `LESSONS.md` | Short lessons about *how* Keel worked, from each round's reflection | Reflexion (an agent writes what went wrong in words and reads it next time); Generative Agents' reflection | The same mistake is made once. A lesson that keeps coming back becomes a runbook rule on Sunday. |

## The difference test (Nora writes it at 07:00; the round stops if it fails)
Before any work starts, the round file states, against the last three rounds:
1. **New question, or a deeper step on an old one** (quote the old round's endpoint and say the step).
2. **New ground:** none of today's three fields is marked mined, and at least one has never been visited.
3. **New lens:** not drawn in the last five rounds.
4. **New hands:** the three scouts, the flaw-hunter and the judge are not yesterday's (rotation table in `TERRITORY.md`).
5. **Novelty check:** each challenger is searched against `../IDEAS.md`, the Lab book, the Library's slips, R02, R05,
   `FRONTIER.md` and the binned list. A near-duplicate must either be dropped or declared a "return" with the new step named.

If a test fails, Nora changes the plan before 08:40; she never writes "same as yesterday".

## The rules that keep it honest (each from a known failure)
- **Every find is real, and checked before it is built on.** The AI Scientist "can hallucinate entire results", and
  one 2026 study of autonomous research agents confirmed 40 fabrications in 1,628 scored runs. So: a find without a
  fetched URL and a quoted line is marked UNVERIFIED and cannot be promoted; the Window gates every find next morning.
- **The builder never judges.** Self-reflection alone stalls once a model is confident ("degeneration of thought");
  debate between agents who disagree fixes some of it. So the flaw-hunter is a different member from the builder,
  the judge is a third, and the flaw-hunter must attack the strongest version of the idea.
- **Judge head to head, not by score.** AI reviewers agree with expert reviewers barely better than chance (the best
  reached 53%, below the 56% two humans manage), and pairwise ranking was the most reliable form. So a challenger is
  never given a mark out of 7 alone: it is read next to the champion, cold, by a judge who has not seen the round,
  and the question is "which would a Wharton judge rather read, and why?". Ray and Caplet's students remain the final judges.
- **Conventional core, one unusual connection.** The most-cited science combines very conventional ideas with one
  atypical pairing (Uzzi et al., 2013, 17.9 million papers). So a promoted idea must rest on sound investing (the
  near field) and carry exactly one surprising link. A far-field idea with no investing core is binned however pretty.
- **Fight the hivemind on purpose.** Different personas, different fields, a rotating lens and the model ladder
  (Haiku 5.5 wide, Sonnet 5.5 deeper, Opus 5.5 for wide reading) are spread across the scouts, so they do not all
  search from the same prompt. Kai's standing rule holds: if a chatbot finds it in ten seconds, bin it.
- **Where an analogy breaks is the finding.** Every far-field find is mapped part for part, and the breaks are written down (Library S-01, S-04).

## How the members go out (Ray: humans have senses, agents have the internet)
The six have lives, and their lives are where human creativity comes from. Each scout goes out through one door
they would really walk through, then one door the map assigns:
- **Nora:** her dad's tiling jobs, the bakery's 6 a.m. proving, netball rotations, her mum's pharmacy.
- **Felix:** clarinet, mahjong scoring rules, train timetables, his mum's audit files.
- **Jun:** engineering, running splits, piano practice, his mum's ICU (triage, reserves, handovers).
- **Kai:** the phone shop (contracts, layaway), basketball, his dad's trading screens, the reading pile.
- **Amara:** tutoring, the gurdwara kitchen (a community fund that feeds anyone, every day), clinic rosters.
- **Tess:** theatre lighting cue sheets, film exposure, the bookshop, court reporting, set-building.

The door is fiction; what comes back through it is not. Every find is a real, fetched source, and no member's life
or the story ever enters a Caplet deliverable (`../pm/INVARIANTS.md` section 2).

## The dial: explore early, deepen late
| Dates (Sydney) | Explore : deepen | Scouts' fields | What the round may change |
|---|---|---|---|
| Wed 28 - Thu 29 Oct | 2 : 1 | near, adjacent, far | ideas and tests for the synthesis (Thu 29) |
| Fri 30 - Sat 31 Oct | 1 : 1 | one far, two to deepen champions | the near-final IPS for Caplet's review (Sat 31) |
| Sun 1 - Thu 5 Nov | 1 : 2 | one far, two verify and deepen | revisions after Caplet's review; nothing new is promoted after Wed 4 Nov |
| Fri 6 - Sat 7 Nov | freeze | none | the IPS is Caplet's; the loop only checks |
| from Sun 8 Nov | 2 : 1 again | the Final Report's sections | the Final Report (due Sat 5 Dec 09:00 Sydney), which can cite everything |

The loop never asks the rewrite for a draft, a word count or a date (`../BIBLE.md` rule 2). It fills the rewrite's
inbox; the rewrite thread decides when the thinking has moved enough to write.

## The loop's health (the Archive fills it nightly, the weekly plan reads it)
`HEALTH.md`, one row a round: fields visited (new / return), finds (verified / unverified), challengers, promoted,
binned, champions changed, lesson written, difference test passed. Warning lights the Sunday review acts on:
- three rounds without a champion change or a kill worth recording: the question is wrong, change it;
- verified finds below half: scouts are skimming, cut to two scouts and read deeper;
- the same field family three rounds running: the map is being gamed, force a far field;
- no far-field find promoted in a week: fine, if the near-field champions moved; if not, the far fields are too far.

## Sources (all accessed Tue 27 Oct 2026)
- Si, Yang, Hashimoto, "Can LLMs Generate Novel Research Ideas?", ICLR 2025, https://arxiv.org/abs/2409.04109: AI ideas
  rated more novel than experts' (5.64 vs 4.84); about 200 of 4,000 seed ideas non-duplicate; best AI judge 53.3%
  agreement with experts, humans 56.1%.
- Jiang et al., "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)", NeurIPS 2025,
  https://arxiv.org/abs/2510.22954: intra-model repetition and inter-model homogeneity.
- Lu et al. (Sakana AI), "The AI Scientist", https://arxiv.org/abs/2408.06292: idea archive, novelty check against
  the literature, automated reviewer; failure modes include hallucinated results and "very similar ideas across different runs".
- Antoniades et al., "Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and
  Novelty" (1 Jul 2026), via https://deeplearn.org/arxiv/784234: six search strategies (greedy, MAP-Elites,
  Go-Explore, islands, curiosity, OMNI); novelty rare; 40 confirmed fabrications in 1,628 scored runs.
- Karpathy, autoresearch (Mar 2026), as described in https://thenewstack.io/karpathy-autonomous-experiment-loop/:
  one editable file, one metric, a fixed time budget, keep or discard each run, `program.md` as the human's lever.
- Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning", NeurIPS 2023, https://arxiv.org/abs/2303.11366.
- Park et al., "Generative Agents: Interactive Simulacra of Human Behavior", 2023, https://arxiv.org/abs/2304.03442:
  memory, reflection and planning each matter.
- Shao et al., "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models" (STORM), 2024,
  https://arxiv.org/abs/2402.14207: research through simulated conversations between different perspectives, grounded in search.
- Du et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate", ICML 2024, https://arxiv.org/abs/2305.14325.
- Liang et al., "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate", EMNLP 2024,
  https://arxiv.org/abs/2305.19118: "degeneration of thought"; a judge; moderate tit-for-tat works best.
- Ecoffet, Huizinga, Lehman, Stanley, Clune, "First return, then explore", Nature 590 (2021), https://arxiv.org/abs/2004.12919.
- Uzzi, Mukherjee, Stringer, Jones, "Atypical Combinations and Scientific Impact", Science 342 (2013),
  https://www.kellogg.northwestern.edu/faculty/research/detail/2013/atypical-combinations-and-scientific-impact.

(Keel is a simulated team, AI-written.)
