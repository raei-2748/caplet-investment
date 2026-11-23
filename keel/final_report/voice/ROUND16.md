# Voice round 16: one image in Laura's words to co-sponsors, with and without it (Mon 23 Nov 2026, evening)

Panel 5 (Mon 23 Nov) took the conceit out of 3d: ink, learned as money held, meets literal ink, a signature, in that
part's aha (owned against signed). The tree kept one candidate, "a signature is the other kind of ink", and a rule:
3d carries it only if readers follow it on one reading (`ARGUMENT_TREE.md` Branch 5). Round 16 tested it. Keel's
prediction was written before anyone read (`round16/PREDICTION.md`).

## Set-up

- **Writer.** One fresh writer who read only Caplet's writing (`CORPUS.md`, the IPS), the facts (`FACTS_PLAIN.md`
  version 7) and the case (brief `round16/brief_r16_X.md`). It carried the IPS on from its last line (about 150 words,
  warm-up), then wrote three pieces in Caplet's voice for the judges: D, the report's first use of pencil and ink (99
  words); P, the team's lead-in (signed as well as held, with Lehman and Spelman) and Laura's own words to co-sponsors
  (228 words); and T, P word for word with one sentence added to the lead-in: "A signature is the other kind of ink: so
  far, ink has meant money that Treasuries held for Laura will pay, and her signature is her written promise to give
  it, the kind of ink a funder can count." The builder checked that T differs from P by that sentence alone. Texts in
  `round16/writer_X.md`; "we" per 100 words: D 1.0, P 1.3, T 1.1.
- **Readers.** Six blind readers in two matched arms, each with one role: a finance professor judging, a strictly
  literal reader, the client. Each read version 61 first (calibration: Caplet followed 4 of its 21 sentences), then
  Caplet's own IPS paragraph C3 (control), then D, then T (readers 1-3) or P (readers 4-6), marking every sentence
  Follow 1-3 and Sense, with a paraphrase for the last passage; then four questions from memory. `round16/build_packs_r16.py`,
  `packs/`, `readings/R1-R6.md`, scores in `round16/SCORES_R16.md`. Readers are simulated, never people.

## Results

**1. The turn fails the rule: 0 of 3 followed it on one reading.** All three T readers gave it a 2 and understood it
on a second look; the literal reader marked it N ("ink now means something different, and the sentence admits it"),
the professor "?" ("it stretches the word"). Keel predicted at most 2 of 3; it was none.

**2. It added nothing to the point it was meant to carry.** All six readers answered "owning against signing" right
from memory, and all six named Lehman and Spelman. The plain lead-in already says it: owning shows the money exists,
the signature says it will be given, and a gift office counts the letter.

**3. It cost the first meaning.** All three T readers named "ink" as the word that changed meaning; no P reader did
(one P reader: "ink does not appear in the last passage; it is replaced by held and signed"). Each T reader said it
helped a little and blurred the rule they had just learned: "ink was about her ability to pay and then became about
her commitment to pay" (reader 1); "the first definition no longer held without that extra clause" (reader 2).

So 3d stays plain, as panel 5 left it. The image stays in CONCEIT's store, retired from 3d.

**4. Laura's words themselves need four repairs, in both arms.** Passage 3 was followed first time in about half its
sentences (15 of 30 in T, 13 of 27 in P), against all 30 of Caplet's own paragraph. The faults, each named by two to
five of six readers, all lie in what the tree and the brief asked the writer to say, not in the image:

- **Why the top, not only why she can.** Four readers: "whatever figure I choose, the money for it is already mine"
  says why she can sign any figure, not why she signs the top rather than the bottom. The IPS gives the reason: the
  shares' returns "help determine your maximum facility contribution", and the other half is "promised to no one"
  (l.15). The half moved in January 2031 is the building's half, and once moved it is held, so the top is a figure she
  gives without touching her flexibility. Now in the fact sheet (version 7, Monday evening) and the tree.
- **When the ten were bought.** Two readers: "$50,000 a year ... held in Treasuries since January 2028" reads as
  wrong after D, since most of each payment was bought in January 2027. Say "bought from January 2027 and complete
  since January 2028" (the tree's line now says so; it had said "held in Treasuries from January 2028").
- **Strong words go on the Treasuries, never on the fund's payout.** Two readers flagged "Those Treasuries are
  guaranteed by the US government, and no market can now change what they pay": the top rests on IBTM, a fund, whose
  payout version 61 had told them is not fixed. Already a rule (a fund share is said as one; WORDS); the writer missed
  it, so the 27 Nov writers' fact sheet keeps it beside Laura's words.
- **One idea per sentence for the range.** Five readers gave the range sentence a 2: the purpose and the range ran
  together in the numbering, and "up to $115,000 since January 2031" asked them to hold two dates and two figures.
  And "I commit to it in writing" left two readers unsure whether "it" was $615,000 or $115,000.

**5. The first definition of ink and pencil was a 2 for all six.** "A figure is in ink once Treasuries held for her
will pay it on its date, and in pencil while none will yet" was understood on a second look by every reader: "while
none will yet" is compressed, and the shares as pencil surprised until the example came. Round 7 had the definition
followed 6 of 6 when it was given at first use in full; here the writer put both words in one sentence and took "while
none will yet" from the fact sheet itself, so the fact sheet's pencil line now says it whole ("while no Treasury held
for her will pay it yet").

## What changes

- `ARGUMENT_TREE.md` Branch 5: the conceit line records round 16 (0 of 3; 3d plain, final); the commitment's ten are
  "bought from January 2027, complete since January 2028"; "why she signs for the top" carries the IPS's reason for the
  top over the bottom.
- `CONCEIT.md` 3d row and `WORDS.md` row 59: "a signature is the other kind of ink" tested and retired from 3d.
- `FACTS_PLAIN.md` version 7, Monday evening: why the top rather than the bottom, strong words on the Treasuries and
  not the fund's payout beside it, and the pencil line said whole.
- Keel's predictions: 1 held (more strongly than predicted), 2 held, 3 held, 4 held.
