"""Batch 10 Phase 7: retcon/continuity explainer and in-universe date context in mv_ask answers."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask  # noqa: E402


def accounts(q):
    env = mv_ask.ask(q)
    return env, {a["claim"]: a for a in env["result"].get("continuity_accounts", [])}


class ContinuityTests(unittest.TestCase):
    def test_disputed_account_listed_not_resolved(self):
        env, acc = accounts("Explain the continuity of Brago")
        self.assertEqual(env["route"], "ask->continuity")
        self.assertIn("CN006", acc)
        self.assertEqual(acc["CN006"]["status"], "CANON_DISPUTED")
        self.assertIn("CANON_DISPUTED_PRESENT", env["flags"])
        self.assertEqual(env["confidence"], "QUALIFIED")
        self.assertIn("not resolved", env["result"]["note"])
        self.assertTrue(acc["CN006"]["source_urls"])

    def test_open_question_rephrasings(self):
        for q in ("Is Lorthos canon?", "Is Lorthos a retcon?", "Any retcons about Lorthos?",
                  "What are the conflicting accounts of Lorthos?"):
            env, acc = accounts(q)
            self.assertIn("ZN010", acc, q)
            self.assertIn("OPEN_QUESTION_PRESENT", env["flags"], q)

    def test_alternate_continuity_listed(self):
        alt = [n for n, c in mv_ask.graph().nodes.items() if c.get("type") == "Claim" and c.get("grade") == "ALTERNATE_CONTINUITY"]
        self.assertTrue(alt)
        # Find an entity asserted by A012 and confirm its explainer lists A012.
        ents = [e["to"] for e in mv_ask.graph().g["edges"] if e["from"] == "claim:A012" and e["relation"] == "asserts"]
        name = mv_ask.graph().nodes[ents[0]]["name"]
        env, acc = accounts(f"Explain the continuity of {name}")
        self.assertIn("A012", acc, name)
        self.assertEqual(acc["A012"]["status"], "ALTERNATE_CONTINUITY")

    def test_timeline_limitation_listed_with_reason(self):
        env, acc = accounts("Explain the continuity of Ugin")
        lim = [a for a in acc.values() if a["why_listed"].startswith("LIMITATION_MENTIONS:")]
        self.assertTrue(lim)
        for a in lim:
            self.assertIn(a["why_listed"].split(":", 1)[1], a["limitation"].lower())

    def test_no_conflict_is_flagged_not_invented(self):
        env, acc = accounts("Explain the continuity of Chandra Nalaar")
        if not acc:
            self.assertIn("NO_CITED_CONTINUITY_CONFLICT", env["flags"])
        env = mv_ask.ask("Is Zorblax the Unreal canon?")
        self.assertEqual(env["confidence"], "NOT_FOUND")

    def test_relation_answers_carry_quoted_date(self):
        env = mv_ask.ask("Who imprisoned the Eldrazi?")
        rows = [r for rs in env["result"]["relations_by_status"].values() for r in rs if r["claim"] == "ZN003"]
        self.assertTrue(rows)
        d = rows[0]["in_universe_date"]
        self.assertEqual(d["value"], "millennia ago")
        self.assertIn(d["value"], d["quote"])

    def test_plain_questions_unchanged(self):
        self.assertEqual(mv_ask.ask("Who is Urza's brother?")["route"], "ask->lore:sibling_of|twin_sibling_of")


if __name__ == "__main__":
    unittest.main()
