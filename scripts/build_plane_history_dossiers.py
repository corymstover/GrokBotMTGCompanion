#!/usr/bin/env python3
"""Phase 5: compile source-backed, explicitly INCOMPLETE histories of registered planes.

Direct facts use existing graph claim edges incident on a Plane. A separate
manually curated section exposes *already cited* same-plane story claims;
these remain CONTEXTUAL and never become new direct graph edges. No timeline
ordering is inferred from publication dates, set dates or era labels.

  python3 scripts/build_plane_history_dossiers.py
  python3 scripts/build_plane_history_dossiers.py --check
"""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.request import Request, urlopen

from audit_lore_pack_c5 import TextOnly, normalize


ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / 'data/multiverse_graph/multiverse_graph.json'
OUT = ROOT / 'data/lore_research/plane_history_dossiers_2026-10-30.json'
CONTEXT = ROOT / 'data/lore_research/plane_context_claims_spec_2026-10-30.json'
MANIFEST = ROOT / 'data/multiverse_graph/manifest.json'


def digest(body: dict) -> str:
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def curated_context(graph: dict, nodes: dict, direct_facts: dict) -> tuple[dict, list]:
    """Reviewable context links, not invented claim-to-plane relations."""
    spec = json.loads(CONTEXT.read_text(encoding='utf-8'))
    if spec['schema'] != 'curated-plane-context-spec/v1':
        raise ValueError('unknown curated-context schema')
    registered = set(json.loads(MANIFEST.read_text(encoding='utf-8'))['claim_packs'])
    result = {k: [] for k in direct_facts}
    bridge_sources = []
    for entry in spec['entries']:
        plane_id, pack_path = entry['plane_id'], entry['pack']
        if plane_id not in result or pack_path not in registered:
            raise ValueError(f'unknown plane or unregistered claim pack: {plane_id}, {pack_path}')
        pack = json.loads((ROOT / pack_path).read_text(encoding='utf-8'))
        plane_local_id = plane_id.removeprefix('plane:')
        if entry['basis'] == 'ON_PLANE_GUIDE_WITH_EXPLICIT_PLANE_ENTITY' or entry['basis'] == 'ON_PLANE_STORY_WITH_EXPLICIT_PLANE_ENTITY':
            if not any(e['id'] == plane_local_id and e['type'] == 'Plane' for e in pack['entities']):
                raise ValueError(f'pack does not explicitly register its plane: {pack_path}')
        elif entry['basis'] == 'EXTERNAL_OFFICIAL_STRIXHAVEN_ARCAVIOS_LOCATION_BRIDGE':
            bridge = entry['official_bridge']
            if plane_id != 'plane:arcavios' or not bridge['url'].startswith('https://magic.wizards.com/') or not bridge['quote']:
                raise ValueError('invalid Arcavios geography bridge')
            bridge_sources.append({'plane_id':plane_id,'source_url':bridge['url'],
                                   'quote':bridge['quote'],
                                   'quote_sha256':hashlib.sha256(normalize(bridge['quote']).encode()).hexdigest()})
        else:
            raise ValueError('unproven on-plane association')
        available = {c['id']: c for c in pack['claims']}
        direct = {f['claim_id'] for f in direct_facts[plane_id]}
        if len(entry['claim_ids']) != len(set(entry['claim_ids'])):
            raise ValueError('duplicate contextual claim within plane')
        for cid in entry['claim_ids']:
            if cid not in available or cid in direct:
                raise ValueError(f'unknown or already directly attached claim {cid} on {plane_id}')
            c = available[cid]
            node = nodes.get('claim:' + cid)
            if not node or node['grade'] != c['grade'] or node['name'] != c['summary']:
                raise ValueError(f'drifted claim grade or wording: {cid}')
            source_evidence = []
            for e in c.get('evidence', []):
                sid = e['source_id']
                if sid not in c['source_ids'] or sid not in pack['source_register']:
                    raise ValueError(f'invalid source reference for {cid}')
                source = pack['source_register'][sid]
                graph_source = nodes.get('source:' + sid)
                if (not graph_source or graph_source.get('source_class') != 'WIZARDS_OFFICIAL'
                        or graph_source['url'] != source['url'] or not source['url'].startswith('https://magic.wizards.com/')
                        or not e['quote']):
                    raise ValueError(f'unverified original Wizards citation for {cid}')
                source_evidence.append({'source_id':sid,'title':source['title'],
                                        'url':source['url'],'quote':e['quote'],
                                        'quote_sha256':hashlib.sha256(normalize(e['quote']).encode()).hexdigest()})
            if not source_evidence:
                raise ValueError(f'missing quote evidence {cid}')
            rels = []
            for edge in graph['edges']:
                if edge.get('claim') == cid and edge['from'] in nodes and edge['to'] in nodes:
                    rels.append({'subject':nodes[edge['from']]['name'], 'relation':edge['relation'],
                                 'object':nodes[edge['to']]['name']})
            if not rels:
                raise ValueError(f'original claim has no graph relation: {cid}')
            result[plane_id].append({
                'claim_id':cid, 'grade':c['grade'], 'statement':c['summary'],
                'limitation':c.get('limitation') or '', 'source_pack':pack_path,
                'basis':'CURATED_ON_PLANE_STORY_CONTEXT_NOT_DIRECT_GRAPH_EDGE',
                'scope_note':entry['scope_note'], 'era_label_not_order':c.get('event_stage'),
                'relations':sorted(rels,key=lambda r:(r['subject'],r['relation'],r['object'])),
                'source_evidence':source_evidence,
            })
    for plane_id in result:
        result[plane_id].sort(key=lambda c:c['claim_id'])
    return result, bridge_sources


