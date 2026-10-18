# L08 verification: cross-deliverable coherence and number integrity

Checked Fri 16 Oct 2026 (Sydney). This is an AI check for planning only, not text to submit. I re-opened every cited file and line, or re-ran the numbers myself.

Verifier scripts are in `scratchpad/oct16/verify/L08w/`:
- `ladder.py` is an independent bootstrap of the official par curve. It prices the ladder four ways and the 2033 reserve.
- `build.py` writes the JSON file.
- `fomc.html` is the Fed calendar as fetched.

**Result:** 20 findings checked.
- 9 confirmed.
- 11 adjusted (5 of them have lower severity).
- 0 refuted outright, although parts of COH-06 and COH-08 were refuted inside the adjustment.
- 3 findings added.

The surviving set is in `verify/L08_coherence_numbers.final.json` (23 items).

No personal data was found in the L08 files. The fork username does not appear.

## The number conflict: $294k or $298.6k?

Both figures use the **same 15 Oct 2026 par curve**. The data is identical in my download and in `caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`. The two figures differ only in **method**:

| Method (cost on 1 Jan 2027) | 6 Oct | 15 Oct | Room on 15 Oct |
|---|---|---|---|
| Holding maturity dates, today's curve applied on 1 Jan 2027 ("yields unchanged"); waiting cash earns 0% | $293,453 | **$298,628** | $1,372 (4.7bp) |
| Holding maturity dates, forward rates | $292,388 | $297,847 | $2,153 |
| 1 Jan payment dates, yields unchanged | $290,005 | $295,246 | $4,754 (16bp) |
| 1 Jan payment dates, forward rates (waiting cash earns market forwards) | $288,938 | **$294,461** | $5,539 (19bp) |

- **L08's $298,624** uses the first method. This is the team's own "executable" basis: MONITOR.md:22 gives "$293,447 ... 22.7bp" on 6 Oct, and COMPETITION.md:153-154 gives "$293k ... about 0.2 percentage points". It is higher for two reasons:
  - cash waits at 0% between each maturity and its payment;
  - no roll-down is earned.
- **The 16 Oct number sheet's $294,453** (`results.json`) uses the last method. V5's "$292,000 at late-September yields" is on this basis too: 25 Sep gives $292,272. If waiting cash earns the 3-month yield, the cost is about $295.3k (L03 verifier).

**Which figure fits which claim:**
- *"What the ten payments cost" (IPS, Final Report).* Use the payment-date, market-rate basis: about $294.5k to $295.3k on 15 Oct, with about $4.7k to $5.5k of room. Laura's plan parks early cash in a short-term Treasury ETF (05_...md:16-17), so this basis is realistic.
- *"Has the IBTR note's 0.2-point trigger moved?" (TNA).* Compare like with like on the maturity basis. The room went from 22.7bp to 4.7bp. On the payment-date basis it went from about 38bp to 19bp. Either way it has halved or worse.
- **$298.6k** is a conservative bound, with the cash earning nothing. It should not be the headline.
- *Odds the ladder costs more than $300k on 1 Jan 2027.* About 28-33% on the market-rate bases, using my driftless estimate with 4.2-4.8bp daily vol in 2026 and 52 trading days. The sheet says 35%. On the 0% basis it is about 44-45%. "About 1 in 3" is fair; "coin toss" or "central case" is not.
- The sheet also contradicts itself. `results.json` has a third method (par-as-zero, $295,924, headroom $4,076, 13.4bp), while its text says 0.19 points.

## Verdicts

**COH-01: ladder headroom. ADJUSTED (stays high).**
- Confirmed: the stale quotes at 05_...md:15 and :29, V5:16 and :24, COMPETITION.md:153-154 and MONITOR.md:22. The 15 Oct curve values are confirmed.
- Changed: the headline mixed bases (see above). The odds come down from about 45% to about 1 in 3.
- Changed: the floor effect of a 25bp fall is a top-up of about $1.8k-5.9k depending on basis, which leaves a floor of about $148k-144k.
- It stays high because the IBTR note is a suggested TNA pick, the TNA is due in 7 days, and notes cannot be edited.

