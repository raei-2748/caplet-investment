# IPS Draft 1 (Writing Room, Tess Bell; Mon 26 Oct 2026, Sydney)

**AI DRAFT (Claude, 26 Oct 2026) - for Caplet to rewrite in its own words; log the AI use.**
(Keel is a simulated team, AI-written. Tess is fiction; the text below is for Caplet to rewrite.)

Files: `pitch.txt` and `ips.txt`. They hold only the final words, with no label, so the textcheck counts stay clean.
Built from the Courtroom verdicts: both judges picked B_voice; Kai picked C_aha. The structure and the body come from
B. The thesis is moved up to paragraph 1, as the practitioner and Kai asked, and the best lines of C and A are grafted
in. Nothing was committed. No WInS, SMApply or Google Doc was touched.

## 1. textcheck (`python3 keel/office/tools/textcheck.py <file> --limit N`, run 26 Oct)
| File | By spaces | Strict | Limit / target | Non-ASCII | Overclaim words |
|---|---|---|---|---|---|
| pitch.txt | 46 | **47** | 50 (target 46-48): PASS, 3 to spare | 0 | 0 |
| ips.txt | 480 | **484** | 500: PASS, 16 to spare; target 485: PASS, 1 to spare | 0 | 0 |

Characters: pitch 282, IPS 2,784 (after the 26 Oct fact-check edits; word counts unchanged). The IPS is still to be checked with the Google Docs word count (COMPETITION.md s9).

## 2. Checklist: every Window item and the sentence that ticks it
| # | Box | Sentence in Draft 1 |
|---|---|---|
| A1 | Time horizons | 2027: "the $300,000 she already has buys them". 2028: "any January gap is the 2028 deposit's first job" and "From the rest of that deposit...". 2031: "In 2031 Laura gives co-sponsors a window". 2033-42: "In 2033 the payment holdings become the operating reserve, one fewer each January" |
| A2 | Risk and return, liquidity, construction, diversification, planned changes | "diversifying a plan whose payments rest on one issuer"; "For liquidity, the funds sell any day and something matures before every payment"; "one fewer each January" |
| A3 | Operating commitment / reserve composition / contribution / flexibility | P2 certainty definition / "the operating reserve, one fewer each January" / "In 2033 the same rule sets the gift, capped at that top" / "the other half stays hers, for flexibility as the project develops" |
| A4 | Framework, not tickers or sums | No ticker, no dollar split, no return figure. The rules: payments first, stocks equal the expected interest, half-the-stocks top, the order for filling a gap |
| M1 | Goal in the first two sentences | S1: the ten $50,000 Januaries, paid only by the portfolio. S2: "buys those ten Januaries first, then builds her facility gift" |
| M2 | Why it fits Laura | "With her living costs met elsewhere, she can afford 'thoughtful risks'. The payments cannot." and the P3 slump reason |
| M3 | Growth, liquidity, funding reliability, risk, flexibility | Growth: "rising facility costs are the index fund's job". Liquidity: "For liquidity...". Reliability: the P2 definition. Risk: "Reinvestment is the soft spot" and "The catch is less upside in a boom". Flexibility: "the other half stays hers" |
| M4 | Decisions as needs change | "we trade only to invest new money"; "any gap comes from Laura's half first, the floor last"; "Each January we review the plan with Laura" |
| M5 | Protect the payments, support the gift | P1 order; "Moving floor money into stocks would raise the expected gift... We refuse." |
| E1 | Clear, creative thesis | P1 S2 (the capital-protected note, minus the option), worked out in P4 |
| E2 | Laura as a person | "a graphic novelist who studied statistics at Wharton, is planning a residency for artists, writers, designers, entrepreneurs and educators" |
| E3 | Concepts applied; good and bad markets | Static floor plus cushion (P4, unnamed), cash-flow matching (P2, unnamed), reinvestment risk, one-issuer concentration. Bad market: "a two-year stock fall"; good market: "The top adds half the stocks' value that day" |
| E5 | Voice; uncertainty stated credibly | "The payments cannot."; "We refuse."; the kicker. Uncertainty: "about what remains", "projected payout, rounded down with a margin", "could also cut yields" |
| K1 | Reserve size, composition and change | "the payment holdings become the operating reserve, one fewer each January"; "kept whole to its date" |
| K2 | Definition of high certainty | "We take 'high degree of certainty' to mean every payment has its own Treasury bond or fund, bought by January 2028, maturing before it, interest reinvested." |
| K3 | Contribution method | the window paragraph (bottom = projected floor less a margin; top = plus half the stocks; capped) |
| K4 | Flexibility kept | "the other half stays hers, for flexibility as the project develops" |
| K5 | Inflation | "Inflation cannot raise the fixed payments; rising facility costs are the index fund's job." |
| K6 | Assumptions (performance, timing, outside money) | "We assume stocks beat Treasuries over decades, not every two years."; "every January"; "only her portfolio may pay it" |
| K7 | 2031 range, good and bad outcomes, protects payments | the window paragraph, plus "a payment needing help first" and "the floor last" |
| G4/G6/G7/G8 | No citations, plain text, no banned assets or words | 0 non-ASCII, 0 overclaim words; "option" appears only as what we do not hold |

