# D34 (V54): Ten Commandments check + Book 11 check, Tue 3 Nov 2026 (Sydney)

AI-generated (Claude Code), not for submission. GPTZero: not yet checked.
A cold check by a reader who did not write V54. I'm not a detector, and nothing below is an AI-likeness score.

**Tally. Commandments: PASS 4 (II, III, V, VII) · FAIL 3 (IV, VIII, X) · OPEN 3 (I, VI, IX).
Book 11: PASS 7 (1, 2, 3, 4, 5, 8, 9) · FAIL 1 (6) · OPEN 1 (7).**
By the Bible's rule ("A draft with a failed line does not go to Caplet"), V54 isn't cleared. Only IV / Book 11.6
touches the text, and its fix costs 0 net words. VIII and X are record-keeping, at no word cost.

**What was checked.** `ips_V54.txt` (md5 `db37137b…`, file time 21:02 UTC 2 Nov): **497 strict** (496 by spaces, 497
split on hyphens), at the house cap. `pitch.txt` (md5 `99ab8e14…`): **50**. Counts from `keel/office/tools/textcheck.py`,
quoting the larger number. Checked against `WHARTON_WORD.md`, `BIBLE.md` (Books 1-5, 9, 10, 11, the commandments), the
case, `voice/06_voice_guide.md`, `IDEA_LEDGER.md`, `THINKING_LOG.md`, `00_GROUND_TRUTH.md` section 3 (the locked TNA)
and the D34 README. `judges/panel_V54/` holds prompts, entries and a blind key, but no results yet.

## The Ten Commandments

| # | Verdict | Reason (V54's own words) |
|---|---|---|
| I | **OPEN** | The test is met: three ideas a judge could retell, none the field's default. "Laura's career already behaves like a stock"; the floor plus its interest as a bank note without the option ("they spend that interest on an option, which expires worthless if the market stands still. Shares don't."); and "Crushing one means selling it before it matures, even for the building." No "every team". Whether the page makes a judge sit up is unproven: panel V54 hasn't reported, and V52 came fourth of six |
| II | **PASS** | All five IPS questions are answered as a whole. The central idea is in P3 plus the pitch. The principles: "every dollar she promises is already in bonds", "so her flexibility shrinks before her gift does". The balance: growth ("one world index fund"), liquidity ("liquid any day"), reliability (P3), flexibility ("as her flexibility"). Change over time runs 2027 → 2028 → 2031 → 2033. Protection plus flexibility: P6, P8. Wharton's "reasoning, assumptions, and tradeoffs" are there: "We assume ... 7.5%", and P7's refused alternative. No final range, no projections |
| III | **PASS, narrowly** | The moves, quoted (the test wants them in the README, so the README should link this file). A sentence that builds and a short one that lands: P4 "– income that can dry up in the kind of downturn that makes a ladder dearer to buy. If that deposit arrives smaller, the gift shrinks." A concession, then "But": P7. A wry line: "Shares don't." Contractions ("couldn't", "can't"), "cheques", "labelled", en dashes. V53's triad ("the cheques, then the floor, then ...") and its mirror ("We don't invest ... We buy them.") are gone from the IPS. Against: P5 reads as a fact sheet ("That is her floor." / "That is under a tenth of her money." / "Shares don't.") |
| IV | **FAIL** | P5: "Banks sell this as a capital-protected note, but they spend that interest on an option, which expires worthless if the market stands still. Shares don't." "this" has no noun, and "Shares don't" leaves the verb for the reader to supply. V53's cold read marked this sentence LOST, and V54 hasn't changed it. Smaller pauses are under (a) |
| V | **PASS** | Case sums and dates ($50,000, ten, $300,000, 2027/28/31/33). One plan date ("late 2032"). One allocation that follows from the sentence before ("roughly the interest it should earn ... under a tenth of her money"). One assumption that says who and what rests on it ("We assume ... but the cheques never depend on it"). No "we judge", no model output |
| VI | **OPEN: not yet checked** | No GPTZero score for the IPS or the pitch. The D34 README says the scan was refused by the session's permission check. No agent stood in for a detector |
| VII | **PASS** | It can be said in three sentences. (1) The 2027 money buys a Treasury for each cheque, never sold early. (2) The 2028 money buys a floor and puts only its interest into world shares; in 2031 half the shares move into bonds to make the top of the range. (3) The reinvestment gap is priced and set aside before naming. Caution: P5 (7 sentences) and P8 still carry mechanism ("add a cushion", "in Treasuries") |
| VIII | **FAIL** | The ledger stops at V52. Two drafts' worth of cuts have no recorded landing: V54's "We don't invest toward these payments. We buy them." (now pitch only) and V53's "The order never changes: the cheques, then the floor, then everything above it." (ledger E4 lists it IN), plus V53's "about a fifteenth" → "under a tenth". The README gives reasons, but the ledger is what the test reads. The critique half is still owed: the bank note is critiqued, but what our version costs (a smaller share of a boom than the option would give) is never said |
| IX | **OPEN** | `panel_V54/` is blind and shuffled per judge: V53, V54 and four rivals across six judges. No SUMMARY and no rank correlations yet |
| X | **FAIL** | THINKING_LOG's last "What Caplet would say" entry is "Mon 2 Nov, morning" (V52). The V53 and V54 rounds have none. The work itself did improve unprompted (the Long Room's six blind readers, the Archive's A19) |

## Book 11, point by point

