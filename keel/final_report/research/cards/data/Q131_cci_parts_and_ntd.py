"""Q131: inside Taiwan's construction cost index - do the materials and labour parts answer the Taiwan dollar?

Keel arithmetic for card Q131 (Wed 18 Nov 2026, Sydney). Research notes, not report prose; no plan figure is made here.

Data (all in Q131_cci_parts_ntd_monthly.csv, one row a month, Jan 1991 to Oct 2026):
  * DGBAS construction cost index (營造工程物價指數, 2021 = 100, linked series), total, materials (材料類), services
    (勞務類), wages (工資類), equipment rent, six material groups, rebar / section steel / steel plate (from 2003) and the
    building-construction index with its two parts. Read at source on 17 Nov 2026 (US date) from DGBAS's statistical
    database, funid A030502015, CSV output (nstatdb.dgbas.gov.tw). The total agrees with card Q10e's read for all 429
    months it had.
  * DGBAS import price index in US dollars (進口物價基本分類指數, 美元計價, funid A030301015): total, energy, base
    metals, copper (from 1991); minerals, stone-and-cement, iron and steel, steel products (from 1998). Same read.
  * NT$ per US$: FRED EXTAUS monthly averages, the repo mirror keel/models/data/twd_per_usd_monthly.csv (verified for
    all 516 months, NUMBERS 8l) plus Oct 2026 (32.2695) read at FRED on 17 Nov 2026.

Conventions:
  * "NT$ move" over a window = fx_start / fx_end - 1: the % more US dollars a fixed NT$ bill needs at the end (NUMBERS 8j,
    card Q10e). Positive = a stronger Taiwan dollar.
  * Index moves are simple % changes over the same months unless a line says "log".
  * "Response" = OLS slope of the index's log change on the NT$ move's log change: % change in the index for each 1%
    stronger NT$. Negative = the index falls when the NT$ strengthens (the claim's mechanism).
  * Newey-West standard errors (lag = window - 1) for overlapping windows.

Run: python3 -I keel/final_report/research/cards/data/Q131_cci_parts_and_ntd.py   (a second or two)
"""
import csv
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = list(csv.DictReader(open(os.path.join(HERE, "Q131_cci_parts_ntd_monthly.csv"), encoding="utf-8")))
MONTHS = [r["month"] for r in ROWS]
IDX = {m: i for i, m in enumerate(MONTHS)}


def series(name):
    return np.array([float(r[name]) if r[name] != "" else np.nan for r in ROWS])


FX = series("twd_per_usd")
S = {k: series(k) for k in ROWS[0] if k not in ("month", "twd_per_usd")}
N = len(MONTHS)
LNFX = np.log(FX)

# DGBAS weights, 2021 base, per mille (Price Statistics Monthly, Table 7-1 footnote "以110年結構為權數")
W = {"materials": 659.24, "cement": 141.07, "sand": 21.14, "brick": 13.91, "metal": 233.42, "timber": 24.00,
     "plastics": 19.55, "paints": 9.30, "electrical": 120.19, "asphalt": 19.07, "misc": 57.58,
     "services": 340.76, "wages": 238.32, "equip_rent": 102.44}
W_BLD = {"materials": 645.67, "services": 354.33}


def ntd_move(a, b):
    return FX[a] / FX[b] - 1


def nw_ols(y, X, lag):
    """OLS with Newey-West (Bartlett) standard errors. X includes a constant column."""
    ok = ~np.isnan(y) & ~np.isnan(X).any(axis=1)
    y, X = y[ok], X[ok]
    n, k = X.shape
    XtXi = np.linalg.inv(X.T @ X)
    b = XtXi @ X.T @ y
    e = y - X @ b
    S0 = (X * e[:, None]).T @ (X * e[:, None])
    for L in range(1, lag + 1):
        wgt = 1 - L / (lag + 1)
        G = (X[L:] * e[L:, None]).T @ (X[:-L] * e[:-L, None])
        S0 += wgt * (G + G.T)
    V = XtXi @ S0 @ XtXi
    r2 = 1 - (e @ e) / ((y - y.mean()) @ (y - y.mean()))
    return b, np.sqrt(np.diag(V)), n, r2


