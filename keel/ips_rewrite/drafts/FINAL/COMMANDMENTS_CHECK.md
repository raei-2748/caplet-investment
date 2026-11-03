# D36 (V56): Ten Commandments, Book 11 and I80 check, Tue 3 Nov 2026 (Sydney)

AI-generated (Claude Code), not for submission. GPTZero: not yet checked.
A cold check by a reader who did not write V56. I'm not a detector, and nothing below is an AI-likeness score.

**Tally. Commandments: PASS 5 (II, III, IV, V, VII) · FAIL 2 (VIII, X) · OPEN 3 (I, VI, IX). Book 11: PASS 8 · OPEN 1 (7).
I80 habits: PASS 8 · OPEN 1 (the closing line).** Both FAILs are record-keeping and cost no IPS words. One text
problem under (b) isn't a FAIL row, but fix it before Caplet: the change to how the shortfall is priced, which nobody logged.

**What was checked.** `ips_V56.txt` (md5 `4ef646bc…`): **493 strict** (488 by spaces). `pitch.txt` (md5 `337ab932…`):
**48**. Both counted with `office/tools/textcheck.py`; the house cap is 497. Read against WHARTON_WORD, BIBLE (Books 1-5,
9-11, the Commandments), INSTRUCTIONS I80, the D35 habit list, the case, voice guide s9, GROUND_TRUTH s3, IDEA_LEDGER and
THINKING_LOG. I compared V56 with V55 line by line, and it differs in four places (see VIII).

## The Ten Commandments

