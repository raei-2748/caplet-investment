# R02 Concepts and reading list for the IPS rewrite

AI-generated research (Claude Code) for Team Caplet, 26 Oct 2026. Not for submission; cite AI use in the Works Cited.

Scope: Part 1 maps 60 investing concepts onto Laura Gao's plan. Part 2 is a reading list of 72 items for the Final
Report Works Cited (due Sat 5 Dec 09:00 Sydney, Fri 4 Dec 5 pm ET). Part 3 gives five "aha" syntheses. All dollar
figures are MODEL figures from `keel/library/ips_numbers_2026-10/` and `keel/ips_rewrite/lab/R01_dedication.py`;
re-run them before any figure goes into a deliverable. Every bibliographic detail in Part 2 is marked VERIFIED (checked
on the URL given, accessed 26 Oct 2026 Sydney) or UNVERIFIED. The IPS itself allows no citations, so the "IPS phrase"
column gives plain words that show the idea without naming it.

Short names used below: **ladder** = the ten holdings bought with the $300k (IBTM-IBTR for 2033-37; T-bonds Feb-2037,
May-2038, Nov-2039, Nov-2040, Nov-2041 for 2038-42). **Floor** = the IBTM top-up bought from the 2028 deposit that grows
to ~$150k by Dec 2032. **VT sleeve** = the ~$32k of the 2028 deposit in one world stock fund. **Rule** = 2031 range =
floor (rounded down) to floor + half VT; 2033 gift = floor + half VT, capped at the 2031 top.

Verdict tags: **S** = supports the current design; **C** = challenges it (answer given); **R** = suggests a refinement.
Depth tags: textbook / practitioner / niche.

---

## Part 1. Concept map (60 concepts)

### A. Matching money to the payments (the ladder)

**1. Liability-driven investing (LDI).** Start from what must be paid, buy assets that behave like those payments,
and invest only the surplus for growth.
- Plan: the whole $300k (Jan 2027) is spent on assets shaped like the ten $50k payments before any stock is bought;
  stocks come only from the 2028 deposit's surplus. **S.**
- IPS phrase: "We start with what Laura owes, not with what markets might pay."
- Depth: practitioner.

**2. Cash-flow matching (dedicated portfolio).** Buy bonds whose payouts land on or just before each liability date,
so no forecast is needed to meet it.
- Plan: one holding per payment, held to maturity; the lab (R01) shows that sizing the rungs as one dedicated block,
  where later bonds' coupons pay earlier payments, roughly halves the coupon-reinvestment exposure. **S + R** (adopt
  dedicated sizing in the 2028 top-up rule if Caplet votes for it).
- IPS phrase: "Each payment has its own Treasury maturing just before it is due."
- Depth: practitioner (Leibowitz's "dedicated bond portfolio" work for pension funds).

**3. Immunisation (Redington, 1952).** Match the present value and duration of assets to liabilities, with assets
more spread out (higher convexity) than liabilities, so small parallel rate moves cannot create a deficit.
- Plan: the ladder is not run as an immunised book (no rebalancing), but its duration (~9.9 years at 1 Jan 2027) is
  close to the payments' duration by construction. Immunisation needs rebalancing as rates move; the plan does none.
  **C**: answer that cash-flow matching beats immunisation when it is available, because it needs no trading and is
  safe against non-parallel moves, not just small parallel ones.
- IPS phrase: "Matched payment by payment, so no rebalancing is needed to stay safe."
- Depth: practitioner (the actuarial origin is niche).

**4. Horizon (Fisher-Weil) duration: price risk and reinvestment risk offset.** For a holder with a fixed horizon,
a rate rise cuts bond prices but raises what coupons earn when reinvested; at the duration point the two cancel.
- Plan: for the five individual T-bond rungs (2038-42), held to maturity, price moves do not matter, so only the
  reinvestment side remains, and it hurts only if yields FALL and stay down (the ~$21k MODEL stress at -2 points).
  The five iBond ETF rungs (IBTM-IBTR, 2033-37) are different: each ends at its net asset value, not a promise of par
  (concept 7; locked TNA note 2), so their terminal value carries some NAV uncertainty in either rate direction, on
  top of reinvestment risk. **S** for the bonds; the ETFs need their own sentence.
- IPS phrase: "Held to maturity, price swings cannot hurt the bond rungs; only lower yields on reinvested coupons can.
  The fund rungs end at their net asset value, close to but not exactly par."
- Depth: practitioner.

**5. Reinvestment risk.** Coupon bonds pay cash before maturity, and the rate earned on that cash is unknown.
- Plan: the main residual risk. TIPS and STRIPS (the zero-coupon fix) are banned, so it cannot be removed, only shrunk
  (dedicated sizing, R01) and backed (the 2028 deposit tops up first; open vote D1a on whether the floor is the last
  source). **R.**
- IPS phrase: "The one thing we cannot fix in advance is the rate at which coupons are reinvested; we size for it."
- Depth: textbook.

**6. Pull-to-par.** A bond's price drifts towards its face value as maturity nears, whatever happened in between.
- Plan: the reason the T-bond rungs are "boring by design": their 2033-42 cash is known today. **S.**
- IPS phrase: "Whatever markets do in between, each bond is worth its face value on the day it matures."
- Depth: textbook.

**7. Defined-maturity ETF: NAV, not par.** A term ETF holds many bonds maturing in one year and liquidates at net
asset value; it does not promise a fixed sum. The IBTM summary prospectus says the fund "does not seek to return any
predetermined amount at maturity".
- Plan: IBTM (2033 payment + the floor) and IBTN-IBTR rungs. This is why the floor is quoted rounded down (~$145k,
  not $150k) and why vote D1b (quote the bottom with a margin) matters. **C**: answer with the TNA's line: the payout
  is not fixed, so the promise is rounded down; in return, an ETF trades in any size, which an odd-lot bond does not.
- IPS phrase: "The fund behaves like a bond held to its end, but its final payout is not fixed, so we promise less
  than we expect."
- Depth: niche.

**8. Duration.** The weighted average time to a bond's cash flows; also the percentage price change per 1-point
yield move.
- Plan: explains why the IBTR note warns that a fall of ~0.2 points before January would force a 2028 top-up: the
  ladder's DV01 is ~$289 per basis point (MODEL, 25 Sep curve). **S.**
- IPS phrase: "A small fall in yields before January makes the ladder dearer; the 2028 deposit covers that first."
- Depth: textbook.

**9. Convexity.** Bond prices rise more when yields fall than they drop when yields rise; longer, more spread-out
cash flows have more of it.
- Plan: Redington's second condition. It matters for an immunised book, not for one held to maturity. **S** (shows
  the team knows why it can ignore it).
- IPS phrase: none needed; use in the Final Report only.
- Depth: textbook.

**10. Key-rate duration (Ho, 1992).** Measures sensitivity to each point of the yield curve separately, not just a
parallel shift.
- Plan: a ladder matched rung by rung has near-zero key-rate mismatch at every maturity; an IEF/TLT barbell matched
  only on total duration (the September alternative) would not. Strong reason the ladder beats the two-fund duration
  match. **S.**
- IPS phrase: "Matched at every maturity, not just on average, so a twist in the yield curve cannot open a gap."
- Depth: niche.

**11. Defeasance.** Setting aside risk-free securities whose cash flows exactly cover a debt, so the debt is treated
as settled.
- Plan: the 2033 "operating reserve" is economically defeased from the day of purchase (Jan 2027), six years before
  the case asks Laura to set it aside. **S** (and a strong framing).
- IPS phrase: "The operating reserve exists from the first day, not from 2033."
- Depth: niche.

**12. Bought latest maturity first.** If money runs short, the longest (cheapest to fund, most rate-sensitive)
payments should be locked first and the nearest gap filled later from a short, low-risk source.
- Plan: the Jan 2027 buying order; the 2028 deposit then fills any gap in the nearest rung, where rate risk over one
  year is smallest. **S.**
- IPS phrase: "We lock the furthest payments first, because they move most when rates move."
- Depth: practitioner.

