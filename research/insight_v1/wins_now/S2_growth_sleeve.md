# S2: Growth sleeve fund research (WInS week 1, PROVISIONAL)

Agent S2 (growth-sleeve researcher), insight_v1 run, written 2026-09-27. This is AI-generated research for Team
Caplet. It is not submission text; the team decides and writes everything. Phases B-E may change it, and the team
has not yet approved the strategy.

Script: `research/insight_v1/scripts/S2_growth_sleeve.py`, with data in `research/insight_v1/scripts/data/S2/`.
Run it from the repo root with `.venv/bin/python research/insight_v1/scripts/S2_growth_sleeve.py`.

Terms used below:
- **Expense ratio**: the fund's yearly fee as a share of the money invested.
- **Top-10 concentration**: the share of the fund held in its ten biggest stocks.
- **Look-through**: what you end up owning, stock by stock, once all your funds are added together.
- **Active share**: how far a portfolio's stock weights differ from an index. 0% means identical and 100% means
  nothing in common.

---

## 0. Summary

1. **The WInS rules page removes the sector problem.** I read Wharton's public SMApply "Trading Details" page myself
   on 2026-09-27. It says: "There is no required sector allocation or minimum number of sectors." It also says:
   "Exchange-Traded Funds: Any ETF available on WInS." Starting cash is $300,000, and the team gets up to 200 trades
   (VERIFIED-PRIMARY, https://wghsinvcomp.smapply.us/res/p/trading/). The FAQ adds a flat $25 commission on each
   stock or ETF trade (VERIFIED-PRIMARY, https://wghsinvcomp.smapply.us/res/p/faqs/). This agrees with A1's case
   register (`phase_A/case_register.md`, R-W65 to R-W70, R-W92). So the "sector minimum = team size" claim is
   **contradicted**. Section 4 keeps a sector-fund fallback only as a contingency.
2. **Recommended pick for both the WInS growth sleeve and Laura's long-term sleeve: VT (Vanguard Total World Stock
   ETF).** PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading. VT costs 0.06%,
   holds 10,048 stocks, and its top-10 concentration is 21.7% (issuer fact sheet 2026-06-30). The S&P 500's top-10
   concentration is 38.8% (issuer holdings 2026-09-24). VT was on the 2025-26 list.
   - **Alternate 1:** VTI + VXUS, about 62/38.
   - **Alternate 2:** ITOT + IXUS, the iShares twins at the same weights.
3. **The real case for global over U.S.-only is concentration, not return.** J.P. Morgan's 2026 LTCMA (repo PDF)
   gives AC World 7.00% compound against U.S. large cap 6.70%. On a ~$95k equity sleeve over 2028-2033, that gap is
   worth only about **$1.9k**. Expected volatility is almost the same (a VT-like mix: 16.42%; U.S. large cap: 16.47%).
   What changes a lot is how much rides on one theme:
   - A 12-stock "AI-linked mega-cap" basket is **40.7% of the S&P 500** today.
   - That basket is **~22% of VT**, counting the top 10 only.
4. **Going global does not remove AI exposure. It moves some of it to Asia.** VXUS's four largest holdings are TSMC,
   Samsung, SK hynix and ASML, together 10.8%. All four make AI chips or chip equipment. Emerging-market funds hold
   **13-16% TSMC**. The team should say this plainly rather than claim that "global = diversified away from AI".
5. **Taiwan: keep market weight and add no tilt.** VT holds Taiwan at 3.5% and TSMC at 1.7%.
   - On a ~$95k equity sleeve, that is about **$3.3k of Taiwan stocks**. A 2033 facility contribution has a median
     of about $207k, so this is about 1.6% of it. That is far too small to hedge Taiwan-dollar facility costs.
   - Taiwan's market is about 75% technology (EWT fact sheet). A tilt toward Taiwan would therefore be an AI bet, and
     choosing it because the residency is in Taiwan would be tokenism.
   - Drop EWT (0.59% fee, 76 holdings, 23% 3-year standard deviation).
6. **A human-capital tilt (underweighting publishing and media) does not earn its complexity.**
   - Book publishing is almost absent from the index. News Corp, which owns HarperCollins (publisher of *Messy
     Roots*), is **0.021% of the S&P 500**, about $20 on the sleeve.
   - Alphabet and Meta make up about 80% of "Communication Services". Underweighting that sector would really be an
     anti-AI bet with the wrong label.
   - Timing also rules it out. Laura's income matters to the portfolio mainly through the 2028 deposit, and that
     arrives before the sleeve holds much stock.
7. **The equity-weight inconsistency needs a team decision.**
   - The plan implies roughly 17-24% total equity after 2028 (50-70% of the sleeve).
   - The WInS mirror in the blueprint uses ~35% equity.
   - My suggestion: mirror the plan, about **21% VT / 79% Treasuries** in WInS. The Trading Notes then match the IPS
     numbers. Section 6 sets out the options.

---

## 1. Candidate table (issuer primary data, accessed 2026-09-27)

"2025-26 list" is the historical list only (`competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt`,
VERIFIED-REPO-FILE; it holds 100 ETFs). This year's rule is "any ETF available on WInS" (VERIFIED-PRIMARY, SMApply).
The approval check for this year is therefore "is it searchable and tradable in WInS?".

Top-10 figures from issuer fact sheets are as of 2026-06-30 unless marked otherwise. The "AI/semis in top 10" column
adds up the top-10 names that belong to the AI-linked set: the Magnificent 7 plus AVGO, MU, AMD and ORCL, and
outside the U.S. TSMC, Samsung, SK hynix, ASML, Tokyo Electron, MediaTek, Delta and Hon Hai. That set is my own
definition (ASSUMPTION), so the figure is a **lower bound**.

| Ticker | Role | Index | Expense ratio | Holdings | Top-10 % | Largest holding | AI/semis in top 10 | Taiwan % / TSMC % | 2025-26 list |
|---|---|---|---|---|---|---|---|---|---|
| **VTI** | U.S. total | CRSP US Total Market (being renamed Morningstar, see note a) | 0.03% | 3,531 | 33.4 | NVDA 6.4 | 32.0 | 0 / 0 | Yes (0.03) |
| ITOT | U.S. total | S&P Total Market Index | 0.03% | 2,460 (9/24) | 32.11 | NVDA 6.63 | 32.11 | 0 / 0 | No |
| SCHB | U.S. total | (Dow Jones U.S. Broad Stock Market, snippet) | 0.03% SNIPPET-UNVERIFIED | ~2,400 SNIPPET-UNVERIFIED | n/a | n/a | n/a | 0 / 0 | No |
| **VOO** | U.S. large | S&P 500 | 0.03% | 506 | 37.9 | NVDA 7.5 | 36.4 | 0 / 0 | Yes (0.03) |
| IVV | U.S. large | S&P 500 | 0.03% | 504 (9/24) | 36.37 | NVDA 7.51 | 36.37 | 0 / 0 | No |
| SPYM (formerly SPLG, note b) | U.S. large | S&P 500 | 0.02% gross | 506 | 36.67 (6/30); **38.82 (9/24)** | NVDA 8.19 (9/24) | **40.73 (9/24, full holdings, 12 names)** | 0 / 0 | No (neither ticker) |
| **VT** | Global all-country | FTSE Global All Cap | 0.06% | 10,048 | 21.7 | NVDA 4.0 | 21.7 | 3.5 / 1.7 | **Yes (0.06)** |
| ACWI | Global all-country | MSCI ACWI | **0.32%** | 2,196 (9/24) | 23.19 | NVDA 4.54 | 23.19 | 3.30 / 1.83 | No |
| VEA | Developed ex-U.S. | FTSE Developed All Cap ex US (includes Canada and Korea) | 0.03% | 3,868 | 15.0 | Samsung 3.5 | 8.9 | 0 / 0 | Yes (0.05 then) |
| IEFA | Developed ex-U.S. | MSCI EAFE IMI (no Canada, no Korea) | 0.07% | 2,627 (9/24) | 12.28 | ASML 3.03 | 3.87 | 0 / 0 | No |
| SCHF | Developed ex-U.S. | FTSE Developed ex US (snippet) | 0.03% SNIPPET-UNVERIFIED | n/a | 13.7 SNIPPET-UNVERIFIED | n/a | n/a | n/a | No |
| **VXUS** | Total ex-U.S. | FTSE Global All Cap ex US | 0.05% | 8,755 | 15.0 | TSMC 4.3 | 10.8 | 9.1 / 4.3 | Yes (0.07 then) |
| IXUS | Total ex-U.S. | MSCI ACWI ex USA IMI | 0.07% | 4,585 (9/24) | 14.95 | TSMC 4.36 | 10.72 | 9.06 / 4.36 | No |
| VWO | Emerging | FTSE Emerging Markets All Cap China A Inclusion (no Korea) | 0.06% | 6,332 | 27.7 | TSMC 16.3 | 19.8 | 34.3 / 16.3 | Yes (0.08 then) |
| IEMG | Emerging | MSCI EM IMI (includes Korea) | 0.09% | 2,861 (9/24) | 35.27 | TSMC 13.22 | 31.5 | 27.41 / 13.22 | No |
| RSP | U.S. equal weight | S&P 500 Equal Weight | 0.20% (2025-26 list; issuer page refused) | ~500 (by design) | ~2 (by design) | ~0.2 each | ~2.4 (12 x ~0.2) | 0 / 0 | Yes (0.2) |
| EWT (for reference) | Single country | MSCI Taiwan 25/50 | 0.59% | 76 (9/24) | 50.51 | TSMC 20.71 | most of it (IT 75.11%) | ~100 / 20.71 | Yes (0.58) |

Notes and status:
- **Vanguard (VTI, VOO, VT, VEA, VXUS, VWO): VERIFIED-PRIMARY.**
  - Source: fact sheets as of 2026-06-30 at https://fund-docs.vanguard.com/F0970.pdf (VTI), F0968.pdf (VOO),
    F3141.pdf (VT), F0936.pdf (VEA), F3369.pdf (VXUS) and F0964.pdf (VWO).
  - I also checked the current expense ratios for VTI (0.03), VT (0.06), VXUS (0.05) and VWO (0.06) on the product
    pages https://investor.vanguard.com/investment-products/etfs/profile/{ticker}.
  - "Holdings" means the fund's "Number of stocks".
  - Vanguard's sector labels follow ICB, a different classification from the S&P/MSCI "GICS". That is why VTI shows
    "Technology 41.0%".
  - (a) The VTI product page is now titled "VTI-Vanguard **Morningstar** Total Stock Market ETF". The fact sheet says
    the CRSP benchmarks are being rebranded as Morningstar after "Morningstar's recent acquisition of CRSP", with the
    change "expected to occur in July 2026". The ticker is unchanged. If WInS shows the new name, it is the same fund.
- **iShares (ITOT, IVV, ACWI, IEFA, IXUS, IEMG, EWT): VERIFIED-PRIMARY.**
  - Sources: fact sheets as of 2026-06-30 (e.g.
    https://www.ishares.com/us/literature/fact-sheet/itot-ishares-core-s-p-total-u-s-stock-market-etf-fund-fact-sheet-en-us.pdf)
    and product pages https://www.ishares.com/us/products/{239724, 239726, 239600, 244049, 244048, 244050, 239686}/.
  - The product pages give the expense ratio and "Number of Holdings" as of 2026-09-24, and the "30 Day Median
    Bid/Ask Spread" of **0.01% for all seven** as of 2026-09-25. That is a liquidity check.
  - The CSV holdings download returned an HTML page instead of data, so iShares top-10 figures come from the
    fact sheets.
- **SPYM: VERIFIED-PRIMARY.**
  - Sources: the fact sheet
    https://www.ssga.com/us/en/intermediary/library-content/products/factsheets/etfs/us/factsheet-us-en-spym.pdf
    (gross expense ratio 0.02%, CUSIP 78464A854) and the daily holdings file (holdings as of 24-Sep-2026) at
    https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spym.xlsx.
  - (b) The old SPLG holdings file stops at "As of 29-Oct-2025" (VERIFIED-PRIMARY, same URL pattern with "splg").
  - Search snippets say the ticker changed from SPLG to SPYM on 2025-10-31 (SNIPPET-UNVERIFIED, MIAX alert
    https://www.miaxglobal.com/alert/2025/10/30/...). **In WInS, search "SPYM", not "SPLG".**
- **Schwab (SCHB, SCHF): the issuer site refused access.** https://www.schwabassetmanagement.com/products/schb returned
  HTTP 403 "Access Denied". The figures shown are SNIPPET-UNVERIFIED (WebSearch 2026-09-27, e.g. aaii.com, etfdb.com).
  Neither fund is recommended until someone verifies them.
- **Invesco (RSP): the issuer site refused access.** invesco.com returned HTTP 406 for the product page and the fact
  sheet. The 0.20% comes from the 2025-26 list (VERIFIED-REPO-FILE, historical). "~$89B assets" and "neared $100
  billion ... July 2026" are SNIPPET-UNVERIFIED.
- **Sizing check:** WInS limits each trade to twice a security's daily volume (SMApply, VERIFIED-PRIMARY). ITOT alone
  traded 1.67M shares (about $280M) on 2026-09-25 (VERIFIED-PRIMARY). A ~$60-110k order is tiny next to that, so the
  limit cannot bind for any core fund here. VT's own daily volume is not verified (ASSUMPTION that it is ample; VT
  ETF net assets were $77.6B on 2026-06-30).

---

## 2. U.S.-only or global? (JPM 2026 LTCMA, `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf`, page 2)

### 2.1 JPM inputs (VERIFIED-REPO-FILE; data as of 2025-09-30, USD, nominal)

| Asset class | Compound | Arithmetic | Volatility | (Arithmetic - cash 3.10) / volatility |
|---|---|---|---|---|
| U.S. large cap | 6.70% | 7.94% | 16.47% | 0.294 |
| AC World equity | 7.00% | 8.28% | 16.78% | 0.309 |
| EAFE equity | 7.50% | 8.90% | 17.63% | 0.329 |
| Emerging markets equity | 7.80% | 9.74% | 20.93% | 0.317 |
| U.S. mid cap / small cap | 7.00% / 6.90% | 8.55% / 8.89% | 18.56% / 21.10% | 0.295 / 0.274 |
| U.S. quality factor / min-vol factor | 6.60% / 7.00% | 7.64% / 7.79% | 15.11% / 13.16% | 0.300 / 0.356 |

- **Correlations** (a correlation of 1 means two assets move together perfectly): U.S. large cap with EAFE 0.87, U.S.
  with EM 0.73, EAFE with EM 0.86, U.S. with AC World 0.97.
- The last column is a simple reward-per-risk ratio (Sharpe-style). It is my calculation from JPM's numbers.

### 2.2 Mixes, computed by the S2 script

A portfolio's compound return is roughly its arithmetic return minus half its variance (ASSUMPTION: the standard
approximation).

| Mix | Arithmetic | Volatility | ≈ Compound |
|---|---|---|---|
| 100% U.S. large cap | 7.94% | 16.47% | 6.58% (JPM states 6.70%) |
| 62/28/10 U.S./EAFE/EM (VT-like; VT is 61.9% U.S.) | 8.39% | 16.42% | 7.04% (matches JPM AC World 7.00%) |
| 70/30 U.S./EAFE | 8.23% | 16.34% | 6.89% |

### 2.3 What this means

1. **Return:** global is expected to beat U.S.-only by about 0.3 points a year. Take $94,800 of equity (60% of a
   ~$158k sleeve; ASSUMPTION from brief section 7) held for 5 years (2028 to 2033):
   - at 6.70% it grows to $131.1k;
   - at 7.00% it grows to $133.0k;
   - **the difference is +$1.9k.**

   This fits the earlier finding in brief section 8, item 5: more equity or different equity mainly changes the
   range, not the median. **Return is not a reason to choose.**
2. **Volatility:** by JPM's numbers, going global barely reduces volatility (16.42% vs 16.47%). Currency risk offsets
   the diversification. **Do not claim "global lowers risk" in the volatility sense.**
3. **Concentration:** here the difference is large, and the numbers come from issuer holdings.

   | | S&P 500 (SPYM, 9/24) | VTI/ITOT (6/30) | VT/ACWI (6/30) |
   |---|---|---|---|
   | Top-10 concentration | 38.8% | 32-33% | 21.7-23.2% |
   | Largest single holding | NVDA 8.19% | ~6.5% | NVDA 4.0-4.5% |
   | AI-linked basket (12 names) | 40.7% | | |

   One theme sits behind 40% of a U.S. large-cap fund. That is the honest risk argument for Laura.
4. **Valuation context:** the fact sheets show price-to-earnings (P/E) ratios of 29.2x for ITOT, 30.2x for IVV, 18.6x
   for IEFA and 19.9x for IEMG (VERIFIED-PRIMARY, 2026-06-30). A P/E ratio is the share price divided by a year of
   earnings; a higher number means investors pay more for each dollar of profit. My reading (ASSUMPTION): JPM expects
   higher returns outside the U.S. mainly because those markets start from lower prices relative to earnings. That
   is a market-consistent reason. It is not a forecast that AI will fail.
5. **Consistency flag:** `strategy_mc.py` models the sleeve as U.S. large cap only (brief section 11). If the team
   picks VT, the projection input should become AC World (7.00% compound, 16.78% volatility). That adds roughly
   +$1.9k to the median. The change is small, but the IPS, the model and the WInS holding should all use one
   assumption.

### 2.4 Global funds still carry AI exposure, now in Asia

VXUS's top four holdings are TSMC 4.3, Samsung 2.6, SK hynix 2.2 and ASML 1.7. IEMG's top three are TSMC 13.22,
Samsung 7.15 and SK hynix 6.70. All are AI-hardware suppliers (VERIFIED-PRIMARY, fact sheets). Adding ex-U.S. stocks
lowers single-stock concentration but still leaves the portfolio tied to the same AI build-out cycle.

**What a strong sentence must contain:**
- the verified top-10 numbers (38.8% vs 21.7%);
- the fact that JPM expects the world to earn slightly more than the U.S.;
- an admission that AI chip exposure remains through TSMC and Korea.

### 2.5 Taiwan exposure and the residency (no tokenism)

**Facts (VERIFIED-PRIMARY, issuer fact sheets as of 2026-06-30):**

| Fund | Taiwan % | TSMC % | Other |
|---|---|---|---|
| VT | 3.5 | 1.7 | |
| ACWI | 3.30 | 1.83 | |
| VXUS | 9.1 | 4.3 | |
| IXUS | 9.06 | 4.36 | |
| VWO | 34.3 | 16.3 | |
| IEMG | 27.41 | 13.22 | |
| EWT | ~100 | 20.71 | information technology 75.11% |

**Size in Laura's plan (ASSUMPTION inputs):**
- A ~$94.8k equity sleeve in VT holds about $3.3k of Taiwan stocks and about $1.6k of TSMC.
- The median 2033 surplus is $207k (brief section 6). The Taiwan holding is about 1.6% of it.

**Why no Taiwan tilt:**
- **Currency.** The residency is in Taiwan, but the case never names a currency (A1, R-AN10). A rise in the Taiwan
  dollar would push up facility costs measured in USD, and would also lift Taiwan stocks measured in USD. At market
  weight this offset is worth only a few thousand dollars against a facility bill of hundreds of thousands. It is a
  fact to disclose, not a hedge to build.
- **What a tilt really buys.** Adding EWT would mostly be adding TSMC and the AI supply chain: 75% information
  technology, a 23.22% 3-year standard deviation and a 0.59% fee. That is more AI concentration, not a hedge.
- **Shared shocks.** A Taiwan-specific shock (geopolitics, an earthquake) could hit the residency project and the
  holding at the same time. The link could run either way, and it is too small to model usefully.
- **Tokenism.** Choosing Taiwan stocks because the residency is in Taiwan is the kind of decoration the brief forbids.

**What the team can honestly say:** "the world index already owns Taiwan at its market weight; we chose not to add
more".

---

## 3. Should the sleeve hold RSP (equal weight) or a factor fund?

- **RSP.** It cuts the AI basket from ~40.7% to ~2.4% (about 0.2% × 12 names). That is a large active bet in its own
  right. It leans toward smaller and value stocks, costs 0.20% (versus 0.03-0.06%), trades back to equal weights every
  quarter, and has no JPM return assumption to anchor a projection. VT already cuts top-10 concentration from 38.8% to
  21.7% while staying market-weighted at 0.06%.
  **Verdict: RSP does not earn a place.** Keep it only as an optional answer if the team explicitly wants to act on an
  AI-bubble view, and then call it a view.
- **Quality factor (QUAL).** JPM gives the U.S. quality factor 6.60% compound, below U.S. large cap's 6.70%, so it
  does not earn a place.
- **Minimum volatility (USMV).** JPM gives the min-vol factor a higher reward-per-risk (0.356). The sleeve's job is
  growth, though, and the brief's "risk only in the surplus" design already controls risk.
  **Not recommended; listed so the team knows it was considered.**

---

## 4. Sector-rule fallback (contingency only; the rule appears NOT to exist)

**Status.** SMApply "Trading Details" says: "There is no required sector allocation or minimum number of sectors."
(VERIFIED-PRIMARY, 2026-09-27). Use this section only if Wharton later says otherwise, or if WInS were to reject broad
ETFs. A broad fund such as VT already holds all 11 GICS sectors, the standard 11-way split of the stock market.

**Fallback set.** These are the 11 Select Sector SPDRs, weighted like today's S&P 500.
- I mapped each of the 504 SPYM holdings (2026-09-24) to the sector fund that holds it; 0.00% was left unmapped.
- All 11 funds have a 0.08% gross expense ratio (issuer fact sheets as of 2026-06-30, VERIFIED-PRIMARY).
- 10 of the 11 were on the 2025-26 list. XLRE was not; VNQ was.

| Fund | Sector | Weight | Fund | Sector | Weight |
|---|---|---|---|---|---|
| XLK | Information Technology | 39% | XLI | Industrials | 8% |
| XLF | Financials | 12% | XLP | Consumer Staples | 4% |
| XLC | Communication Services | 10% | XLE | Energy | 3% |
| XLV | Health Care | 9% | XLU | Utilities | 2% |
| XLY | Consumer Discretionary | 9% | XLB | Materials | 2% |
| | | | XLRE (or VNQ) | Real Estate | 2% |

**Alternates.** Vanguard sector ETFs, 0.09% (VGT, VFH, VDC, VDE, VIS, VOX, VCR, VHT; VNQ 0.13%) from Vanguard fact sheets
as of 2026-06-30 (VERIFIED-PRIMARY). VPU and VAW were not checked.

**How the story changes (script output):**
1. **It is not the market.** The sector funds cap their largest stocks: XLK holds NVDA 15.3%, AAPL 13.8% and MSFT
   10.4%, and XLC holds META 23.2%. So the 11-fund mix owns only 29.7% of the AI basket, against 40.7% in the index.
   - NVDA falls from 8.19% to 6.00%.
   - Alphabet (both share classes) falls from 5.46% to 2.05%.
   - The mix has an active share of **13.5%** against the S&P 500.

   The team would be making a partly hidden anti-mega-cap bet and would have to disclose it.
2. **It is U.S.-only.** No Select Sector fund holds TSMC or Europe, so the global argument in section 2 is lost unless
   the team adds VXUS as a 12th fund.
3. **It costs more to run.** WInS charges a $25 commission per trade (VERIFIED-PRIMARY). Eleven buys cost $275 against
   $25-50 for one or two funds. Every rebalance also uses up to 11 of the 200 trades.
4. **Complexity is visible to judges.** Eleven tickers make the equity sleeve look like sector picking, which works
   against the plan's message that "risk lives only in the surplus".

---

## 5. Optional human-capital hedge (underweight publishing/media): not recommended

**The idea.** Laura's 2028 deposit comes from "publishing advances, speaking engagements, licensing, and other
entrepreneurial ventures" (case p.2, lines 43-45, VERIFIED-REPO-FILE). If her income depends on the publishing and
media economy, perhaps the portfolio should own less of it.

**Facts:**
- *Messy Roots* is published by HarperCollins. Source: the harpercollins.ca product page for ISBN 9780063067769,
  VERIFIED-PRIMARY 2026-09-27. Wikipedia (secondary) says the same: publisher HarperCollins, March 8, 2022.
- HarperCollins appears among News Corp's businesses on https://newscorp.com/ (VERIFIED-PRIMARY 2026-09-27).

**Size (script, SPYM holdings 2026-09-24):**
- News Corp (NWSA + NWS) is **0.021%** of the S&P 500. On a $94.8k equity sleeve that is **about $20**.
- Communication Services is 10.08% of the index. Alphabet and Meta alone are 8.04% of the index, **80% of the
  sector**.
- Halving Communication Services would move about $4.8k. About 80% of that would come out of Alphabet and Meta, not
  publishing.

**Why it fails:**
1. **Wrong target.** The listed market barely contains trade publishing. A "media underweight" is really a bet
   against AI platforms.
2. **Wrong timing.** Her income reaches the portfolio mainly through the 2028 deposit. In 2027 the sleeve is only the
   ~$7.7k left after the Treasury purchase (brief section 6). At 60% equity that is ~$4.6k of stock, and halving
   Communication Services would move about $230. By the time the sleeve is large, the deposit has already arrived.
3. **The strategy already hedges the human-capital risk that matters.** Under lock-early, a missing 2028 deposit hits
   the facility contribution, not the ten payments (brief section 8, item 8). That is the strong human-capital
   argument, and it needs no tilt.

**Verdict:** no tilt. A strong sentence would name:
- the 0.021% figure;
- the 80% Alphabet/Meta share;
- the fact that the lock-early structure is her real hedge against career risk.

This also serves the "willingness vs ability" point from the team's client insight.

---

## 6. Recommendations

Every ticker below carries this label: **PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules
before trading.** This year the check means confirming that the ticker is available and tradable in WInS (SMApply:
"Any ETF available on WInS").

### 6.1 WInS growth sleeve

**Primary: VT.** PENDING APPROVAL CHECK.
- Global all-cap, FTSE Global All Cap index, 0.06%, 10,048 stocks, top-10 concentration 21.7%, ETF net assets
  $77.6B (fact sheet 2026-06-30). It was on the 2025-26 list.
- It is U.S.-listed, so it fills at real-time U.S. prices. WInS delays non-U.S. equity orders until the end of the
  day (SMApply, VERIFIED-PRIMARY).
- **Trace:**
  - The case says she wants "an appropriate balance between pursuing growth and protecting the capital required for
    her goals" (case p.2). The Treasuries protect the capital; VT is the growth part.
  - One cheap, transparent fund means one sentence can explain the growth sleeve.
  - VT matches the JPM AC World assumption used for projections, so WInS, the IPS and the model tell the same story.

**Alternate 1: VTI + VXUS at about 62/38.** PENDING APPROVAL CHECK.
- Blended fee ~0.038%. Both were on the 2025-26 list.
- Same market exposure as VT. Two funds also give the team a visible U.S./international rebalance, which could
  become Trading Note 3 ("discipline").

**Alternate 2: ITOT + IXUS at about 62/38.** PENDING APPROVAL CHECK.
- iShares, 0.03% and 0.07%, bid/ask spread 0.01% (9/25). Neither was on the 2025-26 list.
- Use it if Vanguard tickers are missing from WInS.

**Not recommended:**
- **ACWI:** same exposure at 0.32%, about 5x VT's fee.
- **VOO/IVV/SPYM alone:** 38.8% top-10 concentration.
- **RSP, EWT, the sector set:** see sections 3-4.

### 6.2 Laura's long-term growth sleeve (2028-2033, then post-2033 flexibility)

**Primary: VT.** Label as above. The reasons are the same, and it is a single holding she can follow herself. A
statistics-trained client can check one index against one JPM line.

**Alternate 1: VTI + VXUS.** It saves about 2 basis points a year, about $21 a year on $95k (a basis point is 0.01%).
It also allows a U.S./international rebalancing band if the team wants one.

**Alternate 2: ITOT + IXUS.**

The equity share inside the sleeve (50/60/70%) is the brief's open question. S2 takes no position beyond the brief:
that choice changes the range, not the median.

### 6.3 Resolve the equity-weight inconsistency (team decision; do not hide it)

Figures computed from the brief's inputs (ASSUMPTION):
- At 2028-01-01 the Treasury ladder is worth about $305k: $292.3k grown at about the 1-year rate of 4.50%.
- The sleeve is about $158k: $7.7k plus the $150k deposit.
- At 60% sleeve equity, stocks are about $95k of about $463k, **≈ 20.5% of the total**. At 50% and 70% sleeve
  equity the total is ≈ 17% and ≈ 24%.

| WInS option | Equity (VT) | Treasuries | For | Against |
|---|---|---|---|---|
| A: literal January 2027 book | ~2-3% | ~97% | Exactly what her $300k would hold in 2027 | Almost no growth trade to write a note about; looks like "all bonds" |
| **B: mirror the post-2028 plan (suggested)** | **~21% (~$63k)** | **~79% (~$237k)** | Same percentages as the IPS and the model, so the three deliverables agree | Needs one sentence explaining that WInS's $300k stands in for the post-2028 mix |
| C: blueprint's 35% | ~35% (~$105k) | ~65% | More visible growth activity | Implies an equity share the plan never holds; judges read the notes and the IPS together |

My suggestion is B. The team decides.

**What a strong Trading Note on the VT buy must contain** (elements only; the team writes it):
- the action and share of the portfolio;
- "growth sleeve = money the ten payments don't need";
- why world rather than U.S.-only (top-10 concentration 21.7% vs 38.8%);
- the risk accepted (stock-market falls reduce the facility range, not the payments).

**Final Report chart idea** (charts are not allowed in the IPS): a bar chart of top-10 concentration for the S&P 500,
VTI, VT and VXUS, with the AI-linked share highlighted. The data is the table in section 1.

---

## 7. Open issues passed on
1. Check in WInS that VT, VTI, VXUS, ITOT and IXUS are available, and that SPYM appears under its new ticker.
2. The team chooses the WInS equity mirror: option A, B or C in section 6.3.
3. Switch the projection's equity assumption from U.S. large cap to AC World if VT is chosen (`strategy_mc.py`, brief
   section 11).
