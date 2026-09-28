# D1 - Rates & fixed income: the dated rung in WInS (M044) and the January 2027 purchase rule (M004)

Agent D1 (Rates & Fixed-Income Analyst), run insight_v1, 2026-09-28. AI brainstorming output for the team:
specifications, evidence, numbers and checklists. It is **not** text to submit. The team decides and writes every word.
Scope (brief section 17): Trading Notes (TN, Oct 23) and IPS (Nov 6) only. Anything that is purely Final-Report
material is one line in "Later (after Nov 9)". No relayed messages arrived during this work.

Status labels: VERIFIED-PRIMARY (VP), VERIFIED-REPO-FILE (VRF), SNIPPET-UNVERIFIED (SNIP), ASSUMPTION (ASM),
DERIVED (computed by a script here from labelled inputs), INTERPRETATION (our reading; not a fact).
Every security is **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK** (brief sections 4 and 14).

Scripts (run from the repo root):
- `.venv/bin/python research/insight_v1/scripts/D1_wins_rung.py` (M044: bond prices, sizing, re-weighting, tracking)
- `.venv/bin/python research/insight_v1/scripts/D1_purchase_rule.py` (M004: rate-fall costs, the longest-first split,
  2026 history, gap odds, buying all at once versus in stages, the joint tail)

Terms used below:
- **Ladder / rung:** Laura's real plan buys ten Treasury zero-coupon bonds (STRIPS), one per $50,000 payment. Each is
  a "rung".
- **Coupon bond:** an ordinary Treasury that pays interest every six months and repays its face value at maturity.
- **Face value:** the amount a bond repays at maturity. **Accrued interest:** interest earned since the last coupon;
  the buyer pays it to the seller.
- **Duration:** roughly the % a bond's price moves when rates move 1 percentage point. **Cash-flow match:** the money
  arrives on the date it is needed. **Duration match:** the value moves like the payments' value, but no money is
  dated.
- **Gap:** how much more the ladder costs than the $300,000 first deposit on 1 January 2027.
- **bp** = basis point = 0.01 percentage point. **Funded ratio** = money available ÷ cost of the ladder.

---

## Summary: top findings (ranked by impact on reaching the semifinals and on making the plan hers)

1. **The IPS headline should be rate-conditional: "the whole first deposit buys the ladder on the day it arrives,
   longest-dated payments first. Any unbought part is the earliest payment(s), and it is the first use of the 2028
   deposit, before any growth investment."** (M004, IPS; DERIVED numbers below)
   - Today the real Nov-15 STRIPS ladder costs $294,387, so it fits under $300k with $5,613 to spare (VRF curve;
     DERIVED).
   - A 19bp fall before January creates a gap. The model odds of a gap are **24-31%** (exact-date zeros vs the real
     Nov-15 ladder; ASM zero-drift lognormal). Use these odds, **not** the 173/185-day count, which is history.
   - On the **worst curve of 2026** (Feb 27, 10-year at 3.97%) the gap is $27,631. In 2028 dollars that is $28,549,
     which is **19% of the $150k deposit**.
   - Even then, only part of **one** payment waits: the 2033 payment. The gap exceeds a whole payment only after a
     ~150bp fall. The model odds of that are 0.01%. The gap exceeds the whole 2028 deposit only after a ~420bp fall
     (10-year under 1%).
2. **Buy everything at once. Staging and yield triggers are rate bets with no reward (M004, IPS).** DERIVED, ASM:
   - Four quarterly tranches in 2027 leave the expected funded ratio almost unchanged (+0.2 points).
   - But they turn a known 1.019 into a **27% chance of ending under 1.00** (p5 0.966).
   - A "wait for a 5% margin" trigger does the same (26.5%; p5 0.912).
   - This matches Guide p.5: the strategy "should not be rewritten simply because markets move".
