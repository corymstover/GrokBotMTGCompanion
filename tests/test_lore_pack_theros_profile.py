import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_lore_pack_theros_profile as T  # noqa: E402


class TherosProfilePackTests(unittest.TestCase):
    def test_pack_is_source_graded_not_approved(self):
        self.assertEqual(T.audit()['claims'], 10)
        self.assertFalse(T.audit()['owner_approval'])

    def test_city_list_is_qualified_not_exhaustive(self):
        data = json.loads(T.PACK.read_text(encoding='utf-8'))
        self.assertEqual(data['claims'][1]['object'].split(';'), ['meletis', 'akros', 'setessa'])
        self.assertIn('does not assert they exhaust', data['claims'][1]['limitation'])
        self.assertFalse(T.audit()['inferred_chronological_order'])

    def test_verbatim_guard_rejects_wrong_page(self):
        data = json.loads(T.PACK.read_text(encoding='utf-8'))
        fake = '<html><body>' + ' '.join(c['source_excerpt'] for c in data['claims']) + '</body></html>'
        self.assertEqual(T.audit(fake)['status'], 'PASS')
        with self.assertRaisesRegex(ValueError, 'THP001'):
            T.audit('<html><body>Unrelated page</body></html>')


if __name__ == '__main__':
    unittest.main()
