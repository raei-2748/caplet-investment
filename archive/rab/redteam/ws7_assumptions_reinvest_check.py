"""WS7 red team (key-assumptions challenge), RAB Kit, 2026-09-30 (Sydney). AI-generated (Claude Code) for Team Caplet.
How weak is the coupon-reinvestment assumption behind the IPS's 'high certainty'? Uses rab/models/m1_ladder.py read-only
(Book L holder cash flows, M1_METHOD.md E1) and adds: break-even flat reinvestment rates; Book L at MODEL prices with its
break-even fall; historical change-analog replays (FRED CMT 1962+, yield changes since each start month added to the
28 Sep 2026 curve, floored at 0) for two reinvestment policies ('matched' = each coupon buys a zero to its payment date,
'bills' = rolled in 1-year bills); Japan-1990 and US-2000/2007 replays. MODEL outputs, not in numbers.yaml (UNVERIFIED
for team outputs until WS1 adopts them). Deterministic; writes nothing.
Run from the worktree root: /Users/ray/Research/rab-ws/.venv/bin/python rab/redteam/ws7_assumptions_reinvest_check.py"""
import sys, os, csv, math, bisect, io, contextlib
from datetime import date, timedelta
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models'))
import m1_ladder as M
from scipy.optimize import brentq

ROOT = M.ROOT
rows = M.load_rows([os.path.join(ROOT, "rab/data/treasury_par_2000_2026/2026.csv")])
row = next(r for r in rows if r["_date"] == date(2026, 9, 28))
s = row["_date"]; cv = M.Curve(row)
wins = M.read_wins(os.path.join(ROOT, "rab/data/wins/wins_prices_2026-09-28.csv"))
with contextlib.redirect_stdout(io.StringIO()):
    look = M.section_d(row, s)
H, F = M.ibond_holdings(), M.ishares_facts()
rungs = []
for name, w in wins.items():
    if not w["bookL_size"]:
        continue
    T = date(int(w["bookL_pays_year"]), 1, 1); qty = w["bookL_size"]
    px = w["price"] if w["type"] == "ETF" else w["price"] + M.accrued(w["coupon"], w["mat"], s)
    cost = qty * px / (100 if w["type"] == "Treasury" else 1)
    fl = M.holder_flows(name, w, qty, s, look, H, F)
    y = M.irr(fl, s, cost)
    rungs.append(dict(name=name, T=T, cost=cost, fl=fl, y=y, typ=w["type"]))
rungs.sort(key=lambda r: r["T"])
cost_tot = sum(r["cost"] for r in rungs); comm = 175
DFA = cv.df(M.A27)
print(f"Book L spot cost (model accrued) ${cost_tot:,.0f} + comm ${comm}; fwd to 1 Jan 2027 ${(cost_tot+comm)/DFA:,.0f}; "
      f"fwd headroom ${300000-(cost_tot+comm)/DFA:,.0f}")
# share of each rung's cash that arrives before maturity as coupons (not principal)
for r in rungs:
    tot = sum(a for d, a in r["fl"] if a > 0)
    last = max(d for d, a in r["fl"])
    pre = sum(a for d, a in r["fl"] if a > 0 and d < last) if r["typ"] == "Treasury" else None
    r["cpn_share"] = (pre / tot) if pre is not None else None

def V(r, rate):
    return M.grow(r["fl"], r["T"], rate, cv)

def total(rate):
    return sum(V(r, rate) for r in rungs)

def buffer(rate, net=False):
    if not net:
        return sum(r["cost"] * (50000 / V(r, rate) - 1) for r in rungs if V(r, rate) < 50000)
    # netted: surplus of a rung is carried to the next payment at `rate`; deficits need more of that holding
    carry, buf = 0.0, 0.0
    prevT = None
    for r in rungs:
        if prevT is not None:
            carry *= (1 + rate / 2) ** (2 * M.years(prevT, r["T"]))
        v = V(r, rate) + carry
        if v >= 50000:
            carry = v - 50000
        else:
            buf += r["cost"] * ((50000 - carry) / V(r, rate) - 1); carry = 0.0
        prevT = r["T"]
    return buf

print("\n[1] Flat reinvestment rate r (all coupons and fund income reinvested at r to each 1 Jan payment date)")
for rate in (0.0, 0.01, 0.02, 0.03, 0.035, 0.04, 0.045, 0.05):
    vs = [V(r, rate) for r in rungs]
    print(f"  r={rate:5.1%}: delivered ${sum(vs):,.0f}; rungs under $50k: {sum(v < 50000 for v in vs)}; worst rung "
          f"${min(vs):,.0f}; buffer (no netting) ${buffer(rate):,.0f}, netted ${buffer(rate, True):,.0f}")
