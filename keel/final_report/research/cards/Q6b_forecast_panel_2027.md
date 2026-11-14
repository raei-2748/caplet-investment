# Q6b. Is 7.5% a year for world shares still at the top of the published range, read at the source?

Day 8 card, Sun 15 Nov 2026 (Sydney). Sources read 14-15 Nov 2026 (Sydney). Builds on `Q6_how_far_to_trust_7_5.md`
(Mon 9 Nov) and repeats none of its rows except to correct or upgrade them (rows 12, 26, 31 below). Notes for the store,
not report prose. Figures for the plan come from `NUMBERS.md` (section cited); everything else is a house's own figure,
Keel arithmetic or Keel inference, labelled as such.

**Claims tested**
1. KEEP (verify): J.P. Morgan's 2027 Long-Term Capital Market Assumptions, released about 19-20 Oct 2026, give 7.5% a
   year compound for world (ACWI) shares in USD over 10-15 years, with about 17.9% volatility.
2. KILL or CHANGE: the other houses put world shares lower, so 7.5% is the top of the published range.
3. KEEP or KILL: house forecasts have little skill at 3-5 years, the plan's horizons (VT bought Jan 2028; half moved
   before the 2031 meetings, about three years held; half kept to 2033, about five).

**Class of problem and who solved it first.** Trusting a point forecast drawn from a panel of experts who work on
different bases (compound or arithmetic, real or nominal, local currency or USD, 5, 7 or 10 years). Weather forecasting
solved it first by grading forecasts against outcomes (forecast verification, Brier 1950). Econometrics added forecast
combination (Bates and Granger 1969): put every forecast on one basis and set any one member against the panel. Both
are named from Keel's prior knowledge as prior art. They were not read this run (UNVERIFIED as reads). This card applies the first
two steps: one basis, then each forecast against what happened.

**Verdicts in one screen**
1. **KEEP, verified at the source.** J.P. Morgan 2027 LTCMA USD matrix, "as of September 30, 2026": row "AC World
   Equity 7.50 8.94 17.88 7.00" = 7.50% compound, 8.94% arithmetic, 17.88% annualised volatility, 7.00% the 2026
   compound; "All returns are nominal"; horizon 10-15 years. Press release New York 19 Oct 2026 (20 Oct Sydney): "Global
   equities are projected to return 7.5% (USD), increasing from 7.0%". Two limits to carry: MSCI ACWI is large and mid
   cap while VT holds all caps; the figure is before VT's 0.06% fee (NUMBERS section 0) (rows 1-3).
2. **KILL "the top"; CHANGE to "the upper third".** Fifteen world-share figures, dated Sep 2025 to Nov 2026 and put on
   one basis (nominal, compound where the house says so, Keel arithmetic for blends at 62% US / 28% other developed /
   10% emerging), run from about -2.5% (GMO, from real) to 9.0% (BlackRock, 10 years). Median 6.5%. Four sit above J.P.
   Morgan: BlackRock 9.0, Robeco 7.85 (5 years), HSBC 7.81, BNY about 7.7. Aon ties at 7.5. Of the twelve figures
   dated Jun-Oct 2026, the median is 6.35 and J.P. Morgan ties for fourth. Correction: Northern Trust's 2026 edition says
   6.9 for MSCI ACWI, not 7.1, which was its 2025 edition (Q6 row 5) (rows 6-22).
3. **KEEP, now with numbers.**
   - Robeco graded nine overlapping five-year windows (2012-16 to 2020-24). It under-forecast developed-market shares in
     all nine, by 6.8 points a year on average (range 2.4 to 10.3). Forecast and outcome correlate at 0.05 (Keel arithmetic).
   - Ma et al. (2024): at 5 years the best-known valuation models have out-of-sample R squared of 1.54% and mean
     absolute error of 6.3 points a year (10 years: 9.16% and 4.0 points).
   - Northern Trust's own 2020 five-year forecast for US shares was 4.7%; the outcome was 15.9%.
   - J.P. Morgan's 5.0% of Sep 2021 met an ACWI return of 11.57% a year over the next five years.
   - Value Line's 3-5-year stock projections had "no predictive power".
   - One counterpoint: Lioui and Poncet (2019) find some value up to 4 years.
   (rows 4-5, 23-30)

**What it means for the plan's notes (Keel inference).**
- NUMBERS section 4 already runs 4% to 10%. The stated top is $115,000 in every column, and the top before rounding
  moves $116,580 to $119,851. The half kept moves $18,091 to $23,948.
