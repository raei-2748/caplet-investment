# Verification: L12 Pre-mortem (why Caplet did not make the Top 50)

Verifier pass, Fri 16 Oct 2026 (Sydney). This is AI-generated analysis (Claude) for Team Caplet. It contains no
deliverable prose. It names no person beyond first names and names no account.

**How I checked.** I opened every cited repo line in the main repo (HEAD) and in `caplet-latest` (commit 412e9e3). I
re-ran `oct16/research/KB_verify/num/reconcile.py` on `caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`
for 6, 9, 13, 14 and 15 Oct. I recounted words and comment dates. I re-fetched the Wharton main page (curl; counter
`data-counter-value="2339"` labelled "Numbers from Last Year's Investment Competition ... Teams") and the Rules & Roles
page (page.py `--grep`, found). I re-ran the three Bing RSS searches. I queried the GitHub API for the repo's visibility
and description (GitHub search itself is blocked in this session). Working file: `oct16/verify/L12w/build.py`.

## Verdict summary

| Verdict | Count | IDs |
|---|---|---|
| Confirmed | 4 | PM-02, PM-10, PM-13, PM-16 |
| Adjusted | 13 | PM-01, 03, 04, 05, 06, 07, 08, 09, 11, 12, 14, 15, 17 |
| Refuted | 0 | none |
| Unverifiable | 0 | none |
| Verifier-added | 2 | PM-V01, PM-V02 |

Overall: the lens is accurate. Every quote I checked exists and says what is claimed, and the ladder numbers reproduce
to the dollar. Its weaknesses are framing, not facts: several severities are high for claims that are AI estimates;
PM-05 ignores the TNA's explicit room for a strategy to evolve; PM-08 judges follow-through on items that were not yet
due. The share percentages in its story table (25%, 20%, ...) are AI ESTIMATES with no data behind them. They should
never be repeated as facts.

## The ladder-cost conflict (re-run)

Re-run on the same official 15 Oct curve, same bootstrap:

| Dates priced to | Basis | Cost at 1 Jan 2027 | Room under $300k |
|---|---|---|---|
| 1 Jan payment dates 2033-42 | forward | $294,461 | $5,539 (19.0bp), the number sheet |
| 1 Jan payment dates | yields unchanged | $295,246 | $4,754 (16.3bp) |
| maturities Caplet owns | forward | $297,847 | $2,153 (7.4bp) |
| maturities Caplet owns | yields unchanged | $298,628 | $1,372 (4.7bp), the lenses |

- **Why they differ.** The sheet prices each $50,000 to 1 January of the payment year
  (`caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:87`; the lens said :86). Caplet's holdings mature 2 weeks
  to 10.5 months earlier (IBTM-IBTR on 15 Dec; Feb-2037, May-2038, Nov-2039/40/41), so each $50,000 is needed earlier
  and costs more. That explains about $3,400. Forward versus unchanged yields explains about $800.
- **Something the lens missed.** `results.json` itself holds a third 15 Oct figure. `ladder_cost_1jan2027_today_curve`
  is $295,924, with the field named `ladder_headroom` at $4,076 / 13.4bp (`results.json:10,33-34`). That figure prices
  to the payment dates with par yields used as zero rates. It disagrees with the sheet's headline "about $5,500"
  (`IPS_number_sheet.md:13`). Anyone quoting `results.json` could pick the wrong one.
- **Which figure is right for which claim.** For anything about Caplet's plan, WInS book, notes or reflections, use
  the holdings basis: about $298k, with room of about $1.4k-$2.2k on 15 Oct, and always give the date and basis. Use
  $294.5k only for a sentence that explicitly describes an ideal payment-date ladder. The sheet's "1 in 3" chance of
  costing more than $300k is anchored to $294.5k (`ips_numbers.py:122`), so it is too low for the holdings.
- **Stability.** On the holdings basis with yields unchanged, the room was $4,007 on 14 Oct and $1,372 on 15 Oct. One
  day moved it by $2,635. State the rule, not a forecast.

## Finding by finding

**PM-01: ADJUSTED (critical to high).** faqs.txt:79 is quoted exactly. My word counts match (537,267 / 161,161 /
26,616). Correction: the journal (`final_report.md:14-27`) is about 387 words by my count, not 421. I lowered the
severity for two reasons. Word volume measures AI output, not team hours. And Articulation mostly lives in the Final
Report, whose instructions arrive 9 Nov. The direction of the advice is still right.