3. **Longest-first is right, and now there is a number for it (M004, IPS).** Suppose rates fall 100bp, a gap opens,
   and rates then fall another 100bp during 2027:
   - longest-first: the waiting part (the 2033 payment) costs **+$1.2k (+5%)** more;
   - nearest-first: the waiting part (the 2042 payment) costs **+$3.6-3.8k (+15%)** more.

   Leaving the *shortest* payment unbought leaves the smallest, least rate-sensitive piece exposed (DERIVED).
4. **Name the joint tail plainly (M004, IPS rule; wording is the team's).** Rates fall ~100bp before January **and** the
   2028 deposit never arrives:
   - about **$31k of the $50,000 January-2033 payment is unfunded** (6.3% of the $500k promised; DERIVED);
   - every other payment is bought;
   - a $75k deposit covers every rate fall down to the 2026 worst case;
   - a deposit six months late costs only ~$0.2-0.5k more if rates are unchanged.

   The case says she "will" contribute (R-C27, R-AN35), so this is our own stress scenario and must be labelled as
   such.
5. **One dated Treasury "rung" in WInS is worth one $10 trade, if WInS lists a suitable bond (M044, WInS-now + TN).**
   - It turns "we would buy a ladder" into a holding a fixed-income reader can check: a bond repaying $50,000 on
     15 Nov 2032, 47 days before the first payment.
   - It is the parent bond of the real ladder's first STRIP (CUSIP 91282CFV8 → principal STRIP 912821KC8; VP via S1's
     MSPD table).
   - The effect on hedge accuracy is tiny either way (DERIVED): +$191 to -$104 on a worst 50bp twist, against
     $1,544 now.
   - So the reason to buy it is the evidence it gives, not the hedge accuracy. It is a strong candidate to replace the
     VGSH buy as the third Trading Note.
6. **Which maturities WInS lists cannot be answered from public pages. The only public Stock-Trak bond list is from
   2019 and has no Treasury maturing 2032-2035.**
   - That list (stocktrak.com/available-bonds, dateModified 2019-09-06; VP for its content, **not** a 2026-27 WInS
     list) has 32 U.S. Treasuries.
   - Among them are the **4.375% 15-Nov-2039** and **4.25% 15-Nov-2040** bonds, which are the parents of two of the
     real ladder's STRIPS.
   - The 2026-27 WInS User Guide says the competition involves "a limited number of treasury/government bonds" (VP via
     A4).
   - So the drop-down check is a tier-1 gate item. The fallback order is below.
7. **Small but useful: the case PDF's creation date (2026-09-10) is the day the real ladder cost $299,990.**
   - That is, almost exactly $300,000 (DERIVED from the 2026-09-10 curve).
   - INTERPRETATION only: it may be coincidence. Never claim it in a deliverable.
   - What it does show: the $300k "fit" is knife-edge, not comfortable, which is why the rate-conditional rule in
     finding 1 is needed.

---

## Question M044 (tier 1: WInS now + Trading Notes Oct 23)

**Question (canonical):** Should the WInS book hold one or more individual Treasuries maturing near Laura's payment
dates (Nov 2032-Nov 2041), to show cash-flow matching rather than only duration matching with constant-maturity ETFs,
and which of those maturities does the WInS bond list actually offer?

**One-sentence answer:** Yes, one. If the WInS Bonds drop-down lists a Treasury maturing in the second half of a year
from 2032 to 2041, buy one rung sized to one payment and fund it from IEF (not TLH). The fit barely changes, and it
gives the TN set a checkable, dated piece of Laura's ladder. Which maturities are listed can only be seen when logged
in, and the one public Stock-Trak list suggests the 2032-2035 notes may be missing.

