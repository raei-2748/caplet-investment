# Q36 research cards: can an iBonds Treasury fund's end date move, and who decides?

Fri 13 Nov 2026, Sydney evening. Report parts: 3e (assumptions, limits and what to watch) and Table 3 (row 4, "iBond
fund notices, the floor's too"), with a knock-on for Figure 1's note (the cash-date ranges, NUMBERS 8h).
Notes for the Final Report store, not report prose.

Checked against: Caplet's FINAL IPS (`keel/final_report/FINAL_IPS_as_submitted.txt` l.11, l.13, frozen: "Held to the
end", the two reasons), the Trading Notes (`keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt` l.13, l.15: the
iBond payout "is a net asset value, as opposed to a promise of par"), `CANON.md` (A8, B6, B23, C2, D5), `NUMBERS.md`
(sections 2, 8g, 8h; every plan figure here is quoted from there and is MODEL), `exhibits/tables.md` Table 3 (row 4 and
its note, page cost 21.9 lines), and the cards this one builds on: Q3b (line 23: early end "UNVERIFIED and unsized"),
Q16 (rows 1, 4, 6, 7: the payout history; cited, not repeated), Q26 (rows 11, 12, 14, 16, 17, 21; card 2), Q30 (row 4
before the cut; T19 "Early end | Merged into row 4"). The plan is frozen: a "risk" in the Clash column is a risk to
record, never a change to propose.

**Claims tested**
1. Keep, kill or change: "The iShares Trust board can move an iBonds Treasury fund's end date later without a
   shareholder vote, and must give notice first; Table 3 row 4 watches the right event."
2. Keep, kill or change: "Ending a fund early cannot leave a payment unfunded: the cash comes sooner, and the operating
   reserve is already sized as if money received earns nothing."
3. Keep, kill or change: "Nothing else in the funds' documents can leave a payment unfunded: suspension of redemptions
   (1940 Act section 22(e)), a final distribution in kind instead of cash, a merger into another fund, delisting, or a
   change of objective."

**Problem class and the field that solved it.** Who holds the power to change the terms of a pooled vehicle that an
investor cannot vote down, and how much warning the investor gets. Investment company law and fund governance answer
it: the trust's own charter under Delaware statutory trust law (the iShares Trust Declaration of Trust, 2009, still
in force in 2026), the federal floor in the Investment Company Act of 1940 (section 22(e) on redemption dates, Rule
17a-8 on mergers, Rule 35d-1 on names, Rule 6c-11 on ETFs), and practice shown in the funds' own SEC filings
(prospectus supplements announcing closures). Finance research on ETF closures (Boehmer and Finta, 2023) and the
SEC's investor bulletin on fund liquidations give the base rates and the investor's best move.

## Verdicts in one screen

1. **Claim 1: CHANGE.** The power is right: under the Declaration's term-fund clause (s.11.04(d)) and the prospectus, a
   board majority may extend a fund's end "if a majority of the Board determines the extension to be in the best
   interest of the Fund", with no shareholder vote. "Must give notice first" is wrong: no document sets a notice period
   for an extension. The only practice is the ending notice about two months ahead, in mid-October, four years running
   (Q16 row 7; Q26 row 17). No iBonds fund has ever been extended or ended early in iShares Trust's filings (EDGAR
   full-text search, 13 Nov 2026). Row 4 watches one event of three: it misses an early end and a merger, and it
   cannot see a silent extension. Add "no ending notice by 31 October" and "ends a fund early, merges it" (section c).
2. **Claim 2: CHANGE.** The first half is right and newly verified: the board alone can end a fund early under
   s.11.04(c) if it finds the fund can no longer run "in an economically viable manner" (assets too small, a change in
   law). This settles Q3b line 23's UNVERIFIED. Real early ends give about two months' notice (61 to 66 days from
   notice to last trade, four closures) and pay cash at net asset value 3 to 7 calendar days after the last NAV, with
   the liquidation's costs inside that NAV. The second half is wrong: the reserve's 0% standard counts each fund's
   payout at its end. Cash paid early is the market value of the same Treasuries, smaller by the interest still to
   come (MODEL arithmetic: about 7.5% less, two years early at a 4% yield). The standard is met with $0 to spare once
   the Treasury-bill ETF's fee is charged (NUMBERS 2 and 8h), so early cash left waiting would leave that payment
   short. The fix is already Table 3 row 4's action: buy a Treasury due before the payment the day the cash arrives.
