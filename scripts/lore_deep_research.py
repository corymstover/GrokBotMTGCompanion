#!/usr/bin/env python3
"""Evidence-first character research over *all* English paper printings.

Unlike the quick literal `candidates` search, this deliberately inspects every
printing, expands a character through *documented* aliases/associated figures,
groups alternate flavor texts with exact editions, and shows what an existing
deck missed. A quote is evidence that a card *mentions* someone, never automatic
proof that its art depicts a particular event. No network or paid API is used.
"""

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PROFILES = ROOT / "data" / "lore_research" / "profiles"
DEFAULT_LORE_INDEX = ROOT / "data" / "lore_entries.json"
# Parody and noncanonical joke expansions do not provide ordinary continuity
# evidence. They remain accessible with the explicit --include-parody override.
PARODY_SETS = frozenset({"ugl", "unh", "ust", "unf", "und", "unk", "sunf", "cmb1", "cmb2", "mb2"})
WEIGHTS = {
    ("subject", "printed_flavor"): 125,
    ("subject", "saga_chapter"): 120,
    ("subject", "card_name"): 105,
    ("associated_character", "printed_flavor"): 90,
    ("associated_character", "saga_chapter"): 88,
    ("associated_character", "card_name"): 65,
    ("theme", "printed_flavor"): 45,
    ("theme", "saga_chapter"): 43,
    ("theme", "card_name"): 25,
    # A documented editorial connection is useful, but a literal, edition-
    # specific named quote must outrank an association supplied by a researcher.
    ("curated", "exact_printing"): 85,
    ("editorial", "index_card_link"): 70,
}


def _manifest(archive):
    return json.loads((archive / "manifest.json").read_text(encoding="utf-8"))


def printings(archive, manifest):
    for shard in sorted(manifest["shards"]):
        with (archive / shard).open(encoding="utf-8") as handle:
            for line in handle:
                row = json.loads(line)
                if row.get("l") == "en" and row.get("p"):
                    yield row


def _rx(term):
    if not term.strip():
        raise ValueError("empty profile search term")
    return re.compile(r"(?<![\w])" + re.escape(term.strip()) + r"(?![\w])", re.I)


def _slug(subject):
    return re.sub(r"[^a-z0-9]+", "-", subject.casefold()).strip("-")


def profile(subject, directory=DEFAULT_PROFILES):
    if not subject.strip():
        raise ValueError("subject must not be blank")
    path = directory / (_slug(subject) + ".json")
    if path.is_file():
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("subject", "").casefold() != subject.casefold():
            raise ValueError("profile subject does not match requested subject")
        if not isinstance(data.get("signals"), list) or not isinstance(data.get("pinned_printings", []), list):
            raise ValueError("malformed lore research profile")
        data["profile_used"] = True
    else:
        data = {"subject": subject, "signals": [{"term": subject, "relation": "subject", "phase": "unspecified"}],
                "pinned_printings": [], "reading_sources": [], "profile_used": False}
    for signal in data["signals"]:
        if signal.get("relation") not in ("subject", "associated_character", "theme"):
            raise ValueError(f"unsupported evidence relation {signal.get('relation')}")
        _rx(signal.get("term", ""))
    for pin in data["pinned_printings"]:
        if not all(pin.get(k) for k in ("card", "set", "collector", "reason", "phase")):
            raise ValueError("pinned printings require card, set, collector, reason and phase")
    return data


def _edition(row, flavor="", face=0):
    return {"set": row["s"], "collector": row["c"], "date": row.get("r"),
            "url": row.get("url"), "face": face, "printed_flavor": flavor,
            "printing_id": row["id"]}


def _ordered_edition(row):
    return (row.get("date") or "", row["set"], row["collector"], row.get("face", 0))


def variants(name, archive, *, limit=30):
    """Edition/collector numbers for *each different* actual printed flavor.

    An empty-flavor variant is included because art-only or unflavored editions
    must never be presented as carrying a quote from a different edition.
    """
    if not name.strip() or limit < 0:
        raise ValueError("card name must be nonempty and limit nonnegative")
    man = _manifest(archive)
    editions, groups = [], defaultdict(list)
    for row in printings(archive, man):
        face_names = [f.get("n", "") for f in row.get("faces", [])]
        if name.casefold() not in [row["n"].casefold()] + [n.casefold() for n in face_names]:
            continue
        for i, face in enumerate(row.get("faces", []) or [{}]):
            flavor = face.get("f", "")
            ed = _edition(row, flavor, i)
            editions.append(ed)
            groups[flavor].append(ed)
    if not editions:
        raise ValueError(f"card not found in English paper printings: {name}")
    values = sorted(groups.items(), key=lambda x: (not bool(x[0]), min(_ordered_edition(e) for e in x[1])))
    flavor_variants = [{"flavor_text": flavor, "count": len(editions_for_flavor),
                        "exact_printings": sorted(editions_for_flavor, key=_ordered_edition)}
                       for flavor, editions_for_flavor in values]
    return {"card": name, "total_english_paper_printing_faces": len(editions),
            "distinct_flavor_variants_including_blank": len(groups), "shown_variants": min(limit, len(groups)),
            "flavor_variants": flavor_variants[:limit], "truncated": len(groups) > limit,
            "source": man.get("source"), "coverage": man.get("coverage"),
            "interpretation": "Text belongs only to listed editions; a flavor quote alone does not certify an event or artwork."}


