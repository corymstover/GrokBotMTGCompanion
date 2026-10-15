#!/usr/bin/env python3
"""Generate "EDH Packages.md" (Bot cycle 6, #26): reusable card packages by function, from Scryfall data.
Each sub-package = Oracle-text pattern (shown) → Commander-legal cards, most-played first, with identity, MV, price, GC flag.
Usage: python3 scripts/build_packages.py"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import re
from edh_lib import Data
import ingest_scryfall as ing

ART = r"Artifact"
PKG = [
 ("Ramp", "Plan: accelerate into the commander and big spells. Guidance: about 10 pieces; cheap rocks for colorless or artifact decks, land ramp for green.", [
   ("Mana rocks (MV ≤ 2)", r"\{T\}: Add", dict(types=r"^Artifact(?!.*Creature)", maxmv=2, excl=r"Sacrifice this artifact: Add|^Add")),
   ("Land ramp (puts lands onto the battlefield)", r"search your library for (up to (one|two) )?(a |an )?(basic land|land) cards?[^.]*put (it|them|those cards|one) onto the battlefield", dict(excl=r"opponent")),
   ("Mana creatures (MV ≤ 2)", r"\{T\}: Add", dict(types=r"Creature", maxmv=2)),
   ("Cost reducers", r"spells you cast cost \{\d\} less|cost \{\d\} less to cast", dict(excl=r"this spell costs")),
 ]),
 ("Card advantage", "Plan: keep the hand full over a long multiplayer game. Guidance: about 10 sources, mostly repeatable engines.", [
   ("Repeatable draw engines (permanents)", r"(whenever|at the beginning of)[^.]*draw (a|one) card", dict(types=r"Creature|Enchantment|Artifact|Planeswalker|Battle")),
   ("Burst draw (instants & sorceries)", r"draw (two|three|four|five|seven|X) cards", dict(types=r"Instant|Sorcery")),
   ("Impulse / exile-to-play", r"exile the top[^.]*\. (Until|You may) [^.]*(play|cast)", dict()),
 ]),
 ("Aristocrats", "Plan: make fodder, sacrifice it for value, and drain with death triggers. See [EDH Archetypes → Aristocrats](EDH%20Archetypes.md).", [
   ("Free sacrifice outlets", r"(^|\. |\n)Sacrifice (a|another) creature: ", dict(types=r"Creature|Artifact|Enchantment")),
   ("Death-trigger drain payoffs", r"whenever (a|another) (nontoken )?creature (you control )?dies[^.]*(loses? \d+ life|each opponent loses)", dict()),
   ("Fodder makers (multiple creature tokens)", r"create (two|three|four|X|a number of) [^.]*creature tokens", dict()),
 ]),
 ("+1/+1 counters", "Plan: grow the board with counters and multiply them.", [
   ("Counter doublers", r"(twice that many|that many plus one) \+1/\+1 counters|twice that many counters|one or more counters would be put[^.]*that many plus", dict()),
   ("Proliferate", r"\bproliferate\b", dict()),
   ("Counter payoffs", r"for each \+1/\+1 counter on|creatures? you control with (a|one or more) \+1/\+1 counters? on (it|them)", dict()),
 ]),
 ("Spellslinger", "Plan: chain cheap instants and sorceries and win through cast triggers.", [
   ("Instant/sorcery cost reducers", r"instant and sorcery spells you cast cost \{1\} less|instant or sorcery spells you cast cost", dict()),
   ("Spell copiers", r"copy (target|that) (instant or sorcery|instant|sorcery) spell", dict()),
   ("Cast-trigger payoffs", r"whenever you cast (an|a) (instant or sorcery|instant|sorcery|noncreature) spell|\bmagecraft\b", dict(types=r"Creature|Enchantment|Artifact|Planeswalker")),
 ]),
 ("Graveyard", "Plan: fill the graveyard, then reanimate or recur. ⚠️ Graveyard hate punishes it; see [EDH Interaction](EDH%20Interaction.md#graveyard-hate).", [
   ("Self-mill", r"\bmill (two|three|four|five|X|\w+) cards\b|you mill", dict(excl=r"target opponent mills|each opponent mills")),
   ("Reanimation", r"(return|put) target creature card from (a|your) graveyard (on)?to the battlefield", dict()),
   ("Recursion to hand", r"return (target|up to \w+ target) [a-z ]*cards? from your graveyard to your hand", dict()),
 ]),
 ("Tokens", "Plan: go wide, then pump or convert the tokens.", [
   ("Token doublers", r"twice that many (of those )?tokens|create (twice|double) that many", dict()),
   ("Anthems", r"creatures you control get \+\d+/\+\d+", dict(excl=r"until end of turn", types=r"Creature|Enchantment|Artifact|Planeswalker")),
   ("Mass pump finishers", r"creatures you control get \+X/\+X|creatures you control get \+\d+/\+\d+ and gain trample until end of turn", dict(types=r"Instant|Sorcery")),
 ]),
 ("Blink", "Plan: re-use enters-the-battlefield triggers. Rules: [ETB/LTB](Rules%20Interactions.md#etb--ltb--look-back-triggers).", [
   ("Blink effects", r"exile (up to one )?(another )?target (nontoken )?(creature|permanent|nonland permanent|artifact or creature)[^.]*(you control|you own)?[^.]*\. (Return|Then return) (it|that card|those cards|the exiled card)", dict()),
   ("ETB doublers", r"(entering|enters)[^.]*causes? a triggered ability[^.]*triggers? an additional time", dict()),
 ]),
 ("Lands / landfall", "Plan: extra land drops plus landfall payoffs.", [
   ("Extra land drops", r"play an additional land|play two additional lands", dict()),
   ("Landfall payoffs", r"\blandfall\b|whenever a land (you control )?enters", dict(kind="nonland")),
   ("Lands from graveyard", r"play lands from your graveyard|return (target|all) land cards? from your graveyard", dict()),
 ]),
 ("Artifacts", "Plan: artifact density with cast or enter payoffs.", [
   ("Artifact payoffs", r"whenever (an|another|one or more) (nontoken )?artifacts? (you control )?(enters|is put into a graveyard)|whenever you cast an artifact spell", dict()),
   ("Artifact cost reducers", r"artifact spells you cast cost", dict()),
 ]),
 ("Enchantress", "Plan: enchantment density plus draw-on-cast or draw-on-enter.", [
   ("Enchantress draw", r"whenever you cast an enchantment spell, draw|whenever an enchantment (you control )?enters[^.]*draw", dict()),
 ]),
 ("Voltron (equipment & auras)", "Plan: suit up one creature, often the commander (21 commander damage; [rules](Rules%20Interactions.md#commander-damage)).", [
   ("Protective equipment/auras", r"(equipped|enchanted) creature (gets [^.]*and )?(has|gains) (hexproof|shroud|indestructible|protection|ward)", dict()),
   ("Evasion & double strike", r"(equipped|enchanted) creature (gets [^.]*and )?(has|gains) (double strike|flying|trample|shadow)|can't be blocked", dict(types=r"Equipment|Aura")),
 ]),
 ("Treasure", "Plan: make Treasure for ramp, fixing and artifact synergies.", [
   ("Repeatable Treasure makers", r"(whenever|at the beginning)[^.]*create (a|one|two|X|that many) Treasure tokens?", dict(types=r"Creature|Enchantment|Artifact|Planeswalker")),
 ]),
]


def main():
    import json
    dp = ing.ROOT / "data" / "deck_packages.json"  # written by scripts/build_crossrefs.py
    deck_use = json.loads(dp.read_text(encoding="utf-8"))["packages"] if dp.exists() else {}
    d = Data()
    ce = ing.ROOT / "data" / "card_enrichment.json"  # written by scripts/build_card_enrichment.py
    enriched = {}
    if ce.exists():
        for v in sorted(json.loads(ce.read_text(encoding="utf-8"))["cards"].values(), key=lambda v: v["name"]):
            for pk in v["synergy"]["guidance"]["packages"][:3]:
                enriched.setdefault(pk, []).append(v)
    L = d.header("EDH Packages", "scripts/build_packages.py", 26,
                 "Bracket notes: **GC** cards count toward the Bracket 3 limit of three; see [EDH Standards → brackets](EDH%20Standards.md#power-bracket-assessment). Pick cards whose identity fits your commander.")
    L += ["## Contents"] + [f"- [{p[0]}](#{re.sub(r'[^a-z0-9 -]', '', p[0].lower()).replace(' ', '-')})" for p in PKG] + ["- [Method](#method)", ""]
    tot = 0; subs = 0
    for name, plan, sp in PKG:
        L += [f"## {name}", "", f"**Guidance:** {plan}", ""]
        for lab, pat, kw in sp:
            cs = d.find(pat, **kw)
            subs += 1; tot += min(len(cs), 10)
            gcs = sum(1 for c in cs[:10] if c.get("game_changer"))
            L += [f"### {name}: {lab}", "", f"Pattern: `{pat}` · {len(cs)} Commander-legal matches" + (f" · {gcs} Game Changer(s) in the top 10" if gcs else ""), ""]
            L += d.table(cs, 10) + [""]
            used = deck_use.get(f"{name}: {lab}", [])
            if used:  # Bot cycle 18 (#66): back-links to the decks that run this package (data/deck_packages.json)
                L += [f"Used in decks (≥ 3 matching cards, {len(used)}): " + " · ".join(
                    f"[{u['label']}]({u['deck'].replace(' ', '%20')}) {u['cards']}" for u in used[:12]) + (f" · …{len(used) - 12} more" if len(used) > 12 else ""), ""]
            en = enriched.get(f"{name}: {lab}", [])
            if en:  # Bot cycle 34 (#102): back-links to Phase 8 enriched cards whose Synergy line names this sub-package
                L += [f"Enriched cards naming this package ([card enrichment](Card%20Enrichment.md#by-package), guidance tier, {len(en)}): " + " · ".join(
                    f"[{v['name']}]({v['shard'].replace(' ', '%20')}#{v['anchor']})" for v in en), ""]
            bud = [c for c in cs[10:] if d.price.get(c["oracle_id"], 99) <= 1.0][:4]
            if bud: L += ["Budget options beyond the top 10 (≤ $1.00): " + " · ".join(f"{d.link(c)} ({d.ci(c)}, {d.usd(c)})" for c in bud), ""]
    L += ["## Method", "", "- Each sub-package is a regex on Oracle text over Commander-legal cards (case-insensitive), shown with the section. Matches are heuristics, so some cards fit loosely.",
          "- Related: [EDH Mana Bases](EDH%20Mana%20Bases.md) · [EDH Win Conditions](EDH%20Win%20Conditions.md) · [EDH Interaction](EDH%20Interaction.md) · [EDH Archetypes](EDH%20Archetypes.md) · [EDH Staples](EDH%20Staples.md)."]
    (ing.ROOT / "EDH Packages.md").write_text("\n".join(L) + "\n")
    print("packages", len(PKG), "sub-packages", subs, "card rows", tot)


if __name__ == "__main__":
    main()
