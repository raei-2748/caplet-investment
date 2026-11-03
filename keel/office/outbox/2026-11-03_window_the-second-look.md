# The Window, Tue 3 Nov 2026 (round 7 beat 2): the second look

(Keel is a simulated team, AI-written.) Felix's sweep, with Kai and Tess in huddle H-021
(`../../huddles/2026-11-03_the-second-look/`). For Nora's 07:00 brief and the rewrite thread.

**Result.** V54 has no false line, but it describes one check on the bond ladder's weak point (in 2031) where the
plan's numbers rely on two (2031 and January 2033). Measured fairly, with one check a cheque comes up a little short
in about 1 future in 25, and with two about 1 in 770 (MODEL), so the IPS should name the second check or use Kai's
simpler rule that needs none.

## Breaches and near-breaches
- **No breach.** No false fact in V54 or its pitch; no broken rule in yesterday's outputs.
- **Near-breach 1, V54 P8-P9, the second look** (`../../rooms/window/W-08_the_second_look.md`). The text prices the
  reinvestment gap once, "Before she names the range". The model also prices it again in January 2033 and tops the
  reserve up, her kept stocks first, then the gift. Fair test (W0f): 96.01% of futures pay every cheque in full with
  one look, 99.87% with two; 94.39% v 99.85% if yields fall 2 points for good; median short $1,341 (MODEL, 22 Oct
  curve, 7.5%, 200,000 paths). The Window's first test said 86.76%; Kai found a leak in it, and it is withdrawn.
  The hole is older than V54 (Tess): V29-V30 said "tops up once" and IDEA_LEDGER E2 sent it to the Final Report as
  "detail" at V31. **Keel's call:** reopen E2 and put the step in the IPS, by road A (name it in P9) or road B (Kai's
  lock, below). Offers and constraints: `../../ips_rewrite/inbox/2026-11-03_window.md` s1.
- **Near-breach 2, the pitch's "a promise".** Not false, but the word is ours: the case calls the cheques "the
  operating commitment" and says "promise" only of the range (:114-115). The Writing Room's stranger test keeps its
  job, re-aimed at the pitch beside P6's "every dollar she promises" (F21 is moot on P8: V54 says "gift").

## What was checked
1. **V54 and its pitch, line by line** (`../../ips_rewrite/inbox/2026-11-03_window.md` s2): no false line. P2's new
   "Crushing one means selling it before it matures, even for the building." is TRUE of all ten holdings. P3's
   "pays exactly what it promises" is TRUE in the SEC's own words. P6's "every dollar she promises is already in
   bonds" is true on naming day; the gift still lands under the named top in about 1 future in 50, never under the
   bottom (Final Report).
2. **Re-runs from a clean copy:** the Genius Lab's L-16 and Laura's Room's LR-10, S0 and S6: JSON identical. Every
   number the two requests quoted is confirmed; LR-10's H branch is right.
3. **Round 6's nine finds: 9 verified, 0 UNVERIFIED, 0 overstated, 0 false.** Five re-fetched today, ten quoted
   lines on five pages, all there (near-verbatim via the fetch tool): iShares' iBonds page, IBTM's prospectus, the
   Panadol Osteo leaflet, Australian Prescriber 2018;41:191-3, HMRC CFM13340. Three checked against the repo's own
   files (case :129-130, the updated IPS instructions :79-80, COMPETITION.md :117 and :225-226, the WInS snapshot);
   T3 rests on the Library's 2 Nov re-fetch. The "so" lines hold; HMRC's floor is an option bought "in return for a
   premium", which is why Felix's F3 says Laura holds none. Kai's two CME lines for Laura's Room are there too, both
   conditional.
4. **Five requests to the Window closed**, plus the Window's own 26 Oct re-pricing request: the newest close on file,
   **23 Oct, prices the ten cheques at $297,636, $2,364 under $300,000 (8 bp)**, `../../scripts/ladder_pv.py`.
5. **Official files:** nothing new in `competition/official/` since 27 Oct. One data file arrived in
   `competition/official_market_data/` (`daily-treasury-rates_2026-10-23.csv`, treasury.gov par curve to 23 Oct, filed
   25 Oct and merged into main on 2 Nov); that folder's README doesn't list it yet. Nothing for Caplet to do.
6. **Labels:** D33 and D34 had no label for their paste-clean .txt files; added. Panel V54's judges are labelled
   through the judges README. No new self-change to check against INVARIANTS.
7. **Felix's own find, W-08b:** SEC Pub. No. 151 says a bond held to the end pays "the stated interest rate, as well
   as the face value of the bond". That two-part payment is the step a stranger needs before P8's "costs less than
   the cheques because its bonds pay interest along the way" makes sense.

## The takes
- **Felix:** I posted 86.76% this morning and I was proud of it, because it looked like Monday's cushion all over again.
  The text checks once, the model checks twice. That much is still true. What I got wrong was my own test.
- **Kai:** Felix, mate, your W0 cut Laura's range to pay the gap and then handed the money straight back to her, so of
  course the cheques bounced. That's not V54, that's a leaky bucket. You're dead right that it only looks once,
  though. And who says we need a second look at all? Price the gap as if the interest stops on naming day and buy a
  bit more of the rungs. My nan would sign off on that one.
- **Tess:** Felix, your gap is real; I re-read the JSON to be sure. But it isn't the cut's gap. The order line was a
  priority, never a second look, and the ledger sent the top-up to the Final Report at V31 before anyone had priced it.
  Reopen E2 rather than call it a restoration. And your "a promise in plain English" was taste: the case says
  "commitment".
- **Felix:** Both of you, fair. W0f, scored Kai's way, says 1 in 25 against 1 in 770: smaller than I said, and
  still not what "a high degree of certainty" should mean when a few words of text fix it. My STRIPS reason is gone too.
  Kai's lock goes to the Lab at 13:40, because a rule a judge can check in one line ("as if the interest earned
  nothing") beats a cushion nobody can see the size of.
