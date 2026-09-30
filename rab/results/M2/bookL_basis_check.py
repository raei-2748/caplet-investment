"""WS4: is the WInS-listed ladder (Book L) really dearer than STRIPS, or only sized bigger?

Standard library only. Reads the Gate-A-passed M1 output (rab/models/out/m1_results.json, section E.bookL) and
rescales each Book L rung so that, with coupons and principal reinvested at the 28 Sep curve's forward rates,
it delivers exactly $50,000 on its payment date. Compares the rescaled cost with the locked STRIPS cost.

Answers WS7's fact-audit item (STATUS.md [ws7-fact-audit], 30 Sep): the Book L vs STRIPS cost gap is a sizing
artefact (end-date discount factors + rounding up), since Book L delivers $507,479 at forwards (numbers.yaml
reinvest.bookL_delivered.at_curve_forwards).

Run: python rab/results/M2/bookL_basis_check.py  (from the worktree root) > rab/results/M2/bookL_basis_check.txt
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
M1 = ROOT / "rab/models/out/m1_results.json"
NUMBERS = ROOT / "rab/numbers.yaml"
PAYMENT = 50_000.0
COMMISSION = 5 * 25 + 5 * 10  # five iBonds ETF trades at $25, five Treasury trades at $10 (WInS schedule)


def locked_value(key):
    """Read a scalar 'value:' under a top-level-indented key of numbers.yaml without a YAML library."""
    lines = NUMBERS.read_text().splitlines()
    for i, line in enumerate(lines):
        if line.strip() == f"{key}:":
            for nxt in lines[i + 1:i + 4]:
                if nxt.strip().startswith("value:"):
                    return float(nxt.split(":", 1)[1].strip())
    raise KeyError(key)


def main():
    rows = json.loads(M1.read_text())["E"]["bookL"]
    total_cost = total_resized = total_delivered = 0.0
    print(f"{'holding':24s} {'pays':10s} {'cost':>11s} {'at fwds':>11s} {'x':>7s} {'resized':>11s}")
    for r in rows:
        k = PAYMENT / r["v_curve"]
        resized = r["cost"] * k
        total_cost += r["cost"]
        total_delivered += r["v_curve"]
        total_resized += resized
        print(f"{r['holding']:24s} {r['pays']:10s} {r['cost']:11,.2f} {r['v_curve']:11,.2f} {k:7.4f} {resized:11,.2f}")
    strips = locked_value("laura.ladder.cost_today_strips")
    print()
    print(f"Book L as sized, ex commission        {total_cost:12,.2f}")
    print(f"Book L as sized, with ${COMMISSION} commission  {total_cost + COMMISSION:12,.2f}")
    print(f"Book L delivers at forward rates      {total_delivered:12,.2f}  (target 500,000.00)")
    print(f"Book L resized to $50,000 a rung at forwards, ex commission    {total_resized:12,.2f}")
    print(f"Book L resized to $50,000 a rung at forwards, with commission  {total_resized + COMMISSION:12,.2f}")
    print(f"STRIPS, Nov-15 basis (numbers.yaml laura.ladder.cost_today_strips) {strips:12,.2f}")
    print(f"Resized Book L minus STRIPS: ex commission {total_resized - strips:+,.2f}; "
          f"with commission {total_resized + COMMISSION - strips:+,.2f}")
    print(f"Extra cost of the Sheet sizing over the resized ladder (ex commission) {total_cost - total_resized:,.2f}")


if __name__ == "__main__":
    main()
