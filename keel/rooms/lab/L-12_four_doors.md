# FICTION (the room) + real work (the test). L-12: four doors (V29's framework under every change we can name)

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Genius Lab, Thu 29 Oct
2026, 13:40 Sydney, round 2 beat 5. Scripts `L-12_four_doors/run.py` (nine stresses + the delayed lock) and
`L-12_four_doors/run_requests.py` (open requests + the 2028 deposit sweep); results beside them.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | V29's design = Long Room LR8 "MB+T +lock" (LR8 -> LR-05 -> L-11 -> L-10 -> `ips_numbers.py`, unchanged) |
MODEL.** Reproduction: S0, S1, S6 match LR8's committed rows to the digit (short 0.03/0.03/0.05%; top 84.6/82.9/41.5%).

**For a judge, in plain words.** We tried to break V29's rules nine ways: a smaller 2028 deposit, no deposit, yields
falling before the bonds are bought or after, stocks halving before or after the range is named. In every case where
some 2028 money arrives, even half of it, no cheque comes up more than $1,000 short in more than 1 path in 2,000, and
no quoted bottom is ever broken. Every change lands on the gift first, at a date the case already set. The one change
the rules can't answer is a 2028 deposit below about $50,000: then the cheques are bought but not insured.

**Why this, today.** Q8 (the framework). Book 7 asks for "the strategy and decision-making framework" and "how your
strategy will guide portfolio construction and investment decisions as the client's needs change". C13's holder is
one line plus rules scattered across V29. North stars 3 and 4; Investment Strategy (IS-a, IS-c), Portfolio Analysis.
IPS line that could change: V29 para 10 ("If needs change, cheques first; floor and stocks are bought smaller together").

## Pairings tried
- **N1/N2 x the case's dates (where the ward breaks):** a ward needs alarms because a patient's crash has no date.
  Every flow in Laura's case has one: Jan 2027, Jan 2028, Jan 2031, Jan 2033. So the plan's rules can fire on dates,
  not readings. That is challenger C.
- **W-02 x V29's 2031 mark:** Basel's "step the payout down as the cushion thins" is already what the 2031 mark does
  (bottom = floor owned minus any gap spare money can't cover). Same rule, better name (the Window's request, below).
- **N2 x J1 x the 2031 lock:** the one exception anyone would actually ask for is "wait a year for a recovery before
  locking". Tested below: it is a free option Laura would write against her co-sponsors.
