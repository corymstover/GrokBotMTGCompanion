#!/usr/bin/env python3
"""Bounded, offline v1 acceptance gate for the lore retrieval/deck stack.

    python3 scripts/check_lore_ready.py
    python3 scripts/check_lore_ready.py --bulk-file .cache/lore-printings/default-cards.jsonl.gz

The optional bulk source triggers a real Commander-hard-rules check of the
unapproved Karn demonstration. The default mode never makes legality claims.
No network, writes, or changes to the frozen Grixis snapshot.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import export_printing_lore as P
import lore_evidence as E
import lore_query as Q
import story_deck_planner as S


def check(root, bulk=None):
    archive = root / "data/printing_lore"
    a = P.lookup(archive, "lea", None, limit=0)
    assert (a["matches"], a["distinct_names"], a["oracle_cards"]) == (295, 290, 290), a

    strip = Q.card_printings("Strip Mine", archive, limit=0)
    wilds = Q.card_printings("Evolving Wilds", archive, limit=0)
    assert strip["printings"] > 0 and strip["distinct_flavor_texts"] >= 2
    assert wilds["printings"] > 0 and wilds["distinct_flavor_texts"] >= 2

    saga = Q.card_printings("The Antiquities War", archive, limit=20)
    assert any(face.get("chapters") and "I, II" in face["chapters"]
               for card in saga["items"] for face in card.get("faces", []))

    silly = E.printing_matches("Karn Dogs", archive, limit=5)
    assert silly["total_matches"] >= 1 and any(p["card"] == "Concession Stand" for p in silly["printings"])

    timeline = (root / "Master Timeline.md").read_text(encoding="utf-8")
    ar = Q.timeline_view(timeline, "ar")
    assert [r["verified_date"] for r in ar["rows"]] == [28, 44, 63, 64, 69, 79, 85, 4562]
    assert all(r["official_sources_on_row"] for r in ar["rows"])
    assert Q.timeline_view(timeline, "invasion")["count"] == 5
    omenpaths = Q.timeline_view(timeline, "omenpaths")
    assert not omenpaths["chronological"] and omenpaths["count"] >= 10

    graph = json.loads((root / "data/lore_graph.json").read_text(encoding="utf-8"))
    assert graph["stats"]["lore_entries"] == 280
    assert all(e["evidence"]["tier"] == "contextual_pointer" for e in graph["edges"])
    data = json.loads((root / "data/lore_entries.json").read_text(encoding="utf-8"))
    ugin_bolas = S.plan("Ugin vs Nicol Bolas", data, timeline)
    assert ugin_bolas["beat_total"] >= 4
    invasion = S.plan("Phyrexian Invasion", data, timeline)
    assert invasion["beat_total"] >= 5
    mom = S.plan("March of the Machine", data, timeline)
    assert mom["beat_total"] >= 1, "a summary title must resolve to at least one arc"

    example_path = root / "data/lore_decks/examples/karn_life_story_draft.json"
    example = json.loads(example_path.read_text(encoding="utf-8"))
    assembly = S.assemble(example)
    assert assembly["total"] == 100 and assembly["basic_slots"] == 19
    assert assembly["validation"]["status"] == "not_run", "structure alone is not legality proof"
    assert "Mycosynth Lattice" not in assembly["decklist"]
    assert len(assembly["reasons"]) == 80
    assert all(c.get("source", "").startswith("https://scryfall.com/card/")
               for beat in example["beats"] for c in beat["cards"])

    result = {"status": "retrieval_and_draft_structure_passed", "alpha_printings": a["matches"],
              "alpha_names": a["distinct_names"], "strip_mine_flavor_variants": strip["distinct_flavor_texts"],
              "evolving_wilds_flavor_variants": wilds["distinct_flavor_texts"],
              "saga_printings": saga["printings"], "silly_flavor_matches": silly["total_matches"],
              "dated_AR_events": ar["count"], "ugin_bolas_beats": ugin_bolas["beat_total"],
              "invasion_beats": invasion["beat_total"], "karn_draft_cards": assembly["total"],
              "commander_hard_rules": "not_run_without_bulk"}
    if bulk:
        if not bulk.is_file():
            raise FileNotFoundError(bulk)
        sys.path.insert(0, str(root / "scripts"))
        import evaluate_decklist as ev
        original = ev.ing.get_bulk
        try:
            ev.ing.get_bulk = lambda cache, unused, kind="oracle-cards": original(cache, str(bulk), kind)
            resolver = ev.Resolver()
        finally:
            ev.ing.get_bulk = original
        assessed = ev.check(assembly["decklist"], resolver)
        hard = [i for i in assessed["issues"] if i["type"] in ev.HARD]
        assert assessed["total"] == 100 and not hard, hard
        assert assessed["ci"] == "", assessed["ci"]
        result["commander_hard_rules"] = "passed"
        result["bulk_sha256"] = hashlib.sha256(bulk.read_bytes()).hexdigest()
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--bulk-file", type=Path, default=None)
    args = parser.parse_args(argv)
    try:
        result = check(args.repo.resolve(), args.bulk_file.resolve() if args.bulk_file else None)
    except (OSError, ValueError, AssertionError) as e:
        print(f"lore readiness FAIL: {e}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
