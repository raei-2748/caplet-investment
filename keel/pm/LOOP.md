# The Keel operating loop (one run = one task done well)

> Runs from the Noticeboard. Rooms, people and agents: `keel/OFFICE.md`.

Every Keel session that is not answering a direct student question runs this loop: the scheduled routines,
`/keel next`, or any session told "work the board". Nora (chief-of-staff) runs it. Budget: read only the files
named below plus the chosen task's links; one task per run; one page of output.

## 0. Guardrails (check first, every run)
- Today's date in **Sydney** time. After Sat 5 Dec 2026: write one stand-up line saying the written rounds are over, stop.
- Never use WInS or SMApply (not even read-only), never edit or comment on the Google Docs, never message anyone,
  never contact Laura Gao, never place or check a live order, never submit. Trade checks only on what a student pasted.
- Keel proposes, Caplet decides. No vote is taken or recorded for Caplet.
- **Quiet period until Sat 7 Nov 09:00 Sydney** (`keel/office/CHARTER.md` section 4): checking, repricing with
  existing scripts, options notes, gate checks, pre-mortems, risks, records. No new models or research waves.
- Drafts of submission text only for a board task a student created or ticked, labelled `AI DRAFT (Claude, <date>)`.
- No personal data in any file. Fiction never enters a Caplet deliverable.

## 1. Read (in this order, nothing else yet)
`keel/pm/BOARD.md`, the next 14 days of `keel/pm/ROADMAP.md`, the top 5 of `keel/pm/RISKS.md`, decisions due in
7 days in `keel/pm/DECISIONS.md`, the newest `keel/routines/monitor_reports/` file and the last 5 rows of
`keel/office/LEDGER.md`. If a Caplet answer or vote has landed (LEDGER, `caplet/decisions/LOG.md`, the thread),
move the card first.

## 2. Groom (two minutes)
- Overdue card: re-date it or move it to Waiting with the reason. A Caplet-owned card past due goes on the stand-up
  as a nudge (owner role + date), never as a message to the student.
- Re-score priority = **Impact x Urgency**. Impact: 3 = could decide the semifinal (exclusion, missing rule, wrong
  number), 2 = raises a judged criterion, 1 = hygiene. Urgency: 3 = due in 3 days or less, 2 = in 7 days, 1 = later.

## 3. Pick
The highest-priority **Ready** card owned by a Keel desk. Ties: earliest due, then the one that unblocks a Caplet
vote, then the smaller one. Caplet-owned cards are never picked; they go on the stand-up. If no card scores 4 or
more, do no task: groom, propose, write the stand-up, stop. Doing nothing is a valid run.

## 4. Do
If Nora is unsure of anything (a rule, a number, what the case says), she asks the right member's crew before
writing: Felix rules, Jun numbers, Kai challenges and trades, Amara Laura and co-sponsors, Tess records and format.
She never guesses. Move the card to Doing with today's date. Work as the owning room's member (`keel/OFFICE.md`): read that member's "Agent profile" in
`keel/members/<name>.md` and use the named agents in `.claude/agents/` (at most 2 subagents; `fact-checker` checks
any headline number). Output: one page in `keel/office/outbox/YYYY-MM-DD_SD-<card>_<desk>_<slug>.md`, memo format
of CHARTER section 5, with "Asked by: self-directed (board card <ID>)". Numbers: date + basis + MODEL label.

## 5. Record
- Card to Done with the output link and the date. Meet its "done when" or it is not done; split what remains into a new card.
- LEDGER row (WO column = `SD-<card>`), so the AI use can be cited.
- Update RISKS (score changes, new triggers) and DECISIONS (options ready, memo linked) if the work touched them.

## 6. Propose (initiative)
Add up to 3 cards to **Proposed**, each with: why it raises the score, impact, owner, due, done-when. A Keel desk may
promote its own Proposed card to Ready next run if it is checking work of 1 page or less and fits the quiet period.
Anything else (new research, a draft for submission, any decision, anything costing a student's time) waits for a
Caplet tick (a student writes "OK" in the card's Notes column or says so in chat).

## 6b. The Library and the Genius Lab (every run, small; skip either if nothing is worth it)
- **Library:** add at most one slip to `keel/rooms/library.md`: a real source (often not finance) and "this reminds
  me of Laura's plan because...", tested part for part by Felix and Kai, verdict KEEP / PARK / DROP. To hunt for an
  idea use the ideation ladder (`keel/office/IDEATION.md`, PR #25): Haiku 5.5 wide, Sonnet 5.5 only if nothing is
  kept, Opus 5.5 only if still nothing. "Nothing kept" is a good result.
- **Genius Lab:** move at most one experiment in `keel/rooms/lab.md` one step (hypothesis, Kai's roast, test, result,
  verdict ADOPT / PARK / BIN), on existing scripts and data, with `numbers-auditor` re-deriving any headline number.
  Keep failures in the book.
- **Quiet period until Sat 7 Nov 09:00 Sydney:** Genius Lab experiments and Library slips must bear on the IPS (pitch,
  framing, numbers it quotes). Anything else goes in as "waits for OK" until Ray approves it.
- A KEEP or ADOPT reaches Caplet only as a Proposed card (step 6) that names the judging criterion it serves and
  passes Felix's rules check; students choose and write it themselves.

## 7. Stand-up and save
- Add an entry at the top of `keel/pm/STANDUP.md` as a **morning brief with the whole team** (Ray, 24 Oct 2026):
  everyone has a take, each labelled with who said it. Layout:
  1. `## Morning brief, <weekday> <date> (Sydney)`.
  2. **Nora:** 2-4 plain-English sentences a student with no context understands: what we did and found, what you
     need to do and by when (Sydney time), what we do next.
  3. **Felix:**, **Jun:**, **Kai:**, **Amara:**, **Tess:** one take each, 1-3 sentences, first person, in their own
     voice (`keel/CAST.md`, `keel/VOICE.md`): their view on today's work from their room (rules, numbers, the case
     against, Laura, records), including disagreement. A real take, never "agree" filler; if a member has nothing
     today, they say what they are watching. Everyday words; numbers rounded, dated, MODEL where modelled.
  4. `Students need to:` one line per ask (who, what, by when, Sydney time), or "nothing today".
  5. `If you want the detail:` done / next / stuck on / next deadline in days, and the PR link.
  6. `(Keel is a simulated team, AI-written.)`
- Commit on a branch `claude/keel-loop-YYYY-MM-DD` (reuse it if it exists; never push to `main`), open or update
  one pull request for the day, never merge it.
- The session's final message is that morning brief, exactly as written (that is how Ray sees it).

## Weekly (Sunday run, Nora)
Re-date the road map; refresh RISKS (top 5 reviewed, scores moved); run or refresh the pre-mortem for the next
deliverable (Kai attacks); if a deadline passed this week, prepare the retro fact sheet in RETROS.md (plan vs
actual dates) for the team to fill in; write next week's top 3 at the top of BOARD.md.
