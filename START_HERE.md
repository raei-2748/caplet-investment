# Start here (for Caplet teammates)

Welcome. This repo holds everything for Team Caplet's 2026-27 Wharton Global High School Investment Competition
entry: official rules, the client case, our strategy research, the WInS portfolio and the checks we run.

## Read these first (about 20 minutes)
1. [`COMPETITION.md`](COMPETITION.md): every rule, date, format and where we stand. **Single source of truth.**
2. [`competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf`](competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf): the client case.
3. [`team/google_drive/ips_report/`](team/google_drive/ips_report/): our IPS drafts (Version 5 is the latest) and
   all 15 WInS trade notes, verbatim.
4. [`team/Winning Team Portrait and Scoresheet.md`](team/Winning%20Team%20Portrait%20and%20Scoresheet.md): what the
   judges reward, and a self-scoresheet.

## What's where
| Folder | What it holds |
|---|---|
| `competition/` | Official Wharton materials (PDF + text), public SMApply page snapshots, market data, last year's materials |
| `team/` | Our work: Google Docs/Sheets exports, IPS PDF drafts, AI exemplars (not for submission), scoresheet |
| `office/` | The Caplet Research Office: AI desks that answer a named student's question with a check, a number or a list of problems (`/office` in Claude Code). Start with `office/README.md` |
| `ops/` | Scheduled checks: portfolio monitor, rules watcher, mock judges, evidence lab, and their reports |
| `research/` | AI strategy research (insight_v1, council). Files marked with a 2026-10-14 banner predate the "WInS-only" rule |
| `rab/` | Research-and-build kit: models, verification, numbers |
| `model/laura/`, `decisions/` | Laura cash-flow model and decision log |
| `src/`, `tests/` | The `wharton-ic` Python toolkit (`pytest` to run the tests) |

## Ground rules
- **The team writes all deliverables** (TNA, IPS, Final Report). AI output here is research and checking only;
  Wharton requires AI use to be cited in the Final Report.
- **Only Ray places or cancels WInS trades.** The portfolio plan is "hold"; talk to the team before any trade.
- **Edit the live Google Docs**, not the exports in `team/google_drive/` (those are snapshots from 14 Oct).
- The repo is **public**. Don't commit passwords, emails, birthdays or full surnames.

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
