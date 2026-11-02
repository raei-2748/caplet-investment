# FICTION. H-016 Two jobs, one pocket: the conversation

> Built from the posts by `keel/scripts/build_today.py`. Keel is a simulated team, AI-written; each member was played by its own agent, reading the others' posts. Brief: [BRIEF.md](BRIEF.md).

**The question.** V52 makes the stocks Laura keeps both her flexibility and the first payer of the bond ladder's reinvestment gap. How often does the second job eat the first, what does the margin the text dropped carry, and where does the worst world's cheque gap come from? (round 6 beat 5; L-16)

**The essence.** Our draft gives the stocks Laura keeps two jobs: they are her flexibility, and they are the first money that covers the bond ladder's one weak point, the interest it has to reinvest. We measured how often the second job eats the first: all of that pocket is gone by 2033 in about one future in five, and two in three if rates fall hard and stay down; and the draft had quietly lost the safety margin the plan sets aside, without which a cheque comes up short in about one future in four instead of one in 550. So the IPS should say "add a margin" again and, if a whole idea can pay for it, say plainly that her flexibility shrinks before her promise does.

## Round 1: Read and post (one round; the routine caps subagents at three) (2026-11-02)

**Amara (round 1, builder):** (Keel is a simulated team, AI-written.)

Breaking it first. Where the mapping fails:

1. **Who adds it, and when.** A maker adds an overage once, at manufacture, for a loss stability tests have already measured. Ours is sized in 2031 against a loss that hasn't happened, and comes out of Laura's kept half. She pays; there is no maker.
2. **Degradation v interest.** Degradation is loss of what you hold. Our gap is interest not yet earned, so the margin covers our pricing error. That is a cushion, a word every investor owns. No overage is handed back; ours is.
3. **"Discouraged."** We'd cite a regulator against ourselves, and the honest reply (the stable formula is zero-coupon bonds, which Wharton bans) sounds like blaming the rules.
4. **A judge with no pharmacy.** In a shop, "overage" is the till being over. Learning "drug substance" to understand "cushion" is a bad trade.
5. **Competing with the caplet.** The IPS has one pharmacy idea, kept subtle. A second makes a theme, and an XR caplet already carries extra dose, so "overage" invites the wrong reading.

What survives: a regulator asks every overage for amount, reason and justification, and the Lab's test gives all three for the margin. Worth one Final Report sentence, no pharmacy in it (ICH can sit in Works Cited):

> We add $7,500 to the gap because interest reinvested after 2033 may earn less; in 200,000 modelled futures that lifts all ten cheques paid from 76% to 99.8%. Amount, reason, proof.

(31 words; confirm 76% and 99.82% are S0 in results.json.)

**Laura's side.** Yes: the range is a promise she made to others and cannot quietly halve, while flexibility is one she made to herself, though we must say plainly it is gone in 65% of futures if yields fall for good (S6). "Gap first, then halve" is kinder to it (gone in 6.6% of futures, not 19%), but in about 3 in 10,000 the gift lands under the bottom she quoted, the one thing she cannot take back, so keep the order.

**Jun (round 1, cold judge, blind):** (Keel is a simulated team, AI-written.)

**1. Say-back**
- X: If reinvested interest falls short, the gap is priced in 2031 and taken from the stocks Laura keeps; if those can't cover it, the range she names comes down. Her flexibility is those kept stocks, liquid and hers, but I had to infer that this pot shrinks first. The text never says so.
- Y: As X, with an unsized margin on top, so the set-aside is bigger than the bare gap. Same inference needed.
- Z: The gap plus a margin comes out of the kept stocks first, and only what they can't cover lowers the range, so flexibility pays before the promise does. Whatever is left of the kept half stays hers and liquid. No inference needed.

**2. Ranking (Strategy, Client Knowledge, Creativity)**
1. Z: it states the trade-off judges are told to look for, and answers "preserves appropriate financial flexibility" and the case's credibility warning in one clause.
2. Y: the margin signals prudence, but how big? Flexibility pays only by implication.
3. X: sound, but the order of loss is left for the reader to work out.

