#!/usr/bin/env python3
"""Generate "EDH Themed Decks.md" (Bot cycle 7, #33): an index of the plane-restricted (decks/plane-*.md) and themed
(decks/theme-*.md) deck outlines built by scripts/build_deck_skeleton.py --sets/--theme, with validation, bracket and combo data.
Usage: python3 scripts/build_themed_index.py"""
import json, re
import ingest_scryfall as ing

R = ing.ROOT
combos = json.loads((R / "data" / "combos.json").read_text())["decks"]


def info(p):
    t = p.read_text()
    g = lambda pat, d="—": (re.search(pat, t, re.M).group(1) if re.search(pat, t, re.M) else d)
    return {"title": g(r"^# Deck Skeleton — (.+)$"), "cmd": g(r"^- \*\*(\[.+?\]\(.+?\))\*\*"), "ci": g(r"Color identity: \*\*(.+?)\*\*"),
            "valid": "✅" if "all checks pass" in t else "❌", "gc": g(r"Game Changers \((\d+)\)"), "floor": g(r"Minimum bracket by the published barometers: (\d)"),
            "filler": g(r"(\d+) slots were filled", "0"), "sets": g(r"printing in sets `([^`]+)`", ""), "theme": g(r"EDHREC `([^`]+)` theme", "")}


def main():
    L = ["# EDH Themed & Plane-Restricted Decks", "",
         "> **Auto-generated** by `scripts/build_themed_index.py` (Bot cycle 7, issue [#33](https://github.com/corymstover/GrokBotMTGCompanion/issues/33)). Each deck is a 100-card **outline** built by `scripts/build_deck_skeleton.py` and checked the same way as every other deck in `decks/`: exact 100 cards, singleton, Commander-legal, strict color identity, the Game Changer bracket floor, Commander Spellbook combo detection, and a rules & rulings block.",
         "> **Plane-restricted** decks only use cards with a paper printing in that plane's main expansion sets (Scryfall set codes listed per deck; commander products and supplemental sets are excluded). When EDHREC's suggestions for the commander ran out on-plane, the remaining slots were filled with popular on-plane cards (**filler**). Filler is not tuned synergy, so review it (*Opinion*).",
         "> **Themed** decks use the commander's EDHREC theme page instead of its main page.", "",
         "## Contents", "- [Plane-restricted](#plane-restricted)", "- [Themed](#themed)", "- [Rebuild](#rebuild)", "",
         "## Plane-restricted", "", "| Deck | Commander | Identity | Sets | Valid | GC | Bracket floor | Filler slots | Spellbook combos (two-card ∞) |", "|---|---|---|---|---|---|---|---|---|"]
    rows = {"plane": [], "theme": []}
    for p in sorted((R / "decks").glob("plane-*.md")) + sorted((R / "decks").glob("theme-*.md")):
        i = info(p); c = combos.get(p.stem, {})
        kind = "plane" if p.stem.startswith("plane") else "theme"
        cmd = i["cmd"].replace("](../", "](")
        floor = "3 (two-card ∞)" if c.get("two_card_infinite") and i["floor"] in "12" else i["floor"]
        if kind == "plane":
            rows[kind].append(f"| [{i['title']}](decks/{p.name}) | {cmd} | {i['ci']} | `{i['sets']}` | {i['valid']} | {i['gc']} | {floor} | {i['filler']} / 63 | {len(c.get('combos', []))} ({c.get('two_card_infinite', 0)}) |")
        else:
            rows[kind].append(f"| [{i['title']}](decks/{p.name}) | {cmd} | {i['ci']} | `{i['theme']}` | {i['valid']} | {i['gc']} | {floor} | {len(c.get('combos', []))} ({c.get('two_card_infinite', 0)}) |")
    L += rows["plane"] + ["", "## Themed", "", "| Deck | Commander | Identity | EDHREC theme | Valid | GC | Bracket floor | Spellbook combos (two-card ∞) |", "|---|---|---|---|---|---|---|---|"] + rows["theme"]
    L += ["", "*Bracket floor* is the minimum bracket from the published barometers (Game Changers, MLD and extra turns). **3 (two-card ∞)** means the barometers alone give 1–2, but Commander Spellbook found a two-card infinite, so the deck is at least Bracket 3 as listed ([Brackets](EDH%20Standards.md#power-bracket-assessment)).", "",
          "## Rebuild", "", "```bash",
          'python3 scripts/build_deck_skeleton.py "The Gitrog Monster" --sets isd,dka,avr,soi,emn,mid,vow --plane Innistrad --out plane-innistrad-the-gitrog-monster',
          'python3 scripts/build_deck_skeleton.py "Atraxa, Praetors\' Voice" --theme planeswalkers --out theme-atraxa-praetors-voice-planeswalkers',
          "# …same pattern for every deck (set codes are listed in the table); then:",
          "python3 scripts/deck_rules_notes.py && python3 scripts/detect_combos.py && python3 scripts/build_themed_index.py", "```", ""]
    (R / "EDH Themed Decks.md").write_text("\n".join(L) + "\n")
    print("plane", len(rows["plane"]), "theme", len(rows["theme"]))


if __name__ == "__main__":
    main()
