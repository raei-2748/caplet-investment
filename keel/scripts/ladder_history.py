"""FICTION (Team Keel). Jun's daily number, re-run for every U.S. close since trading opened.
Cost on 1 Jan 2027 of ten $50,000 payments (1 Jan 2033..2042), payment-date basis, same method as ladder_pv.py.
MODEL. Input: treasury.gov daily par yield curve CSV (copy in keel/library/assistant_review_2026-10/checks/)."""
import csv
import sys
from datetime import date, datetime
from pathlib import Path

import ladder_pv as lp

SRC = Path(__file__).resolve().parents[1] / "library/assistant_review_2026-10/checks/tsy_202610_22oct.csv"
TENORS = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": .25, "6 Mo": .5, "1 Yr": 1, "2 Yr": 2, "3 Yr": 3,
          "5 Yr": 5, "7 Yr": 7, "10 Yr": 10, "20 Yr": 20, "30 Yr": 30}


def rows(start=date(2026, 9, 24)):
    with open(SRC) as fh:
        for r in csv.DictReader(fh):
            d = datetime.strptime(r["Date"], "%m/%d/%Y").date()
            if d >= start:
                yield d, {t: float(r[k]) for k, t in TENORS.items()}


if __name__ == "__main__":
    print("US close    10y   30y   cost      headroom  bp   DV01")
    for d, curve in sorted(rows()):
        lp.VAL, lp.CURVE = d, curve
        c = lp.cost()
        dv01 = (lp.cost(-.01) - lp.cost(.01)) / 2
        print(f"{d}  {curve[10]:.2f}  {curve[30]:.2f}  ${c:,.0f}  ${300000 - c:>7,.0f}  {(300000 - c) / dv01:>4.0f}  ${dv01:,.0f}")
