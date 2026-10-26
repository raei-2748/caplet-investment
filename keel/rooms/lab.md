# FICTION (the room) + real work (the experiments). The Genius Lab: lab book

## Now
- **Doing:** Testing whether the dedicated ladder belongs in the IPS
- **Decided:** Dedicated ladder halves the coupon-reinvestment tail (p95 $25.1k to $14.8k) for about $1,486 more (MODEL, 15 Oct curve); default: no WInS trades
- **Next:** Aha hunt (project P03): three candidate insights, roasted and tested; the strongest goes to Draft 2
- **For the judges:** IPS: a risk the plan names and fixes, with the number behind it
- **Updated:** 2026-10-26 13:40 Sydney


> **State (Mon 26 Oct 2026, 13:40 run).** L-01 ADOPT, L-02 ADOPT (D1-c), L-03 PARK, L-04 ADOPT (Final Report),
> L-05 ADOPT C1-C3, L-06 name packages, L-07 ADOPT, L-08 ADOPT (Extended Reserve option). The IPS is now a from-scratch
> rewrite (`../ips_rewrite/`): rooms take WORK_ORDERS first and write to its inbox, never to v4. Today: L-09 = WO-R1 done
> (dedicated ladder halves the coupon tail in 200,000 paths, p95 $25.1k -> $14.8k, +$1,486; MODEL 15 Oct). Next best
> move: whatever WO-R2 (Courtroom) leaves open, else lift C&P on the rewrite's Draft 1 (Fri 30 Oct).

