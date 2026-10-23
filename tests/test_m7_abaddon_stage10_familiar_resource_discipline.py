"""Abaddon stage10 resource-faithful finite comparisons; research only.

Checks the Nightscape/Familiar/Birgi/Ignus cost interaction that was missed
in Stage9 opportunity costs; does not measure win rates or certify M6 I/J.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage10_familiar_mana_and_adversarial_review_20261022.json"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
IMPACT = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage8_nine_offranking_Scryfall_20261022.json"
VEY = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage9_veyran_roaming_throne_Scryfall_20261022.json"
CANON = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
BASICS = {"Island", "Mountain", "Swamp"}


def physical_100(path):
    raw = path.read_bytes()
    counts = Counter()
    for line in raw.decode("utf-8").splitlines():
        qty, name = line.split("x ", 1)
        counts[name.removesuffix(" [Commander]")] += int(qty)
    assert sum(counts.values()) == 100
    assert all(n in BASICS or q == 1 for n, q in counts.items())
    assert counts["Abaddon the Despoiler"] == 1
    return raw, counts


def ignus_cycle(n=3, *, familiar=False, tremors=False, rule_of_law=False,
                removal_after_first=False):
    """Finite mana ledger, not an opponent-simulation or a game engine.

    Assumes Birgi FRONT, Ignus on board, one initial {R}, empty stack, own
    main phase, all engine pieces paid for and no other sources of mana.
    Ignus's sorcery-restricted mana ability does not use the stack.
    """
    red, colorless, spell_casts, opponent_life_loss = 1, 0, 0, 0
    for _ in range(n):
        if rule_of_law and spell_casts == 1:
            break
        if removal_after_first and spell_casts == 1:
            break
        assert red >= 1
        red -= 1  # Ignus activation {R}; return to hand as part of cost
        colorless += 2
        red += 1  # Ignus immediately adds {C}{C}{R}
        reduced_generic = 1 if familiar else 2
        assert colorless >= reduced_generic and red >= 1
        colorless -= reduced_generic
        red -= 1  # pay {1}{R} or {2}{R} to CAST Ignus
        spell_casts += 1
        red += 1  # Birgi SPELL CAST red trigger (creature casts count)
        if tremors:
            opponent_life_loss += 3  # each of three opponents loses 1 to ETB
    return red, colorless, spell_casts, opponent_life_loss


class AbaddonStage10FiniteAdversarial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(EVIDENCE.read_text(encoding="utf-8"))
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.impact = json.loads(IMPACT.read_text(encoding="utf-8"))["oracle_cards"]
        cls.veyran = json.loads(VEY.read_text(encoding="utf-8"))["oracle_cards"]

    def test_source_exact_costs_and_sorcery_mana_activation(self):
        o = self.oracle
        self.assertEqual(o["Abaddon the Despoiler"]["mana_cost"], "{2}{U}{B}{R}")
        self.assertIn("Blue spells and red spells you cast cost {1} less",
                      o["Nightscape Familiar"]["oracle_text"])
        self.assertEqual(o["Grinning Ignus"]["mana_cost"], "{2}{R}")
        self.assertIn("{R}, Return this creature to its owner's hand: Add {C}{C}{R}",
                      o["Grinning Ignus"]["oracle_text"])
        self.assertIn("Activate only as a sorcery",
                      o["Grinning Ignus"]["oracle_text"])
        self.assertIn("Whenever you cast a spell, add {R}",
                      o["Birgi, God of Storytelling // Harnfel, Horn of Bounty"]["oracle_text"])
        self.assertIn("Whenever a creature you control enters",
                      self.impact["Impact Tremors"]["oracle_text"])
        self.assertIn("instant or sorcery spell",self.veyran["Veyran, Voice of Duality"]["oracle_text"])

    def test_familiar_adds_one_colorless_per_cast_not_red(self):
        self.assertEqual(ignus_cycle(n=5, familiar=True), (1, 5, 5, 0))
        self.assertEqual(ignus_cycle(n=5, familiar=False), (1, 0, 5, 0))
        self.assertEqual(ignus_cycle(n=5, familiar=True, tremors=True), (1, 5, 5, 15))
        self.assertEqual(ignus_cycle(n=5, familiar=False, tremors=True), (1, 0, 5, 15))
        # Veyran does not double Birgi on creature Ignus casts and
        # does not double creature-ETB Impact Tremors triggers.

    def test_rule_of_law_and_spot_removal_bound_ignus_loop(self):
        self.assertEqual(ignus_cycle(n=10, familiar=True, tremors=True, rule_of_law=True),
                         (1, 1, 1, 3))
        self.assertEqual(ignus_cycle(n=10, familiar=True, tremors=True,
                                     removal_after_first=True), (1, 1, 1, 3))
        self.assertTrue(any("Spot removal" in r["name"] for r in self.report["adversarial_cases"]))
        self.assertTrue(any("Rule of Law" in r["name"] for r in self.report["adversarial_cases"]))

    def test_neheb_assault_loyal_counterplay_and_payability(self):
        o = self.oracle
        self.assertIn("each of your postcombat main phases",
                      o["Neheb, the Eternal"]["oracle_text"])
        self.assertIn("Activate only as a sorcery",o["Aggravated Assault"]["oracle_text"])
        self.assertIn("beginning of combat on your turn",o["Loyal Subordinate"]["oracle_text"])
        loss = 0
        for nth_combat in range(1, 5):
            loss += 3 * 3  # Loyal with commander: three players each lose three
            mana_this_postcombat_main = loss  # Neheb starts a NEW phase
            self.assertGreaterEqual(mana_this_postcombat_main,5)
            # Assault is an activated ability; {3}{R}{R} is payable.
            self.assertEqual(mana_this_postcombat_main-5,9*nth_combat-5)
        self.assertEqual(loss,36)
        self.assertTrue(self.report["canonical_approved_locked_unchanged"])

    def test_complete_physical_variants_source_legal_unapproved(self):
        report = self.report
        raw, base = physical_100(CANON)
        self.assertEqual(hashlib.sha256(raw).hexdigest(),
                         report["canonical"]["raw_sha256"])
        self.assertEqual(report["status"],"RESEARCH_ONLY_NEW_MATERIAL_INCUMBENT_SYNERGY")
        self.assertFalse(report["owner_ready"])
        self.assertFalse(report["m6_changed_candidate_certified"])
        self.assertTrue(report["deck3_hold"])
        self.assertEqual(len(report["full_100_research_alternatives"]),3)
        for trial in report["full_100_research_alternatives"]:
            after_raw,after = physical_100(ROOT / trial["path"])
            self.assertEqual(hashlib.sha256(after_raw).hexdigest(), trial["raw_sha256"])
            self.assertEqual(sorted((after-base).elements()),sorted(trial["adds"]))
            self.assertEqual(sorted((base-after).elements()),sorted(trial["cuts"]))
            self.assertEqual(sum(after.values()),100)
            self.assertLess(trial["swaps"],5)
            for name in after:
                source = self.oracle.get(name) or self.impact.get(name) or self.veyran.get(name)
                self.assertIsNotNone(source,name)
                self.assertEqual(source["commander_legality"],"legal",name)
                self.assertTrue(set(source["color_identity"]) <= set("UBR"),name)
            for required in ["Nightscape Familiar","Aggravated Assault","Neheb, the Eternal",
                             "Loyal Subordinate","Call Forth the Tempest","Pact of Negation",
                             "Pyroblast"]:
                if trial["name"] != "EXISTING_STAGE9_VEYRAN_IMPACT_PRESERVE_RUINOUS_LOSE_FAMILIAR":
                    self.assertIn(required,after)
            self.assertEqual(after["Island"],3)
            self.assertEqual(after["Swamp"],3)
            self.assertEqual(after["Mountain"],3)


if __name__ == "__main__":
    unittest.main()
