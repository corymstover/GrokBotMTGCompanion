"""Permanent 97-card Abaddon Oracle source snapshot integrity.

The source is the exact CI Scryfall lookup as of its own timestamp.
It does not invent independent review, current-future legality or ownership.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list
from scripts.grixis_m7_abaddon_live_oracle import parse_approved_raw

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Scryfall_20261022.json"
BASE = ROOT / "data/grixis/m7/authority_snapshots/Abaddon_the_Despoiler_Approved_2026-10-13.txt"
CHOSEN = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt"
BASE_SHA = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
CHOSEN_SHA = "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd"
BASE_LH = "lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793"
CHOSEN_LH = "lh1:4bb15eb5acc051871e7d818890f71705eb74f1281e933e73b0e77ff770be1efc"


def logical_hash(cards, evidence):
    entries = Counter(("commander" if i == 0 else "main", evidence[name]["oracle_id"])
                      for i, name in enumerate(cards))
    encoded = "".join(f"{zone}|{oracle}|{n}\n" for (zone, oracle), n in sorted(entries.items()))
    return "lh1:" + hashlib.sha256(encoded.encode("utf-8")).hexdigest()


class AbaddonSavedOracleEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = json.loads(SNAP.read_text(encoding="utf-8"))
        cls.cards = cls.s["oracle_snapshot"]

    def test_all_97_named_current_oracle_text_identity_and_legality(self):
        s, cards = self.s, self.cards
        self.assertEqual(s["card_identity_count"], len(cards))
        self.assertEqual(len(cards), 97)
        self.assertEqual(s["scryfall_endpoint"], "https://api.scryfall.com/cards/collection")
        ts = datetime.fromisoformat(s["checked_at_utc"])
        self.assertEqual(ts.date().isoformat(), "2026-10-22")
        self.assertIsNotNone(ts.tzinfo)
        self.assertLess(ts.astimezone(timezone.utc), datetime.now(timezone.utc))
        for name, obj in cards.items():
            self.assertTrue(name.strip())
            self.assertEqual(obj["commander_legality"], "legal")
            self.assertTrue(set(obj["color_identity"]) <= {"U", "B", "R"})
            self.assertTrue(obj["oracle_id"] and obj["oracle_text"])
            self.assertEqual(hashlib.sha256(obj["oracle_text"].encode("utf-8")).hexdigest(),
                             obj["oracle_text_sha256"])
            self.assertTrue(obj["scryfall_uri"].startswith("https://scryfall.com/"))

    def test_both_exact_physical_100_lists_bound_to_oracle_identifiers(self):
        s = self.s
        base, commanders = parse_approved_raw(BASE.read_bytes())
        chosen, cand_commanders, companions = parse_list(CHOSEN)
        self.assertEqual(commanders, ["Abaddon the Despoiler"])
        self.assertEqual(cand_commanders, commanders)
        self.assertFalse(companions)
        self.assertEqual(len(base), len(chosen))
        self.assertEqual(len(chosen), 100)
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(hashlib.sha256(CHOSEN.read_bytes()).hexdigest(), CHOSEN_SHA)
        self.assertEqual(s["approved_canonical_raw_sha256"], BASE_SHA)
        self.assertEqual(s["chosen_research_candidate_raw_sha256"], CHOSEN_SHA)
        self.assertTrue(set(base + chosen) <= set(self.cards))
        self.assertEqual(logical_hash(base, self.cards), BASE_LH)
        self.assertEqual(logical_hash(chosen, self.cards), CHOSEN_LH)
        self.assertEqual(s["baseline_logical_hash"], BASE_LH)
        self.assertEqual(s["chosen_research_candidate_logical_hash"], CHOSEN_LH)

    def test_exact_source_provenance_and_never_owner_approval(self):
        s = self.s
        p = s["archival_provenance"]
        self.assertEqual(p["source_pr"], 570)
        self.assertEqual(p["exact_head"], "fd143871f84b21ccb03ff8714f5a3df597bd83f1")
        self.assertIn("39822223496", p["github_actions_run"])
        self.assertEqual(s["capture_raw_sha256"], p["source_original_raw_sha256"])
        self.assertEqual(s["canonical_authority_mode"],
                         "SHA_PINNED_CANONICAL_BYTES_NOT_LIVE_CROSS_REPO_READ")
        self.assertFalse(s["owner_m7_approval"])
        self.assertFalse(s["formal_m6_certificate"])
        self.assertFalse(s["reviewer_independent"])
        self.assertFalse(s["locked_canonical_mutated"])
        self.assertEqual(s["official_commander_exceptions_for_abaddon"], [])


if __name__ == "__main__":
    unittest.main()
