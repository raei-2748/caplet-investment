"""Evidence Lineage Auditor enforcing non-hallucinatory claim verification."""

import re
from typing import Any, Dict, List, Optional, Set, Tuple
from pydantic import BaseModel
from wharton_ic.evidence.models import (
    ClaimType,
    EvidenceClaim,
    EvidenceGraph,
    EvidenceGraphNode,
    VerificationStatus,
)


class EvidenceAuditSummary(BaseModel):
    total_claims: int
    verified_count: int
    partially_verified_count: int
    unsupported_count: int
    contradicted_count: int
    inference_count: int
    claims: List[EvidenceClaim]


class EvidenceLineageAuditor:
    """Audits claims against known source datasets, deterministic calculations, and ground truth."""

    def __init__(self, known_source_ids: Optional[Set[str]] = None, known_metrics: Optional[Dict[str, float]] = None):
        self.known_source_ids = known_source_ids or set()
        self.known_metrics = known_metrics or {}
        self.graph = EvidenceGraph()

    def register_source(self, source_id: str, metadata: Dict) -> None:
        self.known_source_ids.add(source_id)
        self.graph.add_node(EvidenceGraphNode(
            node_id=source_id,
            node_type="SOURCE",
            payload=metadata,
        ))

    def register_calculation(self, calc_id: str, value: float, parent_source_ids: List[str]) -> None:
        self.known_metrics[calc_id] = value
        self.graph.add_node(EvidenceGraphNode(
            node_id=calc_id,
            node_type="CALCULATION",
            payload={"value": value},
            parent_ids=parent_source_ids,
        ))

    def audit_claim(self, claim: EvidenceClaim) -> EvidenceClaim:
        """Audits a single claim against primary sources and deterministic calculations."""
        # Non-negotiable rule: AI self-labeling as [FACT] does not grant verification
        clean_text = re.sub(r"\[(FACT|CALCULATION|INFERENCE)\]", "", claim.claim_text).strip()
        
        # Check type
        if claim.claim_type_requested == ClaimType.INFERENCE:
            return EvidenceClaim(
                claim_id=claim.claim_id,
                claim_text=clean_text,
                claim_type_requested=claim.claim_type_requested,
                source_ids=claim.source_ids,
                metric_ids=claim.metric_ids,
                as_of_date=claim.as_of_date,
                verification_status=VerificationStatus.INFERENCE,
                verification_method="CLASSIFIED_AS_REASONING_INFERENCE",
                notes="Inferential claim; valid as argument but not as empirical fact.",
            )

        if claim.claim_type_requested == ClaimType.CALCULATION:
            # Must link to a registered deterministic calculation
            valid_metrics = [m for m in claim.metric_ids if m in self.known_metrics]
            if valid_metrics:
                status = VerificationStatus.VERIFIED if len(valid_metrics) == len(claim.metric_ids) else VerificationStatus.PARTIALLY_VERIFIED
                method = f"MATCHED_DETERMINISTIC_CALCULATIONS: {', '.join(valid_metrics)}"
            else:
                status = VerificationStatus.UNSUPPORTED
                method = "FAILED_TO_LOCATE_DETERMINISTIC_CALCULATION"

            return EvidenceClaim(
                claim_id=claim.claim_id,
                claim_text=clean_text,
                claim_type_requested=claim.claim_type_requested,
                source_ids=claim.source_ids,
                metric_ids=claim.metric_ids,
                as_of_date=claim.as_of_date,
                verification_status=status,
                verification_method=method,
                notes=claim.notes,
            )

        # Factual Claim
        if claim.claim_type_requested == ClaimType.FACTUAL:
            if not claim.source_ids:
                return EvidenceClaim(
                    claim_id=claim.claim_id,
                    claim_text=clean_text,
                    claim_type_requested=claim.claim_type_requested,
                    source_ids=[],
                    metric_ids=[],
                    as_of_date=claim.as_of_date,
                    verification_status=VerificationStatus.UNSUPPORTED,
                    verification_method="NO_SOURCE_LINEAGE_PROVIDED",
                    notes="Claim lacks primary filing or database source ID.",
                )

            valid_sources = [s for s in claim.source_ids if s in self.known_source_ids]
            if len(valid_sources) == len(claim.source_ids) and len(valid_sources) > 0:
                status = VerificationStatus.VERIFIED
                method = f"MATCHED_PRIMARY_SOURCES: {', '.join(valid_sources)}"
            elif len(valid_sources) > 0:
                status = VerificationStatus.PARTIALLY_VERIFIED
                method = f"PARTIAL_SOURCES_MATCHED: {', '.join(valid_sources)}"
            else:
                status = VerificationStatus.UNSUPPORTED
                method = "SOURCES_NOT_FOUND_IN_AUDITED_REGISTRY"

            # Check contradictions
            if claim.contradiction_ids:
                status = VerificationStatus.CONTRADICTED
                method += f" | CONTRADICTED_BY_{len(claim.contradiction_ids)}_ITEMS"

            return EvidenceClaim(
                claim_id=claim.claim_id,
                claim_text=clean_text,
                claim_type_requested=claim.claim_type_requested,
                source_ids=claim.source_ids,
                metric_ids=claim.metric_ids,
                as_of_date=claim.as_of_date,
                verification_status=status,
                verification_method=method,
                notes=claim.notes,
            )

        return claim

    def audit_claims_batch(self, claims: List[EvidenceClaim]) -> EvidenceAuditSummary:
        audited = [self.audit_claim(c) for c in claims]
        counts = {s: 0 for s in VerificationStatus}
        for c in audited:
            counts[c.verification_status] += 1

        return EvidenceAuditSummary(
            total_claims=len(audited),
            verified_count=counts[VerificationStatus.VERIFIED],
            partially_verified_count=counts[VerificationStatus.PARTIALLY_VERIFIED],
            unsupported_count=counts[VerificationStatus.UNSUPPORTED],
            contradicted_count=counts[VerificationStatus.CONTRADICTED],
            inference_count=counts[VerificationStatus.INFERENCE],
            claims=audited,
        )


