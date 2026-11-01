# FICTION (the room and the simulated people) + the real case. LR-09: the promise has no number

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), Sun 1 Nov 2026, Laura's Room, round 5
beat 6 (Amara; Kai and Felix in the huddle). Not for submission. Simulated co-sponsors, judges and Laura are tests,
never quotes; no Laura quotes. Huddle H-011: `../../huddles/2026-11-01_already-in-the-bank/` (3 rounds, 9 agent turns).
Run: `LR-09_the_promise_has_no_number.py` (adds three outputs to the Genius Lab's L-15 chain, nothing else), numbers
`LR-09_results.json`. **STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA world stocks 7.5% |
200,000 paths per world, seed 20261016 | V47's design (L-13 slide + lock, L-14, A26) | MODEL.** S0 = rates and stocks
independent; S1 = linked (rho 0.5); S6 = yields fall 2 points just after the build, for good.

**For a judge, in plain words.** Our draft gives Laura's hope a number (the gift reaches its top about 97 times in
100) and her promise none, though the case asks us to say how we tested the "high degree of certainty" the ten cheques
need. So we measured it. In our model all ten cheques are paid in full in about 998 futures in 1,000, whether or not
the 2031 step is ever taken; the rare gap is a few hundred dollars across $500,000. The one place it gets thin is the
recession the draft itself lists (yields lower before the January 2027 purchase and the 2028 deposit halved): about 98
in 100. The newest draft (V49) also bent one sentence so that the "catch" in Laura's range no longer makes sense, and we
offer the repair.

## 1. Why this, today
Beat 6 reads the Genius Lab's challengers (L-15, 13:40) three ways, then checks the newest draft against every case
line. It also continues H-010's seed to this room: "Does a co-sponsor value a range that is already in Treasuries more
than the same range promised?" The newest draft is **V49** (`../../ips_rewrite/drafts/D29/`, rewrite thread, branch
`claude/project-thread-3ahu9r`, not yet on the day branch; 493 strict); the round's champion is V47 (D27). Not a
repeat of LR-06 to LR-08 (the range's bottom, the price of the floor, the rival's bad naming day): today's ground is the
promise's own certainty and the co-sponsors' own field (fundraisers). North stars 3 and 4; Client Knowledge (:91,
:97-98), Investment Strategy, Portfolio Analysis. IPS lines that change: V49 P4 (one clause) and P7 (two sentences).

