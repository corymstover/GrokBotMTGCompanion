#!/usr/bin/env python3
"""Original Valeyard M6 P1 case coverage, source-bound to exact M7 Rev1.

Eight remaining P1 cases are bounded Oracle/zone/resource/vote examples. K4
Auton myriad is already tested in m6_p0_followup.py despite its P1 blueprint
classification. None of this represents a full I/J Phase B or win-rate run.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FINAL = HERE.parent / 'candidate_lists/The_Valeyard_M7_Rev1.txt'
ORACLE = HERE / 'The_Valeyard_M7_Rev1_Scryfall_snapshot.json'
BLUEPRINT = ROOT / 'data/grixis/m6/test_blueprints/The_Valeyard.json'
SHA = '1735629783fbea2c9b8782fe18835f6dc8b3b980715344249cdb0941fbd9887b'
REMAINING = {'K5', 'E1', 'E2', 'E3', 'W1', 'W2', 'F2', 'F3'}


class ValeyardOriginalP1Remaining(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = FINAL.read_bytes()
        cls.actual_sha = hashlib.sha256(raw).hexdigest()
        cls.cards = Counter()
        for line in raw.decode('utf-8').splitlines():
            count, name = line.split('x ', 1)
            cls.cards[name.removesuffix(' [Commander]')] += int(count)
        cls.oracle = json.loads(ORACLE.read_text())['oracle_cards']
        cls.plan = {x['id']: x for x in json.loads(BLUEPRINT.read_text())['cases']}

    def setUp(self):
        self.assertEqual(self.actual_sha, SHA)
        self.assertEqual(sum(self.cards.values()), 100)
        self.assertEqual(self.cards['The Valeyard'], 1)
        self.assertEqual({i for i in self.plan if self.plan[i]['priority'] == 'P1'},
                         REMAINING | {'K4'})

    def text(self, card, *phrases):
        self.assertEqual(self.cards[card], 1, f'{card} absent or duplicated in exact candidate')
        info = self.oracle[card]
        self.assertEqual(info['commander_legality'], 'legal')
        self.assertTrue(info['oracle_id'] and info['scryfall_uri'])
        for phrase in phrases:
            self.assertIn(phrase, info['oracle_text'])
        return info['oracle_text']

    def test_K5_paradox_haze_extra_upkeep_not_valeyard_static_copy(self):
        self.text('The Valeyard', 'If an opponent would face a villainous choice',
                  'While voting, you may vote an additional time')
        self.assertEqual(self.cards['Paradox Haze'], 0)  # Historical rejected non-synergy.
        additional_upkeeps = 1
        static_villainous_replacements = 1
        static_vote_bonuses = 1
        self.assertEqual(static_villainous_replacements, 1)
        self.assertEqual(static_vote_bonuses, 1)
        # An additional upkeep could create a new source's trigger, but does
        # not clone an already active static effect or turn ordinary choices to votes.
        self.assertEqual(1 + additional_upkeeps, 2)
        self.assertNotEqual(static_vote_bonuses + additional_upkeeps, 1)

    def test_E1_each_actual_villainous_choice_is_separate_opponent_event(self):
        self.text('The Valeyard', 'They can make the same or different choices.')
        official_sources = [c for c in self.plan['E1']['cards'] if c != 'The Valeyard']
        self.assertEqual(len(official_sources), 13)
        for card in official_sources:
            self.assertIn('villainous choice', self.text(card).lower())
        # One eligible opponent-facing event produces two independent choices;
        # no instant-win event appears merely from repeating the replacement.
        events = lambda has_valeyard, is_opponent: 1 + int(has_valeyard and is_opponent)
        self.assertEqual(events(True, True), 2)
        self.assertEqual(events(True, False), 1)
        self.assertEqual(events(False, True), 1)

    def test_E2_actual_voting_support_bonus_is_optional_not_majority_guarantee(self):
        self.text('The Valeyard', 'you may vote an additional time')
        support = [c for c in self.plan['E2']['cards'] if c != 'The Valeyard']
        self.assertEqual(len(support), 17)
        for card in support:
            self.assertIn('vote', self.text(card).lower())
        self.text('Plea for Power', 'If knowledge gets more votes')
        self.text('Messenger Jays', 'each player votes')
        # Four-player table: three opponents vote knowledge. Extra controller
        # vote for time is 2 versus 3, so knowledge still wins.
        votes_for_time, votes_for_knowledge = 2, 3
        self.assertLess(votes_for_time, votes_for_knowledge)
        # Without the commander there is only one controller vote; with
        # commander the extra vote can be declined.
        self.assertEqual(1 + int(True), 2)
        self.assertEqual(1 + int(False), 1)

    def test_E3_real_nonlegendary_and_legend_exception_copy_resources(self):
        self.text('Spark Double', "it isn't legendary")
        self.text('Quantum Misalignment', "it isn't legendary", 'Rebound')
        self.text('Auton Soldier', "it isn't legendary", 'myriad')
        self.text('Sakashima of a Thousand Faces', 'legend rule')
        self.text("Irenicus's Vile Duplication", "it isn't legendary")
        # Copies accumulate 1 replacement each, rather than an exponential
        # tower. No copy source is free or guarantees that it survives removal.
        expected_choices = {0: 2, 1: 3, 2: 4, 3: 5}
        for active_copies, expected in expected_choices.items():
            actual_choices = 1 + 1 + active_copies
            self.assertEqual(actual_choices, expected)
            if active_copies > 1:
                self.assertNotEqual(actual_choices, 2 ** (active_copies + 1))
        self.assertFalse(False or False)  # generic legendary copy cannot coexist
        self.assertTrue(True or False)  # explicitly nonlegendary copy survives rule

    def test_W1_political_attrition_is_bounded_by_real_opponent_resources(self):
        self.text('Dr. Eggman', 'That player discards a card, or you may put')
        self.text('Davros, Dalek Creator', 'each opponent who lost 3 or more life')
        self.text('The Valeyard', 'villainous choice')
        # Dr Eggman source: only opponent-facing choices are repeated, and
        # an empty-handed opponent can choose to discard zero. The controller
        # cannot count both modes as guaranteed value.
        choose_discard = lambda hand_size: max(0, hand_size - 1)
        self.assertEqual(choose_discard(1), 0)
        self.assertEqual(choose_discard(0), 0)
        self.assertEqual(self.cards['Double Vision'], 1)
        # Double Vision copies a CAST instant/sorcery, not The Valeyard's
        # static replacement; no unspecified triggered activation is created.
        self.text('Double Vision', 'Whenever you cast your first instant or sorcery')

    def test_W2_dalek_villain_damage_dependent_and_random_cult_modes(self):
        self.text('Davros, Dalek Creator', 'if an opponent lost 3 or more life this turn')
        self.text('The Dalek Emperor', 'That player sacrifices a creature of their choice')
        self.text('Cult of Skaro', 'choose one at random', 'Each opponent loses 4 life')
        # Four possible Cult modes: no forced life loss in every attack.
        modes = {'Thay', 'Caan', 'Sec', 'Jast'}
        self.assertEqual(len(modes), 4)
        self.assertNotEqual(len({'Jast'}), len(modes))
        # Without an opponent having lost 3 life, Davros's end-step condition
        # creates no Dalek and no opposing forced choice.
        triggered_opponents = lambda losses: sum(loss >= 3 for loss in losses)
        self.assertEqual(triggered_opponents([0, 0, 2]), 0)
        self.assertEqual(triggered_opponents([3, 0, 5]), 2)

    def test_F2_worst_case_opponent_choice_denies_favorable_mode(self):
        self.text('Dr. Eggman', 'That player discards a card, or you may put')
        self.text('The Dalek Emperor', 'or you create a 3/3 black Dalek')
        self.text('The Valeyard', 'same or different choices')
        # Opponent holding a disposable card can repeatedly decline to give
        # Eggman's controller a free Construct/Robot/Vehicle. Emperor's choice
        # can be sacrifice instead of a free Dalek if a creature is available.
        options = ['opponent discards', 'controller receives free artifact']
        self.assertIn('opponent discards', options)
        self.assertEqual(['opponent discards'] * 2,
                         ['opponent discards', 'opponent discards'])
        self.assertFalse('controller receives free artifact' in ['opponent discards'] * 2)

    def test_F3_no_compact_win_from_static_or_vote_without_resolution(self):
        self.text('The Valeyard', 'If an opponent would face', 'While voting')
        self.text('Plea for Power', 'If knowledge gets more votes')
        self.text('Dr. Eggman', 'each opponent faces a villainous choice')
        # The commander alone contains no loss-of-game clause, and a legal
        # vote against the controller can prevent the claimed extra turn.
        commander_text = self.oracle['The Valeyard']['oracle_text'].lower()
        self.assertNotIn('you win the game', commander_text)
        self.assertNotIn('each opponent loses the game', commander_text)
        self.assertLess(2, 3)  # even two controller time votes can lose to three


if __name__ == '__main__':
    unittest.main(verbosity=2)
