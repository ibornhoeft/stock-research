"""
Universe-specific exceptions.

These are raised only when structural assumptions are violated.
No exception in this module should encode strategy logic or metric interpretation.
"""


class UniverseError(Exception):
    """Base class for universe-related errors."""
    pass


class InvalidSecurityError(UniverseError):
    """Raised when a security violates universe-level constraints."""
    pass


class IdentifierError(UniverseError):
    """Raised when security identity cannot be resolved safely."""
    pass