# A4 WInS week-1 guardrails (early run of D10, Compliance Officer)

Agent: A4, insight_v1 run. Written 2026-09-27 (the day before trading opens). Official sources win over everything
else here. This file is compliance research for the team. It has **no submission-ready text**: no trading notes, no IPS
wording, no reflections. It names **instrument types only** (no tickers). Every trade idea must still be checked
against this year's WInS rules and what WInS actually offers.

Status labels (brief section 3): **VERIFIED-PRIMARY** (I read it myself on the primary page on 2026-09-27; URL
given), **VERIFIED-REPO-FILE** (official file in this repo; path and line given), **SNIPPET-UNVERIFIED** (search snippet
or secondary website), **ASSUMPTION**, **INTERPRETATION** (my reading, not a fact). Season tags: **[2026-27]** = this
season; **[PRIOR]** = an earlier season, for background only.

---

## 0. Summary: the ten things to know before the first trade

1. **This year's trading rules are public and I read them myself.** SMApply "Trading Details" and "FAQs" pages
   (VERIFIED-PRIMARY [2026-27], read 2026-09-27 11:54 UTC) state: **$300,000** virtual cash; trading **Sept 28 to
   Nov 6, 2026**; **up to 200 trades**; each trade no larger than **twice the security's daily volume**; allowed
   instruments are **stocks priced at $5 or more, "Any ETF available on WInS", and Treasury bonds** (U.S., U.K.,
   Germany, France, Italy, Netherlands); **not allowed**: margin, short selling, stock-secured debt, crypto,
   derivatives, and "Anything other than the approved investments listed above"; **no sector minimum**. These
   pages confirm and extend what A1 recorded in `phase_A/case_register.md` (R-W56 to R-W95).
2. **There is no separate "approved ETF list" this year.** The rule is "Any ETF available on WInS". Last season was
   different: the 2025-26 WInS User Guide said "You are only permitted to buy ETFs from the approved lists"
   (VERIFIED-PRIMARY [PRIOR]). The file `competition/historical/2025_26/25-26-WGHIC-Approved-ETF-List.txt` is
   therefore **history, not a rule**. INTERPRETATION: last year's rule break may have come from exactly this kind
   of list rule. This year the trap is different: WInS may let you place an order that the written rules still
   forbid. Two examples: stocks priced between $3 and $5 (the generic Stock-Trak default minimum is $3; Wharton's is
   $5), and crypto funds.
3. **New finding: this season's WInS User Guide exists.** A "2026-2027-WInS-Userguide.pdf" was uploaded to the
   Wharton WInS portal on 2026-09-15 (PDF creation date 2026-09-15). I rendered its pages to check which text is
   actually visible. The visible text says: "Day Trading: This is not permitted." and "Position Limit: This is how
   much of your portfolio you can invest in one single stock." (VERIFIED-PRIMARY [2026-27]). It also says to check
   **Portfolio Summary > Session Rules** before trading.
4. **Position limit: open, and important for the current strategy.** This year's number is **not published
   anywhere public**. Stock-Trak's generic Wharton-portal FAQ says "The default position limit is 25%"
   (VERIFIED-PRIMARY, generic platform page, not season-specific). If a 25% limit per security applies, the current
   WInS mirror (about 65% Treasuries split roughly 64.8/35.2 between an intermediate and a long Treasury fund, so
   about 42% in one fund) **would be blocked**. It would need three or more Treasury instruments. **Read Session
   Rules on day 1 before the first order.**
5. **Day trading is not permitted** [2026-27 user guide]. The guide does not define it. ASSUMPTION (safe reading):
   never buy and sell the same security on the same U.S. trading day. This matters for rebalancing and for fixing
   mistakes. The FAQ also says: "If you make an error, we encourage you to run with it" (VERIFIED-PRIMARY).
6. **Trading notes are written at trade time and quoted word for word later.** Official: "Include each Trading Note
   exactly as it appears in WInS." / "The Trading Notes must correspond to trades executed in WInS. Yes, we will
   verify this." (VERIFIED-REPO-FILE, Trading Notes guide p.2 L44, L53). SMApply WInS page: notes "should record the
   reasoning, research, and intended strategic role of each decision at the time it is made" (VERIFIED-PRIMARY).
   **No character limit is published anywhere I could reach** (it is not in the 2026-27 guide or on the public pages).
   Stock-Trak's own 2017 description says students "cannot edit or delete their trade notes" (VERIFIED-PRIMARY,
   vendor blog, not season-specific). Assume the note is permanent.
7. **Only executed trades count.** An order placed after the U.S. close on Nov 6 would fill at the next open. By then
   the portfolio is frozen. INTERPRETATION: that order never executes, and a note on an unfilled order cannot be one
   of the three notes.
8. **The AI policy lets you brainstorm, requires AI use to be recorded, and bans AI-written deliverables.** The
   Wharton AI policy page adds a line the Rules page lacks: "If you use AI to assist you in any way during the
   competition, how you use it must be recorded in your Works Cited pages." (VERIFIED-PRIMARY). See section 4.
9. **Disqualification and exclusion risks are listed with exact sources in section 5.** The biggest are: contacting
   Laura; IPS format errors ("will not be considered for semifinal selection"); missed deadlines (no extensions);
   team size below 4 or above 6; paid help; plagiarism and AI misuse; notes that do not match executed trades.
10. **The third-party "rules" in CLAUDE.md are outdated.** "Sector minimum = team size" and "first trade by a
    deadline" trace to the **2023-24** season (Lumiere page quoting "October 13, 2023"; SNIPPET-UNVERIFIED [PRIOR]).
    This year's primary page says the opposite: "There is no required sector allocation or minimum number of
    sectors." The "200 trades" claim is now confirmed by the primary page.

---

## (a) What the official documents in the repo say

All quotes are VERIFIED-REPO-FILE [2026-27] from `competition/official/2026_27/`. Line numbers refer to the `.txt`
extractions. A1 checked their PDFs against the live Box files by SHA-256 (see `case_register.md` section 0.2).

