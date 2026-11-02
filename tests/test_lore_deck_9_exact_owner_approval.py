"""The owner approved the exact historical Ugin #9 list, not a substitution."""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "data/lore_decks/owner_decisions/2026-11-02_cory_approved_lore_deck_9_ugin.json"
APPROVED_HASH = "94fe43d3b748ee3f49b265797d4384e6a5948d719796308e4ad620e66b0202a8"


class LoreDeck9OwnerApprovalTests(unittest.TestCase):
    def test_exact_100_card_historical_list_and_rule_zero(self):
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        self.assertEqual(receipt["source_sha256"], APPROVED_HASH)
        self.assertEqual(receipt["status"], "OWNER_APPROVED_EXACT_HISTORICAL_LIST")
        self.assertEqual(receipt["deck_number"], 9)
        self.assertEqual(receipt["cards_modified_in_approval"], 0)
        self.assertFalse(receipt["modern_commander_legality_certified"])
        source = ROOT / receipt["source_path"]
        raw = source.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), APPROVED_HASH)
        entries = [re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?", line)
                   for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertTrue(all(entries))
        self.assertEqual(sum(int(e.group(1)) for e in entries), 100)
        self.assertEqual(sum("[Commander]" in x for x in raw.decode("utf-8").splitlines()), 1)
        self.assertEqual(raw.decode("utf-8").splitlines()[0], "1x The Ur-Dragon [Commander]")
        self.assertIn("1x Emrakul, the Aeons Torn\n", raw.decode("utf-8"))
        self.assertIn("Emrakul, the Aeons Torn", receipt["rule_zero_exceptions"])

    def test_index_and_original_evidence_present(self):
        index = (ROOT / "docs/LORE_DECK_APPROVAL_INDEX.md").read_text(encoding="utf-8")
        self.assertIn("| 9 | Ugin's Complete Life Story", index)
        for p in ("ugin_complete_life_story_proposal.json",
                  "ugin_complete_life_story_proposal.md",
                  "ugin_complete_life_story_printing_evidence.json",
                  "ugin_complete_life_story_decklist.txt"):
            self.assertTrue((ROOT / "data/lore_decks/drafts" / p).is_file(), p)


if __name__ == "__main__":
    unittest.main()
