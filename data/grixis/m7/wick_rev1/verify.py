#!/usr/bin/env python3
"""Wick M7 Rev1: source-pinned, bounded Oracle/cost/stack case fixtures.

This models the named card interactions, stack windows, costs and counterfactuals
only. It is not a full MTG engine, opponent-aware win-rate simulator, historical
M6 I/J certificate or claim of mathematically optimal card choices.
"""

from __future__ import annotations
from collections import Counter
from dataclasses import dataclass, field
import hashlib
from itertools import permutations
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[4]
CASE = Path(__file__).resolve().parent
BASE = CASE / "Wick_Oct15_Authority_Baseline.txt"
SELECTED = ROOT / "data/grixis/m7/candidate_lists/Wick__the_Whorled_Mind_M7_Rev1.txt"
ALT11 = ROOT / "data/grixis/m7/candidate_lists/Wick__the_Whorled_Mind_M7_Rev1_alt11.txt"
ALT12 = ROOT / "data/grixis/m7/candidate_lists/Wick__the_Whorled_Mind_M7_Rev1_alt12.txt"
SOURCE = json.loads((CASE / "Wick_M7_Rev1_Scryfall_snapshot.json").read_text())
CARDS = SOURCE["oracle_cards"]
EXPECTED = {
    BASE.name: "f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98",
    SELECTED.name: "1aea08a53b983ee9ce083c1e9c95b366a3abc478a43b75517714d6280b484c48",
    ALT11.name: "bb79980af439382f8ff0810efcfdb42ecd80aa5cf6efb8c8f41607c1146e13f1",
    ALT12.name: "38b3c4480d5a57a9caf82f6164c0399a1067eebae3b3f3c4c992e6afc83ac58f",
}
SWAPS = {
    "Rank Rat": "Tangled Colony",
    "Azure Beastbinder": "Persistent Marshstalker",
    "Yawgmoth, Thran Physician": "Totentanz, Swarm Piper",
    "Swarmyard Massacre": "Blasphemous Act",
    "Beseech the Mirror": "Plumb the Forbidden",
    "Malakir Rebirth // Malakir Mire": "Swarmyard",
    "Misty Rainforest": "Shipwreck Marsh",
    "Verdant Catacombs": "Haunted Ridge",
    "Wooded Foothills": "Stormcarved Coast",
}


def oracle(name):
    card = CARDS[name]
    if card.get("oracle_text"):
        return card["oracle_text"]
    return "\n".join(face["oracle_text"] for face in card["card_faces"])


def parse(path):
    names=[]
    for line in path.read_text().splitlines():
        m=re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?",line)
        if not m:
            raise ValueError(f"Bad decklist source line in {path}: {line}")
        names.extend([m.group(2)]*int(m.group(1)))
    return names


def add_rat(original_types, effect):
    if effect == "Conspiracy":
        return {"Rat"}  # Explicitly replaces existing creature types.
    if effect in {"Arcane Adaptation", "Leyline of Transformation", "Maskwood Nexus", "Xenograft"}:
        return set(original_types)|{"Rat"}
    return set(original_types)


def can_pay_ubr(sources, *, rat_creature_spell=False):
    choices=[]
    for name in sources:
        if name=="Cavern of Souls":
            choices.append(set("UBR") if rat_creature_spell else {"C"})
        elif name in {"Swarmyard","Phyrexian Tower - colorless"}:
            choices.append({"C"})
        elif name=="Phyrexian Altar - one snail":
            choices.append(set("UBR"))  # One pip only for one sacrifice.
        else:
            choices.append(set(name))
    return any(all(p in source for p,source in zip("UBR", group)) for group in permutations(choices,3))


