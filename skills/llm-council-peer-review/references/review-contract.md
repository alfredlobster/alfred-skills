# Peer Review Contract

Example shape:

```yaml
version: llm-council-peer-review-v1
task: Should we adopt an internal developer platform strategy?
anonymized_responses:
  Response A: First model response text
  Response B: Second model response text
reviews:
  - model: anthropic/claude-sonnet-4-6
    status: ok
    review_text: |
      Response A is stronger on...
      Response B is weaker on...
      FINAL RANKING:
      1. Response A
      2. Response B
    parsed_ranking:
      - Response A
      - Response B
```