### Evidence
| Claim | Source (accessed) | Status |
|---|---|---|
| Individual government bonds are a permitted type: "Treasury Bonds: Bonds available on WInS. The list includes Treasury bonds from the United States, …" / "Any Government/Treasury Bonds from any exchange available on WInS" | https://wghsinvcomp.smapply.us/res/p/trading/ and /res/p/faqs/ (via `phase_A/case_register.md` R-W69, R-W89; read 2026-09-27) | VP |
| $10 commission per Treasury bond trade; bond prices update once daily at the U.S. open; coupons every six months; bonds valued at the end | SMApply FAQ (R-W91, R-W92) | VP |
| The platform lists "a limited number of treasury/government bonds"; the quote shows face value, last price, last coupon, accrued interest; "When you buy a bond in between coupon dates you will have to pay accrued interest to the seller" | 2026-27 WInS User Guide p.7, p.11, https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf (re-read 2026-09-28; visible-text check by A4 in `phase_A/wins_week1_guardrails.md`) | VP. The PDF text layer also holds a hidden older line about "approved lists"; A4 found that it is not visible on the rendered page, so do not rely on it |
| Stock-Trak's public "Available Bonds" master list, dated 2019: 32 U.S. Treasuries, symbol format `B-T-<coupon>-<ddmmyyyy>` (e.g. `B-T-4.375-15112039`); maturities 2036-2044 include Feb/May/Aug/Nov bonds, among them 4.375% 15-Nov-2039 and 4.25% 15-Nov-2040; **none maturing 2032-2035** | https://www.stocktrak.com/available-bonds/ (linked from https://content.stocktrak.com/what-are-bonds/: "All bonds, corporate and treasury, that we support are in one master list"); JSON-LD dateModified 2019-09-06; read 2026-09-28 | VP for the page; **relevance to 2026-27 WInS UNVERIFIED** (generic, 7 years old) |
| Stock-Trak's own teaching assignment: "Stock Trak trades only a very limited number of bonds … Treasuries are listed below the Corporates" | https://www.stocktrak.com/investments-bond-analysis-trading-project/ (read 2026-09-28) | VP (generic platform, not a season rule) |
| Candidate bonds exist and are strippable: 4.125% note 15-Nov-2032 (91282CFV8; principal STRIP 912821KC8); 4.375% bond 15-Nov-2039 (912810QD3; 912803DJ9); 4.25% bond 15-Nov-2040 (912810QL5; 912803DP5) | `research/insight_v1/wins_now/S1_mspd_table5_2026-08-31_fixed_2032plus.csv` (Treasury MSPD Table V, record date 2026-08-31, per S1) | VP per S1 |
| IBTM (iShares iBonds Dec 2032 Term Treasury ETF): expense 0.07%; effective duration 5.05y; average YTM 5.03%; 15 holdings; net assets $554.5m; close $21.85; 30-day average volume 215,760 (all as of 2026-09-25/24); the funds "will terminate on or about October or December 15 of the year in each Fund's name" | https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (read 2026-09-28; phrase verified verbatim) | VP. Not on the 2025-26 list (S1 table, VRF) |
| Constant-maturity funds never mature; three-quarters of TLH's bond weight matures after the last payment | `wins_now/securities_and_allocation_v0.md` §1 (74.7%), S4 finding 2 | VRF (repo research) |
| 2024-25 Session Rules screenshot showed a bond "Position Limit (Single Position) 100%" | 2024 WInS guide p.6 via `phase_A/wins_week1_guardrails.md` | VP [PRIOR]: history only |
| S4 dropped an individual 2041 bond only as a position-limit **fallback** on complexity grounds; a single dated "demonstration rung" was never assessed | `wins_now/S4_red_team.md` finding 3 | VRF |

### Numbers (`D1_wins_rung.py`; curve 2026-09-25 VRF; model prices ASM)
| Bond (pays for) | Clean price | Accrued at 9/25 | Yield | Model duration | Next coupon |
|---|---|---|---|---|---|
| 4.125% 15-Nov-2032 (1 Jan 2033) | 95.27 | 1.49 | 5.03% | 5.27y | 15 Nov 2026 (after the Nov 6 freeze) |
| 4.375% 15-Nov-2039 (1 Jan 2040) | 91.36 | 1.58 | 5.29% | 9.64y | same |
| 4.25% 15-Nov-2040 (1 Jan 2041) | 89.31 | 1.54 | 5.34% | 10.21y | same |