- So the house chosen moves the half kept, never the stated top.
- The panel's low end (GMO, Ninety One) sits below the 4% the register tested (row 31).
- The disagreement among houses is small next to each house's own band: BlackRock's five-year middle half alone spans
  3.3% to 15.6%. It is smaller still next to five-year misses of 6-10 points (rows 7, 23, 33).

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | J.P. Morgan 2027 LTCMA: world shares (MSCI ACWI) 7.50% a year compound, 8.94% arithmetic, 17.88% volatility, nominal USD, 10-15 years, estimates as of 30 Sep 2026; the 2026 edition said 7.00% | J.P. Morgan Asset Management (2026a, matrix); J.P. Morgan Asset Management (2026b, press release 19 Oct 2026); J.P. Morgan Asset Management (2026c, report: "pushing our global equity forecast (ACWI) up by 50bps, to 7.5%") | CEILING, HALFKEPT, MOVE2031 | KNOWN | The plan's one borrowed input is quoted correctly in NUMBERS section 0 and CANON B15: compound column, USD, nominal | Horizon 10-15 years; the plan holds VT about 3 and about 5 years. The report says it builds "modestly higher volatility forecasts" for prevailing risks. Released 19 Oct New York = 20 Oct Sydney | VERIFIED (matrix and press release read in full; report in part) | no (IPS names no rate; TNA l.23 cites J.P. Morgan correctly) | Matrix PDF and press release at am.jpmorgan.com, read 14 Nov 2026; FA Mag 20 Oct 2026 confirms the higher equity volatility |
| 2 | J.P. Morgan says its figures are "not promises or even estimates of actual returns a client portfolio may achieve"; its method takes analysts' input "at the start of our forecast horizon, which aligns with our analysts' typical three- to five-year forecast horizon" | J.P. Morgan Asset Management (2026a, matrix footnote); J.P. Morgan Asset Management (2024, methodology handbook) | PRESENTATION, PROCESS | KNOWN | Supports calling 7.5% an assumption to test, never a forecast Laura can rely on; the house itself splits its years into a 3-5-year start and a long-run equilibrium | The 3-5-year input is about the path in, not a 3-5-year return figure; J.P. Morgan publishes no 3- or 5-year world-share number | VERIFIED (matrix quote read in full); handbook read in part | risk: TNA l.23 says "a forecast return", firmer than the house's own words | Matrix PDF footnote; LTCMA methodology handbook (2025 edition), read in part 14 Nov 2026 |
| 3 | Two basis gaps between the 7.5% and VT: MSCI ACWI is large and mid cap, VT tracks FTSE Global All Cap (small caps too); 7.5% is before VT's 0.06% fee | J.P. Morgan Asset Management (2026a); Northern Trust Asset Management (2026, glossary: ACWI "includes large- and mid-cap companies"); NUMBERS section 0 (VT fee 0.06%) | CEILING, HALFKEPT | TEXTBOOK | Net of the fee, Keel arithmetic puts the like-for-like figure at about 7.44%; Northern Trust's ACWI and ACWI IMI (all-cap) forecasts are identical at 6.9, so the cap gap looks small | Small-cap premium forecasts differ by house; no house read here gives FTSE Global All Cap itself | VERIFIED (the two index definitions and the fee); the size of the cap effect is Keel inference | no | Northern Trust 2026 report, detailed table and glossary; NUMBERS section 0 |
| 4 | J.P. Morgan's own world-share figure moves a lot from year to year: 5.0% (2022 edition, Sep 2021), 8.5% (2023), 7.8% (2024), 7.1% (2025), 7.0% (2026), 7.5% (2027) | J.P. Morgan (2021 press release, "pull our estimate of global equity returns down 10bps, to 5.00% in USD terms"); J.P. Morgan Asset Management (2022, 2023 editions, mirrors); J.P. Morgan Asset Management (2024, handbook: ACWI 7.10 compound, 8.37 arithmetic, 16.71 volatility); 2026a | CEILING, PROCESS | NICHE | One house moved 3.5 points in a single year (2022 to 2023 edition, after the 2022 fall). That is more than the gap between 7.5% and the panel median. The figure tracks starting prices, not a stable truth | Moves after big price changes are the method working (lower prices, higher expected returns), not error; a 10-15-year figure should move with starting valuations | Read in part (2021 release at PR Newswire and Stockhouse; 2023 and 2024 reports on third-party mirrors, so UNVERIFIED as J.P. Morgan-hosted copies) | no | PR Newswire 8 Nov 2021; JPMAM 2023 report mirror (argaamplus); 2024 report mirror (storyblok); handbook |
| 5 | J.P. Morgan's forecasts against what ACWI then did: 5.0% (Sep 2021) against 11.57% a year over the next 5 years (miss +6.6 points a year); 7.8% (Sep 2023) against 21.73% a year over the next 3 years (miss +13.9) | J.P. Morgan (2021 release; 2024 report mirror); Aon (2026, quarterly review for the University of Washington: MSCI ACWI to 30 Sep 2026, 1y 16.75, 3y 21.73, 5y 11.57, 10y 12.38) | MOVE2031, HALFKEPT, CEILING | NICHE | At the plan's own horizons (about 3 and about 5 years) the one house the plan cites missed by 7 to 14 points a year, upward. The FR should show 7.5% as the middle of a wide band, which Table 2 already does by market world | Two windows, both in a strong market; a 10-15-year figure is not meant for 3-5 years (J.P. Morgan says so); realised figures from a secondary source, not MSCI's own sheet | Forecasts VERIFIED; realised ACWI read at a secondary source (Aon review), MSCI factsheet not read; misses are Keel arithmetic | no | Aon QIR 3Q26 PDF on hr.uw.edu, read 14 Nov 2026 |
| 6 | BlackRock (Aug 2026, data 30 Jun 2026, USD, starting-point scenario): MSCI ACWI 9.26% a year over 5 years, 9.15% over 7, 9.02% over 10, 8.91% over 15; volatility 18.38%; "All component numbers are geometric" | BlackRock Investment Institute (2026a, workbook; 2026b, web page dated 11 Aug 2026, "updated quarterly") | CEILING, HALFKEPT | KNOWN | Kills claim 2 by itself: the largest asset manager's 10-year figure is 1.5 points above J.P. Morgan's. BlackRock also prints a 5-year figure, the only big house to do so for ACWI | Data are three months older than J.P. Morgan's (30 Jun against 30 Sep 2026); BlackRock's Q3 update was not found | VERIFIED (workbook parsed in full; web page read in part) | no | BlackRock CMA workbook (xlsx, parsed via Firecrawl, cached 13 Nov 2026) and CMA page, read 14 Nov 2026 |
| 7 | BlackRock prints its own uncertainty: the middle half of outcomes for ACWI's mean return runs 3.33% to 15.55% over 5 years, 4.50% to 13.75% over 10 years; its scenarios run from 3.96% (5y, "global risk premia rise") to 14.19% (5y, "AI productivity boom") | BlackRock Investment Institute (2026a, columns for the 25th and 75th percentiles of the mean; 2026b, method: "uncertainty as the range of outcomes for the mean") | MOVE2031, HALFKEPT, CEILING, PRESENTATION | NICHE | One house's own middle half (12 points at 5 years) is three times the spread among the central figures of every other house except GMO and Ninety One (5.0 to 9.0, 4 points). The case for a rule that sets the top from the market, not from the forecast | It is uncertainty about the mean, not the spread of yearly returns; the two can be confused by a reader | VERIFIED | no | BlackRock workbook, same rows as row 6 |
| 8 | HSBC Asset Management (Oct 2026, data Sep 2026, 10 years): MSCI ACWI 7.81% USD unhedged, 7.25% local, 7.55% USD hedged; MSCI World 7.46 USD; MSCI USA 6.95; EM 10.45 | HSBC Asset Management (2026) | CEILING | NICHE | A second Oct 2026 house above J.P. Morgan; currency matters: in local terms HSBC's 7.25 sits below 7.5 | Compound or arithmetic not stated in the part read | Read in part; the basis is UNVERIFIED | no | HSBC AM CMA October 2026 PDF (mena.assetmanagement.hsbc.com), read 14 Nov 2026 |
| 9 | Robeco Expected Returns 2027-2031 ("The Great Rewiring", 16th edition, 22 Sep 2026): developed-market shares 7.75% a year in USD (7.00 EUR), emerging 8.75% USD, five years, geometric; bull 11.5%, bear -1% (developed) | Robeco (2026a, summary); Robeco (2025, previous edition: developed 6.75% USD) | MOVE2031, HALFKEPT, CEILING | KNOWN | The one house publishing a five-year figure close to the plan's horizons; at 90/10 developed and emerging it gives about 7.85% (Keel arithmetic), above J.P. Morgan | Scenario odds (base 50, bull 15, bear 35) are from secondary sources; one secondary source gives the developed bear case as -0.25% in EUR, Robeco's own summary says -1% (currency of the bull and bear cases not stated in the part read) | Figures VERIFIED (summary read in full); scenario odds UNVERIFIED (HF Best Ideas, Gate); bear-case currency UNVERIFIED | no | Robeco summary PDF; robeco.com press page 22 Sep 2026 |
| 10 | BNY Investments 2026 CMAs (28 Jan 2026, 10 years): US 7.6%, developed ex-US 7.8%, emerging 8.1%; world blend about 7.7% (Keel arithmetic) | BNY Investments (2026) | CEILING | NICHE | A third house above J.P. Morgan, though an older edition | Compound or arithmetic not stated in the part read; dated Jan 2026, so not a 2027 edition | Read in part; basis UNVERIFIED | no | bny.com wealth insights page, read 14 Nov 2026 |
| 11 | Aon (Q3 2026, as of 30 Jun 2026): global equity (IMI) 7.5% a year nominal, 5.1% real, 16.1% volatility, 10 years, geometric (30 years 7.4%); Aon says its assumptions "tend to be middle of the pack in the Horizon Survey" | Aon (2026a, Florida Retirement System conference papers, 14 Oct 2026); Aon (2026b, Nebraska Investment Council, Aug 2026) | CEILING, PRESENTATION | KNOWN | Ties J.P. Morgan at 7.5% and is all-cap (IMI), so closer to VT's index. A consultant calls 7.5% "middle of the pack", a fair counterweight to "upper third" | "Middle of the pack" is Aon describing itself, on the Horizon survey, which was not read here | VERIFIED (both PDFs read in part) | no | edr.state.fl.us and nic.nebraska.gov PDFs, read 14 Nov 2026 |
| 12 | Correction to Q6 row 5: Northern Trust's 2026 edition (as of 30 Sep 2025) puts MSCI ACWI at 6.9% a year over 10 years, geometric (ACWI IMI also 6.9); 7.1% was its 2025 edition; history 4.9, 4.6, 6.1, 6.3, 7.1, 6.9 (2021 to 2026 editions) | Northern Trust Asset Management (2026, detailed long-term forecasts table) | CEILING, PROCESS | KNOWN | Panel row moves down 0.2; the panel median is unchanged at 6.5 | The sentence Q6 row 5 quotes ("7.1% for global equities") was not found in the 2026 report in this run; the table rules. Forecast currency not stated beside the table (actual returns are local currency) | VERIFIED (table read twice, 14 Nov 2026) | no | NT 2026 CMA report PDF (ntam.northerntrust.com), detailed table |
| 13 | AQR 2026 (as of 31 Dec 2025, horizon "5 to 10" years): global shares 4.2% a year real, local currency; about 6.5-6.7% nominal at 2.4% US inflation (Keel arithmetic); "a 50% chance" the realised return misses by more than 3% a year | AQR Capital Management (2026) | CEILING, MOVE2031, HALFKEPT | KNOWN | Prices its own error: half the time off by more than 3 points a year, larger than the whole gap from the panel median to J.P. Morgan | Real and local; the conversion is Keel's, not AQR's | VERIFIED (PDF read in part) | no | AQR Alternative Thinking 2026 PDF, read 14 Nov 2026 |
| 14 | Invesco (Q3 2026 USD, estimates as of 30 Jun 2026, 10 years): MSCI ACWI 6.4% geometric; MSCI World 5.9% geometric against 7.2% arithmetic, volatility 16.5% | Invesco (2026) | CEILING, PRESENTATION | KNOWN | Shows on one page the 1.3-point gap between compound and arithmetic for the same index; J.P. Morgan's own gap is 1.44 (7.50 against 8.94) | Prior card Q6 row 6 holds the ACWI figure; this row adds the basis lesson | VERIFIED (read in part) | no | Invesco CMA USD PDF, read 14 Nov 2026 |
| 15 | PGIM (Nov 2026, as of 30 Sep 2026, 10 years, geometric, USD, before fees): US large cap 6.0% (down 0.5), international ex-US 6.8% (down 0.4), emerging 7.0% (down 0.9); world blend about 6.3% (Keel arithmetic) | PGIM (2026) | CEILING | NICHE | A same-quarter house moved down while J.P. Morgan moved up 0.5; the direction of revision is not shared | Blend weights are Keel's | VERIFIED (read in part) | no | pgim.com CMA page, read 14 Nov 2026 |
| 16 | Vanguard (model run of 30 Sep 2026, page 21 Oct 2026, 10 years): US shares 4.8-6.8% (median 5.8%; 5th-95th -2.7% to 14.7%), global ex-US 5.0-7.0% (median 6.0%); world about 5.9% (Keel arithmetic); "valuations tend to be poor predictors of performance over the short or even intermediate term" | Vanguard (2026a, return forecasts page and chart table); Vanguard (2026b, FAVEMOBF, 30 Oct 2026) | CEILING, MOVE2031, HALFKEPT, PRESENTATION | KNOWN | The world's largest index-fund house sits 1.6 points below J.P. Morgan, and says its own figures do not hold at short horizons; VT is a Vanguard fund | Vanguard's 2027 outlook (expected Dec 2026) not yet out; the 30 Sep run is the latest | VERIFIED (page via mirror and chart table; FAVEMOBF confirms) | no | corporate.vanguard.com VEMO return forecasts and dwcharts table; advisors.vanguard.com FAVEMOBF.pdf |
| 17 | State Street (Q4 2026, as of Sep 2026): MSCI ACWI 6.70% (1 year), 6.90% (3-5 years), 6.80% (10+ years), all ARITHMETIC; standard deviation 14.80%; compound equivalent about 5.7-5.8% (Keel arithmetic, arithmetic minus half the variance) | State Street Global Advisors (2026) | CEILING, PRESENTATION, PROCESS | NICHE | The trap in any panel: a reader comparing State Street's 6.9 with J.P. Morgan's 7.5 sees 0.6 points; on one basis the gap is about 1.7. State Street also publishes a 3-5-year world figure (6.90 arithmetic), close to the plan's horizons | The conversion assumes State Street's own volatility; State Street's long-horizon risk figure (4.70%) is a different measure | VERIFIED (page read in full); compound conversion is Keel arithmetic | no | ssga.com long-term asset class forecasts Q4 2026 page, read 14 Nov 2026 |
| 18 | Research Affiliates is now Syzygy Asset Management (renamed Aug-Sep 2026); its asset-allocation tool, as of 31 Oct 2026, 10 years, nominal USD: US large 3.5%, developed ex-US large 8.1%, emerging 7.1%, global 100/0 reference 5.0%; world blend about 5.1% (Keel arithmetic) | Syzygy Asset Management (2026a, asset allocation interactive); Syzygy Asset Management (2026b, relaunch press release 10 Sep 2026); SEC filing 497 of 18 Aug 2026 (name change) | CEILING, PRESENTATION | NICHE | A reference-list trap: cite the tool under its new name, with the old in brackets. Its US figure (3.5%) is the lowest of any house that still expects positive nominal returns | Valuation-led model; geometric basis not stated in the part read | VERIFIED (tool rendered and read; rename read at source); basis UNVERIFIED | no | interactive.researchaffiliates.com (redirects to interactive.syzygyassetmanagement.com), rendered via Firecrawl 14 Nov 2026 |
| 19 | Ninety One (Oct 2026, as at 30 Sep 2026, 10 years, nominal local currency): global shares 2.2%, US 1.7%; it recalls its Oct 2021 forecasts of 2.2% (US) and 2.8% (global) | Ninety One (2026) | CEILING, MOVE2031 | NICHE | A second house far below 4%, the floor of the register's test; its 2021 global forecast of 2.8% met an ACWI return of 11.57% a year over the next five years (Keel arithmetic; currency bases differ) | Local currency, not USD; a valuation-heavy house | VERIFIED (read in part) | no | ninetyone.com CMA October 2026 PDF (published 3 Nov, updated 11 Nov 2026) |
| 20 | GMO 7-year real forecasts (as of 30 Sep 2026, published 16 Oct 2026): US large -7.3%, international large -0.9%, emerging 0.2% a year real; world blend -4.8% real, about -2.5% nominal at 2.4% inflation; on GMO's low-rates set about +0.3% nominal (Keel arithmetic) | GMO (2026) | CEILING, MOVE2031, HALFKEPT | KNOWN | The bottom of the panel; the gap from GMO to BlackRock is about 11.5 points a year among houses publishing in the same quarter | Real, 7 years, a mean-reversion house with a long record of being early; the blend and conversion are Keel's | VERIFIED (PDF read in full) | no | gmo.com 7-year forecast PDF, Sep 2026 |
| 21 | Houses not read at the source this run: EFG 2027 (as at 9 Nov 2026, 10 years, US 6.6% hedged, down from 7.3%; global row not extracted); American Century (3 Nov 2026, 3-5 years, US large cap 7.00% arithmetic); Schwab 2026 (US large 5.9, developed 7.0, emerging 6.8); Callan 2026 (US 7.3, developed 7.6, emerging 8.2); Capital Group 6.0 (20 years) and Janus Henderson 6.2 (prior Q6 row 7) | EFG International (2026); American Century Investments (2026); Schwab (2026); PortfolioLab (n.d.) for Callan | CEILING | NICHE | None changes the ranking much: Callan's blend (about 7.5, Keel arithmetic) would tie J.P. Morgan; the rest sit below it | Mixed bases and dates; Callan only at a secondary aggregator | EFG, American Century and Schwab read in part; Callan UNVERIFIED (secondary only) | no | efginternational.com PDF; americancentury.com; schwab.com; portfoliolab.app |
| 22 | The panel on one basis: GMO -2.5, Ninety One 2.2, Syzygy 5.0, State Street 5.7, Vanguard 5.9, PGIM 6.3, Invesco 6.4, AQR 6.5, Northern Trust 6.9, Aon 7.5, J.P. Morgan 7.5, BNY 7.7, HSBC 7.8, Robeco 7.85, BlackRock 9.0; median 6.5; J.P. Morgan tied fifth of fifteen; the twelve dated Jun-Oct 2026 have median 6.35, J.P. Morgan tied fourth | Rows 1, 6, 8-20 | CEILING, PRESENTATION, PROCESS | NICHE | Claim 2 dies: 7.5% is upper third, not top. It also cuts the other way: 7.5% is not an outlier, since two big consultants (Aon, Callan) sit at or near it | Horizons differ (5, 7, 10, 10-15 years) and so do currencies; the ranking is approximate, as every blend is Keel arithmetic | Inputs VERIFIED as each row says; ranking and median are Keel arithmetic | risk: TNA l.23 cites one house without the range; not a clash, a gap to fill in 3e | This card |
| 23 | Robeco graded its own five-year forecasts: developed-market shares were under-forecast in all nine windows from 2012-16 to 2020-24 (e.g. 3.25% forecast against 13.52% realised for 2020-24); mean miss 6.8 points a year, range 2.4 to 10.3; forecast and outcome correlate at 0.05; emerging 2020-24 was 3.75 against 3.77 | Robeco (2025, chapter 6, EUR, geometric: "we severely underestimated the returns of developed markets equities") | MOVE2031, HALFKEPT, CEILING | NICHE | The best evidence at the plan's own five-year horizon: a house's five-year figure for developed shares carried almost no information about the outcome. Robeco's own lesson: "it is more important to correctly predict the direction and the relative returns of asset classes than their absolute returns" | Overlapping windows (nine windows, fewer than two independent five-year periods); EUR, not USD; a bull decade, so the miss is one-signed. Robeco reports its tactical tilts added 36bp a year (information ratio 0.17) | VERIFIED (chapter read); the mean miss and correlation are Keel arithmetic | no | robeco.com 2026-2030 report PDF ("The Stale Renaissance"), chapter 6 |
| 24 | Northern Trust graded its 2020 five-year forecasts (Sep 2020 to Sep 2025, local currency): US shares 4.7% forecast against 15.9% realised; emerging 5.4% against 9.8%; developed 4.8% against 15.1% (chart labels); risk-asset portfolio 5.1% against 13.4%; "Little did we suspect the huge optimism fueling the AI boom" | Northern Trust Asset Management (2026, "How Have We Done?", Exhibit 15) | MOVE2031, HALFKEPT | NICHE | A second house's five-year check, same direction and size as Robeco's: shares beat the forecast by 4 to 11 points a year. Its bond forecasts were too high in the same window (rates rose in 2022) | The developed-market pairing is read from chart labels (Keel reading); the US and emerging figures are in the text | VERIFIED (text); developed pairing Keel reading of the chart | no | NT 2026 CMA report PDF, section 9 |
| 25 | Ma, Marshall, Nguyen and Visaltanachoti (2024): across long-term expected-return models, predictability is "strongest for 20-year horizons, followed by 10-year horizons, and weakest for 5-year horizons"; at 5 years mean absolute error 6.29 points a year and out-of-sample R squared 1.54%, against 3.95 and 9.16% at 10 years | Ma et al. (2024), Financial Analysts Journal | MOVE2031, HALFKEPT, PROCESS | KNOWN | A peer-reviewed answer to claim 3: at five years, a valuation-based estimate explains about 1.5% of what happens, and misses by about 6 points a year on average | Models, not house forecasts; US data; the best 10-year model (TRCAPE) reaches 30.51%, so the long horizon is not hopeless | VERIFIED (paper read in part) | no | tandfonline.com, DOI 10.1080/0015198X.2024.2358737 |
| 26 | Boudoukh, Israel and Richardson (2019): with 50 years of data and 5-year overlapping windows the effective number of observations rises only "from 10 to just 12", and t-statistics are "effectively double their 'true' value"; upgrades Q6 row 24's citation from UNVERIFIED | Boudoukh, Israel and Richardson (2019), Financial Analysts Journal | PROCESS, PRESENTATION | KNOWN | Why no study can settle 3-5-year skill with confidence: there are too few independent windows. That also limits rows 23-24 | Abstract only | VERIFIED (abstract read) | no | tandfonline.com, DOI 10.1080/0015198X.2018.1547056 |
| 27 | Welch and Goyal at five-yearly frequency: dividend yield in-sample R squared 5.54 but out-of-sample worse than the plain average (RMSE change -2.62); earnings yield -0.54; only the term spread and consumption-wealth ratio beat the average out of sample | Welch and Goyal (working paper, section "5 Five-Yearly Frequencies") | PROCESS | KNOWN | The classic predictors, given five-year windows, lose to the historical mean; adds a third line of evidence to rows 23 and 25 | Working paper version; US index; older sample | VERIFIED (section read in part) | no | repec.som.yale.edu working paper PDF 2412 |
| 28 | Szakmary, Conover and Lancaster (2008): Value Line's 3-5-year stock return projections were "extremely overoptimistic and have no predictive power", averaging 20.3% a year, about twice what the stocks returned (1969-2001, Dow stocks) | Szakmary, Conover and Lancaster (2008), Journal of Banking and Finance | PROCESS | NICHE | The one long record of published 3-5-year return projections, graded: biased up and uninformative | Single stocks, not an index; an analyst service, not a house CMA | VERIFIED (abstract and conclusion read; authors now identified, so the Q6b brief's open citation is closed) | no | sciencedirect.com; scholarship.richmond.edu post-print record |
| 29 | Counterpoint: Lioui and Poncet (2019) find out-of-sample gains for an investor using predictors at horizons up to about 4 years | Lioui and Poncet (2019), European Journal of Operational Research | PROCESS | NICHE | Keeps the card honest: "little skill" is not "no skill"; the gains are about tilting, not about the level of the return | Abstract only; a utility test, not a forecast-error test | Read in part (abstract) | no | sciencedirect.com S0377221719303777 |
| 30 | Across firms at 10 years (Dimensional): forecasts for 2014-2023 missed by "a little over 4" points a year on average and "no firm's forecasts stood above the rest as consistently more accurate" | Wicker (2024), Dimensional (prior Q6 row 13) | PROCESS, PRESENTATION | KNOWN | Choosing the "best" house is not possible from the record, which is why the plan picks one cited figure and tests 4-10% around it | Prior; 10-year, not 3-5 | VERIFIED in Q6 (not re-read) | no | dimensional.com insight page |
| 31 | Plan link: NUMBERS section 4 runs VT at 4%, 6%, 7.5%, 9% and 10% a year. The stated top is $115,000 in every column, the top before rounding $116,580 to $119,851, and the half kept $18,091 to $23,948. So the house chosen moves the half kept by about $5,900, never the stated top. Q6 row 27's $3,784 predates this register | NUMBERS section 4 ("The return assumption barely moves the gift"); Q6 row 27 | CEILING, HALFKEPT, MOVE2031 | NICHE | The forecast panel matters for Laura's flexibility money, not for what she tells co-sponsors; that is the right way round for the IPS's promise (IPS l.15: markets may move the top, the bottom stays) | The register stops at 4%; GMO (about -2.5%) and Ninety One (2.2%) sit below it, so the low end of the published panel is untested in NUMBERS | VERIFIED against NUMBERS section 4 (read 15 Nov); the reading is Keel inference | no (IPS l.15 lets the top rise or fall) | NUMBERS.md lines 299-310 |
| 32 | Wording: TNA l.23's "a forecast return of about 7.5% a year (as per JPMorgan)" is accurate as a citation (CANON B15, TRUE with limits) but reads as a consensus forecast; J.P. Morgan calls it an assumption, not an estimate of what a client will earn, and it is upper third of the panel | TNA l.23; CANON B15; rows 2 and 22 | PRESENTATION, CEILING | KNOWN | The FR can evaluate the TNA's figure without repeating it: name it as one house's 10-15-year compound assumption, place it in the panel, and show the register's 4-10% test (3e and Table 2's note) | The TNA is frozen; this is a risk to record, not a change | Keel inference | risk: TNA l.23 ("forecast", one house) | This card |
| 33 | Scale of the three uncertainties for a five-year hold (Keel inference): house-to-house disagreement about 4 points (5.0 to 9.0 without GMO and Ninety One); one house's own middle half about 12 points (BlackRock, 3.3 to 15.6); realised five-year misses 6 to 10 points (Robeco, Northern Trust, J.P. Morgan) | Rows 7, 22, 23, 24, 5 | MOVE2031, HALFKEPT, CEILING, PRESENTATION | NICHE | Choosing a different house would change the top far less than the market does. The plan already lets the market set the top on the trade day (range rule, NUMBERS section 4) and keeps the forecast out of the promise | The three are different measures (spread of central figures, uncertainty of the mean, realised error); added together they are only an order of size | Built from VERIFIED rows; the comparison is Keel inference | no | This card |
| 34 | Vanguard's own limits: forecasts are "not intended to be extrapolated into short-term outlooks", and the model "may be underestimating extreme negative scenarios" | Vanguard (2026a) | PRESENTATION, MOVE2031 | KNOWN | A second house, the maker of VT, says in its own words what claim 3 says | Disclaimer language; every house has one | VERIFIED (page read in part) | no | corporate.vanguard.com VEMO return forecasts page |

## (b) Cards

**Card 1 (row 1): the 7.5% verified at the source**
- What is it? J.P. Morgan's 2027 LTCMA, estimates as of 30 Sep 2026, released 19 Oct 2026 in New York (20 Oct Sydney).
  The matrix row is "AC World Equity 7.50 8.94 17.88 7.00": compound, arithmetic, volatility, then last year's compound.
  The figures are nominal USD over 10-15 years.
- Did it work? The register (NUMBERS section 0) and CANON B15 quote the right column and the right volatility. No
  correction is needed.
- How is Laura's case like it? The plan uses a long-run world-share figure for VT, a world all-cap fund held in USD.
- How is it not? ACWI is large and mid cap and VT is all-cap. The figure is gross of VT's 0.06% fee (about 7.44% net,
  Keel arithmetic). Its horizon is 10-15 years against the plan's 3 and 5.