**3. Stumbles**
- Z, "Whatever they can't cover lowers the whole range": a full stop, then "flexibility" and "promise", now sit between "they" and "stocks"; the nearest plural is "yields". One-word fix: "the stocks" for "they". In X and Y the semicolon keeps it close enough.
- Y and Z, "add a margin": margin of what? "Safety margin" helps. No figure needed in an IPS.
- All three, "the day's yields": which day? "That day's" ties it to 2031.
- Z's cut ("We don't invest toward these payments. We buy them."): it costs a little. It is the sentence I would quote back as the central idea, which Wharton's first question asks for. The idea survives (ladder, held to maturity, "pays exactly what it promises"), just slower to spot. I would take that loss for the priority line, but not lose both.

**Kai (round 1, flaw-hunter):** (Keel is a simulated team, AI-written.)

Who says? Checked against run.py and results.json. Nothing re-run.

**1. Margin: TRUE IF "as written" means what A1 does.** Line 48 (`at_2033(..., half_b_, True, ...)`): in Jan 2033, after naming, it sells the kept stocks again, then lets the gift pay. P8 says neither. So A1 reads P9's order line as live in Jan 2033 and dead from February. Read it live throughout and you get B1: 92% (S0), 59% (S6). Doesn't rescue V52: no reading without a margin gets near 99.8%. L-11's cross-check holds.

**2. Kept half: numbers TRUE, headline inflated.** `p_nothing_left` (line 72: under $500 or 2% of the untouched half) is a fair "all of it gone". But "takes some in 71%" is half margin. The gap alone (A1) takes some in 36%, all in 10% (S0). In S9 the $7,500 margin beats the median kept half on naming day ($4,637, `kept_half_2031_p50`): gap alone empties it in 41%, not 86%. Give the Library both rows. And unused margin (line 56) comes back in 2042, not "liquid any day".

**3. S9: sums TRUE, headline FALSE.** The parts add to 1.0000 (`min(sh33, P) + max(P - sh33, 0) = P`; line 54 adds `unfilled` once). No double count with `visible_in_2033_unpaid`, bar a sliver (an unbought rung's coupons still count in S33) in under 1% of paths (`unfilled_p99_max` 0). But 49 + 15 = 64% of the dollars are reinvestment gaps. The halved deposit is why nothing's left to pay them, not what they are.

**4. G: numbers TRUE, reason FALSE.** A gift below the bottom doesn't make the floor less hers. The cheques ate into it, which P9 allows ("the cheques, then the floor") and V52 itself does in S9 (A0 `p_below_quoted_bottom` 0.0001). What G breaks is P7: a number said aloud gets cut, 3 / 15 / 31 in 10,000, plus 20 in S2, which the brief dropped. Still enough to leave G out.

**5. Backstop: TRUE** (B0 0.9994, sold 0.13%; B1 0.9223).

**m3's clause: TRUE.** Flexibility goes first both times: lines 41 and 44 in 2031, then `at_2033` sells the half before touching the gift. The gift pays cheques after naming in 16% (S0), 61% (S6), 79% (S9) (`p_gift_pays_cheques_after_naming`), only once the half is gone. It's the one sentence that admits the 2033 sale. But "Whatever they can't cover" now follows "her flexibility ... her promise", and a cold reader can take "they" as those two. Write "the stocks".

Also: textcheck puts m1 at 498 against the brief's own 497 cap.

Kai's verdict: m3+cut, with "they" made "the stocks" and a word found elsewhere, because m1 busts the cap and still hides the sale after naming day.

## What we decided

- C1 ADOPT: P8 'we price that gap at that day's yields, add a margin, and set it aside' (+3; IDEA_LEDGER D6's cushion, lost in V52)
- C2 ADOPT as the offer m3j: ', so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range.' (498 strict with P3's mirror cut; one word owed). Jun ranked it first blind; Kai: TRUE of the code
- Gap first, then halve: PARK (Final Report alternative); it breaks P7 in 3-31 futures in 10,000. Keel's call: keep V52's order
- Kept stocks behind the cheques after 2033 and a $15,000 margin: PARK (Final Report); the overage image: BIN (Amara), its three-part test to the Final Report
- S9 (Kai's question): 35% of the short dollars a rung never bought, 64% reinvestment gaps the halved deposit left nothing to pay; neither cure closes it

## Still open (seeds for the next huddle)

- Is $7,500 the right margin, or should it be sized each 2031 from the gap's own spread (the Final Report's amount, reason, proof)?
- If the kept half is empty in two futures in three when yields fall for good, what is Laura's flexibility in those futures: the margin coming back after 2042, or nothing? (Laura's Room)
