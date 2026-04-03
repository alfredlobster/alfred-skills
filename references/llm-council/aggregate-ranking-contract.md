# Aggregate Ranking Contract

## Purpose
Define how peer-review rankings are combined into a council-wide standing.

## Inputs
- parsed rankings from all successful peer-review outputs
- label-to-model mapping from the anonymization stage

## Required output
```yaml
aggregate_rankings:
  - model: anthropic/claude-sonnet-4-6
    average_rank: 1.5
    rankings_count: 3
  - model: openai/gpt-5.4
    average_rank: 2.0
    rankings_count: 3
```

## Rules
- Lower average rank is better
- Only successful, parseable rankings contribute
- Missing rankings should reduce `rankings_count`, not crash the run
- Ties should remain visible; do not force arbitrary tie-breaking beyond stable sort order
