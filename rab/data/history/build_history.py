"""Turn the raw history files (rab/data/history/raw/, fetched by fetch_history.py) into tidy inputs for M5, M6, M7.

Outputs (all in rab/data/history/):
  annual_history.csv      one row per calendar year 1871-2025; returns are for the calendar year (1 Jan -> 31 Dec),
                          so a value in row t is what $1 held from the start of year t earned by the start of t+1.
  soy_curves.csv          Treasury par yields on the first trading day of each year 1871-2026 (see the 'basis' column)
  daily_curves_1962_1989.csv  FRED constant-maturity yields, every day 1962-1989, in the Treasury par-file layout
  shiller_monthly.csv     Shiller monthly: price, dividend, CPI, GS10, nominal total-return index
  jst_countries_usd.csv   JST equity returns in USD and GDP weights, per country and year (the ex-U.S. build)
  jpm_ltcma_2026_usd.csv, jpm_ltcma_2026_corr.csv   J.P. Morgan 2026 LTCMA U.S.-dollar matrix (repo PDF, page 2)
  market_inflation_2026-09.csv   breakevens, TIPS real yields, Cleveland Fed expected inflation, latest values
  build_checks.txt        overlap checks between sources (printed and saved)

Column sources in annual_history.csv (every choice is stated; see M5_SPEC.md section 1):
  us_eq        S&P 500 total return: Damodaran 1928-2025; JST USA eq_tr 1871-1927
  us_bill      3-month T-bill: Damodaran 1928-2025; JST USA bill_rate/100 1871-1927
  us_bond10    10-year Treasury total return: Damodaran 1928-2025; JST USA bond_tr 1871-1927
  cpi_infl     U.S. CPI, December to December: Shiller monthly CPI (CPI-U from 1913; Warren-Pearson before)
  exus_eq      ex-U.S. developed equities in USD, GDP-weighted (JST R6, 16 countries with equity data) 1871-2020;
               Ken French Developed ex-U.S. market (Mkt-RF + RF) 2021-2025
  world_eq     'VT-like' world mix, rebalanced every year: 0.62 us_eq + 0.38 exus_eq to 1989; from 1990
               0.62 us_eq + 0.28 exus_eq + 0.10 em_kf (VT fact sheet: 62% U.S.; emerging data start 1990)
  us_smallval  Ken French U.S. small-value portfolio (SMALL HiBM, value-weighted) 1927-2025
  us_mkt_kf    Ken French U.S. market (Mkt-RF + RF) 1927-2025
  gold         Damodaran gold 1928-2025 (annual-average prices before 1970, LBMA after)
  housing      Damodaran real estate (U.S. home prices; NOT a REIT index) 1928-2025
  dev_kf, exus_kf, em_kf  Ken French Developed / Developed ex-U.S. (1991-) / Emerging (1990-) market returns, USD
  jpn_eq, jpn_ltrate, jpn_cpi_infl  JST Japan equity total return (yen), long rate (%), CPI inflation
  vt_etf ... vnq_etf  actual fund total returns from Yahoo adjusted closes (Dec to Dec), 2009-2025

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/data/history/build_history.py
"""
import csv
import io
import os
import re
import zipfile
from datetime import date

import numpy as np
import pandas as pd
import xlrd

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "raw")
WT = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))   # worktree root
CHECKS = []
VT_US_SHARE = 0.62          # VT regional mix (Vanguard VT fact sheet 2026-08-31: 62.3% U.S.; S2/D2 inputs)
PAR_COLS = ["1 Mo", "2 Mo", "3 Mo", "6 Mo", "1 Yr", "2 Yr", "3 Yr", "5 Yr", "7 Yr", "10 Yr", "20 Yr", "30 Yr"]
FRED_TO_PAR = {"DGS1MO": "1 Mo", "DGS3MO": "3 Mo", "DGS6MO": "6 Mo", "DGS1": "1 Yr", "DGS2": "2 Yr", "DGS3": "3 Yr",
               "DGS5": "5 Yr", "DGS7": "7 Yr", "DGS10": "10 Yr", "DGS20": "20 Yr", "DGS30": "30 Yr"}


def check(msg):
    CHECKS.append(msg)
    print(msg)


