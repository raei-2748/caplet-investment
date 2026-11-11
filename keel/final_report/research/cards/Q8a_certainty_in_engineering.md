# Q8a research cards: what "certain" means in engineering safety, and what Laura's report can borrow (3a, 3e)

**Date.** Thu 12 Nov 2026 (Sydney morning; Wed 11 Nov, afternoon, in the US). Every web source was read at the source
that day (Parallel web_fetch and web_search); "accessed 12 Nov 2026" below means that day. Report parts 3a (the
standard and its price) and 3e (assumptions, limits, Table 3), with notes for 3c (why the confidence differs by promise),
2.3 (concentration) and 3f (one PROCESS idea).

**Notes for the Final Report store, not report prose.** The IPS, the Trading Notes and the WInS book are frozen: a clash
is a risk to record, never a change. Every figure about the plan is quoted from `../../NUMBERS.md` with its section and
is MODEL. Keel arithmetic on public figures is marked "Keel arithmetic". NUMBERS calls the top-up "the completion"
($38,282 in January 2028: the ladder's $2,388 tail plus the $35,894 backstop, NUMBERS 2); this card uses the WORDS
names. It does not repeat Q4c (likelihood words, CDS-implied default chances, the 585-window bound) or Q31 (how the
standard is SAID: "full cash"); it asks how the standard is EVALUATED, the way engineers evaluate one.

**Claims tested.**
1. CHANGE (expected): Laura's certainty can be stated the way structural and aviation engineers state it: a design
   basis (all ten paid if no interest at all is earned), one named residual beyond it (a US default), and a reason no
   further reduction is reasonably practicable (no safer asset exists for dollar payments).
2. KEEP or KILL: "Laura's plan is fail-safe in the aviation sense: no single failure stops a payment."
3. KEEP or CHANGE: "Nuclear safety cases add what the report lacks: defence in depth and a stated frequency target per year."

**Problem class.** Stating a high-consequence commitment as a bounding case plus named residuals, when the true chance
of failure cannot be measured (rare events, no failures in the record). Solved by nuclear regulation (design basis,
defence in depth: US NRC, IAEA, UK ONR), aviation certification (the FAA fail-safe design concept, 14 CFR 25.1309),
structural design (EN 1990 design situations and reliability differentiation) and UK safety law (ALARP, gross
disproportion). Finance twin: KMV distance-to-default.

## Verdicts in one screen

- **Claim 1: CHANGE.** The shape is right (a bound, named residuals, a reason to stop); four parts change.
  - **Name.** The standard is a *design basis* in the nuclear sense: "the specific functions to be performed" plus "the
    specific values or ranges of values chosen for controlling parameters as reference bounds for design" (10 CFR
    50.2), analysed "in a conservative manner" (IAEA SSR-2/1 5.26). For Laura: function = ten $50,000 payments;
    controlling parameter = interest on everything reinvested or waiting; bound = 0%, after the Treasury-bill ETF's
    0.15% fee (NUMBERS 2, 8h). It is NOT an EN 1990 reliability index: beta is a probability (ordinary buildings: 3.8
    over 50 years, about 7 in 100,000; 4.7 a year, about 1.3 in a million) that EN 1990 itself calls "notional".
  - **Residuals: several, not one.** Beyond the bound sit a missed deposit, a custody failure, fund frictions the top-up
    cannot absorb, a payment delay longer than five business days, and a US default (CANON C9). The IPS names two as
    reasons to change; the rest are sized or watched.
  - **"No safer asset exists" is not ALARP.** ALARP is a cost test: reduce risk unless the cost is grossly
    disproportionate (Edwards v NCB, 1949). Its honest form for Laura has two halves: nothing on Wharton's permitted
    list removes the US default at any price; and Caplet already took the dearer, more protective option ($13,220
    more than Mon 9 Nov's 3-point margin, which was $22,192 short at 0% and short in 35 of 585 windows; NUMBERS 2).
    HSE "rules out ... accepting a less protected but significantly cheaper option": the 10 Nov call has that shape.
  - **Date.** The standard holds from January 2028, when the top-up is bought. In 2027 the ten are $54,595 short at 0%
    (NUMBERS 8h): EN 1990 calls this a "transient design situation".
  - **Apt or a stretch?** Apt as Caplet's audit method; a stretch as report vocabulary for a fixed-income judge. Keep
    the idea, drop the labels: cash-flow matched, a bounding test at zero interest, named exceptions.
- **Claim 2: KILL "fail-safe".** Walked one failure at a time, "regardless of its probability" (FAA AC 25.1309-1B
  2.2.1.1):
  - The top-up covers: every coupon and waiting dollar earning nothing (met exactly after the fee; $1,414 left without
    it, NUMBERS 8h); rates 3 points lower for good ($25,651 left); all 585 historical windows (NUMBERS 2); a deposit up
    to 74.5% smaller at today's yields (NUMBERS 5).
  - Other means cover: one fund paying below its holdings at the interest rates the market expects (the top-up's money
    is never drawn then; $10,775 of it waits in the Treasury-bill ETF on 1 Jan 2033, NUMBERS 8h); a fund closing late
    (sell on the exchange, Q26 row 11); a Treasury payment late by five business days or less (every holding pays 0.5
    to 10.5 months before its payment date, NUMBERS 8h).
  - Nothing covers: a missed deposit (2033 payment $3,016 short at forward rates; the ten $57,455 short at 0%, short in
    all 585 windows; NUMBERS 5); a custody failure above SIPC's $500,000 (about $589,000 held near Dec 2032, Q26 row 22,
    Keel arithmetic); a US default or a delay over five business days.
  - Two more breaks. The FAA's 2024 definition counts failures with a common cause as ONE failure: five rungs share one
    fund family. And in 2027 the top-up's source (the 2028 deposit) shares a cause with the danger it guards (a
    recession cuts her income while yields fall; NUMBERS 5).
