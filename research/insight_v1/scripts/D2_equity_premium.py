"""D2 (Equity & AI-Concentration Analyst), question M030: how much extra return does the growth sleeve's equity
really expect over simply buying Treasuries for the same horizon, and does that move sleeve equity from 60% to 40-50%?

Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D2_equity_premium.py

INPUTS (status labels)
- Official Treasury par curve 2026-09-25, competition/official_market_data/daily-treasury-rates_2026-09.csv
  (VERIFIED-REPO-FILE). Bootstrapped exactly as research/verified_2026-09-27/official_curve_pv.py (method reused).
- J.P. Morgan 2026 LTCMA, competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf p.2 (VERIFIED-REPO-FILE,
  data as of 2025-09-30): U.S. large cap 6.70% compound / 7.94% arithmetic / 16.47% vol; AC World 7.00 / 8.28 / 16.78;
  correlation AC World vs U.S. intermediate Treasuries 0.00.
- Vanguard VCMM, 10-year annualised (geometric) forecasts from the June 30, 2026 run, page dated July 22, 2026
  (VERIFIED-PRIMARY, https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html,
  read 2026-09-27): U.S. equities 4.2%-6.2%; developed ex-U.S. 4.5%-6.5%; emerging markets 2%-4%.
- VT regional mix: 62.3% U.S. / 37.7% non-U.S. (Vanguard VT fact sheet 2026-08-31 via S3 ticket, VERIFIED-PRIMARY);
  the developed/emerging split of the non-U.S. part (75/25) is an ASSUMPTION (roughly FTSE ex-US All Cap).
- FactSet Earnings Insight, 25 Sep 2026 (VERIFIED-PRIMARY): S&P 500 forward 12-month P/E 19.2.
- Shiller CAPE 41.48 on 2026-09-25 (multpl.com, SECONDARY-READ; Shiller's own file not read).
- 10-year breakeven inflation 2.34% (F-009, VERIFIED-PRIMARY derived); used only for a crude CAPE yardstick.
- Plan structure (brief section 7, ASSUMPTION = current provisional plan): ladder $292,264 bought 2027-01-01; sleeve
  = $7,736 in 2027 + $150,000 on 2028-01-01; 80% of the sleeve locked in a 2-year Treasury on 2031-01-01 at 4.81%
  (strategy_mc convention); the rest stays invested to 2033-01-01; annual rebalancing; no fees; lognormal i.i.d.
- Sleeve bonds (VGSH-like short Treasuries): ASSUMPTION 4.80% compound, 2.0% vol, correlation 0 with equities.
  Why: VGSH SEC yield 4.55% (S3 ticket, VERIFIED-PRIMARY) and 1y forward rates 2028-2032 ~4.8-5.1% on today's curve.
  (strategy_mc.py uses JPM intermediate Treasuries 4.00%, which F-317 flags as ~1pp stale.)

OUTPUTS: hurdle rates, equity premiums by house, sleeve outcomes by equity weight under each house, a fixed crash
stress, and the median-gain vs p5-cost trade-off. All outputs are ASSUMPTION-based model numbers except the inputs.
"""
import csv
from datetime import date

import numpy as np

# ---------- 1. Treasury hurdle: what the sleeve earns with no stock risk (forwards locked today) ----------
CSV = "competition/official_market_data/daily-treasury-rates_2026-09.csv"
row = next(r for r in csv.DictReader(open(CSV)) if r["Date"] == "09/25/2026")
tenor = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
         "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}
par = {t: float(row[k]) for k, t in tenor.items()}
val = date(2026, 9, 25)
yf = lambda d: (d - val).days / 365.25


def build(par):
    ts = sorted(par); grid = np.arange(0.5, 30.01, 0.5)
    p = np.interp(grid, ts, [par[t] / 100 for t in ts]); df = []
    for y in p:
        c = y / 2; df.append((1 - c * sum(df)) / (1 + c))
    g = np.r_[0, grid]; lz = np.log(np.r_[1, df])
    return lambda t: np.exp(np.interp(t, g, lz))


DF = build(par)


