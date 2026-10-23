# Wharton IC Rule Custodian & Authority Hierarchy
**Target**: Team Caplet — Wharton Global High School Investment Competition 2026–2027  
**Core Principle**: **Wharton is the Root Configuration**.

---

## 1. The 7-Level Authority Precedence Hierarchy

In financial decision-support and AI-assisted research, the most catastrophic failure mode is an autonomous model assuming competition rules, inventing scoring weights, or treating historical guidelines as active constraints.

To eliminate this vulnerability, `wharton-ic` enforces an un-bypassable programmatic hierarchy:

```
[Level 100] OFFICIAL_PRIVATE_VERIFIED
    └── Released Sept 15, 2026 via SurveyMonkey Apply (Client case, WInS trading limits, rubrics)
           │
[Level 80]  OFFICIAL_PUBLIC_VERIFIED
    └── Published on Wharton Global Youth webpages (Dates, team composition, ethics policy)
           │
[Level 60]  OFFICIAL_GUIDEBOOK_VERIFIED
    └── Official current competition guidebooks and participant FAQs
           │
[Level 40]  TEAM_INTERPRETATION
    └── Explicit deductions authored and signed by student team members
           │
[Level 20]  HISTORICAL_ONLY
    └── 2025 or earlier competition materials (Usable for benchmarking only; NEVER overrides current)
           │
[Level 10]  INSPIRATION
    └── Previous winning team repositories and strategies
           │
[Level 0]   AI_REASONING
    └── Model generation and argumentation — NEVER AUTHORITATIVE EVIDENCE
```

### Precedence Resolution Engine
When two rules or assertions conflict, `RuleConflictDetector` applies three programmatic checks:
1. **Authority Supremacy**: Higher authority level strictly invalidates lower authority (`Private Verified > Public Verified > Historical`).
2. **Current-Year Primacy**: Current 2026–2027 rules permanently supersede historical rules. A historical rule can never silently overwrite or modify an active rule.
3. **Ambiguity Escalation**: If two rules possess identical authority levels and conflict, the system halts with `RulePrecedenceError` and escalates to the student team.

---

## 2. Verified 2026–2027 Public Facts

The initial rule layer is compiled in `toolkit/config/wharton_public_2026_27.yaml`:

### A. Official Competition Timeline
- **Materials Release Date**: September 15, 2026 (via SurveyMonkey Apply portal)
- **Competition & WInS Trading Begins**: September 28, 2026
- **Team Roster Deadline**: October 9, 2026
- **Trading Notes Analysis Deadline**: October 23, 2026
- **Investment Policy Statement (IPS) Deadline**: November 6, 2026
- **WInS Trading Ends / Portfolio Frozen**: November 6, 2026 (at the IPS deadline)
- **Final Report Instructions Released**: November 9, 2026
- **Final Report & School Documentation Due**: December 4, 2026

All deadlines are 5:00 pm ET. (Corrected 2026-10-14: WInS does not close on 4 Dec, and Trading Notes are not due on 4 Dec.)

### B. Core Competition Philosophy
- **Portfolio Returns Do NOT Determine Winner**: Performance on the Wharton Investment Simulator (WInS) has little bearing on the final outcome. Teams are evaluated on the quality, coherence, and articulation of their investment strategy, alignment with client goals, and genuine learning.
- **Strategy Definition**: A strategy is an overarching, disciplined decision framework—not simply a basket of stock picks.
- **Anti-Complexity Warning**: Overly technical strategies or financial jargon do not impress judges. Clarity, storytelling, and defensibility win.
- **Balanced Analysis**: Both qualitative (business moats, governance) and quantitative (forensic accruals, cash flow valuation) analysis are mandatory.

### C. Required Public Deliverables
1. Official Team Roster (Due Oct 9, 2026; submitted and locked)
2. Trading Notes Analysis (Due Oct 23, 2026)
3. Investment Policy Statement (Due Nov 6, 2026)
4. Comprehensive Final Report (Due Dec 4, 2026), with the School Documentation letter as a separate file
5. WInS Trading Simulator Activity (official trading Sept 28 – Nov 6, 2026; practice 15-25 Sep)

### D. Team Composition & WInS Rules
- 4 to 6 students enrolled in the same secondary school.
- One shared WInS account per team.
- Students must personally conduct research, formulate strategy, and enter trades.
- Team leader serves as primary contact and submitter.

### E. Official Wharton AI Policy
- Generative AI may be used for idea brainstorming and scenario exploration.
- Warning: AI content can be inaccurate, incomplete, or hallucinated.
- Generative AI text must **NEVER** be submitted as student work.
- Any AI-assisted concepts must be formally cited.
- Misuse of AI constitutes academic dishonesty and warrants disqualification.

---

## 3. Private Rules (now released; was `AWAITING_OFFICIAL_MATERIAL`)

> **Update 2026-10-14:** the registered-team materials were released on 15 Sep 2026 and the WInS rules are now known. They are:
- **Virtual cash**: $300,000 (the client's $150,000 2028 deposit is not in WInS).
- **Commissions**: $25 per stock/ETF trade; $10 per US Treasury bond trade. 0% interest on cash; no fractional shares.
- **Trade limits**: max 200 trades; each order at most 2x the security's daily volume.
- **Allowed**: stocks (WInS session minimum price $3, read 29 Sep; the public $5 floor is gone from the FAQ and Trading pages (20 Oct 2026, live FAQ)), any ETF available on WInS, US Treasury bonds available on WInS.
- **Banned**: margin, short selling, stock-secured debt, crypto, derivatives, TIPS, STRIPS (20 Oct 2026, live FAQ).
- **Position limits**: 200% per stock/ETF and 100% for bonds, i.e. effectively no cap.
- **No required sector allocation or sector count**, and no minimum number of holdings.
- **Client case**: Laura Gao (see `toolkit/config/client_mandate.yaml`). Rubric criteria are published without weights.
- Per the 6 Oct Wharton email, recommendations for both contributions may only use eligible stocks, ETFs and Treasury bonds available on WInS.

The code's rule registry may still list some of these as `UNKNOWN`; treat this section and competition/COMPETITION.md as authoritative.

**Fail-Closed Rule**: Any production process requiring an unreleased official constraint halts with a clear error message. The system will **never** substitute an arbitrary assumption (such as a 25% sector cap or 10-stock minimum) for real Wharton rules.

---

## 4. Official Ingestion System & CLI

Official files are ingested into `competition/official/2026_27/` and tracked in `manifest.yaml`:

```bash
# Ingest official client case PDF
wharton-ic ingest-official /path/to/2026_client_case.pdf --type client_case

# View rule registry status
wharton-ic rules status

# List verified competition rules
wharton-ic rules list

# Check for rule conflicts
wharton-ic rules conflicts

# Verify a parsed rule
wharton-ic rules verify RULE_ID --by "Student Name"

# Export rule citations table
wharton-ic rules export-citations
```
