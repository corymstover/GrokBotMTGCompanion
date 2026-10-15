#!/usr/bin/env python3
"""Apply or check YAML front-matter on major pages and deck files (issue #44, Bot cycle 15).

Front-matter makes pages filterable with plain text tools, e.g.
  rg -l '^category: lore' *.md        rg -l '^bracket_floor: 4' decks/
Generators rewrite their pages, so re-run this after any generator (README cycle commands).
  python3 scripts/front_matter.py           apply (idempotent; replaces existing front-matter)
  python3 scripts/front_matter.py --check   exit 1 if a page or deck is missing front-matter or a required key
README.md and GOAL.md are left untouched: README is the dashboard and GOAL is the user's own file.
Deck fields are parsed from each deck's Commander and Bracket sections, so they always match the file body.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I = "https://github.com/corymstover/GrokBotMTGCompanion/issues/"
CATEGORIES = {"lore", "edh", "rules", "cards", "meta"}
# file: (category, tags, issues, generator or None, sources)
PAGES = {
    "Art & Flavor Story Links.md": ("lore", ["art", "flavor", "story-spotlight"], [37], "scripts/build_art_flavor.py", ["scryfall", "wizards-story"]),
    "Artist Index.md": ("cards", ["artists", "art-credits"], [43], "scripts/build_artists.py", ["scryfall"]),
    "Card Data Conventions.md": ("meta", ["conventions", "card-entries"], [], None, ["scryfall"]),
    "Card Index.md": ("cards", ["index", "coverage"], [1, 2, 5], "scripts/ingest_scryfall.py", ["scryfall"]),
    "Characters Index.md": ("lore", ["characters", "status", "planeswalkers"], [7, 11, 20], None, ["wizards-story"]),
    "Conflicts & Arcs.md": ("lore", ["arcs", "conflicts"], [7, 13, 34], None, ["wizards-story"]),
    "EDH Archetypes.md": ("edh", ["archetypes", "strategy"], [16, 19], "scripts/build_archetypes.py", ["scryfall", "edhrec", "spellbook"]),
    "EDH Interaction.md": ("edh", ["removal", "interaction", "stax"], [28], "scripts/build_interaction.py", ["scryfall", "edhrec"]),
    "EDH Mana Bases.md": ("edh", ["lands", "mana-base", "color-identity"], [25], "scripts/build_mana_bases.py", ["scryfall", "edhrec"]),
    "EDH Mulligans.md": ("edh", ["mulligan", "opening-hand"], [31], "scripts/build_mulligans.py", ["cr", "scryfall"]),
    "EDH Packages.md": ("edh", ["packages", "ramp", "card-advantage"], [26], "scripts/build_packages.py", ["scryfall", "edhrec"]),
    "EDH Pairings.md": ("edh", ["partner", "background", "pairings"], [32], "scripts/build_pairings.py", ["cr", "scryfall"]),
    "EDH Standards.md": ("edh", ["deckbuilding-rules", "color-identity", "brackets"], [6], None, ["cr", "wotc-articles"]),
    "EDH Staples.md": ("edh", ["staples", "color-identity"], [], "scripts/build_staples.py", ["scryfall", "edhrec"]),
    "EDH Themed Decks.md": ("edh", ["decks", "plane-restricted", "themes"], [33], "scripts/build_themed_index.py", ["scryfall", "edhrec"]),
    "EDH Upgrade Paths.md": ("edh", ["upgrades", "budget"], [30], "scripts/build_upgrade_paths.py", ["scryfall", "edhrec"]),
    "EDH Win Conditions.md": ("edh", ["win-conditions", "combos"], [27], "scripts/build_wincons.py", ["scryfall", "spellbook"]),
    "FAQ.md": ("meta", ["faq", "lore", "rules"], [45], None, ["cr", "wizards-story", "scryfall"]),
    "Format Legality Matrix.md": ("cards", ["legality", "formats", "banned-restricted"], [41], "scripts/build_legality.py", ["scryfall", "wotc-articles"]),
    "Keyword Encyclopedia.md": ("rules", ["keywords", "evergreen", "rulings"], [39], "scripts/build_keywords.py", ["cr", "scryfall", "wotc-articles"]),
    "Knowledge Index.md": ("meta", ["index", "maintenance"], [], None, []),
    "Knowledge Snapshots.md": ("meta", ["tags", "releases", "snapshots"], [47], None, []),
    "Lookup Guide.md": ("meta", ["lookup", "retrieval"], [46], None, []),
    "Master Timeline.md": ("lore", ["timeline", "eras"], [7], None, ["wizards-story"]),
    "Omenpath & Multiverse Connections.md": ("lore", ["omenpaths", "multiverse", "planes"], [36], None, ["wizards-story"]),
    "Planes Index.md": ("lore", ["planes"], [7, 12], None, ["wizards-story"]),
    "Planeswalker Dossiers.md": ("lore", ["planeswalkers", "dossiers", "sparks"], [35], None, ["wizards-story"]),
    "Printing History.md": ("cards", ["printings", "reprints", "reserved-list"], [40], "scripts/build_printings.py", ["scryfall", "wotc-articles"]),
    "Progress Tracker.md": ("meta", ["progress", "milestones"], [], None, []),
    "ROADMAP.md": ("meta", ["roadmap", "sprint"], [], None, []),
    "Rules Interactions.md": ("rules", ["rules", "interactions", "rulings"], [9], "scripts/build_rules_interactions.py", ["cr", "scryfall"]),
    "Side-Media Index.md": ("lore", ["novels", "comics", "side-media"], [38], None, ["wizards-story", "wotc-articles"]),
    "Story Arc Summaries.md": ("lore", ["arcs", "story-beats"], [34], None, ["wizards-story"]),
    "Story Archive Index.md": ("lore", ["story-archive", "sources"], [14], "scripts/crawl_story_index.py", ["wizards-story"]),
    "Tokens, Emblems & Dungeons.md": ("cards", ["tokens", "emblems", "dungeons", "not-cards"], [42], "scripts/build_tokens.py", ["scryfall", "cr"]),
    "Update Log.md": ("meta", ["changelog"], [], None, []),
    "cEDH Primer.md": ("edh", ["cedh", "competitive", "bracket-5"], [29], "scripts/build_cedh.py", ["scryfall", "spellbook"]),
    # Bot cycle 16 — Grixis integration (#59–#63) and the generalized method
    "EDH Deck Template.md": ("edh", ["template", "blueprint", "swap-ledger", "methodology"], [62], None, ["grixis-repo", "cr"]),
    "EDH Deck Evaluation Checklist.md": ("edh", ["checklist", "evaluation", "brackets", "methodology"], [62], None, ["grixis-repo", "cr", "scryfall", "spellbook"]),
    "grixis/README.md": ("edh", ["grixis", "decks", "index"], [59, 60, 61], "scripts/build_grixis.py", ["grixis-repo", "scryfall", "spellbook"]),
    "grixis/Grixis Evaluation.md": ("edh", ["grixis", "validation", "legality"], [59], "scripts/build_grixis.py", ["grixis-repo", "scryfall"]),
    "grixis/Grixis Corrections.md": ("edh", ["grixis", "corrections", "legality", "oracle"], [60], "scripts/build_grixis.py", ["grixis-repo", "scryfall", "spellbook"]),
    "grixis/Grixis Packages.md": ("edh", ["grixis", "packages", "rules-insights"], [61], "scripts/build_grixis.py", ["grixis-repo", "scryfall", "cr"]),
    "grixis/Grixis Integration Summary.md": ("meta", ["grixis", "summary", "follow-ups"], [59, 60, 61, 62, 63], None, ["grixis-repo"]),
}
SUBDIRS = ["grixis"]  # sub-folders whose .md pages must be registered (decks/ folders are handled as decks)
DECK_DIRS = ["decks", "grixis/decks"]
PAGE_KEYS = ["title", "category", "tags", "issues", "generated_by", "sources"]
DECK_KEYS = ["title", "category", "kind", "commander", "color_identity", "bracket_floor", "game_changers", "validated"]
FM = re.compile(r"\A---\n.*?\n---\n\n?", re.S)


def ylist(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def body_of(text):
    return FM.sub("", text, count=1)


def page_fm(path, body):
    cat, tags, issues, gen, src = PAGES[str(path.relative_to(ROOT))]
    h1 = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), path.stem)
    return "\n".join(["---", f"title: {q(h1)}", f"category: {cat}", f"tags: {ylist(tags)}",
                      f"issues: {ylist(issues)}", f"generated_by: {gen or 'hand-written'}", f"sources: {ylist(src)}", "---", ""])


def deck_fm(path, body):
    h1 = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), path.stem)
    cmd = re.search(r"^- \*\*\[([^\]]+)\]", body, re.M)
    ci = re.search(r"^- Color identity: \*\*([A-Z]+|C|Colorless)", body, re.M)
    fl = re.search(r"Minimum bracket by the published barometers: (\d)", body)
    floor = int(fl.group(1)) if fl else None
    imp = re.search(r"\*\*Bracket implication:\*\*.*?\*\*Bracket (\d)\+\*\*", body)
    if imp and floor is not None:
        floor = max(floor, int(imp.group(1)))
    gc = re.search(r"^- Game Changers \((\d+)\)", body, re.M)
    gcn = int(gc.group(1)) if gc else (0 if re.search(r"no Game Changers", body) else None)
    kind = ("grixis" if path.parent.parent.name == "grixis" else "plane" if path.name.startswith("plane-")
            else "theme" if path.name.startswith("theme-") else "core")
    ok = "✅ **all checks pass**" in body
    lines = ["---", f"title: {q(h1)}", "category: deck", f"kind: {kind}",
             f"commander: {q(cmd.group(1)) if cmd else 'null'}", f"color_identity: {ci.group(1) if ci else 'null'}",
             f"bracket_floor: {floor if floor is not None else 'null'}", f"game_changers: {gcn if gcn is not None else 'null'}",
             f"validated: {'true' if ok else 'false'}"]
    if kind == "plane":
        lines.append(f"plane: {path.stem.split('-')[1]}")
    if kind == "grixis":
        lines.append("source_repo: corymstover/grixis-commander-encyclopediaGPT")
    lines += ["---", ""]
    return "\n".join(lines)


def targets():
    for name in sorted(PAGES):
        p = ROOT / name
        if p.exists():
            yield p, page_fm, PAGE_KEYS
    for d in DECK_DIRS:
        for p in sorted((ROOT / d).glob("*.md")):
            yield p, deck_fm, DECK_KEYS


def main(check: bool) -> int:
    bad, n = [], 0
    missing = [name for name in PAGES if not (ROOT / name).exists()]
    for p, fn, keys in targets():
        text = p.read_text(encoding="utf-8")
        body = body_of(text)
        want = fn(p, body)
        n += 1
        if check:
            m = FM.match(text)
            if not m:
                bad.append(f"{p.relative_to(ROOT)}: no front-matter")
                continue
            got = m.group(0)
            for k in keys:
                if not re.search(rf"^{k}: ", got, re.M):
                    bad.append(f"{p.relative_to(ROOT)}: missing {k}")
            if "null" in got:
                bad.append(f"{p.relative_to(ROOT)}: unparsed field (null)")
            if got.strip() != want.strip():
                bad.append(f"{p.relative_to(ROOT)}: front-matter out of date (re-run scripts/front_matter.py)")
        else:
            p.write_text(want + "\n" + body.lstrip("\n"), encoding="utf-8")
    if missing:
        print("registry lists missing pages:", missing)
    unreg = [p.name for p in ROOT.glob("*.md") if p.name not in PAGES and p.name not in ("README.md", "GOAL.md")]
    unreg += [str(p.relative_to(ROOT)) for d in SUBDIRS for p in (ROOT / d).glob("*.md") if str(p.relative_to(ROOT)) not in PAGES]
    if unreg:
        bad.append(f"top-level pages not in the registry: {unreg}")
    if check:
        print(f"front-matter: checked {n} files, {len(bad)} problems")
        for b in bad[:30]:
            print("  " + b)
        return 1 if bad else 0
    print(f"front-matter: wrote {n} files")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
