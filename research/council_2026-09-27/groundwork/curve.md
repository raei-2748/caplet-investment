## Treasury curve and the PV of Laura's 2033-2042 payments (as of 2026-09-27), fact-checked version

**I could not get the official Treasury curve.** The egress proxy blocked every direct fetch. The original report listed home.treasury.gov, federalreserve.gov, fred.stlouisfed.org, advisorperspectives.com, cnbc.com, tradingeconomics.com, forbes.com, public.com, ustreasuryyieldcurve.com and slickcharts.com. I confirmed the blocks on home.treasury.gov and fred.stlouisfed.org (curl returned CONNECT 403) and on cnbc.com, and found three more blocked sites: seekingalpha.com and stockmarketwatch.com (WebFetch refused both), plus econforecasting.com. Only WebSearch worked, so every yield below comes from a search-engine summary, not from a page anyone read. **Treat them all as secondary.** Before any figure goes into the submission, a team member must download the official Treasury par-yield CSV for 2026-09-25 by hand.

### 1. Curve data

**Curve A (preferred): close of Fri 2026-09-25**

| Tenor | Yield | Status after re-check |
|---|---|---|
| 2Y | 4.81% | Confirmed again by an independent search (2026-09-27) |
| 5Y | 4.98% | **UNVERIFIED.** My re-search found no value. One result said only that the 5Y was "higher than its 12-month average of 4.00%". |
| 10Y | 5.17% | Confirmed again: "finished at 5.17%… up less than 1bp to 5.163% after reaching its highest since June 2007 on Thursday [Sep 24]" |
| 30Y | 5.49% | Confirmed again: 5.49% at 3:30pm ET per a Forbes-linked summary. Trading Economics gives 5.50% (+2bp). |

- **Correction to the 10Y.** The original said the 10Y was "down 4bp on the day". A re-search contradicts that: it was up less than 1bp, and CNBC's headline calls it "little changed". The 2007 high was set on Thursday 2026-09-24, not on Sep 25.
- **Estimated tenors.** The 1Y (4.49), 7Y (5.11) and 20Y (5.51) come from a PrimeRates summary for 2026-09-23. The 7Y and 20Y then had +6bp added. **These are estimates, not observations, and I did not re-verify the PrimeRates source.**
- **Correction to the Fed status.** The report marked the Fed hike to 3.75-4.00% on 2026-09-16 as UNVERIFIED. It is now verified in search results: CNBC, "Fed rate decision September 2026: Rates rise to 3.75%-4%", and a Federal Reserve press release at monetary20260916a.htm. The same results say the vote was 12-0, the first hike since 2023, and the projections signal one more hike in 2026.

**Curve B (conflicting): UNVERIFIED, likely stale.** The values are 1M 3.73, 3M 3.74, 6M 3.79, 1Y 3.80, 2Y 3.88, 3Y 3.90, 5Y 4.01, 7Y 4.20, 10Y 4.39, 20Y 4.97, 30Y 4.96.
- When I repeated the search, the summary described these as "the most recent… September 25, 2026".
- They still disagree with Curve A by about 78bp at 10 years. At least three independent summaries give a 10Y of about 5.17%.
- Several signs point to stale data:
  - The 5Y (4.01) is almost exactly the "12-month average of 4.00%" quoted elsewhere.
  - The 1M bill (3.73) sits below the new 3.75-4.00% fed funds range.
  - The 20Y is above the 30Y.
- This is my inference, not a verified fact. I keep Curve B only as a sensitivity case.

**STRIPS and zero-coupon yields for 2033-2042: UNVERIFIED.** The zero rates below are bootstrapped from par yields, not quoted.

### 2. Method (checked, unchanged)
Script: `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/groundwork/curve_pv.py`
- **Valuation date:** 2026-09-25, with year fractions of actual days / 365.25.
- **Curve build:** par yields are treated as semiannual bond-equivalent yields and linearly interpolated onto a 0.5-year grid, then bootstrapped as DF_n = (1 − c·ΣDF)/(1+c). Discount factors between grid points use log-linear interpolation.
- **Value at the funding date:** PV at 2027-01-01 = Σ 50,000·DF(Jan 1 of 2033…2042)/DF(2027-01-01). This matches the client profile, which says withdrawals occur at the beginning of each year. It is the forward value that today's curve locks in, not a forecast.
- **Rate risk:** DV01 is the central difference of ±1bp parallel shifts.
- **Not modelled:** taxes, Taiwan residency effects, convexity beyond the curve, and FX.
- **Caveat on the 20Y input:** the script uses 5.51% for the 20Y, slightly above the 5.49% 30Y. That mild 20s/30s hump is inherited from the estimate.