## 3. Where each fact comes from
| Fact in the text | Source |
|---|---|
| $50,000 a year from 2033 for ten years, fixed, not inflation-adjusted | Case `Laura_Gao_2026_Client_Profile.txt`:90 |
| "only her portfolio may pay it"; "high degree of certainty" | Case :91-92 (rewording of "may not rely on" outside funding, Kai fault 1) |
| $300,000 in 2027, 2028 deposit from publishing, speaking and licensing | Case :43-45 |
| Graphic novelist; Statistics & Information Decisions Management degree, Wharton 2018 | Case :13-16 ("studied statistics" is shorthand; see section 6) |
| Residency for artists, writers, designers, entrepreneurs, educators | Case :78-80 |
| Living costs outside the portfolio | Case :61-63 |
| "thoughtful risks" | Case :70 |
| Flexibility "as the project develops" | Case :102-103 |
| 2031 co-sponsors; credibility; range; protect the payments | Case :108-120 |
| Operating reserve from 2033 | Case :94-97 |
| Start-of-year flows ("every January") | Case :59-60 |
| A slump that cuts her income "could also cut yields" | Reasoning (INF), Laura's Room s2; the Lab fixed "would" to "could" |
| Stocks equal the expected interest; the floor IBTM pays about what it was sized for (1-in-100 payout 98.7%) | MODEL, 22 Oct curve: `lab/D1_split.py`, `lab/D1_run_22oct.py` (D1_lab (a)) |
| "resizes with yields" | MODEL, D1_lab (b): VT at 13% of the 2028 money at -2 points, 29% at +2 points |
| "only a two-year stock fall, or a payment needing help first" | MODEL, D1_lab (c): 21.2 pts stock fall + 3.2 pts other, of the 24.4% below the top |
| "any January gap is the 2028 deposit's first job" | WInS IBTR note (GT s3); ladder headroom 4bp on 22 Oct, MODEL |
| About 10,000 companies | TNA Note 3 (VT) |
| Short-term Treasury fund for interest | TNA Note 1. Which ETF is WInS-listed: **UNVERIFIED** (SGOV/BIL/SHV) |
| Funds sell any day | TNA reflection 2 (iBond liquidity), true of VT too. The 2038-42 T-bonds rely on the maturity half of the sentence |
| "nothing can expire worthless" | D1_lab (e) fix of "nothing that expires" (IBTM ends in 2032 by design) |

## 4. What came from which candidate, and why
| From | Line or move | Why |
|---|---|---|
| B (base) | Opening, "The payments cannot.", "Why first?", the window paragraph, "We refuse.", the trading rule, the annual review, the kicker | Both judges' winner: the best skim, the clearest split between what Laura can bear and what she is willing to risk, the review kept |
| C | Thesis moved into P1 S2 ("like a bank's capital-protected note, minus the option"); "resizes with yields"; "risks only interest her floor has not yet earned"; the gap order "Laura's half first, the floor last" | The practitioner and Kai said the skim must hit the thesis first. These are the lines that show why the stocks equal the interest |
| A | One-issuer concentration with diversification; the inflation sentence; the "bought by January 2028" certainty definition | Ticks A2/K5/K2 in one sentence each; it removes B's "just before" stretch for the Feb-2037 bond |
| Kai | "only her portfolio may pay it"; "has its own Treasury bond or fund ... interest reinvested" in place of "owned"; "A sum equal to its expected interest"; kicker "she holds a Treasury for each" in place of "owns all ten"; one "X, not Y" kept ("a commitment, not a forecast"); "something matures before every payment" | Case accuracy (:91-92), the locked Nov-2039/2041 coupon notes, the iBonds mature in December |
| Courtroom (student) | The K6 assumption sentence | The gap shared by all three candidates; it gives no figure, so the TNA's 7.5% is not exposed |
| Long Room | Name + XR line + disarm in P1; "whole", "timed", "window" as the only motif words; the K1 callback | Motif ration |
| Dropped | "Stocks decide how generous Laura can be, never whether she pays" (C): it repeats the pitch's last line and would be a second kicker. "never take back" (A, C): overclaim. "Taiwan cost overruns" (B): out of scope (:169). "a liquidity no odd-lot bond offers": cut for words | |

