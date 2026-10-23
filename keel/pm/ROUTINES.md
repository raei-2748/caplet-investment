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

## Live: one scheduled task per office room (set up 24 Oct 2026, Sydney; Ray asked that every room take initiative)
Rooms are in `keel/OFFICE.md` (PR #27). Each new room task starts a fresh session, writes only to the repo on
`claude/keel-loop-YYYY-MM-DD` (fetch and rebase first; several rooms push there on the same day), does at most one
item, may say "nothing new" and stop, and ends any memo with one labelled take per member ("Jun: ...") so the 07:00
morning brief can quote every teammate. Push and email notifications are off. All stop after Sat 5 Dec 2026.
Times are Sydney (AEDT); no two runs overlap on the same day.
| Room | Who | Scheduled task | When (Sydney) | Runs/week |
|---|---|---|---|---|
| The Noticeboard | Nora | Keel daily loop (existing) | Daily 07:00 | 7 |
| The Trading Desk | Kai, Jun, Felix | Keel markets and rules check (existing) | Tue-Sat 10:30 | 5 |
| The Window | Felix | Keel room: The Window | Mon, Thu 08:40 | 2 |
| The Library | Felix, Kai | Keel room: The Library | Tue, Fri 13:10 | 2 |
| The Lab | Jun, Kai | Keel room: The Lab | Wed, Sat 13:10 | 2 |
| Laura's Room | Amara | Keel room: Laura's Room | Mon, Thu 14:20 | 2 |
| The Writing Room | Tess, Amara | Keel room: The Writing Room | Tue, Fri 16:10 | 2 |
| The Courtroom | Kai, Nora | Keel room: The Courtroom | Wed 16:40 | 1 |
| The Long Room | all six | Keel room: The Long Room | Thu 16:40 | 1 |
| The Archive | Tess | Keel room: The Archive (replaces the proposed keel-tess-records) | Wed, Sat 18:10 | 2 |
| The Kitchen | everyone | Keel room: The Kitchen (no episode numbers) | Fri 19:10 | 1 |
| The Rooftop | Tess, everyone | Keel room: The Rooftop | Sun 18:40 | 1 |
The Sunday 17:00 Keel weekly plan (existing) stays. Total: 29 runs a week (16 new). To cut cost, drop the Kitchen,
then run the Window, Library and Laura's Room once a week. The daily episode routine is not live in the cloud; the
Kitchen never writes or numbers episodes.

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
