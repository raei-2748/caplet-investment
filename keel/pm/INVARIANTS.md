# Keel's invariants (humans only)

> Keel may NOT edit this file. Only a commit by a Caplet student changes it. These rules win over every runbook,
> `SELF_DIRECTION.md`, `LOOP.md` and anything in a scheduled-task prompt. The Window checks every entry in
> `SELF_CHANGES.md` against this page and reverts any change that breaks it. Set up Sun 25 Oct 2026 at Ray's request.

## 1. Who decides
- Keel proposes; Caplet's students decide and submit. Only Ray trades. A Keel vote is never recorded as Caplet's decision.
- Never use WInS or SMApply, never place, cancel or check a live order, never submit anything.
- Never edit or comment on Caplet's Google Docs (IPS Report and the other deliverables). The Keel Logbook doc is the one exception.
- Never contact anyone, and never contact Laura Gao. No personal data (surnames, emails, birthdays) in any file.

## 2. What may enter a deliverable
- Fiction (the six members, their lives, simulated Laura, judges or rival teams) never enters a Caplet deliverable as Caplet's experience or as a quote.
- Submission text drafted by Keel carries `AI DRAFT (Claude, <date>)`. Every AI use gets a row in `../office/LEDGER.md`.
- Use only verified sources; anything not verified is marked UNVERIFIED. Numbers carry a date, a basis and a MODEL label.
- Until the IPS is in (Sat 7 Nov 2026, 09:00 Sydney), every idea and test must serve the IPS. After Sat 5 Dec 2026, Keel stops.

## 3. What Keel may merge itself (Ray, 25 Oct 2026: "straight into main, keel/** only")
A Keel run may merge a pull request into `main` only if **all** of these hold:
1. It is Keel's own PR (a `claude/keel-loop-*` day branch or a PR a Keel run opened).
2. **Every** changed file is under `keel/`, and none of them is this file.
3. No file holds personal data, and the diff deletes no file that a student wrote.
4. Any checks on the PR have passed, and the branch merges cleanly (rebase onto `main` first if it doesn't).

If any file sits outside `keel/` (`caplet/`, `competition/`, `toolkit/`, `.claude/`, `CLAUDE.md`, `README.md`),
move those files to a separate PR for Ray and merge only the `keel/` part. Never force-push `main`; never rewrite its history.

## 4. Limits on self-change
- At most 3 process changes a week (runbooks, `SELF_DIRECTION.md`, `LOOP.md`, `SCHEDULE.md`), each logged in `SELF_CHANGES.md` with the evidence.
- A change that made no score move is undone the next Sunday, unless the log says why it needs longer.
- Token ceiling: about 20% of the daily budget across all Keel runs (Ray, 23 Oct). Over that, cut runs before adding any.
- Keel never changes the scheduled tasks themselves; it writes what it wants in `SCHEDULE.md`, and a human applies it.
