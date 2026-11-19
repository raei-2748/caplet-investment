# Comprehension study 1: sentences that still make no sense once decoded (Thu 19 Nov 2026, evening)

Book 21 (Caplet, 17:47 and 17:58 Sydney): "the primary problem is that, even after reading it 3 times and understanding
the logical chain, the sentence simply does not make any sense." This study asks where that happens, in Keel's last
IPS drafts and in this week's Final Report prose, and why. Notes for the voice study, not report prose. Readers are
simulated (never people); their scores say how the words read to them, and Book 10 warns that such readers may follow
AI prose too easily, so Caplet's own list of failing lines (asked for, pending) is the ground truth they will be scored
against.

**Files.** Keel's prediction, written and pushed before any reader saw a text: `comprehension/PREDICTION.md`. Packs,
key and sentence list: `comprehension/packs/`, `KEY.md`, `sentences.json` (563 sentences). Sixteen readings:
`comprehension/readings/`. Scores: `comprehension/SCORES.md` (built by `score.py`). Prior art:
`comprehension/PRIOR_ART_sense.md`, `PRIOR_ART_erudite.md` (when the two research workers return).

## Method in brief

Six readers read four IPS drafts blind and whole (Keel's versions 63, 62 and 57, and Caplet's submitted IPS), each in
its own order and role (a sharp essay-writing student, a finance professor judging, a newspaper sub-editor, a strictly
literal reader, a logician, a reader in the client's position). Then sentence by sentence: did they follow it first
time (Follow 1-3), does it make sense once followed (Sense Y/N), a plain paraphrase, and the fault in their own words.
Eight more readers (an essayist and a logician per pack) did the same for this week's Final Report prose: the fresh
writers' passages from voice rounds 8, 9 and 10, and the nine items of cold aha test 8, each pack salted with three of
Caplet's own Trading Notes reflections as controls. Two read the fact sheet the fresh writers write from
(`FACTS_PLAIN.md`).

## Results

| Text | Sentences | Judgements | Reread | No sense once followed | Half or more of readers say no sense |
|---|---|---|---|---|---|
| Caplet's IPS (control) | 32 | 192 | 13% | **5%** | 0 |
| Keel version 63 (mostly Caplet's own words) | 23 | 138 | 7% | 1% | 0 |
| Keel version 57 (4 Nov) | 30 | 180 | 26% | 2% | 0 |
| Keel version 62 (6 Nov, the last all-Keel draft) | 22 | 132 | **64%** | **20%** | 5 |
| Fresh writers, voice round 8 | 76 | 152 | 26% | 8% | 8 |
| Fresh writers, voice round 9 | 93 | 186 | 35% | 22% | 24 |
| Fresh writers, voice round 10 | 83 | 166 | 48% | 16% | 19 |
| Aha test 8 items (Keel's syntheses) | 61 | 122 | 45% | 21% | 14 |
| The fact sheet the fresh writers write from (Keel) | 99 | 198 | 52% | **29%** | 33 |
| Caplet's Trading Notes reflections (control, read out of context) | 44 | 88 | 55% | 32% | 17 |

How to read it. Against Caplet's IPS, version 62 makes readers reread five times as often and loses them four times as
often. Version 63 reads as well as Caplet's IPS because, as Caplet said, it is mostly Caplet's writing. The surprise is
below the line: **this week's Final Report prose fails as often as version 62 did, and the fact sheet the writers work
from fails most of all.** The one warning about the readers is the last row: Caplet's Trading Notes reflections, read
without the trades they reflect on and full of bond terms (net asset value, par, duration-matching), were scored harshly
too. The readers punish missing context and unexplained terms hard, so the table ranks texts against each other; it does
not say Caplet's reflections are nonsense, and Caplet's list will show how far these readers can be trusted.

## Version 62 against Caplet's IPS

All six readers said these version 62 sentences made no sense once followed:
- "Those ten rungs are the first meaning of XR, and crushing the caplet would mean selling one before it repays." A
  name with numbered meanings, explaining nothing the reader needs.
- "In 2028, what the ladder doesn't need buys more of the fund behind the 2033 payment, enough to return about all of
  it by December 2032, which sets the bottom of her range." A fund never introduced, an "it" with three owners, a range
  never defined.
- "It is bought in 2028, not 2031, because the creative residency in Taiwan can't depend on shares ..." The nearest
  thing "it" can be is the share fund, so the reason points the wrong way; and the date nobody had raised is answered.

Half or more also failed the pitch's "The rest buys the bottom of her 2031 range" (a figure treated as something you
can buy) and "In 2033 her operating reserve is already in place: the ladder, the extra reserve and the money waiting for
them" (money waiting for whom?). Every one of the 22 sentences after the pitch's first was reread by most readers.

Caplet's IPS failed in no sentence by a majority. Its sentences do what Voice study 1 found in November and what the
readers named again: people act ("we'll use your first deposit"), each sentence carries one step, every reason is said
out loud ("because it's fixed and non-negotiable"), the worry is named and answered ("But worry not"), and the nouns are
Laura's (advances, speaking fees, licences). Its few flags were mild: "So we hedge it!" (three readers wanted to know
what hedging a career means) and "From 2033 the Treasuries are the operating reserve" (all six reread it, wanting to know
which Treasuries).

## The finding that matters most: the guards became the nonsense

The worst sentences in this week's prose are not clumsy versions of good ideas. They are Keel's own corrections,
written into sentences. Three examples, each failed by every reader who saw it:
- "The IPS's two reasons to change the plan, a missed deposit and a Treasury default, are a separate list: exits for
  when it can't be carried out." This is card Q109's guard ("never 'only two things can break the plan'") turned into
  prose, in six passages across two rounds. Readers: "answers a question nobody asked"; in two passages it contradicts
  the sentence before it, which had just named a default and a missed deposit as ways the payments fail.
- "Of the case's five areas, the return we assume for shares barely moves the top, timing is the 2028 deposit, outside
  money never touches the payments, and inflation changes ..." Card Q37's checklist turned into prose, in four passages.
  It promises five and lists four, and "timing is the 2028 deposit" is a label where a reason should be.
- "Short of a default, that would take fund costs beyond the fees passing about 2% of what the two Treasury funds behind
  the top pay; the margin is only part of that room ..." NUMBERS 8u's caveat turned into prose: "the margin", "that
  room", "the top" and "the move" are Keel's private names, never set up on the page.

The fact sheet explains how they got there. It is the only thing the fresh writers read besides Caplet's writing, and 29%
of its sentences failed: it carries struck phrases, reviewers' codes ("coherence reader 8, L14"), and instructions about
words ("never say they 'complete' or 'finish' the ten") mixed in with the facts. A writer who reads a fact sheet full of
defences writes defences.

This is Caplet's two complaints of Thursday evening as one fault. The research has been hunting small corrections, and
each correction has become a guard; the guards reach the writers; and a guard written as a sentence is, almost by
definition, a sentence that defends against an objection the reader never had, in words the reader was never given.
Cutting the guards out of what writers see fixes much of the comprehension problem and frees the research to look for
ideas.

## What "decoded, still no sense" turned out to be

The readers' own words for the faults, counted across all 563 sentences (one sentence can carry several):

| Fault, in the readers' words | Count | Typical example |
|---|---|---|
| Points at nothing, or a term never introduced | 111 | "the fund behind the 2033 payment"; "the move"; "that room"; "the IPS's two reasons" never named |
| Doesn't follow (the because or so does not produce the claim) | 39 | "buying extra ordinary Treasuries is the only way left to pass the old test" (other ways existed) |
| Contradicts another sentence nearby | 36 | the two reasons named as ways payments fail, then called "not ways a promise fails" |
| The wrong kind of thing | 23 | a range's bottom bought; "both ends are Treasuries she owns"; a date called a danger; "the exception" is a person |
| Overclaims | 15 | "every co-sponsor's target is exact" |
| Answers a question nobody asked | 13 | the two-reasons sentence; "Our first model just priced the change." |
| An image or a label in place of a reason | 13 | the meanings of XR; "That half is the bought deal" |
| Circular or empty | 12 | "the plan works as long as nobody crushes it" |
| Impossible as stated | 5 | interest put into shares in 2028 that will not be paid until 2032 |

Keel's prediction named five ways (the image does the explaining; money that does not exist yet is spent; a because that
does not connect; things given properties they cannot have; answers to questions nobody asked). The readers confirmed
four, and added two Keel did not predict and should have: **contradiction inside a passage** (each sentence written to
satisfy a different check, so neighbours disagree) and, by far the largest, **private names**. On version 62 the
prediction's hits were the meanings of XR, the fund behind the 2033 payment, the "bought in 2028, not 2031" sentence,
"XR's second meaning" and "both ends are owned"; its misses were the pitch's "buys the bottom of her range" and the
"money waiting for them" sentence. One prediction the readers did not confirm is worth keeping in view: "Because it
costs less than it returns, the difference, roughly its interest, goes into one world index fund" describes interest
being invested four years before it is paid, and only the literal reader said so; the other five decoded it into the
sense Keel meant. That is Book 10's warning in a single sentence, and Caplet's list will show which way it falls.

## What changes now

1. **The fact sheet is rebuilt as facts only**: what happens, who does it, when, and the figure, with no guards, codes,
   struck phrases or word instructions (`FACTS_PLAIN.md`, version 2, Fri 20 Nov). The guards stay in Keel's checking
   files, which writers never see.
2. **A check may correct a false fact; it may not add a defending clause.** If a point needs a sentence to fend off an
   objection no reader would raise, the point goes, not the sentence in.
3. **A sense pass on Fri 27 Nov**, after every draft: a literal reader and a logician go sentence by sentence, as in this
   study; a sentence whose paraphrase needs words the page did not give, or whose because does not produce its claim, is
   rewritten whole, never squeezed.
4. **Every reader score is checked against Caplet's list** when it arrives (version 62, which Caplet is reading now).
5. **The aha items are rewritten as people doing things in the order they happen** before test 9, and the
   cold readers' brief adds the sense question.

## Next

The failing lines, rewritten and retested blind, go into voice round 11 (Fri 20 Nov) with the essay study's
second task (`ESSAY_STUDY.md`). Caplet's list of version 62 lines, when it comes, is matched line by line against
`PREDICTION.md` and against these readers.
