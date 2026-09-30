# October trade: a rule written before anyone knows the answer

WS6, RAB Kit, 30 Sep 2026 (Sydney). AI-generated decision memo (Claude Code) for Team Caplet. **The team ratifies it
before the check date; nothing here is applied to the IPS or the Sheet.** Triage: it does not change the strategy.
Revised after the second judge panel (30 Sep): trigger D now fires only on a new fact (a price that was stale on Friday and passes later), not on IPS wording, and trigger B names its basis. Third panel (30 Sep): trigger B's size follows the team's floor definition (`--floor-rule`), and the refresh prints the day's break-even with the cost.

## Why a second trade, and why a rule

The Trading Notes guide asks how each decision "aligned with, tested, or refined" the strategy. Friday's trades carry
out the plan. A second trade can show the plan being **tested** against new prices, or **refined** by the team's own
research, but only if it has its own strategy reason. So the October trade is a rule, fixed now, with named triggers.
If no trigger fires there is no trade, and that is a valid result. We never add a trade to reach a count (PM-10).

## When (times from `trades_clock.py`)

| Step | U.S. Eastern | Sydney |
|---|---|---|
| Check uses this close | Wed 14 Oct 2026 4:00 PM EDT | Thu 15 Oct 2026 7:00 AM AEDT |
| Trade window opens (after the first hour) | Thu 15 Oct 2026 10:30 AM EDT | Fri 16 Oct 2026 1:30 AM AEDT |
| Trade window closes | Tue 20 Oct 2026 3:30 PM EDT | Wed 21 Oct 2026 6:30 AM AEDT |
| Trading Notes Analysis due | Fri 23 Oct 2026 5:00 PM EDT | Sat 24 Oct 2026 8:00 AM AEDT |

There is also an early-morning option. The last U.S. trading hours, 2:00-3:30 PM EDT, fall at 5:00-6:30 AM AEDT the
next day. The window is two weeks after Friday, which is long enough for prices to move, and it finishes before the
three notes are chosen. It also avoids Mon 12 Oct, a U.S. bond-market holiday (Columbus Day; how WInS treats bonds that
day is UNVERIFIED).

## The check (about 30 minutes; one runner and one checker)

1. Read in WInS: positions, cash and Order History (is anything from Friday unfilled?). Type today's bond prices into
   the price file, as on Friday.
2. Run `refresh_tickets.py --basis friday --wins-prices rab/trades/wins_prices_friday.csv --book <book>`. It prints
   the cost of the ten payments on 1 Jan 2027 on the latest curve and the plan split, and it yield-checks every bond.
3. Go through the triggers in order. The first one that fires is the October trade. Trigger A can come on top of
   another. Record the outcome in the decision log either way, with the date and the numbers the script printed.

## The triggers

