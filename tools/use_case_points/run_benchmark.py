from __future__ import annotations
import json
from pathlib import Path
import yaml
from contracts import compute_ucp

ROOT = Path(__file__).resolve().parents[2]
EX = ROOT / 'examples' / 'use-case-points' / 'customer-onboarding'

with open(EX / 'rup-actor-catalog.yaml', 'r', encoding='utf-8') as f:
    actor_catalog = yaml.safe_load(f)
with open(EX / 'rup-usecase-spec.yaml', 'r', encoding='utf-8') as f:
    use_case_specs = yaml.safe_load(f)
with open(EX / 'expected-estimate.yaml', 'r', encoding='utf-8') as f:
    expected = yaml.safe_load(f)

inp = {
    'version': 'ucp-estimation-input-v1',
    'actor_catalog': actor_catalog,
    'use_case_specs': use_case_specs,
    'tcf_ratings': expected['run']['tcf_ratings'],
    'ecf_ratings': expected['run']['ecf_ratings'],
}
actual = compute_ucp(inp)
print(json.dumps({'expected': {
    'uaw': expected['actor_breakdown']['uaw'],
    'uucw': expected['use_case_breakdown']['uucw'],
    'uucp': expected['uucp'],
    'technical_factor_sum': expected['technical_factor_sum'],
    'technical_complexity_factor': expected['technical_complexity_factor'],
    'environmental_factor_sum': expected['environmental_factor_sum'],
    'environmental_complexity_factor': expected['environmental_complexity_factor'],
    'ucp': expected['ucp'],
}, 'actual': actual}, indent=2))
