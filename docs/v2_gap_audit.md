# Wharton-IC V2 Gap Audit & Architectural Rationalization
**Date**: September 19, 2026  
**Auditor**: Lead Architect & Systems Engineer, Team Caplet  
**Mandate**: Rigorous classification of existing codebase assets into `KEEP`, `REFACTOR`, `ARCHIVE_DEMO`, `REMOVE`, and `DEFER`. Enforcing the core principle: **Wharton is the Root Configuration**.

---

## 1. Executive Summary & Audit Mandate

The initial version of `wharton-ic` successfully established deterministic quantitative math, clean separation between logic and LLM calls, and a comprehensive package structure. However, it contained critical vulnerabilities that violate institutional competition standards:
1. **Guessed Competition Rules Treated as Fact**: Unverified limits ($2.5\%$ min weight, $15.0\%$ max position, $25.0\%$ sector cap, 10–20 stock count) were hardcoded into optimization routines as if they were official 2026–27 rules. In reality, official private trading rules are only released on September 15, 2026 via SurveyMonkey Apply.
2. **Demonstration Assets Presented as Live Research**: Ticker `MSFT` and client `Dr. Elena Vance` were written into `decisions/` and `outputs/` without unambiguous synthetic branding, creating the risk of presenting fictional research as competition deliverables.
3. **Misleading Evidence Provenance**: The existing Evidence Auditor trusted LLM `[FACT]` tags and simple regex citations without validating that facts tie back to primary filings or deterministic calculations.
4. **Autonomous AI Approval**: The Committee Chair could synthesize verdicts without requiring an un-bypassable human command-line gate with real student rationale.
5. **No Distinction Between Public Rules, Private Rules, and Team Assumptions**: The system lacked an explicit authority hierarchy capable of rejecting unverified assertions.

---

## 2. Component-by-Component Classification

### A. Core Foundation (`src/wharton_ic/core/`)
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| `config.py` | **REFACTOR** | Replace static YAML loader with tiered configuration: `wharton_public_2026_27.yaml`, `wharton_private_2026_27.yaml` (placeholder), and runtime mode flags (`DEMO` vs `PRODUCTION`). |
| `provenance.py` | **KEEP** | Excellent cryptographic SHA-256 and lineage tracking. Will be connected directly to the new `EvidenceGraph`. |
| `logging.py` | **KEEP** | Rich-based structured logging is clean and institutional. |
| `exceptions.py` | **REFACTOR** | Add `RulePrecedenceError`, `ProductionMissingMaterialError`, `UnverifiedClaimError`, and `HumanGateBlockedError`. |

---

### B. Rule Custodian & Ingestion (`src/wharton_ic/rules/` [NEW])
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| `rules/` Subsystem | **NEW (KEEP)** | First-class subsystem: `RuleRecord`, `RuleRegistry`, `RuleValidator`, `RuleConflictDetector`, `RuleCitationExporter`. Enforces the 7-level authority hierarchy. |
| `competition/official/2026_27/` | **NEW (KEEP)** | Secure ingestion vault with `manifest.yaml`. New rules enter as `PENDING_HUMAN_VERIFICATION`. |

---

### C. Client Mandate Engine (`src/wharton_ic/client/` [NEW])
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| `client/` Subsystem | **NEW (KEEP)** | Extracts official client case into `ClientMandate`. Strictly separates `CLIENT_FACT`, `TEAM_INTERPRETATION`, and `STRATEGIC_ASSUMPTION`. Requires student sign-off before strategy generation. |
| `schemas/client.py` | **REFACTOR** | Upgrade schema to capture uncertainties, conflicting objectives, and line-item source IDs. |

---

### D. AI Council & Strategy Red Team (`src/wharton_ic/council/`, `src/wharton_ic/strategy/`)
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| `council/orchestrator.py` | **REFACTOR** | Shift focus from single-stock analysis to hierarchical investment committee. Implement multi-stage orchestration (Phase 1 Independent, Phase 2 Adversarial, Phase 3 Cross-examination, Phase 4 Evidence, Phase 5 Synthesis, Phase 6 Explicit Uncertainty, Phase 7 Human Decision). |
| `strategy/` Subsystem | **NEW (KEEP)** | Pre-trading Strategy Council: `StrategyArchitectA`, `StrategyArchitectB`, `StrategyArchitectC` generating distinct philosophies in blind Phase 1; followed by `StrategyRedTeam` (Client Red Team, Investment Red Team, Simplicity Editor, Originality Auditor, Narrative Critic, Implementation Critic). |
| `agents/adapter.py` | **REFACTOR** | Maintain multi-provider router, but fail closed in `PRODUCTION` if providers fail. No mock substitute allowed in production mode. Support configurable frontier model names. |

---

### E. Security Research & Mock Fixtures (`src/wharton_ic/research/`)
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| Security Research Interface | **NEW (KEEP)** | Define the 12 core investment questions required for future stock research. |
| Test Fixtures (`TEST_ALPHA`, `TEST_BETA`, `TEST_GAMMA`) | **NEW (KEEP)** | Replace live tickers (`MSFT`, `AAPL`) with fictional test tickers for unit and system tests, preventing any confusion with actual stock research. |

---

