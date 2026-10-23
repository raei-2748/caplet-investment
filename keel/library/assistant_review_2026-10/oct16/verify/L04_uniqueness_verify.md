# Verification: L04 "Special but not stupid" (differentiation)

Adversarial check done on Fri 16 Oct 2026 (Sydney). This is AI-generated analysis (Claude), meant as knowledge, not text to submit.
Repo paths are in `/home/user/caplet-investment` unless they start with `caplet-latest/` (the 16 Oct branch copy).
Web pages were fetched with `oct16/tools/page.py` on 16 Oct 2026. My scripts are in `oct16/verify/L04w/`
(`h2.py` = the lens's history script plus checks on the payment-date basis; `build.py` builds the JSON; `kresge.txt` = the guide's text).

**Result:** 20 findings checked. 3 confirmed, 17 adjusted, 0 refuted, 0 unverifiable. I added 4 findings the lens missed.
No personal data was found in the lens files.

## What I re-ran
- `reconcile.py` on the 15 Oct treasury.gov close gives the same results as the lens. On the 6 Oct close it gives $293,453 / 23.0bp on the strict basis, the same basis as the IBTR note.

| Basis (15 Oct close) | Cost | Room |
|---|---|---|
| Payment dates, forward rates | $294,461 | $5,539 |
| Payment dates, curve unchanged | $295,246 | $4,754 |
| WInS maturities, forward rates | $297,847 | $2,153 |
| WInS maturities, curve unchanged | $298,628 | $1,372 (4.7bp) |

- `hist_ladder.py` gives the same results as the lens: 562 days of 6,698 (8.4%); the last day before 2026 was 13 Jul 2007; the first day in 2026 was 23 Sep.
- **New from my run:** on the payment-date basis there are 687 days (10.3%). One of them is **19 Oct 2023 ($299,192)**, and the first day in 2026 is **10 Sep**.
- All six web quotes were found on the live pages: Budescu, Booth, two from RePEc, Kresge (three quotes) and Merriam-Webster.
  - The Kresge guide is "Updated June 30, 2011". It says the challenge grant "is no longer the centerpiece of our work".
  - Merriam-Webster labels "root and branch" "chiefly British".

## The ladder-cost conflict ($294k vs $298.6k): which figure is right for which claim
- **The lens's diagnosis is right.** The gap comes mostly from dates. The number sheet prices $50k at each 1 Jan payment date (`ips_numbers.py:87`). The lenses price each WInS holding's earlier maturity date. Using the forward or unchanged curve adds about $800. The curve date and the ten payments are the same in both.
- **The lens's interpretation is wrong.** $294.5k is *not* "a ladder Caplet cannot own". It equals Caplet's own holdings if the cash from each early maturity (2 weeks to 10.5 months early) earns today's forward rates until the payment date. $298.6k assumes that cash earns nothing and the curve stays where it is.
- **Use this:**
  - The strict figure (about $298.6k, about $1.4k room on 15 Oct) for "certainty", "already bought" and the IBTR reflection. It matches the note's 6 Oct basis.
  - About $294.5k only with its assumption named. It is the like-for-like successor to V5's "$292,000".
  - The odds of a January gap are about 1 in 3 on the payment-date basis, and higher on the strict basis. The lens's "44-45%" mixes the two bases (L03 verifier).
  - Neither figure counts coupon reinvestment.

## Finding by finding

