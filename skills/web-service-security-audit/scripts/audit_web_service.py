#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import socket
import ssl
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse, urljoin
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import URLError, HTTPError

USER_AGENT = "Alfred-Web-Service-Security-Audit/0.1"
TEST_ORIGIN = "https://audit-origin.invalid"
SENSITIVE_PATHS = [
    "/.env",
    "/.git/HEAD",
    "/config.json",
    "/openapi.json",
    "/swagger.json",
    "/server-status",
    "/actuator/health",
    "/debug/default/view",
    "/backup.zip",
]
SECURITY_HEADERS = {
    "strict-transport-security": "Missing HSTS header",
    "x-content-type-options": "Missing X-Content-Type-Options header",
    "content-security-policy": "Missing Content-Security-Policy header",
    "x-frame-options": "Missing X-Frame-Options header",
    "referrer-policy": "Missing Referrer-Policy header",
}


class NoRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


@dataclass
class Finding:
    severity: str
    title: str
    target: str
    evidence: str
    recommendation: str
    category: str


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_target(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        return raw
    if not raw.startswith(("http://", "https://")):
        raw = "https://" + raw
    return raw


def opener_no_redirect():
    return build_opener(NoRedirectHandler())


def request_once(url: str, method: str = "GET", headers: dict | None = None, timeout: int = 10, body: bytes | None = None):
    req = Request(url, data=body, method=method, headers={"User-Agent": USER_AGENT, **(headers or {})})
    op = opener_no_redirect()
    start = time.time()
    try:
        with op.open(req, timeout=timeout) as resp:
            body = resp.read(4096)
            return {
                "ok": True,
                "url": url,
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "body_preview": body.decode("utf-8", errors="replace"),
                "elapsed_ms": int((time.time() - start) * 1000),
                "error": None,
            }
    except HTTPError as e:
        try:
            body = e.read(4096)
            preview = body.decode("utf-8", errors="replace")
        except Exception:
            preview = ""
        return {
            "ok": False,
            "url": url,
            "status": e.code,
            "headers": dict(e.headers.items()) if e.headers else {},
            "body_preview": preview,
            "elapsed_ms": int((time.time() - start) * 1000),
            "error": str(e),
        }
    except Exception as e:
        return {
            "ok": False,
            "url": url,
            "status": None,
            "headers": {},
            "body_preview": "",
            "elapsed_ms": int((time.time() - start) * 1000),
            "error": str(e),
        }


def tls_info(hostname: str, port: int = 443, timeout: int = 8):
    ctx = ssl.create_default_context()
    with socket.create_connection((hostname, port), timeout=timeout) as sock:
        with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            return {"certificate": cert, "cipher": cipher, "version": ssock.version()}


def check_target(target: str):
    findings: list[Finding] = []
    evidence = {}
    base = normalize_target(target)
    parsed = urlparse(base)
    host = parsed.hostname
    if not host:
        findings.append(Finding("critical", "Invalid target", target, base, "Provide a valid URL or hostname.", "input"))
        return findings, evidence

    https_url = base if parsed.scheme == "https" else f"https://{host}"
    http_url = f"http://{host}"
    root_https = request_once(https_url, method="GET")
    root_http = request_once(http_url, method="GET")
    evidence["root_https"] = root_https
    evidence["root_http"] = root_http

    if not root_https["ok"] and root_https["status"] is None:
        findings.append(Finding("high", "HTTPS unreachable", target, root_https["error"] or "No HTTPS response", "Ensure HTTPS is available and reachable.", "transport"))
    if root_http.get("status") in (200, 204):
        findings.append(Finding("medium", "HTTP served without redirect", target, f"HTTP {root_http['status']} at {http_url}", "Redirect HTTP to HTTPS or disable plain HTTP.", "transport"))
    elif root_http.get("status") in (301, 302, 307, 308):
        location = root_http["headers"].get("Location") or root_http["headers"].get("location", "")
        if not str(location).startswith("https://"):
            findings.append(Finding("medium", "HTTP redirect not clearly upgrading to HTTPS", target, f"Location={location}", "Ensure HTTP redirects directly to HTTPS.", "transport"))

    if root_https["headers"]:
        hdrs = {k.lower(): v for k, v in root_https["headers"].items()}
        for header, msg in SECURITY_HEADERS.items():
            if header not in hdrs:
                findings.append(Finding("medium", msg, target, f"Header absent: {header}", f"Set {header} with an appropriate policy.", "headers"))
        if hdrs.get("access-control-allow-origin") == "*":
            findings.append(Finding("medium", "Wildcard CORS on root response", target, "Access-Control-Allow-Origin: *", "Restrict cross-origin access unless intentionally public and safe.", "cors"))
        cookies = [v for k, v in root_https["headers"].items() if k.lower() == "set-cookie"]
        for cookie in cookies:
            c = cookie.lower()
            if "secure" not in c:
                findings.append(Finding("medium", "Cookie missing Secure flag", target, cookie, "Mark cookies Secure over HTTPS.", "cookies"))
            if "httponly" not in c:
                findings.append(Finding("medium", "Cookie missing HttpOnly flag", target, cookie, "Mark session cookies HttpOnly unless JS access is required.", "cookies"))
            if "samesite" not in c:
                findings.append(Finding("low", "Cookie missing SameSite attribute", target, cookie, "Set SameSite=Lax or Strict where appropriate.", "cookies"))

    cors_resp = request_once(https_url, method="GET", headers={"Origin": TEST_ORIGIN})
    evidence["cors_probe"] = cors_resp
    cors_headers = {k.lower(): v for k, v in cors_resp["headers"].items()}
    if cors_headers.get("access-control-allow-origin") == "*":
        findings.append(Finding("medium", "Wildcard CORS with arbitrary Origin", target, cors_headers.get("access-control-allow-origin", ""), "Restrict allowed origins.", "cors"))
    if cors_headers.get("access-control-allow-credentials", "").lower() == "true" and cors_headers.get("access-control-allow-origin") == "*":
        findings.append(Finding("high", "CORS allows credentials with wildcard origin", target, json.dumps(cors_headers), "Never combine ACAO=* with credentials.", "cors"))

    cors_preflight = request_once(
        https_url,
        method="OPTIONS",
        headers={
            "Origin": TEST_ORIGIN,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "authorization,content-type,x-api-key",
        },
    )
    evidence["cors_preflight"] = cors_preflight
    preflight_headers = {k.lower(): v for k, v in cors_preflight["headers"].items()}
    if cors_preflight.get("status") == 200 and preflight_headers.get("access-control-allow-origin") == "*":
        findings.append(Finding("medium", "Permissive CORS preflight response", target, json.dumps(preflight_headers), "Tighten preflight origin policy to intended callers only.", "cors"))
    if preflight_headers.get("access-control-allow-credentials", "").lower() == "true" and preflight_headers.get("access-control-allow-origin") == "*":
        findings.append(Finding("high", "Preflight allows credentials with wildcard origin", target, json.dumps(preflight_headers), "Do not allow credentials with wildcard origin on preflight responses.", "cors"))
    allow_headers = (preflight_headers.get("access-control-allow-headers") or "").lower()
    if "authorization" in allow_headers or "x-api-key" in allow_headers:
        findings.append(Finding("info", "Preflight advertises auth-related headers", target, preflight_headers.get("access-control-allow-headers", ""), "Verify that auth-bearing browser requests are intended and CORS-restricted appropriately.", "cors"))

    auth_probe = request_once(
        https_url,
        method="GET",
        headers={
            "Origin": TEST_ORIGIN,
            "Authorization": "Bearer obviously-invalid-token",
            "Cookie": "session=obviously-invalid",
        },
    )
    evidence["auth_probe"] = auth_probe
    auth_headers = {k.lower(): v for k, v in auth_probe["headers"].items()}
    if auth_probe.get("status") == 200:
        findings.append(Finding("high", "Authenticated-style request unexpectedly succeeded", target, f"Status 200 with invalid auth material at {https_url}", "Verify authentication enforcement for this route.", "auth"))
    if auth_headers.get("access-control-allow-origin") == "*":
        findings.append(Finding("medium", "Wildcard CORS on auth-flavored request", target, json.dumps(auth_headers), "Restrict cross-origin behavior on authenticated or credential-bearing flows.", "cors"))
    if auth_headers.get("access-control-allow-credentials", "").lower() == "true" and auth_headers.get("access-control-allow-origin") == "*":
        findings.append(Finding("high", "Auth-flavored response combines wildcard origin with credentials", target, json.dumps(auth_headers), "Restrict credentialed cross-origin responses.", "cors"))

    options_resp = request_once(https_url, method="OPTIONS")
    trace_resp = request_once(https_url, method="TRACE")
    evidence["options_probe"] = options_resp
    evidence["trace_probe"] = trace_resp
    allow_hdr = options_resp["headers"].get("Allow") or options_resp["headers"].get("allow", "")
    if "TRACE" in allow_hdr.upper() or trace_resp.get("status") not in (None, 400, 403, 405, 501):
        findings.append(Finding("medium", "TRACE may be enabled", target, f"OPTIONS Allow={allow_hdr}; TRACE status={trace_resp.get('status')}", "Disable TRACE unless explicitly needed.", "methods"))

    sensitive_results = []
    for path in SENSITIVE_PATHS:
        url = urljoin(https_url.rstrip('/') + '/', path.lstrip('/'))
        resp = request_once(url, method="GET")
        sensitive_results.append({"path": path, "status": resp["status"], "error": resp["error"], "preview": resp["body_preview"][:200]})
        if resp.get("status") == 200:
            findings.append(Finding("high", "Potential sensitive path exposed", target, f"{path} returned 200", f"Restrict or remove public access to {path}.", "exposure"))
    evidence["sensitive_paths"] = sensitive_results

    try:
        tinfo = tls_info(host)
        cert = tinfo["certificate"]
        evidence["tls"] = {
            "version": tinfo["version"],
            "cipher": tinfo["cipher"],
            "subject": cert.get("subject"),
            "issuer": cert.get("issuer"),
            "notAfter": cert.get("notAfter"),
        }
        not_after = cert.get("notAfter")
        if not_after:
            expiry = parsedate_to_datetime(not_after)
            days_left = (expiry - datetime.now(expiry.tzinfo)).days
            if days_left < 14:
                findings.append(Finding("high", "TLS certificate expires soon", target, f"Certificate expires in {days_left} days", "Renew certificate before expiry.", "tls"))
            elif days_left < 30:
                findings.append(Finding("medium", "TLS certificate expiry approaching", target, f"Certificate expires in {days_left} days", "Plan certificate renewal soon.", "tls"))
    except Exception as e:
        evidence["tls"] = {"error": str(e)}
        findings.append(Finding("medium", "Unable to inspect TLS certificate", target, str(e), "Verify TLS configuration and certificate availability.", "tls"))

    if not findings:
        findings.append(Finding("info", "No obvious low-hanging issues found in safe surface audit", target, "Checks completed without clear findings.", "Consider deeper manual validation if needed.", "summary"))
    return findings, evidence


def render_markdown(results: list[dict]) -> str:
    lines = ["# Web Service Security Audit", "", f"Generated: {iso_now()}", ""]
    for result in results:
        lines += [f"## {result['target']}", ""]
        lines += [f"- Findings: {len(result['findings'])}", ""]
        for f in result["findings"]:
            lines += [f"### [{f['severity'].upper()}] {f['title']}", "", f"- Category: {f['category']}", f"- Evidence: {f['evidence']}", f"- Recommendation: {f['recommendation']}", ""]
    return "\n".join(lines)


def parse_args():
    p = argparse.ArgumentParser(description="Low-impact local security audit of public web services")
    p.add_argument("--target", action="append", default=[], help="Target URL or hostname; can be repeated")
    p.add_argument("--targets-file", help="Newline-delimited target list")
    p.add_argument("--output-dir", required=True, help="Directory for JSON/Markdown reports")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    targets = [t for t in args.target if t.strip()]
    if args.targets_file:
        targets += [line.strip() for line in Path(args.targets_file).read_text().splitlines() if line.strip() and not line.strip().startswith("#")]
    if not targets:
        print("No targets supplied", file=sys.stderr)
        return 2

    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    results = []
    for target in targets:
        findings, evidence = check_target(target)
        results.append({
            "target": normalize_target(target),
            "checked_at": iso_now(),
            "findings": [asdict(f) for f in findings],
            "evidence": evidence,
        })

    report = {
        "generated_at": iso_now(),
        "tool": "web-service-security-audit",
        "target_count": len(results),
        "results": results,
    }
    json_path = outdir / "security-audit-report.json"
    md_path = outdir / "security-audit-report.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    md_path.write_text(render_markdown(results) + "\n")
    print(json.dumps({"ok": True, "json": str(json_path), "markdown": str(md_path), "targets": len(results)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
