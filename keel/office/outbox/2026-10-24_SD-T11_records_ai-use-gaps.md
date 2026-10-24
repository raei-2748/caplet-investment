# AI_USE.md says things that are no longer true, and its log stops on 20 Oct: the gap list and the rows to add
AI-generated records check by the Keel Office (Claude Code; Tess = Records). Not for submission. Cite in Works Cited.
Work order: SD-T11 | Asked by: self-directed (board card T11; flagged as near-breach 2 in `keel/office/checks/2026-10-24.md`, PR #28) | Desk: Records (ai-use-recorder role, no subagents) | Date: Sat 24 Oct 2026, 12:00 AEDT
Checked: `caplet/docs/AI_USE.md` (main), `keel/office/LEDGER.md`, git history 1-24 Oct, `CLAUDE.md`. Nothing in `caplet/` was edited.

## Why it matters
Wharton's AI policy (as recorded in `competition/COMPETITION.md` s6; the official clause itself is not yet filed, check
item 3 of the 24 Oct rules check) asks that AI use be recorded in the Final Report's Works Cited. If this file feeds that
disclosure, every untrue line below becomes an untrue statement to the judges. Integrity outranks polish (R-ethics).

## Lines that are no longer true (strict reading)
| Line | It says | What actually happens (source) |
|---|---|---|
| :9 | language models "strictly forbidden from authoring prose intended to be submitted" | Since 21-22 Oct the team asks AI for labelled drafts (`CLAUDE.md`, "For every Claude session"); [AI] suggestions 1-13 were accepted into IPS V5 on 16 Oct (this file, s5 rows of 16 Oct) |
| :10 | AI used "strictly within `wharton-ic`" | `wharton-ic` is the September toolkit's old name; most use since is Claude Code sessions, the Keel Office, Claude Cowork, ChatGPT (29 Sep) and Google Docs suggestions |
| :11 | every action signed in `15_human_decision.md` | No such file in the repo (`git ls-files`, 24 Oct); votes go to `caplet/decisions/LOG.md` |
| :18-19 | models "hard-coded to never calculate" financial arithmetic | Claude Code wrote and ran the ladder, range and Monte Carlo scripts (s5 rows; `keel/library/`) |
| :25 | "Every LLM interaction is logged automatically in `toolkit/outputs/ai_use_log.jsonl`" | That file holds 266 rows of the demo's mock calls (`"provider": "mock_anthropic"`, `"is_mock": true`); no real session is in it |
| :101 | "Students ... wrote all submitted text" | Must be true on 5 Dec, but the IPS carries accepted AI wording unless rewritten (16 Oct rows). The disclosure has to say which |
Section 4 (:47-48) is already honest ("PENDING (team to write)"). Sections 1-3 need the same treatment.

## Rows missing from the log (s5 ends 20 Oct; one line each, ready to paste; all Claude Code unless named)
| Date (Sydney) | What the AI did | Output |
|---|---|---|
| 2026-10-16 | Assistant review 30 Sep-15 Oct, North Star memo, IPS pre-mortem, number checks (AI research, not for submission) | `keel/library/assistant_review_2026-10/` |
| 2026-10-17 | 2031 range model on the WInS-only basis; IBTM payout drift | `keel/library/range_2031/` |
| 2026-10-17/18 | Exemplar v3-v12 of the pitch, IPS and three TNA reflections (a model to learn from), also put into the IPS Report Doc as suggestions in Version 5 and Trading Note Reflection tabs | `keel/library/blueprints/04_exemplar_ips_tna_17Oct.md` |
| 2026-10-19/20 | WO-0002: why V5 would not reach the semifinal; check of rewritten VT and IBTR reflections | LEDGER WO-0002a/b |
| 2026-10-21 | WO-0003 world-stock return projections; WO-0004 final TNA check; WO-0005 TNA criteria and hold check; TNA teardown v1-v2 | LEDGER; `keel/library/assistant_review_2026-10/oct21_tna/` |
| 2026-10-22/23 | Team Keel: six fictional personas, episodes, project office and routines (fiction; research findings re-checked before use) | `keel/` |
| 2026-10-23 | WO-0006: TNA vs Week 4 tips (live Doc read) | LEDGER WO-0006 |
| 2026-10-24 | Keel self-directed runs: ladder reprice (SD-T03), vote set B options (SD-T04), IPS rule checklist (SD-T05), Courtroom, Library, Lab, Long Room motif ladder (Haiku 5.5, Sonnet 5.5, Opus 5.5), TIPS/STRIPS check (SD-R11), this memo | LEDGER rows of 24 Oct |
**One row only the students can write:** which TNA reflection words, submitted 23 Oct, came from an AI draft or
exemplar, and which were their own. Keel cannot know; the row says "students to confirm" until they do.

## For the team (suggestions; you can override)
Unless you say otherwise: (1) Keel's Archive adds the rows above to s5 on **Sun 25 Oct**, at the TNA retro (records
only, no disclosure text); (2) sections 1-3 are rewritten by a student in their own words **by Sat 31 Oct**, before the IPS
AI line is written; (3) the TNA row is filled by whoever wrote each reflection, at the retro.

## Takes for the brief
- **Tess:** Which job is this file doing? If it's the Works Cited source, five of its claims are false today. Facts first, then your words.
- **Felix:** Where does it say "strictly forbidden"? In our own file, not Wharton's. We wrote a stricter rule than the competition's and then didn't follow it. That's the worst of both.
- **Kai:** Nobody loses marks for using AI. You lose them for saying you didn't.
- **Jun:** Line 25 is the one that'd embarrass us: 266 logged calls, every one a mock.
- **Amara:** The TNA row matters most. Only the person who wrote each reflection can say what's theirs.
- **Nora:** Rows on Sunday, the rewrite by Sat 31 Oct, the TNA row at the retro.
