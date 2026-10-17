"""Secondary Step C dependency replay source/inventory guard."""
import unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_mox_dependency_proof as p

class TestDependencyScope(unittest.TestCase):
    def test_exact_module_set(self):
        self.assertEqual(set(p.MODULES),{"mana_timing","mana_opportunity","mana_resilience"})
    def test_frozen_sources_are_present_and_different_layer(self):
        a=p.load(p.STATIC)
        self.assertEqual(a["count"],25)
        for row in a["rows"]:
            for name in p.MODULES:
                self.assertTrue((p.ROOT/"data/grixis"/name/(row["slug"]+".json")).is_file())
    def test_scope_cannot_mutate_authority(self):
        self.assertTrue(all(v is False for v in p.AUTH.values()))

if __name__=="__main__":unittest.main()
