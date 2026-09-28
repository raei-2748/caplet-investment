"""S3_allocation_numbers.py - numbers behind research/insight_v1/wins_now/securities_and_allocation_v0.md (agent S3).

What it does (plain English):
1. Rebuilds the official 2026-09-25 Treasury zero curve exactly as research/verified_2026-09-27/official_curve_pv.py
   does, and checks the $292,264 / 9.90y liability numbers.
2. Works out Laura's plan AFTER the 2028 deposit (ladder value + growth sleeve), so the WInS "mirror" weights come
   from the plan itself, not from a rule of thumb.
3. Builds the WInS allocation tables for three mirror options at $100k, $300k and $500k starting cash, with share
   counts at the 2026-09-25 closing prices and a check against WInS's "no more than twice daily volume" rule.
4. Shows how far markets must move before a rebalancing band is hit, and what the hedge does in WInS if rates move.
5. Values the operating reserve at each 1 January 2033-2042 on today's forward curve (what is left after each payment).

Inputs (status labels):
- competition/official_market_data/daily-treasury-rates_2026-09.csv, row 09/25/2026 (VERIFIED-REPO-FILE).
- Effective durations as of 2026-09-24: IEF 6.86, TLH 11.59, TLT 14.88, SHY 1.79 (ishares.com product pages, read by
  S3 with curl 2026-09-27, VERIFIED-PRIMARY). VGSH 1.9y as of 2026-08-31 (investor.vanguard.com data API, 2026-09-27,
  VERIFIED-PRIMARY). BIL OAD 0.10y as of 2026-09-24 (ssga.com, 2026-09-27, VERIFIED-PRIMARY).
- Closing/market prices 2026-09-25 (IEF 90.00, TLH 93.38, TLT 79.32, SHY 81.21, SGOV 100.66: ishares.com; VT 160.03,
  VTI 379.77, VXUS 86.35, VGSH 57.59: Vanguard price API) and BIL 91.58 (2026-09-24, ssga.com). VERIFIED-PRIMARY.
- 30-day average volume 2026-09-25 (ishares.com): IEF 8,830,020; TLH 1,969,419; TLT 35,945,818; SHY 4,892,873;
  SGOV 22,532,914. BIL prior-day exchange volume 745,610 (ssga.com, 2026-09-24). VERIFIED-PRIMARY. Vanguard pages do
  not publish volume (VT/VGSH volume UNVERIFIED; check in WInS).
- JPM 2026 LTCMA compound returns: AC World 7.00%, U.S. intermediate Treasuries 4.00% (VERIFIED-REPO-FILE, via brief
  section 6 and S2). Used only to grow the 2027 residual for one year (ASSUMPTION: expected returns are realised).
- Nov-15 STRIPS ladder cost $294,387 (S1, VERIFIED-PRIMARY inputs, model output).
- ASSUMPTIONS: growth sleeve 60% equity / 40% short Treasuries (brief section 7 and CLAUDE.md provisional call);
  forward rates are realised when valuing the reserve after 2033; T-bill rate 4.0% for the 47-day wait.
- Sections 8-9 (position-limit contingency) import research/insight_v1/wins_now/S1_hedge_weights.py, which values
  each fund from its actual holdings (S1 snapshot CSVs, VERIFIED-PRIMARY). The 25% single-security cap is Stock-Trak's
  generic default (quoted by A4 in phase_A/wins_week1_guardrails.md; this season's value UNKNOWN). The 3.125%
  Treasury bond due 2041-11-15 (CUSIP 912810QT8) comes from S1's MSPD Table V extract; its price and duration are
  model values on the par curve (ASSUMPTION), not market quotes. IBGA facts (for the note in the .md): net assets
  $73.7m, 30-day average volume 84,912 shares, 9,537 shares traded on 2026-09-25 (ishares.com, VERIFIED-PRIMARY).

- Section 10 (added 2026-09-27 after the S4 red team) prints the ONE pre-chosen capped-hedge rule (IEF at its formula
  weight, TLH one point under the cap, SPTL the rest) for caps from 25% to 43%, option (iii) under a cap, and the
  order sizes. It imports research/insight_v1/scripts/S4_red_team_checks.py for forward-consistent tracking.
  SPTL facts: ssga.com, read 2026-09-27 12:42 UTC (VERIFIED-PRIMARY). Sections 3-4 still print $100k/$500k and
  options (i)/(iii) tables; the .md now uses only the $300,000 figures.

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/S3_allocation_numbers.py
"""
import csv
from datetime import date