**13. Maturity-before-payment buffer and the debt ceiling.** US Treasury default risk is not credit risk in the
usual sense but the risk of a political delay (2011 and 2023 debt-limit stand-offs; GAO estimated the 2011 delay
raised Treasury borrowing costs by about $1.3bn in fiscal 2011; Fitch cut the US to AA+ on 1 Aug 2023 citing
"repeated debt-limit political standoffs"; Moody's cut to Aa1 on 16 May 2025).
- Plan: every rung matures before its payment date (IBTM about 15 Dec 2032 for 1 Jan 2033; the Feb-2037 bond about
  ten months before the 1 Jan 2038 payment). A delay of weeks would not stop a payment. **S** (and a niche point few
  teams will make).
- IPS phrase: "Every bond matures before its payment is due, so even a political delay leaves time to pay."
- Depth: niche.

**14. Expectations hypothesis and forward rates as the break-even.** Today's curve implies forward rates; buying
long now beats waiting only if future rates end up below those forwards.
- Plan: answers "why buy the whole ladder in Jan 2027 instead of waiting?": waiting is a bet against the forwards,
  and Laura's mandate is certainty, not rate views. **S.**
- IPS phrase: "We do not bet on where rates go; we accept today's price for certainty."
- Depth: practitioner.

**15. Term premium.** Long bonds usually pay a little more than the expected path of short rates, as pay for bearing
rate risk (Adrian-Crump-Moench estimates it from the curve).
- Plan: the ladder earns whatever term premium is priced in; for a holder with fixed long payments, long bonds are
  the low-risk asset, so she is paid a premium for holding what she would hold anyway. **S.**
- IPS phrase: "For Laura, long Treasuries are the safe asset, not the risky one."
- Depth: niche.

**16. "The risk-free asset depends on the liability" (Campbell-Viceira).** For a long-horizon investor, cash is risky
(its rate rolls over); the riskless asset is the bond that matches her spending.
- Plan: justifies why the safest place for the payment money is not cash or bills but matched long Treasuries. **S.**
- IPS phrase: "Cash is not safe for Laura: it is the rate she cannot predict."
- Depth: niche.

**17. Nominal vs real liabilities.** A fixed dollar payment is a nominal liability; inflation-linked costs are real
liabilities.
- Plan: the case fixes ten NOMINAL $50k payments, so nominal Treasuries match them exactly; TIPS would add an
  inflation hedge the liability does not need (and are banned). Inflation still erodes what the facility gift buys.
  **S** for the ladder, **C** for the gift: answer that inflation is why the gift is left in stocks, the only real
  asset allowed.
- IPS phrase: "The payments are fixed dollars, so fixed-dollar bonds match them; stocks carry the inflation risk of the
  facility."
- Depth: textbook.

**18. Purchasing power parity and FX.** Over long periods exchange rates tend to track relative price levels, but
deviations last years (Rogoff's "PPP puzzle": half-lives of three to five years).
- Plan: the residency's costs are in Taiwan, but Laura's obligation is $50k nominal USD, so FX is the residency's
  problem, not the reserve's. VT's global stocks give the facility gift some non-US exposure. **S** with a stated
  assumption.
- IPS phrase: "Payments are fixed in US dollars; currency risk sits with the facility budget, not the reserve."
- Depth: practitioner.

### B. Choosing how much risk, and where

**19. Markowitz mean-variance (1952).** Choose the mix with the best expected return for its variance, using
correlations.
- Plan: **C**: mean-variance is single-period and treats all risk as symmetric variance; Laura's problem is a
  multi-date liability plus a promise. Answer: we use Markowitz's lesson (diversify; judge holdings by their effect on
  the whole) inside each layer, not as the overall frame.
- IPS phrase: "Diversified where it pays to be, matched where it must be."
- Depth: textbook.

**20. Tobin separation (two-fund theorem).** Every investor should hold the same risky portfolio and set risk only by
how much goes into the risk-free asset.
- Plan: the plan is literally two funds: Laura's risk-free asset (the matched ladder + floor) and one market portfolio
  (VT). Risk is set by the split, never by picking stocks. **S.**
- IPS phrase: "Two building blocks only: bonds that cannot miss, and the whole world's stocks."
- Depth: textbook (its application to a liability-defined risk-free asset is niche).

**21. Roy's safety-first criterion (1952).** Choose the portfolio that minimises the chance of falling below a
"disaster level".
- Plan: the disaster level is any missed payment (probability ~0 by design) and, second, a gift below the promised
  bottom. **S.**
- IPS phrase: "We first minimise the chance of the one outcome Laura cannot accept."
- Depth: practitioner.

**22. Shortfall constraints (Leibowitz-Henriksson).** Maximise return subject to "the probability of ending below X
is at most p".
- Plan: the 2031 confidence statement (~99% the gift lands inside the range, MODEL) is a shortfall constraint stated
  to co-sponsors. **S.**
- IPS phrase: "A range we expect to hit at least nine times in ten." (number subject to vote and re-run)
- Depth: practitioner.

**23. Surplus optimisation (Sharpe-Tint).** Measure risk as the volatility of assets minus liabilities, not of assets
alone.
- Plan: the ladder looks "risky" in price terms (long duration) but has near-zero surplus risk; VT is the only surplus
  risk. **S.**
- IPS phrase: "Risk is measured against what Laura owes, not against a market index."
- Depth: niche.

**24. Goals-based investing / behavioural portfolio theory (Shefrin-Statman).** People hold layered portfolios: a
safety layer for what must happen, an aspiration layer for upside.
- Plan: three layers: ladder (must), floor (promised), VT half (hoped-for). **S.**
- IPS phrase: "Each dollar has one job: pay, promise or grow."
- Depth: practitioner.

**25. Mental accounting (Thaler) and mean-variance with mental accounts (Das-Markowitz-Scheid-Statman).** Treating
money in separate accounts is a bias in general, but Das et al. show that goal accounts can be mapped to a
mean-variance solution with a shortfall limit per account.
- Plan: **C** (a critic says separate pots waste efficiency). Answer: Das et al. show goal pots are consistent with
  efficient portfolios when each has its own shortfall limit; Laura's pots also map to real legal-style commitments.
- IPS phrase: "Separate pots because Laura has separate promises."
- Depth: niche.

**26. Chhabra's wealth allocation framework.** Split wealth into personal-risk (safety), market-risk (diversified
growth) and aspirational-risk buckets.
- Plan: ladder = personal, floor + VT = market, the half of VT that may go to the residency = aspirational. **S.**
- IPS phrase: as 24.
- Depth: practitioner.

**27. Human capital (Bodie-Merton-Samuelson, 1992).** Future earnings are an asset; if they behave like stocks, hold
fewer stocks.
- Plan: the $150k 2028 deposit comes from publishing, speaking and licensing, which likely fall in a recession. That
  is why the plan does NOT rely on it for the ladder (bought with the first deposit) and only uses it for the floor
  and VT. **S** (see Aha 3).
- IPS phrase: "Laura's 2028 savings depend on her career, so nothing certain depends on them."
- Depth: practitioner.

**28. Life-cycle and horizon irrelevance (Merton 1969; Samuelson 1969).** With constant relative risk aversion and
independent returns, the optimal stock share does not depend on the horizon.
- Plan: the case for stocks rests on surplus, not on "she has years to wait". **S.**
- IPS phrase: "Time does not make stocks safe; spare money makes them affordable."
- Depth: practitioner.

**29. Time-diversification fallacy and the cost of insuring stocks (Bodie, 1995).** The price of a put guaranteeing
at least the risk-free return on stocks rises with the horizon, so stocks are not safer in the long run.
- Plan: the reason the floor is NOT in stocks even with six years to go: insuring it would cost more the longer the
  wait. **S.**
- IPS phrase: as 28.
- Depth: practitioner.

**30. Samuelson's fallacy of large numbers (1963).** Repeating a bet you would refuse once does not make it
acceptable; it only scales the possible loss.
- Plan: same lesson, from the other side: VT for five years is not "averaged out". **S.**
- IPS phrase: none; Final Report.
- Depth: niche.

**31. Within-horizon risk (Kritzman-Rich, 2002).** The chance of breaching a limit at some point during the horizon
is much higher than at the end.
- Plan: the 2031 announcement is a within-horizon checkpoint; the cap fixed in 2031 turns 2031-33 into the only window
  in which stocks can make the gift miss its top. **R**: report "chance of reaching the top" for the 2031-33 window
  (see Aha 5).
- IPS phrase: "What matters is not where stocks end, but what we have promised by the time we promise it."
- Depth: niche.

**32. Sequence-of-returns risk.** Withdrawals during a crash lock in losses.
- Plan: removed for the payments: no payment is ever funded by selling stocks. **S.**
- IPS phrase: "No payment ever waits for stocks to recover."
- Depth: practitioner.

**33. Glide paths, and why this plan does not glide.** Target-date funds cut stocks as a date nears.
- Plan: the plan's stock share is set by the surplus, not the calendar; nothing has to be sold as 2033 nears, because
  the ladder already holds the near-term money. **S** (and a common-sense surprise).
- IPS phrase: "No glide path is needed: the money we need soon is already in bonds."
- Depth: practitioner.

**34. Kelly criterion / "never risk what you need" (Kelly, 1956).** Bet in proportion to edge, and never stake an
amount whose loss is ruinous, since ruin ends compounding.
- Plan: the payments and the floor are never at risk; only money whose loss is survivable is exposed. **S.**
- IPS phrase: "Only money Laura can afford to lose is ever at risk."
- Depth: practitioner.

### C. The bond floor + stock upside structure

**35. Option-based portfolio insurance (Leland-Rubinstein).** Guarantee a floor by holding a risk-free bond plus a
call, or replicate the put by dynamic trading.
- Plan: the floor + VT is the static, option-free version (allowed: no derivatives). **S.**
- IPS phrase: "A guaranteed minimum plus a share of the upside, built without derivatives."
- Depth: practitioner.

**36. Constant-proportion portfolio insurance (CPPI; Black-Jones, Black-Perold).** Keep stock exposure equal to a
multiple of the cushion above the floor, rebalancing as markets move; a fast crash can "gap" through the floor.
- Plan: the plan is CPPI with multiplier 1 and no rebalancing: stocks = the cushion (the interest the floor ETF will
  earn), so gap risk is zero. **S** (and a sharp contrast with the 1987 portfolio-insurance failures).
- IPS phrase: "The stocks are bought with the interest the floor will earn, so they can fall to zero without touching
  it."
- Depth: niche.

**37. Buy-and-hold vs constant mix vs CPPI (Perold-Sharpe, 1988).** Buy-and-hold payoffs are linear and need no
trading; constant mix buys losers; CPPI buys winners.
- Plan: deliberately buy-and-hold: linear payoff, no rebalancing, no timing. **S.**
- IPS phrase: "Bought once, held, never traded to a formula."
- Depth: practitioner.

**38. Principal-protected (bond floor + upside) structured product.** A zero-coupon bond guaranteeing principal plus
an equity option for upside.
- Plan: floor = the bond, VT = the upside; the gift formula is the payoff of a capped participation note. **S** (Aha 1).
- IPS phrase: as 35.
- Depth: practitioner.

**39. Participation rate.** The share of the upside the investor receives.
- Plan: co-sponsors' participation rate on VT is 50%; Laura keeps the other 50%. **S.** **R**: say in the IPS that the
  half is fixed now and cannot be changed later.
- IPS phrase: "Half of any stock gains goes to the residency, half stays with Laura."
- Depth: practitioner.

**40. Cap.** A ceiling on the upside, sold to cut the cost of protection.
- Plan: the gift is capped at the 2031 top, so Laura never gives more than she announced (credibility) and keeps all
  gains above it. **S.**
- IPS phrase: "Never more than she announces, never less than she has already set aside."
- Depth: practitioner.

**41. Collar.** Long a put (floor) and short a call (cap) on the same asset.
- Plan: from the co-sponsors' side, the gift is collared between the floor and the 2031 top. **S.**
- IPS phrase: as 40.
- Depth: practitioner.

**42. Caplet and floorlet.** In interest-rate derivatives, a cap is a strip of caplets, each a call-style option on a
reference rate for one period; a floor is a strip of floorlets, each a put-style option for one period (VERIFIED, see
Part 2, items 61-62).
- Plan: the team's name happens to describe its own structure: one period (2031-33), one floor, one cap. The analogy
  is structural only (Laura's structure is on stocks, not rates, and uses no derivatives). **S** (motif, not
  mechanism).
- IPS phrase: use only in the strategy name and the Final Report, never as a claim that Laura holds options.
- Depth: niche.

### D. The 2031 promise: signals, credibility, commitment

**43. Signalling (Spence, 1973).** A signal is believable when it is costly in a way only the "good type" can afford.
- Plan: the floor is already-owned money in Treasuries, which a less-committed founder could not show. **S.**
- IPS phrase: "Her minimum is money she already owns, not a forecast."
- Depth: practitioner.

**44. Leland-Pyle (1977): the entrepreneur's own stake.** An entrepreneur who keeps a large stake in her own project
signals its quality to outside financiers.
- Plan: the case says a meaningful personal contribution "may signal" viability and attract co-sponsors; Leland-Pyle
  is the formal version. **S.** **C**: a critic could say keeping half of VT signals less commitment. Answer: the
  committed half is a hard floor plus a fixed formula; flexibility is what the case itself requires.
