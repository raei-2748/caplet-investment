# Why Keel's prose tastes like plastic (diagnosis, 27 Oct 2026)

AI-generated (Claude Code) voice study, not for submission. Ray (27 Oct): "what you write is just telling facts ... it
is like eating plastic". Ahaan (24 Oct): it "STILL sounded AI ... aspects of AI writing transcend the kinds of things
which you can ban with a neat list". Both are right, and the reason can be measured.

## 1. The measurement
`fingerprint.py` counts how prose moves, not which words it uses. Run on 27 Oct (Ahaan's essays read from the private
project file; nothing of their text is in the repo):

| per piece | Ahaan, 3 essays | Ahaan, 5 books | Keel D1 | Keel D3 | Keel D4 | Genius Lab L-10 memo | Writing Room memo |
|---|---|---|---|---|---|---|---|
| words | 5,860 | 4,161 | 480 | 490 | 487 | 435 | 380 |
| sentence length swing (sd / mean) | **0.66** | **0.72** | 0.49 | 0.59 | 0.49 | 0.61 | 0.62 |
| long sentences (30+ words) | **18%** | 15% | 3% | 3% | 4% | 29% | 12% |
| numerals per 100 words | **0.6** | 0.4 | 2.7 | 2.9 | 3.1 | **11.3** | 7.9 |
| idea-words per 100 (-tion, -ity, -ness, -ment) | **4.5** | 1.6 | 1.5 | 1.4 | 1.2 | 0.7 | 0.8 |
| "X, not Y" / "rather than" per 1,000 | 2.4 | 2.6 | 4.2 | 2.0 | 2.1 | **9.2** | 7.9 |
| sentences opening on But / And / Yet / So | 11% | 8% | 3% | 5% | 7% | **0%** | 4% |
| brackets per 100 words | 0.2 | 0.6 | 0.0 | 0.2 | 0.4 | **4.4** | 4.5 |

Re-run: `python3 keel/voice/fingerprint.py A=/mnt/project-files/voice/ahaan_essays_2026-10-24.txt B=keel/BIBLE.md D4=keel/ips_rewrite/drafts/D4/ips.txt`

## 2. What the numbers say, in words

**Keel has amputated its long sentences.** Ahaan writes one sentence in five at 30+ words: the sentence that builds
a case clause by clause, with asides hung on dashes, before the short one lands. Keel's IPS drafts manage one in 25. Every
sentence sits between 10 and 25 words. That is the plastic feel: no build, so no release. The short punches in D4
("We refuse.") have nothing to punch out of. It happened for a reason Keel thought was good: a 500-word limit and
an Orwell rule ("if it is possible to cut a word out, always cut it out") applied sentence by sentence. Ahaan told
us the opposite on 24 Oct: cut a whole idea, never squeeze a good sentence shorter.

**Keel writes inventory, not argument.** Its drafts carry five times Ahaan's density of numerals and a third of his
idea-words. Ahaan's essays are about ideas (retribution, externalities, compatibilism) and use a number when a
number wins the point ("4 airlines now control 80%"). Keel's drafts are about holdings and dates, with the ideas
left implicit. A judge reading D4 learns what the plan owns. They have to infer what it believes. That is what Ray
means by "just telling facts".

**Genius Lab prose is the extreme case: a lab notebook pasted as a memo.** One numeral every nine words, a bracket
every 23, a "not X but Y" every 109, and not one sentence that starts with "But" or "So". Nobody in it is
arguing with anybody. Its findings are real and good (L-09, L-10): the payments are the weakest promise, and one
coverage rule fixes that. The writing hides them. Exercise 8 in `05_exercises.md` rewrites L-10 to show the difference.

**The antithesis tic.** "X, not Y" is the AI's favourite sentence because it sounds decisive without having to argue.
Ahaan uses it about once every 400 words and makes each one a chiasmus worth remembering ("not between the poor and
the planets ... between the planets and continued poverty"). The lab and Writing Room memos use it every 110-125.

**The brackets are stamps, not asides.** Ahaan's brackets wink: "(A non-exhaustive list)", "(though small)". Keel's
are provenance stamps: "(MODEL, 21 Oct)", "(8.4% if yields and stocks fall together)". Stamps are needed in a lab
log. In prose they are the sound of a machine covering itself.

## 3. Five deeper causes the counter can't see
1. **No opponent.** Every good piece in `02_reading_notes.md` argues with someone: Marks with the market's memory,
   Einhorn with the banks, Ahaan with the libertarians. Keel's drafts argue with no one, so every sentence has the
   same weight. D4's best lines are exactly the ones with an opponent ("ask Lehman's customers why"; "says the
   sceptic").
2. **No person.** Buffett and Ackman grade themselves; Graham corrects himself mid-thought; Cembalest admits he's not
   a futurist. Keel never admits a mistake, a surprise or a change of mind in its prose, so there is nobody there.
   Caplet has real ones (the STRIPS plan the 6 Oct email killed; the ladder that fits under the $300,000 deposit by
   about $1,000 on some days and not at all on others).
3. **Decoration instead of images that argue.** Marks's moving walkway *explains* 40 years of returns. Keel's pill
   images (coated beads, do not crush) mostly *label* things that were already explained. An image earns its place
   only if deleting it deletes part of the argument.
4. **Kicker inflation.** The Writing Room found it on 27 Oct: every slot ended on a quotable reversal, "a stand-up
   set, not a policy". Good writers spend a kicker the way they spend money.
5. **Writing to be checked, not to be read.** Keel's rooms review drafts for counts, facts and banned words, so the
   prose is shaped to pass a checker. Nobody in the office asks "would a judge read this paragraph twice because
   they enjoyed it?" Ahaan's Book 1 asked for exactly that ("the kind of thing they can honestly ENJOY reading").

## 4. What this means for the guide
- Restore the long sentence: one in five should build, clause on clause, and earn the short one after it.
- Halve the numerals; every number left must win an argument or be felt.
- Put the idea-words back: say what the plan *believes* (contract, mood, sequence, credibility), then show the holding.
- One opponent per paragraph, named in their own words.
- Brackets for winks only; provenance lives in the Final Report's notes.
These are rules 2-6 of `06_voice_guide.md`.
