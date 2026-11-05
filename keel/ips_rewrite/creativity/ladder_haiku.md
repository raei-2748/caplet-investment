> AI-generated research (Claude Code, ideation ladder, Thu 5 Nov 2026), not for submission. Keel is a simulated team, AI-written. Read the shortlist beside this file first.

# Ladder brainstorm (Haiku 5.5), 5 Nov 2026: wide-breadth ideas for Laura Gao

Basis: the client case (Laura_Gao_2026_Client_Profile.txt), keel/WHARTON_WORD.md, and the team's FINAL IPS and pitch
(keel/ips_rewrite/drafts/FINAL/). Numbers quoted from the team's own notes (curve of 25 Sep 2026: 5y 4.98%, 10y 5.17%;
ten payments worth about $292k at 1 Jan 2027; headroom under $300k about $8k) are not re-verified here.

Novelty tags: NEW = most strong teams would not think of it; COMMON = many would.
Rule flags: anything that touches a banned instrument or needs a WInS check is marked FLAG.

Categories: (a) funding the operating payments; (b) the 2028 deposit; (c) the 2031 range and co-sponsors; (d) the 2033
split; (e) flexibility and what Laura keeps; (f) risks hidden in the case's dates and cash flows; (g) inflation and the
Taiwan dollar; (h) Laura herself; (i) cross-domain.

---------------------------------------------------------------------------------------------------------------------

## (a) Funding the ten operating payments