### a1. Trading and the WInS portfolio
| # | Exact quote | Location | What it means (INTERPRETATION) |
|---|---|---|---|
| a1.1 | "The WInS portfolio represents each team’s implementation of its investment strategy during the competition." | Case p.4 L129-130 | WInS shows the strategy in action. Every trade must fit the strategy. |
| a1.2 | "It does not determine Laura’s actual portfolio value at the beginning of 2027." | Case p.4 L130 | WInS results never become her starting value. |
| a1.3 | "Gains or losses generated during the WInS trading period should not be added to or subtracted from Laura’s portfolio projections." | Case p.4 L132-133 | Keep WInS profit and loss (P&L) out of every projection. |
| a1.4 | "Successful investing is not simply about selecting individual stocks. It requires making disciplined decisions that consistently support an overall investment strategy." | Trading Notes (TN) guide p.1 L7-8 | Stock-picking stories are not the aim. |
| a1.5 | "Throughout the competition, your Trading Notes should document the research, analysis, and reasoning behind your investment decisions." | TN p.1 L8-9 | Every trade gets a note, not just the three you pick later. |
| a1.6 | "you should already be using a clear strategic approach to guide your investment decisions." | TN p.1 L18-19 | Trades from day 1 should already follow a stated approach. |
| a1.7 | "The focus should be on the quality of your reasoning and the intended role of each decision, not simply whether an investment gained or lost value during the competition." | TN p.1 L15-16 | Say what role each trade plays. Returns do not matter for the notes. |

### a2. Trading notes and verification against executed trades
| # | Exact quote | Location |
|---|---|---|
| a2.1 | "Select three (3) Trading Notes from trades your team executed in WInS." | TN p.2 L42 |
| a2.2 | "Include each Trading Note exactly as it appears in WInS." | TN p.2 L44 |
| a2.3 | "For EACH Trading Note, write a reflection of 100 words or fewer explaining: – Why your team made the investment decision. – How the decision aligned with your overall investment strategy. – How the decision supported the client’s goals, funding needs, or risk considerations." | TN p.2 L46-52 |
| a2.4 | "The Trading Notes must correspond to trades executed in WInS. Yes, we will verify this." | TN p.2 L53 |
| a2.5 | "The Trading Notes you select do not need to correspond to investments that remain in your portfolio at the end of the competition." | TN p.1 L25-26 |
| a2.6 | "The analysis should be consistent with the strategic approach your team is developing and will later articulate in its IPS." | TN p.1 L30-31 |
| a2.7 | "At this stage, your team is not expected to calculate the final size of the operating reserve, complete long-term portfolio projections, determine Laura’s facility contribution, or draft her communication to co-sponsors." | TN p.1 L20-22 |
| a2.8 | Example note: "We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin preparing for Laura’s future operating commitment. The position provides income and greater stability than equities, although interest-rate changes may affect its value. This trade supports our plan to balance continued growth with reliable future cash flows as the residency funding date approaches." | TN p.2 L36-39 |
| a2.9 | "Your team will submit their trading notes via the SurveyMonkey Apply form." | TN p.2 L54 |

DERIVED (my own count): the example note has 59 words and 413 characters. This is the only length signal in the
official files. No character limit is stated in any repo file.

What "verify" implies (INTERPRETATION): Wharton can see the team's WInS account, so it can compare each quoted note
with the trade it is attached to. A note quoted with any change, or taken from a practice trade or an unfilled
order, would fail that check.

### a3. The WInS username
| # | Exact quote | Location |
|---|---|---|
| a3.1 | "WInS username" / "– This is the team’s username for logging into the WInS platform." | IPS guide p.3 L98-100 |
| a3.2 | Sample title page: "WInS Username: sample_team-1234567" | IPS guide p.4 L131 |

Public source, same topic (VERIFIED-PRIMARY [2026-27], SMApply FAQs, https://wghsinvcomp.smapply.us/res/p/faqs/,
read 2026-09-27): "No. Your team’s username is only used to access WInS. Your team username is NOT the same as your
team name." The 2026-27 WInS User Guide p.4 also says "you will not be able to change your team’s username."

### a4. The portfolio lock
| # | Exact quote | Location |
|---|---|---|
| a4.1 | "Investment Policy Statement (Due: November 6; no later than 5:00 p.m. ET) * IMPORTANT: Trading ends and your portfolio is locked." | SMApply Deliverables transcription L10-11 |
| a4.2 | "Once submitted, the IPS becomes the official record of your team’s investment strategy. Your team may not revise its investment strategy after the submission deadline." | IPS guide p.2 L73-74 |
| a4.3 | "Your portfolio and Final Report should reflect the strategy established in your IPS." | IPS guide p.2 L75 |
| a4.4 | "Your team will formally present its investment strategy in the Investment Policy Statement (IPS) in Week 6." | TN p.1 L17 |

### a5. IPS format rules (breaking any = "will not be considered for semifinal selection")
| # | Exact quote | Location |
|---|---|---|
| a5.1 | "Please follow these directions carefully. Submissions that do not meet the requirements below will not be considered for semifinal selection." | IPS p.3 L82-83 |
| a5.2 | "Page 1: Title Page / 1 page maximum" | IPS p.3 L84-85 |
| a5.3 | "Official team name – This should be the same as what you submitted with your official team roster." | IPS p.3 L88-90 |
| a5.4 | "Finalized team member names – These should be the same as what was submitted with your official roster. • Format: First Name, Last Initial" | IPS p.3 L92-96 |
| a5.5 | "WInS username" | IPS p.3 L98 |
| a5.6 | "Pages 2 and 3: Investment Strategy / 2-page maximum" | IPS p.3 L103-104 |
| a5.7 | "Investment Strategy Elevator Pitch, maximum 50 words" / "Investment Policy Statement, maximum 500 words" | IPS p.3 L107-109 |
| a5.8 | "Font: Times New Roman" / "Size: 12-point" / "Spacing: Double-spaced" / "Margins: 1 inch on all sides" | IPS p.3 L112-118 |
| a5.9 | "Submit as a PDF through SurveyMonkey Apply." / "Maximum file size: 5 MB." | IPS p.3 L120-122 |
| a5.10 | "Graphics, charts, images, attachments, external links, footnotes, and formal citations are not permitted." | IPS p.3 L123 |
| a5.11 | "sources do not need to be cited in the IPS. Relevant sources and supporting evidence must be included in the Final Report." | IPS p.3 L124-125 |
| a5.12 | "Formatting choices not specified below are left to the team’s discretion." | IPS p.3 L101 |
| a5.13 | Sample: "Jordan A. \| Taylor B. \| Casey C. \| Morgan D." | IPS p.4 L130 |

