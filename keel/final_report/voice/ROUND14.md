# Voice round 14: carried on from their own last line, and read back cold (Sun 22 Nov 2026, evening)

Two questions. Does a cold retelling (read once, put the text away, tell a friend each step and the reason it was
given) catch the version 61 sentences Caplet could not follow that every simulated reader has passed? And does the
"continuing" exercise from the voice programme (carry the IPS on from its own last line, as the same people, before
writing report passages) bring "we" and the reasons back into fresh writers' sentences? Keel's prediction was written
before any text was read (`round14/PREDICTION.md`).

## Set-up

- **Writers.** Two fresh writers (Y, Z) who read only Caplet's writing (`CORPUS.md`, the IPS by name) and the facts
  (`FACTS_PLAIN.md` version 5). Each first carried the IPS on for about 200 words from "With these promises, ours is to
  take none.", then wrote two report passages of 230-290 words as the same people: P3 the 2031 range and P5 the half
  moved and the half kept, introduced together. Z's brief also said the team likes a dry touch of wit where it comes
  naturally; Y's said nothing about wit. Briefs `round14/brief_r14_Y.md` and `_Z.md`; texts `writer_Y.md`, `writer_Z.md`.
- **Controls.** Version 61 (Caplet followed sentences 1, 5, 6 and 8 only), Caplet's own IPS paragraphs 3 and 4, and
  round 12's range passage by writer X (same topic as P3).
- **Readers.** Four blind readers in round 12's roles (a finance professor judging, a literal reader, a logician, the
  client), each reading version 61 and then seven passages in its own order. For each text: read once, retell cold
  (`R1. Step: ... | Because: ...`), then go back to the numbered sentences (Follow, Sense, which retelling line came
  from which sentence). Two blind scorers marked all 281 retold reasons: E explains, R restates the step, M missing,
  W wrong. `round14/build_packs_r14.py`, `packs/`, `readings/R1-R4.md`, `scorer/`, `score_r14.py`, `SCORES_R14.md`.
  Readers and scorers are simulated, never people. Every reader saw the numbered list in the same file as the plain
  text, so "cold" was the reader's own discipline, not enforced.

## Results

**1. The cold retelling does not reproduce Caplet's failures either.** It caught 2 of the 5 sentences every earlier
reader passed (V20 and V21), against a bar of 3, and 7 of the 17 Caplet failed; it also caught 3 of the 4 Caplet
followed (V01, V05, V06), so it cannot tell Caplet's failures from Caplet's successes. What it finds is a step stated
without a reason: V01 is the plan's rule, V06 names the rungs "X and R", V21 is a plain fact, and each has no "because".
Caplet followed V01, V05 and V06 because they are clear, not because they are argued. So neither simulated test,
round 12's Why column nor this, is a proxy for what Caplet could not follow. Keel predicted 2 of 5 (right in number,
wrong in which: it expected V13 and V16).

