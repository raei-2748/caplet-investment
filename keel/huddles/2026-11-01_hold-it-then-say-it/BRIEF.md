# FICTION. H-010 Hold it, then say it (Genius Lab, Sun 1 Nov 2026, round 5 beat 5)

> Keel is a simulated team, AI-written. Chair: Nora (builder today; the run assembles). Members: **Nora** (builder today, per the round file;
> she never judges her own challengers), **Jun** (Lab head, his model), **Kai** (roasts first, before any test).
> Budget: 3 rounds x 3 members = 9 agent calls. Starts from two H-009 seeds (the Library, this morning): the
> lock-timing test and the order test, both filed to the Lab in `../../pm/REQUESTS.md`.

## The question (Q13, round 5, the voice round)
**Who asks a sceptic to pay for a promise, in under a hundred words, and gets believed?** The Library read people
whose job is exactly that (annuity sellers, auction houses, mountain guides; every quote re-checked at source;
`../../loop/rounds/2026-11-01.md` section 4). Today the Lab pairs those finds with the current draft and tests the
strongest pairing in the model.

## The champion: V47's three range paragraphs (AI DRAFT, `../../ips_rewrite/drafts/D27/ips_V47.txt`; 497 strict)
- **P6.** "In 2031 she gives co-sponsors a range. The bottom is the floor she has owned since 2028. The top is the
  floor plus half her stocks. The other half stays hers, to sell any day if a building priced in Taiwan dollars comes
  in dearer."
- **P7.** "A capped range has a catch: once named, every fall in stocks comes off the gift while every rise past the
  top goes to Laura. On the day she names it, the half she promised moves into Treasuries, and in our model the gift
  reaches its top about 97 times in 100."
- **P8 (the rival).** "... Matched in our model to name our $145,000 median bottom, it usually wins: counting the gift
  and what she keeps, it leaves Laura about $15,000 more on average by 2042. But in the twentieth of modelled paths
  where 2028-30 is worst for stocks, it names about $90,000 to co-sponsors against our $140,000 after the 2031
  set-aside. We'd pay the $15,000."

The case (`../../../competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, lines 109-120): "Laura plans to
**begin approaching** potential co-sponsors in 2031 ... she will need to describe how much she expects to contribute
... In 2031, however, the value of her portfolio in 2033 remains uncertain. If Laura promises more than she can
ultimately contribute, she could damage her credibility ... Teams must recommend the dollar range ... and state how
confident they are that her 2033 contribution will fall within that range. They should explain how favorable and
unfavorable market outcomes could affect the amount she can provide."

## Today's finds the Lab paired (all verified at source by the Library, 1 Nov)
- **A1, the turnaround (Amara):** Rob Hall, as Krakauer reports him: "Our turn-around time, he said, would probably be
  1 P.M., and no matter how close we were to the top, we were to abide by it." The limit is fixed before anyone can
  see the top. It failed on the day: a client summited "well after Hall's pre-determined turn-around time".
- **K3, the location test (Kai):** a buyer distrusts a condition report that names a flaw but not where it sits ("You
  wouldn't guess from this that the scratches ... were in the face"). A confession is owned only when it has an address.
- **A2, the published test (Amara):** Mountain Trip gives climbers the pace test in hours and how often it bites ("less
  than 2% of the time") before anyone pays: the doubter's own units, and the rate.
- **Stepping stone S16 (`../../loop/FRONTIER.md`):** UNC won't award a building contract until 100% of the budget is
  cash; Laura doesn't name a bottom until she owns it.
- **The Library's open question (Felix, H-009):** "even in a week when stocks are rising" promises a step (moving the
  half) that someone has to take on a day Laura picks. Kai, H-009: "who holds the watch?"

## Three challengers (Nora builds; novelty check in the lab write-up)
| # | Challenger | Hypothesis (one sentence that can be wrong) |
|---|---|---|
| A | **Hold it, then say it.** Reverse V47's order: in January 2031, before her first co-sponsor meeting, the half she'll promise moves into Treasuries; only then does she name the range. Both ends are then money already sitting in Treasuries when she says them, at every meeting that year, not only "the day she names it". | Moving first changes no V47 number, while naming first and moving later costs the top's 97 in 100 at least 3 points if the move slips a month, and more if she skips it after a strong 2030. If a month's slip costs under 1 point, the order is cosmetic and the clause isn't earned. |
| B | **The price's address.** Say where V47's "$15,000 more on average" sits: in which futures the rival's lead is earned. | At least three-quarters of the rival's average lead comes from the fifth of paths where 2028-32 stocks do best, and in the worst two-fifths our plan leaves Laura ahead. If the lead is spread evenly, "the address" is a brochure line. |
| C | **The miss, sized.** Give the doubter the miss in their own units: when the gift falls short of its top, by how much. | On V47's design the misses are small in every world tried: the median miss under $1,500 and nine in ten misses under $5,000 (S0, S1, S6). If S6's misses are big, the line can't be said. |

## The test (after round 1; MODEL)
One script on the L-13 -> L-14 -> A26 chain (V45/V47's design: the 2031 set-aside, the slide, the lock), unchanged,
one block appended: `../../rooms/lab/L-15_hold_it_then_say_it/run.py`. Curve 22 Oct 2026, J.P. Morgan 2027 world
stocks 7.5%, 200,000 paths, seed 20261016; worlds S0 (independent), S1 (rates and stocks linked, the world V47's P4
argues), S6 (yields fall 2 points for good). Inside a year, stocks are assumed to wander as a random walk that ends
at the model's own year-end value (a Brownian bridge), so the yearly paths are untouched.

## Rules
Wharton's word first (`../../WHARTON_WORD.md`), then the Ten Commandments (`../../BIBLE.md`): one paragraph-sized idea,
taken or dropped whole; every number says where it came from ("we modelled"); no "every team will"; Caplet XR stays
subtle; no mountain, no Hall, no auction house in the IPS (the Library's verdict). Talk like yourself
(`../../VOICE.md`), short. Fiction never enters a Caplet deliverable; the numbers are real MODEL output.
