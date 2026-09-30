# Response to the WS6 notes judge panel (30 Sep 2026)

WS6-revise, RAB Kit, 30 Sep 2026 (Sydney). AI-generated (Claude Code, Claude Opus 5.5) for Team Caplet. It covers
three panels that reviewed `notes.md` at c11b02f: J1 (WGHSIC judge, self-scoresheet scale), J2 (Laura's side) and J3
(pedantic fact-checker). Each point below is either fixed or rejected with a one-line reason. **The strategy is
unchanged.** The IPS, the Sheet and `numbers.yaml` were not edited; IPS wording items are triaged for the team (`notes.md`
s7), and new figures are requested from WS1 (`notes.md` s7, "Requests to WS1").

## What changed

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

## J1: WGHSIC judge

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

## J2: Laura's side

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

## J3: fact-checker

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

## Checks after the revision

- `build_notes.py`: 20 exemplars, the longest 285 characters. All pass, and the build ends with 0 fail. That covers:
  - the IPS quotes, verbatim against the 30 Sep snapshot;
  - outline length (68/69/70 words);
  - variety;
  - note order against `tickets.csv`.
- `note_check.py --self-test`: PASS (5 tests, including the new `--pick`).
- `refresh_tickets.py`: 83 pass, 0 fail. Totals are unchanged, and C5 matches numbers.yaml to the cent.
- `numbers.yaml` is unchanged (sha256 492ed320...).
