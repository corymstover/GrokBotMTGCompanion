"""Abaddon stage9 source-bound Veyran permanent trigger comparison.

Checks three complete research 100s and the exact cast/copy scope. This does
not imply a globally optimal deck, owner readiness, or a changed M6 certificate.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage9_veyran_warhammer_trigger_review_20261022.json"
SNAP=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage9_veyran_roaming_throne_Scryfall_20261022.json"
IMPACT=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage8_nine_offranking_Scryfall_20261022.json"
ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
BASE=ROOT/"data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
BASICS={"Island","Mountain","Swamp"}


def physical(path):
    raw=path.read_bytes()
    lines=raw.decode().splitlines()
    cards=Counter()
    for line in lines:
        n,name=line.split("x ",1)
        assert n.isdigit()
        cards[name.removesuffix(" [Commander]")]+=int(n)
    return raw,lines,cards


class AbaddonVeyranSourceProof(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=json.loads(REPORT.read_text(encoding="utf-8"))
        cls.snapshot=json.loads(SNAP.read_text(encoding="utf-8"))["oracle_cards"]
        cls.impact=json.loads(IMPACT.read_text(encoding="utf-8"))["oracle_cards"]
        cls.baseoracle=json.loads(ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"]

    def test_veyran_source_mechanics_and_no_cascade_spurious_double(self):
        v=self.snapshot["Veyran, Voice of Duality"]
        self.assertEqual(v["commander_legality"],"legal")
        self.assertEqual(set(v["color_identity"]),{"U","R"})
        self.assertEqual(v["mana_cost"],"{1}{U}{R}")
        self.assertIn("cast or copy an instant or sorcery",v["oracle_text"])
        self.assertIn("triggered ability of a permanent you control",v["oracle_text"])
        throne=self.snapshot["Roaming Throne"]
        self.assertIn("choose a creature type",throne["oracle_text"])
        self.assertIn("another creature",throne["oracle_text"])
        self.assertEqual(throne["commander_legality"],"legal")
        self.assertIn("spells you cast from your hand",self.baseoracle["Abaddon the Despoiler"]["oracle_text"])
        self.assertEqual(len(self.report["trigger_crosswalk"]),10)
        self.assertTrue(any("cascade" in s.lower() for s in self.report["source_negative_rules"]))
        self.assertFalse(self.report["owner_ready"])

    def test_ten_permanent_crosswalk_uses_real_source_text(self):
        snap=self.baseoracle
        names={
            "Birgi, God of Storytelling // Harnfel, Horn of Bounty",
            "Kessig Flamebreather","Thermo-Alchemist","Vivi Ornitier",
            "Storm-Kiln Artist","The Lost and the Damned","Keeper of Secrets",
            "Nalfeshnee","Prosper, Tome-Bound",
            "Abaddon the Despoiler + Passionate Archaeologist",
        }
        rows=self.report["trigger_crosswalk"]
        self.assertEqual({r["permanent"] for r in rows},names)
        self.assertIn("Whenever you cast a spell",snap["Birgi, God of Storytelling // Harnfel, Horn of Bounty"]["oracle_text"])
        self.assertIn("Whenever you cast a spell from exile",snap["Nalfeshnee"]["oracle_text"])
        self.assertIn("Whenever you cast a spell from anywhere other than your hand",snap["Keeper of Secrets"]["oracle_text"])
        self.assertIn("Whenever a land you control enters",snap["The Lost and the Damned"]["oracle_text"])
        self.assertIn("Whenever you play a card from exile",snap["Prosper, Tome-Bound"]["oracle_text"])
        self.assertIn("Commander creatures you own have",snap["Passionate Archaeologist"]["oracle_text"])
        self.assertIn("Whenever you cast or copy an instant or sorcery",snap["Storm-Kiln Artist"]["oracle_text"])

    def test_finite_brainstorm_from_exile_veyran_copies_not_casts(self):
        # Original Brainstorm is CAST once. A controlled Nalfeshnee triggered
        # on exile-cast is doubled by Veyran and makes TWO spell COPIES.
        cast_events=1
        nalfeshnee_copies=2
        total_magecraft_events=cast_events+nalfeshnee_copies
        storm_kiln_treasures=2*total_magecraft_events
        prosper_treasures=2*cast_events
        self.assertEqual((cast_events,nalfeshnee_copies),(1,2))
        self.assertEqual((storm_kiln_treasures,prosper_treasures),(6,2))
        self.assertEqual(storm_kiln_treasures+prosper_treasures,8)
        self.assertIn("Birgi produces two",self.report["finite_cast_from_exile_scenario"]["deterministic_events"][0])
        self.assertTrue(any("COPY is not a CAST" in x
                            for x in self.report["source_negative_rules"]))

    def test_all_three_research_lists_100_source_legal_and_unapproved(self):
        r=self.report
        self.assertFalse(r["owner_ready"])
        self.assertFalse(r["m6_new_certificate"])
        self.assertTrue(r["canonical_approved_locked_unchanged"])
        self.assertTrue(r["deck3_hold"])
        raw0,lines0,base=physical(BASE)
        self.assertEqual(hashlib.sha256(raw0).hexdigest(),r["canonical_sha256"])
        self.assertEqual(sum(base.values()),100)
        variants=r["research_alternatives"]
        self.assertEqual(len(variants),3)
        for q in variants:
            raw,lines,after=physical(ROOT/q["path"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(),q["raw_sha256"])
            self.assertEqual(lines[0],lines0[0])
            self.assertEqual(sum(after.values()),100)
            self.assertEqual(sorted((after-base).elements()),sorted(q["adds"]))
            self.assertEqual(sorted((base-after).elements()),sorted(q["cuts"]))
            self.assertTrue(all(n in BASICS or qty==1 for n,qty in after.items()))
            self.assertIn("Call Forth the Tempest",after)
            self.assertIn("Pyroblast",after)
            self.assertIn("Pact of Negation",after)
            self.assertIn("Aggravated Assault",after)
            self.assertIn("Neheb, the Eternal",after)
            for n in after:
                source=self.baseoracle.get(n) or self.impact.get(n) or self.snapshot.get(n)
                self.assertIsNotNone(source,n)
                self.assertEqual(source["commander_legality"],"legal",n)
                self.assertTrue(set(source["color_identity"]) <= set("UBR"),n)
        self.assertTrue(all(x["swaps"]<5 for x in variants))
        self.assertTrue(r["owner_gate"]["no_forced_swaps"])
        self.assertTrue(r["owner_gate"]["five_is_minimum_not_default"])


if __name__=="__main__":
    unittest.main()
