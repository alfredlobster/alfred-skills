---
name: llm-council-peer-review
description: Run the anonymous peer-review and ranking stage of the LLM Council workflow. Use when first-opinion responses already exist and you need models to evaluate anonymized responses, produce explicit rankings, and prepare inputs for aggregate ranking and chairman synthesis.
---

# LLM Council Peer Review

Perform Stage 2 of a Karpathy-faithful LLM Council run.

## Purpose
Take the first-opinion responses, anonymize them as `Response A`, `Response B`, etc., then ask each council model to:
1. evaluate each response qualitatively
2. produce an explicit best-to-worst ranking

## Inputs
- one `llm-council-first-opinions` artifact
- original task statement
- council model list

## Required output per reviewing model
- `model`
- `review_text`
- `parsed_ranking`
- `status`
- `error` (if failed)

## Rules
- Responses must be anonymized before review
- Reviewers must not know which model produced which answer
- Rankings must be parser-friendly and deterministic enough for aggregation
- This stage does not produce the final answer