| # | Verdict | Reason (V56's own words) |
|---|---|---|
| I | **OPEN** | Three ideas a judge could retell, and none is the field's default. The income link: "tend to dry up in the same downturns that hit share prices ... one bad year could hurt her twice". The bank note without the option: "they spend the interest on an option that can expire worthless. We would rather she owned the shares." Never sell early: "Crushing one means selling it before it matures, even for the building." No "every team". Whether a judge sits up is still unproven: `judges/panel_V56/` has no SUMMARY yet |
| II | **PASS** | The five questions are answered. Central idea: P3. Principles: "no payment depends on shares", "Her spare money shrinks first". The balance is all there: growth ("one world index fund"), liquidity ("shares she can sell any day"), reliability (P3), flexibility ("a cushion if the building costs more in Taiwan dollars"). Change over time: 2027, 2028, 2031, 2033, 2042. One assumption ("We assume about 7.5%") and one admitted cost ("one real weakness"). No range figures, no projections. Thin spot: how the reserve's mix changes after 2033 is only implied ("paying one cheque each January") |
| III | **PASS** | Builds, then lands short: "...an option that can expire worthless. We would rather she owned the shares." Concession, then "but": "a smaller deposit shrinks the building gift, but every payment is already paid for." Wry: "can't quietly be halved after a bad year". Contractions (three "can't"), "labelled", "cheque". No slogans, triads or fact-sheet runs. Against it: four colon reveals (P2, P3, P5, P6), the connector voice guide s9 says to stop |
| IV | **PASS, narrowly** | Nothing LOST on one read. "Ladder" and "floor" are explained when they first appear, and "rung" is never used. Pauses are listed under (a) |
| V | **PASS** | Case sums and dates. "$450,000" is the case's two deposits added up. "less than a tenth" is an allocation, and its reason sits in the same sentence ("roughly the interest that floor will earn"). "We assume about 7.5% ... but no payment relies on it" says who assumes it and what rests on it. No "we judge", no model output |
| VI | **OPEN: not yet checked** | No GPTZero score for the IPS or the pitch. No agent stood in for a detector |
| VII | **PASS** | It can be said in three sentences. (1) 2027's money buys one Treasury holding per cheque, none sold early. (2) 2028's money buys a floor, and only about its interest goes into world shares. (3) In 2031 half the shares move to Treasuries to fix the top, and the reinvestment gap is set aside first |
| VIII | **FAIL** | IDEA_LEDGER stops at V54. V55 and V56 have no entries, and V56 changed four things against V55: "at that day's rates, add a margin" became "as if nothing more were reinvested" (the ledger's V52 line says "priced 'at the day's yields'"); "shrinks before her promise does" became "Her spare money shrinks first"; "of her money" became "of her $450,000"; "Ours holds" became "Ours is". The first is a change of method, not of wording (see b) |
| IX | **OPEN** | `panel_V56/` exists (six blind prompts, a KEY, and some judges' scores on file) but has no SUMMARY or rank correlations yet |
| X | **FAIL** | THINKING_LOG's last "What Caplet would say" entry is "Tue 3 Nov, morning" (V53 to V54). The V55/V56 round after I80 has none |

## Book 11

| # | Verdict | Reason |
|---|---|---|
| 1 No opening rhetorical question | **PASS** | It opens "From 2033, Laura's portfolio must pay $50,000 each January". There's no "?" anywhere |
| 2 No "our model" | **PASS** | No model, probability or projection. "7.5%" is a stated assumption |
| 3 No team history | **PASS** | None. The bank note is an alternative turned down, not a past plan of ours |
| 4 Full-circle XR | **PASS** | Set up in P2 ("come labelled 'do not crush'"; "Crushing one means selling it before it matures"), paid off in the last line ("the plan works as long as nobody crushes it") |
| 5 No subheadings | **PASS** | Continuous prose |
| 6 Plain sense | **PASS, narrowly** | Same as IV |
| 7 Sound human | **OPEN** | GPTZero not yet checked. By ear: III, plus (d) |
| 8 Wharton's guidelines | **PASS** | Strategy and framework, no calculations. It covers liquidity, diversification ("thousands of companies"), flexibility, and inflation on facility costs ("Taiwan dollars") |
| 9 Overdrive | **PASS** | A six-judge blind panel is running on V56, and this cold check is separate from it. The ledger and log gaps are counted at VIII and X |

## I80 habit list (D35 README)

| Habit | Verdict | Evidence |
|---|---|---|
| Slogan flips | **PASS** | None in the IPS. The pitch's "are promises, so we pay for them up front" is D35's own replacement for the flip |
| Two-word kickers | **PASS** | Every paragraph ends on a full clause |
| "That is X." staccato | **PASS** | One "That is what we mean by ...", and D35 allows that form |
| Announcing instead of saying | **PASS** | Once ("The plan's one real weakness is reinvestment."), with the explanation in plain sentences, as D35 allows |
| Stilted asides | **PASS** | None |
| Aphorism openers | **PASS** | P4 opens "Her income is a second reason ...", D35's own fix |
| Metaphor explained twice | **PASS** | One sentence for the tablet, one for X and R, one for what crushing means (Book 11.4 needs that third one) |
| One-line final paragraph | **PASS** | The final paragraph has two full sentences |
| Rule underneath: no wind-up to a punchline | **OPEN** | The last sentence states a moral ("Like the tablet it is named after, the plan works as long as nobody crushes it"). Voice guide s9 asks for "an act rather than a lesson". See (d) |

## The four questions

**(a) Plain sense on one read.** Nothing LOST. These made me pause:
- P2 "Ours is ten Treasury holdings": "ours" (our tablet? our plan?) with a plural complement.
- P6 "which move into Treasuries before she names it, because a number said to co-sponsors can't ...": two clauses
  hang off "shares", and "said to" isn't idiomatic ("told to" or "given to").
- P7 "price the shortfall as if nothing more were reinvested": the reader has to work out that this means the
  coupons from then on earn nothing.
- P7 "the whole range comes down": the pricing happens before naming, so this means the range she names is lower. It
  can be misread as cutting a range she has already announced.
- Pitch "Treasuries that mature one before each January": the word order makes you stop.
- Logic a careful judge may raise: P4 "every payment is already paid for" sits beside P5 "completes the ladder, if
  needed" and P7 "the ladder can fall short". All three are true, but they're never joined up.

**(b) False against the case, the Trading Notes or a checkable fact?** Nothing is outright false. Fix three things:
1. **The shortfall method (P7).** "as if nothing more were reinvested" is the cash bound. In `lab/R08_4_coupons_results.json`
   (MODEL, 22 Oct curve), coupons held as cash from 2027 leave a median gap of $42,906. That gap exceeds the leftover
   plus Laura's half in 79.8% of paths. Pricing from 2031 would be smaller, but I haven't computed it (UNVERIFIED). Even so, the
   rule as written probably uses up "the shares she keeps" and lowers the range in most outcomes, which works against
   the cushion and flexibility story in P6. It also goes back on the ledger's "at the day's yields". Fix: go back to
   V55's "at that day's rates, add a margin," (+1). Or keep the new wording and log the method and its cost in IDEA_LEDGER.
2. **P2 "one redeemed each January".** No holding is redeemed in January. The iBonds close in December, and the T-bonds
   mature in Nov, Feb and May. Fix: "one redeemed for each January" (+1).
3. **P3 "each maturing just before one of the ten Januaries".** This isn't true of the WInS book. TNA note 1's Feb-2037 bond
   is the "latest WInS bond available beforehand", with its proceeds parked in a short-term Treasury ETF, about 11
   months early. The May-2038 bond is 8 months early. Fix: cut "just" (−1).

With all three applied (tested on a scratch copy), the IPS is **494 strict**. Soft spots I left alone: "to run her Taiwan residency" (the case
says "toward the residency's operating expenses", :88); "book advances" for "publishing advances" (fine); "about 7.5%"
(the Final Report must cite the JPM 2027 edition and say whether it's compound or arithmetic).

**(c) Does the opening set up "do not crush", and the ending pay it off?** Yes. P2 gives the label, and what it means
in portfolio terms ("selling it before it matures, even for the building"). P6 and P7 earn the payoff: the building's
cushion and the shortfall both come out of shares, never out of a holding. The last line brings the word back. The
setup sits in P2, not P1, and that's fine.

**(d) Anything that reads as AI or corny?**
- The refrain. P3, P4 and P5 each end on the same reassurance: "no payment depends on shares" / "every payment is already
  paid for" / "no payment relies on it". Three paragraph endings in a row with one shape is a pattern a reader hears
  coming. Optional: end P5 at "We assume about 7.5% a year from them." (−5).
- The closing simile is a tidy bow, and that's the mildly corny part. Optional, an act that repeats P2 word for word:
  replace the last sentence with "None of the ten is crushed, not even for the building." (−5).
- Four colon reveals (": X for ten", ": no payment depends", ": the floor of", ": money she already owns"). Turn one
  into a plain clause, e.g. P5 "..., which sets the floor of her building gift" (+1).
- What reads human: the bank-note pair, "hurt her twice", "can't quietly be halved", "in Taiwan dollars".

## Fixes, smallest first
1. VIII (0 IPS words): add a V55-V56 entry to IDEA_LEDGER, covering the four changes above and the reason for each.
2. X (0 words): add a THINKING_LOG entry for the I80 round. My guess at what Caplet says next: "Read the last line
   aloud. Is that us, or a greeting card?"
3. (b)1-3: net +1, so the IPS goes to 494 strict. Then rerun panel V56's summary before the draft goes to Caplet.
