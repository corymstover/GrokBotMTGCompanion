"""Stage18 decision-grade deterministic adversarial comparison; never certifies M6 I/J."""
import hashlib
import json
from collections import Counter
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "data/grixis/m6/certification_preflight/Abaddon_stage18_candidate_specific_mana_redteam_pool_20261023.json").read_text())

def physical(path):
    blob=(ROOT/path).read_bytes()
    cards=Counter()
    for line in blob.decode().splitlines():
        qty, name=line.split("x ", 1)
        name=name.removesuffix(" [Commander]")
        cards[name]+=int(qty)
    assert sum(cards.values())==100
    return cards, hashlib.sha256(blob).hexdigest()

class Stage18Adversarial(unittest.TestCase):
    def test_four_complete_source_lists_and_exact_hashes(self):
        seen=set()
        for config in R["comparison"]:
            cards, actual=physical(config["path"])
            self.assertEqual(actual, config["raw_sha256"])
            self.assertEqual(cards["Abaddon the Despoiler"], 1)
            self.assertEqual(sum(cards.values()), 100)
            self.assertEqual(sum(q for n,q in cards.items() if n in ("Island","Mountain","Swamp")),8)
            self.assertEqual(cards["Noise Marine"],0 if config["swaps"]==7 else 1)
            seen.add(actual)
        self.assertEqual(len(seen),4)
        cards, _=physical(R["candidate_path"])
        self.assertEqual(cards["Ponder"],0)
        self.assertEqual(cards["Sheoldred, the Apocalypse"],1)
        self.assertEqual(cards["Nightscape Familiar"],1)
        self.assertEqual(cards["Nalfeshnee"],1)
        self.assertEqual(cards["Call Forth the Tempest"],1)
        self.assertEqual(cards["Loyal Subordinate"],1)
        self.assertEqual(cards["Aggravated Assault"],1)
        self.assertEqual(cards["Neheb, the Eternal"],1)

    def test_reproducibility_scope_and_comparator_integrity(self):
        _, candidate=physical(R["candidate_path"])
        self.assertEqual(candidate,R["candidate_raw_sha256"])
        self.assertEqual(R["source_bound_full_oracle"],"data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Stage17_95_Source_Reconciled_20261023.json")
        o=json.loads((ROOT/R["source_bound_full_oracle"]).read_text())
        self.assertEqual(o["candidate_sha256"],candidate)
        self.assertEqual(len(o["oracle_cards"]),95)
        s15=json.loads((ROOT/R["source_receipts"][2]).read_text())
        self.assertEqual(len(s15["cases"]),R["stage15_changed_case_pass"])
        s16=json.loads((ROOT/R["source_receipts"][3]).read_text())
        self.assertEqual(s16["counts"]["historical_p0"],R["stage16_historical_p0_total"])
        self.assertEqual(s16["counts"]["historical_p0_card_cut_dependent"],R["stage16_historical_p0_removed_card_counterfactual"])
        self.assertEqual(R["stage16_historical_p0_only_potentially_reusable"],77)
        self.assertEqual(R["stage16_historical_p1_counterfactual"],3)
        self.assertFalse(R["m6_j_complete"])
        self.assertEqual(R["m6_i_local_best"],"NOT_YET_PASS")
        self.assertFalse(R["owner_ready"])
        self.assertFalse(R["owner_approval"])
        self.assertFalse(R["canon_changed"])
        self.assertTrue(R["deck3_hold"])

    def test_source_paid_counterplay_not_overstated(self):
        cases={c["id"]:c for c in R["deterministic_adverse_cases"]}
        self.assertEqual(len(cases),8)
        self.assertFalse(cases["COLOR_BB_ON_FOUR"]["sheoldred_castable"])
        self.assertEqual(cases["COMMANDER_REMOVED_PRECOPY"]["extra_commander_static_cascade_grants"],0)
        self.assertEqual(cases["SANCTUM_REMOVED_BEFORE_MAIN_TRIGGER_RESOLUTION"]["opponents_life_lost_from_sanctum"],0)
        self.assertEqual(cases["SHEOLDRED_WHEEL_UNCONTESTED"]["sheoldred_opponent_life_lost"],42)
        self.assertEqual(cases["SHEOLDRED_WHEEL_REMOVAL"]["sheoldred_opponent_life_lost"],0)
        self.assertEqual(cases["RULE_OF_LAW"]["additional_cascade_hit_casts_allowed"],0)
        self.assertEqual(cases["MOUNT_DOOM_NO_RESOURCES"]["mount_doom_all_opponent_damage_events"],0)
        self.assertEqual(cases["IGNUS_4_CARD_SEQUENCE"]["opponent_total_damage_per_reentry_three_opponents"],3)
        self.assertEqual(len(R["cut_costs"]),6)
        self.assertEqual({x["add"] for x in R["cut_costs"]},{"Impact Tremors","Sanctum of Stone Fangs","Coruscation Mage","Sakashima of a Thousand Faces","Mount Doom","Sheoldred, the Apocalypse"})

if __name__ == "__main__":
    unittest.main()
