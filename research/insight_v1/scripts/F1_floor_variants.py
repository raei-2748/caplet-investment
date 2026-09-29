"""F1 - smaller-floor variants of the recommended design (REC), requested 2026-09-29 to test the "reads as timid" critique.

How to run (repo root, no network):  .venv/bin/python research/insight_v1/scripts/F1_floor_variants.py

Same engine, seed, paths and inputs as E4/E6 (E4.rival_design). The only change is the size of the floor bought on
1 Jan 2028: it repays F dollars just before 2033, F in {150k (REC default), 125k, 100k, 75k, 50k, 0}; the rest of the
growth money goes into the world stock fund. s = 1/2 and the cap rule are unchanged. The ten payments are bought in
2027 in every variant, so no variant changes whether the payments are funded. Controls: all-Treasury (floor = all
growth money). Every number is a MODEL PROPERTY under E4's stated assumptions, never a forecast.
"""
import importlib.util, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("E4", os.path.join(HERE, "E4_rival_numbers.py"))
E4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(E4)
D6, k = E4.D6, E4.k
G = E4.LEFT * (1 + E4.Y1) + D6.DEP
IN = E4.LEFT + D6.DEP
FLOORS = [None, 125_000, 100_000, 75_000, 50_000, 0]
def a_for(F):
    return None if F is None else F / (1 + E4.Y5) ** 5 / G

def name(F):
    return "150k REC" if F is None else f"{F // 1000}k"

def table(label, req):
    print(f"\n== {label}")
    print(f"{'floor':9s}| {'total p5 / p50 / p95':24s}| {'gift p5 / p50':15s}| top med | P(top) | floor/med gift | stock % avg | total<in | lift vs REC p50 / p5")
    base = E4.rival_design(req)
    ctl = E4.rival_design(req, a=1.0)
    for F in FLOORS:
        d = E4.rival_design(req, a=a_for(F))
        t, g = d["total"], d["gift"]
        print(f"{name(F):9s}| {k(np.percentile(t,5))} / {k(np.median(t))} / {k(np.percentile(t,95))}  "
              f"| {k(np.percentile(g,5))} / {k(np.median(g))} | {k(np.median(d['top']))}  | {d['reached_top']*100:4.0f}%  "
              f"| {d['bottom'][0]/np.median(g)*100:5.0f}%         | {np.median(d['pctyrs'])/5*100:5.1f}%     "
              f"| {np.mean(t<IN)*100:5.1f}%  | {k(np.median(t)-np.median(base['total']))} / {k(np.percentile(t,5)-np.percentile(base['total'],5))}")
    t = ctl["total"]
    print(f"{'all-Tsy':9s}| {k(np.percentile(t,5))} / {k(np.median(t))} / {k(np.percentile(t,95))}  (control: every growth dollar in Treasuries)")
    for F in FLOORS[1:]:
        d = E4.rival_design(req, a=a_for(F))
        print(f"   {name(F):6s} ends below all-Treasury control in {np.mean(d['total'] < ctl['total'])*100:.0f}% of paths;"
              f" below REC in {np.mean(d['total'] < base['total'])*100:.0f}%")

req, rbd = D6.draws(E4.JPM_ACWI, bd=D6.BD_CONSISTENT)
table("JPM 2026 LTCMA (ACWI 7.00%, bonds 5.00%), 200,000 paths", req)
vg = D6.lp(0.0508, 0.0508 + (0.0828 - 0.0700))
table("Vanguard-like house (5.08% compound, JPM vol; ASSUMPTION hybrid)", D6.draws(vg, bd=D6.BD_CONSISTENT)[0])

yrs, heq, hbd = E4.load_hist()
for lab, eq in (("raw S&P 500 TR", heq), ("rescaled to 7.00%", E4.rescale(heq, 0.07))):
    R = np.array([eq[i:i + 6] for i in range(len(eq) - 5)])
    print(f"\n== History, every 6-year window 1928-2025 ({lab}, {len(R)} windows)")
    for F in FLOORS:
        d = E4.rival_design(R, a=a_for(F)); t = d["total"]; w = int(t.argmin())
        print(f"{name(F):9s}| total worst {k(t.min())} (start {yrs[w]}), p10 {k(np.percentile(t,10))}, median {k(np.median(t))}"
              f" | gift worst {k(d['gift'].min())} | 2007 window total {k(t[int(np.where(yrs==2007)[0][0])])}")
