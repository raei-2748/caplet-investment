# Proposed register section 8y (Tue 24 Nov 2026, numbers owner's analysis worker)

Notes and figures for the numbers owner to place in `keel/final_report/NUMBERS.md` after 8x. Not report prose.
NUMBERS.md itself is not edited here. Script `numbers/statement_value.py`; results
`numbers/results_statement_value_2026-11-24.json`.

---

### 8y. What a statement shows co-sponsors in 2031 and 2032 (Tue 24 Nov 2026, numbers owner's analysis worker; three readers playing funders, 24 Nov; `numbers/statement_value.py`, `numbers/results_statement_value_2026-11-24.json`). MODEL; Keel arithmetic where marked

- **Why.** Three readers playing funders (a Taiwanese company's head of giving, a US foundation programme officer and
  a Taiwan Ministry of Culture grants officer) said three things. Co-sponsors will be shown a broker statement at the
  2031 meetings and again before the December 2032 payout. A bond fund two years from its end shows a market value
  below what it will pay out, so the statement could show less than the $115,000 Laura signs for, and no one would be
  there to say why. And a single IBTM line mixes the 2033 payment's lot with the building's lots. This block works out
  what the statement shows. It adds new figures only; no existing figure moves.
- **Script and rerun:** run `python3 -I keel/final_report/numbers/statement_value.py` from the repo root (about 10
  seconds). It imports engine, plan and completion and changes none of them. It reads no results file and writes only
  `results_statement_value_2026-11-24.json`. It asserts every register figure it uses:
  - floor money $81,244 and moved money $18,349;
  - the floor's payout $102,365, the moved half's $20,138, and $122,503 for the two together;
  - the zero-interest values $98,096 and $117,731;
  - the unrounded ends $97,605 and $117,142, and the stated $95,000 and $115,000.

  It also reproduces these to the dollar:
  - 8w's lot values on 1 Jan 2031, 1 Jan 2032 and 30 Nov 2032, with its short-term Treasury ETF balances;
  - Exhibit 3's two yield rows ($80,000 to $100,000, paying $103,940; $110,000 to $130,000, paying $142,858);
  - section 4's top on 3.50% coupons ($117,449).

  Every assert passes.
- **Basis.** The basis is 8w's:
  - the forward rates of the 6 Nov 2026 curve;
  - VT on the central 7.5% path;
  - the escrow standard and Keel's reading of "most";
  - the move modelled on 1 Jan 2031 (the trade on Thu 2 Jan 2031).

  The terms below mean:
  - **Each IBTM lot** is valued at net asset value, as a statement shows it. That is the number of units (the money
    put in divided by that day's net asset value) times the holdings' remaining flows on the date's forward rates,
    less the 0.07% fee charged so far.
  - **A distribution the fund has already paid** waits in the short-term Treasury ETF, grown at forward rates. That
    ETF is a separate statement line, shared with every other dollar that is waiting.
  - **"The building's money on the statement"** is the two IBTM lots plus the distributions they have paid.
  - **"The count"** is what the holdings still to pay, plus the distributions already paid, hand over by 15 Dec 2032 if
    nothing earns interest from that date, after the fund's fee and the ETF's 0.15%. It is the range rule's own count,
    done again on the statement date. On each trade day it equals the rule's value (asserted).

  The exchange price is not modelled. On normal days IBTM traded 0.06% to 0.09% above net asset value (section 0).

**A. The statement on the central path**

| Statement date | The building's two IBTM lots (floor + moved), market value | Their distributions already paid, in the short-term Treasury ETF | **The building's money on the statement** | Against $115,000 | **The count** (zero interest from that date) | The 2033 payment's own IBTM lot | One IBTM line (all three lots) |
|---|---|---|---|---|---|---|---|
| Thu 2 Jan 2031 (the move) | $100,413 | $11,237 | **$111,651** | $3,349 under | **$118,644** | $38,278 | $138,691 |
| Tue 1 Jul 2031 | $100,571 | $13,657 | **$114,227** | $773 under | **$118,965** | $38,338 | $138,909 |
| Sat 3 Jan 2032 | $100,848 | $16,150 | **$116,998** | $1,998 over | **$119,363** | $38,444 | $139,291 |
| Thu 1 Jul 2032 | $101,124 | $18,703 | **$119,827** | $4,827 over | **$119,823** | $38,549 | $139,673 |
| Wed 1 Dec 2032 | $103,214 | $19,096 | **$122,310** | $7,310 over | **$122,306** | $39,357 | $142,572 |
| Wed 15 Dec 2032, the fund's end | paid out | | **$122,542** | $7,542 over | | paid out | |

- **What the building's lots pay at the end.** By this method they pay $122,542. That is $39 above section 4's
  $122,503, because plan.run charges the fund's fee on distributions after they have left the fund (8w's wedge). With
  the ETF's 0.15% charged on the waiting distributions, they pay $122,459 (section 3's no-exit figure). The top was
  set on a count of $117,731 at zero interest from each trade day: less 0.5%, that is $117,142, stated as $115,000.
