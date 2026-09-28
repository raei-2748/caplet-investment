"""E4 (rival strategist) - numbers behind research/insight_v1/phase_E/E4_rival.md.

How to run (repo root, about 20 seconds):
    .venv/bin/python research/insight_v1/scripts/E4_rival_numbers.py

WHAT IT COMPARES (every output is a MODEL PROPERTY under the stated assumptions, not a forecast)
 E1  = the plan in phase_E/E1_change_proposals.md: ten payments bought in Jan 2027 (same in both designs); growth money
       50% world stocks / 50% short Treasuries rebalanced yearly 2028-2030; on 1 Jan 2031 a share a=0.8 is bought as a
       2-year Treasury (the bottom); in 2033 the gift = bottom + s x (what the rest became), s=0.5, uncapped; the other
       (1-s) is kept. Top = bottom + s x the 90th percentile of the rest's 2-year growth. Reproduces E1 P7 row 1
       ("80/10/10") with E1's own engine (D6_behavioural_numbers.py: same random stream, same lognormal fit).
 R   = the rival ("dated barbell"): same ladder; on 1 Jan 2028 whatever arrives first finishes the ladder, then part
       of the growth money buys a Treasury maturing before 1 Jan 2033 (the bottom, known from 2028); the rest goes
       100% into one world stock fund and is left alone (no rebalancing) until 2033. In 2031 nothing is traded: the
       range announced is [bottom, bottom + s x the stock fund's value that day]. In 2033 the gift = bottom +
       s x min(stock fund 2033, stock fund 2031) (capped at the announced top); everything else is kept as flexibility.
       Rival DEFAULT rule: the bottom repays, just before 2033, the dollar amount of the 2028 deposit ($150,000), so the
       locked share a = 150,000 / 1.0498^5 / growth money (about 0.744); s = 1/2; capped. Alternate a = 2/3 (the same
       stock exposure as E1). A grid of a and s is printed.

 [1] Reproduction of E1's P7 row (80/10/10, 50/50 sleeve): bottom, top, gift and kept p5/p50/p95.
 [2] Head-to-head, E1 vs rival grid: total 2033 surplus, the 2031 bottom (distribution across paths), top, width,
     gift, kept, P(top reached) / P(above top), whole-portfolio stock share by stage, stock "percent-years" 2028-2032.
 [3] Stress: a bad 2028-2030 (bottom 10% of 3-year stock returns) and a bad 2031-2032 (bottom 10% of 2-year stock
     returns, i.e. after Laura has spoken): effect on the announced bottom and on the gift.
 [4] Rival sensitivity to the January-2028 5-year rate (4.0% / 4.98% / 5.23%) and to a smaller 2028 deposit ($75k).
 [5] History: every 6-year window 1928-2025 (Damodaran S&P 500 total return; bond proxy 50% T-bill + 50% 10-year
     Treasury, as D3), raw and rescaled to JPM's AC World median, placed in 2027-2032: worst window, p10, median of
     the 2033 surplus and of the gift; share of 2-year S&P periods with a total return >= 0 (the rival's "top
     reached" check, with no model).
 [6] Maximum loss statement: the most money the rival can lose to stock markets (the stock fund) as a share of all
     money, versus E1's stock money at risk in 2028; model P(2-year world-stock return >= 0).
 [7] Rival default: what a rate fall before January 2027 does to the bottom (top-up costs from the D1/D3 table), the
     share of the median gift already owned in 2031, and the WInS book R(ii) (Laura's plan on 2 Jan 2028 scaled to
     $300,000) at the 2026-09-25 closes (IEF 90.00, TLH 93.38, VT 160.03 via ticket v1, VERIFIED-PRIMARY there; IBTM
     NAV 21.83 on iShares, VERIFIED-PRIMARY, read 2026-09-28; the 2032 note's model price is D1's, ASSUMPTION).

INPUTS and status labels
 - $292,264 ladder at 2027-01-01 and leftover $7,736 (VERIFIED-REPO-FILE inputs, official_curve_pv.py; F-101, F-104).
 - $150,000 deposit at 2028-01-01 (VERIFIED-REPO-FILE, case p.2 L43-45).
 - JPM 2026 LTCMA AC World 7.00% compound / 8.28% arithmetic (VERIFIED-REPO-FILE, JPM matrix p.2); lognormal fit and
   random stream from D6_behavioural_numbers.py (seed 20260927, 200,000 paths); sleeve bonds 5.00% compound
   ("market-consistent", ASSUMPTION as in E1/D6 case B).
 - Rival: 2027 leftover in T-bills at the 1-year par 4.50% (VERIFIED-REPO-FILE curve 2026-09-25; ASSUMPTION that it
   holds; the WInS ticket's T-bill rule). E1 keeps D6's convention (leftover invested in the sleeve mix during 2027);
   the difference is under $0.5k.
 - Rival bottom bought 1 Jan 2028 at the 5-year par 4.98% (VERIFIED-REPO-FILE curve 2026-09-25; ASSUMPTION that it
   holds in Jan 2028, the same convention D3_barbell.py uses); sensitivities 4.00% and 5.23% (the 2028->2033 forward
   implied by today's curve, D2; not lockable).
 - E1 bottom bought 1 Jan 2031 at the 2-year par 4.81% (VERIFIED-REPO-FILE; ASSUMPTION that it holds, as E1/D6).
 - Damodaran histretSP 1928-2025 snapshot (VERIFIED-PRIMARY dataset page via D3_data_snapshot.py), bond proxy
   ASSUMPTION (D3).
 - No fees, no taxes, i.i.d. lognormal annual returns (ASSUMPTION, as the verified strategy_mc.py). The ladder is
   identical in both designs, so the ten payments are bought in both; every difference below is about the facility
   and flexibility money only.
"""
import csv
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


