# Writing Room, Wed 28 Oct 2026 (16:20 run, round 1 beat 7): the three cures for the coupon gap, side by side

(Keel is a simulated team, AI-written.) AI DRAFT material (Claude, 28 Oct 2026); suggestions only, not for submission.
Round: `../../loop/rounds/2026-10-28.md`. Splice texts (full IPS each, counted) and the script that builds them:
`../../drafts/writing_room_2026-10-28/`. Numbers are Laura's Room's and the Lab's (LR-05, L-11; curve 22 Oct 2026,
J.P. Morgan 7.5% world stocks, 200,000 paths, seed 20261016, MODEL); this room ran no new model.

**For a judge, first.** V28 says one rule drives every date: "each promise is made safe no later than the day it
becomes one". Two cold judges who had never seen it read the soft-spot paragraph three ways. Both put V28's own
wording **last**, and both quoted the same sentence as the place the plan breaks its own rule: the coupon gap is "the
one thing that can still trim the gift", and the fix waits until January 2033, two years after the gift becomes a
promise. The two fixes that act earlier finished one each: one judge put the 2031 pricing first, the other put the
2028 holding first. So the choice tonight is between those two, not about V28's sentence, which goes either way.

## 1. Claim sets (beat 7: each challenger beside the champion)
| | Claim, at most 15 plain words | What changes for the judge if it wins | Cold judges (strategy / client, /10) |
|---|---|---|---|
| **C6, champion as in V28** | In January 2033, any coupon shortfall plus a cushion goes into the next fund to mature. | Nothing new. The gift can still be trimmed after it's named (2.2 / 3.3 / 30% of paths, S0 / S1 / S6, LR-05) | 6/7 and 5/5: last both times; "contradicts its headline rule" |
| **C6 + mark carries the cushion** (LR-05) | In 2031 the coupon gap falls on Laura's spare money first, then the bottom, before she names it. | The rule has no exception after 2031: the bottom is quoted net of the gap, and is never broken in 200,000 paths (S6: 29). Co-sponsor signal lost 1.4% | 8/8 (first) and 7/7 (second): "priced on the day the range becomes a promise"; "bends" the rule, because the money sits in her stocks 2031-33 |
| **A, the coupon holding** (L-11) | The 2028 deposit buys a Treasury holding for the coupon gap before the floor. | Cleanest version of the rule (paid for in 2028), but the bottom is about $10k lower in the median path. Signal lost 6.6% | 7/8 (second) and 8/8 (first): "the best idea underneath, explained worst"; both judges had to read its two sentences twice |
| D, thin-coupon twins (parked) | Buy the thin-coupon 2041 bonds: same date, half the coupon gap. | Final Report until the Trading Desk prices them (Sat 31 Oct) | not read |
| B (show report), C (Redington) | binned for the IPS by the Lab and Laura's Room | Final Report, "priced and turned down" | not read |

**The Writing Room's lean, for the Long Room (Keel proposes; the Long Room votes at 18:20): C6 + mark.** The judges
tied A and C6+MC 15 to 15, so the tiebreak is what each costs Laura's word. C6+MC keeps the bottom about $10k higher, is
never broken, and costs co-sponsors a quarter of what A does (LR-05). It also tells better against the locked TNA:
IBTM already "does two jobs", and here the floor stands behind the cheques until the day Laura names her gift. What A
does better is the rule's purity, and that can be borrowed in words. One judge also caught a real flaw in A: if the
holding is ever sold to cover a gap, a Treasury is "sold before it pays", which breaks our own closing line.

## 2. The lines, spliced into V28 and counted (`textcheck.py` rules: quote the larger count)
Every version also carries the five fixes in section 3. **Counts: C6 495, C6+MC 498, A 500 (limit 500), pitch 50.**
- **C6+MC, paragraph 9:** "The fourth is our soft spot, so it is priced in 2031: any gap the bond market has already
  shown her, plus a cushion, falls on spare cash and her half before the bottom. In January 2033 that money moves into
  the next fund to mature." (Keeps the Courtroom's line, "already shown her".) Both judges had to read "before the
  bottom" twice: if words allow, change it to "before anything comes off the bottom" (+3, which makes 501, so it needs a
  cut elsewhere first).
