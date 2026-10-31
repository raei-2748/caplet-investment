# AI-generated check (Claude), 31 Oct 2026, not for submission

**For the team lead, in eight lines.**
1. **Counts:** pitch **50/50**, IPS **496/497** strict (492 by spaces), from `office/tools/textcheck.py`. The D25 README still says 497. Section E's package (paid for by cutting the triad) was measured at **IPS 497 / pitch 50**.
2. **Tally:** A (198 rows) **MET 77 · PARTLY 64 · MISSED 2 · N/A 55** (V44: 82 / 58 / 3 / 55); B (34 rows) **MET 23 · PARTLY 10 · MISSED 0 · N/A 1** (V44: 22 / 11 / 0 / 1).
3. **Commandments: PASS 4 (II, VII, VIII, IX) · FAIL 6 (I, III, IV, V, VI, X).** VIII now passes (it failed for V44), because the note is critiqued. X fails because THINKING_LOG has no entry for V44 or V45. VI can't be met from these sessions; the README says "GPTZero: not yet checked".
4. **Biggest misses:** (a) the reliability figure in P6 ("one time in three ... ours, under one in sixty") still has no "says who" in its own sentence, and it still lumps the cheques together with the co-sponsor promise. The V44 check's E1 wasn't taken. (b) The "97 times in 100" isn't tied to the range: the case asks how confident we are the gift falls *within* the range, and what a bad outcome costs (panel V45's J6). (c) The stock sleeve is still never sized, and its diversification is one sentence (J2 and J6 on panel V45).
5. **What V45 fixed:** a real team event ("our first plan was three-quarters stocks, until our own model sank it"; J4 put V45 first for it); "range" no longer appears before it is introduced; the orphaned cake heading is gone; "Sell low, by appointment" has its payoff back; "a list of ways to fail"; the note is critiqued ("can't expire worthless"); the pitch now says the stocks are for the gift, and "the change" is gone.
6. **What V45 broke:** XR's letters are no longer mapped, so Book 5's "X = 10" goes back to PARTLY (J1 had to decode "redemptions"). With "nothing sold early" cut, "Do not crush." is orphaned again (J2: "a closing flourish I could not tie to anything"). There's a new squeeze ("once named"). Colons are up from 7 to 8 and kickers from 4 to 5. The README is stale: it gives 497, doesn't list the four late fixes, and says "no new figure" even though "three-quarters" is new.
7. **Process:** VERSIONS row 45 says "sent to Caplet 31 Oct", but COMMANDMENTS_CHECK says "One fail = the draft is not sent", and six lines fail here. D25's README has no filled ten-line check (section C can be pasted in).
8. **Panel V45 (finished while this check ran):** mean rank V40 2.17, **V45 2.33**, S01 3.0, V44 3.33; tau 0.32. V45 is first with the actuary and the teacher, and no judge ranks it below third. Voice reader 9 puts V45 second of four, and its top rewrite is E1's fragment.

**What was checked.** `pitch.txt` and `ips_V45.txt` in this folder (including the four fixes made after the README was written), read cold by a reader who didn't write them. I checked them against `WHARTON_WORD.md`, all of `BIBLE.md` (the Ten Commandments included), every row of `BIBLE_AUDIT.md` s1 (each judged fresh for V45, using the V44 check's rows), the case, `voice/06_voice_guide.md` and `IDEA_LEDGER.md` (V45 line). For the numbers I used `models/results/suite_results.json` (M7, values re-read for this check), `models/ASSUMPTIONS.md` (A06, A13-A15, A19, A23) and `rooms/lab/L-13_slide_the_range.md`. As corroboration only, never as the marking scheme, I used `judges/panel_V44/SUMMARY.md`, panel V45 (`judges/panel_V45/`: the score files of J1, J2, J4 and J6, decoded with KEY.json, and its SUMMARY, which was finished while this check ran) and voice reader 9 (`voice_first/readers/reader9_verdict.md`, where V45 is Entry 3). I'm not an AI detector and don't judge AI-ness here. I didn't edit the draft.

V45's paragraphs, for reference: P1 opener · P2 "So we don't invest the promise. We buy it." · P3 the 2027 ladder · P4 certainty + the leak · H1 "Sell low, by appointment" · P5 "we made it first: our first plan" + the 60/40 · P6 "But 'usually'" + one in three / one in sixty + the bills + "selling low, on a timetable" · P7 floor + fund + the note · P8 the 2031 range · P9 the catch + lock + 97 · P10 reserve + priority + XR · P11 "Do not crush."

## A. Every expectation in BIBLE_AUDIT s1, judged for V45

