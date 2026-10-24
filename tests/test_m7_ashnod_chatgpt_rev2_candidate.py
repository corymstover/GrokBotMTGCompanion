"""Source-bound Ashnod M7 Rev2 nine-swap evidence. Never authorizes a canonical lock."""
import hashlib, json, math, sys, unittest
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/"scripts"))
import grixis_authority as ga
import grixis_m6_bundle_check as checker
C="data/grixis/m7/candidate_lists/Ashnod_the_Uncaring_ChatGPT_M7_Rev2_Nine_Approval_Candidate.txt"
B="data/grixis/m7/baseline_sources/Ashnod_the_Uncaring_approved_source_2026-10-13.txt"
G="data/grixis/m7/candidate_lists/Ashnod_the_Uncaring.txt"
O="data/grixis/m6/oracle_snapshots/Ashnod_the_Uncaring_ChatGPT_M7_Rev2_Selected_20261023.json"
P="data/grixis/m7/decision_reviews/Ashnod_the_Uncaring_ChatGPT_M7_Rev2_Independent.json"
POOL="data/grixis/m6/ij/tested_pools/Ashnod_the_Uncaring_ChatGPT_Rev2_tested_configurations_20261023.json"
I="data/grixis/m6/ij/certificates/ashnod-the-uncaring-chatgpt-rev2.json"
J="data/grixis/m6/ij/revision_bundles/ashnod-the-uncaring-chatgpt-rev2.json"
RAW="a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761"
LOGICAL="lh1:bd81a60cfbd2728705bfe2e14bd32f56a4081b51cf72b46a7d6cb057e9a30140"
BASE="f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf"
GROK="b1078f084c2fa53426910edb66f0a036978e06bd9c9a2061f460af397503143d"
ADDS={"Corridor Monitor","Basalt Monolith","Aether Spellbomb","Spawning Pit","Animation Module","Priest of Forgotten Gods","Ruthless Knave","City of Brass","Mana Confluence"}
CUTS={"Foundry Inspector","Fellwar Stone","Talisman of Indulgence","Esoteric Duplicator","Reckless Fireweaver","Jhoira, Weatherlight Captain","Farid, Enterprising Salvager","Xander's Lounge","Exotic Orchard"}
ROCKS={"Sol Ring","Arcane Signet","Fellwar Stone","Mind Stone","Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence","Mox Opal","Lotus Petal","Basalt Monolith"}
GC={"Ancient Tomb","Bolas's Citadel","Cyclonic Rift","Demonic Tutor","Fierce Guardianship","Vampiric Tutor"}
def sha(p): return hashlib.sha256((R/p).read_bytes()).hexdigest()
def data(p): return json.loads((R/p).read_text())
def parse(p):
    out=[]
    for line in (R/p).read_text().splitlines():
        if not line: continue
        q,n=line.split("x ",1)
        z="commander" if n.endswith(" [Commander]") else "main"
        out.append((int(q),n.removesuffix(" [Commander]"),z))
    return out
def logical(rows,mapping):
    return ga.logical_hash((z,mapping[n]["oracle_id"],q) for q,n,z in rows)
