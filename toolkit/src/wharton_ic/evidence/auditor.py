"""Evidence Lineage Auditor enforcing non-hallucinatory claim verification (Caplet V2.1)."""

import os
import re
from typing import Any, Dict, List, Optional, Set, Tuple
from pydantic import BaseModel
from wharton_ic.evidence.models import (
    ClaimType,
    EvidenceClaim,
    EvidenceGraph,
    EvidenceGraphNode,
    SourceEvidenceLink,
    SourceSupportType,
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
    """Audits claims against known source datasets, deterministic calculations, and ground truth.
    
    Enforces the core rule: SOURCE_EXISTS != SOURCE_SUPPORTS_CLAIM.
    A factual claim requires an explicit SourceEvidenceLink proving DIRECT_SUPPORT.
    """

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
                support_links=claim.support_links,
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
                support_links=claim.support_links,
            )

        # Factual Claim: SOURCE_EXISTS != SOURCE_SUPPORTS_CLAIM
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
                    support_links=[],
                )

            valid_sources = [s for s in claim.source_ids if s in self.known_source_ids]
            if not valid_sources:
                return EvidenceClaim(
                    claim_id=claim.claim_id,
                    claim_text=clean_text,
                    claim_type_requested=claim.claim_type_requested,
                    source_ids=claim.source_ids,
                    metric_ids=claim.metric_ids,
                    as_of_date=claim.as_of_date,
                    verification_status=VerificationStatus.UNSUPPORTED,
                    verification_method="SOURCES_NOT_FOUND_IN_AUDITED_REGISTRY",
                    notes="Sources referenced do not exist in audited registry.",
                    support_links=claim.support_links,
                )

            # Check contradictions first
            has_contradiction = False
            if claim.support_links:
                has_contradiction = any(link.support_type == SourceSupportType.CONTRADICTS for link in claim.support_links)

            if claim.contradiction_ids or has_contradiction:
                return EvidenceClaim(
                    claim_id=claim.claim_id,
                    claim_text=clean_text,
                    claim_type_requested=claim.claim_type_requested,
                    source_ids=claim.source_ids,
                    metric_ids=claim.metric_ids,
                    as_of_date=claim.as_of_date,
                    verification_status=VerificationStatus.CONTRADICTED,
                    verification_method="SOURCE_CONTRADICTED_BY_RECORDED_EVIDENCE",
                    notes="Source document explicitly contradicts the factual proposition.",
                    contradiction_ids=claim.contradiction_ids or ["LINK_CONTRADICTION"],
                    support_links=claim.support_links,
                )

            # Check explicit proposition links
            if claim.support_links:
                has_direct = any(link.support_type == SourceSupportType.DIRECT_SUPPORT for link in claim.support_links)
                all_direct = all(link.support_type == SourceSupportType.DIRECT_SUPPORT for link in claim.support_links)
                
                if all_direct and has_direct:
                    status = VerificationStatus.VERIFIED
                    method = "PROPOSITION_DIRECTLY_SUPPORTED_BY_LOCATOR"
                elif has_direct:
                    status = VerificationStatus.PARTIALLY_VERIFIED
                    method = "PROPOSITION_PARTIALLY_SUPPORTED"
                else:
                    status = VerificationStatus.UNSUPPORTED
                    method = "LINKS_DO_NOT_SUPPORT_PROPOSITION"

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
                    support_links=claim.support_links,
                )

            # Sources exist, but no explicit SourceEvidenceLink proving proposition
            return EvidenceClaim(
                claim_id=claim.claim_id,
                claim_text=clean_text,
                claim_type_requested=claim.claim_type_requested,
                source_ids=claim.source_ids,
                metric_ids=claim.metric_ids,
                as_of_date=claim.as_of_date,
                verification_status=VerificationStatus.PARTIALLY_VERIFIED,
                verification_method="SOURCE_EXISTS_BUT_AWAITING_LOCATOR_PROOF",
                notes="Source exists in registry, but proposition link (locator/quote) not verified.",
                support_links=[],
            )

        return claim

    def audit_claims_batch(self, claims: List[EvidenceClaim]) -> EvidenceAuditSummary:
        audited = [self.audit_claim(c) for c in claims]
        counts = {s: 0 for s in VerificationStatus}
        for c in audited:
            counts[c.verification_status] += 1

        return EvidenceAuditSummary(
            total_claims=len(claims),
            verified_count=counts[VerificationStatus.VERIFIED],
            partially_verified_count=counts[VerificationStatus.PARTIALLY_VERIFIED],
            unsupported_count=counts[VerificationStatus.UNSUPPORTED],
            contradicted_count=counts[VerificationStatus.CONTRADICTED],
            inference_count=counts[VerificationStatus.INFERENCE],
            claims=audited,
        )


