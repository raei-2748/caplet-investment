"""D3_data_snapshot.py - download and freeze the public data series used by the D3 (Quant Modeler) scripts.

What it does (plain English): fetches three public data sets through the environment's proxy (curl), parses them,
and writes small CSV snapshots under research/insight_v1/scripts/data/D3/ so every D3 number can be re-run later
even if a site changes. It prints a short summary of each file.

Inputs (status labels):
- Damodaran, "Historical Returns on Stocks, Bonds and Bills: 1928-2024" (page dated January 2026; rows run to 2025),
  https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html  -> VERIFIED-PRIMARY (the dataset's own
  page, NYU Stern; it is a compiled dataset: S&P 500 incl. dividends, 3-month T-bill (yearly average rate), 10-year
  U.S. Treasury bond total return, Baa corporate bonds, real estate, gold). Accessed 2026-09-28.
- U.S. Treasury Daily Par Yield Curve Rates, 2026 (all dates to 2026-09-25),
  https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
  -> VERIFIED-PRIMARY, accessed 2026-09-28 (its 09/25/2026 row equals the repo file
  competition/official_market_data/daily-treasury-rates_2026-09.csv, VERIFIED-REPO-FILE).
- FRED (Federal Reserve Bank of St. Louis; source: Board of Governors H.15) daily constant-maturity yields DGS2, DGS5,
  DGS10, https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10 (etc.) -> VERIFIED-PRIMARY, accessed 2026-09-28.

Outputs: data/D3/damodaran_histretSP_1928_2025.csv, data/D3/treasury_par_2026_raw.csv, data/D3/fred_DGS{2,5,10}.csv.
Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D3_data_snapshot.py  [--offline]
(--offline only re-parses files already saved.)
"""
import csv
import html
import os
import re
import subprocess
import sys

OUT = "research/insight_v1/scripts/data/D3"
DAMODARAN = "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html"
TREASURY = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/"
            "all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv")
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"


def curl(url, path):
    r = subprocess.run(["curl", "-sSL", "--http1.1", "--retry", "3", "-m", "120", "-A", "Mozilla/5.0", "-o", path, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip().startswith("2"):
        sys.exit(f"download failed: {url} ({r.stdout} {r.stderr})")


def parse_damodaran(raw_html):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw_html, flags=re.S | re.I)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    toks = [x for x in (re.sub(r"\s+", " ", l).strip() for l in t.split("\n")) if x]
    rows, i = {}, 0
    pct = re.compile(r"-?\d+\.\d+%")
    while i < len(toks):
        if re.fullmatch(r"(19[2-9]\d|20[0-2]\d)", toks[i]) and i + 7 < len(toks) and all(
                pct.fullmatch(toks[i + k]) for k in range(1, 8)):
            y = int(toks[i])
            rows.setdefault(y, [float(toks[i + k].rstrip("%")) / 100 for k in range(1, 8)])
            i += 8
        else:
            i += 1
    return rows


def main():
    os.makedirs(OUT, exist_ok=True)
    offline = "--offline" in sys.argv
    raw = os.path.join(OUT, "_damodaran_raw.html")
    if not offline:
        curl(DAMODARAN, raw)
        curl(TREASURY, os.path.join(OUT, "treasury_par_2026_raw.csv"))
        for s in ("DGS2", "DGS5", "DGS10"):
            curl(FRED.format(s), os.path.join(OUT, f"fred_{s}.csv"))
    out_csv = os.path.join(OUT, "damodaran_histretSP_1928_2025.csv")
    cols = ["year", "sp500_tr", "us_smallcap_bottom_decile", "tbill_3m_avg", "tbond_10y_tr", "baa_corp_tr",
            "real_estate", "gold"]
    if os.path.exists(raw):          # parse the freshly downloaded page, then drop the 650 KB raw file
        rows = parse_damodaran(open(raw, "rb").read().decode("latin-1"))
        with open(out_csv, "w", newline="") as f:
            f.write(f"# source: {DAMODARAN} (page dated January 2026), accessed 2026-09-28; "
                    "VERIFIED-PRIMARY dataset page\n")
            w = csv.writer(f)
            w.writerow(cols)
            for y in sorted(rows):
                w.writerow([y] + [f"{v:.4f}" for v in rows[y]])
        os.remove(raw)
    rows = {int(r["year"]): [float(r[c]) for c in cols[1:]]
            for r in csv.DictReader(l for l in open(out_csv) if not l.startswith("#"))}
    print(f"Damodaran: {len(rows)} years {min(rows)}-{max(rows)}; 2008 S&P {rows[2008][0]:+.2%}, "
          f"10y bond {rows[2008][3]:+.2%}; 2022 S&P {rows[2022][0]:+.2%}, 10y bond {rows[2022][3]:+.2%}")
    tr = list(csv.DictReader(open(os.path.join(OUT, "treasury_par_2026_raw.csv"))))
    print(f"Treasury 2026 curve: {len(tr)} dates, {tr[-1]['Date']} to {tr[0]['Date']}")
    for s in ("DGS2", "DGS5", "DGS10"):
        fr = list(csv.DictReader(open(os.path.join(OUT, f"fred_{s}.csv"))))
        print(f"FRED {s}: {len(fr)} rows, {fr[0]['observation_date']} to {fr[-1]['observation_date']}")


if __name__ == "__main__":
    main()
