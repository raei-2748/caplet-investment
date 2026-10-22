# TNA mock judge panel: section A of current_draft_21Oct.md (IBTM, VT, IBTR)

AI-generated review (Claude Code, Wed 21 Oct 2026, Sydney). **Not for submission.** These are scores, problems and
requirements, not wording. The team writes every sentence. Log this review in `office/LEDGER.md` and in the AI-use log.
The four judges are AI personas, not real judges. Scores are AI opinion.

**What was judged:** the three "Rewritten" reflections in section A of
`SP/oct21/tna/current_draft_21Oct.md` (lines 7-20; Doc read 21 Oct ~18:10 Sydney). SP =
`/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad`.

**Sources** (short names used below)
- TNA = `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt`; GUIDE = `.../2026_WGY_Investment_Competition_Guide.txt`;
  CASE = `.../Laura_Gao_2026_Client_Profile.txt`; DELIV = `.../smapply_public_2026-10-14/deliverables.txt`; FAQ14/FAQ20 =
  `.../smapply_public_2026-10-14/faqs.txt` / `-10-20/faqs.txt`.
- V5 = IPS Report Doc, tab "Version 5", `SP/oct19/drive/ips_report_live.md:23-30` (each paragraph holds a pending v12
  run and an accepted v11 run; labels as in KIT).
- KIT = `SP/oct20/out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md`; WNX = all eleven filled notes, `SP/oct19/drive/ips_report_live.md:107-117`.
- ISH = iShares IBTM page, `SP/oct19/tnakit/web/ibtm_ishares_2026-10-19.txt:849-850` (the iBonds termination and payout disclosure).
- RUB = `SP/oct20/rubric/rubric_scoring.md`; PW = `SP/oct20/pastwinners/past_winners_deep.md`.

**Counts** (`office/tools/textcheck.py`, run 21 Oct): IBTM 94/95 words (spaces/strict), VT 99/99, IBTR 99/99. All pass 100,
but **VT and IBTR are 1 word under the limit**, so any fix that adds a word breaks the limit. Curly quotes in the
reflections are fine; only the notes must match WInS exactly.

**A note on the brief's wording.** "How those decisions ultimately shaped the IPS" is **not in the official text**:
there is no match in `competition/official/2026_27/`. The official equivalents are "supported, tested, or refined
your overall investment strategy" (TNA:29-30; GUIDE:88-89) and "consistent with the strategic approach your team is
developing and will later articulate in its IPS" (TNA:30-31). The "purpose" score uses those. The Doc's prompt says
"goals, objectives, or constraints" (`ips_report_live.md:69`), but the official words are "goals, funding needs, or
risk considerations" (TNA:52).

**Scale (1-10, every dimension):** 5 = competent finisher; 7.5+ = Top-50 contention; 9+ = finalist (bands as in RUB §3b).
Columns: **E** = three required elements; **P** = purpose (supported/tested/refined, IPS link); **C** = client knowledge;
**Cl** = clarity/plain English; **Co** = consistency with IPS V5 and the filed note.

---

## Judge 1: Wharton finance faculty (scored first, independently)

*Lens: are the concepts right? Does each reflection show a decision rule and its test, or just describe a holding?
Would a fixed-income colleague wince?*

| Reflection | E | P | C | Cl | Co | Mean |
|---|---|---|---|---|---|---|
| IBTM | 6 | 6 | 5 | 6 | 4 | 5.4 |
| VT | 6 | 4 | 5 | 7 | 3 | 5.0 |
| IBTR | 6 | 3 | 6 | 5 | 5 | 5.0 |
| **Set** | | | | | | **6** |

- **IBTM.** This is the only reflection that shows a change: a rule arrived and the plan moved. That is the right
  instinct. But S4 then says the fund "has a clear yield, and matures on a set date". The filed note says "the final
  payout is not fixed", and the issuer says the funds "do not seek to return any predetermined amount" and terminate
  "on or about" 15 Dec (ISH:849-850). So the reflection contradicts its own note, and I would mark the concepts down for
  it. Nothing explains why one holding can do both jobs (both fall due at the start of 2033, KIT 3D).
