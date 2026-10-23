# Start here (for Caplet teammates)

Welcome. This repo holds everything for Team Caplet's 2026-27 Wharton Global High School Investment Competition
entry: official rules, the client case, our strategy research, the WInS portfolio and the checks we run.

## Read these first (about 20 minutes)
1. [`COMPETITION.md`](COMPETITION.md): every rule, date, format and where we stand. **Single source of truth.**
2. [`competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf`](competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf): the client case.
3. [`caplet/google_drive/ips_report/`](caplet/google_drive/ips_report/): our IPS drafts (Version 5 is the latest) and
   all 15 WInS trade notes, verbatim.
4. [`caplet/Winning Team Portrait and Scoresheet.md`](caplet/Winning%20Team%20Portrait%20and%20Scoresheet.md): what the
   judges reward, and a self-scoresheet.

## What's where
| Folder | What it holds |
|---|---|
| `competition/` | Official Wharton materials (PDF + text), public SMApply page snapshots, market data, last year's materials |
| `caplet/` | Our work (the six students): Google Docs/Sheets exports, IPS PDF drafts, AI exemplars (not for submission), scoresheet |
| `keel/office/` | The Caplet Research Office: AI desks that answer a named student's question with a check, a number or a list of problems (`/office` in Claude Code). Start with `keel/office/README.md`; one workstream file per deliverable in `keel/office/workstreams/` |
| `keel/routines/` | Scheduled checks: portfolio monitor, rules watcher, mock judges, evidence lab, and their reports |
| `keel/library/` | AI strategy research (insight_v1, council). Files marked with a 2026-10-14 banner predate the "WInS-only" rule |
| `archive/rab/` | Research-and-build kit: models, verification, numbers |
| `archive/model/laura/`, `caplet/decisions/` | Laura cash-flow model and decision log |
| `keel/` | **Team Keel**, the six simulated contestants who lead this repo: they run the office, set the agenda (`keel/road_to_semifinal.md`) and draft; the students vote and submit. Start with `keel/README.md` |
| `archive/` | Superseded material (25 Sep session brief, old strategy brief) |
| `toolkit/src/`, `toolkit/tests/` | The `wharton-ic` Python toolkit (`pytest` to run the tests) |

## Ground rules
- **AI drafts when asked, the team writes the final words** (Ray, 22 Oct). Claude drafts labelled "AI DRAFT"; we
  rewrite in our own words before submitting. Wharton requires every AI use to be cited in the Final Report.
- **Deadlines are in Sydney time first.** TNA Sat 24 Oct 08:00; IPS Sat 7 Nov 09:00; Final Report Sat 5 Dec 09:00.
- **Only Ray places or cancels WInS trades.** The portfolio plan is "hold"; talk to the team before any trade.
- **Edit the live Google Docs**, not the exports in `caplet/google_drive/` (those are snapshots from 14 Oct).
- The repo is **private** (since 23 Oct). Still don't commit passwords, emails, birthdays or full surnames.

## Using Claude with this repo
The team uses one AI system, the **Caplet Research Office** (`keel/office/README.md`).
- **Claude Code** (terminal, desktop or claude.ai/code), opened in this repo, loads the 18 office agents and the
  house rules automatically. Ask questions like this:
  `/office rates analyst: what is the room under $300k on the 16 Oct close? | decides: IPS certainty sentence | by: Tue 27 Oct`
  Use your role, not your name. Answers arrive as one-page memos in `keel/office/outbox/`.
- **Claude app or claude.ai chat**: paste `keel/office/CLAUDE_APP_PROMPT.md` into the chat first, or into a Claude
  Project's instructions, so Claude follows the same rules.
- With either one, Claude will not write your reflections, IPS or report. That is Wharton's AI policy, not a bug.
  Log any AI use you make outside the office in `keel/office/LEDGER.md` or `caplet/docs/AI_USE.md`.

## Using the repo
```bash
git clone https://github.com/raei-2748/caplet-investment.git
```
```bash
cd caplet-investment && python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
```
```bash
.venv/bin/python -m pytest -q
```
Work on a branch and open a pull request (`git checkout -b yourname/topic`). To push, Ray needs to add your GitHub
username as a collaborator.

## Next deadlines
- **Trading Notes Analysis: Sat 24 Oct 08:00 Sydney** (Fri 23 Oct 5 pm ET)
- **IPS + trading freeze: Sat 7 Nov** (Fri 6 Nov ET)
- Final Report + school letter: Sat 5 Dec 09:00 Sydney (Fri 4 Dec 5 pm ET)
