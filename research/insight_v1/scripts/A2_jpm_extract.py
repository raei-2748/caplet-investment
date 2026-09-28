"""A2_jpm_extract.py - read the J.P. Morgan 2026 LTCMA U.S. dollar matrix straight from the PDF in the repo.

What it does (plain English): opens the PDF with pypdf, finds each asset-class row, and prints the four numbers JPM
gives (compound return 2026, arithmetic return 2026, annualised volatility, compound return 2025) plus the
correlations that matter for Laura's plan. "Compound" = the growth rate you actually get over many years (geometric);
"arithmetic" = the simple average of yearly returns, which is always higher when returns are volatile.
It also checks the column order with a formula: arithmetic ~ compound + volatility^2 / 2.

Inputs (with status labels):
- competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf, page 2 (VERIFIED-REPO-FILE; team download of
  the primary J.P. Morgan Asset Management file; "data as of September 30, 2025"; horizon 10-15 years).
- Column order (compound 2026, arithmetic 2026, volatility, compound 2025): read from the header positions on
  page 2 and confirmed by the volatility check below (it fails for any other order).

How to run (from the repo root):
    .venv/bin/python research/insight_v1/scripts/A2_jpm_extract.py
"""
import re

from pypdf import PdfReader

PDF = "competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf"
WANT = ["U.S. Inflation", "U.S. Cash", "U.S. Intermediate Treasuries", "U.S. Long Treasuries", "TIPS",
        "U.S. Aggregate Bonds", "U.S. Short Duration Government/Credit", "U.S. Inv Grade Corporate Bonds",
        "U.S. High Yield Bonds", "World Government Bonds hedged", "U.S. Large Cap", "U.S. Mid Cap", "U.S. Small Cap",
        "EAFE Equity", "Emerging Markets Equity", "AC Asia ex-Japan Equity", "AC World Equity",
        "U.S. Equity Minimum Volatility Factor", "U.S. REITs", "Commodities", "Gold"]
CORR_WITH = ["U.S. Inflation", "U.S. Cash", "U.S. Intermediate Treasuries", "U.S. Long Treasuries", "TIPS",
             "U.S. Aggregate Bonds", "U.S. Large Cap", "AC World Equity"]


def main():
    text = PdfReader(PDF).pages[1].extract_text().replace("\xa0", " ")
    lines = [l.strip() for l in text.splitlines()]
    num = r"-?\d+\.\d\d"
    rows, order = {}, []
    for l in lines:
        m = re.match(rf"^([A-Za-z].*?)\s+((?:{num}\s*)+)$", l)
        if m:
            name, vals = m.group(1).strip(), [float(x) for x in re.findall(num, m.group(2))]
            rows[name] = vals
            order.append(name)
    print(f"Parsed {len(order)} asset rows from {PDF} page 2 ('data as of September 30, 2025').")
    print("\nColumns: compound 2026 | arithmetic 2026 | volatility | compound 2025 | check: comp + vol^2/2")
    for n in WANT:
        c, a, v, c25 = rows[n][:4]
        print(f"  {n:<40} {c:>5.2f} | {a:>5.2f} | {v:>5.2f} | {c25:>5.2f} | {c + (v / 100) ** 2 / 2 * 100:>5.2f}")
    print("\nCorrelations (lower-triangular matrix; column k = k-th asset row):")
    idx = {n: i for i, n in enumerate(order)}
    def corr(x, y):
        i, j = idx[x], idx[y]
        if i < j:
            i, j = j, i
        return rows[order[i]][4 + j]
    hdr = "".join(f"{c[:12]:>13}" for c in CORR_WITH)
    print(f"  {'':<40}{hdr}")
    for n in WANT:
        print(f"  {n:<40}" + "".join(f"{corr(n, c):>13.2f}" for c in CORR_WITH))


if __name__ == "__main__":
    main()