def window_logs(name, h, offset=0, start="1991-01"):
    """Pairs (NT$ log move over t..t+h, index log change over t+offset..t+offset+h), t from start."""
    x = S[name]
    xs, ys, ts = [], [], []
    for t in range(IDX[start], N):
        a, b = t + offset, t + offset + h
        if t + h >= N or b >= N or a < 0:
            continue
        if np.isnan(x[a]) or np.isnan(x[b]):
            continue
        xs.append(LNFX[t] - LNFX[t + h])  # >0 = NT$ stronger
        ys.append(math.log(x[b] / x[a]))
        ts.append(MONTHS[t])
    return np.array(xs), np.array(ys), ts


def pr(*a):
    print(*a)


def section_weights():
    pr("== 1. Weights (DGBAS 2021 base, per mille) ==")
    imp = W["metal"] + W["asphalt"] + W["electrical"] + W["plastics"]
    pr(f"materials {W['materials']}, services {W['services']} (wages {W['wages']}, equipment rent {W['equip_rent']})")
    pr(f"metal {W['metal']}, cement group {W['cement']}, electrical {W['electrical']}, asphalt {W['asphalt']}, "
       f"plastics {W['plastics']}, sand {W['sand']}, misc {W['misc']}, timber {W['timber']}, brick {W['brick']}, paints {W['paints']}")
    pr(f"groups priced mostly off world US$ inputs (metal + asphalt + electrical + plastics): {imp:.2f} per mille = "
       f"{imp/10:.1f}% of the index; metal alone {W['metal']/10:.1f}%; wages {W['wages']/10:.1f}%")
    pr(f"building construction: materials {W_BLD['materials']}, services {W_BLD['services']}")


def section_latest():
    pr("\n== 2. Latest year (Oct 2026 on Oct 2025) and since Dec 2025 ==")
    a, b = IDX["2025-10"], IDX["2026-10"]
    d = IDX["2025-12"]
    for k in ["cci_total", "cci_materials", "cci_metal", "cci_rebar", "cci_cement", "cci_asphalt", "cci_electrical",
              "cci_services", "cci_wages", "cci_equip_rent", "bld_total", "bld_materials", "bld_services",
              "ipi_usd_base_metals", "ipi_usd_iron_steel", "ipi_usd_energy"]:
        x = S[k]
        pr(f"{k:22s} Oct25 {x[a]:7.2f} Oct26 {x[b]:7.2f}  y/y {100*(x[b]/x[a]-1):+6.2f}%  Dec25->Oct26 {100*(x[b]/x[d]-1):+6.2f}%")
    pr(f"NT$ move Oct25->Oct26: {100*ntd_move(a,b):+.2f}% (fx {FX[a]:.4f} -> {FX[b]:.4f})")
    # contributions to the y/y total change, approx with 2021 weights x level relative to total
    tot = S["cci_total"]
    for k, w in [("cci_materials", W["materials"]), ("cci_services", W["services"]), ("cci_wages", W["wages"]),
                 ("cci_equip_rent", W["equip_rent"]), ("cci_metal", W["metal"])]:
        x = S[k]
        c = (w / 1000) * (x[b] - x[a]) / tot[a] * 100
        pr(f"  approx contribution of {k} to the total's y/y: {c:+.2f} points")


def section_corr():
    pr("\n== 3. Correlation and response of each part to the NT$, overlapping windows (since 1991 unless named) ==")
    names = ["cci_total", "cci_materials", "cci_metal", "cci_rebar", "cci_cement", "cci_asphalt", "cci_electrical",
             "cci_sand", "cci_services", "cci_wages", "cci_equip_rent", "bld_total", "bld_materials", "bld_services"]
    for h in (6, 12, 24):
        pr(f"-- window {h} months; offset = index window starts L months after the currency window --")
        for name in names:
            line = f"{name:16s}"
            for off in (0, 6, 12):
                xs, ys, _ = window_logs(name, h, off)
                c = np.corrcoef(xs, ys)[0, 1]
                X = np.column_stack([np.ones_like(xs), xs])
                b, se, n, _ = nw_ols(ys, X, h - 1)
                line += f" | L{off:2d}: r {c:+.2f} resp {b[1]:+.2f} (se {se[1]:.2f}) n{n}"
            pr(line)
    pr("-- same, 12-month windows, two eras --")
    for start, end in (("1991-01", "2005-12"), ("2006-01", "2025-10")):
        for name in ["cci_materials", "cci_metal", "cci_services", "cci_wages", "cci_total"]:
            xs, ys, ts = window_logs(name, 12, 0, start)
            keep = np.array([t <= end for t in ts])
            xs, ys = xs[keep], ys[keep]
            c = np.corrcoef(xs, ys)[0, 1]
            X = np.column_stack([np.ones_like(xs), xs])
            b, se, n, _ = nw_ols(ys, X, 11)
            pr(f"  {start}..{end} {name:14s} r {c:+.2f} resp {b[1]:+.2f} (se {se[1]:.2f}) n{n}")


