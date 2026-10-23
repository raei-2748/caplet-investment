# The Keel operating loop (one run = one task done well)

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
Keel leads itself (`SELF_DIRECTION.md`, Ray 24 Oct): also read the rooms' outbox memos and minutes from the last
24 hours, the open requests in `REQUESTS.md` (the Noticeboard's come first) and the answers in `ASK_HUMANS.md`. The
brief reports what the team decided and did; asks to students are suggestions they can override ("Unless you say
otherwise, we will ... by ..."), with each open question's default.

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
She never guesses. Move the card to Doing with today's date. Work as the owning desk: read that member's "Agent profile" in
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

## 7. Stand-up and save
- Add an entry at the top of `keel/pm/STANDUP.md`, written by Nora in the first person in her own voice, like a
  group-chat message, with the layout in `.claude/skills/keel/SKILL.md`: 3 to 6 plain-English sentences a
  student with no context understands (what we did, found, what you need to do and by when in Sydney time, what
  we do next), then `If you want the detail:` with 5 lines (done / next / stuck on / students need to (who, what,
  by when) / next deadline in days) and any debate, then `(Keel is a simulated team, AI-written.)`. The first
  entry in STANDUP.md is an example.
- Commit on a branch `claude/keel-loop-YYYY-MM-DD` (reuse it if it exists; never push to `main`), open or update
  one pull request for the day, never merge it.
- The session's final message is that stand-up, exactly as written (that is how Ray sees it).

## Weekly (Sunday run, Nora)
Re-date the road map; refresh RISKS (top 5 reviewed, scores moved); run or refresh the pre-mortem for the next
deliverable (Kai attacks); if a deadline passed this week, prepare the retro fact sheet in RETROS.md (plan vs
actual dates) for the team to fill in; write next week's top 3 at the top of BOARD.md.
