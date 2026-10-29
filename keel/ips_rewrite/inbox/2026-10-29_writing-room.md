# Writing Room, Thu 29 Oct 2026 (16:20 run, round 2 beat 7): the four doors, made comparable and read blind

(Keel is a simulated team, AI-written.) AI DRAFT material (Claude, 29 Oct 2026); suggestions only, not for submission.
Round: `../../loop/rounds/2026-10-29.md`. Texts (full IPS each, counted) and the script that builds them from V29:
`../../drafts/writing_room_2026-10-29/` (`build.py`; reads `../drafts/D9/ips.txt`). Readers: `cold_reads.md` there.
Numbers are the Lab's and Laura's Room's (L-12, LR-06; curve 22 Oct 2026, 200,000 paths, seed 20261016, MODEL). This room
ran no new model.

**For a judge, first.** Wharton asks for a "decision-making framework" for how the plan acts "as the client's needs
change". V29 answers in one line, "If needs change, cheques first; floor and stocks are bought smaller together", and a
blind reader called that line "too garbled to work as one". The version below swaps it for an order and a clock:
*"Every rule here fires in a year the case already set, never on a hunch; if needs change, the gift takes it before it
is named, her half after, a cheque last."* Three blind readers out of three advanced it over V29 with only the hard fixes.
The price is one whole idea: the range's two embarrassments (too low or too high). Every reader called that idea the one
thing the losing version did better.

## 1. Each challenger beside the champion (claims at most 15 words)
| | Claim | If it wins, the judge sees | Read blind |
|---|---|---|---|
| **C13, V29 as written** (champion) | Each promise is made safe the day it becomes one; if needs change, cheques first. | A principle, but the dates are spread across four paragraphs and the judge must put them together | A (V29 + hard fixes): framework found 2/5 and 3/5; lost both reads |
| **C, four doors** (Lab, amended by Laura's Room) | Every rule fires in a year the case set; the gift gives way first, cheques last. | One sentence to point to; a reserve that "runs off one rung at a time" (professor); "sounds like a policy and not a slogan" (practitioner) | **B: won 3 of 3** (3/5, 4/5, 4/5) |
| A, buffer table + per-rung alarm | As the cushion thins, the hope shrinks first, by steps written today. | Nothing in the IPS (the table moves no number before naming day); Basel explains the 2031 mark in the FR | not read (parked, FR) |
| B, the one-way valve | A change may make a promise smaller or sooner; never bigger, never later. | The answer to "what if Laura changes her mind?", which V29 never gives; ~15 words with no room in B at 498 | not read (Courtroom's trial tonight) |
| D, Chile's order of payment | Cheques, then the named gift, then the unnamed gift and her half. | Already inside C's order line ("a cheque last") | folded into C |

**The line in our voice, for C** (Ahaan's moves: concede, then turn; one odd word). The judge-facing line is the one
above. The ninety-second rule stays as the Lab wrote it, for the Final Report or the closing: *"Our rules fire on dates,
not alarms – every promise in this case has one."*

## 2. Three counted versions of V29 (pitch unchanged, 48)
| File | What changes from V29 | Words (larger count) |
|---|---|---|
| `ips_A_hard.txt` | H1, H2 and H4 below; nothing else | 499 |
| **`ips_B_doors.txt`** (the readers' pick) | A + the order-and-clock line + "the ten holdings become the operating reserve" (Laura's Room) + H3; **paid by** para 8's two embarrassments ("In 2031 she names a range. Its bottom is…") | **498** |
| `ips_C_doors_keep_range.txt` | B with the two embarrassments back, without the "three times" and the donor clause; paid by the wipe-out line and "never on a hunch" | 497 |

C lost its head-to-head with B (1 reader). Its loss means the wipe-out line counts for more than the range reasoning in
Q's reader's eyes; it doesn't mean the range reasoning is worth nothing. **Writing Room lean: B for Saturday**, with
the range's two embarrassments moved to the Final Report (bank #5, #6 become FR-first, still cited there).

## 3. Hard issues in V29 (at most 5, minimal edits)
1. **H1 "then never changes" is false.** The reserve shrinks every January as each holding pays its cheque (case
   :94-97; Laura's Room LR-06). Edit: "In 2033 the operating reserve tops up once, then only shrinks." (+1; B uses Laura's
   Room's longer line instead.)
2. **H2 "money she has buys certainty; money she expects carries risk" overreaches.** Without the 2028 deposit a
   cheque is short by >$1k in 57% of paths (L-12). Edit: "money she expects insures it, then carries risk." (+2)
3. **H3 "her first $300,000 buys them in January 2027".** On the 22 Oct curve the real holdings cost $224 more than
   $300,000 (only the idealised payment-date ladder fits, by $1,139: `../../pm/RISKS.md` R1), and the ladder costs more
   than $300,000 in 46-47% of MODEL paths. Para 6's "fills any gap" admits it. Three readers today tripped on the pair, the Window this morning and
   two blind readers, one of them saying "the core rule breaks". Edit: "buys them, or nearly, in January 2027" (+2;
   fits in B, not in A at 499). The deeper fix is the Courtroom's: say what "made safe" means for a cheque that is
   99.9% bought in 2027 and finished in 2028.
4. **H4 "which we judge three times worse" is stale.** The bank's own note says the 2031 lock makes it 5-10 times.
   Today's top is reached 86.6% of the time (L-12, S0), which weights over-promising 0.866/0.134 = about 6.5 times
   under-promising. Edit: "three" -> "six" (0 words). Two readers called the number "made up". A true number still
   reads made up when nothing in the text earns it, which is one more reason the idea suits the FR.
5. **Reader notes, no edit proposed here (the rewrite thread's call):** "sized to regrow what's left by 2033" (all
   three readers: what is left of what?), "about one dollar in fifteen" (two: of what, over how long?), and "ten debts
   of one government stand or fall as one" (all three read it as a confession, not an argument).

## 4. Requests closed and filed
Closed: the Window (the $300,000 line: H3 in B); Laura's Room (reserve line: in B, without "first", because a reader saw "from her half" collide with the wipe-out
line); the Lab (insurance clause: H2); the Rooftop (para 9 leads with the rule, no dollars; it reads as a 2031 decision
in a framework, not a trade, and B makes that explicit); the Archive (A22-A23 met in V29); the Long Room (both met in
V29, and V29's blind head-to-head was the cold read). Filed: the Courtroom (B vs V29 tonight, plus the practitioner's
"once the top is locked the range is close to a single number"); the Lab (count how often door 4 reaches the gift's top
after naming).

## Honest weaknesses
The readers are AI subagents told only the case and Wharton's instructions, so three reads is a signal, not a verdict.
B's "her half after" leaves out door 4's last resort: after naming, the gift's top can still be reached once her half
is gone (never the bottom, 0 of 600,000). The share of paths where that happens is uncounted. "A year the case already
set" is true to the year only; the case dates 2031 to the year (:109), and January is our choice (LR-06). B was edited
after round 1 and again after round 2, so the final B text was read blind only in round 2, apart from H3 and the
reserve line.
