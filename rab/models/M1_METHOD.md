# M1 method: ladder cost and WInS book cost

WS1, 2026-09-30 (Sydney). AI-generated research specification (Claude Code) for Team Caplet; no deliverable text.

**Purpose.** An exact, implementation-independent recipe. A second builder who reads only this file and the raw
inputs in section 1 must reproduce every M1 number to $1 (Gate A). No results are printed here on purpose.
The reference implementation is `rab/models/m1_ladder.py`; the blind builder must not read it.

**Scope.** (A) the value of Laura's ten $50,000 payments on the official par curve; (B) the cost of the WInS book
in the Sheet `Portfolio` tab (and the alternative `Book L`); (C) a yield check of every WInS bond price; (D) a
look-through check of the iBonds ETFs; (E) coupon reinvestment stress on the buyable ladder; (F) the plan split;
(G) the history comparison ("cheapest since ...", "2020 yields"). Strategy is not reopened (RUN_PLAN s0).

---

## 1. Inputs (raw files only; paths relative to the worktree root)

| Id | File | What it is |
|---|---|---|
| I1 | `rab/data/treasury_par_2000_2026/2026.csv` | U.S. Treasury Daily Par Yield Curve, 2026. Row `09/28/2026` is the reference curve. Yields in percent, semiannual bond-equivalent |
| I2 | `rab/data/treasury_par_1990_1999/*.csv`, `rab/data/treasury_par_2000_2026/<year>.csv` | Same series, every day 1990-2026 (section G only) |
| I3 | `rab/data/sheet/Portfolio_values_2026-09-30T0030AEST.csv` | Sheet tab `Portfolio`, values as displayed (read 30 Sep 00:30 AEST) |
| I4 | `rab/data/wins/wins_prices_2026-09-28.csv` | WInS 28 Sep 2026 closes: ETF prices per share; bond clean prices and accrued per $100 face; coupon, maturity, CUSIP; plus the Book L sizes |
| I5 | `rab/data/etf/nasdaq_historical.json` | 28 Sep 2026 consolidated closes for ETFs not shown in WInS Notes |
| I6 | `research/insight_v1/wins_now/S1_fund_holdings_snapshot.csv` | iShares holdings of IBTM-IBTR as of 24 Sep 2026 (par, coupon, maturity) |
| I7 | `rab/data/ishares/ibonds_facts.csv` | iShares NAV, shares outstanding, closing price, 28 Sep 2026 |

## 2. Conventions used everywhere

- **Reference date** D = the curve date (28 Sep 2026). Valuation is at the close of D. Settlement date S = D
  (the WInS accrued figures were computed to about 28 Sep; the real settlement convention in WInS is UNVERIFIED).
- **Year fraction** tau(d) = (calendar days from D to d) / 365.25.
- **Money** in U.S. dollars; results rounded to the dollar only at the end.
- **Coupon schedule** of a Treasury with coupon c (percent) and maturity M: semiannual dates M, M-6 months,
  M-12 months, ...; stepping back uses the same day of month, clamped to the month end; if M is the last day of its
  month, every coupon date is the last day of its month (end-of-month rule). Each coupon pays c/2 per 100 face.
- **Accrued interest** at S, per 100 face: (c/2) x (days from the previous coupon date to S) / (days from the
  previous to the next coupon date) (actual/actual ICMA).
- **Coupons from I6** are rounded to 2 decimals in the file; use the nearest 1/8 of a percent (round(8c)/8).

## A. The ten payments on the par curve (liability value)

**A1. Curve (the "D1 method").**
1. Tenors used, in years: 1 Mo = 1/12, 2 Mo = 2/12, 3 Mo = 0.25, 6 Mo = 0.5, 1 Yr = 1, 2 Yr = 2, 3 Yr = 3,
   5 Yr = 5, 7 Yr = 7, 10 Yr = 10, 20 Yr = 20, 30 Yr = 30. The columns "1.5 Month" and "4 Mo" are NOT used.
   A blank tenor is skipped.
2. Par grid: t_j = 0.5 j for j = 1..60. p_j = linear interpolation of the (tenor, par yield / 100) points at t_j;
   flat beyond the first and last available tenor.
3. Bootstrap (each grid point is a par bond paying p_j/2 every half-year):
   DF_j = (1 - (p_j/2) x (DF_1 + ... + DF_{j-1})) / (1 + p_j/2), with DF_1 = 1 / (1 + p_1/2).
4. Discount factor for any date d: DF(d) = exp(L(tau(d))), where L is the linear interpolation of the points
   (0, 0), (t_1, ln DF_1), ..., (t_60, ln DF_60) (log-linear discount factors; flat ln DF beyond 30 years).
5. A parallel shift of b basis points adds b/100 to every par yield (in percent) before step 2.

**A2. Payment dates.** Exact basis: 1 January 2033, 2034, ..., 2042, $50,000 each. Nov-15 basis (the maturity of the
STRIPS that would fund them): 15 November of the year before each payment (15 Nov 2032 ... 15 Nov 2041).

