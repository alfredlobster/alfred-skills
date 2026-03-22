# Hypothesis Output Template

## Output Order

Always produce the following sections in this order:

## Hypothesis Portfolio

Use this exact top-level structure:

### Problem Restatement
- one concise paragraph

### Evidence Basis
- short bullets summarizing the strongest relevant evidence and uncertainty

### Hypotheses
For each hypothesis, use this exact substructure:

#### H1. [Short title]
- **Statement:** one or two sentences
- **Why it could explain or improve the problem:** short rationale
- **Supporting evidence:** bullets
- **Key assumptions:** bullets
- **Discriminating tests or observations:** bullets
- **Assessment:** novelty, plausibility, impact if true, testability, overall priority

Repeat for H2, H3, and so on.

### Cross-Hypothesis Observations
- bullets about overlaps, tensions, dependencies, or sequencing

### Recommended Next Step
- name the next skill and explain why in one short paragraph

## Handoff Payload

Return valid YAML in a fenced code block.

Use this schema and preserve field names exactly:

```yaml
hypothesis_portfolio_handoff:
  version: "1.0"
  source_payload_version: "1.0|unknown"
  research_goal: ""
  problem_statement: ""
  hypothesis_generation_mode: "conservative|balanced|expansive"
  hypotheses:
    - id: "H1"
      title: ""
      statement: ""
      mechanism_or_logic: ""
      supporting_evidence:
        - statement: ""
          provenance: ""
          confidence: "high|medium|low"
      key_assumptions: []
      discriminating_tests: []
      novelty: "high|medium|low|unknown"
      plausibility: "high|medium|low|unknown"
      impact_if_true: "high|medium|low|unknown"
      testability: "high|medium|low|unknown"
      overall_priority: "high|medium|low|unknown"
  cross_hypothesis_observations: []
  recommended_next_skill: "experiment-designer"
  recommended_next_action: ""
```

## Missing Information Rules

- Use empty lists where no items are available.
- Use `unknown` for short scalar fields when the user has not supplied enough information.
- Use `null` only when absence is the clearest representation.
- Never fabricate citations, experiments, or evidentiary support.

## Compression Rules

Inside YAML:
- keep each item short and atomic
- avoid long prose paragraphs
- avoid repeating the same idea in multiple fields
- keep the `statement` and `mechanism_or_logic` fields concise
