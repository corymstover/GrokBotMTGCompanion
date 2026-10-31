#!/usr/bin/env python3
"""Snapshot-qualified natural-language entry points into the Phase 1B Set Atlas.

All quantities describe the committed 2026-10-29 historical shard snapshot,
not a live list of Wizards expansions or a claim about in-universe chronology.
"""
import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path

from historical_set_lookup import card_query, set_query

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "data" / "set_atlas"
CATALOG_PATH = ATLAS / "catalog_2026-10-29.json"
RELEASE_PATH = ATLAS / "phase1b_qualified_functional_release_2026-10-29.json"
REPO_SOURCE = "https://github.com/corymstover/GrokBotMTGCompanion/blob/main/data/set_atlas/"
SCOPE_FLAGS = ["ENGLISH_PAPER_ONLY", "RELEASED_AS_OF_SNAPSHOT", "SOURCE_BULK_NOT_PRESENT",
               "PRINTING_DATE_NOT_IN_UNIVERSE_CHRONOLOGY"]

_ALIASES = {"alpha": "lea", "beta": "leb", "unlimited": "2ed", "revised": "3ed"}
_TOTAL = re.compile(
    r"^(?:how many|what(?: is|'s) the (?:number|count) of)\s+"
    r"(?:magic(?: the gathering)?|mtg)?\s*(?:published |released )?"
    r"(?:sets?|expansions?|set codes?)\s*(?:have (?:been )?released|are there|exist|in total)?\??$", re.I)
_SET_QUESTIONS = [
    (re.compile(r"^how many (?:unique |different |distinct )?cards? (?:are|were|appear|appeared) "
                r"(?:there )?in (.+?)\??$", re.I), "count"),
    (re.compile(r"^(?:what|which) cards? (?:are|were|appear|appeared|were printed) "
                r"(?:there )?in (.+?)\??$", re.I), "list"),
    (re.compile(r"^(?:what|which) cards? debuted in (.+?)\??$", re.I), "debut"),
    (re.compile(r"^(?:what|which) cards? (?:are|were) reprints? in (.+?)\??$", re.I), "reprint"),
    (re.compile(r"^(?:list|show)(?: me)? (?:all |the )?cards? (?:in|from) (.+?)\??$", re.I), "list"),
    (re.compile(r"^(?:how many|what(?:'s| is) the number of) (?:card )?printings? "
                r"(?:are|were|appear|appeared)?\s*(?:there )?in (.+?)\??$", re.I), "count"),
]
_CARD_QUESTIONS = [
    re.compile(r"^(?:which|what) sets? (?:was|were|is) (.+?) (?:printed|reprinted|released) in\??$", re.I),
    re.compile(r"^(?:where|when) was (.+?) first (?:printed|released|published)\??$", re.I),
    re.compile(r"^(?:which|what) sets? did (.+?) (?:first )?(?:debut|appear) in\??$", re.I),
    re.compile(r"^(?:what(?:'s| is) the|show(?: me)? the) (?:printing history|print history) "
               r"(?:of|for) (.+?)\??$", re.I),
    re.compile(r"^what (?:set|expansion) did (.+?) debut in\??$", re.I),
]


@lru_cache(maxsize=1)
def _data():
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    release = json.loads(RELEASE_PATH.read_text(encoding="utf-8"))
    if catalog["as_of"] != release["as_of"]:
        raise ValueError("Historical Set Atlas cutoff disagrees with its acceptance record")
    return catalog, release


def _envelope(query, route, result, sources, flags=None, confidence="QUALIFIED"):
    catalog, _ = _data()
    return {"route": "ask->set_atlas:" + route, "query": query, "confidence": confidence,
            "data_as_of": catalog["as_of"], "sources": sources,
            "flags": SCOPE_FLAGS + (flags or []), "result": result}


def _clean_set_name(name):
    name = name.strip().rstrip("?.! ")
    name = re.sub(r"^the\s+", "", name, flags=re.I)
    name = re.sub(r"\s+(?:set|expansion)$", "", name, flags=re.I)
    return name.strip()


def _set_code(raw):
    catalog, _ = _data()
    sets = catalog["sets"]
    name = _clean_set_name(raw)
    alias = _ALIASES.get(name.casefold(), name.casefold())
    if alias in sets:
        return alias, []
    matches = [code for code, meta in sets.items() if meta["name"].casefold() == name.casefold()]
    if len(matches) == 1:
        return matches[0], []
    return None, sorted(matches)