- What Caplet takes: 3e and Table 2's note. Cite it as J.P. Morgan's 2027 compound assumption for global equities over
  10-15 years, nominal USD, with "as of 30 Sep 2026". Never call it a forecast for 2031 or 2033.

**Card 2 (row 22): where 7.5% sits in the panel**
- What is it? Fifteen world-share figures from Sep 2025 to Nov 2026, put on one basis. They run from about -2.5% to 9.0%,
  with a median of 6.5%. J.P. Morgan ties for fifth.
- Did it work? Claim 2 fails: BlackRock (9.0), Robeco (7.85, five years), HSBC (7.81) and BNY (about 7.7) sit above it.
  It is not an outlier either: Aon (7.5) ties it, and Aon calls itself "middle of the pack".
- How is Laura's case like it? Caplet chose one house's figure. A judge who knows the field may ask why that one.
- How is it not? The houses use different horizons, currencies and bases. The ranking is approximate, and every blend is
  Keel arithmetic.
- What Caplet takes: 3e. One clause names the spread, about 5% to 9% among most large houses. That makes 7.5% read as
  a tested middle assumption, never "the forecast". The register's 4-10% test already covers most of it.

**Card 3 (row 23): Robeco's five-year report card**
- What is it? Robeco graded its own five-year forecasts for developed-market shares over nine windows, 2012-16 to
  2020-24. All nine were too low, by 6.8 points a year on average. Across the nine, forecast and outcome correlate at
  0.05 (Keel arithmetic).
