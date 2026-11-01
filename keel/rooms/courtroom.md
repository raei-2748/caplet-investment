# FICTION (the room and the simulated parties) + real arguments. The Courtroom

## Now
- **Doing:** Put V50 (the rebuild after Ahaan's Book 11) on trial: C-05, huddle H-013
- **Decided:** AMENDED. Repair PROMOTED 4-0: the ending finally says what crushing is ("Crushing one means selling it before its January, even for the building."), and "opened" became "redeemed". Both blind readers picked it, narrowly. Six truth fixes went to the rewrite inbox, paid by three repeated lines
- **Next:** the Window gates the fixes (Mon 08:40); the Writing Room drafts one plain diversification sentence; P04 on the next full draft
- **For the judges:** the capsule's warning at the start and its payoff at the end now mean one thing a reader can say back; two lines both blind readers couldn't follow are rewritten in plain words
- **Updated:** 2026-11-01 19:30 Sydney


> **State (Sun 1 Nov 19:30 AEDT).** Last trial: C-05 V50 on trial (AMENDED; repair + T1-T7 to the inbox). Files
> `courtroom/C-05_*` (case, blind-sheet builder), huddle H-013 (blind sheet, vote note, the bench's Commandments check on
> V50R). Next: P04 on the next full draft; whether D6 (gap set aside before naming) returns once T6 is said plainly.

> Room card: `../OFFICE.md`. Kai prosecutes (`devils-advocate`); Nora presides and runs the mock judges
> (`mock-judge`, workflow `office-judge-panel`). Pre-mortems: `../pm/PREMORTEMS.md`.

## Who appears here
- **Team Spinnaker (simulated rival).** In the story Spinnaker is a rival team from another school (`../STORY_BIBLE.md`,
  PR #23); in the Courtroom, Kai plays them. All sail, no keel: they argue for putting Laura's money mostly in stocks and
  trusting the long run. Their case is built only from real evidence (the J.P. Morgan 2026 LTCMA figures in
  `CLAUDE.md`, the team's own growth-first runs in `../library/verified_2026-09-27/strategy_mc.py`). Keel must beat
  their best argument, not a straw man.
- **The devil's advocate (Kai).** The strongest honest case against one rule or one sentence.
- **Five mock judges** (faculty, practitioner, former finalist, outsider, finance undergraduate;
  `.claude/agents/mock-judge.md`). They score against the official criteria and never rewrite. They sit only after
  Caplet's own scorers have marked the draft (`../office/CHARTER.md` section 6).

## Rules
- A case is one claim, one charge and one verdict: UPHELD (the claim stands), AMENDED (change named), or STRUCK.
- Simulated parties are tests, never quotes. Nothing they say goes into a deliverable.
- Quiet period until Sat 7 Nov 09:00 Sydney: trials of the IPS draft and the plan only.

## Docket (newest at the bottom)
| Date | Claim on trial | Charge (who) | Verdict | What changes |
|---|---|---|---|---|
| Sat 24 Oct | Draft (Tab 15 export, `caplet/google_drive/ips_report/15_tab_15.md:20`): "Any payment shortfall is covered first by the 2027 leftover, then the half Laura keeps, then the contribution above the floor." | Kai: the first link is empty (ladder $298,861-$302,139 on 22 Oct, MODEL) and the chain stops before the floor, so the payments have no last resort in ~9% of paths | AMENDED | Vote D3 (drop the leftover link) and D1 option d (floor as last resort) in `../office/outbox/2026-10-24_SD-T04_strategy_vote-set-B-options.md` |
| Sat 24 Oct | Draft lines 16, 18, 20: the half Laura keeps is a cost cushion, her "defense" against inflation and a stronger Taiwan dollar, and payment back-up number two | Kai: one pot (p50 $26k, p5 $11k in 2033, MODEL) booked three times, and all three jobs get worse in the same bad year | AMENDED | Vote D5: one ranked sentence (payments first) |
| Sat 24 Oct | Draft line 16: "A range built to hold protects her credibility better than a narrower one she might miss." | Kai: the case wants a range plus a confidence; the draft gives no confidence | UPHELD (Nora, after Felix read R7: the final range and its confidence are not expected in the IPS) | The confidence goes in the Final Report; noted for T10 |
| Sat 24 Oct | The plan itself (Spinnaker, played by Kai): ~90% Treasuries forgoes ~3 points a year (J.P. Morgan 2026: AC World 7.00% vs U.S. intermediate Treasuries 4.00%) on money not needed until 2033 | Spinnaker's best case, from real evidence only | UPHELD (the plan stands) | Answer: growth-first missed a payment in 3.2% of the team's own modelled paths (13.7% if the 2028 deposit is $75k), and the plan keeps all equity upside above the floor (`../library/verified_2026-09-27/strategy_mc.py`, 27 Sep runs) |

| Sat 24 Oct (evening) | Lab L-05 candidates C1-C10 for the IPS (`lab/L-05_ips_push/CANDIDATES.md`) | Kai: wrong word ("defeasance": ETFs pay a NAV), overclaim ("never shrink", "no forecast"), dodging the case ("confidence it falls within"), no citation possible (L-04), wrong against the draft (C8), a mapping that breaks and Caplet's world not Laura's (water) | 3 AMENDED, 7 STRUCK | C1-C3 into IPS v3; C5, C6 to the Final Report (`lab/L-05_ips_push/courtroom.md`) |
| Sat 24 Oct (evening) | The C1-C3 package (Spinnaker, played by Kai): admits ~90% sits at ~5% for 15 years and names two leaks | Spinnaker's best case | UPHELD (the package is more defensible) | Two blows land: with ~$1.1k headroom "lowers the floor" is the expected case, so Caplet should own it; keep the one-issuer line on purpose |
| Sun 25 Oct (evening) | D1 lean: $10k buffer from the 2028 deposit + payments before the floor; Laura's Room exhibit 0.75% -> 0.11% | Kai: the buffer is paid from the floor money, so floor, bottom and top all fall $10k; quoting $10k lower with no buffer gives the same 0.11%; payments are 100% covered under d either way (C-01, MODEL) | AMENDED | Vote two dials: d (P5 "+, and last from the floor itself") and a quote margin (P4 "+less a margin for coupon risk"); buffer = D5 question (`../office/outbox/2026-10-25_courtroom_d1-buffer-is-a-lower-quote.md`) |
| Tue 27 Oct (evening) | LR-04: no fixed margin under the 2031 bottom; in 2031 take off only the coupon gap already visible (clearing house: variation, not initial margin) | Kai: a bottom that can be cut isn't the TNA's "promised minimum"; the clearing house is costume; LR-03's donors were households (C-02, MODEL) | AMENDED | Rule stands (0 of 200,000 breaks; letting the gap use the $3,700 gives 35); the IPS states the bottom as a rule, never $145k (below it in 43.5% of paths before any mark); "seven times in ten"; no co-sponsor % in Caplet text (`../office/outbox/2026-10-27_courtroom_mark-to-market-on-trial.md`) |
| Thu 29 Oct (evening) | Challenger C, four doors (Writing Room B, 498) against C13 (V29 para 10) | Kai: B's order line ranks the gift before her half, but para 17 and the model (LR8 line 29) make her half pay the coupon gap first; B drops the range's why; Spinnaker: dates ignore the market | AMENDED | Jun's repair B2 ("the change lands on what isn't yet promised, never a cheque", 495) beats V29 2-0 cold; Keel 5-1; valve and override fall (FR); B3 candidate restores the range's why (`courtroom/C-03_four_doors_on_trial.md`) |
| Sat 31 Oct (evening) | LR-08's paragraph (A09 answered by name; "about $9,000 of her own money in a typical 2033") against V45's "Sell low, by appointment" | Tess: the price is the smallest cell (mean ~$19k by 2042, C-04), the payoff only odds, "promise" twice; Kai/Spinnaker: XR leaves her behind in 62-68% of paths | AMENDED | LR3 (497): the price as a 2042 mean, the rival's January-2031 sale, "$90,000 against our $140,000 after the 2031 set-aside"; panel C04 LR2 1.83 v V45 3.33, voice gate LR3 > LR2; to the inbox (`courtroom/C-04_the_whole_price.md`) |
| Sun 1 Nov (evening) | V50 (D30), the rebuild after Book 11, as the draft Caplet reads Thursday | Kai: "Do not crush" pays off nothing (no "sell" on the page; "opened" is the happy ending, "Break it open" the ruin); Felix: shares "cannot expire worthless" after "every share ... fell to zero", the gap's order, "Never the floor", the leak misnamed, "Nobody else can help" | AMENDED | Amara's repair "Crushing one means selling it before its January, even for the building." ("redeemed" for "opened") beat V50 blind with both readers (36 v 35; 29 v 28), PROMOTE 4-0; T1-T7 truth fixes paid by three repeats (496 count copy); to the inbox (`courtroom/C-05_v50_on_trial.md`) |
Mock judges sat once on 24 Oct, evening, on the Lab's candidates only (Keel's test, not a scoring of Caplet's draft: 25.2 -> 26.4/40). For Caplet's own draft, Caplet's scorers still mark first (`../office/CHARTER.md` section 6; board T14 Sun 1 Nov, T08 Mon 2 Nov).
