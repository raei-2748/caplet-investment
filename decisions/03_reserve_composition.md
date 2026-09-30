# D3: Reserve size, composition, and how it changes 2033–2042

**Status:** DECIDED · **Evidence:** `tables.md` → Liability table, Reserve run-off; `results.json` → `grid[*].reserve_cost_2033`

## Question
What should the operating reserve hold, how large will it be in 2033, and how should it change as payments are made?

## Options
| Option | Pros | Cons |
|---|---|---|
| **Nominal Treasuries held to maturity** (individual notes/bonds, or iBonds term ETFs) | Exact match for fixed-dollar payments; no credit risk; no forced selling | Needs one position per year; slight coupon/timing mismatch |
| **TIPS** (inflation-linked Treasuries) | Protects real value | **Mismatch:** the payments are *not* inflation-adjusted, so TIPS add inflation risk to the funding. If inflation turns out lower than the ~2.5% breakeven, TIPS pay less than the nominal bonds would have. |
| **Bond fund** (e.g., intermediate Treasury index) | Simple, one ticker | Never matures, so its value at payment dates is uncertain. It matches the payments only on average (duration), not exactly. |
| **Investment-grade corporates** | Extra yield ("carry"; Cambridge Associates) | Default and downgrade risk conflicts with the certainty mandate |

## Evidence
- **Cost of the promise:**
  - At the start of 2033: $500k at 0%, $439k at 3%, $413k at 4.5%, $403k at 5.15%.
  - At the start of 2027 (Strategy A): **$298k** at 5.15%, $333k at 4.0%.
- **Modelled 2033 reserve value** (market value of the ladder = cost of the promise), base case: p10 $383k, **p50 $413k**, p90 $446k. Under A this value doesn't matter for funding, because the ladder and the promise move together.
- **Instruments available now:**
  - iShares iBonds term Treasury ETFs mature and pay out their NAV in the named year; expense ratio 0.07%. The range includes **IBTM (Dec 2032), IBTO (Dec 2033), IBTP (Dec 2034), IBTQ (Dec 2035) and IBTR (Dec 2036)**. A fund maturing in December funds the *January* payment that follows: IBTM → 2033, IBTO → 2034, IBTP → 2035, IBTQ → 2036, IBTR → 2037.
  - Individual Treasury notes/bonds exist for every maturity year to 2042. The later years are covered by older 20- and 30-year bonds.
  - STRIPS are listed as *prohibited in WInS* on an unofficial rules page (unverified). That limits only the WInS demonstration, not Laura's real portfolio.
- **Cost of using ETFs:** 0.07% a year on an average balance of ~$300k is about $210 a year, or roughly $2k over the life of the ladder. That is negligible.

## Debate
- **Advocate (nominal Treasuries):** The liability is fixed dollars, so the matching asset is fixed-dollar Treasuries. Textbook cash-flow matching.
- **Opponent (add TIPS):** Inflation will erode the residency's purchasing power; Laura should hedge that.
- **Advocate:** That is a real concern for the *residency's budget*, but the case fixes payments at $50k nominal. TIPS would make funding the *stated* promise less certain. Inflation risk to the residency belongs in the facility and flexibility discussion (D5), not in the reserve.
- **Judge:** Nominal Treasuries. Mention TIPS as considered and rejected, with the reason. This shows judgement.

## Decision
1. **Composition:** a ladder of US Treasuries, one "rung" per payment. Each rung has about $50k face value and matures in Nov/Dec before the January it pays.
   - **Payments 2033–2037:** iBonds Treasury ETFs IBTM, IBTO, IBTP, IBTQ, IBTR (Dec 2032 → Dec 2036). This is simple, and one ticker per year is easy for Laura to follow.
   - **Payments 2038–2042:** individual Treasury notes/bonds maturing Nov 2037 – Nov 2041. Switch to iBonds if BlackRock launches matching years (the team should verify launch plans; do not assume).
2. **Size:** ≈ $298k to buy in Jan 2027 at today's yields. Its value in 2033 is whatever the market says (median ≈ $413k), which is by construction exactly the cost of the remaining payments.
3. **How it changes 2033–2042:** *it doesn't need managing.*
   - Each January, the rung that matured in the previous Nov/Dec pays $50k.
   - Between maturity and the payment date, the cash sits in T-bills or a money-market fund.
   - Coupons received are either used to reduce the face value bought for the shortest rungs, or held in T-bills and applied to the next payment.
   - The ladder's value falls from ~$413k (2033) to $50k (start of 2042) as rungs are used (see the run-off table).
   - No selling, no rebalancing, no market timing.
4. **What it will not hold:** equities, corporate credit, TIPS, or bond funds.

## What would change our mind
- WInS or the final report rules require a specific instrument set.
- The case clarifies that payments are inflation-linked. In that case, switch to TIPS for the same structure.

## Plain English for Laura
Your reserve is ten US government bonds (or bond funds that act like single bonds), each maturing just before one $50k payment is due. Every January one of them pays out, and nobody has to make any investment decisions for the residency's running costs for ten years. We chose regular Treasuries over inflation-protected ones because your $50k payments are fixed in dollars, so fixed-dollar bonds match them exactly.

**Sources:**
- [iShares: Build better bond ladders with iBonds](https://www.ishares.com/us/strategies/bond-etfs/build-better-bond-ladders)
- [IBTM (Dec 2032), stockanalysis.com: 0.07% expense ratio](https://stockanalysis.com/etf/ibtm/)
- [IBTR (Dec 2036)](https://www.ishares.com/us/products/350028/ishares-ibonds-dec-2036-term-treasury-etf)
- [Cambridge Associates: Liability hedging portfolio](https://www.cambridgeassociates.com/insight/liability-hedging-portfolio/)
- [US Treasury real yield curve (TIPS 10Y 2.63%)](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value_month=202609)

> ⚠ **Team check:** the ticker-to-year mapping comes from iShares product pages found on 25 Sep 2026 (IBTM, IBTO, IBTP, IBTQ, IBTR). Re-confirm on ishares.com and check the WInS approved list before trading.