import numpy as np

# ---------- 1. Official curve (same method as official_curve_pv.py) ----------
CSV = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
row = next(r for r in csv.DictReader(open(CSV)) if r["Date"] == "09/25/2026")
TEN = {"1 Mo": 1 / 12, "2 Mo": 2 / 12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3, "5 Yr": 5,
       "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
PAR = {t: float(row[k]) for k, t in TEN.items()}
VAL = date(2026, 9, 25)
yf = lambda d: (d - VAL).days / 365.25


def build(par):
    ts = sorted(par); grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts]); df = []
    for y in p:
        c = y / 2; df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]; lz = np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))


def liab_value(anchor, first=2033, shift=0.0):
    f = build({k: v + shift for k, v in PAR.items()}); ta = yf(anchor)
    return sum(50_000 * f(yf(date(y, 1, 1))) / f(ta) for y in range(first, 2043))


def liab_dur(anchor, first=2033):
    up, dn = liab_value(anchor, first, .01), liab_value(anchor, first, -.01)
    return (dn - up) / 2 / liab_value(anchor, first) * 1e4


A27, A28 = date(2027, 1, 1), date(2028, 1, 1)
L27 = liab_value(A27)
print(f"[check] liability at 2027-01-01 ${L27:,.0f} (verified $292,264); duration {liab_dur(A27):.2f}y (verified 9.90)")
print(f"        same payments valued at 2028-01-01 (forward): ${liab_value(A28):,.0f}; duration {liab_dur(A28):.2f}y")

# ---------- 2. Hedge weights from issuer durations ----------
D = {"IEF": 6.86, "TLH": 11.59, "TLT": 14.88}
TARGET = 9.90
w_tlh = (TARGET - D["IEF"]) / (D["TLH"] - D["IEF"])
w_tlt = (TARGET - D["IEF"]) / (D["TLT"] - D["IEF"])
print(f"\n[hedge] IEF/TLH = {1 - w_tlh:.1%} / {w_tlh:.1%}  (duration {(1 - w_tlh) * D['IEF'] + w_tlh * D['TLH']:.2f}y)")
print(f"        IEF/TLT = {1 - w_tlt:.1%} / {w_tlt:.1%}  (fallback)")
for tgt in (TARGET, liab_dur(A28)):
    w = (tgt - D["IEF"]) / (D["TLH"] - D["IEF"])
    print(f"        if the duration target were {tgt:.2f}y: IEF {1 - w:.1%} / TLH {w:.1%}")

# ---------- 3. The plan after the 2028 deposit ----------
print("\n[plan at 2028-01-01] ladder value vs growth sleeve (ASSUMPTION: 2027 residual earns the sleeve's JPM rate)")
plan = {}
for label, cost in (("exact-date zeros", L27), ("Nov-15 STRIPS ladder", 294_387)):
    ladder28 = liab_value(A28)                       # a ladder that matches the payments is worth their value
    for eq in (0.5, 0.6, 0.7):
        r = eq * 0.0700 + (1 - eq) * 0.0400          # JPM AC World / intermediate Treasuries, compound
        sleeve = (300_000 - cost) * (1 + r) + 150_000
        tot = ladder28 + sleeve
        plan[(label, eq)] = (ladder28 / tot, eq * sleeve / tot, (1 - eq) * sleeve / tot)
        print(f"  {label:<22} equity {eq:.0%} of sleeve: total ${tot:,.0f}; hedge {ladder28 / tot:.1%}, "
              f"equity {eq * sleeve / tot:.1%}, sleeve bonds {(1 - eq) * sleeve / tot:.1%}")

# ---------- 4. WInS allocation tables ----------
PX = {"IEF": 90.00, "TLH": 93.38, "TLT": 79.32, "VT": 160.03, "VGSH": 57.59, "BIL": 91.58, "SHY": 81.21,
      "SGOV": 100.66, "VTI": 379.77, "VXUS": 86.35}