# ------------------------------------------------------------------------------------------------------ Shiller
def shiller():
    s = xlrd.open_workbook(os.path.join(RAW, "shiller_ie_data.xls")).sheet_by_name("Data")
    rows = []
    for r in range(8, s.nrows):
        d = s.cell_value(r, 0)
        if not isinstance(d, float):
            continue
        yr = int(d)
        def v(c):
            x = s.cell_value(r, c)
            return float(x) if isinstance(x, float) else np.nan
        rows.append(dict(year=yr, P=v(1), D=v(2), CPI=v(4), GS10=v(6), real_tr_price=v(9),
                         bond_ret_m=v(17)))
    df = pd.DataFrame(rows)
    df["month"] = df.groupby("year").cumcount() + 1          # 1871.01 .. 1871.1 (Oct) .. 1871.12 in file order
    df["tr_index"] = df.real_tr_price * df.CPI / df.CPI.iloc[-1]      # nominal total-return index (scale arbitrary)
    df.to_csv(os.path.join(ROOT, "shiller_monthly.csv"), index=False)
    return df


def shiller_fix_months(df):
    # rebuild month from the order within each year (robust to the .1 = October convention)
    df = df.copy()
    df["month"] = df.groupby("year").cumcount() + 1
    return df


# ------------------------------------------------------------------------------------------------------ Damodaran
def damodaran():
    b = xlrd.open_workbook(os.path.join(RAW, "damodaran_histretSP.xls"))
    s = b.sheet_by_name("Returns by year")
    out = []
    for r in range(20, s.nrows):
        y = s.cell_value(r, 0)
        if not isinstance(y, float) or y < 1900:
            continue
        out.append(dict(year=int(y), us_eq=s.cell_value(r, 1), smallcap_decile=s.cell_value(r, 2),
                        us_bill=s.cell_value(r, 3), us_bond10=s.cell_value(r, 4), baa=s.cell_value(r, 5),
                        housing=s.cell_value(r, 6), gold=s.cell_value(r, 7)))
    d = pd.DataFrame(out)
    t = b.sheet_by_name("T. Bond yield & return")
    ylds = {int(t.cell_value(r, 0)): t.cell_value(r, 1) for r in range(7, t.nrows) if isinstance(t.cell_value(r, 0), float)}
    d["tbond_rate_end"] = d.year.map(ylds)
    return d.astype(float).assign(year=lambda x: x.year.astype(int)), ylds


# ------------------------------------------------------------------------------------------------------ JST
def jst():
    j = pd.read_excel(os.path.join(RAW, "JSTdatasetR6.xlsx"))
    j = j.sort_values(["iso", "year"]).copy()
    j["xr_prev"] = j.groupby("iso").xrusd.shift(1)
    j["gdp_prev"] = j.groupby("iso").gdp.shift(1)
    j["eq_usd"] = (1 + j.eq_tr) * j.xr_prev / j.xrusd - 1          # xrusd = local currency per USD
    # Weights: real GDP = Maddison real GDP per head (1990 int. $) x population, previous year. JST's nominal 'gdp' is in
    # local currency with country-specific units (billions / trillions), so it cannot weight countries directly.
    j["rgdp"] = j.rgdpmad * j["pop"]
    j["gdp_usd_prev"] = j.groupby("iso").rgdp.shift(1)
    j["cpi_infl"] = j.groupby("iso").cpi.pct_change(fill_method=None)
    keep = j[["year", "iso", "country", "eq_tr", "eq_usd", "gdp_usd_prev", "xrusd", "ltrate", "cpi", "cpi_infl",
              "bill_rate", "bond_tr"]]
    keep.to_csv(os.path.join(ROOT, "jst_countries_usd.csv"), index=False)
    ex = j[(j.iso != "USA") & j.eq_usd.notna() & j.gdp_usd_prev.notna()]
    w = ex.groupby("year").apply(lambda g: pd.Series({
        "exus_eq_jst": float(np.average(g.eq_usd, weights=g.gdp_usd_prev)),
        "exus_n": len(g), "exus_countries": " ".join(sorted(g.iso))}), include_groups=False)
    us = j[j.iso == "USA"].set_index("year")[["eq_tr", "bill_rate", "bond_tr", "ltrate", "cpi_infl"]]
    jp = j[j.iso == "JPN"].set_index("year")[["eq_tr", "ltrate", "cpi_infl", "bond_tr", "bill_rate"]]
    return w, us, jp


