# Q5b research card: keeping 30%, half or 70% of the shares, in numbers

Sat 14 Nov 2026, Sydney. Report part: 3b (the facility contribution and her flexibility; the recommendation sentence),
with a knock-on for 3c (the range's width) and 3e (what the split assumes). Notes for the Final Report store, not
report prose. Every figure is MODEL (Keel's calculation, not a forecast or a promise), from `NUMBERS.md` 8o
(`numbers/kept_share.py`, `numbers/results_kept_share_2026-11-14.json`).

Checked against: Caplet's FINAL IPS (`../../FINAL_IPS_as_submitted.txt` l.15, frozen: "half of the value of the shares
will be promised to no one. That is your flexibility – for building costs that overrun, a stronger Taiwan dollar or a
co-sponsor falling short. Before you meet co-sponsors in 2031, the other half will move into Treasuries"), `CANON.md`
(A30, A31, D1, D12), `WORDS.md` (her flexibility = the half of the shares promised to no one, about $21,300; "about
$29,800" only as her flexibility plus anything above the top), `NUMBERS.md` sections 4, 8f, 8j, 8k, 8l, 8n, and card
Q5 (`Q5_is_half_right.md`: the overrun norms of 13% and 17%; no contingency is sized and no building cost estimated,
case l.106-107, l.164). The plan is frozen: 70% and 30% are benchmarks that show the trade-off half made, never a
change to propose.

**Claim tested.** Keep, kill or change: "Keeping half of the shares unpromised (IPS l.15) is a sound split between
what Laura can promise co-sponsors in 2031 and what she keeps for the three named uses (cost overruns, a stronger
Taiwan dollar, a co-sponsor falling short). Moving 70% of VT (keeping 30%) or moving 30% (keeping 70%) would be worse
on balance."

**Problem class.** A split between a firm promise and an owner's reserve, with one lever (how much of the risky
asset becomes the promise). The trade-off is a straight line in money; the choice turns on which risk the owner would
rather carry. Card Q5 holds the prior art (cost engineers' contingency, Norway's owner reserve); this card adds the
numbers on Caplet's own engine.

## Verdict in one screen

**CHANGE.** Half is a defensible middle of a nearly one-for-one trade, not an optimum, and only one of the two
comparisons shows "worse".
- **"A sound split": KEEP, reworded.** On today's market rates half gives a stated top of $115,000 and leaves her
  flexibility $21,347 plus $8,476 above the top ($29,823). Each $5,000 more promised would cost about $5,266 of what she
  keeps; her total barely moves with the split (a median $372, $877 or $1,094 either way, on the three bases).
- **"Moving 70% would be worse on balance": KEEP for the uses IPS l.15 names.** It adds about $10,000 to the
  contribution, but her flexibility alone covers a 10% stronger Taiwan dollar in 50.0% of simulated futures (93.2% at
  half), 62.2% and 64.1% on history; its 1-in-20 low is about $5,900.
- **"Moving 30% would be worse on balance": KILL.** It costs about $10,000 of contribution in the simulated futures
  ($5,000 at today's rates: $110,000) and adds about $8,300 to what she keeps; her flexibility alone then covers a 10%
  stronger Taiwan dollar in 98.9% of simulated futures and every starting month since 1962. The numbers show a smaller
  promise for a larger cushion, not a worse plan. Preferring half over 30% is a judgment about the contribution's size
  (card Q32), Caplet's call, not a model result.
- **The 3b recommendation sentence** a lay reader asked for ("the most she can give while keeping about $30,000 for the
  three things that could go wrong") holds at today's market rates, if the $30,000 is named as her flexibility plus
  anything above the top and kept as the central figure: $115,000 is the highest $5,000 step that keeps about $30,000;
  $120,000 would keep about $24,700.

## (a) Table

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | On today's market rates: move 70% gives $95,000 to $125,000, contribution $125,000, her flexibility $12,808 ($19,403 with anything above the top); half gives $95,000 to $115,000, $115,000, $21,347 ($29,823); move 30% gives $95,000 to $110,000, $110,000, $29,886 ($35,243) | Keel model, `numbers/kept_share.py` | HALFKEPT, MOVE2031, RANGE2031 | NICHE (Keel model) | The three points of the trade half sits between; the bottom ($95,000) is the same in all three | Central only; the top moves in $5,000 steps, so +$10,000 one way and -$5,000 the other | MODEL; the plan's column reproduces NUMBERS 4 to the dollar | benchmark only: IPS l.15 is frozen at half | NUMBERS 8o, table rows 1-5 |
| 2 | Each $5,000 more of stated top costs about $5,266 of what she keeps (her flexibility plus anything above the top): $35,272 / $30,006 / $24,740 where the $110,000 / $115,000 / $120,000 steps start (28.6%, 41.3%, 53.9% moved) | Keel model, `central_frontier` | HALFKEPT, MOVE2031, RANGE2031 | NICHE (Keel model) | The 3b sentence "the most she can give while keeping about $30,000" is this line read at $115,000 | Central only (today's market rates, VT 7.5%); inside a step only the mix of shares and Treasury money moves | MODEL | no, if said as a description of half's result, not as how half was chosen | NUMBERS 8o, "The trade at the centre" |
| 3 | The split barely changes how much Laura has: contribution plus her flexibility plus anything above the top differs from the plan by a median $372 (simulated futures), $877 (US stocks) and $1,094 (rates and stocks together), either way | Keel model | HALFKEPT, MOVE2031 | NICHE (Keel model) | The split decides what is promised and what stays hers, not how much there is | Linear in the share moved, so the two benchmarks mirror each other exactly | MODEL | no | NUMBERS 8o, "The total barely moves" |
| 4 | Her flexibility alone covers a 10% stronger Taiwan dollar on the contribution in 50.0% / 93.2% / 98.9% of simulated futures (move 70% / half / move 30%); 62.2% / 96.9% / 99.4% on US stocks; 64.1% / 99.3% / 100% with rates and stocks together | Keel model; 8j's test | HALFKEPT, INFLATION_TWD | NICHE (Keel model) | Moving 70% halves the Taiwan dollar cover from her flexibility; half keeps it about 93 in 100 | One use at a time; the contribution is the stated top in every future | MODEL; the plan's column reproduces 8j (93.2%, 13,618 failures; 96.9%; 99.3%) | no | NUMBERS 8o, Taiwan dollar rows |
| 5 | With anything above the top: 97.9% / 99.77% / 99.89% of simulated futures; on the real Taiwan dollar since 1983 (417 windows), her flexibility alone 91.6% / 98.1% / 100%, with anything above 97.6% / 99.8% / 100% | Keel model; Fed G.5 monthly (FRED EXTAUS, mirror verified in 8l) | HALFKEPT, INFLATION_TWD | NICHE (Keel model) | Even at 70% the Treasury money above the top carries most of the Taiwan dollar test | The real-currency test runs on US stocks at today's market rates | MODEL; the plan's 98.1% with the same eight failing starts and 99.8% as 8j | no | NUMBERS 8o |
| 6 | Her flexibility as a share of the stated top, median (1-in-20 low): 10.0% (5.4%) / 17.8% (9.4%) / 26.7% (13.7%) in simulated futures; centrally 10.2% / 18.6% / 27.2% | Keel model | HALFKEPT | NICHE (Keel model) | The percentages card Q5 compares with builders' contingency norms; never a building cost | 8f divides by what the funds pay (9% / 17% / 30%), not by the stated top | MODEL | no | NUMBERS 8o |
| 7 | Against card Q5's overrun allowances (an illustration): her flexibility alone covers 13% / 17% of the contribution in 23.1% / 6.5% (move 70%), 79.7% / 54.9% (half), 96.2% / 87.3% (move 30%) of simulated futures; with anything above, 84.8% / 44.3%, 98.7% / 91.0%, 99.7% / 98.5% | Keel model; card Q5 (Denmark +13% for 80%; GSA about 17%) | HALFKEPT | NICHE (Keel model) | At half, about a fifth of the top is a first cushion for overruns alone, as Q5 found | Not a sizing (case l.106-107); the three uses never tested together | MODEL; the plan's column reproduces 8j's overrun rows | no | NUMBERS 8o |
| 8 | Her flexibility on 1 Jan 2033, 1-in-100 / 1-in-20 / median: $4,000 / $5,900 / $12,400 (move 70%); $6,670 / $9,881 / $20,739 (half, as 8f); $9,300 / $13,800 / $29,000 (move 30%); median if shares fell over 2031-2033: $9,300 / $15,423 / $21,600 | Keel model | HALFKEPT | NICHE (Keel model) | The cushion is smallest in the years co-sponsors cut (8f), at every split | Simulated futures; history is kinder (US stocks: 1-in-20 $7,900 / $13,238 / $18,500) | MODEL; half reproduces 8f | no | NUMBERS 8o |
| 9 | Range width in simulated futures, 1-in-20 / median / high: $15,000 / $25,000 / $45,000 (move 70%), $10,000 / $20,000 / $35,000 (half), $5,000 / $10,000 / $20,000 (move 30%); $5,000 wide or less in 0.5% / 1.6% / 13.9%; one figure in 144 / 254 / 882 of 200,000 | Keel model; 8l (254) | RANGE2031, MOVE2031 | NICHE (Keel model) | Keeping 70% makes the range co-sponsors hear narrower, often near one figure | A narrow range is not wrong in itself; it is a smaller ceiling | MODEL; half reproduces 8l's 254 | no | NUMBERS 8o |
| 10 | The contribution falls inside the stated range in every future and window at all three splits; the stated bottom and the floor are identical across splits | Keel model; completion.rule | RANGE2031, MOVE2031 | NICHE (Keel model) | The rule, not the split, keeps the contribution inside the range | None recorded | MODEL; checked in every future (`checks`) | no | NUMBERS 8o |
| 11 | Against the plan, future by future: move 70% adds $10,000 to the median contribution (+$5,000 to +$15,000) and takes $8,300 from her flexibility plus anything above; move 30% the mirror image | Keel model | HALFKEPT, MOVE2031 | NICHE (Keel model) | The price of each $10,000 of promise is about $8,300 of cushion at the median | Simulated futures; both history bases give the same contribution steps and about $9,200 to $9,800 of cushion | MODEL | benchmark only | NUMBERS 8o |

## (b) Verdict

**CHANGE.** Reasons, all from NUMBERS 8o:
- Keep that half is sound, as the middle of a nearly one-for-one trade: about $5,300 of what she keeps for each $5,000
  more promised, at about the same total (row 2, row 3). The model does not find half to be best; it finds the line half
  sits on.
- Keep that 70% is worse for the uses IPS l.15 names: her flexibility alone would meet a 10% stronger Taiwan dollar in
  only about half the simulated futures and about 6 in 10 historical starts, and its 1-in-20 low falls to about $5,900
  (rows 4, 6, 8).
- Kill that 30% is worse on balance: it is a smaller promise ($110,000 at today's rates; about $10,000 less at the
  median of the simulated futures) for a larger cushion (about $8,300 more), with better Taiwan dollar cover and a
  narrower range (rows 1, 4, 9, 11). Whether a $115,000 top is worth the thinner cushion is the contribution question
  (card Q32), a judgment Caplet made in l.15, not a result.

**Changed claim (a note, not prose).** Half sits in the middle of a nearly one-for-one trade between what Laura
promises and what she keeps. At today's market rates it gives a top of $115,000 with about $30,000 kept (her
flexibility, about $21,300 of shares, plus about $8,500 above the top); each $5,000 more promised would cost about
$5,300 of that. Moving more would leave her flexibility too thin for a stronger Taiwan dollar in many futures; moving
less would keep more for a smaller promise.

**Where it lands.** 3b: the recommendation sentence, with the $30,000 named as WORDS requires and the order of cause
the IPS's (half first; $115,000 follows). The trade line ("about $5,300 for each $5,000") is one clause at most. The
70% and 30% figures stay in the store; the report never offers them as choices.

## (c) Gaps

- The co-sponsor use has no test: no co-sponsor's size or shortfall is modelled (case l.106-107).
- The three uses are tested one at a time, never together (card Q5).
- Stocks and rates are drawn apart in the simulated futures (NUMBERS 7); US stocks since 1871 grew faster than the
  7.5% assumed, which favours keeping more shares there.
- The move is modelled on 1 Jan 2031; the split is the only lever changed.
