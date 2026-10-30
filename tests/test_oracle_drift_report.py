"""Synthetic-fixture tests for scripts/oracle_drift_report.py (no snapshot download needed)."""
import gzip
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import oracle_drift_report as R  # noqa: E402

OID1, OID2, OID3 = ("11111111-1111-1111-1111-111111111111", "22222222-2222-2222-2222-222222222222",
                    "33333333-3333-3333-3333-333333333333")
SHARD = f"""# A

### Alpha Bolt

- **Oracle text:**
  > Alpha Bolt deals 3 damage to any target.
- **Flavor text** (ABC printing):
  > *A flash of light.*
- **Source flags:** oracle_id `{OID1}` · source: Scryfall oracle_cards bulk 2026-10-15

### Beta Golem

- **Oracle text:**
  > Vigilance
- **Source flags:** oracle_id `{OID2}` · source: Scryfall oracle_cards bulk 2026-10-15
"""
INDEX = ("name,oracle_id,shard,anchor,edhrec_rank,color_identity,type_line,commander_legality,game_changer,batch,rulings\n"
         f"Alpha Bolt,{OID1},cards/A/al.md,alpha-bolt,,R,Instant,legal,0,b,0\n"
         f"Beta Golem,{OID2},cards/A/al.md,beta-golem,,C,Artifact Creature — Golem,legal,0,b,0\n")


def card(oid, name, text, ci, tl, legal="legal", gc=False, **kw):
    return dict(oracle_id=oid, name=name, oracle_text=text, color_identity=ci, type_line=tl,
                legalities={"commander": legal}, game_changer=gc, layout="normal", **kw)


class DriftTests(unittest.TestCase):
    def _run(self, cards):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "cards/A").mkdir(parents=True)
            (root / "data").mkdir()
            (root / "cards/A/al.md").write_text(SHARD, encoding="utf-8")
            (root / "data/card_index.csv").write_text(INDEX, encoding="utf-8")
            snap = root / "oracle-cards-20261029090202.jsonl.gz"
            with gzip.open(snap, "wt", encoding="utf-8") as fh:
                for c in cards:
                    fh.write(json.dumps(c) + "\n")
            return R.report(snap, root)

    def test_identical_snapshot_reports_no_drift(self):
        r = self._run([card(OID1, "Alpha Bolt", "Alpha Bolt deals 3 damage to any target.", ["R"], "Instant"),
                       card(OID2, "Beta Golem", "Vigilance", [], "Artifact Creature — Golem")])
        self.assertTrue(all(v == 0 for v in r["counts"].values()), r["counts"])
        self.assertEqual(r["snapshot_date"], "2026-10-29")

    def test_detects_text_legality_and_new_cards(self):
        r = self._run([card(OID1, "Alpha Bolt", "Alpha Bolt deals 2 damage to any target.", ["R"], "Instant"),
                       card(OID2, "Beta Golem", "Vigilance", [], "Artifact Creature — Golem", legal="banned", gc=True),
                       card(OID3, "Gamma Preview", "Flying", ["U"], "Creature", set="trk", set_type="expansion",
                            released_at="2026-11-13")])
        self.assertEqual(r["changed"]["oracle_text"], ["Alpha Bolt"])
        self.assertEqual(r["changed"]["commander_legality"], ["Beta Golem: legal -> banned"])
        self.assertEqual(r["changed"]["game_changer"], ["Beta Golem: 0 -> 1"])
        self.assertEqual(r["counts"]["new_in_snapshot"], 1)
        self.assertEqual(r["new_in_snapshot_breakdown"]["paper_gameplay"], 1)

    def test_flavor_text_is_not_compared(self):
        r = self._run([card(OID1, "Alpha Bolt", "Alpha Bolt deals 3 damage to any target.", ["R"], "Instant"),
                       card(OID2, "Beta Golem", "Vigilance", [], "Artifact Creature — Golem")])
        self.assertEqual(r["changed"]["oracle_text"], [])

    def test_missing_card_is_reported(self):
        r = self._run([card(OID1, "Alpha Bolt", "Alpha Bolt deals 3 damage to any target.", ["R"], "Instant")])
        self.assertEqual(r["counts"]["missing_from_snapshot"], 1)


if __name__ == "__main__":
    unittest.main()
