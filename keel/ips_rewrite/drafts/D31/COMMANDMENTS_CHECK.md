# D31 (V51): Ten Commandments check + Book 11 check, Mon 2 Nov 2026

AI-generated (Claude Code), not for submission. A cold check by a reader who did not write V51.
**GPTZero: not yet checked.** I'm not a detector, and nothing below is an AI-likeness score.

**What was checked.** `ips_V51.txt`: **497 strict** (497 by spaces, 496 split on hyphens). The house cap is 497, so
there is no spare room. `pitch.txt`: **50** (49 by spaces, 50 split on hyphens). `pitch_a.txt`: **50**. All counts
come from `keel/office/tools/textcheck.py`, quoting the larger number. I checked against `WHARTON_WORD.md`, `BIBLE.md`
(Books 1-5, 9, 10, 11 and the commandments), the case, `voice/06_voice_guide.md`, `IDEA_LEDGER.md`, `THINKING_LOG.md`
and `INSTRUCTIONS.md` I60-I79. Corroboration only, never the marking scheme: the D31 cold read (`COLD_READ.md`), panel
V51 (`judges/panel_V51/`, still being written, with no SUMMARY yet; I worked out ranks from KEY.json and each judge's
ranking) and the pitch panel (`judges/pitch_V51/`).

**Tally. Commandments: PASS 4 (II, V, VII, X) · FAIL 4 (I, III, IV, VIII) · OPEN 2 (VI, IX).
Book 11: PASS 6 (1, 2, 3, 4, 5, 8) · FAIL 1 (6) · OPEN 2 (7, 9).** The Bible says "A draft with a failed line does not go
to Caplet". So V51 can't go to Caplet as it stands.

