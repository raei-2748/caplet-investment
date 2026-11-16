# First designs of the report's exhibits (Mon 16 Nov 2026, Final Report Day 9; research from cards Q14a and Q14b in section 8)

Design notes, not report text. One entry per need in `../SKELETON.md` ("Exhibits", items 1-4) and per aha that might
earn a picture (`../research/goldmine/AHA_REGISTER.md`). Each entry gives the question the exhibit answers, its data
(every figure from `../NUMBERS.md`, checked in `build_charts.py` before drawing), the form chosen and why, and what was
tested. The four built exhibits in `../exhibits/` (Table 1, Figure 1, Table 2, Table 3) stay the working versions;
this folder holds the test renders that compete with them or would join them.

**The medium decides half the design.** The report is a PDF in Wharton's format (12-pt Times New Roman, double-spaced,
1-inch margins, 9-12 pages without references), likely read on screen and sometimes printed. So: black and two greys,
no colour carrying meaning (`../exhibits/specs.md` section 0); Times metrics in every figure, at least 10 pt at printed
size; every value a reader needs is printed, because a PDF has no hover (the dataviz skill's tooltip layer does not
apply). The dataviz method still runs in order: form first, then tone by job (emphasis: the plan in black, the
alternatives in grey), one axis per panel, thin marks, selective direct labels and no legend boxes, then render and
look (every render below was looked at and fixed at least twice).

**The page budget decides the other half.** Section 3 has no headroom (about 1,900 words beside Figure 1, Table 2 and
Table 3; SKELETON line 11); Section 2 has about 46 words (`../exhibits/specs.md`, Page cost). So a new exhibit must
either replace prose it does better than, or replace another exhibit. Wharton's older guidebook (W8): "Too many charts,
graphs ... will not dazzle". The default answer is four exhibits; a fifth must win a cold test.

## Summary

| Need (part) | Question a judge should answer in five seconds | Form | Status Mon 16 Nov | File |
|---|---|---|---|---|
| Table 1, holdings (2.1-2.5; Wharton requires it) | What did the $300,000 buy, which payment does each holding stand for, and was it bought as planned? | Table, Wharton's five columns plus "Units bought / target" and "Pays for" | Built (`../exhibits/`); no rival: Wharton prescribes a table | `../exhibits/table1_holdings_2x.png` |
| Figure 1, the operating reserve (3a) | Which Treasury pays each year's $50,000, and what pays the gap if waiting cash earns nothing? | Escrow sufficiency schedule beside a staircase of holding periods | Built; rival c3 tested (below) | `../exhibits/figure1_reserve_2x.png` |
| Table 2, five markets (3b, 3c) | In a bad market, what still holds and what shrinks? | Table of five worlds and the 585-replay spread | Built; rival c4 (dot ranges) tested | `../exhibits/table2_markets_2x.png`, `c4_table2_as_dots.png` |
| Table 3, monitoring (3e) | What is watched, and which two events alone change the plan? | Table, seven rows, five columns | Built; no rival (a checklist is a table) | `../exhibits/table3_monitoring_2x.png` |
| Aha 3, a rare year (2.5) | Was $300,000 a normal price for the ten? | Time series strip from $0 (c1d, default) or from $240,000 (c1a); the sparkline in the sentence is a format risk | **Candidate: scored 5 cold as a chart (c1a), 4 as words**; c1d drawn after card Q14b | `c1d_cost_history_zero_base.png`, `c1a_cost_history_strip.png`, `c1c_sparkline_in_text.png` |
| Aha 6, more shares is the risky choice (3b) | Would more shares let Laura promise more? | Two dot panels on one row set, plus a flexibility column | Candidate: scored 3 cold as a chart, 4 as words; redrawn after the reader | `c2_more_shares.png` |
| Aha 4, certainty has dates (3.0) | When does each part of the money become owned? | Dated timeline, four rows | Test; not yet read cold | `c3_when_owned.png` |
| Aha 2, diversifying the payments (2.3) | Why not spread the ten across several kinds of safe bond? | Icon array | **Dropped**: read as "the ten payments"; words scored 4; icon arrays make a risk feel smaller (card Q14a) | (removed) |

## 1. Table 1, the holdings (Section 2)

- **Question.** Wharton, Section 2: every holding, "ticker or identifier, name, asset type, amount allocated, and
  percentage", "expressed using the original $300,000"; total $300,000 and 100%.
