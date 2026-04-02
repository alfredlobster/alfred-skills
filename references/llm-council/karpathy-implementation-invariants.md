# Karpathy LLM Council — Implementation Invariants

This document captures the non-negotiable mechanics of Andrej Karpathy's `llm-council` implementation so the OpenClaw skill version stays faithful to the original design.

## Source implementation reviewed
- https://github.com/karpathy/llm-council
- README and backend orchestration logic (`backend/council.py`)

## Core 3-stage structure

### Stage 1 — First Opinions
- The same user query is sent to all council models independently.
- Responses are collected in parallel.
- Each response is preserved separately; the council does not collapse them early.
- Failed model calls may be omitted, but successful responses remain distinct.

### Stage 2 — Anonymous Peer Review and Ranking
- Stage 1 responses are anonymized as `Response A`, `Response B`, etc.
- Each council model reviews the anonymized responses.
- The review includes both:
  - qualitative evaluation of each response
  - an explicit final ranking from best to worst
- Rankings must be parseable in a deterministic way.

### Stage 3 — Chairman Synthesis
- A designated chairman model receives:
  - the original query
  - all Stage 1 responses
  - all Stage 2 peer-review/ranking outputs
- The chairman produces the final synthesized answer.
- The chairman is not a voter; it is a synthesizer.

## Non-negotiable invariants
1. **Parallel first pass**
   - First opinions must be independently generated before peer review begins.

2. **Anonymized peer review**
   - Reviewers must not know which model produced which answer.
   - This is meant to reduce model favoritism and brand bias.

3. **Explicit ranking artifact**
   - Stage 2 must produce rankings, not just comments.
   - A valid council run requires machine-readable or parser-friendly ranking output.

4. **Aggregate ranking layer**
   - Rankings from individual reviewers must be aggregated into a council-wide standing.
   - This aggregate view is part of the reasoning context for the final synthesis.

5. **Chairman as final synthesizer**
   - Final answer comes after, not before, peer review.
   - The chairman consumes both opinions and rankings.

## What the OpenClaw version must NOT drift into
- simple multi-model querying without peer review
- free-form debate without structured ranking
- majority vote with no synthesis stage
- one-model summary over first opinions only
- exposing model identities during Stage 2 review

## OpenClaw mapping suggestion
- `llm-council-intake` → normalize query + select council/chairman
- `llm-council-first-opinions` → Stage 1
- `llm-council-peer-review` → Stage 2 review + ranking
- `llm-council-chairman` → Stage 3 synthesis
- `llm-council-reporter` → final structured output

## Testing implication
Any benchmark or gold-standard example for the skill family should verify:
- independent first opinions exist
- review identities are masked
- rankings are parseable
- aggregate standings are generated
- chairman sees all prior stage outputs
