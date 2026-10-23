# ops: scheduled checks

Copies (14 Oct 2026) of the routines that run on Ray's Mac in the Claude desktop app. They are read-only checks: they never trade, never message anyone, never edit team docs, and never write submission text.

- `routines/`: instruction files (MONITOR, WATCHER, JUDGE, LAB), `portfolio_check.py`, and `scheduled_tasks/` (the prompt and schedule of each task).
- `monitor_reports/`: twice-weekly portfolio and doc checks, plus `RULES_CHANGES.md` from the daily rules watcher.
- `claude_lab/`: the evidence-lab backlog for the Final Report and the judge-lens brief.

The live copies are in `~/Research/caplet-monitor/` and the team Drive folder; these copies may fall behind. Paths shown as `<Google Drive>` and `<Claude memory folder>` point to Ray's machine.
