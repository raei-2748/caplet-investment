# AX1b audit: rates and fixed income (D1 rerun)

Agent AX1b (cluster auditor, rates), insight_v1 run, 2026-09-28. This is an adversarial check of
`research/insight_v1/phase_D/D1_rates.md` (M044, the dated WInS rung, and M004, the January 2027 purchase rule) before it
reaches the strategy team. It is AI-generated research: findings, numbers and checklists, not text to submit. The team
decides and writes every word. Status labels follow brief section 3 (VP = VERIFIED-PRIMARY, VRF = VERIFIED-REPO-FILE,
SNIP = SNIPPET-UNVERIFIED, ASM = ASSUMPTION, DERIVED = computed by a script from labelled inputs).
Scope (brief section 17): Trading Notes (TN) and IPS only. No relayed messages arrived during this audit.

**What this task delivers**
- This file.
- An "## Audit corrections (AX1b)" section appended to the end of `D1_rates.md`, with 24 items. D1's own text is
  unchanged.
- One check script: `.venv/bin/python research/insight_v1/scripts/AX1b_rates_audit.py`. It imports D1's curve code
  unchanged and reproduces every number AX1b added.

Nothing was committed.

Terms: **gap** = how much more the ten-payment ladder costs than the $300,000 first deposit on 1 Jan 2027. **Funded
ratio** = money available ÷ cost of the ladder. **p5** = the level that 1 in 20 model outcomes fall below. **Drift** = the
direction a model assumes prices move on average. **Fat tails** = big moves happen more often than a bell-curve model
says.

---

## Verdict (short)

**D1 passes with corrections: 0 blocking, 9 important, 14 minor, plus 1 addition and 1 cross-link.**

What holds:
- Both scripts reproduce exactly.
- Every web source re-opened says what D1 quotes.
- All four decisions survive: buy the whole ladder on arrival; buy the longest-dated payments first; finish the ladder
  before any growth money; buy one conditional dated rung in WInS.

What changes:
- **Headline odds:** the real ladder's chance of a gap is about **1 in 3**, not "24-31%".
- **Tail claims:** "0.01%" and the IPS wording "at most part of the first payment" are thin-tail overclaims.
- **Date promise:** "1 January 2028 at the latest" contradicts D1's own late-deposit rule.
- **Guide p.5 reason:** D1 uses it to reject staging, but it does not apply. This is the same error AX2 found in D2.
- **2019 Stock-Trak list:** it cannot tell us anything about 2032-2035 maturities. Those Treasuries did not exist yet.
- **IBTM fallback:** one Trading Note checklist line becomes false if IBTM replaces the bond.
- **Third note:** D1's suggestion to replace VGSH conflicts with D12 unless it is made conditional on option (ii) vs
  (iii).

---

## 1. Scripts re-run (2026-09-28)

| Script | Result |
|---|---|
| `D1_purchase_rule.py` | Reproduces every quoted figure: ladder costs at each shift (exact-date and Nov-15); break-evens (-19/-26, -148/-153, -421/-423bp); 173/185 and 176/185 days; worst day (Feb 27) $27,631 / $28,549 / 19.0%; P(gap) 24.3% / 30.5%; p90/p95/p99 $8.7k / $12.9k / $20.9k; longest-first vs nearest-first (+$1,265 / +$3,831); staging 1.0211 / 27.3% / 0.966 and trigger 1.0218 / 26.5% / 0.912; joint tail $11,957 / $31,413, +$221 / +$531 if late; 2026-09-10 $299,990. Only the "~71%" worst-day share is off (it is 68.7%). The script's curve check prints "09/25 row equals repo file: True". |
| `D1_wins_rung.py` | Reproduces every figure: bond prices, accrued interest, yields and durations; all 7 option rows; ETF-only $1,544 / $451; the +191 to -104 changes; 13 coupons of $1,031.25; STRIP $37,253. Caveat: the STRIP value is a 1 Jan 2027 forward, while the bond price is for 25 Sep 2026 (see minor item 13). |
| `AX1b_rates_audit.py` (new) | [A] worst-day share 68.7%; [B] odds sensitivity; [C] FRED base rates; [D] staging under a different drift; [E] unfunded face by buying order; [F] STRIP on the same date as the bond; [G] accrued interest by trade date; [H] short rates at -421bp. |

Input check: AX1b downloaded the treasury.gov 2026 daily par-curve CSV again on 2026-09-28. After line-ending
normalisation it is **byte-identical** to `scripts/data/D3/treasury_par_2026_raw.csv` (VP). The rows D1 relies on read:
- 02/27 10-year 3.97;
- 09/10 10-year 4.95;
- 09/25 10-year 5.17.

