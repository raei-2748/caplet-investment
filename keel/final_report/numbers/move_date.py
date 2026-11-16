"""The move date inside 2031: 1 January, 1 April or 1 July (numbers owner, Mon 16 Nov 2026, Sydney). MODEL, not a forecast
or a promise. NUMBERS 8r.

Run from the repo root:  python3 -I keel/final_report/numbers/move_date.py
   or from this folder:  python3 -I move_date.py
Writes keel/final_report/numbers/results_move_date_2026-11-16.json and prints the figures (about 15 seconds, numpy only).
Imports engine.py, plan.py and completion.py and changes none of them; reads no results file.

The question. IPS l.15: "Before you meet co-sponsors in 2031, the other half will move into Treasuries." The register
models the move on 1 Jan 2031 (NUMBERS 4: the trade on Thu 2 Jan 2031, the first trading day). This runs the same plan
with the move on 1 Jan, 1 Apr and 1 Jul 2031 and compares, path by path: the stated bottom and top, how often each
$5,000 step of the top is stated, her flexibility (the half kept, and the half kept plus the excess, on 1 Jan 2033) and
how often a market fall between the earlier and the later date changes the stated top. 1 January is the base.

What changes with the move date, and nothing else (every other input is the register's):
  * VT grows to the move day and the moved half is VT's half on that day (3, 3.25 or 3.5 years after January 2028);
  * the moved half buys the late-2032 fund at that day's yield: the forward rate from the move day to 15 Dec 2032 on
    the 6 Nov curve, plus the path's yield move; its modelled payout earns that yield to 15 Dec 2032, after the fund's
    0.07% fee, as plan.run does for 1 Jan;
  * the top is the range rule on that day (completion.zero_per_dollar on the move day: what $1 of the fund's holdings
    pays if nothing earns interest from then, after the fee from that day and the waiting ETF's fee), less 0.5%,
    rounded down once to $5,000 (completion.rule's arithmetic, with the move day in place of 1 Jan 2031);
  * the half kept is half of VT, valued on 1 Jan 2033 on the same market path; the move date does not change it.
Paths (the same paths for all three dates, so the comparison is path by path):
  house    plan.draws (200,000 paths, seed 2033) exactly as the register; VT's path inside 2031 is filled in by a
           Brownian bridge on each path's own two-year draw (Jan 2031 to Jan 2033), so VT on 1 Jan 2033 is unchanged;
           the yield moves on by independent steps of 0.9 points a year (0.45 points a quarter). Extra draws: seed 2031.
  history  US stocks with dividends (Shiller monthly, plan.shiller_windows' index), every window since 1871 (1,770);
           the move 36, 39 or 42 months after VT is bought; rates at today's forwards.
  joint    rates (FRED DGS1, in proportion to today's forwards) and US stocks from the same months, 585 windows
           (range_rule.py section 5's method); the move at window month 48, 51 or 54, at that month's rate ratio.
Check: with the move on 1 January every array reproduces plan.run and completion.rule exactly (asserted), and so the
register's figures (NUMBERS 4).
"""
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

RUN = "Mon 16 Nov 2026 (Sydney)"
OUTFILE = HERE / "results_move_date_2026-11-16.json"
NAME = C.design_arg()
DSG = C.design(NAME)
MARGIN = DSG["margin"]
MF = C.margin_fn(NAME)
c = E.Curve(E.load_par())
END = date(2032, 12, 15)
FEE, VFEE = E.ASSUMPTIONS["fund_fee"], E.ASSUMPTIONS["vt_fee"]
MU, SD, YV = math.log(1 + E.ASSUMPTIONS["eq_growth"]), E.ASSUMPTIONS["eq_vol"], E.ASSUMPTIONS["yield_vol"]
MOVES = {"jan": (date(2031, 1, 1), 0), "apr": (date(2031, 4, 1), 3), "jul": (date(2031, 7, 1), 6)}
TOPS = (90_000, 95_000, 100_000, 105_000, 110_000, 115_000, 120_000, 125_000, 130_000, 140_000, 150_000)
SEED_EXTRA = 2031