Note: 500 words, double-spaced, 12-point, on at most 2 pages together with a 50-word pitch is tight. ASSUMPTION: at
roughly 250-300 double-spaced words per page, 550 words with headings may not fit on two pages. The team must test
the layout early.

### a6. Final Report format
| # | Exact quote | Location |
|---|---|---|
| a6.1 | "Instructions: Detailed Final Report instructions and requirements will be shared on November 9." | SMApply L44 |
| a6.2 | "Detailed Final Report requirements will be released at the beginning of Week 7." | Case p.4 L162-163 |
| a6.3 | "We require official documentation from your school ... This will be submitted along with your Final Report as a separate file." / "Sample Documentation: Coming soon" | SMApply L45-46 |
| a6.4 | "Evaluators will consider the three deliverables together." | Case p.4 L161 |

**The Final Report's format rules are not yet published.** Nothing about its length, font or charts can be known
before Nov 9.

### a7. Deadlines and submission (all deliverables)
"All deliverables must be submitted via your team's SurveyMonkey Apply account." / "We will not grant any deadline
extensions." / "Team must submit all the deliverables, and meet their necessary requirements, in order to receive a
digital credential." (SMApply L14-17). "Once your official team roster is submitted, teams may not change their
members." (SMApply L22).

---

## (b) What the public web says (searched 2026-09-27, 11:50-12:00 UTC)

### b1. VERIFIED-PRIMARY [2026-27]: read on the page myself
Pages were fetched with curl through the session proxy and the text was taken from the HTML. Access date for all:
2026-09-27.

**SMApply "Trading Details"**, https://wghsinvcomp.smapply.us/res/p/trading/ (public, no login needed)
- Starting cash: "Your team will begin the official trading period with $300,000 in virtual cash."
- Account: "Each team shares one WInS account. All team members will use the same username and password."
- Dates: "Official trading begins on September 28, 2026, and ends on November 6, 2026. When trading ends, your
  portfolio will be frozen, and your team may no longer trade or change its holdings."
- "The $300,000 is your team’s WInS simulator balance. The additional $150,000 contribution described in the Client
  Case Study will not be added to WInS."
- "WInS gains and losses should not be added to or subtracted from the client’s long-term portfolio projections."
- Execution: "You may enter buy and sell orders at any time during the official trading period." / "Orders placed
  while the market is closed are filled at the security’s opening price when the market reopens." / "Prices
  displayed for open positions may be delayed by 10 to 15 minutes." / "International equity orders may experience
  a longer delay and are processed at the end of the applicable trading day." / "WInS automatically completes
  foreign-currency conversions ... exchange-rate movements may affect the value of your holdings."
- Trade limits: "Your team may make up to 200 trades during the competition." / "Your team may trade an amount equal
  to no more than twice a security’s current daily trading volume."
- Approved securities: "Stocks: Any stock available on WInS priced at $5 or more, or the equivalent of $5 in its local
  currency." / "Exchange-Traded Funds: Any ETF available on WInS." / "Treasury Bonds: Bonds available on WInS. The
  list includes Treasury bonds from the United States, United Kingdom, Germany, France, Italy, and the Netherlands."
- Sectors: "There is no required sector allocation or minimum number of sectors. However, diversification remains an
  important investment principle." / "The goal is to build an intentional mix of investments appropriate for your
  strategy, not simply to own a large number of securities."
- "The competition does not require frequent or same-day trading. Make thoughtful, well-researched decisions and
  record the reasoning behind them in your Trading Notes."

**SMApply "FAQs"**, https://wghsinvcomp.smapply.us/res/p/faqs/
- "Your team will be responsible for managing a portfolio of $300,000 in virtual cash."
- "DOES THE COMPETITION ALLOW ALL SECURITIES? No. Investments permitted (for BOTH contributions): Cash / Any stock from
  any exchange available on WInS priced at $5 (or the equivalent of $5 in the local currency) or higher. / Any
  Exchange-Traded Funds (ETFs) available on WInS. / Any Government/Treasury Bonds from any exchange available on WInS.
  The following are NOT permitted: Margin trading / Short selling / Stock-secured debt / Crypto / Derivatives
  (options, futures, swaps, etc.) / Anything other than the approved investments listed above."
- "Each stock transaction is charged a flat $25 commission and treasury bonds are charged $10. Commission is charged
  only on a trade that clears."
- "The bond prices are updated once daily at U.S. market open, and pay out every six months."
- "You can only cancel open orders." / "If you make an error, we encourage you to run with it and not scramble to
  “fix” it. Trading errors are part of the learning process."
- "Students should place trades on WInS, NOT the advisor. ... It should be a team decision. We strongly encourage
  teams to identify different roles for each team member."
- "you should not be doing a lot of buying and selling of the stocks designated for the long-term portion of your
  portfolio"
- "When your team logs in to the shared WInS account, they’ll find tutorial videos, a user guide, and FAQs under
  “Getting Started”"
- "Additionally, teams must meet the required trading activity and portfolio management guidelines throughout the
  competition." (No minimum amount of activity is defined on any public page.)

**SMApply "Wharton Investment Simulator (WInS)"**, https://wghsinvcomp.smapply.us/res/p/wins/
- "You are not being evaluated based on: Your portfolio ranking / How many trades you make / Whether you outperform
  other teams / Whether your portfolio makes money during the competition"
- "All account activity will be cleared after the practice session. Practice trades, portfolio activity, gains and
  losses, and account balances will be reset before official trading begins on September 28."
