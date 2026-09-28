# S1: Treasury and cash sleeve (WInS hedge, cash proxy, Laura's real ladder)

Agent S1, insight_v1 run, 2026-09-27. **PROVISIONAL week-1 research.** The team has not approved the strategy, and
Phases B-E may change it. These are research notes and numbers. They are not text to submit. Every WInS ticker below is
**PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading.**
Script: `research/insight_v1/wins_now/S1_hedge_weights.py`. Run it from the repo root with
`.venv/bin/python research/insight_v1/wins_now/S1_hedge_weights.py`. It reproduces the $292,264 liability value, the 9.90y
duration and the $289/bp DV01.
Data snapshots used by the script, all VERIFIED-PRIMARY and downloaded 2026-09-27:
- `S1_fund_holdings_snapshot.csv`: every bond held by 15 funds.
- `S1_mspd_table5_2026-08-31_fixed_2032plus.csv`: Treasury's table of strippable securities.

## Summary (short version)
1. **The better WInS hedge is IEF + TLH, not IEF + TLT.** Weights from today's issuer durations: IEF 35.7% / TLH 64.3%.
   IEF holds notes maturing May 2033 to Aug 2036. TLH holds bonds maturing Feb 2037 to Aug 2046. Together their bonds sit
   closer to Laura's ten payment dates (2033-2042) than IEF + TLT's do; 74.7% of TLH's bond weight matures after the
   last payment, so this is a closer fit, not a year-by-year match [corrected by S3 after the S4 red team, 2026-09-27]. IEF + TLT is a "barbell": 7-10y notes plus 20-30y
   bonds, with nothing in between. Under a 50bp twist of the curve, IEF+TLT misses the liability by up to **$3,619**.
   IEF+TLH misses by up to **$1,352**. Both mixes stay within about $1.3k of the liability under ±100bp parallel moves
   (VERIFIED-PRIMARY inputs, model output).
2. **The IEF/TLT weights in the brief are out of date.** Durations on the 2026-09-24 issuer pages are IEF 6.86y and TLT
   14.88y. The 2026-06-30 fact sheets said 6.95y and 15.31y. The duration match therefore moves from 64.8/35.2 to
   **62.1/37.9**. Recompute the weights every time you trade.
3. **A third fund does not pay for itself.** The best 3-fund mix (IBTP 34.8 / TLH 62.0 / TLT 3.1) has a worst twist
   error of $1,620, which is worse than the best 2-fund mixes. No long-only 3-fund mix removes the twist error. The
   liability is a "bullet": all its cash flows fall between 6 and 16 years. Constant-maturity funds cannot reproduce
   that exactly. Only a real ladder can.
4. **Cash/floor proxy:** BIL. It was on the 2025-26 list, costs 0.1353% and holds $47.9bn. Alternates are SGOV (0.09%,
   $111.8bn, not on the 2025-26 list) and SHV (on the list). If the team wants a "2031 floor" illustration trade, use
   VGSH (0.03%, on the 2025-26 list) or SHY.
5. **Laura's real ladder:** use ten Treasury STRIPS, $50,000 face each, maturing Nov 15 of the year before each Jan 1
   payment. Principal STRIPS exist for 7 of those dates. For Nov 15 2036, 2037 and 2038, use interest ("coupon") STRIPS.
   On the 2026-09-25 curve the ladder costs **$294,387 at 2027-01-01**. That is $2,124 more than the $292,264 exact-date
   figure, because each $50k arrives about 47 days early. **Headroom under the $300k deposit is about $5.6k (~19bp), not
   $7.7k (27bp).** Most of the $2.1k comes back if the early proceeds sit in T-bills for six weeks.
6. The iShares **iBonds Dec 2037-2043 Treasury funds do not exist**. iShares' full product list jumps from IBTR (Dec
   2036) to IBGA (Dec 2044) (VERIFIED-PRIMARY). So iBonds can fund only the 2033-2037 payments.

## Terms used (plain English)
- **Duration**: roughly the % a bond's price falls if interest rates rise by 1 percentage point. Duration 9.90 means
  about -9.9% for +1%. **Effective duration** is the issuer's version, which allows for how cash flows change when rates
  move.
- **DV01**: dollars gained or lost per 0.01% (1 basis point, "bp") move in rates. The liability's DV01 is $289/bp.
- **Key-rate duration (KRD)**: duration split by maturity. It shows how much value changes if only the 2y, or only the
  10y, or only the 30y yield moves. Two portfolios can have the same total duration but very different KRDs.
- **Parallel shift**: every yield moves by the same amount.
- **Twist**: short and long yields move in opposite directions. In a **steepener**, long yields rise relative to short
  ones. A **flattener** is the reverse.
- **Tracking error ($)** here means: the change in the hedge's value minus the change in the liability's value, for a
  hedge sized at $292,264. A positive number means the hedge did better than the liability.
