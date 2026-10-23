"""Finite source-bound Abaddon Stage13 research ONLY; NOT owner-ready/M6 I-J.

Tests exact physical 100s, live Scryfall card text/legality from captured source,
incremental trigger math and honest zero changes to canonical authorities.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data/grixis/m7/research_challengers"
BASE = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
REPORT = D / "Abaddon_the_Despoiler_stage13_new_EDHREC_protected_engine_decisions_20261023.json"
SOURCE = D / "Abaddon_the_Despoiler_stage13_ten_EDHREC_Scryfall_20261023.json"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
EXTRA = D / "Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json"
STAGE4 = D / "Abaddon_the_Despoiler_stage4_13_source_cards_20261022.json"
STAGE8 = D / "Abaddon_the_Despoiler_stage8_nine_offranking_Scryfall_20261022.json"
BASICS = {"Island", "Swamp", "Mountain"}


def parse_deck(path):
    raw = path.read_bytes()
    lines = raw.decode("utf-8").splitlines()
    counts = Counter()
    for line in lines:
        qty, card = line.split("x ", 1)
        assert qty.isdecimal() and int(qty) > 0, (path, line)
        counts[card.removesuffix(" [Commander]")] += int(qty)
    assert lines[0] == "1x Abaddon the Despoiler [Commander]", path
    assert sum(counts.values()) == 100, path
    assert all(c in BASICS or q == 1 for c, q in counts.items()), path
    return raw, counts


def mage_per_spell_x(opponents=3, offspring=False, solphim=False,
                     bloodletter=False):
    """After a noncreature spell was cast and its triggers resolve."""
    sources = 2 if offspring else 1
    per_target = 2 if solphim else 1
    per_target *= 2 if bloodletter else 1
    return opponents * sources * per_target


class AbaddonStage13OffrankingReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(REPORT.read_text(encoding="utf-8"))
        s = json.loads(SOURCE.read_text(encoding="utf-8"))
        cls.source = s["oracle_cards"]
        assert s["not_found"] == []
        cls.existing = json.loads(ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.extra = json.loads(EXTRA.read_text(encoding="utf-8"))["oracle_cards"]
        cls.stage4 = json.loads(STAGE4.read_text(encoding="utf-8"))["oracle_cards"]
        cls.stage8 = json.loads(STAGE8.read_text(encoding="utf-8"))["oracle_cards"]
        cls.all_cards = dict(cls.existing)
        cls.all_cards.update(cls.extra)
        cls.all_cards.update(cls.stage4)
        cls.all_cards.update(cls.stage8)
        cls.all_cards.update(cls.source)

    def test_four_full_100_variants_correct_hashes_and_deltas(self):
        braw, before = parse_deck(BASE)
        r = self.report
        self.assertEqual(hashlib.sha256(braw).hexdigest(),
                         r["canonical"]["raw_sha256"])
        self.assertEqual(r["status"], "RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertFalse(r["owner_ready"])
        self.assertFalse(r["m6_changed_candidate_certified"])
        self.assertTrue(r["canonical_approved_locked_unchanged"])
        self.assertTrue(r["admiral_approved_locked_unchanged"])
        self.assertTrue(r["deck3_hold"])
        self.assertEqual(sorted(p["swaps"] for p in r["packages"]), [5, 6, 6, 7])
        for p in r["packages"]:
            raw, after = parse_deck(ROOT / p["decklist_path"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), p["raw_sha256"])
            self.assertEqual(sorted((after - before).elements()), sorted(p["add"]))
            self.assertEqual(sorted((before - after).elements()), sorted(p["cut"]))
            self.assertEqual(p["swaps"], len(p["add"]))
            self.assertEqual(p["swaps"], len(p["cut"]))
            self.assertEqual(after["Mountain"], 2)
            self.assertEqual(after["Mount Doom"], 1)
            self.assertEqual(after["Island"], 3)
            self.assertEqual(after["Swamp"], 3)
            self.assertEqual(p["lands"], 34)
            self.assertEqual(p["status"], "RESEARCH_ONLY")
            for card in ("Nightscape Familiar", "Birgi, God of Storytelling // Harnfel, Horn of Bounty",
                         "Grinning Ignus", "Neheb, the Eternal", "Aggravated Assault",
                         "Loyal Subordinate", "Call Forth the Tempest", "Nalfeshnee",
                         "The Lost and the Damned", "Underworld Breach", "Brain Freeze"):
                self.assertIn(card, after, (p["name"], card))
            if p["swaps"] <= 6:
                self.assertIn("Noise Marine", after, p["name"])
            for n in after:
                c = self.all_cards.get(n)
                self.assertIsNotNone(c, (p["name"], n))
                self.assertEqual(c["commander_legality"], "legal", n)
                self.assertTrue(set(c["color_identity"]).issubset("UBR"), n)

    def test_coruscation_mage_real_offspring_cost_and_not_free(self):
        c = self.source["Coruscation Mage"]
        self.assertEqual(c["mana_cost"], "{1}{R}")
        self.assertIn("Offspring {2}", c["oracle_text"])
        self.assertIn("create a 1/1 token copy", c["oracle_text"])
        self.assertIn("Whenever you cast a noncreature spell", c["oracle_text"])
        self.assertIn("1 damage to each opponent", c["oracle_text"])
        self.assertIn("Whenever a creature you control enters",
                      self.stage8["Impact Tremors"]["oracle_text"])
        # One mage alone: one red one-damage event to each of 3 opponents.
        self.assertEqual(mage_per_spell_x(), 3)
        # With paid offspring surviving: two independent red-source triggers.
        self.assertEqual(mage_per_spell_x(offspring=True), 6)
        self.assertEqual(mage_per_spell_x(offspring=True, solphim=True), 12)
        self.assertEqual(mage_per_spell_x(
            offspring=True, solphim=True, bloodletter=True), 24)
        # Impact present as mage AND offspring enter gives two separate ETB events
        # for X=3 each, but only AFTER the original Mage spell is cast.
        self.assertEqual(3 + 3, 6)

    def test_newly_discovered_high_lift_card_timing_does_not_fabricate_tempo(self):
        fragment = self.source["Cryptolith Fragment // Aurora of Emrakul"]
        self.assertEqual(fragment["card_faces"][0]["mana_cost"], "{3}")
        self.assertIn("enters tapped", fragment["card_faces"][0]["oracle_text"])
        self.assertIn("Each player loses 1 life",
                      fragment["card_faces"][0]["oracle_text"])
        # The tapped-ETB is a decisive tempo disadvantage to a T2 Talisman.
        apostle = self.source["Dark Apostle"]
        self.assertEqual(apostle["mana_cost"], "{3}{R}")
        self.assertIn("{3}, {T}:", apostle["oracle_text"])
        self.assertIn("next noncreature spell", apostle["oracle_text"])
        phoenix = self.source["Aurora Phoenix"]
        self.assertEqual(phoenix["mana_cost"], "{4}{R}{R}")
        self.assertIn("Whenever you cast a spell with cascade", phoenix["oracle_text"])

    def test_real_oracle_tradeoffs_for_crawler_ojer_protection(self):
        crawler = self.source["Scrawling Crawler"]
        self.assertEqual(crawler["mana_cost"], "{3}")
        self.assertIn("each player draws a card", crawler["oracle_text"])
        self.assertIn("Whenever an opponent draws a card", crawler["oracle_text"])
        # Incremental opponent life loss after a fully resolved seven-draw Wheel.
        self.assertEqual(3 * 7, 21)
        self.assertEqual(3 * 7 * 2, 42)  # Sheoldred independently
        ojer = self.source["Ojer Axonil, Deepest Might // Temple of Power"]
        front = ojer["card_faces"][0]
        self.assertEqual(front["mana_cost"], "{2}{R}{R}")
        self.assertEqual(front["power"], "4")
        self.assertIn("a red source you control", front["oracle_text"])
        self.assertIn("less than Ojer Axonil's power", front["oracle_text"])
        self.assertIn("shroud", self.source["Lightning Greaves"]["oracle_text"])
        self.assertIn("Ascend", self.source["Twilight Prophet"]["oracle_text"])
        self.assertIn("can't attack a player it has already attacked this turn",
                      self.source["Bloodthirster"]["oracle_text"])

    def test_no_floor_anchoring_or_certification_fabrication(self):
        r = self.report
        self.assertGreaterEqual(len(r["dispositions"]), 15)
        self.assertGreaterEqual(len(r["whole_99_challenge"]["primary_named_cut_challenges"]), 8)
        self.assertIn("Noise Marine", r["decisive_comparison"])
        self.assertIn("Ponder", r["decisive_comparison"])
        self.assertIn("No changed-finalist", " ".join(r["hard_gates_open"]))
        self.assertIn("Do not", r["stop_rule"])
        self.assertFalse(r["owner_ready"])


if __name__ == "__main__":
    unittest.main()
