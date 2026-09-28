"""E6 (Chief Strategist) - numbers behind research/insight_v1/phase_E/E6_final_spec.md and E6_our_strategy_one_page.md.

How to run (repo root, about 20 seconds, no network):
    .venv/bin/python research/insight_v1/scripts/E6_final_checks.py

WHAT IT DOES (every model output is a MODEL PROPERTY under the stated assumptions, never a forecast)
It re-uses the engines of E4_rival_numbers.py (which re-uses D6_behavioural_numbers.py: seed 20260927, 200,000 paths,
the same lognormal fit and random stream as the verified strategy_mc.py) and puts the two finalist designs on one basis:
 REC = the recommended design (E4's "dated" design, default rule): Jan 2027 the first deposit buys the ten payments
       (same ladder in both designs); Jan 2028 the second deposit first completes the ladder, then buys a Treasury that
       repays the deposit's dollar amount ($150,000) just before 2033 (the building minimum); everything left goes into
       one world stock fund, never rebalanced, until 1 Jan 2033. 2031: nothing is traded; the range announced is
       [minimum, minimum + 1/2 x the stock fund's value that day]; gift in 2033 = minimum + 1/2 x min(fund 2033,
       fund 2031) (capped at the top); everything else is kept (Laura's flexibility).
 ALT = the alternative (E1 timing, E1_change_proposals.md P5/P7): growth money 50% world stocks / 50% short Treasuries
       reset yearly 2028-2030; 1 Jan 2031 buy 80% of it as a 2-year Treasury (the bottom). Two ways to state the top:
       ALT-p90 = E1 as written (top = bottom + 1/2 x 90th-percentile 2-year growth of the rest; gift uncapped);
       ALT-cap = the same timing with REC's model-free top (top = bottom + 1/2 x the rest's value on 1 Jan 2031;
       gift = bottom + 1/2 x min(rest 2033, rest 2031)).

 [1] Reproduction: E1 P7 row (80/10/10) and E4 rival default, exactly as their files report.
 [2] Head-to-head on one basis: total facility+flexibility money 2033, bottom, top, gift, kept, P(top reached),
     whole-portfolio stock share each 1 January 2027-2032 and the six-year average, share of the likely gift already
     owned when she speaks in 2031.
 [3] Stress: bad 2028-2030 and bad 2031-2032 (bottom 10% of stock returns) for REC and ALT-cap.
 [4] A lower-return house (Vanguard VT-like blend 5.08% compound, JPM volatility kept; ASSUMPTION hybrid, as D2/AX1).
 [5] History: every 6-year window 1928-2025 (Damodaran, bond proxy as D3), raw and rescaled: totals, gift, bottom;
     and the share of windows in which each design's top is reached.
 [6] Costs: can the stock fund pay the costs? Fees of 0.25/0.5/1.0% a year charged on ALL assets but paid from the
     stock fund (the IPS cost principle: never from the payments or the minimum): chance the fund cannot cover them
     before 2033 and the median cost; versus fees charged on the stock fund only.
 [7] The WInS book for the recommended design (Laura's plan on 2 Jan 2028 scaled to $300,000), with no cap and with a
     25% single-security cap (ticket v1 section 3 hedge branch; IBTM one point under the cap), at the 2026-09-25 closes.
 [8] Rates fall before 1 Jan 2027 (-50/-100/-150bp, D1/D3 top-up table): the minimum, the stock fund and the 2033 total,
     with the five-year rate unchanged or lower in January 2028. Corrects E4 [7], which kept the 2027 leftover (about
     $8k) in the growth money although a fall that creates a gap leaves no leftover.

INPUTS and status labels
 - $292,264 ladder at 2027-01-01, leftover $7,736 (VERIFIED-REPO-FILE inputs, official_curve_pv.py; F-101, F-104);
   $294,387 real Nov-15 STRIPS ladder (VERIFIED-REPO-FILE inputs + ASSUMPTION method, D1/D3/S1) used only in [2]'s
   cost-share line.
 - $150,000 deposit at 2028-01-01 (VERIFIED-REPO-FILE, case p.2 L43-45).
 - JPM 2026 LTCMA AC World 7.00% compound / 8.28% arithmetic / 16.78% vol (VERIFIED-REPO-FILE, JPM matrix p.2);
   sleeve bonds 5.00% (ASSUMPTION, market-consistent, as E1/D6 case B/E4); Vanguard VT-like blend 5.08% (D2 blend of
   the VERIFIED-PRIMARY VCMM ranges; ASSUMPTION hybrid with JPM volatility).
 - Minimum bought 1 Jan 2028 at the 5-year par 4.98%; 2031 bottom at the 2-year par 4.81%; 2027 leftover in T-bills
   at 4.50% (VERIFIED-REPO-FILE curve 2026-09-25; ASSUMPTION that each holds on its date).
 - Forward values of the ladder 2028 $306,077 / 2031 $356,384 / 2033 $394,930 (VERIFIED-REPO-FILE inputs, F-106);
   2029/2030/2032 interpolated (ASSUMPTION arithmetic, as E4).
 - Damodaran histretSP 1928-2025 snapshot (VERIFIED-PRIMARY dataset page via D3_data_snapshot.py); bond proxy 50%
   T-bill + 50% 10-year (ASSUMPTION, D3).
 - Fund prices 2026-09-25 closes: IEF 90.00, TLH 93.38, VT 160.03 (VERIFIED-PRIMARY via ticket v1), IBTM 21.85
   (VERIFIED-PRIMARY via ticket v1 / E4, iShares), SPTL 24.27 (9/24, VERIFIED-PRIMARY via ticket v1).
 - No taxes; no fees except in [6]; i.i.d. lognormal annual returns (ASSUMPTION, as the verified strategy_mc.py).
 Every security named is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK.
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


E4 = load("E4_rival_numbers")
D6 = E4.D6
k, pct3 = E4.k, E4.pct3
LEFT, Y1, Y2, Y5 = E4.LEFT, E4.Y1, E4.Y2, E4.Y5
LADDER_YR = dict(E4.LADDER_YR)
LADDER_YR[2033] = E4.LADDER_2033


def alt_capped(req, rbd, w=0.5, a=0.8, s=0.5, dep=D6.DEP):
    """E1 timing (50/50 reset yearly 2028-30, 80% bought 1 Jan 2031 as a 2-year Treasury) with REC's model-free top:
    top = bottom + s x (value of the unlocked rest on 1 Jan 2031); gift = bottom + s x min(rest 2033, rest 2031)."""
    track = E4.sleeve_track(req, rbd, w=w, dep=dep)
    S = track[:, 4]
    bottom = a * S * (1 + Y2) ** 2
    rest31 = (1 - a) * S
    rest33 = rest31 * (1 + w * req[:, 4] + (1 - w) * rbd[:, 4]) * (1 + w * req[:, 5] + (1 - w) * rbd[:, 5])
    top = bottom + s * rest31
    gift = bottom + s * np.minimum(rest33, rest31)
    kept = rest33 - s * np.minimum(rest33, rest31)
    return dict(bottom=bottom, top=top, gift=gift, kept=kept, total=bottom + rest33, S=S, track=track,
                reached_top=float((rest33 >= rest31).mean()), rest31=rest31, rest33=rest33)


def shares_rec(req, dep=D6.DEP, y5=Y5):
    """Whole-portfolio stock share on 1 Jan 2027..2032 for REC (median across paths)."""
    G = LEFT * (1 + Y1) + dep
    a = min(1.0, dep / (1 + y5) ** 5 / G)
    pot = np.full(req.shape[0], (1 - a) * G)
    out = {2027: 0.0}
    for yi, yr in enumerate((2028, 2029, 2030, 2031, 2032)):
        fl = a * G * (1 + y5) ** yi
        out[yr] = float(np.median(pot / (LADDER_YR[yr] + fl + pot)))
        pot = pot * (1 + req[:, 1 + yi])
    return out


def shares_alt(req, rbd, w=0.5, a=0.8, dep=D6.DEP):
    """Whole-portfolio stock share on 1 Jan 2027..2032 for ALT (median across paths); 2027 leftover in T-bills."""
    track = E4.sleeve_track(req, rbd, w=w, dep=dep)
    out = {2027: 0.0}
    for yi, yr in enumerate((2028, 2029, 2030)):
        sl = track[:, 1 + yi] + (dep if yi == 0 else 0)
        out[yr] = float(np.median(w * sl / (LADDER_YR[yr] + sl)))
    S = track[:, 4]
    out[2031] = float(np.median(w * (1 - a) * S / (LADDER_YR[2031] + S)))
    rest32 = (1 - a) * S * (1 + w * req[:, 4] + (1 - w) * rbd[:, 4])
    out[2032] = float(np.median(w * rest32 / (LADDER_YR[2032] + a * S * (1 + Y2) + rest32)))
    return out


def fmt_shares(sh):
    avg = np.mean([sh[y] for y in range(2027, 2033)])
    return " ".join(f"{y} {sh[y] * 100:4.1f}%" for y in range(2027, 2033)) + f" | six-year average {avg * 100:.1f}%"


def section1(req, rbd):
    print("[1] Reproduction (must match E1 P7 row 1 and E4 [2] default row)")
    e = E4.e1_design(req, rbd)
    r = E4.rival_design(req)
    print(f"    E1 80/10/10 (ALT-p90): bottom med {k(np.median(e['bottom']))}, top med {k(np.median(e['top']))},"
          f" gift {pct3(e['gift'])}, kept {pct3(e['kept'])}, total {pct3(e['total'])}")
    print(f"    E4 rival default (REC): a={r['a']:.3f}, bottom {k(r['bottom'][0])}, top med {k(np.median(r['top']))},"
          f" gift {pct3(r['gift'])}, kept {pct3(r['kept'])}, total {pct3(r['total'])}")
    print("    (expected: E1 $167k / $192k; gift $151k / $188k / $238k; kept $16k / $21k / $29k; total $168k / $210k / $266k."
          " E4: bottom $150k; top $175k; gift $165k / $174k / $188k; kept $16k / $32k / $66k; total $182k / $207k / $250k)")
    return e, r


def section2(req, rbd):
    print("\n[2] Head-to-head on one basis (JPM ACWI 7.00%, bonds 5.00%, no fee)")
    rec = E4.rival_design(req)
    alt = alt_capped(req, rbd)
    p90 = E4.e1_design(req, rbd)
    for lab, d, rt in (("REC (2028 minimum = deposit, s=1/2, capped)", rec, rec["reached_top"]),
                       ("ALT-cap (2031 lock 80%, s=1/2, capped)", alt, alt["reached_top"]),
                       ("ALT-p90 (E1 as written, uncapped)", p90, p90["reached_top"])):
        print(f"    {lab:46s}| total {pct3(d['total'])} | bottom {pct3(d['bottom'])} | top med {k(np.median(d['top']))}"
              f" | gift {pct3(d['gift'])} | kept {pct3(d['kept'])} | P(top reached) {rt * 100:.0f}%")
    print("    whole-portfolio stock share on 1 Jan (median path):")
    print(f"      REC     : {fmt_shares(shares_rec(req))}")
    print(f"      ALT     : {fmt_shares(shares_alt(req, rbd))}")
    # share of the likely gift owned when she speaks (median state 2031)
    print(f"    share of the median 2033 gift already owned in 2031: REC {rec['bottom'][0] / np.median(rec['gift']) * 100:.0f}%;"
          f" ALT-cap {np.median(alt['bottom']) / np.median(alt['gift']) * 100:.0f}% (median bottom / median gift)")
    dif = alt["total"] - rec["total"]
    print(f"    same-path difference ALT-cap minus REC in total money: p5 {k(np.percentile(dif, 5))}, median"
          f" {k(np.median(dif))}, p95 {k(np.percentile(dif, 95))}; ALT-cap ahead in {np.mean(dif > 0) * 100:.0f}% of paths")
    print(f"    REC stock fund on 2 Jan 2028: {k(rec['pot28'][0])} = {rec['pot28'][0] / (E4.LADDER_2028 + LEFT * (1 + Y1) + D6.DEP) * 100:.1f}%"
          f" of all money; ALT stock money 2 Jan 2028 about {k(0.5 * (LEFT * (1 + Y1) + D6.DEP))}")
    print(f"    money Laura puts into the growth money: ${LEFT + D6.DEP:,.0f} (leftover + deposit, nominal);"
          f" REC paths ending below it: {np.mean(rec['total'] < LEFT + D6.DEP) * 100:.2f}%;"
          f" ALT-cap: {np.mean(alt['total'] < LEFT + D6.DEP) * 100:.2f}%")
    print(f"    payments' cost as a share of the $300,000 first deposit: exact-date {292_264 / 3e5 * 100:.1f}%,"
          f" Nov-15 STRIPS {294_387 / 3e5 * 100:.1f}% (2026-09-25 curve)")
    return rec, alt


def section3(req, rbd):
    print("\n[3] Stress (bottom 10% of 3-year stock returns 2028-30; bottom 10% of 2-year returns 2031-32)")
    g3 = (1 + req[:, 1]) * (1 + req[:, 2]) * (1 + req[:, 3])
    g2 = (1 + req[:, 4]) * (1 + req[:, 5])
    early, late = g3 <= np.percentile(g3, 10), g2 <= np.percentile(g2, 10)
    for lab, d in (("REC", E4.rival_design(req)), ("ALT-cap", alt_capped(req, rbd))):
        print(f"    {lab:8s}| bad 2028-30: bottom med {k(np.median(d['bottom'][early]))}, gift med"
              f" {k(np.median(d['gift'][early]))}, total med {k(np.median(d['total'][early]))}"
              f" | bad 2031-32: gift med {k(np.median(d['gift'][late]))}, total med {k(np.median(d['total'][late]))};"
              f" gift >= announced bottom in {np.mean(d['gift'][late] >= d['bottom'][late] - 1e-6) * 100:.0f}%")


def section4():
    print("\n[4] Lower-return house: Vanguard VT-like blend 5.08% compound (JPM vol kept; ASSUMPTION hybrid)")
    vg = D6.lp(0.0508, 0.0508 + (0.0828 - 0.0700))
    req, rbd = D6.draws(vg, bd=D6.BD_CONSISTENT)
    rec, alt = E4.rival_design(req), alt_capped(req, rbd)
    print(f"    REC     total {pct3(rec['total'])}; gift {pct3(rec['gift'])}; P(top reached) {rec['reached_top'] * 100:.0f}%")
    print(f"    ALT-cap total {pct3(alt['total'])}; gift {pct3(alt['gift'])}; bottom {pct3(alt['bottom'])};"
          f" P(top reached) {alt['reached_top'] * 100:.0f}%")


def section5():
    print("\n[5] History: every 6-year window 1928-2025 placed in 2027-2032")
    yrs, heq, hbd = E4.load_hist()
    for lab, eq, bd in (("raw", heq, hbd), ("rescaled to JPM ACWI 7.00% / bonds 5.00%", E4.rescale(heq, 0.07),
                                              E4.rescale(hbd, 0.05))):
        n = len(eq) - 5
        R = np.array([eq[i:i + 6] for i in range(n)])
        B = np.array([bd[i:i + 6] for i in range(n)])
        rec, alt = E4.rival_design(R), alt_capped(R, B)
        print(f"    -- {lab} ({n} windows)")
        for nm, d in (("REC", rec), ("ALT-cap", alt)):
            t = d["total"]
            print(f"       {nm:8s}| total worst {k(t.min())} (start {yrs[int(t.argmin())]}), p10 {k(np.percentile(t, 10))},"
                  f" median {k(np.median(t))} | gift worst {k(d['gift'].min())}, median {k(np.median(d['gift']))}"
                  f" | bottom worst {k(d['bottom'].min())} | top reached in {d['reached_top'] * 100:.0f}% of windows")


def section6(req, rbd):
    print("\n[6] Costs paid from the stock fund (IPS principle: never from the payments or the minimum)")
    G = LEFT * (1 + Y1) + D6.DEP
    a = D6.DEP / (1 + Y5) ** 5 / G
    base = E4.rival_design(req)
    for f in (0.0025, 0.005, 0.010):
        for on_all in (True, False):
            pot = np.full(req.shape[0], (1 - a) * G)
            short = np.zeros(req.shape[0], dtype=bool)
            for yi, yr in enumerate((2028, 2029, 2030, 2031, 2032)):
                fl = a * G * (1 + Y5) ** yi
                fee = f * (LADDER_YR[yr] + fl + pot) if on_all else f * pot
                short |= fee > pot
                pot = np.maximum(pot - fee, 0) * (1 + req[:, 1 + yi])
            tot = a * G * (1 + Y5) ** 5 + pot
            print(f"    fee {f * 100:.2f}% on {'all assets' if on_all else 'the stock fund only'}: stock fund cannot"
                  f" pay it in some year in {np.mean(short) * 100:.1f}% of paths; median total {k(np.median(tot))}"
                  f" ({k(np.median(tot) - np.median(base['total']))} vs no fee); p5 {k(np.percentile(tot, 5))}")


def section7():
    print("\n[7] WInS book for the recommended design: Laura's plan on 2 Jan 2028 scaled to $300,000 (9/25 closes)")
    G = LEFT * (1 + Y1) + D6.DEP
    lock = D6.DEP / (1 + Y5) ** 5
    tot = E4.LADDER_2028 + G
    px = {"IEF": 90.00, "TLH": 93.38, "SPTL": 24.27, "IBTM": 21.85, "VT": 160.03}
    wv = round((G - lock) / tot, 3)
    for lab, book in (("no cap", {"IEF": 0.235, "TLH": 0.425, "IBTM": round(lock / tot - 0.01, 3), "VT": wv}),
                      ("25% cap (ticket v1 s3 hedge branch)", {"IEF": 0.235, "TLH": 0.24, "SPTL": 0.185, "IBTM": 0.24,
                                                                "VT": wv})):
        cost, rows = 0, []
        for t, w in book.items():
            sh = int(300_000 * w // px[t])
            cost += sh * px[t]
            rows.append(f"{t} {w * 100:.1f}% ~{sh:,} sh")
        print(f"    {lab:36s}: " + " | ".join(rows) + f" | cash after {len(book)} x $25 ${300_000 - cost - 25 * len(book):,.0f}")
    print(f"    plan shares on 2 Jan 2028: ladder {E4.LADDER_2028 / tot * 100:.1f}% / minimum {lock / tot * 100:.1f}% /"
          f" stock fund {(G - lock) / tot * 100:.1f}% of {k(tot)}")


def section8(req):
    """Rates fall before 1 Jan 2027 (E6 correction to E4 [7]). When the ladder costs more than $300,000 there is no
    2027 leftover: the whole first deposit is in the ladder, and the January-2028 top-up (D1/D3 table, VRF inputs) comes
    out of the $150,000 deposit alone. E4 [7] subtracted the top-up from growth money that still held the grown 2027
    leftover, so it counted about $8k twice. Two conventions for the five-year rate in January 2028: unchanged at 4.98%
    (E4's convention) and lower by the same amount as the fall (the fall persists; ASSUMPTION parallel shift)."""
    print("\n[8] Rates fall before 1 Jan 2027: minimum and stock fund (corrects E4 [7], which kept the 2027 leftover)")
    lock_base = D6.DEP / (1 + Y5) ** 5
    base_exact = LEFT * (1 + Y1) + D6.DEP - lock_base
    base_strips = 5_613 * (1 + Y1) + D6.DEP - lock_base
    print(f"    no fall: stock fund {k(base_exact)} (exact-date ladder, as [2]); {k(base_strips)} on the Nov-15 STRIPS"
          f" basis of the top-up table (headroom $5,613)")
    for lab, shift, topup in (("-50bp", -0.005, 9_555), ("-100bp", -0.010, 25_711), ("-150bp", -0.015, 42_633)):
        e4_fund = LEFT * (1 + Y1) + D6.DEP - lock_base - topup
        for lab5, y5 in (("5-year stays 4.98%", Y5), ("5-year also lower", Y5 + shift)):
            cost = D6.DEP / (1 + y5) ** 5
            left = D6.DEP - topup
            if left >= cost:
                fund, minimum = left - cost, float(D6.DEP)
            else:
                fund, minimum = 0.0, left * (1 + y5) ** 5
            total = minimum + fund * np.prod(1 + req[:, 1:6], axis=1)
            print(f"    {lab:6s} ({lab5:18s}): top-up {k(topup)}; minimum {k(minimum)}; stock fund {k(fund)};"
                  f" facility+flexibility money 2033 p5/p50/p95 {pct3(total)}")
        print(f"           E4 [7] printed a stock fund of {k(max(e4_fund, 0))}"
              + ("" if e4_fund >= 0 else f" and a minimum of {k(150_000 + e4_fund * (1 + Y5) ** 5)}"))


if __name__ == "__main__":
    req, rbd = D6.draws(E4.JPM_ACWI, bd=D6.BD_CONSISTENT)
    section1(req, rbd)
    section2(req, rbd)
    section3(req, rbd)
    section4()
    section5()
    section6(req, rbd)
    section7()
    section8(req)
