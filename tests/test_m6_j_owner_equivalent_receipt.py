"""M6 J reviewer provenance: owner's 62/62 non-independent Pass C waiver, fail closed.

These tests do NOT generate or certify any final J bundles. They exercise only
the review-provenance subgate and preserve separate Phase B/I/J requirements.
"""
import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch
from scripts import grixis_m6_bundle_check as bc

ROOT = Path(__file__).resolve().parents[1]
WAIVER = "data/grixis/m6/governance/pass_c_owner_waiver_20261021.json"
PROGRESS = "data/grixis/m6/owner_pass_c_substitute/progress.json"
REVIEW = "data/grixis/m6/owner_pass_c_substitute/Abaddon_the_Despoiler/final_disposition.md"
SEAL = "data/grixis/m6/owner_pass_c_substitute/Abaddon_the_Despoiler/seal.json"


def record():
    return {
        "reviewer": "ChatGPT/OpenAI GPT-6",
        "judgment_receipt_path": REVIEW,
        "judgment_receipt_sha256": bc.content_hash(REVIEW),
        "conflicts_resolved": True,  # prospective J-bundle claim, not a current M6 gate
        "review_class": "FORMAL_PASS_C_OWNER_EQUIVALENT",
        "technically_independent": False,
        "waiver_receipt_path": WAIVER,
        "waiver_receipt_sha256": bc.content_hash(WAIVER),
        "progress_receipt_path": PROGRESS,
        "progress_receipt_sha256": bc.content_hash(PROGRESS),
        "stage_a_seal_path": SEAL,
        "stage_a_seal_sha256": bc.content_hash(SEAL),
    }


class M6JOwnerEquivalentReceiptTests(unittest.TestCase):
    def test_actual_sealed_abaddon_owner_equivalent_receipt_passes_provenance_only(self):
        self.assertTrue(bc.validate_pass_c(record(), "Abaddon_the_Despoiler"))
        from scripts import grixis_m6_bundle_check as b
        self.assertEqual(b.check(), 0)  # No final reproducibility bundles yet

    def test_bad_digest_and_wrong_deck_fail_closed(self):
        changed = record()
        changed["judgment_receipt_sha256"] = "sha256:" + "0"*64
        with self.assertRaises(ValueError):
            bc.validate_pass_c(changed, "Abaddon_the_Despoiler")
        with self.assertRaises(ValueError):
            bc.validate_pass_c(record(), "Anhelo__the_Painter")

    def test_technical_independence_claim_is_rejected(self):
        invalid = record()
        invalid["technically_independent"] = True
        with self.assertRaises(ValueError):
            bc.validate_pass_c(invalid, "Abaddon_the_Despoiler")
        invalid = record()
        invalid["reviewer"] = "independent GrokBot"
        with self.assertRaises(ValueError):
            bc.validate_pass_c(invalid, "Abaddon_the_Despoiler")

    def test_wrong_waiver_or_seal_path_is_rejected(self):
        for key, replacement in (("waiver_receipt_path", PROGRESS),
                                 ("progress_receipt_path", WAIVER),
                                 ("stage_a_seal_path", REVIEW),
                                 ("judgment_receipt_path", SEAL)):
            with self.subTest(key=key):
                invalid = record()
                invalid[key] = replacement
                with self.assertRaises(ValueError):
                    bc.validate_pass_c(invalid, "Abaddon_the_Despoiler")

    def test_tampered_waiver_and_progress_fail_even_with_local_digest(self):
        original = bc.load
        for source, mutation in (
            (WAIVER, lambda x: x["scope_and_effect"].update({"other_m6_gates_remain_independently_required": False})),
            (PROGRESS, lambda x: x.update({"technically_independent": True})),
            (PROGRESS, lambda x: x["decks"][0].update({"owner_swap_approved": True})),
            (SEAL, lambda x: x.update({"technically_independent": True})),
        ):
            with self.subTest(source=source, mutation=mutation):
                def compromised(path):
                    data = original(path)
                    if str(path) == str(bc.safe_repo_file(source)):
                        data = copy.deepcopy(data)
                        mutation(data)
                    return data
                with patch.object(bc, "load", side_effect=compromised):
                    with self.assertRaises(ValueError):
                        bc.validate_pass_c(record(), "Abaddon_the_Despoiler")

    def test_legacy_independent_reviewer_path_keeps_old_requirements(self):
        prior = {"reviewer": "Independent critic",
                 "judgment_receipt_path": REVIEW,
                 "judgment_receipt_sha256": bc.content_hash(REVIEW)}
        with patch.object(bc, "load", return_value={
                "reviewer": "Independent critic",
                "status": "critical_review_complete",
                "can_approve_or_lock": False}):
            self.assertTrue(bc.validate_pass_c(prior, "Abaddon_the_Despoiler"))
        with patch.object(bc, "load", return_value={
                "reviewer": "Independent critic",
                "status": "awaiting_review",
                "can_approve_or_lock": False}):
            with self.assertRaises(ValueError):
                bc.validate_pass_c(prior, "Abaddon_the_Despoiler")

    def test_schema_owner_branch_requires_explicit_waiver_metadata(self):
        import jsonschema
        schema = json.loads((ROOT / "data/grixis/schemas/m6_reproducibility_bundle.schema.json").read_text())
        component = schema["properties"]["pass_c"]
        resolver = jsonschema.RefResolver.from_schema(schema, store={
            "https://github.com/corymstover/GrokBotMTGCompanion/data/grixis/schemas/common.schema.json":
                json.loads((ROOT / "data/grixis/schemas/common.schema.json").read_text())
        })
        validator = jsonschema.Draft202012Validator(component, resolver=resolver)
        self.assertEqual(list(validator.iter_errors(record())), [])
        without_waiver = record()
        without_waiver.pop("waiver_receipt_sha256")
        self.assertNotEqual(list(validator.iter_errors(without_waiver)), [])
        fake_independent = record()
        fake_independent["technically_independent"] = True
        self.assertNotEqual(list(validator.iter_errors(fake_independent)), [])


if __name__ == "__main__":
    unittest.main()
