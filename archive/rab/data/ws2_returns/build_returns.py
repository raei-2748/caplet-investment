"""Turn the raw WS2 return files into tidy CSVs (no network). Run after fetch_returns.py.

Outputs (rab/data/ws2_returns/):
  shiller_monthly.csv   one row per month Jan 1871 .. Sep 2026: P, D, CPI, GS10, Shiller's real total-return price,
                        the nominal total-return index built from it, and two versions of the month's nominal
                        total return (from Shiller's real TR price x CPI, and from P and D directly) as a cross-check.
  shiller_annual.csv    calendar-year (January to January) nominal total returns, 1871 .. 2025, from the index.
  damodaran_annual.csv  Damodaran annual S&P 500 total return, 3-month T-bill and 10-year T-bond returns, 1928 .. 2025.
  build_report.txt      summary statistics and the cross-checks below.

Conventions (see rab/models/M3_SPEC.md section 2):
  - Shiller's P is the monthly average of daily closes (the Sep 2026 value is the 1 Sep close); D is the dividend at an
    annual rate. Month t's nominal total return is I_{t+1} / I_t - 1, where I_t = RealTRPrice_t x CPI_t (the real TR
    price is in latest-month dollars, so the constant cancels in the ratio).
  - Cross-check: (P_{t+1} + D_t / 12) / P_t - 1 must agree closely with the index return.
  - Row order, not Shiller's decimal date, identifies the month (Shiller writes October as .1).
"""
import csv
import os

import numpy as np
import xlrd

HERE = os.path.dirname(os.path.abspath(__file__))


def shiller():
    s = xlrd.open_workbook(os.path.join(HERE, "raw", "shiller_ie_data.xls")).sheet_by_name("Data")
    rows = []
    for r in range(8, s.nrows):
        v = [s.cell_value(r, c) for c in range(s.ncols)]
        if not isinstance(v[0], float):
            break
        rows.append(v)
    out = []
    y, m = 1871, 1
    for v in rows:
        yy = int(v[0])
        assert yy == y, (v[0], y, m)
        num = lambda x: float(x) if isinstance(x, float) else np.nan
        out.append({"month": f"{y}-{m:02d}", "P": num(v[1]), "D": num(v[2]), "CPI": num(v[4]), "GS10": num(v[6]),
                    "real_tr_price": num(v[9])})
        m += 1
        if m == 13:
            y, m = y + 1, 1
    idx = np.array([o["real_tr_price"] * o["CPI"] for o in out])
    idx = idx / idx[0]
    for i, o in enumerate(out):
        o["nominal_tr_index"] = idx[i]
        if i + 1 < len(out):
            o["r_nominal"] = idx[i + 1] / idx[i] - 1
            o["r_nominal_PD"] = (out[i + 1]["P"] + o["D"] / 12) / o["P"] - 1 if np.isfinite(o["D"]) else np.nan
        else:
            o["r_nominal"] = o["r_nominal_PD"] = np.nan
    return out


def damodaran():
    s = xlrd.open_workbook(os.path.join(HERE, "raw", "damodaran_histretSP.xls")).sheet_by_name("Returns by year")
    hdr = [s.cell_value(19, c) for c in range(9)]
    assert hdr[1].startswith("S&P 500") and hdr[3] == "3-month T.Bill" and hdr[4].startswith("US T. Bond"), hdr
    out = []
    for r in range(20, s.nrows):
        y = s.cell_value(r, 0)
        if not isinstance(y, float):
            break
        out.append({"year": int(y), "sp500_tr": s.cell_value(r, 1), "tbill_3m": s.cell_value(r, 3),
                    "tbond_10y_tr": s.cell_value(r, 4)})
    return out


