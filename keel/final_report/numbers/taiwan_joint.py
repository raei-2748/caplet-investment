"""Both Taiwan risks together: building costs and the Taiwan dollar against her flexibility (numbers owner,
Mon 16 Nov 2026, Sydney). MODEL, not a forecast or a promise. NUMBERS 8q.

Run from the repo root:  python3 -I keel/final_report/numbers/taiwan_joint.py
   or from this folder:  python3 -I taiwan_joint.py
Writes keel/final_report/numbers/results_taiwan_joint_2026-11-16.json and prints the figures (about 15 seconds, numpy
only). Imports engine.py, plan.py and completion.py and changes none of them; runs joint_stress.py's own setup code
(as range_margin.py does: up to its first results block, nothing it writes); reads no results file.

The question (card Q10e, research/cards/Q10e_taiwan_two_risks_together.md; NUMBERS 9). NUMBERS 8j tests one use of her
flexibility, a 10% stronger Taiwan dollar. Card Q10e built the US-dollar cost of a fixed Taiwan building budget since
1991 (DGBAS's construction cost index divided by NT$ per US$) and found its two-year rise was +28.0% at the 1-in-20
point and +38.9% at worst (Jul 2006 to Jul 2008). Here those two figures, and the 18-month 1-in-20 (+24.6%), are run
against her flexibility exactly the way 8j runs 10%:
  * the gift is the 2033 contribution after the cap (the lower of what the floor and the moved half pay and the stated
    top; NUMBERS 4, "One definition, used everywhere"); it equals the stated top in every path and window, so a test on
    the stated top and a test on the contribution she names are the same test (the share is reported). The stated
    bottom is shown beside it as the lower reading (a facility budget set on the figure fixed in January 2028);
  * "x% rise" = x% more US dollars for the same NT$ building (8j's convention, card Q10e's);
  * two pots, as 8j: the half kept alone (VT's market value on 1 Jan 2033) and the half kept plus the excess the cap
    sends to it (paid on or about 15 Dec 2032, at face);
  * three worlds, as 8j: house model (plan.draws + plan.run + completion.rule, 200,000 paths, seed 2033), US stock
    history (plan.history, 1,770 windows since 1871, rates at today's forwards), joint replay (joint_stress.py's J, 585
    windows, funds pay as realised on each window's own rates);
  * then the real joint series on the same months as the shares (as 8j's real-Taiwan-dollar test): the history model's
    pots and contribution, and the joint move from the meetings (VT purchase + 36 months) to the gift (+ 60 months);
  * and an independent pairing: every house path against every 24-month joint move since 1991 (the move drawn apart
    from the shares).
Every "need" is the rise times the gift, in December 2032 money; every "left" is the pot less the need, at face.
"Keel arithmetic" in the JSON marks arithmetic on register figures that is not itself a register figure.

Data:
  * DGBAS construction cost index (營造工程物價指數, total index, 2021 = 100), monthly Jan 1991 to Sep 2026: the series
    card Q10e read at source on Sun 15 Nov 2026 (ws.dgbas.gov.tw, ccispl.xls linked table / cciidx.xls), copied below
    unchanged. Not re-read today (curl to ws.dgbas.gov.tw is refused, 403). Cross-checked against the register's own
    earlier read (numbers/inflation_inputs.json, card Q10, 9 Nov): Sep 2026 120.26 and its 1-, 5-, 10-, 26- and 35-year
    rates all agree (checks block).
  * NT$ per US$: the repo mirror of FRED EXTAUS (keel/models/data/twd_per_usd_monthly.csv), VERIFIED against FRED for
    all 516 months on Wed 11 Nov (NUMBERS 8l), the file 8j reads.
"""
import ast
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E        # noqa: E402
import plan as P          # noqa: E402
import completion as C    # noqa: E402

RUN = "Mon 16 Nov 2026 (Sydney)"
OUTFILE = HERE / f"results_taiwan_joint_{C.RESULTS}.json"   # Tue 17 Nov evening re-run; the 2026-11-16 file is the record
NAME = C.design_arg()
DSG = C.design(NAME)
MARGIN = DSG["margin"]
MF = C.margin_fn(NAME)
c = E.Curve(E.load_par())
TWD = E.ROOT / "keel/models/data/twd_per_usd_monthly.csv"

