# Fixes applied: coherence reader 7 and lay reader 3 (Tue 17 Nov 2026, evening, Sydney)

Inputs: `2026-11-17_coherence_reader_7.md` (H1, M1-M15, LOW 1-11) and `2026-11-17_lay_reader_3a_3c_3e.md`, with the
lead's calls of Tue 17 Nov. These are planning notes only; no Final Report prose. NUMBERS.md, the cards, the store and the
frozen record (IPS, CANON, TNA, WInS notes) were not edited. Line numbers are as the files stand after this run.

**Count.** 37 items in all: H1 and M1-M15 (16), LOW 1-11 (11), the lay reader's ten points (10). Fixed: 35. Left with
a reason: LOW 8 (NUMBERS only) and M12's two leftovers, which are records rather than wording (both explained below).
M10's two NUMBERS lines are also left for NUMBERS' owner; M10 is otherwise fixed.

**Exhibit build after every change:** 439 figures, 438 PASS, 0 FAIL, 1 flagged (the known $1 rounding of Figure 1's
footing); words check 238 texts x 8 patterns, 0 FAIL. Table 3: 21.4 lines with a 44-word note, one page (18.4 without
the note). Figure 1 18.3 lines (was 17.3), Table 2 20.2 lines (was 18.2), Table 1 unchanged at 20.9.

## HIGH

**H1. 3f's second moment gave the 3.2% as the reason.** Fixed. The lead's call: the cause is IPS l.9's reason, how a
writer is paid, told in the team's words, never the IPS's sentence (CANON A3). The 27 Sep model's 3.2% is only the check
that priced the change ("we checked it": about 1 in 31 against none from January 2028).
- `SKELETON.md` l.266 (3f reservoir, moment 2): rewritten under that cause. It notes that the team's notes of 27 Sep
  already say "lumpy income" (`keel/library/council_2026-09-27/team_notes_2026-09-27.md` l.33).
- `SKELETON.md` l.208 (conceit table, 3f): the knockout turn is told under the change's own cause, and the 3.2% is what
  the check showed.
- `SKELETON.md` l.233 (aha table, 3f): now row 10 version B, with 3.2% as the check and never the reason.
- `CONCEIT.md` l.69 (V2.2, 3f): rewritten the same way, so 3.2% is never the reason. The aha column now reads "for the
  IPS's own reason".
- `CONCEIT.md` l.301 (section 4, the first plan): was "Store only"; it is now 3f under the IPS's cause, with 3.2% as the
  check.
- `AHA_REGISTER.md` row 10 (l.30): the lead's call is added at the head of the row. The part and the job stay 3f, the
  reason is IPS l.9's and the 3.2% is the check. The evidence column cites IPS l.9 and CANON A3.
- `PEOPLE_IN_THE_ROOM_2026-11-16.md`:
  - l.176's keep-out rule is struck, with a dated note; it now keeps out the 3.2% as the reason, and the IPS's own
    sentence;
  - moment B's "Say" (l.163-168) now gives the cause and then the check;
  - the l.103 provenance note, the l.225 table row and the l.262 proposal each carry the same correction.

## MEDIUM

**M1. The reserve's size was gone.** Fixed in an exhibit, by the lead's call. Figure 1's note item 4 (`build_exhibits.py`
l.309) now carries the operating reserve's size on 1 January 2033, printed once at today's rates. It reads about $444,500
and moves with the Wed 18 Nov re-size. It never sits beside the total row.
- `SKELETON.md` l.43, 3a's exhibit and store columns, and l.260, the 3.0 reservoir ("its size printed once, in Figure
  1's note item 4"). If the lead moves the size into 3a's prose, it takes one of 3a's three figures, never a fourth.
- `DENSITY_CUT` l.200 carries a dated note.

**M2. $444,545 against $444,080.** Fixed in the exhibits. Figure 1's last row is relabelled "Paid 2033-2042, added up"
(`exhibit_data.py` l.352; drawn at `build_exhibits.py` l.193, l.952). A check (`exhibit_data.py` l.908) confirms three
things: the label has no "total", it names 2033-2042 and "added up", and the row's figure is not the reserve. The label
is adapted, not taken word for word. The reader's "paid by each payment's own Treasury" names only the first of the
row's three columns, so it would make $500,000 read as paid by the own Treasuries alone. **The lead may prefer the
reader's wording.**
- `DENSITY_CUT` l.218-222 carries a note: the two figures need no reconciling, and $425,319 is the size on Figure 1's
  own basis.
