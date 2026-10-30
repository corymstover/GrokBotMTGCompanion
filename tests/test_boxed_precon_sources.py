"""Wizards product evidence and Scryfall scheme/plane component tests."""
import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
import audit_boxed_precon_sources as A

class BoxedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base=json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous=json.loads(A.PREV.read_text(encoding="utf-8"))
        cls.ledger=json.loads(A.LEDGER.read_text(encoding="utf-8"))
    def build(self,ledger=None):
        return A.build(self.base,self.previous,self.ledger if ledger is None else ledger)

    def test_all_848_codes_and_current_86_762_partition(self):
        j=self.build()
        self.assertEqual(j["new_source_backed_product_codes"],15)
        self.assertEqual(j["new_component_codes_of_parent_products"],5)
        self.assertEqual(j["new_box_or_collection_products"],10)
        self.assertEqual(j["cumulative_family_source_backed_codes"],86)
        self.assertEqual(j["cumulative_source_pending_codes"],762)
        self.assertEqual(j["boxed_source_pending_after_batch"],95)
        self.assertEqual(len(j["remaining_source_pending_queue"]),762)
        self.assertEqual(86+762,848)

    def test_schemes_and_planar_cards_are_components_not_products(self):
        rows={x["code"]:x for x in self.build()["reviewed_boxed_codes"]}
        for code,parent in A.COMPONENT_PARENT.items():
            x=rows[code]
            self.assertEqual(x["parent_product_code_when_component"],parent)
            self.assertTrue(x["component_of_existing_parent_product"])
            self.assertFalse(x["standalone_booster_expansion"])
            self.assertEqual(x["separate_sold_box_vs_card_component"],"packaged_game_card_component")
        for code in ("arc","e01","hop","pc2","pca","cma","cm2","cc1","cc2","cm1"):
            self.assertFalse(rows[code]["component_of_existing_parent_product"])
            self.assertEqual(rows[code]["separate_sold_box_vs_card_component"],"boxed_or_collection_release")
        self.assertTrue(all(not x["premier_set_status_certified"] for x in rows.values()))

    def test_duplicate_nonwizards_bad_parent_premier_inference_rejected(self):
        data=copy.deepcopy(self.ledger)
        data["records"].append(copy.deepcopy(data["records"][0]))
        with self.assertRaisesRegex(ValueError,"Duplicate"):self.build(data)
        data=copy.deepcopy(self.ledger)
        data["records"][0]["source_url"]="https://example.org/"
        with self.assertRaisesRegex(ValueError,"Non-Wizards"):self.build(data)
        data=copy.deepcopy(self.ledger)
        x=next(x for x in data["records"] if x["code"]=="ohop")
        x["group"]="planechase_2009_preconstructed_release"
        with self.assertRaisesRegex(ValueError,"Component promoted"):self.build(data)

    def test_repeatable_and_history_preserved(self):
        self.assertEqual(A.encode(self.build()),A.encode(self.build()))
        self.assertEqual(self.previous["cumulative_family_source_backed_codes"],71)
        self.assertEqual(self.previous["cumulative_pending_codes"],777)

if __name__=="__main__":unittest.main()
