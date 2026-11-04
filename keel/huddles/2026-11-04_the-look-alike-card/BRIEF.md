# H-030 brief: the look-alike card (Genius Lab, Wed 4 Nov 2026, round 8 beat 5)

(Keel is a simulated team, AI-written. FICTION: the members are simulated; their work is real research and tests.)
Chair: the Genius Lab's run (Jun heads the room). Budget: 3 rounds, 7 agent calls.

## The question
Tomorrow (Thu 5 Nov) Caplet's six students rewrite the final IPS in their own words. Since 27 Oct, a one-word swap has
broken a true fact in our drafts at least eight times ("ten Treasuries" for ten holdings; "before its January" for
before it matures; "her floor" without "rounded down"; "a Treasury held to maturity pays exactly" beside two funds that
pay their net asset value; "one weakness"; "as if no more interest were reinvested", which misses the funds' waiting
cash). **Can one page show Caplet each fact in the final IPS beside the false look-alike that once stood in its place
(or that a natural rewrite would land on), so they can reword freely without landing on one? And does it actually
catch the breaks a real rewrite makes?**

The idea comes from Amara (the Kitchen, 3 Nov): hospital pharmacies print look-alike medicine names with the differing
letters in capitals ("tall man" lettering; Australian Commission on Safety and Quality in Health Care), so the eye
lands on the part that differs. The Kitchen voted 3-0: **no numbers on the card, and no "words to keep"** (Wharton
asks for "an authentic team voice": the card protects facts, not wording).

## Files (repo root = /home/user/caplet-investment)
- The final IPS and pitch: `keel/ips_rewrite/drafts/FINAL/ips.txt`, `pitch.txt` (what Caplet rewrites)
- The submitted trading-notes reflections (locked; judges read them beside the IPS): `keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt`
- Look-alikes found before: `keel/loop/FRONTIER.md` section 2 (F1, F11, F15, F16, F17, F19, F21, F22); the Window's
  three (`keel/pm/REQUESTS.md`, row "The Window (Felix, H-028) | The Genius Lab"): "we don't duration-match" /
  "duration-matched" (say "each payment has its own bond"), "the funds pay exactly what they promised", "the ladder's
  one weakness"; the Kitchen's list (same file, row "The Kitchen (Amara, over chai; H-027)"); the Library's lock fix
  (`keel/ips_rewrite/inbox/2026-11-04_library.md`); the Window's note (`keel/ips_rewrite/inbox/2026-11-04_window.md`)
- The case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf` (text: search the repo for
  `client_profile` .txt/.md copies if you can't read the PDF)
- Voice: `keel/VOICE.md`; people: `keel/CAST.md`, `keel/CULTURE.md`, your own `keel/members/<name>.md` (above "## Agent profile")

## Rules for anything Caplet sees (Ray, 3 Nov, I80)
One page, plain English a Year 11 gets on first read. No internal labels (no room names, F-numbers, huddle IDs,
version numbers, file names). No numbers on the card. No slogan flips, no two-word kickers. Each row: the true fact in
plain words, the false look-alike with the differing part in CAPITALS, and why it's false in a few words.

## Rounds
1. **Go away and read** (parallel; nobody sees the others): Kai builds the card. Jun writes three rewrites of the
   final IPS the way three different Year 11 students would, without any card. Amara writes her judging sheet,
   sealed, before she sees the card. Kai also roasts the Lab's L-18 hypothesis, blind to its result (below).
2. **Reply by name** (parallel): Jun audits his three rewrites against the final IPS's facts and the TNA, lists every
   fact that broke, and counts how many the card names. Amara judges the card cold against her sealed sheet.
3. **Land it**: Kai revises the card to Jun's misses and Amara's verdict. Then one stranger with no stake uses only
   the revised card to check Jun's three rewrites, to see if a student could actually use it.

## The Lab's L-18 hypothesis (Kai roasts it in round 1, blind to the result)
The Library asked: when the 2028 deposit falls short in the same downturn that hits her shares (the IPS's own warning
in P5: her income "can dry up in the same downturns that hit share prices"), does every cheque still get paid under
the final lock? The chair's hypothesis: in this plan Laura owns **no shares in 2027**: the first $300,000 is all
ladder, and shares are bought only on 2 Jan 2028 with what the deposit leaves. So a 2027 downturn can shrink the
deposit, push rates down (the ladder's reinvestment gap grows) and make the floor dearer, but it can't also hit shares
she doesn't own yet. The plan's ORDER is what stops her betting on shares twice. If that holds, the test should show
every cheque paid in a 2027 downturn with the deposit halved, and the damage landing on the gift, not the cheques.
Test: four new model worlds on the Courtroom's exhibit N machinery (`keel/rooms/lab/L-18_the_same_downturn/run.py`).

## Chair's change to round 3 (14:00 Sydney, before any round-3 result)
Kai rebuilds the card from Jun's audit of Jun's own three rewrites, so testing the new card on those same rewrites
would grade it on the answers it was fixed to. Round 3 therefore adds a **held-out test**: a stranger to our notes
writes two fresh rewrites (D, E) from the final IPS alone; a second stranger, with only card v2 and no IPS, marks every
line they'd change; Jun audits D and E against the final IPS and the submitted notes (the truth) and scores the
stranger's marks: caught, missed, false alarm. Budget 9 agent calls (was 7).
