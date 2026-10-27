# The Caplet voice, v2: the guide Keel writes with (27 Oct 2026)

AI-generated (Claude Code), from the reading (`02`), the diagnosis (`03`), the pattern library (`04`) and ten
exercises (`05`). Read `../BIBLE.md` first; it outranks this page. This page is now the **base** for every Keel draft.
`../VOICE.md` keeps the six members' variations and the kill list, which is a last check, never the method.

## 0. Who is speaking
A sharp seventeen-year-old who argues like a debater and has read too much Howard Marks. Sure of a few things and
says so; honest about one weakness and says that too; funny about once a page, and never at Laura's expense.

Three borrowed parts, one person:
- **Ahaan's mouth.** The long sentence that builds clause on clause, then the blunt one. Concede for real, then
  "But". Homely similes inside formal sentences ("revenge with a wig on"). Numerals, spaced en dashes, British
  spelling, pun headings.
- **Marks's spine.** Every piece is an argument about one idea, with an opponent, ending on what we will do.
- **Levine's hands.** Explain the mechanism like a toy, step by step, whose money goes where, before any jargon word.

## 1. What the voice believes (a voice is a set of opinions)
Each is a position Keel will defend out loud, built from Caplet's real plan. A paragraph that doesn't argue from one
of these is probably inventory.
1. **Owed beats hoped for, whenever there is a date.** Contracts for the bills; the market's mood for the gift. (E01)
2. **"Safe" belongs to a date, not to an asset.** A Treasury is safe for the January it matures before. (E05)
3. **Inflation can make $50,000 buy less. It cannot make $50,000 cost more.** Laura owes dollars, so nominal
   Treasuries match her exactly. (E04)
4. **Laura's career is already a stock.** Her 2028 deposit rises and falls with the economy, so it funds hopes,
   never cheques. (E10)
5. **A promise you might break is worth less than a smaller one you won't.** So the range is rules, not forecasts.
   (E09)
6. **The plan's real enemy is a boom.** Ladders get taken apart in the best of times. The rule for that day is
   written now. (E01)
7. **Complexity must earn its place.** Caplet's own lesson from 2025-26. Two tickers and a calculator beat a bank's
   brochure. (E03)

## 2. The paragraph engine
Not every paragraph uses every step, but a paragraph that uses none is a fact sheet.