- "Official trading will end on November 6, when your Investment Policy Statement is due. At that time, your WInS
  portfolio will be frozen"
- "Your portfolio should reflect a cohesive strategy designed around the client’s goals. Each investment decision
  should have a clear purpose within that strategy."
- "Complete a Trading Note when your team makes an investment decision. Your Trading Notes should record the
  reasoning, research, and intended strategic role of each decision at the time it is made."
- "Access WInS: https://edu.stocktrak.com/wharton/"

**2026-2027 WInS User Guide (new finding)**,
https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf
(found through the portal's public media listing; upload date 2026-09-15; PDF creation date 2026-09-15; 18 pages;
SHA-256 19d797dfa6269aeec312797e50cf0d98e7547d5b2bfb97f14b76f8d64229a84e). Caution: the file keeps hidden text from
older versions, including the 2024-25 "approved lists" and "70%" rule. I rendered pages 6, 7, 10, 11 and 17 to images
and quote **only the text that is visible**.
- p.5: "how many of your allotted 200 trades your team has used."
- p.6: "Before you start trading, you might want to check your specific trading parameters set by Wharton Global Youth
  Program ... go to ‘Portfolio Simulation’ and click ‘Portfolio Summary’. Then, click ‘Session Rules’." /
  "Wharton Global Youth Program sets the currency, starting cash, interest rates, commission charges, trading dates,
  and a few more rules: Position Limit: This is how much of your portfolio you can invest in one single stock. Day
  Trading: This is not permitted. Short Selling: This is not permitted. Allow trading on margin: This is not
  permitted." (The screenshot on this page is dated 9/17/2024. It shows "Total Trades Allowed 200", "Day Trading
  Allowed No", and a bond "Position Limit (Single Position) 100%". It shows no equity position limit. It is [PRIOR]
  evidence.)
- p.7: "Remember: The Investment Competition primarily involves the buying and selling of stocks, exchange-traded funds
  (ETFs) and a limited number of treasury/government bonds."
- p.10: "Enter a Trade Note (these are important!) to discuss how the purchase fits into your overall strategy." The
  screenshot (dated 2023) shows the banner "You are required to write a TRADE NOTE explaining each trade." and a
  "View Example" link. No character counter is visible.
- p.11: "Once you are on the trading page, select the symbol of the treasury bond you would like to trade get a quote.
  ... When you buy a bond in between coupon dates you will have to pay accrued interest to the seller."
- p.4: "you will not be able to change your team’s username. Your team’s username is only used to access WInS. Your
  team username is NOT the same as your team name."

**Wharton Global Youth public pages** (globalyouth.wharton.upenn.edu):
- Main page, /competitions/investment-competition/: "September 28 Competition begins; first day of trading" ...
  "November 6 Deliverable: Investment Policy Statement (IPS) must be submitted as instructed (5:00 p.m. ET)"; "a free,
  experiential investment challenge for high school students (9th to 12th grade)"; "Students work in teams of four
  to six, guided by a teacher from their school as their advisor".
- Rules & Roles, /competitions/investment-competition/rules-roles/ (eligibility and advisor role):
  - "Teams must be composed of current students from the same high school."
  - "Each team must designate one student team leader who is at least 16 years old at the start of the Competition.
    No exceptions will be granted. Team leaders may not be changed after the Competition begins on September 28, 2026
    unless the Advisor submits a written request due to extenuating circumstances and receives approval".
  - "The Advisor’s role is to provide guidance, encouragement, and educational support throughout the Competition.
    Advisors may not make decisions on behalf of students or actively participate in team activities, trading
    decisions, or strategy development."
  - Advisors are responsible for: "Monitoring team engagement and portfolio activity." / "Serving as a sounding board
    without completing work on behalf of students."
  - "Teams may seek guidance from a parent, industry professional, or other adult serving as a secondary advisor,
    provided the team also has a primary teacher Advisor. However, the use of paid advisors, education consultants,
    or other agents is prohibited."
  - "Teams must meet the required trading activity and portfolio management guidelines throughout the competition."
  - "To remain eligible for the Semifinals and Global Finale, teams must meet all competition requirements and submit
    the competition deliverables by the published deadlines."
  - "The top 50 teams will be selected as semifinalists based on the strength of their Investment Policy Statement
    (IPS) and Final Reports." (The SMApply page says the Trading Notes Analysis is also evaluated. A1 logged this
    conflict as X-8.)
- FAQ, /competitions/investment-competition/faq/: "Any student on the team may serve as the team leader, provided they
  are at least 16 years old on the first day of the Competition (September 28, 2026)." / "Copies of the weekly emails
  will also be posted on the Wharton Investment Simulator (WInS) for all team members to view."
- AI policy: see section (d).

**Stock-Trak pages** (the WInS vendor; platform facts, **not season rules**):
- Wharton WInS portal FAQ, https://edu.stocktrak.com/wharton/portfolio-faq/ (page last modified 2023-08-10):
  "Trading Notes are comment and explanations that must be added to each trade." / "The default position limit is 25%
  which means you cannot put more than 25% of your portfolio value in a single security. Please note that only
  professors have the ability to change the position limit for their classes." / "Minimum Stock Price: The minimum
  stock price must be $3.00 or higher" / "we only allow users to trade up to half of the volume of any security on
  the market." Use: this shows what the platform does by default. Wharton's written rules (a $5 minimum) come
  first, and Session Rules shows this year's actual settings.
- "New Feature – Trade Notes", https://www.stocktrak.com/new-feature-trade-notes/ (Stock-Trak blog, July 10, 2017):
  "students cannot edit or delete their trade notes ... they can add more notes to the same trade (each note has its
  own timestamp for a record of when each note is added)." This conflicts with the 2024-25 and 2025-26 WInS guides
  ("Trade Notes will let you add/edit trade notes." [PRIOR]). The 2026-27 guide dropped that line. Treat every note
  as **permanent and time-stamped**.

