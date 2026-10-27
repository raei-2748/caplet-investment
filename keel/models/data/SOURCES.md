# Model Suite data sources (fetched Tue 27 Oct 2026 by `fetch_data.py`)

AI-generated (Claude Code). The primary sites (Yale/Shiller, FRED, BLS) are blocked by this container's proxy, so the
series come from the Frictionless Data mirrors on GitHub, which republish the primary files unchanged.

| File | Series | Primary source | Mirror fetched | Span |
|---|---|---|---|---|
| `shiller_monthly.csv` | S&P Composite price, dividend, CPI, long interest rate | Robert Shiller, Yale, "ie_data.xls" | https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv | Jan 1871 - Sep 2026 (dividends and CPI to mid-2023) |
| `cpi_us_monthly.csv` | US CPI-U all items | BLS CUUR0000SA0 | https://raw.githubusercontent.com/datasets/cpi-us/main/data/cpiai.csv | Jan 1913 - Aug 2026 |
| `twd_per_usd_monthly.csv` | Taiwan dollars per US dollar, monthly average | Federal Reserve H.10 (FRED EXTAUS) | https://raw.githubusercontent.com/datasets/exchange-rates/main/data/monthly.csv (Taiwan rows) | Oct 1983 - Sep 2026 |

Also used, already in the repo: the 22 Oct 2026 Treasury par curve (`keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv`)
and FRED GS10 monthly 1953-2026 (`keel/library/ips_numbers_2026-10/fred_GS10_monthly.csv`).
UNVERIFIED against the primary files this session (blocked); spot checks: Sep 2026 TWD 31.74 vs 31.82 on 18 Sep in
CLAUDE.md; the long rate matches FRED GS10 exactly in Jan 1980, Jan 2000, Jul 2020, Oct 2022 and Jun 2023 (the mirror's partial Jul-Sep 2023 rows differ, and the suite stops at Jun 2023).
