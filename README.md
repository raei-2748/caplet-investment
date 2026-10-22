# Team Caplet

Our working repo for the Wharton Global High School Investment Competition 2026-27. Client: Laura Gao.

**New here?** Read [`START_HERE.md`](START_HERE.md) (10 min), then [`COMPETITION.md`](COMPETITION.md), the single source
of truth for every rule, date, format and where we stand. Claude sessions read [`CLAUDE.md`](CLAUDE.md) first.

## Deadlines (Sydney time)
| Due | What |
|---|---|
| Sat 24 Oct 08:00 | Trading Notes Analysis |
| Sat 7 Nov 09:00 | IPS (an SMApply form) · trading ends, portfolio locks (last U.S. fill 08:00) |
| Tue 10 Nov 01:00 | Final Report instructions released |
| Sat 5 Dec 09:00 | Final Report + school documentation |

## Where things are
| Folder | What it holds | Start with |
|---|---|---|
| `competition/` | Official Wharton files (PDF + text), Wharton emails, SMApply snapshots, market data, last year's materials | `competition/official/2026_27/` |
| `team/` | Our own work: Google Docs/Sheets exports (snapshots; the live Docs win), IPS drafts, scoresheet | `team/google_drive/ips_report/` |
| `office/` | The Caplet Research Office: 18 AI agents that check work, numbers and rules; `/office` in Claude Code | `office/README.md` |
| `.claude/` | The agent definitions, the `/office` skill and workflows | `.claude/agents/` |
| `mirror_team/` | Team Keel: a fictional mirror team; one research-based episode a day, each ending with checks for Caplet | `mirror_team/README.md` |
| `research/` | AI strategy research: assistant reviews, blueprints, 2031 range model, IPS numbers, insight_v1, council | `research/assistant_review_2026-10/README.md` |
| `rab/` | Root-and-Branch kit: models, numbers, verification, decisions (30 Sep run) | `rab/RUN_PLAN.md` |
| `decisions/`, `deliverables/`, `model/laura/` | 25 Sep session: decision log D1-D8, deliverable outlines, Laura cash-flow model | `decisions/LOG.md` |
| `ops/` | Scheduled checks (portfolio monitor, rules watcher, mock judges, lab) and their reports | `ops/README.md` |
| `docs/` | AI-use log, governance and method notes, the old toolkit README | `docs/AI_USE.md` |
| `archive/` | Superseded material kept for the record | |
| `src/`, `tests/`, `config/`, `prompts/`, `data/`, `outputs/`, `literature/` | The September `wharton-ic` Python toolkit and its inputs (an early demo; `pytest` runs its tests). `config/client_mandate.yaml` and `config/wharton_*` are still referenced | `docs/wharton_ic_toolkit_README.md` |

## House rules (short version)
- AI drafts when asked, labelled **AI DRAFT**; the team rewrites in its own words and submits. Every AI use is logged
  for the Works Cited (`docs/AI_USE.md`, `office/LEDGER.md`).
- Only Ray places or cancels WInS trades. Only WInS-listed stocks, ETFs and Treasury bonds; no TIPS or STRIPS.
- Facts come from official Wharton files or dated primary sources; anything else is UNVERIFIED.
