# Canon: everything Caplet's submitted work commits it to

Keel's continuity file for the Final Report, built Sun 8 Nov 2026 (Sydney). Film continuity departments keep a
record of everything already on camera so that no later scene contradicts it; this is the same idea. It lists every
claim that Caplet's submitted work makes, quoted exactly with its source and line, so that every later note, number
and draft can be checked against it (`DAILY_RUN.md` step 6; the final check on Thu 26 Nov, `README.md`). Notes and
tables only: nothing here is wording for the report.

**The rule.** Ray's guardrail 1: "All submitted items, such as IPS trading notes portfolio and trading note
reflection, are all frozen. You must reach an extremely high of coherence with the materials that has already been
sent." A clash with the canon is a risk to record and explain in the report. It is never a change to the strategy.
Wharton: "you may not redesign your strategy after observing the results", while "A long-term strategy may include
planned adjustments as funding dates approach" (`WHARTON_NORTH_STAR.md` l.53-56). The 2028 top-up and the 2031 move
below are planned adjustments written into the IPS; nothing else is.

**The submitted sources (the only canon).**

| Key | File | What it is |
|---|---|---|
| IPS l.N | `keel/final_report/FINAL_IPS_as_submitted.txt` (line numbers as `cat -n` shows them) | Elevator pitch (l.3) and the 500-word IPS, a letter to Laura signed "Caplet" (l.7-22), submitted 7 Nov |
| TNA l.N | `keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt` | Trading Notes Analysis, locked 23 Oct: three WInS notes (l.5, l.13, l.21) and three reflections (l.7, l.15, l.23) |
| SNAP l.N | `competition/wins/2026-10-23_snapshot.md` | The WInS book (no trade since 8 Oct, SNAP l.71; trading froze 6 Nov) |
| WN l.N | `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md` | Text of every WInS trade note as copied 13 Oct; filled-order notes l.14-24, cancelled-order notes l.37-40. All 15 matched the 22 Oct export character for character (SNAP l.41-42) |

Context only, never canon: the client case (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, cited
"case l.N"), `CASE_MAP.md`, `research/meta/META_ANGLES.md` angle 5, `research/meta/WHY_WHARTON.md` section 0 item 2,
`WHARTON_NORTH_STAR.md`.

**Conventions.** Quotations sit in straight double quotes and are character-exact: the IPS and the reflections use
curly apostrophes and en dashes, the WInS notes straight apostrophes, and both are kept as they are. The three TNA
notes are identical to WN l.16, l.19 and l.14 (checked by script, 8 Nov). Which note belongs to which filled order
rests on the team's 13 Oct record, because the WInS export does not say (SNAP l.43-44). MODEL = Keel's calculation;
UNVERIFIED = not checked at the source. WInS was not opened (house rule).

---

## Table A. Commitments: what the submitted work says will happen

### A.1 The thesis and the meaning of certainty

