import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_commander_name_equivalences as checker


class EquivalentCommanderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = checker.load(checker.ALIASES)
        cls.registry = checker.load(checker.REGISTRY)

    def test_all_62_reconcile_uniquely(self):
        mapped = checker.reconcile(self.data, self.registry)
        self.assertEqual(len(mapped), 62)
        self.assertEqual(len(set(mapped.values())), 62)
        self.assertEqual(
            mapped["Goben__Gene_Splice_Savant"],
            "Norman_Osborn_Green_Goblin",
        )

    def test_approved_hash_is_unchanged(self):
        record = self.data["interchangeable_names"][0]
        self.assertEqual(
            self.registry["decks"][record["engineering_deck_id"]]["source"]["recorded_sha256"],
            record["original_card_approved_list_sha256"],
        )
        self.assertEqual(self.data["certification_claims"]["approved_card_swaps"], 0)

    def test_wrong_hash_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["interchangeable_names"][0]["original_card_approved_list_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            checker.reconcile(data, self.registry)

    def test_duplicate_roster_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["canonical_deck_ids"].append("Goben__Gene_Splice_Savant")
        with self.assertRaises(ValueError):
            checker.reconcile(data, self.registry)

    def test_false_milestone_claim_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["certification_claims"]["full_m8_certification"] = True
        with self.assertRaises(ValueError):
            checker.reconcile(data, self.registry)

    def test_false_project_exception_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["interchangeable_names"][0]["rules_status"] = "project_exception"
        with self.assertRaises(ValueError):
            checker.reconcile(data, self.registry)


if __name__ == "__main__":
    unittest.main()