The likeliest reason, read against Caplet's own notes on version 61 (`WHY_V61_FAILED.md`): Caplet's bar for a reason is
not "is one given?" but "is it explained properly?" ("If you're wrong, don't say it; if you're right, actually explain
it properly", on V12's reinvestment risk). Simulated readers retell V12's reason correctly ("interest arrives years
before the payment, so money waits and earns less if rates fall") and score it E; Caplet wanted to know what that
does to a $50,000 payment and by how much. V20 failed with Caplet for "barring a US default" (Books 3, 5 and 19), a
matter of content, not comprehension. The ground truth stays Caplet's own reading; the readers remain useful for the
faults they do find (finding 3).

**2. Carrying the letter on worked.** "We" rose from round 12's 0.7 per 100 words to 2.6-2.9 for Y and 1.6-2.6 for Z
(Caplet's IPS 2.4); both writers said the exercise put "we" back in charge of the verbs ("we buy, we sell, we count";
"money never acts on its own"). Rereads fell to 17% for Y and 23% for Z (round 12's writers 24% and 32%; round 11's
24-32%; Caplet's own paragraphs 10-14% this round; version 61 45%). Retold reasons that explain: 59-75% for the
writers against 20% and 52% for Caplet's IPS paragraphs 3 and 4, which state and do not argue, as a letter may.

| Text | Reread | Retold reasons E / R / M | Caught (no explaining reason retold) |
|---|---|---|---|
| Version 61 | 45% | 45% / 29% / 26% | 48% |
| Writer Y, the range (Y3) | 21% | 59% / 12% / 29% | 27% |
| Writer Y, the two halves (Y5) | 12% | 75% / 17% / 8% | 22% |
| Writer Z, the range (Z3) | 20% | 65% / 6% / 29% | 22% |
| Writer Z, the two halves (Z5) | 27% | 71% / 7% / 21% | 25% |
| Round 12's X, the range | 23% | 66% / 13% / 21% | 30% |
| Caplet's IPS paragraph 3 | 10% | 20% / 67% / 13% | 65% |
| Caplet's IPS paragraph 4 | 14% | 52% / 9% / 39% | 54% |

**3. The clearest passage was Z's two halves**, named by three of the four readers (the fourth named round 12's X):
every purchase carries its reason, including the order of purchase ("it comes straight after the payments because
nothing arrives after that deposit"; shares "go last because no promise depends on" them) and why the kept half
cannot be promised ("its value is a share price, and promising it would mean promising a forecast"). It was also
reread more than Y's (27%), on its dollar figures and one long chain (Z5.5). What still failed, by all or three of four
readers:
- **Why half, in the range passages.** Y3, Z3 and X3 move half the shares and never say why half or what the other
  half does; the two-halves passages, which do, had no such gap. In the report 3b comes before 3c, so 3c can point
  back; a range passage read alone cannot.
- **Counting rules without their purpose.** "Cautiously", "stingily", "less a margin": only X3 said why ("so that she
  never states more than the fund delivers"). Z's one dry word, "stingily", was reread by three readers for this
  reason: wit that carries no reason costs a reread; the same word with its purpose beside it would not.
- **Sizes never argued.** Why $81,244, "a little over half" or "most" goes to the fund in 2028; the 50-50 split in
  2031 was argued, the 2028 split never.
- **Pointers and phrases that need the next sentence.** "Once the ten payments are finished" (they run to 2042; it
  meant bought), "seen from today" beside "from that day", "a year earlier", "we spend the uncertainty before she
  speaks" (heard only after the next sentence), "that is her range ... put the way a co-sponsor will use it".
- **Two model figures and a condition in one sentence.** "Keep only 30% back and the top rises about $5,000, but her
  flexibility then covers a 10% stronger Taiwan dollar in about half our model's futures, not 93 in 100" (Y5.9, Z5.13)
  and "a top named a year earlier would exceed what the move could buy in about 11 futures in 100" (Y3.8).

**4. Wit.** Z used two dry turns ("we count them stingily, too"; "a forecast is the one thing Laura should not hand to
people deciding how big a building to fund"). The second was retold with its reason by every reader who reached it;
the first was reread. Writer variance and the wit condition cannot be told apart with two writers (as round 10 found).

## What changes

- **For the writers' facts.** `FACTS_PLAIN.md` version 6 (tonight) gives the two reasons readers could not find: why
  the floor gets $81,244 (the IPS's "most", and the same IBTM-to-VT split as the portfolio the team bought and froze,
  about 73 to 27, NUMBERS section 0) and why each end is counted so cautiously (so the figure she states is never more
  than the fund will pay; a co-sponsor plans a building on it).
- **For the 27 Nov writers.** Every writer starts with the continuing exercise; it was the largest single gain in any
  round on "we". A counting rule is said with its purpose in the same sentence; a model figure gets its own sentence;
  "finished" is never used for payments still to come.
- **For the method.** No further simulated test of Caplet's empty reasons: two have failed. The readers keep the
  jobs they do well (pointers, chains, missing reasons, figures without a base). Round 15 tests depth instead of
  presence: after the retelling, each reader answers one concrete question the passage should let them answer ("if
  rates fell to 1% and stayed there, what would happen to the 2033 payment, and how do you know?"), the shape of
  Caplet's own note on reinvestment risk.

## Against the prediction

Caught 2 of 5: right in number, wrong in which. False alarms 1 of 4: wrong (3 of 4). Over the 17, 9-12: wrong (7).
Rereads 16-24%: right (17% and 23%). Writers' E 60-75%: right (59-75%); Caplet's 70-85%: wrong (20% and 52%). "We"
1.5-2.5: right or above (1.6-2.9); the continuation above 3: Z right (3.3), Y wrong (1.4, because the letter's "you"
does the steps). P3 rereads above P5's: mixed (Y yes, Z no). Wit not separable from writer variance: right.