- Did it work? As a forecast of the level, no. Robeco's own lesson is that relative calls matter more than absolute
  levels.
- How is Laura's case like it? Her shares are held about five years (the half kept) and about three (the half moved). These
  are the horizons Robeco graded.
- How is it not? The windows overlap (fewer than two independent periods) and are in EUR. They fall in one long bull
  run, so every miss points the same way. A bear decade would show misses the other way.
- What Caplet takes: 3c and 3e. The top is set from the market on the trade day, never from a forecast (the range rule,
  NUMBERS section 4). Five-year evidence says that is the right order of trust.

**Card 4 (rows 25-28): the academic answer at 3-5 years**
- What is it? Ma et al. (2024): the 5-year horizon is the weakest, with out-of-sample R squared of 1.54% and an average
  miss of 6.3 points a year. Welch and Goyal: at five-yearly frequency the classic predictors lose to the plain average.
  Boudoukh et al. (2019): 50 years hold only about 12 independent five-year windows. Szakmary et al. (2008): Value
  Line's 3-5-year projections were biased up and had no predictive power.
- Did it work? Four lines of evidence, from different methods, agree that skill at 3-5 years is close to nil for the
  level of returns. One counterpoint (Lioui and Poncet 2019) finds modest gains from tilting.
- How is Laura's case like it? VT's two halves are held over exactly these horizons.
- How is it not? The studies cover US indices or single stocks, not ACWI. The plan does not rely on the forecast being right,
  only on it being a reasonable middle.
