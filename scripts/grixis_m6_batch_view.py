#!/usr/bin/env python3
"""Render a compact strategic-review batch for named human/agent judgment.

Read-only helper: never writes evidence or authority state.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--slug', default='abaddon-the-despoiler')
    ap.add_argument('--batch', type=int, default=1)
    a=ap.parse_args()
    p=ROOT/'data/grixis/m6/review_packets'/f'{a.slug}.json'
    d=json.loads(p.read_text(encoding='utf-8'))
    rows=[]
    for x in d['items']:
        if x['batch'] != a.batch:
            continue
        rows.append({
            'review_order': x['review_order'],
            'swap_id': x['swap_id'],
            'source': x['source'],
            'priority_class': x['priority_class'],
            'scrutiny': x['scrutiny'],
            'add': x['add'],
            'cut': x['cut'],
            'burden': x['burden'],
            'hypothesis': x['hypothesis'],
            'expected_benefit': x['expected_benefit'],
            'expected_cost': x['expected_cost'],
            'legality': x['legality'],
            'rules_interactions': x['rules_interactions'],
            'candidate': x['candidate'],
            'test_verdict_counts': x['test_evidence']['verdict_counts'],
            'a_f_obligations': x['a_f_obligations'],
            'flags': x['flags'],
            'refs': x['refs'],
        })
    out={
        'deck_id': d['deck_id'],
        'slug': d['slug'],
        'list_hash': d['list_hash'],
        'batch': a.batch,
        'items': rows,
        'authority': d['authority'],
    }
    print(json.dumps(out, indent=1, ensure_ascii=False, sort_keys=True))

if __name__=='__main__':
    main()
