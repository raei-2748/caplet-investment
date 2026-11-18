# Exhibits rebuild, Wed 18 Nov 2026 evening (Sydney): Table 2's note carried, page fit re-measured

**Superseded in part by the "Second pass" section at the end:** Table 2's note no longer gives a median figure (the
lead's call on card Q146), and it is trimmed to 153 words, 21.2 lines.

Asked: four open items in NUMBERS section 9 and SKELETON's Exhibits list.
1. Carry every hand edit in `tables.md` that the builders do not yet make.
2. Replace Table 3 row 5's "[x]%".
3. Give Table 2's note its own wording for the starting months' method.
4. Rebuild, run every check, re-measure Table 3's one-page fit and look at the PNGs.

Read against NUMBERS.md as it stands after the Tue 17 Nov evening re-size and Wed 18 Nov morning's 8u and 8v. Files
outside `exhibits/` were not edited, except the dated lines in NUMBERS section 9. These are notes for the store, not
report prose.

## 1. Hand edits: what was already carried, what was not

**Method.** HEAD's scripts were run unchanged, and the `tables.md` they wrote was diffed against the committed one.
- **One line differed: Table 2's note items.** It was edited by hand in Wed 18 Nov morning's commit (abb6f65). The
  edit carried the lead's calls on coherence reader 9's H2 and H6 and SKELETON row 3e's hand-off.
- **Every other line was reproduced exactly.** That includes:
  - Mon 16 Nov night's edits to Tables 1-3, Figure 1's legend and note item 1, carried that night and on Tue 17 Nov
    (`REBUILD_2026-11-17.md`);
  - Tue 17 Nov evening's fixes, made in the scripts (commit 4c3332d).

**The three Wed 18 Nov morning edits, now made by `build_exhibits.py` (Table 2's note items) from figures in
`exhibit_data.py`:**

| Edit | Before | Now | Figures and source |
|---|---|---|---|
| The 7.5%'s source and standing (H6) | "shares 7.5% a year in rows 1 and 3" | "... (J.P. Morgan's 2027 assumption for world shares, above the middle of published forecasts (median about 6.5%) of the fifteen houses named in the References, CANON B15; ...)" | `SHARE_RETURN` 7.5% (NUMBERS 0, CANON B15); `FORECAST_MEDIAN` 6.5% (8v's table, card Q6b); the phrase is `SHARE_RETURN_STANDING` |
| The rate past the margin starts from the room under the top (H2) | "if the funds' costs beyond their fees passed the range's 0.5% ... for each further 0.1% centrally" | "if the funds' costs beyond their fees used up the room under the top (the 0.5% margin plus the rounding down, about 2% centrally, NUMBERS 8u) ... by about $120 for each further 0.1%" | `ROOM_UNDER_TOP` read from `results_break_2026-11-18.json` (8u: 2.32%, printed "about 2%"); `SHORT_PER_TENTH` $118, printed "about $120" (sections 3 and 8u) |
| The starting months' method in the note | "(method in 3e)" | "(overlapping starting months, shares of the past, never probabilities; Wed 18 Nov morning, 3e no longer carries the method)" | `TABLE2_STARTS_METHOD`, SKELETON row 3e's hand-off wording |

**Two wording differences from the hand edit, both deliberate.**
- **The 7.5%'s standing is now in NUMBERS 8v's own words**, "above the middle of published forecasts (median about
  6.5%)", which 8v quotes twice. The hand edit read "above the middle of fifteen published forecasts, median about
  6.5%". It was not wrong, but NUMBERS wins, and the brief named the 8v phrase. The fifteen are still named, as card
  Q117 and SKELETON l.100 ask ("the median only with the fifteen named").
- **The reviewer's mark now comes first**: "coherence reader 9, H6, the lead's call, Wed 18 Nov morning: ...". The
  hand edit put "the lead's call" first. With the mark first, the Letter PDF's placeholder note drops it, as it drops
  every other reviewer's mark (`_unmarked`).

**Conflicts with the Tue 17 Nov evening re-size: none.** Every re-sized figure the exhibits print matches NUMBERS:
- Table 3 row 1 and its note: $39,162 = $2,388 + $36,774.
- Figure 1's note: $36,774; $1,177 to spare; about $46,600 of the backstop ($46,566); the reserve about $445,700
  ($445,655); about $1.12 for each $1.
- Table 2: the range $95,000-$115,000; her flexibility $28,700 ($28,682).
- Table 3: $28,700 in row 7.

Floor money ($81,244) and VT ($29,594) are printed in no exhibit.

