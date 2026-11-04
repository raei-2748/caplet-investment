# FICTION. Kai's round 3 check notes (H-027, Tue 3 Nov 2026)

(Keel is a simulated team, AI-written.) Repo files only, read 3 Nov 2026; no web pages. Paths from the repo root.
Line numbers are the file's own (`awk 'NR>=a && NR<=b'`). No model numbers here are meant for the IPS.

## (a) F20: still open? No. Closed 3 Nov.
- `keel/loop/FRONTIER.md` line 53 (F20 row, read to the end): "... F20 closes when the thread takes D; "no fourth flip"
  ... **Closed 3 Nov:** V54 took D (P2 "Crushing one means selling it before it matures, even for the building."),
  and C06 keeps it"
- `keel/huddles/2026-11-03_w5-on-trial/exhibits/C06_ruling_ips.txt` line 3: "Crushing one means selling it before it
  matures, even for the building." Line 19: "Do not crush."
- **Verdict on my round-2 claim:** WRONG. I gave Tess a scout job on a flaw that closed the same day.

## (b) F24, N1, A32, and what K01 actually says
- `keel/loop/FRONTIER.md` line 57 (F24): "open, FR first: two outside readers split, and Library N1 (3-0) kept the IPS
  free of a "scaled" bridge (case :129-130; Wharton: "Your WInS portfolio should reflect the strategy"). The reader's
  fix, "Our trades show this portfolio, scaled to $300,000." (+8), needs 8 words cut from C06 (497 strict). The FR's
  first Portfolio Analysis line says it in the Nov-2041 note's own words ("scaled to the model portfolio") (Archive A32)"
- `keel/loop/rounds/2026-11-02.md` line 135: "### Nora · adjacent · why the WInS book holds stocks"; lines 136-139:
  "N1. Wharton keeps the simulator apart from Laura's money and gives the implementation check to the Final Report.
  Case :129-130 ... updated IPS instructions :79-80 ... **So:** no "scaled" bridge in the IPS; P3 and the pitch carry
  dates. Upheld by Kai and Felix."
- `keel/pm/BOARD.md` line 68 (SD-N07, round 6): "scouts Tess (fund prospectuses), Nora (why the WInS book holds VT),
  Felix (the caplet at an Australian source)". So Nora already scouted this field on Mon 2 Nov.
- `keel/rooms/archive.md` line 101 (A32): "**WATCH 3 Nov** (readers split) | No "scaled" bridge in the IPS (Library N1,
  3-0 ...) ... Keel's call: the IPS stays as C06 ... the FR's first Portfolio Analysis line says the book is the plan
  after the 2028 deposit, scaled to $300,000, in the Nov-2041 note's words (F24)". Sources column cites the
  "Nov-2039 note "Laura's scaled 2040 payment"".
- `keel/ips_rewrite/inbox/2026-11-03_archive.md` lines 38-43: "Keel's call: no IPS words; the Final Report's first
  Portfolio Analysis line says it in the Nov-2041 note's own words ("scaled to the model portfolio")."
- `keel/pm/ASK_HUMANS.md` line 18 (Tue 3 Nov, the Archive): already asks Caplet the 8-words-or-FR question; "Keel's
  call: no IPS words for the scale ... Final Report"; due Wed 4 Nov 20:00.
