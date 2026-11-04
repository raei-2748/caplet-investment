# Blind cross-read: the FINAL against the locked record (Archive, Wed 4 Nov 2026)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code), not for submission.

**Text read.** The FINAL as it stands at 19:20 Sydney (`../../ips_rewrite/drafts/FINAL/`; IPS 495 strict, sha256
`b9368f5b5fa9ffc5`; pitch 48, `2f94abe7c30be498`), the same text as the project-folder copy. The Long Room's offered
", to us," cut was not in it.

**Set-up** (as on 1-3 Nov, new hands, two readers so they can disagree). Two general-purpose agents, each given one file
only: the three TNA notes with their reflections (verbatim from `../archive.md`), the eleven filled-trade notes
(verbatim from `../../../caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`), the FINAL pitch
and IPS, and a six-line case summary (deposits, the ten payments, the 2031 range, the simulator's $300,000, what the
iBonds funds are). Not shown: the register (A1-A33), FRONTIER, any room's finding, the Archive's own view, the cards.
Same four questions: (1) clashes with the locked record, HIGH / MEDIUM / LOW, quoted; (2) commitments the IPS drops;
(3) the IPS against itself; (4) the one fix, if any, with its word cost; "do not invent problems".
- **Reader O:** Opus 5.5, as a Wharton judge who ran pension fixed income for twenty years.
- **Reader S:** Sonnet 5.5, as a Year 12 student on a rival team hunting for lost marks.

## What they found (no HIGH from either)
| Item | Reader O | Reader S | Archive ruling |
|---|---|---|---|
| P3's two methods ("matching their bonds' average timing ... We do the second") v reflection 1 "through duration-matching" | **MEDIUM**, "the one that lands" | **MEDIUM** | **A34, new: both found it alone.** Not a change of plan (the ladder is the same), a change of word. O's fix is false (below). IPS unchanged; Final Report's Articulation owns it |
| No fund-payout caveat beside "A Treasury bond held to maturity pays exactly" (five notes say "not fixed"; reflection 2 "net asset value") | MEDIUM (dropped commitment; "partly covered" by the lock's "every dollar waiting") | MEDIUM (clash B, "a quiet upgrade") | A14, flagged a fourth time. Ray's 26 Oct call stands (no hedge); "bond" already makes the sentence true. Caplet's call, on the card (row C) |
| The WInS book holds VT and IBTM's floor bought with the simulator's $300,000; the pitch says the first $300,000 buys Treasuries | MEDIUM ("the Final Report can carry this if the IPS has no words to spare") | MEDIUM, **its one fix** ("The simulator's single $300,000 stands in for both deposits.", +9) | A32/F24. Readers so far: not a clash (2 Nov), HIGH (3 Nov), MEDIUM, MEDIUM. Keel's call holds (FR, the Nov-2041 note's own words); the split stays visible to Caplet |
| "high certainty means no payment depends on shares" v reflection 1 "a near-ironclad guarantee" | LOW ("near-ironclad is the goal and no shares is the means") | MEDIUM (the IPS's "can fall short" walks back "exactly that") | A3 holds: the IPS names its one weakness and prices it, which is the "near" |
| P7's shares into Treasuries v reflection 3 "not standing between Laura and a payment deadline" | LOW | LOW | A33 holds (deletion test; the shares are sold before any cheque is due) |
| "changes only on fixed dates, never on a market move" v the IBTR note's yield trigger | LOW (date fixed, amount priced) | LOW | A4/A23 hold |
| P6 "The bottom is the floor, rounded down" v P7 "she names a lower range" | LOW (internal) | not raised | Card row K: a lower range is lower at both ends; 2 of 3 strangers missed it today |

## The fix one reader offered, tested
Reader O: "We do the second, which also matches timing without rebalancing." (+2). It says the ladder matches the
payments' average timing. **It doesn't:** the Window's rung-by-rung check puts the ladder at about 7.6 years against the
payments' 10.0 (MODEL, H-028, Kai), because coupons and early maturities come back years before the cheques; that is
exactly the weakness P7 names. So the fix would make the IPS false to make the TNA's word look right. Rule (A34): never
say the ladder matches the payments' average timing or duration. The loose word is October's.

## Reader S's fix
"The simulator's single $300,000 stands in for both deposits." (+9). True in substance (the book is the plan after the
2028 deposit, scaled: bank #142), but the IPS has 2 words of room (4 if the ", to us," cut is taken), and the case keeps
the simulator apart from Laura's money (:129-130). Stays with the Final Report, as ruled on 3 Nov.

## Reader O, verbatim (section 4)
> Item 1a. Change "We do the second, which never needs rebalancing." to "We do the second, which also matches timing
> without rebalancing." ... It tells a judge holding Trading Note 1 that the ladder matches duration as well as cash
> flows, which is true, so the October word and the November method no longer clash. Nothing else must be fixed before
> submission.

## Reader S, verbatim (section 4)
> Fix D. It is the only item that sets the IPS against the actual holdings, and Wharton says the portfolio "should
> reflect the strategy established in your IPS". Add this sentence to the IPS: "The simulator's single $300,000 stands
> in for both deposits." That is 9 words added. ... A and B are wording slips in the IPS that the team can only soften,
> not undo. ... Nothing else needs changing.

Packet as read: rebuilt by `python3` from the files named above (the run's scratch; not kept, since every part is a
repo file named here).