D6 = load("D6_behavioural_numbers")
JPM_ACWI = D6.lp(0.0700, 0.0828)
LEFT = 300_000 - D6.LADDER            # $7,736
Y1, Y2, Y5 = 0.0450, D6.Y2, 0.0498
LADDER_2028, LADDER_2031, LADDER_2033 = 306_077, 356_384, 394_930  # forward values (F-106, VERIFIED-REPO-FILE inputs)
_g1 = (LADDER_2031 / LADDER_2028) ** (1 / 3)
LADDER_YR = {2028: LADDER_2028, 2029: LADDER_2028 * _g1, 2030: LADDER_2028 * _g1 ** 2, 2031: LADDER_2031,
             2032: (LADDER_2031 * LADDER_2033) ** 0.5}   # 2029, 2030, 2032 interpolated (ASSUMPTION arithmetic)
HIST = os.path.join(HERE, "data", "D3", "damodaran_histretSP_1928_2025.csv")


def k(x):
    return f"${x / 1000:,.0f}k"


def pct3(x):
    return " / ".join(k(np.percentile(x, p)) for p in (5, 50, 95))


# ---------------------------------------------------------------- designs
def sleeve_track(req, rbd, w=0.5, dep=D6.DEP):
    """Same arithmetic as D6.lock_early for 2027-2030 (growth money on 1 Jan 2027..2031), for any number of paths."""
    s = np.full(req.shape[0], float(LEFT))
    track = [s.copy()]
    for y in range(4):
        if y == 1:
            s = s + dep
        s = s * (1 + w * req[:, y] + (1 - w) * rbd[:, y])
        track.append(s.copy())
    return np.array(track).T