r_tot = brentq(lambda x: total(x) - 500000, -0.02, 0.1)
r_all = brentq(lambda x: min(V(r, x) for r in rungs) - 50000, -0.02, 0.1)
head_spot = 300000 * DFA - cost_tot - comm
r_head = brentq(lambda x: buffer(x) - head_spot, -0.02, 0.07)
r_head_n = brentq(lambda x: buffer(x, True) - head_spot, -0.02, 0.07)
print(f"  break-even flat rate: total $500k at {r_tot:.2%}; every rung $50k at {r_all:.2%};")
print(f"  2027 deposit can still fund the buffer (spot headroom ${head_spot:,.0f}) down to r = {r_head:.2%} "
      f"(netted {r_head_n:.2%})")
print("  own yields:", ", ".join(f"{r['name'].split(' 15-')[0]} {r['y']:.2%}" for r in rungs))
print("  coupon share of cash before maturity (bonds):", ", ".join(f"{r['name']} {r['cpn_share']:.0%}" for r in rungs if r['cpn_share']))

# ---------------- historical change analog -------------------------------------------------------------------
def load_fred(t):
    out = {}
    for rr in csv.DictReader(open(os.path.join(ROOT, f"rab/data/fred/DGS{t}.csv"))):
        v = rr[f"DGS{t}"]
        if v not in ("", "."):
            out[date.fromisoformat(rr["observation_date"])] = float(v)
    ks = sorted(out); return ks, [out[k] for k in ks]
TEN = {1: "1", 2: "2", 3: "3", 5: "5", 7: "7", 10: "10", 20: "20", 30: "30"}
SER = {t: load_fred(n) for t, n in TEN.items()}
def at(t, d):
    ks, vs = SER[t]
    i = bisect.bisect_right(ks, d) - 1
    if i < 0 or (d - ks[i]).days > 10:
        return None
    return vs[i]
def cmt(d, m):
    """CMT yield (%) at maturity m years on date d, linear across available tenors, flat outside."""
    pts = [(t, at(t, d)) for t in TEN]
    pts = [(t, v) for t, v in pts if v is not None]
    if len(pts) < 2:
        return None
    ts, vs = zip(*pts)
    if m <= ts[0]: return vs[0]
    if m >= ts[-1]: return vs[-1]
    j = bisect.bisect_left(ts, m)
    return vs[j-1] + (vs[j] - vs[j-1]) * (m - ts[j-1]) / (ts[j] - ts[j-1])

def fwd_zero(d1, T):
    """today's forward zero rate (semiannual) from d1 to T."""
    tau = M.years(d1, T)
    if tau <= 0: return 0.0
    return 2 * ((cv.df(d1) / cv.df(T)) ** (1 / (2 * tau)) - 1)

def replay(d0, policy):
    """Deliver each rung with coupons reinvested under historical yield changes since d0 (added to today's curve)."""
    out = []
    for r in rungs:
        v = 0.0
        for d, a in r["fl"]:
            if d >= r["T"]:
                v += a; continue
            u = d - s; dh = d0 + u
            if policy == "matched":
                m = max(M.years(d, r["T"]), 0.25)
                h0, h1 = cmt(d0, m), cmt(dh, m)
                rate = max(0.0, fwd_zero(d, r["T"]) + (h1 - h0) / 100)
                v += a * (1 + rate / 2) ** (2 * M.years(d, r["T"]))
            else:  # roll 1-year bills: today's 1-year par 4.59% + historical 1-year change, floored at 0, monthly steps
                g, t = a, d
                y0 = at(1, d0)
                while t < r["T"]:
                    t2 = min(t + timedelta(days=30), r["T"])
                    yh = at(1, d0 + (t - s))
                    rate = max(0.0, 0.0459 + (yh - y0) / 100)
                    g *= (1 + rate) ** (M.years(t, t2)); t = t2
                v += g
        out.append(v)
    return out

span = M.years(s, date(2042, 1, 1))
starts, d = [], date(1962, 1, 15)
while M.years(d, date(2026, 9, 1)) >= span:
    starts.append(d); m = d.month % 12 + 1; d = date(d.year + (d.month == 12), m, 15)
print(f"\n[2] Historical change-analog replays: {len(starts)} monthly starts {starts[0]}..{starts[-1]} "
      f"(yield changes since the start month, added to today's curve, floored at 0; FRED CMT)")
