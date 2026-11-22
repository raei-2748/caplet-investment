# Every figure in the argument tree, re-derived a second way (Sun 22 Nov 2026)

OVERDRIVE_PLAN Sunday 22 analysis task. MODEL and Keel arithmetic; notes, not report text. No other file was changed:
NUMBERS.md, ARGUMENT_TREE.md and every script and results file are as they were.

**What was checked.** Every dollar figure, percentage, count and dated figure in `ARGUMENT_TREE.md` sections 1-5, as
the file stood on Sun 22 Nov 2026 (a concurrent edit that evening reworded aha 8 and 3d; no figure checked here moved).
Citation years (Leibowitz 1986 and the like), aha-test scores (4.7, 3.3 / 3.7) and figures listed under "Left out" are
not plan figures; the left-out ones that the register holds are checked in one row each.

**How (the second routes).**
- **Fresh runs against the results files.** Fourteen scripts were run, read-only, in a scratch copy of `numbers/` whose
  inputs link back to the repo: `run_numbers`, `reserve`, `first_plan`, `break_test`, `fund_exit`, `one_fund`,
  `forecast_blocks`, `price_history`, `fall40`, `taiwan_joint`, `kept_half`, `most_check`, `range_rule`, `kept_share`.
  Every one of their fourteen results files came back the same, leaf by leaf (more than 10,000 values); only the
  run-time fields differ.
- **An independent bootstrap of the 6 Nov 2026 curve** (`daily-treasury-rates_2026-11-06.csv`), written without the
  engine: tenors under a year read as zero-coupon yields, and continuously compounded zero rates interpolated linearly
  between grid points (the engine interpolates log discount factors). The same code priced FRED's daily curves since
  2007 and the WInS book's DV01.
- **Hand arithmetic** from the register's own inputs: sums of parts against totals, the range rule worked by hand, and
  ratios.
- **Repo data files read again:** card Q131's monthly Taiwan cost and NT$ series, card Q85's MSCI ACWI checkpoints,
  card Q148's Census series and FRED DGS1MO-DGS30.
- Scratch scripts (scratchpad, not in the repo): `second_way/indep_curve.py`, `book_dv01.py`, `cheap_days.py`,
  `cmp_json.py`.

**Result.** 66 figures checked:
- 57 agree, 30 exactly and 27 to rounding;
- 3 differ beyond rounding in the tree, and a fourth disagreement sits in the register's own words (8e), where the tree
  is right;
- 1 agrees only within a model approximation (the book's DV01);
- 5 have no second route.

Seven wording or basis flags follow the disagreements. Eleven groups of figures in the tree have no NUMBERS section at
all (listed after the flags).

## Disagreements

1. **The register's 8e, not the tree: "one day from June 2007".** 8e's row "Days from June 2007 to August 2026: one:
   Thu 19 Oct 2023", its "Last run of days before 2026: June 2007" and its "a single day since June 2007" are wrong.
   The engine's own method (`engine.Curve` on FRED's daily curves, the route `price_history.py` uses) finds 13 more
   closes under $300,000 in July 2007, from 2 to 19 July (19 Jul 2007: $298,426). The independent bootstrap finds the
   same 13. From 1 Aug 2007 to 31 Aug 2026 both find exactly one, 19 Oct 2023 ($299,293 engine, $299,309
   independent). So **the tree's "from August 2007" is right** (aha 3 and section 2's table). 8e should read "from
   August 2007", or "after 19 July 2007". `results_price_history.json` is not wrong: it records only the last day
   before 2026 (2023-10-19); the monthly flat series' last month, 2007-06, is where "June" came from.
2. **"41% down" in the 2000-2003 replay (aha 9; 3e).** The tree pairs it with building costs "about 18% in NT$, 27% in
   US$", which run from the January 2003 meetings to December 2004 on start-of-month dates. Card Q131's file gives
   +18.4% NT$ and +27.2% US$ (exact). On the same start-of-month calendar (the Dec 1999 close to the Dec 2002 close,
   ACWI price to Dec 2000 and gross after), card Q85's checkpoints give world shares **-42.1%**. The 41% is the
   end-of-month figure (Jan 2000 to Jan 2003: -40.6%). Say "about 42%" beside the start-of-month cost figures, or "41%
   to 42%". FACTS_PLAIN version 5 l.103 has the same 41%.
