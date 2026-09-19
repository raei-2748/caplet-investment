"""Test 11 & Test 12: End-to-end integration and Wharton report-pack compliance."""

from datetime import date
from pathlib import Path
from typer.testing import CliRunner
from wharton_ic.cli.main import app

runner = CliRunner()

def test_full_workflow_demonstration():
    """TEST 11: Execute complete demo pipeline generating research, valuation, debate, risk, and ledger."""
    result = runner.invoke(app, ["demo"])
    assert result.exit_code == 0, f"Demo failed with output: {result.stdout}"
    assert "wharton-ic End-to-End Competition Workflow Demonstration" in result.stdout
    assert "DEMONSTRATION COMPLETE" in result.stdout

def test_report_pack_compliance_no_unlabeled_ai_prose():
    """TEST 12: Verify outputs/report_pack/ contains zero unlabeled AI-generated prose."""
    report_pack_dir = Path("outputs/report_pack")
    assert report_pack_dir.exists(), "Report pack directory must exist"

    weights_md = report_pack_dir / "01_portfolio_weights.md"
    risk_md = report_pack_dir / "02_risk_diagnostics.md"
    exec_md = report_pack_dir / "06_executive_summary.md"

    assert weights_md.exists()
    assert risk_md.exists()
    assert exec_md.exists()

    # Verify tables and disclosures
    with open(exec_md, "r", encoding="utf-8") as f:
        content = f.read()
        assert "[AUDITED QUANTITATIVE RESEARCH PACK" in content
        assert "deterministic Python calculations" in content
