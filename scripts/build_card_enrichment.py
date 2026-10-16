#!/usr/bin/env python3
"""Card-level lore & synergy enrichment (Bot cycle 33, Phase 8: issues #99–#103).

Writes data/card_enrichment.json and, for each enriched card, two lines in its card-shard entry:
  - **Lore:**     how the card relates to existing lore entries (lore_lib.ENTRY_PAGES) and the official evidence
  - **Synergy:**  *Proven* data (KB decks that run it, Commander Spellbook combos, EDHREC co-occurrence) and
                  *Guidance* (EDH Packages sub-packages its Oracle text matches)
The lines are stored pre-rendered in the JSON. scripts/ingest_scryfall.py renders them in every entry it writes, so
a re-import keeps them; this script patches the shards in between imports. Nothing here is a new fact: every item
is a pointer to an existing KB entry, a Scryfall field, a cached official page, or a cited third-party dataset.

Lore relations (one per lore entry):
  depicts     the entry's own text links the card and the card is that character / item (name parts match)
  featured    the entry's own text links the card in another context (a plane's notable cards, an arc beat, …)
  name-match  only a name match (the generated "Character cards (name-matched)" tables): not a canon claim ⚠️
Evidence: official URLs on the entry line that links the card (else the entry's own citations, marked "via entry");
Scryfall Story Spotlight printings (Wizards marks these cards as depicting a story moment); printed flavor text found
verbatim in a cached official page (.cache/story/); curated notes (data/card_lore_notes.json, each with official
sources; quotes verified by scripts/lore_quotes.py rules). 🚫 marks Universes Beyond printings (triangle stamp).

Priority pool (Phase 8 order): entry-linked cards · name-matched character cards · legendary creatures ·
planeswalkers · story-flavor cards (Story Spotlight, or flavor text quoted on a cached official page).
Batches: BATCHES below; one per Bot cycle.

  python3 scripts/build_card_enrichment.py --fetch   also fetch missing EDHREC / Spellbook data (polite, 1 s apart)
  python3 scripts/build_card_enrichment.py           rebuild from caches (missing caches → carry the stored data)
  python3 scripts/build_card_enrichment.py --check   exit 1 if stale, or on a citation / tier / reciprocity problem
"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import csv
import glob
import gzip
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote as urlq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402
import lore_lib as L  # noqa: E402

ROOT = L.ROOT
OUT = ROOT / "data" / "card_enrichment.json"
NOTES = ROOT / "data" / "card_lore_notes.json"
PAGE = ROOT / "Card Enrichment.md"
EDH = ROOT / ".cache" / "edhrec"
CSB = ROOT / ".cache" / "spellbook"
ISS = "https://github.com/corymstover/GrokBotMTGCompanion/issues/"
LORE_P, SYN_P = "- **Lore:**", "- **Synergy:**"
UA = {"User-Agent": "GrokBotMTGCompanion/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion; card enrichment)"}
KIND = {"dossier": "Dossier", "character": "Character", "plane": "Plane", "item": "Item", "arc": "Arc",
        "summary": "Arc summary", "era": "Era", "retcon": "Retcon"}
RELATIONS = ("depicts", "featured", "name-match")
NOTE_RELATIONS = ("depicts", "references", "echoes")
TIERS = ("proven", "guidance")
CHAR_PAGES = ("Characters Index.md", "Planeswalker Dossiers.md")


def front(name):
    return name.split(" // ")[0]


def face_types(c):
    return [f.get("type_line", "") for f in (c.get("card_faces") or [c])] if c.get("card_faces") else [c.get("type_line", "")]


def is_legend_or_pw(c):
    t = " ".join(face_types(c))
    return "Legendary" in t or "Planeswalker" in t


def type_group(c):
    t = " // ".join(face_types(c))
    f = face_types(c)[0]
    if "Planeswalker" in f:
        return "planeswalker"
    if "Legendary" in f and "Creature" in f:
        return "legendary creature"
    if "Legendary" in f and "Artifact" in f:
        return "legendary artifact"
    if "Legendary" in f and "Land" in f:
        return "legendary land"
    if "Legendary" in f:
        return "other legendary"
    if "Planeswalker" in t:
        return "planeswalker"
    if "Legendary Creature" in t:
        return "legendary creature"
    for k in ("Creature", "Instant", "Sorcery", "Artifact", "Enchantment", "Land", "Battle"):
        if k in f.split("—")[0]:
            return k.lower()
    return "other"


NO_LORE = "❓ No lore entry or official story evidence linked yet (synergy batch; not a claim that the card has no story)"
# Bot cycle 35 is enriched in slices of ~250 cards (checkpoint pushed after each): PW35 adds every remaining planeswalker,
# RANK35 the legendary creatures up to that EDHREC rank (2026-10-15 bulk). 6,915 = the 1,000th not-yet-enriched one.
PW35 = True
RANK35 = 6915
# Bot cycle 36: the remaining legendary creatures by EDHREC rank (same bulk) in ~250-card slices; UNRANKED36 then adds
# the ones with no EDHREC rank (not Commander-legal or too new to rank).
RANK36 = 8205
UNRANKED36 = False
BATCHES = [(33, "legendary cards and planeswalkers already linked from lore entries",
            lambda c, tiers: "entry-linked" in tiers and is_legend_or_pw(c)),
           (34, "every other lore-entry-linked card, every name-matched character card, every story-flavor card",
            lambda c, tiers: bool(tiers & {"entry-linked", "character-card", "story-flavor"})),
           (35, (("every remaining planeswalker; " if PW35 else "") + f"legendary creatures with EDHREC rank ≤ {RANK35:,} (2026-10-15 bulk)"),
            lambda c, tiers: (PW35 and "planeswalker" in tiers) or ("legendary-creature" in tiers and (c.get("edhrec_rank") or 10**9) <= RANK35)),
           (36, f"remaining legendary creatures with EDHREC rank ≤ {RANK36:,}" + (", then those with no EDHREC rank" if UNRANKED36 else "") + " (2026-10-15 bulk)",
            lambda c, tiers: "legendary-creature" in tiers and ((c.get("edhrec_rank") or 10**9) <= RANK36 or (UNRANKED36 and not c.get("edhrec_rank"))))]


# ------------------------------------------------------------------ inputs
def esc(p):
    return urlq(p, safe="/#")


def card_href(r):
    return f"../../{r['shard']}#{r['anchor']}"


def load_bulk():
    cards, bulk = ing.get_bulk(ing.DEFAULT_CACHE, None)
    return {c["oracle_id"]: c for c in cards}, bulk


def load_printings(want=None):
    """{oracle_id: {"spotlight": [...], "flavors": [...], "ub": bool, "sets": [...]}} from default-cards (paper printings)."""
    out = defaultdict(lambda: {"spotlight": [], "flavors": [], "stamps": set(), "sets": [], "artists": set(), "set_types": set()})
    f = sorted(glob.glob(str(ROOT / ".cache" / "default-cards-*.jsonl.gz")))[-1]
    with gzip.open(f, "rt", encoding="utf-8") as fh:
        for line in fh:
            c = json.loads(line)
            oid = c.get("oracle_id") or ((c.get("card_faces") or [{}])[0].get("oracle_id"))
            if not oid or (want is not None and oid not in want) or c.get("digital"):
                continue
            o = out[oid]
            tag = f"{c['set'].upper()} #{c['collector_number']}"
            if c.get("story_spotlight"):
                o["spotlight"].append(tag)
            for fc in (c.get("card_faces") or [c]):
                ft = fc.get("flavor_text") or (c.get("flavor_text") if fc is not c else None)
                if ft and ft not in o["flavors"]:
                    o["flavors"].append(ft)
            o["stamps"].add(c.get("security_stamp") or "")
            for fc in (c.get("card_faces") or [c]):
                if fc.get("artist") or c.get("artist"):
                    o["artists"].add(fc.get("artist") or c.get("artist"))
            o["sets"].append((c.get("released_at", ""), c["set"].upper()))
            o["set_types"].add(c.get("set_type", ""))
    return out


def entry_links():
    """{(shard, anchor): [{key, kind, name, sources, via}]} from the hand-written text of every lore entry."""
    out = defaultdict(list)
    for e in L.all_entries():
        key = f"{e['page']}#{e['anchor']}"
        ent_urls = L.official_urls(e["text"])
        seen = set()
        for line in e["text"].split("\n"):
            for dest, frag in L.links(line, e["page"]):
                if not dest.startswith("cards/") or (dest, frag) in seen:
                    continue
                seen.add((dest, frag))
                urls = L.official_urls(line)
                fl = [f for f in ("⚠️", "❓", "🚫") if f in line]
                out[(dest, frag)].append({"key": key, "kind": e["kind"], "name": e["name"], "line_flags": fl,
                                          "sources": urls[:3] or ent_urls[:2], "via": "line" if urls else "entry"})
    return out


def charcard_links():
    """{(shard, anchor): [entry key]} from the generated name-matched character-card tables."""
    out = defaultdict(list)
    keys = {f"{e['page']}#{e['anchor']}": e for e in L.all_entries()}
    for page in CHAR_PAGES:
        t = (ROOT / page).read_text(encoding="utf-8")
        blk = t[t.find("<!-- CHARCARDS:START -->"):t.find("<!-- CHARCARDS:END -->")]
        for row in blk.splitlines():
            m = re.match(r"^\| \[[^\]]+\]\(#([^)]+)\) \| (.*?) \|", row)
            if not m:
                continue
            k = f"{page}#{m.group(1)}"
            if k not in keys:
                continue
            for dest, frag in L.links(m.group(2), page):
                if dest.startswith("cards/") and k not in out[(dest, frag)]:
                    out[(dest, frag)].append(k)
    return out, keys


def art_captions():
    """{card name: [(title, url, artist)]} — card art captioned on cached official story pages (data/story_art_captions.csv,
    harvested by scripts/build_art_flavor.py). Used only when the caption artist matches a printing's artist (same rule as
    Art & Flavor Story Links)."""
    out = defaultdict(list)
    for r in csv.DictReader((ROOT / "data" / "story_art_captions.csv").open(encoding="utf-8")):
        t = (r.get("title") or "").split(" | ")[0].strip() or "official story page"
        if r["url"].startswith("https://magic.wizards.com/en/news/") or r["url"].startswith("https://magic.wizards.com/en/story"):
            out[r["caption_name"]].append((t, r["url"], r["caption_artist"]))
    return out


AF_PAGE = "Art & Flavor Story Links.md"


def art_flavor_sections():
    """{(shard, anchor): (section anchor, section title)} for Story Spotlight rows on Art & Flavor Story Links."""
    out = {}
    sec = None
    seen = Counter()
    for line in (ROOT / AF_PAGE).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(#{2,4}) (.+)$", line)
        if m:
            a = L.anchor(m.group(2))
            a2 = f"{a}-{seen[a]}" if seen[a] else a
            seen[a] += 1
            sec = (a2, m.group(2)) if len(m.group(1)) == 3 else (None if len(m.group(1)) == 2 else sec)
            continue
        if sec and line.startswith("| ["):
            first = line.split(" | ")[0]
            for dest, frag in L.links(first, AF_PAGE):
                if dest.startswith("cards/"):
                    out.setdefault((dest, frag), sec)
    return out


def names_match(entry_name, card_name):
    import build_lore_xrefs as X
    cn = front(card_name)
    for n in X.split_names(entry_name):
        n = re.sub(r"^(the|a|an) ", "", n, flags=re.I).strip()
        if len(n) >= 3 and re.search(rf"(?<![\w-]){re.escape(n)}(?![\w-])", cn, re.I):
            return True
    return False


def deck_index():
    import build_crossrefs as bx
    out = defaultdict(list)
    for d in ("decks", "grixis/decks"):
        for p in sorted((ROOT / d).glob("*.md")):
            rel = str(p.relative_to(ROOT))
            lab = bx.deck_label(rel, bx.meta_of(p))
            for n in set(bx.deck_cards(p)):
                out[n].append((lab, rel))
    return out


def story_norm():
    import lore_quotes as Q
    return Q.story(), Q.norm


# ------------------------------------------------------------------ third-party data (cached, polite)
def slug(name):
    n = unicodedata.normalize("NFKD", front(name)).encode("ascii", "ignore").decode().lower()
    n = re.sub(r"[^a-z0-9 -]", "", n)
    return re.sub(r"[ ]+", "-", n.strip())


def get_json(url, path, fetch):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    if not fetch:
        return None
    return _download(url, path)


def _download(url, path):
    """One polite request; a 404 (or EDHREC's 403 for a missing page) is cached as a miss, other errors
    are not cached (retried on the next run).  An EDHREC `{"redirect": "/cards/<slug>"}` stub (split
    cards are filed under both halves' names) is followed once (Bot cycle 34)."""
    try:
        d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
        if isinstance(d, dict) and isinstance(d.get("redirect"), str) and "json.edhrec.com" in url:
            time.sleep(1.0)
            d = json.loads(urllib.request.urlopen(urllib.request.Request(
                "https://json.edhrec.com/pages" + d["redirect"] + ".json", headers=UA), timeout=60).read())
    except urllib.error.HTTPError as ex:
        if not (ex.code == 404 or (ex.code == 403 and "json.edhrec.com" in url)):
            return None
        d = {"_error": f"HTTP {ex.code}"}
    except Exception:  # noqa: BLE001 — network trouble: leave uncached
        return None
    path.write_text(json.dumps(d), encoding="utf-8")
    return d


def urls_for(name, can_command):
    q = urllib.parse.quote(f'card="{name}"')
    out = [("spellbook", f"https://backend.commanderspellbook.com/variants/?q={q}&ordering=-popularity&limit=100", CSB / f"card__{slug(name)}.json"),
           ("edhrec", f"https://json.edhrec.com/pages/cards/{slug(name)}.json", EDH / f"cards__{slug(name)}.json")]
    if can_command:
        out.append(("edhrec", f"https://json.edhrec.com/pages/commanders/{slug(name)}.json", EDH / f"commanders__{slug(name)}.json"))
    return out


def prefetch(cards, delay=1.0):
    """Fetch missing EDHREC / Spellbook pages: one worker per host (the two hosts in parallel), `delay` s between requests."""
    import threading
    jobs = defaultdict(list)
    for c in cards:
        for host, u, pth in urls_for(c["name"], ing.commander_eligibility(c).startswith("Yes")):
            if not pth.exists() and (u, pth) not in jobs[host]:
                jobs[host].append((u, pth))
    done = Counter()

    def work(host):
        for u, pth in jobs[host]:
            ok = _download(u, pth)
            done[host + (" ok" if ok is not None else " failed")] += 1
            if done[host + " ok"] % 200 == 0:
                print(f"  {host}: {done[host + ' ok']}/{len(jobs[host])}", flush=True)
            time.sleep(delay)
    th = [threading.Thread(target=work, args=(h,)) for h in jobs]
    for t in th:
        t.start()
    for t in th:
        t.join()
    print("prefetch:", {h: len(v) for h, v in jobs.items()}, dict(done), flush=True)


def spellbook(name, fetch):
    q = urllib.parse.quote(f'card="{name}"')
    d = get_json(f"https://backend.commanderspellbook.com/variants/?q={q}&ordering=-popularity&limit=100",
                 CSB / f"card__{slug(name)}.json", fetch)
    if d is None:
        return None
    if d.get("_error"):
        return {"error": d["_error"]}
    res = [r for r in d.get("results", []) if (r.get("legalities") or {}).get("commander")]
    top = []
    for r in res[:3]:
        top.append({"id": r["id"], "cards": [u["card"]["name"] for u in r["uses"]],
                    "produces": [p["feature"]["name"] for p in r["produces"]][:2], "popularity": r.get("popularity") or 0})
    return {"count": len(res), "capped": bool(d.get("next")), "top": top}


def edhrec_card(name, fetch):
    d = get_json(f"https://json.edhrec.com/pages/cards/{slug(name)}.json", EDH / f"cards__{slug(name)}.json", fetch)
    if d is None:
        return None
    if d.get("_error") or "container" not in d:
        return {"error": d.get("_error", "no page")}
    jd = d["container"]["json_dict"]
    card = jd.get("card") or {}
    tops = []
    for cl in jd.get("cardlists", []):
        if cl.get("tag") == "topcommanders":
            for v in cl.get("cardviews", []):
                if v.get("name") != name and v.get("potential_decks"):
                    tops.append({"name": v["name"], "decks": v["num_decks"], "pct": round(100 * v["num_decks"] / v["potential_decks"], 1)})
    tops.sort(key=lambda x: -x["decks"])
    return {"decks": card.get("num_decks"), "potential": card.get("potential_decks"), "top_commanders": tops[:3]}


def edhrec_commander(name, fetch):
    d = get_json(f"https://json.edhrec.com/pages/commanders/{slug(name)}.json", EDH / f"commanders__{slug(name)}.json", fetch)
    if d is None:
        return None
    if d.get("_error") or "container" not in d:
        return {"error": d.get("_error", "no page")}
    jd = d["container"]["json_dict"]
    best = {}
    for cl in jd.get("cardlists", []):
        if cl.get("tag") in ("newcards", "topcommanders", "newcommanders"):
            continue
        for v in cl.get("cardviews", []):
            if v.get("synergy") is not None and v.get("potential_decks"):
                best.setdefault(v["name"], {"name": v["name"], "synergy": round(100 * v["synergy"]),
                                            "pct": round(100 * v["num_decks"] / v["potential_decks"], 1)})
    top = sorted(best.values(), key=lambda x: (-x["synergy"], x["name"]))[:3]
    return {"decks": (jd.get("card") or {}).get("num_decks"), "top_synergy": top}


# ------------------------------------------------------------------ build
def pool(rows_by_key, by_id, prints, links, cc, caps, prev=None):
    S, norm = story_norm()
    big = "\n".join(S.values())
    sh = set()
    for txt in S.values():
        w = txt.split()
        for i in range(len(w) - 5):
            sh.add(hash(" ".join(w[i:i + 6])))
    tiers = defaultdict(set)
    for r in rows_by_key.values():
        oid = r["oracle_id"]
        c = by_id.get(oid)
        if not c:
            continue
        k = (r["shard"], r["anchor"])
        if k in links:
            tiers[oid].add("entry-linked")
        if k in cc:
            tiers[oid].add("character-card")
        ft = face_types(c)[0]
        if "Planeswalker" in " ".join(face_types(c)):
            tiers[oid].add("planeswalker")
        elif "Legendary" in ft and "Creature" in ft:
            tiers[oid].add("legendary-creature")
        p = prints.get(oid)
        cn = c["name"] if c["name"] in caps else front(c["name"])
        if p and p["spotlight"]:
            tiers[oid].add("story-flavor")
        elif p and any(a in p["artists"] for _, _, a in caps.get(cn, [])):
            tiers[oid].add("story-flavor")
        elif p:
            for fl in p["flavors"]:
                w = norm(fl).split()
                if len(w) >= 8 and hash(" ".join(w[:6])) in sh and norm(fl).strip(" .'\"-") in big:
                    tiers[oid].add("story-flavor")
                    break
        if not S and (prev or {}).get(oid, {}).get("lore", {}).get("flavor_on"):
            tiers[oid].add("story-flavor")  # no story cache: keep the earlier verified flavor match
    return tiers


# ------------------------------------------------------------------ official "Legends of …" / Story Spotlight pages (Bot cycle 36)
_EXTRA = None


def extra_pages():
    """{url: {"title", "lines" (normalized text lines), "kind"}} from .cache/story/extra/ (scripts/fetch_story_pages.py,
    data/story_extra_sources.csv). These articles give each legend a heading line (the card name) and a backstory."""
    global _EXTRA
    if _EXTRA is None:
        import lore_quotes as Q
        _EXTRA = {}
        kinds = {r["url"].rstrip("/"): r["kind"] for r in csv.DictReader((ROOT / "data" / "story_extra_sources.csv").open(encoding="utf-8"))} \
            if (ROOT / "data" / "story_extra_sources.csv").exists() else {}
        for f in sorted((ROOT / ".cache" / "story" / "extra").glob("*.txt")):
            t = f.read_text(encoding="utf-8")
            head, _, body = t.partition("\n\n")
            url = head.split("\n", 1)[0][4:].strip().rstrip("/")
            title = re.sub(r"\s*\|\s*MAGIC: THE GATHERING\s*$", "", (re.search(r"^TITLE: (.*)$", head, re.M) or [None, ""])[1], flags=re.I)
            _EXTRA[url] = {"title": title.strip(), "kind": kinds.get(url, "legends"),
                           "lines": {Q.norm(l).strip(" .") for l in body.splitlines() if l.strip()}, "text": Q.norm(body)}
    return _EXTRA


def presented_on(card_name, norm):
    """Official pages whose own heading line is the card's (front-face) name: [[title, url, kind]]."""
    fr = norm(front(card_name)).strip(" .")
    if len(fr.split()) < 2:
        return []
    return [[v["title"], u, v["kind"]] for u, v in sorted(extra_pages().items()) if fr in v["lines"]]


# ------------------------------------------------------------------ name-match audit (Bot cycle 35, #100)
OFFICIAL_URL = re.compile(r"https?://magic\.wizards\.com/en/[^\s)\]>\"]+")


def char_names(entry_name, card_name):
    """The character name(s) of a (possibly grouped) entry that the card's name starts with, plus first-name keys."""
    import build_crossrefs as bx
    import build_lore_xrefs as X
    fr = front(card_name)
    out = []
    for n in X.split_names(entry_name):
        keys = [n]
        first = n.split()[0]
        if " " in n and first not in bx.STOP_FIRST and len(first) >= 3:
            keys.append(first)
        if any(fr == k or fr.startswith(k + ",") or fr.startswith(k + " ") for k in keys):
            out += keys
    return out or [entry_name]


def _has(text, name):
    if name.lower() not in text:
        return False
    return re.search(rf"(?<![\w-]){re.escape(name.lower())}(?![\w-])", text) is not None


def lore_flavor_pages(p, S, norm):
    out = []
    for fl in p.get("flavors", []):
        n = norm(fl).strip(" .'\"-")
        if len(n.split()) >= 6:
            out += [u for u, t in S.items() if n in t and u not in out]
    return out


def audit_name_match(x, c, e, p, caps, S, norm):
    """Try to confirm a name-matched character card with official evidence (Bot cycle 35).

    Confirmed -> relation "depicts", `via` "name+<evidence>", `confirmed` = {by, source, detail}:
      art      the card's art is captioned (artist-matched) on an official story page that names the character;
      page     an official page cited by the entry names the card (full name, when it differs from the character's);
      flavor   a printing's flavor text names the character;
      spotlight  Scryfall marks a printing as a Story Spotlight card.
    Otherwise the link stays "name-match" (⚠️). Un-set (`set_type` funny) and digital-only cards get a flag.
    """
    x = dict(x)
    names = char_names(e["name"], c["name"])
    fr = norm(front(c["name"])).strip()
    ent_urls = [u.rstrip("/.,") for u in OFFICIAL_URL.findall(e["text"])]
    ent_urls = list(dict.fromkeys(ent_urls))
    hit = None
    for t, u, a in caps.get(c["name"], []) + (caps.get(front(c["name"]), []) if front(c["name"]) != c["name"] else []):
        if a in p.get("artists", set()) and any(_has(S.get(u.rstrip("/"), ""), norm(n)) for n in names):
            hit = {"by": "art", "source": u, "detail": f"card art captioned on {t}"}
            break
    plain = norm(re.sub(r"\[([^\]]*)\]\([^)]*\)", "", e["text"]))  # entry prose without card links
    if not hit and fr not in {norm(n) for n in names} and len(fr.split()) >= 2 and not _has(plain, fr):
        # (a name the entry itself uses for the character, e.g. "Rowan Kenrith", is not evidence for the card)
        for u in ent_urls + sorted(S):
            if _has(S.get(u, ""), fr) and any(_has(S.get(u, ""), norm(n)) for n in names):
                hit = {"by": "page", "source": u, "detail": "official page names the card" + (" (cited by the entry)" if u in ent_urls else "")}
                break
    if not hit:
        for t, u, kind in presented_on(c["name"], norm):
            if not any(_has(extra_pages()[u]["text"], norm(n)) for n in names):
                continue
            hit = {"by": "legends", "source": u, "detail": f"card presented on {t}"}
            break
    if not hit:
        for fl in p.get("flavors", []):
            if any(_has(norm(fl), norm(n)) for n in names):
                hit = {"by": "flavor", "source": None, "detail": "flavor text names " + next(n for n in names if _has(norm(fl), norm(n)))}
                break
    if not hit:
        for u in lore_flavor_pages(p, S, norm):
            if any(_has(S.get(u, ""), norm(n)) for n in names):
                hit = {"by": "flavor-page", "source": u, "detail": "flavor text verbatim on an official page that names the character"}
                break
    if not hit and p.get("spotlight"):
        hit = {"by": "spotlight", "source": None, "detail": "Story Spotlight printing " + p["spotlight"][0]}
    if hit:
        x["relation"] = "depicts"
        x["via"] = "name+" + hit["by"]
        x["sources"] = [hit["source"]] if hit["source"] else ent_urls[:2]
        x["confirmed"] = hit
    flags = []
    if p.get("set_types") and p["set_types"] <= {"funny"}:
        flags.append("🚫")  # every paper printing is in an Un-/playtest ("funny") set
    if not p.get("sets"):
        flags.append("⚠️")  # no paper printing: digital-only
    x["line_flags"] = flags
    return x


def lore_for(r, c, links, cc, keys, prints, S, norm, notes, caps, afs, prev_lore=None):
    k = (r["shard"], r["anchor"])
    rel = []
    for x in links.get(k, []):
        relation = "depicts" if x["kind"] in ("character", "dossier", "item") and names_match(x["name"], c["name"]) else "featured"
        if relation == "depicts" and x["kind"] == "item" and "Creature" in face_types(c)[0] \
                and front(c["name"]).lower() not in x["name"].lower():
            relation = "featured"  # a creature named for an item (Halo Forager → Halo) features it, not depicts it
        if x["kind"] == "plane" and names_match(x["name"], c["name"]):
            relation = "depicts"  # a legendary land / location named for the plane
        rel.append({"entry": x["key"], "kind": x["kind"], "name": x["name"], "relation": relation, "sources": x["sources"],
                    "via": x["via"], "line_flags": x["line_flags"]})
    have = {x["entry"] for x in rel}
    for ek in cc.get(k, []):
        if ek in have:
            continue
        e = keys[ek]
        rel.append({"entry": ek, "kind": e["kind"], "name": e["name"], "relation": "name-match", "sources": [], "via": "name", "line_flags": []})
    p = prints.get(r["oracle_id"]) or {"spotlight": [], "flavors": [], "stamps": set(), "artists": set(), "sets": [], "set_types": set()}
    rel = [audit_name_match(x, c, keys[x["entry"]], p, caps, S, norm) if x["relation"] == "name-match" else x for x in rel]
    flav = []
    for fl in p["flavors"]:
        n = norm(fl).strip(" .'\"-")
        if len(n.split()) < 6:
            continue
        for u, t in S.items():
            if n in t and u not in flav:
                flav.append(u)
    if not S and prev_lore:
        # No story-page cache on this box (gitignored; lost in the cycle 34 reset): keep the
        # flavor-text matches verified in an earlier run instead of silently dropping them.
        flav = list(prev_lore.get("flavor_on", []))
    cn = c["name"] if c["name"] in caps else front(c["name"])
    art = []
    for t, u, a in caps.get(cn, []):
        if a in p.get("artists", set()) and u not in [x[1] for x in art]:
            art.append([t, u])
    sec = afs.get(k)
    out = {"relations": rel, "spotlight": sorted(set(p["spotlight"]))[:3], "flavor_on": sorted(flav)[:3],
           "art_on": sorted(art, key=lambda x: x[1])[:3], "art_flavor": list(sec) if sec else None,
           "presented_on": presented_on(c["name"], norm)[:3],
           "flags": (["🚫 Universes Beyond printing (triangle stamp): outside Multiverse canon"] if p["stamps"] and p["stamps"] <= {"triangle"} else []) +
                    (["🚫 Un-/playtest card (every printing in a `funny` set): outside story canon"] if p.get("set_types") and p["set_types"] <= {"funny"} else []) +
                    (["⚠️ digital-only card (no paper printing)"] if not p.get("sets") else [])}
    if c["name"] in notes:
        out["note"] = notes[c["name"]]
    return out


def synergy_for(c, decks, pkgmatch, fetch, prev):
    name = c["name"]
    pv = (prev or {}).get("proven", {})
    sb = spellbook(name, fetch)
    if sb is None:
        sb = pv.get("spellbook")
    ec = edhrec_card(name, fetch)
    if ec is None:
        ec = pv.get("edhrec")
    cmd = None
    if ing.commander_eligibility(c).startswith("Yes"):
        cmd = edhrec_commander(name, fetch)
        if cmd is None:
            cmd = pv.get("as_commander")
    dk = sorted(set(decks.get(name, []) + (decks.get(front(name), []) if front(name) != name else [])), key=lambda x: x[1])
    proven = {"decks": [{"label": a, "path": b} for a, b in dk]}
    if sb and not sb.get("error"):
        proven["spellbook"] = sb
    if ec and not ec.get("error"):
        proven["edhrec"] = ec
    if cmd and not cmd.get("error"):
        proven["as_commander"] = cmd
    return {"proven": proven, "guidance": {"packages": pkgmatch(c)}}


def fmt_n(n):
    return f"{n:,}" if isinstance(n, int) else "?"


def render(r, card, lore, syn, rows_by_name):
    def clink(n):
        rr = rows_by_name.get(n) or rows_by_name.get(front(n))
        return f"[{n}]({card_href(rr)})" if rr else n
    parts = []
    by_rel = defaultdict(list)
    for x in lore["relations"]:
        src = ""
        if x["sources"]:
            src = " (" + ", ".join(f"[{'source' if i == 0 else i + 1}]({u})" for i, u in enumerate(x["sources"][:2])) + (" via entry" if x["via"] == "entry" else "") + ")"
        fl = f" (the entry line carries {''.join(x['line_flags'])})" if x["line_flags"] else ""
        if x["via"].startswith("name"):
            fl = ""
            if x.get("confirmed"):
                cf = x["confirmed"]
                src = (f" ([source]({cf['source']}))" if cf["source"] else
                       (" (" + ", ".join(f"[{'entry source' if i == 0 else i + 1}]({u})" for i, u in enumerate(x["sources"][:2])) + ")" if x["sources"] else ""))
                fl = f" — name match confirmed: {cf['detail']}{src}" + fl
        if x.get("confirmed"):
            src = ""
        by_rel[x["relation"]].append(f"[{KIND[x['kind']]} → {x['name']}](../../{esc(x['entry'])}){src}{fl}")
    if by_rel["depicts"]:
        parts.append("Depicts: " + " · ".join(by_rel["depicts"]))
    if by_rel["featured"]:
        parts.append("Featured in: " + " · ".join(by_rel["featured"]))
    if lore["spotlight"]:
        sec = lore.get("art_flavor")
        parts.append("✅ Story Spotlight printing (Scryfall `story_spotlight`): " + ", ".join(lore["spotlight"]) +
                     (f" — [Art & Flavor → {sec[1]}](../../Art%20%26%20Flavor%20Story%20Links.md#{sec[0]})" if sec else ""))
    if lore.get("art_on"):
        parts.append("✅ Card art shown on " + ", ".join(f"[{t}]({u})" for t, u in lore["art_on"]) + " (caption names the card and its artist)")
    for t, u, kind in lore.get("presented_on", []):
        parts.append(f"✅ {'Listed on' if kind == 'spotlight' else 'Presented with an official backstory on'} [{t}]({u})")
    if lore["flavor_on"]:
        parts.append("✅ Flavor text verbatim on " + ", ".join(f"[official page {i + 1}]({u})" for i, u in enumerate(lore["flavor_on"])))
    if lore.get("note"):
        nt = lore["note"]
        parts.append(f"{nt.get('flag', '')} *{nt['relation'].capitalize()}:* {nt['text']} (" + ", ".join(f"[source]({u})" for u in nt["sources"]) + ")")
    if by_rel["name-match"]:
        parts.append("⚠️ Name match only (not a canon claim): " + " · ".join(by_rel["name-match"]))
    parts += lore["flags"]
    if not (lore["relations"] or lore["spotlight"] or lore.get("art_on") or lore["flavor_on"] or lore.get("note") or lore.get("presented_on")):
        parts.insert(0, NO_LORE)
    lore_line = f"{LORE_P} " + " — ".join(p.strip() for p in parts) + " · [format](../../Card%20Enrichment.md#lore-line)"
    pv, gd = syn["proven"], syn["guidance"]
    sp = []
    if pv["decks"]:
        sp.append(f"KB decks ({len(pv['decks'])}): " + " · ".join(f"[{d['label']}](../../{esc(d['path'])})" for d in pv["decks"][:4]) + (" …" if len(pv["decks"]) > 4 else ""))
    sb = pv.get("spellbook")
    if sb and not sb["count"]:
        sp.append("Commander Spellbook: no Commander-legal combo listed")
    if sb and sb["count"]:
        t = sb["top"][0]
        sp.append(f"Commander Spellbook: {sb['count']}{'+' if sb['capped'] else ''} combo{'s' if sb['count'] != 1 else ''}; most popular [{' + '.join(t['cards'])}](https://commanderspellbook.com/combo/{t['id']}/) ({', '.join(t['produces'])})")
    ac = pv.get("as_commander")
    if ac and ac.get("decks"):
        sp.append(f"EDHREC as commander: {fmt_n(ac['decks'])} decks; highest synergy " + ", ".join(f"{clink(x['name'])} (+{x['synergy']}%)" for x in ac["top_synergy"]))
    ec = pv.get("edhrec")
    if ec and ec.get("decks"):
        s = f"EDHREC: in {fmt_n(ec['decks'])} decks"
        if ec["top_commanders"]:
            s += "; most often under " + ", ".join(f"{clink(x['name'])} ({x['pct']}% of its decks)" for x in ec["top_commanders"])
        sp.append(s)
    seg = [f"*Proven* — " + " · ".join(sp)] if sp else ["*Proven* — none in the cached data"]
    if gd["packages"]:
        seg.append("*Guidance (Oracle pattern)* — packages: " + " · ".join(f"[{p}](../../EDH%20Packages.md#{L.anchor(p)})" for p in gd["packages"][:3]))
    syn_line = f"{SYN_P} " + " — ".join(seg) + " · [format](../../Card%20Enrichment.md#synergy-line)"
    return [lore_line, syn_line]


def build(fetch=False):
    import build_crossrefs as bx
    rows = list(csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8")))
    rows_by_key = {(r["shard"], r["anchor"]): r for r in rows}
    rows_by_name = {r["name"]: r for r in rows}
    for r in rows:
        rows_by_name.setdefault(front(r["name"]), r)
    by_id, bulk = load_bulk()
    links = entry_links()
    cc, keys = charcard_links()
    prints = load_printings()
    caps = art_captions()
    afs = art_flavor_sections()
    prev = json.loads(OUT.read_text(encoding="utf-8")).get("cards", {}) if OUT.exists() else {}
    tiers = pool(rows_by_key, by_id, prints, links, cc, caps, prev)
    notes = json.loads(NOTES.read_text(encoding="utf-8")) if NOTES.exists() else {}
    notes = {k: v for k, v in notes.items() if not k.startswith("_")}
    S, norm = story_norm()
    decks = deck_index()
    pkgmatch, _ = bx.package_matcher()
    sel = []
    for r in rows:
        c = by_id.get(r["oracle_id"])
        if c and any(f(c, tiers.get(r["oracle_id"], set())) for _, _, f in BATCHES):
            sel.append(c)
    if fetch:
        # only cards without stored synergy (the third-party caches are gitignored and may be gone; Bot cycle 35)
        prefetch([c for c in sel if c["oracle_id"] not in prev])
    cards = {}
    for r in sorted(rows, key=lambda r: r["name"]):
        c = by_id.get(r["oracle_id"])
        if not c:
            continue
        batch = next((n for n, _, sel in BATCHES if sel(c, tiers.get(r["oracle_id"], set()))), None)
        if batch is None:
            continue
        lore = lore_for(r, c, links, cc, keys, prints, S, norm, notes, caps, afs, prev.get(r["oracle_id"], {}).get("lore"))
        syn = synergy_for(c, decks, pkgmatch, False, prev.get(r["oracle_id"], {}).get("synergy"))
        cards[r["oracle_id"]] = {"name": r["name"], "shard": r["shard"], "anchor": r["anchor"], "batch": batch,
                                 "type": type_group(c), "tiers": sorted(tiers.get(r["oracle_id"], set())),
                                 "lore": lore, "synergy": syn, "lines": render(r, c, lore, syn, rows_by_name)}
    tn = ["entry-linked", "character-card", "legendary-creature", "planeswalker", "story-flavor"]
    pool_ids = {o for o, t in tiers.items() if t}
    cov = {t: {"size": sum(1 for o in pool_ids if t in tiers[o]), "enriched": sum(1 for o in cards if t in tiers.get(o, ()))} for t in tn}
    cov["priority pool (any tier)"] = {"size": len(pool_ids), "enriched": sum(1 for o in cards if o in pool_ids)}
    return {"generated_by": "scripts/build_card_enrichment.py", "bulk": bulk[:10], "batches": [{"cycle": n, "rule": d} for n, d, _ in BATCHES],
            "coverage": cov, "cards": cards}


# ------------------------------------------------------------------ shards, page, checks
def patch_shards(d, write):
    want = {(v["shard"], v["anchor"]): v["lines"] for v in d["cards"].values()}
    stale = 0
    for p in sorted((ROOT / "cards").rglob("*.md")):
        if p.name == "README.md":
            continue
        rel = str(p.relative_to(ROOT))
        text = p.read_text(encoding="utf-8")
        head, sep, body = text.partition("\n## Entries\n")
        seen = Counter()
        out = []
        for ch in re.split(r"\n(?=### )", body):
            if ch.startswith("### "):
                a = ing.gh_anchor(ch.split("\n", 1)[0][4:])
                a2 = f"{a}-{seen[a]}" if seen[a] else a
                seen[a] += 1
                lines = [l for l in ch.split("\n") if not l.startswith((LORE_P, SYN_P))]
                add = want.get((rel, a2))
                if add:
                    i = next((k for k, l in enumerate(lines) if l.startswith(("- **Referenced in:**", "- **Source flags:**"))), len(lines))
                    lines[i:i] = add
                ch = "\n".join(lines)
            out.append(ch)
        new = head + sep + "\n".join(out)
        if new != text:
            stale += 1
            if write:
                p.write_text(new, encoding="utf-8")
    return stale


def write_page(d):
    cards = sorted(d["cards"].values(), key=lambda v: v["name"])
    L_ = ["# Card Enrichment", "",
          f"> **Generated** by `scripts/build_card_enrichment.py` (Bot cycle 33, Phase 8 — [#99]({ISS}99) format, [#100]({ISS}100) lore, [#101]({ISS}101) synergy, [#102]({ISS}102) links + validation). Do not hand-edit; curated lore notes go in `data/card_lore_notes.json`. Machine copy: `data/card_enrichment.json`.",
          "> Each enriched card entry gains a **Lore** line and a **Synergy** line, placed before *Referenced in*. They are pointers to existing KB entries, Scryfall fields, cached official pages and cited third-party data. They never repeat Oracle text or rulings, and they add no new facts.", "",
          "## Contents", "- [Lore line](#lore-line)", "- [Synergy line](#synergy-line)", "- [Coverage of the priority pool](#coverage-of-the-priority-pool)", "- [Name-match audit](#name-match-audit)",
          "- [Enriched cards](#enriched-cards)", "- [By lore entry](#by-lore-entry)", "- [By package](#by-package)", "- [Synergy clusters](#synergy-clusters)", "",
          "## Lore line",
          "| Part | Meaning | Evidence |", "|---|---|---|",
          "| **Depicts** | the lore entry's own text links this card, and the card is that character or item (its name contains the entry's name) | official URLs on the entry line that links the card; *via entry* = the entry's own citations when that line has none |",
          "| **Featured in** | the entry's text links the card in another context: a plane's notable cards, an arc beat, a retcon | same |",
          "| ✅ **Story Spotlight** | a printing Wizards marked as depicting a story moment (Scryfall `story_spotlight`) | Scryfall default-cards bulk |",
          "| ✅ **Flavor text verbatim on** | a printed flavor text that appears word for word on a cached official page | `.cache/story/` (Wizards pages) |",
          "| ✅ **Presented with an official backstory on** / **Listed on** | the card's (front-face) name is a heading line on an official *Legends of …* article (each legend with its backstory) or a *Story Spotlight Cards* preview article (Bot cycle 36) | `data/story_extra_sources.csv` → `.cache/story/extra/` (Wizards pages) |",
          "| *Depicts / References / Echoes:* note | curated note (`data/card_lore_notes.json`). *Echoes* = the card's mechanics mirror a cited story moment (guidance) | official sources listed in the note |",
          "| (the entry line carries ⚠️/❓/🚫) | the lore-entry line that links the card has an uncertainty flag; read the entry before relying on the link | the entry |",
          "| **Depicts — name match confirmed** | a name-matched character card (below) tied to the character by official evidence (Bot cycle 35 audit): its art captioned on an official story page that names the character · an official page (preferably one the entry cites) naming the card · the card presented as a legend on an official *Legends of …* / Story Spotlight article that names the character (cycle 36, second pass) · its flavor text naming the character · a Story Spotlight printing | the page linked on the line; for flavor/Spotlight the entry's own citations |",
          "| ⚠️ **Name match only** | the card's name matches a character entry (the generated *Character cards (name-matched)* tables). Not a claim about canon, timing or which version | Scryfall names |",
          "| 🚫 | every paper printing is Universes Beyond (triangle security stamp), or every paper printing is in an Un-/playtest (`funny`) set: outside the Multiverse story | Scryfall `security_stamp`, `set_type` |",
          "| ⚠️ digital-only | the card has no paper printing | Scryfall `digital` |",
          "| ❓ No lore entry … yet | synergy batch (cycle 35+): no lore link or official evidence found so far; not a claim that the card has no story | — |", "",
          "## Synergy line",
          "| Tier | Contents | Source |", "|---|---|---|",
          "| *Proven* | **KB decks** that run the card · **Commander Spellbook** combo count (Commander-legal variants) and the most popular one · **EDHREC as commander**: decks and highest-synergy cards · **EDHREC**: decks that run the card and the commanders it appears under most (share of that commander's decks) | repo decklists; [Commander Spellbook](https://commanderspellbook.com) API; [EDHREC](https://edhrec.com) JSON pages (community data, snapshot; cached in `.cache/`) |",
          "| *Guidance (Oracle pattern)* | [EDH Packages](EDH%20Packages.md) sub-packages whose Oracle-text pattern the card matches: its archetype role | `scripts/build_packages.py` patterns |", "",
          "EDHREC and Spellbook numbers are snapshots of community data, not rules or canon. A missing value means the source had no page for the card. *n+ combos* = the query returned its first 100 variants by popularity, so there are more.", "",
          "## Coverage of the priority pool",
          "Phase 8 priority order: legendary creatures, planeswalkers, story-significant cards (linked from lore entries or name-matched to characters), strong flavor-text cards (Story Spotlight, or flavor text quoted on a cached official page); then outward. A card can be in several tiers.", "",
          "| Tier | Cards in the KB | Enriched | Coverage |", "|---|---|---|---|"]
    for t, v in d["coverage"].items():
        L_.append(f"| {t} | {v['size']:,} | {v['enriched']:,} | {100 * v['enriched'] / v['size']:.1f}% |" if v["size"] else f"| {t} | 0 | 0 | — |")
    au = Counter()
    for v in cards:
        for x in v["lore"]["relations"]:
            if x["via"].startswith("name"):
                au[x["confirmed"]["by"] if x.get("confirmed") else "kept ⚠️ name match only"] += 1
                if "🚫" in x["line_flags"]:
                    au["of which 🚫 Un-/playtest card"] += 1
                if "⚠️" in x["line_flags"]:
                    au["of which ⚠️ digital-only card"] += 1
    lab = {"art": "confirmed: art captioned on an official page naming the character", "page": "confirmed: official page names the card",
           "flavor": "confirmed: flavor text names the character", "flavor-page": "confirmed: flavor text verbatim on an official page naming the character",
           "spotlight": "confirmed: Story Spotlight printing", "legends": "confirmed: card presented on an official Legends / Story Spotlight article naming the character (cycle 36)"}
    L_ += ["", "## Name-match audit",
           "Bot cycle 35 ([#100](" + ISS + "100)): every link that rested only on a name match (*Character cards (name-matched)* tables) was tested against the cached official story pages (`scripts/fetch_story_pages.py`), the entry's citations and the card's printings. Confirmed links render as *Depicts — name match confirmed* with the evidence; the rest stay ⚠️. Bot cycle 36 ran a second pass over the remaining ⚠️ links with the official *Legends of …* and *Story Spotlight Cards* articles (`data/story_extra_sources.csv`); Planeswalker's Guide card galleries are images, so they are not used as evidence. Group headings no longer repeat cards that sit under the character's own heading (those links were removed in `scripts/build_crossrefs.py`).", "",
           "| Result | Links |", "|---|---|"] + [f"| {lab.get(k, k)} | {n:,} |" for k, n in sorted(au.items(), key=lambda kv: (kv[0].startswith("of which"), kv[0].startswith("kept"), -kv[1]))]
    L_ += ["", "Batches: " + "; ".join(f"Bot cycle {b['cycle']} — {b['rule']}" for b in d["batches"]) + ".", "",
           "## Enriched cards", "Every enriched card, by type and batch. The full per-card record is `data/card_enrichment.json`; the card's own entry shows the two lines.", "",
           "| Type | " + " | ".join(f"Bot cycle {b['cycle']}" for b in d["batches"]) + " | Total |", "|---|" + "---|" * (len(d["batches"]) + 1)]
    tb = Counter((v["type"], v["batch"]) for v in cards)
    for t in sorted({v["type"] for v in cards}, key=lambda t: -sum(n for (tt, _), n in tb.items() if tt == t)):
        L_.append(f"| {t} | " + " | ".join(f"{tb[(t, b['cycle'])]:,}" for b in d["batches"]) + f" | {sum(n for (tt, _), n in tb.items() if tt == t):,} |")
    L_.append("| **all** | " + " | ".join(f"**{sum(1 for v in cards if v['batch'] == b['cycle']):,}**" for b in d["batches"]) + f" | **{len(cards):,}** |")
    ev = Counter()
    for v in cards:
        lo = v["lore"]
        ev.update({"depicts": any(x["relation"] == "depicts" for x in lo["relations"]),
                   "featured": any(x["relation"] == "featured" for x in lo["relations"]),
                   "name match only": bool(lo["relations"]) and all(x["relation"] == "name-match" for x in lo["relations"]),
                   "Story Spotlight": bool(lo["spotlight"]), "art on an official page": bool(lo.get("art_on")),
                   "flavor text on an official page": bool(lo["flavor_on"]), "curated note": bool(lo.get("note")),
                   "🚫 Universes Beyond": bool(lo["flags"]),
                   "in a KB deck": bool(v["synergy"]["proven"]["decks"]),
                   "Spellbook combo": bool(v["synergy"]["proven"].get("spellbook", {}).get("count")),
                   "EDHREC data": bool(v["synergy"]["proven"].get("edhrec", {}).get("decks")),
                   "EDHREC as commander": bool(v["synergy"]["proven"].get("as_commander", {}).get("decks")),
                   "package match (guidance)": bool(v["synergy"]["guidance"]["packages"])})
    L_ += ["", "| Evidence on the card's lines | Cards |", "|---|---|"] + [f"| {k} | {n:,} |" for k, n in ev.items()]
    by_e = defaultdict(list)
    by_p = defaultdict(list)
    for v in cards:
        for x in v["lore"]["relations"]:
            by_e[(x["entry"], x["kind"], x["name"])].append((v, x["relation"]))
        for p in v["synergy"]["guidance"]["packages"][:3]:
            by_p[p].append(v)
    L_ += ["", "## By lore entry", "Every lore entry named on an enriched card's Lore line, with the cards that name it. The entry links each card back in its own text (or, for name matches, in the *Character cards (name-matched)* table).", "",
           "| Lore entry | Enriched cards |", "|---|---|"]
    for (k, kind, nm), vs in sorted(by_e.items(), key=lambda x: (x[0][1], x[0][2])):
        L_.append(f"| [{KIND[kind]} → {nm}]({esc(k)}) | " + " · ".join(f"[{v['name']}]({esc(v['shard'])}#{v['anchor']}) ({r})" for v, r in vs) + " |")
    L_ += ["", "## By package", "Guidance tier: the [EDH Packages](EDH%20Packages.md) sub-packages named on enriched cards' Synergy lines (Oracle-pattern matches).", "",
           "| Package | Enriched cards |", "|---|---|"]
    for p, vs in sorted(by_p.items(), key=lambda x: (-len(x[1]), x[0])):
        L_.append(f"| [{p}](EDH%20Packages.md#{L.anchor(p)}) | " + " · ".join(f"[{v['name']}]({esc(v['shard'])}#{v['anchor']})" for v in vs) + " |")
    cm = defaultdict(list)
    for v in cards:
        for x in v["synergy"]["proven"].get("edhrec", {}).get("top_commanders", []):
            cm[x["name"]].append(v["name"])
    L_ += ["", "## Synergy clusters", "Commanders (EDHREC) under which two or more enriched cards appear most often: proven co-occurrence, not a recommendation.", "",
           "| Commander | Enriched cards it runs most |", "|---|---|"]
    rows = {r["name"]: r for r in csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8"))}
    ent = {v["name"]: v for v in cards}

    def cl(n, src):
        r = src.get(n)
        return f"[{n}]({esc(r['shard'])}#{r['anchor']})" if r else n
    for n, vs in sorted(cm.items(), key=lambda x: (-len(x[1]), x[0])):
        if len(vs) >= 2:
            L_.append(f"| {cl(n, rows)} | {' · '.join(cl(x, ent) for x in sorted(vs))} |")
    return "\n".join(L_) + "\n"


_PKG = None


def pkg_sections():
    """{sub-package title: section text} of EDH Packages.md (### headings)."""
    global _PKG
    if _PKG is None:
        _PKG = {}
        t = (ROOT / "EDH Packages.md").read_text(encoding="utf-8")
        for ch in re.split(r"\n(?=### )", t)[1:]:
            _PKG[ch.split("\n", 1)[0][4:].strip()] = ch.split("\n## ")[0]
    return _PKG


def S_all():
    import lore_quotes as Q
    return set(Q.story()) | set(extra_pages())


def check(d):
    bad = []
    keys = {f"{e['page']}#{e['anchor']}": e for e in L.all_entries()}
    for oid, v in d["cards"].items():
        lo = v["lore"]
        if not (lo["relations"] or lo.get("note") or lo["spotlight"] or lo["flavor_on"] or lo.get("art_on") or lo.get("presented_on")):
            if v["batch"] < 35:
                bad.append(f"{v['name']}: no lore relation or official evidence")
            elif NO_LORE not in v["lines"][0]:
                bad.append(f"{v['name']}: synergy-batch card without lore evidence must carry the ❓ line")
        if lo["spotlight"] and lo.get("art_flavor"):
            t = (ROOT / AF_PAGE).read_text(encoding="utf-8")
            if f"]({v['shard']}#{v['anchor']})" not in t:
                bad.append(f"{v['name']}: Art & Flavor Story Links does not list the card back")
        for x in lo["relations"]:
            if x["relation"] not in RELATIONS:
                bad.append(f"{v['name']}: unknown relation {x['relation']}")
            e = keys.get(x["entry"])
            if not e:
                bad.append(f"{v['name']}: lore entry {x['entry']} does not resolve")
                continue
            if x["relation"] != "name-match" and not x["sources"]:
                bad.append(f"{v['name']}: {x['entry']} relation has no official citation")
            target = (v["shard"], v["anchor"])
            if x.get("confirmed") and x["confirmed"]["by"] not in ("art", "page", "legends", "flavor", "flavor-page", "spotlight"):
                bad.append(f"{v['name']}: unknown name-match confirmation {x['confirmed']['by']}")
            if x.get("confirmed") and x["confirmed"]["source"] and S_all() and x["confirmed"]["by"] in ("page", "legends", "flavor-page", "art") \
                    and x["confirmed"]["source"].rstrip("/") not in S_all():
                bad.append(f"{v['name']}: name-match confirmation cites an uncached page {x['confirmed']['source']}")
            if x["relation"] == "name-match" or x["via"].startswith("name"):
                t = (ROOT / e["page"]).read_text(encoding="utf-8")
                blk = t[t.find("<!-- CHARCARDS:START -->"):]
                row = next((l for l in blk.splitlines() if l.startswith(f"| [") and f"](#{e['anchor']})" in l.split("|")[1]), "")
                if target not in L.links(row, e["page"]):
                    bad.append(f"{v['name']}: name-matched entry {x['entry']} does not list the card back")
            elif target not in L.links(e["text"], e["page"]):
                bad.append(f"{v['name']}: entry {x['entry']} does not link the card back")
        nt = lo.get("note")
        if nt and nt.get("flag", "") not in ("", "⚠️", "❓", "🚫", "🔄"):
            bad.append(f"{v['name']}: curated note flag must be one of ⚠️ ❓ 🚫 🔄")
        if nt:
            if nt.get("relation") not in NOTE_RELATIONS or not nt.get("sources") or not all(L.OFFICIAL.match(u) for u in nt["sources"]):
                bad.append(f"{v['name']}: curated note needs relation in {NOTE_RELATIONS} and official (wizards.com) sources")
            import lore_quotes as Q
            S = Q.story()
            if S:
                pages = [S.get(u.rstrip("/"), "") or extra_pages().get(u.rstrip("/"), {}).get("text", "") for u in nt.get("sources", [])]
                for q in Q.pair_quotes(nt["text"]):
                    if not all(any(pp in pg for pg in pages) for pp in Q.parts(q)):
                        bad.append(f"{v['name']}: note quote not verbatim in its cited page: \"{q[:60]}\"")
        syn = v["synergy"]
        if set(syn) != set(TIERS):
            bad.append(f"{v['name']}: synergy tiers must be exactly {TIERS}")
        for dk in syn["proven"]["decks"]:
            import build_crossrefs as bx
            names = set(bx.deck_cards(ROOT / dk["path"]))
            if v["name"] not in names and front(v["name"]) not in names:
                bad.append(f"{v['name']}: deck {dk['path']} does not contain the card")
        ln = v["lines"]
        if not (ln[0].startswith(LORE_P) and ln[1].startswith(SYN_P) and "*Proven*" in ln[1]):
            bad.append(f"{v['name']}: rendered lines malformed or tier label missing")
        for pk in syn["guidance"]["packages"][:3]:
            sec = pkg_sections().get(pk, "")
            if f"]({v['shard']}#{v['anchor']})" not in sec:
                bad.append(f"{v['name']}: EDH Packages → {pk} does not list the card back (run scripts/build_packages.py)")
        if syn["guidance"]["packages"] and "*Guidance (Oracle pattern)*" not in ln[1]:
            bad.append(f"{v['name']}: guidance tier label missing")
    return bad


def main(argv):
    if "--check" in argv:
        if not OUT.exists():
            print("card enrichment: data/card_enrichment.json missing — run python3 scripts/build_card_enrichment.py")
            return 1
        cur = json.loads(OUT.read_text(encoding="utf-8"))
        problems = []
        if ing.DEFAULT_CACHE.exists() and glob.glob(str(ROOT / ".cache" / "default-cards-*.jsonl.gz")):
            new = build(False)
            if json.dumps(new, sort_keys=True) != json.dumps(cur, sort_keys=True):
                problems.append("data/card_enrichment.json stale — run python3 scripts/build_card_enrichment.py")
            cur = new
            mode = "rebuilt from caches"
        else:
            mode = "bulk cache absent: checked the stored data"
        ns = patch_shards(cur, write=False)
        if ns:
            problems.append(f"{ns} card shards stale")
        pg = PAGE.read_text(encoding="utf-8") if PAGE.exists() else ""
        import front_matter as fm
        if fm.body_of(pg) != write_page(cur):
            problems.append("Card Enrichment.md stale")
        problems += check(cur)
        n = len(cur["cards"])
        rel = sum(len(v["lore"]["relations"]) for v in cur["cards"].values())
        cov = cur["coverage"]["priority pool (any tier)"]
        print(f"card enrichment: {n} cards ({mode}); {rel} lore relations, all reciprocal unless listed; priority pool {cov['enriched']}/{cov['size']}; {len(problems)} problems")
        for p in problems[:30]:
            print("  " + p)
        return 1 if problems else 0
    d = build("--fetch" in argv)
    OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    ns = patch_shards(d, write=True)
    import front_matter as fm
    body = write_page(d)
    old = PAGE.read_text(encoding="utf-8") if PAGE.exists() else ""
    if fm.body_of(old) != body:
        m = fm.FM.match(old)
        PAGE.write_text((m.group(0) if m else "") + body, encoding="utf-8")
    bad = check(d)
    print(f"card enrichment: {len(d['cards'])} cards; {ns} shards updated; {len(bad)} problems")
    for b in bad[:30]:
        print("  " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