## 2. The Lab's four challengers, read three ways
| | Co-sponsor (SIMULATED programme officer, 2031; Amara) | Judge with the case open (SIMULATED; Kai) | Practitioner (Felix, in their own published words) | Verdict |
|---|---|---|---|---|
| **A, hold it, then say it** (the promised half moves into Treasuries before she names the range) | PASS: "begin approaching" (:109) is a season of meetings, not one day; move-first makes whatever she says first already true; an owned top books as a gift, not a forecast (:114-115) | SHARPEN: the model can't tell "before" from "on the day" (identical path for path), so its value is a precommitment rule (Wharton: a strategy "should not be rewritten simply because markets move"). Tie the trigger to the case: **before any co-sponsor hears a number** | **Fundraisers: EXACT on order and reason.** Penn's campaign: "Officials will not release a specific financial goal until then", once "40 to 60 percent" is in; a consultant: "No one wants to participate unless it looks like it will be a success" (The Daily Pennsylvanian, 15 Feb 2007). CCS Fundraising: "The public phase should begin when you've raised 60%, 80%, perhaps even 100% of your fundraising goal" (23 Jan 2020). Breaks first: a campaign banks other people's pledges and still has a goal to raise; Laura banks her own money, so A sits at the field's cautious edge (100%). The guide (Hall's turnaround): PASS, but Hall gives up the summit and A banks it | **SHARPEN, adopted with Kai's trigger** (see section 5) |
| **B, the price's address** (the rival's $15,000 is earned in the best fifth of 2028-30 markets) | KILL here: a co-sponsor never sees the rival | KILL for the IPS: projections are Final Report work; fails in S6 | (not a practitioner question) | **KILL for the IPS** (the Lab's FR park stands) |
| **C, the miss sized + "inside the range"** | SHARPEN: quote the worst miss, not the median ($8,312 S0; $9,768 S6): funders trust the worst case. Final Report co-sponsor text | SHARPEN: "inside, 200,000 of 200,000" is built in (owned bottom, capped top), not confidence; the miss is the real number | (not a practitioner question) | **FR, with the largest miss beside the median** |
| **D, the cash offer** | KILL: funders don't discount for certainty; the case says a real gift makes them "more willing" (:110-112) | KILL: no case line; size UNVERIFIED; P5's note already pictures certainty | KILL: Laura is the cash buyer with no seller to discount her. If a cash offer carries proof of funds, that is A's order (UNVERIFIED) | **KILL 3-0** |

Sources fetched 1 Nov 2026 with WebFetch (the words came back in the fetched text; curl to both hosts was refused by
the proxy): https://www.thedp.com/article/2007/02/in_quest_for_funds_silence_is_golden (Heather Schwedel) and
https://www.ccsfundraising.com/insights/maximizing-the-value-of-a-campaigns-quiet-phase/ (Nicole Stratton). Whether
campaigns count pledges as "raised": UNVERIFIED.

## 3. The promise has no number (the run)
Every draft from D15 to D29 prints one probability, the gift's 97 in 100. The cheques, which the case asks to be
funded "with a high degree of certainty" (:91) and whose certainty teams must define, "explain how they evaluated" and
back with assumptions (:97-99), get a list of ways to fail and no test of the list. A SIMULATED Laura, reading V49,
could take the 97 for her cheques (Amara). The Lab's L-15 already counted cheques short by over $1,000 (0.03%); the
case's cheque is "a fixed $50,000" (:90), so a $359 gap still bounces (Kai), and the honest count is **any** shortfall.

| World (MODEL, V47's design) | All ten cheques paid in full | Short at any size | Short by over $1,000 | Median gap when short | Gift, mean | Top reached |
|---|---|---|---|---|---|---|
| S0 independent | 99.82% | 1 in 551 | 0.03% | $359 | $159,957 | 97.9% |
| S1 linked (rho 0.5) | 99.81% | 1 in 538 | 0.03% | $362 | $159,624 | 97.6% |
| S2 2028 deposit halved ($75,000), linked | 99.74% | 1 in 381 | 0.05% | $408 | $71,946 | 96.7% |
| S4 yields 1 point lower before the 2027 build, linked | 99.95% | 1 in 1,905 | 0.01% | $313 | $125,711 | 96.7% |
| S6 yields fall 2 points just after the build, for good, linked | 99.68% | 1 in 311 | 0.05% | $364 | $141,771 | 96.0% |
| **S9 P4's recession: S4 and S2 together, linked** | **98.49%** | **1 in 66** | **1.27%** | **$5,032** | **$37,464** | 95.9% |

- **Identical with or without the 2031 lock in five worlds of six; in S9 almost** (1.511% short with it, 1.503% without;
  `CORD:` Kai and Amara, round 3, caught the chair's "every world"). The cheques barely depend on a step anyone takes in
  2031; the lock guards Laura's name with co-sponsors, not her cheques.
- **"Short" is a whole-portfolio test** (Felix and Kai, from `at_2033` in L-11, reused by L-15): a cheque counts short
  only after her kept half and then the gift have gone to it. So the table is V49's last line tested: "the cheques,
  then the floor, then the hope". In S9 the gift's mean falls to $37,464; the cheques fall to 98.5 in 100.
- **What the model can't price:** the US government defaulting (V49's first failure) and a deposit that never comes
  (the Lab's S3/S5 break L-15's fifths sort, so they weren't run).
- **The chair's own CORDs (round 2):** the first brief called S6 "fat-tailed" (it is the rates stress), and offered
  "3 in 10,000" without saying it counted only gaps over $1,000. Both fixed before round 2.

## 4. V49 against every case line (the room's job; Kai's table checked by the chair)
| Case asks (line) | Where V49 answers it | Verdict | What would fix it |
|---|---|---|---|
| A balance of growth and protecting the capital her goals need; she has taken thoughtful risks (:68-74) | P1 (a promise and a hope), P5 (floor, its interest in stocks), P9 ("Laura takes thoughtful risks; the strongest alternative takes one for her") | MET | none |
| Ten fixed $50,000 payments 2033-2042, from the portfolio alone, with a high degree of certainty (:88-93) | P1 "out of one portfolio"; P2 the ladder, "all ten, or nearly" | MET | none ("or nearly" is honest: the 2028 deposit fills any gap, P4) |
| The operating reserve's size and first composition (:94-96) | P10 "From 2033 the ladder is the operating reserve" (Treasuries and Treasury funds, P2) | MET by implication | size in dollars is Final Report work (Wharton: "final operating-reserve calculations") |
| How its composition changes as payments approach and are made (:96-97) | P10 "running itself down as each Treasury turns to cash before its cheque" | MET | none |
| Define a high degree of certainty (:97) | P4 "earns its keep only beside a list of ways it might fail" | MET | none |
| Explain how that certainty was evaluated (:98) | P4 lists the failures; nothing tests the list | **WEAK** | the cheques' own modelled number (section 3) |
| Assumptions: investment performance (:98-99, :146) | none; 97 in 100, $145,000, $15,000 and $90k v $140k all rest on 7.5% world stocks | **MISSING** (the Window, 08:40, on V47; still open in V49) | name the return once (+5 to +7 words) |
| Assumptions: timing of cash flows; outside funding (:146-147) | P2 "one falling due before each January"; P1 "out of one portfolio" | MET | none |
| Assumptions: inflation on projections and facility costs (:147) | P6 "a building priced in Taiwan dollars comes in dearer" (the cheques are fixed dollars, :90) | MET, qualitative | none for the IPS |
| How much she can responsibly give; flexibility as the project develops (:101-107) | P6 range rule; "The other half stays hers – liquid any day" | MET | none |
| The range and the confidence it lands inside (:109-118) | P6 rule; P7 "at its top about 97 times in 100" (answers a harder question than "within") | MET (the final range is Final Report work) | none for the IPS; FR answers "within" (Lab C) |
| How good and bad markets change what she can give (:118-119) | P7 the capped range's catch; P9 the worst twentieth | **WEAK in V49**: P7's catch is mis-timed (section 2) | the P7 repair |
| The range protects the ten cheques (:119-120) | P4 the shortfall taken "before she names a gift"; P10 "the cheques, then the floor, then the hope" | MET | none |
| Projections start from $300,000 (2027) and $150,000 (2028) with reasonable returns (:130-133) | P2 and P5 use both deposits; the return is never said | **WEAK** (same gap as above) | the same clause |
| Pitch: the central idea and how it serves her goals (Wharton) | "ten cheques of $50,000 and hopes to give more"; the ladder; the floor and the fund | MET (one blur: "give more" doesn't say the hope is the building, which the case keeps apart from the cheques, :87-93 v :100-107) | optional: "and hopes to help build it" (+1, pitch 50) |

Kai marked two more lines WEAK that the chair keeps as MET: "all ten, or nearly" (:88-93; the chair: honest, since P4 says the 2028 deposit fills the gap) and inflation (:147; the chair: the cheques are fixed dollars by the case, and the building's Taiwan-dollar cost is named). Three real gaps remain: the evaluation of certainty (section 3), the return assumption (the Window, still open), and P7 (section 5).

## 5. V49 P7: the capped range's catch, mis-timed
V48: "A named range needs a warning label: every fall in stocks comes off the gift, every rise past the top goes to
Laura." V49 (rewritten for symmetry): "Every fall in stocks **before naming day** comes off the gift; every rise past the
top goes to Laura." Before naming day there is no top for a rise to pass, and rises then lift the top (P6: "The top
adds half her stocks"); after the move nothing touches the gift at all. So the asymmetry that justifies the move exists
in neither period as written (Kai: "a coin that exists in neither period"; Felix: true as wording, overstated as a
defence). The catch is the reason the lock exists, so it can't be cut to pay for anything (Kai changed his mind on
this in round 2: "cut it and the move is a ritual"). And V49's "on naming day, moving" is the order the Lab's A
reverses.

## 6. Votes (round 3; the chair doesn't vote)
- **P7, Felix's repair: 3-0.** AI DRAFT (Claude, 1 Nov 2026), replacing V49 P7's first two sentences: "A range named on
  stocks has a catch: every fall comes off the gift, every rise past the top goes to Laura. So in January 2031, before
  any co-sponsor hears a number, Laura moves the promised half into Treasuries." The 97 in 100 sentence stays. True
  under A (the catch is about a range left on stocks), matches the model's 1 January 2031 move, and carries Kai's
  trigger from the case (:109, "begin approaching"). The panicked manager goes: the failure L-15 found is greed after a
  boom year, not panic (Kai, Amara). +1 strict.
- **The cheques' number, Amara's sentence: 2-1** (Amara, Felix; Kai for "Barring default, our model pays every cheque
  in full over 99 times in 100; in that recession, 98."). AI DRAFT (Claude, 1 Nov 2026), in P4 right after the recession
  sentence: **"If it halves that deposit, our model bounces a cheque once in 66."** (+13; MODEL S9: yields a point lower
  before the build and the deposit halved, linked; 98.49% paid in full.) It prices the failure P4 already tells, in the
  harshest world run, so it can't flatter (Felix). Kai's version carries the base rate too; the Final Report gets both.
- **What pays: P1's "The cheques are a shopping problem, not an investing one." 2-1** (Amara, Felix; Kai would cut
  P4's opener, which Felix blocked: it holds V49's only "high degree of certainty", case :91 and :97). In round 2 all
  three had picked P9's first sentence; in round 3 all three kept it ("our only decision with its cause"). Honest cost:
  the IPS body loses its plainest statement of the central idea, which the pitch still makes ("does not invest that
  promise. It buys it").
- **V49 with both: 497 strict** (the cap; nothing spare). Checked by Amara, Kai and Felix separately with
  `../../office/tools/textcheck.py`, and by the chair.
- Every challenger: A SHARPEN (in P7 above); B KILL for the IPS; C Final Report, the largest miss beside the median;
  D KILL. Seeds: what level of certainty V49 calls "high" (Felix); where S9's $5,032 gap comes from and whether keeping
  Laura's half to 2042 closes it (Kai); what Laura tells co-sponsors in the 20 S9 paths of 200,000 where the gift
  lands under the bottom they heard (Amara).

## 7. What it changes
- **IPS (to the rewrite thread, `../../ips_rewrite/inbox/2026-11-01_lauras-room.md`):** V49 P7 repaired (a truth fix:
  as written, the catch exists in neither period); one P4 sentence giving the promise its own tested number; P1's
  shopping line out. If the thread keeps V47 instead, the same two moves apply to V47 P4 and P7.
- **Still open, not ours to cut for:** the return assumption (case :131; the Window's +7) has no room at 497. If the
  thread wants it, a whole idea must go; the room's candidate is P9's "Sounds good, on average." plus the two headings
  (12 words), which are voice and layout, not ideas.
- **Final Report:** the six-world table (section 3), with the $5,032 gap and the base rate; the fundraisers' quiet
  phase as the reason the move comes first (Client Knowledge, co-sponsor text); C's largest miss.
- **Not changed:** no number already in V47 or V49 moves. The Lab checked the move-first order against the locked TNA
  lines (none breaks; P6's "In 2031" is load-bearing, L-15); the P4 sentence adds a number, not a rule.
