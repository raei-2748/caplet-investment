"""Publication-grade financial visualization pipeline for Wharton Report Packs."""

from pathlib import Path
from typing import Dict, List, Optional, Any
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Clean institutional style configuration
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Helvetica", "Arial"]
plt.rcParams["axes.edgecolor"] = "#cccccc"
plt.rcParams["axes.linewidth"] = 0.8

class PortfolioVisualizer:
    """Generates publication-quality financial charts for student competition reports."""

    def __init__(self, output_dir: Optional[Path] = None):
        self.output_dir = output_dir or (Path(__file__).resolve().parents[3] / "outputs" / "charts")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def plot_allocation_and_sectors(
        self,
        weights: Dict[str, float],
        sector_map: Dict[str, str],
        filename: str = "allocation_pie_and_sectors.png"
    ) -> Path:
        """Plots asset allocation alongside sector breakdown against the 25% Wharton cap."""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # 1. Asset Weights Bar Chart
        sorted_w = sorted(weights.items(), key=lambda x: x[1], reverse=True)
        tickers = [x[0] for x in sorted_w if x[1] > 0.005]
        vals = [x[1] * 100.0 for x in sorted_w if x[1] > 0.005]

        axes[0].barh(tickers[::-1], vals[::-1], color="#1f77b4", edgecolor="#0e4b75", height=0.6)
        axes[0].set_xlabel("Portfolio Weight (%)", fontsize=11, fontweight="bold")
        axes[0].set_title("Target Portfolio Asset Allocation", fontsize=12, fontweight="bold", pad=12)
        axes[0].axvline(15.0, color="#d62728", linestyle="--", linewidth=1.2, label="Wharton Max Asset Limit (15%)")
        axes[0].legend(loc="lower right", frameon=True)
        axes[0].xaxis.set_major_formatter(mtick.PercentFormatter())

        # 2. Sector Exposure Bar Chart
        sector_totals: Dict[str, float] = {}
        for t, w in weights.items():
            s = sector_map.get(t, "Unclassified")
            sector_totals[s] = sector_totals.get(s, 0.0) + w

        sorted_s = sorted(sector_totals.items(), key=lambda x: x[1], reverse=True)
        s_names = [x[0] for x in sorted_s]
        s_vals = [x[1] * 100.0 for x in sorted_s]

        axes[1].barh(s_names[::-1], s_vals[::-1], color="#2ca02c", edgecolor="#1b631b", height=0.6)
        axes[1].set_xlabel("Sector Allocation (%)", fontsize=11, fontweight="bold")
        axes[1].set_title("GICS Sector Exposure vs. Wharton Cap", fontsize=12, fontweight="bold", pad=12)
        axes[1].axvline(25.0, color="#d62728", linestyle="--", linewidth=1.2, label="Wharton Max Sector Limit (25%)")
        axes[1].legend(loc="lower right", frameon=True)
        axes[1].xaxis.set_major_formatter(mtick.PercentFormatter())

        plt.tight_layout()
        out_path = self.output_dir / filename
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        return out_path

    def plot_optimizer_comparison(
        self,
        metrics_df: pd.DataFrame,
        filename: str = "efficient_frontier_and_models.png"
    ) -> Path:
        """Plots annualized risk vs return across all 8 optimization paradigms."""
        fig, ax = plt.subplots(figsize=(10, 6))

        vols = metrics_df["Annualized Volatility"] * 100.0
        cagrs = metrics_df["CAGR"] * 100.0
        labels = metrics_df["Method"]

        scatter = ax.scatter(vols, cagrs, c=metrics_df["Sharpe Ratio"], cmap="viridis", s=150, edgecolor="black", zorder=3)
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label("Sharpe Ratio", fontsize=11, fontweight="bold")

        for i, txt in enumerate(labels):
            ax.annotate(
                txt,
                (vols.iloc[i], cagrs.iloc[i]),
                textcoords="offset points",
                xytext=(8, 5),
                fontsize=9,
                fontweight="bold"
            )

        ax.set_xlabel("Annualized Volatility (%)", fontsize=11, fontweight="bold")
        ax.set_ylabel("Expected CAGR (%)", fontsize=11, fontweight="bold")
        ax.set_title("Portfolio Optimization Model Comparison (Risk vs. Return)", fontsize=13, fontweight="bold", pad=12)
        ax.xaxis.set_major_formatter(mtick.PercentFormatter())
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())

        plt.tight_layout()
        out_path = self.output_dir / filename
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        return out_path

    def plot_correlation_heatmap(
        self,
        returns_df: pd.DataFrame,
        filename: str = "correlation_heatmap.png"
    ) -> Path:
        """Plots clean correlation matrix of selected portfolio constituents."""
        corr = returns_df.corr()
        n = len(corr)

        fig, ax = plt.subplots(figsize=(max(8, n * 0.7), max(7, n * 0.6)))
        cax = ax.matshow(corr, cmap="coolwarm", vmin=-1.0, vmax=1.0)
        fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)

        ax.set_xticks(range(n))
        ax.set_yticks(range(n))
        ax.set_xticklabels(corr.columns, rotation=45, ha="left", fontsize=9, fontweight="bold")
        ax.set_yticklabels(corr.index, fontsize=9, fontweight="bold")

        # Annotate matrix cells
        for i in range(n):
            for j in range(n):
                ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", color="black" if abs(corr.iloc[i, j]) < 0.6 else "white", fontsize=8)

        ax.set_title("Portfolio Asset Correlation Matrix", fontsize=12, fontweight="bold", pad=20)
        plt.tight_layout()
        out_path = self.output_dir / filename
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        return out_path

    def plot_monte_carlo_cone(
        self,
        mc_results: Dict[str, Any],
        starting_capital: float = 100000.0,
        target_capital: float = 109000.0,
        filename: str = "monte_carlo_cone.png"
    ) -> Path:
        """Plots fat-tailed Student-t Monte Carlo forward projection cone."""
        fig, ax = plt.subplots(figsize=(10, 6))

        days = mc_results["sample_path_dates"]
        p05 = mc_results["p05_path"]
        p50 = mc_results["median_path"]
        p95 = mc_results["p95_path"]

        ax.fill_between(days, p05, p95, color="#1f77b4", alpha=0.20, label="5th–95th Percentile Range")
        ax.plot(days, p50, color="#1f77b4", linewidth=2.5, label=f"Median Path (${mc_results['percentiles_ending_wealth']['p50_median']:,.0f})")
        ax.axhline(starting_capital, color="#666666", linestyle=":", label="Starting Capital ($100,000)")
        ax.axhline(target_capital, color="#2ca02c", linestyle="--", linewidth=1.5, label=f"Client Target 9% (${target_capital:,.0f})")

        ax.set_xlabel("Trading Days Forward (1 Year)", fontsize=11, fontweight="bold")
        ax.set_ylabel("Portfolio Capital ($ USD)", fontsize=11, fontweight="bold")
        prob_str = f"P(Goal Met) = {mc_results['probability_goal_attained']*100:.1f}%, P(DD > 20%) = {mc_results['probability_drawdown_gt_20pct']*100:.1f}%"
        ax.set_title(f"Fat-Tailed Monte Carlo Simulation (5,000 Paths)\n{prob_str}", fontsize=12, fontweight="bold", pad=12)
        ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("${x:,.0f}"))
        ax.legend(loc="upper left", frameon=True)

        plt.tight_layout()
        out_path = self.output_dir / filename
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        return out_path

    def plot_walk_forward_equity_curve(
        self,
        strategy_curve: pd.Series,
        benchmark_curve: Optional[pd.Series] = None,
        equal_weight_curve: Optional[pd.Series] = None,
        filename: str = "walk_forward_equity_curve.png"
    ) -> Path:
        """Plots out-of-sample walk-forward equity curves against baselines."""
        fig, ax = plt.subplots(figsize=(11, 6))

        ax.plot(strategy_curve.index, strategy_curve.values, color="#1f77b4", linewidth=2.5, label="Wharton HRP Portfolio")
        if equal_weight_curve is not None:
            ax.plot(equal_weight_curve.index, equal_weight_curve.values, color="#ff7f0e", linestyle="--", linewidth=1.5, label="Equal Weight Baseline")
        if benchmark_curve is not None:
            ax.plot(benchmark_curve.index, benchmark_curve.values, color="#2ca02c", linestyle=":", linewidth=1.5, label="SPY Benchmark")

        ax.set_xlabel("Out-of-Sample Date", fontsize=11, fontweight="bold")
        ax.set_ylabel("Normalized Growth of $1.00", fontsize=11, fontweight="bold")
        ax.set_title("Out-of-Sample Walk-Forward Backtest Performance", fontsize=13, fontweight="bold", pad=12)
        ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("${x:.2f}"))
        ax.legend(loc="upper left", frameon=True)

        plt.tight_layout()
        out_path = self.output_dir / filename
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        return out_path

visualizer = PortfolioVisualizer()
