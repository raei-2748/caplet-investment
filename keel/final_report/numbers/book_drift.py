"""The WInS book's price drift from the target sheet to the fills, re-derived from the trade records (numbers owner,
Tue 17 Nov 2026, Sydney). Team record and arithmetic, not a model. NUMBERS 8m ("Price drift from the sheet to the
fills"); card Q88 rows 9, 10 and 13.

Run from the repo root:  python3 -I keel/final_report/numbers/book_drift.py
   or from this folder:  python3 -I book_drift.py
Writes keel/final_report/numbers/results_book_drift_2026-11-17.json and prints every figure (under a second, standard
library only). Reads only the three records below; changes nothing.

Records:
  * the target sheet, `caplet/google_drive/sheets/portfolio_and_trading_notes/portfolio.csv` (Portfolio tab, exported
    14 Oct): target units and prices in rows 20-30 (ETFs at the 2 Oct close; bonds "as of 5 Oct 01:18 ET (clean +
    accrued, in Book L)", row 34) and the cash it expected after all eleven orders (row 35, "$2,955");
  * `book_l.csv` (Book L tab): each bond's clean price and accrued interest per $100, which the sheet's bond prices are
    checked against (asserted: the sheet's price = Book L's clean + accrued, for all five);
  * the WInS snapshot of 23 Oct, `competition/wins/2026-10-23_snapshot.md` l.10 and l.22-32: cash $3,513.79, each
    holding's quantity and price paid (bonds per $1,000 face, clean); and NUMBERS 8g's split of what left the account
    at purchase beyond the holdings' cost: $200 of commissions and $1,109.42 of accrued interest, the residual
    ($300,000 less holdings at cost, less cash, less commissions; asserted here).

Sign: positive = the fills cost more than the sheet. Fill times in WInS are US Eastern (6 Oct 7:55 PM to 7 Oct 8:27 PM
ET), which is 7 Oct 10:55 AM to 8 Oct 11:27 AM in Sydney (AEDT, UTC+11; ET in October is EDT, UTC-4).
"""
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SHEETS = ROOT / "caplet/google_drive/sheets/portfolio_and_trading_notes"
SNAP = ROOT / "competition/wins/2026-10-23_snapshot.md"
OUT = HERE / "results_book_drift_2026-11-17.json"

money = lambda s: float(s.replace("$", "").replace(",", "").strip())

# ---------------------------------------------------------------- the target sheet
rows = list(csv.reader(open(SHEETS / "portfolio.csv")))
sheet = {}
for r in rows[19:30]:                                     # l.20-30
    name, typ, price, units = r[1], r[3], r[6], r[7]
    sheet[name] = {"type": typ, "price": money(price), "units": money(units)}
cash_line = [r for r in rows if r[1].startswith("Cash expected after all 11 orders")][0]
sheet_cash_shown = money(cash_line[2])

bookl = {}
for r in list(csv.reader(open(SHEETS / "book_l.csv")))[13:23]:
    if r[2] == "Treasury bond":
        bookl[r[1]] = {"clean": money(r[6]), "accrued": money(r[7])}

# ---------------------------------------------------------------- the snapshot
snap = {}
txt = SNAP.read_text().splitlines()
cash_wins = money(re.search(r"\$([\d,\.]+)", txt[9]).group(0))
for line in txt[21:32]:
    cells = [x.strip() for x in line.strip().strip("|").split("|")]
    snap[cells[0]] = {"qty": money(cells[1]), "paid": money(cells[3])}

ALIAS = {"IBTM": "IBTM (iBonds Dec 2032)", "IBTO": "IBTO (Dec 2033)", "IBTP": "IBTP (Dec 2034)",
         "IBTQ": "IBTQ (Dec 2035)", "IBTR": "IBTR (Dec 2036)", "VT": "VT (Total World Stock)",
         "T 4.750% 15-Feb-2037": "T-bond 4.75% 15-Feb-2037", "T 4.500% 15-May-2038": "T-bond 4.50% 15-May-2038",
         "T 4.375% 15-Nov-2039": "T-bond 4.375% 15-Nov-2039", "T 4.250% 15-Nov-2040": "T-bond 4.25% 15-Nov-2040",
         "T 3.125% 15-Nov-2041": "T-bond 3.125% 15-Nov-2041"}
