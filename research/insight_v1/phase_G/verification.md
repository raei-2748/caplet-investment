# Phase G verification of the six insight_v1 outputs

**Summary (5 lines)**
1. I checked six files adversarially against `phase_E/E6_final_spec.md` and the output of `scripts/E6_final_checks.py` (re-run 2026-09-28, exit 0).
2. I found 19 problems: 1 blocking, 7 important and 11 minor. I fixed 18 in place with minimal edits. One minor item was left because it is consistent with the spec's illustration.
3. The blocking problem was privacy. A parked question in `open_questions.md` quoted a D13a EXCLUDE-PRIVACY line and called it Laura's advice. That text is now withheld.
4. The important problems were: rates-fall figures in `strategy_changes.md` that the spec had already corrected; Laura's word "unstable" in the IPS B2 element list; an unqualified "lock-early misses none"; a lock-early design mixed with REC in one comparison; and three files naming tickers without the PENDING label.
5. After the fixes, every number matches E6 [1]-[8] or the spec. The deadlines, the (ii)R book, REC vs ALT, the three notes and rules R1-R10 agree across files. Every Laura line presented as hers is D13a VERIFIED-PRIMARY.

**Serves:** Trading Notes (Oct 23) and IPS (Nov 6), as a quality check on the files the team will read. This file is AI-generated verification. It contains no deliverable text.

**Status labels:** as in brief s3 (VP, VRF, SNIP, ASM, MODEL, INT). Severity: **blocking** = breaks a hard rule (privacy, quote, submission text); **important** = a wrong or overclaimed number, a cross-file contradiction or a missing mandatory label; **minor** = precision, wording or labelling.

---

## 1. Problems found

| # | File | Problem | Severity | Fixed |
|---|---|---|---|---|
| 1 | open_questions.md | Parked item M217 quoted a D13a **EXCLUDE-PRIVACY** line (B8b-Q34, a personal-life advice line) and called it "Laura's identity-context advice" | blocking | yes: the quote text is withheld and the entry points to the id and the ruling |
| 2 | strategy_changes.md | I9 gave the rates-fall stock fund as "$23k / $7k / $0, minimum $137k" (only the "5-year unchanged" branch). It also said "the spec's R2 row still prints E4 [7]'s $31k / $15k / $147k", which is false: the spec now prints E6 [8]'s ranges | important | yes: now $20-23k (-50bp), $1-7k (-100bp), and at -150bp no fund and a minimum of $127-137k, as in E6 [8] and the spec R2 |
| 3 | ips_spec.md | Section (e), item 4, is the list of what B2 must contain. It carried Laura's own word "unstable" inside the gap (i) element, so it read as IPS content. Brief s16 bans Laura quotes in the IPS | important | yes: gap (i) now cites the case (career income, L43-45). Her word is marked "background only, never in the IPS or the notes" (B8b-Q18) |
| 4 | why_us.md | R1 said "lock-early misses none" next to growth-first's miss rate if the deposit is $0. That is a certainty claim stronger than the evidence. The joint tail (rates fall before January 2027 with no deposit) leaves $11,957 or $31,413 of the 2033 payment unfunded (E6 R2) | important | yes: the claim is now scoped to the model's 9/25 curve, and the joint tail is stated |
| 5 | why_us.md | R1 compared growth-first with lock-early "$207k / $273k". Those numbers come from `strategy_mc.py`, which models the council's 60%-equity design, not REC. REC's p95 on the E6 basis is $250k | important | yes: the source design is labelled and REC's $207k/$250k (E6 [2]) is given |
| 6 | why_us.md | Names IEF, TLH, IBTM and VT with no PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK label | important | yes: a label line and a pointer to the alternates |
| 7 | strategy_changes.md | Names IEF, TLH, TLT, IBTM, VGIT, SPTL, VGSH, VT and EWT with no PENDING label | important | yes: a label line and a pointer to the alternates |
| 8 | open_questions.md | Names 12 tickers (e.g. IEF, TLH, IBTM, SGOV) with no PENDING label | important | yes: a label line and a pointer to the alternates |
| 9 | ips_spec.md | The B6 evidence for VT said "PENDING WInS AVAILABILITY CHECK" (no position-limit part, no alternates). R10 did not point to alternates | minor | yes: the full label, VT alternates (VTI + VXUS, ITOT + IXUS), and an alternates pointer in R10 |
| 10 | securities_and_allocation.md | The summary was one paragraph, not the required 5-line summary | minor | yes: 5 numbered lines with the same content |
| 11 | why_us.md | The reasons were named R1-R8, which collide with the spec's decision rules R1-R10 (e.g. "makes R3, R6 and R8 visible") | minor | yes: a one-line note that R1-R8 here are reasons, not rules |
| 12 | ips_spec.md | Word budget said content "about 390" and total "about 455-460". The ten blocks sum to 385 and the spec says 385 / 455 | minor | yes |
| 13 | ips_spec.md | Section (d) gave the stock fund "a six-year horizon to 2033". The fund is bought in January 2028 and held to January 2033: five years | minor | yes |
| 14 | ips_spec.md | The Vanguard-type return input was labelled "VP via the cited files". E6 [4] labels the 5.08% blend an ASSUMPTION hybrid | minor | yes: "5.08% compound, an ASM hybrid built on VP inputs, E6 [4]" |
| 15 | why_us.md | "we trade about $14k of median gift". The spec says $174k against about $186-188k, which is $12-14k | minor | yes |
| 16 | strategy_changes.md | Insight 4 quoted "takes the jump", an altered form of D13a B1b-Q11 ("you should always take the jump"). Brief s3 says never polish a quote | minor | yes: the exact wording is restored |
| 17 | open_questions.md | Summary item 3 and the "spec inconsistency" note said the R2 issue was fixed in three files. `strategy_changes.md` was still wrong (item 2) | minor | yes: the note now lists all four files and the corrected ranges |
| 18 | trading_notes_pack.md | Section 3 (position-limit branches) named SPTL, VGLT, VGIT and IBTM with no label in that section | minor | yes: a label line |
| 19 | strategy_changes.md | T3 says "4 trades, $100". That is true on the IBTM route; on the 2032-note route it is 3 x $25 + $10 = $85 | minor | no: it matches the spec's IBTM illustration, and the spec's "4-6 trades, $50-150" covers both |

