"""Core exceptions for Wharton IC Operating System."""


class WhartonICException(Exception):
    """Base exception for all wharton_ic domain errors."""
    def __init__(self, message: str = "", *args, **kwargs):
        super().__init__(message, *args)
        self.message = message
        self.kwargs = kwargs


# Backward compatibility alias
WhartonICError = WhartonICException


class PointInTimeViolationError(WhartonICException):
    """Raised when data from after the as_of date is accessed or requested."""
    def __init__(self, message: str = "", as_of_date: str = "", published_date: str = "", field: str = "", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.as_of_date = as_of_date
        self.published_date = published_date
        self.field = field


class UniverseViolationError(WhartonICException):
    """Raised when an asset outside the approved universe is requested."""
    pass


class ConstraintViolationError(WhartonICException):
    """Raised when an allocation or decision violates client mandate constraints."""
    pass


MandateConstraintViolationError = ConstraintViolationError


class HumanApprovalRequiredError(WhartonICException):
    """Raised when an autonomous process attempts to bypass mandatory human approval."""
    pass


HumanGovernanceError = HumanApprovalRequiredError


class ConfigurationError(WhartonICException):
    """Raised when system or model configuration is invalid."""
    pass


class EvidenceProvenanceError(WhartonICException):
    """Raised when a quantitative or fundamental claim lacks primary source lineage."""
    pass


class OptimizationFailureError(WhartonICException):
    """Raised when convex optimization fails to converge under client constraints."""
    pass


class RulePrecedenceError(WhartonICException):
    """Raised when rule precedence is violated or historical rules override active rules."""
    pass


class ProductionMissingMaterialError(WhartonICException):
    """Raised in PRODUCTION mode when required official competition materials are absent."""
    pass


class ProductionSecurityError(WhartonICException):
    """Raised in PRODUCTION mode when synthetic/demo assets attempt to enter production."""
    pass


class CouncilPartialError(WhartonICException):
    """Raised when an LLM provider fails in PRODUCTION and cannot complete council debate."""
    pass