- **K01, what it actually says.** `keel/pm/BOARD.md` lines 7-13 (this week's top 3, item 1, set 1 Nov): "Two fixes,
  from strategy logic only: the five fund rungs (IBTM-IBTR) pay their value at maturity ... and one clause on why the
  WInS book holds VT. Nothing new is promoted after Tue 3 Nov." Line 28 (the K01 row): "Final AI draft for Caplet: V50
  under Book 11; fund-rung wording; WInS clause". Done-when: "Final folder with a filled Ten Commandments + Book 11
  check by a reader who didn't write it, and a blind panel's disagreement report".
- **Verdict:** my quote was accurate but stale. K01's VT clause was written 1 Nov; N1 overruled it on 2 Nov, 3-0, and
  I was one of the three. Sending Nora to F24 against line 117 repeats her own round-6 job.

## (c) Does Wharton ask the IPS to explain the WInS book? No.
- `keel/WHARTON_WORD.md` line 117 (halfway email, "Tips for competition success"): "- Use WInS to demonstrate your
  strategy. Your WInS portfolio should reflect the strategy your team has developed." An instruction about the book.
- `keel/WHARTON_WORD.md` lines 78-79 (IPS instructions): "Focus on the strategy and decision-making framework that
  guide your portfolio rather than describing individual investments or presenting detailed financial calculations."
- `keel/WHARTON_WORD.md` lines 120-121 (same email): "Explain your decisions ... explain why each investment belongs
  in your strategy and how it supports Laura's goals." General advice across the deliverables; lines 78-79 say the
  IPS is not the place for individual investments.
- `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` lines 129-130: "The WInS portfolio represents each
  team's implementation of its investment strategy during the competition. / It does not determine Laura's actual
  portfolio value at the beginning of 2027."
- `competition/official/2026_27/UPDATED_2026_WGY_Investment_Policy_FINAL.txt` lines 79-80: "Your portfolio and Final
  Report should reflect the strategy established in your IPS. In the Final Report, your team / will evaluate how
  effectively it implemented that strategy ..."
- **Gap found:** that updated-instructions sentence (lines 79-80) is not in `keel/WHARTON_WORD.md` (grep for
  "implement" and "reflect" finds only lines 31, 35, 53, 117). A send-off can't quote it with a WHARTON_WORD line
  number (the brief's LS-14 form). Suggest the Library adds it verbatim (a file fix, no IPS words).
- **Verdict:** Wharton asks the book to reflect the strategy and gives the implementation check to the Final Report.
  It doesn't ask the IPS to explain the book. F24 is FR first.

## (d) An unchecked fact under F24? One, Final Report side, checked tonight in the repo
- `competition/wins/2026-10-23_snapshot.md` line 52: "| T-bond Nov-2039 | 10/6 11:45:04 PM | 282 | 10/6 8:02:40 PM (272
  chars, says "scaled 2040 payment") |" (the last column is "Earlier note on a cancelled order", line 46).
- `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md` line 18 (filled order, 11:45:04 PM):
  "... comes due 47 days before Laura's $50,000 payment on 1 Jan 2040." Line 40 (cancelled order, 08:02:40 PM): "...
  comes due 47 days before Laura's scaled 2040 payment."
- Same file line 24 (Nov-2041, filled): "With no iBonds Treasury funds maturing in 2037-43, the last five payments use
  individual Treasuries, scaled to the model portfolio, with reinvested coupons funding part of each." The scaling is
  said of the last five payments' Treasuries, not of VT or the IBTM floor.
- Already caught 16 Oct: `keel/library/assistant_review_2026-10/oct16/lenses/L08_coherence_numbers.md` line 171: "The
  cancelled Nov-2039 note said "scaled 2040 payment" (:40), but the filled version says "$50,000 payment" (:18)." Not
  carried into A32 (archive.md line 101) or bank #142 (`keel/ips_rewrite/IDEA_BANK.md` line 290), which both cite it.
- **So:** the FR line A32 plans should lean on the Nov-2041 note only, and say what it scales (the Treasuries). WInS
  still lists both notes (snapshot line 43), so a judge can see the cancelled one. A correction for the Archive, not a
  scout slot, and no IPS words.

## For the votes
- Amara's Nora job is not a copy: `keel/rooms/archive_checks/A33_lock_deletion_test.py` line 10: "Funds paid as par
  bonds, as in L-17 (the Courtroom's exhibit N is the funds-at-NAV view)." `keel/pm/REQUESTS.md` line 9: the Window's
  A33 gate re-runs it as built ("asserts KW equal to L-17"). Nobody runs the deletion test with the funds as funds.
- LS-16 vs LS-11 and LS-13 (`keel/loop/LESSONS.md` lines 21 and 23): LS-11 has a member read a blind winner against its
  own paragraphs and "list aloud what it deleted"; LS-13 writes a number's "design ... beside it (which plan, which
  engine)". Both write something down. A33 wrote its own gap in line 10 and its clean number still went to the
  Window's queue un-rerun. The new part is the re-run by someone who didn't build it.
- Roles: C06 = V54 + six W5 lines + the lock (brief; C06 file). Amara wrote in W5's room, Kai wrote the lock; Jun wrote
  neither. K01's "reader who didn't write it" (BOARD line 28) can't be Amara or Kai.
