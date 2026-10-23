"""wharton_ic fundamentals package."""

from wharton_ic.fundamentals.metrics import (
    calculate_roic,
    calculate_roe,
    calculate_fcf_conversion,
    calculate_operating_margin,
    calculate_net_debt_ebitda,
    calculate_interest_coverage,
    calculate_altman_z_score,
    calculate_sloan_accrual_ratio,
    compute_comprehensive_fundamentals,
)

__all__ = [
    "calculate_roic",
    "calculate_roe",
    "calculate_fcf_conversion",
    "calculate_operating_margin",
    "calculate_net_debt_ebitda",
    "calculate_interest_coverage",
    "calculate_altman_z_score",
    "calculate_sloan_accrual_ratio",
    "compute_comprehensive_fundamentals",
]
