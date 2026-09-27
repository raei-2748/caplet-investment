# DRAFT v2 (awaiting Ray's approval): Ultracode prompt "Strategy perfection audit"

## Goal
Make Team Caplet's investment strategy for Laura Gao as strong as possible on every dimension the judges and the
case can test, so it earns a Top 50 semifinal place. "Perfect" is defined operationally as:
1. every requirement in the official materials is explicitly addressed (traceable);
2. every number is verified from a primary source file or clearly labelled as an assumption, and reproducible;
3. no internal contradictions across the strategy, the Trading Notes plan, the IPS plan and the Final Report plan;
4. every serious objection a judge, Laura, a co-sponsor, a rival team or a statistician could raise has an answer;
5. the whole strategy can be explained in plain English within the IPS limits (50-word pitch, 500-word IPS).

## Starting point (do not re-debate from scratch)
The current strategy is "Lock early" as recorded in CLAUDE.md and research/verified_2026-09-27/. Challenge it
honestly, but change it only where evidence shows a real improvement.

## Inputs (authoritative first)
- Official: competition/official/2026_27/ (client case, IPS and Trading Notes instructions, deliverables page with
  evaluation criteria and deadlines).
- Verified market data: competition/official_market_data/ + research/verified_2026-09-27/ scripts.
- Team thinking: research/council_2026-09-27/team_notes_2026-09-27.md.
- Prior AI analysis (brainstorming, lower authority): research/council_2026-09-27/.
- Historical only: competition/historical/2025_26/.
- Team client research: research/team_materials/review_why_laura_and_public_profile.md, plus the team's two original
  documents (provided to the run privately, not committed). Fact-check their claims before relying on them.

## Dimensions to audit (one auditor each)
0. Why Wharton chose Laura (lens for all others): what the client choice and the case design signal (client trend
   2023-2027, co-sponsors, certainty, creative/irregular income, diaspora and Taiwan), and whether the strategy
   answers that deeper purpose with analysis rather than decoration or tokenism. Separate verified facts from
   interpretation.
1. Case-requirement coverage: every "must/should/teams are expected" in the case, line by line.
2. Five official evaluation criteria: what a top score needs on each; where the strategy is weak.
3. Client understanding: Laura's profile, fears, goals; generic vs genuinely tailored.
4. "High degree of certainty": definition, how it is evaluated, statistical honesty.
5. Operating reserve: size, composition, how it changes 2033-2042, timing of funding, implementation risks.
6. Facility contribution and financial flexibility: the responsible-contribution rule and what stays back.
7. 2031 co-sponsor range: rule, confidence statement, protection of the floor, what goes in the fundraising draft.
8. Risks: interest rates, equities, 2028 deposit late/smaller, inflation (U.S. and Taiwan construction), USD/TWD,
   reinvestment, implementation/WInS proxy, sequence of events.
9. Consistency and timeline: strategy is frozen at the IPS (Nov 6); Trading Notes (Oct 23) and Final Report (Dec 4)
   must match; WInS P&L excluded from projections.
10. Communication: can each idea be said simply? Jargon, overclaiming, "guaranteed"/"100%" wording.
11. Distinctiveness: what most teams will do, and what makes this strategy stand out while staying correct.
12. Compliance: Wharton AI policy, format rules, eligibility, anything that could disqualify.

## Process
1. Extract a requirement checklist from the official files (quote + location).
2. Auditors (one per dimension) find gaps, each with evidence and a proposed fix.
3. Each gap is attacked by independent skeptics; it survives only if a majority cannot refute it.
4. Surviving fixes are judged for impact and side effects; conflicts between fixes are resolved explicitly.
5. Loop steps 2-4 on the revised strategy until two rounds produce no new material gap.
6. A completeness critic asks what was not checked; anything it finds becomes another round.

## Rules
- No invented data. Primary files first; web-search snippets must be labelled UNVERIFIED; state assumptions.
- Do arithmetic in Python and save scripts. Re-use the verified curve and LTCMA inputs.
- No submission-ready prose (no drafted pitch, IPS paragraphs, notes or report text). Output is a specification,
  evidence and checklists that the team turns into its own writing.
- Out of scope for this run: picking specific securities/tickers (instrument TYPES only), because this year's
  approved list is not available.
- Do not edit official materials or configs; write outputs only under research/strategy_v1/.

## Outputs (research/strategy_v1/)
1. Strategy specification v1: each decision, the reason, the evidence, and the case/criterion it serves.
2. Requirement traceability matrix: every official requirement -> where the strategy addresses it -> status.
3. Risk register: each risk, size (numbers), how the strategy handles it, residual risk.
4. Objection bank: the hardest questions with evidence-based answers (for the written deliverables now, the finale later).
5. Change log vs the current strategy, with reasons.
6. Open questions only the team can answer, and data still needed.
