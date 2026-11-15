# Store digest D1: the payments' tags (Sun 15 Nov 2026, morning, Sydney)

Tags covered: CERTAINTY, LADDER, REINVEST, COMPLETE2028, RESERVE2033 and FLOOR.

Rating changes are in `ratings_D1.csv`, alongside this file. It holds only the rows this pass changed, and every row repeats all four ratings. A blank cell would reset a rating to its first-pass value. Append the file to `../ratings.csv` to apply it; the last row for each id wins.

Nothing else was edited.

## Method

1. Read every A and B row carrying the six tags and skimmed the C rows. Before this pass there were 1,673 such rows: 645 A, 712 B, 164 C, 140 merged and 12 refused.
2. Checked each row against NUMBERS (6 Nov curve), CANON, WORDS, SKELETON, CONCEIT and the frozen IPS.
3. Applied the brief's rules:
   - **Void figure or superseded design:** status adapt, with a note that says it in today's figures.
   - **Shown false, or banned outright:** refuse.
   - **Same idea twice:** merged into the strongest id, never into a row that is itself merged or refused.
4. Rebuilt the store in a scratch copy to check the effect. The six tags then hold 630 A, 623 B, 143 C, 265 merged and 15 refused. The repo store was not rebuilt.

## Counts

| | Rows |
|---|---|
| Rows in `ratings_D1.csv` | 245 |
| Merged | 125 |
| Adapted | 88 (24 newly, from keep; 64 already adapt, re-noted because their notes quoted void 9 Nov figures) |
| Refused | 3 |
| Re-rated (F, R, S or C changed) | 41: 19 raised, 22 lowered |
| Kept, with a new note only | 7 |

## What changed, by kind

### 1. Void 9 Nov figures in notes (about 70 rows)

The 9 Nov pass labelled these rows "VOID figure (NUMBERS.md 9 Nov)". Its replacement figures are now void too. Each note now quotes today's register:

| Void figure | Today's figure | Source |
|---|---|---|
| Keel's margin of $21,149 | the extra Treasuries, $35,894 | NUMBERS 2 |
| A $7,500 buffer | none; the test is "paid even if cash waiting earns nothing" | NUMBERS 2 |
| Bottom $110,000, floor payout $115,929 | stated bottom $95,000, floor payout $103,178 | NUMBERS 4 |
| VT $33,515 | VT $29,829 against the floor's interest of $21,289 | NUMBERS 4 |
| All-Treasury $158,157 | $140,761, stated $130,000 | NUMBERS 4 |
| Reserve $427,028, or 1.07x | $444,545 against $399,089 | NUMBERS 8h |

The rule "VT is about the floor's expected interest" (H1-083 and its duplicates) no longer holds exactly: VT is now the remainder, and slightly larger than that interest.

### 2. Banned names and superseded designs

- **Principal- or capital-protected** (H1-014, H2-068, H2-069): the names are dropped. Each note keeps only "no bank between Laura and the floor".
- **"Escrowed to maturity" and "sufficient without reinvestment"** (H1-015, H9-036, Q20-020): the report names MSRB's "full cash" or "gross" refunding once.
- **"Two-thirds scale" or "in miniature"** (Q17-024): the report says "scaled to the model portfolio".
- **"Backstop"** (Q20-006, Q25-025, Q28-005): the report says "the extra Treasuries".
- **Orange County** (H2-059, H8-115, Q3b-007): never named in the report. The lesson can be told without the name.
- **Superseded designs:** a quarter held back, the range sliding, CLO hold-backs, and her flexibility paying a payment gap. These rows are lowered to store only.

### 3. Store rows that contradict SKELETON, now flagged

- **Q26-023:** took the date the debt limit binds for the X-date. Use Q15-026 instead.
- **Q16-006:** says three funds have ended. The count is five (Q3a-030).
- **Q20-030:** gem2 marked it OUT. Only the $2,388 is IPS l.13's completion; the extra Treasuries size the reserve.
- **Q8b-026:** moving payment money into bills before an X-date was withdrawn, because it is a third trigger that CANON A34 forbids.
- **Q2a-030:** its note used the banned "the ten as bought would have fallen short".
- **Q37-013:** its note used "top stays $115,000" as a headline. Both notes are reworded.

