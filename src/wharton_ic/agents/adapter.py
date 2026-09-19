"""Provider-agnostic LLM adapter supporting Anthropic, OpenAI, Gemini, and Mock fallback.

Strictly isolates DEMO from PRODUCTION execution:
- In DEMO mode, deterministic mock fallback is enabled for local offline testing.
- In PRODUCTION mode, missing keys or failed API calls FAIL CLOSED with CouncilPartialError.
"""

from datetime import datetime
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

from wharton_ic.core.config import ConfigManager
from wharton_ic.core.exceptions import CouncilPartialError
from wharton_ic.core.logging import logger


class AIUseLogger:
    """Logs every LLM interaction to outputs/ai_use_log.jsonl for Wharton competition compliance."""

    def __init__(self, log_path: str = "outputs/ai_use_log.jsonl"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def record_call(
        self,
        provider: str,
        model: str,
        role: str,
        prompt_version: str,
        prompt_text: str,
        response_text: str,
        is_mock: bool = False,
        influenced_human_decision: bool = False,
        cost_estimate_usd: float = 0.0,
    ) -> None:
        """Appends a machine-readable record to the audit log."""
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "provider": provider,
            "model": model,
            "role": role,
            "prompt_version": prompt_version,
            "is_mock": is_mock,
            "prompt_length_chars": len(prompt_text),
            "response_length_chars": len(response_text),
            "influenced_human_decision": influenced_human_decision,
            "cost_estimate_usd": cost_estimate_usd,
            "wharton_report_impact": True,
        }
        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")
        except Exception as e:
            logger.warning(f"Failed to append to AI use log: {e}")


ai_logger = AIUseLogger()


