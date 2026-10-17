"""Abaddon alternative-cut and commander-role preservation proof."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_threshold_access as mod
class TestRolePreregistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=mod.load(mod.PLAN)
        cls.pk=mod.load(mod.M5)
        cls.b=mod.load(mod.BLUEPRINT)
    def test_six_variants_and_four_approved_m5_ids(self):
        v=mod.alternatives(self.p,mod.SOURCE,self.pk,self.b)
        self.assertEqual(len(v),6)
        self.assertEqual(sum(x[0]["existing_m5_id"] is not None for x in v),4)
        self.assertEqual(len(set((x[0]["add"],x[0]["cut"]) for x in v)),6)
    def test_alternates_preserve_threshold_and_minimum_cascade(self):
        v=mod.alternatives(self.p,mod.SOURCE,self.pk,self.b)
        alts=[x for x in v if x[0]["tag"]=="alternate_noncore_printed_cascade_cut"]
        self.assertEqual(len(alts),2)
        for x in alts:
            self.assertEqual(x[2]["printed_cascade_after_cut"],4)
            self.assertFalse(x[2]["removed_core_threshold"])
    def test_cannot_infer_active_effects_or_swaps(self):
        self.assertFalse(any(mod.AUTH.values()))
        self.assertFalse(any(self.p["claims"].values()))
        self.assertIn("does not model",self.p["card_effect_truth"])

if __name__=="__main__":unittest.main()
