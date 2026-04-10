from __future__ import annotations
import yaml, json
from pathlib import Path
from contracts import anonymize_first_opinions, calculate_aggregate_rankings

ROOT = Path(__file__).resolve().parents[2]
EX = ROOT.parent / 'examples' / 'internal-developer-platform'

first = yaml.safe_load(open(EX / 'first-opinions.yaml', 'r', encoding='utf-8'))
peer = yaml.safe_load(open(EX / 'peer-review.yaml', 'r', encoding='utf-8'))

anon = anonymize_first_opinions(first['responses'])
agg = calculate_aggregate_rankings(peer['reviews'], anon['label_to_model'])

print(json.dumps({
    'anonymized': anon,
    'aggregate_rankings': agg,
}, indent=2))
