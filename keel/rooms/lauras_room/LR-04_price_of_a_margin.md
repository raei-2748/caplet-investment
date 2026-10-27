# FICTION (the room, the simulated readers) + real research. LR-04: how a co-sponsor reads a range, and the price of a margin

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), Laura's Room, Tue 27 Oct 2026, 15:10 run
(Sydney). Not for submission. Simulated readers are tests built only from the case, never quotes. Work: WO-R7
(`../../ips_rewrite/WORK_ORDERS.md`) plus the Window's request of 27 Oct (`../../pm/REQUESTS.md`: rewrite LR-03 on
what the studies say, then price D1b). Numbers: `LR-04_price_of_a_margin.py` -> `LR-04_results.json` (MODEL).

**Read:** LR-03; the Window's N2 (`../../office/outbox/2026-10-27_window_7-5-and-three-checks.md`); R05 S1
(newsvendor) and S2 (wrong-way buffers); Keel's D1a/D1b call (`../../pm/ASK_HUMANS.md`); case :108-124.
**Star and criterion:** north star 3 (an aha) and 4 (applied investing knowledge); Client Knowledge and Investment
Strategy. **Line it could change:** the IPS sentence that says how the 2031 range is set and how sure we are.

## 1. The correction: LR-03 had the evidence backwards
LR-03 said donors respond to a committed lead "existing, not its size". The Window is right: that is false on LR-03's
own source. Raising seed money from 10% to 67% of the goal is a change of size, and it gave "a nearly sixfold increase
in contributions". What doesn't matter is the **ratio** of a match (1:1 vs 3:1, Karlan & List). So the corrected
finding is stronger, and it cuts the other way on D1b:
- **The bottom signals, and its size counts.** Every dollar shaved off the quoted bottom is a dollar off the signal.
- **The top is untested.** No study below looks at an uncommitted upper figure. It can't be called a signal or a
  waste on evidence; it can only be priced as a credibility risk, which is what the rule (floor + half the fund,
  capped) already does.

## 2. Would a co-sponsor read a range the newsvendor way? (WO-R7; every source opened 27 Oct 2026)
The newsvendor idea (R05 S1) says the bottom is what she owns and the top a rule-based stretch. Real practice agrees,
and for a sharper reason than taste: **the bottom is the only number a co-sponsor's own books can hold.**
- **Size of a committed lead moves giving.** List & Lucking-Reiley (2002, *JPE* 110(1): 215-233): seed of 10%, 33% and
  67% of the $3,000 needed for a real computer; 10% -> 67% gave "a nearly sixfold increase in contributions"; a refund
  promise added ~20% (econpapers.repec.org; author PDF, econweb.ucsd.edu). VERIFIED.
- **The form of leverage doesn't.** Karlan & List (2007, *AER* 97(5): 1774-1793): a match lifts revenue per letter 19%,
  but "larger match ratios (2:1 and 3:1) relative to smaller match ratios (1:1) have no additional impact" (J-PAL).
  Huck & Rasul (2011, *J. Public Econ.* 95(5-6): 351-362): matching "partially crowd[s] out" donors' own gifts; donor
  money is maximised "by simply announcing the presence of a lead gift" (IDEAS). Rondeau & List (2008, *Exp. Econ.*
  11(3): 253-267): "challenge gifts positively influence contributions in the field, but matching gifts do not"; and a
  lower announced target "significantly decreases contributions" (NBER w13728). VERIFIED (R&L did not vary gift size).
- **Why a lead works: it tells later givers the project is good.** Vesterlund (2003, *J. Public Econ.* 87(3-4)): an
  announcement "helps reveal the charity's quality" and cuts free-riding (author PDF). VERIFIED.
- **How co-sponsors' finance teams count it.** FASB ASU 2018-08 (ASC 958-605): a promise is conditional only if it
  has both "barriers that must be overcome" and a right of return or release; until then it is "a refundable advance";
  a letter stating "an intention to give" is not a promise, so no contribution is recognised (storage.fasb.org).
  CASE campaign counting takes "new documented pledges", and treats revocable expectancies separately (case.org FAQ;
  Mount Allison Policy 7230). VERIFIED. Kresge-style challenge grants are paid only if the rest is raised (Seton Hill,
  $1,095,280 by 1 Mar 2005). VERIFIED (one example).

**Verdict.** Yes for the bottom: a co-sponsor can write it down, and its size is what moves their money. The top
reads as an intention: no standard counts it and no study tests it, so it moves no money and can only cost credibility
if missed. That is the newsvendor reading exactly, so the plan should make the bottom as large as it can honestly be
and keep the top a rule. (Caveats: the field studies are households, not institutions; Laura is the founder, not a
donor to someone else's charity, so the accounting is how her co-sponsors will *read* her figure, not a rule she is
under.)

