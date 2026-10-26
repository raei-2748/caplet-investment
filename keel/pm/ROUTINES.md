# Scheduled routines

## Existing: ten checks on Ray's Mac (keep; do not duplicate)
Prompts in `keel/routines/tasks/scheduled_tasks/`, instructions in `keel/routines/tasks/`. Schedules live on the Mac.
| Task | What | Keel desk it belongs to |
|---|---|---|
| caplet-rules-watcher | Daily Wharton email / public pages watch; notifies Ray on change | Felix (feeds R11) |
| caplet-wharton-monitor | Twice-weekly portfolio and doc check, curve note | Kai + Jun |
| caplet-tna-final-check, caplet-ips-final-check, caplet-final-report-check | Gate check before each deadline | Felix |
| caplet-judge-tna, caplet-judge-ips, caplet-judge-final-1, caplet-judge-final-2 | Five mock judges per draft | Nora |
| caplet-evidence-lab | One Final Report evidence item per run (Sun/Wed) | Jun + Tess |
The loop reads their reports (`keel/routines/monitor_reports/`) instead of redoing them. Felix's rules watch is
already the Mac watcher, so no cloud copy is proposed.

## Live: one scheduled task per office room (since 24 Oct 2026; pointer prompts since 26 Oct)
Every room has its own scheduled task, daily or every two days (Ray, 23-24 Oct: Keel leads itself). Since Mon 26 Oct each
prompt is a short pointer to `runbooks/README.md` ("Every run, every room") and the room's runbook in `runbooks/`, so
how a room works is changed in the repo, not in the prompt. The live table of tasks, times and runbooks is
`SCHEDULE.md`; rooms are described in `../OFFICE.md`. Each run starts a fresh session (its own thread in the project),
writes to `claude/keel-loop-YYYY-MM-DD` (created from `main` by the 07:00 daily loop), updates its room's `## Now`
block and refreshes the Keel Office dashboard. Push and email notifications are off. All stop after Sat 5 Dec 2026.
The Sunday 17:00 weekly plan stays; the daily episode is written by the daily loop; the Kitchen never numbers episodes.

## Proposed: cloud routines (prompts in `routines/`, each under 2 KB)
AEDT = UTC+11 for the whole competition. All write only to the repo, on a `claude/keel-loop-YYYY-MM-DD` branch with
one PR per day, never merged by Keel. All stop after Sat 5 Dec 2026.
| Routine | Persona | Cron (UTC) | Sydney time | Prompt |
|---|---|---|---|---|
| keel-daily-loop | Nora | `0 20 * * *` | Daily 07:00 | `routines/keel-daily-loop.md` |
| keel-jun-markets | Jun | `30 23 * * 1-5` | Tue-Sat 10:30 (after the U.S. curve is out) | `routines/keel-jun-markets.md` |
| keel-weekly-plan | Nora + Kai | `0 6 * * 0` | Sun 17:00 | `routines/keel-weekly-plan.md` |
| keel-daily-episode | All six (story) | `0 9 * * *` | Daily 20:00 | `routines/keel-daily-episode.md` |
| keel-tess-records | Tess | `0 7 * * 3,6` | Wed and Sat 18:00 | `routines/keel-tess-records.md` |

Token budget: the daily loop and the episode are the two daily runs; the rest are small. If budget is tight, drop
keel-tess-records first (the loop already carries card T11), then run keel-jun-markets on Tue and Fri only.