## 2. Table 3 row 5's "[x]%": already done Tue 17 Nov, confirmed tonight

`REBUILD_2026-11-17.md` set it from NUMBERS 4's "A trade-day limit for Table 3 row 5" (0.5% of net asset value for
each fund leg). Tonight's confirmation:
- Row 5 prints "First trading day, prices within 0.5% of net asset value" (`TRADE_LIMIT`, `exhibit_data.py`
  l.638).
- `check()` compares it with NUMBERS 4, and finds no "[x]" in the cells or the 3e list.
- The 3e list keeps the bonds' 25-basis-point curve test (8m).
- The Letter PDF's text has no "[x]".
- The only "[x]" left in `tables.md` is the dated header line saying it was replaced.

Section 9's "l.574-575" and "l.98" were Mon 16 Nov night's line numbers.

## 3. Table 2's note: the method

SKELETON row 3e (recast Wed 18 Nov morning) no longer carries the starting months' method. SKELETON Exhibits item 3 and
the 3e row's hand-off give the wording, so the note now says it itself (edit 3 above). Every other place in
`exhibits/` that pointed to 3e for the method now gives the wording:
- `specs.md` l.203 (was l.199) and its "To prose" clause;
- a dated pointer at the top of `specs.md`.

The 7.5% stays in the note, J.P. Morgan's, with 8v's phrase. It is never "the top", "the consensus" or "upper third",
and three new `words_check` patterns now stop the build if any of them appears in any exhibit text.

## Checks added

**`exhibit_data.check()`, 10 new checks (440 to 450):**
- 7.5% against section 0 ("VT median growth 7.5% a year");
- CANON B15 names J.P. Morgan and "AC World Equity 7.50";
- 6.5% against 8v's table row "the median of fifteen houses' forecasts";
- the phrase "above the middle of published forecasts (median about 6.5%)" is in 8v (found twice);
- 7.5% > 6.5%, so "above the middle" holds;
- the room under the top, 2.32%, against 8u's top row;
- "about 2%" against 8u's "**About 2%**: ... 2.32%";
- $118 against 8u's "about $118 short for each further 0.1% centrally" (section 3's check is kept);
- WORDS's row "the room under the top" (the 0.5% margin plus the rounding down; about 2%, centrally);
- the method's wording against SKELETON's hand-off.

Also, `results_break_2026-11-18.json` must stand on the same register (2026-11-17) and curve (6 Nov 2026), or the
module stops on import.

**`build_exhibits.words_check()`:** three more patterns: "upper third", "consensus", "top of (the) (published)
forecasts/estimates".

**`build_exhibits.carry_check()`, new.** It runs 14 checks on Table 2's note, in its items and in the Letter PDF's
placeholder:
- it must carry the five new phrases;
- it must not carry "method in 3e" or "passed the range's 0.5%".

The build stops on any failure.

**A measurement fix.** An exhibit taller than the room between two prose lines but inside Letter's 9-in block fell
through to the tall-page fallback. That fallback printed "does not fit one page ... -1.3 lines more". Such an exhibit
is now measured by the same gap method and recorded as one Letter page, not between two prose lines
(`between_two_prose_lines: false`); `_measure_tall` sets `fits_one_page` from the height. No earlier measure changes.

## Check results

