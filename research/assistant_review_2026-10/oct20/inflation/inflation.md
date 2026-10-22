# Inflation: what it does to Laura's projections, payments and facility money (facts and numbers, 20 Oct 2026)

> **Verified 20 Oct (`oct20/verify_infl_num/verify_infl_num.md`): all data re-fetched and confirmed.** Fix one reasoning error: the FX/building-cost correlation is NOT a "natural partial offset" - a weaker NT$ and slower building inflation both help a US$ holder and tend to come together, so the negative correlation WIDENS the spread (SD of log building power 0.111 vs 0.098 if independent at 2 years; p5/p95 -22.0% / +12.5%). VT row: $33,515 -> $47,007 -> $40,534 (not $33,170). Real ladder yield about 2.7-2.9% (not 2.6%), in line with the 10-year TIPS yield 2.80%. JPM wording is "a balanced global stock-bond portfolio" (not "60/40"). 54% -> 55% in 3b. Coupon gap "about $19.5-21.3k".


AI-generated research by Claude Code for Team Caplet. These are facts, numbers and a checklist. Nothing here is text to submit. If the team uses any of it, log that use in the AI-use record now and in the Final Report's Works Cited later (Wharton AI Policy, https://globalyouth.wharton.upenn.edu/ai-policy/).

**Labels.** VP = verified on a primary source (URL and access date given). CASE = the official case file. MODEL = computed here, with the inputs shown. HIST = computed from historical data, which describes the past and does not forecast. UNVERIFIED = could not be confirmed.

**Access dates.** All web data was fetched on 19 Oct 2026 between 21:30 and 22:30 UTC (20 Oct morning Sydney).

**Paths.** `INF/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/inflation/`. Scripts are in `INF/scripts/`, outputs in `INF/data/*_out.txt`, raw downloads in `INF/raw/`. `case:` = `/home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`.

**Base date for "real" values.** 1 Jan 2027 (Year 1), when Laura's $300,000 goes in (case:43-60). The older fact register (F-114) used 2026 money: one extra year of discounting, so its figures are about 2.5% lower. **Pick one base date and state it.**

---

## 0. The answer in eight points

