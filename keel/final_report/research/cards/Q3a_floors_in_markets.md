# Q3a research cards: floors in markets, what made them real or false (portfolio insurance 1987, principal-protected notes 2008, target-date 2010 funds, iBond term funds)

**Date.** Fri 13 Nov 2026 (Sydney morning; Thu 12 Nov in the US). Web sources were read at the source that day
(Parallel web_fetch and web_search); "accessed 13 Nov 2026" below means that day. Report parts: 3b (the facility
contribution: what the floor is, named for what it is), 3c (the range: what each end rests on), 3e (assumptions and
limits: what an iBond fund pays; Table 3's fund-notices row), and Section 2 only for one naming clause if the lead
moves it there.

**Notes for the Final Report store, not report prose.** The IPS, the Trading Notes and the WInS book are frozen: a clash
is a risk to record, never a change. Every figure about Laura's plan is quoted from `../../NUMBERS.md` with its section
and is MODEL. Sums of register figures are marked "Keel arithmetic". Names follow `../../WORDS.md` ("the floor", "her
facility contribution", "the top-up", "her flexibility", "the range"). Caplet's design is never called portfolio
insurance, CPPI or guaranteed in this card except to say it is not one. This card does not re-card LDI 2022 or the
Reserve fund 2008 (card Q2a rows 1-7 and 19-22) or the iBond dates and payouts already in card Q16 (rows 1-10); it
cites them.

**Claims tested (each to keep, kill or change).**
1. "A floor is only as real as what pays it: a floor kept by trading (portfolio insurance, CPPI) or by an issuer's
   promise (a principal-protected note) failed exactly when it was needed, while a floor that is owned outright (a
   Treasury maturing on the date) did not."
2. "Target-date 2010 funds lost about a quarter in 2008 because their protection was a glide path, a weight, not an
   owned asset maturing on the date; Caplet's design differs in kind, not degree."
3. "Caplet's floor is not CPPI: no trading rule moves money between shares and Treasuries as markets move, and the one
   move (2031) is fixed in advance. But an iBond fund pays net asset value at term, not par, so it is a floor in
   Treasuries, not a guaranteed sum." Find exactly what the prospectus allows to reduce the payout, and how close
   past funds came to the yield they showed at purchase.

**Problem class and the field that solved it.** Protected-minimum design: how to promise a minimum and keep some
upside. Finance theory classified the answers in 1988 (Perold and Sharpe's family of constant-proportion, constant-mix
and option-based strategies, with buy-and-hold as its one static member); securities regulators settled the
"who pays" question for structured notes after Lehman (FINRA 2009, SEC and FINRA 2011); the SEC and the Department of
Labor took up the "a date is not a promise" question for target-date funds in 2009-10. The test that falls out of all
three: who pays, is it owned outright with no borrowing, can anything force a sale before the date, and does the date
match the need.

## Verdicts in one screen

- **Claim 1: CHANGE.** True for who pays (Lehman's notes: holders became "unsecured creditors and might recover
  little, if anything"). Too strong for portfolio insurance: the 1987 floors were kept by selling, and on 19 Oct the
  selling could not keep up ("far behind the hedge ratios", Brady; futures down 29% against the index's 20%, Leland
  and Rubinstein), but Rubinstein's own 1988 summary says most programs "did not violate their minimum returns"
  (abstract only, UNVERIFIED; Jacobs 1997 says the opposite, also UNVERIFIED). So "fell short of what buyers
  expected, at the moment the trading had to happen", not "failed". And "owned outright" is not enough alone: a
  floor owned but borrowed against (LDI 2022) or held in a fund that froze (Reserve 2008) also failed (card Q2a).
  The real test has four parts (row 33). Laura's floor passes all four, with one qualifier: it is a fund, so it pays
  what its bonds are worth, not a stated sum.
- **Claim 2: CHANGE.** The numbers: 2010 funds' 2008 losses "averaged nearly 24%", "between approximately 9% and 41%",
  against about 37% for the S&P 500 (SEC 2010); Schapiro's hearing figure was "almost 25 percent" across 31 funds,
  from 3.6% to 41%. Their equity at the target date ran from about 25% to 65%. "Differs in kind" holds for the
  promised money only: the ten payments are in Treasuries from January 2028 and both ends of the range are in
  Treasuries after the 2031 move. Her flexibility is a weight in shares on a date, the same kind of exposure as a
  glide path's (half kept $21,347 centrally, NUMBERS 4; median $12,208 in paths where VT ends below its 2028 cost,
  NUMBERS 8f). The sharper lesson is not the loss: 38% of surveyed workers believed target-date funds "offer a
  guaranteed return". People read a date as a promise. Laura states no figure before the move (NUMBERS 4).
- **Claim 3: KEEP the first half, CHANGE the second.** Not CPPI: in Perold and Sharpe's own definitions the plan is
  buy-and-hold, "constant-proportion strategies with a multiplier of one and a floor equal to the value invested in
  bills" (Keel check: in January 2028 the shares, $29,829, equal the money left after the floor, $111,718 minus
  $81,889; NUMBERS 4). Its gap risk is nil because the market must fall 100% before the floor is touched. The 2031
  move is a reset of the floor fixed by date in the IPS, which Perold and Sharpe say must be named as "an integral
  part" of any strategy. Second half: "a floor in Treasuries held through a fund that promises no sum". The
  prospectus allows the payout to be cut by the 0.07% fee, by costs outside the unitary fee with no stated cap
  (interest, taxes, trading costs, litigation and extraordinary expenses), by liquidation costs, by securities-lending
  losses, and to move with the final months' cash yield; the Board may also set a later end date. The range rule's
  0.5% cut carries these up to 0.5% of value (NUMBERS 3, 4). Five Treasury iBond funds have ended on schedule, not
  three (IBTA 2021 and IBTB 2022 as well); the one with a primary figure, IBTF, paid within about 0.01 points a year
  of its launch yield (card Q16 row 8).

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Perold and Sharpe's definitions: constant-proportion strategies set "Dollars in Stocks = m (Assets - Floor)"; CPPI is the case m > 1; "Buy-and-hold strategies are constant-proportion strategies with a multiplier of one and a floor equal to the value invested in bills"; for buy-and-hold, "Portfolio value will never fall below the value of the initial investment in bills" | Perold & Sharpe (1988/1995) | FLOOR, CEILING, PRESENTATION | TEXTBOOK | The plan's name, from the paper that defined CPPI: buy-and-hold. In January 2028 the shares ($29,829) equal what is left after the floor ($111,718 less $81,889; NUMBERS 4), so the multiplier is exactly one (Keel arithmetic on register figures) | Store rows H3-037 and H7-026 call the plan "CPPI with multiplier 1" or "the m = 1 member of the CPPI family": wrong label, since CPPI means m > 1 in the source; H7-026 also carries void figures ($32,133; $117,867; NUMBERS 6) | VERIFIED (paper read in full, 1995 reprint PDF) | no (the IPS names no strategy family) | Stanford course copy of the FAJ reprint |
| 2 | Gap risk is set by the multiplier: "the market can fall by as much as 1/m with no rebalancing before the floor is endangered" | Perold & Sharpe (1988/1995) | FLOOR, CERTAINTY | TEXTBOOK | At m = 1 the market must fall 100%: VT at zero leaves the floor's $103,178 untouched (NUMBERS 4, deletion test). Keel arithmetic, about no real program: at m = 4 a 25% gap reaches the floor, at m = 5 a 20% gap; on 19 Oct 1987 the index fell 20% and futures 29% (row 9) | Laura's money is still not capital-protected: $103,178 back on $111,718 if shares go to zero (NUMBERS 4); the floor protects the bottom of the range, not the deposit | VERIFIED (read in full) | no | As row 1 |
| 3 | Only static strategies can be held by everyone at once: "only buy-and-hold strategies could be followed by everyone"; dynamic floors need someone on the other side of each trade | Perold & Sharpe (1988/1995) | FLOOR, OTHER | KNOWN | Laura's floor never needs a buyer in a fall; nothing in the plan sells because prices dropped | A market-wide argument; Laura's $450,000 moves no market either way | VERIFIED (read in full) | no | As row 1 |
| 4 | Raising a floor during the life of a strategy "can cause stocks to be sold in both up and down markets", so "Resetting rules should thus be considered an integral part of the dynamic strategy" | Perold & Sharpe (1988/1995) | MOVE2031, FLOOR, CEILING | KNOWN | The 2031 move is a reset written into the IPS before trading (l.15: "the other half will move into Treasuries"): one date, half the shares, whatever the market did. Named in advance, as the paper asks | It sells half after a fall too, fixing a lower top; good and bad markets before the move change only the top (NUMBERS 4). A cost of the frozen design, not a defect to fix | VERIFIED (read in full) | no (IPS l.15 sets the move) | As row 1 |
| 5 | Portfolio insurance sold into falls by design: "the typical portfolio insurance model calls for stock sales in excess of 20 percent of a portfolio in response to a 10 percent decline in the market"; $60 to $90 billion was under it, and those assets "increased more than fourfold during 1987" | Presidential Task Force (1988) | FLOOR, CERTAINTY | KNOWN | The contrast in one fact: the plan sells nothing in a fall; its only sale of shares is the dated 2031 move | Brady's figure is a "typical model", not a measured average across programs | VERIFIED (passages read in the report's full text; whole report not read) | no | archive.org full text; Yale YPFS PDF |
| 6 | On 19 Oct 1987 three portfolio insurers' NYSE sell programs were "just under $2 billion" of just under $21 billion; in futures their sales were "the equivalent of $4 billion of stocks, or 34,500 contracts, equal to over 40 percent of futures volume, exclusive of locals"; the Dow fell 508 points, almost 23% | Presidential Task Force (1988) | FLOOR | KNOWN | Scale only; store | Brady is one of several official accounts and blames insurers more than the SEC staff or Leland and Rubinstein do (rows 9-10) | VERIFIED (passages read) | no | As row 5 |
| 7 | The floor depended on trading that could not happen: insurers "remained far behind the hedge ratios dictated by their computer programs"; they believed "the futures market offered a separate haven of liquidity ... In October, this belief proved to be unrealistic" | Presidential Task Force (1988), Study III and p. 55 | FLOOR, CERTAINTY | KNOWN | The clearest statement of "a floor kept by trading": it is real only if the trade can be done at the price assumed, on the day it is needed. Laura's floor needs no trade after January 2028 | The shortfall was against the models' targets; whether clients' minimums were broken is disputed (row 11) | VERIFIED (passages read) | no | As row 5 |
| 8 | A floor bought more risk: pension funds adopting portfolio insurance "typically increased the funds' risk exposure by investing more heavily in common stock" | Presidential Task Force (1988), p. 9 and Study V | FLOOR, CEILING | NICHE | The reverse holds for Laura: the shares are only what is left once the ten and the floor are owned (SKELETON 2.3), about 7% of the $450,000 (6.63%, NUMBERS 6) | One sentence of Brady's; Study V's averages were read in passages only | VERIFIED (passages read) | no | As row 5 |
| 9 | The inventors' account: $60 to $80 billion was insured, about 2% of $3.6 trillion of US equity; insurance trades on 19 Oct were "only $6 billion out of a total of $42 billion"; futures closed down 29%, the index 20%; futures "gapped open down 6.5 percent"; insurers carried "an overhang of unfilled sell orders going into Monday" | Leland & Rubinstein (1988) | FLOOR, CERTAINTY | KNOWN | The gap that a trading floor cannot cross: a 6.5% opening gap and a 29% futures fall in a day | The authors disclose that they consult to their own portfolio insurance firm, and they favour a market-panic cause | VERIFIED (paper read in full) | no | AEA PDF |
| 10 | The SEC staff found at least about $55 billion under portfolio insurance, "no single factor ... was responsible" for the break, and insurance selling was significant on 19-20 Oct (on 20 Oct about 28,000 contracts, 25.5% of S&P futures volume) | SEC Division of Market Regulation (1988) | FLOOR | KNOWN | Store only: official accounts differ on cause and agree on scale | CFTC staff found no evidence for the cascade theory (as reported in the SEC report) | VERIFIED (passages read in the report's first part) | no | sechistorical.org PDF |
| 11 | Did the 1987 floors break? Rubinstein: "most portfolio insurance programs did not violate their minimum returns, many did not perform as well as expected"; "Conservative programs (say, 50 per cent hedged) probably outperformed". Jacobs (1997): "substantial violations of their floors" | Rubinstein (1988); Jacobs (1997) | FLOOR, CERTAINTY | NICHE | Claim 1 must not say portfolio insurance "failed" outright; say it fell short of what buyers expected, when it had to trade | Both sources seen only as an abstract (Rubinstein) and a 1997 Pensions & Investments reprint of two chapters (Jacobs) | UNVERIFIED | no | CFA Institute abstract page; jlem.com excerpt |
| 12 | Theory since 1992: CPPI "is equivalent to investing in perpetual American call options" absent costs; with jumps, its downside risk "is nonnegligible and grows with the multiplier value"; banks sold "gap risk" cover on CPPI notes | Black & Perold (1992); Cont & Tankov (2009); Jessen (2014) | FLOOR | NICHE | Store only: confirms row 2 in modern form | Abstracts only | UNVERIFIED | no | ScienceDirect, Wiley and PM Research abstract pages |
| 13 | The other way a traded floor disappoints: protected mutual funds of 2002-03 could move almost wholly into bonds after a fall; some held "just 1 percent to 2 percent of assets in stocks", with fees of 1.75% to 3% a year and an insurer standing behind the minimum | Ambrose (2003), Daily Press, reporting an NASD investor alert | FLOOR, CEILING | NICHE | The plan never locks out of shares after a fall: her flexibility stays in VT whatever happens before 2033 | Newspaper report; the NASD alert itself ("Principal-Protected Funds: Security Has a Price") was not found at the source | UNVERIFIED | no | Parallel web_search |
| 14 | A principal-protected note is a zero-coupon bond plus an option; "Most importantly, the principal guarantee is subject to the credit-worthiness of the guarantor"; some guarantee "as little as 10 percent"; the guarantee "only applies to notes that are held to maturity"; it "generally relates to nominal principal and does not offer inflation protection" | FINRA (2009) | FLOOR, INFLATION_TWD, CERTAINTY | KNOWN | Who pays Laura's floor: the US Treasury, through bonds the fund owns; no bank's promise sits between her and them. Same as the note on one point: her floor is nominal too (payments fixed in US dollars; NUMBERS 8d) | Laura's fund promises no sum at all (row 25), so there is no guarantor whose credit could fail; the fund is a container, not a promiser | VERIFIED (notice read in full) | no | finra.org |
| 15 | After Lehman: holders of its protected notes "are considered unsecured creditors and might recover little, if anything, of their original investment"; "any guarantee is only as good as the financial strength of the company making that promise" | SEC OIEA & FINRA (2011) | FLOOR, CERTAINTY | KNOWN | The plan's one exception is the same idea at the top of the credit scale: IPS l.11's "barring a US default" | FINRA's 2023 page repeats it: "any principal guarantee is subject to the creditworthiness of the guarantor" | VERIFIED (alert read in full; FINRA 2023 page read) | no | investor.gov; sec.gov copy; finra.org |
| 16 | The name misled: FINRA fined UBS $2.5m and ordered $8.25m restitution (Apr 2011) for selling Lehman "100% Principal-Protection Notes" in Mar-Jun 2008 without stressing they were unsecured, including to "moderate" and "conservative" clients; New Hampshire's consent order: the notes were "senior unsecured debt of the issuer such that if the issuer defaults there will be no protection" | Stempel (2011), Reuters via Fox Business; Skinner (2011), InvestmentNews; New Hampshire Bureau of Securities Regulation (2011) | FLOOR, PRESENTATION, COSPONSOR | KNOWN | Why WORDS bans "guaranteed": the word did the damage, not the arithmetic. TNA l.7's "near-ironclad guarantee" (CANON C13) is never repeated | FINRA's own release returned 404 at its old address; the fine is from press reports | VERIFIED for the New Hampshire order (passages read); UNVERIFIED for FINRA's release (secondary only) | risk: TNA l.7 "near-ironclad guarantee" (CANON C13), already recorded | sos.nh.gov PDF; press pages |
| 17 | Wrong-way risk: the issuer's promise failed in the same crisis that sank the index it protected against (Lehman filed 15 Sep 2008) | Keel reasoning on rows 14-16 | FLOOR, CERTAINTY, TWOREASONS | KNOWN | A floor is worth most when it is least likely to fail in a crash. Treasuries tended to rise in crashes; the plan's one shared exception is a US default, which is also one of its two reasons to change plan (SKELETON Exhibits item 4) | Not a sourced finding; a reading of dates | UNVERIFIED (reasoning, not a source) | no | This card |
| 18 | Store rows H2-068 and H3-092 frame the 2028 money as a "capital-protected" or "principal-protected note" built without a bank. The register says the opposite: "Not capital-protected" (VT $29,829 is more than the floor's expected interest $21,289; $103,178 back on $111,718 if shares go to zero) | NUMBERS 4; store rows H2-068, H3-092 | FLOOR, CEILING, PRESENTATION | NICHE | Keep "the bank taken out" (who pays); drop "protected" (what is protected is the bottom of the range, not the deposit) | The store rows predate the escrow standard of Tue 10 Nov | VERIFIED (register and store read) | clash: H2-068 and H3-092 against NUMBERS 4 (store, not frozen texts) | `../store/by_tag/FLOOR.md` |
| 19 | Target-date 2010 funds in 2008: "the average loss in 2008 among 31 funds with a 2010 target date was almost 25 percent"; returns ranged "from minus 3.6 percent to minus 41 percent" | Schapiro, in SEC & DOL (2009) | FLOOR, CEILING | KNOWN | A date is not a floor: none of these funds owned anything that paid a sum on its date | "It has been reported": Schapiro quotes others' figures | VERIFIED (passages of the hearing transcript read) | no | sec.gov transcript PDF |
| 20 | The SEC's later count: 2010 funds' losses "averaged nearly 24% in 2008, ranging between approximately 9% and 41%", against about 37% for the S&P 500; equity at the target date ran from about 25% to 65% | SEC (2010), Release 33-9126 | FLOOR, CEILING | KNOWN | The spread came from a design choice (how much equity at the date), not from the market | The two official figures differ at the low end (3.6% or 9%); cite one with its source, never both | VERIFIED (passages of the release read) | no | sec.gov PDF |
| 21 | People read the date as a promise: "over 60 percent of employees say that investing in a Target Date Fund means that they will be able to retire on the target date. 38 percent believe that Target Date Funds offer a guaranteed return" | Testimony in SEC & DOL (2009) | COSPONSOR, FUNDRAISING, PRESENTATION | NICHE | Co-sponsors could read a range stated before the move as a promise; the rule states no figure before the move (NUMBERS 4), and the co-sponsor words should keep it so | A survey quoted by one witness; its sample was not read | VERIFIED (passage of the transcript read) | no | As row 19 |
| 22 | The losses were a choice: one witness's "2010 index lost less than 5 percent in 2008 because it stuck to its core objective while the average 2010 fund lost 23 percent"; another: "Many 2010 lifecycle funds, including ours, fell by 25 to 30 percent" | Testimony in SEC & DOL (2009) | FLOOR, CEILING | NICHE | Store only | Witnesses selling their own products | VERIFIED (passages of the transcript read) | no | As row 19 |
| 23 | The regulator's remedy was disclosure: show the asset mix at the target date beside the fund's name | SEC (2010), Release 33-9126 | PRESENTATION | KNOWN | A Section 2 or 3b idea: say for 1 Jan 2033 what part of Laura's money is in shares (none of the promised money; her flexibility only) | A proposal; whether it was adopted was not checked | VERIFIED (proposal passages read); adoption UNVERIFIED | no | As row 20 |
| 24 | Laura's glide-path-like part, sized: her flexibility is half the shares, $21,347 centrally (NUMBERS 4); median $12,208 in the paths where VT ends below its 2028 cost (NUMBERS 8f). Keel arithmetic: $21,347 is 14.7% of the 2028 money in late 2032 ($123,476 paid by the two funds plus $21,347) | NUMBERS 4, 8f | HALFKEPT, CEILING, FLOOR | NICHE | Where claim 2's "differs in kind" stops: promised money holds no shares; her flexibility does, on purpose (IPS l.15: "promised to no one") | Shares left at 2033 are a choice the IPS made; the target-date comparison is about promised money only | VERIFIED (register read) | no | NUMBERS |
| 25 | The fund promises no sum: it "does not seek to return any predetermined amount at maturity or in periodic distributions"; fund pages: "An investment in the Fund(s) is not guaranteed, and an investor may experience losses, including near or at the termination date"; "liquidation proceeds are not predictable at the time of investment" | iShares Trust (2026a, 2026c); BlackRock fund pages | FLOOR, LADDER, CERTAINTY | KNOWN | The floor is "a floor in Treasuries": what its bonds are worth when it ends (WORDS). Because it promises nothing, no promise can fail; what is left is what the bonds pay and what the fund costs | IPS l.13's "pay what they say" (CANON C2) is the plain version; TNA l.15's "a net asset value, as opposed to a promise of par" is the precise one (CANON B23, D5) | VERIFIED (prospectus passages and IBTM summary prospectus read; Q16 S1) | risk: IPS l.13 (CANON C2, D5), already recorded | ishares.com prospectus; card Q16 row 1 |
| 26 | What the prospectus lets reduce the payout, list 1 (costs): the 0.07% fee; the unitary fee excludes "management fees, interest expenses, taxes, acquisition and disposition costs including brokerage, distribution fees, litigation and extraordinary expenses" (no cap stated); the final NAV "will include any costs associated with the liquidation"; money-market fund fees, waived by contract through termination for BlackRock's own funds | iShares Trust (2026a); card Q16 row 7 (Form 497 notices) | FLOOR, CERTAINTY, RESERVE2033 | NICHE | The range rule's 0.5% cut carries these up to 0.5% of value; at 0.75% an end breaks in about 1 house path in 17 (NUMBERS 4). This is the wording NUMBERS 3 asked for ("read its wording before quoting it") | The unitary-fee passage was read cut off after "and any"; the full exclusion list should be re-read before quoting | VERIFIED (prospectus passages read) | risk: IPS l.15 "without doubt" and "the bottom will remain constant" (CANON C5, C6): true on the holdings with 0.5% to spare, not against an uncapped cost | ishares.com prospectus |
| 27 | List 2 (risks): securities lending, where a borrower fails to return the bonds or the cash collateral's investments lose value; the lending agent is a BlackRock affiliate | iShares Trust (2026a) | FLOOR, CERTAINTY | NICHE | The only counterparty inside the floor. Name it once with the costs (SKELETON 3c already says "the prospectus allows lending losses, extraordinary and liquidation costs with no cap"; card Q26 row T21) | Size never disclosed in what was read; no loss case found | VERIFIED (prospectus passages read) | risk: as row 26 | As row 26 |
| 28 | List 3 (yield): "In the months leading up to the Fund's planned termination date, the Fund's yield may move toward prevailing money market rates" | iShares Trust (2026a); card Q16 row 5 | REINVEST, FLOOR, RESERVE2033 | KNOWN | Already in the rule: the floor's zero-interest payout is 3.83% below its modelled payout, the moved half's 2.38% (NUMBERS 3) | Cuts both ways (Q16 row 10: IBTE's final cash earned 4% to 5%) | VERIFIED (prospectus passages read) | no | As row 26 |
| 29 | List 4 (timing): "The Board may extend the termination date if a majority of the Board determines the extension to be in the best interest of the Fund"; no shareholder vote is needed | iShares Trust (2026a); card Q16 row 4 | FLOOR, TWOREASONS, RESERVE2033 | NICHE | A delay, not a cut: watch the October notice before December 2032 (Table 3's fund-notices row) | No extension in five Treasury terminations (row 30) | VERIFIED (prospectus passage read) | no (neither of the two reasons; a watch item) | As row 26 |
| 30 | Five Treasury iBond funds have ended, not three: nine were listed on 25 Feb 2020 (IBTA Dec 2021 to IBTJ); IBTB's last trading and final NAV were 15 Dec 2022, liquidation 21 Dec 2022; IBTA is "no longer active" from Dec 2021; IBTD, IBTE and IBTF ended Dec 2023-2025 (Q16 row 6) | Nasdaq (2020); BlackRock (2022); ETF Database (n.d.); card Q16 row 6 | LADDER, FLOOR, RESERVE2033 | NICHE | Five on-schedule endings, each paying cash in mid-December (IBTB: 11 days before 1 January, Keel arithmetic) | IBTA's end date is from a secondary data site; its liquidation notice was not read | VERIFIED for IBTB (release read in full, republished copy) and the 2020 listing (circular); UNVERIFIED for IBTA's date | clash: NUMBERS 8h and card Q16 rows 4 and 6 say "three" | businessinsurance.com copy of the Business Wire release; nasdaqtrader.com |
| 31 | How close ended funds came to their launch yield: IBTF 1.15% a year since launch to 30 Jun 2025 against a 5-year Treasury yield of 1.16% on launch day (Q16 row 8); IBTE 1.32% against 1.16% (Q16 row 10, secondary); IBTD about 0.85% over three years to Dec 2023 (secondary); no figure found for IBTA or IBTB | Card Q16 rows 8 and 10; etfdb and Yahoo pages for IBTD | FLOOR, LADDER, CERTAINTY | NICHE | Evidence, not promise: held to the end, the one primary case paid within about 0.01 points a year of the yield it showed at purchase, after two years of price falls (2021-22) | One primary case; since-launch returns assume distributions reinvested and stop six months early | VERIFIED for IBTF (via Q16's primary read); UNVERIFIED for IBTD and IBTE | no | Card Q16; secondary data pages |
| 32 | The price paid can differ from what the fund holds: "Shares of ETFs trade at market price, which may be greater or less than net asset value" | BlackRock (2022) | FLOOR, COMPLETE2028 | KNOWN | Already in the 0.5% cut's list ("an ETF bought above its net asset value, bid-ask spreads", NUMBERS 0) | Applies on the January 2028 and 2031 trade days only | VERIFIED (release read) | no | As row 30 |
| 33 | The four-part test for any floor: (1) who pays; (2) owned outright, with no borrowing; (3) nothing can force a sale before the date; (4) the date matches the need. Portfolio insurance failed (3); Lehman's notes (1); target-date funds had no floor and no date match (4); LDI 2022 (2); the Reserve fund 2008 delayed cash through its wrapper (card Q2a). Laura's floor: US Treasury; no borrowing (WInS bans margin); no rule forces a sale; ends 15 Dec 2032 for a December 2032 contribution | Rows 1-29; card Q2a | FLOOR, CERTAINTY, PRESENTATION | NICHE | The answer to "is this portfolio insurance under another name?" in four checks; Exhibit material at most, a clause in prose | The fund wrapper is the one soft spot: it pays net asset value, its costs are not capped, and its Board can delay the end (rows 25-29) | VERIFIED (synthesis of read sources) | no | This card |
| 34 | The naming, in notes: a floor bought once in Treasuries, shares that are only the remainder, and one dated move; no rule trades on prices. Perold and Sharpe's word is buy-and-hold. Never portfolio insurance, CPPI, "protected" or "guaranteed" | Rows 1-4; WORDS | FLOOR, MOVE2031, PRESENTATION | NICHE | EXPECTATIONS 2.2 asks for exactly this: name the idea for what it is, with the source that defined the family | "Buy-and-hold" undersells the dated 2031 move; say both | VERIFIED (paper read) | no | This card |

## (b) Cards

### Card 1. Perold and Sharpe's family: the plan is the buy-and-hold member, not CPPI (rows 1-4, 34)
- **What is it?** Perold and Sharpe (1988/1995) sorted dynamic strategies into buy-and-hold, constant-mix, constant-proportion
  (CPPI) and option-based. Constant-proportion means shares = m times (assets less floor). CPPI is m above one. With
  m equal to one and the floor equal to the bills bought, the rule never trades: that is buy-and-hold, and its value
  "will never fall below the value of the initial investment in bills". Gap risk scales as 1/m. Raising the floor
  midway "can cause stocks to be sold in both up and down markets", so resets belong in the strategy's definition.
- **Did it work?** As theory, yes: the paper is the standard reference (store H7-026 cites it). Its predictions match
  1987: high-multiplier rules sold into the fall; static holders did not have to.
- **How is Laura's case like it?** January 2028: $111,718 left after the top-up; $81,889 buys the floor (which pays
  $103,178 in late 2032); $29,829 buys VT (NUMBERS 4). Shares equal the cushion, so m = 1 exactly. The floor is the
  bonds' payout; VT at zero leaves it whole. The 2031 move is a reset fixed in the IPS.
- **How is it not?** The paper's floor is in bills; Laura's is in a Treasury fund that pays net asset value (Card 5).
  Her 2031 reset sells half whatever happened, not by a rule on prices, and only once.
- **What Caplet takes.** One clause, in 3b where the contribution is built (or 3c beside the range rule): a floor
  bought once in Treasuries, shares that are only the remainder, one dated move; what Perold and Sharpe (1988/1995) call
  buy-and-hold, not a strategy that trades on prices. No number needed; if one, "shares can fall to nothing and the
  bottom is untouched" ($103,178, NUMBERS 4). Store: fix H3-037 and H7-026's label.

### Card 2. Portfolio insurance, October 1987: a floor kept by selling (rows 5-11)
- **What is it?** Programs that kept a minimum by selling shares (or index futures) as prices fell: over 20% of the
  portfolio sold on a 10% fall in a typical model (Brady). $55 billion (SEC) to $60-90 billion (Brady) was insured.
- **Did it work?** Partly. On 19 Oct the index fell 20%, futures 29%, with a 6.5% opening gap (Leland and Rubinstein).
  Insurers "remained far behind the hedge ratios dictated by their computer programs" (Brady). Whether minimums were
  broken is disputed (Rubinstein's abstract: mostly not; Jacobs: substantially; both UNVERIFIED). The method largely
  ended after 1987. Cause is disputed too: the SEC staff found "no single factor".
- **How is Laura's case like it?** Both state a minimum and keep upside in shares.
- **How is it not?** Laura's minimum is bought, not kept by trading; no trade is needed after January 2028 to hold it;
  no rule sells because prices fell; no futures.
- **What Caplet takes.** Store only. At most four words inside Card 1's clause ("no rule sells into a fall"). Never
  tell the 1987 story in the report; never use it for drama.

### Card 3. Principal-protected notes and Lehman, 2008: a floor that was someone's promise (rows 14-18)
- **What is it?** A bank's note: a zero-coupon bond plus an option, with the minimum "subject to the
  credit-worthiness of the guarantor" (FINRA 2009). Lehman's "100% Principal-Protection Notes" were "senior unsecured
  debt of the issuer such that if the issuer defaults there will be no protection" (New Hampshire 2011).
- **Did it work?** No, for Lehman's holders: "unsecured creditors [who] might recover little, if anything" (SEC and
  FINRA 2011). UBS was fined $2.5m with $8.25m restitution for how it sold them (press reports of FINRA's action).
- **How is Laura's case like it?** Same shape: a bond floor plus shares, with the floor sized to come back.
- **How is it not?** No middleman's promise: the fund owns Treasuries and promises nothing itself. And unlike a note,
  Laura's 2028 money is not capital-protected (NUMBERS 4: $103,178 back on $111,718), so the store's "principal-
  protected note without the bank" (H2-068, H3-092) should drop "protected".
- **What Caplet takes.** Store only, plus WORDS' ban on "guaranteed", which this case explains. The co-sponsor words
  (3d) say what pays each end, never "protected". TNA l.7's "near-ironclad guarantee" stays unrepeated (CANON C13).

### Card 4. Target-date 2010 funds in 2008: a date is not a floor (rows 19-24)
- **What is it?** Funds named for a retirement year that lower their share weight along a glide path. In 2008 the
  2010 funds lost "nearly 24%" on average, "between approximately 9% and 41%", with 25% to 65% in equity at the date
  (SEC 2010); Schapiro cited "almost 25 percent" across 31 funds, 3.6% to 41% (2009 hearing).
- **Did it work?** Not as people read it: 38% of surveyed workers thought the funds "offer a guaranteed return". The
  SEC's answer was disclosure of the mix at the date beside the name (proposed 2010; adoption not checked).
- **How is Laura's case like it?** Her flexibility is a share weight held to a date: about $21,300 centrally, about
  $12,200 in a bad path's median (NUMBERS 4, 8f). The 2031 move resembles a glide-path step.
- **How is it not?** Promised money holds no shares: the ten from January 2028, and both ends of the range after the
  move, are in Treasuries ending before they are needed. The move buys a dated Treasury fund; a glide path only lowers
  a weight.
- **What Caplet takes.** The lesson about words, not losses: no figure stated before the move (3c, already planned).
  Possibly one clause in Section 2 or 3b, after the SEC's remedy: what part of Laura's money is in shares on 1 Jan 2033
  (none of the promised money). Otherwise store only.

### Card 5. iBond funds at their end: what the prospectus allows and what five ended funds paid (rows 25-32)
- **What is it?** A term fund that "does not seek to return any predetermined amount" and liquidates at net asset
  value about 15 December of its year. The prospectus lets the payout fall by the 0.07% fee, costs outside the
  unitary fee (no cap stated), liquidation costs and securities-lending losses; lets it drift with money-market yields
  in the last months; and lets the Board set a later end.
- **Did it work?** Five Treasury funds have ended on schedule (IBTA 2021, IBTB 2022, IBTD 2023, IBTE 2024, IBTF 2025).
  IBTF, the one with a primary figure, returned 1.15% a year since launch against a launch-day 5-year yield of 1.16%
  (card Q16 row 8). No extension, no reported lending loss.
- **How is Laura's case like it?** The floor (IBTM, ending 15 Dec 2032) and five of the ten rungs are such funds.
- **How is it not?** Laura's contribution is fixed by a rule that already strips interest after the trade day and
  cuts 0.5% (NUMBERS 3: floor 4.312% under its modelled payout, moved half 2.870%), so past funds' near-match to their
  yield is a margin, not the basis.
- **What Caplet takes.** 3e, one clause (already in SKELETON 3e and 3c): the funds pay what their bonds are worth, not
  a fixed sum; their running costs, closing costs and lending losses are not capped, and the 0.5% cut covers them up to
  0.5% of value. Table 3's fund-notices row: "five Treasury iBond funds have ended on schedule since 2021" as the
  row's evidence note. Correct NUMBERS 8h and card Q16 from three to five.

## (c) Verdicts

**Claim 1: CHANGE.**
- What holds: an issuer's promise failed when it was needed (Lehman, Sep 2008), in the same crisis that hit the index
  the notes protected against (rows 14-17).
- What does not: "failed exactly when it was needed" overstates portfolio insurance. Verified: insurers fell "far
  behind" their own hedge ratios and the futures market was not the "separate haven of liquidity" they assumed
  (Brady). Unverified and disputed: whether clients' minimums were broken (Rubinstein's abstract says mostly not).
  Say: the floor depended on selling at prices that did not exist on the day.
- Missing from the claim: owning is necessary, not sufficient. LDI 2022 owned its gilts but borrowed against them;
  the Reserve fund owned its assets but froze the payout (card Q2a). And Laura's floor is not "a Treasury maturing
  on the date" but a fund of Treasuries ending on 15 Dec 2032 (CANON C7, C8).
- Restated, in notes: a floor is real when the US Treasury pays, the bonds are owned with no borrowing, nothing can
  force a sale before the date, and the date matches the need (row 33). Laura's passes all four; the fund wrapper
  adds a small, named cost (Card 5).
- Where it lands: the four-part test is store or an exhibit's note; in prose at most Card 1's clause.

**Claim 2: CHANGE.**
- The number: "about a quarter" is right for the average (nearly 24% to almost 25%), but say the spread (about 9%
  to 41%, or 3.6% to 41% by Schapiro's count) and the S&P 500's 37% beside it. One source only in any use.
- The cause: a weight, yes; 25% to 65% equity at the date (SEC 2010).
- "Differs in kind, not degree": holds for the promised money. For her flexibility it is the same kind, by design
  (IPS l.15), and sized (row 24). Say "for the promised money".
- The lesson that matters for 3c and 3d: people read the date as a promise (row 21). Laura states nothing before the
  move.
- Where it lands: store; possibly one clause on the mix at 1 Jan 2033 (Card 4).

**Claim 3: KEEP the first half, CHANGE the second.**
- Not CPPI: confirmed in the defining paper's own terms. m = 1, floor = the Treasuries bought, which Perold and Sharpe
  call buy-and-hold (row 1). The 2031 move is a reset fixed by date before trading, the kind the paper says to name as
  part of the strategy (row 4). Store rows H3-037 and H7-026 use the wrong label.
- "A floor in Treasuries, not a guaranteed sum": keep the idea, drop "guaranteed" even in negation in the report
  (WORDS bans it). Change to "a floor in Treasuries held through a fund that promises no sum", with the list of what
  can cut it (rows 26-29) and the evidence of five ended funds (rows 30-31).
- The prospectus list answers NUMBERS 3's open note ("That this applies to IBTM's prospectus is UNVERIFIED"): the
  summary prospectus and the 2026 prospectus allow these costs, with no cap stated; the rule's 0.5% cut is what
  carries them (NUMBERS 4: covered up to 0.5% of value; at 0.75%, about 1 house path in 17 breaks an end).
- Where it lands: one clause in 3e (planned); one clause naming the family in 3b or 3c (lead's choice).

## (d) Gaps

- **Black and Perold (1992)** read as abstract only; **Rubinstein (1988)** as abstract only; **Jacobs (1997)** as a
  Pensions & Investments reprint of two chapters of his later book (1999). The dispute over whether 1987 floors broke (row 11) is therefore open.
- **The Brady report and the SEC staff report** were read in passages of their full texts, not whole. Page numbers
  for Brady quotes (p. 9, p. 55, Studies III and V) come from those passages; re-check before any citation in APA.
- **FINRA's April 2011 release on UBS** returned 404 at its old address; the fine and restitution figures are from
  Reuters (via Fox Business), InvestmentNews and American Banker. The New Hampshire order was read in part.
- **The NASD alert "Principal-Protected Funds: Security Has a Price"** (linked from the 2011 alert) was not found at
  the source; row 13 rests on a 2003 newspaper report.
- **Target-date rule status.** Whether the SEC adopted the 2010 proposal was not checked. The two official loss
  figures differ (row 20); the reason (sample, date, share class) was not found.
- **The unitary-fee exclusions** were read cut off after "and any"; re-read the full sentence before quoting.
  Whether the fund's investment objective can change without a shareholder vote was searched for and not found.
- **IBTA's end** (Dec 2021) comes from a data site; its October 2021 notice or Form 497 was not read. Final NAVs and
  since-launch returns for IBTA, IBTB and IBTD were not found at a primary source; IBTE's is secondary (Q16 row 10).
- **UK Keydata and Arch Cru** were not researched; both were fund or product failures with different causes (fraud,
  a suspended fund) and add little beyond rows 14-16 and card Q2a's Reserve fund.
- **REFERENCES_APA.md** has no entry yet for any source below except the IBTM summary prospectus (row 78), which is
  used as listed. Rows 102 (Perold 1988, implementation shortfall) and 281 (Dybvig 1999) are different papers.
- **Corrections owed elsewhere (not made here; this card edits no other file):** NUMBERS 8h "Three iBonds Treasury
  funds have already ended" should read five; card Q16 rows 4 and 6 likewise; store rows H3-037 and H7-026 ("CPPI
  with multiplier 1"; H7-026's $32,133 and $117,867 are void) and H2-068 and H3-092 ("capital-protected note")
  against NUMBERS 4.
- **Articulation lead, not checked:** store row H9-083 ("CPPI refused ... buy-and-hold chosen") cites "Ideas tab §1".
  If that tab is Caplet's own record, the refusal is a real team event for 3f; who wrote it and when was not checked.

## Sources (APA 7; all accessed 13 Nov 2026)

Read at the source (in full unless marked):
- BlackRock. (2022, October 14). *iShares 2022 term maturity iBonds ETFs near final distribution dates* [Press
  release]. Business Wire. https://index.businessinsurance.com/observerreporter/article/bizwire-2022-10-14-ishares-2022-term-maturity-ibonds-etfs-near-final-distribution-dates
  (republished copy)
- Financial Industry Regulatory Authority. (2009, December 17). *FINRA reminds firms of their sales practice
  obligations relating to principal-protected notes* (Regulatory Notice 09-73).
  https://www.finra.org/rules-guidance/notices/09-73
- Financial Industry Regulatory Authority. (2023, April 12). *Understanding structured notes with principal
  protection*. https://www.finra.org/investors/insights/structured-notes-principal-protection
- iShares Trust. (2026a, February 27). *Prospectus*. BlackRock. https://www.ishares.com/us/literature/prospectus/p-ishares-trust-us-treasury-ibonds-non-ibonds-10-31.pdf
  (passages read)
- iShares Trust. (2026c, February 27). *Summary prospectus: iShares iBonds Dec 2032 Term Treasury ETF*
  (IS-SP-IBTM-0226). BlackRock. https://www.blackrock.com/us/individual/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf
  (REFERENCES_APA row 78)
- iShares Trust. (2020, February 18). *Summary prospectus: iShares iBonds Dec 2021 Term Treasury ETF* (IS-SP-IBTA-0220).
  U.S. Securities and Exchange Commission. https://www.sec.gov/Archives/edgar/data/1100663/000119312520053049/d897028d497k.htm
  (passages read)
- Leland, H., & Rubinstein, M. (1988). Comments on the market crash: Six months after. *Journal of Economic
  Perspectives, 2*(3), 45–50. https://doi.org/10.1257/jep.2.3.45
- Nasdaq. (2020, February 27). *Information circular: iShares iBonds Dec 2021 Term Treasury ETF; iShares iBonds Dec 2022
  Term Treasury ETF; iShares iBonds Dec 2023 Term Treasury ETF; iShares iBonds Dec 2024 Term Treasury ETF; iShares iBonds
  Dec 2025 Term Treasury ETF; iShares iBonds Dec 2026 Term Treasury ETF; iShares iBonds Dec 2027 Term Treasury ETF;
  iShares iBonds Dec 2028 Term Treasury ETF; iShares iBonds Dec 2029 Term Treasury ETF*.
  https://www.nasdaqtrader.com/content/newsalerts/2020/infocircular/iSharesTrustFeb2020.pdf (passages read)
- New Hampshire Bureau of Securities Regulation. (2011, August 22). *In the matter of UBS Financial Services Inc.:
  Consent order*. https://www.sos.nh.gov/sites/g/files/ehbemt561/files/inline-documents/sonh/8-22-11-ubs-financial-services-inc-consent-order.pdf
  (passages read)
- Perold, A. F., & Sharpe, W. F. (1995). Dynamic strategies for asset allocation. *Financial Analysts Journal,
  51*(1), 149–160. https://doi.org/10.2469/faj.v51.n1.1871 (Original work published 1988) (read in full in this
  January-February 1995 reprint at https://web.stanford.edu/class/msande348/papers/PeroldSharpe.pdf; cite in the text
  as Perold & Sharpe, 1988/1995)
- Presidential Task Force on Market Mechanisms. (1988). *Report of the Presidential Task Force on Market Mechanisms*.
  U.S. Government Printing Office. https://archive.org/stream/reportofpresiden01unit/reportofpresiden01unit_djvu.txt
  (passages read; also at https://sechistorical.org/wp-content/uploads/1988_0101_BradyReport.pdf)
- U.S. Securities and Exchange Commission. (2010). *Investment company advertising: Target date retirement fund names
  and marketing* (Release Nos. 33-9126, 34-62300, IC-29301). https://www.sec.gov/files/rules/proposed/2010/33-9126.pdf
  (passages read)
- U.S. Securities and Exchange Commission, Division of Market Regulation. (1988). *The October 1987 market break*.
  https://sechistorical.org/wp-content/uploads/1988_0201_MarketBreak_01.pdf (passages read)
- U.S. Securities and Exchange Commission & U.S. Department of Labor. (2009, June 18). *Public hearing on target date
  funds and other similar investment options* [Transcript]. https://www.sec.gov/spotlight/targetdatefunds/targetdatefunds061809.pdf
  (passages read)
- U.S. Securities and Exchange Commission, Office of Investor Education and Advocacy, & Financial Industry Regulatory
  Authority. (2011, June 2). *Structured notes with principal protection: Note the terms of your investment* [Investor
  alert]. https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/structured

Seen only as an abstract, an excerpt or a secondary report (UNVERIFIED):
- Black, F., & Perold, A. F. (1992). Theory of constant proportion portfolio insurance. *Journal of Economic Dynamics
  and Control, 16*(3–4), 403–426. https://doi.org/10.1016/0165-1889(92)90043-E (abstract)
- Cont, R., & Tankov, P. (2009). Constant proportion portfolio insurance in the presence of jumps in asset prices.
  *Mathematical Finance, 19*(3), 379–401. https://doi.org/10.1111/j.1467-9965.2009.00377.x (abstract)
- Ambrose, E. (2003, May 4). Principal-protected funds sound friendly, could bite. *Daily Press*.
  https://www.dailypress.com/2003/05/04/principal-protected-funds-sound-friendly-could-bite
- ETF Database. (n.d.). *IBTA: iShares iBonds Dec 2021 Term Treasury ETF*. Retrieved November 13, 2026, from
  https://etfdb.com/etf/IBTA
- Jacobs, B. I. (1997, October 13). Crash showed danger of 'insured' assets. *Pensions & Investments*.
  http://jlem.com/documents/FG/jlem/articles/590531_580871_752_Crash_Showed_Danger_of_Insured_Assets.pdf (the
  newspaper's reprint of two chapters of the book below, before it was published)
- Jacobs, B. I. (1999). *Capital ideas and market realities: Option replication, investor behavior, and stock market
  crashes*. Blackwell Publishers. (not read)
- Jessen, C. (2014). Constant proportion portfolio insurance: Discrete-time trading and gap risk coverage. *The
  Journal of Derivatives, 21*(3), 36–53. https://doi.org/10.3905/jod.2014.21.3.036 (abstract)
- Stempel, J. (2011, April 11). UBS fined for misleading clients about Lehman debt. *Fox Business*.
  https://www.foxbusiness.com/markets/ubs-fined-for-misleading-clients-about-lehman-debt
- Rubinstein, M. (1988). Portfolio insurance and the market crash. *Financial Analysts Journal, 44*(1), 38–47.
  https://doi.org/10.2469/faj.v44.n1.38 (abstract read at
  https://rpc.cfainstitute.org/research/financial-analysts-journal/1988/portfolio-insurance-and-the-market-crash; DOI and
  pages from the Crossref record)
- Skinner, L. (2011, April 10). UBS to shell out $10.75M to settle Lehman-related row. *InvestmentNews*.
  https://www.investmentnews.com/fixed-income/ubs-to-shell-out-1075m-to-settle-lehman-related-row/35534

Cited through other cards (read there): card Q16 (iBond notices, IBTF fact sheet, FRED yields; its S1-S9) and card
Q2a (LDI 2022, Reserve fund 2008).
