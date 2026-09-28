# insight_v1: "Leave nothing unconsidered" research run (AI-generated brainstorming)

**What this is.** The output of the locked ultracode prompt v4 (`research/ultracode_prompt_v4_deep_strategy.md`),
run on 2026-09-27 by Claude Code (an AI assistant) as a multi-agent research program for Team Caplet. It stress-tests
the provisional "lock early" strategy for the 2026-27 client Laura Gao and turns what it finds into ranked,
evidence-backed proposals **for the team to approve or reject**.

**AI-use statement (Wharton policy).** Everything in this folder is AI-generated research and brainstorming. None of
it is submission-ready text, and none of its wording may be pasted into the Trading Notes, IPS or Final Report. If the
team uses an idea from here, the Final Report should credit AI assistance (Claude Code) as Wharton's AI policy
requires. The six students make every decision and write every deliverable.

## How the run works
| Phase | Folder | What happens |
|---|---|---|
| Setup | `_context/` | `brief.md`: the single context file every agent reads first |
| A Foundations | `phase_A/` | case register (every official requirement quoted), fact register, stakeholder map, WInS week-1 guardrails |
| B Questions | `phase_B/` | 8 lenses x 2 agents generate anchored questions (plus Laura's own words) |
| C Filter | `phase_C/` | dedupe, then so-what / anchor / adversarial (2 of 3 skeptics) / simplicity tests; counts logged |
| D Research | `phase_D/` | specialists answer surviving questions with sources and Python; auditors re-check |
| E Integration | `phase_E/` | strategy architect, red team (judge, Laura, rival), pre-mortem, chief strategist |
| F Completeness | `phase_F/` | critic loop until two rounds add nothing new |
| Outputs | this folder | the 12 files listed in v4 Part 7 |
| Scripts | `scripts/` | every Python model used; run with `.venv/bin/python` from the repo root |

## Status labels used everywhere
- **VERIFIED-PRIMARY**: read on the primary source (URL + access date given).
- **VERIFIED-REPO-FILE**: from an official or primary file in this repo (path given).
- **SNIPPET-UNVERIFIED**: from a search snippet or secondary source; not confirmed on the primary page.
- **ASSUMPTION**: a modelling or judgement input we chose, with the reason.
- **PARAPHRASE-UNVERIFIED**: words attributed to a person that could not be confirmed verbatim.

## Source access
See `phase_A/source_access.md`. Network access was widened by the team on 2026-09-27, so primary sites were reachable.

## What this teaches
A research program is only as good as its labels: a number without a source and status is an opinion. Separating
"what the case says", "what we verified", "what we assumed" and "what we think it means" is the habit judges
(and Laura, a statistics graduate) will look for.
