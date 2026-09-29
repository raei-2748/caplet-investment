# M5 model card: century backtest and the price of certainty

WS3, 2026-09-30. AI-generated research (Claude Code) for Team Caplet. Every number is MODEL (history replayed through
the adopted rules), not a forecast. Spec `M5_SPEC.md`; code `m5_backtest.py` (deterministic, 3 s); outputs `rab/results/M5/`.

**What it does.** (A) Prices Laura's ten $50,000 payments exactly like the Gate A headline (`laura.ladder.cost_today_strips`,
$289,119) on every Treasury curve back to 1871. (B) Replays Root-and-Branch from 149 start years (1872-2020): that era's
yields buy the ladder and the floor, that era's stock returns drive the branch, and the 2031 range and 2033 gift follow
the adopted rules. A second view keeps today's yields and replays only history's returns.

**Data.** Treasury par curves 1990-2026 and FRED DGS 1962-1989 (daily); Shiller long rate 1871-1961 (monthly);
Damodaran, JST and Ken French returns; Shiller CPI. `rab/data/history/MANIFEST.md`.

## Results

| | Value | Basis |
|---|---|---|
| Ten payments on 28 Sep 2026 | $289,119 (reproduces numbers.yaml to the cent; 2020 median $458,828; high $470,249 on 4 Aug 2020; cheapest since 28 May 2002) | M1 G re-built independently |
| Months since 1871 as cheap as today | 23% (23.5-23.8% after removing the flat-curve bias); since 1962: 51% | month starts |
| Cheapest ever | about $110,000 on 30 Sep 1981 | daily since 1962 |
| History's yields and returns: payments paid in full | 149 of 149 start years; dearest ladder $411k (2013 start) against $450k of deposits | start of each year |
| ... but the 2028 deposit had to finish the ladder | 112 of 149; bottom below $150k in 91 | yields lower than today's in most eras |
| ... gift | median $132k, p10 $67k, worst $29k (2020 start) | VT-like world fund |
| Today's yields, history's returns: gift | worst $159k (fund bought 1929), p10 $169k, median $176k; bottom $150k always; top reached in 85% | the question Laura faces |
| insight_v1 H9 on the 28 Sep basis | total worst $172k raw / $169k rescaled (1928), p10 $185k, median $214k | H9 was $171k / $169k / $185k / $214k: unchanged |

Eras (history's yields): median ladder cost $346k (1872-1913), $356k (1914-45), $328k (1946-81), $301k (1982-2020);
median gift $122k, $111k, $150k, $168k. Figures: `fig_cost_of_certainty.png`, `fig_m5_gift_by_start_year.png`,
`fig_m5_ladder_cost_by_start_year.png`.

## What this teaches (plain English)

Certainty is bought with Treasuries, so its price depends on the interest rate on the day the money arrives. Today's
rates are high by the standard of the last 150 years: only about one month in four since 1871 would have bought the
ten payments as cheaply. That is why Root-and-Branch can both buy the payments outright and promise a $150,000 bottom with a
stock fund on top. At the lower rates of most past eras the same promises would still have been kept, but they would
have left about $130,000 for the facility instead of about $175,000.

## Assumptions and limits

Before 1962 the curve is flat at the long rate (overstates cost by a median 0.8%). The world fund keeps today's 62% U.S.
weight in every year (it beat real VT by about 1 point a year in 2009-2025). Pre-1928 U.S. returns are JST's. Annual
steps (1 January); no fees, taxes or commissions; STRIPS-like rungs (no coupon reinvestment: M1 E covers the WInS book).
Deposits and payments keep today's dollar amounts in every era. Start years only: M1 G found 197 individual days in
2020-21 when a payment could have been left short (none on a 1 January).

**Failure modes.** A curve file with missing long tenors (handled: flat extrapolation, checked); reading a history
number as a forecast; quoting the history-yield gift ($132k) as if it applied now (the ladder price for 2027 is already
known to within about 26bp).

## Triage (contradiction rule; nothing applied to the IPS)

| Finding | Class |
|---|---|
| IPS "about $460,000 at 2020 yields", "cheapest since 2002", "every Treasury curve since 2000": rebuilt with independent code, identical | ignore (supports the IPS) |
| The $150,000 bottom is certain only once the floor is bought (Jan 2028); in 91 of 149 historical start years it came out lower. If the IPS states the bottom without that condition, add it ("certain by construction if the 2028 deposit arrives and yields have not fallen more than about 1 point first", M7 threshold 109bp) | fix-before-6-Nov (wording only, if absent) |
| "Only about one month in four since 1871 was as cheap" is a stronger, checked line than "cheapest since 2002" | note-in-Final-Report (optional) |