- **Claim 3: CHANGE. Defence in depth: KEEP as an audit. A per-year frequency target: KILL.**
  - The layers map onto the five nuclear levels but are not independent for credit (one issuer), custody (one broker,
    assumed) or the fund family. They are independent for rates (after January 2028) and for shares.
  - Missing: diversity against the common cause (no permitted asset supplies it for the issuer), and a written account
    of what Caplet does when each reason fires (CANON A34 allows showing what a missed deposit changes; no new trigger).
  - **Best finding.** IAEA SSR-2/1 4.10: "The existence of multiple levels of defence is not a basis for continued
    operation in the absence of one level." Laura's two reasons are exactly the two events that remove a level: a
    missed deposit removes the top-up; a US default removes the base. Market falls stay inside the design basis. An
    engineering reason for IPS l.17 ("A fall in the market is not one of them.").
  - No frequency target: NRC calls its numbers "aiming points"; ONR says its objectives are not "design targets"; EN 1990
    calls its probabilities "notional". For Laura a per-year figure is either a CDS price of a late US payment (0.2-0.4%
    a year in quiet years, Q4c: 1,500 to 3,000 times a building's annual target, Keel arithmetic) or a model zero that
    is true by construction.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A design situation is a set of conditions over a time interval, chosen "sufficiently severe and varied so as to encompass all conditions that can reasonably be foreseen" | EN 1990:2002 1.5.2.2, 3.2(3)P | CERTAINTY, REINVEST | KNOWN | Laura's design situation: nothing reinvested or waiting earns interest, from 1 Jan 2027 to 2042, and every waiting dollar pays the Treasury-bill ETF's 0.15% fee (NUMBERS 2, 8h) | A building's situations are measured loads; a 0% world is a chosen bound, and it does not cover "all conditions that can reasonably be foreseen" (default, custody, missed deposit sit outside it) | VERIFIED (EN 1990 1.5.2.2-1.5.2.4 and 3.2 read) | no | EN 1990 sections 1.5, 3.2 |
| 2 | A transient design situation lasts "much shorter than the design working life", for example "during execution or repair", and is checked on its own | EN 1990 1.5.2.3 | COMPLETE2028, LADDER, CERTAINTY | NICHE | 2027 is Laura's transient situation: the ladder is bought, the top-up is not. Without it the ten are $54,595 short at 0% (NUMBERS 8h) | A building's construction phase is short and supervised; Laura's lasts a year and ends only if her income delivers the deposit | VERIFIED (EN 1990 1.5.2.3 read) | risk: IPS l.11 states the standard with no date; it holds from January 2028 (SKELETON 3a already notes what 2027 secures) | EN 1990 1.5.2.3 |
| 3 | "Design bases" = the functions a system must perform plus "the specific values or ranges of values chosen for controlling parameters as reference bounds for design" | 10 CFR 50.2 | CERTAINTY | KNOWN | The correct name for Laura's standard: function = ten $50,000 payments on 1 Jan 2033-2042; controlling parameter = interest earned on reinvested and waiting money; bound = 0% after the fee (NUMBERS 2) | A reactor's design basis is approved by a regulator and inspected; Laura's is set by her advisers and checked by a model | VERIFIED (eCFR 10 CFR 50.2, the definition read) | no; matches CANON A4 (the standard is structural, not a probability) | eCFR |
| 4 | Design basis accidents are analysed "in a conservative manner", postulating failures and using conservative assumptions | IAEA SSR-2/1 Rev.1 para 5.26 | CERTAINTY, REINVEST | KNOWN | Zero interest is the conservative assumption: then no payment depends on any future rate (SKELETON 3a). The fee cushion ($885 more, NUMBERS 2) is a conservative margin on top | Nuclear conservatism adds margins to a best estimate; Laura's central case is the interest rates the market expects, and 0% is far below it, not a margin on it | VERIFIED (SSR-2/1 Rev.1 read: 2.13, Requirement 7, 4.9-4.13A, 5.26, Requirements 25-26) | no | IAEA SSR-2/1 section 5 |
| 5 | Beyond the design basis, severe events are still analysed and feed the later levels (mitigation, emergency arrangements) | ONR SAPs paras 610, 724, 768; IAEA SSR-2/1 2.13 | CERTAINTY, TWOREASONS | KNOWN | Laura's beyond-basis events: a missed deposit, a custody failure, a delay over five business days, a US default. Each named; sized where NUMBERS can (NUMBERS 5); watched in Table 3 | Nuclear severe-accident analysis is probabilistic and site-specific; Laura's list is short enough to write out | VERIFIED (SAPs read at these paragraphs) | risk: "one named residual" (claim 1) conflicts with CANON C9 (default is not the only residual) | ONR SAPs |
| 6 | The reliability index beta sets a minimum level by class: RC2 (medium consequence) 3.8 over 50 years and 4.7 a year; RC3 4.3 and 5.2; RC1 3.3 and 4.2 | EN 1990 Annex B Table B2; Annex C Tables C1, C2 | CERTAINTY | TEXTBOOK | Only if a judge asks "how certain, as a number": beta 3.8 is about 7.2 in 100,000 over 50 years; 4.7 a year is about 1.3 in a million a year (Keel arithmetic, Pf = Phi(-beta)) | Beta comes from calibrated load and strength distributions; Laura's residuals have none | VERIFIED (Annexes B and C read) | no | EN 1990 Annexes B, C |
| 7 | EN 1990's probabilities are "only notional values that do not necessarily represent the actual failure rates"; real failure "is significantly dependent upon human error", which the code does not model | EN 1990 Annex C, C4 note and C6(2) | CERTAINTY, PROCESS | NICHE | A model result for Laura (no shortfall in simulated futures or in 585 windows) is notional in the same way: true of the model, silent about human error (a missed purchase, a wrong order) | None: the parallel is exact | VERIFIED (Annex C read) | no; supports CANON A4 | EN 1990 Annex C |
| 8 | Read as betas, CDS-implied US default chances are weak: 0.2% and 0.4% a year are beta 2.88 and 2.65; 1% is 2.33; the 2011, 2013 and 2023 standoffs (4-6%) are 1.75-1.55 | Keel arithmetic on card Q4c's figures and EN 1990 Table C1 | CERTAINTY | NICHE | Why a beta is the wrong language: priced by the market, Laura's residual is 1,500 to 3,000 times a building's annual target (1.3e-6) | CDS prices a late payment and carries a risk premium, so it is an upper bound (Q4c); a building's Pf is notional (row 7). Two different kinds of number | VERIFIED (arithmetic; inputs from Q4c and EN 1990 Table C1) | risk: any per-year figure in the report invites this comparison | Keel arithmetic |
| 9 | KMV's distance-to-default is the finance twin of beta (standard deviations to default); mapped to real defaults a distance of 4 is "around 100 bp" a year, while "the Normal distribution ... is essentially zero" | Crosbie & Bohn (2002) | CERTAINTY | KNOWN | A bond judge's instinct: a Normal-tail certainty number is not believed. One more reason never to state Laura's certainty as a beta or a number of sigmas | KMV models firms with equity; the US Treasury has none | VERIFIED (paper read in full) | no | Crosbie & Bohn (2002) |
| 10 | Reliability differentiation: the graver the consequence, the stricter the target (EN 1990 classes, KFI 1.1 for RC3); the FAA's "inverse relationship" between probability and severity | EN 1990 Annex B Tables B1-B3; AC 25.1309-1B 4.1, Figure 4-1 | CERTAINTY, FLOOR, CEILING, HALFKEPT | KNOWN | Laura's promises carry different standards on purpose: the ten = paid at zero interest; the bottom of the range = what the floor's holdings pay less 0.5%; the top missed in 5.99% of simulated futures at a 0.75% fund cost, by at most $429 (NUMBERS 8l); her flexibility = shares. 3c and 3e can say why confidence differs by promise | Engineering classes are set by law; Laura's are Caplet's choice, so they must be explained | VERIFIED (both read) | no | EN 1990 Annex B; AC 4.1 |
| 11 | Robustness: no damage "disproportionate to the original cause"; survive "the accidental removal of an individual member" | EN 1990 2.1(4)P, 2.1(5)P | LADDER, CERTAINTY | KNOWN | Remove one rung: at the rates the market expects, one fund paying low is absorbed by the top-up's pooled money ($10,775 waiting on 1 Jan 2033; $45,456 in 2033 money in all; NUMBERS 8h). At 0% it is not: $1,414 spare, $0 after the fee (NUMBERS 8h) | Removing a member is sudden and physical; a fund paying 1% low is small and slow | VERIFIED (EN 1990 2.1 read) | no | EN 1990 2.1 |
| 12 | Prefer systems that give warning: "avoiding as far as possible structural systems that can collapse without warning" | EN 1990 2.1(5)P | CERTAINTY, RESERVE2033 | KNOWN | Laura's warnings come early: a fund's notice of a changed end date, its holdings file, the debt-limit date, the deposit's arrival by 31 March 2028. Table 3 is the list of warnings | A building's warning buys time to evacuate; in Laura's plan a warning changes nothing unless it is one of the two reasons (A34) | VERIFIED (EN 1990 2.1 read) | no; Table 3 already has "what it never changes" | EN 1990 2.1 |
| 13 | Design supervision levels: DSL2 = "Checking by different persons than those originally responsible"; DSL3 = "Third party checking ... by an organisation different from that which has prepared the design" | EN 1990 Annex B Table B4 | PROCESS | NICHE | Articulation, only if the team's real record holds it: a number checked by someone who did not build it. Engineers tie the strength of the check to the consequence | A judge will not know the EN term: the idea travels, the label does not | VERIFIED (Table B4 read) | no | EN 1990 Annex B |
| 14 | Reliability comes from design AND from execution and quality management, including measures against "gross human errors" | EN 1990 2.2 | PROCESS, TWOREASONS | KNOWN | Laura's execution side: a fixed purchase order (longest rungs first; complete in January 2028), a deposit deadline (31 March 2028), only two reasons to change. Fewer decisions, fewer chances for error | none recorded | VERIFIED (EN 1990 2.2 read) | no | EN 1990 2.2 |
| 15 | Fail-safe design concept: "the failure of any single element ... must be assumed, regardless of its probability. Such single failures must not be catastrophic"; the rule says a catastrophic condition "Must not result from a single failure" | AC 25.1309-1B 2.2.1.1; 14 CFR 25.1309(b)(1)(ii) | CERTAINTY, TWOREASONS | TEXTBOOK | The test for claim 2: walk each single failure with everything else normal (rows 23-25) | Aircraft carry spare channels of different design; Laura's plan has one issuer | VERIFIED (AC 25.1309-1B and eCFR 25.1309 read) | risk: "fail-safe" is a certainty word (CANON C13, C21, check 5) | AC 25.1309-1B 2.2.1 |
| 16 | Since 2024 a "Single Failure" is "Any failure or set of failures that cannot be shown to be independent from each other (e.g., failures due to a common cause)" | AC 25.1309-1B 1.5.27 (it cancels AC 25.1309-1A of 1988, para 1.3) | LADDER, CERTAINTY | NICHE | Five of the ten rungs are iBond funds of one family, one board, one lending programme (Q26 rows 11, 14, 15): one single failure for any shared cause | The family's risks are small and slow (frictions, an extended end date), not sudden | VERIFIED (AC 1.3, 1.5.27 read) | no | AC 25.1309-1B 1.5 |
| 17 | Catastrophic conditions must be "extremely improbable", about 1 in a billion per flight hour or less, which is a 1 in 10 million budget shared among about 100 conditions | AC 25.1309-1B 3.3, Appendix A | CERTAINTY, PRESENTATION | NICHE | If the report ever gives one confidence for the ten, it is the total over every residual (default, deposit, custody, fund frictions), not each alone: another reason to name residuals, not quote one figure | Aviation counts fleet hours; Laura's plan runs once | VERIFIED (AC 3.3, Appendix A read) | risk: CANON C9 | AC 25.1309-1B Appendix A |
| 18 | Eleven design principles; "The use of only one of these principles or techniques is seldom adequate" | AC 25.1309-1B 2.2.2 | CERTAINTY, PROCESS, PRESENTATION | KNOWN | Checklist for 3a and 3e: designed integrity (Treasuries held to the end); redundancy (the top-up); isolation (promised money kept from shares, IPS l.11); proven reliability (three iBond Treasury fund endings on schedule, NUMBERS 8h); failure annunciation (Table 3); crew procedures (the two reasons); checkability (holdings files); margins (fee cushion, NUMBERS 2); error tolerance (nothing sold after January 2028, NUMBERS 8h). Weakest: designed failure path (what happens when a reason fires) | Aircraft principles assume many independent subsystems | VERIFIED (AC 2.2.2 read) | risk: a written failure path must not add a trigger (CANON A34) | AC 25.1309-1B 2.2.2 |
| 19 | A failure mode is "not foreseeable" only if any knowledgeable person "would unequivocally conclude that a failure mode simply would not occur"; "Probabilistic methods may not be used" for that call | AC 25.1309-1B 7.3.2 | CERTAINTY, TWOREASONS | NICHE | Debt-limit standoffs (2011, 2013, 2023; Q4c; TMPG playbook, Q15 row 17) and broker failures are foreseeable, so they must be named or covered, not left out | The test binds aircraft designers, not advisers | VERIFIED (AC 7.3.2 read) | no | AC 25.1309-1B 7.3.2 |
| 20 | Guard against one event "adversely affecting ... any system and an associated safeguard"; no "new coupling factor" between defences | AC 25.1309-1B 7.4; NRC RG 1.174 Rev 3, defence-in-depth consideration 4 | COMPLETE2028, CAREER, CERTAINTY | NICHE | In 2027 the safeguard (the top-up, paid from the 2028 deposit) and the danger (falling rates) share one cause: a recession cuts her income while yields fall (NUMBERS 5; IPS l.9 makes the same point about shares). After a 2-point fall during 2027 the standard survives a deposit only up to 69.8% smaller; a 3.60-point fall before Jan 2027 takes all $150,000 (NUMBERS 5) | From January 2028 the coupling is gone: the top-up is owned | VERIFIED (AC 7.4 and RG 1.174 read) | risk: IPS l.13 "we'll simply complete it with the 2028 deposit" reads as unconditional (CANON D9 covers a smaller deposit) | AC 25.1309-1B 7.4 |
| 21 | A latent failure is "not detected or annunciated when it occurs"; designs limit how long one can stay hidden by checks at intervals | AC 25.1309-1B 1.5.21 | LADDER, CERTAINTY | KNOWN | A fund's lending loss or extraordinary cost (Q26 row 14) is latent until its holdings or net asset value show it; Table 3's yearly look at each fund is the check interval | Laura cannot undo a hidden loss, only see it early; the top-up absorbs it only at normal rates (row 11) | VERIFIED (AC 1.5.21 read) | no | AC 25.1309-1B 1.5 |
| 22 | After the first failure, "Subsequent failures ... and combinations thereof, should also be considered" | AC 25.1309-1B 2.2.1.2 | CERTAINTY, REINVEST, LADDER | NICHE | The top-up is sized for one stress. At 0% with the ETF fee the spare is $0 (NUMBERS 2, 8h); without the fee $1,414, which is 3.0% of IBTM's $47,413 zero-interest payout or 0.61% of the five funds' $230,655 (NUMBERS 8a; Keel arithmetic). So zero interest plus any fund friction leaves a payment short | Two unlikely events together; at the rates the market expects the spare is large (row 11) | VERIFIED (AC 2.2.1.2 read) | risk: CANON C9 lists NAV as a residual; NUMBERS does not size the joint case (Gaps) | AC 25.1309-1B 2.2.1 |
| 23 | Single-failure walk, part 1: what the top-up covers alone | Keel walk using AC 25.1309-1B 2.2.1.1; NUMBERS 2, 5, 8h | CERTAINTY, REINVEST, COMPLETE2028 | NICHE | Nothing earning interest (met exactly after the fee); rates 3 points lower for good ($25,651 left, NUMBERS 8h); every one of 585 historical windows (NUMBERS 2); a deposit up to 74.5% smaller at today's yields (NUMBERS 5) | Each holds from January 2028 only (row 2) | VERIFIED (NUMBERS and AC read) | no | Keel walk |
| 24 | Single-failure walk, part 2: what something other than the top-up covers | Keel walk; NUMBERS 8h; card Q26 rows 11, 14 | LADDER, RESERVE2033, CERTAINTY | NICHE | One fund paying below its holdings at expected rates (the top-up's money, never drawn then; $10,775 waiting on 1 Jan 2033). A fund ending late: sell its shares on the exchange (Q26 row 11). A Treasury payment late by five business days or less: every holding pays 0.5 to 10.5 months early (NUMBERS 8h) | Selling a fund on the exchange is a procedure at a market price, not "held to the end" | VERIFIED (NUMBERS 8h, Q26 read) | risk: IPS l.7 "Held to the end, these pay what they say" (CANON C2, D5; Q26 row 11) | Keel walk |
| 25 | Single-failure walk, part 3: single failures that nothing in the plan covers | Keel walk; NUMBERS 5; card Q26 row 22; SKELETON Exhibits item 4 | TWOREASONS, CERTAINTY, COMPLETE2028 | NICHE | A missed deposit: 2033 payment $3,016 short at forward rates, the ten $57,455 short at 0%, short in all 585 windows (NUMBERS 5). A custody failure above SIPC's $500,000, against about $589,000 held near Dec 2032 (Q26 row 22, Keel arithmetic). A US default or a delay over five business days. Two of the three are the IPS's two reasons; custody is not in the IPS | SEC rules keep client securities apart from the broker's own (not read), so a custody failure rarely loses them; it is the smallest of the three | VERIFIED (NUMBERS 5, Q26 read) | clash: "fail-safe" (claim 2) is false on three single failures. risk: custody versus IPS l.11 "anybody else's money", read strictly | Keel walk |
| 26 | Common cause beats redundancy: the plan's spare money sits in the same kinds of things as its main money | Keel analysis using ONR SAPs para 180; AC 25.1309-1B 1.5.27 | LADDER, CERTAINTY | NICHE | One issuer (the US Treasury) behind every rung, the top-up and the Treasury-bill ETF; one fund family behind five rungs (the ETF's own family is UNVERIFIED, NUMBERS 7); one custodian (assumed; the IPS is silent). The top-up is redundancy (more of the same Treasuries, NUMBERS 2), not diversity | For dollar payments nothing is safer than the issuer; diversifying away from it adds credit risk instead of removing it | VERIFIED (sources read) | no; the concentration is the design (SKELETON 2.3) | ONR SAPs; AC 25.1309-1B |
| 27 | Defence in depth: five levels (prevent; detect and control; design-basis safety systems; mitigate beyond the basis; emergency response), "as far as practicable, independent" | IAEA SSR-2/1 2.13, Requirement 7; ONR SAPs EKP.3, para 152, Table 1 | CERTAINTY, TWOREASONS, RESERVE2033 | KNOWN | Laura's map: level 1 the Treasuries held to the end; level 2 Table 3's signals; level 3 the top-up; level 4 what changes when a reason fires (partly written: CANON A34, NUMBERS 5); level 5 empty by design, since her flexibility is shares and co-sponsors' money is someone else's (IPS l.11). The Treasury-bill ETF is a support service, not a layer | Nuclear levels are separate hardware; Laura's share an issuer and a custodian (row 26) | VERIFIED (SSR-2/1 and SAPs read) | risk: drawing on her flexibility for payments would contradict IPS l.11 (CANON A5); a map, not a plan | IAEA 2.13; ONR Table 1 |
| 28 | Passive measures first, then automatic, then manual; administrative measures are acceptable where timescales are long | ONR SAPs EKP.5, paras 155, 194 | LADDER, TWOREASONS, CERTAINTY | NICHE | Treasuries held to the end are passive (nothing sold after January 2028, NUMBERS 8h); the top-up is passive once bought; only the two reasons need a person, and her timescales are months (deposit due by 31 March 2028; every holding pays at least half a month early) | The hierarchy is for plant safety systems | VERIFIED (SAPs read) | no | ONR EKP.5 |
| 29 | Redundancy answers random failure; diversity and segregation answer common cause; "claims for CCF should not be better than one failure per 100 000 demands"; no single random failure may stop a safety function | ONR SAPs para 180, EDR.2-EDR.4, para 185 | LADDER, CERTAINTY | NICHE | Names what the top-up is (redundancy) and what no permitted asset gives (diversity from the issuer). Also a ceiling on how certain any claim may sound: a regulator credits no better than 1 in 100,000 for a shared cause | Laura's "demands" are ten payment dates, not plant demands | VERIFIED (SAPs read) | no | ONR EDR |
| 30 | "The existence of multiple levels of defence is not a basis for continued operation in the absence of one level" | IAEA SSR-2/1 Rev.1 para 4.10 | TWOREASONS, CERTAINTY | NICHE | An engineering reason for IPS l.17: a missed deposit removes level 3 (the top-up); a US default removes level 1 (the base). Market falls and rate moves stay inside the design basis, so they change nothing | The IAEA demands a stop; the IPS says only that the plan would change | VERIFIED (SSR-2/1 4.9-4.13A read) | no; supports CANON A34 | IAEA 4.10 |
| 31 | Seven defence-in-depth considerations, including a reasonable balance among layers, no over-reliance on programmatic activities, redundancy, independence and diversity, and defences against common cause and human error | NRC RG 1.174 Rev 3, defence-in-depth section | PROCESS, CERTAINTY | KNOWN | A test for 3e: does the plan lean on a promise to act where it could lean on something owned? Laura's plan leans on ownership, except one step: buying the top-up in January 2028 | RG 1.174 governs changes to licensed plants, not new designs | VERIFIED (RG 1.174 Rev 3 read) | no | RG 1.174 |
| 32 | Safety goals are "aiming points or numerical benchmarks of performance", "not a substitute for existing regulations"; the 1 in a million large-release figure was only proposed; CDF 1e-4 and LERF 1e-5 a year are surrogates | NRC 51 FR 30028 (1986); RG 1.174 Rev 3 | CERTAINTY, PRESENTATION | KNOWN | No per-year target for Laura: even the NRC does not use its numbers as pass marks | NRC has reactor-years of experience; Laura's record is zero failures in 585 overlapping windows, which bounds little (Q4c) | VERIFIED (policy statement read in full) | no | NRC (1986) |
| 33 | ONR's Basic Safety Objectives are not to be used "as design targets, or as surrogates to denote when ALARP levels ... have been achieved"; meeting the limits does not prove risk is ALARP | ONR SAPs para 698, Annex 2; Targets 5 and 9 | CERTAINTY | NICHE | The same lesson from a second regulator: a stated frequency never proves safety | none recorded | VERIFIED (SAPs read) | no | ONR SAPs Annex 2 |
| 34 | ALARP (in law SFAIRP): reduce risk unless the cost is grossly disproportionate; HSE's guidance "rules out HSE accepting a less protected but significantly cheaper option"; "the disproportion must always be gross" (Lead, Thu 12 Nov: the no-interest standard is Keel's call of Tue 10 Nov inside the IPS's completion clause, never "Caplet chose a dearer standard"; INTENT failure 7) | Edwards v National Coal Board (1949), quoted in HSE R2P2 Appendix 3 para 4; HSE SPC/Permissioning/39; ONR SAPs para 12 | CERTAINTY, COMPLETE2028 | KNOWN | Claim 1's "no safer asset exists" is the wrong form. Right form: Caplet chose the dearer, more protective standard over Mon 9 Nov's 3-point margin ($13,220 more; that margin was $22,192 short at 0% and in 35 of 585 windows, NUMBERS 2), and within Wharton's permitted list nothing removes the US default | ALARP is a legal duty to workers and the public; Laura's is a client's wish ("a high degree of certainty"). Reasoning, never a label | VERIFIED (R2P2 read via a gov.uk-hosted copy; SPC/Permissioning/39 read) | no | HSE |
| 35 | "'Tolerable' does not mean 'acceptable'": three regions (unacceptable; tolerable if ALARP; broadly acceptable below about 1 in a million a year); absolute safety "cannot be guaranteed" | HSE R2P2 (2001) paras 122-132 | CERTAINTY, LAURA | KNOWN | The case asks for "a high degree of certainty", not absolute certainty: an engineer reads that as a tolerability standard set by the client. Supports CANON C13's reading of "near-ironclad" and the WORDS ban on "guaranteed" | R2P2's numbers are deaths a year, a different scale and a public-policy setting | VERIFIED (R2P2 read via a gov.uk-hosted copy) | no | HSE R2P2 |

## (b) Cards

**B1. Name the standard a design basis, not a beta (rows 1-9, 34).**
- *What is it?* Nuclear regulation states what a system must do and the bounding values it is designed for (10 CFR
  50.2, "reference bounds for design"), analysed with conservative assumptions (SSR-2/1 5.26). Events beyond the bound
  are named and handled by later levels (row 5). Structural codes instead state a target probability as a reliability
  index (EN 1990: beta 3.8 over 50 years for ordinary buildings).
- *Did it work?* The design-basis language is how US regulation (10 CFR 50) and the IAEA's requirements define what a
  plant must withstand; its known weakness, events beyond the basis, is why both add defence in depth and severe-event
  analysis. EN 1990's beta works for calibrating codes, but Annex C says it is "notional" and "does not necessarily
  provide an indication of the actual frequency of structural failure".
- *How is Laura's case like it?* Her standard is a function (ten $50,000 payments) plus a bound (zero interest after
  the ETF's fee). It is structural, not a probability (CANON A4), and the residuals are events outside the bound.
- *How is it not?* No regulator, no inspection; the bound is chosen, not physical. The residuals are several (CANON
  C9). A beta would be a false number: read from CDS prices her residual is beta 2.65-2.88 a year against a building's
  4.7 (row 8), and a bond reader distrusts Normal-tail numbers anyway (KMV, row 9).
- *What Caplet takes.* 3a: describe the standard as a test with a stated bound and named exceptions, dated from
  January 2028. No engineering labels in the report: the idea, not the word. One number: the top-up, $38,282, about a
  quarter of the deposit (NUMBERS 2). 3e: the list of what lies beyond the bound (missed deposit, custody, fund
  frictions beyond what the top-up absorbs, a long delay, a US default). Exhibit: none new; Figure 1's "interest earns
  nothing" bars already show the bound (NUMBERS 8h).

**B2. The single-failure walk kills "fail-safe" (rows 15, 22-25).**
- *What is it?* Aviation's fail-safe design concept assumes every single failure "regardless of its probability" and
  requires that none be catastrophic (AC 25.1309-1B 2.2.1.1; 14 CFR 25.1309(b)(1)(ii)); then it considers
  combinations (2.2.1.2).
- *Did it work?* It is the certification basis for transport aircraft systems in the US; the 2024 revision (AC
  25.1309-1B) tightened it by counting common-cause sets as single failures.
- *How is Laura's case like it?* A missed payment is her catastrophic outcome (the residency's operations). The walk
  sorts her single failures cleanly: the top-up covers zero interest, lower rates and every historical window; timing
  and procedure cover a fund paying low at expected rates, a late fund ending and a short delay.
