# FICTION (the room) + real work (the test). L-10: last in line (Laura's promises as a capital structure)

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Genius Lab, Tue 27 Oct
2026, 13:40 Sydney. Script `L-10_last_in_line/run.py`, results `L-10_last_in_line/results.json`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | basis: `../../library/ips_numbers_2026-10/ips_numbers.py` unchanged except the patches in the script | MODEL.**

**Why this, today.** The case asks how the IPS "guides construction and decisions as needs change" and says the range
"must also protect the portfolio's ability to fund the ten-year operating commitment" (case :119-120). The Courtroom's
ruling this morning lists "as needs change" as still missing, and the Library asked for one probability of exhaustion
in the IRS's sense (Rev. Rul. 77-374). North stars 3 and 4; Investment Strategy, Portfolio Analysis. IPS line that
could change: the certainty definition and the 2033 step.

**Hypothesis.** Read Laura's plan as a capital structure. Losses run down a fixed order (D1a): leftover cash, then
Laura's kept half of the stock fund, then the gift above the 2031 bottom, then the bottom, and the ten payments last.
In every "as needs change" stress the payments stay whole in at least 99.5% of paths, except a missing 2028 deposit
after yields fall before the build.

**Kai's roast (before the run).** "You've put a junk-bond costume on a draw order. 'Senior tranche' means 'we pay the
payments first', which every team will say. Your 99.5% is circular: you assumed the Treasury pays. The only number
worth having is the one nobody's looked at: after 2033 the gift is gone, and the coupons keep leaking into a half
that's sitting in stocks."

**Test.** Nine scenarios on the model the whole office uses. Wrong if the payments fail in more than 0.5% of paths in
the base or in any stress except S5.

| Stress (MODEL, 22 Oct curve, 7.5%) | Laura's half used | top missed | bottom missed | **a payment short** | median short |
|---|---|---|---|---|---|
| S0 base, rates and stocks independent | 33% | 23% | 0.75% | **6.8%** | $3,154 |
| S1 base, yields and stocks fall together (rho 0.5) | 33% | 25% | 1.3% | **8.4%** | $3,210 |
| S2 2028 deposit halved ($75k) | 33% | 26% | 5.3% | 15% | $3,234 |
| S3 2028 deposit missing | 57% | (no range) | (no range) | 58% | $16,593 |
| S4 yields 1pt lower before the Jan 2027 build | 46% | 28% | 3.8% | 17% | $2,568 |
| S5 S4 + 2028 deposit missing | 98% | (no range) | (no range) | 98% | $43,646 |
| S6 yields fall 2pt just after the build, for good (re-run after the audit) | 73% | 48% | 20% | 39% | $3,350 |
| S7 stocks halve before the 2031 range is set | 33% | 26% | 5.0% | 15% | $3,238 |
| S8 stocks halve after the 2031 range is set | 33% | 98% | 5.0% | 15% | $3,238 |

**Result: hypothesis FALSE, and Kai called it.** The weakest promise in the plan is not the top of the range, nor
the bottom. It's the ten payments. In 6.8-8.4% of paths a payment comes up short after 2033 (median about $3,200,
under a tenth of one payment). Why: the gift leaves in 2033, but the coupons of the 2037-41 bonds are reinvested
until 2042, and after 2033 the only thing behind the payments is Laura's kept half, in stocks. The order is right; the
*timing* is wrong. The plan pays its junior creditor before its senior one is safe. Every number we have quoted as
"the risk is already priced" (0.75-1.43% below the bottom, R05; the Courtroom's WO-R2 ruling; the Library's "a seventh
of the IRS's 1 in 20") measured the bottom. The IRS test measures the fixed payments running out. On that footing
our plan sits at 1 in 12 to 1 in 15: above the IRS's 1 in 20. (The 16 Oct number sheet had this at 5.6% on the 15 Oct
curve at 7.0%; nobody carried it forward.)

**The cure: a coverage test, borrowed from how CLOs protect their senior notes.** A CLO checks a coverage ratio before
it pays anything to its junior notes; when the test fails, cash that would have gone down the stack is diverted to
the senior notes until the test passes again (mechanism to source: Library request below). Our version is one rule in 2033: *before
anything goes to the facility, at least $10,000 must stay behind with Laura for the payments; if it doesn't, the
difference is held back from the gift, from the top first and then the bottom, and follows to the facility once the
payments no longer need it.* Held as cash, no interest assumed (cautious).

| H = $10,000, top then bottom (MODEL) | payment short | top reached (incl. later release) | below bottom in 2033 / in the end | trap used | median held back | median gift 2033 |
|---|---|---|---|---|---|---|
| S0, no trap -> trap | 6.8% -> **0.01%** | 77% -> 75% | 0.75% -> 2.9% / 1.2% | 18% | $7,493 | $165,528 -> $165,292 |
| S1, no trap -> trap | 8.4% -> **0.01%** | 75% -> 74% | 1.3% -> 4.3% / 1.9% | 20% | $8,651 | $165,492 -> $165,311 |
| S6, no trap -> trap | 39% -> **0.02%** | 52% -> 48% | 20% -> 33% / 23% | 62% | $10,000 | $156,663 -> $149,377 |

Top-only trapping fails (S1: 1.75% still short): the paths that need it are the ones where the gift is already at the
bottom, so the bottom must be allowed to wait (which D1a already says: the floor gives before the payments).
H = $20k buys nothing more and holds back twice as often. S6 is the honest worst case: if yields drop two points for
good the day after the build, the trap still keeps the payments whole (0.02%), and it does it by spending the bottom,
which is the order D1a chose. In that world the range itself fails one time in five, trap or no trap.

**Other findings for "as needs change" (all MODEL):** (1) A crash *before* 2031 barely moves the odds of reaching the
top (26% missed vs 25%): the range is set after it, so the promise shrinks with the money. A crash *after* 2031 misses
the top almost surely (98%) but the bottom holds in 95%. That is the case's "favorable and unfavorable outcomes" item
in two sentences. (2) The ten payments lean on the 2028 deposit in 47% of paths (Jan 2027 cost above $300k on this
basis, median gap $9,758): without it, 58% of paths leave a payment short. So the 2028 deposit's first job is the
payments, then the floor, then stocks, exactly the locked IBTR note.

**Verdict: ADOPT the coverage test as a rewrite candidate** (IPS: one sentence; Final Report: the table and the CLO
source). **BIN the hypothesis** (kept here: the stack's order was never the problem, its clock was). "Senior tranche"
and "capital structure" stay out of the IPS: Kai is right that the costume adds nothing; the rule does the work. Cost
of the cure: the gift waits in a fifth of paths, and "inside the range" in 2033 drops from ~99 in 100 to ~96 (final
~98). Courtroom to rule (request below). Audit (numbers-auditor, 27 Oct): PASS WITH NOTES. S0 0.0677 and S1 0.0838 re-derived independently from the base
model's own post-2033 test; inside-range 0.9872 = 1 - 0.0128 (R05 exactly). Fixed before publishing: S6 first put the
2pt fall into the build-day yield, so it stressed nothing (re-run above); the 2033 gap now counts both halves. Notes kept:
the base model grows Laura's half to 2042 before setting it against gaps due from 2034 (optimistic), but throws away
any gift above the top instead of keeping it (conservative: misses 8.4% -> 7.6% if kept, and a cheaper trap source);
and held-back money is only surely free after the last payment (2042), so the 'in the end' columns flatter the 2033 view.

**Plain-English lesson.** Who gets paid first is two questions: in what order, and when. Most plans only answer the first.
