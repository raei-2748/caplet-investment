"""D3_funded_status_log.py - M028: a weekly "funded status" log for the WInS Treasury hedge, and a 2026 backtest of
how closely an IEF/TLH (or IEF/TLT) hedge tracked the value of Laura's ten payments.

Question (phase_C survivors M028): should the team log, from the first WInS trade, the value of Laura's ten payments
on that day's Treasury curve, the ladder cost, the funded ratio and the WInS hedge value, so a Trading Note can say
whether the IEF/TLH mix tracked the promise within X%?

What it does:
 1. LOG MODE (default prints the latest curve date; or --date MM/DD/YYYY; --since MM/DD/YYYY for changes):
    for one treasury.gov curve date it prints (a) the value TODAY of the ten $50k payments (spot PV) and its duration,
    (b) the cost of the payments for 1 January 2027 (exact dates and the Nov-15 STRIPS ladder), (c) the funded ratio
    $300,000 / cost, (d) the modelled % change of the 35.7/64.3 IEF/TLH hedge (holdings-based) and of the payments since
    --since. The team adds one number by hand: the WInS hedge value from the WInS screen.
 2. BACKTEST (--backtest): every 30-trading-day (about 6-week) window in 2026: the modelled hedge % change minus the
    payments' % change ("tracking gap"), for IEF/TLH 35.7/64.3 and IEF/TLT 62.1/37.9. Both funds are valued from their
    actual holdings (S1 snapshot, 2026-09-24) on each day's official curve, coupons received kept as cash.
Inputs and status:
 - Treasury Daily Par Yield Curve 2026 (research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv; home.treasury.gov,
   VERIFIED-PRIMARY, accessed 2026-09-28; refresh with D3_data_snapshot.py).
 - Fund holdings: research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv (iShares latest-holdings, as of 2026-09-24,
   VERIFIED-PRIMARY per S1). ASSUMPTION: the same holdings are used for earlier 2026 dates (funds roll slowly).
 - Weights: IEF 35.7 / TLH 64.3 and IEF 62.1 / TLT 37.9 (S1, from issuer durations 2026-09-24).
 - Curve method: same bootstrap as research/verified_2026-09-27/official_curve_pv.py (ASSUMPTION method).
 - ASSUMPTION: no fund fees, no bid/ask or premium/discount, no dividend timing; this measures curve-shape (twist) risk
   only. Real WInS values also move with fund price noise, so treat the model gap as a lower bound.
Run from the repo root:
   .venv/bin/python research/insight_v1/scripts/D3_funded_status_log.py --backtest
   .venv/bin/python research/insight_v1/scripts/D3_funded_status_log.py --date 09/25/2026 --since 09/01/2026
"""
import argparse
import csv
from collections import defaultdict
from datetime import date

import numpy as np

CURVES = "research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv"
HOLD = "research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv"
TENOR = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
PAY = [date(y, 1, 1) for y in range(2033, 2043)]
STRIPS = [date(y - 1, 11, 15) for y in range(2033, 2043)]
ANCHOR = date(2027, 1, 1)
MIXES = {"IEF/TLH 35.7/64.3": {"IEF": 0.357, "TLH": 0.643}, "IEF/TLT 62.1/37.9": {"IEF": 0.621, "TLT": 0.379}}
WINS_HEDGE = 0.66 * 300_000        # hedge share of the WInS book in option (ii) of the S3 ticket


def load_curves():
    out = []
    for r in csv.DictReader(open(CURVES)):
        m, d, y = r["Date"].split("/")
        par = {t: float(r[k]) for k, t in TENOR.items() if r.get(k) not in (None, "", "N/A")}
        out.append((date(int(y), int(m), int(d)), par))
    return sorted(out)


def build(par):
    ts = sorted(par)
    grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts])
    df = []
    for y in p:
        c = y / 2
        df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]
    lz = np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))


def add_months(d, m):
    y, mo = divmod(d.month - 1 + m, 12)
    return date(d.year + y, mo + 1, min(d.day, 28))


def load_cashflows():
    cf = defaultdict(list)
    for r in csv.DictReader(open(HOLD)):
        if r["fund"] not in ("IEF", "TLH", "TLT"):
            continue
        par, cpn, mat = float(r["par"]), float(r["coupon_pct"]), date.fromisoformat(r["maturity"])
        if mat <= date(2026, 1, 1):
            continue
        cf[r["fund"]].append((mat, par * (1 + cpn / 200)))
        k = 1
        while True:
            d = add_months(mat, -6 * k)
            if d <= date(2025, 12, 31):
                break
            cf[r["fund"]].append((d, par * cpn / 200))
            k += 1
    return {k: (np.array([(d - date(2000, 1, 1)).days for d, _ in v]), np.array([a for _, a in v])) for k, v in cf.items()}


CF = load_cashflows()


