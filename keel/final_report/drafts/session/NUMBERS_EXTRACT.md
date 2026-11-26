# Numbers extract for the writing session (Thu 26 Nov 2026, for Fri 27 Nov)

Checkers' file (WRITING_SESSION 4.1; PREMORTEM cause 3). Checkers verify every printed figure against this file, not
NUMBERS.md. A figure in the draft that is not in a table below fails K1, and so does a figure printed with a second
value, a second basis or a second date. Writers never see this file. Built from FACTS_PLAIN version 15, SECTION_NOTES
(with "Caplet's v2 map"), `exhibits/tables.md` (Table 1, Figure 1 on the fee-and-margin basis, Figure 2, the watch
list printed as Table 2), WORDS, NAME_ORDER, research/COSPONSOR_NOTES and Caplet's own Table 1
(`voice/round21/CAPLET_V2_SECTION2_2026-11-25.md`), each looked up in NUMBERS.md. Nothing was re-run.

**Bases, named once here and used in every table.**
- **6 Nov curve**: the US Treasury par curve at the close of Fri 6 Nov 2026, the day WInS trading froze (NUMBERS 0).
  Every MODEL figure rests on it. Prose dates it twice only: in Section 2's opening and in the recommendation at the
  head of "Ten payments, ten dates" (WORDS l.84; NAME_ORDER decision 6c as amended Thu 26 Nov).
- **Central**: the 6 Nov curve's forward rates ("the rates implied by today's prices", "today's market rates"), world
  shares at J.P. Morgan's 7.5% a year (NUMBERS 4).
- **Cash waiting earns nothing (fee and margin)**: money already paid out earns nothing while it waits, pays the
  short-term Treasury ETF's 0.15% a year, and every iBonds Treasury fund flow is 0.5% smaller. The standard the extra
  Treasuries are sized to, and Figure 1's basis since Thu 26 Nov (NUMBERS 2, 8h, 8zb).
- **Simulated futures**: 200,000 runs of rates and shares, seed 2033 (NUMBERS 0, 4).
- **Record**: the team's WInS record, not a model (NUMBERS 8g, 8m).
- Prose rounds with "about" to $100, $500 or $1,000; tables print exact figures (WORDS l.79). Laura's words never put
  "about" before a figure co-sponsors count.

