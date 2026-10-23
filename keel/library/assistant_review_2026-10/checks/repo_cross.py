import importlib.util, sys
from datetime import date
spec = importlib.util.spec_from_file_location("m1", "../../../../archive/rab/models/m1_ladder.py")
m1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m1)
rows = m1.load_rows([sys.argv[1]])
BUY = [date(2032,12,15), date(2033,12,15), date(2034,12,15), date(2035,12,15), date(2036,12,15),
       date(2037,2,15), date(2038,5,15), date(2039,11,15), date(2040,11,15), date(2041,11,15)]
from scipy.optimize import brentq
for r in rows:
    if r["_date"] in (date(2026,9,28), date(2026,10,6), date(2026,10,13)):
        cv = m1.Curve(r)
        nov = m1.liability(cv, "nov15")["fwd_2027"]; be_nov = m1.breakeven_bp(r, "nov15")
        buy = sum(50000*cv.df(d) for d in BUY)/cv.df(m1.A27)
        be_buy = -brentq(lambda bp: sum(50000*m1.Curve(r,bp).df(d) for d in BUY)/m1.Curve(r,bp).df(m1.A27)-300000, -600, 200, xtol=1e-4)
        print(f"{r['_date']}: repo m1 nov15 fwd {nov:,.0f} BE {be_nov:.1f}bp | buyable fwd {buy:,.0f} BE {be_buy:.1f}bp")
