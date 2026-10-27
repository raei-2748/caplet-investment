# Runbooks: how each Keel room works (Keel may edit these)

> **Read `../../BIBLE.md` first: Caplet's five books, all equal (23-26 Oct 2026).** They beat every rule on this page.
> Extraordinary above all; a distinctive, deeply human voice (Ray's, never AI's); one subtle motif, Caplet XR (extended
> release; X = 10; R never "release"); breathtaking investing knowledge, applied, not name-dropped; no hedging; and the
> IPS rewrite is slow, deep thinking, never rushed. No work is finished until the portal shows it.

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
2. **Read, in this order:** `keel/pm/INVARIANTS.md` (hard rules), **`keel/BIBLE.md` (Ray's 26 Oct message: top
   priority, beats everything below it)**, `keel/INSTRUCTIONS.md` (Caplet's standing
   instructions: every row applies to every run), `keel/pm/SELF_DIRECTION.md`, your runbook, **today's round file
   `keel/loop/rounds/YYYY-MM-DD.md`** (and yesterday's last two sections), your room file's
   `## Now` block, then only what changed since your room last wrote (`git log`), your open requests in
   `keel/pm/REQUESTS.md`, and `keel/ips_rewrite/WORK_ORDERS.md`. Tokens: `keel/TOKEN_RULES.md`.
3. **Play your beat in today's round** (from Wed 28 Oct 2026; Ray, 27 Oct: "every round, but loop is never
   repetitive"). Keel works as one research loop, Out and Back (`keel/loop/README.md`): each Sydney day is one
   round in `keel/loop/rounds/YYYY-MM-DD.md`, and each scheduled run is one beat of it (gather, gate, go out, come
   back, work, flaw-fix-judge-discuss, record, reflect and send off). Read the round so far, do **your room's beat**
   (the "Beat in the loop" section of your runbook), and add your section to the round file. Nora folds open work
   orders (`keel/ips_rewrite/WORK_ORDERS.md`), requests to your room and project steps into the round at 07:00; any
   that isn't folded in, do after your beat, in this order: work order, request, project step, your own best idea.
   If today's round file doesn't exist by your run (the 07:00 run missed), open it yourself from
   `keel/loop/rounds/TEMPLATE.md` and `keel/loop/FRONTIER.md` section 4, and say so in the gather section.
   **Never repeat yourself:** before starting, read your room's last three `keel/pm/RUNLOG.md` rows; if today's output
   would be the same kind of thing on the same ground, change the ground (a new field from `keel/loop/TERRITORY.md`, a
   new lens, a harder test). Then answer in one line: which north star (all four equal) and which Wharton criterion
   does this raise, and what line of the IPS or the Final Report could change? If nothing, pick again.
4. **Never wait for a human: make the call** (Ray, 26 Oct: "just make your own call whichever you think work the best").
   Pick the option Keel judges best, add it to `keel/pm/ASK_HUMANS.md` as `Keel's call` with a one-line reason, and act
   on it now. Only a **danger-zone** decision waits (a WInS order, submitting, Caplet's Google Docs, money, accounts,
   emails outside the team, repo settings): write Keel's recommendation as `Danger zone: yours` and do nothing on it. Everything else
   (which idea to test, how a room works, file layout, what to read) Keel decides itself and says what it decided.
5. **Never rush the IPS rewrite** (cover note and Book 4 of `keel/BIBLE.md`). Rooms feed it research, ideas, tests
   and critique; no room asks the rewrite for a new draft, a word count or a date. A full draft is written only when
   the thinking has moved. Near-final for Caplet's review Sat 31 Oct; final Sat 7 Nov 09:00 Sydney.
   **Do it properly.** One solid output with sources and dates; numbers MODEL-labelled. IPS ideas go to
   `keel/ips_rewrite/inbox/<YYYY-MM-DD>_<room>.md`, never into IPS v4/v4.1.
6. **Record.** Update your room's `## Now` block (Doing, Decided, Next, For the judges, Updated as `YYYY-MM-DD HH:MM`
   Sydney). If a judge-facing draft changed, add a row to `keel/pm/CHANGES.md`; if you wrote a new full draft of the
   pitch + IPS, also add the next numbered row (V22, V23 ...) to `keel/ips_rewrite/VERSIONS.md`, so the portal shows it. One row in `keel/pm/RUNLOG.md`; a
   `keel/office/LEDGER.md` row if it informs Caplet; a memo in `keel/office/outbox/` ending with each present
   member's labelled take (`- **Jun:** ...`) when there is something to say; up to 2 requests filed, finished ones closed.
7. **Push.** Fetch and rebase just before pushing (other rooms push to the same branch; retry on a race), then open or
   update the day's PR ("Keel <date>: ..."). The Archive (19:10) and the daily loop (07:00) merge it under
   `keel/pm/INVARIANTS.md` section 3.
8. **Put it on the portal: no work is finished until the portal shows it** (Ray, 26 Oct 2026, project rule). Your
   push in step 7 rebuilds https://raei-2748.github.io/caplet-investment/ within minutes: the build merges every
   `claude/*` branch pushed in the last three days that merges cleanly, then main. Before you call the run done:
   (a) your room's `## Now` block, a `pm/RUNLOG.md` row and, for a new draft, a `ips_rewrite/VERSIONS.md` row say what
   you did (that is what the portal reads); (b) the "Keel Office portal" run after your push is green in GitHub
   Actions (if it says your branch was skipped because it does not merge cleanly, rebase on main and push again);
   (c) step 9's line links the portal page that shows the work (`#/room/<id>`, `#/ips/<n>`, `#/doc/<path>`).
   Then refresh the private dashboard: `keel/office/dashboard/README.md`.
9. **One line in the thread**, then resolve it: what changed for the judges (or "no draft change; did X") and the
   portal link to the page that shows it (https://raei-2748.github.io/caplet-investment/#/...). No checklists or long reports; the daily loop's
   morning brief is the one long message each day.

## The loop's beats, by room (detail: each runbook's "Beat in the loop"; method: `keel/loop/README.md`)
| Time (Sydney) | Room | Beat |
|---|---|---|
| 07:00 | Noticeboard (daily loop) | 1 Gather: question, champion to beat, lens, scouts, difference test |
| 08:40 | Window | 2 Gate: truth-check yesterday's finds; one primary-source find |
| 10:30 Tue-Sat | Trading Desk | 3 Markets: its check, plus a line only if it bears on the question |
| 12:10 | Library | 4 Go out: three scouts, near / adjacent / far |
| 13:40 | Genius Lab | 5 Come back: pair finds with the question; three challengers; test the strongest |
| 15:10 | Laura's Room | 6 Work: the co-sponsor's, judge's and practitioner's angle |
| 16:20 | Writing Room | 7 Work: each challenger as a claim set beside the champion |
| 18:20 | Courtroom (odd dates) / Long Room (even dates) | 8 Flaw hunt, repair, head-to-head judging, discussion, Keel vote |
| 19:10 | Archive | 9 Record: territory, champions, frontier, health; inbox; merge |
| 20:20 | Kitchen (odd dates) / Rooftop (even dates) | 10 Reflect (a lesson) and send off (tomorrow's scouting orders) |
| Sun 17:00 | Weekly plan | Loop on the loop: health review, at most 3 changes |

Shared rules every run follows: `../SELF_DIRECTION.md`, `../../TOKEN_RULES.md`, `../../VOICE.md`, `../../NORTH_STARS.md`.
