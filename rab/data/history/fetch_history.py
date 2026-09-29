"""WS3 history snapshot: long-run returns, yields and inflation for M5 (century backtest), M6 (rivals) and M7 (stress).

Read-only public GETs, no logins. Writes the raw files into rab/data/history/raw/ and a manifest
rab/data/history/MANIFEST.csv (file, sha256, bytes, url, retrieved UTC / ET / Sydney, as_of, note), same columns as
rab/data/MANIFEST.csv. Raw files are never edited; rab/data/history/build_history.py turns them into tidy CSVs.

Sources
  [S] Robert Shiller, "U.S. Stock Markets 1871-Present and CAPE Ratio" (ie_data.xls): monthly S&P composite price,
      dividend, CPI, 10-year Treasury rate (GS10) from 1871. Current copy from shillerdata.com (Shiller's site);
      the older Yale copy is fetched too, as a cross-check only.
  [D] Aswath Damodaran, "Historical Returns on Stocks, Bonds and Bills" (histretSP.xls, NYU Stern), annual 1928-2025.
  [J] Jorda-Schularick-Taylor Macrohistory Database, release 6 (JSTdatasetR6.xlsx): 18 countries, annual 1870-2020;
      equity total return, long rate, CPI, exchange rate, GDP (for the world and Japan series).
  [K] Kenneth French Data Library: U.S. market and risk-free (1926-), U.S. 6 size/value portfolios (1926-),
      Developed and Developed ex-U.S. 3 factors (1990-), Emerging 5 factors (1989-).
  [F] FRED: CPI (1913-), breakeven inflation, TIPS real yields, Cleveland Fed expected inflation.
  [Y] Yahoo Finance via yfinance (auto_adjust=False): S&P 500 index daily (downgrade windows) and monthly adjusted
      closes of VT, VTI, VXUS, GLD, VNQ (real fund returns since inception).

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/data/history/fetch_history.py
"""
import csv
import hashlib
import os
import subprocess
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "raw")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
KF = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/{}"
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"

SOURCES = [
    # (file, url, use_browser_ua, as_of, note)
    ("shiller_ie_data.xls",
     "https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/70fec4f5-727f-4e53-b5f1-179af109c5fa/ie_data.xls?ver=1788371540009",
     True, "see file (monthly, 1871-)", "Shiller ie_data.xls, current copy linked from https://shillerdata.com/ (primary)"),
    ("shiller_ie_data_yale.xls", "http://www.econ.yale.edu/~shiller/data/ie_data.xls", True, "see file",
     "older Yale copy; cross-check only"),
    ("damodaran_histretSP.xls", "https://pages.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls", True,
     "annual 1928-2025 (page dated January 2026)", "Damodaran histretSP.xls (NYU Stern)"),
    ("JSTdatasetR6.xlsx", "https://www.macrohistory.net/app/download/9834512569/JSTdatasetR6.xlsx?t=1763503850", True,
     "annual 1870-2020", "Jorda-Schularick-Taylor Macrohistory Database R6 (macrohistory.net/database)"),
    ("kf_F-F_Research_Data_Factors_CSV.zip", KF.format("F-F_Research_Data_Factors_CSV.zip"), True, "monthly+annual 1926-",
     "Ken French: U.S. Mkt-RF, SMB, HML, RF"),
    ("kf_6_Portfolios_2x3_CSV.zip", KF.format("6_Portfolios_2x3_CSV.zip"), True, "monthly+annual 1926-",
     "Ken French: U.S. 6 portfolios size x book-to-market (value-weighted)"),
    ("kf_Developed_3_Factors_CSV.zip", KF.format("Developed_3_Factors_CSV.zip"), True, "monthly+annual 1990-07-",
     "Ken French: developed markets Mkt-RF, RF (USD)"),
    ("kf_Developed_ex_US_3_Factors_CSV.zip", KF.format("Developed_ex_US_3_Factors_CSV.zip"), True,
     "monthly+annual 1990-07-", "Ken French: developed ex-U.S. Mkt-RF, RF (USD)"),
    ("kf_Emerging_5_Factors_CSV.zip", KF.format("Emerging_5_Factors_CSV.zip"), True, "monthly+annual 1989-07-",
     "Ken French: emerging markets Mkt-RF, RF (USD)"),
]
FRED_SERIES = ["CPIAUCNS", "T5YIE", "T10YIE", "T5YIFR", "DFII5", "DFII7", "DFII10", "DFII20", "DFII30",
               "EXPINF5YR", "EXPINF10YR", "EXPINF20YR", "EXPINF30YR", "GS10"]
