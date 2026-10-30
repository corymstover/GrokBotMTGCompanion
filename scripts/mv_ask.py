#!/usr/bin/env python3
"""Phase 7 MTG Multiverse Companion: one question entry point with explicit confidence.

It routes a question to committed, cited repository data and wraps every answer in an
envelope saying what it is based on and how far to trust it:

  {"route", "query", "confidence", "flags", "data_as_of", "sources", "result"}

Routes:
  card NAME   card record (Oracle text, type, identity, Commander legality, rulings count) from
              data/card_index.csv and its cards/ shard section
  lore TERM   cited claim-graph relationships (data/multiverse_graph/multiverse_graph.json),
              grouped by canon status; disputed, open and alternate claims are never flattened
  ask TEXT    free text: tries an exact card name, then a graph entity, then simple patterns
              ("who is X's brother", "who killed/destroyed X", "what happened to X"), and
              Commander deck-construction questions ("can X be my commander", "can X and Y be
              commanders together", "can X go in a Y deck") via scripts/commander_rules.py,
              which cites the Comprehensive Rules (2026-09-25)

Confidence levels:
  VERIFIED   every fact comes from a cited, CANON_CONFIRMED claim or a verified Scryfall record
  QUALIFIED  includes disputed, open-question or alternate-continuity claims, or stale data
  NOT_FOUND  no committed evidence. The companion says so instead of guessing.

Flags name the caveats, e.g. STALE_ORACLE_VS_CURRENT_SNAPSHOT, CANON_DISPUTED_PRESENT,
NO_CITED_LORE, AMBIGUOUS_NAME. This tool never fabricates an answer: no evidence returns NOT_FOUND.
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from query_multiverse_graph import MG  # noqa: E402

CARD_INDEX = ROOT / "data" / "card_index.csv"
CURRENT_SNAPSHOT_DATE = "2026-10-29"  # active verified Scryfall release (snap-20261029)
QUALIFYING = {"CANON_DISPUTED", "OPEN_QUESTION", "ALTERNATE_CONTINUITY", "CANON_IMPLIED", "HYPOTHETICAL"}
STRUCTURAL = {"cited_by", "asserts", "see_also_curated_entry", "proposed_in"}

_index = None


def card_index():
    global _index
    if _index is None:
        with CARD_INDEX.open(encoding="utf-8") as fh:
            _index = {r["name"].lower(): r for r in csv.DictReader(fh)}
    return _index


def _section(shard: Path, name: str) -> str:
    text = shard.read_text(encoding="utf-8")
    m = re.search(r"^### " + re.escape(name) + r"\s*$(.*?)(?=^### |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


DRIFT_REPORT = ROOT / "data" / "card_db" / f"oracle_drift_{CURRENT_SNAPSHOT_DATE}.json"
_drift = None


def _reconciled(name: str) -> bool:
    """True only when the committed drift report for the current snapshot found no change for this card."""
    global _drift
    if _drift is None:
        try:
            d = json.loads(DRIFT_REPORT.read_text(encoding="utf-8"))
            ok = d.get("snapshot_date") == CURRENT_SNAPSHOT_DATE and "changed" in d
            names = {re.split(r"(?:: | -> )", x)[0] for v in d.get("changed", {}).values() for x in v}
            _drift = (ok, names)
        except (OSError, ValueError):
            _drift = (False, set())
    ok, changed = _drift
    return ok and name not in changed


def card(name: str) -> dict:
    row = card_index().get(name.strip().lower())
    env = {"route": "card", "query": name, "flags": [], "sources": []}
    if not row:
        sugg = sorted(n for n in card_index() if name.lower() in n)[:5]
        env.update(confidence="NOT_FOUND", data_as_of=None,
                   result={"suggestions": sugg}, flags=["NO_SUCH_CARD_IN_INDEX"] + (["AMBIGUOUS_NAME"] if sugg else []))
        return env
    sec = _section(ROOT / row["shard"], row["name"])
    quoted = [l.strip()[2:] for l in re.findall(r"^\s+> .*$", sec.split("- **Keywords", 1)[0], re.M)]
    oracle = "\n".join(l for l in quoted if not l.startswith("*"))
    flavor = "\n".join(l.strip("*") for l in quoted if l.startswith("*"))
    field = lambda label: (re.search(r"\*\*" + re.escape(label) + r":\*\*\s*([^·\n]+)", sec) or [None, ""])[1].strip()
    src = re.search(r"source: Scryfall oracle_cards bulk (\d{4}-\d{2}-\d{2})", sec)
    as_of = src.group(1) if src else None
    scry = re.search(r"\[Scryfall\]\((https://scryfall\.com/card/[^)]+)\)", sec)
    rulings = re.search(r"\*\*Rulings\*\* \((\d+)\)", sec)
    env["sources"] = [u for u in [scry and scry.group(1)] if u]
    if as_of and as_of < CURRENT_SNAPSHOT_DATE:
        if _reconciled(row["name"]):
            env["flags_info"] = [f"ORACLE_RECONCILED_WITH_SNAPSHOT_{CURRENT_SNAPSHOT_DATE}"]
            env["reconciliation"] = DRIFT_REPORT.relative_to(ROOT).as_posix()
        else:
            env["flags"].append("STALE_ORACLE_VS_CURRENT_SNAPSHOT")
    if not oracle:
        env["flags"].append("ORACLE_TEXT_NOT_PARSED")
    env.update(confidence="QUALIFIED" if env["flags"] else "VERIFIED", data_as_of=as_of, result={
        "name": row["name"], "oracle_id": row["oracle_id"], "type_line": row["type_line"],
        "mana_cost": field("Mana cost"), "color_identity": row["color_identity"],
        "commander_legality": row["commander_legality"], "game_changer": row["game_changer"] == "1",
        "oracle_text": oracle, "flavor_text": flavor or None, "rulings": int(rulings.group(1)) if rulings else 0,
        "shard": f"{row['shard']}#{row['anchor']}"})
    return env


_mg = None


def graph():
    global _mg
    if _mg is None:
        _mg = MG()
    return _mg


def _find(term: str):
    try:
        return graph().find(term)
    except KeyError:
        return None


def lore(term: str, relation: str | None = None, direction: str | None = None) -> dict:
    mg = graph()
    env = {"route": "lore", "query": term, "flags": [], "data_as_of": mg.g.get("evidence_cutoff") or "2026-10-30"}
    nid = _find(term)
    if not nid:
        env.update(confidence="NOT_FOUND", sources=[], result={}, flags=["NO_CITED_LORE"])
        return env
    rows = [r for r in mg.neighbors(nid) if r.get("claim") and r["relation"] not in STRUCTURAL]
    if relation:
        rows = [r for r in rows if r["relation"] in (relation, "inverse_of:" + relation)]
    if direction:
        rows = [r for r in rows if r["direction"] == direction]
    grouped, urls = {}, []
    for r in rows:
        c = mg.nodes.get("claim:" + r["claim"], {})
        r = dict(r, summary=c.get("name"), limitation=c.get("limitation") or None, stage=c.get("stage"))
        grouped.setdefault(r["status"], []).append(r)
        urls += [u for u in r.get("source_urls", []) if u not in urls]
    if not rows:
        env["flags"].append("NO_CITED_LORE")
    bad = sorted(set(grouped) & QUALIFYING)
    env["flags"] += [s + "_PRESENT" for s in bad]
    env.update(confidence="NOT_FOUND" if not rows else ("QUALIFIED" if bad else "VERIFIED"),
               sources=urls, result={"entity": nid, "name": mg.nodes[nid]["name"],
                                     "type": mg.nodes[nid]["type"], "relations_by_status": grouped})
    return env


PATTERNS = [  # (regex, relation, direction from the named entity's point of view)
    (re.compile(r"who (?:is|are|was|were) (.+?)'s (?:brother|sister|sibling|twin)s?\??$", re.I), "sibling_of", None),
    (re.compile(r"who (?:is|was) (.+?)'s (?:wife|husband|spouse)\??$", re.I), "spouse_of", None),
    (re.compile(r"who (?:defeated|slew|beat) (?:the )?(.+?)\??$", re.I), "defeated_by", "out"),
    (re.compile(r"who (?:created|made|built) (?:the )?(.+?)\??$", re.I), "created", "in"),
    (re.compile(r"who (?:destroyed|killed) (?:the )?(.+?)\??$", re.I), "destroyed", "in"),
    (re.compile(r"where did (?:the )?(.+?) come from\??$", re.I), "origin", "out"),
    (re.compile(r"who (?:is|was) (.+?)'s mother\??$", re.I), "mother_of", "in"),
    (re.compile(r"who struck down (?:the )?(.+?)\??$", re.I), "struck_down", "in"),
]

FALLBACK = {"created": [("created_by", "out"),  # "who created X" may be stored as X created_by Y
                        ("designed", "in"), ("invented", "in")],  # Batch 5: Kiran designed Heart of Kiran
            "defeated_by": [("defeated", "in")],  # Batch 5: XLN010 stores Bolas defeated Ugin
            "sibling_of": [("twin_sibling_of", None)],  # Pack A stores Ugin/Bolas as twin_sibling_of
            "destroyed": [("killed", "in")],  # Pack C4 stores Karn killed Elesh Norn (Batch 4)
            "mother_of": [("child_of", "out")]}  # "X child_of Y" also answers "who is X's mother"


def _is_card(name: str) -> bool:
    return name.lower() in card_index()


RULES_PATTERNS = [  # Commander deck-construction questions, answered by scripts/commander_rules.py
    (re.compile(r"^can (.+?) and (.+?) (?:be (?:my )?(?:co-?)?commanders(?: together)?|partner(?: together)?)\??$", re.I), "pair"),
    (re.compile(r"^can (.+?) be (?:my |a )?commander\??$", re.I), "single"),
    (re.compile(r"^can (?:i (?:play|run|include) )?(.+?) (?:go )?in (?:a |an |my )?(.+?) deck\??$", re.I), "include"),
]


def _rules(kind: str, m) -> dict:
    import commander_rules  # local import: commander_rules imports this module
    if kind == "pair":
        return commander_rules.commander([m.group(1), m.group(2)])
    if kind == "single":
        return commander_rules.commander([m.group(1)])
    return commander_rules.include(m.group(1), [x.strip() for x in re.split(r" and | \+ ", m.group(2))])


def ask(text: str) -> dict:
    q = text.strip()
    for rx, kind in RULES_PATTERNS:
        m = rx.search(q)
        if m:
            env = _rules(kind, m)
            env.update(route="ask->rules:" + kind, query=q)
            return env
    for rx, rel, direction in PATTERNS:
        m = rx.search(q)
        if m:
            env = lore(m.group(1).strip(), rel, direction)
            for alt, alt_dir in FALLBACK.get(rel, []):
                if env["confidence"] != "NOT_FOUND":
                    break
                rel, direction = alt, alt_dir
                env = lore(m.group(1).strip(), rel, direction)
            env.update(route="ask->lore:" + rel, query=q)
            return env
    term = re.sub(r"^(?:who|what|where)\s+(?:is|was|are|were)\s+|^tell me about\s+", "", q, flags=re.I).rstrip("?").strip()
    term = re.sub(r"^the\s+", "", term, flags=re.I) if not _is_card(term) else term
    nid = _find(term)
    entity = nid and graph().nodes[nid]["type"] not in {"Card", "Literal"}
    if entity:
        env = lore(term)
        if _is_card(term):  # e.g. "Nicol Bolas" is both a character and a card name
            env["flags"].append("AMBIGUOUS_NAME")
            env["also_card"] = card_index()[term.lower()]["name"]
        env["query"] = q
        return env
    if _is_card(term):
        env = card(term)
        env["query"] = q
        return env
    env = lore(term)
    env["query"] = q
    return env


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("card").add_argument("name")
    lp = sub.add_parser("lore"); lp.add_argument("term"); lp.add_argument("--relation")
    sub.add_parser("ask").add_argument("text")
    a = p.parse_args(argv)
    out = card(a.name) if a.cmd == "card" else lore(a.term, a.relation) if a.cmd == "lore" else ask(a.text)
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 0 if out["confidence"] != "NOT_FOUND" else 3


if __name__ == "__main__":
    sys.exit(main())
