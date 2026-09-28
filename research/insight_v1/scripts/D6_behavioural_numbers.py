"""D6 (Client Psychologist / Behavioural Finance) numbers for questions M237, M019, M197 and M228.

What it computes (every output is a MODEL PROPERTY under the stated assumptions, not a forecast):
 [1] Reproduces the verified base (strategy_mc.py): lock-early surplus 2033 p5/p50/p95 at sleeve equity 60%.
 [2] M237: design table for sleeve equity 0-100% (80% of the sleeve locked in a 2-year Treasury in 2031) and which
     design each candidate selection rule picks: max median; max p5; Telser/Das-style "best median subject to
     P(surplus < threshold) <= 5%"; loss-averse value at the 2033 goal date against two reference points (the
     riskless all-Treasury control, and the nominal money put into the sleeve).
 [3] M019 / bad years: how often Laura's statements would show a fall (growth money and whole portfolio), the size
     of the worst single-year fall of the growth money, and, for contrast only, how often the rejected growth-first
     plan would show the ten payments NOT covered by the assets (funded ratio < 1).
 [4] M197: width of the range Laura would announce in January 2031 (bought floor to the p90/p95 of the 2033 total),
     as a top/bottom ratio, for lock shares 50-100%; plus the 2026-view ratio for comparison.
 [5] M228: word counts in the official case (what the case asks the firm to do).

Inputs and status labels:
 - $292,264 = value at 2027-01-01 of the ten $50k payments on the 2026-09-25 official curve
   (VERIFIED-REPO-FILE: research/verified_2026-09-27/official_curve_pv.py; F-101).
 - 2y par yield 4.81% on 2026-09-25, used for the 2031 floor (VERIFIED-REPO-FILE, F-001; ASSUMPTION that it holds
   in 2031, as in strategy_mc.py).
 - JPM 2026 LTCMA: U.S. large cap 6.70% compound / 7.94% arithmetic / 16.47% vol; intermediate Treasuries 4.00% /
   4.06%; correlation -0.01 (VERIFIED-REPO-FILE, F-301/F-307/F-314). Same lognormal fit as strategy_mc.py.
 - Vanguard midpoint 5.2% compound for U.S. equities (B10a, VERIFIED-PRIMARY there: 4.2%-6.2% range, model run
   2026-06-30); used only as a sensitivity with JPM volatility kept (ASSUMPTION).
 - Riskless control: the whole growth money held in Treasuries to 2033 at ~5.08% semiannual (forward zero 2027->2033,
   F-012), also applied to the 2028 deposit over 5 years (ASSUMPTION: forward 2028->2033 ~ same rate).
 - Rate path for mark-to-market (section [3] only): one flat yield that reprices the ten payments to $292,264 on
   2027-01-01, then a random walk with annual sd 0.75 percentage points (ASSUMPTION: 2026 realised volatility of the
   ladder cost 7.24% (brief s14) divided by duration ~9.9 gives ~0.73pp). Independent of equities (JPM corr ~0).
 - Growth-first glide 75/75/75/75/60/40% equity, as in strategy_mc.py (only used as the rejected contrast).
 - Loss-aversion coefficient lambda = 2.25 (Tversky & Kahneman 1992, widely cited; SNIPPET-UNVERIFIED here: the
   primary paper was not opened). Tested at 1.5 / 2.25 / 3.0. Linear value function (ASSUMPTION, no curvature).
 - Thresholds $140k/$150k/$160k/$170k for the safety-first rule are ASSUMPTIONS (the case sets no facility target).
   The "plain rule" uses the money Laura puts into the growth money ($300,000 - $292,264 + $150,000 = $157,736,
   nominal, DERIVED) as the threshold, at 1-in-20 and 1-in-10 (ASSUMPTION: a reference point most people use).
 - Sleeve bonds: JPM intermediate Treasuries 4.00% in the verified base (case A); 5.00% compound (JPM vol kept) in
   cases B and C, following B10a's correction that today's Treasury yields (~4.8-5.2%) sit ~1pp above JPM's
   assumption (F-317) (ASSUMPTION). Only B and C are fair for comparing designs against the riskless control.
 - i.i.d. lognormal annual returns, no fees, no taxes (ASSUMPTION, as in strategy_mc.py; fat tails not modelled).

Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D6_behavioural_numbers.py
"""
import re
import numpy as np
from scipy.optimize import brentq