def parse_decklist(path):
    """Import Archidekt-style '1x Name' lines, preserving singleton names."""
    included = set()
    slots = 0
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"(\d+)\s*x\s+(.+)", line, re.I)
        if not match:
            raise ValueError(f"unsupported decklist entry at line {lineno}: {line[:80]}")
        quantity, name = int(match.group(1)), match.group(2).strip()
        name = re.sub(r"\s+\[Commander\]$", "", name, flags=re.I)
        if quantity < 1 or not name:
            raise ValueError(f"bad quantity or name at line {lineno}")
        included.add(name.casefold())
        slots += quantity
    return included, slots


def index_cards(subject, path=DEFAULT_LORE_INDEX):
    """Reuse already indexed character/dossier card links with provenance.

    Links are editorial context, not literal quotes, art proof or chronology.
    Their weight must remain strictly below a named character in a printing.
    """
    if not path.is_file():
        return {}, []
    entries = json.loads(path.read_text(encoding="utf-8")).get("items", [])
    matching = [e for e in entries if e.get("kind") in ("character", "dossier") and
                (e.get("name", "").casefold() == subject.casefold() or
                 e.get("name", "").casefold().startswith(subject.casefold() + " "))]
    linked = defaultdict(list)
    contexts = []
    for e in matching:
        ref = f"{e['page']}#{e['anchor']}"
        contexts.append({"entry": e.get("name"), "kind": e.get("kind"), "reference": ref,
                         "related_lore_links": e.get("links", {})})
        for name in e.get("enriched_cards", []):
            linked[name.casefold()].append(ref)
    return linked, contexts


