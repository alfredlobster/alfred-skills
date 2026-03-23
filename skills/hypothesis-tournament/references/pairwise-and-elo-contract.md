# Pairwise Comparison And Elo Output Contract

This reference defines the minimum record shape for deterministic hypothesis-tournament runs.

## Run settings

```yaml
run:
  method: hypothesis_tournament_v1
  seed: 17
  rounds: 3
  k_factor: 24
  initial_score: 1500
  pairing_strategy: round_robin_seeded
```

Rules:
- `method` is fixed to `hypothesis_tournament_v1` for this contract version.
- The same candidates, settings, and seed must produce the same pair sequence and score updates.

## Candidate record

```yaml
candidate:
  id: H1
  label: Targeted anti-inflammatory mechanism
  summary: Explains symptom reduction through a specific pathway.
```

Rules:
- `id` must be stable within the run.
- `label` is short human-readable text.
- `summary` is optional but preferred.

## Pairwise comparison record

```yaml
comparison:
  round: 1
  matchup_id: R1-H1-vs-H3
  candidate_a: H1
  candidate_b: H3
  winner: H1
  criteria:
    - explanatory_power
    - falsifiability
    - evidence_fit
  rationale: H1 better explains the observed effect while remaining testable.
  score_before:
    H1: 1500
    H3: 1500
  expected:
    H1: 0.5
    H3: 0.5
  actual:
    H1: 1
    H3: 0
  score_after:
    H1: 1512
    H3: 1488
```

Rules:
- `winner` must equal either `candidate_a` or `candidate_b`.
- `matchup_id` must be unique within the run.
- `rationale` should justify the decision in one or two sentences.
- `score_before`, `expected`, `actual`, and `score_after` must be sufficient to replay the update exactly.

## Final ranking record

```yaml
ranking:
  - rank: 1
    candidate_id: H1
    score: 1543.7
    confidence:
      band: high
      explanation: Consistent wins across rounds and a clear margin over adjacent candidates.
    rationale_summary: Strongest overall fit to the criteria across repeated head-to-head matchups.
  - rank: 2
    candidate_id: H3
    score: 1508.4
    confidence:
      band: medium
      explanation: Mixed record with moderate separation from the next cluster.
    rationale_summary: Competitive on evidence fit but less complete on explanatory power.
```

Rules:
- Every candidate must appear exactly once.
- Sort by `score` descending.
- `confidence.band` should use a compact ordinal set such as `low`, `medium`, or `high`.
- `rationale_summary` must reflect tournament evidence, not only prior intuition.

## Minimal report sections
- `run`
- `comparisons`
- `ranking`

These sections are enough for orchestrators or reporters to consume the result without inferring hidden state.