- *How is it not?* Three single failures stop at least part of a payment with no cover in the plan: a missed deposit
  ($3,016 short in 2033 at forward rates, $57,455 at 0%; NUMBERS 5), a custody failure above SIPC's $500,000 (Q26 row
  22), and a US default or long delay. The joint case fails too: zero interest plus any fund friction (spare $0 after
  the fee, NUMBERS 8h).
- *What Caplet takes.* Never "fail-safe" (add it to the WORDS never-list: it is a certainty word, CANON C13, C21, check
  5). 3e: the walk as Table 3's logic, not as a table of its own: which single failure each row watches, and that two of
  the uncovered three are the IPS's two reasons. One number: $3,016 (the missed-deposit gap at forward rates).

**B3. Common cause defeats redundancy (rows 16, 20, 26, 29).**
- *What is it?* Redundancy (more of the same) protects against random failure; only diversity and segregation protect
  against a shared cause (ONR para 180). Since 2024 the FAA counts any set of failures that cannot be shown independent
  as one failure (AC 1.5.27), and guards against one event hitting both a system and its safeguard (7.4).
- *Did it work?* It is regulatory doctrine in both fields; ONR caps any common-cause claim at one failure per 100,000
  demands because shared causes are so hard to rule out.
- *How is Laura's case like it?* The top-up is redundancy: more of the same Treasuries (NUMBERS 2). Every layer rests
  on one issuer; five rungs on one fund family; all, probably, on one custodian. In 2027 the top-up's money and the
  danger it guards share a cause (a recession: her income falls while yields fall; NUMBERS 5).
