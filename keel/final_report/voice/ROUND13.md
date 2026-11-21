# Voice round 13: does a 2,400-word explanation hold its reader, and does set-up and payoff help? (Sun 22 Nov 2026)

Day 15 asked for a round on how the best long-form explainers hold a reader across 2,000 words or more, tested blind.
The Final Report's Section 3 is about 1,900 words read in one sitting, so this is the first test of the report's
length rather than its sentences.

## Set-up

- **Writers.** Two fresh writers, each writing one continuous piece of 2,000-2,400 words that explains Laura's plan from
  the deposits to the figure she tells co-sponsors in 2031, as the team ("we"), from Caplet's own writing
  (`CORPUS.md` and the IPS it points to) and the facts (`FACTS_PLAIN.md` version 3). Writer **L** first studied how
  admired long-form explainers hold a reader (it chose Patrick McKenzie, "Banking in very uncertain times", Bits about
  Money, 2023; John McPhee, "Structure", The New Yorker, 2013; Paul Graham, "How to Make Wealth", 2004), read for how
  they are built and not for their words. Writer **M** wrote without that reading (the control). Briefs:
  `round13/brief_r13_L.md`, `brief_r13_M.md`; pieces `round13/writer_L.md` (26 paragraphs), `writer_M.md` (28).
- **Readers.** Six blind readers who know only the case brief, three per piece, each reading one piece once so that
  recall is not helped by the other: an intelligent general reader, a finance professor judging the competition, and
  the client. While reading, each marked every paragraph "with it", "drifting" or "lost"; then, before looking back,
  wrote the argument in three sentences, what it remembered most, any moment where something earlier paid off, any
  question left unanswered and any sentence that announced a point instead of making it; then scored each paragraph
  (Follow 1-3; Why Y/N, "could you tell a friend why, from the page alone"). `round13/build_packs_r13.py`,
  `readings/R1.md`-`R6.md`, `score_r13.py`, `SCORES_R13.md`. Readers are simulated (never people).
- **Prediction** (`round12/PREDICTION.md`, written before any piece was read): L's readers would recall the argument
  better and name more payoffs; M would lose readers at three or more paragraphs each, L at two or fewer; at least one of
  L's readers would hear a set-up as a signpost.

## Results

| Piece | Readers | Paragraph marks "lost" | "Drifting" | Paragraphs reread | Why N | Argument right in three sentences |
|---|---|---|---|---|---|---|
| L (studied long-form) | 3 | 0 of 78 | 6 (8%) | 47% | 31% | 3 of 3 |
| M (control) | 3 | 0 of 84 | 7 (8%) | 48% | 24% | 3 of 3 |

**1. Both pieces held all six readers.** No reader marked a single paragraph "lost", all six stated the plan's argument
correctly from memory, and all six named pencil and ink first or second among what they remembered. Plain explanation
in the team's voice, one date at a time, holds a reader who knows the case for 2,400 words. Keel's prediction that the
control would lose its readers was wrong.

**2. The biggest payoff comes from a question planted at the start.** L opened on two questions a reader can hold
without any finance: how $450,000 becomes about $615,000 of commitments, and why a figure the team calls certain waits
until 2031 and arrives as a range. All three of L's readers named these as their strongest "so that is why" moments,
unprompted and with paragraph numbers (the first answered in its sixth paragraph by Treasuries bought years early, the
second in its seventeenth and eighteenth by the range's two ends being two dates). M's readers named as many payoffs
(six to eight each), but local ones, a term set up in one paragraph and used in the next, plus the opening image
returning in the last paragraph (two of three). Local set-ups make a piece easy to follow; only a planted question gives
the click.

**3. Every reader would have stopped at the same place: just after the main question was answered.** All six named it
(L's nineteenth and twentieth paragraphs, M's nineteenth to twenty-third): once the range was explained, the trade-off
figures and the fund's risks that followed read as "an appendix", "fine print", "a footnote whose numbers I had to
rebuild", "the argument is over and the rest is decoration". Nothing planted earlier was waiting to be paid there. Two
readers gave the same remedy: put each risk beside the claim it tests ("put the fund risks next to the 'certain' claim
... so the certainty is earned where it is made"), one risk per sentence with who covers it.

**4. A plant that announces is heard as a signpost.** L's "It will matter again" (two of three named it as a teaser;
the third counted it a payoff) and "the order is the argument"; M's "her own trade has the right picture for what
replaced it" (two of three). Keel predicted at least one; it was two in each piece. What worked in L's opening was a
question the facts themselves raise, never a promise that something will matter.

**5. The same unanswered questions in both pieces, so the gap was in the facts, not the writing.** Readers of both
asked: why exactly half the shares; why buy the longest-dated payments first; why about $37,000 of extra Treasuries
covers a gap of about $55,000; why reinvested interest fell short so often from 1981 and rarely before; why the top is
$115,000 at a 5% return yet reached in only about 57 futures in 100; why $5,000 more of stated top costs more than
$5,000 of her flexibility; where "five business days late" comes from; what Laura does if the late-2032 fund ends early.
The fact sheet stated each step without its reason. Version 4 (today) gives each its reason.

**6. The dense places were the same in both.** The extra Treasuries (L's eighth to tenth paragraphs and M's ninth to
eleventh, flagged by three of three) and the fund's risks (L's twenty-fourth and twenty-fifth, M's twenty-seventh,
three of three). One reader heard M's two extra images from Laura's trade (the royalty reserve, the printer's cut line)
as decoration; the client remembered the royalty reserve "from my own contracts".

## What changes

- **For the report's structure** (carried into `ARGUMENT_TREE.md` section 5): Section 3 plants its questions where the
  facts raise them and pays them later, never with an announcement. The sentence that first calls the range certain
  (3c) plants its limit, and 3e's list of how each promise could break is that limit paid, one risk per sentence with
  who covers it, so 3e reads as the answer to a question already asked and not as an appendix.
- **For the writers on 27 Nov:** the fact sheet's version 4 gives the reason for each step readers asked about; one
  image per part; the extra Treasuries paragraph gets its why (their own interest and principal, counted without
  reinvesting, add up to more than they cost).
- **For the method:** a long piece is scored by paragraph and by recall; round 18 or later reads a whole part of the
  report the same way.

## Against the prediction

Recall better for L: wrong (both three of three). Losing the thread: wrong (no paragraph lost by anyone; drifting 8% in
each). The places readers drifted were not the range, as predicted, but the extra Treasuries and the fund's risks.
L's set-ups heard as signposts: right (two of three).