- **VT.** "About 7.5% a year per JPMorgan" is not the IPS assumption: V5 says "assumed to return 7% a year"
  (V5:27, both runs). The J.P. Morgan 2026 LTCMA gives AC World 7.00% and EAFE 7.50% (`CLAUDE.md:153-154`), so the
  reflection appears to quote the wrong asset class (where 7.5 came from is UNVERIFIED). S1 says VT "diversifies the
  portfolio". It diversifies the equity sleeve. The portfolio is about 90% one issuer by design (KIT 3E; V5:27
  "Concentration in one issuer is deliberate").
- **IBTR.** The note did the hardest thing in the set: it wrote a test before the trade ("more than about 0.2
  percentage points by January", WNX:108). The reflection never says what happened to that test. Its last sentence
  restates the note with the threshold removed. S1's "2036 Treasuries that mature in December 2036" is wrong: the
  fund *terminates* around 15 Dec 2036 and its bonds mature through 2036 (ISH:849; KIT 2C, holdings list not
  re-checked). S4's "which serves her operating commitment 'with a high degree of certainty'" does not follow from
  "most rate-sensitive".
- **Set.** It covers the payments, the floor and growth well. It is weak on "tested": the one test on record goes
  unreported.

## Judge 2: practising wealth manager, CFA charterholder (scored second, independently)

*Lens: suitability, honesty with the client, overpromising, fees, concentration, liquidity. Would I let this go to a
client file?*

| Reflection | E | P | C | Cl | Co | Mean |
|---|---|---|---|---|---|---|
| IBTM | 6 | 5 | 4 | 6 | 4 | 5.0 |
| VT | 6 | 4 | 5 | 7 | 3 | 5.0 |
| IBTR | 6 | 4 | 6 | 6 | 5 | 5.4 |
| **Set** | | | | | | **6** |

- **IBTM.** "So a stock crash will not make her promise fail" is a compliance red flag. "Promise" is the word the case
  warns about ("If Laura promises more than she can ultimately contribute, she could damage her credibility",
  CASE:114). The case asks for a "credible range" (CASE:116). "Will not" is an absolute about a fund whose payout is not
  fixed. The protection is real (a stock crash does not touch IBTM), but it is stated as a guarantee. "Cheap, easy to
  trade" is generic: it is true of most ETFs and says nothing about Laura. There is no liquidity point, though this is the
  one holding where cash arrives about 17 days before a payment (KIT 3F).
- **VT.** S2 is the best client sentence in the set: the equity is small *because* the payments come first. S5
  says "the other half stays Laura's". To a client that reads as money leaving the portfolio, but if that half backs
  payments it must stay inside it (CASE:91-92). "Covering a payment shortfall" from her half is a model claim: at the
  5th percentile her half is $0 (KIT D1; MODEL, 19 Oct). The note says VT's value "only" sets the top of the range
  (WNX:107). The reflection gives it two more jobs without saying the note understated them.
- **IBTR.** S2 (five iBond funds for payments 1-5, single bonds for 6-10) is the clearest structural fact in the TNA.
  A client could check it. S5 names the trade-off between the two goals, which suits the case's priority order
  (CASE:94). But it does not say which part of the facility money shrinks, the floor or the stock fund (KIT D4).
- **Set.** It is honest in spirit. But "promise", "stays Laura's" and the wrong 7.5% would each draw a question.

## Judge 3: former Top-50 high-school finalist (scored third, independently)

*Lens: what separates a Top-50 TNA. Does each 100 words earn its place? Is there a before/after story? Could any team
that bought VT have written this?*

| Reflection | E | P | C | Cl | Co | Mean |
|---|---|---|---|---|---|---|
| IBTM | 6 | 7 | 5 | 6 | 5 | 5.8 |
| VT | 5 | 3 | 4 | 7 | 4 | 4.6 |
| IBTR | 5 | 3 | 5 | 6 | 5 | 4.8 |
| **Set** | | | | | | **5** |

- **IBTM.** This is the strongest of the three: an early plan, a rule change, a response. The only public Top-50 TNA
  did the same (it quoted an early weak note and then a rule-based one, PW §2.1 row 5 and §3 table). It loses points
  because about a third of the words (S4) are a generic list. It also never says what the change did to the IPS
  (the floor became the bottom of the 2031 range, rounded down, V5:29).
- **VT.** Generic. Any team with VT could write S1-S3. The Caplet-specific parts are "half of VT's value is added to
  that bound" and the backstop. The team's real debate (Darren's 5 Oct "copout" challenge, EWT and GLD raised, KIT
  1D; outcome not recorded) would be the "tested" story, but only if the team really decided it and logs it.
