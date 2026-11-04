# D37 (V57): cold read, Ten Commandments, Book 11 and I80 check

AI-generated (Claude Code, cold reader), Wed 4 Nov 2026. Draft V57.
Not for submission. GPTZero: not yet checked. I'm a reader who did not write V57, not a detector, and nothing below is an AI-likeness score.

**Tally. Commandments: PASS 3 (III, V, VII) · FAIL 1 (IV) · OPEN 6 (I, II, VI, VIII, IX, X). Book 11: PASS 5 · FAIL 1 (6) ·
OPEN 3 (7, 8, 9). I80 habits: PASS 7 · FAIL 1 (aphorism openers) · OPEN 1 (no wind-up to a punchline).** Two FAILs share one
cause (IV and 11.6, plain sense) and one is a habit V56 had already fixed and V57 brought back. All three cost few or no
words to fix (see "Fixes" at the end).

**What was checked.** `ips_V57.txt` (md5 `7d73eed5…`): **495 strict** (492 by spaces). `pitch.txt` (md5 `337ab932…`, the
same file as V56's): **48**. Both counted with `office/tools/textcheck.py`. The house cap is 497, so V57 has 2 words spare.
**Reading set, by instruction, and nothing else:** the draft, the case (`Laura_Gao_2026_Client_Profile.txt`), BIBLE (the Ten
Commandments and Book 11), the D36 check (template, and my only source for V56's wording) and the D35 README (I80 list). I didn't
open WHARTON_WORD, IDEA_LEDGER, THINKING_LOG or the panels, so every row that depends on them is OPEN because it's out of
scope here. That doesn't mean the row failed.

## A. Cold read

**Said back after one reading, one sentence each.**
- **(a) The ten payments.** Laura's first $300,000 buys ten Treasury holdings (bonds and Treasury funds with fixed end
  dates), one maturing before each January from 2033 and held to the end, so no payment depends on shares.
- **(b) The 2028 deposit.** It first tops up the ladder if the ladder is short. Most of the rest buys a Treasury fund
  maturing in late 2032, which is the floor of the building gift. What's left, about the interest that floor will earn,
  goes into one world index fund.
- **(c) The 2031 range.** The bottom is the floor, rounded down. The top is the floor plus half her shares, and those shares
  are sold into Treasuries before she names the range. The other half stays hers as a cushion.
- **(d) If rates fall.** The ladder's reinvested interest can come up short. Before she names the range, the gap is priced
  as if no more interest is reinvested, and that much moves from her kept shares into Treasuries. If her kept shares can't
  cover it, the range she names is lower.

**LOST: phrases I didn't understand on first read.**
1. P7 "we price that shortfall **as if nothing more were reinvested**". I had to stop and work out that it means "as if every
   coupon from that day on earned nothing". On first read I took it as "stop reinvesting", which would be a change of plan.
2. P3 "matching their bonds' **average life** to the payments and **rebalancing as rates move**". I could guess the meaning
   because I know the field, but the case's "smart adult" wouldn't. "Average life" is also the wrong term (see wrong claim 1).
3. P5 "they spend the interest on **an option** that can expire worthless". "Option" is never explained. A reader who has
   never met a call option can't see what was bought or why it can be worthless, and that sentence carries the whole
   comparison with banks.

**Pauses, understood on a second look.**
- P5 "the floor of **her gift**": "gift" first appears here. P1 says "help build the facility" and P2 says "the building", so
  the reader has to work out that the gift is the facility contribution.
- P6 "half her shares, which **move into Treasuries**": shares don't move. They're sold and the money buys Treasuries.
- P6/P7 "Her **spare money**", "her **kept shares**", "the other half": three names for one pot in about 60 words.
- P7 "the whole range **comes down**": this can be read as cutting a range she already announced. It means the range she
  names is lower (D36 flagged this too).
- P8 "the ladder and **the money set aside**": the reader has to connect this back to P7's shortfall money.
- Pitch "Treasuries that **mature one before each January**": the word order still makes you stop (D36 flagged it).
- Logic a careful judge may raise: P3 says "pays exactly what it promised" and "never needs rebalancing", but P7 says "counts
  on reinvesting its bonds' interest" and "can fall short". All of these are true, but the draft never joins them up.
- Logic, range: the top half moves into Treasuries before she names the range, so both ends are in Treasuries when she
  speaks. The range then mostly covers the floor fund's payout ("rounded down"). The draft never says how confident Laura
  should be that the gift lands inside it, and the case asks teams to "state how confident they are" (p.3).

**Factual claims about investing history or practice that I think are wrong or contested.**
1. **Wrong term: "matching their bonds' average life to the payments" (P3).** Immunisation matches **duration**: the
   present-value-weighted average timing of *all* cash flows, which sets how much a value moves with rates. "Average life"
   (weighted average life) is a different measure. It counts only principal repayments and is used for amortising bonds and
   MBS. A judge who knows fixed income will spot it. Zero-word fix: "average timing" (see Fixes). The either/or is also
   simplified, since real pension LDI mixes the two (cash-flow matching for near payments, duration matching further out)
   and often uses swaps. That's fine at IPS length.
2. **Overclaim: "A Treasury held to maturity pays exactly what it promised" (P3).** This is true of a Treasury bond or note.
   It isn't true of the "Treasury funds with fixed end dates" in the same ladder. A defined-maturity ETF promises no payout,
   and its final distribution depends on its holdings, reinvested coupons and fees. Dropping "exactly" softens it. Fix 2
   below does that.
3. **Tension: "We do the second, which never needs rebalancing" (P3) vs "it counts on reinvesting its bonds' interest" (P7).**
   A pure dedicated portfolio sizes each bond's principal net of the coupons it receives, so it never reinvests. This
   ladder's coupons arrive in 2027-32, before the first payment, and have to be reinvested, which is exactly the P7 weakness.
   The claim isn't false, but it reads as though the method is hands-off.
4. **Contested, defensible: "portfolio insurance ... helped deepen the 1987 crash" (P5).** This is the Brady Commission's
   (1988) view. Others dispute how much, for example Roll (1988), who noted the crash hit markets with little portfolio
   insurance. "Helped deepen" is a fair, mainstream wording. Don't strengthen it.
5. **Contested, defensible: "time makes a loss rarer, not smaller" (P4).** This is the Samuelson (1963) and Bodie (1995) line:
   the chance of loss falls with time, but the worst cumulative loss, and the cost of insuring against it, grows. Siegel's
   *Stocks for the Long Run* argues the other side. "Shares are called safe" hands that view to an unnamed "they", which is
   fine.
6. **Fair but incomplete: the capital-protected note (P5).** Zero-coupon bond plus call option is the right description. It
   leaves out the two costs that favour Laura's version most: the bank's fees and the **bank's own credit risk**
   (principal-protected notes issued by Lehman lost holders money in 2008). Nothing in it is wrong.
7. **Case wording: "to run her Taiwan residency" (P1).** The case says "toward the residency's operating expenses" (p.3) and
   allows outside money for "any operating support beyond Laura's commitment". "Run" slightly overstates it. Minor.
8. **Unsourced but plausible:** "book advances, speaking fees and licensing ... tend to dry up in the same downturns" (case
   p.2 says "publishing advances"). "XR tablets ... come labelled 'do not crush'" is accurate for extended-release products.

## B. The Ten Commandments

| # | Verdict | Reason (V57's own words) |
|---|---|---|
| I | **OPEN** | Retellable ideas: income tied to markets ("tend to dry up in the same downturns that hit share prices ... shouldn't bet on shares a second time"); the note without the option ("We would rather she owned the shares."); never crush ("selling it before it matures, even for the building"); new in V57: "rarer, not smaller" and the 1987 contrast. No "every team". Whether a judge sits up can't be shown without a panel |
| II | **OPEN** | Read against the case only (WHARTON_WORD is outside my reading set). Strengths: central idea, growth ("one world index fund holding thousands of companies"), liquidity ("stays hers and liquid"), flexibility and facility inflation ("costs more in Taiwan dollars"), dates 2027-2042. Gaps against the case's own asks: (1) V56's explicit definition of high certainty ("That is what we mean by ...") is gone, and the case says teams must "define what they consider a high degree of funding certainty" (p.3); (2) V56's performance assumption ("We assume about 7.5%") is gone, and the case asks for "assumptions about investment performance" (p.4); (3) no confidence for the range (p.3); (4) how the reserve's mix changes after 2033 is only implied ("paying one cheque each January") |
| III | **PASS** | Concession then "but", twice ("Shares are called safe ..., but"; "Banks sell this ..., but"). A short line that lands ("We would rather she owned the shares."). A wry line ("can't quietly be halved after a bad year"). Contractions (can't ×3, shouldn't) and British spelling ("labelled", "cheque"). Against it: three colon reveals (": X for ten", ": the floor of her gift", ": money she already owns") and no en dashes |
| IV | **FAIL** | Three LOST phrases on one reading (A, LOST 1-3), two of them in V57's new material. All three fix cheaply |
| V | **PASS** | Every figure is from the case ($50,000, ten, $300,000, 2027/2028/2031/2033/2042), a date of history (1987), or an allocation whose reason sits beside it ("half" with "the other half stays hers ... as a cushion"; "roughly the interest that floor will earn"). No model output, no "we judge", no bare multiplier. "Thousands of companies" is checkable |
| VI | **OPEN: not yet checked** | No GPTZero score for the IPS or the pitch. No agent stood in for a detector |
| VII | **PASS, narrowly** | It fits in three sentences: (1) 2027 money buys one Treasury holding per cheque, none sold early; (2) 2028 money buys a floor, and only about its interest goes into world shares; (3) in 2031 half the shares move to Treasuries to fix the top, and the reinvestment gap is covered first. Strain: P3-P5 now carry four borrowed ideas (pension matching, time and risk, the bank note, portfolio insurance) at about one sentence each, which edges towards "every mechanism briefly" |
| VIII | **OPEN** | IDEA_LEDGER is outside my reading set. Against V56 (as quoted in D36), V57 **drops**: the 7.5% assumption with "no payment relies on it"; "less than a tenth of her $450,000"; "one bad year could hurt her twice"; "a smaller deposit shrinks the building gift, but every payment is already paid for"; "That is what we mean by ..." (the certainty definition). It **adds**: pension cash-flow vs duration matching, time diversification, portfolio insurance and 1987. Critique of what it borrowed: the bank note and portfolio insurance are critiqued; duration matching is rejected with a reason; the cost of the method it chose (reinvestment) is in P7 but never linked back; time diversification is used, not critiqued |
| IX | **OPEN** | No panel file in my reading set |
| X | **OPEN** | THINKING_LOG is outside my reading set |

## Book 11

| # | Verdict | Reason |
|---|---|---|
| 1 No opening rhetorical question | **PASS** | It opens "From 2033, Laura's portfolio must pay $50,000 each January". There's no "?" anywhere |
| 2 No "our model" | **PASS** | No model, probability or projection. "We price that shortfall" describes a rule, not an output |
| 3 No team history | **PASS** | None. The bank note, duration matching and portfolio insurance are alternatives turned down, not past plans of ours |
| 4 Full-circle XR | **PASS** | Set up in P2 ("come labelled 'do not crush'"; "Crushing one means selling it before it matures, even for the building"), paid off in the last line ("works as long as nobody crushes it"). R = redemption, as the standing rule requires |
| 5 No subheadings | **PASS** | Continuous prose |
| 6 Plain sense | **FAIL** | Same as IV |
| 7 Sound human | **OPEN** | GPTZero not yet checked. By ear, see III and the last two I80 rows |
| 8 Wharton's guidelines | **OPEN** | Strategy, not sums. But see II: the certainty definition, the performance assumption and the range confidence are missing against the case |
| 9 Overdrive | **OPEN** | This cold check exists. I can't see anything else in my reading set |

## I80 habit list (D35 README)

| Habit | Verdict | Evidence |
|---|---|---|
| Slogan flips | **PASS, narrowly** | No two-sentence flips. Two "X, not Y" antitheses ("rarer, not smaller"; "only on fixed dates, never on a market move"), and the second ends P5. Watch it |
| Two-word kickers | **PASS** | Every paragraph ends on a full clause. The shortest closing line is "so her portfolio shouldn't bet on shares a second time" |
| "That is X." staccato | **PASS** | None |
| Announcing instead of saying | **PASS** | "The ladder's one weakness is that it counts on reinvesting ..." states the weakness and its cause in one sentence |
| Stilted asides | **PASS** | None |
| Aphorism openers | **FAIL** | "Laura's earning power already behaves like a share." is D35's own example ("Laura's career already behaves like a stock.") with two words swapped. V56 had replaced it with D35's fix, and V57 brings it back |
| Metaphor explained twice | **PASS** | One sentence for the tablet, one for X and R, one for what crushing means (Book 11.4 needs that third one) |
| One-line final paragraph | **PASS** | Two full sentences |
| Rule underneath: no wind-up to a punchline | **OPEN** | The last sentence is still a moral bow ("Like the tablet it is named after, the plan works as long as nobody crushes it"), the line D36 flagged. P5's "We would rather she owned the shares." lands well and isn't a wind-up |

## Investing concepts used (Caplet, 4 Nov: "look erudite")

| Concept (where) | Applies to Laura? | Relevance explained? |
|---|---|---|
| Cash-flow matching (dedication) vs duration matching (immunisation), as pension funds use (P3) | **Yes.** Ten fixed nominal payments are a pension-style liability | **Partly.** "We do the second, which never needs rebalancing" says which method, not why it suits *her*. The term "average life" is wrong (should be duration or "average timing"), and the method's cost (reinvestment) is in P7 but never linked back |
| Holding to maturity / Treasury credit (P3) | **Yes**, it's the core of the plan | **Yes** ("whatever markets do"). It overclaims for the funds ("exactly") |
| Defined-maturity Treasury funds ("Treasury funds with fixed end dates", P3) | **Yes**, they're in the ladder | **Named, not critiqued.** The payout isn't fixed |
| Time diversification and its critique (Samuelson, Bodie), "rarer, not smaller" (P4) | **Yes.** Her cheques fall on fixed dates, so she can't wait out a loss | **Yes**: "a fixed cheque can't wait for a recovery". The best-fused concept in the draft |
| Human capital that moves with equities (P4) | **Yes**, through the 2028 deposit | **Yes**, through the source of the deposit. Its wording is the I80 FAIL |
| Capital-protected note = bond + call option (P5) | **Yes.** Her floor-plus-shares design is the same structure, without the option | **Yes**, but "option" is never explained (LOST 3), and it leaves out the bank's fees and credit risk, which are the strongest points for her |
| Portfolio insurance / dynamic hedging, 1987 (P5) | **Yes.** It's the obvious alternative for a floor plus upside | **Yes**: "Our plan changes only on fixed dates, never on a market move" |
| Pre-commitment and credibility (P6) | **Yes.** The case warns about over-promising (p.3) | **Yes**: "a number said aloud can't quietly be halved" |
| Reinvestment risk (P7) | **Yes** | **Yes**, and priced before the range is named |
| Global diversification ("thousands of companies", P5) | **Yes** | Stated, not argued (fine at this length) |
| Currency and facility inflation ("Taiwan dollars", P6) | **Yes** (case p.4 asks for it) | **Yes**, in a clause |
| Liquidity and flexibility ("stays hers and liquid", P6) | **Yes** (case p.3) | **Yes** |

## Fixes, most valuable first (tested on scratch copies with `textcheck.py`; the strict count is the larger one)

1. **Aphorism FAIL (I80), −8 words.** Delete `Laura's earning power already behaves like a share. ` (P4). The next sentence still
   carries the idea ("tend to dry up in the same downturns that hit share prices, so her portfolio shouldn't bet on shares a
   second time"). Result: 487.
2. **Certainty definition back (case p.3; II, 11.8), and the fund overclaim softened, +7 words.**
   `A Treasury held to maturity pays exactly what it promised, whatever markets do, so no payment depends on shares.` ->
   `A Treasury held to maturity pays what it promised, whatever markets do, so no payment depends on shares, which is what we mean by high certainty.`
   With 1 applied as well: **494**.
3. **Wrong term (claim 1), 0 words.** `matching their bonds' average life to the payments and` ->
   `matching their bonds' average timing to the payments' and`. With 1 and 2: 494.
4. **LOST 1 (IV, 11.6), +3 words.** `as if nothing more were reinvested` -> `as if its interest from then on earned nothing`.
   With 1-3: **497**, which is the cap.
5. Not costed, for the Final Report or a later cut: explain "option" in a few words (LOST 3); one name for the kept half;
   the bank's credit risk; the range's confidence; the closing bow.

## Applied after this check (Rewrite, Wed 4 Nov; the check above is of the text before these)
1. Aphorism FAIL fixed differently: the opener "Laura's earning power already behaves like a share." is gone; the idea
   now comes after the evidence, as a reason: "Her income already rides on shares, so her portfolio shouldn't bet on them
   twice." (keeps the human-capital idea, which is one of the I81 concepts).
2. Certainty definition back: "A Treasury held to maturity pays exactly what it promised, whatever markets do. So, to us,
   high certainty means no payment depends on shares." "Exactly" kept: it's said of a Treasury bond held to maturity, and
   Caplet asked on 26 Oct for no hedging there.
3. "average life" -> "average timing" (your 0-word fix).
4. LOST 1: "as if no more interest were reinvested" (+1; your "earned nothing" version would cost +3 and say the same).
   [Corrected later, Wed 4 Nov: they don't say the same. The funds end as cash that is principal, not interest. P7 now
   reads "as if every dollar waiting for a cheque earned nothing"; see `KEEL_RECORD.md` section 7.]
5. "paying one cheque each January" -> "paying each January's cheque" (-1, to make room).
Strict count after: 496 (pitch 48). Not taken: explaining "option" (no room; the Final Report explains it); "never needs
rebalancing" kept: rebalancing and reinvesting coupons are different things, and P7 names the coupon weakness.