- IPS phrase: "Laura's own money goes in first, so others can trust the project."
- Depth: niche.

**45. Cheap talk (Crawford-Sobel, 1982).** When sender and receiver interests differ, only coarse messages are
credible; equilibria take the form of the sender naming an interval, not a point.
- Plan: a RANGE is exactly the form of credible message the theory predicts. **S** (Aha 2).
- IPS phrase: "A range, not a point, because a point would be a guess."
- Depth: niche.

**46. Seed money and leadership gifts (Andreoni 1998; List-Lucking-Reiley 2002; Vesterlund 2003).** A visible early
gift raises later giving, both by making a threshold project reachable and by signalling quality.
- Plan: the 2031 range is a pre-announced leadership gift. **S** (Aha 2).
- IPS phrase: "An early, firm minimum gives co-sponsors a reason to give."
- Depth: niche.

**47. Rules rather than discretion (Kydland-Prescott, 1977).** A promise is believed when the promiser cannot later
gain by breaking it; a fixed rule beats case-by-case judgement.
- Plan: the gift formula is set in the IPS in 2026, frozen by Wharton's rules, and fixed again in 2031. **S.**
- IPS phrase: "The rule is set today, so no one has to trust a later decision."
- Depth: practitioner (from monetary policy; niche in personal finance).

**48. Time inconsistency (Strotz, 1955).** Plans that look best today may be abandoned later when tastes change.
- Plan: Laura in 2033 may be tempted to give more (enthusiasm) or less (caution); the cap and floor stop both. **S.**
- IPS phrase: as 47.
- Depth: niche.

**49. Commitment devices and Ulysses contracts (Elster; Thaler-Shefrin; Ashraf-Karlan-Yin).** Binding yourself in
advance protects against your future self.
- Plan: held-to-maturity bonds, no rebalancing, the frozen IPS. **S.**
- IPS phrase: "We tie our own hands, on purpose."
- Depth: practitioner.

**50. Pre-registration.** Stating the method before seeing the data stops after-the-fact tuning.
- Plan: the 2031 range method is fixed before the 2031 market is known, so the number cannot be massaged. **S.**
- IPS phrase: "The method is fixed before the result is known."
- Depth: niche (from science methodology).

**51. Real options and the value of flexibility.** Keeping the right, but not the duty, to commit more later has
value when the future is uncertain.
- Plan: the half of VT Laura keeps, plus everything above the cap, is her option on "the project as it develops"
  (case wording). **S.** No source verified for this item in Part 2 (cite a corporate-finance textbook after checking).
- IPS phrase: "What she keeps is not caution; it is the freedom to back the project again when it has grown."
- Depth: practitioner.

### E. The growth sleeve: what and how much

**52. Global diversification and home bias (French-Poterba, 1991).** Investors over-hold their home market.
- Plan: VT holds the world (~10,185 stocks, 0.06% expense ratio at 30 Sep 2026). **S.**
- IPS phrase: "Growth from the whole world's companies, not a guess at one country."
- Depth: textbook.

**53. How many stocks make a diversified portfolio (Statman, 1987).** Gains from adding stocks fall quickly after a
few dozen, yet more still helps a little.
- Plan: one fund gives full diversification in one trade. **S.**
- IPS phrase: as 52.
- Depth: practitioner.

**54. The arithmetic of active management (Sharpe, 1991) and the cost matters hypothesis (Bogle).** Before costs,
the average active dollar earns the market; after costs, it must earn less.
- Plan: index fund, 0.06% fee, no stock picking. **S.**
- IPS phrase: "We do not try to beat the market; we make sure costs do not beat Laura."
- Depth: textbook.

**55. Overtrading (Barber-Odean, 2000).** The most active households earn the least, after costs.
- Plan: 11 of 200 WInS trades; nothing more planned. **S.**
- IPS phrase: "Every trade we did not make is money she keeps."
- Depth: practitioner.

**56. Capital market assumptions (J.P. Morgan LTCMA).** Long-run forecast returns, stated as compound (geometric) and
arithmetic. The 2026 edition (30th, 20 Oct 2025) gives global equities 7.0% and US large cap 6.7%.
- Plan: the VT and range modelling inputs. **C**: the TNA says "about 7.5% a year (as per JPMorgan)", which matches
  EAFE (7.5%) rather than AC World (7.0%) in the team's 27 Sep notes. Answer: re-check before the Final Report and
  quote the AC World figure for VT. **[Window 27 Oct: WRONG EDITION. J.P. Morgan's 2027 LTCMA (release 19 Oct 2026) gives global equities 7.5% (USD), up from 7.0%; the TNA's 7.5% is the world-stocks figure. See `../../office/outbox/2026-10-27_window_7-5-and-three-checks.md`.]**
- IPS phrase: none (no numbers needed).
- Depth: practitioner.

**57. The equity premium (Mehra-Prescott, 1985; Dimson-Marsh-Staunton).** Stocks have historically beaten bonds by
more than standard models explain, in many countries over a century.
- Plan: the reason any stocks are held at all. **S.**
- IPS phrase: "Stocks are where Laura is paid for patience."
- Depth: textbook.

**58. Endowment model and spending rules (Swensen; Litvack-Malkiel-Quandt).** Perpetual funds hold illiquid, diverse
assets and spend a smoothed percentage to be fair across generations.
- Plan: **C** for the fit: Laura's money is not perpetual and has dated payments; illiquid assets are not allowed,
  and a smoothed spending rule would break the fixed payments. Answer: we borrow only the idea of a pre-set rule for
  what may be given (the gift formula), not the portfolio.
- IPS phrase: "This is not an endowment: every dollar has a date or a purpose."
- Depth: practitioner.

### F. Knowing the limits of the numbers

**59. Monte Carlo limits: fat tails (Mandelbrot, 1963) and model risk.** Market returns have more extreme moves than
the normal distribution, so simulated probabilities can be too comforting.
- Plan: the 99% and "3 in 4" figures are MODEL figures. The payments do not rely on them (market-priced Treasuries);
  only the gift's upside does. **S** (and honest).
- IPS phrase: "The payments rest on prices, not on models; only the upside rests on a forecast."
- Depth: practitioner.

**60. Knightian uncertainty and ambiguity (Knight, 1921; Ellsberg, 1961).** Risk has known odds; uncertainty does
not, and people rightly avoid bets whose odds are unknown.
- Plan: the floor is promised from already-owned bonds because its odds are known; the top of the range is labelled
  as a forecast. **S.**
- IPS phrase: "We promise only what we own; we forecast the rest, and say so."
- Depth: niche.

Behavioural extras, folded into 49 and 55: loss aversion (Kahneman-Tversky, 1979) and myopic loss aversion
(Benartzi-Thaler, 1995) explain why Laura should not watch VT's price; the plan gives her nothing to do if it falls.

---

## Part 2. Reading list for the Final Report Works Cited (72 items)

Accessed 26 Oct 2026 (Sydney). VERIFIED = bibliographic details confirmed on the URL shown in this session.
"VERIFIED (partial)" = the details named were confirmed; the rest are marked. Concept numbers refer to Part 1.

### Bond matching, duration and rates

1. Redington, F. M. (1952). Review of the principles of life-office valuations. *Journal of the Institute of
   Actuaries*, 78(3), 286-340. DOI 10.1017/S0020268100052811. Takes: the origin of immunisation (match value and
   duration, assets more spread than liabilities). Concepts 3, 9. VERIFIED:
   https://www.cambridge.org/core/journals/journal-of-the-institute-of-actuaries/article/review-of-the-principles-of-lifeoffice-valuations/42DE39108ADCAD8D476B8E633F8E606F
2. Fisher, L., & Weil, R. L. (1971). Coping with the risk of interest-rate fluctuations: Returns to bondholders from
   naive and optimal strategies. *Journal of Business*, 44(4), 408-431. Takes: duration matching to a horizon offsets
   price and reinvestment risk. Concept 4. VERIFIED (journal, volume, issue, pages via the IDEAS record):
   https://ideas.repec.org/a/ucp/jnlbus/v44y1971i4p408-31.html
3. Macaulay, F. R. (1938). *Some Theoretical Problems Suggested by the Movements of Interest Rates, Bond Yields and
   Stock Prices in the United States since 1856*. National Bureau of Economic Research. Takes: the original
   definition of duration. Concept 8. VERIFIED:
   https://www.nber.org/books-and-chapters/some-theoretical-problems-suggested-movements-interest-rates-bond-yields-and-stock-prices-united
4. Leibowitz, M. L., & Weinberger, A. (1982). Contingent immunization, Part I: Risk control procedures. *Financial
   Analysts Journal*, 38(6), 17-31. DOI 10.2469/faj.v38.n6.17. Takes: a safety floor plus active surplus, the
   institutional ancestor of floor + VT. Concepts 3, 36. VERIFIED:
   https://rpc.cfainstitute.org/research/financial-analysts-journal/1982/contingent-immunizationpart-i-risk-control-procedures
5. Leibowitz, M. L., & Weinberger, A. (1983). Contingent immunization, Part II: Problem areas. *Financial Analysts
   Journal*. Takes: where the floor can fail. Concept 36. VERIFIED (title, year, journal only; volume/pages
   UNVERIFIED): https://rpc.cfainstitute.org/research/financial-analysts-journal/1983/contingent-immunizationpart-ii-problem-areas
6. Leibowitz, M. L. (1986). The dedicated bond portfolio in pension funds, Part II: Immunization, horizon matching and
   contingent procedures. *Financial Analysts Journal*. Takes: dedication vs immunisation trade-offs. Concepts 2, 3.
   VERIFIED (existence, year, journal; authorship, volume and pages UNVERIFIED):
   https://rpc.cfainstitute.org/research/financial-analysts-journal/1986/the-dedicated-bond-portfolio-in-pension-fundspart-ii-immunization-horizon-matching-and-conti
7. Ho, T. S. Y. (1992). Key rate durations: Measures of interest rate risks. *Journal of Fixed Income*, 2(2), 29-44.
   Takes: risk at each point of the curve. Concept 10. UNVERIFIED (details from memory; not confirmed in search).
8. Fama, E. F., & Bliss, R. R. (1987). The information in long-maturity forward rates. *American Economic Review*,
   77(4), 680-692. Takes: forward rates forecast, but imperfectly; expectations hypothesis evidence. Concept 14.
   UNVERIFIED (title found in search results; journal details not confirmed).
9. Campbell, J. Y., & Shiller, R. J. (1991). Yield spreads and interest rate movements: A bird's eye view. *Review of
   Economic Studies*, 58(3), 495-514. Takes: the expectations hypothesis fails in a specific way. Concept 14.
   VERIFIED (partial: authors, title and NBER WP 3153 only; journal details UNVERIFIED):
   https://www.nber.org/papers/w3153
