#!/usr/bin/env python3
"""Step B: enrich combo-quality evidence from the cached Commander Spellbook step text.

Commander Spellbook is community-maintained. Its cached steps are useful line descriptions, not official rules text.
This script preserves the raw fields and derives only transparent counts/mentions: step/action count, declared mana symbols,
zone-word mentions, a stack-action proxy and coarse endpoint hints. It never turns those into a win probability or final
combo classification.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CQ = ROOT / "data" / "grixis" / "combo_quality"
STEPS = ROOT / "data" / "grixis_spellbook_steps.json"
REGISTRY = ROOT / "data" / "grixis" / "registry.json"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "combo_line_semantics.schema.json"
OUT = ROOT / "data" / "grixis" / "combo_line_semantics"
VERSION = 1
MANA_RX = re.compile(r"\{([^{}]+)\}")
ZONES = {
    "hand": re.compile(r"\bhand\b", re.I),
    "graveyard": re.compile(r"\bgraveyard\b", re.I),
    "battlefield": re.compile(r"\bbattlefield\b", re.I),
    "exile": re.compile(r"\bexil(?:e|ed)\b", re.I),
    "command_zone": re.compile(r"\bcommand zone\b", re.I),
    "library": re.compile(r"\blibrary\b", re.I),
}


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def dump(p, obj):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def action_counts(steps):
    lines = [x.strip() for x in steps.splitlines() if x.strip()]
    text = "\n".join(lines)
    return len(lines), {
        "cast": len(re.findall(r"\bcast\b", text, re.I)),
        "activate": len(re.findall(r"\bactivate\b", text, re.I)),
        "sacrifice": len(re.findall(r"\bsacrific", text, re.I)),
        "trigger": len(re.findall(r"\btrigger", text, re.I)),
        "resolve": len(re.findall(r"\bresolve\b", text, re.I)),
        "repeat": len(re.findall(r"\brepeat\b", text, re.I)),
    }


def declared_mana(mana_needed):
    symbols = MANA_RX.findall(mana_needed or "")
    colors = sorted({c for token in symbols for c in "WUBRG" if c in token.upper()})
    return symbols, colors


def zone_mentions(blob):
    return {k: len(rx.findall(blob)) for k, rx in ZONES.items()}


def endpoint_hints(produces):
    blob = " ".join(produces or []).lower()
    out = []
    tests = [
        ("damage", r"damage"),
        ("life_loss", r"loss of life|life loss|loses? life"),
        ("mill", r"mill|library"),
        ("mana", r"mana"),
        ("draw", r"draw|card advantage"),
        ("tokens", r"tokens?"),
        ("etb_ltb_death", r"\betb\b|\bltb\b|death triggers?|dies"),
        ("storm", r"storm count|magecraft"),
        ("untap", r"untap"),
    ]
    for name, rx in tests:
        if re.search(rx, blob):
            out.append(name)
    if not out and re.search(r"infinite", blob):
        out.append("other_infinite")
    return out


def line_record(combo, cache):
    cid = combo["id"]
    r = cache.get(cid)
    if not r:
        raw = {"mana_needed": "", "easy_prerequisites": "", "notable_prerequisites": "", "notes": "", "produces": [], "steps": ""}
        step_count, acts = 0, {k: 0 for k in ("cast", "activate", "sacrifice", "trigger", "resolve", "repeat")}
        return {
            "combo_id": cid, "cards": combo["cards"], "record_found": False, "source_status": None,
            "raw": raw,
            "derived": {"step_count": step_count, "action_counts": acts, "mana_symbols_declared": [],
                        "colored_symbols_declared": [], "zone_mentions": {k: 0 for k in ZONES},
                        "interaction_window_proxy": {"stack_action_count_proxy": 0,
                                                     "note": "No cached step record; no interaction-window proxy produced."},
                        "endpoint_hints": []},
            "evidence_class": "derived_metric", "confidence": "low", "evidence": [f"spellbook:{cid}"],
            "limitations": ["No cached Commander Spellbook step record was found for this line."],
        }
    raw = {
        "mana_needed": r.get("mana_needed") or "",
        "easy_prerequisites": r.get("easy_prerequisites") or "",
        "notable_prerequisites": r.get("notable_prerequisites") or "",
        "notes": r.get("notes") or "",
        "produces": r.get("produces") or [],
        "steps": r.get("steps") or "",
    }
    step_count, acts = action_counts(raw["steps"])
    symbols, colors = declared_mana(raw["mana_needed"])
    blob = "\n".join([raw["easy_prerequisites"], raw["notable_prerequisites"], raw["notes"], raw["steps"]])
    zone = zone_mentions(blob)
    stack_proxy = acts["cast"] + acts["activate"] + acts["trigger"] + acts["resolve"]
    return {
        "combo_id": cid,
        "cards": combo["cards"],
        "record_found": True,
        "source_status": r.get("status"),
        "raw": raw,
        "derived": {
            "step_count": step_count,
            "action_counts": acts,
            "mana_symbols_declared": symbols,
            "colored_symbols_declared": colors,
            "zone_mentions": zone,
            "interaction_window_proxy": {
                "stack_action_count_proxy": stack_proxy,
                "note": "Transparent word/action count from community step text; not the exact number of legal opponent priority windows."
            },
            "endpoint_hints": endpoint_hints(raw["produces"]),
        },
        "evidence_class": "derived_metric",
        "confidence": "moderate" if r.get("status") == "OK" else "low",
        "evidence": [f"spellbook:{cid}", f"spellbook_steps:data/grixis_spellbook_steps.json#variants/{cid}"],
        "limitations": [
            "Commander Spellbook is community-maintained and is not an official Comprehensive Rules/rulings source.",
            "Zone mentions are word counts in prerequisites/notes/steps, not normalized per-piece zone requirements.",
            "Declared mana is preserved from Spellbook's mana_needed field; blank does not mean zero mana.",
            "The stack-action proxy counts textual cast/activate/trigger/resolve actions and is not a priority-window simulator.",
        ],
    }


def build_one(did, entry, stepdata):
    slug = entry["slug"]
    cq = load(CQ / f"{slug}.json")
    lines = [line_record(c, stepdata["variants"]) for c in cq["combos"]]
    return {
        "schema_version": 1, "deck_id": did, "slug": slug,
        "canonical_hash": entry["canonical_project_list"]["hash"], "status": "provisional_evidence",
        "authority": {"official_rules_source": False, "can_decide": False,
                      "note": "Community step text enriches Step B evidence only. Official rules/M1 review and later judgment remain authoritative."},
        "source": {"path": "data/grixis_spellbook_steps.json", "retrieved": stepdata.get("retrieved") or "unknown",
                   "source_kind": "Commander Spellbook community-maintained steps cache"},
        "lines": lines,
        "summary": {
            "combo_count": len(lines),
            "step_record_found_count": sum(1 for x in lines if x["record_found"]),
            "missing_step_record_count": sum(1 for x in lines if not x["record_found"]),
            "mana_needed_declared_count": sum(1 for x in lines if x["raw"]["mana_needed"]),
            "zone_mention_count": sum(sum(x["derived"]["zone_mentions"].values()) for x in lines),
            "direct_endpoint_hint_count": sum(1 for x in lines if any(y in ("damage", "life_loss", "mill") for y in x["derived"]["endpoint_hints"])),
        },
    }


def build():
    reg, steps = load(REGISTRY), load(STEPS)
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for did, e in sorted(reg["decks"].items(), key=lambda kv: kv[1]["slug"]):
        d = build_one(did, e, steps)
        dump(OUT / f"{e['slug']}.json", d)
        rows.append({"deck_id": did, "slug": e["slug"], **d["summary"]})
    keys = ("combo_count", "step_record_found_count", "missing_step_record_count", "mana_needed_declared_count", "zone_mention_count", "direct_endpoint_hint_count")
    dump(OUT / "summary.json", {"schema_version": 1, "generated_by": f"scripts/grixis_combo_steps_quality.py v{VERSION}",
                                "decks": rows, "totals": {k: sum(x[k] for x in rows) for k in keys}})
    print(f"combo-line-semantics: built {len(rows)} decks, {sum(x['combo_count'] for x in rows)} lines")


def check():
    try:
        import jsonschema
    except ImportError:
        print("combo-line-semantics: jsonschema required")
        return 1
    schema = load(SCHEMA); common = load(SCHEMA.parent / "common.schema.json")
    store = {schema["$id"]: schema, common["$id"]: common}
    resolver = jsonschema.RefResolver(base_uri=schema["$id"], referrer=schema, store=store)
    validator = jsonschema.Draft202012Validator(schema, resolver=resolver)
    reg, stepdata = load(REGISTRY), load(STEPS)
    problems = []
    expected = {e["slug"] for e in reg["decks"].values()}
    present = {p.stem for p in OUT.glob("*.json") if p.name != "summary.json"}
    if expected != present:
        problems.append(f"file coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did, e in reg["decks"].items():
        p = OUT / f"{e['slug']}.json"
        if not p.exists(): continue
        d = load(p)
        for err in validator.iter_errors(d):
            problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        cq = load(CQ / f"{e['slug']}.json")
        if {x["combo_id"] for x in d["lines"]} != {x["id"] for x in cq["combos"]}:
            problems.append(f"{e['slug']}: combo line id coverage drift")
        if d["canonical_hash"] != e["canonical_project_list"]["hash"]:
            problems.append(f"{e['slug']}: canonical hash drift")
        for x in d["lines"]:
            if x["record_found"] and x["combo_id"] not in stepdata["variants"]:
                problems.append(f"{e['slug']} {x['combo_id']}: claims missing step record exists")
    print(f"combo-line-semantics: {len(expected)} deck files, {len(problems)} problems")
    for x in problems[:40]: print("FAIL", x)
    return 1 if problems else 0


def main(argv=None):
    a = argparse.ArgumentParser(); a.add_argument("--build", action="store_true"); a.add_argument("--check", action="store_true"); a.add_argument("--summary", action="store_true")
    x = a.parse_args(argv); rc = 0
    if x.build: build()
    if x.check: rc |= check()
    if x.summary:
        print(json.dumps(load(OUT / "summary.json")["totals"], indent=2, sort_keys=True))
    if not (x.build or x.check or x.summary): a.print_help()
    return rc


if __name__ == "__main__": sys.exit(main())
