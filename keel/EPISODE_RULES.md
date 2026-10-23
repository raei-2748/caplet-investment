# FICTION. Team Keel: episode rules (headquarters page: `keel/README.md`)

**FICTION, AI-generated (Claude Code), started 22 Oct 2026 at Ray's request.** Keel is an imaginary team of six
students in Sydney (`WORLD.md`). They work on the same competition, the same client (Laura Gao), the same deadlines and the same
Wharton files as Caplet. They are written as a team we are confident would reach the semifinals or the finale.
Every day a new episode shows what they did: research, debates, mistakes, decisions.

A keel is the part of a boat that keeps it upright under sail. That is the team's idea of Laura's portfolio: the
payments are the keel, growth is the sail.

## Why it exists
- **A mirror.** Keel runs into the same problems as Caplet a day or two earlier and shows a strong way through.
  Each episode ends with **"What Caplet can take from today"**: concrete checks for our own work.
- **A voice.** Each Keel member has a personality and a way of arguing. Caplet's writing came out generic partly
  because no one in the AI record had a point of view. Keel members do.
- **Real research inside a story.** The story is invented; the research is not. Every fact, rule and number in an
  episode is real, dated and sourced, or is marked MODEL or UNVERIFIED.

## Hard rules for every episode
1. **Label.** Every file starts with "FICTION" in its first line. Keel is not a real team; its members are not
   based on Caplet members or anyone real. Never map a Keel member onto a Caplet student, and never rank Caplet
   students.
2. **Never copy Keel's story into Caplet's deliverables as Caplet's experience.** Wharton's ethics rule bans
   invented teamwork and experience stories. Keel's *research findings* may be used (re-check them first); Keel's
   *events* never are.
3. **Real research only.** Facts, rules and numbers come from:
   - Wharton's official files in `competition/official/2026_27/` (in the story this is the team's shared Google Drive
     folder "Wharton official"), quoted exactly with file and line;
   - public primary sources fetched that day (URL + date), e.g. treasury.gov, fund fact sheets, Taiwan DGBAS;
   - numbers computed by code that day (say MODEL and give the inputs).
   In the story, Keel keeps its own plan and numbers and does not copy Caplet's; in office work for Caplet, Keel reads Caplet's files (see `keel/README.md`).
4. **Same calendar as Caplet, Sydney time first.** TNA Sat 24 Oct 08:00; IPS + trading freeze Sat 7 Nov 09:00;
   Final Report instructions Tue 10 Nov 01:00; Final Report Sat 5 Dec 09:00 (all Sydney).
5. **Keel obeys the 2026-27 rules.** Only WInS-listed stocks, ETFs and Treasury bonds; no TIPS, STRIPS, margin,
   shorting, crypto or derivatives (Week 4 email). WInS profit is never added to Laura's projections.
6. **Characters stay in character** (see `members/<name>.md`), and they disagree for real. They are allowed to be wrong; the
   story shows how they find out.

## Daily episode recipe (for the scheduled session)
1. Read `TOKEN_RULES.md`, then `CAST.md`, `VOICE.md`, `WORLD.md`, `tea_room.md`, `episodes/INDEX.md` and the summary blocks of
   the last two episodes. Open a full `members/<name>.md` only for the 1-3 members central to today. Check
   `ARCS.md` and `IDEAS.md` for the arc to move and any idea already decided. Look up `CLAUDE.md` and
   `competition/COMPETITION.md` for the calendar only.
2. Work out today's date in Sydney and where the competition calendar is. Pick **one** event that a strong team
   would plausibly face today: a rule question, a research question, a draft review, a disagreement, a market move,
   a deadline task. Prefer what Caplet is about to face in the next few days.
3. Do the research for real, through the backstage crew (below): read the official file, fetch the page, run the
   numbers. Keep a source list.