10. Adrian, T., Crump, R. K., & Moench, E. (2013). Pricing the term structure with linear regressions. *Journal of
    Financial Economics*, 110, 110-138. DOI 10.1016/j.jfineco.2013.04.009. Takes: the term premium estimate the New
    York Fed publishes. Concept 15. VERIFIED (issue number not shown):
    https://academicnewsletter.sufe.edu.cn/info/356673 and https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr340.html
11. Campbell, J. Y., & Viceira, L. M. (2002). *Strategic Asset Allocation: Portfolio Choice for Long-Term Investors*.
    Oxford University Press. Takes: for a long-term investor, the riskless asset is the matched long bond, not cash.
    Concepts 16, 28. VERIFIED: https://ideas.repec.org/b/oxp/obooks/9780198296942.html
12. U.S. Department of the Treasury. Daily Treasury Par Yield Curve Rates. Takes: the official curve used for every
    MODEL figure. Concepts 8, 14. VERIFIED (page title and table name):
    https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve
13. iShares (BlackRock). iShares iBonds Dec 2032 Term Treasury ETF (IBTM), Summary Prospectus, 27 Feb 2026. Takes: the
    fund "will terminate on or about December 15, 2032", distributes net assets, and "does not seek to return any
    predetermined amount at maturity"; management fee 0.07%; ICE 2032 Maturity US Treasury Index. Concepts 7, 13.
    VERIFIED: https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf
14. U.S. Government Accountability Office (2012, 23 July). *Debt Limit: Analysis of 2011-2012 Actions Taken and Effect
    of Delayed Increase on Borrowing Costs* (GAO-12-701). Takes: the 2011 delay raised borrowing costs by about $1.3bn
    in FY2011. Concept 13. VERIFIED: https://www.gao.gov/products/GAO-12-701
15. CNBC (2023, 1 Aug). Fitch downgrades U.S. long-term ratings to AA+ from AAA. Takes: Fitch cited "repeated
    debt-limit political standoffs and last-minute resolutions". Concept 13. VERIFIED (URL date; article text says
    "Tuesday"): https://www.cnbc.com/2023/08/01/fitch-downgrades-us-long-term-ratings-to-aa-from-aaa.html
16. Moody's Ratings (2025, 16 May). The US sovereign rating action: Aaa to Aa1, outlook stable. Takes: no US
    Treasury is AAA at all three agencies any more; still the lowest-risk dollar asset available. Concept 13.
    VERIFIED: https://www.moodys.com/web/en/us/about-us/usrating.html
17. Rogoff, K. (1996). The purchasing power parity puzzle. *Journal of Economic Literature*, 34(2), 647-668. Takes:
    FX drifts back to PPP only slowly. Concept 18. VERIFIED: https://ideas.repec.org/a/aea/jeclit/v34y1996i2p647-668.html

### Portfolio choice and risk measures

18. Markowitz, H. (1952). Portfolio selection. *Journal of Finance*, 7(1), 77-91. Takes: diversification and the
    efficient frontier; why one-period variance is not Laura's risk. Concept 19. VERIFIED (no DOI shown):
    https://econpapers.repec.org/RAS/pma73.htm
19. Roy, A. D. (1952). Safety first and the holding of assets. *Econometrica*, 20(3), 431-449. Takes: minimise the
    chance of disaster first. Concept 21. VERIFIED (JSTOR 1907413):
    https://intouch.econometricsociety.org/publications/econometrica/1952/07/01/safety-first-and-holding-assets
20. Tobin, J. (1958). Liquidity preference as behavior towards risk. *Review of Economic Studies*, 25(2), 65-86.
    Takes: two-fund separation. Concept 20. VERIFIED (partial: volume 25, issue 2, February 1958; pages UNVERIFIED):
    https://academic.oup.com/restud/issue/25/2
21. Leibowitz, M. L., & Henriksson, R. D. (1989). Portfolio optimization with shortfall constraints: A
    confidence-limit approach to managing downside risk. *Financial Analysts Journal*, 45(2), 34-41. DOI
    10.2469/faj.v45.n2.34. Takes: a return goal with a stated confidence of not falling short. Concept 22. VERIFIED:
    https://rpc.cfainstitute.org/research/financial-analysts-journal/1989/portfolio-optimization-with-shortfall-constraints-a-confidence-limit-approach-to-managing-downsi
22. Sharpe, W. F., & Tint, L. G. (1990). Liabilities: A new approach. *Journal of Portfolio Management*, Winter 1990,
    5-10. Takes: optimise the surplus, not the assets. Concept 23. VERIFIED (volume/issue not shown):
    https://web.stanford.edu/~wfsharpe/art/art.htm
23. Kritzman, M., & Rich, D. (2002). The mismeasurement of risk. *Financial Analysts Journal*, 58(3), 91-99. DOI
    10.2469/faj.v58.n3.2541. Takes: within-horizon loss is far likelier than end-of-horizon loss. Concept 31.
    VERIFIED: https://ideas.repec.org/a/taf/ufajxx/v58y2002i3p91-99.html
24. Kelly, J. L., Jr. (1956). A new interpretation of information rate. *Bell System Technical Journal*, 35(4),
    917-926. Takes: never stake what ruin would cost. Concept 34. VERIFIED (partial: volume 35, issue 4, July 1956,
    first page 917; last page UNVERIFIED): https://archive.org/details/bstj35-4-917
25. Bengen, W. P. (1994, October). Determining withdrawal rates using historical data. *Journal of Financial
    Planning*. Takes: sequence risk in withdrawals; the plan avoids it by never selling stocks to pay. Concept 32.
    VERIFIED (partial: author, title, journal, October 1994; volume/pages UNVERIFIED):
    https://www.financialplanningassociation.org/sites/default/files/2021-04/MAR04%20Determining%20Withdrawal%20Rates%20Using%20Historical%20Data.pdf
26. Brinson, G. P., Hood, L. R., & Beebower, G. L. (1986). Determinants of portfolio performance. *Financial Analysts
    Journal*, July-August 1986, 39-44. Takes: policy mix drives most of the variation in returns. Concept 20.
    VERIFIED (partial: authors, journal, issue date and pages from the 1995 reprint; volume UNVERIFIED):
    https://indexacapital.com/bundles/unaiadvisor/docs/papers/1986-Brinson-Determinants-of-Portfolio-Performance-I.pdf

### Goals, mental accounts and life-cycle

27. Shefrin, H., & Statman, M. (2000). Behavioral portfolio theory. *Journal of Financial and Quantitative Analysis*,
    35(2), 127-151. Takes: layered portfolios, a safety layer and an aspiration layer. Concept 24. VERIFIED:
    https://ideas.repec.org/a/cup/jfinqa/v35y2000i02p127-151_00.html
28. Das, S., Markowitz, H., Scheid, J., & Statman, M. (2010). Portfolio optimization with mental accounts. *Journal of
    Financial and Quantitative Analysis*, 45(2), 311-334. Takes: goal pots with shortfall limits can be mean-variance
    efficient. Concept 25. VERIFIED (journal, volume, issue, pages; listed under Markowitz on EconPapers; co-author
    list as commonly cited): https://ideas.repec.org/a/cup/jfinqa/v45y2010i02p311-334_00.html
29. Thaler, R. H. (1999). Mental accounting matters. *Journal of Behavioral Decision Making*, 12(3), 183-206. DOI
    10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F. Takes: how people label money, and when it misleads.
    Concept 25. VERIFIED (as cited in a 2025 Royal Society Open Science replication): https://pmc.ncbi.nlm.nih.gov/articles/PMC12445221
30. Chhabra, A. B. (2015). *The Aspirational Investor: Taming the Markets to Achieve Your Life's Goals*. Harper
    Business. Takes: personal, market and aspirational risk buckets. Concept 26. VERIFIED (author, title, publisher;
    Publishers Weekly review dated 6 Apr 2015): https://www.publishersweekly.com/9780062235091
31. Chhabra, A. B. (2005). Beyond Markowitz: A comprehensive wealth allocation framework for individual investors.
    *Journal of Wealth Management*, 7(4), 8-34. Takes: the original paper behind item 30. Concept 26. UNVERIFIED
    (searches found only secondary mentions).
32. Bodie, Z., Merton, R. C., & Samuelson, W. F. (1992). Labor supply flexibility and portfolio choice in a life cycle
    model. *Journal of Economic Dynamics and Control*, 16(3-4), 427-449. Takes: human capital as an asset that shapes
    stock holdings. Concept 27. VERIFIED: https://www.nber.org/papers/w3954
33. Merton, R. C. (1969). Lifetime portfolio selection under uncertainty: The continuous-time case. *Review of
    Economics and Statistics*, 51(3), 247-257. Takes: optimal stock share need not change with horizon. Concept 28.
    VERIFIED (via the IDEAS record path v51y1969i3p247-57): https://ideas.repec.org/r/tpr/restat/v51y1969i3p247-57.html
34. Samuelson, P. A. (1969). Lifetime portfolio selection by dynamic stochastic programming. *Review of Economics and
    Statistics*, 51(3), 239-246. Takes: same result in discrete time. Concept 28. UNVERIFIED (pages not confirmed).
