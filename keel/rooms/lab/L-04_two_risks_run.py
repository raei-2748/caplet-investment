"""L-04: do the two claims on the half Laura keeps arrive together?

Claim 1 (payment shortfall): yields fall and stay down while coupons are reinvested.
Claim 2 (cost overrun): building costs rise fast between the 2031 quote and the 2033 gift (and while it is built).
US proxy only: Shiller monthly GS10 and CPI (archive/rab/data/history/shiller_monthly.csv). Taiwan costs are not in
the data, so this is a test of the US yield-inflation link, not of Taiwan building costs. MODEL/HISTORY.
Plan clock: start year Y = 2027. Reinvestment years Y+1..Y+14; quote-to-gift Y+4..Y+6; build Y+6..Y+9.
"""
import csv, json, statistics as st, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
rows = list(csv.DictReader(open(ROOT / "archive/rab/data/history/shiller_monthly.csv")))
jan = {int(r["year"]): r for r in rows if r["month"] == "1"}
gs = {y: float(r["GS10"]) for y, r in jan.items() if r["GS10"]}
cpi = {y: float(r["CPI"]) for y, r in jan.items() if r["CPI"]}
def infl(a, b):  # annualised CPI change from Jan a to Jan b
    return (cpi[b] / cpi[a]) ** (1 / (b - a)) - 1
out = {}
for label, y0 in (("1871-2011", 1871), ("1954-2011", 1954)):
    S, C, B, dy, ic = [], [], [], [], []
    for y in range(y0, 2012):
        need = [y + k for k in range(0, 15)]
        if not all(k in gs for k in need) or not all(k in cpi for k in (y + 4, y + 6, y + 9)):
            continue
        d = st.mean(gs[y + k] for k in range(1, 15)) - gs[y]
        i46 = infl(y + 4, y + 6)
        i69 = infl(y + 6, y + 9)
        s = d <= -1.0
        c = i46 > 0.035
        b = i69 > 0.035
        S.append(s); C.append(c); B.append(b); dy.append(d); ic.append(i46)
    n = len(S)
    pS, pC = sum(S) / n, sum(C) / n
    both = sum(1 for s, c in zip(S, C) if s and c) / n
    both_build = sum(1 for s, b in zip(S, B) if s and b) / n
    # inflation in the worst fifth of yield paths vs the rest
    order = sorted(range(n), key=lambda k: dy[k])
    q = order[: n // 5]
    out[label] = {
        "start_years": n,
        "P_shortfall_yields_fall_1pt_for_good": round(pS, 3),
        "P_costs_rise_over_3.5pct_quote_to_gift": round(pC, 3),
        "P_both": round(both, 3),
        "P_both_if_independent": round(pS * pC, 3),
        "P_shortfall_and_build_years_over_3.5pct": round(both_build, 3),
        "P_costs_rise_given_shortfall": round(both / pS, 3) if pS else None,
        "P_costs_rise_given_no_shortfall": round((pC * n - both * n) / (n - sum(S)), 3),
        "corr_yield_change_vs_quote_to_gift_inflation": round(st.correlation(dy, ic), 3),
        "mean_quote_to_gift_inflation_worst_fifth_yield_paths": round(st.mean(ic[k] for k in q), 4),
        "mean_quote_to_gift_inflation_other_paths": round(st.mean(ic[k] for k in order[n // 5:]), 4),
    }
json.dump(out, sys.stdout, indent=1)
