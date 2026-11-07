# Numbers and Models: what the modelling shows (for Portfolio Analysis)

Written by Claude (Keel) on 7 Nov 2026. Every number below is a model result or a market fact with its date. Read the warning first.

## Warning before quoting anything

- These numbers come from several draft designs and several Treasury curves (22 Oct to 5 Nov). Before the Final Report quotes one, re-run it on one engine, on one dated curve, using the design in Caplet's submitted IPS. Keel's own plan calls this "one numbers sheet".
- Say "we modelled" or "in our model", never "we judge" or "we expect", and give the assumption.
- WInS gains and losses never go into Laura's projections (Case p.4).
- Caplet's IPS (v12) uses about 7% a year for world shares. The submitted Trading Notes and most of Keel's models used 7.5% (J.P. Morgan's 2027 long-term estimate). Pick one and state it.

## 1. The numbers in Caplet's submitted IPS (v12), and where they come from

- The ten payments need about 5.1% a year on the 2027 deposit; the chosen Treasuries yield about 5.15%. Check: $500,000 of payments against $300,000 today.
- In our simulations the facility contribution reached the top of the range in about three paths in four (model suite M6: 75% in the standard world, 79% with clustered crashes, 84% replaying history since 1871).
- A 40% fall in world shares during 2032 would lower a typical contribution from about $169,000 to $162,000, because the floor is owned in Treasuries.
- A 0.5-point fall in yields before January 2027 would reduce the floor to about $136,000. Rule of thumb from our models: each 0.1-point fall moves about $3,000 of the 2028 deposit from the floor to the payments (M3).
- A permanent 2-point fall in reinvestment rates would leave the payments about $21,000 short over the decade, covered from the shares Laura keeps (15 Oct number sheet: about $11,000, $21,000 and $31,000 short for 1, 2 and 3-point falls).
- 2.5% inflation cuts the floor's real value by about 12% by 2033.
- Result: about two-thirds Treasuries for the payments, one quarter in the floor, under one tenth in shares.

## 2. The cost of the ten payments today

- 5 Nov 2026 close (US Treasury par curve): the ten payments cost $302,163 on 1 Jan 2027 at curve prices, $2,163 over $300,000 (keel/scripts/ladder_history.py). On 23 Oct they cost $297,636.
- Priced with the exact instruments we hold (5 Nov bond quotes, 4 Nov iBond yields): $303,269. If money earns nothing between each maturity and 1 January: $306,663.
- Sensitivity: about $290 per 0.01 point move in yields, so a 0.25-point fall costs about $7,300 more.
- This is why the IPS lets the 2028 deposit finish the set if yields fall first.

## 3. Why buy certainty now: the history test

- $300,000 could have bought all ten payments in only about one month in four since 1871, and in no month from mid-2007 until autumn 2026. At the 2020 low in yields they would have cost about $469,000, more than both deposits together (model suite M1, using each month's 10-year yield).
- Meaning: high yields in 2026 make certainty unusually cheap. Waiting to buy bonds later is a bet that yields stay high.

## 4. The first plan, and why the evidence killed it

- The team's original plan held about three-quarters shares. In the 27 Sep model it missed a payment in 3.2% of paths, 13.7% if the 2028 deposit was $75,000 and 40.8% if it never arrived.
- Buying the payments first never missed one in the same model.
- How much of the leftover went into shares (50% to 70%) barely changed the median result ($205,000 to $209,000).

## 5. Five rival plans against ours

The model suite ran our plan and five common alternatives on the same market paths. "Breaks a promise" means a payment more than $1,000 short or a gift below the bottom of its own range.
- Our design: breaks a promise in 0% to 1.6% of paths, depending on the world.
- 60/40 balanced, target-date glide path, three-year bucket, bond-fund matching (IEF/TLT), all shares then buy bonds late: each broke one of Laura's two promises in 22% to 36% of paths.
- The honest cost: the rivals leave Laura far more money by 2042 (about $170,000 to $290,000, against our $31,000 to $56,000), and the all-shares plan has the biggest median gift. Our plan spends its growth on certainty.
- The 1923 test: start a 60/40 plan in January 1923. Shares earned about 7% a year for fifteen years and the last two payments still bounced (1937, 1938). Good average returns don't protect fixed payments from a bad order of returns.

## 6. The strongest rival: same bonds, more shares

- A plan with the same ten Treasuries but about 80% of the 2028 deposit in shares, buying the floor only in 2031, never missed a payment either.
- Its typical gift was about $5,000 bigger and its average about $15,000 bigger; all of that is the extra return from shares.
- What it pays for: a crash in 2028-30. In the worst twentieth of those markets, the bottom Laura could promise was about $90,000, against our $140,000.
- Warning: this price came out at $4,000, $9,000, $15,000 and $19,000 on four engines. Use one.

## 7. Stress tests

- Clustered crashes with fat tails (a model fitted to 152 years of stock data) moved the 1-in-20 worst gift by less than $1,000. Crashes hit the share fund, not the payments (M2).
- Delete every share Laura owns on the day she names her range: no payment got worse in any of 600,000 modelled futures. The shares are not holding up any payment, which supports our Trading Note on VT.
- A full 2008 replay (yields 1.9 points lower before the build, 2028 deposit $75,000, shares down 40%) made the ten payments cost $361,003 on an earlier design. The later rules were built to close that gap.
- From 1954 to 2011, a lasting fall in rates and a burst of inflation arrived together 8.6% of the time (against 16.3% if they were unrelated).

## 8. The weak point: reinvesting the interest

- The Treasuries cost less than $500,000 because their interest is reinvested. If rates fall for good, the set delivers less.
- Fixes we tried: a ladder where later bonds' interest pays earlier payments (cut the bad case by about 40% but needed about ten more trades); a long-bond hedge (needed $64,000 to $74,000, about half the gift money, refused); pricing the gap as if nothing more were reinvested, the way public bond escrows are sized (kept).

## 9. Inflation and Taiwan

- At 3.5% a year Taiwan building inflation, the 2042 payment buys about 60% of what $50,000 buys today (M4). Topping all ten payments back up would need about $177,000 in 2033 against the roughly $26,000 Laura keeps, so her kept shares are a cushion for building costs, not inflation insurance for the payments.
- The case fixes the payments in dollars, so inflation affects what they buy and the facility, never whether they are paid.

## 10. The WInS book as evidence

- WInS value on 23 Oct: $305,557.66 (+1.85%). Eleven trades of 200.
- The WInS positions hold about 67-72% of each $50,000 rung, because the book is Laura's post-2028 plan scaled to the $300,000 simulator.
- A test for the Final Report: in October the 10-year yield fell from about 5.28% to 5.00%; our bonds rose, and so did the cost of Laura's payments. The holdings moved with what they owe, which is the point of the plan.

## Where the files are

- Model suite and charts: keel/models/ (README, results/suite_results.json, charts/).
- Ladder pricing: keel/scripts/ladder_history.py and keel/scripts/holdings_ladder.py.
- Final Report plan with every model and its reading list: /mnt/project-files/final_report/ERUDITION_PLAN.md.
