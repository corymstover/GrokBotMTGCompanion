"""Plain present-tense leader questions are not proved by publication order."""
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import mv_ask as A  # noqa: E402


class PresentLeaderSafetyTests(unittest.TestCase):
    def test_present_tense_variants_qualify_latest_citation(self):
        for question in [
            'Who leads the Izzet?', 'Who is the guildmaster of the Izzet?',
            "Who's in charge of the Izzet?", 'Who commands the Izzet?',
            'Who runs the Izzet?', 'Who is the leader of the Izzet?',
            'Who rules the Azorius?',
        ]:
            with self.subTest(question=question):
                env = A.ask(question)
                self.assertEqual(env['confidence'], 'QUALIFIED')
                self.assertIn('CURRENT_LEADER_NOT_ESTABLISHED', env['flags'])
                self.assertIsNone(env['result']['leadership']['verified_current_leader'])
                self.assertTrue(env['sources'])  # real historical claims remain visible

    def test_older_officeholders_are_historical_not_verified_current(self):
        for question in [
            'Who led the Izzet?', 'Who was the guildmaster of the Izzet?',
            'Who commanded the Izzet?',
        ]:
            with self.subTest(question=question):
                env = A.ask(question)
                self.assertEqual(env['confidence'], 'VERIFIED')
                self.assertNotIn('CURRENT_LEADER_NOT_ESTABLISHED', env['flags'])
                self.assertIn('leadership', env['result'])

    def test_every_registered_faction_with_incoming_leader_claim_has_bounded_present_answer(self):
        mg = A.graph()
        led = sorted({e['to'] for e in mg.g['edges'] if e.get('claim') and
                      e['relation'] in A.LEADER_RELATIONS and
                      mg.nodes.get(e['to'], {}).get('type') == 'Faction'})
        self.assertGreaterEqual(len(led), 30)
        for nid in led:
            name = re.sub(r'\s*\(.*?\)', '', mg.nodes[nid]['name']).strip()
            name = re.sub(r'^the ', '', name, flags=re.I)
            with self.subTest(faction=nid):
                env = A.ask('Who leads the ' + name + '?')
                self.assertEqual(env['result'].get('entity'), nid)
                self.assertEqual(env['confidence'], 'QUALIFIED')
                self.assertIn('CURRENT_LEADER_NOT_ESTABLISHED', env['flags'])

    def test_unknown_leader_not_invented(self):
        env = A.ask('Who leads the Elves of Eldraine?')
        self.assertEqual(env['confidence'], 'NOT_FOUND')
        self.assertNotIn('CURRENT_LEADER_NOT_ESTABLISHED', env['flags'])


if __name__ == '__main__':
    unittest.main()
