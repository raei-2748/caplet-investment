"""WS7 devil's advocate, round 5 (30 Sep 2026): read-only checks behind the memo challenges. MODEL, one build (this
script), not Gate-B checked: quote as UNVERIFIED until a stream reproduces them. Reuses rab/models code unchanged
(m4_gap_owner mechanism C = the adopted owner chain; m1_ladder holder cash flows = the locked reinvest.* basis).
Run from the worktree root:  PYTHONDONTWRITEBYTECODE=1 /Users/ray/Research/rab-ws/.venv/bin/python rab/redteam/ws7_da_r5_checks.py
[1] D6 share sweep under the adopted owner (C): P(Laura keeps >= 10% of gift), E[gift], kept p5, P(gift < $145k).
[2] D6 robust s* when yearly costs (f x $465k, all assets) are paid from the stock fund 2028-2033 (M8's cost input;
    at f = 1% the drag reproduces M8's typical top $175k -> $167k).
[3] Cost to keep all ten payments whole if cash earns only r: rung by rung (kit, reinvest.bookL_buffer_cost method)
    vs one pooled dedicated reserve of the same ten WInS-listed holdings (linear programme, classic dedication).
[4] Post-2033 top-up: extra reserve on 1 Jan 2033 to keep payments whole if cash earns 5% before 2033 and r after.
[5] Odds the IBTR 'test' fails: share of 3- and 9-session falls in the average 5/7/10/20-year par yield > 26.2bp."""
import contextlib, io, os, sys
from datetime import date
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import brentq, linprog

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "rab" / "models"))
import m4_gap_owner as GO  # noqa: E402
import m4_ladder_gap as LG  # noqa: E402
with contextlib.redirect_stdout(io.StringIO()):
    import m1_ladder as M  # noqa: E402

print("[1] D6 share sweep, adopted owner C (Laura's part first, top lowered in 2031 by what it cannot cover)")
gp = GO.gaps()
data = LG.primary_GK()
shares = [0.0, 0.25, 1 / 3, 0.40, 0.42, 0.50, 2 / 3]
for scen in ["Book L, today's yields", "Book L, today's yields - 2 points", "Book L, 2%"]:
    v = gp[scen]
    print(f"  {scen} (gap valued 1 Jan 2031 ${v['g31']:,.0f})")
    for m in LG.MODELS:
        B3, B5, phi, F = data[m]
        cells = []
        for s in shares:
            G, K, U, low, short = GO.outcome("C", B3, B5, phi, F, s, v["g31"], v["rate"])
            cells.append(f"s={s:.2f} keep10 {np.mean(K >= GO.KAPPA * G):.1%} E[G] ${G.mean() / 1e3:.1f}k "
                         f"Kp5 ${np.percentile(K, 5) / 1e3:.1f}k G<145k {np.mean(G < GO.A):.2%}")
        print(f"    {m:5s} " + " | ".join(cells))

print("\n[2] D6 robust share s* (PR-4/PR-5, grid 0.01) with yearly costs f x $465k paid from the stock fund, 2028-33")
grid = np.round(np.arange(0, 1.001, 0.01), 2)
drag = lambda f, n: f * 465_000 * sum(1.07 ** k for k in range(n))
for scen in ["none (STRIPS basis, M4 as specified)", "Book L, today's yields"]:
    v = gp[scen]
    for f in [0.0, 0.0005, 0.001, 0.0025, 0.005, 0.01]:
        out = []
        for m in LG.MODELS:
            B3, B5, phi, F = data[m]
            B3f, B5f = np.maximum(B3 - drag(f, 3), 1.0), np.maximum(B5 - drag(f, 5), 0.0)
            best, pk_half = None, None
            for s in grid:
                G, K, *_ = GO.outcome("C", B3f, B5f, phi, F, s, v["g31"], v["rate"])
                pk = np.mean(K >= GO.KAPPA * G)
                if s == 0.5:
                    pk_half = pk
                if np.mean(G < GO.A) <= GO.PD_MAX and pk >= GO.CONF:
                    best = float(s)
            out.append(f"{m} s*={best} keep10@half={pk_half:.1%}")
        print(f"  {scen[:24]:24s} f={f:.2%}: " + " | ".join(out))

print("\n[3]/[4] Coupon reinvestment: rung by rung vs pooled dedicated reserve (same ten holdings, 28 Sep prices)")
with contextlib.redirect_stdout(io.StringIO()):
    rows = M.load_rows([os.path.join(M.ROOT, "rab/data/treasury_par_2000_2026/2026.csv")])
    row = next(r for r in rows if r["_date"] == date(2026, 9, 28))
    S, cv = row["_date"], M.Curve(row)
    wins = M.read_wins(os.path.join(M.ROOT, "rab/data/wins/wins_prices_2026-09-28.csv"))
    look = M.section_d(row, S)
