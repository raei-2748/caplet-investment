"""Configuration manager supporting DEMO vs PRODUCTION execution modes."""

from enum import Enum
import os
from pathlib import Path
from typing import Any, Dict, Optional
import yaml

from wharton_ic.core.exceptions import ProductionMissingMaterialError


class ExecutionMode(str, Enum):
    DEMO = "DEMO"
    PRODUCTION = "PRODUCTION"


class ConfigManager:
    """Manages system configurations and isolates DEMO from PRODUCTION environments."""

    def __init__(self, config_dir: Optional[Path] = None, mode: Optional[ExecutionMode] = None):
        if config_dir is None:
            # Default to root/config
            self.config_dir = Path(__file__).resolve().parent.parent.parent.parent / "config"
        else:
            self.config_dir = Path(config_dir)

        # Mode determination: passed arg > env var > default DEMO
        env_mode = os.getenv("WHARTON_MODE", "DEMO").upper()
        if mode:
            self.mode = mode
        elif env_mode in ["PRODUCTION", "PROD"]:
            self.mode = ExecutionMode.PRODUCTION
        else:
            self.mode = ExecutionMode.DEMO

    @property
    def is_production(self) -> bool:
        return self.mode == ExecutionMode.PRODUCTION

    @property
    def is_demo(self) -> bool:
        return self.mode == ExecutionMode.DEMO

    def load_yaml(self, filename: str) -> Dict[str, Any]:
        """Loads a YAML file from the configuration directory."""
        path = self.config_dir / filename
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    @property
    def models(self) -> Dict[str, Any]:
        return self.load_yaml("models.yaml")

    @property
    def risk(self) -> Dict[str, Any]:
        return self.load_yaml("risk.yaml")

    @property
    def competition(self) -> Dict[str, Any]:
        return self.load_yaml("competition.yaml")

    @property
    def client_mandate(self) -> Dict[str, Any]:
        return self.get_client_mandate_config()

    @property
    def data(self) -> Dict[str, Any]:
        return self.load_yaml("data.yaml")

    @property
    def portfolio(self) -> Dict[str, Any]:
        return self.load_yaml("portfolio.yaml")

    def get_public_rules_config(self) -> Dict[str, Any]:
        return self.load_yaml("wharton_public_2026_27.yaml")

    def get_private_rules_config(self) -> Dict[str, Any]:
        return self.load_yaml("wharton_private_2026_27.yaml")

    def get_client_mandate_config(self) -> Dict[str, Any]:
        if self.is_production:
            mandate = self.load_yaml("client_mandate.yaml")
            if not mandate or mandate.get("client_name") is None:
                raise ProductionMissingMaterialError(
                    "PRODUCTION ERROR: Official client case not loaded into config/client_mandate.yaml. "
                    "Cannot construct client mandate in production mode."
                )
            return mandate
        else:
            # In demo mode, fallback to demo client mandate
            demo_mandate = self.load_yaml("demo_client_mandate.yaml")
            if demo_mandate:
                return demo_mandate
            return self.load_yaml("client_mandate.yaml")

    def ensure_production_ready(self) -> None:
        """Validates that all required official materials exist for production operation."""
        if not self.is_production:
            return

        priv = self.get_private_rules_config()
        if priv.get("status") == "AWAITING_OFFICIAL_MATERIAL":
            raise ProductionMissingMaterialError(
                "PRODUCTION ERROR: Official private competition materials for 2026-2027 have not been ingested. "
                "Production execution is halted until official files are imported via 'wharton-ic ingest-official'."
            )


config_manager = ConfigManager()
