# Bond desk: 3c's precision (Sun 15 Nov 2026, evening)

Planning notes for the 27 Nov session, not report sentences. One reader, a fixed-income portfolio manager, read blind
(nothing under `research/panel/`, no SCORECARD, LESSONS or ARGUMENT_LOG). "Keel arithmetic" marks a sum of my own on
register figures; "desk re-run" marks a calculation I ran on the register's own engine (`numbers/engine.py`,
`completion.py`, `plan.py`, seed 2033, 200,000 simulated futures) in a scratch script, not added to the register.

## What I read, and what I checked at source
- Case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (l.94-120: the reserve is set aside at the
  beginning of 2033 before the contribution; the range must carry a stated confidence).
- Frozen IPS: `FINAL_IPS_as_submitted.txt` l.13-17 (l.15: "whose payout is the bare minimum", "the bottom will remain
  constant", "Before you meet co-sponsors in 2031, the other half will move into Treasuries", "whatever figure you
  choose is money you already own").
- SKELETON rows 3c (l.45 density cut, l.203 conceit, l.235 reservoir), 3e (l.47, l.237), and for dates 3a l.233, 3b
  l.44, 3d l.46 and l.236, Book 17 rank 5 (l.91); WORDS (all); `exhibits/tables.md` Table 2 (l.60-80) and Table 3
  rows 4-5 (l.93-94); NUMBERS 0 (l.62-65), 3 (l.193-241), 4 (l.243-368), 8l (l.1103-1198), 8p (l.1433-1488).
- Code behind the rule: `numbers/completion.py` l.413 (`_PW`), l.428-441 (`zero_per_dollar`), l.444-465 (`rule`);
  `numbers/engine.py` l.150-152 (fund flows and price); `numbers/plan.py` l.78 (the floor's modelled payout).
- **IBTM fund page**, https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf, read Sun
  15 Nov 2026 (the copy served carried data "as of Oct 23, 2026"): Expense Ratio **0.07%**, "Fees as stated in the
  prospectus", no separate net figure or waiver; premium/discount 0.06 (units not printed; read as 0.06%); 30-day
  median bid/ask spread 0.05%; distributions monthly; weighted average coupon 3.50, weighted average maturity 5.69
  years, yield to maturity 4.86%; "the Funds do not seek to return any predetermined amount".
- **IBTM summary prospectus**,
  https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf, read Sun
  15 Nov 2026 (prospectus and SAI "both dated February 27, 2026"): fee table management fee 0.07%, other expenses
  0.00%, acquired fund fees 0.00%, total 0.07%, waiver (0.00)%; "will terminate on or about December 15, 2032, at which
  time it will distribute its remaining net assets to shareholders", under "a plan of liquidation"; "does not seek to
  return any predetermined amount at maturity or in periodic distributions"; in the last six months proceeds are
  "typically ... reinvested ... in investments already in the Underlying Index" or "other cash and cash equivalents",
  and "To the extent that the Fund invests in money market or similar funds, it will incur the fees and expenses of
  such funds"; "By December 15, 2032, the Fund is expected to consist almost entirely of cash"; BFA pays operating
  expenses except "(i) the management fees, (ii) interest expenses, (iii) taxes, (iv) expenses incurred with respect
  to the acquisition and disposition of portfolio securities, (v) distribution fees or expenses, and (vi) litigation
  expenses and any extraordinary expenses", and acquired fund fees are excluded too; it "may lend securities
  representing up to one-third of the value of the Fund's total assets".
- So item 1's first half holds at source: IBTM's fee is 0.07% today, no waiver.

## Findings

### HIGH

**H1. "Already counted" is false for both ends: the range rule charges almost none of the 0.07% fee.**
- Plan: SKELETON l.45, "at the top unless the funds' other costs, beyond their 0.07% yearly fee, which is already
  counted, take more than 0.5% of their value by the end" and "'funds' own costs' said as 'the funds' other costs',
  since the 0.07% fee is already counted"; WORDS l.56, "the 0.5% held back for fund costs beyond the 0.07% fee";
  NUMBERS l.64, "its remaining coupons and principal less the fund fee".
- Register and code: `zero_per_dollar` (completion.py l.428-441) divides the after-fee flows by `nav`, the present
  value of the same after-fee flows (l.436). The fee then cancels from the trade day on; only the fee on the principal's
  five-month cash wait (`_PW`, l.413) survives. A real ETF's net asset value is the market value of its gross holdings,
  and the buyer pays the fee out of it afterwards. The ladder's $302,287 (NUMBERS l.203, engine price 1.0 for after-fee
  flows bought 1 Jan 2027) and the modelled payouts (plan.py l.78, fee for the full term) do count the fee correctly;
  the range rule does not.
- Size (desk re-run): the engine's zero-interest payout per $1 is 1.211695 for the floor bought January 2028 against
  1.208257 with the fee charged from purchase, so 0.284% of value; for the moved half bought 1 Jan 2031, 0.101%. In
  dollars at the centre: about $280 on the unrounded bottom ($98,729 to about $98,449) and $300 on the unrounded top
  ($118,443 to about $118,143). Only about 10% of the floor's fee and 23% of the moved half's is in the rule now.
- What it breaks: the cost margin. NUMBERS 8l l.1138 says fund costs up to 0.50% are covered in every simulated future;
  with the fee charged, other costs up to about 0.22% are covered in every one (bottom 0.216%, top 0.219%, desk
  re-run). At 0.5% of other costs the top is not owned at zero interest in about 6% of simulated futures (largest gap
  about $395), and in one future in 200,000 the contribution falls below the bottom. NUMBERS l.205's "3.83%" loss is
  understated the same way (a fee-charged payout set against a nearly fee-free zero-interest payout), as are section
  3's friction table (l.229-237), 8l's margins (l.1129-1138, l.1153-1156) and 8p's unrounded tops (each about $290 high).
- What it does not break: the central stated range ($95,000 to $115,000), the contribution, the house model's 1-in-20,
  median and 1-in-20 points of both ends (unchanged in the desk re-run), and "inside the range unless the US defaults"
  in any share of futures a report would print. About 6% of simulated futures state one end a $5,000 step lower.
- Why a desk objects: the one exception the confidence sentence names is stated at the wrong size, and "already
  counted" is the reason given for it.
- Fix (note): charge the fee from each trade day in `zero_per_dollar` (denominator: market value of the gross holdings;
  numerator: their flows less the fee from the trade day, and on the principal to 15 Dec 2032); re-run sections 3 and 4,
  8i, 8l, 8p and Table 2 (the 1-in-20 points should hold); then "already counted" is true and the 0.5% is for other costs
  alone. If it is not re-run before 27 Nov, the words must change instead: "the funds' costs, their 0.07% yearly fee
  included, ..." and drop "already counted" from SKELETON l.45 and WORDS l.56.

**H2. The top's rounding reads two ways, and one of them gives $110,000.**
- Plan: SKELETON l.45, "the bottom is what the floor pays; the top adds the half of the shares moved into Treasuries;
  ... each from what those Treasury funds pay if cash waiting earns nothing, less 0.5%, rounded down to the nearest
  $5,000"; WORDS l.33, "the top adds the shares moved into Treasuries, each counted at what its bonds pay if no more
  interest is earned, cut by 0.5% and rounded down to $5,000".
- Register: NUMBERS l.209, "Top: the unrounded bottom plus the moved half on the same basis ... less 0.5%, rounded down
  to $5,000"; code l.453, `t_raw = (Fz + Mz) * (1 - haircut)`, rounded once. Rounding down is applied the same way to
  both ends in the code (`down()`), and the top does add the unrounded bottom, so the register is right.
- Why a desk objects: "each ... rounded down" invites rounding the parts. Keel arithmetic: the moved half's
  zero-interest value less 0.5% is $18,494.70 x 1.071332 x 0.995 = about $19,715; rounded down $15,000; plus the
  stated bottom $95,000 is $110,000, against the register's $115,000. The headline top must be reproducible from the
  rule's own words.
- Also missing from 3c's notes: the floor's part of the top is the January 2028 measurement carried unchanged, never
  re-measured in 2031 (NUMBERS l.241: re-measuring cuts 3.27% instead of 4.31% and overstates what is owned in 11% of
  simulated futures).
- Fix (note): one clause in 3c and in WORDS's "The range" row: the top is the bottom's figure before rounding (from
  January 2028) plus the moved half's, each less 0.5%, and the sum rounded down once to $5,000; the bottom is the
  floor's figure rounded down. Never "each rounded down".

### MEDIUM

**M1. The 0.5% is described as costs (good) but its claimants are not budgeted, and one is misnamed.**
- Plan and register: NUMBERS l.65, "an ETF bought above its net asset value, bid-ask spreads, an expense change made
  with notice"; SKELETON l.45, "the funds' other costs". Table 3 row 4 (tables.md l.93) also charges a fund swap's cost
  for the range to it ("the range's from its 0.5%"), and 8l's stricter reading (M3) would take about 0.07%.
- Source: a normal day's purchase friction is about 0.06% premium plus half of a 0.05% spread (fund page, 23 Oct 2026
  data); the prospectus adds costs outside the 0.07%: interest, taxes, portfolio transaction costs, distribution fees,
  litigation and extraordinary expenses, money-market fund fees in the last six months, and securities-lending losses
  on up to a third of assets (no cap on any of these).