VOL = {"IEF": 8_830_020, "TLH": 1_969_419, "TLT": 35_945_818, "SHY": 4_892_873, "SGOV": 22_532_914, "BIL": 745_610}
hedge_pct = 66.0
OPTIONS = {
    "(i) brief's mirror 65/35": {"IEF": 65 * (1 - w_tlh), "TLH": 65 * w_tlh, "VT": 34.0, "CASH": 1.0},
    "(ii) plan-consistent (recommended)": {"IEF": hedge_pct * (1 - w_tlh), "TLH": hedge_pct * w_tlh, "VT": 20.5,
                                           "VGSH": 12.5, "CASH": 1.0},
    "(iii) literal Jan-2027 book": {"IEF": 97.5 * (1 - w_tlh), "TLH": 97.5 * w_tlh, "VT": 1.5, "CASH": 1.0},
}
for name, wts in OPTIONS.items():
    assert abs(sum(wts.values()) - 100) < 1e-9, name
    bond_dur = sum(wts.get(k, 0) * d for k, d in {**D, "VGSH": 1.9}.items()) / 100
    print(f"\n[WInS] {name}: weights {({k: round(v, 1) for k, v in wts.items()})}; "
          f"portfolio duration {bond_dur:.2f}y")
    for cash in (100_000, 300_000, 500_000):
        cells = []
        for k, v in wts.items():
            dollars = cash * v / 100
            if k == "CASH":
                cells.append(f"{k} ${dollars:,.0f}")
            else:
                sh = int(dollars // PX[k])
                cap = f", {sh / (2 * VOL[k]):.3%} of 2x vol cap" if k in VOL else ""
                cells.append(f"{k} ${dollars:,.0f} (~{sh:,} sh{cap})")
        print(f"   ${cash:,}: " + "; ".join(cells))

# Day-1 version of option (ii): the floor-proxy money waits in BIL until the team's week-2 decision
print("\n[day 1, option (ii)] floor-proxy money parked in BIL until the week-2 decision:")
for cash in (100_000, 300_000, 500_000):
    b = cash * 0.125
    print(f"   ${cash:,}: BIL ${b:,.0f} (~{int(b // PX['BIL']):,} sh) then VGSH ~{int(b // PX['VGSH']):,} sh")

# ---------- 5. Bands and hedge behaviour in WInS ----------
print("\n[bands] equity move (bonds flat) that pushes VT outside 55-65% of the growth sleeve (target 60%):")
for band in (0.55, 0.65):
    # 0.6(1+r) / (0.6(1+r) + 0.4) = band  ->  1+r = band*0.4 / (0.6*(1-band))
    r = band * 0.4 / (0.6 * (1 - band)) - 1
    print(f"   VT share {band:.0%}: equity move {r:+.1%}")
h = 300_000 * hedge_pct / 100
print(f"[hedge in WInS] ${h:,.0f} hedge at 9.90y: +50bp ~ -${h * 9.90 * .005:,.0f}; +100bp ~ -${h * 9.90 * .01:,.0f}; "
      f"-100bp ~ +${h * 9.90 * .01:,.0f} (first-order)")
for dd in (0.25,):
    print(f"   a {dd}y duration gap on ${h:,.0f} = ${h * dd * .01:,.0f} per 100bp parallel move")
# what a rate move does to the IEF/TLH weights: illustrative duration drift used in the file
for di, dt in ((6.82, 11.40), (6.90, 11.78)):
    w = (TARGET - di) / (dt - di)
    held = (1 - w_tlh) * di + w_tlh * dt
    print(f"   if durations became IEF {di}/TLH {dt}: new TLH weight {w:.1%}; unrebalanced hedge duration {held:.2f}y")

# ---------- 6. Operating reserve after 2033 (today's forwards realised; ASSUMPTION) ----------
print("\n[reserve] value at each 1 Jan before that day's payment, on today's forward curve:")
f = build(PAR)
for y in range(2033, 2043):
    n = 2043 - y
    v = liab_value(date(y, 1, 1), first=y)
    d = liab_dur(date(y, 1, 1), first=y + 1) if n > 1 else 0.0      # rungs still held after today's payment
    print(f"   {y}-01-01: {n:>2} payments left, face ${n * 50_000:,}; value ${v:,.0f}; "
          f"after paying ${v - 50_000:,.0f}; duration of the rungs still held {d:.2f}y")
print(f"   T-bill interest on a Nov-15 rung waiting 47 days at 4.0% (ASSUMPTION): ${50_000 * .04 * 47 / 365:,.0f}")
print(f"   2031 floor: a 2-year note at the 2026-09-25 2y par yield 4.81% grows by x{(1 + .0481 / 2) ** 4:.4f} "
      f"(semiannual) over two years")

# ---------- 7. Sector fallback at $300k ----------
SECT = {"XLK": 39, "XLF": 12, "XLC": 10, "XLV": 9, "XLY": 9, "XLI": 8, "XLP": 4, "XLE": 3, "XLU": 2, "XLB": 2,
        "XLRE/VNQ": 2}
eq = 300_000 * 0.205
print(f"\n[sector fallback] equity ${eq:,.0f}: US 62% ${eq * .62:,.0f} in sector SPDRs, VXUS 38% ${eq * .38:,.0f}")
print("   " + "; ".join(f"{k} ${eq * .62 * v / 100:,.0f}" for k, v in SECT.items()))
print(f"   commissions: 12 buys x $25 = $300; smallest position ${eq * .62 * .02:,.0f} "
      f"(commission = {25 / (eq * .62 * .02):.1%} of it)")


# ---------- 8. If WInS caps any single security at 25% of the portfolio (Stock-Trak default; season value UNKNOWN) ----------
# Source of the 25% default: Stock-Trak Wharton portal FAQ, quoted in research/insight_v1/phase_A/wins_week1_guardrails.md
# (VERIFIED-PRIMARY by A4, generic platform page, not season-specific). Reuses S1's holdings-based model.
def capped_hedge_search(cap_total=25.0, hedge_share=66.0, top=6):
    import itertools
    import sys
    from scipy.optimize import minimize
    sys.path.insert(0, "research/insight_v1/wins_now")
    import S1_hedge_weights as s1
    cap = cap_total / hedge_share                                 # cap as a share of the hedge sleeve
    pool = ["IEF", "TLH", "TLT", "SPTI", "SPTL", "VGIT", "VGLT", "IEI", "GOVT", "IBTQ", "IBTR", "IBGA"]
    twists = [k for k in s1.SCEN if "parallel" not in k]
    res = []
    for combo in itertools.combinations(pool, 3):
        D_ = np.array([s1.ISSUER_DUR[n][0] for n in combo])
        R_ = np.array([[s1.R_S[n][k] for n in combo] for k in twists])
        dl = np.array([s1.L_S[k] - s1.L0 for k in twists])
        obj = lambda w: ((s1.L0 * R_ @ w - dl) ** 2).sum()
        cons = [{"type": "eq", "fun": lambda w: w.sum() - 1}, {"type": "eq", "fun": lambda w, D_=D_: w @ D_ - TARGET}]
        best = None
        for x0 in ([1 / 3] * 3, [.3, .35, .35], [.35, .3, .35], [.35, .35, .3]):
            r = minimize(obj, np.array(x0), bounds=[(0, cap)] * 3, constraints=cons, method="SLSQP")
            if r.success and abs(r.x.sum() - 1) < 1e-6 and abs(r.x @ D_ - TARGET) < 1e-4 and \
                    (best is None or r.fun < best.fun):
                best = r
        if best is not None:
            w = dict(zip(combo, best.x))
            te, twist, par_, fee = s1.summary(w)
            res.append((twist, par_, fee, w))
    res.sort(key=lambda x: x[0])
    print(f"\n[cap {cap_total:.0f}% per security] best 3-fund hedges (each <= {cap:.1%} of a {hedge_share:.0f}% hedge), "
          f"duration {TARGET}y:")
    for twist, par_, fee, w in res[:top]:
        print("   " + " / ".join(f"{n} {v:.1%} (total {v * hedge_share:.1f}%)" for n, v in w.items()) +
              f": worst twist ${twist:,.0f}, +/-100bp worst ${par_:,.0f}, fee {fee:.3f}%")
    liquid = [r for r in res if not ({"IBTQ", "IBTR", "IBGA"} & set(r[3]))]
    print("   best using only large, liquid funds (no iBonds):")
    for twist, par_, fee, w in liquid[:3]:
        print("   " + " / ".join(f"{n} {v:.1%} (total {v * hedge_share:.1f}%)" for n, v in w.items()) +
              f": worst twist ${twist:,.0f}, +/-100bp worst ${par_:,.0f}, fee {fee:.3f}%")
    # reference: uncapped IEF/TLH and a two-issuer split (half IEF/TLH, half SPTI/SPTL)
    for label, w in (("uncapped IEF/TLH", s1.two_fund("IEF", "TLH")),
                     ("half IEF/TLH + half SPTI/SPTL",
                      {**{k: v / 2 for k, v in s1.two_fund("IEF", "TLH").items()},
                       **{k: v / 2 for k, v in s1.two_fund("SPTI", "SPTL").items()}})):
        te, twist, par_, fee = s1.summary(w)
        print(f"   ref {label}: " + " / ".join(f"{n} {v:.1%} (total {v * hedge_share:.1f}%)" for n, v in w.items())
              + f": worst twist ${twist:,.0f}, +/-100bp worst ${par_:,.0f}")


capped_hedge_search()


# ---------- 9. Ready-to-use capped hedge mixes (used in the .md, section D.1b) ----------
def capped_variants(work_cap=24.0, hedge_share=66.0):
    """Ready-to-use hedge mixes when a single-security cap of 25% applies. Each capped fund is held at 24% of the
    total (1-point buffer, ASSUMPTION: the cap is checked at the fill price). Weights solve duration = 9.90 exactly."""
    import sys
    sys.path.insert(0, "research/insight_v1/wins_now")
    import S1_hedge_weights as s1
    b = work_cap / hedge_share
    out = []
    # V1: IEF + TLH at the cap + one U.S. Treasury bond (ASSUMPTION: bonds have their own, higher limit, as in the
    # 2024-25 Session Rules screenshot quoted by A4). 3.125% bond due 2041-11-15, CUSIP 912810QT8 (S1, MSPD Table V).
    s1.FUND_CF["UST41"] = s1.cashflows(100.0, 3.125, "2041-11-15")
    v0 = s1.fund_value("UST41", s1.PAR)
    d_b = s1.eff_dur(lambda p: s1.fund_value("UST41", p))
    s1.R_S["UST41"] = {k: s1.fund_value("UST41", s1.shifted(fn)) / v0 - 1 for k, fn in s1.SCEN.items()}
    a = (d_b * (1 - b) - (TARGET - 11.59 * b)) / (d_b - 6.86)
    out.append((f"IEF + TLH + UST 3.125% 2041-11-15 (model dur {d_b:.2f}y, model price {v0:.2f})",
                {"IEF": a, "TLH": b, "UST41": 1 - a - b}, {"IEF": 6.86, "TLH": 11.59, "UST41": d_b}))
    # V2: ETFs only: IEF and TLH at the cap, the rest SPTL + SPTI solving the duration
    rest = 1 - 2 * b
    x = (TARGET - b * (6.86 + 11.59) - rest * 4.78) / (13.65 - 4.78)
    out.append(("IEF + TLH + SPTL + SPTI (ETFs only)", {"IEF": b, "TLH": b, "SPTL": x, "SPTI": rest - x},
                {"IEF": 6.86, "TLH": 11.59, "SPTL": 13.65, "SPTI": 4.78}))
    # V3: TLH missing as well: split each leg across two issuers (SPDR and Vanguard pairs, half each)
    p1, p2 = s1.two_fund("SPTI", "SPTL"), s1.two_fund("VGIT", "VGLT")
    out.append(("TLH missing: half SPTI/SPTL + half VGIT/VGLT", {**{k: v / 2 for k, v in p1.items()},
                                                                  **{k: v / 2 for k, v in p2.items()}},
                {"SPTI": 4.78, "SPTL": 13.65, "VGIT": 4.9, "VGLT": 13.5}))
    print(f"\n[cap variants] each capped position held at {work_cap:.0f}% of the total; hedge = {hedge_share:.0f}%:")
    for label, w, dd in out:
        te, twist, par_, _ = s1.summary(w)
        dur = sum(w[k] * dd[k] for k in w)
        print(f"   {label}: " + " / ".join(f"{k} {v * hedge_share:.1f}%" for k, v in w.items()) +
              f"; duration {dur:.2f}y; worst 50bp twist ${twist:,.0f}; +/-100bp worst ${par_:,.0f}; "
              f"largest single position {max(w.values()) * hedge_share:.1f}%")


capped_variants()


# ---------- 10. Revision after S4 red team (2026-09-27): ONE pre-chosen capped rule, measured forward-consistently ----------
# Rule (S4 finding 3): IEF stays at its formula weight (23.6% of the total, under a 24% working cap); TLH is held one
# point under the cap; SPTL (alternate VGLT) takes the rest of the 66% hedge. Tracking uses S4's forward-consistent
# method (fund forward value vs liability forward value; research/insight_v1/scripts/S4_red_team_checks.py), which
# replaces S1's mixed spot/forward method (S4 finding 8). SPTL is modelled with VGLT holdings (S1 ASSUMPTION).
# SPTL issuer facts re-read by S3 on ssga.com 2026-09-27 12:42 UTC: OAD 13.65y (Sep 24), 0.03% gross, 110 holdings,
# AUM $10,949.50M (Sep 24), prior-day exchange volume 1,088,651 (VERIFIED-PRIMARY).
def capped_rule_table():
    import sys
    sys.path.insert(0, "research/insight_v1/wins_now")
    sys.path.insert(0, "research/insight_v1/scripts")
    import S1_hedge_weights as s1
    from S4_red_team_checks import fwd_track, worst
    dur = {"IEF": 6.86, "TLH": 11.59, "SPTL": 13.65, "TLT": 14.88, "VGIT": 4.9, "VGLT": 13.5}

    def show(label, tot):                                     # tot: share of the TOTAL portfolio, in %
        h = sum(tot.values())
        w = {k: v / h for k, v in tot.items()}
        tw, pa = worst(fwd_track(w))
        d = sum(w[k] * dur[k] for k in w)
        print(f"   {label}: " + " / ".join(f"{k} {v:.1f}" for k, v in tot.items()) +
              f" (hedge {h:.1f}%) | issuer duration {d:.2f}y | worst 50bp twist ${tw:,.0f} "
              f"({tw / s1.L0:.2%} of the hedge) | worst +/-100bp ${pa:,.0f}")

    print("\n[S3 v1 capped rule, option (ii), hedge 66% of the total; forward-consistent tracking]")
    ief = 66.0 * (1 - w_tlh)
    for cap in (None, 43, 40, 35, 30, 25):
        tlh = 66.0 * w_tlh if cap is None or cap - 1 >= 66.0 * w_tlh else cap - 1
        mix = {"IEF": ief, "TLH": tlh}
        if 66.0 - ief - tlh > 1e-9:
            mix["SPTL"] = 66.0 - ief - tlh
        show(f"cap {'none' if cap is None else f'{cap}%'}", mix)
    show("alternate VGLT at a 25% cap", {"IEF": ief, "TLH": 24.0, "VGLT": 66.0 - ief - 24.0})
    show("if TLH is missing, no cap: IEF/TLT", {"IEF": 66.0 * (1 - w_tlt), "TLT": 66.0 * w_tlt})
    # TLH missing AND a 25% cap: IEF and SPTL at 24 each; the remaining 18 split VGIT/VGLT to hit 9.90 (issuer)
    r18 = 66.0 - 48.0
    xg = (TARGET * 66 - 24 * (dur["IEF"] + dur["SPTL"]) - r18 * dur["VGLT"]) / (dur["VGIT"] - dur["VGLT"])
    show("TLH missing, 25% cap", {"IEF": 24.0, "SPTL": 24.0, "VGIT": xg, "VGLT": r18 - xg})

    # Option (iii): the literal Jan-2027 book. 2027 leftover in T-bills (S4 finding 13) -> WInS: hedge 98%, cash 2%.
    print("\n[option (iii), hedge 98% of the total (ladder $294,387 of $300,000), cash 2%, VT 0%]")
    show("no cap", {"IEF": 98 * (1 - w_tlh), "TLH": 98 * w_tlh})
    # 25% cap: IEF, TLH, SPTL at 24 each; the remaining 26 split VGIT/VGLT to hit 9.90 on issuer durations
    rest = 98 - 72
    x = (TARGET * 98 - 24 * (dur["IEF"] + dur["TLH"] + dur["SPTL"]) - rest * dur["VGLT"]) / (dur["VGIT"] - dur["VGLT"])
    show("25% cap (five Treasury funds)", {"IEF": 24.0, "TLH": 24.0, "SPTL": 24.0, "VGIT": x, "VGLT": rest - x})

    # Share counts for the (ii) orders at 2026-09-25 closes (SPTL close $24.27, ssga.com, VERIFIED-PRIMARY)
    px = {**PX, "SPTL": 24.27}
    print("\n[orders at $300,000, option (ii)] approximate shares at 2026-09-25 closes (recompute on the trade date):")
    for label, mix in (("no cap", {"IEF": ief, "TLH": 66.0 * w_tlh, "VT": 20.5, "VGSH": 12.5}),
                       ("25% cap", {"IEF": ief, "TLH": 24.0, "SPTL": 66.0 - ief - 24.0, "VT": 20.5, "VGSH": 12.5})):
        print(f"   {label}: " + "; ".join(f"{k} {v:.1f}% ${3000 * v:,.0f} ~{int(3000 * v // px[k]):,} sh"
                                          for k, v in mix.items()))


capped_rule_table()