| | Fires if | The trade | TN role | IPS sentence it carries out |
|---|---|---|---|---|
| **A. Repair** | A Friday ticket did not fill, was skipped because its price failed the check, or filled only in part | Place it at today's prices; the refresh re-sizes it | supported | "The January 2027 deposit buys the liability-hedging portfolio, latest payments first." |
| **B. Rates-fall test** | The refresh says the ten payments now cost **more than $300,000** on 1 Jan 2027, on the zero-coupon basis of `numbers.yaml` (its "ten payments cost" line; if WS1 locks a buyable-basis test before 14 Oct, use that one and say so in the decision log). Today (28 Sep curve) they cost about $292,000, so yields would have to fall more than about a quarter of a percentage point (about 26bp). | Sell VT down to the new stock-fund share the refresh prints (with `--floor-rule` set to the team's floor definition, `notes.md` s7); buy IBTM with the proceeds. Two trades, $50; only if the amount is at least $2,500 | tested | "A moderate fall in yields would leave some payments for the 2028 deposit to complete" |
| **D. Coupon refinement** | A new fact since Friday: the 1.375% 15 Nov 2040 bond was listed on Friday but its price failed the 25bp check (note T40s), or it was not listed then and is now; its price passes the check that day | Day 1: sell the 4.250% 15 Nov 2040 bond. Day 2 (once the cash shows): buy the 1.375% 15 Nov 2040 bond. Two trades, $20 | refined | "Laura's 2027 deposit buys Treasuries maturing before each of her ten $50,000 payments." (either bond fits it) |
| **C. Spare cash** | WInS cash is above **$6,300**: the $3,300 float (1.1%) plus at least $3,000, so the $25 commission is under 1% | Buy VT with everything above $3,300 | supported | "The rest, plus any 2027 remainder, forms the return-seeking portfolio" |
| **None** | Nothing fires | No trade. Write "checked 14 Oct: the rules said hold" in the decision log | - | - |

B comes before D and C because it is the market test the IPS itself describes. At most one of B, D and C runs.

### Why B buys IBTM

The 2027 deposit buys the latest payments first. If yields fall and the ladder costs more than the deposit, it is
the **earliest** payment (1 Jan 2033) that the 2028 deposit completes, before any stocks, so less is left for the
facility. Which part shrinks depends on the floor's definition, which the team settles (`notes.md` s7, judge panel
round 3): under the kit's model (`--floor-rule fixed`, WS4 `D_pre2027_rate_hedge.md`) the floor stays $150,000 and
the stock fund absorbs the gap (only a very large fall would reach the floor); read literally, the IPS ("repay the
whole remainder as Laura's facility floor", `--floor-rule remainder`) lowers the floor by the whole gap and the stock
fund by only about a fifth of it, so the VT sale is much smaller. Both the payment and the floor sit in IBTM. So
moving the excess from VT into IBTM does in WInS what the IPS says would happen to Laura's money. The dated holdings
already in WInS rise in value when yields fall, so only the stock-fund share needs moving.

### Why D is worth a trade (from `M9_selection.md`)

Of the 4.250% bond's cash before 1 Jan 2041, 38% comes as coupons that must be reinvested at unknown rates. For the
1.375% bond of the same date it is 17%. If coupons earn only 2%, the 1.375% bond delivers 93.9% of the value at
today's forward rates, against 87.9% (MODEL, per dollar). In Laura's plan, being sure of $50,000 on 1 Jan 2041 at 2%
takes about $25,000 of the 1.375% bond against about $26,000 of the 4.250%. At today's forward rates both cost about
$23,000. The trade changes nothing about the date, the kind of instrument or the strategy. It reduces the one risk a
fixed-income judge is most likely to raise.

- **Size.** Sell the whole holding: $17,000 face in the Portfolio book, or $26,000 in Book L. Buy the face value that
  `refresh_tickets.py --units rule --swap "T 4.250% 15-Nov-2040=T 1.375% 15-Nov-2040"` prints. At 28 Sep prices that
  is about $15,000 each way (MODEL illustration); the refresh on the day gives the real size.
- **Why two days.** Bonds fill at end-of-day prices, and it is UNVERIFIED whether a pending sale frees cash the same
  day. So sell first, then buy once the cash shows.
- **The same rule for the 2.000% 15 Nov 2041 bond**, in place of the 3.125%, if its Friday price was stale and now passes. The gain is
  smaller (coupons 33% down to 24%).
- **Do not do it** if either price fails the check, if the team is not sure, or if the 1.375% bond was listed and
  passing on Friday (then the Friday rule already swapped it: SW40). Waiting for IPS wording is not a reason: the
  IPS line "Treasuries maturing before each of her ten $50,000 payments" fits either bond. No trade is better
  than a trade the team cannot explain.

## What is likely (28 Sep numbers)

- **A** happens only if Friday leaves something undone.
- **B** needs a fall of about 26bp in about two weeks. In 2026 the 10-year par yield's daily changes had a standard
  deviation of about 4.5bp. That is our calculation from `rab/data/treasury_par_2000_2026/2026.csv` (185 sessions),
  so this fall would be roughly a two-standard-deviation move: possible, not likely. WS4 owns the reconciled odds.
- **C** does not fire at the cash Friday's tickets leave (about $5,000, `tickets.md`), unless fills or prices leave
  more.
- **D** fires only if the 1.375% bond's Friday price was stale (or it was not listed) and it passes later. If it was
  listed and passing on Friday, the Friday swap rule already bought it. So the most likely outcome is no trade, and
  the three notes come from the first eleven trades (ten on Friday, VT on Mon 5 Oct ET). The 14 Oct check itself is
  then reported in the IBTR reflection ("checked 14 Oct: the rule said hold").

## What we will not do

- Trade because prices moved a little, or buy VT back to 8.7% after a stock move. The branch is held to 2033.
- Sell a dated holding to chase a better yield. Trigger D keeps the same payment date; it is not a yield trade.
- Sell anything on the day it was bought.
- Place "tidy-up" trades after the IPS wording is final. insight_v1 suggested Tue 3 Nov as the cut-off; trading
  itself ends Fri 6 Nov 4:00 PM EST (Sat 7 Nov 8:00 AM AEDT).

## For the Trading Notes Analysis

If D runs, its buy leg is the natural **refined** pick: new research changed an implementation choice, for a reason
the team can state in one line. B would be the natural **tested** pick (feature the VT sale, OB_S, in place of IBTR). A and C are **supported**. As with every pick,
use only filled trades with notes saved in WInS, and keep two alternates.
