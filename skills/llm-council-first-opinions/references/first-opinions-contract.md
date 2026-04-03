# First Opinions Contract

Example shape:

```yaml
version: llm-council-first-opinions-v1
task: Should we adopt an internal developer platform strategy for a 50-team engineering organization?
responses:
  - model: anthropic/claude-sonnet-4-6
    status: ok
    response: |
      Yes, but only if...
  - model: openai/gpt-5.4
    status: ok
    response: |
      The decision depends on...
  - model: google/gemini-3-pro-preview
    status: error
    error: timeout
```

Notes:
- Preserve original wording for downstream anonymous review.
- Do not attach rankings at this stage.
```
