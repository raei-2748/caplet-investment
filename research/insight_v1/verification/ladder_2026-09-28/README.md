# Ladder cost check on the 28 Sep 2026 curve

Two AI tools priced the same ten-rung Treasury ladder ($50,000 maturing each 15 November, 2032-2041) on the
Treasury Daily Par Yield Curve for 28 Sep 2026. Both are MODEL prices, not STRIPS quotes. AI-generated research;
no deliverable text. Logged in `docs/AI_USE.md` section 5.

| Source | Today | Forward to 1 Jan 2027 | Fall in yields before it passes $300k |
|---|---|---|---|
| D1 method (`D1_purchase_rule.py`, Claude Code) | $289,119 | $292,418 | 26bp |
| Independent check (`gpt/`, ChatGPT GPT-6 Astra, high effort) | $289,003 | $292,214 | 26.9bp |
| GPT, alternative interpolation (only the published maturities) | - | $290,965 | 31.2bp |

The $204 gap between the first two rows comes from two conventions, not an error. `reconcile.py` changes them one at a
time in the D1 method and reproduces the GPT figures to the cent:

| D1 method with | Today | Forward |
|---|---|---|
| days/365.25, no 1-3 month nodes (as D1) | $289,119.20 | $292,418.11 |
| days/365 | $289,003.45 | $292,303.31 |
| days/365 and 1-3 month yields as discount-factor nodes (as GPT) | $289,003.45 | $292,214.16 |

Quote it as "about $290-292k, about 27bp of headroom", not to the dollar. On 25 Sep the D1 figure was $294,387 (19bp).

## Files

- `treasury_par_2026_to_09-28.csv`: Treasury Daily Par Yield Curve, all 2026 dates to 28 Sep, downloaded from
  home.treasury.gov on 29 Sep 2026. The 28 Sep row is the input to both calculations.
- `D1_rerun_output_2026-09-28.txt`: full output of `research/insight_v1/scripts/D1_purchase_rule.py` on that file
  (rate-fall table, break-evens, the 24.2% model chance of a gap by January, joint tail).
- `reconcile.py`: the convention-by-convention reconciliation above.
- `gpt/price_ladder.py`, `gpt/check_sensitivity.py`, `gpt/rung_prices.csv`: ChatGPT's code and rung prices, copied
  unchanged from its project folder on 29 Sep 2026. Standard library only. Run from inside `gpt/`.

## The brief ChatGPT was given

It did not see our answer, the repo or the WInS account.

> Independent check, please work from scratch and show your code. Task: price a US Treasury zero-coupon ladder as of
> 1 January 2027, using the US Treasury Daily Par Yield Curve for 28 September 2026: 1M 4.04, 2M 4.20, 3M 4.28,
> 6M 4.41, 1Y 4.59, 2Y 4.92, 3Y 5.01, 5Y 5.06, 7Y 5.15, 10Y 5.24, 20Y 5.60, 30Y 5.56 (percent, semiannual
> bond-equivalent). Ladder: ten zero-coupon Treasuries, each paying $50,000, maturing 15 November of each year 2032
> through 2041. (1) Bootstrap a zero curve from the par yields and state your interpolation choice. (2) Give the cost
> of the ladder bought today (28 Sep 2026) and its forward cost on 1 January 2027. (3) How many basis points of a
> parallel fall in yields would make the 1 January 2027 forward cost exceed $300,000? (4) List each rung's cost and
> say which assumptions drive the result most.

## How to run (from the repo root)

    .venv/bin/python research/insight_v1/verification/ladder_2026-09-28/reconcile.py
    cd research/insight_v1/verification/ladder_2026-09-28/gpt && python3 price_ladder.py && python3 check_sensitivity.py
