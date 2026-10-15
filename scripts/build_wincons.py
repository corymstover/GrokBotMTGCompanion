#!/usr/bin/env python3
"""Generate "EDH Win Conditions.md" (Bot cycle 6, #27): a taxonomy of ways to win, with example and supporting cards.
Usage: python3 scripts/build_wincons.py"""
import json, re
from collections import Counter
from edh_lib import Data
import ingest_scryfall as ing

TAX = [
 ("Combat damage (go-wide)", "Win by attacking with many creatures. Rules: [combat damage](Rules%20Interactions.md#combat-damage-assignment).",
  [("Mass pump / overrun finishers", r"creatures you control get \+[X\d]+/\+[X\d]+ and gain trample until end of turn|creatures you control get \+X/\+X", dict(types=r"Instant|Sorcery")),
   ("Extra combat phases", r"additional combat phase", dict()),
   ("Haste enablers", r"creatures you control (have|gain) haste", dict())]),
 ("Commander damage (voltron)", "21 combat damage from one commander ([CR 903.10a](Rules%20Interactions.md#commander-damage)).",
  [("Double strike granters", r"(equipped|enchanted|target) creature (gets [^.]*and )?(has|gains) double strike", dict()),
   ("Unblockability", r"(equipped|enchanted|target) creature (gets [^.]*and )?(has|gains)?[^.]*can't be blocked", dict())]),
 ("Life drain & burn", "Drain or burn each opponent, often repeatedly. Link: [EDH Packages → Aristocrats](EDH%20Packages.md#aristocrats).",
  [("Repeatable drain", r"(whenever|at the beginning)[^.]*each opponent loses (\d+|X) life", dict(types=r"Creature|Enchantment|Artifact|Planeswalker")),
   ("X-burn / X-drain finishers", r"(each opponent loses X life|deals X damage to each opponent|each opponent loses life equal)", dict(types=r"Instant|Sorcery")),
   ("Damage doublers", r"would deal damage[^.]*(it deals double that damage|deals that much damage plus|twice that much)", dict())]),
 ("Alternate win cards", "Cards that say \"you win the game\".",
  [("\"You win the game\"", r"\byou win the game\b", dict())]),
 ("Opponents lose directly", "Effects that make players lose without damage.",
  [("\"loses the game\" effects", r"(target player|each opponent|that player|target opponent) loses the game", dict())]),
 ("Poison (infect / toxic)", "10 poison counters ([CR 704.5c](Rules%20Interactions.md#state-based-actions)).",
  [("Infect & toxic creatures", r"\b(infect|toxic \d+)\b", dict(types=r"Creature")),
   ("Proliferate finishers", r"\bproliferate\b", dict())]),
 ("Mill (decking)", "A player who draws from an empty library loses ([CR 704.5b](Rules%20Interactions.md#state-based-actions)).",
  [("Mass mill", r"(each opponent|target player|target opponent|each player) mills (X|half|\w+) cards|mills cards equal", dict())]),
 ("Protection for the winning turn", "Supporting pieces that keep the win from being answered.",
  [("Team protection", r"(permanents|creatures) you control (gain|have) (hexproof|indestructible|shroud|protection)|you and permanents you control (gain|phase)", dict(types=r"Instant|Sorcery|Creature|Artifact|Enchantment")),
   ("Counter-proofing", r"can't be countered|your opponents can't cast spells", dict())]),
]


def main():
    d = Data()
    L = d.header("EDH Win Conditions", "scripts/build_wincons.py", 27,
                 "Win-condition definitions come from the Comprehensive Rules (state-based actions 704.5a–c; commander damage 903.10a).")
    L += ["## Contents"] + [f"- [{t[0]}](#{re.sub(r'[^a-z0-9 -]', '', t[0].lower()).replace(' ', '-')})" for t in TAX] + ["- [Combo kills (Commander Spellbook)](#combo-kills-commander-spellbook)", "- [Choosing a win condition (guidance)](#choosing-a-win-condition-guidance)", ""]
    rows = 0
    for name, why, subs in TAX:
        L += [f"## {name}", "", f"**How it wins:** {why}", ""]
        for lab, pat, kw in subs:
            cs = d.find(pat, **kw); rows += min(10, len(cs))
            L += [f"### {lab}", "", f"Pattern: `{pat}` · {len(cs)} Commander-legal matches", ""] + d.table(cs, 10) + [""]
    # combos
    C = json.load(open(ing.ROOT / "data/combos.json"))
    cnt = Counter(); info = {}
    for deck, v in C["decks"].items():
        for c in v["combos"]:
            if c["n"] == 2 and c["infinite"]:
                cnt[c["id"]] += 1; info[c["id"]] = c
    L += ["## Combo kills (Commander Spellbook)", "",
          f"Two-card infinite combos found in this repo's 32 skeletons by the [Commander Spellbook](https://commanderspellbook.com) API (`data/combos.json`, {len(cnt)} distinct). ⚠️ Two-card infinites are outside Brackets 1–2, and at Bracket 3 they shouldn't come early ([EDH Standards](EDH%20Standards.md#power-bracket-assessment)).", "",
          "| Cards | Produces | Spellbook |", "|---|---|---|"]
    for cid, _ in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])):
        c = info[cid]
        cards = " + ".join(d.link(d.by_name[n]) if n in d.by_name else n for n in c["cards"])
        L.append(f"| {cards} | {', '.join(c['produces'][:3])} | [{cid}](https://commanderspellbook.com/combo/{cid}/) |")
    L += ["", "## Choosing a win condition (guidance)", "",
          "**Guidance (opinion):**",
          "- Have **two or three** routes to victory so that one graveyard wipe or counterspell doesn't stop you.",
          "- Match the route to the commander's engine. Token commanders want mass pump; aristocrats want drain; voltron commanders want evasion plus protection.",
          "- At Brackets 1–3, prefer combat or drain finishes. Disclose infinite combos in the pre-game talk ([brackets](EDH%20Standards.md#power-bracket-assessment)).",
          "- Count your protection pieces (see above) as part of the win condition.", "",
          "Related: [EDH Packages](EDH%20Packages.md) · [EDH Interaction](EDH%20Interaction.md) · [cEDH Primer](cEDH%20Primer.md) · [EDH Archetypes](EDH%20Archetypes.md)."]
    (ing.ROOT / "EDH Win Conditions.md").write_text("\n".join(L) + "\n")
    print("categories", len(TAX), "rows", rows, "combos", len(cnt))


if __name__ == "__main__":
    main()