def moved_and_rule(base, move, k, g_to, g_after, s_move, m_move, sF, mF):
    """The moved half, the half kept and the range rule for a move on `move` (k months after 1 Jan 2031).
    base: plan.run output (everything up to January 2028 and the floor; the move date does not touch it).
    g_to, g_after: VT growth (before its fee) from Jan 2028 to the move and from the move to Jan 2033.
    s_move, m_move: the yield on the move day = forward(move, 15 Dec 2032) x m_move + s_move (floored as plan.run).
    sF, mF: the floor's yield move at January 2028 (as completion.rule)."""
    t3, t2 = 3 + k / 12, 2 - k / 12
    fM, tauM = c.fwd(move, END), E.yf(END, move)
    vt_m = np.asarray(base["vt28"], float) * g_to * (1 - VFEE) ** t3
    yM = np.maximum(fM * np.asarray(m_move, float) + s_move, 0.001)
    moved = vt_m / 2 * np.exp(yM * tauM) * (1 - FEE) ** tauM
    kept33 = vt_m / 2 * g_after * (1 - VFEE) ** t2
    Fm, F = np.asarray(base["floor_money"], float), np.asarray(base["floor"], float)
    zf = C.zero_per_dollar(E.J28, sF, mF)
    zm = C.zero_per_dollar(move, s_move, m_move)
    Fz, Mz = Fm * zf, vt_m / 2 * zm
    b_raw, t_raw = Fz * (1 - C.HAIRCUT), (Fz + Mz) * (1 - C.HAIRCUT)
    bottom, top = C.down(b_raw), C.down(t_raw)
    pay = F + moved
    gift = np.minimum(pay, top)
    return dict(vt_move=vt_m, moved_money=vt_m / 2, moved=moved, kept33=kept33, zM=zm, bottom_raw=b_raw, top_raw=t_raw,
                bottom=bottom, top=top, pay=pay, gift=gift, excess=pay - gift, flex=kept33 + pay - gift)


def check_jan(base, r, sF, sM, mF=1.0, mM=1.0):
    """With the move on 1 January the arrays must be plan.run's and completion.rule's, exactly."""
    rr = C.rule(base, sF, sM, mF, mM)
    for a, b in ((r["moved"], base["moved"]), (r["kept33"], base["kept33"]), (r["top"], rr["top"]),
                 (r["bottom"], rr["bottom"]), (r["top_raw"], rr["top_raw"]), (r["excess"], rr["excess"])):
        assert np.allclose(a, b, rtol=0, atol=1e-6), float(np.max(np.abs(np.asarray(a) - np.asarray(b))))


def q(a, ps=(5, 50, 95)):
    a = np.asarray(a, float)
    return [float(np.percentile(a, p)) for p in ps]


def summary(r):
    top = r["top"]
    vals, counts = np.unique(top, return_counts=True)
    return {"stated_bottom_p5_p50_p95": C.qs(r["bottom"]), "stated_top_p5_p50_p95": C.qs(top),
            "top_unrounded_p5_p50_p95": q(r["top_raw"]), "top_unrounded_mean": float(np.mean(r["top_raw"])),
            "share_top_at_least": {f"{t // 1000}k": float((top >= t).mean()) for t in TOPS},
            "share_top_exactly": {f"{int(v) // 1000}k": float(n / top.size) for v, n in zip(vals, counts)},
            "funds_pay_p5_p50_p95": q(r["pay"]), "excess_p5_p50_p95": q(r["excess"]),
            "half_kept_p5_p50_p95": q(r["kept33"]), "flexibility_kept_plus_excess_p5_p50_p95": q(r["flex"]),
            "contribution_equals_top_share": float((np.abs(r["gift"] - top) < 0.5).mean()),
            "moved_half_on_move_day_p5_p50_p95": q(r["moved_money"])}


def compare(r0, r1, fell):
    """Path by path, a later move (r1) against an earlier one (r0). fell: VT lower on the later date than the earlier."""
    d = r1["top"] - r0["top"]
    du = r1["top_raw"] - r0["top_raw"]
    lower, higher = d < -0.5, d > 0.5
    o = {"share_top_lower": float(lower.mean()), "share_top_higher": float(higher.mean()),
         "share_top_same": float((~lower & ~higher).mean()),
         "share_vt_fell_between": float(fell.mean()),
         "share_fell_and_top_lower": float((fell & lower).mean()),
         "share_top_lower_if_fell": float(lower[fell].mean()) if fell.any() else None,
         "share_top_higher_if_rose": float(higher[~fell].mean()) if (~fell).any() else None,
         "top_change_p5_p50_p95": q(d), "top_unrounded_change_p5_p50_p95": q(du),
         "top_change_where_lower_p50_min": [float(np.median(d[lower])), float(d.min())] if lower.any() else [0.0, 0.0],
         "flexibility_change_p5_p50_p95": q(r1["flex"] - r0["flex"]),
         "half_kept_identical": bool(np.allclose(r1["kept33"], r0["kept33"], rtol=1e-12, atol=1e-6)),
         "bottom_identical": bool(np.array_equal(r1["bottom"], r0["bottom"]))}
    return o


