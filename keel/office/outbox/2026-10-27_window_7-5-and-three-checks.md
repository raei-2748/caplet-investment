# The Window, Tue 27 Oct 2026: six facts the rewrite was about to build on were wrong; Draft 4 has none

(Keel is a simulated team, AI-written.) AI-generated check by the Keel Office (Claude Code; Felix = Rules & Integrity,
fact-checker role; two subagents checked ~137 claims, and the Window re-checked each FALSE one at source). Not for
submission. Cite in the Works Cited. Read only: WInS, SMApply and Caplet's Google Docs were not opened.
Work order: SD-WIN-03 | self-directed (Window routine) | Tue 27 Oct 2026, 08:40 AEDT

## Breaches and near-breaches (top)
No rule breach and no new official file since 25 Oct. Six **false facts** in files the rewrite reads. None is in a
draft yet. Each now carries a `[Window 27 Oct: ...]` note on the line itself, so nobody builds on it.

| # | Where | Said | True (source, read 27 Oct 2026) |
|---|---|---|---|
| N1 | R04 #7, R02 (x2), THINKING_LOG day 1, the Window's own D1 checklist | The TNA's 7.5% is EAFE; "the IPS must not repeat 7.5%" | **Wrong edition.** J.P. Morgan release, 19 Oct 2026: "Global equities are projected to return 7.5% (USD), increasing from 7.0%" (am.jpmorgan.com, via WebFetch; same text on finviz.com). The Noticeboard found it first; Window confirms it |
| N2 | Laura's Room LR-03 (memo + rewrite inbox) | Donors respond to a lead gift "existing, not its size" | **The cited study shows the opposite.** List & Lucking-Reiley: "Increasing seed money from 10 percent to 67 percent of the campaign goal produced a nearly sixfold increase in contributions" (poverty-action.org). The **ratio** of a match doesn't matter (Karlan & List); the **size** of a committed sum does |
| N3 | R05 #7 | Fong-Vasicek M²: the Feb-2037 4.75% bond leaks most | **Backwards.** Length beats coupon. Per dollar, flat 5% from Jan 2027: Feb-37 ~20, May-38 ~23, Nov-39 ~28, Nov-40 ~34, Nov-41 ~35 (re-computed twice) |
| N4 | rung2 F-B, F-C | "Redington's third condition"; "our range (p5 to p95, so 90%)"; the case asks for "a range with a confidence" | Redington's third condition asks for asset spread **greater** than the liability's; equal spread is cash-flow matching (M²). The range is floor to floor + half of VT, **~99%** (`IPS_number_sheet.md`). The case says "a credible range" and "state how confident" (:116-118) |
| N5 | Library `## Now`, Library and Long Room memos | Contac 600 is "a 1952 cold capsule with four bead coatings" | **1960** (the Spansule was 1952). Four bead groups, but one is uncoated, so three coats: 3, 6, 9 h (Hillery & Hoffman, basicmedicalkey.com mirror) |
| N6 | R05 #14, proposed IPS line | "staying inside is guaranteed by design" | The cap guarantees the **top**. The bottom can break: 0.75% of paths without a buffer, 0.11% with $10k (LR-02 / C-01, 22 Oct curve, MODEL). A true line that keeps the flair: *"The cap makes the top a promise we keep by design; the number worth stating is the chance of reaching it."* |

Small: R05 dates the DB funding code 29 Aug 2024; it was laid **29 Jul 2024** (TPR press release). The Archive's A14
memo is stale (the bible cleared it). Writing Room: `test_textcheck.py` now has 6 tests, not 7, and the overclaim line is obsolete.

## What it changes for the judges
1. **The VT line holds.** If the IPS gives a return, 7.5% matches the TNA. The 2027 edition also moved US large cap to
   7.5% (from 6.7%) and US intermediate Treasuries to **4.6%** (from 4.0%). `CLAUDE.md` "Key facts" still lists the
   2026 rows as current; that file is Ray's (outside `keel/`), so this is flagged here, not edited.
2. **N2 reverses an argument and turns it into an aha.** If a bigger committed sum raises giving, every dollar shaved
   off the bottom (D1b's margin) buys credibility and costs co-sponsor money. That's a real trade-off with a price on
   both sides. A judge can follow it, and the Final Report can cite it. Neither study tests the *uncommitted* top.
3. **Any motif line naming Contac says 1960.** "Ten coatings, ten Januaries" is still fine as a picture.

## Draft 4 (V24), line by line against `00_GROUND_TRUTH.md`
No false fact. Checked at source: the Lehman line (FINRA fined UBS $2.5m plus $8.25m restitution; UBS "failed to
emphasize they were unsecured obligations of Lehman Brothers", finra.org, 2011). The buyers were UBS's clients
holding Lehman's paper, so "Lehman's customers" is true in substance. Also checked: "nothing but cash" at the December
close (iShares termination, R04 #8); "rarer, not smaller" (Bodie); "nobody else may help" (case :94-95); and "something
matures before every January". Every TNA lock in GT s3 holds. Upgraded to VERIFIED: Palladone withdrawn July 2005 over
alcohol dose dumping; FINRA/UBS Lehman PPNs.

## Instruction check (three of yesterday's outputs against `INSTRUCTIONS.md`)
- **D4:** I34 met (R = redemption, both meanings); I35 met (one clause, near-ironclad). It was written 23:01 Sydney,
  20 minutes before the cover note, so it is not an I41 breach.
- **Noticeboard 7.5% memo:** I14 (states what changes for judges) and I33 (source and date) met.
- **R05:** I04 met (19 concepts, each applied). Its one "overclaim" (#10) is a false claim fixed ("the funds sell any
  day", which failed in March 2020), not word-policing, so I10 holds.
- WO-R5 to R7 (23:36) ask for research, not drafts, so I41 holds. No row was breached; nothing goes in an Evidence cell.

## Labels and self-changes
`keel/drafts/ips_v4_1_2026-10-25/` had no label: `LABEL.md` added. The rewrite drafts are labelled by their folder
READMEs. There were no new Keel entries in `SELF_CHANGES.md`, so there was nothing to check against `INVARIANTS.md`.

## Root cause and Keel's call
Three of the six errors were cases where a source's sentence was right but the conclusion drawn from it was wrong (N2, N4, N6).
**Keel's call:** from today, the Window reads every new "so ..." line beside the source it rests on, not only the
quote. It goes in the runbook as a room rule, logged in `../../pm/SELF_CHANGES.md` (Keel self-change 1 of 3 this week).

## Takes
- **Felix:** Yesterday we checked every quote and they were all perfect. The mistakes were in the word "so": a sixfold
  rise got summarised as "size doesn't matter". From now on I read the "so" as hard as the quote.
