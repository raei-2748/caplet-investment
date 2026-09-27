# Fact register (A2, Phase A): the run's single source of truth for numbers

AI-generated research (Claude Code, 2026-09-27) for Team Caplet. Not submission text: it is a list of checked numbers
with their sources. The team decides what to use and writes every deliverable in its own words.

## Summary (read this first)

1. **Both verified scripts reproduce exactly.** I re-ran them on 2026-09-27 and got the same results: $292,264; lock-early 2033 surplus
   p5/p50/p95 $159k/$207k/$273k; growth-first miss 3.2%. Every number in brief section 6 matches (F-101 to F-106, F-401 to F-408).
2. **NEW, high impact: this season's WInS rules are partly public.** The 2026-27 SMApply FAQs page can be opened
   without logging in. It says the team manages **$300,000 of virtual cash**, the same as Laura's 2027 deposit. It also
   lists the permitted investments: cash, stocks priced at $5 or more, "any ETFs available on WInS" and "any
   Government/Treasury Bonds ... available on WInS". Margin, shorting, crypto and derivatives are banned. Commissions
   are $25 per stock trade and $10 per bond trade (F-605 to F-608). This replaces "starting cash unknown" in the brief. The
   logged-in "Trading Details" page may add more rules, so check it and the WInS account itself before trading.
3. **"The ladder fits inside $300k" is a September 2026 fact, not a normal one.** I priced the same ten payments on
   every 2026 Treasury curve. The ladder cost more than $300k on 173 of 185 trading days: $316.5k on Jan 2 and
   $325.6k at the February low in rates. It fell below $300k only in September (F-111). Using an ASSUMPTION of a
   zero-drift random walk at 2026 volatility, the chance it costs more than $300k on 2027-01-01 is about 24% (F-112).
   That is within the council's 23-32%.
4. **Most brief section 6 "UNVERIFIED" items are now confirmed on primary sources:**
   - The FOMC raised rates 25bp to 3.75-4.00%, 12-0, on 2026-09-16. It was the first rise since July 2023 (F-005).
   - Taiwan CPI for August 2026 was +2.04% (DGBAS). The 2.4% figure is wrong (F-501).
   - The central bank of Taiwan held its discount rate at 2% on 2026-09-17 (F-506).
   - The latest USD/TWD on FRED is 31.82 (2026-09-18). Volatility over the last 10 years is 4.69% (F-510, F-512).
   - The current IEF/TLT durations are 6.86/14.88 years, which gives a duration match of 62.2/37.8 (F-203 to F-205).
   - iShares Treasury iBonds exist for Dec 2026-2036 but not for Dec 2037-2043 (F-206).
5. **Taiwan construction costs.** From the official DGBAS platform I derived +6.53% y/y (the snippet says 6.54%). That jump happened
   in 2026 alone: the index barely moved in 2024-25 and has averaged ~3.5% a year since 2021 (F-508). So the
   one-month "3.2x CPI" multiple should not be used as a trend (S-34).
6. **I resolved all 10 cross-file inconsistencies in brief section 10 and superseded 38 older numbers** (section H).
   The largest corrections are:
   - "Curve B" was the official curve of 2026-03-20, not a mystery. It was six months stale.
   - The coupon-reinvestment "dispute" was two correct sums for two different ladders.
   - The "65/35" WInS mirror is ladder/sleeve, not bonds/equity. Total equity after 2028 is about 17-24% (F-409).

## How to read this file

- **ID scheme:** F-0xx rates; F-1xx liability valuation; F-2xx instruments; F-3xx capital-market assumptions;
  F-4xx simulation outputs; F-5xx Taiwan/FX/inflation; F-6xx competition facts; S-xx superseded numbers.
- **Status labels** follow brief section 3. **Derived numbers** are arithmetic by an A2 script on labelled inputs. They
  carry the weakest input's label plus "(derived, script)". "ASSUMPTION method" means the arithmetic depends on a
  modelling choice, for example how the curve is bootstrapped.
- **Feeds** lists the later numbers that change if this one changes.
- **Access date** for every web source is 2026-09-27 (between 11:38 and 12:15 UTC), from this run's container.
- **Trading rule:** any item that mentions an instrument carries "PENDING APPROVAL CHECK: confirm on this year's WInS
  approved list/rules before trading" (brief section 4, updated 2026-09-27). This register records facts about
  instruments; it does not pick securities.
- **Note for the brief:** brief section 4 still says this year's starting cash and WInS rules are "UNKNOWN". F-605 to
  F-608 show that the public SMApply FAQs page already states the cash amount and the permitted-investment
  categories. The logged-in details are still unknown.

**Plain-English terms used below**
- **Par yield:** the coupon rate at which a new Treasury would sell for exactly its face value.
- **Basis point (bp):** 0.01%.
- **Discount factor / bootstrap:** turning par yields into the value today of $1 paid on a future date.
- **Forward value:** what today's curve locks in for a later date.
- **DV01:** dollars gained or lost for a 1bp parallel rate move.
- **Duration:** the % price change for a 1% rate move.
- **Effective duration:** the fund manager's duration measure.
- **Yield to maturity (YTM):** the fund's average yield if its bonds are held to maturity.
- **30-day SEC yield:** a standardised recent income yield, after fees.
- **Compound (geometric) return:** the growth rate actually achieved over many years.
- **Arithmetic return:** the simple average of yearly returns. It is higher than the compound return when returns jump around.
- **Volatility:** the standard deviation of returns, per year.
- **Correlation:** how closely two assets move together, from -1 to +1.
- **Breakeven inflation:** nominal yield minus TIPS real yield, i.e. the inflation the market is "pricing".

## Step 1: reproduction check (2026-09-27, `.venv/bin/python`, repo root)

| Script | Brief section 6 value | Re-run output | Match |
|---|---|---|---|
| `research/verified_2026-09-27/official_curve_pv.py` | $292,264; -25bp $299,596; -50bp $307,135; -100bp $322,864; +50bp $278,198; +100bp $264,890; DV01 $289/bp; duration 9.90y; headroom $7,736 = 27bp; forward zeros 5.08/5.24/5.48%; 64.8/35.2 | identical, digit for digit | Yes |
| `research/verified_2026-09-27/strategy_mc.py` (200k paths, seed 20260927) | L never misses; surplus p5/p50/p95 $159k/$207k/$273k; floor $127k/$165k/$217k; G 3.2% (13.7% at $75k, 40.8% at $0); G surplus $20k/$226k/$540k; sleeve equity 50/60/70% median $205k/$207k/$209k, p5 $164k/$159k/$154k; equities 5.0%: L median $200k, G miss 5.5% | identical | Yes |
| "Same payments valued at 2033-01-01 on forwards: ~$394.9k" (not printed by either script) | ~$394.9k | $394,930 (`A2_curve_recheck.py`) | Yes |

New scripts written by A2 (all in `research/insight_v1/scripts/`, each with a docstring listing inputs, labels and the run command):
- `A2_curve_recheck.py`: curve and ladder numbers, 2026 history, IEF/TLT weights, council arithmetic checks.
- `A2_jpm_extract.py`: JPM LTCMA rows and correlations, read from the PDF.
- `A2_twd_vol.py`: USD/TWD level and volatility, live from FRED.
- `A2_taiwan_cci.py`: the Taiwan construction cost index, rebuilt from the DGBAS platform.

---

## A. Rates and Treasuries

