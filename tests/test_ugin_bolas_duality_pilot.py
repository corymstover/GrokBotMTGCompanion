"""Phase 6 Pilot 1 regressions: a complete, legal-by-snapshot, UNAPPROVED proposal."""
import copy
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_ugin_bolas_duality_pilot as P


class PilotAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = P.build()
        cls.ev = json.loads(P.EVIDENCE.read_text(encoding="utf-8"))
        cls.cards = {c["name"]: c for c in cls.ev["cards"]}

    def test_complete_hundred_cards_unapproved(self):
        self.assertEqual(self.report["result"], "PASS")
        self.assertEqual(self.report["total"], 100)
        self.assertTrue(self.report["status"].startswith("UNAPPROVED"))
        self.assertFalse(self.report["realtime_fetch"])

    def test_commander_is_grixis_bolas_and_ugin_in_99(self):
        first = P.DECK.read_text().splitlines()[0]
        self.assertTrue(first.startswith("1x Nicol Bolas, the Ravager") and first.endswith("[Commander]"))
        for ugin in ("Ugin, the Spirit Dragon", "Ugin, the Ineffable", "Ugin, Eye of the Storms"):
            self.assertIn(ugin, self.cards)

    def test_game_changer_ceiling(self):
        self.assertEqual(self.report["game_changers"], ["Bolas's Citadel"])

    def test_a4_exact_ugin_art_not_promo(self):
        self.assertEqual(self.cards["Ugin, the Spirit Dragon"]["printing"]["id"],
                         "58c1e824-c8a9-4312-8e4c-a29a26d189a4")

    def test_direct_depictions_are_official_captions_only(self):
        direct = sorted(n for n, c in self.cards.items() if c["tier"] == "DIRECT_DEPICTION")
        self.assertEqual(direct, sorted(["Crux of Fate", "Hour of Devastation", "Jace's Defeat",
                                         "Liliana's Defeat", "Chandra's Defeat", "Liliana's Triumph"]))
        for n in direct:
            self.assertTrue(self.cards[n]["source"].startswith("https://magic.wizards.com/"))

    def test_disputed_claims_not_asserted(self):
        used = {cid for c in self.cards.values() for cid in c["pack_a_claims"]}
        self.assertFalse(used & {"A003", "A004", "A011", "A012"})

    def _mutated(self, fn):
        ev = copy.deepcopy(self.ev)
        fn(ev)
        def fake(path, *a, **k):
            return json.dumps(ev) if path == P.EVIDENCE else path.read_bytes().decode("utf-8")
        with mock.patch.object(Path, "read_text", autospec=True, side_effect=fake):
            with self.assertRaises(ValueError):
                P.build()

    def test_rejects_flavor_only_direct_depiction(self):
        def f(ev):
            for c in ev["cards"]:
                if c["name"] == "Magmaquake":
                    c["tier"] = "DIRECT_DEPICTION"
        self._mutated(f)

    def test_rejects_off_identity_or_illegal(self):
        def f(ev):
            ev["cards"][3]["printing"]["color_identity"] = ["G"]
        self._mutated(f)

    def test_rejects_disputed_claim_dependency(self):
        def f(ev):
            ev["cards"][1]["pack_a_claims"] = ["A003"]
        self._mutated(f)


if __name__ == "__main__":
    unittest.main()