H, Fc = M.ibond_holdings(), M.ishares_facts()
names = sorted([n for n, w in wins.items() if w["bookL_size"]], key=lambda n: int(wins[n]["bookL_pays_year"]))
PAY = [date(y, 1, 1) for y in range(2033, 2043)]
fl, px, qL = {}, {}, {}
for n in names:
    w = wins[n]
    fl[n] = M.holder_flows(n, w, 1.0 if w["type"] == "ETF" else 100.0, S, look, H, Fc)
    px[n] = w["price"] if w["type"] == "ETF" else w["price"] + M.accrued(w["coupon"], w["mat"], S)
    qL[n] = w["bookL_size"] / (1 if w["type"] == "ETF" else 100)
def g(d, T, r):
    return cv.df(d) / cv.df(T) if r == "curve" else (1 + r / 2) ** (2 * M.years(d, T))
def val(n, T, r):
    return sum(a * g(d, T, r) for d, a in fl[n] if d <= T)
qc = {n: 50_000 / val(n, T, "curve") for n, T in zip(names, PAY)}
base = sum(qc[n] * px[n] for n in names)
bookL = sum(qL[n] * px[n] for n in names)
def rung(r):
    return sum(px[n] * 50_000 / val(n, T, r) for n, T in zip(names, PAY))
def lp(r, alpha=0.0):
    A = [[-val(n, Tk, r) for n in names] for Tk in PAY]
    b = [-sum(50_000 * g(Tj, Tk, r) for Tj in PAY[:k + 1]) for k, Tk in enumerate(PAY)]
    res = linprog([px[n] for n in names], A_ub=A, b_ub=b, bounds=[(alpha * qc[n], None) for n in names], method="highs")
    return res.fun, dict(zip(names, res.x))
print(f"  Book L as sized ${bookL:,.0f} (check: + reinvest.bookL_buffer_cost at 2% = ${bookL + 20399:,.0f}); "
      f"resized to $50,000/rung at forwards ${base:,.0f}")
for r in [0.04, 0.03, 0.025, 0.02, 0.0]:
    c0, x0 = lp(r)
    c5, _ = lp(r, 0.5)
    print(f"  cash earns {r:.1%}: rung by rung ${rung(r):,.0f} (+{rung(r) - base:,.0f}) | pooled LP ${c0:,.0f} "
          f"(+{c0 - base:,.0f}) | pooled LP keeping >= half of every dated rung ${c5:,.0f} (+{c5 - base:,.0f})")
    if r == 0.02:
        print("     free LP holdings at 2% ($ cost): " + ", ".join(f"{n.split(' 15-')[0]} {x0[n] * px[n]:,.0f}" for n in names))
print(f"  free LP fits $300,000 at 28 Sep prices if cash earns >= {100 * brentq(lambda r: lp(r)[0] - 300_000, 0, 0.05):.2f}%; "
      f"fits $300,000/1.011 (1 Jan 2027 forward roll) if >= {100 * brentq(lambda r: lp(r)[0] - 300_000 / 1.011, 0, 0.06):.2f}%")
T33 = date(2033, 1, 1)
def g2(d, T, r1, r2):
    if T <= T33:
        return (1 + r1 / 2) ** (2 * M.years(d, T))
    if d >= T33:
        return (1 + r2 / 2) ** (2 * M.years(d, T))
    return (1 + r1 / 2) ** (2 * M.years(d, T33)) * (1 + r2 / 2) ** (2 * M.years(T33, T))
for label, q in [("Book L as sized", qL), ("resized to $50,000/rung at forwards", qc)]:
    for r2 in [0.03, 0.02, 0.0]:
        bal = [sum(q[n] * sum(a * g2(d, Tk, 0.05, r2) for d, a in fl[n] if d <= Tk) for n in names)
               - sum(50_000 * g2(Tj, Tk, 0.05, r2) for Tj in PAY[:k + 1]) for k, Tk in enumerate(PAY)]
        need = max(0.0, max(-b / (1 + r2 / 2) ** (2 * M.years(T33, T)) for b, T in zip(bal, PAY)))
        print(f"  [4] {label}: cash 5% to 2033 then {r2:.0%}: extra reserve needed on 1 Jan 2033 ${need:,.0f}")

print("\n[5] IBTR test: falls in the average 5/7/10/20-year par yield larger than the 28 Sep break-even (26.2bp)")
def lvl(years):
    d = pd.concat([pd.read_csv(ROOT / f"rab/data/treasury_par_2000_2026/{y}.csv") for y in years])
    d["Date"] = pd.to_datetime(d["Date"])
    d = d.sort_values("Date").drop_duplicates("Date")
    return d[["5 Yr", "7 Yr", "10 Yr", "20 Yr"]].mean(axis=1).reset_index(drop=True) * 100
for label, yrs in [("2026", [2026]), ("2000-2026", range(2000, 2027))]:
    L = lvl(yrs)
    for h in (3, 9):
        ch = (L.shift(-h) - L).dropna()
        print(f"  {label}: {h}-session changes sd {ch.std():.1f}bp; falls > 26.2bp {np.mean(ch < -26.2):.2%} of {len(ch)}")
