# Reference Provenance and Code Lineage (Caplet V2.1)

This document establishes the origin, intellectual property boundaries, and licensing classification for every reference mechanism considered or integrated into `wharton-ic`.

---

## 1. Provenance Classifications

To maintain total transparency and academic integrity for the Wharton competition:
1. **ORIGINAL CAPLET CODE**: Architected and written directly for Team Caplet (e.g. Wharton Rule Custodian, AI Authorship Firewall, Decision Journal hash-chaining, Student Governance Gates).
2. **ADAPTED REFERENCE DESIGN**: Conceptual or architectural patterns inspired by open-source frameworks, completely re-engineered from scratch to adhere to Wharton competition rules and Pydantic V2 typing standards.
3. **DIRECTLY INCORPORATED OPEN-SOURCE CODE**: Permissively licensed code blocks imported with full attribution and license preservation (none directly copied in V2.1; all designs are adapted).
4. **LEARN_ONLY CONCEPTUAL REFERENCES**: Lessons drawn from unlicensed competition repositories (Amity, David Liu) where **zero code is copied**, but strategic modeling concepts (e.g. client-goal liability simulation, defensive/offensive barbell sleeves) inform Team Caplet's architecture.

---

## 2. Detailed Lineage Registry

### TauricResearch/TradingAgents
- **License**: Apache License 2.0
- **Source Commit**: `2d17df8da1536c121e4d7395ac5a5dcec9e96d6f`
- **Component**: Checkpointing & Shared Graph State
- **Lineage Classification**: **ADAPTED REFERENCE DESIGN**
- **Caplet Implementation**:
  - `src/wharton_ic/orchestration/checkpointer.py`: Re-implements deterministic checkpoint hashing (`hashlib.sha256(f"{run_id}:{input_hash}:{prompt_version}".encode()).hexdigest()[:16]`) and stage resumability without external SQLite dependency.
  - `src/wharton_ic/orchestration/state.py`: Implements `CouncilRunState` tracking agent outputs, input hashes, model diversity flags, and human decision checkpoints.
- **Modifications Made**: Replaced automated order execution nodes with human multi-signature gates; added Wharton rule snapshots to state context.

### AI4Finance-Foundation/FinRobot
- **License**: Apache License 2.0
- **Source Commit**: `6d6ccd32c1b8b1904dc656cf06897438aba3daec`
- **Component**: Specialist Financial Agent Decomposition
- **Lineage Classification**: **ADAPTED REFERENCE DESIGN**
- **Caplet Implementation**:
  - `src/wharton_ic/agents/routing.py`: Central model registry routing roles (`Client Steward`, `Fundamental Analyst`, `Valuation Analyst`, `Risk Officer`) to configurable providers (`OPENAI`, `ANTHROPIC`, `GOOGLE`, `LOCAL_MOCK`).
- **Modifications Made**: Decoupled from Autogen runtime; enforced fail-closed `PARTIAL_COUNCIL` behavior on API outages; eliminated automated narrative report ghostwriting.

### virattt/ai-hedge-fund
- **License**: MIT License
- **Source Commit**: `154a8b2f46dca0f40764d814e4e747b0ad71f4c4`
- **Component**: Mandate as First-Class Object (`FundSpec`)
- **Lineage Classification**: **ADAPTED REFERENCE DESIGN**
- **Caplet Implementation**:
  - `src/wharton_ic/mandate/models.py`: `CapletMandate` establishing the investment mandate as a durable, serializable data object completely decoupled from stock tickers.
- **Modifications Made**: Replaced market-neutral hedge fund leverage and shorting limits with Wharton-specific long-only constraints, client horizon, and ESG exclusions.

### gavin-ho1/wharton-investment-comp (Hotchkiss — Bullish Bearcats)
- **License**: MIT License
- **Source Commit**: `ac08d15fce77d06064bf8dd7303a6bf04c3ec2f0`
- **Component**: Multi-Phase Pipeline & Report Exhibit Generation
- **Lineage Classification**: **ADAPTED REFERENCE DESIGN**
- **Caplet Implementation**:
  - `src/wharton_ic/reporting_v2/engine.py`: Structured compilation of deliverable exhibits and risk tables.
- **Modifications Made**: Replaced subjective `always-include.txt` lists and arbitrary scoring weights with mandate-derived screening criteria and deterministic provenance.

### aaravp6/All-Wharton-Investment-Competition (Amity 7 Chakras Investments)
- **License**: **NONE (Unlicensed / All Rights Reserved)**
- **Source Commit**: `9b6a93bb79a4a33298e057bd96be92b149d0cbee`
- **Component**: Client Goal Survival Simulation
- **Lineage Classification**: **LEARN_ONLY (Zero Code Copied)**
- **Caplet Implementation**: Inspired the realization that Monte Carlo simulations must calculate client goal survival rates against specific future liabilities rather than abstract volatility.

### davidliu-2008/wharton-investment-competition25-26 (David Liu)
- **License**: **NONE (Unlicensed / All Rights Reserved)**
- **Source Commit**: `89526f3e284d84c64b2d799739290c9148d42b6d`
- **Component**: Barbell Defensive/Offensive Sleeve Structure
- **Lineage Classification**: **LEARN_ONLY (Zero Code Copied)**
- **Caplet Implementation**: Informed the portfolio role framework in `CapletMandate` (Core Compounders, Defensive Stabilizers, Tactical Reinvestment Cash).