Sizing and re-weighting. IEF/TLH are re-solved so that the whole hedge keeps the ticket's model duration (10.09y,
which is 9.90 on issuer numbers). Tracking uses S4's forward-consistent method; the ETF-only worst 50bp twist is $1,544
and the worst ±100bp is $451.

| Option | Rung | Rung $ (share of $300k) | IEF / TLH (share of $300k) | Worst twist | Worst ±100bp |
|---|---|---|---|---|---|
| (iii) literal Jan-2027 book, face $50,000 | 2032 note | $48,378 (16.1%) | 13.6% / 68.3% | $1,735 (+191) | $485 |
| | 2039 bond | $46,473 (15.5%) | 28.1% / 54.5% | $1,440 (-104) | $435 |
| | 2040 bond | $45,424 (15.1%) | 29.9% / 52.9% | $1,456 (-88) | $438 |
| | IBTM ~1,686 sh | $36,841 (12.3%) | 18.2% / 67.5% | $1,710 (+166) | $480 |
| (ii) post-2028 mix scaled, face $34,000 | 2032 note | $32,897 (11.0%) | 9.0% / 46.0% | $1,737 | $485 |
| | 2039 bond | $31,601 (10.5%) | 18.8% / 36.6% | $1,439 | $435 |
| | IBTM ~1,147 sh | $25,052 (8.4%) | 12.2% / 45.5% | $1,711 | $480 |

- **Hedge accuracy is not the argument.** Every change is under $200, less than 0.1% of the hedge (DERIVED).
- **Coupon vs zero.** $50,000 face of the 2032 note costs ~$48.4k. It pays 13 coupons of $1,031.25 ($13,406) before
  its $50,000 principal. The STRIP carved from the same bond costs ~$37.3k and pays only the $50,000 (DERIVED; S3).
  That coupon cash, and the need to reinvest it, is exactly why Laura's real ladder uses STRIPS (brief section 8
  item 11). The rung note can make this point in one clause.
- **Accrued interest:** about $750-800 on $50k face, paid at purchase. No coupon arrives before the Nov 6 freeze
  (DERIVED).
- **Position limit:** the rung is 8-16% of the book, under any documented cap. **Watch-out:** a 2032 rung *raises* the
  TLH share (68% under (iii)), because the rest of the hedge must be longer. A 2039/2040 rung *lowers* it (53-55%).
  Under a cap below ~44%, the ticket's SPTL branch still applies to whatever TLH share remains.
- **Scaling (option ii):** the rung represents one payment at the same 0.685 scale as the rest of the book ($34k face).
  A "$50,000 = one payment" rung reads most naturally under option (iii). That is a small point in (iii)'s favour; it
  is not a reason to switch.

### Implication (decision; WInS-now + TN)
**Decision rule for the WInS gate session (tick in order; stop at the first "yes").**

1. The Bonds drop-down lists a U.S. Treasury maturing **Jul-Dec 2032**. The 4.125% 15-Nov-2032 note (91282CFV8) is
   best: it pays for the first payment, the first year of the residency's operations.
   - Buy face $50,000 under (iii), or ~$34,000 under (ii).
   - Take the money out of **IEF**.
   - Re-solve IEF/TLH with `D1_wins_rung.py` on the trade date.
2. Otherwise, it lists a Treasury maturing Jul-Dec of any year 2033-2041. The 15-Nov-2039 and 15-Nov-2040 bonds on
   Stock-Trak's old list are the likeliest.
   - Buy the same size, funded from IEF and TLH as the script says.
   - Bonus: its ~10-year duration eases the TLH position-limit problem.
