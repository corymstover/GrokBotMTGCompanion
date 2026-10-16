"""Shared helpers for the Bot cycle 47 test suite (plain asserts; runs under pytest or scripts/run_tests.py)."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_authority as ga  # noqa: E402

_R = []


def resolver():
    """The real card resolver (Scryfall bulk cache), loaded once per run."""
    if not _R:
        import evaluate_decklist as ev
        _R.append(ev.Resolver())
    return _R[0]


def skip(msg):
    raise unittest.SkipTest(msg)


class FakeR:
    """Minimal resolver: name -> card with a deterministic oracle_id."""

    def get(self, name):
        if name.startswith("Unknown"):
            return None, None
        return {"name": name, "oracle_id": "oid-" + name.lower().replace(" ", "-")}, None


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


MILESTONES_OK = {"M2": {"status": "accepted", "accepted_by": "corymstover"}, "M4": {"status": "accepted", "accepted_by": "corymstover"}}
MILESTONES_NOT = {"M2": {"status": "not_started", "accepted_by": None}, "M4": {"status": "not_started", "accepted_by": None}}
APPROVERS = {"corymstover"}
H = "lh1:" + "a" * 64


def entry(state="SOURCE_BASELINE", history=None, **kw):
    """A minimal registry deck entry for state/approval tests."""
    hist = history or ["SOURCE_BASELINE"]
    e = {"state": state, "state_history": [{"state": s, "date": "2026-10-16", "cycle": 47, "reason": "test"} for s in hist],
         "approval": {"state": None, "cycle": None, "date": None, "by": None, "record_id": None},
         "current_canonical_hash": H, "official_legal_projection": None, "challengers": [], "finalization_certificate": None,
         "ceiling": {"source_ceiling": {"value": "4"}, "grok_estimated_ceiling": {"value": None}, "resolved_ceiling": {"value": None, "resolved_by": None},
                     "disagreement": None}}
    e.update(copy.deepcopy(kw))
    return e


APPROVED_PATH = ["SOURCE_BASELINE", "UNDER_REVIEW", "TESTING", "APPROVAL_READY", "APPROVED"]


def record(decision="APPROVED", by="corymstover", list_hash=H, rid="appr-1"):
    return {"id": rid, "deck_id": "D", "list_hash": list_hash, "decision": decision, "approved_by": by, "date": "2026-12-01",
            "instruction": "test", "recorded_by": "grokbot", "recorded_cycle": 60}
