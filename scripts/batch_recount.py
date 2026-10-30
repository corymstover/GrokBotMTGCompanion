"""Phase 1 / Phase 8: per-batch recount plus representative-query check (Batch 9).

Read-only. After each published batch, run this to (1) recount story coverage and graph size from the committed
artifacts and (2) re-ask a fixed set of representative questions through mv_ask and check that each one still returns
its expected cited answer with honest confidence. It writes nothing unless --out is given, and never approves,
certifies or changes data.

  python3 scripts/batch_recount.py                 # print the summary; exit 1 if any representative query fails
  python3 scripts/batch_recount.py --json --out data/release/batch_recount_YYYY-MM-DD.json

Every expected answer below is already a cited claim edge in data/multiverse_graph/multiverse_graph.json; this list
is a regression net over existing evidence, not new lore.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask  # noqa: E402

INVENTORY = ROOT / "data/lore_research/story_coverage_inventory_2026-10-30.json"
GRAPH = ROOT / "data/multiverse_graph/multiverse_graph.json"

# (question, a name that must appear among the answers, allowed confidences, flags that must be present)
REPRESENTATIVE = [
    ("Who is Urza's brother?", "Mishra", {"VERIFIED"}, []),
    ("Who is Ugin's brother?", "Nicol Bolas", {"VERIFIED"}, []),
    ("Who killed Elesh Norn?", "Karn", {"VERIFIED", "QUALIFIED"}, []),
    ("Who defeated Ugin?", "Nicol Bolas", {"VERIFIED", "QUALIFIED"}, []),
    ("Who created the Immortal Sun?", "Azor", {"VERIFIED", "QUALIFIED"}, []),
    ("Who killed Razaketh?", "Liliana Vess", {"VERIFIED", "QUALIFIED"}, []),
    ("Who is Kaito's sister?", "Eiko", {"VERIFIED", "QUALIFIED"}, []),
    ("Who mentored Taigam?", "Narset", {"VERIFIED", "QUALIFIED"}, []),
    ("Who leads the Izzet?", "Ral Zarek", {"VERIFIED", "QUALIFIED"}, ["MATCHED_BY_FACTION_ALIAS"]),
    ("Who leads the Orzhov?", "Teysa Karlov", {"VERIFIED", "QUALIFIED"}, ["MULTIPLE_LEADERS_ACROSS_ERAS"]),
    ("Who leads the Temur?", "Surrak Dragonclaw", {"VERIFIED", "QUALIFIED"}, ["ERA_OR_TIMELINE_CONTEXT"]),
    ("Who rules the Jeskai?", "Ojutai", {"QUALIFIED"}, ["CANON_IMPLIED_PRESENT"]),
    # Batch 10 Phase 7 continuity explainer: conflicting/open accounts are listed, never resolved
    ("Explain the continuity of Brago", "Queen Marchesa", {"QUALIFIED"}, ["CANON_DISPUTED_PRESENT"]),
    ("Is Lorthos canon?", "Murasa Skyclave", {"QUALIFIED"}, ["OPEN_QUESTION_PRESENT"]),
]
NOT_FOUND = ["Who is Zorblax the Unreal's brother?"]


def _names(env: dict) -> list[str]:
    res = env.get("result")
    if not isinstance(res, dict):
        return []
    return ([r.get("name") for rs in res.get("relations_by_status", {}).values() for r in rs]
            + [a.get("other") for a in res.get("continuity_accounts", [])])


def run() -> dict:
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    totals = inv["totals"]
    untagged = next((a for a in inv["arcs"] if a.get("arc") in ("", None, "untagged", "(untagged)")), None)
    checks = []
    for q, want, confs, flags in REPRESENTATIVE:
        env = mv_ask.ask(q)
        names = _names(env)
        ok = want in names and env["confidence"] in confs and all(f in env.get("flags", []) for f in flags)
        checks.append({"question": q, "expected": want, "confidence": env["confidence"], "route": env.get("route"),
                       "found": want in names, "flags": env.get("flags", []), "ok": ok})
    for q in NOT_FOUND:
        env = mv_ask.ask(q)
        checks.append({"question": q, "expected": None, "confidence": env["confidence"], "route": env.get("route"),
                       "found": False, "flags": env.get("flags", []), "ok": env["confidence"] == "NOT_FOUND"})
    return {"schema": "batch-recount/v1",
            "meaning": "Recount of committed artifacts plus representative mv_ask regressions; not approval or certification.",
            "coverage": totals,
            "untagged": {k: untagged.get(k) for k in untagged if not isinstance(untagged[k], (list, dict))} if untagged else None,
            "graph": {"nodes": len(graph.get("nodes", [])), "edges": len(graph.get("edges", [])),
                      "stats": graph.get("stats")},
            "queries": checks, "queries_ok": sum(c["ok"] for c in checks), "queries_total": len(checks)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    rep = run()
    text = json.dumps(rep, indent=2, sort_keys=True) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    if a.json:
        print(text, end="")
    else:
        c = rep["coverage"]
        print(f"pages cited {c.get('cited_pages')}/{c.get('pages')}, reviewed {c.get('reviewed_no_claim_pages')}, "
              f"claims {c.get('claims')}, arcs all cited {c.get('arcs_all_cited')}/{c.get('arcs')}")
        for q in rep["queries"]:
            print(("ok   " if q["ok"] else "FAIL ") + q["question"] + f"  [{q['confidence']}]")
        print(f"representative queries {rep['queries_ok']}/{rep['queries_total']}")
    return 0 if rep["queries_ok"] == rep["queries_total"] else 1


if __name__ == "__main__":
    sys.exit(main())
