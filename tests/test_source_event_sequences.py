import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import source_event_sequences as S
import query_lore_chronology as Q
import mv_ask as A


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
        self.assertEqual(self.current['counts'],{
            'strands':6,'events':51,'strict_edges':37,'non_ordering_relations':2,
            'ordered_pairs':101,'total_pairs':1275,
        })

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

    def test_mirrodin_oil_to_conquest_is_source_local_not_a_total_war_order(self):
        chain=S.proof(self.current,'P:karn_brings_oil','P:mirrans_overwhelmed')
        self.assertEqual(chain['result'],'BEFORE')
        self.assertEqual(len(chain['proof']),4)
        self.assertEqual(chain['confidence'],'QUALIFIED_OFFICIAL_SOURCE_SEQUENCE')
        self.assertTrue(all(e['source_id']=='up_nph' for e in chain['proof']))
        self.assertEqual(S.proof(self.current,'P:karn_father_machines','P:venser_restores_karn')['result'],'BEFORE')
        self.assertEqual(S.proof(self.current,'P:mirrans_overwhelmed','P:venser_restores_karn')['result'],'UNKNOWN')
        self.assertEqual(S.proof(self.current,'P:karn_father_machines','P:phyrexian_campaign')['result'],'UNKNOWN')
        self.assertEqual(S.proof(self.current,'P:karn_brings_oil','K:kami_war')['result'],'UNKNOWN')
        self.assertIn('not a statement about present-day New Phyrexia',
                      next(s for s in self.current['strands'] if s['id']=='P')['limitation'])

    def test_muraganda_source_local_account_does_not_invent_moonfall_order(self):
        claim=S.proof(self.current,'M:ancient_magic_discovered','M:ancient_collapse')
        self.assertEqual(claim['result'],'BEFORE')
        self.assertEqual(claim['proof'][0]['source_id'],'lf_muraganda_guide')
        self.assertEqual(S.proof(self.current,'M:ancient_collapse','M:moons_shatter')['result'],'UNKNOWN')
        overlap=S.proof(self.current,'M:moon_strikes_abate','M:survivor_cultures')
        self.assertEqual(overlap['result'],'DURING_OR_AFTER_START')
        self.assertNotIn('M:survivor_cultures',self.current['precedes']['M:moon_strikes_abate'])
        self.assertEqual(S.proof(self.current,'M:autocracy_treaties','M:teams_discover_limits')['result'],'BEFORE')
        self.assertEqual(S.proof(self.current,'M:teams_discover_limits','M:autocracy_expands')['result'],'UNKNOWN')
        self.assertEqual(S.proof(self.current,'M:avishkar_advance_teams','M:grand_prix_begins')['result'],'BEFORE')

    def test_ugin_bolas_memory_is_ordered_but_not_a_current_realm_status(self):
        account=S.proof(self.current,'B:ugin_meditates','B:ugin_reforms')
        self.assertEqual(account['result'],'BEFORE')
        self.assertEqual(len(account['proof']),8)
        self.assertEqual({p['source_id'] for p in account['proof']},{'lf_meditation_chronicle'})
        self.assertIn('or a statement that the Realm remains intact',account['limitation'])
        self.assertEqual(S.proof(self.current,'B:bolas_displaced','B:ugin_reforms')['result'],'UNKNOWN')
        self.assertEqual(S.proof(self.current,'B:ugin_returns','P:venser_restores_karn')['result'],'UNKNOWN')

    def test_new_source_local_questions_use_proof_and_unknown_in_normal_qa(self):
        r=A.ask('Did M:ancient_magic_discovered happen before M:ancient_collapse?')
        self.assertEqual(r['route'],'ask->chronology')
        self.assertEqual(r['result']['relation'],'BEFORE')
        self.assertEqual(r['sources'],['https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-aetherdrift-part-2'])
        b=A.ask('Did B:bolas_attacks happen before B:realm_cataclysm?')
        self.assertEqual(b['result']['relation'],'BEFORE')
        self.assertEqual(b['result']['proof'][-1]['later'],'B:realm_cataclysm')
        gap=A.ask('Did M:ancient_collapse happen before M:moons_shatter?')
        self.assertEqual(gap['result']['relation'],'UNKNOWN')
        self.assertEqual(gap['sources'],[])

    def test_normal_companion_routes_new_phyrexia_order_and_still_says_unknown(self):
        quoted='Did Karn introduces Phyrexian oil to Mirrodin happen before Mirran forces are overwhelmed in the early conquest?'
        answer=A.ask(quoted)
        self.assertEqual(answer['route'],'ask->chronology')
        self.assertEqual(answer['result']['relation'],'BEFORE')
        self.assertEqual(answer['result']['answer'],True)
        self.assertEqual(len(answer['result']['proof']),4)
        self.assertEqual(answer['sources'],['https://magic.wizards.com/en/story/new-phyrexia-plane'])
        undecided=A.ask('Did P:mirrans_overwhelmed happen before P:venser_restores_karn?')
        self.assertEqual(undecided['result']['relation'],'UNKNOWN')
        self.assertIsNone(undecided['result']['answer'])
        self.assertIn('NO_CITED_CHRONOLOGY_PATH',undecided['flags'])

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
