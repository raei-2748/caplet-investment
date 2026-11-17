# Numbers run, Tue 17 Nov 2026, evening: the ten payments carry the 0.5% margin

Numbers worker of the Tue 17 Nov evening run. MODEL throughout (Keel's calculation on the 6 Nov 2026 curve, design
H_plain). Keel's call, logged in `../../pm/ASK_HUMANS.md` (Tue 17 Nov, evening): the re-size the 07:00 call set for the
Wed 18 Nov morning run is done tonight, "so no file carries a figure the register knows is short".

## 1. What changed

- **The margin.** The backstop (the extra Treasuries) is sized by the same linear programme so the ten are paid if no
  coupon earns anything, after the bill ETF's 0.15% fee, with every iBond fund flow 0.5% smaller
  (`completion.PAY_MARGIN = 0.005`, `completion.cost_cut`). The design without it is kept as `H_plain_nomargin`
  (comparison only; `cost_cover.py` part B runs on both).
- **The day count.** `engine.T01` (2027's 365 days over 365.25) in every one-year carry; `plan.py`'s $1.14 (8k) is gone.
  Alone it moves no headline figure by a dollar: the top-up $2,388.22 to $2,388.15; the no-margin design costs
  $336,655.82 before and after.
- **Every results file re-run and dated 2026-11-17** (`completion.RESULTS`); the 15 and 16 Nov files are kept as the
  record; this morning's cost-cover file is `results_cost_cover_2026-11-17_morning.json`. Every script's asserts were
  moved to the new values and pass.

## 2. Old and new, side by side (central, today's forwards, VT 7.5%)

| Figure | Before (Sun 15 / Mon 16 Nov) | Tonight |
|---|---|---|
| Stated range, rounded | $95,000 to $115,000 | **$95,000 to $115,000 (unchanged)** |
| Stated range, unrounded | $98,380 to $118,072 | $97,605 to $117,142 |
| Top-up (Jan 2028 money) | $2,388 | $2,388 |
| Extra Treasuries, Jan 2028 money / 1 Jan 2027 money | $35,894 / $34,369 | **$36,774** / $35,213 |
| First part of the 2028 deposit (top-up + extra) | $38,282, 25.5% ("about $38,000") | **$39,162, 26.1% ("about $39,000")** |
| Floor money / share of the deposit | $81,889 / 54.6% | $81,244 / 54.2% |
| VT bought Jan 2028 / share of the $450,000 | $29,829 / 6.63% | $29,594 / 6.58% |
| Floor pays, late 2032 | $103,178 | $102,365 |
| What the funds pay | $123,476 | $122,503 |
| Excess above the top | $8,476 | $7,503 |
| Half kept | $21,347 | $21,179 |
| Her flexibility (half kept + excess) | $29,823 | $28,682 |
| Reserve on 1 Jan 2033 / funded | $444,545 / 111.4% | **$445,655 / 111.7%** (about $1.12 for each $1) |
| Backstop: 2042 at forwards / 1 Jan 2033 / 1 Jan 2027 money | $74,123 / $45,456 / $34,345 | $75,934 / $46,566 / $35,185 |
| Backstop's cost carried to 1 Jan 2033 | $45,487 (gap $31) | $46,603 (gap $37) |
| Face bought / own interest / flows / ETF fee | $36,867 / $19,143 / $56,010 / $90 | $37,711 / $19,489 / $57,200 / $103 |
| Escrow release, 2033-2042 | $58,603 | $59,835 |
| Figure 1's total row (zero interest, fees) | $444,080 + $55,920, nothing left | $444,080 + $55,920, **$1,177 left** |
| Figure 1's own basis on 1 Jan 2033 | $425,319 | $426,371 |
| What returns to Laura (8k) | $75,298 | $75,266 |
| Design cost (1 Jan 2027) | $336,656 | $337,499 |
| Left after completing / floor's expected interest | $111,718 / $21,289 | $110,838 / $21,121 |
| Deletion test (VT to zero): floor pays / excess | $103,178 / $8,178 | $102,365 / $7,365 |

**Steps crossed** (none central): house 1-in-20 stated bottom $80,000 ($85,000); history 1-in-20 high top $125,000
($130,000); 8i's inflation world top $115,000 ($120,000; Table 2); 8o's 70% moved $120,000 ($125,000), 30% moved
$105,000 ($110,000); 8p row e $105,000 ($110,000), 1-in-20 high $125,000 ($130,000); **13 of 15 houses give a $115,000
top (14)**, Ninety One joining GMO at $110,000; 5(e) after a 2-point fall $55,000 ($60,000).

**Moved, not stepped:** 8j Taiwan dollar 92.9% / 99.74% (93.3% / 99.80%; about 1 in 380, was 1 in 510); history 96.9%
(97.1%); joint 99.1% (99.3%); real currency 98.3% (98.1%); "most" fails at 1.30 points (1.33), in 70 of 200,000 paths
(55); the $75,000 deposit meets the standard in 99.965% (99.97%); the standard takes the whole deposit at a 3.57-point
fall (3.60); custody peak $587,008 ($587,039); "keeping 30%" now buys one $5,000 step, not two (FACTS_PLAIN fixed).

## 3. Checks

- Every re-run script's asserts pass (re-run again after the docstring edits: `topup_paid`, `most_check`,
  `returns_check`, `share_split`, `custody`, exit 0). `returns_check.py`'s two routes agree to $0.31.