def section_partial():
    pr("\n== 4. Holding world US$ prices fixed: 12-month log changes, materials on NT$ move + import prices in US$ ==")
    h = 12
    out = {}
    for name, ctrl in [("cci_materials", ["ipi_usd_base_metals", "ipi_usd_energy"]),
                       ("cci_metal", ["ipi_usd_base_metals"]),
                       ("cci_asphalt", ["ipi_usd_energy"]),
                       ("cci_wages", ["ipi_usd_base_metals", "ipi_usd_energy"]),
                       ("cci_total", ["ipi_usd_base_metals", "ipi_usd_energy"])]:
        for off in (0, 6):
            ys, xs, cs = [], [], []
            for t in range(N):
                a, b = t + off, t + off + h
                if b >= N:
                    continue
                vals = [S[name][a], S[name][b]] + [S[c][t] for c in ctrl] + [S[c][t + h] for c in ctrl]
                if any(np.isnan(v) for v in vals):
                    continue
                ys.append(math.log(S[name][b] / S[name][a]))
                xs.append(LNFX[t] - LNFX[t + h])
                cs.append([math.log(S[c][t + h] / S[c][t]) for c in ctrl])
            ys, xs, cs = np.array(ys), np.array(xs), np.array(cs)
            X = np.column_stack([np.ones_like(xs), xs, cs])
            b, se, n, r2 = nw_ols(ys, X, h - 1)
            # same without controls on the same sample
            b0, se0, _, r20 = nw_ols(ys, np.column_stack([np.ones_like(xs), xs]), h - 1)
            out[(name, off)] = (b, se)
            pr(f"{name:14s} L{off:2d}: NT$ resp {b[1]:+.2f} (se {se[1]:.2f}) with " +
               ", ".join(f"{c} {b[2+i]:+.2f} (se {se[2+i]:.2f})" for i, c in enumerate(ctrl)) +
               f"; R2 {r2:.2f}; without controls {b0[1]:+.2f} (se {se0[1]:.2f}), R2 {r20:.2f}; n{n}")
    # world US$ import prices against the NT$: the confound
    for c in ["ipi_usd_base_metals", "ipi_usd_energy", "ipi_usd_total"]:
        xs, ys = [], []
        for t in range(N - 12):
            if np.isnan(S[c][t]) or np.isnan(S[c][t + 12]):
                continue
            xs.append(LNFX[t] - LNFX[t + 12])
            ys.append(math.log(S[c][t + 12] / S[c][t]))
        pr(f"confound: 12-month corr of NT$ move with {c} (US$ prices) {np.corrcoef(xs, ys)[0,1]:+.2f}")
    return out


