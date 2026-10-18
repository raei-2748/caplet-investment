# Verification: L02 "Client knowledge forensic"

Adversarial check, Fri 16 Oct 2026 (Sydney). Every cited line was opened again in the repo (`/home/user/caplet-investment`), in the 16 Oct branch copy (`caplet-latest/`), or live on the web (page.py fetcher, accessed 16 Oct 2026). Analysis only. No deliverable prose. No personal data.

**Result: 22 findings checked. 6 confirmed, 15 adjusted, 1 refuted (CLIENT-20), 0 unverifiable. 4 added by the verifier.**
Surviving findings, corrected where needed: `verify/L02_client_forensic.final.json` (25 items).

## Does the 16 Oct commit (412e9e3) change L02's conclusions?

Yes, in four places:

1. **A projection now exists (CLIENT-04).** `caplet-latest/research/ips_numbers_2026-10/IPS_number_sheet.md:16-19` gives a range of about $145k-$168k and about 99% confidence that the gift lands inside it (MODEL, 15 Oct curve). It is AI-made, it is on a branch that has not been merged, and the team has not ratified it. So the gap is now adoption and honest framing, not a missing number.
2. **The kept half is worse than L02 says (CLIENT-02).** On the new WInS-basis model, Laura keeps about $28k in 2033 in the middle case and $0 in a 1-in-20 case (`results.json` `laura_kept_2033`). L02's $15-17k came from the superseded 28 Sep STRIPS basis.
3. **New risk: the range does not always protect the payments.** The new model shows a case-compliance gap that L02 missed. See V1 below.
4. **The 13 [AI] suggestions fix none of L02's client gaps.** They add two new problems. See V2 below.

The new rule lets the AI edit deliverables as [AI] suggestions. It does not change any L02 fix. L02's fixes already say the students write. Wharton's AI policy still applies. "Authentic team voice" is a scoring criterion (`smapply_public_2026-10-14/deliverables.txt:57`).

**Ladder-cost conflict, resolved for this lens.** The two figures use the same 15 Oct curve but answer different questions:

- **$294,453 / $5,547 headroom.** `ips_numbers.py:70-90` discounts each $50k to its 1 Jan payment date, as if a zero-coupon bond matured exactly then. It then carries the value forward to 1 Jan 2027. This is a theoretical ladder.
- **$298,624 / $1,376 headroom (4.7bp)** (`lenses/L08_coherence_numbers.md:33`). This prices the WInS holdings Laura can actually buy. They mature 2 weeks to 10.5 months before each payment, and the cash then waits. Yields are held unchanged. L10 traces the gap: about $3.4k from the early maturity dates and about $0.8k from the pricing convention.

**Which to use:**

- For Laura's real, WInS-only ladder headroom (the IBTR reflection, the IPS, any 2033 reserve table), use **about $298.6k / $1.4k**, with its date.
- Use $294k only together with the number sheet's reinvestment section.

## Verdicts

