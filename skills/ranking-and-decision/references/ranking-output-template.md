# Ranking Output Template

## Output Order

Always produce the following sections in this order:

## Ranking And Decision

Use this exact top-level structure:

### Decision Question
- one short paragraph stating what must be decided

### Criteria And Constraints
- bullets listing the criteria used and any hard constraints or gates

### Ranked Options
For each option, use this exact substructure:

#### O1. [Short label]
- **What it is:** one or two sentences
- **Why it ranks here:** short explanation
- **Evidence basis:** bullets
- **Assumptions:** bullets
- **Main tradeoffs:** bullets for benefits, costs, and risks
- **Assessment:** evidence strength, expected value, feasibility, speed, learning value, resource efficiency, strategic fit, overall priority

Repeat for O2, O3, and so on.

### Recommendation
- one short paragraph naming the recommended option and why

### Sensitivity And Reversal Triggers
- bullets describing what would most likely change the decision

### Recommended Next Step
- name the next skill and explain why in one short paragraph

## Handoff Payload

Return valid YAML in a fenced code block.

Use this schema and preserve field names exactly:

```yaml
ranking_decision_handoff:
  version: "1.0"
  source_artifact_type: "research_brief|hypothesis_portfolio|experiment_plan|critique_review|mixed|unknown"
  source_payload_version: "1.0|unknown"
  decision_mode: "quick|balanced|rigorous"
  decision_question: ""
  decision_criteria:
    - criterion: ""
      weight: "high|medium|low|unknown"
      rationale: ""
  options:
    - id: "O1"
      label: ""
      option_type: "hypothesis|experiment|strategy|study_path|other"
      summary: ""
      evidence_basis:
        - statement: ""
          provenance: ""
          confidence: "high|medium|low"
      assumptions: []
      tradeoffs:
        benefits: []
        costs_or_downsides: []
        risks: []
      scores:
        evidence_strength: "high|medium|low|unknown"
        expected_value: "high|medium|low|unknown"
        feasibility: "high|medium|low|unknown"
        speed: "high|medium|low|unknown"
        learning_value: "high|medium|low|unknown"
        resource_efficiency: "high|medium|low|unknown"
        strategic_fit: "high|medium|low|unknown"
        overall_priority: "high|medium|low|unknown"
  ranked_order: []
  recommended_option_id: "O1|unknown"
  recommendation_rationale: ""
  key_tie_breakers: []
  conditions_that_would_change_decision: []
  recommended_next_skill: "study-plan-generator"
  recommended_next_action: ""
```

## Missing Information Rules

- Use empty lists where no items are available.
- Use `unknown` for short scalar fields when information is insufficient.
- Do not invent weights, evidence, or operational details.
- If the ranking is provisional, say so explicitly in both the prose section and the YAML payload.

## Compression Rules

Inside YAML:
- keep each option atomic
- keep rationale short and auditable
- avoid repeating the same evidence item across many fields
- keep `summary` concise