- **Data.** NUMBERS 8g (the WInS record at cost) and 8m (targets set before trading); not a model.
- **Form and why.** A table, because Wharton prescribes it and because the reader needs exact figures to the cent; a
  table is the right form when the reader looks values up rather than compares shapes. The built version adds two
  columns that do argument work: "Units bought / target" (bought as planned, read down the column) and "Pays for" (each
  holding's job, which turns a list into a plan). No graphic competes.
- **Open.** The fresh-reader five-second test on Mon 23 Nov (`../exhibits/specs.md`).

## 2. Figure 1, the operating reserve (3a)

- **Question.** The case: "recommend its size and initial asset composition and explain how its composition should
  change, if at all, as the annual payments approach and are made".
- **Data.** NUMBERS 8h (`../numbers/results_reserve_2026-11-15.json`, the "fee" rows: own Treasuries pay $444,080 of
  the $500,000 if waiting cash earns nothing, the top-up's Treasuries $55,920).
- **Form and why.** The escrow verifier's sufficiency schedule (the professional form for "are these fixed payments
  covered without reinvestment?", card Q28) beside a staircase of holding periods on one unbroken time scale, so the
  six years held before the first payment show at true length. A table alone would hide the time; bars alone would
  hide the sufficiency test.
- **Rival tested: c3, "when each part is owned".** Four rows (the ten payments, the bottom, the top, her flexibility)
  from January 2027 to January 2033, solid where the money is owned in Treasuries, hatched where it rests on markets;
  the payments row is grey for 2027 ($444,080 of $500,000 owned if waiting cash earns nothing; never "89%", which is not in NUMBERS, rater P) and black from
  January 2028. It answers 3.0's aha ("certainty has dates") rather than 3a's question, so it is not a rival to Figure
  1 but a candidate for 3.0, where no exhibit sits. Its words are plain on purpose: the conceit stays in prose, never
  in an exhibit (CONCEIT V2.2: "said beside the table, never in it"), and the prose beside it can say "ink" for solid.
  Cost: about 8 lines with a two-line title and a short note, about 110 words of 3.0's prose. Not yet read cold.
- **Card Q73 (Mon 16 Nov, rater P): how institutions draw a matched ladder, and three fixes for Figure 1's clarity
  cell (3).** Professionals rarely pair each payment with the money that pays it: lotteries print bonds and prizes in two
  tables or prove the match by two equal totals (Missouri, $34,904,000 = $34,904,000), pension funds give one ratio, and
  only GASB 67 projections and escrow verifiers go row by row, so Figure 1's form is rare, not standard (Q73's own
  finding). Its test is stricter than the UK insurance regulator's on both counts: the PRA lets waiting cash earn the
  risk-free rate and allows a shortfall up to 3% of the liabilities' value; Figure 1 lets it earn nothing and allows none
  (Q73-025, both details checked at source; a 3a aha candidate). The fixes, for the next rebuild:
  1. **The sum in the column heads** ("Its own Treasury + Extra Treasuries = $50,000"), New Jersey's split-column shape
     without its "Funded / Unfunded" labels, and a total row that adds up: the printed rows sum to $444,081 and $55,919,
     not $444,080 and $55,920, so the rounding note stays (Q73-036, Q73-011).
  2. **One world per exhibit:** the today's-rates column ($50,000 ten times) goes to the note (Q73-035).
  3. **The condition first in the title, then the verdict** ("If cash waiting earns nothing, ..."); never "about 89%",
     which is not in NUMBERS (Q73-037, adapt).
  Table 1's cost column is never read against the $50,000 payments (Missouri's matched book shows "short" on market
  value), and both exhibits' titles name their scale ($300,000 for Table 1, $450,000 for Figure 1).

## 3. Table 2, five markets (3b and 3c)

- **Question.** The case's "favorable and unfavorable market outcomes"; Wharton: "the level of confidence associated
  with that range and the factors that could affect it".
