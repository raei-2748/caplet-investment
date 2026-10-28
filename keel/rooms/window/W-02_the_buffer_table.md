# W-02. The buffer table: how bank regulators write "as needs change" in advance

(Keel is a simulated team, AI-written.) Felix's primary-source find for round 2 (Q8, the framework), Thu 29 Oct 2026.
Not for submission as written; IPS ideas go through `../../ips_rewrite/inbox/2026-10-29_window.md`.

## Source (primary, official)
Basel Committee on Banking Supervision, *The Basel Framework*, chapter **RBC30 "Buffers above the regulatory
minimum"**, version effective 1 Jan 2027 (technical amendments of Nov 2023), bis.org,
https://www.bis.org/committees/bcbs/basel-framework/81587/chapter.pdf, accessed Thu 29 Oct 2026 (WebFetch; curl is
blocked this session, so "verified" = the words found in the fetched text). Quotes, word for word:

- RBC30.1: the buffer exists to "ensure that banks build up capital buffers outside periods of stress which can be
  drawn down as losses are incurred".
- RBC30.3: "The distribution constraints imposed on banks when their capital levels fall into the range increase as
  the banks' capital levels approach the minimum requirements." ... "The Basel Committee does not wish to impose
  constraints for entering the range that would be so restrictive as to result in the range being viewed as
  establishing a new minimum capital requirement."
- RBC30.4 (the table, Common Equity Tier 1 ratio -> share of earnings the bank must keep, not pay out):
  4.5-5.125% -> 100%; 5.125-5.75% -> 80%; 5.75-6.375% -> 60%; 6.375-7.0% -> 40%; above 7.0% -> 0%.
  "The applicable conservation standards must be recalculated at each distribution date."
- RBC30.5(1): "Items considered to be distributions include dividends and share buybacks" (also discretionary
  payments on other Tier 1 instruments and discretionary staff bonuses).
- RBC30.23: "It is not acceptable for banks which have depleted their capital buffers to use future predictions of
  recovery as justification for maintaining generous distributions to shareholders, other capital providers and
  employees. These stakeholders, rather than depositors, must bear the risk that recovery will not be forthcoming."

Not in the text, so not claimed: that the constraint is "automatic". RBC30 leaves supervisors some discretion (RBC30.5).

## Mechanism, in two sentences
A bank doesn't forecast its losses; it writes down, in advance, a table that says how much of its earnings it may
pay out at each level of spare capital, and re-reads the table on every payout date. As the cushion thins, the
discretionary payers (shareholders, bonus pools) are cut first and in steps, the depositors never, and nobody is
allowed to argue that a recovery is coming.

## Where it breaks for Laura (break first, LS-04)
1. **A bank refills from earnings; Laura can't.** After the 2028 deposit she has no new money before 2033 (case).
   The table's steps only make sense while there is something left to cut: her half of the stock fund and the
   unnamed part of the gift.
2. **After 2031 the gift isn't discretionary.** Once she names a range to co-sponsors it becomes a promise, the
   depositor's side of the line, so the table only governs the "hope" years (2028-2031) and her own half after that.
3. **Four steps is three too many for a 500-word IPS.** The shape (cut in steps, re-read on payout dates, senior
   claims never touched) is what transfers; the bands don't.
4. **Discretion.** Basel keeps a supervisor; Laura has no one but herself, so her table has to be simpler than a
   bank's to be self-enforcing.

## What it could touch
- **V28 para 10** ("If needs change, cheques first; floor and stocks shrink together"): this is already Basel's
  ordering (depositors first, distributions shrink), which means the line is right but unexplained. The framework
  Book 7 asks for is the table, not the ordering: *which* claim shrinks first, *when* the check happens (each
  January a cheque or deposit falls due: 2028, 2031, 2033-2042), and the ban on arguing recovery.
- **RBC30.23 is our 2031 rule in a regulator's words.** The 2031 bottom is "the floor she owns, rounded down" and
  never a forecast of the stock fund's recovery. Laura's Room's co-sponsor test ("would I book this bottom?") asks the
  same question a supervisor asks a bank that wants to keep paying dividends.
- **RBC30.3, the cushion is meant to be used.** The $7,500 the Long Room voted on 28 Oct is a buffer, not a second
  floor: drawing on it is the plan working, not the plan failing. That answers the Writing Room's "bends the rule" worry.
- **Book 7's own words.** "How your strategy will guide portfolio construction and investment decisions as the
  client's needs change" is, in banking, a capital plan with a distribution table. A judge from finance will know the
  shape on sight, and a Year 11 team that uses it without naming it shows north star 4 the way Book 9 asks.

## For the ninety-second judge (lens 13)
"When the cushion thins, the hope shrinks first, by a table written today, and nobody gets to argue a recovery."
Where it breaks: it needs a hope to shrink; once a promise is named, the table has nothing left to cut but Laura's own half.

## 2042 sentence
"Every January we read the table instead of the forecast; the year stocks halved, the hope shrank before anyone
named it, and no cheque noticed."

## Status
Quotes VERIFIED at source (29 Oct). The mapping is Keel's reasoning, not a source claim. Banked as idea bank row 69
(lands in Both: one clause of the IPS framework paragraph; the full table and the Basel reference in the Final Report).
