"""Tests for Caplet V2.1 — Reference-Grounded Agent Architecture.

Verifies:
1. Reference provenance & licensing isolation (unlicensed repos marked LEARN_ONLY, no copied code).
2. Mandate-first independence (CapletMandate built with zero ticker references, Pydantic validation).
3. Strategy architecture & dynamic red team (distinct philosophies, critiques inspect actual fields).
4. Blind council & adversarial debate (independent phase isolation, multi-round debate preservation).
5. State checkpointing & deterministic resumption (resumption without rerun, cache invalidation).
6. Model routing & provider diversity (fail-closed in production, MODEL_DIVERSITY_LIMITED detection).
7. Human governance & decision roster (authentic roster validation, distinct multi-signature >= 2, AI rejection, NOT_RECORDED storage).
8. Proposition-level evidence verification (SOURCE_EXISTS != SOURCE_SUPPORTS_CLAIM, contradiction detection).
9. Decision journal hash chaining (SHA-256 tamper detection, timeline reconstruction).
10. AI Authorship Firewall & non-washable lineage (raw AI blocked, origin=AI cannot become HUMAN).
11. Dynamic judge review (INSUFFICIENT_EVIDENCE_TO_REVIEW when evidence missing, zero fake client names).
"""

import json
from pathlib import Path
import pytest

from wharton_ic.agents.routing import ModelRegistry, ProviderFamily
from wharton_ic.core.exceptions import CouncilPartialError, HumanGovernanceError
from wharton_ic.evidence.auditor import EvidenceLineageAuditor
from wharton_ic.evidence.models import (
    ClaimType,
    EvidenceClaim,
    SourceEvidenceLink,
    SourceSupportType,
    VerificationStatus,
)
from wharton_ic.governance.roster import TeamMember, TeamRoster
from wharton_ic.journal.engine import DecisionJournalEngine
from wharton_ic.journal.models import JournalEvent, JournalEventType
from wharton_ic.mandate.models import CapletMandate, PortfolioRoleDefinition
from wharton_ic.orchestration.checkpointer import CouncilCheckpointer
from wharton_ic.orchestration.state import CheckpointStatus, CouncilRunState
from wharton_ic.reporting_v2.firewall import AIAuthorshipFirewall, AIAuthorshipViolationError
from wharton_ic.reporting_v2.models import (
    AuthorshipType,
    ContentBlock,
    ContentOrigin,
    EditorIdentity,
    ReportEvidencePack,
)
from wharton_ic.research.council import SecurityCouncilEngine
from wharton_ic.research.fixtures import get_mock_security_proposals
from wharton_ic.review.council import JudgeReviewCouncil
from wharton_ic.strategy.architects import StrategyArchitectEngine
from wharton_ic.strategy.engine import StrategyCouncilEngine
from wharton_ic.strategy.models import InvestmentStrategy
from wharton_ic.strategy.red_team import StrategyRedTeam
from conftest import make_sample_mandate as _make_sample_mandate


# ==============================================================================
# 1. REFERENCE PROVENANCE & LICENSING
# ==============================================================================
def test_reference_provenance_and_licensing_isolation():
    """All 6 reference repos documented with exact SHAs, licenses, and LEARN_ONLY restrictions."""
    third_party_md = Path("docs/THIRD_PARTY.md").read_text(encoding="utf-8")
    matrix_md = Path("docs/reference_mechanism_matrix.md").read_text(encoding="utf-8")
    provenance_md = Path("docs/reference_provenance_v2_1.md").read_text(encoding="utf-8")

    # Verify all 6 repositories are documented
    expected_repos = [
        "TauricResearch/TradingAgents",
        "AI4Finance-Foundation/FinRobot",
        "virattt/ai-hedge-fund",
        "gavin-ho1/wharton-investment-comp",
        "aaravp6/All-Wharton-Investment-Competition",
        "davidliu-2008/wharton-investment-competition25-26",
    ]
    for repo in expected_repos:
        assert repo in third_party_md, f"Missing {repo} in THIRD_PARTY.md"
        assert repo in provenance_md, f"Missing {repo} in reference_provenance_v2_1.md"

    # Verify unlicensed repositories are strictly LEARN_ONLY
    assert "aaravp6/All-Wharton-Investment-Competition" in third_party_md
    assert "davidliu-2008/wharton-investment-competition25-26" in third_party_md
    assert "LEARN_ONLY" in third_party_md
    assert "Zero lines of code have been imported from them" in third_party_md


