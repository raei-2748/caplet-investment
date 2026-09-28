"""Route Phase C survivors to Phase D specialists (main-loop utility).

Each specialist takes at most CAP questions (highest skeptic priority first); the rest go to an overflow researcher
(D11 for the markets side D1-D4/D10, D12 for the client side D5-D9). Prints four workflow argument objects.
Run from repo root: .venv/bin/python research/insight_v1/scripts/route_phase_D.py > /tmp/phase_D_args.json
"""
import json
from collections import defaultdict

CAP = 12
S = {
    "D1": ("rates", "Rates & Fixed-Income Analyst", "Covers the Treasury curve, the ladder and STRIPS, the pre-funding gap to January 2027, reinvestment, Treasury credit, and the WInS hedge funds."),
    "D2": ("equity_ai", "Equity & AI-Concentration Analyst", "Covers index concentration, valuations, AI and mega-cap exposure, and what a broad fund really owns in 2026."),
    "D3": ("quant", "Quant Modeler", "Covers the simulation model, confidence statements, the 2031 range and stress scenarios."),
    "D4": ("taiwan_fx", "Taiwan, FX & Geopolitics Analyst", "Covers TWD costs against USD payments, construction inflation, Taiwan Strait contingencies and how the co-sponsor range should be quoted."),
    "D5": ("cosponsors", "Philanthropy & Co-sponsor Analyst", "Covers how co-funders assess a founder's pledge, the 2031 range and its confidence wording, and what the fundraising excerpt must contain (checklist only)."),
    "D6": ("behavioural", "Client Psychologist / Behavioural Finance", "Covers what Laura will feel and do in a bad year, pre-commitment rules, risk willingness vs ability, and what earns her trust."),
    "D7": ("wharton_intent", "Wharton Intent Historian", "Covers the client trend, the official Wharton framing, past case designs vs this one, and what semifinal readers reward."),
    "D8": ("practice", "Professional-Practice Benchmarker", "Maps our strategy against named industry frameworks (LDI, goals-based wealth management, pension and endowment practice, CFA Asset Manager Code), with sources."),
    "D9": ("communication", "Communication Analyst", "Covers whether each idea can be said in plain English within the 50-word pitch and 500-word IPS, jargon and overclaim risks, note and reflection specs, and the Final Report narrative and visuals."),
    "D10": ("compliance", "Compliance Officer", "Covers the WInS rules, the AI policy, format rules, eligibility and anything disqualifying."),
}
D3_EXTRA = """
EXTRA MANDATE (D3, in addition to your questions): build research/insight_v1/scripts/strategy_mc_v2.py by extending research/verified_2026-09-27/strategy_mc.py. Keep the verified base case reproducible: the same seed and inputs must give $159k/$207k/$273k. Add, each switchable and labelled ASSUMPTION or VERIFIED:
(a) rate risk between Sept 2026 and the Jan 2027 purchase, using the "longest rungs first, top up from 2028" rule and the real Nov-15 STRIPS ladder ($294,387 on the 2026-09-25 curve; research/insight_v1/wins_now/S1_treasury_sleeve.md);
(b) 2028 deposit scenarios: full, smaller ($75k), late (arrives 2029), missing, and correlated with 2027 equity returns, with the correlation stated as an assumption and a sensitivity range;
(c) fees: fund expense on the sleeve, plus advisory-fee scenarios of 0 / 0.5% / 1.0% on sleeve and/or ladder;
(d) global equity (JPM AC World 7.00% compound, 8.28% arithmetic, 16.78% vol) vs U.S. large cap, and short-Treasury sleeve bonds as held in WInS;
(e) fat tails (Student-t) as a robustness check;
(f) the 2031 co-sponsor range: floor (bought in a 2-year Treasury) and upper bound, for several floor shares and upper-bound rules. For each, report P(2033 contribution falls within the range), P(below floor) (0 by construction if bought) and P(above upper). The case asks for confidence that the contribution will fall "within that range", so both ends matter;
(g) facility-contribution rule after the reserve: how much of the remaining surplus to contribute vs keep as flexibility, with the distribution of the contribution and of the flexibility money kept.
Print clear tables and write research/insight_v1/phase_D/D3_model_v2_results.md, covering: what each switch changes, the headline numbers, and which numbers are robust vs assumption-driven. Keep the model simple enough to explain in a paragraph."""


def main():
    surv = json.load(open("research/insight_v1/phase_C/survivors.json"))
    by = defaultdict(list)
    for r in surv:
        by[r["domain_tag"]].append(r)
    route = defaultdict(list)
    for tag, rs in by.items():
        rs.sort(key=lambda r: -r["priority"])
        route[tag] += [r["mid"] for r in rs[:CAP]]
        over = "D11" if tag in ("D1", "D2", "D3", "D4", "D10") else "D12"
        route[over] += [r["mid"] for r in rs[CAP:]]
    spec = lambda code, mids, effort="high": {  # noqa: E731
        "code": code, "slug": S[code][0], "name": S[code][1], "scope": S[code][2], "mids": mids, "effort": effort,
        **({"extra": D3_EXTRA} if code == "D3" else {})}
    over = lambda code, side, mids: {  # noqa: E731
        "code": code, "slug": "overflow_" + side, "name": f"Overflow Researcher ({side} side)",
        "scope": "You take the lower-priority surviving questions that did not fit in the specialists' queues. Research them with the same standard.",
        "mids": mids, "effort": "high"}
    groups = [
        {"slug": "rates_quant", "name": "rates and quant", "auditor": "AX1", "codes": ["D1", "D3", "D11"],
         "specialists": [spec("D1", route["D1"]), spec("D3", route["D3"], "max")]},
        {"slug": "markets_rules", "name": "equity, Taiwan/FX and compliance", "auditor": "AX2", "codes": ["D2", "D4", "D10"],
         "specialists": [spec("D2", route["D2"]), spec("D4", route["D4"]), spec("D10", route["D10"])]},
        {"slug": "client_cosponsors", "name": "client psychology and co-sponsors", "auditor": "AY1", "codes": ["D5", "D6", "D12"],
         "specialists": [spec("D5", route["D5"]), spec("D6", route["D6"], "xhigh")]},
        {"slug": "judges_practice_comms", "name": "Wharton intent, practice benchmark and communication", "auditor": "AY2", "codes": ["D7", "D8", "D9"],
         "specialists": [spec("D7", route["D7"]), spec("D8", route["D8"]), spec("D9", route["D9"])]},
    ]
    if route["D11"]:
        groups[0]["specialists"].append(over("D11", "markets", route["D11"]))
    if route["D12"]:
        groups[2]["specialists"].append(over("D12", "client", route["D12"]))
    for g in groups:
        g["specialists"] = [s for s in g["specialists"] if s["mids"]]
    print(json.dumps(groups))
    import sys
    print({k: len(v) for k, v in route.items()}, file=sys.stderr)


if __name__ == "__main__":
    main()