class EvidenceItem(BaseModel):
    claim: str
    claim_type: str
    source_reference: Optional[str]
    is_verified: bool
    ground_truth_value: Optional[float] = None


class EvidenceAuditor:
    """Legacy compatibility auditor. STRICTLY ISOLATED IN PRODUCTION."""

    def __init__(self, ground_truth_data: Optional[Dict[str, Any]] = None):
        if os.environ.get("WHARTON_MODE", "demo").lower() == "production":
            raise RuntimeError(
                "Legacy EvidenceAuditor is strictly forbidden in production mode. "
                "All verification must route through EvidenceLineageAuditor with explicit SourceEvidenceLink validation."
            )
        self.ground_truth = ground_truth_data or {}

    def extract_evidence_items(self, text: str, source_ref: Optional[str] = None) -> List[EvidenceItem]:
        items = []
        for raw_line in text.split("\n"):
            line = raw_line.strip()
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

    def audit_text_block(self, text: str, source_ref: Optional[str] = None) -> List[EvidenceItem]:
        """Audits text block and extracts labeled evidence items (legacy wrapper)."""
        return self.extract_evidence_items(text, source_ref=source_ref)

    def audit_claim(self, claim_text: str) -> EvidenceItem:
        """Audits a single claim string against verified ground truth numbers (demo/legacy)."""
        text = claim_text.strip()
        clean = text.lstrip("- *").strip()

        if "[CALCULATION]" in clean:
            c = clean.replace("[CALCULATION]", "").strip()
            nums = [float(x) for x in re.findall(r"\b\d+\.?\d*\b", c)]
            verified = False
            gt_val = None
            if self.ground_truth:
                gt_vals = [float(v) for v in self.ground_truth.values() if isinstance(v, (int, float))]
                for n in nums:
                    for g in gt_vals:
                        if abs(n - g) < 1e-4 or abs(n - g * 100) < 1e-2:
                            verified = True
                            gt_val = g
                            break
                    if verified:
                        break
            return EvidenceItem(
                claim=c,
                claim_type="CALCULATION" if verified else "UNSUPPORTED",
                source_reference="AUDITED_CALCULATION",
                is_verified=verified,
                ground_truth_value=gt_val,
            )

        if "[FACT]" in clean:
            c = clean.replace("[FACT]", "").strip()
            return EvidenceItem(
                claim=c,
                claim_type="FACT",
                source_reference="AUDITED_FACT",
                is_verified=True,
            )

        if "[INFERENCE]" in clean:
            c = clean.replace("[INFERENCE]", "").strip()
            return EvidenceItem(
                claim=c,
                claim_type="INFERENCE",
                source_reference="QUALITATIVE_INFERENCE",
                is_verified=True,
            )

        return EvidenceItem(
            claim=clean,
            claim_type="UNSUPPORTED",
            source_reference=None,
            is_verified=False,
        )

    def generate_audit_summary(self, evidence_items) -> Dict[str, Any]:
        total = len(evidence_items)
        verified = sum(1 for i in evidence_items if i.is_verified)
        return {
            "total_claims": total,
            "verified_claims": verified,
            "verification_rate": (verified / total) if total > 0 else 1.0,
            "status": "PASSED" if (verified / total if total > 0 else 1.0) >= 0.5 else "AUDIT_WARNING"
        }