def write(name, rows, cols, fmt=None):
    with open(os.path.join(HERE, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for o in rows:
            w.writerow([("" if (isinstance(o[c], float) and not np.isfinite(o[c])) else
                         (f"{o[c]:.10g}" if isinstance(o[c], float) else o[c])) for c in cols])


def main():
    rep = []
    sh = shiller()
    write("shiller_monthly.csv", sh, ["month", "P", "D", "CPI", "GS10", "real_tr_price", "nominal_tr_index",
                                      "r_nominal", "r_nominal_PD"])
    months = [o["month"] for o in sh]
    i_jan = {int(mo[:4]): i for i, mo in enumerate(months) if mo.endswith("-01")}
    ann = []
    for y in range(1871, 2026):
        a, b = sh[i_jan[y]]["nominal_tr_index"], sh[i_jan[y + 1]]["nominal_tr_index"]
        ann.append({"year": y, "r_nominal": b / a - 1, "log_r_nominal": float(np.log(b / a))})
    write("shiller_annual.csv", ann, ["year", "r_nominal", "log_r_nominal"])
    da = damodaran()
    write("damodaran_annual.csv", da, ["year", "sp500_tr", "tbill_3m", "tbond_10y_tr"])

    # summaries and cross-checks
    i0, i1 = months.index("1871-01"), months.index("2025-12")
    r = np.array([o["r_nominal"] for o in sh[i0:i1 + 1]])
    rpd = np.array([o["r_nominal_PD"] for o in sh[i0:i1 + 1]])
    lr = np.log1p(r)
    rep.append(f"Shiller monthly: {sh[0]['month']} .. {sh[-1]['month']} ({len(sh)} rows); sample for models "
               f"{months[i0]} .. {months[i1]} ({len(r)} monthly returns)")
    rep.append(f"  mean monthly log return {lr.mean():.6f} (annualised x12 {lr.mean() * 12:.4%}); sd {lr.std(ddof=1):.5f} "
               f"(x sqrt12 {lr.std(ddof=1) * np.sqrt(12):.4f}); lag-1 autocorrelation "
               f"{np.corrcoef(lr[:-1], lr[1:])[0, 1]:.3f}")
    d = r - rpd
    rep.append(f"  cross-check index return vs (P'+D/12)/P: max |diff| {np.nanmax(np.abs(d)):.2e}, mean diff {np.nanmean(d):.2e}")
    la = np.array([o["log_r_nominal"] for o in ann])
    rep.append(f"Shiller annual (Jan-Jan) 1871-2025: n={len(la)}, mean log {la.mean():.4f} (compound "
               f"{np.expm1(la.mean()):.2%}), sd log {la.std(ddof=1):.4f}, min {np.expm1(la.min()):.1%} "
               f"({ann[int(la.argmin())]['year']}), max {np.expm1(la.max()):.1%} ({ann[int(la.argmax())]['year']})")
    dr = np.array([o["sp500_tr"] for o in da])
    ld = np.log1p(dr)
    rep.append(f"Damodaran S&P 500 TR 1928-2025: n={len(dr)}, mean log {ld.mean():.4f} (compound {np.expm1(ld.mean()):.2%}),"
               f" sd log {ld.std(ddof=1):.4f}, min {dr.min():.1%}, max {dr.max():.1%}")
    ov = {o['year']: o['log_r_nominal'] for o in ann}
    common = [o['year'] for o in da if o['year'] in ov]
    x = np.array([ov[y] for y in common])
    yv = np.array([np.log1p(o['sp500_tr']) for o in da if o['year'] in ov])
    rep.append(f"  Shiller Jan-Jan vs Damodaran Dec-Dec on {common[0]}-{common[-1]}: corr {np.corrcoef(x, yv)[0, 1]:.3f}; "
               f"sd log Shiller {x.std(ddof=1):.4f} vs Damodaran {yv.std(ddof=1):.4f} (Shiller averages daily closes "
               f"within each month, and its years run January to January)")
    txt = "\n".join(rep)
    print(txt)
    open(os.path.join(HERE, "build_report.txt"), "w").write(txt + "\n")


if __name__ == "__main__":
    main()
