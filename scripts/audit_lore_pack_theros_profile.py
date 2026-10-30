#!/usr/bin/env python3
"""Verify ten concise Theros plane-primer claims against Wizards' official page.

  python3 scripts/audit_lore_pack_theros_profile.py --check
  python3 scripts/audit_lore_pack_theros_profile.py --live
"""

import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

from audit_lore_pack_c5 import TextOnly, normalize

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'data/lore_research/pack_p5_theros_plane_profile_2026-10-30.json'
ORIGINAL = ROOT / 'data/lore_research/pack_p5_theros_ths_2026-10-30.json'
OFFICIAL = 'https://magic.wizards.com/en/story/theros-plane'


def audit(page_html=None) -> dict:
    d = json.loads(PACK.read_text(encoding='utf-8'))
    old = json.loads(ORIGINAL.read_text(encoding='utf-8'))
    assert d['status'] == 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED'
    assert d['source_register']['ths_plane'] == old['source_register']['ths_plane']
    assert d['source_register']['ths_plane']['url'] == OFFICIAL
    assert [c['id'] for c in d['claims']] == [f'THP{i:03d}' for i in range(1, 11)]
    entities = {e['id'] for e in d['entities']}
    assert {'theros', 'theros_gods', 'meletis', 'akros', 'setessa'} <= entities
    assert len(entities) == len(d['entities'])
    for claim in d['claims']:
        assert claim['grade'] == 'CANON_CONFIRMED' and claim['source_ids'] == ['ths_plane']
        assert claim['subject'] in entities
        assert all(obj.strip() in entities for obj in claim['object'].split(';'))
        assert claim['source_excerpt'] and claim['summary'] and claim['limitation']
        assert 'before' not in claim['predicate'] and 'after' not in claim['predicate']
    if page_html is not None:
        reader = TextOnly()
        reader.feed(page_html)
        txt = normalize(' '.join(reader.parts))
        for claim in d['claims']:
            if normalize(claim['source_excerpt']) not in txt:
                raise ValueError(f"{claim['id']}: excerpt absent from live official Theros page")
    return {'status': 'PASS', 'claims': len(d['claims']), 'source_url': OFFICIAL,
            'live_quote_check': page_html is not None, 'owner_approval': False,
            'inferred_chronological_order': False}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--check', action='store_true')
    group.add_argument('--live', action='store_true')
    args = parser.parse_args(argv)
    page = None
    if args.live:
        with urlopen(Request(OFFICIAL, headers={'User-Agent': 'MTG-Multiverse-Companion-lore-source-check/1.0'}), timeout=18) as response:
            page = response.read().decode('utf-8', errors='replace')
    print(json.dumps(audit(page), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
