# D32 (V52): Ten Commandments check + Book 11 check, Mon 2 Nov 2026

AI-generated (Claude Code), not for submission. A cold check by a reader who did not write V52.
**GPTZero: not yet checked.** I'm not a detector, and nothing below is an AI-likeness score.

**What was checked.** `ips_V52.txt` as it stands after the coordinator's post-cold-read edit (file time 21:25 UTC, md5
`dc36bad1…`): **496 strict** (496 by spaces and split on hyphens), one under the house cap of 497. `pitch.txt`:
**50**. All counts come from `keel/office/tools/textcheck.py`, quoting the larger number. I checked against
`WHARTON_WORD.md`, `BIBLE.md` (Books 1-5, 9, 10, 11 and the commandments), the case, `voice/06_voice_guide.md`,
`IDEA_LEDGER.md`, `THINKING_LOG.md` and `INSTRUCTIONS.md` I72-I79. Corroboration only, never the marking scheme:
- `COLD_READ.md` was written on an earlier text.
- `COLD_READ_final.md` was written on the text one edit before this one. It found CLEAR 2 · PAUSED 8 · LOST 1 (P8), and
  that P5's "no cheque and no floor depends on it" contradicted the set-aside in P8. Both were then changed.
- `judges/panel_V52/SUMMARY.md` covers four judges, on a V52 that predates both cold reads.
- `judges/pitch_V51/SUMMARY.md` covers the pitch.

**Nothing has read this exact text cold except me.** So P8's rewrite, the main change, hasn't been checked by a second
reader.

**Tally. Commandments: PASS 4 (II, V, VII, X) · FAIL 4 (I, III, IV, VIII) · OPEN 2 (VI, IX).
Book 11: PASS 6 (1, 2, 3, 4, 5, 8) · FAIL 0 · OPEN 3 (6, 7, 9).** By the Bible's rule ("A draft with a failed line
does not go to Caplet"), V52 isn't cleared yet. Of the four failures, VIII takes ten minutes and IV needs one re-read
plus the fixes below. I and III are the standing ones.

**The two questions asked.**
- **The 7.5% assumption sits within Book 11 and Book 9.** It reads: "We assume world shares earn about 7.5% a year over
  the long run, but the cheques never depend on it."
  - It is an input, labelled as ours ("We assume"), not a model's output. The words "model", "paths" and "times in 100"
    appear nowhere.
  - It comes with the context Book 11 said was missing, namely what rests on it: not the cheques. Wharton asks for
    "reasoning, assumptions, and tradeoffs", and the case asks teams to "use reasonable return assumptions".
  - Book 9's complaint was that 7.5% "technically doesn't apply to VT; it applies to world equities in general". V52
    applies it to "world shares", not to VT, which is exactly that correction.
  - The source in the repo is J.P. Morgan's 2027 LTCMA, global equities, 7.5% in USD (Window, 27 Oct, in
    `research/R04_fact_checks.md`). The verified 2026 edition in `competition/official_market_data/` says 7.00%
    compound for AC World. So the Final Report must cite the 2027 edition and say whether the figure is compound or
    arithmetic. The IPS needs no change.
  - "About a fifteenth of her money" is an allocation (portfolio construction, which Wharton asks for), not a model
    result. Three judges asked for it. It is also true to the design, because the sleeve is sized to the floor's
    interest.
  - **The clause is accurate now.** "But the cheques never depend on it" holds: a reinvestment gap is set aside before
    naming, and what the stocks can't cover lowers the range, never a cheque. The earlier "no cheque and no floor" was
    false and has been cut.
- **"Do not crush" passes Book 11, judged on its own words.** Book 11 says the power was the label "stated in the
  introduction" and "that phrase again in the conclusion". V52 does exactly that:
  - P2 sets it up: "a capsule that delivers its dose on schedule, labelled do not crush. Break it open and you ruin how
    it works."
  - The last line repeats it: "Do not crush."
  - The explainer V51 had ("Crushing a capsule here means selling a bond before its January") was never what Book 11
    asked for.
  - The cost falls under IV, not Book 11. Both V52 cold reads paused on the close: "the IPS never says what crushing
    would be in portfolio terms". Fix 3 bridges that in three words without explaining the joke.

**The pitch** ("Laura's ten $50,000 cheques are a promise, so we don't invest for them. We buy them. ...") is the
pitch panel's first choice, at a mean of 1.33 across three judges ("a real student is audibly talking"). It meets
Wharton's brief: the central idea, then what each deposit buys. Two flaws remain. "Floor" is used unexplained (both cold
readers). And "we don't invest for them. We buy them." is said again almost word for word in IPS P3, so the two fields
repeat each other. Both are left as they are: there are no spare words, and the panel prefers this pitch.

