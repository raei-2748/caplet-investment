# The FAQ now bans "Individual" TIPS and STRIPS: what it changes for Caplet (nothing in the book; one question for Wharton)
AI-generated rules check by the Keel Office (Claude Code; Felix = Rules & Integrity). Not for submission. Cite in Works Cited.
Work order: SD-R11 | Asked by: self-directed (Long Room, Sat 24 Oct early run) | Desk: Rules & Integrity (rules-verifier role, no subagents) | Date: Sat 24 Oct 2026, 11:50 AEDT
Read only: repo copies. WInS, SMApply and the Caplet Google Docs were not opened.

## What changed
| Source | Wording on TIPS / STRIPS | File, line |
|---|---|---|
| Week 4 email (pasted 22 Oct), "the only permitted investments (for BOTH contributions, the IPS and Final Report)" | "TIPS (Treasury Inflation-Protected Securities)", "STRIPS (...)" | `competition/official/2026_27/wharton_email_week4_2026-10.md:34-35` |
| Public FAQ, 20 Oct copy | same as the email | `smapply_public_2026-10-20/faqs.txt` |
| Public FAQ, live 24 Oct (fetched 23 Oct 23:59 UTC) | "**Individual** TIPS (...)", "**Individual** STRIPS (...)" | `smapply_public_2026-10-24/faqs.txt:50-51` (PR #22 / #20) |
The permitted list did not change in substance: "Any stock / Any Exchange-Traded Fund (ETFs) / Any Government/Treasury
Bond available on WInS" (`faqs.txt:41-43`, now singular). "Anything other than the approved investments" stays banned (:52).

## Two readings
- **A (narrow).** "Individual" limits the ban to single TIPS and STRIPS securities. A TIPS fund or a STRIPS fund that
  WInS lists would then be "Any Exchange-Traded Fund ... available on WInS", so permitted.
- **B (strict).** The word is tidying, not a new rule. The email, sent to teams and still the newest instruction
  addressed to them, bans TIPS and STRIPS without the qualifier, for both contributions and both deliverables.
Neither page says which wins. **Ruling: follow B until Wharton answers in writing.** The strict reading never puts
Caplet in breach; reading A could, if Wharton meant B.

## Effect on Caplet
1. **The book: none.** WInS holds five iBonds Treasury ETFs (IBTM-IBTR), five nominal T-bonds (Feb-2037 to Nov-2041,
   fixed coupons) and VT (`competition/COMPETITION.md` s8; WInS snapshot 23 Oct). No TIPS, no STRIPS, no fund of either.
   That the iBonds Treasury funds hold no TIPS is UNVERIFIED this session (ishares.com refused, 403, 24 Oct 00:47 UTC);
   the Trading Desk checks the IBTM fact sheet when the network allows.
2. **The plan: none, and here is why it is not a loss.** Each payment "is a fixed $50,000 and is not adjusted for
   inflation" (case text, `Laura_Gao_2026_Client_Profile.txt:90`). A TIPS pays principal indexed to U.S. inflation, so it
   matches a bill that rises with U.S. prices, which hers does not. Inflation does reach the plan in one place: the case
   asks teams to state their assumption about "the effect of inflation on portfolio projections and facility costs"
   (:147), and the facility is in Taiwan, whose costs U.S. CPI would not track. In Caplet's plan that job belongs to the
   growth fund and the flexibility Laura keeps, not to the ladder, and the ban changes neither. (Plain-English "what this
   teaches": match the bond to the bill. A bill fixed in dollars wants a bond fixed in dollars; a cost that rises wants growth.)
3. **The words: one live risk.** Old internal files price the ladder on a "STRIPS basis" (e.g. the RAB brief text
   in `caplet/google_drive/sheets/portfolio_and_trading_notes/trading_notes.csv:5,401`; superseded STRIPS figures in
   `keel/library/insight_v1/`). Those are internal, but any figure a student copies from them must be called the
   "payment-date (zero-coupon) basis", never "STRIPS". The 5 Oct journal line "STRIPS in real life, IBTM as the WInS
   stand-in" (`caplet/google_drive/final_report.md:24`) stays out of every deliverable (as the Week 4 filing says, :62-64).
4. **The IPS: name neither.** 500 words; naming a banned instrument earns nothing and a skimming reader may see a breach.
   The Final Report may carry point 2 as one sentence of strategy rationale, only after Wharton's answer is filed.

## The question for Wharton (Ray sends it; Keel never contacts anyone)
Bundle it with board card T19 ("required trading activity"), due Fri 30 Oct, so it is one email:
> "The Week 4 email lists TIPS and STRIPS as not permitted; the FAQ now says 'Individual TIPS' and 'Individual
> STRIPS'. Are ETFs that hold TIPS or STRIPS permitted in the IPS and Final Report if they are available on WInS?"
File the answer in `competition/official/2026_27/`. Caplet needs no trade either way.

## Takes for the brief
- **Felix:** Where does it say a TIPS fund is fine? Nowhere yet. One word changed on a public page; the email to us didn't. Strict reading until it's in writing.
- **Kai:** Who says we'd even want one? Her bills don't index, so neither should her bonds. Point 2 is a free client-knowledge line and I'd use it in the Final Report.
- **Jun:** No number moves. I'll rename "STRIPS basis" to "payment-date basis" wherever Keel quotes it, so nobody pastes the banned word by accident.
- **Amara:** She'll feel inflation in Taiwan prices, not U.S. ones, and the case makes us say how (:147). The Tab 15 draft says it in words ("Inflation or a stronger Taiwan dollar raises costs in Taiwan", `15_tab_15.md:18`) but names no assumed rate. Is words enough for "identify and explain"? I've asked Laura's Room.
- **Tess:** Logged as SD-R11. One email for both questions, or Ray sends two and we lose track of one.
- **Nora:** Strict reading, no trade, one question bundled into T19.
