#!/usr/bin/env python3
"""Reproducible source-local event orders across bounded plane/history accounts.

This supplements, NEVER silently rewrites, the legacy Packs A–C partial order.
Cross-strand comparisons return UNKNOWN. A narrated legend can be ordered only
*within the account* and never becomes independently confirmed canon.

  python3 scripts/source_event_sequences.py
  python3 scripts/source_event_sequences.py --check
  python3 scripts/source_event_sequences.py --live
  python3 scripts/source_event_sequences.py --list
  python3 scripts/source_event_sequences.py --compare K:konda_imprisons K:realm_barrier_breaks
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict, deque
from pathlib import Path
from urllib.request import Request, urlopen

from audit_lore_pack_c5 import TextOnly, normalize

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / 'data/lore_research/source_event_sequences_spec_2026-10-30.json'
OUT = ROOT / 'data/lore_research/source_event_sequences_2026-10-30.json'
MANIFEST = ROOT / 'data/multiverse_graph/manifest.json'
LEGACY = ROOT / 'data/lore_research/relative_chronology_2026-10-30.json'
CERTAINTIES = {'HISTORICAL_SOURCE_ACCOUNT', 'NARRATED_TRADITION_ONLY'}
RELATIONS = {'BEFORE', 'DURING_OR_AFTER_START'}


def canon(text: str) -> str:
    return normalize(text.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"'))


def digest(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def closure(ids: set[str], edges: list[dict]) -> dict[str, list[str]]:
    succ = defaultdict(list)
    for edge in edges:
        if edge['relation'] == 'BEFORE':
            succ[edge['earlier']].append(edge['later'])
    result = {}
    for start in sorted(ids):
        seen, todo = set(), list(succ[start])
        while todo:
            node = todo.pop()
            if node not in seen:
                seen.add(node)
                todo.extend(succ[node])
        if start in seen:
            raise ValueError(f'chronology cycle involving {start}')
        result[start] = sorted(seen)
    return result


def build() -> dict:
    spec = json.loads(SPEC.read_text(encoding='utf-8'))
    assert spec['schema'] == 'source-local-event-order-spec/v1'
    assert spec['status'] == 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED'
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    registered = set(manifest['claim_packs'])
    source_regs = {}
    for sid, rel in spec['sources'].items():
        if rel not in registered:
            raise ValueError(f'unregistered source claim pack {rel}')
        pack = json.loads((ROOT / rel).read_text(encoding='utf-8'))
        if sid not in pack['source_register']:
            raise ValueError(f'absent source ID {sid}')
        source_regs[sid] = pack['source_register'][sid]
    claims = {}
    for rel in registered:
        pack = json.loads((ROOT / rel).read_text(encoding='utf-8'))
        for c in pack['claims']:
            if c['id'] in claims:
                raise ValueError(f'duplicate claim ID: {c["id"]}')
            claims[c['id']] = c

    nodes, edges, strands = [], [], []
    ids: set[str] = set()
    seen_strands: set[str] = set()
    for strand in spec['strands']:
        sid, certainty = strand['id'], strand['certainty']
        if sid in seen_strands:
            raise ValueError(f'duplicate source-local strand ID: {sid}')
        seen_strands.add(sid)
        assert certainty in CERTAINTIES
        strand_ids = set()
        for node in strand['nodes']:
            nid = node['id']
            if nid in ids or not nid.startswith(sid + ':'):
                raise ValueError(f'duplicate/incorrect strand prefix {nid}')
            refs = []
            for cid in node['claim_ids']:
                if cid not in claims:
                    raise ValueError(f'unregistered referenced claim {cid}')
                grade = claims[cid]['grade']
                if certainty == 'NARRATED_TRADITION_ONLY' and grade != 'CANON_IMPLIED':
                    raise ValueError(f'legend promoted to confirmed in {nid}')
                refs.append({'id': cid, 'grade': grade})
            nodes.append({'id': nid, 'strand': sid, 'label': node['label'],
                          'certainty': certainty, 'claims': refs})
            strand_ids.add(nid)
            ids.add(nid)
        strand_edges = []
        for edge in strand['edges']:
            a, b = edge['earlier'], edge['later']
            relation = edge.get('relation', 'BEFORE')
            if a not in strand_ids or b not in strand_ids or a == b or relation not in RELATIONS:
                raise ValueError(f'invalid source-local edge {a} -> {b}')
            if edge['source_id'] not in source_regs:
                raise ValueError(f'unknown official source: {edge["source_id"]}')
            page = source_regs[edge['source_id']]
            if not page['url'].startswith('https://magic.wizards.com/'):
                raise ValueError('source is not official Wizards')
            q = edge['quote']
            if not q or not edge['note']:
                raise ValueError('missing quoted proof or limitation')
            strand_edges.append({
                'earlier': a, 'later': b, 'relation': relation,
                'certainty': certainty, 'source_id': edge['source_id'],
                'source_url': page['url'], 'source_title': page['title'],
                'quote': q, 'quote_sha256': hashlib.sha256(canon(q).encode()).hexdigest(),
                'note': edge['note'],
            })
        edges.extend(strand_edges)
        strands.append({'id': sid, 'title': strand['title'], 'certainty': certainty,
                        'limitation': strand['limitation'], 'events': len(strand_ids),
                        'strict_edges': sum(e['relation'] == 'BEFORE' for e in strand_edges),
                        'non_ordering_relations': sum(e['relation'] != 'BEFORE' for e in strand_edges)})

    # A same-event bridge is not a chronology edge. Admit it only when both
    # ledgers cite the same official page for the particular event, so the
    # separate historical accounts remain independent except for explicit IDs.
    legacy = json.loads(LEGACY.read_text(encoding='utf-8'))
    old_events = {n['id']: n for n in legacy['nodes'] if n['kind'] == 'EVENT'}
    bridges, touched, used_old, used_local = [], set(), set(), set()
    for link in spec.get('legacy_bridges', []):
        a, b, sid, quote = link['legacy'], link['local'], link['source_id'], link['quote']
        if a not in old_events or b not in ids or (a, b) in touched or a in used_old or b in used_local:
            raise ValueError(f'invalid or duplicate legacy bridge {a} <-> {b}')
        touched.add((a, b))
        used_old.add(a)
        used_local.add(b)
        if sid not in source_regs or not link.get('note') or not quote:
            raise ValueError(f'unsourced legacy bridge {a} <-> {b}')
        source = source_regs[sid]
        if not source['url'].startswith('https://magic.wizards.com/'):
            raise ValueError('cross-ledger bridge source is not official Wizards')
        corroborating = [e for e in legacy['stated_edges']
                         if a in (e['earlier'], e['later']) and e['source_url'] == source['url']
                         and canon(quote) in canon(e['quote'])]
        if not corroborating or not any(b in (e['earlier'], e['later']) and e['source_id'] == sid
                                      for e in edges):
            raise ValueError(f'bridge lacks matching original/local source evidence: {a} <-> {b}')
        bridges.append({'legacy':a,'local':b,'relation':'SAME_EVENT',
                        'source_id':sid,'source_url':source['url'],'source_title':source['title'],
                        'quote':quote,'quote_sha256':hashlib.sha256(canon(quote).encode()).hexdigest(),
                        'note':link['note']})

    paths = closure(ids, edges)
    out = {
        'schema': 'source-event-sequences/v1',
        'status': 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED',
        'date': '2026-10-30',
        'scope': spec['scope'],
        'sources': {sid: {'url': src['url'], 'title': src['title'], 'published': src.get('published')}
                    for sid, src in sorted(source_regs.items())},
        'counts': {'strands':len(strands), 'events':len(nodes), 'strict_edges':sum(e['relation'] == 'BEFORE' for e in edges),
                   'non_ordering_relations':sum(e['relation'] != 'BEFORE' for e in edges),
                   'ordered_pairs':sum(len(reach) for reach in paths.values()),
                   'total_pairs':len(nodes)*(len(nodes)-1)//2,
                   'verified_legacy_bridges':len(bridges)},
        'strands': strands, 'nodes': sorted(nodes, key=lambda n: n['id']),
        'edges': edges, 'legacy_bridges': bridges, 'precedes': paths,
        'known_gaps': [
            'No primary-source edge joins distinct source-local strand IDs. Only explicitly source-corroborated SAME_EVENT links join the legacy and source-local ledgers; all other cross-ledger comparisons remain UNKNOWN.',
            'Valley events order an explicitly legendary in-world account, not objectively certified ancient history.',
            'New Phyrexia events describe early Mirrodin conquest; the source does not order the complete war, the Mirrans being overwhelmed against Venser\'s sacrifice, or the political present after March of the Machine.',
            'Muraganda: the ancient collapse versus moon-shattering sequence, the exact overlap of moon-strikes and survivor cultures, and the origin of the modern Autocracy remain unbridged.',
            'Meditation Realm: Ugin\'s remembered early conflict does not date or establish the Realm\'s condition after Tarkir: Dragonstorm; the fall of Ugin is not a claim of permanent death.',
            'Thran to first invasion: the 2008 historical retrospective does not establish a strict order between the soul-bomb decimation of Old Phyrexia and the Weatherlight Legacy destroying Yawgmoth.',
            'The Weatherlight leaves Mercadia to defend Dominaria after its strike, but the 2008 account does not strictly date that departure against the later Rath overlay.',
            'Original Mirrodin history in the 2008 account is an independent H strand: its mysterious contagion is not automatically identified with later oil accounts or assigned a relative order against the New Phyrexia P strand.',
            'The official Dominaria synopsis and 2008 Kamigawa explanation establish a Dominarian-rift effect on Kamigawa, but not the strict order of the Kami War, the Mending and the Phyrexian invasion.',
            'Karn\'s creation is independently source-bridged to the legacy ledger; his later profile-era motives and world corruption do not automatically establish a SAME_EVENT link to the separate 2008 Mirrodin contagion account.',
            'Serra\'s Realm: the retrospective does not order the end of Radiant\'s administration relative to Urza\'s final powerstone extraction, even though both follow Serra\'s departure.',
            'A DURING_OR_AFTER_START relation is not a strict BEFORE edge and never participates in transitive ordering.',
            'Unknown original plane names, absolute AR years and missing historical events are not supplied.',
            'This source-local supplement does not replace the original Packs A–C chronology or certify L244.',
        ],
    }
    out['content_sha256'] = digest(out)
    return out


def live_check() -> dict:
    data = build()
    pages = {}
    for sid, source in data['sources'].items():
        with urlopen(Request(source['url'], headers={'User-Agent':'MTG-Multiverse-Companion-chronology/1.0'}), timeout=30) as response:
            reader = TextOnly()
            reader.feed(response.read().decode('utf-8', errors='replace'))
        pages[sid] = canon(' '.join(reader.parts))
    for edge in data['edges'] + data['legacy_bridges']:
        if canon(edge['quote']) not in pages[edge['source_id']]:
            raise ValueError(f"source quote missing live: {edge.get('earlier', edge.get('legacy'))} -> {edge.get('later', edge.get('local'))}")
    return {'result': 'PASS', 'live_checked_quotes':len(data['edges'])+len(data['legacy_bridges']), 'pages':len(pages)}


def proof(data: dict, left: str, right: str) -> dict:
    nodes = {n['id']:n for n in data['nodes']}
    if left not in nodes or right not in nodes:
        raise ValueError('unknown source-sequence event ID; use --list')
    if left == right:
        return {'result':'SAME_EVENT', 'left':left, 'right':right, 'proof':[], 'confidence':'QUALIFIED'}
    if nodes[left]['strand'] != nodes[right]['strand']:
        return {'result':'UNKNOWN', 'left':left, 'right':right, 'proof':[], 'confidence':'UNRESOLVED',
                'limitation':'No primary-source chronology path compares these separate planes or traditions.'}
    strand = next(s for s in data['strands'] if s['id'] == nodes[left]['strand'])
    adjacency = defaultdict(list)
    for edge in data['edges']:
        if edge['relation'] == 'BEFORE':
            adjacency[edge['earlier']].append(edge)
    def path(a, b):
        todo = deque([(a, [])]);seen={a}
        while todo:
            current, steps=todo.popleft()
            if current == b:return steps
            for e in adjacency[current]:
                if e['later'] not in seen:
                    seen.add(e['later']);todo.append((e['later'],steps+[e]))
        return None
    forward=path(left,right)
    backward=None if forward is not None else path(right,left)
    if forward is not None:
        result, steps='BEFORE',forward
    elif backward is not None:
        result, steps='AFTER',backward
    else:
        overlap = [e for e in data['edges'] if e['earlier']==left and e['later']==right and e['relation']!='BEFORE']
        result, steps=('DURING_OR_AFTER_START',overlap) if overlap else ('UNKNOWN',[])
    return {'result':result, 'left':left,'right':right, 'proof':steps,
            'confidence':'QUALIFIED_LEGENDARY_SEQUENCE' if strand['certainty']=='NARRATED_TRADITION_ONLY'
                         else 'QUALIFIED_OFFICIAL_SOURCE_SEQUENCE' if steps else 'UNRESOLVED',
            'limitation':strand['limitation'] if steps else 'No supported source-local strict order connects these events.'}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group=p.add_mutually_exclusive_group()
    group.add_argument('--check',action='store_true')
    group.add_argument('--live',action='store_true')
    group.add_argument('--list',action='store_true')
    group.add_argument('--compare',nargs=2,metavar=('EVENT_A','EVENT_B'))
    args=p.parse_args(argv)
    if args.live:
        print(json.dumps(live_check(),indent=2));return 0
    data=build()
    if args.check:
        saved=json.loads(OUT.read_text(encoding='utf-8'))
        if saved!=data:
            raise SystemExit('STALE: regenerate source-event sequences')
        print('PASS source-local chronology',data['counts']);return 0
    if args.list:
        print(json.dumps(data['nodes'],indent=2));return 0
    if args.compare:
        print(json.dumps(proof(data,*args.compare),indent=2));return 0
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Wrote source-local chronology:',data['counts'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
