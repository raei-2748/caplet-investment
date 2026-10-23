# Mathematical & Financial Methodology: `wharton-ic`

This document details the exact mathematical, statistical, and econometric formulations implemented in `wharton-ic`.

---

## 1. Valuation Mathematics

### 1.1 Weighted Average Cost of Capital (WACC)
$$\text{WACC} = \left(\frac{E}{V}\right) R_e + \left(\frac{D}{V}\right) R_d (1 - t_c)$$
Where:
- $E$: Market capitalization of equity ($P \times \text{Shares}$)
- $D$: Total outstanding interest-bearing debt
- $V = E + D$: Enterprise capital base
- $t_c$: Marginal corporate tax rate ($21\%$)
- $R_d$: Pre-tax cost of debt
- $R_e$: Cost of equity computed via the Capital Asset Pricing Model (CAPM):
  $$R_e = R_f + \beta_i \times \text{ERP}$$
  - $R_f$: 10-Year US Treasury risk-free rate ($4.25\%$)
  - $\beta_i$: 5-year monthly equity beta vs. S&P 500
  - $\text{ERP}$: Historical Equity Risk Premium ($5.5\%$)

### 1.2 Multi-Stage Discounted Cash Flow (DCF)
Enterprise Value ($\text{EV}$) is the sum of discounted forecast Free Cash Flows ($\text{FCF}$) and the discounted Terminal Value ($\text{TV}$):
$$\text{EV} = \sum_{t=1}^{N} \frac{\text{FCF}_t}{(1 + \text{WACC})^t} + \frac{\text{TV}_N}{(1 + \text{WACC})^N}$$

Free Cash Flow for year $t$:
$$\text{FCF}_t = \text{NOPAT}_t - \text{Reinvestment}_t$$
Where:
$$\text{NOPAT}_t = \text{EBIT}_t \times (1 - t_c)$$
$$\text{Reinvestment}_t = \text{CapEx}_t - \text{D\&A}_t + \Delta \text{NWC}_t$$

Terminal Value is modeled via the Gordon Growth Model:
$$\text{TV}_N = \frac{\text{FCF}_N \times (1 + g)}{\text{WACC} - g}$$
Where $g$ is the conservative perpetual terminal growth rate ($2.0\% - 3.0\%$).

Implied Share Price:
$$P_{\text{implied}} = \frac{\text{EV} - \text{Total Debt} + \text{Cash}}{\text{Shares Outstanding}}$$

### 1.3 Reverse DCF Root Solving
Given market price $P_{\text{market}}$, solve numerically for the implied growth rate $g^*$ such that:
$$f(g^*) = P_{\text{implied}}(g^*) - P_{\text{market}} = 0$$
Using Brent's method with bracket $[-0.05, \text{WACC} - 0.005]$.

---

## 2. Factor Standardization & Screening

### 2.1 Winsorization
Extreme cross-sectional outliers are clipped at the 2nd and 98th percentiles:
$$\tilde{x}_i = \min\left(\max(x_i, Q_{0.02}), Q_{0.98}\right)$$

### 2.2 Sector-Neutral Z-Score Standardization
Within each GICS sector $S$:
$$z_{i, S} = \frac{\tilde{x}_i - \mu_S}{\sigma_S}$$
Where $\mu_S$ and $\sigma_S$ are the mean and standard deviation of factor values across all approved securities in sector $S$.

### 2.3 Composite Factor Scoring
$$\text{Score}_i = \sum_{k \in \{\text{Quality}, \text{Value}, \text{Growth}, \text{Mom}, \text{LowVol}\}} w_k \cdot z_{i, k}$$

---

## 3. Quantitative Risk Decomposition

### 3.1 Portfolio Returns & Volatility
$$r_{p, t} = \sum_{i=1}^{N} w_i r_{i, t} = w^T r_t$$
$$\sigma_p = \sqrt{w^T \Sigma w} \times \sqrt{252}$$
Where $\Sigma$ is the annualized covariance matrix of asset returns.

