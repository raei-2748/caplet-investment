# Kai's round 2 check (H-028, Wed 4 Nov 2026)

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code, for the fictional Kai). Not text to submit.
MODEL = a computer estimate from the script below, not a fact.

## 1. Is the ladder duration-matched "as a by-product" of one holding per January? (Felix, point 2)

**Question.** Felix says that when every payment has its own bond, the timing matches too. V57 P4 says we buy one bond
per payment rather than matching "average timing"; the locked TNA reflection 1 says the bonds remove uncertainty
"through duration-matching". If the ladder really were duration-matched, the two would agree. Is it?

**How.** Settlement 23 Oct 2026 (the WInS snapshot day). Liability: $50,000 on 1 Jan of each year 2033-2042.
- Five T-bonds: WInS clean prices of 23 Oct (`competition/wins/2026-10-23_snapshot.md`), semiannual coupons, accrued
  interest added, yield solved from the price. The solved yields (5.05, 5.10, 5.23, 5.29, 5.37%) reproduce the snapshot's
  own implied yields, so the pricer agrees with the earlier one.
- Five iBond funds: iShares effective durations "as of Oct 16, 2026" (IBTM 5.02, IBTO 5.68, IBTP 6.39, IBTQ 7.03, IBTR
  7.56 years) as recorded in `keel/library/assistant_review_2026-10/oct20/artic_fixed/attribution_pack_checked.md` line 72.
  Not re-fetched today. Their cheques are discounted at a flat 5.00%, inside the funds' 4.94-5.08% yield range.
- Each rung weighted by the present value of its $50,000 (own-rung sizing: each rung costs what its cheque is worth).
- Duration = modified duration (how much the price moves for a 1-point move in rates).

**Result (MODEL, 23 Oct prices).**

| Rung (pays 1 Jan) | Holding's duration | Cheque's duration | Short by |
|---|---|---|---|
| IBTM (2033) | 5.02 | 6.04 | 1.02 |
| IBTO (2034) | 5.68 | 7.02 | 1.34 |
| IBTP (2035) | 6.39 | 7.99 | 1.60 |
| IBTQ (2036) | 7.03 | 8.97 | 1.94 |
| IBTR (2037) | 7.56 | 9.94 | 2.38 |
| 4.75% Feb-2037 (2038) | 7.97 | 10.92 | 2.95 |
| 4.50% May-2038 (2039) | 8.66 | 11.89 | 3.23 |
| 4.375% Nov-2039 (2040) | 9.48 | 12.85 | 3.37 |
| 4.25% Nov-2040 (2041) | 10.03 | 13.83 | 3.79 |
| 3.125% Nov-2041 (2042) | 11.12 | 14.79 | 3.67 |
| **Whole ladder (weighted)** | **7.61** | **9.99** | **2.38** |

- The ladder moves about **76%** as much as the payments when rates move: about $224 against $294 per 0.01 point on a
  ladder sized at the payments' value, $294,383.
- **Every rung is shorter than its cheque.** On the T-bonds, most of the gap comes from coupons arriving years before the
  payment (2.1 to 3.7 years of the gap). Maturing before the January adds only 0.85 years (Feb-2037, 10.5 months early),
  0.62 (May-2038) and 0.13 (the three November bonds).
- **Cross-check.** The independent 19 Oct model in `keel/library/assistant_review_2026-10/oct20/ldi/ldi_second_opinion.md`
  line 70 found 7.6 against 9.9 years, a 78% hedge ratio, on the 19 Oct curve. Same answer, two curves, two scripts.

