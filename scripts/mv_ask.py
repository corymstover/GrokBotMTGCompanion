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

Plane-history questions route to reproducible Phase 5 cited plane dossiers;
all responses are QUALIFIED because the registered graph is never exhaustive.
Two-event before/after questions route to the source-graded, **partial** in-universe
chronology and retain UNKNOWN for missing links and narrated legends as legends.
Source-local timeline overviews expose the attested events and cited order edges
without flattening an incomplete strand into a fabricated linear timeline.
Set/category/card-printing questions route to the qualified October 29 Phase 1B
historical shard index; recorded release dates are never in-universe chronology.
Explicit rulings, keyword-rules and card-interaction questions surface dated
published rulings and official CR 701/702 excerpts without simulating play.
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
CURRENT_SNAPSHOT_DATE = "2026-10-30"  # latest committed, independently replayed Scryfall release
QUALIFYING = {"CANON_DISPUTED", "OPEN_QUESTION", "ALTERNATE_CONTINUITY", "CANON_IMPLIED", "HYPOTHETICAL"}
STRUCTURAL = {"cited_by", "asserts", "see_also_curated_entry", "proposed_in"}
# A confirmed event in an erased timeline is not necessarily true in the surviving timeline.
_TEMPORAL_CAVEAT = re.compile(
    r"\b(?:original|previous|rewritten|alternate) timeline\b|"
    r"\b(?:prevented|undone|reversed|rewrote|resurrected|revived)\b", re.I)
_CURRENT_CUE = re.compile(r"\b(?:current|currently|present|now|today|these days)\b", re.I)
# A bare present-tense leader question already asks who holds office *now*.
# A cited historical title is evidence of having led, not of still leading.
_PRESENT_LEADER_QUESTION = re.compile(
    r"^who(?:'s|’s| is| are| leads| heads| runs| captains| governs| rules| commands)\b", re.I)
_PLANE_HISTORY_PATTERNS = [
    re.compile(r"^(?:what(?:'s| is) (?:the )?|tell me (?:about )?(?:the )?|"
               r"summari[sz]e (?:the )?|give me (?:the )?|show (?:the )?)"
               r"(?:history|historical background|lore) (?:of|on|for) (.+?)\??$", re.I),
    re.compile(r"^what happened (?:on|in) (.+?)\??$", re.I),
]
_CHRONOLOGY_QUESTION_PATTERNS = [
    (re.compile(r"^(?:which|what) (?:event |one )?happened (?:first|earlier)\s*[:,]?\s*(.+?)\s+or\s+(.+?)\??$", re.I), "FIRST"),
    (re.compile(r"^did\s+(.+?)\s+happen\s+(before|after)\s+(.+?)\??$", re.I), "DID"),
    (re.compile(r"^was\s+(.+?)\s+(before|after)\s+(.+?)\??$", re.I), "DID"),
]
_CHRONOLOGY_OVERVIEW_PATTERNS = [
    re.compile(r"^(?:the )?(?:source[- ]local )?"
               r"(?:timeline|chronology|event sequence|sequence of events) "
               r"(?:of|for|on|in) (.+?)\??$", re.I),
    re.compile(r"^(?:show|give me|list|summari[sz]e) (?:me )?(?:the )?"
               r"(?:source[- ]local )?(?:timeline|chronology|event sequence|sequence of events) "
               r"(?:of|for|on|in) (.+?)\??$", re.I),
    re.compile(r"^what(?:'s| is) (?:the )?(?:source[- ]local )?"
               r"(?:timeline|chronology|event sequence|sequence of events) "
               r"(?:of|for|on|in) (.+?)\??$", re.I),
]
_EXPLICIT_STRAND = re.compile(r"^show (?:me )?(?:the )?"
                              r"(?:source[- ]local )?chronology strand ([A-Za-z])\??$", re.I)
_GRAPH_CONNECTION_PATTERNS = [
    re.compile(r"^how (?:is|are|was|were) (.+?) (?:connected|related|linked) to (.+?)\??$", re.I),
    re.compile(r"^what (?:is|was) the (?:connection|relationship|link) between (.+?) and (.+?)\??$", re.I),
]
_CARD_LORE_RULES_PATTERNS = [
    re.compile(r"^(?:show(?: me)?|give me) (?:the )?card,? lore,? and commander (?:rules|eligibility) for (.+?)\??$", re.I),
    re.compile(r"^what (?:are|is) the lore and commander eligibility (?:of|for) (.+?)\??$", re.I),
    re.compile(r"^tell me (?:the |about the )?lore and commander eligibility (?:of|for) (.+?)\??$", re.I),
]

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
SNAPSHOT_MANIFEST = ROOT / "data" / "scryfall_snapshots" / "snap-20261030-live-20261031.manifest.json"
_drift = None


def _validated_drift(d: dict, manifest: dict, indexed_rows: int) -> tuple[bool, set[str]]:
    """Admit per-card freshness only if the report covers our exact frozen input.

    A success-shaped but incomplete report, mismatched snapshot, or missing
    comparison category must *not* turn old printed card shards into VERIFIED.
    Individual changed cards remain qualified while unaffected cards can be
    marked reconciled against the newer published bulk.
    """
    expected = ('oracle_text', 'name', 'type_line', 'color_identity',
                'commander_legality', 'game_changer')
    try:
        if (d['schema'] != 'oracle-drift-report/v1'
                or d['snapshot_date'] != CURRENT_SNAPSHOT_DATE
                or d['snapshot_file'] != manifest['files']['oracle-cards']['filename']
                or d['index_rows'] != indexed_rows
                or d['shard_sections_parsed'] != indexed_rows
                or d['counts']['missing_from_snapshot'] != 0
                or d['counts']['shard_text_unparsed'] != 0):
            return False, set()
        changed = d['changed']
        if any(not isinstance(changed[k], list) or d['counts'][k] != len(changed[k])
               for k in expected):
            return False, set()
        names = {re.split(r'(?:: | -> )', entry)[0]
                 for k in expected for entry in changed[k]
                 if isinstance(entry, str)}
        # Non-string change entries cannot safely be attributed to a card.
        if sum(len(changed[k]) for k in expected) != sum(
                isinstance(entry, str) for k in expected for entry in changed[k]):
            return False, set()
        return True, names
    except (KeyError, TypeError, ValueError):
        return False, set()


def _reconciled(name: str) -> bool:
    """True only when the committed drift report for the current snapshot found no change for this card."""
    global _drift
    if _drift is None:
        try:
            d = json.loads(DRIFT_REPORT.read_text(encoding="utf-8"))
            manifest = json.loads(SNAPSHOT_MANIFEST.read_text(encoding="utf-8"))
            _drift = _validated_drift(d, manifest, len(card_index()))
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


