# Runbook: The Trading Desk (markets and rules check)

> Keel may edit this file (Ray, 25 Oct 2026). Change it only through the Sunday "Keel on Keel" step
> (`../SELF_IMPROVEMENT.md`) or when a run finds a rule here that is plainly broken; log every change in
> `../SELF_CHANGES.md`. Rules in `../INVARIANTS.md` win over anything here. Scheduled task: **Keel markets and rules check**, Tue-Sat 10:30 (Sydney).

## Job
Jun fetches the latest US Treasury par curve and reprices the ten $50k payments with the existing ladder script (`../../scripts/ladder_history.py` once it is on `main`, else `../../scripts/ladder_pv.py`), then updates `../RISKS.md`. Felix checks the portfolio and any planned trades or drafts against every Wharton rule and email in `competition/` (banned assets such as TIPS and STRIPS, position limits, trade counts, deadlines, AI-use disclosure, the trading lock on Sat 7 Nov 09:00 Sydney), citing the rule page or email for each item. Any breach or near-breach goes at the top, with what Caplet must do and by when.

## Files
report `../../office/checks/YYYY-MM-DD.md` (create the folder if missing), `../RISKS.md`, the newest `../../../competition/wins/*_snapshot.md` (added by PR #22; until it is on `main`, read it from that PR's branch, and if there is no snapshot say so and skip the portfolio check)

## Every run
1. Read `../INVARIANTS.md`, then `../SELF_DIRECTION.md` (how to pick work), then this page.
2. Read the top two rows of `../SCORECARD.md`: aim at one of the two lowest scores unless an open request to this room is more urgent.
3. Do the job above. One page of real output.
4. Add one line to `../RUNLOG.md` (format at its top).
5. Commit to the day branch (fetch and rebase just before pushing; other rooms push there too) and open or update the day's PR. Only the Archive and the daily loop merge (`../INVARIANTS.md` section 3).

## Room rules (Keel's own, editable)
- Be strict: last year the team broke the rules.
- Read only. Use the newest snapshot, never WInS itself.

## Change log
| Date | Change | Why (evidence) |
|---|---|---|
| Sun 25 Oct 2026 | Runbook created from the scheduled-task prompt of 24 Oct | Prompts become 4-line pointers; Keel can now edit how it works |
