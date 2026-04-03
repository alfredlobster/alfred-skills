# Model Modes

## Recommended intent mapping
- General reasoning / writing: `prod-general`, `sonnet`, `opus`
- Coding: `prod-coding`, `prod-coding-fallback`
- Cheap testing: `test-cheap`, `test-cheapest`
- Local-only: `local-gemma`

## Current known aliases
- `prod-general` -> `openai/gpt-5.4`
- `prod-coding` -> `openai-codex/gpt-5-codex` (if available)
- `prod-coding-fallback` -> `openai-codex/gpt-5.3-codex`
- `prod-fallback` -> `mistral/mistral-large-latest`
- `test-cheap` -> `mistral/mistral-small-latest` or `openai/gpt-5.4-mini` depending on availability
- `test-cheapest` -> `openai/gpt-5.4-nano`
- `local-gemma` -> `vllm/gemma4-e4b`
- `sonnet` -> `anthropic/claude-sonnet-4-6`
- `opus` -> `anthropic/claude-opus-4-6`