**Which pitch: `pitch_a.txt`.** It opens on Laura and her dates ("Laura has promised her residency $50,000 every January
from 2033 to 2042"), and its second sentence states the central idea ("Caplet XR buys those cheques outright in 2027").
That is Wharton's brief for the pitch: "the central idea behind your approach and how it is designed to support your
client's financial goals". `pitch.txt` spends its first 18 of 50 words on where the name comes from ("named after an
extended-release capsule, which delivers its dose on schedule and only works whole"). "Only works whole" means nothing
until the IPS's last line, and "its expected interest" could refer to either the deposit or the floor. That is the
squeeze Book 9 warned about. The pitch panel agrees: pitch_a ranked 5, 3, 2 and 7 of 8 (mean 4.25), and pitch.txt ranked
7, 7, 8 and 6 (mean 7.0). Both pitches share one flaw: "a Treasury floor for her building gift" uses "floor" before
anything has explained it.

## The Ten Commandments

| # | Commandment | Verdict | Evidence from V51 |
|---|---|---|---|
| I | Be extraordinary, by our own light | **FAIL** | The test: the three ideas a judge would retell, none of them the field's default. Two aren't the default. (1) "Laura's career already behaves a lot like a stock ... income that dries up in exactly the kind of downturn that makes bonds more expensive" (panel J5: "the sharpest reading of Laura's circumstances"). (2) The stock sleeve is the floor's expected interest, so it's "a capital-protected note, except a bank would spend that interest on an option" (J5: "a structured product rebuilt without the derivative"). The third idea, the one every reader retells, is "We don't invest toward these payments. We buy them." That's the field's skeleton (a ladder plus stocks plus a lock). Panel V51 puts V51 **third of six (mean rank 3.33)**, behind S01 (2.50) and A09 (3.17). J1 and J4 couldn't tell it apart from its siblings ("the same Caplet XR idea again"). No "every team" line (good) |
| II | Wharton's word is the only marking scheme | **PASS** | The panel prompts give WHARTON_WORD as "your ONLY marking scheme", and this check argues from the criteria (see the audit, rows W1-W49). V51 answers all five IPS questions: central idea ("We buy them."), principles ("the order will not: the cheques, then the floor, then the gift"), balance, change over time (2027 → 2028 → 2031 → 2033) and protection plus flexibility ("The other half stays with Laura, liquid any day") |
| III | Write like us, never like a machine | **FAIL** | The test is a README that quotes each move. D31 has no README. The moves are on the page: a concession and then "But" ("We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be quietly halved if markets turn."); a build ("Her 2028 deposit depends on publishing advances, speaking fees and licensing – income that dries up in exactly the kind of downturn that makes bonds more expensive.") that lands ("If that deposit arrives smaller, the gift shrinks."); a wry line ("worth nothing if the market just stands still"); contractions; "cheques"; en dashes. Against, by the commandment's own words ("No slogans, no triads"): a slogan ("not a probability, but a purchase"), a triad ("the cheques, then the floor, then the gift"), mirrored pairs ("To a pharmacist ... To us"; "We don't invest toward these payments. We buy them.") and a closing line on most paragraphs. Read beside Ahaan's tone, V51 is cleaner and more clipped than he is. Its longest sentence is 28 words, and there is none of his long, clause-on-clause argument that runs to its end before the short line lands |
| IV | Clear on one reading | **FAIL** | D31 cold read: CLEAR 2, PAUSED 8, LOST 1. The LOST sentence carries the main downside protection: "Before she names the range, that gap is set aside from the stocks Laura keeps; whatever they can't cover comes off the bottom." "That gap" has no antecedent, because no shortfall is ever stated. Also unclear on first read: "We call it Caplet XR." (what is "it"? the plan hasn't been named yet); "cash paid early earns less while it waits"; "funds that mature like bonds" (paused in both the V50 and V51 cold reads); "an option, which is worth nothing if the market just stands still" (the option's job is never said: cold reader, J1, J4, J6) |
| V | Every number explains itself (read by Book 11: no model numbers) | **PASS** | Every figure is the case's ("$50,000", "$300,000", "ten", 2027, 2028, 2031, 2033) or a plan date ("late 2032"), or a fact ("thousands of companies"). The text never says "model", has no probabilities and has no "we judge" |
| VI | GPTZero before Caplet | **OPEN: not yet checked** | No score exists for the IPS or the pitch. GPTZero can't be reached from Keel's sessions (`DETECTOR_LOG.md`). Until a student pastes both into gptzero.me, the label stays "not yet checked". No agent stood in for a detector |
| VII | Few ideas, at full size | **PASS** | It can be told in three sentences, and J3 did exactly that: "The $300,000 buys the ten payments outright ... Most of the deposit buys a Treasury floor maturing before 2033, roughly its expected interest goes into a diversified world fund, and in 2031 the promised top is moved into bonds before it is spoken." One idea is too small to carry its job: the reinvestment set-aside (see IV) |
| VIII | Lose no idea; critique every borrowed one | **FAIL** | The ledger test is still short. A "V51 and V52" block was added to `IDEA_LEDGER.md` while this check ran (uncommitted). It places V50's cuts in the Final Report: C8 time diversification, "a commitment rather than a forecast", "bought, not hoped for", "Ten capsules, ten Januaries". But there is no V49 or V50 line, so what Book 11 took out has no ledger row: 97 in 100; the strongest rival and its price; 7.5%; the first plan sunk by our model; the worst-twentieth pair; "ten one-year bills" (sequence risk); "a list of ways to fail". Neither does V50's "putting the floor into stocks would be the larger gamble". The critique test is only half met. The bank's note is critiqued ("worth nothing if the market just stands still"), but nothing says what our version gives up |
| IX | Judges who actually disagree | **OPEN** | Panel V51 exists, blind, six judges. V51 ranks 4, 4, 1, 5, 2, 4. S01 ranks 6, 1, 3, 1, 3, 1, which is real disagreement. But the test asks for a panel file that shows the rank correlations and each judge's reasons, and there's no SUMMARY yet |
| X | Improve without being asked | **PASS, narrowly** | The test is a "what they'd say" entry per round, with the next draft showing the fixes. When this check started, THINKING_LOG stopped at V48. While it ran, a "Mon 2 Nov, morning" entry was added (uncommitted) that reads panel V51 ("Rivals still beat you. Why?"), and V52 (`../D32/`) acts on it. The V49 and V50 rounds still have no entry. Taken from the rooms: the Archive's set-aside, "rounded down", "ten holdings" and "cash paid early"; the Courtroom's "Nobody else can pay them.", the option explained, "Laura's career already behaves a lot like a stock." and the new close. Not taken: the Courtroom's guess at Caplet's next line ("Did you read the marking guide?"), which asked for one plain sentence on diversification |

## Book 11, point by point

| # | Book 11 point | Verdict | Evidence from V51 |
|---|---|---|---|
| 1 | No opening rhetorical question | **PASS** | It opens: "In January 2033, Laura's portfolio writes the first of ten cheques". There's no "?" anywhere |
| 2 | No "our model" or model outputs | **PASS** | No "model", no probability, no projection. "Roughly the interest those Treasuries are expected to earn" describes how the sleeve is sized, not a model's output |
| 3 | No team history or past plans | **PASS** | None. "We could put the floor into stocks and chase a bigger gift" is a choice we refused, not a history |
| 4 | Full-circle XR, with "do not crush" set up and paid off | **PASS** | Set up in P2: "a capsule that delivers its dose on schedule, labelled do not crush. Break it open and you ruin how it works." Paid off in P9-P10: "Crushing a capsule here means selling a bond before its January, even for the building." / "Do not crush." J4 had to re-read the payoff, but it decodes |
| 5 | No subheadings | **PASS** | Continuous prose, ten paragraphs |
| 6 | Every sentence makes plain sense; no over-compression | **FAIL** | Paragraph 8 (LOST in the cold read; J1 "had to read twice"). Also "We call it", "cash paid early earns less while it waits", and the ellipsis "A cheque funded by a Treasury already bought does not." |
| 7 | Sound human, not AI | **OPEN** | GPTZero not yet checked. By ear: human moves are present (row III). Against: the cold reader's seven "machine" lines (the slogan, the mirrored pairs, the three-beat order line, the short reveal beats in P1, the tagline close). This is a reading, not a score |
| 8 | Follow Wharton's guidelines | **PASS** | Strategy and framework, not "individual investments or ... detailed financial calculations". All five questions answered. Thin spots (diversification argued only for the stocks; why Treasury funds sit beside bonds) are in the audit |
| 9 | Absolute overdrive; pay attention to the Bible | **OPEN** | The rooms' work is real: a Courtroom trial, the Archive's cross-read with a blind reader, a six-judge panel, a four-judge pitch panel, a cold read. The record caught up for V51 only while this check ran (ledger, log, VERSIONS row 51, uncommitted). V49-V50 are still unrecorded, and D31 has no README |

## Top fixes (exact; measured with textcheck; the package nets to 0, so the IPS stays at **497 strict**)

Each delta was measured by applying that fix alone to V51. The whole package was applied to a scratch copy and measured
at 497. The copy proves the count only: it hasn't had a cold read or a panel. No fix contains a model number. The two
additions are paid for by **cutting two whole ideas**, never by squeezing a sentence.

1. **Paragraph 8, the LOST paragraph (IV; Book 11 point 6). +20.**
   Old: "The weak point is reinvestment. If yields fall and stay low, cash paid early earns less while it waits. Before
   she names the range, that gap is set aside from the stocks Laura keeps; whatever they can't cover comes off the
   bottom."
   New: "The weak point is cash that arrives before it is needed, mostly the interest the bonds pay. If interest rates
   fall and stay low, that cash earns less while it waits, and the ladder falls short of the cheques. Before she names
   the range, that shortfall is set aside from the stocks Laura keeps; whatever they can't cover lowers the whole range."
   This gives the shortfall a referent and says what it is short of. "Lowers the whole range" is also truer than "comes
   off the bottom": the top is the floor plus half the stocks, so if the floor goes down the top must go down with it,
   or "every dollar she promises is already in bonds" stops being true.
2. **Cut the deletion test in P5 (the first of the two whole ideas that pay). −15.**
   Old: "That is her floor: money she will own outright even if every share in the world fell to zero."
   New: "That is her floor."
   The idea ("money she owns") is said again one paragraph later ("The bottom is her floor, rounded down: money she
   already owns."). And the vivid version pulls against paragraph 8: if every share fell to zero, Laura's stocks could
   cover none of the shortfall, so the range would come down. The line goes to the Final Report with the ledger's C5
   ("the shares can help a cheque, never hurt one"). The alternative payer is the order line "Whatever else changes, the
   order will not: the cheques, then the floor, then the gift." (−15). It's a triad, and it repeats P1's "But the
   cheques come first". But three panel judges (J3, J5, J6) named it as where the principles are visible, so it isn't
   recommended.
3. **The certainty slogan (III; Book 11 point 7), and the second whole idea that pays. −9.**
   Old: "That is what "a high degree of certainty" means to us – not a probability, but a purchase."
   New: "That, to us, is "a high degree of certainty"."
   The definition the case asks for (:97-98) stays: it's the sentence before ("A Treasury held to maturity pays exactly
   what it promises, whatever markets do in between"). The dropped idea, certainty as "not a probability", goes to the
   Final Report. There the probability is the test of this definition (Archive, 1 Nov, s4).
4. **"We call it Caplet XR." (IV: "it" has no antecedent). +1.**
   Old: "We call it Caplet XR." New: "We call our plan Caplet XR."
5. **Say what the option is (IV; II row W9; the cold reader, J1, J4 and J6 couldn't follow the comparison). +3.**
   Old: "on an option, which is worth nothing if the market just stands still."
   New: "on an option, a bet on the market rising, worth nothing if it just stands still."
   It keeps the wry ending. What our version gives up next to the bank's (Commandment VIII's "what it costs us") is
   still unsaid. It is first in line if words free up.
6. **Use `pitch_a.txt` as the pitch (Book 9; Wharton's pitch brief). 50 → 50.**
   Old: "Caplet XR is named after an extended-release capsule, which delivers its dose on schedule and only works whole.
   Laura's first $300,000 buys ten $50,000 cheques as Treasuries maturing before each January. Her 2028 deposit buys a
   Treasury floor for the building gift, and its expected interest buys world stocks."
   New: "Laura has promised her residency $50,000 every January from 2033 to 2042. Caplet XR buys those cheques outright
   in 2027, as ten Treasury holdings that each mature before a January. Her 2028 deposit buys a Treasury floor for her
   building gift, and the interest it should earn buys world stocks."

Package: +20 −15 −9 +1 +3 = **0 → IPS 497 strict; pitch 50.** Next in line, with no words left to pay for them:
diversification of the cheques argued in one sentence (the Courtroom's ask, Wharton's "uses appropriate
diversification"), at about +12 to +22, and why "half" her stocks (cold reads of V50 and V51; J5: "asserted, not
argued").

**Process, at no word cost (needed before any version goes to Caplet):** a D31 README carrying this check and the label
"AI DRAFT (Claude); GPTZero: not yet checked" (VERSIONS row 51 has the label now); IDEA_LEDGER lines for V49-V50 that
place every idea listed under VIII; commit the ledger, log and VERSIONS changes made while this check ran; and the
panel V51 SUMMARY with its rank correlations.