- *How is it not?* For dollar payments the issuer concentration is the point: nothing is safer, so diversity would add
  risk, not remove it (SKELETON 2.3, "deliberately concentrated"). The fund-family and custody causes are small and
  slow.
- *What Caplet takes.* 2.3: the concentration is chosen, and its one shared cause is named (a US default). 3e: the 2027
  coupling in one clause, with NUMBERS 5's threshold (after a 2-point fall during 2027 the standard survives a deposit
  up to 69.8% smaller), stated as a risk, not a change. Gap for the numbers owner: a fund-family event across five rungs
  at once is not sized.

**B4. Defence in depth explains why the IPS has exactly two reasons (rows 27, 28, 30, 31).**
- *What is it?* Five levels of defence, independent as far as practicable (IAEA SSR-2/1 2.13, Requirement 7; ONR
  EKP.3), and the rule that having several levels "is not a basis for continued operation in the absence of one level"
  (4.10). Passive measures rank above active and manual ones (ONR EKP.5).
- *Did it work?* It is the organising principle of IAEA design safety requirements and UK and US nuclear regulation; RG
  1.174 turns it into seven considerations for any change to a plant.
- *How is Laura's case like it?* Level 1: the Treasuries held to the end (passive). Level 2: Table 3's signals. Level
  3: the top-up (passive once bought). The two reasons are exactly the two events that remove a level: a missed deposit
  removes level 3; a US default removes level 1. A fall in the market removes no level, so it changes nothing (IPS l.17).
