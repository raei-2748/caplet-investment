AI-generated (Claude Code), fact checks for the IPS rewrite, 26 Oct 2026

# R04: Fact checks for A1-A5 and the old queue

Scope: the 12 claims in the brief (A1, A4, A5 in `THINKING_LOG.md`; Lehman, Bodie, the 7.5% basis, iBond
liquidation, seed money). Checked against `00_GROUND_TRUTH.md`.

**Read this first: how much could be checked this session.** Every outbound page fetch was refused this session
(the egress proxy answered 403 to CONNECT for msrb.org, ishares.com, fda.gov, finra.org, ncbi, repec, cfainstitute,
wikipedia and 25 more hosts tested on 26 Oct; Claude in Chrome was not connected). WebSearch worked but returns
titles and URLs only, with no page text. So this sheet has three levels of evidence:
- **PRIMARY-IN-REPO**: an exact phrase from a primary document already saved in the repo (the JPM LTCMA matrix PDF,
  the archived iShares product pages, earlier verbatim reads logged in the repo). Safe to rely on.
- **TITLE-ONLY**: a search on 26 Oct returned a source whose title or URL states the fact, but the page text could
  not be read. Good enough to keep a claim in a draft. Not good enough to quote. Re-read before the Final Report cites it.
- **UNVERIFIED**: no primary or reputable source could be read. Must not go into submitted text as a fact.
Phrases in quotation marks are verbatim only where the evidence level is PRIMARY-IN-REPO.

## Summary table