- What Caplet takes: 3e. A reference-list candidate, Ma et al. (2024), is the investing literature Book 17 asks for. It
  supports the Table 2 note, which says markets, not the assumption, set the top.

**Card 5 (rows 7 and 33): one house's band is wider than the whole panel's disagreement**
- What is it? BlackRock prints the middle half of outcomes for ACWI's mean return over 5 years as 3.33% to 15.55%. That
  is about 12 points, against about 4 points between the central figures of most houses (5.0 to 9.0).
- Did it work? It is a forecast, so it is untested. It shows the field's own view that the uncertainty is bigger
  than the choice of house.
- How is Laura's case like it? The half kept is the money that rides this uncertainty to 2033. The half moved rides it to
  2031.
- How is it not? It is uncertainty about the mean, not year-to-year swings (17.88% volatility in J.P. Morgan's terms).
  Readers mix the two up.
- What Caplet takes: 3b and 3c. It explains why the plan states a range by rule, not by forecast, and why the half
  kept is promised to no one.

**Card 6 (row 31): the forecast moves the half kept, not the stated top**
- What is it? The register's 4-10% run (NUMBERS section 4). The stated top is $115,000 in every column, and the half kept
  runs $18,091 to $23,948.
- Did it work? Yes, as a deletion-style test: the 7.5% is not doing the work for the co-sponsors' figure.
- How is Laura's case like it? This is her plan, run on the current register.
- How is it not? The panel's low end (GMO about -2.5%, Ninety One 2.2%) lies below the tested 4%.
- What Caplet takes: 3b, 3e and Table 2's note. The plan's notes should say "the house chosen moves her flexibility
  money, not the figure she states". The numbers owner may want a 0% column if the FR mentions GMO (gap).

**Card 7 (rows 4-5): J.P. Morgan against itself**
- What is it? J.P. Morgan's ACWI figure went 5.0 (2022 edition), 8.5, 7.8, 7.1, 7.0, 7.5. Its 5.0 of Sep 2021 met 11.57% a
  year over five years, and its 7.8 of Sep 2023 met 21.73% a year over three (Keel arithmetic on a secondary ACWI
  source).
- Did it work? As a 10-15-year figure it is not yet testable. At the plan's horizons it missed by 7 to 14 points.
- How is Laura's case like it? These are the same house, the same index and the plan's horizons.
- How is it not? J.P. Morgan says the figure is not for short horizons, and there are only two windows.
- What Caplet takes: 3e only, if space allows. It is the sharpest single illustration that "realised markets set it".
  Use it with care: it can read as mocking the house the plan cites.

## (c) What would surprise a judge
- The houses publishing in the same quarter of 2026 disagree by about 11.5 points a year on world shares: GMO's blend
  is about -2.5% nominal and BlackRock's is 9.0%. The 7.5% Caplet used is upper third, not the top and not the
  consensus (rows 20, 6, 22).
- Robeco under-forecast developed-market shares in every one of the nine five-year windows it graded, by 6.8 points a
  year on average. Across those windows its forecast and the outcome are almost uncorrelated, at 0.05 (row 23).
- J.P. Morgan's own world-share figure jumped 3.5 points in one year (5.0% to 8.5%). That is more than the gap between
  its 7.5% today and the panel median (row 4).
- The one market input the plan borrows moves the stated top by $0 across 4% to 10%. It moves Laura's half kept by
  about $5,900 (row 31).
- Research Affiliates no longer goes by that name. Its forecasts are now Syzygy Asset Management's (Aug-Sep 2026), a
  trap for any reference list (row 18).

## (d) Gaps
- Not yet published at 15 Nov 2026: Vanguard's 2027 economic and market outlook (expected Dec 2026); Northern Trust's
  2027 edition; BlackRock's update with data as of 30 Sep 2026 (the workbook read is Aug 2026, data 30 Jun 2026); no
  GMO forecast as of 31 Oct 2026 was found.
- Basis not confirmed at the source: HSBC (compound or arithmetic), BNY (same, and the edition is Jan 2026), Syzygy
  (geometric not stated in the part read), and the currency of Robeco's bull and bear cases. Robeco's scenario odds
  come from secondary sources only.
- EFG 2027: the global equity row was not extracted. Callan was read only on an aggregator. Schwab, Capital Group,
  Janus Henderson and Morningstar were not read at the source this run.
- J.P. Morgan publishes no grading of its own LTCMA. The comparison in row 5 uses a secondary source for realised ACWI
  (Aon's quarterly review for the University of Washington), not MSCI's factsheet. The 2023 and 2024 J.P. Morgan
  figures were read on third-party mirrors.
- Northern Trust's developed-market pairing (4.8 against 15.1) is read from chart labels. The sentence Q6 row 5 quotes
  for 7.1% was not found in the 2026 report.
- Fama and French (1988), Campbell and Shiller, Campbell and Thompson (2008) and GMO's own track record were not read
  this run (the paper-search quota was spent). Brier (1950) and Bates and Granger (1969) are named as prior art
  without a read.
- NUMBERS has no run below 4% a year for VT. If the FR names the panel's low end, the numbers owner would need a 0% or
  -2.5% column (the half kept and the excess would fall; the stated top would not, on the section 4 pattern, which is
  Keel inference until run).
- Robeco's statement that past five-year returns explain only 1.4% of the next five years (its 2016-2020 report) is
  noted from a secondary mention. The original was not opened (UNVERIFIED).

## Sources (APA 7)
Read 14-15 Nov 2026 (Sydney) unless marked prior.

- Aon. (2026a, October 14). *Capital market assumptions: Florida Retirement System assumption conference* [Conference
  paper; as of June 30, 2026]. Office of Economic and Demographic Research, Florida Legislature.
  http://www.edr.state.fl.us/Content//conferences/actuarial/FRSAssumptionConference(Aon)Final.pdf (read in part)
- Aon. (2026b, August). *2026 capital market assumptions* [Board paper]. Nebraska Investment Council.
  https://nic.nebraska.gov/sites/default/files/doc/10a%202026%20Capital%20Market%20Assumptions.pdf (read in part)
- Aon. (2026c, October). *Quarterly investment review, third quarter 2026* [Prepared for the University of Washington].
  https://hr.uw.edu/benefits/wp-content/uploads/sites/3/2026/10/UW-QIR-3Q26-chax.pdf (read in part; secondary source for
  MSCI ACWI returns)
- American Century Investments. (2026, November 3). *Latest capital markets assumptions*.
  https://www.americancentury.com/institutional-investors/en-us/insights/latest-capital-markets-assumptions (read in part)
- AQR Capital Management. (2026). *2026 capital market assumptions for major asset classes* [Alternative Thinking].
  https://www.aqr.com/-/media/AQR/Documents/Alternative-Thinking/AQR-Alternative-Thinking---2026-Capital-Market-Assumptions.pdf
  (read in part)
- BlackRock Investment Institute. (2026a, August). *BlackRock capital market assumptions* [Data set; data as of June 30,
  2026]. https://www.blackrock.com/blk-inst-c-assets/images/tools/blackrock-investment-institute/cma/blackrock-capital-market-assumptions.xlsx
  (read in full, parsed)
- BlackRock Investment Institute. (2026b, August 11). *Capital market assumptions*.
  https://www.blackrock.com/institutions/en-us/insights/thought-leadership/capital-market-assumptions (read in part)
- BNY Investments. (2026, January 28). *2026 capital market assumptions*.
  https://www.bny.com/wealth/global/en/insights/2026-capital-market-assumptions.html (read in part)
- Boudoukh, J., Israel, R., & Richardson, M. (2019). Long-horizon predictability: A cautionary tale. *Financial Analysts
  Journal, 75*(1), 17-30. https://doi.org/10.1080/0015198X.2018.1547056 (abstract read)
- EFG International. (2026, November). *Capital market assumptions 2027*.
  https://www.efginternational.com/doc/jcr:876fd20b-1786-44a6-b890-b9301535d128/lang:en/EFG_CMA_2027_EN.pdf (read in part)
- GMO. (2026, October 16). *GMO 7-year asset class forecast: September 2026*.
  https://www.gmo.com/globalassets/articles/gmo-7-year-asset-class-forecast/2026/gmo-7-year-asset-class-forecastsep26.pdf
  (read in full)
- HSBC Asset Management. (2026, October). *Capital market assumptions: October 2026*.
  https://mena.assetmanagement.hsbc.com/-/media/Files/attachments/common/news-and-articles/articles/capital-market-assumptions-october-2026.pdf
  (read in part)
- Invesco. (2026). *Capital market assumptions, USD, Q3 2026* [Estimates as of June 30, 2026].
  https://www.invesco.com/content/dam/invesco/emea/en/pdf/invesco-capital-market-assumption-usd.pdf (read in part)
- J.P. Morgan Asset Management. (2021, November 8). *J.P. Morgan releases 2022 Long-Term Capital Market Assumptions*
  [Press release]. PR Newswire. (read in part)
- J.P. Morgan Asset Management. (2022). *2023 Long-Term Capital Market Assumptions* [Report; third-party copy].
  https://argaamplus.s3.amazonaws.com/16e85413-b739-4404-b566-776b70e843b7.pdf (read in part; UNVERIFIED as a
  J.P. Morgan-hosted copy)
