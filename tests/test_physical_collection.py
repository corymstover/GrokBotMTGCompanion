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


if __name__ == "__main__":
    unittest.main()