4. Verify SCHB, SCHF and RSP on issuer pages. The sites refused this session (Schwab HTTP 403, Invesco HTTP 406).
5. The iShares holdings CSV endpoint returned HTML, so the AI-basket shares for non-S&P funds are top-10 lower bounds
   only.

## Sources (all accessed 2026-09-27)
- **Wharton SMApply:**
  - https://wghsinvcomp.smapply.us/res/p/trading/ (sector rule, "any ETF", $300,000, 200 trades, volume cap)
  - https://wghsinvcomp.smapply.us/res/p/faqs/ ($25 commission)
- **Vanguard:**
  - fact sheets https://fund-docs.vanguard.com/F0970.pdf, F0968.pdf, F3141.pdf, F0936.pdf, F3369.pdf, F0964.pdf
  - sector fact sheets F0958, F0957, F0955, F0951, F0953, F0959, F0954, F0956, F0986
  - product pages https://investor.vanguard.com/investment-products/etfs/profile/vti (and vt, vxus, vwo, voo, vea)
- **iShares:**
  - fact sheets https://www.ishares.com/us/literature/fact-sheet/{itot-ishares-core-s-p-total-u-s-stock-market-etf, ivv-ishares-core-s-p-500-etf, acwi-ishares-msci-acwi-etf, iefa-ishares-core-msci-eafe-etf, ixus-ishares-core-msci-total-international-stock-etf, iemg-ishares-core-msci-emerging-markets-etf, ewt-ishares-msci-taiwan-etf}-fund-fact-sheet-en-us.pdf
  - product pages https://www.ishares.com/us/products/239724/ (ITOT), 239726 (IVV), 239600 (ACWI), 244049 (IEFA), 244048 (IXUS), 244050 (IEMG), 239686 (EWT)
