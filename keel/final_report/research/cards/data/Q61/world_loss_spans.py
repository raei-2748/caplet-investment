"""Card Q61 (Mon 16 Nov 2026): how often world shares lost money over 3-6 year spans. Keel arithmetic.

Run from the repo root:  python3 -I keel/final_report/research/cards/data/Q61/world_loss_spans.py
Writes results_world_loss_spans.json next to this script. Reads only files in this folder and fall40.py's
annual MSCI World table (imported as text, not executed). Changes no other file.

Inputs (all in this folder):
- msci_world_acwi_gross_usd_monthly.csv: MSCI World (code 990100) and MSCI ACWI (892400), USD, gross total return,
  month-end levels 29 Dec 2000 to 30 Oct 2026, read at source on 16 Nov 2026 from MSCI's end-of-day service
  (app2.msci.com .../getLevelDataForGraph, index_variant=GRTR, END_OF_MONTH). The service refuses start dates before
  1 Jan 1997 and returned nothing before 29 Dec 2000.
- cpi_u_nsa_monthly.csv: US CPI-U, all items, not seasonally adjusted (BLS CUUR0000SA0 = FRED CPIAUCNS). Dec 1969 to
  Aug 2026 from the repo mirror (keel/models/data/cpi_us_monthly.csv), spot-checked equal to FRED on 16 Nov 2026 at
  Dec 1969, Jan 1970, Dec 2000, Jan 2001 and Jun 2025 to Aug 2026; Sep and Oct 2026 from FRED. October 2025 was never
  published (US government shutdown); it is filled here by the geometric mean of September and November 2025.
- MSCI World gross calendar-year returns 1970-2025: the table in keel/final_report/numbers/fall40.py (2012-2025 read
  at MSCI's factsheet; 1970-2011 from Wikipedia, UNVERIFIED at MSCI). This script checks 2001-2025 against the
  monthly MSCI levels above, so only 1970-2000 stays UNVERIFIED.

Conventions: a span starts at one month-end and ends n months later (overlapping spans, every month). "Loss" = total
return below zero over the whole span, point to point. "Real" = deflated by US CPI-U of the start and end months.
Gross returns are before withholding tax and before any fund fee (VT tracks a different index, FTSE Global All Cap,
net of withholding, and charges 0.06%).
"""
import csv
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *[".."] * 6))


def load_msci():
    dates, world, acwi = [], [], []
    with open(os.path.join(HERE, "msci_world_acwi_gross_usd_monthly.csv")) as f:
        for r in csv.DictReader(f):
            dates.append(r["date"])
            world.append(float(r["msci_world_gross_usd"]))
            acwi.append(float(r["msci_acwi_gross_usd"]))
    return dates, world, acwi


def load_cpi():
    cpi = {}
    with open(os.path.join(HERE, "cpi_u_nsa_monthly.csv")) as f:
        for r in csv.DictReader(f):
            cpi[r["month"]] = float(r["cpi_u_nsa"])
    cpi["2025-10"] = math.sqrt(cpi["2025-09"] * cpi["2025-11"])  # never published; geometric fill
    return cpi


def load_annual():
    text = open(os.path.join(ROOT, "keel/final_report/numbers/fall40.py")).read()
    block = text[text.index("MSCI_WORLD_GROSS = {"):]
    block = block[:block.index("}") + 1]
    return {int(y): float(v) for y, v in re.findall(r"(\d{4}):\s*(-?\d+\.\d+)", block)}


def pct(xs, p):
    s = sorted(xs)
    k = (len(s) - 1) * p / 100.0
    lo, hi = math.floor(k), math.ceil(k)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def spans(dates, level, n, cpi=None):
    out = []
    for i in range(len(level) - n):
        j = i + n
        r = level[j] / level[i] - 1
        if cpi is not None:
            r = (1 + r) * cpi[dates[i][:7]] / cpi[dates[j][:7]] - 1
        # largest fall from a month-end peak inside the span (monthly points only)
        peak, mdd = level[i], 0.0
        for k in range(i, j + 1):
            peak = max(peak, level[k])
            mdd = min(mdd, level[k] / peak - 1)
        out.append((dates[i], dates[j], r, mdd))
    return out