# Batch 9: short names for factions and guilds. Generated from the graph's Faction nodes by dropping a
# leading "The" and a trailing organisation word, kept only when the short name is unique among factions,
# so "Izzet" -> Izzet League and "Golgari" -> Golgari Swarm. Never points at a node that is not in the graph.
_ORG_WORDS = {"league", "senate", "legion", "swarm", "syndicate", "clans", "clan", "college", "conclave", "combine"}
_LEAD_ORG_WORDS = {"house"}  # Batch 10: "House Dimir" -> "Dimir"  # guild/college/clan
# words only: "Sun Empire" must not become "Sun"
_EXTRA_ALIASES = {"coppercoats": "faction:coppercoats", "drannith defense force": "faction:coppercoats",
                  "the consulate": "faction:consulate", "mirran resistance": "faction:mirran_resistance"}
_aliases = None


def faction_aliases() -> dict:
    global _aliases
    if _aliases is None:
        cand = {}
        for nid, n in graph().nodes.items():
            if n.get("type") != "Faction":
                continue
            name = re.sub(r"\s*\(.*?\)\s*", " ", n.get("name") or "").strip().lower()
            name = re.sub(r"^the\s+", "", name)
            words = name.split()
            forms = {name}
            if len(words) > 1 and words[-1] in _ORG_WORDS:
                forms.add(" ".join(words[:-1]))
            if len(words) > 1 and words[0] in _LEAD_ORG_WORDS:
                forms.add(" ".join(words[1:]))
            for f in forms:
                cand.setdefault(f, set()).add(nid)
        _aliases = {k: next(iter(v)) for k, v in cand.items() if len(v) == 1 and k}
        _aliases.update({k: v for k, v in _EXTRA_ALIASES.items() if v in graph().nodes})
    return _aliases


def _alias(term: str):
    t = re.sub(r"^the\s+", "", term.strip().lower())
    t = re.sub(r"\s+guild$", "", t)  # "the Izzet guild"
    return faction_aliases().get(t)


def _find(term: str):
    mg = graph()
    exact = any((n.get("name") or "").lower() == term.strip().lower() for n in mg.nodes.values())
    if not exact and _alias(term):
        return _alias(term)
    try:
        return mg.find(term)
    except KeyError:
        return _alias(term) or _first_name(term)


def _first_name(term: str):
    """Batch 6 Phase 7: 'Chandra' -> Chandra Nalaar, only when exactly one character has that first name."""
    t = term.strip().lower()
    if not t or " " in t:
        return None
    hits = [nid for nid, n in graph().nodes.items()
            if n.get("type") == "Character" and (n.get("name") or "").lower().split(" ")[0] == t]
    return hits[0] if len(hits) == 1 else None


def lore(term: str, relation: str | None = None, direction: str | None = None) -> dict:
    mg = graph()
    env = {"route": "lore", "query": term, "flags": [], "data_as_of": mg.g.get("evidence_cutoff") or "2026-10-30"}
    nid = _find(term)
    if not nid:
        env.update(confidence="NOT_FOUND", sources=[], result={}, flags=["NO_CITED_LORE"])
        return env
    if mg.nodes[nid]["name"].lower() != term.strip().lower() and nid == _first_name(term):
        env["flags"].append("MATCHED_BY_FIRST_NAME")
    elif mg.nodes[nid]["name"].lower() != term.strip().lower() and nid == _alias(term):
        env["flags"].append("MATCHED_BY_FACTION_ALIAS")
    rows = [r for r in mg.neighbors(nid) if r.get("claim") and r["relation"] not in STRUCTURAL]
    if relation:
        rels = relation.split("|")  # Batch 8 Phase 7: "a|b" accepts any of several stored relations
        rows = [r for r in rows if r["relation"] in rels or r["relation"] in ["inverse_of:" + x for x in rels]]
    if direction:
        rows = [r for r in rows if r["direction"] == direction]
    grouped, urls = {}, []
    for r in rows:
        c = mg.nodes.get("claim:" + r["claim"], {})
        r = dict(r, summary=c.get("name"), limitation=c.get("limitation") or None, stage=c.get("stage"))
        if edge_dates().get(r["claim"]):  # Batch 10: verbatim in-universe time phrase from the cited quote
            r["in_universe_date"] = edge_dates()[r["claim"]]
        grouped.setdefault(r["status"], []).append(r)
        urls += [u for u in r.get("source_urls", []) if u not in urls]
    if not rows:
        env["flags"].append("NO_CITED_LORE")
    bad = sorted(set(grouped) & QUALIFYING)
    env["flags"] += [s + "_PRESENT" for s in bad]
    if any(_TEMPORAL_CAVEAT.search((r.get("summary") or "") + " " + (r.get("limitation") or ""))
           for rs in grouped.values() for r in rs):
        env["flags"].append("TIMELINE_CONTEXT_REQUIRED")
    env.update(confidence="NOT_FOUND" if not rows else ("QUALIFIED" if bad else "VERIFIED"),
               sources=urls, result={"entity": nid, "name": mg.nodes[nid]["name"],
                                     "type": mg.nodes[nid]["type"], "relations_by_status": grouped})
    if rows and "TIMELINE_CONTEXT_REQUIRED" in env["flags"]:
        env["confidence"] = "QUALIFIED"
    return env


# Batch 11: leader questions query every stored leader relation together. Before this, "led" was asked first and
# "leader_of" only on an empty result, so one "led" edge (e.g. a former guildmaster) could hide every "leader_of" edge.
LEADER_UNION = "led|leader_of|leads"