| # | Exact words (quoted) | Source and line | What it commits Caplet to, in plain words | What the Final Report must show or do to stay consistent | Open question for the numbers |
|---|---|---|---|---|---|
| A1 | "Laura’s career is already a giant stock she can’t sell. So we hedge it!" | IPS l.3 | The plan is a hedge of her career. | Lead the strategy with this thesis and show what is hedged and how. Never present the plan as growth-led. | None required. |
| A2 | "And so, we believe, your portfolio should be a counterbalance to that – definitely not a contributor." | IPS l.9 | The portfolio must not add risk that moves with her career. | Show every promised dollar in Treasuries; VT is the bounded exception (only money not yet promised, A5; tension D11). | VT's share of the plan in Jan 2028. |
| A3 | "So, naturally, that was our plan – until we stopped and considered the actual nature of a writer’s income." | IPS l.9 | A team story already told: Caplet first planned on shares and changed its mind because of how a writer is paid. | The experience section tells the same turn, with real dates and events from Caplet only; no other reason may replace it as the main one. | None. Ask Caplet for its own dated account (the repo also records modelled payment misses for the team's first growth-first design, CLAUDE.md "Strategy status", 28 Sep). |
| A4 | "barring a US default, none of your 10 operating payments will depend on a share price, or on anybody else’s money, when they fall due." | IPS l.11 | Caplet's definition of "a high degree of funding certainty" (case l.91, l.97-98): structural, not a probability. | Use it as the definition the case asks for; then say how it was evaluated, the assumptions, and the residual risks by size (iBond NAV payout, reinvested coupons, maturity gaps, the Jan 2027 price before purchase, the 2028 top-up). | Reinvestment shortfall; iBond NAV gap; top-up on the latest curve. |
| A5 | "The money for the operating commitment will go straight into Treasuries, because it’s fixed and non-negotiable, and only money you haven’t promised yet goes into shares, where it can grow." | IPS l.11 | No share money behind any payment; shares only from money not yet promised. | No exhibit may show a payment drawing on VT. Money waiting between a maturity and its payment stays in Treasuries (A22). | None. |
| A6 | "You take risks on the page. Fair enough; that’s your job. With these promises, ours is to take none." | IPS l.19 | No risk taken with promised money. | Keep the scope ("with these promises"); show the residual risks measured, not denied (C21). | Sizes of the residual risks. |

### A.2 The ladder, bought with the first deposit

| # | Exact words (quoted) | Source and line | What it commits Caplet to, in plain words | What the Final Report must show or do to stay consistent | Open question for the numbers |
|---|---|---|---|---|---|
| A7 | "In January 2027 we’ll use your first deposit to buy 10 Treasuries (T-Bonds or iShares iBonds Term Treasury ETFs, whichever works best for each year), each maturing just before it’s needed." | IPS l.13 | Jan 2027: the first deposit buys ten holdings, one per payment, each a T-bond or an iBond Treasury ETF, each ending before its January. | List the ten by payment year: IBTM, IBTO, IBTP, IBTQ, IBTR for 2033-37; T-bonds Feb-2037, May-2038, Nov-2039, Nov-2040, Nov-2041 for 2038-42 (SNAP l.22-31). Give each gap (B8). Explain "whichever works best" as WInS availability plus one real choice (D13). | Cost of each rung on the 6 Nov close; days of gap per rung. |
| A8 | "Held to the end, these pay what they say – no price fluctuations for us to fear." | IPS l.13 | Every ladder holding is held to its end; nothing is sold on a price move. | Show the hold rule in the implementation (no trade since 8 Oct, SNAP l.71); give the iBond rungs their true meaning (C2, D5). | iBond NAV gap per rung. |
| A9 | "Every year the bonds sit untouched is a good year – one less year of Laura’s money being exposed to anything the restless markets might decide to do." | TNA l.7 | Bonds untouched until they mature. | Same as A8. | None. |
| A10 | "so we’ll simply ignore price noise in the interim." | TNA l.15 | iBond ETF price moves before their end are ignored. | Present WInS price moves as noise, never as performance. | None. |
| A11 | "At current yields, this would cost roughly $300,000 – in other words, your entire first deposit." | IPS l.13 | All of the first deposit goes to the ladder; in Laura's plan none of it buys VT or the floor fund. | Give the cost with its date and basis (B9). Never imply part of the first deposit buys shares (the WInS book does, because it is scaled: D3). | Ladder cost on the latest curve (6 Nov close: $301,544, MODEL). |
| A12 | "Together, our T-Bonds and iBonds ensure each of Laura’s payments rests on a dedicated instrument (not merely a forecast)." | TNA l.15 | One dedicated instrument per payment. | Keep the one-to-one map in every exhibit. If the report discusses later bonds' coupons paying earlier payments (`CASE_MAP.md` C1(b)), the map must still hold. | None. |
| A13 | "we use the 4.750% Treasury maturing 15 Feb 2037 for Laura's 1 Jan 2038 payment because it is the latest WInS bond available beforehand." | TNA l.5 (= WN l.16) | The 2038 payment rests on the Feb-2037 bond. | Keep this rung in every ladder table. | Its reinvestment need. |
| A14 | "Laura’s payments are fixed in nominal dollars, so a nominal Treasury matches the liability perfectly, meaning we don’t need TIPS, which would hedge against a nonexistent inflation risk." | TNA l.7 | Nominal instruments for nominal payments; no inflation-linked instruments. | Put the inflation discussion on the facility side (case l.146-147), not the payments; mention TIPS only as this reflection does (C14, C15). | None. |

### A.3 Reinvestment and the money that waits

| # | Exact words (quoted) | Source and line | What it commits Caplet to, in plain words | What the Final Report must show or do to stay consistent | Open question for the numbers |
|---|---|---|---|---|---|
| A15 | "The 10.5-month gap creates reinvestment-rate risk on the proceeds held in a short-term Treasury ETF." | TNA l.5 (= WN l.16) | Money waiting between a maturity and its payment sits in a short-term Treasury ETF, and Caplet owns the rate risk on it. | Name the holding type (a WInS-listed short-term Treasury ETF; which one is listed is UNVERIFIED) and price the risk. Never "cash at 0%" for Laura's plan (0% is only the WInS cash rule). | Earnings on waiting money; cost of a 2-point fall. |
| A16 | "Its proceeds stay in a short-term Treasury ETF for 7.5 months, so only part of the payment has brief exposure to short-term Treasury rates." | WN l.17 (May-2038, filled 10/7 12:22:11 AM ET) | Same for the 2039 payment. | Same as A15. | Same as A15. |
| A17 | "Held to maturity, its fixed coupons and principal cover most of it; reinvested coupons fund the rest." | WN l.18 (Nov-2039, filled 10/6 11:45:04 PM ET) | The 2040 payment depends partly on coupons reinvested at future rates. | Say so for every T-bond rung, with the split (D7). | Share of each rung paid by fixed cash and by reinvestment. |
| A18 | "With no iBonds Treasury funds maturing in 2037-43, the last five payments use individual Treasuries, scaled to the model portfolio, with reinvested coupons funding part of each." | WN l.24 (Nov-2041, filled 10/6 7:55:45 PM ET) | The last five payments rely partly on reinvested coupons; the WInS bonds are sized to a scaled model portfolio. | Explain the scale once (D3) and show reinvestment for 2038-42. | Same as A17. |

### A.4 The 2028 deposit: top-up, floor fund, VT

| # | Exact words (quoted) | Source and line | What it commits Caplet to, in plain words | What the Final Report must show or do to stay consistent | Open question for the numbers |
|---|---|---|---|---|---|
| A19 | "But worry not – our plan isn’t dependent on yields staying put! Even if yields fall and the total cost of the ladder ends up being above $300,000, we’ll simply complete it with the 2028 deposit." | IPS l.13 | The 2028 deposit's first dollars complete the ladder. A planned step, not a change of plan. | Show the top-up first in the 2028 cash flow, before the floor fund and VT. On the 6 Nov close it is live ($1,544 over, MODEL). | Top-up on the latest curve and after falls of 0.5, 1 and 2 points; which rungs wait a year. |
| A20 | "If yields fall more than about 0.2 percentage points by January, the 2028 deposit would top up the ladder, leaving less for the facility." | WN l.15 (IBTR, filled 10/7 4:42:53 AM ET) | The same rule seen from the facility: the top-up comes out of facility money. | Show the top-up shrinking what is left for the floor fund and VT. Treat "about 0.2" as a dated, basis-dependent figure (B29). | Same as A19. |
| A21 | "this is one of the first payments we would top up if yields fall before January." | WN l.20 (IBTO, filled 10/6 9:58:19 PM ET) | If the first deposit falls short, the 2034 rung (IBTO) is among those left short in Jan 2027 and completed in Jan 2028. | Any account of which rungs are completed first must agree with this, or explain it (D17). | Which rungs, by how much, on the latest curve. |
| A22 | "Most of the 2028 deposit will fund a Treasury fund maturing in late 2032, whose payout is the bare minimum you’ll be able to promise your co-sponsors without doubt." | IPS l.15 | After any top-up, most of the 2028 deposit buys a Treasury fund ending late 2032 (IBTM, A24); its payout is the floor of the facility contribution. | Name the fund, the amount, its expected Dec 2032 payout, and how the promised minimum allows for a payout that is not fixed (C5, C6). Never a fixed "$150,000". | Floor-fund amount (share of the $150k); expected payout and its spread. |
| A23 | "Yet another Treasury fund will decide the floor of her facility contribution, and a world stock ETF will determine the ceiling." | IPS l.3 | Floor from a Treasury fund; ceiling set by the world stock ETF. | As A22, A25, A29 (tensions D1, D2). | As A22 and A25. |
| A24 | "IBTM does two jobs in Laura's plan. It supports her first $50,000 payment and provides a floor for her facility contribution, giving co-sponsors a minimum figure in 2031." | TNA l.13 (= WN l.19) | One fund, two jobs: the 2033 rung and the floor; the minimum is given to co-sponsors in 2031. | Show two lots bought on two dates (Jan 2027 rung, Jan 2028 floor) and that the payment comes first (the case sets the reserve aside before the facility, case l.94). | Lot sizes in the plan; payout of each lot. |
| A25 | "The rest will go into a world share fund of thousands of companies – VT, Vanguard Total World Stock ETF – and its returns will help determine your maximum facility contribution." | IPS l.15 | The remainder of the 2028 deposit goes into VT; VT's returns move the top. | Show VT's amount and its paths to 2031 at the stated assumption (7.5%, B15), in good and bad markets (case l.118-119). | VT amount in Jan 2028; its value at the move date (spread). |
| A26 | "The T-Bonds and iBonds already cover the operating commitments, so VT answers a different question – how generous can the facility contribution be?" | TNA l.23 | VT's job is the facility, never the payments. | As A5; and see D1 for VT's second job (flexibility). | None. |
| A27 | "VT is where we allow ourselves to be wrong – because it’s the only investment not standing between Laura and a payment deadline." | TNA l.23 | Losses are acceptable only in VT. | Show that a VT loss touches no payment and no promised figure (B26, D16). | VT drawdowns in bad markets against the kept half. |

### A.5 The band, the kept half and the 2031 move

| # | Exact words (quoted) | Source and line | What it commits Caplet to, in plain words | What the Final Report must show or do to stay consistent | Open question for the numbers |
|---|---|---|---|---|---|
| A28 | "That means markets will be able to increase or decrease the top of your planned band as we get closer to 2031, but the bottom will remain constant, built on the ever-reliable Treasuries." | IPS l.15 | A band: the bottom fixed by the floor fund, the top moved by markets until the 2031 move. | Show the band and how it moves to 2031 in favourable and unfavourable markets (case l.118-119). | The band today and its paths. |
| A29 | "They only set how far her gift rises above her promised minimum. A fall can shrink the extra, and a rise before 2031 lifts the top of the range co-sponsors hear." | TNA l.21 (= WN l.14) | VT never touches the minimum; before 2031 it moves the top of the range co-sponsors hear. | Same story as A25, A28 and A31 (D1, D4). | As A25. |
| A30 | "Importantly for you, half of the value of the shares will be promised to no one." | IPS l.15 | Half of VT's value is never part of any promise. | Never count the kept half in the range or in the confidence statement. | Size of the kept half in 2031 and 2033 (spread). |
| A31 | "That is your flexibility – for building costs that overrun, a stronger Taiwan dollar or a co-sponsor falling short." | IPS l.15 | The kept half has three named uses. | Treat it as the case's "financial flexibility" (case l.102-103, l.145). Discuss each use without sizing a contingency fund (case l.106-107) or estimating the facility's cost (case l.164-165). Define how its use relates to the announced range (D12). | What each risk could cost against the kept half, as illustration only. |
| A32 | "Before you meet co-sponsors in 2031, the other half will move into Treasuries, so whatever figure you choose is money you already own." | IPS l.15 | A planned move of the promised half of VT into Treasuries before the 2031 meetings; the figure Laura announces is money already owned. | Say when and into what: a WInS-listed Treasury holding that pays out before 1 Jan 2033 (IBTM is the only late-2032 one the repo knows; the choice is UNVERIFIED). Then give the 2031 range and its confidence (case l.117-118; D14). | Promised half at the move date; the 2031 range and its confidence; what still moves between 2031 and 2033. |

### A.6 From 2033, and the only reasons to change

| # | Exact words (quoted) | Source and line | What it commits Caplet to, in plain words | What the Final Report must show or do to stay consistent | Open question for the numbers |
|---|---|---|---|---|---|
| A33 | "From 2033 the Treasuries are the operating reserve." | IPS l.17 | The ladder is the operating reserve (case l.94-96): held to maturity, it pays one rung a year and runs down. | Answer the case's reserve questions from this: size in 2033, composition (iBond ETFs ending 2033-36, then T-bonds), how it changes (no rebalancing; waiting money in a short-term Treasury ETF, A15). | Reserve value on 1 Jan 2033 (MODEL). |
| A34 | "There are only 2 possible reasons we would change our plan – a missed deposit or a Treasury default. A fall in the market is not one of them." | IPS l.17 | No other trigger: market falls, yield moves and NAV gaps change nothing. | Evaluate, never add a rule or trigger. Show what a missed deposit changes (`CASE_MAP.md` C6); a smaller deposit is not named (D9). | What a missed and a smaller 2028 deposit each do to the ladder, the floor and VT. |

---

## Table B. Factual and numerical claims

Status words: TRUE (as worded, with the check named); PARTLY; DATED (true on its date, not now); UNVERIFIED (not
checked at source by Keel today; never guessed). All web pages read Sun 8 Nov 2026.

| # | Exact words (quoted) | Source and line | Status | Check run or source | Note for the Final Report |
|---|---|---|---|---|---|
| B1 | "6 years to wait" | IPS l.9 | TRUE | Case l.43 (first deposit at the start of 2027) and l.88-89 (first payment at the start of 2033) | The 2028 deposit waits 5 years. |
| B2 | "your taste for thoughtful risk" | IPS l.9 | TRUE | Case l.69-70: "willing to take thoughtful risks" | None. |
| B3 | "In good years the advances come, and the speaking fees, and the licences." | IPS l.9 | TRUE (her income sources) | Case l.44-45: "publishing advances, speaking engagements, licensing" | None. |
| B4 | "In a recession they come later and smaller, and during that same period, shares fall and co-sponsors cut their budgets." | IPS l.9 | PARTLY; co-sponsor part UNVERIFIED | For: `research/cards/Q1_career_as_shares.md` rows 30, 31, 33, 35, 36, 44 (2009 advances cut, acquisitions frozen in Nov 2008, speaking budgets cut, licensing royalties down 8.7% in 2009; 46.3% of surveyed authors lost speaking income in COVID). Against: rows 27, 32 (2001 book sales flat; graphic novels up 29% in 2020). Shares: S&P 500 down 36.55% in 2008 but up 18.02% in 2020 (Damodaran file, via the Q1 card). Co-sponsor budgets in a recession: not researched (Q1 card l.222) | Industry evidence, dated; Laura's own income is not observed. The co-sponsor half needs a source (Q4, Q11). |
| B5 | "‘high degree of certainty’" | IPS l.11; also TNA l.7 | TRUE | Case l.91: "must be funded by the investment portfolio with a high degree of certainty" | The case states a requirement; the texts call it Laura's request. Harmless. |
| B6 | "10 Treasuries (T-Bonds or iShares iBonds Term Treasury ETFs, whichever works best for each year)" | IPS l.13 | TRUE of the book | SNAP l.22-31: five iBond ETFs, five T-bonds | "Treasuries" includes funds (C2). |
| B7 | "In January 2027" | IPS l.13 | TRUE | Case l.43, l.59 | The WInS orders were placed in Oct 2026 at Oct prices (Table E). |
| B8 | "each maturing just before it’s needed" | IPS l.13 | PARTLY | My date arithmetic: iBond ETFs end "on or about October or December 15 of the year in each Fund’s name" (iShares IBTM fact sheet, 30 Sep 2026), 17 days before each 1 Jan; Nov-2039, Nov-2040, Nov-2041 bonds 47 days; May-2038 231 days (7.6 months); Feb-2037 320 days (10.5 months) | Two rungs end months early (C4, D6). |
| B9 | "roughly $300,000" | IPS l.13 | TRUE as worded, dated | MODEL, re-run 8 Nov: `keel/scripts/ladder_history.py` on `competition/official_market_data/daily-treasury-rates_2026-11-06.csv` gives $301,544 on 1 Jan 2027 (payment-date basis, 6 Nov close; DV01 $300 per bp). `keel/scripts/holdings_ladder.py` (5 Nov prices): curve $302,137; instruments held $303,269; money idle at 0% between maturity and payment $306,663 | Always quote date and basis. "Under $300,000" is true only on older curves (6 Oct: $288,929, same script). |
| B10 | "your entire first deposit" | IPS l.13 | TRUE in effect | As B9: slightly more than the deposit, which is why A19 is live | None. |
| B11 | "a Treasury fund maturing in late 2032" | IPS l.15 | TRUE (IBTM) | IBTM summary prospectus, 27 Feb 2026: "a term fund that will terminate on or about December 15, 2032" (ishares.com) | A fund terminates rather than matures (C8). Whether any other WInS-listed fund ends in late 2032: UNVERIFIED. |
| B12 | "a world share fund of thousands of companies" | IPS l.15 | TRUE | Vanguard VT page and fact sheet: 10,185 stocks at 30 Sep 2026 (advisors.vanguard.com; fund-docs.vanguard.com/F3141.pdf) | None. |
| B13 | "holds about 10,000 stocks at a 0.06% fee" | TNA l.21 (= WN l.14) | TRUE | Vanguard: 10,185 stocks (30 Sep 2026); expense ratio 0.06% "as of 02/27/2026" | Use Vanguard's dated figure, not the secondary-site counts in older repo files (10,180; 10,242). |
| B14 | "This ETF owns thousands of companies, diversified across countries and sectors" | TNA l.23 | TRUE | Vanguard, 30 Sep 2026: developed 89.98%, emerging 10.02%; sector table on the fact sheet | None. |
| B15 | "a forecast return of about 7.5% a year (as per JPMorgan)" | TNA l.23 | TRUE, with limits | J.P. Morgan press release, 19 Oct 2026: "Global equities are projected to return 7.5% (USD), increasing from 7.0%" (am.jpmorgan.com); horizon 10-15 years. Compound or arithmetic: UNVERIFIED (matrix behind a login; `keel/office/outbox/2026-10-27_noticeboard_7-5-is-world-stocks.md`) | Cite as J.P. Morgan's 2027 assumption for global equities, 10-15 years; never "compound"; it is not net of VT's fee. |
| B16 | "the entire market’s growth premium at an expense ratio of just 0.06%" | TNA l.23 | TRUE as rounding | Vanguard: the FTSE Global All Cap Index "Covers more than 98% of the global investable market capitalization"; fee as B13 | A premium is expected, not promised. |
| B17 | "the 4.750% Treasury maturing 15 Feb 2037" | TNA l.5 | TRUE | SNAP l.27; CUSIP 912810PT9 (team ticket, `caplet/google_drive/sheets/portfolio_and_trading_notes/rb_tickets.csv` l.19) | Older repo files that say "5.000% Feb-2037" are wrong. |
| B18 | "the latest WInS bond available beforehand" | TNA l.5 | TRUE per team record; UNVERIFIED by Keel | `.../trading_notes.csv` l.129: "WInS does not list the 5.000% May-2037 (checked 5 Oct)"; that bond exists (CUSIP 912810PU6, same record) | Present it as the team's 5 Oct check. |
| B19 | "The 10.5-month gap" | TNA l.5 | TRUE | 15 Feb 2037 to 1 Jan 2038 = 320 days = 10.51 months | None. |
| B20 | "It holds 2032 Treasuries, so the timing fits, although the final payout is not fixed." | TNA l.13 (= WN l.19) | TRUE | iShares IBTM fact sheet, 30 Sep 2026: "seeks to track an index of U.S. Treasury bonds maturing in 2032", 15 holdings, Treasuries 99.45%, cash 0.55%. Summary prospectus, 27 Feb 2026: "The Fund does not seek to return any predetermined amount at maturity or in periodic distributions." | In its final months it holds cash and cash-like instruments; the payout comes about 17 days before 1 Jan 2033. |
| B21 | "Some years, WInS lists no Treasuries maturing" | TNA l.15 | TRUE per team record; UNVERIFIED by Keel | `competition/COMPETITION.md` l.112: "WInS lists 43 US T-bonds, none maturing Feb 2031 to Feb 2036" | For 2036 WInS did list a 4.5% Feb-2036 bond; IBTR was chosen over it (`.../trading_notes.csv` l.15). |
| B22 | "Defined-maturity, investment-grade, liquid, cheap and transparent about yields" | TNA l.15 | MOSTLY TRUE | Defined end date and 0.07% fee: iShares pages for IBTM, IBTQ, IBTR. Yields published daily. IBTM: net assets $612m, 30-day median bid/ask 0.05% (28 Oct 2026). IBTR: net assets $11.2m (fact sheet, 30 Jun 2026), a much smaller fund. Credit: Treasury holdings; ratings not re-checked | "Liquid" is relative to odd-lot bonds and weakest for IBTR. |
| B23 | "their terminal payout is a net asset value, as opposed to a promise of par" | TNA l.15 | TRUE | iShares: after termination the fund "will distribute substantially all of its net assets"; "do not seek to return any predetermined amount" | The precise statement; the IPS's looser one is C2. |
| B24 | "a level of liquidity which no odd-lot bond offers" | TNA l.15 | UNVERIFIED | Not checked against a source | Find a source on odd-lot bond pricing before the report leans on it. |
| B25 | "Laura’s payments are fixed in nominal dollars" | TNA l.7 | TRUE | Case l.90: "each payment is a fixed $50,000 and is not adjusted for inflation" | None. |
| B26 | "it’s the only investment not standing between Laura and a payment deadline" | TNA l.23 | TRUE of the WInS positions; loose for the plan | In WInS the one IBTM position also serves the 2033 payment; in Laura's plan the floor lot of IBTM serves no payment either | Read "investment" as "share holding" (D16). |
| B27 | "IBTR is for Laura's fifth payment in 2037." / "IBTO is for Laura's second $50,000 payment, due 1 Jan 2034." / "IBTP is for Laura's $50,000 payment on 1 Jan 2035." / "IBTQ is for Laura's fourth $50,000 payment, due 1 Jan 2036." / "supports Laura's ninth $50,000 payment on 1 Jan 2041." / "supports her final $50,000 payment on 1 Jan 2042." | WN l.15, l.20, l.21, l.22, l.23, l.24 | TRUE | Payments start of 2033 to start of 2042 (case l.88-89); order and dates check | None. |
| B28 | "On the 6 Oct Treasury curve, her first $300,000 is enough to buy Treasuries for all ten payments." | WN l.15 | DATED | My re-run: $288,929 on the 6 Oct close (payment-date basis, MODEL); $301,544 on 6 Nov | Quote only with its date; its condition (B29) has since come true. |
| B29 | "If yields fall more than about 0.2 percentage points by January" | WN l.15 | BASIS-DEPENDENT; UNVERIFIED as stated | 6 Oct, payment-date basis: $11,071 of room at $286 per bp = 39bp (my re-run). The 0.2 fits a stricter basis (instruments held, money idle until each payment), which added about $4,500 to the cost on 5 Nov (`holdings_ladder.py`); 6 Oct on that basis not re-run. The cancelled-order note says "0.3" (WN l.37) | If a threshold is ever quoted, name basis and date. Yields have since fallen past it (6 Nov: $1,544 over). |
| B30 | "WInS has no individual Treasury maturing in 2033" / "Since WInS has no individual Treasury maturing in 2035" | WN l.20, l.22 | TRUE per team record; UNVERIFIED by Keel | `competition/COMPETITION.md` l.112 | None. |
| B31 | "so we use a fund holding 2033 Treasuries instead. Its December payout is not fixed" / "we use a fund that holds 2035 Treasuries instead. Its payout is not fixed, but it ends about two weeks before the payment is due." | WN l.20, l.22 | TRUE | iShares: IBTO and IBTQ track Treasuries maturing in 2033 and 2035 and end on or about 15 Dec; 15 Dec 2035 to 1 Jan 2036 = 17 days | None. |
| B32 | "On 2 Oct, it closed just 0.07% above the value of the Treasuries it holds, so the fund was not trading at a meaningful premium." | WN l.21 | UNVERIFIED | Not re-checked; the team's method is in `.../trading_notes.csv` l.33 (premium to NAV) | Do not repeat unless re-checked against iShares' premium and discount history. |
| B33 | "Its payout is not fixed, but it ends close to when Laura needs the money." | WN l.21 | TRUE | IBTP ends on or about 15 Dec 2034, 17 days before 1 Jan 2035 | None. |
| B34 | "the latest WInS bond before Laura's 1 Jan 2039 payment" | WN l.17 | UNVERIFIED (team record) | Team tickets name the 4.375% Feb-2038 and 5.000% May-2037 as alternatives (`rb_tickets.csv` l.18); no record of a later 2038 bond on WInS | None. |
| B35 | "for 7.5 months" | WN l.17 | TRUE (rounded) | 15 May 2038 to 1 Jan 2039 = 231 days = 7.6 months | None. |
| B36 | "comes due 47 days before Laura's $50,000 payment on 1 Jan 2040" | WN l.18 | TRUE | 15 Nov 2039 to 1 Jan 2040 = 47 days | None. |
| B37 | "A lower-coupon bond would reduce reliance on reinvested coupons, but WInS lists none for that date. Its 5 Oct WInS price was consistent with the Treasury yield curve." | WN l.23 | First clause TRUE (a lower coupon puts more of the payment in fixed principal); the rest UNVERIFIED | The repo's open list asks whether WInS lists a 1.375% Nov-2040 bond (`keel/library/assistant_review_2026-10/oct20/verify_drill2/drill_v2_checked.md` l.602); never answered. The 5 Oct price check is the team's | Do not repeat "WInS lists none" without a check. |
| B38 | "With no iBonds Treasury funds maturing in 2037-43" | WN l.24 | TRUE (as of Aug 2026) | iShares iBonds range brochure (data as of 30 Jun 2026, published 14 Aug 2026): Term Treasury funds end Dec 2026 to Dec 2036, then Dec 2044, 2045, 2054, 2055 | A fund launched after Aug 2026 was not checked. |
| B39 | "Laura's 3.125% Treasury maturing 15 Nov 2041" | WN l.24 | TRUE | SNAP l.31 | None. |

---

## Table C. Loose phrases a bond reader would catch

Readers after the first screen know bonds and liabilities (`research/meta/WHY_WHARTON.md` section 0 item 2;
`research/meta/META_ANGLES.md` angle 5). The meaning column is a note of what is true, for checking drafts; it is not
wording for the report. Rule: explain, never contradict. The last column names the number the register
(`NUMBERS.md`, from Mon 9 Nov) must hold before the phrase can be explained.

| # | Phrase | Source and line | What a fixed-income professional would object to | The exact, true meaning to give it | Number needed from the register |
|---|---|---|---|---|---|
| C1 | "immune to markets" | IPS l.3 | Ladder prices move every day (about $300 per basis point on the 6 Nov close, MODEL); before Jan 2027 the cost itself moves with yields; reinvested coupons depend on future rates; iBond rungs pay NAV | Once bought and held to the end, each T-bond's coupons and face value are fixed in dollars and dates; price moves in between do not change what it pays; share markets cannot reach the ladder | Ladder DV01; reinvestment shortfall; NAV gap |
| C2 | "pay what they say" | IPS l.13 | Five of the ten rungs are iBond ETFs, which "do not seek to return any predetermined amount" | T-bonds pay their stated coupons and face value; iBond ETFs pay their net asset value at termination, close to the value of the Treasuries they hold (the TNA's own words, TNA l.15) | iBond NAV gap per rung (expected payout against the $50,000 target) |
| C3 | "no price fluctuations for us to fear" | IPS l.13 | Prices do fluctuate | Fluctuations exist but cost nothing if nothing is sold before its end (A8) | WInS price changes as an illustration only, never as performance |
| C4 | "each maturing just before it’s needed" | IPS l.13 | Feb-2037 ends 320 days early, May-2038 231 days early | Every holding ends before its payment, never after; two end 7.6 and 10.5 months early and their money waits in a short-term Treasury ETF (TNA l.5) | Gap days per rung; earnings on waiting money |
| C5 | "without doubt" | IPS l.15 | The floor is an iBond ETF payout, not a fixed sum; it is not even bought until Jan 2028 | The minimum Laura promises is a figure the fund's payout will reach barring a US default; the report must show how large the NAV difference can be and that the promised figure allows for it | Floor lot's expected payout and its spread |
| C6 | "the bottom will remain constant" | IPS l.15 | The fund's value moves daily and its payout is not fixed | Share markets cannot move the bottom; from the Jan 2028 purchase it moves only by the small NAV difference | As C5; floor size against Jan 2028 yields |
| C7 | "built on the ever-reliable Treasuries" | IPS l.15 | Fair for credit, but the floor is a fund of Treasuries, not a Treasury | The floor's only credit risk is the US government's (IBTM: Treasuries 99.45%, cash 0.55%, iShares, 30 Sep 2026) | None |
| C8 | "a Treasury fund maturing in late 2032" | IPS l.15 | Funds do not mature; they terminate and pay out | All its bonds mature during 2032; the fund then distributes its net assets on or about 15 Dec 2032 | None |
| C9 | "barring a US default" | IPS l.11 | Default is not the only residual risk | The only credit risk is the US government's; the other residuals (NAV, reinvested coupons, waiting money, the Jan 2027 price, the 2028 top-up) are named and sized | Each residual's size |
| C10 | "none of your 10 operating payments will depend on a share price" | IPS l.11 | iBond ETFs have a share price; full funding may need the 2028 deposit | No payment depends on any stock or stock fund; iBond ETFs held to termination pay NAV, not their market price | Top-up size; NAV gap |
| C11 | "won’t create wealth" | TNA l.7 | The ladder turns about $301,544 (MODEL) into $500,000 of payments, a flat yield of about 5.03% (my arithmetic, annual compounding) | The bonds earn only what the curve offers at purchase, with no upside beyond it; they are not where the facility's growth comes from | Ladder cost against payments; implied yield |
| C12 | "duration-matching" | TNA l.7 | The ladder is cash-flow matched; duration matching (immunisation) is a different technique that needs rebalancing | Matched payment by payment, which also matches duration; no rebalancing (`CASE_MAP.md` C9; `competition/COMPETITION.md` l.197-198) | Optional: ladder and payment durations on 6 Nov |
| C13 | "near-ironclad guarantee" | TNA l.7 | Nothing is guaranteed; the US Treasury owes the bonds, not the ETFs' payouts | As close to certain as Treasuries held to maturity can be, with each remaining gap named and sized | All residuals |
| C14 | "a nominal Treasury matches the liability perfectly" | TNA l.7 | The same TNA item names a 10.5-month gap and reinvestment-rate risk (TNA l.5); coupons arrive years before the payment | Nominal matches nominal: no inflation mismatch for fixed-dollar payments; timing and coupon reinvestment are the imperfect parts | Reinvestment shortfall per rung |
| C15 | "a nonexistent inflation risk" | TNA l.7 | Inflation still touches the facility; the case asks about inflation on projections and facility costs (case l.146-147) | For the payments, fixed in dollars, inflation risk is nil; for the building it is real, and the kept half is the IPS's answer (A31) | None for the plan; Taiwan building-cost and CPI series for context |
| C16 | "these behave a lot like bonds when held to their end" | TNA l.15 | They hold bonds, then cash in the final months; distributions vary; payout is NAV | Held to termination, the payout is close to that of a Treasury maturing that year, less a 0.07% a year fee; NAV, not par | NAV gap; fee drag |
| C17 | "rests on a dedicated instrument (not merely a forecast)" | TNA l.15 | The T-bond rungs need reinvested coupons (WN l.18, l.24), which depend on future rates | Each payment has its own instrument; the part paid by reinvested coupons depends on future rates and is sized | Fixed-cash share per rung |
| C18 | "a level of liquidity which no odd-lot bond offers" | TNA l.15 | IBTR is a small fund ($11.2m, 30 Jun 2026); the claim is unsourced (B24) | An ETF share trades on an exchange in any size at a quoted spread; a small block of one bond can be harder to sell at a fair price | None |
| C19 | "Yet another Treasury fund" | IPS l.3 | The floor fund is the same fund (IBTM) as the 2033 rung | A second purchase of a Treasury fund, in 2028, whose job is the floor (D2) | Lot sizes |
| C20 | "the 10 operating commitments" | IPS l.3 | A case reader: one operating commitment of ten payments (case l.87-89) | The ten operating payments | None |
| C21 | "ours is to take none" | IPS l.19 | Residual risks remain; VT carries share risk | No market risk on money already promised; the kept half of VT carries risk by design | Residual sizes |
| C22 | "whatever figure you choose is money you already own" | IPS l.15 | After the move, the promised half sits in Treasuries; if in an iBond ETF, its payout is NAV again | The figure announced in 2031 is covered by holdings already bought, not by future returns | Payout of the promised half's Treasury holding and its NAV gap |

---

## Table D. Tensions between the submitted texts

Each row gives the reading that makes all the texts true together, or says TRUE CONFLICT. None needs a change of
strategy; all need the report to say the precise thing once.

| # | Texts in tension | Reading that makes them true together | Verdict | What the report must do | Numbers needed |
|---|---|---|---|---|---|
| D1 | Pitch: "Yet another Treasury fund will decide the floor of her facility contribution, and a world stock ETF will determine the ceiling." (IPS l.3); TNA: "They only set how far her gift rises above her promised minimum." (TNA l.21) against "half of the value of the shares will be promised to no one" (IPS l.15) | VT's value at the move date sets the ceiling through the promised half only; the kept half is never in the ceiling; "only" means VT never touches the minimum. VT has a second job (flexibility) that only the IPS names | Reconcilable | State the ceiling as floor plus the promised half; show the kept half separately | Promised half at the move date |
| D2 | "IBTM does two jobs in Laura's plan." (TNA l.13) against separate steps: the first deposit buys the ten (IPS l.13); "Most of the 2028 deposit will fund a Treasury fund maturing in late 2032" (IPS l.15); "Yet another Treasury fund" (IPS l.3) | The same fund is bought twice: Jan 2027 as the 2033 rung, Jan 2028 as the floor. WInS lists no Treasury maturing Feb 2031 to Feb 2036, so IBTM is the only fit for both. WInS has one $300k account, so both lots sit in one position (4,503 shares; team record 1,142 rung and 3,361 floor, `.../trading_notes.csv` l.63) | Reconcilable | Show two lots, two dates, two jobs; the payment lot comes first | Lot sizes and payouts in the plan |
| D3 | "At current yields, this would cost roughly $300,000 – in other words, your entire first deposit." (IPS l.13) against the WInS book: $300k of virtual cash holding VT at 8.6% and the floor shares (SNAP l.36) | WInS shows Laura's plan after both deposits, scaled by 300/450 (team record, `caplet/google_drive/notes_and_discussions.md` l.307-308); each WInS rung holds 67-72% of a full rung (`holdings_ladder.py`, 5 Nov prices). The notes disclose it once: "scaled to the model portfolio" (WN l.24) | Reconcilable if explained once | Explain the scale once, plainly; never call the WInS book "Laura's portfolio"; never add WInS gains to projections (case l.132-133) | Scale factor; a book-to-plan table |
| D4 | "a rise before 2031 lifts the top of the range co-sponsors hear" (TNA l.21) against "Before you meet co-sponsors in 2031, the other half will move into Treasuries" and "markets will be able to increase or decrease the top of your planned band as we get closer to 2031" (IPS l.15) | A rise lifts the top only until the move; it lifts it by half of VT's gain (the promised half); after the move VT no longer moves the top | Reconcilable | Name the move's timing (before the first 2031 meeting) and show the top fixed after it | Top at the move date; its sensitivity to VT |
| D5 | "Held to the end, these pay what they say" (IPS l.13), said of "T-Bonds or iShares iBonds Term Treasury ETFs" (IPS l.13), against "their terminal payout is a net asset value, as opposed to a promise of par" (TNA l.15) and "although the final payout is not fixed" (TNA l.13) | T-bonds pay what they say; iBond ETFs pay what they hold. The TNA is the precise statement and the IPS the plain one | Reconcilable by explanation; the closest thing to a conflict in the canon | Use the TNA's precision; give the measured gap | NAV gap |
| D6 | "each maturing just before it’s needed" (IPS l.13) against "The 10.5-month gap" (TNA l.5) and "for 7.5 months" (WN l.17) | "Just before" means never after; two rungs end early and their money waits in a short-term Treasury ETF | Reconcilable | A gap table for all ten rungs | Gap days; waiting-money earnings |
| D7 | "a nominal Treasury matches the liability perfectly" (TNA l.7) and "rests on a dedicated instrument (not merely a forecast)" (TNA l.15) against "creates reinvestment-rate risk" (TNA l.5), "reinvested coupons fund the rest" (WN l.18) and "with reinvested coupons funding part of each" (WN l.24) | "Perfectly" is about nominal against real, not timing; reinvestment is a separate risk the texts name themselves. The IPS has no rule for a reinvestment shortfall, and the report cannot add one (A34) | Reconcilable; the largest open number (`CASE_MAP.md` C1) | Size the risk, explain it, implement only within the IPS's words | Reinvestment shortfall under falling-rate paths, per rung and in total |
| D8 | "none of your 10 operating payments will depend on a share price, or on anybody else’s money" (IPS l.11) against "we’ll simply complete it with the 2028 deposit" (IPS l.13) and the IPS's own claim that her income comes "later and smaller" in a recession (IPS l.9) | The 2028 deposit is Laura's own money, so the definition holds. But full funding now leans on a deposit the IPS calls recession-sensitive, and recessions tend to bring lower yields, which raise the top-up (Q1 card row 48). On 6 Nov the top-up is $1,544 (MODEL), about 1% of the deposit | Reconcilable; the risk must be shown | Show the top-up as a share of the deposit under falling yields and a smaller deposit | Top-up against deposit size, grid |
| D9 | "There are only 2 possible reasons we would change our plan – a missed deposit or a Treasury default." (IPS l.17) against a deposit that arrives smaller, not missed (no submitted text covers it) | A smaller deposit is not a reason to change; the plan's own order still runs (complete the ladder, then most to the floor fund, the rest to VT), so the floor and VT shrink | A gap in the canon, not a conflict | Say what the existing order does; add no rule | Smaller-deposit cases |
| D10 | "the bottom will remain constant" (IPS l.15) against "although the final payout is not fixed" (TNA l.13) and the floor fund being bought only in 2028 (IPS l.15) | Constant against share markets; set at the Jan 2028 purchase; moving only by the NAV difference after that | Reconcilable | Date the bottom (from Jan 2028) and size its NAV difference | Floor size against Jan 2028 yields; NAV gap |
| D11 | "your portfolio should be a counterbalance to that – definitely not a contributor" (IPS l.9) against holding VT, while "shares fall" in a recession (IPS l.9) | The counterbalance covers promised money; VT holds only money "you haven’t promised yet" (IPS l.11), and half of it moves to Treasuries before 2031 | Reconcilable | Show VT as a small, bounded sleeve | VT's share of the plan |
| D12 | "half of the value of the shares will be promised to no one. That is your flexibility – for building costs that overrun, a stronger Taiwan dollar or a co-sponsor falling short." (IPS l.15) against the case's test of confidence that "her 2033 contribution will fall within that range" (case l.117-118) and "They only set how far her gift rises above her promised minimum" (TNA l.21) | If the kept half is later spent on the building, the money reaching the facility could exceed the range announced in 2031. Reading: the facility contribution is what is promised (floor to floor plus the promised half); any later spending from the kept half is Laura's separate choice, outside the announced range | Not a conflict if defined; the most delicate definition in the canon | Define "facility contribution" once, so the confidence statement and the kept half cannot collide | None beyond A30 |
| D13 | "Some years, WInS lists no Treasuries maturing – so we purchased iShares iBonds" (TNA l.15) against "whichever works best for each year" (IPS l.13) | Forced for 2032-2035 (no WInS T-bond Feb 2031 to Feb 2036); a choice for 2036 (IBTR over the Feb-2036 bond, `.../trading_notes.csv` l.15); T-bonds forced for 2037-2041 (no iBond Treasury fund ends 2037-43, B38) | Reconcilable | One line per rung on why that instrument | None |
| D14 | "whatever figure you choose" and "the top of your planned band" (IPS l.15) and "the range co-sponsors hear" (TNA l.21) against the case's demand for a "range" and a confidence (case l.115-118) | In 2031 Laura announces a range inside the owned band; any figure inside it is owned money | Reconcilable | Give a range and a confidence, as the case asks, from the owned band | The 2031 range; its confidence |
| D15 | Filled IBTR note: "about 0.2 percentage points" (WN l.15) against the cancelled IBTR note: "0.3 percentage points" (WN l.37); both visible in WInS | Two estimates on two days; only the filled-order note is attached to a trade | TRUE CONFLICT in visible text (minor, dated) | Never quote either as current; if needed, give date and basis (B29) | None |
| D16 | "it’s the only investment not standing between Laura and a payment deadline" (TNA l.23) against the floor lot of IBTM (TNA l.13), which serves no payment either | "Investment" means share holding; in WInS the single IBTM position does support the 2033 payment | Reconcilable | Say "the only share holding" in notes | None |
| D17 | "this is one of the first payments we would top up" (WN l.20) against "we’ll simply complete it with the 2028 deposit" (IPS l.13), which names no order | The WInS note adds detail the IPS leaves open | Reconcilable | Keep IBTO among the first rungs completed in any top-up account | Which rungs wait a year |

---

## Table E. The frozen WInS book: what it shows and what it cannot show

Holdings as of the 23 Oct export (SNAP l.19-33); no trade since 8 Oct (SNAP l.71); trading froze 6 Nov. Values are
23 Oct WInS figures, not the frozen-day values (no later export is in the repo).

| Holding (SNAP line) | Quantity; paid; 23 Oct value | What it stands for in Laura's plan | What the book shows | What it cannot show |
|---|---|---|---|---|
| IBTM, iBonds Dec 2032 (l.22) | 4,503 sh; $21.65; $99,313.67 (32.5%) | Two lots: the 2033 rung (Jan 2027) and the floor fund (Jan 2028). Team record: 1,142 rung, 3,361 floor shares (`.../trading_notes.csv` l.63) | One fund doing both jobs (TNA l.13); the snapshot's "Pays for" column reads "2033 payment + floor stand-in" | Two purchase dates; which shares are which; the Dec 2032 NAV payout; the payment-first order |
| IBTO, Dec 2033 (l.23) | 1,024 sh; $22.86; $23,936.00 | 2034 rung | A fund standing in where WInS lists no 2033 Treasury | The Jan 2028 top-up it may receive (WN l.20) |
| IBTP, Dec 2034 (l.24) | 927 sh; $23.90; $22,725.59 | 2035 rung | As above | NAV payout |
| IBTQ, Dec 2035 (l.25) | 894 sh; $23.46; $21,594.48 | 2036 rung | As above | NAV payout |
| IBTR, Dec 2036 (l.26) | 853 sh; $23.24; $20,450.68 | 2037 rung (chosen over the 4.5% Feb-2036 bond) | The choice in D13 | NAV payout |
| T-bond 4.75% 15-Feb-2037 (l.27) | 20 units ($20,000 face); $960.190 per unit; $19,522.68 | 2038 rung | Latest listed bond before 2038 (B18) | The 10.5-month wait in a short-term Treasury ETF; coupon reinvestment |
| T-bond 4.50% 15-May-2038 (l.28) | 20 units; $930.763; $18,962.57 | 2039 rung | As above | The 7.6-month wait; reinvestment |
| T-bond 4.375% 15-Nov-2039 (l.29) | 18 units; $900.053; $16,552.34 | 2040 rung | Ends 47 days early | Reinvestment of coupons (WN l.18) |
| T-bond 4.25% 15-Nov-2040 (l.30) | 18 units; $877.240; $16,161.79 | 2041 rung | As above | As above |
| T-bond 3.125% 15-Nov-2041 (l.31) | 20 units; $749.550; $15,399.25 | 2042 rung | As above | As above |
| VT (l.32) | 167 sh; $158.83; $26,138.84 (8.6%) | The whole share fund, both halves, bought from the 2028 deposit in the plan | Shares as a small, separate sleeve; diversification in one fund | The split into halves; the 2031 move of the promised half into Treasuries; that VT is bought in 2028, not 2026 |
| Cash (l.10) | $3,513.79 (1.1%) | No role in the plan: fees and rounding | Cash kept small | WInS cash earns 0% (`competition/COMPETITION.md` l.86); Laura's waiting money would earn short-term Treasury rates |
| Not in the book | | Short-term Treasury ETF for waiting money (TNA l.5, WN l.17); Treasuries holding the promised half after the move (IPS l.15); the 2028 deposit and top-up (IPS l.13); the operating reserve from 2033 (IPS l.17) | | All of these |

Facts about the book to quote correctly:
- Portfolio value $305,557.66 and return 1.85% (SNAP l.13-14), shown only as evidence of implementation; WInS gains are
  never added to Laura's projections (case l.132-133). Quote portfolio value, not the "market value of long positions"
  line, which disagrees with the positions by $1,310 (SNAP l.63-65).
- 11 trades of 200 (SNAP l.15, l.66); every filled order dated 6-7 Oct ET (SNAP l.46-58).
- Weights: IBTM 32.5%, other iBonds 29.0%, T-bonds 28.3%, VT 8.6%, cash 1.1%, accrued interest 0.4% (SNAP l.36).
  At cost, the floor shares are 73% of floor plus VT (3,361 x $21.65 against 167 x $158.83), which fits "Most of the
  2028 deposit" (IPS l.15).
- The WInS pie chart labels the iBond ETFs "Long Equities", although the book is about 91% Treasuries
  (`competition/COMPETITION.md` l.117). Explain once.
- Accrued interest method UNVERIFIED (SNAP l.67-68): do not quote an accrued-interest figure.
- Bond prices update once a day (`competition/COMPETITION.md` l.108-109).
- The frozen-day value and the November iBond distributions are not in the repo: ask Ray for a post-freeze export
  (Keel never opens WInS).

### Notes visible in WInS, on cancelled orders

Judges can see these; they are not attached to any filled trade (SNAP l.43-58; WN l.33-40).

| Security | Cancelled order (ET) | Note text | How it differs from the filled-order note |
|---|---|---|---|
| IBTR | 10/06/2026 08:31:27 PM | "Future funding: IBTR is for Laura's fifth payment in 2037. On the 6 Oct Treasury curve, her first $300,000 is enough to buy Treasuries for all ten payments. If yields fall more than 0.3 percentage points by January, the 2028 deposit would top up the ladder, leaving less for the facility." (WN l.37) | "0.3" against "about 0.2" (D15) |
| B-T-4.750-15022037 | 10/06/2026 08:17:20 PM | "Future funding: we use the 4.750% Treasury maturing 15 Feb 2037 for Laura's 1 Jan 2038 payment because it is the latest WInS bond available beforehand. The 10.5-month gap creates reinvestment-rate risk only on the proceeds held in a short-term Treasury ETF." (WN l.38) | Adds "only" |
| B-T-4.500-15052038 | 10/06/2026 08:13:31 PM | "Future funding: we use the 4.500% Treasury maturing 15 May 2038 because it is the latest WInS bond before Laura's 1 Jan 2039 payment. Its proceeds stay in a short-term Treasury ETF for 7.5 months, so only part of the payment has brief exposure to short-term Treasury rates." (WN l.39) | Identical |
| B-T-4.375-15112039 | 10/06/2026 08:02:40 PM | "Future funding: the 4.375% Treasury maturing 15 Nov 2039 comes due 47 days before Laura's scaled 2040 payment. Held to maturity, its fixed coupons and principal cover most of it; reinvested coupons fund the rest. We chose Nov over May 2039 to mature closer to the payment." (WN l.40) | "scaled 2040 payment" against "$50,000 payment on 1 Jan 2040" |

---

## Ten checks for every later note or draft sentence

1. **No redesign.** Does it describe the plan exactly as submitted (first deposit to the ten; 2028: top-up, then most
   to the late-2032 Treasury fund, the rest to VT; half of VT promised to no one; the other half to Treasuries before
   2031; the Treasuries are the reserve from 2033), with no new rule, trigger, split or instrument?
2. **Two reasons only.** Does it add any reason to change beyond a missed deposit or a Treasury default (A34)?
3. **Instruments.** Is every instrument WInS-listed and allowed, with TIPS and STRIPS absent except as the TNA itself
   mentions TIPS?
4. **NAV, not par.** Does it say or imply an iBond ETF repays a fixed sum? It must say net asset value (TNA l.13, l.15).
5. **Certainty words.** Does each "immune", "without doubt", "constant", "perfectly", "guarantee" carry its exact
   meaning (Table C), never a retraction?
6. **Numbers.** Is every number dated, sourced and marked MODEL or fact, and does it match `NUMBERS.md`? (Ladder: $301,544
   on the 6 Nov close unless a newer curve is named; never "under $300,000".)
7. **Floor and range.** Is the floor the IBTM payout (not fixed, never "$150,000 fixed") and the range floor to floor
   plus the promised half, with the kept half outside it (D1, D12)?
8. **Flexibility.** Is the kept half named for overruns, a stronger Taiwan dollar and a co-sponsor falling short, with no
   contingency fund sized and no facility cost estimated?
9. **WInS.** Is the book shown as implementation at two-thirds scale of the plan after both deposits, with WInS gains
   kept out of projections and holdings as in Table E?
10. **Same words, same story.** Does it agree with the TNA and WInS notes (10.5-month gap; short-term Treasury ETF;
    "about 7.5% a year (as per JPMorgan)"; 0.06%; "about 10,000 stocks"; IBTO among the first top-ups) and with the
    IPS's own account of the team's change of mind, using real Caplet events only?

---

## Coverage index: every claim-bearing sentence and where it sits

| Source | Rows |
|---|---|
| IPS l.3 (pitch) | A1, A23; C1, C19, C20; D1, D2 |
| IPS l.9 | A2, A3; B1-B4; D8, D11 |
| IPS l.11 | A4, A5; B5; C9, C10; D8, D11 |
| IPS l.13 | A7, A8, A11, A19; B6-B10; C2-C4; D3, D5, D6, D13, D17 |
| IPS l.15 ("The building is a different matter." is framing only) | A22, A25, A28, A30-A32; B11, B12; C5-C8, C22; D1, D2, D4, D9-D12, D14 |
| IPS l.17 | A33, A34; D9 |
| IPS l.19 | A6; C21 |
| TNA l.5 (= WN l.16) | A13, A15; B17-B19; D6, D7 |
| TNA l.7 | A9, A14; B5, B25; C11-C15; D7 |
| TNA l.13 (= WN l.19) | A24; B20; D2, D5, D10, D16 |
| TNA l.15 | A10, A12; B21-B24; C2, C16-C18; D5, D7, D13 |
| TNA l.21 (= WN l.14) | A29; B13; D1, D4, D12, D14 |
| TNA l.23 | A26, A27; B14-B16, B26; D16 |
| WN l.15 (IBTR) | A20; B27-B29; D15 |
| WN l.17 (May-2038) | A16; B34, B35; D6 |
| WN l.18 (Nov-2039) | A17; B36; D7 |
| WN l.20 (IBTO) | A21; B27, B30, B31; D17 |
| WN l.21 (IBTP) | B27, B32, B33 |
| WN l.22 (IBTQ) | B27, B30, B31 |
| WN l.23 (Nov-2040) | B27, B37 |
| WN l.24 (Nov-2041) | A18; B27, B38, B39; D3, D7 |
| WN l.37-40 (cancelled orders) | Table E, last section; D15 |
| SNAP | Table E; D2, D3 |

## Could not be verified today

- WInS listings the notes rely on (Feb-2037 as the latest bond before 2038, May-2038 before 2039, no 2033 or 2035
  Treasury, no lower-coupon Nov-2040): team records only; WInS is off limits to Keel.
- Whether WInS lists a short-term Treasury ETF for waiting money (TNA l.5, WN l.17).
- IBTP's 0.07% premium on 2 Oct (WN l.21) and the Nov-2040 bond's 5 Oct price check (WN l.23).
- The basis of "about 0.2 percentage points" (WN l.15): 39bp on the payment-date basis for 6 Oct.
- J.P. Morgan's 7.5%: compound or arithmetic.
- Co-sponsor budgets falling in recessions (IPS l.9), and odd-lot bond liquidity (TNA l.15).
- Which filled order each note belongs to (13 Oct team record; the export does not say).
- The book's value on the freeze day.
