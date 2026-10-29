# C-03: four doors on trial (Thu 29 Oct 2026, round 2 beat 8)

FICTION (the room and the people) + real arguments and real tests. AI-generated (Claude Code). Not for submission;
Caplet rewrites in its own words. (Keel is a simulated team, AI-written.)

**On trial:** challenger C (four doors), as the Writing Room's text B (`../../drafts/writing_room_2026-10-29/ips_B_doors.txt`,
498), against champion C13 (V29 para 10's one line, `../../ips_rewrite/drafts/D9/ips.txt`). Paragraph it moves (LS-10):
V29 para 10 only. Folded in: five open requests to this room (Writing Room, Laura's Room x2, Lab, Library).
**Kai** prosecutes · **Jun** repairs (one repair) · **Felix** judges cold (two blind readers) · **Nora** rules ·
**Tess, Amara** defend.

## 1. Kai's charges (strongest version first)
- **K1, the order line contradicts its own paragraph 17.** B: "if needs change, the gift takes it before it is named,
  her half after, a cheque last." Read as a ranking, the gift pays before her half. But para 17, two paragraphs up,
  sells her half for the coupon gap *before* anything comes off the quoted bottom, and so does the model
  (`../long_room/LR8_banked_at_the_mark/run.py` line 29: `x` is sold from Laura's half in Jan 2031; the bottom loses
  only what spare cash and her half can't cover; door 4 in 2033: spare cash, her half, then the gift's top). The one
  sentence a judge will test against the rest is the one that fails the test. It is also a tricolon, the shape the
  voice study flags first.
- **K2, the one rule breaks on its first promise.** "Made safe no later than the day it becomes one", yet the cheques
  are promises from page one and are finished only in 2028, with money she *expects* (ladder above $300k in 46-47% of
  MODEL paths; with no deposit a cheque is short >$1k in 57%, L-12). "Or nearly" admits the break without mending it.
- **K3, B sold the range's why.** Dropping "too low ... too high" leaves "In 2031 she names a range" with no reason,
  and the practitioner's question ("once the top is locked, what is the range a range of?") has no answer in the text.
- **K4, Spinnaker (simulated, real evidence only):** "fires on dates, never on a hunch" means four years of ignoring
  the market. **Reads as AI?** Only the tricolon. **Competent but forgettable?** Not with the wipe-out line.

## 2. Defence and Jun's one repair
- **K2 answered (Tess):** the case states the 2028 deposit as a fact, not a hope; the 57% is Keel's own stress. Para 9
  ("money she expects insures it, then carries risk") and para 11 ("fills any gap in the ladder") tell the truth in
  the text itself. The cheques are the one promise made before there is enough money to finish it, so they get the
  first money there is, and the first ~$50k of the next. **K2 fails as an IPS charge; it lives in the FR** (bank #73).
- **K4 answered (Jun):** the one market-driven exception anyone would ask for, waiting a year to lock after a fall,
  was tested (L-12): top reached 84.6% -> 73.6%, and 0.2% if stocks halve in the delay year. Date rules lose nothing.
- **Jun's repair, for K1:** state the principle the model obeys instead of a ranking it doesn't:
  > "Every rule here fires in a year the case already set, never on a hunch; if needs change, the change lands on
  > what isn't yet promised, never a cheque."

  True at every door: before 2031 the hope shrinks (floor and stocks bought smaller); on naming day the coupon gap
  comes from spare cash and her half, then the bottom *before it is quoted*; after naming her half pays, then the
  gift's top, never the bottom (0 of 600,000, LR-06). It is the one rule read from the other side: a promise is
  made safe on its day; a change can only land where no promise stands. **B2 = B + this line, 495 words**
  (`C-03_build.py`, `C-03_B2.txt`).

## 3. Felix's cold judgement (`C-03_cold_reads.md`)
Two blind readers, shuffled, case + Book 7 + Book 8 only: **both advance B2 over V29** (35 v 33; 35 v 34). Both found
the framework in B2 at once ("plainly a framework"; "a real framework") and none in V29 ("a slogan"; "a priority
order"). Both docked B2 one point on Client Knowledge for the lost range reasoning (K3 lands), both found
"comes off the quoted bottom" and the floor-sizing clause hard on first read. Neither tripped on B2's order line.

## 4. Rulings on the folded requests
| Ask (from) | Ruling |
|---|---|
| B vs V29 (Writing Room, Lab) | **AMENDED: B2 replaces C13's holder.** A judge can point at it and say "that's their framework" |
| "Made safe" for a cheque finished in 2028 (Writing Room) | Rule **stands**; "or nearly" **stays** (para 11 explains it). The 57 / 16 / 0.45 / 0.05% deposit table goes to the FR (#73) |
| "Once the top is locked, the range is close to one number" (Writing Room) | Range **upheld**: the case asks for one, and the width is half the stocks on naming day. The answer is the range's why (K3), not a different object |
| Kai's amendment, door 2 insures the cheques first (Lab) | **Already in B** (para 9, para 11) |
| "Between Januaries nothing is sold" (Lab) | **Never write it**: her half is hers any day. "No Treasury is sold before it pays" is the true form, already in |
| One-way valve (Laura's Room, #76) | **FALLS for the IPS.** "Safe sooner, never later" is the one rule's own "no later than"; "smaller before it is named" is B2's order line; the only new power, locking early when stocks feel high, is a hunch door the dated line forbids. FR: the clearing-house reading of "no later than" |
| Signed, expiring override (Library S-07, #70) | **FALLS.** A delay is a free option for Laura paid by the co-sponsors (L-12). FR: why the policy has no override, with the test |
| "For 2031 we choose its first day" (Laura's Room) | **No IPS words needed**: "in a year the case already set" is true as written. FR: one date, one number for every co-sponsor (#77) |

## 5. Discussion and Keel vote
**Promote B2: 5-1** (Nora, Jun, Tess, Amara, Felix / Kai: park until the range's why is back). Promoted to the rewrite
inbox (`../../ips_rewrite/inbox/2026-10-29_courtroom.md`).

## 6. Nora's ruling: AMENDED, one change that matters most
**Put the range's why back (Client Knowledge, Book 8; Book 7 W5), in one clause, without the multiplier.** Both
judges named it as the only thing V29 does better. Candidate B3 (`C-03_B3_candidate.txt`, 498, untested): para 13
"In 2031 she names a range: too low costs gifts; too high, her word."; para 17 "comes off the bottom before it is
quoted"; paid by cutting "sized to regrow what's left by 2033 and" (both readers stumbled on it). The Writing Room reads
B3 blind against B2 on Fri 30 Oct; if it loses, B2 stands.
