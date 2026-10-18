# L11 Communication: adversarial verification

Verifier pass, Fri 16 Oct 2026 (Sydney). AI-generated check (Claude). Analysis only: no deliverable prose.
Inputs: `oct16/lenses/L11_communication.md` and `.findings.json` (19 findings). Output JSON:
`oct16/verify/L11_communication.final.json`. Build script: `oct16/verify/L11w/build.py`.

## How I checked
- I opened every cited repo line (main repo and `caplet-latest/`) and the official files: IPS brief, TNA brief, Guide,
  Infographic, case, `smapply_public_2026-10-14/deliverables.txt` and `faqs.txt`.
- I re-ran the ladder reconciliation (`oct16/research/KB_verify/num/reconcile.py`) on the October Treasury CSV for 2,
  5, 6, 13, 14 and 15 Oct.
- I re-ran the team's draft checker (`D9_draft_checker.py`, read-only) on the V5 pitch and body.
- I recounted the jargon greps, the note lengths and numbers, and the after-[AI] statistics.
- I re-opened these Wharton pages on 16 Oct with `page.py` or curl, and all were FOUND:
  - the 2025 Top 10 post ("hiding behind fancy terms", "simple, elegant ideas");
  - the 2026 Top 50 post ("Wharton School student evaluators", Aberdeen);
  - the 2025-26 semifinal PDF ("not generated or generic responses");
  - the AI Policy ("must use their voice and words");
  - the legacy Developing a Strategy page ("not be among the strongest teams");
  - the legacy judging page 3778, modified 3 Jun 2024 ("Excessive investing jargon...", "Don't use precious space
    repeating known facts...", "make your report memorable").
- I also checked Wikipedia (caplets) and Merriam-Webster (root and branch), both FOUND.
- Privacy: the lens files contain no surnames, initials, emails, usernames or fork names. My outputs contain none.

## Ladder-cost conflict: resolved
The figures are reproduced exactly on the 15 Oct row.

| Basis | Cost on 1 Jan 2027 | Room under $300k |
|---|---|---|
| Payment dates, forward | $294,461 | $5,539 (19.0bp) |
| Payment dates, curve unchanged | $295,246 | $4,754 (16.3bp) |
| Owned maturities, forward | $297,847 | $2,153 (7.4bp) |
| Owned maturities, curve unchanged | $298,628 | $1,372 (4.7bp) |

**Why they differ.**
- About $3,400 comes from the dates priced to. The number sheet prices to 1 Jan payment dates
  (`ips_numbers.py:87`). The lenses price to the maturity dates of the bonds held (15 Dec 2032-36, Feb-2037, May-2038,
  Nov-2039/40/41).
- About $800 comes from the curve basis: forward value carried to 1 Jan, or the curve unchanged to 1 Jan.

**Where L11 goes wrong.** The owned-maturity figure assumes that money from each bond earns nothing between maturity
and payment. The team's own notes say that money sits in a short-term Treasury ETF (`05_...md:16-17`). So $294k is not
"an ideal ladder Caplet does not own". It is what the owned bonds cost if that waiting money earns today's implied
rates.

**Which figure for which claim.**
- $294-295k: the central claim, if labelled and dated.
- About $298k: the cautious claim ("even if waiting money earns nothing").
- The 6 Oct IBTR note's "about 0.2 points" matches the owned basis on 6 Oct (23-27bp). The payment-date basis that day
  was 35-39bp.

**The room moves fast.** From 14 to 15 Oct the room fell by about $2,600-2,700 on both bases. Any level is a one-day
quote.

## Verdicts

| ID | Verdict | Severity (old -> new) | Reason |
|---|---|---|---|
| COMM-01 | confirmed | high | All four lines are at V5:16/24/28/30. Case:85-86 says co-sponsors "may" fund operations. Number sheet:48 admits "cannot miss" is untrue. The 5 Oct reason for keeping "never below the floor" was STRIPS (final_report.md:24), and the 6 Oct email removed it. Already on COMPETITION.md:200, so known-deeper. |
| COMM-02 | adjusted | high -> medium | Counts reproduced. "18 rules" is the lens's own count. The "12 ideas" cap is an AI spec, not a Wharton rule. The scoresheet (:58) already flagged it, so not new. The IPS brief requires about ten topics (IPS:15-20), so the fix now cuts implementation detail, not required topics. |
| COMM-03 | adjusted | high -> medium | Quotes correct. Mostly repackages COMM-01, COMM-04, IPS-08 and IPS-18. Corrected "$292,000 on the wrong basis" to "stale, basis unstated" (it is the payment-date basis). |
| COMM-04 | adjusted | high | Numbers reproduced, but the guidance was one-sided (see above). "44-45%" odds are UNVERIFIED (not re-run). Fix rewritten: one named basis, dated, rule over level. |
| COMM-05 | confirmed | high | V5:36 comment, deliverables.txt:59 and the AI Policy all confirmed. The connective counts are weak style evidence; the doc comment is the real evidence. Overlaps L09. |
| COMM-06 | adjusted | high -> medium | The grep counts are inflated and mix methods. "RAB 2,206" is mostly the folder name "rab/" in paths. "p95 1,110" and "gate 1,055" are substring counts that include binaries. Whole-word, case-sensitive counts: RAB 263, REC 482, p95 300/474, STRIPS 320/312, sleeve 1,507. The point stands; the risk starts on 9 Nov. |
| COMM-07 | confirmed | medium | "facility floor" x3, "floor" x10; no "floor" in the case. Note: the IBTM note's "floor" is frozen (see L11-V01). |
| COMM-08 | confirmed | medium | Reproduced: 498 words, 31 digit tokens, 10 dollar figures, longest sentence 32 words. IPS:68-70 confirmed. The file's own header ("494 after all twelve") is also wrong (13 rows). |
| COMM-09 | confirmed | medium | Quotes correct. Caveat: case:117-118 requires a stated confidence somewhere, so the Final Report needs one; only the IPS is optional. |
| COMM-10 | adjusted | medium -> low | Checker output reproduced, but it does flag "many numbers". The "ladder" ban (ips_spec:53) is a pitch rule, wrongly applied to a WInS note, so that point is removed. It is a team tool, not a deliverable. |
| COMM-11 | confirmed | medium | Top 50 readers, criteria wording, legacy jargon quote and team note all FOUND. |
| COMM-12 | adjusted | medium | Case:91 says "high degree of certainty"; "funding certainty" is at :97-98. Wording corrected. |
| COMM-13 | adjusted | medium -> low | Counts reproduced, but the three suggested picks are the least dense notes (3/5/3 numbers). "450 words of figures" overstated. |
| COMM-14 | confirmed | medium | Note quote confirmed. On the note's basis the room fell from 23-27bp (6 Oct) to 4.7-7.4bp (15 Oct). The reflection must name its basis. |
| COMM-15 | adjusted | medium -> low | Clock facts correct. TNA:53 verifies that notes match trades, not reflection dates. "Filled 7-8 Oct" is consistent with orders placed on US evenings of 6-7 Oct. So this is confusion, not a verification risk. |
| COMM-16 | adjusted | medium -> low | Formats confirmed, but these are working files; the harm only comes by copying, which COMM-08 and COMM-09 cover. |
| COMM-17 | confirmed | medium | The "This policy governs" opening is in seven or more tabs. Both Wharton quotes FOUND; both pages are legacy guidance, now labelled so. |
| COMM-18 | confirmed | low | Both definitions FOUND; the KB supports a credit/fixed-income finale judge. |
| COMM-19 | confirmed | low | "defense" at V5:28 and Tab 15:18; "prioritise" at V4:16 and :24. |

Refuted: none. Every finding had real evidence. Nine needed corrections; seven of those were downgraded.

## Findings L11 missed (verifier-added)

**L11-V01 (medium, TNA first). The frozen notes set the TNA's words.**
- The TNA must quote notes "exactly as it appears in WInS" (TNA:44), and the notes use words that L11's blacklist says
  to replace: "ladder", "floor", "payout is not fixed", "reinvestment-rate risk", "scaled to the model portfolio".
- Two suggested picks already name the minimum two ways: "floor" (IBTM, `05_...md:19`) and "promised minimum" (VT,
  :14).
- Swapping in blacklist words in the reflections would give one idea two names in the same entry.
- What a fix must achieve: the term map starts from the words already in WInS. Each reflection keeps the note's word.
  Where two notes differ, the reflection links them once. All of this is settled before the 23 Oct submission, because
  the TNA's words are fixed two weeks before the IPS.

**L11-V02 (medium). Look-alike numbers on different bases.**
- The IBTR note's "about 0.2 points" (6 Oct, owned basis) and the number sheet's "0.19 points" (15 Oct, payment-date
  basis) look the same. On the note's own basis, the room actually fell from about 0.23-0.27 to about 0.05-0.07 points.
- The cancelled IBTR note said 0.3 and the filled one says 0.2 (`05_...md:37` vs :15).
- The room moved about $2,600-2,700 in one day (14 to 15 Oct).
- What a fix must achieve: updates use the note's basis, named in words and dated. The reflection and the IPS rest on
  the rule, not the level. Numbers are re-run on the day the text is frozen (Thu 22 Oct).

## Does commit 412e9e3 change L11's conclusions?
- It adds the $294k figure and the [AI] suggestions. That makes COMM-04, COMM-08 and COMM-09 more urgent, and it is
  where L11-V02's look-alike number comes from.
- The rule change (`caplet-latest/CLAUDE.md:26-29`) does not change the authenticity point in COMM-05. Accepted [AI]
  wording still has to be cited, and it is not the team's voice.