**PM-02: CONFIRMED (critical).**
- deliverables.txt:51 says the instructions will be "shared on November 9".
- Last year's doc has 63 dated comments: 26 on 11 Dec and 4 on 12 Dec 2025 (my recount).
- The journal placeholders and "Placeholder for now" (`client_portrait.md:14`) are verified.
- Knox Term 4 ends Thu 3 Dec, sourced by L10 from Knox's term-dates page.
- The fix is allowed and contains no drafted prose.

**PM-03: ADJUSTED (stays critical; evidence strengthened).** All cited lines are verified, including the conflict
between `caplet-latest/CLAUDE.md:26-29` and `START_HERE.md:26`. The lens implied a hard-rule conflict but did not quote
it. The Rules & Roles page (fetched 16 Oct) says: "AI-generated work may not be submitted as your own." It also says:
"Any AI-generated material included in your report must be properly cited, just like any other reference source." The
IPS forbids "formal citations" (IPS-FINAL:123), and an IPS that breaks the requirements "will not be considered for
semifinal selection" (:82-83). So an accepted [AI] sentence in the IPS is either uncited AI material or a format breach.
The fix (all six agree the scope; [AI] items limited to facts, numbers and flags) is allowed.

**PM-04: ADJUSTED (stays high).**
- Verified: `results.json:130` (0.9941) and `:138` (0.063, median uncovered $3,150 at :140), V5:28 and :30,
  case:97-99 and :119-120, and IPS-FINAL:73-74.
- Nuance: V5's "cannot miss" refers to the range. The range itself is missed in about 0.6% of model paths. The 6.3%
  is about later payments. Both absolute claims are contradicted by MODEL numbers.
- Added: IPS-FINAL:64-65 asks the IPS to show "How your approach will protect the required operating payments".

**PM-05: ADJUSTED (high to medium).** The cited lines are verified. But the TNA instructions expect the strategy to
change: "your strategy may continue to evolve" (TNA:17-19), and reflections may show that a decision "supported,
tested, or refined" the strategy (:28-30). Choosing an option later is therefore not a breach if the reflections are
honest. Correction: the VT note's "only" (`05_...:14`) already clashes with V5:26, which names "the half Laura keeps"
as the second source for any payment shortfall. That clash exists whichever option is chosen. The lens's claim that
the note "matched the rule when written" is UNVERIFIED: the D6 memo on "who pays a coupon shortfall" dates from 30 Sep
(`caplet-latest/docs/AI_USE.md:71`). Deciding the option before 20 Oct is still sensible.

**PM-06: ADJUSTED (stays high).** All numbers reproduce. Fixes: the line number is `ips_numbers.py:87`, and I added
the third figure in results.json (see above). The IBTR note's "about 0.2" (`05_...:15`) fits the 6 Oct holdings basis
(23.0bp). Note that the cancelled-order version says "0.3" (`:37`).

**PM-07: ADJUSTED (high to medium).** "diversif" has 0 matches in V5, and the pitch is quoted correctly. But the idea
is in V5 without the word: "a global index fund of thousands of companies" and "Relying on one issuer ... we accept
it" (V5:24). Better evidence the lens missed:
- IPS-FINAL:45-47 tells teams to "Explain how your team will approach ... portfolio construction and diversification".
- Wharton's Trading Details page lists "funding purposes" as a diversification dimension (trading.txt:49). That is a
  ready official hook for Caplet's design.

The 2021-22 precedent is FROM KB and was not re-opened.

**PM-08: ADJUSTED (high to medium; title and problem rewritten).** Every cited stale line is still in `caplet-latest`
(COMPETITION.md:49, :182, :193-194; configs; roster). But "none was done" is unfair:
- The commit landed about 24 hours after the brief.
- Items 28 and 30 are due Sun 18 to Sun 25 Oct, so they were not yet late.
- Item 1 was replaced by the team leader's own decision, which is his call to make.
- Item 3 allowed "if it stays public, write down why", and CLAUDE.md records that the leader accepted a public repo.

The clear miss is item 2. The commit edited COMPETITION.md but left in "AI may fill a ticket up to Preview".

**PM-09: ADJUSTED (stays high; confidence high to medium).** The quotes are verified. The deferral line dates from 27
Sep. Later records show at least one team vote ("the team's 1 Oct vote picks one", `sheets/.../rb_tickets.csv:1`; 1 Oct
"IPS content locked", `final_report.md:21`). What is missing is who argued what and why.

