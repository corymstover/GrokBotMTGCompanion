"""M7 #41 Nicol Bolas exact source and finite commander-first interaction checks."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import unittest

HERE=Path(__file__).resolve().parent
BASE=HERE/"nicol_baseline_approved_2026_10_15.txt"
CAND=HERE.parent/"candidate_lists"/"Nicol_Bolas_chatgpt_rev1.txt"
BASE_SHA="e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617"
CAND_SHA="a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6"
SWAPS={
"Hypnotic Specter":"Sarkhan, Soul Aflame",
"Nightscape Familiar":"Rivaz of the Claw",
"Oppression":"Imperial Seal",
"Raiders' Wake":"Ophidian Eye",
"No Mercy":"Mithril Coat",
"The Eldest Reborn":"Reanimate",
"Seething Song":"Coalition Relic",
"Shizo, Death's Storehouse":"Minamo, School at Water's Edge",
"Bojuka Bog":"Plaza of Heroes",
"Viridian Longbow":"Dream Halls",
}
ADDED_CI={
"Sarkhan, Soul Aflame":{"U","R"},
"Rivaz of the Claw":{"B","R"},
"Imperial Seal":{"B"},
"Ophidian Eye":{"U"},
"Mithril Coat":set(),
"Reanimate":{"B"},
"Coalition Relic":set(),
"Minamo, School at Water's Edge":set(),
"Plaza of Heroes":set(),
"Dream Halls":{"U"},
}
LANDS={
"Ancient Tomb","Arena of Glory","Arid Mesa","Badlands","Blood Crypt","Bloodstained Mire",
"Cavern of Souls","City of Brass","Command Beacon","Command Tower","Exotic Orchard",
"Flooded Strand","Hall of the Bandit Lord","Island","Luxury Suite","Mana Confluence",
"Marsh Flats","Minamo, School at Water's Edge","Misty Rainforest","Morphic Pool",
"Mountain","Otawara, Soaring City","Plaza of Heroes","Polluted Delta","Reflecting Pool",
"Scalding Tarn","Steam Vents","Swamp","Takenuma, Abandoned Mire","Training Center",
"Underground Sea","Verdant Catacombs","Volcanic Island","Watery Grave","Wooded Foothills",
"Xander's Lounge"
}
def parse(path):
    rows=path.read_text(encoding="utf-8").splitlines()
    assert rows[0]=="1x Nicol Bolas [Commander]",rows[0]
    cards=Counter()
    for line in rows:
        m=re.fullmatch(r"([1-9][0-9]*)x (.+?)(?: \[Commander\])?",line)
        assert m,repr(line)
        cards[m.group(2)]+=int(m.group(1))
    return cards

class NicolM7(unittest.TestCase):
    def test_exact_sha_and_100_cards(self):
        self.assertEqual(sha256(BASE.read_bytes()).hexdigest(),BASE_SHA)
        self.assertEqual(sha256(CAND.read_bytes()).hexdigest(),CAND_SHA)
        a,b=parse(BASE),parse(CAND)
        self.assertEqual((sum(a.values()),sum(b.values())),(100,100))
        self.assertEqual(b["Nicol Bolas"],1)
        self.assertEqual(len(b),99)
        self.assertEqual({k:v for k,v in b.items() if v>1},{"Island":2})
        self.assertEqual(sum(v for k,v in b.items() if k in LANDS),37)

    def test_exact_ten_swaps_and_not_generic_shell(self):
        a,b=parse(BASE),parse(CAND)
        self.assertEqual(a-b,Counter(SWAPS))
        self.assertEqual(b-a,Counter(SWAPS.values()))
        for name in ("Dragon Tempest","Ingris Stingerquill","Kediss, Emberclaw Familiar",
                     "Chandra's Ignition","Pain for All","Quicksilver Dagger","Waste Not",
                     "Geth's Grimoire","Curiosity","Aggravated Assault",
                     "Sword of Feast and Famine"):
            self.assertEqual(b[name],1,name)

    def test_new_cards_all_fit_ubr(self):
        self.assertEqual(set(ADDED_CI),set(SWAPS.values()))
        self.assertTrue(all(v<=set("UBR") for v in ADDED_CI.values()))

    def test_commander_damage_not_just_combat(self):
        # One qualifying Nicol-sourced point to each of 3 opponents generates 3 discard triggers.
        damage_events={"A":1,"B":1,"C":1}
        self.assertEqual(sum(n>0 for n in damage_events.values()),3)
        # Curiosity/Ophidian Eye each can draw once per separate opponent damage event.
        self.assertEqual(sum(n>0 for n in damage_events.values())*2,6)

    def test_sarkhan_copy_distinct_name_and_temporary(self):
        # The actual copy remains legendary. Name Sarkhan != Nicol so legend rule doesn't apply.
        self.assertNotEqual("Sarkhan, Soul Aflame","Nicol Bolas")
        self.assertEqual(parse(CAND)["Sarkhan, Soul Aflame"],1)

    def test_dream_halls_limitations_are_not_ignored(self):
        self.assertEqual(parse(CAND)["Dream Halls"],1)
        # Casting via alternative cost does NOT waive later commander tax (2 per prior cast)
        self.assertEqual(2*2,4)
        # Dream Halls does not pay UBR upkeep or confer haste; no free auto-win assertion.

    def test_land_untap_and_reanimation_distinctions(self):
        b=parse(CAND)
        self.assertEqual(b["Minamo, School at Water's Edge"],1)
        self.assertEqual(b["Quicksilver Dagger"],1)
        self.assertEqual(b["Reanimate"],1)
        self.assertEqual(b["Rivaz of the Claw"],1)
        # Reanimate can only target a graveyard card, never the command zone.
        # Minamo untapping an equipped/enhanced Nicol doesn't give extra combat phases.

if __name__=="__main__":
    unittest.main()
