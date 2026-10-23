"""Candidate-specific M6 J resource/red-team evidence, not a final J certificate."""
import hashlib
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
PRE = ROOT / "data/grixis/m6/certification_preflight"
MANA = PRE / "Abaddon_stage18_protected_six_mana_20261023.md"
RED = PRE / "Abaddon_stage18_protected_six_red_team_20261023.md"
CAND = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage13_protected_wheel_six_research_20261023.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Stage17_95_Source_Reconciled_20261023.json"
BASE = "0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"
PROPOSED = "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24"


class AbaddonStage18JPrerequisites(unittest.TestCase):
    def test_exact_source_preservation_and_scope(self):
        o = json.loads(ORACLE.read_text(encoding="utf-8"))
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(), PROPOSED)
        self.assertEqual(o["candidate_sha256"], PROPOSED)
        self.assertEqual(o["base_sha256"], BASE)
        for p in (MANA, RED):
            s = p.read_text(encoding="utf-8")
            for h in (BASE, PROPOSED):
                self.assertIn(h, s)
            self.assertIn("not", s.lower())
            self.assertTrue(len(s) > 4500)
            for name in ("Impact Tremors", "Sanctum of Stone Fangs", "Coruscation Mage",
                         "Sakashima of a Thousand Faces", "Mount Doom",
                         "Sheoldred, the Apocalypse", "Ponder", "Keeper of Secrets"):
                self.assertIn(name, s)

    def test_resources_real_not_free_and_adverse_conditions(self):
        m = MANA.read_text(encoding="utf-8")
        self.assertIn("seven physical fetch", m)
        self.assertIn("34 lands", m)
        self.assertIn("double-black", m)
        self.assertIn("two basic Mountains", m)
        self.assertIn("two extra generic", m)
        self.assertIn("no seventh cosmetic land swap", m)
        self.assertIn("does not calculate an observed", m)
        r = RED.read_text(encoding="utf-8")
        for condition in ("Rule of Law", "Drannith Magistrate", "opponent", "postcast",
                          "Keeper of Secrets", "Nalfeshnee", "Noise Marine"):
            if condition == "postcast":
                self.assertIn("21 triggers *after* the wheel was cast", r)
            else:
                self.assertIn(condition, r)
        self.assertIn("Formal fresh M6 I tested-pool selection and M6 J", r)


if __name__ == "__main__":
    unittest.main()
