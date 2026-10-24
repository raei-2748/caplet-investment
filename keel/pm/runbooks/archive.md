# Runbook: The Archive

> Keel may edit this file (Ray, 25 Oct 2026). Change it only through the Sunday "Keel on Keel" step
> (`../SELF_IMPROVEMENT.md`) or when a run finds a rule here that is plainly broken; log every change in
> `../SELF_CHANGES.md`. Rules in `../INVARIANTS.md` win over anything here. Scheduled task: **Keel room: The Archive**, daily 19:10 (Sydney).

## Job
Records: every submitted item (trading notes, TNA reflections) held word for word; check that all new repo work since the last run is consistent with them and with the narrative spine, and list any contradiction; make sure every AI use since the last run has a LEDGER row. **Then the day's merge:** merge today's day PR into `main` if `../INVARIANTS.md` section 3 allows; if not, split the non-keel files into a PR for Ray.

## Files
`../../rooms/archive.md`, `../../office/LEDGER.md`, `../routines/keel-tess-records.md`

## Every run
1. Read `../INVARIANTS.md`, then `../SELF_DIRECTION.md` (how to pick work), then this page.
2. Read the top two rows of `../SCORECARD.md`: aim at one of the two lowest scores unless an open request to this room is more urgent.
3. Do the job above. One page of real output.
4. Add one line to `../RUNLOG.md` (format at its top).
5. Commit to the day branch (fetch and rebase just before pushing; other rooms push there too) and open or update the day's PR. Only the Archive and the daily loop merge (`../INVARIANTS.md` section 3).

## Room rules (Keel's own, editable)
- The Archive is the last room of the day, so it merges. The 07:00 loop sweeps anything it missed.

## Change log
| Date | Change | Why (evidence) |
|---|---|---|
| Sun 25 Oct 2026 | Runbook created from the scheduled-task prompt of 24 Oct | Prompts become 4-line pointers; Keel can now edit how it works |
