# Liability Actuary (LDI / pension defeasance)

## Proposal

# Liability Actuary report: pricing and securing the 2033-2042 operating reserve

## 1) Recommended strategy from my lens

**Secure the promise first, then grow the rest.** At today's Treasury curve, all ten $50k payments can be matched with Treasury zeros for about **$297k as of 1 Jan 2027**. That is roughly 99% of the first deposit and about two-thirds of the $450k Laura commits in total. Lock the whole ladder as soon as the money arrives, with each maturity falling just before its payment date. Everything above the locked amount is surplus, and it is the only money that takes equity risk. I recommend a rule-based framework: "hedge ratio = min(100%, assets ÷ Treasury-priced liability), and it only ratchets up." At current yields that rule gives the same answer as a full lock today.

## 2) Key numbers (sourced / ASSUMPTION)

**Curve inputs (par, as of 25 Sep 2026):** 2y 4.81%, 7y 5.06%, 10y 5.17%, 20y 5.45%, 30y 5.48%. The 5y figure of 4.99% comes from a snippet whose date is unclear, possibly a different day.
- These come from WebSearch result summaries of Advisor Perspectives, Forbes, primerates and the FRED/H.15 pages.
- I could not open any primary page. The egress proxy blocked home.treasury.gov, federalreserve.gov, FRED and all the aggregators. **The team must re-check these against Treasury's daily par curve before using them.**
- Context: 10y TIPS real yield about 2.85% and 10y breakeven about 2.28% (25 Sep 2026, per tipswatch/ecmsource snippets). A mid-September reopening of the 10y TIPS printed a 2.653% real yield.

**Zero curve.** I bootstrapped it from the par yields with linear interpolation (method is my ASSUMPTION). Zero rates for the payment dates, 1 Jan 2033 to 1 Jan 2042: **5.05%, 5.09%, 5.13%, 5.18%, 5.22%, 5.25%, 5.29%, 5.32%, 5.36%, 5.40%**. Real STRIPS trade a few bp away from a fitted curve.

**Liability pricing** (file `actuary/curve.py`):