> Room card: `../OFFICE.md`. Head: Jun. Kai roasts every idea before it is tested. Agents: `scenario-modeller`,
> `numbers-auditor`. Bench (existing models): `../scripts/`, `../library/ips_numbers_2026-10/ips_numbers.py`,
> `../library/verified_2026-09-27/`. The older Final Report evidence lab (Ray's Mac): `../routines/claude_lab/`.

## Charter: the Genius Lab (Ray, 24 Oct 2026)
Ray renamed the Lab "Genius Lab" and gave it one brief: **be as creative as possible: unexpected connections,
distinctive voice, and everything we have talked about** (`../NORTH_STARS.md`, including his 24 Oct refinements).
How the room reads that:
1. **Hunt where nobody else looks.** If a chatbot gets there in ten seconds, it isn't ours. Before an idea is roasted,
   check it against the binned list below and the cold naming test (`../meetings/2026-10-24_after-root-and-branch.md`).
2. **Creativity is the point; truth is the price of entry.** A link still has to map a real mechanism of Laura's
   plan, rest on the case or a checked fact, and serve a judging criterion. The cleverest idea that is false loses to
   a plain one that is true (L-05: the water image died on one broken mapping).
3. **Voice is part of the result.** A Genius Lab output ends in words a person would say out loud, cut the way Ray
   cuts (whole ideas, not squeezed sentences; `../VOICE.md`, "Ray's own essay voice"). Subtle beats eloquent.
4. **Kai still roasts first and failures stay in the book.** Hypothesis, roast, test, result, verdict. A roasted
   idea that wins is the room's favourite kind of result.
5. **Ourselves first.** Ray: everyone optimises for the client; we optimise for a team only Caplet could be, then
   check it fits Laura.

**Binned, do not re-propose:** roots, trees, branches, seeds, gardens; keel and sail, ballast and sail; ladders or rungs
as a name; floor and fund; secure first, grow later; comic panels, ink, storyboards, pencil, pages, drafts or manuscripts as the plan's image (cold test round 2, 25 Oct); coupons as "a dose, not a leak" (L-09 panel: AI template, false); NSW water licences; Firm Yield,
General Security, Dry-Year Rules, Opening Allocation; "defeasance" as an IPS word (Final Report only).

## What counts as a win
An elegant, interpretable model a judge can follow, or an idea Kai roasted that the test proves right. Either way it
only leaves the Genius Lab if it passes all four doors: Felix's rules check (Window), a judging criterion it serves, the
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
| L-03 | Amara's print run (Library fixes applied) maps M1-M11 well enough to be the master motif | "Show me VT in a print shop. Nothing in a warehouse grows." | Rate M1-M11 TRUE/STRETCH/NONE; master only if M2, M3, M8 TRUE, at least 7 TRUE, and VT has an honest image; plus press-day vs reprint size check (`../scripts/ladder_pv.py`, `lab/L-02_results_22oct.json`) | IS; PA; CP | done 24 Oct ([L-03](lab/L-03_print_run_map.md)): 5 TRUE, 5 STRETCH, 1 NONE; per lasting 1-point fall +$31,361 press day vs $10,836 reprints (22 Oct, MODEL) | PARK: risk image for Monday, not the master motif |
| L-04 | A payment shortfall (yields fall for good) and a cost overrun (fast inflation 2031-33) seldom arrive together | "2022. Inflation and bond losses in the same year." | `lab/L-04_two_risks_run.py` on Shiller GS10 + CPI 1871-2025; wrong if joint rate >= independence | IS; CK; case :146-147 | done 24 Oct ([L-04](lab/L-04_two_risks.md)): 1954-2011 joint 8.6% vs 16.3% if independent; 1871-2011 5.0% vs 6.8% (HISTORY) | ADOPT for the Final Report; BIN for the IPS (no citations) |
| L-05 | A three-rung ladder aimed at the IPS's weakest asks finds 3+ lines that survive the Courtroom and score better | "Three survive, none of them the clever one." | Haiku x2 -> Sonnet (re-priced) -> Opus; Library; Courtroom + 5 mock judges; Laura's Room; Writing Room | IS; PA; CK; HC "define certainty"; reserve composition | done 24 Oct ([L-05](lab/L-05_ips_push.md)): 10 candidates, 3 survive amended; judges 25.2 -> 26.4/40 | ADOPT C1-C3 into IPS v3; Kai won his bet |
| L-06 | One name + at most two motif touches + one closing line lift CP above v3 without costing IS or CK | "You'll bolt a pun onto a sound IPS. Judges can smell a garnish." | Three packages on v3; Kai + five mock judges score v3 and each; memory test | CP; CK; IS | done 24 Oct ([L-06](lab/L-06_creativity.md)): CP 5.0 -> Press Day 6.2, Caplet XR 7.0, Pre-Registered 6.4; IS level | ADOPT all three as options for Monday's Long Room (Courtroom leans Pre-Registered; Kai dissents for Caplet XR) |
| L-07 | One true investing line about the plan, said plainly, is what a judge remembers (not a name) | "Forty lunch lines from Haiku and you'll keep the one a textbook already has." | Rung 1 Haiku (40 lines, 20 far mappings), rung 2 Sonnet re-priced on the 22 Oct close (`lab/L-07_lunch_line/r2.py`); Courtroom memory test on v4 | IS; PA; CK | done 25 Oct ([rung 2](lab/L-07_lunch_line/rung2.md)): the fund is the floor ETF's interest taken up front ($32,064 of $150,000, MODEL); v3.1's "any rise stays with Laura" overclaimed (fixed); rung 3 not needed | ADOPT into IPS v4 (both). Kai half-won: it *is* textbook (a bond floor), but it was the only investing idea judges recalled |
| L-08 | XR has a true second reading, from a word the case uses, that lifts C&P as one line without reading as AI | "Backronyms are what a chatbot does in ten seconds. If you find a real one it'll be ex-rights." | Rung 2 Sonnet (10 meanings, real conventions first); rung 3 Opus cold panel of three judges on A-E | CP; CK | done 25 Oct ([L-08](lab/L-08_xr_second_layer.md)): A Extended Reserve +1/+1/+1; B, C negative; D doses +1/+2/-1 | ADOPT A as a Package B option; PARK D for the Final Report; BIN B, C. Kai half-won (ex-rights died) |
| L-09 | Sizing the ladder from 2042 backwards (R01 B3, every holding >= $10k) cuts the coupon tail p95/p99 by a third or more in the 200,000 paths, for under $2k | "You've moved the leak, not plugged it; the tail barely moves once rates wander." | `../ips_rewrite/lab/R01_mc.py`, same paths and seed as the number sheet; audit vs R01 and number sheet; cold panel (Sonnet) on three explaining lines | IS; PA; CP | done 26 Oct ([L-09](lab/L-09_dedicated_ladder.md)): p95 $25,112 -> $14,832, p99 $32,429 -> $17,584, +$1,486; WInS would need ~10 trades, ~$52k each way; dose/leak line binned | ADOPT as a rewrite option (WO-R2 + Caplet decide). Kai half-won: the risk now sits in $85k of pre-2033 coupons |