3. **Claim 3: KEEP, with one move.** None of the five can leave a payment unfunded in dollars: a suspension is capped
   by 22(e) at seven days except a market closure, an emergency or an SEC order (a date risk, Table 3 row 5's "a
   halt"); an in-kind payout at the end would be cash and Treasuries due by 15 December; delisting stops exchange
   sales, not the fund's payout; an objective or index change needs 60 days' notice for the 80% policy. But a merger
   (no shareholder vote unless Rule 17a-8 needs one; at least 30 days' written notice, s.11.05(c)) could move the
   money into a fund with another end date, so it belongs in row 4's watch with the early end.
4. **One new fit (store, or Figure 1's note):** seven calendar days after each fund's end is exactly the last date of
   each cash range in NUMBERS 8h (22 Dec; 24 Dec 2035 for IBTQ). Every closure read here paid inside seven days. If
   22(e) binds the final payout (Keel's reading), the ranges' last dates are the law's limit, not just history.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | The fund's end date is the board's: the term-fund clause lets a board majority wind up a series on the date its prospectus names, with no shareholder vote | iShares Trust (2009) s.11.04(d); iShares Trust (2026a) | LADDER, FLOOR, RESERVE2033 | KNOWN | "Held to its end" means to the board's date, which the IPS cannot fix; the five funds and the floor in IBTM (32.50% at cost, NUMBERS 8g) all rest on it | Q16 row 4 and Q26 row 11 quote the prospectus; this row adds the clause behind it (series set up after 16 Sep 2009, so all five) | VERIFIED (Declaration s.11.04(d) read in full; prospectus 27 Feb 2026) | risk: CANON C2 and D5 ("pay what they say") hold only at the board's date; already recorded as NAV, not par (TNA l.15) | Declaration of Trust, Article XI |
| 2 | Extension: "The Board may extend the termination date if a majority of the Board determines the extension to be in the best interest of the Fund"; no notice period anywhere | iShares Trust (2026a); iShares Trust (2026b); iShares Trust (2009) s.11.04(d)(ii) | LADDER, FLOOR | KNOWN | Claim 1's "must give notice first" is not in any document; a silent extension is possible on paper | Q26 row 11 has the power, not the missing notice period | VERIFIED (prospectus, SAI and Declaration read) | no | Prospectus, each fund's "Principal Investment Strategies"; SAI |
| 3 | An extension would show as a prospectus supplement, since s.11.04(d) works "in accordance with the registration statement (as supplemented)" | iShares Trust (2009) s.11.04(d) | LADDER, PROCESS | NICHE | The team's watch reads the fund page and the fund's Form 497 supplements, not only the press release | Keel inference from the clause's words; no rule says how far ahead | UNVERIFIED (inference) | no | Declaration s.11.04(d) |
| 4 | Ending notices came about two months ahead, in mid-October, four years running (2023 to 2026); silence by 31 October is the cheap warning | Card Q16 row 7; card Q26 row 17; iShares Trust (2026d) | LADDER, RESERVE2033, PRESENTATION | NICHE | Row 4's trigger: "No ending notice by 31 October" | Q30 row 4 had "No notice by 31 Oct" before the cut; the eight-row Table 3 dropped it | VERIFIED (Q16 and Q26 read the notices at source) | no | Q16, Q26, Q30 |
| 5 | No iBonds fund has been extended or ended early in iShares Trust's filings; four of four Treasury iBonds ended on schedule | U.S. SEC (n.d.) EDGAR full-text search; card Q16 row 6; card Q26 row 17 | LADDER, CERTAINTY | NICHE | Base rate for 3e: none found, so the watch is cheap insurance, not a forecast | A word search, not a census; 3 of 10 "iBonds" plus "close and liquidate" hits opened: all were other funds (2016: inflation-linked and rated corporate bond ETFs) in combined filings | VERIFIED (searches run 13 Nov 2026; hits opened) | no | EDGAR full-text search, iShares Trust (CIK 1100663), Form 497 |
| 6 | Early end without a vote: a board majority may sell and distribute a series if it cannot run "in an economically viable manner" (e.g. "inability ... to maintain its assets at an appropriate size", changes in law) | iShares Trust (2009) s.11.04(c); iShares Trust (2026b) | LADDER, FLOOR, RESERVE2033 | NICHE | Settles Q3b line 23: yes, the board alone can end a fund early | Q26 row 12 had the SAI's "only a majority vote of the Board is required"; this is the clause it points to | VERIFIED (Declaration s.11.04(b)-(c) read in full) | risk: not one of the IPS's two reasons; handled as an instrument swap, never a plan change | Declaration s.11.04(c) |
| 7 | iShares' wording names only a later date; Invesco's BulletShares say the board "may change the termination date" (2026), "to an earlier or later date" (2018) | iShares Trust (2026a); Invesco Exchange-Traded Self-Indexed Fund Trust (2026); Invesco Exchange-Traded Self-Indexed Fund Trust (2018) | LADDER | NICHE | An earlier iShares end rests on s.11.04(c) or a shareholder vote, not on the term clause | Whether a supplement could set an earlier date under s.11.04(d) is a legal question | VERIFIED (BSTS summary prospectus read in full); 2018 "earlier or later" wording UNVERIFIED (search excerpt) | no | BSTS 497K, "Principal Investment Strategies" |
| 8 | Precedent: Invesco's board ended two term bond ETFs years early (BulletShares 2023 and 2024 USD Emerging Markets Debt, BSCE and BSDE): vote 20 Jan 2023, last trade 30 Mar, cash at NAV about 6 Apr | Invesco Exchange-Traded Self-Indexed Fund Trust (2023) | LADDER, FLOOR | NICHE | What an early end looks like: 66 days from notice to last trade; cash 7 calendar days (5 business days) later | Emerging-market corporate debt, small funds (size from a news excerpt, UNVERIFIED), not Treasuries | VERIFIED (supplement read in full) | no | Form 497, 23 Jan 2023 |
| 9 | iShares closures: board vote; about 61 to 66 days to the last trade; halt next morning; cash 3 to 7 calendar days after the last NAV; "automatically redeem your shares for cash"; final NAV "will include any costs associated with the liquidation" | iShares Trust (2016); iShares Trust (2025); iShares Trust (2026e) | LADDER, FLOOR, RESERVE2033 | KNOWN | An early end gives about two months to arrange the swap; cash at NAV, net of liquidation costs | Q16 row 7 shows the same mechanics at term ends; Q26 row 14 sizes costs (0.5% cut) | VERIFIED (2025 and 2026 supplements read in full; 2016 closure passage read) | no | Form 497 supplements |
| 10 | 633 US ETFs closed 2012 to 2019 (about 30% of ETFs); about a month from announcement to halt; shares often trade at a discount after the news; holders "may be better off doing nothing" and taking NAV when no extra closing fee is charged | Boehmer and Finta (2023) | LADDER, REINVEST | KNOWN | On an early-end notice: hold for cash at NAV, never sell into the discount; then the swap | Sample mostly equity; Treasury funds trade near NAV; taxes are out of the case's scope | VERIFIED (paper read: introduction, data, conclusion; finance, not psychology) | no | SSRN 4328422 |
| 11 | Early cash is smaller than the end payout: NAV before the end is the market value of the same Treasuries, short of the end payout by the interest still to come | Keel arithmetic; NUMBERS 2 and 8h ($0 spare with the fee; $1,414 without) | RESERVE2033, REINVEST, LADDER, CERTAINTY | NICHE | Claim 2 changes: the 0% standard does not cover early cash left waiting; it must buy a Treasury due before the payment at once (row 4's action) | Q26 row 12 and card 2 already say "buys back about the same cash flows" | VERIFIED (NUMBERS 2, 8h); the 7.5% example is MODEL | risk: a text saying "an early end cannot hurt" would misstate the 0% standard | NUMBERS 8h; card Q26 card 2 |
| 12 | Section 22(e): no fund may suspend redemption or delay payment "for more than seven days", except when the NYSE is closed or restricted, in an emergency, or by SEC order | 15 U.S.C. 80a-22(e) | LADDER, RESERVE2033 | TEXTBOOK | The legal outer bound on a fund's cash date | Shares are redeemable only in Creation Units (BSTS: "Except when aggregated in Creation Units, the Shares are not redeemable securities") | VERIFIED (statute text) | no | Investment Company Act s.22(e) |
| 13 | Seven calendar days after each end is exactly the last date of each cash range (Wed 22 Dec 2032 ... Mon 24 Dec 2035 for IBTQ; Mon 22 Dec 2036); all four closures read paid inside seven days | NUMBERS 8h; 15 U.S.C. 80a-22(e); iShares Trust (2026b); closures in rows 8-9 | LADDER, RESERVE2033, PRESENTATION | NICHE | Figure 1's note could say the ranges end at the law's limit, not only at history | Keel reading: at termination the board may make shares individually redeemable (SAI) and the notices call the payout an automatic redemption, so 22(e) likely binds it; not a legal opinion | VERIFIED (statute, 8h dates, notices); the link is Keel's reading | no | NUMBERS 8h; 22(e) |
| 14 | Suspension: the Trustees may suspend redemption "as permitted under the 1940 Act", effective by the next business day; SAI lists four cases; the SEC once ordered a fund's redemptions suspended (Reserve Fund, 2008) | iShares Trust (2009) s.9.02, s.9.04; iShares Trust (2026b); U.S. SEC (2008) | LADDER, RESERVE2033 | KNOWN | A date risk only, already Table 3 row 5 ("a halt"); dollars still arrive | Q26 row 16 records halts | VERIFIED (Declaration, SAI; the 2008 order as in REFERENCES #354, read 12 Nov) | no | Declaration Article IX; SAI "Redemption" |
| 15 | In kind: whether a distribution, "including any distribution paid upon termination", is cash or other trust property is "wholly in the discretion of the Trustees"; at termination the fund may pay in kind, in cash or both | iShares Trust (2009) s.9.01-9.02; iShares Trust (2026b) | LADDER, RESERVE2033 | NICHE | Near its end a fund holds cash and Treasuries due by 15 December, so an in-kind payout still pays before 1 January; a broker step, not a gap | Practice is cash, four of four (Q16 row 7) | VERIFIED (Declaration and SAI read) | no | Declaration s.9.01; SAI "Termination" |
| 16 | Merger without a vote: a fund set up after 24 Sep 2008 may merge into another iShares fund "unless such vote is required by the 1940 Act", with "at least 30 days' prior written notice" | iShares Trust (2009) s.11.05(c)-(d); iShares Trust (2026b) | LADDER, FLOOR | NICHE | A merger into a fund with another end date is the same swap; add "merges it" to row 4's watch | No iBonds merger found; Rule 17a-8 (row 17) can force a vote | VERIFIED (Declaration read in full) | no | Declaration s.11.05 |
| 17 | Rule 17a-8: a merging fund's holders must vote unless its fundamental policies and advisory contract are not materially different, the boards overlap as set out, and 12b-1 fees are no higher | 17 C.F.R. 270.17a-8(a)(3) | LADDER | TEXTBOOK | Limits row 16; a merger into a fund of another kind would need a vote | Whether iBonds' fundamental policies match other iShares funds' was not checked | VERIFIED (rule text) | no | Rule 17a-8 |
| 18 | Objective and index "may be changed without shareholder approval"; the 80% index policy needs "at least 60 days" notice; Invesco states the same 60 days | iShares Trust (2026a); iShares Trust (2026b); Invesco Exchange-Traded Self-Indexed Fund Trust (2026) | LADDER | KNOWN | An index change that moved the maturity window would come with 60 days' notice; same swap | No precedent found | VERIFIED (prospectus, SAI non-fundamental policy 2) | no | Prospectus; SAI "Investment Policies" |
| 19 | Delisting triggers: fewer than 50 holders after 12 months, loss of Rule 6c-11 status, listing rules not kept, the exchange's opinion, and termination | iShares Trust (2026b) | LADDER | KNOWN | Delisting stops exchange sales, not the fund: it still holds the Treasuries and pays NAV at its end | Q26 row 21 (Rule 6c-11) | VERIFIED (SAI read) | no | SAI "Continued Listing" |
| 20 | Holders have little say: votes only on trustees, advisory contracts and what law requires; Trustees may require redemption "for any reason" and amend the Declaration without a vote except listed matters | iShares Trust (2009) s.7.01, s.9.02, s.11.08 | LADDER, OTHER | NICHE | Laura's protection is the watch and the swap, never a vote | None recorded | VERIFIED (Declaration read in full) | no | Declaration Articles VII, IX, XI |
| 21 | Liquidation rules "depend on state corporate or trust law, on the fund's charter documents, or both"; holders "may or may not have a say"; ETFs announce by press release; holders "can sell ... any time before the fund stops trading" | U.S. SEC (2021) | LADDER, PROCESS | TEXTBOOK | The watch reads press releases and Form 497 supplements; selling before the halt is allowed but rows 10-11 say wait for NAV, then swap | General guidance, not iShares-specific | VERIFIED (bulletin read in full) | no | Investor.gov bulletin |
| 22 | The 2009 Declaration is still the Trust's charter: the Form 8-A of 7 Jul 2026 points to it | iShares Trust (2026f) | OTHER | NICHE | The clauses in rows 1, 6, 14-16 and 20 apply in 2026 | Amendments after 2009 not separately searched | VERIFIED (8-A read) | no | Form 8-A |
| 23 | "Never: the shares" in row 4 could be read as the iBond fund's own shares, yet an extension's step is to sell those on the exchange before the payment | exhibits/tables.md Table 3 row 4; WORDS l.26; card Q26 card 2 | PRESENTATION | NICHE | A reader slip, not an error: WORDS defines "the shares" as the world share fund | None recorded | VERIFIED (table and WORDS read) | no | Table 3 |

## (b) Cards

**Card 1. Two powers in one clause: the board can extend a fund's end, or end it early (iShares Trust Declaration,
s.11.04(c)-(d); prospectus 27 Feb 2026).**
- What is it? The Declaration's term-fund clause lets a board majority wind up any series set up after 16 Sep 2009 on
  the date its registration statement names, with no shareholder vote, and lets the board extend that date if it finds
  an extension "in the best interest". A separate clause, s.11.04(c), lets a board majority sell and distribute any
  series, with no vote, if it finds the series cannot run "in an economically viable manner" (too small, a change in
  law, adverse economic trends). Neither clause sets a notice period.
- Did it work? Both powers are in force (the Form 8-A of 7 Jul 2026 still points to the 2009 Declaration). Neither has
  been used on an iBonds fund: four of four Treasury iBonds ended on schedule (Q16 row 6; Q26 row 17), and EDGAR
  finds no extension or early end.
- How is Laura's case like it? Every iBond rung (2033 to 2037) and the floor inside IBTM (32.50% of $300,000 at cost,
  NUMBERS 8g) pays on the board's date. An extension past 31 December or an early end are the two ways someone else
  could change a cash date.
- How is it not? A board ending a multi-year Treasury fund early would need the economic-viability finding; Caplet's
  funds are Treasury-only and the series has never been extended. The power is real; its use is so far unseen.
- What Caplet takes: 3e, at most one clause naming the board as the one who sets each end, and that any change brings
  Table 3's swap. Table 3 row 4's watch gains "ends a fund early" (section c). Q3b line 23's UNVERIFIED is now settled.

**Card 2. What an early end looks like in practice (Invesco 2023; iShares 2016, 2025, 2026; Boehmer and Finta).**
- What is it? Invesco's board ended its 2023 and 2024 emerging-market BulletShares (BSCE, BSDE) on 20 Jan 2023: notice
  23 Jan, last trade 30 Mar, cash at NAV on or about 6 Apr. iShares closures follow the same script: board vote,
  supplement, 61 to 66 days to the last trade, halt the next morning, cash 3 to 7 calendar days after the last NAV,
  the final NAV "will include any costs associated with the liquidation". Across 633 US ETF closures (2012-2019) the
  average gap from announcement to halt was about a month.
- Did it work? Holders who did nothing got cash at NAV within a week of the last trade in every case read. The paper
  finds shares often trade at a discount after the announcement, so holders "may be better off doing nothing" and
  waiting for NAV when the issuer charges no extra closing fee.
- How is Laura's case like it? An early end of any of her five funds would arrive with about two months' warning and
  pay cash at NAV, net of liquidation costs (Q26 row 14's 0.5% cut covers this kind of cost).
- How is it not? BSCE and BSDE held emerging-market corporate debt and were small; iShares' 2016-2026 closures were
  not term funds. A Treasury iBond's NAV is easy to price, so the discount the paper finds should be small.
- What Caplet takes: the store; one line in Table 3's note at most. The action on any closure notice is "hold for cash
  at NAV, then swap", never a sale into the discount.

**Card 3. Why early cash must not wait: the 0% standard counts payouts at their end (NUMBERS 2 and 8h).**
- What is it? The reserve meets the escrow standard "sufficient without reinvestment": each payment is met if money
  already received earns nothing, after the Treasury-bill ETF's 0.15% fee, with $0 to spare (and $1,414 without the
  fee). Each fund's payout is counted at its end. Cash paid early is the market value of the same Treasuries, which is
  less than their end value by the interest still to come.
- Did it work? Arithmetic, MODEL: two years early at a 4% yield, cash is about 92.5% of the end payout; left at 0%, that
  payment would be about 7.5% short. Bought back at once into a Treasury due before the payment, the same cash buys
  about the same end value (Q26 row 12's inference), less trading costs.
- How is Laura's case like it? Exactly the case: no spare dollars at 0% with the fee, so any early cash that waits
  turns into a gap.
- How is it not? At today's rates the reserve is 111.4% funded on 1 Jan 2033 ($444,545 against $399,089, NUMBERS 8h),
  so a short wait at market rates costs little; the 0% world is the test, not the forecast.
- What Caplet takes: claim 2 changes. Table 3 row 4's action ("the fund, for a Treasury due in time, paid from the
  reserve") already handles it; the note may add that early cash buys that Treasury the day it arrives.

**Card 4. The law's seven days and the cash ranges (15 U.S.C. 80a-22(e); NUMBERS 8h).**
- What is it? Section 22(e) forbids a fund to delay a redemption payment "for more than seven days" except when the NYSE
  is closed or restricted, in an emergency that makes selling or valuing impracticable, or by SEC order. At termination
  the board may make shares individually redeemable (SAI), and iShares' notices call the final payout an automatic
  redemption for cash.
- Did it work? Every closure read here paid inside seven calendar days of the last NAV (3 to 7). The one famous use of
  exception (3) is the SEC's 2008 order suspending the Reserve Fund's redemptions.
- How is Laura's case like it? Seven calendar days after each fund's end lands on the last date of each cash range in
  NUMBERS 8h: Wed 22 Dec 2032 (IBTM), Thu 22 Dec 2033, Fri 22 Dec 2034, Mon 24 Dec 2035 (IBTQ, end taken as Mon 17
  Dec), Mon 22 Dec 2036 (IBTR). All are before 1 January.
- How is it not? Shares are redeemable only in Creation Units outside termination, so applying 22(e) to the final
  payout is Keel's reading, not a legal opinion; an exception can push past seven days.
- What Caplet takes: store, or a few words in Figure 1's note ("the last date is the law's seven-day limit"); the
  exceptions are Table 3 row 5's "a halt".

**Card 5. The rest of the list: merger, objective change, in kind, delisting, suspension.**
- What is it? A merger needs no vote unless Rule 17a-8 needs one, with "at least 30 days' prior written notice"
  (s.11.05(c)). The objective and index can change without a vote; the 80% policy needs 60 days' notice. A termination
  payout may be in kind (s.9.01; SAI). The exchange can delist on four triggers. The Trustees can suspend redemption
  within 22(e).
- Did it work? None has touched an iBonds Treasury fund in the filings read.
- How is Laura's case like it? Only the merger can change a cash date by itself (money moved into a fund that ends on
  another date). The others either keep the dollars (in kind, delisting) or move a date by days (suspension).
- How is it not? Each comes with a notice the team would see, except a suspension, which is a market-wide event.
- What Caplet takes: row 4's watch adds "merges it"; the rest stays in the store.

## (c) Verdicts

**Claim 1: CHANGE.**
- Keep: the board can extend without a shareholder vote (prospectus: "The Board may extend the termination date if a
  majority of the Board determines the extension to be in the best interest of the Fund"; Declaration s.11.04(d)(ii):
  the registration statement must say "that the Trustees may extend such termination date if a majority of the
  Trustees determines that an extension is in the best interest of such Series").
- Kill: "must give notice first". No document sets any notice period for an extension. The only practice is the ending
  notice in mid-October (16 Oct 2023, 17 Oct 2024, 15 Oct 2025, 15 Oct 2026; Q16 row 7, Q26 row 17). An extension
  would likely appear as a prospectus supplement (Keel inference from s.11.04(d)'s "as supplemented"), but nothing
  fixes how early.
- Precedent: none. EDGAR full-text search of iShares Trust's Form 497s finds no iBonds extension and no iBonds early end;
  the three opened "close and liquidate" hits were other funds in combined filings. Invesco's BulletShares documents
  allow a change "to an earlier or later date" (2018 wording, excerpt) and today say "may change the termination date"
  (BSTS, 2026); iShares names only an extension.
- Row 4 is incomplete: it watches only "A notice that moves a fund's end date past a payment". It misses an early end
  and a merger, and it cannot see an extension made without a mid-October notice.

**Claim 2: CHANGE.**
- Keep: the board can end a fund early, alone. Declaration s.11.04(c): the Trustees may sell and distribute "without
  obtaining the approval of shareholders if a majority of the Trustees determines that the continuation of the Trust or
  Series ... is not in the best interests ... as a result of factors or events adversely affecting the ability of ...
  such Series ... to conduct its business and operations in an economically viable manner", e.g. "the inability ... to
  maintain its assets at an appropriate size" or "changes in laws or regulations". The SAI's "in certain circumstances
  described in the Declaration of Trust, only a majority vote of the Board is required" (Q26 row 12) points here.
- Keep: the cash comes sooner and at NAV. Four real closures: 61 to 66 days from notice to the last trade, cash 3 to 7
  calendar days after the last NAV, liquidation costs inside the final NAV (rows 8-9).
- Kill: "the operating reserve is already sized as if money received earns nothing" does not cover it. The standard
  counts each payout at its end; an early payout is smaller by the interest still to come, and the standard has $0 to
  spare with the fee (NUMBERS 2, 8h). Left waiting, early cash would leave its payment short (MODEL: about 7.5% for two
  years at 4%).
- Change to: "An early end pays cash at net asset value about two months after notice; that cash buys a Treasury due
  before the payment the day it arrives (Table 3 row 4), so the payment is funded again, less trading and liquidation
  costs." (A claim for the store, not report text.)
- Also: an early end of IBTM moves the floor too, so the range's bottom (WORDS: what the floor pays) would be restated
  from the new Treasury's face. Store only.

**Claim 3: KEEP, with one move to row 4.**
- Suspension (22(e); Declaration s.9.04; SAI): KEEP. Capped at seven days except NYSE closed or restricted, an
  emergency, or SEC order; the Trustees' declaration takes effect "not later than the close of business on the business
  day next following". Precedent: the SEC's 2008 Reserve Fund order (REFERENCES #354). A date risk only; Table 3 row
  5 already watches "a halt". Seven days after each end is the last date of each 8h range (Card 4).
- In kind (s.9.01-9.02; SAI "Termination"): KEEP. The Trustees decide, and the SAI allows cash, in kind or both, with
  an in-kind election above a stated minimum. Near its end a fund holds cash and Treasuries due by 15 December, which
  still pay before 1 January. Practice: cash, four of four. Store only.
- Merger (s.11.05(c)-(d); Rule 17a-8): MOVE to row 4. No vote unless 17a-8 needs one; at least 30 days' written notice.
  It could put the money in a fund with another end date. No iBonds precedent found.
- Delisting (SAI "Continued Listing"): KEEP. Fewer than 50 holders after 12 months, loss of Rule 6c-11 status, listing
  rules not met, the exchange's opinion, or termination. The fund still holds the Treasuries and pays NAV at its end.
  Store only.
- Change of objective or index (prospectus; SAI policy 2): KEEP. No vote; 60 days' notice for the 80% policy. If it
  moved the maturity window it would be the same swap; the notice gives time. Store only.
- None needs a sale of the world share fund, and none is one of the IPS's two reasons (a missed deposit; a Treasury
  default).

**Proposed Table 3 row 4 (a note for the lead; do not edit the exhibit from this card).**

Now:
`| iBond fund notices, the floor's too | Team | Cash in 4 to 9 business days before the year's last (4 to 6 for 2036) | A notice that moves a fund's end date past a payment | *Changes: *the fund, for a Treasury due in time, paid from the reserve. *Never: *the amount; the shares. |`

Recommended (one cell changes, about ten words more):
`| iBond fund notices, the floor's too | Team | Cash in 4 to 9 business days before the year's last (4 to 6 for 2036) | No ending notice by 31 October, or one that ends a fund early, merges it or moves its end past a payment | *Changes: *the fund, for a Treasury due in time, paid from the reserve. *Never: *the amount; the shares. |`

- The action cell stays: "a Treasury due in time" covers all three events (an early end's cash, a merged fund's shares
  sold, an extended fund's shares sold before the payment).
- Optional Table 3 note item (about ten words): an early end's cash buys that Treasury the day it arrives. Take it only
  if the page budget allows (21.9 lines now).
- "Never: the shares" can stay: WORDS l.26 defines the shares as the world share fund. If a reader slips, "the world
  share fund" is the fix (row 23).

**Where each strong finding lands.**
- Row 4's new trigger (no ending notice by 31 October; early end; merger): Table 3 row 4.
- The board sets each end and can end a fund early (Card 1): one clause in 3e at most; else the store.
- Early cash must not wait (Card 3): Table 3's note, optional; the store.
- 22(e)'s seven days match the cash ranges (Card 4): Figure 1's note, optional; the store.
- Closure practice and Boehmer and Finta (Card 2); in kind, delisting, objective change, suspension (Card 5): store only.

## (d) Gaps

- IBTR's own statutory prospectus was not read today; the 27 Feb 2026 prospectus read covers the Dec 2026 to Dec 2035
  funds (IBTM, IBTO, IBTP, IBTQ). IBTR's 497K (Q26 source 7) was read by Q26; whether the SAI read today also covers
  IBTR was not checked.
- No "plan of liquidation" document for an iBonds fund was found; its terms (timing, cash or in kind) are known only
  from the prospectus and past notices.
- 7 of the 10 EDGAR hits for "iBonds" plus "close and liquidate" (2019, 2023, 2024; lower scores) were not opened.
- Whether a prospectus supplement could set an earlier date under s.11.04(d) needs a legal opinion; this card treats an
  earlier date as resting on s.11.04(c) or a vote.
- Whether 22(e) binds a liquidating distribution is Keel's reading from the notices' word "redeem"; not verified law.
- BSCE and BSDE fund sizes and the reason for their closure come from a news excerpt (ETF.com, 25 Jan 2023), not read
  in full: UNVERIFIED. The supplement gives no reason.
- Invesco's 2018 "to an earlier or later date" wording was read in a search excerpt only: UNVERIFIED. The 2026 BSTS
  wording was read in full.
- Boehmer and Finta: the full PDF was retrieved; the introduction, data section and conclusion were read, the tables
  only in part. It is a finance working paper, not psychology, so no retraction check applies.
- The SEC's 2008 Reserve Fund order was cited from REFERENCES #354 (read 12 Nov by card Q2a), not re-read today.
- IBTM's net assets were not checked today, so the chance of an economic-viability finding cannot be sized.
- Rule 17a-8's vote test for an iBonds merger (do iBonds' fundamental policies match the likely surviving fund's?) was
  not checked.
- The etf.com fund closure study was not read in full.
- REFERENCES_APA.md: no wrong entry found for the sources reused (#78, #354; Q26's 2026a, 2026b, 2026d). Entry #139's
  existing flag stands.
- Card Q3b line 23 ("Whether the board can end a fund early is UNVERIFIED and unsized") can now read VERIFIED for the
  power (s.11.04(c)); its owner should update it. This card does not edit Q3b.

## Sources (APA 7; all accessed 13 Nov 2026)

Already in `../REFERENCES_APA.md` (use those entries): #78 IBTM summary prospectus (27 Feb 2026); #354 U.S. SEC (2008),
Investment Company Act Release No. 28386 (Reserve Fund). Already in card Q26's Sources: iShares Trust (2026a)
prospectus; (2026b) SAI as supplemented 11 Sep 2026; (2026c) IBTR 497K; (2026d) 15 Oct 2026 supplement (IBDR, IBTG,
IBHF); Exchange-traded funds, 17 C.F.R. § 270.6c-11 (2026).

New, read at the source:
1. Boehmer, E., & Finta, M. A. (2023). *Are investors better off doing nothing during exchange-traded fund closures?*
   [Working paper]. SSRN. https://doi.org/10.2139/ssrn.4328422 (full text read at
   https://acfr.aut.ac.nz/__data/assets/pdf_file/0004/809644/Exchange-Traded-Fund-Closures-FULL-ssrn-maf2.pdf)
2. Invesco Actively Managed Exchange-Traded Fund Trust. (2023, January 23). *Supplement dated January 23, 2023 to the
   prospectuses and statements of additional information* [Form 497]. U.S. Securities and Exchange Commission.
   https://www.sec.gov/Archives/edgar/data/1418144/000110465923005865/tm233913d21_497.htm
3. Invesco Exchange-Traded Self-Indexed Fund Trust. (2018, September 28). *Summary prospectus: Invesco BulletShares 2026
   Corporate Bond ETF* [Form 497K]. U.S. Securities and Exchange Commission.
   https://www.sec.gov/Archives/edgar/data/1657201/000119312518286612/d600591d497k.htm (search excerpt only; UNVERIFIED)
4. Invesco Exchange-Traded Self-Indexed Fund Trust. (2023, January 23). *Supplement dated January 23, 2023 to the
   prospectuses and statements of additional information dated December 16, 2022* [Form 497]. U.S. Securities and
   Exchange Commission. https://www.sec.gov/Archives/edgar/data/1657201/000110465923005868/tm233913d2_497.htm
5. Invesco Exchange-Traded Self-Indexed Fund Trust. (2026, June 3). *Summary prospectus: Invesco BulletShares 2028
   Treasury Bond ETF* [Form 497K]. U.S. Securities and Exchange Commission.
   https://www.sec.gov/Archives/edgar/data/1657201/000119312526258724/d123552d497k.htm
6. iShares Trust. (2009, September 17). *Amended and restated agreement and declaration of trust* (Exhibit (a) to
   Post-Effective Amendment No. 303, Form N-1A, filed October 16, 2009). U.S. Securities and Exchange Commission.
   https://www.sec.gov/Archives/edgar/data/1100663/000119312509209172/dex99a.txt
7. iShares Trust. (2016, August 1). *2016 prospectus: iShares iBonds Dec 2021 Term Muni Bond ETF* (as revised August 1,
   2016; with supplements on the liquidation of the iShares Global and International Inflation-Linked Bond ETFs and
   the B - Ca and Baa - Ba Rated Corporate Bond ETFs) [Form 497]. U.S. Securities and Exchange Commission.
   https://www.sec.gov/Archives/edgar/data/1100663/000119312516665780/d220015d497.htm (closure passages read)
8. iShares Trust. (2025, June 13). [Supplement announcing the liquidation of eight iShares funds, CCRV, IVEG, ELQD,
   FOVL, IDAT, HYGI, AGIH and IWTR; Form 497]. U.S. Securities and Exchange Commission.
   https://www.sec.gov/Archives/edgar/data/1100663/000119312525140815/d92035d497.htm
9. iShares Trust. (2026e, June 12). [Supplement announcing the liquidation of the iShares funds AGRH and IVRS; Form
    497]. U.S. Securities and Exchange Commission.
    https://www.sec.gov/Archives/edgar/data/1100663/000119312526269593/d74967d497.htm
10. iShares Trust. (2026f, July 7). *Form 8-A: Registration of certain classes of securities pursuant to Section 12(b)
    or (g) of the Securities Exchange Act of 1934*. U.S. Securities and Exchange Commission.
    https://www.sec.gov/Archives/edgar/data/1100663/000119312526297007/d91865d8a12b.htm
11. Investment Company Act of 1940, 15 U.S.C. § 80a-22 (2024). Legal Information Institute.
    https://www.law.cornell.edu/uscode/text/15/80a-22
12. Mergers of affiliated companies, 17 C.F.R. § 270.17a-8 (2026). Legal Information Institute.
    https://www.law.cornell.edu/cfr/text/17/270.17a-8
13. U.S. Securities and Exchange Commission. (n.d.). *EDGAR full text search* [Database]. Retrieved November 13, 2026,
    from https://efts.sec.gov/LATEST/search-index?q=%22close%20and%20liquidate%22%20%22iBonds%22&ciks=0001100663&forms=497
14. U.S. Securities and Exchange Commission, Office of Investor Education and Advocacy. (2021, December 17). *Investor
    bulletin: Fund liquidation*. Investor.gov.
    https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/investor-bulletin-fund-liquidation
