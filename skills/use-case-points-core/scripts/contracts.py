"""Function contracts and initial implementations for the deterministic UCP backend."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]


def _load_json(path: str | Path) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def classify_actor_complexity(actor: Dict[str, Any]) -> Dict[str, Any]:
    desc = (actor.get('description') or '').lower()
    if 'gui' in desc or 'user' in desc or 'human' in desc:
        classification = 'complex'
    elif 'protocol' in desc or 'transformation' in desc:
        classification = 'average'
    elif 'api' in desc or 'system' in desc or 'service' in desc:
        classification = 'simple'
    else:
        classification = 'unclassified'
    return {
        'id': actor.get('id'),
        'classification': classification,
        'classification_rationale': f'Rule-based match from description: {actor.get("description", "")}'
    }


def classify_usecase_complexity(use_case: Dict[str, Any]) -> Dict[str, Any]:
    tx = use_case.get('transaction_count')
    if tx is None:
        classification = 'unclassified'
    elif tx <= 3:
        classification = 'simple'
    elif tx <= 7:
        classification = 'average'
    else:
        classification = 'complex'
    return {
        'id': use_case.get('id'),
        'transaction_count': tx,
        'classification': classification,
    }


def count_ucp_transactions(use_case_spec: Dict[str, Any]) -> Dict[str, Any]:
    main = use_case_spec.get('main_flow') or []
    alt = use_case_spec.get('alternate_flows') or []
    exc = use_case_spec.get('exception_flows') or []
    count = len(main)
    ambiguity = []
    if not main:
        ambiguity.append('main_flow_missing')
    if any(not isinstance(x, str) or not x.strip() for x in main):
        ambiguity.append('blank_main_flow_step')
    return {
        'id': use_case_spec.get('id'),
        'transaction_count': count,
        'counting_notes': [f'Counted {count} main flow steps'],
        'ambiguity_flags': ambiguity,
        'derived_from_sections': {
            'main_flow_steps': len(main),
            'alternate_flow_entries': len(alt),
            'exception_flow_entries': len(exc),
        },
    }


def validate_rup_artifact(artifact_bundle: Dict[str, Any]) -> Dict[str, Any]:
    findings: List[Dict[str, Any]] = []
    actors = artifact_bundle.get('actors', [])
    actor_ids = {a.get('id') for a in actors}
    use_cases = artifact_bundle.get('use_cases', [])
    nfrs = artifact_bundle.get('non_functional_requirements', [])
    nfr_ids = {n.get('id') for n in nfrs}

    for actor in actors:
        if not actor.get('description'):
            findings.append({'severity': 'error', 'category': 'completeness', 'location': actor.get('id'), 'message': 'Actor missing description'})
        if actor.get('classification') == 'unclassified':
            findings.append({'severity': 'warning', 'category': 'classification_readiness', 'location': actor.get('id'), 'message': 'Actor remains unclassified'})

    for uc in use_cases:
        if not uc.get('main_flow'):
            findings.append({'severity': 'error', 'category': 'completeness', 'location': uc.get('id'), 'message': 'Use case missing main flow'})
        for aid in uc.get('primary_actor_ids', []) + uc.get('secondary_actor_ids', []):
            if aid not in actor_ids:
                findings.append({'severity': 'error', 'category': 'consistency', 'location': uc.get('id'), 'message': f'Unknown actor reference: {aid}'})
        for nfr in uc.get('nfr_refs', []):
            if nfr not in nfr_ids:
                findings.append({'severity': 'warning', 'category': 'consistency', 'location': uc.get('id'), 'message': f'Unresolved NFR reference: {nfr}'})
        if uc.get('complexity_classification') == 'unclassified':
            findings.append({'severity': 'warning', 'category': 'classification_readiness', 'location': uc.get('id'), 'message': 'Use case remains unclassified'})

    status = 'pass'
    if any(f['severity'] == 'error' for f in findings):
        status = 'fail'
    elif findings:
        status = 'warning'
    return {'version': 'ucp-validation-report-v1', 'status': status, 'findings': findings}


def _actor_weight(c: str) -> int:
    return {'simple': 1, 'average': 2, 'complex': 3}.get(c, 0)


def _use_case_weight(c: str) -> int:
    return {'simple': 5, 'average': 10, 'complex': 15}.get(c, 0)


def compute_ucp(estimation_input: Dict[str, Any]) -> Dict[str, Any]:
    actor_catalog = estimation_input['actor_catalog']
    use_case_specs = estimation_input['use_case_specs']
    actors = actor_catalog['actors']
    use_cases = use_case_specs['use_cases']

    actor_breakdown = {'simple': 0, 'average': 0, 'complex': 0}
    for a in actors:
        c = a.get('classification', 'unclassified')
        if c in actor_breakdown:
            actor_breakdown[c] += 1
    uaw = sum(actor_breakdown[k] * _actor_weight(k) for k in actor_breakdown)

    use_case_breakdown = {'simple': 0, 'average': 0, 'complex': 0}
    for uc in use_cases:
        c = uc.get('complexity_classification', 'unclassified')
        if c in use_case_breakdown:
            use_case_breakdown[c] += 1
    uucw = sum(use_case_breakdown[k] * _use_case_weight(k) for k in use_case_breakdown)

    uucp = uaw + uucw

    tcf_cfg = _load_json(ROOT / 'configs/tcf-factors.json')
    ecf_cfg = _load_json(ROOT / 'configs/ecf-factors.json')

    t_sum = sum(item['weight'] * estimation_input['tcf_ratings'][item['id']] for item in tcf_cfg['factors'])
    tcf = 0.6 + (0.01 * t_sum)
    e_sum = sum(item['weight'] * estimation_input['ecf_ratings'][item['id']] for item in ecf_cfg['factors'])
    ecf = 1.4 + (-0.03 * e_sum)
    ucp = uucp * tcf * ecf
    result = {
        'uaw_breakdown': {**actor_breakdown, 'uaw': uaw},
        'uucw_breakdown': {**use_case_breakdown, 'uucw': uucw},
        'uucp': uucp,
        'technical_factor_sum': round(t_sum, 3),
        'technical_complexity_factor': round(tcf, 3),
        'environmental_factor_sum': round(e_sum, 3),
        'environmental_complexity_factor': round(ecf, 3),
        'ucp': round(ucp, 3),
    }
    pf = estimation_input.get('productivity_factor_hours_per_ucp')
    if pf is not None:
        result['effort_hours'] = round(ucp * pf, 3)
    return result


def generate_traceability_matrix(requirements_bundle: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = []
    goals = {g['id']: g for g in requirements_bundle.get('business_goals', [])}
    for uc in requirements_bundle.get('use_case_candidates', []):
        for gid in uc.get('business_goal_ids', []):
            rows.append({
                'business_goal_id': gid,
                'business_goal': goals.get(gid, {}).get('statement'),
                'use_case_id': uc.get('id'),
                'use_case_name': uc.get('name'),
                'nfr_refs': uc.get('nfr_refs', []),
            })
    return rows
