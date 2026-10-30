# BIBLE AUDIT, 30 Oct 2026. AI-generated (Claude Code), not for submission.

**Scope.** Every expectation in `../BIBLE.md` (cover note, Books 1-5, 9, 10, the 18:21 note on Wharton) and in
`../WHARTON_WORD.md` (which outranks the Bible), checked against Keel's current work. The draft audited is **V32
(`drafts/D12/`, pitch 50/50, IPS 500/500 strict, margin 0)**, as asked. While this audit ran, **V33 (`drafts/D13/`)**
was committed (8d36e68, 07:59 UTC). Its own cold read (`drafts/D13/COLD_READ.md`) **fails Commandments IV, V, VI and
VIII**, so V33 can't go to Caplet either. Where V33 already fixes a D12 gap, the row says so ("D13: fixed").

**How it was judged.** I read the draft as a Wharton judge would, then checked it against the idea ledger and bank, the
voice guide, the commandments check, both blind panels (`judges/panel_V31/`, `judges/panel_V32/`, each judge's own
notes), `DETECTOR_LOG.md`, `INSTRUCTIONS.md`, `VERSIONS.md` and `THINKING_LOG.md`. I also ran a few counts on D12:

| D12 IPS | Count |
|---|---|
| "liquidity"/"liquid", "flexibility", "diversify"/"diversification", "growth", "principle", "Taiwan", "inflation" | **0 each** (D13: 0 each) |
| "we" | **1** (D13: 6) |
| colons / spaced en dashes / sentences opening "So" | **11 / 0 / 3** (D13: 5 / 8 / 3) |
| numbers other than years | about 10 (voice guide s4 allows six in the whole form) |

The headline finding, plainly: **Keel has written the rules down and has mostly not applied them.** The commandments
check is an empty template. No draft has ever been through GPTZero. The register of instructions stops at Book 9. Three
of Wharton's five balance words never appear in the IPS. The motif and the knowledge are thinner on the page than in
the research.

Status key: **MET** · **PARTLY** · **NOT MET** · **N/A now** (superseded, or due later: the Final Report is due Sat 5 Dec).
Short labels: CN = cover note (26 Oct); B1-B10 = the books; B10b = Caplet's 18:21 note on Wharton (30 Oct);
W = `WHARTON_WORD.md` sections 1-6; FR = Final Report.

## 1. Every expectation, checked