PATTERNS = [  # (regex, relation, direction from the named entity's point of view)
    (re.compile(r"who (?:is|are|was|were) (.+?)'s (?:brother|sister|sibling|twin)s?\??$", re.I), "sibling_of|twin_sibling_of", None),  # Batch 9: both, so a twin is never hidden by other siblings
    (re.compile(r"who (?:is|was) (.+?)'s (?:wife|husband|spouse)\??$", re.I), "spouse_of", None),
    (re.compile(r"who (?:defeated|slew|beat) (?:the )?(.+?)\??$", re.I), "defeated_by", "out"),
    (re.compile(r"who (?:created|made|built) (?:the )?(.+?)\??$", re.I), "created", "in"),
    (re.compile(r"who (?:destroyed|killed) (?:the )?(.+?)\??$", re.I), "destroyed", "in"),
    (re.compile(r"where did (?:the )?(.+?) come from\??$", re.I), "origin", "out"),
    (re.compile(r"who (?:is|was) (.+?)'s mother\??$", re.I), "mother_of", "in"),
    (re.compile(r"who struck down (?:the )?(.+?)\??$", re.I), "struck_down", "in"),
    # Phase 7 rephrasings (Batch 6): synonyms routed to relations already stored by claim packs
    (re.compile(r"who (?:murdered|assassinated|beheaded) (?:the )?(.+?)\??$", re.I), "killed", "in"),
    (re.compile(r"who (?:was|were) (?:the )?(.+?) (?:killed|murdered|slain) by\??$", re.I), "killed", "in"),
    (re.compile(r"who (?:freed|released|liberated|rescued) (?:the )?(.+?)\??$", re.I), "freed", "in"),
    (re.compile(r"who (?:captured|kidnapped|abducted|took) (?:the )?(.+?)(?: captive)?\??$", re.I), "captured", "in"),
    (re.compile(r"who (?:imprisoned|sealed away|sealed|trapped) (?:the )?(.+?)\??$", re.I), "imprisoned", "in"),
    # A generic parent_of edge does NOT prove whether the person is a mother or father.
    (re.compile(r"who (?:is|was) (.+?)'s (?:father|dad)\??$", re.I), "father_of", "in"),
    (re.compile(r"who (?:is|was) (.+?)'s parent\??$", re.I), "parent_of|mother_of|father_of", "in"),
    (re.compile(r"who (?:are|were) (.+?)'s parents\??$", re.I), "parent_of|mother_of|father_of", "in"),
    (re.compile(r"who (?:is|was) (.+?)'s (?:lover|partner|girlfriend|boyfriend|romantic partner)\??$", re.I), "romantically_involved_with", None),
    (re.compile(r"who (?:currently )?(?:leads|led|captains|captained|heads|headed|runs|ran) (?:the )?(.+?)(?: now| today| currently| these days)?\??$", re.I), LEADER_UNION, "in"),
    (re.compile(r"who won (?:the )?(.+?)\??$", re.I), "won", "in"),
    (re.compile(r"who (?:are|were|is|was) (.+?)'s (?:allies|ally|friends|friend)\??$", re.I), "allied_with|friend_of|childhood_friend_of", None),
    # Batch 8 Phase 7 rephrasings over the Batch 7/8 relations
    # Batch 14 Phase 7: "who's", "current", guildmaster/khan/chief/commander titles, "in charge of", "commands"
    (re.compile(r"who(?:'s|’s| is| was| are| were) (?:the )?(?:current |present |new |original |first )?(?:leaders?|heads?|rulers?|captains?|governors?|guildmasters?|guild ?leaders?|chiefs?|commanders?|khans?|masters?|bosses?) of (?:the )?(.+?)\??$", re.I), LEADER_UNION, "in"),
    (re.compile(r"who(?:'s|’s| is| was| are| were) (?:currently )?in (?:charge|command|control) of (?:the )?(.+?)\??$", re.I), LEADER_UNION, "in"),
    (re.compile(r"who (?:commands|commanded) (?:the )?(.+?)\??$", re.I), LEADER_UNION, "in"),
    (re.compile(r"who (?:governs|governed|rules|ruled) (?:over )?(?:the )?(.+?)\??$", re.I), "ruled|" + LEADER_UNION, "in"),
    (re.compile(r"who (?:mentored|taught|trained) (?:the )?(.+?)\??$", re.I), "mentored", "in"),
    (re.compile(r"who (?:is|was|are|were) (.+?)'s (?:mentors?|teachers?)\??$", re.I), "mentored", "in"),
    (re.compile(r"who (?:founded|established) (?:the )?(.+?)\??$", re.I), "founded", "in"),
    (re.compile(r"who (?:guards|guarded|protects|protected|defends|defended) (?:the )?(.+?)\??$", re.I), "guardian_of|guarded|protected|protects|defended", "in"),
    (re.compile(r"who (?:fought|battled) (?:the )?(.+?)\??$", re.I), "fought|confronted", None),
    (re.compile(r"who (?:serves|served|works for|worked for) (?:the )?(.+?)\??$", re.I), "serves|served|works_for|agent_of", "in"),
    (re.compile(r"who (?:worships|worshipped|worship|reveres|revered) (?:the )?(.+?)\??$", re.I), "worships", "in"),
    (re.compile(r"who (?:attacked|invaded|assaulted|marched on) (?:the )?(.+?)\??$", re.I), "attacked|invaded", "in"),
    (re.compile(r"who did (.+?) meet\??$", re.I), "met", "out"),
    (re.compile(r"who met (?:the )?(.+?)\??$", re.I), "met", None),
    (re.compile(r"who (?:are|were|is|was) (.+?)'s (?:enemies|enemy|rivals|rival|foes|foe)\??$", re.I), "opposed", None),
]

FALLBACK = {"created": [("created_by", "out"),  # "who created X" may be stored as X created_by Y
                        ("designed", "in"), ("invented", "in")],  # Batch 5: Kiran designed Heart of Kiran
            "defeated_by": [("defeated", "in")],  # Batch 5: XLN010 stores Bolas defeated Ugin
            "sibling_of": [("twin_sibling_of", None)],  # Pack A stores Ugin/Bolas as twin_sibling_of
            "destroyed": [("killed", "in")],  # Pack C4 stores Karn killed Elesh Norn (Batch 4)
            # Never fall back from gendered mother/father questions to an untyped parent.
            # Batch 6 Phase 7 rephrasings
            "killed": [("destroyed", "in"), ("slew_and_banished", "in")],
            "freed": [("rescued", "in"), ("restored", "in")],
            "captured": [("abducted", "in"), ("imprisoned", "in")],
            "imprisoned": [("captured", "in"), ("bound_to_service", "in")],
            "parent_of|mother_of|father_of": [("child_of", "out")],
            "romantically_involved_with": [("spouse_of", None)],
            "led": [("leader_of", "in"), ("leads", "in")],
            "opposed": [("fought", None)],
            # Batch 8 Phase 7
            "ruled": [("leader_of", "in"), ("led", "in"), ("leads", "in")],
            "mentored": [("taught", "in"), ("learned_from", "out"), ("student_of", "out")],
            "worships": [("revered_by", "out")]}  # "X child_of Y" also answers "who is X's mother"


LEADER_RELATIONS = {"led", "leader_of", "leads", "ruled"}
_FORMER = re.compile(r"\b(former|formerly|before (?:her|his|their) death|was the .* before|until)\b", re.I)
# Batch 9 (Phase 7 retcon/ambiguity): a claim whose summary or limitation places it in an earlier era or an
# original/rewritten timeline is era context, never the "most recent" leader, whatever its page's publication date.
_PAST_ERA = re.compile(r"(\bin [\w' -]+'s past\b|\byears in [\w' -]+'s past\b|\boriginal timeline\b|\bprevious timeline\b)", re.I)
_ERA_LABEL = re.compile(r"\(([^()]*\b(?:present|past|timeline|era)\b[^()]*)\)", re.I)
_dates = None


def source_dates() -> dict:
    global _dates
    if _dates is None:
        with (ROOT / "data/primary_sources.csv").open(encoding="utf-8") as fh:
            _dates = {r["url"].rstrip("/"): r["date"] for r in csv.DictReader(fh)}
    return _dates


