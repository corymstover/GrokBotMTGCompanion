#!/usr/bin/env python3
"""Gameplay rules-interaction checks: published rulings and Comprehensive Rules citations.

Phase 7. For two cards, or for every card pair in a decklist, this surfaces the official
evidence for how they interact. It does not simulate a game.

  pair CARD_A CARD_B     rulings of either card that name the other card (DIRECT_RULING). A short
                         name that is the ruling card's own ("Nicol Bolas" in a Nicol Bolas, the
                         Deceiver ruling) and a card name that is also a set name are not linked;
                         rulings of either card that mention a keyword the other card has
                         (KEYWORD_RULING); verbatim CR 701/702 text for every keyword involved
  deck DECKLIST.txt      every DIRECT_RULING link between two cards in the list
  audit                  run `deck` over every committed draft decklist and write
                         data/rules/interaction_audit_2026-10-30.json (--check: fail if stale)

Sources:
- Card records and rulings: the committed Scryfall-derived shards (cards/, Oracle bulk 2026-10-15).
  These rulings are the ones Scryfall publishes; in the 2026-10-29 rulings bulk, 79,637 of
  79,706 rulings carry source "wotc" and 69 carry source "scryfall". The shards do not keep
  that per-ruling label.
- Rules: data/rules/cr_20260925_keyword_excerpt.json, verbatim from the official Wizards
  Comprehensive Rules effective 2026-09-25.

Confidence: VERIFIED when at least one ruling names the other card. Otherwise QUALIFIED with
NO_DIRECT_RULING, because the absence of a ruling says nothing about whether the cards interact.
Unknown card names give NOT_FOUND (exit 3).
"""
import argparse
import itertools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask  # noqa: E402
from commander_rules import resolve  # noqa: E402

CR = json.loads((ROOT / "data/rules/cr_20260925_keyword_excerpt.json").read_text(encoding="utf-8"))
AUDIT = ROOT / "data/rules/interaction_audit_2026-10-30.json"
DECKS = sorted((ROOT / "data/lore_decks/drafts").glob("*_decklist.txt"))
BASICS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}
SECTION_BY_NAME = {v.lower(): k for k, v in CR["sections"].items()}
SET_NAMES = {s["name"] for s in json.loads((ROOT / "data/set_atlas/scryfall_set_metadata_2026-10-29.json")
                                         .read_text(encoding="utf-8"))["scryfall_sets"]}
LIMIT = ("Surfaces published rulings and verbatim Comprehensive Rules text; it does not simulate the game. "
         "No ruling does not mean no interaction.")


def record(name: str):
    row = resolve(name)
    if row is None:
        return None
    sec = mv_ask._section(ROOT / row["shard"], row["name"])
    rulings = [{"date": d, "text": t.strip()} for d, t in re.findall(r"^\s+- \*(\d{4}-\d{2}-\d{2})\* — (.+)$", sec, re.M)]
    kw = re.search(r"^- \*\*Keywords:\*\*\s*(.+)$", sec, re.M)
    keywords = [k.strip() for k in kw.group(1).split(",")] if kw else []
    return {"name": row["name"], "front": row["name"].split(" // ")[0], "type_line": row["type_line"],
            "rulings": rulings, "keywords": keywords, "shard": f"{row['shard']}#{row['anchor']}"}


def _names(rec) -> list[str]:
    return list(dict.fromkeys([rec["name"], rec["front"]]))


def _mentions(text: str, name: str) -> bool:
    return bool(re.search(r"(?<![\w’'])" + re.escape(name) + r"(?![\w])", text))


def keyword_section(kw: str):
    k = kw.lower()
    if k in SECTION_BY_NAME:
        return SECTION_BY_NAME[k]
    if k.endswith("walk") and "landwalk" in SECTION_BY_NAME:
        return SECTION_BY_NAME["landwalk"]
    return None


def cite_keyword(kw: str) -> dict:
    sid = keyword_section(kw)
    if sid is None:
        return {"keyword": kw, "rule": None, "note": "no CR 701/702 section with this name"}
    subs = sorted((r for r in CR["rules"] if r.startswith(sid) and r[len(sid):].isalpha()),
                  key=lambda r: (len(r), r))
    return {"keyword": kw, "rule": sid, "heading": CR["sections"][sid],
            "text": [{"rule": r, "text": CR["rules"][r]} for r in subs]}


def direct_links(a, b) -> list[dict]:
    out = []
    for src, other in ((a, b), (b, a)):
        if src["name"] == other["name"]:
            continue
        own = sorted(_names(src), key=len, reverse=True)
        for r in src["rulings"]:
            text = r["text"]
            for n in own:  # a card's rulings name the card itself; don't read that as the other card
                if not any(n in o and len(o) > len(n) for o in _names(other)):
                    text = text.replace(n, "\u0000")
            hit = next((n for n in _names(other) if _mentions(text, n)), None)
            if hit and (src["front"].startswith(hit + ",") or src["front"].startswith(hit + " ")):
                continue  # rulings call a card by its short name ("Nicol Bolas"); that is the card itself
            if hit in SET_NAMES:
                continue  # also a set name ("The Brothers' War"); a mention is ambiguous, so it is not linked
            if hit:
                out.append({"kind": "DIRECT_RULING", "ruling_of": src["name"], "names": other["name"], **r})
    return out


