"""Deck 22 Gwendlyn Di Corci independent M7 Rev1 six-swap research only.
Source-bound exact 100, two manual Scryfall records, bounded trigger/mana cases.
No canonical owner approval or actual game/win-rate claim.
"""
from __future__ import annotations
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Gwendlyn_Di_Corci"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
DATA = ROOT / f"data/grixis/m7/independent_reviews/{D}_M7_Rev1_20261024.json"
ORACLE = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
ADDENDUM = ROOT / f"data/grixis/m7/independent_reviews/{D}_Oracle_Addendum_20261024.json"
BASE_SHA = "9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9"
SHA = "36b76cbe47a04b7492007103e4baaad50324b3e72fb2067b28aa8bb9da70e355"
COMMANDER = "Gwendlyn Di Corci"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(path):
    result = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, line
        result.append((int(m[1]), m[2], bool(m[3])))
    return result


def counter(path):
    return Counter({name: q for q, name, _ in rows(path)})


class GwendlynIndependentM7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review = json.loads(DATA.read_text())
        cls.frozen = json.loads(ORACLE.read_text())
        cls.published = json.loads(ADDENDUM.read_text())["cards"]
        cls.oracle = {c["name"]: c for c in cls.frozen["cards"]}
        cls.oracle.update(cls.published)
        cls.candidate = ROOT / cls.review["primary_candidate"]["path"]

    def test_original_canonical_byte_provenance_and_nonapproval(self):
        self.assertEqual(digest(BASE), BASE_SHA)
        self.assertFalse(BASE.read_bytes().endswith(b"\n"))
        self.assertEqual(self.review["source"]["canonical_baseline_raw_sha256"], BASE_SHA)
        self.assertEqual(self.review["source"]["grok_pr"], 670)
        self.assertEqual(self.review["source"]["grok_head"], "7483728a700e01f2b45172c9c55438903d9092ac")
        self.assertEqual(self.review["stage"], "CHATGPT_M7_INDEPENDENT_SIX_SWAP_RESEARCH_CANDIDATE_NOT_OWNER_APPROVED")
        self.assertFalse(self.review["primary_candidate"]["owner_approved"])
        self.assertFalse(self.review["primary_candidate"]["canonical_changed"])

    def test_raw_candidate_hash_100_physical_singleton_and_commander(self):
        self.assertEqual(digest(self.candidate), SHA)
        self.assertTrue(self.candidate.read_bytes().endswith(b"\n"))
        self.assertEqual(self.review["primary_candidate"]["raw_sha256"], SHA)
        r = rows(self.candidate)
        self.assertEqual((len(r), sum(q for q, _, _ in r)), (95, 100))
        self.assertEqual(r[0], (1, COMMANDER, True))
        self.assertEqual(sum(cmd for _, _, cmd in r), 1)
        self.assertEqual([(q, name) for q, name, _ in r if q > 1],
                         [(2, "Island"), (5, "Swamp")])
        self.assertEqual(counter(self.candidate)["Mountain"], 1)
        self.assertEqual([name for _, name, _ in r[1:]], sorted([name for _, name, _ in r[1:]], key=str.casefold))

    def test_six_exact_physical_substitutions_with_basic_quantity(self):
        base = counter(BASE); cand = counter(self.candidate)
        ss = self.review["swaps"]
        self.assertEqual(len(ss), 6)
        expect_add = {"Hymn to Tourach", "Rings of Brighthearth", "Sting, the Glinting Dagger",
                      "Misty Rainforest", "Marsh Flats", "Shivan Reef"}
        expect_cut = {"Dauthi Voidwalker", "Underworld Dreams", "The Raven Man",
                      "Crumbling Necropolis", "Drowned Catacomb", "Mountain"}
        self.assertEqual(cand - base, Counter({name: 1 for name in expect_add}))
        self.assertEqual(base - cand, Counter({name: 1 for name in expect_cut}))
        self.assertEqual(base["Mountain"], 2)
        self.assertEqual(cand["Mountain"], 1)

    def test_legal_oracle_and_game_changers_all_proposed_100(self):
        candidate = counter(self.candidate)
        self.assertEqual(len(candidate), 95)
        gcs = set(); lands = 0; library_nonlands = 0; mana_sum = 0
        published = set()
        for name, qty in candidate.items():
            self.assertIn(name, self.oracle, name)
            c = self.oracle[name]
            self.assertEqual(c["commander_legality"], "legal", name)
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), name)
            self.assertIsNotNone(c["mana_cost"], name)
            self.assertTrue(c["oracle_text"], name)
            if c["game_changer"]: gcs.add(name)
            if "Land" in c["type_line"]: lands += qty
            elif name != COMMANDER:
                library_nonlands += qty
                mana_sum += float(c["cmc"]) * qty
            if name in self.published:
                published.add(name)
                self.assertTrue(c["source"].startswith("https://scryfall.com/card/"))
                self.assertIsNone(c["oracle_id"])
            else:
                self.assertTrue(c["oracle_id"], name)
        self.assertEqual((lands, library_nonlands), (35, 64))
        self.assertEqual(round(mana_sum/library_nonlands, 3), 2.328)
        self.assertEqual(len(gcs), 17)
        self.assertEqual(published, {"Sting, the Glinting Dagger", "Misty Rainforest"})
        self.assertEqual(self.review["primary_candidate"]["bracket"], "4 — Optimized")
        self.assertEqual(self.review["primary_candidate"]["tags"], ["Discard", "Wheels", "Untap"])
        self.assertEqual(self.review["primary_candidate"]["project_exceptions"], [])

    def test_ring_copy_and_sting_timing_no_false_free_equips(self):
        oracle = self.oracle
        self.assertIn("Activate only during your turn", oracle[COMMANDER]["oracle_text"])
        self.assertIn("Target player discards a card at random", oracle[COMMANDER]["oracle_text"])
        self.assertIn("may pay {2}", oracle["Rings of Brighthearth"]["oracle_text"])
        self.assertIn("copy that ability", oracle["Rings of Brighthearth"]["oracle_text"])
        self.assertIn("Whenever an ability of equipped creature is activated",
                      oracle["Illusionist's Bracers"]["oracle_text"])
        sting = oracle["Sting, the Glinting Dagger"]
        self.assertEqual(sting["mana_cost"], "{2}")
        self.assertIn("Equip {2}", sting["oracle_text"])
        self.assertIn("has haste", sting["oracle_text"])
        self.assertIn("At the beginning of each combat, untap equipped creature", sting["oracle_text"])
        # One Gwendlyn activation with Bracers and a paid Rings trigger:
        # original 1 + free Bracers 1 + optional paid Rings 1 = 3.
        self.assertEqual(1 + 1 + 1, 3)
        # Extra Sting untap at our own combat permits a second activation;
        # an opponent's combat does not override Gwendlyn's own-turn restriction.

    def test_dauthi_exile_replacement_losses_for_three_retained_engines(self):
        t = lambda n: self.oracle[n]["oracle_text"]
        self.assertIn("instead exile it with a void counter", t("Dauthi Voidwalker"))
        self.assertIn("from a graveyard onto the battlefield", t("Tergrid, God of Fright // Tergrid's Lantern"))
        self.assertIn("exile it from their graveyard with a stash counter", t("Tinybones, Bauble Burglar"))
        self.assertIn("card is put into an opponent's graveyard", t("Bloodchief Ascension"))
        self.assertIn("Target player discards two cards at random", t("Hymn to Tourach"))

    def test_typed_fetch_and_pain_mana_tradeoffs(self):
        t = lambda n: self.oracle[n]["oracle_text"]
        self.assertIn("Pay 1 life", t("Misty Rainforest"))
        self.assertIn("Forest or Island card", t("Misty Rainforest"))
        self.assertIn("Pay 1 life", t("Marsh Flats"))
        self.assertIn("Plains or Swamp card", t("Marsh Flats"))
        for land in ("Underground Sea", "Watery Grave"):
            self.assertIn("Island", self.oracle[land]["type_line"])
            self.assertIn("Swamp", self.oracle[land]["type_line"])
        for land in ("Badlands", "Blood Crypt"):
            self.assertIn("Swamp", self.oracle[land]["type_line"])
        for land in ("Steam Vents", "Volcanic Island"):
            self.assertIn("Island", self.oracle[land]["type_line"])
        self.assertIn("Island Swamp Mountain", self.oracle["Xander's Lounge"]["type_line"])
        self.assertIn("Add {U} or {R}", t("Shivan Reef"))
        self.assertIn("deals 1 damage to you", t("Shivan Reef"))
        self.assertIn("This land enters tapped", t("Crumbling Necropolis"))
        self.assertIn("enters tapped unless you control an Island or a Swamp", t("Drowned Catacomb"))
        # New fetches must not be falsely counted as three untapped colors at once.

    def test_owner_protected_untap_discard_and_wheel_identity(self):
        cand=counter(self.candidate)
        keep=[
          "Mind Twist", "Magewright's Stone", "Pemmin's Aura", "Illusionist's Bracers",
          "Minamo, School at Water's Edge", "Patriar's Seal", "Thousand-Year Elixir",
          "Lightning Greaves", "Waste Not", "Geth's Grimoire", "Liliana's Caress",
          "Tinybones, Trinket Thief", "Tinybones, Bauble Burglar", "Bloodchief Ascension",
          "Tergrid, God of Fright // Tergrid's Lantern", "Chains of Mephistopheles",
          "Notion Thief", "Oppression", "Bottomless Pit", "Wheel of Fortune",
          "Wheel of Misfortune", "Windfall", "Timetwister", "Jace's Archivist",
          "Magus of the Wheel", "Kess, Dissident Mage", "Underworld Breach",
          "Yawgmoth's Will", "Dream Salvage", "Rhystic Study"]
        for n in keep: self.assertEqual(cand[n], 1, n)
        for n in ["Megrim", "Aphetto Alchemist", "Thassa's Oracle", "Jeweled Lotus"]:
            self.assertNotIn(n, cand)

    def test_two_staged_alternatives_are_complete_100s_source_valid(self):
        src = counter(self.candidate)
        for a in self.review["alternatives"]:
            p = ROOT / a["path"]
            self.assertEqual(digest(p), a["raw_sha256"])
            self.assertEqual(sum(counter(p).values()), 100)
            self.assertEqual(rows(p)[0], (1, COMMANDER, True))
            for name in counter(p):
                self.assertIn(name, self.oracle, name)
                self.assertEqual(self.oracle[name]["commander_legality"], "legal")
            if a["id"] == "FIVE_SWAP_WITHOUT_SHIVAN":
                self.assertEqual(counter(p) - src, Counter({"Mountain": 1}))
                self.assertEqual(src - counter(p), Counter({"Shivan Reef": 1}))
            else:
                self.assertEqual(a["id"], "FREED_FROM_REAL_OVER_STING_SIX_SWAP")
                self.assertEqual(counter(p) - src, Counter({"Freed from the Real": 1}))
                self.assertEqual(src - counter(p), Counter({"Sting, the Glinting Dagger": 1}))


if __name__ == "__main__":
    unittest.main()
