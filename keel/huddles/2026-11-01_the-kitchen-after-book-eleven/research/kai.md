# Kai, round 1 research notes (H-014, Sun 1 Nov 2026)

(Keel is a simulated team, AI-written.) All pages below were read tonight through the WebFetch tool, which returns a
small model's summary of the page, so every quoted line is near-verbatim, not checked character by character (LS-09).
Anything marked UNVERIFIED was not read at a page. curl and fetch_text.py were not used.

## 1. The door: NSW cooling-off period (Kai's Sunday, Mum the agent)
- URL: https://www.nsw.gov.au/housing-and-construction/buying-and-selling-property/buying-property-nsw/contracts-and-deposits
  (redirected from the Fair Trading address). Read Sun 1 Nov 2026. Page metadata: modified 22 September 2025.
- Says: "When you buy a residential property in NSW, you have a 5 business day cooling-off period after you exchange
  contracts." It ends "at 5pm on the fifth business day after the day of exchange". To withdraw, "you will have to pay the
  vendor 0.25% of the purchase price." "A cooling-off period does not apply if you buy a property at auction."
- Means: backing out of a signed promise has a posted price, and an auction hammer has none. WHY auctions are exempt was
  not on the page: UNVERIFIED. The dinner-table call is Kai's fiction; only the rule is real.
- Possible field later: contract law / real-estate sales (TERRITORY already lists "Contract law: liquidated damages" as
  unvisited). No new field under the 0:3 dial.

## 2. IBTM summary prospectus: the fund's end is not a fixed amount (supports V50 open items 2, 3, F15)
- URL: https://www.ishares.com/us/literature/summary-prospectus/sp-ibonds-dec-2032-term-treasury-etf-10-31.pdf
  Read Sun 1 Nov 2026. Document date: February 27, 2026.
- Says: "By December 15, 2032, the Fund is expected to consist almost entirely of cash. On or around this date, the Fund
  will wind up and terminate." "After appropriate provision is made for any Fund liabilities, its net assets will be
  distributed to then-current shareholders pursuant to a plan of liquidation." "The Fund does not seek to return any
  predetermined amount at maturity or in periodic distributions."
- The fetch found no sentence saying "may differ from par" in the summary prospectus; the "predetermined amount" line is
  the closest. Only IBTM was read. IBTO, IBTP, IBTQ and IBTR are Tess's job (the same sentence should be in each; not read).
- Means: the five iBond rungs pay "net assets", which agrees with the submitted IBTM note ("final payout is not fixed").
  V50 para 3's "A Treasury held to maturity pays exactly what it promises" is true of a Treasury, and the funds sit beside it.
- Repo cross-check: `competition/wins/2026-10-23_snapshot.md`, "Pays for" column: IBTM 2033, IBTO 2034, IBTP 2035,
  IBTQ 2036, IBTR 2037 (funds); the five T-bonds (Feb-2037 to Nov-2041) pay 2038 to 2042. Funds are 61.5% of the
  portfolio value on that snapshot (IBTM 32.5% + other iBonds 29.0%). Note: `CAST.md`'s "Current state" (23 Oct, older)
  lists four iBonds and six Treasuries; the snapshot is the official WInS view and shows five and five.

## 3. Pharmacology: what the "do not crush" label really says (V50 open item 7, the circle)
- ISMP Canada, "Some Medicines Should Not Be Crushed, Split, or Chewed!", https://safemedicationuse.ca/newsletter/newsletter_NotBeCrushedSplitChewed.html
  Read Sun 1 Nov 2026 (second read, for the capsule lines). Page date: 2013-07-09.
  - "If a slow-release tablet is crushed, split, or chewed, a large amount of the medicine may be released all at once."
    "This could cause serious harm."
  - The only capsule sentence: "Always check with your pharmacist before crushing, splitting, or chewing any tablet or
    capsule or before opening any capsule." The page does not mention sprinkling or beads. Its "swallowed whole" sentence
    is about tablets: "Slow-release tablets are generally intended to be swallowed whole."
  - Means: the page's "all at once" reason is about a TABLET. V50 para 2 says a CAPSULE is "labelled do not crush" and "Break
    it open and you ruin how it works". The page does not say that of a capsule. That is a small overclaim in the motif.
