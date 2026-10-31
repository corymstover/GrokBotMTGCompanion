#!/usr/bin/env python3
"""Commander deck-construction rules checks with Comprehensive Rules citations.

Phase 7/8. Answers deck-construction questions from committed Scryfall-derived card
records (data/card_index.csv and the cards/ shards). Every answer cites the official
Wizards Comprehensive Rules (effective 2026-09-25) through the verbatim excerpt in
data/rules/cr_20260925_commander_excerpt.json.

  commander NAME [NAME2]       can this card, or this pair, be your commander?
                               CR 903.3, 903.3a, 702.124a-m
  include CARD --commander C [--commander C2]
                               can CARD go in a deck led by C (and C2)?
                               CR 903.4, 903.5c, 903.5d, 702.124c
  audit-eligibility            recompute single-card eligibility for every indexed card and
                               compare it with the "Can be commander" note already in the
                               shards. Disagreements are listed, never hidden.

Scope and limits:
- These are deck-construction checks only, not gameplay rules-interaction checks.
- Format legality is the dated Scryfall `commander` legality field, not a live
  check of today's banned list. Even a mechanically valid result is QUALIFIED
  until current Oracle text and legality are independently checked.
- Inclusion checks reject an invalid proposed commander configuration; passing
  color identity alone does not make a deck legal.
- Card text that changes the commander rules in a way not modelled here (for example
  un-set text) yields QUALIFIED with the flag UNMODELLED_COMMANDER_TEXT.
- Confidence uses the mv_ask levels: VERIFIED, QUALIFIED and NOT_FOUND (exit code 3).
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask  # noqa: E402

CR = json.loads((ROOT / "data/rules/cr_20260925_commander_excerpt.json").read_text(encoding="utf-8"))
COLORS = "WUBRG"
BASIC_TYPES = {"Plains": "W", "Island": "U", "Swamp": "B", "Mountain": "R", "Forest": "G"}
DASH = "\u2014"
CARD_SHARDS_AS_OF = "2026-10-15"
HISTORICAL_LEGALITY_FLAG = "DATED_SCRYFALL_LEGALITY_NOT_LIVE"


def cite(*ids):
    return [{"rule": i, "text": CR["rules"][i]} for i in ids]


def resolve(name: str):
    """Exact indexed name, or the unique double-faced card whose front face matches."""
    idx = mv_ask.card_index()
    key = name.strip().lower()
    if key in idx:
        return idx[key]
    faces = [r for n, r in idx.items() if " // " in n and n.split(" // ")[0] == key]
    return faces[0] if len(faces) == 1 else None


def _strip_reminder(line: str) -> str:
    return re.sub(r"\s*\([^)]*\)", "", line).strip()


def facts(row: dict, sec: str | None = None) -> dict:
    if sec is None:
        sec = mv_ask._section(ROOT / row["shard"], row["name"])
    quoted = [l.strip()[2:] for l in re.findall(r"^\s+> .*$", sec.split("- **Keywords", 1)[0], re.M)]
    oracle = [l for l in quoted if not l.startswith("*")]
    pt = re.search(r"\*\*P/T:\*\*\s*([^\s·]+)", sec)
    ab = {"partner": False, "partner_text": set(), "partner_with": set(), "background": False,
          "doctors_companion": False}
    for line in oracle:
        bare = _strip_reminder(line)
        if bare.lower().startswith("partner with "):  # names can contain commas
            ab["partner_with"].add(bare[len("partner with "):].strip().lower())
            continue
        for tok in (t.strip() for t in bare.split(",")):
            low = tok.lower()
            if low == "partner":
                ab["partner"] = True
            elif low.startswith("partner" + DASH):
                ab["partner_text"].add(tok.split(DASH, 1)[1].strip().lower())
            elif low == "choose a background":
                ab["background"] = True
            elif low == "doctor's companion":
                ab["doctors_companion"] = True
    text = "\n".join(oracle)
    front = row["type_line"].split(" // ")[0]
    return {"name": row["name"], "type_line": row["type_line"], "front_type": front,
            "subtypes": front.split(DASH, 1)[1].split() if DASH in front else [],
            "identity": "".join(c for c in COLORS if c in row["color_identity"]),
            "legality": row["commander_legality"], "pt": pt.group(1) if pt else None, "abilities": ab,
            "can_be_commander_text": bool(re.search(r"can be your commander", text, re.I)),
            "unmodelled": bool(re.search(r"as your commanders|as though they each had partner|spell commander",
                                         text, re.I)),
            "shard": f"{row['shard']}#{row['anchor']}"}


def single_eligibility(f: dict):
    """(eligible, basis, rule ids) by CR 903.3 / 903.3a / 702.124k, ignoring format legality."""
    tl = f["front_type"]
    legendary = "Legendary" in tl.split(DASH)[0]
    if f["can_be_commander_text"]:
        return True, 'Oracle text: "can be your commander"', ["903.3a"]
    if legendary and "Creature" in tl.split(DASH)[0]:
        return True, "legendary creature", ["903.3"]
    if legendary and "Vehicle" in f["subtypes"]:
        return True, "legendary Vehicle", ["903.3"]
    if legendary and "Spacecraft" in f["subtypes"]:
        if f["pt"]:
            return True, "legendary Spacecraft with a power/toughness box", ["903.3"]
        return False, "legendary Spacecraft without a power/toughness box", ["903.3"]
    if legendary and "Background" in f["subtypes"]:
        return "PAIRED_ONLY", "legendary Background: only alongside a commander with choose a Background", ["702.124k"]
    return False, ("not a legendary creature, Vehicle or Spacecraft with power/toughness, "
                   "and no 'can be your commander' text"), ["903.3"]


def _env(route, query, result, flags, rules):
    # Repository snapshots are reproducible evidence, not a real-time check of
    # the current Commander ban list, card release status or Oracle changes.
    flags = sorted(set(flags) | {HISTORICAL_LEGALITY_FLAG})
    return {"route": route, "query": query, "confidence": "QUALIFIED", "flags": flags,
            "rules_source": {"document": CR["title"], "effective": CR["effective"], "url": CR["source_url"],
                             "sha256": CR["source_sha256"]},
            "card_source": "Scryfall-derived records: data/card_index.csv and cards/ shards",
            "card_data_as_of": CARD_SHARDS_AS_OF,
            "limitation": ("The result uses dated card/legality data and a dated Comprehensive Rules excerpt. "
                           "Confirm current Oracle text, release status, Commander bans and rules before finalizing a deck."),
            "rules": cite(*dict.fromkeys(rules)), "result": result}


def _notfound(route, query, missing):
    return {"route": route, "query": query, "confidence": "NOT_FOUND", "flags": ["NO_SUCH_CARD_IN_INDEX"],
            "result": {"missing": missing}}


def pair_rule(a: dict, b: dict):
    """(allowed, ability, rule ids) for designating a and b together (CR 702.124)."""
    A, B = a["abilities"], b["abilities"]
    an, bn = a["name"].split(" // ")[0].lower(), b["name"].split(" // ")[0].lower()
    if an in B["partner_with"] and bn in A["partner_with"]:
        return True, "partner with [name]", ["702.124j"]
    if A["partner"] and B["partner"]:
        return True, "partner", ["702.124h"]
    shared = A["partner_text"] & B["partner_text"]
    if shared:
        return True, "partner" + DASH + sorted(shared)[0], ["702.124i"]
    for x, y in ((a, b), (b, a)):
        if x["abilities"]["background"] and "Background" in y["subtypes"] and "Legendary" in y["front_type"]:
            return True, "choose a Background", ["702.124k"]
    for x, y in ((a, b), (b, a)):
        if (x["abilities"]["doctors_companion"] and "Legendary" in y["front_type"]
                and "Creature" in y["front_type"] and y["subtypes"] == ["Time", "Lord", "Doctor"]):
            return True, "Doctor's companion", ["702.124m"]
    return False, None, ["702.124a", "702.124f"]


def commander(names: list) -> dict:
    if len(names) > 2:
        return {"route": "commander", "query": names, "confidence": "NOT_FOUND", "flags": ["MORE_THAN_TWO"],
                "rules": cite("702.124g"), "result": {"reason": "No partner ability allows more than two commanders."}}
    rows = [resolve(n) for n in names]
    missing = [n for n, r in zip(names, rows) if r is None]
    if missing:
        return _notfound("commander", names, missing)
    fs = [facts(r) for r in rows]
    flags, rules, per = [], [], []
    for f in fs:
        ok, basis, rids = single_eligibility(f)
        rules += rids
        per.append({"name": f["name"], "eligible_by_cr": ok, "basis": basis,
                    "scryfall_commander_legality": f["legality"], "color_identity": f["identity"] or "C",
                    "shard": f["shard"]})
        if f["unmodelled"]:
            flags.append("UNMODELLED_COMMANDER_TEXT")
    legal = all(p["scryfall_commander_legality"] == "legal" for p in per)
    if len(fs) == 1:
        p = per[0]
        result = {"allowed": p["eligible_by_cr"] is True and legal, "commanders": per}
        if p["eligible_by_cr"] is not True:
            result["reason"] = p["basis"]
        elif not legal:
            result["reason"] = f"Scryfall commander legality is '{p['scryfall_commander_legality']}'"
    else:
        pok, ability, rids = pair_rule(*fs)
        rules += rids + ["702.124c"]
        each = all(p["eligible_by_cr"] is True or (p["eligible_by_cr"] == "PAIRED_ONLY"
                                                   and ability == "choose a Background") for p in per)
        result = {"allowed": pok and each and legal, "pairing_ability": ability, "commanders": per,
                  "combined_color_identity": "".join(c for c in COLORS if any(c in f["identity"] for f in fs)) or "C"}
        if not pok:
            result["reason"] = "no shared partner ability (different partner abilities cannot be combined)"
        elif not each:
            result["reason"] = "; ".join(p["basis"] for p in per if p["eligible_by_cr"] is not True)
        elif not legal:
            result["reason"] = "a commander is not legal in Commander per Scryfall"
    return _env("commander", names, result, sorted(set(flags)), rules)


def include(card_name: str, commanders: list) -> dict:
    if not 1 <= len(commanders) <= 2:
        return {"route": "include", "query": [card_name] + commanders,
                "confidence": "NOT_FOUND", "flags": ["INVALID_COMMANDER_COUNT"],
                "result": {"reason": "A Commander deck must designate one or two valid commanders."}}
    names = [card_name] + commanders
    rows = [resolve(n) for n in names]
    missing = [n for n, r in zip(names, rows) if r is None]
    if missing:
        return _notfound("include", names, missing)
    c, cmd = facts(rows[0]), [facts(r) for r in rows[1:]]
    proposed = commander(commanders)
    ident = {x for f in cmd for x in f["identity"]}
    rules = ["903.4", "903.5c"] + (["702.124c"] if len(cmd) == 2 else [])
    reasons = []
    flags = []
    if not proposed["result"]["allowed"]:
        reasons.append("proposed commander configuration is not legal: "
                       + proposed["result"].get("reason", "commander eligibility or pairing requirement failed"))
        flags.append("INVALID_COMMANDER_CONFIGURATION")
    outside = "".join(x for x in COLORS if x in c["identity"] and x not in ident)
    if outside:
        reasons.append(f"color identity {c['identity']} has {outside}, outside the commander identity")
    if "Land" in c["type_line"].split(DASH)[0]:
        basics = [t for t in c["subtypes"] if t in BASIC_TYPES]
        if basics:
            rules.append("903.5d")
            bad = [t for t in basics if BASIC_TYPES[t] not in ident]
            if bad:
                reasons.append(f"basic land type(s) {', '.join(bad)} produce mana outside the commander identity")
    if c["legality"] != "legal":
        reasons.append(f"Scryfall commander legality is '{c['legality']}'")
    result = {"allowed": not reasons, "card": c["name"], "card_identity": c["identity"] or "C",
              "commander_identity": "".join(x for x in COLORS if x in ident) or "C",
              "commander_configuration": {"allowed": proposed["result"]["allowed"],
                                          "commanders": [f["name"] for f in cmd],
                                          "pairing_ability": proposed["result"].get("pairing_ability")},
              "scryfall_commander_legality": c["legality"], "reasons": reasons, "shard": c["shard"]}
    return _env("include", names, result, flags, rules)


def iter_sections():
    by_shard = {}
    for r in mv_ask.card_index().values():
        by_shard.setdefault(r["shard"], []).append(r)
    for shard, rows in sorted(by_shard.items()):
        text = (ROOT / shard).read_text(encoding="utf-8")
        parts = {m.group(1).strip(): m.group(2)
                 for m in re.finditer(r"^### (.+?)\s*$(.*?)(?=^### |\Z)", text, re.M | re.S)}
        for r in rows:
            yield r, parts.get(r["name"], "")


def audit_eligibility() -> dict:
    agree, disagree, no_note = 0, [], 0
    for r, sec in iter_sections():
        m = re.search(r"Can be commander:\s*(Yes|No|Only alongside)", sec)
        if not m:
            no_note += 1
            continue
        note = {"Yes": True, "No": False, "Only alongside": "PAIRED_ONLY"}[m.group(1)]
        ok, basis, _ = single_eligibility(facts(r, sec))
        if ok == note:
            agree += 1
        else:
            disagree.append({"name": r["name"], "type_line": r["type_line"], "shard_note": m.group(1),
                             "computed": ok, "basis": basis})
    return {"schema": "commander-eligibility-audit/v1", "rules_effective": CR["effective"],
            "cards_compared": agree + len(disagree), "agree": agree, "disagree": len(disagree),
            "cards_without_note": no_note, "disagreements": disagree}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("commander").add_argument("names", nargs="+")
    p = sp.add_parser("include")
    p.add_argument("card")
    p.add_argument("--commander", action="append", required=True)
    sp.add_parser("audit-eligibility").add_argument("--check", action="store_true",
                                                    help="exit 1 if any card disagrees")
    a = ap.parse_args(argv)
    if a.cmd == "commander":
        out = commander(a.names)
    elif a.cmd == "include":
        out = include(a.card, a.commander)
    else:
        out = audit_eligibility()
        print(json.dumps(out, indent=1, ensure_ascii=False))
        return 1 if a.check and out["disagree"] else 0
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 3 if out.get("confidence") == "NOT_FOUND" else 0


if __name__ == "__main__":
    sys.exit(main())
