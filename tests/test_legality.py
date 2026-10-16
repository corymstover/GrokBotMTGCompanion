"""Official Commander legality is kept separate from project authorization; exceptions are never reported as legal."""
import json
import re
import tempfile
from pathlib import Path

from _helpers import APPROVERS, H, MILESTONES_NOT, ROOT, entry, ga, load, record

OFFICIAL = ("legal", "banned", "banned_as_companion", "not_legal", "not_legal_until_release")
AUTH = ("AUTHORIZED_EXCEPTION", "AUTHORIZED_FUTURE_RELEASE", "NOT_REQUIRED", "UNAUTHORIZED")
BJ = "Cecily__Bjorna__Lutri"


def _claims_legal(label):
    return bool(re.search(r"(?<!NOT )Commander-legal(?! yet)", label)) and "NOT" not in label and "not Commander-legal" not in label


def test_label_never_calls_a_non_legal_card_legal():
    for o in OFFICIAL:
        for a in AUTH:
            lab = ga.legality_label(o, a, "2026-11-13")
            if o == "legal":
                assert lab == "Commander-legal"
            else:
                assert not _claims_legal(lab), (o, a, lab)
    assert "project exception" in ga.legality_label("banned", "AUTHORIZED_EXCEPTION")
    assert "legal from 2026-11-13" in ga.legality_label("not_legal_until_release", "AUTHORIZED_FUTURE_RELEASE", "2026-11-13")


def _tmp_exceptions(rows):
    f = Path(tempfile.mkdtemp()) / "exceptions.json"
    f.write_text(json.dumps({"exceptions": rows}), encoding="utf-8")
    return f


def test_only_registered_authorized_legality_issues_are_accepted():
    f = _tmp_exceptions([{"deck_id": "D", "card": "Trade Secrets", "project_authorization_status": "AUTHORIZED_EXCEPTION"},
                         {"deck_id": "D", "card": "Madcap Jester", "project_authorization_status": "AUTHORIZED_FUTURE_RELEASE"},
                         {"deck_id": "D", "card": "Nazgul", "project_authorization_status": "NOT_REQUIRED"}])
    issues = [{"type": "banned", "card": "Trade Secrets"}, {"type": "color identity", "card": "Trade Secrets"},
              {"type": "banned", "card": "Mana Crypt"}, {"type": "not Commander-legal", "card": "Madcap Jester"},
              {"type": "singleton", "card": "Nazgul"}]
    keep, acc = ga.accepted_hard_issues("D", issues, f)
    assert acc == [{"type": "banned", "card": "Trade Secrets"}]
    assert {"type": "color identity", "card": "Trade Secrets"} in keep  # identity is never excused
    assert {"type": "not Commander-legal", "card": "Madcap Jester"} in keep  # future release has its own date-bounded path
    keep2, acc2 = ga.accepted_hard_issues("OTHER", issues, f)
    assert acc2 == [] and len(keep2) == len(issues)


def test_projection_rules():
    pj = {"label": ga.PROJECTION_LABEL, "canonical": False, "approval_state": None, "hash": "lh1:" + "d" * 64}
    assert ga.approval_problems("D", entry(official_legal_projection=pj), [], APPROVERS, MILESTONES_NOT) == []
    for bad in ({"canonical": True}, {"approval_state": "APPROVED"}, {"label": "official list"}, {"hash": H}):
        p = ga.approval_problems("D", entry(official_legal_projection={**pj, **bad}), [], APPROVERS, MILESTONES_NOT)
        assert p, bad
    p = ga.approval_problems("D", entry(official_legal_projection=pj), [record(list_hash=pj["hash"])], APPROVERS, MILESTONES_NOT)
    assert any("projections are never approved" in x for x in p)


def test_projection_text_substitutes_and_drops_companion():
    proj = {"decks": {"D": {"substitutions": [{"from": "Trade Secrets", "to": "Wizard Class"}], "drop_companion": "Lutri, the Spellchaser"}}}
    canon = "1x Cmd [Commander{top}]\n1x Lutri, the Spellchaser [Companion]\n1x Trade Secrets [Draw]\n1x Island\n"
    out = ga.projection_text("D", canon, proj)
    assert "Wizard Class [Draw]" in out and "Trade Secrets" not in out and "Lutri" not in out and "Island" in out
    assert ga.projection_text("OTHER", canon, proj) is None