3. **The date of the 25-basis-point check (branch 1, 2.5).** The tree says "the 25-basis-point price check of 29-30
   September (every bond's yield within 0.25 points of the official curve)". The register (8m) dates the check every
   bond passed **5 Oct**: -10 to +6 basis points, and 2.6 to 8.8 at the fills. On 29-30 September two bond quotes sat
   111 and 92 basis points off the curve (card Q13; store H9-180), and that is when the team made the rule. No figure is
   wrong, but the date and the claim do not belong together. Say "the rule of 29-30 September, met at the 5 October
   check and at every fill".
4. **"In 2027 the payments' money is about $39,000 short" (section 1).** $39,162 is January 2028 money: the first slice
   of the 2028 deposit. Measured in 2027 (1 Jan 2027 money) the gap is **$37,499** ($337,499 - $300,000). Both are
   right on their own basis. The sentence dates the gap 2027 but gives the 2028 figure, so date it 2028 or say "the
   first $39,162 of the 2028 deposit".

**Within a model approximation only:** the book's DV01, "about $159" (row 19), comes out about $155 here, 3% lower. Both
routes model the iBond funds approximately. **No second route:** the ended funds' "within about 0.07%" (row 59) rests
only on card Q3c's own values.

## Wording and basis flags (the figures agree)

- **"About a quarter" for the 24.9% cover (3b, 3e).** Register 8u's words for 3e and the lead's call of Sun 22 Nov
  evening (NUMBERS section 9) print "about 25%, if shares earn the 7.5% a year assumed", in one form, and never "about
  a quarter". The tree also uses "about a quarter" for two other quantities: 26.1% of the deposit (3a) and IBTM's 24.3%
  (2.3). That breaks WORDS' rule of one phrase for one quantity.
- **$502,605 (3a).** This is the no-fee basis: $445,405 + $57,200. Under the standard's own test, with the bill fund's
  0.15%, $500,000 is paid and $1,177 is left. With that fee and 0.5% fund costs it is exactly $500,000.
- **About $4,600 from an early fund end (3e).** The tree, following ATTACKS D2, says the gap is "met from her
  flexibility". The register's dated line under section 0 says it is "met only from interest the waiting cash earns".
  The figure agrees; who covers it does not.
- **"About 1 in 7 against none" (3f).** "None" is the central case. With a $75,000 deposit the house model has 70 of
  200,000 paths short (8s). "At today's rates" in the tree covers this.
- **"At about 5% too" (3c).** True for 5% central (unrounded top $115,811). At 5% with valuations easing, 8v's top
  states **$110,000** (unrounded $114,998).
- **"About 11 of 100" (3c).** This is the house model (10.6%). The same results file's central-path variant gives 20.1%
  for a year early. Quote only the house figure, as the register does.
- **"About 17 separate two-year spans in four episodes" (3e).** The 17 non-overlapping spans cover the whole record
  (1991-2026). The four episodes hold the 20 windows above 28%. The clause reads as if the 17 sat inside the four.

## Figures with no NUMBERS section

- **The reconciliation under Table 1:** book x 1.5 = $293,830, $109,148 and $39,787; the plan's $339,162; and "about
  73% / 27%". These are in `research/attacks_2026-11-20/NUMBERS_ANSWERS.md` (attack 3, Keel arithmetic, "none is in the
  register until the numbers owner adopts it"). The inputs are in 8g, section 0 and section 4.
- **$502,605:** NUMBERS_ANSWERS attack 28; its parts are in 8h.
- **The book's DV01, about $159, and the liability's, about $200:** NUMBERS_ANSWERS attack 12. Section 1 has $300 and
  $234 at full size.
- **-41%, +18% NT$ and +27% US$:** card Q85.
- **The four episodes (1991-93, 2002-05, 2006-08, 2019-21) and the 17 spans:** card Q210. 8q has the 28.0% and $32,191,
  and its own "four episodes" are a different list, of failing VT windows.
- **-7.8% (writers' 2009 receipts):** card Q148 row 5 and card Q206.
- **"About $300 of expected return for each $5,000":** D15's restatement. 8o has $5,267 ("about $5,300").
- **Two custodians:** card Q78. 8t has one broker.
- **WInS listing no bond maturing Feb 2031 to Feb 2036, and no iBond fund ending 2037-2043:** CANON B21 and B38.
- **Lehman's $10 million to Spelman becoming $3 million:** card Q200.
- **Artists Rep's "$500,000 operating seed funds":** card Q204.

## The full table

Result: **exact** = the same to the dollar or figure printed; **rounding** = equal once rounded as the tree rounds;
**differs** = beyond rounding; **approx.** = within a model approximation; **no route** = no second route exists. Rows
are numbered in tree order. A figure that recurs (in section 4's ahas or section 5's threads) is checked once, at its
first appearance.

| # | Figure | Where in the tree | Register | First route | Second route | Result | Note |
|---|---|---|---|---|---|---|---|
| 1 | $450,000 in two deposits ($300,000 in 2027, $150,000 in 2028) | 1 | Case; 0 | Case input | $300,000 + $150,000 | exact | |
| 2 | Ten fixed $50,000 payments, 2033-2042 | 1 | Case | Case input | Count of years | exact | |
| 3 | "In 2027 ... about $39,000 short" | 1 | 2 ($39,162) | Engine, Jan 2028 money | $2,388 + $36,774 = $39,162; in 1 Jan 2027 money $337,499 - $300,000 = $37,499 | differs (basis) | Disagreement 4 |
| 4 | Every share at zero: the ten paid; $95,000 | 2; 3e; 4 | 4, deletion test | Engine: floor pays $102,365; fresh run 95,000 | Rule by hand: $81,244 x 1.207415 x 0.995 = $97,605, rounded down to $95,000 | exact | |
| 5 | The 0.5% margin | 2; 3c | 0 | Input | n/a (definition) | no route | |
| 6 | One day from August 2007 to August 2026 (19 Oct 2023) | 2 table; aha 3 | 8e | `price_history.py` (fresh run equal) | Own bootstrap on FRED: one day from 1 Aug 2007 ($299,309), 13 more in July 2007 (engine's method also) | exact (tree) | Register 8e's "June 2007" is wrong; disagreement 1 |
| 7 | About three-quarters smaller | 2; 2.3; 3e; aha 2; 5 | 5; 8u (73.9%) | `break_test.py` (fresh) | 1 - $39,162 / $150,000 = 73.89% | rounding | Only "at today's rates" |
| 8 | About $95,000 to $115,000 | 2; 3c; many | 4 | Engine; fresh run | Rule by hand: bottom $97,605; top ($98,096 + $18,349 x 1.070113) x 0.995 = $117,142, each rounded down | exact | Unrounded $97,605 and $117,142 exact |
| 9 | Plan built at $450,000, scaled to $300,000 | 2.1 | 8m | Team record | 300 / 450 = two-thirds | exact | |
| 10 | Ten Treasury holdings, five funds, one sponsor, one broker | 2.1; 2.3 | 8g; 8t | 8g table | Count: 5 funds + 5 bonds | exact | Two custodians: card Q78 only |
| 11 | No WInS bond Feb 2031 to Feb 2036; no iBond fund ending 2037-2043 | 2.1 | CANON B21, B38 | Team record; iShares brochure | None (WInS may not be opened; the brochure is not in the repo) | no route | No NUMBERS section |
| 12 | Three dated steps: Jan 2027, Jan 2028, Jan 2031 | 2.2 | 4 (modelled dates) | IPS | n/a | exact | |
| 13 | IBTM about a quarter of all she holds in late 2032, 24.3% at NAV | 2.3 | 8w | `one_fund.py` (fresh: 0.24275) | $142,553 / $587,231 = 24.28% | rounding | The 30 Nov 2032 row ("for scale"); 24.8% on 1 Jan 2032, 25.9% after the move |
| 14 | One-person artists' and writers' receipts -7.8% in 2009 | 2.3 | none | Card Q148 row 5 | Q148 CSV: 11,808,168 / 12,811,801 - 1 = -7.83% | rounding | No NUMBERS section |
| 15 | Book x 1.5: $293,830 / $109,148 / $39,787 | 2.1 note | none (NUMBERS_ANSWERS att. 3) | Keel arithmetic | 8g at cost: ladder ($97,489.95 - $72,765.65 + nine rows) = $195,886.53, x 1.5 = $293,829.79; floor $109,148.47; VT $39,786.92 | rounding | |
| 16 | Plan in Jan 2028: $339,162 / $81,244 / $29,594 | 2.1 note | 4 ($81,244, $29,594); $339,162 none | Engine | $300,000 + $2,388 + $36,774 = $339,162; 0.733 x $110,838 = $81,244.3; the three add to $450,000 | exact | $339,162 mixes 2027 and Jan 2028 money (both "at cost") |
| 17 | What is left splits about 73% floor, 27% VT | 2.1 note | 0 (73.3%) | Frozen book split | $109,148 / $148,935 = 73.29%; $81,244 / $110,838 = 73.30% | rounding | |
| 18 | 25-bp check of 29-30 Sep, every bond within 0.25 points | 2.5 | 8m (5 Oct check) | Team record | 8m: -10 to +6 bp on 5 Oct; fills 2.6-8.8 bp; on 29-30 Sep two quotes 111 and 92 bp off | differs (date) | Disagreement 3 |
| 19 | Book DV01 about $159; liability about $200 | 2.5 | none (att. 12); 1 has $300 | Scratch model | Liability: $299.68 x 2/3 = $199.8 (own bootstrap $299.64). Book: own bootstrap, WInS units and faces, each fund as one bond at its holdings' average maturity: ten rungs about $155 (floor stand-in about $36, against $38) | approx. | Within 3%; both model the funds approximately |
| 20 | $302,287, the ten on the plan's instruments | 2.1; 5 | 1 | Engine (fresh equal) | Own bootstrap, the ten at 1 Jan 2027: $301,506 (register $301,544) + funds' fee $743 (section 3; hand from its fee column, about $746) = $302,249 | rounding | -$38 = interpolation method (0.013%) |
| 21 | $2,287 above the first deposit | 2.1 | 1 | Engine | $302,287 - $300,000 | exact | |
| 22 | $2,388 in January 2028 money | 2.1; 3a | 2 | Engine | Own bootstrap: 2027 forward 4.344%; $2,287 x e^(f x 365/365.25) = $2,388.46 | rounding | |
| 23 | Left out: the 94.8% and 62.8% | 3b | 4 | Engine | Fresh run: 0.947555 and 0.627805 | exact | Not printed |
| 24 | Replay: 585 starting months since 1962; more often than not since 1981; 55.6% not printed | 3a | 2 | `run_numbers.py` (fresh equal) | (39 + 286) / 585 = 55.56%; 39 / 228 = 17.1%; 286 / 357 = 80.1% | exact | |
| 25 | $39,162, about a quarter of the deposit | 3a; aha 5 | 2; 4 | Engine | $2,388 + $36,774; $39,162 / $150,000 = 26.11% | exact | "A quarter" also names 24.3% and 24.9% (flags) |
| 26 | $2,388 top-up and $36,774 extra Treasuries | 3a | 2 | Engine | Sum check (row 25); backstop $35,213 (1 Jan 2027) carried a year | exact | |
| 27 | About $46,600 in 1 Jan 2033 money | 3a | 2; 8h ($46,566) | Engine | Own bootstrap: $75,934 on 1 Jan 2042 discounted to 1 Jan 2033 = $46,567 | rounding | |
| 28 | Pays $502,605 at zero interest against $500,000 | 3a | none (att. 28); parts in 8h | Keel arithmetic | $445,405 + $57,200 = $502,605; also $500,000 + $2,604 left = $502,604 | rounding | No-fee basis (flags) |
| 29 | About $445,700, 111.7% of $399,089 | 3a | 8h | Engine (`reserve.py` fresh equal) | Own bootstrap: the ten valued 1 Jan 2033 at forwards = $399,088; $399,089 + $46,566 = $445,655; ratio 111.67% | rounding | |
| 30 | $110,000 against $115,000 (like for like) | 3b; aha 6 | 4 (all-Treasury) | Engine (fresh: 110,000) | $133,158 x (1 - $20,486 / $139,653) = $113,625, rounded down to $110,000; payout $139,653 - $20,486 = $119,167 (register $119,166) | exact | |
| 31 | About $300 of expected return per $5,000 made certain | 3b | 8o ($5,267) | Keel arithmetic | $5,267 - $5,000 = $267 | rounding | "About $270" is closer; no "$300" in the register |
| 32 | About $21,200 (half kept) | 3b | 4 ($21,179) | Engine | $18,349 x 1.075^2 x 0.9994^2 = $21,179 | rounding | |
| 33 | About $28,700 with anything above the top | 3b | 4 ($28,682) | Engine | $21,179 + ($102,365 + $20,138 - $115,000 = $7,503) | rounding | |
| 34 | About $9,600 in 1 future in 20 | 3b | 8f ($9,621) | `kept_half.py` (fresh equal) | None independent (house model only) | rounding | |
| 35 | A rise of about a quarter in the cost of her share | 3b; 3e | 8u (24.9%) | `break_test.py` (fresh: 0.24941) | $28,682 / $115,000 = 24.94% | rounding | Words conflict (flags) |
| 36 | A top of at least $100,000 in about 91 of 100 | 3c; aha 1 | 4 (91.2%) | Engine (fresh: 0.912145) | None beyond the fresh run (house model) | rounding | |
| 37 | $115,000 in about 57 of 100 | 3c; aha 1 | 4 (57.2%) | Engine (fresh: 0.572215) | Partial: with rates held at forwards, lognormal arithmetic gives 64.6% (8p's 35.4%); the house figure is lower because yields also move the bottom | rounding | |
| 38 | The 6 November 2026 curve | 3c | 0 | Curve file | File date | exact | |
| 39 | Rounded down to $5,000; the fund pays out about 15 Dec 2032 | 3c | 0 | Rule; iShares | n/a | exact | |
| 40 | A top named a year early exceeds the move in about 11 of 100 | 3c; aha 7 | 4 (10.6%) | `range_rule.py` (fresh: 0.10602) | None beyond the fresh run | rounding | Central-path variant 20.1% (flags) |
| 41 | Top states $115,000 for returns of 4% to 10%, and at about 5% | 3c | 4; 8v | Engine (fresh) | Top = $97,605 + $15,727 x (1 + r)^3: $115,811 at 5%; interpolating 4% ($115,296) and 6% ($116,336) gives $115,816 | exact | 5% with valuations easing states $110,000 (flags) |
| 42 | Her whole commitment, about $615,000 | 3d | 8w | Keel arithmetic | 10 x $50,000 + $115,000 | exact | |
| 43 | $50,000 a year, 2033-2042, and $115,000 | 3d; 5 | Case; 4 | | Counts; row 8 | exact | |
| 44 | "At least $95,000" from January 2028 | 3d; 5 | 4 (bottom fixed Jan 2028) | Engine | Row 4 | exact | |
| 45 | Lehman's $10 million to Spelman became $3 million | 3d; aha 8 | none (card Q200) | Card | None | no route | Outside fact |
| 46 | "$500,000 operating seed funds for first two years" | 3d | none (card Q204) | Card | None | no route | Outside fact |
| 47 | Nothing by 31 March 2028; a payment more than five business days late | 3e | 8u row 1; Table 3 | Definitions | n/a | exact | |
| 48 | Fund costs beyond about 2% | 3e | 3; 8u (2.32%) | Engine | 1 - $115,000 / $117,731 = 2.32% | rounding | |
| 49 | At most about $4,600 if cash earned nothing (early end) | 3e | 3 ($4,589) | `fund_exit.py` (fresh equal) | $115,000 - $110,411 = $4,589 | rounding | Who covers it (flags) |
| 50 | Four times since 1991, 28% or more dearer in US$ within two years | 3e | none (card Q210); 8q (28.0%) | Card Q210 | Q131 CSV: 20 of 406 two-year windows at 28% or more, in four runs starting Jan-May 1991, Mar 2002-May 2003, Feb-Aug 2006 and Jun-Sep 2019 (ending by May 1993, May 2005, Aug 2008, Sep 2021) | exact | |
| 51 | Episodes 1991-93, 2002-05, 2006-08, 2019-21 | 3e | none (card Q210) | Card | As row 50 | exact | |
| 52 | About $32,200 on her $115,000 | 3e | 8q ($32,191) | Engine | 0.28 x $115,000 = $32,200; with the 1-in-20 rise of 27.99%, $32,189 | rounding | More than $28,682: true |
| 53 | About 17 separate two-year spans | 3e | none (card Q210) | Card | 430 months / 24 = 17 non-overlapping spans | exact | Wording (flags) |
| 54 | The ten's NT$ value moves (fixed US$) | 3e | 8d | Case | n/a | exact | |
| 55 | A deposit between nothing and about $39,000 | 3e (Table 3) | 2; 5 | Engine | Row 25 | rounding | |
| 56 | Late-2032 fund's end watched in September-October | 3e | 8h | EDGAR notices | IBTA notice of 28 Sep 2021; others mid-October | exact | |
| 57 | Card Q3c's count of five ended funds | 3e | 8h | Card Q3c | Count | exact | |
| 58 | IBTA ended 15 days early | 3e | 8h | EDGAR | 15 Dec 2021 - 30 Nov 2021 (last trade) = 15 days | exact | Its cash came 3 Dec (12 days early) |
| 59 | The five paid within about 0.07% of their last price | 3e | 0; 8h (0.066%) | Card Q3c | None (the card's five values only; their largest is 0.066%) | no route | Rounds correctly from the card |
| 60 | 2000-2003: world shares 41% down | 3e; aha 9 | none (card Q85) | Card Q85 | Q85 checkpoints: start of month -42.1%, end of month -40.6% | differs (convention) | Disagreement 2 |
| 61 | Then costs about 18% (NT$) and 27% (US$) | 3e; aha 9 | none (card Q85) | Card Q85 | Q131 CSV, Jan 2003 to Dec 2004: +18.4% NT$, +27.2% US$ | rounding | |
| 62 | First plan about three-quarters shares | 3f | 8s (75%) | Team notes, 27 Sep | n/a | exact | |
| 63 | About 1 in 31 to none | 3f; aha 10 | 8s | `first_plan.py` (fresh: 6,453 of 200,000) | 200,000 / 6,453 = 1 in 30.99 | rounding | |
| 64 | About 1 in 7 against none with half a deposit | 3f; aha 10; 5 | 8s | `first_plan.py` (fresh: 27,386) | 200,000 / 27,386 = 1 in 7.30 | rounding | "None" is central (flags) |
| 65 | 96.8 in 100 | 3f | 8s | `first_plan.py` | 100 - 3.2265 = 96.77 | rounding | |
| 66 | A fall of about 3.6 points before January 2027 | aha 3 | 5; 8u (3.57) | `break_test.py` (fresh: 3.57195) | Extrapolating section 5's table ($96,303 at 2 points, slope rising from about $29,900 to $34,500 a point) to $150,000 gives about 3.6 | rounding | |
| (aha 4) | A 40% fall before the move: about $95,000-$105,000 | aha 4 | 8p | `fall40.py` (fresh equal) | $117,142 - 0.5324 x ($36,698 - 0.6 x $29,594 x 0.9994^3) = $107,041, rounded down to $105,000 | exact | Counted with row 8's range family; not in the 66 |

Not counted (not plan figures, or not printed): citation years; the aha-test scores 4.7 and 3.3 / 3.7; card Q46's
eight reasons; card Q209's 1-in-4 (stays in the store); the left-out 1 - 0.99^10, -22.4%, the top 0.1%, £12.26m and
60-80%.
