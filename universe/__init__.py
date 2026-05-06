"""
Universe module.

Defines the eligible investment universe and enforces structural constraints
before any metrics, strategy logic, or ranking is applied.

This module is responsible for:
- Security identity and canonical representation
- Structural inclusion and exclusion rules
- Data availability flags and known limitations
"""

from .models import SecurityIdentifier, SecurityRecord, Universe
from .universe import build_universe