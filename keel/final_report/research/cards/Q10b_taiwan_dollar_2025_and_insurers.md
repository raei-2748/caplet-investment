# Q10b research cards: how hard a test is a 10% stronger Taiwan dollar, what May 2025 shows, and why test that side

Sat 14 Nov 2026, Sydney morning. Report parts: 3b (the contribution and her flexibility), 3e (assumptions, limits and
what to watch) and Table 3 row 7 ("Her flexibility's three uses": NT$32.768 per US$1 on 6 Nov 2026; trigger "A Taiwan
dollar 10% stronger ($11,500 more on $115,000)"). Notes for the Final Report store, not report prose.

Checked against: Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt` l.15, frozen: half the shares
"promised to no one. That is your flexibility – for building costs that overrun, a stronger Taiwan dollar or a
co-sponsor falling short"), the Trading Notes (l.7, "a nonexistent inflation risk", about the payments), `CANON.md`
(A31: discuss each use "without sizing a contingency fund"; C15), `NUMBERS.md` (8d: 32.768 and the ten-year strongest
27.52, $18,116-$21,930 more; 8j: $11,500 on $115,000, her flexibility $21,347 covers it in 93.2% of house simulated
futures, 96.9% history, 99.3% joint, 99.77% with the excess; on the real currency since 1983, a move of 10% or more
against Laura in 11.0% of 417 windows and covered in 98.1%; 8l: the EXTAUS mirror verified), `exhibits/tables.md`
Table 3 row 7, card Q10 (rows 18, 24, 25), card Q24 (rows 22, 23) and the INFLATION_TWD store (H3-112, H4-175, H7-089,
H9-128, H3-018, Q10-021 to Q10-025, Q24-022, Q24-023). Every plan figure here is quoted from NUMBERS and is MODEL. The
plan is frozen: a "risk" in the Clash column is a risk to record, never a change to propose. Taiwan law and tax are
out of scope; nothing here is about Laura Gao's real life.

**Claims tested**
1. Keep, kill or change: "A 10% stronger Taiwan dollar over about two years (2031 to late 2032) is a fair test: large
   enough to be a real stress, not so large it is implausible."
2. Keep, kill or change: "The May 2025 move shows how fast the Taiwan dollar can strengthen, and why: Taiwan's life
   insurers' large unhedged US-dollar holdings and their hedging flows, plus trade-policy pressure."
3. Keep, kill or change: "Today's level (about 32.8 per US$1) leaves more room to strengthen than to weaken, so the
   test's direction is the right one."

**Problem class and the field that solved it.** A fixed sum in one currency that must buy a budget priced in another,
on one date, with no hedge: how big a currency move should a stress test assume, how fast can it come, and does
today's level say which way it will go? International finance answers the last part (exchange rates are close to a
random walk over a few years; purchasing power parity pulls only slowly, half-lives of three to five years, store
H3-018). Central banking and insurance supervision answer the middle part for this currency: the Central Bank of the
Republic of China (Taiwan) (CBC) runs a managed float with two-way smoothing, and Taiwan's life insurers hold about
US$700 billion of foreign assets against NT$ policies, so their hedging is part of the market (BIS, the US Treasury,
the Financial Supervisory Commission, FSC). Stress-test practice answers the first part the way bank supervisors
calibrate historical scenarios: count every window of the right length in the record and say where the chosen shock
sits. Keel did that on the Fed's daily H.10 series since October 1983 (method at the end).

**Convention.** "x% stronger" means x% more US dollars for the same NT$ budget (start rate / end rate - 1), as in
NUMBERS 8d and 8j. The stricter reading (the rate falls x%) is given beside it. The CBC's own appreciation figure
(3.07% on 2 May 2025) uses the same convention; the press's "5.85%" over 30 April to 5 May is the rate's fall,
which is +6.21% on ours.

## Verdicts in one screen

1. **Claim 1: KEEP, with two additions.** 10% sits near the top tenth of two-year moves: a rise of 10% or more in the
   US dollars needed came in 9.0% of two-year windows starting since November 2001 (6.1% on the stricter reading),
   7.3% of those starting in the last ten years and 13.2% since October 1983, where the 1985-1989 revaluation
   dominates (Keel arithmetic, Fed H.10 daily). That agrees with 8j (11.0% of 417 monthly windows) and Q10 row 25 (8%
   since 2000). So it is a real stress, about one two-year stretch in ten, and not the worst case: the worst two-year
   moves were +19.4% (March 2009 to March 2011) in the last 25 years and +39.7% (December 1985 to December 1987) in the
   series, and the ten-year-strongest test in 8d (+19.1%, $21,930) already covers the 25-year worst. Addition (a):
   "over about two years" must not read as "gradually". The whole 10% came in 20 trading days in April and May 2025
   (+10.33%, 8 April to 6 May on H.10), so Table 3 row 7 may give no warning; the arithmetic is unchanged because only
   the rate on the day the contribution is converted counts. Addition (b): 10% stronger than 6 Nov 2026's 32.768 is
   NT$29.79, where the rate sat on 26.0% of days in the last ten years and on 35 days between 29 May and 7 August 2025, so
   the trigger is a familiar level, not an extreme. 8j measures the move from the 2031 meetings, not from today: the
   row should name its base (section c, for the lead).
2. **Claim 2: CHANGE.** The speed is right and is a record: on the CBC's Taipei closes the Taiwan dollar rose 3.07% on
   2 May and 6.21% over the two sessions to 5 May (32.017 to 30.145), about 8% intraday on 5 May (secondary), 6.98%
   over May, and 15.15% from the year's weakest close (33.196, 1 April) to its strongest (28.828, 3 July), 93 days. On
   the Fed's series since 1983 the one-day, two-day, one-week and 20-day moves of May 2025 are each the largest on
   record. The "why" is wrong as written. The CBC named speculation on what US tariff talks might bring, exporters
   dumping US dollars and foreign money buying Taiwan's chip shares, and said the US Treasury never asked for a
   stronger currency; the FSC denied that insurers traded heavily (secondary); the US Treasury found the second
   quarter's resident inflow "predominantly driven by the life insurance industry", with insurers' foreign assets
   cut sharply in May, and named "thin liquidity during local holidays"; the BIS found hedging by Asian investors
   played "an important contribution" but is "difficult to disentangle" from speculation. So: several forces at once,
   with insurers' hedging and selling one of them, and "trade-policy pressure" is better said as "expectations around
   US tariff talks". One structural point strengthens the claim: insurers' hedge ratio has since fallen to a record
   50.23% (CBC, end-2025) and 45% (February 2026, Bloomberg via the US Treasury), so the unhedged stock that a rush to
   hedge could hit is larger than in May 2025.
3. **Claim 3: CHANGE.** The description holds only over ten years: 32.85 (H.10, 6 Nov 2026) is weaker than 98.0% of
   days of the last ten years, 1.1% from the ten-year weakest and 19.4% from the strongest; over 25 years it is the
   79th percentile and 6.7% from the weakest (35.21, March 2009). "Room" is not a forecast. In the record, starts in
   the top tenth of their own ten-year range were followed by a 10% rise in 21.1% of two-year windows against 7.9% for
   all starts in the same years, but on 13 start years and overlapping windows, and the next band down (80th to 90th)
   showed no effect; suggestive only. Reasons it could be stronger by 2031-2033 exist (a current-account surplus of
   19.6% of GDP in 2025, private models showing "substantial undervaluation", a joint US-Taiwan statement that
   intervention is for volatility in either direction, record-low insurer hedging), and so do reasons against (the
   FSC's 2026 accounting change cuts hedging demand, which the US Treasury says "may contribute to reduced
   appreciation pressure"; Taiwan's real exchange rate fell in 2026; 90% of the April-July 2025 rise had reversed by
   6 Nov 2026). The test's direction is right for a simpler reason: the contribution is fixed in US dollars and spent
   in NT$, so only a stronger Taiwan dollar costs Laura anything; a weaker one buys more (7.5% more NT$ at the
   25-year weakest). The direction comes from the exposure, not the level.
4. **No clash with the frozen plan.** IPS l.15 names "a stronger Taiwan dollar" as a use of her flexibility and the
   test checks it without sizing a contingency (CANON A31). Risks to record: Table 3 row 7 cannot warn ahead of a jump;
   its base rate is ambiguous; and the store's May 2025 rows (H3-112, H4-175) now have primary sources.

## (a) Table

Report landings are given first in the "Analogy/use" column: **3b**, **3e**, **T3r7** (Table 3 row 7 or its note),
**store** (keep, not in the report).

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A two-year rise of 10% or more in the US dollars a NT$ budget needs came in 9.0% of two-year windows starting since Nov 2001 (stricter reading 6.1%; median +0.9%; 1 in 20 at +11.9%); 8.3% since 2000; 7.3% in the last ten years; 13.2% since Oct 1983 (1 in 20 at +19.5%) | Keel arithmetic on Board of Governors (n.d.-b) DEXTAUS, Fed H.10 daily, 3 Oct 1983 to 6 Nov 2026 | INFLATION_TWD, HALFKEPT, MOVE2031 | NICHE | **3e**: the 10% test is about a one-in-ten two-year move over 25 years: a real stress, not the worst case. Agrees with 8j (11.0% of 417 monthly windows) and Q10 r25 (8% since 2000) | 5,764 overlapping daily starts are about 12 independent two-year spans; one currency's history, two regimes | VERIFIED (data file read in full; `twd_windows.py`) | no | Section (a); method at the end |
| 2 | One-year windows: 10% or more in 1.9% of starts since Nov 2001 (5.6% since 1983); largest since 2001 +13.1% (Jun 2010 to Jun 2011) and +13.0% (Jul 2024 to Jul 2025) | Keel arithmetic, DEXTAUS | INFLATION_TWD, MOVE2031 | NICHE | **store**: if the contribution is stated late in 2031, the window to December 2032 is nearer one year and 10% is rarer | Same overlap caveat | VERIFIED (script) | no | Method |
| 3 | Three-year windows: 10% or more in 8.2% of starts since Nov 2001, largest +19.6% (Mar 2009 to Mar 2012); since 1983 14.0%, largest +51.8% (May 1986 to May 1989) | Keel arithmetic, DEXTAUS | INFLATION_TWD | NICHE | **store**: longer windows add little after 2001; the 1980s are a different regime | none recorded | VERIFIED (script) | no | Method |
| 4 | The worst two-year moves: +39.7% (Dec 1985 to Dec 1987); +19.4% (Mar 2009 to Mar 2011), the 25-year worst; +14.1% (May 2019 to May 2021); +13.2% (Mar 2003 to Mar 2005); +8.4% (Jul 2023 to Jul 2025) | Keel arithmetic, DEXTAUS | INFLATION_TWD, HALFKEPT | NICHE | **3e/store**: 8d's ten-year-strongest test (+19.1%, $21,930) is about the 25-year worst; 8j's house model covers 19 in 20 up to 15.6% | 8j's real-currency windows (monthly averages) give +29.4% as the largest, since its windows start Oct 1986 | VERIFIED (script) | no | Method |
| 5 | Peak-to-trough strengthening episodes: Aug 1985 to Jul 1992 +65.7% (6.9 years); Oct 2002 to Mar 2005 +14.7% (2.4); Mar 2009 to May 2011 +23.5% (2.2); Aug 2019 to Jan 2022 +14.9% (2.4); Apr to Jul 2025 +15.0% (93 days) | Keel arithmetic, DEXTAUS | INFLATION_TWD | NICHE | **store**: since 1992 each big episode was 15% to 24%, three of them over about two years, the last in three months | Causes of the 1980s episode not read at a source | VERIFIED (script) | no | Method |
| 6 | Daily-change volatility was 4.4% to 5.1% a year in every era 1984-2024 and 6.0% from Jan 2025 to Nov 2026; ten-year 4.68%, a two-year standard deviation of about 6.6%, so 10% is about 1.5 of them | Keel arithmetic, DEXTAUS | INFLATION_TWD | KNOWN | **store**: a cross-check; the observed 9.0% is above the 6.5% a normal curve gives, the fat tail the window count already shows | Volatility understates jumps like May 2025 | VERIFIED (script) | no | Method |
| 7 | 10% stronger than 6 Nov 2026's 32.768 is NT$29.79 (stricter 29.49): the rate was at or below 29.79 on 26.0% of days in the last ten years, 18.3% in 25 years, in 11 of the 17 years since 2010, most recently on 35 days between 29 May and 7 Aug 2025 | Keel arithmetic, DEXTAUS; CBC (n.d.) closing rate | INFLATION_TWD, COSPONSOR | NICHE | **T3r7 note**: the trigger is a level the currency held fifteen months ago, not an extreme | 8j measures from the 2031 meetings, not from today; the row should name its base | VERIFIED (script, `twd_level.py`) | risk: row 7's base is ambiguous (section c) | Method |
| 8 | Today's level: 32.85 (H.10, 6 Nov 2026) is weaker than 98.0% of days in ten years (median 30.61), 79.0% in 25 years (median 31.38), 76.0% since 1983; 1.1% from the ten-year weakest (33.21, 1 Apr 2025), 19.4% from the strongest (27.52, 4 Jan 2022), 6.7% from the 25-year weakest (35.21, 2 Mar 2009); 2026 range 31.27 to 32.94 (5 Nov) | Keel arithmetic, DEXTAUS; CBC close 32.768 | INFLATION_TWD | KNOWN | **3e/store**: "more room to strengthen" holds over ten years, much less over 25 | A level is not a forecast (row 9) | VERIFIED (script; extends Q10 r25) | no | Method |
| 9 | Starting from the top tenth of its own trailing ten-year range, the next two years brought a 10% rise in 21.1% of windows (median +3.7%) against 7.9% (median -0.7%) for all starts 1993-2024; from the top twentieth, 24.5%; but 13 and 8 distinct start years, and the 80th-90th band showed 8.3% | Keel arithmetic, DEXTAUS (`twd_windows.py`, `twd_extra.py`) | INFLATION_TWD | NICHE | **store**: supports testing the strong side, never a probability for 2031-2033 | Few independent episodes; exchange rates are near a random walk at this horizon (H3-018) | VERIFIED (arithmetic); the inference is weak | no | Method |
| 10 | The weak side is just as wide: the worst two-year weakening was -21.3% (Jan 1996 to Jan 1998) and -14.4% (Oct 2021 to Oct 2023); one-day -4.00% (Oct 1997) | Keel arithmetic, DEXTAUS | INFLATION_TWD | KNOWN | **store**: a weaker Taiwan dollar helps Laura, so it is not tested | none recorded | VERIFIED (script) | no | Method |
| 11 | May 2025 on the CBC's Taipei closes: 32.017 (30 Apr), 31.064 (2 May, +3.07%), 30.145 (5 May, +6.21% over two sessions); 29.929 (29 May, +6.98% for May); 1 Apr's 33.196 to 3 Jul's 28.828, +15.15% in 93 days; 31.438 at end-2025 (+4.27% for the year) | CBC (2025c) daily closes; CBC (2025a) No. 078 | INFLATION_TWD, COSPONSOR | KNOWN | **3e**: one clause, the whole 10% can come in weeks; what counts is the rate on the conversion day | Taipei closes, not New York noon rates; the two differ by up to about 1% | VERIFIED (table and release read in full) | no | CBC 2025 table |
| 12 | On the Fed's series since Oct 1983, May 2025 holds the largest one-day (+4.16%, 1 to 2 May), two-day (+7.15%), five-day (+8.42%) and 20-day (+10.33%, 8 Apr to 6 May) rises; the next one-day is +3.48% (Dec 2008) | Keel arithmetic, DEXTAUS | INFLATION_TWD | NICHE | **3e/store**: a record, so the speed point is not a cherry-pick | H.10 New York noon rates straddle a Taipei holiday (1 May) | VERIFIED (script) | no | Method |
| 13 | Intraday 5 May the rate touched about 29.59, about 8% in two days; May's 6.98% was the largest monthly rise since 1989; 2 May the largest one-day rise since the CBC's closing-rate records began (1993) | CNA (2025a); Taipei Times (2025a); cnyes (2025); AM Best (2025) | INFLATION_TWD | KNOWN | **store**: quote only with "about" and a secondary source | Not read at a primary source | UNVERIFIED (search excerpts; CBC closes agree on the close-to-close figures) | no | Search excerpts |
| 14 | The CBC on 2 May: media reports since April that the US might seek a stronger NT$ in tariff talks; TSMC +4.63%, TAIEX +552.61 to 20,787.64, foreign net buying NT$42.924bn; the bank stepped in; the US Treasury had not asked | CBC (2025a) No. 078 | INFLATION_TWD, TWOREASONS | KNOWN | **3e**: "trade-policy pressure" becomes "expectations around US tariff talks" | none recorded | VERIFIED (read in full, Chinese) | no | CBC release |
| 15 | The CBC on 5 May, seven points: fundamentals; since 9 April foreign equity inflows and exporters' US-dollar selling on appreciation expectations; the CBC is not in the trade talks and the US did not ask; the "Mar-a-Lago Accord" is speculation; no insurers named | CBC (2025b) No. 079 | INFLATION_TWD | KNOWN | **store**: the central bank's account names no insurer flow | A central bank defending its record | VERIFIED (read in full, Chinese) | no | CBC release |
| 16 | The governor (5 May): the main force was exporters dumping US dollars, large and small; on insurers, losses of "1兆多" (over NT$1tn) on paper, not as large as NT$2tn; the FSC (6 May): large insurers hedge on their own strategies and "未在外匯市場有大量交易" (did not trade heavily) | CNA (2025a, 2025b) | INFLATION_TWD | KNOWN | **store**: the two Taiwanese authorities played insurers down | Not read at the source | UNVERIFIED (search excerpts); CONFLICTING with row 17 | no | Search excerpts |
| 17 | The US Treasury: Q2 2025 residents' portfolio flow swung to a $7bn inflow, "predominantly driven by the life insurance industry", the first since 2011; the CBC's industry data show "a sharp reduction in foreign assets in May"; nonresident inflow $14.1bn, a record; "thin liquidity during local holidays"; the TWD was allowed "to strengthen about 10% to a level more consistent with the underlying fundamentals" | U.S. Department of the Treasury (2026a), Taiwan section | INFLATION_TWD | NICHE | **3e/store**: insurers were one force, with foreign equity money and exporters | Treasury's own inference from balance-of-payments data | VERIFIED (Taiwan section read in full) | no | Treasury Jan 2026 |
| 18 | The BIS: hedging by non-US investors made "an important contribution" to the dollar's slide in April-May 2025; Taiwanese life insurers were about 65% hedged in late 2024, "near historic lows" (BofA); raising a hedge ratio after the fact hits the spot rate; the fall came mostly in Asian hours; "difficult to disentangle hedging from speculative positioning or disinvestment" | Shin, Wooldridge and Xia (2025) | INFLATION_TWD, OTHER | NICHE | **store**: the hedging channel is real and measured, its share unknown | One bulletin; cites Liao and Zhang (2025), not read | VERIFIED (read in full) | no | BIS Bulletin 105 |
| 19 | Insurers' stake: US$1.2tn of assets (131% of GDP), about 60% foreign, over US$700bn of foreign exposure, hedged with non-deliverable forwards and currency swaps; FSC: foreign investments NT$22.3tn, net exposure NT$15.2tn about 60% hedged (end-Oct 2025) | U.S. Department of the Treasury (2026b); FSC (2025d) | INFLATION_TWD, HALFKEPT | NICHE | **store (card 2)**: the same exposure as Laura's contribution, US-dollar money and NT$ needs, at national scale | Insurers' exposure is continuous and regulated; Laura's is one dated sum | VERIFIED (both read) | no | Treasury Jul 2026; FSC 23 Dec 2025 |
| 20 | Hedging costs the interest-rate gap: insurers paid NT$1.6tn for hedging from 2019 to Oct 2025, more than their NT$1.4tn of after-tax profit; Taiwan's policy rate has been 2.0% since the start of 2024 | FSC (2025d); U.S. Department of the Treasury (2026b) | INFLATION_TWD, HALFKEPT | NICHE | **store**: why no one fully hedges this exposure, and why a reserve was preferred | Laura's plan cannot hedge anyway (row 31) | VERIFIED (read) | no | FSC 23 Dec 2025 |
| 21 | Hedge ratios falling: about 70% before COVID, 60% in Sep 2025, 45% in Feb 2026 (Bloomberg via Treasury); a record-low 50.23% at end-2025 (CBC), with FX valuation reserves at a record NT$613.7bn | U.S. Department of the Treasury (2026b) Box 1; CBC (2026) FSR | INFLATION_TWD | NICHE | **3e/store**: the unhedged stock that a rush to hedge could hit is larger than in May 2025 | The 45% is Bloomberg's, cited by a primary source | VERIFIED (CBC 50.23%); 45% secondary within a primary | no | FSR May 2026; Treasury Box 1 |
| 22 | Insurers' 2025 bill: FX losses NT$548.5bn on net foreign assets against hedging gains of NT$57.4bn; pretax income down 50.25% to NT$156.9bn; RBC 315.09%; the FSC's combined FX impact (losses, hedging and reserve) was -NT$263.8bn to end-May, -NT$522.0bn to end-June, -NT$704.8bn to end-November | CBC (2026) FSR; FSC (2025a-c) monthly releases | INFLATION_TWD | KNOWN | **store**: what a 10% move does to an unhedged dollar holding | Reported figures, cumulative year to date | VERIFIED (read) | no | FSR; FSC releases |
| 23 | The regulator chose reserves over full hedges: a new FX valuation reserve (2024; up to 100% offset of unhedged FX losses); 12 Jun 2025 temporary measures (half-year average rates for capital, 30% of 2025 pretax profit into the reserve); 30 Jun 2025 order (mismatch plans); 23 Dec 2025, amortise FX differences on amortised-cost bonds from 1 Jan 2026 (IAS 21 departure); 12 Feb 2026, a volatility reserve, a fixed reserve capped at 10% of net exposure, and a strengthening reserve set by the cut in hedge ratio | FSC (2025e, 2025d, 2026); FSC Insurance Bureau (2025); CNA (2025c) for 2024 | INFLATION_TWD, HALFKEPT, CERTAINTY | NICHE | **store (card 2)**: Taiwan's supervisor answers the same exposure as Laura's with money set aside ahead, not a full hedge, as IPS l.15 does with her flexibility | An accounting reserve smooths earnings; Taiwan Ratings says it "would not reduce the underlying risks" (row 25) | VERIFIED (FSC 2025d, 2025e, Insurance Bureau 2025 and FSC 2026 read in full); 2024 start UNVERIFIED | no | FSC releases |
| 24 | The US Treasury on the FSC's rule: the FSC "acknowledged that these rules depart from industry best practices"; it "may contribute to reduced appreciation pressure on the TWD by limiting hedging activity" | U.S. Department of the Treasury (2026b) Box 1 | INFLATION_TWD | NICHE | **store**: a reason the TWD may rise less, set against row 21 | One assessment | VERIFIED (read in full) | no | Treasury Jul 2026 |
| 25 | Taiwan Ratings (quoted by the CBC): the reserve and accounting changes "would not reduce the underlying risks arising from currency mismatches"; "Under extreme FX rate scenarios, profitability could still be significantly affected" | CBC (2026) FSR | INFLATION_TWD, HALFKEPT | KNOWN | **store**: the limit of a reserve: it must be real money and big enough | Taiwan Ratings' own report not read | VERIFIED (as quoted by the CBC) | no | FSR May 2026 |
| 26 | The CBC: "massive and frequent movements of international short-term capital flows have overtaken international trade flows and macroeconomic fundamentals as the primary drivers of exchange rate fluctuations in the short term" | CBC (2026) FSR | INFLATION_TWD, CERTAINTY | KNOWN | **3e**: the rate on the contribution day is a flow outcome no one can forecast; the plan tests it rather than predicts it | none recorded | VERIFIED (read) | no | FSR May 2026 |
| 27 | The regime: the 14 Nov 2025 joint statement keeps intervention "for combatting excess volatility and disorderly movements", "equally appropriate" against depreciation or appreciation, with quarterly disclosure; the CBC notes the US "從未要求" (never asked) for a stronger NT$ | U.S. Department of the Treasury and CBC (2025); CBC (2025d) | INFLATION_TWD, COSPONSOR | KNOWN | **store**: the CBC smooths, never caps: in 2025 it bought heavily and still let the rate move about 10% | Policy can change before 2031 | VERIFIED (both read in full) | no | Joint statement |
| 28 | Intervention size: net purchases $13.25bn in H1 2025 (3.1% of H1 GDP), net sales $5.56bn in H2, $7.7bn net for the year; strong interventions on 2 and 5 May and 27 and 30 Jun; forward book $79bn at end-2025; once "a previously undisclosed forward book that at one point approached $100 billion" supported insurers' hedging, disclosed since 2020 | U.S. Department of the Treasury (2026a, 2026b); CBC (2026) FSR | INFLATION_TWD | NICHE | **store** | none recorded | VERIFIED (read) | no | Treasury reports |
| 29 | Reasons for a stronger NT$: current account 19.6% of GDP in 2025 (14.1% in 2024); goods and services surplus with the US $145bn; growth 8.7%; private models "tend to show substantial undervaluation"; Cline's estimate "in the low to mid 20s" (May 2022); Taiwan is not an IMF member, so there is no Article IV | U.S. Department of the Treasury (2026a, 2026b) | INFLATION_TWD | KNOWN | **store**: why the strong side is the plausible one to test; never a forecast | Cline not read; undervaluation has persisted for decades | VERIFIED (Treasury read); Cline UNVERIFIED | no | Treasury reports |
| 30 | Reasons against: real exchange rates of surplus economies "have continued to depreciate thus far in 2026, especially for Taiwan"; the NT$ rose 4.5% in 2025 but its real effective rate fell 0.3%; by 6 Nov 2026 the rate (32.768) had reversed 90% of the April-July 2025 rise (Keel arithmetic on CBC closes) | U.S. Department of the Treasury (2026b); CBC (2025c); Keel arithmetic | INFLATION_TWD | KNOWN | **store**: "room" is not momentum | none recorded | VERIFIED | no | Treasury Jul 2026 |
| 31 | The direction comes from the exposure: the contribution is fixed in US dollars and spent in NT$, so only a stronger NT$ costs; at the 25-year weakest (35.21) $115,000 buys 7.5% more NT$ than at 32.768. Laura cannot hedge inside the plan (only stocks, ETFs and Treasuries are permitted; offshore NT$ trades only as non-deliverable forwards) | Keel arithmetic; NUMBERS 8j; Wharton 6 Oct email (CLAUDE.md); U.S. Department of the Treasury (2026b) | INFLATION_TWD, HALFKEPT, CERTAINTY | KNOWN | **3e**: why the test looks one way; if a judge asks "why not hedge?", one clause | Taiwan law out of scope; the NDF point is market structure only | VERIFIED | no | Treasury Jul 2026 (capital controls) |
| 32 | The store's May 2025 rows rest on Bloomberg ("surges another 4%, jumping most since 1988"; "more than 6% in two days"); now primary: +6.21% over two sessions (CBC closes), the largest one-day and two-day moves since 1983 (H.10). The "$1.2bn insurer losses" (Bloomberg Law) stays unread; use the FSC's figures (row 22) | Store H3-112, H4-175, H7-089; CBC (2025c); DEXTAUS | INFLATION_TWD, PROCESS | KNOWN | **store**: upgrade the rows' sources | none recorded | VERIFIED (this card) | no | Store INFLATION_TWD |

## (b) Cards

**Card 1. May 2025, sized at the source (CBC closes and releases No. 078 and 079; Fed H.10).**
- *What is it?* The fastest rise of the Taiwan dollar on record. On the CBC's Taipei closes: 32.017 on 30 April,
  31.064 on 2 May (+3.07%, the CBC's own figure, after the 1 May holiday), 30.145 on 5 May (+6.21% over two sessions),
  about 29.59 intraday on 5 May (about +8%, secondary), 29.929 at the end of May (+6.98% for the month), and 28.828 on
  3 July, +15.15% from 1 April's 33.196 in 93 days. The year ended at 31.438, +4.27%. On the Fed's New York series
  since October 1983 every short window of May 2025 (one day +4.16%, two days +7.15%, five days +8.42%, 20 days
  +10.33%) is the largest strengthening on record; the next one-day move is +3.48% (December 2008).
- *Did it work?* The CBC bought dollars heavily on 2 and 5 May and again on 27 and 30 June (US Treasury) and smoothed
  the move without stopping it; the Treasury says the authorities "generally allowed" about 10%. Then it reversed: by
  6 Nov 2026 the rate was 32.768, 90% of the April-July rise undone.
- *How is Laura's case like it?* The contribution is converted on one day. A move of this size inside a month,
  just before December 2032, would raise the US dollars a NT$ budget needs by about the 10% the plan tests ($11,500
  on $115,000, NUMBERS 8j).
- *How is it not?* It was a short spike that reversed within about 16 months; Laura's exposure is the level on one
  day, and the case does not say who converts the dollars or on which day. The 2025 causes
  (tariff-talk expectations, a holiday-thin market, foreign equity inflows) may not recur.
- *What Caplet takes:* in 3e, the test is a level on a date, and the whole 10% can arrive in weeks, so Table 3 row 7
  watches but cannot promise warning; the answer is her flexibility being there, not a forecast. Quote May 2025 as
  "about 6% in two trading days" (CBC closes, our convention), never as a two-year path.

**Card 2. Taiwan's life insurers: Laura's exposure at national scale, and the regulator's choice of a reserve over a
full hedge (FSC 2025-2026; CBC FSR May 2026; US Treasury July 2026 Box 1; BIS Bulletin 105).**
- *What is it?* Taiwan's life insurers hold about US$700 billion of foreign assets against NT$ policies; a stronger
  NT$ is their loss. Hedging costs the interest-rate gap (NT$1.6tn from 2019 to October 2025, more than their NT$1.4tn
  of after-tax profit, FSC), so their hedge ratio fell from about 70% before COVID to a record 50.23% at end-2025
  (CBC) and 45% in February 2026 (Bloomberg via the Treasury). In 2025 they lost NT$548.5bn on net foreign assets
  against NT$57.4bn of hedging gains. The FSC answered with reserves set aside ahead: an FX valuation reserve, 30% of
  2025 pretax profit into it, amortised FX differences from 1 January 2026, and from February 2026 a volatility
  reserve, a fixed reserve and a strengthening reserve set by how far the hedge ratio is cut.
- *Did it work?* For solvency, so far: capital ratios stayed high (RBC 315.09% at end-2025) and the reserve reached a
  record NT$613.7bn. For risk, no: Taiwan Ratings (quoted by the CBC) says the changes "would not reduce the underlying
  risks arising from currency mismatches", and the US Treasury records that the FSC "acknowledged that these rules
  depart from industry best practices". For the market, both ways: lower hedging means a larger unhedged stock (fuel
  for a rush, as the BIS describes for April-May 2025) but less day-to-day hedging demand, which the Treasury says
  "may contribute to reduced appreciation pressure".
- *How is Laura's case like it?* The same sign of exposure: US-dollar money, NT$ needs. The same choice: no full
  hedge, because a hedge costs the rate gap every year, and money set aside ahead instead. IPS l.15's "a stronger
  Taiwan dollar" is one of her flexibility's three uses.
- *How is it not?* Laura's exposure is one dated sum of about $115,000, not a continuous book; her flexibility is
  real money in shares (which could fall at the same time; 8j finds the two-year currency move's correlation with
  shares +0.09, close to none), not an accounting reserve; she cannot hedge inside the plan at all (only stocks, ETFs
  and Treasuries are permitted); and insurers face policyholders and a regulator, while she faces co-sponsors.
- *What Caplet takes:* store only, unless 3e needs one clause of prior art: the large holders of exactly this
  exposure chose reserves set aside ahead over full hedges, for the same cost reason. The warning travels with it: a
  reserve works only if it is real money and big enough, which is what 8j tests.

**Card 3. How often does the Taiwan dollar rise 10% in two years? (Keel arithmetic on Fed H.10, 1983-2026).**
- *What is it?* Every trading day since October 1983 taken as a start, with the rate 12, 24 and 36 months later.
  Two-year rises of 10% or more in the US dollars needed: 13.2% of starts since 1983, 7.6% since 1990, 8.3% since
  2000, 9.0% since November 2001, 7.3% in the last ten years. One-year: 1.9% since 2001. The 1-in-20 two-year move
  since 2001 is +11.9%; the worst is +19.4% (2009-2011). Non-overlapping two-year January starts: 2 of 21 (1986-1988
  +39.5%, 2016-2018 +12.0%).
- *Did it work?* As a calibration, yes: the monthly windows in NUMBERS 8j (11.0%), Q10 row 25 (8% since 2000) and
  this daily count agree within a few points, and daily data give no hidden fatter tail beyond May 2025.
- *How is Laura's case like it?* The 2031 meetings to December 2032 is about two years, and the contribution is
  converted on one date, the windows' end.
- *How is it not?* Overlapping windows share most of their months, so 5,764 starts since 2001 are about a dozen
  independent two-year spans; regimes changed (the 1980s revaluation, two-way intervention since 2021, the 2025
  joint statement). The past is a range, not a probability for 2031-2033.
- *What Caplet takes:* 3e can say what kind of test 10% is: about one two-year stretch in ten since 2001 on the
  Fed's daily rates, with the worst of the last 25 years (+19.4%) covered by the ten-year-strongest test in 8d.
  NUMBERS keeps its own 11.0% (monthly, 417 windows); this card's figures are a cross-check, so 3e should quote one
  of them, named, not both.

**Card 4. Where the rate sits, and what that does not say (Keel arithmetic; US Treasury January and July 2026).**
- *What is it?* 32.85 on the Fed's series (32.768 at the CBC's close) on 6 Nov 2026 is weaker than 98.0% of days of
  the last ten years and 1.1% from its weakest, but only the 79th percentile over 25 years and 6.7% from the
  25-year weakest. Ten percent stronger than today, NT$29.79, is where the rate sat on about one day in four of the
  last ten years, most recently on 35 days between 29 May and 7 August 2025.
- *Did it work?* As a forecast, weakly at best: from starts in the top tenth of their own ten-year range, a 10% rise
  followed in 21.1% of two-year windows against 7.9% overall, but the effect rests on 13 start years, vanishes in the
  next band down, and fits the economics that exchange rates are close to a random walk at this horizon. The
  fundamentals point both ways: a current-account surplus of 19.6% of GDP and "substantial undervaluation" in private
  models against a 2026 real depreciation and an accounting change that cuts insurers' hedging demand.
- *How is Laura's case like it?* The contribution is fixed in US dollars; only a stronger NT$ costs her. Today's
  weak level makes the costly side more plausible, which is the right side to test.
- *How is it not?* Nothing about today's level fixes the 2031 rate that 8j measures from; if the NT$ is already
  stronger in 2031, a further 10% is measured from there.
- *What Caplet takes:* in 3e, the test looks at the stronger side because that is the only side that costs Laura;
  today's level only shows the trigger is not far-fetched. Never "the Taiwan dollar is likely to strengthen".

**Card 5. A managed float with a two-way promise (Treasury-CBC joint statement, 14 Nov 2025; CBC note; Treasury
reports).**
- *What is it?* The CBC intervenes in both directions: net purchases of $13.25bn in the first half of 2025, net sales
  of $5.56bn in the second, with a $79bn forward book. The joint statement reserves intervention "for combatting
  excess volatility and disorderly movements", "equally appropriate" against depreciation or appreciation, with
  quarterly disclosure from end-December 2025; the CBC says the statement is unrelated to the tariff talks and that the
  US never asked for a stronger NT$.
- *Did it work?* It slowed May 2025 and did not stop it: the rate still moved about 10%, which the US Treasury calls
  "a level more consistent with the underlying fundamentals".
- *How is Laura's case like it?* A central bank that smooths but does not cap is why a 10% move in a year or two stays
  plausible, and why a jump can still come in weeks.
- *How is it not?* Policy and people change before 2031; the statement binds no future rate.
- *What Caplet takes:* store; at most a clause in 3e that the rate floats with smoothing, so no level is promised by
  anyone.

## (c) Verdicts

**Claim 1, KEEP with two additions.** The test is fair. Since November 2001 a two-year rise of 10% or more came in 9.0%
of daily-start windows (6.1% stricter), about one in ten; 1 in 20 at +11.9%; worst +19.4%. Since 1983, 13.2%, driven
by the 1985-1989 revaluation (worst +39.7%). It sits beside 8j's 11.0% and Q10's 8%, and the ten-year-strongest test
(8d, +19.1%, $21,930) already covers the worst of the last 25 years, so the plan tests both a plausible stress and a
severe one. The additions: (a) speed, the whole 10% arrived in 20 trading days in April-May 2025, so "over about two
years" must not read as "gradually", and Table 3 row 7 is a watch, not a warning; (b) the base, 10% stronger than
6 Nov 2026 is NT$29.79, last seen in August 2025, while 8j measures from the 2031 meetings.

**Claim 2, CHANGE.** Keep "how fast": the move is a record on both the CBC's closes and the Fed's series since 1983.
Change "why": the official accounts differ. The CBC names tariff-talk expectations, exporters' dollar selling and
foreign equity inflows, and says the US never asked for a stronger NT$; the FSC denied heavy insurer trading
(secondary); the US Treasury attributes the second quarter's resident inflow "predominantly" to life insurers and adds
holiday-thin liquidity; the BIS finds hedging "an important contribution" but hard to separate from speculation. A
fair line: several forces at once in a thin holiday market, insurers' hedging and selling among them. "Trade-policy
pressure" becomes "expectations around US tariff talks". The structural point to keep is the hedge ratio's fall
since then (50.23% at end-2025, 45% in February 2026): more unhedged dollars than in May 2025.

**Claim 3, CHANGE.** "Room to strengthen" is true over ten years (98th percentile, 1.1% from the weakest) and much
weaker over 25 (79th percentile); it is a description, not a forecast, and the conditional evidence is thin. The
reason the direction is right is the exposure: a US-dollar contribution spent in NT$ loses only if the NT$ rises.
Say that, and use the level only to show the trigger is not far-fetched.

**Clash.** None with the FINAL IPS or the Trading Notes. Risks recorded: (1) Table 3 row 7 cannot warn ahead of a jump
like May 2025; the plan's answer does not need warning, since her flexibility is held either way; (2) row 7's "10%
stronger" has no stated base, and a reader will compute it from the 32.768 shown beside it; (3) the store's May 2025
rows rested on Bloomberg and are now verified at the source (row 32).

**Where each strong finding lands.**
- One-in-ten calibration and the worst case covered by 8d (Card 3): 3e, one clause, with one named source (8j's
  11.0% or this card's 9.0%, the lead's choice).
- Speed, the whole 10% in weeks (Card 1): 3e, one clause; Table 3 row 7 stays a watch.
- The direction follows the exposure (Card 4, row 31): 3e, one clause; replaces any "the Taiwan dollar is likely to
  strengthen".
- The base of row 7's trigger and NT$29.79 (row 7): Table 3's note, if the lead names the base.
- May 2025's causes, the insurers and the FSC's reserves (Cards 1 and 2): store; 3e only if a clause of prior art is
  wanted for "money set aside ahead instead of a hedge".
- The regime (Card 5), the conditional test (row 9), the weak side (row 10): store only.

**For the lead to decide.** (a) Whether Table 3 row 7 names its base ("from the 2031 rate" or "from NT$32.768", which
is NT$29.79). (b) Whether row 7's reader also watches the CBC's quarterly intervention disclosures and the insurers'
hedge ratio as context (Keel's view: no; they change nothing in the plan and would add cells, store only). (c) Which
single figure 3e quotes for how often 10% happens (8j's 11.0% on monthly data since 1983, or "about one two-year
stretch in ten since 2001" on daily data).

## (d) Gaps
- The CBC's own closing-rate history from the 1979 float to 1983 not read; the Fed series starts October 1983.
- The FSC's 6 May 2025 statement and the governor's 5 May press conference read only through CNA excerpts; the
  5 May intraday 29.59 and "largest monthly rise since 1989" are secondary.
- Liao and Zhang (2025, *Review of Financial Studies*) on the hedging channel and McGuire et al. (2021, BIS Quarterly
  Review) not read; both are cited by BIS Bulletin 105.
- Cline (May 2022) fundamental equilibrium exchange rates not read; quoted only through the US Treasury.
- The February 2026 hedge ratio (45%) is Bloomberg's, cited by the US Treasury; the CBC's 50.23% is the primary figure.
- The start date of the new FX valuation reserve mechanism (August or September 2024) rests on CNA and an EY
  newsletter excerpt.
- Meese and Rogoff (1983) on random walks not read in this run; the "near a random walk" point leans on store H3-018
  (Rogoff, 1996), also not re-read.
- No forward-rate cost for a hypothetical hedge computed: the plan cannot hedge, and the number would invite a change
  the frozen plan rules out.

## Method (Keel arithmetic)

Data: FRED DEXTAUS, Board of Governors H.10 noon buying rates in New York, NT$ per US$1, downloaded 14 Nov 2026
(Sydney) from https://fred.stlouisfed.org/data/DEXTAUS.txt ("Last Updated 2026-11-09"), 3 Oct 1983 to 6 Nov 2026,
10,518 daily observations after dropping 727 holiday markers ("."). Check: the monthly averages of these daily rates
match the repo's EXTAUS mirror (`keel/models/data/twd_per_usd_monthly.csv`) in all 516 months to 0.0001.

Windows: each trading day is a start; the end is the last observation on or before the start plus 12, 24 or 36 months.
US dollars needed = start rate / end rate - 1 (NUMBERS 8d, 8j); stricter reading = the rate falls 10% or more.
Episodes: the highest rate, then the lowest after it, inside a date span. k-day moves: k observations apart.
Conditional test: each start's percentile in its own trailing ten years, then its 24-month move. Volatility: standard
deviation of daily log changes times the square root of 250. May 2025 session figures use the CBC's Taipei closes
instead, since the H.10 rate is a New York noon rate (32.85 against the CBC's 32.768 on 6 Nov 2026).

Scripts and outputs (scratchpad, not the repo), run with `python3 -I`:
`/tmp/claude-0/-home-user/cdd961e4-901c-5589-a829-32f064718722/scratchpad/scripts/twd_windows.py` (windows, episodes,
k-day moves, today's level, conditional test, volatility; output `.../scratchpad/twd_windows_out.txt`),
`.../scratchpad/scripts/twd_extra.py` (CBC-close arithmetic, weak-side tails, conditional detail;
`.../scratchpad/twd_extra_out.txt`), `.../scratchpad/scripts/twd_level.py` (days at or below 10% stronger than
6 Nov 2026; `.../scratchpad/twd_level_out.txt`). Data copy: `.../scratchpad/data_dextaus/dextaus.csv` (md5
d5589cf3049ee4d1ef5c12eff5ad151c).

## Sources (APA 7; all accessed 13-14 Nov 2026, Sydney)

Already in `../REFERENCES_APA.md` (use those entries): #16 Board of Governors (n.d.-b), DEXTAUS (this card's download
14 Nov 2026, data to 6 Nov 2026); #141 Board of Governors (n.d.-c), EXTAUS; #612 CBC (n.d.), NT$/US$ closing rate.

New, read at the source (in full unless a section is named):
1. Central Bank of the Republic of China (Taiwan). (2025a, May 2). [Press release (114) No. 078 on the NT dollar's
   rise against the US dollar on 2 May 2025]. https://www.cbc.gov.tw/tw/cp-302-181423-cc30d-1.html
2. Central Bank of the Republic of China (Taiwan). (2025b, May 5). 近期新台幣匯市之說明 [Explanation of the recent
   NT dollar foreign exchange market] (Press release (114) No. 079). https://www.cbc.gov.tw/tw/cp-302-181429-e46a9-1.html
3. Central Bank of the Republic of China (Taiwan). (2025c). *NT$/US$ interbank closing rate, daily data, 2025* [Data
   set; source: Taipei Forex Inc.]. https://www.cbc.gov.tw/en/cp-4237-188473-44dc2-2.html
4. Central Bank of the Republic of China (Taiwan). (2025d, November 14). [Note on the joint statement of the US
   Department of the Treasury and the Central Bank on exchange rate policies]. https://www.cbc.gov.tw/tw/cp-302-187367-a2e5b-1.html
5. Central Bank of the Republic of China (Taiwan). (2026). *Financial stability report* (May 2026, Issue No. 20).
   https://www.cbc.gov.tw/dl-227541-0ffb1a8833524602881c95a69188e69a.html (sections on the NT dollar in 2025, life
   insurers and the FX valuation reserve read)
6. Financial Supervisory Commission. (2025a, May 29). [Insurance industry profit/loss and exchange gains/losses, April
   2025; press release, Chinese]. https://www.fsc.gov.tw/ch/home.jsp?dataserno=202505290005&dtable=News&id=96&mcustomize=news_view.jsp&parentpath=0%2C2
7. Financial Supervisory Commission. (2025b, June 26). *Profit/loss, net value and exchange gains/losses of the
   insurance industry in May 2025* [Press release]. https://www.fsc.gov.tw/en/home.jsp?dataserno=202506260005&dtable=News&id=54&mcustomize=multimessage_view.jsp&parentpath=0%2C2
8. Financial Supervisory Commission. (2025c, July 31). *Profit/loss, net value and exchange gains/losses of the
   insurance industry in June 2025* [Press release]. https://www.fsc.gov.tw/en/home.jsp?dataserno=202507310010&dtable=News&id=54&mcustomize=multimessage_view.jsp&parentpath=0%2C2
   (with the August, October and November 2025 releases: Insurance Bureau, 30 Sep 2025,
   https://www.ib.gov.tw/en/home.jsp?dataserno=202509300005&dtable=News&id=24&mcustomize=multimessage_view.jsp&parentpath=0,2 ;
   FSC, 27 Nov 2025, https://www.fsc.gov.tw/en/home.jsp?dataserno=202511270004&dtable=News&id=54&mcustomize=multimessage_view.jsp&parentpath=0%2C2 ;
   Insurance Bureau, 30 Dec 2025, https://www.ib.gov.tw/en/home.jsp?dataserno=202512300006&dtable=News&id=24&mcustomize=multimessage_view.jsp&parentpath=0,2)
9. Financial Supervisory Commission. (2025d, December 23). [Announcement proposing amendments to regulations on life
   insurers' foreign exchange risk and the accounting for unrealized foreign exchange differences; press release].
   https://www.fsc.gov.tw/en/home.jsp?dataserno=202601020001&dtable=News&id=54&mcustomize=multimessage_view.jsp&parentpath=0%2C2
10. Financial Supervisory Commission. (2025e, June 12). [Temporary measures for life insurers' foreign exchange risk;
    press release, Chinese]. https://www.fsc.gov.tw/ch/home.jsp?dataserno=202506120008&dtable=News&id=96&mcustomize=news_view.jsp&parentpath=0%2C2
11. Financial Supervisory Commission, Insurance Bureau. (2025, June 30). [Order on life insurers' released reserves,
    the FX valuation reserve and currency and duration mismatch plans; Chinese]. https://www.ib.gov.tw/ch/home.jsp?dataserno=202506300001&dtable=Law&id=35&mcustomize=multimessage_view.jsp&parentpath=0
12. Financial Supervisory Commission. (2026, February 12). 金管會修正外匯價格變動準備金應注意事項 [The FSC amends the
    rules on the foreign exchange valuation reserve; press release]. https://www.fsc.gov.tw/ch/home.jsp?id=96&parentpath=0,2&mcustomize=news_view.jsp&dataserno=202602120001&dtable=News
13. Shin, H. S., Wooldridge, P., & Xia, D. (2025, June 20). *US dollar's slide in April 2025: The role of FX hedging*
    (BIS Bulletin No. 105). Bank for International Settlements. https://www.bis.org/publications/bulletin-105-us-dollars-slide-april-2025-role-fx-hedging.pdf
14. U.S. Department of the Treasury. (2026a, January). *Macroeconomic and foreign exchange policies of major trading
    partners of the United States*. https://home.treasury.gov/system/files/136/January-2026-FX-Report.pdf (Taiwan
    section read)
15. U.S. Department of the Treasury. (2026b, July). *Macroeconomic and foreign exchange policies of major trading
    partners of the United States*. https://home.treasury.gov/system/files/206/July-2026-FX-Report.pdf (Taiwan section
    and Box 1 read)
16. U.S. Department of the Treasury & Central Bank of the Republic of China (Taiwan). (2025, November 14). *Statement of
    the U.S. Department of the Treasury and the Taiwan Central Bank on exchange rate policies* [Press release sb0316].
    https://home.treasury.gov/news/press-releases/sb0316

Secondary, search excerpts only (UNVERIFIED; for leads, not citation):
17. AM Best. (2025, May 9). [Comment on Taiwan life insurers and the NT dollar's appreciation]. https://news.ambest.com/pr/PressContent.aspx?altsrc=2&refnum=35994
18. Central News Agency. (2025a, May 5). [The governor's press conference on the NT dollar]. https://www.cna.com.tw/news/afe/202505050193.aspx
19. Central News Agency. (2025b, May 6). [FSC on insurers' hedging and the NT dollar]. https://www.cna.com.tw/news/afe/202505060336.aspx
20. Central News Agency. (2025c, June 11). [Life insurers and the FX valuation reserve]. https://www.cna.com.tw/news/afe/202506110040.aspx
21. cnyes. (2025). [The NT dollar's record one-day rise]. https://news.cnyes.com/news/id/5961088
22. DBS. (2025, May 13). [Taiwan insights: the NT dollar and life insurers' hedging]. https://www.dbs.com.sg/treasures/aics/templatedata/article/generic/data/en/GR/052025/250513_insights_taiwan.xml
23. Focus Taiwan. (2025, May 2). [The NT dollar's rise on 2 May 2025]. https://focustaiwan.tw/business/202505020013
24. Reuters. (2025, May 6). Taiwanese life insurers' portfolios have billions in unhedged dollars. https://www.reuters.com/world/asia-pacific/taiwanese-life-insurers-portfolios-have-billions-unhedged-dollars-2025-05-06
25. Taipei Times. (2025a, May 6). [Front-page report on the NT dollar's two-day surge]. https://www.taipeitimes.com/News/front/archives/2025/05/06/2003836391
26. Bloomberg. (2025, June 30). Taiwan's life insurers caught in dilemma with costly FX hedges. https://www.bloomberg.com/news/articles/2025-06-30/taiwan-s-life-insurers-caught-in-dilemma-with-costly-fx-hedges