- **The first date at or above $115,000, staying there (checked daily):**
  - the building's money on the statement: **Sat 23 Aug 2031** (so the first statement to show it is Mon 25 Aug);
  - the two IBTM lots alone: **never**. They reach at most $103,410, at the end;
  - the count: every day from the move. It is at least $118,644 and never under $117,731;
  - one IBTM line: every day from the move (at least $135,815 before the end). But that line is not the building's
    money (part C).
- **The 2033 payment's lot pays its own promise:** $50,000 on 1 Jan 2033 at today's forward rates, or $47,338 at zero
  interest, with the extra Treasuries paying the other $2,662 (8h). Its distributions already paid ($7,157 on
  2 Jan 2031, $10,431 on 1 Dec 2032) also wait in the short-term Treasury ETF.
- Keel arithmetic: the building's paid distributions make up 14.4% (2 Jan 2031) to 16.4% (1 Jul 2032) of the
  short-term Treasury ETF line ($78,257 and $114,382 on those dates).

**B. The Treasuries behind the building's lots: face value and the coupons still to come**

| Holdings | Face (floor lot + moved lot) | Coupons still to come, gross: 2 Jan 2031 / 1 Jul 2031 / 3 Jan 2032 / 1 Jul 2032 / 1 Dec 2032 | Count on the trade days |
|---|---|---|---|
| The engine's stand-in, which the rule uses (one bond, 4.2513%, maturing 4 Jul 2032) | $99,333 ($81,211 + $18,123) | $8,446 / $6,334 / $4,223 / $2,111 / $0 (after the fund's fee: $8,427 / $6,319 / $4,212 / $2,106 / $0) | $117,731 |
| IBTM's real 3.50% average coupon (a variant) | $102,443 ($84,057 + $18,386) | $7,171 / $5,378 / $3,586 / $1,793 / $0 | $118,039 |

- Keel arithmetic for 2 Jan 2031. The face of $99,333, plus $8,446 of coupons to come, plus $11,237 of distributions
  already paid, comes to $119,016 before the fees still to come. After the fund's fee and the ETF's 0.15% to
  15 Dec 2032, that is the count of $118,644. The market value of $111,651 is the same Treasuries priced today.
- On the 3.50% variant the IBTM lots show more ($102,073 on 2 Jan 2031, $106,053 on 1 Dec 2032), because less is
  paid out along the way. They are still under $115,000.

**C. One IBTM line, read whole.** On 2 Jan 2031 the single IBTM line shows $138,691: the building's two lots
($100,413) plus the 2033 payment's lot ($38,278). It does not include the $11,237 the building's lots have already
paid out. Read as the building's money, it is $27,041 too high on 2 Jan 2031 and $20,262 too high on 1 Dec 2032 (Keel
arithmetic). So the line is wrong in both directions: it includes money that is not the building's, and leaves out
money that is.

**D. Yields: the 1-in-20 worlds of January 2028 (Exhibit 3), and a 1-point rise during 2031**

