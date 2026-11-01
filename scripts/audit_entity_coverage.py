#!/usr/bin/env python3
"""Deterministic source-grade gap census for the *registered* world/entity graph.

The census is intentionally not an assertion that all MTG canon, people,
artifacts or regions are registered. A graph origin/name does not substitute
for a direct claim with an official source URL.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / 'data/multiverse_graph/multiverse_graph.json'
OUT = ROOT / 'data/lore_research/entity_coverage_audit_2026-11-01.json'
REPORT = ROOT / 'research/ENTITY_COVERAGE_AUDIT_2026-11-01.md'
KINDS = ('Plane', 'Place', 'Faction', 'Object', 'Character')
STRUCTURAL = {'cited_by', 'asserts', 'see_also_curated_entry', 'proposed_in'}
GRADES = {'CANON_CONFIRMED', 'CANON_IMPLIED', 'CANON_DISPUTED',
          'OPEN_QUESTION', 'ALTERNATE_CONTINUITY'}


def build() -> dict:
    graph = json.loads(GRAPH.read_text(encoding='utf-8'))
    nodes = {n['id']: n for n in graph['nodes']}
    if len(nodes) != len(graph['nodes']):
        raise ValueError('Duplicate graph node IDs would make entity audit ambiguous')
    sources = {n['id'].removeprefix('source:'): n for n in graph['nodes'] if n['type'] == 'Source'}
    targeted = {nid: node for nid, node in nodes.items() if node['type'] in KINDS}
    direct = defaultdict(list)
    degrees = Counter()
    for edge in graph['edges']:
        a, b = edge['from'], edge['to']
        if a not in nodes or b not in nodes:
            raise ValueError(f'Dangling graph edge: {a}, {b}')
        degrees[a] += 1
        degrees[b] += 1
        if not edge.get('claim') or edge['relation'] in STRUCTURAL:
            continue
        grade = edge.get('grade')
        if grade not in GRADES:
            raise ValueError(f'Invalid direct relationship grade: {grade}')
        urls = []
        for key in edge.get('sources', []):
            source = sources.get(key)
            url = (source or {}).get('url') or ''
            parsed = urlsplit(url)
            if (not source or source.get('source_class') != 'WIZARDS_OFFICIAL' or
                    parsed.scheme != 'https' or parsed.hostname not in
                    {'magic.wizards.com', 'www.magic.wizards.com'}):
                raise ValueError(f'Missing/non-official direct claim source: {key}')
            urls.append(source['url'])
        if not urls:
            raise ValueError(f'No official citation on direct claim {edge["claim"]}')
        for nid in {a, b} & targeted.keys():
            direct[nid].append((edge['claim'], grade, *urls))

    rows = []
    for nid, node in sorted(targeted.items(), key=lambda kv: (KINDS.index(kv[1]['type']), kv[1]['name'].casefold(), kv[0])):
        claims = {item[0] for item in direct[nid]}
        grades = sorted({item[1] for item in direct[nid]})
        urls = sorted({url for item in direct[nid] for url in item[2:]})
        if not claims:
            gap = 'NO_DIRECT_CITED_CLAIM'
        elif 'CANON_CONFIRMED' not in grades:
            gap = 'ONLY_QUALIFIED_DIRECT_CLAIMS'
        elif len(claims) == 1:
            gap = 'ONE_DIRECT_CLAIM_ONLY'
        else:
            gap = None
        rows.append({'id': nid, 'name': node['name'], 'type': node['type'],
                     'registered_origins': sorted(node.get('origins', [])),
                     'graph_incident_edges': degrees[nid],
                     'direct_distinct_claim_count': len(claims),
                     'direct_claim_ids': sorted(claims), 'direct_grades': grades,
                     'official_source_urls': urls, 'gap': gap})
    by_type = {}
    for kind in KINDS:
        group = [r for r in rows if r['type'] == kind]
        gaps = Counter(r['gap'] or 'MULTIPLE_CONFIRMED_OR_MIXED_CLAIMS' for r in group)
        by_type[kind] = {'registered': len(group), 'with_any_direct_claim': sum(r['direct_distinct_claim_count'] > 0 for r in group),
                         'without_direct_claim': gaps['NO_DIRECT_CITED_CLAIM'],
                         'with_one_direct_claim_only': gaps['ONE_DIRECT_CLAIM_ONLY'],
                         'only_qualified_direct_claims': gaps['ONLY_QUALIFIED_DIRECT_CLAIMS'],
                         'gap_counts': dict(sorted(gaps.items()))}
    priority_gaps = sorted([r for r in rows if r['gap'] in {'NO_DIRECT_CITED_CLAIM', 'ONLY_QUALIFIED_DIRECT_CLAIMS'}],
                           key=lambda r: (-r['graph_incident_edges'], KINDS.index(r['type']), r['name'].casefold()))
    report = {
        'schema': 'registered-entity-source-coverage/v1', 'as_of': '2026-11-01',
        'scope': ('Census of every currently registered Plane, Place/region, Faction, Object/artifact and Character node. '
                  'Not a census of all MTG canon or a declaration that every named entity has a complete history.'),
        'source_grade_rule': ('Only nonstructural claim edges carrying a registered, direct, official Wizards URL count. '
                              'Origin files, card-name bridges, uncited neighbors and Scryfall card metadata are not direct lore proof.'),
        'total_registered': len(rows), 'registered_by_type': by_type,
        'nodes_without_direct_claim': sum(r['gap'] == 'NO_DIRECT_CITED_CLAIM' for r in rows),
        'nodes_with_only_qualified_direct_claims': sum(r['gap'] == 'ONLY_QUALIFIED_DIRECT_CLAIMS' for r in rows),
        'priority_review_candidates': [r['id'] for r in priority_gaps[:30]],
        'all_registered_entities': rows,
        'limits': [
            'Graph registration is a curated inventory, not the universe of all MTG planes, regions, factions, objects or people.',
            'One direct claim is not a complete biography, regional survey, faction membership or object history.',
            'An officially cited disputed, implied or alternate-continuity claim is not automatically CANON_CONFIRMED.',
            'Graph degree ranks only local research connectivity, never canonical historical importance.',
            'This audit inventories evidence and gaps; it does not create unsupported lore edges or resolve contradictions.',
        ],
    }
    report['content_sha256'] = hashlib.sha256(json.dumps(report, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return report


def markdown(report: dict) -> str:
    lines = ['# Registered Multiverse planes, regions, factions, artifacts and character audit', '',
             '**2026-11-01 · source-graded coverage and explicit gaps, NOT a complete canon census.**', '',
             f"**{report['total_registered']} registered entities** across the five audited node types; "
             f"**{report['nodes_without_direct_claim']}** without a direct cited claim and "
             f"**{report['nodes_with_only_qualified_direct_claims']}** with only qualified direct claims.", '',
             '| Graph type | Registered | With direct claim | No direct claim | Qualified-only | One confirmed direct claim |',
             '| --- | ---: | ---: | ---: | ---: | ---: |']
    for kind in KINDS:
        r = report['registered_by_type'][kind]
        lines.append(f"| {kind} | {r['registered']} | {r['with_any_direct_claim']} | "
                     f"{r['without_direct_claim']} | {r['only_qualified_direct_claims']} | "
                     f"{r['with_one_direct_claim_only']} |")
    lines += ['', '## Review priority (connectivity is not canonical importance)', '',
              'These IDs have no direct cited relation or only qualified direct claims. '
              'The machine JSON records **every** registered node, each distinct direct claim ID, '
              'grade, official URL and the reason for any coverage gap.', '']
    by_id = {r['id']: r for r in report['all_registered_entities']}
    for nid in report['priority_review_candidates']:
        r = by_id[nid]
        lines.append(f"- **{r['name']}** (`{r['id']}`, {r['type']}): {r['gap']}; "
                     f"graph degree {r['graph_incident_edges']}; {r['direct_distinct_claim_count']} direct claims")
    lines += ['', '## Hard boundaries', ''] + [f'- {limit}' for limit in report['limits']]
    lines += ['', 'Rebuild: `python3 scripts/audit_entity_coverage.py`; verify: '
              '`python3 scripts/audit_entity_coverage.py --check`. '
              'A listed gap is an **actionable source-research question**, not permission to invent the missing relation.', '']
    return '\n'.join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    data = build()
    body = json.dumps(data, indent=1, ensure_ascii=False) + '\n'
    md = markdown(data)
    if args.check:
        if not OUT.is_file() or OUT.read_text(encoding='utf-8') != body or not REPORT.is_file() or REPORT.read_text(encoding='utf-8') != md:
            raise ValueError('Registered entity gap audit artifact/report stale')
    else:
        OUT.write_text(body, encoding='utf-8')
        REPORT.write_text(md, encoding='utf-8')
    print('PASS entity coverage', {'registered': data['total_registered'],
                                   'no_direct': data['nodes_without_direct_claim'],
                                   'qualified_only': data['nodes_with_only_qualified_direct_claims']})
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