def e1_design(req, rbd, w=0.5, a=0.8, s=0.5, q=90, dep=D6.DEP):
    """E1 80/10/10 exactly as E1_split_and_slices.section4 (D6 engine), path by path."""
    track = sleeve_track(req, rbd, w=w, dep=dep)
    S = track[:, 4]                                             # growth money on 1 Jan 2031
    G2 = (1 + w * req[:, 4] + (1 - w) * rbd[:, 4]) * (1 + w * req[:, 5] + (1 - w) * rbd[:, 5])
    g_floor = (1 + Y2) ** 2
    bottom = a * S * g_floor
    g_q = float(np.percentile(G2, q))
    top = bottom + s * (1 - a) * S * g_q
    rest = (1 - a) * S * G2
    gift = bottom + s * rest
    kept = (1 - s) * rest
    s28 = track[:, 1] + dep                                     # growth money 1 Jan 2028 after the deposit
    stock_share = {
        2028: w * s28 / (LADDER_2028 + s28),
        2031: w * (1 - a) * S / (LADDER_2031 + S),
    }
    # percent-years of whole-portfolio stock exposure 2028-2032 (start-of-year weights, summed)
    pctyrs = np.zeros(len(S))
    for yi, yr in enumerate((2028, 2029, 2030)):
        sl = track[:, 1 + yi] + (dep if yi == 0 else 0)
        pctyrs += w * sl / (LADDER_YR[yr] + sl)
    pctyrs += w * (1 - a) * S / (LADDER_YR[2031] + S)
    rest32 = (1 - a) * S * (1 + w * req[:, 4] + (1 - w) * rbd[:, 4])
    pctyrs += w * rest32 / (LADDER_YR[2032] + a * S * (1 + Y2) + rest32)
    return dict(bottom=bottom, top=top, gift=gift, kept=kept, total=gift + kept, stock_share=stock_share,
                pctyrs=pctyrs, above_top=float((gift > top).mean()), reached_top=float((gift >= top).mean()))


def rival_design(req, a=None, s=0.5, y5=Y5, dep=D6.DEP, cap=True):
    """Dated barbell: bottom bought Jan 2028 (matures before 2033); rest 100% stocks, untouched to 2033.
    a=None is the rival's default rule: buy the bottom so that it repays, just before 2033, the amount of the 2028
    deposit ("her 2028 earnings, dollar for dollar"); a = that cost / growth money."""
    n = req.shape[0]
    G = LEFT * (1 + Y1) + dep                                    # growth money 1 Jan 2028 (full deposit: fixed)
    if a is None:
        a = min(1.0, dep / (1 + y5) ** 5 / G)
    G = np.full(n, G)
    bottom = a * G * (1 + y5) ** 5
    pot28 = (1 - a) * G
    pot31 = pot28 * (1 + req[:, 1]) * (1 + req[:, 2]) * (1 + req[:, 3])
    pot33 = pot31 * (1 + req[:, 4]) * (1 + req[:, 5])
    top = bottom + s * pot31
    if cap:
        gift = bottom + s * np.minimum(pot33, pot31)
    else:
        gift = bottom + s * pot33
    kept = bottom + pot33 - gift
    tot28 = LADDER_2028 + G
    stock_share = {2028: pot28 / tot28,
                   2031: pot31 / (LADDER_2031 + a * G * (1 + y5) ** 3 + pot31)}
    pctyrs = np.zeros(n)
    pot = pot28.copy()
    for yi, yr in enumerate((2028, 2029, 2030, 2031, 2032)):
        fl = a * G * (1 + y5) ** yi
        pctyrs += pot / (LADDER_YR[yr] + fl + pot)
        pot = pot * (1 + req[:, 1 + yi])
    return dict(bottom=bottom, top=top, gift=gift, kept=kept, total=bottom + pot33, stock_share=stock_share,
                pctyrs=pctyrs, pot28=pot28, pot31=pot31, pot33=pot33, a=a,
                reached_top=float((pot33 >= pot31).mean()), above_top=0.0 if cap else float((gift > top).mean()))


