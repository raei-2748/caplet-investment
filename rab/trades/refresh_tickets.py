"""Friday WInS tickets: build, re-size from fresh prices, and check (Gate C checks for tickets).

WS6, RAB Kit, 2026-09-30 (Sydney). AI-generated research code (Claude Code) for Team Caplet. It never logs in to WInS
and never places an order: it prints tickets that students check and enter themselves.

Two modes
  --basis locked  (default, no network). The Gate A basis: 28 Sep 2026 closes, the WInS bond prices recorded on
                  29 Sep, the 28 Sep par curve, Portfolio-tab units and Book L sizes as read. Writes the committed
                  rab/trades/tickets.csv and tickets.md, and checks that the totals equal rab/numbers.yaml to the cent.
  --basis friday  (network, read-only GETs). Fetches the latest U.S. Treasury par curve (home.treasury.gov) and ETF
                  closes and volumes (api.nasdaq.com; yfinance with auto_adjust=False as fallback). Bond prices come
                  ONLY from WInS: the team types what WInS shows into a copy of wins_prices_friday_TEMPLATE.csv and
                  passes it with --wins-prices. Units are re-sized with the Sheet's own rules (--units rule, default
                  in this mode). Writes rab/trades/out/tickets_<curve date>.csv and .md.

Order sequence (both books): iBonds ETFs (IBTR ... IBTM), then the Treasury bonds (Nov-2041 ... Feb-2037), then VT
(Portfolio only) as order 11, in the session after the bonds show Filled. The iBonds go first because they fill at live
prices, so the cash they use is known at once; the bonds next because WInS fills them at end-of-day prices, so their
cash is known only after the close (premortem PM-03); VT last so it is sized from the cash actually left and WInS Order
History shows the payments and the floor before growth (judge panel, 30 Sep). The order inside each group is for cash
control only; it is not the IPS rule "latest payments first", which says which payments a short 2027 deposit funds.

Checks (exit status 1 if any fails)
  C1 names    every ticket carries an expected WInS name and a SEEN/UNVERIFIED tag; SEEN names equal tab WInS Notes;
              IBTN (INSCORP Inc in WInS) is never a ticket.
  C2 cash     running cash >= $1,000 after every ticket in the worst case (every ETF at its max price, every bond at its
              max clean price + accrued to the next business day), commission counted once per ticket.
  C3 volume   shares <= 2 x 30-session average volume (official rule); <= 10% of the 20-session median (kit rule,
              PM-05); <= half of the lowest day in 20 sessions (WInS FAQ "half of market volume", worst full day).
  C4 bonds    each WInS bond price within 25bp of the curve model (M1_METHOD.md section C); else use the alternate.
  C5 ledger   (locked basis) Portfolio and Book L totals equal numbers.yaml wins.portfolio.cost_close_0928 and
              wins.bookL.cost_close_0928 to the cent; numbers.yaml sha256 equals rab/numbers.lock.
  C6 words    the generated .md has none of the superseded-book or stale-fact strings (premortem Gate C 4-5).

Run from the worktree root:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/refresh_tickets.py
    /Users/ray/Research/rab-ws/.venv/bin/python rab/trades/refresh_tickets.py --basis friday \
        --wins-prices rab/trades/wins_prices_friday.csv
"""
import argparse
import csv
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import statistics as st
import subprocess
import sys
import time
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
HERE = os.path.join(ROOT, "rab", "trades")
sys.path.insert(0, HERE)
import trades_clock as clock  # noqa: E402

spec = importlib.util.spec_from_file_location("m1", os.path.join(ROOT, "rab/models/m1_ladder.py"))
m1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m1)

ET, SYD = ZoneInfo("America/New_York"), ZoneInfo("Australia/Sydney")
START_CASH, FLOAT_MIN = 300_000.0, 1_000.0
COMM = {"ETF": 25, "Treasury": 10}
SPLIT = {"ladder": 0.659, "floor": 0.243, "vt": 0.087}  # typed in the Portfolio tab (numbers.yaml wins.portfolio.targets_typed)
BOND_MOVE_BP = 10  # max-price band for bonds: 10bp of yield, about two days' typical move of the 10-year
ETF_MIN_BAND = 0.005  # max-price band for ETFs: the larger of 0.5% and two 20-session daily standard deviations
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
TSY = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{y}/all"
       "?type=daily_treasury_yield_curve&field_tdr_date_value={y}&page&_format=csv")
NASDAQ = "https://api.nasdaq.com/api/quote/{t}/historical?assetclass=etf&fromdate={a}&limit=200&todate={b}"
BANNED = [r"\bIEF\b", r"\bTLH\b", r"\bVGSH\b", r"\(ii\)R", r"duration match", r"(?<![\d,.$])9\.90(?!\d)", r"100,000", r"\$100k",
          r"Dec 4", r"500k", r"no Treasuries", r"\$0 commission", r"guaranteed", r"risk-free", r"\blocked\b",
          r"\bmatched\b", r"repays \$", r"cash-flow match", r"\bI bond"]

