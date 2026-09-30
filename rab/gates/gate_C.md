# Gate C (trade kit): PASS for the kit; the live Sheet tabs are out of date (fix before Friday)

WS6-gateC, RAB Kit, 30 Sep 2026 (Sydney). This is an AI-generated check (Claude Code) for Team Caplet. Nothing was run
against WInS and no order was placed. The IPS, the Sheet and `numbers.yaml` were not edited. The Sheet was only read.

## Current run (third run, on kit commit cc887b3 plus this commit)

- **Result:** 413 checks: **0 FAIL**, 18 UNVERIFIED (WInS name strings), 16 CONDITIONAL (open item 3).
  `numbers.yaml` sha256 `492ed3203958...` matches `rab/numbers.lock` and `/Users/ray/Research/rab-kit`.
- **New check G7, the Sheet mirror (46 PASS):** the team reads the kit through the Sheet tabs 'RAB Tickets' and
  'RAB Notes'. The committed mirrors of those tabs (`rab/sheets/rab_tickets.csv`, `rab_notes.csv`) now have to carry
  the same orders, quantities, prices, max prices and Preview totals as `tickets.csv`, and the same exemplar text as
  `notes.csv`, with no retired note left in. G6 now also scans both mirrors for stale facts. `--self-test` breaks the kit
  10 ways, adding a mirror that has drifted, and catches all 10.
- **The kit rebuilds byte-identical.** `refresh_tickets.py` passes 83 of 83. `build_notes.py` reports 0 fail.
  `build_sheet_tabs.py` and `note_check.py --self-test` pass. `git status` shows no change to any kit file.
- **The live Sheet is out of date (open item 7, non-trivial).** I read the tabs read-only with the Sheets connector on
  30 Sep. They still hold the 0141438 build from before the second judge panel:
  - 'RAB Tickets': the Feb-2037 bond's max price is **97.940** in both books (rows 19 and 30, column O). The kit's
    value is 97.919, the top of the 25bp band. At 97.940, stop rule 3's two tests disagree, which a judge flagged.
  - 'RAB Notes': **26 exemplars differ** from `notes.csv`. One example is the IBTR note, which still reads "under her
    $300,000 deposit at latest yields"; the judges flagged that wording. Retired **T40c** is still listed, and **IBTR_F,
    IBTM_R, T40s and SW37 are missing**. I made the comparison against the mirror that 0141438 wrote, which had been
    read back and verified, and spot-checked it against the live read (IBTR text, T37 max price).
  - I did not fix this here. Writing to the team's shared Sheet is not a trivial in-place fix for a checker. The
    local mirror is already correct.