def section_dlag():
    pr("\n== 5. Monthly distributed lag (0..12): materials and wages on NT$ and US$ import prices; cumulative response ==")
    K = 12
    for name, ctrl in [("cci_materials", ["ipi_usd_base_metals", "ipi_usd_energy"]), ("cci_metal", ["ipi_usd_base_metals"]),
                       ("cci_wages", ["ipi_usd_base_metals", "ipi_usd_energy"])]:
        rows_y, rows_X = [], []
        for t in range(K + 1, N):
            vals = [S[name][t], S[name][t - 1]] + [S[c][t - k] for c in ctrl for k in range(K + 2)]
            if any(np.isnan(v) for v in vals):
                continue
            y = math.log(S[name][t] / S[name][t - 1])
            x = [-(LNFX[t - k] - LNFX[t - k - 1]) for k in range(K + 1)]  # >0 = NT$ stronger that month
            for c in ctrl:
                x += [math.log(S[c][t - k] / S[c][t - k - 1]) for k in range(K + 1)]
            rows_y.append(y)
            rows_X.append([1.0] + x)
        y, X = np.array(rows_y), np.array(rows_X)
        b, se, n, r2 = nw_ols(y, X, 12)
        cum6, cum12 = b[1:8].sum(), b[1:14].sum()
        # se of the cumulative sums from the full covariance: recompute
        ok = slice(None)
        XtXi = np.linalg.inv(X.T @ X)
        e = y - X @ b
        S0 = (X * e[:, None]).T @ (X * e[:, None])
        for L in range(1, 13):
            G = (X[L:] * e[L:, None]).T @ (X[:-L] * e[:-L, None])
            S0 += (1 - L / 13) * (G + G.T)
        V = XtXi @ S0 @ XtXi
        g6 = np.zeros(len(b)); g6[1:8] = 1
        g12 = np.zeros(len(b)); g12[1:14] = 1
        pr(f"{name:14s} cumulative response to a 1% stronger NT$: 0-6 months {cum6:+.3f} (se {math.sqrt(g6@V@g6):.3f}), "
           f"0-12 months {cum12:+.3f} (se {math.sqrt(g12@V@g12):.3f}); n{n}, R2 {r2:.2f}")


def episodes(h=24, thresh=0.10):
    pr(f"\n== 6. Every {h}-month window with the NT$ {int(thresh*100)}% or more stronger: what the parts did ==")
    wins = []
    for t in range(N - h):
        mv = ntd_move(t, t + h)
        if mv >= thresh:
            wins.append(t)
    pr(f"{len(wins)} of {N - h} windows (since Jan 1991)")
    # cluster into episodes by contiguous start months
    eps, cur = [], []
    for t in wins:
        if cur and t - cur[-1] > 1:
            eps.append(cur); cur = []
        cur.append(t)
    if cur:
        eps.append(cur)

    def chg(k, a, b):
        x = S[k]
        if b >= N or np.isnan(x[a]) or np.isnan(x[b]):
            return float("nan")
        return 100 * (x[b] / x[a] - 1)

    agg = {k: [] for k in ["cci_total", "cci_materials", "cci_metal", "cci_services", "cci_wages", "bld_total", "usd_cost",
                            "mat_next12", "wag_next12", "tot_next12", "ntd_next12"]}
    for e in eps:
        best = max(e, key=lambda t: ntd_move(t, t + h))
        a, b = best, best + h
        usd = 100 * ((S["cci_total"][b] / S["cci_total"][a]) * (FX[a] / FX[b]) - 1)
        pr(f"episode starts {MONTHS[e[0]]}..{MONTHS[e[-1]]} ({len(e)} windows); strongest {MONTHS[a]}->{MONTHS[b]}: "
           f"NT$ {100*ntd_move(a,b):+.1f}% | total {chg('cci_total',a,b):+.1f}% materials {chg('cci_materials',a,b):+.1f}% "
           f"metal {chg('cci_metal',a,b):+.1f}% services {chg('cci_services',a,b):+.1f}% wages {chg('cci_wages',a,b):+.1f}% "
           f"building {chg('bld_total',a,b):+.1f}% | US$ cost of a fixed NT$ budget {usd:+.1f}% | "
           f"next 12 months: NT$ {100*ntd_move(b,b+12) if b+12<N else float('nan'):+.1f}% materials {chg('cci_materials',b,b+12):+.1f}% "
           f"wages {chg('cci_wages',b,b+12):+.1f}% total {chg('cci_total',b,b+12):+.1f}%")
    for t in wins:
        a, b = t, t + h
        agg["cci_total"].append(chg("cci_total", a, b))
        agg["cci_materials"].append(chg("cci_materials", a, b))
        agg["cci_metal"].append(chg("cci_metal", a, b))
        agg["cci_services"].append(chg("cci_services", a, b))
        agg["cci_wages"].append(chg("cci_wages", a, b))
        agg["bld_total"].append(chg("bld_total", a, b))
        agg["usd_cost"].append(100 * ((S["cci_total"][b] / S["cci_total"][a]) * (FX[a] / FX[b]) - 1))
        agg["mat_next12"].append(chg("cci_materials", b, b + 12))
        agg["wag_next12"].append(chg("cci_wages", b, b + 12))
        agg["tot_next12"].append(chg("cci_total", b, b + 12))
    pr("all such windows, median [min, max]:")
    for k, v in agg.items():
        v = np.array([x for x in v if not math.isnan(x)])
        if len(v):
            pr(f"  {k:14s} median {np.median(v):+6.1f}%  [{v.min():+6.1f}%, {v.max():+6.1f}%]  falls in {int((v<0).sum())} of {len(v)}")
    # comparison: all other windows
    oth = [t for t in range(N - h) if t not in set(wins)]
    for k in ["cci_materials", "cci_wages", "cci_total"]:
        v = np.array([chg(k, t, t + h) for t in oth])
        pr(f"  other windows {k:14s} median {np.median(v):+6.1f}%  falls in {int((v<0).sum())} of {len(v)}")
    return wins


