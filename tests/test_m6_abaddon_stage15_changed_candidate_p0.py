"""Bounded Abaddon Stage15 changed-card M6 P0 game-state fixtures.

Executed cases assert actual cost/phase/stack ordering and adverse events for
the provisional protected six. This is not a complete Magic engine, win-rate
model, M6 I local-optimum certificate, J bundle or owner approval. Old P0/P1
fixtures covering unaffected core must be reused, never counted anew here.
"""
from dataclasses import dataclass
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data/grixis/m7/research_challengers"
SOURCE_NEW = D / "Abaddon_the_Despoiler_stage13_ten_EDHREC_Scryfall_20261023.json"
SOURCE_OLD = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
SOURCE_MORE = D / "Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json"
SOURCE_MAGE = D / "Abaddon_the_Despoiler_stage8_nine_offranking_Scryfall_20261022.json"
SOURCE_COPY = D / "Abaddon_the_Despoiler_stage4_13_source_cards_20261022.json"
MANIFEST = D / "Abaddon_the_Despoiler_stage14_provisional_protected_wheel_six_20261023.json"


class Unpayable(ValueError):
    pass


@dataclass
class Pool:
    generic: int = 0
    red: int = 0
    black: int = 0

    def pay(self, generic=0, red=0, black=0):
        # Colored requirements MUST come from correct colors. Remaining
        # colored mana can contribute generic, but never the reverse.
        if self.red < red or self.black < black:
            raise Unpayable("missing colored mana")
        self.red -= red
        self.black -= black
        generic_left = generic
        c = min(self.generic, generic_left)
        self.generic -= c
        generic_left -= c
        for color in ("red", "black"):
            c = min(getattr(self, color), generic_left)
            setattr(self, color, getattr(self, color) - c)
            generic_left -= c
        if generic_left:
            raise Unpayable("missing generic mana")
        return True


@dataclass
class OwnTurn:
    opponent_count: int = 3
    loss_total: int = 0
    bloodletter: bool = False
    solphim: bool = False
    abaddon_copies: int = 1
    mage_pingers: int = 0
    impact_tremors: bool = False
    cast_count: int = 0
    rule_of_law: bool = False
    first_main_begun: bool = False

    def opponent_loss(self, amount_per_opponent, is_damage=False, red_source=False):
        amount = amount_per_opponent
        # Solphim doubles controlled noncombat damage; not direct life loss.
        if is_damage and self.solphim:
            amount *= 2
        # Bloodletter only doubles what each opponent loses during own turn.
        if self.bloodletter:
            amount *= 2
        self.loss_total += self.opponent_count * amount

    def first_main(self, *, number_of_shrines_when_trigger_resolves):
        if self.first_main_begun:
            raise ValueError("first main already began")
        self.first_main_begun = True
        if number_of_shrines_when_trigger_resolves:
            # Sanctum's X uses current shrine count on trigger RESOLUTION.
            self.opponent_loss(number_of_shrines_when_trigger_resolves)

    def cast_from_hand(self, mv, noncreature=False):
        if self.rule_of_law and self.cast_count >= 1:
            raise Unpayable("Rule of Law second spell")
        granted_cascades = self.abaddon_copies if mv <= self.loss_total else 0
        self.cast_count += 1
        # Cast-triggered pingers resolve AFTER Abaddon's eligibility was
        # established on casting. They cannot retroactively change cascade.
        if noncreature and self.mage_pingers:
            for _ in range(self.mage_pingers):
                self.opponent_loss(1, is_damage=True, red_source=True)
        return granted_cascades

    def cast_cascade_hit(self):
        # Assumes one already qualifying cascade trigger resolved and exposed
        # a legally castable exiled hit with no extra payable cost.
        if self.rule_of_law and self.cast_count >= 1:
            return False
        self.cast_count += 1
        return True

    def mage_enters(self, *, pay_offspring, pool):
        # Coruscation Mage costs {1}{R}, with optional Offspring {2}.
        # A free cascade hit waives its normal mana cost, not additional {2}.
        if pay_offspring:
            pool.pay(generic=2)
        self.mage_pingers += 1 + int(pay_offspring)
        if self.impact_tremors:
            for _ in range(1 + int(pay_offspring)):
                self.opponent_loss(1, is_damage=True, red_source=True)

    def sheoldred_opponents_draw(self, cards_per_opponent):
        self.opponent_loss(2 * cards_per_opponent)
        # Own player's draw-gain is NOT opponent life lost.