## 2. Sources re-opened (fetch helper, 2026-09-28)

| # | Claim in D1 | Source | Result |
|---|---|---|---|
| 1 | Stock-Trak master bond list; dated 2019; symbol format; 4.375% Nov-2039 and 4.25% Nov-2040 bonds; nothing maturing 2032-2035 | https://www.stocktrak.com/available-bonds/ (JSON-LD datePublished 2017-02-21, dateModified 2019-09-06) | VP. **But** the list has 72 Treasuries, of which 32 are still outstanding on 2026-09-28. Two symbols are mistyped. It jumps from 15-Feb-2031 to 15-Feb-2036, and nothing on it was issued after Feb 2014 |
| 2 | "All bonds, corporate and treasury, that we support are in one master list" | https://content.stocktrak.com/what-are-bonds/ | VP verbatim. The same paragraph says "We only have US bonds", "You can only use market orders" and "There are no volume limit rules on Bonds" (generic; see minor item 10) |
| 3 | "Stock Trak trades only a very limited number of bonds … Treasuries are listed below the Corporates" | https://www.stocktrak.com/investments-bond-analysis-trading-project/ | VP verbatim. The page is dated 14 Dec 2016 |
| 4 | "a limited number of treasury/government bonds"; "When you buy a bond in between coupon dates you will have to pay accrued interest to the seller" | 2026-27 WInS User Guide PDF (edu.stocktrak.com) | VP verbatim. "Day Trading: This is not permitted." is also present, split as "Day T rading" in the text layer |
| 5 | "Bonds available on WInS. The list includes Treasury bonds from the United States, …" | https://wghsinvcomp.smapply.us/res/p/trading/ | VP verbatim |
| 6 | "Any Government/Treasury Bonds from any exchange available on WInS"; "$10" per bond trade; "updated once daily at U.S. market open, and pay out every six months" | https://wghsinvcomp.smapply.us/res/p/faqs/ | VP verbatim, all three |
| 7 | IBTM facts: 0.07% expense; 5.05y effective duration; 5.03% yield to maturity; 15 holdings; $554.5m net assets; $21.85 close; 215,760 average volume; "will terminate on or about October or December 15 …" | https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf | VP. All figures are as of 2026-09-25. The same disclosure says the funds "do not seek to return any predetermined amount" (important item 6) |
| 8 | APRA SPS 160: "can be restored to a satisfactory financial position within one year"; "must not exceed three years" | https://handbook.apra.gov.au/standard/sps-160 | VP verbatim (team knowledge only) |
| 9 | Case PDF created 2026-09-10 15:19 | Case PDF metadata: CreationDate D:20260910151951-04'00' | VRF |
| 10 | Case wording: "will contribute", "high degree of certainty", "may not rely" | `Laura_Gao_2026_Client_Profile.txt` L43-45, L91-92 | VRF |
| 11 | Guide p.5 "should not be rewritten simply because markets move" | `2026_WGY_Investment_Competition_Guide.txt` L154-159 | VRF. The line sits in the post-IPS "evaluation and reflection" stage (important item 4) |
| 12 | IPS guide: "Focus on … rather than … detailed financial calculations" | `2026_WGY_Investment_Policy-FINAL.txt` L51; the explicit ban is at L123 | VRF. It is a focus instruction, not a ban (minor item 17) |
| 13 | CUSIPs 91282CFV8 → 912821KC8; 912810QD3 → 912803DJ9; 912810QL5 → 912803DP5 | `wins_now/S1_mspd_table5_2026-08-31_fixed_2032plus.csv` | VRF (MSPD, per S1). Only $26.1m of the 2032 note is stripped |
| 14 | Laura quotes B8b-Q31 ("finished or not") and B8b-Q18 ("unstable income") | `D13a_laura_quotes_verified.md` rows 100 and 127 | VRF, VERIFIED-PRIMARY there. D1 keeps both out of TN/IPS (correct) |
| 15 | Moody's cut the U.S. to Aa1 on 2025-05-16 | Wikipedia (secondary) | Found. The status stays SNIP, as D1 labels it |
| 16 | (AX1b) The 30-year bond was suspended from 2002-02-18 to 2006-02-09 | https://en.wikipedia.org/wiki/United_States_Treasury_security | Found verbatim; secondary, so SNIP. The Stock-Trak list's own jump from Feb-2031 to Feb-2036 agrees |

## 3. Corrections (full wording in the appended section of D1_rates.md)

