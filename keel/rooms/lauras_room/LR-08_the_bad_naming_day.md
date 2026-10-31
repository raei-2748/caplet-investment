# FICTION (the room and the simulated people) + the real case. LR-08: the bad naming day

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), Sat 31 Oct 2026, Laura's Room, round 4
beat 6 (Amara). Not for submission. Simulated co-sponsors and judges are tests, never quotes; no Laura quotes.
Run: `LR-08_the_bad_naming_day.py`, numbers `LR-08_results.json`. **MODEL**: curve 22 Oct 2026 (treasury.gov par),
J.P. Morgan 2027 LTCMA world stocks 7.5% compound, 16.78% vol; 50,000 paths in each of three worlds (house, storms,
bootstrap) plus every start month since 1871 (history, 1,636 paths); engine `../../models/xr_core.py`, unchanged.
Huddle: `../../huddles/2026-10-31_the-bad-naming-day/`.

## 1. Why this, today
Today's question is Q12, why not a safe ladder and the rest in stocks (rival A09, `../../ips_rewrite/rivals/A09.md`).
The Genius Lab's beat had not posted by 15:10, so the room took the three open requests for an A09 run (Rooftop,
Window, Library, `../../pm/REQUESTS.md`) from the one chair it owns: the co-sponsor's. After naming day both plans
lock what they name, so a co-sponsor holding the range in 2032 can't tell them apart. **What a co-sponsor ever sees is
the number Laura can name in 2031.** So the test is that number, not the gift.

## 2. The run
> **Corrected 31 Oct, after the PR #84 review.** The first run left out L-13's 2031 mark on the bottom (the projected
> coupon gap plus the cushion that Laura's own money can't cover comes off the bottom before she names it,
> `../lab/L-13_slide_the_range/run.py`). The reviewer was right: the mark cuts XR's bottom in 6-20% of paths, and
> more often when stocks are low, so XR's bottom does move a little with the market. Both plans now carry the mark
> and A09 is re-matched (f = 0.743). The first run said "XR one in two thousand"; the true figure is about one in
> 150. The direction and the price hold.

- **XR** as V45 describes it: the ladder; the 2028 floor (Treasuries to Dec 2032); the floor's expected interest in
  world stocks; the range named Jan 2031 with the lock and the $7,500 cushion (`caplet_xr(lock=True, cush=7500)`),
  then the 2031 mark on the bottom.
- **A09** at its strongest: the same ladder; the 2028 money 80% world stocks / 20% intermediate Treasuries,
  rebalanced each January; in Jan 2031 a share f of the pot is locked to Dec 2032 as the bottom (rounded down to $5k),
  the rest goes to stocks; top = locked face + half the rest; the promised half locked on naming day as in XR; the
  same cushion, coupon rule and 2031 mark. **f = 0.743**, chosen in the house world so both plans name the **same
  median bottom, $145,000**, then held fixed. Same paths, same seeds.

| MODEL (both bottoms after the 2031 mark) | House | Storms | Bootstrap | History |
|---|---|---|---|---|
| Named bottom, median (XR / A09) | $145k / $145k | $145k / $145k | $145k / $150k | $145k / $150k |
| **Bottom under $100k** | **0.69% / 7.5%** | **0.68% / 8.6%** | **0.30% / 5.4%** | **0 / 3.4%** |
| Bottom under $125k | 11% / 28% | 11% / 25% | 2.4% / 21% | 0.7% / 17% |
| Named bottom in the worst 5% of 2028-30 stock markets (median) | $140k / $90k | $135k / $80k | $145k / $85k | $145k / $95k |
| Correlation of the bottom with 2028-30 stocks | 0.08 / 0.95 | 0.13 / 0.94 | 0.08 / 0.97 | 0.07 / 0.99 |
| The mark cuts the bottom | 20% / 10% | 19% / 10% | 10% / 3% | 6% / 1% |
| Gift below the named bottom | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Gift p5 / p50 / p95, XR | $136k / $166k / $182k | $136k / $166k / $180k | $151k / $169k / $182k | $156k / $169k / $182k |
| Gift p5 / p50 / p95, A09 | $112k / $168k / $251k | $106k / $172k / $234k | $115k / $175k / $250k | $124k / $178k / $261k |
| **Gift + Laura's kept money in 2033, median** | **$182.4k / $191.9k** | **$182.8k / $195.5k** | **$185.6k / $198.5k** | **$186.5k / $202.5k** |
| Laura's money in 2042, mean | $44.8k / $53.5k | $43.0k / $51.3k | $41.8k / $51.4k | $48.3k / $60.6k |
| A cheque short by over $1k | 0.19% / 0.004% | 0.24% / 0.008% | 0.02% / 0 | 0 / 0 |
| Top reached | 84% / 93% | 84% / 93% | 93% / 98% | 97% / 99.6% |