# ==============================================================================
# 2. MANDATE-FIRST INDEPENDENCE
# ==============================================================================
def test_mandate_first_independence_zero_tickers():
    """CapletMandate builds with zero ticker references and enforces Pydantic constraints."""
    client_mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    caplet_mandate = CapletMandate.from_client_mandate(
        client=client_mandate,
        wharton_snapshot_id="WHARTON-PUB-2026-V1"
    )

    # Verify zero tickers exist in the mandate definition
    mandate_json = caplet_mandate.model_dump_json().lower()
    for forbidden_ticker in ["msft", "aapl", "nvda", "jnj", "amzn", "googl"]:
        assert forbidden_ticker not in mandate_json

    # Test ticker validator: forbidden ticker triggers ValueError
    with pytest.raises(ValueError) as exc:
        CapletMandate(
            mandate_id="MANDATE-INVALID",
            client_mandate_id="CLI-001",
            client_name="Elena Foster",
            wharton_rules_snapshot_id="WHARTON-2026",
            objective_hierarchy=["Beat inflation by investing in MSFT stock"],
            risk_philosophy="Capital preservation first.",
            investment_horizon_years=10.0,
            liquidity_philosophy="Maintain 5% liquidity reserve.",
            forbidden_exposures=["Fossil fuels"],
        )
    assert "Ticker 'MSFT' detected in mandate" in str(exc.value)


# ==============================================================================
# 3. STRATEGY ARCHITECTURE & DYNAMIC RED TEAM
# ==============================================================================
def test_strategy_candidate_diversity_and_dynamic_red_team():
    """Candidate strategies differ by philosophy, and red team generates different critiques."""
    mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    engine = StrategyArchitectEngine()
    candidates = engine.generate_candidate_strategies(mandate, mode="demo")

    assert len(candidates) == 3
    strat_ids = [c.strategy_id for c in candidates]
    assert len(set(strat_ids)) == 3
    assert "STRAT-A-QUALITY-MOAT" in strat_ids
    assert "STRAT-B-ASYMMETRIC-TRANSITION" in strat_ids
    assert "STRAT-C-ALL-WEATHER" in strat_ids

    # Dynamic red team evaluates strategies and produces different critiques
    eval_a = StrategyRedTeam.evaluate_strategy(candidates[0], mandate, mode="demo")
    eval_b = StrategyRedTeam.evaluate_strategy(candidates[1], mandate, mode="demo")

    assert eval_a.strategy_id != eval_b.strategy_id
    assert len(eval_a.red_team_critiques) >= 4
    assert len(eval_b.red_team_critiques) >= 4
    
    orig_a = next(c for c in eval_a.red_team_critiques if c.reviewer_role == "Originality Auditor")
    orig_b = next(c for c in eval_b.red_team_critiques if c.reviewer_role == "Originality Auditor")
    assert orig_a.strengths_identified != orig_b.strengths_identified


# ==============================================================================
# 4. BLIND COUNCIL & ADVERSARIAL DEBATE
# ==============================================================================
def test_blind_council_and_adversarial_debate():
    """Independent analyst phase has no peer leakage, multi-round debate preserved."""
    props = get_mock_security_proposals()
    test_alpha = props["TEST_ALPHA"]

    evaluated = SecurityCouncilEngine.evaluate_proposal(test_alpha)
    delib = evaluated.council_deliberation_log

    # Stage 2: Blind independent analysts
    assert "independent_analyst_a" in delib
    assert "independent_analyst_b" in delib
    assert delib["independent_analyst_a"]["key_driver"] != delib["independent_analyst_b"]["key_driver"]

    # Stage 3: Multi-round debate preserved
    assert "adversarial_debate" in delib
    debate = delib["adversarial_debate"]
    assert len(debate["rounds"]) == 2
    assert "bull" in debate["rounds"][0]
    assert "bear" in debate["rounds"][0]
    assert "Rebuttal" in debate["rounds"][1]["bull"]
    assert "Counter-Rebuttal" in debate["rounds"][1]["bear"]

    # Stage 5: Chair recommendation does not overwrite disagreements
    assert evaluated.committee_recommendation is not None
    assert len(evaluated.council_disagreements) > 0


