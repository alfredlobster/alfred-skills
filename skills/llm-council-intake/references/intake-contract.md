# LLM Council Intake Contract

Example shape:

```yaml
version: llm-council-intake-v1
task: Should we adopt an internal developer platform strategy for a 50-team engineering organization?
context:
  - current state: fragmented tooling
  - desired state: lower friction and stronger governance
council_models:
  - anthropic/claude-sonnet-4-6
  - openai/gpt-5.4
  - google/gemini-3-pro-preview
chairman_model: anthropic/claude-opus-4-6
evaluation_axes:
  - correctness
  - depth
  - practicality
  - strategic fit
notes:
  - Keep first-opinion stage independent
```
