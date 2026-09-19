"""Default verified approved universe representing typical Wharton competition securities."""

from typing import List
from wharton_ic.schemas.security import SecurityMetadata, AssetType

DEFAULT_APPROVED_SECURITIES: List[SecurityMetadata] = [
    # Information Technology
    SecurityMetadata(
        ticker="MSFT",
        name="Microsoft Corporation",
        asset_type=AssetType.EQUITY,
        gics_sector="Information Technology",
        gics_industry="Systems Software",
        market_cap_usd=3.1e12,
        average_daily_volume_usd=8e9
    ),
    SecurityMetadata(
        ticker="AAPL",
        name="Apple Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Information Technology",
        gics_industry="Technology Hardware, Storage & Peripherals",
        market_cap_usd=3.4e12,
        average_daily_volume_usd=10e9
    ),
    SecurityMetadata(
        ticker="NVDA",
        name="NVIDIA Corporation",
        asset_type=AssetType.EQUITY,
        gics_sector="Information Technology",
        gics_industry="Semiconductors",
        market_cap_usd=2.8e12,
        average_daily_volume_usd=15e9
    ),
    SecurityMetadata(
        ticker="ASML",
        name="ASML Holding N.V.",
        asset_type=AssetType.EQUITY,
        gics_sector="Information Technology",
        gics_industry="Semiconductor Equipment",
        market_cap_usd=3.5e11,
        average_daily_volume_usd=1.2e9
    ),

    # Health Care
    SecurityMetadata(
        ticker="JNJ",
        name="Johnson & Johnson",
        asset_type=AssetType.EQUITY,
        gics_sector="Health Care",
        gics_industry="Pharmaceuticals",
        market_cap_usd=3.8e11,
        average_daily_volume_usd=1.5e9
    ),
    SecurityMetadata(
        ticker="UNH",
        name="UnitedHealth Group Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Health Care",
        gics_industry="Managed Health Care",
        market_cap_usd=5.2e11,
        average_daily_volume_usd=2.0e9
    ),
    SecurityMetadata(
        ticker="LLY",
        name="Eli Lilly and Company",
        asset_type=AssetType.EQUITY,
        gics_sector="Health Care",
        gics_industry="Pharmaceuticals",
        market_cap_usd=8.2e11,
        average_daily_volume_usd=3.5e9
    ),
    SecurityMetadata(
        ticker="ABT",
        name="Abbott Laboratories",
        asset_type=AssetType.EQUITY,
        gics_sector="Health Care",
        gics_industry="Health Care Equipment",
        market_cap_usd=2.0e11,
        average_daily_volume_usd=8e8
    ),

    # Financials
    SecurityMetadata(
        ticker="JPM",
        name="JPMorgan Chase & Co.",
        asset_type=AssetType.EQUITY,
        gics_sector="Financials",
        gics_industry="Diversified Banks",
        market_cap_usd=6.1e11,
        average_daily_volume_usd=2.5e9
    ),
    SecurityMetadata(
        ticker="V",
        name="Visa Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Financials",
        gics_industry="Transaction & Payment Processing",
        market_cap_usd=5.5e11,
        average_daily_volume_usd=1.8e9
    ),
    SecurityMetadata(
        ticker="MA",
        name="Mastercard Incorporated",
        asset_type=AssetType.EQUITY,
        gics_sector="Financials",
        gics_industry="Transaction & Payment Processing",
        market_cap_usd=4.2e11,
        average_daily_volume_usd=1.4e9
    ),

    # Consumer Staples
    SecurityMetadata(
        ticker="PG",
        name="Procter & Gamble Company",
        asset_type=AssetType.EQUITY,
        gics_sector="Consumer Staples",
        gics_industry="Household Products",
        market_cap_usd=3.9e11,
        average_daily_volume_usd=1.2e9
    ),
    SecurityMetadata(
        ticker="COST",
        name="Costco Wholesale Corporation",
        asset_type=AssetType.EQUITY,
        gics_sector="Consumer Staples",
        gics_industry="Hypermarkets & Supercenters",
        market_cap_usd=3.8e11,
        average_daily_volume_usd=1.5e9
    ),
    SecurityMetadata(
        ticker="KO",
        name="The Coca-Cola Company",
        asset_type=AssetType.EQUITY,
        gics_sector="Consumer Staples",
        gics_industry="Soft Drinks & Non-alcoholic Beverages",
        market_cap_usd=2.7e11,
        average_daily_volume_usd=9e8
    ),

    # Consumer Discretionary
    SecurityMetadata(
        ticker="AMZN",
        name="Amazon.com, Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Consumer Discretionary",
        gics_industry="Broadline Retail",
        market_cap_usd=1.9e12,
        average_daily_volume_usd=6e9
    ),
    SecurityMetadata(
        ticker="HD",
        name="The Home Depot, Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Consumer Discretionary",
        gics_industry="Home Improvement Retail",
        market_cap_usd=3.7e11,
        average_daily_volume_usd=1.3e9
    ),

    # Communication Services
    SecurityMetadata(
        ticker="GOOGL",
        name="Alphabet Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Communication Services",
        gics_industry="Interactive Media & Services",
        market_cap_usd=2.1e12,
        average_daily_volume_usd=4e9
    ),
    SecurityMetadata(
        ticker="DIS",
        name="The Walt Disney Company",
        asset_type=AssetType.EQUITY,
        gics_sector="Communication Services",
        gics_industry="Movies & Entertainment",
        market_cap_usd=1.8e11,
        average_daily_volume_usd=9e8
    ),

    # Industrials
    SecurityMetadata(
        ticker="CAT",
        name="Caterpillar Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Industrials",
        gics_industry="Construction Machinery & Heavy Transportation",
        market_cap_usd=1.8e11,
        average_daily_volume_usd=8e8
    ),
    SecurityMetadata(
        ticker="UNP",
        name="Union Pacific Corporation",
        asset_type=AssetType.EQUITY,
        gics_sector="Industrials",
        gics_industry="Rail Transportation",
        market_cap_usd=1.5e11,
        average_daily_volume_usd=6e8
    ),
    SecurityMetadata(
        ticker="HON",
        name="Honeywell International Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Industrials",
        gics_industry="Industrial Conglomerates",
        market_cap_usd=1.4e11,
        average_daily_volume_usd=5e8
    ),

    # Utilities & Clean Energy
    SecurityMetadata(
        ticker="NEE",
        name="NextEra Energy, Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Utilities",
        gics_industry="Electric Utilities",
        market_cap_usd=1.6e11,
        average_daily_volume_usd=8e8
    ),
    SecurityMetadata(
        ticker="SO",
        name="The Southern Company",
        asset_type=AssetType.EQUITY,
        gics_sector="Utilities",
        gics_industry="Electric Utilities",
        market_cap_usd=9.5e10,
        average_daily_volume_usd=4e8
    ),

    # Materials
    SecurityMetadata(
        ticker="LIN",
        name="Linde plc",
        asset_type=AssetType.EQUITY,
        gics_sector="Materials",
        gics_industry="Industrial Gases",
        market_cap_usd=2.1e11,
        average_daily_volume_usd=7e8
    ),
    SecurityMetadata(
        ticker="SHW",
        name="The Sherwin-Williams Company",
        asset_type=AssetType.EQUITY,
        gics_sector="Materials",
        gics_industry="Specialty Chemicals",
        market_cap_usd=8.5e10,
        average_daily_volume_usd=3.5e8
    ),

    # Energy
    SecurityMetadata(
        ticker="XOM",
        name="Exxon Mobil Corporation",
        asset_type=AssetType.EQUITY,
        gics_sector="Energy",
        gics_industry="Integrated Oil & Gas",
        market_cap_usd=4.8e11,
        average_daily_volume_usd=2e9
    ),
    SecurityMetadata(
        ticker="CVX",
        name="Chevron Corporation",
        asset_type=AssetType.EQUITY,
        gics_sector="Energy",
        gics_industry="Integrated Oil & Gas",
        market_cap_usd=2.7e11,
        average_daily_volume_usd=1.2e9
    ),

    # Real Estate
    SecurityMetadata(
        ticker="PLD",
        name="Prologis, Inc.",
        asset_type=AssetType.EQUITY,
        gics_sector="Real Estate",
        gics_industry="Industrial REITs",
        market_cap_usd=1.1e11,
        average_daily_volume_usd=5e8
    ),
    SecurityMetadata(
        ticker="AMT",
        name="American Tower Corporation",
        asset_type=AssetType.EQUITY,
        gics_sector="Real Estate",
        gics_industry="Telecom Tower REITs",
        market_cap_usd=9.2e10,
        average_daily_volume_usd=4.5e8
    ),

    # Benchmark ETFs
    SecurityMetadata(
        ticker="SPY",
        name="SPDR S&P 500 ETF Trust",
        asset_type=AssetType.ETF,
        gics_sector="Broad Market",
        gics_industry="Large Cap Equity",
        market_cap_usd=5.5e11,
        average_daily_volume_usd=3e10
    ),
    SecurityMetadata(
        ticker="ACWI",
        name="iShares MSCI ACWI ETF",
        asset_type=AssetType.ETF,
        gics_sector="Broad Market",
        gics_industry="Global Equity",
        market_cap_usd=2.0e10,
        average_daily_volume_usd=5e8
    ),
]