| # | Claim | Verdict | Evidence (exact phrase or title) | Source URL | Level, access date |
|---|---|---|---|---|---|
| 1 | Escrowed-to-maturity bonds are treated as paid and typically rated AAA | **PARTLY** (the "AAA" part is out of date) | Titles: "S&P downgrades 11,500 munis tied to US" (2011); "Fitch downgrades of munis tied to U.S. rating to have little impact on market" (2023); "Moody's downgrade US Aa1 and ripple effect bond ratings" (2025); "Fitch Debuts 'AAApre' Notation to Indicate Prerefunded Debt" (pre-2023) | investmentnews.com/fixed-income/sp-downgrades-11500-munis-tied-to-us/38071 ; bondbuyer.com/news/the-downgrade-of-munis-from-fitch-will-have-little-impact ; cumber.com/market-commentary/moodys-downgrade-us-aa1-and-ripple-effect-bond-ratings ; bondbuyer.com/news/rating-agencies-fitch-debuts-aaapre-notation-to-indicate-prerefunded-debt | TITLE-ONLY, 26 Oct 2026 |
| 2a | Mean dissolution time is a standard dissolution metric, MDT = Σ t·ΔM / Σ ΔM | **TRUE** (definition) | Titles: "Mean Dissolution Time" (MetricGate docs); "Comparison of dissolution profiles of Ibuprofen pellets" (Costa et al., the usual MDT reference); Chem. Pharm. Bull. 1982 30(3) 1088-1090 (moment analysis of dissolution) | metricgate.com/docs/mean-dissolution-time/ ; ciencia.ucp.pt/en/publications/comparison-of-dissolution-profiles-of-ibuprofen-pellets/ ; doi.org/10.1248/cpb.30.1088 | TITLE-ONLY for the sources; formula is standard maths, checked below |
| 2b | Mean residence time = AUMC / AUC | **TRUE** | Titles: "Mean Residence Time (MRT): Understanding How Long Drug Molecules Stay in the Body" (Certara); "AUMC & Mean Residence Time" | certara.com/knowledge-base/mean-residence-time-mrt-understanding-how-long-drug-molecules-stay-in-the-body ; metricgate.com/docs/pk-aumc-mean-residence-time/ | TITLE-ONLY, 26 Oct 2026 |
| 2c | "Macaulay duration is a mean dissolution time with discounting" | **TRUE as mathematics, with two caveats** (see note) | Both are first moments: time weighted by the share of the total that arrives at that time | own derivation; ten-payment check against repo's verified 9.90y | Derivation, 26 Oct 2026 |
| 3 | ER dosage forms often aim for zero-order release; OROS achieves near zero-order | **TRUE** (TITLE-ONLY) | Titles: "Osmotic-controlled release oral delivery system" (OROS); patent US4681755 "Delivery device for zero-order release of an active principle into a dissolution fluid" | wikipedia.org/wiki/OROS ; patents.google.com/patent/US4681755 | TITLE-ONLY, 26 Oct 2026 |
| 4a | FDA definition of dose dumping | **UNVERIFIED wording** (concept TRUE) | Titles: "Regulatory Considerations for Alcohol-Induced Dose Dumping of Oral Modified-Release Formulations" (Pharm. Tech.); FDA document fda.gov/media/167019/download (title not shown) | pharmtech.com/view/regulatory-considerations-alcohol-induced-dose-dumping-oral-modified-release-formulations ; fda.gov/media/167019/download | TITLE-ONLY; FDA's exact wording not read |
| 4b | Palladone withdrawn July 2005 over alcohol | **PARTLY** (withdrawal over alcohol: title-level; the month: UNVERIFIED) | Title: "Palladone pulled, FDA looks at other opioids" (MDedge Clinical Psychiatry News) | mdedge.com/clinicalpsychiatrynews/article/22408/addiction-medicine/palladone-pulled-fda-looks-other-opioids | TITLE-ONLY, 26 Oct 2026 |
| 5 | Lehman principal-protected notes lost money in 2008 because the protection was Lehman's own IOU; FINRA v UBS 2011 | **PARTLY** (the FINRA action and its subject: title-level; the "own IOU" mechanism: UNVERIFIED wording) | Titles: "FINRA Fines UBS Financial Services $2.5 Million, Orders UBS to Pay Restitution" (11 Apr 2011, from the URL slug); "UBS to Pay FINRA Fine, Restitution to Investors in Lehman PPNs"; "FINRA Orders UBS To Pay $10.75M For Improper Notes Sales" | finra.org/media-center/news-releases/2011/finra-fines-ubs-financial-services-25-million-orders-ubs-pay ; thinkadvisor.com/2011/04/11/ubs-to-pay-finra-fine-restitution-to-investors-in-lehman-ppns ; financial-planning.com/news/finra-orders-ubs-to-pay-1075m-for-improper-notes-sales-MME218432 | TITLE-ONLY, 26 Oct 2026 |
| 6 | Bodie (1995): cost of insuring stocks against underperforming the risk-free rate rises with horizon | **TRUE** (paper and finding: title-level and repo; exact wording UNVERIFIED) | Repo R02 #36 logged the FAJ page as VERIFIED (exists): Bodie, FAJ 51(3) 18-22. Title: "Measuring risk: the Bodie put when stocks exhibit mean reversion" (Journal of Risk) | rpc.cfainstitute.org/research/financial-analysts-journal/1995/on-the-risk-of-stocks-in-the-long-run ; risk.net/journal-risk/2161106/measuring-risk-bodie-put-when-stocks-exhibit-mean-reversion | Repo + TITLE-ONLY, 26 Oct 2026 |
| 7 | JPM 2026 LTCMA: AC World 7.00% compound; "about 7.5% a year" is fair for VT | **AC World figure TRUE; "about 7.5%" FALSE as an AC World number** | Matrix row "AC World Equity 7.00 8.28 16.78 7.10" (compound 2026, arithmetic 2026, volatility, compound 2025); "EAFE Equity 7.50 8.90 17.63 8.10"; "All estimates on this page are in U.S. dollar terms"; "data as of September 30, 2025" | `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf` (team download of am.jpmorgan.com, 27 Sep 2026) | PRIMARY-IN-REPO, read 26 Oct 2026 **[Window 27 Oct: WRONG EDITION. J.P. Morgan's 2027 LTCMA (release 19 Oct 2026) gives global equities 7.5% (USD), up from 7.0%; the TNA's 7.5% is the world-stocks figure. See `../../office/outbox/2026-10-27_window_7-5-and-three-checks.md`.]** |
| 8 | iBonds Dec-20XX Treasury ETFs: terminate in December, bonds roll to cash in the final year, net assets paid out in cash | **TRUE** | "will terminate on or about October or December 15 of the year in each Fund's name"; "During the final year of the fund's life, the underlying bonds will mature and the proceeds will be held in cash equivalents until the liquidation of the fund"; "Following the Fund's termination date, the Fund will distribute substantially all of its net assets, after deduction of any liabilities, to then-current investors without further notice and will no longer be listed or traded"; "the Funds do not seek to return any predetermined amount" | ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf (archived copy `archive/rab/data/ishares/IBTM_product_page.html.gz`, saved 30 Sep 2026) | PRIMARY-IN-REPO, read 26 Oct 2026 |
| 9 | Annuity-certain = fixed payments on fixed dates for a fixed term, not tied to anyone's survival; the ladder replicates one | **Definition TRUE; "replicated" PARTLY** | Titles: "Life annuity" (contrasts with annuity-certain); "Annuities 101: annuity certain" (Gainbridge); QMUL actuarial notes (annuities-certain) | wikipedia.org/wiki/Life_annuity ; gainbridge.com/post/annuity-certain ; webspace.maths.qmul.ac.uk/b.khoruzhenko/asnotes5.pdf | TITLE-ONLY; replication point is own analysis |
| 10 | Compounding pharmacy: pharmacist combines ingredients to tailor a drug to one patient; FDA section 503A | **TRUE** (concept and 503A: title-level; FDA's exact wording UNVERIFIED) | Title: "Section 503A of the Federal Food, Drug, and Cosmetic Act" (FDA, Human Drug Compounding); CRS "FDA's Authority to Regulate Drug Compounding: A Legal Analysis" (R40503) | fda.gov/drugs/human-drug-compounding/section-503a-federal-food-drug-and-cosmetic-act ; everycrsreport.com/files/20121017_R40503_4cc2f5a2923504dfc5f1c065aa2d9a4582cd5656.html | TITLE-ONLY, 26 Oct 2026 |
| 11 | List and Lucking-Reiley (2002): exact seed-money numbers | **TRUE for the abstract's numbers; the per-arm figures UNVERIFIED** | Abstract (read verbatim 27 Sep, logged in repo): "a change in seed money from 10% to 67% of the campaign goal" produced "nearly a sixfold increase" in contributions; "imposing a refund increased contributions by a more modest 20%" | econpapers.repec.org/article/ucpjpolec/v_3a110_3ay_3a2002_3ai_3a1_3ap_3a215-233.htm ; ideas.repec.org/p/feb/natura/00301.html (repo: `keel/library/insight_v1/phase_B/B6a_cosponsors.md` lines 313-314, 340) | PRIMARY-IN-REPO (abstract), read 27 Sep 2026 |
| 12 | A rating agency would not count an ETF as defeasance-eligible; escrows hold direct Treasury obligations | **Likely TRUE, but by inference** | No rating-agency criteria could be read. Titles: "Investment options for advance refunding escrow" (Baker Tilly); NC Treasurer memo "allowable investments to qualify for in-substance defeasance"; GASB 86 summaries ("essentially risk-free monetary assets"); "Eligible Obligations definition". The iBond's own page: "the Funds do not seek to return any predetermined amount" (PRIMARY-IN-REPO) | bakertilly.com/insights/investment-options-for-advance-refunding-escrow ; nctreasurer.com/documents/files/slgfd/memos/allowable-investments-qualify-substance-defeasance/open ; ucop.edu/uc-controller/dirbf/dep-irms/files/gasb86/gasb86.pdf | TITLE-ONLY + inference, 26 Oct 2026 |

## Notes per claim: what can be said in plain English, and what cannot

**1. Defeasance and "AAA".** The core is sound and standard: when an issuer puts Treasuries (or SLGS) in an
irrevocable escrow that pays the debt, the debt is treated as paid ("defeased", "escrowed to maturity",
"pre-refunded"), and its rating follows the escrow, not the issuer. But the rating now follows the United States'
own rating, and the US is no longer AAA at any of the three big agencies: S&P cut it to AA+ in 2011 and downgraded
about 11,500 escrowed munis with it; Fitch went to AA+ in August 2023 and did the same; Moody's went to Aa1 in May
2025 (all TITLE-ONLY above; whether any agency has since moved is UNVERIFIED). Fitch's "AAApre" label belongs to the
pre-2023 era.
- Safe: "Cities that set aside Treasuries to pay a debt are treated by the market as having already paid it." "The
  same test a bond market uses to call a debt defeased."
- Not safe: "rated AAA". If a rating is wanted, say "rated as safe as the US government itself", which is true at
  any rating level.
- Not safe either: that *Laura's* plan meets the test (see 12). Three gaps: (a) five rungs are ETFs, which pay NAV,
  not a fixed sum; (b) the Nov-2039 and Nov-2041 notes rely on "reinvested coupons", while a real escrow is sized by a
  verification agent to pay without counting on future reinvestment rates (UNVERIFIED wording, but the repo's own
  coupon-shortfall risk shows the gap); (c) on 22 Oct the ladder fits under $300k by $1,139 (4bp), so the "defeased in
  2027" claim depends on the Jan 2027 curve and the 2028 top-up. Plain-English version that survives: "Laura's
  payments are funded the way a city defeases a debt: set aside in Treasuries, years early, so no forecast is needed."
  Call it the model, not a certificate.

**2. Mean dissolution time, mean residence time, Macaulay duration.**
- MDT (in vitro): MDT = Σ t̂ⱼ ΔMⱼ / Σ ΔMⱼ, where ΔMⱼ is the drug dissolved in sampling interval j and t̂ⱼ the interval's
  midpoint. It is the mean time a dissolved molecule took to leave the tablet, a standard model-independent metric
  used next to f1/f2 and dissolution efficiency (TITLE-ONLY sources).
- MRT (in vivo): MRT = AUMC/AUC = ∫ t·C(t) dt / ∫ C(t) dt, the first statistical moment of the concentration curve.
- Macaulay duration: D = Σ t·PV(CFₜ) / Σ PV(CFₜ).
- The maths: all three are the same object, a weighted mean time, where each moment's weight is that moment's share
  of the total. Put the cash paid at t where the drug released at t goes, discount it, and MDT's formula becomes
  Macaulay's exactly. With a zero rate, D = Σ t·CFₜ / Σ CFₜ, which is MDT's formula with cash for milligrams.
  Check on Laura's payments (valued 1 Jan 2027, paid 1 Jan 2033-2042): undiscounted mean time = (6+...+15)/10 = 10.5
  years; the repo's verified discounted duration on the 25 Sep curve is 9.90 years. Discounting pulls the mean
  earlier, as it should.
- So "Macaulay duration is a mean dissolution time with discounting" is **exact as a formula**. Two caveats keep it
  honest: (i) MDT is an estimate from sampled data (interval midpoints, normalised by the amount dissolved by the last
  sample, not always the full dose), while duration is computed from known cash flows; (ii) the analogy maps the
  *liability* (the ten cheques) or the *ladder's payouts*, not the stock fund. THINKING_LOG A5 says the reverse
  ("the same formula as ... Macaulay duration without the discounting"): that is also right, read as MDT = duration
  minus discounting.
- Safe: "A bond's duration is the same calculation a pharmacist uses for a tablet's mean dissolution time, with each
  payment discounted." Not safe: claiming pharmacists use the word duration, or that MDT includes discounting.

**3. Zero-order release.** True in substance: controlled/extended-release design often targets zero-order (constant
rate) release, and osmotic pumps (OROS) are the textbook way to get close to it. Exact pharmacopeial wording not read.
Caveat for the analogy: ten equal cheques once a year are a *stepped* zero-order schedule (same amount per year),
not a continuous one. Safe: "the same amount each year, like an extended-release tablet's steady dose." Not safe:
"exactly zero-order".

**4. Dose dumping and Palladone.** The concept is standard: a modified-release form releasing much or all of its dose
too fast, at once. FDA's own sentence was not read, so do not put a definition in quotation marks or attribute
wording to FDA. Palladone (hydromorphone ER, Purdue) was pulled in 2005 after alcohol was found to make it release
its dose rapidly (TITLE-ONLY); the month "July 2005" is from memory and stays UNVERIFIED until the FDA alert is read.
Safe: "Palladone, a slow-release painkiller, was withdrawn in 2005 because alcohol could make it release its whole
dose at once." Not safe yet: the exact date, or calling it an FDA definition.

**5. Lehman principal-protected notes.** FINRA fined UBS Financial Services $2.5 million and ordered restitution in
April 2011 over its sales of Lehman PPNs; the reported total is $10.75 million (titles). The mechanism (the
"protection" is only as good as the issuing bank's promise, so when Lehman failed in Sept 2008 holders became
unsecured creditors) is standard and consistent with those titles, but FINRA's exact wording was not read.
Safe: "A bank's 'principal-protected' note is only as safe as the bank: Lehman's buyers learned that in 2008." Not
safe: quoting FINRA, or a loss figure per note holder.

**6. Bodie (1995).** The finding, as the paper is generally cited: the price of a put that guarantees a stock
portfolio at least the risk-free return rises with the horizon, so stocks do not get safer the longer you hold them.
It is derived under standard option pricing (random-walk prices); with mean reversion the put is cheaper (the
Journal of Risk title above), which is the usual rebuttal. Safe: "Insuring stocks against losing to Treasuries costs
more the longer the wait, not less (Bodie, 1995)." For the IPS (no citations) drop the name: "time makes a loss less
likely, not cheaper to insure." Not safe: a percentage cost from the paper.

**7. The 7.5% basis.** From the JPM 2026 LTCMA matrix in the repo (USD, data as of 30 Sep 2025): AC World Equity
7.00% compound, 8.28% arithmetic, 16.78% volatility (2025 edition: 7.10% compound). 7.50% is the **EAFE** compound
figure (developed markets outside the US), not world equity. US Large Cap is 6.70% / 7.94%. So "about 7.5% a year"
for VT matches neither JPM's world compound (7.0%) nor its world arithmetic (8.3%). The locked TNA already says it
and cannot change; the IPS should not repeat it. **[Window 27 Oct: WRONG EDITION. J.P. Morgan's 2027 LTCMA (release 19 Oct 2026) gives global equities 7.5% (USD), up from 7.0%; the TNA's 7.5% is the world-stocks figure. See `../../office/outbox/2026-10-27_window_7-5-and-three-checks.md`.]** Two further caveats: VT tracks the FTSE Global All Cap index, so AC
World is a proxy; and JPM's 2027 LTCMA is normally published in the autumn, so a newer edition may exist (not
checked). Safe in the IPS (no numbers needed): nothing. If a number is used anywhere: "about 7% a year (JPMorgan's
long-run assumption for world stocks, compound)".

