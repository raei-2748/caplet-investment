# Exhibits rebuild, Mon 16 Nov 2026 evening (Sydney): notes

Asked: card Q73's three Figure 1 fixes (`../charts/DESIGNS.md` section 2), and Table 2's line of what is held the
same plus one note sentence checking the five worlds against the history replays (`../ARGUMENT_LOG.md`, Mon 16 Nov
Day 9; card Q14b rows 20-21). Then rebuild, run every check, re-measure and render. NUMBERS.md and `../numbers/` were
not edited. Figures come from the 2026-11-15 results files, checked against NUMBERS.md as it stood at about 19:45 AEDT.
The working copy carried another worker's uncommitted additions: a line in 8a, two items in 8d and a new 8t on
custody. None changes a figure the exhibits read; Table 3's 8d checks still pass. Notes for the
store, not report prose: titles stay working labels and notes stay lists of items, written on 27 Nov.

## What changed

### Figure 1 (3a): card Q73's three fixes
1. **The sum in the heads, and a total row that adds up exactly.**
   - The heads read **"Its own Treasury + Extra Treasuries = $50,000"**. This is LACERA's formula head and GASB 67's
     Funded/Unfunded split (Q73-010, -036).
   - The total row reads **"$444,080 + $55,920 = $500,000"**. These are 8h's totals of unrounded figures. They add
     exactly to the ten payments and match 8h's "All ten" row, the note's reconciliation ($55,920) and 3a.
   - The rows, each rounded to the dollar, foot to **$444,081 and $55,919**. So the rounding clause is now a
     **required** note item (item 3), no longer "if room". It names both figures and says the total row is unrounded.
     This closes the morning's observation 1.
   - Lead's call, if wanted: print the footed sums instead ($444,081 + $55,919 = $500,000). The total would then add
     down the column as well as across. But it would print two figures NUMBERS does not hold, and the note would still
     reconcile to $55,920. Keel kept 8h's totals.