def test_bjorna_canonical_keeps_exceptions_and_is_never_legal():
    reg = load("data/grixis/registry.json")
    e = reg["decks"][BJ]
    assert e["official_commander_compliance"]["status"] == "not_compliant_project_exceptions"
    assert e["project_authorization_status"] == "authorized_exceptions"
    assert e["canonical_project_list"]["companion"] == "Lutri, the Spellchaser"
    canon = ga.deck_block_text(e["slug"])
    for c in ("Trade Secrets", "Yawgmoth's Bargain"):
        assert re.search(r"^1x " + re.escape(c) + r"\b", canon, re.M), c
    assert "1x Lutri, the Spellchaser [Companion]" in canon
    pj = e["official_legal_projection"]
    assert pj["official_commander_compliance"] == "compliant" and pj["canonical"] is False and pj["approval_state"] is None
    page = (ROOT / "grixis" / "decks" / f"{e['slug']}.md").read_text(encoding="utf-8")
    assert "validated: false" in page and "official_commander_compliance: not_compliant_project_exceptions" in page
    assert "✅ **all checks pass**" not in page
    assert "🚩 **PROJECT EXCEPTIONS — not Commander-legal.**" in page


def test_every_other_deck_is_compliant_or_pending():
    reg = load("data/grixis/registry.json")
    for did, e in reg["decks"].items():
        if did == BJ:
            continue
        assert e["official_commander_compliance"]["status"] in ("compliant", "pending_release"), did
        assert e["official_legal_projection"] is None
        if e["official_commander_compliance"]["status"] == "pending_release":
            assert e["state"] == "PENDING_RELEASE" and e["project_authorization_status"] == "authorized_future_release"


def test_exception_registry_rows():
    exc = load("data/grixis/exceptions.json")["exceptions"]
    assert len(exc) == 8
    for x in exc:
        if x["official_commander_legality"] != "legal":
            assert x["project_authorization_status"] in ("AUTHORIZED_EXCEPTION", "AUTHORIZED_FUTURE_RELEASE"), x["id"]
            assert x["authorized_by"]
        assert x["render_label"] == ga.legality_label(x["official_commander_legality"], x["project_authorization_status"], x["legal_from"])
        assert not (x["official_commander_legality"] != "legal" and _claims_legal(x["render_label"])), x["id"]
    naz = [x for x in exc if x["card"].startswith("Nazg")]
    assert len(naz) == 2 and all(x["official_commander_legality"] == "legal" and x["project_authorization_status"] == "NOT_REQUIRED" for x in naz)
    assert sum(1 for x in exc if x["verification"]["status"] == "corrected") == 4
    bj = {x["card"]: x for x in exc if x["deck_id"] == BJ}
    assert bj["Lutri, the Spellchaser"]["official_commander_legality"] == "banned_as_companion"
    assert all(x["in_canonical_project_list"] for x in bj.values())


def test_exports_label_every_file():
    man = load("exports/grixis-archidekt/index.json")["files"]
    roles = {}
    for x in man:
        roles.setdefault(x["deck_id"], []).append(x["role"])
        if x["role"] == "projection":
            assert x["label"] == ga.PROJECTION_LABEL and x["state"] is None and x["official_commander_compliance"] == "compliant"
        if x["role"] == "challenger":
            assert x["label"] == ga.CHALLENGER_LABEL and x["state"] == "CHALLENGER"
        if x["role"] == "canonical":
            assert x["label"] == ga.BASELINE_LABEL and x["state"] in ("SOURCE_BASELINE", "PENDING_RELEASE")
    assert len(roles) == 62 and all(r.count("canonical") == 1 for r in roles.values())
    bj = [x for x in man if x["deck_id"] == BJ and x["role"] == "canonical"][0]
    assert bj["official_commander_compliance"] == "not_compliant_project_exceptions"
    readme = (ROOT / "exports" / "grixis-archidekt" / "README.md").read_text(encoding="utf-8")
    assert ga.CHALLENGER_LABEL in readme and ga.PROJECTION_LABEL in readme
