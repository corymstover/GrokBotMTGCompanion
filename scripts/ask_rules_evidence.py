#!/usr/bin/env python3
"""Conservative natural-language published-rulings and CR-keyword evidence surface.

No answer simulates a game, infers undocumented card interactions, or treats an
older printed ruling as proof that today's rules and Oracle text are unchanged.
"""
import re

import rules_interactions as evidence

CARD_RULINGS_AS_OF = "2026-10-15"  # committed card shard ruling text, not the newer Oracle drift date
_PAIR = [
    re.compile(r"^how (?:does|do) (.+?) interact with (.+?)\??$", re.I),
    re.compile(r"^how do (.+?) and (.+?) interact\??$", re.I),
    re.compile(r"^what (?:is|are) the (?:rules? )?interactions? between (.+?) and (.+?)\??$", re.I),
]
_SINGLE = [
    re.compile(r"^(?:what|which) (?:are the )?(?:published |official )?rulings "
               r"(?:for|on|about) (.+?)\??$", re.I),
    re.compile(r"^show(?: me)? (?:the |all )?(?:published )?rulings (?:for|on) (.+?)\??$", re.I),
    re.compile(r"^(?:what|which) (?:keyword )?mechanics (?:does|do) (.+?) have\??$", re.I),
    re.compile(r"^(?:what|which) (?:are the )?keywords (?:on|of|for) (.+?)\??$", re.I),
]
_KEYWORD = [
    re.compile(r"^what (?:is|does) (.+?) (?:mean|do)(?: in (?:mtg|magic))?\??$", re.I),
    re.compile(r"^explain (?:the )?(?:keyword )?(.+?)\??$", re.I),
]


def _sources(*names):
    # The card pages are navigational citations; the dated ruling text is read
    # from the committed Scryfall-derived shards named in each result.
    from mv_ask import card
    urls = [evidence.CR["source_url"]]
    for name in names:
        lookup = card(name)
        for url in lookup.get("sources", []):
            if url not in urls:
                urls.append(url)
    return urls


def _base(query, route, result, flags, names=(), confidence="QUALIFIED", card_evidence=True):
    return {"route": "ask->rules_evidence:" + route, "query": query,
            "confidence": confidence,
            "data_as_of": CARD_RULINGS_AS_OF if card_evidence else evidence.CR["effective"],
            "rules_effective": evidence.CR["effective"], "sources": _sources(*names),
            "flags": (["HISTORICAL_RULINGS_SHARD_NOT_LIVE"] if card_evidence else ["DATED_CR_EXCERPT_ONLY"])
            + ["NO_RULES_SIMULATION"] + flags,
            "result": result}


def _answer_single(query, name):
    rec = evidence.record(name)
    if rec is None:
        return _base(query, "card", {"requested_card": name, "rulings": [], "keywords": []},
                     ["UNKNOWN_CARD_IN_INDEX"], confidence="NOT_FOUND")
    citations = [evidence.cite_keyword(kw) for kw in rec["keywords"]]
    missing_keywords = [r["keyword"] for r in citations if r["rule"] is None]
    return _base(query, "card", {
        "card": rec["name"], "type_line": rec["type_line"], "card_shard": rec["shard"],
        "published_rulings": rec["rulings"], "published_ruling_count": len(rec["rulings"]),
        "keywords": rec["keywords"], "keyword_rules": citations,
        "limitation": "Only listed keywords and published dated rulings from the committed shard; not all card mechanics or an exhaustive interaction analysis."
    }, (["NO_PUBLISHED_RULING_IN_SHARD"] if not rec["rulings"] else []) +
       (["NO_MATCHING_CR_701_702_SECTION"] if missing_keywords else []), (rec["name"],))


def _answer_pair(query, left, right):
    pair = evidence.pair(left, right)
    if pair["confidence"] == "NOT_FOUND":
        return _base(query, "interaction", pair["result"], pair["flags"], confidence="NOT_FOUND")
    return _base(query, "interaction", {**pair["result"],
                  "limitation": pair["limitation"],
                  "rules_source_sha256": pair["rules_source"]["source_sha256"]},
                 pair["flags"], (left, right))


def _answer_keyword(query, kw):
    citation = evidence.cite_keyword(kw)
    if citation["rule"] is None:
        return None  # Do not steal general card names or unsupported mechanic questions.
    return _base(query, "keyword", {"keyword": kw, "comprehensive_rules": citation,
                                   "limitation": "Verbatim sections of the 2026-09-25 CR 701/702 excerpt; not a ruling on a particular card."},
                 ["CR_KEYWORD_EXCERPT_ONLY"], card_evidence=False)


def try_answer(text):
    query = text.strip()
    for pattern in _PAIR:
        match = pattern.fullmatch(query)
        if match:
            return _answer_pair(query, match.group(1), match.group(2))
    for pattern in _SINGLE:
        match = pattern.fullmatch(query)
        if match:
            return _answer_single(query, match.group(1))
    for pattern in _KEYWORD:
        match = pattern.fullmatch(query)
        if match:
            answer = _answer_keyword(query, match.group(1))
            if answer is not None:
                return answer
    return None
