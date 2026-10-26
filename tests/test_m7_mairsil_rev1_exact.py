"""Exact-source Deck #33 Mairsil M7 Rev1 structural and decision tests; no win-rate claims."""
import hashlib
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ROOT_M7 = ROOT / "data/grixis/m7"
BASE = ROOT_M7 / "baseline_sources/Mairsil_the_Pretender_chatgpt_rev1_baseline.txt"
CAND = ROOT_M7 / "candidate_lists/Mairsil_the_Pretender_chatgpt_rev1.txt"
REV = ROOT_M7 / "decision_reviews/Mairsil__the_Pretender_rev1.json"
ALT_SANCTUM = ROOT_M7 / "research_challengers/Mairsil_the_Pretender_ChatGPT_Rev1_alt7_Sanctum.txt"
ALT_RESONATOR = ROOT_M7 / "research_challengers/Mairsil_the_Pretender_ChatGPT_Rev1_alt7_Resonator.txt"

BASE_SHA = "51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5"
CAND_SHA = "fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad"
ADDS = {"Cavern Harpy", "Marsh Flats", "Agatha's Soul Cauldron", "Misty Rainforest", "Riptide Laboratory", "Phyrexian Devourer"}
CUTS = {"Cephalid Inkshrouder", "Haunted Ridge", "Omen Hawker", "Shipwreck Marsh", "Sokenzan, Crucible of Defiance", "Torchling"}
LANDS = {
    "Ancient Tomb", "Badlands", "Blightstep Pathway // Searstep Pathway", "Blood Crypt",
    "Bloodstained Mire", "City of Brass", "Clearwater Pathway // Murkwater Pathway",
    "Command Tower", "Minamo, School at Water's Edge", "Marsh Flats", "Island",
    "Luxury Suite", "Mana Confluence", "Morphic Pool", "Mountain", "Otawara, Soaring City",
    "Polluted Delta", "Riverglide Pathway // Lavaglide Pathway", "Scalding Tarn",
    "Misty Rainforest", "Riptide Laboratory", "Steam Vents", "Stormcarved Coast",
    "Sulfur Falls", "Sulfurous Springs", "Swamp", "Takenuma, Abandoned Mire",
    "Training Center", "Underground Sea", "Volcanic Island", "Watery Grave", "Xander's Lounge",
}

def read_names(path):
    raw = path.read_bytes()
    assert raw.endswith(b"\n"), path
    lines = raw.decode("utf8").splitlines()
    names = []
    for line in lines:
        match = re.fullmatch(r"1x (.+?)( \[Commander\])?", line)
        assert match, (path, line)
        names.append(match.group(1))
    assert len(names) == len(set(names)) == 100, path
    assert names[0] == "Mairsil, the Pretender", path
    return names

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

class TestMairsilRev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = set(read_names(BASE))
        cls.new = set(read_names(CAND))
        cls.review = json.loads(REV.read_text(encoding="utf8"))

    def test_sha_and_archidekt(self):
        self.assertEqual(sha(BASE), BASE_SHA)
        self.assertEqual(sha(CAND), CAND_SHA)
        self.assertEqual(CAND.read_text().count("[Commander]"), 1)
        self.assertEqual(len(self.new & LANDS), 32)

    def test_exact_six_deltas(self):
        self.assertEqual(self.new - self.old, ADDS)
        self.assertEqual(self.old - self.new, CUTS)
        self.assertEqual(set(self.review["final_changes"]["adds"]), ADDS)
        self.assertEqual(set(self.review["final_changes"]["cuts"]), CUTS)
        self.assertEqual(self.review["final_candidate"]["sha256"], CAND_SHA)

    def test_two_real_full_100_larger_packages(self):
        for path, exact_sha, extra_add, extra_cut in [
            (ALT_SANCTUM, "7327154c34cdc34fd18f1bde36b096d10491000da946b3b36d775e9bb6e76f33", "Sanctum of Eternity", "Stormcarved Coast"),
            (ALT_RESONATOR, "1e690ac39a8994635d2e72b47d15b8a7049b38ace92f1b3c4bfe1dcd0860950e", "Strionic Resonator", "Fellwar Stone"),
        ]:
            self.assertEqual(sha(path), exact_sha)
            names = set(read_names(path))
            self.assertEqual(names - self.old, ADDS | {extra_add})
            self.assertEqual(self.old - names, CUTS | {extra_cut})

    def test_preserved_cage_combo_core(self):
        for name in [
            "Mairsil, the Pretender", "Quicksilver Elemental", "Gilded Lotus",
            "Staff of Domination", "Walking Ballista", "Rings of Brighthearth",
            "Pack Rat", "Displacer Kitten", "Spark Double", "Asmodeus the Archfiend",
            "Aetherling", "Hateflayer", "Tree of Perdition", "Morphling",
            "Horseshoe Crab", "Endling", "Fellwar Stone",
        ]:
            self.assertIn(name, self.new)

    def test_owner_boundary_and_metadata(self):
        self.assertFalse(self.review["owner_authority"]["exact_candidate_owner_approved"])
        self.assertFalse(self.review["owner_authority"]["canonical_deck_changed"])
        self.assertEqual(self.review["readiness"], "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED")
        self.assertEqual(self.review["verification"]["power_bracket"], 4)
        self.assertEqual(self.review["verification"]["archidekt_tags"], ["Cage Toolbox", "Activated Abilities", "Combo"])

if __name__ == "__main__":
    unittest.main()
