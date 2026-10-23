"""Caplet Mandate Models: First-Class Mandate Architecture decoupled from tickers."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator
from wharton_ic.client.models import ClientMandate


class PortfolioRoleDefinition(BaseModel):
    """Definition of a strategic portfolio sleeve role."""
    model_config = ConfigDict(frozen=True, extra="forbid")

    role_name: str = Field(description="e.g., Core Compounders, Defensive Stabilizers")
    target_weight_min: float = Field(ge=0.0, le=1.0)
    target_weight_max: float = Field(ge=0.0, le=1.0)
    mandate_purpose: str
    required_characteristics: List[str] = Field(default_factory=list)


class CapletMandate(BaseModel):
    """First-class investment mandate object.
    
    Inspired by virattt/ai-hedge-fund's FundSpec:
    A Caplet Investment Mandate exists independently of any individual stock.
    Hierarchy:
        WhartonRulesSnapshot -> ClientMandate -> CapletMandate -> ApprovedStrategy -> PortfolioRoles -> Universe
    """
    model_config = ConfigDict(frozen=True, extra="forbid")

    mandate_id: str
    client_mandate_id: str
    client_name: str
    wharton_rules_snapshot_id: str
    version: str = "2.1"
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Core Mandate Properties
    objective_hierarchy: List[str] = Field(
        description="Prioritized list of investment goals from primary to tertiary"
    )
    risk_philosophy: str = Field(
        description="Explicit statement of risk capacity, tolerance, and drawdown limits"
    )
    investment_horizon_years: float = Field(
        gt=0.0, description="Mandate horizon in years (e.g. 10.0)"
    )
    liquidity_philosophy: str = Field(
        description="Cash reserve requirements and interim withdrawal buffers"
    )

    # Sleeve and Role Framework
    portfolio_roles: List[PortfolioRoleDefinition] = Field(
        default_factory=list,
        description="Sleeve structure (e.g. Core Compounders, Defensive Stabilizers, Tactical Cash)"
    )
    evaluation_principles: List[str] = Field(
        default_factory=list,
        description="Hurdles securities must overcome (e.g. ROIC > WACC, positive FCF)"
    )
    forbidden_exposures: List[str] = Field(
        default_factory=list,
        description="Excluded sectors, predatory models, or negative screen criteria"
    )

    # Operational Parameters
    review_cadence: str = Field(default="WEEKLY")
    rebalancing_philosophy: str = Field(default="LOW_TURNOVER_DRIFT_BUFFERED")
    decision_thresholds: Dict[str, float] = Field(
        default_factory=lambda: {
            "min_roic_wacc_spread_bps": 300.0,
            "max_position_size": 0.20,
            "min_position_size": 0.05,
            "max_cvar_95": 0.25,
            "min_altman_z": 2.0,
        }
    )
    monitoring_obligations: List[str] = Field(
        default_factory=lambda: [
            "Weekly tracking error and sector drift monitoring against WInS simulator.",
            "Immediate thesis invalidation review upon -15% position drawdown.",
            "Quarterly earnings ROIC and FCF conversion verification.",
        ]
    )
    council_configuration: Dict[str, Any] = Field(
        default_factory=lambda: {
            "debate_rounds": 2,
            "independent_blind_analysts": True,
            "require_two_student_signatures": True,
        }
    )

    @field_validator("forbidden_exposures", "objective_hierarchy", mode="after")
    @classmethod
    def validate_no_tickers(cls, v: List[str]) -> List[str]:
        """Ensures mandate does NOT define strategy via specific stock tickers."""
        common_ticker_flags = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META"]
        for item in v:
            for tkr in common_ticker_flags:
                if f" {tkr} " in f" {item} ":
                    raise ValueError(f"Ticker '{tkr}' detected in mandate! Mandate must remain ticker-independent.")
        return v

    @classmethod
    def from_client_mandate(
        cls,
        client: ClientMandate,
        wharton_snapshot_id: str,
        mandate_id: Optional[str] = None
    ) -> "CapletMandate":
        """Synthesizes an operational CapletMandate from an approved ClientMandate."""
        m_id = mandate_id or f"MANDATE-{client.client_id}-{datetime.now().strftime('%Y%m%d')}"
        
        # Derive objectives
        objectives = [item.statement for item in client.financial_objectives] + [
            item.statement for item in client.nonfinancial_objectives
        ]
        if not objectives:
            objectives = ["Long-term capital growth aligned with client values."]

        # Derive portfolio roles
        roles = [
            PortfolioRoleDefinition(
                role_name="Core Compounders",
                target_weight_min=0.45,
                target_weight_max=0.65,
                mandate_purpose="Harvest secular growth through high-ROIC economic moats.",
                required_characteristics=["ROIC > 15%", "Negative Sloan accruals", "High customer switching costs"],
            ),
            PortfolioRoleDefinition(
                role_name="Defensive Stabilizers",
                target_weight_min=0.20,
                target_weight_max=0.35,
                mandate_purpose="Anchor drawdown protection and low-beta resilience.",
                required_characteristics=["Beta < 0.85", "Inelastic demand", "Dividend coverage > 2.0x"],
            ),
            PortfolioRoleDefinition(
                role_name="Tactical Cash Reserve",
                target_weight_min=0.05,
                target_weight_max=0.15,
                mandate_purpose="Liquidity buffer to satisfy interim needs and drawdown rebalancing.",
                required_characteristics=["Zero duration risk", "Capital preservation"],
            ),
        ]

        exclusions = [item.statement for item in client.explicit_exclusions]

        return cls(
            mandate_id=m_id,
            client_mandate_id=client.client_id,
            client_name=client.client_name,
            wharton_rules_snapshot_id=wharton_snapshot_id,
            objective_hierarchy=objectives,
            risk_philosophy=client.risk_tolerance.statement,
            investment_horizon_years=10.0,
            liquidity_philosophy=client.liquidity_requirements.statement,
            portfolio_roles=roles,
            evaluation_principles=[
                "Every holding must directly map to one of the three mandate portfolio roles.",
                "Valuation must provide margin of safety based on reverse DCF implied growth.",
                "Accounting quality must be verified through Sloan accrual and Altman Z metrics.",
            ],
            forbidden_exposures=exclusions,
        )