**A3. Outputs.** For each basis:
- Spot value at D: V0 = sum over the ten dates of 50,000 x DF(date).
- Forward value at A = 1 January 2027 (the day Laura's $300,000 arrives): V_A = V0 / DF(A).
- Headroom: 300,000 - V_A, and the break-even parallel fall: the shift b < 0 at which V_A(b) = 300,000
  (solve to 0.01bp; report the fall as a positive number of basis points).
- Forward value at 1 January 2028: V0 / DF(1 Jan 2028) (used in F).

**A4. Model-risk band (report, never headline).** Recompute V0 and V_A with: (i) days/365 instead of 365.25;
(ii) (i) plus the 1, 2 and 3-month yields added as extra discount-factor nodes, DF = (1 + y/2)^(-2t) at t = 1/12, 2/12,
0.25; (iii) the par curve interpolated with a monotone cubic (PCHIP) instead of linear in step 2; (iv) zero rates
(continuously compounded, -ln DF / t) interpolated linearly in t instead of ln DF.

**A5. Laura's real ladder is a STRIPS ladder** (zero-coupon, Nov-15 basis): no coupon reinvestment; each $50,000 waits
47 days (15 Nov to 1 Jan) in cash.

## B. Cost of the WInS book

**B1. Book cost** for a list of holdings h with quantity q_h and price P_h:
- ETF: value_h = q_h x P_h (q = shares, P = price per share).
- Treasury: value_h = q_h x (clean_h + accrued_h) / 100 (q = face value in dollars; UNVERIFIED unit in WInS, PM-02).
- Commission: $25 per ETF trade, $10 per Treasury trade, one trade per holding.
- Cost = sum of value_h + sum of commissions. Cash left = 300,000 - cost. Weight_h = value_h / 300,000.

**B2. Holdings.** `Portfolio` tab (I3): the eleven holdings and the quantities in its units column (IBTM, IBTO,
IBTP, IBTQ, IBTR, T 4.750% 15-Feb-2037, T 4.500% 15-May-2038, T 4.375% 15-Nov-2039, T 4.250% 15-Nov-2040,
T 3.125% 15-Nov-2041, VT). `Book L`: the ten ladder holdings and sizes in I4.

**B3. Price sets** (each result names its set):
- `sheet_as_read`: prices displayed in I3 (ETF prices there are live GOOGLEFINANCE values at the read time; bond
  prices are clean + accrued as typed).
- `close_0928`: the prices in I4 (ETF: WInS 28 Sep close where the team recorded one, else the iShares closing price
  for 28 Sep, which equals the Nasdaq consolidated close rounded to the cent); bond clean and accrued as recorded (I4).
- `close_0928_model_accrued`: as `close_0928`, but accrued interest recomputed by section 2 at S = D.

**B4. Sizing rule check** (reproduces the Sheet's formulas; report differences, do not change the book):
- Book L: target_h = 50,000 x DF(end_h) with end = 15 Dec of the iBond's year or the bond's maturity; ETF shares =
  ceiling(target / price); bond face = ceiling(target / (dirty/100) / 1,000) x 1,000.
- Portfolio: ladder share 65.9%, floor 24.3%, stock fund 8.7%, cash 1.1% of $300,000 (typed-in split). Rung
  target_h = 0.659 x 300,000 x (Book L value_h / sum of the ten Book L values), where the Book L values are those of
  the Book L rule above at the same prices (commissions excluded); IBTM adds 0.243 x 300,000; VT target =
  0.087 x 300,000. ETF shares = floor(target / price); bond face = floor(target / (dirty/100) / 1,000) x 1,000.
  Dirty = clean + recorded accrued (I4).

**B5. Cash margin.** Keep the Portfolio quantities and `close_0928` prices. Apply a parallel shift b to the curve:
each Treasury's value scales by Dirty_model(b) / Dirty_model(0) (section C step 2); each iBond ETF's value scales by
model NAV(b) / model NAV(0) (section D); VT is unchanged. Report the fall in yields (positive bp) at which cost
reaches $300,000, and at which cash left falls below $1,000 (solve to 0.01bp).

## C. Yield check of WInS bond prices

For each WInS Treasury price (the five in the book, the two noted as stale on 29 Sep, and any alternate):
1. Dirty_WInS = clean + accrued (accrued from section 2 at S; also report the WInS-recorded accrued).
2. Dirty_model = sum over coupon and principal flows after S of flow x DF(flow date) / DF(S) (curve A1, no shift).
3. Yield of a dirty price P (street convention): the y solving P = sum_k CF_k / (1 + y/2)^(k - 1 + w), k = 1..n over the
   remaining flows, w = (days from S to the next coupon) / (days in that coupon period).
4. Gap = yield(Dirty_WInS) - yield(Dirty_model), in basis points (positive = WInS price is cheap against the curve).
   Also report yield(Dirty_WInS) minus the par yield interpolated (A1 step 2) at the bond's maturity.
5. **Flag** any |Gap| > 25bp as "stale or wrong: do not trade at this price; use the named alternate".

## D. iBonds ETF look-through

Per share of fund f: a_i = par_i (I6) / shares outstanding (I7) for each note i; money-market and cash lines at
face. Model NAV = sum_i a_i x Dirty_model_i / 100 + cash per share. Report model NAV / published NAV - 1 and the
parallel shift of the curve that makes model NAV equal published NAV ("fund price vs curve", bp). Share counts
(28 Sep) and holdings (24 Sep) differ by four days: a creation in between biases the ratio; say so.
For the cash-flow schedule in E, scale a_i by k_f = published NAV / model NAV so the flows are worth the fund.
ETF yield check (independent of the share-count timing): iShares "Average Yield to Maturity" minus the par yield
(A1 step 2) at the fund's "Weighted Avg Maturity" (both from I7), in bp; flag if |gap| > 25bp. Also report the
premium/discount of the closing price to NAV (I7).

## E. Coupon reinvestment stress (PM-23)

**E1. Holder cash flows**, from S to the holding's payment date T_h (1 January of the payment year):
- Treasury: q x c/2 / 100 on each coupon date after S (up to maturity), q at maturity. Price paid = WInS clean +
  accrued from section 2 (not the recorded accrued).
- iBond ETF (per share, times shares): for each note i, a_i k_f x c_i/2/100 on each of its coupon dates after S,
  paid to the holder on that date (ASSUMPTION: the fund's monthly distribution timing is ignored); fee
  -(0.0007/12) x P_ETF per share at each month end after S up to the termination date E_f = 15 December of the fund
  year (ASSUMPTION: "on or about ... December 15", iShares); note principal a_i k_f is held inside the fund from its
  maturity to E_f at the scenario rate, then paid to the holder at E_f.

**E2. Delivered value** at T_h at reinvestment rate r: V_h(r) = sum_k CF_k x (1 + r/2)^(2 x tau_k), where tau_k is
the year fraction (days/365.25) from the flow date to T_h. "Curve" scenario: V_h = sum_k CF_k x DF(t_k) / DF(T_h).

**E3. Scenarios.** r = own yield y_h; y_h - 2 points; 2%; 0% (WInS cash earns 0%); and "curve" (today's forwards).
Own yield y_h = the single rate r at which the value at S of V_h(r) discounted back at r equals the cost paid
(i.e. the IRR of the E1 flows at the price paid, with the fund's internal cash also earning r), semiannual compounding.

**E4. Outputs.** Book L: V_h(r) per rung and summed, against $50,000 per rung and $500,000 in total. Buffer cost =
sum over rungs with V_h(r) < 50,000 of cost_h x (50,000 / V_h(r) - 1) (more of the same holding, same price).
Portfolio tab: V_h(r) / V_h(curve) per rung (the Portfolio rungs are Book L rungs scaled, so the ratio carries over).

## F. Plan split on the current curve (E6 [7] method)

With V_A (exact basis) from A3: leftover = 300,000 - V_A. On 2 January 2028: ladder = V0 / DF(1 Jan 2028);
growth money G = leftover x (1 + y1) + 150,000; floor = 150,000 / (1 + y5)^5; stock fund = G - floor;
total = ladder + G. y1, y5 = the 1-year and 5-year par yields of the reference curve (annual compounding, as E6).
Shares: ladder / total, floor / total, stock fund / total. Also report on the Nov-15 basis.

## G. History ("cheapest since", "2020 yields")

For every curve date d in I2 (1990-2026) with at least the 6-month and 10-year yields present: build the A1 curve
for d. Keep each payment's time from the reference date ("same time to maturity"): on day d, payment date P is
replaced by d + (P - D) and A by d + (A - D). Compute V0(d) and V_A(d) on the Nov-15 basis (the IPS's "$289k" basis)
and on the exact basis. Report: the 2020 median, minimum and maximum; the maximum over all days and its date; the
share of days with V_A <= 300,000 (since 2000 and since 1990); and the last date before D with a value at or below
the value on D ("the cheapest since ..."). Deposit check (as the rescued script): unfunded part on day d =
max(0, V_A(d) - 300,000 - 150,000 x DF_d(A_d + 365 days) / DF_d(A_d)); count the days with a positive value.

## Tolerances and gate

Gate A: the blind builder's A3 values (both bases, spot and forward) and B1 costs agree with the reference to $1.
Yields in C to 0.5bp. E and G to $100 and to the same dates. A difference is explained, never averaged.

## Known limits (state them wherever the numbers are used)

MODEL prices, not dealer quotes (STRIPS mark-ups would add cost). One curve, one day. WInS settlement, bond unit and
accrued conventions are UNVERIFIED. iBond distributions are modelled as pass-through coupons. History uses today's
payment times ("same time to maturity"), not the calendar of a real past purchase.
