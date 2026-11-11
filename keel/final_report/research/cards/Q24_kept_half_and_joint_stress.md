# Q24 research cards: the kept half, the joint stress of rates and shares, and Exhibit 3's scenario matrix

**Date.** Tue 10 Nov 2026 (Sydney), Mon 9 Nov in the US. Web sources were read at the source that day (Parallel
web_search and web_fetch); "accessed 10 Nov 2026" below means that day. Report part 3b (the contribution and
flexibility) and Exhibit 3.

**Notes for the Final Report store, not report prose.** The IPS, the Trading Notes and the WInS book are frozen: a clash
is a risk to record, never a change. Every Keel figure is MODEL, re-derived on the register's engine by
`../../numbers/joint_stress.py` (results in `../../numbers/results_joint_stress.json`, about 3 seconds to run). The
script imports `engine.py` and `plan.py` unchanged and first reproduces the register: floor $115,929, top $138,735,
kept half $23,986, stated bottom $110,000, corrected stated top $130,000, overflow $36,859 nominal ($27,939 in Jan 2033
money), payments short in 6.0% of 585 windows (1-in-20 $1,225, worst $12,117 from Jul 2007), and the 4.1%, 2.6% and
2.5% deductions of NUMBERS 3. The case is cited as "case l.N" (line of the .txt).

**Claims tested.**
1. "A recession lowers rates and shares together, so the kept half and the reserve's overflow shrink together; the
   house model, which treats them as independent, hides this." (bond desk, weakness 4)
2. "The kept half is a designed contingency with a purpose and order of use, a size at 2031 and 2033, and a release
   rule." (co-sponsor judge, weakness 3; IPS l.15; CANON A31, D12)
3. "'Responsible' can be given a test: the kept half covers a 10% stronger Taiwan dollar on the gift in 19 of 20
   paths." (bond desk, weakness 4)
4. Liquidity: when each payment's cash arrives, that every holding can be sold on any trading day, when the gift is
   cash, and where the kept half sits. (bond desk, weakness 5; case l.127 names "liquidity")

**Problem class.** Wrong-way risk between two cushions (asset-liability management under a regime-dependent stock-bond
correlation); owner's contingency and management reserve in building projects (cost engineering, construction
contracts, grant terms); currency exposure of a fixed-dollar gift; operational liquidity of a dedicated Treasury book.

**Method of the joint replay (MODEL).** One window per monthly start from Jan 1962 to Sep 2010 (the 585 windows of
NUMBERS 2). The start month stands for 1 Jan 2027. Rates: the 1-year Treasury yield's path applied in proportion to the
6 Nov 2026 forward rates, capped at 3 times (NUMBERS 2's method). Shares: US stocks with dividends (Shiller, the series
`plan.py` reads) from the same calendar months, so VT is bought at start + 12 months (Jan 2028), half moved at
start + 48 (Jan 2031), the kept half valued at start + 72 (Jan 2033). The floor's yield is the forward times the
rate ratio in Jan 2028, the moved half's the forward times the ratio in Jan 2031; the margin bought in Jan 2028 is
re-priced at the ladder's own yield. Keel's call throughout (margin $21,149). Stated bottom = floor x 0.959 rounded
down to $5,000; stated top = floor x 0.959 + moved half x 0.975 rounded down (NUMBERS 4, correction under review).
"Overflow" = each rung's money above $50,000 on its payment date, valued on 1 Jan 2033 on the 6 Nov forwards.
Independent benchmark: all 585 x 585 pairings of rate windows with share windows (same history, link removed).

## Verdicts in one screen

1. **CHANGE.** The link is real since 2000 and reversed before it. Annual US stock returns against the change in the
   1-year yield: -0.31 for 1962-1999, +0.22 for 2000-2022 (house model 0). In the joint replay the two cushions do
   shrink together when shares end below their 2028 cost (11% of windows). Then the overflow's median is $15,624,
   against $28,190 otherwise and $27,100 if rates and shares were unrelated. Kept half and overflow together have a
   median of $31,112 in those windows, against $42,352 with no link. The whole-sample effect is modest: both are in
   their bottom fifth together in 5.1% of windows against 4.5% unlinked. Those windows are two clusters, starts in mid
   1998 to mid 2000 and in late 2005 to 2006 (the dot-com and 2008 crashes). The house model does not "hide" the range
   or the kept half: it is harsher on both than the joint history. What it cannot show is the overflow, which it
   does not model (NUMBERS 7). The payments do not fail more often when shares fall (4.5% of those windows against
   6.2%). The worst payment windows, the 2007-2008 starts, bought VT near the 2009 low.
2. **CHANGE to a rule.** As IPS l.15 stands, the kept half has a purpose but no order, size, confidence or release.
   The three-line rule in section (c) gives it all four without sizing a contingency fund (case l.106-107). The GAO
   and building-contract sources are the prior art.
