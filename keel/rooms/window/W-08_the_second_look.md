# W-08: the second look (the Window, Tue 3 Nov 2026, round 7 beat 2; huddle H-021)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code). MODEL. Not for submission.

**Question.** V54 P8 names one look at the reinvestment gap: "Before she names the range, we price that gap at that
day's yields, plus a cushion, and move that much from the stocks Laura keeps into Treasuries". P9: "From 2033, the
ladder and the money set aside for its gap become the operating reserve". The model behind every cheque figure since
L-13 also takes a second look in January 2033: `at_2033` (`../lab/L-11_birthday_cure/run.py:60-66`) is called by
L-16 with `need = S33 + C_`, so the gap is priced again at that day's yields, the cushion added again, and the reserve
topped up from her kept stocks first, then the gift. Does the text's one look carry the cheques by itself?

**History (Tess, H-021).** The second look is older than V54. V29 said "tops up once", V30 "topped up once"
(`../../ips_rewrite/drafts/D10/ips.txt:17`); V31 dropped it, and IDEA_LEDGER E2 ("One scheduled top-up in Jan 2033,
then the reserve never changes") was ruled **FR, "Detail behind D6"**, before anyone priced it. V53's cut order line
was a priority, never a second look.

**Method.** `W-08_the_second_look.py` reuses the Lab's L-16 chain unchanged and patches its block the way Laura's
Room's LR-10 does. A0 must still equal L-14's XR (the Lab's assert passes). Curve 22 Oct 2026 (treasury.gov par) |
J.P. Morgan 2027 LTCMA global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 unless S0. About 80 s for both
worlds. Results: `W-08_results.json`.
- **First try (W0, W1), withdrawn.** It skipped the 2033 top-up but left two faults Kai found in round 2: what the
  stocks can't cover on naming day lowered the range and then went back to Laura instead of to the cheques (the gift
  was capped at the quoted top and the rest became hers), and the score counted max(final gap, the gap seen in 2033),
  so futures where yields rose again after 2033 still counted as short. Its 86.76% / 45.77% are **not** findings.
- **Fair test (A0f, W0f, W1f).** What the stocks can't cover leaves the range's money on naming day into the same
  bills (LR-10's move at phi 0, up to everything locked), and every arm is scored on the realised gap.

## Results (MODEL)
| Arm | World | Cheques paid in full | Short over $1,000 | Short, median / 90th when short | Worst tenth of naming-day gaps: a cheque short | Top reached | Gift mean | Laura's 2042 mean |
|---|---|---|---|---|---|---|---|---|
| A0f with the second look (cushion + Jan 2033) | base | 99.87% | 0.02% | $348 / $1,213 | 0.04% | 97.84% | $159,956 | $49,270 |
| **W0f V54 as written (cushion, one look)** | base | **96.01%** | **2.44%** | **$1,341 / $3,822** | **4.56%** | 99.29% | $159,980 | $49,678 |
| W1f no cushion, one look | base | 74.70% | 22.11% | $3,886 / $8,225 | 61.48% | 99.01% | $161,121 | $55,347 |
| A0f | yields 2 pts lower for good | 99.85% | 0.02% | $370 / $1,158 | 0% | 95.86% | $141,771 | $23,725 |
| **W0f** | yields 2 pts lower for good | **94.39%** | **3.27%** | **$1,274 / $3,598** | **0.89%** | 99.55% | $141,826 | $24,038 |
| W1f | yields 2 pts lower for good | 49.39% | 45.28% | $3,625 / $7,606 | 78.08% | 99.48% | $146,376 | $24,532 |

(L-16's own A0, scored its way: 99.82% base, 99.68% yields lower; reproduced identically today.)

## What it means
- **The second look matters, but it is the smaller of the two unnamed steps.** With one look, a cheque is short in
  about 1 base future in 25 (1 in 18 if yields fall 2 points for good), usually by about $1,300; with both, about 1 in
  770. The cushion is the big one (without it, 1 in 4).
- **It costs the gift almost nothing** (mean moves by $24 base, $55 yields lower) and costs her a little flexibility
  (her 2042 mean $49,270 with it v $49,678 without), because the top-up takes her kept stocks first. The top is
  reached a little more often with one look (99.3% v 97.8%), because the cheques then never take from the gift.
- **Why one look leaves a hole:** the gap is priced on naming day at that day's rates, and the money sits in 3-month
  bills (LR8 `run.py:25-29`), so a further fall in yields before 2033 widens the gap with nothing to offset it.
- **Kai's other way, no second look needed** (`W-08c_kai_no_reinvestment_lock.py`, deterministic, re-run identical):
  on naming day, price the gap as if no interest earns anything from that day on and buy Treasuries maturing before
  each January with it, their own coupons also held at 0%. Cost on the 22 Oct curve **$11,201** (A0 sets aside the gap
  at that day's yields, about nothing on this curve, plus $7,500); with yields 2 points lower **$22,867** (A0: $18,996
  + $7,500 = $26,496). After that, 2033 has nothing to check. A design change: the Genius Lab tests it (request).

## For the IPS (no figure, Book 11)
Reopen IDEA_LEDGER E2. Either name the January 2033 look in P9, where the case asks for the reserve's "size and
initial asset composition" (case :95-96), or take Kai's lock and say the gap is priced "as if its interest earned
nothing", which needs no second look. The Writing Room owns the words; constraints in
`../../ips_rewrite/inbox/2026-11-03_window.md` s1.

## For the Final Report
The two looks (or the lock), the order (her kept stocks, then the gift), this table's base rows, and the withdrawn
first try as a lesson in testing your own test.