- *How is it not?* The levels are not independent for the issuer or the custodian. Level 5 is empty by design (her
  flexibility and co-sponsors' money are barred from the payments, IPS l.11), and level 4 (what Caplet does when a
  reason fires) is only partly written.
- *What Caplet takes.* 3e: one sentence of reasoning for the two reasons (each removes a layer the payments stand on;
  a market fall removes none), plus what each reason changes (A34 allows showing it; NUMBERS 5 sizes the missed
  deposit). Never a new trigger. Exhibit: Table 3's "what it changes" column already carries this.

**B5. Different promises, different standards (rows 10, 17).**
- *What is it?* Reliability differentiation: the graver the consequence, the stricter the target (EN 1990 Annex B);
  aviation's inverse relationship of probability and severity (AC 4.1, Figure 4-1) with a shared risk budget (Appendix A).
- *Did it work?* Both are long-standing code practice; the FAA's 2024 AC kept the matrix and the apportionment.
- *How is Laura's case like it?* Her promises already carry graded standards: the ten are paid at zero interest; the
  bottom of the range is what the floor's holdings pay, less 0.5%; the top is missed in 5.99% of simulated futures if
  a fund costs 0.75%, by at most $429 (NUMBERS 8l); her flexibility is shares.
- *How is it not?* Engineering classes are set by law; Caplet chose Laura's, so the report must say why.
- *What Caplet takes.* 3c and 3e: why the confidence words differ (the payments are a bound; the range is a rule on
  owned holdings; her flexibility is shares). If one overall confidence is ever stated, it is the total over all
  residuals, not one at a time. No new exhibit.

