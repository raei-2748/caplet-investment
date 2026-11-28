"""Part 2: the facility money, the 2031 range, Table 3, what Laura keeps, the 0.25-point payout sensitivity.
MODEL. Written for the audit; uses audit_core only. Run: python3 part2_facility.py

House model (the draft states only "Monte Carlo ... 7.5% world equity return"; the rest is this file's choice and is
varied in the robustness block):
  * world shares: lognormal, median growth 7.5% a year (J.P. Morgan 2027 LTCMA, global equities, USD, compound),
    17.88% a year volatility (same edition's AC World row), VT fee 0.06%;
  * Treasury yields: parallel moves, 0.9 points a year standard deviation, independent of shares, in three steps
    (6 Nov 2026 to 1 Jan 2027, 2027, 2028-2030), rates floored at zero;
  * 200,000 paths.
History: Shiller's monthly S&P Composite with dividends, Jan 1871 to Jun 2023, every five-year window
(three years 2028-2031 for the shares bought in 2028, two more to 2033 for the half kept), rates at today's forwards.
"""
import csv
import json
import math
from datetime import date

import numpy as np
from scipy.optimize import linprog

from audit_core import *

cv = bootstrap_pchip()
END32 = date(2032, 12, 15)
G = 7.5 / 100; VOL = 0.1788; N = 200_000; YVOL = 0.009
out = {}


def P_s(d1, d2, s):
    """Forward discount factor on the curve moved by s, the average forward floored at zero."""
    tau = yf(d1, d2)
    if tau <= 0:
        return 1.0
    f = -math.log(cv.P(d1, d2)) / tau
    return math.exp(-max(f + s, 0.0) * tau)


# ---------------------------------------------------------------- per-unit flows (curve-free) and prices (curve-dependent)
def unit_flows(year, buy, world="zero", cut=0.0):
    fl = instrument_flows(year, cv, buy, world, cut)
    if year in BONDS:
        px = BONDS[year].dirty(cv, buy)
        return [(d, a * px) for d, a in fl], px
    f = Fund(FUND_FOR[year], year)
    nav = f.nav_gross(cv, buy) / 1e6
    return [(d, a * nav) for d, a in fl], nav


def unit_price(year, buy, s):
    if year in BONDS:
        return sum(a * P_s(buy, d, s) for d, a in BONDS[year].flows(buy))
    f = Fund(FUND_FOR[year], year)
    v = 0.0
    for p, b in f.notes:
        if b.mat > buy:
            v += p * sum(a * P_s(buy, d, s) for d, a in b.flows(buy))
    v += f.cash0 + sum(p for p, b in f.notes if b.mat <= buy)
    return v / 1e6


# IBTM bought on 1 Jan 2028 and on 1 Jan 2031: what $1 pays by 15 Dec 2032
def ibtm_per_dollar(buy, s, world):
    fl, _ = unit_flows(2033, buy, "zero" if world == "zero" else "fwd")
    px = unit_price(2033, buy, s)
    if world == "zero":
        # distributions wait in a T-bill ETF at zero interest, less 0.15% a year, to 15 Dec 2032 (the rule)
        return sum(a * (1 - WAIT_FEE) ** yf(d, END32) for d, a in fl) / px
    # forward world on the moved curve: distributions reinvested at the moved forwards to 15 Dec 2032.
    # (The fund's own cash earned base forwards inside unit_flows; the difference is second order.)
    return sum(a / P_s(d, END32, s) for d, a in fl) / px


SH = np.round(np.arange(-0.05, 0.0501, 0.0025), 4)
Z28 = np.array([ibtm_per_dollar(J28, s, "zero") for s in SH])
F28 = np.array([ibtm_per_dollar(J28, s, "fwd") for s in SH])
Z31 = np.array([ibtm_per_dollar(J31, s, "zero") for s in SH])
F31 = np.array([ibtm_per_dollar(J31, s, "fwd") for s in SH])
interp = lambda tab, s: np.interp(s, SH, tab)

# ---------------------------------------------------------------- the operating side as a function of yield moves
pay_dates = [date(y, 1, 1) for y in YEARS]
uf27f = {y: unit_flows(y, J27, "fwd") for y in YEARS}
uf27z = {y: unit_flows(y, J27, "zero", CUT if y in FUND_FOR else 0.0) for y in YEARS}
uf28z = {y: unit_flows(y, J28, "zero", CUT if y in FUND_FOR else 0.0) for y in YEARS}