### 3.2 Marginal Contribution to Risk (MCR) & Percent Contribution (PCR)
$$\text{MCR}_i = \frac{\partial \sigma_p}{\partial w_i} = \frac{(\Sigma w)_i}{\sigma_p}$$
$$\text{PCR}_i = \frac{w_i \times \text{MCR}_i}{\sigma_p} \quad \text{such that} \quad \sum_{i=1}^{N} \text{PCR}_i = 1.0$$

### 3.3 Conditional Value at Risk (CVaR / Expected Shortfall)
At confidence level $\alpha = 0.95$:
$$\text{VaR}_\alpha = -F^{-1}(1 - \alpha)$$
$$\text{CVaR}_\alpha = -\mathbb{E}\left[r_p \mid r_p \le -\text{VaR}_\alpha\right] = \frac{1}{1 - \alpha} \int_{0}^{1 - \alpha} -F^{-1}(u) \, du$$

### 3.4 Effective Number of Constituents (ENC)
Measures true portfolio diversification via the inverse Herfindahl index:
$$\text{ENC} = \frac{1}{\sum_{i=1}^{N} w_i^2}$$
For equal weights $w_i = 1/N$, $\text{ENC} = N$. For concentrated portfolios, $\text{ENC} \ll N$.

---

## 4. Portfolio Optimization & Constraints

### 4.1 Hierarchical Risk Parity (HRP)
HRP (López de Prado, 2016) resolves the matrix inversion instabilities of classical Markowitz quadratic optimization:
1. **Tree Clustering**: Computes correlation distance $d_{i, j} = \sqrt{\frac{1}{2}(1 - \rho_{i, j})}$ and clusters assets hierarchically.
2. **Quasi-Diagonalization**: Reorders the covariance matrix so similar assets are placed adjacent to each other.
3. **Recursive Bisection**: Recursively splits the tree into subsets $V_1$ and $V_2$, allocating capital inversely proportional to their cluster variance:
   $$\alpha_1 = 1 - \frac{V_1}{V_1 + V_2}, \quad \alpha_2 = \frac{V_1}{V_1 + V_2}$$

### 4.2 Convex Constraint Projection (CVXPY)
To enforce Wharton's strict competition rules ($w_i \in [0.025, 0.150]$ and $\sum_{i \in \text{Sector}} w_i \le 0.25$):
$$\min_{w} \frac{1}{2} \|w - w_{\text{raw}}\|^2_2$$
$$\text{subject to} \quad \sum_{i=1}^{N} w_i = 1.0 - c_{\text{cash}}$$
$$w_{\min} \le w_i \le w_{\max} \quad \forall i$$
$$\sum_{j \in S_k} w_j \le \text{Cap}_{\text{sector}} \quad \forall k$$

---

## 5. Fat-Tailed Monte Carlo Simulation
Rather than naive Gaussian Brownian motion, we sample returns from a fat-tailed Student-t distribution with $\nu = 5$ degrees of freedom to capture financial leptokurtosis:
$$r_{p, t}^{(k)} \sim t_{\nu}\left(\mu, \sigma \sqrt{\frac{\nu - 2}{\nu}}\right)$$
Across 5,000 paths of 252 trading days:
$$\text{Wealth}_{T}^{(k)} = W_0 \prod_{t=1}^{252} \left(1 + r_{p, t}^{(k)}\right)$$
$$P(\text{Goal Met}) = \frac{1}{5000} \sum_{k=1}^{5000} \mathbb{I}\left(\text{Wealth}_T^{(k)} \ge W_{\text{target}}\right)$$
$$P(\text{Drawdown} > 20\%) = \frac{1}{5000} \sum_{k=1}^{5000} \mathbb{I}\left(\min_t \text{DD}_t^{(k)} \le -0.20\right)$$
