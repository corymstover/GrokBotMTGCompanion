"""Ashad independent M7 Rev3 exact full 100 and local candidate pool: NO OWNER APPROVAL."""
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

R=Path(__file__).resolve().parents[1]
BASE=R/"data/grixis/m7/baseline_sources/Ashad_the_Lone_Cyberman_approved_source_2026-10-13.txt"
PREF=R/"data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman_ChatGPT_M7_Rev3_Ten_Approval_Candidate.txt"
SNAP=R/"data/grixis/m6/oracle_snapshots/Ashad__the_Lone_Cyberman_M7_Rev3_118_Scryfall_20261023.json"
POOL=R/"data/grixis/m6/ij/tested_pools/Ashad__the_Lone_Cyberman_M7_Rev3_tested_configurations_20261023.json"
RAW="352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267"
LOGICAL="lh1:9ebaa891f2ff0e7af81ff2856b54a012c915f8d5cb1936a8ca579579aa8cb8c9"
ADD={"Skullclamp","Piggy Bank","Razorlash Transmogrant","Necron Deathmark",
     "Royal Warden","Mishra's Workshop","Ancient Tomb","City of Brass",
     "Mana Confluence","Liberator, Urza's Battlethopter"}
CUT={"Fellwar Stone","Reckless Fireweaver","Thoughtcast","Noxious Gearhulk",
     "Thopter Spy Network","Tezzeret, Master of the Bridge","Delete",
     "Crumbling Necropolis","Shipwreck Marsh","Kappa Cannoneer"}

def cards(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    d=Counter()
    for l in lines:
        q,name=l.split("x ",1)
        assert q.isdecimal() and int(q)>0
        d[name.removesuffix(" [Commander]")]+=int(q)
    return lines,d

def logical(path,oracle):
    counts=Counter()
    for l in path.read_text(encoding="utf-8").splitlines():
        q,raw=l.split("x ",1)
        zone="commander" if raw.endswith(" [Commander]") else "main"
        name=raw.removesuffix(" [Commander]")
        counts[(zone,oracle[name]["oracle_id"])]+=int(q)
    canonical="".join(f"{zone}|{oid}|{qty}\n" for (zone,oid),qty in sorted(counts.items()))
    return "lh1:"+hashlib.sha256(canonical.encode("utf-8")).hexdigest()

class AshadM7Rev3IndependentSourceBound(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snap=json.loads(SNAP.read_text())
        cls.oracle={c["name"]:c for c in cls.snap["cards"]}
        cls.pool=json.loads(POOL.read_text())

    def test_exact_hash_and_100_physical_95_names(self):
        self.assertEqual(hashlib.sha256(PREF.read_bytes()).hexdigest(),RAW)
        self.assertEqual(logical(PREF,self.oracle),LOGICAL)
        lines,d=cards(PREF)
        self.assertEqual(lines[0],"1x Ashad, the Lone Cyberman [Commander]")
        self.assertEqual((len(lines),len(d),sum(d.values())),(95,95,100))
        self.assertEqual({n:q for n,q in d.items() if q>1},
                         {"Island":3,"Mountain":2,"Swamp":3})
        self.assertEqual(sum("[Commander]" in line for line in lines),1)
        self.assertEqual(set((d-cards(BASE)[1]).elements()),ADD)
        self.assertEqual(set((cards(BASE)[1]-d).elements()),CUT)
        self.assertIn("Ichor Wellspring",d)
        self.assertIn("Marionette Master",d)
        self.assertIn("Unwinding Clock",d)

    def test_all_selected_current_snapshot_legal_grixis_real_oracle(self):
        self.assertEqual((self.snap["cards_count"],len(self.oracle)),(118,118))
        self.assertEqual(self.snap["candidate_raw_sha256"],RAW)
        self.assertEqual(self.snap["candidate_logical_hash"],LOGICAL)
        self.assertFalse(self.snap["all_commander_legal"],"Pool has deliberately rejected names")
        self.assertEqual(set(self.snap["pool_contains_ineligible_rejected_names"]),
                         {"Bio-Asset Allocator","Golos, Tireless Pilgrim"})
        _,d=cards(PREF)
        self.assertTrue(all(n not in d for n in self.snap["pool_contains_ineligible_rejected_names"]))
        for name in d:
            with self.subTest(card=name):
                self.assertEqual(self.oracle[name]["commander_legality"],"legal")
                self.assertTrue(set(self.oracle[name]["color_identity"]) <= {"U","B","R"})
                self.assertTrue(self.oracle[name]["oracle_id"])
        self.assertEqual({n for n in d if self.oracle[n]["game_changer"]},
                         {"Cyclonic Rift","Demonic Tutor","Fierce Guardianship",
                          "Ancient Tomb","Mishra's Workshop"})
        self.assertIn("as though they had flash",self.oracle["Liberator, Urza's Battlethopter"]["oracle_text"])
        self.assertIn("Legendary Artifact Creature",self.oracle["Liberator, Urza's Battlethopter"]["type_line"])
        self.assertIn("first nonlegendary artifact spell",self.oracle["Ashad, the Lone Cyberman"]["oracle_text"])
        self.assertIn("only to cast artifact spells",self.oracle["Mishra's Workshop"]["oracle_text"])
        self.assertEqual(self.oracle["Liberator, Urza's Battlethopter"]["oracle_id"],
                         "798a4a6f-7443-4e8e-afcb-0a694fdfcbb3")

    def test_five_local_configurations_and_no_authority_upgrade(self):
        p=self.pool
        self.assertEqual(p["explicit_pool_size"],5)
        self.assertFalse(p["owner_m7_approved"])
        self.assertEqual(p["candidate_raw_sha256"],RAW)
        ids=set()
        for cfg in p["configurations"]:
            path=R/cfg["path"]
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),cfg["raw_sha256"])
            self.assertEqual(logical(path,self.oracle),cfg["logical_hash"])
            lines,d=cards(path)
            self.assertEqual(sum(d.values()),cfg["physical_cards"])
            ids.add(cfg["id"])
        self.assertEqual(ids,{"BASELINE","NINE","TEN_PATROL","TEN_LIBERATOR","TEN_TECHNOMANCER"})
        self.assertEqual(next(x for x in p["configurations"] if x["id"]=="TEN_LIBERATOR")["logical_hash"],LOGICAL)

    def test_mana_and_role_limits_not_gameplay_guarantee(self):
        _,d=cards(PREF)
        mana_rocks={"Arcane Signet","Rakdos Signet","Sol Ring","Talisman of Creativity",
                    "Talisman of Dominance","Talisman of Indulgence","Mox Opal","Cursed Mirror"}
        lands=sum(q for name,q in d.items() if "Land" in self.oracle[name]["type_line"])
        rocks=sum(d[n] for n in mana_rocks)
        self.assertEqual((lands,rocks),(32,8))
        self.assertEqual(self.oracle["Liberator, Urza's Battlethopter"]["power"],"1")
        self.assertEqual(self.oracle["Shimmer Myr"]["power"],"2")
        self.assertEqual(self.oracle["Kappa Cannoneer"]["mana_cost"],"{5}{U}")

if __name__=="__main__":
    unittest.main()
