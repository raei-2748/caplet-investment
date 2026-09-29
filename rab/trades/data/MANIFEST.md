# rab/trades/data: extra inputs fetched by WS6 (read-only public GETs)

| File | Source (URL) | Retrieved | As of | sha256 |
|---|---|---|---|---|
| `mspd_table5_2026-08-31.json` | https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_5?filter=record_date:eq:2026-08-31&page[size]=500 (U.S. Treasury, Monthly Statement of the Public Debt, Table V: every strippable note and bond) | 2026-09-29 ~16:00 UTC (30 Sep ~02:00 AEST) | record date 31 Aug 2026 | 9fc0263d44902dd9db0538acd65175a1367f08a217c3693d04468c2f017aaf2d |
| `ibtl_nasdaq_historical_2026-09-30.json` | https://api.nasdaq.com/api/quote/IBTL/historical?assetclass=etf&fromdate=2026-06-01&limit=200&todate=2026-09-30 | 2026-09-29 16:07 UTC (30 Sep 02:07 AEST) | last complete session 28 Sep 2026 (the 29 Sep row is a partial session) | b9658e88e49cfcb9427e65b37d297a2dc08a5be69f73e261d48147f5410c2453 |
| `ishares_ibonds_treasury_list_2026-09-30.csv` | https://www.ishares.com/us/product-screener/product-screener-v3.1.jsn?dcrPath=/templatedata/config/product-screener-v3/data/en/us-ishares/ishares-product-screener-backend-config&siteEntryPassthrough=true (iShares US product screener; extract of every iBonds Term Treasury fund; full response sha256 8f60ffe0...be013, not committed) | 2026-09-29 ~16:34 UTC (30 Sep ~02:34 AEST), WS6-notes | NAV as of 28 Sep 2026 | f62a7baa9722673aa4037440a6ed11dc82e5a0c23a011edcde899cb97738d9a8 |

Why: M9 needs every Treasury **bond** (CUSIP 912810..., the 20- and 30-year issues) maturing 2031-2042, including the
low-coupon 2040-2041 issues that the 2032+ extract in `research/insight_v1/wins_now/` does not flag, and the
volume of IBTL (iShares iBonds Dec 2031, a floor runner-up). Nasdaq's quote page names IBTL "iShares iBonds Dec 2031
Term Treasury ETF" (30 Sep 2026). None of this says what WInS lists; WInS names stay UNVERIFIED until seen.

Observation (from the MSPD file, not from WInS): the Treasury-bond class has no issue maturing between
15 Feb 2031 (5.375%, 912810FP8) and 15 Feb 2036 (4.5%, 912810FT0). That is exactly the gap the team saw in the WInS
bond drop-down on 29 Sep (tab `WInS Notes`). So WInS probably lists bonds of this class. If so, the low-coupon issues
1.375% 15-Nov-2040 (912810ST6) and 2.000% 15-Nov-2041 (912810TC2) may be listed too. UNVERIFIED: check the drop-down.

WS6-notes (30 Sep): the iShares list has Treasury iBonds ending Dec 2026 ... Dec 2036, then Dec 2044. None ends
Dec 2037 to Dec 2043, so the 2038-2042 payments need individual bonds (confirms insight_v1 S1 item 6, 27 Sep).
