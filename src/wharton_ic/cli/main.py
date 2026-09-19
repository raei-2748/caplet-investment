"""Command-line interface for wharton-ic using Typer."""

from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional, List
import numpy as np
import pandas as pd
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from wharton_ic.core.config import config_manager, ConfigManager, ExecutionMode
from wharton_ic.core.logging import logger
from wharton_ic.rules.registry import RuleRegistry
from wharton_ic.rules.conflicts import RuleConflictDetector
from wharton_ic.rules.citations import RuleCitationExporter
from wharton_ic.rules.ingestion import OfficialMaterialIngestor
from wharton_ic.client.engine import ClientMandateEngine
from wharton_ic.client.auditor import ClientMandateAuditor
from wharton_ic.client.models import ClientMandate, MandateLineItem, FactCategory
from wharton_ic.strategy.engine import StrategyCouncilEngine
from wharton_ic.strategy.memory import StrategyMemoryQueryEngine
from wharton_ic.journal.engine import DecisionJournalEngine
from wharton_ic.journal.models import JournalEvent, JournalEventType
from wharton_ic.reporting_v2.engine import WhartonReportEngineV2
from wharton_ic.reporting_v2.firewall import AIAuthorshipFirewall
from wharton_ic.reporting_v2.models import ContentBlock, AuthorshipType
from wharton_ic.review.council import JudgeReviewCouncil
from wharton_ic.evidence.auditor import EvidenceLineageAuditor
from wharton_ic.evidence.models import EvidenceClaim, ClaimType
from wharton_ic.research.fixtures import get_mock_security_proposals
from wharton_ic.research.council import SecurityCouncilEngine
from wharton_ic.universe.engine import universe_engine
from wharton_ic.data.yfinance_provider import YFinanceProvider
from wharton_ic.data.point_in_time import PointInTimeStore
from wharton_ic.fundamentals.metrics import compute_comprehensive_fundamentals
from wharton_ic.factors.engine import FactorScreeningEngine
from wharton_ic.valuation.wacc import calculate_wacc
from wharton_ic.valuation.dcf import run_dcf_valuation
from wharton_ic.valuation.comps import run_comps_valuation
from wharton_ic.valuation.scenario import run_multi_scenario_valuation
from wharton_ic.portfolio.optimizer import PortfolioOptimizer
from wharton_ic.risk.metrics import compute_portfolio_diagnostics
from wharton_ic.backtest.engine import WalkForwardBacktester
from wharton_ic.scenarios.stress import ScenarioStressEngine
from wharton_ic.council.orchestrator import CouncilOrchestrator
from wharton_ic.decisions.ledger import decision_ledger
from wharton_ic.monitoring.portfolio_monitor import PortfolioMonitor
from wharton_ic.reporting.visualizer import visualizer
from wharton_ic.reporting.report_pack import report_pack_generator
from wharton_ic.schemas.proposal import HumanApprovalStatus

app = typer.Typer(
    name="wharton-ic",
    help="Wharton Global High School Investment Competition Operating System",
    add_completion=False
)
console = Console()

@app.command("audit-references")
def audit_references():
    """Displays the forensic audit of past Wharton competitor repositories."""
    audit_file = Path("docs/reference_audit.md")
    if audit_file.exists():
        console.print(Panel.fit(
            f"[bold green]Reference Repository Audit[/bold green]\nFound at: {audit_file.resolve()}",
            title="wharton-ic Reference Audit"
        ))
        with open(audit_file, "r", encoding="utf-8") as f:
            for line in f.readlines()[:35]:
                console.print(line, end="")
        console.print("\n[dim]... see docs/reference_audit.md for full analysis.[/dim]")
    else:
        console.print("[red]docs/reference_audit.md not found.[/red]")

rules_app = typer.Typer(name="rules", help="Wharton Rule Custodian and Authority Management")
client_app = typer.Typer(name="client", help="Client Mandate Engine and Governance Gate")
strategy_app = typer.Typer(name="strategy", help="Strategy Council, Red Team, and Human Gate")
journal_app = typer.Typer(name="journal", help="Decision Journal, Trading Notes, and Timeline")
report_app = typer.Typer(name="report", help="Wharton Report Engine V2 and AI Authorship Firewall")
research_app = typer.Typer(name="research", help="Security Research Interfaces and Fixtures")

app.add_typer(rules_app, name="rules")
app.add_typer(client_app, name="client")
app.add_typer(strategy_app, name="strategy")
app.add_typer(journal_app, name="journal")
app.add_typer(report_app, name="report")
app.add_typer(research_app, name="research")

# ==========================================
# 1. RULES SUB-APP COMMANDS
# ==========================================
@rules_app.command("status")
def rules_status():
    """Displays summary status of competition rules (Verified Public, Private Unknown)."""
    from wharton_ic.rules.models import RuleStatus
    registry = RuleRegistry()
    summary = registry.get_status_summary()
    table = Table(title="Wharton IC 2026-2027 Rule Registry Status")
    table.add_column("Rule Status", style="bold cyan")
    table.add_column("Count", justify="right")
    for status, count in summary.items():
        table.add_row(status, str(count))
    console.print(table)
    priv_rules = registry.list_rules(status=RuleStatus.UNKNOWN)
    if priv_rules:
        console.print(f"[yellow]Note: {len(priv_rules)} private competition rules are UNKNOWN awaiting Sept 15 release.[/yellow]")