# ------------------------------------------------------------------------------------------------ securities
# WInS names: SEEN = read in WInS by the team on 29 Sep 2026 (tab WInS Notes); iShares names are the issuer's own
# (product pages, 28 Sep 2026); bond strings in WInS were never recorded (UNVERIFIED): find them by coupon + maturity.
SEC = {
    "IBTR": {"type": "ETF", "name": "iShares iBonds Dec 2036 Term Treasury ETF", "status": "UNVERIFIED (issuer name)",
             "ends": "about 15 Dec 2036", "pays": 2037,
             "serves": {"Portfolio": "Jan 2037 payment", "BookL": "Jan 2037 payment"},
             "trap": "Thinnest fund (about 1.6m shares outstanding). Check the name says Dec 2036.",
             "alt": "IBTQ (ends a year early, the money waits); the 4.5% Feb-2036 bond only if its WInS price passes "
                    "the yield check (stale on 29 Sep)"},
    "IBTQ": {"type": "ETF", "name": "iShares iBonds Dec 2035 Term Treasury ETF", "status": "UNVERIFIED (issuer name)",
             "ends": "about 15 Dec 2035", "pays": 2036,
             "serves": {"Portfolio": "Jan 2036 payment", "BookL": "Jan 2036 payment"},
             "trap": "Check the name says Dec 2035.", "alt": "IBTP (ends a year early)"},
    "IBTP": {"type": "ETF", "name": "iShares iBonds Dec 2034 Term Treasury ETF", "status": "UNVERIFIED (issuer name)",
             "ends": "about 15 Dec 2034", "pays": 2035,
             "serves": {"Portfolio": "Jan 2035 payment", "BookL": "Jan 2035 payment"},
             "trap": "Check the name says Dec 2034.", "alt": "IBTO (ends a year early)"},
    "IBTO": {"type": "ETF", "name": "iShares iBonds Dec 2033 Term Treasury ETF", "status": "UNVERIFIED (issuer name)",
             "ends": "about 15 Dec 2033", "pays": 2034,
             "serves": {"Portfolio": "Jan 2034 payment", "BookL": "Jan 2034 payment"},
             "trap": "NOT IBTN: in WInS, IBTN is INSCORP Inc (SEEN 29 Sep). Type IBTO and read the name.",
             "alt": "IBTM (ends a year early)"},
    "IBTM": {"type": "ETF", "name": "iShares iBonds Dec 2032 Term Treasury ETF", "status": "SEEN 2026-09-29",
             "ends": "about 15 Dec 2032", "pays": 2033,
             "serves": {"Portfolio": "Jan 2033 payment + facility floor (both jobs in one holding)",
                        "BookL": "Jan 2033 payment"},
             "trap": "Largest order. Check the name says Dec 2032.",
             "alt": "none dated: no WInS Treasury matures between Feb 2031 and Feb 2036 (SEEN 29 Sep); if it cannot "
                    "be bought, keep the cash and retry next session"},
    "VT": {"type": "ETF", "name": "Vanguard Total World Stock ETF", "status": "SEEN 2026-09-29", "ends": "-",
           "pays": None, "serves": {"Portfolio": "Branch: the world stock fund (growth money)"},
           "trap": "Not VTI (U.S. only). Order 11: place it only in the session after all five bonds show Filled "
                   "(Mon 5 Oct ET); re-run with --cash-before-vt first.", "alt": "VTI + VXUS in VT's own U.S./non-U.S. mix (two trades)"},
    "T 3.125% 15-Nov-2041": {"type": "Treasury", "name": "U.S. Treasury bond 3.125% maturing 15 Nov 2041",
                             "cusip": "912810QT8", "status": "UNVERIFIED (WInS string not recorded)",
                             "ends": "15 Nov 2041", "pays": 2042,
                             "serves": {"Portfolio": "Jan 2042 payment", "BookL": "Jan 2042 payment"},
                             "trap": "Same date as the 2.000% Nov-2041: check the coupon.",
                             "alt": "2.000% 15 Nov 2041 (912810TC2), if listed and within 25bp"},
    "T 4.250% 15-Nov-2040": {"type": "Treasury", "name": "U.S. Treasury bond 4.250% maturing 15 Nov 2040",
                             "cusip": "912810QL5", "status": "UNVERIFIED (WInS string not recorded)",
                             "ends": "15 Nov 2040", "pays": 2041,
                             "serves": {"Portfolio": "Jan 2041 payment", "BookL": "Jan 2041 payment"},
                             "trap": "Same date as the 1.375% Nov-2040: check the coupon.",
                             "alt": "1.375% 15 Nov 2040 (912810ST6), if listed and within 25bp"},
    "T 4.375% 15-Nov-2039": {"type": "Treasury", "name": "U.S. Treasury bond 4.375% maturing 15 Nov 2039",
                             "cusip": "912810QD3", "status": "UNVERIFIED (WInS string not recorded)",
                             "ends": "15 Nov 2039", "pays": 2040,
                             "serves": {"Portfolio": "Jan 2040 payment", "BookL": "Jan 2040 payment"},
                             "trap": "Not the 4.375% Feb-2038 (stale price on 29 Sep): check the maturity.",
                             "alt": "4.500% 15 Aug 2039 (912810QC5), if listed and within 25bp"},
    "T 4.500% 15-May-2038": {"type": "Treasury", "name": "U.S. Treasury bond 4.500% maturing 15 May 2038",
                             "cusip": "912810PX0", "status": "UNVERIFIED (WInS string not recorded)",
                             "ends": "15 May 2038", "pays": 2039,
                             "serves": {"Portfolio": "Jan 2039 payment", "BookL": "Jan 2039 payment"},
                             "trap": "Not the 4.500% Feb-2036 or Aug-2039: check the maturity. Sheet accrued 0.530 "
                                     "is a typo (1.66 on 28 Sep, 1.71 on 2 Oct); use what WInS shows.",
                             "alt": "4.375% 15 Feb 2038 (912810PW2) only if its WInS price passes the yield check "
                                    "(stale on 29 Sep); else 5.000% 15 May 2037 (912810PU6)"},
    "T 4.750% 15-Feb-2037": {"type": "Treasury", "name": "U.S. Treasury bond 4.750% maturing 15 Feb 2037",
                             "cusip": "912810PT9", "status": "UNVERIFIED (WInS string not recorded)",
                             "ends": "15 Feb 2037", "pays": 2038,
                             "serves": {"Portfolio": "Jan 2038 payment", "BookL": "Jan 2038 payment"},
                             "trap": "Check the maturity says 2037.",
                             "alt": "5.000% 15 May 2037 (912810PU6), if listed and within 25bp"},
}
ORDER = {"Portfolio": ["IBTR", "IBTQ", "IBTP", "IBTO", "IBTM", "T 3.125% 15-Nov-2041", "T 4.250% 15-Nov-2040",
                       "T 4.375% 15-Nov-2039", "T 4.500% 15-May-2038", "T 4.750% 15-Feb-2037", "VT"]}
ORDER["BookL"] = [k for k in ORDER["Portfolio"] if k != "VT"]
WHY = {"IBTR": "iBonds first (live prices, so cash is known at once); a small first order to learn the screen",
       "T 3.125% 15-Nov-2041": "bonds after the iBonds: WInS fills them at end-of-day prices",
       "VT": "last, in the next session: sized from the cash left after the bonds fill (payments and floor first)"}


ALTERNATES = ["T 2.000% 15-Nov-2041", "T 1.375% 15-Nov-2040", "T 4.500% 15-Aug-2039", "T 5.000% 15-May-2037",
              "T 4.375% 15-Feb-2038", "T 4.500% 15-Feb-2036"]
ALT_CUSIP = {"T 2.000% 15-Nov-2041": "912810TC2", "T 1.375% 15-Nov-2040": "912810ST6", "T 4.500% 15-Aug-2039": "912810QC5",
             "T 5.000% 15-May-2037": "912810PU6", "T 4.375% 15-Feb-2038": "912810PW2", "T 4.500% 15-Feb-2036": "912810FT0"}


def parse_bond(k):
    m = re.match(r"^T (\d+\.\d+)% (\d{2}-[A-Z][a-z]{2}-\d{4})$", k)
    return float(m.group(1)), datetime.strptime(m.group(2), "%d-%b-%Y").date()


def alternates_check(ctx):
    """Price bands (curve +-25bp) for the named alternates, and the yield check of any WInS price for them."""
    out = []
    s_chk, cv = ctx["curve_date"], ctx["cv"]
    for k in ALTERNATES:
        c, mat = parse_bond(k)
        a = m1.accrued(c, mat, s_chk)
        dm = m1.model_dirty(cv, c, mat, s_chk)
        y_mod = m1.street_yield(c, mat, s_chk, dm)
        lo, hi = m1.clean_at_yield(c, mat, s_chk, y_mod + 0.0025), m1.clean_at_yield(c, mat, s_chk, y_mod - 0.0025)
        p = ctx["alt_px"].get(k)
        r = {"id": k, "cusip": ALT_CUSIP[k], "model_clean": dm - a, "band_low": lo, "band_high": hi,
             "model_yield_pct": y_mod * 100}
        if p is not None:
            y_w = m1.street_yield(c, mat, s_chk, p["ref"] + a)
            gap = (y_w - y_mod) * 1e4
            r.update({"wins_clean": p["ref"], "wins_asof": p["asof"], "gap_bp": gap,
                      "verdict": "PASS" if abs(gap) <= 25 else "FAIL (stale or wrong)"})
        out.append(r)
    return out


