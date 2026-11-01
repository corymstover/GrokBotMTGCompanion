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
STORY_BRIDGE_PATH = ATLAS / "phase1b_release_scope_story_bridge_2026-10-29.json"
REPO_SOURCE = "https://github.com/corymstover/GrokBotMTGCompanion/blob/main/data/set_atlas/"
SCOPE_FLAGS = ["ENGLISH_PAPER_ONLY", "RELEASED_AS_OF_SNAPSHOT", "SOURCE_BULK_NOT_PRESENT",
               "PRINTING_DATE_NOT_IN_UNIVERSE_CHRONOLOGY"]
STORY_SCOPE_FLAGS = ["HISTORICAL_SET_API_METADATA_ONLY", "STORY_TITLE_LINK_INDEX_NOT_EXHAUSTIVE",
                     "SET_DATE_NOT_IN_UNIVERSE_CHRONOLOGY"]

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
_SET_STORY_QUESTIONS = [
    re.compile(r"^what official (?:magic )?stor(?:y|ies) (?:are|were) linked to (.+?)\??$", re.I),
    re.compile(r"^show (?:me )?the release date and official story series for (.+?)\??$", re.I),
    re.compile(r"^is (.+?) linked to an official story series\??$", re.I),
]
_DUAL_TIMELINE_QUESTIONS = [
    re.compile(r"^compare (.+?) set release chronology with cited in-universe events\??$", re.I),
    re.compile(r"^compare (?:the )?release and lore timelines for (.+?)\??$", re.I),
]


@lru_cache(maxsize=1)
def _data():
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    release = json.loads(RELEASE_PATH.read_text(encoding="utf-8"))
    if catalog["as_of"] != release["as_of"]:
        raise ValueError("Historical Set Atlas cutoff disagrees with its acceptance record")
    return catalog, release


@lru_cache(maxsize=1)
def _story_bridge():
    bridge = json.loads(STORY_BRIDGE_PATH.read_text(encoding="utf-8"))
    catalog, _ = _data()
    if bridge["as_of"] != catalog["as_of"] or set(bridge["set_scope_records"]) != set(catalog["sets"]):
        raise ValueError("Story-series bridge and Set Atlas do not describe the same snapshot")
    return bridge


@lru_cache(maxsize=1)
def _cited_chronology_ledgers():
    paths = [ROOT / 'data/lore_research/relative_chronology_2026-10-30.json',
             ROOT / 'data/lore_research/source_event_sequences_2026-10-30.json']
    ledgers = []
    for path in paths:
        ledger = json.loads(path.read_text(encoding='utf-8'))
        if ledger.get('status') not in {'PRELIMINARY_RESEARCH', 'PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED'}:
            raise ValueError('Changed chronology research grade must be reviewed before set linkage')
        nodes = {n['id']: n['label'] for n in ledger['nodes']}
        edges = ledger['stated_edges'] if 'stated_edges' in ledger else ledger['edges']
        ledgers.append((path, ledger.get('as_of') or ledger.get('date'), nodes, edges))
    return ledgers


def _envelope(query, route, result, sources, flags=None, confidence="QUALIFIED", scope_flags=None):
    catalog, _ = _data()
    return {"route": "ask->set_atlas:" + route, "query": query, "confidence": confidence,
            "data_as_of": catalog["as_of"], "sources": sources,
            "flags": (SCOPE_FLAGS if scope_flags is None else scope_flags) + (flags or []), "result": result}


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
    matches = [code for code, meta in sets.items()
               if re.sub(r"^the\s+", "", meta["name"], flags=re.I).casefold() == name.casefold()]
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


def _answer_set_story(query, raw_set):
    """Offer only the 12 source-backed publication-title bridges, not inferred story canon."""
    code, ambiguous = _set_code(raw_set)
    catalog, _ = _data()
    if code is None:
        return _envelope(query, "set_story", {
            "requested_set": _clean_set_name(raw_set), "set": None,
            "ambiguous_set_codes": ambiguous, "official_story_series": None,
        }, [REPO_SOURCE + CATALOG_PATH.name],
            ["AMBIGUOUS_SET_NAME" if ambiguous else "UNKNOWN_SET_IN_SNAPSHOT"],
            "NOT_FOUND", STORY_SCOPE_FLAGS)

    bridge = _story_bridge()
    record = bridge["set_scope_records"][code]
    link = bridge["wizards_story_series_set_links"].get(code)
    if record["name"] != catalog["sets"][code]["name"]:
        raise ValueError("Story bridge set name conflicts with the frozen catalog")
    flags = ["SET_TO_OFFICIAL_STORY_TITLE_LINK_ONLY", "NO_IN_UNIVERSE_EVENT_ORDER_INFERRED"]
    sources = [REPO_SOURCE + CATALOG_PATH.name, REPO_SOURCE + STORY_BRIDGE_PATH.name,
               "https://scryfall.com/sets/" + code]
    if record.get("wizards_release_source"):
        sources.append(record["wizards_release_source"])
    story = None
    if link:
        if link["connection_scope"] != ("Wizards story publication titled for the named release; "
                                        "no card-lore, plot, or in-universe chronology inference"):
            raise ValueError("Unrecognized story-series citation grade")
        samples = link["sample_first_party_story_sources"]
        if (len(samples) > link["official_story_count_in_recovered_index"] or
                any(not p["url"].startswith("https://magic.wizards.com/") for p in samples)):
            raise ValueError("Unverified or impossible official story-page sample")
        story = {"official_title": link["series_name_as_published"],
                 "official_story_count_in_recovered_index": link["official_story_count_in_recovered_index"],
                 "sampled_official_story_pages": samples,
                 "sample_is_complete": len(samples) == link["official_story_count_in_recovered_index"],
                 "link_grade": "PUBLICATION_TITLE_ONLY"}
        sources.extend(p["url"] for p in samples)
        if not story["sample_is_complete"]:
            flags.append("ONLY_SAMPLE_OF_STORY_PAGES_SHOWN")
    else:
        flags.append("NO_OFFICIAL_TITLE_STORY_LINK_IN_BOUNDED_INDEX")
    return _envelope(query, "set_story", {
        "set": {"code": code, "name": record["name"],
                "scryfall_recorded_release_date": record["released_at"],
                "catalogued_set_type": record["scryfall_set_type"],
                "scope_label": record["scope_label"]},
        "official_story_series": story,
        "story_link_coverage": {"linked_series": bridge["story_series_with_primary_title_links"],
                                "total_catalogued_set_codes": bridge["all_set_codes"]},
        "limitation": ("A Scryfall set release date and a Wizards story-page publication date are "
                       "real-world dates, not dates of in-universe events. A matching official "
                       "story-series title is navigation only, not proof of a card depiction, "
                       "plot, canonical event order or comprehensive story coverage. A missing "
                       "bridge means no link in this bounded research index, not no story exists."),
    }, sorted(set(sources)), flags, scope_flags=STORY_SCOPE_FLAGS)