# ---------------------------------------------------------------- sections
def section1(req, rbd):
    print("[1] Reproduce E1 P7 row 1 (80/10/10, 50/50 sleeve, JPM ACWI 7.00%, bonds 5.0%, no fee)")
    e = e1_design(req, rbd)
    print(f"    median bottom {k(np.median(e['bottom']))}; median top (p90) {k(np.median(e['top']))};"
          f" gift {pct3(e['gift'])}; kept {pct3(e['kept'])}")
    print("    (E1 P7 table: $167k / $192k; gift $151k / $188k / $238k; kept $16k / $21k / $29k)")
    return e


def row(label, d):
    b = d["bottom"]
    return (f"    {label:30s}| total {pct3(d['total'])} | bottom p5/p50/p95 {pct3(b)} | median top {k(np.median(d['top']))}"
            f" (width {np.median(d['top'] / d['bottom']):.2f}x) | gift {pct3(d['gift'])} | kept {pct3(d['kept'])}"
            f" | P(top reached) {d['reached_top'] * 100:.0f}% P(above top) {d['above_top'] * 100:.0f}%"
            f" | stock share 2028 {np.median(d['stock_share'][2028]) * 100:.1f}% 2031 {np.median(d['stock_share'][2031]) * 100:.1f}%"
            f" | stock %-years 2028-32 {np.median(d['pctyrs']) * 100:.0f}")


def section2(req, rbd):
    print("\n[2] Head-to-head (same random stream; ladder identical in both, so payments are bought in both)")
    out = {"E1 80/10/10, 50/50": e1_design(req, rbd)}
    out["E1 70/15/15, 50/50"] = e1_design(req, rbd, a=0.7)
    dflt = rival_design(req)
    out[f"R DEFAULT a={dflt['a']:.3f} s=0.50 cap"] = dflt
    for a in (0.5, 0.6, 2 / 3, 0.8):
        for s in (0.5, 0.75, 1.0):
            out[f"R a={a:.3f} s={s:.2f} cap"] = rival_design(req, a=a, s=s)
    for s in (0.75, 1.0):
        out[f"R DEFAULT rule s={s:.2f} cap"] = rival_design(req, s=s)
    out["R DEFAULT rule s=0.50 NO cap"] = rival_design(req, cap=False)
    for lab, d in out.items():
        print(row(lab, d))
    e = out["E1 80/10/10, 50/50"]
    for lab in (f"R DEFAULT a={dflt['a']:.3f} s=0.50 cap", "R a=0.667 s=0.50 cap", "R a=0.800 s=0.50 cap"):
        b = out[lab]["bottom"][0]
        print(f"    P(E1's 2031 bottom < {lab.split(' s=')[0]} bottom {k(b)}) = {np.mean(e['bottom'] < b) * 100:.0f}%")
    return out


def section3(req, rbd):
    print("\n[3] Stress: bad 2028-2030 (bottom 10% of 3-year stock returns) and bad 2031-2032 (bottom 10% of 2-year)")
    g3 = (1 + req[:, 1]) * (1 + req[:, 2]) * (1 + req[:, 3])
    g2 = (1 + req[:, 4]) * (1 + req[:, 5])
    early = g3 <= np.percentile(g3, 10)
    late = g2 <= np.percentile(g2, 10)
    for lab, d in (("E1 80/10/10", e1_design(req, rbd)), ("R default", rival_design(req)), ("R a=2/3", rival_design(req, a=2 / 3))):
        print(f"    {lab:12s}| all paths: bottom med {k(np.median(d['bottom']))}, gift med {k(np.median(d['gift']))},"
              f" total med {k(np.median(d['total']))}")
        print(f"    {'':12s}| bad 2028-30: bottom med {k(np.median(d['bottom'][early]))} (p5 {k(np.percentile(d['bottom'][early], 5))}),"
              f" gift med {k(np.median(d['gift'][early]))}, total med {k(np.median(d['total'][early]))}")
        inrange = (d["gift"][late] >= d["bottom"][late] - 1e-6).mean()
        width = d["top"][late] - d["bottom"][late]
        lost = np.median(((d["top"][late] - d["gift"][late]) / np.where(width > 0, width, np.nan)))
        print(f"    {'':12s}| bad 2031-32 (after she has spoken): gift med {k(np.median(d['gift'][late]))},"
              f" total med {k(np.median(d['total'][late]))}; gift >= announced bottom in {inrange * 100:.0f}% of these paths;"
              f" median share of the announced range's width not delivered {lost * 100:.0f}%")


