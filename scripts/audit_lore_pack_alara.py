#!/usr/bin/env python3
"""Audit ten distinct Alara plane-history claims; optionally verify official live wording.

  python3 scripts/audit_lore_pack_alara.py --check
  python3 scripts/audit_lore_pack_alara.py --live
"""

import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

from audit_lore_pack_c5 import TextOnly, normalize


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'data/lore_research/pack_p5_alara_plane_profile_2026-10-30.json'
SOURCE_PACK = ROOT / 'data/lore_research/pack_p5_untagged_planes_2026-10-30.json'
OFFICIAL = 'https://magic.wizards.com/en/story/alara-plane'


def audit(page_html=None) -> dict:
    pack = json.loads(PACK.read_text(encoding='utf-8'))
    earlier = json.loads(SOURCE_PACK.read_text(encoding='utf-8'))
    assert pack['status'] == 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED'
    assert pack['source_register']['up_alara'] == earlier['source_register']['up_alara']
    assert pack['source_register']['up_alara']['url'] == OFFICIAL
    assert [x['id'] for x in pack['claims']] == [f'ALA{i:03d}' for i in range(1, 11)]
    entities = {e['id'] for e in pack['entities']}
    assert {'alara', 'bant', 'esper', 'grixis_shard', 'jund', 'naya'} <= entities
    assert len(entities) == len(pack['entities'])
    for claim in pack['claims']:
        assert claim['grade'] == 'CANON_CONFIRMED'
        assert claim['source_ids'] == ['up_alara']
        assert claim['subject'] in entities
        assert all(part.strip() in entities for part in claim['object'].split(';'))
        assert claim['summary'] and claim['source_excerpt'] and claim['limitation']
        assert 'before' not in claim['predicate'] and 'after' not in claim['predicate']
    if page_html is not None:
        reader = TextOnly()
        reader.feed(page_html)
        body = normalize(' '.join(reader.parts))
        for claim in pack['claims']:
            if normalize(claim['source_excerpt']) not in body:
                raise ValueError(f"{claim['id']} short excerpt not verbatim on official Wizards page")
    return {'status': 'PASS', 'claims': len(pack['claims']),
            'source_url': OFFICIAL, 'live_quote_check': page_html is not None,
            'owner_approval': False, 'inferred_in_world_order': False}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--check', action='store_true')
    group.add_argument('--live', action='store_true')
    args = parser.parse_args(argv)
    body = None
    if args.live:
        with urlopen(Request(OFFICIAL, headers={'User-Agent': 'MTG-Multiverse-Companion-lore-source-check/1.0'}), timeout=18) as response:
            body = response.read().decode('utf-8', errors='replace')
    print(json.dumps(audit(body), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