| # | Verdict | Reason |
|---|---|---|
| 1 No opening rhetorical question | **PASS** | It opens "In January 2033, Laura's portfolio writes the first of ten cheques". The text has no "?" anywhere |
| 2 No "our model" | **PASS** | No "model", probability or projection. "7.5%" is a labelled assumption, and "under a tenth" is an allocation |
| 3 No team history | **PASS** | None. P7 ("We could put the floor into stocks ...") is a refused alternative, not a past plan |
| 4 Full-circle XR | **PASS** | It is set up in P2 ("labelled do not crush. Crush it and the schedule is gone. ... Crushing one means selling it before it matures") and paid off in the last line ("Do not crush.") |
| 5 No subheadings | **PASS** | Continuous prose |
| 6 Plain sense | **FAIL** | The same sentence as IV: the bank-note sentence |
| 7 Sound human | **OPEN** | GPTZero not yet checked. By ear: row III |
| 8 Wharton's guidelines | **PASS** | Strategy and framework, one assumption, no calculations. "Flexibility", Wharton's word, is present |
| 9 Overdrive | **PASS** | D34 drew on four rooms, six blind readers and a blind cross-read, and a six-judge panel was built within hours. The ledger and log gaps are counted at VIII and X |

## The three questions

**(a) Does every sentence make plain sense on one read?** No, one does not:
- P5, the bank-note sentence (LOST; see IV).

These made me pause, but I understood them on one read:
- P5 "The remainder, roughly the interest it should earn": "it" means the fund, but the nearest noun is "remainder".
- P8 "set it aside, in Treasuries, from the stocks Laura keeps, so her flexibility shrinks before her gift does": three
  phrases stacked between commas.
- P8 "Whatever the stocks can't cover lowers the whole range": which stocks (the kept half, or all of them), and does
  it lower both ends?
- P4 "the kind of downturn that makes a ladder dearer to buy": it needs the step that falling yields raise bond prices
  (fine for a judge).
- P3 "funds that mature like bonds" (slight).
- Pitch "Treasuries that each mature before a January": which January?

A logic question a careful judge may ask, though no sentence fails: if "every dollar she promises is already in bonds",
why name a range and not one number? The answer (the reinvestment gap, and "rounded down") sits two paragraphs later and
is never joined up. That belongs in the Final Report, not here.

**(b) Is anything false against the case or a checkable fact?** I found nothing false. Three soft spots:
- P1 "to fund her Taiwan residency". The case says the payments go "toward the residency's operating expenses"
  (:88), and the facility is separate (:84). It reads a little broad. Optional: "to help run her Taiwan residency"
  (+1, so it needs a word paid back).
- P4 "If that deposit arrives smaller". The case fixes $150,000 for projections (:131). This is our stress case, built
  on the case's own list of income sources (:44). It is defensible, but it is our assumption, not the case's.
- "about 7.5%". J.P. Morgan's 2027 LTCMA, global equities (the Window, 27 Oct). The 2026 edition filed in the repo says
  7.00% for AC World. The Final Report must cite the 2027 edition and say whether the figure is compound or arithmetic.

These hold:
- "ten holdings, one redeemed for each January" and "one rung falling due before each cheque" fit the locked TNA (IBTM
  to IBTR plus five T-bonds; the Feb-2037 bond's cash waits for the 2038 cheque).
- "under a tenth" holds at plausible yields.
- "expires worthless if the market stands still" is true of the usual note (a zero-coupon bond plus a call option).

**(c) Does the intro set up "do not crush", and does the last line pay it off?** Yes. P2 states the label, its harm
("Crush it and the schedule is gone") and what it means in portfolio terms ("selling it before it matures, even for the
building"). The last line repeats the label alone. P8 earns it: the shortfall comes out of the gift ("lowers the whole
range"), never out of a rung. One caution: there are four "crush" words in P2, which is the motif at full volume in one
place (Book 2's "subtle"). It is the setup, so I let it stand.

## Fixes (measured with textcheck on a scratch copy: **497 strict**, pitch 50 unchanged)

1. **IV / Book 11.6, the bank-note sentence (+3).** Old: "Banks sell this as a capital-protected note" → New: "Banks
   sell the same idea as a capital-protected note". Old: "Shares don't." → New: "Shares don't expire." (V52's words).
2. **The payer: cut one whole idea (−3).** Old: "The top adds half her stocks, valued that day." → New: "The top adds
   half her stocks." The next sentence ("Before she names it, that half moves into Treasuries") already fixes the day.
   I didn't cut "rounded down": it is the bottom's margin against the floor fund's NAV, which isn't a fixed payout (TNA
   note 2).

   Net: +3 −3 = 0, so the IPS stays at **497**.
3. **VIII (0 IPS words).** Add a V53-V54 entry to `IDEA_LEDGER.md`:
   - the mirror line: pitch only;
   - the order line: OUT, with the reason (not true on naming day);
   - A5 (crushing = selling early): back IN;
   - the set-aside: now in Treasuries and part of the reserve;
   - our version's cost against the note: Final Report, or a clause if words free up.
4. **X (0 words).** A THINKING_LOG entry for the V53-V54 round ("what Caplet would say next"). My guess: "Read P5 aloud.
   Does it sound like us?"
5. **Process.** Link this file from the D34 README, rerun the cold read on the fixed P5, and add panel V54's SUMMARY
   with rank correlations before the draft goes to Caplet.
