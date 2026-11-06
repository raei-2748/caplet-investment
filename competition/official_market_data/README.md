# Primary market data (downloaded by the team, 2026-09-27)

| File | Source | As of |
|---|---|---|
| `daily-treasury-rates_2026-09.csv` | U.S. Treasury, Daily Treasury Par Yield Curve Rates (home.treasury.gov) | 2026-09-01 to 2026-09-25 |
| `IEF_fact_sheet_2026-06-30.pdf` | iShares 7-10 Year Treasury Bond ETF fact sheet (ishares.com) | 2026-06-30 |
| `TLT_fact_sheet_2026-06-30.pdf` | iShares 20+ Year Treasury Bond ETF fact sheet (ishares.com) | 2026-06-30 |
| `JPM_LTCMA_2026_US_matrix_USD.pdf` | J.P. Morgan Asset Management 2026 LTCMA, USD assumption matrix | data as of 2025-09-30 |

Calculations from these files: `research/verified_2026-09-27/official_curve_pv.py`.
- `daily-treasury-rates_2026-10.csv`: treasury.gov daily par yield curve, October 2026 (downloaded 16 Oct 2026; latest row 15 Oct).
- `daily-treasury-rates_2026-11-05.csv`: treasury.gov daily par yield curve, 23 Oct to 5 Nov 2026 (read 6 Nov 2026 with
  the WebFetch tool, because curl to home.treasury.gov is refused by the session proxy). Rows 26 Oct to 4 Nov from the
  2026 CSV export; the 5 Nov row from the XML feed (`pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value_month=202611`),
  read twice with the same result; 23 Oct row identical to `daily-treasury-rates_2026-10-23.csv`; 10y for 29 Oct to 4 Nov
  matches FRED DGS10. Ten payments priced on it: `python keel/scripts/ladder_history.py <this file>` (5 Nov: $302,163).
