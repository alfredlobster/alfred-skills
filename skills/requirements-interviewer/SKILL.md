---
name: requirements-interviewer
description: Conduct structured stakeholder interviews for Use Case Point Estimation and emit a normalized intermediate YAML document. Use when eliciting business requirements in natural language from stakeholders who do not know UML or RUP, and you need structured facts for downstream RUP translation and deterministic estimation.
---

# Requirements Interviewer

Elicit business requirements in business language only.

## Purpose
Capture stakeholder intent and normalize it into the canonical intermediate schema for downstream transformation.

## Output boundary
This skill must output only the intermediate YAML structure defined by:
- `skills/use-case-points-core/schemas/requirements-interview.schema.json`

Do **not** produce UML, formal RUP artifacts, estimates, or diagrams.

## Interview phases
1. Opening
   - clarify stakeholder role, business objective, and scope
2. Exploration
   - actors, triggers, outcomes, steps, exceptions, constraints
3. Validation
   - read back assumptions, missing details, and open questions

## Interview rules
- Use business language, not modeling jargon
- Ask one clarifying question at a time when ambiguity matters
- Distinguish between:
  - main success flow
  - alternate flows
  - exception flows
- Capture NFRs explicitly when they appear
- Preserve open questions rather than guessing

## Final output
Return a YAML object that validates against the requirements interview schema.