- **`exhibit_data.py`: 450 checks, 449 PASS, 0 FAIL, 1 flagged.** The flag is unchanged: Figure 1's rounding pair
  ($444,081 / $55,919 against 8h's $444,080 / $55,920), carried by its required note item 3.
- **`words_check`: 240 exhibit texts x 11 patterns, 0 FAIL** (was 240 x 8).
- **`carry_check`: 14 checks, 0 FAIL.**
- **Build: exit 0.** Fonts in the PDF are Liberation Serif regular, bold and italic.
- **Two warnings, both on the review PDF only:** Table 1's and Table 2's placeholder notes (every note item written out,
  longer than the budgets) run over a page break, so their previews are joined. Table 1's warning predates tonight.
  Table 2's warning was in HEAD's build too: its placeholder was already longer than a page's room, and it is longer
  now.
- **Unchanged, byte-identical to HEAD:** `table1_holdings_2x.png`, `table3_monitoring_2x.png`,
  `figure1_reserve_2x.png`, `exhibit2_reserve.png`, and `s2_fit` (626-word ceiling, 46 words of headroom).
  `figure1_reserve.svg` changed only in its date and element ids, so it was restored from HEAD.
- **Changed:**
  - `table2_markets_2x.png`: the table body is pixel-identical to HEAD; only the placeholder note is longer;
  - `exhibits_letter.docx` and `.pdf`;
  - `tables.md`: the title, the generated-by line, one new dated header line, Table 2's note line and its page cost;
  - `measurements.json`: t2 and `_built`;
  - `exhibit_data.py`, `build_exhibits.py` and `specs.md`.
- **Same `tables.md` from the builders.** No hand edit is left, and a rebuild reproduces `tables.md` line for line.
- **Re-run at about 19:47 AEDT, after the numbers owner's concurrent NUMBERS edits.** Those edits were section 5 (c)'s
  "most" deposit, $76,565 to $78,324, and 8q's card Q131 block; no exhibit prints either. The re-run gave the same
  counts (450 / 0 FAIL; 240 x 11; 14) and a byte-identical `tables.md` and `measurements.json` apart from `_built`.
- **`../charts/build_charts.py`** (it reads Table 2's rows from `tables.md`): run in a scratch copy, with its outputs
  sent to the scratchpad, so nothing in `charts/` was written.
  - **37 of 37 PASS, exit 0.**
  - Six of its seven PNGs come out byte-identical to the committed ones.
  - **`c4_table2_as_dots.png` differs, and the committed file is stale, not tonight's work.** It was last built Mon 16
    Nov evening and still shows the pre-re-size figures: $29.8k today, $100k-$120k for inflation, and
    $20.2k / $32.3k / $50.9k for the spread. Table 2 has printed the re-sized figures since Tue 17 Nov evening. For the
    charts owner: re-run `build_charts.py`.

## Line costs and Table 3's fit (Letter, Wharton's format; card Q23's method; `measurements.json`)

| Exhibit | Tue 17 Nov evening (HEAD) | Wed 18 Nov evening | Change |
|---|---|---|---|
| Table 1 (Section 2) | 20.9 (75 words) | 20.9 | none |
| Figure 1 | 18.3 (84 words) | 18.3 | none |
| Table 2 | 20.2 (137 words) | **22.2 (169 words)**: one Letter page, 0.5 in under its 9-in block, but no longer between two prose lines | **+2.0** |
| Table 3 | 21.9 (44 words) | **21.9 (44 words)**: one Letter page, between two prose lines | none |
| Section 3's three | 60.4 | **62.4** | **+2.0 lines, about 28 words of prose** |

**Table 3's fit, measured.**
- It measures 21.9 double-spaced lines, 8.39 in from below the prose line above to the prose line after it.
- It sits between two prose lines on one Letter page. Letter's text block is 9 in, 23.5 double-spaced lines.
- **Without a note: 18.9 lines (7.24 in).**
- **How close to the edge:** tonight's measures put the ceiling for an exhibit between two prose lines above 21.9 lines
  and below 22.2 (Table 2 at 22.2 no longer sits there).
- **Its note has about one word to spare.** Tue 17 Nov evening's measure found the table holds the page with a 44-word
  note and not with 46.
- **The rendered preview is one crop of one page:** row 5 prints 0.5%, and no cell runs into a column or a rule.

**Table 2's budget, counted and measured.**
- **The count.** The three edits add 32 words to a terse note, counted clause by clause:
  - the 7.5%'s source and standing, 14: "(J.P. Morgan's 2027 assumption, above the middle of fifteen published
    forecasts, median about 6.5%)";
  - the room under the top, 13 in for 4 out, with "centrally" moved: 12 net;
  - the method, 9 in for 3 out: 6.
- **A cross-check.** A full terse rendering of the note runs 217 words before and 249 after, also +32 (the previous
  owners' 137 is a tighter rendering; the delta method is theirs).
- **So the budget is 169** (was 137).
- **Measured at nine budgets** (filler notes, the build's own `measure()`):
  - 138 words or fewer: 20.2 lines;
  - 139-156 words: 21.2 lines;
  - 157 words or more: 22.2 lines, and the table no longer sits between two prose lines.

## Rendered PNGs, looked at

- **Table 2:** heads, rows and the two full-width lines are unchanged and clear.
  - The result row's second line ("stated top.") sits close above the rule, but they do not touch, and it is the same
    as HEAD.
  - The placeholder note reads cleanly. It still carries the bookkeeping clause "Wed 18 Nov morning, 3e no longer
    carries the method", which is not a reviewer's mark and so is not stripped.
- **Table 3:** see above.
- **Figure 1:** wait labels clear of the number columns; the total row and legend clear.
- **Table 1:** "Range top, flexibility" reaches the right edge of its column but stays inside it (unchanged since
  Mon 16 Nov).
- **No overflow or collision found.**

## Left open, for the lead

1. **Table 2 costs 2.0 more lines, and Section 3 had no headroom.**
   - Section 3's three exhibits now measure 62.4 lines, against 51.4 in SKELETON's Thu 12 Nov arithmetic and 60.4 this
     morning.
   - **Ways back:** 13 fewer words in Table 2's terse note (156 or fewer) give back 1.0 line, and put the table between
     two prose lines again; 31 fewer (138) give back 2.0.
   - **Cheapest cuts:**
     - say "J.P. Morgan, 2027" once for both the 7.5% and the 17.88% (about 3 words);
     - "about 2% centrally" without its two named parts (about 7), if the prose names them once (WORDS: "said with
       its two parts named once");
     - the method as "overlapping, never probabilities" (about 5).
   - The note is written on 27 Nov. Nothing required was cut here.
2. **SKELETON says the "if room" dates item "gives back more"** (row 3e's hand-off and Exhibits item 3). That item (M7)
   was cut from Table 2's note on Mon 16 Nov evening (`REBUILD_2026-11-16_evening.md`), so it has nothing left to give.
   The note's dates item now is M5's "each column's own date", which is required.
3. **"Shares of the past" sits in a note whose "shares" elsewhere means stocks** ("shares 7.5% a year", "draw shares
   with 17.88% volatility"). It is SKELETON's handed-off wording, so it is kept. If a cold reader stumbles on it,
   "proportions of past starting months" says the same.
4. **CANON B15's "Note for the Final Report" column still reads "in the upper third of fifteen houses' figures" (Sun 15 Nov).** The
   exhibits do not print it, and `words_check` now bars it. CANON is not an exhibits file.
5. **The charts owner's `c4_table2_as_dots.png` is stale** (above).
6. **Not re-checked tonight, still open from Mon 16 Nov evening:** `../template/build_template.py` holds its own copy of
   Figure 1's title and note text (another owner's file).

## Second pass, Wed 18 Nov 2026 evening (about 19:55 AEDT)

The coordinator asked for three things, under the same rules:
1. The lead's call (`../../pm/ASK_HUMANS.md`, top row; card Q146): no median figure for the published forecasts.
2. Table 2's note trimmed to 156 words or fewer.
3. `../charts/build_charts.py` re-run in place.

Notes for the store, not report prose.

### 1. No median figure (the lead's call)

**Why.** Card Q146 read Fidelity International's 7.6% (November 2026) at source. With Goldman Sachs's 7.7%, the median is
about 6.5% of fifteen houses, 6.7% of sixteen and 6.9% of seventeen. "Above the middle of published forecasts" holds on
every count.

**What the note says now:** "J.P. Morgan's 2027 assumption, above the middle of published forecasts". It has no median
and no count of houses: "(median about 6.5%)" and "of the fifteen houses named in the References" are gone. The same
wording is now in `exhibit_data.py` (`SHARE_RETURN_STANDING`; `FORECAST_MEDIAN` removed), `build_exhibits.py`,
`tables.md` (now generated) and `specs.md`.

**The checks, rewritten (same count, 450).**
- The 6.5% comparison is gone. A new check reads every median 8v names (6.5% of fifteen, 6.9% of seventeen) and
  asserts 7.5% is above each. These medians are checked but never printed.
- 8v must carry the phrase and say "the report gives no median figure".
- The lead's call must be in ASK_HUMANS ("with no median figure", naming Table 2's note).

**New guards.**
- `words_check` has a twelfth pattern, `median (about|of) N%`. It stops the build if a median figure appears in any
  exhibit text. "Upper third" was already a pattern.
- `carry_check` now fails on "median about", "fifteen" or "upper third" in Table 2's note.

### 2. Table 2's note trimmed: 169 to 153 words

Counted clause by clause against Tue 17 Nov's terse note, the first pass added 32 words. The second pass adds 16, so the
budget is 137 + 16 = 153. Full terse rendering: 233 words, against 217 before the morning's edits.

| Clause | First pass | Second pass (terse) | Words added |
|---|---|---|---|
| The 7.5% and the 17.88% | "... rows 1 and 3 (J.P. Morgan's 2027 assumption, above the middle of fifteen published forecasts, median about 6.5%); ... 17.88% volatility (J.P. Morgan 2027) ..." | "Shares return 7.5% a year in rows 1 and 3 (J.P. Morgan's 2027 assumption, above the middle of published forecasts) and, in 3b's simulated futures, its 17.88% volatility; yields there move about 0.9 points a year ..." | +7 (was +14) |
| The rate past the margin | "used up the room under the top (the 0.5% margin plus the rounding down, about 2% centrally)" | "used up the room under the top (about 2% centrally)" | +5 (was +12) |
| The starting months | "(overlapping starting months, shares of the past, never probabilities)" | "(overlapping starting months, past frequencies, never probabilities)" | +4 (was +6) |

**Three calls in the trim.**
- **J.P. Morgan is named once.** "Its 17.88% volatility" takes its source from the parenthesis before it.
  - `carry_check` asserts "J.P. Morgan" appears exactly once in the items and in the placeholder.
  - `exhibit_data.check()` still reads 17.88 in NUMBERS 0, and CANON B15 carries "AC World Equity 7.50 8.94 17.88".
- **"About 2% centrally" now stands without its two parts.** The coordinator's condition holds: the note still names
  both parts, in the range-rule item ("less the fees to 15 Dec 2032 and 0.5%", "the bottom rounded down to $5,000",
  "rounded down once").
  - The item's source pointer says so, and `carry_check` now requires all three range-rule phrases in place of the
    room item's old "(the 0.5% margin plus the rounding down".
  - WORDS asks that the room under the top is said once with its two parts named (the lay reader, Wed 18 Nov). The note
    names them in the range rule, so 3c's prose should name them the first time it uses the term.
- **"Past frequencies", not "past share markets".** SKELETON's "shares of the past" means that the spread rows are
  proportions of past starting months, never probabilities. "Past share markets" would name what was replayed (U.S.
  yields and stocks, both) instead of what the percentiles are. "Past frequencies" keeps the meaning, and the note's
  "shares" (stocks) can no longer be confused with it.
  - The coordinator's "overlapping starting months ... never probabilities" is kept at both ends.
  - The SKELETON check now asserts SKELETON's own phrase and that the note's version keeps both ends.
  - **For SKELETON's owner:** row 3e's hand-off and Exhibits item 3 still read "shares of the past".

**No figure was cut** except the median, which is the lead's call; every figure the note's checks require is still
printed (7.5%, 17.88%, 0.9, about 2%, about $120, the curve's date, 5%, $18,500 to $28,700, $31,800). The only changes
to checks are the three described in part 1.

**Measured** (the build's own `measure()`, card Q23):

| Table 2's note | Words (terse budget) | Lines | Between two prose lines |
|---|---|---|---|
| Tue 17 Nov evening (HEAD) | 137 | 20.2 | yes |
| First pass tonight | 169 | 22.2 | no |
| **Second pass** | **153** | **21.2** (8.11 in) | **yes** |

The steps measured in the first pass hold: 138 words or fewer gives 20.2 lines; 139-156 gives 21.2; 157 or more gives
22.2. So 153 leaves 3 words before the next line, and 15 more words cut would give back the last 1.0 line.

### 3. The charts, re-run in place

`python3 -B keel/final_report/charts/build_charts.py`: **37 of 37 PASS**, exit 0.
- **`c4_table2_as_dots.png` and `.svg` now carry the re-sized figures,** the same as Table 2: $28.7k; $18.5k, $19.6k,
  $20.5k and $27.6k; inflation $100k-$115k; the spread $19.4k / $31.8k / $50.2k. Looked at; nothing collides.
- **The other six charts:** their PNGs came out byte-identical, and their SVGs differed from HEAD only in dates and
  element ids, so they were restored from HEAD.
- **For the charts owner:** `build_charts.py` itself still reads the 2026-11-15 results files for its own checks.
  They pass, and they were not edited here.

### Check results (second pass)

- **`exhibit_data.py`: 450 checks, 449 PASS, 0 FAIL, 1 flagged.** The flag is Figure 1's rounding pair, as before.
- **`words_check`: 240 exhibit texts x 12 patterns, 0 FAIL.**
- **`carry_check`: 26 checks, 0 FAIL.** Six musts and six nevers, each in the items and in the placeholder, plus "J.P.
  Morgan" once in each.
- **Build: exit 0.** The two review-PDF warnings are unchanged: the placeholder notes of Tables 1 and 2 run over a page
  break.
- **Byte-identical to HEAD:** `table1_holdings_2x.png`, `table3_monitoring_2x.png`, `figure1_reserve_2x.png`,
  `exhibit2_reserve.png`; `figure1_reserve.svg` was restored, since it differed in metadata only. `s2_fit` is 626 / 46.
- **`table2_markets_2x.png`:** the body is unchanged and the placeholder note shorter; looked at, with no overflow or
  collision.
- **`tables.md`:** the Table 2 note line, its page cost, and a new dated second-pass header line. The first pass's header
  line is now static text that gives no median.

### Line costs and Table 3 (second pass)

| Exhibit | Tue 17 Nov evening (HEAD) | First pass | **Second pass** |
|---|---|---|---|
| Figure 1 | 18.3 | 18.3 | **18.3** |
| Table 2 | 20.2 | 22.2 | **21.2**, between two prose lines |
| Table 3 | 21.9 | 21.9 | **21.9** (8.39 in; 18.9 without a note), one Letter page, between two prose lines |
| Section 3's three | 60.4 | 62.4 | **61.4** (+1.0 line on HEAD, about 14 words of prose) |

Table 3 is unchanged and was re-measured. It still has about one word of note to spare: 44 holds the page, 46 did not
on Tue 17 Nov evening.


## Third pass, Wed 18 Nov 2026 evening (about 20:45 AEDT)

The coordinator asked for three things, under the same rules (exhibits and charts only, one "Done" line in NUMBERS
section 9, no commit):
1. Table 3 row 4 in the lead's call, the numbers owner's wording (NUMBERS 3, "An early end of the late-2032 fund after
   the move"; section 0's dated line; section 9's open item).
2. Bond desk 5 (`../research/panel/2026-11-18_bond_desk_5_3c_table3_3e.md`) where it concerns a table: H1, H2 for row
   7, H3, M5 and M6.
3. The no-median rule kept in Table 2's note.

Notes for the store, not report prose. Section 3's exhibits stay inside their line budget: every change was measured
cell by cell before it went in (a scratch harness on the build's own `measure()`, outputs in the session scratchpad).

### 1. Table 3 row 4: what the 0.5% margin pays, and what it cannot

| | Before | Now |
|---|---|---|
| Cell | "*Changes:* the fund; a gap met from the 0.5% margin the payments and the range each carry. *Never:* a sale of shares." | "*Changes:* the fund; trading costs from the 0.5% margin, lost interest from what its cash earns. *Never:* a sale of shares." |

- **Why.** NUMBERS 3's new block: the margin pays a swap's costs; it does not pay the interest the fund's holdings
  still had to pay when the fund ends early, merges or moves its end. With cash waiting earning nothing an IBTM end in
  2031 leaves the stated top up to $4,589 short. So the old cell promised what the margin cannot do (bond desk 5, M2).
- **Fitted to the row's four lines (measured).** The suggested wording, "its trading costs ... lost interest from what
  waiting cash earns", took a fifth line ("shares." alone) and put Table 3 off its page. So did "trading costs ...
  what waiting cash earns" and "... what cash waiting earns". Wider last columns (2.15 in, from any of the other
  four) did not help. "What its cash earns" keeps four lines and says whose cash waits: the ended fund's payout, in the
  short-term Treasury ETF (the 3e list's one action per event). Both of the owner's parts are kept; "its" before
  "trading costs" went.
- **The 3e list splits the same way** (section 9 asked for it). "A payment's gap comes from the 0.5% margin ... the
  floor's gap comes from the range's 0.5% cut" now reads "a swap's trading costs come from the 0.5% margin (for a
  payment, the margin the extra Treasuries carry for the ten ...; for the range, its 0.5% cut), and the interest an
  early end, merger or moved end loses comes from what the fund's cash earns while it waits".
- **A new 3e-list item gives the size**, read from `results_fund_exit_2026-11-18.json` and checked against section
  3's text:
  - with cash waiting earning nothing: the top up to $4,589 short (covered from January 2032), the bottom up to $2,887
    short (for an end to October 2031), the ten $1,827 short for an end on 1 Jan 2031;
  - at today's market rates nothing is short (the top at least $7,295 over);
  - none of the five ended iBonds Treasury funds ended a year early (8h);
  - IBTM carries the 2033 payment, the bottom and the top, so one notice touches all three (bond desk 5, M2's
    concentration point).
  No probability is given (a board's call, card Q36).

### 2. Bond desk 5 in the tables

**H1, one fund behind the top, bought twice (Table 2's note).** The floor and the shares moved into Treasuries both buy
IBTM, the late-2032 Treasury fund.
- The range-rule item now reads "units of the late-2032 Treasury fund held x its remaining coupons ...". So both ends
  are that fund's units by the rule's own definition. "The shares moved into Treasuries" keeps WORDS's name.
- "If the funds' costs beyond their fees used up the room under the top (about 2% centrally ..." now reads "If the
  fund's costs beyond the fees used up the room under the top (about 2% of what it pays, centrally ...". "Of what it
  pays" gives the 2%'s base: a share of what the fund pays on both purchases, in all ($115,000 / $117,731, 8u). That
  also answers bond desk 5's M1 point that "2%" reads as a yearly rate.
- The flexibility item says "whatever the fund pays above the top".
- Table 1 (IBTM "2033 and the floor") and Figure 1's note (the floor's IBTM shares a separate lot) already said one
  fund. No other table names two.

**H2, row 7 (Table 3).**
- The trigger reads "Taiwan dollar 10% stronger than in 2031: alone, $11,500 more on her $115,000 part". The contribution
  is her part of the building budget, not the building's whole budget. "Of the building budget" did not fit.
- The change reads "*Changes:* her flexibility ($28,700 in 2033 with anything above the top, shares at 7.5%)". The
  $28,700 rests on shares earning J.P. Morgan's 7.5% a year, and the cell now says so. "A call on her flexibility"
  became "her flexibility" (what changes) to keep four lines. "A call on ...; shares 7.5%" and "shares 7.5% a year"
  each took a fifth.
- The 3e list says the cover moves with the share forecast, not with interest rates alone.
- The 25% figure itself is 3e's prose, not a table's. It is not printed in any exhibit.

**H3, the range's date (Table 2's note).** The first item now reads "MODEL, not forecasts; Treasury curve of 6 Nov 2026,
the day trading froze". Its reviewer's mark says it is never re-sized to a later curve (NUMBERS 4, "On a later curve":
13 Nov 2026's curve states $105,000 to $125,000, disclosed, never re-booked). Table 3's note already dates "today's
rates" to the same curve. Nothing is re-sized.

**M5, row 5 (Table 3).**
- (a) Done in the cell: "First trading day, funds within 0.5% of net asset value" (was "prices within"). The 0.5% is
  the fund legs' test (NUMBERS 4: "Table 3 row 5's 'of net asset value' covers the fund legs"). "Fund prices" and
  "fund legs" each took a fourth line.
- The bonds' 25-basis-point curve test stays in the 3e list. A bond test in the cell would take the table off its page.
  The 1.8%-2.8%-of-price reading is bond desk 5's scratch arithmetic, not a register figure.
- (b) Left open: which net asset value, see below.

**M6, row 7 (Table 3).**
- (a) The carry-on cell reads "five-year building costs 1.5% to 5.0% a year" (was "building-cost trend"). Its note item
  is now "building costs: DGBAS construction cost index, to October 2026" (the same word count).
  - The 3e list gives both readings (8d): the five-year rate, 3.19% a year to October 2026, is inside the band; the
    latest year, +7.18%, is outside it.
  - "Five-year building-cost rise ... a year" took a fifth line.
- (b) "Alone," marks the $11,500 as the currency's share. "(the currency alone)" took a fifth line.
  - The 22.3% has no room in the note. Table 3 holds its page with a 44-word note and not with 45, measured tonight on
    the old rows and on the new.
  - So the 3e list carries 8q's card Q131 spans: 30 of 406 two-year spans since 1991 with a Taiwan dollar 10% or more
    stronger; the US-dollar cost rose 9.3% to 29.0%, and 22.3% in the middle span. That is about $25,600 on her
    $115,000 part, inside the row's $28,700 with about $3,100 to spare.
  - `words_check` bars "median N%" (the published forecasts' guard, card Q146), so the span's median is said the
    other way.

### 3. The no-median rule

It stands. Table 2's note still says "J.P. Morgan's 2027 assumption, above the middle of published forecasts", with no
median and no count of houses. `words_check`'s twelfth pattern, `median (about|of) N%`, caught one draft line of the 3e
list. That line was reworded, and the pattern was not weakened.

### Line counts (measured, `measurements.json`)

| Exhibit | Second pass | **Third pass** |
|---|---|---|
| Figure 1 | 18.3 (84 words) | **18.3** |
| Table 2 | 21.2 (153 words), between two prose lines | **21.2 (154 words)**, between two prose lines |
| Table 3 | 21.9 (44 words; 18.9 without), one Letter page, between two prose lines | **21.9 (44 words; 18.9 without)**, the same |
| Section 3's three | 61.4 | **61.4** |
| Section 2 fit | 626 / 46 | 626 / 46 |

**Table 2's budget, counted.** I wrote a full terse rendering of the note before and after: 254 and 255 words, so +1
and the budget is 154 (was 153). The clauses:
- the curve's date, +4 (H3);
- the fund named in the range rule, +2 (H1);
- "the fund's costs ... (about 2% of what it pays", +4 (H1);
- paid for by "(our own assumption)" for "(our own assumption, not a market figure)", -4;
- "above the top" for "above the stated top", -1;
- the dates item with each date said once ("to the floor's trade day, Mon 3 Jan 2028; the top to the move's, Thu 2 Jan
  2031, before the 2031 meetings; her flexibility to January 2033"), -4.

No fact was cut. The measured steps hold: 139-156 words gives 21.2 lines and 157 gives 22.2 (re-measured tonight at 153,
154, 156 and 157). So 154 leaves 2 words.

**Table 3, cell by cell.** The changed cells kept every row's height:
- row 4: four lines;
- row 5: three lines;
- row 7: four lines in each of its three cells.

The note items have the same terse length. Table 3 has no word to spare: 45 words take it off the page, on the old rows
too.

### Checks

- **`exhibit_data.py`: 463 checks, 461 PASS, 0 FAIL, 2 flagged** (was 450).
  - Figure 1's rounding pair, as before.
  - New, `WATCH`: WORDS's "room under the top" row still says "the two Treasury funds behind the top" (bond desk 5, H1).
    WORDS is another owner's file, being edited tonight. The check reads the row either way and flags it; it never
    fails it.
- **New checks:**
  - row 4's figures against section 3's table and text ($4,589, $2,887, $1,827, $7,295; covered from 1 Jan 2032; short
    to 1 Oct 2031; nothing short at today's market rates; none ended a year early);
  - the cell against section 9's suggested words (both parts kept, the old promise gone, the 3e list split);
  - 8q's 30 of 406, 22.3%, 9.3%, 29.0%, $25,607 and $3,075, and the same $28,682 as row 7;
  - 8d's 3.19% and +7.18% against the band;
  - row 7's "her $115,000 part" and "shares at 7.5%";
  - "7.5%" added to the numbers the table may print.
- **`words_check`: 244 exhibit texts x 12 patterns, 0 FAIL.**
- **`carry_check`: 40 checks, 0 FAIL** (was 26). New musts: "units of the late-2032 Treasury fund held", "the fund's
  costs beyond the fees", "whatever the fund pays above the top", "Treasury curve of 6 Nov 2026, the day trading froze",
  and the room item with "of what it pays". New nevers: "the funds' costs", "the funds pay", "two Treasury funds".
- **Build: exit 0.** The two review-PDF warnings are unchanged (Tables 1 and 2: their placeholder notes run over a page
  break). A second rebuild reproduces `tables.md` line for line.
- **Byte-identical to before the pass:** `table1_holdings_2x.png`, `figure1_reserve_2x.png`, `exhibit2_reserve.png`.
  `figure1_reserve.svg` differed in metadata only, so it was restored.
- **Changed:**
  - `table2_markets_2x.png` (the placeholder note only);
  - `table3_monitoring_2x.png` (rows 4, 5 and 7);
  - `exhibits_letter.docx` and `.pdf`;
  - `tables.md`, `measurements.json`;
  - `exhibit_data.py`, `build_exhibits.py`;
  - `specs.md` (a dated pointer, and "the fund pays" in Table 2's spec).
- **PNGs looked at.**
  - Table 3: row 4's "*Never:* a sale of shares." ends its fourth line; "five-/year" breaks at its hyphen; nothing runs
    into a rule or a column.
  - Table 2: the body is unchanged and the placeholder note reads cleanly.
- **Charts.** `../charts/build_charts.py` was run in a scratch copy writing to the scratchpad: 37 of 37 PASS, and all
  seven PNGs are byte-identical to `charts/`. Charts read only Table 2's rows, which did not change, so nothing in
  `charts/` was written.

### Left open

1. **WORDS row "the room under the top"** still says "the two Treasury funds behind the top" (H1). This is for WORDS's
   owner, and the WATCH clears when it changes. SKELETON 3e's note 2 (bond desk 5: SKELETON.md:47) and NUMBERS 8u's
   "the two funds" are for their owners too.
2. **M5 (b), which net asset value** (the last published, or the intraday indicative value a limit is set against).
   NUMBERS 4 does not say, so the cell keeps "net asset value". This is for the numbers owner before the row names
   another.
3. **Row 7's "her $115,000 part"** drops "of the building budget" to fit. 3e's prose says it in full (H2's sentence).
4. **The 22.3% joint move** is in the 3e list only. In the table or its note it costs a line, and Table 3 has none.
5. **Bond desk 5's other table points, not in this brief:**
   - L3 (Table 3's note "cash dates: fund payouts" makes every month a cash date; "fund end payouts" is one word more in
     a note with none to spare);
   - M4 (row 1's $57,455 against Figure 1's fee basis, $58,775);
   - L4 (S&P's five-day test is for notes and bonds).
   They are listed for the lead. None was changed here.
