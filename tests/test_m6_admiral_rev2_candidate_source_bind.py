"""Admiral rev2 candidate-specific M6 preflight; no reused D certificate.

Checks complete physical 100, exact raw/logical fingerprints, Scryfall
source-binding, identity, legality, and honest unclosed I/J. This is a
preflight, not Phase-B simulation or final owner-ready M7 authorization.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/"data/grixis/m6/certification_preflight/Admiral_M6_rev2_candidate_specific_hash_oracle_scope_20261022.json"
BASE=ROOT/"data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
FULL=ROOT/"data/grixis/m7/research_challengers/Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
EXTRA=ROOT/"data/grixis/m7/research_challengers/Admiral_Beckett_Brass_eleven_card_live_Scryfall_20261022.json"
LEGACY_I=ROOT/"data/grixis/m6/ij/certificates/admiral-beckett-brass.json"
LEGACY_J=ROOT/"data/grixis/m6/bundles/admiral-beckett-brass.json"

def physical(path):
    counts=Counter()
    zones={}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        q,raw=line.split("x ",1)
        name=raw.removesuffix(" [Commander]")
        if name in counts:
            raise ValueError("duplicate printed name row: "+name)
        counts[name]=int(q)
        zones[name]="commander" if raw.endswith(" [Commander]") else "main"
    return counts,zones

def logical_hash(counts,zones,oracle):
    rows=sorted(f'{zones[n]}|{oracle[n]["oracle_id"]}|{q}' for n,q in counts.items())
    return "lh1:"+hashlib.sha256("".join(r+"\n" for r in rows).encode()).hexdigest()

class AdmiralRev2SpecificBinding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc=json.loads(DOC.read_text(encoding="utf-8"))
        cls.candidate_path=ROOT/cls.doc["candidate"]["path"]
        cls.d_path=ROOT/cls.doc["baseline_D"]["path"]
        cls.cards,cls.zones=physical(cls.candidate_path)
        cls.base,cls.base_zones=physical(BASE)
        cls.d,cls.d_zones=physical(cls.d_path)
        cls.full={c["name"]:c for c in json.loads(FULL.read_text(encoding="utf-8"))["cards"]}
        cls.extra={c["name"]:c for c in json.loads(EXTRA.read_text(encoding="utf-8"))["verified_cards"]}
        cls.oracle={**cls.full,**cls.extra}

    def test_exact_reproducible_hashes_and_frozen_canonical(self):
        d=self.doc
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(),
                         d["authoritative_canonical"]["approved_locked_raw_sha256"])
        self.assertEqual(hashlib.sha256(self.d_path.read_bytes()).hexdigest(),d["baseline_D"]["raw_sha256"])
        self.assertEqual(hashlib.sha256(self.candidate_path.read_bytes()).hexdigest(),d["candidate"]["raw_sha256"])
        self.assertEqual(logical_hash(self.cards,self.zones,self.oracle),d["candidate"]["logical_hash"])
        self.assertEqual(logical_hash(self.d,self.d_zones,self.oracle),d["baseline_D"]["logical_hash"])
        self.assertEqual(logical_hash(self.base,self.base_zones,self.oracle),
                         "lh1:38598ad4616bb80278e5e8e24c313afdc8bcd555312bbac3fca33fe84d6e9e86")

    def test_full_100_and_actual_role_counts(self):
        d=self.doc["candidate"]
        self.assertEqual(sum(self.cards.values()),100)
        self.assertEqual(len(self.cards),97)
        self.assertEqual(self.cards["Admiral Beckett Brass"],1)
        self.assertEqual(self.zones["Admiral Beckett Brass"],"commander")
        self.assertEqual(sum(q for n,q in self.cards.items() if "Land" in self.oracle[n]["type_line"]),35)
        self.assertEqual(sum(q for n,q in self.cards.items() if "Creature" in self.oracle[n]["type_line"]),34)
        self.assertEqual((d["physical_cards"],d["distinct_names"],d["land_cards"],d["creature_cards"]),(100,97,35,34))
        self.assertTrue(all(q==1 or n in {"Island","Mountain","Swamp"}
                            for n,q in self.cards.items()))

    def test_every_card_oracle_identity_and_commander_legality(self):
        self.assertEqual(set(self.cards)-set(self.oracle),set())
        for name in self.cards:
            with self.subTest(card=name):
                source=self.oracle[name]
                self.assertTrue(source["oracle_id"])
                self.assertTrue(set(source["color_identity"])<={"B","R","U"})
                legality=source.get("commander_legality",source.get("legalities",{}).get("commander"))
                self.assertEqual(legality,"legal")
        self.assertEqual(self.doc["oracle_and_legality"]["project_exceptions"],[])

    def test_d_and_canonical_delta_is_exactly_six_true_replacements(self):
        d=self.doc
        self.assertEqual(sum((self.cards-self.d).values()),1)
        self.assertEqual(sum((self.d-self.cards).values()),1)
        self.assertEqual(set((self.cards-self.d).elements()),set(d["exact_difference_from_D"]["add"]))
        self.assertEqual(set((self.d-self.cards).elements()),set(d["exact_difference_from_D"]["cut"]))
        self.assertEqual(sum((self.cards-self.base).values()),6)
        self.assertEqual(sum((self.base-self.cards).values()),6)
        self.assertEqual(set((self.cards-self.base).elements()),set(d["exact_difference_from_canonical"]["add"]))
        self.assertEqual(set((self.base-self.cards).elements()),set(d["exact_difference_from_canonical"]["cut"]))
        for preserve in ("Bident of Thassa","The Indomitable","Kindred Discovery","Open into Wonder",
                         "March of the Drowned","Fiery Cannonade","Path of Ancestry"):
            self.assertEqual(self.cards[preserve],1)

    def test_selected_paid_effect_is_not_a_free_permanent_bounce(self):
        wave=self.extra["Cosmotronic Wave"]
        palisade=self.full["Raise the Palisade"]
        cannon=self.extra["Fiery Cannonade"]
        self.assertEqual((wave["type_line"],wave["mana_cost"]),("Sorcery","{3}{R}"))
        self.assertEqual((palisade["type_line"],palisade["mana_cost"]),("Sorcery","{4}{U}"))
        self.assertEqual((cannon["type_line"],cannon["mana_cost"]),("Instant","{2}{R}"))
        self.assertIn("can't block this turn",wave["oracle_text"])
        self.assertIn("Return all creatures",palisade["oracle_text"])
        self.assertNotIn("Return all creatures",wave["oracle_text"])
        self.assertEqual(self.cards["Cosmotronic Wave"],1)
        self.assertEqual(self.cards["Raise the Palisade"],0)
        self.assertEqual(self.cards["Fiery Cannonade"],1)

    def test_old_D_i_j_are_valid_historical_but_unusable_for_rev2_hash(self):
        cert=json.loads(LEGACY_I.read_text(encoding="utf-8"))
        bundle=json.loads(LEGACY_J.read_text(encoding="utf-8"))
        current=self.doc["candidate"]["logical_hash"]
        self.assertNotEqual(cert["list_hash"],current)
        self.assertNotEqual(bundle["result_hash"],current)
        self.assertEqual(cert["list_hash"],self.doc["baseline_D"]["logical_hash"])
        self.assertEqual(bundle["result_hash"],self.doc["baseline_D"]["logical_hash"])
        self.assertEqual(self.doc["ij"]["rev2_i_certificate"],"NOT_YET_ISSUED")
        self.assertEqual(self.doc["ij"]["rev2_j_reproducibility_bundle"],"NOT_YET_ISSUED")
        self.assertIs(self.doc["ij"]["m6_10_owner_accepted"],False)
        self.assertIs(self.doc["candidate"]["owner_approved"],False)
        self.assertTrue(self.doc["outstanding_hard_gates"])

if __name__=="__main__":
    unittest.main()
