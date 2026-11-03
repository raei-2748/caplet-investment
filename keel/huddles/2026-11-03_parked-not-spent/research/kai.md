# Kai's sources (H-024, round 1, Tue 3 Nov 2026)

(Keel is a simulated team, AI-written.) Real sources, read 3 Nov 2026 (Sydney). Question: how the people who size
public escrows word the zero-reinvestment assumption, what happens to money the payments didn't need, and what they
would ask of V54's P8 and P9.

**How these were read.** The fetch script (`keel/library/insight_v1/scripts/fetch_text.py`) was refused by the proxy
(HTTP 403, policy denial) for every host tried: mwra.com, mendocino.edu, admin.smc.edu, naplesgov.com, msrb.org,
emma.msrb.org, gfoa.org, nabl.org, sec.gov, home.treasury.gov, treasurydirect.gov, fiscal.treasury.gov, spglobal.com,
moodys.com, fitchratings.com, soa.org, actuary.org, ecfr.gov, govinfo.gov. Not retried. The pages below were read
through the WebFetch tool instead (as the Lab chair did today), which quotes through a summariser in pieces of at most
125 characters. So every quote is **near-verbatim**: check the wording at the source before the Final Report prints
it. Wisconsin s4.1(b) was read twice and confirmed word for word in order.

## S1. MWRA 2025-2 Defeasance Escrow Agreement
- **Publisher / parties:** Massachusetts Water Resources Authority and U.S. Bank Trust Company, National Association
  (as successor Trustee). **Dated** as of 22 Dec 2025.
- **URL:** https://www.mwra.com/media/file/2025-2-defeasance-escrow-agreement. **Read** 3 Nov 2026 (WebFetch).
- **s3 (sizing):** the investments "mature and bear interest payable in such amounts and at such times as will be
  sufficient, without reinvestment," together with "any uninvested moneys remaining in the Defeasance Escrow Fund
  after the purchase of the Defeasance Obligations," "to pay when due the principal of and interest due and to become
  due on the Defeased Bonds." (Confirms the Lab chair's E1.)
- **s5 (reinvesting allowed, capped):** receipts "shall be reinvested in Defeasance Obligations at a yield not to
  exceed the yield on the Defeased Bonds" unless bond counsel advises "that a higher yield is permitted".
- **s7 (surplus at the end):** "Any amounts held by the Trustee on the termination of this Agreement" (not needed for
  fees) "shall be paid promptly over to the Authority upon its written request." Termination: when the bonds' principal
  and interest "shall have been paid or set aside for payment".
- **s10 (surplus early):** "the Authority may request that such moneys be paid into the Revenue Fund", but first "the
  Authority shall certify to the Trustee, based solely upon a mathematical verification report" that "the amounts of
  moneys and investments remaining in the Defeasance Escrow Fund after such payment" will "mature and will earn interest
  in such amounts and at such times so that sufficient moneys will be available". s10 itself does not repeat "without
  reinvestment"; that phrase is in s3.
- **What it means for us:** size at zero, reinvest if you like, and money comes back to the owner either at the end or
  earlier only after the sum is redone for what is left. Reinvesting is allowed; counting on it is not.

## S2. Mendocino-Lake Community College District, Escrow Agreement (2022 GO refunding bonds)
- **Parties:** the District and The Bank of New York Mellon Trust Company, N.A., as Escrow Agent. **Dated** as of
  1 Mar 2022.
- **URL:** https://mendocino.edu/sites/default/files/documents/2022_go_refunding_bonds_escrow_agreement.pdf. **Read**
  3 Nov 2026 (WebFetch; the fetch script got 403).
- **s5(iii) (condition for reinvesting idle cash):** the new investments must "be sufficient without reinvestment to
  pay, when due, the principal, Accreted Value, or redemption price" of and interest on the Refunded Bonds. **s8(iv)**
  (condition for swapping securities) uses the same words, with an independent CPA's certification.
