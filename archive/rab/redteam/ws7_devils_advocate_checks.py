"""WS7 red team (devil's advocate on the decision memos): the four numeric checks behind the critique.

RAB Kit, 30 Sep 2026 (Sydney). AI-generated research (Claude Code) for Team Caplet; no deliverable text; MODEL where
marked. Read-only: imports the WS2 model code (rab/models/) and reads committed files; writes nothing except stdout.
Nothing here is in numbers.yaml; every figure is a red-team check, to be re-derived by WS1/WS2 before any use.

Run from anywhere:
    /Users/ray/Research/rab-ws/.venv/bin/python rab/redteam/ws7_devils_advocate_checks.py

[1] D6 rule (M4_SPEC s5, PR-4/PR-5) with Laura's kept money net of the Book L coupon-reinvestment shortfall
    (numbers.yaml reinvest.rung.*: sum of rung gaps below $50,000, discounted to 1 Jan 2033 at the scenario rate;
    today's-yield-minus-2-points gaps discounted at 3%). M4 defines K = phi F + B5 - G with no ladder term.
[2] Fund choice: how much of gold/REIT's narrower spread comes from a better bad case vs a lower good case.
[3] WInS bond list vs the Treasury's own list (MSPD Table V, 31 Aug 2026): the inference that WInS "probably"
    lists the 1.375% Nov-2040 bond.
[4] IPS body word count (30 Sep snapshot) vs the 500-word limit.
"""
import csv
import collections
import json
import os
import sys

import numpy as np
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "rab", "models"))
import ws2_common as C  # noqa: E402
import m3_branch as M3  # noqa: E402
import m4_cap as M4  # noqa: E402

N = yaml.safe_load(open(os.path.join(ROOT, "rab", "numbers.yaml")))["numbers"]

# ---------------------------------------------------------------- [1]
rungs = sorted((v["value"] for k, v in N.items() if k.startswith("reinvest.rung.")), key=lambda x: x["pays"])


def shortfall(key, rate):
    tot = pv = 0.0
    for i, r in enumerate(rungs):          # rungs pay 1 Jan 2033 ... 1 Jan 2042; i = years after 1 Jan 2033
        gap = max(0.0, 50_000 - r[key])
        tot += gap
        pv += gap / (1 + rate) ** i
    return tot, pv


SCEN = {"none (M4 as run)": (0.0, 0.0), "own yield - 2pp": shortfall("at_own_minus_2pp", 0.03),
        "2%": shortfall("at_2pct", 0.02), "0%": shortfall("at_0pct", 0.0)}
print("[1] D6 rule with kept money net of the Book L coupon shortfall (MODEL)")
for k, (tot, pv) in SCEN.items():
    print(f"    scenario {k:16s}: rung gaps ${tot:,.0f}, value on 1 Jan 2033 ${pv:,.0f}")
inp = C.inputs()
F, y5 = inp["F"], inp["y5"]
phi, _, _ = M4.phi_draws(y5)
A = 145_000.0                                  # announced floor (M4 PR-3 result, D_range_confidence_2031.md)
S = np.round(np.arange(0, 1.0001, 0.01), 2)
for m in M3.DECISION:
    o = C.rule(M3.paths(m), inp["B0"], F)
    for k, (tot, pv) in SCEN.items():
        best, row = None, {}
        for s in S:
            q = M4.measures(o, phi, F, s, low=A)
            kn = q["_K"] - pv
            pf = float(np.mean(kn >= M4.KAPPA * q["_G"]))
            if s in (0.0, 0.5):
                row[s] = (pf, float(np.percentile(kn, 5)))
            if q["P_D"] <= M4.PD_MAX and pf >= M4.CONF:
                best = s
        print(f"    {m:6s} {k:16s} largest passing share {best} | P(kept >= 10% of gift): share 1/2 "
              f"{row[0.5][0]:.1%}, share 0 {row[0.0][0]:.1%} | kept, 1-in-20 case, share 1/2 ${row[0.5][1]:,.0f}")

# ---------------------------------------------------------------- [2]
print("\n[2] Fund choice: gold/REIT (A4) against VT (A0), gift percentiles (rab/results/M6/fund_alternatives.csv)")
fa = list(csv.DictReader(open(os.path.join(ROOT, "rab", "results", "M6", "fund_alternatives.csv"))))
for lens in ("MC_JPM", "history_1928_2020", "etf_2011_2020"):
    a0 = next(r for r in fa if r["fund"] == "A0" and r["lens"] == lens)
    a4 = next(r for r in fa if r["fund"] == "A4" and r["lens"] == lens)
    d5 = float(a4["gift_p5"]) - float(a0["gift_p5"])
    d95 = float(a4["gift_p95"]) - float(a0["gift_p95"])
    d33 = float(a4["T33_p50"]) - float(a0["T33_p50"])
    print(f"    {lens:18s}: bad case (p5) {d5:+,.0f}; good case (p95) {d95:+,.0f}; spread narrows {d5 - d95:,.0f}, "
          f"of which the lower good case is {-d95 / (d5 - d95):.0%}; median total 2033 money {d33:+,.0f}")

# ---------------------------------------------------------------- [3]
print("\n[3] WInS bond list vs MSPD Table V (31 Aug 2026)")
d = json.load(open(os.path.join(ROOT, "rab", "trades", "data", "mspd_table5_2026-08-31.json")))["data"]
cls = collections.Counter(r["security_class1_desc"] for r in d)
bonds = [r for r in d if r["security_class1_desc"] == "Treasury Bonds" and r["maturity_date"] not in (None, "null")]
gap = [r for r in bonds if "2031-02-15" < r["maturity_date"] < "2036-02-15"]
win = [r for r in bonds if "2036-01-01" <= r["maturity_date"] < "2043-01-01"]
low = [(r["interest_rate_pct"], r["maturity_date"]) for r in win if float(r["interest_rate_pct"]) < 3]
print(f"    MSPD classes: {dict(cls)}")
print(f"    Treasury Bonds outstanding: {len(bonds)}; maturing strictly between 15 Feb 2031 and 15 Feb 2036: {len(gap)}")
print(f"    Treasury Bonds maturing 2036-2042: {len(win)}; of which coupon < 3%: {len(low)} {low}")
print("    WInS drop-down: 43 US Treasuries including matured ones (tab WInS Notes, premortem PM-01); 7 of the 2036-2042 "
      "bonds were seen with prices (tab Book L, wins_prices_2026-09-28.csv)")

# ---------------------------------------------------------------- [4]
txt = open(os.path.join(ROOT, "rab", "trades", "data", "ips_doc_text_2026-09-30.txt")).read()
body = txt[txt.index("This policy governs"):]
print(f"\n[4] IPS body words (30 Sep snapshot): {len(body.split())} of 500")
