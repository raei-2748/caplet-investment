# AI-generated check (Claude), 31 Oct 2026, not for submission

**V43 against V42.** *Fixed:* the return assumption is stated ("with world stocks at 7.5% a year"). The pitch names
the cheques, the residency and the gift in plain sentences. "Floor" is defined before it's used. The one-in-three
over-claim is gone. The coupon leak and its 2031 set-aside are back, the capped-range catch is two full sentences again,
and 97 in 100 is back with a source. "Thoughtful risks" is conceded and answered with a "But". "Do not crush." closes the
piece. "the interest they would have earned" is now "should earn". D23 has a README with the GPTZero label, a table of
numbers and the list of cuts. *Broke:* the certainty answer is no longer **evaluated**: the $125,000 break point was
cut, and the list's second entry no longer says it fails ("the 2028 deposit that must cover the gap"). "X for ten" is
gone, so neither letter of XR is stated. "Any rung can be sold any day. None will be." is gone, which leaves the
no-sale rule only in code ("it only works whole"). "Ladder" is now never introduced (V42 had "a ladder of Treasury
bonds"), and "range" is still used before it's introduced. The real confession ("Our first plan was three-quarters
stocks") became "we made it first". "Ours is the same note" is a new over-claim. Colons went from 2 to 6. And the pitch's
"only their interest buys world stocks" is inaccurate.

**What was checked:** `pitch.txt` and `ips_V43.txt` in this folder, read cold by a reader who didn't write them. I
checked against `WHARTON_WORD.md`, all of `BIBLE.md`, every numbered row in `BIBLE_AUDIT.md` s1 (all judged fresh for
V43), the case, `voice/06_voice_guide.md`, `IDEA_LEDGER.md` (including its new "V42 and V43" section), this folder's
README, and the number sources (`models/results/suite_results.json` M1 and M7, `models/ASSUMPTIONS.md`,
`rooms/archive_checks/A25_results.json`, `rooms/lab/L-13_slide_the_range.md`, `drafts/D19/README.md`). Counts from
`office/tools/textcheck.py`: **pitch 50/50, IPS 497 strict** (494 by spaces), cap 497. I'm not an AI detector and
don't judge AI-ness here. I didn't edit the draft.

**Tally.** Section A (198 rows): **MET 72 · PARTLY 67 · MISSED 1 · N/A 58**. Section B (34 rows): **MET 23 · PARTLY
10 · MISSED 0 · N/A 1**. Commandments: **PASS 4 (II, V, VII, X) · FAIL 6 (I, III, IV, VI, VIII, IX)**, and VI can't
be passed from these sessions.

V43's paragraphs, for reference: P1 opener · P2 "So we don't invest the promise. We buy it." · P3 the 2027 purchase ·
P4 certainty + the leak · H1 "Sell low, by appointment" · P5 the concession + the 60/40 · P6 "But 'usually'" + the
bills · H2 "Have your cake and invest the icing" · P7 floor + fund + the note · P8 the 2031 range · P9 the catch + lock
+ 97 · P10 reserve + priority + XR · P11 "Do not crush."

## A. Every expectation in BIBLE_AUDIT s1, judged for V43

| # | Book | Expectation | V43 status | Evidence | Fix |
|---|---|---|---|---|---|
| 1 | CN | Rewrite slowly: long thinking, research, analysis | N/A: process | V43 is the 13th version since Fri 30 Oct. The README says why it exists: rebuilt from voice-first draft A, not squeezed | - |
| 2 | CN | THINK; don't be hasty | N/A: process | THINKING_LOG, Sat afternoon: "cut whole ideas, never squeeze" | - |
| 3 | CN | Creative, original, knowledgeable, evidently widely read | PARTLY | Original: "A high degree of certainty is a list, not an adjective."; "Laura doesn't owe one ten-year bill. She owes ten one-year bills". Only one concept is named and borrowed: "a capital-protected note" | E, misses 9-10 |
| 4 | CN | All Bibles equal; grasp the intent | N/A: process | - | - |
| 5 | CN | Autonomy; may question Caplet | N/A: process | - | - |
| 6 | CN | Expectations met, however disseminated | N/A: process | This file is the item-by-item check for V43 | - |
| 7 | B1 | Distinctive team voice | PARTLY | Present: both pun headings, "But "usually" is the whole trick", "– or nearly –", "Do not crush." Against it: the opener is the field's default shape (row 9), and there are six quotable endings (row 35) | E (C2, C3 cut two kickers) |
| 8 | B1 | Voice carries throughout, pitch included | PARTLY | Better than V42's code. "Laura promised her residency $50,000 a year for ten years, and hopes to add a gift." is a sentence a person says. The last sentence is still a squeezed semicolon pair: "worth all of it by 2032; only their interest buys world stocks." | E7 (pitch) |
| 9 | B1 | Sound unique, unlike any other team | PARTLY | It still opens on "Laura Gao has one promise and one hope.", the default rival's shape (ledger A1). The pitch now echoes P2 ("doesn't invest the promise: her first $300,000 buys it") | Writer's call, 0 words |
| 10 | B1 | Cerebral yet witty | MET | "Have your cake and invest the icing"; "Sell low, by appointment"; "minus the bank (and its fee)" | - |
| 11 | B1 | Passionate yet thoughtful | PARTLY | The only concrete stake is "a building priced in Taiwan dollars". Who the residency is for (artists, writers, educators) never appears | FR (voice guide s7) |
| 12 | B1 | Insightful yet confident | MET | "The US government defaults." said flat; no hedges anywhere | - |
| 13 | B1 | Judges enjoy reading it | PARTLY | Enjoyable: the "But" turn, the headings, the close. Three places a reader stops: "is a list, not an adjective" (a list of what?); "The ladder's one leak – ... – we price and set aside in 2031"; "the range it named" used two paragraphs before any range | E2, E5 |
| 14 | B1 | One unifying motif across the IPS | PARTLY | XR appears only in P10-P11. Cake/icing (H2, P7) and the appointment (H1, P6) compete with it | Miss 8 |
| 15 | B1 | Elaborate, vast motif | N/A: Final Report | - | - |
| 16 | B1 | Intellect and investing knowledge before language | PARTLY | Sound ideas, but mostly unnamed: sequence risk ("a crash in the wrong year forces a sale at the bottom"), human capital (P4), reinvestment risk ("reinvested at lower rates"), pull-to-par ("funds that mature like bonds") | Miss 10 |
| 17 | B1 | Intellect and language together | PARTLY | Language strong; knowledge thin on the page | Miss 10 |
| 18 | B1 | Truly extraordinary, not just competent | PARTLY | Underneath it's the field's skeleton (ladder + stocks + lock: Commandment I). Absent: one borrower on purpose; M1's history of when $300k buys all ten | Miss 11 |
| 19 | B1 | Something no one else would think of | PARTLY | Rare and present: the recession that "pushes yields down, so the ladder costs more, and it shrinks the advances, speaking and licensing behind the 2028 deposit" | - |
| 20 | B1 | An "aha" | PARTLY | Close to one: "Laura doesn't owe one ten-year bill. She owes ten one-year bills". Nothing a judge hasn't half-met | - |
| 21 | B1 | Keep these in your back pocket | N/A: process | - | - |
| 22 | B2 | Name unique | MET | Caplet XR | - |
| 23 | B2 | Nothing roots-themed | MET | No root, branch or tree words ("grow back" is about bonds) | - |
| 24 | B2 | Name tied to the motif | MET | "We call the plan Caplet XR, after the extended-release capsule" | - |
| 25 | B2 | Name fits the strategy, not a stretch | PARTLY | "ten redemptions, one a year" fits, but neither letter is mapped. A judge has to work out X = ten and R = redemption alone. V42 at least said "with an X for ten" | E3 |
| 26 | B2 | Motif not in every sentence | MET | One paragraph and the close | - |
| 27 | B2 | Subtle, not decorative or layered on | PARTLY | It argues now: "it only works whole" / "Do not crush." carry the no-sale rule. But that rule is stated nowhere else, so the argument is in code | E4 |
| 28 | B2 | Motif builds the narrative arc | PARTLY | Better than V42 (MISSED): there's a set-up ("it only works whole") and a payoff ("Do not crush."). But both sit in the last 20 words, so it's an ending, not an arc | Miss 8 |
| 29 | B2 | One image; write like we write | PARTLY | Three frames: the capsule, cake/icing, "by appointment" | Miss 8 |
| 30 | B2 | Only our team could have the name | MET | - | - |
| 31 | B2 | Optimise for ourselves first | MET | - | - |
| 32 | B2 | Motif creative and unexpected ("huh") | PARTLY | "the extended-release capsule" now names the pill (an improvement on V42), but the "huh" depends on decoding X and R | E3 |
| 33 | B2 | Unexpected connections, syntheses | PARTLY | On the page: the bank's note rebuilt from Treasuries plus an index fund; rates × human capital (P4); the capped range treated as an asymmetric payoff (P9) | FR |
| 34 | B2 | Sound deeply human | N/A: needs GPTZero | README: "GPTZero: not yet checked". Not judged here | - |
| 35 | B2 | Lean but messy, human | PARTLY | Lengths vary well, but six kickers: "We buy it.", "never the cake.", "(and its fee).", "printed years in advance.", "it only works whole.", "Do not crush." | C2, C3 |
| 36 | B2 | Cut the human way, not by rearranging | PARTLY | Mostly met: the README lists seven whole ideas cut, and V42's squeezed catch is back at full size. One squeeze remains: V42's "should be a short list of the ways it fails, not a soothing adjective" became "is a list, not an adjective" | E5 |
| 37 | B2 | Parsimonious and lucid | PARTLY | Lucidity fails at "ladder" (never introduced), "the range it named" (before P8), "is a list, not an adjective", "we price and set aside in 2031" (set aside from what, and before what?), and "we made it first" (made what?) | E2, E5, C1 |
| 38 | B2 | Light study of the essays | N/A: process | - | - |
| 39 | B2 | Humanising lists don't work | N/A: process | - | - |
| 40 | B2 | Write more like Ahaan (tone) | MET | Pun headings, en-dash asides, a real concession then "But", long build then short landing (P6: "She owes ten one-year bills"), contractions, "cheque"/"towards" | - |
| 41 | B2 | Essays are tone, not everything | N/A: process | - | - |
| 42 | B3 | Caplet XR clever; justifies the team name | MET | "We call the plan Caplet XR, after the extended-release capsule" | - |
| 43 | B3 | Extend it (timed release, do not crush, more) | MET | Timed: "ten redemptions, one a year". Do not crush: "Do not crush." (restored; V42 had dropped it) | - |
| 44 | B3 | A second meaning of XR | PARTLY | Implied only, by "ten redemptions" | E3 |
| 45 | B3 | "Extended response" | N/A: superseded by Book 5 | - | - |
| 46 | B3 | Product-tier label in intro or close | N/A: Final Report | Ledger A6 | - |
| 47 | B3 | Free to change name or motif | N/A: locked by Book 5 | - | - |
| 48 | B3 | Flair, voice, no over-claim obsession | MET | "Sell low, by appointment"; "Do not crush." | - |
| 49 | B3 | Don't actively over-claim | PARTLY | V42's one-in-three line is gone (fixed). New: "Ours is the same note, minus the bank". It isn't the same note: a capital-protected note buys an option, and we buy shares, which pay off differently. Also, "97 times in 100" holds only if the set-aside comes off before the range is named (L-13), and V43 doesn't say that | E6; optional X1 |
| 50 | B3 | Judges aren't mini-Lauras | MET | It argues investing to a judge | - |
| 51 | B3 | No time on grammar | N/A: process | - | - |
| 52 | B3 | En dashes | MET | Seven en dashes | - |
| 53 | B3 | Marinate | N/A: process | - | - |
| 54 | B4 | Rewrite from scratch; all expectations implemented | PARTLY | Rebuilt from draft A (met). "All implemented": see this table | Section E |
| 55 | B4 | Stop tinkering on the old version | N/A: process | - | - |
| 56 | B4 | Extraordinary knowledge of concepts | PARTLY | Named: "capital-protected note", "60/40", "operating reserve", "rebalance", "index fund". Described but unnamed: sequence risk, human capital, reinvestment risk, pull-to-par. "Ladder" is used and never explained | E2a; miss 10 |
| 57 | B4 | No name-dropping | MET | - | - |
| 58 | B4 | Niche concepts applied and explained | PARTLY | The protected note (explained only as "this"); the capped-range catch (well explained, unnamed) | E6 |
| 59 | B4 | Research uncited in IPS, cited in FR | MET | No citations | - |
| 60 | B4 | FR shows wide reading | N/A: Final Report | - | - |
| 61 | B4 | Knowledge supports the narrative | MET | - | - |
| 62 | B4 | North star 4 equal | N/A: process | - | - |
| 63 | B4 | Long research process | N/A: process | - | - |
| 64 | B4 | Dazzling by 6 Nov | N/A: due later | Final for review end of Wed 4 Nov | - |
| 65 | B5 | Keep Caplet XR | MET | - | - |
| 66 | B5 | State the literal "extended release" | MET | "the extended-release capsule" | - |
| 67 | B5 | Both meanings of XR in the IPS | PARTLY | Literal: yes. Ours: only implied | E3 |
| 68 | B5 | Bare bones of the motif | MET | - | - |
| 69 | B5 | Everything out by the FR | N/A: Final Report | - | - |
| 70 | B5 | Make it clear the name is clever and thought out | PARTLY | A judge has to connect "XR" to "ten redemptions" alone | E3 |
| 71 | B5 | X = 10 | PARTLY | V42 had "with an X for ten". V43 only implies it ("ten redemptions"): a regression | E3 |
| 72 | B5 | R not "release" | MET | "release" appears only in the literal "extended-release capsule"; R is implied as "redemptions" | - |
| 73 | B5 | No fretting over sure-sounding words | MET | "The US government defaults."; "Do not crush." | - |
| 74 | B5 | iBonds: exact sums on exact dates | MET | "Treasury funds that mature like bonds, one falling due before each January" | - |
| 75 | B5 | May say near-ironclad; distinction concise | MET | Not used; no hedging (optional) | - |
| 76 | B5 | Accuracy matters | PARTLY | Fixed: "should earn" for the floor's interest; the $125k misreading went with the cut. New: "the same note" (row 49); pitch "only their interest buys world stocks" (the shares are bought in 2028 with the floor's discount, not with interest paid later); the 97 needs the set-aside's timing (row 49) | E6, E7 |
| 77 | B5 | Human flair | MET | Headings; "Do not crush." | - |
| 78 | B5 | No hedging | MET | - | - |
| 79 | B5 | Test on essays + TNA, not only Orwell | N/A: process | Voice readers 6-7 named in the README | - |
| 80 | B5 | Use Ahaan's voice, not a robotic one | PARTLY | See rows 35, 119 | C2, C3 |
| 81 | B5 | Extraordinary | PARTLY | Row 18 | - |
| 82 | B5 | Distinctive, erudite, clever | PARTLY | Clever yes; erudite thin | Miss 10 |
| 83 | B5 | Final by Sat 31 Oct | N/A: superseded (Wed 4 Nov) | - | - |
| 84 | B5 | Meet every expectation | PARTLY | This table | - |
| 85 | B9 | Meets all Wharton requirements | PARTLY | Certainty is defined but not evaluated (case p.3 "explain how they evaluated"); principles only implicit; diversification thin | E1 |
| 86 | B9 | Don't focus on formatting | N/A: process | - | - |
| 87 | B9 | Seen as intelligent and knowledgeable | PARTLY | The logic is strong; most concepts go unnamed | Miss 10 |
| 88 | B9 | Search for niche concepts | N/A: process | - | - |
| 89 | B9 | Fuse strategies; synergies | PARTLY | The note rebuilt from Treasuries plus an index fund; rates × income. Neither is critiqued for what it costs us | E6 |
| 90 | B9 | Dig in unexpected places | N/A: process | - | - |
| 91 | B9 | Analyse and critique borrowed ideas | PARTLY | The 60/40 is critiqued with numbers (good). The note gets only "minus the bank (and its fee)": a dig at banks, not a note on what ours gives up | E6 |
| 92 | B9 | Show an idea that seems right but isn't | MET | "a 60/40 portfolio usually ends 2042 almost $200,000 ahead of ours. But "usually" is the whole trick" | - |
| 93 | B9 | Show knowledge of strategies few know | PARTLY | Only the protected note | Miss 10 |
| 94 | B9 | Our own strategy for our client | MET | P4: "it shrinks the advances, speaking and licensing behind the 2028 deposit" | - |
| 95 | B9 | Logic: chains to their conclusion | MET | The recession chain (P4); the cap → "every fall ... comes off the gift while every rise past the top goes to Laura" → the lock (P9) | - |
| 96 | B9 | Case studies, evidence | PARTLY | Model figures only (M7, L-13); M8 (1923) and M1 unused | FR |
| 97 | B9 | Voice is qualitative | N/A: process | - | - |
| 98 | B9 | Use Wall Street writers too | N/A: process | - | - |
| 99 | B9 | Don't use own agents as detectors | N/A: process | - | - |
| 100 | B9 | Use real web detectors | N/A: process | Not run (DETECTOR_LOG) | - |
| 101 | B9 | Detection is low priority | N/A: process | - | - |
| 102 | B9 | Don't obsess over 7.5% for VT | MET | "with world stocks at 7.5% a year": world stocks, not VT, said once | - |
| 103 | B9 | Not hamstrung by the TNA | MET | - | - |
| 104 | B9 | Use studies like the donor study | PARTLY | Not in the IPS ("high enough that her lead gift draws bigger ones" is cut), but the ledger now sends it to the FR, so it lands somewhere | Miss 12 (not bought) |
| 105 | B9 | Turn model findings into arguments | MET | M7's price of safety; L-13's 97 after the catch | - |
| 106 | B9 | Every good idea lands somewhere | MET | IDEA_LEDGER "V42 and V43" gives every cut idea IN / FR / OUT with a reason | - |
| 107 | B9 | Research is for the deliverables | N/A: Final Report | - | - |
| 108 | B9 | Don't discard ideas wantonly | N/A: process | Ledger as row 106 | - |
| 109 | B9 | Pitch not AI-squeezed; cut the human way | PARTLY | Sentences 1-2 have verbs and people. Sentence 3 is a squeezed pair: "Her 2028 deposit buys Treasuries worth all of it by 2032; only their interest buys world stocks." The colon-mirror "doesn't invest the promise: her first $300,000 buys it" stays | E7 |
| 110 | B9 | No artificial timeline | N/A: process | - | - |
| 111 | B9 | Work more densely | N/A: process | - | - |
| 112 | B9 | No AI-use logging | N/A: process | - | - |
| 113 | B9 | No minute changes; big picture | N/A: process | - | - |
| 114 | B9 | Judges don't read for precision | N/A: process | - | - |
| 115 | B9 | Put message in the Bible | N/A: process | - | - |
| 116 | B10 | Diverse mock judges | N/A: process | `judges/panel_V43/` has judges' scores; no SUMMARY yet | - |
| 117 | B10 | Judges don't approve every change | N/A: process | - | - |
| 118 | B10 | Judges don't think like Keel | N/A: process | - | - |
| 119 | B10 | Apply the voice studies | PARTLY | Applied: concession then "But" (P5-P6), pun headings, en dashes, contractions, a close that's an act ("Do not crush."). Not applied: law 9 (six kickers, not three), law 6 (three images, not one), law 7 (V42's real confession replaced by "we made it first"), law 10 symmetry ("So we don't invest the promise. We buy it."; "a list, not an adjective"; "the icing, never the cake") | C1-C3 |
| 120 | B10 | Pitch reads as obvious AI | PARTLY | Row 109 (improved from MISSED) | E7 |
| 121 | B10 | GPTZero before Caplet | N/A: process | README: "GPTZero: not yet checked" (the label is present) | - |
| 122 | B10 | "Human-written only" above 50% | MISSED | No score for the pitch or the IPS; GPTZero can't be reached from these sessions | A student pastes both into gptzero.me (DETECTOR_LOG) |
| 123 | B10 | Own voice matters more than the score | PARTLY | Row 119 | - |
| 124 | B10 | Use the human-vs-AI notes | PARTLY | Colons rose from 2 in V42 to 6 ("before we buy: it", "all of it: her floor", "the whole trick: about", "has a catch: once", "runs itself down: each", "capsule: ten"). The triad "the cheques come first, then the floor, then the hope" stays | E3 rewrites one colon line; rest writer's call |
| 125 | B10 | No sentences so compressed they barely make sense | PARTLY | "is a list, not an adjective"; "The ladder's one leak – coupons that arrive early, reinvested at lower rates if yields fall – we price and set aside in 2031."; pitch "worth all of it by 2032; only their interest" | E5, E7; optional X1 |
| 126 | B10 | Natural variation and flair | MET | From "Do not crush." (3 words) to P4's 37-word recession sentence | - |
| 127 | B10 | Judges don't fixate on single lines | N/A: process | - | - |
| 128 | B10 | Mark only to Wharton's guide | N/A: process | This check argues from section B | - |
| 129 | B10 | No "every team will" | MET | No comparison with other teams | - |
| 130 | B10 | No numbers plucked from thin air | PARTLY | Every figure has a source in the README. But "about a fifteenth" still has no run file (README: "no single run file yet"), and the 97 rests on L-13's slide, which the text doesn't describe | Add run file; X1 |
| 131 | B10 | "We model", never "we judge" | MET | "in our model" ×2, "by our sums"; no "we judge" | - |
| 132 | B10 | Stop obsessing over AI use | N/A: process | - | - |
| 133 | B10 | Drop "required trading activity" | MET | Not raised | - |
| 134 | B10 | Final by end of Wed 4 Nov | N/A: deadline | - | - |
| 135 | B10 | Overdrive | N/A: process | - | - |
| 136 | B10 | Demonstrate more work per day | N/A: process | - | - |
| 137 | B10 | Top 50 of 2,300; whatever it takes | N/A: process | - | - |
| 138 | B10 | Number one: extraordinary, not ordinary | PARTLY | Row 18 | - |
| 139 | B10 | Fresh commandments | N/A: process | - | - |
| 140 | B10 | Commandments must be followed | N/A: process | The README has no filled ten-line check. Section C below is that check, and it fails six lines | - |
| 141 | B10 | Final IPS satisfies all expectations | PARTLY | This table | Section E |
| 142 | B10 | Recursive self-improvement | N/A: process | V43 applies most of V42's check (README "Fixed from V42's Bible check") | - |
| 143 | B10 | Initiative, intellectual risks | PARTLY | Risks in voice ("Do not crush." as the last line); none in strategy (one borrower still out) | Miss 11 |
| 144 | B10 | Guess what Caplet will say | N/A: process | THINKING_LOG has a V43-round "What Caplet would say" entry | - |
| 145 | B10 | Rewrite from scratch again | MET | Rebuilt from voice-first draft A | - |
| 146 | B10 | List every idea of every version | N/A: process | IDEA_LEDGER "V42 and V43" | - |
| 147 | B10 | Best ideas end up in the new IPS | PARTLY | In: the leak + set-aside, the catch + lock, 97, 7.5%, the 60/40 price, thoughtful risks, the note, human capital. Out: the $125,000 break point (so certainty has no measure), one borrower, the lead-gift line, the first-plan confession, "Any rung can be sold any day" | E1; misses 11-12 |
| 148 | B10 | Add the message to the Bible | N/A: process | - | - |
| 149 | B10b | Wharton's word with the utmost importance | PARTLY | Section B: certainty isn't evaluated, principles are implicit, diversification is thin | E1 |
| W1 | W1 | Clear and creative thesis | PARTLY | Clear: "So we don't invest the promise. We buy it." Creative in framing more than structure (row 18) | - |
| W2 | W1 | Disciplined planning across horizons and cash flows | MET | 2027 ladder; 2028 floor + fund; 2031 set-aside, range, lock; 2033 reserve | - |
| W3 | W1 | Appropriate diversification | PARTLY | Stocks: only "one world index fund" ("of thousands of companies" was cut). Cheques: "The US government defaults" names the concentration but never argues for it | Miss 11 |
| W4 | W1 | Consistent with IPS/TNA/WInS | MET | Treasury bonds + iBond funds one per January, IBTM-like "Treasuries maturing late in 2032" as floor, one world fund (VT), the 2028 deposit covering the gap first: matches `00_GROUND_TRUTH` s3 | - |
| W5 | W1 | Tailored to circumstances, priorities, risk considerations | MET | "Laura is willing to take thoughtful risks, and in our model ..." answered by "But "usually" is the whole trick"; her income in P4 | - |
| W6 | W1 | ... and residency goals | MET | "a gift towards the residency's building in Taiwan"; "a building priced in Taiwan dollars comes in dearer" | - |
| W7 | W1 | Thoughtful understanding of the client | MET | P4 | - |
| W8 | W1 | Recommendations that can earn her confidence | MET | "The bottom is the floor she has owned since 2028." | - |
| W9 | W1 | Understanding and use of concepts and tools | PARTLY | Row 56 | E2a; miss 10 |
| W10 | W1 | Quantitative + qualitative | MET | M7 and L-13 figures alongside the calendar argument | - |
| W11 | W1 | Reasonable assumptions and projections | PARTLY | Fixed from MISSED: "with world stocks at 7.5% a year". No rate or inflation assumption, and the model is never described | FR (inflation) |
| W12 | W1 | Evaluate reliability, facility, flexibility under varying outcomes | PARTLY | Facility: "about 97 times in 100". Flexibility: "The other half stays hers". **Reliability: not evaluated.** The failure list gives no size and no miss rate for our plan, while the 60/40's ("one time in three") is given | E1 |
| W13 | W1 | Articulation: teamwork, process, learning | PARTLY | Only "There is a serious case against all this, and we made it first." (vaguer than V42's "Our first plan was three-quarters stocks") | FR; X4 |
| W14 | W1 | Compelling, organised narrative | MET | The order is promise → ladder → certainty → opponent → floor → range → catch → reserve → name (V42's order problem is fixed). Clarity slips are counted under row 37 | - |
| W15 | W1 | Authentic team voice | PARTLY | "we" ×6; not detector-checked | - |
| W16 | W1 | Data used effectively | MET | "almost $200,000 ahead", "one time in three", "97 times in 100": each lands a point | - |
| W17 | W1 | Original thinking, meaningful reflection | PARTLY | Original thinking yes; reflection one vague clause | - |
| W18 | W1 | Contribution and uncertainty clear and credible to co-sponsors | MET | The bottom is owned; the catch is explained and the lock shuts it; 97 in 100. (The lead-gift reason for a range is absent: miss 12) | - |
| W19 | W2 | Invest to support goals and cash flows while managing risk | MET | - | - |
| W20 | W2 | Reflect goals, horizons, liquidity, certainty, flexibility | MET | Liquidity: "each turns to cash before its cheque", "to sell any day"; certainty: P4; flexibility: "The other half stays hers" | - |
| W21 | W2 | Q: central idea | MET | "So we don't invest the promise. We buy it." | - |
| W22 | W2 | Q: principles | PARTLY | Implicit: "the cheques come first, then the floor, then the hope"; certainty as a list. The no-sale rule is only in code | E4 |
| W23 | W2 | Q: balance growth, risk, liquidity, reliability, flexibility | MET | Growth's share ("about a fifteenth") is argued by the concession and "But"; the other four are as in W20 | - |
| W24 | W2 | Q: allocation changes as needs approach and payments are made | MET | 2028 floor; 2031 "the half she promised moves into Treasuries"; 2033 "it runs itself down" | - |
| W25 | W2 | Q: protect the commitment, keep flexibility for the contribution | MET | P8-P10 | - |
| W26 | W2 | Remember whom it serves | MET | - | - |
| W27 | W2 | Pitch: strategy, central idea, how it supports her goals | PARTLY | It names the cheques, the residency, the gift and world stocks (fixed). It never links the floor and stocks to the gift, and "only their interest buys world stocks" is inaccurate | E7 |
| W28 | W2 | IPS: risk and return | MET | The return assumption plus the 60/40 trade-off; the risk list | - |
| W29 | W2 | IPS: construction and diversification | PARTLY | W3 | - |
| W30 | W2 | IPS: reserve composition over time | MET | "each turns to cash before its cheque, with nothing to rebalance" | - |
| W31 | W2 | IPS: responsible facility contribution | MET | Bottom = floor, top = floor + half the stocks, other half kept | - |
| W32 | W2 | IPS: appropriate flexibility | MET | "to sell any day if a building priced in Taiwan dollars comes in dearer" | - |
| W33 | W2 | Framework, not individual investments | MET | - | - |
| W34 | W2 | No final reserve sums, projections, final range | MET | No sums and no range. "97 times in 100" is the rule's confidence, not a final range (keep it to one figure) | - |
| W35 | W2 | No citations, charts, links | MET | - | - |
| W36 | W2 | Strategy can't be revised | MET | Dated rules | - |
| W37 | W3 | Reasoning, assumptions, trade-offs | MET | Reasoning; the 7.5% assumption; the trade-off "almost $200,000 ahead" | - |
| W38 | W3 | Cohesive across market outcomes | MET | - | - |
| W39 | W3 | Planned adjustments, not rewritten when markets move | PARTLY | Dated rules and "nothing to rebalance". "No rung sold early" is only in the capsule code | E4 |
| W40 | W4 | Strategy leads across deliverables | MET | - | - |
| W41 | W4 | Know your client | MET | - | - |
| W42 | W4 | Use WInS to demonstrate | N/A: WInS/FR | - | - |
| W43 | W4 | Don't focus on performance | MET | - | - |
| W44 | W4 | Explain why each investment belongs | PARTLY | Treasuries (the calendar) and the world fund (only the interest) are explained. Why Treasury funds as well as bonds isn't: V42's "Any rung can be sold any day" was cut | FR |
| W45 | W4 | Follow the instructions | PARTLY | W12 (reliability not evaluated), W3 | E1 |
| W46 | W5 | Only WInS stocks, ETFs, Treasuries | MET | The note is a foil only ("Banks sell this") | - |
| W47 | W6 | "Responsibly contribute"; keep flexibility | MET | "The other half stays hers" | - |
| W48 | W6 | "Willing to take thoughtful risks" | MET | Conceded in the case's words (no quote marks), then answered | - |
| W49 | W6 | 2028 deposit from advances, speaking, licensing | MET | "shrinks the advances, speaking and licensing behind the 2028 deposit" | - |

## B. Wharton's word, item by item

| # | Source | Item | V43 status | Evidence | Fix |
|---|---|---|---|---|---|
| Q1 | IPS question | Central idea | MET | "So we don't invest the promise. We buy it." | - |
| Q2 | IPS question | Guiding principles | PARTLY | Implicit (the priority order; certainty as a list); the no-sale rule only in code | E4 |
| Q3 | IPS question | Balance growth, risk, liquidity, reliability, flexibility | MET | W20, W23 | - |
| Q4 | IPS question | Allocation change as needs approach and payments are made | MET | 2027 → 2028 → 2031 → 2033 | - |
| Q5 | IPS question | Protect the commitment while keeping flexibility for the contribution | MET | P8-P10 | - |
| Q6 | IPS instruction | Remember whom it serves | MET | - | - |
| M1 | Make it clear | What we're trying to accomplish | MET | P1 | - |
| M2 | Make it clear | Why it's appropriate for the client | MET | Thoughtful risks answered; her income (P4); the stated assumption | - |
| M3 | Make it clear | How it balances the five | MET | As Q3 | - |
| M4 | Make it clear | How it guides construction and decisions as needs change | MET | Dated rules | - |
| M5 | Make it clear | Protect payments while supporting a responsible contribution | MET | "the cheques come first"; the floor owned since 2028 | - |
| P | Pitch | Summarise; central idea; how it supports goals and funding needs | PARTLY | Central idea and goals yes; the gift link is missing; "only their interest" | E7 |
| I1 | IPS para | Tailored to goals, horizons, needs | MET | - | - |
| I2 | IPS para | Risk and return | MET | W28 | - |
| I3 | IPS para | Liquidity | MET | "each turns to cash before its cheque"; "to sell any day" | - |
| I4 | IPS para | Construction and diversification | PARTLY | W3 | Miss 11 |
| I5 | IPS para | Planned changes as needs approach | MET | - | - |
| I6 | IPS para | Prepare for the operating commitment; reserve composition | MET | P3, P10 | - |
| I7 | IPS para | Responsible facility contribution; flexibility | MET | P8 | - |
| J1 | Guide | Reasoning, assumptions, trade-offs | MET | W37 | - |
| J2 | Guide | Cohesive across outcomes | MET | - | - |
| J3 | Guide | Not rewritten because markets move | PARTLY | Implied ("nothing to rebalance"; "Do not crush.") | E4 |
| C1 | Criterion | Investment Strategy | PARTLY | Clear thesis, disciplined dates, consistent. Diversification only implied | Miss 11 |
| C2 | Criterion | Client Knowledge and Objectives | MET | Thoughtful risks, her income, Taiwan dollars, the kept half | - |
| C3 | Criterion | Portfolio Analysis | PARTLY | One assumption now stated, but funding reliability isn't evaluated (W12) and concepts are unnamed | E1; miss 10 |
| C4 | Criterion | Articulation of Competition Experience | PARTLY | One vague clause (mostly the FR's job) | FR |
| C5 | Criterion | Creativity and Presentation | PARTLY | Strong voice and organisation. Terms used before they're introduced; three competing images; co-sponsor communication clear | E2; miss 8 |
| A1 | Advice | Let strategy lead | MET | - | - |
| A2 | Advice | Know your client | MET | - | - |
| A3 | Advice | Use WInS to demonstrate | N/A: WInS/FR | Consistent with the WInS book | - |
| A4 | Advice | Not about performance | MET | - | - |
| A5 | Advice | Explain why each investment belongs | PARTLY | W44 | - |
| A6 | Advice | Follow the instructions | PARTLY | W12 | E1 |
| H | Hard limit | Permitted instruments only | MET | Treasury bonds, Treasury funds, one world index fund; no TIPS/STRIPS | - |

## C. The Ten Commandments

- **I. Extraordinary: FAIL.** The three ideas a judge would retell: certainty "is a list, not an adjective"; "ten
  one-year bills"; the capped range's catch and the lock. The third rests on the lock, which is the field's default
  (BIBLE_AUDIT row 19: 9 of 12 rivals lock), and under all three sits the default skeleton of ladder + stocks + lock.
  The rare ideas (one borrower on purpose, M1's history) aren't on the page.
- **II. Wharton only: PASS.** The text answers all five IPS questions as a whole, and this check argues from section
  B. The gap that matters is W12 (reliability not evaluated).
- **III. Write like us: FAIL.** The README doesn't quote where each move happens. The concession and "But" is there
  (P5-P6), but the triad stays ("the cheques come first, then the floor, then the hope"). There are six kickers
  against a ration of three, three images against one, and six colons. And the one real confession was swapped for
  "we made it first".
- **IV. Clear on one reading: FAIL.** "ladder" is never introduced ("so the ladder costs more" is its first use);
  "range" appears in P6 ("the range it named") before P8 introduces it; "is a list, not an adjective" (a list of
  what?); "we price and set aside in 2031" (what, from where, before what?); "we made it first"; and in the pitch,
  "only their interest buys world stocks".
- **V. Every number explains itself: PASS, with a caveat.** "in our model" covers the $200,000, the one in three and
  the 97; "by our sums" covers the fifteenth; the 7.5% is said to be the model's. The caveats: the fifteenth still
  has no run file, and the 97 is right only if the set-aside comes off before the range is named, which the text
  doesn't say.
- **VI. GPTZero before Caplet: FAIL, and it can't be met here.** (The brief calls this "VIII"; it is VI in
  `BIBLE.md`.) GPTZero can't be reached from Keel's sessions, so there's no "human-written only" score for the pitch
  or the IPS. The README carries the label the commandment requires in that case ("GPTZero: not yet checked"). No
  agent stood in for a detector. A student has to paste both texts into gptzero.me before Caplet's read; until then
  this line stays failed.
- **VII. Few ideas at full size: PASS.** A judge could restate it in three sentences: her 2027 money buys the ten
  cheques as Treasuries, one maturing before each January; her 2028 money buys a floor of Treasuries that grows back
  into itself, and the difference goes into a world index fund; in 2031 she names a range from the floor to the floor
  plus half the stocks, and locks the promised half in Treasuries that day.
- **VIII. Lose no idea; critique every borrowed one: FAIL (half met).** The ledger half passes: every idea V42
  dropped and V43 cut is recorded with where it lands. The critique half fails: the capital-protected note is called
  "the same note" and never critiqued for what ours gives up.
- **IX. Judges who disagree: FAIL (not yet).** `judges/panel_V43/` holds judges' scores but no SUMMARY and no rank
  correlations.
- **X. Improve without being asked: PASS.** THINKING_LOG has a "What Caplet would say" entry for this round, and V43
  visibly carries most of V42's check (README, "Fixed from V42's Bible check").

## D. Numbers

| Figure (where) | Source file and value | Wording matches? | Attribution |
|---|---|---|---|
| $50,000 every January 2033-2042; "ten cheques" (pitch, P1, P3) | Case p.3 | Yes | Case; none needed |
| $300,000 (2027); the 2028 deposit (pitch, P3, P4, P7) | Case p.2 | Yes | Case |
| "buys all ten cheques – or nearly" (P3); pitch "her first $300,000 buys it" | `suite_results.json` M1 `today_cost_bootstrap_22oct` $298,861 (under $300k by $1,139); M1: $300k bought all ten in only 25% of months since 1871 | Yes in the IPS ("or nearly"). The pitch drops "nearly", which is true today but can move | A market fact; acceptable |
| "with world stocks at 7.5% a year" (P5) | `models/ASSUMPTIONS.md` A06: J.P. Morgan 2027 LTCMA global equities 7.5%; ASK_HUMANS 31 Oct | Yes: world stocks, not VT (Book 9) | "in our model, with" |
| 60/40 "usually ends 2042 almost $200,000 ahead of ours" (P5) | M7, 7.5% worlds: `balanced` `laura_2042_p50` $226,292 / $228,752 / $231,463 vs `xr_lock` $30,374 / $30,660 / $31,060 → $196k-$200k ("usually" = the median). Raw history gives $285k vs $34k, so "almost $200,000" is the cautious reading | Yes | "in our model" |
| 60/40 "about one time in three ... misses a cheque or falls short of the range it named" (P6) | M7 `balanced` `p_any_promise_broken` 36.3% / 32.3% / 34.6% (lognormal / regime / bootstrap); history 29.6%. Its own range per A23 (its projection ± 20%). Cheques alone: 6.1% / 7.7% / 6.0% | Yes (it says "or", so no longer pinned on the cheques) | "in our model" carries from P5; the sentence itself has none (acceptable: same paragraph pair) |
| "about a fifteenth of the portfolio by our sums" (P7) | D19 README: about $31k of $450k (≈ 1/14.5); "no single run file yet"; ledger C6 6.5-7.1% | Yes | "by our sums"; **no run file** |
| "Treasuries maturing late in 2032" (P7) | Plan: IBTM (`00_GROUND_TRUTH` s3) | Yes | Plan fact |
| "just enough to grow back into all of it" (P7) | Plan design (the floor sized to repay about the deposit; the range bottom $145k is "rounded down", CLAUDE.md range note) | Roughly. The TNA's IBTM note says "final payout is not fixed"; "just enough" is the design's aim | Plan |
| 2031; "half her stocks"; "since 2028" (P8) | Case p.3; plan rule (ledger D1) | Yes | Case/plan |
| "the gift reaches its top about 97 times in 100" (P9) | `rooms/lab/L-13_slide_the_range.md`: with the slide, 97.9 / 97.6 / 96.0 / 96.7% (four worlds, V29 design + lock). Without the slide, M7 `xr_lock` `p_top_reached` is only 84.1 / 84.5 / 93.2% | **Only if** the 2031 set-aside comes off before the range is named (the slide). V43 says "we price and set aside in 2031" without that order | "in our model". Optional X1 makes the order explicit |
| 2033; "the ten holdings" (P10) | Case p.3; plan | Yes | Case/plan |
| **Proposed E1:** "after a two-point fall in yields, a deposit of about $125,000 is enough" | `A25_results.json`: dy_build −2pt, $125k → 0.19% of paths short by >$1k; $100k → 5.04%; $150k → 0. Stamp: V29/V33 design (lock included) | Yes ("enough" = 99.8% of paths) | "In our model" |

Every model figure in V43 says where it came from. What's still loose: the fifteenth has no run file, and the 97 depends on an
order the text doesn't state.

## E. The misses, ranked by what a Wharton judge would notice, with exact fixes

V43 is 497 strict, and the cap is 497. The package below (E1-E6 for the IPS, E7 for the pitch, paid for by cutting C1-C3) was assembled
on the full text and measured with `textcheck.py`: **IPS 497 strict (494 by spaces), pitch 50.** The deltas are
textcheck's, each applied alone to V43: E1 +19, E2a +4, E2b −1, E3 +4, E4 +4, E5 +2, E6 0, C1 −13, C2 −9, C3 −10 =
**0**. The assembled text was used only to prove the count. It has had no GPTZero check, cold read or panel.

1. **Funding reliability is defined but never evaluated, and the second failure isn't a failure (W12, W45, C3, case
   p.3 "explain how they evaluated that level of certainty").** The judge is given the 60/40's miss rate and nothing
   for ours. *E1:* "behind the 2028 deposit that must cover the gap." → "behind the 2028 deposit, until it can't cover
   the gap. In our model, even after a two-point fall in yields, a deposit of about $125,000 is enough." (**+19**;
   A25.)
2. **Terms used before they're introduced (Commandment IV; rows 37, 56, C5).** *E2a:* "as Treasury bonds, and
   Treasury funds that mature like bonds, one falling due before each January." → "as a ladder of Treasury bonds, and
   Treasury funds that mature like bonds, one rung falling due before each January." (**+4**). *E2b:* "or falls short of
   the range it named." → "or breaks Laura's word to co-sponsors." (**−1**; true to M7, where the miss is the gift
   below the range she named).