def _answer_dual_timeline(query, raw_set):
    """Compare real publication dates and *only exact-page cited* fictional relations."""
    env = _answer_set_story(query, raw_set)
    env['route'] = 'ask->set_atlas:dual_timeline'
    if env['confidence'] == 'NOT_FOUND':
        return env
    env['flags'] = [f for f in env['flags'] if f != 'NO_IN_UNIVERSE_EVENT_ORDER_INFERRED']
    result = env['result']
    series = result['official_story_series']
    pages = {page['url']: page for page in series['sampled_official_story_pages']} if series else {}
    relations, ledger_dates = [], {}
    for path, as_of, nodes, edges in _cited_chronology_ledgers():
        hits = [edge for edge in edges if edge.get('source_url') in pages]
        if hits:
            env['sources'].append('https://github.com/corymstover/GrokBotMTGCompanion/blob/main/'
                                  + path.relative_to(ROOT).as_posix())
            ledger_dates[path.name] = as_of
        for edge in hits:
            if (not edge.get('quote') or not re.fullmatch(r'[a-f0-9]{64}', edge.get('quote_sha256', ''))):
                raise ValueError('Cited in-universe relation lacks source-quote hash')
            relations.append({
                'ledger': path.name, 'source_url': edge['source_url'],
                'published_date': pages[edge['source_url']]['published_date'],
                'earlier_event_id': edge['earlier'], 'earlier_event': nodes[edge['earlier']],
                'later_event_id': edge['later'], 'later_event': nodes[edge['later']],
                'relation': edge['relation'], 'source_grade': edge.get('certainty') or edge.get('kind'),
                'quote': edge['quote'], 'quote_sha256': edge['quote_sha256'],
                'note': edge.get('note') or None,
            })
    relations.sort(key=lambda row: (row['source_url'], row['ledger'], row['earlier_event_id'],
                                    row['later_event_id'], row['relation']))
    result['two_chronology_axes'] = {
        'real_world_set_release': result['set']['scryfall_recorded_release_date'],
        'real_world_story_publications': [
            {'url': page['url'], 'date': page['published_date']}
            for page in (series['sampled_official_story_pages'] if series else [])],
        'in_universe_relations_on_exact_linked_pages': relations[:8],
        'cited_in_universe_relations_total': len(relations),
        'omitted_in_universe_relations': max(0, len(relations) - 8),
        'chronology_ledger_as_of': ledger_dates,
        'fictional_event_date_corresponding_to_set_release': None,
        'release_vs_fictional_event_order': 'NOT_COMPARABLE_DIFFERENT_CHRONOLOGY_AXES',
    }
    result['limitation'] += (' Only quoted event relations from the exact same cited official story '
                             'pages are joined. Source-page identity is not evidence that a release date '
                             'corresponds to an in-universe era, that all scenes are depicted on cards, '
                             'or that these sparse event relations form a complete chronology.')
    env['flags'] += ['EXACT_OFFICIAL_PAGE_TO_EVENT_SOURCE_JOIN',
                     'IN_UNIVERSE_ORDER_ONLY_FROM_CITED_QUOTES',
                     'NO_REAL_WORLD_TO_FICTIONAL_TIME_CONVERSION']
    if not relations:
        env['flags'].append('NO_CITED_IN_UNIVERSE_EVENT_ON_LINKED_SAMPLE_PAGES')
    if len(relations) > 8:
        env['flags'].append('IN_UNIVERSE_RELATIONS_SAMPLED')
    env['sources'] = sorted(set(env['sources']))
    return env


def try_answer(text):
    """Return an evidence-enveloped set answer, or None for non-set questions."""
    query = text.strip()
    if _TOTAL.fullmatch(query):
        return _answer_total(query)
    for pattern in _DUAL_TIMELINE_QUESTIONS:
        match = pattern.fullmatch(query)
        if match:
            return _answer_dual_timeline(query, match.group(1))
    for pattern in _SET_STORY_QUESTIONS:
        match = pattern.fullmatch(query)
        if match:
            return _answer_set_story(query, match.group(1))
    for pattern, mode in _SET_QUESTIONS:
        match = pattern.fullmatch(query)
        if match:
            return _answer_set(query, match.group(1), mode)
    for pattern in _CARD_QUESTIONS:
        match = pattern.fullmatch(query)
        if match:
            return _answer_card(query, match.group(1))
    return None
