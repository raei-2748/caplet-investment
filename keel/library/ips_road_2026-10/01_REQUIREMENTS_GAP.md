# IPS: official requirements, rubric, and gap check of the current draft (Keel, 23 Oct 2026)

AI-generated checking work (Felix, rules desk; Tess, format; Nora, coherence). Not for submission. Read-only: Keel
read the IPS Report doc on 23 Oct and changed nothing in it. Per Ray's rule, this flags hard issues only and never
softens confident wording.

## A. What Wharton requires (quoted from `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt`)
| # | Requirement | Source |
|---|---|---|
| R1 | Title page: official team name, members "First Name, Last Initial" as on the roster, WInS username | :88-98 |
| R2 | Elevator pitch, maximum 50 words: the central idea and how it supports Laura's goals and funding needs | :33-36, :107 |
| R3 | IPS, maximum 500 words: the strategy and the reasoning behind it | :39-41, :109 |
| R4 | Must make clear: what we are trying to do; why it suits Laura; how it balances **growth, liquidity, funding reliability, risk, flexibility**; how it guides decisions as needs change; how it protects the payments while supporting a responsible facility contribution | :53-66 |
| R5 | Must establish: preparing for the operating commitment; **the operating reserve's asset composition over time**; how a responsible facility contribution is determined; financial flexibility | :48-50 |
| R6 | Also cover: risk and return, liquidity, construction and diversification, planned changes as needs approach | :46-47 |
| R7 | Framework, not calculations. Not expected: final reserve numbers, projections, the final range, co-sponsor text | :51, :68-70 |
| R8 | No graphics, charts, images, attachments, links, footnotes or formal citations | :123 |
| R9 | Miss a requirement and the IPS is "not considered for semifinal selection" | :83 |
| R10 | Now an SMApply **form**, not a PDF; "all other requirements remain the same"; TIPS and STRIPS banned in the IPS and Final Report | `wharton_email_week4_2026-10.md` |

## B. How it is judged (`SMApply_Deliverables_Page_2026-09-27.md:48-57`; the three deliverables are judged together)
| Criterion | What the IPS has to show |
|---|---|
| Investment Strategy | "clear and creative investment thesis"; planning across changing horizons; "appropriate diversification"; consistency with the IPS later |
| Client Knowledge | tailored to Laura's "circumstances, priorities, risk considerations, and residency goals"; earns her confidence |
| Portfolio Analysis | mostly Final Report; the IPS must set rules the analysis can test |
| Articulation | mostly Final Report (teamwork, process, growth) |
| Creativity & Presentation | "authentic team voice"; "original thinking"; credible about uncertainty to co-sponsors |

## C. Gap check of the latest draft (tab "Tab 15", read 23 Oct; V5 was the source of most of it)
Strict count: pitch 49/50, IPS **502/500** (498 by spaces). Gate in `workstreams/2_IPS.md` is 45 and 470.
| # | Issue | Type | Fix options (team decides) |
|---|---|---|---|
| G1 | IPS over 500 on the strict count, pitch at 49 (no margin for the form's counter) | Hard: format | Cut ~35 words from the IPS and ~5 from the pitch |
| G2 | "Liquidity" is never named. R4 lists it; V5 had "each payment's liquidity comes from a maturity, not a sale" | Hard: requirement | One sentence on where each payment's cash comes from |
| G3 | "so she cannot miss the range": the floor is IBTM's payout, which the locked TNA says is "a net asset value, as opposed to a promise of par" | Hard: fact, contradicts a locked line | A true line of equal strength, e.g. what the cap makes impossible (giving more than promised) |
| G4 | "income reinvested in the holding that paid it" vs the filed notes: early-maturity proceeds wait "in a short-term Treasury ETF" | Hard: coherence with locked notes | State the short-term Treasury ETF rule (about 13 words) |
| G5 | "about $292,000" is the late-September figure; on the 19 Oct curve it is about $293,000 on the payment-date basis and $297,200 on the holdings basis (MODEL, `competition/COMPETITION.md` section 7) | Hard: number basis | Drop the figure (R7 does not expect it) or quote one dated basis after T03 |
| G6 | Coupon reinvestment risk (~$21k if yields fall 2 points for good, `ips_numbers_2026-10/IPS_number_sheet.md`) is not named; the notes say coupons "fund the rest" | Rule missing | Vote D1 (Tue 27 Oct), then one sentence |
| G7 | Operating-reserve composition over time is one clause ("shrinking as each payment is made") | Thin on R5 | Say what it holds 2033-42 (iBond funds that mature to cash, then T-bonds) |
| G8 | Draft text is AI-written (V5 lineage; the tab's change notes are AI notes). IPS bans citations, so the AI use can only be logged in the Final Report's Works Cited | Integrity risk | Students rewrite in their own words (CLAUDE.md drafting rule); log the AI use |
| G9 | "defense" (US) next to Australian spelling elsewhere ("prioritise" in V4) | Format | Pick one spelling for all three deliverables |
| G10 | Pitch lost the "Messy Roots" echo and "a range built to hold" sits in paragraph 4 | Creativity (pre-mortem cause 7) | Team choice: which one idea the pitch carries |
| G11 | Title page: team name "Caplet" and member initials must match the roster exactly; form fields unknown | Hard: R1, R10 | Ray checks the SMApply form (T15) and the roster |

Clean: no TIPS, STRIPS, "risk-free" or "guaranteed"; no citations or links; diversification and the January review
are present (the 16 Oct pre-mortem said V5 dropped them; Tab 15 has them back).

## D. Numbers to keep consistent across all three deliverables (locked values in bold)
Stock return: **7.5% (TNA, J.P. Morgan 2027 LTCMA, WO-0003)**; V5 used 7.0% (2026 edition). VT fee: **0.06% (WInS
note)** vs **0.07% (TNA reflection)**; which is right is UNVERIFIED until the fact sheet is read again. Neither needs
to appear in the IPS; the Final Report states one sourced figure.
