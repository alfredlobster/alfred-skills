---
name: llm-council
description: Run a Karpathy-faithful multi-model LLM Council workflow for hard idea evaluation. Use when you want parallel first opinions, anonymized peer review, aggregate ranking, chairman synthesis, and a final report from multiple models rather than a single-model answer.
---

# LLM Council

This is the top-level orchestrator skill for the LLM Council workflow.

## Stage order
1. `llm-council-intake`
2. `llm-council-first-opinions`
3. `llm-council-peer-review`
4. aggregate ranking helpers
5. `llm-council-chairman`
6. `llm-council-reporter`

## Purpose
Provide one clear entry point for running the full council process while preserving the stage-specific skill boundaries.

## Rules
- Keep the workflow faithful to Karpathy’s original 3-stage structure
- Do not skip anonymous peer review
- Do not synthesize the final answer before rankings exist
- Preserve first opinions separately from final synthesis

## Inputs
- one hard question / idea / design problem
- optional context
- council member models
- chairman model
- optional evaluation axes

## Outputs
- first-opinion artifact
- anonymized peer-review artifact
- aggregate rankings
- chairman final answer
- final report

## Use when
- evaluating hard ideas
- comparing strategic options
- reviewing architectures or plans
- stress-testing assumptions through multiple model perspectives


## Shared assets
- Common contracts, ranking logic, and runnable examples now live under `skills/llm-council-core/`.
