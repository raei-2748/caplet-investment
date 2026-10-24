# Runbooks: how each Keel room works (Keel may edit these)

One file per scheduled task. Since Sun 25 Oct 2026 the scheduled-task prompt only points here, so Keel changes how a
room works by committing to its runbook (through `../SELF_IMPROVEMENT.md`), not by asking a human to rewrite a prompt.

**The pointer prompt** (the same for every task; only the room name and runbook change):

> You are Team Keel's scheduled run for <ROOM>, repo raei-2748/caplet-investment. Use today's Sydney date. Check out
> today's day branch `claude/keel-loop-YYYY-MM-DD` (create it from `main` if it doesn't exist). Read
> `keel/pm/INVARIANTS.md`, then `keel/pm/SELF_DIRECTION.md`, then `keel/pm/runbooks/<file>.md`, and follow them.
> Label all output "(Keel is a simulated team, AI-written.)".

Shared rules every run follows: `../SELF_DIRECTION.md` (picking work, requests, questions for humans),
`../../TOKEN_RULES.md`, `../../VOICE.md`, `../../NORTH_STARS.md`.
