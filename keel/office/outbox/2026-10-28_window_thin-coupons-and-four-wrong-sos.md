# The Window, Wed 28 Oct 2026: thin coupons, and four wrong "so"s

(Keel is a simulated team, AI-written.) Felix's gate for round 1 (`../../loop/rounds/2026-10-28.md` section 2).

**Result.** Yesterday's research quoted its sources well but drew four wrong conclusions from them, and two of those
were heading for the IPS; all are now marked in place. One new fact answers today's question in part: the
same Treasury maturity often exists twice, with a fat and a thin coupon, and buying the thin one on day one halves
that rung's coupon gap.

## Breaches and near-breaches (top)
| # | What | Rule | Status / fix |
|---|---|---|---|
| N1 | **D6 (V26) line 6:** "her first $300,000 buys them in January 2027" stated as fact. On the 22 Oct curve the headroom is $1,139 (payment-date basis) or -$224 (the model's own); the ladder costs over $300k in 46-47% of MODEL paths | `00_GROUND_TRUTH.md:88`: "$300,000 buys all ten" is a one-close call; echo only the IBTR note's conditional | Near-breach. Request to the Writing Room: join it to line 14 in one move ("...buys them in January 2027, and the 2028 deposit finishes any rung it can't reach") |
| N2 | **D6 line 11** names "Treasury bills" for the 2033 cushion | Only WInS-listed Treasuries may appear (Wharton email 27 Oct); bill listing UNVERIFIED (W1, open since 25 Oct) | Near-breach, carried. Keel's call of 25 Oct stands: generic words ("the shortest Treasuries") |
| N3 | `competition/official/2026_27/manifest.yaml` stopped parsing as YAML on 27 Oct (the new entry sat after `last_updated`) | Records integrity | Fixed on a separate branch for a human merge (outside `keel/`): PR #70 |

No breach of a hard limit. Labels: every 27 Oct memo carries the simulated label; D5a and D6 carry `AI DRAFT` in
their README. No self-change this week breaks `../../pm/INVARIANTS.md`.

## New official files since the last run (all filed 27 Oct; checked today)
- **Updated IPS instructions** (`UPDATED_2026_WGY_Investment_Policy_FINAL.pdf`): sha256 matches the manifest; pages
  1-2 word for word the v1 PDF (diffed); page 3 swaps the title page, Times 12 pt, double spacing, PDF and 5 MB rules
  for two form boxes. One line is gone: "Submissions that do not meet the requirements below will not be considered
  for semifinal selection." Nothing for Caplet to do but paste two boxes by **Sat 7 Nov 09:00** (Fri 6 Nov 5 pm ET).
- **Halfway email** (Book 6): "Individual TIPS" / "Individual STRIPS" replace Week 4's bare "TIPS" / "STRIPS" (diffed
  against `wharton_email_week4_2026-10.md:34-35`). Sydney times re-derived (US clocks go back 1 Nov): IPS Sat 7 Nov
  09:00, Final Report instructions Tue 10 Nov 01:00, Final Report Sat 5 Dec 09:00. All correct.
- **Deliverables page** (Book 8): the five criteria are word for word the 27 Sep copy; only "Sample Documentation"
  changed. **Caplet: request the school letter now** (Wharton: "Do not wait"), due Sat 5 Dec 09:00.

## Yesterday's finds (34 scout claims + every headline number in 27 Oct memos and room files)
Scout claims, read at source today (WebFetch; curl is blocked this session): **27 verified, 7 false or overstated**.
Numbers: L-10, LR-04, C-02 and R10 re-run identically; **5 mismatches**. Each is marked `[Window 28 Oct: ...]` where it sits.

The four that would have reached the IPS:
1. **The IRS trust test as our yardstick** (Library memo, R11, bank row 37). Parks, Finestone & Leahy (*Tax Notes*,
   2015) say low rates stopped new charitable trusts from *qualifying*, not that trusts ran dry when rates fell. And
   Rev. Proc. 2016-42's 5% is the chance an annuitant outlives the trust, a tax test, not our event. "Three to five
   times inside" compares unlike with unlike.
2. **Perry v. United States (1935) as "the Treasury cannot rewrite a bond".** Perry won the argument and got nothing:
   no proven loss, no remedy. The rewrite stood. S6 already has it right ("a right with no remedy").
3. **"If the 2028 deposit never came, the cheques are still covered: yes"** (S1). Our own models say no in 46-47%
   of paths; the 2028 money fills the ladder gap and backs the coupons.
4. **The re-match "shuts" the coupon gap.** R10 rule G still leaves a payment over $1k short in 1.05% of MODEL paths
   (1.6-1.75% when stocks and yields fall together); 0.01% needs the trap to reach into the bottom. D6's "soft spot"
   wording is honest; the synthesis's "measured and re-matched" must not harden into "solved".

Smaller: LR-04's "30 times safer" is 67x; its 2.3 sits *below* R05's lab run (2.69-3.30), not inside a 1.9-2.7
estimate; Model Suite M1b's "$8,400 above the bottom" isn't in the results file; M3's "~56%" break covers only the
January gap (K07: ~$85k of the deposit is needed, so nearer 43%); five engines give five "payment short" rates for V25
(2.05% to 10.6%): name the engine with any one of them. Episode 32 is right: $3,200 is L-10's median shortfall when
short, not a worst case.

## Felix's find: the thin-coupon twin (`../../rooms/window/W-01_low_coupon_rungs.md`)
TreasuryDirect's auction results show 20-year bonds sold in 2021 at **1-7/8% (Feb 2041)** and **2% (Nov 2041)**,
and a **1.375% Nov 2040** sold in 2020 (secondary source). The WInS book holds the old 30-year **4.25% Nov-2040** and
**3.125% Nov-2041**. Same date, same yield, same cost; the thin one sends far less money home early. If coupons earn
2 points less for good (MODEL): the 2041 rung is short $3,144 with the fat bond, $1,482 with the thin one; the 2042
rung $3,019 vs $2,270. A cure bought on its birthday, which is today's question, but only half a cure, and only if
WInS lists the thin issues. Keel's call: Final Report, not IPS, and no trade.

## Takes
- **Felix:** I keep finding the same thing: perfect quotes, wrong "so". The trust paper is the cleanest example. We
  read "trusts failed when rates fell" because it was the sentence we wanted, and the paper was about paperwork. The
  bond twin is the opposite case: dull source, an auction table, and the "so" is just arithmetic. I trust that kind more.
- **Kai:** Fine, but don't undersell your own find, Felix. "We bought the thin coupon on purpose" is the kind of
  sentence a portfolio manager nods at, because it shows we know where the money actually comes from. My worry is
  the other way: if WInS doesn't list it, we've found a cure we can't take, and a judge will ask why we bothered.
- **Felix:** Then it goes in the Final Report as "the cheaper cure we priced and couldn't buy on this shelf", which
  is honest and still shows the thinking. What I won't let through is the IRS line. It sounded clever, and it was wrong.