**Observations (not problems, left unchanged):**
- `why_us.md` says "No blind multi-evaluator tournament was run". During this check, `phase_E/tournament/` (firm_A-F, fairness_log) was being written, with no verdict yet. The statement is true now. If a verdict lands, update `why_us.md` limit 5 and section 0.
- `open_questions.md` M020 mentions the pronouns listed on her public professional site. They are not in the D13a EXCLUDE-PRIVACY list, and the case itself uses "she". I judged this public-professional and left it.
- `open_questions.md` M103 ("would Laura call 'gimmicks'") is verbatim parked-question text in a log. It is not a recommendation. D13a limits "No more gimmicks." to its drafts context, and `ips_spec.md` f3 already warns about it.
- Near-sentence content copied from the spec's pitch element ("each deposit buys a promise when it arrives") appears in `ips_spec.md`, `why_us.md` and `strategy_changes.md`. So do short vocabulary phrases in quotation marks ("moves like a Treasury maturing in late 2032"). All come from the spec and are labelled as content or vocabulary, not drafted text. The five-word copy check (trading_notes_pack s8) will catch any verbatim reuse.
- The D13a JSON holds 106 entries: 93 VERIFIED-PRIMARY, 7 EXCLUDE-PRIVACY and 6 PARAPHRASE-UNVERIFIED. Brief s16 says 91 / 7 / 6. The difference is the later N-series additions (e.g. D13a-N01). It does not affect the six files.

---

## 2. Checks run

**Ground truth.** I ran `.venv/bin/python research/insight_v1/scripts/E6_final_checks.py` on 2026-09-28 (exit 0). Sections [1]-[8] were used for every model number: the REC and ALT totals, bottoms, gifts and kept money; P(top); stock shares; the 53% / -$23k / +$32k same-path figures; $157,736 and 1.73%; 97.4% and 98.1%; the stress, Vanguard-input and history rows; the fees; the (ii)R and 25%-cap books; and the rates-fall rows.

**Check 1: numbers.** Every dollar figure and percentage in the six files was compared with E6 [1]-[8] or the spec (R1-R10, s5.2-5.3, s5.10, s6.1, s7). Numbers outside E6 were traced to their cited sources:
- 78% ALT bottom above $150k: E4 X1.
- About $1k and 48% versus all-Treasury: E3 Q3 / D3 M034.
- $292 per bp and "up to about 600 characters": ticket v1.
- $35k at a 4.0% five-year rate: E4 [4] / X7.
- 3.2%, 13.7% and 40.8%, and $207k / $273k: CLAUDE.md, `strategy_mc.py`.