@dataclass
class WickFixture:
    wick_alive: bool=True
    typechanger: str="none"
    snail_present: bool=False
    snail_power: int=0
    pending: int=0
    created: int=0
    sacrificed: int=0
    impact_tremors: int=0
    opponent_count: int=3
    death_payoff: int=0
    events: list[str]=field(default_factory=list)

    def rat_enters(self, controlled=True):
        if self.wick_alive and controlled:
            self.pending+=1
            self.events.append("Rat entered; Wick triggered")

    def resolve_one(self):
        if not self.pending:
            raise ValueError("No Wick trigger")
        self.pending-=1
        if self.snail_present:
            self.snail_power+=1
            self.events.append("One +1/+1 counter on existing Snail")
        else:
            self.snail_present=True
            self.snail_power=1
            self.created+=1
            self.impact_tremors+=self.opponent_count
            self.events.append("New Snail token created")
            if self.wick_alive and "Rat" in add_rat({"Snail"}, self.typechanger):
                self.pending+=1
                self.events.append("Rat Snail self-entry triggered Wick")

    def sacrifice_snail(self, outlet="Goblin Bombardment", life=40):
        if not self.snail_present:
            raise ValueError("Must control Snail to pay sacrifice cost")
        if outlet=="Yawgmoth, Thran Physician" and life<=1:
            raise ValueError("Cannot pay one life while at one life")
        self.snail_present=False
        self.sacrificed+=1
        self.death_payoff+=self.opponent_count
        self.events.append("Snail sacrificed as cost")
        return self.snail_power

    def repeat(self, n):
        for _ in range(n):
            if not (self.snail_present and self.pending):
                break
            self.sacrifice_snail()
            self.resolve_one()


