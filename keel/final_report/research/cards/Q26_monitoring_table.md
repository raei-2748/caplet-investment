# Q26 research cards: what to monitor as 2031 and 2033 approach (Table 3)

**Date.** Tue 10 Nov 2026 (Sydney), Mon 9 and Tue 10 Nov in the US. Web sources were read at the source that day
(Parallel web_search and web_fetch; TreasuryDirect's securities web service); "accessed 10 Nov 2026" below means that
day. Report part 3e (assumptions, limits and what to watch) and Table 3; one wording note for 3c.

**Notes for the Final Report store, not report prose.** The IPS, the Trading Notes and the WInS book are frozen: a clash
is a risk to record, never a change. Every figure about the plan is quoted from `../../NUMBERS.md` with its section;
Keel figures are MODEL. Keel arithmetic on public data is marked "Keel arithmetic". This card builds on Q15 (13-row
monitoring table, debt-limit history, pension and escrow triggers), Q16 (iBond fund endings) and Q24 (liquidity); it
does not redo them.

**Claims tested.**
1. "Mining TARPs (trigger action response plans) and pension or insurer pre-agreed triggers are the prior art for
   'watch many things, change the plan for only two'. Each fixes signal, threshold and response, including 'no
   action'." Keep, kill or change: what Table 3 should borrow and what not.
2. "Every signal in Table 3 can be read from one public source on a known date, with a threshold." Keep, kill or
   change.
3. "Nothing besides a missed deposit or a Treasury default can change the plan" (IPS l.17; CANON A34). Keep, kill or
   change, after trying to break it with the iBond prospectus and SAI, the T-bonds' call status and VT.

**Problem class.** A pre-agreed watch list for a hold-to-maturity liability match: many signals, a fixed set of
responses, and most responses are "continue as planned". Solved in mine safety by TARPs (NSW and WA regulators) and in
pension schemes by pre-agreed collateral and trigger governance (UK Pensions Regulator, 2023, after the 2022 LDI crisis).
Fund-level events are settled by fund law (iShares prospectus and SAI; SEC Rule 6c-11) and custody law (SIPC).

## Verdicts in one screen

- **Claim 1: KEEP, with a change.** Four sources read at the source (two NSW regulator guides, the WA code of practice,
  the UK Pensions Regulator's LDI guidance) fix the same shape: signal, how often, trigger, planned response, who acts,
  and a "normal" level whose response is to carry on. Table 3 borrows five things: the columns; a Normal level that says
  "continue as planned"; a named reader ("Laura or her asset management team", Wharton's own words); a distance to each
  trigger (NUMBERS 5: the ladder survives a 98.4% smaller deposit, the escrow standard 74.5%); and a yearly status line
  ("triggers reached since last report"). It refuses four: escalating actions on a worsening trend, regular revision of
  the triggers, leverage buffers, and numeric triggers for the two reasons (they are events, not levels).
- **Claim 2: CHANGE.** Table 3 below has **33 rows**. 27 have one public source read or already verified, with a known
  publication time. 4 rest on Laura's own records (the 2028 deposit twice, co-sponsor commitments, the builder's
  contingency); 2 rest on sources not yet known or read (which Treasury-bill ETF; fund shareholder reports). 28 rows
  carry a threshold; 4 carry "none, by design" (VT before and after the move, rating actions, buybacks), which is the
  IPS's own point; 1 cannot happen (a call on a T-bond). Two thresholds come ready-made from law or prospectus: Rule 6c-11's "greater than 2% for more than
  seven consecutive trading days" and the iBond funds' "on or about December 15".
- **Claim 3: KEEP for the plan; CHANGE for the instruments.** No event found changes the plan's shape. Seven events change
  an instrument, a date or where assets sit, and each needs a pre-written step that stays inside the plan:
  a fund ended early by its Board; a fund extended past 31 Dec; a trading halt or redemption suspension; a fund paying
  below its holdings; a money market fund inside the fund; VT changing its index or closing; and holdings above SIPC's
  $500,000 at one broker (about $589,000 near Dec 2032, Keel arithmetic on NUMBERS 4 and 8h). The five T-bonds are not
  callable (TreasuryDirect: "callable":"No" for all five). One residual is not either reason and has no cap in the
  prospectus: a fund paying more than 0.5% below its holdings (securities lending loss, litigation or extraordinary
  costs). It is a C9 residual, not a third reason; record it as a risk.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A TARP is a planned response that a monitored trigger sets off; the actions are written before they are needed | NSW Resources Regulator, Guide: Managing risks of subsidence, s.2.6.2 | TWOREASONS, PROCESS, PRESENTATION | NICHE | Table 3 is Laura's TARP: what is watched, what sets anything off, what is done | Mining TARPs manage slow physical hazards with escalating actions; Laura's two reasons are events | VERIFIED (guide s.2.6.2, s.2.9.2, Appendix B read) | no | NSW subsidence guide |
| 2 | Five TARP design factors: simplicity, clear linkage, clear accountability, communication, escalation | NSW subsidence guide s.2.6.2; WA MIAC (2022) code s.2.5.1 | PROCESS, PRESENTATION | NICHE | Keep the first four; one named reader per row | Escalation does not fit: the plan has no middle actions between "continue" and the two reasons | VERIFIED (both read) | risk: an escalation ladder would add triggers (CANON A34: "never add a rule or trigger") | NSW subsidence guide; WA code |
| 3 | The lowest TARP level is Normal: routine monitoring and "continue mining as per ATM" | NSW TRG Gas outbursts (2023), s.7.6 and Appendix B (Normal green; Level 1 yellow "Increased awareness"; Level 2 orange; Level 3 red) | TWOREASONS, PRESENTATION | NICHE | Most of Table 3 sits at Normal: watch, carry on | Coloured levels may read as alarm in a client report | VERIFIED (TRG s.7.6 and Appendix B read) | no | NSW gas outburst TRG |
| 4 | TARPs exist to stop "normalisation": slow drift accepted because each day looks like the last | WA MIAC (2022) code s.2.5.1 | INFLATION_TWD, HALFKEPT | NICHE | The slow signals for Laura are Taiwan costs and the Taiwan dollar; a five-year pace, not one month | The drift does not touch the ten payments; it only draws on the half kept | VERIFIED (code s.2.5.1 read) | no | WA code |
| 5 | A TARP status report lists each monitored item, date, frequency, triggers reached since the last report and actions taken | NSW subsidence guide, Appendix B | PROCESS, PRESENTATION | NICHE | One yearly status line for Laura's team: "triggers reached since last report: none" | A yearly report is a habit, not a promise; keep it out of the frozen strategy | VERIFIED (Appendix B read) | no | NSW subsidence guide |
| 6 | TARP triggers are set from "detailed knowledge of what is normal" and "regularly reviewed and revised" | NSW TRG Gas outbursts s.7.6 | TWOREASONS | NICHE | Borrow the first half: thresholds come from NUMBERS, not taste | Do not borrow revision: the IPS fixes the two reasons | VERIFIED | risk: "revise the triggers" would contradict IPS l.17 | NSW gas outburst TRG |
| 7 | Pension LDI guidance: pre-agree the thresholds for cash calls, record the process, name who may sell and under which circumstances, and set a waterfall of assets | The Pensions Regulator (2023), Using leveraged LDI | TWOREASONS, COMPLETE2028, HALFKEPT, PROCESS | KNOWN | Laura already has two waterfalls: the 2028 deposit's order (ladder, backstop, floor, VT) and the half kept's three named uses | Laura has no leverage, so nothing ever forces a sale | VERIFIED (guidance read in full) | no | TPR LDI guidance |
| 8 | Test "the size of market movement required before a specific event would happen" | TPR (2023), testing item 2 | COMPLETE2028, CERTAINTY | KNOWN | Distance to trigger: the ladder survives a 98.4% smaller deposit, the escrow standard 74.5%; a 3.60-point fall takes the whole $150,000 (NUMBERS 5) | None | VERIFIED | no | TPR LDI guidance; NUMBERS 5 |
| 9 | A leveraged scheme holds a 250bp stress buffer and refills it within five days | TPR (2023) | OTHER | KNOWN | Disanalogy only: Laura's book has no margin calls | Do not borrow: a buffer rule would be a new rule | VERIFIED | no | TPR LDI guidance |
| 10 | Ask for information outside the normal reporting cycle "if certain triggers are met" | TPR (2023) | PROCESS | KNOWN | The "Look closer" level: read more often, change nothing | None | VERIFIED | no | TPR LDI guidance |
| 11 | IBTM's end was approved by the Board, needs no shareholder vote, and "The Board may extend the termination date" | iShares IBTM summary prospectus (27 Feb 2026); iShares Trust prospectus (27 Feb 2026) | LADDER, FLOOR, RESERVE2033 | KNOWN | A rung's cash could arrive after 1 Jan; the step is to sell shares on the exchange before the payment date | Q16 found four of four Treasury iBond endings on time | VERIFIED (both read) | risk: the IPS says the funds "pay what they say" (CANON C2, D5) | IBTM summary prospectus |
| 12 | The Board may end a fund early; "in certain circumstances described in the Declaration of Trust, only a majority vote of the Board is required" | iShares SAI (27 Feb 2026, supplemented 11 Sep 2026) | LADDER, FLOOR | NICHE | Early cash at NAV; the step is to buy a Treasury maturing before the same payment | Keel inference: the NAV is the market value of the same Treasuries, so it buys back about the same cash flows, less costs | VERIFIED (SAI termination and redemption sections read) | no | iShares SAI |
| 13 | "Declining Yield Risk": in the final months the fund's yield "may move toward prevailing money market rates" | IBTM summary prospectus; IBTR 497K (25 Mar 2026) | LADDER, REINVEST, FLOOR | KNOWN | Same effect NUMBERS 3 already sizes: up to 1.6-2.1% of a rung if final cash earns nothing | Already inside the escrow standard ("sufficient without reinvestment", NUMBERS 2) | VERIFIED | no | IBTM summary prospectus; IBTR 497K |
| 14 | A fund can pay less than its holdings while doing what its prospectus says: costs outside the 0.07% fee (interest, taxes, transaction costs, "litigation expenses and any extraordinary expenses"), securities lending losses, liquidation costs | IBTM summary prospectus (fees section; Securities Lending Risk); iShares Trust supplement 15 Oct 2026 ("final net asset value ... will include any costs associated with the liquidation") | LADDER, FLOOR, CERTAINTY | NICHE | Confirms NUMBERS 3's UNVERIFIED line: the 0.5% haircut, not the prospectus, carries the fund risk | The prospectus sets no cap on a lending loss or extraordinary cost | VERIFIED (all three read) | risk: SKELETON 3c's "a fund failing to work as its prospectus says" is too narrow (see (c)) | IBTM summary prospectus; IBTG supplement |
| 15 | A fund may lend up to one-third of its assets; collateral sits in a money market fund; a non-government money market fund can charge "a discretionary liquidity fee of up to 2%" | IBTM summary prospectus; iShares SAI | LADDER, FLOOR | NICHE | Check that the money market fund in each holdings file is a Treasury fund | IBTG and IBTR hold "BLK CSH FND TREASURY SL AGENCY", a Treasury fund; IBTM's own file not checked for it | VERIFIED (prospectus, SAI; IBTR fact sheet holdings) | no | iShares SAI; IBTR page |
| 16 | Redemptions can be suspended and trading halted ("including through a trading halt") | IBTM summary prospectus (Market Trading Risk); iShares SAI; Vanguard VT prospectus (Trading Halt) | LADDER, FLOOR, MOVE2031 | KNOWN | Matters only on a day Laura must trade: Jan 2028, the 2031 move, an extension sale | The ten payments do not need a trade if the funds end on time | VERIFIED | no | IBTM summary prospectus; SAI; VT prospectus |
| 17 | The Dec 2026 fund (IBTG) is ending on schedule: notice 15 Oct 2026, last trade 15 Dec, proceeds 18 Dec | iShares Trust supplement (15 Oct 2026); BlackRock release on Business Wire (15 Oct 2026) | LADDER, RESERVE2033 | NICHE | Four Treasury iBond endings in a row now match the pattern Q16 found (2023, 2024, 2025, 2026) | Four is a short record; all in calm years | VERIFIED (both read) | no | IBTG supplement; BlackRock release |
| 18 | None of the five T-bonds can be called | TreasuryDirect securities web service: "callable":"No", no call date, for 912810PT9, 912810PX0, 912810QD3, 912810QL5, 912810QT8 | LADDER, CERTAINTY | KNOWN | Closes the question: a T-bond rung cannot be paid early | None | VERIFIED (all five records read) | no | TreasuryDirect web service |
| 19 | Treasury last called a bond in 2009 (the 11-3/4% of 2009-14, issued 1984); 88 callable Treasuries were issued from 1917 to 1984 | TreasuryDirect release (15 Jul 2009); TBAC charge Q2 2024 | LADDER | NICHE | History says calls ended with 1984 issues; Laura's bonds were issued 2007-2011 | None | VERIFIED (release read; TBAC charge read for the count) | no | TreasuryDirect 2009; TBAC |
| 20 | Treasury buybacks are offers, not calls; a holder may ignore them | TreasuryDirect marketable securities FAQ | LADDER | KNOWN | A row with "no action ever" | Buyback schedule not read | UNVERIFIED (FAQ excerpt only) | no | TreasuryDirect FAQ |
| 21 | Rule 6c-11 makes every ETF post holdings, NAV, price and premium or discount each business day, and a statement if the premium or discount is "greater than 2% for more than seven consecutive trading days" | 17 C.F.R. 270.6c-11(c)(1) | LADDER, FLOOR, MOVE2031, PRESENTATION | NICHE | A ready-made public threshold for the "Look closer" level | The flag matters only on days Laura trades; the fund's ending pays NAV | VERIFIED (rule text read) | no | eCFR |
| 22 | SIPC covers up to $500,000 per customer per capacity, including $250,000 cash; it protects custody, not value | SIPC, What SIPC protects; SIPC brochure (2026) | RESERVE2033, OTHER | KNOWN | Near Dec 2032 Laura holds about $589,000 (Keel arithmetic: reserve $444,545, NUMBERS 8h; funds pay $123,476 and half kept $21,347, NUMBERS 4) | Customer securities at a broker are also kept apart by SEC rules (not read); SIPC is the backstop, not the only protection | VERIFIED (page and brochure read) | risk: not in the IPS; an implementation note only | SIPC |
| 23 | Debt-limit headroom was $749,285m on 6 Nov 2026 (limit $41,103,996m less debt subject to limit $40,354,711m) | Daily Treasury Statement, 6 Nov 2026, Table IIIC | TWOREASONS, LADDER, COMPLETE2028 | KNOWN | At the Aug-Nov pace (about $6bn a day) the limit binds about early March 2027; an X-date in mid-2027 falls between the two deposits | Keel arithmetic, not a forecast; fits BPC's "late winter to mid-summer of 2027" (Q15) | VERIFIED (DTS read, 18 Aug and 6 Oct also read) | no | DTS |
| 24 | The par curve is built from quotes taken "at or near 3:30 PM" and is posted "by 6:00 PM Eastern Time each trading day" | Treasury, Yield curve methodology (18 Feb 2025) | LADDER, COMPLETE2028, FLOOR | KNOWN | The known time for rows on yields | Q15 row 31 says the curve is published about 3:30 pm; that is when quotes are taken | VERIFIED (page read in full) | no | Treasury methodology page |
| 25 | The central bank of Taiwan posts one NT$/US$ closing rate each Taipei business day (32.768 on 6 Nov 2026) | CBC, NT$/US$ closing rate | INFLATION_TWD, HALFKEPT | KNOWN | Matches NUMBERS 8d's input; the 27.52 ten-year strongest is the threshold | The rate moves what the gift buys, never the dollars | VERIFIED (data page read) | no | CBC page |
| 26 | VT's Board may change its index "for any other reason determined in good faith by the Board"; the substitute "would represent the same market segment"; the objective "is not fundamental" | Vanguard (2026), VT prospectus | HALFKEPT, MOVE2031 | KNOWN | An index change is an instrument event; the half kept stays world shares | The IPS names VT, so a closure means holding a like fund under another name | VERIFIED (prospectus sections on objective, index, risks and trading read) | risk: IPS l.15 names the fund | VT prospectus |
| 27 | Wharton names who watches: "Laura or her asset management team" | Wharton Final Report instructions (WHARTON_NORTH_STAR s.0) | PRESENTATION, LAURA | TEXTBOOK | The accountability column TARPs require is given by the brief | None | VERIFIED (filed text) | no | WHARTON_NORTH_STAR |
| 28 | Three levels for Laura: Watch (carry on), Look closer (a prepared step inside the plan), Reason (one of the two) | Keel design from rows 1-10 | TWOREASONS, PRESENTATION | NICHE | Lets Table 3 hold 33 signals and still show only two reasons | The middle level must never read as a third reason | n/a (design) | risk: A34; every Look-closer step must stay inside the plan | This card |
| 29 | SKELETON 3c says nothing after the move can break the range "except a default or a fund failing to work as its prospectus says"; a fund working as its prospectus says can still pay below its holdings | IBTM summary prospectus; NUMBERS 3, 4 | CERTAINTY, FLOOR, MOVE2031 | NICHE | Word the exception as "a fund paying more than 0.5% below its holdings", which is what the rule tests | None | VERIFIED | risk: SKELETON wording, not the frozen texts | This card |
| 30 | Q15's monitoring table quotes figures NUMBERS 6 now lists as void ($138,735 top; $23,986 half kept; $110,000 bottom; $21,149 margin; "about $24,500" completion) | Q15 card; NUMBERS 4, 6 | PRESENTATION | n/a | Table 3 here uses only current figures | None | VERIFIED (both files read) | clash: Q15 against NUMBERS 6 | Q15; NUMBERS |
| 31 | Co-sponsor commitments and the builder's contingency have no public source | Case (facility costs out of scope); CANON A31 | COSPONSOR, HALFKEPT | n/a | Laura's own records; they draw on the half kept only | A row without a public source breaks claim 2 as stated | n/a | no | This card |
| 32 | The IPS does not say when a late 2028 deposit becomes a missed one | FINAL IPS l.17; CANON A34, D9 | TWOREASONS, COMPLETE2028 | n/a | The first reason needs a date to be read | A date chosen now would read as a new rule | n/a | risk: the date is an interpretation; the lead decides | This card |

## (b) Cards

**Card 1. A TARP for a bond ladder (rows 1-10, 27, 28).**
- What is it? Mine regulators require trigger action response plans: a table of what is monitored, how often, what
  level sets anything off, what is then done and by whom. The lowest level says carry on.
- Did it work? The WA code says TARPs prevent "normalisation" and delay. The UK Pensions Regulator asked LDI schemes for
  the same pre-agreement after the 2022 gilt crisis. Both are regulators' requirements, not outcome studies.
- Like Laura? Many signals, few actions, all written before they are needed. Wharton's "Laura or her asset management
  team" supplies the "who".
- Not like Laura? Mines escalate actions as a hazard grows; pension schemes refill buffers. Laura's plan has no middle
  action and no leverage. Her two reasons are events, not levels.
- What Caplet takes: 3e, Table 3. Columns from row 5 and TPR; three levels (Watch, Look closer, Reason); a distance to
  trigger in the deposit rows (NUMBERS 5: 98.4% ladder, 74.5% escrow standard, 3.60 points).

**Card 2. Fund endings change dates, not the plan (rows 11, 12, 16, 17).**
- What is it? Each iBond fund ends "on or about December 15" of its year. Its Board may extend that date; in some cases
  the Board alone may end it early (SAI).
- Did it work? Four Treasury iBond endings in a row went to plan: notices in mid-October, proceeds 18-22 Dec
  (Q16 for 2023-2025; IBTG supplement and release for 2026).
- Like Laura? Five of her ten rungs and the floor are these funds.
- Not like Laura? A T-bond cannot be extended or ended early (row 18); the funds can.
- What Caplet takes: 3e, Table 3 rows T17-T20 below; 2 (implementation) may note the step. Early end: buy a Treasury
  maturing before the same payment. Extension past 31 Dec: sell shares on the exchange before the payment.

**Card 3. The 0.5% haircut, not the prospectus, carries the fund risk (rows 13-15, 29).**
- What is it? The IBTM prospectus leaves outside its 0.07% fee "interest expenses", "taxes", trading costs and
  "litigation expenses and any extraordinary expenses". It may lend up to a third of its assets. Its final NAV includes
  liquidation costs (IBTG supplement).
- Did it work? This answers NUMBERS 9's open check. NUMBERS 3 was right to say a fund can pay slightly less than its
  holdings without breaking its prospectus. The prospectus gives no cap.
- Like Laura? The range rule cuts each end 0.5% for this; up to 0.5% is covered everywhere, 0.75% breaks an end in
  about 1 house path in 17 (NUMBERS 4). For the ten, the escrow standard has $1,414 to spare at 0% (NUMBERS 2).
- Not like Laura? A T-bond has none of these costs.
- What Caplet takes: 3c's exception reads "a fund paying more than 0.5% below its holdings", not "a fund failing to work
  as its prospectus says". 3e names the residual (CANON C9) with its trigger (T21).

**Card 4. The debt limit binds in 2027, between the two deposits (rows 23, 24).**
- What is it? Headroom under the limit was $749,285m on 6 Nov 2026 (DTS Table IIIC). At the August to November pace the
  limit binds about early March 2027 (Keel arithmetic), then extraordinary measures buy months.
- Did it work? Q15 records 13 impasses and no missed payment; a late payment is the only event that is reason 2.
- Like Laura? Her ladder is bought in Jan 2027 and completed in Jan 2028. An X-date in mid-2027 sits between them. None
  of her holdings matures in 2027; coupons fall due 15 Feb, 15 May, 15 Aug and 15 Nov.
- Not like Laura? A delayed coupon in 2027 is small next to the ladder; the 2028 completion's price is what moves.
- What Caplet takes: Table 3 rows T7-T10; the definition of reason 2 as a payment on a held security not made on its
  due date (lead decides the words).

**Card 5. Custody above SIPC's limit (row 22).**
- What is it? SIPC covers $500,000 per customer per capacity, $250,000 of it cash, and only the custody function.
- Did it work? SIPC is a backstop to broker failure; it never covers a fall in value.
- Like Laura? Her holdings near Dec 2032 are about $589,000 (Keel arithmetic on NUMBERS 4 and 8h).
- Not like Laura? Treasuries held for a customer are kept apart from the broker's own assets by SEC rules (not read
  here), so SIPC is the last line, not the first.
- What Caplet takes: one implementation line in Section 2 or 3e if the lead wants it (two brokers, or a broker with
  cover above SIPC). It changes where assets sit, never what is held.

**Card 6. Ready-made public thresholds (rows 21, 25 and NUMBERS 5, 8d).**
- What is it? Some thresholds need no Keel judgement: Rule 6c-11's 2% for seven trading days; the funds' "on or about
  December 15"; the Taiwan dollar's ten-year strongest, 27.52 (NUMBERS 8d); the deposit sizes in NUMBERS 5.
- Did it work? Each is published by a regulator, a fund or the register.
- Like Laura? Each row can be read on a known date from one page.
- Not like Laura? Co-sponsors and the builder have no public page.
- What Caplet takes: the threshold column of Table 3.

## (c) Verdicts

**Claim 1: KEEP, with a change.**
- Read at the source: the NSW subsidence guide (s.2.6.2 definition; five factors; s.2.9.2 review triggers; Appendix B
  status report), the NSW gas outburst TRG (s.7.6; Appendix B levels and roles), the WA code (s.2.5.1, normalisation),
  the TPR LDI guidance (thresholds, process, who may sell, waterfall, testing the move needed to reach an event,
  information outside the cycle, testing yearly or triennially). Q15 already holds the pension trigger documents
  (Pennon, Hendy) and TPR integrated risk management.
- Borrow: (1) columns: signal, source and frequency, threshold, response, who; (2) a Normal level whose response is
  "continue as planned" (TRG: "continue mining as per ATM"); (3) a named reader per row; (4) distance to trigger;
  (5) a yearly status line, "triggers reached since last report".
- Do not borrow: (1) escalating actions as conditions worsen; (2) "regularly reviewed and revised" triggers; (3) leverage
  buffers and refill rules; (4) numeric triggers for the two reasons.
- Change from the claim: the prior art fixes the shape, not the content. Laura's middle level is "Look closer": read more
  often, take a prepared step that stays inside the plan. It never changes the plan.

**Claim 2: CHANGE.**
- 33 rows. 27 have one public source and a known time. 4 rest on Laura's records (T4, T5, T31, T32). 2 rest on sources
  not yet known or read (T6 Treasury-bill ETF; T21 shareholder reports).
- 28 rows have a threshold. 4 say "none, by design" (T11, T13, T25, T26): A34 says a market fall is not a reason, so a
  price threshold on VT would be a new trigger. 1 cannot happen (T12: no T-bond rung is callable).
- Sources checked for what they publish: Treasury par curve (quotes at or near 3:30 pm, posted by 6:00 pm ET each
  trading day); DTS Table IIIC (each business day); iShares fund pages (daily, by Rule 6c-11); prospectus supplements
  (event; mid-October in the funds' final year); TreasuryDirect securities data (callable flag); CBC closing rate (each
  Taipei business day); DGBAS price release (monthly; Oct 2026 release dated 5 Nov, REFERENCES #44); SIPC (fixed
  limits); VT prospectus (event).
- So the claim should read: "every public signal has one source and a known date; the private ones are Laura's own
  records, and a market price never has a threshold".

**Claim 3: KEEP for the plan; CHANGE for the instruments.**
- iBond prospectus and SAI, exact words:
  - "The Fund is a term fund that will terminate on or about December 15, 2032, at which time it will distribute its
    remaining net assets to shareholders pursuant to a plan of liquidation. The Fund does not seek to return any
    predetermined amount at maturity or in periodic distributions." (IBTM summary prospectus, 27 Feb 2026)
  - "The Fund's termination was approved by a majority of the Trust's Board of Trustees (the "Board") and does not
    require additional approval by Fund shareholders. The Board may extend the termination date if a majority of the
    Board determines the extension to be in the best interest of the Fund." (same) Event: extension. Instrument change.
  - "The Trust or a fund may be terminated by a majority vote of the Board, subject to the affirmative vote of a majority
    of the shareholders ...; however, in certain circumstances described in the Declaration of Trust, only a majority
    vote of the Board is required." (SAI) Event: early end. Instrument change.
  - "In the last six months of operation, as the bonds held by the Fund mature, the proceeds will typically be reinvested
    by the Fund in investments already in the Underlying Index but may also be invested in other cash and cash
    equivalents as determined by BFA." and "By December 15, 2032, the Fund is expected to consist almost entirely of
    cash." (IBTM) Event: final-month cash. Already sized (NUMBERS 3). No change.
  - "Securities lending involves the risk that the Fund may lose money because the borrower of the loaned securities
    fails to return the securities in a timely manner or at all." (IBTM) Event: payout below holdings. Residual (C9).
  - "Each Fund's final net asset value, as calculated on December 15, 2026, will include any costs associated with the
    liquidation" (IBTG supplement, 15 Oct 2026). Event: payout below holdings. Inside the 0.5% haircut when small.
  - "the potential lack of an active market for Fund shares (including through a trading halt)" (IBTM, Market Trading
    Risk). Event: halt. Date change only.
- T-bonds: none callable (five of five). Buybacks are voluntary.
- VT: "The Fund's investment objective is not fundamental and may be changed without shareholder approval." The Fund
  may substitute an index "for any other reason determined in good faith by the Board. In any such instance, the
  substitute index would represent the same market segment as the Target index." Event: instrument change. The IPS
  names VT (risk, not a change).
- Result: the plan's two reasons stand. No event found changes the order of the deposit, the ladder, the floor, the move
  or the reserve. Seven events change an instrument, a date or custody. One residual (a fund paying more than 0.5% below
  its holdings) can leave an end or a payment short without being either reason. It is named and sized as far as the
  register allows, and never turned into a third reason.

**Table 3 (notes).** Levels: Watch = carry on as planned; Look closer = read more often and take a prepared step that
stays inside the plan; Reason = one of the IPS's two. "Team" = Laura's asset management team. The last column checks each
row against CANON A34 (only a missed deposit or a Treasury default changes the plan; a smaller deposit is not a reason,
D9).

| # | Level | Signal | Source and frequency | Threshold | What it changes (who acts) | What it never changes | Check against the two reasons (A34) |
|---|---|---|---|---|---|---|---|
| T1 | Watch | The plan's own dates | FINAL IPS; NUMBERS 1, 4; fund prospectuses. Dates: 1 Jan 2027; Jan 2028; the move before the 2031 meetings; about 15 Dec 2032-2036; 15 Feb 2037; 15 May 2038; 15 Nov 2039-2041 | A date reached | The steps the IPS already orders; one yearly status line (team) | The steps themselves | Neither; the plan itself |
| T2 | Watch | Treasury yields before the 1 Jan 2027 purchase | Treasury par yield curve (REFERENCES #112): quotes at or near 3:30 pm ET, posted by 6:00 pm ET, each trading day | A fall of more than 0.5 points: cost $317,742 (about an 8% chance, MODEL); 1 point $334,092 (NUMBERS 1) | How much of the 2028 deposit the completion takes (team) | That the ten are bought first, in Jan 2027 | Neither; a price |
| T3 | Watch | Yields during 2027 to the Jan 2028 completion | Same; monthly in 2027, daily in Jan 2028 | Completion $38,282 at 6 Nov forwards; $41,630 after a 1-point fall in 2027 (NUMBERS 5) | Floor money, so the stated bottom, fixed on the purchase day (NUMBERS 4) (team) | The order: ladder, backstop, "most" to the floor, then VT | Neither; a price |
| T4 | Look closer | The size of the 2028 deposit | Laura's records; confirm in Dec 2027 | Below $38,282 the escrow standard is incomplete (a 74.5% fall); below $2,388 the ladder is (98.4%), at 6 Nov yields (NUMBERS 5) | Floor and VT shrink: $112,500 gives a bottom of $65,000, $75,000 gives $40,000, $37,500 gives $0 (NUMBERS 5) (Laura, team) | The order; the ten unless the fall passes the thresholds | Neither; a smaller deposit is not a reason (D9) |
| T5 | Reason | The 2028 deposit does not arrive | Laura's records | Missed (cut-off date not set by the IPS; lead decides) | The plan may change. Measured: $2,287 of the ladder unbought; 2033 payment $3,016 short at forwards; the ten $57,455 short at 0%; no backstop, floor or VT (NUMBERS 5) (Laura) | n/a | IS reason 1 |
| T6 | Watch | The Treasury-bill ETF holding waiting money | That ETF's fund page and prospectus; which ETF is UNVERIFIED (NUMBERS 9) | Fee above 0.15% a year, the cushion's design fee (NUMBERS 0, 2) | The $1,414 spare at 0% (NUMBERS 2) (team) | The ten | Neither |
| T7 | Watch | Debt-limit headroom | Daily Treasury Statement Table IIIC, fiscaldata.treasury.gov, each business day | $749,285m on 6 Nov 2026 (Keel arithmetic); look closer when Treasury starts extraordinary measures | Nothing in the plan; the price of the Jan 2028 completion may move (team) | A payment | Neither; a limit is not a default |
| T8 | Look closer | X-date projections | BPC and CBO (Q15); monthly once measures start | Treasury names a date in a letter to Congress | Team lists holdings and coupons due near that date | A payment | Neither |
| T9 | Look closer | Bill-curve kink at the X-date | Treasury daily bill rates (same page as #112) | A bill maturing just after the X-date yields clearly more than its neighbours (GAO's sign of concern, Q15) | Nothing; tells the team to expect a possible delay | A payment | Neither |
| T10 | Reason | A Treasury payment due to Laura or to one of her funds not made on its due date | Treasury and TreasuryDirect notices; TMPG and SIFMA notices; fund notices; broker statement on each coupon date | One business day late on a security she or her funds hold (Keel's proposed reading of "a Treasury default"; lead decides) | The plan may change (Laura, team) | A market fall; a downgrade | IS reason 2 |
| T11 | Watch | Credit rating actions on the US | Moody's, S&P, Fitch; event | None, by design | Nothing in the plan | Any payment: a downgrade is not a default | Neither |
| T12 | Watch | A call on a T-bond rung | TreasuryDirect securities data: "callable":"No" for all five | None possible | Nothing | Coupons and face of the five bonds | Neither; cannot happen |
| T13 | Watch | Treasury buyback offers | Treasury buyback schedule; event | None, by design: offers are voluntary | Nothing; Laura need not sell | The bond | Neither |
| T14 | Watch | Coupons credited on the T-bonds | Broker statement: 15 Feb and 15 Aug (Feb 2037 bond); 15 May and 15 Nov (the other four) | Not credited by the next business day: go to T10 | Coupons wait in the Treasury-bill ETF (team) | The ten: the backstop is sized at 0% (NUMBERS 2) | Neither, unless T10 |
| T15 | Watch | Each iBond fund's NAV, holdings and cash share | iShares fund pages, each business day (Rule 6c-11) | A rising cash share in the final six months is expected | A rung's payout by up to 1.6-2.1% if final cash earns nothing (NUMBERS 3) | The payment: the escrow standard needs no interest (NUMBERS 2) | Neither; A34 lists NAV gaps as no reason |
| T16 | Look closer | Premium or discount to NAV | iShares and Vanguard fund pages, each business day (Rule 6c-11) | More than 2% for more than seven trading days in a row | The price on a day Laura trades: Jan 2028 floor purchase, the 2031 move (team) | What a fund pays at its end (NAV) | Neither |
| T17 | Watch | The ending notice for that year's fund | Prospectus supplement (Form 497) and BlackRock release; mid-October of the final year (16 Oct 2023, 17 Oct 2024, 15 Oct 2025, 15 Oct 2026) | No notice by 31 Oct of the final year: look closer | Nothing if on time: last trade about 15 Dec, cash 18-22 Dec | The rung's money | Neither |
| T18 | Look closer | The Board extends a fund past 31 Dec | Same | A notice naming a date after 31 Dec of the final year | Sell the shares on the exchange before the payment (team): an instrument step | The plan; the Treasuries the fund holds | Neither; a date |
| T19 | Look closer | The Board ends a fund early | Same; the SAI allows a Board-only vote in some cases | A notice naming a date before the final year | Put the cash into a Treasury maturing before the same payment (team): an instrument step | The plan | Neither; a date |
| T20 | Look closer | A fund's cash not received | Broker statement | Not credited by 28 Dec (four past endings paid 18-22 Dec) | Team takes it up with the broker | The plan | Neither |
| T21 | Look closer | A fund paying below its holdings (lending loss, litigation or extraordinary costs, liquidation costs) | Fund annual and semi-annual reports (not read); final NAV against the holdings file | NAV more than 0.5% below the holdings' value | Range ends: covered up to 0.5%; 0.75% breaks an end in about 1 house path in 17 (NUMBERS 4). The ten: $1,414 spare at 0% (NUMBERS 2) | The plan | Neither; a C9 residual, no cap in the prospectus (risk) |
| T22 | Look closer | The money market fund inside each iBond fund | Daily holdings file | A non-government money market fund appears (SAI: liquidity fee up to 2% possible) | Nothing if a Treasury fund (IBTG and IBTR hold one) | The plan | Neither |
| T23 | Look closer | Trading halt or redemption suspension | Exchange halt notices; fund pages; event | A halt on a day Laura must trade | The trade day moves (team) | The plan | Neither |
| T24 | Watch | Fund fee | Prospectus supplement; event | Any rise above IBTM's 0.07% | A payout by the fee; inside the 0.5% haircut | The plan | Neither |
| T25 | Watch | VT before the move | NYSE Arca price; Vanguard daily NAV | None, by design ("A fall in the market is not one of them") | The top Laura can state: central $115,000; house 1-in-20 $95,000 and $140,000 (NUMBERS 4) | The bottom; any payment | Neither |
| T26 | Watch | VT after the move | Same | None, by design | The half kept only: central $21,347; house $9,881 / $20,739 / $41,258 (NUMBERS 4) | The stated range, both ends owned | Neither |
| T27 | Look closer | VT changes its index or objective, or closes | Vanguard prospectus supplement; event | Any notice | Hold a fund on the same world-shares market (team): an instrument step | Payments; the half kept's three uses | Neither; the IPS names VT (risk) |
| T28 | Watch | The move date | Laura's meeting calendar | Meetings set: the move comes before them (IPS) | Which top she can state; nothing is stated before the move (a top stated 1-12 months early is not yet owned in 2.9%-10.7% of house paths, NUMBERS 4) | The bottom | Neither |
| T29 | Watch | US dollar against the Taiwan dollar | CBC NT$/US$ closing rate, each Taipei business day (32.768 on 6 Nov 2026) | 27.52, the ten-year strongest: $18,116-$21,930 more for the same NT$ budget (NUMBERS 8d) | Calls on the half kept, a named use (A31) (Laura) | The US$ payments; the range in dollars | Neither |
| T30 | Watch | Taiwan construction costs and CPI | DGBAS monthly price release (Oct 2026 release dated 5 Nov, #44); construction cost index (#40) | A five-year pace above 5.0% a year, the top of NUMBERS 8d's band (central 3.0%; one-year +7.29% in Sep 2026) | What the range buys: NT$2.59m-3.14m at 3% cost growth (NUMBERS 8d); calls on the half kept (Laura) | The dollar range; the payments | Neither |
| T31 | Look closer | Co-sponsor commitments | Laura's records; no public source | A co-sponsor cuts or withdraws | Calls on the half kept, a named use (A31) (Laura) | The range she stated; the payments | Neither |
| T32 | Look closer | The builder's contingency | Laura's and the builder's records; no public source; costs out of scope | An overrun beyond the builder's own contingency | Calls on the half kept, a named use (A31) (Laura) | The range she stated; the payments | Neither |
| T33 | Watch | Custody at one broker | SIPC limits (fixed); broker statements | Holdings above $500,000 at one broker in one capacity (about $589,000 near Dec 2032, Keel arithmetic) | Where assets sit (implementation; lead decides) | What is held | Neither; not in the IPS (risk) |

CANON check summary: 2 rows are the two reasons (T5, T10); 31 are neither. None adds a reason. Rows T18, T19, T27 and T33
are instrument or custody steps; the report must show them as steps inside the plan, never as triggers (A34).

## (d) Gaps

- **Which Treasury-bill ETF holds waiting money**, and its fee: still a student check (NUMBERS 9). T6 cannot be sourced.
- **IBTM's own money market holding** was not checked in its holdings file; IBTG and IBTR hold "BLK CSH FND TREASURY SL
  AGENCY". Check IBTM to IBTQ before quoting T22.
- **BlackRock's lending indemnity.** The SAI mentions "BlackRock-specific indemnification exposure"; its terms were not
  read. T21's size beyond 0.5% is therefore open.
- **Fund annual and semi-annual reports** (lending income, any losses) were not read.
- **"An expense change made with notice"** (NUMBERS 0 and 3) was not found in the IBTM summary prospectus; the fee waiver
  "may be terminated prior to the Fund's termination only upon the written agreement of the Trust and BFA". The rest of
  NUMBERS 3's line is now VERIFIED (card 3).
- **SEC customer-protection rule** (customer securities kept apart at a broker) not read; the SIPC row rests on SIPC's own
  pages. The $589,000 is Keel arithmetic adding three NUMBERS figures at slightly different dates.
- **$1,414 against fund frictions.** A 0.5% shortfall on five $50,000 iBond rungs is about $1,250 (Keel arithmetic). The
  engine should confirm whether the $1,414 spare covers it on the real rung sizes.
- **Debt-limit pace** is a straight line from two DTS dates; tax receipts in April 2027 would slow it. Not a forecast.
- **Treasury buyback schedule** not read (row 20 UNVERIFIED). The Atlanta Fed line on callable bonds was seen only in a
  search excerpt; row 19 rests on the TreasuryDirect release and the TBAC charge.
- **Q15 corrections.** Q15 row 31 and its table say the par curve is published about 3:30 pm; quotes are taken then and
  the curve is posted by 6:00 pm ET. Q15's table quotes void figures (row 30 above).
- **REFERENCES_APA #78** gives a blackrock.com URL; this card read the same document (IS-SP-IBTM-0226) at ishares.com.
  No error.
- **DGBAS release page** (eng.stat.gov.tw cp.aspx?n=2328) returned no content on 10 Nov; the DGBAS rows rest on
  REFERENCES #40 and #44 (checked by Q10 on 9 Nov).
- **NSW subsidence guide date**: the document number is RDOC23/51285; the publication date was not recorded.
- **Exact title of the combined iShares Trust prospectus** was not recorded; the APA entry below uses a descriptive title.

## Sources (APA 7; all accessed 10 Nov 2026)

Already in `../REFERENCES_APA.md` (use those entries): #9 IBTM fund page; #13 IBTR fund page; #40 DGBAS construction cost
indices; #44 DGBAS price indices for October 2026; #78 IBTM summary prospectus (re-read in full today); #112 Treasury
daily par yield curve; #116 VT fact sheet.

New, read at the source:
1. Bureau of the Fiscal Service. (2026, November 6). *Daily Treasury Statement* [Data set]. U.S. Department of the
   Treasury. https://fiscaldata.treasury.gov/static-data/published-reports/dts/DailyTreasuryStatement_20261106.pdf
   (also 18 Aug and 6 Oct 2026 statements at the same path).
2. BlackRock. (2026, October 15). *iShares iBonds ETFs near final distribution date* [Press release]. Business Wire.
   http://www.businesswire.com/news/home/20261015791681/en/iShares-iBonds-ETFs-Near-Final-Distribution-Date
3. Central Bank of the Republic of China (Taiwan). (n.d.). *NT$/US$ closing rate* [Data set]. Retrieved November 10,
   2026, from https://www.cbc.gov.tw/en/lp-700-2.html
4. Exchange-traded funds, 17 C.F.R. § 270.6c-11 (2026). https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.6c-11
5. iShares Trust. (2026a, February 27). *Prospectus: iShares iBonds term Treasury ETFs* [Prospectus]. BlackRock.
   https://www.ishares.com/us/literature/prospectus/p-ishares-trust-us-treasury-ibonds-non-ibonds-10-31.pdf
6. iShares Trust. (2026b, February 27). *Statement of additional information: iShares iBonds ETFs* (as supplemented
   September 11, 2026). BlackRock. https://www.ishares.com/us/literature/sai/sai-ishares-ibonds-corporate-etf-10-31.pdf
7. iShares Trust. (2026c, March 25). *Summary prospectus: iShares iBonds Dec 2036 Term Treasury ETF* (Form 497K).
   U.S. Securities and Exchange Commission. https://www.sec.gov/Archives/edgar/data/1100663/000119312526123568/d121596d497k.htm
8. iShares Trust. (2026d, October 15). *Supplement dated October 15, 2026 to the currently effective summary prospectus,
   prospectus and statement of additional information for IBDR, IBTG and IBHF* (Form 497). OTC Markets.
   https://www.otcmarkets.com/filing/html?guid=7q-Xk621EjtFTih&id=19853207
9. Mining Industry Advisory Committee. (2022). *Mine safety management system: Code of practice*. Department of Mines,
   Industry Regulation and Safety, Western Australia.
   https://www.worksafe.wa.gov.au/system/files/migrated/sites/default/files/atoms/files/221188_cp_msms_0.pdf
10. NSW Resources Regulator. (n.d.). *Guide: Managing risks of subsidence* (RDOC23/51285). NSW Government.
    https://www.resources.nsw.gov.au/sites/default/files/documents/guideline-managing-risks-of-subsidence-guideline.pdf
11. NSW Resources Regulator. (2023). *Technical reference guide: Gas outbursts – principal hazard management plan*
    (MEG/DOC21/202783). NSW Government. https://www.resources.nsw.gov.au/sites/default/files/2023-04/trg-gas-outbursts-phmp.pdf
12. Securities Investor Protection Corporation. (n.d.). *What SIPC protects*. https://www.sipc.org/for-investors/what-sipc-protects
13. Securities Investor Protection Corporation. (2026). *How SIPC protects you* [Brochure].
    https://www.sipc.org/media/brochures/HowSIPCProtectsYou-English-Web.pdf
14. The Pensions Regulator. (2023, April 24). *Using leveraged liability-driven investment* [Guidance].
    https://www.thepensionsregulator.gov.uk/document-library/scheme-management-detailed-guidance/funding-and-investment-detailed-guidance/liability-driven-investment
15. TreasuryDirect. (2009, July 15). *Treasury calls 11-3/4 percent bonds of 2009-14* [Press release]. U.S. Department of
    the Treasury. https://maint.treasurydirect.gov/news/2009/release-07-15
16. TreasuryDirect. (n.d.). *Securities search* [Web service; CUSIPs 912810PT9, 912810PX0, 912810QD3, 912810QL5,
    912810QT8]. Retrieved November 10, 2026, from https://www.treasurydirect.gov/TA_WS/securities/search?cusip=912810PT9&format=json
17. Treasury Borrowing Advisory Committee. (2024). *Charge: Q2 2024* [Presentation]. U.S. Department of the Treasury.
    https://home.treasury.gov/system/files/221/TBACCharge2Q22024.pdf
18. U.S. Department of the Treasury. (2025, February 18). *Treasury yield curve methodology*.
    https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics/treasury-yield-curve-methodology
19. Vanguard. (2026c, February 27). *Vanguard Total World Stock ETF prospectus* (Vanguard International Equity Index
    Funds). https://personal.vanguard.com/pub/Pdf/p3141.pdf (sections on objective, strategy, index, risks and ETF
    trading read; financial highlights not read).

Seen, not read in full (UNVERIFIED for quoting): TreasuryDirect marketable securities FAQ (buybacks); Atlanta Fed page
on callable bonds (search excerpt); WorkSafe WA PMHMP page, NSW emergency planning code and MDG-1031 (excerpts only).
No psychology or behavioural papers are cited.