Columns: **Print** (the form the report may print) / **What it is** / **Basis and date** (money of which year) /
**Unrounded** (the register's value) / **NUMBERS** (section) / **Never print, and why** (the other basis or form).

---

## Section 2. Portfolio Implementation (pp2-4; Caplet's opening, paras 1-5, Table 1)

| Print | What it is | Basis and date | Unrounded | NUMBERS | Never print, and why |
|---|---|---|---|---|---|
| $300,000 (2027), $150,000 (2028), $450,000 | Laura's two deposits and their sum | Case | exact | 0, 8k | |
| ten payments of $50,000, 2033-2042; $500,000 | The operating commitment, 1 January each year, fixed in US$ | Case | exact | 2 | |
| $95,000 | The bottom: what the building gets even if every share is worthless | 6 Nov curve; dated in its sentence | $97,605 before rounding down | 4 (deletion test), 8u | "at least $95,000" (WORDS l.52) |
| nearly 90% / 89.55% | Treasuries' share of the WInS portfolio | Record, at cost | $268,652.18 | 8g | |
| Table 1 rows: IBTM $97,489.95 32.50%; IBTO $23,408.64 7.80%; IBTP $22,155.30 7.39%; IBTQ $20,973.24 6.99%; IBTR $19,823.72 6.61%; 912810PT9 $19,203.80 6.40%; 912810PX0 $18,615.26 6.20%; 912810QD3 $16,200.95 5.40%; 912810QL5 $15,790.32 5.26%; 912810QT8 $14,991.00 5.00%; VT $26,524.61 8.84%; cash $3,513.79 1.17%; fees and accrued interest $1,309.42 0.44%; total $300,000.00 100.00% | The final WInS holdings at cost on the original $300,000 | Record; price paid 6-7 Oct 2026 (US Eastern) | as printed; weights by largest remainder | 8g | the May-2038 bond at 6.21% (plain rounding; the table uses largest remainder); any market value (Wharton bars it) |
| $200 commissions; $1,109.42 accrued bond interest | The costs row's two parts | Record | exact | 8g | |
| units 4,503 / 1,024 / 927 / 894 / 853; bonds 20, 20, 18, 18, 20 lots of $1,000; VT 167 against a target of 164 | Units bought against targets set before trading | Record (targets at 2 Oct prices) | exact | 8m | |
| about $302,300 ($302,287 in a table) | What the ten holdings cost, with the funds' 0.07% fee | 6 Nov curve, valued 1 Jan 2027 | $302,287 | 1 | $301,544 (the payments' curve value, no fund fee: a second "cost of the ten") |
| $2,287 | The ten's cost above the $300,000 deposit | 6 Nov curve, January 2027 money | $2,287 | 1, 2 | beside $2,388 as two gaps; say "$2,287, bought a year later for $2,388" or one figure with its date (NAME_ORDER 6b) |
| $2,388 ("the first $2,400 or so") | The top-up that completes the ten | 6 Nov curve, January 2028 money | $2,388.15 | 2, 5 | "in January 2028 money" in prose (NAME_ORDER 6b) |
| about $39,000 ($39,162) | The first part of the 2028 deposit: top-up plus extra Treasuries | 6 Nov curve, January 2028 money | $39,162 | 2, 4 | "about $38,000" (pre 17 Nov); $37,499 (the same gap in January 2027 money, 8za: one of the two only); $31,859 (13 Nov curve) |
| about a quarter (of the 2028 deposit) | $39,162 as a share of $150,000 | as above | 26.1% | 2 | "about a quarter" for a second quantity in the same part (WORDS l.85) |
| $36,774 | The extra Treasuries | 6 Nov curve, January 2028 money | $36,774 | 2 | $35,213 (the same, 1 Jan 2027 money); $35,894 (pre 17 Nov); $38,062 (13 Nov curve) |
| about three-quarters smaller | How much smaller the 2028 deposit could arrive with all ten still paid if cash waiting earns nothing | 6 Nov curve ("at today's rates") | 73.9% | 5, 8u | 78.8% or 78.6% (13 Nov curve); "three-quarters" for any other quantity in the part (WORDS l.40) |
| $81,244; about 54%, "most of the 2028 deposit" | The floor: IBTM bought again in January 2028 | 6 Nov curve, January 2028 | $81,244; 54.2% | 4 | $75,001, "just over half", "about 55%" (WORDS l.86; NUMBERS 5) |
| $29,594 | VT bought in January 2028 | 6 Nov curve, January 2028 | $29,594 | 4 | $29,829 (pre 17 Nov) |
| about 73% to the floor, 27% to VT | Split of what is left after the payments, same in WInS and the plan | Keel arithmetic | 73.29% (WInS), 73.30% (plan) | 0, 8x(e) | |
| 3,361 shares of IBTM against 167 of VT | The WInS split the floor's size copies | Record | exact | 0 | |
| about $102,000 | What the floor pays in mid-December 2032 | Central | $102,365 | 4 | $103,178 (pre 17 Nov); "the floor pays $95,000" (the bottom is not what it pays, WORDS l.34) |
| x1.5; $293,830 / $109,148 / $39,787 / $7,235 | The WInS portfolio scaled to $450,000: payment Treasuries / floor stand-in / VT / cash and costs | Record x 1.5, at cost | as printed | 8x(e) | "book" in print (NAME_ORDER 5); "after the freeze" |
| $339,162 / $81,244 / $29,594 | The plan in January 2028 at cost: payment Treasuries / floor / VT | 6 Nov curve | as printed | 8x(e), 4 | |
| about $160 against about $200 (or "about four-fifths") | Rate sensitivity per 0.01 point: WInS ten rungs against the payments at the same scale. Table 1's note only, if room | MODEL, 6 Nov curve, value 1 Jan 2027 | $159; $199.79 | 8x(e) | "$159" as exact; "duration matches too" |
| 10,185 companies; fee 0.06% | VT's holdings and fee | Vanguard fact sheet, 30 Sep 2026; TNA note 3 | exact | 0 (fee only) | see Mismatches 5 |
| -7.8% | US independent artists', writers' and performers' receipts, 2009 against 2008 | Census Nonemployer Statistics | -7.83% | 8x(e) | -11.6% (whole arts sector, gyms included); "her genre fell 22.4%" |
| about $15,400 | Interest the floor pays out before December 2032, waiting in the short-term ETF | Central, after fees | $15,446 | 3, 8u | |
| IBTM about a quarter of all she holds in late 2032 (2.3 only) | IBTM carries the 2033 payment, the bottom and the top | Central, net asset value, 30 Nov 2032 | 24.3% | 8w | 26.1% as IBTM's share; a second "about a quarter" in 2.3 |
| within 0.25 percentage points (25 basis points) | The team's pre-trade price check | Record | exact | 8m | "0.25 points" alone |
| -10 to +6 basis points (5 Oct); 2.6 to 8.8 (fills) | How far each bond's yield sat from the official curve | Record; fills MODEL | as printed | 8m | |
| 11 trades; $200, about 0.07% of $300,000; $3,514 cash left | The build's cost and cash | Record | 0.067%; $3,513.79 | 8g, 8m | $37,625 beside $200 as a ratio (8za) |
| about 11 of every 100 trading days since 2000 | Days $300,000 bought all ten | 6 Nov engine on each day's curve | 731 of 6,716, 10.9% | 8e | |
| one day from August 2007 to August 2026: Thu 19 Oct 2023 | The only such day in that span | as above | $299,293 that day | 8e | "on no day since 2008"; "since June 2007" |
| $470,217 on 4 Aug 2020 | The dearest day since 2000 | as above | exact | 8e | |
| Mon 5 Oct 2026, cheapest since May 2002 | The year's cheapest day | as above | $288,333 (8e engine) | 8e | a dollar figure for that day beside the ratio to $200 |
| about $1,900 (16 Oct) | The room under $300,000 on 16 Oct, "on the measure the team used that day" | Team's 16 Oct check | $1,913 (its basis); $1,843 (register's method) | 8b | $1,843 printed; "$1,900" without its basis |
| about 1 point a year (yields), about 18% a year (shares) | The simulated futures' spreads, if Section 2 points ahead | MODEL | 0.9 points; 17.88% | 0 | |

