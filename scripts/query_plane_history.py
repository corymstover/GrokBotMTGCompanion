#!/usr/bin/env python3
"""Read-only Phase 5 official-source history lookup by registered plane name.

  python3 scripts/query_plane_history.py Dominaria
  python3 scripts/query_plane_history.py Phyrexia --json
"""

import argparse
from itertools import groupby
import json

import build_plane_history_dossiers as H


def query(name: str) -> dict:
    dossier = json.loads(H.OUT.read_text(encoding='utf-8'))
    matches = [p for p in dossier['planes']
               if p['plane'].casefold() == name.strip().casefold()
               or p['id'].removeprefix('plane:').replace('_', ' ').casefold() == name.strip().casefold()]
    if not matches:
        return {'status': 'NOT_FOUND', 'query': name,
                'note': 'No matching Plane node in the current partial graph; this does not establish nonexistence.'}
    p = matches[0]
    return {'status': 'PARTIAL_OFFICIAL_GRAPH_HISTORY', 'query': name, 'plane': p,
            'note': dossier['chronology_policy']}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('plane', help='Registered plane name, e.g. Dominaria')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    result = query(args.plane)
    if args.json or result['status'] == 'NOT_FOUND':
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result['status'] != 'NOT_FOUND' else 2
    plane = result['plane']
    print(f"{plane['plane']}: {plane['distinct_claims']} direct cited graph claims — PARTIAL, NOT A COMPLETE HISTORY")
    for claim_id, group in groupby(plane['facts'], key=lambda item: item['claim_id']):
        relations = list(group)
        fact = relations[0]
        print(f"\n[{fact['grade']}] {fact['claim_id']}: {fact['statement']}")
        for linked in relations:
            print(f"  Relation: {linked['subject']['name']} → {linked['relation']} → {linked['object']['name']}")
        if fact['era_label']:
            print(f"  Era label (NOT a dated order): {fact['era_label']}")
        if fact['in_universe_date']:
            print(f"  In-universe date quote: {fact['in_universe_date'].get('quote', 'unspecified')}")
        if fact['limitation']:
            print(f"  Limitation: {fact['limitation']}")
        for source in fact['sources']:
            print(f"  Official source: {source['title']} — {source['url']}")
    print('\nLIMITATION: The graph is incomplete; neither the ordering nor the absence of other history is established.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
