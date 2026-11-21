# Voice round 11: can a writer working from the facts alone make version 61's parts followable? (Fri 20 Nov 2026, morning)

Category one of Book 21: every sentence understood by an intelligent reader on one reading, and making sense once
understood. The round asked whether a writer who has read only Caplet's writing (`CORPUS.md`) and the plain facts
(`FACTS_PLAIN.md` version 2) can explain the four parts of the plan Caplet could not follow in version 61, so that a
reader who knows only the case follows every sentence first time. Keel's prediction was written before any reading
(`round11/PREDICTION.md`).

## Set-up

- **Writers.** Two fresh writers (U, V) on the brief `round11/brief_r11.md`: CORPUS and FACTS_PLAIN only, four
  passages of about 200-260 words in the team's "we", no images. Keel's main session (K) wrote the same four as the
  control. Topics: P1 the ten payments; P2 the 2028 deposit; P3 the 2031 range; P4 her flexibility.
- **Controls.** Caplet's own IPS paragraphs 3 ("In January 2027 we ...", C3) and 4 ("The building is a different
  matter ...", C4), in every pack.
- **Readers.** Six blind readers who know only the case brief (`brief_r11.md` section 2), each in a different role:
  an essayist student, a finance professor, a strictly literal reader, a sub-editor, a logician, the client. Each first
  read version 61 whole (21 sentences, Caplet followed only 1, 5, 6 and 8), then eight passages in a shuffled order
  (packs A and B, `round11/packs/`). For every sentence: Follow (1 first time, 2 one reread, 3 more), Sense (Y, N or ?),
  the fault, a plain paraphrase and why; then one question per passage. A reread counts as a failure (Book 21).
- **Scoring.** `round11/score_r11.py` writes `round11/SCORES_R11.md` and `per_sentence_r11.json` from the six readings
  (666 judgements). Readers are simulated (never people); the scores say how the words read to them.

## Results

**Calibration first: the readers catch about half of what Caplet failed.** Of version 61's 17 sentences Caplet could not
follow, each reader flagged 6 to 11 (mean 8.7; Keel predicted 11 to 14). As a panel, 12 of the 17 were flagged by at
least one reader and 9 by at least half. The five no reader flagged are all clear as grammar and empty as reasons:
"The ladder also carries reinvestment risk: interest arrives years before the payment it serves ..." (V12); "So in
2031 ... she sells up to half her shares for an extra reserve of Treasuries ..." (V13); "the top is the bottom plus
what that half raised" (V16); "The plan's biggest strength ... is that ... no payment, and no figure once named,
depends on a share price" (V20); "The tenth rung, with what was set aside for it, meets the last $50,000 in 2042"
(V21). Each can be paraphrased word for word without knowing why the step is taken or why the claim is true, and that
is exactly what Book 22 asked for ("explain the why rather than compress"). Of the four Caplet followed, readers
flagged two heavily (the "Caplet XR" sentences, which only someone who knows the plan's name can decode) and the other
two once in twelve. So the panel discriminates on decoding and misses failures of reason. A passage that passes this
panel has passed half the test.

| Text | Sentences | Reread | No sense | Clean for every reader |
|---|---|---|---|---|
| Version 61 (calibration) | 21 | 49% | 12% | 29% |
| Caplet's IPS, paragraphs 3 and 4 (control) | 12 | 10% | 8% | 67% |
| Fresh writer V | 52 | 24% | 6% | 67% |
| Keel's main session (K) | 49 | 23% | 14% | 65% |
| Fresh writer U | 55 | 32% | 8% | 55% |

| Topic (U, V and K together) | Reread | No sense |
|---|---|---|
| P1 the ten payments | 28% | 14% |
| P2 the 2028 deposit | 21% | 7% |
| P3 the 2031 range | 25% | 5% |
| P4 her flexibility | 32% | 14% |

Writing from the facts alone halves version 61's rereads (49% to 23-32%) but is still two to three times Caplet's own
paragraphs (10%). The best single passages were K's P2 (3% reread, 83% clean), V's P4 (11%, 83%) and V's P3 (17%, no
"no sense"); the worst was K's P4 (55% reread, 36% no sense), where Keel's working names came back: "the December 2032
Treasury fund" and "the IPS" before either was introduced, "The honest limit is the order in which those things can
come", "each can be pictured". The main session is as good as a fresh writer when it writes one step per sentence and
far worse when it summarises; the writer's habit in a passage mattered more than who wrote it.

