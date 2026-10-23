"""Seven explicit Admiral rev2 complete physical candidates; bounded M6 I pool preflight.

No simulator-driven win rates, no unbounded global optimum and no new I/J
certificate: this gate validates evidence that a later authored certificate
may cite, and requires candid incompleteness.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
POOL=ROOT/"data/grixis/m6/ij/tested_pools/Admiral_Beckett_Brass_rev2_seven_configurations_20261022.json"
FULL=ROOT/"data/grixis/m7/research_challengers/Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
POST=ROOT/"data/grixis/m7/research_challengers/Admiral_Beckett_Brass_eleven_card_live_Scryfall_20261022.json"
NEW=ROOT/"data/grixis/m7/research_challengers/Admiral_Beckett_Brass_EDHREC_inclusion_lift_discovery_20261022.json"
OLDI=ROOT/"data/grixis/m6/ij/certificates/admiral-beckett-brass.json"

def parse(path):
    q=Counter()
    zones={}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        a,raw=line.split("x ",1)
        n=raw.removesuffix(" [Commander]")
        if n in q:
            raise ValueError("duplicate row: "+n)
        q[n]=int(a)
        zones[n]="commander" if raw.endswith(" [Commander]") else "main"
    return q,zones

def logical(q,zones,oracle):
    rows=sorted(f'{zones[n]}|{oracle[n]["oracle_id"]}|{num}' for n,num in q.items())
    return "lh1:"+hashlib.sha256("".join(row+"\n" for row in rows).encode()).hexdigest()

class AdmiralRev2PoolPreflight(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(POOL.read_text())
        cls.oracle={r["name"]:r for r in json.loads(FULL.read_text())["cards"]}
        cls.oracle.update({r["name"]:r for r in json.loads(POST.read_text())["verified_cards"]})
        cls.oracle.update({r["name"]:r for r in json.loads(NEW.read_text())["scryfall_new_discovery_oracle"]})
        cls.config={}
        for row in cls.data["configurations"]:
            cls.config[row["id"]]=parse(ROOT/row["path"])[0]

    def test_all_seven_distinct_exact_physical_and_oracle_hashes(self):
        d=self.data
        self.assertEqual(d["explicit_pool_size"],7)
        self.assertEqual(len(self.config),7)
        for row in d["configurations"]:
            with self.subTest(id=row["id"]):
                p=ROOT/row["path"]
                c,z=parse(p)
                self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),row["raw_sha256"])
                self.assertEqual(logical(c,z,self.oracle),row["logical_hash"])
                self.assertEqual(sum(c.values()),100)
                self.assertEqual(c["Admiral Beckett Brass"],1)
                self.assertEqual(z["Admiral Beckett Brass"],"commander")
                self.assertEqual(set(c)-set(self.oracle),set())
                self.assertTrue(all(q==1 or n in {"Island","Mountain","Swamp"} for n,q in c.items()))
                self.assertTrue(all(set(self.oracle[n]["color_identity"])<={"B","R","U"} for n in c))
                self.assertTrue(all(self.oracle[n].get("commander_legality",self.oracle[n].get("legalities",{}).get("commander"))=="legal" for n in c))

    def test_selected_real_six_changed_slots_and_subtyping(self):
        d=self.config
        base=d["BASELINE"]
        selected=d["WAVE_PALISADE"]
        self.assertEqual(sum((selected-base).values()),6)
        self.assertEqual(sum((base-selected).values()),6)
        self.assertEqual(self.data["provisional_preferred"],"WAVE_PALISADE")
        self.assertEqual(self.data["provisional_preferred_raw_sha256"],
                         next(r["raw_sha256"] for r in self.data["configurations"] if r["id"]=="WAVE_PALISADE"))
        self.assertEqual(self.data["provisional_preferred_logical_hash"],
                         next(r["logical_hash"] for r in self.data["configurations"] if r["id"]=="WAVE_PALISADE"))
        self.assertIn("Kari Zev, Skyship Raider",selected)
        self.assertNotIn("Storm Fleet Aerialist",selected)
        self.assertIn("Human Pirate",self.oracle["Kari Zev, Skyship Raider"]["type_line"])
        self.assertIn("Human Pirate",self.oracle["Storm Fleet Aerialist"]["type_line"])
        self.assertIn("red Monkey creature token",self.oracle["Kari Zev, Skyship Raider"]["oracle_text"])

    def test_wave_is_shared_between_competing_six_swap_sources(self):
        d=self.config
        for v in ("WAVE_PALISADE","WAVE_CANNONADE"):
            self.assertEqual(d[v]["Cosmotronic Wave"],1)
            self.assertEqual(d[v]["Bident of Thassa"],1)
            self.assertEqual(d[v]["Open into Wonder"],1)
        self.assertEqual(d["WAVE_PALISADE"]["Fiery Cannonade"],1)
        self.assertEqual(d["WAVE_PALISADE"]["Raise the Palisade"],0)
        self.assertEqual(d["WAVE_CANNONADE"]["Fiery Cannonade"],0)
        self.assertEqual(d["WAVE_CANNONADE"]["Raise the Palisade"],1)
        self.assertEqual(self.oracle["Fiery Cannonade"]["type_line"],"Instant")
        self.assertEqual(self.oracle["Raise the Palisade"]["type_line"],"Sorcery")
        self.assertEqual(self.oracle["Cosmotronic Wave"]["type_line"],"Sorcery")

    def test_more_swaps_does_not_imply_actual_best(self):
        d=self.config
        self.assertEqual(sum((d["NINE_BOTH"]-d["BASELINE"]).values()),9)
        self.assertEqual(sum((d["AERIALIST_WAVE_PALISADE"]-d["BASELINE"]).values()),7)
        for essential in ("Bident of Thassa","Open into Wonder","Fiery Cannonade"):
            self.assertIn(essential,d["WAVE_PALISADE"])
        self.assertNotIn("Bident of Thassa",d["NINE_BOTH"])
        self.assertNotIn("Open into Wonder",d["NINE_BOTH"])
        self.assertNotIn("Fiery Cannonade",d["NINE_BOTH"])

    def test_pool_is_not_new_m6_i_or_j_certification(self):
        d=self.data
        old=json.loads(OLDI.read_text())
        self.assertEqual(old["candidate_pool"]["tested_pool_size"],5)
        self.assertNotEqual(old["list_hash"],d["provisional_preferred_logical_hash"])
        self.assertEqual(d["m6_I_pass_issued"],False)
        self.assertEqual(d["m6_J_pass_issued"],False)
        self.assertEqual(d["owner_m7_approved"],False)
        self.assertEqual(d["m6_10_accepted"],False)
        self.assertTrue(d["no_win_rate_or_global_claim"])
        self.assertGreaterEqual(len(d["still_required"]),3)
        for row in d["configurations"]:
            self.assertGreater(len(row["judgment"]),60)

if __name__=="__main__":
    unittest.main()
