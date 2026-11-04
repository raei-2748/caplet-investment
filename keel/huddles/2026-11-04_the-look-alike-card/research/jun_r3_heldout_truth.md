Ground truth for the held-out test, written before seeing card v2 or the stranger's marks, Wed 4 Nov 2026. Keel is a simulated team, AI-written.

# H-030 round 3: what actually broke in Rewrites D and E (Jun)

Checked against: the final IPS (`keel/ips_rewrite/drafts/FINAL/ips.txt`), the submitted trading-notes reflections and
notes (`keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt`), the WInS book (`competition/wins/2026-10-23_snapshot.md`)
and, for P1, the case text (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`). Rewrites from
`research/heldout_rewrites.md`. Paragraphs count from "From 2033, Laura's portfolio must pay" (P1) to "From 2033, the
ladder and the money set aside" (P8), the same as my round-2 audit. Method: a word diff of each rewrite against the
final, paragraph by paragraph, then every changed or added word read against the three sources.

Same standard as round 2: a break is a line whose plain reading is false (a dropped qualifier that makes it untrue, a
word that contradicts the submitted notes, a changed mechanism, an added claim the final doesn't make). A looser but
still-true paraphrase is not a break. Borderline = false on one fair reading, true on another, or false only to a
bond-literate reader.

## Breaks (two: one in D, one in E)
| ID | Rewrite, para | The rewrite says | The final IPS says | Why it is false |
|---|---|---|---|---|
| D1 | D, P2 | "Ours is ten Treasury holdings, one redeemed each January" | "Ours is ten Treasury holdings, one redeemed for each January" | Nothing in the book is redeemed in a January. IBTM-IBTR end in December (iBonds Dec 2032-Dec 2036); the five bonds mature 15 Feb 2037, 15 May 2038 and 15 Nov 2039-2041 (WInS book, "Pays for"). The submitted Feb-2037 note says it outright: "maturing 15 Feb 2037 for Laura's 1 Jan 2038 payment ... The 10.5-month gap". "For" is the word that kept the line true. Same break as round-2 #3 (C). |
| E1 | E, P2 | "It is ten Treasury holdings, one redeemed each January" | same as D1 | Same fault, same evidence. |

## Borderline (four; not counted as breaks)
| ID | Rewrite, para | The rewrite says | The final IPS says | Why only borderline |
|---|---|---|---|---|
| D2 | D, P3 | "We take the second route, like a row of fixed-date deposits, and it never needs rebalancing." | "We do the second, which never needs rebalancing." | An added picture the final doesn't use. "Fixed-date" is true of all ten (the final's "fixed end dates"), but a deposit also repays a known sum, as opposed to five of the ten holdings: the IBTM note says "the final payout is not fixed" and reflection 2 says "their terminal payout is a net asset value, as opposed to a promise of par". The cousin of "pays exactly" said of the funds. "Like" keeps it an analogy, so not a straight false statement. |
| D3 | D, P5 | "What is left, the interest that floor will earn, goes into one world index fund" | "What remains, roughly the interest that floor will earn, goes into one world index fund" | "Roughly" dropped. The share money is a fixed dollar sum on 2 Jan 2028; the interest a Treasury fund earns to late 2032 isn't known then, because its end payout is its net asset value (IBTM note: "the final payout is not fixed"). Without "roughly" the line sets the two equal. Read as the design (the share money is sized to the floor's interest) it is still true. Same weight as round-2 b4 ("coupon income"): a bond-literate judge might catch it; a Year 11 won't. |
| D4 | D, P7 | "The ladder's weakness is that it counts on reinvesting its bonds' interest." | "The ladder's main weakness is that it counts on reinvesting its bonds' interest" | "Main" dropped. Read as "its weak spot", true. Read as "its only weakness", false: reflection 2 names a second catch ("their terminal payout is a net asset value"). This is the Window's 4 Nov fix ("one weakness" to "main weakness") half undone: no "one", but no "main" either. Nearest to a break of the four; if the stranger marks it, it is not a false alarm. |
| E2 | E, P2 | "We call the plan Caplet XR. It is ten Treasury holdings" | "We call the plan Caplet XR, after extended-release tablets, which ... come labelled "do not crush". Ours is ten Treasury holdings" | In E, "It" can only mean the plan, so E says the plan is ten Treasury holdings. The plan also holds the late-2032 floor fund and a world index fund (E's own P5; VT, 167 shares, in the WInS book). In the final, "Ours" follows "extended-release tablets", so it reads as our tablet, the ladder inside the plan. Borderline because the final's P8 also calls the plan the tablet, so the looseness is in the final too; E only makes it explicit. |

## Checked and fine (looser, still true)
- **Both, P1:** D "Whatever is left"; E "to fund her Taiwan residency" (the case: "Funding the residency beyond the
  final payment in 2042 is outside the scope") and "Any surplus can help fund the facility" (the case: the portfolio
  "may also cover part of the facility's cost").
- **Both, P2:** D "carry the warning "do not crush""; D "Selling one before it matures, even for the building, is
  crushing it" (the final's definition turned round); E "Selling a holding early, even to pay for the building, breaks
  the schedule".
- **Both, P3:** "Pension funds either match ..." drops "cover fixed payments" (round-2 C did the same and passed; "the
  payments" still carries the scope). Both keep "average", "bond" in "A Treasury bond held to maturity", "Treasury
  funds with fixed end dates" and "each maturing before a January payment". Neither names duration matching. E's "High
  certainty therefore means" drops "to us" (round-2 B dropped it too and passed; the case asks teams to "define what
  they consider a high degree of funding certainty", so the line still reads as ours).
- **Both, P4:** both keep "can" ("can dry up", "can fall away"). D's split ("Shares are called safe over ten years.
  Time makes a loss rarer, but not smaller") and E's "often described as safe" keep the set-up-then-knock-down.
- **Both, P5:** "late 2032", "the floor of her gift", "if needed"; E keeps "roughly"; both keep "Banks sell this as a
  capital-protected note, but they spend the interest on an option" (mechanism intact, unlike round-2 B); "We also
  skip/avoid portfolio insurance"; "only on fixed dates, never on a market move/market moves".
- **Both, P6:** "rounded down", "money she already owns", "into Treasuries before she names it/the range", "stays/remains
  hers and liquid". E's "cannot be quietly reduced" for "can't quietly be halved" is still true (a norm about a number
  said aloud). Note for the stranger's marks: E's P7 then says "the whole range is reduced"; that happens before she
  names it, so the two don't contradict, but a reader may think they do. A mark there is a false alarm on the facts.
- **Both, P7:** "kept shares" (D), "retained shares" (E; round-2 B's "retained equities" passed); "every dollar
  waiting for a cheque" / "awaiting a payment"; "Her spare money" in both, as opposed to round-2's "excess cash" and
  "spare cash"; E's "absorbs the gap first" is the same mechanism as "shrinks first" (the gap is paid out of it). E's
  "principal weakness" = main. E's "reinvesting bond interest" has the same scope as "its bonds' interest" (round-2 B
  passed the same).
- **Both, P8:** D is word for word the final. E's "works only while nobody crushes it" turns the final's "as long as"
  (not crushing is enough) into "only while" (crushing is fatal); dropping a claim is not a break, and E's own P2 says
  selling early "breaks the schedule".

## Scoring rule, fixed now, before the marks
- **Caught:** the stranger marks the sentence holding the quoted words and the mark points at the fault (for D1/E1:
  the January timing, or "redeemed each January"). A mark on the right sentence for the wrong reason counts as caught
  but is noted.
- **Missed:** a break (D1, E1) with no mark on its sentence.
- **False alarm:** a mark on a line listed under "Checked and fine". A mark on D2, D3, D4 or E2 is neither caught
  nor a false alarm; it is scored separately as "borderline flagged".
- So recall is out of two, and false alarms are counted against the fine lines above.

## What the count says before anyone marks it
Two breaks in about 1,000 words, as opposed to seven in round 2's three rewrites. The stranger kept almost every
load-bearing word ("bond", "average", "can", "rounded down", "late 2032", "kept/retained shares", "spare money").
The one place both D and E broke is the one place all three round-2 rewrites broke: the "for" in "redeemed for each
January". Five of five rewrites have now dropped or changed it. That preposition is the most fragile word in the IPS,
and it is a one-word-short look-alike ("redeemed each January"), which is exactly what a card in capitals is for.