| ID | Verdict | Severity (in → out) | Reason |
|---|---|---|---|
| CLIENT-01 | adjusted | high → high | Word counts re-run, exact: flexib 5/6/0, responsib 4/3/0, liquid 1/4/0. V3:20 and V3:22 confirmed. **Correction:** V5:20 still contains a certainty statement ("depends mainly on the US government"). Only the labelled definition was dropped. The [AI] suggestions do not restore any of the three concepts. |
| CLIENT-02 | adjusted | high → high | V5:26/:28/:30, ips_spec:119, D6:22/:54 and triage:39 all confirmed. **Corrections:** (a) the numbers are now the 16 Oct model's ($28k median; $0 at 1-in-20); (b) the $25k "benchmark" is an AI comment (tab 7:37) citing unverified nonprofit guidance, and the case says no contingency fund needs sizing (lines 106-107); (c) new_vs_known changed to known-deeper, because triage D1 and the 15 Oct brief's vote set B ("Laura's cushion after 2033", final.md:462) already raised it. |
| CLIENT-03 | confirmed | high | Case lines 96-99 and 146-148 are quoted correctly. D_certainty :19/:63 and Tab 15:35 confirmed. The IPS brief (lines 68-70) defers final reserve calculations to the Final Report, and the fix already respects that. Any reserve table must state its ladder basis (see above). |
| CLIENT-04 | adjusted | high → medium | Case lines 117-119 and V5:30 confirmed. "Cannot miss" was already in the 15 Oct brief (final.md:137, :424). The new sheet now supplies the range, the confidence and a good/bad-markets section. "Inside the range" is close to true by construction: the gift is capped at the top, and the bottom is the floor rounded down. The informative numbers are where in the range the gift lands (at the top or within $1k of it in 76% of paths) and how it fails. |
| CLIENT-05 | confirmed | medium | Case line 109 ("begin approaching potential co-sponsors in 2031") and V5:30 ("value then") confirmed. No valuation date or re-quote rule appears in V5, Tab 15 or the 16 Oct suggestions. The 15 Oct brief does not cover it. |
| CLIENT-06 | adjusted | high → medium | Case quotes (lines 9, 40-41, 126-128) and notes :101/:124/:286-302 confirmed. **Correction:** the stock share is about 7% on the 16 Oct model (`allocation_jan2028_typical` VT 0.069). The 9% figure is the 28 Sep number. The trade-off sentence is already a known open item (COMPETITION.md:164, :199-200). "Timid" comes from AI role-play, not from judges. |
| CLIENT-07 | adjusted | medium → low | V5:22 confirmed. "Stereotyping" overstates it: this is an unsupported inference, and V3 had the same sentence. It is a one-sentence fix in a draft the team is rewriting anyway. |
| CLIENT-08 | confirmed | medium | V5:16, case lines 85-86 and the IPS brief :27 confirmed. Already in the 15 Oct brief (final.md:435). The pitch also carries the stale $292,000 figure. |
| CLIENT-09 | adjusted | medium | Arithmetic re-run: $33,681 and $40,036. **Wording corrected:** the case does not "shift" a gap to co-sponsors. It says extra operating support "may come from" other sources (lines 85-86), and it never says operating costs rise. |
| CLIENT-10 | adjusted | medium → low | 4.69% × √2 = 6.6% is **one standard deviation**, not a bound. "Co-sponsors in Taiwan counting in NT$" is an assumption, not a case fact. The case asks no FX question, so one labelled assumption line is enough. |
| CLIENT-11 | adjusted | medium | Case lines 110-112 and strategy_notes:22 confirmed. Numbers updated to the 16 Oct sheet: total about $645k-$668k, which is 143-148% of deposits. The total adds nominal dollars across 2033-42, and the excess over deposits is investment growth, so it must be labelled. |
| CLIENT-12 | adjusted | high → medium | Every citation confirmed (outline:16; talking points :5/:8/:9/:11; notes :218). The stale numbers in that file were already flagged (final.md:723). The "don't offer matching" advice comes from AI research pasted into the team doc. I did not verify the field studies, so it is a team choice, not a fact. Instructions arrive 9 Nov and the deadline is 5 Dec, so the urgency is medium. |
| CLIENT-13 | adjusted | medium | D6:54 ("she adds her own money"), D_certainty:62 and case lines 91-92 confirmed. Not new: final.md:718 and triage D2 already flag it. The 16 Oct sheet's option 1 ("a few thousand dollars from Laura's kept half after 2033") counts as portfolio money only if the half stays invested until 2042. |
| CLIENT-14 | adjusted | low | Case lines 6 and 43-44 confirmed. **Attribution corrected:** the cited lines sit in an AI-style "companion" essay pasted into the team doc (notes :393-397, dated 27 Sep). CLAUDE.md "Client insight" lists the human-capital hedge as an idea to keep, so dropping it is a team decision. |
| CLIENT-15 | adjusted | medium → low | All quotes confirmed, and the bio quotes were verified live. **Attribution:** these are mostly pasted AI-style text, not clearly the students' own words, and that essay itself warns against tokenism (notes :552). The pull-quote risk is already in final.md:141. It only matters if the wording is copied into a deliverable. |
| CLIENT-16 | adjusted | medium | Confirmed, but one citation is wrong: "residency goals" is at deliverables.txt **:56**, not :59. |
| CLIENT-17 | adjusted | high | The TNA brief's lines 5-6 and 52 are read correctly. A grep of the 11 filled notes finds no flexibility, liquidity, residency, community or confidence. Tab 06 holds only images. **Fix corrected:** the TNA is due before vote set B, so the VT reflection must not call the kept half "flexibility" while the team may still make it the back-up for the payments. Any headroom must be quoted with its date and basis. |
| CLIENT-18 | adjusted | low | Confirmed. One citation fixed: `human_approved: false` is client_mandate.yaml **:145** (the file has 148 lines). "Fictional" and the empty portrait were already flagged (final.md:212, :614). |
| CLIENT-19 | confirmed | low | Bio quote "Laura's roots spread wide through California, Texas, and China." verified live (lauragao.com/hey/, 16 Oct). COMPETITION.md:147 still says "Roots First", a name clash that is already known. |
| CLIENT-20 | **refuted** | low | The facts are true, but the implied contrast is wrong. On the 16 Oct WInS-basis model, the early iBond rungs have the **smallest** 1-in-20 shortfall (IBTM $49,273 … IBTR $47,795). The later fixed-coupon bonds have the largest (about $45.9k-$46.5k), because reinvestment risk grows with time (`results.json` `per_rung_p5_p50`). "Not fixed" is already in the notes and in the 15 Oct brief. |
| CLIENT-21 | confirmed | low | Stronger evidence than the lens gave. Rules & Roles (https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/, accessed 16 Oct 2026): "Advisors may not make decisions on behalf of students or actively participate in team activities, trading decisions, or strategy development." |
| CLIENT-22 | confirmed | medium | Case lines 104-106 and D6:27-32/:60 confirmed. Already a vote-set-B item, so known-deeper is right. Guard: the principle should explain why the share is responsible, not size a contingency fund. |

