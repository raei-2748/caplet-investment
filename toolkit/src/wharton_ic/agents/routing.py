"""Central Model Registry and Multi-Model Routing Engine.

Maps individual council roles to distinct provider families (OpenAI, Anthropic, Google)
and tracks model diversity to prevent fake independence where one model role-plays everyone.
"""

from enum import Enum
import os
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field

from wharton_ic.agents.adapter import LLMAdapter
from wharton_ic.core.exceptions import CouncilPartialError


class ProviderFamily(str, Enum):
    OPENAI = "OPENAI"
    ANTHROPIC = "ANTHROPIC"
    GOOGLE = "GOOGLE"
    LOCAL_MOCK = "LOCAL_MOCK"


class RoleModelBinding(BaseModel):
    """Configuration binding a specific council role to a provider family and model."""
    model_config = ConfigDict(frozen=True)

    role: str
    provider_family: ProviderFamily
    model_name: str
    temperature: float = 0.2
    reasoning_depth: str = "medium"


class ModelRegistry:
    """Central registry managing role-to-provider mappings and model diversity."""

    DEFAULT_ROLE_MAPPINGS: Dict[str, RoleModelBinding] = {
        # Strategy Council
        "strategy_architect_a": RoleModelBinding(
            role="strategy_architect_a", provider_family=ProviderFamily.ANTHROPIC, model_name="claude-3-7-sonnet"
        ),
        "strategy_architect_b": RoleModelBinding(
            role="strategy_architect_b", provider_family=ProviderFamily.OPENAI, model_name="gpt-4o"
        ),
        "strategy_architect_c": RoleModelBinding(
            role="strategy_architect_c", provider_family=ProviderFamily.GOOGLE, model_name="gemini-2.0-flash"
        ),
        "strategy_advocate": RoleModelBinding(
            role="strategy_advocate", provider_family=ProviderFamily.ANTHROPIC, model_name="claude-3-7-sonnet"
        ),
        "strategy_skeptic": RoleModelBinding(
            role="strategy_skeptic", provider_family=ProviderFamily.OPENAI, model_name="gpt-4o"
        ),
        "client_steward": RoleModelBinding(
            role="client_steward", provider_family=ProviderFamily.ANTHROPIC, model_name="claude-3-7-sonnet"
        ),
        
        # Security Council
        "bull_researcher": RoleModelBinding(
            role="bull_researcher", provider_family=ProviderFamily.ANTHROPIC, model_name="claude-3-7-sonnet"
        ),
        "bear_researcher": RoleModelBinding(
            role="bear_researcher", provider_family=ProviderFamily.OPENAI, model_name="gpt-4o"
        ),
        "independent_analyst_a": RoleModelBinding(
            role="independent_analyst_a", provider_family=ProviderFamily.ANTHROPIC, model_name="claude-3-7-sonnet"
        ),
        "independent_analyst_b": RoleModelBinding(
            role="independent_analyst_b", provider_family=ProviderFamily.GOOGLE, model_name="gemini-2.0-flash"
        ),
        "risk_officer": RoleModelBinding(
            role="risk_officer", provider_family=ProviderFamily.OPENAI, model_name="gpt-4o"
        ),
        "evidence_auditor": RoleModelBinding(
            role="evidence_auditor", provider_family=ProviderFamily.ANTHROPIC, model_name="claude-3-7-sonnet"
        ),
        "committee_chair": RoleModelBinding(
            role="committee_chair", provider_family=ProviderFamily.OPENAI, model_name="gpt-4o"
        ),
    }

    def __init__(self, custom_mappings: Optional[Dict[str, RoleModelBinding]] = None):
        self.mappings = custom_mappings or dict(self.DEFAULT_ROLE_MAPPINGS)
        self.adapter = LLMAdapter()

    @property
    def role_mappings(self) -> Dict[str, RoleModelBinding]:
        return self.mappings

    def is_diversity_limited(self) -> bool:
        """Checks if available provider API keys limit multi-model diversity."""
        available_providers = []
        if os.environ.get("ANTHROPIC_API_KEY"):
            available_providers.append(ProviderFamily.ANTHROPIC)
        if os.environ.get("OPENAI_API_KEY"):
            available_providers.append(ProviderFamily.OPENAI)
        if os.environ.get("GEMINI_API_KEY"):
            available_providers.append(ProviderFamily.GOOGLE)
        return len(available_providers) <= 1

    def get_binding(self, role: str) -> RoleModelBinding:
        """Retrieves provider binding for a role, falling back to mock in demo mode."""
        if role in self.mappings:
            return self.mappings[role]
        return RoleModelBinding(
            role=role, provider_family=ProviderFamily.LOCAL_MOCK, model_name="mock-deterministic"
        )

    def assess_diversity(self, roles: List[str]) -> Dict[str, Any]:
        """Assesses provider family diversity for a list of participating roles."""
        providers = set()
        for role in roles:
            binding = self.get_binding(role)
            providers.add(binding.provider_family)

        is_limited = len(providers) <= 1
        return {
            "model_diversity_limited": is_limited,
            "distinct_provider_count": len(providers),
            "providers_active": [p.value for p in providers],
        }

    def execute_role(
        self,
        role: str,
        system_prompt: str,
        user_prompt: str,
        mode: str = "production",
    ) -> str:
        """Executes a prompt using the configured provider family.
        
        In production, provider failure raises CouncilPartialError.
        """
        binding = self.get_binding(role)
        
        # Check API key availability for chosen provider
        has_anthropic = bool(os.environ.get("ANTHROPIC_API_KEY"))
        has_openai = bool(os.environ.get("OPENAI_API_KEY"))
        has_gemini = bool(os.environ.get("GEMINI_API_KEY"))

        if mode == "production":
            if binding.provider_family == ProviderFamily.ANTHROPIC and not has_anthropic:
                raise CouncilPartialError(f"Production provider Anthropic unavailable for role '{role}'.")
            if binding.provider_family == ProviderFamily.OPENAI and not has_openai:
                raise CouncilPartialError(f"Production provider OpenAI unavailable for role '{role}'.")
            if binding.provider_family == ProviderFamily.GOOGLE and not has_gemini:
                raise CouncilPartialError(f"Production provider Google unavailable for role '{role}'.")
            if binding.provider_family == ProviderFamily.LOCAL_MOCK:
                raise CouncilPartialError(f"LOCAL_MOCK provider is forbidden in production mode for role '{role}'.")

        # Route through adapter
        provider_key = binding.provider_family.value.lower()
        return self.adapter.complete(
            prompt=user_prompt,
            system=system_prompt,
            role=role,
            provider=provider_key if mode == "production" else "mock",
            model=binding.model_name,
        )