def live_bridges() -> dict:
    """Audit only the *new* geographic bridge; prior story quotes retain original pack audits."""
    graph=json.loads(GRAPH.read_text(encoding='utf-8'))
    nodes={n['id']:n for n in graph['nodes']}
    planes={k:[] for k,n in nodes.items() if n['type']=='Plane'}
    _,bridges=curated_context(graph,nodes,planes)
    for bridge in bridges:
        with urlopen(Request(bridge['source_url'],headers={'User-Agent':'MTG-Multiverse-Companion-plane-context/1.0'}),timeout=25) as response:
            reader=TextOnly();reader.feed(response.read().decode('utf-8',errors='replace'))
        if normalize(bridge['quote']) not in normalize(' '.join(reader.parts)):
            raise ValueError(f"live official location bridge missing: {bridge['plane_id']}")
    return {'result':'PASS','live_official_geographic_bridges':len(bridges)}


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

    context, bridges = curated_context(graph, nodes, facts)
    dossiers = []
    grade_counts: Counter[str] = Counter()
    for key in sorted(planes, key=lambda x: planes[x]['name'].casefold()):
        rows = sorted(facts[key], key=lambda r: (r['claim_id'], r['relation']))
        for row in rows:
            grade_counts[row['grade']] += 1
        dossiers.append({
            'id': key,
            'plane': planes[key]['name'],
            'evidence_status': 'PARTIAL_DIRECT_AND_SEPARATELY_CURATED_CONTEXT',
            'distinct_claims': len({row['claim_id'] for row in rows}),
            'facts': rows,
            'contextual_claims': context[key],
            'known_gaps': [
                'Direct claims are not an exhaustive history of this plane.',
                'Curated same-plane story context is not a direct claim-to-plane edge and does not prove the geography of every participant in an entire arc.',
                'Era labels and publication dates are not a verified sequence or AR calendar year.',
                'Absence of a cited event or person is not evidence it never occurred or appeared.',
            ],
        })

    body = {
        'schema': 'plane-history-dossiers/v2',
        'as_of': '2026-10-30',
        'status': 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED',
        'source_graph_sha256': graph['content_sha256'],
        'scope': 'Named graph Plane nodes, direct incident claims, and an independently labeled curated subset of already cited on-plane story claims.',
        'chronology_policy': 'Never infer ordering from article date, release date or an era_label; explicit dated quotes are retained verbatim as quoted metadata only.',
        'counts': {'registered_planes': len(planes),
                   'planes_with_direct_claims': sum(bool(p['facts']) for p in dossiers),
                   'direct_claim_edges': sum(len(p['facts']) for p in dossiers),
                   'thin_planes_fewer_than_five_claims': sum(p['distinct_claims'] < 5 for p in dossiers),
                   'planes_with_curated_context':sum(bool(p['contextual_claims']) for p in dossiers),
                   'distinct_contextual_claims':sum(len(p['contextual_claims']) for p in dossiers),
                   'claim_edge_grades': dict(sorted(grade_counts.items()))},
        'curated_context_source':str(CONTEXT.relative_to(ROOT)),
        'official_geographic_bridges':bridges,
        'planes': dossiers,
    }
    body['content_sha256'] = digest(body)
    return body


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--live', action='store_true')
    args = parser.parse_args(argv)
    if args.live:
        print(live_bridges())
        return 0
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