- J.P. Morgan Asset Management. (2023). *2024 Long-Term Capital Market Assumptions* [Report; third-party copy].
  https://a-us.storyblok.com/f/1003391/x/8a94e4a74a/ltcma-full-report2024.pdf (read in part; UNVERIFIED as a
  J.P. Morgan-hosted copy)
- J.P. Morgan Asset Management. (2024). *Long-Term Capital Market Assumptions: Methodology handbook* (2025 ed.). (read in
  part; URL not recorded in this card)
- J.P. Morgan Asset Management. (2026a). *2027 Long-Term Capital Market Assumptions: Matrix, USD* [Data as of September
  30, 2026]. https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/portfolio-insights/ltcma/noindex/ltcma-2027-matrix-usd.pdf
  (read in full)
- J.P. Morgan Asset Management. (2026b, October 19). *J.P. Morgan releases 2027 Long-Term Capital Market Assumptions*
  [Press release]. https://am.jpmorgan.com/us/en/asset-management/adv/about-us/media/press-releases/jp-morgan-releases-2027-long-term-capital-market-assumptions/
  (read in full)
- J.P. Morgan Asset Management. (2026c). *2027 Long-Term Capital Market Assumptions* [Report].
  https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/portfolio-insights/ltcma/noindex/ltcma-2027-report.pdf
  (read in part)