| ID | Fact | Value | Unit | As of | Source | Status | Feeds | Notes |
|---|---|---|---|---|---|---|---|---|
| F-001 | U.S. Treasury par yield curve | 1M 4.04, 1.5M 4.14, 2M 4.20, 3M 4.24, 4M 4.32, 6M 4.33, 1Y 4.50, 2Y 4.81, 3Y 4.94, 5Y 4.98, 7Y 5.06, 10Y 5.17, 20Y 5.54, 30Y 5.49 | % (semiannual bond-equivalent) | 2026-09-25 | `competition/official_market_data/daily-treasury-rates_2026-09.csv` row 09/25/2026; the live CSV at https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv has identical September rows | VERIFIED-REPO-FILE and VERIFIED-PRIMARY | F-011-F-014, all of B, F-205, F-401-F-409 | The verified script ignores the 1.5M and 4M columns (no effect). |
| F-002 | Is there a newer curve? | No. The latest date is 2026-09-25 (9/26-27 is a weekend) | - | checked 2026-09-27 11:40 UTC | same live CSV | VERIFIED-PRIMARY | - | Re-price on purchase day (January 2027). |
| F-003 | Path of yields in 2026 | 10Y: 4.19 (Jan 2), low 3.97 (Feb 27), 4.44 (Jun 30), 4.79 (Sep 1), high 5.18 (Sep 24), 5.17 (Sep 25). 2Y: 3.47 (Jan 2) to 4.81. 30Y: 4.86 to 5.49 | % | 2026-01-02 to 09-25 | live 2026 CSV (F-001) | VERIFIED-PRIMARY | F-111, F-112 | The 10Y rose 38bp in September (4.79 to 5.17) and about 120bp from the February low. |
| F-004 | How high is the 10Y historically? | 5.18% on 2026-09-24 is the highest daily close since 2007-07-06 (5.19%); the 2008-2025 maximum was 4.98% (2023-10-19) | % | 2026-09-24 | FRED DGS10 (H.15), https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10 | VERIFIED-PRIMARY | landscape | Snippets said "since June 2007"; the last higher close was 6 July 2007. A team note's "highest since late 2023" is wrong (S-13). |
| F-005 | FOMC decision | Raised 1/4 point to "3-3/4 to 4 percent"; vote "12 – 0"; effective 2026-09-17 | % | 2026-09-16 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm | VERIFIED-PRIMARY | F-515 | First increase since 2023-07-27 (to 5.25-5.50). The range was 3.50-3.75 from 2025-12-11 until this move (https://www.federalreserve.gov/monetarypolicy/openmarket.htm). |
| F-006 | Implementation rates | Interest on reserve balances 3.90%; overnight reverse repo 3.75%; standing repo 4.0%; primary credit 4.0% | % | effective 2026-09-17 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a1.htm | VERIFIED-PRIMARY | F-515 | - |
| F-007 | Fed projections (Summary of Economic Projections), medians | Fed funds end-2026 4.1, 2027 4.1, 2028 3.9, 2029 3.6, longer run 3.2 (2026 central tendency 4.1-4.4); PCE inflation 2026 3.7, 2027 2.3, 2028 2.1, longer run 2.0; core PCE 2026 3.4; GDP 2026 2.3; unemployment 2026 4.1 | % | 2026-09-16 | https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm | VERIFIED-PRIMARY | F-114 | The 2026 median of 4.1 is the midpoint of 4.00-4.25, i.e. one more 25bp hike. These are projections, not promises. |
| F-008 | TIPS real par yields | 5Y 2.64, 7Y 2.73, 10Y 2.83, 20Y 3.08, 30Y 3.22 (10Y 2.85 on 9/24; 2.61 on 9/17) | % | 2026-09-25 | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026&page&_format=csv | VERIFIED-PRIMARY | F-009 | Resolves the council's 2.85% vs 2.653% conflict (S-22). |
| F-009 | Breakeven inflation (nominal minus real) | 5Y 2.34, 7Y 2.33, 10Y 2.34, 20Y 2.46, 30Y 2.27 | % | 2026-09-25 | F-001 minus F-008 | VERIFIED-PRIMARY (derived) | F-114 | The 7Y (≈ to 2033) is 2.33%. This is market pricing, including risk premia; it is not a forecast. |
| F-010 | 10Y on the JPM LTCMA data date | 4.16% | % | 2025-09-30 | FRED DGS10 | VERIFIED-PRIMARY | F-317 | Yields are about 100bp higher now than when JPM set its bond assumptions. |
| F-011 | Spot zero rates for payment dates, from 9/25 | Jan-2027 4.33%; Jan-2033 5.05%; Jan-2037 5.22%; Jan-2042 5.46% (annual compounding: 4.38/5.11/5.29/5.54) | % semiannual | 2026-09-25 | `A2_curve_recheck.py` method on F-001 | VERIFIED-REPO-FILE inputs + ASSUMPTION method | S-10 | Replaces the chair memo's 5.04-5.38%. |
| F-012 | Forward zero rates from 2027-01-01 | to 2033 5.08%; to 2037 5.24%; to 2042 5.48% | % semiannual | 2026-09-25 | `official_curve_pv.py` | VERIFIED-REPO-FILE inputs + ASSUMPTION method | strategy_mc (5.08% forward factor) | Reproduced. |
| F-013 | 2-year growth factor for the 2031 floor at today's 2Y | 1.0985 (annual convention, used by strategy_mc) vs 1.0997 (semiannual bond-equivalent, Treasury's convention) | x | 2026-09-25 | `A2_curve_recheck.py` | ASSUMPTION (2031 2Y = today's 4.81%) | F-402 | The 0.12% difference is trivial ($166.1k vs $166.3k at S=$189k, a=0.8). Say which convention is used. |
| F-014 | Realised volatility in 2026 | 10Y yield: 71bp a year; ladder cost (value at 2027-01-01): 7.24% a year | bp / % | 2026-01-02 to 09-25 | `A2_curve_recheck.py` on live 2026 CSV | VERIFIED-PRIMARY inputs (derived) | F-112 | Council assumed 36-57bp over 0.27y, which is 69-110bp a year. |

## B. Liability valuation (the ten $50,000 payments, 1 Jan 2033-2042)

| ID | Fact | Value | Unit | As of | Source | Status | Feeds | Notes |
|---|---|---|---|---|---|---|---|---|
| F-101 | Cost at 2027-01-01 (value locked by today's curve) | **$292,264** | USD | curve 2026-09-25 | `official_curve_pv.py`; `A2_curve_recheck.py` [1] | VERIFIED-REPO-FILE inputs + ASSUMPTION method | F-104, F-117, F-401-F-409 | Reproduced. The single number to use (brief section 8.4). |
| F-102 | Parallel-shift costs | -100bp $322,864; -50bp $307,135; -25bp $299,596; +25bp $285,133; +50bp $278,198; +100bp $264,890 | USD | 2026-09-25 | same | same | rule-if-rates-fall analysis | - |
| F-103 | DV01 / duration of the 2027 value | $289/bp (289.2); 9.90 years | USD/bp; years | 2026-09-25 | same | same | F-205 | - |
| F-104 | Headroom under the $300k deposit | $7,736 = 27bp (26.7) | USD; bp | 2026-09-25 | same | same | F-112 | - |
| F-105 | Value today (spot) and its duration | $288,924; 10.16 years | USD; years | 2026-09-25 | `A2_curve_recheck.py` [1] | same | F-205 | For hedging today (WInS), the spot duration (10.16y) is the right target. The 9.90y figure is the duration of the January-2027 value. |
| F-106 | Forward value of the remaining payments | at 2028-01-01 $306,077; at 2031-01-01 $356,384; at **2033-01-01 $394,930** | USD | 2026-09-25 | `A2_curve_recheck.py` [2] | same | F-409; "which number is the reserve" | Replaces the council's $357-358k / $395.8k-$397k (S-09). |
| F-107 | Cost of each rung at 2027-01-01 | 2033 $37,002; 2034 $35,095; 2035 $33,262; 2036 $31,497; 2037 $29,792; 2038 $28,154; 2039 $26,579; 2040 $25,065; 2041 $23,607; 2042 $22,210. 2033-36 total $136,856; 2037-42 total $155,408 | USD | 2026-09-25 | same | same | long-rungs-first rule | The council said 2037-42 was "about $154k" (S-09 family). |
| F-108 | Extra cost of the 2037-42 rungs if rates fall before they are bought | -100bp +$20,221; -200bp +$43,232 | USD | 2026-09-25 | same | same | tiering rejection (brief section 8.2) | Reproduces the council's $20k/$43k. |
| F-109 | Flat-rate equivalents | A flat 5.359% a year reproduces $292,264; a flat 5.26% gives $295,054 (the old "$295k") | %; USD | 2026-09-25 | `A2_curve_recheck.py` [3] | ASSUMPTION (flat curve) | F-110 | 5.26% is not the verified curve's equivalent; 5.36% is. |
| F-110 | Reserve needed on 2033-01-01 if bought then (annuity-due, flat rate) | 7% $375,762; 5.36% $399,778; 5.26% $401,312; 5% $405,391; 4.5% $413,440; 4% $421,767; 3% $439,305 | USD | - | same | ASSUMPTION (rates are illustrations) | growth-first comparison | strategy_mc prices G's 2033 reserve at 5.26% ± 1pp. That is about $6.4k above the forward value (F-106), so it slightly overstates G's shortfall (brief section 11). |
| F-111 | **The same ladder priced on every 2026 curve date** | Jan 2 $316,546; max $325,563 (Feb 27, 10Y 3.97%); Jun 30 $312,974; Sep 1 $302,391; min $292,051 (Sep 24). **Above $300k on 173 of 185 trading days**; at or below $300k only on the 12 days since 2026-09-10 | USD | 2026-01-02 to 09-25 | `A2_curve_recheck.py` [6] on live 2026 CSV | VERIFIED-PRIMARY inputs + ASSUMPTION method | rule-if-rates-fall | "Fits inside $300k" rests on the September 2026 sell-off. |
| F-112 | Chance the ladder costs more than $300k on 2027-01-01 | ~24%; a one-standard-deviation move by then is about ±$11.0k | % | 2026-09-25 | `A2_curve_recheck.py` [6] | ASSUMPTION (zero-drift lognormal at 2026 realised volatility of 7.24%/yr over 0.27y) | rule-if-rates-fall | A model number, not a forecast. The council gave 23-32% (38% at $295k). |
| F-113 | Coupon-reinvestment arithmetic (if coupon Treasuries are used instead of zero-coupon bonds) | Budget ladder (face = cost $295,054): coupons $15,520/yr in 2028-32; reinvesting 200bp lower loses $5,211 by 2033. A fully matched-from-2033 coupon ladder needs $381,258 of face, which pays $20,054/yr; the loss is $6,734 | USD | - | `A2_curve_recheck.py` [4] | ASSUMPTION (flat 5.26% annual coupons, reinvested at 3.26%) | brief section 8.11 (zero-coupon preferred) | Both council sums are correct. The budget-ladder one ($15.5k/$5.2k) is the one that fits Laura's $300k (S-16). |
| F-114 | What a fixed $50k is worth in today's (2026) money | 2.0% inflation: 2033 $43,528, 2042 $36,422. 2.5% (JPM): $42,063 / $33,681. 3.7% (Fed's 2026 PCE median, used only as a stress): $38,772 / $27,958 | USD (2026 dollars) | - | `A2_curve_recheck.py` [7] | ASSUMPTION (inflation rates) | real-erosion question (brief section 9) | U.S. dollars only; Taiwan costs are in F-5xx. |
| F-115 | Discounting example | $50k due in 6 years at 5.26% = $36,761 | USD | - | same [3] | ASSUMPTION (flat rate) | teaching examples | The referee's "$36.9k" should read $36.8k (S-17). |
| F-116 | Team note's "$626k by 2033" | implies a flat 5.99% a year | % | - | same [3] | ASSUMPTION check | - | Reproduces the council. |
| F-117 | Funded ratio (assets ÷ Treasury price of the promise) | $300,000 / $292,264 = 1.026 | ratio | 2026-09-25 | F-101 | VERIFIED-REPO-FILE inputs + ASSUMPTION method | certainty definition | Any fall in rates before purchase lowers it (F-111). |

## C. Instruments (verified data only; PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading)

| ID | Fact | Value | Unit | As of | Source | Status | Feeds | Notes |
|---|---|---|---|---|---|---|---|---|
| F-201 | IEF fact sheet (7-10 year Treasury fund) | Effective duration 6.95 yrs; expense ratio 0.15%; 30-day SEC yield 4.29%; weighted average maturity 8.45 yrs; convexity 0.58; 13 holdings; 3y standard deviation 6.54%; equity beta 0.23; net assets $47,093.37M; 1y NAV return 2.61%; 2022 return -15.23%. **No yield to maturity is printed** | various | 2026-06-30 | `competition/official_market_data/IEF_fact_sheet_2026-06-30.pdf` p.1 (pypdf) | VERIFIED-REPO-FILE | F-205 | - |
| F-202 | TLT fact sheet (20+ year Treasury fund) | Effective duration 15.31 yrs; expense ratio 0.15%; SEC yield 4.89%; weighted average maturity 26.03 yrs; convexity 3.27; 46 holdings; 3y standard deviation 13.74%; beta 0.58; net assets $41,099.93M; 2022 return -31.41%. No yield to maturity printed | various | 2026-06-30 | `.../TLT_fact_sheet_2026-06-30.pdf` p.1 | VERIFIED-REPO-FILE | F-205 | - |
| F-203 | IEF today | Effective duration **6.86 yrs**; YTM 5.17%; SEC yield 4.84%; 12m trailing yield 4.13%; weighted average maturity 8.44; convexity 0.57; weighted average coupon 4.24; YTD NAV total return -4.20% (all as of Sep 24). NAV $89.94 on Sep 25 (52-week range 89.68-97.96); net assets $41,570,344,536; expense 0.15% | various | 2026-09-24/25 | https://www.ishares.com/us/products/239456/ishares-710-year-treasury-bond-etf | VERIFIED-PRIMARY | F-205 | Duration fell from 6.95 as yields rose. |
| F-204 | TLT today | Effective duration **14.88 yrs**; YTM 5.54%; SEC yield 5.41%; trailing yield 4.90%; weighted average maturity 26.04; convexity 3.13; weighted average coupon 3.34; YTD -6.15% (as of Sep 24). NAV $79.28 on Sep 25, **at its 52-week low** (range 79.28-92.05); net assets $45,753,218,426; expense 0.15% | various | 2026-09-24/25 | https://www.ishares.com/us/products/239454/ishares-20-year-treasury-bond-etf | VERIFIED-PRIMARY | F-205 | Mark-to-market losses matter for WInS only, not for a held-to-maturity ladder. |
| F-205 | Duration-matching mix (a duration match only, NOT a cash-flow match) | June fact sheets, 9.90y target: **64.8% IEF / 35.2% TLT**. Current durations, 9.90y: **62.2 / 37.8**. Spot 10.16y target: 61.6/38.4 (June) or 58.9/41.1 (current) | % | 2026-09-24 | `A2_curve_recheck.py` [5] | VERIFIED-PRIMARY inputs (derived) | WInS mirror | The mix drifts as durations and time move, so re-check before each hedge trade. PENDING APPROVAL CHECK: confirm both funds on this year's WInS approved list/rules before trading. |
| F-206 | Which defined-maturity Treasury funds exist (iShares "iBonds Dec-20XX Term Treasury" family) | Dec 2026 through Dec 2036; then Dec 2044-2046 and Dec 2054-2056. **None for Dec 2037-2043** | - | 2026-09-27 | iShares product screener JSON (ishares.com, product-screener-v3.1) | VERIFIED-PRIMARY | brief section 8.12 | Dec 2032-2036 funds pay out before the Jan 2033-Jan 2037 payments (5 payments). Jan 2038-2042 (5 payments) have no matching iShares fund. Other issuers were not checked, and availability inside WInS is unknown: PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading. |
| F-207 | Example: the Dec 2034 fund in that family | Expense 0.07%; effective duration 6.44 yrs; YTM 5.15% (Sep 24) | various | 2026-09-24 | https://www.ishares.com/us/products/337745/ishares-ibonds-dec-2034-term-treasury-etf | VERIFIED-PRIMARY | - | Shows the fund type's cost level (the council's 0.07% snippet is now confirmed for this vintage). |
| F-208 | Other instrument claims in `groundwork/instruments.md` (BulletShares Treasury 2027-31 launch; zero-coupon and T-bill fund expense ratios; VGIT/VGLT durations) | as stated there | - | - | council snippets | SNIPPET-UNVERIFIED (not re-checked by A2) | - | Low priority. Re-check on issuer pages before any of these is recommended (brief section 4, rule d). |

## D. Capital-market assumptions (J.P. Morgan 2026 LTCMA, U.S. dollar matrix)

Source for F-301 to F-314: `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf`, page 2 ("Source: J.P.
Morgan Asset Management; data as of September 30, 2025"; "All returns are nominal"). Read with pypdf by
`A2_jpm_extract.py`. Status: **VERIFIED-REPO-FILE**.

The column order (compound 2026, arithmetic 2026, volatility, compound 2025) comes from the header positions. It is
confirmed by the check "arithmetic ≈ compound + vol²/2", which works only in this order. The horizon is "10- to
15-year" (https://am.jpmorgan.com/us/en/asset-management/institutional/insights/portfolio-insights/ltcma/,
VERIFIED-PRIMARY). Laura's growth-sleeve horizon (2027-2033) is shorter than that.

| ID | Asset class | Compound 2026 | Arithmetic 2026 | Volatility | Compound 2025 (prior edition) | Feeds / notes |
|---|---|---|---|---|---|---|
| F-301 | **U.S. Large Cap** | **6.70** | **7.94** | **16.47** | 6.70 | strategy_mc equity input (brief section 8.14: compound) |
| F-302 | AC World Equity | 7.00 | 8.28 | 16.78 | 7.10 | global alternative for the sleeve |
| F-303 | EAFE Equity | 7.50 | 8.90 | 17.63 | 8.10 | - |
| F-304 | Emerging Markets Equity | 7.80 | 9.74 | 20.93 | 7.20 | - |
| F-305 | U.S. Small Cap / U.S. Mid Cap | 6.90 / 7.00 | 8.89 / 8.55 | 21.10 / 18.56 | 6.90 / 7.00 | - |
| F-306 | AC Asia ex-Japan Equity | 7.90 | 9.83 | 20.84 | 7.20 | Closest JPM row to any Taiwan tilt; **JPM has no Taiwan-only row** |
| F-307 | **U.S. Intermediate Treasuries** | **4.00** | **4.06** | **3.48** | 3.80 | strategy_mc bond input |
| F-308 | U.S. Long Treasuries | 4.90 | 5.69 | 13.02 | 4.30 | - |
| F-309 | TIPS | 4.30 | 4.47 | 5.88 | 4.10 | - |
| F-310 | U.S. Aggregate Bonds | 4.80 | 4.91 | 4.76 | 4.60 | - |
| F-311 | U.S. Cash | 3.10 | 3.10 | 0.67 | 3.10 | - |
| F-312 | U.S. Inflation | 2.50 | 2.52 | 1.77 | 2.40 | F-114 |
| F-313 | Others (compound / arithmetic / vol) | Short-duration govt/credit 4.00/4.01/1.63; IG corporate 5.20/5.46/7.39; high yield 6.10/6.46/8.74; world govt hedged 4.30/4.38/4.02; U.S. minimum-volatility factor 7.00/7.79/13.16; U.S. REITs 8.80/10.15/17.40; commodities 4.60/6.15/18.32; gold 5.50/6.78/16.68 | | | | reference only |

| ID | Fact | Value | Status | Notes |
|---|---|---|---|---|
| F-314 | JPM correlations | **U.S. large cap vs intermediate Treasuries -0.01**; vs long Treasuries 0.02; vs cash 0.01; vs inflation -0.01; vs TIPS 0.34; vs aggregate bonds 0.30. AC World vs intermediate 0.00, vs long 0.01. EAFE 0.02/0.02. EM 0.00/0.02. Small cap -0.08/-0.05. Intermediate vs long Treasuries 0.84. Large cap vs AC World 0.97, vs EAFE 0.87, vs EM 0.73. Inflation vs intermediate Treasuries -0.27, vs long -0.22 | VERIFIED-REPO-FILE | Near-zero stock-bond correlation is JPM's long-run view. The council's +0.4 stock-rate stress remains an ASSUMPTION. |
| F-315 | Is a newer JPM edition out? | No. The LTCMA page still shows the 2026 edition on 2026-09-27; the 2026 edition was released 2025-10-20 (search result) | VERIFIED-PRIMARY (page) / SNIPPET-UNVERIFIED (release date) | A 2027 edition may appear before the IPS (Nov 6) or Final Report (Dec 4). **Re-check in October**; it will reflect yields about 100bp higher (F-010). |
| F-316 | strategy_mc matches JPM | Equity log mean 0.0649 and log sd 0.1520 give an annual-return sd of about 16.5% (JPM 16.47%). Bond log sd 0.0340 gives about 3.5% (JPM 3.48%). Correlation -0.01 | VERIFIED-REPO-FILE inputs (derived) | Inputs are faithful to JPM, but i.i.d. lognormal with no fat tails (brief section 11). |
| F-317 | JPM bond assumptions vs today's yields | JPM intermediate Treasuries 4.00% compound (set when the 10Y was 4.16%) vs IEF YTM 5.17% today (F-203) | VERIFIED (derived comparison) | strategy_mc's sleeve bonds are probably conservative by about 1pp a year (ASSUMPTION interpretation). |
| F-318 | Chance U.S. large cap loses money | ~33% over 1 year; ~27% over 2 years (2031 to 2033) | ASSUMPTION (JPM compound/arithmetic, lognormal) | Replaces the chair memo's 36%/32% (16% vol, 5.5%). Model property, not a forecast. |

## E. Simulation outputs (`strategy_mc.py`; all ASSUMPTION-based model outputs, reproduced exactly 2026-09-27)

These are properties of the model, not of the world. The inputs are F-101, F-001 (2Y 4.81%), F-301, F-307 and F-314. The
assumptions are listed in the script docstring and in brief section 11.

| ID | Case | Lock-early (L) | Growth-first (G) |
|---|---|---|---|
| F-401 | Base | Never misses (**by construction**). 2033 surplus p5/25/50/75/95 $159k/$186k/$207k/$232k/$273k | Miss 3.2%. Surplus $20k/$131k/$226k/$338k/$540k |
| F-402 | 2031 floor (80% of sleeve in a 2Y at 4.81%) | p5/50/95 $127k/$165k/$217k | - |
| F-403 | 2028 deposit $75k | Surplus p5/50/95 $84k/$109k/$144k; floor $67k/$87k/$114k | Miss 13.7%; surplus p5/50/95 -$51k/$125k/$396k |
| F-404 | 2028 deposit $0 | Surplus $8k/$11k/$15k; floor $6k/$9k/$12k | Miss 40.8%; surplus -$123k/$25k/$253k |
| F-405 | Equities 5.0% compound | $154k/$200k/$264k | Miss 5.5%; -$4k/$189k/$483k |
| F-406 | 2033 rate shock sd 1.5pp | unchanged | Miss 3.5%; $17k/$226k/$541k |
| F-407 | Sleeve equity 50 / 60 / 70% | p5/50/95 $164k/$205k/$260k; $159k/$207k/$273k; $154k/$209k/$287k | - |

| ID | Fact | Value | Status | Notes |
|---|---|---|---|---|
| F-408 | Growth-first's 2033 reserve price in the model | Flat 5.26% ± 1pp gives $401.3k at the centre, vs $394.9k on the forward curve (F-106) | ASSUMPTION | Overstates G's shortfall slightly (brief section 11). |
| F-409 | **Total equity share after the 2028 deposit** (ladder ≈ 66% of assets, sleeve ≈ 34%) | Sleeve equity 50/60/70% gives **17.0 / 20.4 / 23.8%** of the whole portfolio | ASSUMPTION (sleeve grows 5% in 2027; ladder at forward value $306,077) | The "65/35" WInS mirror is **ladder/sleeve**, not bonds/equity. Read as 65% Treasuries / 35% equity, it holds about 15pp more equity than the plan (resolves brief section 9, WInS mirror inconsistency). |
| F-410 | Council model outputs A2 could not re-run (council scripts were in an earlier session's scratchpad, now gone) | No-lock shortfall 3.3-9.3%. Partial locks 50/80/90/95% fail 35/26/14/3.4% with no 2028 deposit. Median facility $194-212k. G-L median gap -$23k to +$19k; p5 gap $125-150k in L's favour. Twist gap $3.3-4.4k | ASSUMPTION-based, NOT reproducible | Lower authority than F-401 to F-407. Quote only with "council model, unverified". |

## F. Taiwan, FX and inflation

| ID | Fact | Value | Unit | As of | Source | Status | Feeds | Notes |
|---|---|---|---|---|---|---|---|---|
| F-501 | **Taiwan CPI, August 2026** | **+2.04% y/y**; -0.01% m/m (+0.13% seasonally adjusted); Jan-Aug average +1.84% | % | released 2026-09-08 | https://eng.stat.gov.tw/News_Content.aspx?n=2317&s=236681 and https://www.stat.gov.tw/News_Content.aspx?n=3703&s=236675 (DGBAS) | VERIFIED-PRIMARY | F-509 | The CEIC snippet's 2.4% is wrong (S-19). The snippet's "+0.13% m/m" was the seasonally adjusted figure. |
| F-502 | Taiwan CPI, earlier months | Jul +2.54%, Jun +2.60%, May +2.20% y/y | % | 2026 | DGBAS release headlines (www.stat.gov.tw news list) | VERIFIED-PRIMARY | - | - |
| F-503 | Taiwan producer and trade prices, Aug 2026 | PPI +16.75% y/y; import prices (USD) +20.45%; export prices (USD) +23.05% | % | 2026-09-08 | F-501 pages | VERIFIED-PRIMARY | landscape | Strong upstream price pressure (AI boom, Middle East energy shock per DGBAS/CBC text). |
| F-504 | DGBAS forecasts | CPI 2026 **2.07%**, 2027 **1.90%**; real GDP 2026 11.05%, 2027 6.04% | % | 2026-08-14 | https://eng.stat.gov.tw/News_Content.aspx?n=2317&s=236587 | VERIFIED-PRIMARY | F-509 | Confirms the Focus Taiwan snippet. |
| F-505 | Central bank (CBC) forecasts | CPI 2026 2.03%, core 2.16%; 2027 CPI 1.83%, core 1.89%; GDP 2026 11.48%, 2027 5.82%; Jan-Aug core CPI average 2.11% | % | 2026-09-17 | https://www.cbc.gov.tw/en/cp-448-192883-c5fa1-2.html | VERIFIED-PRIMARY | F-509 | - |
| F-506 | **CBC policy rates** | Held: discount rate **2%**, secured-loan refinancing 2.375%, temporary accommodations 4.25% | % | 2026-09-17 | same | VERIFIED-PRIMARY | F-515 | The discount rate has been 2% since 2024-03-22 (CBC home page), so this is the 10th quarterly hold in a row (derived count). |
| F-507 | Taiwan market rates | Overnight interbank call-loan rate **0.812%**; M2 growth 6.79% | % | 2026-09-24 / 09-23 | https://www.cbc.gov.tw/en/mp-2.html | VERIFIED-PRIMARY | F-515 | Taiwan market rates are far below the 2% discount rate. |
| F-508 | **Taiwan construction cost index (2021 = 100)** | Derived total 119.50 (Aug 2026): **+6.53% y/y** (Jul +6.53%). Wage class 123.75, **+8.12% y/y** (published sub-index). Total excluding wages +6.02%. Machinery rental +2.64%. Index was flat in 2024-25 (110.3 in Jan 2024 to 112.9 in Dec 2025) and jumped in Jan-May 2026. **Average since the 2021 base: 3.54%/yr**; Jan 2024-Aug 2026: 3.16%/yr | index; % | 2026-08 | DGBAS CCI platform https://www.stat.gov.tw/CCI/CCI_Site/CCIPrice/PartialPriceClassesList.aspx via `A2_taiwan_cci.py` | VERIFIED-PRIMARY (wage index) / derived total (fit error ≤0.023 points) | F-509, facility-cost framing | The headline 6.54% (udn snippet) is corroborated within 0.01pp but was not read on a primary page, because the ws.dgbas.gov.tw files were blocked. |
| F-509 | Construction costs vs CPI | One month (Aug 2026): 6.54 / 2.04 = **3.2x**. As a trend: CCI about 3.5%/yr since 2021 vs Taiwan CPI 2026-27 forecasts of about 1.8-2.1% | ratio | 2026 | F-501, F-504, F-505, F-508 | derived; long-run CPI history SNIPPET-UNVERIFIED | co-sponsor range | Do not project 6.5%/yr or 3.2x forward; both are a one-year spike (S-34). |
| F-510 | **USD/TWD (FRED DEXTAUS)** | **31.82 TWD per USD** | TWD/USD | 2026-09-18 (updated Sep 21; next release Sep 28) | https://fred.stlouisfed.org/series/DEXTAUS (Fed H.10 noon buying rate) | VERIFIED-PRIMARY | F-512-F-514 | Matches the council's mirror file. |
| F-511 | NT$/US$ closing rate (CBC) | 31.780 | TWD/USD | 2026-09-24 | https://www.cbc.gov.tw/en/mp-2.html | VERIFIED-PRIMARY | - | The chair memo's "31.73 on 9/26" was a Saturday and is unverifiable (S-21). |
| F-512 | **USD/TWD volatility** (daily log changes x √252) | 1y 4.03%; 3y 5.64%; 5y 5.25%; **10y 4.69%**; full history since 1983 4.79%. 10y from month-end values 5.58% (monthly averages give 4.44%, which understates). 10y range 27.52-33.21; 10y change +0.14%/yr; last 12 months +5.61% (TWD weaker) | % a year | to 2026-09-18 | `A2_twd_vol.py` (live FRED) | VERIFIED-PRIMARY inputs (derived) | F-513, co-sponsor range | Replaces the unsourced "5-7%" (S-20). |
| F-513 | Size of real multi-year moves | Since 2006: 2-year sd 6.8% (p5/p95 -12.1%/+10.6%); 6.25-year sd 6.4% (-12.7%/+6.7%). Since 1983: 2-year sd 9.4%, 6.25-year sd 16.0% (includes the 1980s appreciation and 1997). √-time from 10y daily: 2y 6.6%, 6.25y 11.7% | % | to 2026-09-18 | `A2_twd_vol.py` | VERIFIED-PRIMARY inputs (derived) | 2031 range, TWD quote | The period chosen changes the answer a lot. State which one you use. |
| F-514 | FX illustration | $50,000 = NT$1,591,000 at 31.82. If TWD per USD moves -5%/-10%, the same NT$ cost $52,632/$55,556; +5%/+10% gives $47,619/$45,455 | USD | 2026-09-18 | `A2_twd_vol.py` | ASSUMPTION (moves are illustrations) | - | - |
| F-515 | U.S.-Taiwan short-rate gap | Policy: 3.75-4.00 minus 2.00 = 175-200bp (different instruments). Market: interest on reserve balances 3.90 minus Taiwan call rate 0.812 ≈ 310bp | bp | Sep 2026 | F-005, F-006, F-506, F-507 | VERIFIED-PRIMARY inputs (derived) | cost of converting the floor to TWD | The council's "~5.3% over two years" assumed a 2% Taiwan 2-year rate. With market rates the cost is probably ~6-8% over two years (ASSUMPTION). The Taiwan 2-year government yield is UNVERIFIED (S-35). |
| F-516 | Taiwan 10-year yield | ~1.70% | % | 2026-07-14 | snippet (council) | SNIPPET-UNVERIFIED | - | Not found on a primary page by A2. |
| F-517 | Context stated by the official sources | DGBAS: a Middle East conflict since late February 2026 pushed energy costs up. CBC: the ECB hiked twice since June, the BoJ resumed hikes and the Fed "pivoted toward a policy rate increase" | text | Aug-Sep 2026 | F-504, F-505 pages | VERIFIED-PRIMARY | landscape (Phase D) | Background only. |

## G. Competition facts

| ID | Fact | Value | As of | Source | Status | Feeds | Notes |
|---|---|---|---|---|---|---|---|
| F-601 | Client cash flows | $300,000 at the beginning of 2027; $150,000 at the beginning of 2028; ten fixed $50,000 payments at the beginning of each year 2033-2042, "not adjusted for inflation"; Year = calendar year - 2026; all flows at the beginning of the year | case | `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` lines 43-60, 88-92 | VERIFIED-REPO-FILE | everything | Total paid out: $500,000 nominal (derived). |
| F-602 | Deadlines (5:00 p.m. ET) | Roster Oct 9; Trading Notes Oct 23; IPS Nov 6 ("Trading ends and your portfolio is locked"); Final Report instructions Nov 9; Final Report + school documentation Dec 4 | 2026 | `SMApply_Deliverables_Page_2026-09-27.md`; https://globalyouth.wharton.upenn.edu/competitions/investment-competition/ ; https://wghsinvcomp.smapply.us/prog/2026-2027_wharton_global_high_school_investment_competition_/ | VERIFIED-REPO-FILE + VERIFIED-PRIMARY | plan timing | First trading day Sep 28, 2026; practice Sep 15-25; competition ends Dec 4; "10 weeks"; Global Finale April 29-30, 2027. |
| F-603 | IPS format | Title page (1 page max); pitch ≤50 words; IPS ≤500 words; pages 2-3, 2-page max; Times New Roman 12; double-spaced; 1-inch margins; PDF ≤5 MB; no graphics, charts, images, attachments, external links, footnotes or formal citations | - | `2026_WGY_Investment_Policy-FINAL.txt` p.3 | VERIFIED-REPO-FILE | - | Full register: A1. |
| F-604 | Trading Notes | 3 notes, "exactly as it appears in WInS"; reflection ≤100 words each; "Yes, we will verify this" | - | `2026_WGY_Trading_Notes_Analysis-FINAL.txt` p.2 | VERIFIED-REPO-FILE | - | - |
| F-605 | **WInS virtual cash, 2026-27** | "Your team will be responsible for managing a portfolio of **$300,000** in virtual cash." | 2026-09-27 11:49 UTC | https://wghsinvcomp.smapply.us/res/p/faqs/ (public; the page refers to the Oct 9, 2026 roster, so it is this season's) | VERIFIED-PRIMARY | WInS mirror, seed Q3 | Same as Laura's 2027 deposit. Last season's was $500,000 (F-609). Confirm in the team's WInS account. |
| F-606 | **Permitted investments** (the page says "for BOTH contributions") | Permitted: cash; "Any stock from any exchange available on WInS priced at $5 (or the equivalent of $5 in the local currency) or higher"; "Any Exchange-Traded Funds (ETFs) available on WInS"; "Any Government/Treasury Bonds from any exchange available on WInS". NOT permitted: margin trading, short selling, stock-secured debt, crypto, derivatives (options, futures, swaps, etc.), "Anything other than the approved investments listed above" | same | same | VERIFIED-PRIMARY | compliance, instrument types | "For BOTH contributions" is not explained. It may mean WInS will also simulate the $150k contribution; check the logged-in Trading Details page. Whether particular Treasury issues, zero-coupon Treasuries or defined-maturity funds are *available on WInS* is still unknown: PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading. |
| F-607 | WInS mechanics | $25 flat commission per stock transaction; $10 per Treasury bond trade (only on trades that clear); bond prices updated once daily at U.S. market open; bonds pay every six months; non-U.S. equities clear at the end of the next trading day; dividends and coupons credited | same | same | VERIFIED-PRIMARY | trade plan | The FAQ says "you should not be doing a lot of buying and selling" of long-term holdings. |
| F-608 | Required trading activity | The rules page says: "Teams must meet the required trading activity and portfolio management guidelines throughout the competition"; details are on the logged-in SMApply "Trading Details" page | same | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ ; SMApply program page lists "Trading Details" under Pages | VERIFIED-PRIMARY (existence) | compliance | The specific requirements are NOT public. "Sector minimum = team size", "200-trade cap" and "first trade by Oct 10" remain SNIPPET-UNVERIFIED third-party claims. |
| F-609 | 2025-26 season size | More than 6,300 registered teams at the start of trading (2025-09-29; +1,300 on the prior year); $500,000 virtual cash, the first change since 2012 (up from $100,000); about 2,300 teams from 79 countries submitted final reports (Dec 12, 2025; +~30%); "More than 5,400 high school teams ... began" (Mar 20, 2026). Site counters "2025-2026 Participation Completion Numbers": **2,339 teams, 79 countries, 12,145 students, 1,625 advisors** | 2026-01-27 / 03-20 / live | https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/ ; https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/ ; competition page | VERIFIED-PRIMARY | North Star framing | "Nearly 6,000 teams competed" was not found on the official pages I read (SNIPPET-UNVERIFIED; S-25). Top 50 ≈ 2.1% of 2,339 completers (derived). |
| F-610 | 2025-26 results | 1st FigCapital (Stuyvesant HS); 2nd HHA Investments (Colégio Marista de Brasília); 3rd **Riverhawk Traders** (Farmington HS); 11 finalist teams; judges from Aberdeen, Achilles, King Street, Zen Capital Partners, WRDS | 2026-04-30 | https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/ | VERIFIED-PRIMARY | winners.md | Official pages disagree on the 2026 finale dates: "April 25–26" (Apr 30 article) vs "April 24 and 25" (Jan 27 article). |
| F-611 | Judging | "success is not determined by portfolio performance"; the Top 50 are chosen "based on the strength of their Investment Policy Statement (IPS) and Final Reports" (rules page), while SMApply says Trading Notes, IPS and Final Report "are evaluated"; "all five components of the criteria"; no individual feedback | 2026-09-27 | competition page; rules page; SMApply FAQs | VERIFIED-PRIMARY | - | Treat all three as judged (case: "Evaluators will consider the three deliverables together"). |
| F-612 | Rules relevant to the plan | Teams of 4-6; team leader ≥16; "Teams may not contact the Competition client" (disqualification); advisors "may not make decisions on behalf of students or actively participate in ... trading decisions, or strategy development"; AI for brainstorming only; AI material must be cited | 2026-09-27 | rules page | VERIFIED-PRIMARY | Articulation section | Consistent with brief section 4. |

## H. Superseded numbers (old value -> correct value -> why)

| ID | Old value (where) | Correct value | Why |
|---|---|---|---|
| S-01 | Ladder cost "about $295k (±$3k)" (chair memo 2-3) | **$292,264** (F-101) | One official curve, one method (brief section 8.4). |
| S-02 | $292,323 "Curve A" (referee 1; curve.md) | $292,264 | Curve A mixed estimated 1Y/7Y/20Y (4.49/5.11/5.51) with snippets. |
| S-03 | $297,610 (flat 5.17%); "~$297k" (team notes) | retire | Treats a par yield as a zero rate. |
| S-04 | $314,465 "Curve B" | retire | **Curve B is exactly the official curve of 2026-03-20** (1M 3.73 ... 10Y 4.39, 30Y 4.96): six months stale. |
| S-05 | $333,328 (flat 4%); team's "$333k"; "risk-free floor ~$140k" | illustration only | Flat 4% is not today's market. |
| S-06 | DV01 "≈$297/bp", "$290-297" (chair) | $289/bp | Official curve. |
| S-07 | Headroom "15-20bp" (chair); "$7,677" (referee) | $7,736 = 27bp | Official curve. |
| S-08 | -100bp "≈$326k" (chair); $322,931 (curve.md) | $322,864 | Official curve. |
| S-09 | Reserve value at 1/1/2031 "$357-358k", at 1/1/2033 "$396-397k" (chair); "$395.8k" (referee); 2037-42 rungs "$154k" | $356,384; **$394,930**; $155,408 (F-106, F-107) | Official curve. |
| S-10 | Zero rates 2033-42 "5.04-5.38%" (chair) | 5.05-5.46% semiannual (F-011) | Official curve; semiannual bootstrap. |
| S-11 | Implied forward zeros "5.11/5.24/5.46" (curve.md) | 5.08/5.24/5.48% (F-012) | Official curve. |
| S-12 | 20Y "5.45"/"5.51"; 5Y "4.99"; 30Y "5.48"; 1Y "4.49"; 7Y "5.11" (chair, curve.md) | 20Y 5.54; 5Y 4.98; 30Y 5.49; 1Y 4.50; 7Y 5.06 (F-001) | Official CSV (5.45 was the 20Y on 9/23). |
| S-13 | "10-year ~5.1% (highest since late 2023)" (team notes) | 5.17% on 9/25; 5.18% on 9/24 was the highest close since 2007-07-06 (F-004) | The 2023 peak was 4.98%. |
| S-14 | IEF duration "near 7.5 yr" (blog, instruments.md) | 6.95 (June fact sheet); **6.86 (Sep 24)** | Primary sources. |
| S-15 | IEF/TLT "64.7/35.3" (referee), "69.3/30.7" (7.5y case); blueprint "~42% IEF + ~23% TLT" of 65% | 64.8/35.2 on June durations; **62.2/37.8 on current durations** (≈ 40.4% + 24.6% of a 65% hedge) | Rounding of 9.90; durations have moved (F-205). |
| S-16 | Coupon arithmetic "$20k/yr, $6.7k loss" (L defence) vs "$15.5k, $5.2k" (referee) | Both are correct sums: $20.1k/$6.7k for a ladder with $381k of face, $15.5k/$5.2k for a $295k ladder. **The $15.5k/$5.2k framing fits Laura's budget** (F-113) | Different ladders, not an error. |
| S-17 | "$50k in 6 years at 5.26% ≈ $36.9k" (referee section 4) | $36,761 ≈ $36.8k | Arithmetic. |
| S-18 | "If JPM 6.7% is arithmetic the median is 5.52%"; referee MC rows "6.7% arithmetic" | JPM 6.70% is **compound** (7.94% arithmetic) (F-301) | Primary PDF. |
| S-19 | Taiwan CPI Aug "2.4%" (CEIC snippet, chair memo); "+0.13% m/m" | **2.04% y/y; -0.01% m/m** (+0.13% seasonally adjusted) (F-501) | DGBAS release. |
| S-20 | TWD volatility "5-7%" (chair, unsourced); "monthly 4.4%" (taiwan.md) | 4.0-5.6% over 1-10y windows (10y 4.69%); 10y month-end 5.58% (F-512) | The 4.4% used monthly averages, which smooth the series. |
| S-21 | USD/TWD "31.73 (9/26)" (chair) | 31.780 (CBC close 9/24); 31.82 (FRED 9/18) | 9/26 was a Saturday. |
| S-22 | 10Y TIPS "2.85% / breakeven 2.28%" vs "2.653%" (chair) | Real 10Y 2.83% (9/25), 2.85% (9/24); breakeven 2.34% (9/25) (F-008, F-009) | 2.653% was the 9/17 auction yield (snippet), a different measure and date. |
| S-23 | Fed hike "verified in search results" (curve.md, taiwan.md) | VERIFIED-PRIMARY on federalreserve.gov (F-005) | Now read on the primary page. |
| S-24 | "Final Report (due Nov 9)" (chair section 9) | Instructions Nov 9; **report due Dec 4** (F-602) | SMApply and Wharton pages. |
| S-25 | 2025-26 "nearly 6,000 teams competed" | >6,300 registered; >5,400 began; ~2,300 (counter: 2,339) completed final reports (F-609) | Official pages. "Why Laura would choose us over 6,000" is rhetoric; the field judged on final reports is about 2,300. |
| S-26 | WInS starting cash "$500k" (last season) / "unknown" (brief sections 4, 6) | **$300,000** (F-605) | 2026-27 SMApply FAQs (public). |
| S-27 | "Put a number on high certainty: ≥95% Monte Carlo + floor" (winners.md lesson 2) | The council's market-consistent definition (brief section 8.6) | A model probability moves with its inputs: G misses 3.2% or 5.5% depending on the equity assumption (F-401, F-405). |
| S-28 | Liability PV $313.8k, Macaulay 10.4y, modified 9.95y at a flat 4.5% (instruments.md) | Spot PV $288,924; spot duration 10.16y (F-105) | Official curve. |
| S-29 | Median 2033 facility sleeve "$194-212k (four models)" | $207k median (p5 $159k, p95 $273k) in the one reproducible model (F-401) | Reproducible script, JPM inputs. |
| S-30 | G shortfall "3.3-9.3%", "3-8%", "4.3%"; 17% at $75k; 46-55% at $0 | 3.2%; 13.7%; 40.8% (F-401, F-403, F-404) | JPM compound inputs. Still model-dependent. |
| S-31 | Rung order "nearest maturity first" (chair memo section 1.3, round 1) | **Longest-dated first** (round 2; brief section 7) | A design decision, not a number. The current strategy text uses longest-first. |
| S-32 | "iBonds Dec 2033-2035 exist; later vintages unverified" (chair) | Dec 2026-2036 exist; none for Dec 2037-2043 (F-206) | iShares screener. |
| S-33 | "Taiwan inflation ~1.8-2.2% (unverified)" (team notes) | 2026: 2.07% (DGBAS) / 2.03% (CBC); 2027: 1.90% / 1.83% (F-504, F-505) | Primary forecasts. |
| S-34 | "Construction costs ~3.2x CPI"; "×0.881 over two years if +6.54% persists" (referee) | 3.2x is a one-month ratio. The CCI trend is ~3.5%/yr since 2021 (~0.93 over two years at that rate) (F-508, F-509) | The 2026 jump followed two flat years. |
| S-35 | "Converting the floor to TWD costs ~5.3% over two years"; "2-year forward ~5% fewer TWD per USD" | Probably larger (~6-8%): Taiwan market short rates (0.81%) are well below the 2% discount rate used as a proxy (F-515) | Taiwan 2-year yield still UNVERIFIED. |
| S-36 | Twist gap "$3.3-4.4k" (referee) | unchanged, ASSUMPTION | Not recomputed; it rests on modelling IEF as an 8.5-9.5y bond and TLT as a 30y bond. |
| S-37 | "One sd of two-year FX is ±6.6%" (referee) | Consistent: 6.6% by √-time; 6.8% realised since 2006 (F-513) | Confirmed. |
| S-38 | TWD 10-year range 27.52-33.21, +0.14%/yr, vol 10y/5y/3y/1y 4.7/5.2/5.6/4.0% (taiwan.md) | Confirmed from live FRED (F-512) | The mirror file matched the primary series. |

**Brief section 10 inconsistencies: resolution map.** All resolved; the primary or verified value wins:
- Ladder $295k vs $292,264: resolved by S-01.
- Taiwan CPI 2.4% vs 2.04%: resolved by S-19.
- Rung order: resolved by S-31 (longest-first).
- 20Y 5.45/5.51 vs 5.54: resolved by S-12.
- TWD volatility 5-7% vs 4.7%: resolved by S-20.
- Coupon arithmetic: resolved by S-16.
- Fed hike: resolved by S-23.
- Chair memo's Nov 9 date: resolved by S-24.
- IEF 6.95 vs ~7.5: resolved by S-14 (now 6.86).
- winners.md "≥95% MC": resolved by S-27.
- 6,300+ vs nearly 6,000: resolved by S-25.

## I. Still unverified or blocked (say so; never guess)

| Item | What was tried | Status |
|---|---|---|
| DGBAS attachment files (CPI tables, CCI headline file) on ws.dgbas.gov.tw | curl: TLS "unable to get local issuer certificate", even with the proxy CA bundle; WebFetch: EGRESS_BLOCKED | Blocked. Headline CPI was read on eng.stat.gov.tw instead; the CCI total was derived (F-508). |
| Exact CCI headline "+6.54%" | derived 6.53% | SNIPPET-UNVERIFIED (corroborated). |
| Taiwan CPI history 2022-2025; Taiwan 2-year and 10-year government yields | not found on reachable primary pages | SNIPPET-UNVERIFIED / UNVERIFIED. |
| SMApply "Trading Details" page (logged-in): trade minimums, sector rules, first-trade deadline, what "for BOTH contributions" means | public pages only | UNVERIFIED. The team must read it. |
| Which specific securities (Treasury issues, zero-coupon Treasuries, defined-maturity funds, IEF/TLT) are *available on WInS* | not accessible | UNVERIFIED. Confirm against this year's WInS list/rules before trading. |
| List & Lucking-Reiley (2002) "~6x more giving from 10% to 67% seed" | SSRN 403; journal site 403 | SNIPPET-UNVERIFIED (brief section 8.17: a mechanism only). |
| Council model outputs (F-410) | scripts not preserved | Not reproducible. |
| 2027 JPM LTCMA | not yet published (F-315) | Re-check in October. |
| Festival attendance "2,000+" and other figures in the team's client documents | not checked by A2 (Laura facts belong to other agents) | SNIPPET-UNVERIFIED. |

## Sources (all accessed 2026-09-27)

**Repo files**
- `competition/official_market_data/` (Treasury CSV; IEF and TLT fact sheets p.1; JPM LTCMA p.2).
- `competition/official/2026_27/` (case, IPS guide, Trading Notes guide, SMApply deliverables page).
- `research/verified_2026-09-27/*.py`.
- Council files as cited.

**Web (primary)**
- home.treasury.gov: nominal and real par-yield CSVs for 2026.
- fred.stlouisfed.org: DEXTAUS, DGS10.
- federalreserve.gov: monetary20260916a.htm, monetary20260916a1.htm, fomcprojtabl20260916.htm, openmarket.htm.
- ishares.com: IEF and TLT product pages, Dec 2034 iBonds page, product screener.
- am.jpmorgan.com: LTCMA landing page.
- eng.stat.gov.tw and www.stat.gov.tw: DGBAS releases, CCI platform.
- cbc.gov.tw: en/mp-2.html, en/cp-448-192883-c5fa1-2.html.
- globalyouth.wharton.upenn.edu: competition page, FAQ, rules-roles, three news articles.
- wghsinvcomp.smapply.us: program page, /res/p/faqs/, /res/p/deliverables/.

## What this teaches

A number is only as strong as the path back to where it came from. In one afternoon this register found several
things:
- A "mystery" yield curve was simply six months old.
- A heated argument about coupon reinvestment was two correct sums about two different ladders.
- The most important price in the plan, a ladder "fitting inside $300k", has been true on only 12 trading days this year.
- The competition had already published how much virtual cash each team gets.

Checking the original source is not bureaucracy. It changes what you should do. The habit to keep is to write the
source and its status next to every number when you first use it, and to re-check the few numbers your plan depends
on (the curve, the rules, the durations) on the day you act.