## Section 3, part 1: "Ten payments, ten dates" (pp5-6; 3.0 and 3a; Figure 1)

| Print | What it is | Basis and date | Unrounded | NUMBERS | Never print, and why |
|---|---|---|---|---|---|
| about $445,700 at market value on 1 January 2033 | The operating reserve's size, printed once, in the recommendation sentence | Central (forward market value), 1 Jan 2033 | $445,655 | 8h | "111% funded", "111.7% funded"; $426,371 (the same reserve if cash waiting earns nothing); $444,545 (pre 17 Nov); beside Figure 1's $442,930 total |
| about $1.12 for each $1 the payments need | Reserve against what the payments are worth | Central, 1 Jan 2033 | $445,655 / $399,089 | 8h | "funded ratio"; "$399,089 owed" (say "the remaining payments are worth") |
| $399,089 (if printed) | What the ten still to be paid are worth | Central, 1 Jan 2033 | exact | 8h, 8za(b) | "owed" |
| about $46,600, back to Laura by 2042 | What comes back from the extra Treasuries if rates follow today's prices | Central; its 1 January 2033 money basis named in Figure 1's note only | $46,566 | 8h, 8k | $75,934 (the same money nominal in 2042) or $35,185 (1 Jan 2027 money): one date per figure (NAME_ORDER 6a) |
| about $445,400; about $54,600 short | What the ten as bought in 2027 pay, and the gap, if cash waiting earns nothing and no fees on waiting cash | No-fee zero-interest basis | $445,405; $54,595 | 2, 8h | beside Figure 1 (wrong basis); see the next two rows: one basis wherever the gap is said |
| $444,080; $55,920 short; $1,177 left | The same with the ETF's 0.15% (the "fee" basis) | Fee-only basis | exact | 8h | beside Figure 1 ("$1,177 to spare"), or bare; only with its basis named (8zb) |
| **$442,930 + $57,070 = $500,000; nothing left** | **Figure 1's total row: what the ten's own Treasuries and the extra Treasuries pay, 2033-2042, added up** | **Fee and margin (Figure 1's basis)** | 442,929.57 + 57,070.43 | 8h, 8zb | "the reserve's size" for this total (a ten-year sum of payouts); $442,929 / $57,071 (sums of rounded rows) |
| Figure 1 rows (own / extra): 2033 $47,101 / $2,899; 2034 $46,497 / $3,503; 2035 $45,911 / $4,089; 2036 $45,204 / $4,796; 2037 $44,268 / $5,732; 2038 $43,195 / $6,805; 2039 $43,061 / $6,939; 2040 $43,043 / $6,957; 2041 $42,180 / $7,820; 2042 $42,469 / $7,531 | Each payment's split | Fee and margin | 8zb's cents | 8zb | the fee-basis fund rows ($47,338 / $2,662 and so on, 2033-2037) |
| cash arrives: 20-22 Dec 2032; 19-22 Dec 2033; 18-22 Dec 2034; 20-24 Dec 2035; 18-22 Dec 2036; 17 Feb 2037; 17 May 2038; 15 Nov 2039; 15 Nov 2040; 15 Nov 2041 | When each holding's cash reaches Laura | Card Q2b ranges; bond calendar | as printed | 8h | "10 to 14 days" for all five funds |
| waits 10.5 months / 7.5 months | The Feb-2037 and May-2038 bonds' early payouts | Trading Notes' counts | 10.4 / 7.5 from the cash | 8h | |
| about two weeks (IBTR before 2037) | The 2037 fund's lead over its payment | 8h cash table | 10-14 days | 8h | |
| $37,711 of face and fund dollars; $19,489 of their own interest; $57,200 | Figure 1 note item 2: what the $36,774 buys and pays, added up undiscounted | Cash waiting earns nothing, before the ETF fee and margin | exact | 8h | |
| 3% of the 2033 payment; about 15% of the 2041 and 2042 payments | Interest earned on interest | Central | 3.4%; 15.3%, 14.8% | 8a | |
| about 80 of 100 starting months from 1981; about 17 of 100 from 1962 to 1980 | How often the ten as bought would have come up short, replaying US rates | History, 585 starting months | 80.1% (286 of 357); 17.1% (39 of 228) | 2 | a bare 55.6%; "usually small"; "rarely before" |
| 0.07% a year | Each iBonds Treasury fund's fee | iShares | exact | 0 | |
| 0.15% a year | What the model charges cash waiting in the short-term Treasury ETF | MODEL assumption (which ETF is unverified) | exact | 0, 8za(b) | "the fund charges 0.15%" as a fact about a named ETF |
| 0.5% | The margin each fund's payout is cut by, for costs beyond the fee | Rule | exact | 0, 2, 3 | "a year"; "of the funds' value" (WORDS l.38) |
| about 0.27% | What the plan allows for such costs over a fund's life (Keel's stack, inside the 0.5%) | Keel arithmetic, January 2028 buy held to December 2032 | 0.27% | 0 | as what the ended funds paid (8za(b)) |
| within about 0.07% | How close each of the five ended iBonds funds paid to its last price | Record (card Q3c) | 0.066% | 0, 8h | 0.27% for this |
| five ended funds; IBTA 15 days early | Ended iBonds Treasury funds; IBTA's early end (notice 28 Sep 2021, paid 3 Dec 2021, 29 days before 1 January) | Record | exact | 8h | "ended on schedule" |
| about $334,000 | The ten's cost if yields fell 1 point before January 2027 | 6 Nov curve, re-sized | $334,092 | 1 | "about $30,600" (25 Sep curve, void) |
| about 0.1 point | A rise that would leave no top-up | 6 Nov curve | 0.08 points | 5 | |
| $95,000 to $105,000 (aha 4) | The range after a 40% fall in world shares before the January 2031 move, bottom and every payment unchanged | Central otherwise | $95,000 to $105,000 ($107,041) | 8p | |

