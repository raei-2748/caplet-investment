# U.S. Treasury Daily Par Yield Curve, 2000-2026 (to 28 Sep 2026)

- **What:** 27 yearly CSV files (`2000.csv` ... `2026.csv`), one row per trading day, par yields in percent
  (semiannual bond-equivalent), tenors 1 Mo to 30 Yr as published (some tenors are blank in some years, e.g. 20 Yr
  before 1993 is outside this range; 30 Yr is blank 2002-2006).
- **Source:** U.S. Department of the Treasury, Daily Treasury Par Yield Curve Rates,
  `https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/<YEAR>/all?type=daily_treasury_yield_curve&field_tdr_date_value=<YEAR>&page&_format=csv`
- **Provenance:** first downloaded by an earlier Claude Code session on 2026-09-29 (~15:03 AEST) into a /tmp scratch
  folder that is not backed up. Rescued here by WS1-inventory on 2026-09-30. Every file was re-downloaded from the
  URL above on 2026-09-30 at about 00:20 AEST and is **byte-identical** (27 of 27). Status: VERIFIED-PRIMARY.
- **Latest row:** 09/28/2026 (the 29 Sep curve was not yet published at the check time, 29 Sep 10:20 ET).
- **Used by:** `rab/rescued/ladder_history_2000_2026.py` (ladder cost on every curve since 2000).
