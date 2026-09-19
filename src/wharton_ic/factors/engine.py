"""Cross-sectional factor screening, statistical transformations, and multi-factor ranking."""

from typing import Dict, List, Optional, Tuple, Any
import numpy as np
import pandas as pd
from wharton_ic.core.logging import logger

def winsorize_series(series: pd.Series, limits: Tuple[float, float] = (0.02, 0.02)) -> pd.Series:
    """Clips extreme outliers at lower and upper quantile percentiles."""
    lower_quantile = series.quantile(limits[0])
    upper_quantile = series.quantile(1.0 - limits[1])
    return series.clip(lower=lower_quantile, upper=upper_quantile)

def zscore_standardize(series: pd.Series) -> pd.Series:
    """Standardizes a series to mean 0 and standard deviation 1."""
    std = series.std(ddof=1)
    if std == 0 or np.isnan(std):
        return pd.Series(0.0, index=series.index)
    return (series - series.mean()) / std

def sector_neutral_zscore(df: pd.DataFrame, factor_col: str, sector_col: str = "sector") -> pd.Series:
    """Computes z-scores independently within each GICS sector."""
    return df.groupby(sector_col)[factor_col].transform(lambda group: zscore_standardize(winsorize_series(group)))

def percentile_rank(series: pd.Series, ascending: bool = True) -> pd.Series:
    """Computes uniform percentile ranks in [0.0, 1.0]."""
    return series.rank(ascending=ascending, pct=True)

class FactorScreeningEngine:
    """
    Transparent cross-sectional factor evaluation and multi-model screening.
    Implements multiple screening paradigms (Quality-at-Reasonable-Price, Pure Quality, Low Volatility)
    to compare alternatives rather than relying on an arbitrary single model.
    """

    MODELS = {
        "wharton_garp": {
            "quality": 0.35,
            "value": 0.25,
            "growth": 0.20,
            "momentum": 0.10,
            "low_volatility": 0.10
        },
        "pure_quality": {
            "quality": 0.60,
            "value": 0.10,
            "growth": 0.20,
            "momentum": 0.05,
            "low_volatility": 0.05
        },
        "conservative_defensive": {
            "quality": 0.40,
            "value": 0.20,
            "growth": 0.05,
            "momentum": 0.05,
            "low_volatility": 0.30
        },
        "hotchkiss_benchmark": {
            # Included purely as a historical comparison benchmark
            "quality": 0.1666,
            "value": 0.1111,
            "growth": 0.7222,
            "momentum": 0.0,
            "low_volatility": 0.0
        }
    }

    def __init__(self, raw_factor_df: pd.DataFrame):
        self.df = raw_factor_df.copy()

    def process_and_rank(
        self,
        model_name: str = "wharton_garp",
        sector_neutral: bool = True
    ) -> pd.DataFrame:
        """
        Computes standardized factor z-scores, combines them according to the selected model weights,
        and produces a final ranking.
        """
        weights = self.MODELS.get(model_name, self.MODELS["wharton_garp"])
        res = self.df.copy()

        # Handle missing values with sector medians
        for col in ["quality", "value", "growth", "momentum", "low_volatility"]:
            if col in res.columns:
                if "sector" in res.columns:
                    res[col] = res.groupby("sector")[col].transform(lambda x: x.fillna(x.median()))
                res[col] = res[col].fillna(res[col].median())

        # Transform factors
        for col in ["quality", "value", "growth", "momentum", "low_volatility"]:
            if col in res.columns:
                if sector_neutral and "sector" in res.columns:
                    res[f"{col}_z"] = sector_neutral_zscore(res, col, "sector")
                else:
                    res[f"{col}_z"] = zscore_standardize(winsorize_series(res[col]))
                res[f"{col}_pct"] = percentile_rank(res[col])

        # Compute composite score
        composite = pd.Series(0.0, index=res.index)
        for col, weight in weights.items():
            z_col = f"{col}_z"
            if z_col in res.columns:
                composite += weight * res[z_col]

        res["composite_score"] = composite
        res["final_rank"] = res["composite_score"].rank(ascending=False, method="min").astype(int)
        res["screened_percentile"] = percentile_rank(res["composite_score"])

        return res.sort_values("final_rank")

    @classmethod
    def compare_screening_models(cls, raw_df: pd.DataFrame, top_n: int = 15) -> pd.DataFrame:
        """Generates side-by-side comparison of top ranked stocks across all screening models."""
        engine = cls(raw_df)
        comparisons = {}
        for m_name in cls.MODELS.keys():
            ranked = engine.process_and_rank(model_name=m_name)
            top_tickers = ranked.head(top_n)["ticker"].tolist()
            comparisons[m_name] = top_tickers

        return pd.DataFrame(comparisons)
