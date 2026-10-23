# Taiwan residency: macro and FX groundwork (fact-checked, as of 2026-09-27)

**Access note (re-confirmed):** WebFetch is blocked by the egress proxy. In this session it failed on federalreserve.gov and eng.stat.gov.tw, and the original author reported the same for about 16 other sites. Every item marked **[snippet]** comes from a WebSearch summary, not from the page itself, so check it against the primary page before it goes into the IPS or Final Report. The FX figures come from a downloaded FRED mirror file, and I recomputed them in Python.

## 1. Taiwan CPI
- **Latest print [snippet]:** August 2026 CPI was +2.04% y/y, down from +2.54% in July, against a consensus of about 2.3%. It rose +0.13% m/m. (fx.co 3148980 and 3149025, rttnews 3689120; retrieved 2026-09-27.) **Conflict:** a separate search summary that cites CEIC gave "2.4% in August, 2.4% in July". Use 2.04%, which three snippets agree on, and confirm it on DGBAS. That site is blocked.
- **Official forecast [snippet]:** DGBAS forecast 2026 CPI at +2.07% and 2027 at +1.90% (Focus Taiwan, 2026-08-14). I did not re-check this independently, so it stays at snippet status.
- **History [snippet]:** 2024 about 2.2% and 2025 about 1.66%. 2022–23 are **UNVERIFIED**.
- The central bank's own 2026–27 CPI forecast is **UNVERIFIED**.

## 2. Construction costs (facility)
- **[snippet, re-verified]** The construction cost index (營造工程物價指數) rose +6.54% y/y in August 2026, the same as July and the highest since July 2022. Wages rose +8.12% y/y (a five-year high) and labour services rose +6.45% (the highest since April 2022). The article blames demand from new factory construction plus a tight labour supply. (udn / Economic Daily News, story 9744417, retrieved 2026-09-27)
- **[snippet]** The CEIC building sub-index was 112.23 in February 2026 (2021 = 100). I did not re-check this.
- The CENS "13.71%" figure is **UNVERIFIED — do not use.**
- **Takeaway (recomputed):** 6.54 / 2.04 = **3.2x** headline CPI. Do not inflate the facility cost at CPI.

## 3. USD/TWD (FRED DEXTAUS via datasets/exchange-rates mirror, daily through 2026-09-18). All figures recomputed and confirmed.

| Metric | Value |
|---|---|
| Latest in file (2026-09-18) | 31.82 TWD per USD |
| **[snippet]** spot on 2026-09-24 | 31.787 (not re-checked) |
| 10-year range | 27.52 (2022-01-04) to 33.21 (2025-04-01) |
| 10-year annualized change | +0.14%/yr (31.37 → 31.82) |
| Annualized volatility, daily log returns | 10y 4.7%; 5y 5.2%; 3y 5.6%; 1y 4.0% |
| Annualized volatility, monthly, 10y | 4.4% |
| Largest 7-year log moves since 1990 | −16.1% (TWD stronger, window ending 2011-08) / +31.5% (TWD weaker, window 1995-04 to 2002-04, which includes 1997) |

Illustration only, not a forecast. All figures recomputed and confirmed:
- One $50k payment is worth NT$1.591M.
- If the TWD strengthens by the historical maximum (to 27.09), those same NT$ cost **$58.7k**.
- If the TWD weakens by the historical maximum (to 43.59), they cost **$36.5k**.
- A one-standard-deviation move over 6.25 years (4.7% × √6.25 = 11.75%) gives a range of **$44.5k–$56.2k**.

The claim that the TWD is a managed float with central bank intervention is **UNVERIFIED**.

## 4. Taiwan vs US rates
- **Taiwan [snippet, re-verified]:** the central bank held the discount rate at **2.00%** in September 2026, its tenth straight quarterly hold. It also eased mortgage rules, raising the loan-to-value cap on second homes from 60% to 70%. (RetailNews Asia, OCAC, fx.co 3171184; retrieved 2026-09-27.) The Q2 release gives secured refinancing at 2.375% and temporary accommodation at 4.25% [snippet, not re-checked].
- **US [snippet, re-verified]:** on 2026-09-16 the FOMC voted 12–0 to raise the target range 25bp to **3.75%–4.00%**, its first hike since 2023. The dot plot puts year-end projections at 4.1–4.4%. (Raisin, CNBC, Advisor Perspectives, Fed implementation note monetary20260916a1; retrieved 2026-09-27.) The Fed page itself is blocked.
- **Taiwan 10-year [snippet]:** about 1.70% as of 2026-07-14. A September figure is **UNVERIFIED**.
- **US 10-year [snippet, re-verified]:** closed at **5.17%** on 2026-09-25, having hit its highest level since June 2007 on 2026-09-24. (Advisor Perspectives, CNBC 2026/09/25; retrieved 2026-09-27.) Still confirm it on H.15 / FRED DGS10, which is blocked.
- **Differentials (recomputed):**
  - Policy rates: 3.75–4.00 minus 2.00 gives **175–200bp**. Caveat: the Fed funds target and the Taiwan discount rate are different instruments.
  - 10-year yields: 5.17 − 1.70 = **347bp**. Caveat: this mixes a July Taiwan figure with a September US figure.