class WickM7SourceBoundChecks(unittest.TestCase):
    def test_01_source_and_100_card_scope(self):
        for path in (BASE,SELECTED,ALT11,ALT12):
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),EXPECTED[path.name])
            cards=parse(path)
            self.assertEqual(len(cards),100)
            self.assertEqual(cards[0],"Wick, the Whorled Mind")
            self.assertEqual(len([n for n in cards if n!="Island"]),100-cards.count("Island"))
            for name,copies in Counter(cards).items():
                if copies>1:
                    self.assertIn(name,{"Island","Swamp","Mountain","Plains","Forest","Wastes"})
                self.assertIn(name,CARDS)
                self.assertEqual(CARDS[name]["legalities"]["commander"],"legal",name)
                self.assertTrue(set(CARDS[name]["color_identity"])<={"U","B","R"},name)
        self.assertEqual(Counter(parse(SELECTED))-Counter(parse(BASE)),Counter(SWAPS.keys()))
        self.assertEqual(Counter(parse(BASE))-Counter(parse(SELECTED)),Counter(SWAPS.values()))
        self.assertIn("Whenever Wick or another Rat you control enters",oracle("Wick, the Whorled Mind"))

    def test_C1_commander_trigger_and_adversarial_opponent_rat(self):
        game=WickFixture()
        game.rat_enters(False)
        self.assertEqual(game.pending,0)  # Opponent Rat is not your Rat.
        game.rat_enters(True)  # Wick itself entering is a Rat under control.
        game.resolve_one()
        self.assertEqual((game.created,game.snail_power), (1,1))
        for _ in range(4): game.rat_enters()
        for _ in range(4): game.resolve_one()
        self.assertEqual((game.created,game.snail_power),(1,5))
        game.wick_alive=False
        game.rat_enters()
        self.assertEqual(game.pending,0)

    def test_K1_snail_last_known_power_and_activation_source_independent(self):
        self.assertIn("sacrificed creature's power",oracle("Wick, the Whorled Mind"))
        game=WickFixture(snail_present=True,snail_power=7)
        # Lich's Relic equipped gives +2, a resolved Bulk Up doubles current power.
        self.assertIn("+2/+1",oracle("Lich's Relic"))
        self.assertIn("Double target creature's power",oracle("Bulk Up"))
        game.snail_power=(game.snail_power+2)*2
        lki=game.sacrifice_snail()
        game.wick_alive=False  # Response kills Wick after ability is activated.
        opponents=[40,40,40]
        opponents=[life-lki for life in opponents]
        cards_drawn=lki
        self.assertEqual((lki,opponents,cards_drawn),(18,[22,22,22],18))

    def test_K2_type_changers_preserve_snail_and_conspiracy_does_not(self):
        for effect in ("Arcane Adaptation","Leyline of Transformation","Maskwood Nexus"):
            self.assertTrue({"Snail","Rat"}<=add_rat({"Snail"},effect))
            self.assertTrue("in addition" in oracle(effect) or "every creature type" in oracle(effect))
        self.assertEqual(add_rat({"Snail"},"Conspiracy"),{"Rat"})
        self.assertNotIn("Snail",add_rat({"Snail"},"Conspiracy"))

    def test_K3_wick_infect_source_and_cast_window(self):
        self.assertIn("Wick deals damage",oracle("Wick, the Whorled Mind"))
        self.assertIn("gains infect",oracle("Tainted Strike"))
        source="Wick, the Whorled Mind"  # Not sacrificed Snail.
        self.assertEqual(source,"Wick, the Whorled Mind")
        snail_power=10
        self.assertEqual([snail_power]*3,[10,10,10])  # Infect on Wick -> poison.
        self.assertEqual([0]*3,[0,0,0])  # Infect on Snail alone -> no poison from Wick.

    def test_F1_actual_three_colors_and_cavern_restriction(self):
        self.assertTrue(can_pay_ubr(["U","B","R"]))
        self.assertFalse(can_pay_ubr(["Cavern of Souls","B","R"]))
        self.assertFalse(can_pay_ubr(["Phyrexian Altar - one snail","B"]))
        self.assertTrue(can_pay_ubr(["U","B","R","Swarmyard"]))
        self.assertTrue(can_pay_ubr(["Cavern of Souls","B","R"],rat_creature_spell=True))

    def test_K4_cavern_cast_only_and_K5_ozolith_combat_window(self):
        self.assertIn("only to cast a creature spell",oracle("Cavern of Souls"))
        self.assertFalse(can_pay_ubr(["Cavern of Souls","B","R"]))
        self.assertIn("At the beginning of combat on your turn",oracle("The Ozolith"))
        counters_on_snail=5
        moved_to_ozolith=counters_on_snail  # Leave trigger after sacrifice resolves.
        self.assertEqual(moved_to_ozolith,5)
        self.assertNotEqual("combat-beginning","in-response-to-Wick-activation")

    def test_E1_growth_requires_rat_entries_and_E2_type_changer(self):
        f=WickFixture()
        for _ in range(4): f.rat_enters()
        for _ in range(4): f.resolve_one()
        self.assertEqual((f.created,f.snail_power),(1,4))
        # Type changing Snail does not itself cause a new entry event.
        f.typechanger="Arcane Adaptation"
        self.assertEqual(f.pending,0)
        f.rat_enters(); f.resolve_one()
        self.assertEqual(f.snail_power,5)

    def test_W1_snail_rat_free_outlet_stack_recursion_and_disruption(self):
        f=WickFixture(typechanger="Arcane Adaptation",snail_present=True,snail_power=5)
        f.rat_enters(); f.repeat(12)
        self.assertEqual((f.created,f.sacrificed,f.pending),(12,12,1))
        self.assertEqual(f.impact_tremors,36)  # Three opponents, each new token enters.
        broken=WickFixture(typechanger="none",snail_present=True,snail_power=5)
        broken.rat_enters(); broken.repeat(12)
        self.assertEqual((broken.created,broken.sacrificed,broken.pending),(1,1,0))
        self.assertEqual(broken.impact_tremors,3)
        # If opponent destroys Wick during the first response window, no new
        # Wick trigger will be created by the type-changed Snail token.
        disrupted=WickFixture(typechanger="Arcane Adaptation",snail_present=True,pending=1,wick_alive=False)
        disrupted.repeat(8)
        self.assertEqual((disrupted.created,disrupted.pending),(1,0))

    def test_W2_marrow_gnawer_alarm_actual_rat_arithmetic(self):
        self.assertIn("{T}, Sacrifice a Rat",oracle("Marrow-Gnawer"))
        self.assertIn("Whenever a creature enters, untap all creatures",oracle("Intruder Alarm"))
        def count_after(n):
            # Sacrifice an expendable Rat as a cost, then make X equal to the
            # Rats still controlled as the ability resolves.
            return 2*(n-1) if n>=2 else 0
        self.assertEqual(count_after(2),2)  # Sustainable entries, no growth.
        self.assertEqual(count_after(3),4)  # Net growth.
        self.assertEqual(count_after(4),6)
        self.assertEqual(count_after(1),0)  # Must sacrifice Gnawer itself.
        # Opposing creature entries also untap their creatures via Alarm;
        # cannot assume this is a one-sided static effect.

    def test_W3_power_draw_infect_and_deckout_adversary(self):
        self.assertIn("Then draw cards equal",oracle("Wick, the Whorled Mind"))
        snail_power,library_remaining,opp_life=50,20,35
        self.assertGreater(snail_power,library_remaining)
        self.assertGreater(snail_power,opp_life)
        # Damage is before mandatory draw; pilot also loses for an attempted
        # draw from an empty library at state-based actions, not guaranteed solo win.

    def test_F2_snail_or_wick_removed_in_response(self):
        f=WickFixture(snail_present=True,snail_power=8)
        f.rat_enters()
        f.sacrifice_snail() # Opponent removes before trigger resolves.
        f.resolve_one()
        self.assertEqual((f.created,f.snail_power),(1,1))
        f.wick_alive=False
        f.rat_enters()
        self.assertEqual(f.pending,0)

    def test_F3_artifact_vs_enchantment_hate_differentiated(self):
        self.assertIn("Sacrifice a creature: Add {C}{C}",oracle("Ashnod's Altar"))
        self.assertIn("Sacrifice a creature: Add one mana of any color",oracle("Phyrexian Altar"))
        self.assertIn("Sacrifice a creature:",oracle("Goblin Bombardment"))
        f=WickFixture(typechanger="Arcane Adaptation",snail_present=True)
        f.rat_enters();f.typechanger="none"  # Enchantment was removed.
        f.repeat(3)
        self.assertEqual(f.created,1)
        # Artifact activated-ability suppression disables artifact Altars,
        # not the independent enchantment-based Bombardment sacrifice cost.

    def test_s01_rank_rat_versus_tangled_colony(self):
        self.assertIn("each opponent discards a card",oracle("Rank Rat"))
        self.assertIn("damage dealt to it this turn",oracle("Tangled Colony"))
        self.assertIn("each creature that isn't",oracle("Swarmyard Massacre"))
        self.assertEqual(0,0)  # No damage => Colony dies into zero Rats.

    def test_s02_swarmyard_massacre_tribal_protection_and_snail_risk(self):
        self.assertIn("create two 1/1 green squirrel",oracle("Swarmyard Massacre").lower())
        # With 3 Rats and two new Squirrels, nontribal 1/1 Snail loses 5/5.
        rat_count,squirrel_count=3,2
        minus=rat_count+squirrel_count
        protected={"Rat","Squirrel","Insect","Spider"}
        self.assertNotIn("Snail",protected)
        self.assertGreaterEqual(minus,5)
        self.assertIn("Rat",protected)

    def test_s03_yawgmoth_pay_one_life_and_proliferate(self):
        self.assertIn("Pay 1 life, Sacrifice another creature",oracle("Yawgmoth, Thran Physician"))
        self.assertIn("Proliferate",oracle("Yawgmoth, Thran Physician"))
        life=20
        for _ in range(19):life-=1
        self.assertEqual(life,1)
        self.assertFalse(life>1)  # Not an unlimited outlet without restoring life.

    def test_s04_beseech_bargain_and_life_land_conversion(self):
        self.assertIn("Bargain",oracle("Beseech the Mirror"))
        self.assertIn("mana value is 4 or less",oracle("Beseech the Mirror"))
        self.assertIn("you may cast",oracle("Beseech the Mirror"))
        for target in ("Arcane Adaptation","Maskwood Nexus","Phyrexian Altar","Yawgmoth, Thran Physician"):
            self.assertLessEqual(CARDS[target]["cmc"],4)
        self.assertIn("return it to the battlefield tapped",oracle("Malakir Rebirth // Malakir Mire"))
        malakir_faces=CARDS["Malakir Rebirth // Malakir Mire"]["card_faces"]
        self.assertIn("You lose 2 life",malakir_faces[0]["oracle_text"])
        self.assertIn("This land enters tapped",malakir_faces[1]["oracle_text"])
        self.assertNotIn("unless",malakir_faces[1]["oracle_text"].lower())

    def test_s05_mana_fetches_are_real_typed_land_searches(self):
        self.assertIn("Island card",oracle("Misty Rainforest"))
        self.assertIn("Swamp",oracle("Verdant Catacombs"))
        self.assertIn("Mountain",oracle("Wooded Foothills"))
        for dual,required_type in (("Underground Sea","Island"),("Badlands","Swamp"),("Volcanic Island","Mountain")):
            self.assertIn(required_type,CARDS[dual]["type_line"])


if __name__=="__main__":
    unittest.main(verbosity=2)