3. Otherwise, **IBTM** is listed as an ETF: buy ~$37k under (iii) or ~$25k under (ii). Alternate: IBTO (Dec 2033),
   which funds the 2034 payment.
4. Otherwise, **no rung.** Record "no suitable dated Treasury listed" in the decision log. Do not force it with a
   Feb/May bond far from a payment date.

Mechanics:
- The rung is bought **in the same session as the hedge**, so it adds one trade ($10) and no extra re-weighting trades.
- If it is added later, the IEF trim is a genuine later decision and could itself be a note. Never buy and sell the
  same security on the same U.S. trading day.

**Trading Note checklist for the rung (elements only; the team writes the words):**
- which payment it stands for: 1 Jan 2033;
- its maturity date: 15 Nov 2032, 47 days before;
- its face: $50,000, one payment (or "scaled like the rest of the book");
- that it is held to maturity, so later price moves do not change the $50,000 it repays;
- that the other nine payments' rate sensitivity is carried by the ETFs (about 10 years together);
- the honest limit: it is a coupon bond; Laura's real ladder uses the zero-coupon STRIP cut from this same bond,
  because coupons would have to be reinvested;
- the rule: never sold because rates moved.

**Never claim** that the whole ladder is in WInS, that the ETFs "match" the payments, that the rung is "risk-free" in
WInS value terms, or anything stronger than "certain in U.S. dollars barring a U.S. government default". Moody's cut
the U.S. to Aa1 on 2025-05-16: SNIP (Wikipedia, read 2026-09-28; not checked on moodys.com).

**Reflection (≤100 words) should contain:** the difference between a dated cash flow and a duration stand-in; how that
serves "a high degree of certainty" (case p.3 L91, VRF); and one thing the team learned, e.g. why coupons create
reinvestment risk. No Laura quotes (D13 rule).

**Add to the WInS gate checklist:**
- screenshot the Bonds drop-down, list every U.S. Treasury maturing 2032-2042 (symbol, coupon, maturity);
- record the bond position limit;
- check whether the 2x-daily-volume rule shows a volume for bonds;
- record the accrued interest shown.

This upgrades ticket check 8 from "for the Final Report only" to "decides one order now".

- **Deadline tier:** 1. **Confidence:** medium. The logic is high-confidence; WInS availability is unknown.
- **Changes current strategy?** Yes, slightly. It adds one conditional order to the WInS ticket and a candidate third
  note in place of VGSH. It does not change the plan.
- **Criterion served most:** Portfolio Analysis (why each security belongs; quantitative + qualitative), then
  Investment Strategy.
- **What this teaches:** a fund can *behave* like a promise; only a bond with a date can *keep* one. Showing one real
  rung is simpler and more convincing than a longer explanation of durations.

---

## Question M004 (tier 2: IPS Nov 6; one tier-1 by-product)

**Question (canonical):** If rates fall and the ladder costs more than $300k on the January 2027 purchase date, should
the IPS base rule be "buy as much as the first deposit affords, longest rungs first, and complete it from the 2028
deposit", with a stated shortfall limit and "fully funded by 1 January 2028 at the latest" as the headline? And should
the purchase be made in full, in stages or on yield triggers, in a way Laura would recognise as hers?

**One-sentence answer:** Yes. Buy in full on arrival, longest-dated payments first. Any unbought part is always the
earliest payment(s), completed as the first use of the 2028 deposit before any growth money. State the maximum
dependence and the joint tail openly. Reject staging and triggers: they add a ~27% chance of being under-funded for
+0.2 points of expected funding.