- The direction under interest-rate parity is correct: the USD trades at a forward discount, so hedging USD assets into TWD gives up roughly the differential each year. The exact forward points are **UNVERIFIED**.

## 5. Risks for the IPS and Final Report (unchanged in substance)
1. **Currency mismatch.** Laura's $50k obligation is fixed in USD, but the residency's costs are in TWD. Local prices rising about 2% a year, plus any TWD strengthening, would erode what each payment buys. This is a residency-side risk that co-sponsors should understand.
2. **The facility contribution is exposed to both FX and construction costs.** Building costs are rising about 6.5% y/y. With 5% annual FX volatility, one standard deviation over 6 years is about ±12% (recomputed: 12.2%). Give co-sponsors the range in USD, with its TWD equivalent under strong-TWD and weak-TWD cases.
3. **Hedging costs money** at current differentials of roughly 175–200bp or more a year. Explain why the team did not hedge. Partial hedging, or holding TWD cash close to 2033, are alternatives.
4. **Inflation assumptions.** Use a 2% CPI baseline and a separate, higher stress case for construction costs. No long-run construction-cost forecast was found (**UNVERIFIED**).
5. **Tail risk.** The +31.5% 7-year swing through 1997 shows why scenario analysis is needed, not just the volatility figure.

Data files: `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/groundwork/fx_daily.csv` and `fx_monthly.csv`.

## Verification notes
- **FX:** I recomputed every figure in section 3 from the CSVs (latest rate, range and dates, CAGR, 10/5/3/1-year volatility, monthly volatility, 7-year extremes, and the $58.7k / $36.5k / $44.5k–$56.2k illustrations). All matched. I added the start date of the +31.5% window (1995-04).
- **Arithmetic:** I recomputed the CPI multiple (3.2x), the rate differentials (175–200bp and 347bp) and 5% × √6 (12.2%). All are correct. I added caveats about mismatched instruments and dates.
- **Re-searched independently:**
  - August CPI 2.04%: confirmed by three snippets. One CEIC summary conflicts at 2.4%; this is flagged above.
  - Fed hike to 3.75–4.00%: confirmed, and I added the 12–0 vote and the dot plot.
  - US 10-year at 5.17%: confirmed, and I added "highest since June 2007".
  - Central bank hold at 2.00%: confirmed, and I added the tenth straight hold and the loan-to-value change.
  - Construction index +6.54%, wages +8.12%, labour services +6.45%: confirmed.
- **Not re-checked, still snippet-only:** the DGBAS forecasts, CPI history, the CEIC sub-index, the Taiwan 10-year yield, the 09-24 spot rate, and the Q2 central bank rates.
- **Blocked this session:** federalreserve.gov, eng.stat.gov.tw.

## Sources (all retrieved 2026-09-27)
- FX data: https://raw.githubusercontent.com/datasets/exchange-rates/main/data/daily.csv and https://raw.githubusercontent.com/datasets/exchange-rates/main/data/monthly.csv (FRED DEXTAUS)
- https://www.fx.co/en/forex-news/3148980, https://www.fx.co/en/forex-news/3149025, https://www.rttnews.com/story.aspx?Id=3689120 [snippet]
- https://www.ceicdata.com/en/indicator/taiwan/consumer-price-index-cpi-growth [snippet, conflicting 2.4%]
- https://focustaiwan.tw/business/202608140022 [snippet, 2026-08-14]
- https://money.udn.com/money/story/10869/9744417 and https://udn.com/news/story/7238/9744417 [snippet]
- https://www.ceicdata.com/en/taiwan/construction-cost-index-2021100/construction-cost-index-building-construction-bc [snippet]
- https://www.theglobaleconomy.com/Taiwan/inflation_annual/ and https://www.focus-economics.com/country-indicator/taiwan/inflation/ [snippet]
- https://retailnews.asia/taiwan-holds-rates-at-2-percent-and-eases-property-curbs, https://www.ocac.gov.tw/OCAC/Eng/Pages/Detail.aspx?nodeid=329&pid=82177973, https://www.fx.co/en/forex-news/3171184 [snippet]
- https://www.cbc.gov.tw/en/cp-448-192435-024f3-2.html [snippet]
- https://www.raisin.com/en-us/news/fed-rate-decision-policy-breakdown-september-2026/, https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html, https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a1.htm [snippet]
- https://www.advisorperspectives.com/dshort/updates/2026/09/25/treasury-yields-snapshot-september-25-2026, https://www.cnbc.com/2026/09/25/treasury-yields-bonds-debt.html [snippet]
- https://tradingeconomics.com/taiwan/government-bond-yield/news/551144, https://en.macromicro.me/series/758/10year-bond-yield-taiwan [snippet]
- https://tradingeconomics.com/taiwan/currency [snippet]