PATHS, SEED = 200_000, 20260927
LADDER = 292_264
Y2 = 0.0481
DEP = 150_000


def lp(compound, arithmetic):
    return np.log(1 + compound), np.sqrt(2 * np.log((1 + arithmetic) / (1 + compound)))


EQ = lp(0.0670, 0.0794)
BD = lp(0.0400, 0.0406)
RHO = -0.01


BD_CONSISTENT = lp(0.0500, 0.0506)   # B10a correction: sleeve bonds near today's yields (ASSUMPTION), JPM vol kept


def draws(eq=EQ, seed=SEED, bd=BD):
    """Same random stream and order as strategy_mc.simulate()."""
    rng = np.random.default_rng(seed)
    z1 = rng.standard_normal((PATHS, 6))
    z2 = rng.standard_normal((PATHS, 6))
    req = np.exp(eq[0] + eq[1] * z1) - 1
    rbd = np.exp(bd[0] + bd[1] * (RHO * z1 + np.sqrt(1 - RHO ** 2) * z2)) - 1
    return req, rbd


def lock_early(req, rbd, eq_w=0.60, floor_share=0.80, dep=DEP):
    """Lock-early sleeve. Returns 2033 surplus, 2031 floor, and the sleeve value at each Jan 1 2027..2033."""
    s = np.full(PATHS, 300_000.0 - LADDER)
    track = [s.copy()]                       # Jan 1 2027 (after ladder purchase)
    for y in range(4):                       # 2027..2030
        if y == 1:
            s = s + dep
        s = s * (1 + eq_w * req[:, y] + (1 - eq_w) * rbd[:, y])
        track.append(s.copy())               # Jan 1 2028..2031 (before the 2028 deposit is added)
    floor = floor_share * s * (1 + Y2) ** 2
    rest = (1 - floor_share) * s
    for y in (4, 5):
        rest = rest * (1 + eq_w * req[:, y] + (1 - eq_w) * rbd[:, y])
        track.append(floor_share * s * (1 + Y2) ** (y - 3) + rest)
    return floor + rest, floor, np.array(track).T   # track: (PATHS, 7) = Jan 1 2027..2033


def pct(x, ps=(5, 50, 95)):
    return [int(round(np.percentile(x, p), -3)) for p in ps]


def control_2033():
    f = 1 + 0.0508 / 2
    return (300_000 - LADDER) * f ** 12 + DEP * f ** 10


def pt_value(x, ref, lam):
    gain = np.maximum(x - ref, 0).mean()
    loss = np.maximum(ref - x, 0).mean()
    return gain - lam * loss