- **State Street:**
  - fact sheets https://www.ssga.com/us/en/intermediary/library-content/products/factsheets/etfs/us/factsheet-us-en-{spym,spy,xlk,xlf,xlv,xly,xlc,xli,xlp,xle,xlu,xlb,xlre}.pdf
  - daily holdings https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-{spym,splg,xlk,...}.xlsx (saved as CSV in `research/insight_v1/scripts/data/S2/`)
- **Refused:** https://www.schwabassetmanagement.com/products/schb (HTTP 403); invesco.com RSP pages (HTTP 406).
- **Repo files:**
  - `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf`, page 2
  - `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt`
  - `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, lines 43-45 and 68-74
- **Publisher facts:** https://www.harpercollins.ca/9780063067769/messy-roots-a-graphic-memoir-of-a-wuhanese-american/ ;
  https://newscorp.com/ ; https://en.wikipedia.org/wiki/Messy_Roots (secondary)
- **Snippets (UNVERIFIED):** WebSearch results for SCHB, SCHF, RSP and SPLG→SPYM (aaii.com, etfdb.com, miaxglobal.com,
  etf.com).

## What this teaches
Picking the growth fund is mostly about matching the fund to a forecast you actually use. It is less about hunting for
extra return. The U.S. vs world choice is worth about $2k to Laura's median outcome. Its larger effect is on how much
of her surplus rides on one theme: 40% of the S&P 500 against about 22% of the world index. The best check on any
"clever" tilt (Taiwan, equal weight, sectors, a media underweight) is to size it in dollars and see what it really
buys. Here each one turned out to be tiny, mislabeled, or an AI bet under another name.