4. Write `episodes/YYYY-MM-DD_epNN.md` as a diary episode, 700-1,000 words (NN = the next number in `INDEX.md`):
   - title; date (Sydney), point of view, Long Room (none / light / N room days, and why), countdown;
   - a `> **Summary.**` block of 3-5 lines, then `**Arcs:** **Values:** **Ideas:**` (later sessions read only this);
   - at least one arc moved by one step, at least one value kept, tested or broken; if a concept is debated, a new
     row in `IDEAS.md` with its verdict and reason;
   - most of the day in ordinary time (school, the bus, home), as real teenagers live it; time in the Long Room
     follows `WORLD.md`;
   - the story, with dialogue in each character's voice;
   - **Decisions** (decision, owner, date) and **Open threads**;
   - **What Caplet can take from today** (2-5 specific checks, each pointing at a Caplet file or deadline);
   - **Sources** (file:line, URL + access date, MODEL inputs).
5. Add the episode's row to `episodes/INDEX.md`, update the arc's "Where it stands" line in `ARCS.md`, the Long Room
   log and current state in `tea_room.md`, and `CAST.md`'s "Current state" if it changed.
   Update `tea_room.md` (plan, decision journal, open threads, relationships) and the "Working notes" section of
   each involved member's file (Felix's quotes, Jun's numbers, Amara's case lines, Kai's market watch, Tess's cut
   lines, Nora's one sentence).
6. Commit and push. Episodes are fiction; the research inside them is logged as AI use for the Works Cited.

## Backstage crew (how the work gets done; never shown)
Each Keel member leads a small crew of subagents that does that member's part of the day's work, so the research
and arguments are deeper than one writer could make them. The crew is backstage only: **never mention subagents,
agents, crews or AI helpers in an episode, in `tea_room.md`, in any member's working notes, or in any report or
reflection.** Only this file, `keel/README.md` and the "Agent profile" section of each member file describe the method. In the story, each member
simply did the work.

| Member | Leads (agent types in `.claude/agents/`) | Brings back |
|---|---|---|
| Nora (leader) | `coherence-checker`, `mock-judge` | does today's work fit the one-sentence strategy; how a judge would read it |
| Amara (client) | `case-analyst`, `cosponsor-reader` | what the case actually says; how Laura and co-sponsors would hear it |
| Jun (numbers) | `ladder-pricer`, `scenario-modeller`, `numbers-auditor` | today's numbers, re-derived a second way, labelled MODEL |
| Kai (contrarian) | `devils-advocate`, `trade-checker` | the strongest case against today's position; any trade issue |
| Felix (rules) | `rules-verifier`, `fact-checker` | exact official quotes with file:line; every fact re-checked |
| Tess (editor) | `format-gatekeeper`, `evidence-archivist` | word counts, banned items, what the record shows |

Daily method:
1. Pick the day's event (recipe step 2). Decide which members it involves; crews only for the 1-3 whose part needs new research.
2. For each involved member, run ONE subagent of the most relevant type above, using the brief in the "Agent
   profile" section of that member's file, with the day's question and the README hard rules. Ask it to answer in that member's voice and position, with
   sources. Run them in parallel. Keep the total to 3 subagents a day or fewer, and none on a day that needs no new research (`TOKEN_RULES.md`).
3. Each crew's findings go into its member's "Working notes", written as that member's own notes.
   Write the episode from what came back: the members disagree where their crews disagreed. Felix's crew
   (`fact-checker`) checks the finished episode's facts and numbers before it is committed.
4. Anything a crew could not verify stays UNVERIFIED in the story, or is cut.

## Files
```
EPISODE_RULES.md   rules, daily recipe, backstage method (headquarters page: README.md)
WORLD.md, CULTURE.md, CAST.md, ARCS.md, IDEAS.md, TOKEN_RULES.md   setting, values, cast, arcs, ideas, token rules
tea_room.md    the shared tea room: plan, decision journal, open threads, relationships
members/       one file per member: profile, agent profile, working notes
episodes/      one diary file per day; INDEX.md is the timeline
```
Members: Nora Haddad (team leader) · Amara Singh (client lead) · Jun Park (numbers) · Kai Tran (contrarian and
trader) · Felix Wong (rules and sources) · Tess Bell (editor and team memory). Episodes use first names.
In the story, `competition/official/2026_27/` is the team's shared drive of Wharton files.