def _answer_total(query):
    _, release = _data()
    groups = release["exclusive_set_code_scopes"]
    return _envelope(query, "categories", {
        "question_scope": "Scryfall set codes classified by committed Phase 1B research, not an official universal expansion count",
        "exclusive_set_code_scopes": groups,
        "total_catalogued_codes": sum(groups.values()),
        "historical_regular_mainline_scope_count": groups["historical_regular_mainline"],
        "limitations": [release["release_limitations"][2], release["release_limitations"][3],
                        release["release_limitations"][6]],
        "qualified_answer": "136 reviewed historical regular/mainline set codes; other categories are separate and include promos, tokens, digital and future codes. No universal official expansion total is asserted.",
    }, [REPO_SOURCE + RELEASE_PATH.name], ["NOT_A_UNIVERSAL_PREMIER_SET_TOTAL"])


def _answer_set(query, raw_set, mode):
    code, ambiguous = _set_code(raw_set)
    catalog, _ = _data()
    if code is None:
        return _envelope(query, "set", {"requested_set": _clean_set_name(raw_set),
                                       "ambiguous_set_codes": ambiguous},
                         [REPO_SOURCE + CATALOG_PATH.name],
                         ["AMBIGUOUS_SET_NAME" if ambiguous else "UNKNOWN_SET_IN_SNAPSHOT"], "NOT_FOUND")
    meta = catalog["sets"][code]
    history = set_query(code)
    classified = {status: sum(c["classification"] == status for c in history["cards"])
                  for status in ("debut", "tied debut", "reprint", "unresolved identity")}
    result = {"set_code": code, "set_name": meta["name"], "catalogued_set_type": meta["set_type"],
              "distinct_identities_or_unresolved": history["distinct_identities_or_unresolved"],
              "printing_records": history["printing_records"],
              "identity_classifications": classified,
              "catalog_earliest_printing_date": meta["earliest_printing_date"],
              "count_basis": "English-language paper printing records released by the snapshot cutoff; identities use Oracle IDs and unresolved records remain separate",
              "card_list_complete": mode in ("list", "debut", "reprint"),
              "card_list_scope": {"list": "all", "debut": "debut or tied debut",
                                  "reprint": "reprint"}.get(mode)}
    if mode in ("list", "debut", "reprint"):
        result["cards"] = [c for c in history["cards"]
                           if mode == "list" or (mode == "debut" and c["classification"] in ("debut", "tied debut"))
                           or (mode == "reprint" and c["classification"] == "reprint")]
    return _envelope(query, "set", result,
                     [REPO_SOURCE + CATALOG_PATH.name,
                      REPO_SOURCE + "historical_sets_" + hashlib.sha256(code.encode()).hexdigest()[0] + ".json",
                      "https://scryfall.com/sets/" + code],
                     ["UNRESOLVED_ORACLE_IDENTITIES_PRESENT"] if classified["unresolved identity"] else [])


def _answer_card(query, raw_card):
    name = raw_card.strip().rstrip("?.! ")
    history = card_query(name)
    cards = []
    catalog, _ = _data()
    source_files = set()
    for card in history["cards"]:
        printings = card["printings"]
        earliest = min(p["released_at"] for p in printings)
        first_codes = sorted({p["set"] for p in printings if p["released_at"] == earliest})
        distinct_codes = list(dict.fromkeys(p["set"] for p in printings))
        source_files.add("historical_cards_" + card["oracle_id"][0].lower() + ".json")
        cards.append({"name": card["name"], "oracle_id": card["oracle_id"],
                      "first_recorded_printing_date": earliest,
                      "first_recorded_sets": [{"code": code, "name": catalog["sets"].get(code, {}).get("name", code)}
                                              for code in first_codes],
                      "distinct_set_codes": distinct_codes,
                      "printing_record_count": len(printings), "printings": printings})
    flags = []
    if history["matched_identities"] > 1:
        flags.append("MULTIPLE_ORACLE_IDENTITIES_MATCH_NAME")
    if not cards:
        flags.append("NO_MATCHING_RELEASED_ENGLISH_PAPER_PRINTING")
    return _envelope(query, "card_printings",
                     {"requested_card": name, "matched_oracle_identities": len(cards), "cards": cards,
                      "first_recorded_date_is_not_in_universe_debut": True,
                      "printings_do_not_imply_tournament_legality_or_standalone_product_status": True},
                     [REPO_SOURCE + p for p in sorted(source_files)] or [REPO_SOURCE + CATALOG_PATH.name],
                     flags, "QUALIFIED" if cards else "NOT_FOUND")


def try_answer(text):
    """Return an evidence-enveloped set answer, or None for non-set questions."""
    query = text.strip()
    if _TOTAL.fullmatch(query):
        return _answer_total(query)
    for pattern, mode in _SET_QUESTIONS:
        match = pattern.fullmatch(query)
        if match:
            return _answer_set(query, match.group(1), mode)
    for pattern in _CARD_QUESTIONS:
        match = pattern.fullmatch(query)
        if match:
            return _answer_card(query, match.group(1))
    return None
