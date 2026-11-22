# Voice round 15: depth, the facility contribution and the 2031 range, whole (Mon 23 Nov 2026, morning)

Rounds 12 and 14 found no simulated test that reproduces the lines Caplet could not follow, so round 15 tested depth:
can a reader answer "what happens if" questions about the plan from one piece alone? Keel's prediction and the answer
key were written before any text was read (`round15/PREDICTION.md`, `round15/DEPTH_KEY.md`).

## Set-up

- **Writers.** Two fresh writers (W, V) who read only Caplet's writing (`CORPUS.md`, the IPS) and the facts
  (`FACTS_PLAIN.md` version 6). Each first carried the IPS on for about 200 words from its last line, then wrote one
  piece of 650-750 words for the judges: Laura's facility contribution and the range she gives co-sponsors in 2031,
  read on its own by a reader who knows only the case. V's brief added one paragraph asking for the working that lets
  a reader answer "what happens if" questions (shares halve, rates at 1%, the building dearer); W's did not.
  Briefs `round15/brief_r15_W.md` and `_V.md`; texts `writer_W.md` (748 words) and `writer_V.md` (780).
- **Control.** The IPS's own building paragraph and reasons to change (l.15 and l.17, 190 words), never meant to carry
  this much.
- **Readers.** Three blind readers, each reading the three texts once in a rotated order, one file at a time, answering
  nine questions after each text from that text alone, and counting rereads. A blind scorer marked all 81 answers right
  (R), partly right (P), wrong (W) or not on the page (N) against the key. `round15/build_packs_r15.py`, `packs/`,
  `readings/R1-R3.md`, `scorer/`, `SCORES_R15.md`. Readers and scorer are simulated, never people.

## Results

| Text | R | P | W | N | R+P of 27 | Rereads (paragraphs, 3 readers) | "We", "our", "us" per 100 words |
|---|---|---|---|---|---|---|---|
| W (no depth instruction) | 20 | 7 | 0 | 0 | 27 | 8 | 2.3 |
| V (asked for the working) | 14 | 10 | 1 | 2 | 24 | 6 | 1.7 |
| IPS l.15 and l.17 (control) | 2 | 16 | 0 | 9 | 18 | 1 | 1.6 |

**1. Depth came from the fact sheet, not from the instruction.** Both writers' pieces let readers answer nearly every
question (W 27 of 27, V 24 of 27, against Keel's predicted 4-6 and 6-7 of 9 per reader), so version 6's reasons
reached the page. The instruction to give the working did not help: W, never asked, gave more right answers than V.
Writer variance was again the larger effect, as in round 10. Keel's prediction 2 failed.

**2. Two answers were on no page, because the fact sheet lacked them.** Why a range rather than one figure (one R in
nine answers) and what covers a building-cost rise of about 25% (no reader said it: version 6 never gave the 25%
cover, so neither writer could). Both are now in version 7.

**3. One overclaim came from the fact sheet itself.** V wrote that once the shares are moved "nothing about it is
uncertain", taken almost word for word from version 6, and its readers then said nothing could stop the top. W said
instead "what's left to watch is the fund itself", with the 2% and the early end, and all three of its readers named
what could stop the top. Version 7 says what is and is not uncertain after January 2031: no share price or rate can
change the figure, and the fund's costs, an early end, the broker or a US default could still leave it short. This is
the attack-day rule (strong words on Treasuries, never on a fund's payout) reaching the writers' own facts.

**4. The control shows why the report is needed.** Caplet's own paragraph was the easiest read (one reread in six) and
left readers with gestures, not answers (16 P, 9 N): it was written to state the plan, and the report must evaluate it.

**5. What W did that worked, from the readers' own lines.** W gave each step its reason in the same sentence ("The 10
operating payments go first, because they're fixed"), owned the caution with a dry line ("It looks stingy, and it's
meant to"), named the remaining risks as "what's left to watch", and used one conceit turn, from Laura's own trade,
with its plain rule in the next clause. V's figures without the cover rule led two readers to work out, wrongly, that
a 25% rise exceeds her flexibility. W's piece is the round's best passage for the 27 Nov writers to read beside the
fact sheet, as a passage that held three readers, never as a template.

## What changes

- `FACTS_PLAIN.md` version 7: why a range, the 25% cover with what it counts, and the post-2031 line rewritten.
- The 27 Nov writers' briefs keep no "give the working" instruction; depth comes from the facts they are given.
- Round 16 tests the conceit's one open question from panel 5: whether "a signature is the other kind of ink" is
  followed on one reading in 3d (ARGUMENT_TREE Branch 5); otherwise 3d carries no turn.
