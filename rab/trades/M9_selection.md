# M9 security selection: which WInS security fills each slot

WS6, RAB Kit, 30 Sep 2026 (Sydney). AI-generated research (Claude Code) for Team Caplet; not deliverable text.
Basis: the Gate A lock (`rab/numbers.yaml`, sha256 492ed320...): 28 Sep 2026 Treasury par curve, 28 Sep closes, WInS
bond prices the team recorded on 29 Sep. Screen: `rab/trades/m9_screen.py` (reuses `rab/models/m1_ladder.py`), output
`rab/trades/out/m9_screen_2026-09-28.csv` / `.json`. All model figures are MODEL. The strategy is not reopened.

**Bottom line.** Every holding in the `Portfolio` tab is the best choice among securities the team has **seen** in
WInS, and every order is far inside the volume rules, so no order needs splitting. There is one upgrade worth a team
decision. If the WInS bond list includes the **low-coupon bonds** maturing 15 Nov 2040 (1.375%) and 15 Nov 2041
(2.000%), they fund the 2041 and 2042 payments with much less money arriving early as coupons, at the same cost on
today's curve.

## How a slot is judged

1. **Maturity:** the holding must end *before* the 1 Jan payment. Ending early is safe, because the money just waits.
   Ending after the payment is not, because the price on the day is unknown.
2. **Price against the curve:** the WInS price's yield must be within 25bp of the official par curve, or the price is
   stale (M1_METHOD.md section C).
3. **Coupons to reinvest:** the share of a holding's cash that arrives before the payment date as coupons, and what it
   delivers if those coupons earn only 2%, shown as a share of the "today's forward rates" case (M1_METHOD.md
   section E). Higher is better. This is the premortem's PM-23 risk, measured per security.
4. **Cost:** commission ($25 per ETF trade, $10 per bond trade), fund fee, bid/ask spread.
5. **Liquidity:** the order against 2 x the 30-session average daily volume (the official rule), 10% of the
   20-session median day (the kit rule) and half of the lowest day in 20 sessions (the WInS FAQ rule, worst day).
6. **WInS listing and exact name:** SEEN means the team saw it in WInS on 29 Sep. Anything else is UNVERIFIED.

## Chosen and runner-up, per slot

