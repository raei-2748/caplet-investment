# If Caplet adds the inflation rate, three repeated sentences pay for it; and the reserve line in K4 has its dates wrong
AI-generated research by the Keel Office (Claude Code). Not for submission. Cite in Works Cited.
(Keel is a simulated team, AI-written.)
Work order: SD-WR-01 (Laura's Room request to the Writing Room, 24 Oct) | Room: The Writing Room (Tess; Amara first
drafts; format-gatekeeper role, no subagents) | Date: Sat 24 Oct 2026 (Sydney, afternoon run)

**Text checked:** the newest draft, Keel's second pass on Tab 15 with E1-E12 and K1-K5 applied
(`/mnt/project-files/ips/IPS_edits_v2_2026-10-24.md`, "Full text" section). Suggestions only: nothing here touches the
IPS Report doc, and Caplet writes every final word.

## The counts (`keel/office/tools/textcheck.py`)
| Text | Strict words | By spaces | Characters | Limit | Non-ASCII | Overclaim words |
|---|---|---|---|---|---|---|
| Pitch | 47 | 47 | 293 | 50 | 0 | 0 |
| IPS, as drafted | 494 | 491 | 2,865 | 500 | 0 | 1 ("secures", see issue 3) |
| IPS + option A (Amara's 24-word sentence replaces the 10-word inflation line) | **508** | | | 500 | | |
| IPS + option A + cut package 1 + fix 2 | **467** | | 2,697 | 500 | 0 | 0 |

Option A alone breaks the hard limit by 8. Keel's own margin (470 strict, R7 in `keel/pm/RISKS.md`) needs 38 out.

## Hard issues (at most 5; minimal edits, no rewording for taste)
| # | Where | Issue | Minimal edit | Words |
|---|---|---|---|---|
| 1 | P5 | Option A (the case asks for an assumption about inflation, :146-147) takes the IPS to 508 > 500 | Take one cut package below with it. Without option A nothing needs cutting | -38 to -40 |
| 2 | P6 (K4) | **Dates wrong.** "five Treasury ETFs that close one a year to 2037, then five bonds to 2042": the ETFs close Dec 2032 to Dec 2036 and the bonds mature Feb 2037 to Nov 2041 (`competition/COMPETITION.md` section 8). 2037 and 2042 are *payment* years. IBTM has already closed by January 2033 | "five Treasury ETFs for 2033-37, then five bonds for 2038-42" (says the payment years, true to the book) | -3 |
| 3 | P3 | "Root & Branch **secures** the roots": "secured" is on the team's overclaim list; textcheck missed the other ending (fixed today: "secures" and "guarantees" added). The roots still carry IBTM's payout and coupon-reinvestment risk, so the verb claims more than the plan does | Cut package 1 removes the sentence. If it stays: "secures" -> "buys" (same strength, true) | 0 |
| 4 | P6 | "Coupons are reinvested in the **bond** that paid them": half the ladder is ETFs, which pay distributions, not bonds | "bond" -> "holding" | 0 |

Checked and clean: no TIPS/STRIPS, no citations, no charts, no non-ASCII (Google Docs will curl the apostrophes; the
form counts words, not quote shapes), the review, diversification, one-issuer and early-maturity clauses (SD-T05
rules 3, 6, 12) all present.

## Answer to Amara: which ~38 words come out if Caplet takes option A (options, not wording)
Every candidate repeats something the IPS or pitch already says, so a cut loses words, not a rule. Rules SD-T05 marks
as required (one-issuer choice, diversification, where early cash waits, the annual review, WInS mirror) are not on
the menu.

| Cut | Words | What already says it |
|---|---|---|
| C1 P1: ", so each payment depends mainly on the US government paying its debts" | 12 | P3 "The roots rely on one issuer by design" |
| C2 P3: "Root & Branch secures the roots (the payments and a facility floor) before investing in the branch." | 16 | The pitch, word for word in substance; also clears issue 3. Motif-neutral, so Monday's vote does not change it |
| C3 P3: ", since no dollar asset is safer" | 6 | (Tess's cut from the morning; it is the *reason* for one issuer) |
| C4 P6: "Each payment's cash comes from a maturity, not a sale." | 10 | P1 "maturing before it" |
| C5 P3: ", since their cost moves most with interest rates" | 8 | Nothing: it is the reason the 2027 money buys the latest payments first |

- **Package 1 (Tess's lean): C1 + C2 + C4 = 38.** With option A and fix 2: **467 strict.** Cuts only repeats; every
  reason in the IPS survives.
- **Package 2 (Amara's lean): C2 + C3 + C4 + C5 = 40.** With option A and fix 2: **465.** Keeps P1's plain line on
  what certainty means and drops two reasons instead.
- If Caplet takes option B or C, no cut is needed (491 strict after fix 2), and the 470 margin is the only reason to
  cut at all.

## Requests
- Closed: Laura's Room -> Writing Room (the option A cut).
- Filed: Long Room (Nora): put "package 1 or 2" next to option A on Tuesday's vote sheet, so one vote settles both.

## Takes for the morning brief
Tess: Option A is right, and it costs exactly the three sentences that say things twice. I'd cut C1, C2 and C4: we keep
every *because* in the IPS and lose only echoes. The bigger catch is K4, though – we wrote the payment years where we
meant the maturity dates, and a judge who knows IBTM closes in December 2032 would spot it in one line.
Amara: I'd keep "depends mainly on the US government paying its debts" – it's the only sentence Laura could repeat to a
co-sponsor without us in the room. Cut the "since no dollar asset is safer" and the rate-sensitivity reason instead;
they're true, but a judge believes them already.