def summarise(sp, label):
    rs = [s[2] for s in sp]
    worst = min(sp, key=lambda s: s[2])
    best = max(sp, key=lambda s: s[2])
    losses = [s for s in sp if s[2] < 0]
    # group overlapping losing spans into episodes by end month runs
    episodes, cur = [], None
    for s in sp:
        if s[2] < 0:
            if cur and months_between(cur[-1][0], s[0]) == 1:
                cur.append(s)
            else:
                cur = [s]
                episodes.append(cur)
        else:
            cur = None
    eps = [{"starts": f"{e[0][0][:7]} to {e[-1][0][:7]}", "count": len(e),
            "worst": round(min(x[2] for x in e) * 100, 1),
            "worst_start_end": [min(e, key=lambda x: x[2])[0][:7], min(e, key=lambda x: x[2])[1][:7]]}
           for e in episodes]
    return {
        "label": label,
        "spans": len(sp),
        "first_start": sp[0][0][:7], "last_start": sp[-1][0][:7],
        "share_with_loss": round(len(losses) / len(sp), 4),
        "share_down_10pct_or_more": round(sum(r <= -0.10 for r in rs) / len(sp), 4),
        "share_down_20pct_or_more": round(sum(r <= -0.20 for r in rs) / len(sp), 4),
        "share_down_30pct_or_more": round(sum(r <= -0.30 for r in rs) / len(sp), 4),
        "share_down_40pct_or_more": round(sum(r <= -0.40 for r in rs) / len(sp), 4),
        "share_containing_40pct_fall_from_peak": round(sum(s[3] <= -0.40 for s in sp) / len(sp), 4),
        "worst_pct": round(worst[2] * 100, 1), "worst_start_end": [worst[0][:7], worst[1][:7]],
        "best_pct": round(best[2] * 100, 1), "best_start_end": [best[0][:7], best[1][:7]],
        "p5_p10_p25_p50_pct": [round(pct(rs, p) * 100, 1) for p in (5, 10, 25, 50)],
        "loss_episodes": eps,
    }


def months_between(a, b):
    ya, ma = int(a[:4]), int(a[5:7])
    yb, mb = int(b[:4]), int(b[5:7])
    return (yb - ya) * 12 + (mb - ma)


def annual_spans(ann, cpi, n, real):
    yrs = sorted(ann)
    g = [1 + ann[y] / 100 for y in yrs]
    out = []
    for i in range(len(yrs) - n + 1):
        r = 1.0
        for k in range(i, i + n):
            r *= g[k]
        if real:
            r *= cpi[f"{yrs[i] - 1}-12"] / cpi[f"{yrs[i + n - 1]}-12"]
        out.append((yrs[i], yrs[i + n - 1], r - 1))
    rs = [x[2] for x in out]
    worst = min(out, key=lambda x: x[2])
    return {"spans": len(out), "first": f"{yrs[0]}-{yrs[n - 1]}", "last": f"{out[-1][0]}-{out[-1][1]}",
            "share_with_loss": round(sum(r < 0 for r in rs) / len(rs), 4),
            "count_with_loss": sum(r < 0 for r in rs),
            "losing_spans": [f"{a}-{b} {round(r * 100, 1)}%" for a, b, r in out if r < 0],
            "share_down_20pct_or_more": round(sum(r <= -0.2 for r in rs) / len(rs), 4),
            "share_down_40pct_or_more": round(sum(r <= -0.4 for r in rs) / len(rs), 4),
            "worst": f"{worst[0]}-{worst[1]} {round(worst[2] * 100, 1)}%",
            "p5_p10_p50_pct": [round(pct(rs, p) * 100, 1) for p in (5, 10, 50)]}