| Measure | Value |
|---|---|
| PV today (28 Sep 2026) | **$289,724** |
| Forward PV at 1 Jan 2027 | **$296,692** (team's "~$297k" is confirmed) |
| Forward PV at 1 Jan 2028 | $307,597 |
| Implied cost of the reserve in 2033 if locked now | **$395,933** |
| Reserve cost in 2033 if bought then at a flat 5% / 4% / 3% / 2% | $405k / $422k / $439k / $458k |
| Modified duration | 10.0 |
| DV01 | $291 per bp |
| PV at +100bp / −100bp | $262.2k (−9.5%) / $320.5k (+10.6%) |
| PV at +200bp / −200bp | $237.6k / $355.1k |

- **Tail risk in the team's tiering plan.** Payments 2037-2042 have PV $154.4k today (2033-2036: $135.4k). Leaving them in short duration exposes the plan to **+$20.2k extra cost per −100bp** and **+$43.3k per −200bp**.

**Monte Carlo** (200k paths, `actuary/mc.py` and `sens.py`). All parameters are ASSUMPTIONS, not market data:
- Equities: 6.5% geometric return, 16% volatility.
- Rates: Vasicek model for the reserve yield level, starting at 5.1%, long-run mean 4.0%, speed 0.15, volatility 1%/yr.
- Correlation between equity and rate shocks: 0 or 0.3.
- Surplus is measured at 2033, after buying the reserve.

| Strategy | P(shortfall) | 1st pct surplus | 5th pct | Median |
|---|---|---|---|---|
| Full early lock (85% equity on surplus) | **0.00%** | $96k | $118k | $194k |
| Rule-based: floor 50%→100% by 2031, funded-ratio triggers 1.25/1.4/1.6 | 0.01-0.04% | $46-55k | $82-88k | $193-194k |
| Wait (75% equity, glide to 25%, buy in 2033) | **7.4-9.3%** | −$87k to −$110k | −$21k to −$38k | $185k |

- **Sensitivity to the equity assumption.** At 5% equity return, wait fails 10.3% of the time. At 8%, wait fails 5.1% of the time, and its median ($215k) is only slightly above the lock's ($205k).
- **Stress: the 2028 $150k never arrives.** Lock still funds the promise with $0.3-0.5k to spare. Rule-based and wait each fail about 53-55% of the time.

**Proposed definition of "high degree of certainty":**
1. The reserve is at least 100% funded on a *market-consistent* basis: assets ≥ PV of the 10 payments, discounted at the Treasury zero curve and not at an assumed return.
2. Each payment is matched by a Treasury cash flow maturing on or before its date, and bonds are held to maturity. The only residual risks are US Treasury default and operational error.
3. Before 2033, a modelled shortfall probability of no more than 0.5%. This is a 1-in-200 tolerance by analogy to the Solvency II 99.5% standard, a regulatory convention I cite from memory without a fetched source.

"95% Monte Carlo" wording is not enough on its own. Laura is a Wharton statistics graduate and will expect the model to be stated.

## 3) How this resolves the team's contradictions

**1. Lock-in timing.** Lock all ten payments early. Do not buy only 2033-2036 in 2033 and roll 2037-2042. The tiering plan was meant to avoid locking today's curve, but today's curve is the best reason to lock:
- Zero yields are 5.05-5.40%, and the 10y is near its highest since 2007 per the search snippets.
- Waiting turns a known $297k cost into an uncertain $370k-$470k 2033 cost (model 5th-95th percentile).
- Rising rates after locking only cause mark-to-market losses, which do not matter because the bonds are held to maturity.
- The rule-based version is the principled form: hedge whatever the Treasury-priced liability requires, from the first dollars, and ratchet only upward. At about 5% it means lock ~100% now. At 3% yields it would have meant lock what you can and add as funding allows.

**2. Risk budget.** "75% equities" cannot apply to the total portfolio. It applies to the **surplus** only, which is about $153k in 2027-28 (≈34% of committed capital) and can reasonably be 80-100% growth. Blended, the plan is about 66% liability-matching bonds and 34% growth once both deposits are in.

**3. Rate assumption.** Retire both the flat 4% and the 5.1% par figure. Price the reserve per maturity off the zero curve. Once the reserve is locked, its 2033 cost is a fixed number (about $396k), not a projection, so the projections only need return assumptions for the surplus.

## 4) Implications for the WInS portfolio and first trades

The approved securities list, starting capital, trade limits and sector minimum are all **unknown**, and the "6 sectors" claim is unverified. My proposal is to mirror the post-2028 steady state: roughly 2/3 liability-matching and 1/3 growth. Instrument types and their roles:

- **Target-maturity (defined-maturity) Treasury ETFs.** This is the best way to express the ladder. For example, iShares lists iBonds Dec 2033, 2034 and 2035 Term Treasury funds. A December-maturing fund pays out just before a 1 January payment, so the Dec 20XX fund funds the 1 Jan 20XX+1 payment. I have not verified whether 2032 or 2036-2041 vintages exist, or whether any of them are approved in WInS.
- **Intermediate and long Treasury index ETFs or zero-coupon/STRIPS ETFs.** Blend them to a duration of about 10 to immunise the maturities that a target-maturity fund cannot cover.
- **TIPS ETFs are not the core hedge.** The liability is fixed nominal, so TIPS create a mismatch. At most they go in the surplus sleeve, as a hedge against facility-cost inflation.
- **Growth sleeve.** Diversified equity ETFs or stocks across sectors. This is also where any sector-count rule would be met.

**Trading Note seed.** Record the entry-day zero yields and PV next to the trade, and note in a sentence how the trade reflects the strategy: "we bought the promise at $X."

## 5) Biggest weaknesses of my own proposal

- **The yields are unverified.** They come from search snippets only, the primary pages were blocked, and the 5y date is inconsistent. The real lock rate is set in January 2027, not today.
- **Full lock uses about 99% of the 2027 deposit.** A 2027 snapshot would be almost entirely bonds, which judges may read as under-diversified. It also caps the facility upside: median surplus is about $194k versus about $215k for waiting in the 8% equity case.
- **The Monte Carlo is only as good as its assumed parameters.** It uses a flat-level rate model with no curve twists and no fees; ETF expense ratios and the difference between STRIPS and a fitted curve are not priced in.
- **Locking nominal payments ignores inflation in Taiwan operating costs.** The case fixes the payments at $50k nominal, so the facility and flexibility sleeves bear that risk, along with TWD FX risk.
- **Ladder coverage may be incomplete.** Target-maturity ETFs may not cover 2036-2041, and duration proxies leave some curve risk.

## 6) Sources

All as of the WebSearch snippets retrieved 27 Sep 2026; none of these pages could be opened directly.
- https://www.advisorperspectives.com/dshort/updates/2026/09/25/treasury-yields-snapshot-september-25-2026 (10y 5.17%, 2y 4.81%, 20y 5.45%, 30y ≈5.48%; 25 Sep 2026)
- https://www.forbes.com/advisor/investing/treasury-rates/ (7y 5.06%; 25 Sep 2026)
- https://primerates.com/primerate/treasury-yield-curve/ (5y 4.99%, 10y 5.11%, dated "26 Sep 2026", which is inconsistent)
- https://www.federalreserve.gov/releases/h15/ and https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve (primary sources to verify against; blocked)
- https://tipswatch.com/2026/09/17/10-year-tips-reopening-gets-real-yield-of-2-653-highest-in-nearly-18-years/ and https://ecmsource.com/tips-breakevens-fall-hot-cpi-real-yields-september-2026/ (TIPS 2.85%, breakeven 2.28%; 25 Sep 2026)
- https://www.ishares.com/us/products/332291/ , https://www.ishares.com/us/products/337745/ishares-ibonds-dec-2034-term-treasury-etf , https://www.ishares.com/us/products/342105/ishares-ibonds-dec-2035-term-treasury-etf (target-maturity Treasury ETF type exists; WInS eligibility unknown)

Scripts are in /tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/actuary:
- curve.py
- mc.py
- sens.py
- zc.npy

## Cross-examination

## Liability Actuary cross-examination (verification script: `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/actuary/xexam.py`)

**Council-wide pricing problem.** Three reserve costs for 1/1/2027 are being quoted: $294k (Client, Quant), $296.7k (mine) and $297.7k (CIO). The main reason they differ is method, not the data:
- $294k prices today's spot zeros as if they still apply on 1/1/2027, with the curve unchanged and no roll-forward.
- $296.7k is the no-arbitrage forward price: PV today of $289.7k carried forward to 1/1/2027.
- $297.7k treats par yields as if they were zero yields.

The team needs to choose one method and use it everywhere. I recommend the forward-consistent one, quoted as "about $294–298k depending on method; repriced on the purchase date".

The same issue affects the 2031 and 2033 figures. The forward-implied cost is $356.9k at 2031, against the Client's $364k, and $395.9k at 2033, against the Quant's "$404k". The $404k is roughly what a flat 5% gives ($405.4k).

### Endowment CIO
- **Strongest point conceded.** The first $300k funds the promise, and any cost above $300k (for example after a rate fall) comes out of the 2028 deposit before any money goes to growth. This fixes my own weak spot. At a DV01 of about $298/bp, the $3.3k of headroom disappears if rates fall only **about 11bp** before January 2027.
- **Numbers verified.**
  - PV at 2027: **$297,745**. Reproduced exactly using their par-as-zero curve (5.02–5.245%).
  - Cost at −100bp: **$327,931**. Reproduced exactly.
  - Annuity-due at 5% / 4% / 3%: **$405.4k / $421.8k / $439.3k**. Reproduced.
  - Whole-portfolio equity: 0.7×150/450 = **23.3%**. Reproduced.
  - 2-year floor: 0.6×1.0481² = **0.659×V₃₁**. Reproduced.
- **Most serious flaw.** The capital-market assumptions contradict each other.
  - In the base case the bond sleeve earns **4.0%**, while the same memo quotes the 5-year at 4.98% and locks the ladder at about 5.1%.
  - The equity figures from JPM and Vanguard (Oct and Dec 2025) were set when yields were lower.
  - As a result the growth sleeve's risk premium is misstated. A judge who compares the bond return assumption with the quoted yield will notice.
  - Treating par yields as zeros also overstates the cost by about $1k. This is minor.

### Client & Credibility Strategist
- **Strongest point conceded.** The "floor plus stretch" rule for 2031 is the best answer the council has to the case's requirement for a range plus a confidence level. The floor is already paid for in Treasuries. The stretch has a stated probability that depends on the model. This fits Laura as a statistics graduate who started out fighting misinformation.
- **Numbers verified.**
  - F = 0.5×$86k×1.0487² = **$47.3k**. Reproduced.
  - TWD forward 31.79×(1.02/1.0481)² = **30.11**, which is **−5.3%**. They say 5.4%; the gap is rounding.
  - Real value of $50k at 2% inflation: **$43.5k in 2033 and $36.4k in 2042**. Reproduced.
  - Two-year equity factors: 5th percentile 0.748 and 90th percentile 1.45. Reproduced.
  - P(two-year loss) of **35.9%** holds only if 5.5% is read as the arithmetic mean. If it is the geometric median, the figure is 31.8%, so the label needs to be stated.
- **Most serious flaw.**
  - It says locking before 2031 is "optional". That leaves the reserve exposed to rates for four years, which every other member's Monte Carlo shows is where the shortfall risk comes from: 3–9% of paths, and about 40–60% if the 2028 deposit never arrives.
  - The $364k L31 assumes the curve is unchanged and is not a forward price.
  - Using the policy rate as a stand-in for the 2-year TWD rate in covered interest parity is weak, and should be labelled clearly as an assumption.
  - The fix is that the rule works as a layer on top of an early lock. It should not replace one.

### Quant Risk Modeler
- **Strongest point conceded.**
  - The finding that strategy (c)'s median hardly moves with the equity assumption, while (a)'s 5th percentile swings between $0 and $39k, is the most persuasive statistical case for locking.
  - It also shows that a "95% certainty" figure depends on whose model produced it.
  - The (a) funding probability is 96.7% in the Quant model, 95.6% (1−4.4%) in the CIO's JPM case and 90.7–92.6% in mine. Three models give three answers. This supports my proposal to define "high degree of certainty" in market-consistent terms (assets ≥ Treasury-priced liability) and not as a Monte Carlo percentile.
- **Numbers verified.**
  - "$626k implies about 6.0%": solving 300(1+r)⁶+150(1+r)⁵=626 gives **r = 5.99%**. Confirmed.
  - Macaulay duration from 1/1/2027: **10.05 years**. Confirmed.
- **Most serious flaw.** It tells the team their "$297k method is wrong" and gives **$294k** as the correct figure. But $294k assumes the curve stays unchanged. The no-arbitrage forward figure is **$296.7k**, so the team's number is actually closer. The team should not change a correct figure on the strength of a correction that is itself a matter of method.

### How my recommendation changes
1. **Kept.** Lock all ten maturities as early as possible, measure risk on the surplus, and hold about 2/3 in liability matching and 1/3 in growth once both deposits are in. All four members now agree on this.
2. **Added from the CIO.** A funding waterfall:
   - The 2027 deposit goes to the ladder up to its repriced cost.
   - Any shortfall comes first out of the 2028 $150k. If rates fall more than about 11bp, the 2027 deposit alone will not be enough.
   - Only the remainder goes to growth.
   - Record the lock-date yields in the Trading Notes.
3. **Added from the Client strategist.** Adopt "floor plus stretch" as the 2031 communication rule, applied only to the surplus sleeve. The reserve is already locked and is never part of the range.
   - The floor is put into a 2-year Treasury in 2031.
   - The stretch is quoted with its model stated.
   - The floor share a and pay-out share c are for the students to choose.
4. **Added from the Quant modeler.** Report probabilities rounded to at most two significant figures. Show the funding probability for the no-lock strategy across all three models as a range (about 91–97%), as evidence that model results are unstable.
5. **Unchanged caveats.** Every yield comes from a search snippet, because primary pages were blocked. The WInS rules are unknown, and the "6 sectors" claim is unverified. The numbers here are options for the students to decide on, not text to submit.

---

# Endowment CIO (growth and the facility contribution)

## Proposal

# Endowment CIO report: the growth engine and the facility contribution

## 1) Recommended strategy from my lens

**Lock the promise with the certain money, and grow the dream with the new money.** At current yields, a Treasury zero-coupon ladder paying $50k each year from 2033 to 2042 costs about **$298k at the start of 2027**. That is almost exactly Laura's first $300k deposit. So the first deposit should fund the promise, fully locked in. The 2028 $150k then becomes the facility and flexibility engine: about 70% global equity and 30% intermediate Treasuries until 2030, then stepping down in 2031–32 so the range Laura gives co-sponsors stays credible. The honest headline: with Treasuries near 5%, extra equity mostly widens the range of outcomes and adds little to the median. The engine should be sized for the upside, not sold as a guaranteed extra return.

## 2) Key numbers (Python Monte Carlo, 200k paths; scripts in `.../scratchpad/council/cio/model.py` and `m2.py`)

**Inputs**
- **Treasury curve, close 2026-09-25 (search snippet, see Sources):** 2y 4.81%, 5y 4.98%, 7y 5.06%, 10y 5.17%, 30y 5.47%. The 10y TIPS real yield was 2.85%, with a breakeven of 2.28%.
- **ASSUMPTION:** par yields, interpolated, stand in for STRIPS zero yields, and the curve is unchanged until January 2027.

**Cost of locking the reserve**
- PV at the start of 2027 = Σ 50,000/(1+zₜ)ᵗ for t = 6…15, with zₜ between 5.02% and 5.24%. Result: **$297,745**.
- If the curve falls 100bp before January 2027: **$327,931**, which exceeds $300k.
- Reserve cost at 2033 with a flat curve (annuity-due): $405k at 5%, $422k at 4%, $439k at 3%.

**Equity return assumptions**
- JPM 2026 LTCMA (Oct 2025): US large cap 6.7%, intermediate Treasuries 4.0%, 60/40 6.4%.
- Vanguard VCMM (Dec 2025): US equity 3.5–5.5%, non-US developed 4.9–6.9%, US aggregate bonds 4.1%.
- I ran two equity cases:
  - "JPM": 6.7% geometric.
  - "Vanguard blend": 5.1%, an ASSUMPTION built as 60% US at the 4.5% midpoint plus 40% non-US at the 5.9% midpoint.
- **ASSUMPTIONS:** equity volatility 16%, bond volatility 5%, correlation +0.2, lognormal returns independent year to year.

**Facility and flexibility sleeve at the start of 2033.** Money in: the $2.3k left after the ladder plus $150k in 2028. From 2031 the equity weight drops to 50%, then 25%, of the chosen weight w.

| Equity weight w | JPM 6.7% / bonds 4.0%: p5 / p10 / p50 / p90 | Vanguard 5.1% / bonds 4.0%: p5 / p10 / p50 / p90 |
|---|---|---|
| 40% | 152 / 160 / 195 / 237k | 148 / 157 / 190 / 232k |
| **70%** | **140 / 152 / 200 / 267k** | **135 / 146 / 193 / 256k** |
| 100% | 126 / 140 / 205 / 301k | 119 / 133 / 194 / 284k |

- Going from 40% to 100% equity adds only **+$10k to the median in the JPM case and +$4k in the Vanguard case**. It adds +$50–64k to p90 and costs −$26–29k at p5.
- If bonds instead earn the 4.98% 5y yield, the 70% median is $205k.
- 70% is my pick: it keeps about 75% of the p90 upside, and p10 stays near or above $146k.

**Stress test of the 2028 $150k** (JPM case)

| 2028 deposit | Locked-ladder design (A): p50 facility sleeve | P(reserve shortfall) | Team glide path (B): P(reserve shortfall) | B: p50 surplus |
|---|---|---|---|---|
| On time | about $206k | 0 | 4.4% | $222k |
| 1 year late | about $193k | 0 | 4.1% | $210k |
| Half ($75k) | about $105k | 0 | 16.3% | $120k |
| Never arrives | about $3k | 0 | 43.7% | $18k |

- Design B is the team's 75% equity glide path, with the reserve bought in 2033 at a random rate. **ASSUMPTION:** that 2033 rate is drawn from N(4.5%, 1%).
- With Vanguard assumptions, B's shortfall probabilities are 6.8%, 22.0% and 51.9% for on-time, half and zero.
- In A, the promise never depends on the $150k. Only the facility contribution shrinks.

**The 2031 co-sponsor range.** Take the sleeve value V₃₁ at the start of 2031, with the de-risked 2031–32 path. The 2033 value relative to V₃₁ is 0.95× at p5, 0.98× at p10, 1.10× at p50 and 1.24× at p90. The floor of the range should be moved into 2-year Treasuries at 4.81%. For example, putting 60% of V₃₁ there guarantees 0.66×V₃₁.

## 3) How this resolves the team's flagged contradictions

- **Contradiction #2, risk budget: "~75% equities" vs. a reserve that uses up the first deposit.** Both statements are true, but they are about different things.
  - Risk should be measured on the surplus (assets minus the liability), not on total assets.
  - With the reserve locked, the **whole-portfolio** equity weight in 2028 is about 0.7×150/450 ≈ **23%**, while the growth sleeve runs at 70%.
  - The "full risk budget" is still spent, just only on money that is not needed for the promise.
  - Design B's 75% applied to all the money is what creates the 4–7% chance of breaking the promise (16–52% if the 2028 money disappoints). A pension standard would not accept that.
- **Contradiction #1, lock-in timing.** From a growth lens, lock **all ten maturities at the start of 2027**. Rolling 2037–2042 in short bonds leaves reinvestment risk, and B shows that rate risk alone is material. If the curve falls before January 2027 and the cost rises above $300k (for example $328k at −100bp), fund the gap first from the 2028 deposit before anything goes to growth.
- **Contradiction #3, 4% vs. 5.1%.** Use the sourced curve (about 5.0–5.2% for 2033–2042 maturities) as the base case, and 4% and 3% as stress cases. The team's "~$297k" matches my $297.7k. The team's "$333k" used 4%, which the current curve does not support.

## 4) Implications for the WInS portfolio and the first trades

WInS P&L does not feed into the projections, so the WInS portfolio should be a **scaled mirror of the strategy**. Starting capital, the approved list, trade limits and any sector minimum are **unknown and unverified**. That includes the "6 sectors" claim.

**Target shape**
- **About 65% liability-hedge sleeve.** These should be defined-maturity Treasury ETFs dated 2033–2036 if they are on the approved list. Otherwise use long or intermediate Treasury ETFs, or a zero-coupon Treasury ETF as a STRIPS proxy. Their role is to lock the promise.
- **About 35% growth sleeve,** at 70/30:
  - US broad equity.
  - Developed ex-US equity, and a value tilt. Vanguard ranks non-US developed and US value among the best risk/return profiles.
  - Intermediate Treasuries as the stabiliser.
- If a sector minimum is confirmed, meet it inside the equity sleeve with sector funds or stocks across 6 or more sectors, so the minimum does not drive the allocation.

**Suggested first three trades** (each one a candidate Trading Note)
1. The liability-hedge anchor: "fund the promise first".
2. The global equity core: "grow only the surplus".
3. The intermediate Treasury stabiliser: "protect the 2031 range".

Avoid creator-economy theme bets.

## 5) Biggest weaknesses of my proposal

- **Two to five years of flexibility are given up.** If yields rise further, the locked ladder is behind on mark-to-market. It is still immune at maturity, but that is hard to explain to co-sponsors.
- **The facility is fully exposed to the $150k.** If it never arrives, the facility contribution is about $0. B keeps some upside in that case, but at an unacceptable cost to the promise.
- **Implementation gap.** Money arrives in January 2027, so the $298k cost depends on the curve then. STRIPS yields are not the same as par yields.
- **Stale assumptions.** The equity return figures are from Oct and Dec 2025, when yields were lower. The volatility and correlation figures are assumptions. The model uses independent lognormal returns with no fat tails or crashes, and equity–bond correlation could turn positive under inflation.
- **Sourcing.** Every figure comes from search-result snippets. WebFetch was blocked by network policy for treasury.gov, FRED, federalreserve.gov, jpmorgan.com, schwab.com and morningstar.com, so no primary page was opened. The team should check the numbers against the Treasury or H.15 tables before using them.
- **Not modelled:** TWD FX and Taiwan cost inflation on the facility.

## 6) Sources (all as seen in search results, 2026-09-27)

- Treasury closes 2026-09-25: https://www.advisorperspectives.com/dshort/updates/2026/09/25/treasury-yields-snapshot-september-25-2026 ; https://seekingalpha.com/article/4949891-treasury-yields-snapshot-september-25-2026 ; official table to verify against: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026
- 10y TIPS real yield 2.85%, breakeven 2.28%, as of 2026-09-25; 10y TIPS reopening at 2.653% on 2026-09-17: https://tipswatch.com/2026/09/17/10-year-tips-reopening-gets-real-yield-of-2-653-highest-in-nearly-18-years/ ; https://tipsyield.com/real-yields
- JPM 2026 LTCMA (released 2025-10-20): https://am.jpmorgan.com/us/en/asset-management/institutional/about-us/media/press-releases/jp-morgan-releases-2026-long-term-capital-market-assumptions/ ; https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/tmt/30-years-of-foresight-the-2026-ltcmas-in-focus
- Vanguard VCMM 2026 outlook (Dec 2025): https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/2026-outlook-economic-upside-stock-market-downside.html ; https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html
- Cross-check (2026 editions): Schwab US large cap 5.9%, Invesco 5.0%: https://www.schwab.com/learn/story/schwabs-long-term-capital-market-expectations ; https://www.morningstar.com/markets/experts-forecast-stock-bond-returns-2026-edition

## Cross-examination

# Endowment CIO cross-examination (Team Caplet council)

Recomputation script: `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/cio/xexam.py`

**Consensus so far:** all four members, including me, landed independently on locking the reserve early and growing only the surplus. The disagreements are about calibration, not direction.

## Liability Actuary

**Strongest point I concede.** The ratcheting rule "hedge ratio = min(100%, assets ÷ Treasury-priced liability)" is better than my fixed "lock at the start of 2027". It still gives the right answer if yields have moved by January 2027. It is also a policy statement the team can defend on Nov 6, when the strategy locks and can no longer be revised.

**Most serious flaw.** In the Monte Carlo, the reserve yield mean-reverts from 5.1% towards a 4.0% long-run mean. That is a forecast that rates will fall, and it raises the 2033 reserve cost on the "wait" path. So the 7.4–9.3% "wait" failure rate is partly built in by the assumptions.
- The Quant uses rates with no drift (AR(1) shifts around today's curve) and gets a 3.3% failure rate for a similar strategy. That is less than half.
- The conclusion survives either way: both numbers are far above a 0.5% tolerance. But the team should quote failure probabilities as model-dependent (roughly 3–9%), not as a single figure.
- Separately, the Solvency II 99.5% analogy is cited "from memory". Under the hard rules it has to be sourced or labelled as an ASSUMPTION.

**Numbers checked** (same zero rates, my day count):

| Item | Actuary | My recompute |
|---|---|---|
| PV today | $289,724 | $291,624 |
| Forward PV at 1/1/2027 | $296,692 | $295,253 |
| Implied 2033 cost | $395,933 | $397,003 |
| DV01 / modified duration | $291 / 10.0 | $286 / 9.8 |
| Extra cost of 2037–42 tail at −100bp / −200bp | $20.2k / $43.3k | $19.9k / $42.6k |

- All confirmed within about $2k.
- The gaps come from compounding and day-count conventions. That $1–4k is also the honest precision of every "$29Xk" figure in this council.

## Client & Credibility Strategist

**Strongest point I concede.** "Guaranteed floor plus stretch" is the most credible thing to tell co-sponsors. It speaks directly to the "Client Knowledge" and "Creativity/credible communication" criteria, and it keeps Laura from overstating. That fits both her anti-misinformation history and her statistics training. The List & Lucking-Reiley caveat (evidence for the mechanism, not a prediction) is handled correctly. I adopt this framing for my 2031 range.

**Most serious flaw.** Calling a pre-2031 lock "optional" contradicts the Strategist's own numbers.
- The Strategist shows L31 moving ±$34k for ±150bp. Delaying the lock hands that rate risk to the promise.
- The rule also leaves 50% of S in equities for 2031–32. That is a 36% chance of losing money over two years, and it sits inside the window where the range has just been communicated.
- The resulting range is lopsided. At V31 = $450k, the median ($70.6k) sits only $8k below the upper figure ($78.5k). The "stretch" is barely a stretch, so co-sponsors would effectively be told a number near the median.
- The a = 50% and c = 50% shares are arbitrary. The Strategist admits this.

**Numbers checked:**
- Floor: F = 0.5 × 86k × 1.0487² = **$47.3k**. Confirmed ($47k).
- Two-year equity factors: P(loss) = **0.359**, p5 **0.748**, p90 **1.45**. Confirmed.
- Median contribution **$70.6k** and U = **$78.5k**. Confirmed.

## Quant Risk Modeler

**Strongest point I concede.** Adding equity to the locked design barely moves the median. Going from 70% to 100% growth-sleeve equity adds about $2k to the median while the 5th percentile falls. My own table shows the same thing: +$4–10k from 40% to 100%. I will lower my 70% (see the last section).
- The Quant's challenges to the team notes are exactly what a Wharton judge would ask. I checked one: $626k implies a flat **5.99%** return. Confirmed.

**Most serious flaw.** The council now quotes three different Vanguard US equity ranges, all "Vanguard":
- mine: 3.5–5.5%
- Strategist: 3.9–5.9%
- Quant: 4.2–6.2%

All of them come from snippets. At most one of them is right for any given Vanguard publication date, and a judge who spots the inconsistency discounts everything else.

A second problem: "floor = 0.96 × S2031 with 95% confidence" is a conditional-model percentile, and the memo itself warns against mixing conditional and unconditional intervals. The Quant's own fix (move the floor into a 2-year Treasury) should replace the 0.96 figure, not sit beside it.

**Numbers checked:**
- 2y floor growth: 1.0481² = **1.0985**. Confirmed (×1.10).
- 2033 reserve cost "about $404k": an annuity-due at a flat 5% is **$405.4k**, versus about $397k on the forward curve. That is an $8k spread between two defensible methods, and the team should pick one.
- The "−100bp costs about $46k of median facility" figure is consistent in size with my ladder shock compounded to 2033 at 5.1% (**$40.7k**).

## Flags for the team (not decisions)

- The team should verify one yield curve against the Treasury daily par table or H.15 on a single date. Every member used snippets, and the 5y/7y/20y points differ by date (9/23 vs 9/25).
- The team should confirm the actual Vanguard figure and publication date before any equity number appears in the IPS.
- Across four independent models:

| | Reserve cost at 1/1/2027 | Median 2033 facility |
|---|---|---|
| Range across models | $294–298k | $194–212k |

  The team should present these as ranges, not three-significant-figure points.

## How my recommendation changes

1. **Lock rule.** I replace "lock everything at the start of 2027" with the Actuary's ratchet rule. Unchanged: fund any shortfall from the 2028 deposit before anything goes to growth.
2. **Growth-sleeve equity.** I cut it from 70% to about 50–60% for 2028–30. The Quant's and my own results show the extra median is under about $10k. Lower equity also makes the 2031 range tighter and more credible.
3. **2031 communication.** I adopt the Strategist's floor plus stretch, with these changes:
   - The whole reserve is already locked by then, so it is not optional.
   - The floor is bought as a 2-year Treasury in 2031, which gives a ×1.0985 guarantee at today's 2y rate.
   - The floor share is set by a stated rule (for example, the Quant's p5 ratio of about 0.95 × S) rather than a flat 50%. The share leaves the stretch more room.
4. **Unchanged:** WInS mirrors the post-2028 steady state, about 65/35 hedge/growth. WInS rules are still unverified.

The team, not the council, should choose the share parameters and write the wording for Laura. This analysis is brainstorming input under the Wharton AI policy.

---

# Client & Credibility Strategist

## Proposal

## Client & Credibility Strategist report (Team Caplet council, 2026-09-27)

### 1) Recommended strategy (central idea)
The 2031 co-sponsor figure should be a **rule**, not a forecast: "a guaranteed floor plus a stretch amount". In 2031 we price the whole operating reserve at that day's Treasury prices and lock it in zero-coupon Treasuries maturing 2033–2042. We call what is left the surplus S. Half of S goes into a Treasury maturing in 2033, and that becomes the floor Laura promises. The other half stays invested, and Laura gives some of its 2033 value on top of the floor. She is never asked to promise a number she can't guarantee. She promises a floor that is already paid for, plus a stretch figure stated with a calibrated probability. That matters for a statistics graduate whose public work began as a response to misinformation.

### 2) Key numbers (computed in `client/rule.py`)
**Market inputs:** 2y par 4.81%, 10y 5.17% (2026-09-25); 5y 4.99%, 7y 5.05%, 20y 5.45% (2026-09-23); 30y 5.49%. I bootstrapped these into zero-coupon rates, which run from 4.87% at 2 years to 5.31% at 11 years (annual compounding). Linear interpolation between maturities is an ASSUMPTION.

**Caveat on sourcing:** the egress proxy blocked treasury.gov, federalreserve.gov, FRED and most other pages. Every market number below therefore comes from WebSearch result snippets and was not checked against the source page. The team should confirm them on Treasury.gov or H.15 before using them.

**Rule parameters:** the floor share a = 50% and the pay-out share c = 50% are ASSUMPTIONS for the team to choose. The invested half is modelled as equities at 5.5% expected return and 16% volatility, lognormal, over two years (ASSUMPTION). The 5.5% sits slightly above Vanguard's base case for US equities of 3.9–5.9% a year over 10 years, on the reasoning that a globally diversified sleeve does a little better.

- **Cost of the reserve at 1/1/2031 (L31)**, assuming today's curve: **$364k**. With rates 1.5 points lower it is $398k; 1.5 points higher, $335k.
- **Cost at 1/1/2027** with the curve unchanged: **$294k**. That is 98% of the first $300k deposit.
- **Rule outputs** (the floor is guaranteed by Treasuries; the upper figure U is the 90th percentile):

| 2031 portfolio (V31) | Surplus S | Floor F (2033) | Upper U | Median contribution | Flexibility kept (median) |
|---|---|---|---|---|---|
| $450k | $86k | $47k | $78k | $70k | $23k |
| $550k | $186k | $102k | $169k | $152k | $50k |
| $650k | $286k | $157k | $261k | $234k | $77k |

  Formulas: F = a·S·(1+z₂)², where z₂ is the 2-year zero rate; contribution = F + c·(invested half at 2033); P(contribution ≥ F) ≈ 100%, limited only by Treasury credit risk; P(F ≤ contribution ≤ U) = 90% under the model.
- **What the equity half does over two years:** it loses money 36% of the time; the 5th-percentile growth factor is 0.75 and the 90th is 1.45. This is why the floor has to be locked and can't be left invested.
- **Missing 2028 contribution:** if Laura's $150k never arrives, V31 is roughly $365k, about equal to L31. S is then about zero and the rule says to promise a floor of $0 and only an aspiration. The rule protects her automatically.
- **Currency:** USD/TWD was 31.79 on 2026-09-24. Over six months it ranged from 31.32 to 32.41, and the TWD was down 4.1% over 12 months.
  - The Taiwan central bank's policy rate is 2.0%. Using it as a proxy for a 2-year TWD rate (ASSUMPTION), covered interest parity puts the 2-year forward at about 30.07. A USD promise is therefore worth about 5.4% fewer TWD if Laura locks the rate.
  - Assuming 5–7% annual volatility (ASSUMPTION, not sourced), a bad (5th-percentile) outcome is TWD 11–15% stronger by 2033.
- **Taiwan inflation:** 2.4% year on year in August 2026 (snippet citing DGBAS). The central bank's forecasts are 2.0% for 2026 and 1.8% for 2027. Annual averages were 2.2% in 2024 and 1.66% in 2025. At an ASSUMED 2% a year, the fixed $50k is worth about $43.5k in 2026 money in 2033 and about $36.4k in 2042. That is a real-terms squeeze on the residency's operations for the team to raise with Laura. It does not change the nominal liability.
- **Seed-money claim:** the claim checks out, but it needs context.
  - List & Lucking-Reiley, *JPE* 110(1):215–233 (Feb 2002). Raising seed money from 10% to 67% of the goal gave "nearly a sixfold increase" in contributions, and refunds added about 20%.
  - The setting was direct-mail letters to 3,000 Central Florida households for university computer equipment, raising $5,509 from 183 donors (about $30 each).
  - It shows that visible committed money raises other people's giving. It does not show how institutional co-sponsors behave. The team should cite it as evidence of a mechanism, not as a prediction.

### 3) How it resolves the team's flagged contradictions
1. **When to lock the reserve.** The rule decides this. By 1/1/2031 the whole reserve must be locked in zeros maturing on each payment date, because the promise made in 2031 must "protect the operating commitment". The Philosophy section's plan to keep 2037–2042 in short bonds until three years before each payment would leave the reserve exposed to rates after Laura has spoken to co-sponsors, so we reject it. Locking part of the reserve before 2031 is optional.
2. **Risk budget.** The reserve costs $294k against the first $300k deposit, so "75% equities" is not affordable if we fully lock early. The honest framing: the real risk budget is roughly the $150k 2028 deposit plus whatever the market provides. Laura's money pays for a promise first and the dream second. A useful sourced point: Vanguard's base case for US equities (3.9–5.9%) is about the same as the ~5.1% zero-coupon Treasury rate, so locking early costs little expected return today.
3. **Rate assumption.** Drop the flat 4% and "10y 5.1%". Use today's zero curve and show ±150bp stresses. In 2031 the rule uses that day's prices, so no rate forecast is needed.

### 4) Implications for WInS and the first trades (types only)
Approved securities, sector minimums and trade limits are unknown to us. The "at least 6 sectors" rule is unverified.
- **Liability anchor:** Treasury exposure with a duration that roughly matches 2033–2042. Use long-dated Treasury or STRIPS-type funds if they are allowed; otherwise intermediate or long Treasury funds.
- **Floor anchor:** short Treasury or T-bill funds, standing for the 2-year floor bond.
- **Growth sleeve:** broad, diversified equity index funds, plus any sector positions needed to meet the (unverified) sector minimum. Choose them by role, not by story. Avoid a "creator economy" theme.
- **Optional:** TIPS as a reference for Taiwan-facing inflation, and a TWD or Taiwan exposure only if it is approved and justified as a currency-hedge argument.
- **Trading Notes:** each note should say which bucket a trade serves (promise, floor or dream).

### 5) Biggest weaknesses of this proposal
- a = 50% and c = 50% are judgement calls with no optimisation behind them.
- The 90% "stretch" confidence depends entirely on the model assumptions: lognormal returns, 5.5%/16%, no fat tails. The model is simple and should be described that way.
- It assumes the 2031 curve looks like today's. If rates fall, L31 rises by about $34k, and early locking only partly protects against that.
- Currency risk sits with the facility, but the facility's currency isn't given in the case. Denominating the promise in USD with a TWD reference, or stating a TWD floor with a 15% haircut, are both team choices.
- The seed-money evidence comes from small household gifts. Applying it to co-sponsors is an inference.
- Every market number is from a search snippet, not a fetched source page.
- AI policy: the co-sponsor wording and the "floor plus stretch" framing must be written by the students.

**What makes judges think the team understands Laura:**
- Use her statistics training properly: define what "90% confidence" means, including the model and what it leaves out, and add a calibration check.
- Connect her anti-misinformation origin to "we never overstate".
- Point out that the rule removes the risk from her lumpy income, since the 2028 deposit is handled automatically.
- Tie her product-manager instinct to the phased rule.
- As a graphic novelist, she could show co-sponsors the floor and stretch as a simple visual, such as a "filled/unfilled" gauge. The students should create this themselves.
- Set her quote, "the only person who needs to believe… is yourself", against the fact that co-sponsors must believe too.

### 6) Sources (all accessed 2026-09-27 via WebSearch; pages could not be fetched)
- Treasury yields 2026-09-25 (2y 4.81%, 10y 5.17%): https://www.advisorperspectives.com/dshort/updates/2026/09/25/treasury-yields-snapshot-september-25-2026
- 30y 5.49% 2026-09-25: https://www.forbes.com/advisor/investing/treasury-rates/
- 5y/7y/20y 2026-09-23 (snippet): https://primerates.com/primerate/treasury-yield-curve/ and https://www.federalreserve.gov/releases/h15/
- 10y TIPS 2.85% and breakeven inflation 2.28%, 2026-09-25: https://fred.stlouisfed.org/series/T10YIE and https://tipsyield.com/real-yields
- USD/TWD 31.787 on 2026-09-24, and the six-month range: https://tradingeconomics.com/taiwan/currency and https://wise.com/us/currency-converter/twd-to-usd-rate/history
- Taiwan CPI 2.4% (Aug 2026): https://www.ceicdata.com/en/indicator/taiwan/consumer-price-index-cpi-growth
- Taiwan 2024/2025 averages: https://www.focus-economics.com/country-indicator/taiwan/inflation/
- Taiwan central bank inflation forecasts (2.0% for 2026, 1.8% for 2027) and 2.0% policy rate, Sept 2026: https://finimize.com/content/taiwans-central-bank-edged-up-its-2026-inflation-view and https://www.vtmarkets.com/en-asia/live-updates/taiwan-central-bank-holds-rates-at-2-0-as-inflation-forecast-edges-up-growth-surges/
- Vanguard 2026 outlook (Dec 2025): https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/2026-outlook-economic-upside-stock-market-downside.html
- List & Lucking-Reiley 2002: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=295075 and https://ideas.repec.org/p/van/wpaper/0008.html (UCF design and $5,509 from 183 donors, per https://www.nber.org/reporter/2008number4/using-field-experiments-economics-charity)

Computation: `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/client/rule.py`

## Cross-examination

## Cross-examination: Client & Credibility Strategist (2026-09-27)

I rechecked the figures with a Python script: `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/xexam/x.py`. Every yield in it is still a search snippet, as the other members also note.

### Liability Actuary

**What I concede.** Their standard for "high degree of certainty" is the strongest idea on the council. Assets must be at least the Treasury-priced value of the liability, each payment is matched with a bond held to maturity, and the only risks left are Treasury default and operational error. That is exactly how I would explain "never overstate" to Laura. Their ratchet rule, hedge ratio = min(100%, A/L), turns "lock early" into a policy rather than a view on rates.

**Most serious flaw: a bias built into the model.** In the Vasicek model the rate starts at 5.1% but reverts to a long-run mean of 4.0%. So the model expects rates to fall by 2033, which pushes up the cost of buying the reserve later. That is part of why the "wait" strategy fails 7.4–9.3% of the time. The Quant's AR(1) model centres on today's curve and gets a 3.3% failure rate. The case for locking still holds, but the actuary's headline failure rate is inflated by a hidden rate forecast. A judge who spots it would discount the table.

**Other problems:**
- The Solvency II 99.5% standard is quoted "from memory" and not sourced. It should be sourced or dropped.
- Their own numbers do not reconcile:
  - Their listed zero rates give a PV of **$291.6k** today, not $289.7k.
  - Carrying that forward to 1/1/2027 at the 2y rate of about 4.8% gives **$295.2k**, not $296.7k. Moving $289.7k forward over 0.26 years to reach $296.7k would need about a 9.5% annual rate.
  - These are small gaps, but they are the kind a statistics-trained client would find.

**Numbers I checked:**
- 2033 annuity-due at a flat 5% / 4% / 3% / 2%: **$405.4k / $421.8k / $439.3k / $458.1k.** Confirmed.
- ±100bp: I get $264.6k / $321.9k against their $262.2k / $320.5k. DV01 is $286 against their $291. Macaulay duration is 10.3, so modified duration is about 9.8 against their 10.0. Close enough.
- Implied 2033 cost if locked now: $397.0k against their $395.9k. Close.

### Endowment CIO

**What I concede.** Measure risk on the surplus, not on total assets. Once the reserve is locked, 70% equity in the growth sleeve is only about 23% of the whole portfolio. They also show that going from 40% to 100% equity adds only +$4–10k to the median. That settles contradiction #2 and gives the team an honest line: "extra equity buys range, not return."

**Most serious flaw.**
- **Par yields used as zero rates.** Their $297,745 reproduces exactly, but only because par yields were used as if they were zero-coupon rates. On an upward-sloping curve, zero rates sit above par yields. So this overstates the cost by about $3–4k against the bootstrapped figures of $294–295k, which is the Quant's point.
- **The same rate bias as the actuary.** In Design B, the 2033 rate is drawn from N(4.5%, 1%), below today's roughly 5.1%.
- **A plan that ties the promise to the 2028 money.** "If the curve falls, fund the gap from the 2028 deposit" means the operating promise partly depends on the one cash flow the case makes uncertain. Their own stress test calls that dependence unacceptable. They should say plainly that Laura may have to accept a short delay or a partial lock in 2027.

**Numbers I checked:**
- 0.6 × 1.0481² = **0.659**. Confirmed.
- Equity share 0.7 × 150/450 = **23.3%**. Confirmed.
- Reserve cost of **$327,931** at −100bp. Confirmed, though it carries the same par-as-zero bias.

### Quant Risk Modeler

**What I concede.**
- It is the fairest model on the council: the rate process is centred on today's curve, and seeds and fat tails are tested.
- It gives the best headline: "(a) beats (c) on only 57% of paths."
- Its list of challenges to the team's notes is correct. The "$626k" implies a flat **5.99%** return (I recomputed it). The 20% drawdown claim ignores that by 2032 the portfolio is only 25% equity.
- Its "what a stats client would ask" list matches my Laura framing.

**Most serious flaw: a model percentile offered as a floor.** The Quant recommends "Floor = 0.96 × S2031 at 95% confidence" as what Laura tells co-sponsors. But the case says the 2031 range must *protect the operating commitment*, and it has to hold up in front of co-sponsors. A 95% floor that depends on the model is exactly the "95% under whose model?" problem the Quant raises against others. The Quant mentions the fix, locking in a 2-year Treasury (×**1.0985**, confirmed), only as optional. It should be the default.

**Smaller points:**
- The equity premium comparison is inconsistent across members. Three different "Vanguard US equity" ranges are cited from snippets: 3.5–5.5% (CIO), 3.9–5.9% (mine) and 4.2–6.2% (Quant). The council needs one verified figure.
- Their "(c) median $212k" and the CIO's "$200k" are not reconciled. The gap comes from different equity weights and bond returns, which is fine but should be stated.

### Cross-cutting issue for all of us, including me

All four proposals lock about 98–99% of the first deposit. The case says the reserve is "set aside at the start of 2033". Locking economically in 2027 and formally setting the reserve aside in 2033 is consistent with that, but the IPS must say it in one clear sentence or a judge may read it as a misreading of the case.

The WInS portfolio should mirror the post-2028 steady state, roughly 65/35. None of us knows the approved-securities list, and the 6-sector rule is still unverified.

### How my recommendation changes

1. **The reserve is locked in full at 1/1/2027, not "by 2031".** Actuary, CIO and Quant independently agree, and their three models, despite their biases, all favour it. My $364k cost for locking in 2031 and the ±150bp stresses are no longer the main plan. They become the illustration of what waiting would have cost.
2. **My floor-plus-stretch rule now applies to the growth sleeve only.** S₂₀₃₁ is that sleeve's value; the reserve is no longer netted out of it. At the Quant's median S₂₀₃₁ of $189k and a = 50%, the floor is 0.5 × 189 × 1.0985 ≈ **$104k**. That floor is guaranteed by a 2-year Treasury, not held at 95% confidence. This merges my rule with the Quant's range and the CIO's 2-year floor, but with the floor *locked*.
3. **The 2028 downside becomes cleaner to explain.** If the $150k never arrives, the promise is still fully funded and the facility floor is about $0–9k. Laura tells co-sponsors "aspiration only", and the rule does this automatically.
4. **I am adopting the actuary's three-part certainty definition** as the standard for the operating commitment. Solvency II should be sourced or dropped.
5. **The a and c shares stay open for the students to choose.** The CIO's p5/p50 table is the evidence they should use to pick a.

Open items the students must do themselves:
- Verify all yields on Treasury.gov or H.15.
- Settle on one bootstrap method; this gives $294–295k, not $297–298k.
- Settle on one sourced equity assumption.
- Write the co-sponsor wording in their own words, per the AI policy.

---

# Quant Risk Modeler & Statistical Skeptic

## Proposal

# Quant Risk Modeler and Statistical Skeptic: council memo

Model code and output are in `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/quant/` (`curve.py`, `mc.py`, `report.py`, `extra.py`, `report.txt`). Settings: 100,000 paths, seed 20260927, yearly steps from 1/1/2027 to 1/1/2033. The Monte Carlo standard error on any probability near 0.97 is about 0.06 percentage points, and seeds 1 to 3 reproduce the results to within ±0.1 pp.

## 1) Recommended strategy from my lens
**Strategy (c): lock in the full reserve early, then grow the surplus.** On 1/1/2027, use about $294k of the first $300k to buy zero-coupon Treasuries (STRIPS) maturing at each payment date from 2033 to 2042. Nearly all of the 2028 $150k goes into a separate growth sleeve for the facility.

At current yields of about 5%+, the equity return premium over locked Treasuries is thin, about +1.5 pp at J.P. Morgan's 6.7% and zero or negative against Vanguard's 4.2–6.2% range. So strategy (a) gives up very little by locking in. In exchange the ten payments become arithmetic, not a probability, and the facility outcome becomes much narrower.

In 2031, the facility floor Laura communicates to co-sponsors should be a rule based on the growth sleeve's value at that time, not a fixed dollar figure.

## 2) Key numbers (sources and assumptions)
**Market data (see §6):**
- Par yields as of 9/23–9/25/2026: 2y 4.81, 5y 4.99, 7y 5.05, 10y 5.17, 20y 5.45, 30y 5.49.
- I bootstrapped these into zero rates for 2033–2042: 5.03% rising to 5.39%.
- ASSUMPTION: the curve is flat below 2 years.

**Model assumptions:**
- Equity:
  - Median return 6.7% a year (JPM 2026 LTCMA, US large cap).
  - Volatility 16%. ASSUMPTION: typical large-cap volatility, not sourced this session.
  - Lognormal and independent year to year. I also tested fat tails (Student-t with 4 degrees of freedom).
- Rates:
  - Today's curve moves up and down in parallel shifts.
  - Shifts follow an AR(1) with φ=0.9 and 90bp/yr volatility. ASSUMPTION: roughly historical.
  - Correlation between equities and rate moves: 0 in the base case. I also tested -0.3.
- Bond sleeve: duration-5 Treasury fund.
- Glide path for (a): equity at 75% from 2027 to 2030, then 50% in 2031 and 25% in 2032.
- Reserve: all strategies end with a Treasury ladder in 2033. Strategy (a) buys it at 2033 market prices.

**Base results:**

| | (a) no lock, 75% then glide | (b) calendar lock + 125% trigger | (c) full early lock |
|---|---|---|---|
| P(all ten payments funded) | **96.7%** | ~100% | 100%* |
| 2033 facility contribution, 5th/25th/50th/75th/95th pct | 20/135/233/348/555k | 130/175/212/258/341k | **146/182/212/248/313k** |
| Mean / SD | 253k / 166k | 221k / 65k | 218k / 52k |
| P(facility < $100k) | 17.2% | 0.6% | 0.0% |
| 95% floor as a share of 2031 surplus (q05) | 0.60 | 0.96 | 0.96 |

\*The 100% holds only if Treasury credit risk is taken as zero.

- (a) beats (c) on only 57% of paths.
- For (a), the reserve cost in 2033 ranges from 362k to 455k (5th–95th pct) because of rates alone.

**2031 floor and range for (c):**
- The growth-sleeve surplus in 2031 has a median of 189k (5th–95th pct: 135–268k).
- **Floor = 0.96 × S2031** holds with 95% confidence (S2031 = growth-sleeve surplus in 2031).
- A 90% range of **[0.96, 1.33] × S2031** gives about **181k–251k** at the median.
- To make the floor certain rather than 95%, move the floor amount into a 2-year Treasury in 2031. It then grows by ×1.10 by 2033, at the current 2y rate of 4.81%.

**Sensitivity (median facility; 5th percentile; P(all funded) for (a)):**

| Scenario | (a) | (c) |
|---|---|---|
| Equity return 4.2% | 182k, p5 0; 93.4% | 197k; p5 136k |
| Equity return 7.8% | 256k; 97.6% | 219k |
| Equity vol 20% | p5 0; 93.5% | p5 134k |
| Rate vol 150bp | 95.8% | unchanged |
| Rates 100bp lower before we lock | 95.1% | median falls to 166k (the cost of waiting) |
| Rates 100bp higher | — | median 257k |
| **2028 $150k never arrives** | **60.1%**; median 29k | still 100%; facility ~9k |
| 2028 contribution only $75k | 86.5% | 100%; median 110k |

- (c)'s median barely moves with the equity assumption, because it takes little equity risk.
- A growth sleeve at 100% equity in (c) raises the median by only +2k and lowers the 5th percentile to 131k. It is not worth it.

## 3) How this resolves the team's flagged contradictions
1. **Lock-in timing.** Rolling 2037–2042 in short bonds leaves the reserve exposed to falling rates. -100bp at the start costs about $46k of median facility. Lock the full ladder now. There is no statistical benefit to waiting unless the team has a view on rates, and that would be a forecast, not a policy.
2. **Risk budget.** The notes are right that the reserve PV (~$294k) is about the whole first deposit. So "75% equity" applies to Laura's total wealth only under (a). Under (c) it applies to the growth sleeve only, about 35% of $450k.
3. **Rate assumption.** Use one curve, not 4% in one place and 5.1% in another. That curve is the bootstrapped zero curve of 5.03–5.39%.

**Numbers in the team notes I would challenge:**
- The "$297k at 10y 5.1%" is close in size, but the method is wrong (it uses the 10y par yield). The 9/25 10y was 5.17. The zero-curve answer is **$294k**, repriced on the day of purchase.
- "$626k projected" implies an unstated flat 6.0% return. It is also compared against a reserve priced at 4% (422k), which is inconsistent. At today's curve the reserve costs about $404k.
- "A 20% drawdown to $501k": by 2032 the portfolio is only 25% equity, so a 20% total loss would need roughly an 80% equity crash. It also ignores that rising rates cut the reserve cost at the same time. Use the joint distribution instead.
- "Risk-free floor ~$140k": the source is unknown. It is close to (c)'s 5th percentile (146k), but that is a percentile, not risk-free.
- "~100% certainty": say "certain given no US Treasury default", not a probability from a model.
- Unverified in this session: List & Lucking-Reiley's "~6x", Taiwan inflation of 1.8–2.2%, and "6 sectors".

**What a statistics-trained client would challenge:**
- "95% under whose model?" The answer depends on parameters. For (a), the 5th percentile swings from $0 to $39k.
- Assuming returns are independent year to year and bonds and equities have zero correlation; 2022 had both falling together.
- Confusing a conditional interval (given 2031) with an unconditional one.
- Showing 3 significant figures on quantities with ±30% parameter uncertainty.

## 4) Implications for WInS and the first trades
WInS rules are unknown to us: approved list, sector minimum, trade limits and starting capital are all unverified. The trades below are instrument types and roles only.
- **Liability-matching sleeve (about 65% of $450k):**
  - Defined-maturity Treasury funds (target-maturity bond ETFs), or STRIPS maturing 2033–2042, if approved.
  - If not, a long or intermediate Treasury fund sized so its duration matches the liability. The liability's Macaulay duration is about **10.0 years** in 2027.
- **Growth sleeve (about 35%):** diversified broad equity, with enough sector funds or stocks to meet whatever sector rule turns out to be real.
- **Decision for the team:** WInS today represents a moment before 2027, when only $300k exists and the lock would take 98% of it. I suggest the team state that WInS mirrors the post-2028 steady state, roughly 65/35.
- **Trading Note candidate:** the lock-in purchase itself. Log the yield on the trade date against this memo's 5.17% 10y.

## 5) Biggest weaknesses of my proposal
- I could not open primary sources: treasury.gov, FRED and the Fed's H.15 were blocked by this session's network proxy. All yields come from search-result summaries, and TIPS figures conflict between them (2.653% at auction vs. 2.85%). **Verify on treasury.gov before relying on any number.**
- The purchase happens on 1/1/2027, not today. I used today's spot curve, not forwards, and moved only in parallel shifts, with no twists.
- Equity returns are lognormal and independent year to year, with no volatility regimes. The 16% volatility is an assumption.
- STRIPS bid-ask spreads and fund tracking error are ignored.
- (c) locks in today's high rates. It gives up about $21k of median facility versus (a) and about half of (a)'s 95th-percentile upside. An ambitious "creative risk-taker" client may prefer (b).
- USD/TWD risk for the facility is not modelled (spot ~31.73, 9/26/2026). The payments are fixed in USD.
- (b)'s 125% trigger is arbitrary. In practice (b) converges to (c).

## 6) Sources
- 2y/10y/30y close 9/25/2026: https://www.advisorperspectives.com/dshort/updates/2026/09/25/treasury-yields-snapshot-september-25-2026 (via search summary)
- 5y/7y/20y as of 9/23/2026: https://primerates.com/primerate/treasury-yield-curve/ and https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026 (search summary; page blocked)
- 10y TIPS 2.653% at the 9/17/2026 reopening, 2.28–2.30% breakeven: https://tipswatch.com/2026/09/17/10-year-tips-reopening-gets-real-yield-of-2-653-highest-in-nearly-18-years/ (conflicting 2.85% in the same summary; not used in the model)
- JPM 2026 LTCMA, US large cap 6.7%, global equity 7.0%, EM 7.8%: https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/tmt/30-years-of-foresight-the-2026-ltcmas-in-focus (published late 2025)
- Vanguard US equity 4.2–6.2%: https://www.morningstar.com/markets/experts-forecast-stock-bond-returns-2026-edition (2026 edition)
- USD/TWD 31.7284 as of 9/26/2026: https://pluang.com/en/tools/currency-converter/usd-twd

## Cross-examination

## Quant Risk Modeler: cross-examination of the other three council members

The verification script is `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/quant/xexam/verify.py`. It reads the Actuary's own `zc.npy`, re-implements the CIO's discounting, and re-implements the Client Strategist's rule.

### 1. Liability Actuary

**What I concede.** The DV01 and tail-tiering framing is the clearest argument the council has against the team's rolling plan (keeping the 2037–2042 payments in short bonds instead of locking them). Payments in 2037–42 are worth $154k, and a 100bp fall in rates costs about $20k. The ratchet rule is sound: hedge ratio = min(1, assets ÷ Treasury-priced liability), only moving up. It is the principled general form of my strategy (c), and at today's yields it gives the same answer.

**Recomputed:**
- PV today is $289,724. Confirmed.
- Modified duration is 10.04 and DV01 is $291. Confirmed.
- The implied 2033 reserve cost is $395,933. Confirmed.
- The flat-rate annuity-due costs at 5/4/3/2% are 405/422/439/458k. Confirmed.

**Most serious flaw: a code bug that "confirms" the team's $297k.** In `curve.py`, `df()` interpolates log discount factors on a grid that starts at 0.5 years and has no DF(0)=1 anchor. So `np.interp` treats every date before 0.5y as if it were 0.5y away. The 0.26-year roll from 9/28/2026 to 1/1/2027 is therefore discounted at an implied **9.57%** annual rate.

| | Actuary's code | Fixed (DF(0)=1 added) |
|---|---|---|
| Forward PV at 1/1/2027 | $296,692 | **$293,328** |
| Forward PV at 1/1/2028 | $307,597 | $307,597 (unaffected) |
| Growth from 2027 to 2028 | 3.7% | 4.86%, which is consistent with the curve |

The fixed $293.3k agrees with my $294k and the Client Strategist's $294k. **The "$297k confirmed" is an artefact of the bug.**

**Second flaw: the model has a built-in rate forecast.** The Vasicek model uses a long-run mean θ=4.0% and speed κ=0.15. That makes the expected 2033 rate 4.45%. At that rate the reserve costs $414k, against the $396k forward price. So the "wait" strategy is charged about $18k before any randomness. This is a large part of why the Actuary's wait-strategy shortfall is 7.4–9.3%, while mine is 3.3% (no drift). The CIO's figure is 4.4%, from an N(4.5%, 1%) draw with a mild downward drift.

Two further points:
- The Solvency II 99.5% standard is cited from memory. It is a fine analogy but needs a fetched source or should be labelled as such.
- The TIPS figures 2.85% and 2.653% are both quoted. Neither has been verified.

### 2. Endowment CIO

**What I concede.** The sleeve table is the most useful evidence anyone has produced on risk budgeting. Moving the growth sleeve from 40% to 100% equity adds only $4–10k to the median while costing $26–29k at the 5th percentile. My test of 100% equity inside (c) found the same thing: +$2k to the median. The contingency rule is also practical: if the lock costs more than $300k, fill the gap from the 2028 deposit before anything goes to growth.

**Recomputed:**
- $297,745 is reproduced exactly.
- $327,931 at −100bp is reproduced exactly.
- **But the method uses par yields as zero yields.** On an upward-sloping curve that understates the discount rates. The result is about $4k too high compared with the bootstrapped $293–294k.

**Most serious flaw: a timing gap in the contingency rule.** The rule says to fund any excess over $300k from the 2028 deposit. That money does not exist on 1/1/2027. If rates fall 100bp before January, the team can lock only about 91% of the ladder, and the last maturities stay unhedged for a year. That residual risk has to be stated. The fix is to buy the ladder from the nearest maturity outward, so the unhedged maturities are 2041–42. Those are also the ones with the most time to be topped up.

**Inconsistent sourcing across the council.** Three members cite three different Vanguard US-equity ranges:

| Member | Vanguard US-equity range cited |
|---|---|
| Me | 4.2–6.2% |
| CIO | 3.5–5.5% |
| Client Strategist | 3.9–5.9% |

A judge will notice this. The team needs one fetched primary source with a date.

### 3. Client & Credibility Strategist

**What I concede.** "Floor that is already paid for, plus a stretch amount with a stated probability" is the strongest answer to the co-sponsor criterion. I also verified the List & Lucking-Reiley context (small household gifts, not institutional donors). Treating that study as evidence of a mechanism, not a prediction, is the right way to use it. Taiwan inflation and the TWD forward are the only real client-currency work in the council.

**Recomputed (all confirmed):**
- At V31 = $450/550/650k, the floor F comes to 47.2/102.2/157.1k.
- The medians are 70.6/152.6/234.7k.
- U is 78.4/169.6/260.8k.
- P(two-year loss) = 35.9%, the 5th-percentile growth factor is 0.748 and the 90th is 1.450.
- These match only if 5.5% is read as the **arithmetic** mean. That needs to be stated.

**Most serious flaw: calling early locking "optional".** That reopens the contradiction the other three reports closed. Their own stress test shows L31 rises about $34k if rates fall 150bp. Every dollar of that comes straight out of S, and S is the thing Laura promises in 2031.

**Second flaw: the floor gives up too much certainty.** With a = 50%, the guaranteed floor is only 0.55×S. My de-risked sleeve reaches 0.96×S at 95% confidence. Moving all of S into a 2-year Treasury guarantees 1.10×S. The rule is sound, but a = 50% has not been tuned. The team should show Laura a menu: the floor as a share of S, with the confidence for each.

### 4. What changes in my recommendation

1. **The core does not change.** All four members independently reach "lock the full ladder with the 2027 deposit, grow the surplus". On the corrected curve, the lock costs **$293–294k**. This now needs repricing against the Treasury page on the purchase day.
2. **I adopt the Actuary's ratchet rule as the policy statement.** Strategy (c) becomes its current-yield special case. This keeps a stated policy, not a rate forecast.
3. **I adopt the CIO's growth-sleeve weight of about 70% equity, not 100%,** stepping down in 2031–32.
4. **I adopt the Client Strategist's floor-plus-stretch structure, with a calibrated menu instead of a = 50%.** Options for the floor, for the team to choose from:
   - (i) Fully locked: 1.10×S2031 in a 2-year Treasury, confidence 100%. Stretch comes only from anything left above that.
   - (ii) Partly locked: lock 0.6×S and state the range as [0.66, ~1.2]×S.
   - (iii) My earlier 0.96×S floor at 95% confidence. This is **model-dependent** and should be labelled that way.
5. **New finding on model risk.** The wait strategy's P(shortfall) runs from 3.3% to 9.3% across the four council models, entirely because of rate-drift assumptions. That spread is the strongest statistical argument for locking. Under strategy (c), the payments do not depend on any model's view of rates.
6. **Housekeeping before any number goes into the IPS:**
   - Pick one Vanguard source.
   - Resolve the TIPS figure (2.653% vs 2.85%).
   - Anchor DF(0)=1 in any reused curve code.
   - Treat every yield as unverified until checked on treasury.gov. All four members were blocked from primary sources.

The WInS rules (approved securities list, sector minimum, trade limits, starting capital) are still unknown to all four members. So is the "6 sectors" claim.

---