## Missed findings (verifier-added)

- **CLIENT-V1 (high, new): the range does not always protect the payments.**
  - The case says the range "must also protect the portfolio's ability to fund the ten-year operating commitment" (lines 119-120).
  - On the 16 Oct model, the 2033 gift is paid before later coupon shortfalls are known.
  - In about 6.3% of paths, a post-2033 shortfall is larger than everything Laura kept. It is 5.6% even if her half stays in VT until 2042.
  - So, as V5 is written, the portfolio alone fully funds all ten payments in about 93 of 100 modelled paths (`results.json` post2033_shortfall; `IPS_number_sheet.md:46-54`).
  - The "99% inside the range" figure is a different number. It must not be quoted as payment certainty.
  - The team picks a cover (keep the half until 2042, a buffer from the 2028 deposit, or a 2033 reserve top-up) before 6 Nov.
- **CLIENT-V2 (medium, new): the [AI] IPS suggestions need care.**
  - Suggestions 11-12 cite the case's "must" to put "$145,000 to $168,000" and "99 in 100" into the IPS. But the IPS brief says the IPS is "not expected to include ... a final facility-contribution range" (lines 68-70), and the IPS becomes "the official record" (lines 73-74).
  - Suggestion 10 discloses a $21k payment shortfall but names no cover inside the portfolio.
  - Suggestion 13 cuts the kept half's cost-rise job and fixes none of its other jobs.
  - None of the 13 suggestions adds flexibility, responsible or liquidity.
- **CLIENT-V3 (medium, new): the range bottom is not fixed.**
  - The floor is what remains of the $150k after any 2028 top-up of the ladder.
  - In the sheet's own model, the ladder costs more than $300k on 1 Jan 2027 in 35% of paths. The range bottom is $145k in only about 68% of paths, and the paid floor is about $131k at 1-in-20.
  - On the WInS-holdings basis the room is only $1.4k, so a top-up is close to a central case.
  - The IBTR reflection and the Final Report should tell it as a client trade-off: falling yields cost facility money, not payment safety.
- **CLIENT-V4 (low, new): do not size a contingency fund.**
  - The case says teams are "not expected to determine the size or investment composition of a separate contingency fund" (lines 106-107).
  - Fixes that measure the kept half against a $25k-$100k nonprofit benchmark (an AI comment, source unverified) or against building-cost drift drift toward that unrequested sizing.
  - Answer flexibility with a principle instead.

## Checks on rules, privacy and form

- None of the surviving fixes drafts deliverable prose. They are checklists, decisions and evidence.
- No student surnames, emails, WInS username or birthdays appear in either output.
- The public-bio facts about Laura are self-published by her and are used only as evidence for the "do not use identity themes" point.
- Official text quoted exactly where it matters: case lines 91-92, 96-99, 106-107, 117-120; IPS brief lines 48-50 and 68-70; TNA brief lines 5-6 and 52; Rules & Roles advisor clause.