- **STRIPS**: Treasury bonds split into separate zero-coupon pieces. Each piece pays one amount on one date. Principal
  STRIPS come from the final repayment. Interest STRIPS come from a coupon payment.
- **Defined-maturity fund** (iBonds, BulletShares): holds bonds maturing in one year. It pays out and closes around Dec
  15 of that year.
- **SEC yield**: a standard 30-day yield measure after fees. **YTM** (yield to maturity) is the average return if the
  holdings are held to maturity, before fees.

## 1. Candidate funds (issuer primary pages, accessed 2026-09-27)
Liquidity is shown as the 30-day average share volume times price, about $/day. "2025-26 list" is historical only
(`competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt`). Line numbers are the ticker lines in that file.

### 1a. Intermediate and long Treasury funds (constant maturity: the fund keeps rolling, so it never matures)
| Fund | What it holds (index) | Eff. duration (as of) | Expense | YTM / 30-day SEC | Net assets; liquidity | 2025-26 list | Status |
|---|---|---|---|---|---|---|---|
| IEF iShares 7-10Y | 16 Treasury notes, maturities May-2033 to Aug-2036 [corrected by S3 after the S4 red team, 2026-09-27] (ICE US Treasury 7-10Y) | 6.86y (9/24) | 0.15% | 5.17% / 4.84% | $41.6bn; ~8.8m sh/day (~$0.8bn); spread 0.01% | **Yes** (line 1053, #88) | VERIFIED-PRIMARY |
| TLT iShares 20+Y | 47 bonds, maturities May-2044 to Aug-2056 [corrected by S3 after the S4 red team, 2026-09-27] (ICE US Treasury 20+Y) | 14.88y (9/24) | 0.15% | 5.54% / 5.41% | $45.8bn; ~35.9m sh/day (~$2.8bn); 0.01% | **Yes** (line 1041, #87) | VERIFIED-PRIMARY |
| TLH iShares 10-20Y | 61 bonds, maturities Feb-2037 to Aug-2046 [corrected by S3 after the S4 red team, 2026-09-27] (ICE US Treasury 10-20Y) | 11.59y (9/24) | 0.15% | 5.49% / 5.29% | $10.5bn; ~2.0m sh/day (~$0.18bn); 0.01% | No | VERIFIED-PRIMARY |
| GOVT iShares US Treasury | 218 notes/bonds, Aug-2027 to May-2056 (ICE US Treasury Core) | 5.45y (9/24) | 0.05% | 5.09% / 4.83% | $41.6bn; ~10.9m sh/day (~$0.24bn); 0.05% | **Yes** (line 1089, #91) | VERIFIED-PRIMARY |
| IEI iShares 3-7Y | 83 notes (ICE US Treasury 3-7Y) | 4.20y (9/24) | 0.15% | 5.06% / 4.65% | $17.2bn; ~2.0m sh/day | No | VERIFIED-PRIMARY |
| VGIT Vanguard Interm. Treasury | 102 bonds (Bloomberg US Treasury 3-10Y) | 4.9y (8/31) | 0.03% (as of 2025-12-19) | YTM 4.5% (8/31) / SEC 4.78% (9/24) | $48.3bn total fund (8/31) | No | VERIFIED-PRIMARY |
| VGLT Vanguard Long Treasury | 101 bonds (Bloomberg US Long Treasury) | 13.5y (8/31) | 0.03% | 5.2% (8/31) / 5.41% (9/24) | $15.1bn total (8/31) | No | VERIFIED-PRIMARY |
| SPTI SPDR Portfolio Interm. Treasury | 110 holdings (Bloomberg 3-10Y US Treasury) | 4.78y option-adjusted (9/24) | 0.03% | 5.08% / 4.83% | $10.3bn; 138k sh prior day; spread 0.04% | No | VERIFIED-PRIMARY |
| SPTL SPDR Portfolio Long Treasury | 110 holdings (Bloomberg Long US Treasury) | 13.65y (9/24) | 0.03% | 5.52% / 5.48% | $10.9bn; 1.09m sh prior day; 0.04% | No | VERIFIED-PRIMARY |
| SCHR Schwab Interm. Treasury | 3-10y Treasuries | not found | 0.03% | not found | $12.3-13.5bn (conflicting snippets) | No | **SNIPPET-UNVERIFIED** (schwabassetmanagement.com blocked by egress proxy) |
| SCHQ Schwab Long Treasury | Treasuries >10y | "often exceeding 15 years" (snippet, vague) | 0.03% | not found | not found | No | **SNIPPET-UNVERIFIED** (blocked) |

### 1b. Zero-coupon / STRIPS funds (all far longer than the liability)
| Fund | Holds | Duration | Expense | YTM / SEC | Assets; liquidity | 2025-26 list | Status |
|---|---|---|---|---|---|---|---|
| EDV Vanguard Extended Duration | 80 Treasury STRIPS, 20-30y (Bloomberg US Treasury STRIPS 20-30Y Equal Par) | 24.0y (8/31) | 0.05% | 5.4% (8/31) / 5.64% (9/24) | $4.2bn total (8/31) | No | VERIFIED-PRIMARY |
| GOVZ iShares 25+Y STRIPS | 20 principal STRIPS, Aug-2051 to May-2056 | 26.45y (9/24) | 0.15% gross, **0.10% net** (fee waiver) | 5.54% / 5.64% | $311m; ~585k sh/day (~$19m); spread 0.03%; premium 0.36% | No | VERIFIED-PRIMARY |
| ZROZ PIMCO 25+Y Zero Coupon | STRIPS with 25+ years left | 27.92y (snippet) | 0.15% | not found | not found | No | **SNIPPET-UNVERIFIED** (pimco.com 403/404) |

### 1c. Defined-maturity Treasury funds (iShares iBonds; fee 0.07%; data as of 9/24-9/25)
| Fund | Holdings (maturities) | Eff. duration | YTM / SEC | Assets; ~volume | Funds the payment on | 2025-26 list |
|---|---|---|---|---|---|---|
| IBTM Dec 2032 | 15 notes, Apr-Sep 2032 | 5.05y | 5.09% / 4.79% | $555m; 216k sh | Jan 1 2033 | No |
| IBTO Dec 2033 | 11 notes, Apr-Nov 2033 | 5.71y | 5.12% / 4.83% | $452m; 226k sh | Jan 1 2034 | No |
| IBTP Dec 2034 | 4 notes, Aug-Nov 2034 | 6.44y | 5.15% / 4.90% | $317m; 111k sh | Jan 1 2035 | No |
| IBTQ Dec 2035 | 4 notes, Aug-Nov 2035 | 7.08y | 5.18% / 4.93% | $255m; 100k sh | Jan 1 2036 | No |
| IBTR Dec 2036 | 4 notes/bonds, Feb-Aug 2036 | 7.59y | 5.19% / 4.93% | **$34m** (launched 2026-03-25); 69k sh | Jan 1 2037 | No |
| (Dec 2037-2043) | **none exist** | - | - | - | 2038-2042 uncovered | - |
| IBGA Dec 2044 | 8 bonds, Aug-Nov 2044 | 11.74y | 5.54% / 5.43% | $74m | too late | No |

All VERIFIED-PRIMARY:
- iShares product pages and holdings CSVs.
- The iShares screener JSON, which lists iBonds Treasury funds IBTG-IBTR (2026-2036) and IBGA/IBGB/IBGC/IBGK/IBGL/IBGM
  (2044/45/46/54/55/56) and nothing for 2037-2043.

The pages state that "in the final year" holdings "will mature and the proceeds will be held in cash equivalents until
the liquidation of the fund", and that funds "terminate on or about October or December 15 of the year in each Fund's
name" (IBTR page). The iBonds are thin: IBTR has $34m in assets.

Invesco BulletShares Treasury (BSGR 2027, BSTS 2028, BSGT 2029, BSTU 2030, BSTV 2031) are reported as launched
2026-06-10 at 0.07%. That is **SNIPPET-UNVERIFIED**: invesco.com returned HTTP 406 to curl and was blocked for WebFetch.
They mature 2027-2031, so they cannot fund the 2033+ payments. At most they could hold the 2031 floor.

### 1d. T-bill and floating-rate funds (cash)
| Fund | Holds | Duration | Expense | YTM / SEC | Assets; liquidity | 2025-26 list | Status |
|---|---|---|---|---|---|---|---|
| BIL SPDR 1-3 Month T-Bill | 33 T-bills (Bloomberg 1-3M T-Bill) | 0.10y | 0.1353% | 3.94% / 3.59% (9/24) | $47.9bn; spread 0.01% | **Yes** (line 1101, #92) | VERIFIED-PRIMARY |
| SGOV iShares 0-3 Month | T-bills maturing Oct-Nov 2026 etc. (ICE 0-3M US Treasury) | 0.11y | 0.09% | 3.97% / 3.67% | $111.8bn; ~22.5m sh/day (~$2.3bn); 0.01% | No | VERIFIED-PRIMARY |
| SHV iShares 0-1 Year | T-bills and notes to May-2027 | 0.28y | 0.15% | 4.14% / 3.71% | $21.4bn; ~2.9m sh/day | **Yes** (line 1077, #90) | VERIFIED-PRIMARY |
| TFLO iShares Treasury Floating Rate | 8 Treasury floating-rate notes, Oct-2026 to Jul-2028 | 0.01y | 0.15% | 4.28% / 3.77% | $6.9bn; ~1.9m sh/day | No | VERIFIED-PRIMARY |
| USFR WisdomTree Floating Rate Treasury | Treasury floating-rate notes (Bloomberg US Treasury FRN) | ~0 | 0.15% | not found | $18.76bn (snippet) | **Yes** (line 1124, #94) | **SNIPPET-UNVERIFIED** (wisdomtree.com blocked) |
| SHY iShares 1-3Y (floor proxy) | 91 notes (ICE US Treasury 1-3Y) | 1.79y | 0.15% | 4.86% / 4.43% | $26.2bn; ~4.9m sh/day | **Yes** (line 1029, #86) | VERIFIED-PRIMARY |
| VGSH Vanguard Short Treasury (floor proxy) | 92 bonds (Bloomberg US Treasury 1-3Y) | 1.9y (8/31) | 0.03% | 4.3% (8/31) / 4.55% (9/24) | $39.3bn total (8/31) | **Yes** (line 1113, #93) | VERIFIED-PRIMARY |

## 2. Duration-matched mixes and how well they track the liability
Method (script):
- The same official 2026-09-25 par curve and bootstrap as `research/verified_2026-09-27/official_curve_pv.py`.
- The liability is valued at 2027-01-01 ($292,264; model duration 9.90; DV01 $289).
- Each fund is valued from its **actual holdings' cash flows** on that curve, so its key-rate profile is real, not
  assumed.
- Weights solve (weight × issuer duration) = 9.90 using the issuer's current effective duration, as the task asks.
Scenario definitions (ASSUMPTION, chosen to be simple and symmetric):
- Parallel ±100bp.
- 2s30s twist: 2y -25bp and 30y +25bp for a steepener, straight line in between (pivot about 16y).
- 2s10s twist: 2y -25bp and 10y +25bp, flat beyond 10y.
Other ASSUMPTIONs:
- Shocks are instantaneous, with no fees or bid/ask.
- SPTI/SPTL use VGIT/VGLT holdings as proxies (same Bloomberg index families).

What the liability itself does:

| Scenario | +100bp | -100bp | Steepener 2s30s | Flattener 2s30s | Steepener 2s10s | Flattener 2s10s |
|---|---|---|---|---|---|---|
| Liability change | -$27,373 | +$30,600 | +$1,693 | -$1,666 | -$7,522 | +$7,630 |

Key-rate durations (model; they sum to about the total duration). The liability sits on the 7y, 10y and 20y points and
has **zero** 30y exposure:

| | 7y | 10y | 20y | 30y | model / issuer dur. |
|---|---|---|---|---|---|
| Liability | 1.58 | 6.74 | 2.53 | 0.00 | 9.90 |
| IEF | 3.42 | 3.58 | 0 | 0 | 6.90 / 6.86 |
| TLH | -0.25 | 3.59 | 8.75 | 0 | 11.87 / 11.59 |
| TLT | -0.18 | -0.93 | 5.94 | 10.55 | 15.22 / 14.88 |
| IBTR | 1.01 | 6.73 | 0 | 0 | 7.64 / 7.59 |
| VGLT (=SPTL proxy) | -0.21 | 1.16 | 7.26 | 5.65 | 13.67 / 13.5 |

**2-fund mixes.** Tracking error is in $ for a $292,264 hedge; a positive number means the hedge beat the liability.
| Mix (weights) | Fee | +100bp | -100bp | Worst 50bp twist | Twist detail (2s30s steep/flat; 2s10s steep/flat) | Both on 2025-26 list? |
|---|---|---|---|---|---|---|
| **IEF 35.7 / TLH 64.3** | 0.150% | -244 | +991 | **1,352** | -1,352 / +1,333; +612 / -555 | IEF yes, TLH no |
| IBTR 42.2 / TLH 57.8 (best found) | 0.116% | -244 | +919 | 1,176 | -1,176 / +1,160; +197 / -149 | no |
| **IEF 62.1 / TLT 37.9** (today's durations) | 0.150% | +165 | +1,274 | **3,619** | -3,584 / +3,619; +1,266 / -1,161 | **both yes** |
| IEF 64.8 / TLT 35.2 (brief, June durations) | 0.150% | +726 | +499 | 3,291 | -3,258 / +3,291; +1,479 / -1,388 | both yes |
| GOVT 52.8 / TLT 47.2 | 0.097% | +423 | +1,904 | 5,929 | -5,895 / +5,929; +1,386 / -1,183 | both yes |
| VGIT 41.9 / VGLT 58.1 | 0.030% | +500 | +1,033 | 3,849 | -3,835 / +3,849; +1,606 / -1,469 | no |
| SPTI 42.3 / SPTL 57.7 | 0.030% | +595 | +910 | 3,816 | similar to VGIT/VGLT | no |

**3-fund mixes** (weights ≥ 0 summing to 1, duration 9.90, chosen to minimise key-rate gaps):
| Mix | Worst twist | ±100bp worst |
|---|---|---|
| IBTP 34.8 / TLH 62.0 / TLT 3.1 (best 3-fund) | $1,620 | $1,050 |
| IEF 40.4 / TLH 53.0 / TLT 6.7 | $1,744 | $1,041 |
| IBTR 51.0 / TLH 38.3 / TLT 10.7 | $1,767 | $984 |
| iBonds IBTM-IBTR 6.5% each + TLH 67.6% (6 funds, reference) | $1,471 | $1,037 |

Asking a 3-fund mix to match value, duration **and** the 2s30s twist exactly gives a negative weight for every
combination (script output). No long-only fund mix can do this.

What the numbers say:
- **Parallel moves are handled by any duration match.** The ±100bp error is at most about $1.3k (0.4% of the
  liability) for IEF/TLH and IEF/TLT.
  - Most of it is convexity: the barbell gains a little more when rates fall.
  - Some of it is the gap between the issuer's durations and the par-curve model's durations (model TLT 15.22 vs issuer
    14.88).
- **Twists separate the choices.** The liability has no 30y exposure. TLT's weight sits on the 20y and 30y points, while
  the liability's biggest single exposure is the 10y point. So the IEF/TLT barbell is short the 10y and long the 30y by
  about 4 duration-years each. This matches the brief's "twist gap ~$3-4k", now recomputed with real holdings: $3.3-3.6k.
- TLH puts the long leg on the 10y and 20y points, where the liability is. That cuts the worst twist error by about 63%
  **with the same number of funds and the same fee**. This is complexity-free precision.
- Scale check: a 50bp twist in the 6 weeks of WInS trading would be unusual. Realistic 10-20bp twists mean errors of a
  few hundred dollars for IEF/TLH, against about $1k for IEF/TLT. The case for TLH is the logic (its bonds sit closer to the payment dates than TLT's), not the dollars. The earlier
  wording "the bonds mature when Laura pays" was wrong for most of TLH [corrected by S3 after the S4 red team, 2026-09-27].
- **Weights drift.** As rates rose, TLT's duration fell from 15.31 to 14.88 and IEF's from 6.95 to 6.86. That moved the
  match by 2.7 points of weight. Rule for the team: recompute weights from the issuer page on every trade date.
  - IEF weight = (D_TLH - 9.90) / (D_TLH - D_IEF); TLH weight = 1 - IEF weight [corrected by S3 after the S4 red team, 2026-09-27].
  - Note that the liability's own duration also shortens by about 0.25 a quarter as time passes (ASSUMPTION: rough
    roll-down; not modelled here).

If the WInS "mirror" is about 65% Treasuries (brief section 7; not approved), IEF/TLH comes to about **23.2% IEF + 41.8%
TLH** of the total WInS portfolio. The IEF/TLT fallback comes to about 40.4% IEF + 24.6% TLT.

## 3. Laura's real (non-WInS) ladder: what exactly to buy in January 2027
The source is Treasury's Monthly Statement of the Public Debt, Table V ("holdings of Treasury securities in stripped
form"), record date 2026-08-31, from api.fiscaldata.treasury.gov (VERIFIED-PRIMARY, accessed 2026-09-27). It lists every
strippable note and bond with its principal-STRIPS CUSIP and the amount already stripped. TreasuryDirect confirms three
points (VERIFIED-PRIMARY):
- STRIPS are bought, held and sold "only through a financial institution, a broker, or dealer".
- Par must be in "multiples of $100".
- Each stripped piece "is a zero-coupon security that matures separately" with its own CUSIP.

Costs are for $50,000 face, valued at 2027-01-01 on the 2026-09-25 curve.
ASSUMPTION: STRIPS are priced on the par-derived zero curve. Real STRIPS quotes can differ by a few bp, and a 10bp
difference on a 10-year zero is about 1% of that rung's cost.

| Payment | Recommended rung (maturity) | Instrument (principal-STRIPS CUSIP; underlying; $ already stripped 8/31) | Cost at 2027-01-01 | Alternates (cost) |
|---|---|---|---|---|
| Jan 1 2033 | Nov 15 2032 | Principal STRIP 912821KC8 of the 4.125% note 91282CFV8 ($26m) | $37,253 | Dec 31 2032 principal 912821TN5 ($1.6m stripped, thin) $37,007; Aug 15 2032 principal 912821JN6 ($169m) $37,747; IBTM ~$37,218 |
| Jan 1 2034 | Nov 15 2033 | Principal STRIP 912821NP6 of the 4.5% note 91282CJJ1 ($17m) | $35,336 | Aug 15 2033 912821LW3 ($27m) $35,812; May 15 2033 912821LG8 ($225m) $36,293; IBTO ~$35,346 |
| Jan 1 2035 | Nov 15 2034 | Principal STRIP 912821QX6 of the 4.25% note 91282CLW9 ($209m) | $33,495 | Aug 15 2034 912821QH1 $33,952; IBTP ~$33,550 |
| Jan 1 2036 | Nov 15 2035 | Principal STRIP 912821TF2 of the 4% note 91282CPJ4 ($246m) | $31,720 | Aug 15 2035 912821SR7 ($1,183m, deepest) $32,162; IBTQ ~$31,826 |
| Jan 1 2037 | Nov 15 2036 | **Interest STRIP** due 11/15/2036 (no Nov-2036 principal on 8/31; see note) | $30,007 | May 15 2036 principal 912821UK9 ($40m) $30,861; Aug 15 2036 912821UZ6 ($1m) $30,432; IBTR ~$30,227 |
| Jan 1 2038 | Nov 15 2037 | **Interest STRIP** due 11/15/2037 (no principal STRIPS Jun-Dec 2037) | $28,362 | May 15 2037 principal 912803DA8 (5% bond, $504m) $29,183 |
| Jan 1 2039 | Nov 15 2038 | **Interest STRIP** due 11/15/2038 (no principal STRIPS Jun-Dec 2038) | $26,779 | May 15 2038 principal 912803DD2 (4.5% bond, $559m) $27,569 |
| Jan 1 2040 | Nov 15 2039 | Principal STRIP 912803DJ9 of the 4.375% bond 912810QD3 ($1,893m) | $25,257 | Aug 15 2039 912803DH3 $25,635 |
| Jan 1 2041 | Nov 15 2040 | Principal STRIP 912803DP5 of the 4.25% bond 912810QL5 ($969m) | $23,791 | 912803FU2 (1.375% bond, same date, $118m) $23,791 |
| Jan 1 2042 | Nov 15 2041 | Principal STRIP 912803DU4 of the 3.125% bond 912810QT8 ($520m) | $22,387 | 912803GD9 (2% bond, same date) $22,387 |
| **Total** | | | **$294,387** | exact-date value $292,264 |

Notes on the ladder:
- **Why Nov 15:** Treasury notes and bonds mature on the 15th (Feb/May/Aug/Nov) or at month-end. Nov 15 is the last
  common maturity before each Jan 1.
- **Interest STRIPS for Nov 15 2036-2038 exist.** $272.1bn of fixed-rate notes and bonds that pay coupons every May 15
  and Nov 15 until 2042-2056 is already held in stripped form (Table V, 38 securities; VERIFIED-PRIMARY). Stripping a
  bond creates an interest piece for every remaining coupon date. Table V does not list interest-STRIPS CUSIPs or amounts
  by date, so the exact CUSIPs and how deep the market is are **not verified**. In market practice, interest pieces with
  the same payment date share one CUSIP ("fungible"); that is SNIPPET-UNVERIFIED general knowledge. A broker quote would
  confirm.
- **Nov 15 2036 principal:** the 10-year note sold at the November 2026 refunding would mature Nov 15 2036. The pattern
  in Table V (10-year notes dated 2035-11-15, 2036-02-15, 2036-05-15, 2036-08-15) supports this, but it is an
  ASSUMPTION until the Treasury auction announcement. If it happens, its principal STRIP (same $30,007 cost) can replace
  the interest STRIP for Jan 2037.
- **The ladder costs $2,124 more than the exact-date $292,264**, because each rung pays about 47 days early (Nov 15 vs
  Jan 1). The rest of the gap: the early cash earns T-bill interest for about 47 days, roughly $250 per rung at ~4%
  (ASSUMPTION about future bill rates). If the team uses May-dated principal STRIPS for 2038 and 2039 instead of interest
  STRIPS, add about $1.6k.
- **Updated headroom:** $300,000 - $294,387 = $5,613, which is about 19bp of rates (DV01 $289). The verified model's 27bp
  assumes exact-date zeros.
- **Transaction cost:** broker mark-ups on small STRIPS lots are unknown (UNVERIFIED). Ten $50k-face lots could plausibly
  cost 0.1-0.5% each (ASSUMPTION, not sourced). Get a quote before relying on the headroom.
- **Alternatives:**
  - iBonds IBTM-IBTR for 2033-2037. Costs are similar ($37.2k-$30.2k per rung, using issuer YTM less the 0.07% fee;
    ASSUMPTION: YTM is earned).
    - Advantage: a fund is easier to hold.
    - Disadvantages: monthly coupon distributions must be reinvested; the fund pays out around Dec 15, so the cash sits
      for two weeks; IBTR has only $34m in assets.
    - Nothing exists for 2038-2042.
  - Coupon notes and bonds maturing each Nov 15, sized so that principal plus coupons cover each payment.
    - This is possible, but the coupons received in 2027-2032 arrive before any payment and must be reinvested at
      unknown rates. The brief estimates about $5k of coupon reinvestment risk.
    - STRIPS avoid this, which is why they are the primary pick (consistent with brief section 8 item 11).

## 4. Recommendations
Every WInS pick below is **PENDING APPROVAL CHECK: confirm on this year's WInS approved list/rules before trading.**

**(a) WInS hedge sleeve (the "promise" sleeve; mirrors the ten fixed payments)**
- **Primary: IEF 35.7% + TLH 64.3% of the hedge sleeve.** Recompute from issuer durations on the trade date.
  - Key facts: IEF 0.15%, 6.86y, 16 notes due 2033-2036, $41.6bn; TLH 0.15%, 11.59y, 61 bonds due 2037-2046, $10.5bn.
    Both 9/24-9/25, ishares.com, accessed 2026-09-27.
  - Why it fits Laura: the funds own bonds that mature in the years she pays (2033-2042). This is the closest a 2-fund
    ETF mix gets to her actual ladder, and it has the smallest twist error of the liquid choices ($1,352 vs $3,619).
  - Tie to the case: "a high degree of certainty" for fixed $50k payments.
  - Trading Notes angle: Wharton's own example note buys an intermediate-term Treasury ETF "to reduce portfolio volatility and begin preparing for
    Laura’s future operating commitment" (Trading Notes guide p.2).
  - 2025-26 list: IEF yes; TLH **no**.
- **Alternate 1: IEF 62.1% + TLT 37.9%.** Both were on the 2025-26 list, so this is the most likely to be approved.
  - Worst twist error $3.6k; TLT is very liquid ($45.8bn).
  - Use this if TLH is not approved.
- **Alternate 2: SPTI 42.3% + SPTL 57.7%** (or VGIT 41.9% + VGLT 58.1%). Cheapest at 0.03%, but the twist error is
  about $3.8k and neither pair was on the 2025-26 list.
- Not recommended:
  - STRIPS funds (EDV, GOVZ, ZROZ): durations of 24-28y put 12-29% of the sleeve (in the duration-matched pairs) on the 30y point, where the liability
    has nothing.
  - GOVT/TLT: worst twist $5.9k.
  - A third fund: it adds no accuracy.

**(b) WInS cash / floor proxy**
- **Primary: BIL.** 0.1353%, 0.10y duration, 33 T-bills, $47.9bn, spread 0.01% (ssga.com, 9/24).
  - Pick it over SGOV because it was on the 2025-26 list (line 1101). Over six weeks, the 0.045% fee gap costs about $5
    per $100k.
  - Last year's lesson was that the team traded outside the rules, so the higher chance of approval wins.
- **Alternates:** SGOV (0.09%, $111.8bn, 0.11y; not on the 2025-26 list); SHV (0.15%, 0.28y; on the 2025-26 list).
  - TFLO and USFR are floating-rate options (USFR was on the 2025-26 list; its facts are SNIPPET-UNVERIFIED).
- **Optional "2031 floor" illustration** (the floor is bought in a 2-year Treasury): VGSH (0.03%, 1.9y, on the 2025-26
  list) or SHY (0.15%, 1.79y, on the list).
  - Use only if the team wants a discipline/floor trade for the Trading Notes (blueprint trade 3).
  - Keep it small: the real floor decision is in 2031.

**(c) Laura's real ladder (January 2027; not a WInS trade, but still subject to the team's approval of the strategy)**
- **Primary:** ten Treasury STRIPS, $50,000 face each, maturing Nov 15 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039,
  2040 and 2041.
  - Use principal STRIPS where they exist (2032-2035 and 2039-2041); use interest STRIPS for 2036-2038, or the new Nov-15
    2036 note's principal once it is issued.
  - Cost is about **$294.4k** at the 9/25 curve.
  - Buy the longest rungs first if rates fall before January (brief section 7).
- **Alternate 1:** iBonds IBTM-IBTR for the 2033-2037 payments plus STRIPS for 2038-2042.
- **Alternate 2:** May- or Aug-dated principal STRIPS where Nov-dated ones are missing or thin: 2037-05-15 ($504m
  stripped) and 2038-05-15 ($559m). This adds about $1.6k.

## 5. Open issues for Phases B-E
- **This year's WInS list.** Is TLH on it? Can WInS trade iBonds, STRIPS funds or individual Treasuries at all?
  (UNKNOWN.)
- **TLH not approved.** IEF/TLT is the fallback. Tell the team the twist gap is about $3.6k per 50bp and explain why.
- **Interest-STRIPS CUSIPs and depth** for 11/15/2036-2038, and broker mark-ups on $50k lots: get a real quote.
  (UNVERIFIED.)
- **Nov 2026 refunding:** confirm the new 10-year note matures 2036-11-15. (ASSUMPTION.)
- **Snippet-only facts:** Schwab, WisdomTree, PIMCO and Invesco pages were blocked (HTTP 403/406, egress proxy). SCHR,
  SCHQ, USFR, ZROZ and BSxx remain SNIPPET-UNVERIFIED.
- **Vanguard data age:** Vanguard durations are from 2026-08-31, a month older than the iShares/SSGA figures. Rates rose
  in September, so they are slightly overstated.
- **Liability duration drift:** the liability's duration shortens over time, and the 2027-01-01 anchor gets closer.
  Recompute the 9.90 target before each rebalance.

## Sources (all accessed 2026-09-27)
- iShares product pages (key facts, portfolio characteristics) and "latest-holdings.csv" for each fund:
  - IEF https://www.ishares.com/us/products/239456/ishares-710-year-treasury-bond-etf
  - TLT https://www.ishares.com/us/products/239454/ishares-20-year-treasury-bond-etf
  - TLH https://www.ishares.com/us/products/239453/ishares-1020-year-treasury-bond-etf
  - GOVT https://www.ishares.com/us/products/239468/ishares-us-treasury-bond-etf
  - IEI https://www.ishares.com/us/products/239455/ishares-37-year-treasury-bond-etf
  - GOVZ https://www.ishares.com/us/products/315911/ishares-25+-year-treasury-strips-bond-etf
  - IBTM https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf
  - IBTO https://www.ishares.com/us/products/332291/ishares-ibonds-dec-2033-term-treasury-etf
  - IBTP https://www.ishares.com/us/products/337745/ishares-ibonds-dec-2034-term-treasury-etf
  - IBTQ https://www.ishares.com/us/products/342105/ishares-ibonds-dec-2035-term-treasury-etf
  - IBTR https://www.ishares.com/us/products/350028/ishares-ibonds-dec-2036-term-treasury-etf
  - IBGA https://www.ishares.com/us/products/337747/ishares-ibonds-dec-2044-term-treasury-etf
  - SGOV https://www.ishares.com/us/products/314116/ishares-0-3-month-treasury-bond-etf
  - SHV https://www.ishares.com/us/products/239466/ishares-short-treasury-bond-etf
  - TFLO https://www.ishares.com/us/products/260652/ishares-treasury-floating-rate-bond-etf
  - SHY https://www.ishares.com/us/products/239452/ishares-13-year-treasury-bond-etf
- iShares product screener (full US fund list, used for "no Dec 2037-2043 iBonds Treasury"):
  https://www.ishares.com/us/product-screener/product-screener-v3.1.jsn?dcrPath=/templatedata/config/product-screener-v3/data/en/us-ishares/ishares-product-screener-backend-config&siteEntryPassthrough=true
- Vanguard (the data behind the investor.vanguard.com fund profile pages):
  - Endpoints: https://investor.vanguard.com/vmf/api/{VGIT,VGLT,EDV,VGSH}/{profile,characteristic,price,expense} and
    .../portfolio-holding/bond.json
  - Profile page: https://investor.vanguard.com/investment-products/etfs/profile/vgit
- SSGA:
  - SPTI https://www.ssga.com/us/en/intermediary/etfs/spdr-portfolio-intermediate-term-treasury-etf-spti
  - SPTL https://www.ssga.com/us/en/intermediary/etfs/spdr-portfolio-long-term-treasury-etf-sptl
  - BIL https://www.ssga.com/us/en/intermediary/etfs/spdr-bloomberg-1-3-month-t-bill-etf-bil
- U.S. Treasury:
  - Monthly Statement of the Public Debt, Table V (record date 2026-08-31):
    https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_5?filter=record_date:eq:2026-08-31
  - TreasuryDirect STRIPS page: https://www.treasurydirect.gov/marketable-securities/strips/
- Snippets only (WebSearch, 2026-09-27; primary pages blocked):
  - SCHR: https://www.schwabassetmanagement.com/products/schr, https://cbonds.com/etf/1447/
  - SCHQ: https://cbonds.com/etf/2767/
  - ZROZ: https://www.morningstar.com/funds/arcx/zroz/quote, https://www.aaii.com/etf/ticker/ZROZ
  - USFR: https://www.wisdomtree.com/us/products/fixed-income/usfr
  - BulletShares Treasury: https://etfdb.com/innovative-etfs-content-hub/invesco-grows-bulletshares-suite-treasury-etfs/,
    https://www.aaii.com/etf/ticker/BSTV
- Repo files:
  - `competition/official_market_data/daily-treasury-rates_2026-09.csv` (row 09/25/2026)
  - `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt` (lines 1029-1124)
  - `research/verified_2026-09-27/official_curve_pv.py`
  - `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` (example note, p.2)

## What this teaches
Two portfolios with the same duration can behave differently. Duration only promises protection when every interest
rate moves by the same amount. Laura's payments fall between 2033 and 2042. IEF + TLH owns bonds much closer to
those years than IEF + TLT does (though most of TLH matures after 2042 [corrected by S3 after the S4 red team, 2026-09-27]), so it follows her payments even when short and long rates move apart. IEF + TLT gets the same total
duration by pairing short bonds with 30-year bonds she does not need, and the gap shows up when the curve twists. Adding
a third fund did not help. The simplest fix was choosing the right second fund. For her real money, the best "hedge" is
not a fund at all: ten zero-coupon Treasuries that each pay $50,000 just before a payment date. Real instruments carry
real frictions (they mature on Nov 15, not Jan 1, and some dates exist only as interest STRIPS), and those frictions
cost about $2k of the headroom. Checking what actually exists changes the numbers.