- Left: "Reconcile" in `NUMBERS.md` l.2170 is NUMBERS' to strike.

**M3. The payments' margin.** Fixed. "The 0.5%" and "well inside the margin" are now tied to the range only. Where a note
must speak of the payments, it says they carry the same 0.5% from the Wed 18 Nov re-size.
- `SKELETON.md`:
  - l.47, 3e's density row: "small in the ended funds";
  - l.77, Book 17's amendments;
  - l.179, 3e's two versions.
- `CONCEIT.md` l.431: the iBond bullet.
- `DENSITY_CUT` E15 (l.139).
- Table 3 row 4 (`exhibit_data.py` l.594): "any gap met from the extra Treasuries, or for the range its 0.5% margin".
- A grep finds no other place that gives the payments a margin.

**M4. "Guaranteed".** Fixed. There is now one rule in `WORDS.md` l.24 and `CONCEIT.md` l.49: "guaranteed" and "certain"
take the Treasuries, or the stated range after the move, as their subject, never a fund's payout and never a dollar
figure. WORDS's earlier refusal of coherence reader 6's M2 is replaced and named as replaced.

**M5. Two retired turns.** Fixed.
- "Let the ink dry" is struck from:
  - `SKELETON.md` l.45 (3c's density row) and l.205 (conceit table, 3c);
  - `CONCEIT.md` l.66 (V2.2, 3c), where it is replaced by round 6's "two inkings, two dates";
  - `AHA_REGISTER.md` row 7's turn column (l.27).
- "The key plate" is struck from `SKELETON.md` l.199 and `CONCEIT.md` l.60.
- The early-statement figure now reads "the move would buy less than a top stated a year early in about 11 of 100
  futures" in `SKELETON.md` l.45, `CONCEIT.md` l.66, l.272 and l.339, `AHA_REGISTER.md` row 7 and `DENSITY_CUT` C14.

**M6. $103,178 in 3e.** Fixed. The deletion test now reads "the payments unchanged and the range one figure, the bottom",
with no payout figure. It is changed in `CONCEIT.md` l.68 (V2.2, 3e), l.299 (section 4, VT row) and l.337 (parallel 4),
and in `AHA_REGISTER.md` l.34. Nothing in SKELETON placed it in 3e's prose.

**M7. Table 1 described two ways.** Fixed, in the lead's one description: our WInS portfolio, Laura's plan as it will
stand after January 2028 with both deposits scaled to $300,000. It leaves out the top-up and the extra Treasuries (bought
in 2028 at the day's rates), it is before half the shares move into Treasuries ahead of the 2031 meetings, and its dollar
split is not Section 3's.
- It replaces the old wording in `SKELETON.md` l.38 (2.1 density) and l.199 (conceit 2.0-2.1), `CONCEIT.md` l.60 and
  `WORDS.md` l.41.
- In plan notes it uses WORDS's name, "our WInS portfolio"; "WInS book" is banned in the report.

**M8. INTENT's "the only thing".** Fixed. `INTENT.md` l.23-26 now reads: ten years of her operating commitment owned in
Treasuries, a base, not the residency's whole budget. It cites H9-119 and case l.85-86.

**M9. 3d's bare $115,000.** Fixed. `SKELETON.md` l.46: Laura's words stay bare. The team's lead-in says once that the
figures are today's, and that the rule sets the bottom in January 2028 and the top in January 2031. The reader's text
says the rule sets "them" in January 2031; the bottom is set in January 2028, so the lead-in names both dates.

**M10. "No interest" as shorthand.** Fixed in the plan files; left in NUMBERS.
- Now "if/even if cash waiting earns nothing":
  - `SKELETON.md` l.43 and l.162;
  - `WORDS.md` l.24, l.30 and l.59;
  - `AHA_REGISTER.md` row 5;
  - `CONCEIT.md` l.293 and l.470.
- The exhibit check labels in `exhibit_data.py` now say "the extra Treasuries" (l.1016, l.1031, l.1165). Their regexes
  still read NUMBERS' text unchanged.
- Left: `NUMBERS.md` l.1000 ("the top-up's part for no interest") and l.1014 ("If interest earns nothing"), for
  NUMBERS' owner.

**M11. What comes back.** Fixed. It now has one wording everywhere: worth about $45,500 in 1 January 2033 money if rates
hold, all of it Laura's by the last payment in 2042; if cash waiting earns nothing, none.
- `SKELETON.md`: l.43 (3a supporting 1), l.203 (conceit 3a), l.247 (2.0 reservoir) and l.261 (3a reservoir).
- `WORDS.md`: l.27 and l.70.
- `CONCEIT.md`: l.64, l.298, l.342 and l.472.
- `AHA_REGISTER.md`: row 5, where the $34,369 January 2027 form is struck, and the aviation reserve.
- `INTENT.md`: l.64 and l.87.

**M12. "Policy".** Checked; already done. A grep of every plan file finds "policy" on Laura's or the team's side in two
places only, both left as records:
- `DENSITY_CUT` l.276, "the separation is her policy, not a law", is inside Appendix A's verbatim copy of the old 3e row,
  a record and not a live row.
- `SKELETON.md` l.292 quotes a panel judge of Wed 11 Nov ("I wouldn't approve a policy whose only two exits are
  undefined"), a record of a reading.

**M13. Assumptions without source or date.** Fixed, through the builder.
- Table 3's note now names "building-cost trend: DGBAS construction cost index, to October 2026 (8d)" (`build_exhibits.py`
  l.392; `exhibit_data.py` l.472). It is checked against NUMBERS 8d (l.1339).
- Table 2's note now gives the simulated futures' basis: shares 7.5% with 17.88% volatility (J.P. Morgan), and yields
  moving about 0.9 points a year, independent of shares, our own assumption. Both are checked against NUMBERS 0
  (l.1133-1137). 3b's 93 of 100 points there (`SKELETON.md` l.44).

**M14. Liquidity.** Fixed. `SKELETON.md` l.43 adds one clause to 3a. It names liquidity (TNA l.15) and points to Figure
1's cash dates, with no new figure: each payment's cash arrives before its date, so no holding has to be sold to meet a
payment. The 3a reservoir's "run-down without selling" supports it.

**M15. "Any further gift".** Fixed. `SKELETON.md` l.262 (3b reservoir): the clause is struck. Anything above the top joins
her flexibility, and the plan says nothing more.

## LOW

1. **WHY_A_RANGE 4d.** Fixed. `WHY_A_RANGE_2026-11-16.md` l.361 now says "held since" in 3c's own words. The same fix is
   made at l.52-58, l.219-221, l.171 and l.174, and in the short form at l.366.
2. **"Cushion".** Fixed:
   - `AHA_REGISTER.md` row 9 (twice) and row 1;
   - `INTENT.md` l.33;
   - `SKELETON.md` l.263 and l.232.
3. **Orange County.** Fixed. Struck from the "Nobody can run" reserve (`AHA_REGISTER.md` l.48), with a dated note.
4. **"Rub out".** Fixed. "Can shrink in the same downturn" in `CONCEIT.md` l.61 and l.345, and in `SKELETON.md` l.200.
5. **"Rarely".** Fixed. "Far less often before" in `SKELETON.md` l.43 and l.228, `AHA_REGISTER.md` row 5 and `INTENT.md`
   l.60.
6. **3.0's notes.** Fixed. In `SKELETON.md` l.42 the confidence is now "in one word, certain". In l.260 "The proposition no
   other founder can make" is struck.
7. **INTENT's five stale lines.** All fixed in `INTENT.md`:
   - l.11: "before the 2031 meetings";
   - l.29-30: the top-up and the extra Treasuries named;
   - l.67: the reserve is defined at first use, never "from 2033 the Treasuries are the operating reserve";
   - l.87: $15,000 given its basis, Mon 9 Nov's design (NUMBERS l.220);
   - l.122: about 2,550 words, SKELETON's page arithmetic.
8. **Three NUMBERS labels.** Left, by the lead's instruction not to edit NUMBERS: l.1000, l.1014, and l.2177's
   "$81,891" against l.287's $81,889. They go to NUMBERS' owner.
9. **"The 2031 move" alone.** Fixed. `AHA_REGISTER.md` rows 1 and 4 now say "the move before the 2031 meetings". The same
   change is made in `SKELETON.md` l.248 and `CONCEIT.md` l.68.
10. **Aha row's loose phrases.** Fixed. `AHA_REGISTER.md` l.32: "what she gives", and "certain" on the range she states
    once both ends are owned.
11. **"A click is ink".** Fixed. It moved to 2.5, which 3f already names for buying it:
    - a new 2.5 row in `SKELETON.md` l.201 and `CONCEIT.md` l.62 ("Inking is not tracing" moves with it);
    - struck from both 3f rows;
    - `WORDS.md` l.54 and `CONCEIT.md` l.192 updated.

## Lay reader 3

- **3a, "even if cash waiting earns nothing".** Fixed. `SKELETON.md` l.43 now says it in 3a's own words at first use.
  Each Treasury's interest and final money arrive before the 1 January it is for, and that money waits in the
  short-term Treasury ETF. The test assumes it earns nothing while it waits; every bond's interest and fund payout still
  counts.
- **3a, the $45,500.** Fixed. `SKELETON.md` l.43 and `WORDS.md` l.27 say it as what comes back to her, never as a profit
  beside the price.
- **3c, "$120 for each further 0.1%".** Fixed. Moved to Table 2's note as an if-then item (`build_exhibits.py` l.351-356;
  checked against NUMBERS 3's $119). 3c keeps two figures in prose and says the condition in words (`SKELETON.md` l.45,
  l.263; `DENSITY_CUT` C6).
- **3c, "resting on the floor alone".** Fixed. It now reads "counted from the Treasury fund bought that month alone" in
  `SKELETON.md` l.45 and l.263, `WORDS.md` l.33 and `WHY_A_RANGE` l.54 and l.220.
- **3e, "less than one rounding step".** Fixed. "Less than one $5,000 step" in `SKELETON.md` l.47.
- **3e, 17.88%.** Fixed. Moved to Table 2's note beside the 7.5% (`SKELETON.md` l.47, l.265; `DENSITY_CUT` E2). This
  overrides coherence reader 6's L9 by the lead's call.
- **Table 3, "X-date".** Fixed. Row 3 is now "Debt-limit deadline" (`exhibit_data.py` l.574). The note defines the
  deadline once, naming the X-date.
- **Table 3, "(the range's from its 0.5%)".** Fixed. Row 4 now reads "any gap met from the extra Treasuries, or for the
  range its 0.5% margin".
- **Table 3, "Never: VT".** Fixed. Row 4 now reads "Never: a sale of shares." (`exhibit_data.py` l.1334).
- **Table 3, 9.1% beside 10%.** Fixed. Row 7 prints only "10% stronger than in 2031: $11,500 more on $115,000" (l.636).
  The 9.1% reading and 32.768 move to the item list for 3e (l.674), and a check confirms neither is printed.

## For the lead

1. **Figure 1's label.** "Paid 2033-2042, added up" is adapted from the reader's wording (M2 above). The lead may
   prefer the reader's own.
2. **Where the reserve's size sits.** It is printed in Figure 1's note, the lead's other option. Moving it into 3a's
   prose would take one of 3a's three figures.
3. **The cost of moving $120, 17.88% and 0.9 into notes.**
   - Prose freed: about 36 words in 3c and 3e.
   - Notes added: about 3 lines (Table 2 +2.0, Figure 1 +1.0), roughly 44 words of Section 3's ceiling.
   - Net: about 8 words less headroom.
   - Note budgets: Table 2 is now 137 words (was 95), Figure 1 84 (was 77) and Table 3 44 (was 40).
4. **Table 3 row 6.** It now reads "the top to Jan 2031", cut to fit the page. The lead did not ask for this change.
   Table 3's note is held at 44 words: 46 would spill onto a second page.
5. **For NUMBERS' owner:**
   - l.1000 and l.1014 (M10);
   - l.2170's "reconcile" (M2);
   - l.2177's $81,891 (LOW 8).
