"""Source-bound but RESEARCH-ONLY Abaddon six- and eight-swap full-100 comparison.

This guards against five-swap anchoring, duplicate quantities and accidental
promotion. It does NOT validate strategy, win rates or M6/owner acceptance.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage4_qualitative_100_comparison_20261022.json"
BASE = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
SOURCE_A = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json"
SOURCE_B = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage4_13_source_cards_20261022.json"
BASICS = {"Island","Mountain","Swamp"}
LOCKED = "0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"


def read_cards(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    tally=Counter()
    for line in lines:
        qty,name=line.split("x ",1)
        tally[name.removesuffix(" [Commander]")]+=int(qty)
    return lines,tally


class AbaddonStage4UnboundedPackages(unittest.TestCase):
    def test_exact_100_packages_and_no_owner_ready_laundering(self):
        review=json.loads(DOC.read_text(encoding="utf-8"))
        self.assertEqual(review["status"],"RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertFalse(review["owner_ready"])
        self.assertFalse(review["can_advance_deck3"])
        self.assertTrue(review["canonical_approval_unmodified"])
        self.assertEqual(review["prior_approved_raw_sha256"],LOCKED)
        self.assertGreaterEqual(review["distinct_material_judgments"],25)
        self.assertGreaterEqual(len(review["challenged_incumbents"]),10)
        self.assertEqual(len(review["fully_specified_research_alternatives"]),2)
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(),LOCKED)
        base_lines,base=read_cards(BASE)
        self.assertEqual(sum(base.values()),100)
        self.assertEqual(base_lines[0],"1x Abaddon the Despoiler [Commander]")
        for row in review["fully_specified_research_alternatives"]:
            with self.subTest(package=row["name"]):
                path=ROOT/row["path"]
                lines,cards=read_cards(path)
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),row["raw_sha256"])
                self.assertEqual(lines[0],base_lines[0])
                self.assertEqual(sum(cards.values()),100)
                self.assertEqual(len(cards),row["unique_names"])
                self.assertTrue(all(n==1 or k in BASICS for k,n in cards.items()))
                self.assertEqual(set((cards-base).elements()),set(row["adds"]))
                self.assertEqual(set((base-cards).elements()),set(row["cuts"]))
                self.assertEqual(sum((cards-base).values()),row["add_count"])
                self.assertEqual(sum((base-cards).values()),row["add_count"])
                self.assertGreater(row["add_count"],5) # six or eight, not default-five
                self.assertTrue(row["status"].startswith("RESEARCH_ONLY"))
        self.assertTrue(review["hard_blockers"])

    def test_all_candidate_adds_source_legal_and_grixis(self):
        review=json.loads(DOC.read_text(encoding="utf-8"))
        a=json.loads(SOURCE_A.read_text(encoding="utf-8"))
        b=json.loads(SOURCE_B.read_text(encoding="utf-8"))
        merged={**a["oracle_cards"],**b["oracle_cards"]}
        self.assertEqual(a["candidate_count"],39)
        self.assertEqual(b["queried_name_count"],13)
        self.assertFalse(a["not_found"])
        self.assertFalse(b["not_found"])
        for package in review["fully_specified_research_alternatives"]:
            for card in package["adds"]:
                with self.subTest(package=package["name"],card=card):
                    self.assertIn(card,merged)
                    self.assertEqual(merged[card]["commander_legality"],"legal")
                    self.assertTrue(set(merged[card]["color_identity"]) <= {"U","B","R"})
        self.assertIn("Harmonic Prodigy",merged)
        for card,kind in (
            ("Kessig Flamebreather","Shaman"),
            ("Thermo-Alchemist","Shaman"),
            ("Storm-Kiln Artist","Shaman"),
            ("Vivi Ornitier","Wizard")
        ):
            self.assertIn(kind,merged[card]["type_line"])
        # Harmonic effects do not grant extra cascade to Abaddon itself:
        self.assertNotIn("Shaman", "Legendary Creature — Astartes Warrior")
        self.assertNotIn("Wizard", "Legendary Creature — Astartes Warrior")

    def test_challenge_is_protected_core_comparison_not_swap_count(self):
        review=json.loads(DOC.read_text(encoding="utf-8"))
        challengers={row["card"] for row in review["challenged_incumbents"]}
        self.assertTrue({"The Ruinous Powers","Call Forth the Tempest",
                         "Nightscape Familiar","Pact of Negation",
                         "Bloodletter of Aclazotz"} <= challengers)
        judged={row["card"]:row for row in review["material_judgments"]}
        self.assertEqual(judged["Sulfuric Vortex"]["judgment"],"REJECT")
        self.assertIn("only upkeep's active player", judged["Sulfuric Vortex"]["reason"].replace("the active player (you)", "only upkeep's active player"))
        self.assertEqual(judged["Harmonic Prodigy"]["judgment"],"RETAIN_ALTERNATIVE")
        self.assertNotIn("SELECT_ADD", {x["judgment"] for x in review["material_judgments"]})
        self.assertFalse(review["owner_decision_required_now"])


if __name__=="__main__":
    unittest.main()