- Lioui, A., & Poncet, P. (2019). Long horizon return predictability and investment decisions. *European Journal of
  Operational Research, 278*(3), 961-975. https://www.sciencedirect.com/science/article/abs/pii/S0377221719303777
  (abstract read; title as indexed, check before citing)
- Ma, R., Marshall, B. R., Nguyen, N. H., & Visaltanachoti, N. (2024). Estimating long-term expected returns.
  *Financial Analysts Journal, 80*(4), 134-154. https://doi.org/10.1080/0015198X.2024.2358737 (read in part)
- Ninety One. (2026, November 3; updated 2026, November 11). *Capital market assumptions: October 2026* [Data as at
  September 30, 2026]. https://ninetyone.com/-/media/documents/insights/2026/91-capital-market-asssumptions-october-2026-en.pdf
  (read in part)
- Northern Trust Asset Management. (2026, January 9). *2026 capital market assumptions: 10 year outlook* [Data as of
  September 30, 2025]. https://ntam.northerntrust.com/content/dam/northerntrust/investment-management/global/en/documents/thought-leadership/2026/cma/2026-capital-market-assumptions-report.pdf
  (read in part, twice)
- PGIM. (2026, November). *Capital market assumptions* [Data as of September 30, 2026].
  https://www.pgim.com/us/en/financing/insights/market-portfolio/outlooks/capital-market-assumptions (read in part)
