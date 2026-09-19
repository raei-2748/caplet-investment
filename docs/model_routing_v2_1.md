# Multi-Model Routing and Diversity Specification (Caplet V2.1)

Adapted from `TauricResearch/TradingAgents` and `AI4Finance-Foundation/FinRobot`.

---

## 1. The Principle of Genuine Independence

A frequent failure mode in financial multi-agent systems is **fake independence**: prompting a single LLM model family (e.g. OpenAI GPT-4o) three times with different system prompts ("You are an aggressive trader", "You are a conservative trader", "You are a neutral judge"). Because all responses share the same underlying training biases and weights, they do not provide authentic diversification or error-checking.

Caplet V2.1 enforces genuine architectural independence:
- **Central Model Registry** (`src/wharton_ic/agents/routing.py`): Configures distinct model families across analytical roles.
- **Provider Families**:
  - `ANTHROPIC` (Claude 3.7 Sonnet)
  - `OPENAI` (GPT-4o)
  - `GOOGLE` (Gemini 2.0 Flash)
  - `LOCAL_MOCK` (Deterministic offline mock for development and testing)

---

## 2. Role-to-Provider Topology

| Council Role | Default Provider Family | Model Name | Architectural Role |
|:---|:---|:---|:---|
| **Strategy Architect A** | `ANTHROPIC` | `claude-3-7-sonnet` | Moat & Quality Bias |
| **Strategy Architect B** | `OPENAI` | `gpt-4o` | Macro & Regime Adaptive Bias |
| **Strategy Architect C** | `GOOGLE` | `gemini-2.0-flash` | Contrarian & Margin of Safety Bias |
| **Strategy Advocate** | `ANTHROPIC` | `claude-3-7-sonnet` | Builds Best Constructive Case |
| **Strategy Skeptic** | `OPENAI` | `gpt-4o` | Adversarial Red Team Attack |
| **Independent Analyst A**| `ANTHROPIC` | `claude-3-7-sonnet` | Blind Security Analysis A |
| **Independent Analyst B**| `GOOGLE` | `gemini-2.0-flash` | Blind Security Analysis B |
| **Bull Researcher** | `ANTHROPIC` | `claude-3-7-sonnet` | Multi-Round Upside Thesis |
| **Bear Researcher** | `OPENAI` | `gpt-4o` | Multi-Round Downside Attack |
| **Risk Officer** | `OPENAI` | `gpt-4o` | CVaR & Drawdown Limit Enforcer |

---

## 3. Model Diversity Audit & Fail-Closed Protocols

1. **`MODEL_DIVERSITY_LIMITED` Flag**: If a team only provides credentials for a single provider (e.g. only `OPENAI_API_KEY`), the system marks `model_diversity_limited = True` in `CouncilRunState`. It does not pretend that architects are genuinely independent.
2. **`PARTIAL_COUNCIL` Fail-Closed Behavior**: In production mode (`WHARTON_MODE=production`), if any provider returns a network error, 429 rate limit, or invalid response, the system records `PARTIAL_COUNCIL` and halts. It **never** silently substitutes canned text.
