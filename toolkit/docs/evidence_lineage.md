# Evidence Lineage Graph & Anti-Hallucination Engine
**Target**: Team Caplet — Academic Rigor & Forensic Lineage  
**Principle**: Evidence Before Assertion.

---

## 1. The Vulnerability of Self-Certifying AI

A major defect in off-the-shelf generative AI research is **self-certification**: an LLM authors a paragraph, inserts `[FACT]` or `[VERIFIED]` before an unverified or fabricated statement, and claims it has been audited.

In `wharton-ic`, **AI self-certification is prohibited**. An LLM cannot mark its own claims as verified.

---

## 2. Claim Classification & Verification Statuses

Every substantive sentence or statement is modeled as an `EvidenceClaim` with one of seven strict statuses:

```
┌───────────────────────────┬───────────────────────────────────────────────────────────────┐
│ Status                    │ Meaning & Verification Standard                               │
├───────────────────────────┼───────────────────────────────────────────────────────────────┤
│ VERIFIED                  │ Matched to registered primary source or deterministic calc.   │
│ PARTIALLY_VERIFIED        │ Some citations match; secondary assertions unconfirmed.       │
│ UNSUPPORTED               │ Claim lacks registered filing, database record, or calc ID.   │
│ CONTRADICTED              │ Primary source directly refutes the claim statement.          │
│ INFERENCE                 │ Valid logical deduction or hypothesis; not an empirical fact. │
│ OPINION                   │ Subjective student or analyst perspective.                    │
│ PENDING                   │ Newly extracted statement awaiting automated audit.           │
└───────────────────────────┴───────────────────────────────────────────────────────────────┘
```

---

## 3. The End-to-End Evidence DAG (Directed Acyclic Graph)

The system records an unbroken chain of custody from primary raw filing to final report paragraph:

```
[ PRIMARY SOURCE ]
    │  (e.g., SEC 10-K Filing, Official Case Study PDF, WInS Price Matrix)
    ▼
[ EXTRACTED DATUM ]
    │  (e.g., Net Operating Profit After Tax = $12.4B, Invested Capital = $67.1B)
    ▼
[ DETERMINISTIC CALCULATION ]
    │  (e.g., ROIC = 18.48% compiled via wharton_ic.fundamentals.metrics)
    ▼
[ VERIFIED CLAIM ]
    │  (e.g., "Company generates ROIC of 18.5%, exceeding 7.8% WACC by 1,068 bps")
    ▼
[ INVESTMENT THESIS ]
    │  (e.g., "Core Compounder with durable competitive advantage and pricing power")
    ▼
[ HUMAN DECISION ]
    │  (e.g., "Student PM approves 7.5% allocation in 15_human_decision.md")
    ▼
[ FINAL REPORT STATEMENT ]
       (e.g., "As demonstrated in Table 3.2, our holding in Alpha Dynamics...")
```

### Graph Traceability
Every node stores its parent IDs. Calling `graph.trace_lineage("CLAIM_ID")` walks up the tree, returning the exact filings, dates, mathematical formulas, and student approvals that justify that claim.

---

## 4. The Evidence Lineage Auditor

The `EvidenceLineageAuditor` operates during both research deliberation and final report compilation:
- **Fact Audit**: Queries known source IDs. If a factual claim cites an unrecognized source, it is downgraded to `UNSUPPORTED`.
- **Calculation Audit**: Verifies that cited numbers match deterministic engine outputs within $\pm 0.1\%$ tolerance.
- **Contradiction Detection**: Cross-references claims against recorded risk factors and opposing analyst bear cases.
- **Batch Reports**: Assembles `EvidenceAuditSummary` tables embedded into decision dossiers and report evidence packs.