**Important (fix before the strategy team uses D1)**
1. **The gap odds understate for the real ladder.** Use about 1 in 3 (30-35%) for the Nov-15 ladder:
   - DERIVED from volatility windows of 7.2-7.8%;
   - an "unchanged curve" drift adds about $1.0k to the January cost (+3.4 points).

   Model-free cross-check: the 10-year yield fell by 19bp or more over 68 trading days in 32-36% of windows (FRED DGS10
   since 1962 and since 1990). Caveat: 1982-2020 was a falling-rate era, which biases history toward falls.
2. **"0.01%" and "at most part of the first payment" are thin-tail overclaims.**
   - A 100bp-plus fall over three months happened in 2.1% of windows since 1990 (2008, 2020). The model gives 0.4%.
   - A 148bp-plus fall happened in 0.1% of windows since 1990 and 1.5% since 1962.
   - A repeat of late 2008 (-167bp) leaves all of the 2033 payment plus ~16% of 2034 waiting. That needs $48.6k, about
     one-third of the $150k deposit.
   - A $75k deposit still covers it.
3. **"1 January 2028 at the latest" overclaims.** It contradicts D1's own late or instalment rule and the joint tail.
4. **Guide p.5 is misapplied** to reject staging. The case against staging rests on the numbers.
5. **The 2019 Stock-Trak list cannot tell us anything about 2032-2035 maturities.** Delete the inference. The logged-in
   check stays.
6. **IBTM fallback:** "repays $50,000 / held to maturity" is false for an iBonds ETF.
7. **Third-note conflict with D12 and D10.** Make the recommendation conditional on option (ii) vs (iii).
8. **Rung rationale:** state it as implementation (the promise is dated), not as "evidence for the reader".
9. **The rung under a position cap below 44% is not computed.** Pre-decide: under a cap, only a 2039/2040 bond, or skip.

**Minor (10-22):**
- the bond-list count and symbol typos, plus the generic "no volume limit / market orders only" lines;
- staging "+0.2 points" is an artefact of the assumption (under an unchanged curve it is -0.2 to -0.5 points, with a
  34-35% chance of ending under 1.00);
- the worst-day share is 68.7%;
- STRIP and note prices should be compared on the same date;
- accrued interest is $768-824;
- -421bp is false precision;
- the script cannot "re-solve on the trade date" as written;
- the IPS "ban" is overstated;
- "no probabilities in a note" is a judgement, not a rule;
- three near-final quoted phrases, including the "her own two deposits" pitch fact, which is wrong in most paths;
- the "finished or not" over-reading;
- drop finding 7 (the PDF date);
- "today" and "bought" wording.

**Addition (23):** longest-first also leaves less face value unfunded if the deposit never comes:
- at -100bp, $31.4k versus $47.7k;
- at -50bp, $12.0k versus $19.0k.

Counterpoint: the shortfall then falls on the first operating year.

**Cross-link (24):** under option (iii), a listed rung is a genuine third executed trade. That answers AX2's blocking
D10 C1.

## 4. Contradictions found