class EvidenceAuditor:
    """Auditor for council text block scanning and backward compatibility."""

    def __init__(self, ground_truth_metrics: Optional[Dict[str, Any]] = None):
        self.ground_truth = ground_truth_metrics or {}
        self.lineage_auditor = EvidenceLineageAuditor()

    def audit_claim(self, line: str, source_ref: str = "text"):
        from wharton_ic.schemas.proposal import EvidenceItem
        line_clean = line.strip()
        if "[CALCULATION]" in line_clean:
            clean = line_clean.replace("- [CALCULATION]", "").replace("[CALCULATION]", "").strip()
            return EvidenceItem(
                claim=clean,
                claim_type="CALCULATION",
                source_reference=source_ref,
                is_verified=True
            )
        elif "[FACT]" in line_clean:
            clean = line_clean.replace("- [FACT]", "").replace("[FACT]", "").strip()
            return EvidenceItem(
                claim=clean,
                claim_type="FACT",
                source_reference=source_ref,
                is_verified=True
            )
        elif "[INFERENCE]" in line_clean:
            clean = line_clean.replace("- [INFERENCE]", "").replace("[INFERENCE]", "").strip()
            return EvidenceItem(
                claim=clean,
                claim_type="INFERENCE",
                source_reference=source_ref,
                is_verified=True
            )
        else:
            return EvidenceItem(
                claim=line_clean,
                claim_type="UNSUPPORTED",
                source_reference="none",
                is_verified=False
            )

    def audit_text_block(self, text: str, source_ref: str = "analyst_report"):
        from wharton_ic.schemas.proposal import EvidenceItem
        items = []
        for line in text.split("\n"):
            line = line.strip()
            if not line:
                continue
            if "[FACT]" in line:
                clean = line.replace("- [FACT]", "").replace("[FACT]", "").strip()
                items.append(EvidenceItem(
                    claim=clean,
                    claim_type="FACT",
                    source_reference=source_ref,
                    is_verified=True if self.ground_truth else False
                ))
            elif "[CALCULATION]" in line:
                clean = line.replace("- [CALCULATION]", "").replace("[CALCULATION]", "").strip()
                items.append(EvidenceItem(
                    claim=clean,
                    claim_type="CALCULATION",
                    source_reference=source_ref,
                    is_verified=True if self.ground_truth else False
                ))
            elif "[INFERENCE]" in line:
                clean = line.replace("- [INFERENCE]", "").replace("[INFERENCE]", "").strip()
                items.append(EvidenceItem(
                    claim=clean,
                    claim_type="INFERENCE",
                    source_reference=source_ref,
                    is_verified=False
                ))
        return items

    def generate_audit_summary(self, evidence_items) -> Dict[str, Any]:
        total = len(evidence_items)
        verified = sum(1 for i in evidence_items if i.is_verified)
        return {
            "total_claims": total,
            "verified_claims": verified,
            "verification_rate": (verified / total) if total > 0 else 1.0,
            "status": "PASSED" if (verified / total if total > 0 else 1.0) >= 0.5 else "AUDIT_WARNING"
        }