| Check (task item) | What was tested | Result |
|---|---|---|
| G1 length (1) | 23 exemplars: each at most 300 characters (the WInS box) and at most 285 (the kit's margin). Also checked: the count column is right, the text is plain ASCII in one paragraph, and it matches notes.md. The 6 TN reflection outlines must each stay at or under 100 words | 75 PASS. Longest note 285 characters; longest outline 60 words |
| G2 names (2) | Every ticket and conditional-note security has an expected name that fits. An iBonds "Dec YYYY" name must end in the right year. A bond name must give the coupon and maturity, and its CUSIP must be in MSPD. IBTN / INSCORP never appears. The SEEN names (IBTM, VT) must equal tab WInS Notes | 26 PASS, 18 UNVERIFIED (open item 1) |
| G3 cash (3) | Start at $300,000. Cost = quantity x price (for bonds, clean price + accrued, per $100) + $25 per ETF or $10 per bond. Only whole units; every ETF priced at $3 or more. Cash must stay above zero in the locked, Preview and worst cases. Totals must equal numbers.yaml. No more than 200 trades | 27 PASS. Portfolio book: $294,764.50 including $200 of commissions, $5,235.50 cash left, lowest worst-case cash $2,445. Book L: $292,580.89 including $175, $7,419.11 left, lowest $4,518 |
| G4 volume (4) | ETFs: quantity at most 2 x the 30-session average volume (official rule) and at most half of the quietest day in 20 sessions (WInS FAQ). Bonds: WInS shows no bond volume, so a split plan has to exist | 21 PASS. Largest ETF order is 1.2% of the 2x limit. Bond split plan is in `M9_selection.md` |
| G5 traceability (5) | Every ticket field equals numbers.yaml or a committed dated file, or is worked out again here. Every cent figure in tickets.md traces. Every digit and every number word in the exemplars traces to a case fact, a security term, a numbers.yaml key or a derivation shown in the check | 165 PASS, 16 CONDITIONAL (open item 3) |
| G6 stale facts (6) | Search for 100,000 / $100k / Dec 4 / 500k / $0 commission / "no Treasuries", and for TLH / IEF / VGSH as the current book, in every kit .md and .csv and both Sheet mirrors. In code, a hit is allowed only inside a banned-pattern list | 18 PASS: no hits |
| G7 Sheet mirror | The rab/sheets mirrors match tickets.csv and notes.csv row by row | 46 PASS (the live tabs do not match: open item 7) |

## Open items (the strategy is unchanged)

| # | Item | Class | Evidence / action |
|---|---|---|---|
| 1 | The exact WInS name strings are not yet recorded for IBTR, IBTQ, IBTP, IBTO or the five bonds. Only IBTM and VT were SEEN (29 Sep). | fix-before-6-Nov (Friday 2 Oct, before order 1) | `friday_checklist.md` step 3 copies each name and types IBTN once; it should show INSCORP Inc. Each ticket's rule 1 says the name on screen must match, or the order is not placed |
| 2 | The 2x-volume rule cannot be worked out for bonds, because WInS shows no bond volume. The orders are tiny: $17k-$30k of face value against $16.6bn-$44.6bn outstanding (MSPD). | note-in-Final-Report (only if WInS rejects an order) | Split plan in `M9_selection.md`: if an order is still waiting at 3:30pm ET, cancel it and place half in each of the next two sessions |
| 3 | 16 claims hold only in the case their note is written for: T40b, T40s and T37 (what the drop-down shows); SW40, SW41, SW37, OD_S and OD_B (the price passes); IBTR_F (the test fails); IBTM_R (the backstop sentence is adopted on 1 Oct); IBTP (the premium is re-run on the trade date); OB_S (trigger B); OC (trigger C). | ignore (by design) | `notes.md` s5 and `friday_checklist.md` say which note is typed. Full list in `gate_C_results.json` |
| 4 | The IBTR test and the OB_S trigger use the 28 Sep curve (about $292,000; a fall of about a quarter of a percentage point). | fix-before-6-Nov (already planned) | Friday re-lock of `laura.ladder.cost_2027_strips` and `breakeven_fall_bp_strips`. If the cost is above $300,000, the team trades `--split-from-curve` and types IBTR_F |
| 5 | The tickets' 30-session volume `adv30` is not in numbers.yaml. It comes from the committed, dated `rab/data/etf/etf_summary_2026-09-28.csv`, which was re-read to the share. | note (WS1 request in `notes.md` s7) | Add `adv30` at the Friday re-lock |
| 6 | The Sheet tab Book L shows its own curve gaps: "+13bp" for Nov-2039 and "about 85bp off" for Feb-2038. M1 gives -6.6bp and -92.1bp. The tickets and notes use M1 only. | note-in-Final-Report (Sheet labels only) | `rab/data/sheet/Book_L_values_2026-09-30T0033AEST.txt` against `wins.bond_check.*` |
| 7 | **The live Sheet tabs 'RAB Tickets' and 'RAB Notes' are out of date:** T37 max price 97.940 against 97.919; 26 changed exemplars; T40c still listed; IBTR_F, IBTM_R, T40s and SW37 missing. The team works from these tabs on Friday. | **fix-before-6-Nov (before Friday 2 Oct)** | Ray (or WS6-sheets) re-runs `rab/sheets/build_sheet_tabs.py` and writes `rab_tickets.json` / `rab_notes.json` to the two tabs, then reads them back. The 'Team note' column (M) must be kept if students have typed in it. Until then, use `tickets.md` / `notes.md` |

These items were already known and fall outside this check. The Sheet records 0.530 as the May-2038 bond's accrued
interest (`tickets.csv` `accrued_rec`; the kit trades on 1.712 for 2 Oct). The IPS says "needs no rebalancing". Both
are fix-before-6-Nov, as recorded at Gate A.

A local file, `rab/trades/out/tickets_2026-09-28_friday_rule_Portfolio.csv`, is left over from a test run and is marked
"WInS, typed by test". It is gitignored and never reaches the team; ignore it.

## History

- **First run (e3aef25):** 336 checks, 0 FAIL, 18 UNVERIFIED, 8 CONDITIONAL; self-test 8 of 8. No kit fixes; the
  checker was matched to the kit's stated rules (accrued to 5 Oct for the worst case, the 20-day median keeps its .5,
  MSPD coupons without decimals, a rounding allowance of $0.16 or less per bond ticket for the 3-decimal max price).
- **Second run (cc887b3, after the second judge panel):** 365 checks, 0 FAIL, 18 UNVERIFIED, 16 CONDITIONAL; self-test
  9 of 9. One kit fix: bond max price capped at the band top (T37 97.940 -> 97.919). Ticket totals unchanged.
- **Third run (this commit):** added G7 and the Sheet-mirror stale scan; read the live tabs; found open item 7.

Run from the worktree root:

```
/Users/ray/Research/rab-ws/.venv/bin/python rab/trades/check_gate_c.py              # exit 0 = no FAIL
/Users/ray/Research/rab-ws/.venv/bin/python rab/trades/check_gate_c.py --self-test  # 10 broken kits, all caught
```

Run it again after Friday's re-lock, the refreshed tickets and the Sheet rewrite.
