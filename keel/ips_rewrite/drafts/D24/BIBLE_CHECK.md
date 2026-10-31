# AI-generated check (Claude), 31 Oct 2026, not for submission

**For the team lead, in six lines.**
1. **Counts:** pitch **50/50**, IPS **497/497** strict (493 by spaces), from `office/tools/textcheck.py`. The cap is 497, so every fix in section E is paid for by cutting a whole idea. All the cuts are named, and the full package was measured.
2. **Commandments: PASS 4 (II, VII, IX, X) · FAIL 6 (I, III, IV, V, VI, VIII).** VI can't be passed from these sessions. V fails on one sentence, which the V43 check let through.
3. **Biggest misses:** (a) certainty is defined as "a list" but never tied to a measure. The one reliability figure ("ours, under one in sixty") lumps the cheques together with the co-sponsor promise and has no "says who" in its own sentence. (b) There is no real team event: "we made it first" is a gesture towards a confession that never comes, and judges J1, J4 and J5 on panel V44 all named this. (c) The pitch never says what the stocks are for, and its "the change" stopped two judges.
4. **What V44 fixed:** "ladder" is now introduced; both letters of XR are stated; "nothing sold early" is said plainly; the "same note" over-claim is gone; the 97's condition is stated; the pitch's stock purchase is now accurate; our own failure rate now sits beside the 60/40's (the actuary judge put V44 first for that); kickers are down from six to four; and the unsourced "fifteenth" is gone.
5. **What V44 broke:** "range" still appears before it is introduced (it moved from P6 to P4). Both pun headings lost their payoff lines, and the cake heading is now orphaned. The stock sleeve is no longer sized (judges J2, J5 and J6 noticed). Colons rose from 6 to 7. D24 has no README, so there is no "GPTZero: not yet checked" label, no ten-line check and no number table, and V44 has no row in VERSIONS and no entry in THINKING_LOG.
6. **Tally:** A (198 rows) **MET 82 · PARTLY 58 · MISSED 3 · N/A 55**; B (34 rows) **MET 22 · PARTLY 11 · MISSED 0 · N/A 1**. Section E's package fixes the top five misses at **IPS 497 / pitch 50**, measured.