out = {"stamp": {"run": RUN, "status": "MODEL", "curve": E.CURVE_DAY, "design": NAME, "rule": C.RULE_VERSION,
                 "numbers_section": "8r", "register_move_date": "1 Jan 2031 (NUMBERS 4: trade Thu 2 Jan 2031)",
                 "moves": {k: str(v[0]) for k, v in MOVES.items()}, "extra_seed": SEED_EXTRA}}

# ---------------------------------------------------------------- central path: VT 7.5% a year, today's forwards
cen = P.run(c, margin=MARGIN, margin_fn=MF)
central = {}
for key, (mv, k) in MOVES.items():
    t3 = 3 + k / 12
    r = moved_and_rule(cen, mv, k, 1.075 ** t3, 1.075 ** (5 - t3), 0.0, 1.0, 0.0, 1.0)
    if key == "jan":
        check_jan(cen, r, 0.0, 0.0)
    f = lambda x: float(np.asarray(x).item())
    central[key] = {"vt_on_move_day": f(r["vt_move"]), "moved_money": f(r["moved_money"]),
                    "moved_yield_forward": c.fwd(mv, END), "moved_zero_per_dollar": f(r["zM"]),
                    "moved_pays": f(r["moved"]), "bottom_unrounded": f(r["bottom_raw"]), "bottom": f(r["bottom"]),
                    "top_unrounded": f(r["top_raw"]), "top": f(r["top"]), "funds_pay": f(r["pay"]),
                    "contribution": f(r["gift"]), "excess": f(r["excess"]), "half_kept": f(r["kept33"]),
                    "flexibility": f(r["flex"]),
                    "moved_cut_share_of_its_payout": 1 - f(r["zM"]) * (1 - C.HAIRCUT) * f(r["moved_money"]) / f(r["moved"])}
assert round(central["jan"]["top_unrounded"]) == 118_072 and round(central["jan"]["bottom_unrounded"]) == 98_380
assert round(central["jan"]["excess"]) == 8_476 and round(central["jan"]["half_kept"]) == 21_347
out["central"] = central

# ---------------------------------------------------------------- house model
d0, d1, d2, vt3, vt2 = P.draws()
H = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, vt3, vt2, MF)
rng = np.random.default_rng(SEED_EXTRA)
X2 = np.log(vt2)                                   # VT's log growth Jan 2031 -> Jan 2033 (drift included)
t1, t2 = 0.25, 0.5
X1 = X2 * t1 / 2 + SD * math.sqrt(t1 * (2 - t1) / 2) * rng.normal(size=P.N)                 # bridge to 1 Apr
Xh = X1 + (t2 - t1) / (2 - t1) * (X2 - X1) + SD * math.sqrt((t2 - t1) * (2 - t2) / (2 - t1)) * rng.normal(size=P.N)
e1 = rng.normal(0, YV * math.sqrt(t1), P.N)                                                  # yields, Jan -> Apr
e2 = rng.normal(0, YV * math.sqrt(t2 - t1), P.N)                                             # Apr -> Jul
G = {"jan": 1.0, "apr": np.exp(X1), "jul": np.exp(Xh)}
SM = {"jan": d0 + d1 + d2, "apr": d0 + d1 + d2 + e1, "jul": d0 + d1 + d2 + e1 + e2}
house_r = {}
for key, (mv, k) in MOVES.items():
    house_r[key] = moved_and_rule(H, mv, k, vt3 * G[key], vt2 / G[key], SM[key], 1.0, d0 + d1, 1.0)