def section_designs(eq, label, bd=BD):
    req, rbd = draws(eq, bd=bd)
    C = control_2033()
    money_in = 300_000 - LADDER + DEP
    ws = (0.0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0)
    rows = {}
    for w in ws:
        sur, flo, _ = lock_early(req, rbd, eq_w=w)
        rows[w] = sur
    print(f"\n[2] M237 design table ({label}); 80% of sleeve locked in 2031; riskless control C = ${C:,.0f}; "
          f"money put into the sleeve = ${money_in:,.0f}")
    print("  equity  p5    p10   p50   p95   | P(<C)  E[shortfall vs C | short]")
    for w in ws:
        x = rows[w]
        p5, p10, p50, p95 = pct(x, (5, 10, 50, 95))
        below = (x < C).mean()
        es = (C - x[x < C]).mean() if below > 0 else 0.0
        print(f"  {int(w*100):3d}%  {p5/1e3:5.0f}k {p10/1e3:5.0f}k {p50/1e3:5.0f}k {p95/1e3:5.0f}k | "
              f"{below*100:5.1f}%  ${es/1e3:5.1f}k")
    print("  Rules and the design each picks:")
    med = {w: np.median(rows[w]) for w in ws}
    p5s = {w: np.percentile(rows[w], 5) for w in ws}
    print(f"   max median            -> {int(max(med, key=med.get)*100)}% equity")
    print(f"   max p5                -> {int(max(p5s, key=p5s.get)*100)}% equity")
    for T in (140_000, 150_000, 160_000, 170_000):
        ok = [w for w in ws if (rows[w] < T).mean() <= 0.05]
        pick = max(ok, key=lambda w: med[w]) if ok else None
        print(f"   best median s.t. P(surplus < ${T/1e3:.0f}k) <= 5%  -> "
              f"{'none' if pick is None else str(int(pick*100)) + '% equity'}"
              f"   [P(<T) by design: " + ", ".join(f"{int(w*100)}%:{(rows[w] < T).mean()*100:.1f}" for w in ws) + "]")
    for alpha in (0.05, 0.10):
        ok = [w for w in ws if (rows[w] < money_in).mean() <= alpha]
        pick = max(ok, key=lambda w: med[w]) if ok else None
        print(f"   PLAIN RULE: most equity s.t. P(2033 growth money < money put in ${money_in/1e3:.1f}k) <= "
              f"{int(alpha*100)}%  -> {'none' if pick is None else str(int(pick*100)) + '% equity'}   [P by design: "
              + ", ".join(f"{int(w*100)}%:{(rows[w] < money_in).mean()*100:.1f}" for w in ws) + "]")
    for ref_name, ref in (("riskless control C", C), ("money put in", money_in)):
        for lam in (1.5, 2.25, 3.0):
            v = {w: pt_value(rows[w], ref, lam) for w in ws}
            best = max(v, key=v.get)
            print(f"   loss-averse at 2033, ref={ref_name}, lambda={lam}: best {int(best*100)}% "
                  f"(value by design: " + ", ".join(f"{int(w*100)}%:{v[w]/1e3:+.1f}k" for w in ws) + ")")
    return rows


def section_fat_tails(df=4):
    """[2b] Robustness of the plain rule: equity log-returns Student-t (df=4) scaled to the same mean and sd
    (ASSUMPTION; a crude stand-in for crash years; historical sequences are D3's job, question M059)."""
    rng = np.random.default_rng(SEED)
    z1 = rng.standard_normal((PATHS, 6))
    z2 = rng.standard_normal((PATHS, 6))
    t = np.random.default_rng(SEED + 7).standard_t(df, (PATHS, 6)) / np.sqrt(df / (df - 2))
    for bd_label, bd in (("bonds 4.00%", BD), ("bonds 5.00%", BD_CONSISTENT)):
        req = np.exp(EQ[0] + EQ[1] * t) - 1
        rbd = np.exp(bd[0] + bd[1] * (RHO * z1 + np.sqrt(1 - RHO ** 2) * z2)) - 1
        money_in = 300_000 - LADDER + DEP
        out = []
        for w in (0.4, 0.5, 0.6, 0.7):
            sur, _, _ = lock_early(req, rbd, eq_w=w)
            out.append(f"{int(w*100)}%: P(<money in) {(sur < money_in).mean()*100:.1f}%, p5 ${np.percentile(sur, 5)/1e3:.0f}k, "
                       f"p50 ${np.median(sur)/1e3:.0f}k")
        print(f"\n[2b] Fat-tail check (JPM equities, Student-t df={df}, {bd_label}): " + "; ".join(out))


