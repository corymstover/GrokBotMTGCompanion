"""Phase 7 rephrased-question suite (Batch 8).

Free-text paraphrases over the Batch 7/8 relations (LCI, BLB, THB, KLD/AER, DFT, XLN/RIX, DOM/WAR,
KHM, STX, MID/VOW, THS packs). Each phrasing must reach the same committed claim and answering
node. Batch 8 added parser phrasings: "beheaded", "the leader of X", "governs", "mentored"/"X's
mentor", "founded", "guards", "fought", "serves", "worships", "attacked", "who did X meet", and
friend_of/childhood_friend_of for "X's friends". Answers come only from the committed claim graph;
sources must be official magic.wizards.com pages. These packs are PRELIMINARY_RESEARCH: the suite
checks retrieval faithfulness, not owner approval of the canon.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask as A  # noqa: E402

# (phrasings, expected claim, expected answering node, cited-claim confidence)
# v2.82: present-tense leadership answers now qualify current office separately
# even where the underlying historical claim remains CANON_CONFIRMED.
CASES = [
    (["Who killed the Buried Lord?", "Who was the Buried Lord killed by?", "Who beheaded the Buried Lord?"],
     "MV016", "character:liesa", "VERIFIED"),
    (["Who killed Isperia?", "Who murdered Isperia?"], "WR001", "character:vraska", "VERIFIED"),
    (["Who leads the Omenseekers?", "Who runs the Omenseekers?", "Who is the leader of the Omenseekers?"],
     "KH020", "character:inga_rune_eyes", "VERIFIED"),
    (["Who is Killian Lu's parent?"],
     "SX017", "character:embrose_lu", "VERIFIED"),
    (["Who is Torens's brother?", "Who are Torens's siblings?"], "MV023", "character:elamon", "VERIFIED"),
    (["Who defeated Xenagos?"], "TS033", "character:elspeth_tirel", "VERIFIED"),
    (["Who leads Tynthal?", "Who governs Tynthal?"], "TS030", "character:pilun", "VERIFIED"),
    (["Who imprisoned Pia Nalaar?"], "KLD011", "faction:consulate", "VERIFIED"),
    (["Who leads the Consulate?"], "AER016", "character:tezzeret", "VERIFIED"),
    (["Who leads the Sun Empire?"], "XLN023", "character:apatzec_intli", "VERIFIED"),
    (["Who founded the Sun Empire?"], "XLN024", "character:chacanto_intli", "VERIFIED"),
    (["Who guards the Immortal Sun?"], "XLN021", "character:elenda", "VERIFIED"),
    (["Who mentored Kopala?"], "XLN027", "character:tishana", "VERIFIED"),
    (["Who is Khrad's parent?"], "DF021", "character:khal", "VERIFIED"),
    (["Who leads the Brazen Coalition?", "Who captains the Brazen Coalition?"],
     "XLN019", "character:beckett_brass", "VERIFIED"),
    (["Who leads the Telu set?"], "DF022", "character:khal", "VERIFIED"),
    (["Who mentored Melantha?", "Who was Melantha's mentor?"], "TS025", "character:xenocrates", "VERIFIED"),
    (["Who attacked Thraben?"], "MV014", "character:wilhelt", "VERIFIED"),
    (["Who is Zimone's friend?", "Who are Zimone's friends?"], "SX012", "character:amaka", "VERIFIED"),
    (["Who fought Lukka?"], "SX015", "character:kasmina", "VERIFIED"),
    (["Who did Kaya meet?"], "KH021", "character:inga_rune_eyes", "VERIFIED"),
    (["Who serves Ephara?"], "TS034", "character:iris_oracle", "VERIFIED"),
    # CANON_IMPLIED claims: the envelope must be QUALIFIED, never VERIFIED
    (["Who is Vadrik's husband?", "Who is Vadrik's spouse?"], "MV021", "character:hailin", "QUALIFIED"),
    (["Who leads the Tuskeri?"], "KH016", "character:arni_brokenbrow", "QUALIFIED"),
    (["Who is Gisa's brother?", "Who are Gisa's siblings?"], "MV015", "character:geralf", "QUALIFIED"),
    (["Who is Leinore's sister?"], "MV022", "character:sinnia", "QUALIFIED"),
    (["Who worships Elenda?"], "XLN032", "character:mavren_fein", "QUALIFIED"),
]


def _rows(env):
    return [r for rows in env.get("result", {}).get("relations_by_status", {}).values() for r in rows]


class RephrasedB8(unittest.TestCase):
    def test_every_phrasing_reaches_the_same_claim(self):
        for phrasings, claim, node, conf in CASES:
            for q in phrasings:
                with self.subTest(q=q):
                    env = A.ask(q)
                    present_leader = ('leadership' in env.get('result', {}) and
                                      A._PRESENT_LEADER_QUESTION.search(q) is not None)
                    self.assertEqual(env["confidence"], 'QUALIFIED' if present_leader else conf, q)
                    if present_leader:
                        self.assertIn('CURRENT_LEADER_NOT_ESTABLISHED', env['flags'])
                        self.assertIsNone(env['result']['leadership']['verified_current_leader'])
                    hits = [r for r in _rows(env) if r["claim"] == claim]
                    self.assertTrue(hits, f"{q}: {claim} not among {[r['claim'] for r in _rows(env)]}")
                    self.assertEqual(hits[0]["node"], node)
                    self.assertEqual(hits[0]['status'],
                                     'CANON_CONFIRMED' if conf == 'VERIFIED' else 'CANON_IMPLIED')
                    for u in env["sources"]:
                        self.assertTrue(u.startswith("https://magic.wizards.com/"), u)

    def test_qualified_answers_carry_a_limitation(self):
        for phrasings, claim, _node, conf in CASES:
            if conf != "QUALIFIED":
                continue
            env = A.ask(phrasings[0])
            hit = [r for r in _rows(env) if r["claim"] == claim][0]
            self.assertTrue(hit.get("limitation"), claim)
            self.assertNotEqual(env["confidence"], "VERIFIED")

    def test_new_phrasings_do_not_invent_answers(self):
        for q in ["Who beheaded Zzyzx the Unwritten?", "Who is the leader of the Zzyzx Fleet?",
                  "Who mentored Zzyzx?", "Who founded the Zzyzx Fleet?", "Who guards the Zzyzx Vault?",
                  "Who worships Zzyzx?", "Who did Zzyzx meet?", "Who attacked the Zzyzx Fleet?"]:
            with self.subTest(q=q):
                self.assertEqual(A.ask(q)["confidence"], "NOT_FOUND")

    def test_batch6_routes_unchanged(self):
        self.assertEqual(A.ask("Who defeated Ugin?")["route"], "ask->lore:defeated")
        self.assertEqual(A.ask("Who created Heart of Kiran?")["route"], "ask->lore:designed")


if __name__ == "__main__":
    unittest.main()
