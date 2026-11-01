# FICTION (the room) + real work (the test). L-15: hold it, then say it

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Genius Lab, Sun 1 Nov
2026, 13:40 Sydney, round 5 beat 5 (Q13, the voice round: who asks a sceptic to pay for a promise, in under a hundred
words, and gets believed?). Nora builds; Kai roasts; Jun and Kai judge. Huddle H-010
(`../../huddles/2026-11-01_hold-it-then-say-it/transcript.md`). Script `L-15_hold_it_then_say_it/run.py`; results
`L-15_hold_it_then_say_it/results.json`; results page for the huddle `../../huddles/2026-11-01_hold-it-then-say-it/research/lab_results.md`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 (intra-year bridge draws 20261101) | rho 0.5 unless S0 | V47's design = the L-13 slide + lock, via L-14's
chain and Archive A26's k = 0.76 match | MODEL.** Controls: same-day top reached = L-14's XR row (97.90 / 97.60 /
96.02%, asserted); A26's mean lead reproduced ($14,917 S0, $15,399 S1); the year-late arm uses L-12's delayed-lock rule
exactly (an identity, asserted).

**For a judge, in plain words.** Our draft says the half of Laura's stocks she promises co-sponsors moves into
Treasuries "on the day she names" her range. We tested what happens if that move comes late. A week or a month barely
matters: in our model the gift still reaches its top about 97 times in 100. What matters is skipping it after a
boom year, when skipping feels clever: then the top is reached only about 86 times in 100 in those futures. So we
swap the order. She moves the money first and names the range after. Then there is nothing to skip: a top she hasn't
moved is a top she can't say. Every number in the draft stays the same, and the sentence gets a word shorter.

**Why this, today.** Today's question (Q13) and the Library's request (H-009, filed to the Lab): the clause "even in a
week when stocks are rising" promises a step someone takes on a day Laura picks (Felix), and "who holds the watch?"
(Kai). The case: Laura "plans to begin approaching potential co-sponsors in 2031" (Client Profile, line 109): a season
of meetings, not one day. North stars 3 and 4; Client Knowledge (credibility with co-sponsors, :114-115), Investment
Strategy (a rule that holds "as the client's needs change"), Portfolio Analysis. IPS line that could change: V47 P7,
"On the day she names it, the half she promised moves into Treasuries".

## Pairings tried
- **A1, the turnaround x Q13** (find x question): a limit is believed when it is fixed before anyone can see the top.
- **A1 x stepping stone S16** (find x stone): UNC won't sign a building contract until the money is cash; Laura doesn't
  name a bottom until she owns it. Why stop at the bottom? (-> A)