- **N1 x the ladder:** "a healthy total never excuses one failing part" (bank #71). Tested below: 7 paths in 200,000.
- **A1 (Chile's order of payment) x L-10 / bank #49:** a return. V29 already ranks the claims; not re-tested.

## Challengers, with the novelty check
(`../../IDEAS.md`, this book, the Library's slips, R02, R05, `../../loop/FRONTIER.md`, the binned list, the bank)

| # | Challenger | Novelty | Builder |
|---|---|---|---|
| A | **The buffer table with a per-rung alarm** (W-02 + N1 + N3): read every January at market prices, step the hope down as spare money thins, never argue a recovery, one short rung calls the top-up | Bank #69 and #71, today; the yearly check was binned as a cure in L-11 B | Jun |
| B | **The signed exception** (N2 + J1 + J2): one hope-side step may wait once, in writing, for at most a year; cheques never wait; silence means the default | Bank #70, today; no draft has an override | Jun |
| C | **Four doors, one rule** (new): four Januaries the case already dates; each has one job written today; between doors nothing is sold; a door opens on its date whoever argues; every change lands on hope before a cheque | New. Nearest: I-11 two buckets (adopted, a picture not a rule); bank #49 order of call (a ranking, no dates) | Jun |
| D | **Chile's order of payment** (A1) | **Return** of bank #49 and L-10 | not built |

## Kai's roast (before the run)
"Four doors is a calendar with a nice name. A judge asks 'what if it goes wrong in 2029?' and you say 'wait till 2031'.
And I'll bet you two things. One: a two-point rate fall makes the gift your crumple zone, so 'cheques first' just means
the facility hears a smaller number every time. Two: your rule says money she *has* buys certainty, but take away the
2028 deposit and I bet the cheques fall over, because the coupon gap is paid with money she *expects*."

## Test 1: V29 under nine "as needs change" stresses (rho 0.5 unless S0; MODEL)
| Stress | Door it lands on | **cheque short >$1k** | quoted bottom p5 / p50 | below quoted bottom | top reached (within $1k) | gift p5 / p50 |
|---|---|---|---|---|---|---|
| S0 base, independent | — | **0.03%** | $115k / $145k | 0 | 84.6% | $133k / $166k |
| S1 base, fall together | — | **0.03%** | $110k / $145k | 0 | 82.9% | $132k / $166k |
| S2 2028 deposit halved | 2028: gap first, floor and stocks smaller | **0.05%** | $30k / $65k | 0 | 69.5% | $45k / $82k |
| S3 2028 deposit missing | 2028 never opens | **57%** | no range | — | — | $0 |
| S4 yields 1pt lower before the build | 2027 buys what it can; 2028 fills the gap | **0.01%** | $75k / $110k | 0 | 66.6% | $91k / $130k |
| S5 S4 + no 2028 deposit | 2028 never opens | **98%** | no range | — | — | $0 |
| S6 yields 2pt lower after the build, for good | 2031 settles the gap before the range | **0.05%** | $95k / $130k | 0 | 41.5% | $107k / $150k |
| S7 stocks halve before naming | 2031 names a smaller range | **0.05%** | $105k / $140k | 0 | 70.2% | $122k / $157k |
| S8 stocks halve after naming | already locked; Laura's half takes it | **0.03%** | $110k / $145k | 0 | 81.9% | $132k / $166k |

**The corner (2028 deposit, rho 0.5; Writing Room 3b and Q9):** cheque short >$1k with a deposit of $0 / $5k / $10k /
$20k / $30k / $50k / $75k / $150k = **57% / 46% / 34% / 16% / 6.2% / 0.45% / 0.05% / 0.03%**. With yields 1pt lower
before the Jan 2027 build: 98% / 96% / 92% / 79% / 59% / 19% / 1.3% / 0.01%. When the deposit is missing the median
miss is about $16.6k across the ten cheques (L-10 S3, same mechanics).

## Test 2: the exception anyone would ask for (delay the 2031 lock one year)
| | top reached: lock on naming day -> delayed | mean gift change | mean extra kept by Laura above the top |
|---|---|---|---|
| S0 | 84.6% -> 73.6% | -$270 | +$1,357 |
| S1 | 82.9% -> 71.6% | -$304 | +$1,333 |
| S6 | 41.5% -> 38.2% | +$170 | +$1,052 |
| S7 (stocks already halved: the tempting case) | 70.2% -> 65.1% | -$53 | +$626 |
| S8 (stocks halve inside the delay year) | 81.9% -> **0.2%** | **-$8,496** | -$2,036 |
In S0, among paths where the stocks sit below their 2028 cost on naming day (23%), waiting cuts the gift by >$1k in
12.7% and lifts it in 8.9%. The capped range means the co-sponsors keep every fall and Laura keeps every rise above the
top. Caveat (Kai): the model has no mean reversion, but the asymmetry is the cap's, not the model's.

## Test 3: the open requests on V29's design (S0 / S1 / S6)
- **Ninety (Kitchen):** quoted bottom p0.1 / p1 / p5 / p50 = $85k / $100k / $115k / $145k (S1 $80k / $100k / $110k /
  $145k; S6 $70k / $80k / $95k / $130k); lowest in 200,000 paths $65k / $60k / $50k. **No ninety:** the figure true in
  999 of 1,000 sits $60-65k below the median. But no path ever pays less than the bottom once quoted (0 of 600,000).
  The rule's promise is that a quoted bottom is never broken, not that it has a floor. The court's ruling stands.
- **The top (Courtroom, Long Room), with the lock:** exact 79.2 / 77.5 / 37.8%; within $1k 84.6 / 82.9 / 41.5%; top
  quoted rounded down to $1k 82.5 / 80.7 / 40.0%; to $5k **86.6 / 84.8 / 44.0%**. Recommend: quote the top rounded
  down to $5k, like the bottom, and define "reaching the top" as the gift at least equal to the quoted top: **about
  six times in seven** (S0/S1), 44% if yields fall two points for good. When missed, the median miss is $8.1-8.7k
  ($17.4k in S6). The shared `ips_numbers.py` itself is not patched; the LR8 chain is the V29 model and every room
  should quote from it.
- **One failing rung (Library, bank #71):** ladder funded in total but one rung short by >$1k in **7 of 200,000** paths
  (S0, S1; 0 in S6); largest single-rung gap $1,073, always the 2042 cheque; a pooled coupon account carries all 7 in
  time. With one rate path, rungs fail together. The last cheque is the canary, and the total already reads it.
- **Two-step table (Window):** same rule, better name. Before naming day nothing is traded, so trimming an unspoken
  gift moves no number; the 2031 mark already quotes the bottom net of any gap spare money can't cover. Basel goes to
  the Final Report as the explanation of the mark; "never argue a recovery" earns a place because Test 2 is that argument, priced.

## Result
**Hypothesis (C): V29's rules keep the cheques whole under every needs-change stress where money arrives as the case
says, and every stress lands on hope at a dated door. TRUE for seven of nine stresses (0.01-0.05%), with no quoted
bottom broken. Kai won one bet and lost one.** Lost: the gift is the crumple zone, but it crumples *before* it is
spoken (S6 bottom $130k, top 41%), never after. Won: without the 2028 deposit the cheques fall over (57%), so the
2027 cheques are bought with money she has but insured with money she expects. The first $50k of the 2028 deposit
($75k if yields fall a point before the build) is cheque money; the rest is hope.

## Verdicts (Kai and Nora; Jun built them all, so he doesn't judge)
- **C, four doors: ADOPT as challenger to C13** for tonight's Courtroom, amended by Kai: door 2's first job is the
  cheques' insurance. Claim set for the Writing Room: "Every decision waits for a January the case already set, and
  each January's job is written today: 2027 buys the cheques; 2028 insures them, then buys the floor and the stocks;
  2031 settles what the yields say, names the range from what she owns, and locks it; 2033 tops up the reserve once.
  Between Januaries nothing is sold. A change lands on the gift before it is named, never after, and never on a cheque."
- **A, buffer table: PARK (Final Report).** Same rule as the 2031 mark; the per-rung alarm fires in 7 paths of 200,000.
- **B, signed exception: BIN for anything named.** A delay is a free option against the co-sponsors (S8: top 0.2%).
  Keep its last clause as door C's: a door opens on its date, and silence means the default happens.
- **D: return**, folded into C ("hope before a cheque").

## Honest weaknesses
Rho 0.5 rate-stock link and parallel rate shifts; no mean reversion; one bill rate for the locked half; the stresses are
one-at-a-time. "Between Januaries nothing is sold" is true of the plan's decisions, not of Laura's own half, which is
hers any day. The 2028 threshold (~$50k) is a MODEL number on one curve: the IPS gets the principle, the FR the table.
