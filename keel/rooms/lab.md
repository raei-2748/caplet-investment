# FICTION (the room) + real work (the experiments). The Lab: lab book

> Room card: `../OFFICE.md`. Head: Jun. Kai roasts every idea before it is tested. Agents: `scenario-modeller`,
> `numbers-auditor`. Bench (existing models): `../scripts/`, `../library/ips_numbers_2026-10/ips_numbers.py`,
> `../library/verified_2026-09-27/`. The older Final Report evidence lab (Ray's Mac): `../routines/claude_lab/`.

## What counts as a win
An elegant, interpretable model a judge can follow, or an idea Kai roasted that the test proves right. Either way it
only leaves the Lab if it passes all four doors: Felix's rules check (Window), a judging criterion it serves, the
Archive's spine (no clash with anything locked), and a Caplet student choosing it (`../OFFICE.md` house rule 2).

## Steps for every experiment
1. **Hypothesis**: one sentence that can be wrong.
2. **Kai's roast**: written before the test, so a later win over it is visible.
3. **Test**: the script, inputs and data dates; what result would prove the hypothesis wrong.
4. **Result**: numbers dated, with basis, labelled MODEL; `numbers-auditor` re-derives the headline number.
5. **Verdict**: ADOPT, PARK or BIN, with one line why. Binned experiments stay in the book: "we tried this and here is
   why it didn't work" is evidence of learning.

## Rules
- **Quiet period until Sat 7 Nov 09:00 Sydney:** only experiments that bear on the IPS, run on existing scripts and
  data. Any other experiment is queued as "waits for OK" until Ray approves it or the period ends.
- At most one experiment moves one step per daily run. One page per write-up in `lab/L-NN_slug.md`.
- Log a LEDGER row (`../office/LEDGER.md`) when a result informs a Caplet decision.

## The book
| # | Hypothesis | Kai's roast | Test | Criterion | Status | Verdict |
|---|---|---|---|---|---|---|
| L-01 | A one-line rule ("the cost of Laura's ten payments moves about $290 for every 0.01% move in yields", DV01 $289/bp on the 25 Sep 2026 curve, `CLAUDE.md` key facts) predicts the cost on every 2026 close within $1,500 | "One number for a curve that twists? The short end and the long end don't move together." | `../scripts/ladder_history.py` on every close since 24 Sep; compare the rule's prediction with the full repricing; wrong if any day misses by more than $1,500 | Portfolio Analysis; Creativity & Presentation | done 24 Oct ([L-01](lab/L-01_one_dial.md)): worst miss $652 over 20 closes | ADOPT (for explaining) |
| L-02 | Keeping a small, named buffer from the 2028 deposit covers the coupon-reinvestment gap (about $21k if yields fall two points for good, `../library/ips_numbers_2026-10/IPS_number_sheet.md` section 3) at a cost to the 2031 range a co-sponsor would accept | "So the safe plan needs a safety net for its safety net?" | Reuse the reinvestment case in `../library/ips_numbers_2026-10/ips_numbers.py`; no new model; wrong if the buffer that covers the gap costs more than the range can bear | Investment Strategy; Client Knowledge | done 24 Oct ([L-02](lab/L-02_buffer.md)): $10k -> 2.9%, $15k -> 1.3% of paths short | ADOPT as option D1-c |
