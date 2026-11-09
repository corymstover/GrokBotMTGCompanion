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
        self.assertEqual(len(state["built_decks"]), 4)
        self.assertEqual(len(state["disassembled_decks"]), 4)
        self.assertEqual(state["available_cards"], 1011)
        self.assertEqual(state["available_distinct_names"], 599)
        self.assertEqual(state["active_built_decklists"]["Xander_EDH_IRL.csv"],
                         "data/physical_collection/current_decks/Xander_EDH_IRL.csv")
        self.assertEqual(state["active_built_decklists"]["Dihada_EDH_IRL.csv"],
                         "data/physical_collection/current_decks/Dihada_EDH_IRL.csv")
        self.assertEqual(state["active_built_decklists"]["Izzet_Pauper_IRL.csv"],
                         "data/physical_collection/current_decks/Izzet_Pauper_IRL.csv")
        self.assertEqual(state["active_built_decklists"]["Stefanie_MonoBlack_Pauper_IRL.csv"],
                         "data/physical_collection/current_decks/Stefanie_MonoBlack_Pauper_IRL.csv")
        with redirect_stdout(io.StringIO()):
            audit.main(write=False)

    def test_all_four_active_decks_preserve_ownership_and_release_swapped_cards(self):
        import json
        xander_event = json.loads(audit.XANDER_REBUILD.read_text(encoding="utf-8"))
        dihada_event = json.loads(audit.DIHADA_REBUILD.read_text(encoding="utf-8"))
        original_xander = audit.parse_counts((audit.SNAPSHOT / "decks/Xander_EDH_IRL.csv").read_bytes(), "old Xander")
        original_dihada = audit.parse_counts((audit.SNAPSHOT / "decks/Dihada_EDH_IRL.csv").read_bytes(), "old Dihada")
        active_xander = audit.parse_counts(audit.CURRENT_XANDER.read_bytes(), "current Xander")
        active_dihada = audit.parse_counts(audit.CURRENT_DIHADA.read_bytes(), "current Dihada")
        active_izzet = audit.parse_counts(audit.CURRENT_IZZET.read_bytes(), "current Izzet Pauper")
        active_stefanie_pauper = audit.parse_counts(audit.CURRENT_STEFANIE_PAUPER.read_bytes(),
                                                   "current Stefanie Pauper")
        master = audit.parse_counts(audit.MASTER.read_bytes(), "master")
        available = audit.parse_counts(audit.CURRENT_POOL.read_bytes(), "free")
        self.assertEqual(len(xander_event["swaps"]), 20)
        self.assertEqual(len(dihada_event["swaps"]), 15)
        self.assertEqual(sum(active_xander.values()), 101)
        self.assertEqual(sum(active_dihada.values()), 100)
        self.assertEqual(active_xander["Lutri, the Spellchaser"], 1)
        self.assertEqual(active_xander["Swamp"], 8)
        self.assertEqual(active_xander["The Unicomplex"], 1)
        self.assertEqual(active_dihada["Dihada, Binder of Wills"], 1)
        self.assertEqual(active_dihada["Swamp"], 4)
        self.assertEqual(active_dihada["Plains"], 7)
        self.assertEqual(active_dihada["Blood Crypt"], 1)
        self.assertEqual(audit.sha256(audit.CURRENT_DIHADA.read_bytes()),
                         dihada_event["current_deck_sha256"])
        self.assertEqual(active_xander + active_dihada + active_izzet + active_stefanie_pauper + available, master)
        self.assertEqual(sum(active_izzet.values()), 60)
        self.assertEqual(sum(active_stefanie_pauper.values()), 60)
        self.assertEqual(sum(available.values()), 1011)
        self.assertEqual(len(available), 599)
        for event, original in ((xander_event, original_xander),
                                (dihada_event, original_dihada)):
            for item in event["swaps"]:
                removed, added = item["out"], item["in"]
                self.assertEqual(available[removed],
                                 master[removed] - active_xander[removed]
                                 - active_dihada[removed] - active_izzet[removed]
                                 - active_stefanie_pauper[removed])
                self.assertEqual(available[added],
                                 master[added] - active_xander[added]
                                 - active_dihada[added] - active_izzet[added]
                                 - active_stefanie_pauper[added])
                self.assertGreaterEqual(original[removed], 1)

    def test_pauper_build_exactly_reserves_main_deck_without_a_sideboard(self):
        import json
        event = json.loads(audit.IZZET_BUILD.read_text(encoding="utf-8"))
        main = audit.parse_counts(audit.CURRENT_IZZET.read_bytes(), "current Pauper")
        self.assertEqual(event["sideboard"], [])
        self.assertEqual(event["sideboard_cards"], 0)
        self.assertEqual(main, {entry["name"]: entry["quantity"] for entry in event["main_deck"]})
        self.assertEqual(audit.sha256(audit.CURRENT_IZZET.read_bytes()), event["current_deck_sha256"])
        self.assertEqual(sum(main.values()), 60)
        self.assertEqual(len(main), 16)
        self.assertEqual(main["Andoria"], 4)
        self.assertEqual(main["Jace's Phantasm"], 4)
        self.assertEqual(main["Izzet Guildgate"], 1)

    def test_stefanie_confirmed_monoblack_pauper_build(self):
        import json
        event = json.loads(audit.STEFANIE_PAUPER_BUILD.read_text(encoding="utf-8"))
        main = audit.parse_counts(audit.CURRENT_STEFANIE_PAUPER.read_bytes(),
                                  "current Stefanie Pauper")
        self.assertEqual(event["sideboard"], [])
        self.assertEqual(event["sideboard_cards"], 0)
        self.assertEqual(main, {entry["name"]: entry["quantity"] for entry in event["main_deck"]})
        self.assertEqual(audit.sha256(audit.CURRENT_STEFANIE_PAUPER.read_bytes()),
                         event["current_deck_sha256"])
        self.assertEqual(sum(main.values()), 60)
        self.assertEqual(len(main), 15)
        self.assertEqual(main["Swamp"], 24)
        self.assertEqual(main["Corrupt"], 4)
        self.assertEqual(main["Gray Merchant of Asphodel"], 3)
        self.assertEqual(main["Relentless Drednok"], 3)


if __name__ == "__main__":
    unittest.main()