### 4. Refused

- **H1-030 and H4-189:** the XR medicine motif, which Ray banned on 5 Nov.
- **H4-131:** CPPI described as Laura's plan.

### 5. Raised

| Row | Change | Why |
|---|---|---|
| NUM-001 | F5, C4 | the 5.12% hurdle |
| NUM-002, NUM-007 | C4 | |
| Q39-004, Q39-016, Q39-017, Q39-019 | F5, C4 | the reply to Siegel that SKELETON places in 3a |
| Q39-023 | F5, C4 | Perold and Sharpe's naming for 3b |
| H1-004 | F5, S3, C4 | each promise owned on the day it becomes one: the conceit's inking dates |
| H2-017 | F5, C4 | one issuer on purpose |
| H2-024 | C5 | |
| H4-057 | F4, S3, C4 | the pooled extra Treasuries cost $2,065 less at 0% than padding each rung |
| H2-094, Q3a-030, H2-040, H1-026, Q20-027 | F4 | |
| H7-001, H7-011 | C4 | |

### 6. Merged (125)

- **34 bare names from the H4 and H2 index lists** were folded into their fuller rows. The other 91 are same-idea duplicates.
- **Clusters, each merged into one id:**

| Idea | Merged into |
|---|---|
| Escrow verification | Q20-020 |
| Regulation 126 | Q20-027 |
| The floor bought in 2031 instead | Q7-030 |
| Orange County | H8-115 |
| Nominal promise, nominal match | H7-088 |
| The WInS book at scale | Q17-024 |
| A principal-protected note | Q3a-014 |
| Contingent immunisation | Q7-028 |
| "Risk only the interest" | H1-083 |
| Funds pay NAV | H3-007 |
| Debt service reserve account | H4-037 |
| Annuities | H4-021 |

## Per tag: the three strongest ideas, the biggest hole and the next research step

GEM_LEDGER placement in the tables:

- **SKEL:** the id is cited in SKELETON.
- **GL2a:** "should land (now in SKELETON)".
- **gem2:** the second gem review's verdict.
- **Not placed:** the ledger does not carry the id.

### CERTAINTY (SKELETON 3a, 3e)

| Id | One line | Part | GEM_LEDGER |
|---|---|---|---|
| Q8a-030 (24) | Several layers of defence are no reason to run without one of them. The two reasons in IPS l.17 are the only events that remove a layer. | 3e, one clause | SKEL; not placed by id |
| H1-004 (22, raised from 18) | Each promise is owned on the day it becomes one: the payments in Jan 2027 (completed Jan 2028), the bottom in Jan 2028, the top at the 2031 move. | Spine of 3a to 3c; CONCEIT row 2 | Not placed (carried in CONCEIT, not by id) |
| Q39-019, Q39-016, Q39-017, Q39-004 (24/22/20/20) | The reply to "six to fifteen years is long enough for shares" (Siegel). Across 39 markets a 30-year investor lost to inflation about 12% of the time. A longer horizon makes a loss rarer, not smaller (Samuelson). Insuring shares costs more the longer the horizon (Bodie). | 3a, SKELETON's "raised and answered" list | Not placed (card Q39 came after the ledger) |

**Hole.** 3a will say Laura's test is "the same arithmetic, not the same legal standing" as a full cash refunding escrow. Yet 61.28% of the book sits in iBond ETFs that pay their NAV. No store row says whether escrow practice accepts fund shares at all; for example, rating agencies' lists of permitted escrow investments.

**Next run.** Read one rating agency's or one verification agent's list of permitted defeasance-escrow investments. Record whether Treasury funds or money-market funds qualify, so 3a's "not the same legal standing" has its reason.

