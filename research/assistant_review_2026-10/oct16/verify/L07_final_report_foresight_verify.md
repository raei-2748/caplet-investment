# Verification: L07 "Final Report and finale foresight"

Verifier pass, 16 Oct 2026 (Sydney). I tried to refute each of the 19 findings by opening the evidence myself. Sources:
- repo files at `/home/user/caplet-investment` and the 16 Oct branch copy at `/home/user/caplet-latest`
- live fetches on 16 Oct 2026: the Wharton WordPress API for pages 3768 (Deliverables, modified 2024-05-30) and 3778 (Judging and Evaluation, modified 2024-06-03); the Rules & Roles page (saved to `verify/L07_rules_page.txt`); and the Knox term-dates page
- a re-run of `oct16/research/KB_verify/num/reconcile.py` and the lens's own `series.py` and `simple.py`

**Result:** 11 confirmed, 8 adjusted, 0 refuted, 0 unverifiable, 2 added by me.
**Personal data:** none in the lens outputs. But the repo's `COMPETITION.md:117` and the V5 comment author line hold data that must not be copied (see FR-18). I reproduce neither.

## The ladder-cost conflict ($294k vs $298.6k)

I re-ran it on `caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`, 15 Oct close, using the same bootstrap.

| Dates priced to | Forward to 1 Jan 2027 | Curve held unchanged |
|---|---|---|
| Payment dates, 1 Jan 2033-2042 (number sheet) | $294,461, room $5,539 (19.0bp) | $295,246, room $4,754 |
| Caplet's holdings (iBonds 15 Dec 2032-36; Feb-37, May-38, Nov-39/40/41) | $297,847, room $2,153 (7.4bp) | $298,628, room $1,372 (4.7bp) |

**Why they differ:**
- About $3.4k comes from dates. `ips_numbers.py` `bootstrap_cost()` discounts each payment to `dt.date(y, 1, 1)`, but Caplet's holdings mature 0.5 to 10.5 months earlier.
- About $0.8k comes from the forward basis versus the unchanged-curve basis.

**Which figure is right for which claim:**
- **$294k:** right only for "the market value of the ten payments themselves".
- **$297.8k-$298.6k (holdings basis):** right for anything about Caplet's plan, its WInS book, the IPS, the TNA or the Final Report. The basis and date must be stated with it.

**Two new facts:**
- The number sheet's header (`IPS_number_sheet.md:5-6`) says it models the WInS-listed holdings. So does the 16 Oct AI log row (`caplet-latest/docs/AI_USE.md:77`). Both are wrong for the ladder cost.
- The sheet's "1 case in 3" odds of costing more than $300k on 1 Jan 2027 sit on the payment-date basis (`ips_numbers.py:122`). I redid the estimate on the holdings basis. I used the sheet's own 1.00 pt/yr rate volatility over 78 days, which gives a spread of about 46bp against 7.4bp of room. The result is about 4 in 10.

## Verdicts