### b2. [PRIOR] facts from earlier seasons (history only; not this year's rules)
| Fact | Source | Status |
|---|---|---|
| 2025-26 virtual cash: "$500,000 in virtual cash, up from $100,000" | Wharton news, https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/ (Jan 27, 2026) | VERIFIED-PRIMARY [PRIOR] |
| 2025-26: "Remember: You are only permitted to buy ETFs from the approved lists." / "Teams may use stocks (no approved list) and ETFs and treasury bonds from the approved lists" | 2025 WInS User Guide, https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2025/09/2025-WInS-User-Guide.pdf, p.7 and p.11 | VERIFIED-PRIMARY [PRIOR] |
| 2024-25: "Teams must still have at least 70% of their total stock allocation from the approved list." | 2024 WInS User Guide p.7 | VERIFIED-PRIMARY [PRIOR] |
| 2025-26 approved ETF list (100 ETFs) | `competition/historical/2025_26/` | VERIFIED-REPO-FILE [PRIOR]; **not a 2026-27 rule** |
| 2024-25 Session Rules screenshot: trading 09/30/2024-12/06/2024 4:00 PM; 200 trades; no day trading; bond position limit 100% | 2026-27 guide p.6 image | VERIFIED-PRIMARY image [PRIOR] |

### b3. SNIPPET-UNVERIFIED third-party claims (do not act on these)
| Claim | Where it came from | Verdict |
|---|---|---|
| "Each team must invest in a number of sectors equal to the number of team members" | WebSearch summary (2026-09-27) citing third-party guides. Lumiere Education page (read directly; published 2023-08-05) gives it as a 2023-24 criterion: "the portfolio is invested in at least as many sectors as there are team members." | **[PRIOR] and contradicted for 2026-27** by the primary "There is no required sector allocation or minimum number of sectors." |
| "First trade by" a deadline (CLAUDE.md: "by Oct 10") | Lumiere: "teams must fully execute at least one trade on WInS by close of the U.S. markets (4:00 p.m. ET) on October 13, 2023" | **[PRIOR]**. No 2026-27 primary page states a first-trade deadline. ASSUMPTION: the team trades in week 1 anyway, so it is safe either way. |
| "Each team starts with $500,000" for 2026-27 | WebSearch summary citing Aralia. I read the Aralia page directly and the figure is **not on it**. | **Wrong**: the primary figure is $300,000. |
| "A minimum of four and a maximum of seven members" | WebSearch summary | **Wrong for 2026-27**: primary says "four to six". |
| "trading period begins on September 30 at 9:30 AM" | WebSearch summary | [PRIOR] (2024 season). This year: Sept 28. |
| "200-trade cap" | Third-party | Now **VERIFIED-PRIMARY [2026-27]**. |

### b4. What I could not find
- **The 2026-27 position limit, the exact end time on Nov 6, and the trading-note character limit** are on no public
  page. They are probably on the logged-in Session Rules page and trade screen (see section f).
- No separate 2026-27 "approved list" exists on any public page. The public rule is "any ETF available on WInS".
- Blocked or unreachable: app.raena.ai (connection failed); www.aralia.com through WebFetch (egress blocked, but curl
  reached it). The logged-in SMApply and WInS pages cannot be reached from here.

---

## (c) "Before every trade" checklist (week 1 onward)

Print this. One person reads each line aloud and a second person ticks it. Instrument types only. **Every item means:
confirm against this year's WInS rules and Session Rules.**

**A. Is the instrument allowed?**
1. [ ] The instrument type is one of: a stock priced at **$5 or more** (local-currency equivalent), an **ETF available
   on WInS**, or a **government/Treasury bond available on WInS**, or cash. *(SMApply Trading Details and FAQs.)*
   Confirm against this year's WInS list and rules.
2. [ ] It is **not** margin, a short sale, stock-secured debt, crypto, or a derivative (options, futures, swaps), and
   it is not "anything other than" the listed types. Do not trade it just because WInS lets you place the order.
   Types to avoid unless Wharton confirms in writing (INTERPRETATION of "ETF" and "Crypto"): exchange-traded notes
   (ETNs, which are not ETFs), closed-end funds, mutual funds, crypto-linked ETFs, and leveraged or inverse ETFs
   (they use swaps and futures). Confirm against this year's WInS rules.
3. [ ] It is not one of last year's list rules applied by mistake, **and** it is not assumed to be allowed because it
   was on last year's list. The 2025-26 list is history only.
4. [ ] For an individual Treasury bond: it appears in the WInS **Bonds** drop-down; you have noted the face value,
   price, last coupon date and **accrued interest** (the interest built up since the last coupon, which the buyer
   pays). Bond prices update only once a day at the U.S. open. Commission is $10. Confirm against this year's WInS
   rules.

**B. Do the rules allow this size and timing?**
5. [ ] Session Rules checked this week (screenshot saved in the decision log): position limit per security **and**
   per security type, trades allowed, day trading, dates and times. After this trade, **no single position exceeds
   the position limit**. Confirm against this year's Session Rules.
6. [ ] **Not a day trade**: we have not bought or sold this same security earlier today (U.S. trading day).
   ASSUMPTION: this is the safe reading of "Day Trading: This is not permitted." Confirm against this year's WInS
   rules.
7. [ ] Order size is **no more than twice the security's daily volume**. ASSUMPTION: for a thinly traded fund, keep
   well below this.
8. [ ] Trade count: we are within 200 total and are keeping a reserve (ASSUMPTION: at least 50 left for Oct 23 to
   Nov 6).
9. [ ] Timing: from Australia, an order placed during the day fills at the **next U.S. open** (for example, 9:30 a.m.
   ET Monday 28 Sept = 11:30 p.m. Sydney time). No order depends on filling after the **U.S. close on Friday Nov 6**
   (08:00 Sat 7 Nov Sydney time, ASSUMPTION about the end time). For a trade meant to be one of the three notes,
   make sure it has **filled** (status "Filled" in Order History) well before Oct 23.
10. [ ] Order type chosen on purpose (market or limit). Remember the FAQ: "You can only cancel open orders" and "run
    with" errors. No quick buy-then-sell fixes.

