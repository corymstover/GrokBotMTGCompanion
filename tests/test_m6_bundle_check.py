"""Final-bundle gate: missing evidence, unsafe paths, and schema tampering fail closed."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_m6_bundle_check as bc
import grixis_authority as ga


class TestM6FinalBundle(unittest.TestCase):
    def test_no_bundle_can_be_silently_approved(self):
        self.assertIn(bc.check(), range(63))

    def test_invalid_empty_bundle(self):
        self.assertTrue(ga.validate_file({}, "m6_reproducibility_bundle.schema.json"))

    def test_missing_future_evidence_is_hard_failure(self):
        with self.assertRaises(ValueError):
            bc.safe_repo_file("data/grixis/m6/bundles/definitely-not-a-real-receipt.json")

    def test_path_escape_forbidden(self):
        for path in ("../../etc/passwd", "/etc/passwd"):
            with self.assertRaises(ValueError):
                bc.safe_repo_file(path)

    def test_model_overclaim_schema_guard(self):
        self.assertTrue(ga.validate_file({
            "schema_version": 1,
            "stage": "M6_final_reproducibility_bundle",
            "bundle_status": "approved",  # forbidden even if a script claims it
            "authority": {"can_approve_or_lock": True}
        }, "m6_reproducibility_bundle.schema.json"))


    def test_preserved_admiral_explicit_nonindependent_pass_c_provenance(self):
        bundle = json.loads((ROOT / "data/grixis/m6/bundles/admiral-beckett-brass.json").read_text(encoding="utf-8"))
        self.assertTrue(bc.validate_pass_c(bundle["pass_c"], "Admiral_Beckett_Brass"))

    def test_fake_admiral_third_model_independence_is_still_rejected(self):
        bundle = json.loads((ROOT / "data/grixis/m6/bundles/admiral-beckett-brass.json").read_text(encoding="utf-8"))
        fraudulent = dict(bundle["pass_c"], technically_independent=True)
        with self.assertRaises(ValueError):
            bc.validate_pass_c(fraudulent, "Admiral_Beckett_Brass")


if __name__ == "__main__":
    unittest.main()