def win(d):
    for k, pd in enumerate(pay_dates):
        if (pay_dates[k - 1] if k else date(1900, 1, 1)) < d <= pd:
            return k
    return None


A28 = np.zeros((10, 10))
for j, y in enumerate(YEARS):
    for d, a in uf28z[y][0]:
        k = win(d)
        if k is not None:
            A28[k, j] += a * (1 - WAIT_FEE) ** yf(d, pay_dates[k])


def operating(s0, s1, pooled=False):
    """s0: yield move before 1 Jan 2027; s1: during 2027. Returns (ladder cost J27, top-up J28, extra J28)."""
    units = {}
    cost = 0.0
    for y in YEARS:
        fl, _ = uf27f[y]
        fv = sum(a / P_s(d, date(y, 1, 1), s0) for d, a in fl if d <= date(y, 1, 1))
        u = PAY / fv
        units[y] = u
        cost += u * unit_price(y, J27, s0)
    # a ladder cheaper than $300,000 leaves the rest of the first deposit to carry into 2028 (negative top-up)
    top_up = (cost - 300000) / P_s(J27, J28, s0 + s1)
    own = np.zeros(10)
    for y in YEARS:
        for d, a in uf27z[y][0]:
            k = win(d) if pooled else (YEARS.index(y) if d <= date(y, 1, 1) else None)
            if k is not None:
                own[k] += units[y] * a * (1 - WAIT_FEE) ** yf(d, pay_dates[k])
    price28 = np.array([unit_price(y, J28, s0 + s1) for y in YEARS])
    # surplus from the top-up's own bonds is ignored (cautious): the top-up completes the ten
    n = 10
    c = np.r_[price28, np.zeros(n)]
    Aeq = np.zeros((n, 2 * n)); b = np.zeros(n)
    for k in range(n):
        Aeq[k, :n] = A28[k]; Aeq[k, n + k] = -1
        if k:
            Aeq[k, n + k - 1] = 1 - WAIT_FEE
        b[k] = PAY - own[k]
    r = linprog(c, A_eq=Aeq, b_eq=b, bounds=[(0, None)] * (2 * n), method="highs")
    return cost, top_up, float(r.fun)


G0 = np.round(np.arange(-0.04, 0.0401, 0.005), 4)
G1 = np.round(np.arange(-0.04, 0.0401, 0.005), 4)
OP = {pool: np.zeros((len(G0), len(G1), 3)) for pool in (False, True)}
for pool in (False, True):
    for i, s0 in enumerate(G0):
        for j, s1 in enumerate(G1):
            OP[pool][i, j] = operating(s0, s1, pool)


def op_interp(s0, s1, pool=False):
    s0 = np.clip(s0, G0[0], G0[-1]); s1 = np.clip(s1, G1[0], G1[-1])
    i = np.clip(np.searchsorted(G0, s0) - 1, 0, len(G0) - 2); j = np.clip(np.searchsorted(G1, s1) - 1, 0, len(G1) - 2)
    t = (s0 - G0[i]) / (G0[i + 1] - G0[i]); u = (s1 - G1[j]) / (G1[j + 1] - G1[j])
    T = OP[pool]
    v = (T[i, j] * ((1 - t) * (1 - u))[..., None] + T[i + 1, j] * (t * (1 - u))[..., None]
         + T[i, j + 1] * ((1 - t) * u)[..., None] + T[i + 1, j + 1] * (t * u)[..., None])
    return v


