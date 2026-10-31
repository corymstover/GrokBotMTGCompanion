"""Phase 7 rephrased-question suite (Batch 6).

The same claim should be reachable through several natural phrasings: synonyms ("murdered",
"released", "captains"), passive forms ("was X killed by"), possessives ("X's father", "X's lover")
and bare first names ("Chandra"). Answers come only from the committed claim graph, and every
source must be an official magic.wizards.com page. These claim packs are PRELIMINARY_RESEARCH:
the suite checks that retrieval is faithful, not that the canon is approved.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask as A  # noqa: E402

# (phrasings, expected claim, expected answering node, cited-claim confidence)
# v2.82 present-tense leadership is QUALIFIED even if its historical claim is confirmed.
CASES = [
    (["Who killed Vito?", "Who murdered Vito?", "Who was Vito killed by?"], "LC006", "character:huatli", "VERIFIED"),
    (["Who freed Valgavoth?", "Who released Valgavoth?"], "DS003", "character:marina_vendrell", "VERIFIED"),
    (["Who freed Niharet?", "Who liberated Niharet?"], "DF012", "character:mahitab", "VERIFIED"),
    (["Who captured Loot?", "Who took Loot captive?", "Who kidnapped Loot?"], "DF007", "character:winter", "VERIFIED"),
    (["Who captured Winter?", "Who took Winter captive?"], "DS007", "character:valgavoth", "VERIFIED"),
    (["Who imprisoned Aclazotz?", "Who sealed away Aclazotz?"], "LC003", "character:ojer_axonil", "VERIFIED"),
    (["Who is Kellan's father?"], "WE009", "character:oko", "VERIFIED"),
    (["Who is Kellan's parent?"], "OT004", "character:oko", "VERIFIED"),
    (["Who is Chandra Nalaar's lover?", "Who is Chandra's girlfriend?", "Who is Chandra's partner?"], "DF004", "character:nissa_revane", "VERIFIED"),
    (["Who is Huatli's partner?", "Who is Huatli's lover?"], "LC011", "character:saheeli", "VERIFIED"),
    (["Who leads the Champions of Amonkhet?", "Who led the Champions of Amonkhet?"], "DF002", "character:zahur", "VERIFIED"),
    (["Who captains the Guidelight Voyagers?", "Who runs the Guidelight Voyagers?"], "DF010", "character:mendicant_core", "VERIFIED"),
    (["Who won the Aetherspark?"], "DF001", "faction:champions_of_amonkhet", "VERIFIED"),
    (["Who are Jace's allies?", "Who are Jace Beleren's friends?"], "DS005", "character:kaito", "VERIFIED"),
    (["Who kidnapped Tamiyo?", "Who abducted Tamiyo?"], "NEO010", "character:tezzeret", "VERIFIED"),
    (["Who rescued Vraska?", "Who freed Vraska?"], "OT011", "character:jace_beleren", "VERIFIED"),
    (["Who killed Elesh Norn?", "Who murdered Elesh Norn?"], "MOM017", "character:karn", "VERIFIED"),
    # DS010 is CANON_IMPLIED, so the envelope must be QUALIFIED, never VERIFIED
    (["Who are Valgavoth's enemies?", "Who is Valgavoth's rival?"], "DS010", "character:alquist_proft", "QUALIFIED"),
]


def _rows(env):
    return [r for v in env.get("result", {}).get("relations_by_status", {}).values() for r in v]


class RephrasedQuestions(unittest.TestCase):
    def test_every_phrasing_reaches_the_same_claim(self):
        for phrasings, claim, node, confidence in CASES:
            for q in phrasings:
                with self.subTest(q=q):
                    env = A.ask(q)
                    present_leader = ('leadership' in env.get('result', {}) and
                                      A._PRESENT_LEADER_QUESTION.search(q) is not None)
                    self.assertEqual(env["confidence"], 'QUALIFIED' if present_leader else confidence, q)
                    if present_leader:
                        self.assertIn('CURRENT_LEADER_NOT_ESTABLISHED', env['flags'])
                    hits = [r for r in _rows(env) if r["claim"] == claim]
                    self.assertTrue(hits, f"{q}: {claim} missing")
                    self.assertEqual(hits[0]["node"], node)
                    self.assertEqual(hits[0]['status'],
                                     'CANON_CONFIRMED' if confidence == 'VERIFIED' else 'CANON_IMPLIED')
                    self.assertTrue(hits[0]["source_urls"])
                    self.assertTrue(all("magic.wizards.com" in u for u in hits[0]["source_urls"]))
                    if confidence == "QUALIFIED":
                        self.assertTrue(hits[0]["limitation"])

    def test_first_name_match_is_flagged(self):
        env = A.ask("Who is Chandra's lover?")
        self.assertIn("MATCHED_BY_FIRST_NAME", env["flags"])
        self.assertNotIn("MATCHED_BY_FIRST_NAME", A.ask("Who is Chandra Nalaar's lover?")["flags"])

    def test_ambiguous_first_name_is_not_guessed(self):
        # two characters are named "Ojer ..."; a bare first name must not pick one
        self.assertIsNone(A._first_name("Ojer"))
        self.assertIsNone(A._first_name("Ojer Somebody"))

    def test_unknown_rephrasing_still_not_found(self):
        for q in ["Who murdered Zzyzx the Unwritten?", "Who is Zzyzx's lover?", "Who captains the Zzyzx Fleet?"]:
            with self.subTest(q=q):
                self.assertEqual(A.ask(q)["confidence"], "NOT_FOUND")

    def test_existing_routes_unchanged(self):
        self.assertEqual(A.ask("Who defeated Ugin?")["route"], "ask->lore:defeated")
        self.assertEqual(A.ask("Who created Heart of Kiran?")["route"], "ask->lore:designed")
        self.assertEqual(A.ask("Who is Chandra Nalaar's mother?")["confidence"], "VERIFIED")


if __name__ == "__main__":
    unittest.main()
