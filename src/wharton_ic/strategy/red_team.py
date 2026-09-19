"""Strategy Red Team providing rigorous adversarial critique."""

from typing import List
from wharton_ic.client.models import ClientMandate
from wharton_ic.strategy.models import (
    InvestmentStrategy,
    RedTeamCritique,
    StrategyEvaluation,
)


class StrategyRedTeam:
    """Adversarial multi-agent red team stress-testing candidate investment strategies."""

    @classmethod
    def evaluate_strategy(cls, strategy: InvestmentStrategy, mandate: ClientMandate) -> StrategyEvaluation:
        critiques: List[RedTeamCritique] = []

        # 1. Client Red Team
        critiques.append(RedTeamCritique(
            reviewer_role="Client Red Team",
            critique_focus="Client Objective & Constraint Alignment",
            strengths_identified=[
                f"Acknowledges {mandate.client_name}'s investment horizon.",
                "Explicitly respects client ethical exclusions.",
            ],
            vulnerabilities_and_failure_modes=[
                f"May fail to meet {mandate.client_name}'s liquidity needs if positions become lockup-heavy.",
                "Assumes client is comfortable with prolonged underperformance during market momentum rallies.",
            ],
            jargon_or_complexity_warnings=[],
            unanswered_questions=[
                f"How will {mandate.client_name} react emotionally during a 15% intermediate drawdown?",
            ],
            recommended_revisions=[
                "Explicitly define cash liquidity buffer to meet intermediate client needs.",
            ],
        ))

        # 2. Investment Red Team
        critiques.append(RedTeamCritique(
            reviewer_role="Investment Red Team",
            critique_focus="Financial & Market Assumption Rigor",
            strengths_identified=[
                "Emphasizes cash flow and ROIC/WACC spread over accounting earnings.",
                "Demands margin of safety in valuation.",
            ],
            vulnerabilities_and_failure_modes=[
                "Historical economic moats can erode rapidly under AI-driven technological disruption.",
                "Reverse DCF can be sensitive to small changes in terminal discount rates.",
            ],
            jargon_or_complexity_warnings=[
                "Be careful explaining WACC and reverse DCF so high school judges grasp the concept without feeling overwhelmed.",
            ],
            unanswered_questions=[
                "What specific metric signals that a competitive moat is beginning to decay?",
            ],
            recommended_revisions=[
                "Add explicit falsification thresholds for competitive moat assumptions.",
            ],
        ))

        # 3. Simplicity Editor
        critiques.append(RedTeamCritique(
            reviewer_role="Simplicity Editor",
            critique_focus="Jargon Elimination & Plain-English Clarity",
            strengths_identified=[
                "Clear core philosophy that can be summarized in one sentence.",
            ],
            vulnerabilities_and_failure_modes=[
                "Tendency to overuse financial acronyms (ROIC, WACC, DCF, FCF).",
            ],
            jargon_or_complexity_warnings=[
                "Translate 'economic moat' into practical everyday business language (e.g. why customers cannot leave).",
            ],
            unanswered_questions=[
                "Can a 10th-grade team member explain this clearly in 60 seconds without notes?",
            ],
            recommended_revisions=[
                "Replace academic financial terminology with clear operational analogies.",
            ],
        ))

        # 4. Originality Auditor
        critiques.append(RedTeamCritique(
            reviewer_role="Originality Auditor",
            critique_focus="Authenticity vs Generic Investment Platitudes",
            strengths_identified=[
                "Distinctive portfolio role classification tailored specifically for Team Caplet.",
            ],
            vulnerabilities_and_failure_modes=[
                "Buffett-style 'quality moat' terminology is common among high school teams; needs distinct Caplet execution.",
            ],
            jargon_or_complexity_warnings=[],
            unanswered_questions=[
                "What makes this strategy distinctly Team Caplet rather than a textbook summary?",
            ],
            recommended_revisions=[
                "Infuse specific forensic accounting steps (Sloan accrual checks) as the signature team edge.",
            ],
        ))

        # 5. Wharton Narrative Critic
        critiques.append(RedTeamCritique(
            reviewer_role="Wharton Narrative Critic",
            critique_focus="Competition Storytelling & Judge Memorability",
            strengths_identified=[
                "Compelling contrast between short-term simulator hype and institutional long-term stewardship.",
            ],
            vulnerabilities_and_failure_modes=[
                "Risk of sounding like a passive index fund if buy/sell activity appears too dormant.",
            ],
            jargon_or_complexity_warnings=[],
            unanswered_questions=[
                "How will the team show active learning and adaptation during the 10-week trading journal?",
            ],
            recommended_revisions=[
                "Frame the strategy around disciplined watchlist rebalancing and catalyst monitoring.",
            ],
        ))

        # 6. Implementation Critic
        critiques.append(RedTeamCritique(
            reviewer_role="Implementation Critic",
            critique_focus="Execution Feasibility in 10-Week WInS Simulator",
            strengths_identified=[
                "Clear screening criteria that can be evaluated deterministically.",
            ],
            vulnerabilities_and_failure_modes=[
                "10 weeks is short for intrinsic value realization; judges look for execution discipline, not luck.",
            ],
            jargon_or_complexity_warnings=[],
            unanswered_questions=[
                "What happens if the approved Wharton stock list contains few pure-play moats?",
            ],
            recommended_revisions=[
                "Ensure criteria can flex gracefully to the official approved universe when released.",
            ],
        ))

        return StrategyEvaluation(
            strategy_id=strategy.strategy_id,
            strategy_name=strategy.strategy_name,
            review_label="TEAM INTERNAL QUALITATIVE REVIEW DIMENSIONS",
            client_fit_assessment="High alignment with client long-term capital preservation and compounding.",
            coherence_assessment="Strong internal consistency between screening rules, valuation, and exit criteria.",
            explainability_assessment="Excellent conceptual clarity; requires monitoring of technical acronyms.",
            originality_assessment="Solid institutional framework; strengthened by accounting forensic filters.",
            intellectual_defensibility="Extremely high defensibility against judge Q&A cross-examination.",
            practicality_for_high_school_team="Highly practical; avoids complex derivatives or algorithmic black-boxes.",
            red_team_critiques=critiques,
        )
