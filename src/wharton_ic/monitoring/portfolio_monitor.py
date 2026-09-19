"""Real-time portfolio monitoring, risk drift, and thesis alert engine."""

from enum import Enum
from datetime import date, datetime, timedelta
from typing import Dict, List, Optional, Any
import numpy as np
import pandas as pd
from wharton_ic.risk.metrics import calculate_max_drawdown, calculate_annualized_volatility
from wharton_ic.core.logging import logger

class AlertSeverity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

class PortfolioAlert:
    def __init__(self, severity: AlertSeverity, category: str, ticker: Optional[str], message: str):
        self.timestamp = datetime.utcnow()
        self.severity = severity
        self.category = category
        self.ticker = ticker
        self.message = message

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp.isoformat(),
            "severity": self.severity.value,
            "category": self.category,
            "ticker": self.ticker,
            "message": self.message
        }

    def __repr__(self) -> str:
        t_str = f"[{self.ticker}] " if self.ticker else ""
        return f"[{self.severity.value}] {t_str}{self.category}: {self.message}"

class PortfolioMonitor:
    """
    Monitors portfolio health against Wharton rules and client constraints:
    1. Weight drift exceeding tolerance (+- 3%).
    2. Sector concentration breaching 25%.
    3. Holding-level drawdowns exceeding 15% (thesis review trigger).
    4. Overall portfolio volatility deviating from target (14% +- 4%).
    5. Research obsolescence (proposals older than 45 days).
    """

    def __init__(
        self,
        target_weights: Dict[str, float],
        sector_map: Dict[str, str],
        max_sector_weight: float = 0.25,
        drift_tolerance: float = 0.03,
        drawdown_alert_threshold: float = 0.15,
        target_volatility: float = 0.14
    ):
        self.target_weights = target_weights
        self.sector_map = sector_map
        self.max_sector_weight = max_sector_weight
        self.drift_tolerance = drift_tolerance
        self.drawdown_alert_threshold = drawdown_alert_threshold
        self.target_volatility = target_volatility

    def inspect_portfolio(
        self,
        current_weights: Dict[str, float],
        prices_df: pd.DataFrame,
        proposal_dates: Optional[Dict[str, date]] = None
    ) -> List[PortfolioAlert]:
        """Runs full suite of monitoring checks and returns detected alerts."""
        alerts: List[PortfolioAlert] = []

        # 1. Weight Drift Checks
        for ticker, target_w in self.target_weights.items():
            curr_w = current_weights.get(ticker, 0.0)
            drift = curr_w - target_w
            if abs(drift) > self.drift_tolerance:
                severity = AlertSeverity.WARNING if abs(drift) < 0.06 else AlertSeverity.CRITICAL
                alerts.append(PortfolioAlert(
                    severity=severity,
                    category="WEIGHT_DRIFT",
                    ticker=ticker,
                    message=f"Current weight ({curr_w*100:.1f}%) drifted by {drift*100:+.1f}% from target ({target_w*100:.1f}%)."
                ))

        # 2. Sector Concentration Checks
        sector_totals: Dict[str, float] = {}
        for ticker, curr_w in current_weights.items():
            sector = self.sector_map.get(ticker, "Unclassified")
            sector_totals[sector] = sector_totals.get(sector, 0.0) + curr_w

        for sector, total_w in sector_totals.items():
            if total_w > self.max_sector_weight:
                alerts.append(PortfolioAlert(
                    severity=AlertSeverity.CRITICAL,
                    category="SECTOR_LIMIT_BREACH",
                    ticker=None,
                    message=f"Sector '{sector}' total allocation ({total_w*100:.1f}%) breaches 25% Wharton cap."
                ))

        # 3. Holding-Level Drawdown Checks
        for ticker in current_weights.keys():
            if ticker in prices_df.columns:
                series = prices_df[ticker].dropna()
                if len(series) > 10:
                    peak = series.cummax()
                    dd = float(((series - peak) / peak).iloc[-1])
                    if dd <= -self.drawdown_alert_threshold:
                        alerts.append(PortfolioAlert(
                            severity=AlertSeverity.WARNING,
                            category="THESIS_DRAWDOWN_TRIGGER",
                            ticker=ticker,
                            message=f"Security drawdown reached {dd*100:.1f}%, triggering mandatory fundamental review."
                        ))

        # 4. Portfolio Volatility Check
        port_ret = (prices_df.pct_change().dropna() * [current_weights.get(t, 0.0) for t in prices_df.columns]).sum(axis=1)
        if len(port_ret) > 20:
            vol = calculate_annualized_volatility(port_ret)
            if vol > self.target_volatility + 0.04:
                alerts.append(PortfolioAlert(
                    severity=AlertSeverity.WARNING,
                    category="VOLATILITY_EXPANSION",
                    ticker=None,
                    message=f"Annualized portfolio volatility ({vol*100:.1f}%) exceeds target corridor."
                ))

        # 5. Research Obsolescence Check
        if proposal_dates:
            today = date.today()
            for ticker, p_date in proposal_dates.items():
                if (today - p_date).days > 45:
                    alerts.append(PortfolioAlert(
                        severity=AlertSeverity.INFO,
                        category="RESEARCH_OBSOLESCENCE",
                        ticker=ticker,
                        message=f"Research thesis for {ticker} is {(today - p_date).days} days old. Refresh scheduled."
                    ))

        return alerts