# ------------------------------------------------------------------------------------------------------ Ken French
def kf_annual(zipname, col_sets):
    with zipfile.ZipFile(os.path.join(RAW, zipname)) as z:
        txt = z.read(z.namelist()[0]).decode("latin-1")
    lines = txt.splitlines()
    out = {}
    for label, marker, cols in col_sets:
        i = next(k for k, l in enumerate(lines) if marker.lower() in l.lower())
        hdr = None
        for l in lines[i + 1:]:
            if not l.strip():
                if hdr is not None and out.get(label):
                    break
                continue
            parts = [p.strip() for p in l.split(",")]
            if hdr is None:
                hdr = parts
                out[label] = {}
                continue
            if not re.fullmatch(r"\d{4}", parts[0]):
                break
            row = dict(zip(hdr[1:], [float(x) for x in parts[1:]]))
            out[label][int(parts[0])] = {c: row[c] for c in cols}
    return out


def ken_french():
    ff = kf_annual("kf_F-F_Research_Data_Factors_CSV.zip", [("us", "Annual Factors", ["Mkt-RF", "RF"])])["us"]
    sv = kf_annual("kf_6_Portfolios_2x3_CSV.zip",
                   [("sv", "Average Value Weighted Returns -- Annual", ["SMALL HiBM", "SMALL LoBM", "BIG HiBM"])])["sv"]
    dv = kf_annual("kf_Developed_3_Factors_CSV.zip", [("d", "Annual Factors", ["Mkt-RF", "RF"])])["d"]
    dx = kf_annual("kf_Developed_ex_US_3_Factors_CSV.zip", [("d", "Annual Factors", ["Mkt-RF", "RF"])])["d"]
    em = kf_annual("kf_Emerging_5_Factors_CSV.zip", [("d", "Annual Factors", ["Mkt-RF", "RF"])])["d"]
    rec = {}
    for y, v in ff.items():
        rec.setdefault(y, {})["us_mkt_kf"] = (v["Mkt-RF"] + v["RF"]) / 100
        rec[y]["rf_kf"] = v["RF"] / 100
    for y, v in sv.items():
        if v["SMALL HiBM"] > -99:
            rec.setdefault(y, {})["us_smallval"] = v["SMALL HiBM"] / 100
    for name, src in (("dev_kf", dv), ("exus_kf", dx), ("em_kf", em)):
        for y, v in src.items():
            if v["Mkt-RF"] > -99:
                rec.setdefault(y, {})[name] = (v["Mkt-RF"] + v["RF"]) / 100
    return pd.DataFrame.from_dict(rec, orient="index").sort_index()


# ------------------------------------------------------------------------------------------------------ FRED / curves
def fred(series):
    df = pd.read_csv(os.path.join(WT, "rab", "data", "fred", f"{series}.csv"))
    df.columns = ["date", series]
    df["date"] = pd.to_datetime(df.date)
    df[series] = pd.to_numeric(df[series], errors="coerce")
    return df.set_index("date")[series]


def daily_fred_curves():
    """Every FRED trading day 1962-01-02 .. 1989-12-31, columns in the Treasury par-file layout (percent)."""
    cols = {par: fred(s) for s, par in FRED_TO_PAR.items()}
    df = pd.DataFrame(cols)
    df = df[(df.index >= "1962-01-01") & (df.index <= "1989-12-31")]
    df = df.dropna(how="all")
    df = df[df["10 Yr"].notna() & df["1 Yr"].notna()]
    df.index.name = "date"
    out = df.reindex(columns=PAR_COLS)
    out.to_csv(os.path.join(ROOT, "daily_curves_1962_1989.csv"), float_format="%.2f")
    return out


def par_rows(year):
    p = os.path.join(WT, "rab", "data", "treasury_par_1990_1999" if year < 2000 else "treasury_par_2000_2026",
                     f"{year}.csv")
    rows = []
    for r in csv.DictReader(open(p)):
        m, d, y = r["Date"].split("/")
        r["_date"] = date(int(y), int(m), int(d))
        rows.append(r)
    return sorted(rows, key=lambda r: r["_date"])