### 3. Results (all recomputed; every figure reproduced exactly)

| | Curve A (Sep 25, 10Y 5.17%) | Curve B (unverified, 10Y 4.39%) |
|---|---|---|
| **PV at 2027-01-01** | **$292,323** | $314,465 |
| −100bp | $322,931 (+30,608) | $347,895 (+33,430) |
| −50bp | $307,198 (+14,876) | $330,707 (+16,241) |
| +50bp | $278,253 (−14,069) | $299,114 (−15,351) |
| +100bp | $264,942 (−27,381) | $284,599 (−29,866) |
| DV01 | $289 per bp | $316 per bp |
| Effective duration | 9.90 years | 10.04 years |
| Implied semiannual zero, 2033 / 2037 / 2042 | 5.11 / 5.24 / 5.46% | 4.17 / 4.48 / 4.85% |

### 4. Comparison with the council's ~$295k
- **Curve A gap:** the Curve A PV of $292.3k is $2,677 (0.91%) below $295k. At a DV01 of $289, that equals about 9bp of parallel rate move.
- **The $295k benchmark:** $295k corresponds to a flat **5.26% annual** discount rate (recomputed). That rate is consistent with the Curve A zeros.
- **Curve B gap:** if Curve B were correct, the PV would be about $314k, which is $19k more.
- **Implications for the plan (these depend on the unconfirmed curve):**
  - A matched Treasury or STRIPS ladder would cost about $292k of the $300k deposit, leaving about $7.7k plus the $150k deposit in 2028 for growth assets.
  - A 100bp rally before funding in January 2027 would add about $30.6k to the cost.
  - The rate hike of 2026-09-16 and the signal of another hike point to upward rate pressure. That is context only, not a forecast.

### Verification notes
- **Re-searched independently (2026-09-27):**
  - 10Y on Sep 25: confirmed 5.17%. The "down 4bp" claim was corrected to "up <1bp", and the 2007-high date was corrected to Sep 24.
  - 2Y 4.81%: confirmed.
  - 30Y 5.49%: confirmed, with Trading Economics at 5.50%.
  - 5Y 4.98%: not found, so it is now marked UNVERIFIED.
  - Fed hike to 3.75-4.00% on 2026-09-16: upgraded to verified in search results.
  - Curve B: the source now claims a Sep 25 date, but it still conflicts with the other summaries and remains UNVERIFIED.
- **Fetch attempts, all blocked:** Treasury CSV and FRED CSV by curl, plus CNBC, Seeking Alpha and StockMarketWatch by WebFetch.
- **Arithmetic:** reran curve_pv.py in the venv. All PVs, shifts, DV01, durations, zeros and the 5.26% flat rate reproduced exactly. Checked the $2,677 / 0.91% / 9bp gap and the leftover $7,677. The script's inputs match the stated estimates (7Y 5.05+0.06, 20Y 5.45+0.06).
- **Still UNVERIFIED:** the PrimeRates Sep 23 tenors, the 5Y, Curve B, and all STRIPS yields.

### Sources
All retrieved 2026-09-27 as WebSearch results or summaries. Direct fetches were blocked.
- Advisor Perspectives, Treasury Yields Snapshot Sep 25, 2026: https://www.advisorperspectives.com/dshort/updates/2026/09/25/treasury-yields-snapshot-september-25-2026
- Seeking Alpha, same snapshot (blocked): https://seekingalpha.com/article/4949891-treasury-yields-snapshot-september-25-2026
- CNBC, "10-year Treasury yield is little changed to end a volatile week" (2026-09-25): https://www.cnbc.com/2026/09/25/treasury-yields-bonds-debt.html
- Trading Economics 10Y / 30Y (2026-09-25): https://tradingeconomics.com/united-states/government-bond-yield ; https://tradingeconomics.com/united-states/30-year-bond-yield
- Forbes, "Treasury Rates Today: September 25, 2026": https://www.forbes.com/advisor/investing/treasury-rates/
- Federal Reserve H.15 (title Sep 25, 2026; blocked): https://www.federalreserve.gov/releases/h15/
- CNBC, Fed decision (2026-09-16): https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html
- Federal Reserve FOMC statement (2026-09-16): https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
- PrimeRates (data 2026-09-23; not re-verified): https://primerates.com/primerate/treasury-yield-curve/
- Treasury Daily Par Yield Curve (Curve B summary; blocked): https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026
- TreasuryDirect STRIPS (background only): https://www.treasurydirect.gov/marketable-securities/strips/