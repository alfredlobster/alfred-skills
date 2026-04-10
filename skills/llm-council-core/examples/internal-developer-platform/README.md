# Example: Internal Developer Platform Decision

## Prompt
Should we adopt an internal developer platform strategy for a 50-team engineering organization?

## Included artifacts
- `intake.yaml`
- `first-opinions.yaml`
- `peer-review.yaml`
- `chairman.yaml`

## Expected interpretation
- First opinions should remain independent and inspectable
- Peer review should rank anonymized responses, not named models
- Aggregate ranking should show why one response rose above the others
- Chairman output should synthesize, not overwrite, the earlier process

## Review questions
- Are the first opinions genuinely distinct?
- Are the rankings parseable and auditable?
- Does the chairman answer reflect both top-ranked insight and disagreement where relevant?