1. [a] Coupon-date matching. Choose the bonds whose coupon dates fall in the months just before each January, so most of
   each payment arrives as coupon cash rather than as interest that must be reinvested.
   Mechanism: shrinks the window in which reinvestment risk exists, rung by rung.
   So for Laura: the reinvestment shortfall (about $21k in the team's stress) gets smaller before the range is named.
   Case line: "high degree of certainty" for each payment. Novelty: NEW.

2. [a] Cheapest-cover linear program. Instead of a hand-picked ladder, solve for the set of WInS-listed Treasuries that
   covers each January's $50k at the lowest total price on the purchase day, with a small surplus constraint.
   Mechanism: cash-flow matching as an optimisation; it can recover some of the $8k headroom.
   So for Laura: a cheaper ladder leaves more of the $300k for the facility. Case line: the 2027 deposit. Novelty: NEW.
   FLAG: needs the actual listed bonds on the purchase day.

3. [a] Low-coupon preference. Among bonds that cover the same payment, prefer the lowest coupon, even at a higher price.
   Mechanism: reinvestment exposure scales with the number of coupons received before maturity. Fewer coupons, less to
   reinvest at unknown rates. Plays the same role as a zero-coupon bond without using banned STRIPS.
   So for Laura: the ladder's main weakness shrinks, and the range's shortfall line gets smaller.
   Case line: "high degree of certainty". Novelty: NEW.

4. [a] Purchase-day averaging. The $300k arrives around the first days of January 2027 (a holiday period), so the
   ladder cannot be priced on today's curve. Spread the purchase over the first 20 trading days of 2027, and set each
   rung's size on that day's curve, instead of one trade on one day.
   Mechanism: the ladder's cost is set by the curve on the purchase day, and the headroom is about $8k (27 bp), so one
   bad day can break it. Averaging removes the single-day lottery.
   So for Laura: the ladder fits under $300k even if yields move during the buying window.
   Case line: "start of 2027" deposit with a fixed payment schedule. Novelty: NEW.

5. [a] The reserve is the ladder. Do not set aside new money in 2033. The bonds that mature in 2033-2042 already are the
   operating reserve; the 2033 decision covers only what is left.
   Mechanism: no turnover on the set-aside date, so no transaction or reinvestment decision on the day of the largest
   call on cash.
   So for Laura: the operating reserve needs no action in 2033. Case line: "operating reserve... set aside". Novelty: COMMON.

6. [a] Sinking-fund coverage ratio. Each rung holds about 1.05 times its payment (a 5% margin in each rung), the way
   municipal sinking funds hold a debt-service coverage cushion.
   Mechanism: the margin absorbs a late coupon, a small price miss, or a fee, without touching the next rung.
   So for Laura: costs about $25k up front (5% of the $500k total) and must be paid from the headroom, so it trades
   against the facility minimum. Case line: "high degree of certainty". Novelty: NEW.

7. [a] Targeted early buffer. Put the extra margin on the 2033-2034 rungs only, because a reinvestment shortfall shows up
   first in those years and the reserve must work as the plan's first line.
   Mechanism: targeted buffer rather than even buffer; the years most exposed to a rate fall get the cover.
   So for Laura: uses less headroom than idea 6 for the same protection. Case line: operating commitment. Novelty: NEW.

8. [a] Individual notes, not maturity ETFs. Buy the individual Treasury notes for each rung instead of a maturity-dated
   ETF.
   Mechanism: a held-to-maturity note pays par; a maturity ETF pays its net asset value on the maturity day, net of fees,
   so the rung's cash is a little uncertain.
   So for Laura: the bottom of the 2031 range is an exact payout, not an estimate. Case line: "pays exactly what it
   promised". Novelty: NEW.
   FLAG: check that individual notes are listed on WInS for each rung (the team's WInS book already held individual T-bonds).

## (b) The 2028 deposit

9. [b] The 2028 deposit as a call on information. Do not pre-commit the $150k in 2027. Set a rule: on 1 Jan 2028, use the
   deposit only if the curve has moved against the ladder; otherwise it goes straight to the facility minimum.
   Mechanism: the decision is taken after 14 months of data, and the rule is fixed in advance, so it is not a market timer.
   So for Laura: the facility gets more money in the good case. Case line: "using earnings from publishing advances...".
   Novelty: NEW.

10. [b] Later rungs from the 2028 money. The 2027 money buys the near rungs (2033-2036); the 2028 money buys the far
    rungs (2037-2042) at the curve of 2028.
    Mechanism: the far rungs are the most price-sensitive ones, so buying them later spreads the price risk over two dates.
    So for Laura: the ladder can be built in two halves, with each half priced on a different day.
    Case line: "high degree of certainty" over ten years. Novelty: NEW.

11. [b] The 2027 money alone funds the ladder at today's curve. At 1 Jan 2027 the ten payments cost about $292k against
    $300k of money, so the 2028 deposit is almost free for the facility; it is needed only if yields fall.
    Mechanism: separates the two funding sources cleanly, and shows that the risk is a rate fall, not a missing deposit.
    So for Laura: the facility minimum can be sized from the $150k alone. Case line: the 2028 deposit. Novelty: COMMON.

12. [b] Deposit-free stress as a named test. Run the plan with a zero deposit in 2028 (book advances dry up), and state
    the result: the ladder still pays all ten if the 2027 money alone holds. The stress is the book-deal failure, not a
    market fall.
    Mechanism: stops the team leaning on a deposit that its own IPS says correlates with downturns.
    So for Laura: the IPS's "should not bet on shares twice" logic is tested directly. Case line: the 2028 deposit
    "from book advances, speaking... licensing". Novelty: COMMON.

13. [b] Fixed-date split of the 2028 money. The $150k goes to the ladder gap first, then to the facility minimum, with no
    discretion on the day.
    Mechanism: pre-commitment removes the temptation to hold cash when the market looks bad.
    So for Laura: the plan's only trigger is a date and a yield level set in advance. Case line: "not on market moves"
    (team IPS). Novelty: COMMON.

## (c) The 2031 range and co-sponsors

14. [c] Percentile-labelled range. State each end with its own confidence: the bottom is met with about 99% confidence
    (owned money) and the top with about 50% (half the shares), instead of one blanket confidence.
    Mechanism: two numbers with two probabilities is easier to audit and harder to overpromise.
    So for Laura: the top becomes a probability she can defend, not a hope. Case line: "state how confident they are".
    Novelty: NEW.

15. [c] Conditional top (challenge grant). The bottom is owned money. The top is unlocked only if co-sponsors pledge
    matching money by a fixed date, the way challenge grants work.
    Mechanism: moves part of the top's risk to co-sponsors, and co-sponsors see their own money at work.
    So for Laura: the 2031 range becomes "up to X if the facility is matched". Case line: the top must be credible and
    not damage her credibility. Novelty: NEW.
    FLAG: co-sponsor money is allowed for the facility, never for the payments.

16. [c] Share of the gap, not a dollar amount. Laura pledges to cover a fixed share (say up to 50%) of the facility's
    remaining gap after the other sources, instead of a dollar figure.
    Mechanism: the facility's total cost is not set by the case, so a share is credible when a dollar figure is not.
    So for Laura: the 2031 statement stays true whatever the building costs, and the dollar range is the portfolio's
    answer. Case line: "The total cost of the facility has not been determined." Novelty: NEW.

17. [c] Published rule, not just a number. Publish the formula Laura will use in 2033 (for example, a share of the
    surplus above the reserve), with the 2031 range as the formula's output at two scenario levels.
    Mechanism: a rule can be checked by co-sponsors later; a bare number cannot.
    So for Laura: co-sponsors can see the mechanism, which makes the range more believable. Case line: "credible range".
    Novelty: NEW.

18. [c] Narrowing on a calendar. Announce a wide range in 2031, then a narrower one on fixed dates (for example 1 Jan
    2032), set by the calendar and not by the market.
    Mechanism: information is released on a schedule, so co-sponsors see the range tighten as the portfolio is locked.
    So for Laura: credibility rises over time without any market-timing decision. Case line: "credible range" plus
    "damage her credibility". Novelty: NEW.

19. [c] Averaged valuation date for the top. The top uses the average value of the shares over the 60 trading days before
    the 2031 announcement, not the value on one day.
    Mechanism: a single bad or good day cannot set the top.
    So for Laura: the top is harder to game and less noisy. Case line: the range must "protect the portfolio". Novelty: NEW.

20. [c] Glide-out of shares over 2030-2031. Move the shares into Treasuries in equal quarterly steps across 2030-31,
    not in one move before naming.
    Mechanism: removes exit-timing risk on the share half, the same logic as dollar-cost averaging applied to exit.
    So for Laura: the top settles on a smooth path. Case line: the team's IPS says the half moves "before she names it".
    Novelty: COMMON-to-NEW (team IPS says "before she names it"; the steps are the new part).

21. [c] Minimum-volatility world fund for the cushion. Pick a minimum-volatility world fund, not the cap-weighted index, for
    the half that feeds the 2031 top.
    Mechanism: the top's width depends on how much the shares can move in 2031; lower volatility narrows the range at a
    cost in expected return.
    So for Laura: a tighter range that is easier to keep. Case line: "how favorable and unfavorable market outcomes could
    affect" the range. Novelty: NEW.
    FLAG: check that a minimum-volatility world fund is listed on WInS.

## (d) The 2033 split

22. [d] Senior and junior claims. In 2033, pay in strict order: (1) the ladder to 2042 (senior), (2) the facility minimum,
    (3) the cushion (junior). Mechanism: the way a structured finance deal ranks tranches; no tranche can draw on a senior
    one.
    So for Laura: the payments can never be raided for the facility, by rule. Case line: "must be funded... with a high
    degree of certainty". Novelty: NEW.

23. [d] Debt-service reserve account. Keep twelve months of payments in cash-like holdings as a separate sleeve, on top of
    the ladder.
    Mechanism: the project finance debt-service reserve account; a second line of defence for a single missed payment.
    So for Laura: the ladder's reinvestment problem gets a 12-month buffer. Case line: "high degree of certainty".
    Novelty: NEW.

24. [d] Deferred facility tranche. Contribute part of the facility in 2033 and the rest in 2035, only if co-sponsors reach a
    stated level; the second part is funded from bonds maturing in 2035.
    Mechanism: the decision is pushed to when more is known, and the cushion's bonds do the waiting.
    So for Laura: a real option on the second half without any derivative. Case line: "preserving flexibility".
    Novelty: NEW.

25. [d] Covenant-style trigger on the reinvestment gap. On a fixed date (1 Jan 2033), if the reinvestment shortfall is larger
    than the cushion can cover, the facility amount falls by the gap, computed by a written formula.
    Mechanism: a loan-covenant logic, applied to the one risk the ladder has.
    So for Laura: the facility shrinks automatically, not by discretion. Case line: "responsible facility contribution".
    Novelty: NEW.

26. [d] Cushion laddered to match the build. Put the cushion into short Treasuries maturing 2033-2035, not one lump in
    the world fund, so it arrives as the build needs it.
    Mechanism: matches the cash timing to the construction period, as project finance matches debt to the build.
    So for Laura: the cushion is cash when a cost overrun appears, not when the market recovers. Case line: "if the building
    costs more". Novelty: NEW.
    FLAG: check that the team's cushion is not already in shares that must stay (the IPS needs shares for inflation).

## (e) Flexibility and what Laura keeps

27. [e] Trust-protector band. Laura pre-agrees a facility band (for example, between a lower and an upper dollar figure)
    and a neutral rule for where in the band to land, decided by a named adviser on a fixed date.
    Mechanism: the trust-law device of a protector with powers inside a fixed band; it keeps flexibility without re-deciding
    under pressure.
    So for Laura: she keeps flexibility while the plan has a fixed rule. Case line: "preserving flexibility". Novelty: NEW.
    FLAG: legal structure is out of scope; keep the idea at plan level.

28. [e] Ulysses clause in the IPS. Write the glide path and its fixed dates into the IPS, so that Laura cannot panic-sell in
    a 2031 crash.
    Mechanism: pre-commitment against a known bias; the decision is made when calm.
    So for Laura: the plan is harder to break. Case line: "changes only on fixed dates". Novelty: COMMON.

29. [e] Deferral option. If Taiwan costs jump in 2033, Laura can pay her facility contribution one year later (2034),
    funded by the cushion's bonds.
    Mechanism: a deferral option, priced as the cost of a year's construction inflation.
    So for Laura: the decision date is a choice, not a deadline. Case line: "financial flexibility". Novelty: NEW.

## (f) Risks hidden in the case's dates and cash flows

30. [f] Holiday settlement trap. 1 January is a US market holiday. A Treasury that matures on 31 December or 1 January
    settles on the next business day, so the cash may not be there for the payment date.
    Mechanism: the ladder must mature with a settlement buffer (for example, by mid-December).
    So for Laura: the payment is made on the day it is due, with no cash gap. Case line: payments "at the beginning of
    each year". Novelty: NEW.

31. [f] The bottom is fixed in 2028, not in 2031. The bottom is the fund's payout, and its price is set when the 2028 money
    buys the fund. Laura's 2031 range is only as good as the 2028 purchase price.
    Mechanism: the promise is made two years after the price is locked, so the 2031 announcement cannot change it.
    So for Laura: the 2028 purchase date is the real date of the bottom; the team should say so.
    Case line: "In 2031, however, the value of her portfolio in 2033 remains uncertain." Novelty: NEW.

32. [f] No cash before 2033. The case says Laura takes nothing out before 2033, so the cushion is locked until the facility
    decision. It can only help the building, not the 2027-2032 period.
    Mechanism: a real liquidity constraint; the IPS's word "liquid" must mean liquid from 2033.
    So for Laura: the IPS must not promise cash she cannot touch. Case line: "she will neither add to nor withdraw from the
    portfolio before 2033". Novelty: COMMON.

33. [f] Date stacking on 1 January 2033. The reserve, the first payment and the facility contribution all happen on one
    morning. Their cash must sit in holdings that pay before that morning, in the same month.
    Mechanism: date stacking is a classic operational risk; one missed settlement affects three decisions.
    So for Laura: the 2032 maturities are sized and dated for three calls on the same day. Case line: "start of each
    year". Novelty: NEW.

34. [f] Price the reinvestment gap with a named rate-collapse scenario, not zero. The team's rule treats waiting cash as
    earning nothing; a named scenario (for example, a 2008-style collapse of short rates for three years) is easier to
    defend and smaller.
    Mechanism: zero is a conservative floor but an arbitrary one; a scenario is a stress a judge can follow.
    So for Laura: the reinvestment gap is sized by a story, not an assumption. Case line: "identify the assumptions
    supporting their recommendation". Novelty: NEW.

35. [f] Fixed payments shrink in real terms. $50k fixed for ten years loses about a quarter of its purchasing power by 2042
    at 3% inflation (about 0.77 times). The ladder is not at risk, but the residency's real budget is.
    Mechanism: the payment is a real liability that falls over time; the operating line needs a plan beyond the ten
    payments.
    So for Laura: the team should say what the $50k buys in 2042, not only what it pays. Case line: "not adjusted for
    inflation". Novelty: NEW.

## (g) Inflation and the Taiwan dollar

36. [g] Construction inflation is the delay cost. Taiwan construction costs have risen about 3.5% a year since 2021 (team
    note). A facility funded one year later costs roughly 3.5% more, so the 2031 range should be stated in 2033 dollars.
    Mechanism: a time-value adjustment on the facility, not on the portfolio.
    So for Laura: the range's bottom is in real 2033 terms. Case line: "effect of inflation on... facility costs".
    Novelty: NEW.

37. [g] Shares as the only construction-inflation hedge. The world fund reprices with companies and inflation over time,
    so it is the only part of the plan that tracks construction inflation; that is a reason to keep it, not drop it.
    Mechanism: equity earnings partly track nominal growth; the ladder does not.
    So for Laura: the cushion stays in shares, and the team says why. Case line: the IPS's "shares" argument. Novelty: NEW.

38. [g] Taiwan dollar band in the range. Express the 2031 range in US dollars with a stated Taiwan-dollar band (for example,
    a 10% move in USD/TWD changes the USD cost by about 10%).
    Mechanism: the facility's cost is in TWD; the range must say how much a currency move changes the dollar figure.
    So for Laura: the top is shown with a currency sensitivity. Case line: "unfavorable market outcomes". Novelty: NEW.
    FLAG: a TWD cash or hedge instrument is not verified on WInS; keep the idea to the range's wording only.

39. [g] Inflation top-up for operating support. Use part of the cushion to top up the operating line in real terms, as
    "operating support beyond Laura's commitment", which the case allows from other sources.
    Mechanism: the payments are fixed nominal; the top-up keeps the residency's real budget on track without changing the
    ladder.
    So for Laura: the residency's programme is protected from inflation through the cushion, not through the payments.
    Case line: "any operating support beyond Laura's commitment". Novelty: NEW.

## (h) Laura herself

40. [h] A range she can audit. Her statistics degree means she can check percentiles. Write the range with its
    definitions, the percentile table, and the list of assumptions, so that she, not the team, can defend it.
    Mechanism: client knowledge; the range is in her own language.
    So for Laura: the judges see a client who understands the numbers she signs. Case line: "a thoughtful understanding of
    the client". Novelty: NEW.

41. [h] Product-style staging of the facility. Phase the facility: a minimum first phase in 2033, further phases only if
    co-sponsors and cash allow. Her product-management background makes this a natural frame.
    Mechanism: staged commitment (stage gates) limits what is at risk at each point.
    So for Laura: the facility minimum becomes phase one, not the whole project. Case line: "as the project develops".
    Novelty: NEW.

42. [h] Reputation as a priced loss. Put a value on lost credibility (a missed range costs her co-sponsors, not only money)
    and use it to set how wide the range must be.
    Mechanism: expected-loss logic; the cost of overpromising is larger than the dollar miss.
    So for Laura: the range is set to protect the brand, not only the portfolio. Case line: "damage her credibility".
    Novelty: NEW.

43. [h] Income that moves with markets. Her advances and licensing income are likely to fall in the same downturn that
    hits shares; this is already in the IPS, but the team can price it as a correlation.
    Mechanism: a correlation of income with returns; the 2028 deposit is most likely smallest when shares are weakest.
    So for Laura: the 2028 deposit should be modelled with a downside correlation. Case line: "using earnings from ...
    licensing". Novelty: COMMON.

## (i) Cross-domain

44. [i] Pension cash-flow matching, not immunization. Pension funds often match duration; a held-to-maturity ladder matches
    cash flows, so duration does not need to match. The old team plan matched duration, which is the wrong tool here.
    Mechanism: holding to maturity removes price risk, so only the timing of cash matters.
    So for Laura: the duration match goes; the rung dates carry the plan. Case line: "fund... with a high degree of certainty".
    Novelty: NEW (within this team's plan).

45. [i] Excess-of-loss layering (insurance). Treat the bottom as the primary layer (owned money) and the top as an
    excess layer (shares). The excess layer is allowed to be hit in bad years, as a reinsurance layer is.
    Mechanism: layering is how insurers structure risk so the bottom is robust and the top is priced for loss.
    So for Laura: the 2031 range is a layered promise. Case line: "credible range". Novelty: NEW.

46. [i] Series reliability (engineering). The ten payments are in series: one failed payment fails the residency. If each
    payment has 99.9% reliability, all ten have about 99%. Reliability engineers put the most redundancy where a failure
    would be worst.
    Mechanism: the weakest-link logic says the first payment (2033) and the reinvestment-exposed rungs get extra margin.
    So for Laura: idea 6 and idea 7 are placed by this logic. Case line: "all ten payments must be funded".
    Novelty: NEW.

47. [i] Newsvendor for the promise. The 2031 promise is a newsvendor problem: over-promising costs credibility, under-promising
    costs co-sponsors. With a stated cost ratio, the optimal promise is a set percentile of the 2033 distribution
    (critical fractile = Cu / (Cu + Co)).
    Mechanism: the operations-research rule for the right stock level, applied to a promise.
    So for Laura: if overpromising costs three times underpromising, the top is set at about the 25th percentile.
    Case line: "promises more than she can ultimately contribute". Novelty: NEW.
    FLAG: the cost ratio is a judgment; the team must state it.

48. [i] Costly signal (game theory). Laura's holdback (keeping half the shares) is a costly signal that she is committed:
    she gives up upside to show it.
    Mechanism: a signal is credible when it costs the sender something (Spence-style signalling).
    So for Laura: the kept half is a deliberate signal, not only a cushion. Case line: "demonstrate Laura's commitment".
    Novelty: NEW.

49. [i] Coordination with a focal point (game theory). Co-sponsors are in a stag hunt: each waits for the others. Laura's
    bottom, owned money, is a focal point that makes others join.
    Mechanism: a Schelling point; a number everyone can trust starts the coordination.
    So for Laura: the bottom is the first announcement, the top the second. Case line: "make potential co-sponsors more
    willing to contribute". Novelty: NEW.

50. [i] Segregated account (escrow logic). Ring-fence the ten payments in an account that the facility cannot draw on, with
    release only on the fixed dates.
    Mechanism: escrow and trust law separate the purpose from the balance sheet; the discipline is in the plan.
    So for Laura: the payments are protected by design. Case line: "high degree of certainty". Novelty: NEW.
    FLAG: legal structure is out of scope; keep the idea at plan level.

51. [i] Endowment spending smoothing. Set the facility contribution as a fixed share (for example 4%) of the three-year
    average of the portfolio value, not the 2033 value.
    Mechanism: the endowment spending rule; smoothing cuts the year-to-year noise in the facility figure.
    So for Laura: a 2033 market dip does not cut the facility. Case line: "responsible facility contribution".
    Novelty: NEW.

52. [i] Waterfall with a sinking fund (public finance). Treat the operating payments as a municipal sinking fund with a fixed
    schedule; the facility is the project that can be paid only from what the sinking fund does not need.
    Mechanism: the public-finance rule that the sinking fund is paid first, then the project.
    So for Laura: the same as idea 22, from a different tradition. Case line: "operating reserve". Novelty: COMMON.

53. [i] Cushion in project-style phases. Match the cushion's maturities to the facility's build phases (three years of build
    in 2033-2035), so the cushion funds each phase as it comes due.
    Mechanism: project finance matches the cash timing of funding to the build schedule.
    So for Laura: the cushion arrives as the building needs it. Case line: "as the project develops". Novelty: NEW.

54. [i] Cash-flow game with a stake (behavioural game theory). Co-sponsors are more likely to match money that Laura has
    already committed to a formula, because the formula makes Laura's share predictable.
    Mechanism: a commitment device lowers others' uncertainty and so raises their willingness to give.
    So for Laura: the rule in idea 17 is a co-sponsor magnet. Case line: "make potential co-sponsors more willing".
    Novelty: NEW.

## More: ladder mechanics and the share build

55. [a] Entry through coupons. Shares are not bought on one day: the world fund's money comes from the Treasury fund's
    coupons over 2028-2032, so the share build is already staged.
    Mechanism: the coupon schedule is a dollar-cost average; the team should not buy the whole share sleeve in 2028.
    So for Laura: the share sleeve enters on the coupon schedule, which is naturally staged. Case line: "roughly the
    interest that fund will earn". Novelty: NEW.

56. [a] Premium-versus-discount selection. For the same cash flow, a discount bond costs less on the day than a premium
    bond; pick the cheaper of two bonds that pay the same cash on the same date.
    Mechanism: the purchase price, not the coupon, is what the ladder pays; choosing on price lowers the cash needed.
    So for Laura: frees headroom for the facility. Case line: "high degree of certainty". Novelty: COMMON.

57. [b] Two-date 2028 purchase. Split the 2028 deposit into two purchases (January and July 2028), so the facility fund does
    not depend on one day's curve.
    Mechanism: a second purchase date, like idea 4, for the facility minimum.
    So for Laura: the facility minimum's price risk halves on each date. Case line: the 2028 deposit. Novelty: NEW.

58. [f] Two maturities, not one, for the facility fund. Split the facility minimum into an October 2032 and a December 2032
    maturity so the cash arrives in two steps, and neither depends on a 1 January settlement.
    Mechanism: reduces the single-date settlement risk of idea 30.
    So for Laura: the facility fund arrives in time for the 2033 decision. Case line: "facility contribution... 2033".
    Novelty: NEW.

59. [h] The team's own voice as a judged asset. Judges score "authentic team voice"; a range explained in the team's
    words, with its own assumptions, is judged as creativity.
    Mechanism: Wharton's "Creativity and Presentation" criterion rewards a narrative built on a clear mechanism.
    So for Laura: the range's story is the team's story. Case line: the judging criteria. Novelty: COMMON.

60. [i] Lock the whole plan in a single page of fixed dates. A one-page timetable (dates, amounts, triggers) that the IPS
    publishes; every later decision is checked against it.
    Mechanism: a pre-commitment calendar, the discipline of a public policy schedule.
    So for Laura: the plan can be audited by date, not by feel. Case line: "consistency with the team's IPS". Novelty: COMMON.

---------------------------------------------------------------------------------------------------------------------

## Twelve strongest (for the next rung)
Ranked by how much each would change the plan and how rarely a team would think of it:
1. Holiday settlement trap (30): 1 Jan is a US holiday, so a bond maturing on 31 Dec or 1 Jan can leave the payment short.
2. The bottom is fixed in 2028, not 2031 (31): the 2031 promise is only as good as the 2028 purchase price.
3. Purchase-day averaging for the 2027 ladder (4): one day's curve can break a $8k headroom.
4. Percentile-labelled range with a confidence on each end (14): two probabilities are easier to defend than one.
5. Share of the gap, not a dollar figure (16): the facility's total cost is not set, so a share stays true.
6. A published rule for the 2033 contribution (17): a rule can be checked by co-sponsors; a bare number cannot.
7. Weakest-link logic for the rungs (46): the first payment and the reinvestment-exposed rungs deserve the extra margin.
8. Newsvendor promise level (47): the cost ratio sets the promise as a percentile.
9. Endowment-style three-year smoothing for the facility (51): a 2033 dip does not cut the facility.
10. Senior and junior claims in 2033 (22): the payments can never be raided for the facility.
11. Construction inflation as a delay cost, range in 2033 dollars (36): the facility's price rises each year it waits.
12. The 2028 deposit as a call on information (9): a fixed rule decides after 14 months of data.

FLAGS summary: idea 2 (listing check), 8 (individual notes listed on WInS), 15 and 16 (co-sponsor money only for the facility),
21 (minimum-volatility fund listed on WInS), 26 (cushion must stay partly in shares), 38 (TWD instrument unverified),
50 and 27 (legal structure out of scope). No idea in this list uses a banned instrument (no options, futures, swaps, TIPS,
STRIPS, margin, shorting or crypto).