# DGBAS construction cost index, total, 2021 = 100; Jan to Dec of each year (card Q10e's read of 15 Nov 2026)
CCI_TEXT = """
1991 | 43.91 | 43.99 | 43.89 | 43.93 | 43.82 | 43.68 | 43.72 | 43.71 | 43.89 | 44.00 | 44.09 | 44.10
1992 | 44.46 | 44.82 | 48.85 | 50.48 | 50.62 | 50.89 | 51.62 | 51.90 | 52.48 | 52.91 | 52.94 | 53.70
1993 | 53.85 | 53.65 | 53.91 | 54.14 | 54.13 | 53.89 | 53.73 | 53.71 | 53.42 | 53.12 | 52.87 | 52.41
1994 | 51.90 | 51.95 | 51.81 | 51.76 | 51.54 | 51.33 | 51.08 | 51.02 | 51.11 | 51.26 | 51.03 | 50.86
1995 | 51.17 | 51.60 | 51.83 | 51.90 | 51.83 | 52.08 | 51.90 | 52.07 | 52.18 | 52.15 | 52.11 | 51.91
1996 | 51.85 | 51.74 | 51.62 | 51.50 | 51.40 | 51.09 | 51.26 | 51.67 | 51.75 | 51.67 | 51.53 | 51.67
1997 | 51.70 | 52.13 | 52.38 | 52.62 | 52.77 | 52.75 | 52.74 | 52.70 | 52.79 | 52.72 | 52.98 | 53.30
1998 | 53.72 | 54.02 | 54.02 | 53.93 | 53.97 | 54.09 | 54.09 | 54.09 | 53.99 | 53.98 | 53.78 | 53.57
1999 | 53.45 | 53.46 | 53.52 | 53.66 | 53.69 | 53.66 | 53.71 | 53.65 | 53.59 | 53.76 | 53.74 | 53.70
2000 | 53.35 | 53.41 | 53.62 | 53.66 | 53.67 | 53.65 | 53.56 | 53.33 | 53.14 | 53.15 | 52.99 | 52.91
2001 | 52.84 | 52.77 | 52.69 | 52.57 | 52.56 | 52.80 | 52.91 | 53.12 | 52.91 | 52.93 | 52.95 | 52.93
2002 | 52.98 | 53.14 | 53.30 | 53.53 | 53.84 | 54.49 | 54.57 | 54.49 | 54.16 | 54.13 | 54.25 | 54.48
2003 | 55.05 | 55.97 | 56.69 | 56.51 | 56.08 | 55.89 | 56.31 | 56.59 | 56.69 | 56.64 | 57.00 | 58.18
2004 | 60.12 | 63.17 | 64.92 | 64.47 | 64.06 | 63.78 | 64.93 | 65.62 | 65.58 | 65.98 | 65.53 | 65.18
2005 | 64.91 | 65.30 | 65.53 | 65.43 | 64.95 | 64.24 | 64.13 | 64.39 | 64.92 | 64.98 | 64.88 | 65.04
2006 | 65.38 | 65.66 | 66.50 | 67.92 | 70.31 | 70.78 | 71.10 | 71.02 | 71.23 | 71.59 | 71.83 | 71.84
2007 | 72.11 | 72.75 | 73.82 | 74.95 | 75.47 | 76.16 | 76.25 | 76.44 | 76.94 | 77.91 | 78.11 | 79.41
2008 | 81.09 | 82.87 | 86.00 | 88.13 | 89.74 | 91.98 | 92.10 | 90.92 | 87.90 | 85.00 | 81.59 | 80.33
2009 | 79.77 | 79.70 | 78.52 | 78.29 | 78.19 | 78.19 | 78.45 | 78.92 | 79.33 | 78.77 | 78.63 | 78.97
2010 | 79.80 | 80.12 | 81.01 | 82.75 | 82.51 | 81.31 | 81.05 | 81.26 | 81.36 | 81.23 | 81.50 | 82.01
2011 | 83.02 | 83.35 | 84.12 | 83.98 | 84.07 | 84.15 | 84.11 | 84.31 | 84.47 | 84.56 | 84.01 | 84.23
2012 | 84.45 | 84.60 | 84.87 | 85.70 | 85.96 | 85.43 | 84.95 | 84.81 | 84.19 | 83.71 | 84.00 | 84.11
2013 | 84.53 | 84.75 | 84.88 | 84.48 | 84.14 | 83.92 | 83.96 | 84.10 | 84.49 | 84.48 | 84.69 | 84.88
2014 | 85.19 | 85.26 | 85.28 | 85.82 | 86.03 | 86.42 | 86.62 | 86.72 | 86.61 | 86.19 | 85.96 | 85.74
2015 | 85.43 | 84.93 | 84.69 | 84.50 | 84.10 | 84.01 | 83.42 | 82.93 | 82.74 | 82.14 | 82.02 | 81.79
2016 | 81.64 | 81.46 | 81.56 | 82.48 | 83.02 | 82.44 | 82.18 | 82.13 | 81.93 | 81.73 | 82.24 | 83.02
2017 | 83.52 | 83.59 | 83.98 | 83.71 | 83.20 | 83.28 | 83.50 | 84.38 | 84.97 | 84.89 | 85.15 | 85.33
2018 | 85.80 | 85.61 | 86.08 | 86.22 | 86.47 | 86.78 | 87.30 | 87.49 | 87.82 | 88.13 | 87.94 | 87.74
2019 | 87.84 | 88.57 | 89.04 | 89.11 | 88.93 | 89.06 | 89.05 | 89.20 | 89.00 | 88.66 | 88.82 | 89.23
2020 | 89.52 | 89.42 | 89.64 | 89.23 | 89.29 | 89.57 | 89.59 | 89.94 | 90.59 | 90.84 | 91.31 | 92.76
2021 | 94.90 | 94.94 | 95.97 | 97.34 | 99.60 | 101.25 | 101.87 | 102.15 | 102.39 | 102.98 | 103.36 | 103.25
2022 | 103.67 | 104.47 | 106.88 | 108.83 | 109.05 | 109.02 | 108.11 | 107.32 | 107.96 | 107.69 | 107.45 | 107.92
2023 | 108.69 | 109.21 | 109.49 | 109.60 | 109.00 | 108.76 | 108.96 | 109.04 | 109.25 | 109.48 | 109.38 | 109.88
2024 | 110.26 | 110.48 | 110.50 | 111.07 | 111.60 | 111.91 | 112.02 | 111.82 | 111.56 | 111.75 | 112.04 | 111.84
2025 | 111.81 | 112.16 | 112.56 | 112.49 | 112.23 | 111.97 | 111.83 | 112.15 | 112.09 | 112.43 | 112.66 | 112.86
2026 | 113.81 | 114.69 | 115.62 | 117.50 | 118.77 | 119.16 | 119.14 | 119.48 | 120.26
"""