def main():
    dates, world, acwi = load_msci()
    cpi = load_cpi()
    ann = load_annual()

    # checks: calendar years 2001-2025 from monthly levels against the annual table; World against ACWI each month
    checks = {}
    dec = {d[:4]: i for i, d in enumerate(dates) if d[5:7] == "12"}
    diffs = []
    for y in range(2001, 2026):
        r = world[dec[str(y)]] / world[dec[str(y - 1)]] - 1
        diffs.append((y, round(r * 100, 2), ann[y]))
    checks["annual_2001_2025_from_monthly_vs_table_max_abs_diff_pts"] = max(abs(a - b) for _, a, b in diffs)
    mw = [world[i + 1] / world[i] - 1 for i in range(len(world) - 1)]
    ma = [acwi[i + 1] / acwi[i] - 1 for i in range(len(acwi) - 1)]
    gap = max(abs(a - b) for a, b in zip(mw, ma))
    checks["largest_monthly_gap_world_vs_acwi_pts"] = round(gap * 100, 2)
    checks["largest_monthly_move_world_pct"] = [round(min(mw) * 100, 2), round(max(mw) * 100, 2)]
    # ACWI gross calendar years against MSCI's ACWI factsheet (gross, 30 Oct 2026; 2011 from the 28 Nov 2025 edition)
    acwi_factsheet = {2011: -6.86, 2012: 16.80, 2013: 23.44, 2014: 4.71, 2015: -1.84, 2016: 8.48, 2017: 24.62,
                      2018: -8.93, 2019: 27.30, 2020: 16.82, 2021: 19.04, 2022: -17.96, 2023: 22.81, 2024: 18.02,
                      2025: 22.87}
    checks["acwi_2011_2025_from_monthly_vs_factsheet_max_abs_diff_pts"] = round(max(
        abs((acwi[dec[str(y)]] / acwi[dec[str(y - 1)]] - 1) * 100 - v) for y, v in acwi_factsheet.items()), 3)
    # ACWI 3-year annualized to 30 Oct 2026 against the factsheet's 22.82%
    i_end = dates.index("2026-10-30")
    checks["acwi_3y_annualized_to_oct2026_pct_vs_factsheet_22.82"] = round(
        ((acwi[i_end] / acwi[i_end - 36]) ** (1 / 3) - 1) * 100, 2)

    res = {"card": "Q61", "run": "Mon 16 Nov 2026 (Sydney)", "label": "Keel arithmetic", "checks": checks,
           "monthly_msci_2000_2026": {}, "annual_msci_world_1970_2025": {}}

    # History mapped onto NUMBERS 8p's steps for the stated top (Sun 15 Nov evening register, rates at today's
    # forwards; VT's value at the move against its January 2028 cost): +36.4% or more -> $120,000 or more;
    # +4.8% -> $115,000; down to -26.7% -> $110,000; down to -58.2% -> $105,000; down to -89.8% -> $100,000.
    # Keel arithmetic on register steps: it says which step a past 3-year world return would have landed on, never
    # a plan figure of its own. VT before its 0.06% fee; gross index before withholding tax.
    def step(r):
        if r >= 0.364:
            return "120000_or_more"
        if r >= 0.048:
            return "115000"
        if r >= -0.267:
            return "110000"
        if r >= -0.582:
            return "105000"
        if r >= -0.898:
            return "100000"
        return "95000"

    steps = {}
    for name, lev in (("MSCI World gross USD, monthly starts 2000-12 to 2023-10", world),
                      ("MSCI ACWI gross USD, monthly starts 2000-12 to 2023-10", acwi)):
        rs = [s[2] for s in spans(dates, lev, 36)]
        steps[name] = {k: round(sum(step(r) == k for r in rs) / len(rs), 4)
                       for k in ("120000_or_more", "115000", "110000", "105000", "100000", "95000")}
        steps[name]["spans"] = len(rs)
    yrs = sorted(ann)
    rs = []
    for i in range(len(yrs) - 2):
        r = (1 + ann[yrs[i]] / 100) * (1 + ann[yrs[i + 1]] / 100) * (1 + ann[yrs[i + 2]] / 100) - 1
        rs.append(r)
    steps["MSCI World gross USD, calendar 3-year spans 1970-72 to 2023-25"] = dict(
        {k: round(sum(step(r) == k for r in rs) / len(rs), 4)
         for k in ("120000_or_more", "115000", "110000", "105000", "100000", "95000")}, spans=len(rs))
    res["history_on_8p_steps_3y"] = steps
    for name, lev in (("MSCI World gross USD", world), ("MSCI ACWI gross USD", acwi)):
        for n in (36, 48, 60, 72):
            for real in (False, True):
                key = f"{name} | {n // 12}y | {'real' if real else 'nominal'}"
                res["monthly_msci_2000_2026"][key] = summarise(spans(dates, lev, n, cpi if real else None), key)
    # January starts only (Laura's VT is bought in January): month-end December to month-end December
    for name, lev in (("MSCI ACWI gross USD", acwi), ("MSCI World gross USD", world)):
        for n in (3, 4, 5, 6):
            for real in (False, True):
                idx = [i for i, d in enumerate(dates) if d[5:7] == "12"]
                pts = []
                for a in idx:
                    b = a + 12 * n
                    if b < len(lev):
                        r = lev[b] / lev[a] - 1
                        if real:
                            r = (1 + r) * cpi[dates[a][:7]] / cpi[dates[b][:7]] - 1
                        pts.append((int(dates[a][:4]) + 1, int(dates[b][:4]), r))
                key = f"{name} | Jan starts | {n}y | {'real' if real else 'nominal'}"
                res["monthly_msci_2000_2026"][key] = {
                    "spans": len(pts), "losing": [f"{s}-{e} {round(r * 100, 1)}%" for s, e, r in pts if r < 0],
                    "share_with_loss": round(sum(r < 0 for _, _, r in pts) / len(pts), 4)}
    for n in (3, 4, 5, 6):
        for real in (False, True):
            res["annual_msci_world_1970_2025"][f"{n}y | {'real' if real else 'nominal'}"] = annual_spans(ann, cpi, n, real)
    # the 2000-02 span that the monthly series misses, from the annual table: Dec 1999 to Dec 2002
    g = (1 + ann[2000] / 100) * (1 + ann[2001] / 100) * (1 + ann[2002] / 100) - 1
    res["annual_msci_world_1970_2025"]["2000_2002_nominal_pct"] = round(g * 100, 1)
    res["annual_msci_world_1970_2025"]["2000_2002_real_pct"] = round(((1 + g) * cpi["1999-12"] / cpi["2002-12"] - 1) * 100, 1)
    # US inflation over the monthly sample, for the nominal-real gap
    res["us_cpi_change_dec2000_oct2026_pct"] = round((cpi["2026-10"] / cpi["2000-12"] - 1) * 100, 1)
    with open(os.path.join(HERE, "results_world_loss_spans.json"), "w") as f:
        json.dump(res, f, indent=1)
    return res


if __name__ == "__main__":
    r = main()
    print(json.dumps(r["checks"]))
    for k, v in r["monthly_msci_2000_2026"].items():
        if "Jan starts" in k:
            print(k, v["share_with_loss"], v["losing"])
        else:
            print(k, v["spans"], v["share_with_loss"], v["share_down_20pct_or_more"], v["share_down_40pct_or_more"],
                  v["share_containing_40pct_fall_from_peak"], v["worst_pct"], v["worst_start_end"],
                  v["p5_p10_p25_p50_pct"], [(e["starts"], e["worst"]) for e in v["loss_episodes"]])
    for k, v in r["annual_msci_world_1970_2025"].items():
        print(k, v)
    print("CPI change", r["us_cpi_change_dec2000_oct2026_pct"])
