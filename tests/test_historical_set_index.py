"""Portable Phase 1B historical shard integrity and query regressions."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from publish_historical_set_index import make_index
from historical_set_lookup import set_query, card_query


def card(pid, oid, code, when='2020-01-01'):
    return {'id': pid, 'o': oid, 'n': 'Test Spell' if oid else 'Unknown',
            's': code, 'c': pid, 'l': 'en', 'p': 1, 'r': when}


def fixture(root):
    d = root / 'data/printing_lore'
    d.mkdir(parents=True)
    oid = 'a0000000-0000-0000-0000-000000000000'
    examples = {
        'a-000.jsonl': [card('p1', oid, 'aaa'), card('p2', oid, 'aaa', '2021-01-01')],
        'b-000.jsonl': [card('p3', oid, 'bbb'), card('p4', None, 'bbb', '2026-11-13')]
    }
    shards = {}
    for name, rows in examples.items():
        content = b''.join((json.dumps(p) + '\n').encode('utf-8') for p in rows)
        (d / name).write_bytes(content)
        shards[name] = {'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest(),
                        'rows': len(rows)}
    manifest = {
        'total_shards': 2, 'total_printings': 4, 'source_sha256': 'recorded-not-rechecked',
        'shards': shards,
        'sets': {
            'aaa': {'files': ['a-000.jsonl'], 'printings': 2, 'english_paper': 2},
            'bbb': {'files': ['b-000.jsonl'], 'printings': 2, 'english_paper': 2}
        }
    }
    (d / 'manifest.json').write_text(json.dumps(manifest))
    return oid


class HistoricalSetTests(unittest.TestCase):
    def test_deterministic_index_and_lookups(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            oid = fixture(root)
            outputs, report = make_index(root, expected=(2, 4, 2, 4))
            self.assertEqual(report['shards_verified'], 2)
            self.assertEqual(report['oracle_id_missing_printings'], 1)
            self.assertEqual(report['released_english_paper'], 3)
            folder = root / 'data/set_atlas'
            folder.mkdir()
            for filename, blob in outputs.items():
                (folder / filename).write_bytes(blob)
            a = set_query('aaa', folder)
            self.assertEqual(a['printing_records'], 2)
            self.assertEqual(a['cards'][0]['classification'], 'tied debut')
            b = set_query('bbb', folder)
            self.assertEqual(b['printing_records'], 1)
            self.assertEqual(b['cards'][0]['classification'], 'tied debut')
            self.assertEqual(len(card_query(oid, folder)['cards'][0]['printings']), 3)
            self.assertEqual(set_query('bbb', folder, future=True)['printing_records'], 2)
            self.assertEqual(outputs, make_index(root, expected=(2, 4, 2, 4))[0])

    def test_modified_file_fails_hash_or_size(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            path = root / 'data/printing_lore/a-000.jsonl'
            path.write_bytes(path.read_bytes() + b'!')
            with self.assertRaisesRegex(ValueError, 'byte-size mismatch'):
                make_index(root, expected=(2, 4, 2, 4))


if __name__ == '__main__':
    unittest.main()
