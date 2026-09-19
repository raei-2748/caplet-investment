# Agent Graph Architecture Specification (Caplet V2.1)

Adapted from `TauricResearch/TradingAgents`, `wharton-ic` employs an explicit graph-based orchestration pattern designed specifically for the Wharton Global High School Investment Competition.

---

## 1. Why a Lightweight Internal Graph?

Rather than adding heavy third-party framework dependencies (like Autogen or complex LangGraph runtimes) that add deployment fragility and opaque execution loops, Caplet V2.1 implements a lightweight, deterministic graph engine in `src/wharton_ic/orchestration/graph.py`.

### Key Capabilities:
- **Discrete Node Boundaries**: Each agent operates within an isolated node with explicit input and output typing.
- **Resumable Checkpointing**: Deterministic thread hashing allows long council runs to resume at the exact stage of failure.
- **Blind Phase Isolation**: Parallel nodes (e.g. Strategy Architects A, B, C or Independent Analysts A, B) cannot inspect peer node state during phase 1.
- **Fail-Closed Partial Execution**: On provider outages, nodes report `PARTIAL_COUNCIL` rather than substituting hallucinated responses.
- **First-Class Human Decision Gates**: The graph halts cleanly when human sign-off is required.

---

## 2. Strategy Council Graph Flow

```mermaid
graph TD
    A["Wharton Rules & Client Mandate"] --> B["Stage 1: Blind Parallel Generation"]
    B --> B1["Strategy Architect A (Quality Moats)"]
    B --> B2["Strategy Architect B (Macro Adaptive)"]
    B --> B3["Strategy Architect C (Contrarian Value)"]
    B1 --> C["Stage 2: Dynamic Red Team"]
    B2 --> C
    B3 --> C
    C --> C1["Client Fit Red Team"]
    C --> C2["Investment Red Team"]
    C --> C3["Simplicity & Originality Critics"]
    C --> C4["Implementation & Narrative Critics"]
    C1 --> D["Stage 3: Multi-Round Adversarial Debate"]
    C2 --> D
    C3 --> D
    C4 --> D
    D --> E["Stage 4: Committee Recommendation Memo"]
    E --> F["Stage 5: HUMAN STUDENT DECISION GATE"]
```

---

## 3. Security Research Council Graph Flow

```mermaid
graph TD
    S0["Approved Universe Ticker"] --> S1["Deterministic Ratios & Valuations (Code)"]
    S1 --> S2["Phase 1: Specialist Analysis (Client, Fund, Val, Quant, Macro)"]
    S2 --> S3["Phase 2: Blind Independent Analysts (Model A vs Model B)"]
    S3 --> S4["Phase 3: Multi-Round Bull vs. Bear Debate"]
    S4 --> S5["Phase 4: Risk Officer & Portfolio Architect"]
    S5 --> S6["Phase 5: Evidence Lineage Audit"]
    S6 --> S7["Phase 6: Committee Chair Recommendation Memo"]
    S7 --> S8["Phase 7: HUMAN PORTFOLIO TRADE GATE"]
```