3. **CHANGE the wording.** "19 of 20" holds on history (96.5% of windows since 1871; 97.4% in the joint replay) but
   not in the house model, where it holds in 93.0% of paths (1 in 14 fails, median gap $1,590). The kept half covers
   a 9.4% stronger Taiwan dollar in 19 of 20 house paths. Against the real Taiwan dollar from 1983 (417 windows, same
   months' shares) it covered the actual two-year move in 97.1% of windows. If the surplus above the stated top joins
   the kept half (the panel's cap rule), the test passes in 99.97% of house paths.
4. **KEEP, with two corrections.** The ETFs are exchange-listed (IBTM and the other iBond funds on Nasdaq, VT on NYSE
   Arca). The T-bonds are not "listed": they trade in a dealer market, around the clock on weekdays, closed on
   SIFMA's bond-market holidays (Columbus Day and Veterans Day included, when stock exchanges are open). The gift is
   cash in mid-December 2032. IBTM terminates "on or about December 15, 2032". IBTF, the 2025 fund, stopped trading
   on 15 Dec 2025 and paid on 18 Dec.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | The joint replay runs on the register's own engine and reproduces it: floor $115,929, top $138,735, kept half $23,986, stated range $110,000-$130,000, overflow $27,939 (Jan 2033 money), payments short in 6.0% of windows, worst $12,117 (Jul 2007) | `numbers/joint_stress.py` checks; NUMBERS 2, 3, 4, 8h | CERTAINTY, OTHER | NICHE | Every figure below is comparable with the register | Overlapping monthly windows: about four rate eras, not 585 independent trials (NUMBERS 7) | VERIFIED (script output against NUMBERS) | no | This run |
| 2 | In the data the plan uses, US stock returns and changes in the 1-year yield moved together only after 2000. Annual (Jan to Jan) correlation: -0.09 (1962-2022), -0.31 (1962-1999), +0.22 (2000-2022). Monthly: -0.10, -0.22, +0.29. Over the plan's own windows, shares 2028-2031 against the rate change 2028-2031: +0.35. House model: 0 by assumption | Keel arithmetic on FRED DGS1 (repo copy) and Shiller monthly (repo mirror); `results_joint_stress.json` correlation_data | REINVEST, HALFKEPT, CERTAINTY | NICHE | Names the correlation assumption in 3e with a number: the house model's 0 sits between the two regimes | Positive here means shares and yields fall together (the recession case). 61 annual points; the sign depends on the era | VERIFIED (computed) | risk: the IPS's career-as-shares argument assumes the post-2000 regime | This run |
| 3 | The academic version: the bond-stock return correlation "was positive on average before 2001:Q2 but negative afterward", because inflation and output moved apart before (stagflation) and together after | Campbell, Pflueger and Viceira (2020), JPE 128(8) (S9) | REINVEST, INFLATION_TWD, CERTAINTY | KNOWN | Treasuries counterbalance a slump in the post-2001 regime; in a 1970s-style regime they do not | Store H3-104 has Campbell, Sunderam and Viceira (2017) on the same point; this is the JPE paper with the break date | VERIFIED (journal PDF read) | risk: as row 2 | Parallel search and HBS PDF |
| 4 | A practitioner measure of the same switch: US stock-bond return correlation +0.35 (1970-1999) and -0.29 (2000-2023), monthly returns; "a shift in level or even the sign of the correlation between stocks and bonds can last for decades" | Molenaar, Senechal, Swinkels and Wang (2024), Financial Analysts Journal 80(3) (S10) | REINVEST, CERTAINTY | KNOWN | Same sign switch as row 2 from a different data set; a 3e assumption can cite it | Return correlation has the opposite sign to the stock-yield correlation in row 2 | VERIFIED (article page read) | no | Parallel fetch of tandfonline |
| 5 | Joint replay, all 585 windows: overflow 1-in-20 / median / 1-in-20 high $779 / $27,100 / $70,181; kept half $15,432 / $26,944 / $47,253; kept half plus overflow $22,547 / $58,064 / $98,587; stated bottom $90,000 / $110,000 / $130,000; stated top $110,000 / $135,000 / $160,000; completion in Jan 2028 $18,404 / $24,559 / $31,205 | `results_joint_stress.json` joint | HALFKEPT, RESERVE2033, FLOOR, CEILING | NICHE | The joint history's distribution for Exhibit 3 and 3e | Rates at the start of a window are today's forwards by construction | VERIFIED (computed) | no | This run |
| 6 | When VT ends below its 2028 cost (11.3% of windows), the overflow's median is $15,624 against $28,190 when it ends above; with rates and shares unlinked it would be $27,100 either way. Kept half plus overflow: median $31,112 against $42,352 unlinked | As row 5; independent_pairs | HALFKEPT, RESERVE2033, REINVEST | NICHE | The bond desk's point, sized: in bad share years the second cushion is about $11,000 thinner than independence would say | Driven by the 1998-2000 and 2005-2007 starts | VERIFIED (computed) | risk: the two unpromised cushions are partly pro-cyclical | This run |
| 7 | Both cushions in their own bottom fifth at once (kept half under $18,759, overflow under $12,488): 5.1% of windows (30) against 4.5% unlinked. The 30 starts are Jun 1998 to Jul 2000 and Aug 2005 to Dec 2006, so VT was bought just before the 2000-2002 or the 2007-2009 crash and the 1-year yield then collapsed | As row 5 | HALFKEPT, RESERVE2033 | NICHE | One named storm, two episodes; a 3e sentence can name them | Small excess over independence across the whole sample; large inside those two clusters | VERIFIED (computed) | risk: as row 6 | This run |
| 8 | Kept half plus overflow under $25,000: 7.0% of joint windows against 4.6% unlinked; its 1-in-20 low is $22,547 joint against $25,582 unlinked | As row 5 | HALFKEPT, RESERVE2033 | NICHE | The joint tail is about $3,000 lower, not a collapse | Same caveat as row 1 | VERIFIED (computed) | no | This run |
| 9 | The payments do not fail more when shares fall: a shortfall in 4.5% of windows where VT ended below cost (worst $5,750) against 6.2% where it ended above (worst $12,117). The worst rate windows (2007-2008 starts) bought VT in 2008-2009, near the low | As row 5 | CERTAINTY, REINVEST | NICHE | The ten payments' risk is a rates risk; the shares' bad years and the ladder's bad years only partly overlap | Timing luck in one episode; a slower recovery would change it | VERIFIED (computed) | no | This run |
| 10 | By era of start. 2000-2010 (129 windows): payments short in 27.1% (1-in-20 $10,531, worst $12,117); overflow median $13,885 (1-in-20 $0); kept half median $20,804; both together 1-in-20 $17,734; stated range median $95,000-$120,000. 1962-1979 (216): no shortfall, overflow median $48,142. 1980-1999 (240): no shortfall, overflow median $16,388 | `results_joint_stress.json` by_era_of_start | CERTAINTY, REINVEST, HALFKEPT, FLOOR | NICHE | If the post-2000 regime is the one Laura lives in, the whole picture is about a quarter worse than the all-history medians | 129 overlapping windows cover about one rate cycle | VERIFIED (computed) | risk: "barring a US default, none of your 10 operating payments will depend on a share price" holds; a small shortfall in about a quarter of post-2000 windows is a rate risk the margin covers only to 3 points | This run |
| 11 | The house model is not kinder than the joint history on the range or the kept half: stated bottom 1-in-20 $85,000 (joint $90,000), stated top $105,000 ($110,000), kept half $12,150 ($15,432). Independence flatters only what the house model leaves out, the overflow | `results_joint_stress.json` house vs joint; NUMBERS 7 | HALFKEPT, FLOOR, CEILING | NICHE | 3e can say exactly which number the independence assumption affects | The house model's 17.88% volatility is above US history's, which offsets the missing link | VERIFIED (computed) | no | This run |
| 12 | Jul 2007 start (worst for the payments): payments $12,117 short, overflow $0, completion $31,562, stated range $90,000-$105,000, kept half $23,368 (VT bought Jul 2008, then +13% and +31%) | As row 5, named | CERTAINTY, FLOOR, HALFKEPT | NICHE | The named recession row for Exhibit 3: it hits the payments and the range, not the kept half | One window | VERIFIED (computed) | no | This run |
| 13 | Jun 2006 start (worst for both cushions together): VT bought Jun 2007, down 23% to Jun 2010; overflow $9, kept half $16,237, payments $5,006 short, stated range $105,000-$120,000 | As row 5, named | HALFKEPT, RESERVE2033 | NICHE | The case the bond desk described, and its size | One window | VERIFIED (computed) | risk: as row 6 | This run |
| 14 | Jan 2000 start (VT bought Jan 2001, down 11% to 2004): payments full, overflow $4,691, kept half $16,980, stated range $100,000-$115,000 | As row 5, named | HALFKEPT, FLOOR, CEILING | NICHE | A second recession row | One window | VERIFIED (computed) | no | This run |
| 15 | Worst kept half, Mar 2003 start: $12,361 (VT bought Mar 2004, down 44% from Mar 2007 to Mar 2009), but the overflow is $75,313 because the 1-year yield rose from about 1.2% to 5% (ratio capped at 3x) | As row 5, worst_kept | HALFKEPT, RESERVE2033 | NICHE | The cushions can offset as well as coincide | The proportional mapping magnifies moves that start from very low rates (row 2's s.d. note) | VERIFIED (computed) | no | This run |
| 16 | The lowest stated range comes from rates falling before Jan 2028: Dec 2007 start gives a floor bought at 0.15 x the forward yield, stated $80,000-$100,000 (payments $10,263 short, kept half $34,635) | As row 5, lowest_bottom | FLOOR, CEILING | NICHE | Confirms the bond desk's "January 2028 curve as the single most important thing to watch" | One window | VERIFIED (computed) | no | This run |
| 17 | The deductions depend on the yield. Measured on each window's path: the floor's payout fell more than 4.1% below its locked value in 1 window (-4.3%, Mar 2004 start) and the moved half more than 2.5% below in 23 (worst -5.6%, Oct 2003 start, 2031 yields at 3x today's). After rounding down to $5,000, the realised gift was above the stated bottom in all 585 and above the stated top in all 585 (by at least $664) | `results_joint_stress.json` joint deductions | FLOOR, CEILING, CERTAINTY | NICHE | NUMBERS 3's "in every rate world short of a default" is true after rounding, not for the percentages alone | Proportional mapping: 3x today's yields means about 13-14% | VERIFIED (computed) | risk: register wording only; the deduction should scale with the yield on the purchase day | This run |
| 18 | The realised gift sits above the stated top in every window: by $3,978 / $7,804 / $11,922 (1-in-20 / median / 1-in-20 high). Without a cap rule the gift is never inside the stated range; with one (contribution = stated top, any excess to the kept half) it is inside in 100% | As row 17 | CEILING, HALFKEPT, COSPONSOR | NICHE | Hard evidence for the co-sponsor judge's weakness 1 and CANON D12's definition | The cap rule is under review (NUMBERS 4) | VERIFIED (computed) | risk: needs the D12 definition in 3c; the IPS is silent on a cap | This run |
| 19 | Inflation world (yields up 3 points in a straight line by 2031, shares 0% 2028-2033, US prices and Taiwan building costs 5% a year): payments full, overflow $50,769, stated range $115,000-$135,000, kept half $16,930, gift $143,301. That is $106,933 in 2027 dollars (against $120,334 central) and NT$3.50m of 2027 Taiwan building (NT$3.81m central). The ten payments are worth $302,509 in 2027 dollars (against $390,686 at 2.4%). With shares down 20% first: kept half $13,544, top $130,000 | `results_joint_stress.json` scenarios | INFLATION_TWD, CERTAINTY, HALFKEPT | NICHE | The inflation row for Exhibit 3: the dollars are safe, what they buy is not | Stylised; 5% for six years is above every 16-year US window since 1984 (Q10) | VERIFIED (computed) | no (CANON C15: the TNA's "nonexistent inflation risk" is about funding the payments, which holds) | This run |
| 20 | Inflation-era history: Jan 1973 start gives overflow $51,610, stated range $120,000-$140,000, kept half $22,062; Jan 1979 gives overflow $28,837, kept half $33,475, stated range $115,000-$140,000 | As row 5, named | INFLATION_TWD, RESERVE2033 | NICHE | Rising rates help a hold-to-date ladder and the floor; the cost shows only in real terms (row 19) | Proportional mapping from 1970s rate levels | VERIFIED (computed) | no | This run |
| 21 | Rates 3 points lower for good from Jan 2027 (the world Keel's margin is sized for), shares 7.5%: payments exactly met, overflow $0, completion $32,534, stated range $85,000-$105,000, kept half $22,446 | `results_joint_stress.json` scenarios minus3 | CERTAINTY, FLOOR | NICHE | The design row for Exhibit 3 | Parallel shift | VERIFIED (computed) | no | This run |
| 22 | The Taiwan dollar test: does the kept half cover the extra dollars a 10% stronger Taiwan dollar needs on the announced contribution (floor + moved half)? House 93.0% of paths (fails 1 in 14, median gap $1,590); history since 1871 96.5%; joint replay 97.4%. Stricter reading (rate falls 10%, so 11.1% more dollars): 88.4%, 94.9%, 93.8%. The largest move covered in 19 of 20: 9.4% (house), 11.0% (history) | `results_joint_stress.json` twd_test | INFLATION_TWD, HALFKEPT | NICHE | Gives "responsible" a stated confidence, as GAO asks for contingency (row 27) | The house figure uses the model gift; the joint figure the realised gift | VERIFIED (computed) | no | This run |
| 23 | With the real Taiwan dollar (Fed H.10 monthly, Oct 1983 on) and the same months' US shares, rates at forwards (417 windows, VT bought Oct 1983 to Jun 2018): the two-year move from the meetings to the gift ran -12.7% / +0.1% / +13.7% in dollars needed (1-in-20 each side); 10% or more against Laura in 11.0% of windows; the kept half covered the actual move in 97.1%; worst uncovered gap $10,048 (VT bought Nov 1983, the 1986-1988 appreciation). Correlation of the currency move with shares: +0.09 | `results_joint_stress.json` twd_test real_twd; `keel/models/data/twd_per_usd_monthly.csv` | INFLATION_TWD, HALFKEPT | NICHE | The test on the real currency, not an assumed 10% | The FX file is a mirror, UNVERIFIED against FRED (`keel/models/data/SOURCES.md`); shares are US, not world | VERIFIED (computed); data UNVERIFIED at source | no | This run |
| 24 | If the panel's cap rule is adopted, the pot behind the announcement is the kept half plus the surplus above the stated top (a Treasury surplus, median $7,860 house). Pot: $19,295 / $31,727 / $55,242 (house, 1-in-20 / median / 1-in-20 high). It covers a 10% stronger Taiwan dollar in 99.97% of house paths, a 13% overrun allowance in 99.2% (history 98.9%) and 17% in 91.3% (95.1%). The kept half alone covers 13% in 77.9% (86.0%) and 17% in 51.4% (60.6%) | `results_joint_stress.json` twd_test cap_rule | HALFKEPT, INFLATION_TWD, CEILING | NICHE | The cap rule both makes "inside the range" true and puts about a quarter of the cushion in Treasuries, which answers part of the pro-cyclicality | Overrun shares are illustrations against Q5's early-stage norms (13%-17%), never a cost estimate (case l.164-165) | VERIFIED (computed) | risk: as row 18 | This run |
| 25 | The gift in other money. Central $138,735 = NT$4.55m in 2033 at today's 32.768; NT$4.13m if the Taiwan dollar is 10% stronger; NT$3.82m at its ten-year strongest (27.52). In 2027 US dollars: $120,334 at 2.4% ($123,920 at 1.9%, $112,861 at 3.5%). In Jan 2027 Taiwan building: NT$3.81m at 3% (NT$4.16m at 1.5%, NT$3.39m at 5%). Stated $110,000-$130,000: NT$3.60m-4.26m; $95,410-$112,757 in 2027 dollars; NT$3.02m-3.57m of 2027 building | `results_joint_stress.json` gift_terms; NUMBERS 8d inputs (`inflation_inputs.json`) | INFLATION_TWD, COSPONSOR | KNOWN | The stack reader's weakness 5 paragraph, in one line of numbers | 8d deflates building costs from Sep 2026 (6.17 years) and uses $135,000 as the top; this uses 1 Jan 2027 (6 years) and the corrected $130,000 | VERIFIED (computed) | no | This run |
| 26 | The kept half's size. On the day of the 2031 meetings it equals the moved half: central $20,780; house $12,153 / $20,652 / $35,032; history $13,928 / $22,147 / $34,366. On 1 Jan 2033: central $23,986; house $12,150 / $23,831 / $46,746; joint replay $15,432 / $26,944 / $47,253. As a share of the contribution: 9% / 17% / 31% (house) | `results_joint_stress.json` kept_half_on_meeting_day_2031; NUMBERS 8f | HALFKEPT, COSPONSOR | KNOWN | The size line of the rule: known to the dollar on the meeting day, so it can be named to co-sponsors | An outcome, not a target: the case does not ask teams to size a contingency fund (case l.106-107) | VERIFIED (computed) | no | This run |
| 27 | GAO's cost guide separates contingency ("funds held at or above the government program office for 'unknown unknowns'") from management reserve ("'known unknowns' ... managed at the contractor level"); "Contingency funds should be retained by management until specific needs are realized"; "The amount of contingency should be based on the level of confidence with which management chooses to fund a program"; "no specific confidence level is considered a best practice"; for a high-risk program "70 or 80 percent" | U.S. GAO (2020), GAO-20-195G, ch. 1 note 5, ch. 12 "Cost Contingency" and "Allocation" (S1) | HALFKEPT, CERTAINTY | KNOWN | The kept half is held at the owner's level (Laura), spent only on realised needs, and stated with a confidence (rows 22-24) | Federal acquisition programs, not a private gift; GAO notes "other organizations may use the terms differently" (AACE's naming is the reverse, Q5 row 6) | VERIFIED (PDF read) | no | Parallel search and fetch of the GAO PDF |
| 28 | Owners keep their own contingency apart from the builder's: "Each project should include an owner's, contractor's, and designer's contingency"; "Contingency funds are to be used, first, to complete the scope or deal with unknown conditions. Many owners make the mistake of adding scope with their contingency"; "Any remaining contingency is the owner's, not the contractor's"; contracts should require "periodic reviews of the contingency ... and provide information regarding the release of the contingency back to the owner"; "It makes little to no sense for the contractor to hold more contingency than is required by the current level of risk". Utah State Capitol owner's contingency 6% (3% scope, 2% risk, 1% politics) | Hart (2023), AIA, "Managing the contingency allowance" (S2) | HALFKEPT | KNOWN | Order of use (the builder's contingency first, the owner's after, never for new scope) and release as risk falls | Q5 row 27 cited this page for its 5%-10% figure only; the order and release lines are new here | VERIFIED (page read) | no | Parallel fetch of aia.org |
| 29 | Public owners write it into the contract. A state's AIA A133: "The Owner and CMAR contractor Contingencies shall be the property of the Owner ... Any unused Contingency remaining at the completion of the Project shall be returned to the Owner" (4% owner, 1% contractor). A county exhibit: an "Owner's Contingency ... for the Owner's exclusive use. Monies from the Owner's Contingency may be spent in the discretion of the Owner." A university GMP: the construction contingency "is not intended to fund additional scope"; what remains at final payment "shall be counted as Savings" | State of Louisiana (2025), A133 as modified (S3); Cobb County exhibit (2022) (S4); Princeton University (2025) GMP model (S5) | HALFKEPT, COSPONSOR | NICHE | Release date (completion) and destination (back to the owner) for the kept half; "at the owner's discretion" matches "promised to no one" | Public construction contracts; Laura is a donor, not the building's owner, unless her role says otherwise | VERIFIED (search excerpts of the contract PDFs themselves) | no | Parallel search |
| 30 | Funders write the same rule for unspent gifts: "Any Grant Funds that have not been used for, or committed to, the Project upon expiration or termination of this Agreement must be returned promptly to the Foundation, applied to another Foundation-funded project ..., or applied to another mutually-agreed upon charitable purpose, as directed in writing by the Foundation" | Bill & Melinda Gates Foundation (2026), sample terms and conditions (S6) | HALFKEPT, COSPONSOR, FUNDRAISING | KNOWN | The giver decides where unused money goes, in writing. For Laura the kept half was never given, so its default destination is her own flexibility (case l.102-103) | Grantor-grantee terms; Laura holds the money herself | VERIFIED (search excerpt of the PDF itself) | no | Parallel search |
| 31 | Set in Stone (more than 700 US arts building projects, 1994-2008): "More than 80 percent of the projects studied ran over budget, some by as much as 200 percent"; museums "over only by about 46 percent" | Woronkowicz et al. (2012) and the University of Chicago release (S7) | HALFKEPT | KNOWN | Already in the store (H9-095, H8-147, H7-086); checked again, not repeated | US, mostly large buildings | VERIFIED (release read; report text via search excerpt) | no | Parallel search |
| 32 | Taiwan's public works revise budgets as a matter of course: of 255 PCC-tracked plans in nine ministries (FY2016 to Mar 2020), 165 (64.71%) were revised, 125 of them in budget; "only a few" cut cost or time; 19 moved budget by more than 40%. Ministry of Culture: 18 of 24 plans revised (75.00%). The Taichung opera house went from NT$2.411bn to NT$4.3604bn (+80.86%) and from 2003-2007 to 2003-2016 in 5 revisions; Weiwuying from NT$8.36bn to NT$10.7545bn in 6 | Legislative Yuan Budget Center (2020), evaluation of the FY2019 central government final accounts audit report, item 41 (S8) | HALFKEPT, INFLATION_TWD | NICHE | Taiwan's own record for the "building costs that overrun" use; fills Q9's gap (Taichung's total budget was not found there) | Large public projects; reasons include arbitration and design changes, not only prices | VERIFIED (PDF read, Chinese) | no | Parallel search and fetch of ly.gov.tw |
| 33 | IBTM is "a term fund that will terminate on or about December 15, 2032, at which time it will distribute its remaining net assets to shareholders pursuant to a plan of liquidation"; listed on Nasdaq; after termination it "will no longer be listed or traded". The 2025 Treasury fund: last trading and final NAV 15 Dec 2025, liquidation 18 Dec 2025; holders "will receive their proceeds ... on or around the listed liquidation date, based on their brokerage's processes" | iShares (2026) summary prospectus and fund page (S11); BlackRock (2025) release (S12); Q16 rows 1, 6, 7 | RESERVE2033, FLOOR, CERTAINTY | KNOWN | The gift (floor and moved half, both in the late-2032 fund) is cash about 18 Dec 2032, two weeks before 1 Jan 2033 | Q16 already verified three terminations; this row re-reads the 2026 prospectus and the 2025 release | VERIFIED (prospectus, fund page, release read) | no | Parallel search and fetch |
| 34 | Where the money can be sold. VT trades on NYSE Arca (fact sheet, 30 Sep 2026). US Treasuries trade in "a multiple-dealer over-the-counter market. Trading takes place around the clock during the week", "the deepest and most liquid market in the world". SIFMA recommends full closes for "U.S. dollar-denominated government securities" on its holidays, including Columbus Day (12 Oct 2026) and Veterans Day (11 Nov 2026), when stock exchanges are open | Vanguard (2026) VT fact sheet (S13); Adrian, Fleming and Nikolaou (2025), NY Fed SR 1146 (S14); IAWG (2024) (S15); SIFMA holiday schedule and release (S16) | RESERVE2033, CERTAINTY, TWOREASONS | KNOWN | The liquidity line: every holding can be sold on any normal business day; the plan never needs to (IPS: two reasons to change) | "Listed Treasury" is wrong for the five T-bonds; WInS lists them, exchanges do not | VERIFIED (pages read) | risk: wording; say "traded every business day", not "listed" | Parallel search |
| 35 | When each payment's cash arrives (engine dates): the five iBond rungs about 15 Dec of the year before (half a month early); the Feb-2037 bond 10.5 months early; the May-2038 bond 7.6 months; the three November bonds 1.5 months. The floor and the moved half: about 15-18 Dec 2032. The kept half: in VT, promised to no one, sellable any exchange day | `results_joint_stress.json` liquidity_cash_dates; NUMBERS 8h; Q16 | RESERVE2033, HALFKEPT | KNOWN | The four facts the bond desk asked for, in one table row | Treasury pays on the next business day when a date falls on a weekend or holiday (Q16 row 12) | VERIFIED (engine and sources above) | no | This run |

## (b) Cards: the six strongest ideas

### Card 1. Two cushions in one storm, sized (rows 5-10, 13)
- **What is it?** The plan has two pots nobody is promised: the kept half (shares) and the ladder's overflow (the margin
  handed back when rates hold). A joint replay feeds both the same months of US history.
- **Did it work?** Yes, as a measurement. When shares end below their 2028 cost, the overflow's median halves ($15,624
  against $28,190). With no link it would be $27,100. Together the two pots are about $11,000 thinner in those years
  ($31,112 against $42,352). The worst window for both, a Jun 2006 start, leaves $16,246 in all.
- **How is Laura's case like it?** The IPS's own fear is a recession in which "shares fall and co-sponsors cut their
  budgets". The joint tail is exactly two such episodes, 2000-2002 and 2007-2009.
- **How is it not?** Across all of history the effect is small (bottom fifth together 5.1% against 4.5%). Before 2000
  rates rose in bad share years, and then the overflow grew. The payments themselves are not hit harder (row 9).
- **What Caplet takes:** One sentence in 3e and one row in Exhibit 3. In the years shares fall since 2000, both spare
  pots shrink at once, by about a third against independence. The promised money is untouched, because it is
  Treasuries.

### Card 2. The correlation flips by era (rows 2-4, 10)
- **What is it?** US stocks and Treasury yields have fallen together since about 2001 and moved apart before. Campbell,
  Pflueger and Viceira date the break at 2001:Q2. Molenaar et al. measure +0.35 (1970-1999) and -0.29 (2000-2023) for
  returns. The plan's own data give -0.31 and +0.22 for stocks against yield changes.
- **Did it work?** The post-2000 regime made Treasuries a hedge for shares, which is the premise of the IPS's opening
  ("your portfolio should be a counterbalance").
- **How is Laura's case like it?** Her career income behaves like shares, so in the post-2000 regime the Treasuries
  pay when her income and shares fall.
- **How is it not?** In a 1970s regime, rates rise with inflation while shares fall. Then the ladder and the floor do
  better (rows 19-20), but the dollars buy less and the kept half still shrinks.
- **What Caplet takes:** Name the assumption in 3e: "the house model sets the link at zero; history since 2000 runs
  about +0.2 to +0.3, before it about -0.2 to -0.3; the joint replay shows what each does". This is better than
  either claim alone.

### Card 3. The owner's contingency: held back, used last, returned at completion (rows 27-29)
- **What is it?** GAO: contingency is held above the project office "until specific needs are realized" and sized to
  a stated confidence. AIA: owner, contractor and designer each hold a contingency, which is used "first, to complete
  the scope", never to add scope, and released back to the owner as risk falls. Public A133 contracts: unused
  contingency "shall be returned to the Owner" at completion. An owner's contingency is "for the Owner's exclusive
  use".
- **Did it work?** It is the standard form in US public building contracts (three owners read). Q5 records the sizes
  (13%-17% at an early stage).
- **How is Laura's case like it?** "Promised to no one" is the owner's-contingency idea. The builder sees only the
  announced amount (D12), and Laura decides any call.
- **How is it not?** Laura is a donor and co-founder, not necessarily the building's owner. Her pot is in shares, not
  cash.
- **What Caplet takes:** Name it "Laura's own reserve above the gift" (in AIA's terms an owner's contingency) and take
  three lines from these sources: used only after the builder's contingency, never for new scope, released at
  completion back to Laura.

### Card 4. The Taiwan dollar test, on the real currency (rows 22-23, 25)
- **What is it?** The bond desk's test of "responsible": does the kept half cover a 10% stronger Taiwan dollar on the
  announced contribution?
- **Did it work?** Mostly. On US history the kept half covers it in 96.5% of windows and in the joint replay in
  97.4%, but in the house model only in 93.0%. On the actual Taiwan dollar since 1983 the kept half covered the real
  two-year move in 97.1% of windows. The one large failure was the 1986-1988 appreciation ($10,048 short).
- **How is Laura's case like it?** The facility is paid in Taiwan dollars. A 10% move on about $139,000 is about
  $13,900, close to the kept half's 1-in-20 size.
- **How is it not?** The currency is only one of three named uses. Covering it uses most of the pot in a bad year,
  and the uses can arrive together.
- **What Caplet takes:** State it as a confidence, not a guarantee. The kept half covers a 10% stronger Taiwan dollar
  in about 93 to 97 of 100 cases, and in 97 of 100 on the real currency since 1983. If the cap rule is adopted, the
  figure is 99.97 of 100.

### Card 5. The gift is above the stated top in every window (rows 17-18, 24)
- **What is it?** The deductions (4.1% floor, 2.5% moved half, then rounding down) that make the stated bottom safe
  also put the realised gift above the stated top in all 585 windows. The median gap is $7,804.
- **Did it work?** For the bottom, yes: it was never breached. The percentages alone are breached at high yields
  (floor -4.3% once; moved half up to -5.6% in 23 windows), and only the rounding absorbs that.
- **How is Laura's case like it?** It is what the co-sponsor judge called "a range of choice presented as a range of
  uncertainty".
- **How is it not?** It is a framing question, not a money one: the money is there either way.
- **What Caplet takes:** Adopt the D12 definition with the cap rule. The contribution is the stated top; anything above
  it joins Laura's own reserve. "Inside the range" is then true in every window. The reserve gains about $7,800 of
  Treasury money, which makes it less pro-cyclical. Change NUMBERS 3's wording so the deduction scales with the
  purchase-day yield.

### Card 6. Taiwan revises its public building budgets as a matter of course (row 32)
- **What is it?** The Legislative Yuan's budget office looked at 255 PCC-tracked plans (FY2016 to Mar 2020). It found
  165 revised (64.71%), 125 of them in budget and almost never downward. The Ministry of Culture revised 75% of its
  plans. The Taichung opera house rose 80.86% (NT$2.411bn to NT$4.3604bn) over five revisions.
- **Did it work?** Both opera houses opened, years late and over budget, and the Control Yuan censured Weiwuying
  (Q9 row 26).
- **How is Laura's case like it?** The kept half's first named use, "building costs that overrun", is the normal
  case in Taiwan's public building.
- **How is it not?** These are large state projects; a small residency is simpler. The case bars a cost estimate.
- **What Caplet takes:** One Taiwan fact for 3b beside Set in Stone. Two in three Taiwan public works plans changed
  their budgets, and the Taichung opera house cost 81% more than first approved. That is why half the shares stay
  unpromised.

## (c) Verdicts, the scenario matrix and the rule

**Claim 1: CHANGE.** Replace "the house model hides this" with two sentences. Since 2000, the years shares fall are
years rates fall, so the two spare pots shrink together: about $11,000 less between them than if rates and shares
were unrelated (median $31,112 against $42,352 when VT ends below its cost). Before 2000 the link ran the other way.
The promised money (the payments, the bottom and, after 2031, the top) is Treasuries and does not move with shares.
Report the correlation assumption in 3e (rows 2-4).

**Claim 2: CHANGE to the rule below.** It keeps IPS l.15's three uses and order-free wording intact as the purpose. It
adds an order, a size stated as an outcome with a confidence (not a sized fund, case l.106-107), and a release, all
inside CANON D12.

**Claim 3: CHANGE the wording.** "In 19 of 20" is true on history and false in the house model. Say: the kept half
covers a 10% stronger Taiwan dollar on the announced contribution in about 93 (model) to 97 (history) of 100 cases;
on the real Taiwan dollar since 1983, 97 of 100. When it fails, it falls short by about $1,600 at the median. With the
cap rule, 99.97 of 100.

**Claim 4: KEEP with corrections.** Rows 33-35. Replace "listed Treasury" with "Treasury bonds that trade every
business day, and ETFs listed on Nasdaq (iBonds) and NYSE Arca (VT)".

### Exhibit 3 candidate: the scenario matrix (MODEL; Keel's call; 6 Nov 2026 curve)

| World | Ten payments | Overflow (Jan 2033 money) | Stated bottom | Stated top | Gift paid (Dec 2032) | Kept half, 1 Jan 2033 |
|---|---|---|---|---|---|---|
| Today's forwards, shares 7.5% a year | full | $27,939 | $110,000 | $130,000 | $138,735 | $23,986 |
| Rates 3 points lower for good, shares 7.5% | full (exactly) | $0 | $85,000 | $105,000 | $113,695 | $22,446 |
| Recession replay, start Jul 2007 (worst for the payments) | $12,117 short (2.4%) | $0 | $90,000 | $105,000 | $112,764 | $23,368 |
| Recession replay, start Jun 2006 (worst for both spare pots) | $5,006 short | $9 | $105,000 | $120,000 | $123,892 | $16,237 |
| Recession replay, start Jan 2000 | full | $4,691 | $100,000 | $115,000 | $121,672 | $16,980 |
| Inflation world: yields +3 points by 2031, shares flat, prices 5% a year | full | $50,769 | $115,000 | $135,000 | $143,301 ($106,933 in 2027 dollars) | $16,930 |
| Inflation replay, start Jan 1973 | full | $51,610 | $120,000 | $140,000 | $149,103 | $22,062 |
| Joint history, 1-in-20 low / median (585 windows) | 94% full; 1-in-20 $1,225 short | $779 / $27,100 | $90,000 / $110,000 | $110,000 / $135,000 | | $15,432 / $26,944 |
| House model, 1-in-20 low / median | (not modelled) | (not modelled) | $85,000 / $110,000 | $105,000 / $130,000 | | $12,150 / $23,831 |

Reading for 3b and 3e: the payments fail only when rates fall more than the margin covers, and then by at most 2.4%.
The range moves with rates in January 2028 and with shares until the 2031 move. The kept half moves with shares. The
inflation world is the one that costs real money: everything is paid, and it buys about a tenth less.

### The kept-half rule (notes, three lines, each sourced; coherent with IPS l.15 and CANON D12)

1. **Purpose and order of use.** The kept half is Laura's own reserve above her announced contribution, outside it
   (D12). She calls it only for the three uses IPS l.15 names, and only after whatever stands in front of each is
   spent. First, a stronger Taiwan dollar between the 2031 announcement and the December 2032 payment: nothing
   stands in front of it, and it is measured on the day. Second, building costs that overrun, after the builder's
   own contingency, and never for added scope. Last, a co-sponsor falling short, as a bridge or a capped share.
   Each call is a new decision, announced as Laura's own gift.
   *Sources:* AACE keeps currency and escalation apart from contingency (Q5 row 7). AIA: contingency is used "first,
   to complete the scope", and "Many owners make the mistake of adding scope with their contingency" (row 28). GSA:
   scope changes are not paid from contingency (Q5 row 25). The cost-overrun facility is called last, after the
   contingency and the contractor (store H4-033). Norway's ministry reserve sits above the agency's frame (Q5 row 18).
2. **Size.** It is not a target or a sized fund (case l.106-107). It is half of VT's value, known to the dollar on the
   day of the 2031 meetings and named to co-sponsors then as held back: central $20,780; 1-in-20 $12,153 (house) to
   $13,928 (history). On 1 Jan 2033: central $23,986; 1-in-20 $12,150 (house) to $15,432 (joint history). That is
   about a sixth of the contribution in the middle and a tenth in a bad market. It is stated with its confidence: it
   covers a 10% stronger Taiwan dollar in 93-97 of 100 cases, or an early-stage overrun allowance of 13% in 78-86.
   With the cap rule (the surplus above the stated top joins it, median about $7,800 in Treasuries), those become
   99.97 and 99 of 100.
   *Sources:* GAO, "The amount of contingency should be based on the level of confidence with which management
   chooses to fund a program" (row 27). Q5's early-stage norms, 13%-17% (Norway, Denmark, GSA). Rows 22-26.
3. **Release and destination.** It stays in VT, promised to no one, until the facility's construction is complete. It
   is released in steps as each risk ends (RICS's "progressive release"): the currency part once the December 2032
   payment is converted, the overrun part at completion, the co-sponsor part when pledges are paid. Whatever was not
   called returns to Laura's own money: the "financial flexibility" the case asks her to keep (case l.102-103, l.145).
   It never passes to the facility or the operating budget by default. Any later gift from it is her separate,
   announced choice, so the 2031 range is never exceeded unannounced (D12).
   *Sources:* A133 contracts: "Any unused Contingency remaining at the completion of the Project shall be returned to
   the Owner" (row 29). AIA: periodic review and "release of the contingency back to the owner" (row 28). Gates
   Foundation terms: unused funds go back to the giver unless the giver redirects them in writing (row 30). RICS
   progressive release (Q5 row 29). ConsensusDocs: the balance "reverts back to the owner" (store H2-040).

Coherence check. IPS l.15 is kept verbatim as the purpose. The FINAL says the other half moves "Before you meet
co-sponsors in 2031", so the kept half staying in shares to completion is the IPS's own reading. No line sizes a
contingency fund or estimates the building's cost (CANON A31). The announced contribution remains the floor plus the
moved half (D12). The cap rule is optional and marked as under review.

## (d) Gaps

- **The rate history is one series used in proportion.** Starting from very low yields (2003-2004, 2008-2013) the
  ratio hits its 3x cap and gives 2031 yields of about 13-14%. The 1-year yield's annual log change has an s.d. of
  0.66, which is about 3 points a year at today's 4.6%. The house model uses 0.9 points; the 10-year's annual change
  was 1.17 points over 1962-2025. So the replay is harsher on rates than the house model, and some extreme rows
  (rows 15, 17) partly reflect the mapping.
- **585 overlapping windows are about four rate eras.** The post-2000 subset (129 windows) is about one cycle. The
  correlation figures describe, not estimate.
- **The stock series is the US (Shiller), not world shares (VT).** World shares fell further in 2008 and less in some
  US-only episodes. No world total-return monthly series is in the repo.
- **The Taiwan dollar file is a mirror** (`keel/models/data/twd_per_usd_monthly.csv`, Fed H.10 via a GitHub dataset),
  UNVERIFIED against FRED this session (`keel/models/data/SOURCES.md`). Spot checks there match.
- **The 2028 deposit is held at $150,000 in the joint replay.** The IPS's own story says a recession also shrinks
  Laura's income. The joint deposit-and-market stress is store H4-086's T1, still not re-run on the FINAL design.
  NUMBERS 5 has the deposit sizes on their own.
- **Contract and grant sources were read as search excerpts of the documents themselves** (rows 29-30), not full
  downloads. The AIA page and GAO guide were read in full excerpts.
- **Laura's role in the building** (owner, co-founder, donor) is not in the case. The owner's-contingency analogy fits
  best if she controls the project, and the release rule assumes she does.
- **A sixth world was not run.** A 1970s inflation with a stronger Taiwan dollar at once (a real-terms double hit)
  needs a joint US-Taiwan history from before 1983, which the repo lacks.

## Sources (APA 7 elements; all accessed 10 Nov 2026, Sydney)

- S1. U.S. Government Accountability Office. (2020). *Cost estimating and assessment guide: Best practices for
  developing and managing program costs* (GAO-20-195G). https://www.gao.gov/assets/gao-20-195g.pdf
- S2. Hart, D. H. (2023, November 30). *Managing the contingency allowance*. American Institute of Architects.
  https://www.aia.org/resource-center/managing-the-contingency-allowance
- S3. State of Louisiana, Division of Administration. (2025). *AIA Document A133-2009, Standard form of agreement
  between owner and construction manager as constructor, as modified by owner* (New Southeast Louisiana State Office
  Building). https://wwwprd.doa.louisiana.gov/osp/lapac/agency/pdf/8873801.pdf
- S4. Cobb County School District. (2022). *AIA Document A133-2009: Standard form of agreement between owner and
  construction manager as constructor* [Owner's template 10.28.2015, with Exhibit A, Guaranteed Maximum Price
  Amendment; the owner the document names, REFERENCES_APA 11 Nov]. https://sbcobbstor.blob.core.windows.net/media/WWWCobb/medialib/a133-2009-a133-exhibit-a-combined-cm-at-risk-contract-final-draft-attachment-b.0e31fa63819.pdf
- S5. Princeton University Facilities. (2025). *Construction management GMP contract* (Model v4.4, 03-2025).
  https://facilities.princeton.edu/sites/g/files/toruqf5436/files/documents/construction_management_gmp_contract_v4-4_03-2025_model.pdf
- S6. Bill & Melinda Gates Foundation. (2026). *Sample terms and conditions* [Project support].
  https://docs.gatesfoundation.org/documents/sample-terms-and-conditions.pdf
- S7. Woronkowicz, J., Joynes, D. C., Frumkin, P., Kolendo, A., Seaman, B., Gertner, R., & Bradburn, N. (2012). *Set
  in stone: Building America's new generation of arts facilities, 1994-2008*. Cultural Policy Center, University of
  Chicago. https://www.norc.org/content/dam/norc-org/pdfs/setinstone%20FINAL%20REPORT.pdf ; Harms, W.
  (2012, June 28). *Careful planning and focus on audience crucial to success of new cultural facilities*.
  University of Chicago News. https://news.uchicago.edu/story/careful-planning-and-focus-audience-crucial-success-new-cultural-facilities
- S8. Legislative Yuan Budget Center [立法院預算中心]. (2020, September). *108年度中央政府總決算審核報告評估報告*
  [Evaluation of the audit report on the FY2019 central government final accounts], item 41 (author 羅玉姍).
  https://www.ly.gov.tw/Pages/ashx/File.ashx?FilePath=~%2FFile%2FAttach%2F199201%2FFile_272610.pdf
- S9. Campbell, J. Y., Pflueger, C., & Viceira, L. M. (2020). Macroeconomic drivers of bond and equity risks. *Journal
  of Political Economy, 128*(8), 3148-3185. https://doi.org/10.1086/707766 (read at
  https://www.hbs.edu/ris/Publication%20Files/CampbellPfluegerViceira_JPE2020_c649d0cf-589b-4493-b695-c51d2ac45d48.pdf)
- S10. Molenaar, R., Sénéchal, E., Swinkels, L., & Wang, Z. (2024). Empirical evidence on the stock-bond correlation.
  *Financial Analysts Journal, 80*(3), 17-36. https://doi.org/10.1080/0015198X.2024.2317333
- S11. iShares Trust. (2026, February 27). *Summary prospectus: iShares iBonds Dec 2032 Term Treasury ETF*
  (IS-SP-IBTM-0226). BlackRock. (REFERENCES_APA row 78; copy read at
  https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf) ; BlackRock.
  (n.d.-b). *iShares iBonds Dec 2032 Term Treasury ETF (IBTM)* [Fund page]. iShares (REFERENCES_APA row 9; key facts as
  of 27 Oct 2026). https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf
- S12. BlackRock. (2025, October 15). *iShares iBonds ETFs near final distribution dates* [Press release]. Business
  Wire. https://www.businesswire.com/news/home/20251015356466/en/iShares-iBonds-ETFs-Near-Final-Distribution-Dates
- S13. Vanguard. (2026). *Vanguard Total World Stock ETF (VT)* [Fact sheet, as of 30 Sep 2026].
  https://fund-docs.vanguard.com/F3141.pdf
- S14. Adrian, T., Fleming, M., & Nikolaou, K. (2025). *US Treasury market functioning from the GFC to the pandemic*
  (Staff Report No. 1146). Federal Reserve Bank of New York.
  https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1146.pdf
- S15. Inter-Agency Working Group on Treasury Market Surveillance. (2024, September). *Enhancing the resilience of the
  U.S. Treasury market: 2024 staff progress report*. U.S. Department of the Treasury.
  https://home.treasury.gov/system/files/136/2024-IAWG-report.pdf
- S16. SIFMA. (2025, December 17). *Holiday schedule*. https://www.sifma.org/resources/guides-playbooks/holiday-schedule ;
  SIFMA. (2026, October 28). *SIFMA fixed income market close recommendation in the U.S., the U.K., and Japan for the
  U.S. Veterans Day holiday* [Press release].
  https://www.sifma.org/news/press-releases/sifma-fixed-income-market-close-recommendation-in-the-u-s-the-u-k-and-japan-for-the-u-s-veterans-day-holiday-2026
- Data (repo copies). Board of Governors of the Federal Reserve System. (n.d.-a). *Market yield on U.S. Treasury
  securities at 1-year constant maturity, quoted on an investment basis (DGS1)* [Data set; REFERENCES_APA row 15], FRED, `archive/rab/data/fred/DGS1.csv`. Shiller, R. J. (2023). *U.S.
  stock markets 1871-present* [ie_data.xls], mirror `keel/models/data/shiller_monthly.csv` (UNVERIFIED against the
  primary file). Board of Governors of the Federal Reserve System. (n.d.-c). *Taiwan dollars to U.S. dollar spot exchange
  rate (EXTAUS)* [Data set; release G.5, monthly; REFERENCES_APA, 11 Nov], mirror `keel/models/data/twd_per_usd_monthly.csv` (UNVERIFIED against the primary file).
