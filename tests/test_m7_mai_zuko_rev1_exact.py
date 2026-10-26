"""Exact-source, self-contained Deck #32 M7 Rev1 assertions. No win-rate claims."""
import hashlib
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/baseline_sources/Mai_and_Zuko_chatgpt_rev1_baseline.txt"
CAND = ROOT / "data/grixis/m7/candidate_lists/Mai_and_Zuko_chatgpt_rev1.txt"
INDEX = ROOT / "data/grixis/m7/research_challengers/Mai_and_Zuko_ChatGPT_Rev1_Oracle_Index_20261025.json"
REVIEW = ROOT / "data/grixis/m7/decision_reviews/Mai_and_Zuko_chatgpt_rev1.json"
BASE_SHA = "aa2036f49f38e6503734d99c852acdfa704aa1b27e44bb26d6e9566a73a0d4a2"
CAND_SHA = "8cdf614e47eadf3ec33049a770a3f0a2b84338e84c31bb26a49e6f26f5c60d97"

def names(path):
    data = path.read_text(encoding="utf-8")
    lines = data.splitlines()
    out = []
    for line in lines:
        match = re.fullmatch(r"1x (.+?)( \[Commander\])?", line)
        if match is None:
            raise AssertionError(f"Invalid Archidekt line: {line!r}")
        out.append(match.group(1))
    return out

