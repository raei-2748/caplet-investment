# Ultracode prompt v3: "See what 99% of teams miss" (for a NEW session; approved by Ray before launch)

Paste everything below the line into a new Claude Code session started on branch `claude/zealous-turing-l19aqc`
(or after merging it), include the word "ultracode", and paste the team's two client documents after it.

---

ultracode

## Mission
Team Caplet (Wharton Global High School Investment Competition 2026-27) wants to reach the Top 50 semifinals. Our edge
is understanding Laura Gao and her case more deeply than other teams, through sharp questions that surface
anomalies, hidden intent and professional-grade insight, and turning the answers into a stronger strategy.
Read CLAUDE.md first; it holds the rules, official facts, verified numbers and current strategy ("lock early").

## The question engine
Generate questions through several distinct lenses, one agent group each:
1. **Case anomalies**: every unusual word, number, omission or design choice in the official case, IPS and Trading
   Notes instructions, and the deliverables page ("why is this here / why is this missing?"). Seed list:
   "the strategy that Laura ultimately chooses" (a competitive pitch); "not adjusted for inflation"; the separate
   2028 deposit and its income sources; her quote "the only person who needs to believe... is yourself" vs
   co-sponsors who must believe her; WInS P&L excluded; precise year numbering and start-of-year flows; Taiwan
   (USD payments, TWD costs); no values/ESG preference (unlike 2025-26); "not expected to size a contingency fund"
   yet "preserve flexibility"; the 2031 range two years before 2033.
2. **Why Wharton chose Laura**: what she represents; the client trend 2021-2027 (Jordan, Hjemdahl, Ash, Ayoola,
   Barwin, Gao); what the case designers are testing; Wharton's own framing of the competition.
3. **Top professional strategist**: how the best private-wealth / goals-based / liability-driven practitioners
   (e.g. at Goldman Sachs, BlackRock, JPM Private Bank, pension and endowment CIOs) would approach this exact client:
   household balance sheet including human capital, liability hedging, governance and rebalancing rules, behavioural
   coaching, how they present uncertainty to clients and co-funders. Use published frameworks with sources.
4. **Laura's world**: her public professional record, values and work (her books and the lessons in them), and the
   risks around her income (publishing, book challenges, AI and illustration, US-China). Verified facts only; no
   private details; no tokenism.
5. **Co-sponsors and philanthropy**: how foundations and co-funders evaluate a founder's pledge, seed gifts,
   matching, credibility (e.g. List & Lucking-Reiley 2002 seed-money evidence) and what a strong pledge range looks like.
6. **Judges and past winners**: what semifinalists and winners did, what judges said; what "typical strong team"
   submissions will look like this year, and therefore what is genuinely distinctive.
7. **Contrarian**: the strongest case against every current decision (lock early, 60% equity growth sleeve, 2031
   floor + upside, WInS 65/35 mirror, post-2033 flexibility principle).

## Filters (a question survives only if it passes all three)
- **So-what test**: its answer would change a decision, a number, or a sentence in a deliverable (Trading Notes
  Oct 23, IPS Nov 6, Final Report Dec 4). Questions that fail but are good finale Q&A go to a separate bank.
- **Anchor test**: tied to the official case/criteria, or to a verified fact that bears on them.
- **Adversarial test**: at least two independent skeptics fail to show it is trivial, already answered, or wrong.

## Answering
For each surviving question: research it (primary sources first; label search-snippet facts UNVERIFIED; compute in
Python and save scripts), answer it, and state the implication for the strategy and for which deliverable.
Loop: new answers generate new questions; stop when two consecutive rounds add no question that passes the filters.
Then a completeness critic asks what lens or source was not used; anything found becomes another round.

## Rules
- CLAUDE.md working rules apply: official materials and verified data only; no fictional facts; no submission-ready
  prose (specifications, evidence, checklists only); nothing goes to judges without team approval; no personal data
  of students; respect Laura's privacy (professional public record only); do not contact her.
- Primary sites may be blocked by the network policy; report what was blocked rather than guessing.
- No ticker selection (this year's approved list is not available); instrument types only.
- Write outputs only under research/insight_v1/; commit and push; update CLAUDE.md with key results and open items.

## Outputs (research/insight_v1/)
1. Top insights (10-20) ranked by impact: question -> answer -> evidence -> what changes -> which deliverable.
2. Case anomaly register: every anomaly found, its likely purpose, and how the strategy responds.
3. "Why Laura" synthesis: verified facts vs interpretation, and the one-sentence thesis it supports.
4. Professional-practice benchmark: how top practitioners would handle this client vs our strategy; gaps.
5. Strategy change proposals with reasons and side effects (for team approval), and the updated risk list.
6. Finale Q&A bank (questions that failed the so-what test but are good defence practice).
7. Open questions only the team can answer; data still needed; blocked sources.

## Budget
About 30-60 agents, roughly an hour. Scale to the filters, not to a question count.
