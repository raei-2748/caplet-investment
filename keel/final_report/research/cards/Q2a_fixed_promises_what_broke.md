# Q2a research cards: how fixed promises are made certain, and what broke when they failed (pensions, LDI, insurers' annuities)

**Date.** Thu 12 Nov 2026 (Sydney morning; Wed 11 Nov in the US). Web sources were read at the source that day
(WebFetch, Parallel web_fetch and web_search, Consensus); "accessed 12 Nov 2026" below means that day. Report parts 3a
(commitment and certainty), 3e (assumptions, limits, what to monitor; Table 3) and, for one row, 3d (words for
co-sponsors).

**Notes for the Final Report store, not report prose.** The IPS, the Trading Notes and the WInS book are frozen: a clash
is a risk to record, never a change. Every figure about Laura's plan is quoted from `../../NUMBERS.md` with its section
and is MODEL. Sums of register figures are marked "Keel arithmetic". This card is Q2's share on pension funds,
liability-matched books and insurers' annuity promises. It does not re-card Q15 (matching adjustment), Q17 or Q20
(escrow verifier, Leibowitz dedication, NY Regulation 126); store rows already holding a case are cited by id.

**Claims tested (each to keep, kill or change).**
1. "Every well-documented failure to pay a fixed nominal promise backed by high-grade bonds came from something Laura's
   plan does not have: leverage or collateral calls (UK LDI, Sept 2022), a counterparty's promise (Executive Life 1991
   and the structured settlements and pension annuities it carried; Baldwin-United 1983), reliance on reinvestment or
   duration matching instead of cash-flow matching (immunisation errors under non-parallel moves), or a sponsor that
   could stop paying in." Find at least one failure that DOES apply to Laura and size it against NUMBERS.
2. "Pension funds' own measure of certainty (funding ratio, hedge ratio, a 'flight path' to buy-out) is weaker than
   Laura's standard, because it counts expected returns or reinvestment."
3. "The 2022 LDI crisis is the clearest proof that the danger in a matched book is not the bonds but the financing
   around them."

**Problem class and the field that solved it.** Paying a fixed nominal schedule from a pool of assets is the defined
benefit pension and annuity-writer's problem (actuarial science, asset-liability management). Its certainty is solved in
three layers: the assets (cash-flow matching, called dedication; or duration matching, called immunisation), the
promiser's balance sheet (capital, sponsor covenant) and an outside backstop (PBGC, the UK Pension Protection Fund,
state guaranty associations, a central bank). Failures are studied by insurance regulators (GAO, state auditors, courts
in rehabilitation cases) and, for 2022, by central banks (Bank of England, IMF). Laura's plan has only the first layer,
so the asset test must carry the whole weight.

## Verdicts in one screen