# ---------------------------------------------------------------- the plan, path by path
def plan(s0, s1, s2, g3, g2, pool=False, cut_real=CUT, most=True, deposit=150000.0):
    s0, s1, s2, g3, g2 = map(np.asarray, (s0, s1, s2, g3, g2))
    op = op_interp(s0, s1, pool)
    topup, extra = op[..., 1], op[..., 2]
    R = np.maximum(deposit - topup - extra, 0.0)
    floor_m = 0.733 * R
    if most:
        floor_m = np.minimum(np.maximum(floor_m, 75001.0), R)
    vt = R - floor_m
    vt31 = vt * g3 * (1 - VT_FEE) ** 3
    moved, kept = vt31 / 2, vt31 / 2 * g2 * (1 - VT_FEE) ** 2
    z28, f28 = interp(Z28, s0 + s1), interp(F28, s0 + s1)
    z31, f31 = interp(Z31, s0 + s1 + s2), interp(F31, s0 + s1 + s2)
    bot_u = floor_m * z28 * (1 - CUT)
    top_u = bot_u + moved * z31 * (1 - CUT)
    bottom = np.floor(bot_u / 5000) * 5000
    top = np.floor(top_u / 5000) * 5000
    pays_fwd = floor_m * f28 + moved * f31          # what the facility Treasuries pay by Dec 2032 at forwards
    pays_zero_real = (floor_m * z28 + moved * z31) * (1 - cut_real)
    bot_zero_real = floor_m * z28 * (1 - cut_real)
    contrib = np.minimum(top, pays_fwd)
    excess = np.maximum(pays_fwd - top, 0.0)
    rival = R * g3 * (1 - VT_FEE) ** 3 * (1 - np.where(R > 0, vt / 2 / np.where(R > 0, R, 1), 0)) * f31
    return dict(R=R, floor=floor_m, vt=vt, vt31=vt31, moved=moved, kept=kept, bot_u=bot_u, top_u=top_u, bottom=bottom,
                top=top, pays_fwd=pays_fwd, contrib=contrib, excess=excess, keep_total=kept + excess, rival=rival,
                pays_zero_real=pays_zero_real, bot_zero_real=bot_zero_real, topup=topup, extra=extra)


def pct(x, q=(5, 50, 95)):
    return [round(float(np.percentile(x, k))) for k in q]


# central case
c = plan(0.0, 0.0, 0.0, (1 + G) ** 3, (1 + G) ** 2)
c = {k: float(v) for k, v in c.items()}
out["central"] = {k: round(c[k]) for k in ("topup", "extra", "R", "floor", "vt", "vt31", "moved", "bot_u", "top_u",
                                           "bottom", "top", "pays_fwd", "excess", "kept", "keep_total")}
out["ibtm_per_dollar"] = {"zero_from_jan2028": round(float(interp(Z28, 0)), 6), "fwd_from_jan2028": round(float(interp(F28, 0)), 6),
                          "zero_from_jan2031": round(float(interp(Z31, 0)), 6), "fwd_from_jan2031": round(float(interp(F31, 0)), 6)}
# the draft's own figures plugged into this file's per-dollar payouts (isolates the fund model from the sizing)
d_floor, d_vt = 81244.0, 29594.0
d_vt31 = d_vt * (1 + G) ** 3 * (1 - VT_FEE) ** 3
d_bot = d_floor * float(interp(Z28, 0)) * (1 - CUT)
d_top = d_bot + d_vt31 / 2 * float(interp(Z31, 0)) * (1 - CUT)
d_pays = d_floor * float(interp(F28, 0)) + d_vt31 / 2 * float(interp(F31, 0))
d_kept = d_vt31 / 2 * (1 + G) ** 2 * (1 - VT_FEE) ** 2
out["central_on_drafts_sizes"] = {"bottom_unrounded": round(d_bot), "top_unrounded": round(d_top),
                                  "facility_pays_fwd": round(d_pays), "vt_jan2031": round(d_vt31),
                                  "kept_half_2033": round(d_kept), "keep_total_at_115k": round(d_kept + d_pays - 115000)}

