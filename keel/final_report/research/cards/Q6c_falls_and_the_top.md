# Q6c research cards: a 40% fall in world shares before 2031: how often, and what it does to the top

Sun 15 Nov 2026, Sydney (research run of Sat 14 Nov evening). Report parts: 3b (the facility contribution and her
flexibility), 3c (the 2031 range and its confidence), 3e (assumptions, limits and what to watch; Table 3) and the note
to Table 2. Notes for the Final Report store, not report prose.

Checked against: Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt` l.11, l.15, l.17, frozen), the TNA
(`keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt` l.21, Trading Note 3), `CANON.md` (A28, A29, A34, D4),
`NUMBERS.md` (sections 0 and 4, 8f, 8i, 8o; every plan figure here is MODEL), `WORDS.md` ("her flexibility" for the half
kept; "the shares moved into Treasuries before the 2031 meetings" for the moved half; the NUMBERS labels "half kept" and
"moved half" appear only where a NUMBERS row is quoted), `CONCEIT.md` (pencil and ink) and card Q6 (Mon 9 Nov: how far
to trust 7.5%; its long-run-average work is not repeated here). New computation: `keel/final_report/numbers/fall40.py`,
results `keel/final_report/numbers/results_fall40_2026-11-15.json` (about 9 seconds; imports engine, plan and
completion; changes no other script and writes no other file).

**Claims tested.**
1. KEEP, KILL or CHANGE: "World shares have fallen 40% or more inside a three-year window several times since 1900
   (1929-32, 1973-74, 2000-02, 2007-09; others?)", with frequency, recovery times and the distribution of 3-year and
   5-year world nominal USD returns.
2. KEEP, KILL or CHANGE: "A 40% fall in VT between its purchase in January 2028 and the move before the 2031 meetings
   lowers only the top of the range and her flexibility; the ten payments and the bottom do not move."
3. KEEP, KILL or CHANGE: "The fall result fits IPS l.15 ('markets will be able to increase or decrease the top') and
   Trading Note 3 (TNA l.21: 'a rise before 2031 lifts the top of the range co-sponsors hear')."

**Problem class and the field that solved it first.** Drawdown and shortfall risk over a fixed horizon, the first-passage
problem of a random walk (how often a price path touches a level before a date, against where it ends). Finance met it
first in the long-history studies of market crashes and "time diversification" (Jorion and Goetzmann, 1999; Dimson,
Marsh and Staunton, 2002; Jorion, 2003; Barro and Ursúa, 2009/2017); the plan side is a contingent-claim question
answered by the register's own engine (what each stated end is worth as a function of VT's value on one date).

## Verdicts in one screen

1. **Claim 1: KEEP, with two changes.**
   - **Four times since 1900 in nominal USD, about once a generation.** On GFD's World index (Taylor, 2019): 1929-32
     -75.4% (34 months), 1973-74 -42.4% (18), 2000-02 -49.7% (30), 2007-09 -54.8% (16). Two near misses: 1912-21 -39.4%
     (over nine years) and 1937-40 -39.75% (39 months). On MSCI World with dividends, monthly, since 1970: three (1973-74
     -40.0%, 2000-02 -46.3%, 2007-09 -53.7%; Cambridge Associates, 2019). MSCI's own factsheets put the deepest fall since
     1987 at 57.46% (gross), 31 Oct 2007 to 9 Mar 2009. After inflation there are more: the DMS world index lost 54% in
     real terms in 1929-31 and 44% to 54% in each peacetime bear market (Dimson, Marsh and Staunton, 2009).
   - **Change 1: the fall that matters to the plan is not the drawdown.** The top depends on VT's value on the move day
     against its January 2028 cost, not on the low between. That point-to-point fall of 40% is much rarer than a 40%
     drawdown inside three years: MSCI World calendar 3-year windows 1970-2025, 1 of 54 (2000-02, -41.5%); US stocks
     since 1871, 1.1% of 3-year windows end 40% down while 6.7% contain a 40% fall; the register's house model, 0.94%
     end there while 4.2% (same assumptions, month by month) contain one.
   - **Change 2: recovery is years, not months, and longer after inflation.** MSCI World took 53 months from the
     March 2009 trough to regain its 2007 high, and 40 months from the 2002-03 trough (Walter Scott, 2025, monthly total
     return); the price index regained its 2007 high in February 2013 (Funds Society, 2025). US stocks with dividends
     (repo's Shiller mirror, monthly): 183 months from the 1929 peak, 74 from 2000, 58 from 2007. After inflation, much
     longer (Davis, 2003: most G-7 markets regained their 1972-73 real level only in the mid-1980s to 1990s).
   - **The distribution asked for** (MSCI World gross, USD, calendar years 1970-2025; Keel arithmetic; data before 2012
     UNVERIFIED at MSCI): 3-year total return worst -41.5%, 1 in 20 -16.5%, 1 in 10 -11.7%, median +38.3%, below zero in
     9 of 54 windows; 5-year worst -9.8% (2000-04), 1 in 20 -7.4%, median +70.1%, below zero in 6 of 52, none 20% down.
2. **Claim 2: KEEP, with three changes.** Computed on the register's engine; the central case reproduces NUMBERS 8i row 1
   to the cent ($95,000 ($98,729) to $115,000 ($118,443); funds pay $123,476; contribution $115,000; above the top $8,476;
   half kept $21,347; all ten paid; $74,123 left by 2042).
   - **(a) VT 40% below its January 2028 value at the move, then 7.5% a year:** $95,000 to $105,000 (unrounded top
     $108,250); funds pay $112,981; contribution $105,000; $7,981 above the top; her flexibility $10,310 on 1 Jan 2033
     ($8,922 if VT is then flat); all ten paid; the bottom and the $74,123 from the extra Treasuries unchanged.
   - **(b) VT flat to the move, then 40% down by January 2033:** $95,000 to $110,000 ($114,598), contribution $110,000,
     exactly as with VT flat then 7.5%; only her flexibility moves ($17,184 to $8,922).
   - **(c) 40% down at the move, then back on its 7.5% path by 2033:** the top stays $105,000 and the contribution
     $105,000; her flexibility is back at $21,347. Laura ends $10,494 below the central case: the promised half was
     moved at the low.
   - **Change 1: "lowers only the top" understates it.** The contribution falls with the top ($10,000), because the
     contribution is the lower of what the funds pay and the stated top. **Change 2:** a fall before the move is kept even
     if shares recover (c). **Change 3:** the central $115,000 needs VT up at least 2.5% over 2028-2031 (0.84% a year);
     flat shares give $110,000, which holds down to a 29.0% fall; $105,000 holds to a 60.5% fall; $100,000 to 92.0%;
     $95,000 even at zero. Each $1 VT gains or loses before the move moves the unrounded top by about 53 cents.
   - **With a recession's rates too (yields 2 points below today's forwards from the move):** still $95,000 to $105,000
     ($107,979); funds pay $111,684; all ten paid; what comes back from the extra Treasuries falls from $74,123 to $55,195
     by 2042 (nominal).
3. **Claim 3: KEEP.** IPS l.15 ("markets will be able to increase or decrease the top ... but the bottom will remain
   constant") and TNA l.21 ("A fall can shrink the extra") describe result (a) exactly: the bottom stays $95,000 and the
   extra above it halves, from $20,000 to $10,000. TNA l.21's "a rise before 2031 lifts the top" is the same line read the
   other way (VT up 34% lifts it to $120,000). One risk to record, not a change: the IPS moves half before the meetings
   whatever the market (l.15) and a fall is no reason to change (l.17), so after a crash the promised half is moved at the
   low; the report shows that cost (c) and answers it with l.15's own reason ("whatever figure you choose is money you
   already own").

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | World shares fell 40% or more in nominal USD four times since 1900, each inside 16-34 months: 1929-32 -75.4%, 1973-74 -42.4%, 2000-02 -49.7%, 2007-09 -54.8% (GFD World index, month-ends) | Taylor (2019), Finaeon/GFD, Table 1 | CEILING, MOVE2031 | KNOWN | About one in a generation; one could fall inside Laura's 2028-2031 window | GFD's post does not say whether its world index is price or total return; monthly points | VERIFIED (fetch of the post, full text) | no | GFD post, Table 1 |
| 2 | Two near misses: 1912-21 -39.4% nominal over nine years (-69% after inflation) and 1937-40 -39.75% over 39 months | Taylor (2019) | CEILING | NICHE | "Several" is four at 40%, six at 39%; a slow fall over nine years is a different risk from a crash | Real and nominal tell different stories in inflations | VERIFIED (fetch) | no | GFD post, text and Table 1 |
| 3 | Developed-world shares with dividends, monthly, since 1970: 40% or worse three times (1973-74 -40.0% in 19 months, 2000-02 -46.3% in 30, 2007-09 -53.7% in 16); the other bear markets -17% to -24% | Cambridge Associates (2019), appendix table, MSCI World total return USD | CEILING, MOVE2031 | KNOWN | Since VT's kind of index exists, a 40% fall has come about every 18 years | Monthly data; the 1973-74 figure sits exactly at 40% | VERIFIED (PDF excerpt) | no | Cambridge Associates PDF appendix |
| 4 | MSCI's own deepest falls: World 57.46% gross and 59.07% price since 1987, 57.82% net since 2000; ACWI 58.38%; all 31 Oct 2007 to 9 Mar 2009; World 10-year volatility 14.86% | MSCI (2026a, 2026b, 2026c) factsheets, 30 Oct 2026 | CEILING | TEXTBOOK | The daily low of the worst fall in VT's own index family; the register's 17.88% volatility is above MSCI World's recent 14.9% | Daily drawdown, deeper than monthly figures in rows 1 and 3 | VERIFIED (net factsheet read in full; gross and price in excerpt) | no | msci.com factsheets |
| 5 | After inflation the DMS world index lost 54% in 1929-31 and 44% to 54% in each peacetime bear market, against -18% and -12% in the two world wars | Dimson, Marsh and Staunton (2009), LBS article on the 2009 Yearbook | CEILING, INFLATION_TWD | KNOWN | The plan states dollars, not real value; a fall with inflation (1973-74) hurts the contribution's buying power too (NUMBERS 8i inflation world) | Annual data; real USD | VERIFIED (search excerpt of the LBS page; page fetch fragmentary) | no | LBS news page |
| 6 | Three of the six worst episodes for large global markets since 1900 were geopolitical (WWI, WWII, 1973-74); three of the four largest peacetime bear markets were economic; shares and bonds have each lost more than 70% in real terms, a 60:40 mix never more than 50% | Dimson, Marsh and Staunton (2026), UBS Yearbook public summary, section 7 and 8 | CEILING, OTHER | KNOWN | The causes vary; the plan needs no forecast of which kind comes | Summary edition gives no sizes or dates for the six | VERIFIED (full text fetched; sections 7-8 read) | no | UBS summary PDF |
| 7 | Single countries crash far more often than the world: 30 countries, 3,037 country-years, 124 real falls of 40% or worse (0.049 a year of entering one), 232 of 25% or worse, average length 3.2 years | Barro and Ursúa (2017; NBER w14760) | CEILING, PROCESS | KNOWN | VT owns about 10,000 companies in many countries, so its crash rate is nearer the world's than any one country's | Annual real data; country-level, not a world index | VERIFIED (NBER abstract page and working-paper PDF excerpts) | no | NBER page and PDF |
| 8 | A global index had far less downside than its parts: worst ten-year real loss 54% against 61% for the US and a median 76% across 30 markets; across-country diversification beats waiting longer | Jorion (2003), Financial Management 32(4) | CEILING, HALFKEPT | KNOWN | Supports one world fund (TNA l.23) over any single market; says nothing about timing | Real capital index, no dividends, 1921-1996, GDP weights | VERIFIED (PDF excerpts on Harvey's Duke page) | no | Duke PDF |
| 9 | Falls are synchronised when they are deep: in 1972-74 the G-7 troughs fell between Sep and Dec 1974 although peaks were spread; nominal recovery took 6-7 years in most G-7 markets; correlations with the world index rise in bear markets | Davis (2003), National Institute Economic Review 183 | CEILING, OTHER | NICHE | Diversifying inside VT does not soften a world crash; only the Treasuries do | MSCI price indices in local currency, no dividends | VERIFIED (PDF excerpts, author's site) | no | ephilipdavis.com PDF |
| 10 | Recovery of MSCI World after its two 21st-century falls: 53 months from the March 2009 trough (fall -54%), 40 months after the dot-com trough (fall -47%); the price index regained its 2007 high in Feb 2013 | Walter Scott (2025); Funds Society (2025) | HALFKEPT, MOVE2031 | KNOWN | A fall just before the move would not be recovered by the 2031 meetings; one in early 2028 might be | Fund manager and news summaries; not checked against MSCI data | VERIFIED (search excerpts; secondary) | no | Walter Scott page; Funds Society article |
| 11 | MSCI USA took 74 months to recover from 1973-74, about four years from the dot-com bust and from 2008, two months from 2020 | MSCI (n.d.), "Time in the markets beats timing the markets" | HALFKEPT | KNOWN | Recovery times vary by a factor of 30; no rule can wait them out before 2031 | US index, not world | VERIFIED (search excerpt of msci.com) | no | MSCI blog |
| 12 | Developed-world 3- and 5-year nominal USD returns, calendar years 1970-2025: 3-year worst -41.5% (2000-02), 1 in 20 -16.5%, median +38.3%, 9 of 54 below zero; 5-year worst -9.8%, 1 in 20 -7.4%, median +70.1%, 6 of 52 below zero; 10.1% a year compound over 56 years | Keel arithmetic in fall40.py on MSCI World gross annual returns (2012-2025 MSCI factsheet; 1970-2011 Wikipedia table) | CEILING, MOVE2031 | KNOWN | Point-to-point over three years, a 40% loss came once in 54 calendar windows | Calendar years hide falls inside a year (2007-09 shows only as 2008's -40.3%); pre-2012 data UNVERIFIED at MSCI | Keel arithmetic; data partly UNVERIFIED | no | fall40.py block developed_world_msci_calendar_years |
| 13 | US stocks with dividends since 1871 (monthly averages): three falls of 40% or more (1929-32 -82%, 183 months peak to recovery; 2000-03 -42%, 74; 2007-09 -49%, 58), and 1973-74 at -39%; 6.7% of 3-year windows contain a 40% fall, 1.1% end 40% down, 15.4% end below their start; 5-year: 12.3%, 1.6%, 10.5% | Keel arithmetic in fall40.py on the repo's Shiller mirror | CEILING, MOVE2031, HALFKEPT | KNOWN | Same basis as the register's history column (NUMBERS 4) | US, not world; monthly averages smooth the lows (daily S&P fell about 57% in 2007-09) | Keel arithmetic (mirror UNVERIFIED against Yale, as NUMBERS 0) | no | fall40.py block us_drawdowns_since_1871 |
| 14 | The top depends on VT's value on the move day against its Jan 2028 cost, not on the low in between: each $1 VT gains or loses moves the unrounded top by about 53 cents (about $159 per 1% of VT's value) | fall40.py, breakeven block (completion.rule on the holdings) | CEILING, MOVE2031 | NICHE | Answers CANON D4's "top at the move date; its sensitivity to VT" | Linear only until rounding; the $5,000 steps make it lumpy | Keel arithmetic (MODEL) | no | fall40.py breakeven |
| 15 | A 40% fall from cost at the move: $95,000 to $105,000 (unrounded $108,250); funds pay $112,981; contribution $105,000 ($10,000 less); her flexibility $10,310 (7.5% after) or $8,922 (flat after); all ten paid; bottom unchanged | fall40.py scenario a, a_flat | CEILING, HALFKEPT, MOVE2031 | NICHE | The number for 3c's "what if shares fall before 2031" and Table 2's note | Rates held at today's forwards; the move modelled on 1 Jan 2031 | Keel arithmetic (MODEL); central reproduces 8i row 1 | no | fall40.py scenarios |
| 16 | A 40% fall after the move touches neither end nor the contribution: VT flat to the move then -40% gives $95,000 to $110,000 and $110,000, as VT flat then 7.5% does; only her flexibility falls ($17,184 to $8,922) | fall40.py scenarios b and b0 | HALFKEPT, MOVE2031, COSPONSOR | NICHE | Once inked at the move, the range is out of the market's reach (IPS l.15) | Her flexibility halves in exactly the years co-sponsors may cut (8f, card Q5e) | Keel arithmetic (MODEL) | no | fall40.py scenarios |
| 17 | A fall before the move is kept even if shares recover: 40% down at the move then back on the 7.5% path by 2033 leaves the top and contribution at $105,000; her flexibility returns to $21,347; Laura has $10,494 less than centrally | fall40.py scenario c | MOVE2031, CEILING | NICHE | The price of stating only owned money; it is paid only when a fall comes right before the move | A judge may call it selling low | Keel arithmetic (MODEL) | risk: IPS l.15 moves half before the meetings whatever the market, and l.17 makes a fall no reason to change, so the promised half moves at the low | fall40.py scenarios |
| 18 | In a recession with yields 2 points below forwards from the move, the 40% fall still gives $95,000 to $105,000 ($107,979); funds pay $111,684; the floor pays $102,256, still $7,256 above the stated bottom; all ten paid; what comes back from the extra Treasuries falls from $74,123 to $55,195 by 2042 (3 points: $107,846; $47,070) | fall40.py scenarios d and d3 (joint_stress conventions for what the funds pay) | CERTAINTY, RESERVE2033, MOVE2031 | NICHE | Lower rates cost Laura's returned money, not a payment or a stated end | Stylised parallel rate move; plan.run's own model says $112,605 for funds pay, $921 more | Keel arithmetic (MODEL) | no | fall40.py scenarios |
| 19 | The $5,000 steps: the central $115,000 needs VT up at least 2.5% over 2028-2031; flat VT gives $110,000, held down to a 29.0% fall; $105,000 down to 60.5%; $100,000 down to 92.0%; $95,000 even at zero; up 34% gives $120,000; the house chance VT is below +2.5% at the move is 26.8% | fall40.py breakeven; lognormal at J.P. Morgan's 7.5% and 17.88% | CEILING, MOVE2031 | NICHE | The monitoring signal for 3e: VT's value against its Jan 2028 cost tells Laura which step she is on | Rates at today's forwards; in the house model yield moves widen it (row 20) | Keel arithmetic (MODEL) | no | fall40.py breakeven, house.lognormal_exact |
| 20 | In the register's house model VT is 40% or more below cost at the move in 0.95% of futures (exact lognormal 0.94%); there the stated top is $105,000 at the median ($90,000 to $125,000 at 1 in 20, as yields vary), the bottom's spread is unchanged ($85,000 / $95,000 / $115,000) and the contribution is inside the range in every future | fall40.py house block (200,000 futures, seed 2033) | CEILING, CERTAINTY | NICHE | The bottom does not care what shares did; only yields at the 2028 purchase move it | Shares and yields drawn apart in the house model (NUMBERS 7) | Keel arithmetic (MODEL) | no | fall40.py house |
| 21 | The house model's tail is thinner than US history: on its own assumptions 4.2% of 3-year paths contain a 40% fall from a peak and 0.94% end 40% down, against 6.7% and 1.1% in US history | fall40.py (100,000 monthly paths, seed 4040) and row 13 | CEILING, PROCESS | NICHE | The report should not call 1 in 100 a history-based figure | Lognormal, independent months, no fat tails (card Q6 row 25) | Keel arithmetic | no | fall40.py house.monthly_lognormal_same_assumptions |
| 22 | In US history (rates at forwards) VT 40%+ below cost at the move happens in 20 of 1,770 windows, all purchases Oct 1928 to May 1930; stated top $100,000 to $105,000; lowest top in any window $100,000 | fall40.py history block | CEILING, MOVE2031 | KNOWN | Even 1929-32, the worst fall on record, leaves a range of $95,000 to $100,000 | US stocks stand in for VT | Keel arithmetic (MODEL) | no | fall40.py history |
| 23 | Named purchase months: VT bought Oct 2007 (the 2007 peak) gives a $110,000 top, because VT was back to 0.82 of cost by the move in Oct 2010; Mar 2000 and Aug 2000 give $105,000; Jan 1973 $110,000; Sep 1929 $100,000 | fall40.py history.named_vt_purchase_months | CEILING, PROCESS | NICHE | The 2008 crash, bought at its very top, cost one $5,000 step against flat shares | US stocks, monthly averages | Keel arithmetic (MODEL) | no | fall40.py history |
| 24 | A 40% fall after the move came in 25 US windows (1.4%): purchases Jun 1926 to Apr 1928, and Feb-Mar 2004 (move 2007, crash 2008-09); there the stated top was $110,000 to $135,000 (median $120,000) and only her flexibility fell (median $9,624) | fall40.py history block | HALFKEPT, MOVE2031, COSPONSOR | NICHE | Had Laura moved in early 2007, the 2008 crash would not have touched her range | US stocks; a short list of windows | Keel arithmetic (MODEL) | no | fall40.py history |
| 25 | In the conceit's terms a fall before the move rubs out only pencil (the top not yet inked and her flexibility); a fall after it moves nothing inked; the ten were inked in Jan 2027 and Jan 2028 and contain no share price | fall40.py ledger (no VT input); CONCEIT.md 3e "a market fall moves only pencil" | CERTAINTY, TWOREASONS, PRESENTATION | NICHE | Gives 3e's two-reasons sentence a tested number | At most five image sentences in the report; this is a note, not a sixth | Keel arithmetic; CONCEIT read | no | CONCEIT.md, fall40.py |

## (b) Cards

**Card 1. Global bear markets since 1900 (Taylor, 2019, GFD World index), with MSCI since 1970.**
- What is it? GFD's world index lists eleven global bear markets since 1900. Four fell 40% or more in nominal terms,
  each within 16-34 months: 1929-32 (-75.4%), 1973-74 (-42.4%), 2000-02 (-49.7%) and 2007-09 (-54.8%). Two stopped just
  short: 1912-21 (-39.4%, over nine years) and 1937-40 (-39.75%). The others ran -22% to -26%. On MSCI World with
  dividends, monthly, since 1970, the three deep ones were -40.0%, -46.3% and -53.7% (Cambridge Associates, 2019);
  MSCI's daily low for 2007-09 is 57.46% (gross, since 1987).
- Did it work? As a count it is robust: three independent series (GFD, MSCI through Cambridge Associates, DMS in real
  terms) name the same four modern episodes.
- How is Laura's case like it? VT tracks the same world market; a three-year window like 2028-2031 has held one of these
  falls in about one generation in four or five.
- How is it not? The plan does not care about the low; it cares about VT's value on one day, the move, against its
  January 2028 cost (Card 4). Of the four falls, only 1929-32 left a buyer from the start of a 3-year window 40% down at
  its end in US monthly data; on MSCI World calendar years only 2000-02 did (-41.5%).
- What Caplet takes: for 3e and Table 2's note, "a fall like 2000-02 or 2008" as the named stress, with the plan's
  answer (Card 4), never a probability rarer than 1 in 100 in prose (SKELETON, panel 2's density cut).

**Card 2. Countries crash often; the world less often (Barro and Ursúa, 2017; Jorion, 2003).**
- What is it? Across 30 countries and 3,037 country-years, Barro and Ursúa find 124 real falls of 40% or worse
  (a 4.9% chance a year of entering one) and 232 of 25% or worse, lasting 3.2 years on average. Jorion finds a GDP-
  weighted global index had a worst ten-year real loss of 54%, against 61% for the US and a median of 76% across the 30
  markets, and concludes that "across-country diversification is more effective than across-time diversification".
- Did it work? Both are peer-reviewed (Research in Economics 2017; Financial Management 2003) and widely cited.
- How is Laura's case like it? VT is the across-country diversification Jorion credits; Trading Note 3 says so ("one
  cheap fund diversifies Laura's stocks", TNA l.21).
- How is it not? Real returns, annual or no dividends; neither paper measures a world index's 3-year point-to-point
  falls, and Davis (2003) shows deep falls arrive together across countries (troughs within four months in 1974).
- What Caplet takes: one clause at most, for 2.3 or 3e: a world fund makes a crash rarer and shallower than any one
  market's, not impossible; the Treasuries, not VT's breadth, protect the promises.

**Card 3. How long recovery takes.**
- What is it? MSCI World regained its 2007 high 53 months after the March 2009 trough, and its 2000 high 40 months after
  the 2002-03 trough (Walter Scott, 2025); the price index took until February 2013 (Funds Society, 2025). MSCI USA took
  74 months after 1973-74 (MSCI blog). US stocks with dividends, monthly: 183 months from the 1929 peak, 74 from 2000, 58
  from 2007 (fall40.py). After inflation, most G-7 markets regained their 1972-73 level only in the 1980s or 1990s
  (Davis, 2003).
- Did it work? Recovery came every time in these series, but on clocks from two months (2020) to fifteen years (1929).
- How is Laura's case like it? From VT's purchase (Jan 2028) to the move (before the 2031 meetings) is about three years;
  a fall early in that window may recover in time, one late in it cannot.
- How is it not? Laura's plan does not wait: the move happens before the meetings whatever the market (IPS l.15).
- What Caplet takes: for 3e's "what to watch as 2031 approaches": VT's value against its January 2028 cost, not news of
  a crash; and for her flexibility, that recovery after 2031 helps only the half promised to no one (Card 5).

**Card 4. What a 40% fall before the move does to Laura's numbers (fall40.py, scenarios a, c, d).**
- What is it? The register's engine with VT at 0.6 times its January 2028 value on the move day: $95,000 to $105,000
  (unrounded top $108,250), funds pay $112,981, contribution $105,000, $7,981 above the top, her flexibility $10,310 on
  1 Jan 2033 if VT then grows 7.5% ($8,922 if flat). All ten payments are paid; the bottom and the $74,123 that comes back
  from the extra Treasuries by 2042 are unchanged. With yields 2 points lower from the move: the same stated range
  ($107,979 unrounded), funds pay $111,684, $55,195 back from the extra Treasuries; all ten paid.
- Did it work? The central case reproduces NUMBERS 8i row 1 and NUMBERS 4's deletion test to the cent (checks in the
  results file).
- How is Laura's case like it? This is IPS l.15's "decrease the top" with a size: one $10,000 step pair down, $115,000 to
  $105,000; the extra above the bottom halves ($20,000 to $10,000), TNA l.21's "A fall can shrink the extra".
- How is it not? The fall is a point on one date; real falls have paths. A fall that recovers before the move costs
  nothing; one after the move costs only her flexibility (Card 5).
- What Caplet takes: for 3c, one sentence of notes: "if world shares were 40% below their January 2028 cost when half
  moves, the top would be about $105,000, the bottom still about $95,000, and every payment unchanged". For Table 2's note
  or a row (Exhibit 3 already has shares 1-in-20 low: $95,000 to $110,000).

**Card 5. A fall after the move (fall40.py, scenario b; US windows from early 2004).**
- What is it? VT flat to the move then 40% down by January 2033 gives exactly the range and contribution of VT flat then
  up 7.5% a year: $95,000 to $110,000 and $110,000. Only her flexibility moves, $17,184 to $8,922. In US history 25
  windows saw a 40% fall after the move, including purchases in Feb-Mar 2004 (move 2007, crash 2008-09); there the stated
  top was $110,000 to $135,000 and her flexibility fell to a median of $9,624.
- Did it work? It is the IPS's design working: "the other half will move into Treasuries, so whatever figure you choose
  is money you already own" (l.15).
- How is Laura's case like it? The 2008 crash, had it come after the move, would not have touched what Laura told
  co-sponsors.
- How is it not? Her flexibility halves in exactly the years the IPS expects co-sponsors to cut (l.9; NUMBERS 8f; card
  Q5e), so the money for "a co-sponsor falling short" is smallest then.
- What Caplet takes: for 3b: the range is out of the market's reach after the move; her flexibility is not, and the
  report says so (8f's honest line).

**Card 6. The steps: how far VT can fall before each $5,000 goes (fall40.py breakeven; CANON D4).**
- What is it? Each $1 VT gains or loses before the move moves the unrounded top by about 53 cents. The stated top is
  $115,000 only if VT is up at least 2.5% from its January 2028 cost at the move (0.84% a year); flat shares give
  $110,000, which holds to a 29.0% fall; $105,000 holds to 60.5%; $100,000 to 92.0%; $95,000 is stated even if VT is
  worthless. Up 34% gives $120,000. On J.P. Morgan's 7.5% and 17.88%, VT is below +2.5% at the move about 27% of the time.
- Did it work? It is exact on the register's engine at today's forwards (the unrounded top is linear in VT's value).
- How is Laura's case like it? CANON D4 asks for "top at the move date; its sensitivity to VT"; this is it.
- How is it not? Yield moves before 2028 and before the move also shift the steps (the house model's spread, row 20).
- What Caplet takes: for Table 3 (monitoring), one signal row: VT's value against its January 2028 cost; what it changes:
  which $5,000 step the top lands on; what it never changes: the ten payments and the bottom; not a reason to change the
  plan (l.17). And for 3c: "about $115,000" is the central figure, and it needs shares only to hold their ground.

**Card 7. The move sells half at whatever price the day gives (coherence; scenario c).**
- What is it? If VT is 40% down at the move and then recovers to its 7.5% path by 2033, the top and contribution stay at
  $105,000 while her flexibility recovers to $21,347; Laura ends $10,494 below the central case.
- Did it work? Yes, as designed: the IPS chooses owned money over a hoped-for recovery (l.15) and names no market fall as a
  reason to change (l.17; CANON A34: "Evaluate, never add a rule or trigger").
- How is Laura's case like it? The case warns that promising more than she can contribute "could damage her
  credibility"; a top stated on unowned shares would be such a promise.
- How is it not? A judge may still see "selling after a crash" and ask why not wait. The IPS gives no discretion, and the
  report must not invent one.
- What Caplet takes: for 3c or the Team Reflection (only if a real event supports it): the cost of the rule in its worst
  timing, $10,000 off the contribution, set beside what it buys, a range co-sponsors can rely on. Never "the plan
  protects against crashes" (it protects the promises, not the size of the top).

## (c) What would surprise a judge

- Buying VT at the very top in October 2007 and moving three years later would have cost the plan one $5,000 step
  against flat shares ($110,000 top), because what matters is VT's value on the move day (0.82 of cost in October 2010),
  not the March 2009 low.
- The central $115,000 needs world shares only to hold their ground (+2.5% in three years); a 40% fall takes it to
  about $105,000, and it would take a 92% fall to reach $100,000. The bottom, $95,000, does not move at all.
- A 40% crash after the move leaves the range and the contribution exactly where they were; the 2008 crash, had it come
  in that window, would not have changed a word Laura said to co-sponsors.
- The ten payments contain no share price at all: the engine's payment ledger takes no input from VT.
- The 40% falls that history remembers (four since 1900) are drawdowns; a 40% loss from purchase to a fixed date three
  years later is about four to six times rarer (US 1.1% against 6.7% of windows; house model 0.94% against 4.2%).

## (d) Gaps

- World recovery times are from a fund manager and a news summary (row 10), not read in MSCI's own monthly data; MSCI's
  end-of-day tool needs an interactive session.
- MSCI World annual returns before 2012 come from Wikipedia's table ("citation needed"); only 2012-2025 were matched to
  MSCI's factsheet. A second compilation (alphacubator, net) agrees to about a point a year but was not used.
- GFD's post does not say whether its world index includes dividends; the 1929-32 world recovery time was not found.
- Only the UBS 2026 public summary was read, not the full Yearbook's drawdown chapter; the 2024 summary was read in
  search excerpts on two mirrors.
- Consensus (peer-reviewed search) was unavailable this run (monthly free usage exhausted, resets 1 Dec); peer-reviewed
  sources were found by web search instead.
- The scenarios hold the move on 1 Jan 2031 and treat the fall as a point on that day; a fall in the weeks just before
  the first meeting is the same arithmetic but not modelled separately. The recession variant moves yields in parallel
  by a fixed 2 or 3 points; the joint replay (NUMBERS 8i) remains the history-based version.
- No world monthly series in the repo, so US stocks stand in for VT in history, as everywhere in the register.

## (e) Draft NUMBERS block

For the lead to check; not entered in NUMBERS.md.

### 8p. A 40% fall in world shares before or after the 2031 move (Sun 15 Nov, MODEL; card Q6c)
- **Script and rerun:** `numbers/fall40.py`, results `numbers/results_fall40_2026-11-15.json`. From the repo root,
  `python3 -I keel/final_report/numbers/fall40.py` (about 9 seconds). Imports engine, plan and completion; changes no
  other script and writes no other file.
- **Basis:** the Tue 10 Nov register (design H_plain with the fee cushion, the range rule on the fund's holdings, Keel's
  reading of "most"), rates at today's forwards unless a row says otherwise; the move on 1 Jan 2031. "Down 40%" = VT with
  dividends, before its 0.06% fee, at 0.6 times its value on the earlier date.
- **Check:** the central row reproduces 8i row 1 to the cent and section 4's deletion test ($95,000; $103,178; $8,178).

| World (VT; rates) | Stated range (unrounded top) | What the funds pay | Contribution | Above the top | Her flexibility, 1 Jan 2033 | Ten payments | Back from the extra Treasuries by 2042 |
|---|---|---|---|---|---|---|---|
| Central: 7.5% a year; forwards | $95,000 to $115,000 ($118,443) | $123,476 | $115,000 | $8,476 | $21,347 | All paid | $74,123 |
| 40% below Jan 2028 cost at the move, then 7.5% a year | $95,000 to $105,000 ($108,250) | $112,981 | $105,000 | $7,981 | $10,310 | All paid | $74,123 |
| The same, then flat to 2033 | $95,000 to $105,000 ($108,250) | $112,981 | $105,000 | $7,981 | $8,922 | All paid | $74,123 |
| Flat to the move, then 7.5% a year (baseline for the next row) | $95,000 to $110,000 ($114,598) | $119,517 | $110,000 | $9,517 | $17,184 | All paid | $74,123 |
| Flat to the move, then 40% down by Jan 2033 | $95,000 to $110,000 ($114,598) | $119,517 | $110,000 | $9,517 | $8,922 | All paid | $74,123 |
| 40% down at the move, back on the 7.5% path by Jan 2033 | $95,000 to $105,000 ($108,250) | $112,981 | $105,000 | $7,981 | $21,347 | All paid | $74,123 |
| 40% down at the move; yields 2 points below forwards from the move | $95,000 to $105,000 ($107,979) | $111,684 | $105,000 | $6,684 | $10,310 | All paid | $55,195 |
| 40% below the 7.5% path at the move (25.5% below cost), then 7.5% | $95,000 to $110,000 ($110,557) | $115,357 | $110,000 | $5,357 | $12,808 | All paid | $74,123 |
| VT worthless at the move (section 4's deletion test) | $95,000 ($98,729) | $103,178 | $95,000 | $8,178 | $0 | All paid | $74,123 |

- **The steps (today's forwards):** each $1 VT gains or loses before the move moves the unrounded top by about $0.53.
  Stated top $115,000 needs VT at least 2.5% above its January 2028 cost at the move; $110,000 holds down to a 29.0%
  fall; $105,000 to 60.5%; $100,000 to 92.0%; $95,000 at zero; $120,000 needs +34.0%. On J.P. Morgan's 7.5% and 17.88%,
  VT is below +2.5% at the move in 26.8% of futures (lognormal arithmetic).
- **How often (house model, 200,000 futures, seed 2033):** VT 40% or more below cost at the move in 0.95% (exact
  lognormal 0.94%); there the stated top is $90,000 / $105,000 / $125,000 (1 in 20 low / median / 1 in 20 high), the
  bottom $85,000 / $95,000 / $115,000 (as in all futures) and the contribution inside the range in every future. A 40%
  fall after the move: 0.49% of futures; contribution median $115,000; her flexibility median $9,898.
- **How often (US stocks since 1871, rates at forwards, 1,770 windows):** VT 40%+ below cost at the move in 20 windows
  (1.1%), all purchases Oct 1928 to May 1930; stated top $100,000 to $105,000. A 40% fall after the move in 25 windows
  (1.4%; purchases Jun 1926 to Apr 1928 and Feb-Mar 2004); stated top median $120,000; her flexibility median $9,624.
- **Named purchase months (US stocks):** Oct 2007 $110,000 top (VT 0.82 of cost at the move); Mar 2000 and Aug 2000
  $105,000; Jan 1973 $110,000; Sep 1929 $100,000.
- **Drawdowns against point-to-point falls:** on the house model's own assumptions, month by month (100,000 paths, seed
  4040), 4.2% of 3-year paths contain a 40% fall from a peak, 0.94% end 40% below their start; US stocks since 1871
  (monthly averages): 6.7% and 1.1%. The plan's top responds only to the second.
- **What the report may say (notes, not wording):** a 40% fall in world shares before half moves lowers the top Laura can
  state from about $115,000 to about $105,000 and leaves the bottom, about $95,000, and every payment where they were; a
  fall after the move changes only her flexibility. Never "the plan is protected from crashes"; never a probability rarer
  than 1 in 100 in prose.
- **Limits:** a fall is a point on 1 Jan 2031; the recession row moves yields in parallel by a fixed 2 points (3 points:
  top $107,846, funds pay $111,045, $47,070 back); US stocks stand in for VT in history; stocks and yields are drawn apart
  in the house model (section 7).

## Sources (APA 7)

All accessed 14-15 Nov 2026 (Sydney). "Excerpt" = read through a search or fetch excerpt, not the whole document.

- Barro, R. J., & Ursúa, J. F. (2017). Stock-market crashes and depressions. *Research in Economics, 71*(3), 384-398.
  Read as NBER Working Paper No. 14760 (rev. 2011), https://www.nber.org/system/files/working_papers/w14760/w14760.pdf,
  and https://www.nber.org/papers/w14760 (excerpt; published version confirmed on the NBER page).
- Cambridge Associates. (2019, September). *Managing portfolios through equity market downturns: Market history*.
  https://www.cambridgeassociates.com/wp-content/uploads/2019/09/Market-History.pdf (excerpt).
- Davis, E. P. (2003). Comparing bear markets: 1973 and 2000. *National Institute Economic Review, 183*, 78-89.
  https://www.ephilipdavis.com/davis-final.pdf (excerpt).
- Dimson, E., Marsh, P., & Staunton, M. (2009, March 11). *Keeping faith with stocks*. London Business School.
  https://www.london.edu/news/keeping-faith-with-stocks (search excerpt).
- Dimson, E., Marsh, P., & Staunton, M. (2024). *UBS Global Investment Returns Yearbook 2024: Summary edition*. UBS.
  Mirror: https://mebfaber.com/wp-content/uploads/2024/05/ubs-global-investment-returns-yearbook-2024-summary-edition-3.pdf
  (search excerpt; US drawdowns, Figure 36).
- Dimson, E., Marsh, P., & Staunton, M. (2026). *UBS Global Investment Returns Yearbook 2026: Public summary edition*.
  UBS. https://www.ubs.com/content/dam/assets/wm/static/cio/documents/giry2026-summary-public.pdf (full text fetched;
  sections 7-8 read).
- Funds Society. (2025, July 1). *Memory of a quarter century: How long it has taken markets to recover from each
  financial crisis*. https://www.fundssociety.com/en/news/markets/memory-of-a-quarter-century-how-long-it-has-taken-markets-to-recover-from-each-financial-crisis
  (excerpt; secondary).
- Jorion, P. (2003). The long-term risks of global stock markets. *Financial Management, 32*(4).
  https://people.duke.edu/~charvey/Teaching/BA453_2004/Jorion_The_long_term.pdf (excerpt; journal details from
  https://ideas.repec.org/a/fma/fmanag/jorion03.html).
- MSCI. (2026a). *MSCI World Index (USD)* [Index factsheet, net returns, as of October 30, 2026].
  https://www.msci.com/documents/10199/255599/msci-world-index-usd-net.pdf (read in full).
- MSCI. (2026b). *MSCI World Index (USD)* [Index factsheet, gross returns, as of October 30, 2026].
  https://www.msci.com/documents/10199/178e6643-6ae6-47b9-82be-e1fc565ededb and
  https://www.msci.com/documents/10199/255599/msci-world-index.pdf (excerpt).
- MSCI. (2026c). *MSCI World Index (USD)* [Index factsheet, price returns, as of October 30, 2026].
  https://www.msci.com/documents/10199/255599/msci-world-index-usd-price.pdf (excerpt).
- MSCI. (n.d.). *Time in the markets beats timing the markets* [Blog post].
  https://www.msci.com/research-and-insights/blog-post/time-in-the-markets-beats-timing-the-markets (search excerpt).
- Shiller, R. J. (n.d.). *U.S. stock markets 1871-present* [Data set, ie_data.xls]. Yale University. Read through the
  repo mirror `keel/models/data/shiller_monthly.csv` (UNVERIFIED against Yale, as NUMBERS 0).
- Taylor, B. (2019, August 19). *Wars and financial panics: Global bear markets in the twentieth century*. Finaeon
  (Global Financial Data). https://finaeon.com/wars-and-financial-panics-global-bear-markets-in-the-twentieth-century
  (read in full).
- Walter Scott & Partners. (2025, June 26). *Downside protection: The other side of the return equation*.
  https://www.walterscott.com/research/articles/downside-protection-the-other-side-of-the-return-equation (excerpt).
- Wikipedia contributors. (2026). MSCI World. In *Wikipedia*. https://en.wikipedia.org/wiki/MSCI_World (table of gross
  annual returns 1970-2025; data before 2012 UNVERIFIED at MSCI).
- Engine inputs (J.P. Morgan 2027 LTCMA, 7.50% and 17.88%; the 6 Nov 2026 Treasury curve): as cited in NUMBERS 0.
