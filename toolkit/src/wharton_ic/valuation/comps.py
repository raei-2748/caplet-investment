"""Comparable company analysis (Comps) deterministic valuation module."""

from datetime import date
from typing import List, Dict, Optional
import numpy as np
from wharton_ic.schemas.valuation import ComparableCompanyValuation

def run_comps_valuation(
    target_ticker: str,
    peer_data: Dict[str, Dict[str, float]],  # peer_ticker -> {'pe': float, 'ev_ebitda': float, 'ps': float}
    target_fundamentals: Dict[str, float],   # {'eps': float, 'ebitda': float, 'revenue': float, 'shares': float, 'debt': float, 'cash': float}
    valuation_date: Optional[date] = None
) -> ComparableCompanyValuation:
    """
    Computes comparable multiples (P/E, EV/EBITDA, P/S) across peers
    and derives implied target equity prices.
    """
    if valuation_date is None:
        valuation_date = date.today()

    peer_tickers = list(peer_data.keys())
    pe_list = [v["pe"] for v in peer_data.values() if "pe" in v and v["pe"] > 0]
    ev_ebitda_list = [v["ev_ebitda"] for v in peer_data.values() if "ev_ebitda" in v and v["ev_ebitda"] > 0]
    ps_list = [v["ps"] for v in peer_data.values() if "ps" in v and v["ps"] > 0]

    med_pe = float(np.median(pe_list)) if pe_list else 20.0
    med_ev_ebitda = float(np.median(ev_ebitda_list)) if ev_ebitda_list else 12.0
    med_ps = float(np.median(ps_list)) if ps_list else 3.0

    mean_pe = float(np.mean(pe_list)) if pe_list else 20.0
    mean_ev_ebitda = float(np.mean(ev_ebitda_list)) if ev_ebitda_list else 12.0
    mean_ps = float(np.mean(ps_list)) if ps_list else 3.0

    eps = target_fundamentals.get("eps", 5.0)
    ebitda = target_fundamentals.get("ebitda", 1e9)
    rev = target_fundamentals.get("revenue", 5e9)
    shares = target_fundamentals.get("shares", 1e8)
    debt = target_fundamentals.get("debt", 2e8)
    cash = target_fundamentals.get("cash", 1e8)

    implied_pe = eps * med_pe
    implied_ev = (ebitda * med_ev_ebitda) - debt + cash
    implied_ev_ebitda = implied_ev / max(shares, 1.0)
    implied_ps = (rev * med_ps) / max(shares, 1.0)

    prices = [p for p in [implied_pe, implied_ev_ebitda, implied_ps] if p > 0]
    composite_price = float(np.mean(prices)) if prices else implied_pe

    return ComparableCompanyValuation(
        target_ticker=target_ticker,
        valuation_date=valuation_date,
        peer_tickers=peer_tickers,
        target_metric_values={"eps": eps, "ebitda": ebitda, "revenue": rev},
        peer_multiples_median={"pe": med_pe, "ev_ebitda": med_ev_ebitda, "ps": med_ps},
        peer_multiples_mean={"pe": mean_pe, "ev_ebitda": mean_ev_ebitda, "ps": mean_ps},
        implied_price_by_pe=float(implied_pe),
        implied_price_by_ev_ebitda=float(implied_ev_ebitda),
        implied_price_by_ps=float(implied_ps),
        composite_implied_price=float(composite_price)
    )
