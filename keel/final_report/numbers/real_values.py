"""Real values of the payments and the 2031 range (Keel, Mon 9 Nov 2026). MODEL. Inputs: numbers/inflation_inputs.json.

python3 -I keel/final_report/numbers/real_values.py  -> prints and writes results_real_2026-11-10.json
Tue 10 Nov: the range is read from results_2026-11-10.json (the call's central stated range under the Q19 rule) instead
of the fixed $110,000-$135,000; results_real_2026-11-06.json is kept.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
j = json.load(open(HERE / "inflation_inputs.json"))
_reg = json.load(open(HERE / "results_2026-11-10.json"))
_cr = _reg["plan"][_reg["stamp"]["design"]]["central_rule"]
LO, HI = _cr["bottom"], _cr["top"]
us, tc = j["us"], j["taiwan_construction"]
fx = j["usdtwd"]
out = {}
for lab in ("low", "central", "high"):
    r = us[lab]
    pays = {y: 50_000 / (1 + r) ** (y - 2027) for y in range(2033, 2043)}
    out[f"us_{lab}"] = {"rate": r, "payments_2027_dollars": pays, "ten_total": sum(pays.values()),
                        "range": [LO, HI], "range_in_2027_dollars": [LO / (1 + r) ** 6, HI / (1 + r) ** 6]}
# the facility contribution in Taiwan building terms: NT$ at today's rate, deflated by construction costs 2026->2033
yrs = 2033 - 2026 - (10 / 12)          # from the latest index month (Sep 2026) to Jan 2033, about 6.25 years
for lab in ("low", "central", "high"):
    g = tc[lab]
    out[f"tw_construction_{lab}"] = {"rate": g, "years": yrs,
        "range_ntd_today_costs": [v * fx["latest"] / (1 + g) ** yrs for v in (LO, HI)]}
out["fx"] = {"latest": fx["latest"], "strong_twd_10y": min(fx["range_10y"]),
             "extra_usd_for_same_ntd_at_strong_twd": [v * (fx["latest"] / min(fx["range_10y"]) - 1) for v in (LO, HI)]}
json.dump(out, open(HERE / "results_real_2026-11-10.json", "w"), indent=1)
k = lambda v: f"${v:,.0f}"
for lab in ("low", "central", "high"):
    o = out[f"us_{lab}"]
    print("US", lab, o["rate"], "2033", k(o["payments_2027_dollars"][2033]), "2042", k(o["payments_2027_dollars"][2042]),
          "ten", k(o["ten_total"]), "range", [k(x) for x in o["range_in_2027_dollars"]])
for lab in ("low", "central", "high"):
    o = out[f"tw_construction_{lab}"]
    print("TW build", lab, o["rate"], [f"NT${x/1e6:.2f}m" for x in o["range_ntd_today_costs"]])
print("fx", out["fx"])
