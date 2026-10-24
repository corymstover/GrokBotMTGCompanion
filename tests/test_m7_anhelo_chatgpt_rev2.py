"""Deck #4 independent M7 Rev2 seven-swap source and bounded rules/mana regression.
All candidates are RESEARCH, not owner-approved/canonical. No simulation win rates.
"""
import hashlib
import json
import math
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "data/grixis/m7"
BASE = D / "baseline_sources/Anhelo_the_Painter_approved_source_2026-10-13.txt"
GROK = D / "candidate_lists/Anhelo__the_Painter.txt"
REV2 = D / "candidate_lists/Anhelo__the_Painter_ChatGPT_Rev2.txt"
FIVE = D / "research_challengers/Anhelo__the_Painter_ChatGPT_Rev2_balanced_five.txt"
HIGH = D / "research_challengers/Anhelo__the_Painter_ChatGPT_Rev2_high_mana_seven.txt"
NEW_ORACLE = D / "research_challengers/Anhelo__the_Painter_ChatGPT_Rev2_new_card_oracle.json"
OLD_ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Anhelo__the_Painter_M7_Scryfall_20261023.json"
MEMO = D / "decision_reviews/Anhelo__the_Painter_ChatGPT_Rev2_independent_comparison.md"

HASHES = {
    BASE: "8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972",
    GROK: "2c696db8013b90459b23495f8c6a94426ca86ba180a163a8a941d5c285950a58",
    REV2: "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
    FIVE: "9987bd441134cea5faf6fc14bade84a82077c1378e950a22b41402e1478e99e2",
    HIGH: "10e2882dff10b3b8dfc7b8e7623bb301393a2656f1318426512a72054123c350",
}
ADDS = {"Forsaken Miner", "Skyclave Shade", "Sinister Concierge",
        "Case of the Stashed Skeleton",
        "Fable of the Mirror-Breaker // Reflection of Kiki-Jiki",
        "City of Brass", "Misty Rainforest"}
CUTS = {"Primal Amulet // Primal Wellspring", "Talisman of Indulgence",
        "Fellwar Stone", "Maestros Ascendancy", "Lagomos, Hand of Hatred",
        "Haunted Ridge", "Shipwreck Marsh"}
BASICS = {"Island", "Mountain", "Swamp"}
ROCKS = {"Arcane Signet", "Sol Ring", "Dimir Signet", "Izzet Signet",
         "Rakdos Signet", "Fellwar Stone", "Talisman of Creativity",
         "Talisman of Dominance", "Talisman of Indulgence"}
PROTECTED = {"Anhelo, the Painter", "Reiterate", "Twinflame", "Dualcaster Mage",
             "Narset's Reversal", "Twinning Staff", "Mana Geyser", "Jeska's Will",
             "Storm-Kiln Artist", "Ral, Storm Conduit", "Ghoulish Procession",
             "Jadar, Ghoulcaller of Nephalia",
             "Poppet Stitcher // Poppet Factory", "Kess, Dissident Mage",
             "Underworld Breach", "Thunderclap Drake", "Deekah, Fractal Theorist",
             "Feed the Swarm", "Startle", "Crackle with Power", "Time Warp",
             "Torment of Hailfire", "Black Market Connections"}
NEW_NAMES = {"Forsaken Miner":"d37e0127-6f68-438e-8b9e-a71bb3c34733",
             "Case of the Stashed Skeleton":"64219e17-1302-4a43-85d2-8a6214448890",
             "Fable of the Mirror-Breaker // Reflection of Kiki-Jiki":"c0957e5e-c71b-439c-931c-9f55d2f76ace",
             "City of Brass":"f25351e3-539b-4bbc-b92d-6480acf4d722",
             "Misty Rainforest":"09dd85aa-47bc-4713-a9b9-8b52ff2285ed",
             "Deadly Dispute":"457af74a-02b3-4659-846d-63e482667f34"}

