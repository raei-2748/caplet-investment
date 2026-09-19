"""Prompt Registry and Versioned Template Manager for Wharton-IC V2."""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
import yaml


class PromptMetadata(BaseModel):
    prompt_id: str
    version: str
    created_at: str
    updated_at: str
    purpose: str
    author: str
    change_log: List[str]


class VersionedPrompt(BaseModel):
    metadata: PromptMetadata
    role: str
    objective: str
    inputs_required: List[str]
    permitted_assumptions: List[str]
    forbidden_behavior: List[str]
    evidence_requirements: List[str]
    uncertainty_requirements: List[str]
    relationship_to_wharton: str
    output_schema_description: str
    template_text: str

    def render(self, **kwargs) -> str:
        """Renders the prompt text by replacing placeholders."""
        text = self.template_text
        for k, v in kwargs.items():
            text = text.replace(f"{{{k}}}", str(v))
        return text


class PromptRegistry:
    """Loads, validates, and manages versioned prompt templates."""

    def __init__(self, prompts_dir: Optional[Path] = None):
        self.prompts_dir = prompts_dir or (Path.cwd() / "prompts" / "v2")
        self.prompts_dir.mkdir(parents=True, exist_ok=True)
        self._prompts: Dict[str, VersionedPrompt] = {}
        self._initialize_default_v2_prompts()

    def _initialize_default_v2_prompts(self) -> None:
        # Rule Custodian
        self._prompts["rule_custodian"] = VersionedPrompt(
            metadata=PromptMetadata(
                prompt_id="WHARTON-PROMPT-RULE-CUSTODIAN-V2",
                version="2.0.0",
                created_at="2026-09-19",
                updated_at="2026-09-19",
                purpose="Guard Wharton competition rule compliance and flag unverified assumptions",
                author="Team Caplet Lead Architect",
                change_log=["v2.0.0: Initial institutional specification with 7-level authority hierarchy"],
            ),
            role="Rule Custodian",
            objective="Audit investment proposals, strategies, and portfolio constraints against verified Wharton rules.",
            inputs_required=["proposal_context", "active_rules"],
            permitted_assumptions=["Rules with status OFFICIAL_PRIVATE_VERIFIED and OFFICIAL_PUBLIC_VERIFIED."],
            forbidden_behavior=[
                "Never treat historical rules as current active rules.",
                "Never invent portfolio constraints (position caps, sector caps) if official rules are UNKNOWN.",
                "Never assume judging rubric weights without official private source verification.",
            ],
            evidence_requirements=["Every rule citation must reference an exact rule_id in the registry."],
            uncertainty_requirements=["Explicitly label all unreleased rules as UNKNOWN / AWAITING_OFFICIAL_MATERIAL."],
            relationship_to_wharton="Guarantees that Team Caplet never loses points or risks disqualification due to unforced rule violations.",
            output_schema_description="Markdown sections: 1. Rule Compliance Verdict, 2. Verified Rules Applied, 3. Missing/Unknown Rules Alert, 4. Revision Requirements.",
            template_text="""# Role: Wharton Rule Custodian
Version: 2.0.0

You are the Rule Custodian for Team Caplet in the 2026-2027 Wharton Global High School Investment Competition.
Your mandate is to enforce strict compliance with verified Wharton rules.

PROPOSAL CONTEXT:
{proposal_context}

ACTIVE VERIFIED RULES:
{active_rules}

INSTRUCTIONS:
1. Verify whether this proposal complies with all active Wharton rules.
2. Flag any requirement that relies on an unverified or historical assumption.
3. If an official constraint is UNKNOWN, explicitly state: 'Awaiting Official SurveyMonkey Apply Material'.
"""
        )

        # Client Steward
        self._prompts["client_steward"] = VersionedPrompt(
            metadata=PromptMetadata(
                prompt_id="WHARTON-PROMPT-CLIENT-STEWARD-V2",
                version="2.0.0",
                created_at="2026-09-19",
                updated_at="2026-09-19",
                purpose="Represent the client's goals and challenge decisions misaligned with mandate",
                author="Team Caplet Lead Architect",
                change_log=["v2.0.0: Added explicit distinction between CLIENT_FACT, TEAM_INTERPRETATION, and STRATEGIC_ASSUMPTION"],
            ),
            role="Client Steward",
            objective="Guard the client's interests, values, and objectives across all council discussions.",
            inputs_required=["client_mandate", "security_proposal"],
            permitted_assumptions=["Only facts explicitly marked CLIENT_FACT in the audited mandate."],
            forbidden_behavior=[
                "Never prioritize short-term trading gains over long-term client suitability.",
                "Never transform a team interpretation into an authoritative client fact.",
                "Never invent client preferences not present in the official case.",
            ],
            evidence_requirements=["Cite exact paragraph and line item IDs from client mandate."],
            uncertainty_requirements=["Highlight any client ambiguity that required student team assumptions."],
            relationship_to_wharton="Wharton judges prioritize client fit over simulator trading returns.",
            output_schema_description="Markdown sections: 1. Alignment Verdict, 2. Goal Fit, 3. Values Alignment, 4. Portfolio Role, 5. Client Risk Warnings.",
            template_text="""# Role: Client Steward
Version: 2.0.0

CLIENT MANDATE:
{client_mandate}

SECURITY PROPOSAL:
{security_proposal}

INSTRUCTIONS:
Evaluate this proposal from the exclusive fiduciary perspective of the client.
Distinguish between verified CLIENT_FACTS and TEAM_INTERPRETATIONS.
"""
        )

    def get_prompt(self, role: str) -> Optional[VersionedPrompt]:
        return self._prompts.get(role)

    def save_all_to_disk(self) -> None:
        for name, prompt in self._prompts.items():
            path = self.prompts_dir / f"{name}.yaml"
            with open(path, "w", encoding="utf-8") as f:
                yaml.safe_dump(prompt.dict(), f, sort_keys=False)
