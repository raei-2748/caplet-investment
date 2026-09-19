"""Custom domain exceptions for wharton-ic."""

class WhartonICError(Exception):
    """Base class for all wharton-ic exceptions."""
    pass

class PointInTimeViolationError(WhartonICError):
    """Raised when an operation attempts to access data published after the effective as_of date."""
    def __init__(self, message: str, as_of_date: str, published_date: str, field: str):
        super().__init__(f"Look-Ahead Bias Violation: {message} (as_of={as_of_date}, published={published_date}, field={field})")
        self.as_of_date = as_of_date
        self.published_date = published_date
        self.field = field

class UniverseViolationError(WhartonICError):
    """Raised when an operation references a security outside the Wharton approved universe."""
    def __init__(self, ticker: str, reason: str):
        super().__init__(f"Unauthorized Universe Security: {ticker} is not eligible. Reason: {reason}")
        self.ticker = ticker
        self.reason = reason

class ConstraintViolationError(WhartonICError):
    """Raised when portfolio weights or risks breach Wharton or client constraints."""
    def __init__(self, constraint_name: str, actual_value: float, allowed_limit: float):
        super().__init__(f"Constraint Violation: {constraint_name} value {actual_value} exceeded limit {allowed_limit}")
        self.constraint_name = constraint_name
        self.actual_value = actual_value
        self.allowed_limit = allowed_limit

class HumanApprovalRequiredError(WhartonICError):
    """Raised when attempting to execute or commit an unapproved investment proposal."""
    def __init__(self, ticker: str):
        super().__init__(f"Governance Gate Blocked: Proposal for {ticker} cannot proceed without recorded human decision.")
        self.ticker = ticker

class ConfigurationError(WhartonICError):
    """Raised when a configuration file is missing, malformed, or invalid."""
    pass