for pol in ("matched", "bills"):
    res = []
    for d0 in starts:
        vs = replay(d0, pol)
        res.append((d0, sum(vs), sum(max(0, 50000 - v) for v in vs), sum(v < 50000 for v in vs)))
    tots = sorted(x[1] for x in res)
    short = [x for x in res if x[2] > 0]
    n = len(res)
    pct = lambda p: tots[int(p * (n - 1))]
    print(f"  policy {pol}: delivered p5 ${pct(.05):,.0f} / median ${pct(.5):,.0f} / p95 ${pct(.95):,.0f}; "
          f"worst ${tots[0]:,.0f}; starts with any payment short {len(short)}/{n} ({len(short)/n:.0%}); "
          f"total < $500k in {sum(x[1] < 500000 for x in res)/n:.0%}")
    worst = sorted(res, key=lambda x: -x[2])[:5]
    print("    largest shortfalls (sum of rung gaps): " + "; ".join(f"{w[0]:%Y-%m} ${w[2]:,.0f} ({w[3]} rungs)" for w in worst))
    by_dec = {}
    for x in res:
        by_dec.setdefault(x[0].year // 10 * 10, []).append(x[2] > 0)
    print("    share of starts short, by decade: " + ", ".join(f"{k}s {sum(v)/len(v):.0%}" for k, v in sorted(by_dec.items())))
    # recent: start 2007-06 (the 2008-2021 low-rate era)
    for dd in (date(2000, 1, 15), date(2007, 6, 15), date(2008, 9, 15), date(1990, 1, 15), date(1981, 9, 15)):
        x = next((y for y in res if y[0] == dd), None)
        if x: print(f"    start {dd:%Y-%m}: delivered ${x[1]:,.0f}, shortfall ${x[2]:,.0f} over {x[3]} rungs")

# ---------------- [3] Book L at MODEL prices (Laura's real purchase is at market, not WInS prices) + break-even fall
def bookL_cost(bp):
    c = M.Curve(row, bp); tot = 0.0
    for name, w in wins.items():
        if not w["bookL_size"]:
            continue
        q = w["bookL_size"]
        if w["type"] == "Treasury":
            tot += q * M.model_dirty(c, w["coupon"], w["mat"], s) / 100
        else:
            tot += q * M.nav_model(row, H[name], F[name]["shares"], s, bp) * look[name]["ratio"]
    return tot + comm, c
c0, cc = bookL_cost(0.0)
f0 = c0 / cc.df(M.A27)
be = -brentq(lambda b: (lambda x: x[0] / x[1].df(M.A27))(bookL_cost(b)) - 300000, -300, 100, xtol=1e-3)
print(f"\n[3] Book L (as sized) at MODEL prices: spot ${c0:,.0f}; fwd 1 Jan 2027 ${f0:,.0f}; headroom ${300000-f0:,.0f}; "
      f"break-even parallel fall {be:.1f}bp (STRIPS headline: 26.2bp)")

# ---------------- [4] Japan 1990 replay on reinvestment (matched policy, parallel change = Japan long-rate change)
jp = {}
for rr in csv.DictReader(open(os.path.join(ROOT, "rab/data/history/annual_history.csv"))):
    if rr["jpn_ltrate"]:
        jp[int(rr["year"])] = float(rr["jpn_ltrate"])
print("  Japan long rate 1990..2006:", ", ".join(f"{y}:{jp[y]:.1f}" for y in range(1990, 2007) if y in jp))
def replay_parallel(delta_of_year):
    out = []
    for r in rungs:
        v = 0.0
        for d, a in r["fl"]:
            if d >= r["T"]:
                v += a; continue
            k = d.year - 2027
            rate = max(0.0, fwd_zero(d, r["T"]) + delta_of_year(k) / 100)
            v += a * (1 + rate / 2) ** (2 * M.years(d, r["T"]))
        out.append(v)
    return out
for base in (1990, 1991):
    vs = replay_parallel(lambda k: jp.get(base + max(k, 0), jp[max(jp)]) - jp[base])
    print(f"[4] Japan {base} long-rate changes applied to reinvestment (matched): delivered ${sum(vs):,.0f}; shortfall "
          f"${sum(max(0, 50000 - v) for v in vs):,.0f}; rungs short {sum(v < 50000 for v in vs)}")
# US 2007-2021 actual 10y change path, annual
for base in (2000, 2007):
    vs = replay_parallel(lambda k: (cmt(date(base + max(k, 0), 6, 15), 5) or 0) - cmt(date(base, 6, 15), 5))
    print(f"[4] US {base} 5-yr CMT changes, annual steps (matched): delivered ${sum(vs):,.0f}; shortfall "
          f"${sum(max(0, 50000 - v) for v in vs):,.0f}")

# ---------------- [5] bills with no yield change (term premium effect) and per-rung pattern in the 2007 replay
def bills_flat(rate_of_t):
    out = []
    for r in rungs:
        v = 0.0
        for d, a in r["fl"]:
            if d >= r["T"]:
                v += a; continue
            v += a * (1 + rate_of_t) ** M.years(d, r["T"])
        out.append(v)
    return out
vs = bills_flat(0.0459)
print(f"\n[5] bills at today's 1-year 4.59% with NO change: delivered ${sum(vs):,.0f}; shortfall ${sum(max(0,50000-v) for v in vs):,.0f}")
vs = replay(date(2007, 6, 15), "matched")
print("    2007-06 matched replay per payment: " + ", ".join(f"{r['T'].year}: ${v:,.0f}" for r, v in zip(rungs, vs)))
vs = replay(date(2007, 6, 15), "bills")
print("    2007-06 bills replay per payment:   " + ", ".join(f"{r['T'].year}: ${v:,.0f}" for r, v in zip(rungs, vs)))
