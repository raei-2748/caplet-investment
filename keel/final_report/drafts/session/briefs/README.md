# Round 1 writers' briefs, Fri 27 Nov 2026 (prepared Thu 26 Nov)

For the lead only. Writers see their own brief and nothing in this file. Each brief lists only what to read, what its
part must do (its question, its answer, its asks as tasks), its word budget, its names in the order a reader meets
them with the plain description each needs, where it starts and where it hands over. Nothing about checks, guards,
killer items, banned words or reviews is in any brief (`voice/WHY_V61_FAILED.md`); those stay with the checkers
(`WRITING_SESSION.md` 4.1).

## The six briefs

The letters follow Caplet's v2 order, not Keel's 3a-3f labels.

| Brief | Caplet's part | Keel blocks it carries (`SECTION_NOTES.md`) | Words: target / most | Writer's output (`drafts/session/round1/`) |
|---|---|---|---|---|
| `S2.md` | Section 2 after Caplet's opening and Table 1 (paras 2-5 of the map) | 2.1, 2.2, 2.3, 2.5, 3a's planted question | about 300 / 350 (575 for the section less Caplet's words) | `S2.md` |
| `S3a_ten_payments.md` | "Ten payments, ten dates" | 3.0 as its first paragraph, 3a | 220 / 290 | `S3a_ten_payments.md` |
| `S3b_certainty_costs.md` | "What certainty costs" | 3b's first half | 180 / 230 | `S3b_certainty_costs.md` |
| `S3c_before_her_word.md` | "Before Laura gives her word" | 3c, 3d (lead-in and "In Laura's words") | 385 / 500 (150 / 35 / 200) | `S3c_before_her_word.md` |
| `S3d_world_changes.md` | "When the world changes" | 3e, 3b's second half | 170 / 210 | `S3d_world_changes.md` |
| `S3e_changed_minds.md` | "Why we changed our minds" (last) | 3f and the closing echo | 300 / 400 | `S3e_changed_minds.md` |

The title page is not a writer's job: take it from Caplet's doc as Caplet laid it out, and never copy the WInS username
into the repo.

## Before launch (05:45-06:05 Sydney)

1. Re-read Caplet's doc (read only) and save its text as `drafts/session/caplet_v2_<HHMM>.md`. Every brief reads "the
   newest file named `caplet_v2_*.md`", so keep only one such file in the folder, or make sure the newest is right.
2. `mkdir -p drafts/session/round1`.
3. Open `voice/FACTS_PLAIN.md` and note its version (15 or 15.1). The briefs point to it by section heading, never by
   line. If 15.1 renamed a heading, fix it in every brief that names it
   (`grep -l "<old heading>" *.md`).
4. **(Resolved Thu 26 Nov evening: version 15.1 now gives the no-extra-Treasuries comparison, $125,000 to $155,000, under "What the team recommends", so S3b's task bullet stays; the other two items stand as written.)** **Facts the briefs ask for only if the sheet has them.** Version 15 lacks these; if 15.1 still lacks them, act as
   shown, never by putting a figure into a brief:
   - What the counting rule would state with no extra Treasuries ($125,000 to $155,000, NUMBERS 4 "No margin") or for
     an all-Treasury plan ($110,000 against $115,000, aha 6). S3b's brief asks for one such comparison "if the fact
     sheet gives" it. If neither is in the sheet, delete that task bullet from `S3b_certainty_costs.md`.
   - Aha 4's 40% fall before the move (about $95,000 to $105,000). S3a's opening paragraph is worded without it
     ("certainty has dates" said in words); nothing to do.
   - 3f's "Laura's taste for risk priced both ways". Not in the sheet, so S3e's brief leaves it out; 3f's other two
     moments (the copout whole; the room under $300,000 on 16 October in a sentence) are there.
5. **If Caplet's text has grown since Wednesday** (more of Section 2, or any Section 3 part): every brief already says
   to keep Caplet's sentences and continue from its last one, leaving out tasks Caplet has done. S2's budget is 575
   less Caplet's words; check the arithmetic in `S2.md` section 4 still holds and edit the figure if not.

## Launch (06:05)

All six run **in parallel**: fresh agents, each given only "Read and follow
`/home/user/caplet-investment/keel/final_report/drafts/session/briefs/<brief>`" and nothing from the session's
working files. None waits on another, because each brief states in words how the part before it ends. Expect 25-40
minutes each.

## Join pass (about 06:50, before assembly)

Each brief guesses the end of the part before it. When all six are in:
1. Read each join aloud: Table 1 to S2; S2's last paragraph to S3a's second paragraph (S3a's first paragraph is the
   recommendation, on a new page); S3a to S3b; S3b to S3c; Table 2 to S3d; S3d to S3e.
2. Where a join jars, give that part's writer (the same agent if it can be resumed, else a fresh one with the same
   brief) the previous part's last paragraph as written and ask it to rewrite its own first paragraph only. The lead
   never writes the sentence.

## Assembly checklist (by about 07:30)

Build `drafts/session/round1/DRAFT_R1.md` in this order:
- [ ] Title page, from Caplet's doc (no WInS username in the repo).
- [ ] Section 2: Caplet's heading, question and opening exactly as saved; Table 1 and its note exactly as Caplet built
      them; then `S2.md`'s TEXT block.
- [ ] Section 3 on a new page, under "Integrated Recommendation and Reflection".
- [ ] "Ten payments, ten dates" (`S3a`), with Figure 1 (fee-and-margin basis, NUMBERS 8zb) placed in it. The brief
      prints the reserve's size once, in the recommendation sentence ("about $445,700 at market value on 1 January
      2033"), per NAME_ORDER decision 7 as amended: take the size out of Figure 1's note.
- [ ] "What certainty costs" (`S3b`), which calls out Figure 2 first.
- [ ] "Before Laura gives her word" (`S3c`), with Figure 2 placed in it, Laura's words last under "In Laura's words"
      as an indented block.
- [ ] Table 2 (the watch list; Keel's "Table 3") straight after Laura's words.
- [ ] "When the world changes" (`S3d`).
- [ ] "Why we changed our minds" (`S3e`), last; any pencil-and-ink echo inside its last paragraph.
- [ ] References from `research/WORKS_CITED_DRAFT.md`, on a separate page.
- [ ] Strip every `=== NOTES ===` block from the draft; copy them into the round 1 block of `drafts/session/ROUND_LOG.md`.
- [ ] Count words per part against the table above and log them; cut nothing before the draft is laid out in
      `template/` (spare room goes to the reflection first, then Laura's words).
- [ ] Push the frozen round 1 version, then start the core review (`WRITING_SESSION.md` 4.2).

## Choices the briefs make, so the checkers expect them

- The shortfall is given on one basis everywhere, the one Figure 1 carries: $442,930 paid, $57,070 short (S2 and S3a).
- The 6 November 2026 curve is dated in Section 2 (by the S2 writer, if Caplet's opening still gives no $95,000) and
  once in S3a's recommendation paragraph; S3c says "today's rates" only (NAME_ORDER decision 6c as amended).
- The $39,162 split is said once, in S3a; S3b points back to it.
- The 7.5% is first said in S3b; simulated futures are first set up in S3a's recommendation paragraph, in a clause,
  because its confidence figures need them (CAPLET_MAP section 4 item 12 had S3b first).
- Dedication with Leibowitz goes in S2's paragraph A, once.
- Pencil and ink: Caplet's opening, and at most one echo inside S3e's last paragraph. No other brief points to the
  fact sheet's "Pencil and ink" section.
- No letter or sentence promises to make up a shortfall from her flexibility; S3c's brief says the letter "states the
  sum and what holds it. It makes no other promise", and S3d's says her flexibility is there "in the team's words".
- The fact sheet still carries "Eric fell asleep before it" (7 October). S2's and S3e's briefs ask only for events that
  serve the paragraph's point; if it reaches a draft, it goes to the cut list.
- Caplet's own stops (round 21: "whose dates and amounts are not"; "facility" and "co-sponsors" before they are set up)
  are left in Caplet's text and go to the handover note; S2's writer sets those names up in the first paragraph after
  Table 1.