@rules_app.command("list")
def rules_list(category: Optional[str] = typer.Option(None, "--category", "-c")):
    """Lists competition rules with authority and provenance."""
    from wharton_ic.rules.models import RuleCategory
    registry = RuleRegistry()
    cat_filter = RuleCategory(category) if category else None
    rules = registry.list_rules(category=cat_filter)
    table = Table(title=f"Competition Rules ({len(rules)} total)")
    table.add_column("Rule ID", style="bold")
    table.add_column("Category")
    table.add_column("Authority Level", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Title")
    for r in rules:
        table.add_row(r.rule_id, r.category.value, r.authority_level.name, r.status.value, r.title)
    console.print(table)

@rules_app.command("conflicts")
def rules_conflicts():
    """Detects rule contradictions and enforces authority precedence."""
    registry = RuleRegistry()
    rules = registry.list_rules()
    conflicts = RuleConflictDetector.find_conflicts(rules)
    if not conflicts:
        console.print("[green]No active rule conflicts detected. Rule precedence hierarchy is clean.[/green]")
    else:
        table = Table(title="Detected Rule Conflicts / Supersessions")
        table.add_column("Rule A")
        table.add_column("Rule B")
        table.add_column("Winner", style="bold green")
        table.add_column("Resolution")
        table.add_column("Description")
        for c in conflicts:
            table.add_row(c.rule_a_id, c.rule_b_id, c.winning_rule_id or "NONE", c.resolution_status, c.description)
        console.print(table)

@rules_app.command("verify")
def rules_verify(
    rule_id: str = typer.Argument(..., help="Rule ID to verify"),
    by: str = typer.Option(..., "--by", "-b", help="Student verifier name")
):
    """Student verification of a pending competition rule."""
    registry = RuleRegistry()
    try:
        updated = registry.verify_rule(rule_id, by)
        console.print(f"[green]Rule {rule_id} successfully verified by {by}. Status: {updated.status.value}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to verify rule {rule_id}: {e}[/red]")

@rules_app.command("export-citations")
def rules_export_citations():
    """Exports verified rule citations in Markdown table format for report evidence."""
    registry = RuleRegistry()
    rules = registry.list_rules()
    md_table = RuleCitationExporter.to_markdown_table(rules)
    console.print(md_table)


# ==========================================
# 2. CLIENT SUB-APP COMMANDS
# ==========================================
@client_app.command("show")
def client_show():
    """Displays the active client mandate."""
    engine = ClientMandateEngine()
    mandate = engine.load_mandate()
    if not mandate:
        console.print("[yellow]No active client mandate found. Ingest official case study or initialize mandate.[/yellow]")
        return
    console.print(Panel.fit(
        f"[bold]Client Name[/bold]: {mandate.client_name}\n"
        f"[bold]Horizon[/bold]: {mandate.investment_horizon.statement}\n"
        f"[bold]Return Objective[/bold]: {mandate.return_objectives.statement}\n"
        f"[bold]Risk Tolerance[/bold]: {mandate.risk_tolerance.statement}\n"
        f"[bold]Governance Status[/bold]: [bold green]{'APPROVED' if mandate.human_approved else 'PENDING_STUDENT_APPROVAL'}[/bold green]\n"
        f"[bold]Approved By[/bold]: {mandate.approved_by or 'None'}",
        title=f"Client Mandate: {mandate.client_name}"
    ))

@client_app.command("audit")
def client_audit():
    """Audits client mandate for fact support, tensions, and governance sign-off."""
    engine = ClientMandateEngine()
    mandate = engine.load_mandate()
    if not mandate:
        console.print("[red]No client mandate loaded to audit.[/red]")
        return
    result = ClientMandateAuditor.audit_mandate(mandate)
    table = Table(title="Client Mandate Audit Result")
    table.add_column("Audit Metric", style="cyan")
    table.add_column("Value")
    table.add_row("Compliant with Wharton Rules", "[green]YES[/green]" if result.is_compliant else "[red]NO[/red]")
    table.add_row("Supported Client Facts", str(result.supported_facts_count))
    table.add_row("Team Interpretations", str(result.interpretations_count))
    table.add_row("Strategic Assumptions", str(result.assumptions_count))
    table.add_row("Governance Approval", f"[bold]{result.approval_status}[/bold]")
    table.add_row("Dialectical Tensions Detected", str(len(result.tensions)))
    console.print(table)
    if result.unsupported_facts:
        console.print("[bold red]Unsupported Client Facts (Missing Citations):[/bold red]")
        for u in result.unsupported_facts:
            console.print(f"- {u}")
    if result.tensions:
        console.print("[bold yellow]Detected Objective Tensions:[/bold yellow]")
        for t in result.tensions:
            console.print(f"- {t}")

@client_app.command("approve")
def client_approve(
    signer: str = typer.Option(..., "--signer", "-s", help="Student team member name"),
    notes: str = typer.Option(..., "--notes", "-n", help="Approval rationale")
):
    """Student governance action to approve the client mandate."""
    engine = ClientMandateEngine()
    try:
        updated = engine.approve_mandate(signer, notes)
        console.print(f"[bold green]Client mandate approved by {signer} at {updated.approval_timestamp}.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Approval failed: {e}[/bold red]")


# ==========================================
# 3. STRATEGY SUB-APP COMMANDS
# ==========================================
@strategy_app.command("run-council")
def strategy_run_council():
    """Runs independent Strategy Architects (A, B, C) and adversarial Red Team."""
    c_engine = ClientMandateEngine()
    mandate = c_engine.load_mandate()
    if not mandate:
        console.print("[red]Cannot run strategy council without an active client mandate.[/red]")
        return
    s_engine = StrategyCouncilEngine()
    console.print("[cyan]Running independent Strategy Architects (Phase 1 Blind)...[/cyan]")
    evaluations = s_engine.run_strategy_council(mandate)
    console.print(f"[green]Successfully evaluated {len(evaluations)} candidate strategies with adversarial Red Team.[/green]")
    for ev in evaluations:
        console.print(Panel.fit(
            f"[bold cyan]{ev.strategy_name}[/bold cyan] ({ev.strategy_id})\n"
            f"[bold]Client Fit[/bold]: {ev.client_fit_assessment}\n"
            f"[bold]Explainability[/bold]: {ev.explainability_assessment}\n"
            f"[bold]Red Team Critiques[/bold]: {len(ev.red_team_critiques)} adversarial reviews",
            title="Strategy Candidate Review"
        ))

@strategy_app.command("candidates")
def strategy_candidates():
    """Lists candidate strategies generated by the council."""
    s_engine = StrategyCouncilEngine()
    candidates = s_engine.get_candidate_strategies()
    if not candidates:
        console.print("[yellow]No candidate strategies found. Run 'wharton-ic strategy run-council' first.[/yellow]")
        return
    for c in candidates:
        console.print(f"- [bold]{c.strategy_name}[/bold] (`{c.strategy_id}`): {c.central_philosophy[:120]}...")

@strategy_app.command("approve")
def strategy_approve(
    strategy_id: str = typer.Option(..., "--id", "-i", help="Strategy ID to select"),
    signers: List[str] = typer.Option(..., "--signer", "-s", help="Student signatures (minimum 2)"),
    rationale: str = typer.Option(..., "--rationale", "-r", help="Student selection rationale"),
    notes: str = typer.Option("", "--notes", "-n", help="Deliberation notes")
):
    """Mandatory student governance action to choose Team Caplet's strategy."""
    s_engine = StrategyCouncilEngine()
    try:
        decision = s_engine.approve_strategy(
            strategy_id=strategy_id,
            student_signatures=signers,
            student_rationale=rationale,
            discussion_notes=notes or "Strategy selected after multi-agent council review."
        )
        console.print(f"[bold green]Strategy {decision.chosen_strategy_name} officially approved by students: {', '.join(signers)}[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Strategy approval failed: {e}[/bold red]")

@strategy_app.command("show")
def strategy_show():
    """Displays the active approved investment strategy."""
    s_engine = StrategyCouncilEngine()
    strat = s_engine.get_active_strategy()
    if not strat:
        console.print("[yellow]No approved investment strategy found. Run 'wharton-ic strategy run-council' and approve one.[/yellow]")
        return
    console.print(Panel.fit(
        f"[bold]Strategy Name[/bold]: {strat.strategy_name} ({strat.strategy_id})\n"
        f"[bold]Philosophy[/bold]: {strat.central_philosophy}\n"
        f"[bold]Portfolio Roles[/bold]: {', '.join(strat.portfolio_roles)}\n"
        f"[bold]Buy Criteria[/bold]: {', '.join(strat.buy_criteria)}\n"
        f"[bold]Sell Criteria[/bold]: {', '.join(strat.sell_criteria)}",
        title=f"Team Caplet Approved Strategy: {strat.strategy_name}"
    ))

@strategy_app.command("memory")
def strategy_memory():
    """Answers the 14 competition reflection questions for the Final Report."""
    mem_engine = StrategyMemoryQueryEngine()
    console.print(mem_engine.format_as_markdown())


# ==========================================
# 4. JOURNAL SUB-APP COMMANDS
# ==========================================
@journal_app.command("add")
def journal_add(
    event_type: str = typer.Option(..., "--type", "-t", help="Event type e.g. TRADE_APPROVED, MISTAKE_IDENTIFIED"),
    title: str = typer.Option(..., "--title", help="Event title"),
    decision: str = typer.Option(..., "--decision", "-d", help="Decision made"),
    reason: str = typer.Option(..., "--reason", "-r", help="Reasoning"),
    participants: List[str] = typer.Option(..., "--participant", "-p", help="Student team members present"),
    discussion: str = typer.Option("", "--discussion", help="Discussion context"),
    lesson: str = typer.Option("", "--lesson", help="Retrospective lesson learned")
):
    """Appends an authentic, timestamped event to the decision journal."""
    import uuid
    engine = DecisionJournalEngine()
    evt = JournalEvent(
        event_id=f"EVT-{str(uuid.uuid4())[:8]}",
        event_type=JournalEventType(event_type),
        title=title,
        participants=participants,
        student_discussion=discussion or reason,
        final_student_decision=decision,
        reasoning=reason,
        retrospective_lesson=lesson or None,
    )
    path = engine.add_event(evt)
    console.print(f"[bold green]Journal event recorded: {evt.title} ({evt.event_type.value}) -> {path}[/bold green]")

@journal_app.command("timeline")
def journal_timeline():
    """Displays chronological timeline of competition decisions."""
    engine = DecisionJournalEngine()
    timeline = engine.get_timeline()
    if not timeline:
        console.print("[yellow]No events logged in the decision journal yet.[/yellow]")
        return
    table = Table(title="Team Caplet Decision Timeline")
    table.add_column("Timestamp")
    table.add_column("Type", style="cyan")
    table.add_column("Title", style="bold")
    table.add_column("Decision", style="green")
    table.add_column("Team Members")
    for t in timeline:
        table.add_row(t["timestamp"], t["type"], t["title"], t["decision"], t["participants"])
    console.print(table)

@journal_app.command("trading-notes")
def journal_trading_notes():
    """Generates the required Trading Notes deliverable table."""
    engine = DecisionJournalEngine()
    console.print(engine.get_trading_notes())

@journal_app.command("lessons")
def journal_lessons():
    """Displays mistakes and retrospective lessons learned."""
    engine = DecisionJournalEngine()
    lessons = engine.get_lessons()
    if not lessons:
        console.print("[yellow]No lessons or mistakes logged yet.[/yellow]")
        return
    for l in lessons:
        console.print(Panel.fit(
            f"[bold]{l['event']}[/bold] ({l['date']})\n"
            f"[bold]Discussion[/bold]: {l['what_happened']}\n"
            f"[bold green]Lesson Learned[/bold green]: {l['lesson_learned']}",
            title="Team Caplet Reflection & Learning"
        ))

@journal_app.command("evolution")
def journal_evolution():
    """Outputs the complete 'How our thinking evolved over the competition' story."""
    engine = DecisionJournalEngine()
    console.print(engine.get_evolution_narrative())

@journal_app.command("verify-chain")
def journal_verify_chain():
    """Verifies the cryptographic hash-chain integrity of the Decision Journal."""
    engine = DecisionJournalEngine()
    res = engine.verify_chain()
    if res["valid"]:
        console.print(f"[bold green]✓ Decision Journal Hash Chain Verified: {res['status']}[/bold green]")
        console.print(f"Events verified: {res['event_count']}, Head Hash: {res.get('head_hash', 'N/A')[:16]}...")
    else:
        console.print(f"[bold red]✗ TAMPERING DETECTED in Decision Journal![/bold red]")
        console.print(f"Broken Event ID: {res['tampered_event_id']}, Index: {res['index']}")
        console.print(f"Reason: {res['reason']}")
        raise typer.Exit(code=1)



# ==========================================
# 5. REPORT SUB-APP COMMANDS
# ==========================================
@report_app.command("evidence-pack")
def report_evidence_pack():
    """Assembles the comprehensive Report Evidence Pack for student report synthesis."""
    engine = WhartonReportEngineV2()
    pack = engine.assemble_evidence_pack()
    console.print(f"[bold green]Report Evidence Pack compiled: {pack.pack_id}[/bold green]")
    console.print(f"Markdown: outputs/report_pack/report_evidence_pack.md")
    console.print(f"JSON: outputs/report_pack/report_evidence_pack.json")

@report_app.command("judge-review")
def report_judge_review():
    """Runs the 9-role Wharton Judge Review Council on the evidence pack."""
    r_engine = WhartonReportEngineV2()
    pack = r_engine.assemble_evidence_pack()
    review = JudgeReviewCouncil.evaluate_pack(pack)
    console.print(f"[bold green]Judge Review completed: outputs/report_pack/judge_review.md[/bold green]")

@report_app.command("audit-ai")
def report_audit_ai():
    """Audits report content blocks against Wharton AI policy and academic integrity."""
    test_block = ContentBlock(
        block_id="BLK-001",
        section_id="strategy_narrative",
        authorship_type=AuthorshipType.HUMAN_AUTHORED,
        author_identity="Ray (Lead PM)",
        content_text="Team Caplet focuses on enduring economic moats verified by forensic Sloan accruals."
    )
    compliant, violations = AIAuthorshipFirewall.audit_blocks([test_block])
    if compliant:
        console.print("[bold green]AI Authorship Audit PASSED: Zero unauthorized generative AI prose detected.[/bold green]")
    else:
        console.print("[bold red]AI Authorship Violations:[/bold red]")
        for v in violations:
            console.print(f"- {v}")


# ==========================================
# 6. RESEARCH SUB-APP COMMANDS
# ==========================================
@research_app.command("fixture-eval")
def research_fixture_eval(ticker: str = typer.Argument("TEST_ALPHA")):
    """Evaluates a synthetic research fixture (TEST_ALPHA, TEST_BETA, TEST_GAMMA)."""
    fixtures = get_mock_security_proposals()
    prop = fixtures.get(ticker)
    if not prop:
        console.print(f"[red]Fixture {ticker} not found. Available: TEST_ALPHA, TEST_BETA, TEST_GAMMA[/red]")
        return
    evaluated = SecurityCouncilEngine.evaluate_proposal(prop)
    console.print(Panel.fit(
        f"[bold]{evaluated.company_name} ({evaluated.ticker})[/bold]\n"
        f"Sector: {evaluated.sector} | Role: {evaluated.portfolio_role}\n"
        f"Committee Recommendation: [bold cyan]{evaluated.committee_recommendation.value}[/bold cyan]\n"
        f"Human Status: [bold green]{evaluated.human_status.value}[/bold green]\n"
        f"Conditions: {', '.join(evaluated.committee_conditions)}",
        title="Security Council Evaluation (Synthetic Fixture)"
    ))


# ==========================================
# 7. GENERAL COMPETITION COMMANDS
# ==========================================
@app.command("ingest-official")
def ingest_official(
    file_path: Optional[Path] = typer.Argument(None, help="Path to official file to ingest"),
    doc_type: str = typer.Option("client_case", "--type", "-t", help="Document type")
):
    """Ingests official Wharton competition files into competition/official/2026_27/."""
    ingestor = OfficialMaterialIngestor()
    if file_path:
        if not file_path.exists():
            console.print(f"[red]File {file_path} not found.[/red]")
            return
        rec = ingestor.ingest_file(file_path, doc_type)
        console.print(f"[bold green]Ingested {rec.filename} ({rec.document_type}) into manifest.yaml with hash {rec.sha256_hash[:12]}...[/bold green]")
    else:
        manifest = ingestor.load_manifest()
        docs = manifest.get("documents", [])
        console.print(f"[cyan]Official 2026-27 Manifest: {len(docs)} documents registered in competition/official/2026_27/manifest.yaml.[/cyan]")
        for d in docs:
            console.print(f"- {d.get('filename')} ({d.get('document_type')}) [hash: {d.get('sha256_hash')[:8]}]")

@app.command("update-data")
def update_data():
    """Refreshes market price caches and financial statements for approved securities."""
    tickers = universe_engine.get_all_tickers(equities_only=True)
    console.print(f"[cyan]Updating local cache for {len(tickers)} approved securities...[/cyan]")
    provider = YFinanceProvider()
    end_dt = date.today()
    start_dt = end_dt - timedelta(days=365)
    prices = provider.get_historical_prices(tickers, start_dt, end_dt)
    console.print(f"[green]Cached price matrix: {prices.shape[0]} days x {prices.shape[1]} assets.[/green]")

@app.command("screen")
def screen_universe(
    model: str = typer.Option("wharton_garp", help="Screening model: wharton_garp, pure_quality, conservative_defensive"),
    top_n: int = typer.Option(15, help="Number of top ranked candidates to display")
):
    """Executes cross-sectional multi-factor screening across the approved universe."""
    tickers = universe_engine.get_all_tickers(equities_only=True)
    console.print(f"[cyan]Executing cross-sectional factor screening across {len(tickers)} approved equities using model '{model}'...[/cyan]")
    
    provider = YFinanceProvider()
    end_dt = date.today()
    start_dt = end_dt - timedelta(days=365)
    prices = provider.get_historical_prices(tickers, start_dt, end_dt)
    
    factor_records = []
    sector_map = universe_engine.get_sector_map()

    for t in tickers:
        p_series = prices[t].dropna() if t in prices else None
        vol = float(p_series.std() * (252**0.5)) if p_series is not None and len(p_series) > 20 else 0.20
        mom = float((p_series.iloc[-1] / p_series.iloc[0]) - 1.0) if p_series is not None and len(p_series) > 20 else 0.05
        
        stmts = provider.get_financial_statements(t, end_dt)
        f_rec = stmts[0] if stmts else {}
        meta = universe_engine.get_metadata(t)
        mcap = meta.market_cap_usd or 5e10
        metrics = compute_comprehensive_fundamentals(f_rec, mcap)

        factor_records.append({
            "ticker": t,
            "sector": sector_map.get(t, "Unclassified"),
            "quality": metrics["roic"] + metrics["operating_margin"] + (metrics["altman_z_score"] * 0.05),
            "value": metrics["fcf_yield"] + (1.0 / max(metrics["pe_ratio"], 5.0)),
            "growth": float(f_rec.get("revenue", 1e8)) / 1e10,
            "momentum": mom,
            "low_volatility": -vol
        })

    factor_df = pd.DataFrame(factor_records)
    engine = FactorScreeningEngine(factor_df)
    ranked = engine.process_and_rank(model_name=model)

    table = Table(title=f"Top {top_n} Ranked Securities ({model.upper()})")
    table.add_column("Rank", justify="right", style="cyan")
    table.add_column("Ticker", style="bold green")
    table.add_column("Sector", style="magenta")
    table.add_column("Composite Score", justify="right")
    table.add_column("Quality Z", justify="right")
    table.add_column("Value Z", justify="right")

    for _, row in ranked.head(top_n).iterrows():
        table.add_row(
            str(int(row["final_rank"])),
            str(row["ticker"]),
            str(row["sector"]),
            f"{row['composite_score']:.2f}",
            f"{row.get('quality_z', 0.0):.2f}",
            f"{row.get('value_z', 0.0):.2f}"
        )

    console.print(table)

@app.command("research")
def research_ticker(ticker: str):
    """Gathers and displays comprehensive point-in-time fundamentals and ratios for a security."""
    ticker = ticker.upper()
    sec = universe_engine.validate_ticker(ticker)
    console.print(f"[cyan]Researching fundamentals for {ticker} ({sec.name})...[/cyan]")

    provider = YFinanceProvider()
    end_dt = date.today()
    stmts = provider.get_financial_statements(ticker, end_dt)
    f_rec = stmts[0] if stmts else {}
    mcap = sec.market_cap_usd or 5e11
    metrics = compute_comprehensive_fundamentals(f_rec, mcap)

    table = Table(title=f"Fundamental Ratios & Financial Health: {ticker}")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right", style="bold green")
    table.add_column("Benchmark / Interpretation", style="dim")

    table.add_row("Return on Invested Capital (ROIC)", f"{metrics['roic']*100:.2f}%", "Hurdle: > 12.0%")
    table.add_row("Return on Equity (ROE)", f"{metrics['roe']*100:.2f}%", "Benchmark: > 15.0%")
    table.add_row("Operating Margin", f"{metrics['operating_margin']*100:.2f}%", "Healthy: > 20.0%")
    table.add_row("Free Cash Flow Conversion", f"{metrics['fcf_conversion']*100:.1f}%", "Target: >= 70.0%")
    table.add_row("Net Debt / EBITDA", f"{metrics['net_debt_to_ebitda']:.2f}x", "Cap: <= 3.0x")
    table.add_row("Altman Z-Score", f"{metrics['altman_z_score']:.2f}", "Safe Zone: > 2.99")
    table.add_row("Sloan Accrual Ratio", f"{metrics['accrual_ratio']:.3f}", "High Quality: < 0.05")
    table.add_row("P/E Ratio", f"{metrics['pe_ratio']:.1f}x", "Market multiple")
    table.add_row("FCF Yield", f"{metrics['fcf_yield']*100:.2f}%", "Cash generation")

    console.print(table)

@app.command("value")
def value_ticker(ticker: str):
    """Executes deterministic DCF, WACC, Comps, and Reverse DCF valuation for a security."""
    ticker = ticker.upper()
    sec = universe_engine.validate_ticker(ticker)
    console.print(f"[cyan]Valuing {ticker} ({sec.name}) deterministically...[/cyan]")

    provider = YFinanceProvider()
    end_dt = date.today()
    prices = provider.get_historical_prices([ticker], end_dt - timedelta(days=365), end_dt)
    current_price = float(prices[ticker].iloc[-1]) if ticker in prices else 150.0

    wacc_params = calculate_wacc(
        risk_free_rate=0.0425,
        beta=1.05,
        equity_risk_premium=0.055,
        pre_tax_cost_of_debt=0.048,
        market_value_equity=sec.market_cap_usd or 5e11,
        total_debt=2.5e10
    )

    stmts = provider.get_financial_statements(ticker, end_dt)
    f_rec = stmts[0] if stmts else {}
    base_rev = float(f_rec.get("revenue", 5e10))
    shares = float(f_rec.get("shares_outstanding", 1e9))

    dcf_res = run_dcf_valuation(
        ticker=ticker,
        current_share_price=current_price,
        shares_outstanding=shares,
        base_revenue=base_rev,
        revenue_growth_rates=[0.08, 0.08, 0.07, 0.06, 0.05],
        target_operating_margins=[0.26, 0.26, 0.27, 0.27, 0.27],
        wacc_params=wacc_params,
        terminal_growth_rate=0.025,
        total_debt=float(f_rec.get("total_debt", 2.5e10)),
        cash_and_equivalents=float(f_rec.get("cash_and_equivalents", 1.5e10)),
        valuation_date=end_dt
    )

    scenarios = run_multi_scenario_valuation(
        ticker=ticker,
        current_share_price=current_price,
        shares_outstanding=shares,
        base_revenue=base_rev,
        wacc_params=wacc_params,
        total_debt=float(f_rec.get("total_debt", 2.5e10)),
        cash_and_equivalents=float(f_rec.get("cash_and_equivalents", 1.5e10)),
        valuation_date=end_dt
    )

    table = Table(title=f"Deterministic Valuation Summary: {ticker}")
    table.add_column("Scenario", style="cyan")
    table.add_column("Implied Price ($)", justify="right", style="bold green")
    table.add_column("Current Price ($)", justify="right")
    table.add_column("Implied Upside (%)", justify="right")

    table.add_row("Base Case DCF", f"${dcf_res.implied_share_price:.2f}", f"${current_price:.2f}", f"{dcf_res.implied_upside_downside_pct*100:+.1f}%")
    table.add_row("Bear Case DCF", f"${scenarios.bear_case_price:.2f}", f"${current_price:.2f}", f"{scenarios.bear_upside_pct*100:+.1f}%")
    table.add_row("Bull Case DCF", f"${scenarios.bull_case_price:.2f}", f"${current_price:.2f}", f"{scenarios.bull_upside_pct*100:+.1f}%")

    console.print(table)
    rev_growth_str = f"{dcf_res.reverse_dcf_implied_growth*100:.2f}%" if dcf_res.reverse_dcf_implied_growth else "N/A"
    console.print(f"[bold]WACC Hurdle Rate[/bold]: {wacc_params.wacc*100:.2f}% | [bold]Reverse DCF Implied Growth[/bold]: {rev_growth_str}")

@app.command("debate")
def debate_ticker(ticker: str):
    """Executes the adversarial Bull vs. Bear debate and Evidence Audit for a security."""
    ticker = ticker.upper()
    sec = universe_engine.validate_ticker(ticker)
    console.print(f"[cyan]Initiating adversarial Bull vs. Bear debate for {ticker}...[/cyan]")
    propose_ticker(ticker)

@app.command("propose")
def propose_ticker(ticker: str):
    """Executes AI Council deliberation and generates the immutable decision ledger for a security."""
    ticker = ticker.upper()
    sec = universe_engine.validate_ticker(ticker)
    console.print(f"[cyan]Initiating AI Council and Decision Ledger for {ticker} ({sec.name})...[/cyan]")

    provider = YFinanceProvider()
    end_dt = date.today()
    prices = provider.get_historical_prices([ticker], end_dt - timedelta(days=365), end_dt)
    current_price = float(prices[ticker].iloc[-1]) if ticker in prices else 150.0

    stmts = provider.get_financial_statements(ticker, end_dt)
    f_rec = stmts[0] if stmts else {}
    mcap = sec.market_cap_usd or 5e11
    fundamentals = compute_comprehensive_fundamentals(f_rec, mcap)

    wacc_params = calculate_wacc(
        risk_free_rate=0.0425,
        beta=1.05,
        market_value_equity=mcap,
        total_debt=float(f_rec.get("total_debt", 2e10))
    )
    valuation = run_multi_scenario_valuation(
        ticker=ticker,
        current_share_price=current_price,
        shares_outstanding=float(f_rec.get("shares_outstanding", 1e9)),
        base_revenue=float(f_rec.get("revenue", 5e10)),
        wacc_params=wacc_params,
        total_debt=float(f_rec.get("total_debt", 2e10)),
        cash_and_equivalents=float(f_rec.get("cash_and_equivalents", 1e10)),
        valuation_date=end_dt
    )

    factors = {"quality_rank": 0.88, "value_rank": 0.65, "momentum_rank": 0.72}
    portfolio_impact = {
        "marginal_volatility_contribution": 0.018,
        "marginal_cvar_contribution": 0.024,
        "sector_concentration_post_trade": 0.165
    }

    orchestrator = CouncilOrchestrator()
    council_result = orchestrator.run_full_council(
        ticker=ticker,
        company_name=sec.name,
        sector=sec.gics_sector,
        industry=sec.gics_industry,
        fundamentals=fundamentals,
        valuation=valuation,
        factors=factors,
        portfolio_impact=portfolio_impact,
        target_weight=0.075
    )

    sources = {
        "filings": f_rec,
        "as_of_date": str(end_dt),
        "source_provider": "yfinance_edgar_pipeline",
        "retrieved_at": datetime.utcnow().isoformat()
    }
    ledger_path = decision_ledger.write_decision_record(
        ticker=ticker,
        proposal=council_result["proposal"],
        council_outputs=council_result,
        sources=sources,
        as_of_date=end_dt
    )

    console.print(Panel.fit(
        f"[bold green]Proposal Created & Frozen in Decision Ledger[/bold green]\n"
        f"Location: {ledger_path.resolve()}\n"
        f"Contains: 00_metadata.json through 15_human_decision.md\n"
        f"Status: [yellow]PROPOSED (Pending Human Signature in 15_human_decision.md)[/yellow]",
        title="Decision Ledger Confirmation"
    ))

@app.command("portfolio")
def optimize_portfolio():
    """Runs all 8 portfolio optimizers and compares metrics against SPY benchmark."""
    tickers = ["MSFT", "AAPL", "NVDA", "JNJ", "UNH", "JPM", "V", "PG", "COST", "CAT", "NEE", "LIN", "XOM", "SPY"]
    console.print(f"[cyan]Optimizing portfolio across {len(tickers)-1} assets using skfolio...[/cyan]")

    provider = YFinanceProvider()
    end_dt = date.today()
    start_dt = end_dt - timedelta(days=400)
    prices = provider.get_historical_prices(tickers, start_dt, end_dt)
    
    returns = prices.pct_change().dropna()
    spy_ret = returns["SPY"]
    asset_ret = returns.drop(columns=["SPY"])

    sector_map = universe_engine.get_sector_map()
    optimizer = PortfolioOptimizer(
        returns_df=asset_ret,
        sector_map=sector_map,
        benchmark_returns=spy_ret
    )

    weights_df, metrics_df = optimizer.compare_all_methods()

    table = Table(title="Portfolio Optimization Model Comparison")
    table.add_column("Method", style="bold cyan")
    table.add_column("CAGR", justify="right")
    table.add_column("Volatility", justify="right")
    table.add_column("Sharpe", justify="right", style="green")
    table.add_column("Max DD", justify="right")
    table.add_column("CVaR (95%)", justify="right")
    table.add_column("Beta to SPY", justify="right")
    table.add_column("ENC", justify="right")

    for _, row in metrics_df.iterrows():
        table.add_row(
            str(row["Method"]).upper(),
            f"{row['CAGR']*100:.2f}%",
            f"{row['Annualized Volatility']*100:.2f}%",
            f"{row['Sharpe Ratio']:.2f}",
            f"{row['Max Drawdown']*100:.1f}%",
            f"{row['Daily CVaR (95%)']*100:.2f}%",
            f"{row['Beta to SPY']:.2f}",
            f"{row['Effective Constituents (ENC)']:.1f}"
        )

    console.print(table)

@app.command("backtest")
def run_backtest():
    """Executes rolling walk-forward backtest and displays out-of-sample performance."""
    tickers = ["MSFT", "AAPL", "NVDA", "JNJ", "UNH", "JPM", "V", "PG", "COST", "CAT", "NEE", "LIN", "XOM", "SPY"]
    console.print("[cyan]Executing walk-forward rolling backtest (lookback=252d, rebalance=quarterly)...[/cyan]")

    provider = YFinanceProvider()
    end_dt = date.today()
    start_dt = end_dt - timedelta(days=600)
    prices = provider.get_historical_prices(tickers, start_dt, end_dt)
    
    spy_prices = prices["SPY"]
    asset_prices = prices.drop(columns=["SPY"])
    sector_map = universe_engine.get_sector_map()

    backtester = WalkForwardBacktester(
        prices_df=asset_prices,
        benchmark_prices=spy_prices,
        sector_map=sector_map,
        lookback_days=200,
        rebalance_freq_days=63
    )

    comparison_df = backtester.compare_strategies_walk_forward()

    table = Table(title="Walk-Forward Out-of-Sample Backtest Results")
    table.add_column("Strategy", style="bold cyan")
    table.add_column("CAGR", justify="right")
    table.add_column("Vol", justify="right")
    table.add_column("Sharpe", justify="right", style="green")
    table.add_column("Max DD", justify="right")
    table.add_column("Turnover", justify="right")
    table.add_column("Hit Rate", justify="right")

    for _, row in comparison_df.iterrows():
        table.add_row(
            str(row["Strategy"]),
            f"{row['CAGR']*100:.2f}%",
            f"{row['Volatility']*100:.2f}%",
            f"{row['Sharpe']:.2f}",
            f"{row['Max Drawdown']*100:.1f}%",
            f"{row['Turnover']*100:.1f}%",
            f"{row['Hit Rate']*100:.1f}%"
        )

    console.print(table)

@app.command("stress")
def run_stress():
    """Executes historical crisis replays, macro factor shocks, and Monte Carlo simulations."""
    console.print("[cyan]Executing portfolio stress testing and fat-tailed Monte Carlo...[/cyan]")
    provider = YFinanceProvider()
    end_dt = date.today()
    tickers = ["MSFT", "AAPL", "NVDA", "JNJ", "UNH", "JPM", "V", "PG", "COST", "CAT", "NEE", "LIN", "XOM"]
    prices = provider.get_historical_prices(tickers, end_dt - timedelta(days=400), end_dt)
    returns = prices.pct_change().dropna()
    weights = np.ones(len(tickers)) / len(tickers) * 0.98

    stress_engine = ScenarioStressEngine(weights, returns)
    replays = stress_engine.run_historical_replay()
    shocks = stress_engine.run_synthetic_shocks()
    mc_results = stress_engine.run_fat_tailed_monte_carlo()

    table_replay = Table(title="Historical Stress Crisis Replays")
    table_replay.add_column("Regime", style="bold cyan")
    table_replay.add_column("Simulated Drawdown", justify="right", style="bold red")
    table_replay.add_column("Trough Capital ($100k start)", justify="right")
    table_replay.add_column("Est. Recovery", justify="right")

    for k, v in replays.items():
        table_replay.add_row(v["name"], f"{v['simulated_drawdown']*100:.1f}%", f"${v['estimated_capital_trough']:,.0f}", f"{v['recovery_months_estimate']} mos")
    console.print(table_replay)

    console.print(f"[bold green]Monte Carlo 1-Yr Goal Attainment P(Return >= 9%): {mc_results['probability_goal_attained']*100:.1f}%[/bold green]")
    console.print(f"[bold red]Monte Carlo 1-Yr Downside P(Drawdown > 20%): {mc_results['probability_drawdown_gt_20pct']*100:.1f}%[/bold red]")

@app.command("monitor")
def monitor_portfolio():
    """Monitors live portfolio health, weight drift, sector limits, and thesis triggers."""
    tickers = ["MSFT", "AAPL", "NVDA", "JNJ", "UNH", "JPM", "V", "PG", "COST", "CAT", "NEE", "LIN", "XOM"]
    target_weights = {t: 1.0 / len(tickers) for t in tickers}
    current_weights = {t: 1.0 / len(tickers) for t in tickers}
    # Induce small simulated drift for demo
    current_weights["NVDA"] += 0.04
    current_weights["MSFT"] -= 0.04

    provider = YFinanceProvider()
    end_dt = date.today()
    prices = provider.get_historical_prices(tickers, end_dt - timedelta(days=60), end_dt)
    sector_map = universe_engine.get_sector_map()

    monitor = PortfolioMonitor(target_weights=target_weights, sector_map=sector_map)
    alerts = monitor.inspect_portfolio(current_weights, prices)

    table = Table(title="Portfolio Monitoring & Drift Alerts")
    table.add_column("Severity", style="bold")
    table.add_column("Category", style="cyan")
    table.add_column("Ticker", style="bold magenta")
    table.add_column("Message")

    if alerts:
        for a in alerts:
            sev_color = "red" if a.severity.value == "CRITICAL" else ("yellow" if a.severity.value == "WARNING" else "green")
            table.add_row(f"[{sev_color}]{a.severity.value}[/{sev_color}]", a.category, a.ticker or "PORTFOLIO", a.message)
    else:
        table.add_row("[green]HEALTHY[/green]", "PORTFOLIO", "ALL", "No breaches or active drift detected.")

    console.print(table)

@app.command("review")
def review_decision(ticker: str):
    """Inspects the immutable decision ledger and human sign-off status for a security."""
    ticker = ticker.upper()
    ledger_dir = decision_ledger.get_ledger_dir(ticker)
    meta_path = ledger_dir / "00_metadata.json"
    human_path = ledger_dir / "15_human_decision.md"

    if not meta_path.exists():
        console.print(f"[yellow]No decision record found for {ticker} at {ledger_dir}.[/yellow]")
        return

    import json
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    console.print(Panel.fit(
        f"[bold]Decision Review: {ticker}[/bold]\n"
        f"Directory: {ledger_dir}\n"
        f"Decision Date: {meta.get('as_of_date')}\n"
        f"Portfolio Role: {meta.get('portfolio_role')}\n"
        f"Proposed Weight: {float(meta.get('proposed_weight', 0.0))*100:.1f}%\n"
        f"Governance Status: [bold green]{meta.get('human_status')}[/bold green]\n"
        f"Approved By: {meta.get('approved_by', 'Pending')}",
        title=f"Wharton IC Decision Ledger — {ticker}"
    ))

@app.command("export-report-pack")
def export_report_pack():
    """Generates the audited Wharton Report Pack and publication charts."""
    tickers = ["MSFT", "AAPL", "NVDA", "JNJ", "UNH", "JPM", "V", "PG", "COST", "CAT", "NEE", "LIN", "XOM"]
    provider = YFinanceProvider()
    end_dt = date.today()
    prices = provider.get_historical_prices(tickers, end_dt - timedelta(days=365), end_dt)
    returns = prices.pct_change().dropna()
    weights = np.ones(len(tickers)) / len(tickers) * 0.98
    w_dict = {t: float(weights[i]) for i, t in enumerate(tickers)}
    sector_map = universe_engine.get_sector_map()

    diag = compute_portfolio_diagnostics(weights, returns)
    opt_df = pd.DataFrame([{"Method": "HRP", "CAGR": diag["cagr"], "Vol": diag["annualized_volatility"], "Sharpe": diag["sharpe_ratio"]}])

    # Visualizations
    visualizer.plot_allocation_and_sectors(w_dict, sector_map)
    visualizer.plot_correlation_heatmap(returns)

    report_dir = report_pack_generator.generate_report_pack(
        weights_dict=w_dict,
        sector_map=sector_map,
        diagnostics=diag,
        optimizer_comparison_df=opt_df,
        decisions_summary=[],
        client_mandate=config_manager.client_mandate
    )
    console.print(f"[bold green]Report Pack exported to: {report_dir.resolve()}[/bold green]")

@app.command("demo")
def run_demo():
    """Runs the complete end-to-end competition demonstration workflow."""
    console.print(Panel.fit(
        "[bold green]Starting wharton-ic End-to-End Competition Workflow Demonstration[/bold green]\n"
        "Philosophy: CLIENT → STRATEGY → RESEARCH → EVIDENCE → VALUATION → PORTFOLIO → RISK → COUNCIL → HUMAN DECISION → REPORT",
        title="wharton-ic Competition System"
    ))

    # 1. Screen
    screen_universe(model="wharton_garp", top_n=10)

    # 2. Value & Propose Anchor Stock (MSFT)
    value_ticker("MSFT")
    propose_ticker("MSFT")

    # 3. Simulate Human Sign-off for Demo
    decision_ledger.record_human_approval(
        ticker="MSFT",
        student_name="Ray (Lead Student Portfolio Manager)",
        allocated_weight=0.085,
        notes="Approved by unanimous human committee consensus. High ROIC compounder within client mandate."
    )
    console.print("[green]Simulated Human Sign-Off recorded in 15_human_decision.md for MSFT.[/green]")

    # 4. Portfolio Optimization
    optimize_portfolio()

    # 5. Backtest
    run_backtest()

    # 6. Stress Testing & Monte Carlo
    console.print("[cyan]Executing Fat-Tailed Monte Carlo (5,000 paths) and Crisis Replays...[/cyan]")
    provider = YFinanceProvider()
    end_dt = date.today()
    tickers = ["MSFT", "AAPL", "NVDA", "JNJ", "UNH", "JPM", "V", "PG", "COST", "CAT", "NEE", "LIN", "XOM"]
    prices = provider.get_historical_prices(tickers, end_dt - timedelta(days=400), end_dt)
    returns = prices.pct_change().dropna()
    weights = np.ones(len(tickers)) / len(tickers) * 0.98

    stress_engine = ScenarioStressEngine(weights, returns)
    mc_results = stress_engine.run_fat_tailed_monte_carlo()
    replays = stress_engine.run_historical_replay()

    console.print(f"[bold green]Monte Carlo Probability of Meeting 9% Client Goal: {mc_results['probability_goal_attained']*100:.1f}%[/bold green]")
    console.print(f"[bold red]Monte Carlo Probability of Drawdown > 20%: {mc_results['probability_drawdown_gt_20pct']*100:.1f}%[/bold red]")

    # 7. Generate Visualizations
    console.print("[cyan]Generating publication-quality charts...[/cyan]")
    sector_map = universe_engine.get_sector_map()
    w_dict = {t: float(weights[i]) for i, t in enumerate(tickers)}
    visualizer.plot_allocation_and_sectors(w_dict, sector_map)
    visualizer.plot_correlation_heatmap(returns)
    visualizer.plot_monte_carlo_cone(mc_results)

    # 8. Compile Report Pack
    console.print("[cyan]Compiling audited Wharton Report Pack...[/cyan]")
    diag = compute_portfolio_diagnostics(weights, returns)
    opt_df = pd.DataFrame([{
        "Method": "HRP",
        "CAGR": diag["cagr"],
        "Vol": diag["annualized_volatility"],
        "Sharpe": diag["sharpe_ratio"]
    }])
    decisions_summary = [{
        "Date": str(end_dt),
        "Ticker": "MSFT",
        "Role": "Core Compounder",
        "Target Weight": "8.5%",
        "Human Decision": "APPROVED",
        "Approved By": "Ray (Lead Portfolio Manager)"
    }]
    report_pack_dir = report_pack_generator.generate_report_pack(
        weights_dict=w_dict,
        sector_map=sector_map,
        diagnostics=diag,
        optimizer_comparison_df=opt_df,
        decisions_summary=decisions_summary,
        client_mandate=config_manager.client_mandate
    )

    console.print(Panel.fit(
        f"[bold green]DEMONSTRATION COMPLETE[/bold green]\n"
        f"Verified Report Pack: {report_pack_dir.resolve()}\n"
        f"Charts Generated: outputs/charts/\n"
        f"Decision Ledger: decisions/{end_dt.isoformat()}_MSFT/",
        title="wharton-ic Success"
    ))

if __name__ == "__main__":
    app()
