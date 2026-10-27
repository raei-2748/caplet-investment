# FICTION (the room, the people, the votes) + real work. Long Room, Sat 24 Oct 2026 (afternoon): the IPS, line by line

> **Summary.** Called by Nora after Ray asked Keel to work on the IPS. Six members, one table: the morning's twelve
> edits, the ladder at ~$300k, vote set B, the open motif. Jun found a timing error in the shortfall sentence (the
> gift above the floor is paid in 2033, the coupon gaps arrive in 2038-42). The ideation ladder stopped at rung 1 with
> a plain line for "one yield hits twice". Five new edits (K1-K5), IPS 494 strict. Motif still held open to Monday.
> **Arcs:** Nora holds a question open on purpose (second time); Jun says the thing he's afraid of out loud; Kai
> loses a cut and takes it. **Values:** 2 Where does it say that?; 4 Say it the day you see it. **Ideas:** none new;
> "one price, twice" moved from a finding to an IPS sentence.

Sydney, Sat 24 Oct, 15:10 to 17:40. Long Room: light (one sitting, about two room days of work, because the IPS is
fourteen days out and nothing in it is new strategy). Countdown: IPS and trading lock in 13 days 16 hours (Sat 7 Nov
09:00). AI-generated; not for submission. Output for Caplet: `2026-10-24_IPS_edits_v2.md`.

## Before the table
Nora came straight from the bakery, flour still on one sleeve, forty minutes late because the Saturday girl called in
sick and someone had to do the 1 p.m. bake. Amara was on the phone from the gurdwara kitchen for the first hour, a
tray of rotis audibly going past her. Jun had spent lunch trying to pull Friday's US close and got nothing:
treasury.gov wouldn't load, nor would the Fed's data site. "So the 22 Oct close is still the newest number we've got,"
he said. "$298,861 on payment dates. Four basis points of room. Or minus two thousand, depending on which basis you
like. Which is the point: no number goes in the IPS."

## Item 1: the morning's twelve edits
Tess read them aloud, one at a time, with the counts. Eleven went through without a word. E12 did not.

Jun had the model open. "This sentence says a short payment is covered by the half Laura keeps, then the contribution
above the floor. When is the contribution paid?"
"2033," said Amara.
"And when does a coupon come up short?"
Nobody answered, so he did. "The later payments. 2038 to 2042. The gift above the floor was spent on a building five
years earlier. It can't cover anything then." He scrolled. "Our own model doesn't do what our sentence says. It prices
the gap in 2033, at that day's yields, and takes it out before the gift. So the sentence is wrong and the plan's
right."

Kai leaned back. "Who says a judge notices?"
"A judge who knows bonds notices in one read," Jun said, and then, quieter: "I nearly didn't say it. It's my model.
I wrote that sentence's number on the 16th and never checked the words against the code."
Tess wrote that down, word for word. Value 4.

Jun's fix (K5): *"Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside
from the half Laura keeps, then the contribution above the floor."* Felix checked it against the code
(`ips_numbers.py`, lines 209-227) and against D1's buffer option: a buffer slots in as one more clause. **6-0.**

## Item 2: one yield, twice
Kai had brought the morning's Long Room finding back. "Jun's line. One price hits us twice: before we buy and while
the cash waits. That's the only sentence anyone's written this month that a judge hasn't read in another team's IPS.
It goes in."
"In five hundred words," said Tess. "With what?"

Nora ran the ladder on it the way Ray set it up: rung 1, wide, thirty-five candidate sentences, from drought and tides
to caramel and cricket. Felix struck every image in under five minutes. "A drought raises the price of water. It
doesn't raise the price of a future dollar. If the picture needs the next sentence to explain it, it's wallpaper."
What survived was plain: *"One yield sets both the ladder's January price and what its coupons earn later, so a single
fall works twice."* Rung 1 had a keeper, so the ladder stopped there.

Amara pushed back, and meant it. "A judge reads that and feels nothing. Laura reads that and feels nothing. Where are
the artists in it?"
"They're in the next paragraph," Kai said, "in the bit where it doesn't happen to them."
"That's a good line. Say that one in the Final Report." She didn't change her vote.

Tess found the words: the sentence *is* D2 option c (name the one residual risk), so the optional seven-word D2 add
from the morning can go. **5-1, Amara against** (K2).

