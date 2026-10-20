import json, shutil, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "scripts"))
import grixis_m6_grokbot_advisory_check as chk
class T(unittest.TestCase):
    def setUp(self):
        self.t = Path(tempfile.mkdtemp()); (self.t / "data/grixis/m6").mkdir(parents=True)
        shutil.copytree(ROOT / chk.BASE, self.t / chk.BASE)
        shutil.copy(ROOT / "data/grixis/m6/single_deck_depth_tracker.json", self.t / "data/grixis/m6/")
    def tearDown(self): shutil.rmtree(self.t)
    def test_repo_ok(self): self.assertEqual(chk.problems(), [])
    def test_copy_ok(self): self.assertEqual(chk.problems(self.t, use_git=False), [])
    def test_stage_a_tamper(self):
        p = self.t / chk.BASE / "Abaddon_the_Despoiler/stage_a.md"; p.write_text(p.read_text() + "x")
        self.assertTrue(chk.problems(self.t, use_git=False))
    def test_formal_flag(self):
        p = self.t / chk.BASE / "Abaddon_the_Despoiler/seal.json"; j = json.loads(p.read_text()); j["formal_independent_pass_c"] = True; p.write_text(json.dumps(j))
        self.assertTrue(chk.problems(self.t, use_git=False))
if __name__ == "__main__": unittest.main()