### Evidence
| Claim | Source (accessed) | Status |
|---|---|---|
| "All ten payments must be funded by the investment portfolio with a high degree of certainty." / "Teams may not rely on co-sponsors, grants, program fees, or other outside funding". The 2028 deposit is Laura's own contribution *to the portfolio*, so using it is not outside funding | case p.3 L91-92 (R-C47, R-C48); p.2 L43-45 (R-C26, R-C27) | VRF (reading of R-C48 is INTERPRETATION, low risk) |
| She "will contribute an additional $150,000 at the beginning of 2028, using earnings from publishing advances, speaking engagements, licensing, and other entrepreneurial ventures"; no other flows before 2033 | case p.2 L43-45, L63-65 (R-C27, R-C34) | VRF |
| "A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten simply because markets move" | Competition Guide p.5 (`2026_WGY_Investment_Competition_Guide.txt`) | VRF |
| IPS "Focus on the strategy and decision-making framework … rather than … detailed financial calculations"; no citations or charts | `2026_WGY_Investment_Policy-FINAL.txt` L51; brief §5 | VRF |
| Ladder cost above $300k on 173 of 185 trading days of 2026 (exact-date); 176/185 for the real Nov-15 ladder | `D1_purchase_rule.py` [5] on `scripts/data/D3/treasury_par_2026_raw.csv` (treasury.gov snapshot; its 9/25 row equals the repo file) | VP inputs + DERIVED |
| Case PDF created 2026-09-10 15:19 | `phase_A/case_register.md` §1.1 | VRF |
| Practice anchor: Australia's defined-benefit standard sets a shortfall limit ("can be restored to a satisfactory financial position within one year") and a restoration period that "must not exceed three years" | APRA SPS 160, https://handbook.apra.gov.au/standard/sps-160 (both phrases verified verbatim 2026-09-28) | VP. Team knowledge only: the IPS bans citations, and the Final Report is out of scope for now |
| Laura's "I give myself a deadline for when I must post the art, finished or not." (Geeks OUT, 2022-05-11, about posting art) and "self-employed, with unstable income" (Overachiever, 2021-03-15) | `phase_D/D13a_laura_quotes_verified.md` rows B8b-Q31, B8b-Q18 | VP. **Not for TN/IPS** (D13 rule); there is no verified Laura statement about investing, so any "hers" link is INTERPRETATION |

### Numbers (`D1_purchase_rule.py`; curve VRF/VP; method ASM, identical to the verified script)
**[1]-[2] Cost at 2027-01-01 and the longest-first split** (real Nov-15 STRIPS ladder; exact-date zeros in brackets)
| Parallel fall before Jan 2027 | Ladder cost | Gap | What waits | 2028 $ needed | % of $150k |
|---|---|---|---|---|---|
| 0 (today) | $294,387 ($292,264) | none (-$5,613) | nothing | $0 | 0% |
| -25bp | $301,676 ($299,596) | $1,676 (none) | 4% of the 2033 payment | $1,751 | 1.2% |
| -50bp | $309,169 ($307,135) | $9,169 | 24% of the 2033 payment | $9,555 | 6.4% |
| -100bp | $324,793 ($322,864) | $24,793 | 63% of the 2033 payment | $25,711 | 17.1% |
| -150bp | $341,313 | $41,313 | all of 2033 + 2% of 2034 | $42,633 | 28.4% |
| 2026 worst day (Feb 27) | $327,631 ($325,563) | $27,631 | ~71% of the 2033 payment | $28,549 | 19.0% |

- **Break-evens:**
  - a gap opens below -19bp (Nov-15 ladder) or -26bp (exact-date);
  - the gap exceeds one whole payment below about -150bp;
  - the gap exceeds the whole 2028 deposit below -421bp (10-year about 0.96%).
- **Gap odds on 2027-01-01** (ASM: zero-drift lognormal, 2026 realised volatility 7.16-7.24% a year, 0.27 years):
  - P(gap) = 24.3% (exact-date) or 30.5% (Nov-15 ladder);
  - p90 gap $8.7k, p95 $12.9k, p99 $20.9k (Nov-15);
  - P(gap > one whole payment) = 0.01%.