YF_DAILY = ["^GSPC"]
YF_MONTHLY = ["VT", "VTI", "VXUS", "GLD", "VNQ", "SPY"]


def now():
    t = datetime.now(timezone.utc)
    return (t.strftime("%Y-%m-%dT%H:%M:%SZ"), t.astimezone(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M %Z"),
            t.astimezone(ZoneInfo("Australia/Sydney")).strftime("%Y-%m-%d %H:%M %Z"))


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def curl(url, out, browser_ua):
    cmd = ["curl", "-s", "-L", "--fail", "--max-time", "180", "-o", out, url]
    if browser_ua:
        cmd[1:1] = ["-A", UA]
    subprocess.run(cmd, check=True)


def main():
    os.makedirs(RAW, exist_ok=True)
    rows = []
    for fn, url, ua, as_of, note in SOURCES:
        out = os.path.join(RAW, fn)
        curl(url, out, ua)
        utc, et, syd = now()
        rows.append([f"raw/{fn}", sha(out), os.path.getsize(out), url, utc, et, syd, as_of, note])
        print(f"{fn:42s} {os.path.getsize(out):>10,} bytes")
    for s in FRED_SERIES:
        out = os.path.join(RAW, f"fred_{s}.csv")
        curl(FRED.format(s), out, False)          # FRED refuses the browser user agent; plain curl works
        utc, et, syd = now()
        with open(out) as f:
            lines = [l for l in f.read().splitlines() if l.strip()]
        last = next((l for l in reversed(lines) if l.split(",")[-1] not in ("", ".")), "")
        rows.append([f"raw/fred_{s}.csv", sha(out), os.path.getsize(out), FRED.format(s), utc, et, syd,
                     f"{lines[1].split(',')[0]}..{last.split(',')[0]} (last non-blank)", "FRED (St. Louis Fed)"])
        print(f"fred_{s:36s} last {last}")
    import yfinance as yf                      # read-only market data; auto_adjust=False keeps Close and Adj Close
    for t in YF_DAILY:
        df = yf.download(t, start="2011-06-01", end="2026-09-30", interval="1d", auto_adjust=False, progress=False)
        fn = f"yf_{t.replace('^', '')}_daily.csv"
        df.to_csv(os.path.join(RAW, fn))
        utc, et, syd = now()
        rows.append([f"raw/{fn}", sha(os.path.join(RAW, fn)), os.path.getsize(os.path.join(RAW, fn)),
                     f"yfinance.download('{t}', start='2011-06-01', interval='1d', auto_adjust=False)", utc, et, syd,
                     f"to {df.index[-1].date()}", "Yahoo Finance; secondary source; downgrade windows only"])
    df = yf.download(YF_MONTHLY, start="2008-06-01", end="2026-09-30", interval="1mo", auto_adjust=False,
                     progress=False)
    fn = "yf_funds_monthly.csv"
    df.to_csv(os.path.join(RAW, fn))
    utc, et, syd = now()
    rows.append([f"raw/{fn}", sha(os.path.join(RAW, fn)), os.path.getsize(os.path.join(RAW, fn)),
                 f"yfinance.download({YF_MONTHLY}, start='2008-06-01', interval='1mo', auto_adjust=False)", utc, et,
                 syd, f"to {df.index[-1].date()}", "Yahoo Finance; Adj Close = total-return proxy; secondary source"])
    with open(os.path.join(ROOT, "MANIFEST.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file", "sha256", "bytes", "url", "retrieved_utc", "retrieved_et", "retrieved_sydney", "as_of",
                    "note"])
        w.writerows(rows)
    print(f"manifest: {len(rows)} files")


if __name__ == "__main__":
    sys.exit(main())