**B6. No frequency target; the ALARP shape instead (rows 8, 32-35).**
- *What is it?* NRC safety goals are "aiming points"; ONR's objectives are not "design targets"; EN 1990's
  probabilities are "notional". What regulators require instead is ALARP: reduce risk unless the cost is grossly
  disproportionate, and never accept "a less protected but significantly cheaper option" (HSE SPC/Permissioning/39).
- *Did it work?* ALARP has been UK law since Edwards v NCB (1949) and runs through HSE and ONR practice.
- *How is Laura's case like it?* Caplet paid $13,220 more than Mon 9 Nov's cheaper 3-point margin to remove its $22,192
  shortfall at 0% and its 35 failing windows (NUMBERS 2): the more protective option chosen at a stated price.
- *How is it not?* ALARP is a legal duty; Laura's standard is a client's wish. And her one irreducible residual (a US
  default) has no price at which a permitted asset removes it.
- *What Caplet takes.* 3a: the price of the standard in one place (the top-up, $38,282; NUMBERS 2), and, if a judge
  might ask "why not cheaper?", the rejected cheaper option's shortfall. No per-year probability anywhere; Q4c's CDS
  figures stay a note, not a claim.

## (c) Verdicts

- **Claim 1: CHANGE.**
  - Keep: a bound, the things beyond it, and a reason to stop there. That is the right structure, and it already
    matches CANON A4 (structural, not a probability).
  - Change the name: "design basis" (nuclear) fits; EN 1990's beta does not. Beta is a calibration number that its own
    code calls notional (row 7). Any number Caplet could put in its place is a CDS price (an upper bound on a late
    payment) or a model zero (row 8).
  - Change "one named residual": CANON C9 already says default is not the only residual; row 25 lists three uncovered
    single failures, and row 22 a joint one.
  - Change "no safer asset exists": that is a fact about the permitted list, not an ALARP argument. The ALARP argument is
    the price Caplet paid for the more protective option (row 34).
  - Add the date: the standard holds from January 2028 (row 2). Before then the ladder alone stands.
  - Apt or stretch: apt for checking the plan and for one sentence of reasoning in 3e; a stretch as words in the
    report. A fixed-income judge knows "cash-flow matched" and "bounding test", not "design basis" or "beta".
