---
name: model-switcher
description: Switch Alfred's default model profile intentionally and safely. Use when changing the default model for general work, coding, cheap testing, or local-first experiments, and you want a consistent policy instead of ad hoc config edits.
---

# Model Switcher

Use this skill when changing Alfred's default model behavior.

## Typical targets
- `prod-general` → strong default for general non-coding work
- `prod-coding` / `prod-coding-fallback` → coding-focused work
- `test-cheap` → cheap experiments
- `test-cheapest` → minimal-cost quick tests
- `local-gemma` → local-only lightweight testing
- `sonnet` / `opus` → Anthropic writing/reasoning

## Workflow
1. Identify the desired mode (general / coding / cheap / local).
2. Resolve alias to concrete provider/model.
3. Update the default model config.
4. Restart/reload the gateway if required.
5. Verify with model list or a simple test call.

## Safety rules
- Do not silently change the default model without surfacing it to Peter.
- Prefer local/cheap models for experimentation.
- Prefer stronger reasoning models for production-critical work.
- Keep coding and non-coding defaults conceptually separate.

## Output
Always state:
- old default
- new default
- why the switch was made
- whether restart/verification succeeded
