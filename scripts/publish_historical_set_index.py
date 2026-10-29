#!/usr/bin/env python3
"""Validate historical printings and publish deterministic set/card lookup shards.

The 105 committed printing shards are the only input. --write changes only
data/set_atlas/historical_*. This does not authenticate the lost 2026-10-28
original bulk file or modify any protected Grixis records.
"""
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORICAL_DATE = date(2026, 10, 29)


def serialized(obj):
    return (json.dumps(obj, ensure_ascii=False, separators=(',', ':'), sort_keys=True) + '\n').encode('utf-8')


def make_index(root=ROOT, cutoff=HISTORICAL_DATE, expected=(105, 119509, 1062, 107700)):
    manifest = json.loads((root / 'data/printing_lore/manifest.json').read_text(encoding='utf-8'))
    if manifest['total_shards'] != len(manifest['shards']) or len(manifest['shards']) != expected[0]:
        raise ValueError('Historical shard count does not match expectation')
    if manifest['total_printings'] != expected[1]:
        raise ValueError('Historical printing count does not match expectation')
    declared = manifest['sets']
    if len(declared) != expected[2]:
        raise ValueError('Historical set count does not match expectation')
    per_set, per_card = defaultdict(list), defaultdict(list)
    per_set_counts = defaultdict(Counter)
    present_ids = set()
    missing_oracle = 0
    total = 0
    for filename, metadata in sorted(manifest['shards'].items()):
        raw = (root / 'data/printing_lore' / filename).read_bytes()
        if len(raw) != metadata['bytes']:
            raise ValueError(f'{filename}: byte-size mismatch')
        if hashlib.sha256(raw).hexdigest() != metadata['sha256']:
            raise ValueError(f'{filename}: SHA-256 mismatch')
        lines = raw.splitlines()
        if len(lines) != metadata['rows']:
            raise ValueError(f'{filename}: row-count mismatch')
        for line in lines:
            item = json.loads(line)
            pid, code = item.get('id'), item.get('s')
            if not pid or pid in present_ids:
                raise ValueError(f'{filename}: duplicate/missing printing ID {pid}')
            if code not in declared or filename not in declared[code]['files']:
                raise ValueError(f'{filename}: invalid set linkage {code}')
            if not isinstance(item.get('n'), str) or not item['n'] or not item.get('c'):
                raise ValueError(f'{filename}: incomplete printing {pid}')
            try:
                released = date.fromisoformat(item['r'])
            except (TypeError, ValueError, KeyError) as exc:
                raise ValueError(f'{filename}: invalid date for {pid}') from exc
            present_ids.add(pid)
            total += 1
            oid = item.get('o')
            if not oid:
                missing_oracle += 1
            record = [pid, oid, item['n'], item['c'], item['r'],
                      item.get('l'), int(bool(item.get('p')))]
            per_set[code].append(record)
            if oid:
                per_card[oid].append([code, *record])
            counts = per_set_counts[code]
            counts['all'] += 1
            if item.get('l') == 'en' and item.get('p'):
                counts['english_paper'] += 1
                if released <= cutoff:
                    counts['released_english_paper'] += 1
            if released > cutoff:
                counts['future_dated'] += 1
    if total != manifest['total_printings'] or len(present_ids) != total:
        raise ValueError('Historical printing-ID total mismatch')
    if set(per_set) != set(declared):
        raise ValueError('Shard/manifest set-code mismatch')
    for code, details in declared.items():
        counts = per_set_counts[code]
        if counts['all'] != details['printings'] or counts['english_paper'] != details['english_paper']:
            raise ValueError(f'{code}: per-set count mismatch')
    if sum(c['english_paper'] for c in per_set_counts.values()) != expected[3]:
        raise ValueError('English paper total mismatch')
    payloads = {}
    for n in '0123456789abcdef':
        sets = {code: sorted(records, key=lambda x: (x[4], x[3], x[0]))
                for code, records in per_set.items()
                if hashlib.sha256(code.encode()).hexdigest()[0] == n}
        cards = {oid: sorted(records, key=lambda x: (x[5], x[0], x[4], x[1]))
                 for oid, records in per_card.items() if oid[0].lower() == n}
        payloads[f'historical_sets_{n}.json'] = serialized(sets)
        payloads[f'historical_cards_{n}.json'] = serialized(cards)
    report = {
        'schema': 1,
        'archive': '2026-10-28 committed historical printing shards',
        'cutoff': cutoff.isoformat(),
        'source_bulk_sha256_recorded_not_independently_rechecked': manifest['source_sha256'],
        'count_policy': 'One row per Scryfall printing ID; paper, language and future status remain separate',
        'shards_verified': len(manifest['shards']),
        'set_codes': len(declared),
        'printing_ids': total,
        'oracle_id_missing_printings': missing_oracle,
        'stable_oracle_ids_indexed': len(per_card),
        'english_paper': expected[3],
        'released_english_paper': sum(c['released_english_paper'] for c in per_set_counts.values()),
        'future_dated_all_printings': sum(c['future_dated'] for c in per_set_counts.values()),
        'per_set': {code: dict(sorted(per_set_counts[code].items())) for code in sorted(declared)},
        'generated_file_sha256': {name: hashlib.sha256(data).hexdigest() for name, data in sorted(payloads.items())}
    }
    payloads['historical_shard_audit_2026-10-29.json'] = serialized(report)
    return payloads, report


def run(root=ROOT, write=False):
    payloads, report = make_index(root)
    folder = root / 'data/set_atlas'
    if write:
        folder.mkdir(parents=True, exist_ok=True)
    for name, content in sorted(payloads.items()):
        dest = folder / name
        if write:
            dest.write_bytes(content)
        elif not dest.exists() or dest.read_bytes() != content:
            raise ValueError(f'{name}: missing or differs from reproducible index')
    print(json.dumps({k: v for k, v in report.items()
                      if k not in ('per_set', 'generated_file_sha256')}, sort_keys=True))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write', action='store_true', help='write only set atlas files')
    args = p.parse_args()
    run(write=args.write)


if __name__ == '__main__':
    main()
