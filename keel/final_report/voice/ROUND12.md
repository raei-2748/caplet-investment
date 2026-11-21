# Voice round 12: does asking "why, from the page alone?" catch what Caplet could not follow? (Sun 22 Nov 2026)

Category one of Book 21 again (every sentence understood on one reading and making sense once understood), with Book
22's two asks added to the brief: "we" as Caplet's IPS uses it, and the why explained rather than compressed. Round 11
found that simulated readers catch sentences that are hard to decode and miss sentences that are clear as grammar but
empty as reasons. So every reader this round also answered, for each sentence that takes a step or makes a claim,
"could you tell a friend why this is done or true, from this page alone?" (Why Y or N), and a "no" counted as a failure.
Keel's prediction was written before any text was read (`round12/PREDICTION.md`).

## Set-up

- **Writers.** Two fresh writers (W, X) who read only Caplet's writing (`CORPUS.md`, and the IPS it links to,
  `FINAL_IPS_as_submitted.txt`) and the facts (`FACTS_PLAIN.md` version 3). Each wrote three passages of 220-280 words
  as the team: P1 the ten payments, P3 the 2031 range, P4 her flexibility (P2, the 2028 deposit, was round 11's
  clearest topic and was left out). Brief `round12/brief_r12.md`; texts `round12/writer_W.md`, `writer_X.md`.
- **Controls.** Version 61 (21 sentences; Caplet followed only 1, 5, 6 and 8), Caplet's own IPS paragraphs 3 and 4,
  and round 11's two kept passages (K's P2, V's P4).
- **Readers.** Four blind readers who know only the case brief, each in a role: a finance professor judging the
  competition, a strictly literal reader, a logician, the client. Each read version 61 first, then ten passages in its
  own shuffled order. Per sentence: Follow (1 first time, 2 one reread, 3 more), Sense, Why, the fault.
  `round12/build_packs_r12.py`, `packs/`, `readings/R1.md`-`R4.md`, `score_r12.py`, `SCORES_R12.md`. Readers are
  simulated (never people).

## Results

**1. The Why column does not catch Caplet's empty sentences.** Of the five version 61 sentences Caplet could not follow
and round 11's readers all passed (V12, V13, V16, V20, V21), the Why column caught none: one "no" in twenty judgements.
Each reader's flags on Caplet's seventeen rose only from 34 to 38 of 68 in all. Keel predicted at least three of the
five. Asked whether a reason is given, a simulated reader finds the sentence's own reason and says yes; it does not ask
whether that reason explains anything. So the column cannot be the test of Caplet's primary problem, and round 14 tries
another (below).

**2. It does find missing reasons in new text, and they are the same few.** Where the writers took a step and gave no
reason, all or nearly all readers said so:

| What readers could not explain from the page | Sentences (readers of 4) |
|---|---|
| Why buy shares at all | W3.4 (4), and Caplet's own C4.3 (2) |
| Why exactly half the shares are moved, and what the other half is for | W3.5 (4), X3.6 (4), V4.2 (3) |
| Why ten Treasuries already bought need their interest to earn interest | W1.6 (3), X1.5 (4), K2.4 (2) |
| Why a shortfall found in 2033 could not be closed from money already held | W1.8 (2), X1.7 (3) |
| Why a gap that size means building should wait | W4.11 (3), X4.13 (3) |

The fact sheet held the facts behind each, but not the reason in plain words, so version 5 (today) adds them: the
IPS's own reason for shares ("only money you haven't promised yet goes into shares, where it can grow"); why money
already held could not close a 2033 gap (it is promised to the building, or it is a share price); why the ten rely on
reinvested interest; why a building already started can no longer be made smaller or later.