class AbaddonStage15SourcePaidP0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new = json.loads(SOURCE_NEW.read_text(encoding="utf-8"))["oracle_cards"]
        cls.old = json.loads(SOURCE_OLD.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.more = json.loads(SOURCE_MORE.read_text(encoding="utf-8"))["oracle_cards"]
        cls.mage = json.loads(SOURCE_MAGE.read_text(encoding="utf-8"))["oracle_cards"]
        cls.copy = json.loads(SOURCE_COPY.read_text(encoding="utf-8"))["oracle_cards"]
        cls.candidate = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_p0_01_source_payable_mage_offspring_normal_cast(self):
        mage = self.new["Coruscation Mage"]
        self.assertEqual(mage["mana_cost"], "{1}{R}")
        self.assertIn("Offspring {2}", mage["oracle_text"])
        p = Pool(generic=3, red=1)
        p.pay(generic=1, red=1)
        turn = OwnTurn(impact_tremors=True)
        turn.mage_enters(pay_offspring=True, pool=p)
        self.assertEqual((p.generic, p.red), (0, 0))
        self.assertEqual(turn.mage_pingers, 2)
        self.assertEqual(turn.loss_total, 6)  # two ETBs, three opponents

    def test_p0_02_offspring_not_free_when_mage_hit_by_cascade(self):
        turn = OwnTurn(impact_tremors=True)
        with self.assertRaisesRegex(Unpayable, "generic"):
            turn.mage_enters(pay_offspring=True, pool=Pool())
        self.assertEqual(turn.mage_pingers, 0)
        turn.mage_enters(pay_offspring=True, pool=Pool(generic=2))
        self.assertEqual(turn.loss_total, 6)
        self.assertEqual(turn.mage_pingers, 2)

    def test_p0_03_later_cast_two_mage_triggers_not_own_cast_retroactive(self):
        turn = OwnTurn(impact_tremors=False, mage_pingers=2)
        self.assertEqual(turn.cast_from_hand(3, noncreature=True), 0)
        self.assertEqual(turn.loss_total, 6)
        self.assertEqual(turn.cast_from_hand(3, noncreature=True), 1)
        self.assertEqual(turn.loss_total, 12)

    def test_p0_04_offspring_survives_one_spot_removed_original(self):
        turn = OwnTurn(mage_pingers=2)
        # Opponent kills just one separate creature before next hand cast.
        turn.mage_pingers -= 1
        self.assertEqual(turn.cast_from_hand(1, noncreature=True), 0)
        self.assertEqual(turn.loss_total, 3)

    def test_p0_05_sakashima_new_grant_only_after_enter_resolution(self):
        self.assertEqual(self.copy["Sakashima of a Thousand Faces"]["mana_cost"], "{3}{U}")
        self.assertIn("legend rule", self.copy["Sakashima of a Thousand Faces"]["oracle_text"])
        turn = OwnTurn(loss_total=12, abaddon_copies=1)
        self.assertEqual(turn.cast_from_hand(4), 1)  # Sakashima itself
        turn.abaddon_copies = 2  # ETB copied original Abaddon after resolving
        self.assertEqual(turn.cast_from_hand(3), 2)  # later hand spell

    def test_p0_06_abaddon_removed_before_sakashima_etb_reduces_copy_ceiling(self):
        turn = OwnTurn(loss_total=6, abaddon_copies=1)
        self.assertEqual(turn.cast_from_hand(4), 1)
        turn.abaddon_copies = 0  # opponent removes original before clone enters
        self.assertEqual(turn.cast_from_hand(3), 0)

    def test_p0_07_sanctum_one_shrine_first_main_life_loss_vs_damage(self):
        self.assertIn("first main phase", self.mage["Sanctum of Stone Fangs"]["oracle_text"])
        turn = OwnTurn(solphim=True)
        turn.first_main(number_of_shrines_when_trigger_resolves=1)
        self.assertEqual(turn.loss_total, 3)  # Solphim doesn't alter LIFE LOSS
        self.assertEqual(turn.cast_from_hand(3), 1)

    def test_p0_08_sanctum_removed_in_response_current_shrine_count_zero(self):
        turn = OwnTurn(bloodletter=True)
        turn.first_main(number_of_shrines_when_trigger_resolves=0)
        self.assertEqual(turn.loss_total, 0)
        turn.cast_from_hand(3)
        self.assertEqual(turn.loss_total, 0)

    def test_p0_09_sheoldred_wheel_loss_only_after_cast(self):
        s = self.more["Sheoldred, the Apocalypse"]
        self.assertIn("Whenever an opponent draws a card, they lose 2 life", s["oracle_text"])
        turn = OwnTurn(loss_total=3, abaddon_copies=2)
        self.assertEqual(turn.cast_from_hand(3, noncreature=True), 2)
        turn.sheoldred_opponents_draw(7)
        self.assertEqual(turn.loss_total, 45)
        self.assertEqual(turn.cast_from_hand(5), 2)

    def test_p0_10_sheoldred_windfall_variable_and_bloodletter(self):
        t = OwnTurn(bloodletter=True)
        t.sheoldred_opponents_draw(2)
        self.assertEqual(t.loss_total, 24)
        t2 = OwnTurn(bloodletter=True)
        t2.sheoldred_opponents_draw(7)
        self.assertEqual(t2.loss_total, 84)
        self.assertGreater(t2.loss_total, t.loss_total)

    def test_p0_11_mount_doom_paid_activation_and_noncombat_replacement(self):
        land = self.more["Mount Doom"]
        self.assertIn("{1}{B}{R}, {T}: Mount Doom deals 1 damage to each opponent",
                      land["oracle_text"])
        # Activation uses the land's {T}; its own tap-for-B/R ability is
        # unavailable while activating the same {T} ability.
        pool = Pool(generic=1, red=1, black=1)
        pool.pay(generic=1, red=1, black=1)
        t = OwnTurn(solphim=True, bloodletter=True)
        t.opponent_loss(1, is_damage=True)
        self.assertEqual(t.loss_total, 12)
        self.assertEqual((pool.generic, pool.red, pool.black), (0, 0, 0))
        with self.assertRaises(Unpayable):
            Pool(generic=1, red=1).pay(generic=1, red=1, black=1)

    def test_p0_12_rule_of_law_cascade_spells_forbidden_land_damage_works(self):
        t = OwnTurn(loss_total=20, abaddon_copies=2, rule_of_law=True)
        self.assertEqual(t.cast_from_hand(3), 2)
        self.assertFalse(t.cast_cascade_hit())
        with self.assertRaisesRegex(Unpayable, "Rule of Law"):
            t.cast_from_hand(1)
        # Land activated ability is NOT another spell; still X3.
        t.opponent_loss(1, is_damage=True)
        self.assertEqual(t.loss_total, 23)

    def test_p0_13_sole_mage_and_sol_bloodletter_multiplied_delayed_cast(self):
        t = OwnTurn(mage_pingers=2, solphim=True, bloodletter=True)
        self.assertEqual(t.cast_from_hand(1, noncreature=True), 0)
        self.assertEqual(t.loss_total, 24)
        self.assertEqual(t.cast_from_hand(5), 1)

    def test_p0_14_signature_nonhand_40k_loss_explicit_in_selection(self):
        # Keeper was one cast-from-exile targeted MV damage source (6MV own
        # cost) and is REMOVED; Nalfeshnee and Noise printed cascade retained.
        chosen = self.candidate["preferred_provisional"]
        self.assertIn("Keeper of Secrets", chosen["cut"])
        self.assertNotIn("Noise Marine", chosen["cut"])
        self.assertNotIn("Nalfeshnee", chosen["cut"])
        self.assertIn("Whenever you cast a spell from anywhere other than your hand",
                      self.old["Keeper of Secrets"]["oracle_text"])
        self.assertIn("Cascade", self.old["Noise Marine"]["oracle_text"])
        self.assertIn("Whenever you cast a spell from exile",
                      self.old["Nalfeshnee"]["oracle_text"])


if __name__ == "__main__":
    unittest.main()