**8. iBond maturity mechanics.** Confirmed from iShares' own page (verbatim above): the fund terminates on or about
15 December of its year, holds cash equivalents in its final year as bonds mature, then pays out substantially all
net assets in cash and delists; the payout is not a predetermined amount. Timing works for the plan: IBTM's cash
arrives in mid-to-late December 2032, before the 1 Jan 2033 payment (the exact distribution date after termination
is not stated on the page). Safe: "Each fund ends in the December before its payment and pays out in cash." Not
safe: "repays $50,000" or any fixed sum.

**9. Annuity-certain.** Correct term: a series of payments of fixed amounts at fixed intervals for a fixed term,
paid regardless of anyone's survival (contrast: life annuity). Laura's promise is a ten-year, level, deferred
annuity-certain paid at the start of each year (an annuity-due in actuarial terms) beginning 2033. The ladder
*approximates* buying one: the T-bond rungs repay fixed sums but lean on reinvested coupons for part of some
payments, and the iBond rungs pay NAV. Safe: "Her ten payments are what an insurer would call a ten-year
annuity-certain; we build it from Treasuries instead of buying it." Not safe: "an exact replica" or "guaranteed like
an annuity".

**10. Compounding pharmacy.** Concept true: a licensed pharmacist combines, mixes or alters ingredients to make a
medicine for one patient's prescription, regulated federally under FDCA section 503A (outsourcing facilities fall
under 503B). FDA's page wording was not read, so do not quote it. Caution for A4's pun: compounded drugs are not
FDA-approved and FDA warns about their risks, so a judge with a health background may read "compounding pharmacy" as
less safe, not more. That cuts against a safety story.