- Why a desk objects: (a) with H1 unfixed, the fee silently takes about 0.28 of the 0.5 points, leaving about 0.15%
  for everything above once M3's 0.07% is also charged (Keel arithmetic: 0.5 - 0.28 - 0.07), barely twice a normal
  day's premium and half-spread; (b) "an expense change made with notice" is loose: a rise in the advisory fee
  generally needs a shareholder vote under the Investment Company Act's section 15 (UNVERIFIED for IBTM's agreement;
  read the SAI), while the prospectus's exclusions above can rise without one. Nowhere in 3c, WORDS or NUMBERS is the
  0.5% called a market-risk cushion: that part passes.
- Is 0.5% defensible? Yes for frictions once H1 is fixed and the ends are measured on units held times net asset value
  (M2), because the premium and spread then drop out and 0.5% is several times what is left in a normal market. It is
  not a bound for lending losses or extraordinary costs, which is why 3e names the prospectus clause (SKELETON l.235).
- Fix (note): one line in NUMBERS 0 listing what the 0.5% carries, each with its source and a normal-market size:
  money-market fees in the final months, the T-bill fund's fee on distributions if M3 charges it there, a fund swap
  under Table 3 row 4, costs outside the unitary fee; replace "an expense change made with notice" with "costs the
  prospectus leaves outside the 0.07% fee".

