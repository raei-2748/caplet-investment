"""D4_facility_purchasing_power.py - which risk moves "how much building Laura's facility money buys" the most by
2033: U.S. market risk, the USD/TWD exchange rate, or Taiwan construction-cost inflation? (Phase D question M095.)

Plain English: Laura's facility contribution is decided and promised in US$ (the portfolio is in US$), but the
building is in Taiwan and is paid for in NT$ (ASSUMPTION: Taiwan construction is priced in NT$). So the real
"building power" of her money is
        building power = (US$ amount) x (NT$ per US$) / (Taiwan construction cost index)
and in logs the three pieces simply add up. The script measures each piece on the SAME horizon, from two vantage
points: (a) today (Sep 2026) looking to 1 Jan 2033 (~6.3 years) and (b) Laura's 2031 conversation looking to
1 Jan 2033 (2 years). It separates a predictable DRIFT (costs rise on average) from two-sided UNCERTAINTY (spread).

Inputs (with status labels):
- U.S. market: the verified model research/verified_2026-09-27/strategy_mc.py (lock-early, 60% equity sleeve,
  80% of the sleeve locked in a 2y Treasury in 2031; JPM 2026 LTCMA inputs VERIFIED-REPO-FILE; lognormal returns,
  2y yield 4.81% in 2031 = ASSUMPTION as in that file). 2031 vantage: median 2031 sleeve state, as in B6b.
- USD/TWD: FRED DEXTAUS daily (Fed H.10), https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXTAUS,
  VERIFIED-PRIMARY when downloaded live (a local copy can be passed with --fx path.csv).
- U.S. equities for the FX-equity correlation: FRED SP500 daily (10 years only on FRED), VERIFIED-PRIMARY live
  (--spx path.csv for an offline copy).
- Taiwan construction cost index (CCI, 2021=100): DGBAS CCI platform via A2_taiwan_cci.query (wages class and
  machinery-rental class; the total is reconstructed by least squares, piecewise by base period
  2008-2015 / 2016-2020 / 2021-), VERIFIED-PRIMARY inputs, derived total (fit error printed).
- Taiwan CPI forecasts 1.90% (DGBAS 2027) / 1.83% (CBC 2027): VERIFIED-PRIMARY in fact_register F-504/F-505
  (typed in here, not downloaded).
- Crisis dates for the event check: Third Taiwan Strait Crisis 1995-07-21 to 1996-03-23 (Wikipedia, read
  2026-09-27; secondary source); Aug 2022 PLA drills 2022-08-04 to 2022-08-10 (general knowledge, UNVERIFIED).
- Independence between the three pieces in the combined band: ASSUMPTION; the script also reports a version with
  the measured FX-equity correlation.
- FX drift: zero (random walk) = ASSUMPTION; 10y realised drift +0.14%/yr supports it (F-512).
- Taiwan 2-year government bond yield 1.66% (2026-08-10): SNIPPET-UNVERIFIED (MacroMicro/search snippet; the
  primary Taipei Exchange page was not read). U.S. 2y par 4.81% (2026-09-25): VERIFIED-REPO-FILE. Used only for the
  cost of locking NT$ in 2031 by covered interest parity (ASSUMPTION: parity holds; the same gap as today in 2031).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/D4_facility_purchasing_power.py
    .venv/bin/python research/insight_v1/scripts/D4_facility_purchasing_power.py --fx DEXTAUS.csv --spx SP500.csv
Results on 2026-09-27 are recorded in research/insight_v1/phase_D/D4_taiwan_fx.md.
"""
import argparse
import io
import sys
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "verified_2026-09-27"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import strategy_mc as smc  # noqa: E402
import A2_taiwan_cci as cci_mod  # noqa: E402

FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
T_LONG = 6.3          # Sep 2026 -> 1 Jan 2033, years (FX last obs 2026-09-18; CCI last obs Aug 2026)
T_SHORT = 2.0         # 1 Jan 2031 -> 1 Jan 2033
USDTWD_NOW = 31.82    # F-510, FRED 2026-09-18


def fred(series, path=None):
    if path:
        raw = open(path, encoding="utf-8").read()
    else:
        with urllib.request.urlopen(FRED.format(series), timeout=60) as r:
            raw = r.read().decode("utf-8")
    df = pd.read_csv(io.StringIO(raw))
    df.columns = ["date", "v"]
    df["date"] = pd.to_datetime(df["date"])
    df["v"] = pd.to_numeric(df["v"], errors="coerce")
    return df.dropna().set_index("date")["v"]


def horizon_moves(s, years, since=None):
    """Overlapping log moves over `years` (calendar), sampled monthly (month-end)."""
    m = s.resample("ME").last().dropna()
    if since is not None:
        m = m[m.index >= since]
    k = int(round(years * 12))
    return np.log(m.values[k:] / m.values[:-k])