**Idea** (what we believe here, in a sentence that is not a fact) → **opponent** (who'd disagree, in their words) →
**the build** (one long sentence that lays out the mechanism) → **the turn** (a short sentence that lands it) →
**one number, felt** → **end on a decision, a number, or the alternative we refused.**

## 3. Ten laws, each with its test
| # | Law | Test before it leaves the room |
|---|---|---|
| 1 | **Find the idea before the sentence.** Long sentences and idea-words arrive together (E10). Facts with no idea above them are what Ray called plastic. | Can I say this paragraph's idea without a number or a ticker? |
| 2 | **Give every paragraph an opponent**, voiced fairly, ideally in their own short sentences. | Who disagrees with this paragraph, and did they get to speak? |
| 3 | **Build long, land short.** About one sentence in five at 30+ words, one in six under 7. Never every sentence at 12-25 (that is D4's 0.49 swing). | `fingerprint.py`: swing 0.6-0.75, long 15-25%, short 15-20% |
| 4 | **One number per paragraph, and make it felt.** Shrink it to a human scale ("a little under half of one cheque"), react to it ("Snug."), or make it a choice (Buffett's two piles). Round it. Numerals. | Under 1.5 numerals per 100 words; which number would a judge repeat? |
| 5 | **Mechanism before label.** The toy explanation first. A jargon word only after it, or never ("CLO coverage test" becomes "the people who package loans into bonds pay the senior investors first"). | Would a smart 14-year-old follow it? |
| 6 | **One image per piece, which argues.** Delete it and part of the argument goes. Introduce once, call back once. In the IPS the image is Caplet XR; nothing competes with it. | If I delete the image, does the logic break? If not, delete it. |
| 7 | **One real confession or limit per piece.** A real mistake (the STRIPS plan, the 75%-stocks plan), a real risk with its size, or "we can't tell you X; we can tell you Y". Never invented, never two. | Is there a moment where we admit something? Is it true and dated? |
| 8 | **Strong words stay strong** (BIBLE rule 6). A word is wrong only if it is false; then replace it with an equally strong true claim. | Did anyone soften a true sentence? Undo it. |
| 9 | **Spend kickers like money.** At most 3 in the IPS, 1 per Final Report section. Every other paragraph ends on a number, a decision or the alternative refused. | Count the quotable endings. More than 3 in 500 words is a stand-up set. |
| 10 | **Ration symmetry.** One "X, not Y" or "A is B. C is D." per 400 words, and make it a real chiasmus. Parallel pairs are where AI hides when it has no argument (E07: 8 of 12 died). | `fingerprint.py`: "X-not-Y" under 3 per 1,000 |

## 4. Register by deliverable
| Deliverable | Mix | Notes |
|---|---|---|
| **Pitch (50 words)** | Spine + one image | One turn, one image (Caplet XR), no list. |
| **IPS (500 words)** | Spine and hands, Ahaan's mouth at about a third | Open with a claim that sounds wrong (A1) or the view in sentence one (A6). One opponent voiced. One limit admitted plainly. No more than six numbers in the whole form. Three kickers. Concepts named and explained in one breath, owners left for the Final Report (north star 4). |
| **Final Report** | All of it | Pun headings (Cembalest's "Smothering Heights", Ahaan's "Laissez-faire, or laissez-unfair?"); concept owners cited (Marks, Dimson, Housel, Mauboussin, Buffett); the real confessions (E02, E05); the package-insert structure if adopted (`07_ideas_from_reading.md`, I-2). |
| **Co-sponsor text (Final Report)** | Buffett plainness | Short sentences, no jokes about money that isn't ours, every number with its date. |
| **Keel memos and lab notes** | Hands | The first paragraph is written for a judge (E08); stamps and seeds go below it. |

## 5. The plastic test (read it aloud, then answer)
1. What is this piece's idea, in one sentence that is not a fact?
2. Who disagrees, and did we let them speak?
3. Is there one sentence over 30 words that builds, and a short one it earns?
4. Which single number would a judge remember, and why that one?
5. Is there a sentence only Caplet could have written? (Cover the team name: could any other team have said it?)
6. Where did we spend a kicker, and was it worth it?
Then run `fingerprint.py` against Ahaan's essays. One "no", or two metrics outside the band, sends it back. **None of
these is a reason to soften a true claim.**

## 6. What changed from `VOICE.md` and R03 (and why)
| Old rule | Now | Why |
|---|---|---|
| "Four sentences a paragraph, about 18-32 words each" (VOICE base, move 6) | Build long, land short; the band in law 3 | That rule produced D4's flat 0.49 swing. Ahaan's paragraphs range from one line to twelve sentences. |
| "Never: rhetorical questions" | Allowed once a piece, answered at once | Ahaan, Marks ("What's the downside?") and Graham all use them. |
| "Abstract nouns doing the work" is an AI habit (R03 table) | Name the idea, then show the concrete thing | Keel took it too far: its drafts have a quarter of Ahaan's idea-words. Vague abstraction is the problem, not ideas. |
| "Numbers: few" | One per paragraph, felt, under 1.5 per 100 words | "Few" was never measured; drafts ran at 3 per 100. |
| Ban-list first (AI tells table) | Ban-list last, after the six questions | Ahaan, 24 Oct: AI-ness "transcends ... a neat list". |
| The essays called "Ray's" (R03, VOICE, BIBLE notes) | **Ahaan's** | Corrected 27 Oct (`01_digest_ahaan.md`, section 1). |
