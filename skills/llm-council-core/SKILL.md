---
name: llm-council-core
description: Shared contracts, ranking logic, references, and runnable examples for the LLM Council workflow. Read when maintaining or packaging the LLM Council skills so all common assets live under skills/ instead of repo-root folders.
---

# LLM Council Core

This folder is the shared home for reusable LLM Council assets that were previously split across repo-level `tools/llm_council`, `references/llm-council`, and `examples/llm-council`.

## Contents
- `scripts/` — contracts, ranking logic, and example runners
- `references/` — shared contracts and implementation notes
- `examples/` — canonical example artifacts and README files

## Intent
- Keep shared council assets self-contained under `skills/`
- Let the council subskills reference one canonical location
- Reduce repo-root sprawl and make packaging cleaner