| Slot (Laura's plan) | Chosen: exact name [WInS status] | Runner-up | One-line reason |
|---|---|---|---|
| 1 Jan 2033 payment | **IBTM** iShares iBonds Dec 2032 Term Treasury ETF [SEEN 29 Sep] | None dated in WInS. If IBTM fails, keep the cash and retry. | It ends about 15 Dec 2032, two weeks before the payment. No WInS Treasury matures between Feb 2031 and Feb 2036 (SEEN). Its yield is within 2bp of the curve. |
| Facility floor (repays the 2028 remainder by late 2032) | **IBTM**, the same holding (the floor is 24.3 of its 32.5 points) | IBTL iShares iBonds Dec 2031 Term Treasury ETF [UNVERIFIED in WInS], else the 5.375% bond of 15 Feb 2031 [UNVERIFIED] | The IPS says "Treasuries maturing in late 2032". Both runners-up end a year or more early, so the floor money would sit idle. |
| 1 Jan 2034 payment | **IBTO** iShares iBonds Dec 2033 Term Treasury ETF [UNVERIFIED name] | IBTM (ends 12.6 months early) | It ends two weeks before the payment and there is no WInS Treasury in that window. **Trap: IBTN in WInS is INSCORP Inc.** |
| 1 Jan 2035 payment | **IBTP** iShares iBonds Dec 2034 Term Treasury ETF [UNVERIFIED name] | IBTO (ends a year early) | Same logic. At 2%, it delivers 94.9% against 92.4% for the runner-up. |
| 1 Jan 2036 payment | **IBTQ** iShares iBonds Dec 2035 Term Treasury ETF [UNVERIFIED name] | IBTP (ends a year early) | Same logic. At 2%, it delivers 93.9% against 91.7%. |
| 1 Jan 2037 payment | **IBTR** iShares iBonds Dec 2036 Term Treasury ETF [UNVERIFIED name] | IBTQ, or the 4.5% bond of 15 Feb 2036 only if its WInS price passes the check (it was 111bp off on 29 Sep) | The only holding that ends in late 2036. It is thin ($37.6m in assets, iShares, 28 Sep), but our order is 2.5% of a median day. |
| 1 Jan 2038 payment | **T 4.750% 15-Feb-2037** (CUSIP 912810PT9) [price SEEN; WInS string UNVERIFIED] | T 5.000% 15-May-2037 (912810PU6), if listed | Its price passes (-15bp). The May-2037 bond ends 3 months later but has a higher coupon, so it comes out the same at 2% (90.5% each). |
| 1 Jan 2039 payment | **T 4.500% 15-May-2038** (912810PX0) [price SEEN] | T 4.375% 15-Feb-2038 only if Friday's price passes (92bp off on 29 Sep), else T 5.000% 15-May-2037 | It is the last bond maturing before the payment, and its price passes (-14bp). **The Sheet's accrued interest for it (0.530) is a typo**: about 1.7 is right. |
| 1 Jan 2040 payment | **T 4.375% 15-Nov-2039** (912810QD3) [price SEEN] | T 4.500% 15-Aug-2039 (912810QC5), if listed | It ends 7 weeks before the payment and its price passes (-7bp). The runner-up is about equal (89.0% against 89.3% at 2%). |
| 1 Jan 2041 payment | **T 4.250% 15-Nov-2040** (912810QL5) [price SEEN] | **T 1.375% 15-Nov-2040 (912810ST6), better if listed** | Same date, but only 17% of its cash comes as coupons, against 38%. At 2%, it delivers 93.9% against 87.9%. See the decision below. |
| 1 Jan 2042 payment | **T 3.125% 15-Nov-2041** (912810QT8) [price SEEN] | **T 2.000% 15-Nov-2041 (912810TC2), better if listed** | Same date. Coupons are 24% of its cash against 33%. At 2%, it delivers 91.0% against 88.3%. |
| Branch (world stock fund) | **VT** Vanguard Total World Stock ETF [SEEN 29 Sep] | VTI + VXUS in VT's own mix (about 62/38 U.S./non-U.S.) [both SEEN] | One trade holds about 10,000 stocks at a 0.06% fee: the IPS's "global index fund of thousands of companies". The pair saves about 0.02% a year but costs a second trade and a weight to keep. ACWI costs 0.32%, holds about 2,200 stocks and is UNVERIFIED in WInS. |
| Cash float | **Cash** (about 1.7% after Friday) | SGOV iShares 0-3 Month Treasury Bond ETF [SEEN 29 Sep] | WInS cash earns 0%, but one $25 commission is repaid only above about $6,500 held for the 35 days to 6 Nov (1-month yield 4.04%). The float is smaller than that, and whether WInS credits fund distributions is UNVERIFIED. |

The 2% column compares money delivered on the payment date if coupons earn only 2% with the case at today's forward
rates. It is scale-free: per dollar invested, MODEL, from `m9_screen.py`. The ten chosen rungs reproduce
`numbers.yaml` `reinvest.rung.*` exactly (30 of 30 ratios; the script asserts it).

## Evidence behind the table

**Reinvestment exposure by slot** (MODEL, per dollar invested, delivered on 1 Jan as a share of the curve case).

| Holding | Ends (months early) | Yield vs curve | Share of cash as coupons | Coupons at 0% | Coupons at 2% |
|---|---|---|---|---|---|
| IBTM | 15 Dec 2032 (0.6) | +1.6bp | 17% | 94.8% | 96.7% |
| IBTO | 15 Dec 2033 (0.6) | +0.4bp | 22% | 93.2% | 95.6% |
| IBTP | 15 Dec 2034 (0.6) | +1.7bp | 25% | 92.2% | 94.9% |
| IBTQ | 15 Dec 2035 (0.6) | +1.7bp | 28% | 90.7% | 93.9% |
| IBTR | 15 Dec 2036 (0.6) | +0.3bp | 30% | 88.5% | 92.3% |
| T 4.750% 15-Feb-2037 | (10.5) | -15.3bp | 33% | 85.8% | 90.5% |
| T 4.500% 15-May-2038 | (7.6) | -14.4bp | 35% | 84.8% | 89.6% |
| T 4.375% 15-Nov-2039 | (1.5) | -6.6bp | 37% | 84.7% | 89.3% |
| T 4.250% 15-Nov-2040 | (1.5) | -5.1bp | 38% | 82.9% | 87.9% |
| T 1.375% 15-Nov-2040 (alternate) | (1.5) | model price | 17% | 91.4% | 93.9% |
| T 3.125% 15-Nov-2041 | (1.5) | -1.9bp | 33% | 83.5% | 88.3% |
| T 2.000% 15-Nov-2041 (alternate) | (1.5) | model price | 24% | 87.3% | 91.0% |

For iBonds the yield shown is iShares' average yield to maturity against the par curve at the fund's average
maturity (`numbers.yaml` `wins.ibond_checks`). For bonds it is the WInS price against the curve model
(`wins.bond_check.*`). A negative gap means the WInS price is a little rich.

**Liquidity** (Nasdaq consolidated volume, complete sessions to 28 Sep; `numbers.yaml` `market.etf_2026-09-28`).
Every Portfolio-tab order is at most 1.2% of the official limit (2 x the 30-session average) and at most 2.8% of a
median day (IBTM). The worst single case is IBTR's 846 shares, 11% of its thinnest day in 20 sessions, which is still
inside the FAQ's half-of-volume rule. Book L's larger orders peak at 3.7% of a median day (IBTR, 1,252 shares).
**No split is needed.** The live risk is timing. At 9:30am ET almost no iBond volume has traded yet, and WInS lets an
order take only half of the volume traded so far. So place iBond orders after the first hour. If WInS shows an order
as waiting, leave it alone: never re-enter it. If it is still waiting at 3:30pm ET, cancel it and split it over the
next two sessions (half each day).

**Names.** SEEN in WInS on 29 Sep: IBTM, VT, VTI, VXUS and SGOV (tab `WInS Notes`), and prices for all seven bonds
above (tab `Book L`, premortem PM-04). The names for IBTO-IBTR are the issuer's own (iShares product pages, 28 Sep).
Their WInS strings are UNVERIFIED, and outside data cannot confirm them: Longbridge has no IBTN record. The WInS
string for every bond is UNVERIFIED. Find each bond by coupon and maturity, never by a made-up symbol.

**Why the low-coupon bonds may be listed.** The Treasury's own list of bonds (MSPD Table V, 31 Aug 2026,
`rab/trades/data/`) has no bond maturing between 15 Feb 2031 and 15 Feb 2036. That is exactly the gap the team saw in
the WInS drop-down. So WInS probably lists that class of bond, and the 1.375% Nov-2040 and 2.000% Nov-2041 belong to
it. This is an inference: check the drop-down on Friday.

