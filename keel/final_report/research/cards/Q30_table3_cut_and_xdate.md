# Q30 research cards: cutting Table 3 from 33 rows to eight, and settling the next debt-limit X-date

Wed 11 Nov 2026 Sydney (evening run). Report parts: 3e (assumptions, limits and what to watch; Table 3), with knock-ons
for 3a (the January 2028 completion) and 3d (what co-sponsors can show and when).
Notes for the Final Report store, not report prose.

Checked against: Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt` l.11, l.15, l.17, frozen), the
Trading Notes (`keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt`, notes 1-3), `CANON.md` (A31, A33, A34, C9,
D9, D12), `NUMBERS.md` (sections 0, 2, 3, 4, 5, 8d, 8h, 8j, 8k; every plan figure here is MODEL and quoted from there),
SKELETON version 2 (3a, 3e, exhibits item 4), Wharton's instructions (`WHARTON_NORTH_STAR.md` section 0: "what Laura or
her asset management team should monitor as 2031 and 2033 approach"), and the cards this one builds on: Q26 (rows
T1-T33, the expanded list), Q15 (rows 15, 20-26), Q4c (rows 28-31), Q11d (rows 16 and 22, card 2). Store rows Q26-023
and Q15-026 read in `research/store/insights.jsonl`. The plan is frozen: a "risk" in the Clash column is a risk to
record, never a change to propose.

**Claims tested**
1. Keep, kill or change: "Table 3 can be cut from 33 rows to about eight without dropping any signal that would change
   an instrument, a date, custody or the plan, using checklist design's rule of 'killer items'."
2. Keep, kill or change: "The next binding US debt-limit date (the X-date) falls before the 2031 co-sponsor meetings and
   again before December 2032."
3. Keep, kill or change: "A row for co-sponsors' January budget filings is worth one of the eight places."

**Problem class and the field that solved it.** Choosing the few items a busy reader must check from a long list of
things that could go wrong, where a missed critical item is costly and a long list gets skimmed. Human factors
engineering solved it for flight decks (NASA's checklist studies, Boeing's and the Air Transport Association's
checklist philosophy: only steps whose omission has "a direct and adverse impact on normal operation", most critical
first, an expanded checklist kept off the flight deck) and for operating theatres (WHO's Surgical Safety Checklist:
"Five to nine items in each Checklist section are ideal", every item "linked to a specific, unambiguous action", tested
before rollout). The X-date question is public finance forecasting: the statute (31 U.S.C. 3101 and its notes), the
Daily Treasury Statement, and the projections of CBO, the Bipartisan Policy Center and the National Taxpayers Union.

## Verdicts in one screen

- **Claim 1: KEEP, with changes.** The cut works: 33 rows become 8 (8 kept as the base of a row, 21 merged into one,
  2 moved out of the table, 2 dropped), and every Q26 row that changes an instrument, a date, custody or a reason sits
  inside one of the eight. But Degani and Wiener do not hand over a cut rule. They call the question of which items
  belong "a cardinal question in checklist philosophy" and warn that "a consensus can never be reached". The usable
  inclusion rule is Boeing's and the ATA's, quoted by them; the size comes from WHO (five to nine); the order from
  Degani and Wiener's guideline 10 (most critical first, and it "should take precedence"). Laura's killer item,
  restated: a signal whose miss alone could cost a payment, leave a planned step undone, or make a stated figure
  untrue. Rows 1, 2, 4 and 5 pass; row 3 is row 2's early warning (Degani and Wiener allow duplicating "a very few
  highly critical items" based on "possibly transient data"); rows 6-8 are not killer items and are kept for other,
  named reasons (the IPS rule, the half kept's three uses, custody). Row 8 is the weakest place.
- **Claim 2: CHANGE.** The binding date and the X-date are two different dates. The limit ($41,103,996m, raised by
  $5,000,000,000,000 by Pub. L. 119-21 s.72001, 4 Jul 2025) is projected to bind between February and mid-summer 2027
  (BPC "late winter and mid-summer of 2027"; CBO "sometime in 2027"; NTU May 2027). Extraordinary measures then last
  "roughly six to nine months" (BPC), so the next X-date falls about August 2027 to May 2028 (NTU central February
  2028). That is years before the 2031 meetings and right around the January 2028 completion. Another X-date before
  December 2032 is likely, not certain: binding dates since 2013 have come 9 to about 29 months apart, a fix lasting
  from 2028 past December 2032 would be the longest since 2011, and CBO's projected $49.4T of debt by end FY2031
  needs more than $8.3T above today's limit, against a record single increase of $5T. Whether one lands exactly
  between the 2031 meetings and December 2032 cannot be known now. **Store row Q26-023 is wrong** (its "X-date in
  mid-2027 falls between the two deposits" is the binding date, not the X-date); Q15-026 is right in substance and
  needs the November data. Replacement text in (c).
- **Claim 3: KILL as its own row; CHANGE into a source inside row 7 and a line of 3e prose.** Under the Foundations Act
  (Art. 25) a foundation's board passes the year's plan and budget within one month after the year begins, files it,
  and the record is public within a month of filing, so about February-March. The first filing that could show a
  co-sponsor's 2033 money is public about February-March 2033, after Laura's contribution is paid (cash about 18 Dec
  2032, SKELETON 3a). The filing changes no instrument, date, custody or reason; it only informs a call on the half
  kept (A31) and the 3d ask, and Laura hears from each co-sponsor before any filing is public.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Checklist designers split on what goes in: every configuration item (the systems engineering view) or only the critical ones (the human performance view); "a cardinal question in checklist philosophy" | Degani & Wiener (1990), s.3.1.5 | PRESENTATION, TWOREASONS | KNOWN | Q26's 33 rows are the all-items list; Table 3 must be the critical-only list, and say so | Flight checklists run many times a day; Laura's table is read a few times a year, so the cost of length is attention, not minutes | VERIFIED (NASA CR-177549 read in full at NTRS) | no | NTRS PDF |
| 2 | Killer items defined: "critical items are those whose omission can alone lead to an accident. Pilots call them 'killer items.'" | Degani & Wiener (1993), p.350 of the journal (author copy) | PRESENTATION, TWOREASONS, CERTAINTY | KNOWN | Laura's version: a signal whose miss alone could cost a payment, leave a planned step undone, or make a stated figure untrue | In a cockpit the item is an action; in Table 3 it is a signal to read, and the miss is not reading it in time | VERIFIED (author's copy of Human Factors 35(2) read in full; SAGE article page shows no retraction or correction notice) | no | Author PDF; SAGE page |
| 3 | Long lists get shortcut: crews running checklists 3-10 times a day do "only what he/she perceives as the critical items"; one DC-9-50 checklist had 81 items and the company saw poor discipline | Degani & Wiener (1990), s.3.1.6 | PRESENTATION | KNOWN | If Table 3 has 33 rows, the reader picks their own eight; better that Caplet picks them and writes down how | One company's case, no measured error rate | VERIFIED (s.3.1.6 read) | no | NTRS PDF |
| 4 | The inclusion rule: "Only procedural steps which, if omitted, would have a direct and adverse impact on normal operation are included. Items annunciated by the Crew Alerting System (EICAS) are not included." (Boeing B-757; ATA 1986 says the same) | Degani & Wiener (1990), s.3.1.7-3.1.8, quoting Boeing and ATA (1986, p.46) | PRESENTATION, TWOREASONS | KNOWN | What the broker statement or a fund notice already "annunciates" (a coupon credited, T14) needs no row of its own; it folds into the row whose action it triggers | Degani and Wiener: "a consensus can never be reached as to which list of items are important enough" | VERIFIED (both quotations read in s.3.1.7-3.1.8) | no | NTRS PDF |
| 5 | A minimal list's success "is difficult to measure in everyday line operation, and is even harder to defend after an occurrence of a checklist-related accident" | Degani & Wiener (1990), s.3.1.8 | PRESENTATION, PROCESS | NICHE | Write the inclusion rule under Table 3 and keep the 33-row list in the store with a fate for every row, so any dropped signal has a recorded reason | A report table has no accident investigation; the defence needed is a judge asking "what about X?" | VERIFIED | no | NTRS PDF |
| 6 | The expanded checklist "follows the same steps ... but in more detail", is for training, and "is not meant to be referred to in flight" | Degani & Wiener (1990), s.2.1.2 | PRESENTATION | KNOWN | Q26 is the asset management team's expanded list (kept in the store); Table 3 is the normal list Laura reads | The report has a page limit (9-12 pages without References), so the expanded list cannot ride along as an appendix | VERIFIED | no | NTRS PDF |
| 7 | Most critical items first; guideline 10 "should take precedence" when it conflicts with others | Degani & Wiener (1990), s.7.2.4 and Appendix A (10); Degani & Wiener (1993), guideline 6 | PRESENTATION, TWOREASONS | KNOWN | The two reasons are rows 1 and 2, before every watch row | In the cockpit the reason is interruption; for Laura it is a reader who stops after the first rows | VERIFIED | no | NTRS PDF; author PDF |
| 8 | Chunk long lists and separate the chunks; "having one task-checklist with 76 items may be somewhat absurd"; "as the list of items grows, there may be a higher probability of overlooking any given item" (Swain and Guttman, as quoted) | Degani & Wiener (1990), s.7.1.1 and Appendix A (7); Degani & Wiener (1993), guideline 3 | PRESENTATION | TEXTBOOK | Three tiers (Reason, Look closer, Watch) are the chunks; eight rows sit inside them | The memory research behind it is about short-term memory, a weak basis for a printed table; used only as a ceiling | VERIFIED (the paper's use; Miller 1956 and Swain and Guttman 1983 not read) | no | NTRS PDF |
| 9 | "There should be no compromise, however, regarding the critical 'killer' items" | Degani & Wiener (1990), Appendix A (15) | TWOREASONS, CERTAINTY | KNOWN | Cutting is allowed everywhere except the two reasons and the payment-day signals | Written for FAA inspectors approving airline checklists, not for a client table | VERIFIED | no | NTRS PDF |
| 10 | Duplicate "a very few highly critical items ('killer items') that are based on possibly transient data" | Degani & Wiener (1990), s.7.2.5; Degani & Wiener (1993) | TWOREASONS, LADDER | NICHE | Row 3 (debt limit and X-date) repeats row 2 ahead of time, because the X-date moves with tax receipts like a flap setting moves with weight and runway | Their example is a value recalculated minutes later; the X-date moves over months | VERIFIED | no | NTRS PDF |
| 11 | "We have now advocated conflicting principles: brevity of checklists and repetition of critical items ... no absolute list of principles can be religiously adhered to by the designer" | Degani & Wiener (1993) | PRESENTATION, PROCESS | KNOWN | The cut is a judgement; the card records it as one, with the rule and the fates | None | VERIFIED | no | Author PDF |
| 12 | WHO's three principles: simplicity ("An exhaustive list ... would be difficult to implement and convey, and would probably face significant resistance"), wide applicability, measurability; checklists should "address the major safety issues that, if omitted, put a patient at risk for harm"; "Checklist fatigue" from many checklists | World Health Organization (2009a), Section I and Appendix | PRESENTATION | KNOWN | Measurability: every kept row has a public source or a named record and a level (Q26 gave a source, date and threshold for 27 of 33) | Surgery is repeated daily by teams; Laura's watch spans nine years | VERIFIED (Guidelines Sections I, III, IV read) | no | WHO IRIS PDF |
| 13 | "Focused: ... concise, addressing those issues that are most critical and not adequately checked by other safety mechanisms. Five to nine items in each Checklist section are ideal." | World Health Organization (2009b), "Modifying the Checklist" | PRESENTATION | KNOWN | Eight rows. "Not adequately checked by other mechanisms" drops what cannot happen or needs no act (T12 a call: none of the five T-bonds is callable; T13 buybacks are voluntary) | WHO's figure is per section of a spoken checklist, not per printed table | VERIFIED (Implementation Manual read in full) | no | WHO IRIS PDF |
| 14 | "Actionable: Every item on the Checklist must be linked to a specific, unambiguous action. Items without a directly associated action will result in confusion" | World Health Organization (2009b) | PRESENTATION, TWOREASONS | KNOWN | Each row says what it changes and what it never changes; row 6's action is "carry on", which is the IPS rule itself | Row 6 is an anti-action row; WHO has no such item. Kept because the IPS sentence must be visible | VERIFIED | no | WHO IRIS PDF |
| 15 | "Brief: ... no more than a minute for each section" | World Health Organization (2009b) | PRESENTATION | KNOWN | A reader should get through Table 3 in about a minute: one line per cell, no paragraphs inside cells | None | VERIFIED | no | WHO IRIS PDF |
| 16 | "Tested": run it round a table, then one team for a day, modify, repeat, before rollout | World Health Organization (2009b) | PRESENTATION, PROCESS | KNOWN | The scorecard's "read right by a stranger": give the eight rows to someone outside the team and ask what Laura does if each trigger fires | A one-off read is not a field test | VERIFIED | no | WHO IRIS PDF |
| 17 | "not intended to be comprehensive"; "removing safety steps because they cannot be accomplished ... is strongly discouraged"; "cautioned against making the Checklist unmanageably complex" | World Health Organization (2009a), Section III footer; (2009b) | PRESENTATION, COSPONSOR | KNOWN | Short, but no killer signal goes because it is hard to read: co-sponsor commitments have no public source and still stay, inside row 7 | None | VERIFIED | no | WHO IRIS PDF |
| 18 | Did it work: a 19-item checklist at 8 hospitals cut deaths from 1.5% to 0.8% and complications from 11.0% to 7.0% | Haynes et al. (2009), as reprinted in World Health Organization (2009a) | PROCESS | TEXTBOOK | Evidence that a short list that gets used beats a long list that does not | Before-and-after design with no control group; a surgical result, not a monitoring one | VERIFIED (abstract, methods and intervention as reprinted, with its DOI) | no | WHO IRIS PDF |
| 19 | The cut: Q26's 33 rows go to eight: 8 kept as a row's base, 21 merged, 2 moved out, 2 dropped; every signal that changes an instrument, a date, custody or a reason sits inside a kept row | This card, "Table 3 cut"; Q26 rows T1-T33 | PRESENTATION, TWOREASONS | NICHE | Table 3 in the report; Q26 stays as the expanded list | The rule is Caplet's adaptation, not an aviation or WHO rule | VERIFIED (Q26 read in full) | no | Q26 card |
| 20 | The killer test applied: rows 1, 2, 4, 5 are killer items; row 3 is row 2's early warning; rows 6-8 are kept for named reasons (the IPS rule, A31's three uses, custody) | This card; Degani & Wiener (1990, 1993) | TWOREASONS, HALFKEPT | NICHE | Lets the report say which rows can change something and which are there to show nothing changes | Rows 4 and 5 hold "look closer" levels; they must read as checks on implementation, not new rules | VERIFIED (inputs) | risk: CANON A34 "Evaluate, never add a rule or trigger"; Table 3's levels must not read as new triggers for changing the plan | This card |
| 21 | Q26-023 against Q15-026: Q26-023's "X-date in mid-2027 falls between the two deposits" is the binding date (about early March 2027 at the Aug-Nov pace), not the X-date; Q15-026 is right in substance | Store rows Q26-023, Q15-026; BPC (2026); NTU (Dickerson, 2026); DTS | TWOREASONS, COMPLETE2028 | NICHE | Table 3 row 3 and 3e use the corrected dates | Q26-023's own store note already says late 2027 to early 2028 | VERIFIED (both store rows; DTS, BPC and NTU read) | no | insights.jsonl |
| 22 | The current limit is $41,103,996m; Pub. L. 119-21 s.72001 (4 Jul 2025) raised the limit "as most recently increased by section 401(b) of Public Law 118-5" by $5,000,000,000,000 | 31 U.S.C. 3101 statutory notes; DTS 6 and 9 Nov 2026 | TWOREASONS | KNOWN | The law that sets today's limit, for 3e if a date is stated | None | VERIFIED (uscode.house.gov notes; DTS Table IIIC) | no | uscode.house.gov; fiscaldata |
| 23 | Headroom under the limit: $749,285m on 6 Nov 2026 and $739,767m on 9 Nov 2026 (debt subject to limit $40,354,711m and $40,364,229m) | DTS 6 and 9 Nov 2026, Table IIIC | TWOREASONS | KNOWN | Row 3's normal level: headroom shrinking, no date named | Day-to-day headroom moves with tax receipts and trust-fund flows; one reading is noise | VERIFIED (both DTS PDFs read) | no | fiscaldata.treasury.gov |
| 24 | The limit binds in 2027: BPC "between late winter and mid-summer of 2027"; CBO "sometime in 2027"; NTU May 2027 (February to July) | BPC (2026); CBO (2026); NTU (Dickerson, 2026) | TWOREASONS, COMPLETE2028 | KNOWN | Before the binding date nothing at all is at risk; the X-date is what matters | All three are projections; CBO's is from February | VERIFIED (BPC and NTU read in full; CBO passage) | no | BPC; NTU; CBO |
| 25 | The X-date: measures last "roughly six to nine months" (BPC); NTU central February 2028, Congress should act "by January 1, 2028", a deficit $10bn a month higher pulls it to January 2028; BofA "Nov '27", "uncomfortably close ... as early as Aug '27" | BPC (2026); NTU (Dickerson, 2026); Fortune (9 Nov 2026) | TWOREASONS, COMPLETE2028, FLOOR | NICHE | The X-date window, about Aug 2027 to May 2028, contains the January 2028 completion, backstop and floor purchase | Treasury has named no date; its 4 Nov refunding papers only "encourage Congress to act" | VERIFIED (BPC, NTU); UNVERIFIED (Fortune partial read; Treasury and TBAC excerpts only) | risk: SKELETON 3a and NUMBERS 5 fix the completion in January 2028, inside the X-date window (no change; a risk to record) | BPC; NTU; Fortune |
| 26 | Binding dates since 2013 came 9 to about 29 months apart (May 2013 to Feb 2014; Mar 2015 to Mar 2017; Mar 2019 to Aug 2021; Jan 2023 to Jan 2025); a 2028 fix lasting past Dec 2032 would be the longest since 2011, and CBO's $49.4T by end FY2031 needs more than $8.3T above today's limit against a record increase of $5T | 31 U.S.C. 3101 notes (Keel arithmetic); CRS IF10292 for CBO's $49.4T | TWOREASONS, RESERVE2033 | NICHE | Another standoff before December 2032 is likely; its exact timing is unknowable | Laws can suspend the limit for any length; history is not a rule | VERIFIED (statutory notes); UNVERIFIED (CRS figure from excerpts; Q15 read the CRS piece) | no | uscode.house.gov; CRS |
| 27 | The riskiest X-date for Laura is one near mid-December 2032, when IBTM's final payout funds both the 2033 payment and the contribution; in 1979 late checks were back to normal in under three weeks | SKELETON 3a; Q26 T17 (cash 18-22 Dec in four past endings); Q15 row 15 (1979) | TWOREASONS, FLOOR, RESERVE2033 | NICHE | Row 3's normal level: no X-date within three months of a payment to Laura or her funds; read daily if one is named | No projection reaches 2032; this is a window to watch, not a forecast | VERIFIED (dates from SKELETON and Q26; 1979 from Q15, not re-read) | no | This card |
| 28 | From January 2028 every waiting dollar sits in a Treasury-bill ETF (0 to 3 months), the securities a standoff delays first; in Oct 2013 bills maturing near the X-date yielded up to 47bp more and money funds announced no exposure to them | NUMBERS 0 ("Where waiting money sits"); Q15 row 20 | REINVEST, TWOREASONS, LADDER | NICHE | A delay there is late payment, not loss; it touches no payment to Laura before 1 Jan 2033 | The design test charges the ETF's fee, not a delayed bill | VERIFIED (NUMBERS 0 read; Q15 rows read) | risk: a delayed bill inside the ETF is not in NUMBERS' design test | NUMBERS; Q15 |
| 29 | Q26 T10 reads "a Treasury default" as a payment "one business day late". On that reading a 2027-28 delay of a coupon or a bill would be reason 2, although no payment to Laura falls before 1 Jan 2033 | Q26 T10; FINAL IPS l.17; CANON A34, C9 | TWOREASONS, CERTAINTY | NICHE | Lead decides what counts as a Treasury default and what "may change" means; a reading where reason 2 opens a review keeps A34 | GAO 2026: 13 impasses 2011-2025, no missed payment (Q15 row 24) | VERIFIED (texts read) | risk: the one-day reading widens reason 2 beyond "barring a US default" (C9) | Q26; IPS; CANON |
| 30 | Foundations Act Art. 25: the year's plan and budget pass the board within one month after the year begins and are filed; work report and accounts within five months after year-end; the authority's record is public within a month; the prior year's grant and donation lists are public; fine NT$30,000-150,000 | 財團法人法 Art. 25 | COSPONSOR, FUNDRAISING, HALFKEPT | NICHE | When a co-sponsor's budget becomes readable: about February-March each year | Applies to foundations under the Act; city-registered foundations' portals not checked | VERIFIED (law.moj.gov.tw Art. 25, Chinese and English) | no | law.moj.gov.tw |
| 31 | The timing does not fit: a co-sponsor's 2033 budget is public about Feb-Mar 2033, after Laura's contribution is paid (about 18 Dec 2032); the only filing readable before she pays is the 2032 plan (public about Feb-Mar 2032), where a 2031 meeting would land | Art. 25 (Keel arithmetic); SKELETON 3a; Q11d card 2 | COSPONSOR, HALFKEPT | NICHE | Kills the January-filings row: it arrives after the decision it would inform | A co-sponsor may also announce a gift before filing; Laura hears directly first | VERIFIED (Art. 25; SKELETON) | no | This card |
| 32 | A filings row fails the inclusion rule: it changes no instrument, date, custody or reason, only a call on the half kept (A31) and the 3d ask; it becomes a source in row 7 and the year-by-year assumption goes to 3e prose (Q11d) | This card; CANON A31; Q11d | COSPONSOR, HALFKEPT | NICHE | Row 7 names Laura's own records first, then public filings | None | VERIFIED (inputs) | risk: SKELETON 3e says "Table 3 gains ... the co-sponsors' January budget filings as signals"; that line needs to read "as a source for row 7" | SKELETON; this card |
| 33 | Public funders are a different signal: government-endowed foundations prepare their plan and budget before the fiscal year (Art. 55); ministry and city money follows the legislature's or council's budget vote (Q11d) | 財團法人法 Art. 55; Q11d | COSPONSOR, FUNDRAISING | NICHE | For a public co-sponsor, row 7 reads the budget vote, not a January filing | The budget vote's timing is from Q11d, not re-read | VERIFIED (Art. 55 read); budget vote from Q11d | no | law.moj.gov.tw; Q11d |
| 34 | Custody is the weakest row: holdings at one broker pass SIPC's $500,000 cover before 2033; all the money at the end is $589,655 in 1 Jan 2033 money (NUMBERS 8k), about $474,000 after the $115,268 contribution leaves (Keel arithmetic) | NUMBERS 8k; Q26 T33 (SIPC $500,000) | RESERVE2033, OTHER | KNOWN | Kept as row 8 because Wharton names the asset management team and the brief names custody; first row to move to 3e prose if space runs short | The register has no custody line or crossing date; SIPC covers a failed broker's missing customer property, not market loss | VERIFIED (NUMBERS 8k); UNVERIFIED here (SIPC limit from Q26, not re-read) | risk: custody is not in the IPS; whether to split holdings is implementation (lead decides) | NUMBERS; Q26 |

## (b) Cards

**Card 1. Killer items and the inclusion rule (Degani and Wiener, 1990 and 1993; Boeing and ATA).**
- What is it? NASA-funded field studies of airline checklists. They found two camps (every item, or only critical
  ones), crews shortcutting long lists to "killer items", and a design rule used by Boeing and the ATA: include only
  steps whose omission has "a direct and adverse impact on normal operation", and leave out what the aircraft already
  announces. Most critical first; no compromise on killer items; a detailed expanded checklist kept for training.
- Did it work? The papers are design guidance from interviews, observation and accident reports, not a trial. They are
  frank that no consensus on the item list is possible and that a minimal list is "even harder to defend after an
  occurrence".
- How is Laura's case like it? A long list (Q26, 33 rows) will be skimmed; a few signals, if missed, cost a payment or
  a planned step. Her broker statement and fund notices "annunciate" many events, as EICAS does.
- How is it not? Laura reads a table a few times a year, not 3-10 times a day; her items are signals, not switch
  settings; a miss is noticed late, not fatal at once.
- What Caplet takes: the restated killer test (miss alone costs a payment, leaves a planned step undone, or makes a
  stated figure untrue); the inclusion rule written under Table 3; the two reasons as rows 1-2; Q26 kept in the store
  as the expanded list. Report part 3e, exhibit Table 3.

**Card 2. WHO's checklist rules: Focused, Actionable, Brief, Tested (WHO 2009a, 2009b; Haynes et al. 2009).**
- What is it? The rules WHO gave hospitals for adapting its Surgical Safety Checklist: five to nine items a section,
  each tied to an unambiguous action, a minute a section, tested round a table and by one team before rollout, and
  never comprehensive.
- Did it work? In the eight-hospital study, deaths fell from 1.5% to 0.8% and complications from 11.0% to 7.0%, on a
  before-and-after design with no control group.
- How is Laura's case like it? A team (Laura and her asset management team) needs a short shared list that ties each
  item to an act, and the scorecard already asks for a stranger's read.
- How is it not? A surgical checklist is spoken aloud and repeated daily; Table 3 is printed and read rarely. WHO's
  numbers are surgical outcomes, not evidence about investment monitoring.
- What Caplet takes: eight rows; an action column ("what it changes") on every row, with "carry on" as row 6's action;
  the stranger test before 27 Nov. Report part 3e.

**Card 3. The eight-row cut (this card's "Table 3 cut" section).**
- What is it? Q26's 33 candidate rows reduced to eight in three tiers, with a fate for every row.
- Did it work? Every row of Q26 that changes an instrument, a date, custody or a reason is kept or merged into a kept
  row; the two dropped rows cannot happen or need no act (T12, T13); the two moved rows are already covered elsewhere
  (T15 in NUMBERS 3 and 3a; T22 as a one-time check).
- How is Laura's case like it? Wharton asks what "Laura or her asset management team should monitor as 2031 and 2033
  approach"; the IPS says only two things change the plan. Eight rows can show both.
- How is it not? Unlike a cockpit card, Table 3 must also show what does not change, which no killer-item rule covers.
- What Caplet takes: the eight rows, the fates, and SKELETON exhibits item 4's borrowed columns (normal level, reader,
  distance to trigger). Report part 3e, Table 3.

**Card 4. The next X-date, settled at the source.**
- What is it? The statute (Pub. L. 119-21 s.72001), the Daily Treasury Statement (headroom $739,767m on 9 Nov 2026),
  and three projections (BPC, CBO, NTU) put the binding date in 2027 and the X-date about August 2027 to May 2028.
- Did it work? Every standoff since 2011 ended before a missed payment (GAO 2026 via Q15); the warning time Treasury
  gave was 7 weeks to 137 days (Q15).
- How is Laura's case like it? Her January 2028 completion, backstop and floor purchase fall inside the window; from
  then on her waiting money sits in 0-3 month bills.
- How is it not? No payment to Laura falls before 1 Jan 2033, so a 2027-28 delay touches coupons and bills inside her
  funds, not her payments. The window that could touch a payment is mid-December 2032, and no projection reaches it.
- What Caplet takes: row 3 with the corrected dates; the replacement for store row Q26-023; one 3e clause that the
  standoff falls around the January 2028 completion; the lead's call on the reason-2 reading. Report parts 3a and 3e.

**Card 5. Co-sponsors' January filings (Foundations Act Arts. 25 and 55).**
- What is it? Taiwan's foundations file the year's plan and budget within a month of the year starting, with public
  disclosure about a month later, and file accounts and grant lists by the end of May.
- Did it work? The filings exist and are public on the competent authority's portal (Q11d row 22's example).
- How is Laura's case like it? Co-sponsor money comes year by year in NT$ (Q11d), and the half kept's third use is "a
  co-sponsor falling short" (A31).
- How is it not? The filing that could show 2033 money is public after Laura pays; she hears from co-sponsors before
  any filing; the filings are in Chinese on the authority's portal.
- What Caplet takes: a source inside row 7, not a row; the year-by-year assumption in 3e prose; SKELETON's 3e line
  amended. Report parts 3d and 3e.

## (c) Verdicts

**Claim 1: KEEP, with changes.**
- The cut holds: the fate table below accounts for all 33 rows (8 + 21 + 2 + 2 = 33).
- What the sources do and do not say. Degani and Wiener (1990) treat the item list as unresolved ("a consensus can
  never be reached"). Their 1993 paper defines killer items and admits brevity and repetition conflict. They give no
  numeric size. The inclusion rule that works is Boeing's and the ATA's, which they quote. WHO gives the size (five to
  nine) and the action rule. So the claim's wording "using checklist design's rule of 'killer items'" overstates the
  source. Change it to: killer items for the top rows, Boeing's inclusion rule for the rest, WHO's five to nine for the
  size.
- The restated test and how each row scores:
  - Row 1 (2028 deposit): killer. A missed deposit leaves $2,287 of the ladder unbought, the 2033 payment $3,016 short at
    forwards, and the ten $57,455 short at 0% (NUMBERS 5).
  - Row 2 (Treasury payment on time): killer. It is reason 2.
  - Row 3 (debt limit, X-date): not a killer on its own; row 2's early warning on transient data (Degani and Wiener's
    allowed duplicate).
  - Row 4 (fund notices): killer. A fund extended past 31 Dec would pay after the 1 Jan payment unless sold first (Q26
    T18).
  - Row 5 (trade days): killer. A missed completion leaves a planned step undone; a meeting before the move would make
    a stated top not yet owned (2.9% to 10.7% of house paths if stated 1 to 12 months early, NUMBERS 4).
  - Rows 6-8: not killer items. Row 6 is kept because the IPS rule must be visible ("A fall in the market is not one of
    them", l.17); row 7 because the IPS names three uses of the half kept (A31) and Wharton asks about flexibility as
    2033 approaches; row 8 for custody, the weakest.
- The rule to write under the table (notes, not prose): a row earns a place if missing it alone could cost a payment,
  leave a planned step undone or make a stated figure untrue, or if it shows something the IPS says never changes the
  plan; everything else stays in the expanded list.
- The IPS rule stays visible: two Reason rows, three Look closer rows, three Watch rows; every row has a "never
  changes" cell.

**Claim 2: CHANGE.**
- Settled facts (11 Nov 2026):
  - Limit $41,103,996m (DTS Table IIIC), set by Pub. L. 119-21, title VII, s.72001 (4 Jul 2025), a $5T increase on the
    limit that returned on 2 Jan 2025 after Pub. L. 118-5's suspension.
  - Headroom $749,285m (6 Nov) and $739,767m (9 Nov).
  - Binding: BPC late winter to mid-summer 2027 (4 Jun 2026); CBO "sometime in 2027" (Feb 2026); NTU May 2027 (20 Aug
    2026).
  - X-date: BPC six to nine months after binding; NTU central February 2028; BofA November 2027 (UNVERIFIED, partial
    read). Treasury has named no date.
- So the first half of the claim is true only in a misleading way: the next X-date is about August 2027 to May 2028,
  well before 2031, and its importance for Laura is the January 2028 completion, not the 2031 meetings.
- The second half ("again before December 2032") is likely, not certain. Evidence for: binding dates 9 to about 29
  months apart since 2013; CBO's projected $49.4T by end FY2031 (CRS, UNVERIFIED here) needs more than $8.3T above
  today's limit. Evidence against certainty: Congress can suspend the limit for any length. No source projects a 2031
  or 2032 X-date.
- Q26-023 against Q15-026: **Q26-023 is wrong** in its "use" line ("an X-date in mid-2027 falls between the two
  deposits"); it treats the binding date as the X-date. **Q15-026 is right** and its figures check against the sources
  read here; its NTU citation names "How Congress should respond to the debt limit" while the projection figures were
  read here in "Projecting the Debt Limit" (same author and date; see Gaps). Its own note (drop the "only payment in the
  window" line, since the funds also pay monthly) stands.
- Replacement text for store row Q26-023 (a store note, not report prose): "Debt-limit headroom was $749,285m on 6 Nov
  2026 and $739,767m on 9 Nov 2026 (DTS Table IIIC; limit $41,103,996m set by Pub. L. 119-21 s.72001). The limit is
  projected to bind between February and mid-summer 2027 (BPC June 2026; CBO 'sometime in 2027'; NTU May 2027);
  extraordinary measures then last about six to nine months (BPC), so the X-date falls about August 2027 to spring 2028
  (NTU central February 2028), around the January 2028 completion, not mid-2027 between the deposits. Projections, not
  forecasts; Treasury has named no date."
- What it means for the plan (nothing changes; risks to record):
  - The January 2028 completion, backstop and floor purchase may be priced during a standoff (in Oct 2013 long yields
    were 7bp lower, Q15 row 20). Nothing in the plan moves (A34).
  - From January 2028 the waiting money's bill ETF holds the securities a standoff delays first. A delay is late
    payment, not loss, and no payment to Laura falls due before 1 Jan 2033.
  - The one window where a delay could touch a payment is mid-December 2032 (IBTM's final payout funds the 2033 payment
    and the contribution). No projection reaches it, so it goes into row 3's normal level, not into a forecast.
  - Q26 T10's reading ("one business day late") would make a 2027-28 technical delay reason 2. The lead decides.

**Claim 3: KILL as its own row; CHANGE into a source.**
- Art. 25 timing: plan and budget passed and filed within one month of the year starting; public within a month of the
  authority's record; accounts and grant lists within five months after year-end.
- Laura's decision dates: the stated range at the 2031 meetings; the contribution paid about 18 Dec 2032. The 2033
  filing comes after both. Only the 2032 plan (public about Feb-Mar 2032) is readable before she pays.
- Inclusion rule: the filing changes no instrument, date, custody or reason. It can only inform a call on the half
  kept (A31) and the 3d ask. Laura's own records of what each co-sponsor told her come first and come earlier.
- Public funders: Art. 55 foundations budget before the year; ministry and city money follows the budget vote (Q11d).
- So: no row of its own. Row 7 names its sources (Laura's records first, then the co-sponsors' filed plans and grant
  lists, then the budget vote for public funders). The year-by-year assumption goes to 3e prose (Q11d). SKELETON 3e's
  line "Table 3 gains ... the co-sponsors' January budget filings as signals" should read "as a source for row 7".

## Table 3 cut (notes, not report text)

**The eight rows.** Levels: Reason (the IPS's two reasons), Look closer (a check that can change an instrument or a
date, never the plan), Watch (shown so the reader sees it changes nothing, or changes only the half kept). Reader in
Wharton's words: "Laura or her asset management team" (here "Laura" or "team"). Figures: NUMBERS sections as named;
Keel arithmetic marked.

| Row | Level | Signal | Reader | Normal level (carry on) | Trigger and its distance today | What it changes | What it never changes | Built from (Q26) |
|---|---|---|---|---|---|---|---|---|
| 1 | Reason | The 2028 deposit: arrives, and its size | Laura | $150,000 in Jan 2028; the order runs: completion ($38,282), backstop, "most" to the floor, the rest to VT (NUMBERS 4, 5) | Missed = reason 1 (cut-off date: lead decides). Smaller: escrow standard holds unless the deposit falls by more than 74.5%; payments stay full at forwards unless more than 98.4% (NUMBERS 5) | Missed: the plan may change ($2,287 of the ladder unbought; 2033 payment $3,016 short; ten $57,455 short at 0%). Smaller: floor and VT shrink in order ($112,500 gives a stated bottom of $65,000) | A smaller deposit is not a reason (D9); the order | T5 + T4 |
| 2 | Reason | Each Treasury payment to Laura or her funds made on its due date | Team (broker statement on each due date) | Credited on the due date (coupons 15 Feb/15 Aug for the Feb-2037 bond, 15 May/15 Nov for the others) | Not made on its due date = reason 2 (what counts as "a Treasury default": lead decides). Distance: 13 impasses 2011-2025, no missed payment (Q15) | The plan may change | A downgrade, a price fall, a buyback offer | T10 + T11, T14 |
| 3 | Look closer | Debt limit and X-date (row 2's early warning) | Team (DTS Table IIIC; Treasury letters; CBO, BPC) | No X-date named within three months of a payment to Laura or her funds; read monthly | Treasury names an X-date: read daily, list holdings and coupons due near it. Headroom $739,767m on 9 Nov 2026; binding about Feb to mid-2027; X-date about Aug 2027 to May 2028, around the Jan 2028 completion | Nothing in the plan; the Jan 2028 completion may be priced in a standoff | The order; the payments; the dates | T7 + T8, T9 |
| 4 | Look closer | Fund notices (five iBond rungs, the floor fund, VT, the bill ETF) | Team (fund supplement each mid-October of a fund's last year; broker statement late December) | Ending notice mid-October; cash 18-22 Dec; fees unchanged (4 of 4 past endings on time, Q26 T17) | No notice by 31 Oct; an extension (sell before the payment); an early end (buy a Treasury maturing before the same payment); cash not credited by 28 Dec; a fee rise; a fund paying more than 0.5% below its holdings (at 0.75%, a range end short in 5.0% / 6.0% of paths, by at most $339 / $429, NUMBERS 3); VT changing its index | An instrument or a date | The plan; the five T-bonds (not callable, cannot be extended) | T17 + T1 (fund dates), T6, T18, T19, T20, T21, T24, T27 |
| 5 | Look closer | The plan's own trade days: 1 Jan 2027, Jan 2028 completion, the 2031 move before the meetings | Team; Laura for the meeting dates | Trade on the planned day; the move before the first meeting; nothing stated before the move | A trading halt; a premium or discount over 2% for more than seven trading days (Rule 6c-11, Q26 T16); a meeting set before the move (a top stated 1 to 12 months early is not yet owned in 2.9% to 10.7% of house paths, NUMBERS 4) | A date, by days | The step itself; the order | T1 + T16, T23, T28 |
| 6 | Watch | Market prices: Treasury yields and VT | Team | Any level: carry on | None, by design (IPS l.17). Central range $95,000 to $115,000; stated bottom house 1-in-20 $85,000 / $95,000 / $115,000; top $95,000 / $115,000 / $140,000 (NUMBERS 4) | Numbers only: the completion price and the bottom are fixed in Jan 2028, the top on the move day; after the move only the half kept moves ($21,347; house $9,881 / $20,739 / $41,258, NUMBERS 4) | The payments; the order; the dates; the two reasons | T25 + T2, T3, T26 |
| 7 | Watch | The half kept's three uses: building costs, the Taiwan dollar, co-sponsors | Laura | USD/TWD near 32.768; Taiwan building costs within 5.0% a year over five years; co-sponsors as pledged | TWD at its ten-year strongest, 27.52: $18,116-$21,930 more (NUMBERS 8d); the half kept covers a 10% stronger TWD in 93.2% of house paths, 99.77% with the excess (8j); a five-year cost pace above 5.0% (Sep 2026 +7.29% y/y, 8d); a co-sponsor cut, or an overrun past the builder's contingency. Sources: Laura's records first, then filed plans and grant lists (Art. 25) or the budget vote (public funders) | A call on the half kept (A31), outside the stated range | The stated range; the payments; the instruments | T29 + T30, T31, T32; claim 3's filings as a source |
| 8 | Watch | Custody: holdings at one broker | Team | Under SIPC's $500,000 per customer per capacity (Q26 T33) | Above it before 2033: all the money at the end is $589,655 in 1 Jan 2033 money (NUMBERS 8k), about $474,000 after the contribution leaves (Keel arithmetic) | Where assets sit (implementation; lead decides) | What is held | T33 |

**Fates of Q26's 33 rows (8 kept as a base, 21 merged, 2 moved, 2 dropped).**

| Q26 row | Signal | Fate | Reason |
|---|---|---|---|
| T1 | The plan's own dates | Kept as row 5 (fund dates merged into row 4) | Trade days are killer items; fund dates live where the fund notices are |
| T2 | Yields before 1 Jan 2027 | Merged into row 6 | Changes a cost, not the plan; the purchase is weeks away |
| T3 | Yields in 2027 to the Jan 2028 completion | Merged into row 6 | Changes the completion price only ($38,282; $41,630 after a 1-point fall, Q26) |
| T4 | Size of the 2028 deposit | Merged into row 1 | Same event as T5; the distances 74.5% and 98.4% go in row 1 |
| T5 | Deposit missing | Kept as row 1 | Reason 1, a killer item |
| T6 | Bill ETF fee above 0.15% | Merged into row 4 | A fund notice; $1,414 spare at 0% (NUMBERS 2) |
| T7 | Debt-limit headroom | Kept as row 3 | Early warning for reason 2 |
| T8 | X-date projections | Merged into row 3 | Same signal, next step |
| T9 | Bill-curve kink | Merged into row 3 | A market sign of the same signal |
| T10 | Treasury payment not made on its due date | Kept as row 2 | Reason 2, a killer item |
| T11 | Credit ratings | Merged into row 2 ("never changes") | A downgrade is not a default |
| T12 | A call on a T-bond | Dropped | Cannot happen: none of the five is callable |
| T13 | Buyback offers | Dropped | Voluntary; needs no act; UNVERIFIED in Q26 |
| T14 | Coupons credited | Merged into row 2 | The broker statement "annunciates" it; a missing coupon is row 2's trigger |
| T15 | iBond NAV and cash share | Moved to 3a prose | Already in NUMBERS 3 (payout moves 1.6-2.1% if final cash earns nothing) and inside the escrow standard; no act |
| T16 | Premium or discount over 2% | Merged into row 5 | Matters only on a trade day |
| T17 | Ending notice mid-October | Kept as row 4 | A fund extended past 31 Dec could miss a payment |
| T18 | Extension past 31 Dec | Merged into row 4 | Same notice; the act is to sell before the payment |
| T19 | Early end | Merged into row 4 | Same notice; the act is to buy a Treasury maturing before the payment |
| T20 | Cash not credited by 28 Dec | Merged into row 4 | Same event, last step |
| T21 | Fund paying more than 0.5% below holdings | Merged into row 4 | A fund-level cost; NUMBERS 3 sizes it |
| T22 | Non-government money market fund inside a fund | Moved to a one-time check before 27 Nov | Read IBTM's and the rungs' holdings files once; if only Treasury money funds, nothing to watch; if not, it joins row 4's cost trigger |
| T23 | Trading halt | Merged into row 5 | Matters only on a trade day |
| T24 | Fund fee above 0.07% | Merged into row 4 | A fund notice |
| T25 | VT before the move | Kept as row 6 | Shows the IPS rule: a market fall is not a reason |
| T26 | VT after the move | Merged into row 6 | Changes only the half kept |
| T27 | VT index change or closure | Merged into row 4 | A fund notice; the act is to hold a fund on the same world-shares market |
| T28 | Move date against the meeting calendar | Merged into row 5 | A trade day against Laura's calendar |
| T29 | USD/TWD | Kept as row 7 | One of the half kept's three named uses |
| T30 | Taiwan construction costs | Merged into row 7 | Second named use |
| T31 | Co-sponsor commitments | Merged into row 7 | Third named use; the January filings join here as a source |
| T32 | Builder's contingency | Merged into row 7 | Overruns are the first named use |
| T33 | Custody | Kept as row 8 | Wharton names the asset management team; weakest row, first to move to prose |

**Notes for whoever builds the exhibit.**
- Order: rows 1-2 (Reason) first, then 3-5 (Look closer), then 6-8 (Watch). Most critical first (Degani and Wiener
  guideline 10).
- Every row keeps a "what it never changes" cell: that column is how the IPS rule (watch many things, change the plan
  for only two) stays visible.
- Do not borrow numeric triggers for the two reasons (SKELETON exhibits item 4). The 74.5% and 98.4% are distances, not
  triggers.
- The inclusion rule goes under the table as a note; Q26 stays in the store as the expanded list.
- Stranger test before 27 Nov (WHO "Tested"): a reader outside the team reads the eight rows and says what Laura does
  if each trigger fires. Pass: all eight answered right, including "nothing" for row 6.
- If space forces seven rows, row 8 moves to one clause of 3e prose.

## (d) Gaps

- Retraction status: Degani and Wiener (1993) checked on the SAGE article page (no retraction or correction notice);
  the Retraction Watch database itself was not queried. The author copy's header says "pp. 28-43", which does not match
  the journal's 345-359; the journal pagination is used.
- Haynes et al. (2009) read as reprinted in WHO (2009a) (abstract, methods, intervention), not on the journal site; the
  reprint gives the author list and the DOI (10.1056/NEJMsa0810119); the issue number was not checked.
- Miller (1956) and Swain and Guttman (1983) are quoted only as Degani and Wiener use them; not read.
- Treasury's 4 Nov 2026 refunding statement and the TBAC report, Fortune (9 Nov 2026, BofA's forecast), Bloomberg,
  BPC's Deficit Tracker (15 Oct 2026) and CRS IF10292 were seen in excerpts only: UNVERIFIED for quoting. Fortune's
  "$557 billion of room" does not match the DTS headroom and is unexplained.
- NTU: Q15-026 cites Dickerson (2026), "How Congress should respond to the debt limit"; the projection read in full here
  is Dickerson (2026), "Projecting the Debt Limit" (same author and date, different URL). Both pages exist; the store
  should cite the one whose figures it quotes.
- REFERENCES_APA.md #34 (CBO) gives publication/61882 while the Q10 and Q15 cards use publication/62105 for the text;
  the entry already says "use one URL". Not fixed here.
- None of the new sources (Degani and Wiener; WHO; Haynes; BPC; NTU; DTS; 31 U.S.C. 3101; 財團法人法) is yet in
  REFERENCES_APA.md.
- The X-date window (about Aug 2027 to May 2028) is Keel arithmetic on BPC's two windows; no source gives a 2031 or
  2032 X-date, and none can yet.
- Custody: the register has no custody line and no date when holdings first pass $500,000; SIPC's limit was not re-read
  here (Q26 T33). The $474,000 after the contribution is Keel arithmetic ($589,655 less $115,268, NUMBERS 8k).
- City-registered foundations' disclosure portals and the legislature's budget calendar were not checked (Q11d holds
  the budget-vote point).
- Pub. L. 119-21's enacted short title was not checked; it is cited by number only.

## Sources (APA 7; all accessed 11 Nov 2026)

- Bureau of the Fiscal Service. (2026a, November 6). *Daily Treasury Statement* (Table IIIC). U.S. Department of the
  Treasury. https://fiscaldata.treasury.gov/static-data/published-reports/dts/DailyTreasuryStatement_20261106.pdf (read)
- Bureau of the Fiscal Service. (2026b, November 9). *Daily Treasury Statement* (Table IIIC). U.S. Department of the
  Treasury. https://fiscaldata.treasury.gov/static-data/published-reports/dts/DailyTreasuryStatement_20261109.pdf (read)
- Congressional Budget Office. (2026). *The budget and economic outlook: 2026 to 2036*.
  https://www.cbo.gov/publication/61882 (REFERENCES_APA #34; debt-limit passage only)
- Degani, A., & Wiener, E. L. (1990). *Human factors of flight-deck checklists: The normal checklist* (NASA Contractor
  Report 177549). NASA Ames Research Center. https://ntrs.nasa.gov/api/citations/19910017830/downloads/19910017830.pdf
  (read in full)
- Degani, A., & Wiener, E. L. (1993). Cockpit checklists: Concepts, design, and use. *Human Factors, 35*(2), 345–359.
  https://doi.org/10.1177/001872089303500209 (author copy read in full; SAGE page checked, no retraction or correction
  notice)
- Dickerson, M. (2026, August 20). *Projecting the debt limit*. National Taxpayers Union.
  https://www.ntu.org/publications/detail/projecting-the-debt-limit (read in full)
- Haynes, A. B., Weiser, T. G., Berry, W. R., Lipsitz, S. R., Breizat, A.-H. S., Dellinger, E. P., Herbosa, T.,
  Joseph, S., Kibatala, P. L., Lapitan, M. C. M., Merry, A. F., Moorthy, K., Reznick, R. K., Taylor, B., & Gawande, A.
  A. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. *New England
  Journal of Medicine, 360*, 491–499. https://doi.org/10.1056/NEJMsa0810119 (read as reprinted in WHO 2009a, which
  carries the author list and the DOI; issue number not checked)
- Office of the Law Revision Counsel. (n.d.). *31 U.S.C. § 3101: Public debt limit* (with statutory notes, including
  Pub. L. 119-21, title VII, § 72001, 139 Stat. 332). United States Code.
  https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title31-section3101&num=0&edition=prelim (read in full)
- Quakenbush, C., Till, A., & Akabas, S. (2026, June 4). *When will we reach the debt limit (again)?* Bipartisan
  Policy Center. https://bipartisanpolicy.org/article/when-will-we-reach-the-debt-limit-again/
  (read in full)
- 財團法人法 [Foundations Act], arts. 25, 55 (2018). 全國法規資料庫 [Laws and Regulations Database of the Republic of
  China (Taiwan)]. https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0020030&flno=25 and
  https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0020030&flno=55 (read in Chinese; English at
  https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=I0020030)
- World Health Organization. (2009a). *WHO guidelines for safe surgery 2009: Safe surgery saves lives*
  (WHO/IER/PSP/2008.08-1E). https://iris.who.int/server/api/core/bitstreams/c2ea24bb-10f7-48e4-8f63-55932e817ddc/content
  (Sections I, III and IV and the reprinted study read)
- World Health Organization. (2009b). *Implementation manual: WHO surgical safety checklist 2009*.
  https://iris.who.int/server/api/core/bitstreams/135fa0d8-8c94-4ecc-a606-c1a8d41ecc7d/content (read in full)
- Seen in excerpts only, UNVERIFIED: Fortune (2026, November 9), BofA's X-date forecast; U.S. Department of the
  Treasury (2026, November 4), quarterly refunding statement and TBAC report; Bipartisan Policy Center, Deficit Tracker
  (2026, October 15); Congressional Research Service (2026, September 21), *The debt limit* (IF10292),
  https://www.congress.gov/crs-product/IF10292.
