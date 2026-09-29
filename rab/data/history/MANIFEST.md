# WS3 history snapshot (M5, M6, M7)

Fetched 30 Sep 2026 about 02:00 AEST (29 Sep 2026 about 12:00 EDT) by `fetch_history.py` (read-only public GETs).
Per-file SHA-256, bytes, URL, retrieval time (UTC, ET, Sydney) and as-of range: `MANIFEST.csv`. Tidy inputs are built
offline by `build_history.py`; its overlap checks are in `build_checks.txt`. AI-generated data work (Claude Code) for
Team Caplet. Environment note: `xlrd==2.0.2` was added to the shared env (`uv pip install`) to read the `.xls` files.

| Raw file | Source | Used for | Status |
|---|---|---|---|
| `shiller_ie_data.xls` | Robert Shiller, U.S. Stock Markets 1871-Present, via https://shillerdata.com/ (monthly to Sep 2026; recent CPI months estimated by Shiller) | GS10 1871-1961 (flat curves), CPI (Dec to Dec) | Primary. Identical to the Yale copy on 1,788 common months before 2020 |
| `shiller_ie_data_yale.xls` | http://www.econ.yale.edu/~shiller/data/ie_data.xls | cross-check only | Primary (older copy) |
| `damodaran_histretSP.xls` | A. Damodaran, https://pages.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls (page dated Jan 2026) | U.S. stocks, T-bills, 10-year bonds, gold, home prices 1928-2025 | Primary (compiled) |
| `JSTdatasetR6.xlsx` | Jorda-Schularick-Taylor Macrohistory Database R6, https://www.macrohistory.net/database/ | U.S. 1871-1927; 16 non-U.S. countries (world ex-U.S.); Japan | Primary (academic) |
| `kf_*.zip` | Kenneth French Data Library, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html (CRSP/Bloomberg Aug 2026 builds) | U.S. market and small-value; developed ex-U.S. (1991-); emerging (1990-) | Primary (academic) |
| `fred_*.csv` | FRED, https://fred.stlouisfed.org/series/<ID> | CPI, breakevens (T5YIE, T10YIE, T5YIFR), TIPS yields (DFII*), Cleveland Fed expected inflation (EXPINF*) | Primary |
| `yf_*.csv` | Yahoo Finance via `yfinance` (auto_adjust=False) | S&P 500 around the three downgrades; VT, VTI, VXUS, GLD, VNQ, SPY adjusted closes 2008-2026 | Secondary |

Derived: `annual_history.csv` (calendar-year returns and inflation 1871-2025; sources per column in the
`build_history.py` docstring), `soy_curves.csv` (par yields on the first trading day of each year 1871-2026),
`daily_curves_1962_1989.csv` (FRED DGS in the par-file layout), `shiller_monthly.csv`, `jst_countries_usd.csv`,
`jpm_ltcma_2026_usd.csv` + `jpm_ltcma_2026_corr.csv` (parsed from the repo PDF
`competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf`, page 2, data as of 30 Sep 2025),
`market_inflation_2026-09.csv` (latest value of each inflation series).

## Known limits (state them wherever the history is used)

- Before 1962 only one Treasury yield exists (Shiller's long rate): the curve is flat at it. On 1962-2026 this
  overstates the ladder cost by a median 0.8% (5th-95th percentile -0.8% to +2.1%; `rab/results/M5/check_flat_vs_full_curve.csv`).
- World stocks ex-U.S. = 16 JST countries weighted by real GDP (Maddison GDP per head x population), in U.S. dollars;
  no emerging markets before 1990; Canada and Ireland have no JST equity series. JST's nominal GDP cannot weight
  countries (its units differ by country); a first build that used it was wrong and was replaced (ex-U.S. 1991-2020
  now 6.84% a year vs Ken French 6.37%, correlation 0.95).
- The "VT-like" world mix keeps today's 62% U.S. weight in every year; in 2009-2025 it beat actual VT by about
  1.1 points a year (VT held less U.S. then).
- U.S. returns before 1928 are JST's (their U.S. equity series tracks Damodaran's 1928-2020 with correlation 0.975).
- JST's Japan series are annual as published (its 1990 equity return is -13%, milder than the calendar-year Topix fall).
- REIT history: Nareit's site blocks scripted downloads (JavaScript challenge); no REIT index before VNQ (2004). The
  M6 history lens uses Damodaran's home-price series as a labelled stand-in; the ETF lens uses VNQ.
- Damodaran's gold is annual-average prices before 1970 (the gold price was fixed before 1971).