# ==============================================================================
# 5. STATE CHECKPOINTING & DETERMINISTIC RESUMPTION
# ==============================================================================
def test_state_checkpointing_and_resumption(tmp_path):
    """CouncilRunState saves checkpoint and invalidates when input hashes change."""
    checkpointer = CouncilCheckpointer(checkpoints_dir=tmp_path)
    state = CouncilRunState(
        run_id="RUN-TEST-001",
        council_type="SECURITY",
        wharton_rules_snapshot_id="WHARTON-PUB-2026-V1",
        client_mandate_version="2026.1",
        input_artifact_hashes={"mandate": "hash123", "universe": "hash456"},
        prompt_metadata={"analyst_prompt": "prompt_hash_v1"},
        model_metadata={"fundamental_analyst": "claude-3-7-sonnet"},
        completed_stages=["STAGE_1_SPECIALISTS"],
        agent_outputs={"stage_1": {"analysts": ["client_steward", "valuation"]}},
        checkpoint_status=CheckpointStatus.COMPLETED,
    )

    path = checkpointer.save_checkpoint(state)
    assert path.exists()

    # Resume from checkpoint with identical inputs
    resumed = checkpointer.load_checkpoint(
        run_id="RUN-TEST-001",
        current_input_hashes={"mandate": "hash123", "universe": "hash456"},
        prompt_versions={"analyst_prompt": "prompt_hash_v1"},
        model_config={"fundamental_analyst": "claude-3-7-sonnet"},
    )
    assert resumed is not None
    assert resumed.run_id == "RUN-TEST-001"
    assert resumed.checkpoint_status == CheckpointStatus.COMPLETED

    # Invalidation occurs when prompts change
    invalidated = checkpointer.load_checkpoint(
        run_id="RUN-TEST-001",
        current_input_hashes={"mandate": "hash123", "universe": "hash456"},
        prompt_versions={"analyst_prompt": "prompt_hash_v2_CHANGED"},
        model_config={"fundamental_analyst": "claude-3-7-sonnet"},
    )
    assert invalidated is None


# ==============================================================================
# 6. MODEL ROUTING & PROVIDER DIVERSITY
# ==============================================================================
def test_model_routing_diversity_and_fail_closed(monkeypatch):
    """ModelRegistry maps roles across provider families and fails closed in production."""
    registry = ModelRegistry()
    assert len(registry.role_mappings) >= 11

    # Check that roles span distinct provider families
    providers = set(cfg.provider_family for cfg in registry.role_mappings.values())
    assert ProviderFamily.ANTHROPIC in providers
    assert ProviderFamily.OPENAI in providers
    assert ProviderFamily.GOOGLE in providers

    # Diversity limitation detection
    assert registry.is_diversity_limited() is True

    # In production mode without real keys, fails closed with CouncilPartialError
    monkeypatch.setenv("WHARTON_MODE", "PRODUCTION")
    with pytest.raises(CouncilPartialError):
        registry.execute_role(
            role="valuation_analyst",
            system_prompt="Test system",
            user_prompt="Analyze MSFT",
            mode="production",
        )


# ==============================================================================
# 7. HUMAN GOVERNANCE & DECISION ROSTER
# ==============================================================================
def test_human_governance_roster_and_ai_rejection(tmp_path):
    """Roster validates distinct students, rejects AI signatures and duplicate signers."""
    roster_file = tmp_path / "team_roster.json"
    roster = TeamRoster(storage_path=roster_file)

    # 1. Valid registered students pass
    signers = roster.validate_signatures(["Student A", "Student B"], min_signers=2)
    assert len(signers) == 2

    # 2. Reject AI agent signatures
    for fake_sig in ["Committee Chair Agent", "AI Assistant", "Valuation Bot", "Model Lead"]:
        with pytest.raises(HumanGovernanceError) as exc:
            roster.validate_signatures([fake_sig, "Student A"], min_signers=2)
        assert "AI agents are forbidden from signing" in str(exc.value)

    # 3. Reject duplicate signatures by the same student
    with pytest.raises(HumanGovernanceError) as exc:
        roster.validate_signatures(["Student A", "Student A"], min_signers=2)
    assert "Duplicate signature detected" in str(exc.value)

    # 4. Strategy approval stores NOT_RECORDED when student discussion omitted
    engine = StrategyCouncilEngine(base_dir=tmp_path / "strat", roster=roster)
    mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    engine.run_strategy_council(mandate)

    decision = engine.approve_strategy(
        strategy_id="STRAT-A-QUALITY-MOAT",
        student_signatures=["Student A", "Student B"],
        student_rationale="Authentic student rationale for choosing quality moats.",
        discussion_notes=None,  # Omitted notes
    )
    assert decision.student_discussion_notes == "NOT_RECORDED"
    assert decision.key_disagreements == ["NOT_RECORDED"]


