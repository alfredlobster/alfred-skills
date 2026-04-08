---
name: web-service-security-audit
description: Audit one or more public web services for obvious low-hanging security flaws using local-only tooling. Use when you need a safe white-hat surface review of a website or API endpoint: TLS sanity, HTTP→HTTPS behavior, response headers, cookie flags, CORS posture, TRACE / OPTIONS, and common sensitive-file exposure checks, with a structured JSON/Markdown report.
---

# Web Service Security Audit

Use this skill for **authorized, low-impact** security reviews of public web services.

## What it does
- probes HTTP and HTTPS reachability
- checks redirect behavior
- inspects TLS certificate basics
- checks common security headers
- checks cookie flags from `Set-Cookie`
- checks CORS posture with a synthetic `Origin`
- checks `OPTIONS` / `Allow`
- checks whether `TRACE` appears enabled
- checks a short list of common sensitive paths for obvious exposure
- writes JSON and Markdown findings

## What it does not do
- brute force
- exploit vulnerabilities
- fuzz aggressively
- bypass auth
- do high-volume content discovery
- rely on SaaS scanners

## Workflow
1. Confirm target(s) are authorized.
2. Run the local audit script against one target or a newline-delimited targets file.
3. Review `summary`, `findings`, and evidence.
4. If needed, follow up manually with narrower checks.

## Execution
Single target:

```bash
python skills/web-service-security-audit/scripts/audit_web_service.py \
  --target https://example.com \
  --output-dir /tmp/web-audit-example
```

Targets file:

```bash
python skills/web-service-security-audit/scripts/audit_web_service.py \
  --targets-file ./targets.txt \
  --output-dir /tmp/web-audit-batch
```

## Output files
- `security-audit-report.json`
- `security-audit-report.md`

## Safety rules
- Use only for targets Peter owns or is explicitly authorized to assess.
- Keep checks low-impact and deterministic.
- Prefer evidence-backed findings over speculative claims.
- Mark uncertain issues as `warning` or `info`, not `critical`.
