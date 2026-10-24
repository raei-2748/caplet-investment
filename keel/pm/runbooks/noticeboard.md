# Runbook: The Noticeboard (Keel daily loop)

> Keel may edit this file (Ray, 25 Oct 2026). Change it only through the Sunday "Keel on Keel" step
> (`../SELF_IMPROVEMENT.md`) or when a run finds a rule here that is plainly broken; log every change in
> `../SELF_CHANGES.md`. Rules in `../INVARIANTS.md` win over anything here. Scheduled task: **Keel daily loop**, daily 07:00 (Sydney).

## Job
Nora runs `../LOOP.md`: groom the board, pick the single highest-value piece of work Keel owns (an open request to the Noticeboard first, then the best card by Impact x Urgency, which may be Keel's own new idea), do it in one page, file or close requests, propose up to 3 cards. Then the morning brief and the day's short episode.

## Files
`../BOARD.md`, `../STANDUP.md`, `../REQUESTS.md`, `../ASK_HUMANS.md`, `../../office/outbox/`, `../../episodes/`

## Every run
1. Read `../INVARIANTS.md`, then `../SELF_DIRECTION.md` (how to pick work), then this page.
2. Read the top two rows of `../SCORECARD.md`: aim at one of the two lowest scores unless an open request to this room is more urgent.
3. Do the job above. One page of real output.
4. Add one line to `../RUNLOG.md` (format at its top).
5. Commit to the day branch (fetch and rebase just before pushing; other rooms push there too) and open or update the day's PR. Only the Archive and the daily loop merge (`../INVARIANTS.md` section 3).

## Room rules (Keel's own, editable)
- **Watchdog first** (`../SELF_IMPROVEMENT.md` section 3): check `../RUNLOG.md` for every room due yesterday; the brief opens with the health line.
- **Merge sweep:** merge yesterday's day PR into `main` if `../INVARIANTS.md` section 3 allows and the Archive has not done it.
- **Morning brief:** Nora opens in 2-4 plain sentences (what the team decided and did); then Felix, Jun, Kai, Amara and Tess each give a labelled take, 1-3 sentences in their own voice (real views, disagreement allowed); then "Students need to:" as suggestions they can override ("Unless you say otherwise, we will ... by ..."); then "Open questions:" each with Keel's default (also in `../ASK_HUMANS.md`); then the PR link; then "(Keel is a simulated team, AI-written.)". Save at the top of `../STANDUP.md` and post it exactly as written.
- **Episode:** Sydney Year 11 students in real Sydney life, never another planet; real research, debate, disagreement, votes; aha moments only if earned. Ideation ladder Haiku 5.5 -> Sonnet 5.5 -> Opus 5.5. Rules in `../../EPISODE_RULES.md`.

## Change log
| Date | Change | Why (evidence) |
|---|---|---|
| Sun 25 Oct 2026 | Runbook created from the scheduled-task prompt of 24 Oct | Prompts become 4-line pointers; Keel can now edit how it works |
