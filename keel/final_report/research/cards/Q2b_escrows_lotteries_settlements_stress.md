# Q2b research card: refunding escrows, lottery annuities and structured settlements under stress

**Date.** Thu 12 Nov 2026 (Sydney), which is Wed 11 Nov in the US. Web sources read with Parallel web_search and
web_fetch, all accessed 12 Nov 2026. A source read only as a search excerpt is marked UNVERIFIED.

**Report parts.** 3a (the ten operating payments and the operating reserve), 3e (assumptions, limits, Table 3
monitoring), 3d (only for row 9), 3f (no).

**Notes for the Final Report store, not report prose.** The plan is frozen: a clash is a risk to record, never a
change to propose. Plan figures come only from `../../NUMBERS.md` (section named in each row) and are MODEL. Dates and
day counts marked "Keel arithmetic" are calendar arithmetic on the sources named.

**Not re-carded (already in the store).** California lottery policy rules and the IRC 130(d)(2) "reasonably related"
test (Q16 rows 18-25, 34-35); MSRB "full cash or gross refunding" and the California lottery reserve (Q31); Moody's
2020 escrow method and the City of Austin escrow agreements (Q17, Q20); the 1979 delay and the debt limit (Q15); the
Lehman markup case (harvest H4-036); past iBond endings and the Fed holiday rule (Q16 rows 6, 12, 13). This card cites
or extends them only.

**Claims tested.**
1. "Full-cash municipal escrows and state lottery annuities, the closest cousins of Laura's plan, have essentially
   never failed to pay; where they did run short, the cause was something outside the bonds." (keep, kill or change)
2. "Structured settlements are certain only as far as the insurer behind them: when Executive Life failed in 1991,
   payees were cut." (keep, kill or change; with how much, how long, what a Treasury-funded settlement changes, and
   what having no insurer costs and saves Laura)
3. "A payment can be late without any bond defaulting: administration, custody and the calendar are the real risks
   in a fully funded schedule." (keep, kill or change; with the days of slack per payment from CANON B8)

