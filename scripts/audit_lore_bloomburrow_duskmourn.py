#!/usr/bin/env python3
"""Audit Valley's legendary history and Duskmourn's origin without status inflation.

--check verifies pack structure, IDs, source identity and epistemic grade;
--live additionally checks every excerpt against the original Wizards pages.
"""
import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

from audit_lore_pack_c5 import TextOnly, normalize

ROOT = Path(__file__).resolve().parents[1]
PACKS = (
    ROOT / 'data/lore_research/pack_p5_bloomburrow_valley_history_2026-10-30.json',
    ROOT / 'data/lore_research/pack_p5_duskmourn_origin_2026-10-30.json',
)
OLD = (
    ROOT / 'data/lore_research/pack_p5_bloomburrow_2026-10-30.json',
    ROOT / 'data/lore_research/pack_p5_duskmourn_2026-10-30.json',
)


def audit(live=False):
    packs = [json.loads(x.read_text(encoding='utf-8')) for x in PACKS]
    old = [json.loads(x.read_text(encoding='utf-8')) for x in OLD]
    docs = {}
    for pack, previous, prefix, length in zip(packs, old, ('BLH', 'DH'), (13, 12)):
        assert pack['status'] == 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED'
        assert [c['id'] for c in pack['claims']] == [f'{prefix}{i:03d}' for i in range(1, length+1)]
        entities = {e['id'] for e in pack['entities']}
        assert len(entities) == len(pack['entities'])
        for source_id, entry in pack['source_register'].items():
            assert previous['source_register'][source_id] == entry
            assert entry['url'].startswith('https://magic.wizards.com/')
            docs[source_id] = entry['url']
        for c in pack['claims']:
            assert c['grade'] in ('CANON_CONFIRMED', 'CANON_IMPLIED')
            assert c['subject'] in entities
            assert all(obj.strip() in entities for obj in c['object'].split(';'))
            assert c['source_excerpt'] and c['summary'] and c['limitation']
            assert c['source_ids'] and all(s in pack['source_register'] for s in c['source_ids'])
            assert not any(key in c for key in ('absolute_ar_year', 'owner_approved'))
    blh, dh = packs
    assert all(c['grade'] == 'CANON_IMPLIED' for c in blh['claims'][:11]), 'Valley legend promoted to fact'
    assert blh['claims'][-1]['subject'] == 'valley', 'Valley local governance improperly expanded to the entire plane'
    assert dh['claims'][1]['grade'] == 'CANON_IMPLIED', 'Artifact hints promoted to confirmed fact'
    assert dh['claims'][0]['predicate'] == 'original_name_forgotten'
    assert blh['claims'][4]['evidence'][0]['quote'].startswith('For two generations')
    if live:
        text_by_source = {}
        for sid, url in docs.items():
            with urlopen(Request(url, headers={'User-Agent':'MTG-Multiverse-Companion-lore-audit/1.0'}), timeout=30) as response:
                reader = TextOnly()
                reader.feed(response.read().decode('utf-8', errors='replace'))
            text_by_source[sid] = normalize(' '.join(reader.parts))
        for pack in packs:
            for c in pack['claims']:
                for sid in c['source_ids']:
                    if normalize(c['source_excerpt']) not in text_by_source[sid]:
                        raise ValueError(f"{c['id']}: quote not found in {sid}")
                for ev in c.get('evidence', []):
                    if normalize(ev['quote']) not in text_by_source[ev['source_id']]:
                        raise ValueError(f"{c['id']}: dated evidence quote not found")
    return {'status':'PASS', 'claims':sum(len(p['claims']) for p in packs), 'official_sources':len(docs),
            'live':live, 'no_legend_promotion':True, 'no_deck_changes':True}


def main():
    parser = argparse.ArgumentParser()
    opts = parser.add_mutually_exclusive_group(required=True)
    opts.add_argument('--check', action='store_true')
    opts.add_argument('--live', action='store_true')
    args = parser.parse_args()
    print(json.dumps(audit(live=args.live), indent=2))


if __name__ == '__main__':
    main()