COMMISSIONS = 200.0
ACCRUED_WINS = 1109.42                                     # NUMBERS 8g (residual), asserted below

out = {"run": "Tue 17 Nov 2026 (Sydney), numbers owner", "basis": "team record and arithmetic, not a model"}
lines = {}
fund_drift = 0.0
for k in ("IBTM", "IBTO", "IBTP", "IBTQ", "IBTR"):
    s, w = sheet[k], snap[ALIAS[k]]
    assert s["units"] == w["qty"], k
    d = w["qty"] * (w["paid"] - s["price"])
    fund_drift += d
    lines[k] = {"units": w["qty"], "sheet_price_2oct": s["price"], "paid": w["paid"], "drift": round(d, 2),
                "drift_pct": (w["paid"] / s["price"] - 1)}
vs, vw = sheet["VT"], snap[ALIAS["VT"]]
vt = {"target_units": vs["units"], "filled_units": vw["qty"], "sheet_price_2oct": vs["price"], "paid": vw["paid"],
      "sheet_cost": vs["units"] * vs["price"], "fill_cost": vw["qty"] * vw["paid"]}
vt["change"] = vt["fill_cost"] - vt["sheet_cost"]
vt["three_extra_at_fill_price"] = (vw["qty"] - vs["units"]) * vw["paid"]
vt["drift_on_target_units"] = vs["units"] * (vw["paid"] - vs["price"])
vt["drift_on_filled_units"] = vw["qty"] * (vw["paid"] - vs["price"])
vt["three_extra_at_sheet_price"] = (vw["qty"] - vs["units"]) * vs["price"]
assert abs(vt["three_extra_at_fill_price"] + vt["drift_on_target_units"] - vt["change"]) < 1e-6
assert abs(vt["three_extra_at_sheet_price"] + vt["drift_on_filled_units"] - vt["change"]) < 1e-6

bonds = {}
b_sheet_dirty = b_sheet_clean = b_sheet_acc = b_wins_clean = 0.0
for k in ("T 4.750% 15-Feb-2037", "T 4.500% 15-May-2038", "T 4.375% 15-Nov-2039", "T 4.250% 15-Nov-2040",
          "T 3.125% 15-Nov-2041"):
    s, w, bl = sheet[k], snap[ALIAS[k]], bookl[k]
    face = s["units"]
    assert face == w["qty"] * 1000, k
    assert abs(bl["clean"] + bl["accrued"] - s["price"]) < 1e-9, k   # the sheet's bond price is Book L's clean + accrued
    sd, sc, sa = face * s["price"] / 100, face * bl["clean"] / 100, face * bl["accrued"] / 100
    wc = w["qty"] * w["paid"]
    b_sheet_dirty += sd
    b_sheet_clean += sc
    b_sheet_acc += sa
    b_wins_clean += wc
    bonds[k] = {"face": face, "sheet_clean_per100": bl["clean"], "sheet_accrued_per100": bl["accrued"],
                "sheet_dirty_per100": s["price"], "wins_clean_per1000": w["paid"], "clean_drift": round(wc - sc, 2)}

etf_sheet = sum(sheet[k]["units"] * sheet[k]["price"] for k in ("IBTM", "IBTO", "IBTP", "IBTQ", "IBTR", "VT"))
etf_wins = sum(snap[ALIAS[k]]["qty"] * snap[ALIAS[k]]["paid"] for k in ("IBTM", "IBTO", "IBTP", "IBTQ", "IBTR", "VT"))
holdings_at_cost = etf_wins + b_wins_clean
residual = 300_000 - holdings_at_cost - cash_wins - COMMISSIONS
assert abs(residual - ACCRUED_WINS) < 0.005, residual       # 8g's accrued interest is the residual
sheet_cash_exact = 300_000 - etf_sheet - b_sheet_dirty - COMMISSIONS
bond_drift = (b_wins_clean + ACCRUED_WINS) - b_sheet_dirty
total_change = fund_drift + vt["change"] + bond_drift
cash_gap_exact = cash_wins - sheet_cash_exact
assert abs(-total_change - cash_gap_exact) < 0.005