check_jan(H, house_r["jan"], d0 + d1, d0 + d1 + d2)
house = {key: summary(r) for key, r in house_r.items()}
assert house["jan"]["stated_top_p5_p50_p95"] == [95_000.0, 115_000.0, 140_000.0]
assert round(house["jan"]["share_top_at_least"]["115k"], 4) == 0.5979                       # NUMBERS 4: 59.8%
house["bridge_check"] = {"vt_growth_jan_to_apr_median_and_mean": [float(np.median(G["apr"])), float(np.mean(G["apr"]))],
                         "expected_mean_jan_to_apr": math.exp(MU * t1 + SD ** 2 * t1 / 2),
                         "vt_log_sd_jan_to_apr": float(np.std(X1)), "expected_sd_jan_to_apr": SD * math.sqrt(t1),
                         "vt_log_sd_jan_to_jul": float(np.std(Xh)), "expected_sd_jan_to_jul": SD * math.sqrt(t2)}
house["compare"] = {"apr_vs_jan": compare(house_r["jan"], house_r["apr"], G["apr"] < 1.0),
                    "jul_vs_jan": compare(house_r["jan"], house_r["jul"], G["jul"] < 1.0),
                    "jul_vs_apr": compare(house_r["apr"], house_r["jul"], G["jul"] < G["apr"])}
for key in ("apr", "jul"):
    fell = G[key] < 1.0
    for cut in (0.9, 0.8):
        house["compare"][f"{key}_vs_jan"][f"if_vt_down_more_than_{round((1 - cut) * 100)}pct"] = {
            "share_paths": float((G[key] < cut).mean()),
            "share_top_lower": float((house_r[key]["top"] < house_r["jan"]["top"] - 0.5)[G[key] < cut].mean()),
            "top_change_p50": float(np.median((house_r[key]["top"] - house_r["jan"]["top"])[G[key] < cut]))}
out["house"] = house

# ---------------------------------------------------------------- US stock history (rates at forwards)
import csv   # noqa: E402
p, dv, keys = [], [], []
for row in csv.DictReader(open(E.ROOT / "keel/models/data/shiller_monthly.csv")):
    if row["Date"] >= "2023-07":
        break
    p.append(float(row["SP500"]))
    dv.append(float(row["Dividend"]))
    keys.append(row["Date"][:7])
p, dv = np.array(p), np.array(dv)
idx = np.r_[1.0, np.cumprod((p[1:] + dv[:-1] / 12) / p[:-1])]
nw = len(idx) - 60
w_reg = P.shiller_windows()
assert nw == len(w_reg)
ii = np.arange(nw)
HS = P.history(c, margin=MARGIN, margin_fn=MF)
hist_r, GH = {}, {}
for key, (mv, k) in MOVES.items():
    g_to = idx[ii + 36 + k] / idx[ii]
    g_af = idx[ii + 60] / idx[ii + 36 + k]
    if key == "jan":
        assert np.allclose(g_to, [a for _, a, _ in w_reg]) and np.allclose(g_af, [b for _, _, b in w_reg])
    GH[key] = idx[ii + 36 + k] / idx[ii + 36]
    hist_r[key] = moved_and_rule(HS, mv, k, g_to, g_af, 0.0, 1.0, 0.0, 1.0)
check_jan(HS, hist_r["jan"], 0.0, 0.0)
hist = {key: summary(r) for key, r in hist_r.items()}
assert hist["jan"]["stated_top_p5_p50_p95"] == [110_000.0, 115_000.0, 130_000.0]
hist["compare"] = {"apr_vs_jan": compare(hist_r["jan"], hist_r["apr"], GH["apr"] < 1.0),
                   "jul_vs_jan": compare(hist_r["jan"], hist_r["jul"], GH["jul"] < 1.0),
                   "jul_vs_apr": compare(hist_r["apr"], hist_r["jul"], GH["jul"] < GH["apr"])}
starts = [k_ for k_, _, _ in w_reg]
named = {}
for s0 in ("1929-07", "1929-09", "1973-01", "1987-01", "2000-01", "2007-07", "2008-01", "2017-01"):
    if s0 in starts:
        i = starts.index(s0)
        named[s0] = {key: {"top": float(hist_r[key]["top"][i]), "top_unrounded": float(hist_r[key]["top_raw"][i]),
                           "flexibility": float(hist_r[key]["flex"][i]),
                           "vt_since_jan_move_day": float(GH[key][i] - 1)} for key in MOVES}