def load_cci():
    out = {}
    for line in CCI_TEXT.strip().splitlines():
        p = [x.strip() for x in line.split("|")]
        for m, v in enumerate(p[1:], 1):
            if v:
                out[f"{int(p[0]):04d}-{m:02d}"] = float(v)
    return out


def add_months(key, k):
    y, m = int(key[:4]), int(key[5:7]) + k
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    return f"{y:04d}-{m:02d}"


CCI = load_cci()
FX = {r["Date"][:7]: float(r["TWD_per_USD"]) for r in csv.DictReader(open(TWD))}
MONTHS = sorted(k for k in CCI if k in FX)
U = {k: CCI[k] / FX[k] for k in MONTHS}          # US-dollar cost of a fixed NT$ building, index


def joint_move(a, b):
    """Percentage more US dollars the same NT$ building needs at month b than at month a (card Q10e, 8j's convention)."""
    return U[b] / U[a] - 1


def q(a, ps=(5, 50, 95)):
    a = np.asarray(a, float)
    return [float(np.percentile(a, p)) for p in ps] if a.size else None


out = {"stamp": {"run": RUN, "status": "MODEL", "curve": E.CURVE_DAY, "design": NAME, "rule": C.RULE_VERSION,
                 "card": "research/cards/Q10e_taiwan_two_risks_together.md", "numbers_section": "8q",
                 "cci": "DGBAS construction cost index, total, 2021 = 100, Jan 1991 to Sep 2026 (card Q10e's read of "
                        "15 Nov 2026, copied into this script; not re-read today: curl refused, 403)",
                 "twd": "keel/models/data/twd_per_usd_monthly.csv (FRED EXTAUS mirror, VERIFIED 11 Nov, NUMBERS 8l)"}}