def q(x, p):
    return float(np.percentile(x, p))


def pct(x):
    return f"{(np.exp(x) - 1) * 100:+.1f}%"


def cci_total():
    """Reconstruct the CCI total 2008-01..latest from two class queries, fitting weights per base period."""
    wage, rent = cci_mod.query("3", by=2008, bm=1), cci_mod.query("10", by=2008, bm=1)
    months = sorted(set(wage) & set(rent))
    tot, errs = {}, []
    for lo, hi in (((2008, 1), (2015, 12)), ((2016, 1), (2020, 12)), ((2021, 1), (2099, 12))):
        ks = [k for k in months if lo <= k <= hi]
        a = np.array([[wage[k][1] - wage[k][0], -(rent[k][1] - rent[k][0])] for k in ks])
        b = np.array([rent[k][0] - wage[k][0] for k in ks])
        (w1, w2), *_ = np.linalg.lstsq(a, b, rcond=None)
        for k in ks:
            t1 = wage[k][0] + w1 * (wage[k][1] - wage[k][0])
            t2 = rent[k][0] + w2 * (rent[k][1] - rent[k][0])
            tot[k] = (t1 + t2) / 2
            errs.append(abs(t1 - t2))
        print(f"  CCI segment {lo}-{hi}: wage weight {w1:.3f}, rental weight {w2:.3f}, "
              f"max fit error {max(abs((wage[k][0] + w1*(wage[k][1]-wage[k][0])) - (rent[k][0] + w2*(rent[k][1]-rent[k][0]))) for k in ks):.3f} pts")
    idx = pd.Series({pd.Timestamp(y, m, 1) + pd.offsets.MonthEnd(0): v for (y, m), v in tot.items()}).sort_index()
    return idx, max(errs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fx")
    ap.add_argument("--spx")
    args = ap.parse_args()

    print("=" * 100)
    print("1. U.S. MARKET RISK on the facility pool (verified model, lock-early, 60% equity sleeve, 80% 2031 floor)")
    r = smc.simulate("L")
    sur = r["surplus"]
    lsur = np.log(sur)
    med = np.median(sur)
    print(f"  2026 view, 2033 pool p5/p50/p95: ${q(sur,5):,.0f} / ${med:,.0f} / ${q(sur,95):,.0f}")
    print(f"     relative to median: p5 {pct(q(lsur,5)-np.log(med))}, p95 {pct(q(lsur,95)-np.log(med))}; "
          f"log sd {lsur.std():.4f}")
    # 2031 vantage at the median 2031 sleeve state (B6b method): total = f*s*1.0481^2 + (1-f)*s*g2
    rng = np.random.default_rng(smc.SEED + 1)
    z1, z2 = rng.standard_normal((2, 200_000, 2))
    ze, zb = z1, smc.RHO * z1 + np.sqrt(1 - smc.RHO ** 2) * z2
    req = np.exp(smc.EQ[0] + smc.EQ[1] * ze) - 1
    rbd = np.exp(smc.BD[0] + smc.BD[1] * zb) - 1
    g2 = np.prod(1 + 0.6 * req + 0.4 * rbd, axis=1)
    s31 = np.median(r["floor"]) / (0.8 * (1 + smc.Y2) ** 2)
    tot31 = 0.8 * s31 * (1 + smc.Y2) ** 2 + 0.2 * s31 * g2
    lt = np.log(tot31)
    m31 = np.median(tot31)
    print(f"  2031 view (median 2031 sleeve ${s31:,.0f}): 2033 p5/p50/p95 ${q(tot31,5):,.0f} / ${m31:,.0f} / "
          f"${q(tot31,95):,.0f}; rel. p5 {pct(q(lt,5)-np.log(m31))}, p95 {pct(q(lt,95)-np.log(m31))}; log sd {lt.std():.4f}")
    lt100 = 0.0  # 100% locked -> no market spread
    print(f"  (If 100% of the sleeve were locked in 2031 the 2031-view market spread would be {lt100:.0%}.)")

    print("=" * 100)
    print("2. USD/TWD (NT$ per US$; + = TWD weaker = more NT$ per US$ = MORE building per US$)")
    fx = fred("DEXTAUS", args.fx)
    print(f"  FRED DEXTAUS {fx.index[0].date()} to {fx.index[-1].date()}, latest {fx.iloc[-1]:.2f}")
    fx_stats = {}
    for label, since in (("since 2006", pd.Timestamp("2006-01-01")), ("since 1983", None)):
        for T in (T_SHORT, T_LONG):
            mv = horizon_moves(fx, T, since)
            fx_stats[(label, T)] = mv
            print(f"  {label:>10}, {T:.1f}y moves (n={len(mv)} monthly overlapping): p5 {pct(q(mv,5))}, "
                  f"p50 {pct(q(mv,50))}, p95 {pct(q(mv,95))}; log sd {mv.std():.4f}")
    d10 = np.diff(np.log(fx[fx.index >= fx.index[-1] - pd.DateOffset(years=10)].values)).std() * np.sqrt(252)
    print(f"  sqrt-time from 10y daily vol {d10:.4f}: 2y sd {d10*np.sqrt(2):.4f}, 6.3y sd {d10*np.sqrt(T_LONG):.4f}")

    # Event check: Taiwan Strait crises
    for name, a, b in (("Third Taiwan Strait Crisis", "1995-07-20", "1996-03-25"),
                       ("Aug 2022 PLA drills", "2022-08-01", "2022-08-12")):
        w = fx[(fx.index >= a) & (fx.index <= b)]
        pre = fx[fx.index <= a].iloc[-1]
        print(f"  {name}: NT$/US$ {pre:.2f} before -> max {w.max():.2f} ({(w.max()/pre-1)*100:+.1f}%) -> "
              f"{w.iloc[-1]:.2f} at end ({(w.iloc[-1]/pre-1)*100:+.1f}%)")
    wide = fx[(fx.index >= "1995-06-01") & (fx.index <= "1996-06-30")]
    print(f"  1995-06..1996-06 range {wide.min():.2f}-{wide.max():.2f}")

    print("=" * 100)
    print("3. TAIWAN CONSTRUCTION COST INDEX (CCI) - higher cost = LESS building per NT$")
    cci, err = cci_total()
    print(f"  CCI total (derived) {cci.index[0].date()} to {cci.index[-1].date()}, latest {cci.iloc[-1]:.2f}; "
          f"max fit error {err:.3f} pts")
    ann = cci.resample("YE").mean()
    yoy = ann.pct_change().dropna()
    print("  Calendar-year average growth: " + ", ".join(f"{d.year} {v*100:+.1f}%" for d, v in yoy.items()))
    yrs_all = (cci.index[-1] - cci.index[0]).days / 365.25
    cagr_all = (cci.iloc[-1] / cci.iloc[0]) ** (1 / yrs_all) - 1
    print(f"  CAGR {cci.index[0].date()}..{cci.index[-1].date()} ({yrs_all:.1f}y): {cagr_all*100:.2f}%/yr")
    cci_stats = {}
    for T in (T_SHORT, T_LONG):
        mv = horizon_moves(cci, T)
        cci_stats[T] = mv
        print(f"  {T:.1f}y CCI moves (n={len(mv)}): p5 {pct(q(mv,5))}, p50 {pct(q(mv,50))}, p95 {pct(q(mv,95))}; "
              f"mean {pct(mv.mean())}, log sd {mv.std():.4f}")
    scen = {"Taiwan CPI forecast 1.9%/yr (F-504)": 0.019, f"CCI 2008-2026 CAGR {cagr_all*100:.2f}%": cagr_all,
            "CCI since 2021 base 3.54%/yr (F-508)": 0.0354, "2026 spike 6.53%/yr (F-508; do not project)": 0.0653}
    print("  Cumulative cost rise Aug 2026 -> Jan 2033 and building power of a FIXED US$ (FX unchanged):")
    for k, g in scen.items():
        c = (1 + g) ** T_LONG
        print(f"    {k:<45} cost x{c:.3f} ({(c-1)*100:+.0f}%) -> a fixed US$ buys {(1/c-1)*100:+.0f}% building")

    print("=" * 100)
    print("4. CORRELATIONS")
    spx = fred("SP500", args.spx)
    fm, sm = fx.resample("ME").last(), spx.resample("ME").last()
    j = pd.concat([np.log(fm).diff(), np.log(sm).diff()], axis=1).dropna()
    j.columns = ["fx", "spx"]
    rho_m = j.corr().iloc[0, 1]
    ja = pd.concat([np.log(fx.resample("YE").last()).diff(), np.log(spx.resample("YE").last()).diff()], axis=1).dropna()
    print(f"  Monthly: corr(NT$ per US$ change, S&P 500 return) = {rho_m:+.2f} over {len(j)} months "
          f"({j.index[0].date()}..{j.index[-1].date()})")
    print(f"  Annual (n={len(ja)}): {ja.corr().iloc[0,1]:+.2f}")
    # beta: how many % does TWD weaken per -10% S&P month
    beta = np.polyfit(j["spx"], j["fx"], 1)[0]
    print(f"  Beta of FX on S&P monthly: {beta:+.3f} (a -10% S&P month ~ {beta*-10:+.2f}% NT$ per US$)")
    ca = pd.concat([np.log(cci.resample("YE").mean()).diff(), np.log(fx.resample("YE").mean()).diff()], axis=1, sort=True).dropna()
    print(f"  Annual corr(CCI growth, NT$ per US$ change) 2009-2026 (n={len(ca)}): {ca.corr().iloc[0,1]:+.2f}")

    print("=" * 100)
    print("5. COMBINED: building power = US$ pool x FX / CCI (log sum). Drift vs spread by vantage point")
    for vantage, T, m_sd, fxmv, ccimv in (("2026 view -> 2033", T_LONG, lsur.std(), fx_stats[("since 2006", T_LONG)], cci_stats[T_LONG]),
                                         ("2031 view -> 2033", T_SHORT, lt.std(), fx_stats[("since 2006", T_SHORT)], cci_stats[T_SHORT])):
        fx_sd, cci_sd = fxmv.std(), ccimv.std()
        var = {"market": m_sd ** 2, "FX": fx_sd ** 2, "construction (spread)": cci_sd ** 2}
        tot = sum(var.values())
        drift_cci = -np.log(1.0354) * T
        print(f"  {vantage}: log sd market {m_sd:.3f}, FX {fx_sd:.3f} (since 2006), CCI {cci_sd:.3f}; "
              f"variance shares " + ", ".join(f"{k} {v/tot*100:.0f}%" for k, v in var.items()))
        print(f"     combined sd (independent) {np.sqrt(tot):.3f} -> 90% band about {pct(-1.645*np.sqrt(tot))}/{pct(1.645*np.sqrt(tot))}")
        cov = 2 * rho_m * m_sd * fx_sd
        print(f"     with measured FX-equity corr {rho_m:+.2f}: combined sd {np.sqrt(tot+cov):.3f}")
        print(f"     CONSTRUCTION DRIFT at 3.54%/yr: {pct(drift_cci)} (one-sided, expected); "
              f"at 1.9% CPI-like: {pct(-np.log(1.019)*T)}")

    print("=" * 100)
    print("6. NT$ ILLUSTRATION (dated rate 31.82 on 2026-09-18; FX only)")
    for lab, usd in (("2026-view median pool", med), ("2031-view median", m31), ("2031 bought floor (median state)", 0.8*s31*(1+smc.Y2)**2)):
        mv = fx_stats[("since 2006", T_SHORT)]
        print(f"  {lab}: US${usd:,.0f} = NT${usd*USDTWD_NOW/1e6:.2f}m; 2y FX p5/p95 -> NT${usd*USDTWD_NOW*np.exp(q(mv,5))/1e6:.2f}m"
              f" / NT${usd*USDTWD_NOW*np.exp(q(mv,95))/1e6:.2f}m")
    # 2031 view NT$ band combining market (sim) with FX (bootstrap from historical 2y moves), independent
    rng2 = np.random.default_rng(7)
    mv = fx_stats[("since 2006", T_SHORT)]
    ntd = tot31 * USDTWD_NOW * np.exp(rng2.choice(mv, size=tot31.size))
    print(f"  2031 view NT$ band (market x historical 2y FX, independent): p5 {pct(np.log(q(ntd,5)/np.median(ntd)))}, "
          f"p95 {pct(np.log(q(ntd,95)/np.median(ntd)))}  vs US$ band p5 {pct(q(lt,5)-np.log(m31))}, p95 {pct(q(lt,95)-np.log(m31))}")
    fl = 0.8 * s31 * (1 + smc.Y2) ** 2
    fl_ntd = fl * USDTWD_NOW * np.exp(mv)
    print(f"  US$ floor is certain; the SAME floor in NT$ falls below its dated NT$ value in "
          f"{(fl_ntd < fl*USDTWD_NOW).mean()*100:.0f}% of historical 2y windows since 2006, by >5% in "
          f"{(fl_ntd < 0.95*fl*USDTWD_NOW).mean()*100:.0f}%, by >10% in {(fl_ntd < 0.90*fl*USDTWD_NOW).mean()*100:.0f}%")

    print("=" * 100)
    print("7. COST OF LOCKING NT$ IN 2031 (covered interest parity; ASSUMPTION today's 2y gap persists)")
    tw2, us2 = 0.0166, smc.Y2
    fwd = ((1 + tw2) / (1 + us2)) ** 2 - 1
    print(f"  2y forward vs spot: {fwd*100:+.1f}% NT$ per US$ (TW 2y {tw2:.2%} SNIPPET-UNVERIFIED, US 2y {us2:.2%})")
    mv = fx_stats[("since 2006", T_SHORT)]
    print(f"  Share of 2y windows since 2006 in which NT$ strengthened by more than that (lock would have paid): "
          f"{(np.exp(mv)-1 < fwd).mean()*100:.0f}%; median realised 2y move {pct(np.median(mv))}")


if __name__ == "__main__":
    main()
