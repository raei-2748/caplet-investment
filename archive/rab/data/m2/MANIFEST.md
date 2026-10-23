# M2 extra data (WS4)

AI-generated data work (Claude Code) for Team Caplet. Read-only public GET; no login.

| File | What | Source | Retrieved | As of | sha256 | Status |
|---|---|---|---|---|---|---|
| `MOVE_yahoo_daily.csv` | ICE BofA MOVE index (1-month Treasury option implied normal volatility, bp a year), daily OHLC, 5,905 rows | Yahoo Finance `^MOVE` via `yfinance` 1.7.0, `auto_adjust=False`, start 2002-01-01 (first row 12 Nov 2002) | 2026-09-29 16:02 UTC = 12:02 EDT 29 Sep = 02:02 AEST 30 Sep 2026 | close of 28 Sep 2026 (the 29 Sep row is an intraday partial and is not used) | e68a0a7b03310346303d9d8613f059f481b3880bde30b85c73307a05878a3e3a | SECONDARY (ICE owns the index; Yahoo redistributes it). MOVE on 28 Sep 2026 = 101.82. Used only by M2 estimator E5 |

Not fetched: Shiller `ie_data` (Yale) and Damodaran `histret` - M2 needs only yields, and the daily Treasury/FRED
panel (1962-2026, `rab/data/treasury_par_*`, `rab/data/fred/`) already covers them at daily frequency.
