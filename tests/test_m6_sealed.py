"""K sealing: adversarial field-blinding and fail-closed schema invariants."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_m6_sealed as sealed
import grixis_authority as ga


def fixture():
    return {
        "slug": "sample", "deck_id": "Sample", "list_hash": "lh1:" + "a" * 64,
        "candidates": [{"card": "Test Addition", "full_review": True,
                        "review": {"swap": "swap:sample:1",
                                   "blueprint": {"fit": "strong", "named_by": [], "anti_goal": False},
                                   "a_f_evidence": {"hypotheses": []},
                                   "edhrec": 123}}],
        "swaps": [{"id": "swap:sample:1", "cuts": ["Test Cut"], "adds": ["Test Addition"],
                   "tests": ["test:sample:1"], "blueprint": {"identity": "A"}}],
        "tests": [{"id": "test:sample:1", "verdict": "pass", "other": "canary"}],
        "tournament": {"sensitive": "A"},
    }


class TestSealedFirstPasses(unittest.TestCase):
    def test_commander_projection_is_blind_to_test_data(self):
        original = fixture()
        changed = copy.deepcopy(original)
        changed["tests"][0]["verdict"] = "fail"
        changed["tournament"] = {"sensitive": "B"}
        changed["candidates"][0]["review"]["edhrec"] = 999999
        self.assertEqual(sealed.project_a(original), sealed.project_a(changed))
        self.assertEqual(sealed.pass_output("A", original), sealed.pass_output("A", changed))

    def test_performance_projection_is_blind_to_identity(self):
        original = fixture()
        changed = copy.deepcopy(original)
        changed["candidates"][0]["review"]["blueprint"]["anti_goal"] = True
        changed["candidates"][0]["review"]["blueprint"]["fit"] = "weak"
        changed["swaps"][0]["blueprint"]["identity"] = "B"
        self.assertEqual(sealed.project_b(original), sealed.project_b(changed))
        self.assertEqual(sealed.pass_output("B", original), sealed.pass_output("B", changed))

    def test_objective_functions_not_same(self):
        a, b = sealed.pass_output("A", fixture())["pass"], sealed.pass_output("B", fixture())["pass"]
        self.assertNotEqual(a["objective_function"]["family"], b["objective_function"]["family"])
        self.assertNotEqual(a["objective_function"]["formula_sha256"], b["objective_function"]["formula_sha256"])
        self.assertFalse(ga.check_reconciliation(a, b))

    def test_manifest_cannot_self_accept_critic(self):
        obj = {
            "schema_version": 1, "stage": "M6_A_B_commit_then_reveal",
            "pass_a_commit": "a" * 40, "pass_b_commit": "b" * 40,
            "passes": [{"deck_id": "Sample", "slug": "sample", "list_hash": "lh1:" + "a" * 64,
                        "a_sha256": "sha256:" + "a" * 64, "b_sha256": "sha256:" + "b" * 64,
                        "agreements": 0, "disagreements": 0, "deep_review": 0}] * 62,
            "counts": {"decks": 62, "agreements": 0, "disagreements": 0, "deep_review": 0},
            "pass_c": {"complete": False, "status": "awaiting_named_critic",
                       "model_limited_positive_tests_decisive": False},
            "authority": sealed.AUTHORITY,
        }
        self.assertFalse(ga.validate_file(obj, "m6_sealed_reconciliation.schema.json"))
        obj["pass_c"]["complete"] = True
        self.assertTrue(ga.validate_file(obj, "m6_sealed_reconciliation.schema.json"))


if __name__ == "__main__":
    unittest.main()