def leadership(env: dict) -> dict | None:
    """Batch 9: order leader answers by the publication date of the citing official page, so a question like
    "who leads the Orzhov?" names the most recently cited leader and keeps earlier ones as era context."""
    rows = [r for rs in env.get("result", {}).get("relations_by_status", {}).values() for r in rs]
    if not rows:
        return None
    tl = []
    for r in rows:
        ds = [source_dates().get(u.rstrip("/")) for u in r.get("source_urls", [])]
        ds = [d for d in ds if d]
        tl.append({"node": r["node"], "claim": r["claim"], "status": r["status"], "summary": r.get("summary"),
                   "source_date": max(ds) if ds else None,
                   "described_as_former": bool(_FORMER.search(r.get("summary") or "")),
                   "described_as_past_era": bool(_PAST_ERA.search((r.get("summary") or "") + " " + (r.get("limitation") or ""))),
                   "era_label": (lambda m: m.group(1) if m else None)(_ERA_LABEL.search(r.get("summary") or ""))})
    tl.sort(key=lambda x: (x["source_date"] or "", x["claim"]))
    live = [x for x in tl if not x["described_as_former"] and not x["described_as_past_era"]] or tl
    latest = live[-1]
    death_evidence = []
    for r in graph().neighbors(latest["node"]):
        if (r.get("claim") and r.get("status") == "CANON_CONFIRMED"
                and r.get("relation") in {"inverse_of:killed", "inverse_of:slain", "inverse_of:destroyed"}):
            death_evidence.append({"claim": r["claim"], "sources": r.get("source_urls", []),
                                   "claim_status": r["status"]})
    out = {"most_recent_cited": latest, "timeline": tl,
           "note": ("Ordered by the publication date of the citing official page. The most recent cited leader is the "
                    "latest one these packs cite, not proof of the leader in present-day canon; claims whose summary "
                    "calls the leader former are kept as era context.")}
    if death_evidence:
        out["latest_leader_death_evidence"] = death_evidence
        out["note"] += (" The graph also records this person's death; they must not be presented as "
                        "a verified current leader without later, independent evidence.")
    if any(x["described_as_past_era"] or x["era_label"] for x in tl):
        out["era_note"] = ("Some cited claims are labelled with an in-universe era or timeline. Publication order is not "
                           "in-universe order: claims set in a past era or an original/rewritten timeline are kept as era "
                           "context and are never reported as the most recent leader. Where a story rewrote history, "
                           "the cited claims here do not by themselves establish who leads in present-day canon.")
    return out


# Batch 10 Phase 7: retcon / continuity explainer. Lists every cited account about an entity that the packs
# mark as disputed, alternate-continuity, open, or limited by a timeline/retcon caveat, side by side with its
# own sources. It never picks a winner: conflicting accounts are reported, not resolved.
CONTINUITY_PATTERNS = [
    re.compile(r"^(?:explain|describe) (?:the )?(?:continuity|canon|retcons?|timeline) (?:of|for|around|about) (?:the )?(.+?)\??$", re.I),
    re.compile(r"^is (?:the )?(.+?) (?:canon|still canon|a retcon|retconned)\??$", re.I),
    re.compile(r"^(?:was|were|has|have) (?:the )?(.+?) (?:been )?retconned\??$", re.I),
    re.compile(r"^(?:what are )?(?:the )?(?:conflicting|contradictory|disputed) (?:accounts|stories|claims|versions) (?:of|about) (?:the )?(.+?)\??$", re.I),
    re.compile(r"^(?:any )?retcons? (?:of|about|for|involving) (?:the )?(.+?)\??$", re.I),
]
CONTINUITY_STATUSES = ("CANON_DISPUTED", "ALTERNATE_CONTINUITY", "OPEN_QUESTION")
_CONT_LIMIT = re.compile(r"\b(retcon\w*|timeline|rewr(?:ote|itten|iting)|contradict\w*|conflict\w*|alternate|unresolved|"
                         r"disputed|rumou?r|accus\w*|unreliable|earlier account|later story|in-universe history)\b", re.I)
_edge_dates = None


def edge_dates() -> dict:
    global _edge_dates
    if _edge_dates is None:
        _edge_dates = {e["claim"]: e["in_universe_date"] for e in graph().g["edges"]
                       if e.get("claim") and e.get("in_universe_date")}
    return _edge_dates


def continuity(term: str) -> dict:
    env = lore(term)
    env["route"] = "continuity"
    if env["confidence"] == "NOT_FOUND":
        return env
    accounts, seen = [], set()
    for status, rows in env["result"]["relations_by_status"].items():
        for r in rows:
            lim = r.get("limitation") or ""
            caveat = _CONT_LIMIT.search(lim)
            if status not in CONTINUITY_STATUSES and not caveat:
                continue
            if r["claim"] in seen:
                continue
            seen.add(r["claim"])
            accounts.append({"claim": r["claim"], "status": status, "relation": r["relation"], "other": r["name"],
                             "summary": r.get("summary"), "limitation": lim or None, "stage": r.get("stage") or None,
                             "in_universe_date": edge_dates().get(r["claim"]),
                             "why_listed": status if status in CONTINUITY_STATUSES else "LIMITATION_MENTIONS:" + caveat.group(1).lower(),
                             "source_urls": r.get("source_urls", [])})
    order = {s: i for i, s in enumerate(CONTINUITY_STATUSES)}
    accounts.sort(key=lambda a: (order.get(a["status"], 9), a["claim"]))
    others = sum(len(v) for v in env["result"]["relations_by_status"].values()) - len(accounts)
    env["result"] = {"entity": env["result"]["entity"], "name": env["result"]["name"], "type": env["result"]["type"],
                     "continuity_accounts": accounts, "other_cited_claims": others,
                     "note": ("Each account is shown with its own grade, caveat and official sources. Disputed, "
                              "alternate-continuity and open claims are not resolved here; the cited pages do not settle "
                              "them, and publication order is not in-universe order.")}
    env["flags"] = [f for f in env["flags"] if not f.endswith("_PRESENT")]
    env["flags"] += sorted({a["status"] + "_PRESENT" for a in accounts if a["status"] in CONTINUITY_STATUSES})
    if accounts:
        env["confidence"] = "QUALIFIED"
    else:
        env["flags"].append("NO_CITED_CONTINUITY_CONFLICT")
    return env


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