hist["named_vt_purchases"] = named
out["history"] = hist

# ---------------------------------------------------------------- joint replay: rates and US stocks, same months
pos = {k_: i for i, k_ in enumerate(keys)}
st = P.setup(c)
DGS1 = E.ROOT / "archive/rab/data/fred/DGS1.csv"
rows = []
for s0, mult in E.history_windows(DGS1, "DGS1"):
    i0 = pos.get(s0)
    if i0 is None or i0 + 72 >= len(idx):
        continue
    rows.append((s0, i0, mult(E.J28), {key: mult(mv) for key, (mv, _) in MOVES.items()}))
assert len(rows) == 585
i0s = np.array([r[1] for r in rows])
m28 = np.array([r[2] for r in rows])
mM = {key: np.array([r[3][key] for r in rows]) for key in MOVES}
jd1 = st["fF"] * (m28 - 1)
jd2 = st["fM"] * mM["jan"] - st["fM"] - jd1
JB = P.run(c, MARGIN, None, 150_000.0, 0.0, jd1, jd2, idx[i0s + 48] / idx[i0s + 12], idx[i0s + 72] / idx[i0s + 48],
           C.margin_fn_mult(NAME, m28))
joint_r, GJ = {}, {}
for key, (mv, k) in MOVES.items():
    g_to = idx[i0s + 48 + k] / idx[i0s + 12]
    g_af = idx[i0s + 72] / idx[i0s + 48 + k]
    GJ[key] = idx[i0s + 48 + k] / idx[i0s + 48]
    joint_r[key] = moved_and_rule(JB, mv, k, g_to, g_af, 0.0, mM[key], 0.0, m28)
check_jan(JB, joint_r["jan"], 0.0, 0.0, m28, mM["jan"])
joint = {key: summary(r) for key, r in joint_r.items()}
assert joint["jan"]["stated_top_p5_p50_p95"] == [95_000.0, 115_000.0, 140_000.0]
assert joint["jan"]["stated_bottom_p5_p50_p95"] == [80_000.0, 95_000.0, 115_000.0]
joint["compare"] = {"apr_vs_jan": compare(joint_r["jan"], joint_r["apr"], GJ["apr"] < 1.0),
                    "jul_vs_jan": compare(joint_r["jan"], joint_r["jul"], GJ["jul"] < 1.0),
                    "jul_vs_apr": compare(joint_r["apr"], joint_r["jul"], GJ["jul"] < GJ["apr"])}
joint["note"] = ("funds pay as plan.run models them at the path's purchase yields (range_rule.py section 5), not as "
                 "realised on the window's rates (8i)")
out["joint"] = joint

json.dump(out, open(OUTFILE, "w"), indent=1, default=float)


# ---------------------------------------------------------------- print
def m(x):
    return f"${x:,.0f}"


for key, v in central.items():
    print("central", key, {a: (m(b) if abs(b) > 10 else round(b, 6)) for a, b in v.items()})
for wname, w in (("house", house), ("history", hist), ("joint", joint)):
    for key in MOVES:
        s = w[key]
        print(wname, key, "bottom", s["stated_bottom_p5_p50_p95"], "top", s["stated_top_p5_p50_p95"],
              "top unrounded", [round(x) for x in s["top_unrounded_p5_p50_p95"]], "mean", round(s["top_unrounded_mean"]),
              "| kept", [round(x) for x in s["half_kept_p5_p50_p95"][:2]], "flex",
              [round(x) for x in s["flexibility_kept_plus_excess_p5_p50_p95"][:2]],
              "| contribution = top", s["contribution_equals_top_share"])
        print("   at least", {a: round(b, 4) for a, b in s["share_top_at_least"].items()})
    for cmpk, cv in w["compare"].items():
        print("  ", wname, cmpk, json.dumps({a: (round(b, 4) if isinstance(b, float) else b) for a, b in cv.items()
                                             if not isinstance(b, (list, dict))}),
              "change p5/50/95", cv["top_change_p5_p50_p95"], "unrounded", [round(x) for x in cv["top_unrounded_change_p5_p50_p95"]],
              "flex", [round(x) for x in cv["flexibility_change_p5_p50_p95"]])
print("bridge", house["bridge_check"])
for s0, v in named.items():
    print("named", s0, json.dumps(v))