## 5. Open votes this draft assumes (Keel's leans, vote set B, Tue 27 Oct)
- **D1a yes**: a coupon gap draws on Laura's half of the stocks first, the floor last ("the floor last").
- **D1b margin**: the 2031 bottom is quoted "rounded down with a margin" ($140k version, D1_lab (a)).
- **Residents**: the five groups are spelled out once; neither "residents" nor "artists" alone is used.
- **Name**: Caplet XR, X = ten, R = release. Fallback "Ten Januaries": drop the XR and disarm lines (about 30 words
  freed) and say "range" for "window".

## 6. Three lines Caplet should most want to rewrite in its own voice
1. **"To a rates trader a caplet is an option; this one holds none: the floor is a Treasury fund, the cap a rule."** ("promise" changed to "rule" by the fact-check, 26 Oct)
   It is the most writerly line and the one a judge will remember. It should sound like Caplet, not like Keel.
2. **"With her living costs met elsewhere, she can afford 'thoughtful risks'. The payments cannot."** This is the
   client insight. Say it in your own words. Also decide whether "studied statistics at Wharton" is close enough to the
   degree's name (case :16).
3. **"Laura owes ten Januaries. From 2028 she holds a Treasury for each."** The kicker. If D1a or the order changes,
   check it again ("from 2028" assumes the deposit fills any gap).

## 7. Known risks to check in Draft 2
- The IPS is at 484 strict, 1 under the 485 target, so a rewrite must cut a word for each word it adds. First cuts:
  "Why first?" (2), "of about 10,000 companies" (4).
- "Caplet XR buys those ten Januaries first" claims only the order. The amount depends on a one-close headroom (4bp).
  P3 states the condition.
- The pitch line "Stocks move the top, not the floor" is true of stocks. A coupon gap can still reach the floor, last
  (D1a), and the IPS says so.
- "The catch is less upside in a boom": a bank note's participation rate and cap are UNVERIFIED, so the trade-off is
  stated in words only.

## 8. Fact-check (26 Oct)
Fact-checker + format gatekeeper (Window / Writing Room roles), Mon 26 Oct 2026 Sydney. AI-generated (Claude Code).
**Verdict: FIX (done), then SHIP to Caplet as Draft 1.** Three edits in `ips.txt`, none changing the word count; `pitch.txt` unchanged.

### Edits made (ips.txt)
| # | Was | Now | Why |
|---|---|---|---|
| 1 | P1 "the cap a promise." | "the cap a rule." | Overclaim word ("promised" is on the fact-checker list). The case warns against promising (:114-116); the locked TNA makes the *minimum* the promise (Note 3, "her promised minimum"), and the top is missed in ~24% of MODEL paths (D1_lab (c)). The top is set by a rule (floor + half the stocks) |
| 2 | P2 "is building a residency" | "is planning a residency" | Case :76 "In 2033, Laura plans to establish": nothing is being built in 2026 |
| 3 | P5 "so only a two-year stock fall, or a payment needing help first, can pull it lower" | "so mainly a two-year stock fall, ..." | Not true as an absolute on the MODEL basis: `keel/library/ips_numbers_2026-10/ips_numbers.py` :208 sets top = what IBTM is sized to repay + half the stocks, so IBTM paying slightly short (NAV, not par; 1-in-20 99.1%) is a third cause inside the 3.2 pts "stocks did not fall" (D1_lab (c)) |

### Final counts (textcheck re-run after the edits; third method = regex `\b\w+\b`, the most generous split)
| File | By spaces | Strict | Regex | Limit | Chars | Non-ASCII | Overclaim words |
|---|---|---|---|---|---|---|---|
| pitch.txt | 46 | **47** | 49 | 50: PASS | 282 | 0 | 0 |
| ips.txt | 480 | **484** | 492 | 500: PASS | 2,784 | 0 | 0 |

Google Docs / SMApply form word count: NOT CHECKED (no access by rule); 492 is the worst case on file.

