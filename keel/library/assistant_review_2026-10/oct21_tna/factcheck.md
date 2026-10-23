# TNA section A: mechanical, provenance and fact check (Wed 21 Oct 2026, Sydney)

> AI-generated check (Claude Code). Not for submission, and log it in the AI-use record. It contains no replacement wording: each row says what is wrong and what a fix has to do. The students write any fix.
> Input: `SP/oct21/tna/current_draft_21Oct.md` section A (read from the live Doc ~18:10 Sydney; Doc modifiedTime 2026-10-21T05:08:58Z).
> SP = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad`. Work files: `SP/oct21/tna/factcheck/work/` (r_*.txt = reflections, n_*.txt = notes as drafted, w_*.txt = notes from the WInS export, prov_*.txt = provenance output). Web copy: `SP/oct21/tna/factcheck/web/ibtr_ishares_2026-10-21.txt` (iShares IBTR page, fetched 21 Oct).
> **Limit on the check:** IPS V5 was checked against the 19 Oct read (`SP/oct19/drive/ips_report_live.md:23-30`). The Doc changed on 21 Oct, so any V5 edits made on 20-21 Oct are UNVERIFIED here.

## 1. Word counts and characters

Tool: `keel/office/tools/textcheck.py` (whitespace count, plus a strict count that splits on hyphens, slashes and dashes), and a third "naive" count of letter/number runs. The naive count splits `Laura’s`, `$50,000` and `7.5%`, which is what a crude web counter does. How SMApply counts words is UNVERIFIED (`SP/oct20/verify_semiblue/semiblue_checked.md:328`).

| Reflection | Whitespace | Strict (kit) | Naive alnum-run | Characters | Verdict |
|---|---|---|---|---|---|
| IBTM | 94 | 95 | 99 | 567 | Passes. Margin 5 on the strict count; 1 on the naive count |
| VT | 99 | 99 | **104** | 610 | **Within 1 of the limit.** Over 100 on a crude counter |
| IBTR | 99 | 99 | **101** | 588 | **Within 1 of the limit.** Over 100 on a crude counter |

- VT and IBTR are both within 3 words of the limit. The kit's target is 95 or fewer on two counters (Fact Kits v2:413, :591). Both miss that target by 4 words. IBTM meets it on the strict count (95).
- The labels "Reflection:" and "Reflection (Ray):" are not part of the reflection. Pasting "(Ray):" into the form would add 2 words, and a name.
- **Non-ASCII:** the reflections use curly ’ “ ” (IBTM 5, VT 6, IBTR 5). There are no dashes, no non-breaking spaces and no odd characters. This does not matter for the reflections: no rule asks for ASCII, and SMApply is a web form (assumed to accept Unicode; UNVERIFIED). It matters only in two ways:
  - (a) A crude counter splits a word at ’, which is how VT and IBTR get to 104 and 101.
  - (b) The three **notes** in section A are plain ASCII with straight apostrophes. Nobody may "tidy" them to match the curly quotes in the reflections, because the notes must match WInS exactly (TNA:44).
- Overclaim scan (textcheck list): no hits in the reflections. The list misses **"her promise"** in IBTM, because it only lists "promised". "Promised" is on the kit's banned list (Fact Kits v2:751).

## 2. Exact match of the three notes

Each section-A note was compared byte for byte (`cmp`) and with `textcheck.py --compare` against the WInS Trade Notes export (`caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:14, :15, :19`). The repo copy and `/home/user/snap/main/...` are identical (`diff`).

| Note | Order (ET, as WInS shows) | Chars | Match |
|---|---|---|---|
| IBTM | 10/06/2026 10:01:41 PM | 292 | **Identical** |
| VT | 10/07/2026 08:27:19 PM | 288 | **Identical** ("co-sponsors hear", correct) |
| IBTR | 10/07/2026 04:42:53 AM (filled order; "about 0.2") | 294 | **Identical** (not the cancelled 8:31:27 PM "0.3" note, export :37) |

- The typo is real but is not in section A. The working copy in the Doc's "## VT" section reads "co-sponsors **here**" (draft D:38). Whoever pastes into SMApply must copy from WInS or from section A, never from the "## VT" working section. A second student then checks the paste against the export.
- A 13 Oct export cannot prove what WInS shows today. Re-copy from the live WInS Trade Notes page on submission day; the kit's rule is to copy from WInS, not from a Doc (Fact Kits v2:744).

## 3. Provenance: shared 5-word runs with AI text

Tool: `SP/oct20/verify_runbook/provenance_fixed.py`, n=5. Allowed (quoted on purpose): the WInS notes and the case. Each corpus was run on its own and then all together (`work/prov_all.txt`, `work/prov_union.txt`).

AI corpora used:
- (G1) section C [AI] texts;
- (G2) exemplar v1-v12 (`SP/oct19/exemplars/versions/*.md`, `SP/oct19/tna/working/ex11.md`, `ex12.md`);
- (G3) live-Doc AI text, 19 Oct (`SP/oct19/exemplars/ips_v5_tab_with_v12_suggestions_accepted.txt`, `ips_doc_live_base_text.txt`);
- (G4) AI kits, blueprint and notes (`SP/oct19/tnakit/tna_fact_kits.md`, `SP/oct20/out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md`, `/home/user/snap/main/rab/trades/notes.md`, `keel/library/blueprints/01_trading_notes_blueprint.md`, `keel/library/insight_v1/trading_notes_pack.md`);
- (G5) Doc tabs the team itself marks as AI (`caplet/google_drive/ips_report/01_version_5.md`, `02_v4_need_to_humanise.md`, `15_tab_15.md`), plus the Sheet's exemplar column (`SP/oct19/drive/sheets/trading_notes.md`).

| Reflection | Union coverage | Shared runs (AI source: file:line) |
|---|---|---|
| IBTM | **24%** of 94 words, all flagged | "limited laura's recommended portfolio to securities listed on wins" (exemplar `054b53b.md:51`; the section C IBTM shares "portfolio to securities listed on WInS"); "lists no individual treasury maturing in 2032 ibtm" (section C IBTM; exemplars; live Doc `ips_v5_tab..._accepted.txt:123`); "funding her first $50,000 payment as" (exemplar `52e6be7.md:51`) |
| VT | **5%**, flagged | "is the branch of our" (exemplar `08c10f4.md:40`). Clean against section C and the kits |
| IBTR | **28%** (22% flagged, 6% allowed) | "we bought the ladder from 2042 backwards because the" (section C IBTR; exemplar `1ed9130.md:56`; also kit v1 `tna_fact_kits.md:87`); "payments are most sensitive to interest rates" (exemplar `054b53b.md:47`); "more than $300,000 the 2028 deposit" (exemplar `8b8aeb0.md:47`; live Doc base text :113). ALLOWED: "with a high degree of certainty" (CASE:91) |

Below the 5-word threshold, three sentences are still AI sentences with a few words swapped. The judges or Wharton could see this side by side:
- **IBTM sentences 1-3** follow the AI IBTM sentence by sentence:
  - zero-coupon plan dropped, then the 6 Oct guidance and WInS-only (exemplar `8b8aeb0.md:51`, section C);
  - then "WInS lists no individual Treasury maturing in 2032";
  - then IBTM funds the first payment.
- **IBTR sentence 4** is the AI sentence "We bought the ladder from 2042 backwards because the most distant payments are the most sensitive to rates" (section C; `1ed9130.md:56`) with "most distant" changed to "furthest" and "rates" to "interest rates".
- **IBTR's last sentence** has the AI logic and order: cost above $300,000, then the 2028 deposit completes it, then the facility gets less (`8b8aeb0.md:47`). It shares a 6-word run with the older student rewrite in B. That B text sits under a "Rewritten (AI version is below)" heading.
- **VT** shares one 6-word run, "portfolio across countries and sectors without", with B's own student text. That is lineage, not AI.

What the fix must achieve:
- Every flagged span is rebuilt from the author's own notes, or cut, and the AI sentence order is dropped as well. Swapping single words does not change who wrote the sentence.
- The fact phrase "no individual Treasury maturing in 2032" can stay as a fact. It must not keep the AI's wording and position.
- The team logs each decision, and the AI-use log names the exemplars v1-v12, the [AI] Doc reflections and this check. Wharton: "You may not submit any work generated by an AI program as your own" (Fact Kits v2:5).
- A clean result does not prove authorship (tool docstring).

## 4. Fact check, claim by claim

Short names: CASE = `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`; GUIDE = `.../2026_WGY_Investment_Competition_Guide.txt`; FAQ20 = `.../smapply_public_2026-10-20/faqs.txt`; WNX = the WInS export above; ISH-M = iShares IBTM page, 19 Oct (`SP/oct19/tnakit/web/ibtm_ishares_2026-10-19.txt`); ISH-R = iShares IBTR page, 21 Oct (`SP/oct21/tna/factcheck/web/ibtr_ishares_2026-10-21.txt`; raw `ibtr_page.html`); KIT = `SP/oct20/out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md`; REG = `SP/oct20/numreg/numbers_register.md`; IPS = `SP/oct19/drive/ips_report_live.md` line; JPM = `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf`.

### 4.1 IBTM reflection

| # | Claim | Verdict | Evidence | What the fix must achieve |
|---|---|---|---|---|
| M1 | "favouring zero-coupon Treasuries at first" | TRUE | Team journal 5 Oct: "STRIPS in real life, IBTM as the WInS stand-in" (KIT:682). The insight_v1 plan was STRIPS-based (CLAUDE.md) | Fine. Make clear it was Laura's **real** plan, not the WInS trade |
| M2 | "Wharton's week 2 email" | TRUE (week), UNVERIFIED (text and time) | Week 4 ends 23 Oct and Week 6 ends 6 Nov (GUIDE:87, :10), so 5-9 Oct is Week 2 and Tue 6 Oct falls in it. The email is quoted only in AI-written competition/COMPETITION.md:91-94. The primary is not in the repo, the Drive or Gmail (KIT:647, :267). The Doc "Letters" tab holds only the Week 4 email (draft D:37) | Name it so a judge can place it, e.g. by date (6 Oct). File the primary email in the Letters tab before submitting |
| M3 | email "limited Laura's recommended portfolio to securities listed on WInS" | TRUE | Quoted text: "for both contributions may include only approved investment types: eligible stocks, ETFs and Treasury bonds available on WInS" (competition/COMPETITION.md:91-92). The public FAQ now says the same: "Investments permitted (for BOTH contributions, the IPS and Final Report)" and "STRIPS ... NOT permitted" (FAQ20:42-45, :53) | Keep the fact. The wording is AI-derived (section 3) |
| M4 | "we abandoned that plan **because**" of the email; "IBTM **therefore** became the best alternative" | MISLEADING | In WInS, IBTM was the 2032 stand-in from 29 Sep, before the email: "Use IBTM for the building minimum" (`SP/oct19/drive/sheets/wins_notes.md:25`). Whether the email arrived before the 10:01:41 PM ET order is UNVERIFIED (KIT:693). No comparison of alternatives is recorded, e.g. the 15 Feb 2031 bond or a short Treasury ETF, so "best" is unsupported | Say what the email changed (Laura's real plan) and what it did not (the WInS trade). Drop "best" or support it with a recorded comparison. Use "refined" only if the arrival time is confirmed |
| M5 | "WInS also lists no individual Treasury maturing in 2032" | TRUE (team record, 29 Sep) | "43 US Treasuries; none mature between 15 Feb 2031 and 15 Feb 2036" (`wins_notes.md:25`). Not re-checked in WInS since (the assistant does not use WInS) | One student re-checks the WInS bond drop-down before submitting |
| M6 | "it is cheap" | TRUE | Fee 0.07% (ISH-M:220-222) | Fine |
| M7 | "easy to trade" | TRUE | 30-day median bid/ask spread 0.05% and volume 332,785 shares, 16 Oct (ISH-M:240-266) | Fine |
| M8 | "has a clear yield" | MISLEADING | iShares shows several yields: 30-day SEC 4.98% and 12m trailing 4.05% (ISH-M:287-293). "the Fund(s) will make distributions of income that vary over time" (ISH-M:849). The realised yield depends on cash rates in the fund's final year (ISH-M:674) | No claim that the yield is known or fixed. It must agree with the note's own "the final payout is not fixed" |
| M9 | "matures on a set date" | MISLEADING | An ETF does not mature. It "will terminate on or about October or December 15 of the year in each Fund's name", and its proceeds "are not predictable ... do not seek to return any predetermined amount" (ISH-M:849-850). The bonds inside mature during 2032 | Say what really happens: the fund closes around mid-December 2032 and pays out an amount that is not fixed. That is about 17 days before the 1 Jan 2033 payment (KIT:634), the trio's one liquidity point |
| M10 | "Laura's second deposit buys a second batch of IBTM to ground a minimum" | TRUE (plan) | IPS:27, both runs: the 2028 deposit first completes the ladder if needed, then "Its remainder buys the floor, a Treasury fund maturing in December 2032". In WInS both batches were bought together (1,142 + 3,361 shares; KIT:623-626) | Mention the "if needed, the ladder first" order, or the IBTR reflection's point contradicts it (see 5) |
| M11 | "a stock crash will not make her promise fail" | MISLEADING | Narrowly true: a stock fall does not touch IBTM. But (a) the payout is not fixed (ISH-M:850, and the note itself). (b) Falling yields before January shrink the floor through a ladder top-up: about $137-138k after a half-point fall (MODEL, 19 Oct; KIT:203). (c) The accepted IPS uses the floor "last" for a payment shortfall (IPS:25 [acc]). So a crash plus a coupon shortfall can reach the floor. (d) "promise": the case asks for a "credible range" (CASE:115-116) and warns against promising more (CASE:114). The IPS rounds the floor down for exactly this reason (IPS:29) and the reflection never says so | Name the risks that can still move the minimum (fund payout, yields before purchase) and how the plan allows for them (rounding down). No promise language |
| M12 | "As the 'root' of our strategy" | MISLEADING (minor) | IBTR calls itself "a 'root'", like IBTM. The IPS [pend] pitch calls the payment Treasuries the roots, then adds the floor (IPS:23) | The three reflections must use the metaphor the same way: "the" root or "a" root |

### 4.2 VT reflection

| # | Claim | Verdict | Evidence | What the fix must achieve |
|---|---|---|---|---|
| V1 | VT diversifies across countries and sectors without stock picking | TRUE | About 10,242 holdings at a 0.06% fee (KIT:331). Wharton calls diversification "an important investment principle" (KIT:342, TRD:48-49). The $25 commission per stock trade (FAQ20:63) supports "costly" | Fine. "the portfolio" is about 90% Treasuries (KIT:660), so VT diversifies only the stock part |
| V2 | "9% of the portfolio" | MISLEADING | WInS: 8.84% of $300k at cost, 8.65% of the 19 Oct book. Laura's real plan: about 7% (6.9-7.0% of about $465k, MODEL; REG:166 H4). REG:13 lists "~9% of all money" for Laura as a real error | Say which portfolio (WInS book vs Laura's plan) and match the IPS's "under one tenth" |
| V3 | kept small "since we prioritise certainty for Laura's payments" | MISLEADING (incomplete) | VT is what is left after the payments **and the floor** are bought (IPS:27, "Buy the payments, then the floor, then growth"). The payments come from the 2027 deposit whatever size VT is | Give the real sizing rule, payments then floor then stocks, in the team's words |
| V4 | VT is "the branch ... the part that grows" | TRUE | IPS:23 pitch, both runs | Fine. The wording is AI-derived (section 3, "is the branch of our") |
| V5 | "expected return, about 7.5% a year per JPMorgan" | **FALSE** | JPM 2026 LTCMA: AC World Equity 7.00% compound (8.28% arithmetic, 16.78% vol). **7.50% is EAFE Equity** (JPM matrix rows "EAFE Equity 7.50 8.90 17.63", "AC World Equity 7.00 8.28 16.78"; CLAUDE.md Key facts). IPS:27 assumes 7%. REG:13 lists "7.5%" as a real error, and REG:176 (I1) gives the approved wording basis | If a number is used at all: 7% compound, the 2026 edition, named as an assumption, matching the IPS. Or drop the number |
| V6 | the expected return "can raise the upper bound" | MISLEADING | The upper bound uses VT's **value** in 2031, not its expected return: "adds half the equity fund's value, less any expected payment shortfall" (IPS:29) | Tie the bound to the fund's 2031 value and include the shortfall deduction the IPS states |
| V7 | "half of VT's value is added to that bound" | TRUE (rule) | IPS:29, both runs; draft section C | Fine |
| V8 | "The other half stays Laura's, giving her flexibility and covering a payment shortfall if reinvested coupons earn less or iBond payouts fall short" | MISLEADING | Matches IPS [pend] (IPS:28-29: "retains the other half for flexibility"; "funded from the equity Laura retains"). But: (a) the filed VT note says "They **only** set how far her gift rises", and this gives VT a second job without saying so (KIT:148-158). (b) "stays Laura's" reads as money leaving the portfolio, and payments must be portfolio-funded (CASE:91-92; KIT:394). (c) MODEL, 19 Oct: Laura's kept half is $0 at p5, and leftover plus her half fails to cover the whole coupon shortfall in 6.5-8.0% of paths (KIT:161-163). So "covering" is not assured. (d) The iBond payout risk is real (ISH-M:850) | Face the note's "only" honestly. Keep the backstop money inside the portfolio. Make the shortfall cover conditional, not absolute. All of it must agree with the IPS run the team keeps (D1) |

### 4.3 IBTR reflection

| # | Claim | Verdict | Evidence | What the fix must achieve |
|---|---|---|---|---|
| R1 | "IBTR holds 2036 Treasuries that mature in December 2036" | **FALSE** | iShares: "U.S. Treasury bonds maturing between January 1, 2036, and December 15, 2036". It has 4 holdings and a weighted average maturity of **9.53 yrs** as of 19 Oct 2026 (about May 2036) (ISH-R:163, :209-210, :233-234; `ibtr_page.html` key benefits). The **fund** terminates on or about 15 Dec 2036 (ISH-R:509). Its payout is not fixed (ISH-R:510) | Separate the fund's bonds (maturing during 2036) from the fund's close (about mid-December 2036), and say that the payout is not fixed. The note says nothing about that |
| R2 | "just before Laura's fifth payment on 1 January 2037" | TRUE | Payments 2033-2042, so 2037 is the 5th (CASE:88-89). The fund ends about 17 days before (KIT:452) | Fine |
| R3 | "one of five iBond funds covering payments one to five; individual Treasury bonds cover six to ten" | TRUE | IBTM 2033, IBTO 2034, IBTP 2035, IBTQ 2036, IBTR 2037; Feb-37 2038, May-38 2039, Nov-39 2040, Nov-40 2041, Nov-41 2042 (WNX:14-24). Note that IBTM also carries the floor (KIT:623-625) | Fine |
| R4 | IBTR is "held to maturity" | MISLEADING (minor) | A fund has no maturity. It is held until it closes (ISH-R:509) | Use the fund-close idea, consistent with R1 |
| R5 | "We bought the ladder from 2042 backwards" | MISLEADING | Order times (ET), first round: Nov-41 7:55:45 PM, Nov-40 7:59:20, Nov-39 8:02:40 (cancelled), May-38 8:13:31 (cancelled), Feb-37 8:17:20 (cancelled), IBTR 8:31:27 (cancelled), IBTQ 8:36:15, IBTP 8:45:09, IBTO 9:58:19, IBTM 10:01:41 (draft D:39; KIT:117-130). So the **first round** ran 2042 to 2033. Of the filled orders, IBTR (#10 of 11) was re-placed at 4:42:53 AM, **after** IBTM. All were entered with the market closed, so they filled at the next open together: ETF fills match the 7 Oct open, and bond fill times are UNVERIFIED (TRD:33; KIT:143). The rule is about Laura's 1 Jan 2027 purchase (IPS:27) | Say whose purchase the order rule describes (Laura's January 2027 plan vs the WInS entries), and claim nothing the fill record contradicts |
| R6 | "the furthest payments are most sensitive to interest rates" | TRUE | The 2042 rung costs about $33 per 0.01-point move and the 2033 rung about $22. Per $1,000: $1.46 vs $0.59 (KIT:178-182, MODEL, 16 Oct). Independent check: 15-year vs 6-year zero at about 5%, roughly $33 vs $22 | Fine. It now also clashes with the IPS [pend] reason (see 5) |
| R7 | the buying order "serves her operating commitment 'with a high degree of certainty'" | Quote TRUE; logic MISLEADING | The exact case words are at CASE:91 ("must be funded by the investment portfolio with a high degree of certainty") and CASE:136 ("Supports the ten-year operating commitment with a high degree of certainty"). Certainty comes from holding Treasuries that mature before each payment (IPS:25). Buying order matters only if purchases are spread over time; WInS bought them in one session | The certainty claim must rest on what actually delivers certainty, not on the order of entry |
| R8 | "If yields fall, the ladder may cost more than $300,000" | TRUE (MODEL, dated) | Basis D, 19 Oct: cost $297,162, room $2,838 = 9.8bp, 41% model odds of more than $300k on 1 Jan 2027. On maturity sizing with the 0.07% fund fee it is already about $300.4-300.7k (KIT:14, :497, :519). The reflection drops the note's "more than about 0.2" test, which the 19 Oct data no longer match (room about 0.10) | If a threshold or level is quoted, it needs a date and a basis (D5). If none is quoted, the reflection should still say how it relates to the note's 0.2 test |
| R9 | "the 2028 deposit then completes it, so the facility contribution is lower" | TRUE (rule) | IPS:27, both runs. Floor about $137-138k after a half-point fall (MODEL, KIT:203) | Agree with IBTM (M10, M11) on who absorbs a top-up (D4) |

## 5. Consistency (note vs reflection, across the trio, vs IPS V5 and the pending suggestions)

1. **IBTM reflection vs its own note.** The note says "the final payout is not fixed". The reflection says "clear yield", "matures on a set date" and "a stock crash will not make her promise fail", and never says the payout is not fixed (M8, M9, M11).
2. **IBTM vs VT.** VT admits "iBond payouts fall short" as a risk the kept half covers. IBTM calls the same fund's yield "clear". A judge reading the two together sees a contradiction.
3. **VT reflection vs its own note.** The note says VT's stocks "only set how far her gift rises". The reflection adds a second job, covering payment shortfalls (V8).
4. **IBTR reflection vs its own note.** They agree on payment 5 and the top-up rule. The reflection drops the note's 0.2-point test without saying why. R1 adds a December-maturity claim the note does not make, and it is false.
5. **Who absorbs a top-up (D4).**
   - IBTR: "the facility contribution is lower".
   - IBTM: the minimum survives a stock crash, and yields are not mentioned.
   - IPS:27: the remainder buys the floor, so the floor shrinks first.
   - The trio never says it is the floor (IBTM's second batch) that shrinks. IBTM and IBTR must tell the same story.
6. **WInS vs Laura's plan.** VT uses a WInS share ("9%"). IBTM and IBTR describe Laura's January 2027/2028 purchases. IBTR's "We bought ... backwards" mixes the two. No reflection states the scale: WInS is Laura's 2 Jan 2028 plan scaled by about 0.64 (KIT:248).
7. **IPS V5 (19 Oct read):**
   - "7.5% per JPMorgan" vs IPS:27 "assumed to return 7% a year". **Direct contradiction** (V5).
   - The 2042-first reason. IBTR's "most sensitive to interest rates" matches [acc] ("the most rate-sensitive") but **contradicts [pend]** ("so any shortfall falls on near payments the 2028 deposit can still fund", IPS:27). If the team accepts the pending suggestion, IBTR breaks.
   - Floor rounding. IPS:29 says the lower bound is "rounded down because a fund's payout is not fixed". IBTM says the opposite in effect (M8, M9) and never mentions rounding.
   - Backstop. IPS:25 [acc] says "covered by her other assets, with the floor used last", which is outside money and is barred (CASE:91-92). IPS [pend] says "her other holdings". VT's "stays Laura's" echoes the same trap. If [acc] stays, IBTM's "promise will not fail" is also contradicted, because the floor can be used.
   - "Promise only what is owned" ([acc] heading, IPS:29) supports IBTM's tone. That is a problem with the IPS too, not a defence.
   - The other 9 of the 10 pending AI suggestions (7 in V5, 3 [AI] reflections; CLAUDE.md) do not change these findings. The 3 [AI] reflections in section C are the source of the IBTM and IBTR overlaps. Reject them and move them out before submission (KIT:262-264).
8. **Theme coverage across the trio (TNA:5-6).**
   - Growth: VT. Risk: IBTR and VT. Funding reliability: IBTR and IBTM.
   - Liquidity is **missing**: IBTM's fund-close timing is the natural home, but M9 misstates it.
   - Financial flexibility: only in VT's "stays Laura's" (V8).

## 6. Must-fix list (in order)

1. V5: "7.5% per JPMorgan" is false (7.00% AC World). It must match the IPS's 7%.
2. R1: IBTR's bonds do not mature in December 2036; only the fund closes then.
3. M8, M9, M11 (IBTM): yield, maturity and "promise" claims contradict the filed note and the issuer.
4. R5, R7 (IBTR): the "backwards" order and the certainty logic.
5. V8: the note's "only", and the backstop kept inside the portfolio.
6. V2, item 6 in section 5: say which portfolio and which scale.
7. Provenance: rebuild IBTM sentences 1-3 and IBTR sentences 4-5 from the authors' own notes.
8. Word margins: VT and IBTR at 99 words.
9. Copy the notes from WInS on the day. Never use the "## VT" working copy ("here").
