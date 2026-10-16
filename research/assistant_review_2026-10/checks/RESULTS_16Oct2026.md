# Number checks for the TNA and IPS, 16 Oct 2026 (AI check, MODEL numbers, not submission text)

Treasury par curves from home.treasury.gov (`tsy_202610_new.csv`, downloaded 16 Oct; latest row 15 Oct 2026).
Scripts: `indep_pricer.py` (bootstrapped curve), `v5_figures_16oct.py`, `v5_floor_range_16oct.py`.

## 1. Ladder cost on 1 Jan 2027 vs the $300,000 deposit (for the IBTR reflection and the IPS)
| Curve | Zero basis ($50k at each holding's end date) | Room | Break-even fall | Coupon basis (income reinvested at own yield) |
|---|---|---|---|---|
| 6 Oct | $292,327 | $7,673 | 0.27 pts | $290,606 |
| 13 Oct | $294,336 | $5,664 | 0.20 pts | $292,469 |
| 14 Oct | $295,076 | $4,924 | 0.17 pts | |
| 15 Oct | $297,778 | $2,222 | **0.08 pts** | $295,828 |

The team's 6 Oct figure ($293,447, method not committed) sits about $1,100 above our zero basis. On that basis the
15 Oct cost is about $298,900, with roughly 0.04 points of room. **On any basis the room is now nearly gone.** A further
fall of about 0.05-0.1 points before January means the 2028 deposit tops up the ladder first, and the floor drops below
$150,000.

**IBTR pair (7 → 15 Oct):** the WInS Treasury holdings rose about **$4,200 (+1.5%)** (curve-based estimate, not WInS
quotes). Laura's real January purchase got about **$5,800 dearer** ($291,933 → $297,778).

## 2. Figures added to IPS Version 5 on 16 Oct
| V5 figure | Check | Verdict |
|---|---|---|
| "about $294,000 at mid-October" | True on 13 Oct only. $295-299k by 15 Oct, depending on basis | Out of date within two days. Date it or drop it |
| "yields fell two points for good → about $21,000 short" | $21,444-21,754 (6-15 Oct curves). At 0% reinvestment, about $50-52k short | **Reproduces** |
| "the rest, about $32,000, buys the branch" | $33,270 (15 Oct) to $34,021 (13 Oct). Floor cost in Jan 2028 about $116-117k at a 5.1-5.2% forward yield | Reproduces (rounded) |
| "about $145,000 to $168,000 today" | Bottom: the floor quoted rounded down. Top: $150,000 + half the fund = $167,746 (15 Oct), **but only if the 2027 leftover goes into the stock fund**, and only while no ladder top-up is needed | Conditional. It breaks if yields fall about 0.05-0.1 pts more |
| "lands inside the range about 99 times in 100" | 200,000 paths (7% compound, 16.8% vol, JPM AC World). Floor stressed for a permanent 2-point fall: **0.000% below $145,000**. The cap means the gift never goes above the top. The floor still delivers $146,855 if yields fall 4 points for good. The gift equals the top in about 60% of paths | Cautious. The 1% is a margin, not a named scenario. The model leaves out IBTM fees (0.07%) and how its final payout works |

## 3. iBond distributions near the 6 Nov freeze (WInS book)
- Saved iShares pages (`rab/data/ishares/`, 28 Sep) show monthly distributions, with ex-date on the first business day
  and payment about 3 business days later (ex 1 Sep / paid 4 Sep; ex 3 Aug / paid 6 Aug).
- If November follows the pattern (UNVERIFIED), the ex-date is about Mon 2 Nov and payment about Thu 5 Nov, inside the
  window.
- Estimated at September's rates, the payout is IBTM $342 + IBTO $86 + IBTP $81 + IBTQ $77 + IBTR $71 = **about $657**.
  Whether WInS credits ETF distributions is UNVERIFIED.
- Reinvesting "in the holding that paid it" would take 5 trades ($125, about 19% of the cash) and whole shares only.
  **Recommendation: no trade.** Give one reason in the Final Report.
- VT pays quarterly (no November payment). The T-bond coupons fall on 15 Nov or in Feb/Aug, which is after the freeze
  or outside the window.

## 4. The 6 Oct email's arrival time (for IBTM, gate G3)
Not found in the Gmail account connected to this session (searched 4-9 Oct). It probably went to a school account or
was posted on the WInS dashboard. Still UNVERIFIED.