**3. Rereads did not fall.** Writer X 24% (22% without the splitter's error below), writer W 32%, the same as round
11's fresh writers (24-32%), against 8% for Caplet's own paragraphs and 49% for version 61. Keel predicted 15-22%.

| Text | Reread | No sense | Why N | Any failure | Clean for all four |
|---|---|---|---|---|---|
| Version 61 | 49% | 2% | 17% | 54% | 33% |
| Caplet's IPS paragraphs 3-4 | 8% | 10% | 14% | 25% | 33% |
| Writer X | 24% | 1% | 8% | 28% | 51% |
| Writer W | 32% | 2% | 14% | 39% | 33% |
| Round 11's K, P2 | 4% | 4% | 16% | 19% | 50% |
| Round 11's V, P4 | 27% | 0% | 26% | 40% | 50% |

By passage, the worst was W's P3 (58% of judgements failed) and the best X's P4 (23%). By topic, the range (P3) failed
most (40%) and her flexibility (P4) least (27%); Keel predicted the range worst for Why (right: 14%) and the ten
payments best (wrong: P4 was, at 6%).

**4. What made readers reread was rarely the hard idea.** Every sentence that all four readers reread had one of five
faults:
- A phrase that means nothing until the next sentence: "its ends say different true things" (X3.10), "the two ends were
  settled three years apart" (W3.8).
- A figure whose base is not on the page: "about $11,500 more" (V4.11), "half the shares ... buy Treasuries for ...
  $115,000" when the other half is worth about $21,200 (X4.1), "more of IBTM" when the reader was never told she
  already holds it (W3.2).
- Two dates or two forms in one clause: "returns to Laura by 2042, worth about $46,600 at the start of 2033" (X1.10);
  "about 1 in 6 ... and 80 in 100" (W1.7); 2000 standing for 2028 and 2003 for 2031 (V4.8).
- A word with two readings: "real two-year moves" heard as inflation-adjusted (W4.6, X4.8; it meant actual).
- One assumption said twice in different words, which reads as circular: "as if its interest earned nothing more ...
  even if its cash earns nothing" (W3.3).

Caplet's own IPS sentence "Held to the end, these pay what they say" failed with three of four readers, for the
funds: an iBonds fund has no stated payout. The report's fund sentence already says what a fund pays (`WORDS.md`).

**5. "We" stayed at a third of Caplet's rate.** Caplet's IPS uses "we", "our" or "us" about 2.4 times per 100 words;
both writers used it 0.7 times, although the brief asked for "we" as the IPS uses it. Keel predicted 1.5-3.5. The
reason is visible in the text: the steps are done by money, not people ("$81,244 of her second deposit buys more of
IBTM", "half of those shares are sold"), the shape `WHY_V61_FAILED.md` names. The IPS is a letter in which "we" do
things for "you"; a report about Laura in the third person loses that pairing unless the writer says who acts.

**6. A scoring fault.** The sentence splitter broke "J.P. Morgan" into two sentences three times (W4.2, X3.7, X4.3),
and readers counted the broken row as a reread. Without those rows writer X's rereads are 22% and W's 32%. The
splitter is fixed for later rounds.

## What changes

- **For the method.** The Why column stays, because it finds missing reasons in new text (finding 2). It is not the
  test of empty reasons, so round 14 adds a cold retelling: after reading a passage once, the reader puts it away and
  writes, for each step, the reason the passage gave. A retelling that only restates the step ("they buy Treasuries
  because they buy Treasuries for the payments") marks an empty reason, and it is calibrated first on Caplet's
  seventeen version 61 lines, where Keel will count it as working only if it catches at least three of the five that
  every reader has passed so far.
- **For the writers.** Fact sheet version 5 gives the reasons readers asked for (finding 2), says "actual" for the
  currency test and which flexibility it used, and writes the history's two eras in one form ("80 in 100 ... about 17
  in 100"). Round 14's writers start with the "continuing" exercise from the voice programme (`README.md`, the
  method): they read the IPS aloud and keep writing from its last line, as the team, so the people doing each step are
  in the sentence before the report's subject arrives. The brief names `FINAL_IPS_as_submitted.txt` (writers W and X
  found it only through CORPUS's link).
- **For the report's structure.** The range's reason for being a range is said in the same sentence as the range
  (finding 4's first fault), and the half moved and the half kept are introduced together, each with its reason
  (finding 2), carried into `ARGUMENT_TREE.md` section 5.

## Against the prediction

The Why column catching three of the five: wrong (none). Readers' flags rising to 11-13 of 17 each: wrong (mean 9.5).
Rereads 15-22%: wrong (24% and 32%). "No sense" 4-8%: lower (1-2%). Why N 10-20%: right (8% and 14%). Caplet's
controls about 10% rereads and 15% Why N: right (8% and 14%). The range failing Why most: right. "We" 1.5-3.5 per 100
words: wrong (0.7).