class BoundedAshnodRev2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=parse(C);cls.oracle=data(O);cls.o={x["name"]:x for x in cls.oracle["cards"]};cls.p=data(P)
    def test_exact_raw_and_untouched_sources(self):
        self.assertEqual(sha(C),RAW)
        self.assertEqual(sha(B),BASE)
        self.assertEqual(sha(G),GROK)
        self.assertEqual(self.p["candidate"]["raw_sha256"],RAW)
        self.assertFalse(self.p["candidate"]["owner_approved"])
        self.assertFalse(self.p["candidate"]["canonical_modified"])
    def test_100_95_singleton_and_exact_swaps(self):
        a,b=self.rows,parse(B)
        self.assertEqual((sum(q for q,_,_ in a),len(a),len({n for _,n,_ in a})),(100,95,95))
        self.assertEqual(a[0],(1,"Ashnod the Uncaring","commander"))
        self.assertEqual({n:q for q,n,_ in a if q>1},{"Island":3,"Mountain":2,"Swamp":3})
        old=Counter({n:q for q,n,_ in b});new=Counter({n:q for q,n,_ in a})
        self.assertEqual(set((new-old).elements()),ADDS)
        self.assertEqual(set((old-new).elements()),CUTS)
        self.assertEqual(len(self.p["swaps"]),9)
    def test_selected_oracle_ids_legality_and_logical_digest(self):
        self.assertEqual(set(self.o),{n for _,n,_ in self.rows})
        self.assertEqual((len(self.o),self.oracle["physical_cards"]),(95,100))
        self.assertEqual((self.oracle["candidate_raw_sha256"],self.oracle["candidate_logical_hash"]),(RAW,LOGICAL))
        self.assertEqual(logical(self.rows,self.o),LOGICAL)
        self.assertEqual(self.oracle["project_exceptions"],[])
        for q,n,z in self.rows:
            x=self.o[n]
            self.assertEqual((x["quantity"],x["zone"]),(q,z))
            self.assertEqual(x["commander_legality"],"legal",n)
            self.assertTrue(set(x["color_identity"])<=set("UBR"),n)
            self.assertTrue(x["oracle_id"] and isinstance(x["oracle_text"],str),n)
    def test_mana_game_changers_and_probability_proxy(self):
        self.assertEqual(sum(q for q,n,_ in self.rows if "Land" in self.o[n]["type_line"]),33)
        self.assertEqual(sum(q for q,n,_ in self.rows if n in ROCKS),8)
        self.assertEqual({n for _,n,_ in self.rows if self.o[n]["game_changer"]},GC)
        prob=lambda k:sum(math.comb(k,i)*math.comb(99-k,11-i)/math.comb(99,11) for i in range(5,12))
        vals=self.p["mana"]["prob_ge_5_sources_in_first_11_99_card_library"]
        self.assertAlmostEqual(prob(42),vals["baseline"])
        self.assertAlmostEqual(prob(41),vals["rev2"])
        self.assertAlmostEqual(prob(40),vals["grok_first_pass"])
    def test_basalt_two_loops_and_walking_ballista_outlet(self):
        o=self.o
        self.assertIn("{T}: Add {C}{C}{C}",o["Basalt Monolith"]["oracle_text"])
        self.assertIn("{3}: Untap",o["Basalt Monolith"]["oracle_text"])
        self.assertIn("cost {1} less",o["Forensic Gadgeteer"]["oracle_text"])
        self.assertIn("may pay {2}",o["Rings of Brighthearth"]["oracle_text"])
        self.assertEqual((3-(3-1),6-(3+2)),(1,1))
        self.assertIn("Walking Ballista",o)
    def test_pit_manual_combo_algebra_and_copy_cost_gate(self):
        o=self.o
        self.assertIn("Sacrifice a creature: Put a charge counter",o["Spawning Pit"]["oracle_text"])
        self.assertIn("Remove two charge counters",o["Spawning Pit"]["oracle_text"])
        self.assertIn("if one or more permanents were sacrificed to activate it",o["Ashnod the Uncaring"]["oracle_text"])
        self.assertIn("Whenever you sacrifice an artifact",o["Crime Novelist"]["oracle_text"])
        counters,red=2,1
        for _ in range(12):
            self.assertGreaterEqual(min(counters//2,red),1)
            counters-=2;red-=1
            counters+=2;red+=1
        self.assertEqual((counters,red),(2,1))
        self.assertFalse(self.p["independent_discoveries"]["independent_manual_rules_case"]["indexed_by_spellbook"])
    def test_module_knave_priest_spellbomb_and_engineer(self):
        o=self.o
        self.assertIn("Whenever one or more +1/+1 counters",o["Animation Module"]["oracle_text"])
        self.assertIn("Sacrifice an artifact:",o["Arcbound Ravager"]["oracle_text"])
        self.assertIn("add {R}",o["Crime Novelist"]["oracle_text"])
        self.assertIn("Sacrifice two other creatures",o["Priest of Forgotten Gods"]["oracle_text"])
        self.assertIn("Any number of target players",o["Priest of Forgotten Gods"]["oracle_text"])
        self.assertIn("Sacrifice a creature: Create two Treasure",o["Ruthless Knave"]["oracle_text"])
        self.assertIn("Sacrifice three Treasures: Draw a card",o["Ruthless Knave"]["oracle_text"])
        self.assertIn("Sacrifice this artifact: Draw a card",o["Aether Spellbomb"]["oracle_text"])
        self.assertIn("Return target artifact card",o["Goblin Engineer"]["oracle_text"])
        self.assertIn("untap target artifact or creature",o["Corridor Monitor"]["oracle_text"])
        self.assertEqual(len([x for x in self.p["independent_discoveries"]["source_bound_spellbook"] if "Animation Module" in x["cards"]]),3)
    def test_eight_reproducible_full100_alternatives(self):
        pool=data(POOL)
        self.assertEqual(len(pool["configurations"]),8)
        self.assertEqual(pool["explicit_pool_size"],8)
        research=data("data/grixis/m7/research_challengers/Ashnod_the_Uncaring_Scryfall_live_20261023.json")
        oi=dict(self.o)
        oi.update({x["name"]:x for x in research["baseline_cards"]+research["cards"]})
        for x in pool["configurations"]:
            self.assertEqual(sha(x["path"]),x["raw_sha256"],x["id"])
            c=parse(x["path"])
            self.assertEqual((sum(q for q,_,_ in c),len({n for _,n,_ in c})),(100,95),x["id"])
            self.assertEqual(logical(c,oi),x["logical_hash"],x["id"])
        self.assertEqual(pool["configurations"][2]["raw_sha256"],RAW)
    def test_separate_rev2_i_and_j_are_source_bound_and_not_approval(self):
        cert,bundle=data(I),data(J)
        self.assertEqual(ga.validate_file(cert,"zero_improvement_certificate.schema.json"),[])
        self.assertEqual(cert["list_hash"],LOGICAL)
        self.assertEqual(bundle["result_hash"],LOGICAL)
        self.assertEqual(cert["candidate_pool"]["source_sha256"],"sha256:"+sha(POOL))
        self.assertEqual(cert["candidate_pool"]["tested_pool_size"],8)
        self.assertTrue(checker.validate_bundle(bundle,checker.load(checker.REGISTRY),checker.load(checker.SEALS)))
        self.assertFalse(bundle["pass_c"]["technically_independent"])
        self.assertFalse(bundle["authority"]["can_approve_or_lock"])
        self.assertFalse(cert["authority"]["can_approve_or_lock"])
        self.assertTrue(all(not t["supports_improvement_claim"] for t in bundle["phase_b"]["tests"]))
if __name__=="__main__": unittest.main()