**M2. The basis of each end is in the register but not in 3c's notes or Table 2's note, and the register's basis is a
model device a desk could not execute in 2031.**
- Plan: SKELETON l.45, "Table 2's note names what pays each end too"; tables.md l.78 (Table 2's note items) names the
  curve date and the replays but no rule basis: not the money put in, not the per-$1 zero-interest payout, not the 0.5%,
  not the rounding.
- Register: NUMBERS l.63-64, "the money put into the late-2032 fund times what $1 of the fund's holdings pays on 15 Dec
  2032 if nothing earns interest from the trade day ... priced on the trade day's curve", the holdings being one
  synthetic bond (4.2513%, maturing 4 Jul 2032 in the engine), cautious against IBTM's real 3.50% coupons (l.224, l.366).
- Why a desk objects: "today's market rates" in 3c is the 6 Nov 2026 par curve and a synthetic bond; in 2031 no curve
  is needed. "Money put in" also lets a purchase premium into the figure, which is why the 0.5% has to carry it.
- Fix (note): the 2031 recipe in NUMBERS 0, and its gist in Table 2's note: units of the fund held (from the trade
  confirmation) times the fund's remaining coupons and principal per unit from its published holdings on the trade day,
  undiscounted, less the fee to 15 Dec 2032 and 0.5%, the bottom rounded down, the top as H2; until then, modelled on
  the 6 Nov 2026 par curve with a stand-in holding.

