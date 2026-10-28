# W-01: the coupon gap is partly a choice of bond (Window, Wed 28 Oct 2026)

(Keel is a simulated team, AI-written.) Felix's primary-source find for round 1's question: is there a cure for the
coupon gap that is itself bought on its birthday? Numbers are MODEL; script `W-01_low_coupon_rungs.py`, results
`W-01_low_coupon_rungs_results.json`.

## The find (sources read Wed 28 Oct 2026)
- **TreasuryDirect auction results, 17 Feb 2021** (`https://www.treasurydirect.gov/instit/annceresult/press/preanre/2021/R_20210217_1.pdf`):
  "20-Year Bond", interest rate "1-7/8%", CUSIP 912810SW9, issued 1 Mar 2021, maturing **15 Feb 2041**.
- **TreasuryDirect auction results, 17 Nov 2021** (`.../2021/R_20211117_3.pdf`): "20-Year Bond", interest rate "2%",
  CUSIP 912810TC2, issued 30 Nov 2021, maturing **15 Nov 2041**.
- **1.375% bond of 15 Nov 2040**, CUSIP 912810ST6, issued 30 Nov 2020 (TradingView security page; secondary source,
  the TreasuryDirect result PDF did not surface in search).
- WInS book (`competition/wins/2026-10-23_snapshot.md`): the 2041 and 2042 cheques sit in the **4.25% Nov-2040** and
  **3.125% Nov-2041** bonds (old 30-year issues), yields 5.29% and 5.37% on 23 Oct.

So the same maturity exists twice: once with a fat coupon from 2010-11, once with a thin one from 2020-21. Ordinary
coupon Treasuries, not STRIPS and not TIPS, so they are allowed in Laura's plan **if WInS lists them** (UNVERIFIED;
Keel never opens WInS).

## What the bond choice does (MODEL: settle 1 Jan 2027, flat yield, coupons reinvested to maturity)
Each rung is sized to deliver $50,000 if coupons are reinvested at the purchase yield; both versions cost the same.
Then every coupon is reinvested 2 points lower for good.

| Cheque | Bond | Share of the $50k that arrives early as coupons | Short if coupons earn 2pt less for good |
|---|---|---|---|
| Jan 2041 | 4.25% Nov-2040 (held) | 46% | **$3,144** |
| Jan 2041 | 1.375% Nov-2040 | 22% | **$1,482** |
| Jan 2042 | 3.125% Nov-2041 (held) | 41% | **$3,019** |
| Jan 2042 | 2% Nov-2041 | 31% | **$2,270** |
| (scale) | a zero (STRIPS: banned) | 0% | $0 |

**So:** picking the thinnest coupon at purchase halves the 2041 rung's coupon gap and cuts the 2042 rung's by a
quarter, for no extra cost on the same yield. It is the one cure for the coupon gap that is bought on the day the
promise is made, which is what round 1 asked for. It is not a full cure: here only the 2041-42 cheques have a thin twin; the 2033-37 cheques sit in iBond
funds, where the choice doesn't arise, and the 2038-40 bonds have no 20-year twin of the same date. (The 1.875% Feb-2041 could also serve the 2042
cheque, at the price of eleven months' wait in cash, the same wait the locked Feb-2037 note already accepts.)

## Where it breaks (LS-04: the break is the finding)
1. **Listing.** The rule is "any Government/Treasury Bond available on WInS". If WInS lists only the fat issues, the
   rule is empty for Laura's plan and becomes a Final Report "what we'd do with a wider shelf".
2. **Price.** Low-coupon off-the-run 20-year bonds have traded a few basis points cheap or rich to the curve; same
   yield is an assumption. 5bp on a $24k rung of duration ~12 is about $150, small beside
   the $1.6k saved.
3. **Locked lines.** The TNA notes name the fat bonds as held. Saying "lowest coupon" in the IPS while the WInS book
   holds 4.25% invites a judge to ask why. Keel's call: FR, not IPS, unless the shelf check shows the thin issues.

## Lineage (for the Final Report, cited there)
Cash-flow dedication has always preferred low-coupon, deep-discount bonds for exactly this reason: less of the money
arrives early, so less is exposed to reinvestment (the standard dedication texts; to be read at source and cited in the FR, not yet checked by the Window).
The zero is the limit case, and Wharton has banned it, which makes the thin-coupon twin the nearest legal thing.