# house model
rng = np.random.default_rng(20261128)
s0 = rng.normal(0, YVOL * math.sqrt(yf(VAL, J27)), N)
s1 = rng.normal(0, YVOL, N)
s2 = rng.normal(0, YVOL * math.sqrt(3), N)
g3 = np.exp(rng.normal(3 * math.log(1 + G), VOL * math.sqrt(3), N))
g2 = np.exp(rng.normal(2 * math.log(1 + G), VOL * math.sqrt(2), N))
h = plan(s0, s1, s2, g3, g2)
cut75 = plan(s0, s1, s2, g3, g2, cut_real=0.0075)
fail_b = cut75["bot_zero_real"] < h["bottom"] - 1e-6
fail_t = cut75["pays_zero_real"] < h["top"] - 1e-6
out["house"] = {
    "paths": N,
    "top_at_least_115k": round(float((h["top"] >= 115000).mean()), 4),
    "top_at_least_100k": round(float((h["top"] >= 100000).mean()), 4),
    "bottom_stated_p5_p50_p95": [float(np.percentile(h["bottom"], q, method="lower")) for q in (5, 50, 95)],
    "top_stated_p5_p50_p95": [float(np.percentile(h["top"], q, method="lower")) for q in (5, 50, 95)],
    "table3_plan_p5_p50_p95": pct(h["pays_fwd"]), "table3_rival_p5_p50_p95": pct(h["rival"]),
    "plan_below_95k": round(float((h["pays_fwd"] < 95000).mean()), 4),
    "rival_below_95k": round(float((h["rival"] < 95000).mean()), 4),
    "median_gap_rival_minus_plan": round(float(np.percentile(h["rival"], 50) - np.percentile(h["pays_fwd"], 50))),
    "p5_gap_plan_minus_rival": round(float(np.percentile(h["pays_fwd"], 5) - np.percentile(h["rival"], 5))),
    "plan_behind_rival_share": round(float((h["pays_fwd"] < h["rival"]).mean()), 4),
    "keep_total_p5_p50_p95": pct(h["keep_total"]),
    "stated_ends_fail_at_zero_interest_with_0.5pct": int(((h["bot_zero_real"] * 0 + h["bot_u"]) < h["bottom"]).sum()),
    "with_0.75pct_cut_bottom_short": round(float(fail_b.mean()), 4),
    "with_0.75pct_cut_top_short": round(float(fail_t.mean()), 4),
    "with_0.75pct_cut_either_short": round(float((fail_b | fail_t).mean()), 4),
    "with_0.75pct_cut_largest_short": round(float(np.max(np.r_[h["bottom"] - cut75["bot_zero_real"], h["top"] - cut75["pays_zero_real"]]))),
    "with_0.75pct_cut_short_at_forward_rates": int(((cut75["pays_fwd"] * (1 - 0.0025) < h["top"])).sum()),
    "most_rule_binds_share": round(float((0.733 * h["R"] < 75001).mean()), 4),
}
# 1-point cut sensitivities for the either-short rate
for cr in (0.006, 0.0065, 0.007, 0.0075, 0.01):
    x = plan(s0, s1, s2, g3, g2, cut_real=cr)
    out["house"][f"either_short_cut_{cr*100:.2f}pct"] = round(float(((x["bot_zero_real"] < h["bottom"] - 1e-6) | (x["pays_zero_real"] < h["top"] - 1e-6)).mean()), 4)

# ---------------------------------------------------------------- history: Shiller total return, five-year windows
rows = [r for r in csv.DictReader(open(HERE.parents[1] / "models/data/shiller_monthly.csv"))]
rows = [r for r in rows if r["Date"] <= "2023-06-01"]
P = np.array([float(r["SP500"]) for r in rows]); D = np.array([float(r["Dividend"]) for r in rows])
tr = np.ones(len(P))
for i in range(1, len(P)):
    tr[i] = tr[i - 1] * (P[i] + D[i - 1] / 12) / P[i - 1]
starts = np.arange(0, len(P) - 60)
hg3 = tr[starts + 36] / tr[starts]; hg2 = tr[starts + 60] / tr[starts + 36]
z = np.zeros(len(starts))
hh = plan(z, z, z, hg3, hg2)
lo = int(np.argmin(hh["pays_fwd"])); lor = int(np.argmin(hh["rival"])); lok = int(np.argmin(hh["keep_total"]))
out["history"] = {"windows": int(len(starts)), "first": rows[0]["Date"], "last_start": rows[int(starts[-1])]["Date"],
                  "plan_p5_p50_p95": pct(hh["pays_fwd"]), "rival_p5_p50_p95": pct(hh["rival"]),
                  "plan_lowest": [round(float(hh["pays_fwd"][lo])), rows[lo]["Date"]],
                  "rival_lowest": [round(float(hh["rival"][lor])), rows[lor]["Date"]],
                  "rival_below_95k": round(float((hh["rival"] < 95000).mean()), 4),
                  "plan_below_95k": round(float((hh["pays_fwd"] < 95000).mean()), 4),
                  "keep_lowest": [round(float(hh["keep_total"][lok])), rows[lok]["Date"]],
                  "top_stated_lowest": float(hh["top"].min())}