**What was checked.** `pitch.txt` and `ips_V44.txt` in this folder, read cold by a reader who didn't write them. I checked
them against `WHARTON_WORD.md`, all of `BIBLE.md` (the Ten Commandments included), every row of `BIBLE_AUDIT.md` s1
(each judged fresh for V44), the V43 check (`../D23/BIBLE_CHECK.md`), the case, `voice/06_voice_guide.md`, and
`IDEA_LEDGER.md` (including its V44 lines). For the numbers I used `models/results/suite_results.json` (M1, M7),
`models/ASSUMPTIONS.md`, `models/xr_core.py` and `rooms/lab/L-13_slide_the_range.md`. As corroboration only (never as
the marking scheme) I used the blind panel `judges/panel_V44/` (six judges' notes and SUMMARY) and voice reader 8
(`voice_first/readers/reader8_verdict.md`). I'm not an AI detector and I don't judge AI-ness here. I didn't edit the
draft. (`drafts/D25/` with V45 appeared while this check ran; it isn't checked here.)

V44's paragraphs, for reference: P1 opener · P2 "So we don't invest the promise. We buy it." · P3 the 2027 ladder ·
P4 certainty + the leak · H1 "Sell low, by appointment" · P5 "we made it first" + the 60/40 · P6 "But 'usually'" +
one in three / one in sixty + the bills · H2 "Have your cake and invest the icing" · P7 floor + fund + the note · P8 the
2031 range · P9 the catch + lock + 97 · P10 reserve + priority + XR · P11 "Do not crush."

## A. Every expectation in BIBLE_AUDIT s1, judged for V44

| # | Book | Expectation | V44 status | Evidence (V44's exact words, or what is absent) | Fix |
|---|---|---|---|---|---|
| 1 | CN | Rewrite slowly: long thinking, research, analysis | N/A: process | V44 is a same-day patch of V43 (Sat 31 Oct), the 14th version since Fri 30 Oct. It has no THINKING_LOG entry of its own | - |
| 2 | CN | THINK; don't be hasty | N/A: process | V44 was paid for by cutting whole ideas (ledger, V44 line), not by squeezing | - |
| 3 | CN | Creative, original, knowledgeable, evidently widely read | PARTLY | Original: "A high degree of certainty is a list, not an adjective."; "Laura doesn't owe one ten-year bill. She owes ten one-year bills". New knowledge signal: "swaps the bank's option for shares". Still only one borrowed concept is named ("a capital-protected note") | E5; not bought X5 |
| 4 | CN | All Bibles equal; grasp the intent | N/A: process | - | - |
| 5 | CN | Autonomy; may question Caplet | N/A: process | - | - |
| 6 | CN | Expectations met, however disseminated | N/A: process | This file is V44's item-by-item check | - |
| 7 | B1 | Distinctive team voice | PARTLY | Present: "But "usually" is the whole trick", "– or nearly –", "Do not crush.", "Sell low, by appointment". Against: the opener is the field's default shape (row 9); four kickers against a ration of three (row 35); voice reader 8 ranked V44 third of four, saying it "explained its own pun in a bracket" | E4 |
| 8 | B1 | Voice carries throughout, pitch included | PARTLY | "the change buys world stocks" is how a person talks, but the colon mirror "doesn't invest the promise: her first $300,000 buys it" stays, and J4 and J5 both stopped at "the change" | E2 |
| 9 | B1 | Sound unique, unlike any other team | PARTLY | Still opens "Laura Gao has one promise and one hope." (the default rival's shape, ledger A1) | Writer's call, 0 words |
| 10 | B1 | Cerebral yet witty | MET | "Sell low, by appointment"; "leaves out the bank (and its fee)"; "Do not crush." | - |
| 11 | B1 | Passionate yet thoughtful | PARTLY | The only concrete stake is "a building priced in Taiwan dollars". Who the residency is for (artists, writers, educators: case p.2) never appears | FR (voice guide s7) |
| 12 | B1 | Insightful yet confident | MET | "The US government defaults." said flat; no hedges | - |
| 13 | B1 | Judges enjoy reading it | PARTLY | The "But" turn and the close work. Readers stop at: "The US government defaults." (it reads as a claim until you see it's a list item); "before any range is named" (no range yet); "breaks its word to co-sponsors" (J4); "ours, under one in sixty" (J6); "swaps the bank's option" (J1, J2) | E1, E3, E7 |
| 14 | B1 | One unifying motif across the IPS | PARTLY | XR appears only in P10-P11. The cake heading lost its callback ("A crash can cost her the icing, never the cake." was cut), so it's now a decoration competing with the capsule | C1 |
| 15 | B1 | Elaborate, vast motif | N/A: Final Report | - | - |
| 16 | B1 | Intellect and investing knowledge before language | PARTLY | New: the note's insides ("the bank's option"). Still described but not named: sequence risk ("a crash in the wrong year forces a sale at the bottom"), reinvestment risk ("coupons paid early earn less if yields fall"), pull-to-par ("funds that mature like bonds"), human capital (P4) | Not bought X5 |
| 17 | B1 | Intellect and language together | PARTLY | Strong language; the knowledge on the page is still thin | X5 |
| 18 | B1 | Truly extraordinary, not just competent | PARTLY | The skeleton is still the field's (ladder + stocks + lock: Commandment I). Panel V44's mean ranks: V40 1.67, V43 and V44 3.17 | - |
| 19 | B1 | Something no one else would think of | PARTLY | Rare, and present: "a recession arrives before we buy: it pushes yields down, so the ladder costs more, and it shrinks the advances, speaking and licensing behind the 2028 deposit" (J5 learned this from it) | - |
| 20 | B1 | An "aha" | PARTLY | "Laura doesn't owe one ten-year bill. She owes ten one-year bills" (J5: "the sharpest reading of the client's problem in the set") | - |
| 21 | B1 | Keep these in your back pocket | N/A: process | - | - |
| 22 | B2 | Name unique | MET | Caplet XR | - |
| 23 | B2 | Nothing roots-themed | MET | No root, branch or tree words | - |
| 24 | B2 | Name tied to the motif | MET | "We call the plan Caplet XR, after the extended-release capsule" | - |
| 25 | B2 | Name fits the strategy, not a stretch | MET | "(X for ten, R for redemption): one cheque a year" (fixed from V43) | - |
| 26 | B2 | Motif not in every sentence | MET | One paragraph and the close | - |
| 27 | B2 | Subtle, not decorative or layered on | MET | It now argues: "with nothing sold early" sets up "it only works whole" and "Do not crush." (fixed from V43). J4 still found "Do not crush." opaque | - |
| 28 | B2 | Motif builds the narrative arc | PARTLY | The set-up and the payoff both sit in the last 30 words, so it's an ending, not an arc | Not bought (writer's call) |
| 29 | B2 | One image; write like we write | PARTLY | The capsule, cake and icing (now an orphaned heading), "by appointment", and the leak | C1 |
| 30 | B2 | Only our team could have the name | MET | - | - |
| 31 | B2 | Optimise for ourselves first | MET | - | - |
| 32 | B2 | Motif creative and unexpected ("huh") | MET | "the extended-release capsule (X for ten, R for redemption)": the "huh" no longer depends on the judge decoding it | - |
| 33 | B2 | Unexpected connections, syntheses | PARTLY | The bank's note rebuilt from Treasuries and shares; rates × her income (P4); the capped range as a one-sided bet (P9) | FR |
| 34 | B2 | Sound deeply human | N/A: needs GPTZero | No score. D24 doesn't even carry the "not yet checked" label (no README) | README label (row 121) |
| 35 | B2 | Lean but messy, human | PARTLY | Four kickers: "We buy it.", "(and its fee).", "it only works whole.", "Do not crush." (V43 had six) | E5 + C3 drops one |
| 36 | B2 | Cut the human way, not by rearranging | PARTLY | Met for the cuts: three whole ideas went (ledger V44 line). Two squeezes remain: "is a list, not an adjective" and the gapped clause "; ours, under one in sixty" | E1, E7 |
| 37 | B2 | Parsimonious and lucid | PARTLY | Lucidity slips: "range" in P4 before P8 introduces it; "The US government defaults."; pitch "the change"; "we made it first" (made what, first of whom?) | E2, E3, E4, E7 |
| 38 | B2 | Light study of the essays | N/A: process | - | - |
| 39 | B2 | Humanising lists don't work | N/A: process | - | - |
| 40 | B2 | Write more like Ahaan (tone) | MET | En-dash asides, a real "But" turn, long build then short landing ("She owes ten one-year bills"), contractions, "cheque", "towards", "dearer" | - |
| 41 | B2 | Essays are tone, not everything | N/A: process | - | - |
| 42 | B3 | Caplet XR clever; justifies the team name | MET | P10 | - |
| 43 | B3 | Extend it (timed release, do not crush, more) | MET | "one cheque a year"; "Do not crush." | - |
| 44 | B3 | A second meaning of XR | MET | "X for ten, R for redemption" | - |
| 45 | B3 | "Extended response" | N/A: superseded by Book 5 | - | - |
| 46 | B3 | Product-tier label in intro or close | N/A: Final Report | Ledger A6 | - |
| 47 | B3 | Free to change name or motif | N/A: locked by Book 5 | - | - |
| 48 | B3 | Flair, voice, no over-claim obsession | MET | "The US government defaults."; "Do not crush." | - |
| 49 | B3 | Don't actively over-claim | MET | "the same note" is gone (fixed). "under one in sixty" is true, and conservative (D). Minor: the pitch's "her first $300,000 buys it" drops the IPS's "or nearly" | - |
| 50 | B3 | Judges aren't mini-Lauras | MET | It argues investing to a judge | - |
| 51 | B3 | No time on grammar | N/A: process | - | - |
| 52 | B3 | En dashes | MET | Four (two spaced pairs) | - |
| 53 | B3 | Marinate | N/A: process | - | - |
| 54 | B4 | Rewrite from scratch; all expectations implemented | PARTLY | V43 was the rebuild; V44 patches it. "All implemented": see this table | Section E |
| 55 | B4 | Stop tinkering on the old version | N/A: process | - | - |
| 56 | B4 | Extraordinary knowledge of concepts | PARTLY | Named: "ladder" (now introduced), "capital-protected note", "60/40", "operating reserve", "index fund", "rebalance" (in "nothing to rebalance"). Unnamed: row 16 | X5 |
| 57 | B4 | No name-dropping | MET | - | - |
| 58 | B4 | Niche concepts applied and explained | PARTLY | The note is explained one step further ("swaps the bank's option for shares"), but never says what the option does. J1: "I could not tell what option was given away" | E5 |
| 59 | B4 | Research uncited in IPS, cited in FR | MET | No citations | - |
| 60 | B4 | FR shows wide reading | N/A: Final Report | - | - |
| 61 | B4 | Knowledge supports the narrative | MET | - | - |
| 62 | B4 | North stars, all four equal | N/A: process | - | - |
| 63 | B4 | Long research process | N/A: process | - | - |
| 64 | B4 | Dazzling by 6 Nov | N/A: due later | The final for review is due end of Wed 4 Nov | - |
| 65 | B5 | Keep Caplet XR | MET | - | - |
| 66 | B5 | State the literal "extended release" | MET | "the extended-release capsule" | - |
| 67 | B5 | Both meanings of XR in the IPS | MET | Literal and ours, both in P10 | - |
| 68 | B5 | Bare bones of the motif | MET | - | - |
| 69 | B5 | Everything out by the FR | N/A: Final Report | - | - |
| 70 | B5 | Make it clear the name is clever and thought out | MET | The bracket makes it clear. (Voice cost: reader 8 says the author "never explains his own joke"; writer's call) | - |
| 71 | B5 | X = 10 | MET | "X for ten" (fixed from V43) | - |
| 72 | B5 | R not "release" | MET | "R for redemption"; "release" appears only in the literal "extended-release capsule" | - |
| 73 | B5 | No fretting over sure-sounding words | MET | - | - |
| 74 | B5 | iBonds: exact sums on exact dates | MET | "Treasury funds that mature like bonds, one rung falling due before each January" | - |
| 75 | B5 | May say near-ironclad; distinction concise | MET | Not used (optional) | - |
| 76 | B5 | Accuracy matters | PARTLY | Fixed: "the same note", the pitch's "only their interest". Loose: "ours, under one in sixty" comes from M7's xr_lock design (set-aside in 2033 plus a $7,500 cushion), not the 2031 set-aside the text describes (L-13); the 60/40's one in three rests on a rival range Keel assumed (±20%; with ±40% it's about one in four); "just enough to grow back into all of it" is true only when the 2027 ladder needed no top-up (the case today, $1,139 to spare) | E1 (scope); D |
| 77 | B5 | Human flair | MET | Headings; "Do not crush." | - |
| 78 | B5 | No hedging | MET | - | - |
| 79 | B5 | Test on essays + TNA, not only Orwell | N/A: process | Voice reader 8 read V44 against the essays | - |
| 80 | B5 | Use Ahaan's voice, not a robotic one | PARTLY | Rows 35, 119 | E4 |
| 81 | B5 | Extraordinary | PARTLY | Row 18 | - |
| 82 | B5 | Distinctive, erudite, clever | PARTLY | Clever, yes; erudite, thin | X5 |
| 83 | B5 | Final by Sat 31 Oct | N/A: superseded (Wed 4 Nov) | - | - |
| 84 | B5 | Meet every expectation | PARTLY | This table | - |
| 85 | B9 | Meets all Wharton requirements | PARTLY | Certainty is defined and now given a number, but the two don't meet (W12). The inflation assumption is absent (case p.4). Diversification is thin | E1, E7; X1 |
| 86 | B9 | Don't focus on formatting | N/A: process | - | - |
| 87 | B9 | Seen as intelligent and knowledgeable | PARTLY | The logic is strong; most concepts go unnamed | X5 |
| 88 | B9 | Search for niche concepts | N/A: process | - | - |
| 89 | B9 | Fuse strategies; synergies | PARTLY | The note rebuilt from Treasuries and shares; rates × income. What the fusion costs us isn't said | E5 |
| 90 | B9 | Dig in unexpected places | N/A: process | - | - |
| 91 | B9 | Analyse and critique borrowed ideas | PARTLY | The 60/40 is critiqued with numbers. The note: "leaves out the bank (and its fee)" says what ours avoids, never what it gives up (an option catches more of a rally, but can expire worthless) | E5 |
| 92 | B9 | Show an idea that seems right but isn't | MET | "a 60/40 portfolio usually ends 2042 almost $200,000 ahead of ours. But "usually" is the whole trick" | - |
| 93 | B9 | Show knowledge of strategies few know | PARTLY | Only the protected note | X5 |
| 94 | B9 | Our own strategy for our client | MET | P4's advances, speaking and licensing | - |
| 95 | B9 | Logic: chains to their conclusion | MET | The recession chain (P4); the cap → "every fall in stocks comes off the gift while every rise past the top goes to Laura" → the lock (P9) | - |
| 96 | B9 | Case studies, evidence | PARTLY | Model figures only (M7, L-13); M1's history unused | FR |
| 97 | B9 | Voice is qualitative | N/A: process | - | - |
| 98 | B9 | Use Wall Street writers too | N/A: process | - | - |
| 99 | B9 | Don't use own agents as detectors | N/A: process | None used here | - |
| 100 | B9 | Use real web detectors | N/A: process | Not run (DETECTOR_LOG) | - |
| 101 | B9 | Detection is low priority | N/A: process | - | - |
| 102 | B9 | Don't obsess over 7.5% for VT | MET | "with world stocks at 7.5% a year": world stocks, not VT, said once | - |
| 103 | B9 | Not hamstrung by the TNA | MET | - | - |
| 104 | B9 | Use studies like the donor study | PARTLY | The lead-gift line is in the ledger for the FR. J5 and J6 on panel V44 asked for the reason behind the range's shape | Not bought X6 |
| 105 | B9 | Turn model findings into arguments | MET | M7 now gives both sides of the price of safety ("one time in three ... ours, under one in sixty"); L-13 the 97 | - |
| 106 | B9 | Every good idea lands somewhere | MET | The ledger's V44 line records the three cut ideas as FR | - |
| 107 | B9 | Research is for the deliverables | N/A: Final Report | - | - |
| 108 | B9 | Don't discard ideas wantonly | N/A: process | As row 106 | - |
| 109 | B9 | Pitch not AI-squeezed; cut the human way | PARTLY | The last sentence is now a full clause ("and the change buys world stocks"), which is fixed. The colon mirror "doesn't invest the promise: her first $300,000 buys it" stays | E2 |
| 110 | B9 | No artificial timeline | N/A: process | - | - |
| 111 | B9 | Work more densely | N/A: process | - | - |
| 112 | B9 | No AI-use logging | N/A: process | - | - |
| 113 | B9 | No minute changes; big picture | N/A: process | - | - |
| 114 | B9 | Judges don't read for precision | N/A: process | - | - |
| 115 | B9 | Put message in the Bible | N/A: process | - | - |
| 116 | B10 | Diverse mock judges | N/A: process | `judges/panel_V44/SUMMARY.md`: six judges, mean Kendall tau 0.24, four different #1 reasons | - |
| 117 | B10 | Judges don't approve every change | N/A: process | Panel V44 put V44 joint second on mean rank, below V40 | - |
| 118 | B10 | Judges don't think like Keel | N/A: process | - | - |
| 119 | B10 | Apply the voice studies | PARTLY | Applied: concession, then "But"; long build, short landing; a close that's an act. Not applied: law 7 (no real confession: "we made it first" is a gesture, as reader 8 put it); law 6 (three frames); law 9 (four kickers, not three); law 10 symmetry ("So we don't invest the promise. We buy it."; "a list, not an adjective") | E4, C1, E7 |
| 120 | B10 | Pitch reads as obvious AI | PARTLY | Row 109 | E2 |
| 121 | B10 | GPTZero before Caplet | MISSED | No score (can't be had here), and D24 has no README, so the label the commandment requires instead ("GPTZero: not yet checked") is missing too | Add D24/README with the label |
| 122 | B10 | "Human-written only" above 50% | MISSED | No score for the pitch or the IPS | A student pastes both into gptzero.me (DETECTOR_LOG) |
| 123 | B10 | Own voice matters more than the score | PARTLY | Row 119 | - |
| 124 | B10 | Use the human-vs-AI notes | PARTLY | Seven colons (V43 had six): "before we buy: it", "One leak remains: coupons", "the whole trick: about", "all of it: her floor", "has a catch: once", "runs itself down: each", "redemption): one cheque". The triad stays: "the cheques come first, then the floor, then the hope" | E1 removes one colon; X2 |
| 125 | B10 | No sentences so compressed they barely make sense | PARTLY | Fixed: the leak now reads plainly ("coupons paid early earn less if yields fall"). Left: "is a list, not an adjective"; "; ours, under one in sixty"; pitch "the change" | E1, E2, E7 |
| 126 | B10 | Natural variation and flair | MET | From "Do not crush." (3 words) to the 34-word ladder sentence | - |
| 127 | B10 | Judges don't fixate on single lines | N/A: process | - | - |
| 128 | B10 | Mark only to Wharton's guide | N/A: process | This check argues from section B | - |
| 129 | B10 | No "every team will" | MET | No comparison with other teams. (The 60/40 is a portfolio, not a team) | - |
| 130 | B10 | No numbers plucked from thin air | MET | Every figure traces to a run (D). The unsourced "about a fifteenth" is gone; the 97's condition is now in the text ("before any range is named") | - |
| 131 | B10 | "We model", never "we judge" | MET | "in our model" ×2; "we price"; no "we judge" | - |
| 132 | B10 | Stop obsessing over AI use | N/A: process | - | - |
| 133 | B10 | Drop "required trading activity" | MET | Not raised | - |
| 134 | B10 | Final by end of Wed 4 Nov | N/A: deadline | - | - |
| 135 | B10 | Overdrive | N/A: process | - | - |
| 136 | B10 | Demonstrate more work per day | N/A: process | - | - |
| 137 | B10 | Top 50 of 2,300; whatever it takes | N/A: process | - | - |
| 138 | B10 | Number one: extraordinary, not ordinary | PARTLY | Row 18 | - |
| 139 | B10 | Fresh commandments | N/A: process | - | - |
| 140 | B10 | Commandments must be followed | MISSED | D24 has no README with the filled ten-line check that BIBLE requires of every draft; section C below fails six lines | Paste section C into D24/README |
| 141 | B10 | Final IPS satisfies all expectations | PARTLY | This table | Section E |
| 142 | B10 | Recursive self-improvement | MET | V44 carries six of the V43 check's seven fixes (ladder, "breaks its word", X/R, "nothing sold early", "swaps", the pitch) plus X1's timing. E1 ($125k) was swapped for M7's own rate, and E5 was not taken | - |
| 143 | B10 | Initiative, intellectual risks | PARTLY | It takes risks in voice ("Do not crush." as the last line), none in strategy | - |
| 144 | B10 | Guess what Caplet will say | N/A: process | THINKING_LOG has no V44 entry (its last is the V42/V43 afternoon round) | Add one |
| 145 | B10 | Rewrite from scratch again | MET | V43 was rebuilt from voice-first draft A; V44 builds on it | - |
| 146 | B10 | List every idea of every version | N/A: process | IDEA_LEDGER, V44 line | - |
| 147 | B10 | Best ideas end up in the new IPS | PARTLY | In: our own failure rate, the leak + set-aside timing, the catch + lock, 97, 7.5%, the 60/40 price, thoughtful risks, the note, human capital. Out: the first-plan confession (it was in V40, which three judges ranked first for it), the $125,000 break point, one borrower, the lead-gift line, inflation, the sleeve's size | E4; X1, X3, X6 |
| 148 | B10 | Add the message to the Bible | N/A: process | - | - |
| 149 | B10b | Wharton's word with the utmost importance | PARTLY | Section B: certainty isn't evaluated against its own definition, assumptions are thin, diversification is thin | E1, E7 |
| W1 | W1 | Clear and creative thesis | PARTLY | Clear: "So we don't invest the promise. We buy it." Creative more in framing than in structure (row 18) | - |
| W2 | W1 | Disciplined planning across horizons and cash flows | MET | 2027 ladder; 2028 floor + fund; 2031 set-aside, range, lock; 2033 reserve | - |
| W3 | W1 | Appropriate diversification | PARTLY | Stocks: "one world index fund" only. Cheques: "The US government defaults." names the concentration, but no sentence argues for it | FR |
| W4 | W1 | Consistent with IPS/TNA/WInS | MET | The Treasury bonds + iBond funds rung by rung, the IBTM-like "Treasuries maturing late in 2032", one world fund (VT), and the 2028 deposit filling any gap first all match `00_GROUND_TRUTH` s3 | - |
| W5 | W1 | Tailored to circumstances, priorities, risk considerations | MET | "Laura is willing to take thoughtful risks" answered by "But "usually" is the whole trick"; her income in P4 | - |
| W6 | W1 | ... and residency goals | MET | "a gift towards the residency's building in Taiwan"; "a building priced in Taiwan dollars comes in dearer" | - |
| W7 | W1 | Thoughtful understanding of the client | MET | P4 | - |
| W8 | W1 | Recommendations that can earn her confidence | MET | "The bottom is the floor she has owned since 2028." | - |
| W9 | W1 | Understanding and use of concepts and tools | PARTLY | Row 56 | X5 |
| W10 | W1 | Quantitative + qualitative | MET | M7 and L-13 alongside the calendar argument | - |
| W11 | W1 | Reasonable assumptions and projections | PARTLY | One assumption is stated ("world stocks at 7.5% a year"). Nothing on rates or inflation, and the model is never described; J6: the one-in-sixty "has no stated assumptions behind it" | Not bought X1 |
| W12 | W1 | Evaluate reliability, facility, flexibility under varying outcomes | PARTLY | Improved from V43: reliability now has a number ("ours, under one in sixty"); facility, "about 97 times in 100"; flexibility, "The other half stays hers". But P4's definition ("a list") and P6's number never meet. The number mixes cheques with the co-sponsor promise (J6 couldn't tell which). No outcome other than "on average" is shown | E1, E7 |
| W13 | W1 | Articulation: teamwork, process, learning | PARTLY | Only "There is a serious case against all this, and we made it first." J1: "the lack of any account of how the team got here"; J4 and J5 ranked V40 first for its first-plan story | E4 |
| W14 | W1 | Compelling, organised narrative | MET | Promise → ladder → certainty → opponent → floor → range → catch → reserve → name | - |
| W15 | W1 | Authentic team voice | PARTLY | "we" ×6, "our/ours" ×8; not detector-checked | - |
| W16 | W1 | Data used effectively | MET | "almost $200,000 ahead"; "one time in three ... under one in sixty"; "97 times in 100" | - |
| W17 | W1 | Original thinking, meaningful reflection | PARTLY | Original thinking, yes; the reflection is one vague clause | E4 |
| W18 | W1 | Contribution and uncertainty clear and credible to co-sponsors | MET | The bottom is owned; the catch is explained and the lock closes it; 97 in 100 | - |
| W19 | W2 | Invest to support goals and cash flows while managing risk | MET | - | - |
| W20 | W2 | Reflect goals, horizons, liquidity, certainty, flexibility | MET | Liquidity: "each turns to cash before its cheque", "to sell any day"; flexibility: "The other half stays hers" | - |
| W21 | W2 | Q: central idea | MET | "So we don't invest the promise. We buy it." | - |
| W22 | W2 | Q: principles | MET | Now all on the page, unlabelled: buy the promise; "nothing sold early"; "the cheques come first"; on naming day "the half she promised moves into Treasuries" | - |
| W23 | W2 | Q: balance growth, risk, liquidity, reliability, flexibility | PARTLY | The balance is argued (the concession, the $200,000 price, the "But"), but with "about a fifteenth" cut, growth's share is sized nowhere. J5: "the growth sleeve is never sized"; J6: "no sizing of the interest sleeve" | Not bought X3 |
| W24 | W2 | Q: allocation changes as needs approach and payments are made | MET | 2028 floor; 2031 "the half she promised moves into Treasuries"; 2033 "it runs itself down" | - |
| W25 | W2 | Q: protect the commitment, keep flexibility for the contribution | MET | P8-P10 | - |
| W26 | W2 | Remember whom it serves | MET | - | - |
| W27 | W2 | Pitch: strategy, central idea, how it supports her goals | PARTLY | It names the cheques, the gift and the stocks, but never links the stocks to the gift. J4: "the pitch never says what the world-stock part is for" | E2 |
| W28 | W2 | IPS: risk and return | MET | The return assumption, the 60/40 trade-off, the risk list | - |
| W29 | W2 | IPS: construction and diversification | PARTLY | W3, W23 | - |
| W30 | W2 | IPS: reserve composition over time | MET | "each turns to cash before its cheque, with nothing sold early and nothing to rebalance" | - |
| W31 | W2 | IPS: responsible facility contribution | MET | Bottom = floor; top = floor + half the stocks; the other half kept | - |
| W32 | W2 | IPS: appropriate flexibility | MET | "to sell any day if a building priced in Taiwan dollars comes in dearer" | - |
| W33 | W2 | Framework, not individual investments | MET | - | - |
| W34 | W2 | No final reserve sums, projections, final range | MET | No sums and no range; "97 times in 100" is the rule's confidence | - |
| W35 | W2 | No citations, charts, links | MET | - | - |
| W36 | W2 | Strategy can't be revised | MET | Dated rules | - |
| W37 | W3 | Reasoning, assumptions, trade-offs | PARTLY | Reasoning and the trade-off are strong ("almost $200,000 ahead"). Assumptions: one (W11) | X1 |
| W38 | W3 | Cohesive across market outcomes | MET | - | - |
| W39 | W3 | Planned adjustments, not rewritten when markets move | MET | "with nothing sold early and nothing to rebalance" (fixed from V43) | - |
| W40 | W4 | Strategy leads across deliverables | MET | - | - |
| W41 | W4 | Know your client | MET | - | - |
| W42 | W4 | Use WInS to demonstrate | N/A: WInS/FR | - | - |
| W43 | W4 | Don't focus on performance | MET | - | - |
| W44 | W4 | Explain why each investment belongs | PARTLY | Treasuries (the calendar) and the world fund (only the interest) are explained. Why Treasury funds as well as bonds is not; J5 couldn't tell what "Treasury funds that mature like bonds" are | FR |
| W45 | W4 | Follow the instructions | PARTLY | W12 and W11 (case p.3: "explain how they evaluated that level of certainty"; p.4: inflation among the assumptions) | E1, E7 |
| W46 | W5 | Only WInS stocks, ETFs, Treasuries | MET | The note and its option are a foil only ("Banks sell this"; ours "swaps the bank's option for shares") | - |
| W47 | W6 | "Responsibly contribute"; keep flexibility | MET | "The other half stays hers" | - |
| W48 | W6 | "Willing to take thoughtful risks" | MET | The case's words, without quote marks, conceded then answered | - |
| W49 | W6 | 2028 deposit from advances, speaking, licensing | MET | "shrinks the advances, speaking and licensing behind the 2028 deposit" | - |

## B. Wharton's word, item by item (`WHARTON_WORD.md`)

| # | Source | Item | V44 status | Evidence | Fix |
|---|---|---|---|---|---|
| Q1 | IPS question | Central idea | MET | "So we don't invest the promise. We buy it." | - |
| Q2 | IPS question | Guiding principles | MET | W22: buy the promise; nothing sold early; cheques first; lock on naming day | - |
| Q3 | IPS question | Balance growth, risk, liquidity, reliability, flexibility | PARTLY | Argued, but growth is never sized (W23) | X3 |
| Q4 | IPS question | Allocation change as needs approach and payments are made | MET | 2027 → 2028 → 2031 → 2033 | - |
| Q5 | IPS question | Protect the commitment while keeping flexibility for the contribution | MET | P8-P10 | - |
| Q6 | IPS instruction | Remember whom it serves | MET | - | - |
| M1 | Make it clear | What we're trying to accomplish | MET | P1 | - |
| M2 | Make it clear | Why it's appropriate for the client | MET | Thoughtful risks answered; her income (P4) | - |
| M3 | Make it clear | How it balances the five | PARTLY | As Q3 | X3 |
| M4 | Make it clear | How it guides construction and decisions as needs change | MET | Dated rules; "nothing sold early" | - |
| M5 | Make it clear | Protect payments while supporting a responsible contribution | MET | "the cheques come first"; "the floor she has owned since 2028" | - |
| P | Pitch | Summarise; central idea; how it supports goals and funding needs | PARTLY | Central idea and both goals, yes. What the stocks do for the gift, no (W27) | E2 |
| I1 | IPS para | Tailored to goals, horizons, needs | MET | - | - |
| I2 | IPS para | Risk and return | MET | W28 | - |
| I3 | IPS para | Liquidity | MET | "each turns to cash before its cheque"; "to sell any day" | - |
| I4 | IPS para | Construction and diversification | PARTLY | W3, W23 | - |
| I5 | IPS para | Planned changes as needs approach | MET | - | - |
| I6 | IPS para | Prepare for the operating commitment; reserve composition | MET | P3, P10 | - |
| I7 | IPS para | Responsible facility contribution; flexibility | MET | P8 | - |
| J1 | Guide | Reasoning, assumptions, trade-offs | PARTLY | W37 | X1 |
| J2 | Guide | Cohesive across outcomes | MET | - | - |
| J3 | Guide | Not rewritten because markets move | MET | "nothing sold early and nothing to rebalance"; "Do not crush." | - |
| C1 | Criterion | Investment Strategy | PARTLY | Clear thesis, disciplined dates, consistent. Diversification only implied | - |
| C2 | Criterion | Client Knowledge and Objectives | MET | Thoughtful risks, her income, Taiwan dollars, the kept half | - |
| C3 | Criterion | Portfolio Analysis | PARTLY | Reliability now has a number, but it isn't tied to the definition (W12); one assumption only (W11); concepts unnamed | E1, E7 |
| C4 | Criterion | Articulation of Competition Experience | PARTLY | One vague clause; the real event is missing (W13) | E4 |
| C5 | Criterion | Creativity and Presentation | PARTLY | Strong voice; co-sponsor communication clear. Against: "range" before it's introduced; an orphaned heading; four first-read stumbles on the panel (row 13) | E3, C1 |
| A1 | Advice | Let strategy lead | MET | - | - |
| A2 | Advice | Know your client | MET | - | - |
| A3 | Advice | Use WInS to demonstrate | N/A: WInS/FR | Consistent with the WInS book | - |
| A4 | Advice | Not about performance | MET | - | - |
| A5 | Advice | Explain why each investment belongs | PARTLY | W44 | - |
| A6 | Advice | Follow the instructions | PARTLY | W45 | E1, E7 |
| H | Hard limit | Permitted instruments only | MET | Treasury bonds, Treasury funds, one world index fund; no TIPS, STRIPS or options (the bank's option is the foil) | - |

## C. The Ten Commandments

- **I. Extraordinary: FAIL.** The three ideas a judge would retell are the ten one-year bills, the recession that hits
  both the ladder's price and the 2028 deposit, and the capped range's catch and the lock. The last rests on the lock,
  which is the field's default (BIBLE_AUDIT row 19), and all three sit on the default skeleton of ladder + stocks +
  lock. Panel V44's mean rank puts V44 joint second (3.17), behind V40 (1.67).
- **II. Wharton only: PASS.** The text answers all five IPS questions as a whole, and this check and panel V44 both argue
  from the criteria. The gaps that matter are W12 and W11.
- **III. Write like us: FAIL.** No README quotes where each move happens. Present: a concession and then "But" (P5-P6);
  a build then a landing ("She owes ten one-year bills"); a wry line ("leaves out the bank (and its fee)"). Missing:
  the real event ("we made it first" gestures at one; the first-plan story isn't there). Against the voice: the triad
  "the cheques come first, then the floor, then the hope", four kickers, seven colons.
- **IV. Clear on one reading: FAIL.** "range" is used in P4 ("before any range is named") before P8 introduces it.
  "The US government defaults." reads as a claim before it reads as a list item. On panel V44, the small-model skimmer
  (J1) did not understand "capital-protected note", "swaps the bank's option for shares" or "leak". J4 stopped at "the
  change", "Do not crush." and "breaks its word to co-sponsors"; J6 at "under one in sixty"; J5 at "the change" and
  "Treasury funds that mature like bonds". ("ladder" is now introduced: fixed.)
- **V. Every number explains itself: FAIL, on one sentence.** The test is "in its own sentence". P6's "about one time
  in three ... ours, under one in sixty" has no "says who": the "in our model" is in P5's sentence. Every other figure
  passes ("in our model" with the $200,000 and the 97; the 7.5% is said to be the model's; the rest are the case's).
  V43 had the same gap and its check let it through. E1 adds "in the same model".
- **VI. GPTZero before Caplet: FAIL, and it can't be met here.** GPTZero can't be reached from Keel's sessions
  (DETECTOR_LOG), so there's no "human-written only" score. Worse than V43: D24 has no README, so the "GPTZero: not yet
  checked" label the commandment requires in that case is missing. No agent stood in for a detector. A student pastes
  both texts into gptzero.me before Caplet's read.
- **VII. Few ideas at full size: PASS.** A judge could say it in three sentences. Her 2027 money buys the ten cheques
  as Treasuries, one maturing before each January. Her 2028 money buys a Treasury floor that grows back into itself,
  and the interest goes into a world index fund. In 2031 she names a range from the floor to the floor plus half the
  stocks, prices the coupon shortfall first, and locks the promised half in Treasuries that day.
- **VIII. Lose no idea; critique every borrowed one: FAIL (half met).** The ledger half passes: the V44 line records
  the three cut ideas as FR. The critique half fails: the capital-protected note is described ("swaps the bank's option
  for shares") but never critiqued for what ours gives up.
- **IX. Judges who disagree: PASS.** `judges/panel_V44/SUMMARY.md`: six judges with different models and priors, mean
  Kendall tau 0.24 (I recomputed it from the six score files: 0.236), with each judge's reasons in their own file. Four
  judges put V40 first, but for different reasons, and the actuary put V44 first.
- **X. Improve without being asked: PASS, narrowly.** V44 visibly carries the V43 check's fixes (row 142). But there
  is no THINKING_LOG "what Caplet would say" entry for the V44 round, and no VERSIONS row.

## D. Numbers

| Figure (where) | Source file and value | Wording matches? | Attribution |
|---|---|---|---|
| $50,000 a year for ten years (pitch); $50,000 every January 2033-2042; "ten cheques" (P1, P3) | Case p.3 | Yes | The case; none needed |
| $300,000 (2027); the 2028 deposit (pitch, P3, P4, P7) | Case p.2 | Yes | The case |
| "buys all ten cheques – or nearly" (P3); pitch "her first $300,000 buys it" | `suite_results.json` M1 `today_cost_bootstrap_22oct` $298,861 (A01: $1,139 to spare, 3.8bp); M1: $300k bought all ten in 25.2% of months since 1871 | The IPS, yes. The pitch drops "nearly": true at today's curve, but it can move by January | A market fact |
| "with world stocks at 7.5% a year" (P5) | `ASSUMPTIONS.md` A06: J.P. Morgan 2027 LTCMA global equities 7.5% compound, vol 16.78% | Yes; world stocks, not VT (Book 9) | "in our model, with" |
| 60/40 "usually ends 2042 almost $200,000 ahead of ours" (P5) | M7 `laura_2042_p50`, balanced vs xr_lock: $226,292 − $30,374 = $195,918 (lognormal); $228,752 − $30,660 = $198,092 (regime); $231,463 − $31,060 = $200,403 (bootstrap). Raw history is wider ($285k vs $34k) | Yes ("usually" = the median; the bootstrap is a hair over $200k) | "in our model" |
| "about one time in three the 60/40 misses a cheque or breaks its word to co-sponsors" (P6) | M7 balanced `p_any_promise_broken` 36.3 / 32.3 / 34.6% (history 29.6%). "Breaks its word" = gift below the bottom of the range it named, where that range is Keel's assumption (A23: its own projection ±20%). With ±40% (`regime_band40`): 23.6%, about one in four. Cheques alone: 6.1 / 7.7 / 6.0% | Yes, given A23 | **None in its own sentence** (Commandment V) |
| "ours, under one in sixty" (P6) | M7 xr_lock `p_any_promise_broken` 1.39 / 1.63 / 0.22%, history 0 (1/60 = 1.67%; the regime world clears it by 0.04 points). Cheques alone (`p_payment_short`, >$1,000 short): 0.19 / 0.24 / 0.02%. **Design:** xr_lock = V25 + lock + a $7,500 cushion, with the set-aside in Jan 2033 (A15, A19). The text describes L-13's design, where the shortfall is priced in 2031 before naming; there the cheques are short >$1k in 0.03-0.05% and the bottom is never broken | True and conservative, but from a different variant than the text describes; "either" isn't said, so the scope is unclear (J6) | **None in its own sentence** |
| "Treasuries maturing late in 2032" (P7); pitch "by 2032" | The plan: IBTM, Dec 2032 (`00_GROUND_TRUTH` s3) | Yes | Plan fact |
| "just enough to grow back into all of it" (P7) | A13: the floor is sized to grow back to R = deposit − any 2027 gap. Today's gap is $0 ($1,139 to spare), so R = $150,000 | True today; "all of it" fails if the ladder costs more than $300k by January | Plan |
| "the interest those bonds should earn" (P7) | Not given as a number. My one-off computation in `xr_core.py` at the 22 Oct curve, no shift: a 4.95-year yield of 4.78% → floor cost $118,717, leaving **$31,283 = 6.95% of $450,000 (about a fourteenth)**. No run file exists | n/a (no figure in V44) | - |
| 2031; "half her stocks"; "since 2028" (P8) | Case p.3; plan rule (ledger D1) | Yes. "The bottom is the floor" is approximate: M7's bottom is the floor less $3,700, rounded down to $5k (A14) | Case/plan |
| "the gift reaches its top about 97 times in 100" (P9) | L-13 with the slide: 97.9 / 97.6 / 96.0 / 96.7% (four worlds, 200,000 paths, V29 design + lock). Without the slide, M7 xr_lock `p_top_reached` is 84.1 / 84.5 / 93.2% | **Yes now**: P4 states the order ("set it aside from the hope, before any range is named"), which is L-13's slide | "in our model" |
| 2033; "the ten holdings" (P10) | Case p.3; plan | Yes | Case/plan |
| "X for ten" (P10) | Book 5 | Yes | - |
| **Proposed E1:** "in the same model ... Ours does either under one in sixty" | As the two rows above | Yes ("either" = cheque or co-sponsor promise, which is what `p_any_promise_broken` counts) | "in the same model" |
| **Proposed X1:** "Inflation can't make a fixed cheque cost more." | Case p.3: "each payment is a fixed $50,000 and is not adjusted for inflation" | Yes | The case |
| **Proposed X3:** "about a fourteenth of her money by our sums" | The computation above (6.95%) | Yes. The old "fifteenth" (6.67%) was slightly low | "by our sums"; needs a run file first |

Every model figure in V44 traces to a run. What's still loose: P6's two figures carry no attribution in their own
sentence, and "under one in sixty" comes from a more cautious variant of the plan than the one P4 describes.

## E. The misses, ranked by what a Wharton judge would notice, with exact fixes

The package below (E1-E5 and E7 for the IPS, E2 for the pitch, paid for by cutting C1-C3) was applied to V44's full text
and measured with `textcheck.py`: **IPS 497 strict (492 by spaces), pitch 50.** Deltas, each applied alone to V44:
E1 +7, E3 0, E4 0, E5 (with C3 inside it) +2, E7 +2, C1 −7, C2 −4 = **0**. (E5 alone, keeping the fee, is +10; C3
alone is −8.) The assembled text was used only to prove the count. It has had no GPTZero check, cold read or panel.

1. **Certainty is defined but not evaluated against its own definition (W12, W45, C3; case p.3 "define ... explain how
   they evaluated"; Commandment V).** P4 says certainty "is a list" without saying a list of what. P6's number names
   no model and mixes two promises.
   *E7:* "A high degree of certainty is a list, not an adjective." → "A high degree of certainty is a list of the ways
   it fails." (**+2**; "The US government defaults." then reads as item one, not a claim.)
   *E1:* "But "usually" is the whole trick: about one time in three the 60/40 misses a cheque or breaks its word to
   co-sponsors; ours, under one in sixty." → "But "usually" is the whole trick: in the same model, about one time in
   three the 60/40 misses a cheque or gives co-sponsors less than Laura promised. Ours does either under one in
   sixty." (**+7**; M7. It also fixes J4's "breaks its word" and J6's "covers both or only the cheques".)
2. **No real team event (W13, C4, law 7, Commandment III).** Three judges ranked V40 first for its first-plan story,
   and reader 8 called V44's version "the claim of a confession" without the confession. *E4:* "There is a serious
   case against all this, and we made it first." → "Our own first plan was three-quarters stocks, until our model sank
   it." (**0**; a real event: the team's original ~75%-stock plan, sunk by the 27 Sep simulation, CLAUDE.md
   "Growth-first ... failed".)
3. **The pitch doesn't say what the stocks are for, and "the change" stops readers (W27, P; J4, J5).** *E2:* the whole
   pitch becomes "Laura promised her residency ten yearly $50,000 cheques, and hopes to add a gift. Caplet XR doesn't
   invest the promise: her first $300,000 buys it, in Treasuries maturing before each January. Her 2028 deposit buys
   Treasuries that repay it in 2032, and what's left buys world stocks for the gift." (**50**; "worth all of it", whose
   "it" could mean the promise, becomes "that repay it".)
4. **The borrowed note isn't critiqued, and its jargon is opaque (Commandment VIII, rows 58, 91; J1, J2).** *E5:*
   "Ours swaps the bank's option for shares and leaves out the bank (and its fee)." → "Ours swaps the bank's option for
   shares, which catch less of a rally but can't expire worthless." (**+2** net.) That's true: an option bought with
   the same discount gets a leveraged share of the index's rise but can be worth nothing at maturity. It names what we
   give up and what we gain, and it explains the option in passing.
5. **"range" is used before it's introduced (Commandment IV, row 37).** *E3:* "before any range is named." → "before
   she names any gift." (**0**; it keeps L-13's order, so the 97 stays true.)

**The cuts that pay (whole ideas, not squeezes):**
- *C1: cut* the heading "Have your cake and invest the icing" (**−7**). Its callback ("A crash can cost her the icing,
  never the cake.") was cut in V44, so it now decorates, and it competes with the capsule (law 6: "In the IPS the image
  is Caplet XR; nothing competes with it"). "Sell low, by appointment" stays as the one heading. The cake image goes
  to the FR.
- *C2: cut* "and nothing to rebalance" (**−4**). "it runs itself down: each turns to cash before its cheque, with
  nothing sold early" already says the reserve needs no trading. The idea goes to the FR.
- *C3 (inside E5): cut* "and leaves out the bank (and its fee)" (**−8**). It's a kicker (four become three, law 9),
  and the fee point goes to the FR. If the team wants the wry line back, E5 alone costs +10, so C3's 8 words plus 2
  more must come from elsewhere (e.g. X4).

**Not bought (no words left; each is first in line if a cut above is rejected or the team accepts a further cut):**
6. **E7b, the second failure isn't stated as a failure.** "behind the 2028 deposit that must cover the gap." → "behind
   the 2028 deposit, just when it must cover the gap." (+2). It can be paid by X4.
7. **X1, no inflation assumption (W11, W37, J1; case p.4).** Add "Inflation can't make a fixed cheque cost more." after
   "one rung falling due before each January." (+8.)
8. **X3, the stock sleeve is never sized (W23, Q3; J2, J5, J6).** "buys one world index fund." → "buys one world index
   fund, about a fourteenth of her money by our sums." (+9; write a run file first: D.)
9. **X2, the triad (Commandment III).** "If anything changes, the cheques come first, then the floor, then the hope." →
   "If anything goes wrong, the hope gives way to the floor, and the floor to the cheques." (+4.) With X4 (−4) on top
   of the package, measured: **497**.
10. **X4, the cut that pays for 6 or 9:** the heading "Sell low, by appointment" (−4). Its payoff line ("selling low,
    on a timetable printed years in advance") was cut in V44, and reader 8 noticed. With X4 and E7b on top of the
    package, measured: **495**. Weigh this against keeping one pun heading.
11. **X5, concepts described but unnamed (rows 16, 56, W9).** e.g. "Planners call this sequence risk." before "Laura
    doesn't owe one ten-year bill." (+5). FR otherwise.
12. **X6, why a range at all: the lead-gift effect (row 104; J5, J6).** "In 2031 she gives co-sponsors a range, low
    enough to keep her word and high enough that her lead gift draws bigger ones." (+16). It's in the ledger for the FR.
13. **Process (costs no words; Commandments III, VI, X; rows 121, 140, 144).** Add `D24/README.md` with "AI DRAFT
    (Claude, 31 Oct); GPTZero: not yet checked", the quoted voice moves, the number table (section D) and the ten-line
    check (section C can be pasted). Add the V44 rows to VERSIONS and THINKING_LOG. A student gets a GPTZero score.
