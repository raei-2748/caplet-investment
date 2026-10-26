# Rung 2 (deep): seven IPS insights, verified on the 22 Oct 2026 curve

Basis for all numbers: treasury.gov par curve 22 Oct (tsy_202610_22oct.csv), keel/scripts/ladder_pv.py adapted in lab/r2.py and r2b.py. Bootstrapped zero curve, ten $50k payments valued at 1 Jan 2027. All MODEL unless stated. Core: cost $298,861, headroom $1,139 (4bp), DV01 $296/bp, cost per $1 of promise 59.8c.

## Keepers

**1. A rate fall lands on the facility, never on the payments (1A #2, #3, #7).**
(a) VERIFIED, with a correction. 100bp fall adds $31.4k; 100bp rise saves $28.0k (1A said ~$29k). Falls hurt about 12% more than rises help. Headroom is $1.1k, so a one-day curve move (21 to 22 Oct: cost $293.9k to $298.9k, +$5.0k) is over four times the headroom. A January gap is a coin flip, not a forecast.
(b) The rule that matters is the order: payments are bought first, the 2028 deposit fills any gap, so the floor shrinks dollar for dollar. Payments are the one thing a fall cannot touch.
(c) Professor: "Short a rally" is a liability-matching truism, not insight; and you cannot call it "short" once the bonds are bought, because the position is then closed.
(d) HC, BAL, ASM. (e) Clause: "If yields fall before we buy, the facility floor shrinks dollar for dollar. The ten payments are bought first and never shrink."

**2. The promise costs 60 cents per dollar and needs only the curve's own yield (1A #26, #27, #40).**
(a) VERIFIED. $300k for $500k nominal; 59.8c at cost. IRR on $300k is 5.09%, at the 22 Oct cost 5.13%. Payment-weighted zero yields run 4.9% (2033) to 5.3% (2042), so this equals the curve by construction. It sits above the 10-year (4.96%) because the money runs 6 to 15 years.
(b) Answers "assumptions about returns" in one line: no forecast of ours is needed for the payments; stocks are never in the arithmetic.
(c) Professor: tautology; any bond earns its yield. Reply: the point is what is absent, no equity assumption.
(d) ASM, IS, CK. (e) Clause: "The payments need about 5.1% a year, which is what Treasuries pay today. We forecast no return to fund them."

**3. The gift is a floor plus a capped half share, and the cap binds in the common case (1A #10, corrected #11).**
(a) #11 FALSIFIED as framed. The cap is set from the 2031 fund, not 2028. The gift reaches the top whenever VT does not fall from 2031 to 2033: 76% (range_2031 README, MODEL). My check of "needs 7% for five years" only applies to a fixed $168k target, which is not the rule. #10 holds: gift = floor + half of 2031 fund, so a call spread on the fund.
(b) Implication: "the cap binds about 3 times in 4" is the honest statement about 2033 upside; the 2031 range top is the cap.
(c) Professor: Laura owns everything, so there is no "note"; the cap is a promise she chooses. Right; call it her rule, not a product.
(d) IS, CK, AR. (e) Clause: "The gift is the floor plus half the fund's 2031 value. Stocks falling after 2031 cut it; stocks rising after 2031 change nothing."

**4. The operating reserve exists from January 2027, and its rate exposure runs off (1A #18, #17).**
(a) VERIFIED. DV01 of the remaining payments: $296 (2027), $217 (2031), $161 (2033), $84 (2036), $27 (2039), $0 (2042). Reserve value at 1 Jan 2033 $399k.
(b) 2033 relabels, it buys nothing. Composition is 100% Treasuries throughout, shortening as payments pass. That is the official "reserve composition over time" ask answered directly.
(c) Professor: marked-to-market DV01 is irrelevant for hold-to-maturity assets. Agree: say the exposure that remains is coupon reinvestment ($11k per point, number sheet), also shrinking. The DV01 line is a sidebar.
(d) RES, ALLOC, PR. (e) Clause: "Our operating reserve is bought in 2027 and shortens by one payment a year. In 2033 it is renamed, not rebuilt."

**5. Cash-flow timing: five holdings mature before their payment (1A #21 corrected).**
(a) VERIFIED mapping: IBTM to IBTR mature 31 Dec, one day early. Feb-2037, May-2038 mature 320 and 231 days early; the three Nov bonds 47 days. 1A is right on the dates but wrong on the sign: early cash is not a "free carry". It earns bill rates (about 4.1 to 4.3%) below the bond yield (about 5%), so real cost is about $0.8k above the model, taking headroom to about $0.3k (1bp).
(b) Implication: expect a January gap with certainty, not half the time. State it.
(c) Professor: trivial dollars. True, but the headroom is trivial too, so it matters here.
(d) ASM (cash-flow timing is named in the ask). (e) Clause: "Holdings mature up to eleven months before their payment. The cash waits in Treasury bills, and we expect a small gap, covered in 2028."

**6. The two big risks seldom arrive together (L-04, tests the Lab's inferred claim).**
(a) PARTLY VERIFIED, US proxy only, HISTORY. Shortfall (yields fall 1pt for good) with costs over 3.5% a year quote-to-gift: 1871-2011 both 5.0% vs 6.8% if independent; 1954-2011 8.6% vs 16.3%. Weak in the long sample, strong post-war.
(b) Laura's kept half backs two risks that rarely strike together. Do not claim "never".
(c) Professor: 58 overlapping 15-year windows are about 4 independent samples; Taiwan costs are not in the data; 2022 showed inflation and bond losses together. Kill the claim if the team will not say "US history, not Taiwan".
(d) BAL, ASM. (e) Clause: "Laura's kept half backs two risks, falling yields and rising costs, that rarely arrived together in US history."

**7. "High degree of certainty" means one name and a stated residual (1A #22, #35 corrected).**
(a) The name is VERIFIED: every holding is a US Treasury or a Treasury ETF. But "one day, one name" is false as stated: coupon reinvestment is spread over a decade (shortfall about $21k for a lasting 2-point fall) and IBTM pays NAV, not par.
(b) Better: certainty is a US government claim plus two named residuals. This fits the locked "near-ironclad guarantee" and the 93 of 100 figure, and does not contradict it.
(c) Professor: Treasuries are not riskless; a sovereign claim is a credit and politics claim.
(d) HC (the official "define" ask). (e) Clause: "Certain means the US government pays. Two things can still move: coupon reinvestment, and the 2032 fund's payout, which is not par."

## Killed
- 1A #11 as written: wrong target (see 3).
- 1B #25 San Giorgio: history is real (Genoa 1407, creditors assigned specific customs revenues), but the IPS bans citations, the locked "dedicated instrument" line already does the job, and San Giorgio's ability to top up from taxes breaks the mapping. Costs words, adds nothing.
- 1A #35 "one day": see 7. Also the buy cannot happen on 1 Jan.
- 1B #11 damper: VT does not exist when the ladder is bought (2028), so it cannot offset the ladder's cost rise; wrong mechanism, and 2022 broke it anyway.
- 1A #39: last five rungs (2038 to 2042) hold 56% of DV01 against 50% of payments. Not "concentrated".

## Factual errors in rung 1
- 1A #3 "$29k" is $28.0k up / $31.4k down on 22 Oct.
- 1A #8 holiday is CORRECT: 1 Jan 2027 is a Friday, a US market holiday; earliest buy Mon 4 Jan. The model's 1 Jan price is approximate. 1 Jan 2033 is a Saturday; payments simply settle on the next business day, irrelevant to the plan.
- 1A #21 sign of carry (see 5).
- 1A #36 floor $140k vs $145k: the IPS needs one number.
- 1A #5 "half of paths" understated on 22 Oct (headroom about $0.3k to $1.1k).
- 1B #11, #25 as above.

Priority for the 500-word budget: 1, 4, 7 are rules or definitions the IPS must hold; 2 and 5 are single-sentence assumptions; 3 and 6 only if words remain.
