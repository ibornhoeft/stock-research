#### File Index — Chief Architect (CA)

#### docs/INDEX/INDEX_CA.md
- this file
- owned and maintained by Chief Architect

#### docs/TODO/TODO_CA.md
- architectural backlog and design decisions

#### docs/00_Canonical_Vision.md
- constitutional document
- defines purpose and non-negotiable rules

#### docs/01_System_Architecture.md
- defines module boundaries and data flow

#### docs/interfaces/
- all interface specifications (CA-owned governance)

#### docs/CHAT_CONTINUITY_GUIDE.md
- defines AI roles, restart rules, and handoff protocols

#### AI_HANDOFF.md
- global project state
- CA is responsible for accuracy and updates

---

#### Architecture Summary

CA governs the system:

Vision → Architecture → Interfaces → Enforcement

No module is allowed to drift outside defined boundaries.

---

#### Cross-Role Dependencies

CA depends on:
- all roles for implementation feedback

CA must NOT:
- perform module-level work unnecessarily
- violate modular separation

---

#### Design Constraints

- Documentation must precede implementation
- Interfaces must remain explicit
- No hidden logic