def deep_research(subject, archive, *, decklist=None, profile_dir=DEFAULT_PROFILES,
                  limit=50, max_variants=5, include_parody=False, index_path=DEFAULT_LORE_INDEX):
    if limit < 0 or max_variants < 0:
        raise ValueError("limits must be nonnegative")
    p = profile(subject, profile_dir)
    man = _manifest(archive)
    signals = [(s, _rx(s["term"])) for s in p["signals"]]
    pins = defaultdict(list)
    for pin in p["pinned_printings"]:
        pins[pin["card"].casefold()].append(pin)
    linked_cards, linked_context = index_cards(subject, index_path)
    results = {}

    def record(name, evidence, ed):
        key = name.casefold()
        item = results.setdefault(key, {"card": name, "score": 0, "evidence": [],
                                        "best_printing": None, "phase": "unspecified"})
        # Exact printing is important; never infer that every edition carries the same flavor.
        ekey = (evidence["relation"], evidence["field"], evidence["term"], ed["set"], ed["collector"], ed["face"])
        if ekey not in item.setdefault("_keys", set()):
            item["_keys"].add(ekey)
            item["evidence"].append({**evidence, "printing": ed})
        if evidence["field"] == "exact_printing":
            item["_curated_phase"] = evidence["phase"]
        score = evidence["score"]
        if score > item["score"] or (score == item["score"] and (not item["best_printing"] or _ordered_edition(ed) < _ordered_edition(item["best_printing"]))):
            item["score"] = score
            item["best_printing"] = ed
            item["phase"] = evidence["phase"]

    for row in printings(archive, man):
        if not include_parody and row["s"].casefold() in PARODY_SETS:
            continue
        name = row["n"]
        for source in linked_cards.get(name.casefold(), []):
            record(name, {"relation": "editorial", "field": "index_card_link", "term": subject,
                          "phase": "linked lore entry — chronology unverified",
                          "score": WEIGHTS[("editorial", "index_card_link")],
                          "source": source, "reason": "existing character/dossier card enrichment",
                          "qualification": "editorial link; neither literal quote nor direct event proof"},
                   _edition(row, (row.get("faces") or [{}])[0].get("f", "")))
        for pin in pins.get(name.casefold(), []):
            if row["s"].casefold() == pin["set"].casefold() and str(row["c"]) == str(pin["collector"]):
                fl = (row.get("faces") or [{}])[0].get("f", "")
                record(name, {"relation": "curated", "field": "exact_printing", "term": name,
                              "phase": pin["phase"], "score": WEIGHTS[("curated", "exact_printing")],
                              "reason": pin["reason"], "source": pin.get("source"),
                              "qualification": "curated association requires review of linked evidence"}, _edition(row, fl))
        for i, face in enumerate(row.get("faces", []) or [{}]):
            for signal, rx in signals:
                for field, value in (("printed_flavor", face.get("f", "")),
                                     ("saga_chapter", face.get("chapters", "")),
                                     ("card_name", name + " " + face.get("n", ""))):
                    if not value or not rx.search(value):
                        continue
                    relation = signal["relation"]
                    record(name, {"relation": relation, "field": field, "term": signal["term"],
                                  "phase": signal.get("phase", "unspecified"), "score": WEIGHTS[(relation, field)],
                                  "reason": signal.get("reason", ""), "source": signal.get("source"),
                                  "qualification": "literal textual match; association/depiction is not independently proved"},
                           _edition(row, face.get("f", ""), i))

    # A second pass gives *all* alternate printings of discovered cards, not just
    # the first N matches and not just editions containing the search words.
    variants_by_card = defaultdict(lambda: defaultdict(list))
    if results:
        for row in printings(archive, man):
            if not include_parody and row["s"].casefold() in PARODY_SETS:
                continue
            key = row["n"].casefold()
            if key not in results:
                continue
            for i, face in enumerate(row.get("faces", []) or [{}]):
                variants_by_card[key][face.get("f", "")].append(_edition(row, face.get("f", ""), i))

    items = []
    for key, item in results.items():
        if item.get("_curated_phase"):
            item["phase"] = item.pop("_curated_phase")
        families = variants_by_card[key]
        def flavor_relevance(flavor):
            return max((WEIGHTS[(s["relation"], "printed_flavor")] for s, rx in signals
                        if flavor and rx.search(flavor)), default=0)

        # In the subject-specific deep view, a later quote naming the subject
        # must not be lost behind five older, less relevant generic printings.
        choices = sorted(families.items(), key=lambda x: (-flavor_relevance(x[0]),
                         not bool(x[0]), min(_ordered_edition(e) for e in x[1])))
        item["flavor_variant_count_including_blank"] = len(choices)
        item["flavor_variants"] = [{"text": flav, "example_exact_printing": min(eds, key=_ordered_edition),
                                    "printing_count": len(eds), "quote_relevance_score": flavor_relevance(flav)}
                                   for flav, eds in choices[:max_variants]]
        item["flavor_variants_truncated"] = len(choices) > max_variants
        item["evidence"].sort(key=lambda x: (-x["score"], _ordered_edition(x["printing"])))
        # Bound repeated quote evidence from duplicate promo/reprint editions.
        item["evidence_count"] = len(item["evidence"])
        selected = item["evidence"][:5]
        pin = next((e for e in item["evidence"] if e["field"] == "exact_printing"), None)
        if pin is not None and pin not in selected:
            selected.append(pin)
        item["evidence"] = selected
        del item["_keys"]
        items.append(item)
    items.sort(key=lambda x: (-x["score"], x["card"].casefold()))
    count = len(items)
    included, slots = parse_decklist(decklist) if decklist else (set(), 0)
    excluded = [it for it in items if it["card"].casefold() not in included]
    by_phase = defaultdict(lambda: {"discovered": 0, "in_deck": 0, "missing": 0})
    for it in items:
        phase = it["phase"]
        by_phase[phase]["discovered"] += 1
        by_phase[phase]["in_deck" if it["card"].casefold() in included else "missing"] += 1
    return {"subject": subject, "profile_used": p["profile_used"],
            "linked_lore_entries": linked_context,
            "subject_signals": p["signals"], "reading_sources": p.get("reading_sources", []),
            "source_snapshot": man.get("source"), "source_sha256": man.get("source_sha256"),
            "total_evidence_candidates": count, "decklist_compared": str(decklist) if decklist else None,
            "decklist_slots": slots if decklist else None, "total_not_in_deck": len(excluded) if decklist else None,
            "coverage_by_phase": dict(sorted(by_phase.items())),
            "parody_sets_excluded": [] if include_parody else sorted(PARODY_SETS),
            "shown": min(limit, len(excluded if decklist else items)),
            "candidates": (excluded if decklist else items)[:limit],
            "interpretation": "Discovery and gap auditing only: printed mention, title, and curated association are distinct tiers. Verify chronology, art, and actual canon before choosing cards."}
