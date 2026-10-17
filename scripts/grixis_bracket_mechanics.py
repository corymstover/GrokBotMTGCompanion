#!/usr/bin/env python3
"""Step F frozen-snapshot deck-level execution for bounded Step-E mechanics.

Only Bracket-5 suites currently request Step-E mechanic execution. This runner evaluates the
canonical champion list (not a challenger swap) with the existing deterministic v1.1 zone trace
and the already-frozen Step-E parsers/metrics. It reports availability/friction evidence only:
no multiplayer win rate, no composite stress score, and no automated deck/swap verdict.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_sim as gs
import grixis_mech as gm
from grixis_mech import observe, stack, stax
import grixis_mechanics as mech
import grixis_bracket_stress_runner as routing

REG = ROOT / "data/grixis/registry.json"
SUITES = ROOT / "data/grixis/bracket_stress"
OUT = ROOT / "data/grixis/bracket_stress_mechanics"
LOCK = ROOT / "data/grixis/dev_snapshot_lock.json"
SCHEMA = ROOT / "data/grixis/schemas/bracket_stress_mechanics.schema.json"

VERSION = 1
SAMPLES = 300
SEED = 66
MODEL = "1.1"
TURNS = [4, 6, 8, 10]


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256(path):
    return "sha256:" + hashlib.sha256(Path(path).read_bytes()).hexdigest()


def b5_entries():
    reg = load(REG)
    rows = []
    for did, entry in sorted(reg["decks"].items(), key=lambda kv: kv[1]["slug"]):
        suite = load(SUITES / f"{entry['slug']}.json")
        if suite["bracket"]["suite_family"] == "B5_competitive":
            rows.append((did, entry, suite))
    return rows


def required_module_ids(suite):
    ids = []
    for item in suite["items"]:
        if item["kind"] != "mechanic_module":
            continue
        for mid in routing.MODULE_ALIASES.get(item["executor"], [item["executor"]]):
            if mid not in ids:
                ids.append(mid)
    return ids


def models_for(deck):
    return {x["name"]: x for x in deck.library + list(deck.commanders)}


def supported_cards(module, models, cards):
    out = []
    for name in sorted(models):
        if name not in cards:
            continue
        row = cards[name]
        if module.matches(name, row["text"], row["type_line"]):
            out.append(name)
    return out


def counter_result(games, models, cards, commanders):
    ctx = {"cards": cards, "models": models, "commanders": commanders}
    names = supported_cards(stack.Counterspells, models, cards)
    rows = []
    for name in names:
        rule, why = stack.counter_parse(name, cards[name]["text"], cards[name]["type_line"])
        rows.append({
            "card": name,
            "semantics": {"rule": rule, "not_modelable": why},
            "counter_ready_turns_by_turn": {
                str(t): round(stack.counter_ready(games, name, ctx, t), 4) for t in TURNS
            },
        })
    return {
        "module_id": "counterspell_density",
        "module_version": stack.Counterspells.SPEC["version"],
        "status": "executed_deck_level_test_result",
        "evidence_class": "test_result",
        "supported_card_count": len(rows),
        "supported_cards": rows,
        "metric_semantics": (
            "Per supported card: average number of end-of-own-turn checkpoints through the stated turn "
            "at which the counter is available under the Step-E readiness model. Cards are not summed "
            "into a universal protection score."
        ),
        "spec": stack.Counterspells.SPEC,
    }


def protection_result(games, models, cards, commanders):
    ctx = {"cards": cards, "models": models, "commanders": commanders}
    names = supported_cards(stack.StackProtection, models, cards)
    rows = []
    for name in names:
        rule, why = stack.protection_parse(name, cards[name]["text"], cards[name]["type_line"])
        rows.append({
            "card": name,
            "semantics": {"rule": rule, "not_modelable": why},
            "protection_ready_or_active_turns_by_turn": {
                str(t): round(stack.protection_ready(games, name, ctx, t), 4) for t in TURNS
            },
        })
    return {
        "module_id": "stack_protection",
        "module_version": stack.StackProtection.SPEC["version"],
        "status": "executed_deck_level_test_result",
        "evidence_class": "test_result",
        "supported_card_count": len(rows),
        "supported_cards": rows,
        "metric_semantics": (
            "Per supported card: average number of end-of-own-turn checkpoints through the stated turn "
            "with reactive protection ready or static/activated protection active under Step-E semantics. "
            "Cards are not collapsed into a universal protection score."
        ),
        "spec": stack.StackProtection.SPEC,
    }


def stax_result(games, models, cards, commanders):
    del commanders
    names = supported_cards(stax.StaxTax, models, cards)
    rows = []
    for name in names:
        rules, why = stax.parse(name, cards[name]["text"], cards[name]["type_line"])
        by_turn = {}
        for t in TURNS:
            points = [stax.metrics(games, name, rules, t, spells, noncreature, draws)
                      for spells, noncreature, draws in stax.points()]
            by_turn[str(t)] = {
                "active_rounds": round(points[0]["active_rounds"], 4),
                "opponent_extra_mana_range": [
                    round(min(x["opponent_extra_mana"] for x in points), 4),
                    round(max(x["opponent_extra_mana"] for x in points), 4),
                ],
                "opponent_spells_blocked_range": [
                    round(min(x["opponent_spells_blocked"] for x in points), 4),
                    round(max(x["opponent_spells_blocked"] for x in points), 4),
                ],
                "opponent_draws_blocked_range": [
                    round(min(x["opponent_draws_blocked"] for x in points), 4),
                    round(max(x["opponent_draws_blocked"] for x in points), 4),
                ],
                "static_lock_rounds_range": [
                    round(min(x["static_lock_rounds"] for x in points), 4),
                    round(max(x["static_lock_rounds"] for x in points), 4),
                ],
                "self_burden": bool(points[0]["self_burden"]),
                "kinds": points[0]["kinds"],
            }
        rows.append({
            "card": name,
            "semantics": {"rules": rules, "not_modelable": why},
            "category_metrics_by_turn": by_turn,
        })
    return {
        "module_id": "stax_tax",
        "module_version": stax.StaxTax.SPEC["version"],
        "status": "executed_deck_level_test_result",
        "evidence_class": "test_result",
        "supported_card_count": len(rows),
        "supported_cards": rows,
        "metric_semantics": (
            "Per supported permanent and per category only. Opponent extra-mana demand, blocked spells, "
            "blocked draws and static-lock activity remain separate; symmetric self-burden is explicit. "
            "No composite stax score is produced."
        ),
        "spec": stax.StaxTax.SPEC,
    }


EXECUTORS = {
    "counterspell_density": counter_result,
    "stack_protection": protection_result,
    "stax_tax": stax_result,
}


def provenance():
    lock = load(LOCK)
    return {
        "development_snapshot": lock["snapshot"],
        "locked_files": lock["files"],
        "locked_sha256": lock["sha256"],
        "simulator": {
            "name": gs.NAME,
            "version": gs.VERSION,
            "model": MODEL,
            "sha256": gs.model_sha256(),
        },
        "trace": {
            "samples": SAMPLES,
            "seed": SEED,
            "turns": TURNS,
            "observer_sha256": sha256(ROOT / "scripts/grixis_mech/observe.py"),
        },
        "module_code_sha256": {
            "stack": sha256(ROOT / "scripts/grixis_mech/stack.py"),
            "stax": sha256(ROOT / "scripts/grixis_mech/stax.py"),
        },
        "runner_sha256": sha256(Path(__file__)),
    }


def build_one(did, entry, suite, cards):
    required = required_module_ids(suite)
    unknown = [x for x in required if x not in EXECUTORS]
    if unknown:
        raise RuntimeError(f"{entry['slug']}: unsupported Step-F mechanic module(s): {unknown}")
    deck = gs.load_deck(entry["slug"])
    games = observe.trace_games(deck, SAMPLES, SEED, model=MODEL)
    models = models_for(deck)
    commanders = {x["name"] for x in deck.commanders}
    results = [EXECUTORS[mid](games, models, cards, commanders) for mid in required]
    return {
        "schema_version": 1,
        "deck_id": did,
        "slug": entry["slug"],
        "canonical_hash": entry["canonical_project_list"]["hash"],
        "suite_family": suite["bracket"]["suite_family"],
        "status": "executed",
        "evidence_class": "test_result",
        "authority": {
            "can_decide": False,
            "note": (
                "Deck-level Step-E outputs are bounded evidence for Step-F review. They cannot approve/reject "
                "a deck, decide a swap, or substitute for Commander-first judgment."
            ),
        },
        "aggregate_score": None,
        "required_module_ids": required,
        "module_results": results,
        "provenance": provenance(),
        "limitations": [
            "The underlying trace is the deterministic one-player v1.1 goldfish model, not a multiplayer simulator.",
            "Counter/protection outputs measure readiness or availability, not whether an opponent presents a valuable legal target.",
            "Stax/tax outputs preserve category-specific ranges and self-burden; unlike effects are never summed into one score.",
            "Unsupported card semantics remain outside the bounded modules and require later judgment rather than invented numeric evidence.",
        ],
    }


def build():
    cards = mech.cards_index()
    OUT.mkdir(parents=True, exist_ok=True)
    expected = set()
    rows = []
    for did, entry, suite in b5_entries():
        expected.add(entry["slug"])
        doc = build_one(did, entry, suite, cards)
        dump(OUT / f"{entry['slug']}.json", doc)
        rows.append({
            "deck_id": did,
            "slug": entry["slug"],
            "canonical_hash": doc["canonical_hash"],
            "required_module_ids": doc["required_module_ids"],
            "supported_card_counts": {
                r["module_id"]: r["supported_card_count"] for r in doc["module_results"]
            },
        })
        print(entry["slug"], {r["module_id"]: r["supported_card_count"] for r in doc["module_results"]})
    for p in OUT.glob("*.json"):
        if p.name != "summary.json" and p.stem not in expected:
            p.unlink()
    dump(OUT / "summary.json", {
        "schema_version": 1,
        "generated_by": f"scripts/grixis_bracket_mechanics.py v{VERSION}",
        "development_snapshot": load(LOCK)["snapshot"],
        "decks": rows,
        "totals": {"b5_decks": len(rows), "module_executions": sum(len(x["required_module_ids"]) for x in rows)},
    })
    print(f"bracket-mechanics: built {len(rows)} B5 deck records")


def problems():
    import jsonschema
    probs = []
    rows = b5_entries()
    expected = {entry["slug"]: (did, entry, suite) for did, entry, suite in rows}
    present = {p.stem for p in OUT.glob("*.json") if p.name != "summary.json"} if OUT.exists() else set()
    if present != set(expected):
        probs.append(f"coverage mismatch missing={sorted(set(expected)-present)} extra={sorted(present-set(expected))}")
    schema = load(SCHEMA)
    lock = load(LOCK)
    for slug, (did, entry, suite) in expected.items():
        p = OUT / f"{slug}.json"
        if not p.exists():
            continue
        d = load(p)
        probs += [f"{slug}: schema {list(e.path)}: {e.message}"
                  for e in jsonschema.Draft202012Validator(schema).iter_errors(d)]
        if d["deck_id"] != did:
            probs.append(f"{slug}: deck id drift")
        if d["canonical_hash"] != entry["canonical_project_list"]["hash"]:
            probs.append(f"{slug}: canonical hash drift")
        if d["provenance"]["development_snapshot"] != lock["snapshot"]:
            probs.append(f"{slug}: development snapshot drift")
        if d["provenance"]["locked_sha256"] != lock["sha256"]:
            probs.append(f"{slug}: locked snapshot hashes drift")
        required = required_module_ids(suite)
        if d["required_module_ids"] != required:
            probs.append(f"{slug}: required module routing drift")
        got = [r["module_id"] for r in d["module_results"]]
        if got != required:
            probs.append(f"{slug}: module result coverage/order drift")
        for r in d["module_results"]:
            if r["status"] != "executed_deck_level_test_result":
                probs.append(f"{slug}:{r['module_id']}: not executed")
            if r["module_id"] not in gm.MODULES:
                probs.append(f"{slug}:{r['module_id']}: no Step-E registry module")
            elif str(r["module_version"]) != str(gm.MODULES[r["module_id"]].SPEC["version"]):
                probs.append(f"{slug}:{r['module_id']}: module version drift")
        txt = json.dumps(d).lower()
        for forbidden in gm.FORBIDDEN_METRICS:
            if f'"{forbidden}"' in txt:
                probs.append(f"{slug}: forbidden metric {forbidden}")
        if d["authority"]["can_decide"] is not False or d["aggregate_score"] is not None:
            probs.append(f"{slug}: evidence became decision-capable or aggregate-scored")
    summary = OUT / "summary.json"
    if not summary.exists():
        probs.append("summary missing")
    else:
        s = load(summary)
        if s.get("development_snapshot") != lock["snapshot"]:
            probs.append("summary snapshot drift")
        if s.get("totals", {}).get("b5_decks") != len(expected):
            probs.append("summary B5 count drift")
    return probs


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--build", action="store_true")
    a.add_argument("--check", action="store_true")
    x = a.parse_args(argv)
    rc = 0
    if x.build:
        build()
    if x.check:
        p = problems()
        print(f"bracket-mechanics: {len(b5_entries())} B5 decks, {len(p)} problems")
        for e in p[:100]:
            print("FAIL", e)
        rc |= 1 if p else 0
    if not (x.build or x.check):
        a.print_help()
    return rc


if __name__ == "__main__":
    sys.exit(main())