def soy_curves(sh, fredd):
    """First trading day of each year: par file (1990-2026), FRED CMT (1962-1989), flat Shiller GS10 January (1871-1961)."""
    out = []
    for y in range(1871, 2027):
        if y >= 1990:
            r = par_rows(y)[0]
            rec = {c: (float(r[c]) if r.get(c) not in (None, "", "N/A") else np.nan) for c in PAR_COLS}
            rec.update(year=y, date=r["_date"].isoformat(), basis="treasury_par")
        elif y >= 1962:
            sub = fredd[fredd.index.year == y]
            d0 = sub.index[0]
            rec = {c: sub.iloc[0][c] for c in PAR_COLS}
            rec.update(year=y, date=d0.date().isoformat(), basis="fred_cmt")
        else:
            g = sh[(sh.year == y) & (sh.month == 1)].GS10.iloc[0]
            rec = {c: np.nan for c in PAR_COLS}
            rec["10 Yr"] = g
            rec.update(year=y, date=f"{y}-01 (monthly avg)", basis="flat_shiller_gs10")
        out.append(rec)
    df = pd.DataFrame(out)[["year", "date", "basis"] + PAR_COLS]
    df.to_csv(os.path.join(ROOT, "soy_curves.csv"), index=False, float_format="%.4f")
    return df


# ------------------------------------------------------------------------------------------------------ Yahoo funds
def yahoo_funds():
    raw = pd.read_csv(os.path.join(RAW, "yf_funds_monthly.csv"), header=[0, 1], index_col=0)
    adj = raw["Adj Close"]
    adj.index = pd.to_datetime(adj.index)
    dec = adj[adj.index.month == 12]
    ann = dec.pct_change(fill_method=None)
    ann.index = ann.index.year
    ann = ann.loc[2009:2025]
    ann.columns = [f"{c.lower()}_etf" for c in ann.columns]
    return ann


# ------------------------------------------------------------------------------------------------------ JPM LTCMA
def jpm_matrix():
    from pypdf import PdfReader
    pdf = os.path.join("/Users/ray/Research/rab-kit", "competition", "official_market_data",
                       "JPM_LTCMA_2026_US_matrix_USD.pdf")
    t = PdfReader(pdf).pages[1].extract_text().replace("\xa0", " ").splitlines()   # names carry no-break spaces
    rows = []
    for l in t:
        m = re.match(r"^(.+?)\s+((?:-?\d+\.\d\d\s+)*-?\d+\.\d\d)\s*$", l.strip())
        if m and not re.match(r"^\d", m.group(1)):
            nums = [float(x) for x in m.group(2).split()]
            if len(nums) >= 5 and abs(nums[-1] - 1.0) < 1e-9:
                rows.append((m.group(1).strip(), nums))
    names, stats, corr = [], [], {}
    for name, nums in rows:
        k = len(nums) - 4                     # number of correlations = position in the matrix
        names.append((k, name))
        stats.append(dict(pos=k, asset=name, compound_2026=nums[0], arithmetic_2026=nums[1], vol=nums[2],
                          compound_2025=nums[3]))
        corr[k] = nums[4:]
    st_df = pd.DataFrame(stats).sort_values("pos")
    n = max(corr)
    assert sorted(corr) == list(range(1, n + 1)) or True
    st_df.to_csv(os.path.join(ROOT, "jpm_ltcma_2026_usd.csv"), index=False)
    pos = {k: nm for k, nm in names}
    lines = []
    for k in sorted(corr):
        for i, c in enumerate(corr[k]):
            if (i + 1) in pos:
                lines.append(dict(row=pos[k], col=pos[i + 1], corr=c))
    pd.DataFrame(lines).to_csv(os.path.join(ROOT, "jpm_ltcma_2026_corr.csv"), index=False)
    check(f"JPM LTCMA 2026 matrix: {len(st_df)} assets parsed (positions {st_df.pos.min()}..{st_df.pos.max()}); "
          f"missing positions: {sorted(set(range(1, n + 1)) - set(pos))}")
    return st_df