# ---------------------------------------------------------------- named cases
f40 = plan(0.0, 0.0, 0.0, (1 + G) ** 3 * 0.6, (1 + G) ** 2)
out["fall40_before_move"] = {"bottom": float(f40["bottom"]), "top": float(f40["top"]), "top_unrounded": round(float(f40["top_u"]))}
# what certainty costs: no extra Treasuries (only the top-up), the range still read by the same zero-interest rule
R_alt = 150000 - c["topup"]
fl_alt, vt_alt = 0.733 * R_alt, R_alt - 0.733 * R_alt
mv_alt = vt_alt * (1 + G) ** 3 * (1 - VT_FEE) ** 3 / 2
bot_alt = fl_alt * float(interp(Z28, 0)) * (1 - CUT); top_alt = bot_alt + mv_alt * float(interp(Z31, 0)) * (1 - CUT)
out["without_extra_treasuries_same_range_rule"] = {"bottom_unrounded": round(bot_alt), "top_unrounded": round(top_alt),
                                                    "bottom": math.floor(bot_alt / 5000) * 5000, "top": math.floor(top_alt / 5000) * 5000}
# a 40% fall, two readings: 40% below the expected 2031 value, and 40% below the January 2028 purchase price
f40b = plan(0.0, 0.0, 0.0, 0.6, (1 + G) ** 2)
out["fall40_before_move"]["below_purchase_price"] = {"bottom": float(f40b["bottom"]), "top": float(f40b["top"]), "top_unrounded": round(float(f40b["top_u"]))}
d40a = d_bot + d_vt31 * 0.6 / 2 * float(interp(Z31, 0)) * (1 - CUT)
d40b = d_bot + d_vt * 0.6 * (1 - VT_FEE) ** 3 / 2 * float(interp(Z31, 0)) * (1 - CUT)
out["fall40_before_move"]["on_drafts_sizes_top_unrounded"] = {"below_expected_2031": round(d40a), "below_purchase_price": round(d40b)}
# July 1929 start, kept money
i29 = [i for i, r in enumerate(rows) if r["Date"] == "1929-07-01"][0]
out["history"]["keep_total_start_jul1929"] = round(float(hh["keep_total"][i29]))
out["history"]["keep_total_p5"] = round(float(np.percentile(hh["keep_total"], 5)))
# smaller deposit
for dep in (112500.0, 75000.0):
    x = plan(0.0, 0.0, 0.0, (1 + G) ** 3, (1 + G) ** 2, deposit=dep)
    out[f"deposit_{int(dep)}"] = {"left": round(float(x["R"])), "bottom": float(x["bottom"]), "top": float(x["top"])}
# pooled rule for the extra Treasuries: what it does to the central range
cp = plan(0.0, 0.0, 0.0, (1 + G) ** 3, (1 + G) ** 2, pool=True)
out["central_if_extra_pooled"] = {"extra": round(float(cp["extra"])), "bottom_unrounded": round(float(cp["bot_u"])),
                                  "top_unrounded": round(float(cp["top_u"])), "bottom": float(cp["bottom"]), "top": float(cp["top"])}
# robustness of the 57%: yield volatility and treating 7.5% as an arithmetic mean
rob = {}
for yv in (0.006, 0.012):
    r2 = np.random.default_rng(7)
    a0 = r2.normal(0, yv * math.sqrt(yf(VAL, J27)), N); a1 = r2.normal(0, yv, N); a2 = r2.normal(0, yv * math.sqrt(3), N)
    x = plan(a0, a1, a2, g3, g2)
    rob[f"yield_vol_{yv*100:.1f}pt"] = round(float((x["top"] >= 115000).mean()), 4)
mu_ar = math.log(1 + G) - VOL ** 2 / 2
x = plan(s0, s1, s2, np.exp(rng.normal(3 * mu_ar, VOL * math.sqrt(3), N)), g2)
rob["7.5pct_as_arithmetic_mean"] = round(float((x["top"] >= 115000).mean()), 4)
out["robustness_top_at_least_115k"] = rob
out["inflation_2.5pct_7yrs"] = round(115000 / 1.025 ** 7)
out["inflation_2.4pct_7yrs"] = round(115000 / 1.024 ** 7)
print(json.dumps(out, indent=1))
json.dump(out, open(HERE / "results_part2.json", "w"), indent=1)