def fwd_annual(d0, d1):
    """Annual-compounding forward rate locked today for money invested at d0 and returned at d1."""
    t0, t1 = yf(d0), yf(d1)
    return (DF(t0) / DF(t1)) ** (1 / (t1 - t0)) - 1


H = {
    "2027->2033 (6y)": fwd_annual(date(2027, 1, 1), date(2033, 1, 1)),
    "2028->2031 (3y, floor money)": fwd_annual(date(2028, 1, 1), date(2031, 1, 1)),
    "2028->2033 (5y, whole sleeve)": fwd_annual(date(2028, 1, 1), date(2033, 1, 1)),
    "today->2032-09 (6y spot)": fwd_annual(val, date(2032, 9, 25)),
}
print("== 1. Treasury hurdle rates (annual compounding, locked on today's official curve)")
for k, v in H.items():
    print(f"  {k:32s} {v*100:5.2f}%")
HURDLE = H["2028->2033 (5y, whole sleeve)"]

# ---------- 2. Expected equity returns by house and yardstick (compound, nominal USD) ----------
us_w, nonus_w = 0.623, 0.377
dev_share = 0.75  # ASSUMPTION
vg = {"US": (4.2, 6.2), "DEV": (4.5, 6.5), "EM": (2.0, 4.0)}
def vt_blend(pick):
    return us_w * pick(vg["US"]) + nonus_w * (dev_share * pick(vg["DEV"]) + (1 - dev_share) * pick(vg["EM"]))
houses = {
    "JPM 2026 AC World (VT-like)": 7.00,
    "JPM 2026 U.S. large cap": 6.70,
    "Vanguard U.S. low": 4.2, "Vanguard U.S. mid": 5.2, "Vanguard U.S. high": 6.2,
    "Vanguard VT-blend low": vt_blend(lambda r: r[0]),
    "Vanguard VT-blend mid": vt_blend(lambda r: (r[0] + r[1]) / 2),
    "Vanguard VT-blend high": vt_blend(lambda r: r[1]),
    "Yardstick: forward earnings yield 1/19.2": 100 / 19.2,
    "Yardstick: CAPE earnings yield 1/41.48 + 2.34% breakeven": 100 / 41.48 + 2.34,
}
print(f"\n== 2. Expected compound equity return minus the 2028->2033 Treasury hurdle ({HURDLE*100:.2f}%)")
for k, v in houses.items():
    print(f"  {k:58s} {v:5.2f}%   premium {v - HURDLE*100:+5.2f} pp/yr")

# ---------- 3. Sleeve Monte Carlo under each house ----------
PATHS, SEED = 200_000, 20260927
SLEEVE_2027 = 300_000 - 292_264
DEPOSIT_2028 = 150_000
Y2 = 0.0481
BOND_C, BOND_V = 0.048, 0.020  # ASSUMPTION (see docstring)


def lognorm_from_compound(compound, vol):
    """Log-mean/log-sd so the median growth equals the compound rate and the simple-return sd ~ vol."""
    s = np.sqrt(np.log(1 + (vol / (1 + compound)) ** 2))  # arithmetic ~ JPM's (8.31% vs 8.28% for AC World)
    return np.log(1 + compound), s


def run(eq_compound, eq_vol, w, floor_share=0.80, crash=None):
    rng = np.random.default_rng(SEED)
    mu_e, s_e = lognorm_from_compound(eq_compound, eq_vol)
    mu_b, s_b = lognorm_from_compound(BOND_C, BOND_V)
    ze = rng.standard_normal((PATHS, 6)); zb = rng.standard_normal((PATHS, 6))
    re = np.exp(mu_e + s_e * ze) - 1; rb = np.exp(mu_b + s_b * zb) - 1
    if crash is not None:  # deterministic stress: equity return in a given year index
        yr, r = crash; re[:, yr] = r
    s = np.full(PATHS, float(SLEEVE_2027))
    for y in range(4):  # 2027..2030
        if y == 1: s += DEPOSIT_2028
        s *= 1 + w * re[:, y] + (1 - w) * rb[:, y]
    floor = floor_share * s * (1 + Y2) ** 2
    rest = (1 - floor_share) * s
    for y in (4, 5):
        rest *= 1 + w * re[:, y] + (1 - w) * rb[:, y]
    return floor, floor + rest


