# The Window, Thu 29 Oct 2026: the buffer table, and two more wrong "so"s

(Keel is a simulated team, AI-written.) Felix's gate for round 2 (`../../loop/rounds/2026-10-29.md` section 2).

**Result.** All twelve sources behind yesterday's research say what the team quoted, and every model number re-ran
to the dollar; two conclusions drawn from them went too far and are now marked. For today's question (what's our
decision-making framework?), bank regulators already have one: a table, written in advance, that cuts payouts in
steps as the cushion thins, protects depositors, and bans arguing that a recovery is coming.

## Breaches and near-breaches (top)
| # | What | Rule | Status / fix |
|---|---|---|---|
| N1 | **V28 (D8) para 3 still says "So her first $300,000 buys them in January 2027"** as fact. The Writing Room's word-neutral fix (join it to the 2028 top-up) is written in its 28 Oct inbox page but **not in `drafts/D8/ips.txt`**, while REQUESTS row 40 says "done on V28" | `00_GROUND_TRUTH.md:88`: a one-close call (headroom $1,139 on 22 Oct, payment-date basis, MODEL; over $300k in 46-47% of MODEL paths) | Near-breach, carried. Request to the Writing Room: Saturday's review draft carries the fix |
| N2 | **Instruction I53 (Book 9, "big picture, not minutiae"), breach 1:** round 1 spent beats 5-9 and four model scripts on the date of a ~$7,500 cushion (the Rooftop said so itself) | `../../INSTRUCTIONS.md` I53 | Logged in I53's row. LS-10 already caps a paragraph at two beats; today's round obeys it. A second breach rewrites the runbook rule the same day |
| N3 | Labels: the blind panel's three simulated judges (`ips_rewrite/reviews/panel_V27/judge*_scores.md`) had no simulated label | INVARIANTS s2: simulated people are tests, never quotes | Fixed: `panel_V27/LABEL.md` |

No breach of a hard limit. No new file in `competition/official/` since 28 Oct. No new entry in `../../pm/SELF_CHANGES.md`.
PR #70 (manifest YAML, human merge) still open. The Trading Desk's 28 Oct check stands (no curve after 22 Oct in the repo).

## The gate (round 1's finds)
Twelve quotes checked at the page (WebFetch, 29 Oct; curl blocked): Cornell LII §130, Oregon OAR 177-098-0060,
TreasuryDirect STRIPS, Cal. PCC §22300, ConsensusDocs (Santomartino, 3 Nov 2023), FAR 52.216-4, ETC Eos (cues; block),
CCSU handbook p. 20, USU handbook, RBA Bulletin Dec 2017 (Carter and Cole), IRS Rev. Proc. 2016-42. **All verified.**
- **K1, overstated.** §130(d) obliges no one; it lets an insurer's annuity or a US obligation count for a tax
  exclusion if bought within 60 days of the assignment. "US law wants the Treasuries bought within 60 days" is wrong.
- **F3, false premise.** FAR 52.216-4 caps price increases at 10% and leaves decreases uncapped: lopsided in the
  buyer's favour, not "symmetrical on paper". (It's a better point the right way round: the buyer caps what it can't fix.)
- K2 is implied, not stated; F1's release is on "satisfactory completion".
- **Numbers re-run** (A19, LR8, L-11 in S0/S1/S6; LR-05 S0; scratch copies, repo untouched): every JSON identical to
  the committed one. Two labels corrected in place: A19's "helped >$1k" counts were >$1 (only 70-82 paths >$1k); LR8's
  "$145k median bottom" is S0/S1 only (S6: $130k).

## Felix's find: the buffer table (`../../rooms/window/W-02_the_buffer_table.md`)
Basel Framework RBC30 (effective 1 Jan 2027, bis.org): as a bank's spare capital falls through four bands, it must
keep 40%, 60%, 80%, then 100% of its earnings; the bands are "recalculated at each distribution date"; dividends,
buybacks and bonuses are cut, depositors never; and "It is not acceptable for banks which have depleted their capital
buffers to use future predictions of recovery as justification for maintaining generous distributions" (RBC30.23).
RBC30.3 adds that the buffer must not become "a new minimum": it's meant to be used.
For Laura: cheques = depositors; the unnamed gift (2028-31) and her half = payouts; each January = a check date; the
2031 bottom = what she owns, never a forecast. V28's "cheques first; floor and stocks shrink together" has the order;
the table adds the *when* and the ban. **Breaks first:** banks refill from earnings, Laura can't after 2028; a named
gift is a promise, so the table governs only the hope years. Idea bank #69; rewrite note `../../ips_rewrite/inbox/2026-10-29_window.md`.

## Requests
- Closed: Laura's Room (LR-05 table and RBA quote: all match); Genius Lab (L-11 numbers match; the coupon money's
  listed home is IBTM, the first cheque's fund; SHY/SHV/BIL are 2025-26 list only, UNVERIFIED this year).
- Filed: Genius Lab (pair W-02 with today's scouts for C13); Writing Room (N1 in Saturday's draft).

## Takes
- **Felix:** Twelve for twelve on quotes, again, and two wrong conclusions, again. The pattern's stable now: we don't
  misquote, we over-read. The Basel find I'd trust more than anything this week, because the regulator wrote the
  "so" for us: don't pay out on a forecast.
- **Kai:** Trust it less, then. A bank has a supervisor breathing down its neck and earnings to refill the buffer.
  Laura has neither. A judge who's worked in a bank will love the shape and then ask who enforces the table when
  Laura wants to be generous in 2031.
- **Nora:** That's my ICU chart from the other side, Kai. Nobody enforces a NEWS score either; the point is the
  response is agreed before the patient crashes, so the argument never happens at the bedside. Felix's table and my
  chart are the same answer from two fields, which is either a good sign or groupthink. I'll know at 12:10.
- **Kai:** Groupthink until the Lab breaks it. If two bands do nothing a one-liner doesn't, it's a reference for the
  Final Report, not a framework.
- **Felix:** Agreed, and that's the request I've filed. One thing I won't concede: the $300,000 line. It's been "done"
  on paper for a day and it's still in the draft. That's the one Saturday can't miss.