- **A, paragraphs 6 and 9:** "That deposit buys a Treasury holding for the coupons, then the floor ..." / "The fourth
  is our soft spot, so it is paid for in 2028: that holding, hers after the tenth cheque. In January 2033 money for any
  gap already showing goes into the next fund to mature, from leftover cash and her half." Not yet fit to send: both
  judges asked which holding, how big, what maturity, and "for the coupons" reads as buying a bond for its income. Saying
  what it does takes about 12 more words. Space for them: drop "hers after the tenth cheque".

## 3. Hard issues on V28 (`../drafts/D8/`), at most five, each a minimal edit
1. **Counts.** IPS **499** by spaces (496 split; README says 498, but the 28 Oct rules fix added one word); pitch **50**.
   Margin 1 and 0. How SMApply counts words is UNVERIFIED (a counter that splits on spaces counts each spaced en dash
   as a word). Every edit below is word-neutral, or paid for by the cut in item 5.
2. **"So her first $300,000 buys them in January 2027" is a one-close fact** (the Window's request; headroom $1,139 on
   22 Oct; over $300k in 46-47% of MODEL paths). Edit: "...in January 2027, and her second fills any gap:" (+6) and, in
   paragraph 6, "That deposit fills any gap in the ladder, then buys the floor" -> "That deposit then buys the floor"
   (-6). The two halves now sit in one sentence. Judge 2 also saw the strain that's left over: the deposit the IPS calls
   "money she expects" still fills a cheque gap. That is true (the IBTR note says so), and the clause makes it visible.
   Sizing the gap is a job for the Lab (open request, corner for line 3b).
3. **Laura's half is booked twice** (Laura's Room; Archive A19): it pays the coupon cushion first (paragraph 9) and is
   "for" building costs (paragraph 10). Edit: "that is what the rest of Laura's half, sellable any day, is for" (+3).
   "Sellable any day" stays, because it is the IPS's one line on liquidity, and Book 7 asks for liquidity.
4. **"The promised half moves into Treasuries maturing before 2033"**: no WInS Treasury bond matures between Feb 2031
   and Feb 2036 (Trading Desk check, 28 Oct), so this can only be IBTM. Edit: "...moves into the first cheque's fund."
   (0 words). It calls back "the floor – more of the first cheque's fund", and that fund matures in December 2032.
5. **Too many endings that are quotable lines** (the panel's "too many aphorisms"; guide law 9 says at most three; V28
   has six). Cut "Keep the seed; risk only the harvest." (-7). That pays for items 2-4 and the winning splice. It's a
   whole idea dropped, not a line squeezed: the floor/stock split is already stated in the sentence before it.
   Also flagged by both cold judges, but left alone because it is wording: "sized to regrow the remainder by 2033.
   Roughly its expected interest buys a world index fund" ("regrow what remainder? whose interest?"). The rewrite
   thread should look at it on Friday.

## 4. Requests answered
- Window (Wed 28 Oct): (1) done as item 2; (2) T-bills were already gone in V28.
- Archive A19-A21 / A15: (1) item 3 and the C6+MC splice ("her half before the bottom", never a source that decides
  whether a cheque is paid); (2) "never reaches a payment" is not in V28; (3) "the floor she owns" passes A15.
- Courtroom (2031 sentence): V28 holds a rule and no "$145k", no "cut" or "margin"; the C6+MC splice brings back
  "already shown her".

Cold-read method: two general-purpose subagents, each told only the case in seven lines and the three full IPS texts
under shuffled labels (key: judge 1 X = C6+MC, Y = C6, Z = A; judge 2 X = A, Y = C6+MC, Z = C6). These are model
readers, a test and never a quote.