**Against Keel's prediction.** Fresh writers: predicted 25-30% reread and 6-10% no sense; found 24-32% and 6-8%
(right). Keel's main session about ten points worse: wrong on average (23%), right about where it fails (summaries and
working names, all in one passage). Caplet's controls: predicted 15% and 5%, found 10% and 8% (the 8% is three readers
rejecting C4's "whatever figure you choose is money you already own" as an overclaim). By topic: predicted P3 worst;
found P4 and P1 worst for rereads and P3 the fewest "no sense" (wrong). On P3's question, readers of V and K gave the
reason for a range (the case asks for one; the top is what she gives and what co-sponsors plan around; the bottom is
the part held since January 2028), but all three readers of U's P3 said the passage never answered "why not just say
$115,000?" (right in kind, fewer than predicted).

## The sentences that failed, by kind

Every sentence that more than half its readers reread, or half or more found made no sense, is listed in
`round11/SCORES_R11.md`. They fall into six kinds, each named by at least four of the six readers.

1. **Figures that do not reconcile on the page.** The ten "cost about $301,500", so $1,500 short, then "the last
   $2,388" (K1.9-K1.10, U1.7-U1.8, 3 of 3 no sense for K1.10). The instruments the plan holds cost $302,287 with the
   funds' 0.07% fee (NUMBERS 1), so the gap is $2,287 in January 2027 money and $2,388 in January 2028 money; the fact
   sheet's version 3 prints the instruments' price, about $302,300, and drops the bare-curve $301,500.
   Likewise "$102,000 ... counted with room to spare ... $95,000" with the steps stacked in one clause.
2. **A dollar figure treated as money owned.** "The bottom is bought", "both ends are owned", "the figure she stated
   [is] already owned in Treasuries", and Caplet's own "whatever figure you choose is money you already own" (C4.7,
   rejected by three readers). The literal reader named it: "the writer means the Treasuries behind the figure". For
   the conceit this is the decisive finding of the day: ink must be defined with the Treasuries as the subject ("a
   dollar figure that Treasuries she owns will pay"), never "a figure owned" (ATTACKS D2 made the same change for the
   bond judge's reason).
3. **Names before things.** "The December 2032 Treasury fund", "the IPS", "the ladder", "her shares", "the meetings",
   "the day trading froze", "a different matter": every one a stall for a reader who knows only the case.
4. **"Because" and "so" claiming a cause that is not there.** "Spent that month, because nothing comes in after it"
   (V2.2, 3 of 3 no sense); "so for a year there are two gaps" (one overspend gives one gap); "the only other place
   for that money in the meantime is shares" (K2.8, a false premise: it could wait in Treasury bills).
5. **The cautious count stacked into one clause.** "Counted as if the interest it pays out from then on earns
   nothing, less 0.5% for costs beyond its fee, and rounded down": three steps in one breath, and "costs beyond its
   fee" never explained. Readers followed each step alone.
6. **Signposts that announce a point.** "The honest limit is the order in which those things can come", "each can be
   pictured", "The hard case is two at once", "Because the two ends say different things". Each only made sense after
   the next sentences did the work.

What passed, in the readers' own words: "the plain step-by-step sentences that carry one fact and one number each
almost never failed, however long they were" (finance professor); "hard words and long sentences were not what failed"
(logician); the history (world shares bought in 2000 were 41% down three years later) worked once a passage said the
mapping outright ("three years after buying, as 2031 is for her") and stalled where it said "the point that matches
her meetings". No image was used and none was missed.

## What changes

- **For the writers on 27 Nov** (carried into `FACTS_PLAIN.md` version 3 and the brief): the Treasuries, never the
  figure, are what she owns; one figure for the 2027 gap, or the step shown; every thing introduced before it is named;
  "because" only for a real cause; one step of the cautious count per clause, with what the 0.5% is for; no signpost
  sentences; the 2000-2003 mapping said outright; and every sentence that takes a step gives its reason in the same or
  the next sentence (the five sentences no reader flagged are the ones that took a step without one).
- **For the method.** Simulated readers test decoding, not reasons. From round 12 each reader also answers, for every
  sentence that states a step or a claim, "could you tell a friend, from this page alone, why this is done or why it is
  true?" (Why: Y, N), and a "No" counts as a failure. Version 61's five unflagged sentences stay in the calibration as
  the check that the new question catches them.
- **Round 12 (this evening):** "we" and the why, per OVERDRIVE_PLAN, with the new Why column, P4 and P1 rewritten by
  fresh writers on the version 3 fact sheet, and K's P2 and V's P4 kept as the best of round 11 for comparison.

## Files

`round11/brief_r11.md` (writers' brief), `round11/writer_U.md`, `writer_V.md`, `writer_K.md` (the passages),
`round11/build_packs_r11.py` (packs, key and sentence list), `round11/packs/` (the six packs), `round11/key.json`,
`round11/readings/R1.md`-`R6.md`, `round11/score_r11.py`, `round11/SCORES_R11.md`, `round11/per_sentence_r11.json`,
`round11/PREDICTION.md`.