def section_bad_years():
    req, rbd = draws(EQ)
    rng = np.random.default_rng(SEED + 1)          # separate stream: rates for mark-to-market only
    y0 = brentq(lambda y: sum(50_000 / (1 + y) ** (6 + k) for k in range(10)) - LADDER, 0.01, 0.10)
    dy = 0.0075 * rng.standard_normal((PATHS, 6))
    ylev = y0 + np.cumsum(dy, axis=1)              # yield at Jan 1 2028..2033

    def pv_payments(y, t):                         # value at Jan 1 (2027+t) of the ten payments from 2033
        return sum(50_000 / (1 + np.maximum(y, 0.0)) ** (6 - t + k) for k in range(10))

    print(f"\n[3] Bad years. Flat yield repricing the ladder to $292,264 = {y0*100:.2f}%; rate sd 0.75pp/yr (ASM)")
    sur, flo, track = lock_early(req, rbd, eq_w=0.60)
    # growth money: calendar-year change in value, excluding the 2028 deposit (years 2027..2032)
    base = track[:, :-1].copy()
    base[:, 1] = base[:, 1] + DEP                   # the 2028 deposit arrives on Jan 1 2028
    chg = track[:, 1:] - base                       # dollar change during each calendar year 2027..2032
    ret = chg / base
    down_year = (chg < 0)
    print("  Current plan (sleeve 60% equity, 80% floor in 2031):")
    print(f"   growth money: P(a given year 2028-2030 is down) = {down_year[:, 1:4].mean()*100:.0f}%; "
          f"P(at least one down year 2028-2032) = {(down_year[:, 1:6].any(1)).mean()*100:.0f}%")
    worst = chg[:, 1:6].min(1)
    worst_pct = ret[:, 1:6].min(1)
    print(f"   worst single-year change of the growth money 2028-2032: median ${np.median(worst)/1e3:,.0f}k "
          f"({np.median(worst_pct)*100:.0f}%), p5 ${np.percentile(worst, 5)/1e3:,.0f}k "
          f"({np.percentile(worst_pct, 5)*100:.0f}%)")
    ladder = np.column_stack([np.full(PATHS, pv_payments(y0, 0))] +
                             [pv_payments(ylev[:, t - 1], t) for t in range(1, 7)])
    lchg = ladder[:, 1:] - ladder[:, :-1]           # (PATHS, 6): calendar years 2027..2032
    print(f"   ladder (marked to market): P(a given year shows a fall) = {(lchg[:, :6] < 0).mean()*100:.0f}%; "
          f"p5 single-year fall ${np.percentile(lchg[:, :6], 5)/1e3:,.0f}k; the payments' value falls by the same "
          f"dollars in the same year (funded ratio of the promise stays 1.00 by construction)")
    tot_chg = lchg + chg
    print(f"   whole statement: P(a given year 2027-2032 shows a fall) = {(tot_chg < 0).mean()*100:.0f}%; "
          f"P(at least one down year 2027-2032) = {(tot_chg < 0).any(1).mean()*100:.0f}%")
    # growth-first contrast (rejected plan): funded ratio = assets / value of the payments
    glide = (0.75, 0.75, 0.75, 0.75, 0.60, 0.40)
    v = np.full(PATHS, 300_000.0)
    fr_hand, fr_after = [], []
    for y in range(6):
        v = v * (1 + glide[y] * req[:, y] + (1 - glide[y]) * rbd[:, y])
        L = pv_payments(ylev[:, y], y + 1)
        fr_hand.append(v / L)                      # Dec 31 statement, before any Jan 1 deposit
        if y == 0:
            v = v + DEP
        fr_after.append(v / L)
    fr_hand, fr_after = np.array(fr_hand).T, np.array(fr_after).T
    print("  Rejected growth-first plan, for contrast (75% equity to 2030):")
    print(f"   P(Dec-2027 statement: assets on hand < value of the ten payments) = {(fr_hand[:, 0] < 1).mean()*100:.0f}% "
          f"(before the 2028 deposit)")
    print(f"   P(after the 2028 deposit, assets < value of the payments on some Jan 1 2028-2033) = "
          f"{(fr_after < 1).any(1).mean()*100:.1f}%; P(cushion under 5% at some point) = "
          f"{(fr_after < 1.05).any(1).mean()*100:.1f}%")