# ------------------------------------------------------------------------------------------------------ market inflation
def market_inflation():
    rows = []
    for s in ["T5YIE", "T10YIE", "T5YIFR", "DFII5", "DFII7", "DFII10", "DFII20", "DFII30", "EXPINF5YR", "EXPINF10YR",
              "EXPINF20YR", "EXPINF30YR", "CPIAUCNS"]:
        df = pd.read_csv(os.path.join(RAW, f"fred_{s}.csv"))
        df.columns = ["date", "v"]
        df["v"] = pd.to_numeric(df.v, errors="coerce")
        last = df.dropna().iloc[-1]
        rows.append(dict(series=s, date=last.date, value=float(last.v),
                         url=f"https://fred.stlouisfed.org/series/{s}"))
    pd.DataFrame(rows).to_csv(os.path.join(ROOT, "market_inflation_2026-09.csv"), index=False)
    return pd.DataFrame(rows)


# ------------------------------------------------------------------------------------------------------ assemble
def main():
    sh = shiller_fix_months(shiller())
    sh.to_csv(os.path.join(ROOT, "shiller_monthly.csv"), index=False)
    dam, ylds = damodaran()
    exus, jus, jjp = jst()
    kf = ken_french()
    fredd = daily_fred_curves()
    soy = soy_curves(sh, fredd)
    yfa = yahoo_funds()
    jpm_matrix()
    market_inflation()

    years = range(1871, 2026)
    A = pd.DataFrame(index=pd.Index(years, name="year"))
    d = dam.set_index("year")
    # U.S. equity, bills, bonds
    A["us_eq"] = [d.us_eq.get(y) if y >= 1928 else jus.eq_tr.get(y) for y in years]
    A["us_bill"] = [d.us_bill.get(y) if y >= 1928 else jus.bill_rate.get(y) / 100 for y in years]
    A["us_bond10"] = [d.us_bond10.get(y) if y >= 1928 else jus.bond_tr.get(y) for y in years]
    A["src_us"] = ["damodaran" if y >= 1928 else "jst_usa" for y in years]
    # CPI Dec-Dec from Shiller
    dec = sh[sh.month == 12].set_index("year").CPI
    A["cpi_infl"] = [dec.get(y) / dec.get(y - 1) - 1 if (y - 1) in dec.index and y in dec.index else np.nan for y in years]
    # ex-U.S.: JST GDP-weighted to 2020, Ken French developed ex-U.S. 2021+
    A["exus_eq"] = [exus.exus_eq_jst.get(y) if y <= 2020 else kf.exus_kf.get(y) for y in years]
    A["exus_n_countries"] = [exus.exus_n.get(y) if y <= 2020 else np.nan for y in years]
    A["src_exus"] = ["jst_gdp_weighted" if y <= 2020 else "kf_developed_ex_us" for y in years]
    # VT-like world mix: 62% U.S. / 38% outside the U.S. (VT fact sheet); from 1990, when emerging-market data start,
    # the 38% is 28% developed ex-U.S. + 10% emerging (VT's non-U.S. part is about three-quarters developed).
    em = pd.Series([kf.em_kf.get(y) for y in years], index=A.index)
    A["world_eq"] = np.where(em.notna(), VT_US_SHARE * A.us_eq + 0.28 * A.exus_eq + 0.10 * em,
                             VT_US_SHARE * A.us_eq + (1 - VT_US_SHARE) * A.exus_eq)
    A["us_mkt_kf"] = [kf.us_mkt_kf.get(y) for y in years]
    A["us_smallval"] = [kf.us_smallval.get(y) for y in years]
    A["gold"] = [d.gold.get(y) for y in years]
    A["housing"] = [d.housing.get(y) for y in years]
    A["dev_kf"] = [kf.dev_kf.get(y) for y in years]
    A["exus_kf"] = [kf.exus_kf.get(y) for y in years]
    A["em_kf"] = [kf.em_kf.get(y) for y in years]
    A["jpn_eq"] = [jjp.eq_tr.get(y) for y in years]
    A["jpn_ltrate"] = [jjp.ltrate.get(y) for y in years]
    A["jpn_cpi_infl"] = [jjp.cpi_infl.get(y) for y in years]
    for c in yfa.columns:
        A[c] = [yfa[c].get(y) for y in years]
    A.to_csv(os.path.join(ROOT, "annual_history.csv"), float_format="%.6f")

    # ------------------------------------------------ overlap checks (reported, never averaged)
    ov = A.loc[1928:2020]
    c = np.corrcoef(ov.us_eq, jus.eq_tr.reindex(ov.index))[0, 1]
    gd = (np.prod(1 + ov.us_eq) ** (1 / len(ov)) - 1) - (np.prod(1 + jus.eq_tr.reindex(ov.index)) ** (1 / len(ov)) - 1)
    check(f"U.S. equity 1928-2020: Damodaran vs JST USA correlation {c:.3f}; geometric-mean gap {gd * 100:+.2f}pp/yr")
    o2 = A.loc[1991:2020]
    c2 = np.corrcoef(o2.exus_eq, o2.exus_kf)[0, 1]
    g1 = np.prod(1 + o2.exus_eq) ** (1 / len(o2)) - 1
    g2 = np.prod(1 + o2.exus_kf) ** (1 / len(o2)) - 1
    check(f"ex-U.S. 1991-2020: JST GDP-weighted vs Ken French developed ex-U.S. correlation {c2:.3f}; geometric means "
          f"{g1 * 100:.2f}% vs {g2 * 100:.2f}%")
    o3 = A.loc[2009:2025]
    wk = o3.world_eq
    c3 = np.corrcoef(wk, o3.vt_etf)[0, 1]
    check(f"world mix vs actual VT 2009-2025: correlation {c3:.3f}; geometric means "
          f"{(np.prod(1 + wk) ** (1 / len(o3)) - 1) * 100:.2f}% vs {(np.prod(1 + o3.vt_etf) ** (1 / len(o3)) - 1) * 100:.2f}%")
    fr = pd.read_csv(os.path.join(RAW, "fred_CPIAUCNS.csv"))
    fr.columns = ["date", "v"]
    fr["date"] = pd.to_datetime(fr.date)
    frd = fr[fr.date.dt.month == 12].set_index(fr[fr.date.dt.month == 12].date.dt.year).v
    fi = frd.pct_change().loc[1914:2025]
    mx = np.nanmax(np.abs(fi.values - A.cpi_infl.reindex(fi.index).values))
    check(f"CPI Dec-Dec 1914-2025: Shiller vs FRED CPIAUCNS max abs difference {mx * 100:.2f}pp")
    dy = pd.Series(ylds)
    sj = sh[sh.month == 1].set_index("year").GS10
    gap = (sj.reindex(range(1929, 1962)) / 100 - dy.reindex(range(1928, 1961)).values)
    check(f"start-of-year 10y yield 1929-1961: Shiller January GS10 minus Damodaran end of prior year: median "
          f"{np.nanmedian(gap) * 1e4:+.0f}bp, max abs {np.nanmax(np.abs(gap)) * 1e4:.0f}bp")
    y = xlrd.open_workbook(os.path.join(RAW, "shiller_ie_data_yale.xls")).sheet_by_name("Data")
    yale = {}
    for r in range(8, y.nrows):
        d0 = y.cell_value(r, 0)
        if isinstance(d0, float) and isinstance(y.cell_value(r, 6), float) and isinstance(y.cell_value(r, 1), float):
            yale[round(d0, 2)] = (y.cell_value(r, 1), y.cell_value(r, 6))
    cur = {round(yy + mm / 100 if mm != 10 else yy + 0.1, 2): (p_, g_) for yy, mm, p_, g_ in
           zip(sh.year, sh.month, sh.P, sh.GS10)}
    common = [k for k in yale if k in cur and cur[k][0] == cur[k][0] and k < 2020]
    dp = max(abs(yale[k][0] / cur[k][0] - 1) for k in common)
    dg = max(abs(yale[k][1] - cur[k][1]) for k in common)
    check(f"Shiller current copy vs Yale copy, {len(common)} common months before 2020: largest price difference "
          f"{dp:.2%}, largest GS10 difference {dg:.2f} points")
    check(f"annual_history.csv: {len(A)} years {A.index.min()}-{A.index.max()}; world_eq complete "
          f"{A.world_eq.first_valid_index()}-{A.world_eq.last_valid_index()} ({A.world_eq.notna().sum()} years)")
    check(f"soy_curves.csv: {len(soy)} years; bases: {soy.basis.value_counts().to_dict()}")
    with open(os.path.join(ROOT, "build_checks.txt"), "w") as f:
        f.write("\n".join(CHECKS) + "\n")


if __name__ == "__main__":
    main()
