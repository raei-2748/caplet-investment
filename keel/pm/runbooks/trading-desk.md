# Runbook: The Trading Desk (markets and rules check)

> **Read `../../BIBLE.md` first: eight books, all equal (Caplet's five, 23-26 Oct 2026, and Wharton's three official files of 27 Oct).** They beat every rule on this page.
> Extraordinary above all; a distinctive, deeply human voice (Ahaan's, never AI's); one subtle motif, Caplet XR (extended
> release; X = 10; R never "release"); breathtaking investing knowledge, applied, not name-dropped; no hedging; and the
> IPS rewrite is slow, deep thinking, never rushed. No work is finished until the portal shows it.

> Keel may edit this file (Ray, 25 Oct 2026). Change it only through the Sunday "Keel on Keel" step
> (`../SELF_IMPROVEMENT.md`) or when a run finds a rule here that is plainly broken; log every change in
> `../SELF_CHANGES.md`. Rules in `../INVARIANTS.md` win over anything here. Scheduled task: **Keel markets and rules check**, Tue-Sat 10:30 (Sydney).

## Job
Jun fetches the latest US Treasury par curve and reprices the ten $50k payments with the existing ladder script (`../../scripts/ladder_history.py` once it is on `main`, else `../../scripts/ladder_pv.py`), then updates `../RISKS.md`. Felix checks the portfolio and any planned trades or drafts against every Wharton rule and email in `competition/` (banned assets such as TIPS and STRIPS, position limits, trade counts, deadlines, AI-use disclosure, the trading lock on Sat 7 Nov 09:00 Sydney), citing the rule page or email for each item. Any breach or near-breach goes at the top, with what Caplet must do and by when.

## Beat in the loop (from Wed 28 Oct 2026; method: `../../loop/README.md`)
**Beat 3, Markets (Tue-Sat 10:30).** The check below is unchanged. Add a line to today's round file only
if a market or rules fact bears on today's question (for example, a curve move that changes the champion's number).
Otherwise write nothing in the round: silence is fine here.

## Files
report `../../office/checks/YYYY-MM-DD.md` (create the folder if missing), `../RISKS.md`, the newest `../../../competition/wins/*_snapshot.md` (added by PR #22; until it is on `main`, read it from that PR's branch, and if there is no snapshot say so and skip the portfolio check)

## Every run
Follow the shared steps in `README.md` ("Every run, every room"): day branch, read the instruction register, pick
work (work order, request, project step, own idea; never wait for a human), do it, update this room's `## Now` block,
log, push, refresh the dashboard, one line in the thread. This page only adds the room's own job and rules.

## Room rules (Keel's own, editable)
- Be strict: last year the team broke the rules.
- Read only. Use the newest snapshot, never WInS itself (unattended runs have no browser; a WInS look is a question for Ray in `../ASK_HUMANS.md`).
- When the ladder cost moves, update the figure in `../../ips_rewrite/00_GROUND_TRUTH.md` section 5 and add a `../CHANGES.md` row if a draft quotes it.

## Change log
| Date | Change | Why (evidence) |
|---|---|---|
| Sun 25 Oct 2026 | Runbook created from the scheduled-task prompt of 24 Oct | Prompts become 4-line pointers; Keel can now edit how it works |
| Mon 26 Oct 2026 | Shared steps moved to `README.md`; job and rules brought in line with `../../INSTRUCTIONS.md` (Claude, at Ray's request) | Ray, 26 Oct: Keel was not applying his 24-26 Oct instructions |
| Tue 27 Oct 2026 | "Beat in the loop" added: this room's beat in the daily research round (`../../loop/README.md`) (Claude, at Ray's request; not a Keel self-change) | Ray, 27 Oct: scheduled tasks "should not be repetitive"; every round must differ and scout widely |