**COH-02: stock share vs WInS. ADJUSTED (high → medium).**
- Confirmed: VT is 167 × 158.83, which is 8.84% of $300k. The sheet target is 8.7%. The "~9%" and "~$40k" lines are confirmed.
- Changed: the plan's share is about 6.9% to 8.1%. It depends on the basis and on where the 2027 leftover sits: the sheet's 8.7% put it in VT, while the 16 Oct number sheet keeps it as a Treasury (VT about $32k).
- A gap of 1-2 points does not justify a trade. The 15 Oct brief already found that no rebalance was needed (final.md:589-590).
- Fix changed: pin the mirror to the trade-date plan with a tolerance band.

**COH-03: VT note "only" vs V5's four jobs. ADJUSTED (high → medium).**
- Confirmed: the quotes.
- Changed: "the leftover is stock money" was stated as fact. Tab 15:34 asks it as an open question ("如果它在 VT 里", which means "if it is in VT"). The 16 Oct sheet models the leftover as a Treasury.
- Changed: the note's "only" describes what stocks do to the gift. The tension with V5 is real but mild.

**COH-04: six floor definitions. ADJUSTED (stays high).**
- Wrong citation: strategy_notes.md:47 is about the OODA loop. The "$150k ... money she already owns" text is at :20.
- New: the 16 Oct sheet now offers one definition ("$150,000 face, quoted as $145,000", lowered by any top-up; IPS_number_sheet.md:14). So this is now a vote, not a research gap.
- The D_range "2 times in 3" figure is from the STRIPS era. The sheet gives a payout of at least 98.7% of face in 99 of 100 paths.

**COH-05: "never below the floor". ADJUSTED (high → medium; known-deeper).**
- Confirmed: the journal quote (final_report.md:24) and the missing 6 Oct entry.
- Already known: the team lists softening the phrase as an open item (COMPETITION.md:199-200). Tab 15:27 rewrote the logic, and the 15 Oct brief banned the phrase (final.md:137).
- What is new: the STRIPS reason and the missing "challenge" story for Articulation.

**COH-06: WInS mapping and scale. ADJUSTED (high → medium).**
- Confirmed: the 0.643 scale and the 9-of-11 count.
- Refuted, part 1: "drop COMPETITION.md:70's gloss". The official page says "The $300,000 is your team's WInS simulator balance. The additional $150,000 contribution ... will not be added to WInS" (trading.txt:26). The gloss is a fair reading.
- Refuted, part 2: the IBTR note's "$300,000 ... all ten payments" is about Laura's plan, so it does not clash with the 65.9% WInS split.
- Refuted, part 3: ips_outline.md:3 "WInS is the real ladder" refers to D7's dropped shadow-ladder branch (decisions/LOG.md:33). It is shorthand, not an error.
- Correction: TNA-FINAL:53 "we will verify this" refers to trades being executed, not to how notes are sized.

**COH-07: "depends mainly on the US government". ADJUSTED (medium; known-deeper).**
- Confirmed: the quotes and the table. For example, Feb-2037 delivers about 93% of its scaled target if coupons earn 0%.
- No longer new: the 16 Oct sheet, section 3, makes the same point.
- L08's added value is that the filled notes already admit the risk.

**COH-08: "$292,000 has no basis". ADJUSTED (medium).**
- Partly refuted: V5 dates the figure ("late-September 2026 yields"), and it reproduces exactly on the sheet's basis.
- Confirmed: CLAUDE.md:121-122 still says "VERIFIED" while :106-107 corrects it. The 16 Oct commit adds a third figure (~$294k).
- Fix changed: label the method for each claim, not one maturity-basis rule for all.

**COH-09: six strategy names. ADJUSTED (medium → low).**
- CLAUDE.md:65 sits in a section marked superseded.
- V5, Tab 15 and the journal already agree. The only live risk is COMPETITION.md:147 and :204.

**COH-10: Feb-2037 coupon. CONFIRMED (medium).**
- I re-computed the yield at the 96.019 fill: 5.25% with a 4.750% coupon, 5.51% with 5.000%.
- It was flagged on 15 Oct and is still not fixed.