35. Merton, R. C. (2014). The crisis in retirement planning. *Harvard Business Review*, July-August 2014. Takes:
    plan for the income you need, not the wealth you have. Concepts 1, 27. VERIFIED (partial: title and author via
    the AU library record and the author's site; volume/pages UNVERIFIED): https://library.au.int/fr/node/328498 and
    https://robertcmerton.com/?p=339

### Stocks over time

36. Bodie, Z. (1995). On the risk of stocks in the long run. *Financial Analysts Journal*, 51(3), 18-22. DOI
    10.2469/faj.v51.n3.1901. Takes: insuring stocks costs more the longer the horizon. Concept 29. VERIFIED:
    https://rpc.cfainstitute.org/research/financial-analysts-journal/1995/on-the-risk-of-stocks-in-the-long-run
37. Samuelson, P. A. (1963). Risk and uncertainty: A fallacy of large numbers. *Scientia*. Reprinted in *Casualty
    Actuarial Society Forum* (Spring 1994). Takes: repeating a bad bet does not make it good. Concept 30. VERIFIED
    (partial: reprint exists; original volume/pages UNVERIFIED): https://www.casact.org/pubs/forum/94sforum/94sf049.pdf
38. Mehra, R., & Prescott, E. C. (1985). The equity premium: A puzzle. *Journal of Monetary Economics*, 15(2),
    145-161. Takes: why stocks pay more than models predict. Concept 57. VERIFIED:
    https://ideas.repec.org/a/eee/moneco/v15y1985i2p145-161.html
39. Dimson, E., Marsh, P., & Staunton, M. (2002). *Triumph of the Optimists: 101 Years of Global Investment Returns*.
    Princeton University Press. Takes: a century of returns in many countries. Concepts 52, 57. VERIFIED:
    https://eyrolles.com/Loisirs/Livre/triumph-of-the-optimists-9780691091945
40. Ilmanen, A. (2011). *Expected Returns: An Investor's Guide to Harvesting Market Rewards*. Wiley. Takes: how to
    form return assumptions, and their limits. Concept 56. VERIFIED: https://www.oreilly.com/library/view/expected-returns-an/9781119990772/
41. J.P. Morgan Asset Management (2025, 20 Oct). *2026 Long-Term Capital Market Assumptions* (30th edition), press
    release. Takes: global equities 7.0%, US large cap 6.7%, 60/40 6.4% (10-15 years). Concept 56. VERIFIED:
    https://am.jpmorgan.com/us/en/asset-management/adv/about-us/media/press-releases/jp-morgan-releases-2026-long-term-capital-market-assumptions/
42. Mandelbrot, B. (1963). The variation of certain speculative prices. *Journal of Business*, 36, 394-419. Takes:
    fat tails; why simulated odds can mislead. Concept 59. VERIFIED (partial: volume 36, first page 394; issue and
    last page UNVERIFIED): https://ideas.repec.org/a/ucp/jnlbus/v36y1963p394.html
43. Knight, F. H. (1921). *Risk, Uncertainty and Profit*. Houghton Mifflin. Takes: measurable risk vs true
    uncertainty. Concept 60. VERIFIED: https://www.econlib.org/library/Knight/knRUP.html
44. Ellsberg, D. (1961). Risk, ambiguity, and the Savage axioms. *Quarterly Journal of Economics*, 75(4), 643-669.
    Takes: people avoid bets with unknown odds. Concept 60. VERIFIED:
    https://ideas.repec.org/a/oup/qjecon/v75y1961i4p643-669..html

### Floors, insurance and structured payoffs

45. Rubinstein, M., & Leland, H. E. (1981). Replicating options with positions in stock and cash. *Financial Analysts
    Journal*, 37(4), 63-72. DOI 10.2469/faj.v37.n4.63. Takes: a floor can be built without buying options. Concept
    35. VERIFIED: https://rpc.cfainstitute.org/research/financial-analysts-journal/1981/replicating-options-with-positions-in-stock-and-cash
46. Leland, H. E. (1980). Who should buy portfolio insurance? *Journal of Finance*, 35(2), 581-594. Takes: insurance
    suits investors whose needs rise sharply below a floor. Concept 35. UNVERIFIED (not found in search).
47. Black, F., & Jones, R. (1987). Simplifying portfolio insurance. *Journal of Portfolio Management*, 14(1), 48-51.
    Takes: the CPPI rule. Concept 36. UNVERIFIED (not found in search).
48. Black, F., & Perold, A. F. (1992). Theory of constant proportion portfolio insurance. *Journal of Economic
    Dynamics and Control*, 16(3-4), 403-426. Takes: CPPI's maths and its gap risk. Concept 36. VERIFIED (via the IDEAS
    record path v16y1992i3-4p403-426): https://ideas.repec.org/r/eee/dyncon/v16y1992i3-4p403-426.html
49. Perold, A. F., & Sharpe, W. F. (1988). Dynamic strategies for asset allocation. *Financial Analysts Journal*,
    January/February 1988, 16-27. Takes: buy-and-hold vs constant mix vs CPPI. Concept 37. VERIFIED (volume not
    shown): https://web.stanford.edu/~wfsharpe/art/art.htm
50. Hull, J. C. *Options, Futures, and Other Derivatives* (11th ed.). Pearson. Takes: the textbook definition of
    caps, floors, caplets and floorlets. Concept 42. VERIFIED (title, edition, publisher; year not shown):
    https://www.pearson.com/store/en-us/p/options-futures-and-other-derivatives/P200000005938
51. Wikipedia. Interest rate cap and floor. Takes: a cap is "European call options, known as caplets, which exist for
    each period"; a floor is "a series of European put options or floorlets". Concept 42. VERIFIED (tertiary source;
    cite Hull in the Final Report): https://en.wikipedia.org/wiki/Interest_rate_cap_and_floor

### Signals, promises and commitment

52. Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics*, 87(3), 355-374. Takes: a costly signal
    is believed. Concept 43. VERIFIED: https://www.sfu.ca/%7Eallen/Spence.pdf
53. Leland, H. E., & Pyle, D. H. (1977). Informational asymmetries, financial structure, and financial
    intermediation. *Journal of Finance*, 32(2), 371-387. Takes: the entrepreneur's own stake signals project quality.
    Concept 44. VERIFIED (no DOI shown): https://ideas.repec.org/a/bla/jfinan/v32y1977i2p371-87.html
54. Crawford, V. P., & Sobel, J. (1982). Strategic information transmission. *Econometrica*, 50(6), 1431-1451.
    Takes: credible messages take the form of intervals. Concept 45. VERIFIED:
    https://ideas.repec.org/a/ecm/emetrp/v50y1982i6p1431-51.html
55. Andreoni, J. (1998). Toward a theory of charitable fund-raising. *Journal of Political Economy*, 106(6),
    1186-1213. Takes: seed money makes threshold projects reachable. Concept 46. VERIFIED:
    https://ideas.repec.org/a/ucp/jpolec/v106y1998i6p1186-1213.html
56. List, J. A., & Lucking-Reiley, D. (2002). The effects of seed money and refunds on charitable giving:
    Experimental evidence from a university capital campaign. *Journal of Political Economy*, 110(1), 215-233.
    Takes: field evidence that a larger announced seed raises later gifts (effect size UNVERIFIED; read before
    quoting). Concept 46. VERIFIED: https://econpapers.repec.org/article/ucpjpolec/v_3a110_3ay_3a2002_3ai_3a1_3ap_3a215-233.htm
57. Vesterlund, L. (2003). The informational value of sequential fundraising. *Journal of Public Economics*, 87(3-4),
    627-657. Takes: announcing an early gift tells later donors the project is good. Concept 46. VERIFIED:
    https://ideas.repec.org/a/eee/pubeco/v87y2003i3-4p627-657.html
58. Kydland, F. E., & Prescott, E. C. (1977). Rules rather than discretion: The inconsistency of optimal plans.
    *Journal of Political Economy*, 85(3), 473-492 (often cited as 473-491; the JSTOR print shows 473-492). Takes:
    fixed rules make promises credible. Concept 47. VERIFIED:
    https://www.econ.puc-rio.br/mgarcia/Macro%20II%20-%20Mestrado/KydlandPrescott1977.pdf
59. Strotz, R. H. (1955-56). Myopia and inconsistency in dynamic utility maximization. *Review of Economic Studies*,
    23(3), 165-180. Takes: plans get abandoned when the future self differs. Concept 48. VERIFIED (JSTOR 2295722):
    https://www.ceremade.dauphine.fr/~ekeland/lectures/strotz1955.pdf
60. Thaler, R. H., & Shefrin, H. M. (1981). An economic theory of self-control. *Journal of Political Economy*,
    89(2), 392-406. Takes: the planner binds the doer. Concept 49. VERIFIED:
    https://ideas.repec.org/a/ucp/jpolec/v89y1981i2p392-406.html
61. Elster, J. (1979). *Ulysses and the Sirens: Studies in Rationality and Irrationality*. Cambridge University
    Press. Takes: precommitment as rational. Concept 49. VERIFIED:
    https://resolve.cambridge.org/core/journals/canadian-journal-of-philosophy/article/jon-elster-ulysses-and-the-sirens-studies-in-rationality-and-irrationality-cambridge-cambridge-university-press-1979-pp-ix-193/B2E3EF2C530035FDAEBA97C963BAC6E3
62. Ashraf, N., Karlan, D., & Yin, W. (2006). Tying Odysseus to the mast: Evidence from a commitment savings product
    in the Philippines. *Quarterly Journal of Economics*, 121(2). Takes: people choose to lock their own savings.
    Concept 49. VERIFIED (partial: title and authors via the IDEAS working-paper record; journal pages UNVERIFIED):
    https://ideas.repec.org/p/ags/yaleeg/28411.html
63. Thaler, R. H., & Benartzi, S. (2004). Save More Tomorrow: Using behavioral economics to increase employee saving.
    *Journal of Political Economy*, 112(S1), S164-S187. Takes: pre-set rules beat later willpower. Concept 49.
    VERIFIED: https://ideas.repec.org/a/ucp/jpolec/v112y2004is1ps164-s187.html

### Costs, diversification and behaviour

64. Sharpe, W. F. (1991). The arithmetic of active management. *Financial Analysts Journal*, 47(1), 7-9. Takes: after
    costs, the average active dollar must lag the index. Concept 54. VERIFIED (reprint header):
    https://marottaonmoney.com/wp-content/uploads/2021/07/The-Arithmetic-of-Active-Management.pdf
65. Bogle, J. C. *The Little Book of Common Sense Investing*. Wiley. Takes: the cost matters hypothesis. Concept 54.
    VERIFIED (title and publisher; edition and year UNVERIFIED): https://en.wikipedia.org/wiki/The_Little_Book_of_Common_Sense_Investing
66. French, K. R., & Poterba, J. M. (1991). Investor diversification and international equity markets. *American
    Economic Review*, 81(2), 222-226. Takes: home bias. Concept 52. VERIFIED:
    https://ideas.repec.org/a/aea/aecrev/v81y1991i2p222-26.html
67. Statman, M. (1987). How many stocks make a diversified portfolio? *Journal of Financial and Quantitative
    Analysis*, 22(3), 353-363. Takes: diversification gains. Concept 53. VERIFIED:
    https://ideas.repec.org/a/cup/jfinqa/v22y1987i03p353-363_01.html
68. Vanguard. Vanguard Total World Stock ETF (VT) fact sheet, as of 30 Sep 2026. Takes: 0.06% expense ratio; 10,185
    stocks; FTSE Global All Cap Index. Concept 52. VERIFIED: https://fund-docs.vanguard.com/F3141.pdf
69. Barber, B. M., & Odean, T. (2000). Trading is hazardous to your wealth. *Journal of Finance*, 55(2), 773-806.
    Takes: overtrading costs households. Concept 55. VERIFIED: https://ideas.repec.org/a/bla/jfinan/v55y2000i2p773-806.html
70. Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2),
    263-292 (often cited as 263-291). Takes: losses hurt more than gains please. Concept 60 extras. VERIFIED (the
    Econometric Society page lists pages 263-292):
    https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk
71. Benartzi, S., & Thaler, R. H. (1995). Myopic loss aversion and the equity premium puzzle. *Quarterly Journal of
    Economics*, 110(1), 73-92. Takes: checking prices often makes stocks feel riskier than they are. Concept 60 extras.
    VERIFIED: https://ideas.repec.org/a/oup/qjecon/v110y1995i1p73-92..html

### Institutional practice and the IPS form

72. Swensen, D. F. (2009). *Pioneering Portfolio Management: An Unconventional Approach to Institutional Investment*
    (fully revised and updated ed.). Free Press. Takes: the endowment model, and why it needs perpetual, illiquid
    capital Laura does not have. Concept 58. VERIFIED (title, edition, ISBN 9781416544692; publisher per the Simon &
    Schuster page): https://www.simonandschuster.com/books/Pioneering-Portfolio-Management/David-F-Swensen/9781416554035

Supplementary (not counted above):
- Litvack, J. M., Malkiel, B. G., & Quandt, R. E. (1974). A plan for the definition of endowment income. *American
  Economic Review*, 64(2), 433-437. Takes: spending rules for endowments. Concept 58. VERIFIED:
  https://ideas.repec.org/a/aea/aecrev/v64y1974i2p433-37.html
- CFA Institute. *Elements of an Investment Policy Statement for Individual Investors*. Takes: the standard headings of
  an IPS (objectives, constraints, review). Concept: structure of the IPS. VERIFIED (title and publisher; year
  UNVERIFIED): https://rpc.cfainstitute.org/policy/positions/elements-of-an-investment-policy-statement-for-individual-investors
- Tobin, J. (1974). What is permanent endowment income? *American Economic Review*, 64(2), 427-432. Takes:
  intergenerational equity ("The trustees of an endowed institution are the guardians of the future against the
  claims of the present", quoted in a Yale course chapter citing this article). **[Library 27 Oct: VERIFIED,
  https://ideas.repec.org/a/aea/aecrev/v64y1974i2p427-32.html]**

Added by the Library, Tue 27 Oct 2026 (accessed 27 Oct 2026; slip S-05 and LC-03 in `../../rooms/library.md`):
- Yale University, Policy 2202 "Endowment Spending and Distributions" (effective 1 Mar 2023, revised 1 Jul 2026).
  Takes: "80% of the prior year's spending plus 20% of the long-term spending rate" (5.25%) applied to market value,
  inflation-adjusted, bounded 4.0%-6.5%: a fixed-dollar draw and a fixed-share draw blended by a dial. VERIFIED:
  https://your.yale.edu/policies-procedures/2202-endowment-spending-and-distributions
- 26 CFR 1.664-2 (charitable remainder annuity trust) and 1.664-3 (unitrust), Cornell LII. Takes: US law's own split
  of a "sum certain" (annuity trust; "no additional contributions may be made ... after the initial contribution")
  from "a fixed percentage of the net fair market value of the trust assets determined annually" (unitrust).
  VERIFIED: https://www.law.cornell.edu/cfr/text/26/1.664-2 ; https://www.law.cornell.edu/cfr/text/26/1.664-3
- Internal Revenue Service, Rev. Proc. 2016-42 (effective 8 Aug 2016), describing Rev. Rul. 77-374. Takes: a sum-
  certain trust fails if the chance it is exhausted "is greater than 5 percent", worked out at one assumed rate (the
  section 7520 rate) with a mortality table. VERIFIED: https://www.irs.gov/pub/irs-drop/rp-16-42.pdf
- Parks, C. T., Finestone, W., & Leahy, S. (2015). Charitable remainder trusts and the probability of exhaustion test.
  *Tax Notes*, 148(10), 1141 (7 Sep 2015). Takes: the test "assumes that the section 7520 rate in existence at
  creation will be the rate of growth of CRAT assets throughout its life"; low rates made CRATs fail it. VERIFIED (PDF
  on the firm's site): https://www.cov.com/-/media/files/corporate/publications/2015/09/charitable_remainder_trusts_and_the_probability_of_exhaustion_test.pdf
- Costa, F. O., Sousa, J. J. S., Pais, A. A. C. C., & Formosinho, S. J. (2003). Comparison of dissolution profiles of
  Ibuprofen pellets. *Journal of Controlled Release*, 89, 199-212. Takes: zero order = "Constant release rate"; mean
  dissolution time MDT = integral of t dM(t) over integral of dM(t), the same first moment as Macaulay duration
  without discounting. VERIFIED (author repository PDF): https://baes.uc.pt/bitstream/10316/5781/1/filebf23384fd26443af89fb7d1128288cea.pdf
- Health Canada (3 Aug 2005). Potentially fatal interaction between slow-release opioid painkillers and alcohol.
  Takes: FDA instructed Purdue to withdraw Palladone on 13 July 2005; "This effect is known as dose dumping."
  VERIFIED: https://www.canada.ca/en/news/archive/2005/08/potentially-fatal-interaction-between-slow-release-opioid-painkillers-alcohol.html
- Hughes, K., Gray, A., Asgarzadeh, F., et al. (2015). Regulatory considerations for alcohol-induced dose dumping of
  oral modified-release formulations. *Pharmaceutical Technology*, 39(10), 40-46. Takes: dose dumping = "the rapid
  release of the entire dose or a significant fraction thereof in a short period of time"; Palladone with 240 mL of
  40% alcohol gave a peak plasma level "approximately six times higher" than with water. VERIFIED (note: the article
  calls Palladone "hydrocodone"; it was hydromorphone, per Health Canada and D'Souza et al. 2017):
  https://pharmtech.com/view/regulatory-considerations-alcohol-induced-dose-dumping-oral-modified-release-formulations

Count: 72 numbered items, 3 supplementary. Numbered items: VERIFIED 54; VERIFIED (partial) 12 (items 5, 6, 9, 20,
24, 25, 26, 35, 37, 42, 62, 65); UNVERIFIED 6 (items 7, 8, 31, 34, 46, 47). Supplementary: 2 VERIFIED, 1 UNVERIFIED
(Tobin 1974).

---

Added by the Library, Wed 28 Oct 2026 (accessed 28 Oct 2026; quoted lines found word for word in the fetched page;
round 1 beat 4 in `../../loop/rounds/2026-10-28.md`, LC-04 and S-06 in `../../rooms/library.md`):
- 26 U.S.C. § 130(d), qualified funding asset, Cornell LII: https://www.law.cornell.edu/uscode/text/26/130. Takes: a
  court's fixed schedule funded with "any obligation of the United States" bought within 60 days of the promise. Bank #59.
- Oregon Administrative Rules 177-098-0060, Prize Payment (Mega Millions), via https://oregon.public.law/rules/oar_177-098-0060
  (aggregator; official OAR text not opened). Takes: the prize is "the actual amount purchased", not the advertised one. Bank #57.
- California Public Contract Code § 22300, via https://california.public.law/codes/public_contract_code_section_22300.
  Takes: securities in lieu of retainage, owned by the contractor. Bank #56.
- Santomartino, S. (3 Nov 2023). The contractor's contingency: what contractors and construction managers need to know
  and be wary of. ConsensusDocs (Peckar & Abramson): https://www.consensusdocs.org/the-contractors-contingency-what-contractors-and-construction-managers-need-to-know-and-be-wary-of/
- FAR 52.216-4, Economic Price Adjustment - Labor and Material: https://www.acquisition.gov/far/52.216-4
- ETC. *Eos Family Online Help*, "About Cues and Cue Lists" and "Block":
  https://www.etcconnect.com/WebDocs/Controls/EosFamilyOnlineHelp/en/Content/12_Cues_and_Cue_Lists/About_Cues_and_Cue_Lists.htm. Bank #58.
- Central Connecticut State University Theatre (2025). *Stage Management and Assistant Stage Management Handbook*, pp. 19-20:
  https://www.ccsu.edu/sites/default/files/2025-08/Updated%20SM%20and%20ASM%20Handbook%202025%20mf.pdf
- SVB Financial Group (8 Mar 2023). Strategic Actions / Q1'23 Mid-Quarter Update, Form 8-K ex. 99.2:
  https://www.sec.gov/Archives/edgar/data/719739/000119312523064680/d430920dex992.htm
- Barings (Jun 2025). What is a CLO?:
  https://www.barings.com/globalassets/2-assets/perspectives/viewpoints/insights/2025/06-june/what-is-a-clo.pdf

Added by the Library, Thu 29 Oct 2026 (accessed 29 Oct 2026; quoted lines found in the fetched page text; round 2 beat 4
in `../../loop/rounds/2026-10-29.md`, slip S-07 in `../../rooms/library.md`):
- Presidente de la República de Chile (17 Sep 2025). Mensaje Nº 199-373, bill Boletín 17.856-05 (reform of Ley 20.128),
  via Diario Constitucional: https://www.diarioconstitucional.cl/2025/10/18/gobierno-propone-nuevas-reglas-para-fortalecer-fondos-soberanos/mensaje-boletin-no-17-856-05/
  (mirror; the law text on bcn.cl did not load). Takes: the "orden de prelación" ranking the pension fund over the
  stabilisation fund.
- Norwegian Ministry of Finance. Meld. St. 1 (2023-2024), National Budget 2024, ch. 3:
  https://www.regjeringen.no/en/documents/meld.-st.-1-20232024/id2998356/?ch=2. Takes: "major changes in Fund value
  should not immediately entail major changes in Fund spending".
- Alaska Permanent Fund Corporation. FAQs & Helpful Information, https://apfc.org/?p=4896, and Generating Revenue for
  Today & Tomorrow, https://apfc.org/era-durability/. Takes: 5% of a lagged average, "limited to the ERA balance".
- Grundgesetz für die Bundesrepublik Deutschland, Art. 115: https://www.gesetze-im-internet.de/gg/art_115.html. Takes:
  the emergency exception "ist mit einem Tilgungsplan zu verbinden". Bank #70.
- European Commission (20 Mar 2020). COM(2020) 123 final, activation of the general escape clause of the Stability and
  Growth Pact (German text): https://economy-finance.ec.europa.eu/document/download/4039fca6-615f-4115-a9ad-cdce4be17279_de
- Potthoff, S., Finke, M., Scholten, M., Gieselmann, A., Vollmann, J. and Gather, J. (21 Oct 2022). Opportunities and
  risks of self-binding directives. *Frontiers in Psychiatry* 13:
  https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.974132/full
- Royal College of Physicians (Dec 2017). *National Early Warning Score (NEWS) 2*, executive summary:
  https://www.rcp.ac.uk/media/ctulqqbn/news2-executive-summary_0.pdf. Takes: the "single red score". Bank #71.
- NSW Health (7 Apr 2025). Policy Directive PD2025_014, *Recognition and management of patients who are deteriorating*:
  https://www1.health.nsw.gov.au/pds/ActivePDSDocuments/PD2025_014.pdf. Takes: signed, expiring alterations; escalation
  on silence. Bank #70.
- Ede, J., Jeffs, E., Vollam, S. and Watkinson, P. (2020). A qualitative exploration of escalation of care in the acute
  ward setting. *Nursing in Critical Care* 25(3): https://pmc.ncbi.nlm.nih.gov/articles/PMC7217245. Bank #71.
- Badawy, J., Nguyen, O. K., Clark, C., Halm, E. A. and Makam, A. N. Is everyone really breathing 20 times a minute?
  *BMJ Quality & Safety* 26(10): https://qualitysafety.bmj.com/content/26/10/832 (year not shown in the fetched text).

Added by the Library, Fri 30 Oct 2026 (accessed 30 Oct 2026; quoted lines found in the fetched page text; round 3 beat 4
in `../../loop/rounds/2026-10-30.md`, slip S-08 in `../../rooms/library.md`). Q10, why a range and what each end costs:
- Ritter, J. R. (2026). Initial Public Offerings: Price Revision Statistics Through 2025. University of Florida:
  https://site.warrington.ufl.edu/ritter/files/IPOs-price-revision.pdf. Takes: Table 7, below / within / above the file
  range, 33/45/22% (2001-2019) and 16/55/29% (2020-2025); first-day returns 3/12/38% and 6/21/51%. Bank #87.
- Hanley, K. W. (1993). The underpricing of initial public offerings and the partial adjustment phenomenon. *Journal of
  Financial Economics* 34(2), 231-250: https://business.lehigh.edu/sites/default/files/2019-08/7%20hanley_1993_jfe_0.pdf.
  Takes: 20.7% above the range, 10.0% within, 0.6% below. Bank #87.
- Busaba, W. Y., Liu, Z. and Restrepo, F. (2020). Do Underwriters Price Up IPOs to Prevent Withdrawal? *Journal of
  Financial and Quantitative Analysis* 55(6), 2005-2036 (abstract): https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/do-underwriters-price-up-ipos-to-prevent-withdrawal/2100A5B72028FDF5851084656AA3CA92
- List, J. A. and Lucking-Reiley, D. (2002). The Effects of Seed Money and Refunds on Charitable Giving: Experimental
  Evidence from a University Capital Campaign. *Journal of Political Economy* 110(1) (reprint on J. Andreoni's UCSD
  site): https://econweb.ucsd.edu/~jandreoni/PhilanthropyAndFundraising/Volume%202/8%20List%20Lucking-Riley%202002.pdf.
  Direction checked at the source: seed 10% -> 67% of the goal, "a nearly sixfold increase in contributions", donors
  3.7% -> 8.2%, mean gift $15.42 -> $39.87; refunds +20%, "no effect on the participation rate". Bank #85.
- Verhaert, G. A. and Van den Poel, D. (2012). The Role of Seed Money and Threshold Size in Optimizing Fundraising
  Campaigns: Past Behavior Matters! Ghent University WP 12/815: http://wps-feb.ugent.be/Papers/wp_12_815.pdf (working
  paper). Takes: seed money "with a low threshold it could have a baleful influence".
- Stratton, N. (23 Jan 2020). Maximizing the Value of a Campaign's Quiet Phase. CCS Fundraising:
  https://www.ccsfundraising.com/insights/maximizing-the-value-of-a-campaigns-quiet-phase/ (practitioner). Bank #86.
- Jowdy, J. (13 May 2026). Don't Go Public Too Soon. NonProfit PRO:
  https://www.nonprofitpro.com/post/dont-go-public-too-soon-what-the-capital-campaign-quiet-phase-is-really-for/
  (practitioner). Bank #86.
- Eisenstein, A. (3 Sep 2021, updated 4 Jul 2026). Set the Right Fundraising Goal for Your Capital Campaign. Elevation:
  https://www.elevationweb.org/blog/set-the-right-fundraising-goal-for-your-capital-campaign/ (practitioner).
- LeClerc, J. E. and Joslyn, S. (2011). The Effects of the Use of Uncertainty Estimates on Weather-Related
  Decision-Making. AMS 91st Annual Meeting, J13.7 (abstract): https://ams.confex.com/ams/91Annual/webprogram/Paper182589.html.
  Journal version: Joslyn, S. and LeClerc, J. (2012), *J. Exp. Psych.: Applied* 18(1), 126-140 (citation only). Bank #84.
- Richardson, D. S. (2003). Predictability and economic value. ECMWF seminar paper:
  https://www.ecmwf.int/sites/default/files/elibrary/2003/11922-predictability-and-economic-value.pdf. Takes: the
  cost-loss rule. Bank #84.
- MIT OpenCourseWare (Fall 2014). 15.772J / EC.733J D-Lab: Supply Chains, Newsvendor Inventory Problem:
  https://ocw.mit.edu/courses/15-772j-d-lab-supply-chains-fall-2014/6952be57b43aa185119c6f114908bcc5_MIT15_772JF14_Newsboy.pdf.
  Takes: the critical fractile, underage / (underage + overage). Bank #84.

Added by the Library, Sat 31 Oct 2026 (accessed 31 Oct 2026; quoted lines found in the fetched page text; round 4 beat 4
in `../../loop/rounds/2026-10-31.md`, slip S-09 in `../../rooms/library.md`). Q12, why not a safe ladder and the rest in stocks:
- Harvard Magazine (18 Feb 2009). Faust: University Will Slow Pace of Construction in Allston:
  https://www.harvardmagazine.com/index%2ephp/2009/02/harvard-to-slow-pace-of-construction-in-allston; Faust, D. G.
  (18 Feb 2009), letter to the community: https://www.harvard.edu/president/news-faust/2009/letter-to-the-community-2009/;
  Harvard Magazine (Dec 2009), Harvard delays Allston construction, campus development:
  https://harvardmagazine.com/2009/12/harvard-delays-allston-campus-planning-development. Takes: endowment down 30%
  from $36.9bn; construction slowed, then "pauses indefinitely". Bank #95.
- Hughes, C. J. (22 Jan 2009). Recession Halts Yale Construction Projects. *Architectural Record*:
  https://www.architecturalrecord.com/news/daily/archives/090122yaleconstruction.asp; *Daily Princetonian* (Apr 2009),
  U. postpones $695 million in construction projects:
  https://www.dailyprincetonian.com/article/2009/04/u-postpones-695-million-in-construction-projects. Bank #95.
- UNC Chapel Hill. Capital Gift Funding Policy (2021, modified 2026):
  https://policies.unc.edu/TDClient/2833/Portal/KB/Article/132150/Capital-Gift-Funding-Policy. Takes: 100% in cash
  before the award (85% exception). Bank #95.
- Government Finance Officers Association (2022). Investment and Management of Bond Proceeds (best practice):
  https://www.gfoa.org/materials/investment-and-management-of-bond-proceeds. Bank #96.
- California Government Code s 53601 (local agency investments), at California Public Law:
  https://california.public.law/codes/government_code_section_53601. Bank #96.
- Washington State Legislature (1999-2000). Senate Final Bill Report, SSJR 8208:
  https://lawfilesext.leg.wa.gov/Biennium/1999-00/Htm/Bill%20Reports/Senate/8208-S.FBR.htm. Bank #96.
- California Legislative Analyst's Office (1 Sep 1995). A Review of the Orange County Recovery Plan as Proposed August
  22, 1995: https://lao.ca.gov/1995/090195_orange_county/orange.html; Wood, D. B. (16 Dec 1994). Orange County Debt
  Squeeze Felt From Precinct to Classroom. *Christian Science Monitor*:
  https://www.csmonitor.com/layout/set/amphtml/1994/1216/16014.html. FR cautionary tale only (leveraged bonds). Bank #96.
- Zulauf, C. (15 Nov 2012). 2012 Drought, the Harvest Price Option, and Forward Contracting. *farmdoc daily*:
  https://farmdocdaily.illinois.edu/2012/11/2012-drought-the-harvest-price.html. Takes: best ratio 20-31% of expected
  production. Bank #97.
- Schnitkey, G. (24 Jul 2012). Consider Hedging RP Guarantee before Harvest. *farmdoc daily*:
  https://farmdocdaily.illinois.edu/2012/07/consider-hedging-rp-guarantee.html; Schnitkey, G. and Coppess, J. (15 May
  2018). Pre-Harvest Hedging and Revenue Protection. *farmdoc daily* (8):88:
  https://farmdocdaily.illinois.edu/2018/05/pre-harvest-hedging-revenue-protection.html. Bank #97.
