# Bond desk re-read 2: Table 3, the 2031 range rule and the "inked" definition (Sat 14 Nov 2026, Sydney evening)

Fixed-income reader, blind to earlier readers. Notes, not prose.

Read in the repo: the case (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`); the IPS as submitted;
`exhibits/tables.md` (Table 2, Table 3 and its note, Figure 1's note and cash dates); `SKELETON.md` rows 3c and 3e
(density cut and section 3) and "The conceit"; `CONCEIT.md` sections 2, 3, 5 (bleed row), 5b rank 3, 7 guard 5, 8;
`NUMBERS.md` sections 0, 3, 4, 5, 8h (cash dates, spare), 8i, 8j. To check a basis only: cards Q36 and Q2b.
Nothing under `research/panel/` was opened. Every plan figure below is the register's (MODEL); "Keel arithmetic" marks
my own sums on register figures.

## Checked at source (all read Sat 14 Nov 2026)

| What | Source | Finding |
|---|---|---|
| IBTM terms: index window 1 Jan to 15 Dec 2032; ends "on or about December 15, 2032"; "does not seek to return any predetermined amount"; board may extend the end with no shareholder vote; in the last six months proceeds "may also be invested in other cash and cash equivalents", including BlackRock money market funds; "By December 15, 2032, the Fund is expected to consist almost entirely of cash"; may lend up to one-third of assets; securities lending can lose money | IBTM summary prospectus, 27 Feb 2026: https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf | VERIFIED |
| Unitary fee 0.07%; BFA pays all operating expenses except the management fee, interest, taxes, trading costs, distribution fees, litigation and extraordinary expenses; BFA waives money-market fees through the end, a waiver that can end by written agreement of the Trust and BFA | Same summary prospectus, fee table and footnotes | VERIFIED |
| Index rules: market-value weighted; rebalanced on the last calendar day of each month; new issues added once settled; cash from bond payments reinvested in the remaining bonds at month end | Same summary prospectus, "Principal Investment Strategies"; ICE Bond Index Methodologies: https://www.ice.com/publicdocs/data/Bond_Index_Methodologies.pdf (rebalancing paragraph, search excerpt) | VERIFIED (ICE page from excerpt only) |
| The October notice and the cash date: supplement dated 15 Oct 2026 for IBTG: last trade Tue 15 Dec 2026, trading halted 16 Dec, proceeds "on or about December 18, 2026, subject to their brokerage firm's processes"; final NAV "will include any costs associated with the liquidation" | https://www.ishares.com/gls-download/literature/prospectus/p-ishares-trust-us-treasury-ibonds-non-ibonds-10-31.pdf (supplement on its first pages) | VERIFIED (2026 only; earlier Octobers not re-read) |
| No duty to give an ending notice: funds distribute "without further notice" after the end | IBTM page and fact sheet risk text: https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf ; https://www.ishares.com/us/literature/fact-sheet/ibtm-ishares-ibonds-dec-2032-term-treasury-etf-fund-fact-sheet-en-us.pdf | VERIFIED |
| IBTM trading cost: 30-day median bid-ask 0.05%, premium 0.09% (6 Nov 2026); net assets $639m (9 Nov 2026) | https://www.blackrock.com/us/individual/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (search excerpt) | VERIFIED (excerpt) |
| Treasury pays on the next business day when a payment date is "a Saturday, Sunday, or other day on which the Federal Reserve System is not open for business", without extra interest | 31 CFR 356.30(a): https://www.ecfr.gov/current/title-31/part-356/section-356.30 | VERIFIED |
| Fed calendar: a Saturday holiday leaves Reserve Banks open the Friday before; a Sunday holiday closes the Monday after | Federal Reserve Board K.8: https://www.federalreserve.gov/aboutthefed/k8.htm ; https://www.frbservices.org/about/holiday-schedules | VERIFIED (published to 2030; later years on the same rule) |
| A fund's advisory contract must be approved by a majority of the fund's shares and "precisely describes all compensation" | 15 U.S.C. 80a-15(a): https://www.law.cornell.edu/uscode/text/15/80a-15 | VERIFIED (so the 0.07% fee cannot rise on notice alone; costs outside the unitary fee can) |
| U.S. Treasury bill yields have gone below zero for days: Dec 2008 (3-month -0.01%), 2015, March 2020 (3-month -0.036% on 25 Mar) | https://www.cnbc.com/2020/03/25/negative-rates-come-to-the-us-1-month-and-3-month-treasury-bill-yields-are-now-negative.html ; Treasury TBAC, May 2020: https://home.treasury.gov/system/files/221/TBACCharge1Q22020.pdf ; https://www.latimes.com/archives/la-xpm-2008-dec-10-fi-treasury10-story.html | VERIFIED |

Calendar arithmetic (Python on the K.8 rule): every cash date in Figure 1 is a business day on the weekday printed;
slack from cash to the last Fed business day of the year is IBTM 7-9, IBTO 5-8, IBTP 4-8, IBTQ 4-6, IBTR 6-8 business
days, so "4 to 9 (4 to 6 for 2036)" is right; the Feb-2037 bond pays Tue 17 Feb (15 Feb is a Sunday, 16 Feb Presidents'
Day) and the May-2038 bond Mon 17 May (15 May is a Saturday); trade days Mon 4 Jan 2027 and Mon 3 Jan 2028; the first
business day of 2031 is Thu 2 Jan. A 31 December note pays on 31 Dec in 2032, 2035 and 2036, but on Tue 3 Jan 2034 and
Tue 2 Jan 2035 (31 Dec on a weekend, 1 Jan or 2 Jan observed).

UNVERIFIED: which Treasury-bill ETF holds the waiting money and its fee (NUMBERS 0 says so too); whether past iBond
endings carried any liquidation cost in the final NAV (none sized at source).

## Claim 1. Table 3 is what a bond desk would run: KEEP, with changes

The structure is right: two reasons, a carry-on level, one trigger per cell, "never" per row, business-day-adjusted
due dates, a numeric slack. Every figure I tested matches the register. The fixes are scope and wording.

**Row 1, the 2028 deposit.** Figures check ($2,388 + $35,894 = $38,282; 2033 payment $3,016 short at forward rates,
NUMBERS 5). Change: $38,282 is a today's-rates figure (house 1-in-20 $33,884 to $54,679, NUMBERS 4); unlabelled in a
"carry on while" cell, a different January 2028 figure reads as a breach. Fix: "its first part to the payments (about
$38,000 at today's rates)". Optional, for a desk the larger change: a missed deposit also leaves the ten $57,455 short if
cash waiting earns nothing (NUMBERS 5); one clause in the Changes cell or the note.

**Row 2, Treasury payments.** "Paid when due, or the next business day after a holiday": the rule covers weekends too
(31 CFR 356.30(a)), and two of the five bonds land on weekends. Fix: "after a weekend or holiday". Five business days:
keep (a stated convention, with the delay inside it logged under row 3).

**Row 3, X-date.** Keep. The prospectus says each fund is "almost entirely" cash by 15 December, so the December payouts
are exactly where a debt-limit delay would bite; watching cash dates is the right test. No sale ahead of it: keep (a sale
on a political signal would be a third reason).

**Row 4, iBond fund notices.** Board powers check (extension by board majority, no vote; prospectus). Six changes:
1. "the floor's from its 0.5% margin": the moved half also goes into the late-2032 fund (NUMBERS 0, range rule: "the
   money put into the late-2032 fund" for both ends). IBTM carries three lots: the 2033 payment, the bottom and the top.
   Fix: "the range's from its 0.5% margin", and the 0.5% is one budget shared with every other fund cost, not a second
   margin.
2. "the swap bought with the fund's own cash" fits an early end (cash at NAV a few days after the last trade, per the
   15 Oct 2026 notice), not an extension or a merger, where the fund's shares must be sold on the exchange. Fix: "its
   money (paid out, or its shares sold) buys ...". Cost of a sale today: about 0.05% to 0.1% (spread 0.05%, premium
   0.09%), inside the 0.5%.
3. "a Treasury maturing just before it's needed": a month-end note can pay after 1 January (31 Dec 2033 pays Tue 3 Jan
   2034; 31 Dec 2034 pays Tue 2 Jan 2035). Fix: "a Treasury maturing by 15 December", which also keeps the row's
   business-day slack true.
4. "any gap from the extra Treasuries": they have about $45,500 to spare at today's rates (1 Jan 2033 money) but $0 if
   cash waiting earns nothing and pays the bill fund's 0.15% (NUMBERS 8h). A gap paid there leaves the no-interest test
   short by that gap. Fix: add "then re-tested at no interest" (SKELETON already says it; the cell or the note does not).
5. A missing October notice: the October notice is practice, not a duty ("without further notice", fund page). Silence
   is a reason to read the fund page and filings, not to swap. Fix: the Changes cell applies to an early end, a merger
   or a later end only; for silence, "check the fund page and filings".
6. The waiting money's fund is watched nowhere. Every coupon and fund payout waits in a Treasury-bill ETF whose 0.15% fee
   is exactly what the no-interest test can bear, yet `CONCEIT.md` section 8 says "Table 3 watches each", listing "a fee
   on waiting money above the modelled 0.15%". Fix: row 4's signal "iBond and Treasury-bill fund notices", with "its fee
   above 0.15%" as a trigger; or strike that item from section 8's sentence.
Also: "(4 to 6 for 2036)" reads as the December 2036 fund (IBTR, 6-8); it means the 2036 payment (IBTQ, cash December
2035). Fix: "(4 to 6 for the 2036 payment)".

**Row 5, trades.** "Limit orders near each fund's value": the January 2027 purchase also buys five bonds. Fix: "near each
holding's value (a fund's net asset value, a bond's quoted price)". Bigger: the 2031 move has no fixed day ("before the
2031 meetings"; the model uses 1 Jan 2031). An open date is a timing option, and after a fall in late 2030 the pull is to
wait, which is the market call IPS l.17 rules out. Desks fix rebalance dates in advance. Fix: name the day now (the first
trading day of 2031, Thu 2 Jan 2031, as modelled), moved only by a halt.

**Row 6, yields and share prices.** "1 percentage point lower before 2027: an $85,000 bottom" and the note's 3.60 points
check (NUMBERS 5). Clarity clash: Table 2's "Rates 3 points lower for good" gives an $80,000 bottom, so a reader sees 1
point cost $10,000 and 3 points $15,000. They differ in timing (Table 2's fall starts January 2027, after the ten are
bought, NUMBERS 8i; Table 3's comes before). Fix: label both ("from January 2027" in Table 2's row; "before 4 January
2027" in Table 3). Optional: "a Treasury's price on a statement" is not a signal (IBTM's price will move every day to
2032).

**Row 7, flexibility.** "$11,500 more on $115,000" is right only on NUMBERS 8d/8j's convention (10% more US dollars for
the same NT$ budget, NT$32.768 to about 29.79). Printed beside "NT$32.768 per US$1", a desk reads 10% stronger as
NT$29.49 and gets $12,778 (Keel arithmetic). Fix: say the convention ("needs 10% more US dollars than in 2031") or put it
in the note. "anything above the top ($29,800)" mislabels a sum: $29,800 is the half kept ($21,347) plus the excess
($8,476). Fix: "a call on her flexibility (about $29,800 with the excess, January 2033, today's rates)".

**Cash dates and slack.** All verified (above). Keep.

## Claim 2. The "inked" definition (CONCEIT section 7, guard 5): CHANGE

What holds: Treasuries pay fixed dollars on fixed dates, the fund's end payout follows its holdings, and "dollars on
dates only, never values" is the most important line in the guard (a Treasury's price, and IBTM's, moves daily). The
inking dates are right. What breaks:

1. **"the funds' running costs within 0.5%" names the one cost already counted.** The 0.07% fee is inside the engine's
   payout (NUMBERS 0, range-rule holdings; NUMBERS 3). The 0.5% covers costs outside the unitary fee: trading costs on the
   index's monthly rebalancing, litigation and extraordinary expenses, securities-lending losses, liquidation costs inside
   the final NAV, money-market fees if BFA's waiver ends, a premium paid at purchase. Fix: "other fund costs beyond the
   stated 0.07% fee, up to 0.5% of value, once". Side note for the numbers owner: NUMBERS 0's "an expense change made with
   notice" is loose; raising the 0.07% needs a shareholder vote (15 U.S.C. 80a-15(a)); costs outside it need none.
2. **"for the top" misses the bottom before the move.** From January 2028 to the 2031 move the bottom rests on the floor
   alone, with the same 0.5% plus rounding (central margin about $4,200, 4.3%, Keel arithmetic); at 0.75% costs the bottom
   alone is short in 5.0% of house paths, by up to $339 (NUMBERS 3). After the move both funds stand behind it. Fix: the
   0.5% condition applies to either end before the move and to the top after it.
3. **"For an iBonds fund ... less 0.5%" is wrong for five of the six iBond lots.** IBTM's 2033 lot and IBTO to IBTR carry
   no 0.5% cut: Figure 1 counts them at their no-interest payout after the 0.07% fee, and the extra Treasuries meet the
   test with $0 to spare after the bill fund's 0.15% (NUMBERS 8h). Fix: restrict the sentence to the late-2032 fund's
   range lots. For the payments the condition is "at the funds' stated fees and the bill fund's 0.15%", and the room for
   any other fund cost is the interest itself (about $45,500 at today's rates), none at zero.
4. **"owned in Treasuries" in a fund's last months.** The prospectus allows cash and money market funds in the last six
   months and lending of up to a third of assets. "Barring a US default" is the right headline, but literally the
   exceptions in those months also include a money fund or a lending loss, which the 0.5% covers for the range and
   nothing covers for the payment lots at zero interest. Fix: no change to the headline; 3e's planned line that the funds
   pay net asset value carries it once.
5. **"even if cash waiting earns nothing" is a margin, not a floor.** Bill yields have gone below zero for days (2008,
   2015, March 2020). The cost would be tiny, but with $0 spare it is technically a miss. Fix: never call zero the worst
   case (SKELETON 3e already says "margins, not forecasts"; keep it).
6. **Early end, merger, extension.** Ink survives only if the cash buys a Treasury the day it arrives (an early payout is
   short of the end payout by the interest still to come). Section 8 lists this; the definition should point to it in
   one clause: "and any fund event swapped as Table 3 row 4 says".

Elements the corrected guard 5 must carry (notes, for the writers to word): a dollar figure on a date; owned in
Treasuries directly or through iBonds funds; paid even if cash waiting earns nothing, with each fund at its stated fee
and the bill fund at 0.15%; barring a US default; for the range only, 0.5% of value held back once for other fund costs
(either end before the move, the top after it); any fund event swapped; never a value.

## Claim 3. Trim line, bleed and safe area (CONCEIT 5b rank 3): CHANGE

1. **Trim line = the stated top: exact.** The contribution is the lower of what the funds pay and the top, and equals
   the top in every house path, history window and replay (NUMBERS 4, 8i).
2. **"the funds pay past it (about $8,500 centrally)" sizes the bleed with pencil.** The $8,476 is a today's-rates
   figure. Central split (Keel arithmetic on NUMBERS 3-4): about $4,400 is interest that exists only if waiting cash earns
   it; about $3,400 is rounding down to $5,000 (anything from $0 to $4,999 by path); about $600 is the 0.5% cut. A bleed is
   a fixed allowance sized against a known error; here that is the 0.5% alone. Owned at zero interest, the overhang is
   about $4,000 centrally and as little as about $500 (smallest no-interest margin over the top across 585 replays $532,
   NUMBERS 8i). Fix: the bleed is the 0.5% the rule holds back (plus whatever rounding adds); the $8,500 is what today's
   rates add on top, and joins her flexibility.
3. **Safe area = the bottom: exact after the move only.** After it, both funds would have to lose about a fifth (20%,
   Keel arithmetic) to reach it. Before it, the floor alone holds the bottom on its own 0.5% plus rounding (claim 2,
   point 2). Since nothing is stated before the move, the image is true when used; date it "once the half has moved".
4. **"the 0.5% cut covers fund costs up to 0.5%": change** to costs beyond the 0.07% fee, once, of value; and it is the
   same 0.5% a Table 3 row 4 swap would draw on. "About 1 in 17 by a few hundred dollars" at 0.75% checks (6.0%, at most
   $429, NUMBERS 3).
5. **"a US default is a mis-cut no bleed covers": kill.** A mis-cut is a large version of the error a bleed is for, and a
   wider bleed would cover it. A default is a different kind of event: every margin here (the 0.5%, the rounding, the
   extra Treasuries) is held in the same Treasuries, so a default takes the figure and its margin together. CONCEIT 8
   already has the right picture ("it is the paper"). Fix: use that, or name the default plainly with no image.

Related, in SKELETON 3c (density cut row): "against a fee of 0.07% a year today" invites a reader to compute 0.07% x 5
years = 0.35% and think the 0.5% is mostly used. Fix: "beyond their 0.07% yearly fee, which is already counted". And "each
from what those Treasury funds will pay, rounded down" drops the basis. Fix: "what they pay if cash waiting earns nothing,
less 0.5%, rounded down to $5,000" (as SKELETON section 3's row 3c already has it).

## Scores

| Item | Precision (1-5) | Clarity (1-5) | Why |
|---|---|---|---|
| Table 3 | 4 | 3 | Every figure and date checks; the swap's maturity, the waiting fund, the shared IBTM lots and the open 2031 date are gaps; rows 6-7 need their conventions |
| 3c range rule | 4 | 3 | Rule, cap and confidence check against the register; "0.07% a year" comparison and "rounded down" without its basis mislead |
| "Inked" definition | 3 | 3 | Right core, three overreaches: 0.5% applied to payment funds, "running costs" for the cost already counted, "for the top" missing the pre-move bottom |

## Sign-off on Table 3

Yes, with changes. Required before 27 Nov: row 4's "maturing by 15 December", "the range's" margin, "paid out, or its
shares sold", the waiting fund watched (or CONCEIT 8 corrected), and silence as a look, not a swap; row 5's fixed 2031
day; row 7's currency convention. The rest are wording.
