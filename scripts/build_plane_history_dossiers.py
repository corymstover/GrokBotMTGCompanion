#!/usr/bin/env python3
"""Phase 5: compile source-backed, explicitly INCOMPLETE histories of registered planes.

Uses only existing graph claim edges that directly touch a Plane node. No
timeline ordering is inferred from set release dates, article dates, or eras.

  python3 scripts/build_plane_history_dossiers.py
  python3 scripts/build_plane_history_dossiers.py --check
"""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / 'data/multiverse_graph/multiverse_graph.json'
OUT = ROOT / 'data/lore_research/plane_history_dossiers_2026-10-30.json'


def digest(body: dict) -> str:
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def build() -> dict:
    graph = json.loads(GRAPH.read_text(encoding='utf-8'))
    nodes = {n['id']: n for n in graph['nodes']}
    planes = {key: node for key, node in nodes.items() if node['type'] == 'Plane'}
    facts: dict[str, list[dict]] = {key: [] for key in planes}
    for edge in graph['edges']:
        if not edge.get('claim'):
            continue
        touches = [key for key in (edge['from'], edge['to']) if key in planes]
        if not touches:
            continue
        claim = nodes.get('claim:' + edge['claim'])
        if not claim or claim['type'] != 'Claim':
            raise ValueError(f"orphan plane-history claim {edge['claim']}")
        if edge.get('grade') != claim.get('grade'):
            raise ValueError(f"conflicting grade for {edge['claim']}")
        sources = []
        for source_id in edge.get('sources', []):
            source = nodes.get('source:' + source_id)
            if not source or source.get('source_class') != 'WIZARDS_OFFICIAL':
                raise ValueError(f"missing official citation {source_id} for {edge['claim']}")
            sources.append({'id': source_id, 'title': source['name'], 'url': source['url']})
        if not sources:
            raise ValueError(f"uncited plane-history claim {edge['claim']}")
        item = {
            'claim_id': edge['claim'],
            'grade': claim['grade'],
            'statement': claim['name'],
            'limitation': claim.get('limitation', ''),
            'relation': edge['relation'],
            'subject': {'id': edge['from'], 'name': nodes[edge['from']]['name']},
            'object': {'id': edge['to'], 'name': nodes[edge['to']]['name']},
            'era_label': edge.get('era'),
            'in_universe_date': edge.get('in_universe_date'),
            'sources': sorted(sources, key=lambda s: s['id']),
        }
        for plane_id in touches:
            facts[plane_id].append(item)

    dossiers = []
    grade_counts: Counter[str] = Counter()
    for key in sorted(planes, key=lambda x: planes[x]['name'].casefold()):
        rows = sorted(facts[key], key=lambda r: (r['claim_id'], r['relation']))
        for row in rows:
            grade_counts[row['grade']] += 1
        dossiers.append({
            'id': key,
            'plane': planes[key]['name'],
            'evidence_status': 'PARTIAL_DIRECT_GRAPH_CLAIMS_ONLY',
            'distinct_claims': len({row['claim_id'] for row in rows}),
            'facts': rows,
            'known_gaps': [
                'Direct claims are not an exhaustive history of this plane.',
                'Era labels and publication dates are not a verified sequence or AR calendar year.',
                'Absence of a cited event or person is not evidence it never occurred or appeared.',
            ],
        })

    body = {
        'schema': 'plane-history-dossiers/v1',
        'as_of': '2026-10-30',
        'status': 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED',
        'source_graph_sha256': graph['content_sha256'],
        'scope': 'Only named planes presently registered as graph Plane nodes and directly incident claim edges.',
        'chronology_policy': 'Never infer ordering from article date, release date or an era_label; explicit dated quotes are retained verbatim as quoted metadata only.',
        'counts': {'registered_planes': len(planes),
                   'planes_with_direct_claims': sum(bool(p['facts']) for p in dossiers),
                   'direct_claim_edges': sum(len(p['facts']) for p in dossiers),
                   'thin_planes_fewer_than_five_claims': sum(p['distinct_claims'] < 5 for p in dossiers),
                   'claim_edge_grades': dict(sorted(grade_counts.items()))},
        'planes': dossiers,
    }
    body['content_sha256'] = digest(body)
    return body


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args(argv)
    current = build()
    if args.check:
        try:
            saved = json.loads(OUT.read_text(encoding='utf-8'))
        except FileNotFoundError:
            print('FAIL: plane-history dossiers missing')
            return 1
        if saved != current:
            print('FAIL: plane-history dossiers stale; regenerate from current graph')
            return 1
        print('PASS plane-history dossiers:', current['counts'])
        return 0
    OUT.write_text(json.dumps(current, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('Wrote source-backed, partial plane histories:', current['counts'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
