"""Caplet WInS portfolio health check (read-only). Holdings = WInS fills 7-8 Oct 2026."""
import csv, io, math, sys, urllib.request, datetime as dt
import yfinance as yf, numpy as np, pandas as pd

ETFS = {  # ticker: (shares, fill, target weight, job)
    "IBTM": (4503, 21.65, .326, "Jan-2033 payment + facility floor"),
    "IBTO": (1024, 22.86, .078, "Jan-2034"), "IBTP": (927, 23.90, .074, "Jan-2035"),
    "IBTQ": (894, 23.46, .070, "Jan-2036"), "IBTR": (853, 23.24, .066, "Jan-2037"),
    "VT":   (167, 158.83, .087, "Growth"),
}
BONDS = {  # name: (units of $1000, coupon, maturity, fill clean, target)
    "T37": (20, 4.750, dt.date(2037, 2, 15), 96.019, .066),
    "T38": (20, 4.500, dt.date(2038, 5, 15), 93.076, .062),
    "T39": (18, 4.375, dt.date(2039, 11, 15), 90.005, .056),
    "T40": (18, 4.250, dt.date(2040, 11, 15), 87.724, .053),
    "T41": (20, 3.125, dt.date(2041, 11, 15), 74.955, .050),
}
CASH = 3513.79
FREEZE = dt.datetime(2026, 11, 7, 8, 0)  # AEDT

def par_curve():
    today = dt.date.today()
    for ym in (today.strftime("%Y%m"), (today.replace(day=1) - dt.timedelta(days=1)).strftime("%Y%m")):
        url = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/"
               f"all/{ym}?type=daily_treasury_yield_curve&field_tdr_date_value_month={ym}&page&_format=csv")
        try:
            rows = list(csv.DictReader(io.StringIO(urllib.request.urlopen(url, timeout=20).read().decode())))
            if rows: return rows[0]
        except Exception as e: print("curve fetch failed:", e, file=sys.stderr)
    return None

def interp(curve, yrs):
    pts = [(1,"1 Yr"),(2,"2 Yr"),(3,"3 Yr"),(5,"5 Yr"),(7,"7 Yr"),(10,"10 Yr"),(20,"20 Yr"),(30,"30 Yr")]
    xs = [p for p,k in pts if curve.get(k)]; ys = [float(curve[k]) for p,k in pts if curve.get(k)]
    return float(np.interp(yrs, xs, ys)) / 100

def bond_price(c, mat, y, settle):
    # clean price per 100, semiannual, approx accrual
    cfs, d = [], mat
    while d > settle:
        cfs.append(d); d = d.replace(year=d.year - (1 if d.month <= 6 else 0), month=(d.month - 6 - 1) % 12 + 1)
    prev = d; nxt = cfs[-1]
    frac = (nxt - settle).days / (nxt - prev).days
    pv = sum((c / 2) / (1 + y / 2) ** (i + frac) for i in range(len(cfs))) + 100 / (1 + y / 2) ** (len(cfs) - 1 + frac)
    acc = c / 2 * (1 - frac)
    dur = sum((i + frac) / 2 * ((c / 2) + (100 if i == len(cfs) - 1 else 0)) / (1 + y / 2) ** (i + frac) for i in range(len(cfs))) / pv
    return pv - acc, acc, dur / (1 + y / 2)

def main():
    today = dt.date.today(); out = []
    px = yf.download(list(ETFS) + ["^TNX"], period="1y", auto_adjust=True, progress=False)["Close"]
    rows, total = [], CASH
    for t, (n, fill, tw, job) in ETFS.items():
        info = yf.Ticker(t).info
        last = float(px[t].dropna().iloc[-1]); nav = info.get("navPrice")
        prem = (last / nav - 1) * 100 if nav else float("nan")
        mv = n * last; total += mv
        rows.append(dict(h=t, job=job, units=n, price=round(last, 2), mv=mv, tw=tw, pnl=n*(last-fill),
                         prem=round(prem, 2), ytd=info.get("ytdReturn")))
    curve = par_curve(); cdate = curve.get("Date") if curve else "n/a"
    bond_dur = 0
    for b, (u, c, mat, fill, tw) in BONDS.items():
        yrs = (mat - today).days / 365.25
        if curve:
            y = interp(curve, yrs); clean, acc, md = bond_price(c, mat, y, today)
        else:
            y, clean, acc, md = float("nan"), fill, 0, 10
        mv = u * 10 * (clean + acc); total += mv; bond_dur += mv * md
        rows.append(dict(h=b, job=f"Jan-{mat.year+1}", units=u, price=round(clean, 3), mv=mv, tw=tw,
                         pnl=u*10*(clean-fill), prem=float("nan"), ytd=round(y*100, 3)))
    df = pd.DataFrame(rows); df["w"] = df.mv / total; df["drift_pt"] = (df.w - df.tw) * 100
    print(f"Caplet WInS check {dt.datetime.now():%Y-%m-%d %H:%M} | curve date {cdate} | days to freeze {(FREEZE-dt.datetime.now()).days}")
    print(f"Est. value ${total:,.0f} ({(total/300000-1)*100:+.2f}%), cash ${CASH:,.0f} ({CASH/total*100:.1f}%)")
    print(df[["h","units","price","mv","w","tw","drift_pt","pnl","prem"]].to_string(index=False,
          formatters={"mv":"{:,.0f}".format,"w":"{:.1%}".format,"tw":"{:.1%}".format,"drift_pt":"{:+.2f}".format,"pnl":"{:+,.0f}".format}))
    # rate sensitivity: iBond ETFs approx duration = years to Dec maturity
    etf_dur = sum(ETFS[t][0]*float(px[t].dropna().iloc[-1])*((dt.date(y,12,15)-today).days/365.25)
                  for t,y in [("IBTM",2032),("IBTO",2033),("IBTP",2034),("IBTQ",2035),("IBTR",2036)])
    dv = (etf_dur + bond_dur) * 0.005
    print(f"Rate sensitivity: +/-50bp parallel ~ -/+${dv:,.0f} ({dv/total*100:.1f}% of value)")
    r = px.pct_change().dropna()
    ladder = r[["IBTM","IBTO","IBTP","IBTQ","IBTR"]].mean(axis=1)
    c = r["VT"].corr(ladder); c90 = r["VT"].tail(63).corr(ladder.tail(63))
    print(f"VT vs ladder daily corr: 1y {c:+.2f}, last 3m {c90:+.2f}; VT 1y vol {r['VT'].std()*math.sqrt(252)*100:.1f}%")
    flags = []
    if (df.drift_pt.abs() > 2).any(): flags.append("drift >2pt: " + ", ".join(df.h[df.drift_pt.abs() > 2]))
    if (df.prem.abs() > 0.5).any(): flags.append("ETF premium/discount >0.5%: " + ", ".join(df.h[df.prem.abs() > 0.5]))
    if CASH < 1000: flags.append("cash below $1,000")
    print("FLAGS:", "; ".join(flags) if flags else "none")

if __name__ == "__main__": main()
