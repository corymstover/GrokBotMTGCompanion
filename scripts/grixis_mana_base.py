#!/usr/bin/env python3
"""Step C mana-base optimizer, batch 68.1: reproducible static mana/pip/source baseline for all 62 decks.

Uses only committed frozen-development artifacts: canonical exports, data/card_index.csv, and generated card shards.
It does not refresh Scryfall and does not propose swaps. Probabilities are transparent no-mulligan draw/source-access
proxies, not cast probabilities or multiplayer win rates. Conditional/restricted mana sources remain separately labeled.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "grixis" / "registry.json"
CARD_INDEX = ROOT / "data" / "card_index.csv"
OUT = ROOT / "data" / "grixis" / "mana_base"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "mana_base.schema.json"
VERSION = 1
COLORS = "WUBRG"
BASIC_TYPE_COLOR = {"Plains": "W", "Island": "U", "Swamp": "B", "Mountain": "R", "Forest": "G"}
PIP = re.compile(r"\{([^}]+)\}")
FETCH_RX = re.compile(
    r"Search your library for (?:an? )?[^.]*?\b(Plains|Island|Swamp|Mountain|Forest|basic land)\b[^.]*? card",
    re.I,
)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def hyper_atleast(N, K, n, k=1):
    """Exact hypergeometric P(at least k successes in n draws)."""
    if N <= 0:
        return 1.0 if k <= 0 else 0.0
    if k <= 0:
        return 1.0
    K = max(0, min(N, K))
    n = max(0, min(N, n))
    if k > min(K, n):
        return 0.0
    den = comb(N, n)
    return sum(
        comb(K, i) * comb(N - K, n - i) / den
        for i in range(k, min(K, n) + 1)
        if 0 <= n - i <= N - K
    )


def p_land_drops(N, L, turns, hand=7):
    """Exact no-mulligan P(land drop available each turn 1..turns), multiplayer draw on turn 1."""
    if not 0 <= L <= N or N < hand or turns < 0:
        return 0.0
    den = comb(N, hand)
    dist = {
        l: comb(L, l) * comb(N - L, hand - l) / den
        for l in range(max(0, hand - (N - L)), min(L, hand) + 1)
    }
    seen = hand
    for t in range(1, turns + 1):
        nd = {}
        for l, p in dist.items():
            rem, reml = N - seen, L - l
            if rem <= 0:
                nd[l] = nd.get(l, 0.0) + p
                continue
            pl = reml / rem
            nd[l + 1] = nd.get(l + 1, 0.0) + p * pl
            nd[l] = nd.get(l, 0.0) + p * (1 - pl)
        dist, seen = nd, seen + 1
        dist = {l: p for l, p in dist.items() if l >= t}
    return sum(dist.values())


def p_all_colors_seen(N, masks, required, n):
    """Exact inclusion-exclusion P(at least one drawn source for every required color), presence only."""
    req = sorted(set(required))
    if not req:
        return 1.0
    n = max(0, min(N, n))
    den = comb(N, n)
    total = 0.0
    for subset_bits in range(1 << len(req)):
        missing = {req[i] for i in range(len(req)) if subset_bits & (1 << i)}
        if not missing:
            p = 1.0
        else:
            forbidden = sum(1 for m in masks if set(m) & missing)
            good = N - forbidden
            p = comb(good, n) / den if good >= n else 0.0
        total += (-1 if len(missing) % 2 else 1) * p
    return max(0.0, min(1.0, total))


def parse_cost(raw):
    """Parse the front-face cost; hybrid contributes fractionally to demand but stays explicitly flexible."""
    raw = (raw or "").split(" // ", 1)[0].strip()
    fixed = {c: 0.0 for c in COLORS}
    flex, generic, phyrexian = [], 0, []
    for s in PIP.findall(raw):
        if s.isdigit():
            generic += int(s)
            continue
        if s in ("X", "Y", "Z"):
            continue
        parts = s.split("/")
        if len(parts) == 2 and parts[1] == "P" and parts[0] in COLORS:
            phyrexian.append(parts[0])
            continue
        opts = [x for x in parts if x in COLORS]
        if len(opts) > 1:
            flex.append(opts)
            for c in opts:
                fixed[c] += 1 / len(opts)
        elif len(opts) == 1:
            fixed[opts[0]] += 1
        elif s in COLORS:
            fixed[s] += 1
        elif s == "S":
            generic += 1
    return {
        "raw": raw,
        "generic": generic,
        "colored_equivalent": {k: round(v, 3) for k, v in fixed.items() if v},
        "flexible_groups": flex,
        "phyrexian_optional": phyrexian,
    }


class CardDB:
    """Frozen generated-card-page reader. get() returns card facts, not deck-context classifications."""

    def __init__(self):
        self.index = {}
        with CARD_INDEX.open(encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                self.index[r["name"]] = r
        self.shards, self.cache = {}, {}

    def _section(self, name):
        row = self.index.get(name)
        if not row:
            raise KeyError(name)
        path = ROOT / row["shard"]
        txt = self.shards.get(path)
        if txt is None:
            txt = path.read_text(encoding="utf-8")
            self.shards[path] = txt
        marker = f"### {name}\n"
        i = txt.find(marker)
        if i < 0:
            raise KeyError(f"heading not found for {name} in {row['shard']}")
        i += len(marker)
        j = txt.find("\n### ", i)
        return row, txt[i : (len(txt) if j < 0 else j)]

    def get(self, name):
        if name in self.cache:
            return self.cache[name]
        row, sec = self._section(name)
        mm = re.search(r"- \*\*Mana cost:\*\* (.*?) · \*\*MV:\*\* ([0-9.]+)", sec)
        tm = re.search(r"- \*\*Type:\*\* (.*)", sec)
        oracle, in_oracle = [], False
        for line in sec.splitlines():
            if line.startswith("- **Oracle text:**"):
                in_oracle = True
                continue
            if in_oracle:
                if line.startswith("  > "):
                    oracle.append(line[4:])
                    continue
                if line.strip() == "":
                    continue
                break
        d = {
            "name": name,
            "mana_cost": mm.group(1) if mm else "—",
            "mv": float(mm.group(2)) if mm else 0.0,
            "color_identity": row.get("color_identity") or "C",
            "type_line": tm.group(1).strip() if tm else row.get("type_line", ""),
            "oracle": "\n".join(oracle),
            "shard": row["shard"],
        }
        self.cache[name] = d
        return d


def _add_clause_colors(text, deck_ci):
    colors, conditional, amount = set(), False, 1
    for line in text.splitlines():
        if "Add " not in line and "add " not in line:
            continue
        low = line.lower()
        if "any color" in low or "any one color" in low or "any type" in low:
            colors |= set(deck_ci)
        syms = [x for x in PIP.findall(line) if x in COLORS + "C"]
        colors |= set(syms)
        groups = re.findall(r"Add ((?:\{[^}]+\})+)", line)
        for g in groups:
            amount = max(amount, len(PIP.findall(g)))
        if any(x in low for x in ("opponent", "another land", "could produce", "among permanents", "among lands", "spend this mana only")):
            conditional = True
        if re.search(r"\{[^}]+\},\s*\{T\}:\s*Add", line):
            conditional = True
    return colors, amount, conditional


def _fetch_types(text):
    """Potential basic land types a search-to-battlefield land can find from its Oracle search clause."""
    for line in text.splitlines():
        if "Search your library" not in line or not FETCH_RX.search(line):
            continue
        types = [t for t in BASIC_TYPE_COLOR if re.search(rf"\b{re.escape(t)}\b", line)]
        return types, ("basic land" in line.lower())
    return [], False


def classify(d, deck_ci):
    """Resolve deck-context mana properties; deck_ci is required for Command Tower/Arcane Signet text."""
    tl, text = d["type_line"], d["oracle"]
    ci = set(c for c in deck_ci if c in COLORS)
    faces = [x.strip() for x in tl.split(" // ")]
    land = bool(faces and "Land" in faces[0])
    flex_land = not land and any("Land" in x for x in faces[1:])
    cost = parse_cost(d["mana_cost"])
    colors, amount, conditional = _add_clause_colors(text, ci)
    fetch_types, basic_fetch = _fetch_types(text)
    if fetch_types:
        colors |= {BASIC_TYPE_COLOR[t] for t in fetch_types}
    elif basic_fetch:
        colors |= ci
    basic_types = [t for t in BASIC_TYPE_COLOR if t in tl]
    colors |= {BASIC_TYPE_COLOR[t] for t in basic_types}
    low = text.lower()
    tapped_match = bool(re.search(r"enters(?: the battlefield)? tapped", low))
    tapped_uncond = tapped_match and not any(x in low for x in ("unless", "if you don't", "you may pay", "if you control", "as long as"))
    tapped_cond = tapped_match and not tapped_uncond
    nonmana_activated = [x for x in text.splitlines() if ":" in x and "Add " not in x and "add " not in x and "Search your library" not in x]
    beneficial_static = any(k in low for k in ("you have no maximum hand size", "creatures you control", "spells you cast", "whenever you cast", "at the beginning of your"))
    utility_land = land and bool(nonmana_activated or beneficial_static)
    repeatable_nonland = not land and not flex_land and bool(colors) and ("{T}" in text or "tap an untapped" in low)
    ritual = not land and ("Instant" in tl or "Sorcery" in tl) and bool(re.search(r"\bAdd (?:\{[^}]+\}){2,}", text))
    one_shot = not land and bool(re.search(r"Sacrifice [^:]*: Add|Sacrifice ~: Add|Sacrifice this artifact: Add", text, re.I))
    fast = (repeatable_nonland and d["mv"] <= 2) or (ritual and d["mv"] <= 2) or (one_shot and d["mv"] <= 2)
    return {
        **d, "cost": cost, "land": land, "flex_land": flex_land,
        "source_colors": "".join(c for c in COLORS + "C" if c in colors), "source_amount_proxy": amount,
        "conditional_source": conditional, "fetch_types": fetch_types, "basic_fetch": basic_fetch, "basic_types": basic_types,
        "tapped_unconditional": tapped_uncond, "tapped_conditional": tapped_cond, "utility_land": utility_land,
        "repeatable_nonland_source": repeatable_nonland, "ritual": ritual, "one_shot_mana": one_shot, "fast_mana": fast,
    }


def parse_export(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"(\d+)\s+(.+?)(?:\s+\[(Commander|Companion)\])?$", line)
        if m:
            out.append(((m.group(3) or "main").lower(), int(m.group(1)), m.group(2)))
    return out


def demand(cards):
    by_color = {c: 0.0 for c in "UBR"}; early2 = {c: 0.0 for c in "UBR"}; early3 = {c: 0.0 for c in "UBR"}; double = {c: 0 for c in "UBR"}
    colored_spells = 0
    for q, c in cards:
        if c["land"]:
            continue
        p = c["cost"]["colored_equivalent"]
        if p:
            colored_spells += q
        for col, v in p.items():
            if col not in by_color:
                continue
            by_color[col] += q * v
            if c["mv"] <= 2: early2[col] += q * v
            if c["mv"] <= 3: early3[col] += q * v
            if v >= 2: double[col] += q
    total = sum(by_color.values())
    return {"colored_spell_count": colored_spells, "raw_colored_pip_equivalents": {c: round(by_color[c], 3) for c in "UBR"},
            "share": {c: (round(by_color[c] / total, 4) if total else 0.0) for c in "UBR"},
            "mv_le_2": {c: round(early2[c], 3) for c in "UBR"}, "mv_le_3": {c: round(early3[c], 3) for c in "UBR"},
            "double_pip_spell_count": double}


def build_one(did, entry, db):
    export = ROOT / entry["canonical_project_list"]["export"]
    ents = parse_export(export); cmd_names = [n for z, q, n in ents if z == "commander"]; unresolved = []
    raw_cmd = []
    for n in cmd_names:
        try: raw_cmd.append(db.get(n))
        except Exception as e: unresolved.append({"card": n, "reason": str(e)})
    deck_ci = set().union(*(set(c["color_identity"]) & set(COLORS) for c in raw_cmd)) if raw_cmd else set("UBR")
    if deck_ci != set("UBR"):
        unresolved.append({"card": "<commander color identity>", "reason": f"expected UBR project identity, derived {''.join(sorted(deck_ci))}"})
    commanders = [classify(c, deck_ci) for c in raw_cmd]
    library = []
    for z, q, n in ents:
        if z != "main": continue
        try: c = classify(db.get(n), deck_ci)
        except Exception as e: unresolved.append({"card": n, "reason": str(e)}); continue
        library += [(n, c)] * q
    N = sum(q for z, q, n in ents if z == "main")
    lands = [(n, c) for n, c in library if c["land"]]; flex = [(n, c) for n, c in library if c["flex_land"]]
    rep = [(n, c) for n, c in library if c["repeatable_nonland_source"]]; fast = [(n, c) for n, c in library if c["fast_mana"]]
    rituals = [(n, c) for n, c in library if c["ritual"]]; oneshot = [(n, c) for n, c in library if c["one_shot_mana"]]
    fetches = [(n, c) for n, c in lands if c["fetch_types"] or c["basic_fetch"]]; utility = [(n, c) for n, c in lands if c["utility_land"]]
    strict_masks = [c["source_colors"] for n, c in lands]; all_masks = [c["source_colors"] for n, c in lands + rep]
    source_counts = {col: sum(1 for m in strict_masks if col in m) for col in "UBR"}; all_source_counts = {col: sum(1 for m in all_masks if col in m) for col in "UBR"}
    untapped = {col: sum(1 for n, c in lands if col in c["source_colors"] and not c["tapped_unconditional"]) for col in "UBR"}
    unconditional = {col: sum(1 for n, c in lands if col in c["source_colors"] and not c["conditional_source"]) for col in "UBR"}
    conditional = {col: sum(1 for n, c in lands if col in c["source_colors"] and c["conditional_source"]) for col in "UBR"}
    dem = demand([(1, c) for n, c in library])
    turns = {}
    for t in (2, 3, 4, 5):
        seen = min(N, 7 + t)
        turns[str(t)] = {"cards_seen_no_mulligan": seen, "strict_land_drop_probability": round(p_land_drops(N, len(lands), t), 6),
                         "flex_land_drop_probability": round(p_land_drops(N, len(lands) + len(flex), t), 6),
                         "all_three_land_source_presence": round(p_all_colors_seen(N, strict_masks, "UBR", seen), 6),
                         "per_color_at_least_one_land_source": {col: round(hyper_atleast(N, source_counts[col], seen, 1), 6) for col in "UBR"}}
    cmd = []
    for c in commanders:
        fixed = {k: int(v) for k, v in c["cost"]["colored_equivalent"].items() if k in "UBR" and float(v).is_integer()}
        target = max(1, int(math.ceil(c["mv"]))); seen = min(N, 7 + target)
        cmd.append({"name": c["name"], "mana_cost": c["mana_cost"], "mana_value": c["mv"], "colored_requirements": fixed,
                    "base_resource_target": target, "first_recast_resource_target": target + 2, "second_recast_resource_target": target + 4,
                    "per_color_source_presence_by_base_turn": {col: round(hyper_atleast(N, source_counts[col], seen, max(1, k)), 6) for col, k in fixed.items()},
                    "all_required_colors_present_by_base_turn": round(p_all_colors_seen(N, strict_masks, fixed.keys(), seen), 6)})
    basics = {t: sum(1 for n, c in lands if "Basic Land" in c["type_line"] and t in c["basic_types"]) for t in BASIC_TYPE_COLOR}
    typed = {t: sum(1 for n, c in lands if t in c["basic_types"]) for t in BASIC_TYPE_COLOR}
    return {"schema_version": 1, "deck_id": did, "slug": entry["slug"], "canonical_hash": entry["canonical_project_list"]["hash"],
            "status": "provisional_evidence", "evidence_class": "derived_metric", "confidence": "moderate",
            "authority": {"can_decide": False, "note": "Step C static mana evidence only; no land or mana-source swap is decided by this record."},
            "inputs": {"canonical_export": str(entry["canonical_project_list"]["export"]), "card_index": "data/card_index.csv", "card_shards": "cards/** (frozen generated Oracle pages)"},
            "deck_color_identity": "".join(c for c in COLORS if c in deck_ci),
            "counts": {"library_cards": N, "lands": len(lands), "flex_land_mdfcs": len(flex), "repeatable_nonland_sources": len(rep), "fast_mana": len(fast),
                       "rituals": len(rituals), "one_shot_mana": len(oneshot), "fetchlands": len(fetches), "utility_lands": len(utility),
                       "unconditional_tapped_lands": sum(c["tapped_unconditional"] for n, c in lands), "conditional_tapped_lands": sum(c["tapped_conditional"] for n, c in lands),
                       "conditional_mana_lands": sum(c["conditional_source"] for n, c in lands)},
            "colored_sources": {"land_sources": source_counts, "land_plus_repeatable_nonland": all_source_counts,
                                "untapped_or_conditionally_untapped_land_sources": untapped, "unconditional_land_sources": unconditional, "conditional_land_sources": conditional},
            "pip_demand": dem, "turn_access_proxies": turns, "commander_casting": cmd,
            "land_type_coverage": {"basic_counts": basics, "typed_land_counts": typed,
                                   "fetches": [{"card": n, "types": c["fetch_types"], "basic_fetch": c["basic_fetch"], "potential_source_colors": c["source_colors"]} for n, c in fetches]},
            "utility_opportunity_cost": {"colorless_only_utility_lands": [n for n, c in utility if not any(x in c["source_colors"] for x in "UBR")],
                                         "tapped_utility_lands": [n for n, c in utility if c["tapped_unconditional"]], "utility_lands": [n for n, c in utility]},
            "fast_mana_cards": [n for n, c in fast], "ritual_cards": [n for n, c in rituals], "one_shot_mana_cards": [n for n, c in oneshot], "mdfc_cards": [n for n, c in flex],
            "unresolved_cards": unresolved,
            "limitations": ["Source-access probabilities are no-mulligan draw/presence proxies, not cast probabilities.",
                            "Conditional/filter/opponent-dependent sources are labeled but not assigned a real-game reliability percentage.",
                            "Fetch colors are potential colors from Oracle/basic-land-type wording; target availability is summarized by typed-land coverage and refined in later Step C batches.",
                            "Tapped-source timing is counted, not yet simulated jointly with spell sequencing.",
                            "Fast mana and rituals are inventoried; commander-tax recovery and startup sequencing are refined later in Step C."]}


def build():
    reg, db, rows = load(REGISTRY), CardDB(), []; OUT.mkdir(parents=True, exist_ok=True)
    for did, e in sorted(reg["decks"].items(), key=lambda kv: kv[1]["slug"]):
        d = build_one(did, e, db); dump(OUT / f"{e['slug']}.json", d)
        rows.append({"deck_id": did, "slug": e["slug"], "lands": d["counts"]["lands"], "flex_land_mdfcs": d["counts"]["flex_land_mdfcs"], "fast_mana": d["counts"]["fast_mana"], "unresolved": len(d["unresolved_cards"])})
    dump(OUT / "summary.json", {"schema_version": 1, "generated_by": f"scripts/grixis_mana_base.py v{VERSION}", "decks": rows,
         "totals": {"decks": len(rows), "lands": sum(x["lands"] for x in rows), "flex_land_mdfcs": sum(x["flex_land_mdfcs"] for x in rows), "fast_mana": sum(x["fast_mana"] for x in rows), "unresolved": sum(x["unresolved"] for x in rows)}})
    print(f"mana-base: built {len(rows)} decks; unresolved={sum(x['unresolved'] for x in rows)}")


def check():
    try: import jsonschema
    except ImportError: print("mana-base: jsonschema required"); return 1
    schema, reg, problems = load(SCHEMA), load(REGISTRY), []
    expected = {e["slug"] for e in reg["decks"].values()}; present = {p.stem for p in OUT.glob("*.json") if p.name != "summary.json"}
    if expected != present: problems.append(f"file coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did, e in sorted(reg["decks"].items()):
        p = OUT / f"{e['slug']}.json"
        if not p.exists(): continue
        d = load(p)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        if d.get("canonical_hash") != e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
        if d.get("deck_color_identity") != "UBR": problems.append(f"{e['slug']}: expected UBR deck identity, got {d.get('deck_color_identity')}")
        if d.get("unresolved_cards"): problems.append(f"{e['slug']}: unresolved cards: {[x['card'] for x in d['unresolved_cards']]}")
        if d.get("authority", {}).get("can_decide") is not False: problems.append(f"{e['slug']}: mana baseline became decision-capable")
    print(f"mana-base: {len(expected)} deck files, {len(problems)} problems")
    for x in problems[:40]: print("FAIL", x)
    return 1 if problems else 0


def main(argv=None):
    a = argparse.ArgumentParser(); a.add_argument("--build", action="store_true"); a.add_argument("--check", action="store_true"); a.add_argument("--summary", action="store_true")
    x = a.parse_args(argv); rc = 0
    if x.build: build()
    if x.check: rc |= check()
    if x.summary: print(json.dumps(load(OUT / "summary.json"), indent=2, sort_keys=True))
    if not (x.build or x.check or x.summary): a.print_help()
    return rc


if __name__ == "__main__": sys.exit(main())