- Leer, S. (27 Jun 2012). Drought could cost farmers with future delivery contracts. Purdue University News:
  https://www.purdue.edu/newsroom/archive/releases/2012/Q2/drought-could-cost-farmers-with-future-delivery-contracts.html;
  Walters, C. and Preston, R. (2022). Historical Corn Price Evolution Implications for Pre-harvest Hedging. UNL CAP:
  https://cap.unl.edu/news/historical-corn-price-evolution-implications-pre-harvest-hedging. Bank #97.
- Zulauf, C. R. and Irwin, S. H. (1998). Market Efficiency and Marketing to Enhance Income of Crop Producers. *Review of
  Agricultural Economics* 20(2), 308-331 (working paper 1997): https://ideas.repec.org/p/wpa/wuwpfi/9711004.html. Bank #97 (the break).

## Part 3. Five "aha" syntheses

### Aha 1. Laura's gift is a capped, principal-protected note, built without a single derivative
**Mechanism.** At 2031 the top is set at K = floor + half of VT's value then. In 2033 the gift is
min(floor + ½·VT₂₀₃₃, K). Since min(X, K) = K - max(K - X, 0), the gift equals the announced top minus half a put on
VT struck at its 2031 value: from 2031, co-sponsors hold a promise that pays the top unless world stocks fall over two
years, and never less than the floor. Before 2031, the structure is a bond floor plus 50% participation in VT: the
payoff of a principal-protected note with a participation rate and a cap. Laura is short the cap (she keeps everything
above it) and keeps the other half of VT.
**Why it is true.** The floor is a Treasury fund sized to grow to ~$150k by Dec 2032; VT is bought with the
interest that fund will earn, so VT can go to zero without touching the floor. That is CPPI with multiplier 1 and no
rebalancing, so it cannot "gap" (the failure that hurt dynamic portfolio insurance in 1987). Option-based insurance
needs options (banned); CPPI needs trading; this needs neither.
**Strongest objection.** "A bank sells this as one product; why not use it?" Answer: structured notes are not on
the permitted list, carry the issuer's credit risk and fees, and hide the cap. Laura's version is transparent, has US
Treasury credit, and costs 0.06-0.07% a year. Second objection: the floor fund's payout is NAV, not par, so the
"principal protection" is near-certain, not certain; hence the rounded-down bottom (vote D1b).