## The Ten Commandments

| # | Commandment | Verdict | Evidence from V52 |
|---|---|---|---|
| I | Be extraordinary, by our own light | **FAIL** | The same two uncommon ideas as V51: "Laura's career already behaves a lot like a stock", and the stock sleeve as the interest "a bank would spend ... on an option". They sit on the field's skeleton (a ladder plus stocks plus a lock). Panel V52, four judges: V52 **3.75, fourth of six**, behind A09 2.00, S01 2.25 and H19 3.00, though above V51 for three of the four. No "every team" line |
| II | Wharton's word is the only marking scheme | **PASS** | The assumption was added because Wharton asks for "reasoning, assumptions, and tradeoffs" and four judges marked V51 down on exactly that. The panel prompts give WHARTON_WORD as the only scheme. All five IPS questions are answered: central idea ("We buy them."), principles ("The order never changes: the cheques, then the floor, then the gift."), balance (P5-P6), change over time (2027 → 2028 → 2031 → 2033) and protection plus flexibility ("The other half stays with Laura, liquid any day") |
| III | Write like us, never like a machine | **FAIL** | The test (a README quoting the moves) can't pass: D32 has no README. The moves are there: a concession then "But" (P7); a build that lands (P4: "– income that dries up ..." → "If that deposit arrives smaller, the gift shrinks."); a wry line ("worth nothing if the market stands still"). The slogan "not a probability, but a purchase" is gone, which is a fix. Against: the triad "the cheques, then the floor, then the gift", which both V52 cold readers flagged; the mirrored "We don't invest toward these payments. We buy them."; P7's polished aphorism; and the even cadence the final cold reader noticed (short lines, then a long one, paragraph after paragraph) |
| IV | Clear on one reading | **FAIL** | The final cold read (one edit back) found CLEAR 2 · PAUSED 8 · LOST 1. P8, the LOST paragraph, was rewritten afterwards. It now says why reinvestment matters ("The ladder costs less than the cheques because its bonds pay interest along the way, to be reinvested") and how the gap is sized ("we price that gap at the day's yields"), which answers both of the reader's questions. But it hasn't been re-read, and "If yields fall and stay low, it earns less" leaves "it" unclear (the ladder, or the interest?). Pauses that remain on the current text: P4 never draws its conclusion (both cold readers: the bond-price clause "does not reach its conclusion"); the close (what is "crush" in portfolio terms?); "funds that mature like bonds"; P5's density, with seven sentences in one paragraph; "the floor, then the gift", when the floor is the bottom of the gift |
| V | Every number explains itself (read by Book 11: no model numbers) | **PASS** | Case sums and dates ($50,000, $300,000, ten; 2027, 2028, 2031, 2033) and a plan date (late 2032). "About a fifteenth of her money" follows from the sentence before ("roughly the interest those Treasuries are expected to earn"). "About 7.5% a year" says who ("We assume"), for what ("world shares ... over the long run") and what rests on it ("the cheques never depend on it"). No model output, no "we judge" |
| VI | GPTZero before Caplet | **OPEN: not yet checked** | No score for the IPS or the pitch. VERSIONS row 52 carries the label. No agent stood in for a detector |
| VII | Few ideas, at full size | **PASS** | It can be told in three sentences (the cold reader's paraphrases do so). One caution: P5 now carries the top-up, the floor, the fund, its size, the note and the assumption, and both cold readers called it dense |
| VIII | Lose no idea; critique every borrowed one | **FAIL, narrowly** | The ledger has caught up for Book 11's cuts ("What Book 11 took out of the IPS (V49 to V50)") and for V51-V52. But its V52 line describes the text before the final edit. It lists as IN "That is about a fifteenth of her money, small on purpose: no cheque and no floor depends on it", which is now cut. It also doesn't place two ideas that have since gone: "small on purpose" (the reason the slice is small) and "or she needs flexibility", which leaves the IPS with no "flexibility" at all. The critique half: the bank's version is critiqued, but what our version costs us is never said |
| IX | Judges who actually disagree | **OPEN** | Panel V52 is blind and its judges disagree (J2 put V52 last, J4 second). But it was four judges picked because they had marked V51 down, on a V52 that predates both cold reads, and it reports no rank correlations. That is a targeted test of one fix, not the panel the commandment describes. The final text hasn't been panelled |
| X | Improve without being asked | **PASS** | THINKING_LOG "Mon 2 Nov, morning" predicts Caplet's line ("Rivals still beat you. Why?") and names the fixes (one assumption; the slice's size). V52 carries both, plus the cold-read repairs to P8 and P5 |