I recomputed with Python:
- **Share counts:** all 15 at the 9/25 closes, with no mismatch.
- **(ii)R cash:** $3,090 before and $2,990 after fees.
- **Hedge mix and re-solves:** the IEF share is 0.356. The re-solves (VGIT 16.6 / TLH 49.4; SPTI 16.3 / 49.7; IEF 40.9 / TLT 25.1) and the 20%-cap book (about 9.9y) all match.
- **Other figures:**
  - the $150k minimum costs $118,047 at 4.98%;
  - the note costs $72,570 at 95.27 + 1.49;
  - Nov 15 to Jan 1 is 47 days;
  - the IPS blocks sum to 385 words.

The known-and-fixed items were confirmed: the rates-fall ranges $20-23k / $1-7k / minimum $127-137k (now also in `strategy_changes.md`), and the $5,613 = 19bp headroom (every file uses it; $7.7k / 27bp appears only as CLAUDE.md's superseded exact-date figure).

**Check 2: cross-file agreement.**
- **Deadlines:** I converted them with `zoneinfo`:
  - Oct 9, 5 pm ET = Sat Oct 10, 08:00 AEDT;
  - Oct 23, 5 pm ET = Sat Oct 24, 08:00 AEDT;
  - Nov 6, 5 pm ET = Sat Nov 7, 09:00 AEDT;
  - the Oct 20 close = Wed Oct 21, 07:00 AEDT;
  - the Oct 2 open = 23:30 AEST.

  All files agree.
- **Plan terms:** book (ii)R, REC vs ALT, and the three notes (A = TLH, tested; B = the minimum, refined only if logged, otherwise supported; C = VT, supported, with the growth-first story) are the same in all files.
- **Rules:** R1-R10 in `ips_spec.md` match spec s4.

**Check 3: no drafted text.** I read every file in full. There are element lists, checklists and banned-word lists only. There are no notes, reflections, pitch sentences or IPS sentences.

**Check 4: no Final Report content.** I grepped for "Final Report" and "FR". Every hit is a pointer (Works Cited, "numbers go to the Final Report", "the Final Report states the fee assumption"), and each matches the spec's rules. Final Report items appear only in the `open_questions.md` s5 "Later" list, which matches spec s10 plus two one-line additions (M014, Works Cited).

**Check 5: privacy and quotes.**
- **Privacy:** I grepped the six files for privacy terms (family, home, Taipei, co-living, memoir, pronoun, coming out and others) and for D13-restricted phrases ("unstable", "take the jump", "earliest supporters", "gimmick", "risk-adverse", the pull quote, "floor-first", "investment philosophy"). I also read the full `parked.json` text of M017, M020, M072, M145, M217 and M221.
- **Quote ids:** I resolved all 20 Laura ids cited in the six files against `phase_D/D13a_laura_quotes_verified.json`: D13a-N01, B1b-Q11, B8b-Q18/B8a-Q07, B8b-Q38, B8b-Q37, B8b-Q10, B8b-Q21, B8b-Q13, B8b-Q12, B8b-Q31, B8b-Q35, B8a-Q19, B9b-Q09, B8a-Q13, B2b-Q08, B3a-Q04, B8b-Q39, B8a-Q03 and B8b-Q14. All are VERIFIED-PRIMARY, and the quoted fragments are verbatim. No Laura quote is recommended for the notes or the IPS after fix 3.

**Check 6: ticker labels.** I counted the labels and tickers in each file. After fixes 6-9 and 18, every file that names a ticker carries the full PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK label and points to same-type alternates. `securities_and_allocation.md` s1-s2 and s6 list them.

**Check 7: certainty words.** I grepped for "guaranteed", "100%", "matched" / "match", "risk-free", "riskless" and "misses none". Remaining uses are banned-word lists, composition statements ("100% stocks"), MODEL-labelled results that hold by construction (the gift is at or above the bottom in 100% of paths), or "matched" for the real plan's held-to-maturity Treasuries (spec B2(a)). None applies to a fund.

**Check 8: file hygiene.**
- **Required parts:** each file has status labels, a 5-line summary (`securities_and_allocation.md` after fix 10), a "Serves:" line naming TN and/or IPS, and a closing "What this teaches".
- **Scripts:** the scripts the files tell the team to run exist and accept the stated flags (`D9_draft_checker.py --kind pitch|ips|note|reflection`, `D9_ips_page_fit.py --draft`, `A2_curve_recheck.py`, `D9_numbers.py`).

Nothing was committed.

---

## What this teaches

A final check is worth most where files copy numbers from each other. The one stale figure survived because a note said "fixed in three files" when a fourth also needed the fix. The privacy slip hid in a truncated log line that nobody meant as advice. Checking against the script's own output, and not against another file's copy of it, is what caught both.