def physical(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    counts = Counter()
    for line in lines:
        quantity, sep, name = line.partition("x ")
        assert sep and quantity.isdecimal() and int(quantity)>0, line
        counts[name.removesuffix(" [Commander]")] += int(quantity)
    return lines, counts

def choose(n,k):
    return math.comb(n,k) if 0 <= k <= n else 0

def source_prob(count,n=9,required=3):
    return sum(choose(count,k)*choose(99-count,n-k)/choose(99,n)
               for k in range(required,min(count,n)+1))

class AnheloChatGPTRev2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        prev = json.loads(OLD_ORACLE.read_text(encoding="utf-8"))
        newer = json.loads(NEW_ORACLE.read_text(encoding="utf-8"))
        cls.oracle = {x["name"]:x for x in prev["cards"]+newer["cards"]}
        cls.live = newer

    def test_each_full_deck_exact_raw_hash_100(self):
        for path,expected in HASHES.items():
            with self.subTest(file=path.name):
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),expected)
                lines,cards=physical(path)
                self.assertEqual(lines[0],"1x Anhelo, the Painter [Commander]")
                self.assertEqual(sum(cards.values()),100)
                self.assertEqual(len(cards),94)
                self.assertEqual(len(lines),94)
                self.assertEqual({n:q for n,q in cards.items() if q>1},
                                 {"Island":3,"Mountain":3,"Swamp":3})
                self.assertTrue(all(q==1 or n in BASICS for n,q in cards.items()))
                self.assertEqual(sum("[Commander]" in x for x in lines),1)

    def test_selected_real_seven_swaps_baseline_source_and_combo_core(self):
        _,old=physical(BASE)
        _,new=physical(REV2)
        self.assertEqual(set((new-old).elements()),ADDS)
        self.assertEqual(set((old-new).elements()),CUTS)
        self.assertEqual(sum((new-old).values()),7)
        self.assertEqual(sum((old-new).values()),7)
        self.assertTrue(PROTECTED.issubset(new))
        self.assertIn("Talisman of Dominance",new)
        self.assertIn("Talisman of Creativity",new)
        self.assertNotIn("Bedevil",new)
        self.assertIn("Feed the Swarm",new)

    def test_source_bound_live_oracle_legal_identity_and_games_changers(self):
        self.assertEqual(len(self.live["cards"]),6)
        for name,expected_id in NEW_NAMES.items():
            self.assertEqual(self.oracle[name]["oracle_id"],expected_id)
            self.assertEqual(self.oracle[name]["commander_legality"],"legal")
        _,selected=physical(REV2)
        self.assertEqual(len(selected),94)
        self.assertTrue(all(n in self.oracle for n in selected))
        for name in selected:
            x=self.oracle[name]
            self.assertEqual(x["commander_legality"],"legal",name)
            self.assertTrue(set(x["color_identity"]).issubset({"U","B","R"}),name)
        GC={n for n in selected if self.oracle[n].get("game_changer")}
        self.assertEqual(GC,{"Cyclonic Rift","Demonic Tutor","Fierce Guardianship",
                             "Jeska's Will","Mystical Tutor","Underworld Breach",
                             "Vampiric Tutor"})
        self.assertEqual(len(GC),7)

    def test_front_face_land_rock_counts_each_full_portfolio(self):
        expected={BASE:(34,9),GROK:(33,6),REV2:(34,7),FIVE:(34,7),HIGH:(34,8)}
        for path,(land_count,rock_count) in expected.items():
            with self.subTest(file=path.name):
                _,x=physical(path)
                land=sum(q for n,q in x.items() if
                         "Land" in self.oracle[n]["type_line"].split(" // ")[0])
                rock=sum(x[n] for n in ROCKS)
                self.assertEqual((land,rock),(land_count,rock_count))
                self.assertEqual(land+rock,land_count+rock_count)
        self.assertTrue(set(["Underground Sea","Watery Grave","Steam Vents",
                             "Volcanic Island","Xander's Lounge"]).issubset(physical(REV2)[1]))

    def test_three_full_alternatives_and_no_empty_five_swap_padding(self):
        _,old=physical(BASE)
        _,five=physical(FIVE)
        _,high=physical(HIGH)
        self.assertEqual(sum((five-old).values()),5)
        self.assertEqual(sum((old-five).values()),5)
        self.assertEqual(sum((high-old).values()),7)
        self.assertEqual(sum((old-high).values()),7)
        self.assertIn("Fellwar Stone",high)
        self.assertNotIn("Deekah, Fractal Theorist",high)
        self.assertIn("Deekah, Fractal Theorist",physical(REV2)[1])

    def test_finite_rules_research_requires_real_payments_and_timing(self):
        miner=self.oracle["Forsaken Miner"]["oracle_text"]
        self.assertIn("Whenever you commit a crime",miner)
        self.assertIn("pay {B}",miner)
        self.assertIn("from your graveyard to the battlefield",miner)
        case=self.oracle["Case of the Stashed Skeleton"]["oracle_text"]
        self.assertIn("create a 2/1 black Skeleton creature token",case)
        self.assertIn("To solve",case)
        self.assertIn("You control no suspected Skeletons",case)
        self.assertIn("at the beginning of your end step",case)
        self.assertIn("Solved — {1}{B}, Sacrifice this Case",case)
        self.assertIn("Activate only as a sorcery",case)
        fable=self.oracle["Fable of the Mirror-Breaker // Reflection of Kiki-Jiki"]
        self.assertEqual(fable["layout"],"transform")
        self.assertIn("Create a 2/2",fable["card_faces"][0]["oracle_text"])
        self.assertIn("nonlegendary creature",fable["card_faces"][1]["oracle_text"])
        self.assertIn("{1}, {T}",fable["card_faces"][1]["oracle_text"])
        self.assertIn("Sacrifice it at the beginning of the next end step",
                      fable["card_faces"][1]["oracle_text"])
        self.assertIn("Forest or Island",self.oracle["Misty Rainforest"]["oracle_text"])
        self.assertIn("deals 1 damage to you",self.oracle["City of Brass"]["oracle_text"])
        self.assertIn("sacrifice an artifact or creature",
                      self.oracle["Deadly Dispute"]["oracle_text"])
        # These assert actual Oracle constraints and documented official release-note
        # interaction evidence; they do not implement the comprehensive game engine.
        memo=MEMO.read_text(encoding="utf-8")
        self.assertIn("outlaws-of-thunder-junction-release-notes",memo)
        self.assertIn("not cast",memo)
        self.assertIn("not permanent removal",memo)

    def test_mana_thresholds_are_bounded_not_win_rate(self):
        baseline=source_prob(43)
        proposed=source_prob(41)
        grok=source_prob(39)
        high=source_prob(42)
        for actual,want in ((baseline,.8393566408938197),(proposed,.8060171502387122),
                            (grok,.7684913234258165),(high,.823207118283408)):
            self.assertAlmostEqual(actual,want,places=12)
        self.assertTrue(baseline>high>proposed>grok)
        self.assertGreater(proposed-grok,.03)
        self.assertLess(baseline-proposed,.04)
        memo=MEMO.read_text(encoding="utf-8")
        self.assertIn("not a multiplayer win rate",memo)
        self.assertIn("not user-approved",memo.lower())

if __name__=="__main__":
    unittest.main()
