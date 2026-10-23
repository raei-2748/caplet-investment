import sys
from datetime import date
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import indep_pricer as P
path = sys.argv[1]
for day, d0 in (("10/06/2026", date(2026,10,7)), ("10/07/2026", date(2026,10,8))):
    c = P.Curve(P.load_curve(path, day))
    for cp, mat, fill in ((4.75, date(2037,2,15), 96.019), (5.0, date(2037,2,15), 96.019), (4.5, date(2038,5,15), 93.076),
                          (4.375, date(2039,11,15), 90.005), (4.25, date(2040,11,15), 87.724), (3.125, date(2041,11,15), 74.955)):
        dirty = P.dirty_from_curve(c, cp, mat, d0) / c.df(0)  # settle ~ d0
        clean = dirty - P.accrued(cp, mat, d0)
        y = P.ytm_from_dirty(fill + P.accrued(cp, mat, d0), cp, mat, d0)
        print(f"curve {day} settle {d0}: {cp:.3f}% {mat}: model clean {clean:.3f} vs fill {fill} (diff {fill-clean:+.3f}); fill ytm {y*100:.3f}%")
