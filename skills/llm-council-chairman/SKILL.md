---
name: llm-council-chairman
description: Run the chairman synthesis stage of the LLM Council workflow. Use when first opinions, peer reviews, and aggregate rankings already exist and you need a final synthesized answer that reflects both the independent model outputs and the council's ranked judgments.
---

# LLM Council Chairman

Perform Stage 3 of a Karpathy-faithful LLM Council run.

## Purpose
The chairman consumes the original task, all first opinions, and the peer-review/ranking results, then produces the final synthesized answer.

## Inputs
- original task
- first opinions artifact
- peer review artifact
- aggregate rankings

## Output boundary
This stage outputs only the final synthesized answer plus minimal metadata.
It must not rerun peer review or alter the aggregate rankings.

## Rules
- The chairman is a synthesizer, not a voter
- It must consider:
  - the original task
  - all first-pass answers
  - all peer-review notes
  - the aggregate council standing
- It should resolve disagreement where possible and surface uncertainty where necessary
