# Practice: ten exercises on Caplet's case, and what they taught (27 Oct 2026)

AI-generated (Claude Code) voice study. Every piece is an AI DRAFT exercise, written to practise a voice on Caplet's
real case. **None is IPS text and none is for submission.** Each file has the piece, then a critique of what worked
and what still reads like plastic.

| # | Manner | Piece | One line worth keeping | Verdict |
|---|---|---|---|---|
| E01 | Howard Marks memo | [Contract and mood](exercises/E01_marks_memo.md) | "You can be owed the money, or you can hope for it." | Best opening of the study; "Neither is better" is false balance |
| E02 | Buffett confession | [The envelope and the cut-up cheque](exercises/E02_buffett_confession.md) | "a postdated cheque, cut into pieces and posted to you twice a year" | Real mistake explains the real risk; Final Report, Articulation |
| E03 | Matt Levine explainer | [The bank's favourite product, home-made](exercises/E03_levine_toy.md) | "protected by Lehman Brothers" | Mechanism before label; cure for lab prose |
| E04 | Sell-side note | [Maturity, underrated](exercises/E04_sellside_note.md) | "Inflation can make $50,000 buy less. It cannot make $50,000 cost more." | Strongest single line; voiceless by design |
| E05 | Admissions essay | [Safe for](exercises/E05_admissions_essay.md) | "a bet on interest rates with a very respectable name" | Shape for the Final Report's opening |
| E06 | Ahaan pastiche | [Buy and hold your breath](exercises/E06_ahaan_pastiche.md) | "ten one-year windows, each with a $50,000 bill nailed to the door" | Closest in spirit; borrows his tics too literally |
| E07 | Paul Graham one-liners | [Twelve, then the cull](exercises/E07_graham_aphorisms.md) | "A ladder is admitting you do know when." | 8 of 12 died: symmetry is not insight |
| E08 | Lab rescue | [L-10 rewritten for a reader](exercises/E08_lab_rewrite.md) | "A few thousand dollars is not a disaster. A missed payment is." | Same facts, a judge can now feel them |
| E09 | Five voices, one idea | [The 2031 range](exercises/E09_five_voices_one_idea.md) | "a hope with a formula attached, which is about as honest as hope gets" | The method for finding which sentences are ours |
| E10 | The converged voice | [The deposit that isn't money yet](exercises/E10_convergence_human_capital.md) | "Bad news travels in pairs." | Nearest to Ahaan's fingerprint; an idea, not a holding |

## The scoreboard (fingerprint.py, 27 Oct)
Ahaan's three essays are the target. Bold = inside or near his band.

| | Ahaan | Keel D4 | E01 | E02 | E03 | E04 | E05 | E06 | E08* | E09 | E10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sentence-length swing | 0.66 | 0.49 | **0.63** | 0.50 | 0.54 | **0.62** | 0.55 | **0.73** | 0.59 | **0.70** | **0.63** |
| short (6 words or fewer) | 17% | 14% | 29% | **15%** | **15%** | **17%** | **20%** | 32% | **19%** | 24% | **18%** |
| long (30+ words) | 18% | 4% | 8% | **15%** | 5% | 9% | 5% | 11% | 12% | 3% | **24%** |
| numerals per 100 words | 0.6 | 3.1 | **1.5** | **1.2** | 2.6 | 2.6 | 3.7 | 2.8 | 6.9 | 2.3 | **1.1** |
| idea-words per 100 | 4.5 | 1.2 | 2.5 | 0.0 | 0.7 | 2.4 | 1.1 | 2.0 | 0.8 | 0.6 | 2.0 |
| "X, not Y" per 1,000 | 2.4 | 2.1 | **0** | **0** | **3.2** | **2.9** | **0** | **0** | 7.7 | 6.2 | **0** |

*E08 counts the Lab's "before" paragraph too.

## What practice taught (honestly)
1. **My first correction was the wrong one.** Told that Keel's prose was flat, I made it punchy: E01 and E06 have 29%
   and 32% short sentences, nearly double Ahaan's. Punchy is the *other* AI voice, the LinkedIn one. Ahaan's short
   sentences are rare and earned by the long ones before them.
2. **The long sentence and the idea arrive together.** Only E10, which argues about an idea (human capital) rather
   than a holding, reached Ahaan's share of long sentences without sounding padded. When a paragraph has an idea to
   develop, a long sentence is where it moves; when it only has facts, a long sentence is a list. So the fix for
   "just telling facts" is not a style rule. It is to find the idea first.
3. **Numbers are the habit hardest to break.** Only E01, E02 and E10 got under 1.5 per 100 words. Every other piece
   reached for a figure where a sentence would have done. Rule: one number per paragraph, and it must win the point.
4. **Symmetry is the tell that survives every word list.** E07 lost 8 of 12 lines, all parallel pairs. E09's five
   voices pushed "X, not Y" to 6 per 1,000 because every voice reached for the same shape. Ahaan does it once every
   400 words and makes it a chiasmus.
5. **Confession and opponent were the two moves that changed the feel most.** E02 (a real mistake) and E06 (the
   all-stock sceptic in his own words) read as written by a person, even where their numbers drift from the band.
   Neither move can be added by an editor at the end; the piece has to be built around it.
6. **Every voice is a costume except the one with a stake.** Marks, Levine, Buffett and the banks all sound like
   *someone*, but only because each has a position they'd defend at dinner. The Caplet voice needs the same: a few
   opinions Keel will defend out loud (they are listed in `06_voice_guide.md` section 1).

## Re-run
`python3 keel/voice/fingerprint.py A=/mnt/project-files/voice/ahaan_essays_2026-10-24.txt E10=keel/voice/exercises/E10_convergence_human_capital.md`
