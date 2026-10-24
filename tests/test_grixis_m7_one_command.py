"""One-command intake must reuse evidence without pretending to finalize."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.grixis_m7_one_command import (
    IntakeError, build_packet, choose, classify_grok_files,
    plan_inventory, quantity_check, render_brief,
)


class OneCommandDeckIntakeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ids = [f"Deck_{i:02d}" for i in range(1, 63)]
        cls.ids[24] = "Kefka__Court_Mage"
        cls.registry = {"decks": {id: {"approved_list_artifact":
                     (f"refinement/decklists/{id}_M7_Approved.txt" if i < 24
                      else f"refinement/decklists/{id}_Approved.txt")}
                     for i, id in enumerate(cls.ids)}}
        cls.raw = ("1x Kefka, Court Mage // Kefka, Ruler of Ruin [Commander]\n" +
                   "".join(f"1x Unique Card {i}\n" for i in range(99))).encode()
        cls.sha = hashlib.sha256(cls.raw).hexdigest()
        cls.registry["decks"]["Kefka__Court_Mage"]["approved_list_sha256"] = cls.sha
        cls.plan = {"plan": "data/grixis/m6/test_blueprints/Kefka__Court_Mage.json",
                    "P0": ["C1", "K1", "K2", "K3", "F1"],
                    "P1": ["K4", "K5", "E1", "E2", "W1", "W2", "W3", "F2", "F3"],
                    "designed_not_executed": True}

    def packet(self, raw=None, head="a"*40):
        return build_packet(
            registry=self.registry, deck_id="Kefka__Court_Mage", order=25,
            canonical_sha="b"*40, raw_deck=self.raw if raw is None else raw,
            plan=self.plan, grok_pr=673, grok_head=head,
            grok_changed_files=[
                {"filename": "data/grixis/m6/ij/certificates/kefka-court-mage-m7.json"},
                {"filename": "tests/test_m6_kefka_court_mage_m7_mechanics.py"},
                {"filename": "tests/test_m6_kefka_court_mage_m7_ij.py"},
                {"filename": "data/grixis/m7/decision_reviews/Kefka__Court_Mage.json"},
            ])

    def test_next_deck_is_first_without_new_m7(self):
        self.assertEqual(("Kefka__Court_Mage", 25), choose(self.registry, "next"))

    def test_numerical_or_exact_deck_selection(self):
        self.assertEqual(("Kefka__Court_Mage", 25), choose(self.registry, "#25"))
        self.assertEqual(("Kefka__Court_Mage", 25), choose(self.registry, "Kefka__Court_Mage"))

    def test_bad_deck_does_not_fall_back_to_guess(self):
        with self.assertRaisesRegex(IntakeError, "Not a canonical deck ID"):
            choose(self.registry, "Kefka guessed")

    def test_source_is_exact_100(self):
        self.assertEqual(100, quantity_check(self.raw)["physical_commander_deck_cards"])

    def test_bad_99_rejected(self):
        with self.assertRaisesRegex(IntakeError, "99 cards"):
            quantity_check(self.raw.replace(b"1x Unique Card 98\n", b""))

    def test_sha_mismatch_fail_closed(self):
        with self.assertRaisesRegex(IntakeError, "do not match approved raw SHA"):
            self.packet(raw=self.raw.replace(b"Unique Card 1", b"Changed Card 1"))

    def test_grok_ij_is_prior_scope_not_final_pass(self):
        p = self.packet()
        self.assertEqual("RESEARCH_INTAKE_ONLY_NOT_OWNER_READY", p["status"])
        self.assertEqual(1, len(p["grok_original"]["scoped_ij_receipts"]))
        self.assertEqual(2, len(p["grok_original"]["mechanics_test_files"]))
        self.assertTrue(p["grok_original"]["old_evidence_is_not_final_candidate_certification"])

    def test_not_fetched_grok_is_not_fabricated_pass(self):
        p = self.packet(head=None)
        self.assertEqual("FIRST_PASS_NOT_FETCHED_OR_NOT_AVAILABLE", p["grok_original"]["status"])
        self.assertFalse(p["grok_original"]["available"])

    def test_invalid_head_fails(self):
        with self.assertRaisesRegex(IntakeError, "Unpinned Grok"):
            self.packet(head="oops")

    def test_legacy_case_schema_supported(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            p = root / "data/grixis/m6/test_blueprints/Kefka__Court_Mage.json"
            p.parent.mkdir(parents=True)
            p.write_text(json.dumps({"deck_id": "Kefka__Court_Mage", "cases": [
                {"id": "C1", "priority": "P0"},
                {"id": "K4", "priority": "P1"},
            ]}))
            plan = plan_inventory(root, "Kefka__Court_Mage")
            self.assertEqual(["C1"], plan["P0"])
            self.assertEqual(["K4"], plan["P1"])
            self.assertTrue(plan["designed_not_executed"])

    def test_pinned_remote_blueprint_is_inventory_only(self):
        blueprint = json.dumps({"deck_id": "Kefka__Court_Mage", "cases": [
            {"id": "C1", "priority": "P0", "status": "DESIGN_ONLY_UNIMPLEMENTED_NOT_RUN"},
            {"id": "K1", "priority": "P1", "status": "DESIGN_ONLY_UNIMPLEMENTED_NOT_RUN"},
        ]}).encode()
        with tempfile.TemporaryDirectory() as temp:
            p = plan_inventory(Path(temp), "Kefka__Court_Mage", source=blueprint,
                               pinned_ref="f"*40)
        self.assertEqual("f"*40, p["pinned_source_commit"])
        self.assertTrue(p["designed_not_executed"])
        self.assertEqual(["C1"], p["P0"])

    def test_wrong_remote_blueprint_identity_fails_closed(self):
        raw = json.dumps({"deck_id": "Kess__Dissident_Mage", "cases": []}).encode()
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(IntakeError, "does not match requested deck"):
                plan_inventory(Path(temp), "Kefka__Court_Mage", source=raw,
                               pinned_ref="f"*40)

    def test_missing_blueprint_is_not_silent(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(IntakeError, "Missing M6"):
                plan_inventory(Path(temp), "Kefka__Court_Mage")

    def test_user_brief_has_exact_sha_and_honest_status(self):
        brief = render_brief(self.packet())
        self.assertIn(self.sha, brief)
        self.assertIn("not owner-ready", brief)
        self.assertIn("5 P0, 9 P1", brief)


if __name__ == "__main__":
    unittest.main()