**PM-10: CONFIRMED (high).** `2025_knox_wharton.md:3827` and `:3852` are verbatim, and the journal blanks are verified.
The lens correctly names no one. Keep it that way: blaming an individual is not useful and would breach the team's
no-ranking rule.

**PM-11: ADJUSTED (high to medium; known-repeat).** `caplet-latest/docs/AI_USE.md:91`, `:71` and `:73` are verified.
The WInS notes do overlap with the AI example notes (28-45% for four notes; FROM L09 verify). But the line is labelled
"Disclosure to adapt for the Final Report appendix" and sits in the 25 Sep section. Nothing has been submitted, and
the 15 Oct brief already flagged it (P2; items 24 and 30).

**PM-12: ADJUSTED (stays medium).** Every gate is verified: IPS-FINAL:82-123; TNA-FINAL:44 and :53; the cancelled-order
notes at `05_...:33-40`; V5 at 47/50 and 497/500 words (recounted). Added one gate the list misses: teams "must meet
the required trading activity and portfolio management guidelines" (faqs.txt:76). No public page defines this, and the
portfolio freezes on 6 Nov (trading.txt:24). The team should copy any logged-in rule word for word before then (also
L05 TNA-10).

**PM-13: CONFIRMED (medium).** COMPETITION.md:49 says "Laura is a fictional client". The main page says: "While the
client is real, the financial scenario is developed specifically for the competition."

**PM-14: ADJUSTED (stays medium).** I re-ran the Bing searches and got unrelated results only. But Bing is not how a
student would search. The repo is public, has one fork, and its description reads "Knox Wharton Investment Competition
- Team Caplet" (GitHub API, 16 Oct). GitHub's own repo search covers descriptions. I could not run it here, so
"unlikely to be found" is UNVERIFIED and should not be claimed. Per L09 verify, the fork holds only the 15 Oct
snapshot; the 16 Oct AI IPS rewrites are in the main repo only.

**PM-15: ADJUSTED (stays medium).** V5:24 and suggestion 8 "(cut)" are verified. Number fix: the sheet shows about 93%
Treasuries in Jan 2028 (`IPS_number_sheet.md:61`). Added the case's own words: "willing to take thoughtful risks ... an
appropriate balance" (case:70-72).

**PM-16: CONFIRMED (medium).** The Rules page quote is re-verified: "selected as semifinalists based on the strength
of their Investment Policy Statement (IPS) and Final Reports". The TNA is still evaluated (deliverables.txt:27) and is
read together with the other two (case:161). "Time-box it" is the right reading; "ignore it" would not be.

**PM-17: ADJUSTED (medium to low).** It is accurate, but it restates PM-03, PM-05 and PM-06 without a separate action.

## Missed findings (verifier-added)

**PM-V01 (high, new): the drafted [AI] suggestions would make stories 4 and 5 worse.**
- Suggestion 5 inserts "about $294,000", the ideal payment-date figure, not the holdings basis.
- Suggestions 11 and 12 put a range and "99 times in 100" into the IPS. Wharton says the IPS "is not expected to
  include ... a final facility-contribution range" (IPS-FINAL:68-70), and the figures will be stale by 4 Dec.
- Suggestion 10 adds a MODEL "$21,000 short" without the back-up rule.
- Suggestion 9 deletes the IPS's only review and substitution rule (V5:26), although the IPS must show how the
  strategy "will guide ... investment decisions as the client's needs change" (:61-62).

The lens flagged only suggestion 8. L06 also flags no. 11; the points on 5 and 9 are new here.

**PM-V02 (medium, new): two "true story" items in the lens's reverse pre-mortem need care.**
- The 7 Oct mis-click was "an AI browser click" (`caplet-latest/COMPETITION.md:193`). Telling that story truthfully
  discloses that AI operated the WInS account. L09 flagged the platform's robot terms (binding UNVERIFIED).
- Wharton says teams are "not expected to stay awake during the night to trade" (trading.txt:52). A 12:30 a.m. story
  can read as ignoring that advice.

Build the story on the lesson, and record AI's role honestly.

## Things I checked and found fine
- No surnames, emails, usernames or account names appear in either lens file. The fork owner is not named.
- The deadline conversions are right. The TNA is due Sat 24 Oct 08:00 Sydney. After the 1 Nov clock change, the IPS is
  due Sat 7 Nov 09:00 and the Final Report Sat 5 Dec 09:00 Sydney.
- No fix asks the assistant to write deliverable text, contact anyone, or trade.
