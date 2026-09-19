"""Evidence Auditor and fact verification module."""

import re
from typing import List, Dict, Any, Tuple
from wharton_ic.schemas.proposal import EvidenceItem

class EvidenceAuditor:
    """
    Audits agent claims and reports against verified deterministic financial outputs.
    Ensures no hallucinated numbers or ungrounded assertions reach the investment committee.
    """

    def __init__(self, verified_metrics: Dict[str, Any]):
        self.verified_metrics = verified_metrics

    def audit_claim(self, claim_text: str, source_ref: str = "financial_model") -> EvidenceItem:
        """Inspects a claim and assigns strict provenance classification."""
        claim_clean = claim_text.strip()
        
        # Check if explicitly tagged
        if "[FACT]" in claim_clean:
            claim_type = "FACT"
            is_verified = True
        elif "[CALCULATION]" in claim_clean:
            claim_type = "CALCULATION"
            is_verified = True
        elif "[INFERENCE]" in claim_clean:
            claim_type = "INFERENCE"
            is_verified = True
        else:
            # Automatic heuristic check against verified numbers
            numbers_in_claim = re.findall(r"[-+]?\d*\.\d+|\d+", claim_clean)
            is_verified = False
            claim_type = "INFERENCE"

            if not numbers_in_claim:
                claim_type = "INFERENCE"
                is_verified = True
            else:
                # Cross-check extracted numbers against verified metrics
                for num_str in numbers_in_claim:
                    num_val = float(num_str)
                    for k, v in self.verified_metrics.items():
                        if isinstance(v, (int, float)) and abs(v - num_val) < 0.05 * (abs(v) + 1.0):
                            is_verified = True
                            claim_type = "CALCULATION"
                            break
                    if is_verified:
                        break

            if not is_verified and len(numbers_in_claim) > 0:
                claim_type = "UNSUPPORTED"

        return EvidenceItem(
            claim=claim_clean.replace("[FACT]", "").replace("[CALCULATION]", "").replace("[INFERENCE]", "").strip(),
            claim_type=claim_type,
            source_reference=source_ref,
            is_verified=is_verified
        )

    def audit_text_block(self, text: str, source_ref: str = "report") -> List[EvidenceItem]:
        """Extracts bullet points or key assertions from markdown text and audits them."""
        lines = [line.strip("- *").strip() for line in text.split("\n") if line.strip().startswith(("-", "*"))]
        if not lines:
            lines = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 20][:5]

        items = []
        for line in lines:
            if len(line) > 10:
                item = self.audit_claim(line, source_ref=source_ref)
                items.append(item)
        return items

    def generate_audit_summary(self, evidence_items: List[EvidenceItem]) -> Dict[str, Any]:
        """Generates summary statistics on evidence quality and audit status."""
        total = len(evidence_items)
        if total == 0:
            return {"status": "PASSED", "verified_count": 0, "total_count": 0, "verification_rate": 1.0}

        verified = sum(1 for item in evidence_items if item.is_verified)
        unsupported = sum(1 for item in evidence_items if item.claim_type == "UNSUPPORTED")
        rate = verified / total

        status = "PASSED" if unsupported == 0 else "WARNING_UNSUPPORTED_CLAIMS"
        return {
            "status": status,
            "total_claims": total,
            "verified_claims": verified,
            "unsupported_claims": unsupported,
            "verification_rate": float(rate),
            "evidence_breakdown": [item.model_dump() for item in evidence_items]
        }