**C. Is the note right, before the order is sent?**
11. [ ] **The note was drafted and agreed before the order was placed**, in the team's own words (no AI-written
    text; see section d). It says the instrument **type**, its **role** in the strategy, and how it serves Laura's
    goals, funding needs or risk. *(TN guide; SMApply WInS page: "at the time it is made".)*
12. [ ] It uses the **same strategy words the IPS will use**. These are the official vocabulary: growth, risk,
    liquidity, funding reliability, financial flexibility, future cash-flow needs, operating commitment, operating
    reserve, facility contribution. *(TN p.1 L4-6; IPS p.1 L20-26.)* The team keeps a one-page glossary of its own
    words and uses it for every note.
13. [ ] **Nothing in the note contradicts the plan**: no hot-theme, momentum or single-stock story that the IPS will
    not support. No claim about WInS profit being added to Laura's projections. No reserve size, facility amount or
    co-sponsor range (not expected yet; TN p.1 L20-22). No "our advisor decided" (advisors may not make decisions).
14. [ ] No personal details about Laura. Nothing that looks like contacting her. Only case facts and public
    professional record.
15. [ ] Length: short and complete. The example is 59 words and 413 characters. **Assume the note cannot be edited
    after it is saved** until the team has confirmed otherwise in WInS.
16. [ ] Spell-checked in a separate document first, then pasted. What is in WInS is what will be quoted "exactly".

**D. Record it (decision log)**
17. [ ] After the fill: copy the **note text exactly as WInS shows it** (character for character) into the team
    decision log, plus a **screenshot** of Order History and Transaction History showing date/time, symbol, quantity,
    price, status "Filled", and the note. Export Transaction History to Excel weekly.
18. [ ] The log records: who proposed, who checked (two names), which checklist items were checked, the rule
    source, and whether this trade is a **candidate for the three notes** (does it show strategy being applied,
    tested or refined?).