- **A1 x the binned delayed lock** (find x binned idea; L-12 BIN, stone S13): re-tested on V47's design, by the week,
  month, quarter, half-year and year, and as the temptation itself ("wait while it rises"; "skip after a boom"). (-> A's test)
- **K3, the location test x V47 P8** (find x champion): "$15,000 more on average": average over which futures? (-> B)
- **A2, the published test x K1, the flaw with an address** (find x find): give the doubter the miss in their own
  units, with its size. (-> C)

## Challengers, with the novelty check
(`../../IDEAS.md`, this book, the Library's slips, R02, R05, `../../loop/FRONTIER.md` s3, the binned list, the bank)

| # | Challenger | Novelty | Builder |
|---|---|---|---|
| A | **Hold it, then say it:** the promised half moves into Treasuries *before* she names the range | **Return** of H-009's order-test seed (Felix) and of the North Star memo's "commit only money she already owns" (16 Oct; FRB-93; stone S16, which stops at the bottom). New here: the top too, the lag curve, and the skip | Nora |
| B | **The price's address:** where the rival's $15,000 average lead is earned | **Return** of bank #107 (the location test, a wording check) and H-005 (Jun: "the mean gap is carried by the best 5%"). New: the number, by fifths | Nora |
| C | **The miss, sized, and the range's own confidence** | **Return** of #88 (bottom never broken; residual misses about $1k). New: the tail of the misses and "inside the range" as the case's own question (:117-118) | Nora |
| D | **The cash offer** (home sellers take less from a buyer paying cash, because cash can't fall through) | **Not built.** Same job as #104 (agreed-value cover, Kitchen, 31 Oct): a second picture for the price of certainty beside the capsule (Commandment VII); the size of the cash discount UNVERIFIED (not fetched) | Nora |

## Kai's roast (before the run; `../../huddles/2026-11-01_hold-it-then-say-it/posts/r1_kai.md`)
"Is the order a real difference or a word swap? V47 already moves the half on the day she names the range ... If it
costs under a point, A is V47 with the clauses swapped. Bold. Brave. Cosmetic." On C: "Is a $1,500 miss a selling
point or a hedge? ... Ask for the tail." Bet: "A dies. A month's slip costs our model under 1 point of the 97 in 100."
Sealed guesses (Kai / Nora / Jun): a month late 97.5 / 95.4 / 97.4%; the best fifth's share 82 / 95 / 76%; S6 median
miss $1,900 / $2,800 / $1,062.

## Test (three worlds, 200,000 paths each, MODEL)
Inside 2031 stocks move as a Brownian bridge on the model's own 2031 draw, so the yearly paths are untouched; the
fat-tailed month swaps the bridge's normal draw for a Student t (3 df, same variance). A "slip" names the range on 1 Jan
2031 and moves the promised half later; the money earns the model's short rates after it moves.

**A. Order and lock timing: top reached, % (S0 / S1 / S6)**
| Arm | S0 | S1 | S6 |
|---|---|---|---|
| Same day (V47) | 97.9 | 97.6 | 96.0 |
| Move a week late | 97.7 | 97.4 | 95.9 |
| Move a month late (fat-tailed month) | 97.1 (97.3) | 96.9 (96.9) | 95.6 (95.7) |
| Move a quarter late | 95.6 | 95.3 | 94.7 |
| Move six months late | 93.6 | 93.0 | 93.7 |
| Move a year late (L-12's rule; on V29's design it gave 73.6) | 90.9 | 89.8 | 92.1 |
| Wait while it rises (move after the first down week; median 2 weeks) | 97.6 | 97.4 | 95.9 |
| Skip after a top-fifth 2030 (2030 averaged +36.5%), inside those paths, v moving | **85.8 v 98.5** | **85.1 v 98.6** | **89.2 v 96.4** |
| Skip everywhere (no lock) | 87.9 | 86.9 | 91.0 |
| **Move first, name a month / a quarter / six months later** | **97.9** | **97.6** | **96.0** |
Move-first is identical path for path, by construction: the top is read off what already sits in Treasuries. Cheques
short by more than $1,000 stay 0.03 / 0.03 / 0.05% in every arm. The quoted bottom: 0 / 0 / 1 path of 200,000 below
it on the same day (S6's one path); under 1 in 20,000 in every arm. A slip barely moves the average gift (-$8 for a
month, -$29 for a quarter, S0) and hands Laura the rises (+$80 / +$262 by 2042): a free option the co-sponsors pay for
in misses, as L-12 found.
**Read it under move-first:** if she skips the move, nothing new sits in Treasuries, so the top she can say is the
floor. A skip shrinks the range before it is spoken instead of breaking it after (Jun, Kai and Nora, round 2).

**B. Where the rival's lead sits** (A09 matched to our $145,000 median bottom; lead = gift + Laura's 2042 money;
fifths of 2028-30 stock markets, the sort Jun fixed before the run)
| Fifth | 1 (worst) | 2 | 3 | 4 | 5 (best) |
|---|---|---|---|---|---|
| S0 mean lead | -$27,896 | -$5,352 | +$11,069 | +$29,929 | +$66,837 |
| S0 rival ahead | 1.2% | 26% | 86% | 99% | 99.8% |
Outside the best fifth the rival's lead averages under $2,000 (S0 $1,938, S1 $1,892). S1 matches S0 within $3,000 a
cell. **S6 differs:** mean lead $27,114, fifth 2 turns +$1,737, the best fifth carries about two-thirds. Sorted by
2028-32 instead, the best fifth carries 77.8 / 77.5 / 60.9%. When 2028-32 stocks beat the 2028 five-year Treasury yield
(62% of paths) the rival is ahead 86% of the time, by +$32,000 on average; when they don't, it is behind by about
$13,700 (same sign in 82% of paths).

**C. The miss, sized (V47, same day)**
| | S0 | S1 | S6 |
|---|---|---|---|
| Top missed | 2.1% | 2.4% | 4.0% |
| Miss when missed: median / p90 / p99 / largest | $865 / $3,057 / $5,320 / $8,312 | $948 / $3,095 / $5,348 / $8,331 | $1,062 / $3,189 / $5,572 / $9,768 |
| Misses under $5,000 | 98.4% | 98.7% | 98.2% |
| Inside the quoted range | 200,000 / 200,000 | 200,000 / 200,000 | 199,999 / 200,000 |

## Result against the hypotheses
- **A: false as written.** A month costs 0.8 / 0.75 / 0.4 points, not 3: Kai wins his bet. True in a form nobody wrote
  down before the run: the order matters for the skip, not the lag, and moving first removes the skip at no cost.
- **B: holds in S0 and S1** (best fifth 77.8% on the 2028-32 sort, 89.6% on 2028-30; our plan ahead on average in the
  worst two-fifths), **fails in S6.**
- **C: holds in all three worlds** (median miss under $1,500, 98% of misses under $5,000).
- **numbers-auditor (the chair, by hand):** a month moves the promised half (about $15,000-17,000; the median top is
  $165,000 on a $150,000 floor) by about 4.6% in one standard deviation, about $770. The money above the quoted top is
  about two years of bill interest on that half (roughly $1,200) plus the round-down to $5,000 (0-$5,000). A $770 swing
  clears that slack in well under 1 path in 100 on its own; 0.8 points, with the ~2% already near the line re-sorted,
  is the right size. A quarter (about $1,200) gives about 1.5 points by the same sum, against 2.3 modelled.

## Verdicts (the builder doesn't judge; Jun and Kai, round 3)
- **A, hold it, then say it: ADOPT 2-0** for V47 P7, as a word swap: "Before she names it, the half she'll promise
  moves into Treasuries" (P7 50 strict v 52, IPS 495). No number moves; a skip can't hide. Kai lost the argument he
  won the bet on: "I bet on the wrong failure." Kai's check: P6's "In 2031" is now load-bearing (cut it and a judge can
  read the move as 2030, and the locked VT note, "a rise before 2031 lifts the top of the range co-sponsors hear",
  stops being true); no locked line or case line breaks.
- **B, the price's address: PARK 2-0 (Final Report).** True in two worlds of three (S6 spreads the lead: about $11,000
  outside the best fifth); a sort of paths is "detailed portfolio projections", which Wharton's updated IPS
  instructions send to the Final Report (lines 69-71); P8's worst twentieth already gives the cost an address. Jun: "I
  was wrong to print it."
- **C, the miss sized and the range's confidence: PARK 2-0 (Final Report).** The same instructions keep "a final
  facility-contribution range" out of the IPS, and C is that range's confidence statement; in the IPS "inside" is the
  design talking (she owns the bottom, the cap stops the top) and 600,000 is one seed in three worlds. V47's "97 in
  100" stays: it says how often one rule holds (Jun). For the Final Report: inside the range in 200,000 of 200,000
  paths (S0, S1) and 199,999 (S6); misses median $865-1,062, 98% under $5,000, largest $9,768.
- **Bank #106's clause, "even in a week when stocks are rising": BIN for the IPS 2-0.** Its hard case costs 0.2
  points (a week) or 0.3 (waiting while it rises), and under A no promised half sits through a rising week. Kai: "a
  lock on an empty tin." The Final Report keeps the lag table as the reason the order is what it is.
- **D, the cash offer:** not built (novelty check).

## What it changes
- **IPS (to the rewrite thread, `../../ips_rewrite/inbox/2026-11-01_genius-lab.md`):** P7's second sentence, -2 words.
  The Library's P7 rewrite (Amara's, 55 strict) is superseded on its new clause; its "that same day" order is the one
  A reverses.
- **Final Report:** the lag and skip table (why the money moves first), B's address (Nora's text in the inbox), C's
  confidence line and the miss tail.
- **The Library's request** (H-009's two tests) is closed: no V47 number changes when the half moves first; the lag
  costs 0.1-2.3 points from a week to a quarter; the skip after a boom costs 12.6-13.5 points inside those paths (S0,
  S1), 7.2 (S6).
