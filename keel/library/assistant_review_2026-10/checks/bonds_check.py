from datetime import date
import indep_pricer as ip
d0 = date(2026, 9, 28)
c = ip.Curve(ip.load_curve('par2026.csv', '09/28/2026'))
# WInS clean prices seen 29 Sep (28 Sep closes) from archive/rab/data/sheet Book L tab + tickets alternates
bonds = [("T 4.750% 15-Feb-2037", 4.75, date(2037,2,15), 97.152),
         ("T 4.500% 15-May-2038", 4.50, date(2038,5,15), 94.281),
         ("T 4.375% 15-Nov-2039", 4.375, date(2039,11,15), 91.363),
         ("T 4.250% 15-Nov-2040", 4.25, date(2040,11,15), 89.186),
         ("T 3.125% 15-Nov-2041", 3.125, date(2041,11,15), 76.367),
         ("T 4.375% 15-Feb-2038 (stale?)", 4.375, date(2038,2,15), 99.980),
         ("T 4.500% 15-Feb-2036 (stale?)", 4.50, date(2036,2,15), 102.950)]
print(f"{'bond':32s} {'accr':>6s} {'WInS clean':>10s} {'curve clean':>11s} {'WInS ytm':>9s} {'curve ytm':>9s} {'gap bp':>7s}")
for name, cpn, mat, clean in bonds:
    a = ip.accrued(cpn, mat, d0)
    dirty_c = ip.dirty_from_curve(c, cpn, mat, d0)
    y_w = ip.ytm_from_dirty(clean + a, cpn, mat, d0)
    y_c = ip.ytm_from_dirty(dirty_c, cpn, mat, d0)
    print(f"{name:32s} {a:6.3f} {clean:10.3f} {dirty_c - a:11.3f} {y_w*100:8.3f}% {y_c*100:8.3f}% {(y_w-y_c)*1e4:7.1f}")
