"""A2_taiwan_cci.py - Taiwan construction cost index (CCI, 營造工程物價指數) from the official DGBAS platform.

Why: the facility will be built in Taiwan, so building-cost inflation matters for the co-sponsor range. The headline
"+6.54% y/y in August 2026" was only a news snippet, and the official download files (ws.dgbas.gov.tw) could not be
opened from this environment (TLS failure / egress block). The DGBAS "CCI calculation platform" on www.stat.gov.tw
is reachable. It returns, for any chosen class, (a) that class's index and (b) the total index EXCLUDING that class.

Method (plain English): the total index is a fixed-weight average of its parts (Laspeyres, base 2021 = 100), so
    total = w * class + (1 - w) * total_excluding_class.
Asking for two different classes (wages; machinery rental) gives two such equations per month with the same total;
least squares solves for the two weights and hence the total index each month. The fit error is printed.

Inputs (with status labels):
- DGBAS CCI platform, https://www.stat.gov.tw/CCI/CCI_Site/CCIPrice/PartialPriceClassesList.aspx (POST, cmd PrCL),
  category ids 3 (wages, 工資類) and 10 (machinery/equipment rental, 機具設備租金類): VERIFIED-PRIMARY when
  downloaded live (index values published to 2 decimals).
- Fixed-weight (Laspeyres) aggregation: ASSUMPTION about the index formula; checked by the size of the fit error.
- Base-period centre 2021-07-01 for the long-run average growth: ASSUMPTION (the base is the 2021 annual average).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/A2_taiwan_cci.py
Results on 2026-09-27 are recorded in research/insight_v1/phase_A/fact_register.md (Taiwan/FX/inflation section).
"""
import html
import json
import re
import urllib.request
from datetime import date

import numpy as np

URL = "https://www.stat.gov.tw/CCI/CCI_Site/CCIPrice/PartialPriceClassesList.aspx"


def query(category_ids, by=2024, bm=1, ey=2026, em=8):
    inner = json.dumps({"CategoriesId": "", "CategoryIds": category_ids, "CategoryType": "PCLS",
                        "CorrespondsBYr": by, "CorrespondsBMn": bm, "CorrespondsEYr": ey, "CorrespondsEMn": em})
    body = json.dumps({"cmd": "PrCL", "data": inner}).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json",
                                                          "User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        page = json.loads(r.read().decode("utf-8"))["PageHtml"]
    out = {}
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.S):
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", c))).strip()
                 for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
        if len(cells) == 3 and re.match(r"^\d+/\d+$", cells[0]):
            roc_y, m = cells[0].split("/")
            out[(int(roc_y) + 1911, int(m))] = (float(cells[1]), float(cells[2]))  # (total excl. class, class)
    return out


def main():
    wage, rent = query("3"), query("10")
    months = sorted(set(wage) & set(rent))
    a = np.array([[wage[k][1] - wage[k][0], -(rent[k][1] - rent[k][0])] for k in months])
    b = np.array([rent[k][0] - wage[k][0] for k in months])
    (w1, w2), res, _, _ = np.linalg.lstsq(a, b, rcond=None)
    tot = {k: wage[k][0] + w1 * (wage[k][1] - wage[k][0]) for k in months}
    tot2 = {k: rent[k][0] + w2 * (rent[k][1] - rent[k][0]) for k in months}
    err = max(abs(tot[k] - tot2[k]) for k in months)
    print(f"Source: {URL} (DGBAS CCI platform), {months[0]} to {months[-1]}, base 2021 = 100")
    print(f"Implied weights: wages {w1:.4f}, machinery rental {w2:.4f}; max disagreement between the two "
          f"reconstructions {err:.3f} index points")
    print("\n month    total(derived)  wages  total-excl-wages  rental")
    for k in months:
        print(f" {k[0]}-{k[1]:02d}   {tot[k]:>8.2f}      {wage[k][1]:>7.2f}   {wage[k][0]:>8.2f}      {rent[k][1]:>7.2f}")
    last = months[-1]
    prev = (last[0] - 1, last[1])
    print(f"\nYear-on-year to {last[0]}-{last[1]:02d}: total {(tot[last] / tot[prev] - 1) * 100:+.2f}% (derived); "
          f"wages {(wage[last][1] / wage[prev][1] - 1) * 100:+.2f}%; rental {(rent[last][1] / rent[prev][1] - 1) * 100:+.2f}%;"
          f" total excluding wages {(wage[last][0] / wage[prev][0] - 1) * 100:+.2f}%")
    yrs = (date(last[0], last[1], 15) - date(2021, 7, 1)).days / 365.25
    print(f"Average growth since the 2021 base (centre 2021-07-01, {yrs:.2f} years): "
          f"{((tot[last] / 100) ** (1 / yrs) - 1) * 100:.2f}% a year")
    jan24 = (2024, 1)
    if jan24 in tot:
        y2 = (date(last[0], last[1], 1) - date(2024, 1, 1)).days / 365.25
        print(f"Average growth {jan24[0]}-{jan24[1]:02d} to {last[0]}-{last[1]:02d}: "
              f"{((tot[last] / tot[jan24]) ** (1 / y2) - 1) * 100:.2f}% a year")


if __name__ == "__main__":
    main()
