# Final-Report research: the January 2027 STRIPS ladder and the reserve run-down

Agent S3, insight_v1 run, 2026-09-27. **PROVISIONAL.** The team has not approved the strategy, and Phases B-E may
change it. This is AI-generated research (tables, numbers, caveats), not text to submit. The team decides and writes
every word.

**Why this file exists.** These two tables were sections E.2 and E.5 of `securities_and_allocation_v0.md`. The S4 red
team (finding 6) said they are Final-Report material (due Dec 4), not week-1 trading material. The Trading Notes guide
says teams are "not expected to calculate the final size of the operating reserve" at the Trading Notes stage
(`competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` line 20, VERIFIED-REPO-FILE). Nothing here
belongs in a WInS note.

None of these instruments is traded in WInS. They are Laura's real (non-WInS) portfolio. If the team ever uses one in
WInS, it is **PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading** (this season:
WInS availability + Session Rules position limit).

Numbers come from `research/insight_v1/wins_now/S1_hedge_weights.py` (ladder), `research/insight_v1/scripts/S3_allocation_numbers.py`
section 6 (run-down) and `research/insight_v1/scripts/S4_red_team_checks.py` section 5 (rate-fall costs). Run each from
the repo root with `.venv/bin/python <path>`.

## Terms
- **STRIPS**: zero-coupon Treasuries. Each pays one amount on one date and nothing before.
- **Rung**: one STRIPS in the ladder; it pays one of Laura's ten $50,000 payments.
- **Principal / interest STRIP**: a STRIP cut from a bond's final repayment, or from one of its coupons.
- **Forward value**: what something is worth on a future date if today's curve predicts future rates correctly
  (ASSUMPTION wherever used).

## 1. The January 2027 ladder, rung by rung (was E.2)
Source: S1, from Treasury MSPD Table V (record date 2026-08-31, api.fiscaldata.treasury.gov, VERIFIED-PRIMARY per S1,
accessed 2026-09-27). Costs are valued at 2027-01-01 on the 2026-09-25 official curve (model output; ASSUMPTION: STRIPS
price on the par-derived zero curve; real quotes differ by a few bp). STRIPS are bought "only through a financial
institution, a broker, or dealer" in $100 multiples (treasurydirect.gov, VERIFIED-PRIMARY per S1).

| Pays the payment on | Rung matures | Instrument | Cost at 2027-01-01 | Alternate |
|---|---|---|---|---|
| Jan 1 2033 | Nov 15 2032 | Principal STRIP 912821KC8 | $37,253 | IBTM (iBonds Dec 2032) ~$37,218 |
| Jan 1 2034 | Nov 15 2033 | Principal STRIP 912821NP6 | $35,336 | IBTO ~$35,346 |
| Jan 1 2035 | Nov 15 2034 | Principal STRIP 912821QX6 | $33,495 | IBTP ~$33,550 |
| Jan 1 2036 | Nov 15 2035 | Principal STRIP 912821TF2 | $31,720 | IBTQ ~$31,826 |
| Jan 1 2037 | Nov 15 2036 | Interest STRIP due 11/15/2036 (CUSIP not in Table V: broker quote) | $30,007 | IBTR ~$30,227 ($34m fund); May 15 2036 principal 912821UK9 $30,861 |
| Jan 1 2038 | Nov 15 2037 | Interest STRIP due 11/15/2037 | $28,362 | May 15 2037 principal 912803DA8 $29,183 |
| Jan 1 2039 | Nov 15 2038 | Interest STRIP due 11/15/2038 | $26,779 | May 15 2038 principal 912803DD2 $27,569 |
| Jan 1 2040 | Nov 15 2039 | Principal STRIP 912803DJ9 | $25,257 | Aug 15 2039 912803DH3 $25,635 |
| Jan 1 2041 | Nov 15 2040 | Principal STRIP 912803DP5 | $23,791 | 912803FU2 (same date) |
| Jan 1 2042 | Nov 15 2041 | Principal STRIP 912803DU4 | $22,387 | 912803GD9 (same date) |
| **Total** | | | **$294,387** | Exact-date value $292,264; headroom under $300k ~$5.6k (~19bp) |