**COH-11: reserve size undefined. CONFIRMED (medium).**
- I re-computed $396,131 (forward) and $404,949 (curve unchanged).
- The IPS is "not expected to include final operating-reserve calculations" (IPS-FINAL.txt:68-70), so the numbers belong in the Final Report, as the fix already says.

**COH-12: shortfall order. ADJUSTED (medium).**
- Confirmed: the order differs between files.
- Partly wrong: "V5 drops the 2031 check". V5:30 does adjust the 2031 bottom "after any expected shortfall", while D_range adjusts the top.
- The sheet shows most shortfalls arise after 2033.

**COH-13: "income reinvested ... held without trading". CONFIRMED (medium).**
- T-bills (trading_notes.csv:129) are out after 6 Oct (COMPETITION.md:89-90).

**COH-14: "latest first" vs order timestamps. CONFIRMED (low).**

**COH-15: stale files feed the Final Report. CONFIRMED (medium).**
- The PDF text search found no "STRIPS" or "superseded" on any of its 27 pages.
- trading_notes_pack.md and the README have no banner.

**COH-16: "Show chart 02". CONFIRMED (low).**
- The ban is at IPS-FINAL.txt:123, and :82-83 says non-compliant submissions will not be considered for semifinal selection.

**COH-17: rule statements. CONFIRMED (low).**
- I re-fetched the Rules & Roles page live on 16 Oct 2026. Both quotes were found: Top 50 chosen on the "Investment Policy Statement (IPS) and Final Reports", and the recording ban.

**COH-18: "91% Treasuries". CONFIRMED (low).**
- At cost: 89.9% including cash, 91.0% excluding it.

**COH-19: no re-price rule. ADJUSTED (medium).**
- The FOMC dates are now verified on federalreserve.gov (accessed 16 Oct 2026): "October 27-28" and "December 8-9*".
- The December meeting falls after the 4 Dec Final Report deadline.

**COH-20: terminology drift. CONFIRMED (medium).**

## Added findings

**VER-L08-01: the 16 Oct commit adds a second ladder basis and hides the change since 6 Oct (high).**
- COMPETITION.md says "$293k on the 6 Oct curve" (maturity basis).
- The sheet and CLAUDE.md say "about $294,000" on 15 Oct (payment basis), and the sheet adds "It was $290-292k a week ago".
- Read side by side, these suggest that yields barely moved. Like for like, the cost rose about $5.2k-5.5k.
- This will surface in the IBTR reflection.

**VER-L08-02: the sheet's confidence figures rank the gift above the payments (high).**
- The gift falls inside the range in 99.4% of paths.
- In 6.3% of paths, part of a later payment is not covered by what Laura kept (median about $3,150; `results.json`).
- The case makes the payments the first duty: "high degree of certainty" (Client_Profile.txt:91), and the range "must also protect" them (:119-120).
- This overlaps the L03 verifier's STRAT-03.

**VER-L08-03: the 16 Oct [AI] suggestions would create new contradictions if accepted as written (high).**
- Suggestion 5 changes the body to $294k but leaves the pitch at $292k (V5:16).
- Suggestion 2 says "principal depends only on the US government". That is false for the five iBond rungs: iShares says they "do not seek to return any predetermined amount" (IBTM page, accessed 16 Oct 2026), and the IBTM, IBTO, IBTP and IBTQ notes say "payout is not fixed".
- Suggestions 11-12 put a dollar range and "99 times in 100" into the IPS. IPS-FINAL.txt:68-70 says this is not expected, and caplet-latest/COMPETITION.md:202-203 now steers the team to do it.
- UNVERIFIED: whether these suggestions have been posted into the Google Doc.

## Does commit 412e9e3 change L08's conclusions?

Yes, in four places:
- It supplies the like-for-like headline ($294.5k), so COH-01 and COH-08 are corrected.
- It proposes a floor definition, which turns COH-04 into a vote.
- It already discloses coupon risk, so COH-07 is known-deeper.
- It introduces three new coherence risks (VER-L08-01 to 03).

The new "[AI] suggestions" rule does not change any verdict. No fix in the surviving set contains drafted deliverable prose.
