# Q88. How would a professional measure how well the WInS portfolio was bought, and what can Section 2.5 honestly claim?

- **Date:** Mon 16 Nov 2026 (Sydney).
- **Report parts it serves:** 2.5 (main), 2.1 (what the scale model cannot show), Table 1 (its note), 3e (assumptions and
  limits: Laura's real purchase), Table 3 (the checks at the January 2028 build and the 2031 move).
- **Notes for the Final Report store, not report prose.**
- **Not repeated** (checked): Q17 rows 1-4 (Perold citation, T-Standard as "industry standard", Russell's "rate
  volatility" line, FCA's "important element"), rows 7 and 9 (escrow verification, 0% SLGS), rows 34-35 (the stale
  price that changed a rung; ETF median spreads and the $46 half-spread); Q29 rows 12-14 and 26-27 (targets as fidelity,
  the five stop rules, VT bought last; SEC hypothetical performance); Q45 row 26 (SEC's 0.07% retail Treasury spread);
  Q54-028 and Q54-030 (escrow bidding safe harbour; SLGS one basis point below Treasury's rate); Q76-021 (GIPS
  no-linking and theoretical-performance labels); Q26 (Rule 6c-11's 2%-for-seven-days statement); Q3a (Perold and
  Sharpe; store row 102 is Perold 1988). Store grep: "15c3-5", "transition manag", "performance holiday", "2232", "6750"
  and "Hu, Pan" 0 each; "implementation shortfall" 3; "T-Standard" 1.
- **Claims tested:**
  1. Perold's (1988) implementation shortfall fits 2.5, with the book's parts mapped (fees, trading against the curve
     band, opportunity cost) and one number a practitioner would accept.
  2. Bond and ETF desks use known benchmarks (arrival price, the curve, premium to NAV; TRACE, Rule 6c-11), and some of
     the team's pre-trade checks match professional practice.
  3. A one-time build to fixed targets is judged by completeness and cost, not return; 2.5 can borrow a real
     post-trade report's format.
  4. A judge will raise three limits (WInS fills at WInS prices; $300,000 of a $450,000 plan; later returns do not
     count), and they can be stated plainly.
- **Problem class and the field that solved it first:** transaction cost analysis. Solved first for institutional
  share trading (Perold named the implementation shortfall at Harvard Business School in 1988; Arnott and Wagner 1990),
  carried to one-time portfolio builds by transition managers (Russell's T-Standard, 2003; the industry's T-Charter,
  2007), and for bonds by fixed income TCA and, in public finance, by the US tax rules for buying escrow Treasuries.

## Verdicts in one screen

- **Claim 1: CHANGE.** The name is right: the CFA curriculum calls it "the standard for measuring the total cost of
  the trade", Meketa (2026) "the most comprehensive measure of transition success", Keim and Madhavan "the most natural
  method" (rows 7, 29, 32). But WInS sits nearer Perold's "paper" than his "reality": on paper you trade "with no price
  impact and free of all commissions", and a simulated order moves no price (row 1). Mapped, Keel arithmetic: fees $200,
  equal to the ticket file's estimate (rows 11-12); spread, not charged by WInS, estimated at about $77 (row 27);
  opportunity cost $0, all eleven trades filled and every Treasury holding at its target units (rows 5, 14); delay, a
  price move whose sign depends on the start date: the funds filled $558 below the 2 Oct closes the targets used, while
  the ten payments' cost rose $572 from 5 to 7 Oct (rows 9-10). The single number: "$200 of fees, as estimated, with
  nothing left unbought"; about $280 (0.09% of $300,000) only as a labelled estimate.
  - Judge's note: a reader expects a simulator to flatter execution. By Perold's own definition it cannot show slippage
    at all, so the honest claim is completeness and fees, and the price drift is told only as the reason VT is 167.
- **Claim 2: CHANGE.** ETFs: desks use the bid-offer midpoint when the order arrives (Rule 600) and the premium to NAV
  with a 30-day median spread (Rule 6c-11); WInS recorded neither, but Laura can check both for free (rows 15-16).
  Bonds: desks use paid evaluated prices or competing dealer quotes (rows 23, 25), and none is public for an old
  Treasury: no trade tape (FINRA 6750(d)(5); Treasury's advisers still asking in Aug 2026), no printed markup (Rule 2232)
  (rows 18-19), and the par curve is built from bid-side quotes on the newest issues (row 17). So the 25-basis-point
  band is not a cost measure. It is the staleness and error filter the bond-market standard-setter asks for (row 22),
  sized at 6.9 times normal Treasury scatter and 1.22 times the December 2008 peak, and it caught stale screen prices
  25-31 times normal scatter (row 20). All five stop rules map onto the SEC's rule 15c3-5 controls (row 21).
  - Judge's note: "within a quarter of a percentage point" sounds loose. Against the Treasury market's own noise, every
    genuine price would have passed it in the worst week of 2008, and both stale quotes still failed it.
- **Claim 3: KEEP, sharpened.** Filed transition reports open with completion, then cost against the pre-trade
  estimate with a range, then "the main driver of the difference" (Westminster 2025, RBKC 2026, Clearwater 2010; rows
  11, 14, 33). The measure "does not consider what happens to the target securities after they are purchased" (row 32),
  and the build itself is a "performance holiday" (row 31). 2.5 borrows four lines: completion; $200 against $200; VT
  167 against 164 and why (row 13); then the story of buying it, in Pensions UK's order.
  - Judge's note: Wharton's ban on WInS gains is the profession's own rule for a build, so 2.5 loses nothing by
    obeying it.
- **Claim 4: CHANGE into a two-sentence statement (row 36).** (a) WInS prices and fees: the portfolio measured what
  was bought, in what order and at what price against the curve, never what a dealer would charge; (b) two-thirds
  scale: fixed fees and $1,000 bond lots do not scale (row 12; NUMBERS 8m); (c) later returns: the clock stops at the
  last fill (rows 31-32; GIPS in Q76-021). Any drift figure carries its start date (row 10). For Laura, about $75-$105
  would sit hidden in prices on $300,000 at normal spreads (Keel arithmetic), small beside the year's $37,625 swing in
  the ten's cost (NUMBERS 8b). The curve check is her one public yardstick, told as how IPS l.13's "whichever works
  best for each year" is carried out, never as a new IPS rule.
  - Judge's note: the largest limit is the calendar, not the simulator. The cost that mattered was the rate level on
    the day, which is why the IPS has its completion clause.

## Rows for the store

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Perold's picture of "paper" trading fits WInS better than his "reality": on paper "transactions occur by mere stroke of the pen. You can transact at all times in unlimited quantities with no price impact and free of all commissions"; "Reality involves the cost of trading and the cost of not trading" | Perold (1988), opening pages (Streetwise reprint, 1998, pp. 106-111) | PROCESS, PRESENTATION | KNOWN | A simulated order moves no market price, and WInS filled every order; it charged only $25 or $10 a trade (NUMBERS 8g) and capped size at twice daily volume (COMPETITION s.4). So 2.5 claims what a simulator can measure (every target bought, $200 of fees, prices checked against the curve), never low slippage | Keel's reading of how WInS fills (COMPETITION l.87: US orders "fill in real time"; bonds at end-of-day prices, tickets.md order notes); whether WInS fills at the bid, offer or last price is UNVERIFIED | VERIFIED (read at source, 16 Nov 2026: the reprint's opening pages; rest paywalled) | no | This run: degruyterbrill.com doi 10.1515/9781400829408-014 |
| 2 | Perold's gap was huge for a high-turnover strategy: 1965-1986 the Value Line Fund beat the market by 2.5% a year while the paper portfolio of its rankings, rebalanced weekly, beat it by "almost 20% a year"; 1979-1991, 26.2% against 16.1% a year, though the fund made "the same trades ... with only a slight delay" | Perold (1988); Leinweber (2002), Caltech SSWP 1135 | PROCESS, LADDER | KNOWN | The shortfall grows with turnover. Laura's plan has three builds in six years (Jan 2027, Jan 2028, the 2031 move, NUMBERS 8r) and holds to the end (IPS l.13), so its exposure to Perold's gap is small by design: one clause in 2.5 or 3e, never a boast | Weekly stock picking, unlike a Treasury ladder; the two windows differ; Value Line's own projections were poor (store Q6b-028) | VERIFIED (read at source, 16 Nov 2026) | no | This run: degruyterbrill.com; divisions-prod.s3.amazonaws.com wp1135 |
| 3 | Leinweber's checklist: paper portfolios "incur no commissions, no taxes, no bid-ask spreads, no market impact, and no opportunity costs"; "The best way to measure transactions costs is to look at the difference between real and paper portfolios" | Leinweber (2002) | PROCESS, PRESENTATION | KNOWN | 2.5's five-line cost account: commissions $200 (NUMBERS 8g); taxes out of scope (case); spreads estimated, not charged by WInS (row 27); market impact none in a simulator (row 1); opportunity cost $0, nothing left unbought (row 14) | The account is of the WInS portfolio; Laura's January 2027 purchase pays real spreads (row 36) | VERIFIED (read at source, 16 Nov 2026) | no | This run: divisions-prod.s3.amazonaws.com wp1135 |
| 4 | Perold's method is to "run a paper portfolio alongside your real portfolio" holding your "wish list" of decisions "just before you try to implement them", managed under the same restrictions | Perold (1988) | PROCESS, LADDER | KNOWN | The Portfolio tab's target units at 2 Oct closes (portfolio.csv l.20-31) are Perold's wish-list portfolio, set before the first order; the WInS fills (snapshot l.22-32) are the real one. It gives 2.5's targets column its professional name (Q29 row 12 gave it the pilot name) | The tab was exported 14 Oct, after the fills (Q29 row 12); Perold's paper book runs on, the team's stops at the last fill | VERIFIED (read at source, 16 Nov 2026; repo files) | no | This run: degruyterbrill.com; repo portfolio.csv |
| 5 | Perold's Appendix B in a formula: shortfall = execution cost (each trade's price less the start price, times the amount traded) + opportunity cost (the paper return times what was never bought); the window "must span the time over which the order is executed"; benchmark prices "can be either trade prices or quote midpoints" | Hendershott, Jones & Menkveld (2013), following "Perold (1988, Appendix B)" | PROCESS | KNOWN | Caplet's second term is zero: real units equal paper units for all ten Treasury holdings and VT exceeded its target (NUMBERS 8m), so the whole shortfall is fees plus price moves inside the window, from the 2 Oct prices to the last fill | Re-stated "with a few notational changes"; Perold's appendix itself not read | VERIFIED (read at source, 16 Nov 2026: Hendershott et al.); Perold's appendix UNVERIFIED (paywalled) | no | This run: faculty.haas.berkeley.edu chapter_ELOv5.pdf |
| 6 | In the paper book "All trades ... are assumed to be made at benchmark prices"; the quote midpoint when the decision was made "is probably the most common benchmark", VWAP "the second most common"; for orders never filled, "impute a fill at the closing price" | Hasbrouck (2015), slides 4-10, 27 | PROCESS | TEXTBOOK | Names the benchmark the team used (closing prices on the decision day, 2 Oct) and the one a desk prefers (the midpoint at each order), which WInS screens did not record; 2.5 says "against the prices the targets were set on", never "against the market" | Teaching notes for shares; no bond benchmark in them | VERIFIED (read at source, 16 Nov 2026) | no | This run: pages.stern.nyu.edu Hasbrouck STPPTradingCosts.pdf |
| 7 | The CFA curriculum: "The implementation shortfall measure is the standard for measuring the total cost of the trade", split into delay, execution and opportunity cost; funds "whose valuation is calculated using closing prices" "typically select the closing price post-trade benchmark" | CFA Institute (2026a), Trade Strategy and Execution | PROCESS, PRESENTATION | TEXTBOOK | The name is right for 2.5 and a Wharton judge will know it; the team's reference prices were closes, the benchmark the curriculum gives for books valued at the close | Per-order measure for managers seeking returns; the page gives no bond or ETF benchmark | VERIFIED (read at source, 16 Nov 2026) | no | This run: cfainstitute.org refresher readings 2026 |
| 8 | Delay is its own part: "the cost associated with not submitting the order to the market" at "the time of the portfolio manager's investment decision"; Wagner and Edwards (1993) put trade delay at 0.20% of value in liquidity-neutral markets, though the evidence is "minimal and mixed" | CFA Institute (2026a); Steil (2002) citing Wagner & Edwards (1993); Supit (2020) | PROCESS | KNOWN | The targets were set on 2 Oct closes and the orders went in on 6-7 Oct ET (the planned day moved, Q29 row 14), so most of the gap between sheet and fills (row 9) is delay: market movement, not execution | Wagner and Edwards read only through Steil and Supit; share-market data | VERIFIED (read at source, 16 Nov 2026: CFA, Steil, Supit); Wagner & Edwards UNVERIFIED (secondary only, paywalled) | no | This run: cfainstitute.org; pricing.free.fr JPM_Steil.pdf; thesis.eur.nl Supit.pdf |
| 9 | Keel arithmetic: the six funds filled $557.58 below the 2 Oct closes the targets were set on (five iBond funds -$507.48, between 18 and 51 basis points each; VT -$50.10 on 167 shares) | portfolio.csv l.20-30 (2 Oct closes); WInS snapshot 23 Oct l.22-32 ("Paid") | PROCESS, LADDER | NICHE | The delay part of the build in dollars; a price move, so 2.5 uses it only to explain VT's 167 (row 13), never as money saved | A WInS gain in Wharton's terms; no skill in it (NUMBERS 8b: "luck of timing"); bond drift not computed (the sheet's bond price basis is unclear, Gaps) | VERIFIED (read at source, 16 Nov 2026: repo files); Keel arithmetic | Risk: told as a saving or gain it breaks Wharton's "WInS gains are never evidence" | This run: repo portfolio.csv; competition/wins snapshot |
| 10 | The start date sets the sign: from the 2 Oct closes the funds came in $558 cheaper (row 9); from the year's cheapest close, 5 Oct, the ten payments' cost had risen $572 by 7 Oct (NUMBERS 8b); practitioners warn the shortfall can be "manipulated ... by choosing when to begin the performance calculation" | NUMBERS 8b; row 9; Pensions UK (2014), tip 8 | PROCESS, PRESENTATION, CERTAINTY | NICHE | Evidence for SKELETON's 2.5 aha, "built to need the year, not the day": a few days' drift swings about $570 either way, so 2.5 prints no drift figure without its start date, and the risk sits with the rate level, answered by the 2028 completion (IPS l.13) | Two different measures (six funds' fills against a model value of the ten); approximate | VERIFIED (read at source, 16 Nov 2026); Keel arithmetic | no | This run: pensionsuk.org.uk 0385; NUMBERS 8b |
| 11 | The fees met their pre-trade estimate to the dollar: the ticket file's per-order commissions ($25 on each of six funds, $10 on each of five bonds) add to $200, and WInS charged $200; filed reports print the same line (Northern Trust for Clearwater, 2010: commissions $21,572 against $21,571 estimated) | archive/rab/trades/tickets.md (Commission column); NUMBERS 8g; City of Clearwater (2010) | PROCESS, PRESENTATION | NICHE | 2.5's "cost against estimate" line in dollars: "$200 of fees, as planned" | Fixed fees always match their estimate and test nothing; the FCA warns estimates can be set high "to ensure a good performance relative to the chosen benchmark" (TR14/1); here the estimate was the fee schedule, so say it plainly and claim nothing for it | VERIFIED (read at source, 16 Nov 2026) | no | This run: edocuments.myclearwater.com id 288670; fca.org.uk TR14/1; repo tickets.md |
| 12 | Keel arithmetic: a fixed fee bites small orders: $25 was 2.6 basis points of IBTM's $97,490 but 10.7-12.6 on the four smaller iBond funds; $10 was 5.2-6.7 on each bond; 9.4 on VT; 6.7 on the whole $300,000 | NUMBERS 8g (amounts at cost); COMPETITION s.4 (fees) | PROCESS, LADDER | NICHE | Why fees are among what the scale model cannot show (SKELETON 2.1): at $450,000 and her own broker's prices the share differs; 2.5 says "calculated, not measured" if it says anything | Laura's broker fees are not in the repo; none assumed | VERIFIED (read at source, 16 Nov 2026); Keel arithmetic | no | This run: NUMBERS 8g |
| 13 | Keel arithmetic: the build's price drift landed in VT and cash, never in promised money: the iBond funds came in $507 under the sheet, the three extra VT shares cost $476.49, and cash ended $558.79 above the sheet's estimate ($3,513.79 against $2,955), because VT was sized from the cash then left and bought last | portfolio.csv l.30, l.34; snapshot; NUMBERS 8g, 8m; TNA l.23 | CEILING, PROCESS, LADDER | NICHE | The "167 / 164" clause with a reason a judge can check: the last order took up the build's price noise, and it sits in VT, "the only investment not standing between Laura and a payment deadline" (TNA l.23), while the ten Treasury holdings were bought at exactly their target units | The figures need not net (bonds and accrued interest moved too); approximate; the extra cash is not a promise either | VERIFIED (read at source, 16 Nov 2026); Keel arithmetic | no | This run: repo portfolio.csv, snapshot, TNA |
| 14 | Filed transition reports open with completion: "Completion was 65% by the end of the wider restructure benchmark point, and 100% after 3 full days of trading" (RBKC 2026); "trading fully complete after 4 days" (Westminster 2025) | BlackRock TM for RBKC (2026); BlackRock TM for Westminster (2025) | PROCESS, PRESENTATION | NICHE | 2.5's first line in the same form: all eleven trades filled, all ten Treasury holdings at exactly their target units, VT above target, no order open at the freeze (NUMBERS 8m); Perold's opportunity cost is therefore $0 | Four orders were cancelled and placed again (snapshot), so completion counts filled trades, not orders sent | VERIFIED (read at source, 16 Nov 2026) | no | This run: rbkc.gov.uk s34570; westminster.moderngov.co.uk s70514 |
| 15 | The regulator's arrival benchmark for shares and ETFs: effective spread is "double the amount of difference between the execution price and the midpoint of the national best bid and national best offer at the time of order receipt" | 17 CFR 242.600(b); CFA Institute (2025b) | PROCESS | KNOWN | The professional measure for the six fund trades needs the bid and offer at each order, which WInS neither showed nor kept; 2.5 can cite only the funds' published median spreads (Q17 row 35) and must call that an estimate | CFA: effective spread is "a poor estimate of actual transaction costs when large orders have been filled in many parts" (not Caplet's case: one order each) | VERIFIED (read at source, 16 Nov 2026) | no | This run: ecfr.gov 17 CFR 242.600; cfainstitute.org |
| 16 | Every ETF must post each business day its net asset value, market price and premium or discount, a table of days at a premium or discount, and a median bid-ask spread taken from the best bid and offer "as of the end of each 10 second interval during each trading day of the last 30 calendar days" | 17 CFR 270.6c-11(c)(1)(ii), (iii), (v) | LADDER, MOVE2031, PROCESS | KNOWN | A free public check before each iBond fund purchase (Jan 2027, Jan 2028, the 2031 move): price against yesterday's NAV and against the fund's usual spread; the team's 2026 fund checks were a price ceiling only (tickets "Max price") | Yesterday's NAV, not today's; Q26 holds the 2% statement and Q17 row 35 the figures, so only the method is new | VERIFIED (read at source, 16 Nov 2026) | no, if told as how IPS l.13's "whichever works best" is carried out; a new IPS rule would be | This run: law.cornell.edu 17 CFR 270.6c-11 |
| 17 | The yardstick the team used is a quote curve, not a trade curve: Treasury's par curve uses "indicative, bid-side market price quotations (not actual transactions) for the most recently auctioned securities", taken by the New York Fed "at or near 3:30 PM" | U.S. Department of the Treasury (2025), Treasury Yield Curve Methodology | LADDER, CERTAINTY, PROCESS | NICHE | None of Caplet's five bonds is among the newest bonds the curve uses, and a buyer pays the offer, so each should sit a few basis points off the curve: the right test is a band, not a point (2.6-8.8 at the fills, Q17) | WInS bonds fill at end-of-day prices, the curve is read at 3:30 PM: a timing gap inside the band | VERIFIED (read at source, 16 Nov 2026) | no | This run: home.treasury.gov yield curve methodology |
| 18 | No public tape exists for the bonds Caplet bought: since 25 Mar 2024 FINRA publishes single Treasury trades only for on-the-run coupons, at day's end, and none for a Treasury "other than an On-the-Run Nominal Coupon"; in Aug 2026 Treasury's advisory committee was still asking whether to publish "near off-the-runs" | FINRA Rule 6750(c)-(d); SEC (2024) approval order; FINRA (n.d.) TRACE dissemination page; TBAC charge Q3 2026; CFA Institute (2026a) | LADDER, PROCESS, CERTAINTY | NICHE | A retail buyer of an old bond in January 2027 cannot look up what others paid that day; the CFA text adds that bonds trade in "a bilateral, dealer-centric market structure", "especially" thin for "off-the-run bonds"; so the public curve is the yardstick she has (row 36) | Daily aggregate volumes are published; dealers and paid services see more | VERIFIED (read at source, 16 Nov 2026) | no | This run: finra.org Rule 6750; federalregister.gov 2024-02804; home.treasury.gov TBAC Q3 2026 |
| 19 | No markup is printed either: FINRA's 2016 rule putting the dealer's markup on retail bond confirmations covers corporate and agency debt and "would not apply to U.S. Treasury Securities" | SEC (2016), Release 34-79346, n.12 | PROCESS, LAURA | NICHE | Laura's confirmation for a Treasury will not show a markup, so the cost is hidden in the price; checking the price against the curve before buying is the only check she can make herself (3e; 2.5's "what WInS could not show") | Later amendments not read; FINRA Rule 2121 on fair markups still binds dealers (not read at FINRA) | VERIFIED (read at source, 16 Nov 2026) | no | This run: sec.gov 34-79346.pdf |
| 20 | Keel arithmetic on Hu, Pan and Wang: Treasury yields scatter about a fitted curve by about 3.61 basis points in normal times ("comparable to the average bid ask yield spread of 2 basis points"), peaking at 20.47 on 10 Dec 2008; the team's 25-basis-point band is 6.9 times normal scatter and 1.22 times the 2008 peak; the fills sat at 0.7-2.4 times normal scatter; the two stale screen prices (111 and 92 basis points off, SKELETON l.248) at 31 and 25 times it | Hu, Pan & Wang (2013), JF 68(6), and NBER WP 16468; SKELETON l.248; Q17 (2.6-8.8 basis points) | LADDER, PROCESS, CERTAINTY | NICHE | The band was wide enough that no genuine Treasury price would have failed it even in the worst week of 2008, and narrow enough to catch both stale quotes many times over: a calibrated filter, said as "a quarter of a percentage point" (SKELETON 2.5) | Their noise is an average across 1-10-year bonds on a zero curve; Caplet's bonds are 10-15 years and were checked on the par curve; one bond can stray more than the average | VERIFIED (read at source, 16 Nov 2026: paper excerpts); Keel arithmetic | no | This run: web.mit.edu HuPanWang13.pdf; nber.org w16468 |
| 21 | The five stop rules are the SEC's market-access controls in miniature: rule 15c3-5 makes brokers block orders that exceed "pre-set credit or capital thresholds" (cash "Never below $1,000", worst-case cash), "erroneous orders ... that exceed appropriate price or size parameters" (max price, the curve band, the 1% total band, the 10x/1,000x unit test) or "indicate duplicative orders" (no repeats), and orders in securities a person "is restricted from trading" (IBTN "never a buy") | 17 CFR 240.15c3-5(c)(1)(i)-(ii), (c)(2)(ii); tickets.md l.7-13 | PROCESS, PRESENTATION | NICHE | One clause in 2.5 (buying it): every order passed the same kinds of check a US broker must run before an order reaches the market; it answers "is this a student checklist?" | The rule binds brokers, not investors; the team's checks were manual; whether each rule was read aloud is not recorded (Q29 row 13) | VERIFIED (read at source, 16 Nov 2026) | no | This run: ecfr.gov 17 CFR 240.15c3-5; repo tickets.md |
| 22 | The bond-market standard-setter asks first that price data be reliable: processes must "ensure that data is not stale or erroneous"; "Given the episodic nature of transaction data in most FICC markets", execution checks "may rely heavily on ... quotation information" | FMSB (2020), Measuring execution quality in FICC markets | PROCESS, LADDER | NICHE | Names what the curve band is: a staleness and error test on the one quote WInS showed, FMSB's first test, not a cost measure; it changed one rung's instrument (Q17 row 34) | Written for dealers and institutions with quote streams Caplet lacked | VERIFIED (read at source, 16 Nov 2026) | no | This run: fmsb.com measuring-execution-quality-in-FICC-markets.pdf |
| 23 | Bond desks measure fills against paid evaluated prices: a trade's price "can be compared to our Continuous Evaluated Pricing ... as a benchmark", scored within distributions by "asset class, tenor, trade side, and trade size"; a TCA vendor says bond cost measurement "is all about market data availability" | ICE (n.d.); BestX (2019) | PROCESS | KNOWN | The professional bond benchmark exists but is sold to institutions; neither WInS nor Laura's broker shows it, so the public curve stands in, and 2.5 says "checked against the Treasury curve", never "best execution" | Vendor pages; no Treasury accuracy figures read | VERIFIED (read at source, 16 Nov 2026: excerpts) | no | This run: ice.com best-execution-transaction-analysis; bestx.co.uk 2019 |
| 24 | Bond TCA reads a bond's spread to its benchmark twice: "at order arrival", which "shows the absolute arrival price", and "at the time of execution", which "shows how the spread changed in the intervening period" | Bloomberg Professional Services (2021) | PROCESS, LADDER | NICHE | The team has both readings for each bond: against the curve at the 5 Oct check (-10 to +6 basis points, portfolio.csv l.25-29) and at the fills (2.6 to 8.8, Q17), so 2.5 can say each bond was checked before its order and again after its fill | Different curves and dates; Q17's reading is MODEL; the sheet's sign convention is not stated | VERIFIED (read at source, 16 Nov 2026: excerpt) | no | This run: bloomberg.com professional insights 2021 |
| 25 | Where dealers compete, the bond benchmark is their quotes: one transition manager reports prices "on average 23.7 basis points better than the average of the quotes received", with "on average, eight quotes received per trade" over 923 bond trades | Russell Investments (n.d.), UK pension consolidation case study | PROCESS, LAURA | KNOWN | Caplet saw one price per bond, and Laura holds every holding at one broker (card Q78); with no rival quotes the curve check is the substitute for competition, which is why it belongs in how the plan is carried out | Institutional sizes; the 23.7 basis points is the manager's own claim | VERIFIED (read at source, 16 Nov 2026: excerpt) | no | This run: russellinvestments.com UK case study PDF |
| 26 | Keel arithmetic on the US tax rule for a reasonable broker's fee when buying escrow investments, "the lesser of: (A) $30,000 and (B) 0.2% of the computational base or, if more, $3,000" (before cost-of-living rises): on $300,000 it allows $3,000; Caplet paid $200, a fifteenth of it | 26 CFR 1.148-5(e)(2)(iii) | PROCESS, CERTAINTY | NICHE | An outside, public answer to "is $200 a lot?", from the market that buys Treasuries against fixed payment dates (Q17 row 7; Q54); the same section values a purchase on "the trade date rather than the settlement date" and records "the cost of the most efficient portfolio of State and Local Government Series Securities" | A tax rule on what an issuer may count as an administrative cost, not a market price; Q54-028 and Q54-030 already hold the bidding safe harbour and the SLGS rate | VERIFIED (read at source, 16 Nov 2026) | no | This run: ecfr.gov 26 CFR 1.148-5 |
| 27 | Keel arithmetic, the one number a practitioner would accept: $200 charged, plus estimated half-spreads of about $46 on the iBond funds and $1 on VT (Q17 row 35) and about $30 on the bonds (half the SEC's 0.07% retail Treasury effective spread, Q45 row 26, on $84,801) = about $277, 0.09% of $300,000, with $0 opportunity cost | NUMBERS 8g; Q17 row 35; Q45 row 26; Hasbrouck (2015); 17 CFR 242.600 | PROCESS, PRESENTATION | NICHE | If a judge asks "what did buying it cost?": about $280 in all, $200 charged and the rest estimated; 2.5's text keeps the $200 (SKELETON: dollars only), and the estimate goes in Table 1's note if anywhere | The SEC figure averages all Treasuries, where bills and new issues dominate, so old bonds likely cost more; WInS charged no visible spread; the 0.07% comes from a withdrawn proposal (row 28) | VERIFIED (inputs read at source, 16 Nov 2026); Keel arithmetic | no | This run: repo cards Q17, Q45; NUMBERS 8g |
| 28 | The SEC is "formally withdrawing" its Regulation Best Execution proposal (12 Jun 2025, Release 33-11377) and "does not intend to issue final rules"; its data tables remain SEC staff analysis | SEC (2025), withdrawal notice and Regulation Best Execution page | OTHER, PRESENTATION | KNOWN | Citation fix for Q45 row 26 and row 27 here: cite the 0.07% as data from a 2023 SEC proposal later withdrawn, never as an SEC rule or standard | The data stand; the rule never came | VERIFIED (read at source, 16 Nov 2026) | no | This run: sec.gov 33-11377.pdf; sec.gov regulation-best-execution |
| 29 | Two academics on why the name fits: costs must capture explicit and implicit parts "because the two components are jointly determined", measured "at the level of the entire order"; "Perold's implementation shortfall approach is the most natural method", though "considerable disagreement surrounds how best to measure implicit trading costs" | Keim & Madhavan (1998), FAJ 54(4) | PROCESS | KNOWN | Supports naming it once in 2.5 while claiming only the fees as measured; the rest stays an estimate (row 27) | Institutional share trades of the 1990s | VERIFIED (read at source, 16 Nov 2026: excerpt of the article) | no | This run: hillsdaleinv.com copy of FAJ 1998 |
| 30 | Measuring is for improving, not proving: "The search is not for a meaningless proof of 'best execution,' but for areas that need improvement" | Arnott & Wagner (1990), FAJ 46(6), abstract | PROCESS, PRESENTATION | KNOWN | Sets 2.5's tone (Book 17: evaluate, don't describe): close with what the build changed for January 2027 (the price checked against the curve before every order; one person places orders after a mis-click, told without attribution, SKELETON l.248), not with praise for the fills | Abstract only | VERIFIED (read at source, 16 Nov 2026: abstract page) | no | This run: rpc.cfainstitute.org FAJ 1990 |
| 31 | A build is a "performance holiday": "The period that runs from when an incoming manager has taken control over the transferred assets until the date the manager completes any restructuring activity, and their performance history officially commences"; T-Standard reports split pre-implementation, implementation and post-implementation periods | Russell Investments (2026), glossary; Russell Investments (2025), fixed income ETF case study, Exhibit 1 | PROCESS, LADDER, MOVE2031 | NICHE | Professionals judge a build by cost and completion and count returns only after it ends; Laura's three builds (Jan 2027, Jan 2028, the 2031 move, NUMBERS 8r) are each judged by whether every target was bought at a checked price, never by return | Written for managers whose returns are judged later; Laura's plan is never judged by return at all (its test is each payment covered) | VERIFIED (read at source, 16 Nov 2026: excerpts) | no | This run: russellinvestments.com US TM explained 2026; Russell FI ETF case study 2025 |
| 32 | The measure ends at purchase by design: it "Assumes that the portfolio restructuring is undertaken instantaneously at the outset and at zero cost" and "does not consider what happens to the target securities after they are purchased"; across six providers 0-6.1% of transitions fell outside their expected cost range; in 2026 it "remains the most comprehensive measure of transition success" | Meketa (2019); Meketa (2026) | PROCESS, PRESENTATION | KNOWN | Wharton's "WInS gains are never evidence" is also the profession's rule for a build: 2.5 stops its clock at the last fill and reports nothing after it (no 23 Oct value, no return) | Provider survey, self-reported; the 2019 table's years unclear | VERIFIED (read at source, 16 Nov 2026: excerpts) | no | This run: meketa.com 2019 and 2026 PDFs |
| 33 | A filed post-transition report's spine: completion, then "Cost: The implementation shortfall for the transition was 0.32% versus a pre-trade estimate of 0.18% +/- 0.10%", then "the main driver of the difference", then a T-Charter conclusion; guidance says it should "tell the 'story' of the event", "report on the overall result and highlight any differences from pre-transition estimates" and "report on the strategy deployed" | BlackRock TM for Westminster (2025); Pensions UK (2014); Russell Investments (2023: T-Standard "adopted by the T-Charter as the recommended default") | PRESENTATION, PROCESS | NICHE | What 2.5 borrows inside its 180 words: completion (row 14), cost against estimate ($200 against $200, row 11), the driver of the one difference (VT 167 against 164, row 13), then the story (buying it: the curve check and one owner), in Pensions UK's order | Written for trustees moving hundreds of millions; Caplet needs four lines, not fifteen pages | VERIFIED (read at source, 16 Nov 2026) | no | This run: westminster.moderngov.co.uk s70514; pensionsuk.org.uk 0385; advisorperspectives.com 2023 |
| 34 | Even professionals see market moves swamp execution: one council's 2021 transition cost 206.0 basis points in all, but its trading costs were 32.2 against 32.6 predicted; 168.0 was "Physical opportunity cost", the old portfolio's market move on the trading day | RBKC (2021), Transition report, Investment Committee 24 Feb 2021 | PROCESS, CERTAINTY | NICHE | The report keeps the two apart, and so should 2.5: $200 of fees on one line; the year's $37,625 swing in the ten's cost (NUMBERS 8b) is the plan's problem, answered by the 2028 completion, never charged to execution | Shares, one bad day; Q17 row 3 holds Russell's "rate volatility" line, this adds a filed report showing the split | VERIFIED (read at source, 16 Nov 2026: excerpt) | no | This run: rbkc.moderngov.co.uk 2021 transition report |
| 35 | The asset-management word for what WInS holds: a model portfolio is "A list of investments and transactions for an investment strategy that are not actually held by the portfolio but can be backtested over historical periods and/or run contemporaneously" | State Street Global Advisors (2020); GIPS no-linking already in store Q76-021 | PRESENTATION, PROCESS | KNOWN | The WInS portfolio is a model portfolio run at the time, not built with hindsight: its targets were set before the prices it filled at, the honest strength to claim, while its results stay non-actual (Q76-021; Q29 rows 26-27) | White paper read in part (definitions) | VERIFIED (read at source, 16 Nov 2026: excerpt) | no | This run: ssga.com model portfolio white paper |
| 36 | The limits in two sentences: WInS filled at its own prices and charged only its fees, so the portfolio measured what was bought, in what order and at what price against the curve, never what a dealer would charge; and its clock stops at the last fill, at two-thirds scale. Keel arithmetic: at the funds' and the SEC's normal spreads, Laura's January 2027 purchase would carry about $75-$105 hidden in prices on $300,000 | Rows 1, 18, 19, 27, 32; NUMBERS 8m (scale 300/450); Q17 row 35; Q45 row 26 | PRESENTATION, LADDER, LAURA | NICHE | 2.5's "what WInS could not show" clause (beside the 2028 date) and 3e's limits; $75-$105 against the year's $37,625 swing (NUMBERS 8b) keeps the real risk where the IPS put it, in the rate level, answered by the completion rule (IPS l.13) | Normal-market spreads only; in March 2020 they widened many times (Q45); her broker and fees unknown | VERIFIED (inputs read at source, 16 Nov 2026); Keel arithmetic | no | This run: repo; cards Q17, Q45 |

## Best five for the report

1. **Row 20, 2.5 ("bonds within a quarter of a percentage point").** Turns a loose-sounding number into a calibrated
   one: every genuine price would have passed it in December 2008, and both stale quotes failed it many times over.
2. **Row 21, 2.5 (buying it, one clause).** The five stop rules are the controls the SEC requires of brokers with
   market access, which answers "student checklist?" before a judge asks it.
3. **Row 13, 2.5 (VT "167 / 164").** The last order took up the build's price noise, and it sits in the one holding
   "not standing between Laura and a payment deadline" (TNA l.23): the design shows in the fills.
4. **Row 10, 2.5's aha ("built to need the year, not the day").** The same few days read as $558 saved or $572 lost
   depending on the start date, so the plan rests on the completion clause, not on the purchase day.
5. **Row 33, 2.5's order.** A filed transition report's spine (completion, cost against estimate, the driver of the
   difference, the story) gives the 180 words a professional shape a finance judge recognises.

## Gaps

- Perold (1988) beyond its opening pages: paywalled (De Gruyter, PM Research); Appendix B read only as re-stated by
  Hendershott, Jones and Menkveld (2013).
- Wagner and Edwards (1993), "Best Execution", FAJ 49(1): paywalled; its cost split and 0.20% delay figure read only
  in Steil (2002) and Supit (2020). Steil (2002)'s full author list was not read (the copy is filed under "Steil").
- The bid and offer at each of the six fund orders, and each fund's premium to NAV on the fill days (6-8 Oct ET): not
  found; fund pages show only current tables (also Q17's gap).
- Retail trading costs for old 10-15-year Treasuries in particular: the SEC's 0.07% averages all Treasuries.
- Bond drift against the target sheet not computed: portfolio.csv says bond prices are "clean + accrued" in its note
  but lists clean prices (97.122 and so on) in the bond rows; the basis needs settling before any bond drift figure.
- Register dates: NUMBERS 8b says the orders "filled 7-8 Oct"; 8g says prices paid "on 6-7 Oct (ET)" and 8m a "first
  fill (6 Oct ET)"; the snapshot's times are evening ET, so they may be order times. A T-Standard start date depends on
  which; the lead or numbers owner should settle it before 2.5 names a date.
- How WInS fills (last price, bid or offer; whether its bond prices are refreshed daily): UNVERIFIED (snapshot check 4).
- The T-Charter text itself: read only through Russell, Pensions UK and The TRADE.
- FINRA Rule 2121 (fair markups for dealers): not read at FINRA.
- Hu, Pan and Wang measure 1-10-year bonds; no scatter figure was found for 10-15-year old bonds.
- Not reached (search budget): Quantitative Brokers' history of implementation shortfall; the SSGA white paper beyond
  its definitions; Treynor (1981).

## Sources

- Arnott, R. D., & Wagner, W. H. (1990). The measurement and control of trading costs. *Financial Analysts Journal,
  46*(6). https://doi.org/10.2469/faj.v46.n6.73 (abstract page:
  https://rpc.cfainstitute.org/research/financial-analysts-journal/1990/the-measurement-and-control-of-trading-costs).
  Retrieved 16 Nov 2026.
- BestX. (2019, February 26). *Measuring the unmeasurable?*
  https://www.bestx.co.uk/publications/2019/2/26/measuring-the-unmeasurable. Retrieved 16 Nov 2026.
- BlackRock Transition Management. (2025, November 20). *City of Westminster Pension Fund global equity transition:
  Post-transition analysis*.
  https://westminster.moderngov.co.uk/documents/s70514/Appendix%201%20-%20CoWPF%20Post%20Transition%20Analysis.pdf.
  Retrieved 16 Nov 2026.
- BlackRock Transition Management. (2026, April 21). *Royal Borough of Kensington and Chelsea global equity transition:
  Post-transition analysis*.
  https://www.rbkc.gov.uk/Committees/documents/s34570/appendix%201%20-%20RBKC%20Global%20Equity%20Restructure%20Post%20Transition%20Analysis%20-%2021.04.pdf.
  Retrieved 16 Nov 2026.
- Bloomberg Professional Services. (2021, June 29). *Fixed income TCA: The state of the art*.
  https://www.bloomberg.com/professional/insights/trading/fixed-income-tca-the-state-of-the-art/. Retrieved 16 Nov 2026.
- CFA Institute. (2026a). *Trade strategy and execution* (CFA Program Level III refresher reading, 2026 curriculum).
  https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/trade-strategy-execution.
  Retrieved 16 Nov 2026.
- CFA Institute. (2025b). *Trading costs and electronic markets* (refresher reading, 2026 curriculum).
  https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2025/trading-costs-and-electronic-markets.
  Retrieved 16 Nov 2026.
- City of Clearwater. (2010). *Equity post trade analysis* (prepared by Northern Trust, 11 Aug 2010).
  https://edocuments.myclearwater.com/WebLink/DocView.aspx?dbid=0&id=288670&repo=Clearwater. Retrieved 16 Nov 2026.
- Financial Conduct Authority. (2014). *Transition management review* (Thematic Review TR14/1).
  http://www.fca.org.uk/publication/thematic-reviews/tr14-01.pdf. Retrieved 16 Nov 2026.
- FINRA. (n.d.). *Rule 6750. Dissemination of transaction information* (version valid from 25 Mar 2024).
  https://www.finra.org/rules-guidance/rulebooks/finra-rules/6750. Retrieved 16 Nov 2026.
- FINRA. (n.d.). *TRACE reporting and dissemination*.
  https://www.finra.org/filing-reporting/trade-reporting-and-compliance-engine-trace/trace-reporting-timeframes.
  Retrieved 16 Nov 2026.
- FINRA. (2024, March 8). *Regulatory Notice 24-06: FINRA adopts amendments to enhance post-trade transparency in the
  U.S. Treasury securities market*. https://www.finra.org/rules-guidance/notices/24-06. Retrieved 16 Nov 2026.
- FMSB. (2020, September). *Measuring execution quality in FICC markets* (Spotlight review).
  https://fmsb.com/wp-content/uploads/2025/04/measuring-execution-quality-in-FICC-markets.pdf. Retrieved 16 Nov 2026.
- Hasbrouck, J. (2015). *Chapter 8: Transaction costs* [Class notes, Securities trading: Principles and procedures].
  NYU Stern. https://pages.stern.nyu.edu/~jhasbrou/Teaching/POST%202015%20Fall/classNotes/STPPTradingCosts.pdf.
  Retrieved 16 Nov 2026.
- Hendershott, T., Jones, C. M., & Menkveld, A. J. (2013). *Implementation shortfall with transitory price effects*
  [Working paper]. https://faculty.haas.berkeley.edu/hender/chapter_ELOv5.pdf. Retrieved 16 Nov 2026.
- Hu, G. X., Pan, J., & Wang, J. (2013). Noise as information for illiquidity. *The Journal of Finance, 68*(6),
  2341-2382. https://web.mit.edu/wangj/www/pap/HuPanWang13.pdf; working paper version (NBER WP 16468):
  https://www.nber.org/system/files/working_papers/w16468/w16468.pdf. Retrieved 16 Nov 2026.
- ICE. (n.d.). *Transaction analysis: An anchor in volatile markets*.
  https://www.ice.com/insights/market-pulse/best-execution-transaction-analysis. Retrieved 16 Nov 2026.
- Keim, D. B., & Madhavan, A. (1998). The cost of institutional equity trades. *Financial Analysts Journal, 54*(4),
  50-69. https://www.hillsdaleinv.com/uploads/The_Cost_of_Institutional_Equity_Trades%2C_Donald_B._Keim%2C_Ananth_Madhaven%2C_Financial_Analysts_Journal%2C_JulyAugust_1998%2C_Pages_50-69.pdf.
  Retrieved 16 Nov 2026.
- Leinweber, D. J. (2002). *Using information from trading in trading and portfolio management: Ten years later*
  (Social Science Working Paper 1135). California Institute of Technology.
  https://divisions-prod.s3.amazonaws.com/hss70/working_papers/wp1135.pdf. Retrieved 16 Nov 2026.
- Meketa Investment Group. (2019). *Transition management*.
  https://meketa.com/wp-content/uploads/2012/10/Transition-Management-FINAL.pdf. Retrieved 16 Nov 2026.
- Meketa Investment Group. (2026, March). *Transition management update*.
  https://meketa.com/wp-content/uploads/2026/03/MEKETA_Transition-Management-Update.pdf. Retrieved 16 Nov 2026.
- Pensions UK. (2014). *Transition management made simple*.
  https://www.pensionsuk.org.uk/portals/0/Documents/0385-Transition-management-made-simple.pdf. Retrieved 16 Nov 2026.
- Perold, A. F. (1988). The implementation shortfall: Paper versus reality. *The Journal of Portfolio Management,
  14*(3), 4-9. https://doi.org/10.3905/jpm.1988.409150 (opening pages read in the reprint: P. L. Bernstein & F. J.
  Fabozzi (Eds.), *Streetwise: The best of The Journal of Portfolio Management* (pp. 106-111), Princeton University
  Press, 1998, https://www.degruyterbrill.com/document/doi/10.1515/9781400829408-014/html). Retrieved 16 Nov 2026.
- Royal Borough of Kensington and Chelsea. (2021, February 24). *Transition report* (Investment Committee, agenda item
  A5, appendix 1).
  https://rbkc.moderngov.co.uk/Committees/Data/Investment%20Committee/202102241830/Agenda/A5%20Appx%201%20-%20Transition%20Report.pdf.
  Retrieved 16 Nov 2026.
- Royal Borough of Kensington and Chelsea. (2026, July 9). *Active equity update* (Investment Committee report).
  https://www.rbkc.gov.uk/Committees/documents/s34569/Active%20equity%20update%20cover%20report.pdf. Retrieved 16 Nov
  2026.
- Russell Investments. (2023, November 2). *Confessions of a transition manager*. Advisor Perspectives.
  https://api.advisorperspectives.com/commentaries/2023/11/02/confessions-transition-manager. Retrieved 16 Nov 2026.
- Russell Investments. (2025). *Case study of a fixed income ETF transition during volatile markets*.
  https://russellinvestments.com/content/dam/ri/files/us/en/institutions/case-studies/case-study-fixed-income-transition.pdf.
  Retrieved 16 Nov 2026.
- Russell Investments. (2026). *Transition management explained* (US ed.).
  https://russellinvestments.com/-/media/files/us/insights/institutions/implementation/transition-management-explained.pdf.
  Retrieved 16 Nov 2026.
- Russell Investments. (n.d.). *Managing transition costs when consolidating pension funds* [Case study].
  https://russellinvestments.com/content/dam/ri/files/uk/Transition%20management%20case%20study.pdf. Retrieved 16 Nov
  2026.
- Securities and Exchange Commission. (2016, November 17). *Order granting accelerated approval of a proposed rule
  change, as modified by Amendment No. 1, relating to FINRA Rule 2232 (Customer Confirmations)* (Release No.
  34-79346). https://www.sec.gov/rules/sro/finra/2016/34-79346.pdf. Retrieved 16 Nov 2026.
- Securities and Exchange Commission. (2024, February 12). Self-regulatory organizations; Financial Industry Regulatory
  Authority, Inc.; Order approving proposed rule change relating to dissemination of information on individual
  transactions in U.S. Treasury securities and related fees. *Federal Register, 89*(29).
  https://www.federalregister.gov/documents/2024/02/12/2024-02804/self-regulatory-organizations-financial-industry-regulatory-authority-inc-order-approving-proposed.
  Retrieved 16 Nov 2026.
- Securities and Exchange Commission. (2025, June 12). *Withdrawal of proposed regulatory actions* (Release No.
  33-11377). https://www.sec.gov/files/rules/final/2025/33-11377.pdf; Regulation Best Execution page:
  https://www.sec.gov/rules-regulations/2025/06/regulation-best-execution. Retrieved 16 Nov 2026.
- State Street Global Advisors. (2020). *Model portfolio performance* [White paper].
  https://www.ssga.com/library-content/announcement/etfs/au/Best_Practices_Model_Portfolio_Performance_White_Paper.pdf.
  Retrieved 16 Nov 2026.
- Steil (2002; full author list not read). Controlling institutional trading costs. *The Journal of Portfolio
  Management* (Spring 2002). http://pricing.free.fr/docs/vwap/JPM_Steil.pdf. Retrieved 16 Nov 2026.
- Supit (2020). *Transaction costs and short term price signals: A happy marriage* [Master's thesis, Erasmus
  University Rotterdam]. https://thesis.eur.nl/pub/52353/Supit.pdf. Retrieved 16 Nov 2026.
- The TRADE. (2007, December 6). *Code of best practice for transition managers a "significant step forward"*.
  https://www.thetradenews.com/code-of-best-practice-for-transition-managers-a-significant-step-forward. Retrieved 16
  Nov 2026.
- Treasury Borrowing Advisory Committee. (2026). *Charge, Q3 2026: What incremental steps should the Treasury consider
  towards additional transparency of secondary market transactions?* U.S. Department of the Treasury.
  https://home.treasury.gov/system/files/221/TBACCharge1Q32026.pdf. Retrieved 16 Nov 2026.
- U.S. Department of the Treasury. (2025, February 18). *Treasury yield curve methodology*.
  https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics/treasury-yield-curve-methodology.
  Retrieved 16 Nov 2026.
- Risk management controls for brokers or dealers with market access, 17 C.F.R. § 240.15c3-5.
  https://www.ecfr.gov/current/title-17/section-240.15c3-5. Retrieved 16 Nov 2026.
- NMS security designation and definitions, 17 C.F.R. § 242.600 (definition of average effective spread).
  https://www.ecfr.gov/current/title-17/chapter-II/part-242/subject-group-ECFRac68bdd026a46db/section-242.600.
  Retrieved 16 Nov 2026.
- Exchange-traded funds, 17 C.F.R. § 270.6c-11. https://www.law.cornell.edu/cfr/text/17/270.6c-11. Retrieved 16 Nov
  2026.
- Yield and valuation of investments, 26 C.F.R. § 1.148-5. https://www.ecfr.gov/current/title-26/section-1.148-5.
  Retrieved 16 Nov 2026.
- Repo files read (team record and register, not references): `caplet/google_drive/sheets/portfolio_and_trading_notes/portfolio.csv`
  l.20-34; `competition/wins/2026-10-23_snapshot.md` l.22-58; `archive/rab/trades/tickets.md` l.7-40;
  `keel/final_report/NUMBERS.md` 8b, 8g, 8m, 8r; `keel/final_report/SKELETON.md` l.41, 225, 246-248; cards Q17, Q29, Q45.
