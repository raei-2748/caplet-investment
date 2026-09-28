"""D5 (Philanthropy & Co-sponsor Analyst): the 2031 co-sponsor range, its confidence wording, and how much of the
2033 post-reserve money stays uncommitted as "financial flexibility" (questions M003, M091, M107, M094).

How to run (repo root):  .venv/bin/python research/insight_v1/scripts/D5_range_and_flexibility.py

INPUTS and status labels
- Ladder cost at 2027-01-01 $292,264 (VERIFIED-REPO-FILE: research/verified_2026-09-27/official_curve_pv.py on the
  official 2026-09-25 Treasury curve).
- 2y par yield 4.81% on 2026-09-25 (VERIFIED-REPO-FILE, competition/official_market_data/). Used as the 2031 2-year rate
  (ASSUMPTION, same as strategy_mc.py and fact_register F-013).
- JPM 2026 LTCMA U.S. large cap 6.70% compound / 7.94% arithmetic; U.S. intermediate Treasuries 4.00% / 4.06%;
  correlation -0.01 (VERIFIED-REPO-FILE, JPM LTCMA PDF in competition/official_market_data/).
- Deposits $300k (2027) and $150k (2028) (VERIFIED-REPO-FILE, case p.2).
- Growth sleeve 60% equity / 40% intermediate Treasuries, annual rebalancing, lognormal i.i.d. returns, no fees
  (ASSUMPTION; identical to strategy_mc.py so results reconcile with fact_register F-401/F-402).
- USD/TWD 31.82 on 2026-09-18 (VERIFIED-PRIMARY per fact_register F-510); s.d. of 2-year USD/TWD moves 6.8% since 2006
  (derived from FRED data per brief section 14 / fact_register; used here only for a dated NT$ reference band).
- Rule parameters a (share of the 2031 sleeve bought as the floor), s (share of the unlocked remainder's 2033 value
  added to the gift), q (percentile of the 2-year growth used for the top of the range): TEAM CHOICES (ASSUMPTION).

WHAT IT PRINTS
 [0] reconciliation with strategy_mc.py (2031 floor at a=0.8 must be ~$127k/$165k/$217k at p5/p50/p95)
 [1] the 2031 range under the rule, at the median, p10 and p90 2031 sleeve value, for several (a, s, q)
 [2] flexibility kept in 2033 (dollars and share of the post-reserve money) under each rule
 [3] why the range must be a 2031 RULE, not dollar figures fixed today: P(gift lands in a range fixed in 2026)
 [4] the capped-gift trap: capping the gift at the top makes P(within range) = 100% by construction
 [5] missing / smaller 2028 deposit
 [6] dated NT$ reference band for the floor
"""
import numpy as np

PATHS, SEED = 200_000, 20260927
LADDER = 292_264
Y2 = 0.0481
G_FLOOR = (1 + Y2) ** 2          # annual convention, as strategy_mc.py (1.0985)


def lognorm_params(compound, arithmetic):
    mu = np.log(1 + compound)
    s2 = 2 * np.log((1 + arithmetic) / (1 + compound))
    return mu, np.sqrt(s2)


EQ = lognorm_params(0.0670, 0.0794)
BD = lognorm_params(0.0400, 0.0406)
RHO = -0.01


def draws(eq_w=0.60):
    """Same random stream and construction as strategy_mc.simulate('L') so numbers reconcile."""
    rng = np.random.default_rng(SEED)
    z1 = rng.standard_normal((PATHS, 6)); z2 = rng.standard_normal((PATHS, 6))
    zb = RHO * z1 + np.sqrt(1 - RHO ** 2) * z2
    req = np.exp(EQ[0] + EQ[1] * z1) - 1
    rbd = np.exp(BD[0] + BD[1] * zb) - 1
    r = 1 + eq_w * req + (1 - eq_w) * rbd          # sleeve gross return per year, 2027..2032
    return r


