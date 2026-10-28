# FICTION (the room) + real work (the test). L-11: a cure with a birthday

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Genius Lab, Wed 28 Oct
2026, 13:40 Sydney, round 1 beat 5 (`../../loop/rounds/2026-10-28.md`). Script `L-11_birthday_cure/run.py` (reuses
L-10's patches from its own file), results `L-11_birthday_cure/results.json`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | basis: `../../library/ips_numbers_2026-10/ips_numbers.py` + L-10's patches | MODEL.**

**For a judge, first.** The coupon gap splits in two. About four-fifths of it has already happened by January 2033 and
can simply be paid then, out of what's there. The last fifth is still to come, and that part can be bought in 2028,
the first day the money exists, as a small Treasury holding of its own. A cost is paid the day it's known; a risk is
bought the day it starts. That takes the payments from short in 1 path in 15 to short by more than $1,000 in fewer than 1 in 10,000, and it
never asks Laura's stocks to meet a deadline.

**Why this, today.** Requests from the Library (28 Oct: price the reserve bought on its birthday and the check before
every cheque; how much of the gap arrives after 2033) and the Archive (27 Oct: size the Jan 2033 set-aside). Round 1's
question: is there a cure for the coupon gap that is itself bought on its birthday, so the central idea has no
exception? North stars 3 and 4; Investment Strategy, Portfolio Analysis; Book 7's "how the reserve changes over time".
IPS lines that could change: synthesis slot 7 (how the reserve changes) and the 2028 deposit's order.

**Hypothesis.** A coupon holding bought on the 2028 deposit day, at most $10k, takes "a payment short by over $1k" below
1% in S0, S1 and S6, never sells Laura's stocks at a payment deadline, and costs the co-sponsors less than the one-time
January 2033 set-aside (champion C6).

**Kai's roast (before the run).** "A safety net for the safety net. Again: L-02 sized a 2028 buffer on 24 Oct and it
needed $15k to get to 1.3%. And 'birthday' is a greeting card: the cheques' birthday is January 2027, and that day
there's no money (headroom -$224). Whatever you buy, you'll shrink the floor to cover a $3,000 median gap."

**Test.** Five designs on the office's model, three stresses (S0 independent, S1 stocks fall with yields, S6 yields
2 points lower for good just after the build). Wrong if no size up to $10k gets under 1% in all three.

| MODEL, 22 Oct curve, 7.5% | payment short >$1k: S0 / S1 / S6 | Laura's stocks sold | top reached (S0) | below bottom in 2033: S0 / S1 / S6 | bottom (median) | gift (median) |
|---|---|---|---|---|---|---|
| D0 no rule (L-10 base, reproduced: 6.77%, 8.38%) | 5.9% / 7.4% / 35% | 37%, some at deadlines | 77% | 0.75% / 1.3% / 20% | $145k | $165.5k |
| D1 Jan 2033 set-aside, cushion $7.5k (C6, Archive A19) | 0.07% / 0.07% / 0.09% | 71% (once, Jan 2033) | 73% | 2.2% / 3.3% / 30% | $145k | $165.4k |
| D2 $7.5k bought 2 Jan 2028 **before the floor** | **0.00% / 0.00% / 0.01%** | 34% (once, Jan 2033) | 77% | **0.8% / 1.4% / 20%** | $135k | $157.2k |
| D2 $7.5k bought 2 Jan 2028 from the stock fund | 0.00% / 0.00% / 0.76% | 34% (once, Jan 2033) | 76% | 2.5% / 3.4% / 34% | $145k | $161.3k |
| D2 $5k before the floor | 0.68% / 0.68% / 1.5% | 34% | 77% | 0.8% / 1.4% / 21% | $140k | $159.9k |
| D3 a check before every cheque, no holding | 6.2% / 7.7% / 36% | 38%; at a deadline in 24% | 77% | 0.75% / 1.3% / 20% | $145k | $165.5k |