def q(x, p): return float(np.percentile(x, p))


cases = {"JPM AC World 7.00% / 16.78%": (0.0700, 0.1678),
         "Vanguard VT-blend mid %.2f%% / 16.78%%" % houses["Vanguard VT-blend mid"]:
             (houses["Vanguard VT-blend mid"] / 100, 0.1678),
         "Vanguard U.S. low 4.2% / 16.78%": (0.042, 0.1678)}
weights = (0.0, 0.40, 0.50, 0.60, 0.70, 1.00)
res = {}
print("\n== 3. Lock-early sleeve (facility money) on 2033-01-01 and the 2031 bought floor, by sleeve equity weight")
print("   (payments are funded by the ladder in every row; these are facility/flexibility dollars)")
for cname, (c, v) in cases.items():
    print(f"  -- {cname}")
    _, base_tot = run(c, v, 0.0)
    for w in weights:
        fl, tot = run(c, v, w)
        res[(cname, w)] = (fl, tot)
        below = float((tot < np.median(base_tot)).mean())
        print(f"    equity {int(w*100):3d}%: surplus p5/p50/p95 ${q(tot,5)/1e3:6.1f}k / ${q(tot,50)/1e3:6.1f}k / "
              f"${q(tot,95)/1e3:6.1f}k | floor p5/p50 ${q(fl,5)/1e3:6.1f}k / ${q(fl,50)/1e3:6.1f}k | "
              f"P(below all-Treasury median) {below*100:4.1f}%")

print("\n== 4. Trade-off of moving from 50% to 60% sleeve equity (and 40% to 60%)")
for cname in cases:
    for lo in (0.40, 0.50):
        a = res[(cname, lo)][1]; b = res[(cname, 0.60)][1]
        fa = res[(cname, lo)][0]; fb = res[(cname, 0.60)][0]
        print(f"  {cname:40s} {int(lo*100)}->60: median {(q(b,50)-q(a,50))/1e3:+5.1f}k, p5 {(q(b,5)-q(a,5))/1e3:+5.1f}k, "
              f"p95 {(q(b,95)-q(a,95))/1e3:+5.1f}k; floor p5 {(q(fb,5)-q(fa,5))/1e3:+5.1f}k")

print("\n== 5. Crash stress: stocks -35% in 2030 (the year before the floor is bought), JPM otherwise")
for w in (0.40, 0.50, 0.60, 0.70):
    fl, tot = run(0.07, 0.1678, w, crash=(3, -0.35))
    print(f"  equity {int(w*100)}%: floor p50 ${q(fl,50)/1e3:6.1f}k, surplus p50 ${q(tot,50)/1e3:6.1f}k")

print("\n== 6. Whole-portfolio equity share in 2028 (ladder ~$305k + sleeve ~$158k; brief/S2 arithmetic)")
for w in (0.40, 0.50, 0.60):
    print(f"  sleeve {int(w*100)}% equity -> {w*158_000/463_000*100:4.1f}% of the whole portfolio; "
          f"WInS option (ii) VT weight {w*0.34*100:4.1f}% / VGSH {(1-w)*0.34*100 - 1:4.1f}% (1% cash)")

print("\n== 7. What the equity really owns in dollars (2028, sleeve ~$158k; VT top-10 = 21.7%, all AI-linked, a LOWER")
print("   bound; S2 table, Vanguard fact sheet 2026-06-30, VERIFIED-PRIMARY; S&P 500 AI basket 40.7%, SPYM 2026-09-24)")
for w in (0.50, 0.60):
    eq = w * 158_000
    print(f"  sleeve {int(w*100)}%: VT ${eq/1e3:.0f}k -> AI-linked top-10 >= ${0.217*eq/1e3:.1f}k "
          f"({0.217*eq/463_000*100:.1f}% of the whole portfolio); same money in an S&P 500 fund: ${0.407*eq/1e3:.1f}k")
print("  WInS option (ii) at 50/50 on $300,000: VT $51,000 (~%d sh at $160.03), VGSH $48,000 (~%d sh at $57.59)"
      % (51_000 // 160.03, 48_000 // 57.59))
