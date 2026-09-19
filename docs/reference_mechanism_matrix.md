# Reference Mechanism Matrix (Caplet V2.1)

This matrix classifies individual mechanisms from the six examined reference repositories for integration into `wharton-ic`.

### Classification Key:
- **`COPY`**: Small, clean, permissively licensed implementation incorporated with explicit attribution.
- **`ADAPT`**: Concept or architectural pattern rewritten to fit Wharton rules and Caplet design standards.
- **`WRAP`**: External library or module kept intact and accessed through a clean adapter interface.
- **`LEARN_ONLY`**: Conceptual lesson informing design; no code copied (mandatory for unlicensed repos).
- **`REJECT`**: Inappropriate, misleading, unsafe, overcomplicated, or violating Wharton competition rules.

---

## Mechanism Classification Table

| Mechanism | Source Repo | Source Commit | License | Caplet Need | Classification | Risk / Conflict with Wharton | Adaptation Plan | Caplet Destination |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **Deterministic Checkpoint Hashing** (`thread_id`) | TradingAgents | `2d17df8` | Apache-2.0 | Resumable multi-stage agent runs without re-executing | **ADAPT** | Checkpoints must invalidate if input rules or mandate change | Adapt SHA-256 hash folding run ID, input hash, and prompt signatures | `src/wharton_ic/orchestration/checkpointer.py` |
| **Typed Shared Agent State** | TradingAgents | `2d17df8` | Apache-2.0 | Explicit tracking of multi-agent runs, turns, and evidence | **ADAPT** | Must include Wharton rule snapshots and human decision gates | Implement `CouncilRunState` Pydantic model with strict validation | `src/wharton_ic/orchestration/state.py` |
| **Multi-Round Adversarial Debate** | TradingAgents | `2d17df8` | Apache-2.0 | Dynamic debate between Advocate and Skeptic | **ADAPT** | Must not aim for forced consensus; must expose root disagreements | Implement 2-round Advocate/Skeptic debate with synthesis node | `src/wharton_ic/strategy/engine.py`, `research/council.py` |
| **Post-Decision Reflection Memory** | TradingAgents | `2d17df8` | Apache-2.0 | Track student decision evolution and lessons learned | **ADAPT** | Historical AI opinions must not become facts | Maintain separate Factual vs Learning memories; tie to journal | `src/wharton_ic/strategy/memory.py`, `journal/engine.py` |
| **Direct Autonomous Trading Execution** | TradingAgents | `2d17df8` | Apache-2.0 | None | **REJECT** | Violates Wharton rule: AI cannot execute trades | Prohibited; human multi-signature gate enforced before trade | N/A (Blocked) |
| **Social Media / Reddit Sentiment Scraper** | TradingAgents | `2d17df8` | Apache-2.0 | None | **REJECT** | Unreliable, ungrounded noise; disfavored by Wharton judges | Use verified filings and deterministic financial ratios only | N/A (Blocked) |
| **Specialist Financial Agent Library** | FinRobot | `6d6ccd3` | Apache-2.0 | Modular role registry for multi-agent council | **ADAPT** | Must bind each role to Wharton competition dimensions | Implement role registration decoupled from Autogen | `src/wharton_ic/agents/routing.py` |
| **Deterministic Compute / LLM Boundary** | FinRobot | `6d6ccd3` | Apache-2.0 | Strict separation of math from narrative | **ADAPT** | None (core Caplet principle) | Ensure all numbers originate from Python code with provenance | `src/wharton_ic/evidence/auditor.py` |
| **Automated Complete PDF Report Generation** | FinRobot | `6d6ccd3` | Apache-2.0 | None | **REJECT** | Violates Wharton academic integrity / ghostwriting rules | Report engine outputs Evidence Pack & tables; prose is student-written | `src/wharton_ic/reporting_v2/` |
| **Mandate as First-Class Object** (`FundSpec`) | ai-hedge-fund | `154a8b2` | MIT | Strategy & mandate existing independently of tickers | **ADAPT** | Must reflect individual high-school client, not hedge fund | Implement `CapletMandate` with objective hierarchy & constraints | `src/wharton_ic/mandate/models.py` |
| **Short-Selling & Market-Neutral Leverage** | ai-hedge-fund | `154a8b2` | MIT | None | **REJECT** | Strictly prohibited by Wharton trading simulator rules | Strictly long-only equity & cash constraints enforced in code | `src/wharton_ic/portfolio/` |
| **Multi-Phase Pipeline Configuration** | Hotchkiss | `ac08d15` | MIT | Structured competition workflow from screening to report | **ADAPT** | Hotchkiss used arbitrary factor weights | Adapt clear stage separation driven by client mandate objectives | `src/wharton_ic/cli/main.py` |
| **Correlation Threshold Clustering** | Hotchkiss | `ac08d15` | MIT | Diversification control preventing sector concentration | **ADAPT** | Thresholds must link to client risk tolerance | Adapt pairwise correlation filtering into portfolio screening | `src/wharton_ic/factors/`, `portfolio/` |
| **Hardcoded `always-include.txt`** | Hotchkiss | `ac08d15` | MIT | None | **REJECT** | Arbitrary bias bypassing objective research | Every security must pass the 11-member research council | N/A (Blocked) |
| **Report Table Generation Scripts** | Hotchkiss | `ac08d15` | MIT | Deterministic formatting of submission exhibits | **ADAPT** | Must include provenance hashes and citation footnotes | Implement deterministic markdown/CSV table exporters | `src/wharton_ic/reporting_v2/` |
| **Client-Goal Survival Monte Carlo Simulation** | Amity 7 Chakras | `9b6a93b` | NONE | Model client-specific liabilities & spending needs | **LEARN_ONLY** | Unlicensed repo; cannot copy code | Rewrite client liability survival simulation from scratch | `src/wharton_ic/scenarios/` |
| **Fragile Web Scraping of Consensus Estimates** | Amity 7 Chakras | `9b6a93b` | NONE | None | **REJECT** | Unreliable, ungrounded HTML scraping prone to breakage | Use point-in-time cached data providers | N/A (Blocked) |
| **Barbell Sleeve Architecture (60/40)** | David Liu | `89526f3` | NONE | Explicit defensive vs. offensive sleeve role separation | **LEARN_ONLY** | Unlicensed repo; hardcoded parameters | Adapt conceptual sleeve framework into `CapletMandate` roles | `src/wharton_ic/mandate/models.py` |
| **Uncalibrated Subjective Expected Returns** | David Liu | `89526f3` | NONE | None | **REJECT** | Numbers pulled from thin air without verifiable data source | Enforce strict lineage from market data & reverse DCF | N/A (Blocked) |
