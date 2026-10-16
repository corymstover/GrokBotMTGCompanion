#!/usr/bin/env python3
"""Apply or check typed YAML front-matter on every major entry (issue #44 Bot cycle 15; schema v2 issue #65 Bot cycle 17).

Three entry kinds share one documented schema (see "Front-Matter Schema.md", generated from SCHEMA below):
  * page  — every top-level page and grixis/ page (registry PAGES below)
  * deck  — decks/*.md and grixis/decks/*.md (fields parsed from each deck body, so they match it)
  * shard — cards/<L>/<prefix>.md card shards (fields parsed from the shard; ingest_scryfall.py calls apply_shards)
Front-matter makes the repo filterable with plain text tools, e.g.
  rg -l '^category: lore' *.md     rg -l '^tags: .*two-card-infinite' decks grixis/decks     rg -l '^bracket_floor: 4' decks/
Usage:
  python3 scripts/front_matter.py           apply to pages, decks and shards + regenerate the schema page (idempotent)
  python3 scripts/front_matter.py --check   exit 1 on a missing/stale/ill-typed field, unknown tag form or unregistered page
  python3 scripts/front_matter.py --no-shards   skip the 739 card shards (faster)
README.md and GOAL.md are left untouched: README is the dashboard and GOAL is the user's own file.
"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote as urlq, unquote

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import lore_lib  # noqa: E402  (Bot cycle 31: entry kinds/counts for lore pages)
I = "https://github.com/corymstover/GrokBotMTGCompanion/issues/"
SCHEMA_VERSION = 2
CATEGORIES = {"lore", "edh", "rules", "cards", "meta"}
SOURCES = {"scryfall": "Scryfall Oracle/rulings/default-cards bulk", "wizards-story": "magic.wizards.com story pages",
           "edhrec": "EDHREC public JSON (community data)", "spellbook": "Commander Spellbook API (community data)",
           "cr": "Comprehensive Rules text", "wotc-articles": "magic.wizards.com / WPN announcements and documents",
           "grixis-repo": "corymstover/grixis-commander-encyclopediaGPT (read-only source)"}
COLOR_ORDER = "WUBRG"
IDENTITY_NAMES = {"C": "colorless", "W": "mono-white", "U": "mono-blue", "B": "mono-black", "R": "mono-red", "G": "mono-green",
                  "WU": "azorius", "UB": "dimir", "BR": "rakdos", "RG": "gruul", "WG": "selesnya", "WB": "orzhov", "UR": "izzet",
                  "BG": "golgari", "WR": "boros", "UG": "simic", "WUG": "bant", "WUB": "esper", "UBR": "grixis", "BRG": "jund",
                  "WRG": "naya", "WBG": "abzan", "WUR": "jeskai", "UBG": "sultai", "WBR": "mardu", "URG": "temur",
                  "UBRG": "glint", "WBRG": "dune", "WURG": "ink", "WUBG": "witch", "WUBR": "yore", "WUBRG": "five-color"}
TAG_RX = re.compile(r"^[a-z0-9+]+(-[a-z0-9+]+)*$")
PAGES = {
    "Art & Flavor Story Links.md": ("lore", ["lore", "art", "flavor", "story-spotlight"], [37], "scripts/build_art_flavor.py", ["scryfall", "wizards-story"]),
    "Artist Index.md": ("cards", ["artists", "art-credits"], [43], "scripts/build_artists.py", ["scryfall"]),
    "Card Data Conventions.md": ("meta", ["conventions", "card-entries"], [96, 99], None, ["scryfall"]),
    "Card Index.md": ("cards", ["index", "coverage"], [1, 2, 5], "scripts/ingest_scryfall.py", ["scryfall"]),
    "Card Enrichment.md": ("cards", ["card-enrichment", "lore", "synergy", "coverage", "phase-8"], [99, 100, 101, 102], "scripts/build_card_enrichment.py", ["scryfall", "wizards-story", "spellbook", "edhrec"]),
    "Characters Index.md": ("lore", ["lore", "characters", "status", "planeswalkers"], [7, 11, 20, 74, 92, 93, 94], None, ["wizards-story"]),
    "Conflicts & Arcs.md": ("lore", ["lore", "arcs", "conflicts"], [7, 13, 34, 72, 73, 92, 93, 94], None, ["wizards-story"]),
    "Contradictions & Retcons Log.md": ("lore", ["lore", "retcons", "contradictions", "canon"], [73, 76, 92, 93, 94], None, ["wizards-story"]),
    "Items & Artifacts Index.md": ("lore", ["lore", "items", "artifacts", "relics"], [75, 92, 93, 94], None, ["wizards-story"]),
    "Lore Primary Sources.md": ("lore", ["lore", "sources", "primary", "planeswalkers-guide", "story-episodes"], [73, 94], "scripts/build_primary_sources.py", ["wizards-story"]),
    "EDH Archetypes.md": ("edh", ["archetypes", "strategy"], [16, 19], "scripts/build_archetypes.py", ["scryfall", "edhrec", "spellbook"]),
    "EDH Interaction.md": ("edh", ["removal", "interaction", "stax"], [28], "scripts/build_interaction.py", ["scryfall", "edhrec"]),
    "EDH Mana Bases.md": ("edh", ["lands", "mana-base", "color-identity"], [25], "scripts/build_mana_bases.py", ["scryfall", "edhrec"]),
    "EDH Mulligans.md": ("edh", ["mulligan", "opening-hand"], [31, 96], "scripts/build_mulligans.py", ["cr", "scryfall"]),
    "EDH Packages.md": ("edh", ["packages", "ramp", "card-advantage"], [26, 102], "scripts/build_packages.py", ["scryfall", "edhrec"]),
    "EDH Pairings.md": ("edh", ["partner", "background", "pairings"], [32], "scripts/build_pairings.py", ["cr", "scryfall"]),
    "EDH Standards.md": ("edh", ["deckbuilding-rules", "color-identity", "brackets"], [6, 96], None, ["cr", "wotc-articles"]),
    "EDH Staples.md": ("edh", ["staples", "color-identity"], [], "scripts/build_staples.py", ["scryfall", "edhrec"]),
    "EDH Themed Decks.md": ("edh", ["decks", "plane-restricted", "themes"], [33], "scripts/build_themed_index.py", ["scryfall", "edhrec"]),
    "EDH Lore-Themed Deckbuilding.md": ("edh", ["lore-decks", "story-first", "methodology", "template"], [79, 80, 81, 95], None, ["scryfall", "wizards-story", "spellbook", "cr"]),
    "EDH Upgrade Paths.md": ("edh", ["upgrades", "budget"], [30], "scripts/build_upgrade_paths.py", ["scryfall", "edhrec"]),
    "EDH Win Conditions.md": ("edh", ["win-conditions", "combos"], [27, 96], "scripts/build_wincons.py", ["scryfall", "spellbook"]),
    "FAQ.md": ("meta", ["faq", "lore", "rules"], [45, 96], None, ["cr", "wizards-story", "scryfall"]),
    "Format Legality Matrix.md": ("cards", ["legality", "formats", "banned-restricted"], [41, 96], "scripts/build_legality.py", ["scryfall", "wotc-articles"]),
    "Keyword Encyclopedia.md": ("rules", ["keywords", "evergreen", "rulings"], [39, 96], "scripts/build_keywords.py", ["cr", "scryfall", "wotc-articles"]),
    "Knowledge Index.md": ("meta", ["index", "maintenance"], [], None, []),
    "Knowledge Snapshots.md": ("meta", ["tags", "releases", "snapshots"], [47], None, []),
    "Lookup Guide.md": ("meta", ["lookup", "retrieval"], [46], None, []),
    "Master Timeline.md": ("lore", ["lore", "timeline", "eras"], [7, 72, 92, 93, 94], None, ["wizards-story"]),
    "Omenpath & Multiverse Connections.md": ("lore", ["lore", "omenpaths", "multiverse", "planes"], [36], None, ["wizards-story"]),
    "Planes Index.md": ("lore", ["lore", "planes"], [7, 12, 74, 92, 93, 94], None, ["wizards-story"]),
    "Planeswalker Dossiers.md": ("lore", ["lore", "planeswalkers", "dossiers", "sparks"], [35, 74, 92, 93, 94], None, ["wizards-story"]),
    "Printing History.md": ("cards", ["printings", "reprints", "reserved-list"], [40, 96], "scripts/build_printings.py", ["scryfall", "wotc-articles"]),
    "Progress Tracker.md": ("meta", ["progress", "milestones"], [], None, []),
    "ROADMAP.md": ("meta", ["roadmap", "sprint"], [], None, []),
    "Rules Interactions.md": ("rules", ["rules", "interactions", "rulings"], [9, 96], "scripts/build_rules_interactions.py", ["cr", "scryfall"]),
    "Side-Media Index.md": ("lore", ["lore", "novels", "comics", "side-media"], [38], None, ["wizards-story", "wotc-articles"]),
    "Story Arc Summaries.md": ("lore", ["lore", "arcs", "story-beats"], [34, 93, 96], None, ["wizards-story"]),
    "Story Archive Index.md": ("lore", ["lore", "story-archive", "sources"], [14], "scripts/crawl_story_index.py", ["wizards-story"]),
    "Tokens, Emblems & Dungeons.md": ("cards", ["tokens", "emblems", "dungeons", "not-cards"], [42, 96], "scripts/build_tokens.py", ["scryfall", "cr"]),
    "Update Log.md": ("meta", ["changelog"], [], None, []),
    "cEDH Primer.md": ("edh", ["cedh", "competitive", "bracket-5"], [29], "scripts/build_cedh.py", ["scryfall", "spellbook"]),
    # Bot cycle 16 — Grixis integration (#59–#63) and the generalized method
    "EDH Deck Template.md": ("edh", ["template", "blueprint", "swap-ledger", "methodology"], [62, 81, 96], None, ["grixis-repo", "cr"]),
    "EDH Deck Evaluation Checklist.md": ("edh", ["checklist", "evaluation", "brackets", "methodology"], [62, 81, 96], None, ["grixis-repo", "cr", "scryfall", "spellbook"]),
    "grixis/README.md": ("edh", ["grixis", "decks", "index"], [59, 60, 61], "scripts/build_grixis.py", ["grixis-repo", "scryfall", "spellbook"]),
    "grixis/Grixis Evaluation.md": ("edh", ["grixis", "validation", "legality"], [59], "scripts/build_grixis.py", ["grixis-repo", "scryfall"]),
    "grixis/Grixis Corrections.md": ("edh", ["grixis", "corrections", "legality", "oracle"], [60], "scripts/build_grixis.py", ["grixis-repo", "scryfall", "spellbook"]),
    "grixis/Grixis Packages.md": ("edh", ["grixis", "packages", "rules-insights"], [61], "scripts/build_grixis.py", ["grixis-repo", "scryfall", "cr"]),
    # Bot cycle 17 — Phase 5 optimization pass (#65–#68)
    "EDH Bracket Calibration.md": ("edh", ["brackets", "calibration", "game-changers", "combos", "pilot-notes"], [68, 95], "scripts/deck_calibration.py", ["scryfall", "spellbook", "edhrec", "wotc-articles"]),
    "Front-Matter Schema.md": ("meta", ["schema", "front-matter", "tags", "retrieval"], [65], "scripts/front_matter.py", []),
    # Bot cycle 31 — Phase 7 lore optimization pass (#92–#96)
    "Lore Entry Index.md": ("lore", ["lore", "index", "entries", "retrieval"], [92, 94], "scripts/build_lore_index.py", ["wizards-story"]),
    "grixis/Grixis Integration Summary.md": ("meta", ["grixis", "summary", "follow-ups"], [59, 60, 61, 62, 63], None, ["grixis-repo"]),
}
INDEX_ONLY = {"Lore Entry Index.md", "Card Enrichment.md"}  # generated hub that links every lore page; never counted as another page's "related"
SUBDIRS = ["grixis"]  # sub-folders whose .md pages must be registered (decks/ folders are handled as decks)
DECK_DIRS = ["decks", "grixis/decks"]
SHARD_DIR = "cards"
REF_DIR = "references"  # reverse card index (Bot cycle 18, #66; scripts/build_crossrefs.py)
SCHEMA_PAGE = "Front-Matter Schema.md"
# key: (type, required, meaning)
SCHEMA = {
    "page": {
        "title": ("string", True, "The page's H1 heading, quoted."),
        "category": ("enum: " + "/".join(sorted(CATEGORIES)), True, "Top-level area of the knowledge base."),
        "tags": ("list of tags", True, "Lower-case kebab-case topic tags (vocabulary below)."),
        "issues": ("list of int", True, "GitHub issues that created or own the page ([] if none)."),
        "generated_by": ("script path or `hand-written`", True, "Generator to re-run instead of hand-editing."),
        "sources": ("list of source keys", True, "Where the facts come from (source keys below)."),
        "related": ("list of page paths", True, "Up to 6 most strongly linked registered pages (links in + out; meta pages excluded for non-meta pages). Computed."),
        "entry_kind": ("enum: arc/summary/era/dossier/character/plane/item/retcon", False, "Lore entry pages only (Bot cycle 31, #92): what each entry on the page is (see scripts/lore_lib.py ENTRY_PAGES)."),
        "entries": ("int", False, "Lore entry pages only: number of entries on the page (indexed in data/lore_entries.json and Lore Entry Index.md)."),
        "schema": ("int", True, f"Front-matter schema version (currently {SCHEMA_VERSION})."),
    },
    "deck": {
        "title": ("string", True, "The deck page's H1 heading."),
        "category": ("`deck`", True, "Always `deck`."),
        "kind": ("enum: core/plane/theme/grixis/lore", True, "core = EDHREC skeleton; plane = plane-restricted; theme = EDHREC theme page; grixis = imported from the Grixis repo; lore = story-first lore-themed (Bot cycle 21)."),
        "commander": ("string", True, "First commander's Scryfall name."),
        "color_identity": ("WUBRG-ordered letters or `C`", True, "Commander color identity (CR 903.4), always in WUBRG order."),
        "bracket_floor": ("int 1–5", True, "Minimum bracket by the published barometers (Game Changers, MLD, two-card infinites)."),
        "game_changers": ("int", True, "Number of official Game Changers in the 100."),
        "combos": ("int", True, "Complete Commander Spellbook combos in the list."),
        "two_card_infinites": ("int", True, "Two-card infinite combos among them."),
        "validated": ("bool", True, "All hard checks pass (legality, identity, 100 cards, singleton)."),
        "tags": ("list of tags", True, "Computed: kind, identity name, `bracket-floor-N`, Game Changer and combo flags, plane/theme."),
        "plane": ("string", False, "Plane-restricted decks only."),
        "theme": ("string", False, "Theme decks only (EDHREC theme)."),
        "lore_score": ("float 0–100", False, "Lore decks only (Bot cycle 23): % of non-basic cards (commander + non-lands + non-basic lands) that are story-linked."),
        "lore_standard_met": ("bool", False, "Lore decks only: lore_score ≥ 85 (the Lore-Themed Deckbuilding standard; enforced by `build_lore_decks.py --check`)."),
        "source_repo": ("string", False, "Grixis decks only: the read-only source repository."),
        "legality_status": ("enum: pending", False, "Bot cycle 38: present only on decks published before some cards are Commander-legal (data/grixis_pending.json). validate_all accepts the listed cards only while legal_from is in the future."),
        "legal_from": ("date YYYY-MM-DD", False, "Pending decks only: the date Scryfall gives for the not-yet-legal cards' set release."),
        "pending_cards": ("list of card names", False, "Pending decks only: the cards that are not Commander-legal yet."),
        "schema": ("int", True, f"Front-matter schema version (currently {SCHEMA_VERSION})."),
    },
    "reference": {
        "title": ("string", True, "The page's H1 (`Reverse card index — L`)."),
        "category": ("`cards`", True, "Always `cards`."),
        "kind": ("`reference`", True, "Always `reference`."),
        "letter": ("string", True, "Card-shard letter folder the page mirrors (`index` for references/README.md)."),
        "cards": ("int", True, "Number of cited cards listed on the page."),
        "generated_by": ("`scripts/build_crossrefs.py`", True, "Never hand-edited."),
        "tags": ("list of tags", True, "Always `[reverse-index, cross-references]`."),
        "schema": ("int", True, f"Front-matter schema version (currently {SCHEMA_VERSION})."),
    },
    "shard": {
        "title": ("string", True, "The shard's H1 (`Cards — `prefix``)."),
        "category": ("`cards`", True, "Always `cards`."),
        "kind": ("`shard`", True, "Always `shard`."),
        "prefix": ("string", True, "Shard key prefix (see Card Data Conventions → Storage layout)."),
        "cards": ("int", True, "Number of card entries in the shard."),
        "bulk": ("date", True, "Scryfall Oracle bulk date the entries were rendered from."),
        "generated_by": ("`scripts/ingest_scryfall.py`", True, "Shards are never hand-edited."),
        "tags": ("list of tags", True, "Always `[card-entries, oracle, rulings]`."),
        "schema": ("int", True, f"Front-matter schema version (currently {SCHEMA_VERSION})."),
    },
}
FM = re.compile(r"\A---\n.*?\n---\n\n?", re.S)
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")


def ylist(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def body_of(text):
    return FM.sub("", text, count=1)


def h1(body, default):
    return next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), default)


def wubrg(letters):
    return "".join(c for c in COLOR_ORDER if c in letters) or "C"


# ------------------------------------------------------------------ related pages (link graph)
_REL = None


def related_map():
    """{page: [up to 6 related pages]} from links between registered pages (weight = links out + links in)."""
    global _REL
    if _REL is not None:
        return _REL
    w = defaultdict(Counter)
    for name in PAGES:
        p = ROOT / name
        if not p.exists():
            continue
        for t in LINK.findall(body_of(p.read_text(encoding="utf-8"))):
            if re.match(r"^[a-z]+:", t):
                continue
            path = t.partition("#")[0]
            if not path:
                continue
            try:
                dest = str((p.parent / unquote(path)).resolve().relative_to(ROOT))
            except ValueError:
                continue
            if dest in PAGES and dest != name:
                w[name][dest] += 1
                w[dest][name] += 1
    _REL = {}
    for name in PAGES:
        meta = PAGES[name][0] == "meta"
        cands = [(n, k) for k, n in w[name].items() if (meta or PAGES[k][0] != "meta") and k not in INDEX_ONLY]
        cands.sort(key=lambda x: (-x[0], x[1]))
        _REL[name] = [k for _, k in cands[:6]]
    return _REL


# ------------------------------------------------------------------ builders
def page_fm(path, body):
    rel = str(path.relative_to(ROOT))
    cat, tags, issues, gen, src = PAGES[rel]
    related = ", ".join(q(r) for r in related_map()[rel])
    lines = ["---", f"title: {q(h1(body, path.stem))}", f"category: {cat}", f"tags: {ylist(tags)}",
             f"issues: {ylist(issues)}", f"generated_by: {gen or 'hand-written'}", f"sources: {ylist(src)}",
             f"related: [{related}]"]
    if rel in lore_lib.ENTRY_PAGES:  # Bot cycle 31 (#92): lore entry pages carry their entry kind and count
        lines += [f"entry_kind: {lore_lib.ENTRY_PAGES[rel][0]}", f"entries: {len(lore_lib.entries(rel))}"]
    return "\n".join(lines + [f"schema: {SCHEMA_VERSION}", "---", ""])


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def deck_fields(path, body):
    title = h1(body, path.stem)
    cmd = re.search(r"^- \*\*\[([^\]]+)\]", body, re.M)
    ci = re.search(r"^- Color identity: \*\*([A-Z]+|C|Colorless)", body, re.M)
    fl = re.search(r"Minimum bracket by the published barometers: (\d)", body)
    floor = int(fl.group(1)) if fl else None
    imp = re.search(r"\*\*Bracket implication:\*\*.*?\*\*Bracket (\d)\+\*\*", body)
    if imp and floor is not None:
        floor = max(floor, int(imp.group(1)))
    cal = re.search(r"\*\*Calibrated floor: Bracket (\d)\*\*", body)  # Bot cycle 19 calibration block, if present
    if cal and floor is not None:
        floor = max(floor, int(cal.group(1)))
    gc = re.search(r"^- Game Changers \((\d+)\)", body, re.M)
    gcn = int(gc.group(1)) if gc else (0 if re.search(r"no Game Changers", body) else None)
    cb = re.search(r"\*\*(\d+) complete combo\(s\); (\d+) two-card infinite", body)
    kind = ("grixis" if path.parent.parent.name == "grixis" else "plane" if path.name.startswith("plane-")
            else "theme" if path.name.startswith("theme-") else "lore" if path.name.startswith("lore-") else "core")
    ident = None if not ci else ("C" if ci.group(1) in ("C", "Colorless") else wubrg(ci.group(1)))
    f = {"title": title, "kind": kind, "commander": cmd.group(1) if cmd else None, "color_identity": ident,
         "bracket_floor": floor, "game_changers": gcn, "combos": int(cb.group(1)) if cb else 0,
         "two_card_infinites": int(cb.group(2)) if cb else 0, "validated": "✅ **all checks pass**" in body}
    if kind == "plane":
        f["plane"] = path.stem.split("-")[1]
    if kind == "lore":
        ls = re.search(r"\*\*Story-linked: \d+ / \d+ non-basic cards \(([\d.]+)%\)\*\*", body)
        f["lore_score"] = float(ls.group(1)) if ls else None
    if kind == "theme":
        m = re.search(r"— ([^—]+?) theme$", title)
        f["theme"] = slug(m.group(1)) if m else None
    tags = [kind]
    if ident:
        tags.append(IDENTITY_NAMES.get(ident, slug(ident)))
    if floor is not None:
        tags.append(f"bracket-floor-{floor}")
    tags.append("game-changers" if gcn else "no-game-changers")
    if f["two_card_infinites"]:
        tags.append("two-card-infinite")
    elif f["combos"]:
        tags.append("combos")
    pend = re.search(r"PENDING LEGALITY — not Commander-legal yet\.\*\* Legal from \*\*(\d{4}-\d{2}-\d{2})\*\*.*?Not-yet-legal cards: (.*?)\. This page", body)
    if pend:  # Bot cycle 38: pending-legality banner written by scripts/build_grixis.py
        f.update(legality_status="pending", legal_from=pend.group(1), pending_cards=re.findall(r"\*\*(.+?)\*\*", pend.group(2)))
        tags.append("pending-legality")
    if f.get("plane"):
        tags.append(f"plane-{f['plane']}")
    if f.get("theme"):
        tags.append(f"theme-{f['theme']}")
    f["tags"] = tags
    return f


def deck_fm(path, body):
    f = deck_fields(path, body)
    nv = lambda v: "null" if v is None else v
    lines = ["---", f"title: {q(f['title'])}", "category: deck", f"kind: {f['kind']}",
             f"commander: {q(f['commander']) if f['commander'] else 'null'}", f"color_identity: {nv(f['color_identity'])}",
             f"bracket_floor: {nv(f['bracket_floor'])}", f"game_changers: {nv(f['game_changers'])}",
             f"combos: {f['combos']}", f"two_card_infinites: {f['two_card_infinites']}",
             f"validated: {'true' if f['validated'] else 'false'}", f"tags: {ylist(f['tags'])}"]
    if f["kind"] == "plane":
        lines.append(f"plane: {f['plane']}")
    if f["kind"] == "theme":
        lines.append(f"theme: {nv(f['theme'])}")
    if f["kind"] == "lore":
        lines.append(f"lore_score: {nv(f['lore_score'])}")
        lines.append(f"lore_standard_met: {'true' if (f['lore_score'] or 0) >= 85 else 'false'}")
    if f["kind"] == "grixis":
        lines.append("source_repo: corymstover/grixis-commander-encyclopediaGPT")
    if f.get("legality_status"):
        lines += [f"legality_status: {f['legality_status']}", f"legal_from: {f['legal_from']}", f"pending_cards: {ylist([q(c) for c in f['pending_cards']])}"]
    lines += [f"schema: {SCHEMA_VERSION}", "---", ""]
    return "\n".join(lines)


def shard_fm(path, body):
    title = h1(body, path.stem)
    n = re.search(r"^\*\*(\d+) cards? in this shard\.\*\*", body, re.M)
    b = re.search(r"Scryfall Oracle bulk data \((\d{4}-\d{2}-\d{2})\)", body)
    return "\n".join(["---", f"title: {q(title)}", "category: cards", "kind: shard", f"prefix: {path.stem}",
                      f"cards: {n.group(1) if n else 'null'}", f"bulk: {b.group(1) if b else 'null'}",
                      "generated_by: scripts/ingest_scryfall.py", "tags: [card-entries, oracle, rulings]",
                      f"schema: {SCHEMA_VERSION}", "---", ""])


def ref_fm(path, body):
    n = re.search(r"^\*\*([\d,]+) cards\b", body, re.M)
    return "\n".join(["---", f"title: {q(h1(body, path.stem))}", "category: cards", "kind: reference",
                      f"letter: {'index' if path.name == 'README.md' else path.stem}",
                      f"cards: {n.group(1).replace(',', '') if n else 'null'}", "generated_by: scripts/build_crossrefs.py",
                      "tags: [reverse-index, cross-references]", f"schema: {SCHEMA_VERSION}", "---", ""])


def targets(shards=True):
    for name in sorted(PAGES):
        p = ROOT / name
        if p.exists():
            yield p, page_fm, "page"
    for d in DECK_DIRS:
        for p in sorted((ROOT / d).glob("*.md")):
            yield p, deck_fm, "deck"
    for p in sorted((ROOT / REF_DIR).glob("*.md")):
        yield p, ref_fm, "reference"
    if shards:
        for p in sorted((ROOT / SHARD_DIR).rglob("*.md")):
            if p.name != "README.md":
                yield p, shard_fm, "shard"


# ------------------------------------------------------------------ typed validation
def parse_fm(block):
    out = {}
    for line in block.strip().strip("-").strip().splitlines():
        k, _, v = line.partition(": ")
        out[k.strip()] = v.strip()
    return out


def as_list(v):
    if not (v.startswith("[") and v.endswith("]")):
        return None
    return [a if a else b.strip() for a, b in re.findall(r'"((?:[^"\\]|\\.)*)"|([^,\s][^,]*)', v[1:-1])]


def type_errors(kind, d):
    errs = []
    for k, (typ, req, _) in SCHEMA[kind].items():
        if k not in d:
            if req:
                errs.append(f"missing {k}")
            continue
        v = d[k]
        if v == "null":
            errs.append(f"unparsed field {k} (null)")
            continue
        if typ.startswith("list"):
            xs = as_list(v)
            if xs is None:
                errs.append(f"{k} is not a list")
            elif typ == "list of tags":
                errs += [f"tag not kebab-case: {t}" for t in xs if not TAG_RX.match(t)]
            elif typ == "list of int" and not all(x.isdigit() for x in xs):
                errs.append(f"{k} has non-integer items")
            elif typ == "list of source keys":
                errs += [f"unknown source key: {x}" for x in xs if x not in SOURCES]
            elif typ == "list of page paths":
                errs += [f"related page not registered: {x}" for x in xs if x not in PAGES]
        elif typ in ("int", "int 1–5") and not v.isdigit():
            errs.append(f"{k} is not an int")
        elif typ == "int 1–5" and not 1 <= int(v) <= 5:
            errs.append(f"{k} out of range")
        elif typ == "bool" and v not in ("true", "false"):
            errs.append(f"{k} is not a bool")
        elif typ.startswith("enum") and v not in typ.split(": ", 1)[1].split("/"):
            errs.append(f"{k} not in enum: {v}")
        elif typ.startswith("WUBRG") and v != "C" and v != wubrg(v):
            errs.append(f"{k} not in WUBRG order: {v}")
        elif typ.startswith("script path") and v != "hand-written" and not (ROOT / v).exists():
            errs.append(f"{k} script missing: {v}")
    extra = set(d) - set(SCHEMA[kind])
    if extra:
        errs.append(f"keys not in schema: {sorted(extra)}")
    return errs


# ------------------------------------------------------------------ schema page
def schema_page():
    tagpages = defaultdict(list)
    for name, (cat, tags, *_r) in PAGES.items():
        for t in tags:
            tagpages[t].append(name)
    decktags = Counter()
    for d in DECK_DIRS:
        for p in (ROOT / d).glob("*.md"):
            m = FM.match(p.read_text(encoding="utf-8"))
            if m:
                for t in as_list(parse_fm(m.group(0)).get("tags", "[]")) or []:
                    decktags[t] += 1
    n_sh = sum(1 for p in (ROOT / SHARD_DIR).rglob("*.md") if p.name != "README.md")
    n_deck = sum(1 for d in DECK_DIRS for _ in (ROOT / d).glob("*.md"))
    n_ref = sum(1 for _ in (ROOT / REF_DIR).glob("*.md"))
    L = ["# Front-Matter Schema", "",
         f"> **Auto-generated** by `scripts/front_matter.py` (Bot cycle 17, issue [#65]({I}65)) from the `SCHEMA` and `PAGES` tables in the script, so this page cannot drift from what `--check` enforces. Schema version **{SCHEMA_VERSION}**. Do not hand-edit.",
         f"> Coverage: **{len(PAGES)}** registered pages (README.md and GOAL.md are exempt), **{n_deck}** decks, **{n_sh}** card shards, **{n_ref}** reverse-index pages. Related: [Lookup Guide](Lookup%20Guide.md) · [Knowledge Index](Knowledge%20Index.md) · [Card Data Conventions](Card%20Data%20Conventions.md).", "",
         "## Contents", "- [Format](#format)", "- [Page keys](#page-keys)", "- [Deck keys](#deck-keys)", "- [Card-shard keys](#card-shard-keys)", "- [Reverse-index keys](#reverse-index-keys)",
         "- [Source keys](#source-keys)", "- [Tag vocabulary](#tag-vocabulary)", "- [Validation rules](#validation-rules)", "- [Filtering examples](#filtering-examples)", "",
         "## Format", "",
         "Every entry starts with a YAML block between `---` lines. Values are flat: strings (quoted when free text), ints, `true`/`false`, and inline lists `[a, b]`. "
         "This flat subset is readable by any YAML parser and by `rg` line matching. README.md and GOAL.md are exempt.", ""]
    for kind, head in (("page", "Page keys"), ("deck", "Deck keys"), ("shard", "Card-shard keys"), ("reference", "Reverse-index keys")):
        L += [f"## {head}", "", "| Key | Type | Required | Meaning |", "|---|---|---|---|"]
        for k, (typ, req, mean) in SCHEMA[kind].items():
            L.append(f"| `{k}` | {typ} | {'yes' if req else 'when applicable'} | {mean} |")
        L.append("")
    L += ["Example (deck):", "", "```yaml", deck_fm(ROOT / "grixis/decks/cult-of-skaro.md",
          body_of((ROOT / "grixis/decks/cult-of-skaro.md").read_text(encoding="utf-8"))).rstrip(), "```", ""]
    L += ["## Source keys", "", "| Key | Meaning |", "|---|---|"] + [f"| `{k}` | {v} |" for k, v in SOURCES.items()] + [""]
    L += ["## Tag vocabulary", "", "Tags are lower-case kebab-case (`^[a-z0-9+]+(-[a-z0-9+]+)*$`). Page tags are assigned in the `PAGES` registry; deck tags are computed from the deck body.", "",
          "### Page tags", "", "| Tag | Pages |", "|---|---|"]
    for t in sorted(tagpages):
        L.append(f"| `{t}` | " + " · ".join(f"[{Path(n).stem}]({urlq(n)})" for n in sorted(tagpages[t])) + " |")
    L += ["", "### Deck tags", "", "| Tag | Decks |", "|---|---|"] + [f"| `{t}` | {n} |" for t, n in sorted(decktags.items())] + [""]
    L += ["## Validation rules", "", "`python3 scripts/front_matter.py --check` (also step 2 of `scripts/validate_all.py`) fails when:",
          "- an entry has no front-matter, a required key is missing, a key is not in the schema, or a value is `null` (unparsed);",
          "- a value has the wrong type (int, bool, list, enum, WUBRG order, unknown source key, unregistered related page, missing generator script);",
          "- a tag is not kebab-case;",
          "- the stored block differs from what the script computes now (stale — re-run `python3 scripts/front_matter.py`);",
          "- a top-level or `grixis/` page is not in the registry, or this schema page is stale.", "",
          "## Filtering examples", "", "| I want… | Command |", "|---|---|",
          "| All lore pages | `rg -l '^category: lore' *.md` |",
          "| Lore pages made of entries, with counts | `rg -n '^entries: ' *.md` |",
          "| Every lore entry flagged ❓ unknown | `python3 scripts/kb_find.py --tag has-unknowns --category lore` |",
          "| Dossiers/characters whose spark is lost | `python3 scripts/kb_find.py --tag spark-lost` |",
          "| Pages about brackets | `rg -l '^tags: .*\\bbrackets\\b' *.md grixis/*.md` |",
          "| Pages related to Rules Interactions | `rg -l '^related: .*Rules Interactions' *.md` |",
          "| Decks with a two-card infinite | `rg -l '^tags: .*two-card-infinite' decks grixis/decks` |",
          "| Grixis-identity decks anywhere | `rg -l '^color_identity: UBR$' decks grixis/decks` |",
          "| Decks at bracket floor 2 | `rg -l '^bracket_floor: 2' decks grixis/decks` |",
          "| Card shards rendered from an older bulk | `rg -L '^bulk: 2026-10-15' -g '*.md' cards` |", ""]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ main
def apply_shards():
    """Called by ingest_scryfall.py after it rewrites the shards."""
    n = 0
    for p in sorted((ROOT / SHARD_DIR).rglob("*.md")):
        if p.name == "README.md":
            continue
        text = p.read_text(encoding="utf-8")
        body = body_of(text)
        new = shard_fm(p, body) + "\n" + body.lstrip("\n")
        if new != text:
            p.write_text(new, encoding="utf-8")
        n += 1
    return n


def main(check: bool, shards: bool = True) -> int:
    global _REL
    bad, n = [], 0
    missing = [name for name in PAGES if not (ROOT / name).exists()]
    items = list(targets(shards))
    if not check:  # decks and shards first, then the schema page (reads deck tags), then pages (related reads all links)
        sp = ROOT / SCHEMA_PAGE
        order = [t for t in items if t[2] != "page"]
        for p, fn, kind in order:
            text = p.read_text(encoding="utf-8")
            body = body_of(text)
            new = fn(p, body) + "\n" + body.lstrip("\n")
            if new != text:
                p.write_text(new, encoding="utf-8")
        sp.write_text(schema_page(), encoding="utf-8")
        _REL = None
        missing = [name for name in PAGES if not (ROOT / name).exists()]
        items = [t for t in targets(False) if t[2] == "page"]
        n = len(order)
    for p, fn, kind in items:
        text = p.read_text(encoding="utf-8")
        body = body_of(text)
        want = fn(p, body)
        n += 1
        rel = p.relative_to(ROOT)
        if check:
            m = FM.match(text)
            if not m:
                bad.append(f"{rel}: no front-matter")
                continue
            got = m.group(0)
            bad += [f"{rel}: {e}" for e in type_errors(kind, parse_fm(got))]
            if got.strip() != want.strip():
                bad.append(f"{rel}: front-matter out of date (re-run scripts/front_matter.py)")
            if p.name == SCHEMA_PAGE and body.strip() != schema_page().strip():
                bad.append(f"{rel}: schema page stale (re-run scripts/front_matter.py)")
        else:
            new = want + "\n" + body.lstrip("\n")
            if new != text:
                p.write_text(new, encoding="utf-8")
    if missing:
        bad.append(f"registry lists missing pages: {missing}")
    unreg = [p.name for p in ROOT.glob("*.md") if p.name not in PAGES and p.name not in ("README.md", "GOAL.md")]
    unreg += [str(p.relative_to(ROOT)) for d in SUBDIRS for p in (ROOT / d).glob("*.md") if str(p.relative_to(ROOT)) not in PAGES]
    if unreg:
        bad.append(f"top-level pages not in the registry: {unreg}")
    print(f"front-matter: {'checked' if check else 'wrote'} {n} files (schema v{SCHEMA_VERSION}), {len(bad)} problems")
    for b in bad[:30]:
        print("  " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv, "--no-shards" not in sys.argv))