- **[3] Longest-first versus nearest-first:** after a -100bp gap, a *further* -100bp during 2027 raises the Jan-2028
  top-up by +$1,265 (+5%) under longest-first, against +$3,831 (+15%) under nearest-first.
- **[7] All at once versus staged versus trigger** (ASM: cost relative to T-bills is zero-drift; starting funded ratio
  1.019):

  | Rule | Mean funded ratio | Chance under 1.00 | p5 |
  |---|---|---|---|
  | Buy all on the day | 1.019 | 0% (once bought) | 1.019 |
  | Four quarterly tranches | 1.021 | 27.3% | 0.966 |
  | Wait for a 5% margin, else buy at year-end | 1.022 | 26.5% | 0.912 |

  The "all at once" row takes the purchase-day curve as given; the uncertainty *before* the purchase day is the gap
  odds above, and every rule shares it.
- **[8] Joint tail:**
  - -50bp and no deposit: $11,957 of the first $50,000 payment unfunded (2.4% of $500k);
  - -100bp and no deposit: $31,413 (6.3%);
  - a $75k deposit covers every case down to the 2026 worst;
  - six months late (1 Jul 2028), with rates unchanged, the -100bp case needs +$531.
- **[5] Case PDF date (2026-09-10):** the Nov-15 ladder cost **$299,990** and the exact-date ladder $297,879. See
  finding 7: INTERPRETATION only.

### Implication (decision + one IPS rule; IPS, with one TN by-product)
**IPS: rules to fix before Nov 6.** These are the elements the team's own wording must contain; this is not drafted
text.
1. **Buy on arrival, in full.** The first deposit buys the ladder on 1 January 2027. There is no staging and no waiting
   for better yields. That would be a rate forecast, and the Guide says strategy is not rewritten "because markets
   move".
2. **Order: longest-dated payments first.** Reason in plain words: the piece left waiting is the smallest and least
   sensitive to rates, and it is the one needed soonest after the 2028 deposit arrives.
3. **Completion before growth.** Any unbought part is the first use of the 2028 deposit, before any growth
   investment. If the deposit is late or arrives in instalments, completion comes first from each instalment.
4. **Headline promise, rate-conditional:**
   - fully funded on 1 January 2027 if rates stay near today's;
   - otherwise fully funded on the day the second deposit arrives (1 January 2028 at the latest);
   - "fully funded" means the Treasuries are *bought*, not forecast.
5. **Stated maximum dependence:** in words, not a table (the IPS bans detailed calculations). Content: "at most part
   of the first payment, and about one-fifth of the 2028 deposit even on 2026's most expensive day".
6. **Joint tail, named once:** if rates fall sharply before January *and* the second deposit never comes, part of the
   first payment would be unfunded; every other payment is bought. This is the plan's known residual risk, and our
   own stress scenario (the case says "will").
7. **If rates rise instead:** the few thousand dollars left over wait in Treasury bills until 2028, then join the
   growth money. This is already in the ticket (§8).

- **For the elevator pitch** (≤50 words; the team's words): the one fact worth carrying is "the payments are bought
  first, with her own two deposits". Do **not** put "fits inside $300,000" in the pitch: it was false on 176 of 185
  days this year.
- **TN by-product (tier 1, optional):** if the team writes a reflection on the hedge trade, it may say the hedge was
  sized to what the first deposit buys at today's prices, with the top-up rule stated. No probabilities in a note.
- **Deadline tier:** 2 (IPS). **Confidence:** high on the direction (all at once, longest-first, completion first);
  medium on the odds (model ASMs).
- **Changes current strategy?** Refines it without reversing it (brief §7 already says longest-first plus a 2028
  top-up). Three changes:
  - the headline stops saying "fits inside $300k";
  - "completion before growth" becomes an explicit rule;
  - staging and triggers are explicitly rejected in the IPS.
- **Criterion served most:** Investment Strategy (a decision rule set before the surprise). Also Client Knowledge:
  Laura's 2028 income is her own career money, and she called self-employment "unstable income" (VP, but team
  knowledge only).