- WA Health, "Don't rush to crush" (PDF, code "OSQ-012777 SEP'14", so a September 2014 edition; no author named on the
  page), https://www.health.wa.gov.au/~/media/Files/Corporate/general-documents/safety/PDF/Medication-safety-resources/Dont-rush-to-crush.pdf
  Read Sun 1 Nov 2026. Says: "Slow release medicines must never be crushed." "Crushing can increase the risk of drug
  toxicity." No "dose dumping" or "all at once" on that page.
- NPS MedicineWise, Australian Prescriber note on the first edition of the *Don't rush to crush* handbook (SHPA, Collingwood,
  Victoria, 2011, 647 pages), https://www.nps.org.au/australian-prescriber/articles/australian-dont-rush-to-crush-handbook-1st-edition
  Read Sun 1 Nov 2026. The text fetched gave no reason for not crushing; only that the handbook has a section on medicines
  that should not be crushed. The handbook itself was not read: UNVERIFIED what it says about capsules.
- Means for Felix tomorrow: find the Australian handbook's (SHPA, *Don't rush to crush*) own words on capsules, so the
  motif's setup can say the true reason (the dose arrives all at once) about the right object, or stay silent where the
  source is silent.

## 4. Repo checks behind the post (all read tonight)
- `keel/ips_rewrite/THINKING_LOG.md` line 488: "L1 is the best single sentence on offer: for the cheques we don't
  diversify, on purpose, because a chain of ten is only as certain as its links are correlated." The idea predates V50;
  the rebuild dropped it (V50 has no diversification sentence).
- `keel/WHARTON_WORD.md` s1 ("uses appropriate diversification") and s2 (the IPS "does not need" final calculations,
  projections, a final range or the co-sponsor draft; "sources do not need to be cited in the IPS").
- `keel/loop/FRONTIER.md` s4, Round 5 send-off (every number kept with its source) against `keel/WHARTON_WORD.md` s2.

## 5. Round 2 checks (repo only, no new web pages; Sun 1 Nov 2026)
- What Monday already has queued: `keel/pm/REQUESTS.md` rows 9-13 (Window 08:40 gates the A19 cure with A5 and A16, and the
  Courtroom's "Crushing one means ..." repair; Writing Room 16:20 cold-reads the Archive's 495 copy, incl. "ten holdings", and
  writes the no-number diversification sentence from ledger B6: "every cheque sits on the one borrower whose promise is the
  point; the spreading happens in the stocks"). The motif's real mechanism, pre-mortem 16 and pre-mortem 17 are queued nowhere.
- The floor is a fund in the frozen book: `competition/wins/2026-10-23_snapshot.md`, "Pays for" column, IBTM = "2033 payment +
  floor stand-in". So the fund question reaches V50 para 6 ("a commitment rather than a forecast"), not only para 3. Whether
  WInS lists an individual Treasury maturing in late 2032 (V50 para 5): UNVERIFIED (the IBTO and IBTQ notes say WInS has none
  for 2033 or 2035; nothing read says so for 2032).
- Submitted fund notes that say the payout is not fixed: IBTM, IBTO, IBTP, IBTQ
  (`caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md` lines 19-22). IBTR's filled note (line 15)
  says nothing of its payout and calls the whole ladder "Treasuries for all ten payments".
- Wharton's word s2: "Focus on the strategy and decision-making framework that guide your portfolio rather than describing
  individual investments or presenting detailed financial calculations." Means: the cheapest true fix for the fund rungs may be
  fewer instrument words (F1's 28 Oct "ten holdings"), not a sentence explaining funds.
- Jun's door against ledger B6 (`keel/ips_rewrite/IDEA_LEDGER.md` line 80): "ten separate 99% bets miss one about one decade
  in ten" is the same arithmetic as Jun's 1 - 0.99^10 = 9.6%. B6 is parked in the Final Report (cut from V31 for words, 30 Oct).
- Pre-mortem 16 and 17: `keel/pm/PREMORTEMS.md` lines 54-55. Public budgeting row: `keel/loop/TERRITORY.md` line 62 (Washington
  SSJR 8208, "stocks only for money without a deadline"; whether voters passed it UNVERIFIED, Amara's note).