- **Data.** NUMBERS 8i and 8j; `../exhibits/tables.md` (parsed by `build_charts.py`).
- **Form and why (built).** A table of five named worlds and the replay spread, with the payments column first ("All
  paid" in every row) and a closing row: the contribution equals the stated top in every world and replay. Card Q28:
  named conditional worlds fit a table, and text avoids the misreadings of a bracket graphic (Joslyn and Savelli 2021).
- **Rival tested: c4, the same rows as dot ranges.** Position on a common scale makes the worlds' ranges comparable at a
  glance (the overlap of every row with $95,000-$115,000 is visible), and the flexibility panel shows how little it
  moves. Against it: the exact stated figures are what Laura would say, so the table's numbers are the content, and
  the chart repeats them as labels anyway. Verdict for now: the table stays; c4 goes to the Mon 23 Nov fresh reader as
  the alternative, and wins only if that reader answers the five-second question faster from it.

## 4. Table 3, monitoring (3e)

- **Question.** Wharton: "what Laura or her asset management team should monitor as 2031 and 2033 approach".
- **Form and why.** A checklist is a table: seven signals, five columns (signal; reader; carry on while; look closer or
  act when; what it changes and never changes), the two reasons to change defined in their own rows. No graphic does
  this job. Built; precision waits for the next bond reader (row 4's notice watch now reads September-October).

## 5. Aha 3, a rare year (2.5): the strongest new candidate

- **Question.** Was $300,000 a normal price for ten $50,000 payments starting six years out?
- **Data.** NUMBERS 8e (each day's Treasury curve since 2000, the ten valued as if that curve were 6 Nov 2026's):
  $300,000 was enough on 731 of 6,716 days since 2000 (10.9%); on one day from June 2007 to August 2026 (19 Oct 2023,
  $299,293); the dearest $470,217 on 4 Aug 2020; 5 Oct 2026 $288,333, the cheapest since May 2002. All checked in
  `build_charts.py` against `results_price_history.json` and the register. One basis per sentence: 8e's long series
  runs on average $1,944 above 8b's dated 2026 values (the same 37 closes under $300,000), so a dollar figure for a 2026
  day said beside this chart comes from 8e ($288,333 on 5 Oct), and one said in 2.5's table talk from 8b ($287,938),
  never both in one paragraph.
- **Form c1a: a time-series strip** (6.5 x 2.2 in, about 9 lines with title and note): the cost line in mid-grey, the
  days when $300,000 was enough as heavier black dots on it, the $300,000 line in black, four direct labels. **Cold
  test: 5 of 5** with only a caption (reader B: "it changes the plan in my head from 'a conservative team playing safe'
  to 'a team that saw a window'"); the words alone scored 4. Fixed after the reader: the "enough" days now differ
  from the line in weight as well as tone, and the 19 Oct 2023 label says what the day was.
- **Form c1b/c1c: a sparkline** (Tufte's word-sized graphic, 0.95 x 0.16 in) inside a sentence: "From 2000 to 2026 the
  ten cost [line] more than $300,000 on nine days in ten." It costs no lines. Against it: APA numbers every figure, and
  an unnumbered inline graphic is unusual in an APA paper, so it is a format risk for a first-round reader; and at
  0.16 in the $300,000 reference line is faint.
- **What the reader also forced.** The words overclaimed: "the plan never needed the luck" is false for 2020 (the ten
  cost more than both deposits). The register now says the plan was built to need the year, not the day
  (`../research/goldmine/aha_test_2026-11-16/RESULTS.md`).
- **Verdict for now.** c1a is the best new exhibit found so far, and it belongs to Section 2 (2.5), whose 46 words of
  headroom cannot hold it: it would displace about 130 words of Section 2, or replace part of Table 1's 75-word note.
  The Mon 23 Nov fresh reader sees Section 2 with and without it.

## 6. Aha 6, more shares is the risky choice (3b)

- **Question.** Would putting more of the 2028 money into shares let Laura promise more?
- **Data.** NUMBERS 8n (`results_share_split_2026-11-15.json`, 200,000 simulated futures): stated range on today's
  market rates, all money left beyond the ten (median and 1-in-20 low), her flexibility (median), for five splits.
- **Form c2.** Left panel: the stated range per split, a staircase falling from $130,000 (all to the floor) to $0-$70,000
  (all shares), the plan in black. Middle panel (redrawn after the cold reader): all money left, as the change against
  the plan, median and bad 1-in-20 on a zero line, so the trade is read off one axis (three-quarters shares: +$7,000 at
  the median, -$14,000 in a bad future). Right: her flexibility as a printed column ($9k for all-floor against $29k for
  the plan), which answers the reader's objection that all-floor "is about as good in a bad future".
- **Cold test (before the redraw): 3 as a chart, 4 as words.** The left panel alone "would score 4"; the right panel's
  axis starting at $125,000 exaggerated the gaps (fixed: a zero-centred change scale), and the all-floor row argued
  against the plan without its flexibility beside it (fixed: the flexibility column).
- **Verdict for now.** The words carry this aha in 3b; the chart is a reserve for 3b only if it replaces about 150 words
  there and wins the Mon 23 Nov read.

## 7. Aha 2, diversifying the payments (2.3): dropped as a picture

An icon array (100 squares, 10 black: if each of ten payments were 99% safe on its own, about 10 Lauras in 100 would
miss one) was drawn because icon arrays help readers with natural frequencies. Cold, it scored 3 against the words' 4:
the ten black squares read as "the ten payments", nothing said a square is a Laura, and it showed no comparison with the
plan's one issuer. Numerate judges do not need it. The arithmetic stays in the words.

## 8. What the Q14 research changes (cards Q14a and Q14b, Mon 16 Nov)

### Graphical perception (card Q14a, 30 rows, 27 verified at source)

Cleveland and McGill (1984) rank the elementary judgements: position on a common scale is read most accurately, then
position on unaligned scales, then length, then angle and area; Tufte's "Compared with what?" and "show the zeros";
Galesic, Garcia-Retamero and Gigerenzer (2009) on icon arrays; Padilla, Kay and Hullman (2022) on how a drawn boundary is read. What it means here:

- **Table 1** stays a table, rows in maturity order, no pie or treemap, no price history beside it; the definition of
  "owned" sits in the sentence beside the table, never in it (CONCEIT V2.2).
- **Figure 1** already draws what differs between rows as position on one aligned date axis, to scale, with no axis
  break and the dollars printed as numbers, which is what the card asks. Three changes to weigh on the next exhibits
  rebuild, each against its page cost: a fourth number column printing "$0" short in all ten rows (Tufte: the zeros are
  the finding; "Show the zeros", row 14); direct labels in place of the legend line (the bars already carry their
  tickers, so "iBonds Treasury ETF" and "Treasury bond" can each be said once beside the rows); and the card's leaner
  rival, ticks for each cash date and payment date without bars from 2027. The bars stay for now: they are the one
  place the report shows the six years held before the first payment at true length, which is 3a's point.
- **Table 2** stays a table (about 20 numbers; a drawn range would be read as a category boundary, row 20). Any chance in
  its note is a count out of 100 simulated futures with "simulated" in the heading. If 3c's confidence is ever pictured,
  twenty dots on one dollar axis, never a band or fan: the stated range's ends may be hard lines because Laura owns
  them; the spread's ends may not. The store's fan-chart idea (H9-143) is refused for that reason. c4 draws stated
  ranges only, so it passes; it stays the alternative for the fresh reader.
- **Table 3** prints each row's normal value and its action level, rows in the order each signal can first be seen, the
  two reasons to change set apart as the only rows that act.
- **The icon array for 2.3 is dropped twice over.** The cold reader read the ten black squares as the payments, and
  the research says icon arrays make a risk feel smaller (row 16), the opposite of 2.3's job; the sentence names the
  wrong intuition first, then the count: ten promises each kept 99 times in 100 are all kept in about 90 of 100 futures
  (Tversky and Kahneman 1974; Slovic, Fischhoff and Lichtenstein 1978; rows 26-27).
- **Sparklines.** The card rejects word-sized price lines because a holding's price path invites reading WInS gains as
  evidence. c1's line is the market cost of the ten, not a holding's gain, so that reason does not reach it, but with
  APA's numbered figures it confirms c1c as a format risk; c1a or c1d is the form.
- **A dated timeline in 2.0** (McCloud: time read as distance), if 2.0 needs the calendar at all: one line of five
  dated marks drawn to scale (Jan 2027; Jan 2028; the first trading day of 2031; the 2031 meetings; Jan 2033), about a
  tenth of a page, replacing prose of equal length. c3 is the fuller version of the same idea; never comic panels.

### Plain English, regulators and past teams (card Q14b, 29 rows, 26 verified at source)

- **Table 1.** Rows by maturity date, time running forward (SEC Plain English Handbook, p. 52); right-aligned figures,
  one precision per column, commas (UK Government Statistical Service); no allocation pie beside it (the handbook, p. 53:
  not more than 5 or 6 slices, and a table is often clearer). The built table already does all three; the title states
  its message in plain words and never uses pencil or ink.
- **Figure 1.** No axis break, every step from $0 (the handbook, p. 51 and the Rule 421 note, p. 67: "draw the graphs
  and charts to scale"). The built staircase starts at $0. Its note can give the two totals a court reads for a
  structured settlement, cost on the purchase date beside $500,000 paid on ten dates (New York's settlement forms,
  row 15), with "guaranteed" allowed (Book 19). Figure 1 is also the one schedule her team would re-run each January,
  as Berkshire's yearly table outlived its author (row 10), so Table 3 can name it as the first thing watched.
- **Table 2.** The built table already follows the Social Security Trustees' form: today's forward rates first, the
  named worlds under one head and history's 585 replays under another, the payments column the same in every row
  (rows 18-19). Two changes to make on the next exhibits rebuild: one line naming what is held the same in every world
  (the Bank of England's Table 3.A row "Assumptions that are consistent across projections", row 20: the 6 Nov 2026
  curve, 7.5% for shares where shares are modelled, the range rule), and one sentence in the note checking the named
  worlds against the replays, as the Bank's staff check named scenarios against a reference distribution (row 21). That
  check is now an aha reserve (`../research/goldmine/AHA_REGISTER.md`): all five named worlds leave her less
  flexibility than the median replay ($19,500-$29,800 against $32,300), the lowest stated bottom ($75,000) is below
  history's 1-in-20 low ($80,000), and none reaches its 1-in-20 high top ($140,000); the worlds were picked to hurt.
- **Table 3.** A table because it is a set of ifs and thens (the handbook, p. 33: "consider presenting the information in
  a table"); 3e's prose does not walk its rows (UNECE: no "table reading"), and it names the limits of its own tests
  (ASOP 51, 4.1(f)).
- **c1a against c1d (new).** The handbook's rule on baselines applies to c1a, whose axis starts at $240,000, so its
  2020 peak stands about 3.8 times as tall as the $300,000 line when it cost 1.57 times as much ($470,217). Distances
  from the $300,000 line are true in both versions, which is what the aha reads, but a reader judging heights is
  misled by c1a. c1d draws the same data from $0 (6.5 x 2.6 in, about 11 lines): the line still sits above
  the $300,000 line almost everywhere after 2002, and nothing is exaggerated. Both go to the Mon 23 Nov fresh reader;
  c1d is the default unless c1a is read faster and no less truly.
- **The prose beside every exhibit.** The first sentence of each paragraph carries the claim in words and no figure; the
  figure follows as its proof (UNECE 2009, pp. 3-4); say a number the way a person says it ("One in ten ..."; the ONS);
  the text adds what the exhibit cannot and never repeats its trend. What Laura owns is stated as fact; calibrated
  words, each with its number, only for what is not yet owned. The IPCC does exactly this: "It is unequivocal that
  human influence has warmed ..." beside "likely (medium confidence)" (row 23); a strikingly dissimilar parallel to the
  conceit's ink and pencil, for `../CONCEIT.md`'s owner, in prose only.
- **What winning teams showed.** No winning Final Report is public (Wharton: "We do not release final reports from
  previous winners"); the one public Top-50 report and last year's Top-50 repository leaned on tables and at most one
  modelled chart, with no trading-gains chart (rows 24-26). Four exhibits, one of them a figure, sit inside that
  pattern; a fifth must still win the cold test. None of these pages is a reference.

## Next

- ~~**Mon 16 Nov evening (first):** Table 3 is 27.9 lines against a 23.5-line Letter page after tonight's precision fixes (row 4, the fund-event watch, alone takes 12 lines; 1.4 lines over even with no note). Cut it before any reader sees it: row 4 to its signal and action in Wharton's words, its window and the earlier-fund class to the note or 3e; `../exhibits/build_exhibits.py` now measures and warns.~~ **Done Tue 17 Nov** (`../exhibits/REBUILD_2026-11-17.md`): 21.4 lines with its note, one page between two prose lines (18.4 without); row 4 from 10 printed lines to 4 with all its watched events; row 5's limit is NUMBERS 4's 0.5%; every cut detail in the "For 3e's notes" list under Table 3 in `tables.md`; 433 checks, 0 FAIL; charts 37 of 37. Next: a bond reader on rows 4 and 5, and the stranger test on the cut table.

- Done Mon 16 Nov: Q14's cards (`../research/cards/Q14a_showing_work_graphics.md`, `Q14b_showing_work_plain_english.md`)
  read against these designs (section 8).
- Mon 23 Nov: the fresh-reader five-second test reads the four built exhibits plus c1d and c1a, c3 and c4 (as
  alternatives), each cold with only its title.
- Next exhibits rebuild (`../exhibits/build_exhibits.py`): Table 2's line of what is held the same in every world and
  its one-sentence check against the replays; Figure 1's "$0" column and direct labels, each only if it fits the page. Figure 1's three Q73 fixes (section 2): the sum in the heads with a total row that adds up, the today's-rates column to the note, the condition first in the title.
- Rebuild: `python3 -I keel/final_report/charts/build_charts.py` from the repo root (about 20 seconds; 37 checks, then 8 renders).
- Mon 16 Nov evening, done (`../exhibits/REBUILD_2026-11-16_evening.md`): Figure 1's three Q73 fixes (one world; heads "Its own Treasury + Extra Treasuries = $50,000"; total "$444,080 + $55,920 = $500,000", with the $444,081 / $55,919 rounding note now required; title opens "If Cash Waiting Earns Nothing") and Table 2's held-the-same line and history check; 419 checks, 0 FAIL; Section 3's exhibits 55.4 -> 55.9 lines.
