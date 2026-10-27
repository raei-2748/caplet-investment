# The Archive: what is locked (real records)

## Now
- **Doing:** Day 2 of the rewrite against the locked TNA and 11 notes; ledger gaps closed; L-10 brought onto the day branch
- **Decided:** A19 NEW, would contradict: Laura's stock half as the payment backstop (D1a, D4, L-10) breaks reflection 3 ("the only investment not standing between Laura and a payment deadline"). Cure that keeps it true: set any gap, plus a reserve for coupons still to come, aside in Treasury bills in Jan 2033, before the gift. A20/A21 need the same rule. A12 and A17 closed
- **Next:** Lab sizes the Jan 2033 set-aside with LR-04's mark (request filed); check the Fri 30 Oct fresh draft line by line against A1-A21; Final Report bank (P05) started
- **For the judges:** Keeps the IPS from contradicting the TNA judges already hold; AI-use log complete for the Works Cited
- **Updated:** 2026-10-27 20:10 Sydney


> **State (last run Tue 27 Oct, 20:10 AEDT, Tess).** Locked text unchanged (TNA as read 24 Oct; 11 WInS notes). Today's
> check: L-10 (Genius Lab, PR #50, cherry-picked onto the day branch), LR-04, Courtroom C-02 and WO-R2/R6, Library S-05,
> Writing Room cold read, Window, Noticeboard, thinking log to 27 Oct, D4. Register A1-A21: **1 would-contradict (A19,
> the stock half as payment backstop)**, 2 conditional (A20, A21: true only with the Jan 2033 set-aside), A12 and A17
> closed, A15 one new breach in a candidate line. LEDGER complete to 27 Oct 20:00 AEDT (5 rows added: rewrite thread
> D2-D4 and research, markets check, loop, this run). AI_USE.md 27 Oct row in a separate PR for Ray (outside keel/).
> Note: LEDGER has two different "WO-0003" rows (21 Oct return projections; 26 Oct IPS Draft 1): cite them by ID + date.
> Next run: `git log --since='2026-10-27 20:10 +1100'`; read only `keel/ips_rewrite/` (inbox, drafts), LEDGER, outbox,
> rooms changed; the fresh draft lands Fri 30 Oct: check it line by line against A1-A21.
>
> Room card: `../OFFICE.md`. Keeper: Tess (`evidence-archivist`, `ai-use-recorder`); `coherence-checker` works here for
> Nora. Rule: nothing new may contradict anything on this page. Read it before drafting any deliverable.

## Locked submissions (Caplet's, official)
| Item | Locked on (Sydney) | Where the exact text lives | Notes |
|---|---|---|---|
| Team roster | by Sat 10 Oct 08:00 | private (personal data; not in the repo) | members locked |
| 11 WInS trades and their notes | 7-8 Oct (fills) | `../../caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md` (14 Oct export) | Live Doc tab "WInS Trading Notes" read 24 Oct: all 11 notes identical to the export. Notes cannot be edited, only added to |
| Trading Notes Analysis (3 notes + reflections) | Fri 23 Oct (submitted; Sat 24 Oct 08:00 AEDT deadline) | below, "The TNA as held"; source: IPS Report Doc, tab "Trading Notes" (read only, 24 Oct) | Held as the Doc reads on 24 Oct, the day after submission. A student confirms it matches what went in (`../pm/ASK_HUMANS.md`). Keel never opens SMApply |
| IPS (form) + trading freeze | due Sat 7 Nov 09:00 | | |
| Final Report + school documentation | due Sat 5 Dec 09:00 | | |

## The TNA as held (Caplet's own words; quote exactly, never paraphrase)
Counts (`../office/tools/textcheck.py`): reflection 1 99 by spaces / 98 strict; 2: 99 / 100; 3: 100 / 99. All within 100.

### Trading Note 1: B-T-4.750-15022037

**Note (as saved in WInS):** Future funding: we use the 4.750% Treasury maturing 15 Feb 2037 for Laura's 1 Jan 2038 payment because it is the latest WInS bond available beforehand. The 10.5-month gap creates reinvestment-rate risk on the proceeds held in a short-term Treasury ETF.

**Reflection:** We know Treasury bonds (including this one – maturing 2037) won’t create wealth, but they will remove uncertainty, through duration-matching. In other words, we take Laura’s requested ‘high degree of certainty’ to mean a near-ironclad guarantee, and we provide exactly that. Every year the bonds sit untouched is a good year – one less year of Laura’s money being exposed to anything the restless markets might decide to do. Notably – Laura’s payments are fixed in nominal dollars, so a nominal Treasury matches the liability perfectly, meaning we don’t need TIPS, which would hedge against a nonexistent inflation risk.


### Trading Note 2: IBTM

**Note (as saved in WInS):** Future funding and risk management: IBTM does two jobs in Laura's plan. It supports her first $50,000 payment and provides a floor for her facility contribution, giving co-sponsors a minimum figure in 2031. It holds 2032 Treasuries, so the timing fits, although the final payout is not fixed.

**Reflection:** Some years, WInS lists no Treasuries maturing – so we purchased iShares iBonds (like IBTM for 2032) instead. Defined-maturity, investment-grade, liquid, cheap and transparent about yields, these behave a lot like bonds when held to their end – so we’ll simply ignore price noise in the interim. Together, our T-Bonds and iBonds ensure each of Laura’s payments rests on a dedicated instrument (not merely a forecast). The catch is, their terminal payout is a net asset value, as opposed to a promise of par – but in return we gain a level of liquidity which no odd-lot bond offers.


### Trading Note 3: VT

**Note (as saved in WInS):** Growth: Vanguard Total World Stock ETF holds about 10,000 stocks at a 0.06% fee, so one cheap fund diversifies Laura's stocks. They only set how far her gift rises above her promised minimum. A fall can shrink the extra, and a rise before 2031 lifts the top of the range co-sponsors hear.

**Reflection:** VT is where we allow ourselves to be wrong – because it’s the only investment not standing between Laura and a payment deadline. This ETF owns thousands of companies, diversified across countries and sectors, which means we can avoid paying the price for the vain illusion that we can pick winners, instead buying the entire market’s growth premium at an expense ratio of just 0.06%, for a forecast return of about 7.5% a year (as per JPMorgan). The T-Bonds and iBonds already cover the operating commitments, so VT answers a different question – how generous can the facility contribution be?


## Coherence register (what new work must agree with)
Checked 27 Oct against: Genius Lab L-10 (`../rooms/lab/L-10_last_in_line.md`), Laura's Room LR-04, Courtroom WO-R2/WO-R6 trials 1-2 and C-02 (`../ips_rewrite/inbox/2026-10-27_courtroom.md`), Library S-05, Writing Room cold read (18 lines), Window and Noticeboard notes, `../ips_rewrite/THINKING_LOG.md` to 27 Oct, Draft 4 (V24).
Checked 26 Oct against: `../ips_rewrite/00_GROUND_TRUTH.md` (s3 quotes exact) and the six inbox notes of 26 Oct (Genius Lab L-09, Laura's Room LR-03, Library S-04, Long Room motif, Window, Writing Room H1-H3). v4/v4.1 are no longer checked (Ray, 26 Oct: rewrite from scratch).
Checked 25 Oct against: IPS v4.1 vote copy (`../drafts/ips_v4_1_2026-10-25/`, pitch 37 / IPS 480), Package B (`night_2026-10-25/v4/B_*.txt`), Courtroom C-01, Lab L-08 (Extended Reserve: consistent, "begun six years early"), Library S-03. Checked 24 Oct against: IPS edits v3 (`/mnt/project-files/ips/IPS_edits_v3_2026-10-24.md`, pitch 45 / IPS 471), Tab 15
export, vote set B options and ballot (SD-T04, SD-T12), Laura's Room option A, Lab L-03, Writing Room cut packages.
| # | Locked words | New work | Status | The rule from now on |
|---|---|---|---|---|
| A1 | VT reflection: "a forecast return of about 7.5% a year (as per JPMorgan)" | Library LC-02 (25 Oct): J.P. Morgan 2027 LTCMA p. 8 raises global equity "to 7.5%" (matrix behind a login). IPS v4.1 states no return | **HOLDS** (was WATCH) | Any stock return stated is "J.P. Morgan 2027 LTCMA, global equity, 7.5%" or none; no "compound"/"ACWI" until a human opens the matrix. The 21 Oct teardown's FALSE is superseded |
| A2 | Reflection 1: payments "fixed in nominal dollars", so TIPS "would hedge against a nonexistent inflation risk" | IPS v3: "Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first"; Laura's Room option A adds a 3.5%/yr rate | **WATCH** (consistent today) | Inflation belongs to facility and overrun costs, never to the payments. No sentence may say inflation threatens a payment |
| A3 | Reflection 1: "a near-ironclad guarantee, and we provide exactly that"; reflection 2: payout "a net asset value, as opposed to a promise of par" | IPS v3: "every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short." | Consistent | The IPS definition is the "near" in "near-ironclad", spelled out. Don't soften it to "aim"/"likely" (reverses "we provide exactly that") or harden it to "guaranteed" (reverses the NAV line) |
| A4 | Reflection 1: "Every year the bonds sit untouched is a good year"; reflection 2: "we'll simply ignore price noise" | IPS v3 P6: "replacing any holding that becomes unavailable"; the "held without trading" sentence was cut. No D1-D6 option sells a payment holding | **WATCH** (consistent today) | A payment holding is replaced only when it becomes unavailable, never because of its price |
| A5 | IBTM note: floor "giving co-sponsors a minimum figure in 2031 ... although the final payout is not fixed" | IPS v3: "quoted at the 2032 ETF's projected payout rounded down"; D4: "the floor's projected payout, rounded down"; LR-04 + C-02 (27 Oct): the bottom is a rule, "what the floor will pay, rounded down, less any gap the bond market has already shown", never a printed $145k (below it in 43.5% of MODEL paths before any mark) | Consistent | The mark is taken before Laura speaks, so a minimum figure is still named in 2031. Keep "rounded down" or an equivalent; never "fixed"; no dollar bottom in the IPS (if one must appear: "up to about $145,000") |
| A6 | IBTR note: a yield fall means "the 2028 deposit would top up the ladder, leaving less for the facility" | IPS v3 (C2): "a rate fall before we buy lowers the floor, not a payment" | Consistent | The strongest echo across the set. Keep C2 |
| A7 | VT note: "her promised minimum" | IPS v3: "a floor Laura can quote" (optional "promise" -> "quote") | Low | Either word is fine; the IPS must not argue against promising, which would read as reversing a submitted note |
| A8 | Reflection 1 names TIPS, as rejected | Week 4 email bans TIPS/STRIPS; SD-R11: IPS names neither | Consistent | Rejected-on-merit is already on the record; the IPS needn't repeat it |
| A9 | No locked text uses roots, branches or "Root & Branch" | Ray, 24 Oct: name and roots motif out | Consistent | Dropping it costs no coherence. A new motif must not contradict "VT is where we allow ourselves to be wrong" |
| A10 | (spine) North Star memo: "commit only money she already owns" | IPS v3: floor bought only from the 2028 remainder; the 2027 deposit goes to payments | Consistent | `00_SPINE.md` (PR #25) is not on the day branch yet; the memo governs until it is |
| A11 | Reflection 2: iBonds' "terminal payout is a net asset value, as opposed to a promise of par"; IBTM note: "the final payout is not fixed" | v4.1 pitch: payments bought "in Treasuries held to maturity"; Package B pitch "Like an extended-release pill, they release one payment each January" and IPS "Each payment's Treasury releases its cash by maturing"; Library S-03 rule: "release" only for Treasuries held to maturity | **WATCH** | Five of the ten payments (2033-37) sit in iBonds ETFs. A "release" or "held to maturity" line may cover them only if nothing beside it says or implies a fixed dollar amount ("exactly", "$50,000 released", "fixed"). The rung pays NAV; the TNA already told the judges so |
| A12 | VT note: "her promised minimum"; IBTM note: "a floor ... giving co-sponsors a minimum figure in 2031" | Courtroom C-01 dial 1 / dial 2 (25 Oct) -> superseded 27 Oct by LR-04: mark the 2031 bottom to market by the coupon gap visible then; 0 of 200,000 MODEL paths break the named bottom (7 in the joint shock); C-02 upheld it | **CLOSED 27 Oct** (consistent) | The bottom is a rule, marked in 2031 and then kept. A margin padded in today is not needed. See A19 for what happens after 2033 |
| A13 | Note 1 (Feb-2037 bond): "proceeds held in a short-term Treasury ETF" | v4.1 P6: "Coupons and early maturities wait in a short-term Treasury ETF"; R14: no WInS listing check yet for such an ETF | Consistent | Keep a short-term Treasury holding as the waiting place. If WInS lists none (T24), say "Treasury bills" or name a listed holding, never "cash" alone, which would read as a change from the submitted note |
| A14 | Note 1: "The 10.5-month gap creates reinvestment-rate risk"; reflection 2: "terminal payout is a net asset value, as opposed to a promise of par"; IBTM note: "the final payout is not fixed" | Library S-04 / inbox (26 Oct): Contac picture, "Exact, not about. ... Treasuries pay exact sums on exact dates" | **CLEARED 26 Oct** (`../BIBLE.md` rule 3) | "Exact sums on exact dates" is allowed for iBonds held to the December liquidation and T-bonds held to maturity (Ray: pull-to-par, final NAV is matured cash minus a tiny fee). The locked "not fixed" line is answered, if a draft wants it, by one concise clause; never a hedge. Old objection kept in git history |
| A15 | Reflection 2: "rests on a dedicated instrument (not merely a forecast)"; IBTM note: "the final payout is not fixed" | LR-03 (26 Oct): the 2031 bottom "is a Treasury fund on a statement, not a forecast"; candidate line "in the bank" | **WATCH; 1 breach 27 Oct** | Write "already bought" (Writing Room H1) or the locked "not merely a forecast"; never "not a forecast". The quoted bottom is a projected payout rounded down (A5). 27 Oct breach: LR-04's candidate line "The bottom isn't a forecast" -> "The bottom is already bought" (or cut). The marked bottom still rests on a projected payout |
| A16 | Reflection 2: "behave a lot like bonds when held to their end – so we’ll simply ignore price noise"; Note 1 "reinvestment-rate risk"; Nov-2039 note "reinvested coupons fund the rest"; IBTR note (yield fall -> top-up) | Long Room (26 Oct): one motif sentence, hold to maturity / "do not crush": "price swings can't touch a payment you don't sell" | **WATCH** (consistent as worded) | Only *price* swings are shut out. Rates still reach payments through reinvested coupons and the 2038 gap, as three locked notes say. Never "rates/markets can't touch a payment". If a sale rule is stated, keep "replaced only when unavailable" (A4) |
| A17 | Reflection 1: "Every year the bonds sit untouched is a good year"; every WInS bond note names its own payment year | Genius Lab L-09 (26 Oct): dedicated ladder, WInS mirror ~10 trades / ~$52k each way. Courtroom WO-R2 (27 Oct): contradicts four locked lines (reflection 2 "dedicated instrument", Nov-2039 and Nov-2041 notes, IBTR 0.2pt threshold); KILL for the IPS, Final Report only as an alternative priced and declined | **CLOSED 27 Oct** (no mirror trades) | No re-sizing of the frozen book. The Final Report may show L-09 as the plug we priced and chose not to buy |
| A18 | VT note: "a rise before 2031 lifts the top of the range co-sponsors hear"; reflection 3: VT answers "how generous can the facility contribution be?" | LR-03 (26 Oct): "the top is a rule (minimum + half the fund)"; "a bigger top buys little" | Consistent | The top must keep moving with VT. LR-03 may argue for a smaller share of the fund, never for a range that is the floor alone |
| A19 | Reflection 3: "VT is where we allow ourselves to be wrong – because it's the only investment not standing between Laura and a payment deadline" and "The T-Bonds and iBonds already cover the operating commitments" | D1a (Keel's call 26-27 Oct: coupon gap drawn from Laura's half first); D4: "we price any gap and hold it back – from Laura's half first, the floor last" and "no payment needs them to"; L-10 (27 Oct, MODEL, 22 Oct curve, 7.5%): Laura's half is drawn for payment gaps in 33% of paths, and after 2033 it is the only thing behind the payments, which fall short in 6.8-8.4% of paths (median ~$3,200); thinking log: her half also pays inflation and currency overruns | **WOULD CONTRADICT** (new) | No IPS line may make Laura's stocks a source for a payment at a payment deadline. Consistent cure: in Jan 2033, before the gift, any visible gap plus a reserve for coupons still to come is sold out of stocks (leftover, Laura's half, then the gift: top first, floor last) into Treasury bills, once. From then on no payment waits on a share price, and reflection 3 is true. D4's hold-back sentence is one clause away: "price any gap, and the coupons still to come, and set it aside in Treasury bills". Lab to size the reserve (request 27 Oct) |
| A20 | Reflection 1: "near-ironclad guarantee, and we provide exactly that"; Note 1: "reinvestment-rate risk"; Nov-2039 note: "reinvested coupons fund the rest" | Writing Room 3b "all ten cheques are bought by January 2028" and hard issue 4 "it never reaches a payment"; D4 "Ten cheques, then – each bought before the first is written"; L-10: a 2pt fall just after the build leaves a payment short in 39% of paths without a rule, 0.02% with the 2033 trap | **CONDITIONAL** | True as written only if the same IPS carries the Jan 2033 set-aside (A19). Without it the honest number is about 1 in 15 and "exactly that" in the locked reflection reads as an overclaim the IPS itself disproves. Never write "never reaches a payment" about yields; the locked notes name the coupon risk |
| A21 | Reflection 1 defines "high degree of certainty" as "a near-ironclad guarantee" | Library S-05: IRS 1-in-20 "probability of exhaustion" as the yardstick, set against "0.75% below the bottom" | **CONDITIONAL** | The IRS test measures the fixed payments running out, not the bottom. On today's plan that is 6.8% (above the IRS's 5%); with the Jan 2033 set-aside 0.01%. Any yardstick line quotes the payment number and needs A19's rule; the Library's and Writing Room's lean (Final Report only) avoids the problem |

## The AI-use record
`../office/LEDGER.md` (one row per office answer) and `../../caplet/docs/AI_USE.md` (lines for the Works Cited).

**Wording trace of the TNA reflections (24 Oct, records only).** 4-word runs shared with every Markdown/CSV file in
the repo (474 files): before 23 Oct, no AI file shares more than a generic phrase ("payments are fixed in"; "about 7.5% a
year", in the 21 Oct teardown that told the team to delete it; "across countries and sectors"). Every longer match is a
file written on or after 23 Oct that quotes the submitted text (VOICE.md, ladder record, L-03, SD-T04). This covers repo
files only, not chats (ChatGPT, Claude.ai) or the Doc's suggestion history. It is evidence for the students, not an answer:
each writer still says what was theirs.

**Pasted into `AI_USE.md` s5 on Sun 25 Oct** (plus three new rows: Codex reviews, the outside review Ray pasted, Keel 25 Oct) (SD-T11's eight rows, with the last row completed to 24 Oct 19:00):
| Date (AEST) | Tool | What the AI did | Output | Student decision |
|---|---|---|---|---|
| 2026-10-16 | Claude Code | Assistant review 30 Sep-15 Oct, North Star memo, IPS pre-mortem, number checks (AI research, not for submission) | `keel/library/assistant_review_2026-10/` | |
| 2026-10-17 | Claude Code | 2031 range model on the WInS-only basis; IBTM payout drift | `keel/library/range_2031/` | |
| 2026-10-17/18 | Claude Code | Exemplar v3-v12 of the pitch, IPS and three TNA reflections (a model to learn from), also put into the IPS Report Doc as suggestions (Version 5, Trading Note Reflection tabs) | `keel/library/blueprints/04_exemplar_ips_tna_17Oct.md` | |
| 2026-10-19/20 | Claude Code | WO-0002: why V5 would not reach the semifinal; check of rewritten VT and IBTR reflections | LEDGER WO-0002a/b | |
| 2026-10-21 | Claude Code | WO-0003 world-stock return projections; WO-0004 final TNA check; WO-0005 TNA criteria and hold check; TNA teardown v1-v2 | LEDGER; `keel/library/assistant_review_2026-10/oct21_tna/` | |
| 2026-10-22/23 | Claude Code | Team Keel: six fictional personas, episodes, project office and routines (fiction; research re-checked before use) | `keel/` | |
| 2026-10-23 | Claude Code | WO-0006: IPS requirements, gap check of Tab 15 (read only), plan to 7 Nov, narrative spine | LEDGER WO-0006 | |
| 2026-10-24 | Claude Code (with Haiku 5.5, Sonnet 5.5 and Opus 5.5 sub-agents) | Keel's self-directed runs and IPS work: ladder reprice (SD-T03), vote set B options and ballot (SD-T04, SD-T12), IPS rule checklist (SD-T05), TIPS/STRIPS wording (SD-R11), AI-use gaps (SD-T11), markets and rules check, Courtroom, Library, Lab L-01 to L-05, Laura's Room inflation test, Writing Room counts, Long Room motif and cold naming test, IPS edits v1-v3 (WO-0007, LR-2026-10-24b, SD-LAB-05), this Archive check | LEDGER rows of 24 Oct | |
| 2026-10-23 | (students to confirm) | Which words in the three TNA reflections came from an AI draft or exemplar, and which were the writers' own | | students to confirm at the TNA retro |

## How this was checked
TNA text: Google Docs read of the IPS Report Doc (read only; no suggestion or comment made), tab "Trading Notes"
(`t.xhphc2882vkp`), 0 pending suggestions. Counts: `textcheck.py`. Wording trace: 4-gram overlap script (session
scratch, not kept; rerun by tokenising lowercase words and intersecting 4-word runs). Ledger: every `keel/office/LEDGER.md`
on every remote branch compared by row ID with the day branch.