1. **The ten payments carry no inflation funding risk, by the case's own rule.** Each payment "is a fixed $50,000 and is not adjusted for inflation" (case:90). Nominal Treasuries bought in 2027-28 pay fixed dollars, so inflation after purchase does not change whether the payments are made. It changes only what they buy.
   TIPS would not be needed even if allowed, and they are not allowed: the live FAQ lists "TIPS (Treasury Inflation-Protected Securities)" under "NOT permitted", for "BOTH contributions, the IPS and Final Report" (VP, https://wghsinvcomp.smapply.us/res/p/faqs/; copy `INF/raw/faqs.txt:42-56`).
2. **What the payments buy (MODEL).** At 2.5% US inflation (the JPM 2026 LTCMA figure), the ten payments total $500,000 nominal but $386,777 in Jan-2027 dollars. The 2042 payment buys 80% of what the 2033 one buys. At 2.0% the total is $406,790; at 3.5% it is $350,118.
3. **In Taiwan the dollar has not eroded at the US rate (HIST, new).** Since 2000, Taiwan CPI rose 1.25%/yr and US CPI 2.63%/yr. Yet NT$ per US$ went from 30.75 (Jan 2000) to 31.85 (Sep 2026). Purchasing-power parity (PPP) would have predicted about 21.5.
   So a fixed US$ amount spent in Taiwan lost buying power at roughly *Taiwan's* inflation rate, not the US rate. The US-CPI figures in point 2 bracket the answer from the worse side. With FX flat and Taiwan CPI at 1.9%, the 2042 payment buys 84% of the 2033 one, not 80%.
4. **Official Taiwan forecasts are below 2% from 2027 (VP).** DGBAS (14 Aug): 2.07% for 2026, 1.90% for 2027. CBC (17 Sep): 2.03% and 1.83%. IMF WEO (Oct 2026): 2.0% for 2026, then 1.5-1.8% a year for 2027-2031.
   But the latest monthly reading jumped: **Taiwan CPI was +2.73% y/y in September 2026** (core +2.52%; DGBAS, released 7 Oct).
5. **Taiwan building costs are rising fast now (VP, official DGBAS series, no longer derived).** The construction cost index (CCI, 2021 = 100) was 120.26 in Sep 2026, **+7.29% y/y**, up from +6.54% in August, with wages inside the index +9.29%. The building-construction group, the closest to a residency facility, rose +5.93%.
   Over longer periods: 2.9%/yr since 1991, 3.1%/yr since 2000, 2.5%/yr since 2010 and 3.6%/yr since the 2021 base. That is 1.1-2.3 points a year above Taiwan CPI over the same windows.
6. **What the facility money buys (MODEL/HIST).** Between a 2031 quote and Jan 2033, a fixed US$ range loses about 4-7% of its building power at normal cost growth (1.9-3.6%/yr), and about 13% if the 2026 pace (7.3%) continued.
   Add the exchange rate and history says more. In 2-year windows since 2000, a fixed US$ amount's Taiwan building power changed by p5 -22% / median -5% / p95 +12.5%. It fell more than 10% in 32% of windows.
7. **Stocks are a weak inflation shield over five years (HIST, new).** In the highest-inflation fifth of 5-year windows since 1950 (US CPI of 4.6%/yr or more), US stocks' median real total return was **0.7%/yr**, and 47% of those windows lost real value. In the other four fifths the medians were 8.9-11.8%.
   This tests the live IPS idea that "the equity half Laura keeps is her defense" against inflation and the Taiwan dollar (`oct19/drive/ips_report_live.md:157`).
8. **The 2026 rise in US yields was mostly real, not an inflation scare (VP, FRED/Treasury).** From end-2025 to 16 Oct 2026 the 10-year yield rose +91bp: real +81bp, breakeven +10bp. Markets still price about 2.35-2.47% inflation over 5-20 years, even with headline CPI at 3.7% y/y (Sep 2026).

---

## 1. US inflation: what forecasters and markets expect (all VP unless marked)

| Measure | Latest | Date / source | Note |
|---|---|---|---|
| CPI-U, headline, y/y | **3.74%** (NSA); 3.72% (SA) | Sep 2026; FRED CPIAUCNS / CPIAUCSL (BLS data), updated 14 Oct 2026. https://fred.stlouisfed.org/series/CPIAUCNS | The BLS page returned 403 to curl, so the figures were read via FRED. Oct 2025 CPI was never published (FRED gap); comparisons are date-aligned (`INF/scripts/us_now.py`). |
| Core CPI y/y | 2.57% | Sep 2026; FRED CPILFESL | |
| PCE price index y/y | 3.42% | Aug 2026; FRED PCEPI | |
| US CPI, past averages (HIST) | 10y **3.39%**/yr; 20y 2.57%; 30y 2.56%; 40y 2.83% | to Sep 2026; FRED CPIAUCNS | The last 10 years ran well above 2.5% |
| Breakeven inflation (nominal minus TIPS par yield) | 5y **2.38**, 7y **2.37**, 10y **2.35**, 20y **2.47**, 30y **2.27** | 19 Oct 2026; Treasury daily par and real par curves, https://home.treasury.gov/resource-center/data-chart-center/interest-rates/ (`INF/raw/par_202610.csv`, `real_2026.csv`) | FRED T5YIE 2.38 / T10YIE 2.35 / 5y5y forward T5YIFR 2.32 on 19 Oct. 2026 range of the 10y: 2.18-2.50. Breakevens include risk and liquidity premia; they are prices, not forecasts. |
| Cleveland Fed model, expected inflation | 1y 2.98; 2y 2.87; 5y 2.77; 7y 2.75; **10y 2.73**; 20y 2.70; 30y 2.70 | Oct 2026 run, "Last updated October 14, 2026"; https://www.clevelandfed.org/indicators-and-data/inflation-expectations; FRED EXPINF*YR | Model "uses Treasury yields, inflation data, inflation swaps, and survey-based measures". About 0.4 points above breakevens (the model estimates the risk premia separately; the gap's cause is not tested here). Up from 2.30 (10y) a year ago. |
| Survey of Professional Forecasters (Philadelphia Fed), Q3 2026 | 10-year CPI (2026-2035) **2.30%**; 5-year (2026-2030) 2.60%; CPI Q4/Q4 2026 3.6, 2027 2.3, 2028 2.3 | released 14 Aug 2026; https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/spf-q3-2026 (`INF/raw/spf_q3_2026.txt:222, 300-356`) | 10y CPI is 0.10 lower than the previous survey |
| Fed SEP medians (PCE, not CPI) | 2026 3.7; 2027 2.3; 2028 2.1; 2029 2.0; longer run **2.0** | 16 Sep 2026; https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm | CPI usually runs a little above PCE (general knowledge; size UNVERIFIED) |
| IMF WEO Oct 2026, US CPI (annual average) | 2026 3.6; 2027 2.8; 2028 2.1; 2029-2031 1.9 | IMF DataMapper API, source "World Economic Outlook (October 2026)", modified 8 Oct 2026; https://www.imf.org/external/datamapper/api/v1/PCPIPCH/USA | 2027-31 average 2.12% |
| JPM 2026 LTCMA, U.S. inflation | **2.50%** compound (2.52% arithmetic, 1.77% volatility) | data as of 30 Sep 2025; repo file `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf` | The team's current anchor |
| JPM **2027** LTCMA | Published ("data as of September 2026"). The public page states U.S. large cap 7.5% (up 80bp) and a 60/40 portfolio at 7.0%, "more inflation volatility", and a "higher stock-bond correlation" | https://am.jpmorgan.com/us/en/asset-management/adv/insights/portfolio-insights/ltcma/ (`INF/raw/jpm_ltcma.txt:186-193`) | **UNVERIFIED: its U.S. inflation figure.** The matrix and report PDFs sit behind a login. Ask the advisor to download the USD matrix if the team wants the 2027 edition; otherwise state "2026 edition" explicitly. |

**Where 2.5% sits (MODEL comparison).** The forward-looking anchors run from 2.30% (SPF) through 2.35-2.47% (breakevens) to 2.73% (Cleveland Fed); IMF and Fed longer-run figures are about 2.0-2.1% (the Fed's on the PCE basis). 2.5% is inside that band. A 3.5% stress is about the realised 10-year average to Sep 2026 (3.39%).

**History as a spread, not a forecast (HIST, rolling monthly windows of US CPI).**

| Horizon | Window ends | p5 | median | p95 | worst |
|---|---|---|---|---|---|
| 6 years (Jan 2027 → Jan 2033) | since 1950 | 1.37%/yr | 2.76% | 8.60% | 9.33% |
| 6 years | since 2000 | 1.43% | 2.43% | 3.91% | 4.56% |
| 15 years (Jan 2027 → Jan 2042) | since 1950 | 1.74% | 3.19% | 7.06% | 7.40% |
| 15 years | since 2000 | 1.98% | 2.45% | 3.19% | 3.32% |

Source: `INF/data/us_now_out.txt`. The choice of history changes the tail a lot. Since 1950 the tail includes the 1970s.

---

## 2. Taiwan: prices, construction costs, wages, exchange rate (all VP unless marked)

**Consumer prices** (DGBAS, CPI 2021 = 100):

| Item | Figure | Source |
|---|---|---|
| CPI, Sep 2026 | 112.82; **+2.73% y/y**, +0.44% m/m; Jan-Sep +1.94% y/y | "The Price Indices for September 2026", posted 2026-10-07, https://eng.stat.gov.tw/News_Content.aspx?n=2317&s=236760; Table 1 `cpi.xls` (`INF/raw/dl/cpi_sep2026.xls`) |
| Core CPI (excluding fruit, vegetables and energy) | +2.52% y/y; Jan-Sep +2.15% | same table |
| Items a residency would pay for (context only, not a budget) | Residential rents +1.72%; electricity +4.35%; food away from home +3.04%; services +2.49% | same table |
| Monthly y/y path in 2026 | Jan 0.71, Feb 1.75, Mar 1.20, Apr 1.72, May 2.19, Jun 2.56, Jul 2.52, Aug 2.05, **Sep 2.73** | DGBAS time series `cpiidx.xls` (https://ws.dgbas.gov.tw/001/Upload/464/relfile/10320/2710/cpiidx.xls, linked from https://eng.stat.gov.tw/cp.aspx?n=2327) |
| Annual averages | 2021 1.97, 2022 2.95, 2023 2.49, 2024 2.18, 2025 1.66 | same file |
| Long-run averages (HIST) | 5y 2.30%/yr; 10y 1.61%; 20y 1.41%; 30y 1.15%; since 2000 1.25% | same file (`INF/data/tw_stats_out.txt`) |
| Rolling 15-year CPI average, windows ending since 2000 (HIST) | p5 0.95%, median 1.22%, p95 2.41%, max 2.61% | same |
| DGBAS forecast | CPI 2026 **2.07%**, 2027 **1.90%** | "GDP: Preliminary Estimate for 2026Q2 and Outlook for 2026-27", posted 2026-08-14, https://eng.stat.gov.tw/News_Content.aspx?n=2317&s=236587. The next outlook date is UNVERIFIED (probably late Nov). |
| CBC forecast | CPI 2026 **2.03%** (core 2.16%); 2027 **1.83%** (core 1.89%); "likely ease to below 2% next year" | CBC press release, 17 Sep 2026, https://www.cbc.gov.tw/en/cp-448-192883-c5fa1-2.html |
| IMF WEO Oct 2026, Taiwan CPI | 2026 2.0; 2027 1.8; 2028 1.6; 2029 1.5; 2030 1.6; 2031 1.5 (2027-31 average 1.60%) | https://www.imf.org/external/datamapper/api/v1/PCPIPCH/TWN (source "World Economic Outlook (October 2026)") |

**Construction costs** (DGBAS CCI, 2021 = 100, official series):

| Item | Figure | Source |
|---|---|---|
| Total, Sep 2026 | **120.26; +7.29% y/y**; +0.65% m/m; Jan-Sep +4.87% | "The Changes of Construction Cost Indices", `cci.xls` (https://ws.dgbas.gov.tw/001/Upload/464/relfile/10320/2710/cci.xls) |
| Parts (y/y, Sep 2026) | Materials +7.27% (metal products +7.57%, electrical machinery +18.03%, plastics +18.14%, cement -0.79%); services +7.32% (**wages +9.29%**, equipment rent +2.83%) | same |
| Building construction group (closest to a facility) | 116.86; **+5.93% y/y**; Jan-Sep +3.84%. Civil engineering: 124.60, +8.88% | same |
| y/y path in 2026 | Jan 1.79, Feb 2.26, Mar 2.72, Apr 4.45, May 5.83, Jun 6.42, Jul 6.54, Aug 6.54, **Sep 7.29** | `cciidxc.xls` |
| Annual averages | 2021 +10.9, 2022 +7.4, 2023 +1.7, 2024 +2.0, 2025 +0.8. Falls in 2009 (-8.9), 2013, 2015 (-2.8) and 2016 | `cciidx.xls` (`INF/data/tw_stats_out.txt`) |
| Long-run pace (HIST) | Since 1991 2.87%/yr (Taiwan CPI 1.57%); since 2000 3.09% (CPI 1.25%); since 2010 2.49% (CPI 1.41%); last 10y 3.91% (CPI 1.61%); since the 2021 base 3.63% (building group 3.06%) | same |
| 24-month change (windows ending since 2000) | p5 -4.2%, median +4.3%, p95 +20.8% (worst -12.0%, best +30.0%) | same |
| 76-month change (Sep 2026 → Jan 2033 length) | p5 +0.7%, median +20.2%, p95 +47.2% | same; overlapping windows, so only about 4 independent periods |

**Corrections to older repo numbers.** The derived Aug-2026 CCI of 119.50 matches the official 119.48. The "Average since 2021 base 3.54%/yr" (F-508) is now 3.63% with September. The "6.53% y/y" is now 7.29% (September).

**Wages** (DGBAS, Aug 2026): average regular earnings of all employees NT$49,518, +3.00% y/y; median NT$39,714, +3.17%. Post date 2026-10-15, https://eng.stat.gov.tw/News_Content.aspx?n=2317&s=236790.

**Exchange rate.**

| Item | Figure | Source |
|---|---|---|
| NT$ per US$ | **32.445** (CBC closing rate, 19 Oct 2026); 32.40 (FRED DEXTAUS, 16 Oct) | https://www.cbc.gov.tw/en/mp-2.html; https://fred.stlouisfed.org/series/DEXTAUS |
| A year earlier | 30.63 (16 Oct 2025), so the NT$ is 5.8% weaker. 2026 range 31.27-32.44 | FRED |
| Range since 2000 (month-end) | 27.66 (Aug 2021) to 35.11 (Feb 2002) | FRED (`INF/data/tw_stats_out.txt`) |
| 24-month change (windows ending since 2000; HIST) | p5 -10.4%, median -0.4%, p95 +11.5%; worst -15.0%, best +16.7% | matches `oct19/cosponsor/cosponsor_research.md:154-160` |
| 76-month change (since 2000) | p5 -11.8%, median 0.0%, p95 +26.3% | |
| PPP check (HIST) | From Jan 2000: Taiwan/US price ratio -30.1%, so PPP predicted 21.48; actual 31.85. From Jan 2010: PPP 25.96 vs actual 31.85. From 1983: PPP 23.31 vs actual 31.85 | FRED CPIAUCNS + DGBAS CPI + FRED DEXTAUS (`INF/scripts/tw_stats.py`) |

**Since the 2025-26 weakening**, the same US$145,000 is NT$4.70m at 32.445, against NT$4.63m at 31.94 on 9 Oct (+1.6%). Any NT$ figure goes stale within weeks. **Date it.**

---

## 3. The fixed $50,000 payments in real terms

**3a. US dollars, 1-Jan-2027 money (MODEL; `INF/scripts/model.py` section A, checked independently by `check2.py`)**

| Payment | 2.0% | 2.5% (JPM 2026) | 3.5% (stress) |
|---|---|---|---|
| 2033 | $44,399 | $43,115 | $40,675 |
| 2034 | $43,528 | $42,063 | $39,300 |
| 2035 | $42,675 | $41,037 | $37,971 |
| 2036 | $41,838 | $40,036 | $36,687 |
| 2037 | $41,017 | $39,060 | $35,446 |
| 2038 | $40,213 | $38,107 | $34,247 |
| 2039 | $39,425 | $37,178 | $33,089 |
| 2040 | $38,652 | $36,271 | $31,970 |
| 2041 | $37,894 | $35,386 | $30,889 |
| 2042 | $37,151 | $34,523 | $29,845 |
| **Total (nominal $500,000)** | **$406,790** | **$386,777** | **$350,118** |
| 2042 vs 2033 buying power | 83.7% | 80.1% | 73.4% |
| Ten payments' cumulative shortfall vs ten payments holding 2033's buying power (2033 $) | $41,888 | $51,457 | $69,616 |

Other anchors (same method): 2.3% (SPF) total $394,641; 2.4% (breakeven) $390,686; 2.7% (Cleveland Fed) $379,098.

**Historical spread (HIST).** Against US CPI 15-year windows ending since 2000, the 2042 payment would be worth p5 $31,235 / median $34,761 / p95 $37,274. Since 1950 (including the 1970s): p5 $17,983 / median $31,230.

**3b. NT$ terms: what each payment buys in Taiwan (MODEL; `model.py` section B)**

- Conversion: $50,000 = NT$1,622,250 at 32.445 (CBC, 19 Oct). Each payment is then deflated by a Taiwan price path to Jan-2027 NT$.
- Percentages are of NT$1.62m. Ten payments at today's value would be NT$16.2m.

| FX path → / Taiwan prices ↓ | 1.5% | 1.9% (DGBAS 2027 forecast) | 2.5% | 3.0% (wage-like) |
|---|---|---|---|---|
| **FX flat at 32.445** (the 2000-2026 pattern) | 2033 91% / 2042 80%; total NT$13.9m | 89% / **75%**; NT$13.3m | 86% / 69%; NT$12.5m | 84% / 64%; NT$11.9m |
| **NT$ +0.6%/yr** (PPP at US 2.5% vs TW 1.9%) | 88% / 73%; NT$13.1m | 86% / 69%; NT$12.5m | 83% / 63%; NT$11.8m | 81% / 59%; NT$11.2m |
| **NT$ 10% stronger** from 2033 (29.20) | 82% / 72%; NT$12.5m | 80% / 68%; NT$12.0m | 78% / 62%; NT$11.3m | 75% / 58%; NT$10.7m |
| **NT$ 10% weaker** from 2033 (35.69) | 101% / 88%; NT$15.3m | 98% / 83%; NT$14.7m | 95% / 76%; NT$13.8m | 92% / 71%; NT$13.1m |
| Since-2000 extremes 27.66 / 35.11 | strongest: 78% / 68% | 76% / 64% | 74% / 59% | 71% / 55% |

**What the table shows (MODEL).**
- The spread across these plausible paths for the 2042 payment runs from about 54% to 88% of today's NT$ value. The exchange-rate paths and the Taiwan-price paths each move it by roughly 15-20 points.
- In the base cell (FX flat, 1.9%), the erosion from 2033 to 2042 is to 84%, close to the 2.0% US-CPI column. In the PPP cells it is about 80%, the same as US CPI at 2.5%.
- **So state which frame is used: US CPI (simple, conservative) or Taiwan CPI with a stated FX assumption.**

**3c. What this means for the commitment (facts, no recommendation)**
- **Funding.** Inflation does not create a payment shortfall: the payments are nominal by case rule (case:90), and the ladder is nominal.
  The plan's nominal risk runs the other way: **falling** yields cut the income reinvested from coupons. The oct19 coupon study puts a permanent 2-point fall at about $19-21k short (`oct19/out/Caplet_Update_19Oct2026.md:31`). Lower-inflation worlds tend to be lower-yield worlds; that link is an interpretation, not tested here.
- **Who covers the erosion.** The case says "any operating support beyond Laura's commitment, may come from co-sponsors, grants, collaborators, program fees, continued business income, or other sources" (case:85-86). The real-value gap is therefore not a Laura liability. It is a fact co-sponsors will notice.
- **Scale check (MODEL).** The ten-year cumulative erosion is about $32k (TW 1.5%, FX flat) to $40k (TW 1.9%, FX flat), $50-51k (2.5%, or PPP) and $70k (US 3.5%), all in 2033 dollars.
  Laura's kept half is "about $24-29k in a middle case and $0-12k at 1-in-20" (`oct19/out/Caplet_Update_19Oct2026.md:328`). The kept half cannot cover the payments' real erosion, and the case does not ask it to.

---

## 4. The facility contribution: buying power 2031-2033 (and from today)

Range used for illustration: floor about $145,000 and top about $168,000 (the V5 IPS range; `oct19/numbers/findings.md:85, 158`). The bottom is set by a rule, not a fixed dollar figure (`oct19/out/Caplet_Update_19Oct2026.md:330`).

**4a. Building-cost drift only, FX flat (MODEL; `model.py` section C, `extras.py`)**

| Taiwan building-cost growth | Jan 2031 → Jan 2033: building lost on $145k / $168k | Sep 2026 → Jan 2033 (6.34y): building power | $145k in Sep-2026 building, NT$ |
|---|---|---|---|
| 1.9%/yr (CPI-like; understates building) | -3.7%: $5.4k / $6.2k | -11.2% | NT$4.18m (vs NT$4.70m today) |
| 2.5%/yr (CCI 2010-2026) | -4.8%: $7.0k / $8.1k | -14.5% | NT$4.02m |
| 2.9%/yr (CCI 1991-2026) | -5.6%: $8.1k / $9.3k | -16.6% | NT$3.93m |
| 3.6%/yr (CCI since 2021 base) | -6.8%: $9.9k / $11.5k | -20.1% | NT$3.76m |
| 7.3%/yr (last 12 months; do not project) | -13.1%: $19.1k / $22.1k | -36.0% | NT$3.01m |

**4b. Exchange rate plus building costs together (HIST; `tw_stats.py`, `model.py`)**
- Building power of a fixed US$ over 24 months = (NT$ per US$ change) ÷ (CCI change), same windows, since 2000 (321 overlapping monthly windows, about 13 independent).
  Result: **p5 -22.0% / p25 -12.3% / median -5.2% / p75 +2.6% / p95 +12.5%**. It fell in 69% of windows and by more than 10% in 32%.
- Robustness: with monthly-average FX the result is -21.9 / -5.3 / +12.1. Since 1993: -22.0 / -3.1 / +14.6.
- Applied to a 2031 quote at a 32.445-equivalent rate, the building it buys by 2033 is:
  - $145k (NT$4.70m): **NT$3.67m / 4.13 / 4.46 / 4.83 / 5.29m** (p5 / p25 / median / p75 / p95).
  - $168k (NT$5.45m): NT$4.25m / 4.78 / 5.17 / 5.59 / 6.13m.
- Over 76 months (today → 2033, since 2000): median **-17.7%**, p5 -34.8%, p95 +20.0%. It fell more than 10% in 62% of windows.
- **Natural partial offset.** The 24-month FX and CCI moves are negatively correlated (-0.26; -0.45 over 76 months, since 1993). Years when the NT$ weakened tended to be years of lower building inflation. The prior D4 memo found -0.36 on annual data.

**4c. Effects on the floor's real value (MODEL)**
- The floor is bought in Jan 2028 and pays out around Jan 2033 (5 years). Its real loss:
  - US CPI: -9.4% at 2.0%, **-11.6% at 2.5%**, -15.8% at 3.5%.
  - In Taiwan building terms: -13.3% at 2.9%, -16.2% at 3.6%.
- **Check of the live IPS.** It says "Inflation of 2.5% would cut the floor's real value by about 12% by 2033" (`oct19/drive/ips_report_live.md:30`). That is correct if measured from the Jan 2028 purchase; from Jan 2027 it is 13.8%. **Name the start date.** The line measures US CPI, not Taiwan building costs (which give 13-16%).
- In Jan-2027 dollars, $150k (IBTM in Dec 2032) is worth $133.2k at 2.0%, $129.3k at 2.5% and $122.0k at 3.5%. The range $145k-$168k becomes $125.0k-$144.9k at 2.5%.

**4d. Facts that bear on "responsible" and "flexibility" (no recommendation)**
- The case asks for a "dollar range" (case:117). In US$, the bought floor is unaffected by inflation. What inflation and FX change is what the dollars build, and both effects fall on whoever budgets the building in NT$.
- Between a 2031 quote and 2033 delivery, normal cost drift is 4-7% (one-directional). The FX-plus-cost band (p5 -22% to p95 +12.5%) is two-sided and far wider than the US$ uncertainty of the bought floor.
- Hedging is outside the rules. A NT$ forward is a derivative ("NOT permitted", FAQ). Taiwan equities as a currency hedge were rejected on substance before (`snap/main/research/insight_v1/phase_D/D4_taiwan_fx.md`, E20). Holding the money in US$ until contracts are signed keeps the option to re-scope (D4 implication 4, still valid).
- **The kept half as an inflation buffer (MODEL comparison).** A 2-year drift on the top of the range at 2.9-3.6% is $9-11k. The kept half's bad case is $0-12k. In 5-year high-inflation windows, stocks' median real return was about 0.7%/yr (section 5). So "the equity half is her defense" against inflation is thin on both size and behaviour. Whether that matters is a team judgement about what "responsible" means (D6 in the IPS kit).

---

## 5. Inflation and the portfolio projections

| Sleeve | What inflation does (facts) | Numbers |
|---|---|---|
| **Payment ladder** (Treasuries 2033-2042, bought Jan 2027, topped up Jan 2028) | Nominal and matched to nominal payments, so no funding effect after purchase. **Before** purchase, higher inflation expectations at an unchanged real yield raise nominal yields and make the ladder cheaper; lower ones make it dearer | MODEL, `model.py` D (par yields used as zero rates, an approximation): DV01 **$289/bp** at the 19 Oct curve, the same as the verified 25 Sep figure (CLAUDE.md, `research/verified_2026-09-27/official_curve_pv.py`). ±50bp ≈ -$14.1k / +$14.9k. Do not quote this PV ($295k) as the cost; use the team's chosen basis (A-E) |
| | 2026's yield rise was real, not inflation (VP: FRED DGS/DFII) | End-2025 → 16 Oct: 10y +91bp nominal = +81bp real + 10bp breakeven; 7y +104 = +93 + 11; 5y +116 = +105 + 11. The 10y TIPS yield hit 2.95% on 5 Oct, the highest since Nov 2008 (3.15). The team note "121bp, 113bp real" (`oct19/drive/notes_and_discussions_live.md:198`) depends on the start date: the 2026 low-to-high was +134 / +123. Same conclusion; **date it** |
| | Real yield of the ladder | Nominal about 5.0-5.1% minus breakeven about 2.4% ≈ **2.6% real**, consistent with the 7-10y TIPS yields of 2.67-2.80% (19 Oct) |
| **Floor (IBTM, Jan 2028 → Dec 2032)** | Nominal; real value erodes | See 4c: -11.6% at 2.5% over 5 years |
| **VT (global equity)** | Nominal 7% assumed (live IPS:27, "7% a year before inflation"); real ≈ 4.4% at 2.5% | JPM 2026 AC World 7.00% compound → real 4.90% / 4.39% / 3.38% at 2.0 / 2.5 / 3.5% inflation. $33,170 (Jan 2028) → $46,523 nominal in Jan 2033 → $40,116 in Jan-2027 $ at 2.5% |
| | Short-run behaviour in high inflation (HIST: Shiller monthly US total-return data, `INF/scripts/stocks_inflation.py`) | 5-year windows since 1950 (n=921): corr(inflation, real return) **-0.47**. Highest-inflation fifth (4.6-10.1%/yr): median real **0.7%/yr**, 47% negative. Lowest fifth (0.8-1.8%): median 11.8%. Since 1926: corr -0.19; top fifth median 3.1%. US stocks only; VT is global (no global series checked) |
| **Equity-inflation correlation (JPM view)** | Long-run assumption near zero | JPM 2026: U.S. large cap vs inflation -0.01 (F-314) |
| **TIPS** | Not permitted (FAQ). JPM 2026 TIPS 4.30% compound vs intermediate Treasuries 4.00% | Payments are nominal, so a TIPS ladder would mismatch them anyway (`snap/main/research/assistant_review_2026-10/oct16/lenses/L03_strategy_redteam.md` STRAT-14; the "1.43x" figure there was on the STRIPS basis and should not be quoted) |

**Projections are nominal US$.** The case wants projections from $300k (2027) plus $150k (2028) with "reasonable return assumptions" (case:130-133) and assumptions on "the effect of inflation on portfolio projections and facility costs" (case:146-148). The JPM return inputs are nominal. Restating one or two key outputs in base-date dollars shows the inflation assumption at work.

---

## 6. Checklist: what the Final Report must state on inflation

The Final Report instructions come out on 9 Nov (case:162-163). Re-check this list against them then. Each item names what to state, not wording.

1. **The inflation assumption for projections:** one number, its index (US CPI, or PCE if stated), source and date (e.g. "JPM 2026 LTCMA, data as of 30 Sep 2025"), and why it is reasonable against at least one market and one survey anchor (section 1). If JPM 2027 is used, read its inflation line first; it is UNVERIFIED here.
2. **The base date for any "real" figure** (Jan 2027 or 2026), and that projections are nominal US$.
3. **Why the ladder is nominal:** the payments are fixed and "not adjusted for inflation" (case:90), so nominal Treasuries match them. TIPS are not permitted (FAQ, read 19 Oct). Inflation after purchase does not threaten the payments; falling yields (coupon reinvestment) are the nominal risk.
4. **What the payments buy:** one line or small table, e.g. the 2042 payment's buying power and the ten-payment total at the chosen rate. Say that extra operating support beyond Laura's commitment comes from others (case:85-86).
5. **A separate facility-cost assumption:** Taiwan construction costs (DGBAS CCI) with a chosen rate, its source and date, and why not CPI (CCI has run 1.1-2.3 points a year above Taiwan CPI). Say the team is not estimating the facility's cost (case:164-167).
6. **What the 2031 range buys by 2033:** the range stays in US$ (case:117). State the expected drift 2031→2033 at the chosen rate (about 4-7%) and the currency effect, with a dated NT$ illustration and who bears FX risk.
7. **The floor and range in real terms** (one line): e.g. the floor's 2033 value in base-date dollars, with the start date of the erosion named (5-year vs 6-year).
8. **One adverse inflation case** (e.g. 3.5% US, or the 2026 CCI pace for 2 years) and its effect on the payments' buying power and the facility money. Plus one favourable case (NT$ weaker, or lower Taiwan inflation).
9. **Which frame for Taiwan buying power:** US CPI, or Taiwan CPI with an FX assumption. History since 2000 shows no PPP drift (section 2). Pick one and say why.
10. **What, if anything, absorbs higher Taiwan costs** (the kept half, co-sponsors, re-scoping), sized honestly against section 4. Don't claim equities hedge inflation over 5 years without the section-5 caveat.
11. **IPS, by 6 Nov (no charts or citations):**
    - at most a principle: payments and range in US$; facility costs in Taiwan expected to rise; no currency hedge (derivatives and TIPS not permitted).
    - The live line "about 12% by 2033" must name its start year if kept.
12. **AI use:** any figure from this file used in a deliverable must be re-derived or re-checked by a student and recorded in the AI-use log and Works Cited.

---

## 7. What this teaches (plain English)
- **Nominal vs real.** A promise in fixed dollars is easy to fund exactly. Inflation then decides what those dollars buy, not whether they arrive. Keep the two questions apart.
- **Whose inflation?** Laura saves in US dollars but spends in Taiwan. Since 2000 Taiwan prices rose about half as fast as US prices, and the exchange rate did not adjust. The inflation that matters is the one where the money is spent, plus the exchange rate.
- **Drift vs spread.** Building costs are expected to rise (drift): state that as an assumption. The exchange rate can go either way (spread): show it as a range with a date.
- **Stocks are a long-run, not short-run, inflation shield.** Over five high-inflation years, US stocks' median real return was close to zero.

---

## 8. Open items and limits
- **UNVERIFIED:**
  - JPM 2027 LTCMA U.S. inflation figure (login wall).
  - The next DGBAS forecast date.
  - The history of the building-construction CCI group (only its Sep 2026 level was read).
  - Whether the FAQ's TIPS ban also covers WInS-listed TIPS ETFs (already on the batch-2 Wharton list, `oct19/out/Caplet_Update_19Oct2026.md:379`).
  - The size of the CPI-PCE gap.
- **Limits:**
  - Rolling windows overlap heavily (24-month windows since 2000 are about 13 independent periods; 76-month about 4).
  - CCI is a construction index, not a residency fit-out cost.
  - The PPP check is a statement about 1983-2026, not a forecast.
  - The DV01 check uses par yields as zero rates.
  - The stocks/inflation statistics are US-only (Shiller data, 2026 dividends missing).
- **Method note.** The Taiwan government sites (eng.stat.gov.tw, ws.dgbas.gov.tw) send an incomplete certificate chain. TLS verification was kept on. The missing TWCA intermediate was added and verified against the Mozilla-listed "TWCA CYBER Root CA" (from certifi, SHA-256 3F:63:BB:28...C5:58). The bundle is in `INF/certs/bundle_tw.pem` and the fetcher in `INF/scripts/tw.sh`. This is why the official DGBAS files, blocked in September, could be read this time.

## 9. Files
- Scripts:
  - `INF/scripts/us_now.py` (US CPI, breakevens, Cleveland, history)
  - `tw_load.py` (DGBAS/FRED loaders)
  - `tw_stats.py` (Taiwan CPI, CCI, FX, PPP, joint building power)
  - `model.py` (sections A-E)
  - `check2.py` (independent second pass)
  - `extras.py`
  - `stocks_inflation.py`
  - `tw.sh`, `txt.py`
- Outputs: `INF/data/us_now_out.txt`, `tw_stats_out.txt`, `model_out.txt`, `check2_out.txt`, `extras_out.txt`, `stocks_inflation_out.txt`.
- Raw: `INF/raw/*.csv` (FRED: CPIAUCNS, CPIAUCSL, CPILFESL, PCEPI, T5YIE, T10YIE, T5YIFR, DFII5-30, DGS5-30, EXPINF1-30YR, MICH, DEXTAUS); `par_202610.csv`, `real_2026.csv` (treasury.gov); `INF/raw/dl/{cpiidx,cpiidxc,cci,cciidx,cciidxc,cpi_sep2026}.xls` (DGBAS); `dgbas_236760/236587/236790.txt`, `cbc_sep2026.txt`, `cbc_fx.html`, `spf_q3_2026.txt`, `cleve.html`, `jpm_ltcma.txt`, `imf_pcpipch.json`, `imf_ind.json`, `faqs.txt`.
