"""Research-only Admiral stage4 EDHREC additional packages: exact 100, source + timing.

Finite adverse bounds, not multiplayer outcome, selected M6 I/J candidate or approval.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"data/grixis/m7/research_challengers"
CANONICAL=ROOT/"data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
SOURCE=DIR/"Admiral_Beckett_Brass_seven_Regalia_Wave_20261022.txt"
ORACLE=DIR/"Admiral_Beckett_Brass_EDHREC_inclusion_lift_discovery_20261022.json"
FILES={
 "AERIALIST":("Admiral_Beckett_Brass_eight_Aerialist_20261022.txt",{"Kari Zev, Skyship Raider":"Storm Fleet Aerialist"},8),
 "DREAMCALLER":("Admiral_Beckett_Brass_eight_Dreamcaller_20261022.txt",{"Open into Wonder":"Dreamcaller Siren"},8),
 "BOTH":("Admiral_Beckett_Brass_nine_Aerialist_Dreamcaller_20261022.txt",{"Kari Zev, Skyship Raider":"Storm Fleet Aerialist","Open into Wonder":"Dreamcaller Siren"},9),
}
CANONICAL_SHA="4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"

def cards(path):
    raw=path.read_bytes()
    lines=raw.decode("utf-8").splitlines()
    quantities=Counter()
    for row in lines:
        if not row.strip():
            continue
        number,name=row.split("x ",1)
        quantities[name.replace(" [Commander]","")]+=int(number)
    return quantities,lines,hashlib.sha256(raw).hexdigest()

class Stage4Research(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.canonical,_,cls.canonical_hash=cards(CANONICAL)
        cls.source,_,cls.source_hash=cards(SOURCE)
        cls.oracle={c["name"]:c for c in json.loads(ORACLE.read_text(encoding="utf-8"))["scryfall_new_discovery_oracle"]}

    def test_frozen_approved_source_and_distinct_physical_lists(self):
        self.assertEqual(self.canonical_hash,CANONICAL_SHA)
        hashes=set()
        for label,(filename,swaps,target) in FILES.items():
            result,rows,sha=cards(DIR/filename)
            self.assertEqual(sum(result.values()),100,label)
            self.assertEqual(result["Admiral Beckett Brass"],1,label)
            self.assertEqual(rows[0],"1x Admiral Beckett Brass [Commander]",label)
            self.assertTrue(all(q==1 or n in {"Island","Mountain","Swamp"}
                                for n,q in result.items()),label)
            expected=self.source.copy()
            for cut,add in swaps.items():
                self.assertEqual(expected[cut],1,(label,cut))
                expected.subtract({cut:1})
                expected.update({add:1})
            self.assertEqual(result,expected,label)
            self.assertEqual(sum((result-self.canonical).values()),target,label)
            self.assertEqual(sum((self.canonical-result).values()),target,label)
            hashes.add(sha)
        self.assertEqual(len(hashes),len(FILES))

    def test_new_combat_pirates_source_legal_and_exact_cost(self):
        air=self.oracle["Storm Fleet Aerialist"]
        siren=self.oracle["Dreamcaller Siren"]
        for record in (air,siren):
            self.assertEqual(record["commander_legality"],"legal")
            self.assertTrue(set(record["color_identity"])<= {"B","U","R"})
        self.assertEqual(air["mana_cost"],"{1}{U}")
        self.assertIn("if you attacked this turn",air["oracle_text"])
        self.assertEqual(siren["mana_cost"],"{2}{U}{U}")
        self.assertIn("Flash",siren["oracle_text"])
        self.assertIn("if you control another Pirate",siren["oracle_text"])
        self.assertIn("tap up to two target nonland permanents",siren["oracle_text"])

    def test_tapped_blockers_exactly_two_does_not_guarantee_three_hits(self):
        # Conservative finite blockers count; Dreamcaller tapping two at
        # pre-blockers window leaves two eligible blockers if four were ready.
        pirate_attackers=3
        enemy_ready_blockers=4
        enemy_tapped_by_siren=min(2,enemy_ready_blockers)
        remaining=enemy_ready_blockers-enemy_tapped_by_siren
        self.assertEqual(remaining,2)
        hits=max(0,pirate_attackers-remaining)
        self.assertEqual(hits,1)
        self.assertLess(hits,3)

    def test_raid_counter_not_same_turn_automatic_combat_hit(self):
        # Aerialist has no innate haste; a Pirate played post-combat with Raid
        # qualifies as countered body later, never retroactively as a third
        # Pirate damage source in the already-resolved combat.
        attacks_this_turn=True
        creature_was_on_battlefield_for_attackers=False
        raid_counter_on_entry=attacks_this_turn
        same_combat_pirate_hit=creature_was_on_battlefield_for_attackers
        self.assertTrue(raid_counter_on_entry)
        self.assertFalse(same_combat_pirate_hit)

    def test_no_owner_promotion_on_more_swap_configs(self):
        snapshot=json.loads(ORACLE.read_text(encoding="utf-8"))
        self.assertEqual(snapshot["status"],"RESEARCH_ONLY_DISCOVERY_NOT_OWNER_READY")
        self.assertNotIn("OWNER_READY", {x["judgment"] for x in snapshot["scryfall_new_discovery_oracle"]})

if __name__=="__main__":
    unittest.main()
