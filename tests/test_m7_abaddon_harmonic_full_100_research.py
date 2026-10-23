"""Abaddon Harmonic research physical-100 source and nonapproval guard."""
from pathlib import Path
from collections import Counter
import hashlib, json, unittest

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
REPORT=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage5_harmonic_payable_review_20261022.json"
SNAP=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage4_13_source_cards_20261022.json"
SNAP39=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json"
BASICS={"Island","Mountain","Swamp"}


def physical(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    cards=Counter()
    for line in lines:
        qty,n=line.split("x ",1)
        cards[n.removesuffix(" [Commander]")]+=int(qty)
    return lines,cards


class AbaddonHarmonicResearch(unittest.TestCase):
    def test_exact_full_harmonic_100_without_false_approval(self):
        record=json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertFalse(record["owner_ready"])
        self.assertFalse(record["owner_approval_or_new_lock"])
        self.assertTrue(record["deck3_hold"])
        self.assertTrue(record["status"].startswith("RESEARCH_ONLY"))
        trial=record["leader_alternative"]
        before_lines,before=physical(BASE)
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(),
                         record["canonical_approved_raw_sha256"])
        afterpath=ROOT/trial["path"]
        after_lines,after=physical(afterpath)
        self.assertEqual(hashlib.sha256(afterpath.read_bytes()).hexdigest(),trial["sha256"])
        self.assertEqual(sum(before.values()),100)
        self.assertEqual(sum(after.values()),100)
        self.assertEqual(after_lines[0],before_lines[0])
        self.assertEqual(len(after),trial["distinct_names"])
        self.assertTrue(all(v==1 or k in BASICS for k,v in after.items()))
        self.assertEqual(set((after-before).elements()),set(trial["adds"]))
        self.assertEqual(set((before-after).elements()),set(trial["cuts"]))
        self.assertEqual(sum((after-before).values()),6)
        self.assertEqual(sum((before-after).values()),6)
        self.assertIn("Pact of Negation",after)
        self.assertNotIn("Pyroblast",after)
        self.assertTrue(record["still_missing"])

    def test_selected_source_challengers_legal_but_only_hypotheses(self):
        report=json.loads(REPORT.read_text(encoding="utf-8"))
        s=json.loads(SNAP.read_text(encoding="utf-8"))["oracle_cards"]
        s.update(json.loads(SNAP39.read_text(encoding="utf-8"))["oracle_cards"])
        for name in report["leader_alternative"]["adds"]:
            self.assertIn(name,s)
            self.assertEqual(s[name]["commander_legality"],"legal")
            self.assertTrue(set(s[name]["color_identity"]) <= {"U","B","R"})
        self.assertTrue(any("Rule of Law" in row["condition"]
                            for row in report["adverse_scenarios"]))
        self.assertIn("Harmonic Prodigy",report["leader_alternative"]["adds"])


if __name__=="__main__":
    unittest.main()
