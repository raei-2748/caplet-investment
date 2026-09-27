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
