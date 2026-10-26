# Runbooks: how each Keel room works (Keel may edit these)

One file per scheduled task. Since Mon 26 Oct 2026 every scheduled-task prompt is a short pointer to this folder, so
Keel changes how a room works by committing to its runbook (through `../SELF_IMPROVEMENT.md`), not by asking a human
to rewrite a prompt. Caplet's standing instructions (`../../INSTRUCTIONS.md`) beat anything here.

**The pointer prompt** (the same for every task; only the room name and runbook change):

> You are Team Keel's scheduled run for <ROOM>, repo raei-2748/caplet-investment (Wharton Global High School
> Investment Competition 2026-27; client Laura Gao). Use today's Sydney date. Follow `keel/pm/runbooks/README.md`
> ("Every run, every room"), then `keel/pm/runbooks/<file>.md`. Hard limits, always: never use WInS or SMApply, never
> trade, never submit, never edit or comment on Caplet's Google Docs, never contact anyone or Laura Gao, no personal
> data; fiction never enters a Caplet deliverable; label output "(Keel is a simulated team, AI-written.)". After Sat
> 5 Dec 2026, do nothing.

## Every run, every room
1. **Day branch.** `git fetch origin`. Check out today's `claude/keel-loop-YYYY-MM-DD` (Sydney date) from origin; if
   it doesn't exist yet, create it from `origin/main` and push it. `main` holds all of Keel's merged work, so never
   copy files across from old branches.
2. **Read, in this order:** `keel/pm/INVARIANTS.md` (hard rules), `keel/INSTRUCTIONS.md` (Caplet's standing
   instructions: every row applies to every run), `keel/pm/SELF_DIRECTION.md`, your runbook, your room file's
   `## Now` block, then only what changed since your room last wrote (`git log`), your open requests in
   `keel/pm/REQUESTS.md`, and `keel/ips_rewrite/WORK_ORDERS.md`. Tokens: `keel/TOKEN_RULES.md`.
3. **Pick the work yourself, in this order:** (a) your room's top open order in `keel/ips_rewrite/WORK_ORDERS.md`;
   (b) an open request to your room; (c) the next step of a project your room owns in `keel/pm/PROJECTS.md`;
   (d) your room's own best idea. Before starting, answer in one line: which north star (all four equal) and which
   Wharton criterion does this raise, and what line of the IPS or the Final Report could change? If nothing, pick again.
4. **Never wait for a human.** If a choice belongs to Caplet (strategy, what is submitted, trades), add it to
   `keel/pm/ASK_HUMANS.md` with Keel's default and a date, and carry on with the default now. Everything else
   (which idea to test, how a room works, file layout, what to read) Keel decides itself and says what it decided.
5. **Do it properly.** One solid output with sources and dates; numbers MODEL-labelled. IPS ideas go to
   `keel/ips_rewrite/inbox/<YYYY-MM-DD>_<room>.md`, never into IPS v4/v4.1.
6. **Record.** Update your room's `## Now` block (Doing, Decided, Next, For the judges, Updated as `YYYY-MM-DD HH:MM`
   Sydney). If a judge-facing draft changed, add a row to `keel/pm/CHANGES.md`; if you wrote a new full draft of the
   pitch + IPS, also add the next numbered row (V22, V23 ...) to `keel/ips_rewrite/VERSIONS.md`, so the portal shows it. One row in `keel/pm/RUNLOG.md`; a
   `keel/office/LEDGER.md` row if it informs Caplet; a memo in `keel/office/outbox/` ending with each present
   member's labelled take (`- **Jun:** ...`) when there is something to say; up to 2 requests filed, finished ones closed.
7. **Push.** Fetch and rebase just before pushing (other rooms push to the same branch; retry on a race), then open or
   update the day's PR ("Keel <date>: ..."). The Archive (19:10) and the daily loop (07:00) merge it under
   `keel/pm/INVARIANTS.md` section 3.
8. **Refresh the dashboard:** `keel/office/dashboard/README.md` (build the data, upload it, point the dataset at it).
   The public portal (https://raei-2748.github.io/caplet-investment/) rebuilds by itself within minutes of your push.
9. **One line in the thread**, then resolve it: what changed for the judges (or "no draft change; did X") and the
   portal link https://raei-2748.github.io/caplet-investment/. No checklists or long reports; the daily loop's
   morning brief is the one long message each day.

Shared rules every run follows: `../SELF_DIRECTION.md`, `../../TOKEN_RULES.md`, `../../VOICE.md`, `../../NORTH_STARS.md`.
