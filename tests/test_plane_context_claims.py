"""Curated same-plane story claims remain separate from direct plane evidence."""
import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_plane_history_dossiers as H
import mv_ask


class PlaneContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads(H.OUT.read_text(encoding='utf-8'))
        cls.graph = json.loads(H.GRAPH.read_text(encoding='utf-8'))
        cls.nodes = {n['id']:n for n in cls.graph['nodes']}
        cls.planes = {p['id']:p for p in cls.saved['planes']}

    def test_exact_determinism_and_separate_counts(self):
        self.assertEqual(self.saved, H.build())
        self.assertEqual(self.saved['schema'], 'plane-history-dossiers/v2')
        self.assertEqual(self.saved['counts']['registered_planes'], 33)
        self.assertEqual(self.saved['counts']['direct_claim_edges'], 207)
        self.assertEqual(self.saved['counts']['thin_planes_fewer_than_five_claims'], 8)
        self.assertEqual(self.saved['counts']['planes_with_curated_context'], 4)
        self.assertEqual(self.saved['counts']['distinct_contextual_claims'], 53)

    def test_four_curated_planes_have_exact_bounded_claim_counts(self):
        expected = {'plane:eldraine':10,'plane:arcavios':16,
                    'plane:new_capenna':15,'plane:lorwyn_shadowmoor':12}
        actual = {pid:len(p['contextual_claims']) for pid,p in self.planes.items()
                  if p['contextual_claims']}
        self.assertEqual(actual, expected)
        for plane in self.planes.values():
            direct={c['claim_id'] for c in plane['facts']}
            contextual={c['claim_id'] for c in plane['contextual_claims']}
            self.assertFalse(direct & contextual)

    def test_each_claim_retains_original_grade_and_official_quote(self):
        for plane in self.planes.values():
            for c in plane['contextual_claims']:
                original=self.nodes['claim:'+c['claim_id']]
                self.assertEqual(original['name'],c['statement'])
                self.assertEqual(original['grade'],c['grade'])
                self.assertEqual(c['basis'],'CURATED_ON_PLANE_STORY_CONTEXT_NOT_DIRECT_GRAPH_EDGE')
                self.assertTrue(c['scope_note'])
                self.assertTrue(c['source_evidence'])
                for e in c['source_evidence']:
                    self.assertEqual(e['url'],self.nodes['source:'+e['source_id']]['url'])
                    self.assertTrue(e['url'].startswith('https://magic.wizards.com/'))
                    self.assertEqual(e['quote_sha256'],hashlib.sha256(H.normalize(e['quote']).encode()).hexdigest())

    def test_explicit_off_plane_and_duplicated_claims_are_excluded(self):
        for plane_id, ids in {
            'plane:eldraine':{'EL011'},
            'plane:arcavios':{'SX006','SX009','SX012'},
            'plane:new_capenna':{'SN015'},
            'plane:lorwyn_shadowmoor':{'EC005','EC006','EC008','EC013','EC014','EC016'}
        }.items():
            present={c['claim_id'] for c in self.planes[plane_id]['contextual_claims']}
            self.assertFalse(present & ids)

    def test_location_bridge_is_official_and_hash_locked(self):
        bridges=self.saved['official_geographic_bridges']
        self.assertEqual(len(bridges),1)
        b=bridges[0]
        self.assertEqual(b['plane_id'],'plane:arcavios')
        self.assertEqual(b['quote'],'Arcavios is the plane where Strixhaven University is located.')
        self.assertTrue(b['source_url'].startswith('https://magic.wizards.com/'))
        self.assertEqual(b['quote_sha256'],hashlib.sha256(H.normalize(b['quote']).encode()).hexdigest())

    def test_new_capenna_answer_shows_old_and_new_provenance_separately(self):
        a=mv_ask.ask('What is the history of New Capenna?')
        self.assertEqual(a['confidence'],'QUALIFIED')
        self.assertEqual(a['result']['direct_claims'],5)
        self.assertEqual(len(a['result']['claims']),5)
        self.assertEqual(a['result']['contextual_claim_count'],15)
        self.assertIn('CURATED_ON_PLANE_CONTEXT_NOT_DIRECT_GRAPH_CLAIMS',a['flags'])
        self.assertTrue(any(c['claim_id']=='SN003' for c in a['result']['contextual_claims']))
        self.assertFalse(any(c['claim_id']=='SN015' for c in a['result']['contextual_claims']))
        self.assertIn('https://magic.wizards.com/en/news/magic-story/episode-5-hymn-angels-2022-04-05',a['sources'])

    def test_eldraine_context_and_direct_are_not_conflated(self):
        a=mv_ask.ask('What is the history of Eldraine?')
        self.assertEqual(a['result']['direct_claims'],5)
        self.assertEqual(a['result']['contextual_claim_count'],10)
        self.assertFalse(a['result']['complete_history'])
        self.assertFalse(a['result']['verified_total_chronology'])
        self.assertIn('EL001',{c['claim_id'] for c in a['result']['contextual_claims']})

    def test_unrelated_planes_have_no_artificial_context(self):
        a=mv_ask.ask('What is the history of Theros?')
        self.assertEqual(a['result']['direct_claims'],6)
        self.assertEqual(a['result']['contextual_claim_count'],0)
        self.assertNotIn('CURATED_ON_PLANE_CONTEXT_NOT_DIRECT_GRAPH_CLAIMS',a['flags'])


if __name__=='__main__':
    unittest.main()
