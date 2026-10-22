"""Fail-closed Abaddon M6.7 full 100-card choice verification.

Checks the only authored preferred exact physical package against an independent
trusted original source mirror. Does not confer M6 certification or approval.
"""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import hashlib
import json
import unittest

from scripts.grixis_m7_decision_gate import canonical_source, parse_list

ROOT=Path(__file__).resolve().parents[1]
DECK="Abaddon_the_Despoiler"
PREFERRED="data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_engine_answer_betrayal.txt"
ALTERNATE="data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_engine_answer_keeper.txt"
PORTFOLIO="data/grixis/m7/research_challengers/Abaddon_the_Despoiler_portfolio_v3_decisive.json"
INVENTORY="data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json"
APPROVED="2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
CHOSEN="1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd"
KEEPER="3ceddb947b0e7aff9cae489a0c60704214a2e580b97bfb1aaee5bb254c71fdaa"
CORE={"The Lost and the Damned","The Ruinous Powers","Call Forth the Tempest",
      "Keeper of Secrets","Loyal Subordinate","Neheb, the Eternal",
      "Birgi, God of Storytelling // Harnfel, Horn of Bounty",
      "Underworld Breach","Brain Freeze","Lion's Eye Diamond",
      "Mind's Desire","Storm-Kiln Artist","Nalfeshnee","Prosper, Tome-Bound"}
BASICS={"Island","Mountain","Swamp"}
ADD=Counter({"Grinning Ignus":1,"Chaos Warp":1})
CUT=Counter({"Rakdos, Lord of Riots":1,"Inevitable Betrayal":1})


class AbaddonExactM67Chosen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        registry=json.loads((ROOT/"data/grixis/registry.json").read_text())
        source_path,is_md=canonical_source(ROOT,registry["decks"][DECK])
        cls.source,cmd,companions=parse_list(source_path,source_markdown=is_md)
        if cmd!=["Abaddon the Despoiler"] or companions:
            raise AssertionError("Source commander not exact Abaddon")
        cls.chosen,chosen_cmd,_=parse_list(ROOT/PREFERRED)
        cls.alternate,alternate_cmd,_=parse_list(ROOT/ALTERNATE)
        assert chosen_cmd==alternate_cmd==cmd
        cls.plan=json.loads((ROOT/PORTFOLIO).read_text())
        cls.inventory=json.loads((ROOT/INVENTORY).read_text())

    def test_physical_100_diff_is_exact_two_swap(self):
        self.assertEqual(len(self.source),100)
        self.assertEqual(len(self.chosen),100)
        self.assertEqual(len(self.alternate),100)
        self.assertEqual(Counter(self.chosen)-Counter(self.source),ADD)
        self.assertEqual(Counter(self.source)-Counter(self.chosen),CUT)
        self.assertEqual(Counter(self.alternate)-Counter(self.source),ADD)
        self.assertEqual(Counter(self.source)-Counter(self.alternate),
                         Counter({"Rakdos, Lord of Riots":1,"Keeper of Secrets":1}))

    def test_list_singleton_and_protected_identity(self):
        for cards in (self.source,self.chosen,self.alternate):
            self.assertEqual({card:n for card,n in Counter(cards).items()
                              if n>1 and card not in BASICS},{})
            self.assertIn("Abaddon the Despoiler",cards)
        self.assertTrue(CORE.issubset(set(self.chosen)))
        self.assertEqual(sum(n for c,n in Counter(self.source).items() if c in BASICS),
                         sum(n for c,n in Counter(self.chosen).items() if c in BASICS))
        self.assertIn("Inevitable Betrayal",self.alternate)
        self.assertNotIn("Keeper of Secrets",self.alternate)

    def test_exact_pinned_source_and_hashes(self):
        self.assertEqual(self.plan["canonical"]["approved_sha256"],APPROVED)
        self.assertEqual(self.plan["proposed"]["physical_sha256"],CHOSEN)
        self.assertEqual(self.plan["competing"]["physical_sha256"],KEEPER)
        self.assertEqual(hashlib.sha256((ROOT/PREFERRED).read_bytes()).hexdigest(),CHOSEN)
        self.assertEqual(hashlib.sha256((ROOT/ALTERNATE).read_bytes()).hexdigest(),KEEPER)
        self.assertEqual(self.plan["proposed"]["adds"],list(ADD))
        self.assertEqual(self.plan["proposed"]["cuts"],list(CUT))
        self.assertFalse(self.plan["owner_approved"])
        self.assertFalse(self.plan["m6_certified"])

    def test_95_mechanical_cases_are_scope_limited(self):
        self.assertEqual(len(self.inventory["replay_cases"]),95)
        self.assertEqual(self.inventory["required_open"],[])
        self.assertFalse(self.inventory["authority"]["formal_m6_certified"])
        self.assertFalse(self.inventory["completion_claim"])
        self.assertEqual({p["id"] for p in self.inventory["newly_covered_parent_topics"]},
                         {"P0-021","P0-022","P0-023","P0-024","P0-025",
                          "P0-026","P0-027","P0-028","P0-029"})

    def test_original_commander_remains_active_and_unapproved_change(self):
        proposal=(ROOT/"data/grixis/m6/certification_preflight/Abaddon_M6_7_decisive_commander_choice_20261022.md").read_text()
        for text in ["SELECT_FOR_FINAL_VERIFICATION","RETAIN_ALTERNATIVE",
                     "M6.6 PARTIAL","M6 J BLOCKED","M7 0/62",
                     "One-deck-at-a-time enforced"]:
            self.assertIn(text,proposal)
        self.assertNotIn("Admiral Beckett Brass",self.plan["proposed"]["file"])
        self.assertFalse(self.plan["no_canonical_changes"] is False)


if __name__=="__main__":
    unittest.main()