def sleeve_2031(r, deposit_2028=150_000):
    s = np.full(PATHS, 300_000.0 - LADDER)
    for y in range(4):
        if y == 1:
            s += deposit_2028
        s *= r[:, y]
    return s


def pct(x, ps=(5, 10, 50, 90, 95)):
    return {p: float(np.percentile(x, p)) for p in ps}


def k(x):
    return f"${x/1000:,.0f}k"


if __name__ == "__main__":
    r = draws()
    S = sleeve_2031(r)
    G2 = r[:, 4] * r[:, 5]                           # 2-year growth of the unlocked part, 2031->2033
    gq = {q: float(np.percentile(G2, q * 100)) for q in (0.50, 0.80, 0.85, 0.90)}

    print("[0] Reconciliation with strategy_mc.py")
    fl = 0.8 * S * G_FLOOR
    print("    2031 sleeve S p5/p10/p50/p90/p95:", {p: k(v) for p, v in pct(S).items()})
    print("    floor at a=0.8 p5/p50/p95:", {p: k(v) for p, v in pct(fl, (5, 50, 95)).items()},
          " (strategy_mc/F-402: $127k/$165k/$217k)")
    surplus = fl + 0.2 * S * G2
    print("    2033 surplus p5/p50/p95:", {p: k(v) for p, v in pct(surplus, (5, 50, 95)).items()},
          " (F-401: $159k/$207k/$273k)")
    print("    2-year growth factor of sleeve G2 quantiles:", {q: round(v, 4) for q, v in gq.items()},
          " P(G2<1) =", round(float((G2 < 1).mean()), 3))

    print("\n[1]+[2] Range stated in 2031 = [floor, floor + s*(1-a)*S*G2_q]; 2033 gift = floor + s*(1-a)*S*G2;"
          " flexibility = (1-s)*(1-a)*S*G2")
    S_med, S_p10, S_p90 = (float(np.percentile(S, p)) for p in (50, 10, 90))
    rows = []
    for a in (0.6, 0.7, 0.8, 1.0):
        for s in (0.0, 0.5, 1.0):
            if a == 1.0 and s > 0:
                continue
            q = 0.85
            F = a * S_med * G_FLOOR
            T = F + s * (1 - a) * S_med * gq[q]
            gift = a * S * G_FLOOR + s * (1 - a) * S * G2
            flex = (1 - s) * (1 - a) * S * G2
            post = a * S * G_FLOOR + (1 - a) * S * G2
            share = flex / post
            width = (T - F) / F if F > 0 else float("nan")
            rows.append((a, s, F, T, width, pct(flex), float(np.median(share)), pct(gift)))
            print(f"    a={a:.1f} s={s:.1f} | at median S {k(S_med)}: range {k(F)}-{k(T)} (width {width*100:4.1f}% of floor)"
                  f" | flexibility p5/p50/p95 {k(pct(flex)[5])}/{k(pct(flex)[50])}/{k(pct(flex)[95])}"
                  f" = {np.median(share)*100:4.1f}% of post-reserve money (median)"
                  f" | gift p5/p50/p95 {k(pct(gift)[5])}/{k(pct(gift)[50])}/{k(pct(gift)[95])}")
    print("    P(2033 gift below floor) = 0 by construction (floor bought in a Treasury maturing before 2033)"
          " barring U.S. default; P(above top) = 1-q.")
    print("\n    Range at p10 / p90 of the 2031 sleeve, rule a=0.7, s=0.5, q=0.85:")
    for lab, Sv in (("p10", S_p10), ("p50", S_med), ("p90", S_p90)):
        F = 0.7 * Sv * G_FLOOR; T = F + 0.5 * 0.3 * Sv * gq[0.85]
        print(f"      S {lab} {k(Sv)} -> floor {k(F)}, top {k(T)}, midpoint {k((F+T)/2)}")

    print("\n    Top of range by percentile q (a=0.7, s=0.5, median S): confidence 'within range' = q")
    for q in (0.80, 0.85, 0.90):
        F = 0.7 * S_med * G_FLOOR; T = F + 0.5 * 0.3 * S_med * gq[q]
        print(f"      q={q:.2f}: range {k(F)}-{k(T)}; P(below floor)=0; P(above top)={1-q:.2f}")

    print("\n[3] A dollar range fixed TODAY (2026) instead of a 2031 rule: P(2033 gift inside it)")
    a, s = 0.7, 0.5
    gift = a * S * G_FLOOR + s * (1 - a) * S * G2
    for lo_p, hi_p in ((10, 90), (25, 75)):
        lo, hi = np.percentile(gift, lo_p), np.percentile(gift, hi_p)
        print(f"    today's p{lo_p}-p{hi_p} of the gift = {k(lo)}-{k(hi)}: P(inside) = {((gift>=lo)&(gift<=hi)).mean():.2f};"
              f" P(below its bottom) = {(gift<lo).mean():.2f}  <- a promised bottom that is missed is the overpromise")
    F_med = a * S_med * G_FLOOR
    print(f"    a floor figure copied from today's median ({k(F_med)}) is missed in {(a*S*G_FLOOR < F_med).mean()*100:.0f}% of paths;"
          " the 2031 rule's floor is missed in 0% (it is re-based on what is actually owned in 2031)")

    print("\n[4] Capped-gift trap: if the 2033 gift is capped at the top, P(within) = 100% by construction;"
          " the informative numbers are P(capacity reaches the top) and where money above the top goes")
    for q in (0.80, 0.85, 0.90):
        print(f"    q={q:.2f}: P(capacity above top) = {1-q:.2f}")

    print("\n[5] 2028 deposit smaller / missing (rule a=0.7, s=0.5)")
    for dep in (150_000, 75_000, 0):
        Sd = sleeve_2031(r, dep)
        F = 0.7 * Sd * G_FLOOR
        gift = F + 0.5 * 0.3 * Sd * G2
        print(f"    deposit {k(dep)}: floor p5/p50/p95 {k(np.percentile(F,5))}/{k(np.percentile(F,50))}/{k(np.percentile(F,95))};"
              f" gift median {k(np.median(gift))}")

    print("\n[6] Dated NT$ reference for the floor at the median (a=0.7): rate 31.82 TWD/USD (2026-09-18)")
    F = 0.7 * S_med * G_FLOOR
    for lab, m in (("central", 1.0), ("TWD 6.8% stronger (1 sd, 2y)", 1 / 1.068), ("TWD 6.8% weaker", 1.068)):
        print(f"    {lab}: NT${F*31.82*m/1e6:,.2f}m (US${F/1000:,.0f}k binding)")

    print("\n[7] How far above the top a good market goes (rule a=0.7, s=0.5, q=0.85, median S)")
    F = 0.7 * S_med * G_FLOOR; T = F + 0.15 * S_med * gq[0.85]
    g_cond = F + 0.15 * S_med * G2
    above = g_cond[g_cond > T] - T
    print(f"    P(above top) {(g_cond > T).mean():.3f}; excess over top when above: median {k(np.median(above))},"
          f" p95 {k(np.percentile(above, 95))}; kept flexibility in those paths median"
          f" {k(np.median(0.15 * S_med * G2[g_cond > T]))}")
    print(f"    P(gift below the midpoint of the range) {(g_cond < (F + T) / 2).mean():.2f}"
          "  <- why the midpoint is not a planning figure")

    print("\n[8] Sanity anchor for the flexibility share (ASSUMPTION-based, not a contingency fund):")
    cci = 0.0354   # Taiwan construction cost index average since 2021 (fact_register F-508, VERIFIED-PRIMARY)
    for yrs in (2, 3, 4):
        print(f"    building-cost drift on a fixed US$ pledge over {yrs} years at {cci*100:.2f}%/yr: {((1+cci)**yrs-1)*100:.1f}%")
    print("    1-sd 2-year USD/TWD move: 6.8% (derived, fact_register)")
