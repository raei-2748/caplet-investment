# Response to the WS6 notes judge panels (30 Sep 2026)

WS6-revise, RAB Kit, 30 Sep 2026 (Sydney). AI-generated (Claude Code, Claude Opus 5.5) for Team Caplet. Three rounds
of three panels each: round 3 reviewed `notes.md` at dd68e6e, round 2 at 104476c, round 1 at c11b02f. In each, J1 is the WGHSIC judge
(self-scoresheet scale), J2 is Laura and her co-sponsors, and J3 is the pedantic fact-checker. Each point is either
fixed or rejected with a one-line reason. **The strategy is unchanged.** The IPS, the live Sheet and `numbers.yaml`
were not edited. IPS wording items are triaged for the team (`notes.md` s7), and new figures are requested from WS1
(`notes.md` s7, "Requests to WS1").

## Round 3 (panel at dd68e6e)

### What changed

- **Who absorbs a gap (J2 #1-2, J3 #2-3).** IBTR now ends "the facility gets less" and IBTR_F "less is left for
  the facility". Both are true whether the floor is a fixed $150,000 (the kit's model, WS4) or what is left of the
  2028 deposit (the IPS read literally). The two definitions are a new fix-before-6-Nov triage row and a new 1 Oct
  vote item. `refresh_tickets.py` gains `--floor-rule fixed|remainder`. The default is unchanged. When the test fails,
  the script prints the split under the other definition too. The strategy is unchanged.
- **IBTR's number follows Friday's curve (J1 #1).** The refresh now prints the room, the break-even and the words to
  type: under 22.5bp "about a fifth", 22.5-30 "about a quarter", 30-37.5 "about a third". On the Gate A basis it
  prints 26.2bp and "about a quarter", as locked. I re-ran J1's figures on par curves fetched 30 Sep: 20.1bp (24 Sep),
  19.3 (25 Sep), 26.2 (28 Sep) and 28.9 (29 Sep). The brief quotes them as MODEL; only 28 Sep is locked.
- **Basis corrected (J2 #8, J3 #4).** WS4's 22.8bp is the same STRIPS basis with yields unchanged. It is not the
  buyable ladder. A WInS-listed ladder sized to $50,000 a rung costs within $100 of STRIPS (WS4 memo;
  `bookL_basis_check.txt`). The "about a fifth" basis switch and "likely higher" are deleted. WS1 request 9 is
  rewritten.
- **Exemplars:**
  - IBTR (294 characters): "We checked first: ... Treasuries for Laura's ten $50,000 payments cost under her
    $300,000 first deposit. It is future funding for the fifth payment. ... the facility gets less."
  - IBTR_F follows IBTR.
  - T39: "in her plan", and "the rest depends on reinvested coupons".
  - IBTM_R: "the first call on a shortfall".
  - IBTM_P: one sentence, and "It holds 2032 Treasuries".
  - VT: "thousands of companies worldwide" and "the top of the range". "Bought last" and "Half the fund stays hers" are
    dropped.
  - IBTP: "At the 1 Oct close" (the premium iShares publishes).
  - IBTQ and IBTO: the whole payout "is not fixed".
  - T38: "in her plan its money waits ... in Treasury bills", with no stale-price clause.
  - Every bond check is dated: "Its 1 Oct (WInS) price passed our curve check".
  - The swap notes say "more of what it pays comes at maturity".
- **Kit limit.** 285, or 295 for a note with no security name left to swap in (IBTR and IBTR_F name none; IBTM and
  VT were SEEN). This is J1's own proposal for IBTR. Every exemplar is 300 or fewer (longest 294). The limit is the
  new `kit_limit` column in `notes.csv`. `note_check.py --ticker` and Gate C G1 apply it.
- **Picks.**
  - Pick 2 is still the first of SW40, SW41, OD_B or IBTM_R. IBTM_R now also needs the IPS draft to carry the
    sentence the same day.
  - If none exists, the fallback is **T39** (supported: the reinvestment discovery), not IBTM_P.
  - The alternates are now IBTM_P, T39 and T41. T38's price check and the IBTN trap go to the Final Report.
  - Reflections:
    - Pick 1 leads with "$300,000 alone ... on only about 1 day in 9 since 2000".
    - Pick 2's one number is "$466,000 against ten $50,000 payments" at 2%.
    - Pick 3 adds the tradeoff, her balance clause, the cushion and the cap. It also names what backs the floor
      when pick 2 is a bond swap.
    - The scale sentence is reworded.
    - The new rule-reading clause goes in any featured reflection whose note cites a WInS listing gap.
- **Checker.**
  - `note_rules.py` bans "covers the rest", "covers her/the/that/each payment", "delivers $50,000", "half the fund
    stays" (unless it follows "at least") and the kit's 28 Sep reference prices ($21.76 ...). It now allows "operating
    reserve" and bans only a reserve size.
  - `note_check.py` self-test 7 catches the first and the last of these.
  - Gate C's claim patterns follow the new texts.
- **Runbook.** `friday_checklist.md` gets three additions:
  - Thursday: read the whole bond drop-down read-only; vote on the floor definition and on the IPS-draft condition
    for IBTM_R.
  - Friday: the break-even and words lines, the IBTP premium step and the dated bond prices.
  - `--floor-rule` in the failed-test branch.

  `october_trade.md` trigger B follows the floor definition. The `tickets.md` volume note now cites the Nasdaq URL,
  the fetch time and the file, and shows that the numbers.yaml series gives lower ratios.

### Round 3, J1: WGHSIC judge

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | The refresh prints no Friday break-even | Fixed | Room, break-even and words printed; J1's bands (plus guards under 15bp and over 37.5bp); Trade Log; WS1 request 1 |
| 2 | IBTR wording clipped; allow about 295 | Fixed | 294 characters, "Treasuries for", "the fifth payment". J1's model dropped the role word (the checker failed it), so it opens "We checked first:" |
| 3 | Read the drop-down before the vote | Fixed | Thursday read-only copy of all 43 bonds into the WInS Notes tab; writers draft only the variants that can happen |
| 4 | IBTM_R "any gap" | Fixed | "The first call on a shortfall" (J2): "cover a shortfall" would still promise cover |
| 5 | IBTM_R needs an IPS clause | Fixed | Triage row: the order of use by 6 Nov; type IBTM_R only if the IPS draft carries the sentence on 1 Oct |
| 6 | VT has no research | Fixed | "Thousands of companies worldwide" (the IPS phrase); "bought last" dropped |
| 7 | T39 "most of that payment" false at WInS scale | Fixed | "In her plan"; the brief gives the scale ($18,000 face) |
| 8 | IBTP "on the trade date" | Fixed | J3's more exact form: "At the 1 Oct close", the premium iShares publishes for that close |
| 9 | IBTM_P grammar and no research | Fixed in part | One sentence, no colons or split parenthesis, 287 characters. It uses "It holds 2032 Treasuries" (J2) in place of "WInS lists no late-2032 Treasury"; that reason moves to the alternate A outline with the rule-reading clause |
| 10 | Pick 1 history tests a different threshold | Fixed | Leads with the 1-in-9 quote_as; the 1-in-10 forward figure after WS1 request 12 |
| 11 | VT reflection has no tradeoff | Fixed | Tradeoff bullet (IPS paraphrase), 59 words |
| 12 | Two $300,000s side by side | Fixed | J1's scale sentence |
| 13 | Fallback should be T39, not IBTM_P | Fixed | T39 is the pick-2 fallback; IBTM_P is alternate A |
| 14 | "Curve check" is jargon | Agreed (ignore) | The definition stays in the pick 2 outline |
| 15 | T38 tested WInS data | Fixed | Out of the alternates (J2 #15); the story goes to the Final Report, as J1 suggested |

### Round 3, J2: Laura and co-sponsors

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | IBTR points at the wrong pocket | Fixed | "The facility gets less"; IBTR_F, the pick 1 row and the brief follow it |
| 2 | Two floor definitions | Triaged (fix-before-6-Nov) + tool | Vote item, IPS sentence, `--floor-rule`; the kit default is unchanged; no strategy change |
| 3 | T39 "covers the rest" | Fixed | "The rest depends on reinvested coupons"; now banned by the checker |
| 4 | IBTM_R "any gap" | Fixed | J2's "first call", with "shortfall" |
| 5 | VT: "stays hers", "lifts the range" | Fixed in part | "The top of the range". "Her cushion" goes in the reflection: the note's spare characters carry J1's research phrase (286 characters) |
| 6 | IBTM_R should outrank the swaps | Rejected in part | J1 and J3 rank a trade-made refinement higher, so the swaps stay first. J2's own fallback is adopted: when pick 2 is a swap, the VT reflection names what backs the floor |
| 7 | IBTM_P soft floor | Fixed | "It holds 2032 Treasuries"; the name string is the Friday fact; no price slot |
| 8 | Delete "about a fifth" and "likely higher" | Fixed | Both are gone. The Friday words band (J1 #1) is different: it follows the day's curve, not a basis switch |
| 9 | Pick 1 stakes | Fixed | "1 day in 9", then "less is left for the facility" |
| 10 | Pick 2 needs a number | Fixed | "About $466,000 against ten $50,000 payments" at 2% |
| 11 | Pick 3 cherry-picks her sentence | Fixed | Her balance clause, the cushion and the cap |
| 12 | "WInS lists no..." reads as a simulator limit | Fixed | New rule-reading clause (s6) and triage row |
| 13 | The checker bans "operating reserve" | Fixed | Only a reserve size is banned. The optional T41 clause is not used: no room |
| 14 | IBTQ/IBTO caveats understate the limit | Fixed | "What it pays out is not fixed" / "the amount it pays out that December is not fixed"; IBTQ drops the 2031 span |
| 15 | T38 and IBTP reason about WInS | Fixed | Alternate C is T41; T38 says her plan's Treasury bills; IBTP is not featured |
| 16 | iBonds rungs slightly short | Triaged (note-in-Final-Report) | Row added; "delivers $50,000" banned |

### Round 3, J3: fact-checker

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | T39 false reassurance | Fixed | As J2 #3, plus "in her plan" (J1) |
| 2 | IBTR/IBTR_F/pick 1 "stocks get less" | Fixed | "The facility gets less". Not used: "Tested first:" (J1 asked for an opening that is not a label) |
| 3 | IPS floor ambiguity | Triaged | As J2 #2 |
| 4 | 22.8bp misattributed | Fixed | Brief, triage row and request 9, checked against WS4 memo lines 27-35 |
| 5 | IBTP check cannot measure what it claims | Fixed | J3's text; checklist step for the published 1 Oct premium; request 2 |
| 6 | VT loose claims | Fixed | "The top of the range"; "stays hers" dropped. "At least half stays with her" is not used; the cushion goes in the reflection |
| 7 | IBTM_R exists only in the note | Fixed in part | "Shortfall"; typed only if the IPS draft carries the sentence; ranked last of the refined routes. **Rejected:** "feature IBTM_P instead". Once IBTM_R is typed, WInS holds its text, and with the sentence in the IPS draft "our policy" is true. The fallback when nothing refined exists is T39 |
| 8 | Pick 1 history selective | Fixed | As J1 #10 |
| 9 | Bond checks on a price the order will not get | Fixed | "Its 1 Oct (WInS) price" in T40b, T38, SW40, SW41 and SW37 ("its 1 Oct price failed" in T40s); fill price to the Trade Log. T40b trimmed to "Laura's ninth $50,000 payment" |
| 10 | T38 stale clause | Fixed | Dropped |
| 11 | $21.76 example | Fixed | Placeholder; the 28 Sep closes are banned; self-test 7 |
| 12 | IBTM is not a fund of late-2032 Treasuries | Fixed | Brief and triage row (IPS wording), 91282CPQ8 added; checked: 47.5% by weight matures by 31 May 2032 (S1 snapshot) |
| 13 | "1 Jan" and "operating payment" | Triaged (note-in-Final-Report) | Row added |
| 14 | Checker misses coverage claims | Fixed | Four patterns added; self-test 7 |
| 15 | "More of its value is owed" | Fixed | "More of what it pays comes at maturity" in SW40, SW41, OD_S and OD_B |
| 16 | IBTO wording | Superseded | J2 #14 (the whole payout is not fixed) |
| 17 | Ticket volume not in numbers.yaml | Fixed in part | `tickets.md` cites the Nasdaq URL, fetch time and file, and says the numbers.yaml series gives lower ratios. numbers.yaml is WS1's (request 7) |

### Checks after round 3

- `build_notes.py`: 0 fail.
  - 23 exemplars, the longest 294 characters. Every exemplar is within its kit limit (285, or 295) and under 300.
  - Outlines are 60, 60 and 59 words, and 81 and 88 with their shared sentence.
  - Pick openings: 0 shared. Variety passes.
- `note_check.py --self-test`: PASS (7 tests).
- `refresh_tickets.py`: 83 pass, 0 fail. `tickets.csv` is byte-identical, and it prints 26.2bp and "about a quarter".
- `check_gate_c.py`: 418 checks, 0 FAIL, 18 UNVERIFIED, 16 CONDITIONAL. `--self-test` catches 10 of 10.
  `build_sheet_tabs.py` rebuilt the mirrors.
- `numbers.yaml` is unchanged (sha256 492ed320...).
- Not done (outside WS6): the live Sheet tabs still need the re-sync (Gate C open item 7).

## Round 2 (panel at 104476c)

### What changed

- **Pick 1, IBTR (tested), rewritten, and the test now decides the trade.** The note now says "cost", "first
  deposit", "yields fall over about a quarter of a percentage point" and "by January". It gives the consequence: her
  2028 deposit tops up the earliest payments and stocks get less. The curve date ("at 1 Oct yields") is its Friday
  fact, and it opens with "Tested before this first order". If Friday's refresh is above $300,000, the script says
  IBTR TEST FAILS. The team then trades the new `refresh_tickets.py --split-from-curve` ticket (more in the dated
  holdings, less VT) and types IBTR_F (`friday_checklist.md`, "If the IBTR test fails").
- **Pick 2 (refined) is no longer forced.** It is the first of these that exists:
  - SW40 or SW41: a low-coupon bond swapped in on Friday;
  - OD_B: the October swap, only after a stale Friday price;
  - IBTM_R: a new variant, used if the 1 Oct vote adopts the backstop sentence (the half of the stock fund Laura
    keeps, not the floor, covers a shortfall).

  If none exists, the team features IBTM_P as supported. T40b records a constraint and is no longer a pick. **T40c is
  retired** because it would look like a staged trade. The new T40s covers a listed 1.375% bond whose price is stale.
- **One Friday rule for all same-slot alternates** (1 Oct vote): if an alternate is listed and inside its 25bp band,
  swap it in on Friday. This covers the 1.375% Nov 2040, the 2.000% Nov 2041 and the 5.000% May 2037 (new SW37).
  Trigger D now fires only on a new fact, a Friday price that was stale and now passes. It no longer waits on IPS
  wording.
- **No "set amount" on its own.**
  - T39: "held to maturity its set coupons and principal cover most of that payment; reinvesting coupons covers the
    rest".
  - T41: "part of each payment comes from reinvested coupons".
  - The low-coupon notes say "less of her payment rests on reinvested coupons", never "less income".
- **Other exemplars:**
  - IBTP: the check is on the trade date, "we paid a fair price" (not "her money"), and "its end value is not fixed".
  - IBTM_P: "has two jobs" (no "then"), the floor gloss, co-sponsors, and "its end value is not fixed".
  - IBTO: "pays out that December".
  - IBTM_L and OB_B: "its end value is not fixed".
  - T38: "about seven and a half months", "the 4.375% Feb 2038 bond".
  - T37: no untraced comparison.
  - VT: "what Laura's plan has left", "not below the floor", "before 2031", "half the fund stays hers".
  - OB_S: the facility consequence and the full IBTM name, and it is added to PICK_IDS.
  - OC: the floor gloss.
  - SW40 and OD_B no longer say "at about the same cost" (WS1 request 5 first).
- **Checks added:**
  - Numbers written in words are now caught and must be declared, e.g. "a quarter of a percentage point", "almost
    exactly", "most of" (`note_rules.py`; `note_check.py` self-test 6).
  - Every exemplar names its Friday-fact slot, and exemplar plus slot must fit 285.
  - No two notes that can be featured together may open with the same two words (0 found).
  - Outlines are limited to 60 words.
- **Reflections:**
  - The scale sentence goes in pick 1 only. The certainty phrase is used once, in pick 2, and now says "the U.S.
    government owes most of each payment, and the rest depends on reinvesting coupons".
  - Pick 1 names its basis and points to pick 2.
  - Pick 3 carries the research (WS3's fund comparison, quoted after WS1 merges it) and Laura's tolerance.
- **Tickets (a real error):** the Feb-2037 bond's max price (97.940) sat above the top of its 25bp band (97.919).
  `refresh_tickets.py` now caps a bond's max price at the band top and floors its min at the band bottom. Totals are
  unchanged ($294,764.50 and $292,580.89); lowest worst-case cash is $2,445.28 and $4,518.06.
- **Kit docs:**
  - `october_trade.md`: trigger D now needs a new fact, and trigger B names its basis. "The floor gets less" is
    corrected to "the stock fund gets less" (WS4 memo: the gap lands on the stock fund).
  - `M9_selection.md`: the one swap rule. The May-2037 row explains why M9's 1.2% cost gap is not a reason on its
    own.
  - `friday_checklist.md`: the Thursday decisions, the swap flags and the failure branch.
- **Not done (outside WS6):** the live Sheet tabs "RAB Notes" and "RAB Tickets" still show the 104476c texts. The
  local mirrors in `rab/sheets/` are rebuilt; WS0 or Ray re-syncs the tabs.

### Round 2, J1: WGHSIC judge

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | IBTR lacks "cost"; the gap falls on stocks, not a payment | Fixed | "they cost under her $300,000 first deposit"; "her 2028 deposit tops up the earliest; stocks get less" |
| 2 | 26.2bp is the zero-coupon basis; about 22bp on the buyable ladder | Fixed in part | "A quarter" stays, because it is the only locked figure. The brief, the pick 1 outline and a new triage row name the basis. WS1 request 9: if a buyable-basis break-even lands before Friday, the note, reflection and IPS all use it ("about a fifth") |
| 3 | "Tested" changes nothing on Friday; the reflection lacks stakes | Fixed | A failed test now changes the ticket (`--split-from-curve`, IBTR_F). The outline gives the stakes: history (only 2020-21 yields left part of one payment unfunded), who absorbs it, and the 14 Oct result. The odds ("about 1 in 3") come after WS1 merges them (request 10) |
| 4 | "Less income to reinvest" reads as a drawback | Fixed | Every Nov-2040/2041 note says less of her payment rests on reinvested coupons (OD_B's framing) |
| 5 | The refined pick rests on unagreed IPS wording; no fallback | Fixed | Pick 2 is the first of SW40, SW41, OD_B or IBTM_R. Otherwise three honest labels (IBTM_P supported). The outline gives the refinement as a rule going forward |
| 6 | T40c then trigger D is a staged trade | Fixed | T40c retired. Listed and passing means swap on Friday. Trigger D only after a stale Friday price (T40s) |
| 7 | T41 is silent on the 2.000% Nov 2041 | Fixed | The same Friday rule (SW41). The T41 brief adds "WInS lists no lower-coupon bond of that date" if it is not listed |
| 8 | "Set amount" suggests a fixed payment | Fixed | T39 and T41 rewritten in words (84-90% of each bond rung is set coupons plus principal, `reinvest.rung.*`) |
| 9 | Certainty phrase too soft | Fixed | New phrase: "the U.S. government owes most of each payment, and the rest depends on reinvesting coupons". The same reflection names the backstop money once the team decides (triage row 2) |
| 10 | Word budget over 100 | Fixed | Outlines are 60 words or fewer. The scale sentence goes in pick 1 only (73 words with it) and the certainty phrase in pick 2 only (87 words) |
| 11 | IBTP "her money", no caveat, 28 Sep date | Fixed | Trade-date check, "we paid a fair price", "its end value is not fixed" |
| 12 | IBTM_P "then"; why a third; the gloss | Fixed in part | "Has two jobs" plus the full gloss. "About a third" was left out: those characters are kept for the Friday fact (a dated price) |
| 13 | VT has no research; "gets what was left" is loose | Fixed | "What Laura's plan has left" (in her plan the stock fund is all the rest). The pick 3 outline carries the WS3 comparison and "willing to take thoughtful risks" |
| 14 | Picks 1 and 2 share an opening | Fixed | IBTR opens "Tested before this first order", SW40 "We chose the". The new pick-opening check finds 0 shared pairs in any combination |
| 15 | IBTR has no Friday fact | Fixed | "At 1 Oct yields" is inside the note |
| 16 | T37: waiting money, jargon | Fixed | "It is the last WInS bond maturing before then, so it ends about ten and a half months early; what the waiting money and its coupons earn can vary". SW37 covers the listed case |
| 17 | No pick shows the floor or co-sponsors | Fixed | IBTM_R / IBTM_P are the pick-2 routes. The pick 3 outline says the floor is the least she can name to co-sponsors in 2031 |
| 18 | "Curve check" never explained | Fixed | The pick 2 and alternate C outlines explain it: a yield within a quarter of a percentage point of the official curve |
| 19 | IBTQ, IBTO, IBTM_L, OC | Agreed (ignore) | IBTO's "which then closes" was changed anyway (J2 #14) |

### Round 2, J2: Laura and co-sponsors

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | Picks 1 and 2 undercut each other | Fixed | Pick 1 names its zero-coupon basis and points to pick 2. Pick 2 carries the certainty phrase and names who covers a shortfall. The Book L buffer cost is already in numbers.yaml (`reinvest.bookL_buffer_cost`); WS1 requests 9 and 11 add the rest |
| 2 | IBTR: "fall in yields", "first deposit", facility | Fixed in part | The first two are in. "Stocks get less" is used, not "less is left for the facility", to stay within 285; the stock fund is the facility money above the floor, and the reflection says so. The fund name is dropped (WInS shows it) |
| 3 | IBTM_P ranks the floor behind the payment | Fixed | J2's wording, almost exactly |
| 4 | No pick about the floor; no backstop | Fixed | New IBTM_R (J2's text, trimmed), used only if the 1 Oct vote adopts the sentence. The triage row says the decision is due at the vote |
| 5 | T40b is a non-decision | Fixed | J2's wording; T40b is no longer a pick |
| 6 | T40c knowingly buys the worse bond | Fixed | Retired (J1 #6) |
| 7 | SW40/SW41/OD_S framing; untraced cost claim | Fixed | Reframed. "At about the same cost" is dropped until WS1 request 5 |
| 8 | T41/T39 "set amount" | Fixed | J2's T41 clause ("part of each payment comes from reinvested coupons"); for T39, J1's clause, which J1 checked against the kit's own figure |
| 9 | VT: before 2031, flexibility, cash, bare 9% | Fixed | All four. The 9% moves to the reflection |
| 10 | OB_S: facility consequence; not in PICK_IDS | Fixed | "Leaving less for the facility"; added to PICK_IDS; the pick anchor passes |
| 11 | IBTP | Fixed | J1 #11 |
| 12 | Pick 1 outline: the Friday test is nearly a formality | Fixed | The outline leads with the rule set in advance, the history figure and who absorbs a gap. The 4.5bp standard deviation is not quoted |
| 13 | IBTM_L "with its income reinvested" | Fixed | "Its end value is not fixed" |
| 14 | IBTO "which then closes" | Fixed | "A fund of 2033 Treasuries that pays out that December" |
| 15 | T38 is about data only | Fixed | J2's text, with J3's coupon ("the 4.375% Feb 2038 bond") and "seven and a half months" (231 days; "about seven" would round down) |
| 16 | OC has no floor gloss | Fixed | Gloss added |
| 17 | IBTQ, IBTO, IBTM_L, T37 listing-gap reasons | Agreed (ignore) | Under R1(a) the listing gap binds Laura's plan too |

### Round 2, J3: fact-checker

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | IBTR threshold stated as the effect; "re-priced her payments" | Fixed | "Over about a quarter", "cost", "tops up the earliest", "by January" |
| 2 | A failed test has no consequence for the trade | Fixed | The Friday branch (`--split-from-curve`, IBTR_F) and a script warning |
| 3 | IBTP date and "her money" | Fixed | The trade-date re-run. Its Gate C claim is CONDITIONAL on that re-run. WS1 request 2 |
| 4 | T37: untraced comparison; the T38 rule picks May 2037 | Fixed; rejected in part | SW37 under the one Friday rule, and the default T37 has no comparison. **Rejected:** "about 1.2% cheaper". M9 prices the May 2037 bond at the model and the Feb 2037 bond at a WInS price 15bp rich, so the gap is mostly that richness. The swap rests on timing (three months nearer) and the same share at 2% |
| 5 | Feb-2037 max price above the band top | Fixed | Cap in `refresh_tickets.py`; tickets regenerated |
| 6 | VT "only"; "a rise lifts the top" | Fixed | "Not below the floor"; "before 2031" |
| 7 | IBTM_P: "covers", "then", "in Laura's plan" | Fixed; rejected in part | "Covers" and "then" are gone. **Rejected:** "only WInS's stand-in". Under the adopted reading R1(a), her real plan is limited to WInS-listed securities, and none matures in late 2032, so IBTM is her floor holding too. The brief and triage row that said otherwise are corrected |
| 8 | T38 name, quote_as wording, date label | Fixed | "The 4.375% Feb 2038 bond"; the number is dropped, so the quote_as mismatch is gone. The brief says "the 28 Sep close, seen in WInS 29 Sep" |
| 9 | T40b records no change | Fixed; rejected in part | T40b is no longer a pick. **Rejected:** J3's policy-clause T40b. The policy route is IBTM_R (J2), which also shows the floor; a second variant would duplicate it |
| 10 | SW40/OD_B cost claim not in numbers.yaml | Fixed | Removed until WS1 request 5 |
| 11 | T41 range and "set amount" | Fixed | "From 2037 to 2043"; "part of each payment comes from reinvested coupons" |
| 12 | The checker ignores numbers in words | Fixed | Word-quantity patterns in `note_rules.py`, declared per note; the self-test catches an undeclared one. The Gate C self-test also breaks a word quantity (9 of 9 caught) |
| 13 | Uncommitted ws7 ticket edits | Passed to WS0 | WS6 cannot edit ws7. New triage row: WS0 picks the final tickets before Friday, then `build_notes.py` is re-run (it checks note order against `tickets.csv`) |
| 14 | No room for the Friday fact | Fixed; rejected in part | Each exemplar names its slot and the build checks exemplar + slot against 285. Most hold the fact already, or swap in the WInS name at no cost. **Rejected:** a 255-character cap everywhere, which would cut content with no gain |
| 15 | "Three different jobs" credited to the TN guide | Fixed | Now labelled a kit rule (PM-19), separate from the official rules |
| 16 | OB_S/OB_B names, caveat, basis | Fixed; rejected in part | Full IBTM name, OB_B caveat, and trigger B's basis in `october_trade.md`. **Rejected:** VT's full name in OB_S. The note sits on the VT sale, where WInS shows the name, and it would push the note past 285 |
| 17 | IBTM_L unqualified | Fixed | J2 #13 |
| 18 | IBTN claim too broad | Fixed | "No iShares iBonds Treasury fund uses the ticker IBTN" |
| 19 | Basis for the Final Report | Fixed | Triage row (note-in-Final-Report), WS1 request 9 |
| 20 | "A day early" | Fixed | "About a day and a half early" |

### Checks after round 2

- `build_notes.py`: 23 exemplars, the longest 285 characters, 0 fail. This covers:
  - IPS quotes verbatim;
  - outlines at 60, 59 and 60 words;
  - variety;
  - pick openings (0 shared);
  - note order against `tickets.csv`.
- `note_check.py --self-test`: PASS (6 tests).
- `refresh_tickets.py`: 83 pass, 0 fail.
- `check_gate_c.py`: 365 checks, 0 FAIL, 18 UNVERIFIED, 16 CONDITIONAL. Its `--self-test` catches 9 of 9.
- `numbers.yaml` is unchanged (sha256 492ed320...).

## Round 1 (panel at c11b02f)

Kept as the record of round 1. Where rounds 2 and 3 changed a round-1 answer (T40c, the IBTR wording, the certainty phrase, the outlines' 70-word limit), round 2 wins.

### Round 1: what changed

- **Picks rebuilt.** Pick 1 **tested** is IBTR: before the first order the team re-prices the ten payments against
  Laura's $300,000 deposit. That IPS claim fails if yields fall about a quarter of a percentage point, and the 14 Oct
  check runs it again. Pick 2 **refined** is whichever Nov 2040 note is typed (SW40, T40b or T40c; OD_B if trigger D
  fills): the coupon-reinvestment discovery plus the IPS wording it changes. Pick 3 **supported** is VT. Alternates:
  IBTM (floor), the Nov 2039 bond (certainty), the May 2038 bond (price check).
- **VT is order 11**, placed Mon 5 Oct ET once the five bonds show Filled, so Order History shows payments and floor
  before growth. `refresh_tickets.py` has a new `--cash-before-vt` option: VT gets the plan share, trimmed if cash would
  fall below $1,000. Also changed for this: the `tickets.md` order text (cash control only, no IPS clause),
  `friday_checklist.md` (a Monday step) and `trades_clock.py` (Monday times; the 9:45 row relabelled). Ticket totals are
  unchanged: $294,764.50 and $292,580.89, and all 83 checks pass.
- **T40 retired.** T40b is the default note for order 7 and SW40 covers the swap. A new T40c covers the case where the
  bond is listed but kept for October.
- **Every exemplar rewritten or checked:** exact fund names, a gloss on "facility floor", which of her ten payments,
  short caveats that vary from note to note, and no IBTN step inside a note. IBTP now uses a premium-to-NAV test and T38
  says "percentage point of yield". Two dates are fixed: T37 is "ten and a half months" and T39 is "about seven weeks".
- **New checks:**
  - The Laura anchor no longer accepts a bare year.
  - Featured notes must name the residency, co-sponsors or which of her ten payments (`note_check.py --pick`).
  - A variety check: at most 3 of the 11 Portfolio notes may share an opening, and at most 2 an ending.
  - Outlines are limited to 70 words.
  - A 25-49% overlap with an exemplar is no longer a pass.
- **Reflections:**
  - Each one carries the scale sentence ("Our WInS portfolio is Laura's plan after both deposits, scaled down to
    $300,000.") and what was checked after Friday.
  - The certainty phrase is used once, with its condition.
  - The strategy name is used once, if Ray confirms it.
- **Fact fixes:**
  - The iShares quote now reads its iBonds funds "do not seek to return any predetermined amount".
  - Accrued interest now reads "1.66 on 28 Sep (1.71 on 2 Oct)" in notes, tickets and M9.
  - M9 no longer says no later bond exists for the 2038 payment. The 5.000% May 2037 bond does.

### Round 1, J1: WGHSIC judge

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | No real test or refinement in the picks | Fixed | IBTR tested, Nov 2040 note refined, VT supported; IBTM is alternate A (supported) |
| 2 | IBTM is not a refinement; its limit is unmeasured | Fixed | Relabelled supported. The brief measures the limit (about 97% if income is reinvested at 2%, `reinvest.rung.IBTM`), to be quoted only after WS1 adds a quote_as (request 4). If the team keeps 'refined', the outline says what must be named |
| 2a | "The MSPD Table V file covers bonds only, so late-2032 notes are UNVERIFIED" | Rejected | The kit's MSPD file lists notes: 4.125% 15 Nov 2032 (91282CFV8) and 3.75% 30 Nov 2032 (91282CPM7). This is now in the IBTM brief and in s7 |
| 3 | May 2038 'tested' checks data, not strategy; 25bp band not justified | Fixed | Now alternate C. Its outline ties the check to the IPS cost claim. The brief justifies the band: good prices sat 2-15 hundredths of a point of yield off, stale ones 92 and 111 (`wins.bond_check.*`). WS1 request 6 |
| 4 | VT shows as trade 6 of 11, before the bonds | Fixed | VT is now order 11, on Mon 5 Oct ET, after the bond fills (see "What changed") |
| 4a | Size VT from all cash above the float | Rejected in part | VT keeps the typed 8.7% plan share, trimmed only if cash is short. Raising it would change the Sheet's split, and spare cash is October trigger C's job |
| 4b | VT note: tolerance clause and floor gloss | Fixed in part | The note has the floor gloss. The tolerance ("willing to take thoughtful risks", Client Profile p.2) is in the VT brief and outline, because the box space went to the exact name (J3) and the upside (J2) |
| 5 | Scale ambiguity ($21k holding against a "$50,000 payment") | Fixed | Every reflection carries the scale sentence (Book L has its own). No ratio is quoted (WS1 request 8) |
| 6 | T40 "we are checking" is false once the order is placed | Fixed | T40 retired; T40b is the default, T40c covers listed-but-kept, and the "say 'we are checking'" instruction is gone |
| 7 | IBTR should carry the quarter-point figure | Fixed | It is the note's one number. "Role: future funding and risk management" was not used: it needs space the test uses |
| 8 | IBTP: the yield comparison does not show a fair price; false precision | Fixed | The note uses the premium to NAV (0.06% on 28 Sep) in words. The brief re-runs it on Friday. A figure needs a quote_as first (WS1 request 2) |
| 9 | IBTO spends the box on the IBTN mix-up | Fixed | The name check moves to the Trade Log and the Final Report. The note gives the payment and what the fund holds |
| 10 | T37 gives no reason for the Feb 2037 bond | Fixed | It is "ten and a half months" early. The 5.000% May 2037 bond, the only later bond of this class (MSPD), comes out the same once coupons count (M9). If WInS lacks it, a Friday sentence swap applies |
| 11 | T39 is a textbook sentence | Fixed | One clause on price, plus its fit to the date (about seven weeks before the payment). Now alternate B for certainty |
| 12 | T38 "about 1 point of yield" | Fixed | Now "almost a full percentage point of yield", dated 29 Sep; WS1 request 3 aligns the quote_as |
| 13 | Boilerplate openings and caveat tails | Fixed | Openings and endings vary, enforced by the variety check. Every brief gives a Friday fact, and 25-49% overlap is "not a pass" |
| 14 | "Facility floor" used without definition | Fixed | Glossed as "the least she plans to give" in IBTM_P, VT and the outlines; this is also an s1 rule |
| 15 | `tickets.md` order reason contradicts `notes.md` | Fixed | In the `refresh_tickets.py` template: the order is for cash control only, and it says so |
| 16 | Conditional notes: OD_B/SW40 cost, OC reason | Fixed | SW40 and OD_B say "about the same cost on today's curve" (M9, MODEL, no figure; WS1 request 5). OC now uses Laura's plan instead of the cash-interest reason. OB_S unchanged |
| 17 | Strategy name kept out of the reflections | Fixed | Reflections may use it once if Ray confirms by 22 Oct. WInS notes still leave it out (triage row) |
| 18 | Outlines are already at 100 words | Fixed | Now 68, 69 and 70 words, with the IPS paraphrased and room left for the scale sentence and the after-Friday result. build_notes.py enforces 70 |
| 19 | IPS "just before" disagrees with the notes | Triaged | fix-before-6-Nov, merged with the "matched" row. Wording only; the team decides |
| 20 | IBTQ, T41 and IBTM_L need no change | Agreed | IBTQ and T41 lightly edited to lead with Laura (J2 #9) |
| 21 | "1 Jan" payment dates | Agreed | No change |

### Round 1, J2: Laura's side

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | No pick says why the payments are highly certain | Fixed | IBTR tested (re-pricing against $300,000), T38 moved to alternate, T39 is the certainty alternate |
| 1a | Put "about $292,000" in the IBTR note | Rejected in part | A note may hold one number, and $292,000 moves at the Friday re-lock, which may land after the orders. The note states the result in words ("under her $300,000 deposit") plus the threshold, and the reflection quotes Friday's figure |
| 2 | IBTM note should name the floor for co-sponsors and bound its limit | Fixed | The note uses the floor "that she can name to co-sponsors in 2031" and puts the payment before the floor. The real-account notes (MSPD) and the iShares limit are in alternate A |
| 3 | VT: no upside, no flexibility | Fixed | The note says "a rise lifts the top of the range co-sponsors hear". The cushion (half stays with her) and the cap are in the brief and outline |
| 4 | T38 draft "about 8% too high" | Rejected | The figure is not in numbers.yaml, and the clean-price gap is 8.5% (99.98 against 92.183). The yield wording is kept; WS1 request 3 |
| 5 | Kit rules removed co-sponsors and certainty; the Laura anchor is too weak | Fixed | s2 bans only 2031 dollar figures and encourages the ideas. The Laura anchor drops bare years and adds residency, and a pick-anchor check is added. Reflections use "high degree of certainty" once, with its condition |
| 6 | Repeated "must be reinvested" tail | Fixed | Short, bounded phrases that vary by holding |
| 6a | Wording "only what its coupons earn can vary" | Rejected | This overclaims (J3 #11): money waiting between maturity and payment also earns an unknown rate. The certainty phrase names both |
| 7 | IPS does not say which money covers a reinvestment shortfall | Triaged | fix-before-6-Nov, wording only: about $20,000 at 2% against about $7,600 of headroom (`reinvest.bookL_buffer_cost`, `laura.ladder.headroom_2027_strips`) |
| 8 | Delete T40 | Fixed | Retired |
| 9 | IBTO, IBTQ, IBTM_L, T41 and IBTP lead with process | Fixed | Each now leads with which of her payments (or the residency) and gives availability second |
| 10 | "Her artists' first payment"; scale sentence missing | Fixed | That outline is gone and no outline mentions artists. Every reflection has the scale sentence |
| 11 | Decide the low-coupon swap on its merits | Fixed | `friday_checklist.md` Thursday item: swap if listed and passing. It names which Nov 2040 note gets typed; SW40 becomes pick 2 if swapped. Figures wait for WS1 request 5 |
| 12 | Book L hides the floor and growth | Fixed | Stated as a Laura-lens reason at the 1 Oct vote (`friday_checklist.md`, s6) |
| 13 | Keep OB_S, OB_B and OD_B | Agreed | OB_S unchanged; OB_B gets J3 #14; OD_B gets the cost clause |

### Round 1, J3: fact-checker

| # | Point | Verdict | What changed, or why not |
|---|---|---|---|
| 1 | T40 sentence false; "the rate its coupons earn" | Fixed | T40 retired. The listed-not-swapped case is T40c, built on J3's idea. The wording is now "income to reinvest" |
| 1a | Use J3's replacement text as the default T40 | Rejected | The note is true only when the bond is listed but not swapped, so it is the T40c variant, not the default |
| 2 | IBTR "any gap falls on her first payment" | Fixed | Now "the earliest", with the exact fund name |
| 3 | IBTP fair-price logic | Fixed | Premium to NAV (J1 #8) |
| 4 | `tickets.md` order statements; the 9:45 row | Fixed | VT is now last in fact, the IPS clause is removed, and the 9:45 row reads "earliest any order may go in, only if Plan A cannot wait" |
| 5 | iShares misquote | Fixed | Checked against `rab/data/ishares/IBTM_product_page.html.gz`: "the Funds do not seek to return any predetermined amount" |
| 6 | Exact security names | Fixed | IBTM_P, VT, IBTQ, IBTP, IBTM_L, OB_B and OC. The WInS strings for IBTO-IBTR stay UNVERIFIED, and each brief says to copy them on Friday |
| 7 | T38 "1 point"; "that day's curve" | Fixed | "Almost a full percentage point of yield", "the latest official curve", and the stale reading is dated |
| 7a | Write "0.9 of a percentage point" | Rejected | That needs a quote_as change before Friday. J1's number-free wording says the same |
| 8 | Pick 1 label contradicts its outline; "artists" | Fixed | IBTM is supported. The refinement (the IPS certainty wording) moves to the Nov 2040 pick |
| 9 | T38 test never changed the decision | Fixed | Demoted; IBTR is the tested pick |
| 10 | VT outline misstates the IPS tradeoff | Fixed | Now "more stock widens the range and shrinks the floor co-sponsors hear in 2031" |
| 11 | T39 "only" and "we hold"; "income earns only 2%" | Fixed | "Her plan holds it to maturity", no "only", and the briefs say "reinvested at only 2%" |
| 12 | T37 "ten months" | Fixed | "Ten and a half months" |
| 13 | IBTO | Fixed | The IBTN check is out of the note |
| 13a | Keep the IBTN parenthetical (J3's text) | Rejected | Two judges ask to move process out of the note. It goes to the Trade Log and the Final Report instead |
| 14 | OB_B "as our plan expects"; shortened names | Fixed | "As our plan allows", with the full IBTM name |
| 14a | Tighten OB_S | Rejected | Kept as written because J1 and J2 scored it 3 of 3. The brief says to write "the earliest payments" if a refresh ever shows a gap beyond the first payment |
| 15 | Two 30-day averages; the "so far" reading | Fixed in part | "So far" is marked UNVERIFIED in `tickets.md`. Relabelling numbers.yaml belongs to WS1 (request 7), and there is no trading impact |
| 16 | Accrued 1.66 against 1.7 | Fixed | "1.66 on 28 Sep (1.71 on 2 Oct)" in notes, tickets and M9 |
| 17 | New iBonds funds "every March" | Fixed in part | Logged as note-in-Final-Report (UNVERIFIED). "Every March" is inaccurate: only IBTQ (25 Mar 2025) and IBTR (25 Mar 2026) launched in March, while IBTP launched Jun 2024 and IBTO Jun 2023 (iShares list, 30 Sep) |
| 18 | "Role:" prefix is style only | Superseded | Openings vary under J1 #13; no rule forces a prefix |

### Checks after round 1

- `build_notes.py`: 20 exemplars, the longest 285 characters. All pass, and the build ends with 0 fail. That covers:
  - the IPS quotes, verbatim against the 30 Sep snapshot;
  - outline length (68/69/70 words);
  - variety;
  - note order against `tickets.csv`.
- `note_check.py --self-test`: PASS (5 tests, including the new `--pick`).
- `refresh_tickets.py`: 83 pass, 0 fail. Totals are unchanged, and C5 matches numbers.yaml to the cent.
- `numbers.yaml` is unchanged (sha256 492ed320...).