def section_range_width():
    req, rbd = draws(EQ)
    print("\n[4] M197 range Laura would announce in Jan 2031 = [bought floor, p90 or p95 of the 2033 total]")
    for w in (0.6, 1.0):
        g2 = (1 + w * req[:, 4] + (1 - w) * rbd[:, 4]) * (1 + w * req[:, 5] + (1 - w) * rbd[:, 5])
        for a in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
            fl = a * (1 + Y2) ** 2
            tot = fl + (1 - a) * g2
            r90, r95 = np.percentile(tot, 90) / fl, np.percentile(tot, 95) / fl
            p_above_mid = (tot > np.median(tot)).mean()
            print(f"  equity {int(w*100)}% of the unlocked part, lock share {int(a*100)}%: top/bottom "
                  f"{r90:.2f}x (p90 top) / {r95:.2f}x (p95 top); median 2033 total / floor {np.median(tot)/fl:.2f}x")
    sur, flo, _ = lock_early(req, rbd)
    s31 = flo / (0.8 * (1 + Y2) ** 2)
    for q, name in ((10, "weak"), (50, "median"), (90, "strong")):
        S = np.percentile(s31, q)
        F = 0.8 * S * (1 + Y2) ** 2
        g2 = (1 + 0.6 * req[:, 4] + 0.4 * rbd[:, 4]) * (1 + 0.6 * req[:, 5] + 0.4 * rbd[:, 5])
        tot = F + 0.2 * S * g2
        print(f"  2031 {name} state (sleeve p{q} = ${S/1e3:,.0f}k): floor ${F/1e3:,.0f}k, "
              f"p90 top ${np.percentile(tot, 90)/1e3:,.0f}k, p95 top ${np.percentile(tot, 95)/1e3:,.0f}k")
    p5, p95 = np.percentile(sur, 5), np.percentile(sur, 95)
    print(f"  2026 view of the 2033 surplus p5-p95: ${p5/1e3:,.0f}k-${p95/1e3:,.0f}k, ratio {p95/p5:.2f}x")


def section_case_words():
    txt = open("competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt", encoding="utf-8").read().lower()
    pats = {"certain*": r"\bcertain\w*", "credib*": r"\bcredib\w*", "confiden*": r"\bconfiden\w*",
            "protect*": r"\bprotect\w*", "flexib*": r"\bflexib\w*", "growth/grow*": r"\bgrow\w*",
            "risk*": r"\brisk\w*", "promis*": r"\bpromis\w*", "responsib*": r"\bresponsib\w*",
            "reliab*/reliable": r"\breliab\w*"}
    print("\n[5] M228 word counts in the official case text (VERIFIED-REPO-FILE, derived):")
    print("  " + "; ".join(f"{k} {len(re.findall(p, txt))}" for k, p in pats.items()))


if __name__ == "__main__":
    req, rbd = draws(EQ)
    sur, flo, _ = lock_early(req, rbd)
    print(f"[1] Reproduction of strategy_mc base, lock-early 60% sleeve equity: surplus p5/p50/p95 = {pct(sur)}; "
          f"floor p5/p50/p95 = {pct(flo)}")
    section_designs(EQ, "A: verified base inputs, JPM equities 6.70%, sleeve bonds JPM 4.00%")
    section_designs(EQ, "B: JPM equities 6.70%, sleeve bonds 5.00% (B10a-consistent, ASM)", bd=BD_CONSISTENT)
    section_designs(lp(0.052, 0.052 + (0.0794 - 0.0670)),
                    "C: Vanguard midpoint 5.2% equities (JPM vol kept), sleeve bonds 5.00% (ASM)", bd=BD_CONSISTENT)
    section_fat_tails()
    section_bad_years()
    section_range_width()
    section_case_words()