3. **Neither letter of XR is stated (Book 5; rows 25, 44, 67, 70, 71).** *E3:* "after the extended-release capsule:
   ten redemptions, one a year, and it only works whole." → "after the extended-release capsule: X for ten, R for
   redemption, one a year, and it only works whole." (**+4**).
4. **The no-sale rule lives only in code (W22, W39, J3, row 27).** Since "Any rung can be sold any day. None will
   be." was cut, nothing plainly says that no Treasury is sold before its cheque, which is what "Do not crush." means.
   *E4:* "with nothing to rebalance." → "with nothing sold early and nothing to rebalance." (**+4**). It also gives the
   close a set-up a judge can decode.
5. **"The same note" over-claims, and the borrowed idea isn't critiqued (rows 49, 76, 91; Commandment VIII).** *E6:*
   "Ours is the same note, minus the bank (and its fee)." → "Ours swaps the bank's option for shares and skips its
   fee." (**0**). That's true, and it shows we know what's inside a protected note.
6. **The squeezed certainty line (Commandment IV; row 125).** *E5:* "is a list, not an adjective." → "is a list of
   failures, not an adjective." (**+2**).
7. **The pitch's inaccurate last clause (W27, rows 76, 109).** The shares are bought in 2028 with the floor's
   discount, not later with interest. *E7:* "; only their interest buys world stocks." → ", and the change buys world
   stocks." (**0**; pitch stays 50.)

