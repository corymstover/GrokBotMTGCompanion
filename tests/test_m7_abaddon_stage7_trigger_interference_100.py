"""Abaddon M7 stage7: source-bound conditional trigger effects and full physical 100s.

Research-only finite fixtures. This suite does not certify a gameplay win rate,
an M6 I/J result, or an owner-ready/approved final deck.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
REPORT = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage7_trigger_interference_100_review_20261022.json"
ORACLE_BASE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
ORACLE_39 = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json"
ORACLE_13 = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage4_13_source_cards_20261022.json"
BASICS = {"Island", "Mountain", "Swamp"}


def physical(path):
    raw = path.read_bytes()
    lines = raw.decode("utf-8").splitlines()
    cards = Counter()
    for line in lines:
        prefix, name = line.split("x ", 1)
        assert prefix.isdigit(), line
        cards[name.removesuffix(" [Commander]")] += int(prefix)
    return raw, lines, cards


def kessig_harmonic_pings(opponents=3, *, harmonic=True, ghyrson=True,
                           solphim=False, bloodletter=False):
    """Finite resolved *event* model; no stack, timing, or win-rate surrogate.

    Kessig's every-opponent 1-damage simultaneous event happens one time per
    Kessig trigger; Harmonic supplies another distinct Kessig trigger.
    Solphim modifies damage before dealt; Bloodletter modifies resultant life
    loss (not damage dealt). Ghyrson checks original damage as actually dealt.
    Ob checks the grouped exactly-one life loss, not per-opponent triggers.
    """
    total_opponent_life_loss = 0
    ob_triggers = 0
    ghyrson_triggers = 0
    for _ in range(2 if harmonic else 1):
        dealt = 2 if solphim else 1
        loss_each = dealt * (2 if bloodletter else 1)
        total_opponent_life_loss += opponents * loss_each
        if loss_each == 1:
            ob_triggers += 1
        if ghyrson and dealt == 1:
            ghyrson_triggers += opponents
            total_opponent_life_loss += opponents * 2 * (
                2 if bloodletter else 1
            )
    return total_opponent_life_loss, ob_triggers, ghyrson_triggers


class AbaddonStage7SourceAndPhysics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(REPORT.read_text(encoding="utf-8"))
        cls.base_source = json.loads(ORACLE_BASE.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.candidates = {}
        for p in (ORACLE_39, ORACLE_13):
            cls.candidates.update(json.loads(p.read_text(encoding="utf-8"))["oracle_cards"])

    def test_source_bound_both_complete_100_and_exact_sha(self):
        r = self.report
        self.assertFalse(r["owner_ready"])
        self.assertFalse(r["new_owner_approval"])
        self.assertFalse(r["formal_m6_10_accepted"])
        self.assertTrue(r["deck3_on_hold"])
        self.assertTrue(r["status"].startswith("RESEARCH_ONLY"))
        raw0, lines0, before = physical(BASE)
        self.assertEqual(hashlib.sha256(raw0).hexdigest(),r["canonical"]["raw_sha256"])
        self.assertEqual(sum(before.values()),100)
        self.assertEqual(lines0[0],"1x Abaddon the Despoiler [Commander]")
        self.assertEqual(len(r["full_100_alternatives"]),2)
        for trial in r["full_100_alternatives"]:
            raw, lines, after = physical(ROOT / trial["path"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(),trial["sha256"])
            self.assertEqual(lines[0],lines0[0])
            self.assertEqual(sum(after.values()),100)
            self.assertEqual(len(after),95)
            self.assertTrue(all(n in BASICS or q==1 for n,q in after.items()))
            self.assertEqual(sorted((after-before).elements()),sorted(trial["adds"]))
            self.assertEqual(sorted((before-after).elements()),sorted(trial["cuts"]))
            self.assertEqual(sum((after-before).values()),trial["swaps"])
            self.assertEqual(sum((before-after).values()),trial["swaps"])
            self.assertEqual(after["Mountain"],2)
            self.assertEqual(after["Island"],3)
            self.assertEqual(after["Swamp"],3)
            for must in trial["protected"]:
                self.assertIn(must,after)
            for name in after:
                source=self.base_source.get(name) or self.candidates.get(name)
                self.assertIsNotNone(source, f"{name} has no source Oracle")
                self.assertEqual(source["commander_legality"],"legal", name)
                self.assertTrue(set(source["color_identity"])<=set("UBR"),name)
        self.assertEqual(sorted(t["swaps"] for t in r["full_100_alternatives"]),[5,7])

    def test_real_printed_text_not_pseudo_synergy(self):
        b=self.base_source
        c=self.candidates
        self.assertIn("If an opponent would lose life",b["Bloodletter of Aclazotz"]["oracle_text"])
        self.assertIn("noncombat damage",b["Solphim, Mayhem Dominus"]["oracle_text"])
        self.assertIn("deals exactly 1 damage",c["Ghyrson Starn, Kelermorph"]["oracle_text"])
        self.assertIn("lose exactly 1 life",c["Ob Nixilis, Captive Kingpin"]["oracle_text"])
        self.assertIn("Shaman or another Wizard",c["Harmonic Prodigy"]["oracle_text"])
        self.assertIn("Whenever you cast a noncreature spell",b["Kessig Flamebreather"]["oracle_text"])
        self.assertIn("Cascade, cascade",b["Call Forth the Tempest"]["oracle_text"])
        self.assertIn("During your turn",b["Abaddon the Despoiler"]["oracle_text"])

    def test_ob_ghyrson_both_doublers_are_not_additive(self):
        # Three opponents, one original Kessig trigger doubled by Harmonic.
        self.assertEqual(kessig_harmonic_pings(),(18,2,6))
        # Solphim changes dealt 1 to dealt 2; neither Ghyrson nor Ob triggers.
        self.assertEqual(kessig_harmonic_pings(solphim=True),(12,0,0))
        # Bloodletter changes life loss, not source's 1 damage: Ghyrson DOES
        # still trigger, whereas Ob does not.
        self.assertEqual(kessig_harmonic_pings(bloodletter=True),(36,0,6))
        self.assertEqual(kessig_harmonic_pings(harmonic=False),(9,1,3))

    def test_each_real_draw_but_no_retroactive_cast_cascade(self):
        c=self.candidates
        self.assertIn("Whenever an opponent draws a card",c["Kederekt Parasite"]["oracle_text"])
        self.assertIn("if you control a red permanent",c["Kederekt Parasite"]["oracle_text"])
        # A wheel in 4-player game: seven distinct draws each for three opponents.
        # If Kederekt/red permanent survive, each separate draw can create a
        # subsequent damage/loss event, not an Ob trigger on the initial cast.
        draw_events=3*7
        parasite_triggers=draw_events
        ob_triggers_without_doubler=draw_events
        self.assertEqual((parasite_triggers,ob_triggers_without_doubler),(21,21))
        self.assertIn("from your hand",self.base_source["Abaddon the Despoiler"]["oracle_text"])
        self.assertTrue(any("never retroactively" in s for s in
                            self.report["critical_nonadditive_oracle_finding"]["findings"]))

    def test_spear_self_damage_and_protection_tradeoff(self):
        txt=self.candidates["Spear Spewer"]["oracle_text"]
        self.assertIn("each player",txt)
        self.assertIn("{T}",txt)
        # Damage 1 to its own controller and later Ghyrson extra 2, even if
        # only three opponents are strategically counted in threshold X.
        self.assertEqual((3*3,1+2),(9,3))
        by_id={x["id"]:x for x in self.report["full_100_alternatives"]}
        a=by_id["protected_exact_one_five"]
        b=by_id["aggressive_pinger_burn_seven"]
        self.assertNotIn("Pyroblast",a["cuts"])
        self.assertIn("Pyroblast",b["cuts"])
        self.assertIn("Loyal Subordinate",b["cuts"])
        self.assertIn("Fiery Confluence",b["adds"])
        self.assertIn("Spear Spewer",b["adds"])
        self.assertIn("Call Forth the Tempest",a["protected"])
        self.assertIn("Call Forth the Tempest",b["protected"])

    def test_research_packet_does_not_abuse_five_swap_floor(self):
        self.assertTrue(self.report["governance"]["minimum_five_is_eligibility_not_optimization_goal"])
        self.assertTrue(self.report["governance"]["not_proven_local_best"])
        self.assertTrue(self.report["governance"]["these_two_100s_are_adversarial_research_not_owner_ready"])
        self.assertGreaterEqual(self.report["prior_evidence"]["material_judgments"],10)
        self.assertGreaterEqual(self.report["prior_evidence"]["credible_incumbent_challenges"],8)
        for row in self.report["conditional_judgments"]:
            self.assertIn(row["disposition"],{
                "SELECT_ADD","RETAIN_ALTERNATIVE","REJECT","EXCLUDE_INVALID"
            })


if __name__=="__main__":
    unittest.main()