| ID | Verdict | Severity (old -> new) | Reason |
|---|---|---|---|
| UNIQ-01 | adjusted | high -> medium | The quotes are real (TNA:36-39, IPS:22-23, Guide:156, why_us.md:3,90). The "modal team" is an inference. "No structural edge" comes from AI-simulated evaluators (why_us.md:18-23), not judges. The case says "There is no single correct strategy" (case:126-128). |
| UNIQ-02 | adjusted | high -> medium | Much of the "buried" material belongs in the Final Report by design. The IPS is not expected to include the range or the co-sponsor draft (IPS:68-70), and the TNA is not expected to include projections (TNA:20-23). The visibility map is still useful. |
| UNIQ-03 | adjusted | high (kept) | The odds are about 1 in 3, not 44-45%. "Rarely pay to run it" is weakly supported (SSIR starvation cycle, stakeholder_map.md:263-265), not unsupported. The 15 Oct brief already said "unsupported, not contradicted" (final.md:779). The slogan is not literally true: the 2028 deposit has two parts, and the kept half has three jobs (L04-V2). |
| UNIQ-04 | adjusted | high -> medium | The figures reproduce. "Stale" is right: $289,119 is the Nov-15 ladder valued on 28 Sep (ladder_2026-09-28/README.md:3-11). But on the payment-date basis 19 Oct 2023 qualifies and 10 Sep 2026 is the first day in 2026. So "no day since 2007" depends on the basis, and the case-timing story is speculative, not "false". Whether a chart is allowed in the Final Report is UNVERIFIED until 9 Nov. |
| UNIQ-05 | adjusted | high (kept) | All quotes are real. The Kresge guide is from 2011 and covers a programme now used only "on occasion". "Committed, imminent or backstopped" covers named sources only. Budescu says numbers "increase the correspondence", which is less than "fixed much". Cite the original Gneezy-Epley paper. |
| UNIQ-06 | adjusted | medium | The figure is only half circular. The cap fixes the top, but the 99.4% also tests the bottom against coupon shortfalls (sheet:17). The case *requires* a confidence statement (case:117-118), so do not drop it. The range is not expected in the IPS (IPS:68-70). |
| UNIQ-07 | adjusted | high (kept) | Stronger than stated. The IPS instructions ask about "portfolio construction and diversification" (IPS:45-47). V5 never uses the word. Suggestion 7 also drops "thousands of companies" (suggestions:15). Accepting 7 and 8 together leaves no diversification content. |
| UNIQ-08 | adjusted | medium | Overlaps STRAT-02/04. The fix now lists the number sheet's three options (sheet:49-54) and warns that L03's design affects the IBTM rung that the notes describe. |
| UNIQ-09 | adjusted | medium | The Kresge "sustaining support" question (Q6) is about keeping donors, not running costs. Use Q3 ("annual operating needs") and the SSIR article instead. |
| UNIQ-10 | adjusted | medium | Confirmed: F1_floor_variants.py uses the E4/E6 engine from the STRIPS era. Changed from new to known-deeper (final.md:437, :613). |
| UNIQ-11 | adjusted | medium | Changed to known-deeper (time order is already objective 6, final.md:457). The fix misses a format risk: the 2-page limit is disqualifying (IPS:82-83, 103-105). V5 fills 41 of 46 lines, and blank lines push it to 48 (L06:79). |
| UNIQ-12 | adjusted | medium | Wharton does not score trade count (Guide:74-77) and discourages frequent trading (faqs.txt:39), so "reads as passive" is a weak risk. The real value is the dated IBTR "tested" story (TNA:7, 12). |
| UNIQ-13 | adjusted | medium | The stories are real, but the citations are wrong. final_report.md has 27 lines; the stories are at :18, :19 and :22. The STRIPS drop is recorded only in CLAUDE.md, not the journal. |
| UNIQ-14 | adjusted | low | Merriam-Webster says "chiefly British", so many US judges may not read it as an idiom at all. |
| UNIQ-15 | confirmed | medium | Journal :18, KB 2.2/2.4 and the cached iShares disclaimer are all verified. The 2026-27 semifinal format is UNVERIFIED. |
| UNIQ-16 | adjusted | medium | Changed to known-deeper (brief objective 8; COH-08). The TNA needs few figures (TNA:20-23). |
| UNIQ-17 | confirmed | high | CLAUDE.md:27-30, the 13 rewrites and V5:36 "Best version that AI generated" are verified. L09 INT-01 (critical) should lead on this. |
| UNIQ-18 | adjusted | medium | The citation should be final_report.md:23, not :39. Wharton's "NOT investment strategies" is about slogans and Porter's Five Forces, not themed picks. The comic-art ban is verified only for the IPS. |
| UNIQ-19 | confirmed | low | KB 5.2, journal :27 and brief :114/:277-279 are verified. |
| UNIQ-20 | adjusted | medium | The numbers reproduce, but the interpretation is wrong (see the ladder-cost section above). Retitled and rewritten. |

## Findings the lens missed (added)
1. **L04-V1 (medium, new). The co-sponsor research misreads its key funder source.**
   - The team notes say Kresge counts "only" written pledges or cash. The guide's list also includes organizational funds, long-term financing and in-kind gifts.
   - The notes then say "any funder's books", which one funder's rule cannot show.
   - Note 17 turns the donor-support question (Q6) into an operating-costs fear.
   - The guide dates from 2011, for a programme Kresge says is no longer central.
   - V5's pitch premise grows from this note, and L01:413 repeats the claim.
2. **L04-V2 (medium). The "one job" signature clashes with the kept half.** Laura's kept half has three jobs in V5 (:26, :28, :30), and the number sheet proposes a fourth (keep it to 2042 as a payment back-up). Settle its role before adopting the signature.
3. **L04-V3 (medium). The lens's IPS additions do not fit.** V5 is already 47 + 497 words, and the safe target is 45/470. L04 adds about six items with no cut list, and the 2-page limit is disqualifying.
4. **L04-V4 (low). Vote set A is overloaded.** Four new decisions land on Sun 18 Oct, five days before the TNA. Decide only what the TNA needs that day.

## Deadlines checked
- TNA: Fri 23 Oct, 5:00 pm ET (Guide:169) = Sat 24 Oct 08:00 Sydney.
- IPS: 6 Nov, which is also when trading freezes (Guide:172-175).
- Final Report instructions: 9 Nov (deliverables.txt:51).

All the lens's dated fixes fall before the deadlines they serve.
