"""Regression tests for Cory's immutable 2026-11-08 ownership snapshot."""

import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("physical_audit", ROOT / "scripts" / "audit_physical_collection.py")
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class PhysicalCollectionSnapshotTests(unittest.TestCase):
    def test_reconciled_immutable_snapshot(self):
        with redirect_stdout(io.StringIO()):
            audit.main(write=False)

    def test_reserved_staples_and_source_deck_sizes(self):
        master = audit.parse_counts(audit.MASTER.read_bytes(), "master")
        with ZipFile(audit.ARCHIVE) as archive:
            decks = {name: audit.parse_counts(archive.read(name), name)
                     for name in audit.DECKS}
        reserved = decks["Xander_EDH_IRL.csv"] + decks["Dihada_EDH_IRL.csv"]
        for card in ("Sol Ring", "Arcane Signet", "Command Tower"):
            self.assertEqual(master[card], 2)
            self.assertEqual(reserved[card], 2)
        self.assertEqual(sum(decks["Xander_EDH_IRL.csv"].values()), 101)
        self.assertEqual(sum(decks["Dihada_EDH_IRL.csv"].values()), 100)
        self.assertEqual(sum(decks["Stefanie_Jund_Prerelease.csv"].values()), 43)

    def test_owner_confirmed_teardown_is_current(self):
        import json
        state = json.loads(audit.CURRENT_STATUS.read_text(encoding="utf-8"))
        self.assertEqual(len(state["built_decks"]), 2)
        self.assertEqual(len(state["disassembled_decks"]), 4)
        self.assertEqual(state["available_cards"], 1131)
        self.assertEqual(state["available_distinct_names"], 621)
        self.assertEqual(state["active_built_decklists"]["Xander_EDH_IRL.csv"],
                         "data/physical_collection/current_decks/Xander_EDH_IRL.csv")
        with redirect_stdout(io.StringIO()):
            audit.main(write=False)

    def test_confirmed_20_swaps_release_removed_cards_and_preserve_dihada(self):
        import json
        event = json.loads(audit.XANDER_REBUILD.read_text(encoding="utf-8"))
        original = audit.parse_counts((audit.SNAPSHOT / "decks/Xander_EDH_IRL.csv").read_bytes(), "old")
        active = audit.parse_counts(audit.CURRENT_XANDER.read_bytes(), "current")
        dihada = audit.parse_counts((audit.SNAPSHOT / "decks/Dihada_EDH_IRL.csv").read_bytes(), "Dihada")
        master = audit.parse_counts(audit.MASTER.read_bytes(), "master")
        available = audit.parse_counts(audit.CURRENT_POOL.read_bytes(), "free")
        self.assertEqual(len(event["swaps"]), 20)
        self.assertEqual(sum(active.values()), 101)
        self.assertEqual(active["Lutri, the Spellchaser"], 1)
        self.assertEqual(active["Swamp"], 8)
        self.assertEqual(active["The Unicomplex"], 1)
        self.assertEqual(active + dihada + available, master)
        self.assertEqual(len(available), 621)
        for item in event["swaps"]:
            removed, added = item["out"], item["in"]
            # Every removed Xander copy is available again, while the newly
            # reserved replacement is unavailable except for extra owned copies.
            self.assertEqual(available[removed], master[removed] - dihada[removed] - active[removed])
            self.assertEqual(available[added], master[added] - dihada[added] - active[added])
            self.assertGreaterEqual(original[removed], 1)


if __name__ == "__main__":
    unittest.main()
