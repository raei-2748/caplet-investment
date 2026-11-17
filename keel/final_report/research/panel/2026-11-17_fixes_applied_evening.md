# Fixes applied: coherence reader 8 and the evening lay reader (Tue 17 Nov 2026, late evening, Sydney)

Inputs:
- `2026-11-17_coherence_reader_8.md` (H1, M1-M10, LOW 1-14);
- `2026-11-17_lay_reader_3e_evening.md` (three stumbles, two points noticed in passing);
- the lead's calls of Tue 17 Nov evening.

These are planning notes only: no Final Report prose.

Not edited: the frozen record (IPS, TNA, WInS notes, the case), CANON's submitted-quote columns, the cards, the store and
CLAUDE.md. CANON's check columns gained dated notes only (L14). Line numbers are as the files stand after this run.

Every guard written here was checked against EXPECTATIONS standing order 24. None limits strong words about Treasuries.

**Count.** 29 items in all:
- coherence reader 8's 25 (H1, M1-M10, L1-L14);
- four more of the lead's calls: the lay reader's stumbles 1-3 and Table 3's "today's rates". The stale margin dates
  are counted as L3.

Fixed: 28. Left with a reason: 1, M9 (CLAUDE.md is the lead's). Dated records that quote the old wording are listed under
"For the lead" and were left as they stand.

**Exhibit build** (`python3 keel/final_report/exhibits/build_exhibits.py`, last run after every change):
- Check against NUMBERS.md: 440 figures, 439 PASS, 0 FAIL, 1 flagged. The flag is the known $1 rounding of Figure 1's
  footing. One check is new: Table 3's rows 1, 4 and 6 and its note.
- Words check: 240 exhibit texts x 8 patterns, 0 FAIL.
- Table 3: 21.9 lines with its 44-word note, on one page (18.9 without the note). It was 21.4 and 18.4.
- Table 2 is unchanged at 20.2.

## HIGH

**H1. 3f's aha gave "high" a meaning of the report's own (the lead's call).** Fixed.
- "A high degree of certainty" keeps IPS l.11 as its only definition (CANON A4). The aha is now the price of l.11's "one
  step further".
- Struck wherever they stood:
  - the clause "'high' is measured against what the same two deposits can buy";
  - the heading "Why 3.2% fails 'a high degree of certainty'".
- Where the change was made:
  - `SKELETON.md` l.233 (aha table, 3f), rewritten. The wording now there is under "For the lead", item 1.
  - `AHA_REGISTER.md` row 10 (l.30):
    - version B is reframed in place, with a note that the new wording has not yet been read cold;
    - the old heading is now "What 3.2% meant beside IPS l.11's step further";
    - the job column says the 3.2% is "the check that priced IPS l.11's step".
  - `NUMBERS.md` l.1956 (8s): the readers' question (a) now reads "what 3.2% meant beside the step further IPS l.11 took",
    with the lead's call and "never 'why 3.2% fails high'".
  - `voice/FACTS_PLAIN.md` l.44: the same order, IPS l.9's reason first and the check second (see M6).
- Card Q120 (rows 1, 6 and 15) supports the 90% figures: judges average 90.28% and 90.1%, and 17 CFR 210.4-10 gives "at
  least a 90% probability".

## MEDIUM

**M1. Table 3 row 4's "any gap met from the extra Treasuries" (the lead's call).** Fixed.
- The cell (`exhibit_data.py` l.607) now reads: "*Changes: *the fund; a gap met from the 0.5% margin the payments and the
  range each carry. *Never: *a sale of shares." Row 4 drops from five lines to four.
- New 3e-list line (l.690; `tables.md` l.122):
  - with cash waiting earning nothing, the extra Treasuries leave $1,177 spare when the funds cost nothing beyond their
    fees, and nothing once those costs reach 0.5% (NUMBERS 2);
  - a gap beyond that is met only from interest the waiting cash earns, never from shares;
  - such a gap is not a reason to change the plan (IPS l.17's two reasons stand).
- The 3e list's one-action line (l.685) now names the margin.
- Checks:
  - updated: l.1380 and l.1414;
  - $1,177 is allowed in the 3e list as Figure 1's checked note figure (l.1350);
  - new: l.1355-1360.
- `build_exhibits.py` l.889: "ties the 0.5% to the range only" became "names the 0.5% margin in row 4".
- `SKELETON.md`:
  - l.303, the open question, is marked answered;
  - l.292, three "any gap / any cost" notes in the Table 3 spec, are bounded the same way.

**M2. "About 3%" should read "about 2%"** (2.32%, NUMBERS 3). Fixed in all nine places, each with the old figure dated:
- `AHA_REGISTER.md` l.21 and l.57;
- `INTENT.md` l.86;
- `CONCEIT.md` l.66, l.347 and l.391;
- `FACTS_PLAIN.md` l.138;
- `SKELETON.md` l.45 and l.263.

**M3. Figures from before the re-size.** Fixed against NUMBERS 8l, 4, 5 and 8o.

| Where | Was | Now |
|---|---|---|
| `SKELETON.md` l.263 | $402, 98.36%, 1.52%, 1 in 810, 3 paths, $182 | $447, 98.04%, 1.81%, 1 in 660, 6 paths, $123 |
| `SKELETON.md` l.45 | "as before" items | marked as re-sized, each old figure kept |
| `SKELETON.md` l.46 | 3 paths, $182 | 6 paths, $123 |
| `SKELETON.md` l.285 | $1,414 | $1,177 with the fee; $2,604 without it |
| `SKELETON.md` l.291 | $29,800 | $28,700 |
| `SKELETON.md` l.292 | $60,000; 74.5% | $55,000; 73.9% |
| `CONCEIT.md` l.346 and l.372 | $21,300; $9,900 | $21,200; $9,600 |
| `CONCEIT.md` l.357 | bottom from about $85,000 | from about $80,000 |
| `CONCEIT.md` l.514 | $9,900 to $41,300 | $9,600 to $40,900 (not listed by the reader; same re-size) |
| `WORDS.md` l.28 | $21,300; $29,800 | $21,200; $28,700 |
| `INTENT.md` l.95 | $21,300; $29,800 | $21,200; $28,700 |
| `INTENT.md` l.148 | 1 in 3,600 | 1.30 points; 70 of 200,000, about 1 in 2,900 |
| `INTENT.md` l.154 | $82,000 | about $81,000 ($81,244) |

**M4. 3a's "no holding has to be sold".** Fixed with the TNA's own fact.
- `SKELETON.md` l.43 now reads: the cash "waits in the short-term Treasury ETF (TNA l.5: 'the proceeds held in a
  short-term Treasury ETF'), which is sold to pay it, so no bond or fund is sold before its end to meet a payment".
- The same words replace "run-down without selling" at l.261.
- Table 3 row 1's new "Never" uses them too (see stumble 2).

**M5. "Laura's inked figures go only if the paper goes."** Fixed.
- `CONCEIT.md` l.269 now reads "A Treasury's payment goes only if the paper goes".
- The plain sentence beside it names the other limit: fund costs beyond the fee larger than the 0.5% margin (Q109-033;
  TNA l.13, "is not fixed").

**M6. FACTS_PLAIN: 40.8% beside "none", and the 3.2% without its reason.** Fixed.
- l.44 is now in 3f's order:
  - the team dropped the plan for how a writer is paid (IPS l.9);
  - a check that day priced it: about 1 in 31 against none from January 2028;
  - the 3.2% is never the reason and never a test of "high".
- l.51 is a new "Never set against 'none'" line, holding 13.7% and 40.8%, with the Treasury plan's own $57,455 short if
  no deposit comes (IPS l.17).

**M7. Turns struck tonight still on offer.** Fixed.
- `FACTS_PLAIN.md` l.146: the seal, knockout and overprint, pencils printed beside the inks, and the key plate are moved
  into one "struck, history only" line. Their plain facts stay.
- `WORDS.md` l.54: 3f now has no turn ("none for 3f, which stays plain").
- `AHA_REGISTER.md` row 10's conceit column now reads "None (plain)".
- `CONCEIT.md` l.69's purpose column: "registration" became "one date, not a crash". The struck turn's own text is left
  as history.

**M8. FACTS_PLAIN: the reserve without its basis, and "most comes back".** Fixed.
- l.41: "At today's rates ... about $445,700: printed once, in Figure 1's note item 4, never in prose and never as a
  percentage" (the 112% is gone).
- l.118: "worth about $46,600 in 2033 money if rates hold, all of it hers by 2042; if cash waiting earns nothing, none
  beyond the 0.5% margin for fund costs (never 'most comes back')".
- `CONCEIT.md` l.349 (section 3's 2033 row) gives the reserve the same basis.

**M9. CLAUDE.md still says the payments carry no margin.** Left: CLAUDE.md is the lead's, so it was not edited.
- l.4 still says "they carry no such margin until then".
- It still gives $35,894, $38,282, $444,545 and "14 of 15 houses".
- NUMBERS l.2366 lists the same items for the lead's commit.

**M10. Table 3 spec: "swaps that fund for a Treasury maturing before the payment".** Fixed. `SKELETON.md` l.292 now
reads "swaps that fund for an earlier iBond fund or the short-term Treasury ETF, as the built table says (never a Treasury
due before the payment, which WInS does not list for 2033 or 2035)", tested again with cash waiting earning nothing.

## LOW

1. **L1, "if cash waiting earns nothing, none".** Fixed. It now reads "none beyond the 0.5% margin for fund costs" in:
   - `SKELETON.md` l.43, l.203, l.247 and l.261;
   - `WORDS.md` l.27 and l.70;
   - `INTENT.md` l.91;
   - `CONCEIT.md` l.64, l.373, l.417 and l.547;
   - `AHA_REGISTER.md` l.25 and l.57;
   - `FACTS_PLAIN.md` l.118.
2. **L2, the 3a reservoir asks for the reserve's size in prose.** Fixed. `SKELETON.md` l.261 is marked "Store; Figure 1's
   note item 4 only, never in 3a's prose", with "at today's rates" added.
3. **L3, the "Wed 18 Nov re-size" dates (the lead's call).** Fixed. Each now says the payments carry the 0.5% since the
   Tue 17 Nov evening re-size:
   - `SKELETON.md` l.47 (3e), l.77 and l.179;
   - `CONCEIT.md` l.506;
   - `DENSITY_CUT_2026-11-17.md` l.139 and l.202;
   - `GEM_LEDGER.md` l.522 and `SKELETON.md` l.264 ($115,000 re-checked: unchanged, NUMBERS 4).
4. **L4, two roundings of $28,682 in 3b.** Fixed: `SKELETON.md` l.44 now gives $28,700 only, as Tables 2 and 3 print it.
5. **L5, WORDS's rounding rule.** Amended. `WORDS.md` l.57 now reads: "or to $100 where the figure is checked against a
   table or exhibit that prints it", with the figures named.
6. **L6, "at most about $120".** Fixed. Table 2's note now reads "by about $120 for each further 0.1% centrally"
   (`build_exhibits.py` l.361; `tables.md` l.88).
   - The same wording, with $144 at the house 1-in-20 high, is at `SKELETON.md` l.263, `INTENT.md` l.86 and
     `CONCEIT.md` l.347 and l.391.
   - The comment at `exhibit_data.py` l.482 is updated.
7. **L7, AHA row 10 contradicts itself.** Fixed (l.30). The price of "none" now points to "The figure, Tue 17 Nov
   evening", and 74.5% becomes 73.9% (the first $39,162 is 26.1% of the deposit).
8. **L8, NUMBERS calls the whole first slice the top-up.** Fixed. `NUMBERS.md` l.600 now reads "more than twice the first
   $39,162, the top-up and the extra Treasuries together".
9. **L9, "rarely before" and "about 55%".** Fixed.
   - `NUMBERS.md` l.191 and l.2088 now read "far less often before" (about 1 start in 6, 1962-80).
   - l.625 now reads "about 54%, 54.2% centrally".
10. **L10, pencil widened past its definition.** Fixed.
    - The archive note (`CONCEIT.md` l.261) now reads "every modelled figure", with pencil for figures only, never a
      model's odds.
    - The Mitchell note (l.219) now reads "a figure no Treasury she owns will pay yet is pencil, however large", never "no
      sale has turned into money".
    - Both are to be read cold with the definition first.
11. **L11, "never the payments".** Fixed. `SKELETON.md` l.250 now reads "the building money first and the payments last".
12. **L12, "law the case leaves out of scope".** Fixed. `SKELETON.md` l.264 now uses the case's words (l.168-169): a
    statute used as a parallel is not such a requirement.
13. **L13, "on its own evidence".** Fixed. `INTENT.md` l.102 now reads "for its own reason, then checked it (IPS l.9's
    reason first, the 27 Sep model only the check that priced it, CANON A3)".
14. **L14, $1,544's basis and FACTS_PLAIN's date.** Fixed.
    - CANON A19 (l.76, column 5) and B29 (l.140, last column) each gained a dated note: $1,544 is the curve basis, and
      $2,388 in January 2028 money is the top-up on the instruments held. Keel's columns only.
    - `FACTS_PLAIN.md` is re-dated to the Tue 17 Nov evening register (l.5), and its $301,500 names its basis (l.26).

## The evening lay reader (the lead's calls)

**Stumble 1, "one $5,000 step".** Fixed. Each place now says once what a step is: she states the range in $5,000 steps,
each end rounded down (NUMBERS's range rule).
- `SKELETON.md` l.47 (3e);
- `AHA_REGISTER.md` row 7 (l.27);
- `FACTS_PLAIN.md` l.60.

**Stumble 2, Table 3 row 1's "Never: a sale".** Fixed (`exhibit_data.py` l.568). The cell now reads: "*Changes: *no range
until paid; the ten short $3,016 at today's rates, $57,455 if cash waiting earns nothing, until the deposit fills them.
*Never: *a bond or fund sold early."
- Who fills the gap: the deposit, when paid, fills the ten first (card Q34; NUMBERS 5's order).
- What is never sold: no bond or fund the ten hold is sold before its end, in M4's words.
- Measured on the page against "a sale of what they hold", which also fits.

**Stumble 3, the $85,000 bottom.** Fixed.
- Row 6's trigger (l.632) now reads "None (for scale: 1 point lower by Jan 2027 sets an $85,000 bottom in Jan 2028)".
- A new 3e-list line (l.700; `tables.md` l.124) says:
  - the bottom is set when the floor is bought in January 2028 and stays put after it (IPS l.15);
  - before then the rate on the day decides it;
  - Mon 4 Jan 2027 is the first trade day, when the ten are bought.
- The same explanation is in `SKELETON.md` l.292 and `FACTS_PLAIN.md` l.60 and l.155. "Fixes the bottom" became "sets
  ... and it stays put".
- The first wording, "gives an $85,000 bottom, set Jan 2028", took a fifth line and put Table 3 on two pages, so it was
  not used.

**Table 3's "today's rates".** Fixed.
- Note item 1 (`build_exhibits.py` l.387, from `exhibit_data.py` l.662) now reads "$39,162: January 2028 money at today's
  rates (the Treasury curve of 6 Nov 2026), ...".
- `SKELETON.md` l.304 is marked done.

**Noticed in passing.**
- The two rows' disagreement about the margin is fixed by L3.
- The flexibility's size appearing only in Table 3 row 7 was not acted on (see "For the lead").

## For the lead

1. **The H1 wording now in `SKELETON.md` l.233** (also in AHA row 10's version B): "The price of IPS l.11's 'one step
   further' ...: the first plan's 96.8 in 100 would have passed the usual reading of 'high' (judges put 'beyond reasonable
   doubt' at about 90%, and the SEC writes 'a high degree of confidence' as at least 90%; card Q120 rows 1, 6, 15), so
   'high' did not rule it out; the team dropped it for IPS l.9's reason, how a writer is paid ..., and the 27 Sep model's
   check priced l.11's step: about 1 in 31 against none from January 2028. 'A high degree of certainty' keeps IPS l.11
   as its only definition (CANON A4)." This wording has not been read cold. It should go to the next cold aha test.
2. **Table 3's page fit.**
   - The table measures 21.9 lines: row 1 gained a line, and row 4 gave one back. This was the fit before 17 Nov.
   - The note still fits only at 44 words: 50 spills onto a second page.
   - The note items now run 76 words (69 before), because the date of today's rates adds six. The note written on 27 Nov
     must still fit 44 words, so one item will need shortening (for example, "the CBO's" for "the Congressional Budget
     Office's").
   - `tables.md` l.7 and l.9 keep the 21.4 measured that morning, as their dated history.
3. **Row 1's "Never" wording is mine, measured to fit.** It borrows M4's "no bond or fund sold before its end".
4. **Dated records left as they stand.** They quote the old wording or dates as what was said at the time:
   - `aha_test_2026-11-16b/`, `aha_test_2026-11-17/` and `aha_test_2026-11-17_evening/` (brief, readers, ITEMS,
     RESULTS);
   - `ARGUMENT_LOG.md` l.8: the morning's "argument now" says "'high' certainty is measured against what the same money
     can buy". The lead's next line should carry the reframing.
   - `pm/ASK_HUMANS.md` l.20 and `numbers/RUN_2026-11-17_evening.md`;
   - the voice-round dates in `voice/ROUND6.md`, `ROUND7.md` and `README.md`, which are the rounds' own dates, not the
     re-size.
5. **Lay reader points outside the lead's list, not acted on:**
   - (a) one sentence that the same two events (a missed deposit, a US default) can break both promises;
   - (e) 3a's "what comes back" carries three time stamps, and "2033 money" means nothing to a lay reader;
   - the flexibility's size appears only in Table 3 row 7.
   Each would change 3a's or 3e's density rows, so each is left for the lead's call.
