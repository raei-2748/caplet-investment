# AI Council Architecture V2: Hierarchical Multi-Agent Investment Committee
**Target**: Team Caplet — Wharton Global High School Investment Competition 2026–2027  
**Governance**: Human-in-the-Loop Fiduciary Oversight.

---

## 1. Architectural Philosophy

In traditional generative AI demos, multi-agent frameworks frequently devolve into "agreeable echo chambers" where models praise each other's hallucinations and invent quantitative metrics.

The `wharton-ic` AI Council V2 is fundamentally redesigned around Wharton's evaluation standards:
1. **Numbers from Code**: All quantitative metrics (ROIC, Sloan accruals, WACC, DCF, MCR, VaR) originate from verified Python routines. No LLM does arithmetic.
2. **Encouraged Disagreement**: The council is structured to surface flaws, blind spots, and contradictions. Consensus without vigorous debate is treated as a defect.
3. **Strict Bounds of Authority**: AI models generate arguments, hypotheses, and adversarial critiques; **only humans make investment and strategy decisions**.

---

## 2. Multi-Stage Council Hierarchy

```
STAGE A: COMPLIANCE & CLIENT STEWARDSHIP
├── Rule Custodian    ── Enforces Wharton rules & flags unverified assumptions
└── Client Steward    ── Challenges decisions that fail client objectives

STAGE B: STRATEGY FORMATION (Pre-Trading Council)
├── Strategy Architect A  ── Quality Compounders & Economic Moats
├── Strategy Architect B  ── Structural Transitions & Asymmetry
└── Strategy Architect C  ── All-Weather Endowment Discipline

STAGE C: STRATEGY RED TEAM (Adversarial Stress Test)
├── Client Red Team           ── "Where does this fail the client?"
├── Investment Red Team       ── "What financial assumptions are fragile?"
├── Simplicity Editor         ── "Where is technical jargon obscuring the story?"
├── Originality Auditor       ── "Is this generic or authentically Team Caplet?"
├── Wharton Narrative Critic  ── "Would a judge understand and remember this?"
└── Implementation Critic     ── "Can this realistically guide 10-week execution?"

STAGE D: FUTURE SECURITY RESEARCH COUNCIL (Post-Kickoff)
├── Fundamental Analyst  ── ROIC/WACC spread, cash flow conversion
├── Valuation Analyst    ── Multi-stage DCF, reverse DCF growth rate
├── Quant Analyst        ── Winsorized factor Z-scores, pairwise correlation
├── Risk Officer         ── Marginal CVaR, drawdown risk, position caps
├── Bull Researcher      ── Secular compounding catalysts
├── Bear Researcher      ── Thesis-breaking exit conditions
├── Evidence Auditor     ── Verifies numbers against primary filings
└── Committee Chair      ── Synthesizes recommendation (SUPPORT / REJECT)

STAGE E: HUMAN GOVERNANCE GATE
└── Student Officers     ── Formally signs off in decision ledger (HUMAN_APPROVED)
```

---

## 3. The 7-Phase Orchestration Protocol

The council executes sequentially across seven formal phases:

### Phase 1: Independent Blind Analysis
- Strategy Architects and initial security analysts work in complete isolation.
- Prompts are generated without access to peer outputs to prevent groupthink and early consensus anchoring.

### Phase 2: Adversarial Criticism
- Dedicated Red Team personas attack proposed strategies and theses.
- Every weakness must identify specific failure modes and actionable revision targets.

### Phase 3: Dialectical Cross-Examination
- Bull and Bear researchers debate specific operational variables (e.g., pricing power vs. regulatory scrutiny).
- Client Steward cross-examines high-return ideas that exceed client risk capacity.

### Phase 4: Evidence Verification
- `EvidenceLineageAuditor` validates every factual and numerical claim against registered source datasets.
- Self-asserted `[FACT]` labels from LLMs are discarded; claims lacking registered source lineage are flagged as `UNSUPPORTED`.

### Phase 5: Synthesis
- The Committee Chair summarizes the debate, listing points of agreement, key disputes, and conditions for entry.
- The Chair outputs a `COMMITTEE_RECOMMENDATION` (`SUPPORT`, `SUPPORT_WITH_CONDITIONS`, `RESEARCH_MORE`, or `REJECT`).
- **Critical Invariant**: The Committee Chair **CANNOT** approve an investment or strategy.

### Phase 6: Explicit Uncertainty Modeling
- The council explicitly documents unresolvable questions, unobserved client preferences, and macroeconomic risks that cannot be predicted.

### Phase 7: Human Decision Gate
- A minimum of two student team members must review the complete council dossier, enter independent rationale, and sign the decision in the CLI.

---

## 4. Production vs. Demo Failure Handling

In **DEMO** mode:
- If API keys are absent, the system engages deterministic mock generators grounded in prompt metrics for offline testing.

In **PRODUCTION** mode (`WHARTON_MODE=production`):
- If frontier LLM providers (Anthropic, OpenAI, Gemini) fail, time out, or lack API keys, the system raises `CouncilPartialError` and **FAILS CLOSED**.
- Mock responses and canned investment advice are strictly prohibited in production.
- Every API call records prompt length, response length, model version, timestamp, and whether it influenced a human decision in `outputs/ai_use_log.jsonl`.
