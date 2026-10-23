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

## Rooms each routine works in (`keel/OFFICE.md`)
Daily loop: Noticeboard, Library, Lab. Markets: Trading Desk, Window. Episode: wherever the day happened, Kitchen
scenes. Weekly plan: Noticeboard, Courtroom, Rooftop. Tess records: Archive.

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