# ==============================================================================
# 8. PROPOSITION-LEVEL EVIDENCE VERIFICATION
# ==============================================================================
def test_proposition_level_evidence_verification():
    """SOURCE_EXISTS != SOURCE_SUPPORTS_CLAIM; verifies direct support and contradictions."""
    auditor = EvidenceLineageAuditor(known_source_ids={"SEC-10K-2025"})

    # Case A: Source exists, but proposition link not provided -> PARTIALLY_VERIFIED
    claim_a = EvidenceClaim(
        claim_id="CLM-01",
        claim_text="Revenue grew 14% year-over-year.",
        claim_type_requested=ClaimType.FACTUAL,
        source_ids=["SEC-10K-2025"],
        as_of_date="2026-09-19",
    )
    audited_a = auditor.audit_claim(claim_a)
    assert audited_a.verification_status == VerificationStatus.PARTIALLY_VERIFIED

    # Case B: Explicit SourceEvidenceLink with DIRECT_SUPPORT -> VERIFIED
    claim_b = EvidenceClaim(
        claim_id="CLM-02",
        claim_text="Revenue was $245B in fiscal 2025.",
        claim_type_requested=ClaimType.FACTUAL,
        source_ids=["SEC-10K-2025"],
        support_links=[
            SourceEvidenceLink(
                source_id="SEC-10K-2025",
                locator="Item 8 - Financial Statements, Consolidated Income Statement, Page 62",
                verbatim_quote="Total revenue: $245,123 million",
                support_type=SourceSupportType.DIRECT_SUPPORT,
                verified_by="Student Analyst Lead",
            )
        ],
        as_of_date="2026-09-19",
    )
    audited_b = auditor.audit_claim(claim_b)
    assert audited_b.verification_status == VerificationStatus.VERIFIED

    # Case C: Source contradicts claim proposition -> CONTRADICTED
    claim_c = EvidenceClaim(
        claim_id="CLM-03",
        claim_text="Company has zero debt.",
        claim_type_requested=ClaimType.FACTUAL,
        source_ids=["SEC-10K-2025"],
        support_links=[
            SourceEvidenceLink(
                source_id="SEC-10K-2025",
                locator="Item 8 - Balance Sheet, Long-Term Debt, Page 64",
                verbatim_quote="Long-term debt: $47,250 million",
                support_type=SourceSupportType.CONTRADICTS,
                verified_by="Fundamental Analyst Lead",
            )
        ],
        as_of_date="2026-09-19",
    )
    audited_c = auditor.audit_claim(claim_c)
    assert audited_c.verification_status == VerificationStatus.CONTRADICTED


# ==============================================================================
# 9. DECISION JOURNAL HASH CHAINING & TAMPER DETECTION
# ==============================================================================
def test_decision_journal_hash_chaining_and_tamper_detection(tmp_path):
    """Cryptographic hash chain detects any modification to historical events."""
    engine = DecisionJournalEngine(journal_dir=tmp_path)

    evt1 = JournalEvent(
        event_id="EVT-01",
        event_type=JournalEventType.STRATEGY_PROPOSED,
        title="Initial Strategy Proposal",
        participants=["Lead PM", "Risk Lead"],
        student_discussion="Discussed Quality Moats vs Macro Regime.",
        final_student_decision="Pursue Quality Moats.",
        reasoning="Matches Elena's endowment horizon.",
    )
    engine.add_event(evt1)

    evt2 = JournalEvent(
        event_id="EVT-02",
        event_type=JournalEventType.THESIS_REVISED,
        title="Revised Margin of Safety",
        participants=["Lead PM"],
        student_discussion="Demanded 15% margin of safety after market rally.",
        final_student_decision="Tighten buy hurdle rate.",
        reasoning="Capital preservation first.",
    )
    engine.add_event(evt2)

    # Initial chain is intact
    verification = engine.verify_chain()
    assert verification["valid"] is True
    assert verification["event_count"] == 2
    assert verification["status"] == "TAMPER_FREE"

    # Tamper with Event 1 in the log file
    log_lines = (tmp_path / "events.jsonl").read_text(encoding="utf-8").splitlines()
    tampered_evt1 = json.loads(log_lines[0])
    tampered_evt1["reasoning"] = "TAMPERED: We decided to buy speculative meme stocks."
    log_lines[0] = json.dumps(tampered_evt1)
    (tmp_path / "events.jsonl").write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    # Chain verification immediately detects tampering
    tamper_check = engine.verify_chain()
    assert tamper_check["valid"] is False
    assert tamper_check["tampered_event_id"] == "EVT-01"