## The one decision (triage: decide at the 1 Oct vote; otherwise note-in-Final-Report)

**Low-coupon bonds for the 2041 and 2042 payments.** A bond with a small coupon pays most of its value at maturity,
so less has to be reinvested at rates nobody knows. That is the risk the IPS line "needs no rebalancing" leaves out
(PM-23). Take the 2041 payment in Laura's plan. To be sure of $50,000 on 1 Jan 2041 even if coupons earn only 2%:

- the 4.250% Nov-2040 bond needs about **$26,000** today;
- the 1.375% Nov-2040 bond needs about **$25,000**.

At today's forward rates both need about $23,000 (MODEL: $26,456 / $24,641 / $23,266 / $23,146 in
`m9_screen_2026-09-28.json`; the 1.375% is at the curve model price because no WInS price has been seen).

- **If WInS lists them on Friday and their prices pass the 25bp check,** the team can use them in place of the
  4.250% and 3.125% bonds. Run `refresh_tickets.py --basis friday --swap "T 4.250% 15-Nov-2040=T 1.375% 15-Nov-2040"`
  (and the same for Nov-2041). It re-sizes the ticket and checks the price.
- **Or keep Friday as planned, and make the swap the October refinement** (`october_trade.md`, trigger D), after the
  team has worked through the coupon issue and fixed the IPS wording.
- **If WInS does not list them,** nothing changes in WInS. The Final Report can still say that in Laura's real plan,
  low-coupon bonds (or STRIPS, if the looser reading of "for BOTH contributions" holds) cut the coupon risk.

This is security selection inside the adopted strategy: the same payment dates and the same kind of instrument.
It does not change the strategy.

## Other triage

| Finding | Class | Evidence |
|---|---|---|
| IBTM carries two jobs (the 2033 payment and the floor); iBonds "do not seek to return any predetermined amount" | note-in-Final-Report; notes never say IBTM "repays" a sum | iShares (insight_v1 `open_questions.md` s3); `assumptions.md` C5 |
| T 4.500% May-2038 accrued typo in the Sheet (0.530, about 1.7 is right) | fix-before-6-Nov (Sheet input); tickets already use the right figure | `numbers.yaml` `wins.bond_accrued_mismatch` |
| Two stale WInS bond prices (4.5% Feb-2036, 4.375% Feb-2038) | ignore for Friday (not in the book); re-check only if needed as alternates | `wins.bond_check.*` (-111bp, -92bp) |
| The 2038 and 2039 bonds end 10.5 and 7.6 months early (no later bond exists in that class) | note-in-Final-Report (money waits in bills in Laura's plan; 0% in WInS) | MSPD Table V; `assumptions.md` C6 |
| VT against VTI + VXUS / ACWI | ignore (VT stays); WS3 owns the return comparison | fees and stock counts: insight_v1 `wins_now/S2_growth_sleeve.md` (Vanguard and iShares pages, 30 Jun / 24 Sep 2026) |

## Limits

These are MODEL prices from one curve on one day. Coupons are reinvested at a flat rate. iBonds are valued by
looking through to their holdings on 24 Sep (IBTM and IBTR are scaled to their 28 Sep NAV because the dates do not
line up). WInS names, the bond unit and the accrued-interest convention are UNVERIFIED. The volume figures are real
market volume, not whatever WInS measures ("market volume" is undefined in the FAQ).
