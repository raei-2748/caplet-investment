"""Tests 6-9: DEMO vs PRODUCTION Isolation and Fail-Closed Security."""

import os
import pytest
from pathlib import Path
from wharton_ic.core.config import ConfigManager, ExecutionMode
from wharton_ic.core.exceptions import (
    ProductionMissingMaterialError,
    CouncilPartialError,
)
from wharton_ic.agents.adapter import LLMAdapter
from wharton_ic.reporting_v2.firewall import AIAuthorshipFirewall, AIAuthorshipViolationError
from wharton_ic.reporting_v2.models import ContentBlock, AuthorshipType


def test_6_production_cannot_use_synthetic_financial_data(monkeypatch, tmp_path):
    """TEST 6: Production mode fails if attempting to access unverified/synthetic client mandate."""
    monkeypatch.setenv("WHARTON_MODE", "PRODUCTION")
    # Isolated config dir with only the demo mandate, independent of the real client_mandate.yaml
    demo_src = Path(__file__).resolve().parents[2] / "config" / "demo_client_mandate.yaml"
    (tmp_path / "demo_client_mandate.yaml").write_text(demo_src.read_text(encoding="utf-8"))
    cfg = ConfigManager(config_dir=tmp_path)
    assert cfg.is_production is True
    # client_mandate.yaml without official content raises ProductionMissingMaterialError
    with pytest.raises(ProductionMissingMaterialError) as exc:
        cfg.get_client_mandate_config()
    assert "Official client case not loaded" in str(exc.value)


def test_6b_production_loads_official_client_mandate(monkeypatch):
    """TEST 6b: Production mode loads the ingested official client case, not the demo client."""
    monkeypatch.setenv("WHARTON_MODE", "PRODUCTION")
    mandate = ConfigManager().get_client_mandate_config()
    assert mandate["client_name"] == "Laura Gao"
    assert mandate["human_approved"] is False


def test_7_production_cannot_use_mock_ai(monkeypatch):
    """TEST 7: Production mode raises CouncilPartialError if provider API keys are missing instead of falling back to mock."""
    monkeypatch.setenv("WHARTON_MODE", "PRODUCTION")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    adapter = LLMAdapter(ConfigManager(mode=ExecutionMode.PRODUCTION))
    with pytest.raises(CouncilPartialError) as exc:
        adapter.generate(
            provider="anthropic",
            model="claude-3-5-sonnet-20241022",
            system_prompt="System",
            user_prompt="Evaluate asset",
        )
    assert "ANTHROPIC_API_KEY is not set" in str(exc.value) or "Cannot complete council deliberation in production" in str(exc.value)


def test_8_demo_artifacts_cannot_enter_production_report():
    """TEST 8: AI Authorship Firewall blocks UNKNOWN or demo generated text from entering deliverables."""
    demo_block = ContentBlock(
        block_id="BLK-DEMO-001",
        section_id="strategy",
        authorship_type=AuthorshipType.AI_GENERATED,
        author_identity="mock_llm",
        content_text="This is a synthetic analysis of MSFT.",
    )
    with pytest.raises(AIAuthorshipViolationError) as exc:
        AIAuthorshipFirewall.assert_compliant([demo_block])
    assert "raw AI_GENERATED text" in str(exc.value)


def test_9_production_fails_closed_when_required_inputs_absent(monkeypatch):
    """TEST 9: Production fails closed when private competition materials are awaiting release."""
    monkeypatch.setenv("WHARTON_MODE", "PRODUCTION")
    cfg = ConfigManager(mode=ExecutionMode.PRODUCTION)
    with pytest.raises(ProductionMissingMaterialError) as exc:
        cfg.ensure_production_ready()
    assert "Official private competition materials for 2026-2027 have not been ingested" in str(exc.value)