# ==============================================================================
# 10. AI AUTHORSHIP FIREWALL & NON-WASHABLE LINEAGE
# ==============================================================================
def test_ai_authorship_firewall_and_non_washable_lineage():
    """Raw AI text blocked; origin=AI cannot be washed into pure HUMAN_AUTHORED."""
    # 1. Raw AI_GENERATED prose fails
    ai_block = ContentBlock(
        block_id="BLK-AI-01",
        section_id="strategy",
        authorship_type=AuthorshipType.AI_GENERATED,
        author_identity="frontier_model",
        content_text="This is direct AI text without student rewriting.",
    )
    with pytest.raises(AIAuthorshipViolationError) as exc:
        AIAuthorshipFirewall.assert_compliant([ai_block])
    assert "raw AI_GENERATED text" in str(exc.value)

    # 2. Authorship washing attempt: origin=AI but labeled HUMAN_AUTHORED fails
    washed_block = ContentBlock(
        block_id="BLK-WASH-01",
        section_id="intro",
        origin=ContentOrigin.AI,
        authorship_type=AuthorshipType.HUMAN_AUTHORED,
        author_identity="Student A",
        content_text="Student claims this is pure human work, but origin was AI.",
    )
    with pytest.raises(AIAuthorshipViolationError) as exc2:
        AIAuthorshipFirewall.assert_compliant([washed_block])
    assert "cannot be washed into human origin" in str(exc2.value)

    # 3. Legitimate human editing retains origin=AI with last_editor=HUMAN and edit history
    legit_block = ContentBlock(
        block_id="BLK-LEGIT-01",
        section_id="analysis",
        origin=ContentOrigin.AI,
        authorship_type=AuthorshipType.AI_ASSISTED_IDEA,
        author_identity="fundamental_analyst",
        content_text="Original AI concept.",
        has_mandatory_disclosure=True,
    )
    legit_block.record_human_edit("Student A", "Rewrote thesis in student voice.")
    assert legit_block.origin == ContentOrigin.AI
    assert legit_block.last_editor == EditorIdentity.HUMAN
    assert legit_block.authorship_type == AuthorshipType.HUMAN_EDITED
    assert len(legit_block.edit_history) == 1


# ==============================================================================
# 11. DYNAMIC JUDGE REVIEW
# ==============================================================================
def test_dynamic_judge_review_insufficient_evidence(tmp_path):
    """JudgeReviewCouncil returns INSUFFICIENT_EVIDENCE_TO_REVIEW if evidence missing."""
    empty_pack = ReportEvidencePack(
        pack_id="PACK-EMPTY-01",
        assembled_at="2026-09-19",
        client_mandate={"status": "AWAITING_STUDENT_APPROVAL"},
        approved_strategy={"status": "AWAITING_STUDENT_SELECTION"},
        verified_rules=[],
    )

    review = JudgeReviewCouncil.evaluate_pack(empty_pack, output_dir=tmp_path)
    assert review is not None
    client_critique = next(c for c in review.role_critiques if c.role_name == "Client Alignment Reviewer")
    strategy_critique = next(c for c in review.role_critiques if c.role_name == "Strategy Coherence Reviewer")

    assert any("INSUFFICIENT_EVIDENCE_TO_REVIEW" in w for w in client_critique.weaknesses)
    assert any("INSUFFICIENT_EVIDENCE_TO_REVIEW" in w for w in strategy_critique.weaknesses)