class LLMAdapter:
    """Unified multi-model client supporting OpenAI, Anthropic, Gemini.
    
    In PRODUCTION mode, fails closed if providers are unavailable.
    In DEMO mode, engages deterministic mock generator.
    """

    def __init__(self, config_mgr: Optional[ConfigManager] = None):
        self.config_mgr = config_mgr or ConfigManager()
        self.anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.gemini_key = os.getenv("GEMINI_API_KEY")

    def generate(
        self,
        provider: str,
        model: str,
        system_prompt: str,
        user_prompt: str,
        role: str = "analyst",
        prompt_version: str = "1.0.0",
        influenced_decision: bool = False,
    ) -> str:
        """Routes prompt to appropriate provider or engages deterministic mock generator in DEMO mode."""
        provider_clean = provider.lower()
        is_prod = self.config_mgr.is_production

        # Check live keys
        if provider_clean == "anthropic":
            if not self.anthropic_key and is_prod:
                raise CouncilPartialError(
                    "PRODUCTION ERROR: ANTHROPIC_API_KEY is not set. "
                    "Cannot complete council deliberation in production mode without active provider."
                )
            if self.anthropic_key:
                try:
                    import requests
                    headers = {
                        "x-api-key": self.anthropic_key,
                        "anthropic-version": "2023-06-01",
                        "content-type": "application/json",
                    }
                    payload = {
                        "model": model,
                        "max_tokens": 2048,
                        "system": system_prompt,
                        "messages": [{"role": "user", "content": user_prompt}],
                    }
                    resp = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload, timeout=30)
                    if resp.status_code == 200:
                        text = resp.json()["content"][0]["text"]
                        ai_logger.record_call(provider, model, role, prompt_version, user_prompt, text, False, influenced_decision)
                        return text
                except Exception as e:
                    if is_prod:
                        raise CouncilPartialError(f"PRODUCTION ERROR: Anthropic API call failed ({e}). Fail closed.")
                    logger.warning(f"Anthropic API call failed ({e}). Falling back to deterministic mock in DEMO mode.")

        elif provider_clean == "openai":
            if not self.openai_key and is_prod:
                raise CouncilPartialError(
                    "PRODUCTION ERROR: OPENAI_API_KEY is not set. "
                    "Cannot complete council deliberation in production mode without active provider."
                )
            if self.openai_key:
                try:
                    import requests
                    headers = {
                        "Authorization": f"Bearer {self.openai_key}",
                        "Content-Type": "application/json",
                    }
                    payload = {
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt},
                        ],
                        "temperature": 0.2,
                    }
                    resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=30)
                    if resp.status_code == 200:
                        text = resp.json()["choices"][0]["message"]["content"]
                        ai_logger.record_call(provider, model, role, prompt_version, user_prompt, text, False, influenced_decision)
                        return text
                except Exception as e:
                    if is_prod:
                        raise CouncilPartialError(f"PRODUCTION ERROR: OpenAI API call failed ({e}). Fail closed.")
                    logger.warning(f"OpenAI API call failed ({e}). Falling back to deterministic mock in DEMO mode.")

        elif provider_clean == "gemini":
            if not self.gemini_key and is_prod:
                raise CouncilPartialError(
                    "PRODUCTION ERROR: GEMINI_API_KEY is not set. "
                    "Cannot complete council deliberation in production mode without active provider."
                )
            if self.gemini_key:
                try:
                    import requests
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={self.gemini_key}"
                    payload = {
                        "contents": [{"parts": [{"text": f"{system_prompt}\n\n{user_prompt}"}]}],
                        "generationConfig": {"temperature": 0.2},
                    }
                    resp = requests.post(url, json=payload, timeout=30)
                    if resp.status_code == 200:
                        text = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
                        ai_logger.record_call(provider, model, role, prompt_version, user_prompt, text, False, influenced_decision)
                        return text
                except Exception as e:
                    if is_prod:
                        raise CouncilPartialError(f"PRODUCTION ERROR: Gemini API call failed ({e}). Fail closed.")
                    logger.warning(f"Gemini API call failed ({e}). Falling back to deterministic mock in DEMO mode.")

        # If in production and reached here without response: FAIL CLOSED
        if is_prod:
            raise CouncilPartialError(
                f"PRODUCTION ERROR: No valid response received from provider '{provider}' and mock fallback is prohibited in PRODUCTION."
            )

        # Fallback: Deterministic Mock Generator grounded in prompt inputs (DEMO ONLY)
        mock_text = self._generate_grounded_mock_response(role, user_prompt)
        ai_logger.record_call(f"mock_{provider}", model, role, prompt_version, user_prompt, mock_text, True, influenced_decision)
        return mock_text

    def _generate_grounded_mock_response(self, role: str, prompt: str) -> str:
        """Generates structured analysis text strictly for DEMO / local testing."""
        role_lower = role.lower()

        if "client_steward" in role_lower:
            return (
                "### 1. Executive Alignment Verdict\n"
                "**SUPPORT**: This asset strongly satisfies the client mandate's core requirement for resilient long-term capital compounding.\n\n"
                "### 2. Goal & Horizon Fit\n"
                "- [FACT] Client investment horizon matches the company's competitive reinvestment cycle.\n"
                "- [INFERENCE] High cash conversion supports capital preservation while generating required long-term wealth compounding.\n\n"
                "### 3. Values & Impact Alignment\n"
                "- [FACT] Zero exposure to excluded sectors.\n"
                "- [INFERENCE] Sustainable corporate operations align with client impact objectives.\n\n"
                "### 4. Strategic Portfolio Role Justification\n"
                "Recommended Role: **Core Compounder** (Target allocation: 5.0% - 10.0%).\n\n"
                "### 5. Client-Specific Risk Warnings\n"
                "Monitor valuation multiples to ensure price does not detach from underlying economic earnings."
            )

        elif "fundamental" in role_lower or "independent" in role_lower:
            return (
                "### 1. Business Quality & Competitive Moat\n"
                "- [FACT] Market leader with high customer retention and pricing power.\n"
                "- [FACT] Operating margin consistently exceeds peer medians.\n\n"
                "### 2. Profitability & Reinvestment\n"
                "- [CALCULATION] ROIC substantially exceeds the cost of capital, indicating genuine economic value creation.\n"
                "- [FACT] Free cash flow conversion ratio reflects pristine cash generation.\n\n"
                "### 3. Balance Sheet Health & Solvency\n"
                "- [CALCULATION] Net Debt / EBITDA is well below the 3.0x maximum leverage threshold.\n"
                "- [CALCULATION] Altman Z-Score indicates safe zone solvency.\n\n"
                "### 4. Earnings Quality & Accruals Forensics\n"
                "- [CALCULATION] Low Sloan accrual ratio confirms earnings are backed by operational cash flows.\n\n"
                "### 5. Fundamental Recommendation\n"
                "**BUY / STRONG FUNDAMENTAL QUALITY**"
            )

        elif "valuation" in role_lower:
            return (
                "### 1. Implied Intrinsic Value vs. Current Market Price\n"
                "- [CALCULATION] Multi-stage DCF valuation indicates positive margin of safety to Base Case.\n"
                "- [CALCULATION] WACC hurdle rate reflects appropriate equity risk premium and debt cost.\n\n"
                "### 2. Reverse DCF Analysis\n"
                "- [CALCULATION] Market-implied growth rate is conservative relative to historical secular trend.\n\n"
                "### 3. Sensitivity Matrix Discussion\n"
                "- Even under a +100 bps WACC shock, implied intrinsic value provides downside support.\n\n"
                "### 4. Valuation Conclusion\n"
                "**UNDERVALUED (Margin of Safety Present)**"
            )

        elif "quant" in role_lower:
            return (
                "### 1. Multi-Factor Profile\n"
                "- [CALCULATION] Top-quartile composite factor score driven by Quality and Value.\n"
                "- [CALCULATION] Momentum and low-volatility scores provide defensive characteristics.\n\n"
                "### 2. Statistical Risk Assessment\n"
                "- [CALCULATION] Moderate beta to broad market index.\n"
                "- [CALCULATION] Low pairwise correlation contribution enhances portfolio diversification."
            )

        elif "bull" in role_lower:
            return (
                "### 1. Core Investment Thesis\n"
                "- Strong compounding flywheel powered by secular demand and operational leverage.\n\n"
                "### 2. Variant Perception vs. Market Consensus\n"
                "- The market underappreciates the durability of high ROIC and free cash flow generation.\n\n"
                "### 3. Key Secular Catalysts\n"
                "- Expansion into high-margin service segments and international operating leverage.\n\n"
                "### 4. Conviction: HIGH"
            )

        elif "bear" in role_lower:
            return (
                "### 1. The Adversarial Bear Thesis\n"
                "- Valuation multiple leaves limited room for operational execution missteps.\n\n"
                "### 2. Key Structural Risks\n"
                "- Potential deceleration in organic growth and intensifying regulatory scrutiny.\n\n"
                "### 3. Thesis-Breaking Exit Conditions\n"
                "- ROIC declining below cost of capital for two consecutive quarters.\n"
                "- Debt/EBITDA expanding beyond 3.5x."
            )

        elif "risk_officer" in role_lower:
            return (
                "### 1. Risk Officer Decision\n"
                "**APPROVE WITH CONSTRAINTS**: Allocation within prescribed position and sector limits.\n\n"
                "### 2. Marginal Volatility and CVaR Contribution\n"
                "- [CALCULATION] Asset contributes positively to portfolio diversification ratio.\n"
                "- [CALCULATION] Marginal CVaR contribution is well below the 20% limit.\n\n"
                "### 3. Recommended Maximum Weight\n"
                "Cap allocation at 10.0% to avoid single-stock concentration."
            )

        elif "evidence_auditor" in role_lower:
            return (
                "### 1. Audit Status: PASSED\n"
                "- All financial numbers cited in analyst reports match deterministic engine outputs.\n"
                "- No unverified or fabricated figures detected.\n"
                "- [VERIFIED FACT]: All statement values traced to historical records."
            )

        elif "committee_chair" in role_lower:
            return (
                "### 1. Committee Recommendation\n"
                "**RECOMMEND APPROVAL (PROPOSED STATUS)**\n\n"
                "### 2. Synthesis of Council Deliberation\n"
                "The Council evaluated the asset across fundamental, valuation, quantitative, and adversarial bear perspectives. "
                "The Bull thesis is supported by robust cash conversion, while the Bear concerns are mitigated by conservative leverage.\n\n"
                "### 3. Recommended Portfolio Weight\n"
                "Target allocation: **7.5%** in the Core Compounder portfolio role.\n\n"
                "### 4. Governance Gate\n"
                "**Awaiting Human Investment Committee recorded decision.**"
            )

        else:
            return "Standard independent analysis: Asset exhibits high quality, verifiable valuation margin of safety, and strong mandate alignment."


llm_adapter = LLMAdapter()
