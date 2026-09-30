# Gate C (trade kit): PASS, with 3 items the team settles on the WInS screen on Friday

WS6-gateC, RAB Kit, 30 Sep 2026 (Sydney). AI-generated check (Claude Code) for Team Caplet. Nothing was run
against WInS, no order was placed, and the IPS, the Sheet and `numbers.yaml` were not touched.

## Re-run after the second judge panel (30 Sep, WS6-revise): still PASS

- **Result:** 365 checks: **0 FAIL**, 18 UNVERIFIED (the same WInS name strings), 16 CONDITIONAL (each named in
  open item 3 below). 23 exemplars (T40c retired; IBTR_F, IBTM_R, T40s and SW37 added), longest 285 characters;
  outlines 60 words or fewer.
- **Checker updated to the new texts, not loosened:** the claim list was rebuilt so every number word in the rewritten
  notes sits inside a derivation (for example "cover most of that payment" = `reinvest.rung.T_4.375%_15-Nov-2039`
  at_0pct 85.9% of $50,000; "about seven and a half months" = 231 days; "three months less" = 89 days). The outline
  count now reads headers that carry the shared-sentence total, and "2 Oct" (the Friday trade date) is an allowed
  date. `--self-test` now breaks the kit 9 ways (adds an untraced word quantity, "a third of a percentage point") and
  catches all 9.
- **One kit fix (a judge found it):** the Feb-2037 bond's max price (97.940) sat above the top of its 25bp band
  (97.919), so stop rule 3's two tests disagreed. `refresh_tickets.py` now caps a bond's max price at the band top and
  floors its min price at the band bottom. Ticket totals are unchanged ($294,764.50 and $292,580.89); lowest
  worst-case cash is now $2,445.28 (Portfolio) and $4,518.06 (Book L). 83 of 83 ticket checks pass.
- **Open item 3 now lists 16 conditional claims:** T40b, T40s, T37 (drop-down cases), SW40, SW41, SW37, OD_S, OD_B
  (price passes), IBTR_F (test fails), IBTM_R (backstop sentence adopted), IBTP (trade-date premium re-run), OB_S,
  OC (October triggers). **Open item 4:** a failed IBTR test no longer means "stop": the team trades the
  `--split-from-curve` ticket and types IBTR_F (`friday_checklist.md`).

## First run (WS6-gateC, 30 Sep)

- **Checker:** `rab/trades/check_gate_c.py` (standard library + PyYAML, no network). It does not trust
  `refresh_tickets.py` or `build_notes.py`. It works every number out again from the committed inputs: `numbers.yaml`,
  the Sheet and WInS snapshots in `rab/data/sheet/`, the ETF volume file `rab/data/etf/etf_summary_2026-09-28.csv`,
  MSPD Table V (31 Aug 2026), the iShares iBonds list (30 Sep) and the M9 screen.
- **Result:** 336 checks: **0 FAIL**, 18 UNVERIFIED (WInS name strings not yet copied from the screen), 8 CONDITIONAL
  (claims that hold only in the case the note is written for). Full list in `rab/gates/gate_C_results.json`.
- **The checker catches real errors:** `check_gate_c.py --self-test` breaks a copy of the kit 8 ways (a 301-character
  note, IBTN as a ticket, 3x the daily volume, an untraced 12%, "eight weeks", the wrong ordinal payment, "Dec 4", TLH as
  the book). It catches all 8.
- **The kit's own checks still pass and give the same files:** `refresh_tickets.py` passes 83 of 83,
  `note_check.py --self-test` passes, `build_notes.py` reports 0 fail, and rebuilding leaves `tickets.csv`,
  `tickets.md`, `notes.csv` and `notes.md` byte-identical.
- **Numbers file:** `numbers.yaml` sha256 `492ed3203958...` matches `rab/numbers.lock` and `/Users/ray/Research/rab-kit`.