out.update({
    "ibond_funds": {"lines": lines, "drift_total": round(fund_drift, 2)},
    "vt": {k: (round(v, 2) if isinstance(v, float) else v) for k, v in vt.items()},
    "six_funds_drift_on_filled_units": round(fund_drift + vt["drift_on_filled_units"], 2),
    "bonds": {"lines": bonds, "sheet_dirty": round(b_sheet_dirty, 2), "sheet_clean": round(b_sheet_clean, 2),
              "sheet_accrued": round(b_sheet_acc, 2), "wins_clean": round(b_wins_clean, 2),
              "wins_accrued_8g": ACCRUED_WINS, "clean_drift": round(b_wins_clean - b_sheet_clean, 2),
              "accrued_drift": round(ACCRUED_WINS - b_sheet_acc, 2), "drift_dirty": round(bond_drift, 2),
              "basis": "sheet bond prices = Book L clean + accrued per $100, WInS screens 5 Oct 01:18 ET (asserted)"},
    "cash": {"sheet_shown": sheet_cash_shown, "sheet_exact_from_its_prices": round(sheet_cash_exact, 2),
             "wins": cash_wins, "gap_vs_shown": round(cash_wins - sheet_cash_shown, 2),
             "gap_vs_exact": round(cash_gap_exact, 2)},
    "reconciliation": {"ibond_funds": round(fund_drift, 2), "vt": round(vt["change"], 2), "bonds": round(bond_drift, 2),
                       "commissions": 0.0, "fills_less_sheet": round(total_change, 2)},
    "zones": {"first_fill": "Tue 6 Oct 7:55 PM ET = Wed 7 Oct 10:55 AM Sydney",
              "last_fill": "Wed 7 Oct 8:27 PM ET = Thu 8 Oct 11:27 AM Sydney"},
})
print("iBond funds against the 2 Oct closes: %+.2f  %s" % (fund_drift, {k: v["drift"] for k, v in lines.items()}))
print("VT: sheet 164 x %.2f = %.2f; filled 167 x %.2f = %.2f; change %+.2f = three extra at fill %.2f %+.2f drift on 164"
      " (or three at sheet %.2f %+.2f drift on 167)" % (vs["price"], vt["sheet_cost"], vw["paid"], vt["fill_cost"],
                                                      vt["change"], vt["three_extra_at_fill_price"],
                                                      vt["drift_on_target_units"], vt["three_extra_at_sheet_price"],
                                                      vt["drift_on_filled_units"]))
print("six funds on filled units: %+.2f" % out["six_funds_drift_on_filled_units"])
print("bonds (dirty, against the 5 Oct check): sheet %.2f, fills %.2f + %.2f accrued = %.2f; drift %+.2f (clean %+.2f, accrued %+.2f)"
      % (b_sheet_dirty, b_wins_clean, ACCRUED_WINS, b_wins_clean + ACCRUED_WINS, bond_drift,
         b_wins_clean - b_sheet_clean, ACCRUED_WINS - b_sheet_acc))
print("cash: sheet shows %.0f, its own prices give %.2f; WInS %.2f; gap %.2f vs shown, %.2f vs exact"
      % (sheet_cash_shown, sheet_cash_exact, cash_wins, cash_wins - sheet_cash_shown, cash_gap_exact))
print("fills less sheet: %+.2f = funds %+.2f + VT %+.2f + bonds %+.2f" % (total_change, fund_drift, vt["change"], bond_drift))
OUT.write_text(json.dumps(out, indent=1))
print("wrote", OUT.name)