def add_swap(ctx, old, new):
    """Replace a planned bond by a named alternate for the same payment (M9 upgrade candidate; a team decision)."""
    if new not in ALTERNATES or SEC.get(old, {}).get("type") != "Treasury":
        raise SystemExit(f"--swap {old}={new}: NEW must be one of {ALTERNATES} and OLD a planned bond")
    c, mat = parse_bond(new)
    o = SEC[old]
    SEC[new] = {"type": "Treasury", "name": f"U.S. Treasury bond {c:.3f}% maturing {mat:%-d %b %Y}",
                "cusip": ALT_CUSIP[new], "status": "UNVERIFIED (alternate; confirm it is in the WInS drop-down)",
                "ends": f"{mat:%-d %b %Y}", "pays": o["pays"], "serves": o["serves"],
                "trap": f"Swapped in for the planned {old} (team decision). Check coupon AND maturity.",
                "alt": f"{old} (the planned bond)"}
    if o["pays"] and not mat < date(o["pays"], 1, 1):
        raise SystemExit(f"{new} does not mature before the 1 Jan {o['pays']} payment")
    ctx["wins"][new] = {"type": "Treasury", "coupon": c, "mat": mat, "bookL_end": mat, "acc_rec": None,
                        "bookL_pays_year": str(o["pays"]), "price": None}
    if new not in ctx["px"]:
        if ctx["basis"] == "friday" and new in ctx["alt_px"]:
            ctx["px"][new] = {"ref": ctx["alt_px"][new]["ref"], "asof": ctx["alt_px"][new]["asof"],
                              "source": "WInS, typed", "acc_shown": None, "status": "SEEN in WInS (typed)"}
        else:
            a = m1.accrued(c, mat, ctx["curve_date"])
            ctx["px"][new] = {"ref": m1.model_dirty(ctx["cv"], c, mat, ctx["curve_date"]) - a,
                              "asof": ctx["curve_date"].isoformat(), "source": "curve model (no WInS price)",
                              "acc_shown": None, "status": "STALE REFERENCE: MODEL price only; read it in WInS"}
    ctx["wins"][new]["price"] = ctx["px"][new]["ref"]
    for b in ORDER:
        ORDER[b] = [new if x == old else x for x in ORDER[b]]


def next_business_day(d):
    d += timedelta(days=1)
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d


