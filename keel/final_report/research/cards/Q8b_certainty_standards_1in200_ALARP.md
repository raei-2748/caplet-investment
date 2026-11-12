# Q8b research cards: "a high degree of certainty" against regulators' numbers (Solvency II 1-in-200, HSE's tolerability of risk and ALARP, rating agencies' default tables)

Date: Thu 12 Nov 2026 (Sydney morning; US Wed 11 Nov). Worker W-q8b.
Report parts: 3a (the commitment and its standard), 3c (confidence words), 3e (limits: the US default exception; Table 3), 3d (only as background for what co-sponsors bear).

Notes for the Final Report store, not report prose.

Claims tested:
1. Keep, kill or change: "Laura's standard (all ten payments are paid even if interest earns nothing, barring a US default)
   is stricter than Solvency II's 1-in-200 (99.5% value-at-risk over one year)."
2. Keep, kill or change: "ALARP (as low as reasonably practicable, HSE's R2P2, 2001) gives Laura the words for why she
   stops where she does: no safer dollar asset exists, a bank adds bank risk, a second sovereign adds currency risk."
3. Keep, kill or change: "A rating agency's idealised default table gives the best plain number for 'barring a US
   default' over 2033-2042."

Problem class: stating a structural near-certainty that has one named residual, against the numeric standards that
regulators use when they must put a number on "safe enough". Fields that solved it: insurance prudential regulation
(EU Solvency II: a one-year 99.5% quantile of own-funds loss, with policy zeros for some sovereigns); UK safety
regulation (HSE's tolerability of risk framework, ALARP and the gross-disproportion test from case law); credit rating
(agency default definitions, idealised benchmark tables, observed default studies). Q4c already sized the default
exception from CDS prices; this card does not re-card it (Q4c rows 28-33) or the likelihood-word ladders (Q4c) or the
escrow and refunding analogies (Q31). Engineering codes (Eurocode reliability) are left to worker W-q8a.

## Verdicts in one screen

1. **Claim 1: CHANGE. "Stricter" is true only for the risks her test covers, and says nothing about the one it excludes.**
   - Rates and reinvestment: stricter by construction. From 30 Jan 2027 the Solvency II down shock is
     r(1 - s) - b by maturity (C(2025) 7206). On the NUMBERS 0 curve that is a fall of about 2.4-2.6 points at 5-10
     years and 3.7 points at 1 year (Keel arithmetic; Treasury par yields stand in for the insurer's swap-based curve).
     Her test takes every rate to zero for good, a fall of 4.3-5.3 points. NUMBERS 2 (MODEL): $0 short at 1, 2 or 3
     points lower for good, and $0 at 0% with $1,414 spare.
   - The US default: no comparison is possible. Solvency II's standard formula charges a US Treasury 0% spread risk and
     0% concentration risk: a third-country central government, own currency, credit quality step 1 at AA+/Aa1
     (Delegated Reg. 2015/35 Art. 180(3), 187(4); Implementing Reg. 2016/1800). Both standards carve out the same event.
   - Horizon and method differ:
     - Solvency II is one year with recapitalisation; 1 in 200 each year for ten independent years is about 1 in 20
       (4.9%, Keel arithmetic). Hers runs the whole life of the payments with no fresh money after 2028.
     - Solvency II is a model quantile (value-at-risk). Hers is a deterministic scenario that the holdings pass by
       construction (CANON A4: structural, not a probability).
   - Solvency II also charges operational risk (Art. 101(4)). Her test does not size it (custody, fund frictions).
   - On a market measure, the standoff-year CDS figure of 4-6% (Q4c) is 8 to 12 times 1 in 200. Quiet years at
     0.2-0.4% are 1 in 250 to 1 in 500, the same order as 1 in 200. Those figures price a likely-cured late payment,
     not a loss of capital.
2. **Claim 2: CHANGE. Keep the shape; kill the numbers; rename the reason she stops.**
   - Keep the shape from R2P2: a tolerable residual, never called "acceptable", kept as low as reasonably practicable
     and periodically reviewed (paras 122-124). That review is what Table 3 does.
   - Kill HSE's numbers. They are each person's yearly chance of death. CDS-implied 0.2-0.4% a year is 2,000-4,000 in a
     million, above even the workers' limit of 1 in 1,000. That would read as "intolerable" for a risk that is in fact
     a likely-cured delay.
   - The reason she stops is risk transfer, HSE's own term (SPC/Permissioning/39: an added risk to others "should be
     offset against the benefits"), not gross disproportion of cost. Each alternative moves risk elsewhere:
     - A bank adds bank risk above FDIC's $250,000 per depositor, per bank, per ownership category, and FDIC's fund
       is itself "backed by the full faith and credit of the United States government".
     - A second sovereign adds currency risk, which Solvency II stresses at 25% (Art. 188).
   - Where ALARP truly bites is on the small residuals. Both measures below are cheap, so ALARP would require them:
     - moving money into bills before a named X-date (Table 3 row 3);
     - the custody set-up ($589,655 at the end against SIPC's $500,000, SKELETON).
3. **Claim 3: CHANGE, and KILL the idealised table.**
   - Moody's idealised table (Aaa 0.01%, Aa1 0.10% at 10 years) is a 1989 benchmark for structured-finance models,
     "not intended to match historical or future ratings performance", and never revised.
   - The right observed record for US debt is local currency, not foreign currency. S&P 1993-2024, AA in local
     currency: 0.00% cumulative default for 1 to 10 years, then 0.37% at 11 years and 2.24% at 15. Those are two
     defaults: Cyprus 2013 and Barbados 2018, each about 17-19 years after its first AA rating.
   - Laura's Treasuries are held about 6 to 15 years (Jan 2027 to the 15 Nov 2041 bond), so "ten-year" undersells
     her last five payments.
   - Q4c's "0.00% at 1-15 years" is the foreign-currency table. For US debt it holds only to 10 years.
   - Use in the report:
     - the definition first: five business days, which is S&P's test; Moody's counts any delay past a contractual
       grace period, and Treasuries have none;
     - then the rating record as context only (none within ten years, small samples);
     - then Q4c's CDS figures as an upper bound for a late payment.
     - No single ten-year probability.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Solvency II's "1 in 200": the capital requirement is set "so that ruin occurs no more often than once in every 200 cases", that is a 99,5 % probability of meeting obligations "over the following 12 months" | Directive 2009/138/EC, recital 64 | CERTAINTY | TEXTBOOK | The reference point the claim borrows: one year, whole company, a calibration target | A calibration aim for a capital model, not a promise that each policy is paid; recapitalisation is assumed after the year | VERIFIED (recital 64 read, EUR-Lex OJ text) | no | EUR-Lex |
| 2 | The requirement is the value-at-risk of basic own funds at 99,5 % over one year; it covers "all quantifiable risks", existing business plus 12 months of new business, and "only unexpected losses" on existing business | Directive 2009/138/EC, Art. 101(3) | CERTAINTY | TEXTBOOK | "1 in 200" is the size of a one-year loss of capital, not a statement about each promise being paid | Value-at-risk says how large a 1-in-200 loss is, nothing about the loss beyond it | VERIFIED (Art. 101 read, consolidated text 9 Jul 2018) | no | EUR-Lex |
| 3 | The standard covers non-life, life and health underwriting, market, counterparty default and operational risk; each module is calibrated at the same 99,5 % one-year level; counterparty default is over "the following 12 months" | Directive 2009/138/EC, Art. 101(4), 104(4), 105(6) | CERTAINTY, PROCESS | KNOWN | Solvency II puts a capital number on operational risk; Laura's test does not size hers (custody above SIPC cover, fund frictions, the funds' net asset value). So "stricter" fails on these | CANON C9 already names those residuals; they are named and sized as money, not as a probability | VERIFIED (articles read) | no (CANON A6 scopes "take none" to "these promises") | EUR-Lex |
| 4 | The regulator uses two lines: the capital requirement at 99,5 % and a minimum requirement calibrated at 85 % over one year (about 1 in 7) | Directive 2009/138/EC, Art. 129(1)(c) | CERTAINTY, TWOREASONS, PROCESS | KNOWN | A regulator's own two tiers: one to watch, one to act. Table 3 has the same shape (look closer; act) with only two events that change the plan | The minimum is a supervisory intervention point, not a client promise; Laura's two reasons are defined events, not quantiles | VERIFIED (Art. 129 read) | no | EUR-Lex |
| 5 | An internal model may use another time period or risk measure if it gives policyholders an equivalent level of protection | Directive 2009/138/EC, Art. 121-122 | CERTAINTY | NICHE | The regulator itself treats "99.5% over one year" as one way to state a protection level, not the only one; Laura states hers over the whole life of the payments | Equivalence must be shown with a model and approved; Laura's is a construction | VERIFIED (articles read) | no | EUR-Lex |
| 6 | EU member states' central governments in their own currency: 0% spread-risk stress and 0% concentration factor | Delegated Reg. (EU) 2015/35, Art. 180(2), 187(3) | CERTAINTY | KNOWN | The home sovereign is treated as default-free by rule, not by model | A policy choice, not an estimate; critics of the sovereign zero (ESRB, Basel Committee) were not read here | VERIFIED (legislation.gov.uk "as adopted"; EIOPA rulebook, Art. 180 updated 12 Jul 2024) | no | legislation.gov.uk; eiopa.europa.eu |
| 7 | Third-country central governments, "denominated and funded in the domestic currency", with an agency rating: credit quality step 0 or 1 gets a 0.0% spread stress at every duration (step 2: 1.1% x duration up to 5 years) | Delegated Reg. (EU) 2015/35, Art. 180(3) | CERTAINTY, LADDER | NICHE | A US Treasury held by an EU insurer carries no spread charge at all | Same policy zero as row 6; it says what the rule-maker chose, not what the risk is | VERIFIED (table in the "as adopted" text; EIOPA rulebook) | no | legislation.gov.uk |
| 8 | The same exposures: concentration factor 0% at steps 0-1, then 12%, 21%, 27% and 73% at steps 2, 3, 4 and 5-6; a generic exposure pays 12% even at steps 0-1 (Art. 186), above a 3% threshold (Art. 185) | Delegated Reg. (EU) 2015/35, Art. 185-187(4) | CERTAINTY, LADDER | NICHE | An insurer may put its whole book in US Treasuries with no concentration charge; Laura's single-issuer book is what the rule-maker itself allows | Concentration in one issuer is still the one risk left; the rule simply declines to price it | VERIFIED (articles read) | no | legislation.gov.uk |
| 9 | Rating map: S&P AA+, AA, AA- and Moody's Aa1-Aa3 are step 1; AAA/Aaa step 0. So the US (AA+, Aa1) is step 1 and its Treasuries carry 0% spread and 0% concentration charge. The 2025 Moody's downgrade moved it from step 0 to step 1 and changed no charge; a charge starts only in the single-A range (Keel reading of the map) | Implementing Reg. (EU) 2016/1800, Annex (consolidated to 22 Jul 2024); Q4c row 33 for the current ratings | CERTAINTY, TWOREASONS | NICHE | The key fact for claim 1: both standards exclude the same event, so "stricter" cannot be tested on the US default | The second-best-rating rule when ratings differ (Art. 4 of 2015/35) was not read | VERIFIED (Annex read) | no | EUR-Lex |
| 10 | From 30 Jan 2027 the interest-rate down shock becomes r(1 - s) - b by maturity: 1 year s 58%, b 1.16%; 5 years 40%, 0.71%; 7 years 37%, 0.63%; 10 years 40%, 0.61%; 20 years 50%, 0.50%; 30 years 53%, 0.41%; floors near -1.25%. Today's rule is a relative fall, nil for negative rates | Commission Delegated Regulation C(2025) 7206 final/2, Art. 167 as amended; EIOPA (2026, 15 Jul) for the date; EIOPA rulebook Art. 167 (updated 27 Mar 2024) | CERTAINTY, REINVEST | NICHE | The insurer's 1-in-200 fall in rates, in the year Laura's plan starts | The current table's values were images and were not read; the Official Journal number (2026/269) comes from a law-firm briefing only | VERIFIED (Commission text and EIOPA release read) | no | ec.europa.eu; eiopa.europa.eu |
| 11 | That shock on the NUMBERS 0 curve: 10 years 4.86% to 2.31% (a fall of 2.55 points); 7 years 4.74% to 2.36% (2.38); 5 years 4.64% to 2.07% (2.57); 1 year 4.33% to 0.66% (3.67). Laura's test takes every rate to zero for good, a fall of 4.3-5.3 points | Row 10; NUMBERS 0 (curve, 6 Nov 2026); Keel arithmetic | CERTAINTY, REINVEST, LADDER | NICHE | On rates and reinvestment her test is the limit case of the insurer's one-year shock, held for the whole life. NUMBERS 2 (MODEL): $0 short at 1, 2 or 3 points lower for good; $0 at 0% with $1,414 spare | Insurers use a swap-based curve with a credit adjustment, not Treasury par yields; their shock is instant and on value, hers is a path of cash | VERIFIED (inputs read; arithmetic checked) | no | NUMBERS 0, 2; this card |
| 12 | One year against the whole life: an insurer meeting 1 in 200 every year for ten independent years fails about 4.9% of the time (about 1 in 20); for fifteen years, 7.2% | Recital 64; Keel arithmetic (1 - 0.995^10; 1 - 0.995^15) | CERTAINTY, PRESENTATION | NICHE | The honest horizon point: the insurer's yearly standard compounds; Laura's test is stated once, for 2033-2042, with no fresh money after 2028 (case) | Insurers recapitalise and years are not independent; this illustrates a horizon gap, it does not estimate anything | VERIFIED (arithmetic) | no | This card |
| 13 | A model against a construction: Solvency II's number is a quantile of a modelled loss; Laura's is a deterministic scenario test (a stress test) that her holdings pass because the cash is owned before it is needed | Art. 101(3); CANON A4; NUMBERS 2 | CERTAINTY, LADDER | KNOWN | Name it a scenario test, not a value-at-risk; there is no "99.5%" in her standard to compare | A construction can fail through what it assumes away (the default, net asset value, custody); CANON C9 names them | VERIFIED (texts read) | no | This card |
| 14 | Q4c's CDS figures set against 1 in 200: quiet years 0.2-0.4% a year (1 in 250 to 1 in 500); 2024-25 about 1% (1 in 100); standoffs 4-6% (1 in 25 to 1 in 17, 8 to 12 times 1 in 200) | Q4c rows 28-30; Keel arithmetic | CERTAINTY, TWOREASONS, MOVE2031 | NICHE | Outside a standoff, the market price of a late US payment sits near an insurer's whole-company yearly tolerance; inside one, far above it | Different events: CDS is risk-adjusted and mostly prices a technical, cured delay (Q4c row 29); Solvency II's is a loss of own funds | VERIFIED (Q4c rows read; arithmetic) | no | Q4c; this card |
| 15 | Currency risk: the standard formula stresses each foreign currency by an instant 25% rise and 25% fall against the local currency | Delegated Reg. (EU) 2015/35, Art. 188(3)-(4) | CERTAINTY, LADDER | NICHE | The regulator's own size for the risk Laura would add by moving payment money into another sovereign's bonds, with payments fixed in US dollars | A capital stress, not a forecast of the exchange rate | VERIFIED (Art. 188 read, "as adopted") | no | legislation.gov.uk |
| 16 | HSE's tolerability of risk: three regions (unacceptable, tolerable, broadly acceptable); "'tolerable' does not mean 'acceptable'"; a tolerable risk is borne only if residual risks are "kept as low as reasonably practicable" and "periodically reviewed"; built on HSE's 1988 paper on nuclear power stations | HSE (2001), R2P2, paras 122-124 and the summary | CERTAINTY, TWOREASONS, PROCESS | TEXTBOOK | The shape of Laura's standard: the US default is a tolerated residual, never called acceptable, watched in Table 3 | Built for risks to life from work activities; HSE says it holds numerical criteria only for fatalities | VERIFIED (R2P2 read in full, gov.uk copy) | no | assets.publishing.service.gov.uk |
| 17 | HSE's numbers: about 1 in a million a year is the line between broadly acceptable and tolerable; 1 in 1,000 a year is the limit of tolerable for workers; 1 in 10,000 a year for the public; background risk about 1 in 100 a year over a lifetime | HSE (2001), R2P2, paras 130-132 | CERTAINTY | TEXTBOOK | None as numbers (row 19); they show only that a regulator states a band, not a point | They are each person's yearly chance of death; Laura's residual is a late or missed dollar payment | VERIFIED (paras read) | no | R2P2 |
| 18 | The public's limit is ten times tighter because the risk is "imposed" on them "in the wider interest of society"; workers choose theirs | HSE (2001), R2P2, para 132 | COSPONSOR, CERTAINTY | KNOWN | Laura chooses her residual; co-sponsors and the residency rely on it without choosing it. So the words to co-sponsors carry the residual plainly (3d) | Co-sponsors bear a delayed contribution, not harm; they also choose whether to rely on her figure | VERIFIED (para read) | no | R2P2 |
| 19 | The numbers do not transfer: CDS-implied 0.2-0.4% a year is 2,000-4,000 in a million a year, above even the workers' limit of 1,000 in a million; standoffs are 40,000-60,000 in a million | R2P2 paras 130-132; Q4c rows 28-30; Keel arithmetic | CERTAINTY, PRESENTATION | NICHE | Borrowing HSE's numbers would make Laura's residual look "intolerable" when it prices a likely-cured delay. Kill any numeric ALARP line | Unlike measures: a risk-adjusted market price of a delay against a real-world chance of death | VERIFIED (arithmetic on read sources) | no | This card |
| 20 | Gross disproportion: weigh the "quantum of risk" against the "sacrifice, whether in money, time or trouble"; if there is "a gross disproportion between them", the duty is discharged (Edwards v National Coal Board, 1949) | HSE (2001), R2P2, Appendix 3, paras 4-5, quoting Edwards v National Coal Board [1949] 1 All ER 743 | CERTAINTY, PROCESS | TEXTBOOK | The legal test behind "why stop here"; for Laura it fits the small residuals (row 26), not the default (row 23) | The judgment itself was not read, only HSE's quotation | VERIFIED (as quoted in R2P2; judgment not read) | no | R2P2 |
| 21 | HSE's working rule: a proportion factor (cost over benefit) of at least 1, with 10 suggested as an upper value; infinite in the intolerable region and zero in the broadly acceptable one; if cost is not shown to be grossly disproportionate, "the Operator is duty bound to implement that measure"; value of a prevented fatality about GBP 1.65m (2008) | HSE (2023), SPC/Permissioning/37 | PROCESS | NICHE | The burden sits with the duty-holder: a cheap measure is done unless shown grossly disproportionate | Built for major-hazard sites; money against lives | VERIFIED (HSE page read) | no | hse.gov.uk |
| 22 | Risk transfer: "If a measure results in a transfer of risk to other people, the added risk to those people should be offset against the benefits the measures provide"; factor at least 1 (perhaps 2) near the broadly acceptable line, at least 10 at the intolerable line; "the disproportion must always be gross"; estimates may be uncertain by "an order of magnitude or more" | HSE (2026), SPC/Permissioning/39 | CERTAINTY, LADDER | NICHE | The honest name for why Laura stops: every alternative to Treasuries moves risk elsewhere, so the net benefit is negative before cost is weighed | HSE's example is storage (drums against bulk); here the "other people" are Laura and her co-sponsors themselves | VERIFIED (HSE page read) | no | hse.gov.uk |
| 23 | No measure removes the default without adding a risk: no US-dollar asset is safer than a Treasury, and the alternatives in rows 24-25 move risk rather than cut it. So the default sits outside ALARP's cost test; it is a risk-transfer (risk against risk) trade-off | Rows 22, 24, 25; FINAL l.11, l.17 | CERTAINTY, TWOREASONS | NICHE | The plain reason for "barring a US default": nothing she could buy removes it without adding a larger one | "No safer USD asset" is Keel's reading, not a sourced finding; the frozen plan allows only WInS-listed stocks, ETFs and Treasury bonds anyway (COMPETITION.md section 4, not re-read today) | VERIFIED (rows 22, 24, 25 read) | no | This card |
| 24 | A bank deposit: FDIC insures "$250,000 per depositor, per FDIC-insured bank, for each account ownership category"; the Deposit Insurance Fund "is backed by the full faith and credit of the United States government" | FDIC, Understanding deposit insurance | LADDER, CERTAINTY | KNOWN | Cash at banks adds each bank's risk above $250,000 and still rests on the same US credit; Laura's holdings reach $589,655 at the end (NUMBERS 8k, via SKELETON) | The point is the same credit underneath, not a likely loss | VERIFIED (FDIC page read) | no | fdic.gov |
| 25 | A second sovereign (a AAA euro issuer, say): removes US credit, adds a currency risk the regulator sizes at 25% (row 15); a hedge needs derivatives, which the competition's rules ban | Row 15; COMPETITION.md section 4 (not re-read) | LADDER, CERTAINTY | KNOWN | Payments are fixed in US dollars; swapping a 0.2-0.4% a year priced residual for a 25% currency stress is a bad trade | Keel's reading; not a model run | VERIFIED (Art. 188 read); rules from the repo, not re-read | no | This card |
| 26 | Where ALARP truly bites: the small residuals. Cheap measures it would require are already in the plan's notes: (a) an X-date within a month of a date the plan needs cash moves that payment's money into bills maturing before it (Table 3 row 3); (b) custody: $589,655 at the end against SIPC's $500,000, a set-up decision (two custodians or confirmed excess cover) | SKELETON 3e and Exhibits item 4; Q30; rows 20-21 | TWOREASONS, PROCESS, RESERVE2033 | NICHE | Under the gross-disproportion test both measures must be taken: cost is small, benefit is real. Gives 3e a reason, not a slogan | The custody decision is still open in SKELETON; an ALARP frame would expose it if left open | VERIFIED (SKELETON and Q30 read) | risk: custody set-up still undecided (SKELETON Exhibits item 4 (c)); no change to the plan | SKELETON; Q30 |
| 27 | Bias to safety: "there should be a transparent bias on the side of health and safety"; where uncertain, "err on the side of safety" (Lead, Thu 12 Nov: the no-interest standard is Keel's call of Tue 10 Nov inside the IPS's completion clause, never "Caplet chose a dearer standard"; INTENT failure 7) | HSE (2001), R2P2 | CERTAINTY, REINVEST | NICHE | The same bias is in Laura's choice of the zero-interest test over a forward-rate test: design A at forwards is $54,595 short at 0% and short in 55.6% of history windows (NUMBERS 2, MODEL) | A safety principle about lives; here it prices the top-up, about a quarter of the 2028 deposit, most of which comes back (NUMBERS 8k) | VERIFIED (R2P2 read) | no | R2P2; NUMBERS 2 |
| 28 | S&P's default: a payment "not made on the date due", unless S&P believes it will be made "within the next five business days in the absence of a stated grace period" (or within the earlier of the grace period or 30 calendar days); SD is a selective default (Lead, Thu 12 Nov: the five-business-day test is Keel's definition, Wed 11 Nov, of the IPS's "a Treasury default", not the IPS's own words; IPS l.17 names only the event) | S&P Global Ratings, Ratings definitions | TWOREASONS | KNOWN | The IPS definition of a Treasury default (not paid within five business days) is S&P's test; ISDA uses three (SKELETON 3e) | S&P's test is a belief at the due date; the IPS test is a fact after five business days | VERIFIED (definitions page read) | no | spglobal.com |
| 29 | Moody's default: "a missed or delayed disbursement of a contractually-obligated interest or principal payment (excluding missed payments cured within a contractually allowed grace period)"; also bankruptcy, a distressed exchange, or a sovereign-imposed change in terms (e.g. forced redenomination) | Moody's Investors Service (2022), Rating symbols and definitions | TWOREASONS, CERTAINTY | KNOWN | Treasuries state no grace period, so by Moody's wording even a one-day delay counts (Keel reading); Moody's statistics count events the IPS logs under the debt-limit row | Definitions differ, so "default rates" from different agencies are not the same event | VERIFIED (read in a copy of Moody's June 2022 document hosted by DHL Group) | no | group.dhl.com (Moody's document) |
| 30 | Moody's idealised cumulative default rates: 10 years Aaa 0.0100%, Aa1 0.1000%, Aa2 0.2000%, Aa3 0.4000%, A1 0.7000%; 1 year Aaa 0.0001%, Aa1 0.0006%. Moody's: "highly stylized and ... not intended to match historical or future ratings performance"; built in 1989; Aaa and Aa2 set below their historical rates; never revised | Moody's (2006), Request for comment, Figure 8; Moody's (2022), footnote 27 | CERTAINTY | NICHE | Kill as Laura's number: a benchmark input for structured-finance models, not a probability | None needed; the agency says it itself | VERIFIED (both documents read) | no | moodys.com; group.dhl.com |
| 31 | Observed against idealised: Moody's own 10-year corporate cumulative default rates were Aaa 0.5564% and Aa 0.5798%, about 56 and 6 times the idealised Aaa and Aa1 figures | Moody's (2006), Request for comment, Figure 3; Keel arithmetic | CERTAINTY | KNOWN | Corporate history (about 0.6% at ten years for AA) is a misfit too: companies cannot issue the currency they owe | Corporate S&P figures (about 0.65% for AA) seen only on a secondary site | VERIFIED (Moody's figure read); S&P corporate UNVERIFIED | no | moodys.com |
| 32 | Moody's sovereign studies: Aaa and Aa sovereigns 0.000% cumulative default at 1-10 years (1983-2006; 1983-2008); "No sovereign rated single-A or higher defaulted on bonds" (1983-2005); the 0% investment-grade sovereign rate is "statistically indistinguishable" from the corporate one, given the small sample (1985-2002) | Varma (2003, 2006); Zazzarelli (2007); Duggar (2009): Moody's sovereign default studies | CERTAINTY | KNOWN | A clean record, stated with its own caveat about sample size | All end by 2008, before Greece (2012) and Cyprus (2013) | VERIFIED (the four PDFs read) | no | moodys.com |
| 33 | S&P, local currency, 1993-2024: AA cumulative default 0.00% at years 1-10, then 0.37% (11), 0.78% (12), 1.23% (13), 1.72% (14), 2.24% (15); AAA 0.00% to 15; foreign currency AA 0.00% to 15 (1975-2024). S&P warns local-currency rates "could also be understated" (forced rollovers, coerced exchanges with domestic banks) | Rossi & Kraemer (2025), Tables 16-17 and text | CERTAINTY, TWOREASONS | NICHE | US Treasuries are local-currency debt, so Table 17 is the right row; "none within ten years" holds; "none within fifteen" does not | Small samples; ratings are opinions, not probabilities | VERIFIED (study page read; Tables 16, 17 seen) | risk: Q4c row 33 and verdict 2 quote the foreign-currency table as "0.00% at 1-15 years"; for US debt true only to 10 years (store note, not a FINAL clash) | spglobal.com |
| 34 | Who they were: the two local-currency defaults from AA are Cyprus (28 Jun 2013; first local-currency rating AA+, 16 Jul 1996) and Barbados (7 Aug 2018; first AA-, 17 Dec 1999); their gaps (16.95 and 18.64 years) give Table 20's average 17.79 years and standard deviation 1.19 | Rossi & Kraemer (2025), Tables 18, 20; Keel arithmetic | CERTAINTY | NICHE | Neither issues a reserve currency on its own. Cyprus paid in euros, which it uses but does not issue alone; Barbados issues its own dollar, pegged to the US dollar. So owing in your own currency did not prevent default (Barbados) | Euro and peg facts are Keel's knowledge, not read today; Table 18's column headings were not seen (the reading is confirmed by matching Table 20) | VERIFIED (Tables 18 and 20 read) | no | spglobal.com |
| 35 | Laura's horizon is longer than ten years: Treasuries held from Jan 2027 to maturities from mid-Dec 2032 (IBTM) to 15 Nov 2041, about 6 to 15 years. If forced, Table 17 read at each rung's horizon averages about 0.6% across the ten payments (historical, two events, not a forecast). Also from S&P: no one-year default from any rating above BBB-; a default from AA came through years of downgrades (local currency, 15 years on: 32.81% A, 19.27% BBB, 2.60% SD) | NUMBERS 0 (the ten instruments); Rossi & Kraemer (2025), Tables 13, 17, Appendix 1; Keel arithmetic | CERTAINTY, TWOREASONS, LADDER | NICHE | Say "none within ten years" only with the horizon stated; and a slide from AA is watchable long before any default (ratings change nothing in the plan, Q26 T11) | Rung horizons rounded; the AA category mixes AA+, AA, AA-; two events cannot carry a number for one country | VERIFIED (inputs read; arithmetic checked) | no | NUMBERS 0; spglobal.com |

## (b) Cards

**Card 1. Solvency II prices US Treasuries at zero credit risk (rows 6-9).**
- What is it? The EU insurance standard formula charges no spread risk and no concentration risk on a foreign central
  government's bonds in its own currency at credit quality step 0 or 1 (AAA to AA-). The US, at AA+/Aa1, is step 1.
- Did it work? It is the rule for every EU insurer, live since 2016. The 2025 Moody's downgrade (Aaa to Aa1) changed
  the step from 0 to 1 and left the charge at zero. A charge starts only in the single-A range.
- How is Laura's case like it? Her standard and the insurer's both treat the same event as outside the test: "barring a
  US default" (FINAL l.11) and a 0% charge.
- How is it not? The insurer's zero is a policy choice made by a rule-maker. Laura's is an exception she names, and she
  says what changes if it happens (reason 2, defined at five business days).
- What Caplet takes: 3a and 3e. Never "stricter than insurers" alone. If the comparison appears at all, it is scoped:
  stricter on rates and reinvestment; the same carve-out on the default. One clause at most; no exhibit.

**Card 2. The 2027 down shock against the zero-interest test (rows 10-13).**
- What is it? From 30 Jan 2027 an insurer's 1-in-200 one-year fall in rates is r(1 - s) - b by maturity. On today's
  curve that is about 2.4-2.6 points at 5-10 years and 3.7 points at 1 year (Keel arithmetic, approximation).
- Did it work? It is the regulator's own calibration of a 1-in-200 year, for every EU insurer from 30 Jan 2027.
- How is Laura's case like it? Her test is the limit case: every rate to zero, held for the whole life. NUMBERS 2
  (MODEL): $0 short at 1, 2 or 3 points lower for good; $0 at 0% with $1,414 spare.
- How is it not? The insurer's shock is instant, on value, on a swap-based curve; hers is a path of cash on Treasury
  yields. One year with recapitalisation against ten-plus years with none (1 in 200 a year for ten years is about
  1 in 20).
- What Caplet takes: 3a's evaluation methods (SKELETON row 3a). This is a fourth lens if a judge asks "how strict is
  strict"; it survives a fall larger than an insurer must hold capital for. Note only; figures from NUMBERS 0 and 2.

**Card 3. Tolerability of risk, with risk transfer as the reason to stop (rows 16-23, 26).**
- What is it? HSE's three regions: a tolerable risk is borne only if kept as low as reasonably practicable and reviewed.
  "Reasonably practicable" means a measure is required unless its cost is grossly disproportionate to the risk it
  removes (Edwards v National Coal Board, 1949). When a measure moves risk to others, the added risk is offset against
  its benefit (SPC/Permissioning/39).
- Did it work? It has been the UK's working basis for risk decisions since 1988-2001. HSE says it uses numbers only for
  deaths.
- How is Laura's case like it? The US default is a tolerated residual, never "acceptable". Each alternative moves risk
  rather than cutting it: bank risk above FDIC's $250,000 (and the same US credit underneath), or a 25% currency stress
  on a second sovereign. Table 3 is the periodic review.
- How is it not? HSE's numbers are yearly chances of death; CDS-implied 0.2-0.4% a year is 2,000-4,000 in a million,
  which HSE's scale would call intolerable for a likely-cured delay. Money is not lives.
- What Caplet takes: 3e. The shape only, no HSE numbers, and probably not the acronym. The test is useful inside the
  team: it says the two cheap measures (bills before a named X-date; the custody set-up) must be done. The custody
  decision should be closed before 27 Nov.

**Card 4. Moody's idealised table is not a probability (rows 30-31).**
- What is it? A table built in 1989 that gives each rating a target cumulative default rate (Aa1: 0.10% at ten years).
- Did it work? As a benchmark inside structured-finance models, yes. As a forecast, Moody's says it is "not intended to
  match historical or future ratings performance". Its own observed corporate rates are 6 to 56 times higher.
- How is Laura's case like it? It is the tidy "one plain number" the claim wanted.
- How is it not? It is stylised, never revised, and corporate-based, and Moody's counts any delay as a default.
- What Caplet takes: nothing for the report. Store note: never cite it. If a single number is ever needed, it is the
  observed record (card 5) beside Q4c's CDS bound, each with its caveat.

**Card 5. The local-currency record and Laura's fifteen-year horizon (rows 33-35).**
- What is it? S&P's 1993-2024 local-currency study: AA sovereigns 0.00% cumulative default for 1-10 years, 2.24% at 15.
  The two events are Cyprus (2013) and Barbados (2018), each about 17-19 years after its first AA rating.
- Did it work? Ratings ranked default risk well: no one-year default above BBB-. A default from AA came only after
  years of downgrades.
- How is Laura's case like it? US Treasuries are local-currency debt. Her holdings run about 6 to 15 years from
  January 2027, so her last five payments sit in the part of the table that is not zero.
- How is it not? Two events in a small sample. Neither issues a reserve currency on its own; the US issues the
  currency it owes. S&P also warns the local-currency rates may be understated.
- What Caplet takes: 3e. "No AA or AAA sovereign defaulted within ten years in either agency's record" is usable only
  with the horizon and sample caveat stated. Never as a probability; CANON A4 stays structural. Store correction: Q4c
  row 33's "0.00% at 1-15 years" is foreign currency.

**Card 6. The definition does the work the number cannot (rows 28-29).**
- What is it? S&P calls a payment default only if it is not made within five business days where no grace period is
  stated. Moody's counts any missed or delayed payment beyond a contractual grace period, and Treasuries state none.
- Did it work? These definitions decide whether history holds a US default at all: Moody's records none since 1983
  (Q4c row 33). The 1979 paper-check delay hit only paper holders and was over in under three weeks (Q15 rows 14-15).
- How is Laura's case like it? The IPS's reason 2 is S&P's five-business-day test (SKELETON 3e), so the plan's trigger
  and the most-used rating definition are the same event.
- How is it not? S&P judges at the due date; the IPS judges after five business days. Moody's would count a delay the
  IPS logs under the debt-limit row.
- What Caplet takes: 3e and Table 3 row 2. Lead with the definition and cite S&P's wording as its source. One clause
  that ISDA uses three days (already in SKELETON). This is the answer to "what exactly is 'barring a US default'".

## (c) Verdicts

**Claim 1 ("stricter than Solvency II's 1-in-200"): CHANGE.**
- Risk by risk:
  - Interest rates and reinvestment: stricter. Her test takes every rate to zero for good (a fall of 4.3-5.3 points
    on the NUMBERS 0 curve). The insurer's 2027 shock is a fall of about 2.4-2.6 points at 5-10 years and 3.7 at
    1 year (rows 10-11). NUMBERS 2 (MODEL) also shows $0 short at 1, 2 and 3 points lower for good, which already
    exceeds the insurer's shock at 7-10 years.
  - Equity: no shares stand behind the payments, so there is nothing to stress. Solvency II's equity shock was not
    read, so this is not sized.
  - The US default: the same carve-out (rows 6-9). Solvency II's standard formula gives US Treasuries a 0% spread and
    0% concentration charge. Neither standard puts a number on the event.
  - Operational and custody risk: Solvency II charges a number (Art. 101(4)). Laura's test names the residual
    (CANON C9) but does not size it as a probability. So "stricter" fails here.
- Form: one year with recapitalisation against the whole life with no fresh money. A quantile of a model against a
  scenario passed by construction (rows 12-13).
- Market measure (Q4c): quiet years 1 in 250 to 1 in 500 (the same order as 1 in 200); standoff years 8 to 12 times
  1 in 200. Those figures price a likely-cured delay, not a capital loss.
- Design note: if the comparison is used, scope it to rates and reinvestment and say the carve-out is shared. Bare
  "stricter than insurers" would overclaim, and a judge who knows Solvency II would see the 0% charge.

**Claim 2 ("ALARP gives Laura the words for why she stops"): CHANGE.**
- The tolerability of risk framework fits the shape of her standard: a residual is tolerated, not accepted; it is kept
  as low as reasonably practicable and reviewed. That review is what Table 3 is.
- It does not fit the default itself on cost grounds. No measure reduces the US default without adding a risk.
  - A bank deposit adds bank risk above $250,000 per bank and ownership category, and FDIC's fund rests on the same US
    credit.
  - A second sovereign adds a currency stress that Solvency II sizes at 25%; a hedge needs derivatives, which the rules
    ban.
  - So the reason she stops is risk transfer, HSE's own term (SPC/Permissioning/39), not a gross disproportion of
    cost.
- HSE's numbers must not be borrowed (row 19): they are yearly chances of death and would make the residual look
  intolerable.
- Real use: the gross-disproportion test applies cleanly to the small residuals. The X-date move into bills and the
  custody set-up are cheap, so the test says both must be done.
- Is the parallel honest? Yes for the shape and for the small residuals. No as a numeric or cost-based justification
  for the default exception.

**Claim 3 ("the idealised table gives the best plain number"): CHANGE; the idealised table is KILLED.**
- Moody's idealised rates are a 1989 stylised benchmark, explicitly not a forecast (row 30). They are also corporate
  and below Moody's own observed rates (row 31).
- The observed sovereign record is the better reference:
  - Moody's: Aaa and Aa sovereigns 0.000% to ten years, 1983-2008.
  - S&P local currency: AA 0.00% to ten years and 2.24% at fifteen, 1993-2024, from two events.
- For Laura's 2033-2042 payments, bought in 2027-28, the horizon is about 6 to 15 years. So any "within ten years"
  statement must carry the horizon.
- Recommendation, in order: (1) the definition (five business days, S&P's test); (2) the rating record as context,
  with sample size and horizon; (3) Q4c's CDS figures as an upper bound on a late payment. No single ten-year
  probability; CANON A4 keeps the exception structural.
- Caveats that must travel with any rating figure:
  - small samples ("statistically indistinguishable", Moody's);
  - local-currency rates may be understated (S&P);
  - definitions differ (Moody's counts any delay; S&P allows five business days);
  - no sovereign that issues a reserve currency on its own is among the defaults (Keel knowledge).

## (d) Gaps

- S&P sovereign study: read through the fetch tool's extracts of the web page, not a PDF. Tables 13, 16, 17, 18, 20,
  42 and 43 were seen in part. The US's own row and the 10-year local-currency table without rating modifiers were not
  seen; the table with modifiers (Table 42) shows AA+ and AA to SD at 0.00% over ten years.
- Table 18's column headings were not seen. The columns were read as default date, first rating date and first rating
  because the two AA cases reproduce Table 20's average and standard deviation (Keel arithmetic).
- Q4c row 33 and Q4c verdict 2 cite the foreign-currency table (Table 16) as "0.00% at 1-15 years" for AA. For US
  (local-currency) debt this holds only to ten years. Not edited (brief: edit no other file); the lead may want a store
  note. REFERENCES_APA entry 222 (Rossi & Kraemer) was used as is; no error found.
- The Official Journal number of the 2027 delegated regulation ((EU) 2026/269) comes from a law-firm briefing
  (Lexology), not the Official Journal. The Commission's C(2025) 7206 final/2 text and EIOPA's 15 Jul 2026 release
  (application from 30 Jan 2027) were read.
- The current Art. 167 down-shock table values are images on the rulebook page and were not read.
- Solvency II's US-dollar basic rate curve (EIOPA's, swap-based with a credit adjustment) was not used. Treasury par
  yields stand in, so rows 10-11 are an approximation.
- Not read:
  - Art. 4 of 2015/35 (which rating counts when agencies differ);
  - the equity shock (Art. 169);
  - technical provisions (Art. 77);
  - the critiques of the sovereign zero (ESRB 2015; Basel Committee 2017).
- R2P2 was read in a gov.uk copy (an inquiry exhibit, IQ8.10.J); HSE's own PDF link was not fetched. Edwards v National
  Coal Board was read only as quoted in R2P2.
- Moody's 2022 Rating symbols and definitions was read in a copy hosted by DHL Group, not on moodys.com. The current
  edition was not read. APA elements missing for the Moody's studies: months and authors were not recorded for most.
- S&P corporate AA ten-year default (about 0.65%) was seen only on a secondary site (investmentgrade.com): UNVERIFIED.
- Not read today (Keel knowledge only):
  - that Cyprus paid in euros and that the Barbados dollar is pegged to the US dollar;
  - whether the 1979 paper-check delays would meet the IPS definition (Q15 says book-entry holders were unaffected).
- The 1979 delay itself (Zivney & Marcus, 1989; CRS 2016) is in Q15 and was not re-read.

## Sources (APA 7; all accessed 12 Nov 2026)

1. European Parliament & Council of the European Union. (2009). Directive 2009/138/EC of the European Parliament and of
   the Council of 25 November 2009 on the taking-up and pursuit of the business of Insurance and Reinsurance (Solvency
   II) (recast). *Official Journal of the European Union*, L 335, 1-155. https://eur-lex.europa.eu/eli/dir/2009/138/oj/eng
   (consolidated text of 9 Jul 2018: https://eur-lex.europa.eu/eli/dir/2009/138/2018-07-09/eng). Read: recital 64,
   Art. 101, 104, 105, 121-122, 129.
2. European Commission. (2015). Commission Delegated Regulation (EU) 2015/35 of 10 October 2014 supplementing Directive
   2009/138/EC of the European Parliament and of the Council on the taking-up and pursuit of the business of Insurance
   and Reinsurance (Solvency II). *Official Journal of the European Union*, L 12, 1-797.
   https://www.legislation.gov.uk/eur/2015/35/title/I/chapter/V/section/5/adopted ;
   https://www.legislation.gov.uk/eur/2015/35/article/188/adopted ; EIOPA Single Rulebook: Art. 180
   https://www.eiopa.europa.eu/rulebook/solvency-ii-single-rulebook/article-5800_en , Art. 187
   https://www.eiopa.europa.eu/rulebook/solvency-ii-single-rulebook/article-5837_en , Art. 167
   https://www.eiopa.europa.eu/rulebook/solvency-ii-single-rulebook/article-5787_en . Read: Art. 167, 180, 185-188.
3. European Commission. (2016). Commission Implementing Regulation (EU) 2016/1800 of 11 October 2016 laying down
   implementing technical standards with regard to the allocation of credit assessments of external credit assessment
   institutions to an objective scale of credit quality steps in accordance with Directive 2009/138/EC. *Official
   Journal of the European Union*, L 275, 19-26. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02016R1800-20240722
   (consolidated to 22 Jul 2024). Read: Annex.
4. European Commission. (2025). *Commission Delegated Regulation (EU) .../... of 29.10.2025 amending Delegated Regulation
   (EU) 2015/35* (C(2025) 7206 final/2). https://ec.europa.eu/finance/docs/level-2-measures/solvency2-delegated-regulation-2025-7206_en.pdf
   Read: Art. 167 as amended (the s and b table).
5. European Insurance and Occupational Pensions Authority. (2026, July 15). *EIOPA completes Solvency II Review mandate
   with final guidelines and draft technical standards before revised framework takes effect early next year* [Press
   release]. https://www.eiopa.europa.eu/eiopa-completes-solvency-ii-review-mandate-final-guidelines-and-draft-technical-standards-revised-2026-07-15_en
6. Health and Safety Executive. (2001). *Reducing risks, protecting people: HSE's decision-making process*. HSE Books.
   ISBN 0 7176 2151 0. https://assets.publishing.service.gov.uk/media/6634988fcf3b5081b14f30cd/IQ8.10.J_Document_9_Health_and_Safety_Executive__Reducing_risks__protecting_people__HSE_s_decision-making_process__2001.pdf
   (read in full).
7. Health and Safety Executive. (2023, April 25). *Guidance on ALARP decisions in COMAH* (SPC/Permissioning/37).
   https://www.hse.gov.uk/foi/internalops/hid_circs/permissioning/spc_perm_37/index.htm
8. Health and Safety Executive. (2026, January 30). *HID's approach to ALARP decisions* (SPC/Permissioning/39).
   https://www.hse.gov.uk/foi/internalops/hid_circs/permissioning/spc_perm_39.htm
9. Federal Deposit Insurance Corporation. (n.d.). *Understanding deposit insurance*. Retrieved November 12, 2026, from
   https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance
10. Moody's Investors Service. (2006, June). *Request for comment: Mapping of Moody's U.S. municipal bond rating scale to
    Moody's corporate rating scale and assignment of corporate equivalent ratings to municipal obligations*.
    https://www.moodys.com/sites/products/DefaultResearch/2005700000427679.pdf (Report No. 97921). Read: Figures 3 and 8.
11. Moody's Investors Service. (2022, June). *Rating symbols and definitions*. Read in a copy hosted by DHL Group:
    https://www.group.dhl.com/content/dam/deutschepostdhl/en/investors/creditor-relations/ratings/2022/DPDHL-Moodys-Rating-Definitions-2022-06-02.pdf
    Read: default definition; footnote 27 on the idealised tables.
12. Varma, P. (2003, February). *Sovereign bond defaults, rating transitions, and recoveries (1985-2002)* [Special
    comment]. Moody's Investors Service. https://www.moodys.com/sites/products/DefaultResearch/2001900000415841.pdf
    (Report No. 77350).
13. Varma, P. (2006, April). *Default and recovery rates of sovereign bond issuers, 1983-2005* [Special
    comment]. Moody's Investors Service. https://www.moodys.com/sites/products/DefaultResearch/2005600000424157.pdf
14. Zazzarelli, A. (2007, June). *Sovereign default and recovery rates, 1983-2006* [Special comment]. Moody's
    Investors Service.
    https://www.moodys.com/sites/products/DefaultResearch/2006600000441428.pdf
15. Duggar, E. (2009, March). *Sovereign default and recovery rates, 1983-2008* [Special comment]. Moody's
    Investors Service.
    https://www.moodys.com/sites/products/DefaultResearch/2007400000587968.pdf
16. S&P Global Ratings. (n.d.). *S&P Global Ratings definitions*. Retrieved November 12, 2026, from
    https://www.spglobal.com/ratings/en/research/articles/190705-s-p-global-ratings-definitions-504352
17. Rossi, L., & Kraemer, N. W. (2025, March 24). *Default, transition, and recovery: 2024 annual global sovereign default
    and rating transition study*. S&P Global Ratings.
    https://www.spglobal.com/ratings/en/research/articles/250324-default-transition-and-recovery-2024-annual-global-sovereign-default-and-rating-transition-study-13448189
    (REFERENCES_APA entry 222). Read: Tables 13, 16, 17, 18, 20, 42, 43, Appendix 1 and text.

Repo files read (not sources for the report): FINAL_IPS_as_submitted.txt; CANON.md (A4, A6, C1, C5, C9, C12, C13);
WORDS.md; SKELETON.md (3a, 3c, 3e, Exhibits item 4); NUMBERS.md (0, 1, 2, 7, 8k, 8l); cards Q4c, Q15, Q30, Q31;
REFERENCES_APA.md.
