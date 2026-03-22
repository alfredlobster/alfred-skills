# Escalation and Next Skills

Preserve compatibility with the upstream `research-intake-brief` and `hypothesis-generator` skills.

## Input assumptions

The most reliable input is a structured YAML handoff. If both prose and YAML are present:
1. trust the YAML for structure
2. use the prose for nuance and context
3. never upgrade a low-confidence YAML inference into a fact without saying so

## Recommended next skills

Choose exactly one next skill.

- `critic-reviewer`
  - use when the plan needs challenge, red-teaming, confounder analysis, or stress-testing
- `ranking-and-decision`
  - use when multiple experiments or strategies need prioritization against constraints
- `study-plan-generator`
  - use when the user wants a broader phased program, roadmap, or execution plan

## Handoff preservation rules

- Keep `version` unchanged unless the schema actually changes.
- Preserve provenance labels.
- Preserve confidence labels.
- Append open questions instead of silently dropping them.