# ------------------------------------------------------------------------------------------------ data
def curl(url, accept=None, tries=3):
    cmd = ["curl", "-sSL", "--http1.1", "-m", "90", "-A", UA, "-w", "\n%{http_code}", url]
    if accept:
        cmd[1:1] = ["-H", f"Accept: {accept}"]
    for k in range(tries):
        r = subprocess.run(cmd, capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code.startswith(b"2"):
            return body
        time.sleep(3 * (k + 1))
    raise RuntimeError(f"fetch failed: {url} (curl {r.returncode}, HTTP {code!r})")


def vol_stats(rows):
    """rows: newest first, complete sessions, each {'close': float, 'volume': int, 'date': str}."""
    v = [r["volume"] for r in rows]
    c = [r["close"] for r in rows[:21]][::-1]
    rets = [math.log(c[i + 1] / c[i]) for i in range(len(c) - 1)]
    return {"adv30": sum(v[:30]) / 30, "median20": st.median(v[:20]), "min20": min(v[:20]),
            "sigma20": st.pstdev(rets), "last_close": rows[0]["close"], "last_date": rows[0]["date"],
            "sessions": min(len(v), 30)}


def nasdaq_rows(raw, upto):
    out = []
    for r in raw:
        d = datetime.strptime(r["date"], "%m/%d/%Y").date()
        if d <= upto:
            out.append({"date": d.isoformat(), "close": float(r["close"].replace("$", "").replace(",", "")),
                        "volume": int(float(r["volume"].replace(",", "")))})
    return sorted(out, key=lambda r: r["date"], reverse=True)


def locked_context(trade_date):
    rows = m1.load_rows([os.path.join(ROOT, "rab/data/treasury_par_2000_2026/2026.csv")])
    row = next(r for r in rows if r["_date"] == date(2026, 9, 28))
    wins = m1.read_wins(os.path.join(ROOT, "rab/data/wins/wins_prices_2026-09-28.csv"))
    nas = json.load(open(os.path.join(ROOT, "rab/data/etf/nasdaq_historical.json")))
    summ = {r["ticker"]: r for r in csv.DictReader(open(os.path.join(ROOT, "rab/data/etf/etf_summary_2026-09-28.csv")))}
    stats = {}
    for t in ("IBTM", "IBTO", "IBTP", "IBTQ", "IBTR", "VT"):
        s = vol_stats(nasdaq_rows(nas[t], date(2026, 9, 28)))
        # the committed summary is the reference for the volume columns; assert we read the same thing
        assert abs(s["adv30"] - float(summ[t]["avg_volume_30d"])) < 1 and s["min20"] == int(summ[t]["min_volume_20d"])
        stats[t] = s
    px = {}
    for k in SEC:
        w = wins[k]
        px[k] = {"ref": w["price"], "asof": w["price_date"], "source": w["price_source"],
                 "acc_shown": w["acc_rec"], "status": w["price_status"]}
    alt_px = {k: {"ref": wins[k]["price"], "asof": wins[k]["price_date"]} for k in ALTERNATES if k in wins}
    return {"basis": "locked", "row": row, "cv": m1.Curve(row), "curve_date": row["_date"], "trade_date": trade_date,
            "settle_date": next_business_day(trade_date), "px": px, "stats": stats, "wins": wins, "alt_px": alt_px,
            "label": "Gate A basis: 28 Sep 2026 closes and par curve; WInS bond prices recorded 29 Sep (tab Book L)"}


def friday_context(trade_date, wins_prices):
    """Fresh data with fallbacks, so a failed fetch never blocks Friday: curve -> the committed Gate A curve;
    Nasdaq -> Yahoo -> the committed 28 Sep volume file. Any price that falls back to 28 Sep is flagged STALE and
    fails a check unless the team typed the WInS price for it."""
    now_et = datetime.now(timezone.utc).astimezone(ET)
    upto = now_et.date() if now_et.hour >= 17 else now_et.date() - timedelta(days=1)  # last complete session
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    warn = []
    try:
        b = curl(TSY.format(y=upto.year))
        path = os.path.join(HERE, "out", f"treasury_par_{upto.year}_fetched_{now_et:%Y%m%dT%H%M}ET.csv")
        open(path, "wb").write(b)
        rows = m1.load_rows([path])
    except Exception as e:  # noqa: BLE001
        warn.append(f"curve fetch failed ({str(e)[:60]}): using the committed Gate A curve file")
        path = os.path.join(ROOT, "rab/data/treasury_par_2000_2026/2026.csv")
        rows = m1.load_rows([path])
    row = rows[-1]
    stats, raw = {}, {}
    nas_saved = json.load(open(os.path.join(ROOT, "rab/data/etf/nasdaq_historical.json")))
    for t in ("IBTM", "IBTO", "IBTP", "IBTQ", "IBTR", "VT"):
        try:
            j = json.loads(curl(NASDAQ.format(t=t, a=(upto - timedelta(days=70)).isoformat(), b=upto.isoformat()),
                                accept="application/json"))
            raw[t] = nasdaq_rows(j["data"]["tradesTable"]["rows"], upto)
            src = "api.nasdaq.com consolidated close"
        except Exception:  # noqa: BLE001 - fall back to Yahoo, then to the committed file
            try:
                import yfinance as yf
                d = yf.download(t, period="3mo", interval="1d", auto_adjust=False, progress=False)
                val = lambda x: float(x.iloc[0]) if hasattr(x, "iloc") else float(x)
                raw[t] = sorted([{"date": i.date().isoformat(), "close": val(r["Close"]), "volume": int(val(r["Volume"]))}
                                 for i, r in d.iterrows() if i.date() <= upto], key=lambda r: r["date"], reverse=True)
                assert len(raw[t]) >= 30
                src = "Yahoo Finance close (yfinance, auto_adjust=False)"
            except Exception:  # noqa: BLE001
                raw[t] = nasdaq_rows(nas_saved[t], date(2026, 9, 28))
                src = "STALE: committed 28 Sep Nasdaq file (fetch failed)"
                warn.append(f"{t}: price and volume fetch failed, using 28 Sep")
        stats[t] = vol_stats(raw[t]) | {"source": src}
    json.dump(raw, open(os.path.join(HERE, "out", f"etf_history_fetched_{now_et:%Y%m%dT%H%M}ET.json"), "w"), indent=0)
    wins = m1.read_wins(os.path.join(ROOT, "rab/data/wins/wins_prices_2026-09-28.csv"))
    px = {}
    for t in stats:
        stale = stats[t]["source"].startswith("STALE")
        px[t] = {"ref": stats[t]["last_close"], "asof": stats[t]["last_date"], "source": stats[t]["source"],
                 "acc_shown": None, "status": ("STALE REFERENCE: type the WInS price and re-run" if stale else
                                               "OUTSIDE SOURCE; compare with the WInS price at Preview")}
    typed = {}
    if wins_prices and os.path.exists(wins_prices):
        for r in csv.DictReader(open(wins_prices)):
            if r.get("clean_or_etf_price_shown", "").strip():
                typed[r["instrument"].strip()] = r
    else:
        warn.append(f"no WInS price file at {wins_prices}: bond prices fall back to 28 Sep and fail the check")
    for k, meta in SEC.items():
        r = typed.get(k)
        if r is not None:
            px[k] = {"ref": float(r["clean_or_etf_price_shown"]), "asof": r.get("seen_at_et", "").strip() or "Friday",
                     "source": f"WInS, typed by {r.get('seen_by', '').strip() or 'team'}",
                     "acc_shown": float(r["accrued_per100_shown"]) if r.get("accrued_per100_shown", "").strip() else None,
                     "status": "SEEN in WInS (typed)"}
        elif meta["type"] == "Treasury":
            w = wins[k]
            px[k] = {"ref": w["price"], "asof": w["price_date"], "source": "WInS 28 Sep (recorded 29 Sep)",
                     "acc_shown": None, "status": "STALE REFERENCE: read this bond in WInS and re-run"}
    alt_px = {k: {"ref": float(typed[k]["clean_or_etf_price_shown"]), "asof": typed[k].get("seen_at_et", "") or "Friday"}
              for k in ALTERNATES if k in typed}
    for w_ in warn:
        print("WARNING:", w_)
    return {"basis": "friday", "row": row, "cv": m1.Curve(row), "curve_date": row["_date"], "trade_date": trade_date,
            "settle_date": next_business_day(trade_date), "px": px, "stats": stats, "wins": wins, "alt_px": alt_px,
            "label": f"Refresh {now_et:%a %-d %b %Y %-I:%M %p %Z}: curve {row['_date']}, ETF closes "
                     f"{stats['VT']['last_date']}, bond prices as typed from WInS (see status column)"
                     + ("; WARNINGS: " + "; ".join(warn) if warn else ""),
            "fetched": path}


# ------------------------------------------------------------------------------------------------ units
def units_sheet():
    port, _ = m1.read_portfolio(os.path.join(ROOT, "rab/data/sheet/Portfolio_values_2026-09-30T0030AEST.csv"))
    wins = m1.read_wins(os.path.join(ROOT, "rab/data/wins/wins_prices_2026-09-28.csv"))
    return {"Portfolio": {h["holding"]: h["units"] for h in port},
            "BookL": {k: w["bookL_size"] for k, w in wins.items() if w["bookL_size"]}}


def dirty_for_sizing(k, ctx):
    p = ctx["px"][k]
    if SEC[k]["type"] == "ETF":
        return p["ref"]
    acc = p["acc_shown"] if p["acc_shown"] is not None and ctx["basis"] == "friday" else \
        m1.accrued(ctx["wins"][k]["coupon"], ctx["wins"][k]["mat"], ctx["trade_date"])
    return p["ref"] + acc


def units_rule(ctx):
    """The Sheet's own sizing rules (M1_METHOD.md B4), at this context's prices and curve."""
    cv = ctx["cv"]
    bl, blv = {}, {}
    for k in ORDER["BookL"]:
        w = ctx["wins"][k]
        tgt = 50_000 * cv.df(w["bookL_end"])
        px = dirty_for_sizing(k, ctx)
        q = math.ceil(tgt / px) if SEC[k]["type"] == "ETF" else math.ceil(tgt / (px / 100) / 1000) * 1000
        bl[k] = q
        blv[k] = q * px / (100 if SEC[k]["type"] == "Treasury" else 1)
    tot = sum(blv.values())
    pf = {}
    for k in ORDER["Portfolio"]:
        px = dirty_for_sizing(k, ctx)
        if k == "VT":
            tgt = SPLIT["vt"] * START_CASH
        else:
            tgt = SPLIT["ladder"] * START_CASH * blv[k] / tot + (SPLIT["floor"] * START_CASH if k == "IBTM" else 0)
        pf[k] = math.floor(tgt / px) if SEC[k]["type"] == "ETF" else math.floor(tgt / (px / 100) / 1000) * 1000
    return {"Portfolio": pf, "BookL": bl}


# ------------------------------------------------------------------------------------------------ tickets
def ticket(book, seq, k, qty, ctx):
    meta, p = SEC[k], ctx["px"][k]
    cv, s_chk, s_tr, s_set = ctx["cv"], ctx["curve_date"], ctx["trade_date"], ctx["settle_date"]
    r = {"book": book, "seq": seq, "id": k, "ticker": k if meta["type"] == "ETF" else "(bond: pick by coupon + maturity)",
         "type": meta["type"], "wins_name_expected": meta["name"], "wins_name_status": meta["status"],
         "cusip": meta.get("cusip", ""), "ends": meta["ends"], "serves": meta["serves"][book],
         "qty": qty, "qty_unit": "shares" if meta["type"] == "ETF" else "face value $ (unit UNVERIFIED in WInS)",
         "ref_price": p["ref"], "ref_asof": p["asof"], "ref_source": p["source"], "price_status": p["status"],
         "commission": COMM[meta["type"]], "trap": meta["trap"], "alternate": meta["alt"], "why_here": WHY.get(k, "")}
    if meta["type"] == "ETF":
        stt = ctx["stats"][k]
        band = max(ETF_MIN_BAND, 2 * stt["sigma20"])
        r.update({"accrued_rec": "", "accrued_trade": "", "band_pct": band * 100,
                  "max_price": math.ceil(p["ref"] * (1 + band) * 100) / 100,
                  "min_price": math.floor(p["ref"] * (1 - band) * 100) / 100})
        r["cost_locked"] = qty * p["ref"] + r["commission"]
        r["cost_ref"] = r["cost_locked"]
        r["cost_max"] = qty * r["max_price"] + r["commission"]
        r["preview_low"] = qty * r["min_price"] + r["commission"]
        r.update({"adv30": stt["adv30"], "median20": stt["median20"], "min20": stt["min20"],
                  "x_of_2adv30": qty / (2 * stt["adv30"]), "pct_median20": qty / stt["median20"],
                  "pct_min20": qty / stt["min20"]})
        r["pass_volume"] = r["x_of_2adv30"] <= 1 and r["pct_median20"] <= 0.10 and r["pct_min20"] <= 0.5
        r.update({"yield_gap_bp": "", "yield_check": "n/a (ETF)"})
    else:
        w = ctx["wins"][k]
        c, mat = w["coupon"], w["mat"]
        a_chk = m1.accrued(c, mat, s_chk)
        a_tr = m1.accrued(c, mat, s_tr)
        a_set = m1.accrued(c, mat, s_set)
        a_rec = p["acc_shown"]
        y_ref = m1.street_yield(c, mat, s_chk, p["ref"] + a_chk)
        dm = m1.model_dirty(cv, c, mat, s_chk)
        y_mod = m1.street_yield(c, mat, s_chk, dm)
        gap = (y_ref - y_mod) * 1e4
        mx = m1.clean_at_yield(c, mat, s_chk, y_ref - BOND_MOVE_BP / 1e4)
        mn = m1.clean_at_yield(c, mat, s_chk, y_ref + BOND_MOVE_BP / 1e4)
        band25 = (m1.clean_at_yield(c, mat, s_chk, y_mod + 0.0025), m1.clean_at_yield(c, mat, s_chk, y_mod - 0.0025))
        acc_locked = a_rec if a_rec is not None else a_tr
        # expected Preview: the accrued WInS itself showed (typed on Friday), else our act/act figure to the trade date
        a_prev = a_rec if (ctx["basis"] == "friday" and a_rec is not None) else a_tr
        r.update({"accrued_rec": a_rec if a_rec is not None else "", "accrued_trade": a_tr,
                  "band_pct": (mx / p["ref"] - 1) * 100, "max_price": round(mx, 3), "min_price": round(mn, 3),
                  "yield_band_25bp_low": round(band25[0], 3), "yield_band_25bp_high": round(band25[1], 3)})
        r["cost_locked"] = qty * (p["ref"] + acc_locked) / 100 + r["commission"]
        r["cost_ref"] = qty * (p["ref"] + a_prev) / 100 + r["commission"]
        r["cost_max"] = qty * (mx + max(a_set, a_prev)) / 100 + r["commission"]
        r["preview_low"] = qty * (mn + min(a_tr, a_prev)) / 100 + r["commission"]
        r.update({"adv30": "", "median20": "", "min20": "", "x_of_2adv30": "", "pct_median20": "", "pct_min20": "",
                  "pass_volume": True, "yield_gap_bp": gap,
                  "yield_check": "PASS" if abs(gap) <= 25 else "FAIL: stale or wrong price, use the alternate",
                  "wins_yield_pct": y_ref * 100, "model_yield_pct": y_mod * 100})
    # PM-02 stop band: the larger of 1% and the price band around the expected Preview total
    r["preview_expected"] = r["cost_ref"]
    r["stop_if_preview_above"] = max(r["cost_max"], r["cost_ref"] * 1.01)
    r["stop_if_preview_below"] = min(r["preview_low"], r["cost_ref"] * 0.99)
    return r


def build(book, units, ctx):
    """Cash walk in sequence. ctx['cash_after_etfs'] (Friday, optional) replaces the modelled cash after the last iBonds
    ETF with what WInS actually shows, so the bonds are sized from the cash actually left (PM-03).
    ctx['cash_before_vt'] (Portfolio, optional) replaces the modelled cash before VT (order 11, placed after the bonds
    fill) with what WInS shows then."""
    rows, cash_l, cash_r, cash_w = [], START_CASH, START_CASH, START_CASH
    last_etf = max(i for i, k in enumerate(ORDER[book]) if SEC[k]["type"] == "ETF" and k != "VT")
    for i, k in enumerate(ORDER[book], 1):
        if k == "VT" and ctx.get("cash_before_vt") is not None:
            cash_l = cash_r = cash_w = ctx["cash_before_vt"]
        t = ticket(book, i, k, units[k], ctx)
        cash_l -= t["cost_locked"]
        cash_r -= t["cost_ref"]
        cash_w -= t["cost_max"]
        if i - 1 == last_etf and ctx.get("cash_after_etfs") is not None:
            cash_l = cash_r = cash_w = ctx["cash_after_etfs"]
        t.update({"cash_after_locked": cash_l, "cash_after_ref": cash_r, "cash_after_worst": cash_w})
        rows.append(t)
    return rows


def size_vt_from_cash(units, ctx):
    """--cash-before-vt: VT gets the plan share, or less if the cash WInS shows would leave under $1,000 in the worst
    case (VT at its max price). It never takes more than the plan share; spare cash waits for October trigger C."""
    t = ticket("Portfolio", 11, "VT", 1, ctx)
    afford = math.floor((ctx["cash_before_vt"] - FLOAT_MIN - t["commission"]) / t["max_price"])
    u = dict(units)
    u["VT"] = max(0, min(u["VT"], afford))
    return u


def trim_for_float(book, units, ctx):
    """Rule mode only: if the worst case leaves under $1,000, trim bonds $1,000 face at a time, earliest payment
    first (the IPS buys the latest payments first, so the earliest is completed last)."""
    u = dict(units)
    bonds = [k for k in ORDER[book] if SEC[k]["type"] == "Treasury"][::-1]
    trims = []
    while min(r["cash_after_worst"] for r in build(book, u, ctx)) < FLOAT_MIN:
        k = next(b for b in bonds if u[b] >= 1000)
        u[k] -= 1000
        trims.append(k)
    return u, trims


# ------------------------------------------------------------------------------------------------ checks
def wins_notes_names():
    names = {}
    for ln in open(os.path.join(ROOT, "rab/data/sheet/WInS_Notes_values_2026-09-30T0034AEST.txt")):
        m = re.match(r"^([A-Z]{2,5}) (.+?) \$([\d.]+) ([\d,]+)$", ln.strip())
        if m:
            names[m.group(1)] = m.group(2)
    return names


def run_checks(books, ctx, numbers, units_mode):
    out = []
    seen = wins_notes_names()
    for book, rows in books.items():
        for r in rows:
            ok = bool(r["wins_name_expected"]) and ("SEEN" in r["wins_name_status"] or "UNVERIFIED" in r["wins_name_status"])
            if r["type"] == "ETF" and "SEEN" in r["wins_name_status"]:
                ok = ok and seen.get(r["id"]) == r["wins_name_expected"]
            ok = ok and r["id"] != "IBTN"
            out.append(("C1 names", f"{book} #{r['seq']} {r['id']}", ok, r["wins_name_status"]))
            out.append(("C2 cash", f"{book} #{r['seq']} {r['id']}", r["cash_after_worst"] >= FLOAT_MIN,
                        f"worst-case cash after ${r['cash_after_worst']:,.0f}"))
            if r["type"] == "ETF":
                out.append(("C3 volume", f"{book} #{r['seq']} {r['id']}", r["pass_volume"],
                            f"{r['x_of_2adv30']:.1%} of 2x30d avg; {r['pct_median20']:.1%} of 20d median; "
                            f"{r['pct_min20']:.1%} of lowest day"))
            else:
                out.append(("C4 bonds", f"{book} #{r['seq']} {r['id']}", r["yield_check"] == "PASS",
                            f"gap {r['yield_gap_bp']:+.1f}bp vs curve {ctx['curve_date']}"))
    if ctx["basis"] == "friday" or any("MODEL price" in r["price_status"] for rows in books.values() for r in rows):
        for book, rows in books.items():
            stale = [r["id"] for r in rows if "STALE" in r["price_status"]]
            out.append(("C4 bonds", f"{book}: every price fresh or typed from WInS", not stale,
                        "missing: " + ", ".join(stale) if stale else "all typed"))
    if (ctx["basis"] == "locked" and units_mode == "sheet" and ctx.get("cash_after_etfs") is None
            and ctx.get("cash_before_vt") is None):
        want = {"Portfolio": numbers["wins.portfolio.cost_close_0928"]["value"],
                "BookL": numbers["wins.bookL.cost_close_0928"]["value"]}
        for book, rows in books.items():
            tot = sum(r["cost_locked"] for r in rows)
            ok = abs(tot - want[book]["cost"]) < 0.005 and abs(START_CASH - tot - want[book]["cash_left"]) < 0.005
            out.append(("C5 ledger", f"{book} total", ok, f"${tot:,.2f} vs numbers.yaml ${want[book]['cost']:,.2f}"))
        if "Portfolio" in books:
            rows = books["Portfolio"]
            vt = sum(r["cost_locked"] - r["commission"] for r in rows if r["id"] == "VT")
            dated = sum(r["cost_locked"] - r["commission"] for r in rows if r["id"] != "VT")
            cash = rows[-1]["cash_after_locked"]
            sp = numbers["wins.portfolio.split_close_0928"]["value"]
            ok = (abs(dated / START_CASH - sp["dated_holdings_incl_floor"]) < 5e-5 and abs(vt / START_CASH - sp["vt"]) < 5e-5
                  and abs(cash / START_CASH - sp["cash"]) < 5e-5)
            tt = numbers["wins.portfolio.targets_typed"]["value"]
            out.append(("C5 ledger", "Portfolio split", ok,
                        f"dated holdings incl. floor {dated / START_CASH:.2%} (tab target "
                        f"{(tt['ladder_65.9pct'] + tt['floor_24.3pct']) / START_CASH:.1%}), VT {vt / START_CASH:.2%} "
                        f"(target {tt['stock_fund_8.7pct'] / START_CASH:.1%}), cash {cash / START_CASH:.2%} (target "
                        f"{tt['cash_1.1pct'] / START_CASH:.1%}); equals numbers.yaml wins.portfolio.split_close_0928"))
        hold = {h["holding"]: h for h in numbers["wins.portfolio.holdings_close_0928"]["value"]}
        for r in books.get("Portfolio", []):
            v = r["cost_locked"] - r["commission"]
            ok = abs(v - hold[r["id"]]["value"]) < 0.005 and r["qty"] == hold[r["id"]]["qty"]
            out.append(("C5 ledger", f"Portfolio {r['id']} value", ok, f"${v:,.2f}"))
    lock = open(os.path.join(ROOT, "rab/numbers.lock")).read().split()[0]
    h = hashlib.sha256(open(os.path.join(ROOT, "rab/numbers.yaml"), "rb").read()).hexdigest()
    out.append(("C5 ledger", "numbers.yaml hash", h == lock, h[:12]))
    return out


def text_check(paths):
    out = []
    for p in paths:
        txt = open(p).read()
        hits = [b for b in BANNED if re.search(b, txt)]
        out.append(("C6 words", os.path.relpath(p, ROOT), not hits, ", ".join(hits) or "clean"))
    return out


# ------------------------------------------------------------------------------------------------ output
CSV_COLS = ["book", "seq", "id", "ticker", "type", "wins_name_expected", "wins_name_status", "cusip", "ends", "serves",
            "qty", "qty_unit", "ref_price", "ref_asof", "ref_source", "price_status", "accrued_rec", "accrued_trade",
            "max_price", "min_price", "band_pct", "commission", "preview_expected", "stop_if_preview_below",
            "stop_if_preview_above", "cost_locked", "cash_after_locked", "cost_max", "cash_after_worst", "adv30",
            "median20", "min20", "x_of_2adv30", "pct_median20", "pct_min20", "yield_gap_bp", "yield_check",
            "yield_band_25bp_low", "yield_band_25bp_high", "trap", "alternate", "why_here"]


def write_csv(path, books):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLS, extrasaction="ignore")
        w.writeheader()
        for rows in books.values():
            for r in rows:
                w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})