- `exhibits/exhibit_data.py`: 439 figures, 438 PASS, **0 FAIL**, 1 flagged (as before); `build_exhibits.py` rebuilt
  `tables.md`, the PDF, the PNGs and `figure1_reserve.svg`; words check 0 FAIL; Table 3 still one page.
- Card Q98's script, run on the re-sized engine (scratch copy; the card's file untouched), gives the register's
  $2,388, $36,775 and $39,163 on 6 Nov (within $1, its own carry).
- The design without the margin costs the same before and after the day-count fix ($336,656), so every move is the
  margin's.

## 4. Files swept tonight (line numbers as of tonight)

- `NUMBERS.md`: header block "What changed on Tue 17 Nov, evening" and the living headline; sections 2, 4 (table,
  certainty table, VT-growth table, deletion test, capital-protection and backstop bullets), 5 (3.57 points, the later-curve
  line, 5(d)'s key-rate reading), 8c, 8g, 8h, 8j, 8k, 8o, 8p, 8q, 8r, 8s (99.965%; "What none cost"), 8t; section 9 items
  closed; section 10's new block.
- `SKELETON.md` l.38, 43, 44, 45, 47, 87, 203, 226, 247, 248, 261, 262, 264, 265, 287, 292 (3a's headline now "about
  $39,000"; 3b's "about $30,000" now "about $29,000", parts about $21,200 and $7,500; Table 3's 3.57 points and $55,000).
- `INTENT.md` l.44, 50, 54 (the margin said), 57, 66, 90, 133, 143, 145.
- `CONCEIT.md` l.64, 66, 270, 273, 274, 294, 295, 298, 299, 316, 320, 334, 336, 342, 357, 444, 472.
- `WORDS.md` l.21, 22 (the reserve's size printed once, in Figure 1's note), 23, 24 (M9's basis: the ten payments carry
  the 0.5% margin), 26 (about $1.12), 27, 30, 62, 63, 65, 70.
- `voice/FACTS_PLAIN.md` l.27-28, 37-39, 46, 54-55, 61, 106, 120, 147, 159.
- `research/goldmine/AHA_REGISTER.md` l.25 (row 5), 26 (row 6), 27 (row 7), 30 (row 10: what "none" cost), 44, 57.
- `research/goldmine/GOLDMINE.md` l.38 (13 of 15).
- `CANON.md` l.202 (D8, its "Numbers needed" column only: dated note on the stale $1,544).
- `exhibits/exhibit_data.py` (register date 2026-11-17; five 8h regexes, two section 5 regexes, the column-total check
  now adds the $1,177 left, `SHORT_PER_TENTH` 118, `FALL_TAKES_WHOLE_DEPOSIT` 3.57, comments), `exhibits/build_exhibits.py`
  (Figure 1 note item 2 adds "$1,177 to spare, the 0.5% margin"; item 4 drops "the Wed 18 Nov re-size moves it"),
  `exhibits/tables.md` regenerated.
- Docstrings: `numbers/custody.py`, `most_check.py`, `share_split.py`, `topup_paid.py`.
- `CASE_MAP.md`: nothing to change (its "about $30,000" and "about $21,000" are other quantities).
- `../../pm/ASK_HUMANS.md`: Keel's call row.

## 5. Section 9 items (job 2)

- **Q98's later curve:** in NUMBERS 5, dated. On 13 Nov: no top-up, $6,203 of the first deposit left over, extra
  Treasuries $38,277, the deposit's first $32,074 to the payments, floor money $86,440, VT $31,486.
- **5(d):** on the ten's own key rates the fall that breaks "most" (1.30 points) came in 1.21% of 56-day windows since
  1962, about half the 1-year's 2.4%; 0.31% from a 10-year of 3.5%-6.5% (Oct-Nov 2008 only), against 0.20%.
- **CANON D8:** dated note added (top-up $2,388, 1.6% of the deposit; first $39,162, 26.1%).
- **8l's EXTAUS entry:** already in `research/REFERENCES_APA.md` row 141 (added 11 Nov); items closed.
- **Q81 row 9:** confirmed on the re-run: 16-year windows Jan 2006 to Dec 2008 (36 starts); 15-year Jan 2007 to Dec 2008
  (24). 8a states both; no working file quotes the row.
- **Aha test 4, what "none" cost (Keel arithmetic, NUMBERS 8s):** in the 27 Sep model's own terms the Treasury-first plan
  left about $19,000 less above the ten at the median ($207,290 against $226,096; 1-in-20 low $159,224 against $19,990);
  Caplet's plan on today's engine about $65,000 less at the median ($191,066 against $256,543), 1-in-20 low $158,942
  against $280.

## 6. Open items

1. **3b's flexibility figure.** SKELETON now says "about $29,000" ($28,682) where it said "about $30,000"; elsewhere
   "about $28,700". The writers pick one rounding for 3b.
2. **"If cash waiting earns nothing, none"** (WORDS l.27, l.70; SKELETON; INTENT; CONCEIT; AHA): with the margin,
   $1,177 is left after 2042 at zero interest when the funds cost nothing beyond their fee. "None" holds under the
   standard as sized (a 0.5% cost uses it); the wording owner decides whether to keep it.
3. **CANON A19 and B29** quote the same stale "$1,544 over" in their check columns (not edited; D8 only, as asked).
4. **Not edited, owners replace from the register:** `research/meta/BOLD_THESES.md`, `EVALUATE_NOT_DESCRIBE.md`,
   `research/gem2/G2_3a_read.md`, `G4a_3c_read.md`, `G5_T3_3f_read.md`, `exhibits/specs.md` l.211-212,
   `AHA_REGISTER_candidates.md`, `aha_candidates_2026-11-16.md`. Cards, the store and dated records stand (NUMBERS 10).
5. **CLAUDE.md** still gives $35,894, $38,282, $444,545 and "14 of 15", and says the ten carry no margin until
   Wed 18 Nov: for the lead's commit.
6. **FACTS_PLAIN l.105** says "most of that money comes back", which WORDS l.27 (M11) forbids; a voice owner's fix.
7. **Not run:** a "what none cost" figure inside `first_plan.py` (tonight's is scratch Keel arithmetic, in 8s with its
   limits); the joint replay's month names for the lowest all-money figures in 8n (Sun 15 Nov's, not re-listed).