### Aha 2. A range is what game theory says a credible promise must look like, and the floor makes it a costly signal
**Mechanism.** Crawford and Sobel (1982) show that when sender and receiver interests differ (Laura wants
co-sponsors to give; they want an accurate figure), only coarse messages are credible, and equilibria take the form of
the sender naming an interval. The case asks for exactly that: a dollar range with confidence. Spence (1973) and
Leland-Pyle (1977) add that the message is believed when it is costly to fake: the bottom of Laura's range is money
already sitting in Treasuries, which a founder with a weak project would not lock away. The fund-raising literature
closes the loop: seed money and early leadership gifts raise later giving (Andreoni 1998; List and Lucking-Reiley
2002; Vesterlund 2003, where an early announced gift tells later donors the project is good).
**Why it is true.** The partition result is the central theorem of Crawford-Sobel; the seed-money effect is
documented in a field experiment (List and Lucking-Reiley) and theory (Andreoni, Vesterlund). The case text itself
uses signalling language ("may signal that the residency is financially viable").
**Strongest objection.** Crawford-Sobel is about one-shot talk; Laura's range is backed by assets, so it is closer
to a contract than cheap talk. Answer: that is the point. The floor turns the bottom of the interval from talk into a
commitment, and the cap stops over-promising, which the case says would "damage her credibility". The theory explains
the shape (an interval); the bonds explain why the bottom is believed.

### Aha 3. The 2028 deposit and the ladder's main risk move together, so the plan was right to lock the ladder first
**Mechanism.** The ladder costs more when yields fall (MODEL: ~$289 per basis point). Yields usually fall when the
economy weakens and the Fed cuts. Laura's 2028 deposit comes from publishing advances, speaking and licensing: income
that is likely to shrink in the same weak economy (human capital that behaves partly like stocks, Bodie-Merton-
Samuelson 1992). So the moment the ladder might need a top-up is also the moment the top-up money is most at risk.
**Why it is true.** The plan already answers it: the whole $300k buys the ladder in Jan 2027 before the uncertain
deposit exists; the 2028 deposit is only asked to fill a small gap, then fund the floor and VT. If the deposit falls
short, the facility gift shrinks, not the payments. The case says nothing certain may depend on outside money; the
plan extends that to "nothing certain depends on uncertain inside money".
**Strongest objection.** The correlation is assumed, not measured; a graphic novelist's licensing income might not
track the cycle at all. Answer: the plan does not need the correlation to be true, only to be possible; it is
robust either way. **Refinement:** state in the IPS that the 2028 deposit is used in order ladder gap, then floor, then
VT, so a smaller deposit cuts the upside first (this also settles vote D1a's framing).

### Aha 4. The STRIPS ban turns a solved problem into an unsolved one, and the old pension-fund fix halves it
**Mechanism.** With zero-coupon bonds, cash-flow matching is perfect: no coupons, no reinvestment. Wharton bans
STRIPS (and TIPS), so every rung pays coupons whose reinvestment rate is unknown. Fisher-Weil horizon analysis says
for a holder to maturity price risk vanishes and only reinvestment risk is left, and it bites only if yields fall and
stay down (~$21k MODEL at a lasting -2 points). Leibowitz's "dedicated portfolio" practice from 1980s pension funds
sizes all rungs together so that later bonds' coupons pay earlier payments directly instead of being reinvested; the
lab (R01) finds that roughly halves the exposure.
**Why it is true.** It is arithmetic: a coupon used to pay a bill is not reinvested, so it carries no reinvestment
rate. The remaining exposure sits in coupons paid before 2033, which must wait in a short Treasury fund.
**Strongest objection.** The ladder is already bought rung by rung; re-sizing it means trades, and WInS freezes on
6 Nov. Answer: the refinement applies to Laura's real plan (sizing in Jan 2027 and the Jan 2028 top-up), not to the
WInS book, and the IPS describes Laura's plan. It should be phrased as a rule ("coupons pay the next payment first"),
not as a trade.

### Aha 5. The plan's real stock-risk window is two years, not six, which is why "about 3 in 4" is believable
**Mechanism.** Before 2031, a fall in VT lowers the top of the range co-sponsors hear, but no promise is broken.
After the 2031 announcement, the cap is fixed, so the gift misses its top only if VT falls between the 2031
announcement and the 2033 gift. Kritzman and Rich (2002) show risk must be measured within the horizon at the points
where it matters; here the point is the promise. Bodie (1995) says insuring stocks costs more the longer the horizon:
the plan insures only the two-year window, and only partly (the floor), which is the cheapest part to insure.
**Why it is true.** Rough MODEL check: with 7.0% expected return and ~16.8% volatility (LTCMA AC World), the chance
that world stocks end a two-year window higher is about 2 in 3 to 3 in 4 depending on assumptions, which matches the
team's "~3 in 4 to reach the top" from the range model. The ~99% "inside the range" figure is high because the bottom
is owned bonds.
**Strongest objection.** The two-year window still includes crashes like 2008 (world stocks fell by roughly half
peak to trough; figure from memory, UNVERIFIED). Answer: then the gift lands near the floor, which was announced as the bottom, so the promise holds;
only the hope is lost. **Refinement:** in the Final Report, quote the confidence as two separate numbers (bottom:
near-certain from owned bonds; top: about 2-3 in 4 from a two-year stock window), which is clearer than a single
"99% inside" figure.

---

## Specific facts requested

| Fact | Status | Source checked (26 Oct 2026) |
|---|---|---|
| Redington's immunisation paper: 1952, *J. Inst. Actuaries* 78(3), 286-340, DOI 10.1017/S0020268100052811 | VERIFIED | https://www.cambridge.org/core/journals/journal-of-the-institute-of-actuaries/article/review-of-the-principles-of-lifeoffice-valuations/42DE39108ADCAD8D476B8E633F8E606F |
| Markowitz, "Portfolio Selection", *J. Finance* 7(1), 77-91, 1952 | VERIFIED | https://econpapers.repec.org/RAS/pma73.htm |
| Roy, "Safety First and the Holding of Assets", *Econometrica* 20(3), 431-449, July 1952 | VERIFIED | https://intouch.econometricsociety.org/publications/econometrica/1952/07/01/safety-first-and-holding-assets |
| Leland & Pyle, *J. Finance* 32(2), 371-387, May 1977 | VERIFIED | https://ideas.repec.org/a/bla/jfinan/v32y1977i2p371-87.html |
| Caplet = one period of an interest-rate cap (a call-style option on the rate for that period); floorlet = one period of a floor (put-style) | VERIFIED (tertiary; confirm against Hull, item 50) | https://en.wikipedia.org/wiki/Interest_rate_cap_and_floor |

Corrections found while checking: Kydland-Prescott's last page is 492 on the JSTOR print (not 491); the Econometric
Society lists Prospect Theory as 263-292; the TNA's "about 7.5% a year (as per JPMorgan)" for VT looks like the EAFE
figure, not AC World's 7.0% (re-check before the Final Report). **[Window 27 Oct: WRONG EDITION. J.P. Morgan's 2027 LTCMA (release 19 Oct 2026) gives global equities 7.5% (USD), up from 7.0%; the TNA's 7.5% is the world-stocks figure. See `../../office/outbox/2026-10-27_window_7-5-and-three-checks.md`.]**

## Added Mon 2 Nov 2026 (Library H-015, the verify round): sources re-checked at the page, for the Final Report's reading list
All read 2 Nov 2026 with WebFetch and re-checked by the Library (`../../huddles/2026-11-02_the-other-side-of-each-holding/research/README.md`, 48 of 48 lines found).
| Source | What it is for |
|---|---|
| iShares, *iShares iBonds Dec 2032 Term Treasury ETF* summary prospectus (cover 27 Feb 2026), https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf (IBTO-IBTQ the same, 27 Feb 2026; IBTR 25 Mar 2026) | The floor and the first five rungs in the issuer's words: index of Treasuries "scheduled to mature between January 1, 2032 and December 15, 2032, inclusive"; "will terminate on or about December 15, 2032"; "does not seek to return any predetermined amount at maturity" |
| iShares, "iBonds" (strategy page), https://www.ishares.com/us/strategies/ibonds | "Mature like a bond" / "iBonds ETFs payout their NAV in their maturity year."; "Government backing ... does not apply to the funds." |
| iShares Trust, Form 497 supplement, iBonds Dec 2024 Term Treasury ETF, 17 Oct 2024, https://sec.gov/Archives/edgar/data/1100663/000119312524238913/d894453d497.htm | What a fund's end looks like: "the Fund will automatically redeem your shares for cash based on the net asset value" (a sister fund; IBTM's own notice comes about Oct 2032) |
| 31 CFR 356.30, https://www.law.cornell.edu/cfr/text/31/356.30; TreasuryDirect, "Redeeming", https://treasurydirect.gov/marketable-securities/redeeming-marketable-securities | "We will pay principal ... on the maturity date"; "get the money (redeem it)": the T-bond rungs and R = redemption |
| Selina Taylor and Beverley Glass, "Altering dosage forms for older adults", *Australian Prescriber* 2018;41:191-3, DOI 10.18773/austprescr.2018.063 | Caplet XR's harm at an Australian source: crushed, "the duration of the drug's activity is reduced"; the fix, "alternative formulations" (slip S-11) |
| Haleon Australia, Panadol Osteo CMI (Jan 2026), https://www.safetyandquality.gov.au/medicine-finder/panadol-osteo-modified-release-caplets | A real Australian extended-release caplet, labelled: "Do not suck, crush or chew the caplets" |
| WA Health, *Don't rush to crush!*, https://www.health.wa.gov.au/~/media/Files/Corporate/general-documents/safety/PDF/Medication-safety-resources/Dont-rush-to-crush.pdf | "XR Extended release"; "Slow release medicines must never be crushed." |
| Patricia Cornish, "'Avoid the crush'", *CMAJ* 2005;172(7):871, DOI 10.1503/cmaj.050176 | "Crushing the tablet destroyed the drug's sustained-release properties" |
| NYU Stern, Prof. Carpenter, "Caps, Floors, and Collars" (Debt Instruments and Markets slides), https://pages.stern.nyu.edu/~jcarpen0/courses/b403333/18capfloor.pdf; HMRC CFM13340, https://www.gov.uk/hmrc-internal-manuals/corporate-finance-manual/cfm13340 | The bond trader's caplet ("a kind of call on the 0.5-year rate") and floor ("guaranteed a minimum rate of interest"): the Final Report's floorlet line on reinvestment risk (seed 3) |