### LADDER (SKELETON 2.1 to 2.3, Table 1; 3a)

| Id | One line | Part | GEM_LEDGER |
|---|---|---|---|
| Q17-040 (23), with H2-017 (21, raised) | 89.55% of the book at cost is in US Treasuries by design: one issuer on purpose, with the spreading done in VT. | 2.3 lead | SKEL; not placed by id |
| Q16-018 (23) | A state lottery's written rule for fixed yearly prizes is each bond "maturing just before it's needed". | 2.0 and 3a precedent | SKEL; GL2a should land (now in SKELETON) |
| Q17-024 (24, re-noted; H2-095 merged in) | The WInS book is the whole plan scaled to the model portfolio (300/450), not the January 2027 purchase. | 2.1, first job | Not placed by id; name in WORDS |

**Hole.** CANON B24 marks TNA l.15's "a level of liquidity which no odd-lot bond offers" UNVERIFIED. 2.2's case for iBond ETFs over individual bonds for 2033 to 2037 leans on it, and the report must stay coherent with the TNA. No store row sources odd-lot Treasury pricing; H9-076 names odd lots without evidence.

**Next run.** Find one primary study of trade cost by size for Treasury or other bonds (FINRA TRACE or a Fed or SEC staff paper). Set it against an ETF's quoted spread and file it as B24's evidence.

### REINVEST (SKELETON 3a)

| Id | One line | Part | GEM_LEDGER |
|---|---|---|---|
| NUM-001 (24, raised from 21) | The ten as written pay only if the interest each bond pays earns 5.12% a year until needed. That hurdle is why the extra Treasuries exist. | 3a, must land | SKEL; gem2 should land high |
| Q16-020 (22) | The same lottery buys extra bonds on purpose against reinvestment risk: a public precedent for the extra Treasuries. | 3a | SKEL; GL2a should land (now in SKELETON) |
| H7-011 (20, C raised) | Zero is a rate that waiting cash has really earned: Fed target 0-0.25% from Dec 2008 to Dec 2015, and again from Mar 2020 to 16 Mar 2022 (card Q2d, Sun 15 Nov). The zero-interest test is history, not an invented stress. | 3a | SKEL; gem2 should land high, REF |

Runner-up: Q2a-030. The ten as written would have needed the 2028 deposit's help in about half the starting months (55.6% of 585).

**Hole.** H7-011's dates are not yet in NUMBERS. No row counts how often a short-Treasury fund's yield, after its fee, sat at or below zero. NUMBERS 2's "with the ETF fee" column is a model, not history.

**Next run.** Pull FRED's 3-month bill rate (DTB3) and the Fed target range. Count the months since 2008 when the bill yield was below a 0.15% fee, and file the result beside NUMBERS 8a so 3a can cite it.

### COMPLETE2028 (SKELETON 3a, 3e, Table 3 row 1)

| Id | One line | Part | GEM_LEDGER |
|---|---|---|---|
| Q3b-034 (23) | The two reasons are the only two flows the plan does not own: money coming in (the 2028 deposit) and the Treasury's own payments. | 3e, "why only these two" | SKEL; not placed by id |
| Q12-001, Q12-004, Q12-008 (22 each) | An advance arrives in instalments over years, royalties come twice a year three months late, and publishers stretched payments in 2020. This is what the deposit rests on. | 3e, assumption area (2) | SKEL; GL2a should land (now in SKELETON) |
| Q37-016 (24), with Q20-030 re-noted | The assumption is the case's "in full at the start of 2028", and 31 March 2028 is reason 1's trigger, never the assumption. Only the $2,388 top-up is IPS l.13's completion; the extra Treasuries ($35,894) size the reserve. | 3e; 3a | Not placed; Q20-030 gem2 OUT (consistent with the re-note) |

**Hole.** Table 3 row 1's early warning (Laura confirms the deposit in writing by 1 December 2027) is Keel's own date. No store row shows how practitioners give notice before a scheduled contribution, so the date has no outside reason.

