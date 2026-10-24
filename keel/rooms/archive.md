# The Archive: what is locked (real records)

> **State (last run Sat 24 Oct, 19:30 AEDT, Tess).** Locked text held below word for word (TNA read from the live Doc
> 24 Oct; all 11 WInS notes identical to the 14 Oct export). Coherence register A1-A10: 0 contradictions, 3 WATCH
> (A1 stock return 7.5%, A2 inflation scope, A4 no price-triggered sales). LEDGER on the day branch now carries every
> AI use found on any branch to 24 Oct 19:00 AEDT. AI_USE.md s5 rows staged below, paste due Sun 25 Oct (default in
> `../pm/ASK_HUMANS.md`). Next run: start from `git log --since` this time; re-read only changed IPS drafts and
> LEDGER/outbox; re-run the checks in "How this was checked".
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
Checked 24 Oct against: IPS edits v3 (`/mnt/project-files/ips/IPS_edits_v3_2026-10-24.md`, pitch 45 / IPS 471), Tab 15
export, vote set B options and ballot (SD-T04, SD-T12), Laura's Room option A, Lab L-03, Writing Room cut packages.
| # | Locked words | New work | Status | The rule from now on |
|---|---|---|---|---|
| A1 | VT reflection: "a forecast return of about 7.5% a year (as per JPMorgan)" | IPS V5 assumed 7% (2026 LTCMA); the 21 Oct teardown called 7.5% FALSE (EAFE row of the 2026 edition). WO-0003 (21 Oct): J.P. Morgan's 2027 LTCMA, released 19 Oct, puts global equities at 7.5%. IPS v3 states no return figure | **WATCH** | The locked line stands on the 2027 edition. Any stock return the IPS or Final Report states is 7.5% (2027 LTCMA) or says why it differs. The teardown's FALSE verdict is superseded once the Library confirms the 2027 figure at source |
| A2 | Reflection 1: payments "fixed in nominal dollars", so TIPS "would hedge against a nonexistent inflation risk" | IPS v3: "Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first"; Laura's Room option A adds a 3.5%/yr rate | **WATCH** (consistent today) | Inflation belongs to facility and overrun costs, never to the payments. No sentence may say inflation threatens a payment |
| A3 | Reflection 1: "a near-ironclad guarantee, and we provide exactly that"; reflection 2: payout "a net asset value, as opposed to a promise of par" | IPS v3: "every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short." | Consistent | The IPS definition is the "near" in "near-ironclad", spelled out. Don't soften it to "aim"/"likely" (reverses "we provide exactly that") or harden it to "guaranteed" (reverses the NAV line) |
| A4 | Reflection 1: "Every year the bonds sit untouched is a good year"; reflection 2: "we'll simply ignore price noise" | IPS v3 P6: "replacing any holding that becomes unavailable"; the "held without trading" sentence was cut. No D1-D6 option sells a payment holding | **WATCH** (consistent today) | A payment holding is replaced only when it becomes unavailable, never because of its price |
| A5 | IBTM note: floor "giving co-sponsors a minimum figure in 2031 ... although the final payout is not fixed" | IPS v3: floor = 2032 Treasury ETF, "quoted at the 2032 ETF's projected payout rounded down" | Consistent | Keep "rounded down" or an equivalent; never "fixed" |
| A6 | IBTR note: a yield fall means "the 2028 deposit would top up the ladder, leaving less for the facility" | IPS v3 (C2): "a rate fall before we buy lowers the floor, not a payment" | Consistent | The strongest echo across the set. Keep C2 |
| A7 | VT note: "her promised minimum" | IPS v3: "a floor Laura can quote" (optional "promise" -> "quote") | Low | Either word is fine; the IPS must not argue against promising, which would read as reversing a submitted note |
| A8 | Reflection 1 names TIPS, as rejected | Week 4 email bans TIPS/STRIPS; SD-R11: IPS names neither | Consistent | Rejected-on-merit is already on the record; the IPS needn't repeat it |
| A9 | No locked text uses roots, branches or "Root & Branch" | Ray, 24 Oct: name and roots motif out | Consistent | Dropping it costs no coherence. A new motif must not contradict "VT is where we allow ourselves to be wrong" |
| A10 | (spine) North Star memo: "commit only money she already owns" | IPS v3: floor bought only from the 2028 remainder; the 2027 deposit goes to payments | Consistent | `00_SPINE.md` (PR #25) is not on the day branch yet; the memo governs until it is |

## The AI-use record
`../office/LEDGER.md` (one row per office answer) and `../../caplet/docs/AI_USE.md` (lines for the Works Cited).

**Wording trace of the TNA reflections (24 Oct, records only).** 4-word runs shared with every Markdown/CSV file in
the repo (474 files): before 23 Oct, no AI file shares more than a generic phrase ("payments are fixed in"; "about 7.5% a
year", in the 21 Oct teardown that told the team to delete it; "across countries and sectors"). Every longer match is a
file written on or after 23 Oct that quotes the submitted text (VOICE.md, ladder record, L-03, SD-T04). This covers repo
files only, not chats (ChatGPT, Claude.ai) or the Doc's suggestion history. It is evidence for the students, not an answer:
each writer still says what was theirs.

**Staged for `AI_USE.md` s5 on Sun 25 Oct** (SD-T11's eight rows, with the last row completed to 24 Oct 19:00):
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