def section4(req):
    print("\n[4] Rival sensitivity (default rule: bottom = the 2028 deposit; s = 1/2; cap)")
    for y5 in (0.040, Y5, 0.0523):
        d = rival_design(req, y5=y5)
        print(f"    Jan-2028 5-year rate {y5 * 100:.2f}%: a={d['a']:.3f}; stock fund {k(d['pot28'][0])}; bottom {k(np.median(d['bottom']))}; total {pct3(d['total'])};"
              f" gift {pct3(d['gift'])}")
    d = rival_design(req, dep=75_000)
    print(f"    Deposit $75k (beyond-case stress): bottom {k(np.median(d['bottom']))}; total {pct3(d['total'])};"
          f" gift {pct3(d['gift'])}")


def load_hist():
    rows = [r for r in csv.DictReader(l for l in open(HIST) if not l.startswith("#"))]
    yrs = np.array([int(r["year"]) for r in rows])
    eq = np.array([float(r["sp500_tr"]) for r in rows])
    bd = 0.5 * np.array([float(r["tbill_3m_avg"]) for r in rows]) + 0.5 * np.array([float(r["tbond_10y_tr"]) for r in rows])
    return yrs, eq, bd


def rescale(x, target):
    lx = np.log1p(x)
    return np.expm1(lx - lx.mean() + np.log1p(target))


def section5():
    print("\n[5] History: every 6-year window 1928-2025 placed in 2027-2032 (S&P 500 TR; bond proxy 50% bills + 50% 10y)")
    yrs, heq, hbd = load_hist()
    for lab, eq, bd in (("raw", heq, hbd), ("rescaled to JPM ACWI 7.00% / bonds 5.00%", rescale(heq, 0.07), rescale(hbd, 0.05))):
        n = len(eq) - 5
        R = np.array([eq[i:i + 6] for i in range(n)])
        B = np.array([bd[i:i + 6] for i in range(n)])
        e = e1_design(R, B)
        r = rival_design(R)
        r23 = rival_design(R, a=2 / 3)
        print(f"    -- {lab} ({n} windows)")
        for nm, d in (("E1 80/10/10", e), ("R default", r), ("R a=2/3", r23)):
            t = d["total"]
            w = int(t.argmin())
            print(f"       {nm:12s}| total worst {k(t.min())} (start {yrs[w]}), p10 {k(np.percentile(t, 10))},"
                  f" median {k(np.median(t))} | gift worst {k(d['gift'].min())}, p10 {k(np.percentile(d['gift'], 10))},"
                  f" median {k(np.median(d['gift']))} | bottom worst {k(d['bottom'].min())}")
        for start in (1929, 1973, 2000, 2007):
            i = int(np.where(yrs == start)[0][0])
            print(f"       {start}-{start + 5}: E1 total {k(e['total'][i])} (bottom {k(e['bottom'][i])}, gift {k(e['gift'][i])});"
                  f" R default total {k(r['total'][i])} (bottom {k(r['bottom'][i])}, gift {k(r['gift'][i])});"
                  f" R 2/3 total {k(r23['total'][i])} (gift {k(r23['gift'][i])})")
    two = (1 + heq[:-1]) * (1 + heq[1:]) - 1
    print(f"    Share of 2-year S&P 500 total-return periods >= 0, 1928-2025 (overlapping, n={len(two)}):"
          f" {np.mean(two >= 0) * 100:.0f}%; non-overlapping even starts: {np.mean(two[::2] >= 0) * 100:.0f}%"
          f" (n={len(two[::2])}); since 1950: {np.mean(two[yrs[:-1] >= 1950] >= 0) * 100:.0f}%")