**Next run.** Find two practitioner rules for notice before a scheduled contribution: private-fund capital-call notice periods, and a pledge-payment reminder schedule. Set row 1's warning date by them.

### RESERVE2033 (SKELETON 3a reserve, Figure 1, 3e)

| Id | One line | Part | GEM_LEDGER |
|---|---|---|---|
| Q16-022 (21) | The lottery's yearly portfolio report, and "a report affirming the sufficiency of the portfolio cash flow" before any change. This is what Laura's managers report each January from 2033 to 2041. | 3a and 3e | gem2 should land medium (Table 3 note or 3e prose) |
| Q9-009 (22), with Q9-016 (23) | The field puts operating reserves before buildings, the plan's own order. Founder-led museums that closed lasted a median of ten years, which Laura's ten prepaid years cover. | 3a; 3b | SKEL; GL2a should land (now in SKELETON) |
| Q16-039 (21), with Q25-025 (22), both re-noted | Size: $444,545 on 1 Jan 2033 against the $399,089 the payments are worth (NUMBERS 8h). What comes back from the extra Treasuries is $45,456 (60%), against her flexibility with what is above the top, $29,823 (40%) (8k). | 3a; Figure 1's note | Q16-039 gem2 carried; Q25-025 not placed |

**Hole.** How the reserve is actually held and released from 2033 to 2042 rests only on the lottery precedent and the custody rows (Q2b-008, Q2b-029): who holds it, who releases each January's $50,000, and who signs the yearly sufficiency report. No row shows the paperwork a real founder uses with an arts nonprofit.

**Next run.** Read one public multi-year operating-support or pledge-payment agreement between a founder and an arts nonprofit, or a donor-advised fund's multi-year grant schedule. File the three clauses 3a needs: who holds, who releases, who reports.

### FLOOR (SKELETON 3b, 3c)

| Id | One line | Part | GEM_LEDGER |
|---|---|---|---|
| Q5c-011 (24) | A minimum with full freedom above it is the best simple rule when you want commitment but expect news: the IPS's shape in one theorem. | 3b | SKEL; GL2a should land (now in SKELETON) |
| Q7-030 (21, re-noted; H2-061, H9-052, NUM-005 and NUM-006 merged in) | NUMBERS 8c. Buying the floor in 2028 costs about $7,400 at the middle. Bought in 2031 instead, Laura is under $95,000 in 15.8% of simulated futures (about 1 in 6) and in 9.1% of history windows. | 3b | SKEL; GL2a should land (now in SKELETON) |
| Q39-023 (22, raised), with Q3a-034 | The naming: buy-and-hold in Perold and Sharpe's terms. The floor is bought once in Treasuries and the shares are only the remainder; never CPPI or portfolio insurance. | 3b naming clause | Not placed by id; SKELETON names Perold and Sharpe |

**Hole.** The bottom rests on IBTM's final payout. The only evidence from ended funds is IBTF's return (Q16-008) and the five funds' dates (Q3a-030). No row sets a terminated iBond Treasury fund's final distribution against its NAV and SEC yield a year before the end. Whether another WInS-listed fund ends in late 2032 is UNVERIFIED (CANON B11).

**Next run.** For each of the five ended iBond Treasury funds, record from iShares' filings:
- the NAV a year before the end;
- the SEC yield then;
- the final distribution.

File the gaps beside NUMBERS 3's 4.1% zero-interest deduction.

## The three biggest holes

1. **FLOOR.** No evidence on what an ended iBond Treasury fund actually paid against its NAV and yield beforehand. The stated bottom ($95,000) rests on IBTM's payout.
2. **REINVEST.** The report's standard is "paid even if cash waiting earns nothing", but the history that waiting cash did earn about nothing after fees is not filed in NUMBERS. H7-011's dates still need FRED.
3. **LADDER.** TNA l.15's odd-lot liquidity claim (CANON B24) is unsourced. The report's case for iBond ETFs must stay coherent with it.