| ID | Verdict | Severity (final) | Reason |
|---|---|---|---|
| FR-01 | adjusted | critical | Evidence holds: 30 of 63 dated open comments fall on 11-12 Dec 2025 (my count). "Make up stories" is at `2025_knox_wharton.md:3827`, and :3844 has a similar comment. Knox Term 4 ends Thu 3 Dec, and Fri 4 Dec is a Staff PD day. Correction: on a Staff PD day staff are at school and students are not. So the risk is students dispersing after Presentation Day, not staff being away. "Exam week" timing is UNVERIFIED. Critical kept: the Final Report is half the Top 50 basis and has a 25-day window. |
| FR-02 | confirmed | high | Page 3768, re-fetched live, says "minimum of 5 pages", "maximum of 8 pages" and "Reports that go over or under this range will not be reviewed." The 2022-23 version says "will be disqualified". It is a forecast, so medium confidence is right. |
| FR-03 | confirmed | high | Page 3768 requires two snapshots plus a 150-word same/different answer. `portfolio.csv:2, 38-39` and `COMPETITION.md:98` (61.6% "Long Equities") check out. Stronger than claimed: last year's Knox doc had a "PORTFOLIO-AT-A-GLANCE" section (:108). The 2023-24 spec also asked for sector percentages, which a Treasury book cannot fill naturally. I added that to the fix. |
| FR-04 | adjusted | high | Numbers reproduce exactly. Two corrections. First, the par-yield check ($299,995) is about $1.4k off the bootstrap. That equals the unchanged-basis room; it is not larger than both rooms, and par-as-zero is the cruder method. Second, I replaced the lens's suggested "honest claim" sentence with what the claim must contain, so it is not drafted wording. Added: the basis mislabel in the sheet and the AI log, and the about 4 in 10 holdings-basis odds. |
| FR-05 | adjusted | high | The IPS instruction quote (:75-77) is exact. The trade log is blank in the 14 Oct export (the live Sheet may differ). The Trade Log ask was already in the 15 Oct brief. Whether WInS history stays open after the season is UNVERIFIED. Timing changed: the IPS is due Sat 7 Nov 09:00 Sydney, so the full capture moves to after submission. The book is frozen, so nothing changes in the meantime. |
| FR-06 | confirmed | medium | Coupon check: $450 + $393.75 + $382.50 + $312.50 = $1,538.75 on 15 Nov. FAQ :59 and :63 cover coupons, `trading.txt:24` covers the freeze, and V5:26 says income is reinvested. It overlaps COH-13 but adds post-freeze tracking. The WInS date for the May-2038 coupon is UNVERIFIED. |
| FR-07 | confirmed | high | 10 triage rows and 7 decision memos carry "note-in-Final-Report", and none of the 7 has the 14 Oct banner. The STRIPS-basis and 28 Sep figures are at the cited lines. `final_report_outline.md:5` uses old-plan numbers. The 16 Oct branch did not touch `rab/` or `deliverables/`. |
| FR-08 | adjusted | high | The claim that the IPS "bans projections" overstates the rule. The instruction says the IPS "is not expected to include ... detailed portfolio projections" and should avoid "detailed financial calculations" (:51-52, :68-70). Charts and citations are banned (:123). The journal is about ten dated entries, not exactly ten bullets. The main point stands. |
| FR-09 | adjusted | high | The rule quotes (:72-74, :124-125) are exact. V5 does give a certainty mechanism (:20) and does time the 2031 top ("value then", :30). So the real gaps are a test for certainty and a stated return assumption. V5 is at about 497 of 500 words (L04-V3), so any new principle must replace words, not add them. |
| FR-10 | adjusted | high | Wrong line: "[who argued what]" is `final_report.md:25`, not :16. The ethics rule is re-checked live: "invent teamwork and experiential stories". The 7 Oct AI click is confirmed (`COMPETITION.md:192-193`). |
| FR-11 | confirmed | high | 24 dated rows, none from 1-15 Oct. The :91 template and the :45-51 DCF disclosure are as quoted, and the 2023-24 "1-2 sentences" rule is re-fetched. Added: :9 still says AI is "strictly forbidden from authoring prose", which contradicts the 16 Oct rule. Row :77 names no model and mislabels the ladder basis. |
| FR-12 | confirmed | medium | Knox doc :84-86 and :247 check out. Page 3768: "Advisor Reflections: This should be written by the advisor." |
| FR-13 | confirmed | medium | The criterion wording and the old chart plan check out. "Five charts" is a suggestion, not a rule. |
| FR-14 | confirmed | medium | The template fields, "Do not wait until the last minute" and "not yet requested as of 13 Oct" all check out. Semifinal letterhead and consent forms re-checked live. It overlaps INT-18 and TP-20. |
| FR-15 | adjusted | medium (was high) | The evidence holds. But live defence is tested only after Top 50 selection, and the authorship side is already covered by INT-02, INT-04 and TP-01. The first test also landed in IPS week, so the first full test moves to Sun 8 Nov. |
| FR-16 | confirmed | medium | Guide :158-159 quoted exactly. The 2025-26 semifinal rule on weaknesses is confirmed. |
| FR-17 | confirmed | medium | The 2025-26 rules ("case study of one stock or ETF"; "Do NOT introduce completely new material") are confirmed in the evidence pack. |
| FR-18 | adjusted | medium | The posting ban is confirmed live, but it applies "during the Semifinals or Global Finale". The username requirement is on the IPS title page (IPS :98-100); the Final Report's title page is unknown until 9 Nov. Worse than stated: the WInS username is already public at `COMPETITION.md:117`. The fix now includes removing it. |
| FR-19 | confirmed | low | 2027 Term 2 starts Tue 27 Apr (Knox page). Costs and the accompanying adult are confirmed. 9:00 am EDT is 11:00 pm AEST. |

## Findings the lens missed (added)

- **VER-L07-01 (high, new): every Final Report holding must be WInS-listed.**
  - The 2026-27 FAQ allows only WInS-listed stocks, ETFs and Treasury bonds "for BOTH contributions" (`faqs.txt:42-52`).
  - Wharton's 2023-24 Judging page says: "Teams that include prohibited securities in their final report are not eligible for the Semifinals" (page 3778, live 16 Oct 2026).
  - Caplet's files still name things that are either not on WInS or have no ticker: STRIPS, the 15-Nov-2032 note (no WInS T-bond matures Feb 2031 to Feb 2036), a leftover kept in "a Treasury fund" with no ticker, and V5's "substitute a Treasury maturing earlier".
  - Fix: an instrument list checked in WInS before the freeze.
- **VER-L07-02 (high, new): the coupon-risk option must be in the IPS.**
  - The 16 Oct sheet's coupon-risk choice (options 2 and 3 change who holds what) has to be in the IPS by 6 Nov.
  - The Final Report must test "funding reliability ... under varying market outcomes", and the team's own model shows part of a later payment uncovered in about 6-7 of 100 paths.
  - Adding the rule later would be the redesign the Guide forbids (:158-159).

## Does commit 412e9e3 change the lens's conclusions?

Yes, partly:
- **The number sheet:** it adds useful 15 Oct inputs, but its headline ladder cost and odds are on the wrong basis for Caplet's plan, and it mislabels its own basis.
- **The rule change:** it makes FR-11 more urgent. Accepted [AI] wording would make the AI_USE.md template disclosure untrue, and AI_USE.md:9 now contradicts the rule.
- **The coupon-risk decision:** it creates a new IPS-to-Final-Report dependency (VER-L07-02).
