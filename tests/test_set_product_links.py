"""Portable Phase 1B Scryfall set metadata / exact parent-link regressions."""
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from audit_set_product_links import build, clean


def entry(code, kind, *, parent=None, released="2020-01-01", digital=False):
    return {"id": "id-" + code, "code": code, "name": "Test " + code,
            "set_type": kind, "parent_set_code": parent, "released_at": released,
            "digital": digital, "card_count": 100, "scryfall_uri": "https://scryfall.com/sets/" + code}


def atlas(codes):
    return {"source_sha256": "frozen-printing-source",
            "sets": {code: {"name": "Test " + code, "set_type": "expansion" if code == "aaa" else "promo",
                            "printings": 12, "released_distinct_oracle_ids": 8}
                     for code in codes}}


def snapshot(rows):
    return {"source_url": "https://api.scryfall.com/sets", "snapshot_date": "2026-10-29",
            "fetched_utc": "2026-10-29T23:15:00+00:00", "scryfall_sets": clean(rows)}


class ProductLinkTests(unittest.TestCase):
    def test_explicit_parent_statuses_and_source_category_not_premier(self):
        raw = [entry("aaa", "expansion"), entry("pa", "promo", parent="aaa"),
               entry("future", "expansion", released="2026-11-13"),
               entry("digital", "core", digital=True),
               entry("unknown", "promo", parent="not-printed")]
        source = snapshot(raw)
        catalog, summary = build(source, atlas(["aaa", "pa", "future", "digital", "unknown"]))
        self.assertEqual(catalog["pa"]["parent_set_code"], "aaa")
        self.assertEqual(catalog["unknown"]["parent_set_code"], "not-printed")
        self.assertFalse(next(x for x in summary["direct_parent_relationships"]
                              if x["child"] == "unknown")["parent_in_scryfall_set_snapshot"])
        self.assertEqual(catalog["future"]["release_status_as_of_cutoff"], "announced_future")
        self.assertEqual(summary["counts"]["released_nondigital_expansion_core_candidates_NOT_premier_certification"], 1)
        self.assertEqual(catalog["aaa"]["premier_release_status"], "not_independently_certified")
        self.assertEqual(catalog["aaa"]["scryfall_card_count_at_fetch"], 100)
        self.assertEqual(catalog["aaa"]["printing_records_in_oct29_default_cards"], 12)

    def test_missing_metadata_preserved_not_guessed(self):
        catalog, summary = build(snapshot([entry("aaa", "expansion")]), atlas(["aaa", "zz"]))
        self.assertTrue(catalog["zz"]["scryfall_set_metadata_missing"])
        self.assertEqual(summary["mapped_codes"], 1)
        self.assertEqual(len(summary["warnings"]), 1)

    def test_reject_duplicate_codes_invalid_dates_and_self_parent(self):
        with self.assertRaisesRegex(ValueError, "duplicated"):
            clean([entry("aaa", "expansion"), entry("aaa", "promo")])
        with self.assertRaises(ValueError):
            clean([entry("abc", "promo", released="2026-52-50")])
        with self.assertRaisesRegex(ValueError, "self-referential"):
            build(snapshot([entry("aaa", "expansion", parent="aaa")]), atlas(["aaa"]))

    def test_derived_output_is_stable(self):
        s = snapshot([entry("aaa", "expansion"), entry("bbb", "promo", parent="aaa")])
        a = atlas(["aaa", "bbb"])
        self.assertEqual(build(s, a), build(s, a))


if __name__ == "__main__":
    unittest.main()
