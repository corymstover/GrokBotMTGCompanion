#!/usr/bin/env python3
"""Batch 13: printed-flavor lore links for cards still NO_LORE_YET in card_lore_links_2026-10-30.json.

Evidence is Wizards-printed flavor text from the pinned Scryfall Default Cards snapshot (English printings).
This is PRINTED-FLAVOR evidence, kept distinct from story claims: it shows that a card's printed text
quotes or names a graph entity, not that the card depicts a cited story event.

Rules (conservative, same spirit as L213):
- Pool: card_lore_links NO_LORE_YET cards that are not Universes Beyond (card_lore_links rule: no non-UB-marked
  printing under the card's own name). Speaker cards must be native Magic cards by the same rule.
- ATTRIBUTION: a flavor line beginning with a dash whose speaker head (text before the first comma) IS a graph
  entity name or starts with it ("Ajani Goldmane" -> Ajani). A head in italics or quotes is an in-universe work
  title (e.g. *The History of Kamigawa*): it is recorded in in_universe_work_titles, never linked as a speaker;
  entity names inside it count as MENTION_IN_WORK_TITLE, names elsewhere inside a head as MENTION. MENTION: an entity name in the flavor.
- Case-sensitive, word-boundary match; the entity name must pass the proper-name gate (a word of >=4 letters
  never seen lowercase in the English flavor corpus). A shorter name inside a longer matched name is skipped.
- Strong (FLAVOR_LINKED) only when the name is unambiguous in the graph AND (multi-word, OR a Plane entity,
  OR the card is printed in a set in the entity's footprint: sets of cards named after the entity plus the
  story sets of its origin packs). Otherwise *_NAME_ONLY (a lead; same-name identity unverified).
- SPEAKER_CARD_CHARACTER (separate tier, not a graph link): the speaker head equals the name, or the part before
  the comma of the name, of a native (non-UB) legendary Magic creature card; a single-word
  head also needs a set shared with the quoting card. Shows the printed text quotes a printed character.
"""
import argparse, collections, gzip, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LR = ROOT / "data/lore_research"
OUT = LR / "flavor_lore_links_2026-10-30.json"
BULK = ROOT / ".cache/multiverse/default-cards-20261029090546.jsonl.gz"
BULK_SHA = "008434d5"
ENTITY_TYPES = ("Character", "Concept", "Faction", "Place", "Object", "Plane", "Event")
WORD = re.compile(r"[A-Za-zÀ-ÿ0-9'\-]+")
ATTR = re.compile(r"(?m)^\s*[—―]\s*(.+?)\s*$")


def jload(p):
    return json.loads(Path(p).read_text())


def proper(name, lower):
    return any(len(w) >= 4 and w.lower() not in lower for w in WORD.findall(name))


def finditer(text, name):
    return re.finditer(r"(?<![A-Za-zÀ-ÿ0-9'])" + re.escape(name) + r"(?![A-Za-zÀ-ÿ0-9])", text)


def find(text, name):
    return re.search(r"(?<![A-Za-zÀ-ÿ0-9'])" + re.escape(name) + r"(?![A-Za-zÀ-ÿ0-9])", text)


