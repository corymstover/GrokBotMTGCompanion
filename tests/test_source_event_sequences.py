import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import source_event_sequences as S
import query_lore_chronology as Q


class SourceEventSequencesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current=json.loads(S.OUT.read_text(encoding='utf-8'))
        cls.old=json.loads(Q.DATA.read_text(encoding='utf-8'))

    def test_exact_rebuild_and_sha(self):
        self.assertEqual(self.current,S.build())
        d=dict(self.current)
        sig=d.pop('content_sha256')
        self.assertEqual(sig,S.digest(d))
        self.assertEqual(self.current['counts']['strands'],3)
        self.assertEqual(self.current['counts']['events'],24)

    def test_source_proofs_have_original_claim_ids_and_digest(self):
        for node in self.current['nodes']:
            self.assertTrue(node['id'].startswith(node['strand']+':'))
        for e in self.current['edges']:
            self.assertTrue(e['source_url'].startswith('https://magic.wizards.com/'))
            self.assertEqual(e['quote_sha256'],hashlib.sha256(S.canon(e['quote']).encode()).hexdigest())
            self.assertNotIn('ar_year',e)

    def test_historical_kamigawa_order_is_qualified(self):
        r=S.proof(self.current,'K:konda_imprisons','K:realm_barrier_breaks')
        self.assertEqual(r['result'],'BEFORE')
        self.assertEqual(len(r['proof']),3)
        self.assertIn('QUALIFIED',r['confidence'])
        self.assertEqual(S.proof(self.current,'K:imperials_founded','K:realm_barrier_breaks')['result'],'UNKNOWN')

    def test_valley_legend_is_not_canonically_certified(self):
        r=S.proof(self.current,'V:holly_pact','V:war_of_cinders')
        self.assertEqual(r['result'],'BEFORE')
        self.assertEqual(r['confidence'],'QUALIFIED_LEGENDARY_SEQUENCE')
        self.assertEqual(S.proof(self.current,'V:lily_saves_valley','V:sealed_great_magic')['result'],'BEFORE')
        self.assertEqual(S.proof(self.current,'V:holly_pact','V:sealed_great_magic')['result'],'UNKNOWN')
        self.assertTrue(all(n['certainty']=='NARRATED_TRADITION_ONLY'
                            for n in self.current['nodes'] if n['strand']=='V'))

    def test_wildsear_during_war_not_after_war_ended(self):
        r=S.proof(self.current,'V:war_of_cinders','V:wildsear_appears')
        self.assertEqual(r['result'],'DURING_OR_AFTER_START')
        self.assertNotIn('V:wildsear_appears',self.current['precedes']['V:war_of_cinders'])

    def test_duskmourn_chain_and_unknown_cross_plane(self):
        self.assertEqual(S.proof(self.current,'D:marina_lures','D:ascension')['result'],'BEFORE')
        self.assertEqual(S.proof(self.current,'V:holly_pact','D:ascension')['result'],'UNKNOWN')
        self.assertEqual(Q.compare_across_datasets(self.old,self.current,'A:elder_dragon_war','D:ascension')['result'],'UNKNOWN')

    def test_existing_legacy_chronology_is_not_replaced(self):
        self.assertEqual(self.old['counts']['event_nodes'],56)
        self.assertEqual(self.old['counts']['stated_edges'],63)
        self.assertEqual(Q.check(self.old)['result'],'PASS')
        self.assertEqual(Q.compare_across_datasets(self.old,self.current,'A:elder_dragon_war','A:primeval_rule')['result'],'BEFORE')

    def test_human_readable_partial_label_lookup(self):
        r=Q.compare_across_datasets(self.old,self.current,'Konda imprisons a part','breaks the barrier')
        self.assertEqual(r['result'],'BEFORE')
        with self.assertRaises(ValueError):
            Q.compare_across_datasets(self.old,self.current,'Valgavoth','K:kami_war')


if __name__=='__main__':
    unittest.main()
