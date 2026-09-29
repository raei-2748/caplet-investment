# M8 model card: what moves the 2031 range

WS2, 30 Sep 2026 (Sydney). Code `rab/models/m8_sensitivity.py`; spec `M8_SPEC.md`; results `rab/results/M8/`.
AI-generated research (Claude Code). All figures are Laura's plan, MODEL, 28 Sep 2026 curve, share = half.

**What it does.** It rebuilds the whole chain from the 1 Jan 2027 ladder purchase to the 2031 range, using WS1's Gate A
pricer (the D1 curve method). It then moves one assumption at a time (tornado) and all of them together (Sobol,
SALib). Market luck is kept separate from assumptions. Base check: ladder $292,418 on 1 Jan 2027 and stock fund
$40,736, both exactly as in `rab/numbers.yaml`.

**Tornado** (median 2031 top; base $175k, bottom $150k):

| Assumption (low / high) | Median top | 1-in-20 top |
|---|---|---|
| Yield move before the 1 Jan 2027 purchase (-93 / +92 bp, historical 95-day moves since 1990) | $143k to $194k | $138k to $178k |
| 5-year yield move during 2027, the floor's price (-1.95 / +2.27 points, historical 1-year moves) | $168k to $182k | $162k to $171k |
| Yearly costs paid from the stock fund (0 / 1% of all assets) | $175k to $167k | $166k to $160k |
| Stock fund's expected return (4.08% / 8.00%) | $173k to $176k | $165k to $167k |
| Volatility (0.12 / 0.20), fat tails (normal / nu = 3), floor reinvestment | under $10 | up to $4k |
| For scale, not assumptions: share 1/3 vs 2/3 / choice of return model (M3) | $167k to $183k / $0.5k | $161k to $171k / $1k |

A fall in yields before January 2027 is the only input that also moves the **bottom**. If the ladder then costs more
than $300,000, the 2028 deposit first completes it, and under the IPS wording ("the whole remainder") the floor
shrinks: to $129k at the -93bp end.

**Sobol, assumptions only** (total-order index ST for the median 2031 top): January-2027 yields 0.90, January-2028
5-year yield 0.07, costs 0.03, expected return 0.003, volatility and tails 0.000. The 1-in-20 top ranks them the same
way. With market luck included, luck in 2028-2030 explains only about 0.22 of the variance of the 2031 top, against
0.73 for January-2027 yields (`sobol_A_top2031.csv`).

**The three assumptions the IPS must state** (pre-registered rule: largest ST; tornado and 1-in-20 ranking agree):
1. **Treasury yields when the first deposit buys the ten payments (1 Jan 2027).** They decide what is left over, or
   how much of the 2028 deposit must complete the ladder. That in turn sets the floor and the size of the stock fund.
2. **The 5-year Treasury yield when the floor is bought (Jan 2028).** Higher yields make the floor cheaper and the
   stock fund bigger.
3. **Costs, and who pays them.** The IPS text read on 30 Sep does not yet say who pays costs (WS2 D_ips_three_assumptions: fix-before-6-Nov); the model charges them to the stock fund. A 1% yearly fee on all assets
   would cut the typical top by about $8k and the typical gift by about $11k.

The stock-return assumption is not on the list. Across the published range (4.1% to 8%) it moves the typical top by
under $3k. It matters for how often the top is reached (M3), not for the range itself.

**Floor wording (inventory flag F4)** (`floor_reading.csv`). If yields fall 50bp first, the IPS reading gives a floor
of $142,612 plus a fund of $28,501. The insight_v1 E6 reading (keep $150,000 of floor; the fund pays the top-up) gives
$150,000 plus $22,590. At -100bp the two readings give $126,560 + $22,836 against $150,000 + $3,626. They agree when
there is no gap.

**Limits and failure modes.** Inputs are independent (in reality, yields in 2026 and 2027 are linked, and stocks and
yields can move together). Uniform ranges for the return, volatility and fee inputs are judgements. The rate inputs use
the empirical 1990-2026 distribution. The top-up is grown along the shifted curve for one year. Tails are interpolated
on a 121-point grid in Sobol B. Sobol indices describe these ranges, not the true odds.

**What this teaches (plain English).** The 2031 range depends much more on interest rates on two dates, and on fees,
than on how stocks do. Because the stock fund is small, a stock-market forecast barely changes what Laura can
announce. The IPS should name those two rate dates and the cost rule, and say that the floor is whatever the 2028
deposit can buy once all ten payments are covered.