def build():
    links = jload(LR / "card_lore_links_2026-10-30.json")
    pool = {c["oracle_id"]: c for c in links["cards"] if c["status"] == "NO_LORE_YET"}
    graph = jload(ROOT / "data/multiverse_graph/multiverse_graph.json")
    ents = [n for n in graph["nodes"] if n["type"] in ENTITY_TYPES]
    names = jload(LR / "card_name_anchors_2026-10-30.json")["anchors"]
    story_sets = jload(LR / "claim_card_anchors_2026-10-30.json")["story_sets"]
    named_cards = collections.defaultdict(set)
    for a in names:
        for c in a["cards"]:
            named_cards[a["entity"]].add(c["oracle_id"])
    leg_cards, native = {}, set()
    flav = collections.defaultdict(list)
    osets = collections.defaultdict(set)
    lower = set()
    with gzip.open(BULK, "rt") as f:
        for line in f:
            r = json.loads(line)
            if r.get("lang") != "en":
                continue
            faces = r.get("card_faces") or []
            oid = r.get("oracle_id") or (faces[0].get("oracle_id") if faces else None)
            osets[oid].add(r["set"])
            mark = r.get("security_stamp") == "triangle" or "universesbeyond" in (r.get("promo_types") or [])
            if not mark and all(n in (None, r.get("name"), f.get("name")) for f in
                    [r] + (r.get("card_faces") or []) for n in [f.get("printed_name")]):
                native.add(oid)
            tl = r.get("type_line") or (faces[0].get("type_line") if faces else "") or ""
            if "Legendary" in tl.split(" // ")[0] and "Creature" in tl.split(" // ")[0] and oid not in leg_cards:
                leg_cards[oid] = {"name": r["name"], "scryfall_uri": r.get("scryfall_uri", "").split("?")[0]}
            for t in [r.get("flavor_text")] + [x.get("flavor_text") for x in faces]:
                if not t:
                    continue
                lower.update(w for w in WORD.findall(t) if w.islower())
                if oid in pool:
                    flav[oid].append({"flavor": t, "set": r["set"], "collector_number": r["collector_number"],
                                      "scryfall_uri": r.get("scryfall_uri", "").split("?")[0]})

    by_name = collections.defaultdict(list)
    for e in ents:
        if proper(e["name"], lower):
            by_name[e["name"]].append(e)
    rejected_generic = sorted({e["name"] for e in ents if not proper(e["name"], lower)})
    footprint = {}
    for e in ents:
        short = e["id"].split(":", 1)[1]
        fp = set()
        for o in named_cards.get(short, ()):
            fp |= osets.get(o, set())
        for p in e.get("origins", []):
            fp |= set(story_sets.get(p, []))
        footprint[e["id"]] = fp
    names_by_len = sorted(by_name, key=lambda n: (-len(n), n))
    legends = collections.defaultdict(list)
    for o, lc in leg_cards.items():
        if o not in native:
            continue
        nm = lc["name"].split(" // ")[0]
        for k in {nm, nm.split(",")[0].strip()}:
            if len(k) >= 4:
                legends[k].append({"name": lc["name"], "oracle_id": o, "scryfall_uri": lc["scryfall_uri"]})
    works = collections.defaultdict(set)
    cards, counts, attrib_unmatched = [], collections.Counter(), collections.Counter()
    for oid, c in sorted(pool.items(), key=lambda kv: kv[1]["name"]):
        if c["universes_beyond"]:  # no native printing (card_lore_links rule)
            counts["excluded_universes_beyond"] += 1
            continue
        ev, seen, spk_seen = [], set(), set()
        card_sets = osets.get(oid, set())
        unmatched_here = set()
        for pr in flav.get(oid, []):
            spans = []
            for m in ATTR.finditer(pr["flavor"]):
                h = m.group(1).split(",")[0].strip()
                if h[:1] in "*\"'“‘_":
                    works[h.strip('*"\'“”‘’_ ')].add(oid)
                    spans.append(("MENTION_IN_WORK_TITLE", h, False))
                else:
                    spans.append(("ATTRIBUTION", h, True))
            spans.append(("MENTION", ATTR.sub("", pr["flavor"]), False))
            for kind, txt, is_head in spans:
                taken, hit = [], False
                for nm in names_by_len:
                    for mm in finditer(txt, nm):
                        if any(x <= mm.start() and mm.end() <= y for x, y in taken):
                            continue
                        taken.append((mm.start(), mm.end()))
                        k = kind
                        if is_head and not (txt == nm or txt.startswith(nm + " ")):
                            k = "MENTION"
                        hit = hit or k == "ATTRIBUTION"
                        for e in by_name[nm]:
                            key = (k, e["id"])
                            if key in seen:
                                continue
                            seen.add(key)
                            multi = len(WORD.findall(nm)) > 1
                            consistent = bool(card_sets & footprint[e["id"]])
                            ambiguous = len({x["id"] for x in by_name[nm]}) > 1
                            strong = (multi or e["type"] == "Plane" or consistent) and not ambiguous
                            g = "PRINTED_FLAVOR_ATTRIBUTION" if k == "ATTRIBUTION" else "PRINTED_FLAVOR_MENTION"
                            if k == "MENTION_IN_WORK_TITLE":
                                g = "PRINTED_FLAVOR_MENTION_IN_WORK_TITLE"
                            ev.append({"kind": k, "entity": e["id"], "entity_name": nm, "entity_type": e["type"],
                                       "grade": g if strong else g + "_NAME_ONLY", "multi_word_name": multi,
                                       "set_consistent": consistent, "ambiguous_name": ambiguous,
                                       "flavor_text": pr["flavor"],
                                       "printing": {q: pr[q] for q in ("set", "collector_number", "scryfall_uri")}})
                        break
                if is_head and not hit:
                    leg = legends.get(txt, [])
                    if len(WORD.findall(txt)) == 1:
                        leg = [l for l in leg if osets.get(l["oracle_id"], set()) & card_sets]
                    leg = [l for l in leg if l["oracle_id"] != oid]
                    if leg and txt not in spk_seen:
                        spk_seen.add(txt)
                        ev.append({"kind": "SPEAKER_CARD_CHARACTER", "speaker": txt,
                                   "grade": "PRINTED_FLAVOR_SPEAKER_IS_CARD_CHARACTER",
                                   "speaker_cards": [{"name": l["name"], "oracle_id": l["oracle_id"],
                                                      "scryfall_uri": l["scryfall_uri"]} for l in leg[:5]],
                                   "flavor_text": pr["flavor"],
                                   "printing": {q: pr[q] for q in ("set", "collector_number", "scryfall_uri")}})
                    elif not leg:
                        unmatched_here.add(txt)
        for t in unmatched_here:
            attrib_unmatched[t] += 1
        strong = [x for x in ev if x["kind"] != "SPEAKER_CARD_CHARACTER" and not x["grade"].endswith("_NAME_ONLY")]
        spk = [x for x in ev if x["kind"] == "SPEAKER_CARD_CHARACTER"]
        status = ("FLAVOR_LINKED" if strong else "FLAVOR_SPEAKER_CHARACTER" if spk else
                  "FLAVOR_NAME_ONLY" if ev else "NO_LORE_YET")
        counts[status] += 1
        for x in ev:
            counts["evidence_" + x["grade"]] += 1
        cards.append({"oracle_id": oid, "name": c["name"], "status": status, "has_english_flavor": oid in flav,
                      "evidence": ev})
    body = {"schema": "flavor-lore-links/v1", "status": "PRELIMINARY_RESEARCH",
            "not": "owner approved; printed-flavor evidence is distinct from story claims and never asserts a depicted event",
            "card_data_source": {"provider": "Scryfall Default Cards", "file": BULK.name, "sha256_prefix": BULK_SHA,
                                 "snapshot_id": "snap-20261029-40848334824-1"},
            "pool": {"source": "card_lore_links_2026-10-30.json status NO_LORE_YET", "cards": len(pool)},
            "rule": __doc__.split("Rules")[1].strip(),
            "counts": dict(sorted(counts.items())),
            "generic_entity_names_never_matched": rejected_generic,
            "unmatched_attribution_heads_top": dict(attrib_unmatched.most_common(40)),
            "in_universe_work_titles": {k: len(v) for k, v in sorted(works.items())},
            "cards": cards}
    body["content_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    return body


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    if not BULK.exists():
        sys.exit("pinned bulk cache absent")
    body = build(); text = json.dumps(body, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    if a.check:
        ok = OUT.exists() and OUT.read_text() == text
        print("PASS flavor lore links current" if ok else "FAIL flavor lore links stale"); sys.exit(0 if ok else 1)
    OUT.write_text(text); print("wrote", OUT.relative_to(ROOT), body["counts"])


if __name__ == "__main__":
    main()