- **Claim 1: CHANGE.** The failures read fall into five patterns, not four, and one named leg has no documented case.
  - Two patterns Laura's plan does not have:
    - leverage and collateral (UK LDI 2022: about £70bn of margin and collateral calls; Orange County 1994, store H3-085);
    - a counterparty's or related party's promise (Executive Life 1991: 44,000 pension retirees paid 70% for almost 13
      months; ELNY 2013: about 15% of structured settlement payees cut; Baldwin-United 1983: over $3bn of annuities cut
      from a 7.5% minimum to 5.5% after about 20% of reserves went into the parent's paper).
  - Three patterns Laura's plan carries in small form:
    - a payer-in who stops (Studebaker 1964; Central States, rescued by $35.8bn of taxpayer money in 2022);
    - reliance on reinvestment at a set rate (Japan's life insurers 1997-2001);
    - a payout that arrives late from a fund or broker (Reserve U.S. Government Fund 2008, redemptions suspended from
      17 Sep; Lehman's broker 2008, 110,000 accounts moved over ten days).
  - **Kill the immunisation leg as a "documented failure".** No failure of a fixed promise from duration-matching error
    under curve twists was found; the case for calling the ladder cash-flow matched stays, on design grounds.
  - **The failure that applies, sized (NUMBERS 5, 2).** A missed 2028 deposit leaves the 2033 payment $3,016 short at
    forward rates and the ten $57,455 short if interest earns nothing. A smaller deposit keeps the standard only down to a
    74.5% fall (56.4% after a 1-point fall in yields). The reinvestment gap of the ten as written ($54,595 at 0%) is
    closed only by the top-up bought from that deposit ($38,282 in January 2028), so the reinvestment failure and the
    deposit failure are one failure for Laura.
  - **A second, new one: a late fund payout.** $173,476 rides on one fund's end around 15 Dec 2032 (2033 payment
    $50,000, NUMBERS 8h; floor and moved half $123,476, NUMBERS 4; Keel arithmetic), against $10,775 of waiting cash on
    1 Jan 2033 (8h). Only the $50,000 is due on 1 January. Late, not lost, if the fund's Treasuries are good.
- **Claim 2: CHANGE.** Fair on the asset test, unfair as a whole. Pension measures do count on returns:
  - UK low dependency basis: gilts plus up to 0.5% a year;
  - US ERISA funding: corporate bond yields averaged over 24 months;
  - US public plans (GASB 67): the expected return, e.g. 7.00%.
  A pension-style "100% funded at market" on Laura's ten is $302,287 at forwards (NUMBERS 2, design A), short in 55.6%
  of 585 historical starting months. Laura's standard costs $336,656 and was short in none. But a pension has four
  things Laura lacks after January 2028: a sponsor who must fill deficits (UK Fast Track recovery plans up to six years),
  pooling, a lifeboat and a buy-out market. Restate: a pension needs less from its assets because it has more around them.
  Laura has nothing around hers, so she needs the stronger asset test. The lifeboats have limits too:
  - guaranty associations cap cover at $100,000 or $300,000;
  - PBGC's multiemployer fund was near insolvency in 2016;
  - a buy-out swaps the sponsor for an insurer (Executive Life).
- **Claim 3: KEEP, reworded.** "The danger in a matched book is not the bonds but the financing and the operations
  around them: collateral, the time it takes to move money between pots, and trades on dates you cannot choose."
  - Bank of England: 30-year gilt yields rose 160bp in a few days, more than twice the largest move since 2000; at least
    £50bn of forced sales against about £12bn of normal daily turnover.
  - The Bank bought £19.3bn of gilts.
  - Fire sales cost about 10% on the gilts sold, about half the price fall (Pinter et al.).
  - Raising cash took one to two weeks (IMF).
  - Laura has no leverage. Her only "calls" are dated trades she chose (Jan 2027, Jan 2028, the 2031 move, each draw on
    the Treasury-bill ETF) and payouts she waits for (iBond funds about 17 days before each 1 January).

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | In 2022 the UK's liability-matched pension books broke through their financing, not their gilts: the 30-year gilt yield "rose by 160 basis points in just a few days", a four-day move "more than twice as large as the largest move since 2000", and leveraged LDI funds could not meet the collateral calls | Cunliffe (2022a) | CERTAINTY, LADDER | KNOWN | Laura's ten are bought outright: no borrowing, no swaps, no repo (WInS bans margin and derivatives, `competition/COMPETITION.md` section 4). A yield jump moves her prices but calls no cash | Store H7-037 held this from secondary sources (Bank Underground, ACT wiki); this row moves it to the Bank's own letter | VERIFIED (Bank of England letter of 5 Oct 2022 read in full) | no | Bank of England, Deputy Governor's letter to the Treasury Committee |
| 2 | The spiral's size: market intelligence of at least £50bn of forced gilt sales against about £12bn of normal daily turnover; without the Bank, "a large number of pooled LDI funds would have been left with negative net asset value" and schemes' holdings in them "would be worth zero"; intraday range of 127bp on 28 Sep | Cunliffe (2022a) | CERTAINTY | KNOWN | Shows how a matched book reaches zero: only when it is borrowed against. Laura's cannot | "Worth zero" is what the Bank feared without action, not an outcome | VERIFIED (same letter) | no | Same letter |
| 3 | The fix was a buyer of last resort: the Bank bought £19.3bn of gilts (£12.1bn conventional, £7.2bn index-linked) from 28 Sep to 14 Oct 2022 | Cunliffe (2022b); Bank of England (2023) | CERTAINTY | KNOWN | The case gives Laura no outside money; her plan must never need a rescuer. It does not, barring a US default | The Bank's purchases were later sold back at a profit; not relevant to Laura | VERIFIED (18 Oct 2022 letter and the Bank's report on official market operations 2022-23 read) | no | Bank of England |
| 4 | The IMF's post-mortem: about £70bn of margin and collateral calls, £37bn of gilt sales, about 175 pooled LDI funds serving about 1,800 schemes; schemes needed one to two weeks and board approvals to raise cash; funds must now hold enough for a 250bp rise and deliver collateral within five days | Chen & Kemp (2023) | CERTAINTY, PROCESS | KNOWN | The time to move money mattered as much as the amount. For Laura: know how long each money move takes (an iBond fund's final payout, a broker transfer, the 2028 deposit) | IMF counts all sellers; Pinter et al. count LDI funds only (row 5), so the totals differ | VERIFIED (IMF Working Paper 2023/210 read in full) | no | IMF |
| 5 | Fire sales of safe assets: LDI funds sold £25.3bn of gilts and cut repo by £32.6bn; forced sellers took a discount of about 10%, about half the price fall; pooled funds sold more than single-client funds; UK life insurers "were able to manage collateral calls and avoid large forced sales" because their money was not split into segments; "capital can be slow moving internally" | Pinter, Siriwardane & Walker (2024) | CERTAINTY, RESERVE2033, PROCESS | NICHE | Laura's money also sits in pots: the ten and the top-up, the floor, the half kept. A rule that says which pot pays first is the unsegmented answer; the case already puts the reserve before the facility contribution (CANON A24) | Her pots have one owner and one adviser; the LDI delay came from trustees, managers and banks | VERIFIED (Bank of England Staff Working Paper 1,089 read in full; same paper as BIS Working Paper 1233) | no | Bank of England |
| 6 | The Work and Pensions Committee: UK schemes hedged about 85% of rate risk against about 50% in the Netherlands; DB assets fell about £400bn in 2022 while PPF-measured funding improved by over 20 points as liabilities fell faster; recapitalising LDI funds took "more than a week"; trustees saw data 1 to 25 days late; the new buffer is 250bp plus about 100bp of operational buffer | WPC (2023) | CERTAINTY, PROCESS | KNOWN | A hedge ratio is a measure of rate sensitivity, not a payment-by-payment match (store Q17-014, Q17-015). "85% hedged" with leverage was more fragile than an unlevered cash-flow match | The committee does not report any member who missed a pension payment; the loss was to hedges, growth assets and future funding | VERIFIED (HC 826 report read in full) | no | UK Parliament |
| 7 | Claim 3 reworded: in a matched book the danger is the financing and the operations around the bonds (collateral, time to move money, trades on dates you cannot choose), not the bonds | Rows 1-6 | CERTAINTY, PROCESS, MOVE2031 | KNOWN | Laura's only "calls" are dated trades she chose: January 2027 (the ten), January 2028 (the top-up $38,282, the floor and VT; NUMBERS 2, 4), the 2031 move of half of VT, and each draw on the Treasury-bill ETF. No lender can force any of them | Store H7-036 already says a dated sale out of shares acts like a scheduled margin call; this row adds the LDI evidence | VERIFIED (rows 1-6) | no | This card |
| 8 | Executive Life (California) failed in April 1991 after a $4bn policyholder run in 1990; junk bonds were 63% of its assets (its New York arm 64%); its 75,000 annuitants were paid 70% in conservation; four large failed insurers held nearly $85bn of business | GAO (1992a) | CERTAINTY, LAURA | KNOWN | The promise rested on one company's assets. Laura's rests on Treasuries she owns: "barring a US default, none of your 10 operating payments will depend on a share price, or on anybody else's money" (IPS) | Store H7-038 gave "a 30% cut" from a commercial site; this row verifies it at GAO | VERIFIED (GAO T-GGD-92-13 read in full) | no | GAO testimony |
| 9 | A pension buy-out moves the risk; it does not remove it: "the 44,000 retirees with Executive Life annuities received only 70 percent of their monthly annuities ... for almost 13 months"; PBGC's guarantee ceases once a plan buys annuities; 27 states capped guaranty cover at $100,000, most others at $300,000; about 1 in 6 annuities was above $100,000; DOL reviewed 1,109 plans that had bought them | GAO (1993) | CERTAINTY | NICHE | Where a pension is "stronger" through the buy-out market, it swaps a sponsor's promise for an insurer's. Laura never swaps her Treasuries for anyone's promise | Today's UK buy-out market is regulated more strictly (store Q7-026, Q15 for the matching adjustment) | VERIFIED (GAO HRD-93-29 read in full) | no | GAO report |
| 10 | Executive Life's final loss: assets $8.8bn at conservation (11 Apr 1991); policies revalued at about 78% under the 1993 plan; final recovery 86% (State Auditor) or 90% (Department of Insurance); loss $3.1bn or $936m by the two counts; junk bonds 55-60% of assets against 7-11% for the industry | California State Auditor (2008) | CERTAINTY | NICHE | Gives the size range if a judge asks "how bad was it" | The two counts disagree; quote both. Only the summary page was read, not the full report | VERIFIED (report summary page read in full) | no | California State Auditor |
| 11 | ELNY 2012-13: people paid fixed monthly sums under structured settlements took cuts when Executive Life of New York was liquidated; the court said about 15% of payees take reductions, "some by significant percentages" | Matter of Executive Life Ins. Co. of N.Y. (2013) | CERTAINTY, LAURA | NICHE | The closest real match to Laura's promise: fixed nominal payments for many years, funded by one insurer's bonds. Laura's are funded by Treasuries she holds | About 10,000 payees, cuts over $920m and cuts up to 59% come from Courthouse News, not the court: UNVERIFIED | VERIFIED (Appellate Division opinion, 103 A.D.3d 631, read in full) | no | New York courts |
| 12 | Baldwin-United 1983: over $3bn of single-premium deferred annuities promised at least 7.5% a year for years 2-10 (first-year rate about 14%); its insurers had "upstreamed" about 20% of reserves into the parent's and affiliates' paper; in rehabilitation, holders kept principal and interest to 13 Jul 1983, then 9.5% to 1 May 1984, then 5.5% to Nov 1987, two points under the minimum | In re Baldwin-United (1985); Matter of Baldwin-United (1985); Baldwin-United v. Garner (1984) | CERTAINTY | NICHE | A related-party leg claim 1 lacked: the assets behind the promise were lent to the promiser's own group. Laura's nearest analog is securities lending inside the iBond funds (store Q26-015: IBTM may lend up to a third of its assets) | Fund lending goes to third parties against collateral, not to the fund's parent; its risk sits inside the fund's NAV, which the plan already treats as not fixed (NUMBERS 3) | VERIFIED (607 F. Supp. 1312 read in full; 55 B.R. 885 and the Arkansas opinion read) | no | Court opinions |
| 13 | The brokers who sold Baldwin's annuities "as safe as a savings account" paid about $140m (5.5% of accumulated value) to settle | In re Baldwin-United (1985) | PRESENTATION, COSPONSOR | NICHE | A selling word that outran the structure cost money. Caplet's certainty words should point to a structure, not a feeling | Different seller and buyer; used only as a warning about words | VERIFIED (607 F. Supp. 1312) | risk: the TNA's "near-ironclad guarantee" (TNA note 1) is a selling word; the report names the structure instead (CANON C12) | Court opinion |
| 14 | Studebaker 1963-64: when the sponsor closed, about 3,600 retirees were paid in full, about 4,000 active workers got about 15%, and thousands of younger workers nothing | PBGC (2026) | COMPLETE2028, TWOREASONS, CERTAINTY | KNOWN | The payer-in stopped. Laura's 2028 deposit is her plan's only payer-in after January 2027 (store H2-013: the deposit acts as the plan's employer covenant) | Already in store H5-030, H4-067, H5-031; this row only adds the PBGC page read today | VERIFIED (PBGC page read in full) | no | PBGC |
| 15 | Central States: employers left without paying in full ("orphans"); the plan asked to cut benefits in 2015; Treasury refused in May 2016 (cuts not shown to avoid insolvency, not fairly spread, notices not understandable); it was projected to run out of money in 2025; $35.8bn of special financial assistance (taxpayer money) saved it in Dec 2022; without it, benefits would have fallen to PBGC levels, "roughly 60% below" the plan's | PBGC (2022); Lew (2016) | TWOREASONS, COMPLETE2028, CERTAINTY | KNOWN | When payers-in leave, only an outside rescuer saves the promise. The case gives Laura no outside money (case: portfolio-funded, no other flows), so her plan cannot count on one | A multiemployer plan counts on contributions for decades; Laura's last contribution is January 2028 | VERIFIED (PBGC press release 22-45 and the Treasury Secretary's letter read in full) | no | PBGC; US Treasury |
| 16 | Lifeboats are promises too: in 2016 Treasury warned that PBGC's multiemployer fund "may itself already be insolvent" by the time Central States failed; PBGC's guarantee is "subject to legal limits" (store H5-032) | Lew (2016); PBGC (2022) | CERTAINTY | KNOWN | One of the four things that make a pension "stronger" than Laura's plan was itself near failure | Congress did fund it in 2021; a rescue is a political choice, not a contract | VERIFIED (Treasury letter) | no | US Treasury |
| 17 | Japan's life insurers promised guaranteed rates that their assets later could not earn (the "negative spread"); seven failed in 1997-2001 and an eighth in 2008, at a public cost of ¥3,496bn, about 0.7% of GDP | Bernard & La Motte (2014), abstract | REINVEST, CERTAINTY | KNOWN | The reinvestment pattern: a promise that needs future money to earn a set rate. Laura's ten as written need coupons reinvested ($54,595 short if interest earns nothing, NUMBERS 2); the top-up closes it | Store H4-011, H5-072 (Nissan Mutual 1997) hold the case; the count and the cost here come from an abstract | UNVERIFIED (abstract only) | no | Consensus search |
| 18 | No documented failure of a fixed promise was found that came from immunisation error under non-parallel curve moves; theory says duration matching can fail when the curve twists, and one empirical test finds duration "a fairly good measure" of rate risk | Reitano (1996), abstract; Barber (2023), abstract; rows 1-17 | LADDER, CERTAINTY | NICHE | Drop the immunisation leg from claim 1 as history. Keep it as design: a cash-flow match (dedication) needs no rebalancing; duration matching does | Absence of evidence after a bounded search; the failures read came from leverage, counterparties, guaranteed rates or missing payers-in | UNVERIFIED (abstracts only; no failure case found) | risk: the TNA calls the ladder "duration-matching" (CANON C12) | Consensus search |
| 19 | A fund holding only government paper can still pay late: the Reserve U.S. Government Fund had redemptions suspended from 17 Sep 2008 by SEC order; it said it could not raise cash "without selling its assets at substantially diminished prices" and "cannot currently estimate when distributions will be made"; on 20 Nov 2008 the Treasury agreed to buy its assets so each holder would get $1 a share after a 45-day sale period | SEC (2008); The Reserve Fund (2008); U.S. Department of the Treasury (2008) | RESERVE2033, CERTAINTY, LADDER | NICHE | The failure that applies to Laura in form: money in a fund of Treasuries arrives late. Her 2033 payment depends on IBTM's final payout about 17 days before 1 Jan 2033 (NUMBERS 8h, 8m) | A money fund promised $1 on demand and faced a run after its sister fund broke the buck (Makhija, 2025); an iBond ETF has a set end date, trades on an exchange and promises no fixed amount. Three iBond Treasury funds have ended on schedule, Dec 2023, 2024 and 2025 (NUMBERS 8h) | VERIFIED (SEC order IC-28386, the fund's 485APOS filing, Treasury HP-1286 read in full); the first 40% paid from 13 Nov 2008 is UNVERIFIED (InvestmentNews) | risk: CANON C9 (a US default is not the only residual) | SEC; US Treasury |
| 20 | The size of Laura's one-fund exposure: on IBTM's end around 15 Dec 2032 ride the 2033 payment ($50,000, NUMBERS 8h), the floor payout ($103,178) and the moved half ($20,298) if it goes into IBTM; together $173,476, or $153,178 without the moved half (Keel arithmetic; the two facility parts are NUMBERS 4's "funds pay $123,476") (Lead, Thu 12 Nov: the $173,476 assumes the moved half goes into IBTM, which CANON A32 marks UNVERIFIED; say the floor's payout alone if the fund is not named) | NUMBERS 4, 8h; CANON A24, A32 | RESERVE2033, FLOOR, MOVE2031 | NICHE | Against it, the waiting cash in the Treasury-bill ETF on 1 Jan 2033 is $10,775 (NUMBERS 8h). Only the $50,000 is due that day; the facility money is not | The moved half's fund is not chosen (CANON A32: IBTM is the only late-2032 fund the repo knows) | VERIFIED (register figures; the sum is Keel arithmetic) | risk: CANON A32 (the moved half's holding is UNVERIFIED) | NUMBERS |
| 21 | A bridge sits inside the reserve: if IBTM paid late, the 2033 payment's gap after the waiting cash is $39,225 ($50,000 less $10,775, Keel arithmetic), less than the next rung (IBTO, own rung $47,545 on 1 Jan 2033, NUMBERS 8h), which could be sold and replaced when IBTM pays | NUMBERS 8h | RESERVE2033, PROCESS | NICHE | A liquidity answer from Laura's own holdings, with no lender: the LDI lesson (row 4) applied to her | Not in the IPS; it sells a later rung early at a market price (about one year of rate risk) and buys it back | VERIFIED (register figures; the bridge is Keel's reading) | risk: the IPS names only two reasons to change (CANON A34); a bridge must be framed as paying on time, never as a change of plan | This card |
| 22 | A broker's failure cost days, not money, where customer assets were kept apart: Lehman's broker-dealer customers (110,000 accounts, $92bn) were moved to solvent brokers "over the next ten days" from 19 Sep 2008 and all made whole; at MF Global $1.6bn of futures customers' money was not set aside, yet "all securities customers were satisfied early" | Harbeck (2013) | CERTAINTY, PROCESS | KNOWN | A failure at Laura's broker would most likely delay her Treasuries, not reduce them. SIPC covers $500,000 against holdings of $589,655 (store Q26-022, Q30-034) | Lehman's speed needed a court order and a buyer; a failure in late December could still delay a 1 January payment | VERIFIED (SIPC President's statement of 21 Nov 2013 read in full) | no | SIPC |
| 23 | Claim 1 restated as five patterns: (1) leverage and collateral; (2) a counterparty's or related party's promise; (3) a payer-in who stops; (4) reliance on reinvestment at a set rate; (5) a payout that arrives late from a fund or broker. Laura's plan has none of (1)-(2) and carries (3)-(5) in small, sized form | Rows 1-22; store H1-080, H2-039 (four ways promises failed), H3-085 (Orange County), H6-032 and H6-033 (AIG collateral), H7-039 (Lehman notes) | CERTAINTY, TWOREASONS | NICHE | A one-line map for 3e: which history Laura's plan avoids by design and which it carries, with a number for each | Store H1-080 and H2-039 have four patterns; this adds the fifth (delay) and splits counterparty from related party | VERIFIED (rows 1-22; store rows not re-read today) | no | This card |
| 24 | The failure that applies, sized: a missed 2028 deposit (nothing received by 31 March 2028) leaves $2,287 of the ladder unbought; with the longest rungs bought first, the 2033 payment is $3,016 short at forward rates; the ten are $57,455 short if interest earns nothing, and short in all 585 historical starting months | NUMBERS 5 | COMPLETE2028, TWOREASONS, REINVEST | KNOWN | The Studebaker and Central States pattern in small form. The IPS already names it as one of the two reasons to change | CANON D8 (the deposit is recession-sensitive), D9 (a smaller deposit is not a reason) | VERIFIED (register) | no | NUMBERS |
| 25 | A smaller deposit: the standard holds unless the deposit falls by more than 74.5% at today's yields (56.4% after a 1-point fall, 36.5% after 2 points); the ten stay paid at forward rates unless it falls by more than 98.4%; deposits of $10,000, $20,000 or $30,000 buy 21%, 49% or 77% of the top-up's backstop and leave the ten $42,718, $27,114 or $11,509 short if interest earns nothing | NUMBERS 5 | COMPLETE2028, REINVEST | KNOWN | Answers "how much of the payer-in does the plan need?" | Yields falling before January 2028 make it worse (the standard takes the whole $150,000 at a 3.60-point fall, NUMBERS 5) | VERIFIED (register) | no | NUMBERS |
| 26 | For Laura the reinvestment failure and the deposit failure are one failure: the ten as written are $54,595 short if interest earns nothing (NUMBERS 2), and only the top-up bought from the 2028 deposit ($38,282 in January 2028) closes that | NUMBERS 2, 5 | REINVEST, COMPLETE2028, CERTAINTY | NICHE | Until January 2028 Laura carries a Japan-style reinvestment risk in small form; after it she does not. The standard is as strong as the deposit until then | Interest on interest is 3% of the 2033 payment and about 15% of the 2041-42 payments (NUMBERS 8a): the risk sits in the late rungs | VERIFIED (register) | risk: the Trading Notes say "reinvested coupons fund the rest" (CANON A17, A18); true of the ten as written, so the report must say what closes it | NUMBERS |
| 27 | The UK regulator's low dependency basis: discount at gilts plus no more than 0.5% a year (Fast Track); be at least 100% funded on it by the relevant date; hedge at least 90% of rate and inflation risk; the margin is "a prudent estimate of the return" on the low dependency assets; "low dependency on the employer, not no dependency"; "Fast Track is not risk free" | TPR (n.d.-c); TPR (2024) | CERTAINTY | KNOWN | The UK's everyday top standard still counts on 0.5% a year above gilts and on the employer. Laura's counts on 0% after the top-up | Store H3-091 and Q7-022 to Q7-024 hold the basis; this row adds the Fast Track figures and quotes | VERIFIED (TPR pages read in full) | no | The Pensions Regulator |
| 28 | Pensions fill gaps over years: Fast Track recovery plans may run up to six years (three on or after the relevant date), paid by the employer | TPR (2024); TPR (n.d.-a) | COMPLETE2028, TWOREASONS | KNOWN | Laura is her own employer, and only until January 2028: one top-up, then no recovery plan | Store H2-013 | VERIFIED (TPR pages) | no | The Pensions Regulator |
| 29 | US measures count on spreads or expected returns: ERISA funding discounts at high-quality corporate bond yields, 24-month averages held inside a corridor around 25-year averages with a 5% floor; US public plans under GASB 67 discount at the long-term expected return (Orange County: 7.00%) | IRS (n.d.); GASB (n.d.); Segal (2026) | CERTAINTY, REINVEST | KNOWN | "Fully funded" here assumes the assets earn a corporate or an equity rate. Laura's test assumes they earn nothing | Store H7-007 (public pensions at expected returns), H9-034 (ASOP 4's low-default-risk measure, from a snippet) | VERIFIED (IRS segment rates page, GASB summary and the OCERS GASB 67 report read) | no | IRS; GASB; OCERS |
| 30 | The fair comparison in Laura's own numbers: a pension-style "100% funded at market" is the ten as written at forward rates, $302,287 (NUMBERS 2, design A), short in 55.6% of 585 historical starting months (median $1,592; worst $45,266, start Jul 2007); Laura's standard costs $336,656 and was short in none | NUMBERS 1, 2 | CERTAINTY, REINVEST, LADDER | NICHE | A like-for-like test: a 100% market funding ratio is not "paid even if interest earns nothing" | A pension adds a sponsor and a lifeboat to the market test; Laura has neither after January 2028 | VERIFIED (register) | no | NUMBERS |
| 31 | Gilts plus 0.5% applied to Laura's ten would value them about $15,000 below the curve cost (50bp at $300 a basis point, NUMBERS 1; linear, Keel arithmetic, not a register figure) | NUMBERS 1; TPR (n.d.-c) | CERTAINTY, REINVEST | NICHE | Sizes the return a UK low dependency measure counts on: about two-fifths of Laura's top-up ($38,282) | A linear estimate; ignores convexity; pension liabilities are longer and carry longevity | VERIFIED (inputs); the $15,000 is Keel arithmetic | no | This card |
| 32 | Where pensions are stronger: pooling of many members, a sponsor who must fill gaps, a lifeboat (PPF, PBGC) and a buy-out market (store Q7-026: UK buy-outs £49.1bn in 2023). Each has limits: guaranty cover $100,000 or $300,000 (GAO, 1993); PBGC "subject to legal limits"; the multiemployer fund near insolvency (row 16) | TPR; GAO (1993); Lew (2016) | CERTAINTY | KNOWN | Laura has none of the four after January 2028, so the asset test carries the whole weight. That is why her test is stronger than a pension's, not because pensions are careless | Pooling does not apply to fixed nominal payments with no longevity; the comparison is about funding, not mortality | VERIFIED (sources read; store rows not re-read) | no | This card |
| 33 | Naming: the ladder is cash-flow matched (dedication), not immunised; duration matching is a different technique that needs rebalancing; the instruments run 7.76 years against the payments' 9.94, $234 against $300 a basis point (NUMBERS 1) | NUMBERS 1; CANON C12 | LADDER, PRESENTATION | TEXTBOOK | Say it positively in 3a and 3e ("matched payment by payment"), never "not duration-matched" | Store Q17 rows (Leibowitz, Redington, Fisher and Weil) | VERIFIED (register) | risk: TNA "duration-matching" (CANON C12) | NUMBERS; CANON |

