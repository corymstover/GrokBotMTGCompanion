"""Bounded feature sign-off cannot be used to bypass source or owner gates."""
import copy
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_foundation_capabilities as A  # noqa: E402


class CapabilityAuditTests(unittest.TestCase):
    def test_reproduces_committed_scope_without_release_acceptance(self):
        current = json.loads(A.OUT.read_text(encoding='utf-8'))
        self.assertEqual(current, A.build())
        self.assertEqual(A.REPORT.read_text(encoding='utf-8'), A.markdown(current))
        self.assertEqual(len(current['capabilities']), 5)
        self.assertTrue(all(x['supported'] for x in current['capabilities'].values()))
        self.assertFalse(current['owner_accepted'])
        self.assertFalse(current['release_certified'])
        self.assertTrue(current['phase6_deckbuilding_deferred'])
        self.assertIn('NOT_RELEASE_CERTIFIED', current['status'])

    def test_unreviewed_source_page_reopens_scope(self):
        original = A.load

        def changed(path):
            data = original(path)
            if 'story_coverage_inventory' in path:
                data = copy.deepcopy(data)
                data['totals']['reviewed_no_claim_pages'] -= 1
            return data

        with patch.object(A, 'load', side_effect=changed):
            with self.assertRaisesRegex(ValueError, 'unreviewed declared pages'):
                A.build()

    def test_missing_hard_negative_or_ambiguity_is_not_scoped_complete(self):
        original = A.load

        def changed(path):
            data = original(path)
            if 'foundation_acceptance_packet' in path:
                data = copy.deepcopy(data)
                data['representative_questions'] = [
                    q for q in data['representative_questions'] if q['id'] != 'graph_nav_unknown']
            return data

        with patch.object(A, 'load', side_effect=changed):
            with self.assertRaisesRegex(ValueError, 'required source/negative'):
                A.build()

    def test_fabricated_release_acceptance_fails_scope_audit(self):
        original = A.load

        def changed(path):
            data = original(path)
            if 'foundation_acceptance_packet' in path:
                data = copy.deepcopy(data)
                data['release_certified'] = True
            return data

        with patch.object(A, 'load', side_effect=changed):
            with self.assertRaisesRegex(ValueError, 'release approval was falsely implied'):
                A.build()

    def test_nonstrict_graph_path_cannot_be_reported_as_historical_proof(self):
        original = A.load

        def changed(path):
            data = original(path)
            if 'foundation_acceptance_packet' in path:
                data = copy.deepcopy(data)
                data['cross_plane_graph_navigation'][0]['evidence_type'] = 'PROVEN_CHRONOLOGY'
            return data

        with patch.object(A, 'load', side_effect=changed):
            with self.assertRaisesRegex(ValueError, 'overstates historical proof'):
                A.build()


if __name__ == '__main__':
    unittest.main()
