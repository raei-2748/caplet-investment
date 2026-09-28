"""D12 (Overflow Researcher, client side), question M234: how many outside readers does a restate-it test need?

What it computes
1. Nielsen-Landauer problem-discovery curve: share of problems found with n readers, 1 - (1 - L)^n, for L = 31%.
2. For one specific misreading that a share p of all readers would make, the chance that at least one of n readers
   makes it, and the chance that at least two do (two = a pattern worth changing the wording for).
3. Time cost of a test of the 50-word pitch plus the IPS rule sentences.

Inputs and status labels
- L = 31% "typical value ... averaged across a large number of projects", and "testing no more than 5 users":
  https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ (Jakob Nielsen, 2000-03-18), read
  2026-09-28 (VERIFIED-PRIMARY). The formula image did not render in the text read; the formula
  N(1-(1-L)^n) is from Nielsen & Landauer (1993), cited on that page (the form is SNIPPET-UNVERIFIED as text, but the
  page's "85%" for 5 users matches it: 1 - 0.69^5 = 0.84).
- "Conduct between 6 to 9 interviews" for paraphrase testing: https://digital.gov/guides/plain-language/test/paraphrase-testing
  (U.S. plain-language guide), read 2026-09-28 (VERIFIED-PRIMARY).
- Misreading rates p (10-50%) and minutes per reader: ASSUMPTION (illustrative).
- Readers are independent and alike: ASSUMPTION (the Nielsen page itself warns the formula holds only for comparable
  users).

Run from the repo root:  .venv/bin/python research/insight_v1/scripts/D12_reader_test.py
"""
from math import comb

L = 0.31
print("== 1. Share of problems found (Nielsen-Landauer, L = 31%) ==")
for n in (1, 3, 5, 6, 9):
    print(f"  n={n}: {1 - (1 - L) ** n:.0%}")


def p_at_least(k, n, p):
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


print("\n== 2. One specific misreading made by a share p of readers ==")
print(f"  {'p':>5s} " + " ".join(f"n={n}: >=1 / >=2   " for n in (5, 6, 9)))
for p in (0.10, 0.20, 0.31, 0.50):
    cells = []
    for n in (5, 6, 9):
        cells.append(f"{p_at_least(1, n, p):5.0%} / {p_at_least(2, n, p):4.0%}   ")
    print(f"  {p:5.0%} " + " ".join(cells))

print("\n== 3. Time cost (ASSUMPTION: 10 min per reader for pitch + 5-8 rule sentences, 2 students per session) ==")
for n in (5, 6):
    print(f"  n={n}: {n * 10} reader-minutes; {n * 10 * 2 / 60:.1f} student-hours; one round before Oct 30, "
          "a second after the fixes")