# ---------------------------------------------------------------- 0. data checks
inf = json.load(open(HERE / "inflation_inputs.json"))["taiwan_construction"]
g = inf["growth"]
chk = {
    "sep2026_level": [CCI["2026-09"], inf["latest"]["level"]],
    "1y_sep": [CCI["2026-09"] / CCI["2025-09"] - 1, g["1y_sep"]],
    "5y_total": [CCI["2026-09"] / CCI["2021-09"] - 1, g["5y_total"]],
    "10y_total": [CCI["2026-09"] / CCI["2016-09"] - 1, g["10y_total"]],
    "since_sep_2000_per_year": [(CCI["2026-09"] / CCI["2000-09"]) ** (1 / 26) - 1, g["since_sep_2000_per_year"]],
    "since_sep_1991_per_year": [(CCI["2026-09"] / CCI["1991-09"]) ** (1 / 35) - 1, g["since_sep_1991_per_year"]],
}
for k, (a, b) in chk.items():
    assert abs(a - b) < 6e-4, (k, a, b)
out["checks"] = {"cci_against_register_read_of_9_nov": chk, "months_in_joint_series": len(MONTHS),
                 "first_month": MONTHS[0], "last_month": MONTHS[-1]}

# ---------------------------------------------------------------- 1. the joint series' own figures (reproduces card Q10e)
series = {}
for h in (18, 24):
    rows = []
    for a in MONTHS:
        b = add_months(a, h)
        if b in U:
            rows.append((joint_move(a, b), a, b, CCI[b] / CCI[a] - 1, FX[a] / FX[b] - 1))
    js = np.array([r[0] for r in rows])
    mx = max(rows)
    series[f"{h}m"] = {"windows": len(rows), "first_start": rows[0][1], "last_start": rows[-1][1],
                       "median": float(np.median(js)), "p90": float(np.percentile(js, 90)),
                       "p95_1in20": float(np.percentile(js, 95)), "p99": float(np.percentile(js, 99)),
                       "max": float(mx[0]), "max_window": [mx[1], mx[2]], "max_cost_part": float(mx[3]),
                       "max_currency_part": float(mx[4]),
                       "share_above": {f"{x:.2f}": float((js > x).mean()) for x in (0.10, 0.15, 0.20, 0.25, 0.28)},
                       "moves": js}
S24, S18 = series["24m"], series["18m"]
# card Q10e: 405 windows, 1-in-20 +28.0%, worst +38.9% Jul 2006 to Jul 2008; 18 months: 411 windows, 1-in-20 +24.6%
assert S24["windows"] == 405 and round(S24["p95_1in20"] * 100, 1) == 28.0, S24["p95_1in20"]
assert round(S24["max"] * 100, 1) == 38.9 and S24["max_window"] == ["2006-07", "2008-07"], (S24["max"], S24["max_window"])
assert S18["windows"] == 411 and round(S18["p95_1in20"] * 100, 1) == 24.6, S18["p95_1in20"]
out["joint_series"] = {k: {kk: vv for kk, vv in v.items() if kk != "moves"} for k, v in series.items()}

STRESS = {"currency_10pct_8j": 0.10,                              # 8j's test, run again as the check on the pots
          "joint_18m_1in20": S18["p95_1in20"],                    # +24.6%: mid-2031 meetings to December 2032
          "joint_24m_1in20": S24["p95_1in20"],                    # +28.0%: January 2031 meetings to January 2033
          "joint_24m_worst_jul2006_jul2008": S24["max"]}          # +38.9%
out["stresses"] = STRESS


# ---------------------------------------------------------------- 2. the register's pots in three worlds (as 8j)
def joint_setup():
    """joint_stress.py's own top-level code up to its first results block (def window), skipping every statement that
    assigns to its `out` dict; nothing is written (copied from range_margin.py, unchanged logic)."""
    path = HERE / "joint_stress.py"
    tree = ast.parse(path.read_text())

    def touches_out(t):
        while isinstance(t, (ast.Subscript, ast.Attribute)):
            t = t.value
        return isinstance(t, ast.Name) and t.id == "out"

    body = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "window":
            break
        if isinstance(node, ast.Assign) and any(touches_out(t) for t in node.targets):
            continue
        body.append(node)
    ns = {"__name__": "joint_stress_setup", "__file__": str(path)}
    exec(compile(ast.Module(body=body, type_ignores=[]), str(path), "exec"), ns)
    return ns


