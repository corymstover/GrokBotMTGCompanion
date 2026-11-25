"""Regression tests for historic source integrity and current five-deck allocation."""
from __future__ import annotations

import importlib.util
import io
import json
import sys
import unittest
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location(
    "physical_audit", ROOT / "scripts" / "audit_physical_collection.py")
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)
from audit_physical_collection_2026_11_25 import BASE, MAPPING, ACTIVE_MAPPING, RETIRED, SNAP, OLD, read_csv, verify


class PhysicalCollectionSnapshotTests(unittest.TestCase):
    def test_immutable_november_8_archive_unchanged(self):
        master = audit.parse_counts(audit.MASTER.read_bytes(), "historical inventory")
        self.assertEqual((sum(master.values()), len(master)), (1332, 751))
        with ZipFile(audit.ARCHIVE) as archive:
            cards = {n: audit.parse_counts(archive.read(n), n) for n in audit.DECKS}
        self.assertEqual(sum(cards["Xander_EDH_IRL.csv"].values()), 101)
        self.assertEqual(sum(cards["Dihada_EDH_IRL.csv"].values()), 100)
        self.assertEqual(sum(cards["Stefanie_Jund_Prerelease.csv"].values()), 43)
        self.assertEqual(cards["Xander_EDH_IRL.csv"]["Lutri, the Spellchaser"], 1)

    def test_current_audit_entry_point(self):
        with redirect_stdout(io.StringIO()):
            audit.main(write=False)

    def test_owner_source_november_25_and_five_active_decks(self):
        with redirect_stdout(io.StringIO()):
            result = verify(write=False)
        self.assertEqual(result["owned"], 1470)
        self.assertEqual(result["distinct_owned"], 844)
        self.assertEqual(result["deck_slots"], 461)
        self.assertEqual(result["physical_reserved"], 448)
        self.assertEqual(result["available"], 1022)
        self.assertEqual(result["available_names"], 610)
        self.assertEqual(result["incoming_proxies"], 13)
        self.assertEqual(len(MAPPING), 5)
        self.assertEqual(len(ACTIVE_MAPPING), 5)

    def test_house_rule_lutri_is_separate_from_main_deck(self):
        xander = read_csv(BASE / "current_decks" / "Xander_EDH_IRL.csv")
        self.assertEqual(xander["Lord Xander, the Collector"], 1)
        self.assertEqual(xander["Lutri, the Spellchaser"], 1)
        self.assertEqual(sum(xander.values()) - xander["Lutri, the Spellchaser"], 100)
        state = json.loads((BASE / "current_status.json").read_text())
        self.assertTrue(state["xander_companion_counted_outside_main_deck"])
        self.assertIn("banned", state["xander_companion_status"])

    def test_xander_exact_owner_confirmed_upgrade(self):
        historical = read_csv(SNAP / "Cory_s_Lord_Xander_IRL_EDH.csv")
        active = read_csv(BASE / "current_decks" / "Xander_EDH_IRL.csv")
        event = json.loads((BASE / "updates" / "2026-11-25_lord_xander_upgrade.json").read_text())
        self.assertEqual(historical - active, Counter(dict.fromkeys(event["removed"], 1)))
        self.assertEqual(active - historical, Counter(dict.fromkeys(event["added"], 1)))
        self.assertEqual(len(event["added"]), 18)
        self.assertEqual(len(event["removed"]), 18)
        self.assertEqual(sum(active.values()), 101)
        self.assertEqual(active["Lord Xander, the Collector"], 1)
        self.assertEqual(active["Lutri, the Spellchaser"], 1)
        self.assertEqual(active["Fraying Sanity"], 1)
        self.assertEqual(active["Nicol Bolas, God-Pharaoh"], 1)
        self.assertEqual(active["Sauron, the Dark Lord"], 1)
        self.assertEqual(event["lands"], 37)

    def test_recorded_sale_leaves_original_uploaded_inventory_unchanged(self):
        uploaded = read_csv(SNAP / "Every_Card_we_own_IRL_corrected.csv")
        status = json.loads((BASE / "current_status.json").read_text())
        live = read_csv(ROOT / status["source_master_inventory"])
        self.assertEqual((sum(uploaded.values()), len(uploaded)), (1471, 845))
        self.assertEqual((sum(live.values()), len(live)), (1470, 844))
        self.assertEqual(uploaded - live, Counter({"The Balrog, Durin's Bane": 1}))
        self.assertEqual(live - uploaded, Counter())
        self.assertEqual(live["Ingris Stingerquill"], 1)

    def test_dihada_exact_owner_confirmed_five_swaps(self):
        original = read_csv(SNAP / "Stefanie_Dihada_EDH_IRL.csv")
        active = read_csv(BASE / "current_decks" / "Dihada_EDH_IRL.csv")
        event = json.loads((BASE / "updates" / "2026-11-25_dihada_upgrade.json").read_text())
        self.assertEqual(original - active, Counter(dict.fromkeys(event["removed"], 1)))
        self.assertEqual(active - original, Counter(dict.fromkeys(event["added"], 1)))
        self.assertEqual(sum(active.values()), 100)
        self.assertEqual(active["Dihada, Binder of Wills"], 1)
        for keep in ["Piru, the Volatile", "Heroes' Podium", "Zeriam, Golden Wind", "Ingris Stingerquill"]:
            self.assertEqual(active[keep], 1)
        for addition in event["added"]:
            self.assertEqual(active[addition], 1)
        self.assertEqual(len(event["added"]), len(event["removed"]))
        self.assertEqual(event["lands"], 36)
        self.assertTrue((ROOT / event["approved_full_user_list"]).read_text().startswith("1x Adriana, Captain of the Guard (dmc)"))

    def test_monored_shortfalls_are_proxies_not_owned(self):
        state = json.loads((BASE / "current_status.json").read_text())
        inventory = read_csv(ROOT / state["source_master_inventory"])
        red = read_csv(SNAP / "Mono_Red_Madness.csv")
        self.assertEqual(sum(red.values()), 60)
        proxies = Counter({"Fireblast": 2, "Grab the Prize": 4,
                           "Kessig Flamebreather": 1, "Lava Dart": 2,
                           "Voldaren Epicure": 4})
        all_decks = Counter()
        for source, _, _ in ACTIVE_MAPPING.values():
            live_name = next(name for name, rec in ACTIVE_MAPPING.items() if rec[0] == source)
            all_decks.update(read_csv(BASE / "current_decks" / live_name))
        self.assertEqual(all_decks - inventory, proxies)
        self.assertEqual(inventory["Fireblast"], 1)
        self.assertEqual(inventory["Kessig Flamebreather"], 3)
        self.assertEqual(inventory["Lava Dart"], 2)
        self.assertEqual(inventory["Grab the Prize"], 0)
        self.assertEqual(inventory["Voldaren Epicure"], 0)

    def test_current_pool_excludes_only_actual_owned_deck_copies(self):
        state = json.loads((BASE / "current_status.json").read_text())
        inventory = read_csv(ROOT / state["source_master_inventory"])
        all_decks = Counter()
        for source, _, _ in ACTIVE_MAPPING.values():
            live_name = next(name for name, rec in ACTIVE_MAPPING.items() if rec[0] == source)
            all_decks.update(read_csv(BASE / "current_decks" / live_name))
        pool = read_csv(BASE / "current_available.csv")
        self.assertEqual(pool, inventory - all_decks)
        self.assertEqual(sum(pool.values()), 1022)
        self.assertEqual(len(pool), 610)

    def test_monoblack_devotion_released_but_archived(self):
        archived = read_csv(OLD / "Mono_Black_Devotion_Control.csv")
        self.assertEqual(sum(archived.values()), 60)
        self.assertEqual(len(archived), 15)
        self.assertFalse((BASE / "current_decks" / RETIRED).exists())
        pool = read_csv(BASE / "current_available.csv")
        state = json.loads((BASE / "current_status.json").read_text())
        owned = read_csv(ROOT / state["source_master_inventory"])
        active = Counter()
        for filename in ACTIVE_MAPPING:
            active.update(read_csv(BASE / "current_decks" / filename))
        # Retired deck copies are in circulation: they may subsequently be
        # assigned to other live decks (e.g., Eject the Warp Core in Xander).
        for name in archived:
            self.assertEqual(pool[name], max(0, owned[name] - active[name]), name)
        self.assertEqual(read_csv(BASE / "current_decks" / "Xander_EDH_IRL.csv")["Eject the Warp Core"], 1)
        state = json.loads((BASE / "current_status.json").read_text())
        self.assertNotIn(RETIRED, state["built_decks"])
        self.assertEqual(state["disassembled_built_decks"], [RETIRED])



    def test_dihada_swap_and_new_grixis_cards(self):
        before = read_csv(OLD / "Stefanie_Dihada_EDH_IRL.csv")
        after = read_csv(SNAP / "Stefanie_Dihada_EDH_IRL.csv")
        self.assertEqual(before - after, Counter({"The Balrog, Durin's Bane": 1}))
        self.assertEqual(after - before, Counter({"Ingris Stingerquill": 1}))
        pool = read_csv(BASE / "current_available.csv")
        for name in ["Gandalf, Goblins' Bane // Flameshape"]:
            self.assertGreaterEqual(pool[name], 1, name)
        for name in ["Fraying Sanity", "Hedron Crab", "Ruin Crab", "Zellix, Sanity Flayer", "Nicol Bolas, God-Pharaoh"]:
            self.assertEqual(pool[name], 0, name)
        self.assertEqual(pool["Ingris Stingerquill"], 0)
        self.assertEqual(pool["The Balrog, Durin's Bane"], 0)
        self.assertEqual(read_csv(ROOT / json.loads((BASE / "current_status.json").read_text())["source_master_inventory"])["The Balrog, Durin's Bane"], 0)
        self.assertEqual(pool["Cavern-Hoard Dragon"], 0)


if __name__ == "__main__":
    unittest.main()
