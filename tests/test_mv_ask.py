"""Phase 7 companion: representative hard queries with explicit confidence flags."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask as A  # noqa: E402


class CompanionTests(unittest.TestCase):
    def test_card_lookup_separates_oracle_and_flavor_and_flags_staleness(self):
        r = A.card("Sol Ring")
        self.assertEqual(r["result"]["oracle_text"], "{T}: Add {C}{C}.")
        self.assertEqual(r["result"]["commander_legality"], "legal")
        self.assertTrue(r["sources"][0].startswith("https://scryfall.com/card/"))
        if r["data_as_of"] < A.CURRENT_SNAPSHOT_DATE:
            if A._reconciled("Sol Ring"):  # committed drift report found no change against the current snapshot
                self.assertEqual(r["confidence"], "VERIFIED")
                self.assertTrue(r["flags_info"][0].startswith("ORACLE_RECONCILED_WITH_SNAPSHOT_"))
            else:
                self.assertIn("STALE_ORACLE_VS_CURRENT_SNAPSHOT", r["flags"])
                self.assertEqual(r["confidence"], "QUALIFIED")

    def test_card_changed_in_drift_report_stays_stale(self):
        saved = A._drift
        try:
            A._drift = (True, {"Sol Ring"})
            r = A.card("Sol Ring")
            self.assertIn("STALE_ORACLE_VS_CURRENT_SNAPSHOT", r["flags"])
            self.assertEqual(r["confidence"], "QUALIFIED")
            A._drift = (False, set())  # report missing or for another snapshot
            self.assertEqual(A.card("Sol Ring")["confidence"], "QUALIFIED")
        finally:
            A._drift = saved

    def test_unknown_card_is_not_found_with_suggestions(self):
        r = A.card("Sol Rin")
        self.assertEqual(r["confidence"], "NOT_FOUND")
        self.assertIn("sol ring", r["result"]["suggestions"])

    def test_sibling_question(self):
        r = A.ask("Who is Urza's brother?")
        self.assertEqual(r["confidence"], "VERIFIED")
        names = [x["name"] for x in r["result"]["relations_by_status"]["CANON_CONFIRMED"]]
        self.assertEqual(names, ["Mishra"])
        self.assertTrue(all("magic.wizards.com" in u for u in r["sources"]))

    def test_disputed_answer_is_qualified_not_flattened(self):
        r = A.ask("Where did the Golgothian Sylex come from?")
        self.assertEqual(r["confidence"], "QUALIFIED")
        self.assertIn("CANON_DISPUTED_PRESENT", r["flags"])
        row = r["result"]["relations_by_status"]["CANON_DISPUTED"][0]
        self.assertIn("competing legends", row["limitation"])

    def test_inverse_direction_question(self):
        r = A.ask("Who destroyed the Golgothian Sylex?")
        rows = r["result"]["relations_by_status"]["CANON_CONFIRMED"]
        self.assertEqual([x["name"] for x in rows], ["Ajani"])

    def test_open_question_and_ambiguous_name(self):
        r = A.ask("Nicol Bolas")
        self.assertEqual(r["result"]["type"], "Character")
        self.assertIn("AMBIGUOUS_NAME", r["flags"])
        self.assertIn("OPEN_QUESTION_PRESENT", r["flags"])
        self.assertEqual(r["also_card"], "Nicol Bolas")

    def test_unknown_lore_is_not_invented(self):
        r = A.ask("Who is Zorblax the Unreal?")
        self.assertEqual(r["confidence"], "NOT_FOUND")
        self.assertEqual(r["result"], {})
        self.assertIn("NO_CITED_LORE", r["flags"])

    def test_who_defeated_yawgmoth_preserves_all_accounts(self):
        r = A.ask("Who defeated Yawgmoth?")
        self.assertEqual(r["confidence"], "QUALIFIED")
        self.assertIn("CANON_DISPUTED_PRESENT", r["flags"])
        names = {x["name"] for x in r["result"]["relations_by_status"]["CANON_DISPUTED"]}
        self.assertTrue({"Karn", "Gerrard Capashen", "Urza"} <= names)

    def test_who_created_old_phyrexia_is_open(self):
        r = A.ask("Who created Old Phyrexia?")
        self.assertEqual(r["confidence"], "QUALIFIED")
        self.assertIn("OPEN_QUESTION_PRESENT", r["flags"])

    def test_who_created_mirrodin(self):
        r = A.ask("Who created Mirrodin?")
        self.assertEqual(r["confidence"], "VERIFIED")
        self.assertIn("Karn", {x["name"] for x in r["result"]["relations_by_status"]["CANON_CONFIRMED"]})

    def test_cli_exit_codes(self):
        self.assertEqual(A.main(["ask", "Who was Kayla bin-Kroog's husband?"]), 0)
        self.assertEqual(A.main(["ask", "Who is Zorblax the Unreal?"]), 3)


if __name__ == "__main__":
    unittest.main()