- **IBTR.** It wastes the set's best material. The note set a numeric test on 6-7 Oct and yields then moved toward it
  (the long end fell about 0.12-0.16 points to 19 Oct, KIT 2E; MODEL room on basis D was 9.8bp on 19 Oct). A
  finalist reflection would report that. This one restates the note instead.
- **Set.** One decision shows refinement (IBTM). One should show testing (IBTR) but does not. One is aligned only
  (VT). Two of three spend a sentence restating their note.

## Judge 4: smart non-finance outsider (scored fourth, independently)

*Lens: can I follow it without a finance degree? Do I believe it? Does it sound like teenagers who understand their
plan?*

| Reflection | E | P | C | Cl | Co | Mean |
|---|---|---|---|---|---|---|
| IBTM | 6 | 6 | 5 | 5 | 5 | 5.4 |
| VT | 7 | 5 | 6 | 7 | 5 | 6.0 |
| IBTR | 6 | 4 | 6 | 5 | 6 | 5.4 |
| **Set** | | | | | | **6** |

- **IBTM.** "Zero-coupon Treasuries", "iBond" and "root" are never explained, and the TNA is read before the IPS
  arrives. "Despite favouring X, we abandoned X because..." is a muddle: "despite" signals a contrast that is not
  there. The note says the payout is not fixed, but the reflection says the fund has a clear yield and a set date.
  Which is it?
- **VT.** This is the easiest to read. I understood that it is small on purpose and why. I could not tell what "9% of
  the portfolio" is 9% of. The note says VT "only" sets the extra, but the reflection says half of it can also cover
  payments. I noticed the difference.
- **IBTR.** "Most sensitive to interest rates" means nothing to me, and nothing explains it. "If yields fall,
  the ladder may cost more than $300,000": by how much would they have to fall? The note gave a number and the
  reflection dropped it.
- **Set.** The "root/branch" words tie the three together nicely. All three use the same words, so they read as one plan.

---

## Per-reflection teardown

### Reflection 1: IBTM (note 10/06/2026 10:01:41 PM ET, WNX:112)

Sentences: S1 "Despite favouring ... securities listed on WInS." S2 "WInS also lists no individual Treasury maturing in
2032." S3 "IBTM therefore became ... first $50,000 payment." S4 "As the 'root' ... matures on a set date." S5 "Laura's
second deposit ... her promise fail."

**5 worst problems, ranked**
1. **S4 contradicts the filed note.** "Has a clear yield, and matures on a set date" sits beside a note that says "the
   final payout is not fixed" (WNX:112), and against the issuer: "on or about ... December 15", "do not seek to return any
   predetermined amount" (ISH:849-850). It also contradicts V5's own reason for rounding the floor down (V5:29, both
   runs).
2. **S5 overclaims in the case's danger word.** "Promise" and "will not make her promise fail" are absolutes. The case
   frames the 2031 figure as a "credible range" and warns about promising (CASE:114-116). Accepted V5 has "Promise only
   what is owned" (V5:29), so the team must decide this jointly with the IPS (KIT D6).
3. **The IPS link is missing.** The reflection never says what the change did to the strategy: the floor is the
   lower bound of the 2031 range, rounded down because the payout is not fixed (V5:29). This is the "refined" half of
   the instruction (TNA:29-30).
4. **S1's causation is shaky and undated.** The public FAQ already said "Investments permitted (for BOTH
   contributions)" in the 14 Oct snapshot (FAQ14:42). KIT 3D says the insight_v1 register quoted it on 27 Sep. The
   email's text and arrival time are UNVERIFIED (KIT 3G). IBTM was the WInS choice from 29 Sep anyway, so the email
   changed Laura's real plan, not this trade (KIT 3G). A Wharton reader may ask why the team planned a security that
   the FAQ now lists as "NOT permitted" (FAQ20:54-55). The reflection must make clear which plan changed, and when.
