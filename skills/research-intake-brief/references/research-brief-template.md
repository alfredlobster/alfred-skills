# Research Brief Template

## Output Order

Always produce the following sections in this order:

## Research Brief

Use this exact top-level structure:

### Problem Framing
- one concise paragraph

### Objective
- one concise paragraph or short bullet list

### Success Criteria
- bullets

### Constraints
- bullets

### Evidence and Context
- short synthesized bullets or compact paragraphs

### Assumptions
- bullets

### Unknowns
- bullets

### Candidate Hypothesis Directions
- short bullets with rationale

### Risks and Confounders
- bullets

### Recommended Next Step
- name the next skill and explain why in one short paragraph

## Handoff Payload

Return valid YAML in a fenced code block.

Use this schema and preserve field names exactly:

```yaml
research_brief_handoff:
  version: "1.0"
  mode: "fast|guided|rigorous"
  research_goal: ""
  problem_statement: ""
  domain_context: ""
  success_criteria: []
  constraints: []
  provided_materials:
    - type: "note|paper|metadata|question|problem-statement|other"
      description: ""
      provenance: "user-provided|uploaded|web|connector|inferred"
  known_facts:
    - statement: ""
      provenance: ""
      confidence: "high|medium|low"
  user_claims_needing_validation: []
  inferred_assumptions: []
  unknowns: []
  literature_context:
    summary: ""
    key_points: []
  candidate_hypothesis_directions:
    - title: ""
      rationale: ""
      confidence: "high|medium|low"
  risks_and_confounders: []
  recommended_next_skill: "hypothesis-generator"
  recommended_next_action: ""
```

## Missing Information Rules

- Use empty lists where no items are available.
- Use `"unknown"` for short scalar fields when the user has not supplied enough information.
- Use `null` only when absence is the clearest representation.
- Never fabricate citations, papers, experiments, or factual support.

## Compression Rules

Inside YAML:
- keep each item short and atomic
- avoid long prose paragraphs
- avoid repeating the same idea in multiple fields
- keep rationale to one or two sentences at most