| # | Book | Expectation | V45 status | Evidence (V45's exact words, or what is absent) | Fix |
|---|---|---|---|---|---|
| 1 | CN | Rewrite slowly: long thinking, research, analysis | N/A: process | V45 is a same-day patch of V44 (Sat 31 Oct), the 15th version since Fri 30 Oct. No THINKING_LOG entry | - |
| 2 | CN | THINK; don't be hasty | N/A: process | Cuts were whole ideas (ledger V45 line); one squeeze crept in (row 36) | - |
| 3 | CN | Creative, original, knowledgeable, evidently widely read | PARTLY | Original: "A high degree of certainty is a list of ways to fail, not an adjective."; "Laura doesn't owe one ten-year bill. She owes ten one-year bills". Knowledge: "Ours swaps the bank's option for shares, which can't expire worthless." Still only one borrowed concept is named ("a capital-protected note") | E3; X5 |
| 4 | CN | All Bibles equal; grasp the intent | N/A: process | - | - |
| 5 | CN | Autonomy; may question Caplet | N/A: process | - | - |
| 6 | CN | Expectations met, however disseminated | N/A: process | This file is V45's item-by-item check | - |
| 7 | B1 | Distinctive team voice | PARTLY | Present: "But "usually" is the whole trick", "– or nearly –", "Sell low, by appointment" with its payoff, "until our own model sank it", "Do not crush.". Against: the opener is the field's default shape (row 9); five kickers against a ration of three (row 35); the echo "we made it first: our first plan" | C3; A1 (C1) |
| 8 | B1 | Voice carries throughout, pitch included | PARTLY | Pitch: "what's left buys world stocks for the gift" sounds spoken (fixed), but the colon mirror "doesn't invest the promise: her first $300,000 buys it" stays | E6 |
| 9 | B1 | Sound unique, unlike any other team | PARTLY | Still opens "Laura Gao has one promise and one hope." (the default rival's shape, ledger A1) | Writer's call, 0 words |
| 10 | B1 | Cerebral yet witty | MET | "Sell low, by appointment" / "selling low, on a timetable printed years in advance"; "Do not crush." | - |
| 11 | B1 | Passionate yet thoughtful | PARTLY | The only concrete stake is "a building priced in Taiwan dollars". Who the residency is for (artists, writers, educators: case p.2) never appears | FR (voice guide s7) |
| 12 | B1 | Insightful yet confident | MET | "The US government defaults." said flat; no hedges | - |
| 13 | B1 | Judges enjoy reading it | PARTLY | The confession and the "But" turn land (J4 V45: "argues against itself in plain words"). First-read stumbles on panel V45: "redemptions" (J1); "the half she promised" (J1); the option line (J1, J6); "selling low, on a timetable" (J4, read twice); "Do not crush." (J2); what "97 times in 100" means for the range (J6) | E2, E3, E4, X7 |
| 14 | B1 | One unifying motif across the IPS | PARTLY | XR appears only in P10-P11. The cake image is gone (fixed), so the only thing competing with the capsule is the "by appointment" heading | A1 (C1) |
| 15 | B1 | Elaborate, vast motif | N/A: Final Report | - | - |
| 16 | B1 | Intellect and investing knowledge before language | PARTLY | Described but not named: sequence risk ("a crash in the wrong year forces a sale at the bottom – selling low, on a timetable"), reinvestment risk ("coupons paid early earn less if yields fall"), pull-to-par ("funds that mature like bonds"), human capital (P4) | X5 |
| 17 | B1 | Intellect and language together | PARTLY | Strong language; little named knowledge on the page | X5 |
| 18 | B1 | Truly extraordinary, not just competent | PARTLY | The skeleton is still the field's: ladder + stocks + lock (Commandment I). Panel V45: V40 2.17, V45 2.33 | - |
| 19 | B1 | Something no one else would think of | PARTLY | Rare, and present: "it pushes yields down, so the ladder costs more, and it shrinks the advances, speaking and licensing behind the 2028 deposit" (J4, J6 V45 both picked it out) | - |
| 20 | B1 | An "aha" | PARTLY | "Laura doesn't owe one ten-year bill. She owes ten one-year bills". No judge on panel V45 has named it yet | - |
| 21 | B1 | Keep these in your back pocket | N/A: process | - | - |
| 22 | B2 | Name unique | MET | Caplet XR | - |
| 23 | B2 | Nothing roots-themed | MET | No root, branch or tree words | - |
| 24 | B2 | Name tied to the motif | MET | "We call the plan Caplet XR, after the extended-release capsule" | - |
| 25 | B2 | Name fits the strategy, not a stretch | MET | "ten redemptions, one a year, and it only works whole" fits a ten-rung ladder. (The letter mapping is judged at rows 44, 67, 70, 71) | - |
| 26 | B2 | Motif not in every sentence | MET | One paragraph and the close | - |
| 27 | B2 | Subtle, not decorative or layered on | PARTLY | Regressed: "with nothing sold early" is cut, so the only set-up left for "Do not crush." is "it only works whole". J2 V45: "a closing flourish I could not tie to anything in the strategy" | X7 |
| 28 | B2 | Motif builds the narrative arc | PARTLY | The set-up and the payoff both sit in the last 30 words, so it's an ending, not an arc | Writer's call |
| 29 | B2 | One image; write like we write | PARTLY | Improved: cake and icing are gone. Left: the capsule, "by appointment", the leak | A1 (C1) |
| 30 | B2 | Only our team could have the name | MET | - | - |
| 31 | B2 | Optimise for ourselves first | MET | - | - |
| 32 | B2 | Motif creative and unexpected ("huh") | PARTLY | Regressed: the "huh" depends again on decoding X and R from "ten redemptions" (J1 V45: "the name's key word ('redemptions') had to be decoded") | E4 |
| 33 | B2 | Unexpected connections, syntheses | PARTLY | The note rebuilt from Treasuries and shares; rates × her income (P4); the capped range as a one-sided bet (P9) | FR |
| 34 | B2 | Sound deeply human | N/A: needs GPTZero | No score. README now labels it "GPTZero: not yet checked" (fixed from V44) | - |
| 35 | B2 | Lean but messy, human | PARTLY | Five kickers: "We buy it.", "selling low, on a timetable printed years in advance.", "which can't expire worthless.", "it only works whole.", "Do not crush." (V44 had four; the ration is three) | A1 (C1) drops one |
| 36 | B2 | Cut the human way, not by rearranging | PARTLY | Met for the cuts: five whole ideas went (ledger V45 line). Squeezes: new, "once it is named" became "once named", which dangles ("once named, every fall in stocks"); still there, the gapped clause "; ours, under one in sixty". Fixed: "a list of ways to fail" | E1, E5 |
| 37 | B2 | Parsimonious and lucid | PARTLY | Fixed: "range" before it's introduced; pitch "the change". Left: "breaks its word to co-sponsors" comes before P8 introduces what she tells them; "the gap" (P4) has to be traced back to "– or nearly –"; "Treasury funds that mature like bonds" | E1; X8 |
| 38 | B2 | Light study of the essays | N/A: process | - | - |
| 39 | B2 | Humanising lists don't work | N/A: process | - | - |
| 40 | B2 | Write more like Ahaan (tone) | MET | En-dash asides, a real "But" turn, long build then short landing ("She owes ten one-year bills"), contractions ("don't", "doesn't", "can't", "What's"), "cheque", "towards", "dearer" | - |
| 41 | B2 | Essays are tone, not everything | N/A: process | - | - |
| 42 | B3 | Caplet XR clever; justifies the team name | MET | P10 | - |
| 43 | B3 | Extend it (timed release, do not crush, more) | MET | Timed: "ten redemptions, one a year"; "Do not crush." (its set-up is weaker: row 27) | - |
| 44 | B3 | A second meaning of XR | PARTLY | Regressed from V44: implied only, by "ten redemptions" | E4 |
| 45 | B3 | "Extended response" | N/A: superseded by Book 5 | - | - |
| 46 | B3 | Product-tier label in intro or close | N/A: Final Report | Ledger A6 | - |
| 47 | B3 | Free to change name or motif | N/A: locked by Book 5 | - | - |
| 48 | B3 | Flair, voice, no over-claim obsession | MET | "The US government defaults."; "Do not crush." | - |
| 49 | B3 | Don't actively over-claim | MET | "can't expire worthless" is literally true (shares don't expire). "under one in sixty" is true and conservative (D). Minor: the pitch's "her first $300,000 buys it" drops the IPS's "or nearly" | - |
| 50 | B3 | Judges aren't mini-Lauras | MET | It argues investing to a judge | - |
| 51 | B3 | No time on grammar | N/A: process | - | - |
| 52 | B3 | En dashes | MET | Five: two spaced pairs and "at the bottom – selling low" | - |
| 53 | B3 | Marinate | N/A: process | - | - |
| 54 | B4 | Rewrite from scratch; all expectations implemented | PARTLY | V43 was the rebuild; V44 and V45 patch it. "All implemented": see this table | Section E |
| 55 | B4 | Stop tinkering on the old version | N/A: process | - | - |
| 56 | B4 | Extraordinary knowledge of concepts | PARTLY | Named: "ladder", "capital-protected note", "option", "60/40", "operating reserve", "index fund". ("rebalance" went with its clause.) Unnamed: row 16 | X5 |
| 57 | B4 | No name-dropping | MET | - | - |
| 58 | B4 | Niche concepts applied and explained | PARTLY | The note now has its weakness ("can expire worthless"), but what the option *does* is still not said. J1 V45: "the option line about shares"; J6 V45: "'which can't expire worthless' as a description of the swap" | E3 |
| 59 | B4 | Research uncited in IPS, cited in FR | MET | No citations | - |
| 60 | B4 | FR shows wide reading | N/A: Final Report | - | - |
| 61 | B4 | Knowledge supports the narrative | MET | - | - |
| 62 | B4 | North stars, all four equal | N/A: process | - | - |
| 63 | B4 | Long research process | N/A: process | - | - |
| 64 | B4 | Dazzling by 6 Nov | N/A: due later | The final for review is due end of Wed 4 Nov | - |
| 65 | B5 | Keep Caplet XR | MET | - | - |
| 66 | B5 | State the literal "extended release" | MET | "the extended-release capsule" | - |
| 67 | B5 | Both meanings of XR in the IPS | PARTLY | Regressed: literal, yes; ours ("X = ten, R = redemption") only implied by "ten redemptions" | E4 |
| 68 | B5 | Bare bones of the motif | MET | - | - |
| 69 | B5 | Everything out by the FR | N/A: Final Report | - | - |
| 70 | B5 | Make it clear the name is clever and thought out | PARTLY | Regressed: a judge has to connect "XR" to "ten redemptions" alone (J1 V45 did, with effort). The README's reason (readers 5-8: spelling it out kills the joke) is a fair voice call, but Book 5 asks that it be *clear* | E4 |
| 71 | B5 | X = 10 | PARTLY | Regressed: V44's "X for ten" is cut, and nothing on the page says X is ten | E4 |
| 72 | B5 | R not "release" | MET | "release" appears only in the literal "extended-release capsule"; R is implied as "redemptions" | - |
| 73 | B5 | No fretting over sure-sounding words | MET | - | - |
| 74 | B5 | iBonds: exact sums on exact dates | MET | "Treasury funds that mature like bonds, one rung falling due before each January" | - |
| 75 | B5 | May say near-ironclad; distinction concise | MET | Not used (optional) | - |
| 76 | B5 | Accuracy matters | PARTLY | New and true: "our first plan was three-quarters stocks, until our own model sank it" (CLAUDE.md: "Growth-first (team's original ~75% equity ...) failed", 27 Sep run). Loose, unchanged: "ours, under one in sixty" comes from M7's xr_lock design (2033 set-aside + $7,500 cushion), not L-13's 2031 set-aside that P4 describes; the 60/40's one in three rests on a rival range Keel assumed (A23, ±20%; about one in four at ±40%); "just enough to grow back into all of it" holds only when the 2027 ladder needs no top-up | E1 (scope); D |
| 77 | B5 | Human flair | MET | The heading and its payoff; "Do not crush." | - |
| 78 | B5 | No hedging | MET | - | - |
| 79 | B5 | Test on essays + TNA, not only Orwell | N/A: process | Voice reader 9 read V45 against the essays: second of four (behind voice draft A, ahead of V44 and V40) | - |
| 80 | B5 | Use Ahaan's voice, not a robotic one | PARTLY | Rows 35, 119 | C3 |
| 81 | B5 | Extraordinary | PARTLY | Row 18 | - |
| 82 | B5 | Distinctive, erudite, clever | PARTLY | Clever, yes; erudite, thin | X5 |
| 83 | B5 | Final by Sat 31 Oct | N/A: superseded (Wed 4 Nov) | - | - |
| 84 | B5 | Meet every expectation | PARTLY | This table | - |
| 85 | B9 | Meets all Wharton requirements | PARTLY | Certainty is defined and given a number, but the two still don't meet (W12). The range's confidence isn't tied to the range (W18). There's no inflation assumption (case p.4). Diversification is thin | E1, E2; X1 |
| 86 | B9 | Don't focus on formatting | N/A: process | - | - |
| 87 | B9 | Seen as intelligent and knowledgeable | PARTLY | The logic is strong (J2 V45: "the most self-contained"); most concepts go unnamed | X5 |
| 88 | B9 | Search for niche concepts | N/A: process | - | - |
| 89 | B9 | Fuse strategies; synergies | PARTLY | The note rebuilt from Treasuries and shares; rates × income. What the fusion costs us (an option catches more of a rally) still isn't said | E3 |
| 90 | B9 | Dig in unexpected places | N/A: process | - | - |
| 91 | B9 | Analyse and critique borrowed ideas | MET | Narrowly. New: the note's blind spot, "the bank's option ... can expire worthless" is implied by "shares, which can't expire worthless". The 60/40 is critiqued with numbers; the ladder's own leak and the cap's catch are stated | E3 sharpens |
| 92 | B9 | Show an idea that seems right but isn't | MET | "a 60/40 portfolio usually ends 2042 almost $200,000 ahead of ours. But "usually" is the whole trick" | - |
| 93 | B9 | Show knowledge of strategies few know | PARTLY | Only the protected note | X5 |
| 94 | B9 | Our own strategy for our client | MET | P4's advances, speaking and licensing | - |
| 95 | B9 | Logic: chains to their conclusion | MET | The recession chain (P4); the cap → "every fall in stocks comes off the gift while every rise past the top goes to Laura" → the lock (P9) | - |
| 96 | B9 | Case studies, evidence | PARTLY | Model figures (M7, L-13) and one model-driven decision ("until our own model sank it"); M1's history unused | FR |
| 97 | B9 | Voice is qualitative | N/A: process | - | - |
| 98 | B9 | Use Wall Street writers too | N/A: process | - | - |
| 99 | B9 | Don't use own agents as detectors | N/A: process | None used here | - |
| 100 | B9 | Use real web detectors | N/A: process | Not run (DETECTOR_LOG) | - |
| 101 | B9 | Detection is low priority | N/A: process | - | - |
| 102 | B9 | Don't obsess over 7.5% for VT | MET | "with world stocks at 7.5% a year": world stocks, not VT, said once | - |
| 103 | B9 | Not hamstrung by the TNA | MET | - | - |
| 104 | B9 | Use studies like the donor study | PARTLY | The lead-gift line is in the ledger for the FR. J4 V45 asks for "the range, in dollars, with the confidence"; J6 V45 sees the co-sponsor purpose as thin | X6 |
| 105 | B9 | Turn model findings into arguments | MET | M7 gives both sides of the price of safety; L-13 the 97; the first plan "sank" by the model | - |
| 106 | B9 | Every good idea lands somewhere | MET | The ledger's V45 line records the cake heading, "nothing sold early", "nothing to rebalance", "(and its fee)" and the XR bracket as FR. ("and leaves out the bank" isn't named separately, but goes with the fee) | - |
| 107 | B9 | Research is for the deliverables | N/A: Final Report | - | - |
| 108 | B9 | Don't discard ideas wantonly | N/A: process | As row 106 | - |
| 109 | B9 | Pitch not AI-squeezed; cut the human way | PARTLY | Fixed: "ten yearly cheques of $50,000"; the last sentence is a full clause. Still there: the colon mirror "doesn't invest the promise: her first $300,000 buys it" | E6 |
| 110 | B9 | No artificial timeline | N/A: process | - | - |
| 111 | B9 | Work more densely | N/A: process | - | - |
| 112 | B9 | No AI-use logging | N/A: process | - | - |
| 113 | B9 | No minute changes; big picture | N/A: process | - | - |
| 114 | B9 | Judges don't read for precision | N/A: process | - | - |
| 115 | B9 | Put message in the Bible | N/A: process | - | - |
| 116 | B10 | Diverse mock judges | N/A: process | Panel V45 SUMMARY: mean tau 0.32; #1s V40 ×3, V45 ×2, S01 ×1 | - |
| 117 | B10 | Judges don't approve every change | N/A: process | J2 V45 marks V45 down: "cautious dressed as rigorous"; J1, J2, J5 and J6 put it third; V40 still leads on mean rank | - |
| 118 | B10 | Judges don't think like Keel | N/A: process | - | - |
| 119 | B10 | Apply the voice studies | PARTLY | Applied: law 7, now with a real confession ("our first plan was three-quarters stocks, until our own model sank it"); concession then "But"; long build, short landing; a close that's an act. Not applied: law 6 (two frames: capsule + "by appointment"); law 9 (five kickers); law 10 symmetry ("So we don't invest the promise. We buy it."; "a list of ways to fail, not an adjective") | C3; A1 (C1) |
| 120 | B10 | Pitch reads as obvious AI | PARTLY | Row 109 | E6 |
| 121 | B10 | GPTZero before Caplet | PARTLY | Improved: the D25 README is headed "GPTZero: not yet checked", the fallback Commandment VI allows. But VERSIONS row 45 says "sent to Caplet 31 Oct" with this check's six fails outstanding | Hold the send until C passes, or say so |
| 122 | B10 | "Human-written only" above 50% | MISSED | No score for the pitch or the IPS (it can't be had from these sessions) | A student pastes both into gptzero.me (DETECTOR_LOG) |
| 123 | B10 | Own voice matters more than the score | PARTLY | Row 119 | - |
| 124 | B10 | Use the human-vs-AI notes | PARTLY | Eight colons (V44 had seven): "before we buy: it", "One leak remains: coupons", "made it first: our first plan", "the whole trick: about", "all of it: her floor", "has a catch: once named", "runs itself down: each", "capsule: ten redemptions". The triad stays: "the cheques come first, then the floor, then the hope" | E1 removes one colon; C3 removes the triad |
| 125 | B10 | No sentences so compressed they barely make sense | PARTLY | Fixed: "a list of ways to fail". Left: "; ours, under one in sixty"; new "once named, every fall in stocks" | E1, E5 |
| 126 | B10 | Natural variation and flair | MET | From "Do not crush." (3 words) to the 33-word sentences; textcheck: 30 sentences, spread 56% | - |
| 127 | B10 | Judges don't fixate on single lines | N/A: process | - | - |
| 128 | B10 | Mark only to Wharton's guide | N/A: process | This check argues from section B | - |
| 129 | B10 | No "every team will" | MET | No comparison with other teams. (The 60/40 is a portfolio, not a team) | - |
| 130 | B10 | No numbers plucked from thin air | MET | Every figure traces to a run or a real event (D). "three-quarters" is new (CLAUDE.md, ~75% equity) | - |
| 131 | B10 | "We model", never "we judge" | MET | "in our model" ×2; "our own model"; "we price"; no "we judge" | - |
| 132 | B10 | Stop obsessing over AI use | N/A: process | - | - |
| 133 | B10 | Drop "required trading activity" | MET | Not raised | - |
| 134 | B10 | Final by end of Wed 4 Nov | N/A: deadline | - | - |
| 135 | B10 | Overdrive | N/A: process | - | - |
| 136 | B10 | Demonstrate more work per day | N/A: process | - | - |
| 137 | B10 | Top 50 of 2,300; whatever it takes | N/A: process | - | - |
| 138 | B10 | Number one: extraordinary, not ordinary | PARTLY | Row 18 | - |
| 139 | B10 | Fresh commandments | N/A: process | - | - |
| 140 | B10 | Commandments must be followed | MISSED | The D25 README has no filled ten-line check (it points to this file). Section C fails six lines, and VERSIONS says it was sent anyway | Paste section C into D25/README; fix before sending |
| 141 | B10 | Final IPS satisfies all expectations | PARTLY | This table | Section E |
| 142 | B10 | Recursive self-improvement | MET | V45 carries most of the V44 check: E3 ("before she names any gift"), E4 (in its own words, keeping "we made it first"), E7 ("a list of ways to fail"), E2 (the pitch, nearly word for word), half of E5 ("can't expire worthless", without "catch less of a rally"), C1, C2, C3. Not taken: E1. The opposite of X4 was taken: the payoff was restored, not the heading cut | E1 |
| 143 | B10 | Initiative, intellectual risks | PARTLY | Risks in voice (the confession, "Do not crush."); none in strategy | - |
| 144 | B10 | Guess what Caplet will say | N/A: process | THINKING_LOG still has no V44 or V45 entry (its last is the V42/V43 afternoon round), although the V44 check asked for one | Add one (Commandment X) |
| 145 | B10 | Rewrite from scratch again | MET | V43 was rebuilt from voice-first draft A; V45 builds on it | - |
| 146 | B10 | List every idea of every version | N/A: process | IDEA_LEDGER, V45 line | - |
| 147 | B10 | Best ideas end up in the new IPS | PARTLY | In: the first-plan confession (back), our own failure rate, the leak + set-aside timing, the catch + lock, 97, 7.5%, the 60/40 price, thoughtful risks, the note (now critiqued), human capital. Out: the $125,000 break point, one borrower, the lead-gift line, inflation, the sleeve's size, the typical $1,000 miss | E2; X1, X3, X6 |
| 148 | B10 | Add the message to the Bible | N/A: process | - | - |
| 149 | B10b | Wharton's word with the utmost importance | PARTLY | Section B: certainty isn't evaluated against its own definition; the range's confidence isn't stated as one; assumptions are thin; diversification is thin | E1, E2 |
| W1 | W1 | Clear and creative thesis | PARTLY | Clear: "So we don't invest the promise. We buy it." Creative more in framing than in structure (row 18) | - |
| W2 | W1 | Disciplined planning across horizons and cash flows | MET | 2027 ladder; 2028 floor + fund; 2031 set-aside, range, lock; 2033 reserve | - |
| W3 | W1 | Appropriate diversification | PARTLY | Stocks: "one world index fund" only. Cheques: "The US government defaults." names the concentration, but no sentence argues for it. J6 V45: "diversification is one world fund with little said beyond that" | FR / X3 |
| W4 | W1 | Consistent with IPS/TNA/WInS | MET | Treasury bonds + iBond funds rung by rung, IBTM-like "Treasuries maturing late in 2032", one world fund (VT): matches `00_GROUND_TRUTH` s3 | - |
| W5 | W1 | Tailored to circumstances, priorities, risk considerations | MET | "Laura is willing to take thoughtful risks" answered by "But "usually" is the whole trick"; her income in P4 | - |
| W6 | W1 | ... and residency goals | MET | "a gift towards the residency's building in Taiwan"; "a building priced in Taiwan dollars comes in dearer" | - |
| W7 | W1 | Thoughtful understanding of the client | MET | P4 (J4, J6 V45: the recession-sensitive income) | - |
| W8 | W1 | Recommendations that can earn her confidence | MET | "The bottom is the floor she has owned since 2028." | - |
| W9 | W1 | Understanding and use of concepts and tools | PARTLY | Row 56 | X5 |
| W10 | W1 | Quantitative + qualitative | MET | M7 and L-13 alongside the calendar argument | - |
| W11 | W1 | Reasonable assumptions and projections | PARTLY | One assumption is stated ("world stocks at 7.5% a year"). Nothing on rates or inflation, and the model is never described | X1 |
| W12 | W1 | Evaluate reliability, facility, flexibility under varying outcomes | PARTLY | Reliability: "ours, under one in sixty" (no "says who" in its sentence; it mixes cheques with the co-sponsor promise). Facility: "about 97 times in 100", with nothing on how far it misses when it misses. Flexibility: "The other half stays hers". P4's list and P6's number still don't meet | E1, E2 |
| W13 | W1 | Articulation: teamwork, process, learning | PARTLY | Much improved: "our first plan was three-quarters stocks, until our own model sank it" (J4 V45: "a team that changed its mind because of evidence"). Still one sentence, with no teamwork; J6 V45 scores Articulation 5/10: "the only sign of process" | FR |
| W14 | W1 | Compelling, organised narrative | MET | Promise → ladder → certainty → confession + opponent → floor → range → catch → reserve → name | - |
| W15 | W1 | Authentic team voice | PARTLY | "we" ×6, "our/ours" ×7; a real event now; not detector-checked | - |
| W16 | W1 | Data used effectively | MET | "almost $200,000 ahead"; "one time in three ... under one in sixty"; "97 times in 100" | - |
| W17 | W1 | Original thinking, meaningful reflection | PARTLY | Original thinking, yes. The reflection is now real but one clause long | - |
| W18 | W1 | Contribution and uncertainty clear and credible to co-sponsors | PARTLY | The bottom is owned, the catch is explained and the lock closes it. But the case (p.3) asks "how confident ... that her 2033 contribution will fall within that range" and how unfavourable outcomes affect it; "reaches its top about 97 times in 100" answers neither directly. J6 V45: "not clearly tied to a confidence statement about the range" | E2 |
| W19 | W2 | Invest to support goals and cash flows while managing risk | MET | - | - |
| W20 | W2 | Reflect goals, horizons, liquidity, certainty, flexibility | MET | Liquidity: "each turns to cash before its cheque", "to sell any day"; flexibility: "The other half stays hers" | - |
| W21 | W2 | Q: central idea | MET | "So we don't invest the promise. We buy it." | - |
| W22 | W2 | Q: principles | MET | Buy the promise; price the leak "before she names any gift"; "the cheques come first"; on naming day "the half she promised moves into Treasuries". ("nothing sold early" is gone) | - |
| W23 | W2 | Q: balance growth, risk, liquidity, reliability, flexibility | PARTLY | The balance is argued (the concession, the $200,000 price, the "But"), but growth's share is sized nowhere. J2 V45: "I was not told the actual proportion of stocks" | X3 |
| W24 | W2 | Q: allocation changes as needs approach and payments are made | MET | 2028 floor; 2031 "the half she promised moves into Treasuries"; 2033 "it runs itself down" | - |
| W25 | W2 | Q: protect the commitment, keep flexibility for the contribution | MET | P8-P10 | - |
| W26 | W2 | Remember whom it serves | MET | - | - |
| W27 | W2 | Pitch: strategy, central idea, how it supports her goals | MET | Fixed: "what's left buys world stocks for the gift" | - |
| W28 | W2 | IPS: risk and return | MET | The return assumption, the 60/40 trade-off, the risk list | - |
| W29 | W2 | IPS: construction and diversification | PARTLY | W3, W23 | X3 |
| W30 | W2 | IPS: reserve composition over time | MET | "the ten holdings are the operating reserve, and it runs itself down: each turns to cash before its cheque" | - |
| W31 | W2 | IPS: responsible facility contribution | MET | Bottom = floor; top = floor + half the stocks; the other half kept | - |
| W32 | W2 | IPS: appropriate flexibility | MET | "to sell any day if a building priced in Taiwan dollars comes in dearer" | - |
| W33 | W2 | Framework, not individual investments | MET | - | - |
| W34 | W2 | No final reserve sums, projections, final range | MET | No sums and no range; "97 times in 100" is the rule's confidence | - |
| W35 | W2 | No citations, charts, links | MET | - | - |
| W36 | W2 | Strategy can't be revised | MET | Dated rules | - |
| W37 | W3 | Reasoning, assumptions, trade-offs | PARTLY | Reasoning and trade-off strong; assumptions: one (W11) | X1 |
| W38 | W3 | Cohesive across market outcomes | MET | - | - |
| W39 | W3 | Planned adjustments, not rewritten when markets move | MET | Dated adjustments (2028, the 2031 set-aside and lock, 2033); "it runs itself down". (The explicit "nothing sold early" is gone; row 27) | - |
| W40 | W4 | Strategy leads across deliverables | MET | - | - |
| W41 | W4 | Know your client | MET | - | - |
| W42 | W4 | Use WInS to demonstrate | N/A: WInS/FR | - | - |
| W43 | W4 | Don't focus on performance | MET | - | - |
| W44 | W4 | Explain why each investment belongs | PARTLY | Treasuries (the calendar) and the world fund (only the interest) are explained. Why Treasury funds as well as bonds isn't | FR |
| W45 | W4 | Follow the instructions | PARTLY | W12, W18 and W11 (case p.3: "explain how they evaluated that level of certainty", "state how confident"; p.4: inflation among the assumptions) | E1, E2 |
| W46 | W5 | Only WInS stocks, ETFs, Treasuries | MET | The note and its option are a foil only ("Banks sell this"; ours "swaps the bank's option for shares") | - |
| W47 | W6 | "Responsibly contribute"; keep flexibility | MET | "The other half stays hers" | - |
| W48 | W6 | "Willing to take thoughtful risks" | MET | The case's words, without quote marks, conceded then answered | - |
| W49 | W6 | 2028 deposit from advances, speaking, licensing | MET | "shrinks the advances, speaking and licensing behind the 2028 deposit" | - |

## B. Wharton's word, item by item (`WHARTON_WORD.md`)

| # | Source | Item | V45 status | Evidence | Fix |
|---|---|---|---|---|---|
| Q1 | IPS question | Central idea | MET | "So we don't invest the promise. We buy it." | - |
| Q2 | IPS question | Guiding principles | MET | W22 | - |
| Q3 | IPS question | Balance growth, risk, liquidity, reliability, flexibility | PARTLY | Argued, but growth is never sized (W23) | X3 |
| Q4 | IPS question | Allocation change as needs approach and payments are made | MET | 2027 → 2028 → 2031 → 2033 | - |
| Q5 | IPS question | Protect the commitment while keeping flexibility for the contribution | MET | P8-P10 | - |
| Q6 | IPS instruction | Remember whom it serves | MET | - | - |
| M1 | Make it clear | What we're trying to accomplish | MET | P1 | - |
| M2 | Make it clear | Why it's appropriate for the client | MET | Thoughtful risks answered; her income (P4) | - |
| M3 | Make it clear | How it balances the five | PARTLY | As Q3 | X3 |
| M4 | Make it clear | How it guides construction and decisions as needs change | MET | Dated rules; the lock on naming day | - |
| M5 | Make it clear | Protect payments while supporting a responsible contribution | MET | "the cheques come first"; "the floor she has owned since 2028" | - |
| P | Pitch | Summarise; central idea; how it supports goals and funding needs | MET | Fixed from V44: the promise bought, the 2028 floor, "what's left buys world stocks for the gift" | (E6 is voice only) |
| I1 | IPS para | Tailored to goals, horizons, needs | MET | - | - |
| I2 | IPS para | Risk and return | MET | W28 | - |
| I3 | IPS para | Liquidity | MET | "each turns to cash before its cheque"; "to sell any day" | - |
| I4 | IPS para | Construction and diversification | PARTLY | W3, W23 | X3 |
| I5 | IPS para | Planned changes as needs approach | MET | - | - |
| I6 | IPS para | Prepare for the operating commitment; reserve composition | MET | P3, P10 | - |
| I7 | IPS para | Responsible facility contribution; flexibility | MET | P8 | - |
| J1 | Guide | Reasoning, assumptions, trade-offs | PARTLY | W37 | X1 |
| J2 | Guide | Cohesive across outcomes | MET | - | - |
| J3 | Guide | Not rewritten because markets move | MET | Dated rules; "it runs itself down"; "Do not crush." | - |
| C1 | Criterion | Investment Strategy | PARTLY | Clear thesis, disciplined dates, consistent. Diversification only implied | X3 |
| C2 | Criterion | Client Knowledge and Objectives | MET | Thoughtful risks, her income, Taiwan dollars, the kept half | - |
| C3 | Criterion | Portfolio Analysis | PARTLY | Reliability has a number but no "says who" and a mixed scope (W12); one assumption only (W11); concepts unnamed | E1; X1 |
| C4 | Criterion | Articulation of Competition Experience | PARTLY | Improved: one real, dated decision ("until our own model sank it"). No teamwork or growth beyond it (W13); the FR carries the rest | FR |
| C5 | Criterion | Creativity and Presentation | PARTLY | Strong voice; the range is clear. Against: the confidence figure isn't tied to the range (W18); five first-read stumbles on panel V45 (row 13) | E2, E3, E4 |
| A1 | Advice | Let strategy lead | MET | - | - |
| A2 | Advice | Know your client | MET | - | - |
| A3 | Advice | Use WInS to demonstrate | N/A: WInS/FR | Consistent with the WInS book | - |
| A4 | Advice | Not about performance | MET | - | - |
| A5 | Advice | Explain why each investment belongs | PARTLY | W44 | FR |
| A6 | Advice | Follow the instructions | PARTLY | W45 | E1, E2 |
| H | Hard limit | Permitted instruments only | MET | Treasury bonds, Treasury funds, one world index fund; no TIPS, STRIPS or options (the bank's option is the foil) | - |

## C. The Ten Commandments (ready to paste into `D25/README.md`)

- **I. Extraordinary: FAIL.** A judge would retell three ideas: the ten one-year bills, the recession that hits both the ladder's price and the 2028 deposit, and the capped range's catch with the lock. The first plan "sunk by our own model" is the most retold line on panel V45 (J1, J2, J4, J6 all name it), but it's a story, not a strategy idea. All of it sits on the field's default skeleton (ladder + stocks + lock), and J2 V45 calls it "cautious dressed as rigorous". Panel V45: V40 2.17, V45 2.33.
- **II. Wharton only: PASS.** The text answers all five IPS questions as a whole. Panel V45's judges score on the five criteria, and this check argues from section B. The gaps that matter are W12, W18 and W11.
- **III. Write like us: FAIL.** The test asks the README to quote each move, and D25's README quotes none. The moves are there: a concession and then "But" ("Laura is willing to take thoughtful risks ... But "usually" is the whole trick"); a build then a landing ("Laura doesn't owe one ten-year bill. She owes ten one-year bills"); a wry line ("Sell low, by appointment"); and now a real event ("our first plan was three-quarters stocks, until our own model sank it"). Against the voice: the triad "the cheques come first, then the floor, then the hope", five kickers (the ration is three), eight colons.
- **IV. Clear on one reading: FAIL.** Fixed: "range" is no longer used before it's introduced. Still failing on panel V45: the small-model skimmer (J1) didn't understand "redemptions", "the half she promised" or "the option line about shares". J6 (also a small model) didn't follow "which can't expire worthless" as a description of the swap, or what "97 times in 100" means for the range. J4 read "selling low, on a timetable printed years in advance" twice, and J2 couldn't tie "Do not crush" to anything. "breaks its word to co-sponsors" comes before P8 says what she tells them.
- **V. Every number explains itself: FAIL, on one sentence.** The test is "in its own sentence". P6's "about one time in three the 60/40 misses a cheque or breaks its word to co-sponsors; ours, under one in sixty" has no "says who": the "in our model" is in P5's sentence, across a paragraph break. The V44 check's E1 wasn't taken. Every other figure passes ("in our model" with the $200,000 and the 97; the 7.5% is said to be the model's; "three-quarters" is our own plan's; the rest are the case's).
- **VI. GPTZero before Caplet: FAIL, and it can't be met here.** GPTZero can't be reached from Keel's sessions (DETECTOR_LOG), so there's no "human-written only" score. The README carries the label the commandment requires in that case: "AI DRAFT, Claude; GPTZero: not yet checked" (fixed from V44, whose folder had no README when it was checked). No agent stood in for a detector. A student pastes both texts into gptzero.me before Caplet's read.
- **VII. Few ideas at full size: PASS.** J4 V45, in effect, in three sentences: her 2027 money buys the ten cheques as Treasuries, one maturing before each January; her 2028 money buys a Treasury floor that grows back into itself, and its interest buys a world index fund; in 2031 she names a range from the floor to the floor plus half the stocks, prices the coupon shortfall first, and locks the promised half in Treasuries that day.
- **VIII. Lose no idea; critique every borrowed one: PASS, narrowly.** Ledger: the V45 line records every cut idea (row 106). Critique: the borrowed note now has its blind spot stated ("Ours swaps the bank's option for shares, which can't expire worthless"); the 60/40's is in numbers; the ladder's own leak and the cap's catch are stated. It's narrow because what our version gives up (an option's bigger share of a rally) is unsaid, and two judges couldn't follow the line (IV). E3 fixes both.
- **IX. Judges who disagree: PASS.** `judges/panel_V45/SUMMARY.md`: six judges on different models with different priors, mean Kendall tau 0.32. The #1s are V40 (J1, J5, J6), V45 (J3, J4) and S01 (J2), and each judge gives reasons in their own file (J2 marks V45 down for its caution). Before the SUMMARY existed I computed tau 0.16 from the first four score files. 0.32 is higher than panel V44's 0.24, but the judges still split on #1.
- **X. Improve without being asked: FAIL.** The second half of the test holds (V45 carries most of the V44 check's fixes: row 142). The first half doesn't: THINKING_LOG has no "what they'd say" entry for the V44 round or the V45 round, although the V44 check asked for one. Two rounds running is no longer "narrowly".

## D. Numbers

| Figure (where) | Source file and value | Wording matches? | Attribution |
|---|---|---|---|
| "ten yearly cheques of $50,000" (pitch); $50,000 every January 2033-2042; "ten cheques" (P1, P3) | Case p.3: "ten annual payments of $50,000", "fixed $50,000 and is not adjusted for inflation" | Yes | The case; none needed |
| $300,000 (2027); the 2028 deposit (pitch, P3, P4, P7) | Case p.2 | Yes | The case |
| "buys all ten cheques – or nearly" (P3); pitch "her first $300,000 buys it" | `suite_results.json` M1 `today_cost_bootstrap_22oct` $298,861 (A01: $1,139 to spare); M1: $300k bought all ten in 25.2% of months since 1871 | The IPS, yes. The pitch drops "nearly": true at today's curve, but it can move by January | A market fact |
| "our first plan was three-quarters stocks, until our own model sank it" (P5) | CLAUDE.md, strategy status: "Growth-first (team's original ~75% equity + later reserve) failed: 3-8% payment shortfall"; `keel/library/verified_2026-09-27/strategy_mc.py` (27 Sep: 3.2% miss; 13.7% if the 2028 deposit is $75k) | Yes. A real, dated team event | "our first plan", "our own model" |
| "with world stocks at 7.5% a year" (P5) | `ASSUMPTIONS.md` A06: J.P. Morgan 2027 LTCMA global equities 7.5% compound, vol 16.78% | Yes; world stocks, not VT (Book 9) | "in our model, with" |
| 60/40 "usually ends 2042 almost $200,000 ahead of ours" (P5) | M7 `laura_2042_p50`, balanced vs xr_lock: $226,292 − $30,374 = $195,918 (lognormal); $228,752 − $30,660 = $198,092 (regime); $231,463 − $31,060 = $200,403 (bootstrap). Raw history is wider ($285k vs $34k) | Yes ("usually" = the median) | "in our model" |
| "about one time in three the 60/40 misses a cheque or breaks its word to co-sponsors" (P6) | M7 balanced `p_any_promise_broken` 36.3 / 32.3 / 34.6% (history 29.6%). "Breaks its word" = gift below the bottom of the range it named, where that range is Keel's assumption (A23: its own projection ±20%). At ±40% (`regime_band40`): 23.6%, about one in four. Cheques alone (`p_payment_short`): 6.1 / 7.7 / 6.0% | Yes, given A23 | **None in its own sentence** (Commandment V) |
| "ours, under one in sixty" (P6) | M7 xr_lock `p_any_promise_broken` 1.39 / 1.63 / 0.22%, history 0 (1/60 = 1.67%; the regime world clears it by 0.04 points). Cheques alone: 0.19 / 0.24 / 0.02%. **Design:** xr_lock = V25 + lock + $7,500 cushion, set-aside in Jan 2033 (A15, A19). P4 describes L-13's design (shortfall priced in 2031 before naming), where cheques are short >$1k in 0.03-0.05% and the bottom is broken 0 times in 200,000 | True and conservative, but from a different variant than P4 describes; the scope (either promise) isn't said | **None in its own sentence** |
| "Treasuries maturing late in 2032" (P7); pitch "that repay it in 2032" | The plan: IBTM, Dec 2032 (`00_GROUND_TRUTH` s3); A13 | Yes | Plan fact |
| "just enough to grow back into all of it" (P7) | A13: the floor grows back to R = deposit − any 2027 gap. Today the gap is $0 | True today; "all of it" fails if the ladder costs more than $300k by January | Plan |
| "the interest those bonds should earn" (P7) | Not given as a number. The V44 check's one-off `xr_core.py` sum (22 Oct curve): floor $118,717, leaving $31,283 = 6.95% of $450,000. No run file exists | n/a (no figure in V45) | - |
| 2031; "half her stocks"; "since 2028" (P8) | Case p.3; plan rule (ledger D1); A14 | Yes. "The bottom is the floor" is approximate: M7's bottom is the floor less $3,700, rounded down to $5k (A14) | Case/plan |
| "the gift reaches its top about 97 times in 100" (P9) | L-13 with the slide: 97.9 / 97.6 / 96.0 / 96.7% (four worlds, 200,000 paths). Without the slide, M7 xr_lock `p_top_reached` is 84.1 / 84.5 / 93.2% | Yes: P4 states the slide's order ("set it aside from the hope, before she names any gift") | "in our model" |
| 2033; "the ten holdings" (P10) | Case p.3; plan | Yes | Case/plan |
| **Proposed E1:** "in the same model ... Ours does either under one in sixty" | As the two P6 rows | Yes ("either" = a cheque or the co-sponsor promise, which `p_any_promise_broken` counts) | "in the same model" |
| **Proposed E2:** "a typical miss is about $1,000" | L-13 slide, "median miss" $865 / $948 / $1,062 / $1,194; the bottom is broken 0 times in 200,000 in every world | Yes ("typical" = median) | In the same sentence as "in our model" |
| **Proposed X1:** "Inflation can't make a fixed cheque cost more." | Case p.3: "not adjusted for inflation" | Yes | The case |
| **Proposed X3:** a stock share | 6.95% (above): needs a run file before it's used | - | "by our sums" |

Every model figure in V45 traces to a run or a real event. Still loose: P6's two figures carry no attribution in their own sentence, and "under one in sixty" comes from a more cautious variant of the plan than the one P4 describes. The D25 README says "no new figure", but "three-quarters" is new; it is sourced above.

## E. The misses, ranked by what a Wharton judge would notice, with exact fixes

**Package A (recommended): E1 + E2 + E5, paid for by cut C3, with E4 and E6 at zero cost.** I applied it to V45's full text and measured it with `textcheck.py`: **IPS 497 strict (493 by spaces), pitch 50/50.** The deltas, each applied alone to V45, are E1 +7, E2 +6, E5 +1, E4 0 and C3 −13, which sums to +1 (496 → 497). Package A1, which swaps C3 for C1, was also measured: 497 (492 by spaces). The assembled texts were used only to prove the count. They have had no GPTZero check, cold read or panel.

1. **The reliability figure has no "says who" and mixes two promises (Commandment V, W12, C3; case p.3 "explain how they evaluated").** This is the V44 check's E1, still open. *E1:* "But "usually" is the whole trick: about one time in three the 60/40 misses a cheque or breaks its word to co-sponsors; ours, under one in sixty." → "But "usually" is the whole trick: in the same model, about one time in three the 60/40 misses a cheque or gives co-sponsors less than Laura promised. Ours does either under one in sixty." (**+7**; it also removes the gapped clause and the not-yet-introduced "its word to co-sponsors". Voice reader 9 ranks this fragment first among V45's three passages that most need rewriting: "The semicolon fragment is the tell.")
2. **The range's confidence isn't stated as confidence in the range (W18, W12, C5; case p.3 "state how confident ... within that range" and "how ... unfavorable market outcomes could affect the amount"; J6 V45, and J4 V45 wants "the range ... with the confidence").** *E2:* "the gift reaches its top about 97 times in 100." → "the gift reaches its top about 97 times in 100; a typical miss is about $1,000." (**+6**; L-13 slide, median miss $865-$1,194. Because the bottom is far below and never broken in L-13, a judge can see the gift stays inside the range. A full-stop variant could repeat "in our model".)
3. **The stock sleeve is never sized, and its diversification is one sentence (W3, W23, Q3, I4, C1; J2 and J6 V45; J2, J5, J6 V44).** This is not bought here, because it needs a run file first (D, X3). Once the run exists: "buys one world index fund." → "buys one world index fund, about a fourteenth of her money by our sums." (**+9**, measured. Package A has no words left, so this needs the alternative cut C1 on top of A: measured at IPS 493 with both.)
4. **The note line is still opaque to the small-model readers, and it doesn't say what ours gives up (Commandment IV/VIII, rows 58, 89; J1, J6 V45).** *E3 (package B):* "Ours swaps the bank's option for shares, which can't expire worthless." → "The bank spends that interest on an option, which can expire worthless; we buy the shares." (**+5**.)
5. **XR's letters aren't mapped, and "Do not crush." is orphaned again (rows 27, 44, 67, 70, 71; J1 and J2 V45).** *E4 (in A, 0 words, writer's call):* "ten redemptions, one a year" → "X redemptions, one a year": the Roman X stands in for "ten", so the letter is shown on the page, not glossed. The risk is that a reader takes the X for a placeholder. The fallback is V44's bracket, which reader 8 disliked. *X7 (package B):* "each turns to cash before its cheque." → "each turns to cash before its cheque, and none is sold early." (**+5**; it puts back the set-up that "it only works whole" and "Do not crush." need.)
6. **A new squeeze (rows 36, 125).** *E5 (in A):* "once named, every fall in stocks" → "once it's named, every fall in stocks" (**+1**; it fixes the dangling modifier.)
7. **The pitch's colon mirror (rows 8, 109, 120).** *E6 (0 words):* "Caplet XR doesn't invest the promise: her first $300,000 buys it, in Treasuries" → "Caplet XR doesn't invest the promise. Her first $300,000 buys it, in Treasuries". Measured: **pitch 50**. It now echoes P2's "So we don't invest the promise. We buy it."

**The cut that pays for A (a whole idea, not a squeeze):**
- *C3: cut* "If anything changes, the cheques come first, then the floor, then the hope." (**−13**.) It's the draft's one triad (Commandment III). Voice reader 9 objects to it on two counts: the colon-and-triad run at the close, and "the hope" made to hold a bank balance ("then the floor, then the hope"). The priority it states is already shown where it acts: the shortfall is set aside "from the hope, before she names any gift", the bottom is "the floor she has owned since 2028", and the promised half moves into Treasuries on naming day. The cost: the principle is no longer said in one line (W22, Q2), and J2 V45 listed it as content. It goes to the FR as the stated waterfall.
- *A1, the alternative cut C1 (measured, also 497):* cut the heading "Sell low, by appointment" and its payoff "– selling low, on a timetable printed years in advance" instead, so P6 ends "forces a sale at the bottom." (**−13**.) For it: J4 V45 read the payoff twice; it takes kickers from five to four and frames from two to one (law 6). Against it, and the reason it's not the recommendation: voice reader 9 calls the payoff "the odd specific detail that proves a person wrote it" and already finds V45 "flatter" for having only one heading. C1 would leave none.

**Package B (only if the team accepts both cuts): C1 + C3 + E1 + E2 + E3 + E4 + E5 + X7, measured: IPS 494 strict (489 by spaces).** This adds the clearer note (E3, +5) and the "none is sold early" set-up (X7, +5), and loses both the heading and the triad. X3 (+9) would then not fit until another 6 words come out.

**Not bought (no words left; each is first in line if a cut above is rejected or another is accepted):**
8. **X1, no inflation assumption (W11, W37, J1; case p.4 "the effect of inflation on portfolio projections and facility costs").** Add "Inflation can't make a fixed cheque cost more." after "one rung falling due before each January." (**+8**, measured.)
9. **X2, the triad (Commandment III) if A1 is chosen instead of C3.** "If anything changes, the cheques come first, then the floor, then the hope." → "If anything goes wrong, the hope gives way to the floor, and the floor to the cheques." (**+4**, measured.)
10. **X8, "the gap" (P4) needs a referent.** "behind the 2028 deposit that must cover the gap." → "behind the 2028 deposit, just when it must cover any shortfall in the ladder." (**+5**, measured.)
11. **X5, concepts described but not named (rows 16, 56, W9).** For example, "Planners call this sequence risk." before "Laura doesn't owe one ten-year bill." (**+5**, measured.) Otherwise it goes to the FR.
12. **X6, why a range at all: the lead-gift effect (row 104).** "In 2031 she gives co-sponsors a range, low enough to keep her word and high enough that her lead gift draws bigger ones." (**+16**, measured.) It's in the ledger for the FR.
13. **Process (costs no words; Commandments III, VI, X; rows 121, 140, 144).** Update `D25/README.md`: IPS 496 (or 497 after E); the four late fixes; the quoted voice moves; section C pasted in as its ten-line check; "three-quarters" in a number table. Add a V44/V45 "what Caplet would say" entry to THINKING_LOG. Correct VERSIONS row 45's "sent to Caplet", or record that it was sent with this check's six fails open. A student gets a GPTZero score.