2. **One world per exhibit.** The figure now shows one basis only, cash waiting earning nothing after the 0.15% fee
   (8h's "fee" block).
   - The "At today's market rates" column ($50,000 ten times) is gone.
   - Today's rates are now note item 4. It merges the old item 2 tail and item 3: each own Treasury pays its whole
     $50,000, about $45,500 of the extra Treasuries comes back (1 Jan 2033 money), and about $1.11 for each $1 the
     payments need, with its reason (8h; card Q31). Q73-035's other option, a "$0" column, was not drawn: the note
     carries that world.
3. **The condition first in the title**, then the verdict, then the scale (Q73-016, -037). New working title: *If
   Cash Waiting Earns Nothing, Each $50,000 Payment Is Still Met by Its Own Treasury and Extra Treasuries From the
   2028 Deposit (Laura's Plan for Both Deposits, $450,000, Modelled)*.
   - It still sets on two lines.
   - It gives no per cent ("about 89%" is not in NUMBERS).
   - The title now lives in `exhibit_data.FIGURE1_TITLE`, so the checks can read it.
   - The question head ("If cash waiting earns nothing, what pays each $50,000?") goes, since the title now opens
     with that condition. The head is two lines instead of four, and the image is 3.19 in tall, not 3.56.

Unchanged in Figure 1: the bars, the cash dates, the wait labels and the legend. A new layout assert stops the build
if a wait label runs into the number column.

### Table 2 (3b, 3c)
- **The held-the-same line** is the first line under the heads, full width, plain, with a thin rule below it (the Bank
  of England's Table 3.A row; Q14b row 20). It reads: "Every row keeps the plan's deposits, steps, dates, fees and range
  rule; only the markets differ."
  - It fits one printed line.
  - It is checked against the data. The results file's one stamp gives one design, one range rule (0.5% cut, rounded
    down to $5,000, fees from each trade day) and the 0.15% waiting fee. The 2028 deposit is $150,000 in every
    scenario world (completion plus what is left = $150,000). 8i says it is one plan in five worlds.
  - "Only the markets differ" holds for every printed cell. The inflation row's 5% prices change only its 2027-dollar
    value, which is not printed (8i).
- **The history check, confirmed from the builder's data** (8i, 8j's joint-replay column). Every named world's
  flexibility is below the median replay's $32,326:
  - $29,823 (today's rates);
  - $19,476 (2006);
  - $21,086 (rates 3 points lower);
  - $21,910 (2007);
  - $23,641 (inflation).

  Printed as one note item: "checked against history: each named world's flexibility ($19,500 to $29,800) is below the
  median replay's ($32,300) (8i, 8j)". Two more facts are checked but not printed, for 3c or the aha reserve: the
  lowest stated bottom ($75,000) is below the replays' 1-in-20 low ($80,000), and no world's top reaches the 1-in-20
  high ($140,000; the highest is $120,000). **Caveat for the lead:** the first row is the base case, not a stress. It
  sits below the median replay because its shares grow 7.5% a year, against about 9.6% in the US history windows
  (8j "What it shows"). So "picked to hurt" fits the four stresses. The note states the fact, not an intent.
- **Note within its 95-word budget.** In a terse note the new sentence is 9 words ("Each named world's flexibility is
  below the median replay's"). It is paid for by cutting 9 words from the range-rule item, "modelled on the 6 Nov 2026
  curve until then", which the first item ("MODEL, not forecasts; Treasury curve of 6 Nov 2026") already says.
  - Net change: 0 words.
  - Cut: the "if room" dates item (M7), SKELETON's named first cut. It was outside the 95. Figure 1 shows the cash
    dates; the sequence stays in the store and 3a.
  - Fixed: "less the fee" now reads "less the fees" (NUMBERS 0 has two fees: the fund's, and the waiting ETF's 0.15%).
    This closes morning observation 2, with no word added.

### Checks added
- **`exhibit_data.check()`: 24 new checks.**
  - Figure 1:
    - the sum head, against every row;
    - the total row: across, against the ten payments, and against 8h's three "All ten" totals;
    - the footed pair, and its $1 gaps;
    - one world: no today's-rates column, head or title;
    - every row pays $50,000 at today's rates (note item 4);
    - the title opens with the condition, keeps "$450,000" and "Modelled", and gives no per cent.
  - Table 2:
    - the held line, against the stamp, the deposit and 8i;
    - its five named parts;
    - the five worlds against the median replay;
    - the median's flexibility against 8j;
    - the two unprinted history facts.
- **`build_exhibits.words_check()`, new.** It reads 226 exhibit texts (titles, heads, cells, legend, bar labels,
  every note item) against 8 patterns: the conceit's two words, "endowment", "optimal", "natural hedge", "fail-safe",
  "fixed" (an iBond fund's payout is never fixed) and "89%". The build stops on any hit.

## Check results
- `exhibit_data.py`: **419 checks, 418 PASS, 0 FAIL, 1 flagged.** The morning had 395. The flag is the same rounding
  pair, now carried by required note item 3.
- `words_check`: **226 texts x 8 patterns, 0 FAIL.**
- Build: exit 0. Fonts in the PDF are Liberation Serif regular, bold and italic. The three table previews were cropped
  from `exhibits_letter.pdf`.
- **Unchanged, byte-identical:** Table 1's and Table 3's PNGs, `s2_fit` (626-word ceiling, 46 words of headroom).
- **Changed:** Figure 1's SVG and PNGs, the Table 2 PNG, `tables.md` and `measurements.json`.
- `../charts/build_charts.py` reads Table 2's rows from `tables.md`. It was not run, since it writes outside
  `exhibits/`. Instead its exact regex was run on the new `tables.md`: it reads all 8 rows ($95,000 / $115,000 /
  $29,800 first). The held line sits outside the Markdown table, as the result row does.

## Line costs (Letter, Wharton's format; card Q23's method; `measurements.json`)

| Exhibit | Morning: with note / without | Evening: with note / without | Change |
|---|---|---|---|
| Table 1 | 20.9 / 15.9 (75 words) | 20.9 / 15.9 (75) | none |
| Figure 1 | 17.3 / 13.3 (60 words) | 17.3 / 12.3 (77 words) | 0.0: the figure is 1.0 line shorter; the note's required items are 17 words longer |
| Table 2 | 16.2 / 9.2 (95 words) | 16.7 / 9.7 (95 words) | +0.5: the held line (one single-spaced line and its rule) |
| Table 3 | 21.9 / 18.9 (40 words) | 21.9 / 18.9 (40) | none |
| Section 3's three | 55.4 | **55.9** | **+0.5 line, about 7 words of prose** |

- **Figure 1's note budget is now 77 words (was 60).** Counted in a terse rendering, items 1-5 run 114 words against 97
  for the morning's items 1-4. The +17 is two things: the rounding clause, now required (+10), and today's rates
  folded into one item (+7). Measured at the old 60 words, the figure would cost 16.3 lines; it now costs the same
  17.3 as this morning.
- **Section 3 had no headroom (SKELETON page arithmetic), so the half line must come from somewhere.** Two ways back,
  both measured tonight:
  - Table 2's note at about 90 words or fewer costs 15.7 lines, not 16.7 (filler at 85, 88 and 90 words: 15.7; at
    92: 16.7). Five fewer words would pay for the held line and give back half a line more.
  - Figure 1's note at 60 words would cost 16.3 lines; at 66 and above, 17.3.

  Which items to tighten is the lead's call. Nothing required was cut here.

## Not done, or for the lead
- `../template/build_template.py` (another owner) still has its own Figure 1 title and note text from before these
  fixes. It places `exhibit2_reserve.png`, which is now the new one-world figure at 3.19 in. On 27 Nov, pour with
  `build_exhibits.add_figure1` and `add_table2` (specs.md decision 7).
- `specs.md`: the Exhibit 2 and 3 rows were not rewritten. A pointer at the top sends readers here and to `tables.md`.
- DESIGNS's other Next item for Figure 1 ("the '$0' column and direct labels") is not done. The one-world fix drops
  today's rates to the note, so no "$0" column is drawn.
- Restore "modelled on the 6 Nov 2026 curve until then" to Table 2's range-rule item if the bond desk wants M2's
  phrase kept in that item. It costs 9 words, and Table 2's note goes back over 95.
- Morning observation 3 (the Feb-2037 bond's "waits 10.5 months", counted from 15 Feb) is unchanged. It is an accepted
  call.
- The fresh-reader five-second test (Mon 23 Nov) should read the new Figure 1 cold. Its head is now an equation over a
  column whose only figure is in the total row. Keel's look found it reads as a sum, but no cold reader has seen it.