| Between | What conflicts | Resolution (AX1b view) |
|---|---|---|
| D1 vs D12 / D10 | D1: the rung replaces VGSH as the third note. D12: VGSH carries the only "risk management" role word, and D10 wants note variety | Conditional. Under (ii) keep VGSH and treat the rung as optional. Under (iii) the rung is the natural extra note (see cross-link 24). The team decides |
| D1 vs D8 rule 1 | D8: "If the 2028 deposit is smaller or late: … only the facility range shrinks" | D1 is right. If the deposit is missing, or smaller than the gap, part of the first payment stays unfunded. D8's wording needs the joint-tail exception. Main loop to fix; D8 is outside this cluster |
| D1 vs D10 (line 63), brief §14, F-112 | "About 24%" odds are used for the real ladder | Use about 1 in 3 for the real Nov-15 ladder (item 1). The brief §16 wording "roughly 1 in 4 to 1 in 3" is acceptable |
| D1 vs S4 finding 9 | 30.5% vs 30.7% | Harmless: 7.16% (the ladder's own volatility) vs 7.24%. D1's figure is the internally consistent one |
| D1 vs the ticket (check 8) | The ticket says "Record … the bond drop-down (for the Final Report only)"; D1 upgrades it to "decides one order now" | D1 is consistent with brief §17 (no Final Report work). The main loop should update ticket check 8 |
| D1 vs brief §7 | Brief: the ladder "fits inside $300k at today's curve" | D1 is right to drop "fits inside $300k" from the headline and pitch (history: 176 of 185 days above $300k) |
| D1 vs D2 (AX2 C3) | Both misuse Guide p.5 | Same fix: the Guide line is about not redesigning after results. Rules written in advance are allowed |
| D1 vs the ticket's hedge and leftover rules | None | IEF/TLH weights, the option (iii) 35.0/63.0 split and "leftover waits in T-bills" all match |

## 5. Overclaims, jargon, privacy, tokenism, prose

- **Overclaims:** "0.01%", "at most", "at the latest", "matches Guide p.5", "no reward" and "suggests the 2032-2035 notes
  may be missing" (items 1-5, 11).
- **Checked and clean:** D1 correctly bans "match", "risk-free" and anything stronger than "certain in U.S. dollars
  barring a U.S. government default".
- **Jargon:** mostly defined. Not defined: "p5", "zero-drift lognormal" and "forward-consistent". This file defines the
  first two. Keep all three out of deliverables.
- **False precision:** -421bp; "0.01%"; accrued "$750-800".
- **Unearned complexity:** finding 7 (the PDF date). The rung is earned under (iii) and optional under (ii).
- **Privacy:** clean. Both Laura lines are from her professional or public record and are kept out of TN/IPS.
- **Tokenism:** none.
- **Near-submission prose:** three quoted phrases (item 19). Convert them to elements.

## 6. What the strategy team should take from D1 (after corrections)

**IPS: rules to fix before Nov 6** (elements, not wording):
- buy on arrival, in full;
- longest-dated payments first;
- finish the ladder before any growth money, including from each instalment if the deposit arrives late;
- the headline is conditional: fully bought in January 2027 if rates stay near today's (about 2 in 3), otherwise when
  the second deposit arrives;
- name the joint tail as our own stress case;
- name dependence on the 2028 deposit in words, as a typical and a bad case, never as "at most".

**TN / WInS-now:**
- read the Bonds drop-down (by maturity);
- if a Jul-Dec 2032 note is listed, or a 2033-2041 second-half maturity, one rung may be bought:
  - face $50k under (iii), ~$34k under (ii);
  - funded from IEF;
  - under a cap below 44%, only a 2039/2040 bond, or skip;
- IBTM is the last fallback, and its note must not say "repays $50,000";
- every security is PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK.

## Sources (accessed 2026-09-28 unless stated)
- https://www.stocktrak.com/available-bonds/ ; https://content.stocktrak.com/what-are-bonds/ ;
  https://www.stocktrak.com/investments-bond-analysis-trading-project/ (VP content; generic Stock-Trak, not a 2026-27
  WInS rule)
- https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf (VP)
- https://wghsinvcomp.smapply.us/res/p/trading/ ; https://wghsinvcomp.smapply.us/res/p/faqs/ (VP)
- https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (VP)
- https://handbook.apra.gov.au/standard/sps-160 (VP)
- https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
  (VP; identical to the repo snapshot)
- FRED DGS10 daily 1962-2026: `research/insight_v1/scripts/data/D3/fred_DGS10.csv` (VP per D3; not re-downloaded)
- https://en.wikipedia.org/wiki/United_States_Treasury_security ;
  https://en.wikipedia.org/wiki/United_States_federal_government_credit-rating_downgrades (secondary, SNIP)
- Repo (VRF): case txt/PDF; Competition Guide p.5; IPS guide L51 and L123; `wins_now/securities_and_allocation_v0.md`;
  `wins_now/S4_red_team.md`; `wins_now/S1_mspd_table5_2026-08-31_fixed_2032plus.csv`; `phase_A/case_register.md`
  (R-C27, R-C48, R-W28, R-W88, R-AN35, R-AN48); `phase_A/fact_register.md` (F-003, F-014, F-111, F-112);
  `phase_D/D8_practice.md`, `D10_compliance.md`, `D12_overflow_client.md`, `D13a_laura_quotes_verified.md`,
  `audit_markets_rules.md`.

## What this teaches
1. **A model's odds are only as good as its assumptions.** Two honest assumptions (forwards come true; the curve stays
   put) move the chance of a gap from 30% to 34%. History says about 1 in 3. Quote the range and the plain-English
   version, not one decimal.
2. **Bell curves hide crashes.** The model called a 150bp fall in three months a 1-in-10,000 event. It happened in late
   2008. A rule that says "at most" must survive the worst day in history, not just the worst day this year.
3. **Old evidence can be empty for a structural reason.** A 2019 list could not contain 2032 notes, because the U.S.
   had not issued them yet. Before reading meaning into an absence, ask whether the thing could have been there.
4. **A fund with a date is still a fund.** An iBonds ETF ends in a known month but does not promise a dollar amount.
   Only a bond repays a fixed amount on a fixed date. Words in a permanent Trading Note must match the instrument
   actually bought.