**Read it like this.** On a typical naming day the two plans promise the same bottom. A09 has to name under $100,000
about **one time in thirteen** (house; 3-9% across the four worlds); XR about **one time in 150** (0-0.7%), roughly ten
times rarer. In the worst twentieth of 2028-30 markets XR names $135-145k and A09 $80-95k. A09's bottom tracks the
market almost one for one (0.94-0.99); XR's barely (0.07-0.13), and only through the mark: in a bad market Laura's own
half is smaller, so less of the coupon gap is covered before the bottom is touched. Before the mark, locking its whole
pot would still have left A09 about $125k in that slice (Felix's re-run, house). With the mark in, neither plan's gift
ever lands below its named bottom.

**The price, out loud.** A09 leaves Laura **about $9,000-$16,000 more** at the median in 2033 (gift plus what she
keeps; $9.4k in the house world), about $9,000-$12,000 more on average by 2042, and a far fatter top: its p95 gift is
about $250k against XR's $182k, because XR's gift can only ever own half of a small stock fund.

**Against us, honestly.** After 2033 XR comes up short somewhere across the ten cheques more often than A09 (0.19%
against 0.004% of house paths by over $1k; Felix: 0.4% at any size, median $680), because A09 leaves Laura more of her
own stock money for the coupon leak. The gift, cheque and top-reached rows use the Model Suite engine's gift rules,
which the mark doesn't change; L-13's chain puts XR's top-reached at about 97 in 100. **So the run supports one claim:
the bottom Laura can name on a bad day, and its price.**

## 3. V45 against every case line
The case is `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (line numbers); the IPS questions are
`keel/WHARTON_WORD.md` s2. Wharton says the IPS does not need "a final facility-contribution range" (WHARTON_WORD s2),
so the missing dollar range is not a gap. Verdicts: MET, THIN (answered, but a top team answers it better), MISSING.

| Case asks | Line | V45's answer | Verdict | What a judge with the case open would say |
|---|---|---|---|---|
| Ten fixed $50k payments, high certainty, portfolio only | :88-92 | "So we don't invest the promise. We buy it." + the ladder | MET | The strongest line in the draft. |
| Define high certainty, how evaluated, assumptions | :97-99 | "a list of ways to fail, not an adjective": default, a recession before the build, the coupon leak; "under one in sixty" | MET, one hole | The list is the definition and it's good. "Under one in sixty" has no owner yet (E1, open). |
| Operating reserve: size, first holdings, how it changes | :94-97 | "From 2033 the ten holdings are the operating reserve, and it runs itself down: each turns to cash before its cheque." | MET | LR-06's fix landed; it answers "as the payments approach and are made". |
| A responsible facility contribution, justified | :101-106 | floor + half her stocks; "the other half stays hers" | THIN | Why half? The only reason given is a dearer building. A judge asks once; the FR answers (M4: the kept half is a cushion, not insurance). |
| Flexibility, without committing everything | :102-103, :145 | "to sell any day" | MET | |
| 2031 range + confidence it falls inside | :117-118 | bottom owned, top = floor + half; "reaches its top about 97 times in 100" | THIN | The case asks the chance of landing INSIDE. V45 gives the chance of the top and leaves "inside" to be inferred from "owned". (E2, open.) |
| Favourable and unfavourable markets | :118-119, :148-149 | "every fall ... comes off the gift while every rise past the top goes to Laura", then the lock | MET | |
| The range protects the payments | :119-120 | "the cheques come first, then the floor, then the hope" | MET | |
| Assumptions: returns, timing, outside money, inflation | :146-148 | 7.5% world stocks; one rung before each January; the 2028 deposit's business income; Taiwan-dollar building | THIN | Inflation is touched only for the building. The cheques are fixed in dollars (:90), a fact V45 never uses. |
| Balance growth against protection; "thoughtful risks" | :68-74 | "Laura is willing to take thoughtful risks", the 60/40 paragraph | MET against the 60/40; **MISSING against A09** | Below. |

**The one real gap: V45 never meets A09.** Its only rival is the 60/40 ("about one time in three ... ours, under one in
sixty"). A09 has the same ladder, misses no more cheques, and two of six panel-4 judges put it first. The sentence that
carries XR's answer is there ("Most of the 2028 deposit buys Treasuries maturing late in 2032 ... her floor"), but it
says *what*, never *why 2028 and not 2031*. A judge with :68-74 open ("an appropriate balance between pursuing growth
and protecting the capital required for her goals") reads the floor as caution with no price. Section 2 is the why,
and its price. The other THIN rows are already in V45's Bible check (E2 confidence, X1 inflation); "why half" is new
and goes to the Final Report (M4: the kept half is a cushion, not insurance).

## 4. The three readings (SIMULATED, never quotes)
- **A co-sponsor's programme officer, 2031** (case :109-116). Reads both ranges on a good day and can't tell them
  apart: both bottoms are bought on the day she hears them. Reads them on a bad day and sees A09's lead shrink by a
  third in the same year her own board is cutting. Kill, sharpen or pass: **sharpen.** A09's $90k is not a broken
  promise (Kai: it names $90k and hands over $90k); it is a smaller signal at the worst time. The lead-gift study the
  team trusts (List and Lucking-Reiley, verified 27 Oct, LR-04) shows a bigger lead raises more, and says nothing about
  recessions or where "meaningful" starts (Amara's check, round 3).
- **A competition judge with the case open** (:68-74, :117-120, WHARTON_WORD s2). Asks "why not the plan I'd have
  written?" and finds no answer in V45; the 60/40 is a rival nobody on the panel ranked first. Wants the price of the
  floor in dollars beside what it buys, both from the same model. **Pass**, with Kai's one-world rule.
- **The practitioner: a municipal treasurer** (GFOA, Library A1: money for a building is invested so its "duration is
  no longer than the expected drawdown schedule"). Would ask why any of the gift sits in shares at all, and would see
  that XR's answer, only the floor's expected interest, is the honest gap (Library A2). **Pass for the Final Report**:
  it explains XR's line to a judge, not the IPS's job.

## 5. What the team could change
1. **The IPS (offered, the thread decides):** answer A09 by name. Paragraph in `../../ips_rewrite/inbox/2026-10-31_lauras-room.md`:
   it replaces V45's heading "Sell low, by appointment" and the two paragraphs under it, whole; V45 goes 496 -> 485
   strict. House-world numbers only: under $100,000 about one time in thirteen against one in 150; about $9,000 of
   her 2033 money at the median.
2. **The IPS (one word):** "set it aside from the hope" -> "from what she keeps" (+1): the model takes the coupon gap
   from Laura's half first.
3. **The Final Report:** the worst-5% slice ($135-145k vs $80-95k across four worlds), the correlations, A09 locking its
   whole pot (~$125k before the mark), the after-2033 hair (0.4% of house paths, median $680), the 60/40 and sequence-risk paragraphs
   if (1) is taken, the treasurer's question, and "why half" (M4).
4. **Left for the Lab:** the after-2033 shortfall and top-reached on L-13's chain with the 2031 mark, XR vs A09.