def plane_history(name: str) -> dict | None:
    """One source-limited answer per cited claim, even when it touches several places."""
    from query_plane_history import query

    found = query(re.sub(r'^the plane (?:of )?', '', name.strip().rstrip('?'), flags=re.I))
    if found['status'] == 'NOT_FOUND':
        return None  # preserve the normal fallback for names not known as planes
    plane = found['plane']
    claims = {}
    urls = set()
    for fact in plane['facts']:
        row = claims.setdefault(fact['claim_id'], {
            'claim_id': fact['claim_id'], 'grade': fact['grade'],
            'statement': fact['statement'], 'limitation': fact['limitation'],
            'era_label_not_order': fact['era_label'],
            'in_universe_date': fact['in_universe_date'],
            'relations': [], 'sources': [],
        })
        row['relations'].append({'subject': fact['subject']['name'],
                                 'relation': fact['relation'], 'object': fact['object']['name']})
        for source in fact['sources']:
            urls.add(source['url'])
            if source['url'] not in row['sources']:
                row['sources'].append(source['url'])
    statuses = {x['grade'] for x in claims.values()}
    flags = ['PARTIAL_REGISTERED_PLANE_HISTORY', 'NO_VERIFIED_TOTAL_CHRONOLOGY']
    contextual = plane.get('contextual_claims', [])
    if contextual:
        flags.append('CURATED_ON_PLANE_CONTEXT_NOT_DIRECT_GRAPH_CLAIMS')
        for item in contextual:
            statuses.add(item['grade'])
            for evidence in item['source_evidence']:
                urls.add(evidence['url'])
    if 'CANON_DISPUTED' in statuses:
        flags.append('CANON_DISPUTED_PRESENT')
    if 'CANON_IMPLIED' in statuses:
        flags.append('CANON_IMPLIED_PRESENT')
    if 'OPEN_QUESTION' in statuses:
        flags.append('OPEN_QUESTION_PRESENT')
    if 'ALTERNATE_CONTINUITY' in statuses:
        flags.append('ALTERNATE_CONTINUITY_PRESENT')
    return {'route': 'ask->plane_history', 'confidence': 'QUALIFIED',
            'flags': flags, 'data_as_of': '2026-10-30', 'sources': sorted(urls),
            'result': {'plane': plane['plane'], 'plane_id': plane['id'],
                       'direct_claims': plane['distinct_claims'],
                       'claims': list(claims.values()),
                       'contextual_claim_count':len(contextual),
                       'contextual_claims':contextual,
                       'complete_history': False,
                       'verified_total_chronology': False,
                       'known_gaps': plane['known_gaps']}}


def entity_history(name: str) -> dict | None:
    """Expose direct cited Character/Faction claims without pretending to tell a full biography.

    This is intentionally not an inferred chronology or a traversal through a
    character's friends, cards, places or entire faction. One claim may have
    several direct relations; it is counted once with all its cited edges.
    """
    term = re.sub(r'^the (?:character|faction|organization|organisation) (?:of )?',
                  '', name.strip().rstrip('?'), flags=re.I)
    nid = _find(term)
    mg = graph()
    if not nid or mg.nodes[nid]['type'] not in {'Character', 'Faction'}:
        return None
    baseline = lore(term)
    claims: dict[str, dict] = {}
    sources = set()
    for grade, rows in baseline['result']['relations_by_status'].items():
        for relation in rows:
            claim_id = relation['claim']
            claim_node = mg.nodes.get('claim:' + claim_id)
            if not claim_node or claim_node.get('grade') != grade:
                raise ValueError(f'Inconsistent cited entity-history claim {claim_id}')
            row = claims.setdefault(claim_id, {
                'claim_id': claim_id, 'grade': grade,
                'statement': claim_node['name'],
                'limitation': claim_node.get('limitation') or None,
                'era_label_not_order': claim_node.get('stage'),
                'in_universe_date': edge_dates().get(claim_id),
                'relations': [], 'sources': [],
            })
            if row['grade'] != grade:
                raise ValueError(f'Conflicting grades for entity-history claim {claim_id}')
            edge = {'direction': relation['direction'], 'relation': relation['relation'],
                    'other_id': relation['node'], 'other_name': relation['name'],
                    'other_type': relation['type']}
            if edge not in row['relations']:
                row['relations'].append(edge)
            for url in relation['source_urls']:
                sources.add(url)
                if url not in row['sources']:
                    row['sources'].append(url)
    for row in claims.values():
        row['relations'].sort(key=lambda r: (r['direction'], r['relation'], r['other_id']))
        row['sources'].sort()
    grades = {c['grade'] for c in claims.values()}
    flags = ['PARTIAL_CITED_ENTITY_HISTORY', 'DIRECT_GRAPH_CLAIMS_ONLY',
             'NO_VERIFIED_TOTAL_CHRONOLOGY']
    flags += [g + '_PRESENT' for g in sorted(grades & QUALIFYING)]
    flags += [f for f in baseline['flags'] if f.startswith('MATCHED_BY_')]
    if not claims:
        flags.append('NO_CITED_ENTITY_HISTORY')
    return {'route': 'ask->entity_history',
            'confidence': 'QUALIFIED' if claims else 'NOT_FOUND',
            'flags': flags, 'data_as_of': baseline['data_as_of'],
            'sources': sorted(sources),
            'result': {'entity': nid, 'name': mg.nodes[nid]['name'],
                       'type': mg.nodes[nid]['type'],
                       'direct_claims': len(claims),
                       'claims': [claims[k] for k in sorted(claims)],
                       'complete_history': False,
                       'verified_total_chronology': False,
                       'known_gaps': [
                           'Only cited graph edges directly incident on this entity are included.',
                           'Other stories, relationships, eras and unregistered entities may be missing.',
                           'Publication dates and era labels cannot establish event order or present-day status.',
                           'The absence of a claim does not prove an event or relationship never occurred.',
                       ]}}


def parent_role(term: str, relation: str) -> dict:
    """Never identify an untyped parent (or the other parent) as a father/mother.

    Accept a role-specific edge or a directly worded, cited parent_of claim;
    keep any other family relationships as context, not a gendered answer.
    """
    answer = lore(term, relation, 'in')
    if answer['confidence'] != 'NOT_FOUND':
        return answer
    # A few older packs stored explicitly worded father claims as generic
    # parent_of edges. Only accept the actual parent's name next to the role,
    # not the child's gender, a title such as King, or a bare 'son of' phrase.
    role = relation.removesuffix('_of')
    typed = lore(term, 'parent_of', 'in')
    quoted = {}
    for grade, rows in typed.get('result', {}).get('relations_by_status', {}).items():
        for row in rows:
            wording = row.get('summary') or ''
            parent_name = re.escape(row['name'])
            if (re.search(r'\b' + role + r'\s+(?:is|was)\s+' + parent_name + r'\b', wording, re.I) or
                re.search(r'\b' + parent_name + r'\b.{0,70}\b(?:his|her|their|the)\s+' + role + r'\b', wording, re.I)):
                quoted.setdefault(grade, []).append(row)
    if quoted:
        typed['result']['relations_by_status'] = quoted
        typed['sources'] = sorted({url for rows in quoted.values() for row in rows
                                   for url in row.get('source_urls', [])})
        typed['flags'].append('PARENT_ROLE_EXPLICIT_IN_CITED_CLAIM')
        typed['confidence'] = ('QUALIFIED' if set(quoted) & QUALIFYING else 'VERIFIED')
        return typed
    family = lore(term, 'parent_of|mother_of|father_of|child_of')
    contextual = []
    for rows in family.get('result', {}).get('relations_by_status', {}).values():
        for row in rows:
            if ((row['relation'] in {'inverse_of:parent_of', 'inverse_of:mother_of', 'inverse_of:father_of'}
                 and row['direction'] == 'in') or
                (row['relation'] == 'child_of' and row['direction'] == 'out')):
                contextual.append(row)
    answer['sources'] = sorted({url for row in contextual for url in row.get('source_urls', [])})
    answer['flags'] = ['NO_ROLE_SPECIFIC_PARENT_EVIDENCE']
    answer['result']['known_parental_relations_not_answer'] = contextual
    answer['result']['note'] = (f'The cited graph does not establish a {relation.removesuffix("_of")}. '
                                'Other parent or family edges are context only; they do not answer this question.')
    return answer