## Item 3: what Tess cut
To fit K2 and K5, Tess wanted "A fall in stocks can shrink only the part above the floor." gone (K3).
Kai didn't like it. "That's the echo of 'VT is where we allow ourselves to be wrong'. It's the locked line."
"The pitch says the branch grows the gift above the minimum," Tess said. "The next sentence says we refuse to move
floor money into stocks. Which job is your sentence doing that those two aren't?"
Kai looked at it for a long time. "Fine. You win this one. I want it on the record I lost it with dignity."
**4-2 (Kai, Amara against).**

## Item 4: Felix's two catches
1. **"Promised" (K1).** P4 ends "so she never gives more than she promised". Felix read the case aloud: Laura wants a
   range "rather than promising one exact amount" (`Laura_Gao_2026_Client_Profile.txt`:115-116). "Our own checker
   flags 'promised' too. P4 and P5 already say 'quoted'. Same word, same thing." **6-0.**
2. **The reserve's make-up (K4).** The IPS brief asks for "the operating reserve's asset composition over time"; the
   draft gives it half a clause. Felix and Tess checked the book line by line (`competition/COMPETITION.md`:169-170,
   197-206): IBTM to IBTR pay 2033-37, the five T-bonds pay 2038-42. *"...the operating reserve: five Treasury ETFs
   that close one a year to 2037, then five bonds to 2042."* **6-0.**

## Item 5: the motif, and Tuesday
Amara wanted to know whether today's lines would survive Monday if the print run won. Nora made everyone check: none of
K1-K5 names roots, paper or presses beyond the pitch's Root & Branch. "Good. Then Monday decides the Final Report's
image, not this page. And I'm not closing it today." She put the card back on the wall. Tess noted that was the second
time this week Nora had left something open on purpose.

For Tuesday's vote set B the room agreed on what each answer does to the text: D1 option c adds nine words to K5 and
Tess has the cut ready; D1 option d needs a P5 clause dropped; D2 is now K2. Jun will reprice if a new close comes
through. Nobody trades: D6 stays hold.

## Decisions (Keel's; Caplet decides)
| Decision | Owner | Date |
|---|---|---|
| K1-K5 go to Caplet as suggestions (file `2026-10-24_IPS_edits_v2.md`) | Tess | Sat 24 Oct |
| Motif stays open to Mon 26 Oct; IPS lines kept motif-proof | Nora | Mon 26 Oct |
| Reprice on the first new close that loads | Jun | next run |
| D1 c/d wording ready for Tue 27 Oct | Tess, Felix | Tue 27 Oct |

## Ideation ladder record (for `keel/office/ideation_log.md` when PR #25 merges)
Question: one IPS sentence (12-24 words) that makes "one yield hits twice" visible and literally true. Rung reached:
1 (Haiku 5.5, 35 candidates: plain finance, Root & Branch echoes, print run, weather, sport, cooking, music). Keeper:
"One yield sets the January price of the ladder and the rate each coupon is reinvested at, so a single fall works
twice" (rung 1, tightened by Tess). Killed: every image (drought, tide, choir, caramel, cricket, paper), because none
maps the yield-to-price link; a judge would read them as decoration. Stopped at rung 1 (keeper found).

## What Caplet can take from today
1. Fix E12's timing whatever else you change: the gift above the floor is paid in 2033 and cannot cover a 2040
   shortfall; say the gap is priced and set aside before the gift (K5).
2. Swap "promised" for "quoted" in P4 (K1); the case says Laura is not promising an exact amount.
3. Give the reserve its make-up in one clause (K4); it is a named IPS requirement.
4. Decide on Tuesday whether the plan's one insight goes in (K2). If it does, the D2 add is not needed.
5. Strict count with everything: 494. If D1 = c, cut "since no dollar asset is safer".

## Sources
Case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`:44, 115-119. IPS brief:
`competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt`:48-52, 68-70. Book:
`competition/COMPETITION.md`:169-170, 197-206. Model: `keel/library/ips_numbers_2026-10/ips_numbers.py`:209-248;
22 Oct run `keel/rooms/lab/L-02_results_22oct.json` (PR #28): post-2033 gap p95 $5,462; ladder $298,861 (payment
dates). Counts: `keel/office/tools/textcheck.py`. MODEL figures are model output, not facts. (Keel is a simulated
team, AI-written.)
