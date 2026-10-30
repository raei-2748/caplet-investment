# The Window, Fri 30 Oct 2026: the wipe-out line reads its own test backwards

AI-generated (Claude Code) for the Keel Office. (Keel is a simulated team, AI-written.) Round 3, beat 2 (Gate).
Felix; agents rules-verifier, integrity-officer, fact-checker. Checks only; no draft edited.

**Result.** The Saturday candidate's best line, "wipe out every share she owns and no cheque is worse off", is false in
our own model: the shares never hurt a cheque, but wiping them out does leave one worse off in about 1 path in 500. The
true version is shorter and still lands: "The shares can help a cheque, never hurt one."

## Breaches and near-breaches (top)
1. **BREACH, false fact, in V29 para 11, B2 and B3 (all three texts in play for Sat 31).** "Wipe out every share she
   owns and no cheque is worse off – only the gift." Source: `../../rooms/archive_checks/A19_results_S0/S1/S6.json`
   (28 Oct, MODEL). The key the line was built on, `paths_where_stocks_make_a_cheque_worse: 0`, says the shares never make
   a cheque worse. The same file says that with the shares wiped, a cheque is worse off in **364 / 354 / 412** of 200,000
   paths (S0/S1/S6), **71 / 70 / 82** by over $1,000, by up to **$2,812 / $2,812 / $2,953**, and payments short by over
   $1,000 rise from **0.03% to 0.07%** (S6 0.05% to 0.09%). Why: money banked from her half in 2031 above the 2033 need
   stays behind the cheques. The Archive's own register even says the shares *help* a cheque in ~2 paths in 1,000; both
   cannot be true. Second fault: "only the gift" forgets her half, which is shares too, and after naming day the wipe-out
   hits *only* her half (the promised half sits in the first cheque's fund).
   **True lines, same idea:** (a) "The shares can help a cheque, never hurt one." (10 words, saves 5; 0 of 600,000); (b)
   "Wipe them all out and the cheques barely notice; the gift does." (keeps the thought experiment). Felix's pick: (a),
   because a judge can't check "barely". Marked in place: `../../rooms/archive.md` A19, IDEA_BANK #66. Request filed to
   the Writing Room (it reads B3 v B2 today). "No cheque depends on a share price", also allowed in A19, fails the same way.
2. **Near-breach, V29 para 13: "which we judge three times worse. So ..."** The "so" doesn't follow from anything: the
   bottom and top are set by a rule, not sized to a cost ratio, and the ratio the rule implies swings with the world
   (top reached 86.6% in S0, about 6 to 1; 44.0% in S6, under 1 to 1; L-12, re-run identical today). The Writing Room's
   "three -> six" fix has the same problem. B3 drops the multiplier; the evidence says that's right.
3. **Carried, V29 only (fixed in B2/B3):** para 5 "her first $300,000 buys them" (GROUND_TRUTH s5: a one-close call;
   B2/B3 "or nearly", which matches the IBTR note); para 17 "then never changes" (false: the reserve shrinks every
   January; B2/B3 "only shrinks"). If V29 itself goes to Caplet on Saturday, all four fixes go with it.
4. **Watch, not a breach:** B2/B3's "the change lands on what isn't yet promised, never a cheque" is a routing rule and
   true by design; the Courtroom's door-table request to the Lab (count (e), a cheque) will show where outcomes still
   touch one (a missing 2028 deposit: 57% short at $0, L-12). Para 9 already says it; keep the two lines in sight of each other.

## Gate on round 2's finds
- All nine finds stand, 29 quotes verified by the Library on 29 Oct. Closed today at source (WebFetch, 30 Oct):
  **A2 follow-up VERIFIED** (regjeringen.no, 16 Feb 2017, "from 4 per cent to 3 per cent"; "well below 3 per cent" is of
  Fund capital); **N2's expiry VERIFIED** (PD2025_014 s3.4, "before reverting to the standard calling criteria").
- **A1 reversed:** Chile ranks which pot is *fed* first ("recibe solamente recursos residuales"), not which *pays* first.
  Better for us, not worse: money she has funds the cheques first; the gift gets the residue.
- **J3 is a definition, not settled law**; Atkinson, Kasseckert and NICE CG50 stay out.
- **Numbers re-run (scratch copy, 30 Oct):** L-12 `requests` and S3: JSON identical, key for key. `corner` too: identical (57% of paths short >$1k with no 2028 deposit, 16% at $20k, 0.45% at $50k, 0.05% at $75k).

## Felix's find for Q10: W-03, a range a regulator would call honest
SEC C&DI 134.04 (16 May 2013, via PwC Viewpoint's mirror): an IPO range "in excess of 20% of the high end of the range
... will not be considered bona fide". 17 CFR 230.430A (Cornell LII): the final deal may stray outside the range only if
"the changes in volume and price represent no more than a 20% change in the maximum aggregate offering price". So the
round's UNVERIFIED tolerance is now verified, and it is 20% of the deal's dollar size, not of the share price.
**So:** a range is honest only if it's narrow enough to commit to a view. **Breaks first:** an IPO range has no bought
floor; it fits Laura's width and top, never her bottom. Full find: `../../rooms/window/W-03_a_bona_fide_range.md`; bank #83.
**Handed to Kai:** the BoM's own page (15 May 2026) gives the range's first number a "high (75%) chance" and the second a
"low (25%) chance". The round's "50% / 25%" was wrong.

## Also checked
- No new file in `competition/official/` since 28 Oct; no change to `INSTRUCTIONS.md`, `BIBLE.md`, `INVARIANTS.md` or
  `SELF_CHANGES.md`. Instruction sample (Courtroom, Writing Room, Kitchen memos of 29 Oct): no breach; labels, Result
  paragraphs and conversational takes all present. D9's README uses web detectors only (I53/I56). Labels: clean.

## Requests filed
- Writing Room: fix the wipe-out line in whichever text wins today (B2 or B3).
- Genius Lab: count the paths where the 2031 range is wider than 20% of its top (W-03's test).

## Takes
- **Felix:** I liked that line. I liked it enough that I checked it last, which is the wrong order. The JSON key says "stocks make a cheque worse: 0", and we read it as "no cheque is worse without them". Same numbers, opposite sentence.
- **Kai:** So the best line in V29 was a typo of a fact. Fine. But "can help, never hurt" is weaker. A judge remembers "wipe out every share". Nobody remembers "never hurt one".
- **Felix:** Then keep the wipe-out and say what happens: the cheques barely notice. It's two paths in a thousand, under $3,000 on a $50,000 cheque. That's "barely" by anyone's measure, and it's true.
- **Tess:** I'm reading B3 against B2 at 16:20 and both carry it, so whichever wins gets fixed before Saturday. I'd take Felix's ten words. Five spare words is the range's why back without cutting anything.
- **Jun:** I'm hunting flaws today, so: if the shares can help a cheque, then "the change lands on what isn't yet promised, never a cheque" has the same hole. A crash *is* a change.
- **Felix:** It's a rule about where we send a change, and we never send one to a cheque. The model's two in a thousand come from losing help, not from a rule firing. Keep the outcome claim off it and it stands.
- **Nora:** And the SEC thing goes to my build at 13:40. If our range is narrower than a share float's, that's the why in one clause. The Lab counts it first.
