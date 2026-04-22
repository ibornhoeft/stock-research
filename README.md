# Documentation Overview

This directory contains all architectural, conceptual, and contractual
documentation for the research assistant system.

## Document Order and Authority

1. 00_Canonical_Vision.md  
   Defines the purpose, principles, non-goals, and success criteria.
   This is the highest-authority document.

2. 01_System_Architecture.md  
   Defines module boundaries, responsibilities, and data flow.

3. interface documents (docs/interfaces/)  
   Define contracts between modules. These are treated as APIs.

4. Module documents (02–06)  
   Define domain-specific logic within approved boundaries.

## Governance Rules

- Documentation precedes implementation.
- Any cross-module dependency must be reflected in an interface document.
- AI is not permitted to generate analytical logic.

This structure is designed for durability, auditability, and handoff continuity.