d0, d1, d2, vt3, vt2 = P.draws()
H = P.run(c, MARGIN, None, 150_000.0, d0, d1, d2, vt3, vt2, MF)
Hr = C.rule(H, d0 + d1, d0 + d1 + d2)
HS = P.history(c, margin=MARGIN, margin_fn=MF)
HSr = C.rule(HS)
NS = joint_setup()
J = NS["J"]
cen = P.run(c, margin=MARGIN, margin_fn=MF)
cr = C.rule(cen)
nh = len(HS["starts"])
bc = lambda x, n: np.broadcast_to(np.asarray(x, float), (n,)).copy()
WORLDS = {
    "central": dict(kept=np.atleast_1d(float(cen["kept33"])), contrib=np.atleast_1d(float(cr["gift"])),
                    excess=np.atleast_1d(float(cr["excess"])), top=np.atleast_1d(float(cr["top"])),
                    bottom=np.atleast_1d(float(cr["bottom"])), label="today's forwards, VT 7.5% a year"),
    "house": dict(kept=np.asarray(H["kept33"], float), contrib=Hr["gift"], excess=Hr["excess"], top=Hr["top"],
                  bottom=Hr["bottom"], label="house model, 200,000 paths, seed 2033"),
    "history": dict(kept=np.asarray(HS["kept33"], float), contrib=bc(HSr["gift"], nh), excess=bc(HSr["excess"], nh),
                    top=bc(HSr["top"], nh), bottom=bc(HSr["bottom"], nh),
                    label="US stock history, 1,770 windows since 1871, rates at today's forwards"),
    "joint": dict(kept=np.asarray(J["kept33"], float), contrib=np.asarray(J["gift_capped"], float),
                  excess=np.asarray(J["excess"], float), top=np.asarray(J["top_stated"], float),
                  bottom=np.asarray(J["bottom_stated"], float),
                  label="joint replay, 585 windows (Jan 1962 to Sep 2010 starts), funds pay as realised"),
}
# register checks: section 4's central figures and 8f's pots, 8j's 10% coverage
# (Tue 17 Nov evening re-run: the payments' 0.5% margin and the 365.25-day carry; the Mon 16 Nov values were $8,476,
# $21,347, [9,881, 20,739], [16,508, 28,918], [20,469, 31,314], [20,180, 32,326])
reg = {"central_contribution": [float(cr["gift"]), 115_000.0], "central_excess": [round(float(cr["excess"])), 7_503],
       "central_kept": [round(float(cen["kept33"])), 21_179],
       "house_kept_p5_p50": [[round(x) for x in q(H["kept33"], (5, 50))], [9_621, 20_486]],
       "house_kept_plus_excess_p5_p50": [[round(x) for x in q(H["kept33"] + Hr["excess"], (5, 50))], [16_176, 28_624]],
       "history_kept_plus_excess_p5_p50": [[round(x) for x in q(HS["kept33"] + HSr["excess"], (5, 50))],
                                           [20_387, 31_308]],
       "joint_kept_plus_excess_p5_p50": [[round(x) for x in q(J["kept33"] + J["excess"], (5, 50))], [19_412, 31_845]]}
for k, (a, b) in reg.items():
    assert a == b, (k, a, b)
cov10 = {w: [float((WORLDS[w]["kept"] >= 0.10 * WORLDS[w]["contrib"]).mean()),
             float((WORLDS[w]["kept"] + WORLDS[w]["excess"] >= 0.10 * WORLDS[w]["contrib"]).mean())]
         for w in ("house", "history", "joint")}
