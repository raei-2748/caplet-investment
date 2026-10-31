# AI-generated check (Claude), 1 Nov 2026, not for submission

**For the team lead, in eight lines.**
1. **Counts** (from `office/tools/textcheck.py`): pitch **50/50**, IPS **497/497** strict (496 by spaces). Section E's Package A was measured at **IPS 497, pitch 50**.
2. **Tally:** A (198 rows) **MET 76 · PARTLY 63 · MISSED 4 · N/A 55**; for V45 it was 77 / 64 / 2 / 55. B (34 rows) **MET 21 · PARTLY 11 · MISSED 1 · N/A 1**; for V45 it was 23 / 10 / 0 / 1.
3. **Commandments: PASS 3 (II, VII, IX) · FAIL 7 (I, III, IV, V, VI, VIII, X).** For V45 it was 4 pass and 6 fail. VIII newly fails, because the ledger has no V46 line. V newly fails, because "$15,000" doesn't say it's an average. D26 has no README, so it has no ten-line check and no GPTZero label of its own.
4. **Top three misses:** (a) The case's two explicit asks now have no number on the page: a confidence for the range ("97 in 100" cut) and an evaluated level of certainty for the cheques ("under one in sixty" went with the 60/40). There's also no stated assumption at all, since "7.5%" was cut. Panel V46: J2, J3, J4, J5 and J6 all mark this. (b) "it usually wins ... about $15,000 more by 2042". The $15,000 is a **mean**. The typical (median) lead on V46's own design is **$9,300-$11,800**. (c) "– selling low, on a timetable printed years in advance" grammatically trails "where we promise $140,000", so it says *we* sell low. The heading also floats at 70% of the page (J5, reader 10).
5. **Fixed from V45:** the straw-man 60/40, scored against a range Keel drew for it, is gone. The rival is now the one judges actually favour (A09), priced honestly ("We'd pay the $15,000"). Also taken from the V45 check: E5 ("once it's named"), E6 (pitch full stop) and C3 (the triad is cut). A16 and A28 are accurate.
6. **Broken compared with V45:** the range's confidence, the priority order (J1, J2, J3, J6 ask where it went), the return assumption and "ten one-year bills" (the line three C-04 judges could retell). Kickers rose from 5 to 7. There's a new compression ("in a typical year"). The worst-twentieth slice is back in the IPS, although the Lab (L-14) and Laura's Room (LR-08) had both ruled it a chosen stress test for the Final Report only. Panel V46 ranks V46 **3.83, fourth of six** (V45 3.17, LR3 1.17), and Keel has already moved on to V47 (`../D27/`).
7. **Number verdict: no figure is invented, and every one traces to a run or the case.** My read-only rerun of A26 reproduces its means to the dollar (S0, S1). Four wording mismatches: "$15,000" needs "on average"; "in a typical year" should be "in a typical future"; "set it aside from the hope" is wrong on the design (Laura's half absorbs the set-aside first: L-13 `run.py` line 29); and "The bottom is the floor" leaves the $150k → $145k → $140k steps unexplained. The pitch's "buys it" still drops "nearly".
8. **Process:** D26 has no README, the IDEA_LEDGER has no V46 line and THINKING_LOG has no V46 entry. VERSIONS row 46 carries the label "GPTZero: not yet checked", and nothing records V46 as sent.

**What was checked.** I read `pitch.txt` and `ips_V46.txt` in this folder cold, as a reader who didn't write them. I checked them against `WHARTON_WORD.md`, all of `BIBLE.md` (the Ten Commandments included; unchanged since the V45 check), every row of `BIBLE_AUDIT.md` s1 (each judged fresh for V46, using the V45 check's row list), the case (`Laura_Gao_2026_Client_Profile.txt`), `voice/06_voice_guide.md` and `IDEA_LEDGER.md`. Numbers: `models/results/suite_results.json` (M1, M3, M7), `models/xr_core.py` (I recomputed the ladder cost on the newest curve in the repo, 22 Oct: $298,861), `rooms/lab/L-13_slide_the_range.md` and its `run.py`, `rooms/lab/L-14_price_of_the_floor.md`, `rooms/archive_checks/A26_results.json` (plus a **read-only copy** of `A26_lr3_on_v45_design.py` in `/tmp`, writing only to `/tmp`, that adds the per-path median; S0 and S1 reproduce every A26 mean exactly), `rooms/courtroom/C-04_the_whole_price.md`, the 31 Oct inboxes (archive, courtroom, Laura's Room, Window) and `rooms/window/` W-01 to W-04. As corroboration only, never as the marking scheme: panel V46 (`judges/panel_V46/`: SUMMARY, KEY.json and all six score files) and voice reader 10 (`voice_first/readers/reader10_verdict.md`, where V46 is Entry 4). I'm not an AI detector and don't judge AI-ness here. I didn't edit the draft or any script, and I committed nothing.

V46's paragraphs, for reference: P1 opener · P2 "So we don't invest the promise. We buy it." · P3 the 2027 ladder · P4 certainty + the leak + the 2031 set-aside · P5 floor + fund + the note · P6 the 2031 range · P7 the catch + the lock · H1 "Sell low, by appointment" · P8 the confession + the rival + its price · P9 "But "usually" is the whole trick" + worst twentieth + "We'd pay the $15,000." · P10 reserve + XR · P11 "Do not crush."

## D. Numbers (first, as asked; every figure in V46, re-checked against the models and rooms on 1 Nov)

"True on V46's design" means the 2027 ladder, the 2028 floor and fund, the 2031 mark with the slide (the shortfall priced and taken off both ends before naming), and the lock on naming day. That is the L-13 → L-14 chain A26 runs ("V45's design"), and V46 changes none of it.

| Figure (where) | Source file and value | True on V46's design? Wording matches? | Says who, in its own sentence |
|---|---|---|---|
| "ten yearly cheques of $50,000" (pitch); "$50,000 every January from 2033 to 2042" (P1); "all ten cheques" (P3) | Case :88-90: "ten annual payments of $50,000", "a fixed $50,000 and is not adjusted for inflation" | Yes | The case; none needed |
| "Her first $300,000" (pitch, P3); "the 2028 deposit" (pitch, P4, P5, P8) | Case :43-45 | Yes | The case |
| "buys all ten cheques – or nearly" (P3) | `suite_results.json` M3 `cost_22oct` $298,861, `headroom` $1,139 = **3.8bp**; a 10bp rally leaves a $1,842 gap. Recomputed today with `xr_core.bootstrap_cost`: $298,861. **The 22 Oct curve is the newest in the repo**, so this figure is ten days old | The IPS, yes: "or nearly" is what makes it true | A market fact; none needed |
| Pitch: "Her first $300,000 buys it" | As above | **Loose.** It drops "nearly", which is true on one day's curve only. The Window has flagged this at four gates (28-31 Oct) | - |
| "Treasuries maturing late in 2032" (P5); pitch "repay it in 2032" | The plan: IBTM, Dec 2032 (`00_GROUND_TRUTH` s3); A13 | Yes | Plan fact |
| "just enough to grow back into all of it: her floor" (P5) | A13: the floor grows back to R = the deposit less any 2027 gap. The gap is $0 on 22 Oct | True today; "all of it" fails if the ladder costs more than $300k in January (3.8bp away) | Plan |
| "Most of the 2028 deposit" / "What's left – the interest those bonds should earn" (P5) | L-14 (Window R06 on this design): the fund on 2 Jan 2028 is **$31,082 median = 20.7% of the 2028 deposit**, 6.6% of the portfolio (S0, S1) | Yes: about 79% goes to Treasuries ("most") | No figure in V46. X3 below would add one, and it now has a run file |
| "half her stocks" (P6); "the half she promised moves into Treasuries" (P7) | Plan rule (ledger D1); L-13 lock | Yes | Plan |
| "The bottom is the floor she has owned since 2028" (P6) | `xr_core.caplet_xr(bottom_cut=3700)`: bottom = floor less $3,700, rounded down to $5k, then cut by the 2031 mark's uncovered gap `u31 = ceil5(max(S31 + C − L33 − 0.5·V31, 0))` (L-13 `run.py` line 29), with cut > 0 in 16.9% of S0 paths. A26: XR's median bottom is **$145,000** | **Approximate, and the draft contradicts itself.** P5 says the floor grows back to "all of" the 2028 deposit ($150,000), but P8 has us promising $145,000 and P9 $140,000. V46 cut V45's "after the 2031 set-aside", which was the only bridge | Plan |
| "In 2031 we price that shortfall and set it aside from the hope, before she names any gift" (P4) | L-13 line 29: the shortfall plus a $7,500 cushion is set **first against Laura's half** (0.5·V31) and her cash (L33), and only the remainder comes off the range. L-13 door (b): her half is sold for the cheques in 71.7% of S0 paths. LR-08 s3 says the same | **Wrong on the design.** "From the hope" points at the gift, but it's mostly what she keeps. LR-08's fix: "from what she keeps" (+1). This also strains P6's "The other half stays hers, to sell any day" | - |
| "One leak remains: cash paid early earns less if yields fall" (P4) | A16 (Archive): the coupons plus the Feb-2037 note's 10.5 months of waiting principal; L-13: cheques short by >$1k in 0.03 / 0.03 / 0.05 / 0.05% of paths (S0 / S1 / S6 / S2) | Yes. "Remains" doesn't say the leak is closed. LR-08 counts XR short *somewhere* in 0.4% of house paths (any size, median $680), against 0.03% for A09. That's a price V46 doesn't mention (it makes no contrary claim) | No figure |
| "our first plan was three-quarters stocks, until our own model sank it" (P8) | CLAUDE.md (growth-first, ~75% equity, 3-8% shortfall, 27 Sep); `verified_2026-09-27/strategy_mc.py` (3.2% miss); W-04 restamp on today's basis 2.3-2.5% | Yes: a real, dated team event | "our first plan", "our own model" |
| "Laura has been willing to take thoughtful risks all her career" (P8) | Case :69-71: "she has been willing to take thoughtful risks throughout her entrepreneurial career" | Yes. A close paraphrase, without quote marks | The case (implicit) |
| "the strongest rival ... keeps our ladder, leaves the 2028 deposit mostly in stocks, and buys its bottom in January 2031" (P8) | L-14 "A09 as built (at its strongest)": the same ladder; R goes 80% world stocks / 20% intermediate Treasuries; on 1 Jan 2031 a share k of the pot buys a 2-year Treasury | Yes. "Strongest" is Keel's own label (L-14; two of six panel-4 judges put A09 first). Panel V46 ranks A09 4.67 of six as a *text*, which says nothing about its investment merit | Keel's label |
| "Set in our model to promise the same $145,000 as us" (P8) | A26 S0 and S1: XR median bottom $145,000; A09 matched at k = 0.75-0.77 also names $145,000 | Yes | "in our model" |
| "in a typical year" (P8) | It's the median across 200,000 modelled futures. There is one naming day, not a typical year | **Wording mismatch.** It should be "in a typical future" (0 words, E4). Tess raised the same point at C-04 ("reads two ways") | - |
| "it usually wins" (P8) | A26: A09 ahead (gift + Laura's 2042 money) in **61.1-63.7%** of paths (k 0.75-0.77, S0 and S1) | Yes ("usually" = about 5 in 8) | "in our model" (same sentence) |
| "counting the gift and what she keeps, it leaves her about $15,000 more by 2042" (P8) | A26 mean (A09 − XR), gift + Laura's 2042 money: **$13,680-$16,169 (S0), $14,178-$16,632 (S1)**. **Median, from my read-only rerun: $9,261-$11,598 (S0), $9,417-$11,772 (S1)** | **Mismatch.** $15,000 is a mean, but V46 dropped LR3's "on average" and sets the figure right after "usually wins", so a reader takes it as the typical lead, about half as large again as the true one (≈$10,000). E1 below fixes it (+2) | "in our model", but it never says it's an average, and the stock assumption it rests on (7.5%) is no longer stated (W11) |
| "In the worst twentieth of our futures for stocks in 2028-30" (P9) | L-14 / A26 `worst5`: the 5% of paths with the worst 2028-30 world-stock return | True as a definition. **But both rooms that built the number ruled it out of the IPS:** L-14 ("Not adopted: the worst-5% slice"; Jun: it "flatters XR by construction") and LR-08 (Kai's numbers rule: "a chosen stress test: Final Report only"). C-04 put it back. The unsliced pair (named bottom under $100k: A09 about 1 in 13, XR about 1 in 150, LR-08 house, after the mark) is the fairer one. "Our futures" can also be read as futures *contracts* (a derivative, which isn't permitted) | "our futures" is a weak says-who: it never says "modelled" |
| "the rival can promise co-sponsors only about $90,000, where we promise $140,000" (P9) | A26 `worst5_bottom_p50`: **S0 $90,000 v $140,000; S1 $85,000 v $135,000** | True on S0 (rates and stocks independent). P4's own argument (a recession moves yields and stocks together) is S1, where it's $85k v $135k: still "about", but the softer world was picked | As the row above |
| "We'd pay the $15,000." (P9) | As the $15,000 row | As a price, the mean is the right figure (C-04: "the premium is a mean"), but the same "on average" is needed upstream | Refers back |
| "From 2033 the ten holdings" (P10) | Case :95; plan | Yes | Case/plan |
| "ten redemptions, one a year" (P10) | The ten rungs | Yes | Plan |
| **Cut from V45, so no longer checked in text:** "97 times in 100", "with world stocks at 7.5% a year", 60/40 "almost $200,000", "one time in three / under one in sixty" | L-13 slide: 97.9 / 97.6 / 96.0 / 96.7%; A06 7.5% | Still true on V46's design: the 97 can come back unchanged (E2) | - |
| **Proposed E2:** "in our model the gift reaches its top about 97 times in 100" | L-13 arm A (slide), which is XR's row in L-14 and A26 ("reproduces L-13's 'A slide' exactly"); Window re-ran S0 and S6 on 31 Oct and the JSON was identical | Yes | "in our model" |
| **Proposed X3:** "about a fifteenth of the portfolio in our model" | L-14: 6.6%, one part in 15.1 (S0, S1); one in 24 after a 2-point fall | Yes, of the **portfolio** (not "everything she owns") | "in our model" |
| **Proposed X9:** "a cheque falls over $1,000 short about three times in 10,000" | L-13 / L-14 XR: 0.03% (S0, S1), 0.05% (S6, S2) | Yes on S0 and S1 | "in our model" |

**Number verdict.** No number is made up. Every model figure traces to A26 or L-13/L-14 on V46's own design, and A26 reproduces exactly. Four wordings aren't true as written: the "$15,000" (a mean, presented as the typical win), "in a typical year", "set it aside from the hope" (it's mostly from her half), and "The bottom is the floor", which jars with $145,000 and $140,000. The pitch still says "buys it" without "nearly". One selection is open to challenge: the worst-twentieth slice, which two rooms had kept out of the IPS. All model figures sit on the 22 Oct curve, the newest in the repo.

## A. Every expectation in BIBLE_AUDIT s1, judged for V46

| # | Book | Expectation | V46 status | Evidence (V46's exact words, or what is absent) | Fix |
|---|---|---|---|---|---|
| 1 | CN | Rewrite slowly: long thinking, research, analysis | N/A: process | V46 is a same-morning re-assembly: V45 plus the Archive's A26 paragraph, put back into V45's voice. No THINKING_LOG entry | - |
| 2 | CN | THINK; don't be hasty | N/A: process | The cuts were whole ideas, but four of them (97, the priority line, 7.5%, ten bills) were the ones panel V46 then missed | - |
| 3 | CN | Creative, original, knowledgeable, evidently widely read | PARTLY | Original: "A high degree of certainty is a list of ways to fail, not an adjective."; "the strongest rival takes one for her". Knowledge: "Ours swaps the bank's option for shares, which can't expire worthless." Lost: "Laura doesn't owe one ten-year bill. She owes ten one-year bills" (C-04: the line three judges could retell). One borrowed concept is named | X5 |
| 4 | CN | All Bibles equal; grasp the intent | N/A: process | - | - |
| 5 | CN | Autonomy; may question Caplet | N/A: process | - | - |
| 6 | CN | Expectations met, however disseminated | N/A: process | This file is V46's item-by-item check | - |
| 7 | B1 | Distinctive team voice | PARTLY | Present: "and the strongest rival takes one for her" (reader 10: "the most generous line about Laura in the set"), "We'd pay the $15,000." (reader 10: "the best short landing"), "– or nearly –", "until our own model sank it". Against: the default opener (row 9); seven kickers against a ration of three (row 35); "the worst twentieth of our futures" (reader 10: "model-speak") | E7; C7 |
| 8 | B1 | Voice carries throughout, pitch included | MET | Pitch E6 taken: "Caplet XR doesn't invest the promise. Her first $300,000 buys it" (the colon mirror is gone) | - |
| 9 | B1 | Sound unique, unlike any other team | PARTLY | Still opens "Laura Gao has one promise and one hope." (the default rival's shape, ledger A1) | Writer's call, 0 words |
| 10 | B1 | Cerebral yet witty | MET | "the strongest rival takes one for her"; "We'd pay the $15,000."; "Do not crush." | - |
| 11 | B1 | Passionate yet thoughtful | PARTLY | The only concrete stake is still "a building priced in Taiwan dollars". The people the residency serves (case :78, artists and writers) never appear | FR (voice guide s7) |
| 12 | B1 | Insightful yet confident | MET | "The US government defaults." said flat; "We'd pay the $15,000." | - |
| 13 | B1 | Judges enjoy reading it | PARTLY | It lands: "We'd pay the $15,000" (J2: "a clearly priced trade-off, which I respect"), the downside in dollars (J6). Stumbles: the heading "breaks the read" (J5); the rival's set-up "reads like the caption of a chart" (reader 10); "selling low" attached to the wrong clause (reader 10); "Do not crush" as an ending (J3, on the shared close) | E3/C7, E4, E7 |
| 14 | B1 | One unifying motif across the IPS | PARTLY | XR appears only in P10-P11. "By appointment" competes and now sits at 70% of the page | C7 |
| 15 | B1 | Elaborate, vast motif | N/A: Final Report | - | - |
| 16 | B1 | Intellect and investing knowledge before language | PARTLY | Regressed: sequence risk lost its explanation with "ten one-year bills". Described but not named: reinvestment risk ("cash paid early earns less if yields fall"), pull-to-par ("funds that mature like bonds"), human capital (P4) | X5 |
| 17 | B1 | Intellect and language together | PARTLY | Strong language; little named knowledge | X5 |
| 18 | B1 | Truly extraordinary, not just competent | PARTLY | Still the field's skeleton: ladder + stocks + lock (Commandment I). Panel V46: **3.83, fourth of six**, behind LR3 1.17, S01 2.83 and V45 3.17 | - |
| 19 | B1 | Something no one else would think of | PARTLY | Kept: "it pushes yields down, so the ladder costs more, and it shrinks the advances, speaking and licensing behind the 2028 deposit" (J3 V46: "a recession hits the ladder's cost and Laura's 2028 income at the same mo[ment]") | - |
| 20 | B1 | An "aha" | PARTLY | Regressed: the aha ("ten one-year bills") is cut. What's left is "Banks sell this as a capital-protected note", which small-model readers stumble on (row 58) | X5 or restore in FR |
| 21 | B1 | Keep these in your back pocket | N/A: process | - | - |
| 22 | B2 | Name unique | MET | Caplet XR | - |
| 23 | B2 | Nothing roots-themed | MET | None | - |
| 24 | B2 | Name tied to the motif | MET | "We call the plan Caplet XR, after the extended-release capsule" | - |
| 25 | B2 | Name fits the strategy, not a stretch | MET | "ten redemptions, one a year, and it only works whole" | - |
| 26 | B2 | Motif not in every sentence | MET | One paragraph and the close | - |
| 27 | B2 | Subtle, not decorative or layered on | PARTLY | "Do not crush." still has only "it only works whole" to point back to. J3 V46 (on the same close in LR3): "'Do not crush' as an ending" not understood | X7 |
| 28 | B2 | Motif builds the narrative arc | PARTLY | Set-up and payoff both sit in the last 30 words | Writer's call |
| 29 | B2 | One image; write like we write | PARTLY | The capsule, "by appointment", the leak | C7 |
| 30 | B2 | Only our team could have the name | MET | - | - |
| 31 | B2 | Optimise for ourselves first | MET | - | - |
| 32 | B2 | Motif creative and unexpected ("huh") | PARTLY | The "huh" still depends on decoding X and R from "ten redemptions" (E4 of the V45 check wasn't taken) | V45 check E4 |
| 33 | B2 | Unexpected connections, syntheses | PARTLY | The note rebuilt from Treasuries and shares; rates × her income; the capped range as a one-sided bet | FR |
| 34 | B2 | Sound deeply human | N/A: needs GPTZero | No score. D26 has no README; VERSIONS row 46 says "GPTZero: not yet checked" | - |
| 35 | B2 | Lean but messy, human | PARTLY | Seven kickers (V45 had five; the ration is three): "We buy it.", "which can't expire worthless.", "But "usually" is the whole trick.", "– selling low, on a timetable printed years in advance.", "We'd pay the $15,000.", "and it only works whole.", "Do not crush." | C7 drops one |
| 36 | B2 | Cut the human way, not by rearranging | PARTLY | The cuts were whole ideas (the 60/40, the bills, the 97, the triad). Fixed: "once it's named". New compressions: "to promise the same $145,000 as us in a typical year"; "the worst twentieth of our futures for stocks in 2028-30" | E4, E7 |
| 37 | B2 | Parsimonious and lucid | PARTLY | "the gap" (P4) still has to be traced back to "– or nearly –"; "our futures"; $150k floor → $145k → $140k never bridged (D) | E5; X8 |
| 38 | B2 | Light study of the essays | N/A: process | - | - |
| 39 | B2 | Humanising lists don't work | N/A: process | - | - |
| 40 | B2 | Write more like Ahaan (tone) | MET | En-dash asides, a real "But" turn, a long build then a short landing ("... printed years in advance. We'd pay the $15,000."), contractions, "cheque", "towards", "dearer" | - |
| 41 | B2 | Essays are tone, not everything | N/A: process | - | - |
| 42 | B3 | Caplet XR clever; justifies the team name | MET | P10 | - |
| 43 | B3 | Extend it (timed release, do not crush, more) | MET | "ten redemptions, one a year"; "Do not crush." | - |
| 44 | B3 | A second meaning of XR | PARTLY | Implied only, by "ten redemptions" | V45 check E4 |
| 45 | B3 | "Extended response" | N/A: superseded by Book 5 | - | - |
| 46 | B3 | Product-tier label in intro or close | N/A: Final Report | - | - |
| 47 | B3 | Free to change name or motif | N/A: locked by Book 5 | - | - |
| 48 | B3 | Flair, voice, no over-claim obsession | MET | "The US government defaults."; "We'd pay the $15,000." | - |
| 49 | B3 | Don't actively over-claim | MET | No claim beyond its run. The selection of the worst-twentieth slice is judged at row 76, not here. Minor: the pitch's "buys it" drops "nearly" | - |
| 50 | B3 | Judges aren't mini-Lauras | MET | - | - |
| 51 | B3 | No time on grammar | N/A: process | - | - |
| 52 | B3 | En dashes | MET | Five: two spaced pairs and "$140,000 – selling low" | - |
| 53 | B3 | Marinate | N/A: process | - | - |
| 54 | B4 | Rewrite from scratch; all expectations implemented | PARTLY | V43 was the rebuild; V44-V46 patch it | Section E |
| 55 | B4 | Stop tinkering on the old version | N/A: process | - | - |
| 56 | B4 | Extraordinary knowledge of concepts | PARTLY | Named: "ladder", "capital-protected note", "option", "operating reserve", "index fund". "60/40" went with its comparison. Unnamed: row 16 | X5 |
| 57 | B4 | No name-dropping | MET | - | - |
| 58 | B4 | Niche concepts applied and explained | PARTLY | Unchanged from V45: what the option *does* is never said. Reader 10: "the jargon-first note sentence" | V45 check E3 |
| 59 | B4 | Research uncited in IPS, cited in FR | MET | - | - |
| 60 | B4 | FR shows wide reading | N/A: Final Report | - | - |
| 61 | B4 | Knowledge supports the narrative | MET | - | - |
| 62 | B4 | North stars, all four equal | N/A: process | - | - |
| 63 | B4 | Long research process | N/A: process | - | - |
| 64 | B4 | Dazzling by 6 Nov | N/A: due later | Final for review due end of Wed 4 Nov | - |
| 65 | B5 | Keep Caplet XR | MET | - | - |
| 66 | B5 | State the literal "extended release" | MET | "the extended-release capsule" | - |
| 67 | B5 | Both meanings of XR in the IPS | PARTLY | Ours is implied only | V45 check E4 |
| 68 | B5 | Bare bones of the motif | MET | - | - |
| 69 | B5 | Everything out by the FR | N/A: Final Report | - | - |
| 70 | B5 | Make it clear the name is clever and thought out | PARTLY | A judge has to connect "XR" to "ten redemptions" alone | V45 check E4 |
| 71 | B5 | X = 10 | PARTLY | Nothing on the page says X is ten | V45 check E4 |
| 72 | B5 | R not "release" | MET | "release" appears only in the literal | - |
| 73 | B5 | No fretting over sure-sounding words | MET | - | - |
| 74 | B5 | iBonds: exact sums on exact dates | MET | "Treasury funds that mature like bonds, one rung falling due before each January" | - |
| 75 | B5 | May say near-ironclad; distinction concise | MET | Not used (optional) | - |
| 76 | B5 | Accuracy matters | PARTLY | Section D: "$15,000" is a mean, set after "usually"; "in a typical year"; "set it aside from the hope" (the model takes it from her half first); "The bottom is the floor" against $145k/$140k; the worst-twentieth slice, which L-14 and LR-08 ruled out of the IPS; the pitch's "buys it" | E1, E4, E5; D |
| 77 | B5 | Human flair | MET | "the strongest rival takes one for her"; "We'd pay the $15,000." | - |
| 78 | B5 | No hedging | MET | - | - |
| 79 | B5 | Test on essays + TNA, not only Orwell | N/A: process | Voice reader 10: A > V45 > **V46** > LR3 | - |
| 80 | B5 | Use Ahaan's voice, not a robotic one | PARTLY | Rows 35, 119 | C7 |
| 81 | B5 | Extraordinary | PARTLY | Row 18 | - |
| 82 | B5 | Distinctive, erudite, clever | PARTLY | Clever, yes; erudite, thin | X5 |
| 83 | B5 | Final by Sat 31 Oct | N/A: superseded (Wed 4 Nov) | - | - |
| 84 | B5 | Meet every expectation | PARTLY | This table | - |
| 85 | B9 | Meets all Wharton requirements | PARTLY | Regressed: no confidence for the range, no evaluated certainty for the cheques and no stated assumptions (W11, W12, W45). Diversification is still thin | E2; X1, X9 |
| 86 | B9 | Don't focus on formatting | N/A: process | - | - |
| 87 | B9 | Seen as intelligent and knowledgeable | PARTLY | J1 V46: "a little thinner than the others ... the case rests on fewer numbers" | E2 |
| 88 | B9 | Search for niche concepts | N/A: process | - | - |
| 89 | B9 | Fuse strategies; synergies | PARTLY | The note rebuilt from Treasuries and shares; what the fusion costs (an option catches more of a rally) still isn't said | V45 check E3 |
| 90 | B9 | Dig in unexpected places | N/A: process | - | - |
| 91 | B9 | Analyse and critique borrowed ideas | MET | The rival is critiqued with its price and its tail; the note's blind spot ("can't expire worthless"); our own leak and the cap's catch | - |
| 92 | B9 | Show an idea that seems right but isn't | MET | "it usually wins ... But "usually" is the whole trick." | - |
| 93 | B9 | Show knowledge of strategies few know | PARTLY | Only the protected note | X5 |
| 94 | B9 | Our own strategy for our client | MET | P4's advances, speaking and licensing | - |
| 95 | B9 | Logic: chains to their conclusion | MET | The recession chain (P4); the catch → the lock (P7); the rival's bottom "with whatever those stocks fetch that morning" → $90,000 (P8-P9) | - |
| 96 | B9 | Case studies, evidence | PARTLY | Model figures (A26) and one model-driven decision ("until our own model sank it"); Giving USA (W-04) unused | FR |
| 97 | B9 | Voice is qualitative | N/A: process | - | - |
| 98 | B9 | Use Wall Street writers too | N/A: process | - | - |
| 99 | B9 | Don't use own agents as detectors | N/A: process | None used here | - |
| 100 | B9 | Use real web detectors | N/A: process | Not run | - |
| 101 | B9 | Detection is low priority | N/A: process | - | - |
| 102 | B9 | Don't obsess over 7.5% for VT | MET | Not mentioned (though now no return assumption is stated at all: W11) | - |
| 103 | B9 | Not hamstrung by the TNA | MET | - | - |
| 104 | B9 | Use studies like the donor study | PARTLY | The donor/recession timing (W-04, Giving USA) and the lead-gift line stay in the FR | X6 |
| 105 | B9 | Turn model findings into arguments | MET | A26 → "We'd pay the $15,000."; "until our own model sank it" | - |
| 106 | B9 | Every good idea lands somewhere | PARTLY | Regressed: IDEA_LEDGER has **no V46 line**. The cut ideas (the 60/40 price, "one in three / under one in sixty", "ten one-year bills", "97 in 100", the priority triad, "7.5%") are named for the FR only in room files (C-04 s4; LR-08) and in VERSIONS row 46, not in the ledger | Add the V46 line |
| 107 | B9 | Research is for the deliverables | N/A: Final Report | - | - |
| 108 | B9 | Don't discard ideas wantonly | N/A: process | As row 106 | - |
| 109 | B9 | Pitch not AI-squeezed; cut the human way | MET | Fixed: "Caplet XR doesn't invest the promise. Her first $300,000 buys it, in Treasuries maturing before each January." | - |
| 110 | B9 | No artificial timeline | N/A: process | - | - |
| 111 | B9 | Work more densely | N/A: process | - | - |
| 112 | B9 | No AI-use logging | N/A: process | - | - |
| 113 | B9 | No minute changes; big picture | N/A: process | - | - |
| 114 | B9 | Judges don't read for precision | N/A: process | - | - |
| 115 | B9 | Put message in the Bible | N/A: process | - | - |
| 116 | B10 | Diverse mock judges | N/A: process | Panel V46: tau 0.45; #1s LR3 ×5, S01 ×1 | - |
| 117 | B10 | Judges don't approve every change | N/A: process | Panel V46 puts V46 below V45 (3.83 v 3.17) | - |
| 118 | B10 | Judges don't think like Keel | N/A: process | - | - |
| 119 | B10 | Apply the voice studies | PARTLY | Applied: law 7 (a real confession); concession then "But"; long build, short landing ("We'd pay the $15,000."). Not applied: law 9 (seven kickers); law 6 (two frames); law 10 symmetry ("So we don't invest the promise. We buy it."; "every fall in stocks comes off the gift while every rise past the top goes to Laura", which reader 10 calls "a mirrored pair followed by an instruction") | C7 |
| 120 | B10 | Pitch reads as obvious AI | MET | Row 109 | - |
| 121 | B10 | GPTZero before Caplet | PARTLY | Not sent (VERSIONS row 46 doesn't say sent; V47 replaced it). Labelled "GPTZero: not yet checked" in VERSIONS only; D26 has no README to carry it | Add the README |
| 122 | B10 | "Human-written only" above 50% | MISSED | No score for the pitch or the IPS | A student pastes both into gptzero.me |
| 123 | B10 | Own voice matters more than the score | PARTLY | Row 119 | - |
| 124 | B10 | Use the human-vs-AI notes | PARTLY | The triad is gone (fixed). Still eight colons: "before we buy: it", "One leak remains: cash", "all of it: her floor", "has a catch: once", "made it first: our first plan", "typical year, it usually wins: counting", "runs itself down: each", "capsule: ten redemptions" | - |
| 125 | B10 | No sentences so compressed they barely make sense | PARTLY | Fixed: "once it's named". New: "promise the same $145,000 as us in a typical year"; "the worst twentieth of our futures for stocks in 2028-30" | E4, E7 |
| 126 | B10 | Natural variation and flair | MET | 32 sentences, 3 to 34 words | - |
| 127 | B10 | Judges don't fixate on single lines | N/A: process | - | - |
| 128 | B10 | Mark only to Wharton's guide | N/A: process | This check argues from section B | - |
| 129 | B10 | No "every team will" | MET | "the strongest rival" is a plan, not a team | - |
| 130 | B10 | No numbers plucked from thin air | MET | Every figure traces (D) | - |
| 131 | B10 | "We model", never "we judge" | MET | "Set in our model"; "our own model"; "our futures"; "we price"; no "we judge" | - |
| 132 | B10 | Stop obsessing over AI use | N/A: process | - | - |
| 133 | B10 | Drop "required trading activity" | MET | Not raised | - |
| 134 | B10 | Final by end of Wed 4 Nov | N/A: deadline | - | - |
| 135 | B10 | Overdrive | N/A: process | - | - |
| 136 | B10 | Demonstrate more work per day | N/A: process | - | - |
| 137 | B10 | Top 50 of 2,300; whatever it takes | N/A: process | - | - |
| 138 | B10 | Number one: extraordinary, not ordinary | PARTLY | Row 18 | - |
| 139 | B10 | Fresh commandments | N/A: process | - | - |
| 140 | B10 | Commandments must be followed | MISSED | No README and no filled ten-line check in D26; section C fails seven lines | Paste section C into a D26 README |
| 141 | B10 | Final IPS satisfies all expectations | PARTLY | This table | Section E |
| 142 | B10 | Recursive self-improvement | PARTLY | Regressed from MET. Taken from the V45 check: E5, E6 and C3; E1 is moot (its sentence was cut). Reversed: E2 asked to tie 97 to the range, and V46 cut the 97 instead. Not taken: E3, E4, X7 | E2 |
| 143 | B10 | Initiative, intellectual risks | PARTLY | It takes the hardest rival on (a real risk); no risk in strategy | - |
| 144 | B10 | Guess what Caplet will say | N/A: process | THINKING_LOG has no V46 entry (the last is "Sat 31 Oct, evening: V44 and V45") | Commandment X |
| 145 | B10 | Rewrite from scratch again | MET | V43 was rebuilt from voice-first draft A; V46 builds on it | - |
| 146 | B10 | List every idea of every version | N/A: process | No V46 line in IDEA_LEDGER (row 106) | - |
| 147 | B10 | Best ideas end up in the new IPS | PARTLY | In: the rival and its price, the confession, thoughtful risks, the leak, the catch + lock, the note. Out: 97 in 100, the priority order, ten one-year bills, 7.5%, any cheque-reliability figure, the sleeve's size, inflation. Panel V46 says the first two are exactly why it lost to LR3 | E2; X2, X3, X9 |
| 148 | B10 | Add the message to the Bible | N/A: process | - | - |
| 149 | B10b | Wharton's word with the utmost importance | PARTLY | Section B: the range's confidence, the evaluation of certainty and the assumptions are all missing in words or figures | E2; X1, X9 |
| W1 | W1 | Clear and creative thesis | PARTLY | Clear: "So we don't invest the promise. We buy it." Creative in framing more than structure | - |
| W2 | W1 | Disciplined planning across horizons and cash flows | MET | 2027 ladder; 2028 floor + fund; 2031 set-aside, range, lock; 2033 reserve | - |
| W3 | W1 | Appropriate diversification | PARTLY | Stocks: "one world index fund" only. J2 V46: "the equity exposure is small" | X3 |
| W4 | W1 | Consistent with IPS/TNA/WInS | MET | Treasury bonds + iBond funds, "Treasuries maturing late in 2032" (IBTM), one world fund (VT) | - |
| W5 | W1 | Tailored to circumstances, priorities, risk considerations | MET | "Laura has been willing to take thoughtful risks all her career, and the strongest rival takes one for her", then priced; her income in P4 | - |
| W6 | W1 | ... and residency goals | MET | "a gift towards the residency's building in Taiwan"; "a building priced in Taiwan dollars" | - |
| W7 | W1 | Thoughtful understanding of the client | MET | P4 (J3 V46) | - |
| W8 | W1 | Recommendations that can earn her confidence | MET | "The bottom is the floor she has owned since 2028." | - |
| W9 | W1 | Understanding and use of concepts and tools | PARTLY | Row 56 | X5 |
| W10 | W1 | Quantitative + qualitative | MET | A26's figures alongside the calendar argument | - |
| W11 | W1 | Reasonable assumptions and projections | MISSED | Regressed from PARTLY: V46 states **no** assumption. "with world stocks at 7.5% a year" went with the 60/40. Nothing on rates, inflation or the model (J6 V46: "states no return"; J1 V46: "most of the model detail" dropped). The $15,000 and the $90,000 depend on assumptions the reader never sees | X1; restore "with world stocks at 7.5% a year" |
| W12 | W1 | Evaluate reliability, facility, flexibility under varying outcomes | PARTLY | Regressed. Reliability: a list ("a list of ways to fail"), no figure. Facility: the bad tail ($140,000 v $90,000) and the good side ("every rise past the top goes to Laura"), but no confidence. Flexibility: "The other half stays hers" | E2; X9 |
| W13 | W1 | Articulation: teamwork, process, learning | PARTLY | "our first plan was three-quarters stocks, until our own model sank it" (J4 V46: "it shows the team changed its mind"). One sentence; no teamwork | FR |
| W14 | W1 | Compelling, organised narrative | MET | Promise → ladder → certainty → floor → range → catch → rival → reserve → name (reader 10: "plan, opponent, verdict ... the order of a market letter") | - |
| W15 | W1 | Authentic team voice | PARTLY | "we" ×7, "our" ×5; one real event; no detector check | - |
| W16 | W1 | Data used effectively | MET | "$15,000", "$90,000, where we promise $140,000" (J6 V46: "the clearest picture of selling low in any entry") | - |
| W17 | W1 | Original thinking, meaningful reflection | PARTLY | The reflection is real but one clause long | - |
| W18 | W1 | Contribution and uncertainty clear and credible to co-sponsors | PARTLY | The bottom is owned, the catch is explained, the lock closes it, and the bad tail is in dollars. But the case (:117) asks teams to "state how confident they are that her 2033 contribution will fall within that range", and V46 states no confidence at all (J3: "no stated confidence for the range"; J5, J6 the same) | E2 |
| W19 | W2 | Invest to support goals and cash flows while managing risk | MET | - | - |
| W20 | W2 | Reflect goals, horizons, liquidity, certainty, flexibility | MET | "each turns to cash before its cheque", "to sell any day" | - |
| W21 | W2 | Q: central idea | MET | "So we don't invest the promise. We buy it." | - |
| W22 | W2 | Q: principles | PARTLY | Regressed: the stated order ("the cheques come first, then the floor, then the hope") is cut. Left implicit: buy the promise; price the leak before naming; lock on naming day. J1, J2, J3 and J6 V46 all name the missing "what gives way first" | X2 |
| W23 | W2 | Q: balance growth, risk, liquidity, reliability, flexibility | PARTLY | The balance is argued in dollars (the $15,000 price) but growth's share is sized nowhere | X3 |
| W24 | W2 | Q: allocation changes as needs approach and payments are made | MET | 2028 floor; 2031 lock; 2033 "it runs itself down" | - |
| W25 | W2 | Q: protect the commitment, keep flexibility for the contribution | MET | P6-P7, P10 | - |
| W26 | W2 | Remember whom it serves | MET | - | - |
| W27 | W2 | Pitch: strategy, central idea, how it supports her goals | MET | "what's left buys world stocks for the gift" | - |
| W28 | W2 | IPS: risk and return | PARTLY | Regressed: risk is listed and the rival's extra return is priced ($15,000), but no expected return is stated for anything | Restore 7.5% (X1 note) |
| W29 | W2 | IPS: construction and diversification | PARTLY | W3, W23 | X3 |
| W30 | W2 | IPS: reserve composition over time | MET | "the ten holdings are the operating reserve, and it runs itself down" | - |
| W31 | W2 | IPS: responsible facility contribution | MET | Bottom = floor; top = floor + half the stocks; the other half kept | - |
| W32 | W2 | IPS: appropriate flexibility | MET | "to sell any day if a building priced in Taiwan dollars comes in dearer" | - |
| W33 | W2 | Framework, not individual investments | MET | - | - |
| W34 | W2 | No final reserve sums, projections, final range | MET | $145,000 and $140,000 are model medians used to compare rules, not a recommended range | - |
| W35 | W2 | No citations, charts, links | MET | - | - |
| W36 | W2 | Strategy can't be revised | MET | Dated rules | - |
| W37 | W3 | Reasoning, assumptions, trade-offs | PARTLY | Reasoning and trade-off strong ("We'd pay the $15,000"); assumptions: none (W11) | X1 |
| W38 | W3 | Cohesive across market outcomes | MET | - | - |
| W39 | W3 | Planned adjustments, not rewritten when markets move | MET | Dated adjustments; "it runs itself down" | - |
| W40 | W4 | Strategy leads across deliverables | MET | - | - |
| W41 | W4 | Know your client | MET | - | - |
| W42 | W4 | Use WInS to demonstrate | N/A: WInS/FR | - | - |
| W43 | W4 | Don't focus on performance | MET | - | - |
| W44 | W4 | Explain why each investment belongs | PARTLY | Treasuries and the world fund are explained. Why Treasury funds as well as bonds isn't | FR |
| W45 | W4 | Follow the instructions | MISSED | Regressed from PARTLY. Three explicit case instructions now have no answer on the page: "state how confident they are that her 2033 contribution will fall within that range" (:117); "explain how they evaluated that level of certainty" (:97-98, a definition by list, no evaluation); "the effect of inflation on portfolio projections" among the assumptions (:147) | E2; X9; X1 |
| W46 | W5 | Only WInS stocks, ETFs, Treasuries | MET | The note and option are a foil only. "our futures" (D) should not be left to read as futures contracts | E7 |
| W47 | W6 | "Responsibly contribute"; keep flexibility | MET | "The other half stays hers" | - |
| W48 | W6 | "Willing to take thoughtful risks" | MET | "Laura has been willing to take thoughtful risks all her career" (the case's words, unquoted) | - |
| W49 | W6 | 2028 deposit from advances, speaking, licensing | MET | "shrinks the advances, speaking and licensing behind the 2028 deposit" | - |

## B. Wharton's word, item by item (`WHARTON_WORD.md`)

| # | Source | Item | V46 status | Evidence | Fix |
|---|---|---|---|---|---|
| Q1 | IPS question | Central idea | MET | "So we don't invest the promise. We buy it." | - |
| Q2 | IPS question | Guiding principles | PARTLY | W22: the stated priority order is cut; four of six judges miss it | X2 |
| Q3 | IPS question | Balance growth, risk, liquidity, reliability, flexibility | PARTLY | Growth's price is stated ($15,000), its share never; reliability has no figure | X3, X9 |
| Q4 | IPS question | Allocation change as needs approach and payments are made | MET | 2027 → 2028 → 2031 → 2033 | - |
| Q5 | IPS question | Protect the commitment while keeping flexibility for the contribution | MET | P6-P7, P10 | - |
| Q6 | IPS instruction | Remember whom it serves | MET | - | - |
| M1 | Make it clear | What we're trying to accomplish | MET | P1 | - |
| M2 | Make it clear | Why it's appropriate for the client | MET | Thoughtful risks answered with a priced rival; her income (P4) | - |
| M3 | Make it clear | How it balances the five | PARTLY | As Q3 | X3 |
| M4 | Make it clear | How it guides construction and decisions as needs change | MET | Dated rules; the lock on naming day | - |
| M5 | Make it clear | Protect payments while supporting a responsible contribution | MET | The ladder; "the floor she has owned since 2028" | - |
| P | Pitch | Summarise; central idea; how it supports goals and funding needs | MET | The promise bought; the 2028 floor; "what's left buys world stocks for the gift". (The missing "nearly" is in D) | - |
| I1 | IPS para | Tailored to goals, horizons, needs | MET | - | - |
| I2 | IPS para | Risk and return | PARTLY | W28: no expected return is stated | X1 note |
| I3 | IPS para | Liquidity | MET | "each turns to cash before its cheque"; "to sell any day" | - |
| I4 | IPS para | Construction and diversification | PARTLY | W3, W23 | X3 |
| I5 | IPS para | Planned changes as needs approach | MET | - | - |
| I6 | IPS para | Prepare for the operating commitment; reserve composition | MET | P3, P10 | - |
| I7 | IPS para | Responsible facility contribution; flexibility | MET | P6 | - |
| J1 | Guide | Reasoning, assumptions, trade-offs | PARTLY | W37: no assumptions | X1 |
| J2 | Guide | Cohesive across outcomes | MET | - | - |
| J3 | Guide | Not rewritten because markets move | MET | Dated rules; "Do not crush." | - |
| C1 | Criterion | Investment Strategy | PARTLY | Clear thesis, disciplined dates, consistent; diversification implied only; the principles' order is gone | X2, X3 |
| C2 | Criterion | Client Knowledge and Objectives | MET | Thoughtful risks, her income, Taiwan dollars, the kept half | - |
| C3 | Criterion | Portfolio Analysis | PARTLY | Regressed: no reliability figure, no range confidence, no assumption. The one analysis left (A26) is strong but is a mean presented as typical, plus a chosen tail (D) | E1, E2; X1, X9 |
| C4 | Criterion | Articulation of Competition Experience | PARTLY | One real, dated decision ("until our own model sank it"); the FR carries the rest | FR |
| C5 | Criterion | Creativity and Presentation | PARTLY | Strong landings ("We'd pay the $15,000."). Against: a floating heading (J5), the misattached tail (reader 10), seven kickers, no confidence statement for the range | E2, C7 |
| A1 | Advice | Let strategy lead | MET | - | - |
| A2 | Advice | Know your client | MET | - | - |
| A3 | Advice | Use WInS to demonstrate | N/A: WInS/FR | - | - |
| A4 | Advice | Not about performance | MET | - | - |
| A5 | Advice | Explain why each investment belongs | PARTLY | W44 | FR |
| A6 | Advice | Follow the instructions | MISSED | W45: "state how confident", "explain how they evaluated", inflation | E2; X9; X1 |
| H | Hard limit | Permitted instruments only | MET | Treasury bonds, Treasury funds, one world index fund; no TIPS, STRIPS or options (the bank's option is a foil) | - |

## C. The Ten Commandments (ready to paste into a `D26/README.md`, which doesn't exist yet)

- **I. Extraordinary: FAIL.** The three ideas a judge would retell are the recession that hits both the ladder's price and the 2028 deposit (J3), the capped range's catch and the lock, and the rival that "usually wins" by $15,000 but can promise only $90,000 in a bad run (J1, J2, J6). The best of them is the rival's price, but it's a comparison, not our idea. All three sit on the field's default skeleton (ladder + stocks + lock). The one line that wasn't the default, "ten one-year bills", is cut. Panel V46: 3.83, fourth of six.
- **II. Wharton only: PASS.** Panel V46's judges score on the five criteria, and this check argues from section B. The gaps that matter are W11, W12, W18 and W45.
- **III. Write like us: FAIL.** There's no README, so no moves are quoted, which is the test. The moves are present: a concession + "But" ("it usually wins ... But "usually" is the whole trick."); a build and a landing ("... printed years in advance. We'd pay the $15,000."); a wry line ("the strongest rival takes one for her"); a real event ("our first plan was three-quarters stocks, until our own model sank it"). The triad is gone (fixed). Against: seven kickers, eight colons, and reader 10's "the caption of a chart" for the rival's set-up.
- **IV. Clear on one reading: FAIL.** "– selling low, on a timetable printed years in advance" trails "where we promise $140,000", so on a literal read we are the ones selling low (reader 10). "In a typical year" (there is one naming day). "The worst twentieth of our futures" (model-speak, and "futures" is also an instrument). The floor is "all of" the 2028 deposit, yet "we promise $145,000" and then $140,000, with nothing to bridge them. The heading floats at 70% of the page (J5: it "breaks the read"). "Do not crush." (J3, on the shared close).
- **V. Every number explains itself: FAIL, on one figure.** The test is "says what it is and where it came from, in its own sentence". "$15,000" says where it came from ("in our model") but not what it is: it's an average, set right after "usually wins", and the median is about $10,000. "The worst twentieth of our futures" never says "modelled". Every other figure passes.
- **VI. GPTZero before Caplet: FAIL, and it can't be met here.** No score. The "not yet checked" label is in VERSIONS row 46 only, and D26 has no README for it. No agent stood in for a detector.
- **VII. Few ideas at full size: PASS.** J3 V46 retold it in effect: the 2027 money buys the ladder; most of the 2028 deposit buys Treasuries that grow back to the full deposit, with only the expected interest in stocks; in 2031 the range runs from that owned floor to the floor plus half the stocks, the leak is priced first, and the promised half is locked in Treasuries.
- **VIII. Lose no idea; critique every borrowed one: FAIL.** The critique half holds: the rival is critiqued with its price and its tail, and the note has its blind spot ("can't expire worthless"). But the test is "each new draft is checked against the ledger", and IDEA_LEDGER has no V46 line. Six ideas left the IPS (the 60/40 price, "one in three / under one in sixty", "ten one-year bills", "97 in 100", the priority triad, "7.5%") with their landing place recorded only in room files and VERSIONS.
- **IX. Judges who disagree: PASS, narrowly.** Panel V46: six judges on four models, mean Kendall tau 0.45, each with reasons in their own file. It's narrow because five of six #1 picks are the same (LR3), the closest agreement of any recent panel. On the commandment's own words ("a panel that agrees in substance is rebuilt"), the next panel should check this isn't a herd.
- **X. Improve without being asked: FAIL.** THINKING_LOG has no V46 entry. Of the V45 check's fixes, three were taken (E5, E6, C3), one was reversed (E2 asked to tie the 97 to the range, and V46 cut it), and three weren't taken (E3, E4, X7).

## E. The misses, ranked by what a Wharton judge would notice, with exact fixes

**Package A (recommended): E1 + E2 + E4 + E5 + E7, paid for by cut C7.** I applied it to V46's full text and measured it with `textcheck.py`: **IPS 497 strict (495 by spaces); pitch unchanged at 50.** Each change, applied alone to V46 and measured, has these deltas: E1 +2, E2 +10, E4 0, E5 +1, E7 0, C7 −13 (heading −4, payoff −9), which nets to 0. The assembled text was used only to prove the count. It has had no GPTZero check, cold read or panel. (V47 in `../D27/` already carries E1's "on average" and the 97, in LR3's wording. E4, E5, E7 and X3 apply to V47 too.)

1. **No confidence for the range (W18, W45, A6, C3; case :117; J2, J3, J4, J5, J6 V46).** *E2:* "On the day she names it, the half she promised moves into Treasuries." → "From naming day the promised half sits in Treasuries, and in our model the gift reaches its top about 97 times in 100." (**+10**. L-13 slide, 96.0-97.9% across four worlds. The bottom is broken 0 times in 200,000 in S0, so the gift stays inside the range.)
2. **"$15,000" reads as the typical win, but it's the average (Commandment V, row 76).** *E1:* "it leaves her about $15,000 more by 2042." → "it leaves her about $15,000 more on average by 2042." (**+2**. The A26 mean is $13.7-16.6k; the median is $9.3-11.8k, from my read-only rerun.)
3. **The "selling low" tail attaches to us, and the heading floats (Commandment IV; J5, reader 10).** *C7, the cut that pays (a whole idea, not a squeeze):* cut the heading "Sell low, by appointment" and its payoff "– selling low, on a timetable printed years in advance", so P9 ends "where we promise $140,000." (**−13**.) The picture C-04 called the paragraph's most important (the rival's sale on a date fixed years ahead) survives in P8's "buys its bottom in January 2031 with whatever those stocks fetch that morning". The cost: V46 has no heading (reader 10 marks LR3 down for exactly that), and it loses a voice line readers 9 and 10 both liked. It goes to the FR with "ten one-year bills" as the sequence-of-sales section.
4. **"In a typical year" (Commandment IV, D).** *E4:* "as us in a typical year" → "as us in a typical future" (**0**).
5. **The set-aside is mostly from her half, not the hope (row 76; L-13 line 29; LR-08 s3).** *E5:* "set it aside from the hope, before she names any gift" → "set it aside from what she keeps, before she names any gift" (**+1**). Note: this makes P6's "The other half stays hers, to sell any day" a little less absolute. That's true to the model, where her half pays the leak first in about 72% of paths.
6. **"Our futures" (Commandment V; W46).** *E7:* "In the worst twentieth of our futures" → "In the worst twentieth of modelled futures" (**0**).

**Package B (if the team keeps the heading): E1 + E2 + E3 + E4 + E5 + E7, paid for by cut C6, measured: IPS 494 strict (492 by spaces).** *E3* (+1) reattaches the tail: "the rival can promise co-sponsors only about $90,000, where we promise $140,000 – selling low, on a timetable printed years in advance." → "the rival is selling low, on a timetable printed years in advance, and can promise co-sponsors only about $90,000. We promise $140,000." *C6* (−17): cut "Laura has been willing to take thoughtful risks all her career, and the strongest rival takes one for her." and start the next sentence "The strongest rival keeps our ladder, ...". It isn't recommended, because it costs W48 (the case's own words on her risk appetite, Client Knowledge) and reader 10's favourite line. That's a Wharton criterion paid to keep a voice line, which inverts the order Book 10 sets.

**Not bought (no words left; each is first in line if a cut above is rejected or another accepted; all measured alone on V46):**
7. **X9, no evaluated certainty for the cheques (W12, W45; case :97-98).** "The US government defaults." → "The US government defaults. Short of that, in our model a cheque falls over $1,000 short about three times in 10,000." (**+17**. L-13/L-14 XR 0.03%, S0 and S1. The Window's caution stands: the model has no default in it, hence "Short of that".)
8. **X2, the priority order (W22, Q2; J1, J2, J3, J6 V46).** After "each turns to cash before its cheque.": "If anything goes wrong, the hope gives way to the floor, and the floor to the cheques." (**+17**. It isn't a triad, so Commandment III holds.)
9. **X1, no assumptions (W11, W28, J1).** "Inflation can't make a fixed cheque cost more." after "one rung falling due before each January." (**+8**.) With it, put back the return basis: "with world stocks at 7.5% a year" in the "Set in our model ..." sentence (about +7, not measured).
10. **X3, the stock sleeve never sized (W3, W23, I4; J2 V46).** "buys one world index fund." → "buys one world index fund, about a fifteenth of the portfolio in our model." (**+9**. L-14 now gives the run: 6.6%, one in 15.1, S0 and S1.)
11. **X8, "the gap" (P4) needs a referent.** "behind the 2028 deposit that must cover the gap." → "behind the 2028 deposit, just when it must cover any shortfall in the ladder." (**+5**.)
12. **The worst-twentieth slice (row 76; L-14, LR-08 rulings).** Keep it only with the Courtroom's ruling recorded against both rooms' rules, or swap it for LR-08's unsliced pair ("under $100,000 about one time in thirteen ... ours, about one in 150"). That pair is on the Model Suite engine with the mark, not yet on L-13's chain, so it needs a run on V46's design first.
13. **Pitch "nearly" (D).** "Her first $300,000 buys it, in Treasuries" → "Her first $300,000 buys it, or nearly, in Treasuries" (**+2**; the pitch would be 52). It needs a 2-word cut in the pitch, so it isn't bought.
14. **Process (costs no words; Commandments III, VI, VIII, X; rows 106, 121, 140, 144).** Write `D26/README.md` with the quoted voice moves, the numbers table and section C as its ten-line check, labelled "AI DRAFT, Claude; GPTZero: not yet checked". Add a V46 line to IDEA_LEDGER (the six ideas cut and where each lands). Add a V46 "what Caplet would say" entry to THINKING_LOG. A student gets a GPTZero score.
