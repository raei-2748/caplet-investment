# RAB data snapshot (WS1-data)

Fetched 29 Sep 2026, about 10:30-11:15 ET (30 Sep 2026, about 00:30-01:15 AEST), by `rab/data/fetch_snapshot.py`
(read-only public GETs; re-run it to refresh). Per-file SHA-256, bytes, URL, retrieval time (UTC, ET, Sydney) and
as-of date are in `MANIFEST.csv`. AI-generated data work (Claude Code) for Team Caplet.

| Folder | What | Source (URL) | As of | Status |
|---|---|---|---|---|
| `treasury_par_2000_2026/` | Daily Treasury Par Yield Curve, one CSV per year | home.treasury.gov `.../daily-treasury-rates.csv/<YEAR>/all?type=daily_treasury_yield_curve&field_tdr_date_value=<YEAR>&page&_format=csv` | last row **28 Sep 2026** | VERIFIED-PRIMARY. All 27 files re-fetched and byte-identical to the rescued copies |
| `treasury_par_1990_1999/` | Same series, 1990-1999 (1990 is the first year of the daily par series) | same URL pattern | 2 Jan 1990 .. 31 Dec 1999 | VERIFIED-PRIMARY (new) |
| `fred/DGS*.csv` | Constant-maturity yields 1M ... 30Y, full history (fallback and cross-check) | `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>` | last value 25 Sep 2026 (FRED lags a day) | VERIFIED-PRIMARY; the 25 Sep values equal the Treasury 25 Sep row |
| `etf/yfinance_daily_6mo.csv` | Daily OHLCV, 14 ETFs (+ Yahoo's "IBTN", not the WInS security) | Yahoo Finance via `yfinance`, `auto_adjust=False` | 30 Mar - 29 Sep 2026; **29 Sep is a partial session** | Secondary |
| `etf/nasdaq_historical.json` | Daily close and consolidated volume, 14 ETFs | `https://api.nasdaq.com/api/quote/<T>/historical?assetclass=etf...` | to 28 Sep 2026 | Primary for volume |
| `etf/etf_summary_2026-09-28.csv` | Close (WInS / Nasdaq / Yahoo / iShares), 28 Sep volume, 20- and 30-session average, 20-session median and minimum | derived offline | 28 Sep 2026 | The 20-session mean equals iShares' "30 Day Avg. Volume" exactly (IBTM, IBTO, IBTR) |
| `ishares/` | iBonds product pages (gzipped) and parsed facts: NAV, close, shares outstanding, net assets, avg YTM, duration, WAM | ishares.com product pages (URLs in the CSV) | 28 Sep 2026 | VERIFIED-PRIMARY |
| `sheet/` | Sheet `1EHCJxbFI0UOzNOpOWvDfzNqbK45qWuopZcL7HNN3VPM` tabs Portfolio (CSV), Book L and WInS Notes (page text) | read-only through the logged-in Chrome browser (gviz endpoint) | Sheet at 29 Sep 10:30 ET | SEEN 30 Sep. ETF prices in these tabs are **live** GOOGLEFINANCE values (29 Sep intraday), not 28 Sep closes |
| `wins/wins_prices_2026-09-28.csv` | WInS 28 Sep prices used by M1: ETF closes, bond clean + recorded accrued, CUSIP, Book L sizes, SEEN/UNVERIFIED per row | hand-built from `sheet/`, `ishares/`, MSPD Table V and rab/premortem.md PM-04 | 28 Sep 2026 | Mixed: see each row |

## What could not be fetched, and what replaced it

- **Google Sheets and Drive connectors** refused the credential ("can't be used with the current credential"), so the
  Sheet was read through the browser. The first attempt (CSV export URL) made Chrome save the Portfolio tab as
  `~/Downloads/data.csv` (3,767 bytes, 30 Sep 00:30 AEST). It is copied unchanged into `sheet/`; the file in Downloads
  can be deleted. Book L and WInS Notes were then read as HTML pages (no download).
- **Longbridge MCP** refused the credential; prices come from Nasdaq (primary), Yahoo (secondary) and iShares.
- **iShares holdings CSVs** return the product page to curl, so iBond holdings stay the 24 Sep snapshot
  (`research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv`). Its dates do not line up with the 28 Sep share
  counts for IBTM and IBTR (M1 [D]); M1 scales the look-through to the published NAV.
- **Stooq** needs a JavaScript bot check; not used.
- **WInS**: no login (ground rule). WInS names are known only for the tickers in tab WInS Notes; the exact WInS
  strings for IBTO-IBTR and all five bonds, the bond quantity unit and the accrued WInS charges are UNVERIFIED.

## Notes for later streams

- Ticket prices must come from WInS on the trade day (PM-29). These files size and check; they do not price orders.
- Volume: use `avg_volume_20d`, `median_volume_20d` and `min_volume_20d` from the summary (complete sessions only).
- The par curve for 29 Sep publishes after the U.S. close; for Friday, re-run `fetch_snapshot.py T` and
  `rab/models/m1_ladder.py --curve-date <date>`.