def chronology_question(text: str) -> dict | None:
    """Answer only recognizable two-event comparisons; ambiguous names never guess."""
    intent, left, right = None, None, None
    for regex, mode in _CHRONOLOGY_QUESTION_PATTERNS:
        m = regex.search(text)
        if m:
            intent = 'first' if mode == 'FIRST' else m.group(2).lower()
            left = m.group(1).strip().strip('"“”')
            right = (m.group(2) if mode == 'FIRST' else m.group(3)).strip().strip('"“”')
            break
    if intent is None:
        return None

    # This read-only route uses the existing exact, independently regenerated
    # chronology files. It never infers global AR years or publication-order links.
    from query_lore_chronology import DATA, compare_across_datasets
    from source_event_sequences import OUT
    old = json.loads(DATA.read_text(encoding='utf-8'))
    local = json.loads(OUT.read_text(encoding='utf-8'))
    envelope = {'route':'ask->chronology', 'query':text, 'data_as_of':'2026-10-30',
                'sources':[], 'flags':['PARTIAL_IN_UNIVERSE_CHRONOLOGY']}
    try:
        evidence = compare_across_datasets(old, local, left, right)
    except ValueError:
        envelope.update(confidence='NOT_FOUND',
                        flags=envelope['flags']+['UNKNOWN_OR_AMBIGUOUS_EVENT_LABEL'],
                        result={'left_input':left, 'right_input':right,
                                'relation':'UNKNOWN', 'answer':None,
                                'guidance':'Use a unique event-label phrase or full ID from scripts/query_lore_chronology.py --list.'})
        return envelope

    labels = {n['id']:n['label'] for n in old['nodes']+local['nodes']}
    nodes = {n['id']:n for n in local['nodes']}
    relation = evidence['result']
    if relation == 'BEFORE':
        first = evidence['left']
    elif relation == 'AFTER':
        first = evidence['right']
    else:
        first = None
    answer = (labels[first] if first else None) if intent == 'first' else (
        relation == intent.upper() if relation in {'BEFORE','AFTER'} else None)
    proof = evidence.get('proof', [])
    corroboration = evidence.get('printed_ar_sources', [])
    urls = {e['source_url'] for e in proof+corroboration if e.get('source_url')}
    envelope['sources'] = sorted(urls)
    if relation == 'UNKNOWN':
        envelope['flags'].append('NO_CITED_CHRONOLOGY_PATH')
    if relation == 'DURING_OR_AFTER_START':
        envelope['flags'].append('OVERLAP_NOT_STRICT_ORDER')
    if any(nodes.get(evidence[key], {}).get('certainty') == 'NARRATED_TRADITION_ONLY'
           for key in ('left','right')):
        envelope['flags'].append('NARRATED_LEGEND_NOT_VERIFIED_HISTORY')
    if any(e.get('relation') == 'SAME_EVENT' for e in proof):
        # A supported legacy→local→legacy detour also deserves this flag;
        # endpoint ledger membership alone cannot identify the proof route.
        envelope['flags'].append('CROSS_LEDGER_SOURCE_BRIDGED')
    elif any(nid in nodes for nid in (evidence['left'],evidence['right'])) and not all(
            nid in nodes for nid in (evidence['left'],evidence['right'])):
        envelope['flags'].append('CROSS_LEDGER_UNANCHORED')
    envelope.update(confidence='QUALIFIED', result={
        'intent':intent, 'left_id':evidence['left'], 'right_id':evidence['right'],
        'left_event':labels[evidence['left']], 'right_event':labels[evidence['right']],
        'relation':relation, 'answer':answer, 'proof':proof,
        'printed_ar_sources':corroboration,
        'limitation':evidence.get('limitation') or 'Only a bounded source-local account is known.',
        'verified_total_chronology':False,
    })
    return envelope


def chronology_overview_question(text: str) -> dict | None:
    """Present one *bounded* source-local partial order, never a synthetic timeline.

    A strand must be selected uniquely by explicit ID, full title, or a phrase
    appearing in exactly one title. Ambiguous subjects are not arbitrarily
    resolved to the best-known account (e.g. Mirrodin has distinct ledgers).
    """
    explicit = _EXPLICIT_STRAND.fullmatch(text)
    topic = explicit.group(1) if explicit else next(
        (m.group(1) for rx in _CHRONOLOGY_OVERVIEW_PATTERNS
         if (m := rx.fullmatch(text))), None)
    if topic is None:
        return None

    from source_event_sequences import OUT
    local = json.loads(OUT.read_text(encoding='utf-8'))
    term = topic.strip().strip('?.! ').casefold()
    if not explicit:
        term = re.sub(r'^the\s+', '', term)
    if explicit:
        choices = [s for s in local['strands'] if s['id'].casefold() == term]
    elif len(term) >= 4:
        choices = [s for s in local['strands'] if s['title'].casefold() == term or
                   re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)',
                             s['title'].casefold())]
    else:
        choices = []
    env = {'route': 'ask->chronology_overview', 'query': text,
           'data_as_of': local['date'], 'sources': [],
           'flags': ['SOURCE_LOCAL_NOT_GLOBAL_CHRONOLOGY']}
    if len(choices) != 1:
        ambiguous = len(choices) > 1
        env.update(confidence='NOT_FOUND',
                   flags=env['flags'] + [
                       'AMBIGUOUS_SOURCE_STRAND' if ambiguous else 'NO_MATCHING_SOURCE_STRAND'],
                   result={'topic': topic, 'strand': None, 'events': [],
                           'strict_edges': [], 'candidates': [
                               {'id': s['id'], 'title': s['title']} for s in choices],
                           'guidance': ('Specify the exact strand ID with "Show chronology strand X" '
                                        'or use a unique phrase from the strand title.'),
                           'verified_total_chronology': False})
        return env

    strand = choices[0]
    sid = strand['id']
    nodes = [n for n in local['nodes'] if n['strand'] == sid]
    ids = {n['id'] for n in nodes}
    edges = [e for e in local['edges'] if e['earlier'] in ids and e['later'] in ids]
    before = [e for e in edges if e['relation'] == 'BEFORE']
    other = [e for e in edges if e['relation'] != 'BEFORE']
    reaches = {nid: [end for end in local['precedes'][nid] if end in ids]
               for nid in sorted(ids)}
    pairs = sum(len(v) for v in reaches.values())
    possible = len(nodes) * (len(nodes) - 1) // 2
    unresolved = possible - pairs
    if unresolved < 0 or len(nodes) != strand['events'] or len(before) != strand['strict_edges']:
        raise ValueError(f'Invalid source-local chronology metadata for {sid}')
    flags = env['flags'] + ['PARTIAL_SOURCE_LOCAL_CHRONOLOGY']
    if unresolved:
        flags.append('UNRESOLVED_STRICT_EVENT_ORDER')
    if other:
        flags.append('NON_STRICT_TEMPORAL_RELATIONS_PRESENT')
    if strand['certainty'] == 'NARRATED_TRADITION_ONLY':
        flags.append('NARRATED_LEGEND_NOT_VERIFIED_HISTORY')
    env.update(confidence='QUALIFIED', flags=flags,
               sources=sorted({e['source_url'] for e in edges}),
               result={'topic': topic, 'strand': strand,
                       'events': nodes,  # ID order is NOT chronology order.
                       'strict_edges': before, 'non_strict_relations': other,
                       'strict_order_reachability': reaches,
                       'ordered_event_pairs': pairs, 'possible_event_pairs': possible,
                       'unresolved_strict_pairs': unresolved,
                       'source_local_total_order': unresolved == 0,
                       'verified_total_chronology': False,
                       'limitation': strand['limitation'],
                       'display_guidance': ('Event array order is by ID, not event time. '
                                            'Only BEFORE edges and their transitive closure prove strict order; '
                                            'other pairs are UNKNOWN or non-strict overlaps. '
                                            'No inter-strand chronology or absolute years are inferred.')})
    return env