**Caveat (S4 finding 9, script section 5; ASSUMPTION: zero-drift lognormal cost, 7.24% a year volatility, the brief's
section 14 method):**
- The real Nov-15 ladder costs more than $300,000 on 2027-01-01 in about **3 of 10** rate paths (30.7%), against 24.3%
  for exact-date zeros.
- Cost if rates fall before the purchase: -25bp $301,676; -50bp $309,169; -100bp $324,793.
- In those paths the rule "buy the longest rungs first and the rest from the 2028 deposit" means certainty for the
  **first** rungs depends on the 2028 deposit arriving. With a missing or late deposit, that is the brief's unanswered
  "joint tail" (section 9). Passed to Phases B-E.
- STRIPS dealer mark-ups are unknown (UNVERIFIED) and would add to the cost.

## 2. The operating reserve after 2033, as payments are made (was E.5)
Values on today's forward curve (ASSUMPTIONS: forwards are realised; rungs treated as exact-date zeros). The Nov-15
rungs pay about 47 days early and each earns about $258 of T-bill interest while it waits (ASSUMPTION: 4% bill rate).

| Jan 1 | Payments left (face) | Holdings just before the payment | Market value | Value of STRIPS still held after paying |
|---|---|---|---|---|
| 2033 | 10 ($500k) | $50k T-bills + 9 STRIPS | $394,930 | $344,930 |
| 2034 | 9 ($450k) | $50k T-bills + 8 STRIPS | $363,676 | $313,676 |
| 2035 | 8 ($400k) | $50k T-bills + 7 STRIPS | $330,957 | $280,957 |
| 2036 | 7 ($350k) | $50k T-bills + 6 STRIPS | $296,706 | $246,706 |
| 2037 | 6 ($300k) | $50k T-bills + 5 STRIPS | $260,825 | $210,825 |
| 2038 | 5 ($250k) | $50k T-bills + 4 STRIPS | $223,086 | $173,086 |
| 2039 | 4 ($200k) | $50k T-bills + 3 STRIPS | $183,342 | $133,342 |
| 2040 | 3 ($150k) | $50k T-bills + 2 STRIPS | $141,396 | $91,396 |
| 2041 | 2 ($100k) | $50k T-bills + 1 STRIP | $97,042 | $47,042 |
| 2042 | 1 ($50k) | $50k T-bills | $50,000 | $0 |

How the composition changes (answers the case's "how composition changes as payments approach"):
- Treasuries only, getting shorter and more cash-like every year.
- Nothing is sold before maturity, so rate moves change the market value but never the payment.
- The small interest earned while each rung waits goes to project flexibility.
- Brief section 8 item 9: report the reserve at its 2033-01-01 market value ($394.9k) and reconcile "funded 2027, set
  aside 2033" in one sentence.

**Final Report chart idea:** a stacked bar per year 2033-2042 (T-bills waiting vs STRIPS still held), from the table
above. The IPS bans charts; the Final Report does not.

## Sources
- `research/insight_v1/wins_now/S1_treasury_sleeve.md` and `S1_mspd_table5_2026-08-31_fixed_2032plus.csv` (MSPD
  Table V, api.fiscaldata.treasury.gov, accessed 2026-09-27 by S1).
- `competition/official_market_data/daily-treasury-rates_2026-09.csv` row 09/25/2026 (VERIFIED-REPO-FILE).
- `research/insight_v1/wins_now/S4_red_team.md` finding 9; `research/insight_v1/scripts/S4_red_team_checks.py`.

## What this teaches
A plan that is "certain" at today's prices can still depend on something uncertain before it is bought. The ladder
fits inside $300,000 today, but only just, and in about three rate paths out of ten it will not. Saying exactly which
payments then lean on the 2028 deposit is more honest, and more useful to Laura, than a single "fully funded" label.