**M3. Where the funds' monthly distributions wait is unstated, and the range rule treats waiting money differently
from 3a's standard.**
- Register: NUMBERS l.62, waiting money sits in a Treasury-bill ETF and "The design test charges 0.15% a year on every
  waiting dollar" (3a's standard); the range rule counts distributions at face (8l l.1178: "The rule counts the funds'
  monthly distributions at face"); charged at 0.15% the floor's zero-interest payout falls $69 and the moved half's $3,
  and the cost covered falls from 0.50% to about 0.43% (l.1181-1183; on top of H1).
- Why a desk objects: two standards for the same cash in one report; IBTM pays monthly (fund page), so about a fifth of
  the floor's payout is cash Laura holds for up to five years.
- Fix (note): either charge the 0.15% in the rule (consistent with 3a) or state that distributions wait as cash in the
  custody account with no fee, and say which once in NUMBERS 0.

**M4. "Short by a few hundred dollars" is not a bound.**
- Plan: SKELETON l.45, "and then short by a few hundred dollars". Register: $429 largest at 0.75%, $881 at 1% (NUMBERS
  l.233-234, 8l l.1130-1132); with H1 fixed, about $839 at 0.75% of other costs (desk re-run).
- Why a desk objects: the shortfall grows with the costs; "a few hundred" holds only up to a level 3c does not name.
- Fix (note): say the rate, not a size: about $120 for each tenth of a percent of value the costs run above the cut
  (Keel arithmetic: 0.1% of the central zero-interest value of both funds, $119,039).

**M5. Table 2's note dates every column to markets before January 2028; only the bottom is.**
- Plan: tables.md l.78, "each row is a different market before January 2028; within each, the bottom is fixed from
  then"; SKELETON l.45, "dated: it is the spread before January 2028".
