import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_lore_pack_alara as A  # noqa: E402


class AlaraPlanePackTests(unittest.TestCase):
    def test_offline_primary_source_and_distinct_claims(self):
        self.assertEqual(A.audit()['claims'], 10)
        self.assertFalse(A.audit()['owner_approval'])

    def test_no_new_temporal_order(self):
        d = json.loads(A.PACK.read_text(encoding='utf-8'))
        self.assertTrue(all('before' not in c['predicate'] and 'after' not in c['predicate'] for c in d['claims']))
        self.assertEqual(d['claims'][0]['object'].split(';'),
                         ['bant', 'esper', 'grixis_shard', 'jund', 'naya'])
        self.assertIn('not exhaustive', ' '.join(d['remaining']))

    def test_live_excerpt_mutation_is_rejected(self):
        d = json.loads(A.PACK.read_text(encoding='utf-8'))
        fake = '<html><body>' + ' '.join(c['source_excerpt'] for c in d['claims']) + '</body></html>'
        self.assertEqual(A.audit(fake)['claims'], 10)
        with self.assertRaisesRegex(ValueError, 'ALA001'):
            A.audit('<html><body>Unrelated text</body></html>')


if __name__ == '__main__':
    unittest.main()
