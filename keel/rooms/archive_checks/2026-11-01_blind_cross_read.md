# Blind cross-read: V50 against the locked record (Archive, Sun 1 Nov 2026)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code), not for submission.

**Set-up.** One outside reader (a general-purpose agent on Sonnet 5.5), given only two files: the locked record (the
three TNA notes with their reflections, and all eleven WInS notes, verbatim from `../archive.md` and
`../../../caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`) and V50 (pitch + IPS,
`../../ips_rewrite/drafts/D30/`) with the Courtroom's offered lines (C-05, without their reasons). It was not shown the
Archive's register (A1-A28), the FRONTIER flaws or the Archive's own findings. Asked: where would a judge with the
locked record open read a contradiction, ranked HIGH / MEDIUM / LOW, with the smallest fix.

**What it found, and how it squares with the Archive's own check** (its words in quotes; the Archive's ruling after the arrow)

| # | Its rating | Its finding | Archive ruling |
|---|---|---|---|
| 4 | HIGH | "The IPS makes stocks the first line of cover for a missed cheque. The locked reflection says stocks never stand between Laura and a payment. The offered line says 'stocks' outright, which is sharper than the original." | **Same as A19 (found independently).** Its fix ("what Laura keeps", -2) "only softens it"; the Archive's cure dates the set-aside before she names the range, which is C6's holder |
| 2 | HIGH | "Five of the ten rungs are funds with no promised par payout, so 'ten Treasuries ... redeemed' overstates. The body hedges ('funds that mature like bonds'). The pitch does not." | **Same as F1 / A11.** Para 2 "ten holdings" (0); pitch "ten Treasury holdings" (+1, 41 of 50). "Redeemed" stays: R is redemption (Book 5) |
| 5 | MEDIUM | "The IPS calls the floor certain, and the locked notes say its payout is not fixed." | **Same as A5 / A15.** "The bottom is her floor, rounded down" (+2); the Courtroom's cut of "a commitment rather than a forecast" removes A15 |
| 3 | HIGH | "We buy them" and "not a probability, but a purchase" against "The weak point is reinvestment" and the Nov-2039 note's "reinvested coupons fund the rest" | **A20: holds once the A19 cure is in.** No hedge ("We buy almost all of them" would undo Book 5 and reflection 1's "we provide exactly that"); the dated set-aside is what makes "We buy them" true |
| 1 | HIGH | IBTM "does two jobs" (first cheque and floor); the IPS's 2028 deposit "buys Treasuries maturing in late 2032" as if separate, so giving the floor to the building could "crush" rung 1 | **A30, WATCH, no change.** Both jobs are one 2032 fund that matures in December 2032, before the first cheque and the gift, so nothing is sold before its January. The Final Report says the first rung and the floor are one fund with two earmarks |
| 6 | MEDIUM | "A cheque funded by a Treasury already bought does not [shrink]" while the same deposit may finish a rung | **A24 holds:** V50 para 5 already says the deposit "first finishes any rung", so "already bought" is the qualifier that keeps it true |
| 7 | MEDIUM | Pitch "Never the floor" against a floor that can be touched | **Courtroom T2 endorsed:** with the A19 cure only a fall in rates can shrink the bottom, and only before she names it |
| 8 | LOW | The Courtroom's T4 ("the interest the bonds pay earns less when it is reinvested") drops the waiting proceeds that Trading Note 1 names | **A16, adopted:** "cash paid early earns less while it waits" covers both, -3 words against T4 |
| 9 | LOW | WInS trades dated Oct 2026, the IPS says January 2027 | No change: the case sets the 2027 start; the WInS book is the stand-in (the Nov-2041 note says "scaled to the model portfolio") |

Its "nothing found" list: "Nobody else can pay them" and "Laura's career already behaves a lot like a stock" (Courtroom T1, T7); the VT
description; the 2031 mechanics ("half her stocks, valued that day", which "match VT's note"); the cheque dates.

**So.** Three of its four HIGH items are the Archive's own (A19, F1, A20 via A19), found without the register; the
fourth (IBTM's two jobs) is a Final Report line, not an IPS fix. Repaired count copy: `V50R_archive_repaired_ips.txt` (495 strict).
