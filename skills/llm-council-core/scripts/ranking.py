"""Deterministic helpers for the LLM Council ranking stage."""

from __future__ import annotations

import re
from collections import defaultdict
from typing import Dict, List, Any


def parse_ranking_from_text(review_text: str) -> List[str]:
    if 'FINAL RANKING:' in review_text:
        section = review_text.split('FINAL RANKING:', 1)[1]
        numbered = re.findall(r'\d+\.\s*Response [A-Z]', section)
        if numbered:
            return [re.search(r'Response [A-Z]', m).group() for m in numbered]
        fallback = re.findall(r'Response [A-Z]', section)
        if fallback:
            return fallback
    return re.findall(r'Response [A-Z]', review_text)


def calculate_aggregate_rankings(peer_reviews: List[Dict[str, Any]], label_to_model: Dict[str, str]) -> List[Dict[str, Any]]:
    positions = defaultdict(list)
    for review in peer_reviews:
        ranking = review.get('parsed_ranking') or []
        for idx, label in enumerate(ranking, start=1):
            if label in label_to_model:
                positions[label_to_model[label]].append(idx)
    aggregate = []
    for model, vals in positions.items():
        aggregate.append({
            'model': model,
            'average_rank': round(sum(vals) / len(vals), 2),
            'rankings_count': len(vals)
        })
    aggregate.sort(key=lambda x: (x['average_rank'], x['model']))
    return aggregate
