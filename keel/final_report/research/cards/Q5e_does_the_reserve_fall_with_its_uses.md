# Q5e research cards: does her flexibility fall when the claims on it rise?

Sat 14 Nov 2026, Sydney. Report parts: 3b (the facility contribution and her flexibility) and 3e (assumptions, limits
and what to watch; Table 3 row 7, "Her flexibility's three uses"). Notes for the Final Report store, not report prose.

Checked against: Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt` l.15, frozen: "half of the value of
the shares will be promised to no one. That is your flexibility – for building costs that overrun, a stronger Taiwan
dollar or a co-sponsor falling short"), `CANON.md` (A30 never counted in the range; A31 the three uses, no contingency
sizing, no facility cost estimate; C15), `NUMBERS.md` (8d, 8f, 8j, 8k; every plan figure here is quoted from there and is
MODEL), `WORDS.md` rows 28 and 34 ("her flexibility"; the three uses ranked by no one; anything above the top goes to her
flexibility), `exhibits/tables.md` Table 3 row 7, and the cards and store rows this builds on: Q5 (how much), Q10 (the
Taiwan index), Q24 (joint stress), Q4b and store rows H8-112, H9-013, Q4b-002, Q4b-007, Q12b-021 (giving in downturns),
H3-104 and H4-167 (wrong-way regimes), H9-097 (a contractor's failure in Taiwan). Limits kept: no cost for Laura's
building; rates and percentages only. The plan is frozen: a "risk" in the Clash column is a risk to record, never a
change to propose. Nothing in FINAL, the TNA, INTENT or SKELETON claims a natural hedge (grep, 14 Nov); the claim is
the lead's hypothesis.

**Claim tested.** Keep, kill or change: "Building costs and contractors' bid prices tend to fall or slow after a
share-market fall (contractors bid low when work dries up), so the shares-held flexibility is smallest when the overrun
risk it covers is also lower: a partial natural hedge."

**Problem class and the fields that solved it.** Asset-liability matching: judge a reserve by how it moves with the
claims on it, not by its own size alone. Pension surplus management states it as the "liability hedging credit"
(Sharpe and Tint, 1990; restated and criticised by Ang, Chen and Sundaresan, 2013); corporate risk management states it
as "hedge less when your cash and your needs move together" (Froot, Scharfstein and Stein, 1993). The building side is
answered by procurement-auction economics (markups over the cycle: Gugler, Weichselbaumer and Zulehner, 2015; De Silva
and Rosa, 2024), construction economics (tender price indices and their leading indicators) and the price series
themselves (Taiwan's DGBAS construction cost index; Turner's building cost index; the BEA price of nonresidential
structures; BLS producer prices; the UK tender price indices), tested here against TAIEX and the S&P 500.

## Verdicts in one screen

1. **The claim: CHANGE.** Half of it is right and it is not a hedge anyone can count on.
   - **Right, with a lag, in slumps without inflation.** Contractors do cut margins when work dries up: Austrian
     winning markups fell 3.3 points in the 2008-09 crisis (Gugler et al., 2015); Texas highway bids fell from 1.05 to
     0.93 of the engineer's estimate with "nearly two additional bidders" (De Silva and Rosa, 2024); Turner's selling
     price index fell 8.4% in 2009 and 4.0% in 2010; UK tender prices fell seven quarters running to Q3 2009. In US
     years with inflation under 4%, building costs one year after a share move correlate +0.22 (Turner) and +0.31 (BEA)
     with it (Keel arithmetic).
   - **Wrong in the same year, and wrong in inflationary falls.** In the year shares fall, building costs more often
     rise: the same-year correlation is negative in every series (Taiwan index against TAIEX -0.34, 1992-2025; Turner
     against the S&P 500 -0.31, 1965-2025; BEA structures -0.31, 1950-2025). Costs kept climbing through the crash
     year (Taiwan +14.0% in 2008 as TAIEX fell 46.0%; Turner +17.2% in 1974 as the S&P fell 29.2%) and rose through the
     2022 fall (Taiwan +7.4%, Turner +8.0%, BEA +16.3% as shares fell 16-22%). In US years with inflation of 4% or more
     the link is wrong-way both in the same year (-0.51 Turner) and a year later (-0.39).
   - **About nothing over Laura's own windows.** Shares over two years against building costs over the next two (her
     window: the 2031 meetings to the December 2032 contribution, then the build): correlations from -0.33 to +0.25
     across four series and two methods, none clearly different from zero. For Laura's actual pair, world shares (S&P
     500 as the stand-in for VT) against Taiwan building costs, the sign is negative (-0.15; -0.33 on separate
     windows): after the five two-year S&P falls since 1993, Taiwan costs rose faster in the next two years (mean +8.4%
     against +4.6%), because the 2004-05 steel boom followed the 2000-02 fall.
   - **Taiwan's index moves fast, then rebounds.** Month by month (1992-2026), the Taiwan index's yearly change
     follows the S&P's about six months later (r = +0.28 at 6 months), then turns (-0.31 at 24 months): costs fall
     after a slump and climb back within two to three years. The index measures materials and wages, so the fast part
     is commodity prices (Jul 2008 peak to May 2009: -15.1%), not contractors' bids.
   - **A low bid is not a low cost.** Rider Levett Bucknall in 2009: a contingency for change-order claims "on the rise
     because of unrealistic low bids"; AP in 2009: "risky bids could cause contractors, especially smaller ones, to
     fail"; Taiwan's Taipei Performing Arts Center lost its main contractor to bankruptcy in 2016 (store H9-097). And
     Taiwan's public works contracts pass index moves during the build to the owner (three-level price adjustment),
     so a cheap tender does not fix the cost of the years that follow.
2. **The three uses in one line (from this card, NUMBERS 8j and the store):** building costs give her flexibility no
   dependable help (lagged help in slumps, wrong-way in inflationary falls, about zero over two-year windows); the Taiwan
   dollar is independent of shares (+0.09 over the same two years, NUMBERS 8j); co-sponsors move against it in slumps
   (US giving -3.2% real in 2009, arts -10.1% real in 2008; store H8-112, H9-013, Q4b-002, Q12b-021) but held in current
   dollars through 2022 (arts +2.9%, Q4b-007). So the uses take turns: a demand slump hits co-sponsors and eases building
   costs a year later; an inflationary fall raises building costs while giving holds in dollars. They hit together in a
   stagflation like 1973-75 (giving -9.2%, H8-112; Turner +17.2% in 1974), the one named start in NUMBERS 8f where her
   flexibility is $13,832 (with the excess $22,036).
3. **The framing (Froot, Scharfstein and Stein, 1993; Sharpe and Tint, 1990, via Ang et al., 2013).** A reserve that
   falls exactly when its claims fall needs less backing ("even without hedging, the supply of internal funds tends to
   match the demand for funds"). Laura's shares earn no such credit against building costs, a negative one against
   co-sponsors, and none against the Taiwan dollar. The case for holding her flexibility in VT is its expected size,
   never a hedge. The part of her flexibility that does not fall with shares is the excess above the stated top (WORDS
   row 34): with it, the median in the paths where shares fell over 2031-33 is $23,201, against $15,423 for the shares
   alone (house model, NUMBERS 8f).
4. **The finding that most changes the report:** do not write "a partial natural hedge" anywhere. The honest line in
   NUMBERS 8f ("smallest in the years it is most likely to be needed") holds for co-sponsors in a slump and for building
   costs in an inflationary fall, not for the Taiwan dollar, and a stagflation is the case where two uses meet. Table 3
   row 7 watches building costs at "1.5% to 5.0% a year" with no trigger of its own; 2022's pattern (costs above 5% while
   shares fall) is the one this card says to watch (section c, for the lead).

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | In the year shares fall, building costs more often rise: same-year correlation of yearly cost changes with share returns is negative in every series (Taiwan index vs TAIEX -0.34, n=34; Turner vs S&P -0.31, n=61; BEA structures vs S&P -0.31 since 1950, n=76) | Keel arithmetic on DGBAS (2026), TWSE (2009-2026), Turner (2013-2026), U.S. Census Bureau (2003), BEA via FRED, Shiller (repo) | HALFKEPT, INFLATION_TWD | NICHE | If an overrun bill arrives while her flexibility is still in VT, the same-year relation is the one that applies, and it is wrong-way | Yearly data, small n (95% interval for Taiwan -0.61 to -0.00); Spearman agrees (-0.26 to -0.28); partly a timing artefact (costs are late-cycle) | VERIFIED (Keel arithmetic on primary series, method below) | risk: IPS l.15 holds her flexibility in shares; already recorded in NUMBERS 8f's honest line | Method, table M1 |
| 2 | One year after a share move the sign turns weakly right-way: Taiwan index +0.18 (TAIEX), +0.27 (S&P); Turner -0.02 since 1965 but +0.34 since 1990; BEA +0.12 since 1930 | Keel arithmetic, same series | HALFKEPT, INFLATION_TWD | NICHE | The lagged help the claim describes exists in the data, but it is small and only clear in the US since 1990 | Only Turner since 1990 (95% interval +0.01 to +0.60) excludes zero | VERIFIED (Keel arithmetic) | no | Method, table M1 |
| 3 | Over two-year windows (shares 2031-33, costs 2033-35 in Laura's terms) the relation is about nothing: -0.33 to +0.25 across four series and two methods | Keel arithmetic, same series | HALFKEPT, INFLATION_TWD, CEILING | NICHE | The window that matters to Laura shows no dependable hedge and no dependable harm from building costs | Overlapping windows inflate apparent n; separate windows leave 16-48 points | VERIFIED (Keel arithmetic) | no | Method, table M2 |
| 4 | Laura's actual pair (world shares, Taiwan building costs) leans wrong-way: Taiwan index vs S&P over the next two years -0.15 (overlapping), -0.33 (separate windows); after five two-year S&P falls, Taiwan costs rose +8.4% on average over the next two years against +4.6% after rises | Keel arithmetic, DGBAS + Shiller | HALFKEPT, INFLATION_TWD | NICHE | Taiwan's costs answer world commodity cycles; after 2000-02 they jumped (2004 +14.1%) as the world recovered | S&P stands in for VT; n=5 falls; the 2004-05 steel boom drives the gap | VERIFIED (Keel arithmetic) | no | Method, table M2 |
| 5 | Regime decides the sign: US years with inflation of 4% or more: Turner -0.51 same year, -0.39 a year later; BEA -0.30, -0.28. Under 4%: Turner -0.11, +0.22; BEA +0.02, +0.31 | Keel arithmetic; Shiller CPI (to 2022) | HALFKEPT, INFLATION_TWD, OTHER | NICHE | The same flip as stocks and bonds (store H3-104, H4-167): the help comes in demand slumps, the harm in inflationary falls | US only (Taiwan's index starts 1991, too few inflationary years); 19-25 inflationary years | VERIFIED (Keel arithmetic) | risk: the inflationary fall is the case to name in 3e | Method, table M3 |
| 6 | After big falls (over 20%), costs rise in the crash year and ease the next: Turner after the S&P's 1974, 2002, 2008 falls +8.2% then -1.1% (all-year mean +4.8%); Taiwan after seven TAIEX falls over 20% +6.1% then -0.3% (after rises +3.5%) | Keel arithmetic | HALFKEPT, INFLATION_TWD | NICHE | The claim's lagged form holds on average after large crashes, with the crash year itself wrong-way | n=3 and n=7; averages hide 1974 (inflationary) against 2009 (deflationary) | VERIFIED (Keel arithmetic) | no | Method, table M4 |
| 7 | Taiwan's index follows the S&P by about six months, then rebounds: monthly r +0.25 at 3 months, +0.28 at 6, +0.09 at 12, -0.20 at 18, -0.31 at 24 (n=417 months; +0.22 and -0.32 without 2021-23) | Keel arithmetic, DGBAS monthly + Shiller monthly | INFLATION_TWD, HALFKEPT | NICHE | A building priced six months after a slump gets cheaper inputs; one built over the following two to three years meets the rebound | Overlapping yearly changes: effective n about 35, so +/-0.33 is noise-level; a pattern, not proof | VERIFIED (Keel arithmetic) | no | Method, M5 |
| 8 | Cost surprise against trend (yearly change minus its own five-year mean) is wrong-way the same year and right-way the next: Taiwan vs TAIEX -0.43 then +0.41; Turner -0.20 then +0.20; BEA -0.27 then +0.05 | Keel arithmetic | INFLATION_TWD, HALFKEPT | NICHE | An overrun is cost above the budgeted drift (NUMBERS 8d's 3.0%); its timing against shares is the same split | Trend definition is Keel's choice | VERIFIED (Keel arithmetic) | no | Method, M6 |
| 9 | Taiwan 2008-09: the index peaked in Jul 2008 (92.10) with shares already falling, rose 14.0% on the year as TAIEX fell 46.0%, then fell 15.1% to May 2009 and 8.9% on 2009's average as TAIEX rose 78.3% | DGBAS (2026); TWSE (2009); Kaohsiung PWB (2012) | INFLATION_TWD, HALFKEPT | KNOWN | The strongest right-way move on record, but driven by steel and other materials falling with the world, not by bids | Annual averages make 2008 look wrong-way; Dec-to-Dec 2008 was +1.2% | VERIFIED (DGBAS table read in full; Kaohsiung report excerpt) | no | Card 4 |
| 10 | Taiwan's contractors named low-price bidding their main 2009 difficulty, yet their net margin rose to 4.3% from 2.4% in 2008 | Construction and Planning Agency (2011), abstract items 16 and 24 | INFLATION_TWD | NICHE | In Taiwan the 2009 bid discount was smaller than the materials fall (Keel inference): owners got less than the index's -8.9% | One survey year; margin is the industry's, not tender prices | VERIFIED (English abstract read in full) | no | Card 4 |
| 11 | Taiwan's public works contracts pass index moves during the build to the owner: a three-level price adjustment (single items, sub-groups, total index); typically changes beyond +/-2.5% of the award month, monthly from start to completion | Central News Agency (2022a); Kaohsiung PWB (2012) | INFLATION_TWD, HALFKEPT | NICHE | For a build under such a contract, the cost path through the build, not the tender price, reaches the project; the same-year relation (row 1) matters | Laura's residency's contract form is unknown and out of scope; private contracts may differ | VERIFIED (both read in part) | no | Card 4 |
| 12 | 2022, the inflationary counter-case: TAIEX -22.4%, S&P -16.3%; Taiwan index +7.4% (materials +8.51%), Turner +8.0%, BEA +16.3% | Keel arithmetic; Legislative Yuan Budget Center (2023) | INFLATION_TWD, HALFKEPT | KNOWN | The year her flexibility would be small is a year building costs ran well above NUMBERS 8d's 5.0% band top | One year; Taiwan's index flattened from May 2022 (-1.0% to December) | VERIFIED (DGBAS; LY report read in part) | risk: Table 3 row 7 has no building-cost trigger | Card 5 |
| 13 | In 2022 Taiwan's large public tenders (NT$50m+) awarded only at the third or later try rose to 26.32% (15.71% in 2017); first-try awards fell to 21.96% (39.87% in 2017) | Legislative Yuan Budget Center (2023), table 5 | INFLATION_TWD, OTHER | NICHE | When costs run, Taiwan tenders fail before they award: delay is the first form an overrun takes | Public works only; failed tenders also reflect budgets set below market (PCC's own finding) | VERIFIED (LY report read in part) | no | Card 5 |
| 14 | Of 98 major projects (NT$1bn+) revised in 2021 to Jul 2023, 41 raised their budgets for construction prices and wages; Kinmen Bridge: four revisions, 7 years 6 months longer | Legislative Yuan Budget Center (2023), section 4 | INFLATION_TWD | NICHE | Budget revisions bunch in an inflationary run, not after a share crash | Percentages for Laura only; no cost read across | VERIFIED (read in part) | no | Card 5 |
| 15 | Taipei found failed-tender rates for large works highly correlated with the index's yearly change (2012-2021) | Taipei City Public Works Department (2022) | INFLATION_TWD | NICHE | The overrun signal in Taiwan is the cost index itself, not the share market | Taipei only; the correlation figure not read | VERIFIED (abstract read) | no | Card 5 |
| 16 | Markups are procyclical: Austrian construction auctions, markups of all bids -1.5 points and of winning bids -3.3 points in the crisis; without the stimulus the fall would have been larger | Gugler, Weichselbaumer & Zulehner (2015) | INFLATION_TWD, OTHER | NICHE | The mechanism in the claim ("contractors bid low when work dries up") is real and measured | Austria, public works, stimulus muddies it; a few points of margin, not a collapse | VERIFIED (PMC full text read in part: abstract, data, results) | no | Card 3 |
| 17 | Texas highway bids fell from 1.05 to 0.93 of the engineer's estimate in the recession and stimulus; contracts drew "nearly two additional bidders"; lower costs and lower markups both explain it | De Silva & Rosa (2024); Belsie (2025) | INFLATION_TWD, OTHER | NICHE | A 12-point swing against the estimate is the size of the discount a slump can bring | Roads, not buildings; Texas; 2006-2010 only | VERIFIED (NBER paper read in part; Digest read) | no | Card 3 |
| 18 | US 2009: every state's bids 5-12% below estimates (AASHTO); New Jersey schools 15-39% below; a Texas contractor bid 17% under estimates against 9% over in 2006, margins cut 20-25%; NYC school bids drew 7-12 bidders against 2-4 | Associated Press (2009); Greer (2009) | INFLATION_TWD | KNOWN | The discount is visible at tender within a year of the crash | Press reports; selective examples | VERIFIED (read in part) | no | Card 3 |
| 19 | Selling-price indices fell hard, sticky indices barely: Turner -10.8% y/y (Q3 2009), RLB -3.5% (Q2 2009), 14 of 15 indexes down; BLS's new-school-building PPI only -2.9% from its Mar 2009 peak | Grogan (2009a, 2009b); BLS via FRED (PCU236222236222) | INFLATION_TWD | KNOWN | How much the "fall" is depends on the index; any 3e wording names the index | Indices differ in method; CONFLICTING sizes | CONFLICTING (sources disagree on size) | no | Card 3 |
| 20 | Low bids come back as claims and failures: RLB carried "a contingency for claims for change orders, which are on the rise because of unrealistic low bids"; "risky bids could cause contractors, especially smaller ones, to fail" | Grogan (2009b); Associated Press (2009); store H9-097 | INFLATION_TWD, OTHER | KNOWN | A slump-time tender can raise the overrun risk her flexibility covers (Taipei Performing Arts Center, store H9-097) | Anecdote, no rate of failure measured | VERIFIED (quotes read) | no | Card 3 |
| 21 | Construction is late-cycle: backlogs carry prices 12-18 months; competition "could intensify even more as non-residential building contractors work off their backlog"; "Backlogs fall and competition rises" | Grogan (2009b); Gugler et al. (2015) highlights | INFLATION_TWD | KNOWN | Explains rows 1 and 2: same year wrong-way, next year right-way | Mechanism, not a measured lag | VERIFIED (read) | no | Card 3 |
| 22 | UK after 2008: BCIS tender prices -12.6% in the year to Q2 2009, -3.7% to Q2 2010; seven quarters of falls to Q3 2009; social-housing tender prices still 13% below their Q2 2008 peak in Q3 2012 | Lowery (2010); RICS (2010); BIS (2012, 2013) | INFLATION_TWD | KNOWN | A third country shows the lagged fall and how long it lasts (four years below peak) | Not tested against the FTSE (gap); secondary for BCIS | VERIFIED (read in part) | no | Card 3 |
| 23 | The share index is not a reliable leading indicator of construction prices: UK "all share index ... produced inconclusive results"; ENR and Hong Kong forecasting models use the real economy and construction workload, not shares | Akintoye et al. (1998); Ashuri et al. (2012); Wong et al. (2010) | INFLATION_TWD, OTHER | NICHE | The link from shares to building costs runs through the real economy; sometimes it does not run at all | Abstracts only | UNVERIFIED (abstracts read, papers not) | no | Gaps |
| 24 | Hedge less when cash and needs move together ("even without hedging, the supply of internal funds tends to match the demand for funds"); with no correlation "it is optimal to hedge fully"; hedge ratios above one "when investment opportunities are negatively correlated with current cash flows" | Froot, Scharfstein & Stein (1993) | HALFKEPT, CERTAINTY | NICHE | The test for her flexibility: no use earns the "hedge less" credit; co-sponsors argue for more | Firms with investment needs, not a donor's reserve; equations not rendered | VERIFIED (full text read) | no | Card 1 |
| 25 | Sharpe-Tint's surplus objective rewards assets that move with liabilities: E(r_A) - (lambda/2)var(r_A) + lambda cov(r_A, r_L); "If the assets are uncorrelated with the liabilities ... standard mean-variance" | Sharpe & Tint (1990), via Ang, Chen & Sundaresan (2013) eq. (3) | HALFKEPT, CERTAINTY | KNOWN | VT earns about zero credit against building costs; its case in the plan is expected size, never hedging | Sharpe-Tint's own paper is a scan, not read | UNVERIFIED at source (read via ACS 2013) | no | Card 2 |
| 26 | Downside matters more than average co-movement: Sharpe-Tint counts downside "symmetrically with upside"; with a downside penalty the equity weight falls from 84% to 48%, "exactly the opposite of the Sharpe-Tint advice" | Ang, Chen & Sundaresan (2013) | HALFKEPT, CERTAINTY | NICHE | Her flexibility is judged in the bad states, and the bad state (an inflationary fall) is where building costs turn wrong-way | Pension calibration (liability-equity correlation 0.35 from LKB); not Laura's numbers | VERIFIED (read in full) | no | Card 2 |
| 27 | The classic surplus calibration assumes pension liabilities correlate 1.00 with bonds and 0.35 with equities; Keel finds building costs about 0 to -0.3 with shares | Leibowitz, Kogelman & Bader (1992), via ACS (2013) note 5 | HALFKEPT | NICHE | Against building costs, shares are a worse hedge than pension theory assumes for pension claims | LKB not read; different liability | UNVERIFIED (via ACS) | no | Card 2 |
| 28 | The uses take turns: slump 2008-09, giving fell and building costs fell a year later; inflationary 2022, building costs rose while giving held in dollars; stagflation 1973-75, both (giving -9.2%; Turner +17.2% in 1974); NUMBERS 8f's 1973 start leaves her flexibility $13,832 ($22,036 with the excess) | This card; store H8-112, H9-013, Q4b-007; NUMBERS 8f, 8j | HALFKEPT, COSPONSOR, INFLATION_TWD | NICHE | One sentence for 3e: which use calls on her flexibility depends on the kind of fall; only a stagflation brings two at once | 1973-75 is US-only; Taiwan's index starts 1991 | VERIFIED (each part at its source; the pattern is Keel's reading) | risk: the stagflation case, to record | Verdicts 2 |
| 29 | The part of her flexibility that does not move with shares is the excess above the stated top: median with it $23,201 where shares fell over 2031-33, against $15,423 without (house); $23,987 against $16,164 (history) | NUMBERS 8f; WORDS row 34 | HALFKEPT, CEILING | KNOWN | The plan's own answer to wrong-way timing is Treasury money, already in the design | MODEL; the excess exists only when the funds pay above the top | VERIFIED (NUMBERS 8f) | no | Verdicts 3 |

## (b) Cards

**Card 1. Hedge less when the money and the needs move together (Froot, Scharfstein and Stein, 1993).**
- What is it? A firm whose outside money is costly should hedge so that its own cash is there when its best uses
  come. How much depends on how the cash and the needs move together. Their oil-company example: "For such a company,
  hedging against oil price declines is less valuable—even without hedging, the supply of internal funds tends to
  match the demand for funds." With no link, "it is optimal to hedge fully"; and "optimal hedge ratios greater than one
  will arise when investment opportunities are negatively correlated with current cash flows." Conclusion: "Firms will
  want to hedge less, the more closely correlated are their cash flows with future investment opportunities."
- Did it work? It is the standard account of why firms hedge (Journal of Finance, 1993). Its test is exactly the
  claim's: does the money fall when the needs fall?
- How is Laura's case like it? Her flexibility is the money; the three uses are the needs; outside money (Laura's own
  later income) is costly or absent, since the case funds everything from the portfolio.
- How is it not? Laura cannot hedge after Nov 2026 (the plan is frozen), and her flexibility is by design unhedged
  money. The paper's options and state-dependent hedges have no place in the plan.
- What Caplet takes: the test, in plain words, for 3b or 3e: building costs do not reliably fall with shares (this
  card), the Taiwan dollar is unlinked (+0.09), and co-sponsors fall with them (store); none earns the "hedge less"
  credit. The Treasury part of what reaches her flexibility (the excess, row 29) is the plan's existing hedge.

**Card 2. The liability hedging credit, and why the downside matters more (Sharpe and Tint, 1990; Ang, Chen and
Sundaresan, 2013; Leibowitz, Kogelman and Bader, 1992).**
- What is it? Sharpe and Tint's surplus objective adds a credit for assets that move with the liabilities (Ang et
  al.'s eq. (3), which "emphasizes that the correlation of the liabilities with the asset returns influences the
  optimal portfolio holdings"). Ang et al. show it counts downside co-movement "symmetrically with upside covariance";
  penalising only shortfalls cuts the equity weight from Sharpe-Tint's 84% to 48%, "exactly the opposite of the
  Sharpe-Tint advice!", because "although equities are positively correlated with the liabilities, there can be
  instances of substantial underperformance". Their calibration follows LKB: liabilities correlate 0.98 (LKB 1.00) with
  bonds and 0.35 with equities.
- Did it work? It is how pension funds judge a reserve, and the downside version explains why funds that took the
  equity credit were hurt in the falls when it vanished.
- How is Laura's case like it? Her flexibility is a small surplus held against three unpriced claims. The building
  claim's correlation with shares is about 0 on average and negative in inflationary falls (rows 1, 3, 5): the average
  credit is nil and the downside credit is negative.
- How is it not? Pension liabilities are long bond-like streams; Laura's three uses are one-off and of unknown size
  (CANON A31: no contingency sizing). Sharpe-Tint was read through Ang et al. only.
- What Caplet takes: the vocabulary of the test ("judge a reserve by how it moves with what it pays for") and the
  result: VT is there for its expected size (the top of the range, NUMBERS 4's all-Treasury benchmark records the cost),
  not as a hedge of building costs.

**Card 3. Contractors do bid low in slumps, a year late and at a price (Gugler et al., 2015; De Silva and Rosa, 2024;
ENR and AP, 2009; UK tender prices).**
- What is it? Procurement-auction studies measure margins over the cycle. Austria: markups of all bids fell 1.5 points
  and of winning bids 3.3 points in the crisis, and "without the government stimulus package this decrease would have
  been larger" (procyclical markups). Texas: relative bids fell from 1.05 to 0.93 of the engineer's estimate, with nearly
  two more bidders per contract. Field reports: Turner's selling price index -10.8% in the year to Q3 2009; every state's
  bids 5-12% under estimates; New Jersey schools 15-39% under. UK tender prices fell seven quarters running, and social-housing
  tender prices stayed 10-13% below their 2008 peak into 2012.
- Did it work? For owners who tendered in 2009-10, yes: the same building cost less. The lag is the backlog: ENR, Sep
  2009, "competition could intensify even more as non-residential building contractors work off their backlog";
  Turner's index rose 6.3% in 2008 and fell only in 2009-10.
- How is Laura's case like it? A Taiwan residency tendered a year after a demand slump would meet keener bids.
- How is it not? Three ways. The discount is late (a year or more), so in the crash year itself costs are still rising
  (row 1). It is partly paid back: RLB in 2009 carried "a contingency for claims for change orders, which are on the
  rise because of unrealistic low bids", and AP warned "risky bids could cause contractors, especially smaller ones, to
  fail" (Taiwan: H9-097). And it vanishes when the fall is inflationary (Card 5). The share index is also a poor signal
  of construction prices (Akintoye et al., 1998: "inconclusive"; abstract only).
- What Caplet takes: the true half of the claim, at most one clause in 3e if room ("a year after a slump, bids can be
  lower; in an inflationary fall, costs rise"), never as a reason her flexibility can be smaller.

**Card 4. Taiwan 2008-09: the fastest right-way move on record, made by materials (DGBAS; TWSE; Kaohsiung PWB, 2012;
Construction and Planning Agency, 2011).**
- What is it? Taiwan's construction cost index (materials and wages, 2021 = 100) peaked at 92.10 in Jul 2008, with
  shares already falling (S&P monthly average 1,403 in May 2008, 1,257 in July, 883 in November); it fell 15.1% to
  78.19 in May 2009 (Keel arithmetic). On yearly
  averages it rose 14.0% in 2008 (TAIEX -46.0%) and fell 8.9% in 2009 (TAIEX +78.3%). Kaohsiung's public works bureau
  called the swing "相當劇烈" (very sharp) and not normal market behaviour.
- Did it work? For owners pricing in 2009, inputs were cheaper. Contractors named "the competition in bids with the
  lowest price" their main 2009 difficulty, but their net margin rose to 4.3% from 2.4% in 2008: bids fell less than
  inputs (Keel inference from the survey).
- How is Laura's case like it? Taiwan's index moves with world commodity prices within months (row 7), so a world
  slump lowers Taiwan's input costs quickly.
- How is it not? Taiwan's public contracts pass index moves to the owner during the build ("契約三層級物價調整機制",
  CNA 2022; ±2.5% from the award month, Kaohsiung 2012), so the rebound that follows within two to three years (row 7:
  -0.31 at 24 months; 2004 +14.1% after the 2000-02 fall) also reaches the project. The residency's contract form is
  unknown and out of scope.
- What Caplet takes: 3e's monitoring: the DGBAS index is the signal for building costs (Table 3 row 7 already reads it
  against 1.5-5.0%); the share market is not.

**Card 5. 2022: the inflationary fall, when building costs and a small flexibility coincide (Legislative Yuan Budget
Center, 2022, 2023; Turner; BEA; store Q4b-007).**
- What is it? In 2022 TAIEX fell 22.4% and the S&P 16.3% (December averages). Taiwan's index rose 7.4% on the year
  (materials +8.51%, after +13.74% in 2021); Turner rose 8.0%; the BEA price of nonresidential structures 16.3%. Taiwan's
  large public tenders awarded only at the third or later try rose to 26.32% of awards (15.71% in 2017), first-try
  awards fell to 21.96%, and 41 of 98 major projects revised from 2021 to Jul 2023 raised budgets for prices and wages.
- Did it work? Against the claim: the share fall came with rising building costs and failing tenders. Giving held in
  dollars (foundations +2.5%, arts +2.9% current; Q4b-007), so co-sponsors were not the use under strain.
- How is Laura's case like it? An inflationary 2031-33 would shrink her flexibility (NUMBERS 8f: median about $15,400
  where shares fell, house) while building costs ran above NUMBERS 8d's 5.0% band top.
- How is it not? Taiwan's index flattened from May 2022 (109.05) and was 1.0% lower by December; the peak of the
  pressure was 2021, a year when shares rose 23.7% (TAIEX). One episode, not a law.
- What Caplet takes: the one case where building costs call on her flexibility while it is small. The store's
  wrong-way rows (H3-104, H4-167) already name the inflationary regime for bonds; this card adds building costs to the
  same regime. A risk to record in 3e, never a change.

**Card 6. The test itself: what the numbers say over Laura's windows (Keel arithmetic, method below).**
- What is it? Yearly cost changes in three building series (Taiwan's DGBAS index 1992-2025; Turner 1965-2025; BEA
  structures 1930-2025) against share returns (TAIEX; S&P 500) the same year, one and two years later, over two-year
  windows, after big falls, against trend, by inflation regime, and month by month for Taiwan.
- Did it work? The pattern is consistent across series: wrong-way in the same year (-0.24 to -0.34), weakly right-way
  a year later (+0.12 to +0.34), about nothing over two-year windows (-0.33 to +0.25), wrong-way in inflation (-0.51),
  right-way without it (+0.22 to +0.31 a year later).
- How is Laura's case like it? Her flexibility is valued on 1 Jan 2033 and stays in VT until used (IPS l.15); the
  two-year windows match the 2031 meetings to the contribution and the build after it.
- How is it not? The S&P stands in for VT (world shares; Taiwan is a small part); TAIEX is a price index without
  dividends; Taiwan's index measures inputs, not tender prices; yearly data give 34-96 points.
- What Caplet takes: no natural hedge to claim; the honest summary of three uses (Verdicts 2); the regime as the thing
  to watch.

## (c) Verdict

**CHANGE.**
- Keep: "contractors bid low when work dries up" (Gugler et al.: winning markups -3.3 points; De Silva and Rosa:
  1.05 to 0.93 of the estimate) and "building costs fall or slow after a share-market fall" in demand slumps, a year
  later (Turner -8.4% in 2009, -4.0% in 2010; Taiwan -8.9% in 2009; UK -12.6% to Q2 2009; one year on, US
  low-inflation correlation +0.22 to +0.31).
- Kill: "so the shares-held flexibility is smallest when the overrun risk it covers is also lower: a partial natural
  hedge". In the crash year costs more often rise (-0.24 to -0.34), in inflationary falls they rise (2022; 1974), after
  slumps they rebound within two to three years (Taiwan, -0.31 at 24 months), and over Laura's two-year windows the
  link is about zero (-0.33 to +0.25). Low bids bring claims and failures, and Taiwan's public contracts pass index
  moves to the owner during the build.
- Change to (a note, not prose): "Building costs follow no fixed pattern after a share fall: in a slump without
  inflation, bids and costs often ease a year later; in an inflationary fall they rise; so her flexibility gets no
  dependable help from building costs, and the plan claims none."
- Across the three uses: building costs, no dependable link (this card); the Taiwan dollar, unlinked (+0.09, NUMBERS
  8j); co-sponsors, wrong-way in slumps (store) but steady in dollars in 2022 (Q4b-007). The uses take turns by kind of
  fall; a stagflation brings two at once (1973-75; NUMBERS 8f's 1973 start: $13,832, $22,036 with the excess).
- For the lead to decide:
  1. Whether 3e names the inflationary fall (2022's pattern) as the case where building costs and a small flexibility
     meet, beside the slump case NUMBERS 8f already states.
  2. Whether Table 3 row 7's "Look closer" cell gains a building-cost trigger, e.g. Taiwan's index above 5.0% a year
     (NUMBERS 8d's band top) while shares fall; today it names only the Taiwan dollar. A monitoring change, not a plan
     change.
  3. Whether NUMBERS 8f's honest line ("smallest in the years it is most likely to be needed") is narrowed to "in the
     years co-sponsors are most likely to fall short" with the inflationary case beside it.

## Method and figures (Keel arithmetic)

Scripts and outputs in scratch, outside the repo: `/tmp/claude-0/q5e/scripts/corr.py` (output `corr_out.txt`) and
`/tmp/claude-0/q5e/scripts/monthly_lag.py` (output `monthly_out.txt`), data in `/tmp/claude-0/q5e/data/`.

**Series.**
- Taiwan building costs: DGBAS 營造工程物價指數 總指數 銜接表 (construction cost index, total, linked, 2021 = 100),
  monthly Jan 1991 to Sep 2026 with yearly averages; https://ws.dgbas.gov.tw/001/Upload/463/relfile/10315/2703/ccispl.xls
  (read in full). Sub-indices are materials and labour (wages, equipment rent): an input-cost index, not a tender-price
  index.
- TAIEX: year-end closes 1989-2025, TWSE Fact Books table 2.01 (2009 edition for 1989-2008; 2019, 2020, 2024, 2025,
  2026 editions for later years); price index, no dividends.
- S&P 500: Shiller monthly averages, repo mirror `keel/models/data/shiller_monthly.csv`; December average to December
  average (price), and a total return with dividends to 2022.
- Turner Building Cost Index (selling prices, "the competitive condition of the marketplace"): Census quarterly
  1964-2002 (1996 = 100, rounded to whole numbers; U.S. Census Bureau, 2003) spliced to Turner's yearly averages
  2000-2025 (Turner releases) at the 2000-02 ratio 5.047.
- BEA price index, nonresidential structures, yearly 1929-2025: FRED B009RG3A086NBEA.
- BLS PPI construction materials and components, December values 1947-2025: FRED WPUSI012011; new school building
  construction (bid-price PPI) PCU236222236222; net inputs to nonresidential construction (goods) WPUIP2312301.

**Conventions.** Cost change in year t against share return in year t - lag. A positive correlation means costs fall
when shares fall (the claim's hedge). Pearson with Fisher 95% intervals; Spearman beside it. Two-year windows: share
return over (t-2, t] against cost change over the same window and over (t, t+2]; "separate" uses every second window.

**M1. Yearly correlations (Pearson; Spearman in brackets).**

| Pair | Years, n | Same year | 1 year later | 2 years later |
|---|---|---|---|---|
| Taiwan index (yearly average) vs TAIEX | 1992-2025, 34 | -0.34 (-0.26) | +0.18 (+0.24) | -0.13 |
| Taiwan index (Dec to Dec) vs TAIEX | 1992-2025, 34 | -0.18 | +0.13 (+0.34) | -0.26 |
| Taiwan index (yearly average) vs S&P 500 | 1992-2025, 34 | -0.24 | +0.27 | -0.22 |
| Taiwan index (Dec to Dec) vs S&P 500 | 1992-2025, 34 | +0.10 | +0.10 | -0.35 |
| Turner vs S&P 500 | 1965-2025, 61 | -0.31 (-0.27) | -0.02 | +0.18 |
| Turner vs S&P 500 total return | 1965-2022, 58 | -0.29 | +0.01 | +0.20 |
| Turner vs S&P 500 | 1990-2025, 36 | -0.23 | +0.34 (+0.11) | +0.35 |
| BEA structures vs S&P 500 | 1930-2025, 96 | -0.10 (-0.17) | +0.12 | +0.21 |
| BEA structures vs S&P 500 | 1950-2025, 76 | -0.31 (-0.28) | -0.06 | +0.10 |
| BEA structures vs S&P 500 | 1990-2025, 36 | -0.31 | +0.09 | +0.23 |
| BLS construction materials PPI vs S&P 500 | 1948-2025, 78 | -0.03 | +0.04 | -0.13 |

95% intervals: about +/-0.33 at n = 34-36, +/-0.24 at n = 61, +/-0.20 at n = 96.

**M2. Two-year windows (Laura's: shares 2031-33; costs then and after).**

| Pair | Same window (overlapping / separate) | Next window (overlapping / separate) | Next two years' cost change after a two-year share fall / rise (mean) |
|---|---|---|---|
| Taiwan index vs TAIEX | -0.09 / +0.32 | +0.13 / -0.01 | +3.4% / +6.7% (n = 14 / 17) |
| Taiwan index vs S&P 500 | -0.24 / -0.07 | -0.15 / -0.33 | +8.4% / +4.6% (n = 5 / 26) |
| Turner vs S&P 500 | -0.23 / -0.34 | +0.14 / +0.25 | +9.8% / +10.0% (n = 12 / 46) |
| BEA structures vs S&P 500 | -0.08 / -0.13 | +0.17 / +0.19 | +9.9% / +9.0% (n = 21 / 72) |

**M3. By inflation regime (US CPI December to December, Shiller, to 2022).**

| Series | CPI 4% or more: same year / 1 year later | CPI under 4%: same year / 1 year later |
|---|---|---|
| Turner | -0.51 / -0.39 (n = 19) | -0.11 / +0.22 (n = 39) |
| BEA structures | -0.30 / -0.28 (n = 25) | +0.02 / +0.31 (n = 67) |

**M4. After share falls (mean cost change, %).**

| Pair | Shares fell: same year / next | Fell over 20%: same year / next | Shares rose: same year / next |
|---|---|---|---|
| Taiwan index vs TAIEX (1992-2024) | +4.5 / +0.3 (n = 10) | +6.1 / -0.3 (n = 7) | +2.3 / +3.5 (n = 23) |
| Taiwan index vs S&P 500 | +2.3 / +0.0 (n = 8) | +8.1 / -2.1 (n = 2) | +3.2 / +3.4 (n = 25) |
| Turner vs S&P 500 (1965-2024) | +6.1 / +5.0 (n = 17) | +8.2 / -1.1 (n = 3) | +4.3 / +4.7 (n = 43) |
| BEA vs S&P 500 (1930-2024) | +4.6 / +4.0 (n = 31) | +3.8 / -1.6 (n = 6) | +3.9 / +4.3 (n = 64) |

**M5. Taiwan month by month** (index yearly change in month t against the S&P's yearly change k months earlier,
1992-2026, 417 months): k = 0: +0.14; 3: +0.25; 6: +0.28; 9: +0.20; 12: +0.09; 15: -0.05; 18: -0.20; 21: -0.27;
24: -0.31; 27: -0.27; 30: -0.19; 36: -0.08. Without 2021-23: 6: +0.22; 24: -0.32. Overlapping yearly changes leave
an effective sample of about 35, so these are a shape, not a test.

**M6. Cost surprise against trend** (yearly change minus its own previous five-year mean): Taiwan vs TAIEX -0.43 same
year, +0.41 a year later (n = 29, 28); Taiwan vs S&P -0.24, +0.40; Turner vs S&P -0.20, +0.20 (n = 55, 54); BEA vs
S&P -0.27, +0.05 (n = 91, 90).

**Episodes (yearly change, %; shares calendar-year price return, S&P on December averages).**

| Year | TAIEX | S&P 500 | Taiwan index (avg) | Taiwan index (Dec-Dec) | Turner | BEA structures | BLS materials PPI |
|---|---|---|---|---|---|---|---|
| 1973 | n/a | -19.3 | n/a | n/a | +5.8 | +7.7 | +11.7 |
| 1974 | n/a | -29.2 | n/a | n/a | +17.2 | +13.8 | +16.5 |
| 1975 | n/a | +32.2 | n/a | n/a | +4.7 | +11.9 | +6.2 |
| 2000 | -43.9 | -6.8 | -0.5 | -1.5 | +4.3 | +3.9 | -0.6 |
| 2001 | +17.1 | -14.0 | -1.0 | +0.0 | +3.0 | +5.2 | -0.6 |
| 2002 | -19.8 | -21.5 | +2.1 | +2.9 | +1.0 | +4.2 | +1.8 |
| 2003 | +32.3 | +20.2 | +4.7 | +6.8 | +0.3 | +3.6 | +3.7 |
| 2004 | +4.2 | +11.0 | +14.1 | +12.0 | +5.4 | +7.4 | +11.1 |
| 2008 | -46.0 | -40.7 | +14.0 | +1.2 | +6.3 | +5.1 | +6.2 |
| 2009 | +78.3 | +26.5 | -8.9 | -1.7 | -8.4 | -1.8 | -2.8 |
| 2010 | +9.6 | +11.8 | +3.2 | +3.8 | -4.0 | -0.8 | +2.5 |
| 2015 | -10.4 | -0.0 | -2.8 | -4.6 | +4.5 | +1.6 | -2.1 |
| 2016 | +11.0 | +9.4 | -1.7 | +1.5 | +4.9 | -0.1 | +2.2 |
| 2020 | +22.8 | +16.3 | +1.4 | +4.0 | +1.8 | +1.5 | +6.8 |
| 2021 | +23.7 | +26.5 | +10.9 | +11.3 | +1.9 | +3.3 | +35.1 |
| 2022 | -22.4 | -16.3 | +7.4 | +4.5 | +8.0 | +16.3 | -2.6 |
| 2023 | +26.8 | +19.7 | +1.7 | +1.8 | +6.0 | +5.7 | +0.4 |

2004 row computed separately from the same series (TAIEX 6,139.69 / 5,890.69; Taiwan index 64.45 / 56.47). The 2020
crash and rebound fell inside one calendar year; yearly data cannot test it.

**Caveats.** The S&P 500 stands in for VT (world shares); MSCI ACWI was not used. TAIEX has no dividends (the
correlations barely move with a steady yield). Turner before 2000 is whole-number Census data (a one-point step is
2-5% in the 1960s-70s). BEA's structures price is partly built from cost indices. Annual averages smear turning points
(2008 in Taiwan). None of this estimates a cost for Laura's building.

## (d) Gaps

- No Taiwan tender-price index found: the DGBAS index measures inputs. Award-to-budget ratios exist only for Taipei's
  public works bureau, 2013-2018 (89.49% in 2013 to 77.26% in 2015, 85.94% in 2016; Taipei City Public Works
  Department, 2019, read in part); a national series by year was not found. 2015's dip fits the claim (TAIEX -10.4%,
  index -2.8%) but is one city.
- Sharpe and Tint (1990) is a scanned PDF with no text: read only through Ang et al. (2013) and secondary sources.
  Leibowitz, Kogelman and Bader (1992) not read: their 1.00 and 0.35 correlations come from Ang et al.'s note 5.
- Gugler et al. (2015) and De Silva and Rosa (2024) read in part (abstract, data, results), not every section.
- Akintoye et al. (1998), Wong et al. (2010) and Ashuri et al. (2012): abstracts only (Consensus); co-authors after the
  first not confirmed.
- RLB and Mortenson index series not obtained; their 2009 figures come from ENR's reports.
- UK not tested against the FTSE; Japan not done.
- Taiwan before 1991 (including 1973-75) not testable: the index starts in 1991.
- Whether Laura's residency would build under a price-adjusted contract is unknown and out of scope (case: no
  facility cost estimates).

## Sources (APA 7; all accessed 14 Nov 2026, Sydney)

Ang, A., Chen, B., & Sundaresan, S. (2013). *Liability driven investment with downside risk* [Author manuscript;
published in The Journal of Portfolio Management]. Columbia Business School.
http://www.columbia.edu/~bc2404/papers/Ang-Chen-Sundaresan.JPM.2013.pdf (read in full)

Akintoye, A., et al. (1998). Macro-economic leading indicators of construction contract prices. *Construction
Management and Economics*. https://consensus.app/papers/details/w:c2971b9e-ce34-4e8d-b7af-2de7454e891b/ (abstract only;
co-authors UNVERIFIED)

Ashuri, B., et al. (2012). Empirical tests for identifying leading indicators of ENR Construction Cost Index.
*Construction Management and Economics*. https://consensus.app/papers/details/w:9e322063-f72b-4722-8fc4-c735f4ef551d/
(abstract only)

Associated Press. (2009, September 8). Sunken economy boosts public construction projects. *San Bernardino Sun*.
https://www.sbsun.com/2009/09/08/sunken-economy-boosts-public-construction-projects (read in part)

Belsie, L. (2025, March). Highway construction costs during the Great Recession: Evidence from Texas. *NBER Digest*.
https://www.nber.org/digest/202503/highway-construction-costs-during-great-recession-evidence-texas

Central News Agency. (2022a, March 2). 公共工程斷炊危機？工程會因應缺工有對策 [Public works at risk? The Public
Construction Commission's measures for labour shortages]. https://www.cna.com.tw/news/afe/202203020355.aspx

Central News Agency. (2022b, June 10). 營建物價上漲缺工缺料 工程會多管齊下因應 [Rising construction prices and
shortages: the Public Construction Commission responds]. https://www.cna.com.tw/news/afe/202206100324.aspx

Construction and Planning Agency, Ministry of the Interior. (2011). *2009 economic survey of construction industry in
Taiwan* [Abstract]. https://www.nlma.gov.tw/uploads/files/3928f4dc1a83906c195a2c9dfbccd773.pdf (English abstract read in
full)

De Silva, D. G., & Rosa, B. (2024). *Highway procurement during the Great Recession and stimulus* (NBER Working Paper
No. 33299). National Bureau of Economic Research.
https://www.nber.org/system/files/working_papers/w33299/w33299.pdf (read in part)

Department for Business, Innovation and Skills. (2012). *Quarterly construction price and cost indices commentary:
3rd quarter 2012*.
https://assets.publishing.service.gov.uk/media/5a78e8d9ed915d04220664e8/12-p150c-Construction-Price-Cost-Indices-Commentary-2012Q3.pdf

Department for Business, Innovation and Skills. (2013). *Quarterly construction price and cost indices commentary:
4th quarter 2012*.
https://assets.publishing.service.gov.uk/media/5a75c6d1ed915d6faf2b5984/13-p150a-Construction-Price-Cost-Indices-Commentary-2012Q4.pdf

Directorate-General of Budget, Accounting and Statistics. (2026). *營造工程物價指數 總指數 銜接表* [Construction cost
index, total, linked series, 2021 = 100] [Data set]. https://ws.dgbas.gov.tw/001/Upload/463/relfile/10315/2703/ccispl.xls
(read in full)

Federal Reserve Bank of St. Louis. (2026). *FRED series B009RG3A086NBEA, PCU236222236222, WPUIP2312301 and
WPUSI012011* [Data sets; U.S. Bureau of Economic Analysis and U.S. Bureau of Labor Statistics].
https://fred.stlouisfed.org/graph/fredgraph.csv?id=B009RG3A086NBEA (and the same URL with each other id)

Froot, K. A., Scharfstein, D. S., & Stein, J. C. (1993). Risk management: Coordinating corporate investment and
financing policies. *The Journal of Finance, 48*(5), 1629-1658.
https://doi.org/10.1111/j.1540-6261.1993.tb05123.x (read in full)

Greer, J. (2009, September 16). Bidding frenzy. *ENR*. https://www.enr.com/articles/11180-bidding-frenzy (read in part;
author's first name UNVERIFIED)

Grogan, T. (2009a, June 24). Costs post rare quarterly decline. *ENR*.
https://www.enr.com/articles/1766-costs-post-rare-quarterly-decline (read in part)

Grogan, T. (2009b, September 23). Competition intensifies as recession deepens. *ENR*.
https://www.enr.com/articles/print/1798-competition-intensifies-as-recession-deepens (read in part)

Gugler, K., Weichselbaumer, M., & Zulehner, C. (2015). Competition in the economic crisis: Analysis of procurement
auctions. *European Economic Review, 73*, 35-57. https://doi.org/10.1016/j.euroecorev.2014.10.007 (PMC full text,
https://pmc.ncbi.nlm.nih.gov/articles/PMC4318169, read in part)

Kaohsiung City Government Public Works Bureau. (2012). *營建物價之分析與趨勢評估* [Construction prices: analysis and
trends]. https://pwb.kcg.gov.tw/Web/FileDownLoad/FileUpload/20131029165728513215.pdf (read in part)

Legislative Yuan Budget Center. (2022, September). 六七、近年國內營建材料及勞務價格持續上漲，致工程採購案件流、廢標情形趨增
[Item 67: rising construction prices and failed tenders].
https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=45676&pid=221597 (read in part)

Legislative Yuan Budget Center. (2023, September). 六二、受近年營造工程物價上漲之影響，部分公共工程採購案件多次流標
[Item 62: repeated failed tenders and budget increases].
https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=46405&pid=231952 (read in part)

Leibowitz, M. L., Kogelman, S., & Bader, L. N. (1992). Asset performance and surplus control: A dual-shortfall
approach. *The Journal of Portfolio Management*. (Not read; cited through Ang et al., 2013, note 5; UNVERIFIED)

Lowery, D. (2010, October 28). Tender prices "have hit the bottom". *Construction News*.
https://www.constructionnews.co.uk/sections/news/tender-prices-have-hit-the-bottom-28-10-2010 (read in part)

Royal Institution of Chartered Surveyors. (2010, February 12). *RICS surveys reveal contraction in workloads and drop in
tender prices in UK* [Press release]. PR Newswire.
http://www.prnewswire.com/news-releases/rics-surveys-reveal-contraction-in-workloads-and-drop-in-tender-prices-in-uk-in-stark-contrast-to-hong-kongs-more-promising-market-condition-84205732.html

Sharpe, W. F., & Tint, L. G. (1990). Liabilities: A new approach. *The Journal of Portfolio Management, 16*(2), 5-10.
https://www.andreisimonov.com/NES/SharpeTint1990JPM.pdf (scan, no text; not read at source; pages UNVERIFIED)

Shiller, R. J. (2026). *U.S. stock market data, monthly* [Data set; repo mirror
`keel/models/data/shiller_monthly.csv`, per `keel/models/data/SOURCES.md`].

Taipei City Public Works Department. (2019). *統計應用分析報告: 臺北市公共工程執行情形與效能分析* [Public works
execution in Taipei]. Taipei City Government (read in part).

Taipei City Public Works Department. (2022). *統計應用分析報告: 嚴重特殊傳染性肺炎（COVID-19）疫情前後營造工程物價變化及對公共工程招標之影響*
[Construction prices before and after COVID-19 and their effect on public tenders]. Taipei City Government (abstract
read).

Taiwan Stock Exchange. (2009-2026). *Fact book*, table 2.01 [Data set; 2009, 2019, 2020, 2024, 2025 and 2026
editions]. https://www.twse.com.tw/downloads/zh/about/company/factbook/2009/s2.01.html (and the later editions' 2.01)

Turner Construction Company. (2013-2026). *Turner building cost index* [Quarterly releases, incl. Q4 2022, Q3 2025,
Q1 2026]. https://www.turnerconstruction.com/uploads/cost-index-Q1-2026.pdf

U.S. Census Bureau. (2003). *Quarterly indexes used in deriving estimates of the value of construction put in place in
constant dollars* [Archived]. https://permanent.fdlp.gov/websites/www.census.gov/www.census.gov/const/C30/quarterly.pdf

Wong, J. M. W., et al. (2010). Forecasting construction tender price index in Hong Kong using vector error correction
model. *Construction Management and Economics*.
https://consensus.app/papers/details/w:5e70b1f5-b503-4c37-acac-27bd3587007c/ (abstract only)