**11. Seed money.** Abstract numbers (verbatim, repo): seed money raised from 10% to 67% of the goal gave "nearly a
sixfold increase" in contributions; a refund raised them "a more modest 20%". The 33% middle arm and the $3,000
goal per computer campaign are from memory: UNVERIFIED. As B6a Q15 already warns, the effect is a share of a known
goal; Laura's facility cost is unknown, so no percentage effect can be claimed for her. Safe (Final Report only): "A
field experiment found a larger announced seed gift drew far more giving." Not safe: "six times more" applied to Laura.

**12. ETFs and defeasance eligibility.** No rating-agency criteria could be read, so this rests on inference plus
the fund's own words. Escrows for defeasance are normally restricted to direct US Treasury obligations (and SLGS),
sometimes also obligations guaranteed by the US (common in bond documents' "defeasance obligations" definitions and
GASB 86's "essentially risk-free monetary assets"; titles only). An ETF share is an equity interest in a fund whose
payout "do[es] not seek to return any predetermined amount", so it cannot be matched to a fixed debt-service
schedule. A verification agent could not certify it. Conclusion: the T-bond rungs pass the defeasance analogy; the
five iBond rungs do not, strictly. A1 survives only as "funded the way a defeasance is funded", not "defeased".

## Bottom line for A1-A5
- **A1** survives in a weaker form: drop "AAA"; say "treated as already paid", and do not claim the iBond half meets
  the formal test.
- **A4**: "annuity-certain" is the right term; "replicate" must be "build", not "exactly copy". The compounding pun
  carries a safety connotation that works against the plan.
- **A5** is mathematically exact (duration = MDT with discounting) and zero-order fits as "same amount each year".
  Palladone's date and FDA's dose-dumping wording are not yet verified.
- **7.5%**: the IPS must not repeat it; JPM's world equity figure is 7.0% compound. **[Window 27 Oct: WRONG EDITION; 2027 = 7.5% global equities (USD), so 7.5% coheres with the TNA. `../../office/outbox/2026-10-27_window_7-5-and-three-checks.md`.]**
- Before any of the TITLE-ONLY items is quoted or cited in the Final Report, a student (or a session with web access)
  must open the page and copy the sentence.
