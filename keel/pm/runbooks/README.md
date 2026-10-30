# Runbooks: how each Keel room works (Keel may edit these)

> **Read `../../BIBLE.md` first: ten books (23-30 Oct 2026; Book 10 and the Ten Commandments, 30 Oct), under Wharton's word (`keel/WHARTON_WORD.md`), which ranks first.** They beat every rule on this page.
> Extraordinary above all; a distinctive, deeply human voice (Ahaan's, never AI's); one subtle motif, Caplet XR (extended
> release; X = 10; R never "release"); breathtaking investing knowledge, applied, not name-dropped; no hedging; and the
> IPS rewrite is slow, deep thinking, never rushed. No work is finished until the portal shows it.

> **BOOK 10 MODE, Fri 30 Oct - Wed 4 Nov 2026 (overrides anything below that disagrees).** Caplet, 30 Oct (BIBLE Book
> 10): the mock judges were too alike and approved every change; V29 read as robotic and over-compressed; the rules
> were decoration. Until the final IPS goes to Caplet (**end of Wed 4 Nov, Sydney; the Sat 31 Oct review is
> cancelled**), every room runs this way:
> 1. **The rewrite thread drafts; rooms feed it.** No room writes, votes on or names a full pitch + IPS, and no room
>    picks "Caplet's review draft" or adds a VERSIONS row. The current draft is the newest `keel/ips_rewrite/drafts/D*`
>    folder named in `keel/ips_rewrite/README.md`. Rooms send ideas, evidence, model numbers, fact-checks and
>    alternative paragraphs to `keel/ips_rewrite/inbox/<date>_<room>.md`; the thread folds the best in.
> 2. **The Ten Commandments** (`keel/BIBLE.md`) bind every output. Read `keel/WHARTON_WORD.md` (ranks first) and Book 10.
> 3. **Judging only the new way** (`keel/ips_rewrite/judges/README.md`): different models, priors and methods, blind,
>    rivals in the field, only Wharton's word; report disagreement. Never ask a reader for "the line that wins".
> 4. **Most wanted from rooms now:** (a) truth-checks of every claim and number in the current draft (the Window's
>    30 Oct catch on the wipe-out line is the model); (b) the work orders in `keel/ips_rewrite/WORK_ORDERS.md` marked
>    BOOK 10; (c) paragraphs rewritten in Caplet's voice (Ahaan's essays, `keel/voice/06_voice_guide.md`), clearer and
>    less compressed, offered as alternatives; (d) niche ideas that answer the panel's open criticisms.
> 5. No "every team will ...", no unexplained numbers ("we modelled", never "we judge"), no AI-use or "required trading
>    activity" worries, no grammar or formatting work.

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
5. **Deep, dense work on the big picture** (`keel/BIBLE.md` Books 4 and 9, rules 2, 5 and 11). Rooms feed the rewrite
   research, ideas, tests and critique, intensively, every run. The only timeline rule is the final IPS for
   Caplet's review at the **end of Wed 4 Nov** (Book 10; IPS due Sat 7 Nov 09:00 Sydney); the rewrite thread drafts.
   Spend runs on strategy, niche investing knowledge (fused and critiqued, never copied) and logic, not on small word
   or accuracy fixes. Formatting is Caplet's job, not Keel's. **Do it properly.** One solid output with sources and dates; numbers MODEL-labelled. IPS ideas go to
   `keel/ips_rewrite/inbox/<YYYY-MM-DD>_<room>.md`, never into IPS v4/v4.1.
5b. **Bank every good idea** (BIBLE Book 9, rule 10: "Every single good idea ... must end up in either the IPS or the
   Final Report or both"). Before you record, add a row to `keel/ips_rewrite/IDEA_BANK.md` for each good idea the run found: the
   idea in plain words, where it lands (IPS, FR or Both), why it earns its place, and its honest weakness (critique,
   don't dump), with the proof file. Drop a weak one with a reason in the bank's "Dropped" table; never drop one
   because Caplet hasn't replied.
   The portal's Ideas tab shows the bank. No AI-use logging or questions (rule 12): Caplet cites AI use itself.
6. **Record.** Update your room's `## Now` block (Doing, Decided, Next, For the judges, Updated as `YYYY-MM-DD HH:MM`
   Sydney). If a judge-facing draft changed, add a row to `keel/pm/CHANGES.md`; if you wrote a new full draft of the
   pitch + IPS, also add the next numbered row (V22, V23 ...) to `keel/ips_rewrite/VERSIONS.md`, so the portal shows it. One row in `keel/pm/RUNLOG.md`; a memo in `keel/office/outbox/` ending with each present
   member's labelled take (`- **Jun:** ...`) when there is something to say; up to 2 requests filed, finished ones closed.
   **Takes are a conversation, not six statements** (Ray, 27 Oct: "I cannot really see the dialogues you guys had"):
   each take answers, pushes back on or builds on the one before it, by name where it helps. The portal's front page
   shows them as a chat. Start the memo with a `**Result.**` paragraph in one or two plain sentences; the portal quotes it.
   **Say it plainly, for Caplet (Ray, 27 Oct: "make it clear essence ... very clear, simple").** Append one bullet to
   `keel/today/YYYY-MM-DD.md` (Sydney date) under `## In plain words`:
   `- **<Room, no "The">:** <what you did and found, in one or two sentences a Year 11 student gets on first read; no
   jargon, IDs or file names; then what it changes>. ([memo](../office/outbox/<your memo>.md))`
   Create the file from yesterday's if it is missing (title `# <Ddd d Mon> 2026: what Keel did today`, the AI note, an
   empty `## For Caplet`, then `## In plain words`). Never edit another room's bullet. The Noticeboard (07:00, last
   night's file) and the Archive (19:10, today's) write `## For Caplet`: at most four bullets, the most important first,
   each opening with a bold one-line headline. Ticked to-dos: mark finished tasks in `pm/BOARD.md` `## Done` with the
   day (`Tue 27 Oct`) and finished work orders `done <d Mon>`, which is what the portal's "Done" list reads.
7. **Push.** Fetch and rebase just before pushing (other rooms push to the same branch; retry on a race), then open or
   update the day's PR ("Keel <date>: ..."). The Archive (19:10) and the daily loop (07:00) merge it under
   `keel/pm/INVARIANTS.md` section 3.
8. **Put it on the portal: no work is finished until the portal shows it** (Ray, 26 Oct 2026, project rule). Your
   push in step 7 rebuilds https://raei-2748.github.io/caplet-investment/ within minutes: the build merges every
   `claude/*` branch pushed in the last three days that merges cleanly, then main. Before you call the run done:
   (a) your room's `## Now` block, a `pm/RUNLOG.md` row and, for a new draft, a `ips_rewrite/VERSIONS.md` row say what
   you did (that is what the portal reads); (b) the "Keel Office portal" run after your push is green in GitHub
   Actions (if it says your branch was skipped because it does not merge cleanly, rebase on main and push again);
   (c) step 9's line links the portal page that shows the work (the day, `#/day/YYYY-MM-DD`, or `#/room/<id>`,
   `#/ips/<n>`, `#/doc/<path>`). The front page (Today) shows `keel/today/<date>.md`, the memos' conversations and
   research, the day's Done list and the research round; if your line isn't there, step 6 isn't finished.
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
