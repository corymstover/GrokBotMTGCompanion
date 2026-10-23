"""Abaddon provisional six: bounded source-paid mechanical and Oracle preflight tests.

The source transport is mocked ONLY for deterministic offline mutation/fail-
closed tests; the workflow separately runs the live Scryfall audit. This is
not a full multiplayer simulator, M6 I/J certificate or owner approval.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_abaddon_stage14_live_oracle import (
    validate, OracleGateError, ROOT, REPORT, BASE,
)

D = ROOT / "data/grixis/m7/research_challengers"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"


def sources():
    full = dict(json.loads(ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"])
    for path in (
        D / "Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json",
        D / "Abaddon_the_Despoiler_stage4_13_source_cards_20261022.json",
        D / "Abaddon_the_Despoiler_stage8_nine_offranking_Scryfall_20261022.json",
        D / "Abaddon_the_Despoiler_stage13_ten_EDHREC_Scryfall_20261023.json",
    ):
        full.update(json.loads(path.read_text(encoding="utf-8"))["oracle_cards"])
    return full


def offline_scryfall_fetch(*, mutate_card=None, mutate_key=None, mutate_value=None):
    all_sources = sources()
    by_front = {key.split(" // ", 1)[0]: (key, v)
                for key, v in all_sources.items()}

    def get_json(url, payload=None):
        cards = []
        for requested in payload["identifiers"]:
            key, v = by_front[requested["name"]]
            row = {
                "object": "card", "name": key,
                "oracle_id": v["oracle_id"],
                "scryfall_uri": v["scryfall_uri"],
                "color_identity": v["color_identity"],
                "cmc": v.get("cmc", v.get("mana_value")),
                "mana_cost": v.get("mana_cost", ""),
                "oracle_text": v["oracle_text"],
                "legalities": {"commander": v["commander_legality"]},
                "games": ["paper"],
            }
            if key == mutate_card:
                if mutate_key == "commander_legality":
                    row["legalities"]["commander"] = mutate_value
                else:
                    row[mutate_key] = mutate_value
            cards.append(row)
        return json.dumps({"object": "list", "not_found": [], "data": cards}).encode()

    return get_json


def next_hand_cascade_sources(*, life_loss_before_cast, mv, abaddon=True,
                              sakashima_abaddon_copy=False):
    """Count triggers when THIS hand spell was cast, no retroactive increase."""
    if not abaddon or life_loss_before_cast < mv:
        return 0
    return 1 + int(sakashima_abaddon_copy)


def damage_from_paid_mage_offspring(*, opponents=3, solphim=False,
                                   bloodletter=False):
    """Mage and one paid offspring each ping on LATER noncreature cast."""
    damage_each = 2 if solphim else 1
    lost_each = damage_each * (2 if bloodletter else 1)
    return opponents * 2 * lost_each


class AbaddonStage14Preflight(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads(REPORT.read_text(encoding="utf-8"))

    def test_exact_new_six_has_protected_printed_cascade(self):
        m = self.m
        self.assertFalse(m["owner_ready"])
        self.assertFalse(m["formal_m6_certification"])
        self.assertFalse(m["m6_ij_candidate_specific_rebound"])
        self.assertFalse(m["explicit_owner_approval_for_new_list"])
        self.assertTrue(m["deck3_hold"])
        self.assertEqual(len(m["preferred_provisional"]["add"]), 6)
        self.assertEqual(len(m["preferred_provisional"]["cut"]), 6)
        path = ROOT / m["preferred_provisional"]["path"]
        content = path.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("1x Abaddon the Despoiler [Commander]"))
        for name in ["Noise Marine", "Nalfeshnee", "Nightscape Familiar",
                     "Neheb, the Eternal", "Aggravated Assault", "Call Forth the Tempest"]:
            self.assertIn("1x " + name + "\n", content)
        self.assertNotIn("1x Keeper of Secrets\n", content)
        self.assertNotIn("1x Ponder\n", content)
        self.assertEqual(len(m["other_material_dispositions"]), 6)

    def test_mocked_live_card_identity_100_and_current_oracle_gate(self):
        r = validate(fetch=offline_scryfall_fetch(), sleeper=lambda _: None)
        self.assertEqual(r["physical_cards"], 100)
        self.assertGreaterEqual(r["oracle_unique_names_checked"], 90)
        self.assertEqual(r["candidate_raw_sha256"],
                         self.m["preferred_provisional"]["raw_sha256"])
        self.assertFalse(r["owner_ready"])
        self.assertFalse(r["m6_ij_rebound"])

    def test_fail_closed_new_mage_text_and_legality_mutations(self):
        with self.assertRaisesRegex(OracleGateError, "Material"):
            validate(fetch=offline_scryfall_fetch(
                mutate_card="Coruscation Mage", mutate_key="oracle_text",
                mutate_value="Whenever you cast a noncreature spell, ping a creature."
            ), sleeper=lambda _: None)
        with self.assertRaisesRegex(OracleGateError, "Illegal"):
            validate(fetch=offline_scryfall_fetch(
                mutate_card="Coruscation Mage", mutate_key="commander_legality",
                mutate_value="banned"
            ), sleeper=lambda _: None)

    def test_first_main_sanctum_and_two_abaddon_cascades_no_retroactivity(self):
        # Turn where shrine survived, first main triggered X3 on three opponents.
        self.assertEqual(next_hand_cascade_sources(
            life_loss_before_cast=3, mv=3, sakashima_abaddon_copy=True), 2)
        self.assertEqual(next_hand_cascade_sources(
            life_loss_before_cast=3, mv=4, sakashima_abaddon_copy=True), 0)
        # A fully resolving Wheel now makes Sheoldred trigger 21*2 life loss.
        x_after_wheel = 3 + (3 * 7 * 2)
        self.assertEqual(x_after_wheel, 45)
        # AFTER Wheel: hand 5 MV sees two grants; Wheel's own grants remain 2.
        self.assertEqual(next_hand_cascade_sources(
            life_loss_before_cast=x_after_wheel, mv=5, sakashima_abaddon_copy=True), 2)
        self.assertEqual(next_hand_cascade_sources(
            life_loss_before_cast=0, mv=3, sakashima_abaddon_copy=True), 0)
        # Rule of Law means each cast may TRIGGER cascade, but its exile-hit
        # spell cannot be cast if player already cast the originating spell.

    def test_paid_offspring_later_cast_loss_and_interference(self):
        self.assertEqual(damage_from_paid_mage_offspring(), 6)
        self.assertEqual(damage_from_paid_mage_offspring(solphim=True), 12)
        self.assertEqual(damage_from_paid_mage_offspring(
            solphim=True, bloodletter=True), 24)
        src = sources()["Coruscation Mage"]
        self.assertEqual(src["mana_cost"], "{1}{R}")
        self.assertIn("Offspring {2}", src["oracle_text"])
        # Not unlimited copies: Offspring can be paid once per Mage cast and
        # requires TWO actually available generic mana even on free cascade.
        # Opponent removing the original still leaves the offspring token,
        # but removing both creatures stops further two-mage burn.


if __name__ == "__main__":
    unittest.main()