**What it means.** One holding per January matches the **dates**, not the **duration**. Felix's "as a by-product" is only
roughly true: three-quarters. The missing quarter is the reinvestment risk V57 P8 names as "the ladder's one weakness".
So V57 P4 ("We do the second") is the accurate description, and the locked TNA reflection 1 ("through
duration-matching") is the loose one. The TNA's own reflection 2 already uses the right idea: "each of Laura's payments
rests on a dedicated instrument". No IPS word fixes a locked TNA, and bending P4 to echo "duration-matching" would make
the IPS untrue.

## 2. Point 1, read against the locked text and the instructions (no calculation)
- `keel/ips_rewrite/drafts/FINAL/ips.txt`, P4: "A Treasury held to maturity pays exactly what it promised, whatever
  markets do." True of a Treasury security. A fund is not "a Treasury".
- Locked TNA (`keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt`): the IBTM note says "the final payout is not
  fixed" (line 13); reflection 2 says "their terminal payout is a net asset value, as opposed to a promise of par"
  (line 15). The distinction is already made once, in one clause, in a deliverable judged with the IPS.
- `keel/INSTRUCTIONS.md` I35 (Ray, 26 Oct): iBonds held to the December liquidation are "near-ironclad"; a T-bond vs
  iBond distinction, "if made at all, is one concise, direct clause".
- Scope of "rounded down": V57's 2031 paragraph says "The bottom is the floor, rounded down"; the floor is the "Treasury
  fund maturing in late 2032" bought with the 2028 deposit. It does not cover the five funds that pay January cheques,
  so it can't answer "and the funds?" if "bond" is added.

## 3. Word counts (`keel/office/tools/textcheck.py`, on scratch copies)
| Text | By spaces | Split on hyphens (the count to quote) |
|---|---|---|
| V57 as it stands | 493 | **496** |
| V57 with "A Treasury bond held to maturity" | 494 | **497** (the house cap) |
Kai's fix (none) keeps 496.

## 4. The script (re-runnable: `python3 kai_dur.py`)
```python
from datetime import date
S = date(2026, 10, 23)
def yrs(d): return (d - S).days / 365.25
def bond_cfs(cpn, mat, face=100.0):
    cfs = []; y, m, dd = mat.year, mat.month, mat.day
    while True:
        d = date(y, m, dd)
        if d <= S: break
        cfs.append((d, cpn / 2 + (face if d == mat else 0.0)))
        m -= 6
        if m <= 0: m += 12; y -= 1
    cfs.sort(); prev = date(y, m, dd); nxt = cfs[0][0]
    return cfs, cpn / 2 * (S - prev).days / (nxt - prev).days
def price(cfs, y): return sum(c / (1 + y / 2) ** (2 * yrs(d)) for d, c in cfs)
def solve_y(cfs, dirty):
    lo, hi = 0.0, 0.2
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if price(cfs, mid) > dirty else (lo, mid)
    return (lo + hi) / 2
def mod_dur(cfs, y):
    return sum(yrs(d) * c / (1 + y / 2) ** (2 * yrs(d)) for d, c in cfs) / price(cfs, y) / (1 + y / 2)
rows = [(py, 0.05, ed) for py, ed in [(2033, 5.02), (2034, 5.68), (2035, 6.39), (2036, 7.03), (2037, 7.56)]]
for cpn, mat, clean, py in [(4.75, date(2037, 2, 15), 97.6134, 2038), (4.50, date(2038, 5, 15), 94.8129, 2039),
                            (4.375, date(2039, 11, 15), 91.9574, 2040), (4.25, date(2040, 11, 15), 89.7877, 2041),
                            (3.125, date(2041, 11, 15), 76.9963, 2042)]:
    cfs, ai = bond_cfs(cpn, mat); y = solve_y(cfs, clean + ai); rows.append((py, y, mod_dur(cfs, y)))
pv = a = l = 0
for py, y, ad in rows:
    t = yrs(date(py, 1, 1)); p = 50000 / (1 + y / 2) ** (2 * t)
    pv += p; a += p * ad; l += p * t / (1 + y / 2)
print(f"assets {a/pv:.2f}y, payments {l/pv:.2f}y, ratio {a/l:.0%}")   # assets 7.61y, payments 9.99y, ratio 76%
```
