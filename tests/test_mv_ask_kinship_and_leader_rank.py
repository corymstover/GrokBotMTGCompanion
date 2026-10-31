"""Phase 7: relational evidence cannot establish gender or in-universe seniority by itself.

These previously returned misleading VERIFIED answers: Tamiyo was identified as
Nashi's father, and the latest cited Izzet leader was offered as the first.
The tests protect direct source-backed relations while keeping uncertain claims
visible as context, not as answers to narrower questions.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import mv_ask as A  # noqa: E402


def rows(env):
    return [r for group in env.get('result', {}).get('relations_by_status', {}).values() for r in group]


class KinshipSafety(unittest.TestCase):
    def test_mother_is_not_reported_as_father(self):
        wrong_role = A.ask("Who is Nashi's father?")
        self.assertEqual(wrong_role['confidence'], 'NOT_FOUND')
        self.assertIn('NO_ROLE_SPECIFIC_PARENT_EVIDENCE', wrong_role['flags'])
        self.assertEqual(rows(wrong_role), [])
        context = wrong_role['result']['known_parental_relations_not_answer']
        self.assertTrue(any(x['name'] == 'Tamiyo' and x['relation'] == 'inverse_of:mother_of'
                            for x in context))
        mother = A.ask("Who is Nashi's mother?")
        self.assertEqual(mother['confidence'], 'VERIFIED')
        self.assertTrue(any(x['name'] == 'Tamiyo' for x in rows(mother)))

    def test_untyped_parent_is_not_reported_as_mother_or_father(self):
        for question, parent_name in [
            ("Who is Killian Lu's mother?", 'Embrose Lu'),
            ("Who is Killian's father?", 'Embrose Lu'),
            ("Who is Khrad's mother?", 'King Khal'),
            ("Who is Khrad's father?", 'King Khal'),
        ]:
            with self.subTest(question=question):
                env = A.ask(question)
                self.assertEqual(env['confidence'], 'NOT_FOUND')
                self.assertEqual(rows(env), [])
                self.assertTrue(any(x['name'] == parent_name and x['relation'] == 'inverse_of:parent_of'
                                    for x in env['result']['known_parental_relations_not_answer']))
                self.assertTrue(all(u.startswith('https://magic.wizards.com/') for u in env['sources']))

    def test_generic_parent_route_preserves_mother_and_parent_claims(self):
        for question, expected in [
            ("Who are Nashi's parents?", ('Tamiyo', 'inverse_of:mother_of')),
            ("Who are Killian Lu's parents?", ('Embrose Lu', 'inverse_of:parent_of')),
            ("Who are Chandra's parents?", ('Pia Nalaar', 'inverse_of:parent_of')),
        ]:
            env = A.ask(question)
            self.assertEqual(env['confidence'], 'QUALIFIED')
            self.assertIn('PARENT_ROSTER_NOT_EXHAUSTIVELY_VERIFIED', env['flags'])
            self.assertTrue(any((r['name'], r['relation']) == expected for r in rows(env)))

    def test_unknown_person_remains_unknown(self):
        env = A.ask("Who is Zorblax the Unreal's mother?")
        self.assertEqual(env['confidence'], 'NOT_FOUND')
        self.assertEqual(env['result']['known_parental_relations_not_answer'], [])

    def test_explicit_father_wording_on_generic_edge_is_still_answerable(self):
        env = A.ask("Who is Kellan's father?")
        self.assertEqual(env['confidence'], 'VERIFIED')
        self.assertIn('PARENT_ROLE_EXPLICIT_IN_CITED_CLAIM', env['flags'])
        self.assertEqual([(r['name'], r['claim']) for r in rows(env)], [('Oko', 'WE009')])


class LeaderRankSafety(unittest.TestCase):
    def test_first_original_and_new_not_inferred_from_publication_dates(self):
        for question, rank in [
            ("Who was the first leader of the Izzet?", 'first'),
            ("Who is the original guildmaster of the Izzet?", 'original'),
            ("Who is the new leader of the Izzet?", 'new'),
        ]:
            with self.subTest(question=question):
                env = A.ask(question)
                self.assertEqual(env['confidence'], 'QUALIFIED')
                self.assertIn('REQUESTED_LEADER_CHRONOLOGY_NOT_ESTABLISHED', env['flags'])
                lead = env['result']['leadership']
                self.assertEqual(lead['requested_rank'], rank)
                self.assertIsNone(lead['verified_requested_leader'])
                self.assertEqual(lead['most_recent_cited']['node'], 'character:ral_zarek')

    def test_nonranked_leader_query_preserves_claims_but_not_current_office(self):
        env = A.ask('Who leads the Izzet?')
        self.assertEqual(env['confidence'], 'QUALIFIED')
        self.assertIn('CURRENT_LEADER_NOT_ESTABLISHED', env['flags'])
        self.assertIsNone(env['result']['leadership']['verified_current_leader'])
        self.assertNotIn('REQUESTED_LEADER_CHRONOLOGY_NOT_ESTABLISHED', env['flags'])


if __name__ == '__main__':
    unittest.main()