## 3. The price of a margin (Window's request; MODEL, 22 Oct curve, 7.5% world stocks, 200,000 paths)
D1b (Keel's call, 26 Oct) knocks a fixed margin off the 2031 bottom. A clearing house would call that **initial
margin**: posted up front, in every path, sized for a tail. Clearing houses also take **variation margin**: only the
loss already visible, marked to market. The plan can do the same: in 2031, re-price the ladder's coupon reinvestment
at 2031 yields and cut the bottom only by the gap already visible that the 2027 leftover and Laura's half of the stock
fund can't cover. (The bottom's existing rounding, $3.7k-$8.7k below the floor, is already a small initial margin for
the two unknown years 2031-33.)

| Margin under the quoted bottom | Bottom breaks (2033 gift below it) | Median miss when it breaks | Average cut to the bottom | Paths where the bottom is cut | Co-sponsor money lost, if size works as in the seed study* |
|---|---|---|---|---|---|
| none | 0.75% (1,498 paths) | $4.0k | $0 | 0% | 0 |
| fixed $5,000 | 0.31% | $3.4k | $5,000 | 100% | 3.4% (1.8%) |
| fixed $10,000 | 0.11% | $2.5k | $10,000 | 100% | 6.8% (3.7%) |
| fixed $20,000 | 0.004% | $1.8k | $20,000 | 100% | 13.7% (7.5%) |
| **marked to market in 2031** | **0 of 200,000** | - | **$809** | **8%** | **0.6% (0.3%)** |
| marked to market, no rounding up | 0 of 200,000 | - | $584 | 8% | 0.4% (0.2%) |
| half the visible gap only | 0.04% | $1.3k | $533 | 8% | 0.4% (0.2%) |

\* Co-sponsor money lost = 1 - (quoted / unpadded bottom)^E, averaged over paths. E = 0.94 is read off List &
Lucking-Reiley (seed x6.7 gave giving x~6); E = 0.5 in brackets as a gentler case. Both are heroic extrapolations from
a mail campaign to institutional co-sponsors: the ranking is the point, not the decimals.

**Break-even.** A fixed $5k margin (0.75% -> 0.31% breaks) pays only if a broken bottom costs Laura more than about
**8 times all co-sponsor money** (4 times at E = 0.5); $10k needs about 11 times (6). Marking to market pays if a broken
bottom costs more than about **0.8 times** co-sponsor money, which the case all but says it does ("lose the confidence
or participation of co-sponsors", :114-115). Why it works: the gap visible in 2031 and the gap known in 2033 move
together (correlation 0.95 in the model), so two years out the bond market has already told Laura most of what
can hurt the bottom.

**Caveat that decides it.** Stocks and rates are independent in this model. The bad case (R05 S2) is yields falling
for good in a recession, when Laura's half is smallest. The Genius Lab's WO-R5 joint run must re-run this table before
"0 of 200,000" goes anywhere near a draft (request filed).

**Newsvendor check (WO-R7, for R05 S1).** Under the rule, the gift reaches the exact top in 69.9% of paths (76.7%
within $1k). The implied over/under-promise cost ratio is 0.699 / 0.301 = **2.3**, inside R05's 1.9-2.7.

## 4. The finding (for Thursday's synthesis)
**Don't pad the bottom today; mark it to market in 2031.** A fixed margin taxes the signal in every path to guard
against a gap that, by 2031, is mostly visible. Marking to market cuts the bottom only in the ~8% of paths where the
bond market has already shown a gap, by about $800 on average, and in this model never breaks. It answers the case's
two costs (:110-115) the way the newsvendor would: the bottom as big as the evidence allows, never broken; the top a
rule reached about seven years in ten. Knowledge underneath (uncited in the IPS, cited in the Final Report):
initial vs variation margin (central clearing), seed money and lead gifts, conditional pledges in nonprofit
accounting, newsvendor quantiles.

## 5. Visit (SIMULATED; built only from the case)
| Who | Reaction (SIMULATED) | Case line | What the team could change |
|---|---|---|---|
| Co-sponsor, foundation programme officer | Reads the bottom as the number she can write in a board paper and the top as "nice if it happens". Hears "fixed $10k below what she owns" as Laura hedging her own project. | :110-112 | Quote the owned floor, cut only by what 2031 already shows |
| Same | "If the bottom moves in 2031, will it move again in 2033?" | :113-115 | Say once: the 2031 figure already nets the visible gap; after that only stocks move, and only the top |
| Co-sponsor, corporate sponsor's finance lead | Wants one sentence on what makes the top move. "Half a stock fund" is clear; a percentage chance of the top is more useful than "99% inside". | :117-119 | Confidence = the chance of reaching the top (~70%), the bottom stated as owned |
| Laura (simulated) | Comfortable: nothing of hers is pledged beyond the floor; her half still covers gaps first. | :101-103 | none |

## 6. Candidate line (AI DRAFT (Claude, 27 Oct 2026); for the rewrite to weigh, Caplet rewrites)
- "In 2031 Laura names a bottom she already owns, less any gap the bond market has already shown her, and a top
  that is the floor plus half her stock fund. The bottom isn't a forecast; the top is reached about seven years in ten."