def money(x):
    return f"${x:,.2f}"


def md_book(book, rows, ctx):
    L = [f"### {'Portfolio tab book (current plan, 11 trades: 1-10 on Friday, VT in the session after the bonds fill)' if book == 'Portfolio' else 'Book L (literal ladder, 10 trades; only if the 1 Oct vote picks it)'}",
         "",
         "| # | Ticker or bond | Exact WInS name to look for | Serves (Laura's plan) | Quantity | Reference price (as of) | "
         "Max price | Commission | Expected Preview total | Cash after: expected / worst case | Size vs 2x-volume limit; vs median day | Yield vs curve |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["type"] == "ETF":
            q = f"{r['qty']:,} shares"
            src = "WInS" if r["ref_source"].startswith("WInS, typed") else "WInS close" if r["ref_source"].startswith("WInS") else (
                "iShares close" if "iShares" in r["ref_source"] else r["ref_source"].split(" (")[0])
            ref = f"${r['ref_price']:.2f} ({src}, {r['ref_asof']})"
            mx = f"${r['max_price']:.2f}"
            pc = lambda x: "<0.1%" if x < 0.001 else f"{x:.1%}"
            vol = f"{pc(r['x_of_2adv30'])}; {pc(r['pct_median20'])}" + (" PASS" if r["pass_volume"] else " FAIL")
            yc = "-"
            nm = f"{r['wins_name_expected']} [{r['wins_name_status']}]"
            tk = f"**{r['id']}**"
        else:
            q = f"${r['qty']:,} face"
            ref = f"{r['ref_price']:.3f} clean ({r['ref_asof']}) + {r['accrued_trade']:.3f} accrued on {ctx['trade_date']:%-d %b}, per $100"
            if r["accrued_rec"] != "" and abs(r["accrued_rec"] - r["accrued_trade"]) > 0.1:
                ref += f" (Sheet records {r['accrued_rec']:.3f}: wrong)"
            if "STALE" in r["price_status"]:
                ref += " **STALE: read this bond in WInS and re-run**"
            mx = f"{r['max_price']:.3f} clean"
            vol = "WInS shows no bond volume (UNVERIFIED)"
            yc = f"{r['yield_gap_bp']:+.1f}bp {r['yield_check'].split(':')[0]}"
            nm = f"{r['wins_name_expected']}, CUSIP {r['cusip']} [{r['wins_name_status']}]"
            tk = "bond"
        L.append(f"| {r['seq']} | {tk} | {nm} | {r['serves']} | {q} | {ref} | {mx} | ${r['commission']} | "
                 f"{money(r['preview_expected'])} | {money(r['cash_after_ref'])} / {money(r['cash_after_worst'])} | {vol} | {yc} |")
    tl = sum(r["cost_locked"] for r in rows)
    tr = sum(r["cost_ref"] for r in rows)
    tw = sum(r["cost_max"] for r in rows)
    cl, cr, cw = rows[-1]["cash_after_locked"], rows[-1]["cash_after_ref"], rows[-1]["cash_after_worst"]
    L += ["", f"- Total at the reference prices with the accrued interest recorded in the Sheet: **{money(tl)}**, "
              f"cash left **{money(cl)}** ({cl / START_CASH:.1%}).",
          f"- Expected on the trade date (bond accrued interest recomputed to {ctx['trade_date']}): {money(tr)}, "
          f"cash {money(cr)} (the 'expected' cash column).",
          f"- Worst case (every ETF at its max price, every bond at its max clean price, accrued to "
          f"{ctx['settle_date']}): {money(tw)}, cash {money(cw)}.",
          f"- {len(rows)} trades; commissions ${sum(r['commission'] for r in rows)}.", ""]
    return L


def md_detail(rows):
    L = ["| # | Holding | Stop if the Preview total is outside | Watch out | If it cannot be bought |", "|---|---|---|---|---|"]
    for r in rows:
        extra = ""
        if r["type"] == "Treasury":
            extra = (f" Curve check band (25bp): clean {r['yield_band_25bp_low']:.3f} to {r['yield_band_25bp_high']:.3f}.")
        L.append(f"| {r['seq']} | {r['id']} | {money(r['stop_if_preview_below'])} to {money(r['stop_if_preview_above'])} | "
                 f"{r['trap']}{extra} | {r['alternate']} |")
    return L + [""]


def write_md(path, books, ctx, checks, trims, units_mode):
    L = [f"# Friday WInS tickets", "",
         f"**Basis:** {ctx['label']}. **Trade date:** Fri {ctx['trade_date']:%-d %b %Y} (U.S. Eastern). "
         f"**Units:** {'as in the Sheet tabs' if units_mode == 'sheet' else 're-sized with the Sheet rules at these prices'}.",
         "",
         "AI-generated trade tickets (Claude Code, RAB Kit WS6) for Team Caplet. Nothing here places an order: students "
         "check and enter every order themselves. Generated by `rab/trades/refresh_tickets.py` (do not edit by hand). "
         "Every dollar figure is the WInS book ($300,000), not Laura's plan. Friday: re-run with `--basis friday` "
         "and trade from that output, not from this file. The team's 1 Oct vote picks the book; both are here.", "",
         "## Five stop rules (read aloud before the first order)", "",
         "1. **Name:** the name WInS shows must match the 'Exact WInS name' column (bonds: coupon and maturity). "
         "IBTN is INSCORP Inc, never a buy. Two students read ticker, name, quantity and total aloud.",
         "2. **Total:** stop, do not submit, if the Preview total is outside the stop band in the detail table "
         "(the larger of 1% and the price band). Unit test: quantity x the price WInS shows (bonds: clean + accrued, "
         "per $100) + commission must be within 1% of the Preview total. A 10x or 1,000x gap means the bond unit is "
         "wrong (PM-02).",
         "3. **Price:** do not pay above the max price. If a limit order exists, set the limit at the ask shown, "
         "never above the max. Bonds: the WInS price must sit inside the 25bp curve band, or use the alternate.",
         "4. **Cash:** after each ETF fill, WInS cash must be at or above the 'worst case' cash figure; if it is lower, "
         "stop and find out why. Bonds settle at the end of the day: check cash the next morning. Never below $1,000.",
         "5. **No repeats, no same-day sells:** a pending order is not a failed order. Check Order History before "
         "re-entering anything. Never sell something the day it was bought; log a mistake, fix it another day.", "",
         "## Order sequence and why", "",
         "The order is for cash control only. It is not the IPS rule \"latest payments first\": that rule says which "
         "payments a short 2027 deposit funds, not the order of WInS trades.", "",
         "1-5. **iBonds ETFs (IBTR, IBTQ, IBTP, IBTO, IBTM), Friday.** They fill at live prices, so the cash they use "
         "is known at once. IBTR is also a small first order, a safe way to learn the order screen. Place them after "
         "the first hour: thin funds, wide spreads at the open, and the WInS FAQ rule that an order may take at most "
         "half of a security's market volume (we read that as the volume traded so far that day: UNVERIFIED).",
         "6-10. **Treasury bonds (Nov-2041 ... Feb-2037), Friday.** WInS fills bonds at end-of-day prices, so their "
         "cash is known only after the close; sizing them after the iBonds have filled keeps cash safe.",
         "11. **VT (Portfolio book only), the next session (Mon 5 Oct ET), once all five bonds show Filled.** It is "
         "sized from the cash WInS then shows (`--cash-before-vt`), and WInS Order History shows the payments and the "
         "floor bought before any stocks, as the IPS describes.", ""]
    for book, rows in books.items():
        L += md_book(book, rows, ctx)
        L += [f"Details, {book}:", ""] + md_detail(rows)
    if trims:
        L += [f"Re-sized to keep $1,000 of cash in the worst case: trimmed {', '.join(trims)} by $1,000 face each.", ""]
    L += ["## Alternates: the clean price range that passes the 25bp curve check", "",
          f"Curve {ctx['curve_date']}. Use an alternate only when the planned bond fails its check or is not listed, "
          "and only if the WInS price sits inside this range. MODEL bands; WInS listing of every alternate is UNVERIFIED.", "",
          "| Alternate | CUSIP | Accept a WInS clean price from | to | WInS price seen | Verdict |", "|---|---|---|---|---|---|"]
    for r in ctx["alternates"]:
        seen = f"{r['wins_clean']:.3f} ({r['wins_asof']}), gap {r['gap_bp']:+.0f}bp" if "wins_clean" in r else "not seen"
        L.append(f"| {r['id']} | {r['cusip']} | {r['band_low']:.3f} | {r['band_high']:.3f} | {seen} | "
                 f"{r.get('verdict', '-')} |")
    L += ["", "## How the columns are built", "",
          "- **Reference price:** ETFs: the closing price on the date shown (WInS where the team saw it, else the "
          "issuer/Nasdaq close); bonds: the clean price WInS showed (per $100 face) plus accrued interest. Ticket "
          "prices on Friday come only from WInS or a timestamped close (PM-29).",
          f"- **Max price:** ETFs: reference x (1 + the larger of 0.5% and two daily standard deviations over 20 "
          f"sessions). Bonds: the clean price at a yield {BOND_MOVE_BP}bp below the reference yield.",
          "- **2x-volume check:** shares / (2 x 30-session average daily volume), the official rule; the column also "
          "shows shares / the 20-session median day (kit rule: at most 10%). Every order is also below half of the "
          "lowest day in 20 sessions (the WInS FAQ rule, worst full day). Volumes: Nasdaq consolidated, complete sessions.",
          "- **Yield check:** the yield of the WInS price minus the yield of the price from the official par curve "
          "(M1_METHOD.md section C); over 25bp either way = stale or wrong, use the alternate.",
          "- **Bond quantity:** face value in dollars. The WInS unit (dollars, $1,000 bonds or $100 units) is "
          "UNVERIFIED: enter whatever makes the Preview total land inside the stop band.", ""]
    L += ["## Checks (Gate C, tickets)", "", "| Check | Passed | Detail |", "|---|---|---|"]
    groups = {}
    for c, item, ok, det in checks:
        groups.setdefault(c, []).append((item, ok, det))
    for c, items in groups.items():
        fails = [f"{i} ({d})" for i, ok, d in items if not ok]
        if c in ("C5 ledger", "C6 words"):
            det = "; ".join(f"{i}: {d}" for i, ok, d in items)
        else:
            det = "all tickets" if not fails else "FAIL: " + "; ".join(fails)
        L.append(f"| {c} | {sum(ok for _, ok, _ in items)} of {len(items)} | {det} |")
    L += ["", "## Times (from `rab/trades/trades_clock.py`, zoneinfo)", "", clock.table(), ""]
    open(path, "w").write("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--basis", choices=["locked", "friday"], default="locked")
    ap.add_argument("--units", choices=["sheet", "rule"])
    ap.add_argument("--trade-date", default="2026-10-02")
    ap.add_argument("--wins-prices", default=os.path.join(HERE, "wins_prices_friday.csv"))
    ap.add_argument("--md", help="write the markdown here (default by mode)")
    ap.add_argument("--swap", action="append", default=[], metavar="OLD=NEW",
                    help='use a named alternate, e.g. --swap "T 4.250%% 15-Nov-2040=T 1.375%% 15-Nov-2040" (needs --units rule)')
    ap.add_argument("--book", choices=["both", "Portfolio", "BookL"], default="both",
                    help="which book to build (the 1 Oct vote decides; required with --cash-after-etfs)")
    ap.add_argument("--cash-after-etfs", type=float, help="Friday: the cash WInS shows after the five iBonds orders "
                    "filled; bonds are then re-sized from it (use with --units rule)")
    ap.add_argument("--cash-before-vt", type=float, help="Portfolio, next session: the cash WInS shows once the bonds "
                    "have filled; VT (order 11) is sized from it, never above the plan share")
    a = ap.parse_args()
    td = date.fromisoformat(a.trade_date)
    if a.cash_after_etfs is not None and a.book == "both":
        ap.error("--cash-after-etfs needs --book Portfolio or --book BookL (the cash differs by book)")
    if a.cash_before_vt is not None and a.book != "Portfolio":
        ap.error("--cash-before-vt needs --book Portfolio (Book L holds no VT)")
    ctx = locked_context(td) if a.basis == "locked" else friday_context(td, a.wins_prices)
    ctx["alternates"] = alternates_check(ctx)
    ctx["cash_after_etfs"] = a.cash_after_etfs
    ctx["cash_before_vt"] = a.cash_before_vt
    units_mode = a.units or ("sheet" if a.basis == "locked" else "rule")
    for sw in a.swap:
        if units_mode != "rule":
            ap.error("--swap needs --units rule (the Sheet has no units for an alternate)")
        old, new = [x.strip() for x in sw.split("=")]
        add_swap(ctx, old, new)
    units = units_sheet() if units_mode == "sheet" else units_rule(ctx)
    trims = []
    books = {}
    for book in (("Portfolio", "BookL") if a.book == "both" else (a.book,)):
        u = units[book]
        if book == "Portfolio" and a.cash_before_vt is not None:
            u = size_vt_from_cash(u, ctx)
        if units_mode == "rule":
            u, t = trim_for_float(book, u, ctx)
            trims += [f"{book}: {x}" for x in t]
        books[book] = build(book, u, ctx)
    numbers = yaml.safe_load(open(os.path.join(ROOT, "rab/numbers.yaml")))["numbers"]
    checks = run_checks(books, ctx, numbers, units_mode)
    if (a.basis == "locked" and units_mode == "sheet" and a.cash_after_etfs is None and a.cash_before_vt is None
            and a.book == "both" and not a.swap):
        csv_p, md_p = os.path.join(HERE, "tickets.csv"), a.md or os.path.join(HERE, "tickets.md")
    else:
        tag = f"{ctx['curve_date'].isoformat()}_{a.basis}_{units_mode}" + ("" if a.book == "both" else f"_{a.book}") \
            + ("_swap" if a.swap else "") + ("_vt" if a.cash_before_vt is not None else "")
        csv_p, md_p = os.path.join(HERE, "out", f"tickets_{tag}.csv"), a.md or os.path.join(HERE, "out", f"tickets_{tag}.md")
    write_csv(csv_p, books)
    write_md(md_p, books, ctx, checks, trims, units_mode)
    others = [os.path.join(HERE, f) for f in ("M9_selection.md", "friday_checklist.md", "october_trade.md")]
    words = text_check([md_p, csv_p] + [p for p in others if os.path.exists(p)])
    checks += words
    write_md(md_p, books, ctx, checks, trims, units_mode)
    # plan-split drift warning (information only; the split is the team's typed input). M1_METHOD.md section F.
    L = m1.liability(ctx["cv"], "nov15")
    y1, y5 = float(ctx["row"]["1 Yr"]) / 100, float(ctx["row"]["5 Yr"]) / 100
    left = START_CASH - L["fwd_2027"]
    G = left * (1 + y1) + 150_000
    floor = 150_000 / (1 + y5) ** 5
    tot = L["fwd_2028"] + G
    split = {"ladder": L["fwd_2028"] / tot, "floor": floor / tot, "vt": (G - floor) / tot}
    print(f"{ctx['label']}\ncurve {ctx['curve_date']}: ten payments cost ${L['fwd_2027']:,.0f} on 1 Jan 2027 "
          f"(Nov-15 basis, MODEL); plan split ladder {split['ladder']:.1%} / floor {split['floor']:.1%} / stock fund "
          f"{split['vt']:.1%} vs typed 65.9 / 25.3 (24.3 + 1 cash) / 8.7")
    if abs(split["vt"] - SPLIT["vt"]) > 0.01:
        print("  NOTE: the stock-fund share moved more than 1 point from the typed split: a team decision, "
              "not applied here (see october_trade.md trigger B)")
    for book, rows in books.items():
        tl = sum(r["cost_locked"] for r in rows)
        print(f"{book}: {len(rows)} tickets, total ${tl:,.2f}, cash left ${rows[-1]['cash_after_locked']:,.2f}; worst-case cash "
              f"${min(r['cash_after_worst'] for r in rows):,.2f}")
    bad = [c for c in checks if not c[2]]
    for c in bad:
        print("FAIL", c)
    print(f"checks: {len(checks) - len(bad)} pass, {len(bad)} fail; wrote {os.path.relpath(csv_p, ROOT)}, "
          f"{os.path.relpath(md_p, ROOT)}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
