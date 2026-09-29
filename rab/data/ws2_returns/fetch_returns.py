"""WS2 return-history snapshot for M3 (branch Monte Carlo), M4 (cap optimiser) and M8 (sensitivity).

Read-only public GETs, no logins. Downloads two raw files into rab/data/ws2_returns/raw/ and writes
rab/data/ws2_returns/MANIFEST.csv (same columns as rab/data/MANIFEST.csv). Raw files are never edited;
build_returns.py turns them into tidy CSVs.

Sources
  [S] Robert J. Shiller, "U.S. Stock Markets 1871-Present and CAPE Ratio" (ie_data.xls): monthly S&P composite price,
      dividend, CPI, GS10 and real total-return price from Jan 1871. Current copy linked from https://shillerdata.com/
      (Shiller's data page; the old Yale URL http://www.econ.yale.edu/~shiller/data/ie_data.xls serves an older copy).
  [D] Aswath Damodaran, "Historical Returns on Stocks, Bonds and Bills: 1928-2025" (histretSP.xls, NYU Stern),
      https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html (cross-check only).

The same two URLs are fetched by WS3 (rab/ws3: rab/data/history/fetch_history.py). On 30 Sep 2026 the bytes were
identical (SHA-256 recorded in the manifest), so the two streams use the same data.

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/data/ws2_returns/fetch_returns.py
"""
import csv
import hashlib
import os
import subprocess
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "raw")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
SOURCES = [
    ("raw/shiller_ie_data.xls",
     "https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/"
     "70fec4f5-727f-4e53-b5f1-179af109c5fa/ie_data.xls?ver=1788371540009",
     "monthly Jan 1871 - Sep 2026 (Sep 2026 price = 1 Sep close; recent CPI estimated by Shiller)",
     "Shiller ie_data.xls, current copy linked from https://shillerdata.com/ (VERIFIED-PRIMARY)"),
    ("raw/damodaran_histretSP.xls", "https://pages.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls",
     "annual 1928-2025 (page dated January 2026)", "Damodaran histretSP.xls, NYU Stern (VERIFIED-PRIMARY)"),
]


def stamp():
    t = datetime.now(timezone.utc)
    return (t.strftime("%Y-%m-%dT%H:%M:%SZ"), t.astimezone(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M %Z"),
            t.astimezone(ZoneInfo("Australia/Sydney")).strftime("%Y-%m-%d %H:%M %Z"))


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    os.makedirs(RAW, exist_ok=True)
    rows = []
    for rel, url, as_of, note in SOURCES:
        out = os.path.join(ROOT, rel)
        subprocess.run(["curl", "-s", "-L", "--fail", "--max-time", "180", "-A", UA, "-o", out, url], check=True)
        u, e, s = stamp()
        rows.append([rel, sha(out), os.path.getsize(out), url, u, e, s, as_of, note])
        print(rel, rows[-1][1], rows[-1][2])
    with open(os.path.join(ROOT, "MANIFEST.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file", "sha256", "bytes", "url", "retrieved_utc", "retrieved_et", "retrieved_sydney", "as_of", "note"])
        w.writerows(rows)


if __name__ == "__main__":
    main()