def fund_value(name, t, f, since=None):
    """Holdings value on day t (curve f); coupons/principal paid after `since` and on/before t count as cash."""
    days, amt = CF[name]
    td = (t - date(2000, 1, 1)).days
    fut = days > td
    val = (amt[fut] * f((days[fut] - td) / 365.25)).sum()
    if since is not None:
        sd = (since - date(2000, 1, 1)).days
        val += amt[(days > sd) & ~fut].sum()
    return val


def liab_spot(t, f):
    return sum(50_000 * f((p - t).days / 365.25) for p in PAY)


def liab_2027(t, f, dates=PAY):
    return sum(50_000 * f((p - t).days / 365.25) for p in dates) / f((ANCHOR - t).days / 365.25)


def log_line(curves, day, since=None):
    t, par = next((c for c in curves if c[0] == day), (None, None))
    if t is None:
        raise SystemExit(f"{day} not in {CURVES}; refresh with D3_data_snapshot.py")
    f = build(par)
    up, dn = build({k: v + 0.01 for k, v in par.items()}), build({k: v - 0.01 for k, v in par.items()})
    L = liab_spot(t, f)
    dur = (liab_spot(t, dn) - liab_spot(t, up)) / (2 * L * 1e-4)
    ex, st = liab_2027(t, f), liab_2027(t, f, STRIPS)
    print(f"{t}: payments' value today ${L:,.0f} (duration {dur:.2f}y, ${(liab_spot(t, dn) - liab_spot(t, up)) / 2:,.0f}"
          f" per bp); cost for 1 Jan 2027: exact dates ${ex:,.0f}, Nov-15 STRIPS ${st:,.0f}; funded ratio "
          f"$300k/STRIPS cost = {300_000 / st:.3f} ({'fits' if st <= 300_000 else 'does NOT fit'} under $300k)")
    if since is not None:
        t0, par0 = next(c for c in curves if c[0] == since)
        f0 = build(par0)
        L0 = liab_spot(t0, f0)
        print(f"   since {t0}: payments' value {L / L0 - 1:+.2%}")
        for name, w in MIXES.items():
            h = sum(wi * fund_value(n, t, f, since=t0) / fund_value(n, t0, f0) for n, wi in w.items()) - 1
            print(f"   {name}: modelled hedge {h:+.2%}; gap {h - (L / L0 - 1):+.2%} = "
                  f"${(h - (L / L0 - 1)) * WINS_HEDGE:+,.0f} on a ${WINS_HEDGE:,.0f} WInS hedge")


def backtest(curves, window=30):
    fs = [(t, build(p)) for t, p in curves]
    Ls = np.array([liab_spot(t, f) for t, f in fs])
    print(f"Backtest on {len(fs)} official curve dates, {fs[0][0]} to {fs[-1][0]}; window {window} trading days")
    print(f"  payments' value today moved from ${Ls[0]:,.0f} to ${Ls[-1]:,.0f} ({Ls[-1] / Ls[0] - 1:+.1%}) over the period")
    for name, w in MIXES.items():
        gaps = []
        for i in range(len(fs) - window):
            (t0, f0), (t1, f1) = fs[i], fs[i + window]
            h = sum(wi * fund_value(n, t1, f1, since=t0) / fund_value(n, t0, f0) for n, wi in w.items()) - 1
            gaps.append(h - (Ls[i + window] / Ls[i] - 1))
        g = np.array(gaps)
        full = sum(wi * fund_value(n, fs[-1][0], fs[-1][1], since=fs[0][0]) / fund_value(n, fs[0][0], fs[0][1])
                   for n, wi in w.items()) - 1
        print(f"  {name}: {len(g)} windows; gap (hedge % change minus payments' % change) mean {g.mean():+.2%}, "
              f"sd {g.std():.2%}, p5 {np.percentile(g, 5):+.2%}, p95 {np.percentile(g, 95):+.2%}, "
              f"worst {g[np.abs(g).argmax()]:+.2%} -> on a ${WINS_HEDGE:,.0f} WInS hedge: 95% of windows within "
              f"${np.percentile(np.abs(g), 95) * WINS_HEDGE:,.0f}; whole period: hedge {full:+.1%} vs payments "
              f"{Ls[-1] / Ls[0] - 1:+.1%}")
    # typical 6-week move of the payments' value, for scale
    moves = np.array([Ls[i + window] / Ls[i] - 1 for i in range(len(Ls) - window)])
    print(f"  for scale: the payments' value itself moved by sd {moves.std():.2%} over 6-week windows "
          f"(p5 {np.percentile(moves, 5):+.2%}, p95 {np.percentile(moves, 95):+.2%}) = "
          f"${np.percentile(np.abs(moves), 95) * WINS_HEDGE:,.0f} on the WInS hedge at the 95th percentile")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--since")
    ap.add_argument("--backtest", action="store_true")
    a = ap.parse_args()
    curves = load_curves()
    parse = lambda s: date(int(s.split("/")[2]), int(s.split("/")[0]), int(s.split("/")[1]))
    if a.backtest:
        backtest(curves)
    day = parse(a.date) if a.date else curves[-1][0]
    log_line(curves, day, parse(a.since) if a.since else None)


if __name__ == "__main__":
    main()