def pair(a_name: str, b_name: str) -> dict:
    a, b = record(a_name), record(b_name)
    missing = [n for n, r in ((a_name, a), (b_name, b)) if r is None]
    env = {"route": "rules_interaction", "query": [a_name, b_name], "limitation": LIMIT,
           "rules_source": {k: CR[k] for k in ("title", "effective", "source_url", "source_sha256")},
           "card_source": "Scryfall-derived shards (cards/), rulings as published by Scryfall"}
    if missing:
        return {**env, "confidence": "NOT_FOUND", "flags": ["UNKNOWN_CARD"], "result": {"missing": missing}}
    direct = direct_links(a, b)
    kw_hits = []
    for src, other in ((a, b), (b, a)):
        for r in src["rulings"]:
            for kw in other["keywords"]:
                if kw and re.search(r"\b" + re.escape(kw) + r"\b", r["text"], re.I):
                    kw_hits.append({"kind": "KEYWORD_RULING", "ruling_of": src["name"], "keyword_of": other["name"],
                                    "keyword": kw, **r})
    kws = list(dict.fromkeys(a["keywords"] + b["keywords"]))
    flags = [] if direct else ["NO_DIRECT_RULING"]
    return {**env, "confidence": "QUALIFIED" if flags else "VERIFIED", "flags": flags,
            "result": {"cards": [{k: c[k] for k in ("name", "type_line", "keywords", "shard")} | {"rulings": len(c["rulings"])}
                                 for c in (a, b)],
                       "direct_rulings": direct, "keyword_rulings": kw_hits,
                       "keyword_rules": [cite_keyword(k) for k in kws]}}


def parse_decklist(path: Path) -> list[str]:
    names = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*\d+x?\s+(.+?)(?:\s+\([a-z0-9]{2,6}\)\s+\S+)?(?:\s+\*\w+\*)?\s*(\[.*\])?\s*$", line)
        if m and not line.lstrip().startswith(("#", "//")):
            names.append(m.group(1).strip())
    return list(dict.fromkeys(names))


def deck(path: Path) -> dict:
    names = parse_decklist(path)
    recs, missing = {}, []
    for n in names:
        r = record(n)
        (missing.append(n) if r is None else recs.__setitem__(r["name"], r))
    links = []
    cards = [r for r in recs.values() if r["front"] not in BASICS]
    for a, b in itertools.combinations(sorted(cards, key=lambda r: r["name"]), 2):
        links.extend(direct_links(a, b))
    links.sort(key=lambda l: (l["ruling_of"], l["names"], l["date"], l["text"]))
    return {"deck": path.relative_to(ROOT).as_posix(), "cards": len(names), "resolved": len(recs),
            "missing": missing, "cards_with_rulings": sum(1 for r in recs.values() if r["rulings"]),
            "rulings_total": sum(len(r["rulings"]) for r in recs.values()),
            "direct_ruling_links": links}


def audit() -> dict:
    decks = [deck(p) for p in DECKS]
    return {"schema": "rules-interaction-audit/v1",
            "status": "AUTOMATED_EVIDENCE_SURFACING (not a rules certification; decks remain UNAPPROVED proposals)",
            "limitation": LIMIT, "rules_source": {k: CR[k] for k in ("title", "effective", "source_sha256")},
            "card_source": "Scryfall-derived shards (cards/, Oracle bulk 2026-10-15)",
            "decks": decks,
            "totals": {"decks": len(decks), "direct_ruling_links": sum(len(d["direct_ruling_links"]) for d in decks),
                       "unresolved_cards": sum(len(d["missing"]) for d in decks)}}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sp = p.add_subparsers(dest="cmd", required=True)
    pp = sp.add_parser("pair")
    pp.add_argument("a")
    pp.add_argument("b")
    dp = sp.add_parser("deck")
    dp.add_argument("path", type=Path)
    ap = sp.add_parser("audit")
    ap.add_argument("--check", action="store_true")
    a = p.parse_args(argv)
    if a.cmd == "pair":
        out = pair(a.a, a.b)
        print(json.dumps(out, indent=1, ensure_ascii=False))
        return 3 if out["confidence"] == "NOT_FOUND" else 0
    if a.cmd == "deck":
        print(json.dumps(deck(a.path.resolve()), indent=1, ensure_ascii=False))
        return 0
    d = audit()
    text = json.dumps(d, indent=1, ensure_ascii=False) + "\n"
    if a.check:
        if not AUDIT.exists() or AUDIT.read_text(encoding="utf-8") != text:
            print("FAIL: interaction audit is stale; rerun scripts/rules_interactions.py audit")
            return 1
        print(f"PASS interaction audit current: {d['totals']}")
        return 0
    AUDIT.write_text(text, encoding="utf-8")
    print(f"wrote {AUDIT.relative_to(ROOT)}: {d['totals']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