### F. Evidence Lineage Engine (`src/wharton_ic/evidence/`)
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| `evidence/auditor.py` | **REFACTOR** | Completely rewrite. Ban AI self-certification (`[FACT]` tags). Introduce `EvidenceClaim` with 7 verification states. Build full lineage graph: `SOURCE` → `DATUM` → `CALCULATION` → `CLAIM` → `THESIS` → `DECISION` → `REPORT STATEMENT`. |

---

### G. Decision History, Journal & Trading Notes (`src/wharton_ic/journal/` [NEW])
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| `journal/` Subsystem | **NEW (KEEP)** | Immutable, timestamped event log reconstructing "How our thinking evolved over the competition". Provides the foundational record for required Trading Notes and the Final Report story. |
| `decisions/ledger.py` | **REFACTOR** | Move ledger into journal integration. Remove auto-approval capability. Require explicit CLI command with student identifier. |

---

### H. Quantitative Engines (`factors/`, `valuation/`, `portfolio/`, `risk/`, `backtest/`, `scenarios/`)
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| `factors/engine.py` | **DEFER (PHASE 2)** | Keep math and unit tests intact. Defer execution until real production universe is ingested. |
| `valuation/` (`wacc.py`, `dcf.py`, `comps.py`, `scenario.py`) | **DEFER (PHASE 2)** | Keep mathematical DCF, Reverse DCF, and Sensitivity implementations. Mark as Phase 2 / Data-Dependent. |
| `portfolio/optimizer.py` | **REFACTOR & DEFER** | Remove hardcoded 2.5%–15% and 25% sector caps from production path; parameterize by official rule inputs. If official rules are unknown, require explicit user parameters or halt with `RulePrecedenceError`. Keep math for Phase 2. |
| `risk/metrics.py` | **DEFER (PHASE 2)** | Keep MCR, PCR, ENC, and VaR routines intact. |
| `backtest/engine.py` | **DEFER (PHASE 2)** | Keep walk-forward simulator intact. |
| `scenarios/stress.py` | **DEFER (PHASE 2)** | Keep historical stress and Monte Carlo routines intact. |

---

### I. Reporting & AI Authorship Firewall (`src/wharton_ic/reporting_v2/` [NEW])
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| `reporting_v2/` Subsystem | **NEW (KEEP)** | Assembles Report Evidence Packs, not ghostwritten student prose. Verifies official rule coverage and client facts. |
| AI Authorship Firewall | **NEW (KEEP)** | Content-block level provenance tracking (`HUMAN_AUTHORED`, `AI_GENERATED`, etc.). Blocks compilation if unlabeled AI text enters student deliverables. Directs AI ideas to `outputs/research_assistance/` and student writing to `report/student_authored/`. |
| `reporting/report_pack.py` | **ARCHIVE_DEMO** | The old generator created monolithic reports from synthetic MSFT data. Relocate to demo pipeline. |

---

### J. Judge Review Council (`src/wharton_ic/review/` [NEW])
| Component | Classification | Rationale & Remediation |
| :--- | :--- | :--- |
| Judge Review Council | **NEW (KEEP)** | 9 adversarial student draft reviewers (Client Alignment, Strategy Coherence, Research, Risk, Narrative, Simplicity, Originality, Skeptical Judge, Compliance). Produces `judge_review.md` without fake numerical points. |

---

### K. Existing Synthetic / Demonstration Assets
| Asset Path | Classification | Remediation Plan |
| :--- | :--- | :--- |
| `decisions/2026-09-19_MSFT/` | **ARCHIVE_DEMO** | Move to `decisions/demo/2026-09-19_MSFT/` with prominent synthetic banners. |
| `outputs/report_pack/` | **ARCHIVE_DEMO** | Move to `outputs/demo/report_pack/` with synthetic disclaimers. |
| `outputs/charts/` | **ARCHIVE_DEMO** | Move to `outputs/demo/charts/`. |
| `config/client_mandate.yaml` | **ARCHIVE_DEMO** | Archive Dr. Elena Vance profile to `config/demo_client_mandate.yaml`. Replace active mandate with empty template awaiting September 15 case. |
| `config/competition.yaml` | **REFACTOR** | Remove unverified constraints; replace with `config/wharton_public_2026_27.yaml`. |

---

## 3. Implementation Roadmap

```
Step 1: Relocate and Archive Demo Assets (decisions/demo/, outputs/demo/, config/demo/)
Step 2: Implement Wharton Rule Custodian (src/wharton_ic/rules/)
Step 3: Implement Official Material Ingestion System (competition/official/2026_27/)
Step 4: Implement Client Mandate Engine & Auditor (src/wharton_ic/client/)
Step 5: Implement Pre-Trading Strategy Council & Red Team (src/wharton_ic/strategy/)
Step 6: Rebuild Evidence Lineage Graph & Auditor (src/wharton_ic/evidence/)
Step 7: Implement Competition Decision Journal & Trading Notes (src/wharton_ic/journal/)
Step 8: Implement Security Research Fixture & Future Council Interface (src/wharton_ic/research/)
Step 9: Implement Report Engine V2 & AI Authorship Firewall (src/wharton_ic/reporting_v2/)
Step 10: Implement Wharton Judge Review Council (src/wharton_ic/review/)
Step 11: Upgrade CLI with all V2 Commands
Step 12: Write & Execute Comprehensive Test Suite (33+ Criteria)
Step 13: Produce Complete V2 Documentation Suite (including docs/START_HERE_TEAM_CAPLET.md)
Step 14: Final Verification, Git Commit & Push
```