assert round(cov10["house"][0], 3) == 0.929 and round(cov10["house"][1], 4) == 0.9974, cov10     # 8j: 92.9%, 99.74% (17 Nov evening; were 93.3%, 99.80%)
assert round(cov10["history"][0], 3) == 0.969 and cov10["history"][1] == 1.0, cov10              # 96.9%, 100% (was 97.1%)
assert round(cov10["joint"][0], 3) == 0.991 and cov10["joint"][1] == 1.0, cov10                  # 99.1%, 100% (was 99.3%)
out["checks"]["register"] = reg
out["checks"]["8j_10pct_reproduced_kept_and_kept_plus_excess"] = cov10
out["checks"]["contribution_equals_stated_top_share"] = {
    w: float((np.abs(WORLDS[w]["contrib"] - WORLDS[w]["top"]) < 0.5).mean()) for w in WORLDS}


# ---------------------------------------------------------------- 3. the fixed stresses (8j's method)
def test(world, x, base):
    """Share of paths in which each pot covers a rise of x on the gift (base 'contribution' or 'stated_bottom')."""
    w = WORLDS[world]
    gift = w["contrib"] if base == "contribution" else w["bottom"]
    need = gift * x
    o = {"need_p5_p50_p95": q(need)}
    for name, pot in (("kept_half", w["kept"]), ("kept_half_plus_excess", w["kept"] + w["excess"])):
        left = pot - need
        ok = left >= 0
        gap = -left[~ok]
        o[name] = {"covers": float(ok.mean()), "fails_count": int((~ok).sum()), "paths": int(ok.size),
                   "left_p5_p50_p95": q(left), "left_min": float(left.min()),
                   "left_where_covered_p50": float(np.median(left[ok])) if ok.any() else None,
                   "gap_when_fails_p50_p95_max": ([float(np.median(gap)), float(np.percentile(gap, 95)),
                                                   float(gap.max())] if gap.size else [0.0, 0.0, 0.0])}
    return o


fixed = {}
for wname in WORLDS:
    fixed[wname] = {}
    for sname, x in STRESS.items():
        fixed[wname][sname] = {base: test(wname, x, base) for base in ("contribution", "stated_bottom")}
out["fixed_stresses"] = fixed
# the rise each pot covers 19 times in 20 (its 5th percentile over the contribution); 8j quotes the house figures
out["rise_covered_19_in_20"] = {w: {"kept_half": float(np.percentile(WORLDS[w]["kept"] / WORLDS[w]["contrib"], 5)),
                                    "kept_half_plus_excess": float(np.percentile(
                                        (WORLDS[w]["kept"] + WORLDS[w]["excess"]) / WORLDS[w]["contrib"], 5))}
                                for w in ("house", "history", "joint")}
out["rise_covered_central"] = {"kept_half": float(cen["kept33"] / cr["gift"]),
                               "kept_half_plus_excess": float((cen["kept33"] + cr["excess"]) / cr["gift"])}

# ---------------------------------------------------------------- 4. the real joint series on the same months as the shares
# The history model (US stocks, rates at forwards): VT bought in month s; meetings s + 36 (Jan 2031 in the plan); gift
# s + 60 (Jan 2033). Need = the contribution x the joint move from the meetings to the gift (only rises count).
keys, idx = NS["keys"], NS["idx"]
kpos = {k: i for i, k in enumerate(keys)}
sel, mv, st_ = [], [], []
for i, s0 in enumerate(HS["starts"]):
    j0 = kpos[s0]
    if j0 + 60 < len(keys) and keys[j0 + 36] in U and keys[j0 + 60] in U:
        sel.append(i)
        mv.append(joint_move(keys[j0 + 36], keys[j0 + 60]))
        st_.append(s0)
sel, mv = np.array(sel), np.array(mv)
kk = WORLDS["history"]["kept"][sel]
ee = WORLDS["history"]["excess"][sel]
cc = WORLDS["history"]["contrib"][sel]
bb = WORLDS["history"]["bottom"][sel]
shares5 = np.array([idx[kpos[s] + 60] / idx[kpos[s]] for s in st_])
shares2 = np.array([idx[kpos[s] + 60] / idx[kpos[s] + 36] for s in st_])
rt = {"windows": int(sel.size), "first_vt_purchase": st_[0], "last_vt_purchase": st_[-1],
      "meeting_to_gift": "VT purchase + 36 months to + 60 months (Jan 2031 to Jan 2033 in the plan)",
      "move_p5_p50_p95": q(mv), "move_max_and_start": [float(mv.max()), st_[int(np.argmax(mv))]],
      "share_move_above": {f"{x:.2f}": float((mv > x).mean()) for x in (0.10, 0.20, 0.25, 0.28)},
      "contribution_p5_p50_p95": C.qs(cc),
      "corr_move_vs_us_shares_2031_2033": float(np.corrcoef(mv, np.log(shares2))[0, 1]),
      "corr_move_vs_us_shares_2028_2033": float(np.corrcoef(mv, np.log(shares5))[0, 1])}