def section_falls():
    pr("\n== 7. Which part ever falls? 12-month changes, Jan 1992 to Oct 2026 ==")
    for k in ["cci_total", "cci_materials", "cci_metal", "cci_cement", "cci_sand", "cci_asphalt", "cci_services",
              "cci_wages", "cci_equip_rent", "bld_services"]:
        x = S[k]
        yoy = np.array([100 * (x[t] / x[t - 12] - 1) for t in range(12, N)])
        mn = int(np.argmin(yoy)) + 12
        mx = int(np.argmax(yoy)) + 12
        pr(f"{k:16s} falls in {int((yoy<0).sum()):3d} of {len(yoy)} months; worst {yoy.min():+6.2f}% ({MONTHS[mn]}), "
           f"best {yoy.max():+6.2f}% ({MONTHS[mx]}); sd {yoy.std():.2f}")
    # longest run of yoy wage falls
    x = S["cci_wages"]
    yoy = [(MONTHS[t], 100 * (x[t] / x[t - 12] - 1)) for t in range(12, N)]
    neg = [m for m, v in yoy if v < 0]
    pr("wage y/y falls in months:", ", ".join(neg) if neg else "none")
    # wage index level falls: peak-to-trough
    peak, worst = x[0], 0.0
    for v in x:
        peak = max(peak, v); worst = min(worst, v / peak - 1)
    pr(f"wage index largest fall from a previous peak: {100*worst:.2f}%")
    x = S["cci_materials"]
    peak, worst, wm = x[0], 0.0, ""
    for i, v in enumerate(x):
        peak = max(peak, v)
        if v / peak - 1 < worst:
            worst, wm = v / peak - 1, MONTHS[i]
    pr(f"materials index largest fall from a previous peak: {100*worst:.2f}% (trough {wm})")


def section_sizes(partial):
    pr("\n== 8. Sizes for a 10% stronger NT$ (NUMBERS 8j's test), Keel arithmetic on the responses above ==")
    # 10% stronger NT$ in 8j's convention = 10% more US$ for a fixed NT$ bill; log move = ln(1.10)
    s = math.log(1.10)
    b, se = partial[("cci_materials", 0)]
    bt, set_ = partial[("cci_total", 0)]
    mat = math.exp(b[1] * s) - 1
    tot = math.exp(bt[1] * s) - 1
    pr(f"holding world US$ prices: materials {100*mat:+.2f}% in the same 12 months; total {100*tot:+.2f}%; "
       f"US$ cost of a fixed NT$ budget {100*((1+tot)*1.10-1):+.2f}% instead of +10.00%")
    pr(f"  materials share of the index {W['materials']/10:.1f}%: materials effect alone moves the total by about "
       f"{W['materials']/1000*100*mat:+.2f} points")


if __name__ == "__main__":
    section_weights()
    section_latest()
    section_corr()
    partial = section_partial()
    section_dlag()
    episodes(24, 0.10)
    episodes(12, 0.10)
    section_falls()
    section_sizes(partial)
