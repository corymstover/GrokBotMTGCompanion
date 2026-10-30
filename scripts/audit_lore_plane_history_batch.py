#!/usr/bin/env python3
"""Check the Kamigawa and New Phyrexia history expansion against old source IDs.

Offline structural/provenance check: --check. Optional live official-quote check: --live.
"""
import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

from audit_lore_pack_c5 import TextOnly, normalize

ROOT = Path(__file__).resolve().parents[1]
KAM = ROOT / 'data/lore_research/pack_p5_kamigawa_history_profile_2026-10-30.json'
NPH = ROOT / 'data/lore_research/pack_p5_new_phyrexia_historical_profile_2026-10-30.json'
OLD_KAM = ROOT / 'data/lore_research/pack_p5_untagged_planes_2026-10-30.json'
OLD_NEO = ROOT / 'data/lore_research/pack_p5_kamigawa_neon_dynasty_2026-10-30.json'


def audit(live=False):
    packs = [json.loads(p.read_text(encoding='utf-8')) for p in (KAM, NPH)]
    old = json.loads(OLD_KAM.read_text(encoding='utf-8'))['source_register']
    old_neo = json.loads(OLD_NEO.read_text(encoding='utf-8'))['source_register']
    expected_sources = {'up_kamigawa':old['up_kamigawa'], 'neo_guide':old_neo['neo_guide'],
                        'up_nph':old['up_nph']}
    urls = {}
    counts = []
    for pack, prefix, number in zip(packs, ('KMH', 'NPHH'), (12, 8)):
        assert pack['status'] == 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED'
        assert len(pack['claims']) == number
        assert [c['id'] for c in pack['claims']] == [f'{prefix}{i:03d}' for i in range(1, number+1)]
        entities = {e['id'] for e in pack['entities']}
        assert len(entities) == len(pack['entities'])
        for sid, source in pack['source_register'].items():
            assert source == expected_sources[sid], f'source metadata drift: {sid}'
            assert source['url'].startswith('https://magic.wizards.com/')
            urls[sid] = source['url']
        for c in pack['claims']:
            assert c['grade'] == 'CANON_CONFIRMED'
            assert c['subject'] in entities and all(o.strip() in entities for o in c['object'].split(';'))
            assert c['source_ids'] and all(s in pack['source_register'] for s in c['source_ids'])
            assert c['source_excerpt'] and c['summary'] and c['limitation']
            assert 'before' not in c['predicate'] and 'after' not in c['predicate'] or c['id'] == 'KMH007'
            if c['id'] in {'KMH002', 'KMH004'}:
                assert c['evidence'][0]['source_id'] in c['source_ids']
                assert c['source_excerpt'] in c['evidence'][0]['quote']
            assert not any(t in c for t in ('absolute_ar_year', 'approves_deck'))
        counts.append(number)
    if live:
        pages = {}
        for sid, url in urls.items():
            with urlopen(Request(url, headers={'User-Agent':'MTG-Multiverse-Companion-source-audit/1.0'}), timeout=25) as response:
                html = response.read().decode('utf-8', errors='replace')
            reader = TextOnly()
            reader.feed(html)
            pages[sid] = normalize(' '.join(reader.parts))
        for pack in packs:
            for c in pack['claims']:
                for sid in c['source_ids']:
                    assert normalize(c['source_excerpt']) in pages[sid], f"missing official quote for {c['id']}"
                for evidence in c.get('evidence', []):
                    assert normalize(evidence['quote']) in pages[evidence['source_id']], c['id']
    return {'result':'PASS','claims':sum(counts),'packs':len(packs),
            'official_sources':len(urls),'live_quotes_checked':live,
            'approval_requested':False,'inferred_ar_dates':False}


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--live', action='store_true')
    args = parser.parse_args()
    print(json.dumps(audit(live=args.live), indent=2))


if __name__ == '__main__':
    main()
