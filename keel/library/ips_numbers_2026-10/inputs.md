# Inputs and sources (IPS number sheet, 16 Oct 2026)

AI-generated (Claude Code) for Team Caplet.

| Input | Value | Source (retrieved 16 Oct 2026) |
|---|---|---|
| US Treasury par yield curve, 15 Oct 2026 | 1y 4.49, 2y 4.77, 5y 4.91, 7y 5.00, 10y 5.10, 20y 5.48, 30y 5.43 | treasury.gov daily par yield curve CSV, saved as `competition/official_market_data/daily-treasury-rates_2026-10.csv` (https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202610?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610&page&_format=csv) |
| US 10-year yield, monthly 1953-2026 | for rate volatility (12-month change sd 1.08 points) and the history replay | FRED series GS10, https://fred.stlouisfed.org/graph/fredgraph.csv?id=GS10, saved as `fred_GS10_monthly.csv` |
| Global stock return | 7.00% a year compound, 16.78% volatility | J.P. Morgan 2026 LTCMA, AC World (repo `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf`) |
| VT expense ratio | 0.06% | UNVERIFIED this session (Vanguard fact sheet value as widely published; check vanguard.com) |
| Holdings and coupons | IBTM-IBTR (Dec 2032-Dec 2036); T 4.75% Feb-2037, 4.50% May-2038, 4.375% Nov-2039, 4.25% Nov-2040, 3.125% Nov-2041 | WInS fills 7-8 Oct (`keel/routines/tasks/portfolio_check.py`) |
| Plan rules | IPS Version 5 (Google Doc "IPS Report", tab "Version 5") | `caplet/google_drive/ips_report/01_version_5.md` |
| Model choices | rates: parallel random walk, 1.0 point a year, floored at 0.25%; stocks independent of rates; 200,000 paths, seed 20261016 | `ips_numbers.py` |
