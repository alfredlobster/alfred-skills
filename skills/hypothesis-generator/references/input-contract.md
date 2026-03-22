# Input Contract

## Preferred upstream payload

When present, consume this upstream structure from `research-intake-brief`:

```yaml
research_brief_handoff:
  version: "1.0"
  mode: "fast|guided|rigorous"
  research_goal: ""
  problem_statement: ""
  domain_context: ""
  success_criteria: []
  constraints: []
  provided_materials: []
  known_facts: []
  user_claims_needing_validation: []
  inferred_assumptions: []
  unknowns: []
  literature_context:
    summary: ""
    key_points: []
  candidate_hypothesis_directions: []
  risks_and_confounders: []
  recommended_next_skill: "hypothesis-generator"
  recommended_next_action: ""
```

## Consumption rules

If the payload is present:
- treat it as the canonical structure
- preserve `research_goal`, `problem_statement`, `constraints`, and uncertainty fields unless the user explicitly corrects them
- use `candidate_hypothesis_directions` as starting cues, not final hypotheses
- use prose outside the YAML only to enrich nuance, examples, or evidence details

If both payload and prose conflict:
- prefer direct user corrections made later in the conversation
- otherwise preserve the conflict explicitly in the portfolio or handoff payload
- do not silently resolve contested points

## Minimal fallback frame

If no payload is available, reconstruct this minimum internally before generating hypotheses:
- research goal
- problem statement
- strongest known facts
- major assumptions
- critical unknowns
- key constraints

Ask follow-up questions only if these gaps would materially change the hypothesis set.