- **Claim 2: KILL.** The plan passes the single-failure test for interest rates, for one fund paying low at expected
  rates, for a late fund ending and for a short delay. It fails for a missed deposit, a custody failure above SIPC and
  a US default (row 25), and under the 2024 FAA definition the five iBond rungs are one failure for any shared cause
  (row 16). "Fail-safe" is also a certainty word of the kind CANON C13 and C21 forbid. What survives is narrower and
  true: no single change in interest rates or share prices can stop a payment once the top-up is bought.
- **Claim 3: CHANGE.**
  - Defence in depth: KEEP as Caplet's audit and as the reasoning behind the two reasons (row 30). The layers are real
    but not independent (rows 26, 29). The missing piece the report can supply is what each reason changes (row 27);
    the missing piece it cannot supply is diversity from the issuer.
  - Frequency target per year: KILL (rows 32, 33). No regulator treats its number as a pass mark, and Laura has no data
    to make one.
- **Risk found in passing (not my claims; for the lead).** SKELETON 3d's note says "what can lower it (only a US
  default)". NUMBERS 8l shows the contribution below the stated bottom in 1 of 200,000 simulated futures if a fund costs
  0.75% ($211), and 5 paths at 1%; CANON C9 and the WORDS never-list ("the only exception") also stand against "only".

## (d) Gaps

- EN 1990:2023 (the second-generation Eurocode) not read; its reliability annex may differ. EN 1990:2002+A1:2005 was
  read from the BS EN text posted by Public.Resource.Org (a legal public posting of a standard CEN sells), through a
  mirror; sections 1.5, 2.1, 2.2, 3.2 and Annexes B and C were read, not the whole standard.
- EASA's AMC 25.1309 not read. AC 25.1309-1A (1988) not read: 1B cancels it, and 1B 2.2.1.2 carries the combination
  rule used in row 22.
