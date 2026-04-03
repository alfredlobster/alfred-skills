# LLM Council Workflow

## Goal
Turn one difficult question into a multi-stage council deliberation.

## Expected run shape
1. Normalize task and council setup
2. Collect parallel first-pass answers
3. Anonymize answers and collect peer-review rankings
4. Aggregate rankings across reviewers
5. Ask the chairman model to synthesize final answer
6. Produce a structured report

## Important distinction
- First opinions show diversity of thought
- Peer review introduces comparative judgment
- Chairman output is the final synthesis, not a replacement for earlier stages