**Result: hypothesis TRUE on the payments, MIXED on the cost, and Kai wins the novelty point.**
1. **The blind spot is a fifth, not most.** Of all shortfall dollars, 81% are already visible in a January 2033
   projection (S6: 89%); only 3.7% of paths see a gap appear after 2033. What arrives later is small and bounded:
   p99 $7,146, p99.9 $8,749 (S0). That corrects bank #58's "where L-10 finds most of the shortfall": L-10's payments
   fail after 2033 because the gift has gone, not because most of the gap is late. So the 2033 check is the right
   shape for what has happened, and a block can't be the right shape for what hasn't.
2. **$7.5k bought in 2028, before the floor, is enough.** It grows to about $9.2k by 2033 in short Treasuries (bill
   rate; no interest after 2033, cautious) and covers the p99.9 of everything still to come. Payments short by over $1k:
   under 1 in 10,000 in S0 and S1, 0.01% in S6 (short by anything: 0.03%, 0.03%, 0.06%). Unused, it goes back to Laura after the tenth cheque (median $9,573).
3. **Where the $7.5k comes from decides who pays.** Before the floor (the locked 2028 order: payments, then floor,
   then stocks) the bottom rule gives about $10k less in the median path ($7.5k plus the $5k rounding), but the
   bottom is kept as often as with no rule at all (S1 98.6%, S6 80%). From the stock fund the $145k label survives,
   but the bottom is missed more (S1 3.4%) and S6 breaks it (0.76% short): falling yields shrink the fund, which is
   the interest taken up front, at the same moment they widen the gap. Wrong-way risk, in miniature.
4. **The 2033 set-aside alone does the same job for the payments, at a different price.** It keeps the $145k label
   and the median gift, but takes the cushion from the gift whenever Laura's half is short, so the bottom is missed
   2-3 times as often (S1 3.3%, S6 30% vs 20%). A smaller promise kept, or a bigger one missed: Courtroom to rule.
5. **The check before every cheque is a habit, not a cure** (BIN as a cure). With no holding behind it, it is worse
   than no rule (6.2% vs 5.9%), because it sells Laura's stocks earlier and at a payment deadline in 24% of paths,
   the exact thing locked reflection 3 rules out. Tess's own break was right: theatre has a next show; we have no
   new money.
6. **Immunisation, priced and turned down.** To offset the gap's rate exposure, not just its size, Laura would need
   $64-74k of a 30-year Treasury bought in January 2028 and sold in 2033: 43-50% of the deposit, which would then lose
   roughly an eighth of its value for every point yields rise. Redington's cure costs nine times the holding. Final Report only.
7. **The thin-coupon twin helps at the margin** (W-01, WInS listing UNVERIFIED): swapping the 2041-42 rungs cuts the
   shortfall's p95 from $25.1k to $22.1k and lets a $5k holding reach 0.17%. PARK for the Final Report.

**Verdict.** ADOPT D2 (before the floor, ~$7.5k, MODEL) as the challenger to C6, with C6's January 2033 set-aside kept
for the gap already showing: the two together are the cure. Kai's novelty point stands: this is L-02 come back, but
re-sized from a buffer for the whole gap ($15k for 1.3%) to a holding for the fifth still to come ($7.5k for 0.00%),
which only the blind-spot split made possible. "Birthday" is honest only as "the first day money exists": the cheques
were bought in January 2027 with nothing to spare. BIN the yearly check as a cure and immunisation for the IPS; PARK
the thin twin. Wording flag for the Writing Room: the case's "operating reserve" means the ten payments' money
(case :94-95), so never call this holding "the reserve" on its own.

**Self-check (not an independent audit).** D0 reproduces L-10's S0 and S1 exactly (0.0677, 0.0838). D2's 0.00% is
consistent: $7,500 x median bill growth 1.229 = $9,219 > the post-2033 gap's p99.9 $8,749. The fact-checker should
re-derive the 81% split and the D2 row from `results.json` before any line uses them.

**Plain-English lesson.** Some of a risk has already happened by the time you look, and some hasn't. Pay for the
first when you see it; buy the second on day one.