## Book 11, point by point

| # | Book 11 point | Verdict | Evidence from V52 |
|---|---|---|---|
| 1 | No opening rhetorical question | **PASS** | "In January 2033, Laura's portfolio writes the first of ten cheques"; no "?" |
| 2 | No "our model" or model outputs | **PASS** | No "model", probability or projection. The 7.5% is a labelled assumption and the fifteenth is an allocation (see above) |
| 3 | No team history or past plans | **PASS** | None. P7 is a refused alternative, not a history |
| 4 | Full-circle XR; "do not crush" set up and paid off | **PASS** | P2: "labelled do not crush. Break it open and you ruin how it works." Close: "Do not crush." That is the intro's label used again at the end, which is the power Book 11 names. Its clarity is judged at IV |
| 5 | No subheadings | **PASS** | Continuous prose |
| 6 | Every sentence makes plain sense | **OPEN** | The LOST paragraph has been rewritten and now explains itself, but no second reader has read it. "It earns less" needs a noun (fix 2) |
| 7 | Sound human, not AI | **OPEN** | GPTZero not yet checked. By ear: row III |
| 8 | Follow Wharton's guidelines | **PASS** | Strategy and framework, now with the one assumption Wharton's "reasoning, assumptions, and tradeoffs" asks for. No final range, projections or calculations. A watch point: "flexibility", Wharton's own word in the fifth question, no longer appears; the idea survives in "liquid any day, in case the building costs more in Taiwan dollars" |
| 9 | Absolute overdrive; pay attention to the Bible | **OPEN** | The volume is real: two cold reads, two panels, a ledger catch-up and a log entry within hours. But D32 has no README, and the final text has no cold read or panel |

## Top fixes (exact; measured with textcheck; the package takes the IPS from 496 to **497 strict**)

Each delta was measured by applying that fix alone to V52 as it stands. The package was applied together to a scratch
copy and measured at 497. That copy proves the count only. No fix contains a model number. The three small additions
are paid for by **cutting one whole idea**, not by squeezing a sentence.

1. **Top fix: make P4 reach its conclusion (IV; Book 9's "causal chains ... to their logical conclusion"). +2.**
   Old: "income that dries up in exactly the kind of downturn that pushes bond prices up."
   New: "income that dries up in exactly the kind of downturn that makes a ladder dearer to buy."
   Both cold readers said the bond-price clause argues for bonds as a hedge, not for buying the ladder in 2027. This
   names the double hit: if the ladder waited for the 2028 deposit, a downturn would shrink the money just as it raised
   the price. That makes P4, the panel's best-liked client reading, prove the plan's order.
2. **Give P8's pronoun a noun (IV; Book 11 point 6). +1.**
   Old: "If yields fall and stay low, it earns less, and the ladder falls short."
   New: "If yields fall and stay low, that interest earns less, and the ladder falls short."
3. **Let the close land on a rule a reader can name (IV; Creativity and Presentation). +3.**
   Old: "paying out one bond at a time as each cheque is written."
   New: "paying out one bond at a time as each cheque is written, never sold early."
   It doesn't explain the joke. It puts the one act that would "crush" the plan two lines before "Do not crush.", which
   is where both cold readers looked for it.
4. **The payer: cut the opening's duplicate of the priority rule. −5.**
   Old: "She also hopes to contribute to the building. But the cheques come first."
   New: "She also hopes to contribute to the building."
   The same idea closes the IPS ("The order never changes: the cheques, then the floor, then the gift."), and the pitch
   opens on it. Three V51 judges named that closing line as where the principles are visible, so the closing line is
   the one kept. The cost is one concession-then-"But" move at the opening. P7 keeps the other.

Package: +2 +1 +3 −5 = **+1 → IPS 497 strict; pitch 50 unchanged.**
**An equal-cost swap if the team prefers Wharton's word to the motif:** put back "flexibility" instead of fix 3
(+3, also measured). Old: "in case the building costs more in Taiwan dollars." New: "as her flexibility, in case the
building costs more in Taiwan dollars."

**Process, at no word cost:**
- A D32 README carrying this check and "AI DRAFT (Claude); GPTZero: not yet checked".
- Update the ledger's V52 line to the final text: "small on purpose" and "or she needs flexibility" out, with where
  each lands.
- One cold read of P8 as rewritten.
- A full six-judge panel on the final text, with rank correlations.
