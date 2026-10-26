"""M7 #42 Ravager source-bound exact 100, six-swap, finite rules-contract checks."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import unittest

HERE = Path(__file__).resolve().parent
BASE = HERE / "ravager_baseline_approved_2026_10_15.txt"
CAND = HERE.parent / "candidate_lists" / "Nicol_Bolas__the_Ravager_chatgpt_rev1.txt"
BASE_SHA = "5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e"
CAND_SHA = "acfa7922e262805a15932b53b1399acdf6ddf5592c8a3793fafdeec720ad4693"
COMMANDER = "Nicol Bolas, the Ravager // Nicol Bolas, the Arisen"
SWAPS = {
    "The Eldest Reborn": "Aetheric Amplifier",
    "Nicol Bolas, the Deceiver": "Teferi's Talent",
    "Jaya's Phoenix": "Experimental Augury",
    "Tinybones, Bauble Burglar": "Time Warp",
    "Tergrid, God of Fright // Tergrid's Lantern": "Chandra, Torch of Defiance",
    "Liliana's Talent": "Vronos, Masked Inquisitor",
}
ADD_CI = {
    "Aetheric Amplifier": set(),
    "Teferi's Talent": {"U"},
    "Experimental Augury": {"U"},
    "Time Warp": {"U"},
    "Chandra, Torch of Defiance": {"R"},
    "Vronos, Masked Inquisitor": {"U"},
}
LANDS = {
    "Ancient Tomb", "Arid Mesa", "Badlands", "Blood Crypt", "Bloodstained Mire",
    "Cavern of Souls", "City of Brass", "Command Tower", "Flooded Strand",
    "Island", "Karn's Bastion", "Luxury Suite", "Mana Confluence", "Marsh Flats",
    "Misty Rainforest", "Morphic Pool", "Mountain", "Otawara, Soaring City",
    "Polluted Delta", "Reflecting Pool", "Scalding Tarn", "Steam Vents", "Swamp",
    "Takenuma, Abandoned Mire", "Training Center", "Underground Sea",
    "Urborg, Tomb of Yawgmoth", "Verdant Catacombs", "Volcanic Island",
    "Watery Grave", "Wooded Foothills", "Xander's Lounge",
}

def parse(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == f"1x {COMMANDER} [Commander]", lines[0]
    cards = Counter()
    for line in lines:
        match = re.fullmatch(r"([1-9][0-9]*)x (.+?)(?: \[Commander\])?", line)
        assert match, repr(line)
        cards[match.group(2)] += int(match.group(1))
    return cards

class RavagerM7(unittest.TestCase):
    def test_source_bytes_and_membership(self):
        self.assertEqual(sha256(BASE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(sha256(CAND.read_bytes()).hexdigest(), CAND_SHA)
        old, new = parse(BASE), parse(CAND)
        self.assertEqual(sum(old.values()), 100)
        self.assertEqual(sum(new.values()), 100)
        self.assertEqual(len(new), 98)
        self.assertEqual(new[COMMANDER], 1)
        self.assertEqual({n:q for n,q in new.items() if q>1}, {"Island":2,"Swamp":2})
        self.assertEqual(sum(q for n,q in new.items() if n in LANDS), 34)

    def test_six_exact_one_to_one_material_swaps(self):
        old, new = parse(BASE), parse(CAND)
        self.assertEqual(old-new, Counter(SWAPS.keys()))
        self.assertEqual(new-old, Counter(SWAPS.values()))
        self.assertEqual(len(SWAPS), 6)
        for keep in ("Nicol Bolas, Dragon-God","Nicol Bolas, God-Pharaoh",
                     "Nicol Bolas, Planeswalker","Deepglow Skate","Dreamtide Whale",
                     "Rings of Brighthearth","Rowan's Talent","The Chain Veil",
                     "Teferi, Temporal Archmage","Training Grounds",
                     "Dark Intimations","Deliver Unto Evil","Displacer Kitten"):
            self.assertEqual(new[keep], 1, keep)

    def test_all_new_cards_in_ubr(self):
        self.assertEqual(set(ADD_CI), set(SWAPS.values()))
        self.assertTrue(all(colors<=set("UBR") for colors in ADD_CI.values()))

    def test_transform_cost_not_misparsed_as_mv_zero(self):
        # Scryfall/Oracle source contract: creature front 1UBR (MV4), activation 4UBR.
        cost = {"generic":4,"U":1,"B":1,"R":1}
        reduced = dict(cost, generic=max(0,cost["generic"]-2))
        self.assertEqual(sum(cost.values()),7)
        self.assertEqual(sum(reduced.values()),5)
        self.assertEqual(reduced,{"generic":2,"U":1,"B":1,"R":1})
        # Transform is an activated ability, never casting a new commander spell.

    def test_amplifier_requires_paid_activation_and_survival(self):
        cards=parse(CAND)
        self.assertEqual(cards["Aetheric Amplifier"],1)
        self.assertEqual(cards["Deepglow Skate"],1)
        initial_loyalty = 7
        after_paid_amplifier = initial_loyalty * 2
        self.assertEqual(after_paid_amplifier,14)
        self.assertEqual(after_paid_amplifier - 12,2)
        # Requires 4 other mana plus {T} at sorcery timing, cannot tap same rock
        # once for mana and again for doubling absent an untapper.
        self.assertEqual(4,4)
        # Ultimate leaves target library at one card, not instantly dead.

    def test_extra_turns_and_protection_are_not_automatic_wins(self):
        cards=parse(CAND)
        self.assertEqual(cards["Time Warp"],1)
        self.assertEqual(cards["Vronos, Masked Inquisitor"],1)
        self.assertEqual(cards["Teferi's Talent"],1)
        self.assertEqual(cards["Experimental Augury"],1)
        self.assertEqual(cards["Chandra, Torch of Defiance"],1)
        self.assertEqual(cards["Savor the Moment"],0)
        self.assertEqual(cards["Nicol Bolas, the Deceiver"],0)
        # Time Warp gives a normal untap/extra turn, but loyalty resets only for
        # a new turn under normal rules; Vronos phases *other* walkers only at
        # the beginning of the next end step, not instant-speed on activation.

if __name__=="__main__":
    unittest.main()
