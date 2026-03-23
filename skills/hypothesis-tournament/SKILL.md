---
name: hypothesis-tournament
description: Score competing hypotheses with reproducible pairwise comparisons and Elo-style updates. Use when the user wants hypotheses ranked by repeated head-to-head judgments instead of a one-pass list, and the output must include score, confidence, and rationale for each candidate.
---

# Hypothesis Tournament

Use this skill to score competing hypotheses with reproducible pairwise comparisons and Elo-style updates.

## Inputs
- A hypothesis set with stable candidate IDs.
- Evaluation criteria and any domain constraints.
- Tournament settings:
  - `seed`
  - `rounds`
  - `k_factor`
  - `initial_score`
  - optional `pairing_strategy`

## Required process
1. Normalize candidates into a stable list with immutable IDs.
2. Fix the run settings up front and echo them back in the output.
3. Generate pairings deterministically from the candidate IDs, `seed`, and `pairing_strategy`.
4. For each matchup, produce a comparison record using the contract in `references/pairwise-and-elo-contract.md`.
5. Apply Elo-style score updates after every comparison.
6. Aggregate per-candidate evidence across all rounds.
7. Emit a final ranking sorted by score, including confidence and rationale for every candidate.

## Pairwise comparison rules
- Compare only two candidates at a time.
- Judge against the provided criteria, not generic plausibility.
- Pick one winner for every matchup. Do not emit ties in this first slice.
- Keep rationale short and decision-relevant.
- Record enough detail to replay the score updates deterministically.

## Scoring rules
- Start every candidate at `initial_score`.
- Use standard Elo expected-score math:
  - `expected_a = 1 / (1 + 10 ^ ((score_b - score_a) / 400))`
  - `expected_b = 1 - expected_a`
  - `new_score = old_score + k_factor * (actual - expected)`
- Use `actual = 1` for the winner and `0` for the loser.
- Round only in presentation, not during intermediate updates.

## Confidence guidance
- Confidence is a band, not a claim of truth.
- Derive it from tournament evidence such as:
  - number of comparisons observed
  - score separation from nearby candidates
  - consistency of wins across rounds
- Express confidence with a compact label and a short explanation.
- If evidence is thin or unstable, say so explicitly.

## Output requirements
- Include:
  - run settings
  - ordered final ranking
  - each candidate's score
  - each candidate's confidence band
  - each candidate's rationale summary
- Use the reference contract for field names and structure.
- State any assumptions that could affect reproducibility.

## Boundaries
- This slice defines the comparison and reporting contract only.
- Do not invent Bayesian intervals or other advanced uncertainty machinery unless the user asks for it.
- If candidate quality is too underspecified to compare, stop and ask for better criteria instead of fabricating certainty.
