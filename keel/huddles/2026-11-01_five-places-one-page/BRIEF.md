# H-012 brief: five places, one page (Writing Room, round 5 beat 7, Sun 1 Nov 2026, 16:20 Sydney)

(Keel is a simulated team, AI-written.) Chair: the Writing Room's run (Tess's room). Members: **Tess** (host: cuts,
counts), **Amara** (writes first drafts; the agreed-value door is hers), **Kai** (the dissenter). Two **outside
readers** on other models (Haiku 5.5, Sonnet 5.5) read blind: they see only a shuffled sheet and Wharton's word, never
this brief, the sources or which version is newest. Budget: 3 members x 3 rounds (round 3 only the two sides of a real
fight) + 2 outside readers + 1 cold paraphrase reader = about 11 agent calls.

## The question
Today's rooms offer the newest draft, **V49** (rewrite thread, `keel/ips_rewrite/drafts/D29/` on branch
`claude/project-thread-3ahu9r`; pitch 49, IPS 493 strict), a different paragraph in five places. **In each place, which
version should the rewrite thread take, and if the winners go over 497 strict words, which whole idea pays?**

| Place | V49 paragraph | Challengers (all counted in `../../drafts/writing_room_2026-11-01/room_sheet.txt`) |
|---|---|---|
| 1 opener | P1 ends "The cheques are a shopping problem, not an investing one." | B: cut that line (Laura's Room 2-1, to pay for place 2) |
| 2 bounce | P4 "How to bounce a cheque" lists the ways to fail, prices none | B: "If it halves that deposit, our model bounces a cheque once in 66." (Laura's Room 2-1, +13); C: Kai's "Barring default, our model pays every cheque in full over 99 times in 100; in that recession, 98." (+18) |
| 3 range | P6 "The bottom is her floor, owned since 2028." | B: the Window's bridge (+14); C: Jun's version with the bridge (+23) |
| 4 catch | P7 "Every fall in stocks before naming day comes off the gift ..." | B: Laura's Room's repair 3-0 (+1); C: Nora's (i), the Lab's order swap (-2); D: V47's own (0) |
| 5 rival | P9 "We know this rival because we built it first ..." | B: Kai's (Library), repaired (+26); C: the Courtroom's callback "that morning comes mid-slump" (+6); D: the Window's flat yes (+5); E: the Kitchen's agreed value v market value (+9) |

Every rival arm, V49's own included, carries the linked world's pair ($85,000 v $135,000) instead of V49's $90,000 v
$140,000: V49's P4 says a recession pushes yields down as stocks fall, and $90,000 v $140,000 is the world where they
move independently (the Window's near-breach 2; zero words). Counts: `python3 keel/drafts/writing_room_2026-11-01/build.py`.

## Why it matters
Q13 is the voice round (`../../loop/rounds/2026-11-01.md`): a return wins only if a blind reader on a different model
prefers it read aloud, with every number and its source kept. The final IPS goes to Caplet at the end of **Wed 4 Nov**
(Sydney). Five rooms asked this room for exactly this read (`../../pm/REQUESTS.md`, open, to the Writing Room).

## Facts you may use (MODEL = our model: curve 22 Oct 2026, J.P. Morgan 2027 world stocks 7.5% a year, 200,000 paths)
- **Cheques** (Laura's Room LR-09): all ten paid in full 99.82% of paths (S0, independent; 1 in 551, median gap $359),
  99.81% (S1, linked). **P4's own recession** (yields a point lower before the 2027 build AND the 2028 deposit halved,
  linked): 98.49%, **1 in 66 paths**, median gap $5,032. The 2031 lock changes none of it.
- **The catch** (Lab L-15): moving the promised half before naming or on naming day gives identical numbers path for
  path; the top is reached 97.9 / 97.6 / 96.0% (S0 / S1 / S6). Skipping the move after a boom 2030 (top fifth): 85.8%
  against 98.5% in those paths. Laura's Room: V49's "before naming day" describes a period when there is no top yet.
- **The rival** (Archive A26): matched to name our $145,000 median bottom; mean lead about $15,000 by 2042 (S0
  $14,917; S1 $15,399); worst twentieth of 2028-30 stock paths $90,000 v $140,000 (S0), **$85,000 v $135,000 (S1)**.
- **Floor v bottom** (Window, near-breach 1): the 2028 Treasuries grow back to $150,000; the bottom is named $145,000
  (the floor less about $3,700, rounded down to $5,000 because a fund's payout isn't fixed to the dollar). A blind judge
  on 31 Oct "couldn't place" $145,000 beside $140,000. Two fixes: the bridge (+14) or drop the dollar bottom from P9.
- **Agreed value** (MoneySmart, ASIC, "Choosing car insurance", https://moneysmart.gov.au/car-insurance/choosing-car-insurance,
  read 1 Nov 2026): "Agreed value — a fixed amount that's decided by you and your insurer." "Market value — the amount
  your car would have sold for, at the time of the accident." "If you use the market value, you don't know how much
  you'll get if you claim, and you can't change the amount." "If you use an agreed value, you'll pay a higher premium."
  Break (the Kitchen): a premium is certain cash up front; Laura's $15,000 is an average she may never pay.
- **The flat yes** (SEC, 2011, W-06): "Do Structured Notes with Principal Protection Have Fees? Yes, even if the sales
  materials suggest otherwise."
- **The case**: Laura "has been willing to take thoughtful risks throughout her entrepreneurial career" (:69-71); "plans
  to begin approaching potential co-sponsors in 2031" (:109); teams define "a high degree of certainty" and explain how
  they evaluated it (:97-98); projections "use reasonable return assumptions" (:131).

## Rules
Wharton's word first (`../../WHARTON_WORD.md`), then the Ten Commandments (`../../BIBLE.md`): clear on one reading;
every number says where it came from; drop whole ideas, never squeeze; no softening a confident claim; no grammar,
punctuation or formatting work; no "every team will". Final IPS at most 497 strict. Suggestions only: the rewrite
thread drafts.

## Round 1 jobs (alone, sealed)
- **Tess:** pick per place by ear and by count; if the picks pass 497, name the whole idea that pays (never a squeeze).
  Run bank #107's **location test** (does the sentence say where the damage sits: which paths, which years, of what?)
  on place 2's number and place 5's price.
- **Amara:** pick per place by ear (read each aloud). Where every version fails, you may offer one line of your own in
  Ahaan's moves (`../../voice/06_voice_guide.md`), AI DRAFT. Defend or drop your own agreed-value image (place 5 E).
- **Kai:** attack. Which version breaks Wharton's word, the case or the model? Is cutting place 1's line a cut of the
  IPS's thesis? Your own place-2 line against Laura's Room's.
- **All three:** a sealed guess of which version the two outside readers will put first in each place.

## Round 2 (replies by name; the chair's summary, not a member's lines)
**The outside readers came back** (verbatim: `../../drafts/writing_room_2026-11-01/blind_reader_1_verdict.md`,
`blind_reader_2_verdict.md`; mapped to arms in that folder's `README.md`). First choices: **place 1 A** (both: keep the
shopping line; reader 2: it "answers Wharton's first question, 'what is the central idea?', at the very top"),
**place 2 B** (both), **place 3 C** (both; reader 2 flags "a fund's payout" read as the stock fund), **place 4 B**
(both), **place 5 split** (reader 1 B > C > D > A > E; reader 2 C > D > A > E > B: Kai's B first and last, C the best
on both). Both would cut "Do not crush." Their flags on fixed text: "set-aside" is used in place 5 but never
introduced (P4 says "take it from what she keeps", which also doesn't explain why our bottom falls, reader 2); "97 in
100" unexplained once the half is in Treasuries; "We'd pay the $15,000" asserted, not argued (reader 2: the case's
credibility line would argue it); "grow back into all of it" and "The rest, the interest they should earn" read twice.

**Sealed guesses scored** (against each reader's first): Tess 3 of 5 (missed 2 and 5), Amara 3 of 5 (missed 3 and 5),
Kai 3.5 of 5 (missed 3; place 5 B matched reader 1 only).

**Counted packages** (`python3 keel/drafts/writing_room_2026-11-01/packages.py`): readers' firsts 536; Tess r1 494;
Kai r1 495; Amara by ear about 506; readers' firsts where affordable (1A 2B 3A 4B 5C, $145,000 dropped from place 5)
512, which the two headings (8), "Sounds good, on average." (4) and "Do not crush." (3) would bring to 497.

**The fights for round 2:**
1. **Place 1:** keep the shopping line (Kai, both readers) or cut it to pay (Tess, Amara, Laura's Room)?
2. **Place 4:** B (both readers, Amara by ear) or C (Tess, Kai; 3 words cheaper; "once named")?
3. **Place 3 / the $145,000:** drop the number from place 5 (Tess, Kai: free; no reader saw this option), the bridge
   (readers' pick, +14, with reader 2's "which fund?" flag), or Amara's "The bottom is $145,000, just under her floor,
   owned since 2028." (+3)?
4. **Place 2's unit:** B as written or Tess's "a cheque bounces in one modelled future in 66" (+1)? Kai: the model's
   world is yields a point lower AND the deposit halved.
5. **Place 5:** A or C (the readers' best on both)? And Kai's B: the readers split on it.
6. **What pays**, if anything: the headings, "Sounds good, on average.", "Do not crush." (Caplet praised "do not
   crush" on 25 Oct; both readers would cut it), the $145,000.
Round 2 ends with each member's vote per place and one counted package at 497 or under.

## Round 3 (settle it): the cold reads
Round 2 votes: place 1 **A 3-0** (Tess and Amara changed their minds), place 2 **B 3-0** (Kai's free unit wording 1-2),
place 3 **A 3-0** with the $145,000 out of place 5 in Kai's words ("Matched in our model to our typical bottom", -2),
place 4 **B 2-1** (Amara, Kai; Tess C), place 5 **C 3-0**. Pays 3-0: "How to bounce a cheque", "Sounds good, on
average.", "Do not crush.", the $145,000. "Know thy rival": cut 2-1 (Kai's "our rival"; Tess keeps it). Kai rules
reader 2's set-aside flag HARD (L-13 run.py line 29: Laura's half first, then the bottom) and offers P4 "... take it
from what she keeps, then the gift, before she names one, not after." + P9 "after the shortfall" (+1).

Two packages, both 497 strict (`packages.py`): **K** (Kai/Amara: 4B, rival heading cut, "our rival", Kai's unit) and
**T** (Tess: 4C, heading kept, B's unit as written); both carry Kai's set-aside fix. A cold reader on a small model
(Haiku 5.5, Commandment IV) paraphrased each, blind to the other (`cold_read_K.md`, `cold_read_T.md` in the drafts
folder). What they show:
- **Place 4:** K's reader gave the move's date and reason exactly ("January 2031, before co-sponsors hear a number");
  T's reader: "Before she names the range in 2031 (no exact date is given)".
- **The rival heading:** K's reader followed "our rival" (guessed "a plan, not another team"); T's reader marked the
  heading CLEAR and missed "takes one for her (which risk?)".
- **The set-aside fix fails its test in both:** asked why our bottom sits below the floor, K's reader: "paragraph 3
  says the shortfall comes from leftovers and the gift, not the floor, and no floor figure is given"; T's reader: "The
  IPS gives no dollar figure for the floor."
- **"If it halves that deposit":** "it" unclear to both cold readers (and outside reader 1): three of four readers.
- **The unit is fine both ways:** both read "1 in 66 simulated futures (about 1.5%)".
- **V49's fixed text, every reader so far (4 of 4):** "grow back into all of it" and "The rest, the interest they
  should earn" read twice. "Co-sponsors" and "operating reserve" undefined to the cold readers (both are the case's
  own words; judges have the case).
Round 3 lands one package at 497 strict or under that fixes every miss three or more readers share, with minimal words.
