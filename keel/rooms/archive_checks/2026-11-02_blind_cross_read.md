# Blind cross-read: V53 and today's offers against the locked record (Archive, Mon 2 Nov 2026)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code), not for submission.

**Set-up** (as on 1 Nov). One outside reader (a general-purpose agent on Sonnet 5.5) given three files only: the locked
record (the three TNA notes with their reflections, verbatim from `../archive.md`, and every WInS note, verbatim from
`../../../caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`), V53 (pitch + IPS,
`../../ips_rewrite/drafts/D33/`, paragraphs numbered) and eight offered lines (O1 "one rung"; O2 "none sold"; O3 "the
ladder and everything set aside for it"; O4 cut "We buy them"; O5 Laura's Room's quarter; O6 "to attract
co-sponsors"; O7 cut "under a tenth"; O8 the Archive's "before her gift does"), with no reasons and no names. It was not
shown the register (A1-A30), FRONTIER, or the Archive's own verdict ("no breach"). Asked: where would a judge with the
locked record open read a contradiction, HIGH / MEDIUM / LOW, with the smallest fix; then each offer, more or less
consistent. The Long Room's D (19:31) landed after the reader started; the Archive checked D itself (below).

| # | Its rating | Its finding (its words in quotes) | Archive ruling |
|---|---|---|---|
| 1 | HIGH | P8 "set it aside from the stocks Laura keeps ... Whatever the stocks can't cover lowers the whole range" against reflection 3 ("the only investment not standing between Laura and a payment deadline") and the VT note ("They only set how far her gift rises"): "They become the first buffer against a ladder shortfall, so they do stand behind a payment." Fix: "set it aside, in Treasuries, from the stocks Laura keeps" (+2) | **Overturns the Archive's "no breach". A19: words breach, design inside.** The model sells the gap and cushion from her half on naming day into short Treasuries (`../long_room/LR8_banked_at_the_mark/run.py:29`, then `x * bill2` to 2033; on V53's own design `../lab/L-16_two_jobs_one_pocket/run.py:41`, `:47`, `c0 = L33 + x_ * bill2`), so after 2031 no share price stands between Laura and the 2031 gap. V53 never says where the money goes, so a reader keeps it in stocks until January. Yesterday's reader rated the undated line HIGH; today's rates the dated one HIGH. The date was half the cure; the home is the other half. Take the reader's +2; keep "Whatever the stocks can't cover" (its "-1" makes "that" point nowhere) |
| 2 | MEDIUM | Pitch "We buy them" and P3 "A Treasury held to maturity pays exactly what it promises" against reflection 2's "net asset value, as opposed to a promise of par" and four notes' "payout is not fixed". Fix: "(their payout isn't fixed)" (+4) | **HOLDS by Caplet's call** (26 Oct, BIBLE rule 3: "exact sums on exact dates" allowed for the funds held to their December close; no hedge, A14). The sentence is said of a Treasury, and reflection 2 already told the judges the funds pay a NAV. Disagreement reported, not settled by Keel: the Long Room's actuary said the same tonight. The pitch's "Treasuries" is the IBTR note's own sentence ("her first $300,000 is enough to buy Treasuries for all ten payments") |
| 3 | MEDIUM | P5's floor ("buys a Treasury fund maturing in late 2032") reads as an eleventh holding against the IBTM note's "two jobs". Fix: "buys more of the late-2032 Treasury fund behind her first cheque" (+4) | **A30, WATCH, second blind flag** (HIGH yesterday). Consistent in fact (one fund, two earmarks, matures in December 2032 before both uses). No IPS words free once the cure is in (D 497); the Final Report says it in a line |
| 4 | LOW | "Treasury floor" (pitch) and "money she already owns" (P6) against "not fixed" | Covered by P6's "rounded down" (A5) |
| 5 | LOW | P9 "one bond per cheque": five rungs are funds | **O1 / D: "one rung" (0).** Take it |

**Its "looks like a clash, isn't" list** matches the register: P8 "falls short" v "near-ironclad" (A20); the 7.5% (A1);
the WInS book holding VT and the floor (A32 new: "scaled to the model portfolio"); P5's top-up v the IBTR note (A23);
P4 "already bought" (A24); Taiwan-dollar costs v the no-TIPS line (A2); the 2031 move (A27).

**Its reading of the offers:** O1 MORE; O2 MORE, slightly ("applies only to the ten holdings"); O3 MORE (internal; it
places P8's cushion, as D's P9 now does); O4 MORE, marginally; **O5 LESS** ("it makes the stocks' role as a backstop larger
and more explicit"); O6 and O7 no effect; **O8 MORE, slightly** ("'Gift' is the record's word").

**The Long Room's D, checked by the Archive against the same record** (`../../huddles/2026-11-02_what-the-last-line-asks/arms/D_round2_majority.txt`, sha256 `fb9c9a8463ce9ddd`, 495 strict):
- P2 "Crushing one means selling it before its January, even for the building." Consistent with reflection 1
  ("untouched") and A30 (the floor's fund matures before the building is paid). Loose at one rung: the Feb-2037 bond
  (Trading Note 1) matures in February 2037 and its money waits in a short-term Treasury fund (and the May-2038 bond's, for 2039) that is
  sold to pay that cheque, so "before its January" catches a sale the plan makes. **"before it matures" (0) is true of all ten**
  (F19, Kai, 1 Nov). Optional; the six-of-six say-back was on "before its January".
- P3 cut "We buy them": no locked stake; the pitch keeps it, and A20 holds with A19's cure.
- P9 "the ladder and the money set aside for its gap become the operating reserve, paying out one rung per cheque":
  consistent, and with "in Treasuries" in P8 the reserve's composition is said in words (case :95-96).
- The order line cut: no locked stake, but it was the only sentence telling a judge the stocks come last. Without it,
  P8's "in Treasuries" is the line that keeps reflection 3 true. Take them together.

**So.** The reader found one thing the Archive missed and rated it the most serious: not what the plan does, but that
the words never say the gap money leaves the stocks. Count copy, D + the cure: `V54D_archive_repaired_ips.txt` (497
strict; textcheck). V53 + the cure alone is 499, over the 497 rule, so it needs D's cuts.