- Register: the top is fixed at the move (NUMBERS l.327-328, "Good and bad markets before the move change only the
  top"); Table 2 row 2 ("Replay from 2006: shares fall") keeps the central bottom and moves the top and the flexibility,
  so its market differs after January 2028.
- Fix (note): the bottom turns on markets to January 2028, the top on markets to the move before the 2031 meetings,
  her flexibility on markets to January 2033; the same three dates in 3c's spread clause.

**M6. "Before 2031" is not the IPS's date.**
- Plan: SKELETON l.45, "the top when the shares move before 2031" and "higher if share prices rise before 2031"; also
  l.44, l.47, l.72, l.102. The same row later says "'when the shares move' said once as 'before the 2031 meetings'".
- Source and register: IPS l.15, "Before you meet co-sponsors in 2031"; NUMBERS l.245, move "modelled as 1 Jan 2031"
  (a market holiday); Table 3 row 5 (tables.md l.94), "First trading day" (Thu 2 Jan 2031).
- Why a desk objects: "before 2031" reads as by 31 Dec 2030; the top's fixing date is the one date 3c must get right.
- Fix (note): "before the 2031 meetings" everywhere; the modelled date (1 Jan 2031, traded on the first trading day)
  in Table 2's note; the same for the floor (modelled Sat 1 Jan 2028, traded Mon 3 Jan 2028, Table 3 row 5).

**M7. The contribution's date and the cash date disagree across parts.**
- Plan: SKELETON l.236 (3d), "when Laura's contribution is paid in December 2032"; SKELETON l.233 (3a), "the gift is
  cash about 18 Dec 2032" (a Saturday); Figure 1 (tables.md l.42), IBTM cash "Mon 20 to Wed 22 Dec 2032"; Table 2's
  last row (tables.md l.76), "the facility contribution in January 2033"; WORDS l.29, "at the start of 2033".
- Source: the case sets the reserve aside at the beginning of 2033 "before making the first operating payment or
  contributing to the facility" (case l.94-95, l.101).
- Fix (note): one sequence everywhere: the fund ends on or about Wed 15 Dec 2032, its cash reaches Laura about 20 to
  22 Dec 2032, the reserve is set aside at the start of 2033, then the contribution; 3d's close date says "no later than
  January 2033".

### LOW

- **L1. "The bottom is what the floor pays"** (SKELETON l.45; WORDS l.33). The floor pays $103,178 at today's market
  rates (NUMBERS l.253); the bottom is $95,000, its zero-interest value less 0.5%, rounded down (l.254-255). Define the
  bottom by the rule; quote IPS l.15's "bare minimum" rather than paraphrase it.
- **L2. "If no more interest is earned"** survives in WORDS l.33 and SKELETON l.235, the phrasing WORDS l.73 retired
  because each bond's own interest still counts. Use "if cash waiting earns nothing" in both.
- **L3. "Before the move the same condition applies to the bottom"** (SKELETON l.45) suggests a figure with a status
  before anything is stated. Note: from January 2028 the bottom is owned on the same cost condition, though Laura states
  nothing until 2031; after the move it bites only where the range is one figure.
- **L4. "Both funds lose about a fifth"** (SKELETON l.235, reservoir) reads the room above the bottom as a market-loss
  buffer; held to their end, Treasury funds pay less only through a default or costs. Keep it out of the prose.
- **L5. 3d's paragraph notes** (SKELETON l.46) still carry "against a fee of 0.07% a year today", the phrase 3c dropped,
  and "1 simulated future in 200,000 at 0.75%, by $211", a probability rarer than 1 in 100. Bring 3d into line with 3c
  after H1.
- **L6. Scale.** 3c's notes never name the $450,000 plan; Table 2's title does ("Laura's Plan for Both Deposits
  ($450,000)"), and Table 1 shows IBTM at $97,489.95 for "2033 and the floor" at the $300,000 WInS scale. One clause in
  3c ("for the $450,000 plan") stops a judge reading a floor off Table 1.
- **L7. Book 17 rank 5** (SKELETON l.91) sets Laura's range beside finance chiefs' 80% forecast ranges held "about 36%
  of the time". Say it as a contrast (her band is money owned, not a forecast), never as hit rates side by side, or the
  band reads as a forecast interval.
- **L8. One flat cut for two holding periods.** The floor runs about five years, the moved half about two; a cost that
  accrues each year takes about two and a half times as much from the floor. A cut per year to 15 Dec 2032 would match
  costs better; store only, no change before 27 Nov.

## What I would sign
- The rule's design: each end is money owned in a Treasury fund held to its end, counted at what its holdings pay if
  cash waiting earns nothing, cut once, rounded down, the top added onto the bottom's figure before rounding, the
  contribution capped at the top with anything above going to her flexibility, nothing stated before the move. The code
  does this consistently for both ends.
- The fixing dates (bottom January 2028, top at the move) and the reading that the real uncertainty is which range she
  can state, not whether she reaches it; the contribution equal to the stated top in every future and replay.
- The figures: $95,000 to $115,000 central, and the 1-in-20 spreads ($80,000 to $115,000 and $95,000 to $140,000 in the
  replays; $85,000 for the simulated low), which survive H1's correction unchanged.
- The density rule in 3c's paragraph column: no probability rarer than 1 in 100, no likelihood word, the denominators
  named in Table 2.
- I would sign 3c once H1 (the fee) and H2 (the top's rounding) are fixed, and M2, M4 and M6 are in the notes.

## Score
**3 / 5.** The numbers and the rule are sound and the central range survives the correction, but the confidence
sentence names a cost margin the engine does not have (about 0.22%, not 0.5%, beyond the fee) and the top's rounding
can be read to give $110,000; with H1 and H2 fixed, 4.