19. [ ] The log records **who placed the order**: a student, never the advisor ("Students should place trades on
    WInS, NOT the advisor").
20. [ ] If anything above is unclear: **do not trade**. Log the question and ask Wharton through the SMApply "Contact
    Us" route (the team leader is the contact; FAQ: "Please use the Contact Us form.").

---

## (d) AI-use policy: exact wording and what it means for this research

### d1. Exact wording (VERIFIED-PRIMARY [2026-27], read 2026-09-27)
**Rules & Roles, "Use of Generative AI"** (https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/):
> "Teams may use generative AI tools (such as ChatGPT) for brainstorming and idea generation. However:
> AI-generated content may be inaccurate, incomplete, or misleading and should be used with caution. / AI-generated
> work may not be submitted as your own. / Any AI-generated material included in your report must be properly cited,
> just like any other reference source. / Plagiarism, misuse of AI, or any other form of academic dishonesty will be
> handled in accordance with the Competition Ethics and Code of Conduct policies."

**Rules & Roles, "AI Policy"** (same page):
> "You may not submit any work generated by an AI program as your own. If you include material generated by an AI
> program, it should be cited like any other reference material (with due consideration for the quality of the
> reference, which may be poor). Any plagiarism or other form of cheating will be dealt with severely under relevant
> Investment Competition policies."

**AI Policy page, Investment Competition section** (https://globalyouth.wharton.upenn.edu/ai-policy/):
> "All material referenced or generated by AI should be cited like any other reference material (with due
> consideration for the quality of the reference, which may be poor). If you use AI to assist you in any way during
> the competition, how you use it must be recorded in your Works Cited pages."

and its Ethics text adds: "...enroll in non-Wharton extracurricular courses that claim to “teach” the competition,
pass AI generated writing or work off as your own, or plagiarize existing strategies."

**Statement of AI Use** (same page): "When students express themselves in the Wharton Global Youth Program, they must
use their voice and words. Using somebody else’s work without crediting the source – including generative AI — is
plagiarism. ... AI-generated work should be cited like any other reference material, including how and where
students used AI-generated information."

**Checklist Questions** (same page): "Did I come to my current conclusion before or after using generative AI tools?"
/ "Did I verify the information I gathered from generative AI tools, whether it is the research it mentions, or the
source it cites?" / "Did I double check the numbers and information are most up-to-date?" / "Did I understand the key
learnings and how to arrive at the answers without the assistance of generative AI tools?"

Written for Wharton's pre-baccalaureate courses, not the competition, but relevant (INTERPRETATION): "Don’t use AI for
personal reflection or opinion-based tasks."

Ethics (Rules & Roles): "Plagiarism and any kind of academic cheating are grounds for dismissal from the competition."

### d2. What this means for how the team uses this research (INTERPRETATION plus ASSUMPTION)
1. **Everything in `research/insight_v1/` is AI brainstorming.** It is allowed as idea generation and must be
   **recorded**. Keep a running "AI use log": date, tool (Claude Code), what it was asked, what the team kept, what
   the team checked itself. This becomes the Works Cited / AI-use entry in the Final Report. The IPS cannot carry
   citations, so the record lives in the Final Report ("Relevant sources and supporting evidence must be included in
   the Final Report", IPS p.3 L124-125).
2. **No AI text in any deliverable.** Trading notes, reflections, the pitch, the IPS and the Final Report are written
   by the students in their own words. Do not paste or lightly reword AI sentences. The **trading notes are the
   highest risk**, because they are typed into WInS now, time-stamped, and later quoted "exactly".
3. **Reflections and the Articulation section must be the team's own experience.** They cannot be invented: "We
   trust that you will not ... fabricate analyses, invent teamwork and experiential stories". AI must not write them.
4. **Verify before relying.** Every number the team uses from this research should be re-checked against its primary
   source (URL/file given here) or recomputed by a student. The policy's checklist asks exactly this.
5. **Decide before or after AI?** The team should write down its own view first (for example, the strategy choice),
   then use AI output to test it. The log should show that order.
6. **Charts and images**: if the Final Report uses a chart that AI helped make, cite it. The Code of Conduct requires
   teams to "acknowledge ownership of all images and other media ... it (or a team member) does not own or did not
   solely develop."
7. Wharton warns that "use may also stifle your own independent thinking and creativity". The judging criteria ask
   for "an authentic team voice". The safest and strongest path is the same: AI for questions and checks, students
   for words and decisions.

---

## (e) Disqualification and penalty risks across all deliverables

"Stated consequence" quotes the source exactly. Where no consequence is written down, I say so.

| # | Risk | Exact rule | Source | Stated consequence |
|---|---|---|---|---|
| e1 | Contacting Laura | "Teams may not contact the Competition client. Teams that violate this rule will be disqualified." / "IMPORTANT: Teams are not permitted to contact Laura Gao." | Rules & Roles; SMApply Client page | **Disqualified** |
| e2 | Team size outside 4-6 | "Teams that fall below four members or exceed six members at any time during the Competition will be disqualified." | Rules & Roles | **Disqualified** |
| e3 | Removing a member without approval | "Teams that remove a member without prior approval will be disqualified." Roster locked after submission: "teams may not change their members." | Rules & Roles; SMApply L22 | **Disqualified** |
| e4 | Paid help or outside competition courses | "Teams suspected ... of using paid advisors, education consultants, extracurricular coursework, or other agents will be disqualified." | Rules & Roles | **Disqualified** |
| e5 | Changing advisor without approval | "Teams that change Advisors without prior approval will be disqualified." | Rules & Roles | **Disqualified** |
| e6 | Advisor making decisions or trading | "Advisors may not make decisions on behalf of students or actively participate in team activities, trading decisions, or strategy development." / "Students should place trades on WInS, NOT the advisor." | Rules & Roles; SMApply FAQs | None stated; a rule breach |
| e7 | Plagiarism or AI text submitted as own work | "Plagiarism and any kind of academic cheating are grounds for dismissal from the competition." / "will be dealt with severely" | Rules & Roles (Ethics; AI Policy) | **Dismissal** possible |
| e8 | AI use not recorded | "how you use it must be recorded in your Works Cited pages" | AI policy page | Treated as misuse of AI (e7) |
| e9 | Missing a deadline | "no later than 5:00 p.m. ET" / "We will not grant any deadline extensions." / "To remain eligible for the Semifinals ... submit the competition deliverables by the published deadlines." | SMApply L8-17; Rules & Roles | **Loses semifinal eligibility**; no credential |
| e10 | IPS: any format rule broken (1-page title page; 2-page strategy; 50/500-word limits; TNR 12; double spacing; 1-inch margins; PDF of 5 MB or less; no graphics, charts, images, attachments, external links, footnotes or formal citations) | "Submissions that do not meet the requirements below will not be considered for semifinal selection." | IPS guide p.3 L82-125 | **Not considered for semifinals** |
| e11 | IPS title page: team name different from roster; names not "First Name, Last Initial" or different from roster; team name given instead of WInS username | IPS p.3 L88-100; FAQ "Your team username is NOT the same as your team name." | IPS guide; SMApply FAQs | Same as e10 |
| e12 | Trading notes changed, paraphrased, or not from an executed WInS trade | "Include each Trading Note exactly as it appears in WInS." / "The Trading Notes must correspond to trades executed in WInS. Yes, we will verify this." | TN p.2 L44, L53 | None stated; an integrity failure that could fall under e7 (INTERPRETATION) |
| e13 | Reflection over 100 words; not exactly three notes | "Select three (3) Trading Notes" / "a reflection of 100 words or fewer" | TN p.2 L42, L46 | None stated; a requirement failure |
| e14 | Trading outside the permitted instruments (last year's problem) | "The following are NOT permitted: ... Anything other than the approved investments listed above." / "Teams must meet the required trading activity and portfolio management guidelines throughout the competition." | SMApply FAQs; Rules & Roles | None stated; risk to "meet all competition requirements" (eligibility) |
| e15 | Day trading or exceeding the position limit | "Day Trading: This is not permitted." | 2026-27 WInS guide p.6 | Usually blocked by the platform; a rule breach if not |
| e16 | Changing the strategy after Nov 6; portfolio or Final Report that does not follow the IPS | "Your team may not revise its investment strategy after the submission deadline." / "Your portfolio and Final Report should reflect the strategy established in your IPS." / criterion: "maintains consistency with the team’s IPS" | IPS p.2 L73-75; SMApply criteria | Scored down (Investment Strategy criterion); the rule itself forbids revision |
| e17 | Trades after the lock | "your portfolio will be frozen, and your team may no longer trade or change its holdings" | SMApply Trading Details | Impossible after the freeze; unfilled orders are not trades |
| e18 | WInS P&L put into projections | "should not be added to or subtracted from Laura’s portfolio projections" | Case p.4 L132-133 | Scored down (a case error) |
| e19 | Missing school documentation | "Final Report & Official School Documentation (Due: December 4" / "Semifinalists must also submit documentation on official school letterhead" | SMApply; Rules & Roles | Not eligible (e9); sample "Coming soon" |
| e20 | Team leader under 16 or changed after Sept 28 | "at least 16 years old at the start of the Competition. No exceptions will be granted." | Rules & Roles | Change needs written approval |
| e21 | Inappropriate team name | "reserves the right to require a team to change an inappropriate team name or disqualify the team" | Rules & Roles | **Disqualification** possible |
| e22 | Lying about decisions or inventing teamwork stories | "We trust that you will not lie about your investment decisions and outcomes, fabricate analyses, invent teamwork and experiential stories" | Rules & Roles (Ethics) | Ethics breach (e7) |
| e23 | Sources not cited in the Final Report | "Each team is required to properly cite any sources used" / "Relevant sources and supporting evidence must be included in the Final Report." | Rules (Code of Conduct); IPS p.3 L124-125 | "will not be accepted" applies to materials that break laws or IP rules |
| e24 | Final Report format | Unknown until Nov 9 | SMApply L44 | Check on Nov 9 |

Deadline clock for Australia (DERIVED with Python `zoneinfo`; ASSUMPTION: the school is in Sydney, AEDT from Oct 4):
| Deadline (5:00 p.m. ET) | UTC | Sydney | Brisbane | Perth |
|---|---|---|---|---|
| Roster, Fri Oct 9 | 21:00 Fri | **08:00 Sat Oct 10** | 07:00 Sat | 05:00 Sat |
| Trading Notes, Fri Oct 23 | 21:00 Fri | **08:00 Sat Oct 24** | 07:00 Sat | 05:00 Sat |
| IPS + portfolio lock, Fri Nov 6 | 22:00 Fri (U.S. market close 21:00) | **09:00 Sat Nov 7** (close 08:00) | 08:00 Sat | 06:00 Sat |
| Final Report, Fri Dec 4 | 22:00 Fri | **09:00 Sat Dec 5** | 08:00 Sat | 06:00 Sat |
Working rule (ASSUMPTION): submit by Friday evening Australian time, a full night early.

---

## (f) Open compliance questions only the team can answer

When logged in to WInS on day 1, before the first order:
1. **Session Rules page** (Portfolio Simulation > Portfolio Summary > Session Rules): record, with a screenshot, the
   starting cash (expect $300,000), trading begin and end date/time, allowed security types, total trades allowed
   (expect 200), day trading, margin, short selling, commissions, and **position limits (single position and all
   positions of one security type)** for equities/ETFs and for bonds. If the single-position limit is below about
   45%, the planned two-fund Treasury mix breaks. The team then needs a strategy decision (more Treasury instruments
   of the same type), not a workaround.
2. **Dashboard**: does it show $300,000 cash and 200 trades remaining? Were practice trades cleared?
3. **Trade note box**: is a note required? Is there a character limit or counter? Can a saved note be edited, or only
   added to? If several notes exist on one trade, which one would count as "the" note? (Ask Wharton if unclear.)
4. **Which instrument types WInS actually lists**: the U.S. Treasury bonds in the Bonds drop-down (which maturities?
   Are there bonds maturing 2033-2042?). Search the trade screen for Treasury ETFs of different durations,
   defined-maturity Treasury ETFs, zero-coupon/STRIPS ETFs, and broad equity ETFs. Record what exists. Do not assume.
5. **Getting Started / weekly emails** inside WInS and SMApply: any rule not on the public pages (for example, a
   minimum-activity rule behind "required trading activity and portfolio management guidelines")?
6. **Exact WInS username** as it appears at login (case, hyphens, digits): needed on the IPS title page.
7. **Official team name** and the "First Name, Last Initial" forms exactly as the roster (due Oct 9) will list them.
8. **Who holds the login and who places trades** (a student "trader" role), and the two-person check.
9. **Which Australian time zone** applies (it changes every deadline hour; see the table in e).
10. **"Investments permitted (for BOTH contributions)"** in the SMApply FAQ: does this list also limit what the team
    may recommend for Laura's long-term portfolio (the $300,000 and $150,000)? INTERPRETATION: probably a leftover
    phrase, but it matters if the plan recommends instruments WInS does not list (for example, STRIPS). Consider
    asking Wharton through Contact Us.
11. **Ambiguous ETF types** (leveraged/inverse, crypto-linked, ETNs): does the team want any at all? If yes, ask
    Wharton first. If no, record "not used" in the decision log.
12. **How "day trading" is defined** in Session Rules (the tooltip "?" next to it).
13. Whether the $25 commission applies to ETFs as "stock transactions" (budget for 200 trades: at most $5,000,
    about 1.7% of $300,000; DERIVED).
14. **AI use log**: who keeps it, and where (it feeds the Works Cited pages).

---

## Sources (all accessed 2026-09-27, 11:50-12:00 UTC unless noted)
- Repo, VERIFIED-REPO-FILE: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`,
  `2026_WGY_Investment_Policy-FINAL.txt`, `2026_WGY_Trading_Notes_Analysis-FINAL.txt`,
  `SMApply_Deliverables_Page_2026-09-27.md`; historical `competition/historical/2025_26/README.md`.
- SMApply public: https://wghsinvcomp.smapply.us/res/p/trading/ ; https://wghsinvcomp.smapply.us/res/p/faqs/ ;
  https://wghsinvcomp.smapply.us/res/p/wins/ ; https://wghsinvcomp.smapply.us/res/p/deliverables/ ;
  https://wghsinvcomp.smapply.us/res/p/client/
- Wharton Global Youth: https://globalyouth.wharton.upenn.edu/competitions/investment-competition/ ;
  .../rules-roles/ ; .../faq/ ; https://globalyouth.wharton.upenn.edu/ai-policy/ ; news (Jan 27, 2026) URL in b2.
- Stock-Trak (WInS vendor): https://edu.stocktrak.com/wharton/wp-content/uploads/sites/19/2026/09/2026-2027-WInS-Userguide.pdf ;
  .../2025/09/2025-WInS-User-Guide.pdf ; .../2024/09/2024-WInS-User-Guide.pdf ;
  https://edu.stocktrak.com/wharton/wp-json/wp/v2/media (media listing used to find the 2026-27 guide) ;
  https://edu.stocktrak.com/wharton/portfolio-faq/ ; https://www.stocktrak.com/new-feature-trade-notes/ (2017).
- Third-party (SNIPPET-UNVERIFIED): https://www.lumiere-education.com/post/wharton-global-youth-program-s-investment-competition-a-comprehensive-guide
  (published 2023-08-05, modified 2025-09-23); https://www.aralia.com/helpful-information/guide-to-the-wharton-global-high-school-investment-competition/ ;
  https://internshala.com/competitions/wharton-global-high-school-investment-competition-2026-27/ ; WebSearch summaries.

## What this teaches
Compliance is a habit you practise, not a document you read once. Three lessons carry over to real investing. First,
**the rulebook beats the platform**: a system that lets you click "buy" does not make a trade allowed. Real fund
managers work under an investment mandate (a written list of what they may hold), and "the broker let me" is no
defence. Second, **the record is made at the moment of the decision**. A time-stamped note cannot be improved with
hindsight. That is why professionals write the reason before they trade, and why the notes will show honest reasoning
only if they are honest from day 1. Third, **check which season a rule comes from**. Half the "rules" circulating
online were true in 2023 and false now. Always ask where a rule came from, and whether it applies this year.