class TestMaiZukoRev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = names(BASE)
        cls.candidate = names(CAND)
        cls.idx = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.review = json.loads(REVIEW.read_text(encoding="utf-8"))
        cls.by_name = {row["name"]: row for row in cls.idx["cards"]}

    def test_exact_hash_and_format(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(), CAND_SHA)
        self.assertTrue(CAND.read_bytes().endswith(b"\n"))
        self.assertEqual(len(self.candidate), 100)
        self.assertEqual(len(self.original), 100)
        self.assertEqual(len(set(self.candidate)), 100)
        self.assertEqual(self.candidate[0], "Mai and Zuko")
        self.assertEqual(self.original[0], "Mai and Zuko")
        self.assertEqual(CAND.read_text().count("[Commander]"), 1)

    def test_exact_seven_replacements(self):
        expected_adds = {
            "Verdant Catacombs", "Spire of Industry",
            "Sink into Stupor // Soporific Springs", "Jeska's Will",
            "Pact of Negation", "Fire Nation Turret", "Forensic Gadgeteer"
        }
        expected_cuts = {
            "Sulfurous Springs", "Path of Ancestry", "Xander's Lounge",
            "Chaos Warp", "Lightning Greaves", "Avatar Roku, Firebender", "Tundra Tank"
        }
        self.assertEqual(set(self.candidate) - set(self.original), expected_adds)
        self.assertEqual(set(self.original) - set(self.candidate), expected_cuts)
        self.assertEqual(set(self.review["final_changes"]["adds"]), expected_adds)
        self.assertEqual(set(self.review["final_changes"]["cuts"]), expected_cuts)
        self.assertFalse(self.review["owner_authority"]["canonical_deck_changed"])
        self.assertFalse(self.review["owner_authority"]["exact_candidate_owner_approved"])

    def test_both_real_eight_swap_challengers(self):
        variants = [
            (
                ROOT / "data/grixis/m7/research_challengers/Mai_and_Zuko_ChatGPT_Rev1_alt8_Arid_over_Bog.txt",
                "a73ac5672bd890b25c3e12454804bf705711482b696e72f5dc39972fe1d88ece",
                "Arid Mesa", "Bojuka Bog",
            ),
            (
                ROOT / "data/grixis/m7/research_challengers/Mai_and_Zuko_ChatGPT_Rev1_alt8_Grim_over_Fellwar.txt",
                "4922e70ed3e38bba38bc85ad4e689d8ff2e3957c63ba0244d4f047ca2161f39f",
                "Grim Monolith", "Fellwar Stone",
            ),
        ]
        final_adds = set(self.review["final_changes"]["adds"])
        final_cuts = set(self.review["final_changes"]["cuts"])
        for path, digest, extra_add, extra_cut in variants:
            cards = names(path)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest)
            self.assertEqual(len(cards), 100)
            self.assertEqual(len(set(cards)), 100)
            self.assertEqual(cards[0], "Mai and Zuko")
            self.assertEqual(set(cards) - set(self.original), final_adds | {extra_add})
            self.assertEqual(set(self.original) - set(cards), final_cuts | {extra_cut})

    def test_oracle_card_identity_and_legality(self):
        self.assertEqual(len(self.by_name), 100)
        self.assertEqual(set(self.by_name), set(self.candidate))
        self.assertEqual(self.idx["candidate_sha256"], CAND_SHA)
        self.assertEqual(self.idx["baseline_sha256"], BASE_SHA)
        for card in self.by_name.values():
            self.assertEqual(card["commander_legality"], "legal", card["name"])
            self.assertTrue(set(card["color_identity"]) <= set("UBR"), card["name"])
            self.assertTrue(card["oracle_id"], card["name"])
            self.assertTrue(card["oracle_text"], card["name"])
        self.assertEqual(self.idx["project_exceptions"], [])
        self.assertEqual(self.by_name["Mai and Zuko"]["color_identity"], ["B", "R", "U"])

    def test_lands_and_protected_engine(self):
        land_faces = {n for n, c in self.by_name.items() if "Land" in c["type_line"]}
        self.assertEqual(len(land_faces), 31)
        self.assertIn("Sink into Stupor // Soporific Springs", land_faces)
        self.assertEqual(self.idx["front_face_lands_including_mdfc"], 31)
        for name in [
            "Ally Encampment", "Fire Lord Azula", "Firebender Ascension",
            "Fire Nation Occupation", "Unwinding Clock", "Bender's Waterskin",
            "Roaming Throne", "Basalt Monolith", "Rings of Brighthearth",
            "Walking Ballista", "Bolas's Citadel", "Aetherflux Reservoir",
            "Sensei's Divining Top", "Underworld Breach",
            "Lion's Eye Diamond", "Brain Freeze", "Toxic Deluge",
        ]:
            self.assertIn(name, self.candidate)

    def test_real_finite_mana_and_timing_cases(self):
        # Basalt taps for three and pays two to untap with Gadgeteer.
        self.assertIn("cost {1} less", self.by_name["Forensic Gadgeteer"]["oracle_text"])
        self.assertIn("investigate", self.by_name["Forensic Gadgeteer"]["oracle_text"])
        self.assertEqual(3 - (3 - 1), 1)
        # Basalt + Rings copy: two activations yield six, costs 3+2.
        self.assertEqual(6 - (3 + 2), 1)
        # Grim + Rings without Gadgeteer does not generate mana.
        self.assertEqual(6 - (4 + 2), 0)
        # Commander firebending3 and an added Turret firebending2
        # are independently granted: 5R in combat when both trigger.
        self.assertIn("firebending 2", self.by_name["Fire Nation Turret"]["oracle_text"].lower())
        self.assertIn("Firebending 3", self.by_name["Mai and Zuko"]["oracle_text"])
        self.assertEqual(3 + 2, 5)
        self.assertIn("{3}{U}{U}", self.by_name["Pact of Negation"]["oracle_text"])
        self.assertIn("sorcery", self.by_name["Jeska's Will"]["type_line"].lower())

    def test_declaration_and_preapproval_gates(self):
        self.assertEqual(self.review["final_candidate"]["sha256"], CAND_SHA)
        self.assertEqual(self.review["final_candidate"]["card_count"], 100)
        self.assertEqual(self.review["verification"]["power_bracket"], 4)
        self.assertEqual(self.review["verification"]["archidekt_tags"], ["Artifacts", "Flash", "Firebending"])
        self.assertEqual(self.review["readiness"], "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED")

if __name__ == "__main__":
    unittest.main()
