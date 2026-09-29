"""RAB data snapshot (WS1-data). Read-only public market data -> rab/data/, plus a manifest.

What it fetches (all read-only GETs, no logins):
  [T] U.S. Treasury Daily Par Yield Curve, every year 1990-2026 (1990 is the first year of the daily par series).
      1990-1999 -> treasury_par_1990_1999/; 2000-2026 are compared with the rescued files in treasury_par_2000_2026/
      (never overwritten; a changed file is saved next to them as <year>_refetch_<stamp>.csv and flagged).
  [F] FRED constant-maturity Treasury yields DGS1MO ... DGS30 (fallback / cross-check), full history -> fred/.
  [E] ETF daily prices and volume from Yahoo via yfinance (auto_adjust=False, so Close is the traded close) and a
      second source (Nasdaq quote API) for the same tickers -> etf/.
  [I] iShares product pages for the iBond ETFs (NAV, closing price, shares outstanding, net assets, yields,
      duration) -> ishares/ (raw pages gzipped + parsed facts CSV).
Writes MANIFEST.csv (file, sha256, bytes, URL, retrieved UTC and Sydney, as-of date) and prints a summary.

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/data/fetch_snapshot.py
Sheet copies (tab Portfolio / Book L / WInS Notes) and WInS bond prices are NOT fetched here: they are hand-recorded
in rab/data/sheet/ and rab/data/wins/ (see MANIFEST.md for how each was obtained).
"""
import csv
import gzip
import hashlib
import html
import io
import json
import os
import re
import subprocess
import statistics as st
import sys
import time
from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
TSY = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{y}/all"
       "?type=daily_treasury_yield_curve&field_tdr_date_value={y}&page&_format=csv")
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}"
FRED_SERIES = ["DGS1MO", "DGS3MO", "DGS6MO", "DGS1", "DGS2", "DGS3", "DGS5", "DGS7", "DGS10", "DGS20", "DGS30"]
NASDAQ = ("https://api.nasdaq.com/api/quote/{t}/historical?assetclass=etf&fromdate={a}&limit=200&todate={b}")
TICKERS = ["IBTM", "IBTO", "IBTP", "IBTQ", "IBTR", "VT", "VTI", "VXUS", "ACWI", "IEF", "TLH", "VGIT", "SPTI", "SGOV"]
ISHARES = {
    "IBTM": "https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf",
    "IBTO": "https://www.ishares.com/us/products/332291/ishares-ibonds-dec-2033-term-treasury-etf",
    "IBTP": "https://www.ishares.com/us/products/337745/ishares-ibonds-dec-2034-term-treasury-etf",
    "IBTQ": "https://www.ishares.com/us/products/342105/ishares-ibonds-dec-2035-term-treasury-etf",
    "IBTR": "https://www.ishares.com/us/products/350028/ishares-ibonds-dec-2036-term-treasury-etf",
}
MANIFEST = []


def now():
    t = datetime.now(timezone.utc)
    return t.strftime("%Y-%m-%dT%H:%M:%SZ"), t.astimezone(ZoneInfo("Australia/Sydney")).strftime("%Y-%m-%d %H:%M %Z")