def graph_connection_question(text: str) -> dict | None:
    """Find a source-backed navigation path, not an inferred historical relationship.

    A route between two entities can contain reversed claim edges and unrelated
    claims. It establishes only a traceable graph connection, never that the
    endpoint entities met, caused one another's actions or share a dated era.
    """
    match = next((m for rx in _GRAPH_CONNECTION_PATTERNS if (m := rx.fullmatch(text))), None)
    if match is None:
        return None
    left, right = (s.strip().rstrip('?').strip() for s in match.groups())
    mg = graph()
    envelope = {'route': 'ask->graph_connection', 'query': text,
                'data_as_of': mg.g.get('evidence_cutoff') or '2026-10-30',
                'sources': [], 'flags': ['GRAPH_NAVIGATION_ONLY', 'NOT_TEMPORAL_OR_CAUSAL_PROOF']}
    src, dst = _find(left), _find(right)
    if not src or not dst:
        envelope.update(confidence='NOT_FOUND', flags=envelope['flags'] + ['UNKNOWN_OR_AMBIGUOUS_ENDPOINT'],
                        result={'left_input': left, 'right_input': right, 'path': None,
                                'limitation': 'One or both named entities are not uniquely identified by the registered graph.'})
        return envelope
    if src == dst:
        envelope.update(confidence='NOT_FOUND', flags=envelope['flags'] + ['SAME_ENTITY_NOT_A_RELATIONSHIP'],
                        result={'left_id': src, 'right_id': dst, 'path': None})
        return envelope
    path = mg.path(src, dst, max_depth=4)  # confirmed and source-cited only, enforced during BFS
    if not path:
        envelope.update(confidence='NOT_FOUND', flags=envelope['flags'] + ['NO_CITED_GRAPH_PATH_WITHIN_FOUR_HOPS'],
                        result={'left_id': src, 'right_id': dst, 'path': None, 'max_hops': 4,
                                'limitation': 'No qualifying path within the search bound is not proof that a relationship never existed.'})
        return envelope
    if not all(h['status'] == 'CANON_CONFIRMED' and h['claim'] and h['source_urls'] for h in path):
        raise ValueError('Unverified graph edge escaped the confirmed-citation path filter')
    sources = sorted({url for h in path for url in h['source_urls']})
    flags = envelope['flags']
    if ((mg.nodes[src]['name'].lower() != left.lower() and src == _first_name(left)) or
            (mg.nodes[dst]['name'].lower() != right.lower() and dst == _first_name(right))):
        flags.append('MATCHED_BY_FIRST_NAME')
    if ((mg.nodes[src]['name'].lower() != left.lower() and src == _alias(left)) or
            (mg.nodes[dst]['name'].lower() != right.lower() and dst == _alias(right))):
        flags.append('MATCHED_BY_FACTION_ALIAS')
    envelope.update(confidence='QUALIFIED', sources=sources, result={
        'left_id': src, 'left_name': mg.nodes[src]['name'],
        'right_id': dst, 'right_name': mg.nodes[dst]['name'],
        'hops': len(path), 'direct_cited_relation': len(path) == 1,
        'max_hops': 4, 'path': path,
        'limitation': ('Each hop is an individually cited confirmed claim, but the overall path is navigation only. '
                       'Reverse traversal does not reverse historical causation, and a multi-hop path is not a '
                       'claim that the endpoints directly interacted or existed simultaneously.'),
    })
    return envelope


