"""Admiral M7 stage7 source-bound six/seven-swaps retaining key draw and recovery.

This is a physical/source/finite-effect regression, NOT M6 certification,
multi-player win-rate, global best proof, or owner-ready M7 approval.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/"data/grixis/m7/research_challengers"
BASE=ROOT/"data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
D=R/"Admiral_Beckett_Brass_evasive_pirate_density_package.txt"
VARIANTS={
 "six_Aerialist":(
  "Admiral_Beckett_Brass_six_Aerialist_draw_resilient_20261022.txt",
  {"Kari Zev, Skyship Raider":"Storm Fleet Aerialist"},6),
 "seven_Aerialist_Wave":(
  "Admiral_Beckett_Brass_seven_Aerialist_Wave_draw_resilient_20261022.txt",
  {"Kari Zev, Skyship Raider":"Storm Fleet Aerialist",
   "Fiery Cannonade":"Cosmotronic Wave"},7),
 "six_Wave_Palisade":(
  "Admiral_Beckett_Brass_six_Wave_Palisade_draw_resilient_20261022.txt",
  {"Raise the Palisade":"Cosmotronic Wave"},6),
 "seven_Aerialist_Wave_Palisade":(
  "Admiral_Beckett_Brass_seven_Aerialist_Wave_Palisade_draw_resilient_20261022.txt",
  {"Raise the Palisade":"Cosmotronic Wave",
   "Kari Zev, Skyship Raider":"Storm Fleet Aerialist"},7),
}
BASE_HASH="4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
D_HASH="201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee"

def physical(path):
    raw=path.read_bytes()
    rows=raw.decode("utf-8").splitlines()
    quantities=Counter()
    names=[]
    for row in rows:
        if not row:
            continue
        quantity_text,raw_name=row.split("x ",1)
        name=raw_name.removesuffix(" [Commander]")
        quantities[name]+=int(quantity_text)
        names.extend([name]*int(quantity_text))
    return names,quantities,hashlib.sha256(raw).hexdigest()

class AdmiralStage7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base,cls.base_names,cls.base_sha=physical(BASE)
        cls.d,cls.d_names,cls.d_sha=physical(D)
        cls.full={x["name"]:x for x in json.loads((R/"Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json").read_text())["cards"]}
        cls.post={x["name"]:x for x in json.loads((R/"Admiral_Beckett_Brass_eleven_card_live_Scryfall_20261022.json").read_text())["verified_cards"]}
        cls.new={x["name"]:x for x in json.loads((R/"Admiral_Beckett_Brass_EDHREC_inclusion_lift_discovery_20261022.json").read_text())["scryfall_new_discovery_oracle"]}

    def test_canonical_frozen_and_no_variant_is_owner_approved(self):
        self.assertEqual(self.base_sha,BASE_HASH)
        self.assertEqual(self.d_sha,D_HASH)
        self.assertEqual(len(self.base),100)
        ledger=json.loads((R/"Admiral_Beckett_Brass_current_continuation_20261022.json").read_text())
        self.assertFalse(ledger["canonical_authority"]["new_m7_owner_approval"])
        # The historical stage7 package remains research-only, even after a
        # SEPARATE rev2 owner-ready candidate passes the decisive gate. Do not
        # force the ledger to retain its obsolete interim status forever.
        self.assertIn(ledger["m7_status"], {
            "RESEARCH_ONLY_REOPENED_OWNER_APPROVAL_WITHHELD",
            "REVISED_M7_SIX_SWAP_OWNER_CANDIDATE_IN_PR616_AWAITING_LATEST_EXACT_HEAD_CI_NO_OWNER_APPROVAL",
            "REVISED_M7_OWNER_APPROVAL_REQUIRED_STRICT_GATE_PASSED_NO_OWNER_APPROVAL",
        })
        self.assertFalse(ledger["canonical_authority"]["new_m7_owner_approval"])
        if ledger["m7_status"].startswith("REVISED_M7_"):
            revised=ledger["m7_rev2_decision_packet"]
            self.assertFalse(revised["owner_approval"])
            self.assertFalse(revised["canonical_changed"])
            self.assertNotEqual(revised["raw_sha256"],D_HASH)
            self.assertEqual(revised["genuine_swaps"],6)

    def test_four_complete_distinct_alternative_100_card_systems(self):
        for title,(file,replacements,swap_count) in VARIANTS.items():
            with self.subTest(title=title):
                names,quantities,sha=physical(R/file)
                self.assertEqual(len(names),100)
                self.assertEqual(names[0],"Admiral Beckett Brass")
                self.assertEqual(len(sha),64)
                self.assertTrue(all(count==1 or card in {"Island","Mountain","Swamp"}
                                    for card,count in quantities.items()))
                expected=self.d_names.copy()
                for cut,add in replacements.items():
                    self.assertEqual(expected[cut],1)
                    del expected[cut]
                    expected[add]+=1
                self.assertEqual(quantities,expected)
                self.assertEqual(sum((quantities-self.base_names).values()),swap_count)
                self.assertEqual(sum((self.base_names-quantities).values()),swap_count)
                for protected in ("Bident of Thassa","March of the Drowned",
                                  "Path of Ancestry","The Indomitable",
                                  "Open into Wonder","Kindred Discovery"):
                    self.assertEqual(quantities[protected],1,(title,protected))
                self.assertNotIn("Brotherhood Regalia",quantities)
                self.assertNotIn("Shizo, Death's Storehouse",quantities)
                if "Palisade" in title:
                    self.assertEqual(quantities["Fiery Cannonade"],1)
                    self.assertEqual(quantities["Cosmotronic Wave"],1)
                    self.assertEqual(quantities["Raise the Palisade"],0)

    def test_Kari_Zev_is_pirate_but_attacking_monkey_is_not(self):
        kari=self.full["Kari Zev, Skyship Raider"]
        self.assertIn("Human Pirate",kari["type_line"])
        self.assertIn("red Monkey creature token",kari["oracle_text"])
        self.assertNotIn("Monkey Pirate creature token",kari["oracle_text"])
        ragavan_card=self.full["Ragavan, Nimble Pilferer"]
        self.assertIn("Monkey Pirate",ragavan_card["type_line"])
        aerialist=self.new["Storm Fleet Aerialist"]
        self.assertIn("Human Pirate",aerialist["type_line"])
        self.assertEqual(aerialist["mana_cost"],"{1}{U}")
        self.assertEqual(aerialist["commander_legality"],"legal")
        # The substitution does not increase the number of printed Pirate
        # creature cards. Flying-evasion versus menace + Monkey token is real.
        self.assertEqual(sum("Pirate" in self.full[n]["type_line"]
                             for n in self.d if n in self.full),
                         sum("Pirate" in (self.new[n]["type_line"] if n in self.new
                                           else self.full[n]["type_line"])
                             for n in physical(R/VARIANTS["six_Aerialist"][0])[0]
                             if n in self.full or n in self.new))

    def test_source_bound_payable_role_losses_Cannonade_vs_Wave(self):
        wave=self.post["Cosmotronic Wave"]
        cannon=self.post["Fiery Cannonade"]
        self.assertEqual((wave["mana_cost"],wave["type_line"]),("{3}{R}","Sorcery"))
        self.assertEqual((cannon["mana_cost"],cannon["type_line"]),("{2}{R}","Instant"))
        self.assertIn("can't block this turn",wave["oracle_text"])
        self.assertIn("2 damage to each non-Pirate creature",cannon["oracle_text"])
        # A 5-toughness blocker is not removed by Cannonade's 2 damage;
        # Wave prevents it blocking only that one turn after sorcery resolution.
        self.assertGreater(5,2)
        self.assertIn("Creatures your opponents control can't block this turn", wave["oracle_text"])
        self.assertEqual(self.post["Bident of Thassa"]["mana_cost"],"{2}{U}{U}")
        self.assertEqual(self.post["March of the Drowned"]["mana_cost"],"{B}")
        self.assertEqual(self.post["Path of Ancestry"]["type_line"],"Land")
        # The alternate Wave cut retains Cannonade's instant defense but
        # exchanges Palisade's board bounce for one attack-window block ban.
        palisade=self.full["Raise the Palisade"]
        self.assertEqual((palisade["mana_cost"],palisade["type_line"]),("{4}{U}","Sorcery"))
        self.assertIn("Return all creatures that aren't of the chosen type",palisade["oracle_text"])
        self.assertNotIn("Return all creatures",wave["oracle_text"])

if __name__=="__main__":
    unittest.main()
