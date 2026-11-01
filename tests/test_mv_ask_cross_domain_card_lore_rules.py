"""Joined card, source-graded lore and dated Commander rules must fail closed."""
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask as A  # noqa: E402

CR_URL = 'https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt'


class CardLoreCommanderEvidence(unittest.TestCase):
    def test_ugin_card_legality_is_not_eligible_commander(self):
        q = A.ask('What are the lore and Commander eligibility of Ugin, the Spirit Dragon?')
        self.assertEqual(q['route'], 'ask->card_lore_commander_evidence')
        self.assertEqual(q['confidence'], 'QUALIFIED')
        self.assertEqual(q['result']['card']['name'], 'Ugin, the Spirit Dragon')
        self.assertEqual(q['result']['card']['commander_legality'], 'legal')
        self.assertFalse(q['result']['commander_eligibility']['allowed'])
        self.assertEqual(q['result']['named_lore_subjects'][0]['name'], 'Ugin')
        self.assertGreater(q['result']['named_lore_subjects'][0]['direct_claim_count'], 8)
        self.assertEqual(len(q['result']['named_lore_subjects'][0]['sampled_claims']), 8)
        self.assertIn('LORE_CLAIMS_TRUNCATED_TO_EIGHT_PER_SUBJECT', q['flags'])
        self.assertIn('GRAPH_NAME_BRIDGE_NOT_DEPICTION_PROOF', q['flags'])
        self.assertIn('DATED_SCRYFALL_LEGALITY_NOT_LIVE', q['flags'])
        self.assertIn(CR_URL, q['sources'])

    def test_dual_face_front_name_resolves_by_exact_oracle_id(self):
        q = A.ask('Show card, lore, and Commander rules for Nicol Bolas, the Ravager')
        self.assertTrue(q['result']['card']['name'].startswith('Nicol Bolas, the Ravager //'))
        self.assertTrue(q['result']['commander_eligibility']['allowed'])
        subjects = q['result']['named_lore_subjects']
        self.assertEqual([s['id'] for s in subjects], ['character:nicol_bolas'])
        self.assertEqual(subjects[0]['bridge'], 'GRAPH_NAMES_ENTITY_NAVIGATION_ONLY')
        self.assertIn('CANON_DISPUTED', subjects[0]['direct_claim_grades'])
        self.assertIn('CANON_DISPUTED_PRESENT', q['flags'])
        self.assertEqual(q['confidence'], 'QUALIFIED')

    def test_unlinked_art_caption_does_not_infer_character_or_scene(self):
        q = A.ask('Tell me the lore and Commander eligibility of Blackblade Reforged')
        self.assertEqual(q['result']['named_lore_subjects'], [])
        self.assertIn('NO_CITED_NAMED_ENTITY_BRIDGE', q['flags'])
        self.assertFalse(q['result']['commander_eligibility']['allowed'])
        self.assertIn('not proof of which scene', q['result']['limitation'])

    def test_unknown_card_returns_no_made_up_rules_or_lore(self):
        q = A.ask('What are the lore and Commander eligibility of Zorblax the Unreal?')
        self.assertEqual(q['confidence'], 'NOT_FOUND')
        self.assertEqual(q['flags'], ['NO_SUCH_CARD_IN_INDEX'])
        self.assertEqual(q['sources'], [])
        self.assertIsNone(q['result']['card'])

    def test_ambiguous_duplicate_oracle_graph_anchor_fails_closed(self):
        mg = A.graph()
        clone = copy.copy(mg)
        clone.nodes = dict(mg.nodes)
        base = next(n for n in mg.nodes.values()
                    if n.get('type') == 'Card' and n.get('name') == 'Ugin, the Spirit Dragon')
        clone.nodes['card:synthetic_duplicate_ugin'] = dict(base, id='card:synthetic_duplicate_ugin')
        with patch.object(A, 'graph', return_value=clone):
            q = A.ask('What are the lore and Commander eligibility of Ugin, the Spirit Dragon?')
        self.assertEqual(q['result']['named_lore_subjects'], [])
        self.assertIn('AMBIGUOUS_GRAPH_CARD_ORACLE_ID', q['flags'])
        self.assertIn('NO_UNIQUE_GRAPH_CARD_ANCHOR', q['flags'])
        self.assertEqual(q['confidence'], 'QUALIFIED')

    def test_sample_sources_are_all_in_the_outer_citation_list(self):
        q = A.ask('What are the lore and Commander eligibility of Ugin, the Spirit Dragon?')
        self.assertEqual(q['evidence_as_of']['comprehensive_rules'], '2026-09-25')
        self.assertEqual(q['evidence_as_of']['scryfall_commander_legality'], '2026-10-15')
        for person in q['result']['named_lore_subjects']:
            for claim in person['sampled_claims']:
                self.assertTrue(claim['sources'])
                self.assertTrue(set(claim['sources']).issubset(q['sources']))
        self.assertFalse(any(s.startswith('http://') for s in q['sources']))


if __name__ == '__main__':
    unittest.main()