for base, gift in (("contribution", cc), ("stated_bottom", bb)):
    rt[base] = {}
    for name, pot in (("kept_half", kk), ("kept_half_plus_excess", kk + ee)):
        need = gift * np.maximum(mv, 0.0)
        left = pot - need
        bad = left < 0
        rt[base][name] = {"covers_actual_move": float((~bad).mean()), "fails_count": int(bad.sum()),
                          "fails_starts": [s for s, b in zip(st_, bad) if b],
                          "gap_when_fails_p50_max": ([float(np.median(-left[bad])), float((-left[bad]).max())]
                                                     if bad.any() else [0.0, 0.0]),
                          "left_p5_p50": q(left, (5, 50)), "worst": [float(left.min()), st_[int(np.argmin(left))]]}


def window(s0):
    i = st_.index(s0)
    j0 = kpos[s0]
    return {"vt_bought": s0, "meetings": keys[j0 + 36], "gift": keys[j0 + 60], "joint_move": float(mv[i]),
            "cost_part": CCI[keys[j0 + 60]] / CCI[keys[j0 + 36]] - 1,
            "currency_part": FX[keys[j0 + 36]] / FX[keys[j0 + 60]] - 1,
            "us_shares_2031_2033": float(shares2[i] - 1), "us_shares_2028_2033": float(shares5[i] - 1),
            "contribution": float(cc[i]), "stated_bottom": float(bb[i]), "need_on_contribution": float(cc[i] * mv[i]),
            "kept_half": float(kk[i]), "excess": float(ee[i]), "kept_plus_excess": float(kk[i] + ee[i]),
            "left_kept_plus_excess": float(kk[i] + ee[i] - cc[i] * max(mv[i], 0.0)),
            "left_kept_half": float(kk[i] - cc[i] * max(mv[i], 0.0))}


NAMED = {"2006-08 (the worst, meetings Jul 2006)": "2003-07", "1991-93 (meetings Jan 1991)": "1988-01",
         "2002-04 (meetings Jan 2002)": "1999-01", "2019-21 (meetings Aug 2019)": "2016-08",
         "2009-11 rebound (meetings Mar 2009)": "2006-03"}
rt["named"] = {k: window(v) for k, v in NAMED.items() if v in st_}
worst_i = int(np.argmin(kk + ee - cc * np.maximum(mv, 0)))
rt["worst_window_with_excess"] = window(st_[worst_i])
meet = np.array([keys[kpos[s] + 36] for s in st_])
cur_ = np.array([FX[keys[kpos[s] + 36]] / FX[keys[kpos[s] + 60]] - 1 for s in st_])   # the Taiwan dollar part alone
rt["corr_currency_part_vs_us_shares_2031_2033"] = float(np.corrcoef(cur_, np.log(shares2))[0, 1])
rt["corr_currency_part_vs_us_shares_2028_2033"] = float(np.corrcoef(cur_, np.log(shares5))[0, 1])
for lab, msk in (("meetings_by_dec_2000", meet <= "2000-12"), ("meetings_from_jan_2001", meet >= "2001-01")):
    need_ = cc[msk] * np.maximum(mv[msk], 0)
    rt[lab] = {"windows": int(msk.sum()),
               "kept_half_covers": float((kk[msk] >= need_).mean()),
               "kept_half_plus_excess_covers": float((kk[msk] + ee[msk] >= need_).mean()),
               "fails_with_excess": int((kk[msk] + ee[msk] < need_).sum()),
               "corr_move_vs_us_shares_2031_2033": float(np.corrcoef(mv[msk], np.log(shares2[msk]))[0, 1]),
               "corr_move_vs_us_shares_2028_2033": float(np.corrcoef(mv[msk], np.log(shares5[msk]))[0, 1]),
               "corr_move_vs_kept_plus_excess": float(np.corrcoef(mv[msk], kk[msk] + ee[msk])[0, 1]),
               "corr_currency_part_vs_us_shares_2031_2033": float(np.corrcoef(cur_[msk], np.log(shares2[msk]))[0, 1]),
               "corr_currency_part_vs_us_shares_2028_2033": float(np.corrcoef(cur_[msk], np.log(shares5[msk]))[0, 1])}
