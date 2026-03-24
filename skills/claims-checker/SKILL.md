---
name: claims-checker
description: Verify whether claims in an article are actually supported by their cited references. Use when reviewing drafts, blog posts, reports, or manuscripts that contain factual claims with URLs, citations, or DOIs, and you need to confirm source validity, accessibility, and evidentiary support.
---

# Claims Checker

Verify claims against their cited references.

## What this skill checks
For each claim/reference pair:
1. Does the reference exist and resolve?
2. Is it accessible and readable?
3. Is it the intended source (not a dead redirect, login wall, or wrong page)?
4. Does the source support the claim?
5. If not fully supported, is it partial, contradicted, or unverifiable?

## Use this skill when
- A draft article contains linked references
- You need citation verification before publication
- You want DOI-preferred validation where possible
- You need to detect dead links, soft-404s, and unsupported claims

## Workflow
1. Parse the article into claim/reference pairs.
2. Validate each reference first:
   - working URL / DOI resolution
   - final destination after redirects
   - readable content available
3. Extract the relevant source content.
4. Compare claim vs source.
5. Assign one verdict:
   - Supported
   - Partially supported
   - Not supported
   - Contradicted
   - Unverifiable
6. Produce a structured report using `references/report-template.md`.

## Source rules
- Prefer DOI-backed sources where available.
- Only cite references that actually resolve and are accessible.
- If a source is dead, inaccessible, or ambiguous, mark it explicitly.
- Do not treat a secondary summary as equivalent to a primary source unless clearly stated.

## Output requirements
Always produce:
1. Executive summary
2. Per-claim verification table
3. Broken/invalid reference list
4. Recommended fixes

## Quality bar
- No fabricated support
- No “probably supported” language without evidence
- No duplicated wording across verdicts or summary
- If the evidence is weak, say so plainly