## (b) Cards

### Card 1. The UK LDI crisis of 2022: the financing broke, not the gilts (rows 1-7)
- **What is it?** UK defined benefit schemes hedged their liabilities with leveraged gilt funds (LDI), using repo and
  swaps. After the 23 Sep 2022 fiscal statement, 30-year gilt yields rose 160bp in a few days, more than twice the
  largest move since 2000. Collateral calls hit about £70bn (IMF). Funds sold gilts into a falling market: at least £50bn
  of forced sales against about £12bn of normal daily turnover (Bank). The Bank bought £19.3bn from 28 Sep to 14 Oct.
- **Did it work?** The hedges did their job on paper. Schemes' liabilities fell faster than their assets, and PPF-measured
  funding improved by over 20 points in 2022-23 (WPC). What failed was the money around the hedges. Schemes needed one to
  two weeks and board approvals to raise cash (IMF). Forced sellers lost about 10% on the gilts sold, about half the price
  fall (Pinter et al.). Life insurers, whose money sat on one balance sheet, met their calls without large forced sales.
- **How is Laura's case like it?** She also matches a fixed liability with long Treasuries. She also has dated money
  moves: the January 2028 top-up and floor purchase, the 2031 move of half of VT, each draw on the Treasury-bill ETF,
  and payouts she waits for (iBond funds about 17 days before each 1 January; NUMBERS 8h).
