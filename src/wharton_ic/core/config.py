"""Configuration loader and schema validator."""

import os
from pathlib import Path
from typing import Any, Dict, Optional
import yaml
from wharton_ic.core.exceptions import ConfigurationError

class ConfigManager:
    """Manages loading, validating, and caching YAML configuration files."""

    def __init__(self, config_dir: Optional[Path] = None):
        if config_dir is None:
            # Default to repo root config/ directory
            self.config_dir = Path(__file__).resolve().parents[3] / "config"
        else:
            self.config_dir = Path(config_dir)
            
        self._configs: Dict[str, Dict[str, Any]] = {}

    def get_config(self, name: str) -> Dict[str, Any]:
        """Loads and returns a YAML configuration by name (e.g. 'client_mandate', 'risk')."""
        if name in self._configs:
            return self._configs[name]

        config_path = self.config_dir / f"{name}.yaml"
        if not config_path.exists():
            raise ConfigurationError(f"Configuration file not found: {config_path}")

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            self._configs[name] = data
            return data
        except yaml.YAMLError as e:
            raise ConfigurationError(f"Error parsing YAML file {config_path}: {e}")

    @property
    def client_mandate(self) -> Dict[str, Any]:
        return self.get_config("client_mandate")

    @property
    def competition(self) -> Dict[str, Any]:
        return self.get_config("competition")

    @property
    def risk(self) -> Dict[str, Any]:
        return self.get_config("risk")

    @property
    def models(self) -> Dict[str, Any]:
        return self.get_config("models")

    @property
    def data(self) -> Dict[str, Any]:
        return self.get_config("data")

    @property
    def portfolio(self) -> Dict[str, Any]:
        return self.get_config("portfolio")

# Global singleton instance
config_manager = ConfigManager()