| # | Book | Expectation (short quote or close paraphrase) | Applies to | Status | Evidence | Fix needed |
|---|---|---|---|---|---|---|
| 1 | CN | Rewriting "should not have been this fast"; a long process of thinking, ideation, research, analysis | process | PARTLY | Research waves R02-R11 and 91 idea-bank rows are real. But V31 and V32 were both written on 30 Oct, and D12's ips.txt is timestamped 07:41 UTC, about 12 minutes after D11's (07:29) | Before writing each new version, log in THINKING_LOG what new thinking justifies it |
| 2 | CN | "THINK ... I don't want you to be hasty. That's the worst mistake" | process | PARTLY | V32 was tuned to panel 1's reasons and judged by the same six personas within the hour. That is haste dressed as rigour | One round a session: draft, cold read, panel, then stop and write what was learned |
| 3 | CN | Creativity, originality, novelty, knowledge, insight, an "evidently widely-read" IPS | IPS | PARTLY | Panel 2, J3: "a ladder alone separates nobody"; J1 couldn't tell V31 from V32 | Gaps 1, 12 and 15 below |
| 4 | CN | All Bibles equal; Keel may weigh them but must grasp the intent | process | PARTLY | `INSTRUCTIONS.md` header still says "eight books"; Book 10 has no row | Add the Book 10 rows (Process gap P5) |
| 5 | CN | Keel has autonomy; may question Caplet; neither side always defers | process | MET | `voice/01_digest_ahaan.md` s3; panel 1 summary "Not taken: J2's 80% stocks" | - |
| 6 | CN | "I don't care how you ... disseminate it ... as long as our expectations are met" | process | PARTLY | This audit is the first full item-by-item check since BIBLE_TRACE (27 Oct, 41 rows, Books 1-7 only) | Re-run this audit on every candidate draft |
| 7 | B1 | A "genuinely distinctive team voice" | IPS, FR | PARTLY | D12 has "we" once and reads as a third-person spec. Panel 2, J6: "creative voice a little less distinctive than the best of the rest" | Gap 7; write the whole IPS in the first-person plural |
| 8 | B1 | The voice "must carry throughout" | IPS, pitch, FR | PARTLY | Pitch and IPS open with the same mirrored line ("one promise ... one hope"), so it reads as a refrain, not a voice | Gap 11 |
| 9 | B1 | "Sound unique ... quite unlike any other team" | IPS | PARTLY | "One promise, one hope" is the shape of the simulated default rival A09 (ledger A1: "A09-style rivals") | Gap 11 (drop the mirrored opener) |
| 10 | B1 | "Cerebral yet witty" | IPS | PARTLY | Cerebral: yes. Witty: one line ("minus the bank and its fee") | Keep one wry line; don't add jokes |
| 11 | B1 | "Passionate yet thoughtful" | IPS | PARTLY | "The boldest bet of her life" is the only line that cares. Who the residency serves never appears | Optional if words free up; FR otherwise (voice guide s7, F2) |
| 12 | B1 | "Insightful yet confident" | IPS | MET | No hedging; certainty defined by where it breaks (all six panel-2 judges praised it) | - |
| 13 | B1 | Work judges "can honestly ENJOY reading" | IPS | PARTLY | Panel 2: "reads cleanly" (J2), "the pill opening is still a conceit" (J4) | Gaps 8, 12, 13 |
| 14 | B1 | One unifying extended metaphor/motif across the IPS and FR | IPS, FR | PARTLY | XR shows up in paragraphs 2, 3 and 9 only; the gift and range half (paragraphs 5-8) has no motif | Gap 12; FR: the package-insert structure (`voice/07_ideas_from_reading.md` I-2) |
| 15 | B1 | Ideally "elaborate and vast", tying back almost every corner | FR | N/A now | Tempered by Book 2 for the IPS; the FR is not started (instructions out Tue 10 Nov) | FR plan: every section heading a dose rule |
| 16 | B1 | It's an investing competition: intellect and knowledge before language | IPS | PARTLY | The investing ideas are good but mostly unnamed (row 56) | Gap 15 |
| 17 | B1 | Both intellect and language together "couldn't do any harm" | IPS | PARTLY | - | Gaps 12, 15 |
| 18 | B1 | "Truly extraordinary ... not just another great competent team" | IPS | NOT MET | Book 10 called V29 "ordinary". Panel 2 sees V32 as the "same safe core as Entries 1, 4 and 6" (J2) | Gaps 1, 12, 15: show the two ahas the field lacks |
| 19 | B1 | Something "no one else would do or think to do (not even ... teams using AI)" | IPS | PARTLY | Human capital and the bank-free note are rare (0 of 36 rivals had human capital, THINKING_LOG 28 Oct). The 2031 lock is the crowd's default (9 of 12 rivals) | Lead with what is rare; keep the lock short (D12 does) |
| 20 | B1 | An "aha"; "insights which make us seem like geniuses" | IPS | PARTLY | The one idea panel-2 J5 counted among "what I learned", one liability borrower on purpose (ledger B6), was cut from V31 and V32 | Gap 1 |
| 21 | B1 | Keep these "in your back pocket" and apply them | process | MET | `NORTH_STARS.md`, the commandments | - |
| 22 | B2 | "Root and branch" needn't be final; the name must be unique | IPS | MET | Caplet XR | - |
| 23 | B2 | No roots-themed name (AI groupthink) | IPS | MET | D12 has no root, branch or tree words | - |
| 24 | B2 | Name "deeply specific to our extended metaphor / motif" | IPS | MET | XR = extended release | - |
| 25 | B2 | Name clearly fits the strategy, not a stretch | IPS | MET | X = ten cheques; R = redemption | - |
| 26 | B2 | Motif not in every sentence; "a tool ... not a crutch that wastes word count" | IPS | MET | Three places | - |
| 27 | B2 | Subtle, but not "decorative or layered on top as a frantic last-minute addition" | IPS | PARTLY | "(do not crush)" is a bare two-word parenthesis that no judge can decode. That is layering on | Gap 12 |
| 28 | B2 | The motif adds "a thoughtful layer ... almost transcendent"; it "will help to build our narrative arc" | IPS, FR | NOT MET | No arc: the pill appears, the name is explained, then the motif vanishes until a parenthesis at the end | Gap 12 (call it back once in the reserve paragraph, with its meaning) |
| 29 | B2 | AI over-uses metaphors, so be subtle; "write like WE write" | IPS | PARTLY | D12 mixes pill, ladder, leak, floor and "plugs any gap". Voice guide law 6: "One image per piece ... nothing competes with it" | Gap 12; drop "leak" or the pill, not both |
| 30 | B2 | A name "which only our team could have ... could not apply to any other" | IPS | MET | - | - |
| 31 | B2 | Relevant to the client, but "optimise for OURSELVES first" | IPS | MET | - | - |
| 32 | B2 | Motif "genuinely creative. Unexpected. Insightful" ("huh, that's an interesting way of putting it") | IPS | PARTLY | The pharmacology ladder is the road less taken (digest row 7: met). On the page it shrinks to a simile | Gap 12 |
| 33 | B2 | "Find unexpected connections, synergies, analogies, syntheses" | IPS, FR | PARTLY | IDEA_BANK has 91 rows (Chile, Alaska, IPO ranges, the donor study, Ulysses contracts ...). The IPS shows about three | Gap 15; the FR carries the rest with citations |
| 34 | B2 | "Above all ... sound deeply human" | IPS, FR | NOT MET (unverified) | Never checked by any real detector; colon-chained, aphoristic paragraphs (11 colons) | Gap 13; Process gap P1 |
| 35 | B2 | "Lean ... but ... like real, messy human writing" | IPS | PARTLY | Every paragraph ends on a tidy closer (at least six kickers; voice guide law 9 allows three) | Gap 13: end three paragraphs on a plain fact or decision |
| 36 | B2 | When cutting, don't "just rearrange words so they're more concise" | IPS | PARTLY | V31 dropped whole ideas (ledger). V32 squeezed new ones in: "yields fall two points before we buy and her 2028 deposit more than halves" (J4 had to read it twice) | Gaps 9, 3 |
| 37 | B2 | "Parsimonious and lucid"; no fluff | IPS | MET | - | - |
| 38 | B2 | Do light analysis of Ahaan's essays vs your own writing | process | MET | `research/R03_voice_study.md`, `voice/01-06` | - |
| 39 | B2 | Agents' "humanising" failed; detectors said 100% AI; AI-ness "transcends ... a neat list" | process | PARTLY | Ban lists retired (voice guide s6). No detector run since (row 101) | Process gap P1 |
| 40 | B2 | "Try to write more like me"; the essays' voice as "a direct inspiration" | IPS | PARTLY | No file shows which of Ahaan's moves D12 uses. D12 has no en dash, no long build of over 36 words, and one concession-then-"but" | Gap 13; quote each move in the draft README (Commandment III test) |
| 41 | B2 | Not every aspect of the essays applies; use them as tone | process | MET | Voice guide s0 | - |
| 42 | B3 | Caplet XR is "exceptionally clever"; it justifies the team name | IPS | MET | - | - |
| 43 | B3 | Extend it: "releases at a certain time, do not crush"; more dimensions | IPS, FR | PARTLY | IPS: same dose on schedule (yes), do not crush (unexplained). FR bank: coated beads, Contac 600, 80-125% bioequivalence, blister pack (#29-31, #90) | Gap 12; FR gets the rest |
| 44 | B3 | "ANOTHER potential meaning of the acronym XR" | IPS | MET | X for ten, R for redemption | - |
| 45 | B3 | "Extended response" as the motif's meaning | - | N/A now | Superseded by Book 5 (extended release + X = 10) | - |
| 46 | B3 | Label it, in the intro or conclusion, as something that sounds like a real investing plan | IPS | PARTLY | "Caplet XR" already reads as a product; no product-tier flourish (ledger A6 -> FR) | Optional; FR |
| 47 | B3 | Free to change the name or motif | - | N/A now | Locked in Book 5 | - |
| 48 | B3 | Stop the over-claim obsession; "We want FLAIR. We want VOICE" | IPS | PARTLY | No hedging (good); not much flair either | Gap 13 |
| 49 | B3 | Don't ACTIVELY over-claim | IPS | PARTLY | "anyone owing a fixed amount must sell at the bottom of a crash" is too general. "Ten one-year bills" is wrong: the cheques are 6-15 years away | Gap 8 |
| 50 | B3 | Judges aren't mini-Lauras; they hunt the best investing knowledge and strategy | IPS, process | PARTLY | The panel design is right. The IPS still hides its knowledge (row 56) | Gap 15 |
| 51 | B3 | Don't waste time on grammar, punctuation, spelling | process | MET | No word-policing gates | - |
| 52 | B3 | "En dashes are correct in Australia and we're going to use them" | IPS | NOT MET | D12 has 0 en dashes and uses colons in their place (D13: 8 en dashes, fixed). Note: a spaced dash counts as a word in textcheck | Gap 13 |
| 53 | B3 | "Marinate, ruminate"; apply these to the IPS and FR | process | MET | - | - |
| 54 | B4 | Rewrite from scratch; "I want to see them all implemented" | IPS | PARTLY | V31 is a fresh rewrite (met). "All implemented" is not: see this table | Top 15 |
| 55 | B4 | Stop tinkering on the flawed old version | process | MET | v4.1 abandoned 26 Oct | - |
| 56 | B4 | North star 4: "truly extraordinary knowledge of investing concepts and strategies" | IPS | PARTLY | Concepts used but unnamed: sequence risk, human capital, reinvestment risk, cash-flow matching, pull-to-par, the payoff of a capped call. Only "capital-protected note" is named | Gap 15 |
| 57 | B4 | No rapid name-dropping | IPS | MET | - | - |
| 58 | B4 | Apply and explain "a wide range ... including potentially niche ones" | IPS | PARTLY | Niche on the page: the protected note, human capital, the cap's asymmetry. The niche research (donor study, the 1923 replay M8, the IPO-range rule) sits in the bank | Gap 15; Gap 14 (FR) |
| 59 | B4 | Research used uncited in the IPS, cited in the FR | IPS, FR | PARTLY | Several R11 figures are "LISTED (title seen, page not read)" | Verify every R11 figure before the FR quotes it |
| 60 | B4 | FR shows "stunning wide reading" | FR | N/A now | The reading log holds 165 pieces; the citation list isn't built | Start the Works Cited bank from IDEA_BANK sources now |
| 61 | B4 | Knowledge must support, not undercut, the narrative and a clear tailored strategy | IPS | MET | - | - |
| 62 | B4 | North star 4 equal, neither first nor minimised | process | PARTLY | It is the least visible on the page | Gap 15 |
| 63 | B4 | "A long process of research and discovery and deep, deep thought" | process | PARTLY | See row 1 | - |
| 64 | B4 | "Something dazzling ... by 6 November" | IPS | N/A now | Due: final draft for review end of Wed 4 Nov | - |
| 65 | B5 | "Caplet XR is a brilliant name; let's stick with it" | IPS | MET | - | - |
| 66 | B5 | Mention the literal "extended-release" meaning | IPS | MET | Paragraph 2 | - |
| 67 | B5 | Ahaan's instinct: both meanings of XR in the IPS | IPS | MET | Paragraphs 2-3 | - |
| 68 | B5 | At least "the bare bones of the extended metaphor motif" in the IPS | IPS | MET | - | - |
| 69 | B5 | "Everything out by the Final Report" | FR | N/A now | Bank rows 26-31, 90 | FR |
| 70 | B5 | "Make it clear that we've got a clever and thought-out name" | IPS | PARTLY | "R for redemption" is never tied to anything. The cold reader of D13: "redemption is never connected to anything later" | Gap 12 (one clause: the Treasury redeems each bond just before its cheque) |
| 71 | B5 | X = 10, "definitely keep this meaning" | IPS | MET | - | - |
| 72 | B5 | R must not be "release"; find something clever | IPS | MET | Redemption | - |
| 73 | B5 | Stop fretting over "words that make something sound surer than it is" | IPS | MET | "a cheque can fail only if ..." | - |
| 74 | B5 | iBonds are as close to exact sums on exact dates as it gets | IPS | MET | "each maturing before its January" | - |
| 75 | B5 | You may call iBonds "near-ironclad"; any T-bond distinction concise | IPS | MET (optional) | Not used (ledger B8 -> FR); no hedging | - |
| 76 | B5 | "Accuracy is important" | IPS | PARTLY | D12's break point ("more than halves") is wrong: the corrected break is a deposit under about $85,000 (D13 commit, Lab K07). "Ten one-year bills" is inaccurate | Gaps 8, 9 |
| 77 | B5 | "Allow a bit of human flair to slide in" | IPS | PARTLY | - | Gap 13 |
| 78 | B5 | Hedging is "a classic habit of AI"; avoid it | IPS | MET | - | - |
| 79 | B5 | Test against Ahaan's essays and his rewritten TNA, not only Orwell | process | NOT MET | No voice read is filed for D11 or D12; D13's cold read "did not read ... the voice guide" | Process gap P3 |
| 80 | B5 | "Actually use my voice ... rather than your generic and frankly annoyingly robotic AI voice" | IPS | NOT MET (unverified) | Book 10 says V29 failed; D12 isn't shown to be different in kind | Gap 13; Process gaps P1 and P3 |
| 81 | B5 | IPS and FR "truly, exceptionally, stunningly ... extraordinary" | IPS, FR | NOT MET | See row 18 | Top 15 |
| 82 | B5 | "Distinctive ... unexpected ... erudite and clever" | IPS | PARTLY | - | Gaps 1, 12, 15 |
| 83 | B5 | A final version for review by Sat 31 Oct | process | N/A now | Moved to end of Wed 4 Nov (Book 10). `ips_rewrite/README.md` plan still says Sat 31 Oct and `drafts/D5/` | Update the README plan (P9) |
| 84 | B5 | "Meet EVERY SINGLE EXPECTATION ... Blow us away" | all | PARTLY | This table | Top 15 + process gaps |
| 85 | B9 | The IPS meets all Wharton's requirements; it has "a VERY specific and defined job" | IPS | PARTLY | Liquidity, flexibility, diversification and principles are never named (rows W12-W30) | Gaps 1, 4, 5, 6 |
| 86 | B9 | Stop focusing on formatting | process | MET | - | - |
| 87 | B9 | Judges must see us as "INTELLIGENT and KNOWLEDGEABLE" | IPS | PARTLY | - | Gap 15 |
| 88 | B9 | Search the world for niche concepts; a unique case needs a unique strategy | process | MET | R02, R05, R07 (40 ideas), R11 (22 concepts), bank rows 83-91 on 30 Oct | - |
| 89 | B9 | Fuse niche strategies; "We need SYNERGIES" | IPS | PARTLY | On the page: XR + sequence risk; the protected note + an index fund; human capital + the deposit order. Fused in research, mostly invisible in the text | Gap 15 |
| 90 | B9 | Dig "from the most unexpected places" | process | MET | Lighting consoles, NEWS2, Alaska, the hui organiser, Mega Millions (bank) | - |
| 91 | B9 | Don't dump uncritically: "Analyse them. Evaluate them. Critique them" (IPS too) | IPS | PARTLY | Critiques the note ("the price is a smaller boom") and the 60/40 | Keep both; Gap 3 makes the 60/40 critique readable |
| 92 | B9 | Show one that "might initially seem relevant ... but really it's not, and here's why" | IPS | PARTLY | The 60/40 line is the one example, and four of six panel-2 judges couldn't tell which promise it breaks | Gap 3 |
| 93 | B9 | Prove what we know of existing strategies, "including those which 99.9% ... don't know" | IPS | PARTLY | - | Gap 15 |
| 94 | B9 | Create "our OWN strategy, unique to OUR client" | IPS | MET | Human capital and the deposit order are client-specific (J3 and J5 called it the best client reasoning) | - |
| 95 | B9 | LOGIC: analogies, thought experiments, causal chains to their "logical conclusion" | IPS | PARTLY | One good chain (cap -> asymmetry -> lock). The thought experiment (wipe out every share) was cut as false in a few paths; its true form ("the shares can help a cheque, never hurt one") was never used | Optional; see Gap 8 |
| 96 | B9 | Case studies, evidence, studies, facts and figures | IPS | PARTLY | No case study or study is visible. M8 (the 1923 start: stocks win and the cheques still bounce) is built for one clause and unused | Gap 8 offers M8 as the alternative |
| 97 | B9 | The essays are tone, "not gospel"; voice is "fundamentally qualitative" | process | MET | `fingerprint.py` retired as a gate | - |
| 98 | B9 | Use the Wall Street writers as well as his essays | process | PARTLY | In the guide (s0); no draft README shows it | Process gap P3 |
| 99 | B9 | Don't use Keel's own agents as AI detectors | process | MET | Commandment VI; DETECTOR_LOG rejects the home-made GPT-2 score | - |
| 100 | B9 | Use real, reputable web detectors, perhaps weighted | process | NOT MET | 27-30 Oct: none run. On 30 Oct DETECTOR_LOG tried GPTZero: API needs a key (I re-tested: HTTP 401 "Require login or API key"); the free scan needs reCAPTCHA. Every other detector host is refused by the proxy | Process gap P1 |
| 101 | B9 | AI detection is low priority; don't make it a big project | process | MET | - | - |
| 102 | B9 | Don't obsess over JPM's 7.5% for VT | IPS | MET | No return figure in D12 | Gap 2 states a world-stocks assumption, labelled as world stocks, not as VT |
| 103 | B9 | Not hamstrung by the TNA; go deeper | IPS | MET | - | - |
| 104 | B9 | Studies like the donor study are "absolutely BRILLIANT"; use them | IPS, FR | PARTLY | IPS: "her lead gift draws bigger ones" (the evidence is hidden). Bank #85 now read at source (sixfold) | Gap 14 (FR and the co-sponsor text; IPS only if words free up) |
| 105 | B9 | Turn model findings into arguments ("3 times in 4 ... 3 times worse") | IPS, FR | PARTLY | Ledger D4 -> FR as a newsvendor calculation. The IPS never says how the top's confidence was set (panel-2 J3: "how ... the 97% figure [was] chosen") | Gap 14 |
| 106 | B9 | "Every single good idea ... must end up in either the IPS or the Final Report" | IPS, FR | PARTLY | Ledger and bank exist (met). The ledger's IN column is about V31; 30 Oct bank rows 83-91 aren't in the ledger | Process gap P10 |
| 107 | B9 | Research is done "SPECIFICALLY so that it can go into one of the deliverables" | FR | N/A now | - | FR outline maps each bank row to a section |
| 108 | B9 | Discard weak ideas, but "don't just throw ideas out wantonly" | process | MET | Bank "Dropped" list, each with a reason | - |
| 109 | B9 | Pitches "FEEL noticeably more AI"; "cut the HUMAN way" | pitch | NOT MET | D12 pitch: mirrored "one promise ... one hope", "Treasury floor" never defined, inverted slogan close "whatever she announces, we lock away". D13: the same close | Gap 10 |
| 110 | B9 | No artificial timeline constraints | process | MET | - | - |
| 111 | B9 | Work "far more intensively and densely"; quality and quantity | process | PARTLY | Book 10 is "disappointed in your progress" | Rows 134-136 |
| 112 | B9 | Stop AI-use logging; "Trust us" | process | MET | LEDGER and recorder retired | - |
| 113 | B9 | No "minute changes"; the big picture | process | PARTLY | Breach 1 logged (I53). Lab L-13 and LR-07 (30 Oct) still model a $9,768 coupon claim to the dollar | Rooms: one strategy question per round |
| 114 | B9 | Judges don't read word-for-word for precision | process | MET | - | - |
| 115 | B9 | Put this message in the Bible | process | MET | - | - |
| 116 | B10 | Mock judges "diverse not just in label but in their evaluations" | process | MET (design) | Six personas on four models; tau 0.34 (panel 1) and 0.23 (panel 2) | - |
| 117 | B10 | Judges must not approve almost every change Keel proposes | process | PARTLY | V32 was built from panel 1's stated reasons, then judged by the same six personas: four put it first. That is teaching to the test | Process gap P8 |
| 118 | B10 | Judges must not think like Keel | process | PARTLY | All judges and all rivals are written by Claude-family models. The rivals are Keel's simulation of the field | Process gap P8: add human-written controls |
| 119 | B10 | Apply the voice studies ("you're simply not applying them") | IPS | NOT MET | The guide's own tests fail on D12: colons as connectors (s9), no en dashes, ~10 numbers (s4: six), 6+ kickers (law 9: three). No README quotes the moves | Gap 13; Process gap P3 |
| 120 | B10 | The pitch is "so obvious it's AI" | pitch | NOT MET | See row 109 | Gap 10 |
| 121 | B10 | GPTZero on every draft before Caplet sees it | process | NOT MET | Never run on V25-V33. D12 isn't even labelled "not yet checked" (V33 is, in VERSIONS row 33) | Process gap P1 |
| 122 | B10 | "Human-written only" above 50%; change it until it is | IPS, pitch | NOT MET | No score exists | Process gap P1 |
| 123 | B10 | Our own unique voice matters more than the detector score | IPS | PARTLY | - | Gap 13 |
| 124 | B10 | Use the human-vs-AI notes that were "completely ignored in your IPS" | IPS | NOT MET | Voice guide s9 (stop: colons as connectors, triads, slogan endings) vs D12: 11 colons; closes on a triad ("the cheques come first, then the floor, then the hope") | Gaps 6, 13 |
| 125 | B10 | No sentences so compressed "they barely make sense" | IPS | PARTLY | Unclear on one read (panel 2, the D13 cold read): "two points ... more than halves", "sized to grow back to the whole remainder", "for a dearer building", "(do not crush)", "one time in four", "97 times in 100" | Gaps 3, 5, 9, 12 |
| 126 | B10 | "Natural human variation or flair", not minimalism | IPS | PARTLY | Sentences run 9-36 words; no build longer than 36 | Gap 13 |
| 127 | B10 | Judges mustn't fixate on deal-breaker sentences, "framework lines" or elegant rhetoric | process | MET (design) | Judges README: "no single sentence may decide" | - |
| 128 | B10 | "Your only allegiance in terms of marking is to the marking guide from Wharton" | process | MET | Judges get only WHARTON_WORD + the case | - |
| 129 | B10 | No "every team will do x" | IPS | MET | None in D12. D13 adds "where most investors would", a milder comparison (its cold read flags it) | Keep it out |
| 130 | B10 | No arbitrary numbers "plucked out of thin air" | IPS | PARTLY | "about a fifteenth", "two points", "more than halves" and "$300,000" (cost) have no source in their sentence | Gap 2 |
| 131 | B10 | "We model" / "we calculate", never "we judge" | IPS | MET | "in our model" ×3; no "we judge" | - |
| 132 | B10 | Stop obsessing over AI use | process | MET | - | - |
| 133 | B10 | "Required trading activity" doesn't contradict the plan; drop it | process | MET | Not raised since | - |
| 134 | B10 | Final IPS by the end of Wed 4 Nov | process | open | 5 days left | - |
| 135 | B10 | "Absolute overdrive"; "significantly increase your pace" | process | PARTLY | 30 Oct: V30-V33, two panels, L-13, LR-07, the detector tests. But THINKING_LOG's last entry is 29 Oct | Process gap P7 |
| 136 | B10 | "Demonstrate to yourself" vastly more work per day than before | process | NOT MET | No per-day output tally anywhere (RUNLOG lists runs, not volume) | Add a daily tally line to `pm/CHANGES.md` |
| 137 | B10 | 2,300 teams, Top 50, winner takes all: "WHATEVER it takes" | process | PARTLY | - | - |
| 138 | B10 | "Number one instruction": not ordinary, but creative, original, novel, insightful, EXTRAORDINARY | IPS | NOT MET | Panels rank V32 best of Keel's own field; nothing yet shows it beats a strong human field | Gaps 1, 12, 15; Process gap P8 |
| 139 | B10 | A fresh list of commandments | process | MET | BIBLE.md, the Ten Commandments | - |
| 140 | B10 | "It MUST BE FOLLOWED. Right now, they exist for decoration" | process | NOT MET | `COMMANDMENTS_CHECK.md` is an empty template. D11 and D12 have no README or check. D13's check fails 4 lines | Process gap P2 |
| 141 | B10 | "Your final IPS MUST satisfy ALL of our expectations" | IPS | PARTLY | This table | Top 15 |
| 142 | B10 | Recursive self-improvement without Caplet's feedback | process | PARTLY | Panels and cold reads exist; the fixes they ask for aren't checked against the Bible | Re-run this audit each round |
| 143 | B10 | Take initiative and intellectual risks | IPS | PARTLY | D12 is safe. The one risky idea (one government on purpose) was cut | Gap 1 |
| 144 | B10 | Guess what Caplet will say next and have it covered | process | NOT MET | No "what they'd say" entry exists anywhere (the Commandment X test) | Process gap P7 |
| 145 | B10 | Rewrite from scratch again | IPS | MET | V31 | - |
| 146 | B10 | Keep a list of every idea in every version | process | MET | `IDEA_LEDGER.md` (versions 1-30) | Add V32-V33 columns (P10) |
| 147 | B10 | "All of the best ideas end up in the new IPS" | IPS | PARTLY | The best ones that are out: B6 one borrower, B9 inflation/Taiwan, B12 numbers explained, the donor evidence | Gaps 1, 5, 14 |
| 148 | B10 | Add this message to the Bible | process | MET | - | - |
| 149 | B10b | Wharton's documents are "God"; strip the logistics; treat the useful parts with "the utmost importance" | process, IPS | PARTLY | WHARTON_WORD.md done (met). The draft still ignores Wharton's own list of five balance words | Gaps 1, 4, 5, 6 |
| W1 | W1 | Investment Strategy: "a clear and creative investment thesis" | IPS | PARTLY | Clear, yes. Creative: see row 18 | Gaps 1, 12 |
| W2 | W1 | "Disciplined planning across Laura's changing time horizons and cash-flow needs" | IPS | MET | 2027 / 2028 / 2031 / 2033 each has a rule | - |
| W3 | W1 | "Uses appropriate diversification" | IPS | NOT MET | The word and the argument are both absent; "a world index fund" is the only hint. Concentrating the cheques in one government is unexplained | Gap 1 |
| W4 | W1 | "Maintains consistency with the team's IPS" (TNA, WInS, FR) | IPS | MET | Matches the locked TNA lines (`00_GROUND_TRUTH.md` s3: IBTM floor, VT growth only, the 2028 top-up) | - |
| W5 | W1 | Client Knowledge: tailored to her "circumstances, priorities, risk considerations" | IPS | MET | Human capital; "thoughtful risks" already spent | - |
| W6 | W1 | ... "and residency goals" | IPS | PARTLY | No Taiwan, no currency, no building cost (panel 2, J3 and J4) | Gap 5 |
| W7 | W1 | "A thoughtful understanding of the client" | IPS | MET | - | - |
| W8 | W1 | "Recommendations that can earn her confidence" | IPS | MET | - | - |
| W9 | W1 | Portfolio Analysis: "understanding and effective use of investment concepts and tools" | IPS | PARTLY | Concepts unnamed (row 56) | Gap 15 |
| W10 | W1 | "Integrates quantitative and qualitative analysis" | IPS | MET | - | - |
| W11 | W1 | "Reasonable assumptions and projections" | IPS | NOT MET | No assumption stated anywhere (panel 2, J3: "states no return or inflation assumptions"; J6: "the model ... is never described") | Gap 2 |
| W12 | W1 | Evaluate "funding reliability, the facility contribution, and financial flexibility under varying market outcomes" | IPS | PARTLY | Reliability: yes. Facility: yes. Flexibility: never evaluated, never named | Gap 5 |
| W13 | W1 | Articulation: "teamwork, communication, and learning ... research and decision-making process" | IPS, FR | PARTLY | One bracket in D12 (J1 4/10, J6 5/10). D13: fixed (story told) | Gap 7 |
| W14 | W1 | Creativity & Presentation: "a compelling, well-organized narrative" | IPS | PARTLY | - | Gaps 11, 12 |
| W15 | W1 | "In an authentic team voice" | IPS | NOT MET | "we" ×1; not detector-checked | Gaps 7, 13 |
| W16 | W1 | "Uses data effectively to support conclusions" | IPS | PARTLY | Two of D12's four model numbers confused four of six judges | Gap 3 |
| W17 | W1 | "Original thinking and meaningful reflection" | IPS | PARTLY | - | Gaps 1, 7 |
| W18 | W1 | Communicates the facility contribution and uncertainty "clearly and credibly to prospective co-sponsors" | IPS, FR | PARTLY | "97 times in 100" with no reason why it isn't 100 | Gap 3; FR co-sponsor text |
| W19 | W2 | Explain how we invest "to support their financial goals and future cash flow needs while managing risk" | IPS | MET | - | - |
| W20 | W2 | Reflect "goals, time horizons, liquidity needs, desired degree of funding certainty, and need for financial flexibility" | IPS | PARTLY | Liquidity needs and flexibility are never addressed by name | Gaps 4, 5 |
| W21 | W2 | Q: "What is the central idea?" | IPS | MET | Buy the promise; grow the hope on a floor | - |
| W22 | W2 | Q: "What principles will guide your investment decisions?" | IPS | PARTLY | Implicit only; no sentence a judge can point to | Gap 6 |
| W23 | W2 | Q: how it "balance[s] growth, risk, liquidity, funding reliability, and financial flexibility" | IPS | PARTLY | Growth, liquidity and flexibility never named | Gaps 4, 5 |
| W24 | W2 | Q: how allocation "will change as future funding needs approach and payments are made" | IPS | PARTLY | 2028 / 2031 / 2033 shown. After 2033, what happens to her kept half and the floor's leftovers is never said | Gap 5 (one clause); FR |
| W25 | W2 | Q: protect the operating commitment while preserving flexibility for a responsible contribution | IPS | MET | - | - |
| W26 | W2 | "Always remember who your strategy is designed to serve" | IPS | MET | - | - |
| W27 | W2 | Pitch: summarise the strategy; the central idea; how it supports her goals | pitch | PARTLY | Central idea yes; "Treasury floor" and "lock away" unclear | Gap 10 |
| W28 | W2 | IPS: "approach risk and return" | IPS | PARTLY | The risk side is thorough; the return side has no assumption | Gap 2 |
| W29 | W2 | IPS: "portfolio construction and diversification" | IPS | PARTLY | Construction: yes. Diversification: no | Gap 1 |
| W30 | W2 | IPS: "managing the operating reserve's asset composition over time" | IPS | MET | "the reserve runs itself down" | - |
| W31 | W2 | IPS: "determining a responsible facility contribution" | IPS | MET | The range rule | - |
| W32 | W2 | IPS: "preserving appropriate financial flexibility" | IPS | PARTLY | "the other half stays hers, for a dearer building" (unclear; flexibility unnamed) | Gap 5 |
| W33 | W2 | Strategy and decision framework, not individual investments or detailed calculations | IPS | MET | - | - |
| W34 | W2 | Not expected: final reserve sums, detailed projections, a final range | IPS | MET | - | (the 97-in-100 is close to a final-range confidence: Gap 3) |
| W35 | W2 | Sources not cited; no charts, links or citations | IPS | MET | - | - |
| W36 | W2 | "Once submitted, the strategy may not be revised" | IPS | MET | Dated rules | - |
| W37 | W3 | "The reasoning, assumptions, and tradeoffs behind those decisions" | IPS | PARTLY | Reasoning and trade-offs: strong. Assumptions: none | Gap 2 |
| W38 | W3 | A cohesive strategy "across a range of possible market outcomes" | IPS | MET | - | - |
| W39 | W3 | Planned adjustments as dates approach, "not ... rewritten simply because markets move" | IPS | PARTLY | True of the plan, never said. Bank #72 ("dated doors, not alarms") sits in the FR column | Gap 6 |
| W40 | W4 | "Let your investment strategy lead" across WInS, the TNA, the IPS and the FR | IPS | MET | Consistent with the WInS book | - |
| W41 | W4 | "Know your client" | IPS | MET | - | - |
| W42 | W4 | "Use WInS to demonstrate your strategy" | FR | MET | WInS = the ladder + VT | FR |
| W43 | W4 | "Do not focus on portfolio performance"; no WInS P&L in projections | IPS | MET | - | - |
| W44 | W4 | "Explain why each investment belongs in your strategy" | IPS | PARTLY | Why iBond funds and not only bonds (liquidity, per the locked TNA) is never said; why a world fund rather than US stocks, never said | Gaps 1, 4 |
| W45 | W4 | "Follow the instructions" | IPS | PARTLY | See W3, W11, W20, W22 | Gaps 1-6 |
| W46 | W5 | Only WInS stocks, ETFs and Treasuries; no TIPS, STRIPS or derivatives | IPS | MET | The bank's protected note appears only as a foil ("minus the bank") | - |
| W47 | W6 | Case lines judges hold us to: "responsibly contribute"; "committing all remaining assets could limit her financial flexibility" | IPS | PARTLY | The kept half answers it, but too briefly to be noticed | Gap 5 |
| W48 | W6 | "Willing to take thoughtful risks" | IPS | MET | Met head-on (panel 2, J5: "the sharpest reading of the client"). The growth hawk still wants the small sleeve argued (J2) | Optional: D13's concession line |
| W49 | W6 | The 2028 deposit comes from "publishing advances, speaking engagements, licensing" | IPS | MET | - | - |

## 2. Top 15 gaps for the IPS draft, ranked by how much a Wharton judge would notice

These are edits to **D12**. Each says whether D13 already fixes it. Budget: D12 is 500/500 strict, so the package
below pays for every addition with a named cut of a whole idea. Book 10 rules apply: cut ideas, don't squeeze;
no "every team"; every number says where it came from; no worrying about AI-use citation or "required trading
activity". The running total is checked at the end: the whole package comes to **IPS 499 strict (494 by spaces) and
pitch 48**, using `office/tools/textcheck.py`.

**1. Diversification is a Wharton criterion, and the IPS never argues it (W3, W29; B1's aha; B10 "intellectual
risks").** A judge with the rubric looks for "appropriate diversification", finds every cheque resting on one
government and no word on why, and marks it down. It is also our best unused aha: panel-2 J5 counted it among "what
I learned that I did not know" (ledger B6, bank L1). *Add* after "That's our XR, too: X for ten, R for redemption.":
"We spread her stocks across the world but keep every cheque with one borrower, because ten safe bets on ten borrowers
would miss a January more often." (+27). *Paid by* gaps 8 and 9. D13: not fixed.

**2. "In our model" never says what the model assumes (W11, W28, W37; B10 "says who").** Two judges said so outright
(J3: "states no return or inflation assumptions"; J6: "which model and which return assumptions"). Wharton names
"reasoning, assumptions, and tradeoffs". *Change* "in our model a balanced portfolio" to "In our model (world stocks
at about 7% a year) a 60/40 portfolio" (the models run 7.5% with a 6.5% sceptic case on the 22 Oct curve: say
"world stocks", never "VT's return", per Book 9). *Change* "a cheque can fail only if" to "In our model a cheque fails
only if", and "about a fifteenth of all she owns" to "about a fifteenth of her money by our sums". (+11 in all). D13: not fixed.