- **How is it not?** No leverage, no swaps, no repo, no collateral (WInS bans margin and derivatives). Nobody can call
  her cash. Her price risk matters only on days she chose to trade.
- **What Caplet takes.** 3e: the lesson in one line ("the danger is the financing and the timing, and this plan borrows
  nothing"). Table 3 or prose: the dated money moves, with when each happens. Number: 160bp in a few days, £19.3bn
  bought. Do not borrow the LDI story for drama; one sentence is enough.

### Card 2. Executive Life, ELNY and Baldwin-United: someone else's promise (rows 8-13)
- **What is it?** Three insurers that sold fixed payments. Executive Life (1991): junk bonds 63% of assets, a $4bn run,
  44,000 pension retirees paid 70% for almost 13 months, a final loss of $936m to $3.1bn. ELNY (2013): structured
  settlement payees, people paid fixed monthly sums, about 15% of them cut. Baldwin-United (1983): over $3bn of annuities
  promised 7.5% a year; about 20% of reserves had gone into the parent's paper; holders were cut to 5.5%.
- **Did it work?** No. The bonds behind the promises were weak or were lent to the promiser's own group. Buyers trusted
  a company, not a structure. The guaranty associations stepped in, but within limits ($100,000 or $300,000 a life).
- **How is Laura's case like it?** Fixed nominal payments over many years are the same promise. ELNY's structured
  settlements are the closest real match to Laura's ten.
- **How is it not?** Laura owns the Treasuries; no company stands between her and the US government. The IPS already
  says it: "barring a US default ... not ... on anybody else's money". The nearest trace of the risk is inside the iBond
  funds: they may lend part of their bonds (store Q26-015), and an iBond fund pays its net asset value, not a promise
  (NUMBERS 3).
- **What Caplet takes.** 3a: why "certainty" means owning the payer's bonds, not a company's promise. 3e: one line on
  fund lending and custody. Number: 70% for 13 months (GAO, 1993). Also, Baldwin's brokers paid about $140m for calling
  annuities "as safe as a savings account": the report's certainty words should point to the structure.

### Card 3. The payer-in who stops: Studebaker, Central States and Laura's 2028 deposit (rows 14-17, 24-26)
- **What is it?** Pensions fail when the money stops coming in. Studebaker (1964): about 4,000 active workers got about
  15%. Central States (2016-22): employers left, cuts were refused, and $35.8bn of taxpayer money saved it; without it,
  benefits would have fallen about 60%. Japan's life insurers (1997-2001) failed the other way: they needed their money
  to keep earning a promised rate.
- **Did it work?** Only with a rescuer. The PBGC lifeboat for multiemployer plans was itself near failure in 2016.
- **How is Laura's case like it?** This is the failure that applies. Laura's 2028 deposit is her plan's only payer-in
  after January 2027. It pays for the top-up, and the top-up is what closes the reinvestment gap. So for Laura the
  reinvestment failure and the payer-in failure are one failure. Sizes (NUMBERS 2, 5):
  - the ten as written are $54,595 short if interest earns nothing;
  - the top-up costs $38,282 in January 2028;
  - a missed deposit leaves the 2033 payment $3,016 short at forward rates and the ten $57,455 short at 0%;
  - the standard survives a deposit up to 74.5% smaller at today's yields (56.4% after a 1-point fall);
  - the ten stay paid at forward rates unless the deposit falls by more than 98.4%.
- **How is it not?** It is one payment, a year away, from Laura herself. It is not decades of contributions from
  employers who can leave. It is one of the IPS's two reasons to change, defined as nothing received by 31 March 2028.
- **What Caplet takes.** 3a and 3e: say once that the standard depends on the 2028 deposit until January 2028, with
  the 74.5% figure. 3e Table 3: the deposit row already exists. CANON D8 and D9 govern the wording.

### Card 4. A payout that arrives late: Reserve U.S. Government Fund and Lehman's customers (rows 19-22)
- **What is it?** In September 2008 a money fund holding only short-term government and agency paper had redemptions
  suspended by SEC order from 17 Sep. It could not raise cash "without selling its assets at substantially diminished
  prices". On 20 Nov the Treasury agreed to buy its assets so each holder would get $1 after a 45-day sale. The same
  month, Lehman's broker-dealer failed; 110,000 customer accounts ($92bn) were moved to solvent brokers over ten days,
  and all customers were made whole.
- **Did it work?** Holders of government paper were paid in the end, but late: for the fund, more than two months
  before a rescue plan; for Lehman's customers, days.
- **How is Laura's case like it?** Her 2033 payment depends on IBTM's final payout, about 17 days before 1 Jan 2033.
  On that one fund's end also ride the floor payout ($103,178) and, if the moved half goes there, $20,298 (NUMBERS 4).
  In all, $173,476 (Keel arithmetic), against $10,775 of waiting cash on 1 Jan 2033 (NUMBERS 8h). Her holdings also sit
  with one broker: SIPC covers $500,000 against $589,655 (store Q26-022).
- **How is it not?** An iBond ETF has a set end date and promises no fixed amount. It trades on an exchange, so a holder
  can sell before the end. Three iBond Treasury funds have ended on schedule (2023, 2024, 2025; NUMBERS 8h). Only the
  $50,000 is due on 1 January; the facility money is not.
- **What Caplet takes.** 3e: name "a late payout" as a limit, sized, and its answer in her own holdings: the gap after
  the waiting cash is $39,225, less than the next rung (IBTO, $47,545; NUMBERS 8h; Keel arithmetic). "Late, not lost."
  Monitoring (3e): IBTM's termination notice, expected mid-October 2032 (NUMBERS 8h). Never call it a third reason to
  change.

### Card 5. How a pension states certainty, and whether Laura's standard is fairly called stronger (rows 27-32)
- **What is it?**
  - UK: the regulator's low dependency basis discounts at gilts plus up to 0.5% a year, asks for 90% hedging and says
    "low dependency on the employer, not no dependency"; gaps are filled over up to six years.
  - US private plans: discount at corporate bond yields averaged over 24 months.
  - US public plans (GASB 67): discount at the expected return (Orange County: 7.00%).
- **Did it work?** For most schemes, yes, because a sponsor, pooling and a lifeboat stand behind the assets. Where those
  failed (Studebaker, Central States, Executive Life buy-outs), members lost money.
- **How is Laura's case like it?** Same question: how sure is a fixed schedule? Laura's ten at a pension-style "100%
  funded at market" cost $302,287 and would have run short in 55.6% of 585 historical starting months. Her standard
  costs $336,656 and was short in none (NUMBERS 2). Gilts plus 0.5% would value the ten about $15,000 lower (Keel
  arithmetic on NUMBERS 1).
- **How is it not?** A pension can lean on its sponsor for years and on a lifeboat after. Laura's sponsor is herself, and
  only until January 2028. She has no lifeboat and no outside money.
- **What Caplet takes.** 3a: "paid even if interest earns nothing, barring a US default" is stronger than a pension's
  test because nothing stands behind her assets, not because pensions are careless. One comparison number at most: the
  $302,287 against $336,656 pair, or the 0.5% a year the UK basis counts on. Exhibit: none needed.

## (c) Verdicts

**Claim 1: CHANGE.**
- What holds:
  - Leverage and collateral (LDI 2022, Orange County) are absent from Laura's plan.
  - Counterparty failure (Executive Life, ELNY) is absent too.
  - Each is verified at a primary source (rows 1-11).
- What changes:
  - (a) Add related-party assets as its own leg (Baldwin-United, row 12). The nearest trace in Laura's plan is fund
    securities lending, inside the fund's NAV.
  - (b) Kill "immunisation errors under non-parallel moves" as a documented failure (row 18). Keep the cash-flow-matched
    name on design grounds (row 33).
  - (c) Add a fifth pattern, delay at a fund or broker (rows 19-22).
- The failures that apply to Laura:
  - The payer-in: a missed or smaller 2028 deposit, $57,455 short at 0% if missed (NUMBERS 5).
  - Reinvestment: $54,595 at 0% before the top-up (NUMBERS 2). These two are one failure, because the deposit pays for
    the top-up.
  - A late payout: $173,476 on one fund's end around 15 Dec 2032, of which $50,000 is time-critical, against $10,775 of
    waiting cash (Keel arithmetic on NUMBERS 4, 8h).
- Reworded claim, for the store: "The documented failures of fixed promises backed by bonds came from borrowing against
  the bonds, from trusting someone else's promise or assets, from a payer-in who stopped, from needing money to keep
  earning a set rate, or from money arriving late. Laura's plan has none of the first two. It carries the last three in
  small, sized form."

**Claim 2: CHANGE.**
- The asset test is weaker in every pension measure read:
  - UK low dependency: gilts plus up to 0.5%;
  - US ERISA: corporate yields, averaged over 24 months, kept inside a corridor around 25-year averages;
  - US GASB 67: the expected return (7.00% for Orange County).
  Each counts on some return the assets must earn.
- The comparison is unfair if left there. Pensions put less weight on assets because they have a sponsor, pooling, a
  lifeboat and a buy-out market. Even the UK regulator says low dependency is "not no dependency".
- Fair version: "With nothing behind her assets after January 2028, Laura needs a stronger asset test than a pension
  does, and her plan has one." The lifeboats are not perfect either:
  - PBGC's guarantee is "subject to legal limits";
  - guaranty associations cap cover at $100,000 or $300,000;
  - the multiemployer fund was near insolvency in 2016;
  - buy-outs swap the sponsor for an insurer (Executive Life).
- Numbers for the report, if one is used:
  - $302,287 (pension-style market funding) against $336,656 (Laura's standard) (NUMBERS 2), short in 55.6% against 0%
    of 585 historical starting months;
  - or about $15,000 as the UK basis's 0.5% (Keel arithmetic, not a register figure; prefer the register pair).

**Claim 3: KEEP, reworded.**
- The Bank of England's own letters say a four-day move "more than twice as large as the largest move since 2000"
  triggered collateral calls and forced sales. Without the Bank, "a large number of pooled LDI funds would have been left
  with negative net asset value".
- The IMF and Pinter et al. size the calls (about £70bn), the sales (£37bn in all; £25.3bn by LDI funds) and the
  fire-sale discount (about 10%).
- The WPC shows funding levels improved overall: the bonds did their job; the money around them did not.
- Reworded: "the financing and the operations around them". Pinter et al. show that the time it takes money to move
  between pots was part of the damage.
- For Laura: no leverage, but dated money moves and payouts she waits for. Liquidity at payment dates is already built in
  (10 of 10 rungs pay before their payment, NUMBERS 8m). The one place to say more is the late payout (Card 4).

## (d) Gaps

- **Bank of England FSR, Dec 2022.** The chapter on LDI was not reached (two fetches stopped in sections 1-4).
  The Bank's own figures come from Cunliffe's two letters and the Bank's report on official market operations 2022-23.
- **ELNY.** The court opinion gives "about 15%" of payees cut. The figures of about 10,000 payees, cuts over $920m and
  cuts up to 59% come from Courthouse News only: UNVERIFIED. The liquidation plan itself was not read.
- **Reserve U.S. Government Fund.** When holders were finally paid in full is not verified. The first distribution
  of about 40% from 13 Nov 2008 is from InvestmentNews only: UNVERIFIED. The Primary Fund's 99.1 cents by Dec 2014 is
  from Makhija (2025) and is about the sister fund.
- **Japan.** Seven failures 1997-2001, an eighth in 2008, and the ¥3,496bn cost come from an abstract (Bernard & La Motte,
  2014): UNVERIFIED. The store rows H4-011 and H5-072 carry the Nissan Mutual case.
- **Immunisation.** No failure case found after a bounded search; the theory rows are abstracts only (Reitano, 1996;
  Barber, 2023). The claim "no documented failure" is an absence of evidence, not proof.
- **Central States.** Its 2014 funded ratio (53.1%) and the GAO's 2018 review come from search excerpts of CRS R44355
  and GAO-18-106, not read in full: not used in the table.
- **Sunburst Bank v. Executive Life (1994).** Read from excerpts only. Its "about 70%" for one class of claimants is not
  used; GAO (1993) carries the 70% figure.
- **The iBond fund's end.** IBTM's prospectus was not re-read today for what happens if the fund cannot sell or collect
  a holding before its end, or whether the end date can move. NUMBERS 3 and 8h, and CANON B11 and B20, hold what is
  verified. Read the termination wording before 3e quotes "late, not lost".
- **SIPC and the broker.** The Lehman and MF Global figures are from SIPC's President's statement (2013). The
  trustee's own reports were seen only as search excerpts.
- **TPR's 2023 LDI guidance** (store Q26-007) was not re-read today.
- **WPC on members.** The committee does not say whether any member missed a pension payment because of LDI; the card
  says "not reported", not "none".
- **REFERENCES_APA.md.** None of the sources below is in the register yet, except The Pensions Regulator's "Journey
  planning" (row 101), used here only through store rows. They need new entries. No entry found wrong.
- **Store rows cited by id** (H1-080, H2-039, H2-013, H3-085, H3-091, H4-011, H4-067, H5-030, H5-031, H5-032, H5-072,
  H6-032, H6-033, H7-007, H7-036, H7-037, H7-038, H7-039, H9-034, Q7-022 to Q7-026, Q17-014, Q17-015, Q26-015, Q26-022,
  Q30-034) were not re-read today beyond the by-tag summaries.

## Sources (APA 7; all accessed 12 Nov 2026)

Read at the source:
- Bank of England. (2022). *Financial stability report: December 2022*.
  https://www.bankofengland.co.uk/financial-stability-report/2022/december-2022 (sections 1-4 only; see Gaps)
- Bank of England. (2023). *Report on the Bank's official market operations 2022-23*.
  https://www.bankofengland.co.uk/-/media/boe/files/sterling-monetary-framework/report-on-the-banks-official-market-operations-2022-23.pdf
- Baldwin-United Corp. v. Garner, 283 Ark. 385, 678 S.W.2d 754 (1984).
  https://law.justia.com/cases/arkansas/supreme-court/1984/84-162-0.html
- California State Auditor. (2008, January). *Department of Insurance: Former Executive Life Insurance Company
  policyholders have incurred significant economic losses, and distributions of funds have been inconsistently
  monitored and reported* (Report 2005-115.2). https://information.auditor.ca.gov/reports/summary/2005-115.2
- Chen, R., & Kemp, E. (2023). *Putting out the NBFire: Lessons from the UK's liability-driven investment (LDI) crisis*
  (IMF Working Paper No. 2023/210). International Monetary Fund.
  https://www.imf.org/-/media/files/publications/wp/2023/english/wpiea2023210-print-pdf.pdf
- Cunliffe, J. (2022a, October 5). [Letter to Mel Stride, Chair of the Treasury Committee, on the Bank's gilt market
  operations]. Bank of England.
  https://www.bankofengland.co.uk/-/media/boe/files/letter/2022/october/letter-from-jon-cunliffe-ldi-5-october-2022
  (also https://committees.parliament.uk/publications/30136/documents/174584/default)
- Cunliffe, J. (2022b, October 18). [Letter to Mel Stride, Chair of the Treasury Committee, on LDI]. Bank of England.
  https://www.bankofengland.co.uk/-/media/boe/files/letter/2022/october/letter-from-jon-cunliffe-ldi-18-october-2022.pdf
- Governmental Accounting Standards Board. (n.d.). *Summary: Statement No. 67*. Retrieved November 12, 2026, from
  https://www.gasb.org/page/pronouncement?isStaticPage=true&pageId=%2Fstandards-and-guidance%2Fpronouncements%2Fsummary-statement-no-67.html
- Harbeck, S. P. (2013, November 21). *Statement to the House Financial Services Committee, Subcommittee on Capital
  Markets and Government Sponsored Enterprises*. Securities Investor Protection Corporation.
  https://www.sipc.org/media/testimony/hhrg-113-ba16-wstate-sharbeck-20131121.pdf
- House of Commons Work and Pensions Committee. (2023). *Defined benefit pensions with liability driven investments*
  (HC 826). https://publications.parliament.uk/pa/cm5803/cmselect/cmworpen/826/report.html
- In re Baldwin-United Corp. (Single Premium Deferred Annuities Insurance Litigation), 607 F. Supp. 1312 (S.D.N.Y. 1985).
  https://law.justia.com/cases/federal/district-courts/FSupp/607/1312/2372187/
- Internal Revenue Service. (n.d.). *Pension plan funding segment rates*. Retrieved November 12, 2026, from
  https://www.irs.gov/retirement-plans/pension-plan-funding-segment-rates
- Lew, J. J. (2016, May 6). [Letter to the chairs and ranking members of the Senate Finance and HELP Committees and the
  House Ways and Means and Education and the Workforce Committees on the Central States application]. U.S. Department of
  the Treasury. https://home.treasury.gov/system/files/131/MPRA-SecLew-Letter-to-Congress-050616.pdf
- Makhija, A. (2025). United States: Reserve Primary Fund suspension, 2008. *Journal of Financial Crises, 7*(2),
  227-256. https://doi.org/10.17132/2693-3179.1655
- Matter of Baldwin-United Corp., 55 B.R. 885 (Bankr. S.D. Ohio 1985).
  https://openjurist.org/55/br/885/matter-of-baldwin-united-corp-1543573
- Matter of Executive Life Ins. Co. of N.Y., 103 A.D.3d 631 (N.Y. App. Div. 2013).
  https://www.nycourts.gov/reporter/3dseries/2013/2013_00738.htm
- Segal. (2026). *Orange County Employees Retirement System: GASB 67 actuarial valuation as of December 31, 2025*.
  Orange County Employees Retirement System.
  https://www.ocers.org/sites/main/files/file-attachments/a-3c_ocers_december_31_2025_gasb_67_report.pdf
- Pension Benefit Guaranty Corporation. (2026, June 24). *PBGC, pensions, and Studebaker*.
  https://www.pbgc.gov/about/pbgc-pensions-studebaker
- Pension Benefit Guaranty Corporation. (2022, December 8). *PBGC approves SFA application for Central States plan*
  (Press Release No. 22-45). https://www.pbgc.gov/news/press/pr22-45
- Pinter, G., Siriwardane, E., & Walker, D. (2024). *Fire sales of safe assets* (Staff Working Paper No. 1,089). Bank of
  England. https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2024/fire-sales-of-safe-assets.pdf (also BIS
  Working Paper No. 1233, https://www.bis.org/publ/work1233.pdf)
- The Pensions Regulator. (n.d.-c). *Low dependency funding basis*. Retrieved November 12, 2026, from
  https://www.thepensionsregulator.gov.uk/document-library/code-of-practice/funding-and-investment/funding-defined-benefits/long-term-planning/low-dependency-funding-basis
- The Pensions Regulator. (2024, November 20). *Fast Track submission tests and conditions*.
  https://www.thepensionsregulator.gov.uk/document-library/scheme-management-detailed-guidance/funding-and-investment-detailed-guidance/fast-track-submission-tests-and-conditions
- The Pensions Regulator. (n.d.-a). *The funding regime*. Retrieved November 12, 2026, from
  https://www.thepensionsregulator.gov.uk/en/document-library/code-of-practice/funding-and-investment/funding-defined-benefits/the-funding-regime
- The Reserve Fund. (2008). [Post-effective amendment to registration statement, Form 485APOS]. U.S. Securities and
  Exchange Commission. https://www.sec.gov/Archives/edgar/data/83335/000110465908067301/a08-15773_1485apos.htm
- U.S. Department of the Treasury. (2008, November 20). *Treasury enters into agreement to assist the Reserve Fund's US
  Government money market fund* (Press Release HP-1286). https://home.treasury.gov/news/press-releases/hp1286
- U.S. General Accounting Office. (1992a). *Insurance regulation: The failures of four large life insurers*
  (GAO/T-GGD-92-13). https://www.gao.gov/assets/t-ggd-92-13.pdf
- U.S. General Accounting Office. (1993). *Private pensions: Protections for retirees' insurance annuities can be
  strengthened* (GAO/HRD-93-29). https://www.gao.gov/assets/hrd-93-29.pdf
- U.S. Securities and Exchange Commission. (2008). *Order temporarily suspending redemption of investment company shares
  and postponing payment for investment company shares which have been submitted for redemption for which
  payment has not been made* (Investment Company Act Release No. 28386). https://www.sec.gov/files/rules/ic/2008/ic-28386.pdf

Not read in full (UNVERIFIED where used):
- Barber, J. R. (2023). Empirical test of multiple-liability immunization conditions. *The Journal of Fixed Income, 33*(2), 111–127.
  https://doi.org/10.3905/jfi.2023.1.168 Abstract seen through Consensus:
  https://consensus.app/papers/details/w:05f1d578-9e15-4a29-afaa-d6213fb04a9b/
- Filip, I. (2012, April 18). *Insurance cuts leave some livid*. Courthouse News Service. https://www.courthousenews.com/insurance-cuts-leave-some-livid
  (secondary; ELNY figures)
- Bloomberg. (2008, November 14). The Reserve begins $4.5B distribution of fund. *InvestmentNews*.
  https://www.investmentnews.com/mutual-funds/the-reserve-begins-45b-distribution-of-fund/18608 (secondary)
- Reitano, R. R. (1996). Non-parallel yield curve shifts and stochastic immunization. *The Journal of Portfolio
  Management, 22*(2), 71–78. https://doi.org/10.3905/jpm.1996.71 Abstract seen through Consensus:
  https://consensus.app/papers/details/w:300c5d6c-1387-4b14-9bb2-e188c8f0f4f1/
- Bernard, R., & La Motte, L. (2014, May). *Défaillances dans le secteur de l'assurance vie au Japon dans les décennies
  1990 et 2000* (Analyse et synthèse No. 30). Autorité de contrôle prudentiel et de résolution, Banque de France.
  https://acpr.banque-france.fr/system/files/import/acpr/medias/documents/20140526-defaillances-dans-secteur-assurance-vie-japon-decennies-1990-et-2000.pdf
  Abstract seen through Consensus:
  https://consensus.app/papers/details/w:1ac589e2-7339-4404-a0dd-936e054f653e/
- Sunburst Bank v. Executive Life Ins. Co., 24 Cal. App. 4th 1156 (1994).
  https://law.justia.com/cases/california/court-of-appeal/4th/24/1156.html (excerpts only)
- Sidor, G., & Topoleski, J. J. (2016, January 28). *Benefit reductions in the Central States multiemployer DB pension
  plan: Frequently asked questions* (CRS Report No. R44355). Congressional Research Service.
  https://www.congress.gov/crs-product/R44355 ; and U.S. Government Accountability Office. (2018, June 4). *Central
  States Pension Fund: Investment policy decisions and challenges facing the plan* (GAO-18-106).
  https://www.gao.gov/products/gao-18-106 . On Central States: search excerpts only.
