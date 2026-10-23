"""Abaddon stage11 finite source/physical test, not a game win-rate model.

Sanctum supplies pre-main commander cascade eligibility after surviving a
turn; Mirkwood Bats converts actual token create/sac events, subject to timing.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage11_sanctum_bats_precombat_comparison_20261022.json"
ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
NEW=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage8_nine_offranking_Scryfall_20261022.json"
VEY=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage9_veyran_roaming_throne_Scryfall_20261022.json"
BASE=ROOT/"data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
BASICS={"Island","Mountain","Swamp"}


def physical(path):
    raw=path.read_bytes()
    counts=Counter()
    for line in raw.decode().splitlines():
        qty,n=line.split("x ",1)
        counts[n.removesuffix(" [Commander]")]+=int(qty)
    assert sum(counts.values())==100
    assert counts["Abaddon the Despoiler"]==1
    assert all(n in BASICS or q==1 for n,q in counts.items())
    return raw,counts


def sanctum_pre_main(opponents=3, shrines=1, bloodletter=False, solphim=False,
                     already_on_battlefield=True):
    # Exact life-loss event. Solphim doubles DAMAGE only, not loss of life.
    if not already_on_battlefield:
        return 0
    lost_per_opponent=shrines*(2 if bloodletter else 1)
    return opponents*lost_per_opponent


def bats_token_events(opponents=3, created=0, sacrificed=0):
    """One bats trigger for each token creation and each token sacrifice."""
    return opponents*(created+sacrificed)


class AbaddonStage11SourceProof(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=json.loads(REPORT.read_text(encoding="utf-8"))
        cls.baseoracle=json.loads(ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.new=json.loads(NEW.read_text(encoding="utf-8"))["oracle_cards"]
        cls.veyran=json.loads(VEY.read_text(encoding="utf-8"))["oracle_cards"]

    def test_exact_oracle_shrine_and_token_candidates(self):
        s=self.new
        self.assertEqual(s["Sanctum of Stone Fangs"]["mana_cost"],"{1}{B}")
        self.assertIn("At the beginning of your first main phase",
                      s["Sanctum of Stone Fangs"]["oracle_text"])
        self.assertIn("number of Shrines you control",
                      s["Sanctum of Stone Fangs"]["oracle_text"])
        self.assertIn("Whenever you create or sacrifice a token",
                      s["Mirkwood Bats"]["oracle_text"])
        self.assertIn("artifact you control enters",
                      s["Reckless Fireweaver"]["oracle_text"])
        self.assertIn("At the beginning of your upkeep",
                      s["Creeping Bloodsucker"]["oracle_text"])
        self.assertIn("At the beginning of your first main phase",
                      s["Sanctum of Stone Fangs"]["oracle_text"])
        self.assertIn("during your turn",self.baseoracle["Bloodletter of Aclazotz"]["oracle_text"])
        self.assertIn("noncombat damage",self.baseoracle["Solphim, Mayhem Dominus"]["oracle_text"])

    def test_pre_main_x_on_following_turn_not_cast_turn(self):
        self.assertEqual(sanctum_pre_main(),3)
        self.assertEqual(sanctum_pre_main(bloodletter=True),6)
        self.assertEqual(sanctum_pre_main(solphim=True),3)
        self.assertEqual(sanctum_pre_main(already_on_battlefield=False),0)
        self.assertGreaterEqual(sanctum_pre_main(),3)
        # With Abaddon already battlefield, X=3 precedes the paid
        # original 3-MV spell CAST (Wheel/Windfall) and cascade grant.
        self.assertEqual(self.baseoracle["Abaddon the Despoiler"]["mana_cost"],
                         "{2}{U}{B}{R}")
        self.assertIn("spells you cast from your hand with mana value X or less",
                      self.baseoracle["Abaddon the Despoiler"]["oracle_text"])

    def test_bats_mixed_token_burst_without_fake_veyran_double(self):
        self.assertEqual(bats_token_events(created=2,sacrificed=2),12)
        self.assertEqual(bats_token_events(created=2,sacrificed=2+2),18)
        self.assertEqual(bats_token_events(created=0,sacrificed=0),0)
        self.assertIn("instant or sorcery",self.veyran["Veyran, Voice of Duality"]["oracle_text"])
        # Veyran can double original qualifying Storm-Kiln/Prosper/Lost
        # cast triggers; later Bats trigger from token events is NOT
        # directly a spell-cast/copy-triggered ability.

    def test_source_legal_full_100_and_not_owner_ready(self):
        r=self.report
        baseline_raw,base=physical(BASE)
        self.assertEqual(hashlib.sha256(baseline_raw).hexdigest(),
                         r["canonical"]["sha256"])
        self.assertTrue(r["canonical_approved_locked_unchanged"])
        self.assertFalse(r["owner_ready"])
        self.assertFalse(r["m6_candidate_specific_certified"])
        self.assertTrue(r["deck3_hold"])
        self.assertEqual(len(r["three_complete_100_research_variants"]),3)
        for v in r["three_complete_100_research_variants"]:
            raw,current=physical(ROOT/v["path"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(),v["sha256"])
            self.assertEqual(sorted((current-base).elements()),sorted(v["add"]))
            self.assertEqual(sorted((base-current).elements()),sorted(v["cut"]))
            self.assertEqual(v["swaps"],len(v["add"]))
            self.assertLess(v["swaps"],5)
            self.assertEqual((current["Island"],current["Mountain"],current["Swamp"]),
                             (3,3,3))
            for protected in ["Nightscape Familiar","Aggravated Assault","Neheb, the Eternal",
                              "Loyal Subordinate","Call Forth the Tempest","Pact of Negation",
                              "Pyroblast","Bloodletter of Aclazotz","Solphim, Mayhem Dominus"]:
                self.assertIn(protected,current)
            for n in current:
                oracle=self.baseoracle.get(n) or self.new.get(n) or self.veyran.get(n)
                self.assertIsNotNone(oracle,n)
                self.assertEqual(oracle["commander_legality"],"legal",n)
                self.assertTrue(set(oracle["color_identity"])<=set("UBR"),n)

if __name__=="__main__":
    unittest.main()