**3. The two probability lines confuse most of the panel (W16, W18; B10 "barely make sense").** Four of six
panel-2 judges couldn't tell whose promise the 60/40 "breaks one time in four", or why a locked top is reached only
"97 times in 100". *Cut* "In our model the gift reaches its top about 97 times in 100." (-13). Wharton says the
final range and its confidence belong to the FR, and the lock sentence ends the paragraph better without it.
*Rewrite* the 60/40 clause as "usually leaves her richer but misses a cheque or its own range one time in four"
(+4; Model Suite M7: 60/40 cheques short 7.6%, below its own range 27%; re-run on D12's design before use).
D13: explained both, but its own cold read found a new clash ("one future in thirty" for 75% stocks next to "one
time in four" for 60/40). Fix that by naming the metric, as here.

**4. Liquidity, a word in Wharton's own question, is missing (W20, W23, W44).** The locked TNA already says why we
use iBond funds: "a level of liquidity which no odd-lot bond offers". *Change* "each maturing before its January." to
"each maturing before its January, each sellable any day." (+4). D13: not fixed.

**5. Flexibility and the residency's Taiwan side are missing (W6, W12, W32, W47; panel 2, J3 and J4).** "For a
dearer building" is the only nod to flexibility, and a cold reader can't decode it. *Change* "and the other half
stays hers, for a dearer building." to "and the other half stays hers, as flexibility for a building priced in Taiwan
dollars." (+4). This names flexibility, ties the kept half to the residency goal and hints at currency risk in one
clause. If 7 more words free up, add "still in world stocks" to answer W24 (what happens after 2033). D13: tried and
cut.

**6. No sentence states a principle, and the close is a triad slogan (W22, W39; voice guide s9).** Wharton asks
"What principles will guide your investment decisions?" and says a strategy shouldn't be "rewritten simply because
markets move". *Replace* "If anything changes, the cheques come first, then the floor, then the hope." with "Our
rules fire on dates, never on market moves, and the hope gives way before any cheque." (+4). This promotes bank #72
(dated doors) from FR to IPS, because it is Wharton's own language. D13: not fixed.

**7. The team is invisible (W13, W15; B1 voice; panel-2 Articulation 4-7/10).** D12 has "we" once, and its only
team event sits in brackets. *Change* "(Our first plan, three-quarters stocks, missed cheques in our model.)" to "Our
first plan, three-quarters stocks, missed cheques in our model, so we dropped it." (+4). *Change* "so Caplet XR keeps
them apart" to "so we keep them apart" (-1). D13: fixed (we ×6; the story told), but keep out its "where most
investors would" (Book 10's comparison rule).

**8. The sceptic lines are inaccurate and duplicate the real opponent (B3 accuracy, B10 clarity, voice guide law
2).** "Laura doesn't owe one ten-year bill. She owes ten one-year bills" is wrong on its face: her cheques fall due 6
to 15 years out. The point it reaches for is sequence risk, and the 60/40 line already voices the opponent with a
number. *Cut* "Stocks beat bonds over most decades, but Laura doesn't owe one ten-year bill. She owes ten one-year
bills, and anyone owing a fixed amount must sell at the bottom of a crash." (-32). *Replace* the end of the pill
sentence with "Her cheques are like that, because $50,000 falls due, good year or dreadful, and shares sold in a
dreadful year never come back." (+11 over D12's 12-word sentence; net -21). Alternative, if the team wants the
sceptic kept: use Model Suite M8 instead (start a 60/40 in 1923, stocks win the next fifteen years and the last two
cheques still bounce), which is evidence rather than an aphorism. Re-check M8's numbers first; the Window flagged
M1b. D13: not fixed.

**9. The break point is factually wrong and reads as code (B5 accuracy; B10; panel-2 J4 read it twice).** "Her 2028
deposit more than halves" isn't the modelled break: with the coupon backstop counted, it is a deposit under about
$85,000 (Window 28 Oct; Lab K07; D13's commit). *Change* to "and her 2028 deposit shrinks from $150,000 to under
$85,000" (+3). *Also cut*, as a whole idea, "The cheques add up to $500,000 but cost about $300,000, because interest
pays the rest." (-15). It has no source in its sentence (Commandment V), it is an FR fact rather than a principle,
and D13 dropped it too. D13: break point fixed.

**10. The pitch still sounds like an AI slogan (B9 "FEEL noticeably more AI", B10 "so obvious it's AI", W27).** It
mirrors the IPS's opener, uses "Treasury floor" before anyone has said what a floor is (Commandment IV), and closes
on an inverted slogan ("whatever she announces, we lock away") that doesn't say what is locked or into what.
*Replace* the whole pitch with (48 words): "Laura owes her residency $50,000 every January for ten years, and hopes to add a
gift for the building. Caplet XR buys all ten cheques first, with Treasuries that mature in time. Her second deposit
backs the gift with bonds and risks only their interest in world stocks." It sounds like something said across a
table (voice guide s9 test), and it carries the central idea and the client fit Wharton asks for. D13: not fixed
(same close).

**11. The mirrored opener duplicates the pitch and garbles the first sentence (B1 "unlike any other team", W14).**
"Laura has made her residency one promise and has one hope" reads, on first pass, as if the residency made the
promise (D13's cold read). It is also the default rival's shape. *Cut* that sentence (-11) and *start*: "Laura's
promise is $50,000 every January ... ; her hope is a gift for the building ..." (0). D13: not fixed.

**12. The motif has no arc and one part of it is undecodable (B2 "narrative arc", "not ... layered on"; B3 "do not
crush"; B5 "clever and thought-out").** XR is used in paragraphs 2-3, then reappears only as "(do not crush)", which
no judge can read without knowing pill labels. *Change* "(do not crush)" to "(an XR pill's \"do not crush\")" (+3), so
the motif returns once, with its meaning, where it does real work (no sale before a bond pays). Keep D12's "however
much is left": it is the fixed-dollar point (zero-order release), and D13 lost it. If words free up, add one clause to
"R for redemption": "since each bond is redeemed just before its cheque". The FR gets the therapeutic window (range)
and the blister pack (bank #90). D13: crush explained, "however much is left" dropped.

**13. The prose fails the voice guide Keel wrote (B2, B5, B10 "voice studies ... not applying them"; Commandment
III).** D12 has 11 colons used as connectors (guide s9: an AI-compression tell), no en dashes (Book 3: "we're going to
use them"), three sentences opening "So", and a kicker ending nearly every paragraph. *Do*: turn at least five colons
into full stops (word-neutral: "certainty. In our model", "already taken. The residency", "a cheque. It plugs",
"smaller boom. In our model", "a flaw. Once"). Drop the three sentence-opening "So"s (-3). Let three paragraphs end on a plain
decision rather than a line. Use spaced en dashes where an aside is real, but each one counts as a word in
textcheck. Then do what Commandment III asks: file a README quoting the build-then-land pair, the concession and
"But", and the wry line, checked against Ahaan's TNA reflections, not only his essays. D13: partly fixed (5 colons,
8 en dashes).

**14. The range's evidence and its logic are hidden (B9 "donor study ... BRILLIANT", "3 times in 4" argument; W18).**
"High enough that her lead gift draws bigger ones" asks the judge to take it on trust. The study is now read at
source (bank #85: raising announced seed money from 10% to 67% of the goal, "nearly sixfold" giving). *IPS*: keep as
is; it costs about 15 words, and gaps 1-9 matter more to a judge. *FR and co-sponsor text*: give the study, the
newsvendor reading of the two costs (each end as sure as its miss is costly, bank #84) and the IPO-range honesty test
(#83, #87), with citations. This is a conscious FR placement under Book 9's "save it ... include it in the Final
Report", not a drop. D13: not in.

**15. Investing knowledge is used but barely named (B4 north star 4; B9 "INTELLIGENT and KNOWLEDGEABLE"; W9).** A
judge scanning for concepts finds "capital-protected note" and nothing else, though the IPS runs on sequence risk,
human capital, reinvestment risk and cash-flow matching. Naming two of them, each in one breath, is cheap. *Change*
"and her income from advances, speaking and licensing shrinks" to "and her human capital (advances, speaking,
licensing) shrinks" (-1). Gap 8's new line already gives sequence risk in plain words. Name it ("planners call it
sequence risk") only if 5 words free up. D13: not fixed.

**Budget check (all 15 applied to D12):** cuts -32 (sceptic), -15 ($500k), -13 (97), -11 (opener), -3 ("So"s),
-1 (human capital), -1 ("we keep"). Additions +27 (one borrower), +11 (assumptions and sources), +11 (crash line),
+4 each (60/40 wording, liquidity, flexibility/Taiwan, principle, team story), +3 each (break point, crush), plus
word-neutral colon swaps. Measured with textcheck: **IPS 494 by spaces, 499 strict; pitch 48**. The assembled text is shown below only to prove the package fits. It is not a
draft for Caplet: it has had no GPTZero check, cold read or panel.

> Laura's promise is $50,000 every January from 2033 to 2042, paid from this portfolio alone; her hope is a gift for
> the building, big enough to win co-sponsors over. They need different kinds of money, so we keep them apart.
>
> Pharmacists call a pill that releases the same dose every hour, however much is left, extended release: XR. Her
> cheques are like that, because $50,000 falls due, good year or dreadful, and shares sold in a dreadful year never
> come back. Our first plan, three-quarters stocks, missed cheques in our model, so we dropped it.
>
> Her first $300,000 buys all ten cheques in January 2027: a ladder of Treasury bonds and iBond Treasury funds, each
> maturing before its January, each sellable any day. That's our XR, too: X for ten, R for redemption. We spread her
> stocks across the world but keep every cheque with one borrower, because ten safe bets on ten borrowers would miss a
> January more often.
>
> That is our definition of a high degree of certainty. In our model a cheque fails only if the US government
> defaults, or if yields fall two points before we buy and her 2028 deposit shrinks from $150,000 to under $85,000.
> The ladder's one leak, coupons reinvested at lower yields, is priced and set aside in 2031, before she names
> anything.
>
> Laura's "thoughtful risks" are already taken. The residency is the boldest bet of her life, and her human capital
> (advances, speaking, licensing) shrinks in exactly the recessions that make bonds dear. Her 2028 deposit never
> carries a cheque. It plugs any gap in the ladder, then builds her gift.
>
> Most of it buys her floor: Treasuries maturing late in 2032, sized to grow back to the whole remainder. The interest
> they should earn, about a fifteenth of her money by our sums, goes into a world index fund. It's a bank's
> capital-protected note, minus the bank and its fee. The price is a smaller boom. In our model (world stocks at
> about 7% a year) a 60/40 portfolio usually leaves her richer but misses a cheque or its own range one time in four.
>
> In 2031 Laura gives co-sponsors a range: low enough to keep her word, high enough that her lead gift draws bigger
> ones. The bottom is the floor she owns; the top adds half her stocks, and the other half stays hers, as flexibility
> for a building priced in Taiwan dollars.
>
> But a capped range hides a flaw. Once it's named, a fall in stocks comes off the gift while a rise past the top
> goes to Laura. The day she names it, the promised half moves into Treasuries.
>
> From 2033 the ten holdings are the operating reserve. Nothing is sold before it pays (an XR pill's "do not crush");
> each turns to cash before its cheque, so the reserve runs itself down. Our rules fire on dates, never on market
> moves, and the hope gives way before any cheque.

Still weak after the package, and left for the writer to judge: "sized to grow back to the whole remainder" (say what
the remainder is), and "the ladder's one leak" (the third image after the pill and the floor). D13's concession line
("Laura is willing to take thoughtful risks, but she has already taken the big one") is better than D12's and costs 9
words. It is the first thing to buy if Gap 5's optional clause is dropped.

## 3. Process gaps

**P1. GPTZero (Book 10; Book 9 asked for real detectors three days earlier).** No draft has ever been scanned. D12
isn't even labelled "not yet checked", which Commandment VI requires when GPTZero can't be reached. What is true from
this container on 30 Oct: gptzero.me loads (HTTP 200), the API answers 401 "Require login or API key" (paid), and the
free scan needs Google reCAPTCHA, which the network blocks and which Keel may not bypass (DETECTOR_LOG). ZeroGPT,
QuillBot, Sapling, Copyleaks, Originality, Scribbr, Grammarly, Undetectable, Writer and Hugging Face are all refused by
the proxy. The local GPT-2 detectors scored 44% leave-one-out, worse than a coin, and were rightly rejected. Caplet
can't keep a computer on, can't use the paid API and couldn't sign up to GitHub (30 Oct), so DETECTOR_LOG's "paste it on
Thursday" is the only route left, and it puts the work back on Caplet. **Fix:** (a) label every draft "GPTZero: not
yet checked" in its README and in VERSIONS, as V33 now is; (b) the coordinator should check the environment's network
settings (`read_documentation`, topic `environment.network`) and ask the owner to allow `gptzero.me`,
`api.gptzero.me`, `www.google.com/recaptcha` and `www.gstatic.com`, which is a one-time web setting needing no
computer left on (still UNVERIFIED whether the free scan then works headless, and a CAPTCHA must never be solved by
Keel); (c) until then, the voice work (P3) carries the load, and Keel says so plainly rather than implying a check
happened.

**P2. The commandments are decoration again (Book 10: "it MUST BE FOLLOWED").** `COMMANDMENTS_CHECK.md` is an empty
template; D11 and D12 have no README and no check; D13's check exists and fails four lines. By the Bible's own rule
("A draft with a failed line does not go to Caplet"), no current draft can go to Caplet. **Fix:** no new version
number without a filled ten-line check in its folder, by a reader who didn't write it. Add this audit's Top-15 list
as an eleventh line ("Wharton's five balance words and the IPS's five questions answered by name").

**P3. Voice studies not applied (Books 2, 5, 9, 10).** The guide's own tests fail on D12 (s9 colons, law 9 kickers,
s4 six numbers, no en dashes). No draft is compared with Ahaan's rewritten TNA reflections, which Book 5 named.
D13's cold reader "did not read ... the voice guide". **Fix:** a separate voice reader for each draft. It reads
Ahaan's TNA reflections and one Wall Street piece from `voice/reading/`, then marks every sentence of the draft "his",
"theirs" or "machine", qualitatively, with no counts as gates (Book 9). Any "machine" sentence is rewritten before
the panel sees the draft.

**P4. The voice guide contradicts Book 10.** `voice/06_voice_guide.md` s5 still says "Keel never judges whether its
own prose 'sounds AI': ... a student pastes the text into a reputable web detector". Book 10 makes the scan Keel's job.
**Fix:** rewrite s5 to point to Commandment VI and DETECTOR_LOG the same day (BIBLE: "the run that notices rewrites
the other file that day").

**P5. The register of instructions stops at Book 9.** `INSTRUCTIONS.md` still says "eight books", its last row is
I56, and Book 10 has no row. CLAUDE.md says a row goes in "the day a student gives a new one". **Fix:** add I57-I66
for Book 10's ten asks (diverse judges; voice studies applied; GPTZero over 50%; no over-compression; judges only on
Wharton's guide; no "every team"; "we model"; no AI-use or trading-activity fretting; overdrive with measured
output; commandments enforced; an idea list across versions; recursive self-improvement) and one for the 18:21 note
(Wharton = God). Give each a status and its evidence from this audit.

**P6. Panel 2 records were incomplete when V32 was handed on.** `rankings.json` left out J5, and there was no
SUMMARY until 8d36e68. VERSIONS had no rows 30-32 until the same commit. **Fix:** a version is "done" only when its
VERSIONS row, panel summary and check are in the same commit (CLAUDE.md: "No work is finished until the portal shows
it").

**P7. No "what they'd say" log (Commandment X; Book 10 "GUESS what I'm thinking").** THINKING_LOG's last entry is
Thu 29 Oct. Nothing records the 30 Oct round or predicts Caplet's next complaint. **Fix:** a short entry per round:
what Caplet would say next, and the fix. For Thursday, the likely complaints are that the IPS still doesn't name
liquidity, flexibility or diversification (Wharton's own words); that it was never put through GPTZero; that the
pitch is a slogan; and that "the motif disappears halfway through".

**P8. The panels mark Keel's homework with Keel's red pen (Book 10).** V32 was tuned to panel 1's stated reasons,
then judged by the same personas, so its 4-of-6 first places partly measure that tuning. Every rival is a Keel-written
simulation, so "first of six" says little about "Top 50 of 2,300". **Fix:** (a) refresh the rival set every round and
include at least one human-written control: Caplet's own Version 5 (`caplet/google_drive/ips_report/01_version_5.md`)
and, if the team can supply one, a human-written IPS from 2025-26; (b) give each judge persona a fresh random seed of
rivals it hasn't seen; (c) report how often the panel's top reason matches the change Keel just made: high overlap
means teaching to the test.

**P9. The rewrite README's plan is stale.** It still schedules "Sat 31 Oct near-final draft" in `drafts/D5/`. **Fix:**
rewrite the plan to Book 10's dates (final for review by end of Wed 4 Nov, read Thu 5 Nov; IPS due Sat 7 Nov 09:00
Sydney / Fri 6 Nov 5 pm ET).

**P10. The idea ledger tracks V31, not the live draft.** Its IN column refers to V31; V32 appears only as a
footnote. Some ledger "IN" rows aren't in D12 (A2 "Every number she says aloud is already owned"; A5's heading; E3's
"overruns, Taiwan costs and the currency" shrank to "a dearer building"). The 30 Oct bank rows 83-91 aren't mapped.
**Fix:** one column per live version (V32, V33, ...) and a "best idea not in the IPS" list at the top, which the
writer must argue against before each new draft (Book 10: "all of the best ideas end up in the new IPS").

**P11. Haste presented as overdrive (CN vs Book 10).** Book 10 asks for "vastly more work per day", but the cover
note still forbids haste. Four versions and two panels in one evening is volume, not thought: V32 created two of the
confusions panel 2 found (the 97 and the one-in-four). **Fix:** measure overdrive by what was learned and tested per
day (models run, sources read at source, ideas promoted or killed), logged in `pm/CHANGES.md`, not by how many
version numbers were issued.