**Problem class and the field that solved it.** A known stream of fixed nominal payments funded in advance (dedicated
funding). Public finance solved it with refunding escrows of Treasuries held by a trustee; lotteries with Treasury
zeros (or, for lifetime prizes, insurers' annuities); tort law with structured settlements funded by an insurer's
annuity or a Treasury. The failures in all three came from where the money sat (an insurer or a dealer), who could
release it (a legislature), or the plumbing that moves it (clearing banks, fund administrators, Fedwire).

## Verdicts in one screen

- **Claim 1: CHANGE.** No case found of a Treasury-only refunding escrow or a Treasury-funded lottery annuity failing to
  pay (absence in the record searched, not proof). The failures that did happen were in structures where the money sat
  in something other than Treasuries: about $3 billion of municipal bonds placed whole in an Executive Life contract
  in 1986 (bondholders lost; downgrade clauses have been required since, S5), and repos with a dealer that failed in
  1985 (ESM; about $300m lost by municipalities and others, UNVERIFIED). Yield burning (1990-94) cost issuers and the
  Treasury, never bondholders: more than $139m settled by 17 firms in 2000, preserving the tax exemption of more than
  3,600 issues (S1). Illinois 2015 was not a money failure: nearly 3,900 valid prize claims, more than $112m, waited
  up to about five months because nobody had legal authority to pay; all were paid within a month of the appropriation
  (S10). No lottery prize found cut by an insurer's failure; the lotteries kept the liability (S12, S13). Changed
  claim: "no Treasury-funded one found failing; the failures were in what held the money or who could release it".
- **Claim 2: KEEP, with numbers.** Executive Life (California): 75,000 annuitants paid 70% (GAO, S14), from 1 May 1991
  (S15); state guaranty associations filled the 30% gap up to their caps (Pennsylvania: $100,000 per life, $300,000
  in all) from about May 1992 (S15). Executive Life of New York: paid in full for twenty years under a 1992 plan, then
  liquidated; about 15% of some 10,000 payees cut, "some by significant percentages" (S16, S17); the run-off lasted from
  1991 to 2026 (S18). A Treasury-funded settlement under IRC 130 still leaves the payee a general creditor of the
  assignment company (S21). Laura owns her Treasuries directly.
- **Claim 3: KEEP, sized.** Slack between cash in hand and the last Fed business day before each 1 January (Keel
  arithmetic): the five iBond rungs 4 to 9 business days (7 to 13 calendar days; 2036 the tightest at 4 to 6); the
  three November bonds 30 to 31 business days (25 to 26 after a five-business-day Treasury default window); May-2038
  158; Feb-2037 220. One-day plumbing failures (BoNY 1985, Fedwire 2021) fit inside every rung if each payment is sent
  before the last business day. A week-long fund-administration failure (SunGard 2015, still unresolved after six
  days) in mid-December would cross 1 January for an iBond rung. For the iBond rungs the December risk is
  administration, not default.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Yield burning: from 1990 to 1994 dealers sold Treasuries into advance-refunding escrows at "excessive, undisclosed markups"; the 2000 global settlement took more than $139m from 17 firms, more than $120m of it to the Treasury to "preserve the tax-exempt status of more than 3600 separate issues", more than $18m to municipalities; every escrow still paid its bondholders | S1 (SEC press release 2000-45); S2 (SEC summary table: 3,706 deals, $170.9m in all with earlier cases) | LADDER, CERTAINTY, PROCESS | NICHE | The only thing an escrow buyer can lose is the price paid. Laura's equivalent is execution: card Q17 found the fills 2.6 to 8.8bp from the curve and flat $10 commissions | Extends H4-036 (one Lehman case) to the whole settlement; bondholders were never short, so this is a cost and tax story, not a payment failure | VERIFIED (S1 read in full); S2 totals UNVERIFIED (search excerpt) | no | Parallel web_fetch of sec.gov |
| 2 | SLGS sales were suspended 10 times in 1995-2014, average 69 days, longest 163 (Oct 1995-Mar 1996) and 152 (May-Oct 2013), always at the debt limit; escrows then buy open-market Treasuries, which Treasury said "might increase cost and cause inconvenience". Later suspensions: 2015, 2017-18, 2019, 2021, 2023 | S3 (CRS R41811, table of suspensions); S4 (TreasuryDirect releases) | TWOREASONS, LADDER, PROCESS | KNOWN | Does not touch Laura: she buys marketable Treasuries in Jan 2027 and Jan 2028 and never needs SLGS. The parallel is the debt-limit X-date near a date the plan needs cash, which SKELETON Table 3 row 3 already handles | Extends Q16's NYS GFOA line ("the SLGS window has regularly closed") with dates and lengths | VERIFIED (S3 read in full); post-2015 dates UNVERIFIED (release headings in search results) | no | congress.gov CRS page |
| 3 | Municipal bonds whose whole proceeds sat in an insurer's contract failed: Executive Life and Drexel issued about $3 billion of such bonds in 1986, "all of the bond issue was placed in an Executive Life GIC"; when the insurer failed bondholders lost, the commissioner tried to repudiate the contracts, courts later ruled for the holders, and downgrade clauses have been required ever since | S5 (Modugno 2000, Society of Actuaries); S6, S7 (LA Times 1991: Colorado and Nebraska agencies in default on $400m; $32.4m of Mello-Roos money frozen) | CERTAINTY, LADDER | NICHE | The money must sit in the Treasury itself, not in someone's promise to pay a Treasury-like return. Laura holds Treasuries and Treasury funds; her waiting money sits in a Treasury-bill ETF (NUMBERS 0), not a contract | These were new-money bonds, not refunding escrows; still the closest structure that broke | VERIFIED (S5 read in full); S6, S7 amounts UNVERIFIED (excerpts) | no | soa.org; latimes.com archive |
| 4 | ESM Government Securities (1985): municipalities had lent cash to a dealer on repos whose Treasury collateral was not held in their name; when the dealer failed, losses were estimated at about $300m, with at least 50 municipalities affected | S8 (Chicago Tribune, 11 Mar 1985); S9 (Morning Call, 1 Apr 1985) | RESERVE2033, PROCESS | KNOWN | Custody is part of certainty: the Treasuries must be held for the owner, not lent out. Laura's are held by a regulated broker; SIPC covers $500,000 against $589,655 at the end (NUMBERS 8k), already a set-up decision in SKELETON item 4(c) and Q26 row 22 | Excerpts only; figures not checked against a court or SEC record | UNVERIFIED (newspaper excerpts) | no | Parallel web_search |
| 5 | The record, read across rows 1-4 and 10-11: no Treasury-only escrow or Treasury-funded lottery annuity found that failed to pay; every failure found sat in an insurer, a dealer or an appropriation | Keel synthesis of S1-S13 | CERTAINTY, LADDER | NICHE | Supports the IPS's "Held to the end, these pay what they say" with history, and names exactly what is outside the bonds: who holds them, who can release the cash, how it moves | Absence of a found case is not proof; rating-agency default studies of pre-refunded bonds not read (Gaps) | UNVERIFIED (as a universal statement) | no; agrees with IPS l.13 and CANON C9 | This run |
| 6 | Illinois Lottery 2015: from 1 Jul 2015 prizes over $25,000 were delayed, later prizes over $600; "nearly 3,900 valid claims being delayed, totaling more than $112 million. Within a month of receiving an appropriation, all valid claims were paid"; "the Illinois Lottery has the money to pay" | S10 (Lottery statement reproduced by KWQC, 27 Jun 2017) | PROCESS, RESERVE2033, LAURA | NICHE | Money present, payment late: the failure was legal authority to release it. Laura's version is who can sell and send $50,000 each January if she cannot act (travel, illness, Taiwan) | Public body; Laura is a private payer with no appropriation step | VERIFIED (S10 read in full) | no | kwqc.com |
| 7 | Winners sued (Rasche v. Lane, N.D. Ill., Dec 2015): dismissed on Eleventh Amendment immunity; the prize money sat in a fund "subject to legislative appropriation", so payees had no court remedy while they waited | S11 | PROCESS | NICHE | A payee's certainty includes a remedy; Laura's payees depend on her own instruction, not a court | She has no immunity and no appropriation; the parallel is only that money in place is not the same as money paid | VERIFIED (opinion text read in full, CounselStack copy) | no | law.counselstack.com |
| 8 | Illinois 2017 repeat: delays for claims over $25,000 from 1 Jul 2017 and Powerball and Mega Millions sales suspended from 28 and 30 Jun 2017; bills for a continuing appropriation (SB 1497, HB 3448) "would have provided the Lottery with a continuing appropriation ... to avoid payment delays" but stayed in committee | S10; S27 (sales back 6 Jul 2017) | PROCESS, RESERVE2033 | NICHE | The fix the payer asked for was a standing authority. Laura's equivalent is a standing instruction with the custodian for all ten January transfers, plus a named second person able to act (a set-up note, not a new rule) | Set-up detail; not in the case; must not read as a third reason to change the plan | VERIFIED (S10 read in full); S27 date UNVERIFIED | no | kwqc.com; news-gazette.com excerpt |
| 9 | Lateness cost trust even with money in hand: the Lottery estimated lost sales of $66.5m to $71.5m while it could not pay (14 Oct-14 Dec 2015) and "continues its work to regain the trust of its players" | S10 | COSPONSOR, PROCESS | NICHE | For co-sponsors the cost of a late payment is credibility, not dollars; on time every January is part of what Laura can show by 2031 | Players are not co-sponsors; one public body's estimate | VERIFIED (S10) | no | kwqc.com |
| 10 | Illinois switched lottery funding in 1985 from insurers to Treasuries: before 30 Jul 1985 prizes were funded by "annuities under group contracts" and "The Department would be liable for future payments if the insurance companies were to default"; since then only direct US obligations, Treasury zeros "held by a custody bank in the name of the State Treasurer", "maturities scheduled to coincide with cash requirements"; fair value $290,011,101 (30 Sep 2020) | S12 | LADDER, CERTAINTY | NICHE | The closest public twin of Laura's ladder: dated Treasuries, held in the payer's own name, maturing for each payment. Laura's rungs end before each payment rather than on it (CANON B8) | Lottery zeros match each date; Laura's coupon bonds and funds need waiting money (NUMBERS 2) | VERIFIED (S12 read in full) | no | illinoislottery.com PDF |
| 11 | Minnesota went the other way in 2004: it sold its zero-coupon government securities and bought lifetime annuities from insurers in each winner's name, because the prizes are paid for life; 27 are active; the state guaranty fund covers $300,000 per annuity, and the Lottery "may be ultimately responsible" | S13 | CERTAINTY, LADDER | NICHE | When the number of payments depends on how long someone lives, an insurer earns its place (it pools lives). Laura's ten are fixed in number and date, so Treasuries fit and an insurer would add only its own credit risk | One state, small book; the reason for the 2004 switch is inferred from the prizes being for life, not stated | VERIFIED (debt administration section and note 10 read; not every page) | no | mnlottery PDF |
| 12 | The payer stays on the hook whatever it buys: Illinois has "an unconditional obligation to pay all grand prizewinners" and was liable if insurers defaulted; Minnesota "may be ultimately responsible" above the guaranty fund | S12; S13 | CERTAINTY, LAURA | NICHE | Lottery winners had a state behind the asset. Laura's payments have nothing behind the asset ("no outside money", case), which is why the asset must be the one that does not need a second payer | Inference from two filings | VERIFIED (S12, S13 passages read) | no | as rows 10-11 |
| 13 | Executive Life (California), seized April 1991: "the 75,000 annuitants of Executive Life are being paid only 70 percent of their benefits"; the cut ran from 1 May 1991 | S14 (GAO T-GGD-92-43, 9 Sep 1992); S15 (625 A.2d 1286) | CERTAINTY | KNOWN | Sizes the claim: a 30% cut to every annuitant at once, for an insurer rated triple A five years earlier (S5) | The store's H7-038 says "373,000+ customers"; GAO counts 75,000 annuitants (Gaps) | VERIFIED (S14, S15 read in full) | no | gao.gov; courtlistener |
| 14 | Why it failed: junk bonds, fast growth, surplus-relief reinsurance and regulators' forbearance; a run of about $4bn in 1990; "Without surplus relief reinsurance ... insolvent as early as 1983" | S14 | CERTAINTY | KNOWN | An insurer's promise rests on its balance sheet and its regulator; the four failures GAO studied held nearly $85bn for more than 900,000 policies | Testimony, not an audit of every claim | VERIFIED (S14 read in full) | no | gao.gov |
| 15 | How long the cut lasted: a rehabilitation plan (Aurora National Life) with a guaranty-association agreement to "fill in the 30% gap" up to each state's caps; Pennsylvania's association was ordered to start within 90 days of 18 Feb 1992; caps $100,000 per life, $300,000 in all | S15 | CERTAINTY | NICHE | About a year at 70% for most; full only up to the caps. Laura's ten payments total $500,000, above any single cap shown | Caps vary by state and year; only Pennsylvania's read | VERIFIED (S15 read in full) | no | courtlistener |
| 16 | Executive Life of New York: paid in full from a 1992 plan for twenty years, then liquidated (2012, affirmed 2013); liabilities exceeded assets by $1.5bn; of about 10,000 payees about 85% paid in full and 15% less, "some by significant percentages"; funding from the estate, about $700m from guaranty associations, a $71m industry addition and a $100m hardship fund | S16 (Nassau County, 16 Apr 2012); S17 (2d Dept, 6 Feb 2013) | CERTAINTY | NICHE | A promise can look kept for twenty years and still fail; certainty is a property of the asset, not of the track record | Mostly structured-settlement payees with long, large contracts | VERIFIED (S16, S17 read in full) | no | justia; nycourts.gov |
| 17 | Why New York's case worsened: "Capital market developments of the late 1990s and through 2002 ... severe negative effect on the ELNY portfolio, and also (perhaps more significantly) on the value of the SSA liabilities": falling rates raised the value of long fixed payments faster than the assets | S18 | REINVEST, CERTAINTY, COMPLETE2028 | NICHE | The same force the top-up answers: without it the ten as written are $54,595 short if interest earns nothing, and short in 55.6% of 585 historical windows (NUMBERS 2, MODEL); with it, $1,414 spare at 0% | ELNY's liabilities were for life and decades long; Laura's are ten dated payments | VERIFIED (S18 read in full) | no | nylifega.org |
| 18 | The tail: rehabilitation from April 1991, liquidation 8 Aug 2013, the guaranty corporation paid more than $1.1bn to 30 Jun 2026, Pacific Life took over the obligations on 1 Jul 2026: about 35 years | S18 | CERTAINTY | NICHE | An insurer failure is not one bad day; payees lived inside it for decades | One company | VERIFIED (S18) | no | nylifega.org |
| 19 | Who bore ELNY's loss: advocacy sources say about 1,550 payees short by about $900m, averaging $600,000, all but 31 of them structured settlements, some cut more than 60% | S19 (AIRROC 2012); S20 (Edward Stone) | CERTAINTY | NICHE | Shows who carries the gap when caps bind: the largest, longest contracts | Advocacy figures, not court-checked | UNVERIFIED (excerpts) | no | Parallel web_search |
| 20 | IRC 130: a qualified funding asset is an insurer's annuity "or any obligation of the United States"; payments must be "fixed and determinable" and "cannot be accelerated, deferred, increased, or decreased by the recipient"; rights greater than "those of a general creditor" are disregarded | S21 | CERTAINTY, LADDER | NICHE | Even a Treasury-funded settlement leaves the payee a general creditor of the assignment company that owns the Treasury. Laura owns hers directly; only her custodian stands between her and the Treasury | Extends Q16 (the "reasonably related" test) with the general-creditor point | VERIFIED (LII text read in full) | no | law.cornell.edu |
| 21 | Tax law makes a settlement unchangeable by the payee; Caplet's plan is unchangeable by choice except for two defined reasons | S21; FINAL IPS ("only 2 possible reasons") | TWOREASONS | NICHE | The structured-settlement rule is an outside precommitment; the IPS's is self-imposed. Same aim: the payments cannot be raided or moved | Analogy only; card Q7 holds precommitment | VERIFIED (S21); analogy is Keel's | no | This run |
| 22 | What having no insurer costs Laura and saves her: no pooling of lives (worthless here, the ten are not for life), no guaranty fund (caps of $100,000-$300,000 would not cover $500,000 anyway), no insurer's load or spread; she keeps ownership, the right to sell, and what is left (12.8% of all money at the end returns to her, NUMBERS 8k, MODEL) | S11 to S21; NUMBERS 8k | CERTAINTY, LAURA, OTHER | NICHE | The answer to "why not just buy an annuity": an annuity fits payments that depend on a life; hers depend only on the calendar | Insurer annuity quotes for a ten-year period-certain contract not priced (Gaps) | VERIFIED (caps S15, S13); inference marked | no | This run |
| 23 | iBond rungs, slack: each fund ends on or about 15 Dec; past funds paid holders 3 to 7 days later (Q16 row 6); 1 Jan is a Fed holiday. From cash in hand to the last Fed business day before 1 Jan: 2033 7-9 business days, 2034 5-8, 2035 4-8, 2036 4-6, 2037 6-8 (7 to 13 calendar days) | Keel arithmetic on S22 (Fed holiday rule), Q16 rows 6 and 13, CANON B8 | RESERVE2033, LADDER, PROCESS | NICHE | Sizes the thinnest margin in the plan. It is days, not weeks | Q16 row 13 says "weeks of slack exist on every rung": true for the T-bonds, not for the iBond rungs | VERIFIED (dates and rule); arithmetic is Keel's | risk: Q16 row 13's wording; CANON B8's 17 days run to 1 Jan, not to cash in hand | This run |
| 24 | For the iBond rungs the Treasury default risk sits months earlier than the payment: each fund's money waits in cash for 5.4 to 7.4 months before the end (NUMBERS 3, MODEL), so a late Treasury maturity inside a fund mostly lands in mid-year; the December risk is the fund's own process (final value, final distribution) | NUMBERS 3; S24; S25 | RESERVE2033, TWOREASONS, LADDER | NICHE | Splits the iBond rung's two risks: the five-business-day Treasury trigger and the fund's December administration. Only the second sits close to 1 Jan | NUMBERS 3's months may be an average; a note maturing in late 2032 inside the fund not checked (Gaps). Refines Q15 row 30 | VERIFIED (NUMBERS 3); inference marked | risk: CANON C9 (default is not the only residual); this sizes the other residual | This run |
| 25 | T-bond rungs, slack (Keel arithmetic): Feb-2037 pays Tue 17 Feb 2037, 317 days and 220 business days before Thu 31 Dec 2037; May-2038 pays Mon 17 May 2038, 228 and 158; Nov-2039 45 and 31 (to Fri 30 Dec 2039); Nov-2040 46 and 30; Nov-2041 46 and 30. After a full five-business-day default window the November bonds keep 25-26 business days | S22; Q16 row 12 (31 CFR 356.30); SKELETON item 4(a) trigger | LADDER, TWOREASONS, RESERVE2033 | NICHE | Every T-bond rung absorbs a payment delayed inside the default window, and a 1979-length delay (18 days, Q15) | Long waits cost interest instead (TNA note 1's "10.5-month gap"), which the top-up prices | VERIFIED (dates); arithmetic is Keel's | no | This run |
| 26 | Bank of New York, 21-22 Nov 1985: a software flaw failed at 32,000 transactions and the bank could not redeliver Treasuries it received; it borrowed $22.6bn overnight from the New York Fed ($23.6bn in all); the next day the Fed stopped transfers to its account for about 1.5 hours; fixed and repaid later on 22 Nov | S23 (Richmond Fed EB15-05) | PROCESS, RESERVE2033 | KNOWN | A clearing or custody failure of one to two days, with the Treasuries themselves sound: fits inside every rung's slack if the payment is not left to the last business day | 1985 systems; scale far beyond Laura's | VERIFIED (S23 read in full) | no | richmondfed.org PDF |
| 27 | SunGard InvestOne / BNY Mellon, Aug 2015: an operating-system change on 22 Aug corrupted fund accounting and the backups failed; more than 10% of US ETFs and some mutual funds could not be priced (26 ETF providers, 20 fund companies); on 28 Aug mutual fund prices still had "no ETA"; ETF creations and redemptions kept settling at actual prices (Guggenheim) | S24 (Financial Planning, 28 Aug 2015); S25 (Reuters) | RESERVE2033, PROCESS, LADDER | NICHE | The real case for an iBond rung: its final payout needs a fund administrator to strike a final value. A week like this starting on a fund's last day would push cash past 1 Jan; the exchange stayed open, so a sale before the last trading day was still possible | Not an ending fund; prices were struck manually or late, not lost | VERIFIED (S24 read in full); S25 excerpt | risk: IPS l.13 "Held to the end": a sale before the end departs from it; Q30 row 4 already allows one for an extension | financial-planning.com |
| 28 | Fedwire and FedACH, 24 Feb 2021: all 14 Fed services down from about 11:15 a.m. ET, Fedwire Funds and Securities back at 3:14 p.m., FedACH at 2:57 p.m.; "human error" (maintenance run in business hours); in 2019 a three-hour Fedwire outage and a two-day ACH delay | S26 (Banking Dive) | RESERVE2033, PROCESS | KNOWN | A one-day wire failure on the last business day of December would make a payment late; sending on the second-to-last business day removes it | Hours, not days | VERIFIED (S26 read in full; the Fed's own status post not read) | no | bankingdive.com |
| 29 | The December calendar for the ten transfers (last Fed business day before each 1 Jan): Fri 31 Dec 2032, Fri 30 Dec 2033, Fri 29 Dec 2034, Mon 31 Dec 2035, Wed 31 Dec 2036, Thu 31 Dec 2037, Fri 31 Dec 2038, Fri 30 Dec 2039, Mon 31 Dec 2040, Tue 31 Dec 2041 | Keel arithmetic on S22 | RESERVE2033, PROCESS, PRESENTATION | NICHE | Gives Table 3 row 4 ("cash not credited by 28 Dec") real dates per year, and the send-by date one business day earlier | K.8 lists holidays only to 2030; the Saturday and Sunday rule is assumed to hold | VERIFIED (rule); dates are Keel's | no | This run |

## (b) Cards

**Card 1. Where the money sits decides whether it pays (rows 3, 5, 10, 11, 12).**
- What is it? Three families fund fixed payments in advance: refunding escrows (Treasuries held by a trustee),
  lottery annuities (Treasury zeros, or insurers' annuities for lifetime prizes), muni bonds parked in an insurer's
  contract.
- Did it work? The Treasury versions: no failure to pay found. The insurer version broke in 1991 (about $3 billion
  issued in 1986, S5). Illinois moved from insurers to Treasuries in 1985 and has funded with Treasury zeros "held ...
  in the name of the State Treasurer" since (S12). Minnesota moved the other way in 2004, but only for prizes paid for
  life (S13).
- How is Laura's case like it? Ten fixed dates, funded in full in advance, from Treasuries held for the payer.
- How is it not? No trustee, no verifier, no state behind the asset: if the asset fails, no second payer exists.
- What Caplet takes: 3a, one line of history behind "Held to the end, these pay what they say": the arrangements that
  failed held a promise, not a Treasury. 3e: the "why not an annuity" answer from row 11 (an insurer pools lives; the
  ten are not for life). No new exhibit.

**Card 2. Executive Life, both companies: what payees lost and for how long (rows 13-20).**
- What is it? The largest life-insurer failures of 1991; their structured-settlement and annuity payees were cut.
- Did it work? California: 75,000 annuitants at 70% from 1 May 1991 (S14, S15), topped up to state caps from about
  May 1992 (S15). New York: full payments for twenty years, then 15% of about 10,000 payees cut from 2013 (S16, S17); a
  35-year tail (S18).
- How is Laura's case like it? Fixed nominal payments promised years ahead, funded by a pool of bonds.
- How is it not? Her payees rely on Treasuries she owns, not on a company that owns them. Even an IRC 130
  Treasury-funded settlement leaves the payee a general creditor (S21).
- What Caplet takes: 3e assumptions note: the one residual left is the Treasury itself, named as reason 2. Numbers to
  quote: 70%, 75,000, about a year to partial repair. Laura's plan keeps the WORDS name: paid even if interest earns
  nothing, barring a US default.

**Card 3. Falling rates broke an insurer; the top-up answers the same force (row 17).**
- What is it? New York's guaranty corporation says falling rates after the late 1990s raised the value of ELNY's long
  fixed payments, perhaps more than they hurt its assets (S18).
- Did it work? No: the gap reached $1.5bn (S16).
- How is Laura's case like it? Her ten as written depend on interest earned on waiting money: $54,595 short if it
  earns nothing, short in 55.6% of 585 historical windows, median $1,592, worst $45,266 (NUMBERS 2, MODEL).
- How is it not? Her exposure is ten years and capped; ELNY's was for life and decades long.
- What Caplet takes: 3a, the reason the top-up exists, in one historical sentence: a payer whose bonds did not match
  its dates lost when rates fell. The top-up ($38,282 = $2,388 the ten still lack plus $35,894 so interest is never
  needed, NUMBERS 2) makes the ten paid even if interest earns nothing, barring a US default.

**Card 4. Illinois: the money was there, the payment was late (rows 6-9).**
- What is it? A state lottery that held the prize money but had no legal authority to release it for five months.
- Did it work? Paid in full within a month of the appropriation; about 3,900 claims, more than $112m (S10); no court
  remedy meanwhile (S11); lost sales of $66.5m to $71.5m.
- How is Laura's case like it? Her ten payments need someone with authority to sell and send $50,000 each January,
  from 2033 to 2042, possibly while she lives in Taiwan.
- How is it not? No legislature; one owner who can sign.
- What Caplet takes: 3a or 3e, a set-up note: a standing transfer instruction for the ten payments with the custodian,
  and a named second person able to act. 3d: on time every year is what co-sponsors see. Not a rule, not a trigger.

**Card 5. The December calendar: slack per rung and what eats it (rows 23-29).**
- What is it? Days between cash in hand and the last Fed business day before each 1 January (Keel arithmetic, S22,
  Q16 row 6, CANON B8).

| Payment | Rung | Cash in hand | Last business day | Calendar days | Business days |
|---|---|---|---|---|---|
| Pay 2033 | IBTM | Mon 20 to Wed 22 Dec 2032 | Fri 31 Dec 2032 | 9 to 11 | 7 to 9 |
| Pay 2034 | IBTO | Mon 19 to Thu 22 Dec 2033 | Fri 30 Dec 2033 | 8 to 11 | 5 to 8 |
| Pay 2035 | IBTP | Mon 18 to Fri 22 Dec 2034 | Fri 29 Dec 2034 | 7 to 11 | 4 to 8 |
| Pay 2036 | IBTQ (15 Dec 2035 is a Saturday; end taken as Mon 17 Dec, as IBTE in 2024) | Thu 20 to Mon 24 Dec 2035 | Mon 31 Dec 2035 | 7 to 11 | 4 to 6 |
| Pay 2037 | IBTR | Thu 18 to Mon 22 Dec 2036 | Wed 31 Dec 2036 | 9 to 13 | 6 to 8 |
| Pay 2038 | 4.750% Feb-2037 | Tue 17 Feb 2037 | Thu 31 Dec 2037 | 317 | 220 |
| Pay 2039 | 4.500% May-2038 | Mon 17 May 2038 | Fri 31 Dec 2038 | 228 | 158 |
| Pay 2040 | 4.375% Nov-2039 | Tue 15 Nov 2039 | Fri 30 Dec 2039 | 45 | 31 |
| Pay 2041 | 4.250% Nov-2040 | Thu 15 Nov 2040 | Mon 31 Dec 2040 | 46 | 30 |
| Pay 2042 | 3.125% Nov-2041 | Fri 15 Nov 2041 | Tue 31 Dec 2041 | 46 | 30 |

- Did it work? Past iBond endings paid 18-22 Dec (Q16 row 6, Q30 row 4). Plumbing failures of hours to two days
  (BoNY 1985, Fedwire 2021) fit every rung if the transfer goes on the second-to-last business day. A week-long
  administration failure (SunGard 2015) starting at a fund's end would not fit an iBond rung.
- How is Laura's case like it? Five payments rest on a fund's final distribution in the last two weeks of December.
- How is it not? The T-bond rungs have one to ten months, so only the iBond rungs are tight.
- What Caplet takes: 3e and Table 3 row 4: (i) the dates in row 29; (ii) the decision point for an iBond rung is its
  last trading day (about 15 Dec), since after it the shares cannot be sold; a public administration problem before
  that day leaves one act, an exchange sale settling the next business day (T+1, Q16 row 13); (iii) "cash not credited
  by 28 Dec" is then a look-closer with no act left behind it, and the payment would be late by days, logged, never
  reason 2. Section 2 can show the slack column in the holdings table only if space allows.

## (c) Verdicts

**Claim 1: CHANGE.**
- Kept: no Treasury-only refunding escrow or Treasury-funded lottery annuity found that failed to pay (rows 1, 2, 5,
  10). The Treasury failed to pay neither escrow holders nor lottery winners in the record searched.
- Changed: "essentially never failed" is too broad for the family. Structures that parked the money with an insurer
  (1986 Executive Life muni bonds, S5) or a dealer (ESM 1985, UNVERIFIED) did fail, and bondholders lost. "Something
  outside the bonds" has three named parts: what holds the money, who can release it, how it moves.
- Each case asked for:
  - Yield burning: promised an escrow at fair market prices; dealers marked up the Treasuries; more than $139m (2000
    settlement, 17 firms) and more than $172m from 21 firms with earlier cases (S1); bondholders paid in full. For
    Laura: only as a price risk, already measured (Q17).
  - SLGS suspensions: promised a supply of special Treasuries; ten suspensions in 1995-2014, average 69 days (S3);
    escrows bought open-market Treasuries. For Laura: no (she never needs SLGS).
  - Refunded bonds that defaulted: none found where the escrow held only Treasuries. The insurer-held cases are row 3.
  - Illinois 2015: promised prompt prize payment; no appropriation; about 3,900 claims, more than $112m, up to about
    five months late, then paid (S10). For Laura: the authority-to-pay version only (card 4).
  - A lottery's annuity provider failing: none found that cut a winner; both lotteries read keep the liability above
    the insurer (S12, S13).

**Claim 2: KEEP, with numbers.**
- California: 75,000 annuitants at 70% (S14) from 1 May 1991 (S15); the 30% gap filled by guaranty associations up to
  caps from about May 1992 (Pennsylvania: $100,000 per life, $300,000 in all, S15). So about a year at 70%, then full
  up to the caps.
- New York: 100% for twenty years, then about 15% of some 10,000 payees cut from 2013, some heavily (S16, S17);
  run-off to 2026 (S18). Falling rates were a main cause (S18).
- Treasury-funded settlements: allowed (IRC 130(d)), but the payee is still a general creditor of the assignment
  company (S21). The Treasury inside does not belong to the payee.
- What no insurer costs Laura: no pooling of lives (of no value for ten dated payments); no guaranty fund (caps would
  not cover $500,000). What it saves: insurer credit risk, the insurer's load, the middleman; she keeps ownership,
  liquidity and what is left (NUMBERS 8k).

**Claim 3: KEEP, sized.**
- Slack per payment: card 5. iBond rungs 4 to 9 business days; T-bonds 30 to 220.
- Operational failures and whether they apply:
  - Custody (ESM 1985): applies as SIPC and custody set-up; already in SKELETON item 4(c).
  - Clearing bank outage (BoNY 1985, one to two days): applies; fits if sent before the last business day.
  - Fund administration outage (SunGard 2015, a week or more): applies to the five iBond rungs only; does not fit.
  - Payment network outage (Fedwire 2021, hours): applies; fits if sent on the second-to-last business day.
  - Authority to pay (Illinois 2015, months): applies as a set-up step (card 4).
  - Calendar (1 Jan a holiday; weekend 15ths): applies; dated in row 29.
  - Treasury delay (1979, 18 days, Q15): absorbed by every T-bond rung; for the iBond rungs most of the Treasury
    money is already in cash months before the end (row 24), so the December exposure is the fund's own process.

## (d) Gaps

- No rating-agency study of pre-refunded or escrow-backed bond defaults was read; row 5 is absence of evidence. A
  search for escrow verification errors found only defeasance notices (EMMA), no failures.
- LA Times 1991 figures (Colorado and Nebraska, $400m; $1.8bn of bonds backed by Executive Life contracts; $32.4m of
  Mello-Roos money) and ESM 1985 figures are from excerpts only. A court record for the 1991 muni-contract cases was not
  found.
- Post-2015 SLGS suspension dates and GAO-12-701's 2011 dates (6 May to 2 Aug, against CRS's 6 May to 1 Aug) seen only
  in excerpts.
- ELNY's loss by payee (AIRROC, Edward Stone) not checked against court filings.
- The store's harvest H7-038 says Executive Life cut payments "30% for 373,000+ customers" (medium-reliability source).
  GAO (S14) gives 75,000 annuitants at 70%. The larger number may count all policyholders; the report should use GAO's.
- CRS R41811 (2015 update): the authors were not printed in the HTML read; the APA entry uses CRS as author until the
  PDF cover is checked.
- Minnesota's 2025 financial statements: read in the debt administration section and note 10 only; the title in the
  APA entry is descriptive.
- Each iBond fund's last Treasury maturity before its end was not checked (row 24 rests on NUMBERS 3's months of cash
  wait). The fund's final cash holdings (bills or a money market fund) are not published in advance.
- The Fed's K.8 table runs only to 2030; row 29 assumes the Saturday and Sunday rule still holds in 2032-2041.
- Quotes for a ten-year period-certain annuity from an insurer were not priced, so row 22's "insurer's load" is not
  sized.
- IBTQ's 2035 last trading day is not yet announced (15 Dec 2035 is a Saturday); card 5 assumes Mon 17 Dec, as IBTE did
  in 2024.

## Sources (APA 7; all accessed 12 Nov 2026)

- S1. U.S. Securities and Exchange Commission. (2000, April 6). *SEC settles with ten brokerage firms as part of
  global resolution of yield burning claims* (Press Release No. 2000-45).
  https://www.sec.gov/newsroom/press-releases/2000-45-sec-settles-ten-brokerage-firms-part-global-resolution-yield-burning-claims
  (read in full)
- S2. U.S. Securities and Exchange Commission. (n.d.). *Supplementary news material: Summary of yield burning
  settlement payments*. https://www.sec.gov/news/extra/yeildb.htm (search excerpt only; UNVERIFIED)
- S3. Congressional Research Service. (2015). *State and local government series (SLGS) Treasury debt: A description*
  (CRS Report No. R41811; updated October 29, 2015). https://www.congress.gov/crs_external_products/R/HTML/R41811.html
  (read in full)
- S4. U.S. Department of the Treasury, Bureau of the Fiscal Service. (2015-2023). *Treasury to suspend [resume] sales
  of State and Local Government Series securities* [Press releases]. TreasuryDirect. For example
  https://treasurydirect.gov/news/2023/release-06-05-slgs and https://slgs.gov/news/2021/release-12-16 (headings and
  excerpts only; UNVERIFIED)
- S5. Modugno, V. (2000, September). Municipal reinvestment contracts. *Risks and Rewards*, (35), 12-14. Society of
  Actuaries. https://www.soa.org/globalassets/assets/library/newsletters/risks-and-rewards/2000/september/rar-2000-iss35-modugno.pdf
  (read in full)
- S6. Los Angeles Times. (1991, May 3). Executive Life failure reaches muni bonds.
  https://www.latimes.com/archives/la-xpm-1991-05-03-fi-1068-story.html (excerpt only; UNVERIFIED)
- S7. Los Angeles Times. (1991, December 8). Agencies' bonds frozen in Executive Life bankruptcy.
  https://www.latimes.com/archives/la-xpm-1991-12-08-mn-387-story.html (excerpt only; UNVERIFIED)
- S8. Chicago Tribune. (1985, March 11). Bond search pressed in firm's failure.
  https://www.chicagotribune.com/1985/03/11/bond-search-pressed-in-firms-failure (excerpt only; UNVERIFIED)
- S9. The Morning Call. (1985, April 1). City trying to protect its other government securities.
  https://www.mcall.com/1985/04/01/city-trying-to-protect-its-other-government-securities (excerpt only; UNVERIFIED)
- S10. KWQC. (2017, June 27). *Illinois Lottery modifies its payment policy*.
  https://www.kwqc.com/content/news/Illinois-Lottery-modifies-its-payment-policy-431131843.html (read in full; it
  reproduces the Illinois Lottery's statement)
- S11. Rasche v. Lane, 150 F. Supp. 3d 934 (N.D. Ill. 2015). https://law.counselstack.com/opinion/rasche-v-lane-ilnd-2015
  (read in full)
- S12. Illinois Department of the Lottery. (2020). *Investments and prizes payable in installments: September 30, 2020*
  [Monthly investment note].
  https://www.illinoislottery.com/content/dam/il/pdfs/financial-pdfs/investments/2020/2020-9-30-Illinois-Lottery-Investments.pdf
  (read in full)
- S13. Minnesota State Lottery. (2025). *Minnesota State Lottery financial statements, fiscal years ended June 30, 2025
  and 2024* [Annual report].
  https://mnlottery-craft-assets-prod.s3.us-gov-west-1.amazonaws.com/Annual-Report/2025_Financial_Statement.pdf
  (debt administration section and note 10 read)
- S14. U.S. General Accounting Office. (1992, September 9). *Insurer failures: Regulators failed to respond in timely
  and forceful manner in four large life insurer failures* (GAO/T-GGD-92-43; testimony of R. L. Fogel).
  https://www.gao.gov/assets/t-ggd-92-43.pdf (read in full)
- S15. Pennsylvania Life and Health Insurance Guaranty Association v. Insurance Department, 625 A.2d 1286 (Pa. Commw.
  Ct. 1993). https://storage.courtlistener.com/harvard_pdf/6501284.pdf (read in full)
- S16. Matter of Executive Life Insurance Co. of New York, 2012 NY Slip Op 31174(U) (Sup. Ct. Nassau County Apr. 16,
  2012). https://law.justia.com/cases/new-york/other-courts/2012/2012-ny-slip-op-31174-u.html (read in full)
- S17. Matter of Executive Life Insurance Co. of New York, 103 A.D.3d 631 (2d Dep't 2013).
  https://www.nycourts.gov/REPORTER/3dseries/2013/2013_00738.htm (read in full)
- S18. The Life and Health Insurance Company Guaranty Corporation of New York. (n.d.). *Executive Life Insurance Company
  of New York*. Retrieved November 12, 2026, from https://www.nylifega.org/Custom/Index/718 (read in full)
- S19. AIRROC. (2012). The elephant in the courtroom. *AIRROC Matters*, Summer 2012.
  https://airroc.memberclicks.net/assets/CLIP/elephant%20in%20the%20courtroom.airroc_matters_summer_2012%202.pdf
  (excerpt only; UNVERIFIED)
- S20. Stone, E. S. (n.d.). *ELNY debacle*. Retrieved November 12, 2026, from https://edwardstonelaw.com/elny/elny-litigation
  (excerpt only; UNVERIFIED)
- S21. Certain personal injury liability assignments, 26 U.S.C. § 130. Legal Information Institute.
  https://www.law.cornell.edu/uscode/text/26/130 (read in full)
- S22. Board of Governors of the Federal Reserve System. (2026, July 8). *Holidays observed by the Federal Reserve
  System 2026-2030* (K.8). https://www.federalreserve.gov/aboutthefed/k8.htm (read in full)
- S23. Ennis, H. M., & Price, D. A. (2015). *Discount window lending: Policy trade-offs and the 1985 BoNY computer
  failure* (Economic Brief No. 15-05). Federal Reserve Bank of Richmond.
  https://www.richmondfed.org/-/media/richmondfedorg/publications/research/economic_brief/2015/pdf/eb_15-05.pdf
  (read in full)
- S24. Financial Planning. (2015, August 28). *BNY Mellon tech issues continue to dog funds*.
  https://www.financial-planning.com/news/bny-mellon-tech-issues-continue-to-dog-funds-mme257866 (read in full)
- S25. Reuters. (2015, August 26). *BNY Mellon pricing glitch affects billions of dollars of funds*.
  https://www.reuters.com/article/markets/wealth/bny-mellon-pricing-glitch-affects-billions-of-dollars-of-funds-idUSKCN0QV28C
  (excerpt only; UNVERIFIED)
- S26. Banking Dive. (2021, February 24; updated February 26). *Fed says 'operational error' caused payment system
  outage*. https://www.bankingdive.com/news/federal-reserve-operational-error-payment-system-outage/595678 (read in full)
- S27. The News-Gazette. (2017). *Illinois Lottery says state budget impasse cost it almost $4M in sales*.
  https://www.news-gazette.com/news/illinois-lottery-says-state-budget-impasse-cost-it-almost-4m-in-sales/article_214b77f2-5b91-5b1d-a215-511361e1ec6c.html
  (excerpt only; UNVERIFIED)
