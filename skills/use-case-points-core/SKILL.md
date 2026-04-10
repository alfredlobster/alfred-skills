---
name: use-case-points-core
description: Shared schemas, factor configs, and deterministic contracts for the Use Case Points workflow. Read when maintaining UCP-related skills or validating that UCP assets are packaged in a self-contained location under skills/.
---

# Use Case Points Core

This folder is the shared home for reusable UCP assets that were previously scattered across repo-level `schemas/`, `configs/`, and `tools/` locations.

## Contents
- `schemas/` — JSON schemas for interview, RUP artifacts, estimation input, and validation report
- `configs/` — actor/use-case classification rules plus TCF/ECF factor definitions
- `scripts/contracts.py` — deterministic calculator / validation helper module
- `references/README.md` — original notes from the former repo-level tools folder

## Intent
- Keep UCP assets self-contained under `skills/`
- Let multiple UCP skills reference a single canonical shared location
- Reduce repo-root sprawl and make packaging cleaner
