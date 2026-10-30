#!/usr/bin/env python3
"""Look up complete historical set/card printing history from GitHub-readable files.

Source: frozen October 28 historical shard archive. Default filter: English
paper printings released by October 29, 2026. Does not need Scryfall bulk.
"""
import argparse
import hashlib
import json
from datetime import date
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data/set_atlas'


@lru_cache(maxsize=64)
def load(bucket, kind, folder=DATA):
    """Cache immutable published JSON buckets for full-catalog acceptance queries."""
    return json.loads((folder / f'historical_{kind}_{bucket}.json').read_text(encoding='utf-8'))


def selected(record, cutoff, future=False, digital=False, foreign=False):
    # Per-set row = [printing_id, oracle_id, name, collector, date, language, paper]
    if not foreign and record[5] != 'en':
        return False
    if not digital and not record[6]:
        return False
    if not future and date.fromisoformat(record[4]) > cutoff:
        return False
    return True


def set_query(code, folder=DATA, cutoff=date(2026, 10, 29), **flags):
    group = load(hashlib.sha256(code.encode()).hexdigest()[0], 'sets', folder)
    if code not in group:
        raise KeyError(f'Unknown historical set code: {code}')
    cache, identities = {}, {}
    printing_count = 0
    for record in group[code]:
        if not selected(record, cutoff, **flags):
            continue
        printing_count += 1
        oid = record[1]
        key = oid or 'unresolved:' + record[0]
        if key not in identities:
            status = 'unresolved identity' if not oid else 'reprint'
            if oid:
                bucket = oid[0].lower()
                if bucket not in cache:
                    cache[bucket] = load(bucket, 'cards', folder)
                history = cache[bucket][oid]
                eligible = [(p[0], p[5]) for p in history if selected(p[1:], cutoff, **flags)]
                if eligible:
                    debut = min(day for _, day in eligible)
                    first_sets = {setcode for setcode, day in eligible if day == debut}
                    if any(p[4] == debut for p in group[code] if p[1] == oid and selected(p, cutoff, **flags)):
                        status = 'tied debut' if len(first_sets) > 1 else 'debut'
            identities[key] = {'name': record[2], 'oracle_id': oid,
                               'classification': status, 'printings': 0}
        identities[key]['printings'] += 1
    cards = sorted(identities.values(), key=lambda x: (x['name'].casefold(), x['oracle_id'] or ''))
    return {'set_code': code, 'distinct_identities_or_unresolved': len(cards),
            'printing_records': printing_count, 'cards': cards}


def card_query(name_or_oid, folder=DATA, cutoff=date(2026, 10, 29), **flags):
    target = name_or_oid.casefold()
    buckets = [target[0]] if len(target) == 36 and target[0] in '0123456789abcdef' else '0123456789abcdef'
    matches = []
    for bucket in buckets:
        for oid, history in load(bucket, 'cards', folder).items():
            if oid.casefold() != target and not any(
                    p[3].casefold() == target or
                    target in [face.strip().casefold() for face in p[3].split(' // ')]
                    for p in history):
                continue
            eligible = [p for p in history if selected(p[1:], cutoff, **flags)]
            if eligible:
                matches.append({
                    'oracle_id': oid, 'name': eligible[0][3],
                    'printings': [{'set': p[0], 'printing_id': p[1],
                                   'collector_number': p[4], 'released_at': p[5]}
                                  for p in sorted(eligible, key=lambda x: (x[5], x[0], x[4]))]})
    return {'query': name_or_oid, 'matched_identities': len(matches), 'cards': matches}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--as-of', type=date.fromisoformat, default=date(2026, 10, 29))
    p.add_argument('--include-future', action='store_true')
    p.add_argument('--include-digital', action='store_true')
    p.add_argument('--include-foreign', action='store_true')
    p.add_argument('--all', action='store_true')
    subs = p.add_subparsers(dest='mode', required=True)
    subs.add_parser('set').add_argument('target')
    subs.add_parser('card').add_argument('target')
    args = p.parse_args()
    flags = {'future': args.include_future, 'digital': args.include_digital,
             'foreign': args.include_foreign}
    result = (set_query(args.target.lower(), cutoff=args.as_of, **flags)
              if args.mode == 'set' else card_query(args.target, cutoff=args.as_of, **flags))
    if not args.all:
        result['cards'] = result['cards'][:30]
    print(json.dumps({'as_of': args.as_of.isoformat(), 'filter': flags,
                      **result}, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
