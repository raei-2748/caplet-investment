# FICTION (the room and the simulated parties) + real arguments. The Courtroom

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

Mock judges not seated on 24 Oct: Caplet's own scorers mark the draft first (`../office/CHARTER.md` section 6; board T14 Sun 1 Nov, T08 Mon 2 Nov).