### Findings
| Claim | Result | Checked against |
|---|---|---|
| $50,000 each January 2033-42, fixed; only the portfolio pays | PASS | Case :88-92, :59-60 ("beginning" of each year read as January) |
| $300,000 in 2027; 2028 deposit from publishing, speaking, licensing | PASS | Case :43-45 ("other entrepreneurial ventures" left out: fair) |
| Graphic novelist; "studied statistics at Wharton" | PASS (shorthand) | Case :13-16 (degree: Statistics & Information Decisions Management) |
| Five resident groups | PASS | Case :78-79 |
| Living costs elsewhere; "thoughtful risks" (exact quote) | PASS | Case :61-63, :70 ("can afford" is our inference about ability; the case says "willing") |
| "high degree of certainty" (exact quote); certainty definition | PASS | Case :91, :97-98. Every holding matures before its January: IBTM-IBTR Dec 2032-36 for 2033-37; Feb-2037, May-2038, Nov-2039/40/41 for 2038-42 (COMPETITION.md s8). Stays below the TNA's "near-ironclad guarantee" |
| "interest reinvested" | PASS | Locked WInS notes Nov-2039 / Nov-2041 (GT s3) |
| Slump "could also cut yields" | PASS (reasoning, hedged) | Not a case fact; "could" is right |
| "$300,000 ... buys them; any January gap is the 2028 deposit's first job" | PASS | WInS IBTR note (GT s3); MODEL 22 Oct: headroom $1,139 (4bp), over $300k in 47% of paths |
| Floor "sized to grow back to about what remains" | PASS | TNA Note 2 "final payout is not fixed"; MODEL payout median 100.0%, 1-in-100 98.7% |
| Stocks = expected interest; "resizes with yields" | PASS, re-derived | Lab (b): $20.1k / $32.1k / $43.0k at -2 / 0 / +2 pts. Independent hand check, 150,000 x (1 - (1+y/2)^-9.9): $20.1k / $32.1k / $42.9k (MODEL, 22 Oct curve forwards) |
| About 10,000 companies | PASS | Locked TNA Note 3 (~10,000 stocks) |
| One issuer; diversification | PASS | All payment holdings are US Treasuries or Treasury ETFs |
| "nothing can expire worthless" | PASS | D1_lab (e) |
| "less upside in a boom" | PASS in words; size UNVERIFIED | No bank-note participation or cap data on file (D1_lab (e)) |
| 2031 window; bottom = projected payout rounded down with a margin; half the stocks stays hers "as the project develops" | PASS (D1b vote pending) | Case :109-120, :102-103; MODEL bottom $145k plain / $140k with margin; IBTM pays below the quote in 0% of paths |
| Inflation cannot raise the payments | PASS | Case :90 |
| Short-term Treasury fund for new money | UNVERIFIED | Locked TNA Note 1 names it, but which ETF is WInS-listed (SGOV/BIL/SHV) is unconfirmed; Laura's plan may use only WInS-listed securities |
| Gap order "Laura's half first, the floor last" | PASS (D1a vote pending) | COMPETITION.md s7 also puts the ~$1k 2027 leftover first; too small to matter, but D2 may add it if words allow |
| Funds sell any day; something matures before every payment | PASS | TNA reflection 2; maturity list above |
| Operating reserve from 2033, one fewer each January | PASS | Case :94-97 |
| Banned words / assets | PASS | 0 hits for guaranteed, risk-free, locked, secured, promised, cannot miss, never below, CPPI, immunisation (after edit 1); "option" only as what is not held; no TIPS/STRIPS/derivatives; no ticker, link, citation or figure from code |
| Form | PASS | Pitch <= 50, IPS <= 500 (form :33, :39); framework, not tickers (form :51-52); no final range or projections (form :68-70) |
| TNA / WInS coherence | PASS | Pitch "Stocks move the top, not the floor" = Note 3; IBTM's two jobs = Note 2; top-up order = IBTR note; no "guarantee" |

### Could not fix (for Draft 2 / Caplet)
1. **What the top is added to.** P5 "The top adds half the stocks' value that day" reads as bottom + half; the MODEL uses
   IBTM's sized repayment + half (`ips_numbers.py` :207-208), about $5-10k higher. Caplet picks one, and the Lab re-runs the
   2031 numbers on that basis. With bottom + half, "only" would hold again, since IBTM never pays below the quote in the MODEL.
2. Short-term Treasury ETF on WInS: UNVERIFIED (a student must look it up in WInS; AI may not).
3. Google Docs / SMApply word count: NOT CHECKED.
4. "studied statistics" and "can afford" are fair shorthand, but they are Caplet's call (section 6, item 2).