- **Is it "hers"?** INTERPRETATION, with low risk if kept internal. A person who sets deadlines "finished or not" is
  well served by a rule that acts on the day the money arrives, not one that waits for a better price. Do not present
  this as her investment view (D13: no verified statement about investing exists).
- **What this teaches:** when a promise is priced by today's market, "can we afford it?" has a date attached. Write the
  rule for the unlucky day before it happens. Leave the part most exposed to rates as small and as short as possible,
  and never wait for a better price on money that already has a job.

---

## Already answered / mis-posed notes
- M004's member hypotheses asked for "FR sentence" and "re-run the surplus at the 2026-average curve" items. Those are
  Final-Report or D3-model work and are outside this scope (brief §17). Logged below.
- M044's "which maturities does WInS offer" cannot be answered from public sources. It is correctly a logged-in check
  (R-AN48), now with a symbol format and a fallback order.

## Later (after Nov 9), one line each
- FR: say that part of today's surplus reflects unusually high September 2026 yields; D3 to re-run the surplus on the
  2026-average curve.
- FR: joint-tail sensitivity line and the break-even rate falls ($ table above).
- FR: optional practice analogy (APRA SPS 160 shortfall limit / restoration period) if it earns its place.

## Sources
- Case and guides (VRF): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (p.2 L43-65, p.3 L88-92,
  p.4 L129); `2026_WGY_Investment_Competition_Guide.txt` p.5; `2026_WGY_Investment_Policy-FINAL.txt` L51.
- SMApply Trading Details and FAQ (VP, 2026-09-27, via case_register R-W65-R-W92):
  https://wghsinvcomp.smapply.us/res/p/trading/ ; https://wghsinvcomp.smapply.us/res/p/faqs/
- 2026-27 WInS User Guide (VP, re-read 2026-09-28):
  https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf
- Stock-Trak bond pages (VP content, generic, 2019; read 2026-09-28): https://www.stocktrak.com/available-bonds/ ;
  https://content.stocktrak.com/what-are-bonds/ ; https://www.stocktrak.com/investments-bond-analysis-trading-project/
- iShares IBTM (VP, read 2026-09-28): https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf
- Treasury par curves 2026 (VP snapshot by D3): `research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv`;
  `competition/official_market_data/daily-treasury-rates_2026-09.csv` (VRF).
- MSPD Table V (VP per S1): `research/insight_v1/wins_now/S1_mspd_table5_2026-08-31_fixed_2032plus.csv`.
- APRA SPS 160 (VP, 2026-09-28): https://handbook.apra.gov.au/standard/sps-160
- U.S. rating (SNIP, secondary, 2026-09-28): https://en.wikipedia.org/wiki/United_States_federal_government_credit-rating_downgrades
- Repo research (VRF): `wins_now/securities_and_allocation_v0.md`, `S1_treasury_sleeve.md`,
  `S3_final_report_ladder_and_reserve.md`, `S4_red_team.md`, `phase_A/fact_register.md` (F-101-F-117, F-206,
  F-605-F-608), `phase_A/wins_week1_guardrails.md`, `phase_D/D13a_laura_quotes_verified.md`.

## What this teaches
1. **Behave versus keep.** Bond funds that roll forever can *move like* Laura's payments. Only a bond with a date can
   *pay* one. One visible rung explains the plan faster than a paragraph about duration.
2. **A promise priced by the market has a date on it.** $300,000 bought the real Nov-15 ladder on only 9 of 185 trading days this year (12 for exact-date zeros). The
   honest plan says what happens on the other days, and makes the part that has to wait as small and as short as
   possible.
3. **Waiting is a forecast.** Buying in stages or on a trigger feels careful, but with a fixed promise it only adds a
   chance of falling short, for almost no expected gain.