5. **No "why one holding, which job first".** It does not explain why one fund serves both the first payment and the
   floor (both fall due at the start of 2033, KIT 3D), or that the payment shares come first (KIT 3B: 1,142 for the
   payment, 3,361 for the floor). Liquidity (cash about 17 days before 1 Jan 2033, KIT 3F) is the trio's only chance at
   Wharton's "liquidity" theme (TNA:5), and it is unused.

**Filler or restating the note**
- S3: it restates the note's first job ("supports her first $50,000 payment"). The new content is only "therefore became".
- S4: generic attributes ("cheap, easy to trade") that fit almost any ETF; the other two are wrong (problem 1).
- S5, middle clause "to ground a minimum for her facility contribution": it restates the note's second job. The new
  content is "Laura's second deposit buys a second batch", which is good (V5:27).

**Claims a judge would doubt**
- "because Wharton's week 2 email limited..." (S1): see problem 4. "Week 2" is unverified as Wharton's label.
- "the best alternative" (S3): no alternative is named, so "best" is asserted.
- "has a clear yield", "matures on a set date" (S4): see problem 1.
- "easy to trade" (S4): plausible ($593m net assets on 16 Oct, KIT 3C), but unsupported here.
- "a stock crash will not make her promise fail" (S5): true for a stock crash. But a yield fall before Jan 2027 can
  shrink the floor through a ladder top-up (MODEL about $137-138k after a half-point fall, KIT D3). The IBTR reflection
  says exactly that ("the facility contribution is lower"). One sentence on when the floor is fixed (bought Jan 2028,
  after any top-up) would clear it.
- "a second batch of IBTM": the judge sees one WInS order of 4,503 shares. The WInS-is-scaled statement appears
  nowhere in the TNA (KIT D6).

**What a Top-50 reflection would do that this does not** (requirements only)
- State the before, the cause (dated and sourced) and the after, and say which plan changed: Laura's real plan, not
  the WInS trade.
- Show the consequence for the IPS: the floor's role as the range's lower bound and the rounding principle (no dollar
  figure, TNA:20-22).
- Name the "not fixed" risk and the rule that handles it, instead of claiming certainty.
- Explain why one holding serves two jobs and which job is served first.
- Tie the floor to the case's credibility concern in the case's terms, with no absolutes.
- Optional: use the liquidity timing.

**Student-written or AI-polished?** Mostly student, built on an AI frame.
- Student signs: the faulty "Despite ... we abandoned" construction; "ground a minimum"; "a second batch"; the
  unparallel four-item list; British "favouring".
- AI-lineage signs: 18 of 95 words sit in runs of 4+ words shared with the [AI] IBTM text (section C), including the
  whole of S2 ("lists no individual Treasury maturing in 2032"), "portfolio to securities listed on WInS" and "her first
  $50,000 payment". S1-S3 follow the [AI] text's order (rule, then no 2032 bond, then IBTM became...).
- Forensic risk: moderate. S2 is a verbatim AI sentence.

### Reflection 2: VT (note 10/07/2026 08:27:19 PM ET, WNX:107)

Sentences: S1 "Our choice of VT diversifies ... stock picking." S2 "We intentionally kept ... Laura's payments." S3 "VT is
the 'branch' ... the part that grows." S4 "Its expected return, about 7.5% ... added to that bound." S5 "The other half
stays Laura's ... iBond payouts fall short."

**5 worst problems, ranked**
1. **7.5% is wrong for this fund and contradicts the IPS.** V5 assumes 7% (V5:27, both runs). 7.00% is JPM's AC World
   figure, and 7.50% is EAFE (`CLAUDE.md:153-154`). Two numbers for the same assumption across the deliverables, which
   are judged together (CASE:161-162), breaks the IPS-consistency criterion (DELIV:55). It also presents a 10-15-year
   forecast as an "expected return" for a holding kept from 2028 to 2033.