def section6(req, rbd):
    print("\n[6] Money at stock-market risk (the most that can be lost to stocks), share of all assets")
    r = rival_design(req)
    print(f"    Rival default: stock fund bought Jan 2028 {k(r['pot28'][0])} = {r['pot28'][0] / (LADDER_2028 + LEFT * 1.045 + 150_000) * 100:.1f}%"
          f" of all assets; if it went to zero, gift = bottom {k(r['bottom'][0])} and every payment is still bought")
    e = e1_design(req, rbd)
    print(f"    E1: stock money Jan 2028 about {k(0.5 * (LEFT * 1.05 + 150_000))}; a stock fall before 2031 also lowers the bottom"
          f" that is bought in 2031 (bottom p5/p50/p95 {pct3(e['bottom'])})")
    print("    Model P(2-year world-stock return >= 0), JPM ACWI lognormal:"
          f" {np.mean((1 + req[:, 4]) * (1 + req[:, 5]) >= 1) * 100:.0f}%")


def section7(req):
    print("\n[7] Rival default: rates-fall top-up (D1/D3 table), share of the likely gift already owned in 2031,"
          " and the WInS book R(ii)")
    G = LEFT * (1 + Y1) + D6.DEP
    lock = D6.DEP / (1 + Y5) ** 5
    pot = G - lock
    print(f"    growth money Jan 2028 {k(G)}; bottom costs {k(lock)} (repays $150,000 before 2033 at 4.98%); stock fund {k(pot)}")
    for lab, topup in (("-50bp", 9_555), ("-100bp", 25_711), ("-150bp", 42_633)):
        left = pot - topup
        bottom = 150_000 if left >= 0 else 150_000 + left * (1 + Y5) ** 5
        print(f"    rates {lab} before Jan 2027: top-up in Jan 2028 {k(topup)} (D1/D3 table) -> stock fund {k(max(left, 0))},"
              f" bottom {k(bottom)}")
    r = rival_design(req)
    print(f"    share of the median 2033 gift already owned when she speaks in 2031: {150_000 / np.median(r['gift']) * 100:.0f}%")
    # WInS R(ii): Laura's plan on 2 Jan 2028 scaled to $300,000 (hedge share = ladder forward value / total)
    tot = LADDER_2028 + G
    w_hedge, w_min, w_vt = LADDER_2028 / tot, lock / tot, pot / tot
    print(f"    plan on 2 Jan 2028: ladder {w_hedge * 100:.1f}% / bottom {w_min * 100:.1f}% / stock fund {w_vt * 100:.1f}% of {k(tot)}")
    px = {"IEF": 90.00, "TLH": 93.38, "IBTM": 21.85, "VT": 160.03}   # closes 2026-09-25 (VP via ticket v1 / iShares)
    book = {"IEF": 0.235, "TLH": 0.425, "IBTM": round(w_min - 0.01, 3), "VT": round(w_vt, 3)}
    cost = 0
    for t, wt in book.items():
        sh = int(300_000 * wt // px[t])
        cost += sh * px[t]
        print(f"      {t:5s} {wt * 100:5.1f}%  ~{sh:,} sh  ${sh * px[t]:,.0f}")
    print(f"      cash after 4 x $25: ${300_000 - cost - 100:,.0f}")
    note_face = 300_000 * (w_min - 0.01) / 0.9676    # 4.125% 15-Nov-2032 note: clean 95.27 + ~1.49 accrued (D1 model, 9/25)
    print(f"    if the 4.125% 15-Nov-2032 note is listed instead of IBTM: about ${note_face:,.0f} face (D1 model price 95.27"
          f" + accrued ~1.49 per 100 on 9/25; WInS shows its own price); one $10 trade")


if __name__ == "__main__":
    req, rbd = D6.draws(JPM_ACWI, bd=D6.BD_CONSISTENT)
    section1(req, rbd)
    section2(req, rbd)
    section3(req, rbd)
    section4(req)
    section5()
    section6(req, rbd)
    section7(req)