**The cuts that pay (whole ideas, not squeezes):**
- *C1: cut* "There is a serious case against all this, and we made it first." (**−13**). P5 then opens on the
  concession, "Laura is willing to take thoughtful risks". The self-steelman claim was vague, and the real event
  behind it (the 75%-stocks first plan) goes to the FR's Articulation section. If the team wants it on the page, X4
  replaces the sentence with "Our first plan was three-quarters stocks." (−6 instead of −13, so 7 more words must
  come from elsewhere, e.g. dropping E4 and E5 and one more).
- *C2: cut* " – selling low, on a timetable printed years in advance" (**−9**). It's a kicker restating the heading
  "Sell low, by appointment". The sentence now ends "forces a sale at the bottom."
- *C3: cut* "A crash can cost her the icing, never the cake." (**−10**). It's a kicker restating the heading "Have your
  cake and invest the icing", and "her floor" already carries the protection. The kickers drop from six to four.

**Not bought (no words left; each is the first in line if a cut above is rejected):**
8. **Three competing images (rows 14, 29; law 6).** Writer's call: retitle one heading to point at the capsule (0
   words). FR for the full pill structure.
9. **The 97's condition.** *X1:* "we price and set aside in 2031." → "we price and set aside in 2031, before any gift
   is named." (+5). This is the honest fix for D's one partial match. It could replace E4 + E5 (+6).
10. **Concepts unnamed (rows 16, 56, W9).** *X2:* "Planners call this sequence risk." before "Laura doesn't owe one
    ten-year bill." (+5).
11. **The cheques' single borrower is unargued (W3, C1, rows 18, 143).** FR, or about 27 words (BIBLE_AUDIT gap 1).
12. **Why a range at all: the lead-gift effect (row 104).** *X3:* "In 2031 she gives co-sponsors a range, low enough to
    keep her word and high enough that her lead gift draws bigger ones." (+16). It's in the ledger for the FR.
13. **Process (Commandments III, VI, IX).** These cost no words. Add the moves-quoted line and the ten-line check to the
    README (section C here can be pasted); get a GPTZero score from a student; finish the panel_V43 SUMMARY with rank
    correlations; add a run file for "about a fifteenth".
