# Runbook: The Noticeboard (Keel daily loop)

> **Read `../../BIBLE.md` first: Caplet's five books, all equal (23-26 Oct 2026).** They beat every rule on this page.
> Extraordinary above all; a distinctive, deeply human voice (Ray's, never AI's); one subtle motif, Caplet XR (extended
> release; X = 10; R never "release"); breathtaking investing knowledge, applied, not name-dropped; no hedging; and the
> IPS rewrite is slow, deep thinking, never rushed. No work is finished until the portal shows it.

> Keel may edit this file (Ray, 25 Oct 2026). Change it only through the Sunday "Keel on Keel" step
> (`../SELF_IMPROVEMENT.md`) or when a run finds a rule here that is plainly broken; log every change in
> `../SELF_CHANGES.md`. Rules in `../INVARIANTS.md` win over anything here. Scheduled task: **Keel daily loop**, daily 07:00 (Sydney).

## Job
Nora runs `../LOOP.md`: groom the board, pick the single highest-value piece of work Keel owns (an open request to the Noticeboard first, then the best card by Impact x Urgency, which may be Keel's own new idea), do it in one page, file or close requests, propose up to 3 cards. Then the morning brief and the day's short episode.

## Files
`../BOARD.md`, `../STANDUP.md`, `../REQUESTS.md`, `../ASK_HUMANS.md`, `../../office/outbox/`, `../../episodes/`

## Every run
Follow the shared steps in `README.md` ("Every run, every room"): day branch, read the instruction register, pick
work (work order, request, project step, own idea; never wait for a human), do it, update this room's `## Now` block,
log, push, refresh the dashboard, one line in the thread. This page only adds the room's own job and rules.

## Room rules (Keel's own, editable)
- **Day branch first:** merge yesterday's day PR into `main` (`../INVARIANTS.md` section 3; non-keel files to a separate PR for Ray), then create today's `claude/keel-loop-YYYY-MM-DD` from `main` and push it before anything else. If yesterday's PR can't be merged, branch from yesterday's day branch instead, so no work is lost.
- **Watchdog** (`../SELF_IMPROVEMENT.md` section 3): check `../RUNLOG.md` for every room due yesterday; the brief opens with the health line.
- **Morning brief:** first line: what changed in what the judges will see since yesterday (`../CHANGES.md`; say plainly if nothing did) and the dashboard link (https://claude.ai/artifact/NTBamRzChW4niBLYpkm19M). Then Nora opens in 2-4 plain sentences (what the team decided and did); then Felix, Jun, Kai, Amara and Tess each give a labelled take, 1-3 sentences in their own voice (real views, disagreement allowed); then "Students need to:" as suggestions they can override ("Unless you say otherwise, we will ... by ..."); then "Open questions:" each with Keel's default (also in `../ASK_HUMANS.md`); then the PR link; then "(Keel is a simulated team, AI-written.)". Save at the top of `../STANDUP.md` and post it exactly as written in the daily loop's thread (this is the one long message Keel posts each day).
- **Episode:** Sydney Year 11 students in real Sydney life, never another planet; real research, debate, disagreement, votes; aha moments only if earned. Ideation ladder Haiku 5.5 -> Sonnet 5.5 -> Opus 5.5. Rules in `../../EPISODE_RULES.md`.

## Change log
| Date | Change | Why (evidence) |
|---|---|---|
| Sun 25 Oct 2026 | Runbook created from the scheduled-task prompt of 24 Oct | Prompts become 4-line pointers; Keel can now edit how it works |
| Mon 26 Oct 2026 | Shared steps moved to `README.md`; job and rules brought in line with `../../INSTRUCTIONS.md` (Claude, at Ray's request) | Ray, 26 Oct: Keel was not applying his 24-26 Oct instructions |