| World | Stated range | Building lots / building money, 2 Jan 2031 | Building lots / building money, 1 Dec 2032 | Building money reaches the world's own top | Building money reaches $115,000 | Count, at least |
|---|---|---|---|---|---|---|
| Central | $95,000 to $115,000 | $100,413 / $111,651 | $103,214 / $122,310 | Sat 23 Aug 2031 | Sat 23 Aug 2031 | $118,644 |
| Yields 1-in-20 low in January 2028 (1.59 points under today's forward rates; "most" binds, floor $75,001) | $80,000 to $100,000 | $88,264 / $97,718 | $88,093 / $103,838 | Mon 6 Oct 2031 | never (the lots pay $103,940) | $101,726 |
| Yields 1-in-20 high in January 2028 (1.59 points over) | $110,000 to $130,000 | $112,833 / $126,224 | $119,445 / $142,549 | Wed 25 Jun 2031 | from the move | $136,878 |

- **In every world the IBTM lots alone stay under that world's own stated top to the end.** Their peaks are $88,271
  (low), $103,410 (central) and $119,744 (high). On the move day the building's money on the statement is 2% to 3%
  under the world's top: $2,282 under $100,000 (low), $3,349 under $115,000 (central) and $3,776 under $130,000
  (high), by Keel arithmetic. That gap closes between late June and early October 2031. In the low-yield world the
  lots drift down as they near maturity ($88,264 to $86,885 by 1 Jul 2032), because their 4.25% coupon is above that
  world's rates. The money including the distributions still rises.
- **A 1-point rise all at once.** Here the short-term Treasury ETF is taken as not moving, since its bills mature
  within three months. The building's two lots fall by:
  - $1,436 (1.4%) on 2 Jan 2031;
  - $980 on 1 Jul 2031;
  - $494 on 3 Jan 2032;
  - $8 on 1 Jul 2032;
  - $0 on 1 Dec 2032, because the engine's holdings mature on 4 Jul 2032.

  A 1-point fall adds about as much ($1,458 down to $0). The 2033 payment's lot moves by $706 down to $15.
- **A 1-point rise held for good from the day after the move (2 Jan 2031).** The statement then shows:
  - $110,214 that day, against $111,651 centrally;
  - $113,315 on 1 Jul 2031, against $114,227.

  It passes $115,000 about Sun 5 Oct 2031 rather than 23 Aug. At the end the lots pay $123,351, which is $809 more,
  because the waiting money earns more. If the rise comes on 1 Jul 2031 instead, the statement shows $113,248 that
  day, passes $115,000 about Thu 9 Oct 2031, and the lots pay $123,277 at the end. The count does not fall: it is
  $118,644 on 2 Jan 2031 either way, and higher than the central path's from then on. The stated range does not move.

**What it shows**
- **A statement on the day of the move shows the building's money at about $111,700.** That is about $3,300 under
  the $115,000 she signs for. Nothing has been lost. A Treasury fund's market value is its remaining payments priced
  today, and it climbs to its payout as the fund's end nears. Centrally, the building's money passes $115,000 in late
  August 2031 and reaches about $122,300 by 1 Dec 2032. In both yield worlds the gap on the move day is also a few
  thousand dollars, closed between late June and early October 2031.
- **The IBTM lots alone never show $115,000; they reach at most about $103,400.** By December 2032 about $19,100,
  which is 16% of the building's money, has been paid out by the fund as distributions. It sits in the short-term
  Treasury ETF line, beside the payments' waiting money.
- **One IBTM line errs the other way.** It shows about $138,700 at the 2031 meetings, because it also holds the 2033
  payment's lot. Read whole, it overstates the building's money by $20,000 to $27,000.
- **Yields move the statement, not the count.** A 1-point rise the day after the move takes about $1,400 off the
  statement. The effect gets smaller each month after that, and is nothing after July 2032 on the engine's holdings.
  What the holdings hand over at zero interest does not move, and at market rates the payout goes up.

**What a co-sponsor should be shown beside the market value** (notes for the lead and the exhibits owner; not report prose)
1. **The building's money as its own figure, never the IBTM line.** That means the two lots by purchase date (a
   broker's lot detail lists each purchase with its date and cost) and the distributions they have paid.
   - Keel's suggestion, an execution choice the IPS does not touch: hold the two lots and their distributions in a
     second account at the same broker. Then one statement covers the building alone, and the 2033 payment's lot
     stays with the other nine payments.
   - In January 2028 the 2033 payment's IBTM tail ($2,286) and the floor ($81,244) are bought in the same month.
     Placing them as two orders keeps the lots apart.
2. **The count on the statement date, worked out from the fund's published holdings.** This is what these
   Treasuries, and the distributions they have already paid, hand over by mid-December 2032 if they earn nothing more
   from that day.
   - It is $118,644 on the day of the move and $122,306 by 1 Dec 2032, and never under the $117,731 the top was set on.
   - Show it with the face value of the Treasuries behind it ($99,333 on the engine's holdings, about $102,400 on
     IBTM's real coupons), the coupons still to come and the cash already paid.
   - A co-sponsor can check it against iShares' daily holdings list and her share count, without having to trust a
     forecast.
3. **One fact on why the market value is lower:** a Treasury fund's market value is what its remaining payments are
   worth today, and it rises to its payout as the fund's end nears. Beside it, give the expected statement on later
   dates at today's forward rates (the monthly series in the results file), so that the December 2032 statement
   matches what was said in 2031.
4. **The end date, and what moves each figure.** The fund ends on or about 15 Dec 2032. A rise in rates lowers the
   statement for a while but does not lower the count. An early end of the fund is the one event that would lower the
   count (section 3; 8w part C).
- **Words.** Never say "secured", "escrow" or "guaranteed" about the fund's payout. "Certain" stays the stated range's
  word and is never used for a statement figure. Never present a statement figure as a promise; say "on the central
  path". In report words, never write "the fund" alone (8w's words note; WORDS' rows for the floor and the moved
  shares).

**Limits.**
- The figures cover the central path and the two yield worlds of Exhibit 3 only, where yields move once, in January
  2028. The 1-point rise is the one stated above.
- The engine's IBTM is one bond that pays twice a year and matures on 4 Jul 2032. The real fund pays monthly and held
  notes maturing as late as 30 Nov 2032 (card Q93 row 13, iShares holdings as of 24 Sep 2026). So the real IBTM line
  falls a little each month rather than in half-year steps, and a yield move in the second half of 2032 still moves it
  slightly. The building's money (the lots plus their paid distributions) is the same either way.
- Waiting money is grown at forward rates without the ETF's 0.15% (as in 8t and 8w). With that fee charged, the
  building's money is lower by at most $83 by 15 Dec 2032.
- The exchange price can sit above or below net asset value: 0.06% to 0.09% above on normal days, and more than 1% off
  in March 2020 (section 0).
- 3 Jan 2032 is a Saturday, so a statement that day carries the close of Fri 2 Jan 2032 (under $20 different).
- Two of the daily first dates fall on weekends. The next trading day's statement is the first to show them.
- Every figure assumes the fund runs to its stated end. Section 3 and 8w part C cover an early end, a merger or a moved
  end.
