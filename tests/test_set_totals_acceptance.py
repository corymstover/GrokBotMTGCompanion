"""Qualified set totals must never turn Scryfall category codes into a canon premier count."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_set_totals_acceptance as S


class QualifiedSetTotalsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = S.build()

    def corrupt(self, path: Path, mutate, message):
        data = json.loads(path.read_text(encoding="utf-8"))
        mutate(data)
        with tempfile.TemporaryDirectory() as folder:
            temp = Path(folder) / path.name
            temp.write_text(json.dumps(data), encoding="utf-8")
            arg = {S.SCOPE: "scope_path", S.CATALOG: "catalog_path", S.GATES: "gates_path"}[path]
            with self.assertRaisesRegex(ValueError, message):
                S.build(**{arg: temp})

    def test_exact_distinct_qualified_denominators(self):
        r = self.report
        c = r["counts"]
        self.assertEqual(c["all_scryfall_set_codes"], 1062)
        self.assertEqual(c["scryfall_expansion_or_core_category_all_dates"], 145)
        self.assertEqual(c["released_nondigital_expansion_or_core_candidates_at_cutoff"], 142)
        self.assertEqual(c["wizards_sourced_historical_regular_mainline_subset"], 136)
        self.assertEqual(c["wizards_sourced_documented_auxiliary_not_regular_mainline"], 4)
        self.assertEqual(c["provisional_foreign_border_variants_without_primary_confirmation"], 2)
        self.assertEqual(len(r["first_party_source_cited_codes"]), 140)
        self.assertFalse(r["all_time_wizards_premier_census_certified"])
        self.assertEqual(sum(c["scryfall_set_types"].values()), 1062)

    def test_fabricated_all_time_premier_certification_rejected(self):
        self.corrupt(S.SCOPE, lambda x: x.update(all_time_premier_set_count_certified=True),
                     "unverified all-time")

    def test_missing_code_cannot_be_ignored(self):
        self.corrupt(S.SCOPE, lambda x: x["set_scope_records"].pop("lea"), "not exhaustive")

    def test_source_free_regular_mainline_is_rejected(self):
        self.corrupt(S.SCOPE, lambda x: x["set_scope_records"]["lea"].update(wizards_release_source=None),
                     "no Wizards evidence")

    def test_false_first_party_url_is_rejected(self):
        self.corrupt(S.SCOPE, lambda x: x["set_scope_records"]["lea"]
                     .update(wizards_release_source="https://example.invalid/sets"), "no Wizards evidence")

    def test_foreign_border_cannot_be_upgraded_to_primary(self):
        self.corrupt(S.SCOPE, lambda x: x["set_scope_records"]["fbb"]
                     .update(wizards_release_source="https://magic.wizards.com/unknown"),
                     "localized border variant was promoted")

    def test_product_category_drift_rejected(self):
        self.corrupt(S.CATALOG, lambda x: x["sets"]["bro"].update(scryfall_set_type="commander"),
                     "per-type Scryfall totals disagree")

    def test_released_paper_candidate_classification_drift_rejected(self):
        self.corrupt(S.CATALOG, lambda x: x["sets"]["bro"].update(digital_only=True),
                     "candidate roster drifted")

    def test_stale_artifact_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            stale = Path(folder) / "stale.json"
            stale.write_text("{}\n", encoding="utf-8")
            with patch.object(S, "OUT", stale):
                with self.assertRaisesRegex(ValueError, "stale"):
                    S.main(["--check"])


if __name__ == "__main__":
    unittest.main()