def card_lore_rules_question(text: str) -> dict | None:
    """Join three independently sourced domains without turning a name into art/canon proof.

    A graph names_entity edge identifies the card's *named subject* only. It is
    navigation rather than evidence of a particular illustration, depicted
    event, or story-era print. All legality is dated, and the lore sample is
    deliberately bounded with the total direct-claim count disclosed.
    """
    match = next((m for rx in _CARD_LORE_RULES_PATTERNS if (m := rx.fullmatch(text))), None)
    if match is None:
        return None
    requested = match.group(1).strip().rstrip('?').strip()
    import commander_rules
    row = commander_rules.resolve(requested)
    env = {'route': 'ask->card_lore_commander_evidence', 'query': text,
           'confidence': 'NOT_FOUND', 'flags': [], 'sources': [], 'data_as_of': None}
    if row is None:
        env.update(flags=['NO_SUCH_CARD_IN_INDEX'],
                   result={'requested_card': requested, 'card': None,
                           'limitation': 'No unambiguously indexed card matches this name or unique front face.'})
        return env

    found = card(row['name'])
    rule = commander_rules.commander([row['name']])
    if found['confidence'] == 'NOT_FOUND' or rule['confidence'] == 'NOT_FOUND':
        raise ValueError('Indexed cross-domain card unexpectedly failed its own source lookup')

    mg = graph()
    matches = [nid for nid, node in mg.nodes.items()
               if node.get('type') == 'Card' and node.get('oracle_id') == row['oracle_id']]
    flags = ['DATED_SCRYFALL_LEGALITY_NOT_LIVE', 'NO_RULES_SIMULATION',
             'GRAPH_NAME_BRIDGE_NOT_DEPICTION_PROOF', 'PARTIAL_DIRECT_LORE_ONLY']
    flags += found.get('flags', []) + rule.get('flags', [])
    if len(matches) > 1:
        # A duplicated Oracle identity would make the graph-to-card join
        # ambiguous. Never select a favorite node by title similarity.
        flags.append('AMBIGUOUS_GRAPH_CARD_ORACLE_ID')
        matches = []
    if not matches:
        flags.append('NO_UNIQUE_GRAPH_CARD_ANCHOR')

    entities, urls = [], set(found['sources']) | {rule['rules_source']['url']}
    if matches:
        named = [r for r in mg.neighbors(matches[0])
                 if r['relation'] in {'names_entity', 'inverse_of:names_entity'}
                 and r['type'] in {'Character', 'Faction'}]
        subjects = sorted({r['node'] for r in named})
        if not subjects:
            flags.append('NO_CITED_NAMED_ENTITY_BRIDGE')
        if len(subjects) > 1:
            flags.append('MULTIPLE_NAMED_SUBJECTS_NO_SINGLE_IDENTITY_INFERRED')
        for nid in subjects:
            history = entity_history(nid)
            if history is None:
                raise ValueError('Named graph subject is missing from direct history lookup')
            claims = history['result']['claims']
            sample = claims[:8]
            for claim in sample:
                urls.update(claim['sources'])
            flags += [flag for flag in history['flags'] if flag.endswith('_PRESENT')]
            if len(claims) > len(sample):
                flags.append('LORE_CLAIMS_TRUNCATED_TO_EIGHT_PER_SUBJECT')
            entities.append({'id': nid, 'name': history['result']['name'],
                             'type': history['result']['type'],
                             'bridge': 'GRAPH_NAMES_ENTITY_NAVIGATION_ONLY',
                             'direct_claim_count': len(claims),
                             'direct_claim_grades': sorted({c['grade'] for c in claims}),
                             'sampled_claims': sample,
                             'omitted_claim_count': len(claims) - len(sample)})

    env.update(confidence='QUALIFIED', flags=sorted(set(flags)), sources=sorted(urls),
               data_as_of=mg.g.get('evidence_cutoff') or '2026-10-30',
               evidence_as_of={'card_shard': found['data_as_of'],
                               'scryfall_commander_legality': rule['card_data_as_of'],
                               'comprehensive_rules': rule['rules_source']['effective']},
               result={'card': found['result'], 'commander_eligibility': rule['result'],
                       'commander_rules': rule['rules'], 'rules_source': rule['rules_source'],
                       'named_lore_subjects': entities,
                       'limitation': ('The named-entity graph bridge is a card-name association, not proof of which '
                                      'scene or event the illustration depicts. The lore shown is a bounded sample '
                                      'of direct source-graded claims, not a complete character history. Commander '
                                      'eligibility combines dated Scryfall legality and dated official rules; it '
                                      'is not a live ban check, gameplay simulation or deck recommendation.')})
    return env


def ask(text: str) -> dict:
    q = text.strip()
    for rx, kind in RULES_PATTERNS:
        m = rx.search(q)
        if m:
            env = _rules(kind, m)
            env.update(route="ask->rules:" + kind, query=q)
            return env
    # A graph-only question must not require importing the large Set Atlas or
    # historical rules shards; this route is also useful in a sparse clone.
    connection = graph_connection_question(q)
    if connection is not None:
        return connection
    combined = card_lore_rules_question(q)
    if combined is not None:
        return combined
    # The bounded, cited event ledger is independent of the much larger
    # card-printing and rules snapshots. An event-order question should use
    # that ledger directly, including in research-only sparse checkouts.
    chronology = chronology_question(q)
    if chronology is not None:
        return chronology
    overview = chronology_overview_question(q)
    if overview is not None:
        return overview
    from ask_set_atlas import try_answer as set_atlas_answer
    set_answer = set_atlas_answer(q)
    if set_answer is not None:
        return set_answer
    from ask_rules_evidence import try_answer as rules_evidence_answer
    evidence_answer = rules_evidence_answer(q)
    if evidence_answer is not None:
        return evidence_answer
    for rx in _PLANE_HISTORY_PATTERNS:
        m = rx.search(q)
        if m:
            env = plane_history(m.group(1))
            if env is not None:
                env['query'] = q
                return env
            env = entity_history(m.group(1))
            if env is not None:
                env['query'] = q
                return env
    for rx in CONTINUITY_PATTERNS:
        m = rx.search(q)
        if m:
            env = continuity(m.group(1).strip())
            env.update(route="ask->continuity", query=q)
            return env
    for rx, rel, direction in PATTERNS:
        m = rx.search(q)
        if m:
            env = (parent_role(m.group(1).strip(), rel) if rel in {'mother_of', 'father_of'}
                   else lore(m.group(1).strip(), rel, direction))
            for alt, alt_dir in FALLBACK.get(rel, []):
                if env["confidence"] != "NOT_FOUND":
                    break
                rel, direction = alt, alt_dir
                env = lore(m.group(1).strip(), rel, direction)
            env.update(route="ask->lore:" + rel, query=q)
            if "'s parents" in q.lower() and env['confidence'] != 'NOT_FOUND':
                # The graph may cite one parent but has never verified an exhaustive family roster.
                env['flags'].append('PARENT_ROSTER_NOT_EXHAUSTIVELY_VERIFIED')
                env['confidence'] = 'QUALIFIED'
                env['result']['note'] = ('These are the cited parent relations, not a verified complete list '
                                         'of biological, adoptive, or other parents.')
            if set(rel.split("|")) & LEADER_RELATIONS and env["confidence"] != "NOT_FOUND":
                lead = leadership(env)
                env["result"]["leadership"] = lead
                if len({x["node"] for x in lead["timeline"]}) > 1:
                    env["flags"].append("MULTIPLE_LEADERS_ACROSS_ERAS")
                if "era_note" in lead:
                    env["flags"].append("ERA_OR_TIMELINE_CONTEXT")
                if "latest_leader_death_evidence" in lead:
                    env["flags"].append("LATEST_CITED_LEADER_DEATH_RECORDED")
                    env["confidence"] = "QUALIFIED"
                if _CURRENT_CUE.search(q) or _PRESENT_LEADER_QUESTION.search(q):
                    env["flags"].append("CURRENT_LEADER_NOT_ESTABLISHED")
                    env["confidence"] = "QUALIFIED"
                    # Neither the most recently published nor an undated cited leader
                    # proves who presently holds office, even without the word "current".
                    lead["verified_current_leader"] = None
                requested_rank = re.search(r'\b(first|original|new)\b', q, re.I)
                if requested_rank:
                    env['flags'].append('REQUESTED_LEADER_CHRONOLOGY_NOT_ESTABLISHED')
                    env['confidence'] = 'QUALIFIED'
                    lead['requested_rank'] = requested_rank.group(1).lower()
                    lead['verified_requested_leader'] = None
                    lead['note'] += (' The latest publication-date citation cannot establish who was first, '
                                     'original, or newly appointed in in-universe history.')
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