## Section 3, part 2: "What certainty costs" (p7; 3b first half)

| Print | What it is | Basis and date | Unrounded | NUMBERS | Never print, and why |
|---|---|---|---|---|---|
| 7.5% a year | J.P. Morgan's 2027 assumption for world shares, "above the middle of published forecasts"; first said here | J.P. Morgan 2027 LTCMA (estimates as of 30 Sep 2026) | exact | 0 | any median ("6.5%", "6.9%"), "upper third", "the top", "the consensus" (CANON B15) |
| $125,000 to $155,000 against $95,000 to $115,000 | The range with no extra Treasuries ("No margin": the ten sized only at today's prices) against the plan's | Central | $129,988 to $156,008 | 4 (cost table) | $130,000 bottom (pre 15 Nov) |
| $39,162 / $81,244 / $29,594 | The 2028 deposit's three uses, pointed back to (never split again) | 6 Nov curve, January 2028 | exact | 4 | |
| about 4.7% (2028 purchase) and about 3% (2031 purchase) | How much the cautious count cuts each purchase | Central | 4.65%; 2.98% | 3, 4 | the void 4.31% / 2.87% or fixed 4.1% / 2.5% |
| about $270 per $5,000 | Expected share growth given up for each $5,000 of top made certain | Central | $267 | 8o, 8x(e) | "about $300"; "costs her $5,300 of what she keeps" |
| about $5,300 per $5,000 | What each $5,000 more of stated top costs of what Laura keeps (3b's trade) | Central | $5,267 | 8o | as a cost to her total |
| about $1,100 or less | How much her total (contribution plus flexibility) changes at the median, any split | Simulated futures and history | $400 / $900 / $1,100 | 8o | |
| keep 30%: top about $5,000 higher; covers a 10% stronger Taiwan dollar in about half of futures | The 70%-moved split | Central; simulated futures | $120,000; 49.8% | 8o | $125,000 (pre 17 Nov) |
| half: about 93 in 100 | Her flexibility alone covers a 10% stronger Taiwan dollar | Simulated futures | 92.9% | 8j, 8o | 93.3% (pre 17 Nov) |
| keep 70%: top about $10,000 lower | The 30%-moved split | Central | $105,000 | 8o | $110,000 (pre 17 Nov) |
| 44.5% to 57.3% | Any share moved in this span states the same $115,000 (a flat stretch; reserve only) | Central | exact | 8o | "a maximum" |
| about $122,500 | What IBTM pays on its two purchases, centrally | Central | $122,503 | 4 | $123,476 (pre 17 Nov) |
| $110,000 against $115,000 | An all-Treasury plan with the same flexibility | Central | $119,166 stated $110,000 | 4 (C8) | 94.8% and 62.8% (SECTION_NOTES 3b trap) |

## Section 3, part 3: "Before Laura gives her word" (pp7-9; 3c, 3d with Laura's words; Figure 2)

| Print | What it is | Basis and date | Unrounded | NUMBERS | Never print, and why |
|---|---|---|---|---|---|
| about $95,000 to $115,000 (team's voice); $95,000 and $115,000 (Laura's words, no "about") | The 2031 range | 6 Nov curve (dated once, at the head of Section 3's first part) | $97,605 to $117,142 | 4 | $105,000 to $125,000 (13 Nov curve, register note only); $145,000-$170,000 and $140,000-$160,000 (void); "up to $115,000"; "at least $115,000" |
| at least $100,000 in about 91 of 100 simulated futures; at least $115,000 in about 57 | Seen from today, which top she will be able to state | Simulated futures | 91.2%; 57.2% | 4 | 53.4%, 5.4%, 96.9% (never printed, 3); 59.8% / 92.2% (pre 17 Nov); "95%", "confidence interval" |
| about 11 of 100 | A top named in January 2030 would exceed what the January 2031 move buys (one clause inside aha 1's sentence) | Simulated futures | 10.6% | 4 | "not yet owned in 11 of 100" |
| $115,000 at about 5% a year; $110,000 at 3.1% | The top at the team's own build from yield, growth and valuation, and at the low end (Figure 2's note) | Central otherwise | $115,811; 3.417% threshold | 8v | "building blocks" |
| top states $115,000 for growth from 4% to 10% a year | Robustness (Figure 2's note) | Central | $115,296 to $118,537 | 4 | |
| about $117,100 (at 7.5%); about $115,800 (at 5%) | Unrounded tops, if the rounding is explained | Central | $117,142; $115,811 | 4, 8v | |
| $85,000 | The bottom if yields were 1 point lower by January 2027 | 6 Nov curve, shifted | $85,000 | 5(e) | |
| a tenth of a point | A yield move that can shift either end one $5,000 step | 6 Nov curve | 0.07 to 0.10 points | 4 ("On a later curve"), 8u | |
| $20,000 | The gap between the ends: the shares moved in January 2031 | Central, rounded ends | about $19,500 unrounded | 4 | |
| $615,000 in all | Her whole commitment: $500,000 plus $115,000, a sum of promises at face | Exact | exact | 8k | "about $615,000"; set against what comes back to her |
| $115,000 is about NT$3.77 million | The pledge's Taiwan-dollar size on a named day | 32.768 NT$ per US$, 6 Nov 2026 | 3,768,320 | 8d, 8j | a promise in NT$ |
| about $111,700 (market value) | The broker's statement of the building's money on the day of the January 2031 move (team's words, never Laura's) | Central, 6 Nov curve | $111,651 | 8y | "net asset value"; a model date for passing $115,000 (passes about late August 2031 in the model: never printed as a date); "monthly" statements |
| about $117,700 | What the building's Treasuries will pay by December 2032 even if cash waiting earns nothing, while IBTM runs to its stated end | Zero interest from each trade day, after both fees | $117,731 | 3, 8y | "never under $117,731" (fact check v15); $118,644 (the same count on the move day, a second figure) |
| $10 million over five years; $3 million | Lehman's October 2007 pledge to Spelman College; what the college received after the September 2008 bankruptcy | Card Q200 (outside fact) | exact | 8x(e) (card citation suffices) | "Holdings itself"; "a pledge from a fortune" |
| Figure 2 rows (bottom / top / flexibility plus anything above the top, Jan 2033): today's rates $95,000 / $115,000 / $28,700; 2006 recession $95,000 / $105,000 / $18,500; rates 3 points lower $75,000 / $95,000 / $19,600; 2007 recession $80,000 / $95,000 / $20,500; inflation world $100,000 / $115,000 / $27,600; median starting month $95,000 / $115,000 / $31,800 | Five markets and history (585 overlapping starting months, 1962-2010) | MODEL, 6 Nov curve; flexibility to the nearest $100 | 8i, 8j unrounded | 8i, 8j | history's 5th or 95th percentile, "1 in 20" for history rows (card Q210) |
| 200,000; 17.88%; about 0.9 points a year; 5% a year (inflation world) | Figure 2's note: the simulated futures' runs, volatility, yield moves, inflation | MODEL assumptions | exact | 0, 8i | |
| about 2% of what it pays; about $120 for each further 0.1% | Figure 2's note: the room under the top, and the shortfall past it, if cash waiting earns nothing | Central | 2.32% of $117,731; $118 | 3, 8u | "about 3%", "about 7%" (pre 17 Nov covers); "a year" |
| Mon 3 Jan 2028; Thu 2 Jan 2031 | The trade days each end turns on | Model dates | exact | 4 | |

## Section 3, part 4: "When the world changes" (pp10-11; 3e, 3b second half; Table 2 in print, the watch list)

| Print | What it is | Basis and date | Unrounded | NUMBERS | Never print, and why |
|---|---|---|---|---|---|
| about $21,200 | Her flexibility (half the shares, promised to no one) | Central, 1 Jan 2033, shares at 7.5% | $21,179 | 4, 8k | under the name "her flexibility" for $28,700 |
| about $28,700 | Her flexibility plus anything IBTM pays above the top | Central, 1 Jan 2033 | $28,682 | 4, 8k | "her flexibility" alone; $29,823 (pre 17 Nov) |
| about $9,600 or less, in 1 simulated future in 20 | Her flexibility's low end | Simulated futures | $9,621 | 4, 8o | $9,881 (pre 17 Nov) |
| about $7,500 (if printed) | What IBTM pays above the top | Central, 15 Dec 2032 | $7,503 | 4 | "excess", "cap" (WORDS) |
| a rise of about 25% in the cost of the part of the building her $115,000 pays for, if shares earn the 7.5% assumed | What her flexibility plus anything above the top covers | Central | 24.9% | 8u | "her share of the building"; "a building-cost rise of 25%"; 30.2% or 51.2% (bottom readings, never in prose); 23.6% at 6.5% only with its return named |
| $11,500 | What a 10% stronger Taiwan dollar adds on her $115,000 (currency alone) | 8j's reading (10% more US dollars) | $11,500 | 8j | 29.49 NT$ per US$ (NT$ down 10%); 29.79 is for scale only |
| about 98 of 100 two-year stretches | The half of the shares alone covering the actual two-year Taiwan-dollar move | History since October 1986 (417 windows) | 98.3% | 8o, 8za(b) | "since 1983" for these windows |
| four times since 1991 (1991-93, 2002-05, 2006-08, 2019-21); 28% or more; about $32,200 | Building costs and the Taiwan dollar together, within two years; the need on $115,000 | DGBAS index and FRED EXTAUS since Jan 1991 | 20 windows in four episodes; $32,191 at the 28.0% 1-in-20 | 8q, 8x(d) | "1 in 20" for the episodes; "17 spans in four episodes"; "four times" as aha 9's frequency |
| 38% more US dollars, 1986-88, from the currency alone; about $44,000 | Largest two-year move in the Fed's monthly series (from October 1983) | FRED EXTAUS | +38.3%; $44,046 | 8x(a,b) | "larger than any since 1991" without "from the currency alone"; the Taipei city +48.1% beside 38.9% |
| more than 40% (start 2000 to start 2003); about 17% below cost (end 2004); about 18% (NT$) and about 27% (US$), Jan 2003 to Dec 2004; steel bar 38%; three months, Dec 2003 to Mar 2004 | The 2000-04 replay (aha 9) | MSCI ACWI price series, DGBAS, FRED | 44.15%; 16.7%; 18.40%, 27.24%; 37.8% | 8za(a) | "about 42%"; "about 10%" below cost; "56-57%" rise; "one quarter" for three months |
| about a quarter dearer in US$ (twice: through steel 2003-04, through the Taiwan dollar after 2008-09) | Both world-share falls of 30% or more since 2000 | Run medians | about 27%; about 24% | 8za(a) | as a frequency |
| 29 of 31 starts (fails January 1988 and January 2000) | Her flexibility with anything above the top covered the building's rise, shares bought each January from 1988 | Taiwan replay, Laura's calendar | 29 of 31 | 8q | |
| $4,600 / $2,900 at most; about $1,800 or about $2,800 (2036 payment) | What an early end of IBTM in 2031 leaves short if cash waiting earns nothing: top / bottom; the ten with no costs beyond the fee or with the full 0.5% | Zero interest; exit 2 Jan 2031 | $4,589; $2,887; $1,827; $2,756 | 3 | "met from her flexibility" or any make-up (Mismatches 3); a probability; at today's market rates nothing is short |
| about 2% (top) | The room under the top for fund costs beyond the fees | Central, cash waiting earns nothing | 2.32% | 3, 8u | "a year" |
| $500,000 | SIPC's cap; the risk above it is delay | SIPC | exact | 8u | |
| five business days | When a late Treasury payment counts as a default (S&P's test) | S&P | exact | 8u | a delay after the Fed credit (31 CFR 356.30) as a reason to change |
| 31 March 2028 | A missed deposit (nothing received by then) | Table 2's reading, never the IPS's date | exact | 5, 8u | "the IPS's date" |
| $57,455 | The ten short with no 2028 deposit, if cash waiting earns nothing | Zero interest, no ETF fee | $57,455 | 5, 8u | $58,775 (with the ETF fee) beside it |
| $3,016 | The 2033 payment short with no 2028 deposit, at today's rates | Central | $3,016 | 5 | |
| 3.57 points | Fall before 2027 the payments' standard survives (Table 2's note) | 6 Nov curve | 3.57 | 5 | 3.89 beside it (the ten alone at forwards) |
| about $39,000 (Table 2 row 1) | The first part of the deposit to the payments | 6 Nov curve, January 2028 money | $39,162 | 2 | |
| Table 2 rows: $150,000; $3,016 / $57,455; $85,000 (1 point lower by Jan 2027); 0.07% and 0.15%; 31 October; 0.5% of net asset value; 1 Dec 2027; $11,500; 1.5% to 5.0% a year (five-year building costs); $28,700 | The watch list's figures | as each row above; building-cost band DGBAS to October 2026 | the five-year rate 3.19%; the latest year +7.18% (Oct 2026, 120.50) | 4, 5, 8d, 8j | "monthly" statement; any figure in Laura's words |
| 2027 (the X-date about August-December 2027) | The debt-limit risk's date | Card Q253 | | (card) | "early 2028" |
| $16,900 (if used) | Need on $115,000 after the 2008-09 slump on Laura's calendar | Card Q246 row 25 | about $16,900 | (card) | "1 in 25" |

## Section 3, part 5: "Why we changed our minds" (pp11-12, last; 3f)

| Print | What it is | Basis and date | Unrounded | NUMBERS | Never print, and why |
|---|---|---|---|---|---|
| 27 September 2026 | The day the first plan was dropped, before any trade | Record | | 8s | |
| 75% shares | The first plan's mix | Record | 75% | 8s | "three-quarters" in the same section (WORDS l.40) |
| about 1 run in 31 (3.2%) of the 27 September model's runs | The first plan missed at least one payment | 27 Sep model | 3.2% | 8s | "simulated markets"; "3.2% fails 'high'"; the 27 Sep model's "never" for the Treasury plan (its code assumed it) |
| 13.7%; 40.8% | The first plan's misses with a $75,000 deposit; with none | 27 Sep model | exact | 8s | |
| none | The Treasury plan's misses once the 2028 deposit is in (from January 2028, cash waiting earns nothing) | Standard, 0 of 585 history windows | $0 | 2 | resting "none" on the 27 Sep model |
| 1 January 2033 | The first plan's one danger date, when all ten had to be bought | 8s | | 8s | "one of ten dates" |
| 29-30 September; 5 October; 7 October, 00:30 Sydney; 7-8 October; 6-7 November | Dated events (stale prices; the copout; the open and the click; fills; the IPS) | Record | | 8g, 8m | "about nine hours" before the open (8za store only) |
| 19 Dec 2007; 1 Jan 2008 to 31 Dec 2017 | Buffett's bet (3c only, if used) | Outside fact | | (card) | |

---

## Outside facts in the files (cards, not NUMBERS figures)

NUMBERS 8x(e) lets a card citation stand for these; the checker confirms the card, not the register.

| Print | Fact | Source (as the files give it) |
|---|---|---|
| "until 2024 at the earliest" (2 Feb 2021); raised May 2022; review 15 Nov 2022 | RBA forward guidance (reserve only since Thu 26 Nov) | RBA Media Release 2021-01; review p.14 |
| more than a percentage point in a few days; no claims | 2022 gilt crisis | PPF to Parliament, Nov 2022 (card Q243) |
| 25 September 2025 | California State Lottery Commission policy approved for 2025 | Card Q211 |
| 8 of 17 (about half) | Executives who broke a pre-agreed stop rule | Boulding, Morgan and Staelin (1997) |
| 4 March 2025 | Laura's *Climbing* magazine quote | FACTS l.23 |
| 10,185 | VT's companies at 30 Sep 2026 | Vanguard fact sheet |
| did not pass 2008 until 2011 | Census receipts after 2009 | Card Q148 |

## Never print (banned forms and the other basis)

| Never | Print instead | Why (source) |
|---|---|---|
| "about $300" per $5,000 | "about $270" | $267 rounds to $270 (NUMBERS 8x(e)) |
| "about 42%" (2000-03 fall); -42.1%, -40.6% | "more than 40%" | spliced price and gross series (8za; CLAUDE.md Mon 23 Nov) |
| "about 10%" below cost in 2004; "56-57%" rise | "about 17% below cost"; no rise figure | 8za(a) |
| $502,605; a bare "$1,177 spare"; "about $502,600" beside Figure 1 | Figure 1's $442,930 + $57,070 = $500,000 | 8x(e); SECTION_NOTES l.314; see Mismatches 2 |
| $444,080 / $55,920 / $1,177 or $445,405 / $54,595 beside Figure 1 | the fee-and-margin figures | 8zb: one basis per figure |
| $301,544 as the ten's cost | about $302,300 | 1: the payments' curve value has no fund fee |
| $2,287 and $2,388 side by side as two gaps; "in January 2028 money" in prose | one of the two, with its date | NAME_ORDER 6b |
| $37,499 beside $39,162 | one, with its date | 8za(a) |
| $35,213 (extra Treasuries in 2027 money) | $36,774 | one money year |
| $75,934 or $35,185 beside about $46,600 | "about $46,600 by 2042" | NAME_ORDER 6a |
| "$399,089 owed" | "the $399,089 the remaining payments are worth" | 8za(b) |
| 111.7% / "111% funded" / "funded ratio" | "about $1.12 for each $1", Figure 1's note only | WORDS l.30 |
| $105,000 to $125,000; $31,859; $32,074; 78.6% / 78.8% | the 6 Nov figures | 13 Nov curve: a register note, never re-booked (4, 5) |
| "about $615,000"; "at least $95,000"; "at least $115,000"; "up to $115,000"; "certain" in Laura's words | "$615,000 in all"; "$95,000, held for me since January 2028"; "$115,000" | COSPONSOR_NOTES C4, C8, C9; WORDS l.51-53 |
| any promise to make up a shortfall from her flexibility | the sum and what holds it | WORDS l.53; FACTS v15; C3 dropped |
| $75,001; "just over half"; "about 55%" | "most of the 2028 deposit" (about 54%, at today's rates) | WORDS l.86 |
| "about $38,000"; any pre-17 Nov figure ($38,282, $35,894, $81,889, $29,829, $103,178, $123,476, $21,347, $29,823, $98,380 to $118,072, $444,545) | the re-sized figures above | NUMBERS header, 6 |
| "about 3%" / "about 7%" covers of the top | "about 2%" (cash waiting earns nothing) | 3, bond desk 4 |
| a median for the 7.5% ("about 6.5%", "6.9%"); "upper third"; "the top"; "the consensus" | "above the middle of published forecasts" | CANON B15; card Q146 |
| -11.6% (writers' 2009 receipts); "her genre fell 22.4%" or "by a third" | -7.8% | 8x(e); card Q108 |
| a bare 55.6%; "usually small"; "rarely before" | "about 80 of 100 starting months from 1981, about 17 of 100 from 1962 to 1980" | 2 |
| "1 in 20" or "four times" as a frequency for the Taiwan episodes; "17 spans in four episodes" | "four times since 1991, in four separate episodes" | 8x(d), 8za(b) |
| "since 1983" for the 98 of 100 | "since October 1986" | 8za(b) |
| 0.27% as what the ended funds paid | "within about 0.07%" | 8za(b) |
| 29.49 NT$ per US$ | 29.79, for scale only, or none | tables.md Table 2 list, row 7 |
| "early 2028" for the debt limit | "2027" | card Q253 |
| "monthly" statements | "at least quarterly" | card Q230 |
| "net asset value" for the statement | "market value" | card Q251 |
| 53.4%, 5.4%, 96.9%, 51.2%, 30.2% | none | 3, 8u: never printed |
| "about 1 point" for the stale prices; "about nine hours"; $75 (card Q6d); "four years out of five" | none, or the card checked first | 8za(a): store only |
| $145,000-$170,000, $145k-$168k, $140,000-$160,000, $110,000 to $130,000, "about 75-76%", "94% of 16-year stretches" | the current range | NUMBERS 6 (void) |
| "barring a US default" attached to Treasuries in new sentences | the strong word alone | Book 19 |

---

## Mismatches (figures in the source files not found in NUMBERS, or at odds with it)

No figure in the source files disagrees with NUMBERS in value. The ten items below are basis, placement, wording or
registration problems for the lead to settle before round 1; items 1-4 touch text that would be printed.

1. **Where the reserve's size prints.** `exhibits/tables.md` l.74 (Figure 1 note item 4) prints "about $445,700 ...
   printed once, here", but NAME_ORDER l.331-333 (decision 7 as amended Thu 26 Nov) and WORDS l.29 move it to the
   recommendation sentence of "Ten payments, ten dates" and out of Figure 1's note; SECTION_NOTES l.271 still says "in
   3a's first sentence" against WORDS' "the part's first sentence stays about the payments". Value agrees ($445,655,
   NUMBERS 8h). Print once: the recommendation sentence; take note item 4's size out.
2. **"About $502,600".** `exhibits/tables.md` l.74 (Figure 1 note item 8, "if room") prints it on the no-fee basis;
   SECTION_NOTES l.314 says never "about $502,600"; NUMBERS 8x(e) allows it only with the no-fee basis named. With
   Figure 1 now on fee and margin, keep item 8 out of print.
3. **Make-up remnants against FACTS v15 and WORDS l.53.** `exhibits/tables.md` l.143 ("$4,589 short, met from her
   flexibility"); research/COSPONSOR_NOTES l.55 ("at most about $4,600, from her flexibility"); NUMBERS section 4,
   "The letter fixes the sum" (l.583: "she makes up the difference from her flexibility"). The figures ($4,589,
   $2,887, $1,827) agree with NUMBERS 3; the words do not. FACTS l.87 is the form: "What she kept back could cover that,
   but her letter does not promise it."
4. **"The floor always over half the deposit".** `exhibits/tables.md` l.48 (Table 1's note). NUMBERS 5(e): after a
   fall of 1.30 points or more before January 2027 the floor gets all of what is left, less than half; WORDS l.86 bars
   any label saying the floor's minimum binds. Say "about 54% at today's rates" or drop the clause.
5. **VT's 10,185 companies** (FACTS l.69): not in NUMBERS (only the 0.06% fee is, section 0). Vanguard fact sheet of 30
   Sep 2026; check the card before printing, or say "thousands of companies".
6. **"Did not pass their 2008 level again until 2011"** (FACTS l.70): NUMBERS 8x(e) registers only 2008 against 2009
   (-7.83%). Not registered; card Q148's file.
7. **Boulding, Morgan and Staelin's 8 of 17** (FACTS l.129): a literature figure, not in NUMBERS; check the card.
8. **"About 1 percentage point" for the stale WInS prices** (FACTS l.152): NUMBERS 8za(a) lists it "not printed, store
   only". FACTS already says check the record first; default: no figure.
9. **"About a quarter" for IBTM's 24.3%.** SECTION_NOTES l.225 and NUMBERS l.3317 say "about a quarter" is WORDS' for
   the 26.1% alone, but WORDS l.85 and NAME_ORDER decision 11 allow it for IBTM's 24.3% in 2.3, and FACTS l.69 uses it
   there. Decision 11 wins: allowed in 2.3, one quantity per part.
10. **NUMBERS 8d, internal.** l.997 registers October 2026's index (120.50, +7.18%, 3.19% over five years, read at
    source 17 Nov); its sub-bullet l.998 still says "the register keeps September's +7.29%". The watch list's note uses
    October; print October's figures.

Count: 121 printable rows (Section 2: 35; part 1: 23; part 2: 13; part 3: 18; part 4: 24; part 5: 8), about 210
figures once Table 1's, Figure 1's, Figure 2's and the watch list's grouped cells are counted singly; 7 outside facts;
32 never-print forms.

## Resolved the same evening (Thu 26 Nov)

- Mismatches 1-4 fixed at source: Figure 1's note no longer prints the reserve's size (printed once, in the recommendation sentence of "Ten payments, ten dates"; SECTION_NOTES agrees); "about $502,600" removed from Figure 1's note; the make-up wording in the watch list's row 4, COSPONSOR_NOTES and NUMBERS marked dropped; "the floor always over half the deposit" removed from Table 1's note.
- Second reading at source (`research/day19_2026-11-26/SECOND_READING.md`): the Census -7.8% is for artists and writers "working as sole proprietors" (all one-person businesses in the group -6.2%); IBTA stopped trading 15 days early and paid out 12 days early (3 December 2021), say "about two weeks early"; the Lottery policy was "reaffirmed and adopted" on 25 September 2025, never "approved".
- The six unregistered figures (VT's 10,185 companies, the Census "until 2011", Boulding's 8 of 17, the stale-price "about 1 point", "about a quarter" for 24.3%, NUMBERS 8d's index note) stay printable only in the words their cards give; a checker treats any other form as a killer item.