- **s3(b) (surplus):** "Any moneys remaining in the Escrow Fund established hereunder after August 1, 2026" "which are
  in excess of the amount needed to pay owners of the Refunded Bonds" "shall be immediately transferred by the Escrow
  Agent to Mendocino County, on behalf of the District". **s8:** money freed by a swap and not needed for the payments
  "shall be paid to the District as received by the Escrow Agent free and clear of any trust, lien".
- **What it means for us:** a second, unrelated issuer and agent use the same words, "sufficient without
  reinvestment". The Lab chair's caution ("one agreement, one issuer") can be eased to "the public escrows we read".

## S3. State of Wisconsin, Event Filing #2021-19 (notice of defeasance), with its Refunding Escrow Agreement and Verification Report
- **Publisher:** State of Wisconsin, Department of Administration (capital finance disclosure filings). **Dated**
  23 Sep 2021. Contains: Refunding Escrow Agreement (State of Wisconsin Building Commission and The Bank of New York
  Mellon Trust Company, N.A., 23 Sep 2021) and a Verification Report by Samuel Klein and Company, Certified Public
  Accountants (23 Sep 2021).
- **URL:** https://doa.wi.gov/DEBFCapitalFinance/2021/EF2021_19_GO_Refunding_2021_4.pdf. **Read** 3 Nov 2026 (WebFetch,
  three passes).
- **Agreement s1.2:** the deposit "will be sufficient to make all payments of the Redemption Price of, and interest on,
  the Refunded Bonds".
- **Agreement s4.1:** escrow money "may be invested, reinvested, or disbursed in any manner directed in writing by the
  State", provided **(b)** an independent CPA opines that "the amounts available or to be available for payment of the
  Refunded Bonds will remain sufficient after such action to pay when due without further reinvestment all Redemption
  Price of, and interest on, the Refunded Bonds up to and including their respective Redemption Dates" (confirmed in
  order, second pass), and (c) bond counsel's opinion.
- **Agreement s4.5:** "Upon final disbursement for the payment of the Refunded Bonds", "the Escrow Agent will transfer
  any balance (cash and securities) remaining in the Escrow Fund to the State".
- **Verification Report:** an "independent verification report addressing the arithmetical accuracy of computations";
  the receipts "will be sufficient to pay, when due, the interest and redemption requirements on the Refunded Bonds";
  "In our opinion, the computations contained in the schedules provided are mathematically correct."
- **Schedule C (UNVERIFIED in detail):** WebFetch's reading is that receipts are added to a running cash balance and paid
  out on each due date, with no earnings on the balance. That is a summariser's description of a table, not a quote.
- **What it means for us:** this is the exact test for handing money back early: what remains must still pay every
  later payment "without further reinvestment". Applied to P9: not "whatever each rung didn't need" but what no
  *remaining* cheque needs, counted at zero.

## S4. Minnesota Statutes, section 475.67 (Refunding bonds), subd. 6 and 9
- **Publisher:** Minnesota Office of the Revisor of Statutes. **Version** 2025.
- **URL:** https://www.revisor.mn.gov/statutes/2025/2025-10-19%2013:59:46+00:00/cite/475.67/pdf. **Read** 3 Nov 2026
  (WebFetch).
- **Subd. 6:** escrow funds "shall be invested in securities maturing or callable at the option of the holder on such
  dates" as will "provide funds sufficient, with any cash retained in the escrow account, to pay when due the
  interest" and principal; the governing body "shall irrevocably appropriate for these purposes the escrow account";
  "any funds in the escrow account in excess of the amounts from time to time needed for the foregoing purposes may be
  remitted to the municipality."
- **Subd. 9:** "The agent may be directed to reinvest the balance held in the account from time to time."
- **What it means for us:** a statute, not a contract, with the same shape: irrevocable for the payments, surplus back
  to the owner "from time to time" once it is more than what is still needed. The statute itself does not say
  "without reinvestment".

## S5. Santa Monica Community College District, Escrow Deposit Agreement
- **Parties:** U.S. Bank National Association (Escrow Agent) and the District. **Dated** as of 1 Apr 2018.
- **URL:** https://admin.smc.edu/administration/governance/board-of-trustees/documents/2018/8-escrow-agreement.pdf.
  **Read** 3 Nov 2026 (WebFetch).