jan = np.array([s[5:] == "01" for s in st_])
rt["january_starts_only"] = {
    "windows": int(jan.sum()),
    "kept_half_covers": float((kk[jan] >= cc[jan] * np.maximum(mv[jan], 0)).mean()),
    "kept_half_plus_excess_covers": float((kk[jan] + ee[jan] >= cc[jan] * np.maximum(mv[jan], 0)).mean()),
    "fails_with_excess": [s for s, b in zip(np.array(st_)[jan], (kk[jan] + ee[jan] < cc[jan] * np.maximum(mv[jan], 0)))
                          if b]}
out["real_joint_with_same_months_shares"] = rt

# ---------------------------------------------------------------- 5. independent pairing: every path x every 24-month move
moves24 = np.maximum(S24["moves"], 0.0)
ind = {"moves": int(moves24.size), "note": "each path's pot against every 24-month joint move since 1991, drawn apart "
                                           "from the shares; history since 2001 moved them together (card Q10e, +0.42)"}
for wname in ("house", "history", "joint"):
    w = WORLDS[wname]
    ind[wname] = {}
    for name, pot in (("kept_half", w["kept"]), ("kept_half_plus_excess", w["kept"] + w["excess"])):
        ratio = np.sort(pot / w["contrib"])
        covered = 1 - np.searchsorted(ratio, moves24, side="left") / ratio.size   # share of paths with ratio >= move
        ind[wname][name] = float(covered.mean())
out["independent_pairing_24m"] = ind

# ---------------------------------------------------------------- 6. Keel arithmetic on the register's central figures
CEN = {"contribution": 115_000.0, "stated_bottom": 95_000.0, "kept": 21_347.0, "excess": 8_476.0}
ka = {}
for sname, x in STRESS.items():
    for base in ("contribution", "stated_bottom"):
        need = CEN[base] * x
        ka[f"{sname}_on_{base}"] = {"need": need, "left_kept_half": CEN["kept"] - need,
                                    "left_kept_plus_excess": CEN["kept"] + CEN["excess"] - need}
out["keel_arithmetic_central_register_figures"] = ka

json.dump(out, open(OUTFILE, "w"), indent=1, default=float)


# ---------------------------------------------------------------- print
def m(x):
    return f"${x:,.0f}"


print("joint series", json.dumps(out["joint_series"], default=float))
print("checks", json.dumps(out["checks"], default=float))
for wname in WORLDS:
    for sname in STRESS:
        for base in ("contribution", "stated_bottom"):
            t = fixed[wname][sname][base]
            print(f"{wname:8s} {sname:32s} {base:14s} kept {t['kept_half']['covers']:.4f} "
                  f"(fails {t['kept_half']['fails_count']}, gap p50/p95/max {[round(v) for v in t['kept_half']['gap_when_fails_p50_p95_max']]}, "
                  f"left p5/p50 {[round(v) for v in t['kept_half']['left_p5_p50_p95'][:2]]}) | +excess "
                  f"{t['kept_half_plus_excess']['covers']:.4f} (fails {t['kept_half_plus_excess']['fails_count']}, gap "
                  f"{[round(v) for v in t['kept_half_plus_excess']['gap_when_fails_p50_p95_max']]}, left p5/p50 "
                  f"{[round(v) for v in t['kept_half_plus_excess']['left_p5_p50_p95'][:2]]})")
print("rise covered 19 in 20", json.dumps(out["rise_covered_19_in_20"]), out["rise_covered_central"])
print("real joint", json.dumps({k: v for k, v in rt.items() if k not in ("named",)}, default=float))
for k, v in rt["named"].items():
    print("  named", k, json.dumps(v))
print("independent", json.dumps(ind))
print("keel arithmetic", json.dumps(ka))
