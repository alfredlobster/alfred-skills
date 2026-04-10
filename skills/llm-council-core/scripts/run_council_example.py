from __future__ import annotations
import json
from pathlib import Path
import yaml
from ranking import calculate_aggregate_rankings

ROOT = Path(__file__).resolve().parents[2]
EX = ROOT.parent / 'examples' / 'internal-developer-platform'

intake = yaml.safe_load(open(EX / 'intake.yaml', 'r', encoding='utf-8'))
first = yaml.safe_load(open(EX / 'first-opinions.yaml', 'r', encoding='utf-8'))
peer = yaml.safe_load(open(EX / 'peer-review.yaml', 'r', encoding='utf-8'))
chair = yaml.safe_load(open(EX / 'chairman.yaml', 'r', encoding='utf-8'))

label_to_model = {
    'Response A': first['responses'][0]['model'],
    'Response B': first['responses'][1]['model'],
    'Response C': first['responses'][2]['model'],
}
agg = calculate_aggregate_rankings(peer['reviews'], label_to_model)

report = {
    'task': intake['task'],
    'council_models': intake['council_models'],
    'chairman_model': intake['chairman_model'],
    'first_opinions_count': len(first['responses']),
    'peer_reviews_count': len(peer['reviews']),
    'aggregate_rankings': agg,
    'final_response': chair['final_response'],
}

print(json.dumps(report, indent=2))
