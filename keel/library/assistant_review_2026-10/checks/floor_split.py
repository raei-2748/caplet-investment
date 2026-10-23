import sys, math
from datetime import date
from scipy.stats import norm
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import indep_pricer as P
path = sys.argv[1]
J27, J28, D32 = date(2027,1,1), date(2028,1,2), date(2032,12,15)
for day, d0 in (("09/28/2026", date(2026,9,28)), ("10/06/2026", date(2026,10,6)), ("10/13/2026", date(2026,10,13))):
    pts = P.load_curve(path, day); c = P.Curve(pts); y5 = dict(pts)[5]; y1 = dict(pts)[1]
    T = P.yf(J28, D32)
    f_locked = 150000 / (1 + y5) ** 5
    f_semi = 150000 / (1 + y5 / 2) ** (2 * T)
    f_fwd = 150000 * c.df(P.yf(d0, D32)) / c.df(P.yf(d0, J28))
    f_unch = 150000 * c.df(T)
    # plan split on 2 Jan 2028, buyable basis, forward convention
    lad0 = P.ladder(c, d0, P.BUYABLE)
    c27 = lad0 / c.df(P.yf(d0, J27)); left27 = 300000 - c27
    lad28 = lad0 / c.df(P.yf(d0, J28))
    left28 = left27 * c.df(P.yf(d0, J27)) / c.df(P.yf(d0, J28))
    print(f"{day}: 5y par {y5*100:.2f}%  floor cost: locked(annual,5y) {f_locked:,.0f} | semiannual to 15 Dec 2032 {f_semi:,.0f} "
          f"| forward from curve {f_fwd:,.0f} | yields-unchanged {f_unch:,.0f}")
    for lab, F in (("locked", f_locked), ("forward", f_fwd)):
        stock_ex = 150000 - F; stock_in = stock_ex + left28; tot = lad28 + 150000 + left28
        print(f"   [{lab}] stock fund ex-2027-leftover {stock_ex:,.0f}; incl leftover {stock_in:,.0f}; "
              f"2 Jan 2028 split ladder {lad28/tot*100:.1f}% floor {F/tot*100:.1f}% stock {stock_in/tot*100:.1f}% (total {tot:,.0f}; ladder {lad28:,.0f}; leftover28 {left28:,.0f})")
# probability table, 13 Oct
T = (J27 - date(2026,10,13)).days / 365.25
print(f"horizon {T:.3f}y ({(J27-date(2026,10,13)).days} days)")
for be_lab, be, room in (("buyable/unchanged", 16.3, 4710), ("buyable/forward", 19.6, 5664), ("nov15/forward", 23.9, 6945)):
    row = []
    for vol in (70, 80, 100, 120):
        s = vol * math.sqrt(T); p = norm.cdf(-be / s)
        # expected top-up and 95th pct top-up in $ (dv01 ~287/bp)
        sd = s * 287; mu = -room
        e = sd * norm.pdf(mu / sd * -1) + mu * norm.cdf(mu / sd) if False else (mu * norm.cdf(mu/sd) + sd * norm.pdf(mu/sd))
        q95 = max(0.0, mu + 1.645 * sd)
        row.append(f"{vol}bp/yr: sigma {s:.0f}bp P={p*100:.0f}% E[top-up]=${e:,.0f} 95th=${q95:,.0f}")
    print(be_lab, "|", " ; ".join(row))
