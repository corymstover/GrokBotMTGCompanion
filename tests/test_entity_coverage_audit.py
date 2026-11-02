"""All registered world-entity types receive source-graded, explicit gap records."""
import json
import sys
import unittest
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_entity_coverage as E  # noqa: E402


class EntityCoverageCensus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = E.build()

    def test_all_five_registered_entity_categories_reconciled(self):
        data = self.report
        self.assertEqual(data['total_registered'], 839)
        self.assertEqual({k: d['registered'] for k, d in data['registered_by_type'].items()},
                         {'Plane': 33, 'Place': 112, 'Faction': 156, 'Object': 54, 'Character': 484})
        self.assertEqual(len(data['all_registered_entities']), 839)
        self.assertEqual(len({n['id'] for n in data['all_registered_entities']}), 839)
        for kind, stats in data['registered_by_type'].items():
            self.assertEqual(stats['registered'], sum(stats['gap_counts'].values()), kind)
            self.assertEqual(stats['registered'], stats['with_any_direct_claim'] + stats['without_direct_claim'])

    def test_all_registered_entities_have_direct_official_sources(self):
        no_proof = [n for n in self.report['all_registered_entities']
                    if n['gap'] == 'NO_DIRECT_CITED_CLAIM']
        self.assertEqual(self.report['nodes_without_direct_claim'], 0)
        self.assertEqual(no_proof, [])
        self.assertEqual(self.report['nodes_with_only_qualified_direct_claims'], 139)

    def test_four_prior_evidence_gaps_are_resolved_by_specific_official_claims(self):
        by_id = {row['id']: row for row in self.report['all_registered_entities']}
        expected = {
            'place:ardenvale': ('EL012', 'feature/planeswalkers-guide-eldraine-2019-10-31'),
            'artifact:great_henge': ('EL013', 'feature/planeswalkers-guide-eldraine-2019-10-31'),
            'place:riders_lock': ('SE037', 'magic-story/games-2016-04-27'),
            'place:sotheran_supervoid': ('EO031', 'magic-story/the-legends-of-edge-of-eternities'),
        }
        for node_id, (claim_id, source_suffix) in expected.items():
            with self.subTest(node_id=node_id):
                row = by_id[node_id]
                self.assertIn(claim_id, row['direct_claim_ids'])
                self.assertIn('CANON_CONFIRMED', row['direct_grades'])
                self.assertEqual(row['direct_distinct_claim_count'], 1)
                self.assertEqual(row['gap'], 'ONE_DIRECT_CLAIM_ONLY')
                self.assertEqual(len(row['official_source_urls']), 1)
                self.assertTrue(row['official_source_urls'][0].endswith(source_suffix))

    def test_every_direct_claim_citation_is_exact_first_party_and_graded(self):
        for node in self.report['all_registered_entities']:
            if node['direct_distinct_claim_count']:
                self.assertTrue(node['direct_claim_ids'])
                self.assertTrue(node['official_source_urls'])
                self.assertTrue(node['direct_grades'])
            for url in node['official_source_urls']:
                parsed = urlsplit(url)
                self.assertEqual(parsed.scheme, 'https')
                self.assertIn(parsed.hostname, {'magic.wizards.com', 'www.magic.wizards.com'})
            if node['gap'] == 'ONLY_QUALIFIED_DIRECT_CLAIMS':
                self.assertNotIn('CANON_CONFIRMED', node['direct_grades'])

    def test_audit_artifacts_are_deterministic_and_canon_scope_is_limited(self):
        saved = json.loads(E.OUT.read_text(encoding='utf-8'))
        self.assertEqual(saved, self.report)
        self.assertEqual(E.REPORT.read_text(encoding='utf-8'), E.markdown(self.report))
        self.assertIn('Not a census of all MTG canon', self.report['scope'])
        self.assertTrue(any('not a complete biography' in limit for limit in self.report['limits']))

    def test_k102_checked_with_bounded_broader_history_acceptance(self):
        import audit_full_checklist
        rows = audit_full_checklist.items()
        audit = [r for r in rows if r['task'].startswith('Audit major planes, regions')]
        self.assertEqual(len(audit), 1)
        self.assertTrue(audit[0]['checked'])
        # K103 is accepted only under the owner's v3.09 bounded repository
        # finish line.  The cited graph retains explicit UNKNOWN canon gaps.
        self.assertTrue(next(r for r in rows if r['task'].startswith('Connect cross-plane histories'))['checked'])
        # v3.00 certifies seven bounded gates with separately witnessed exact-SHA CI.
        self.assertEqual([r['checked'] for r in rows
                          if r['section'].startswith('Definition of the first major')],
                         [True] * 7)
        # v3.09 accepted K108/K110 as bounded preflight build capabilities;
        # v3.11 separately records Cory's three exact hash-bound pilot approvals.
        self.assertEqual({r['id'] for r in rows if r['section'].startswith('Phase 6') and r['checked']},
                         {f'K{x}' for x in range(106, 116)})


if __name__ == '__main__':
    unittest.main()