- PortfolioLab. (n.d.). *Capital market assumptions*. https://www.portfoliolab.app/capital-market-assumptions (secondary;
  Callan figures UNVERIFIED)
- Robeco. (2025). *5-year expected returns 2026-2030: The stale renaissance*.
  https://www.robeco.com/files/docm/docu-2025-robeco-5-year-expected-returns-the-stale-renaissance.pdf (chapter 6 read)
- Robeco. (2026a, September 22). *Expected returns 2027-2031: The great rewiring* [Summary].
  https://www.robeco.com/files/docm/docu-summary-expected-returns-2027-2031-en.pdf (read in full)
- Schwab Asset Management. (2026). *Schwab's long-term capital market expectations*.
  https://www.schwab.com/learn/story/schwabs-long-term-capital-market-expectations (read in part)
- State Street Global Advisors. (2026). *Long-term asset class forecasts: Q4 2026*.
  https://www.ssga.com/us/en/institutional/insights/long-term-asset-class-forecasts-q4-2026 (read in full)
- Syzygy Asset Management. (2026a). *Asset allocation interactive: Expected returns* [Interactive tool; as of October
  31, 2026; formerly Research Affiliates]. https://interactive.researchaffiliates.com/asset-allocation (rendered and
  read)
- Syzygy Asset Management. (2026b, September 10). *Research Affiliates relaunches as Syzygy Asset Management* [Press
  release]. https://www.syzygyassetmanagement.com/about-us/in-the-news/press-release/research-affiliates-relaunches-as-syzygy-asset-management
  (read in part)
- Szakmary, A. C., Conover, C. M., & Lancaster, C. (2008). An examination of Value Line's long-term projections.
  *Journal of Banking & Finance, 32*(5), 820-833. https://doi.org/10.1016/j.jbankfin.2007.06.002 (abstract and
  conclusion read)
- Vanguard. (2026a, October 21). *Vanguard economic and market outlook: Return forecasts* [Model run of September 30,
  2026]. https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html (read in part,
  via a mirror and the chart table)
- Vanguard. (2026b, October 30). *Vanguard economic and market outlook* [FAVEMOBF].
  https://advisors.vanguard.com/content/dam/fas/pdfs/FAVEMOBF.pdf (read in part)
- Welch, I., & Goyal, A. (n.d.). *A comprehensive look at the empirical performance of equity premium prediction*
  [Working paper, section 5]. https://repec.som.yale.edu/icfpub/publications/2412.pdf (read in part; published version
  2008, *Review of Financial Studies*, not re-read)
- Wicker, W. (2024). *Reality check: Capital market assumptions vs. actual returns*. Dimensional Fund Advisors.
  https://www.dimensional.com/us-en/insights/reality-check-capital-market-assumptions-vs-actual-re (prior, card Q6 row
  13; URL as recorded, truncated)
