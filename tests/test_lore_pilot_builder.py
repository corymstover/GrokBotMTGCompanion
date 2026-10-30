"""Tests for the spec-driven Phase 6 pilot builder and audit (offline, synthetic fixtures)."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pilot as A  # noqa: E402
import build_lore_pilot as B  # noqa: E402

PILOT1 = ROOT / "data/lore_decks/specs/pilot1_ugin_bolas_elder_dragon_duality.json"
UID = "00000000-0000-0000-0000-{:012d}"


def card(name, n, ident=("U",), legal="legal", gc=False):
    return {"name": name, "set": "tst", "collector_number": str(n), "id": UID.format(n),
            "oracle_id": UID.format(1000 + n), "illustration_id": UID.format(2000 + n), "artist": "X",
            "released_at": "2020-01-01", "flavor_text": "Flavor.", "legalities": {"commander": legal},
            "color_identity": list(ident), "type_line": "Creature", "game_changer": gc,
            "promo": False, "border_color": "black", "full_art": False, "set_type": "expansion"}


def mini_spec():
    row = lambda name, n: {"name": name, "set": "tst", "collector_number": str(n), "tier": "CANON_REFERENCE",
                           "source_id": "s", "claims": [], "why": "test"}
    return {"schema": "lore-pilot-spec/v1", "stem": "test_pilot", "theme": "T",
            "status": "UNAPPROVED PROPOSAL - test; not approved, not locked, not certified",
            "color_identity": ["U"], "narrator_note": "n", "sources": {"s": "https://magic.wizards.com/en/x",
                                                                       "scryfall_card_text": "scryfall-snapshot:printed_flavor_or_name"},
            "commander": row("Cmdr", 1), "acts": [{"title": "I", "lore_keys": [], "cards": [row("Story", 2)]}],
            "story_lands": {"title": "Lands", "lore_keys": [], "cards": []},
            "playability": {"names": ["Rock"], "why": "fn"}, "basics": {"Island": 97},
            "canon_caveats": [], "unrepresentable_in_identity": [], "archidekt_tags": ["a", "b", "c"],
            "tier_definitions": {}}


def db(**over):
    d = {"Cmdr": [card("Cmdr", 1)], "Story": [card("Story", 2)], "Rock": [card("Rock", 3, ident=())]}
    d.update(over)
    return d


class BuilderTests(unittest.TestCase):
    def test_minimal_spec_builds_100(self):
        prop, ev, deck, imp = B.build(mini_spec(), db(), {"id": "t"})
        self.assertEqual(prop["counts"]["total"], 100)
        self.assertTrue(deck.startswith("1x Cmdr (tst) 1 [Commander]"))
        self.assertFalse(any(prop["approval"][k] for k in ("approved", "locked", "certified")))
        self.assertEqual(imp.splitlines()[0], "1x Cmdr")

    def test_off_identity_rejected(self):
        with self.assertRaises(SystemExit):
            B.build(mini_spec(), db(Story=[card("Story", 2, ident=("R",))]), {})

    def test_illegal_rejected(self):
        with self.assertRaises(SystemExit):
            B.build(mini_spec(), db(Story=[card("Story", 2, legal="banned")]), {})

    def test_count_must_be_100(self):
        s = mini_spec()
        s["basics"] = {"Island": 96}
        with self.assertRaises(SystemExit):
            B.build(s, db(), {})

    def test_singleton_enforced(self):
        s = mini_spec()
        s["playability"]["names"] = ["Story"]
        with self.assertRaises(SystemExit):
            B.build(s, db(), {})

    def test_game_changer_ceiling(self):
        s = mini_spec()
        s["game_changer_ceiling"] = 0
        with self.assertRaises(SystemExit):
            B.build(s, db(Rock=[card("Rock", 3, ident=(), gc=True)]), {})

    def test_spec_cannot_be_approved(self):
        s = mini_spec()
        s["status"] = "APPROVED by bot"
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(s, fh)
        with self.assertRaises(B.SpecError):
            B.load_spec(fh.name)

    def test_spec_basics_must_match_colours(self):
        s = mini_spec()
        s["basics"] = {"Mountain": 97}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(s, fh)
        with self.assertRaises(B.SpecError):
            B.load_spec(fh.name)


class AuditTests(unittest.TestCase):
    def test_every_committed_spec_passes(self):
        specs = sorted(A.SPECS.glob("*.json"))
        self.assertIn(PILOT1, specs)
        for s in specs:
            r = A.audit(s)
            self.assertEqual((r["result"], r["total"]), ("PASS", 100))
            self.assertTrue(r["status"].startswith("UNAPPROVED"))
            B.load_spec(s)

    def test_pilot1_spec_reproduces_committed_hash(self):
        # The generic builder reproduced Pilot 1 byte-for-byte against the Oct 29 snapshot;
        # the audit pins the same SHA-256 that PR #823 recorded.
        self.assertEqual(A.audit(PILOT1)["decklist_sha256"],
                         "01d087aa2819b1ed3c7ac1f64843f76f36b551b72fda62d64218d19c40b0ab45")

    def test_spec_drift_is_caught(self):
        spec = json.loads(PILOT1.read_text())
        bad = copy.deepcopy(spec)
        bad["acts"][0]["cards"][0]["name"] = "Some Other Card"
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(bad, fh)
        with self.assertRaises(ValueError):
            A.audit(fh.name)


if __name__ == "__main__":
    unittest.main()
