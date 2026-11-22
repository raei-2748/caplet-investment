# Voice round 15: Keel's prediction, written before any of the round's text was read (Mon 23 Nov 2026, morning)

Rounds 12 and 14 found that no simulated test reproduces the lines Caplet could not follow: a per-sentence "why, from
the page alone?" column caught none of the five version 61 sentences (round 12), and a cold retelling caught 2 of 5
(round 14). So round 15 stops looking for a proxy for Caplet's ear and tests depth: whether a passage gives a reader
enough working to answer "what happens if" questions about the plan from the page alone. Caplet's own failing lines
stay the ground truth for single sentences (Book 22).

Design. Two fresh writers read only CORPUS.md, the IPS and FACTS_PLAIN version 6, first carry the IPS on for about 200
words from its last line, then write one 650-750-word piece on Laura's facility contribution and her 2031 range, read
on its own with only the case summary. Writer V's brief adds one paragraph asking for the working that lets a reader
answer "what happens if" questions (if shares halve, if interest rates fall to 1% and stay there, if the building
costs more); writer W's does not. Control: the IPS's own paragraphs on the building and the reasons to change (l.15
and l.17, about 190 words), which were never meant to carry this much. Three blind readers read the three texts once
each, in different orders, with the case summary only, then answer nine questions without looking back (the key is in
`DEPTH_KEY.md`, written from FACTS_PLAIN version 6 before any text was read). A blind scorer marks each answer right,
partly right, wrong or not on the page, and each reader counts rereads.

What Keel expects:

1. **Depth.** Right or partly right answers: V 6-7 of 9 per reader, W 4-6, the IPS control 3-4. The questions most
   often missed in every text: 6 (what could stop the stated top being paid) and 7 (building costs 25% higher, who
   pays), because both need the limits, which a piece written in the team's confident voice tends to leave out.
2. **The instruction matters more than the writer.** V beats W by at least 1.5 right answers per reader on average.
   If it does not, writer variance is the larger effect again (as in round 10) and the instruction adds nothing.
3. **The cost of depth.** V is reread more than W (V 20-30% of paragraphs, W 15-25%; Caplet's own 8% in round 12),
   because giving the working adds figures.
4. **"We".** Both writers, having first continued the letter, use "we" at 1.5-3 per 100 words in the piece (round 14:
   1.6-2.9; Caplet's IPS 2.4).
5. **The most useful result for 27 Nov** is whichever questions both writers leave unanswerable: those mark the steps
   whose reason the writing team must put on the page.
