# Naming inflation is not stating an assumption: the IPS needs one rate, and the 2031 range holds in dollars but not in what it buys
AI-generated research by the Keel Office (Claude Code). Not for submission. Cite in Works Cited.
(Keel is a simulated team, AI-written.)
Work order: SD-LR-01 (Felix's request to Laura's Room, 24 Oct) | Room: Laura's Room (Amara; agents case-analyst, cosponsor-reader in role, no subagents) | Date: Sat 24 Oct 2026 (Sydney, afternoon run)

**Text read:** the full Tab 15 text with Keel's E1-E12 applied (`/mnt/project-files/ips/IPS_edits_2026-10-24.md`, 486
strict words), P4 and P5. Simulated Laura and a simulated co-sponsor are built only from the case
(`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`). Their reactions are tests, never her words, and are
never quoted in anything Caplet submits.

## Answer to Felix's request: does "Inflation or a stronger Taiwan dollar raises costs in Taiwan" meet the case?
**Not fully.** The case asks teams to "identify and explain their assumptions about ... the effect of inflation on
portfolio projections and facility costs" (:146-147). The line names a direction and a defence (the half Laura keeps),
which is a risk, not an assumption: it gives no rate, so a judge cannot tell how big the defence must be. SD-T05 marked
it OK because it is named; this run says named is the floor, not the bar. Two halves, two homes:
- **Facility costs (IPS).** One rate. Verified basis: Taiwan's construction cost index rose **3.54% a year** on average
  since its 2021 base (DGBAS, Aug 2026; F-508 in `keel/library/insight_v1/phase_A/fact_register.md`). The 6.5% of the
  last year is a spike and must not be projected forward (F-509).
- **Portfolio projections (Final Report).** The IPS quotes no projections, so it can stay silent here. The Final Report
  says all projections are nominal dollars, like the fixed $50,000 payments (case :90), with JPM's 2.5% inflation as the
  backdrop.

**Options for the authors (Caplet writes the words):**
| Option | What the IPS gains | Words |
|---|---|---|
| A. Add the rate to P5 (Keel's lean) | The assumption is stated, sourced and checkable; it sizes the defence | about +14 (486 -> ~500) |
| B. Keep the line; put the rate in the Final Report | Nothing now; one deliverable answers it later | 0 |
| C. Replace the line with a nominal-basis sentence | Covers projections, still no facility rate | about +5 |

An example of A, only to show the size (AI DRAFT, Claude, 24 Oct 2026): *"We assume building costs in Taiwan keep
rising about 3.5% a year, as they have since 2021; a stronger Taiwan dollar adds to that."* At ~500 it is at the limit and
30 over Keel's 470 margin; the Writing Room is asked to find the cut (below).

## The visit (SIMULATED)
| # | Who | Reaction (SIMULATED) | Case line it rests on | What the team could change |
|---|---|---|---|---|
| 1 | Laura | "Raises costs by how much? You told me what to fear, not how much to set aside for it." | :146-147; :68-74 (she wants the balance recommended, not left to her) | Option A |
| 2 | Co-sponsor | "Your range can't be missed in dollars. But you quote me in 2031 and pay in 2033: at 3.5% a year, the building costs about **7.2% more** by then, so the bottom of $145,000 buys what about **$135,000** bought when you quoted. And the Taiwan dollar alone moves about **6.6%** either way over two years (one standard deviation)." | :114-116 (the credibility risk); :113 ("remains uncertain") | IPS: nothing beyond option A; the range promises dollars and keeps them, so it does **not** overpromise. Final Report co-sponsor text: quote the range "in US dollars" and say in one line that what it buys moves with Taiwan's costs |
| 3 | Laura | "The half I keep pays three bills: a payment shortfall first, then overruns, then my own plans. In a bad market is there anything left for me?" | :101-103 (flexibility "as the project develops") | Nothing yet: see the finding below; the Lab tests it |
| 4 | Laura | Nothing she would not understand in P4-P5. "Built to hold" and "capped at that top" read cleanly. No change | :117-120 | None |

**Finding (the one worth Monday's time).** In the model's bad case (p5), the half Laura keeps is about **$12k**
(`keel/library/range_2031/README.md`, normal returns). Two years of 3.54% cost drift on the median gift ($168k) is about
**$12.1k**. So at p5 the kept half covers one 2031-to-2033 cost drift and nothing else. That would be a real gap, except
for a point no draft makes yet: **its two big claims tend not to arrive together.** A payment shortfall comes from
yields falling for good (coupons reinvested cheaply); a cost overrun comes from inflation, which usually pushes yields
up, not down. INFERRED, not tested: the Lab's model has no inflation-yield link. If it holds, it is one IPS clause of
genuine insight ("the half she keeps backs two risks that rarely strike in the same years"); if it fails, the D1 buffer
vote on Tue 27 Oct gains a reason.

Numbers: 1.0354^2 - 1 = 7.21%; 145,000 x 0.0721 = $10.4k (so $145k in 2033 buys what ~$135.2k bought in 2031); 168,000 x 0.0721 =
$12.1k; TWD vol 4.69% a year (10-year, F-510/F-512) x sqrt(2) = 6.63%. All MODEL or derived; Laura's 2033 dollars are
nominal.

## Requests filed
- To the Lab (Jun): do falling-yield shortfalls and high-inflation years coincide? US 1954-2025 or any verified series.
- To the Writing Room (Tess): if Caplet takes option A, which ~30 words come out to get back to 470?

## Takes for the morning brief
Amara: Our range is the one promise in the plan that can't be broken – in dollars. The co-sponsor doesn't build in
dollars, though, and that's the sentence the Final Report owes them. For the IPS I'd add the 3.5% and stop there; Laura
deserves the number, not just the warning.
Felix: "Identify and explain their assumptions" (case :146) – a direction isn't an assumption, so I'm withdrawing my own
OK from SD-T05 on this one row. Option A, sourced to DGBAS, and the 6.5% spike stays out.
