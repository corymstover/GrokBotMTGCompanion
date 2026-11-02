"""Only Cory's exact post-draft SHA-256 decisions can close K112–K114."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pilot_owner_approvals as A  # noqa: E402


class LorePilotExactOwnerApprovalTests(unittest.TestCase):
    def test_three_owner_approved_exact_hashes_with_original_drafts_unchanged(self):
        r = A.check()
        self.assertEqual(r["checklist_ids"], ["K112", "K113", "K114"])
        self.assertEqual(r["cards_per_pilot"], 100)
        self.assertFalse(r["current_rules_or_power_certified"])
        self.assertEqual(r["source_sha256"], {k: v[3] for k, v in A.EXPECTED.items()})

    def test_owner_hash_cannot_be_substituted_by_updating_registry_alone(self):
        d = json.loads(A.RECORD.read_text(encoding="utf-8"))
        d["pilots"][0]["raw_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "forged.json"
            path.write_text(json.dumps(d), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "owner's exact hash"):
                A.check(record=path)

    def test_future_revision_is_not_automatically_approved(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "changed.txt"
            original = (ROOT / "data/lore_decks/drafts/ugin_bolas_elder_dragon_duality_decklist.txt").read_bytes()
            path.write_bytes(original.replace(b"1x Sol Ring", b"1x Arcane Signet", 1))
            with self.assertRaisesRegex(ValueError, "exact owner-approved decklist bytes changed"):
                A.check(deck_overrides={"K112": path})

    def test_approval_does_not_certify_current_rules_or_future_revisions(self):
        d = json.loads(A.RECORD.read_text(encoding="utf-8"))
        d["current_legality_or_bracket_certified"] = True
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "overclaim.json"
            path.write_text(json.dumps(d), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "bounded exact historical approval"):
                A.check(record=path)


if __name__ == "__main__":
    unittest.main()
