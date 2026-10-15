#!/usr/bin/env python3
"""Generate "EDH Interaction.md" (Bot cycle 6, #28): interaction & hate hierarchies, from Scryfall data.
Hierarchy = buckets ordered from most to least flexible (guidance); cards inside each bucket ordered by EDHREC rank.
Usage: python3 scripts/build_interaction.py"""
import re
from edh_lib import Data
import ingest_scryfall as ing

INST = r"Instant|Flash"


def inst(d, c):
    return bool(re.search(r"Instant", d.ftype(c))) or "Flash" in (c.get("keywords") or [])


H = [
 ("Targeted removal", "Most flexible first: any nonland permanent > two or more types > creature only. Instant speed and low mana value are better.", [
   ("Any permanent / nonland permanent", r"(destroy|exile) target (nonland )?permanent|(destroy|exile) target (artifact, creature, enchantment, or planeswalker|nonland permanent)", dict()),
   ("Artifact or enchantment", r"(destroy|exile) target (artifact or enchantment|artifact, enchantment|enchantment or artifact)", dict()),
   ("Creature", r"(destroy|exile) target creature\b(?! card)", dict(excl=r"you control")),
   ("Bounce (tempo)", r"return target (nonland permanent|creature|permanent) to its owner's hand", dict()),
 ]),
 ("Mass removal (board wipes)", "Guidance: run 2–4. One-sided or flexible wipes first.", [
   ("Creature wipes", r"(destroy|exile) all (other )?creatures|all creatures get -\d+/-\d+|each creature gets -X/-X|deals? (\d+|X) damage to each creature", dict()),
   ("Everything / nonland wipes", r"(destroy|exile) all (nonland )?permanents|(destroy|exile) all artifacts, creatures, and enchantments|return all nonland permanents to their owners' hands", dict()),
   ("Artifact / enchantment wipes", r"(destroy|exile) all (artifacts|enchantments|artifacts and enchantments|noncreature artifacts)", dict()),
 ]),
 ("Stack interaction", "Most flexible first: hard counter > soft counter > narrow counter. Free spells matter at high power.", [
   ("Hard counters (any spell)", r"^Counter target spell\.|Counter target spell\. ", dict(types=r"Instant", excl=r"unless")),
   ("Free / alternative-cost counters", r"rather than pay this spell's mana cost[^.]*|If you control a commander, you may cast this spell without paying", dict(types=r"Instant", extra=lambda c: "Counter target" in Data.text(c))),
   ("Soft & conditional counters", r"counter target (noncreature|creature|instant|sorcery|activated|spell)[^.]*(unless|with mana value)|counter target noncreature spell", dict(types=r"Instant")),
   ("Ability counters (Stifle effects)", r"counter target (activated or triggered ability|activated ability|triggered ability)", dict()),
 ]),
 ("Graveyard hate", "Permanent hate > repeatable > one-shot. ⚠️ It also hurts your own graveyard plans.", [
   ("Static graveyard hate", r"(If a card|If a nontoken creature|cards?)[^.]*would be put into (a|an opponent's|your opponents') graveyard[^.]*exile it instead|Cards in graveyards (lose|can't)|Players can't cast spells from graveyards", dict()),
   ("Repeatable / instant-speed exile", r"exile (target card from a graveyard|all cards from target player's graveyard|target player's graveyard|each opponent's graveyard|all graveyards|all cards from all graveyards|up to \w+ target cards? from (a single graveyard|graveyards))", dict(types=r"Artifact|Creature|Enchantment|Instant|Land")),
 ]),
 ("Artifact & enchantment hate (static)", "Static or repeatable answers to artifacts and enchantments.", [
   ("Repeatable answers on permanents", r"(destroy|exile) target (artifact|enchantment)[^.]*\.|artifacts (your opponents control )?(don't|can't)|activated abilities of artifacts can't", dict(types=r"Creature|Enchantment|Artifact|Planeswalker", excl=r"^Enchant")),
 ]),
 ("Stax & taxes", "Pieces that slow opponents' resources. ⚠️ Many are Game Changers. Mass land denial is outside Brackets 1–3 ([brackets](EDH%20Standards.md#power-bracket-assessment)).", [
   ("Search / tutor hate", r"can't search libraries|If (an opponent|a player) would search a library", dict()),
   ("Spell-count limits", r"(each player|players) can't cast more than one spell each turn|can't cast more than one spell each turn", dict()),
   ("Taxes", r"(spells|noncreature spells|creature spells|activated abilities)[^.]{0,40}cost \{\d\} more", dict(types=r"Artifact|Enchantment|Creature")),
   ("Untap restriction", r"(artifacts|creatures|lands|permanents)[^.]{0,30} don't untap during (their|its controllers?') untap steps?|(creatures|artifacts|nonbasic lands|permanents|lands) (your opponents control )?enter (the battlefield )?tapped", dict(types=r"Artifact|Enchantment|Creature", excl=r"^Enchant")),
   ("⚠️ Mass land denial", r"destroy all lands|each player sacrifices (all|\w+) lands|destroy all nonbasic lands|lands don't untap", dict()),
 ]),
]


def main():
    d = Data()
    L = d.header("EDH Interaction", "scripts/build_interaction.py", 28,
                 "Hierarchies list buckets from most to least flexible. The bucket order is **guidance**; the card order inside each bucket is EDHREC data.")
    L += ["## Contents"] + [f"- [{h[0]}](#{re.sub(r'[^a-z0-9 -]', '', h[0].lower()).replace(' ', '-')})" for h in H] + ["- [How much interaction (guidance)](#how-much-interaction-guidance)", ""]
    rows = 0
    for name, why, subs in H:
        L += [f"## {name}", "", f"**Hierarchy (guidance):** {why}", ""]
        for i, (lab, pat, kw) in enumerate(subs, 1):
            cs = d.find(pat, **kw)
            insts = [c for c in cs if inst(d, c)]
            rows += min(10, len(cs))
            L += [f"### {i}. {lab}", "", f"Pattern: `{pat}` · {len(cs)} matches ({len(insts)} instant or flash)", ""]
            L += d.table(cs, 10, extra=("Speed", lambda c: "instant" if inst(d, c) else "sorcery speed / permanent")) + [""]
    L += ["## How much interaction (guidance)", "",
          "**Guidance (opinion):**",
          "- Casual 100-card decks often run about **8–12 targeted answers** and **2–4 board wipes**.",
          "- Counterspells are worth more in blue-heavy decks and at higher brackets.",
          "- Bring at least 2–3 graveyard-hate pieces if your playgroup reanimates, or run flexible ones (artifact or land based).",
          "- At Brackets 1–3, don't play mass land denial, and disclose heavy stax in the pre-game talk.", "",
          "Related: [EDH Packages](EDH%20Packages.md) · [EDH Win Conditions](EDH%20Win%20Conditions.md) · [cEDH Primer](cEDH%20Primer.md) · [Rules: stack & priority](Rules%20Interactions.md#stack--priority)."]
    (ing.ROOT / "EDH Interaction.md").write_text("\n".join(L) + "\n")
    print("hierarchies", len(H), "buckets", sum(len(h[2]) for h in H), "rows", rows)


if __name__ == "__main__":
    main()
