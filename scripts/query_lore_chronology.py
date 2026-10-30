#!/usr/bin/env python3
"""Explain what the sourced *partial* MTG chronology can and cannot order.

Examples:
  python3 scripts/query_lore_chronology.py --list
  python3 scripts/query_lore_chronology.py --compare A:elder_dragon_war A:primeval_rule
  python3 scripts/query_lore_chronology.py --check

NEVER treats publication order or unrelated story-page presents as an in-world date.
Every chronological proof has a path to the committed official-source evidence.
"""
import argparse
from collections import defaultdict, deque
import hashlib
import json
from pathlib import Path
import source_event_sequences as SEQ

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/lore_research/relative_chronology_2026-10-30.json"


def graph(data):
    nodes = {n["id"]: n for n in data["nodes"]}
    labels = {e["earlier"]: e["later"] for e in data["stated_edges"]
              if e["relation"] == "SAME_TIME_AS_LABEL"}
    canonical = lambda n: labels.get(n, n)
    arcs = defaultdict(list)
    for e in data["stated_edges"] + data["derived_edges"]:
        if e["relation"] != "BEFORE":
            continue
        a, b = canonical(e["earlier"]), canonical(e["later"])
        if a == b:
            raise ValueError("self-ordering: " + a)
        arcs[a].append((b, e))
    return nodes, labels, arcs


def proof_path(start, end, arcs):
    queue = deque([(start, [])])
    seen = {start}
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for nxt, edge in arcs[current]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [edge]))
    return None


def compare(data, left, right):
    nodes, labels, arcs = graph(data)
    if left not in nodes or right not in nodes:
        raise ValueError("unknown chronology ID; use --list to see available events")
    if left == right:
        return {"result": "SAME_EVENT", "left": left, "right": right, "proof": []}
    a, b = labels.get(left, left), labels.get(right, right)
    if a == b:
        relation, path = "SAME_PRINTED_AR", []
    else:
        path = proof_path(a, b, arcs)
        if path is not None:
            relation = "BEFORE"
        else:
            path = proof_path(b, a, arcs)
            relation = "AFTER" if path is not None else "UNKNOWN"
    supporting = []
    # Printed AR labels do not assert an event-to-label chronological edge; they
    # represent a dated scene. Keep their two *primary* quotes in every AR proof.
    involved = {a, b}
    for e in path or []:
        involved.update((e["earlier"], e["later"]))
    for e in data["stated_edges"]:
        if e["relation"] == "SAME_TIME_AS_LABEL" and e["later"] in involved:
            supporting.append(e)
    return {"left": left, "right": right, "result": relation, "proof": path or [],
            "printed_ar_sources": supporting,
            "limitation": ("No cited chronology path connects these events. This means UNKNOWN, "
                           "not that the events were simultaneous or unrelated.")
            if relation == "UNKNOWN" else
            "Chronological order is scoped to the quoted narrative/continuity; "
            "it does not establish a universal absolute timeline."}


def check(data):
    nodes, labels, arcs = graph(data)
    if data["cycles"] or data["counts"]["cycles"]:
        raise ValueError("chronology contains cycles")
    for e in data["stated_edges"]:
        if e["earlier"] not in nodes or e["later"] not in nodes:
            raise ValueError("broken chronology node reference")
        if not e["source_url"].startswith("https://magic.wizards.com/"):
            raise ValueError("non-Wizards cited source")
        from build_relative_chronology import norm
        digest = hashlib.sha256(norm(e["quote"]).encode()).hexdigest()
        if e["quote_sha256"] != digest:
            raise ValueError("chronology quote digest drift")
    for e in data["derived_edges"]:
        if e["kind"] != "DERIVED_FROM_PRINTED_AR":
            raise ValueError("unproven derived chronology edge")
        if nodes[e["earlier"]]["kind"] != "PRINTED_AR_LABEL" or nodes[e["later"]]["kind"] != "PRINTED_AR_LABEL":
            raise ValueError("derived date edge is not between printed labels")
        if nodes[e["earlier"]]["ar"] >= nodes[e["later"]]["ar"]:
            raise ValueError("printed AR dates not in ascending order")
    for left, later in data["precedes"].items():
        if left not in nodes:
            raise ValueError("unknown closure key")
        canon = labels.get(left, left)
        reachable = set()
        queue = [canon]
        while queue:
            for nxt, _ in arcs[queue.pop()]:
                if nxt not in reachable:
                    reachable.add(nxt)
                    queue.append(nxt)
        expected = sorted(n for n in nodes if labels.get(n, n) in reachable)
        if expected != later:
            raise ValueError("chronology transitive closure drift: " + left)
    # A tempting but unsupported inference: publication date != story era.
    result = compare(data, "C:josu_undead", "A:eldrazi_imprisoned")
    if result["result"] != "UNKNOWN":
        raise ValueError("independent story presents were implicitly joined")
    return {"result": "PASS", "events": data["counts"]["event_nodes"],
            "ordered_pairs": data["counts"]["comparable_pairs"],
            "total_pairs": data["counts"]["total_pairs"],
            "unresolved_pairs": data["counts"]["total_pairs"] - data["counts"]["comparable_pairs"]}


def compare_across_datasets(legacy, local, left, right):
    """Query both independent chronology ledgers without inventing links between them."""
    old_ids = {n['id'] for n in legacy['nodes']}
    new_ids = {n['id'] for n in local['nodes']}
    lookup = {n['id']:n['label'] for n in legacy['nodes'] + local['nodes']}
    def resolve(phrase):
        if phrase in lookup:
            return phrase
        hits = [eid for eid, name in lookup.items() if phrase.casefold() in name.casefold()]
        if len(hits) != 1:
            raise ValueError(f'ambiguous or unknown chronology label {phrase!r}; use --list or a full event ID')
        return hits[0]
    left, right = resolve(left), resolve(right)
    if left in old_ids and right in old_ids:
        return compare(legacy, left, right)
    if left in new_ids and right in new_ids:
        return SEQ.proof(local, left, right)
    if (left in old_ids | new_ids) and (right in old_ids | new_ids):
        return {'result': 'UNKNOWN', 'left': left, 'right': right, 'proof': [],
                'confidence': 'UNRESOLVED',
                'limitation': 'The original Packs A–C chronology and new source-local strands have no cited cross-ledger bridge. No relative order can be inferred.'}
    raise ValueError('unknown chronology event ID; use --list')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    choice = ap.add_mutually_exclusive_group(required=True)
    choice.add_argument("--list", action="store_true")
    choice.add_argument("--compare", nargs=2, metavar=("EARLIER_ID", "LATER_ID"))
    choice.add_argument("--check", action="store_true")
    args = ap.parse_args()
    data = json.loads(DATA.read_text(encoding="utf-8"))
    source_data = json.loads(SEQ.OUT.read_text(encoding='utf-8'))
    if args.list:
        result = ([{"id": n["id"], "label": n["label"]} for n in data["nodes"] if n["kind"] == "EVENT"]
                  + [{"id": n["id"], "label": n["label"], "certainty": n["certainty"]}
                     for n in source_data["nodes"]])
    elif args.compare:
        result = compare_across_datasets(data, source_data, *args.compare)
    else:
        result = check(data)
        if source_data != SEQ.build():
            raise ValueError('source-event sequences stale; regenerate from quoted specification')
        result['source_local_sequences'] = source_data['counts']
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