- **s2.6(a):** "Except as otherwise expressly provided in Sections 2.1 and 2.3, the Escrow Agent shall have no power or
  duty to invest any moneys held hereunder" or "to make substitutions of the Escrowed Securities held hereunder".
- **s3.1:** "any moneys remaining in the Escrow Fund following such payment in whole on the redemption date shown on
  Schedule B" "shall, after payment of any amounts due the Escrow Agent, be transferred to the District."
- **No "without reinvestment" wording** in this one; s2.3 counts the securities "together with any uninvested cash on
  deposit therein" as "sufficient for such purposes".
- **What it means for us:** here the cash literally sits idle; the agent may not invest it. So J's picture ("sat idle")
  is true to practice. Kai still backs A for the word, not the picture.

## Context (secondary, a professional body's glossary)
- NABL (National Association of Bond Lawyers), *Verification Report* (last modified 2 Mar 2023),
  https://www.nabl.org/bond-basics/verification-report/, read 3 Nov 2026 (WebFetch): "A document provided by the
  Verification Agent, which verifies the mathematical accuracy of the Cash Flows" "for repayment of the Refunded
  Bonds". Says nothing on reinvestment.
- NABL, *Defeasance* (last modified 3 Apr 2023), https://www.nabl.org/bond-basics/defeasance/, read 3 Nov 2026
  (WebFetch): "sufficient funds or investments to guarantee timely payment of Principal and Interest"; "verification of
  the sufficiency of the amounts deposited into the Escrow Fund is required"; escrow investments are "usually
  obligations of the federal government or, sometimes, federal agencies, or both"; once defeased, bonds are "generally
  considered no longer outstanding from the Issuer's perspective."

## Not read / UNVERIFIED
- **Rating-agency criteria** (S&P, Moody's, Fitch) on defeased or escrowed bonds: not found in open pages; hosts refused
  the fetch script. Any claim that agencies "require zero reinvestment" is UNVERIFIED.
- **MSRB/EMMA and GFOA pages:** not read (403 on the fetch script; not tried through WebFetch).
- **California Debt Financing Guide 9.2.5 "Refunding Escrow Funds"** (CDIAC),
  https://debtguide-api.treasurer.ca.gov/guide-pages/chapter-9-investment-of-bond-funds/9-2-types-of-funds-available-for-investment/9-2-5-refunding-escrow-funds:
  only navigation loaded, no body text. Not used.
- **Pension and structured-settlement actuaries:** not read today.
- **Treasury's zero-percent SLGS** (31 CFR 344): not read (the Lab chair's attempt failed too).

## What a practitioner would ask of V54
1. **P8, "at that day's yields, plus a cushion":** why forecast at all? Every escrow above is sized so it pays without
   reinvestment; zero needs no yield guess and no cushion. Kai's lock (C1) is that rule.
2. **J vs A:** the field's word is "without reinvestment". A ("as if nothing more is reinvested") says it and reuses
   P8's own "reinvest". J ("as if money paid later sat idle") is true to practice (S5) but "money paid later" is
   unclear: paid by whom, to whom? A reader can take it for the cheques.
3. **P9:** where does the surplus go, when, and on what test? Every escrow says: to the owner after the last payment,
   or earlier only if what stays is still sufficient "without further reinvestment" (S3 s4.1(b); S1 s10; S4 subd. 6).
   The chair's add-on tests the wrong thing ("whatever each rung didn't need"). Kai's wording, same ten words: "and
   handing back to Laura what no remaining cheque needs." Cuts offered: A (-1); P8 "that interest earns less, and"
   (-5); P9 "the money set aside for its gap" -> "its gap money" (-4). Plain counts by Kai; the chair runs
   `textcheck.py` for the strict count.
4. **C1's "never look again":** escrows are irrevocable for the payments but do look again, only to release surplus
   after a fresh sum. Lab design note, not IPS wording.
5. **Where each piece lands (Book 11):** the rule goes into the IPS uncited; the escrow sources, the verification idea
   ("a sum anyone can redo") and the cash-flow table (C4) go to the Final Report.