| Check (task item) | What was tested | Result |
|---|---|---|
| G1 length (1) | 20 exemplars: each at most 300 characters (the WInS box) and at most 285 (the kit's margin); the character count is right; plain ASCII; one paragraph; the same text as in notes.md. Also the 6 reflection outlines, which must stay at or under 100 words | 66 PASS. Longest note 285 characters; longest outline 70 words |
| G2 names (2) | Every ticket and conditional-note security has an expected name that fits it: an iBonds "Dec YYYY" name ends in the right year, and a bond name gives the coupon and maturity, with its CUSIP found in MSPD. IBTN / INSCORP never appears. The SEEN names (IBTM, VT) equal the tab WInS Notes | 26 PASS, 18 UNVERIFIED (see open item 1) |
| G3 cash (3) | Starting from $300,000: cost = quantity x price (bonds: clean + accrued, per $100) + $25 per ETF / $10 per bond. Whole units only; ETF price at least $3. Cash stays above zero in all three cases (locked, Preview, worst). Totals equal numbers.yaml. At most 200 trades | 27 PASS. Portfolio book: $294,764.50 incl. $200 commissions, $5,235.50 cash left, lowest worst-case cash $2,441. Book L: $292,580.89 incl. $175, $7,419.11 left, lowest $4,512. At most 16 trades planned (11 now + 5 in October) |
| G4 volume (4) | ETFs: quantity at most 2 x the 30-session average volume (official rule) and at most half of the quietest day in 20 sessions (WInS FAQ). Bonds: WInS shows no bond volume, so a split plan has to exist | 21 PASS. Largest ETF order: 1.2% of the 2x limit (IBTM 4,486 shares); IBTR in Book L is 16% of its quietest day. Bonds: split plan in `M9_selection.md` (see open item 2) |
| G5 traceability (5) | Every ticket field equals numbers.yaml, a committed dated file, or is worked out here (bond accrued interest on 2 Oct and 5 Oct, actual/actual; price bands; running cash). Every figure in tickets.md traces. Every digit and every number word in the 20 exemplars traces to a case fact, a real coupon or maturity (MSPD / iShares), a numbers.yaml key, or a derivation shown in the check (for example "about seven weeks" = 47 days; "about a quarter of a percentage point" = 26.2bp; "almost exactly the value" = 0.06% premium; "about the same cost" = $23,146 against $23,266, from M9) | 153 PASS, 8 CONDITIONAL (open item 3); 154 of 154 cent figures in tickets.md trace |
| G6 stale facts (6) | Search for 100,000 / $100k / Dec 4 / 500k / $0 commission / "no Treasuries" and for TLH / IEF / VGSH as the current book, across every kit .md and .csv. In code, a hit is allowed only inside a list of banned patterns | 16 PASS: no hits |

## Fixes made

None were needed in the kit. The only changes were to the new checker, to match the kit's stated rules:

- the worst case uses accrued interest to 5 Oct;
- a 20-day median keeps its .5, where numbers.yaml rounds it;
- MSPD gives coupons such as "5" and "2" without decimals;
- a bond's maximum clean price is shown to 3 decimals, so a rounding allowance of up to $0.16 per bond ticket is allowed.

## Open items (the strategy is unchanged)

| # | Item | Class | Evidence / action |
|---|---|---|---|
| 1 | The exact WInS name strings are **not yet recorded** for IBTR, IBTQ, IBTP and IBTO or for the five bonds. The kit carries the issuer's name and the coupon and maturity, and marks each one UNVERIFIED. Only IBTM and VT were SEEN (29 Sep). This cannot be closed offline, because it needs the WInS screen. | fix-before-6-Nov (on Friday 2 Oct, before order 1) | `friday_checklist.md` step 3 copies each iBonds name and types IBTN once (it should show INSCORP Inc). The bond drop-down read records the bond strings. Each ticket's rule 1: the name on screen must match, or the order is not placed |
| 2 | The 2x-volume rule **cannot be computed for bonds**, because WInS shows no bond volume. The orders are tiny: $16k-$30k of face value against $16.6bn-$44.6bn outstanding (MSPD). | note-in-Final-Report (only if WInS rejects an order) | Split plan in `M9_selection.md`: if an order is still waiting at 3:30pm ET, cancel it and place half in each of the next two sessions |
| 3 | 8 claims hold **only in their use case**. T40b: "WInS does not list one". T40c: "WInS also lists a 1.375% bond". SW40, SW41, OD_B: "price passed our curve check". OB_S: trigger B (cost above $300,000). OC: trigger C (cash above $6,300 = $3,300 float + $3,000). | ignore (by design) | `notes.md` s5 says when each note is used. Friday's refresh and drop-down read decide which one is typed |
| 4 | The IBTR note's result ("under her $300,000 deposit", "about a quarter of a percentage point") is on the 28 Sep curve. | fix-before-6-Nov (already planned) | Re-lock `laura.ladder.cost_2027_strips` and `breakeven_fall_bp_strips` on Friday's curve. If the cost is above $300,000, stop and tell Ray (`notes.md` IBTR brief) |
| 5 | The tickets' 30-session volume `adv30` is not in numbers.yaml. It comes from the committed, dated `rab/data/etf/etf_summary_2026-09-28.csv` and was re-read to the share. | note (WS1 request 7 in `notes.md` s7) | Add `adv30` to `market.etf_2026-09-28` at the Friday re-lock |
| 6 | The Sheet tab Book L shows its own curve gaps (for example "+13bp" for the Nov-2039 bond and "about 85bp off" for Feb-2038). numbers.yaml's M1 check gives -6.6bp and -92.1bp. The tickets and notes use M1 only. | note-in-Final-Report (Sheet labels only) | `rab/data/sheet/Book_L_values_2026-09-30T0033AEST.txt` against `wins.bond_check.*` |

These items were already known and are outside this check: the Sheet's accrued interest of 0.530 on the May-2038 bond,
and the IPS wording "needs no rebalancing" (both fix-before-6-Nov, as recorded at Gate A).

Run from the worktree root:

```
/Users/ray/Research/rab-ws/.venv/bin/python rab/trades/check_gate_c.py              # exit 0 = no FAIL
/Users/ray/Research/rab-ws/.venv/bin/python rab/trades/check_gate_c.py --self-test  # 8 broken kits, all caught
```

After Friday's re-lock and the refreshed tickets, run it again. If the re-lock moves a headline number, the IBTR claim
check will pick it up.