- The JRC report on Eurocode reliability (JRC113687) was seen only as a search excerpt (UNVERIFIED); row 6 rests on
  EN 1990 and Keel arithmetic, not on it.
- Long documents (SSR-2/1, the ONR SAPs, RG 1.174, AC 25.1309-1B) were read at the sections cited, not cover to cover.
- The SEC customer protection rule (17 CFR 240.15c3-3) not read; custody is sized only through SIPC (Q26 row 22). One
  custodian is assumed; the IPS is silent.
- The Treasury-bill ETF and its fund family are UNVERIFIED (NUMBERS 7), so its share in the common cause is unknown.
- The iBond family's shared causes (board, lending programme) come from Q26, not re-read here.
- The fund-friction cover at 0% ($1,414 = 3.0% of IBTM's payout, 0.61% of the five funds') is Keel arithmetic on
  NUMBERS 8a and 8h; NUMBERS does not size a fund shortfall jointly with the zero-interest world (as Q31 row 28 also
  notes), nor a fund-family event across five rungs. For the numbers owner.
- The CDS-to-beta conversion (row 8) is Keel arithmetic; Q4c's CDS figures are upper bounds.
- HSE's own R2P2 page (hse.gov.uk/enforce/assets/docs/r2p2.pdf) was not used; R2P2 was read as a gov.uk-hosted copy
  filed in a public inquiry bundle. Same text; cite HSE as author.
- REFERENCES_APA.md had no entry for any source below (checked); all entries are new.

## Sources (APA 7; all accessed 12 Nov 2026)

- British Standards Institution. (2005). *Eurocode: Basis of structural design* (BS EN 1990:2002+A1:2005, incorporating
  corrigendum December 2008). Posted by Public.Resource.Org.
  https://www.phd.eng.br/wp-content/uploads/2015/12/en.1990.2002.pdf (sections 1.5, 2.1, 2.2, 3.2, Annex B and Annex C
  read; the CEN standard is sold, so this public posting was read).
- Crosbie, P., & Bohn, J. (2002). *Modeling default risk* [Technical document, revised 14 January 2002]. KMV LLC.
  http://marshallinside.usc.edu/dietrich/KMVModellingDefaultRisk2002.pdf (read in full).
- Definitions, 10 C.F.R. § 50.2 (2026).
  https://www.ecfr.gov/current/title-10/chapter-I/part-50/subject-group-ECFR1aad221999377bf/section-50.2 (definition of
  "design bases" read).
- Equipment, systems, and installations, 14 C.F.R. § 25.1309 (2026).
  https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-F/subject-group-ECFR4f2ea8e8dd5b4ad/section-25.1309
  (read in full).
- Federal Aviation Administration. (2024). *System design and analysis* (Advisory Circular No. 25.1309-1B). U.S.
  Department of Transportation. https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_25.1309-1B.pdf (sections
  1.3, 1.5, 2.2, 3.1, 3.3, 4.1, 7.3, 7.4 and Appendix A read).
- Health and Safety Executive. (2001). *Reducing risks, protecting people: HSE's decision-making process*. HSE Books.
  https://assets.publishing.service.gov.uk/media/6634988fcf3b5081b14f30cd/IQ8.10.J_Document_9_Health_and_Safety_Executive__Reducing_risks__protecting_people__HSE_s_decision-making_process__2001.pdf
  (read: the tolerability framework, paras 122-132, and Appendix 3).
- Health and Safety Executive. (2026, January 30). *HID's approach to ALARP decisions* (SPC/Permissioning/39). https://www.hse.gov.uk/foi/internalops/hid_circs/permissioning/spc_perm_39.htm (read
  in full).
- International Atomic Energy Agency. (2016). *Safety of nuclear power plants: Design* (IAEA Safety Standards Series No.
  SSR-2/1 (Rev. 1)). https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1715web-46541668.pdf (para 2.13, Requirement 7
  and paras 4.9-4.13A, para 5.26, Requirements 25-26 read).
- Office for Nuclear Regulation. (2020). *Safety assessment principles for nuclear facilities* (2014 ed., Rev. 1).
  https://www.onr.org.uk/media/pobf24xm/saps2014.pdf (paras 12, 152-156, 180-194, EKP.3, EKP.5, EDR.2-EDR.4, paras 610,
  698, 724, 768, Annex 2 and Targets 5 and 9 read).
- U.S. Nuclear Regulatory Commission. (1986). Safety goals for the operations of nuclear power plants; Policy statement.
  *Federal Register, 51*(162), 30028-30033. https://www.nrc.gov/reading-rm/doc-collections/commission/policy/51fr30028.pdf
  (read in full).
- U.S. Nuclear Regulatory Commission. (2018). *An approach for using probabilistic risk assessment in risk-informed
  decisions on plant-specific changes to the licensing basis* (Regulatory Guide 1.174, Rev. 3).
  https://www.nrc.gov/docs/ML1731/ML17317A256.pdf (the defence-in-depth considerations and the CDF and LERF acceptance guidelines read).
- Not read at the source (UNVERIFIED; for the record only): European Commission Joint Research Centre. (2018).
  *Reliability of structural members designed with the Eurocodes NDPs selected by EU and EFTA Member States*
  (JRC113687); Federal Aviation Administration. (1988). *System design and analysis* (AC 25.1309-1A).
- Legal case, cited as quoted in HSE (2001), Appendix 3: Edwards v National Coal Board [1949] 1 All ER 743.
- Repo files (not external sources): Wharton Global Youth Program, *Laura Gao 2026 client profile*
  (`competition/official/2026_27/`); `../../FINAL_IPS_as_submitted.txt`; `../../CANON.md` (A4, A5, A6, A34, C2, C9,
  C13, C21, D5, D9); `../../WORDS.md`; `../../SKELETON.md` (2.3, 3a, 3d, 3e, Exhibits item 4); `../../NUMBERS.md`
  sections 2, 3, 5, 7, 8a, 8h, 8l; cards Q4c, Q7, Q15, Q26, Q31.
