# blind_m1_2: second blind build of M1

WS1-second-blind-pricer, 2026-09-30 (Sydney). AI-generated verification code (Claude Code) for Team Caplet;
no deliverable text. Gate A dual computation: built only from `rab/models/M1_METHOD.md` (30 Sep corrected) and
the raw inputs I1-I7 it lists. Nothing in `rab/models/*.py` or elsewhere in `rab/verification/` was read.

## Run

    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/blind_m1_2/blind_m1_2.py

About one second. Deterministic (no stochastic step; seed 20260930 recorded for the run convention).

| File | What |
|---|---|
| `blind_m1_2.py` | Sections A-G in one module; interpretive choices P1-P10 in the docstring |
| `results.json` | Every number, input SHA-256s, `summary` (A6/B6 headline definitions), `flags` (classified) |
| `history_daily.csv` | Section G per day, 1990-01-02 .. 2026-09-28 (9,191 rows) for date-by-date comparison |
| `run_log.txt` | Console summary of the run |

## Headline (A6 / B6 definitions), 28 Sep 2026 curve

- Ten payments, Nov-15 basis: spot V0 $289,119.20; V_A (1 Jan 2027) $292,418; headroom $7,582; break-even
  parallel fall 26.20bp. Exact basis (payment dates; not buyable): V0 $287,016; V_A $290,291; break-even 33.22bp.
- WInS book, `Portfolio` tab at `close_0928`, commissions included: $294,764.50; cash left $5,235.50.
  Cash margin (B5): cost reaches $300k after a 27.64bp parallel fall; cash under $1,000 after 22.41bp.
- Book L at `sheet_as_read`: $292,418.81 incl. $175 commissions (Sheet shows cash left $7,581: agrees).

## Internal checks that passed

- All ten Book L discount factors in the Sheet's display reproduced to 6 decimals.
- Section G value on D equals section A to the cent (same curve, two code paths).
- B4 spec rule reproduces every `Portfolio` and `Book L` quantity at `sheet_as_read` prices.
- IBTO, IBTP, IBTQ look-through NAV within 0.03-0.07% of published NAV.

## Flags (see `results.json["flags"]` for evidence pointers)

- F1 fix-before-6-Nov: T 4.500% 15-May-2038 recorded accrued 0.530 is inconsistent with a May/Nov cycle
  (model 1.663); about $215 of hidden cost and a misleading "+6bp" status.
- F2 note: the Sheet's +13/+14/+15bp status texts are not reproduced on 28 Sep (or 25 Sep); all five book bonds
  still pass the 25bp test.
- F3 note: both 29 Sep "stale" prices confirmed stale (-111bp, -92bp); IBTR holds the Feb-2036 bond at a
  curve-implied dirty 95.20 vs WInS 102.95.
- F4 ignore: IBTM/IBTR look-through shift is a share-count timing artefact; their YTM gaps are +1.6/+0.3bp.
- F5 note: Book L rule ignores the 7bp fee and the maturity-to-1-Jan wait; iBond rungs about $40-100 under,
  Treasury rungs $700-2,700 over in the curve scenario; $447k of $500k at 0% reinvestment.
- F6 ignore: half-cent ties in the Nasdaq closes for IBTM/IBTR.

Known limits: model prices, one curve, one day; WInS settlement, bond unit and accrued conventions UNVERIFIED.
