"""AI-generated (Claude Code), Tue 27 Oct 2026. Fetches the historical series the Model Suite runs on.
Primary sites (Shiller's Yale page, FRED, BLS) are blocked by this container's proxy, so the series come from the
Frictionless Data mirrors on GitHub, which republish them unchanged. Sources and dates are written to SOURCES.md.
Run from repo root: .venv/bin/python keel/models/data/fetch_data.py
"""
import csv, io, pathlib, urllib.request
HERE = pathlib.Path(__file__).parent
GET = lambda u: urllib.request.urlopen(u, timeout=60).read().decode()

# 1. Shiller monthly (S&P Composite price, dividend, CPI, long rate), 1871 on
spx = GET("https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv")
(HERE / "shiller_monthly.csv").write_text(spx)
# 2. US CPI-U all items, monthly, 1913 on (BLS CUUR0000SA0)
(HERE / "cpi_us_monthly.csv").write_text(GET("https://raw.githubusercontent.com/datasets/cpi-us/main/data/cpiai.csv"))
# 3. Taiwan dollars per US dollar, monthly average (FRED EXTAUS/H.10), 1983 on: keep Taiwan only
fx = list(csv.DictReader(io.StringIO(GET("https://raw.githubusercontent.com/datasets/exchange-rates/main/data/monthly.csv"))))
with open(HERE / "twd_per_usd_monthly.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["Date", "TWD_per_USD"])
    for r in fx:
        if r["Country"] == "Taiwan" and r["Exchange rate"]:
            w.writerow([r["Date"], r["Exchange rate"]])
print("ok")