2. **It silently contradicts its own note.** The note says the stocks "only set how far her gift rises above her
   promised minimum" (WNX:107). S5 gives Laura's half two more jobs (flexibility; covering a payment shortfall). The
   reflection is where the team can show it *refined* VT's role, but it does not say the note understated it. It also
   leaves the note's "gift" and "promised minimum" uncorrected (CASE:116, "credible range"; KIT 1H).
3. **"Stays Laura's" moves the backstop outside the portfolio.** If her half covers payments, it must remain portfolio
   money (CASE:91-92). As written, it reads like the V5 trap "covered by her other assets" (V5:25 accepted run; RUB
   §3d red flag). Which IPS run is kept also decides whether "flexibility" is one of VT's jobs at all: it is only in the
   pending run (KIT D1).
4. **No decision content.** It never says why one world fund rather than the alternatives the team actually raised
   (Darren's 5 Oct challenge, EWT, GLD; KIT 1D, outcome not recorded), why the split is half and half, or why VT was
   bought last (order #11, after every payment holding, KIT 1B). That sequence *is* the strategy (payments, then floor,
   then growth, V5:27).
5. **"9% of the portfolio" is unanchored.** It is the WInS share at cost (8.84%, KIT 1B). Laura's real plan is about 7%
   (MODEL, KIT 1C). V5 says "under one tenth". The judge cannot tell which portfolio is meant.

**Filler or restating the note**
- S1: it restates the note's "one cheap fund diversifies Laura's stocks". It adds countries and sectors but drops the
  fee and the holdings count.
- S3: a label ("branch", "the part that grows") with no information. The judge does not yet have the IPS, which
  defines it.
- S4, second half: it largely restates the note's "a rise before 2031 lifts the top of the range co-sponsors hear". The
  new content is "half".

**Claims a judge would doubt**
- "diversifies the portfolio" (S1): the portfolio is about 90% Treasuries from one issuer (KIT 3E).
- "costly (and risky) stock picking" (S1): asserted, with no evidence or alternative.
- "about 7.5% a year per JPMorgan" (S4): see problem 1.
- "Its expected return ... can raise the upper bound" (S4): it is VT's 2031 value, not its expected return, that sets
  the bound (V5:29).
- "covering a payment shortfall" (S5): a model claim. Her half can be $0 at the 5th percentile (KIT D1, MODEL 19 Oct).
- "if ... iBond payouts fall short" (S5): honest and correct (ISH:850), and it links to IBTM and IBTR. Keep the idea.

**What a Top-50 reflection would do that this does not** (requirements only)
- Make the size decision a trade-off with its reason: what was given up and what it protects. Use one number with its
  basis, the same number the IPS uses.
- Own the note's understatement and show how VT's role was refined, matching exactly the IPS run the team will
  submit (D1).
- Give the "why this fund" reasoning, with an alternative only if the team really decided it and logged it.
- Say what a stock fall can and cannot do: it moves only the top of the range; the payments are untouched (V5:29
  "No payment changes").
- Keep every backstop inside the portfolio.
- Use the case's balance idea (CASE:71-74) or flexibility "as the project develops" (CASE:102-103), in the team's own
  words.

**Student-written or AI-polished?** The most student-sounding of the three.
- Student signs: parenthetical asides ("(and risky)", "(9% of the portfolio)"); "per JPMorgan"; "the part that grows";
  a number an AI copying the IPS would not have got wrong.
- AI-lineage signs: 15 of 100 words are shared with the older student rewrite (section B), which itself descends from
  the [AI] VT text. The idea order (small by design, then one fund, then half sets the bound, then Laura keeps half) is
  the AI skeleton. Only 4 words are verbatim with the [AI] text ("the upper bound of").
- Forensic risk on the reflection: low. Separate issue: the *filed note* contains a 13-word clause copied from the
  30 Sep AI example notes (KIT 1H; D6). That needs disclosure, and the note cannot be changed.

### Reflection 3: IBTR (note 10/07/2026 04:42:53 AM ET, WNX:108; not the cancelled "0.3" note, WNX:128)

Sentences: S1 "IBTR holds 2036 Treasuries that mature in December 2036, just before ... 1 January 2037." S2 "It is one of
five iBond funds ... six to ten." S3 "Like IBTM, it is a 'root' of our strategy, held to maturity." S4 "We bought the
ladder from 2042 backwards ... 'with a high degree of certainty'." S5 "If yields fall, the ladder may cost more than
$300,000; ... the facility contribution is lower."

**5 worst problems, ranked**
1. **The test is not reported.** The note set a pre-committed, numeric test ("more than about 0.2 percentage points by
   January", WNX:108). That is exactly what Wharton's feedback asks for: "Will certain triggers dictate whether you buy
   or sell a security?" (RUB §2e, TF2324:16-18). The reflection never says what has happened since. MODEL, basis D: the
   room was 23.0bp on 6 Oct, fell to 3.6bp on 16 Oct and was 9.8bp on 19 Oct. The line was not crossed at any published
   close (KIT 2E). Whatever the team reports must carry a date and a basis, must allow for either outcome, and must
   not use "triggered" (KIT 2H).
2. **S5 restates the note** (its third sentence, with the threshold dropped) and is now *vaguer* than the note: "If yields
   fall" implies any fall, where the note gave about 0.2 points. It spends 21 words saying less than the filed note.
3. **S1 has a factual error.** The fund's bonds do not all "mature in December 2036". The fund terminates "on or about"
   15 Dec 2036 (ISH:849), and its holdings mature during 2036 (KIT 2C: "4 Treasuries maturing in 2036", from iShares on
   28 Sep, not re-checked). S3's "held to maturity" is loose for an ETF, which terminates and distributes (ISH:850).
4. **S4's reasoning breaks halfway.** "Most sensitive to interest rates, which serves her operating commitment with a high
   degree of certainty" leaves out the link (why buying the most rate-sensitive payments first protects certainty). The
   reason also differs between V5 runs: accepted "the most rate-sensitive" vs pending "so any shortfall falls on near
   payments the 2028 deposit can still fund" (V5:27; KIT D2). Whichever run the team keeps, the reflection must match it.
   In WInS, "from 2042 backwards" is true of the first round, not of the filled IBTR order (re-placed 7 Oct 4:42 AM ET,
   after IBTM; KIT Part 0).
5. **Who absorbs a top-up is left vague.** "The facility contribution is lower": is it the floor or the stock fund? The
   reflections and V5 must give one answer (KIT D4). Why IBTR rather than the WInS-listed 4.5% Feb-2036 bond is also
   unexplained (KIT 2D; reasons not recorded).

**Filler or restating the note**
- S1, partly: "fifth payment ... 2037" restates the note. The added maturity detail is wrong.
- S3: filler ("root" label; "like IBTM").
- S5: almost wholly restates note sentence 3.

**Claims a judge would doubt**
- "mature in December 2036" (S1), "held to maturity" (S3): see problem 3.
- "We bought the ladder from 2042 backwards" (S4): true of the first round and of Laura's plan. A judge who checks
  WInS order times sees IBTR placed after IBTM (WNX:108, 112).
- "which serves her operating commitment 'with a high degree of certainty'" (S4): a non sequitur as written.
- "the ladder may cost more than $300,000" (S5): true, but undated and with no threshold. The MODEL odds were about 41%
  by 1 Jan on basis D at 19 Oct (KIT 2E). That is not TNA content, but a judge may ask.

**What a Top-50 reflection would do that this does not** (requirements only)
- Report the outcome of the note's own test so far, with its date and basis, and say what the rule does next (or that
  no trade was needed and why). Log any "we checked and held" before claiming it (KIT 2G).
- Give the reason for buying long payments first, with the logic visible, matching the IPS run kept.
- Explain, in plain terms, what the threshold means for Laura's money. One gloss of "percentage points" or "rate
  sensitivity" is enough.
- Name who absorbs a top-up, the same way as IBTM, VT and the IPS.
- Optionally, say once that WInS is Laura's post-2028 plan scaled down (KIT D6). IBTR is the suggested home for that.

**Student-written or AI-polished?** Student-written around one AI sentence.
- AI-lineage signs: "We bought the ladder from 2042 backwards because the" is an 8-word verbatim run from the [AI] IBTR
  text (section C), followed by a near-paraphrase ("furthest payments are most sensitive" vs "most distant payments are
  the most sensitive"). 13 of 99 words are in shared runs with the [AI] text. 11 are shared with the older student
  rewrite (section B).
- Student signs: "Like IBTM, it is a 'root'"; the semicolon-then-"so" chain in S5; the stitched-on case quote in S4.
- Forensic risk: moderate, concentrated in S4.

---

## The set of three as a whole

| Test | J1 | J2 | J3 | J4 | Consensus |
|---|---|---|---|---|---|
| Do the picks cover the strategy (payments, floor, growth; TNA:14-15) | 8 | 8 | 7 | 8 | **7.8** |
| Is there one decision shown as refined or changed | 5 | 5 | 4 | 5 | **4.8** |
| Free of reflections that merely restate the note | 5 | 6 | 5 | 6 | **5.5** |
| **Set score** | 6 | 6 | 5 | 6 | **5.8** |

- **Coverage: good.** The three picks cover funding reliability and future cash flows (IBTR, IBTM), risk (all three),
  growth (VT) and flexibility (VT). The "root/branch" thread ties them together.
- **Liquidity is missing** from all three (TNA:5 lists it; IBTM is the natural home, KIT Part 0b).
- **Refined: only IBTM claims a change.** It is the WInS-only rule moving Laura's real plan off zero-coupon Treasuries.
  What changed (real plan, not the WInS trade) and when (the email's time is UNVERIFIED, KIT D7) are unclear.
- **Tested: none.** IBTR is built for "tested" and does not use it.
- **VT could be "refined"** (its note understated the role of Laura's half) if the team decides D1 first.
- **Restating:** IBTR S5 almost entirely; VT S1 and half of S4; IBTM S3.

**Joints that break across the trio and the IPS**
- The return assumption: VT says 7.5%, V5 says 7%.
- VT's jobs: one in the note ("only"), three in the VT reflection, two or three in V5 depending on the run kept (KIT D1).
- Who absorbs a ladder top-up: IBTR says "the facility contribution". IBTM implies the minimum is fixed. Neither says
  when the floor is fixed (KIT D4).
- The 2042-first reason: it matches the accepted V5 run, but not the pending one (KIT D2).
- Where shortfall cover sits: VT's "stays Laura's" vs case:91-92. Accepted V5's "her other assets" has the same flaw
  (V5:25).
- Scale: "9%" (VT), one 4,503-share IBTM order described as "a second batch", and "her first $300,000" (IBTR note). None of
  this makes sense to a judge without one statement that WInS is the scaled-down post-2028 plan (KIT D6).

---

## Panel summary

### Consensus scores (mean of four judges; AI opinion)

| Reflection | E | P | C | Cl | Co | Overall |
|---|---|---|---|---|---|---|
| IBTM | 6.0 | 6.0 | 4.8 | 5.8 | 4.5 | **5.4** |
| VT | 6.0 | 4.0 | 5.0 | 7.0 | 3.8 | **5.2** |
| IBTR | 5.8 | 3.5 | 5.8 | 5.5 | 5.3 | **5.2** |
| Set | | | | | | **5.8** |

Band: **competent, not yet Top-50 contention** (7.5+). The weakest columns are Purpose (tested/refined) and
Consistency. Both are fixable in an evening without new research. Panel estimate if items 1-10 below are done well,
in the students' own words: about 7-7.5 per reflection (AI opinion).

### The 10 must-fix items, ranked by score gain per minute of student work

| # | Item (requirement, not wording) | Where | Minutes | Gain |
|---|---|---|---|---|
| 1 | Use the IPS's return assumption (or no forecast at all); 7.5% is the wrong asset class and contradicts V5 | VT S4 | 2 | Co +2 |
| 2 | Correct the IBTR maturity statement: the fund ends about 15 Dec 2036, and its bonds mature during 2036; also fix "held to maturity" for a fund | IBTR S1, S3 | 3 | Co +1, PA concepts |
| 3 | Remove the "clear yield / set date" claims that contradict the filed note and the issuer | IBTM S4 | 3 | Co +2 |
| 4 | Remove "promise" and the absolute "will not ... fail"; express the protection in the case's credibility terms, decided jointly with V5's "Promise only what is owned" (D6) | IBTM S5 | 5 | C +1, Co +1 |
| 5 | Remove the 8-word verbatim AI clause and the verbatim AI sentence ("lists no individual Treasury maturing in 2032"); reword in the team's own words | IBTR S4, IBTM S2 | 5 | Voice/integrity risk |
| 6 | Report the result of the note's pre-set 0.2-point test, with date and basis (or say it is not crossed and what the rule will do), in place of the restating S5 | IBTR S5 | 15 | P +3 (largest single gain) |
| 7 | Make the 2042-first reasoning complete (why it protects certainty), matching the V5 run kept (D2) | IBTR S4 | 5 | Cl +1, Co +1 |
| 8 | Say which plan the rule change altered (Laura's real plan; IBTM was already the WInS choice), date it honestly, and add the IPS consequence (floor = lower bound, rounded down because the payout is not fixed) | IBTM S1, S3, S5 | 10 | P +1.5 |
| 9 | Show VT's role as refined: acknowledge that the note's "only" understated it, keep Laura's half inside the portfolio, and match the IPS run kept (needs the D1 decision first) | VT S5 | 15 | P +2, Co +1 |
| 10 | Anchor "9%" (WInS share vs Laura's plan) and say once, somewhere in the trio, that WInS is the scaled-down post-2028 plan | VT S2; IBTR | 5 | Co +1, Cl +1 |

**Word budget:** VT and IBTR are at 99. Items 6, 8 and 9 add content, so the team has to cut first. The best cuts are
the filler and restating sentences listed above (VT S1/S3, IBTR S3/S5, IBTM S4). Re-count with the SMApply form's
counter and `textcheck.py`. Aim for 95 or fewer.

**Housekeeping (no score, but gates):**
- Do not submit the "(Ray)" author label.
- Paste each note from the WInS Trade Notes page, not from the Doc. One working copy of the VT note reads "co-sponsors
  here" (draft D, line 38), but WInS reads "hear".
- For IBTR, paste the 04:42:53 AM note ("about 0.2"), not the cancelled "0.3" one (WNX:128).
- Move or delete the [AI] texts in the tab (KIT D6).
- Log this panel and the AI lineage noted above (KIT common checks).

### Verdict: are IBTM, VT and IBTR the best three of the eleven filled notes?

**Yes. Keep them.** Notes compared: WNX:107-117.
- **IBTM** is the only trade that serves both objectives (first payment and floor), and the only one with a
  rule-change story.
- **IBTR** is the only filed note with a numeric test written in advance, which is the strongest possible "tested"
  material if the reflection uses it.
- **VT** is the only growth trade. Without it the set loses "growth", the first theme Wharton lists (TNA:5), and any
  link to the 2031 range's top.

**Runners-up, and why each loses:**
- **Feb-2037 bond** (WNX:109). Its 10.5-month gap and reinvestment-rate risk give good analysis. It is the best
  reserve, but it would replace either the only growth trade or the only pre-set test, and it repeats the
  "payment holding" role.
- **Nov-2039** (WNX:111). "Chose Nov over May 2039" shows a real choice between alternatives, but a small one.
- **Nov-2040** (WNX:116). It covers the coupon-reliance trade-off and a price check. Good diligence, but narrow.
- **Nov-2041** (WNX:117). It explains the fund/bond split and the "scaled to the model portfolio" point. It is useful
  context, but IBTR S2 already carries the structure.
- **IBTO, IBTP, IBTQ** (WNX:113-115). These are near-duplicates of IBTR's role. IBTO's "first payments we would top
  up" supports the pending 2042-first reason, so read it before deciding D2.

**Risks the picks carry, which the reflections must handle and a swap would not remove:**
- The VT note's "only", "gift" and "promised minimum", plus its 13-word AI-exemplar clause (KIT 1H).
- The IBTM note's 30% overlap with its AI exemplar (KIT 3H).
- Neither note can be edited. Both need honest handling in the reflection and in the AI-use log.