def et_of(utc):
    t = datetime.strptime(utc, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return t.astimezone(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M %Z")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def curl(url, accept=None, tries=4, browser_ua=True):
    """browser_ua=False sends curl's default user agent (FRED times out on a browser UA without JavaScript)."""
    cmd = ["curl", "-sSL", "--http1.1", "-m", "120"] + (["-A", UA] if browser_ua else []) + ["-w", "\n%{http_code}", url]
    if accept:
        cmd[1:1] = ["-H", f"Accept: {accept}"]
    for k in range(tries):
        r = subprocess.run(cmd, capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code.startswith(b"2"):
            return body
        time.sleep(3 * (k + 1))
    raise RuntimeError(f"FETCH FAILED {url}: curl {r.returncode} HTTP {code!r} {r.stderr[:200]!r}")


def record(path, url, asof, note=""):
    b = open(path, "rb").read()
    utc, syd = now()
    MANIFEST.append({"file": os.path.relpath(path, ROOT), "sha256": sha(b), "bytes": len(b), "url": url,
                     "retrieved_utc": utc, "retrieved_et": et_of(utc), "retrieved_sydney": syd, "as_of": asof,
                     "note": note})


def last_row_date_treasury(b):
    rows = list(csv.DictReader(io.StringIO(b.decode())))
    ds = [datetime.strptime(r["Date"], "%m/%d/%Y").date() for r in rows]
    return max(ds), min(ds), len(rows)


def fetch_treasury():
    os.makedirs(f"{ROOT}/treasury_par_1990_1999", exist_ok=True)
    out = []
    for y in range(1990, 2027):
        url = TSY.format(y=y)
        b = curl(url)
        hi, lo, n = last_row_date_treasury(b)
        if y < 2000:
            p = f"{ROOT}/treasury_par_1990_1999/{y}.csv"
            open(p, "wb").write(b)
            record(p, url, f"{lo}..{hi} ({n} rows)")
            out.append((y, "new", n, hi))
            continue
        p = f"{ROOT}/treasury_par_2000_2026/{y}.csv"
        old = open(p, "rb").read()
        if old == b:
            record(p, url, f"{lo}..{hi} ({n} rows)", "re-fetched now: byte-identical to the rescued file")
            out.append((y, "identical", n, hi))
        else:
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
            p2 = f"{ROOT}/treasury_par_2000_2026/{y}_refetch_{stamp}.csv"
            open(p2, "wb").write(b)
            record(p2, url, f"{lo}..{hi} ({n} rows)", f"DIFFERS from rescued {y}.csv (kept); new rows or revisions")
            out.append((y, "CHANGED", n, hi))
    return out


def fetch_fred():
    os.makedirs(f"{ROOT}/fred", exist_ok=True)
    out = []
    for s in FRED_SERIES:
        url = FRED.format(s=s)
        try:
            b = curl(url, browser_ua=False, tries=2)
        except RuntimeError as e:
            out.append((s, "FAILED", str(e)[:120], ""))
            continue
        p = f"{ROOT}/fred/{s}.csv"
        open(p, "wb").write(b)
        rows = [r for r in csv.reader(io.StringIO(b.decode()))][1:]
        vals = [r for r in rows if r[1] not in ("", ".")]
        record(p, url, f"{rows[0][0]}..{vals[-1][0]} (last non-blank)")
        out.append((s, rows[0][0], vals[-1][0], vals[-1][1]))
    return out


def fetch_etf():
    import yfinance as yf
    os.makedirs(f"{ROOT}/etf", exist_ok=True)
    d = yf.download(TICKERS + ["IBTN"], period="6mo", interval="1d", auto_adjust=False, progress=False,
                    group_by="ticker", threads=False)
    rows = []
    for t in TICKERS + ["IBTN"]:
        if t not in d.columns.get_level_values(0):
            continue
        sub = d[t].dropna(how="all")
        for idx, r in sub.iterrows():
            rows.append({"ticker": t, "date": idx.date().isoformat(), **{k.lower().replace(" ", "_"): r[k]
                         for k in ("Open", "High", "Low", "Close", "Adj Close", "Volume")}})
    p = f"{ROOT}/etf/yfinance_daily_6mo.csv"
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    record(p, "yfinance.download(period='6mo', interval='1d', auto_adjust=False) [Yahoo Finance]",
           f"to {max(r['date'] for r in rows)}", "last row may be a PARTIAL session if fetched during US hours")
    # second source: Nasdaq quote API (consolidated volume)
    today = date.today()
    nas = {}
    for t in TICKERS:
        url = NASDAQ.format(t=t, a=date(today.year, 6, 1).isoformat(), b=today.isoformat())
        try:
            j = json.loads(curl(url, accept="application/json"))
            nas[t] = j["data"]["tradesTable"]["rows"]
        except Exception as e:  # noqa: BLE001 - record the failure, keep going
            nas[t] = {"error": str(e)[:200]}
    p = f"{ROOT}/etf/nasdaq_historical.json"
    json.dump(nas, open(p, "w"), indent=1)
    record(p, NASDAQ.format(t="<TICKER>", a="2026-06-01", b=today.isoformat()), f"to {today}",
           "second source for close and volume; api.nasdaq.com")
    return rows, nas


FACT_LABELS = {  # key: consecutive label lines on the iShares product page (checked on the 29 Sep ET pages)
    "net_assets": ["Net Assets of Fund"], "closing_price": ["Closing Price"], "daily_volume": ["Daily", "Volume"],
    "avg_volume_30d": ["30 Day Avg.", "Volume"], "shares_outstanding": ["Shares Outstanding"],
    "premium_discount_pct": ["Premium/Discount"], "number_of_holdings": ["Number of", "Holdings"],
    "sec_yield_30d": ["30 Day SEC", "Yield"], "weighted_avg_coupon": ["Weighted Avg", "Coupon"],
    "eff_duration": ["Effective", "Duration"], "option_adjusted_spread": ["Option Adjusted", "Spread"],
    "avg_ytm": ["Average Yield to", "Maturity"], "wam": ["Weighted Avg", "Maturity"],
}
DATE = re.compile(r"([A-Z][a-z]{2} \d{2}, \d{4})")


def page_lines(raw):
    t = re.sub(r"<script.*?</script>", "", raw, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return [ln.strip() for ln in t.split("\n") if ln.strip()]


def parse_ishares(raw):
    """Value = first line after the label lines; as-of = first date within the next three lines."""
    L = page_lines(raw)
    facts = {}
    for i, ln in enumerate(L):
        if ln == "NAV as of" and "nav" not in facts:
            facts["nav_asof"] = L[i + 1]
            facts["nav"] = next(w for w in L[i + 2:i + 6] if re.match(r"^\d+\.\d+$", w))
    for key, lab in FACT_LABELS.items():
        n = len(lab)
        for i in range(len(L) - n):
            if L[i:i + n] == lab:
                facts[key] = L[i + n]
                m = DATE.search(" ".join(L[i + n + 1:i + n + 4]))
                facts[key + "_asof"] = m.group(1) if m else ""
                break
    return facts


def fetch_ishares():
    os.makedirs(f"{ROOT}/ishares", exist_ok=True)
    out = []
    for t, url in ISHARES.items():
        raw = curl(url + "?switchLocale=y&siteEntryPassthrough=true")
        p = f"{ROOT}/ishares/{t}_product_page.html.gz"
        with gzip.open(p, "wb") as f:
            f.write(raw)
        facts = parse_ishares(raw.decode("utf-8", "ignore"))
        record(p, url, facts.get("closing_price_asof", ""), "raw product page, gzipped")
        out.append({"ticker": t, "url": url, **facts})
    p = f"{ROOT}/ishares/ibonds_facts.csv"
    keys = sorted({k for r in out for k in r}, key=lambda k: (k != "ticker", k))
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(out)
    record(p, "parsed from the product pages above", out[0].get("closing_price_asof", ""))
    return out


def main():
    try:
        run(sys.argv[1:] or ["T", "F", "E", "I", "M", "S"])
    finally:
        write_manifest()


MANUAL = [  # hand-recorded inputs: (file, source, retrieved UTC, as-of, note)
    ("sheet/Portfolio_values_2026-09-30T0030AEST.csv",
     "Sheet 1EHCJxbFI0UOzNOpOWvDfzNqbK45qWuopZcL7HNN3VPM tab Portfolio via the logged-in Chrome browser "
     "(docs.google.com/.../gviz/tq?tqx=out:csv&sheet=Portfolio; the browser saved it as ~/Downloads/data.csv, copied "
     "here unchanged)", "2026-09-29T14:30:57Z", "Sheet values at read time",
     "Sheets/Drive connectors refused the credential; ETF prices in the tab are live GOOGLEFINANCE values at the read "
     "time (29 Sep ~10:31 ET, market open); bond prices typed-in"),
    ("sheet/Book_L_values_2026-09-30T0033AEST.txt",
     "Sheet tab Book L via Chrome (gviz tqx=out:html), page text copied verbatim", "2026-09-29T14:33:00Z",
     "Sheet values at read time", "ETF prices live at read time; bond clean + accrued typed-in (WInS 28 Sep)"),
    ("sheet/WInS_Notes_values_2026-09-30T0034AEST.txt",
     "Sheet tab WInS Notes via Chrome (gviz tqx=out:html), page text copied verbatim", "2026-09-29T14:34:00Z",
     "WInS as seen by the team on 29 Sep 2026 (28 Sep closes)", ""),
    ("wins/wins_prices_2026-09-28.csv",
     "Hand-built by WS1 from the three Sheet files above, rab/premortem.md PM-04 (stale bond prices), the iShares "
     "product pages (closing prices of IBTO-IBTR) and MSPD Table V (CUSIPs)", "2026-09-29T14:50:00Z", "2026-09-28",
     "each row carries its own source and SEEN/UNVERIFIED status"),
]


def register_manual():
    for f, src, utc, asof, note in MANUAL:
        p = f"{ROOT}/{f}"
        b = open(p, "rb").read()
        MANIFEST.append({"file": f, "sha256": sha(b), "bytes": len(b), "url": src, "retrieved_utc": utc,
                         "retrieved_et": et_of(utc),
                         "retrieved_sydney": datetime.strptime(utc, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                         .astimezone(ZoneInfo("Australia/Sydney")).strftime("%Y-%m-%d %H:%M %Z"),
                         "as_of": asof, "note": note})


def summarise_etf(asof="2026-09-28"):
    """Offline: last complete close and volume statistics per ticker from the saved raw files (sessions <= asof)."""
    import pandas as pd
    y = pd.read_csv(f"{ROOT}/etf/yfinance_daily_6mo.csv")
    y = y[y.date <= asof]
    nas = json.load(open(f"{ROOT}/etf/nasdaq_historical.json"))
    ish = {r["ticker"]: r for r in csv.DictReader(open(f"{ROOT}/ishares/ibonds_facts.csv"))}
    wins = {}
    for ln in open(f"{ROOT}/sheet/WInS_Notes_values_2026-09-30T0034AEST.txt"):
        m = re.match(r"^([A-Z]{2,5}) (.+?) \$([\d.]+) ([\d,]+)$", ln.strip())
        if m:
            wins[m.group(1)] = (m.group(2), float(m.group(3)), int(m.group(4).replace(",", "")))
    out = []
    for t in TICKERS:
        n = [r for r in nas.get(t, []) if isinstance(r, dict)]
        n = [r for r in n if datetime.strptime(r["date"], "%m/%d/%Y").date().isoformat() <= asof]
        vol = [int(r["volume"].replace(",", "")) for r in n]  # newest first
        yy = y[y.ticker == t].sort_values("date")
        last = yy.iloc[-1]
        row = {"ticker": t, "asof": asof, "wins_name_seen_2026-09-29": wins.get(t, ("",))[0],
               "close_wins": wins.get(t, (None, ""))[1] if t in wins else "",
               "close_nasdaq": n[0]["close"] if n else "", "close_yahoo": round(float(last.close), 4),
               "close_ishares": ish[t]["closing_price"].replace("$", "") if t in ish else "",
               "volume_nasdaq": vol[0] if vol else "", "volume_wins": wins[t][2] if t in wins else "",
               "avg_volume_30d": round(sum(vol[:30]) / 30) if len(vol) >= 30 else "",
               "avg_volume_20d": round(sum(vol[:20]) / 20) if len(vol) >= 20 else "",
               "median_volume_20d": int(st.median(vol[:20])) if len(vol) >= 20 else "",
               "min_volume_20d": min(vol[:20]) if len(vol) >= 20 else "",
               "ishares_avg_volume_30d": ish[t]["avg_volume_30d"].replace(",", "").split(".")[0] if t in ish else "",
               "sessions_used": min(len(vol), 30), "first_session_used": n[min(len(n), 30) - 1]["date"] if n else ""}
        out.append(row)
    p = f"{ROOT}/etf/etf_summary_{asof}.csv"
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    record(p, "derived offline from etf/nasdaq_historical.json (volume, close), etf/yfinance_daily_6mo.csv (close), "
              "ishares/ibonds_facts.csv, sheet/WInS_Notes (WInS close, volume, name)", asof,
           "volume stats use complete sessions up to as_of, Nasdaq consolidated volume; iShares' '30 Day Avg. Volume' "
           "equals our 20-session mean exactly for IBTM, IBTO, IBTR (checked 30 Sep)")
    return out


def run(which):
    if "M" in which:
        register_manual()
    if "S" in which:
        for r in summarise_etf():
            print(f"[S] {r['ticker']}: close {r['close_nasdaq']} vol {r['volume_nasdaq']} avg30 {r['avg_volume_30d']} "
                  f"med20 {r['median_volume_20d']} min20 {r['min_volume_20d']}")
    if "T" in which:
        for y, status, n, hi in fetch_treasury():
            if status != "identical" or y >= 2025:
                print(f"[T] {y}: {status}, {n} rows, last {hi}")
    if "F" in which:
        for s, a, b, v in fetch_fred():
            print(f"[F] {s}: {a}..{b} last {v}")
    if "E" in which:
        rows, nas = fetch_etf()
        print(f"[E] yfinance rows {len(rows)}; nasdaq ok for {sum(isinstance(v, list) for v in nas.values())} tickers")
    if "I" in which:
        for r in fetch_ishares():
            print(f"[I] {r['ticker']}: " + ", ".join(f"{k}={r.get(k, '')}" for k in
                                                     ("nav", "closing_price", "daily_volume", "avg_volume_30d", "shares_outstanding", "avg_ytm",
                                                      "eff_duration", "premium_discount_pct", "closing_price_asof")))


def write_manifest():
    if not MANIFEST:
        return
    p = f"{ROOT}/MANIFEST.csv"
    old = list(csv.DictReader(open(p))) if os.path.exists(p) else []
    for r in old:  # add the ET column to rows written before it existed
        if not r.get("retrieved_et"):
            r["retrieved_et"] = et_of(r["retrieved_utc"])
    keep = [r for r in old if r["file"] not in {m["file"] for m in MANIFEST}]
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(MANIFEST[0]))
        w.writeheader()
        w.writerows(sorted(keep + MANIFEST, key=lambda r: r["file"]))
    print(f"manifest: {len(keep) + len(MANIFEST)} files")


if __name__ == "__main__":
    main()
