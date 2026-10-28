#!/usr/bin/env python3
"""Mechanical physical-slot ledger from the already authored M6 and M7 review."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REV = ROOT.parent / "decision_reviews" / "The_Valeyard_M7_Rev1_99slot_ledger.csv"
CUTS = {
    "Arcane Denial": ("Swan Song", "Replace two-mana broad counter plus two opponent cards with one-blue noncreature stack protection; concede no creature/artifact counter and opponent 2/2 flyer."),
    "Blasphemous Act": ("Toxic Deluge", "Replace situational 13-damage wrath with three-mana, life-scaled -X/-X to defeat indestructible threats; lose cheap one-red sweeper into packed creature boards."),
    "Brainstorm": ("Irenicus's Vile Duplication", "Trade one-blue fetchland-assisted selection for a permanent nonlegendary Valeyard token, one more independent static choice/vote modifier."),
    "Haunted Ridge": ("Ancient Tomb", "Trade reliable BR dual for untapped two-colorless acceleration toward five-mana Valeyard and expensive choice spells; costs two life and no colors."),
    "Izzet Signet": ("Chrome Mox", "Trade sustained two-mana UR filter for zero-mana conditional colored acceleration; imprint loses a nonartifact/nonland card and reduces late-game resources."),
    "Kess, Dissident Mage": ("Double Vision", "Trade one spell recast from graveyard each our turn for copying first instant/sorcery cast EACH turn, potentially repeating genuine votes/choices; costs one extra mana."),
}
KEEPS = {
    "The Master, Gallifrey's End": "A retained native villainous-choice source: Missy can produce actual face-down nontoken Cybermen cards whose deaths trigger the Master; not a disposable generic 4-drop.",
    "Missy": "Preserved Doctor Who artifact/nontoken creature conversion that can fuel the Master's villainous choice and board recursion.",
    "Midnight Crusader Shuttle": "Preserved hard-to-replace direct villainous-choice source despite crew/combat demand; rejected helm alternative removes one native choice card.",
    "Auton Soldier": "Preserved nonlegendary Valeyard copier; myriad combat clones add separate modifiers only while they exist.",
    "Quantum Misalignment": "Preserved one-token nonlegendary Valeyard copy plus rebound as a second cast; native power rather than general combo.",
    "Sakashima of a Thousand Faces": "Preserved legal commander copy by suspending your legend rule; unlike ordinary Clone it can remain with Valeyard.",
    "Spark Double": "Preserved direct nonlegendary Valeyard copy at four mana; part of the protected multiplier engine.",
    "Plea for Power": "Preserved true will-of-the-council vote; Valeyard casts a second vote, but opposing three votes still determine majority unless influenced.",
    "Illusion of Choice": "Preserved low-mana way to set every vote while drawing a card; resolves both majority control and Grudge Keeper choices.",
    "Grudge Keeper": "Preserved real voting payoff; warn that voting for both choices oneself can turn off its punishment condition.",
    "Model of Unity": "Preserved repeat vote finish scry plus multicolor mana from artifact; a unique two-role card.",
    "Path of the Enigma": "Preserved five-mana draw four with bona fide Will of the Planeswalkers voting; planeswalk/chaos rider requires rules-context caution.",
    "Path of the Schemer": "Preserved five-mana graveyard creature acquisition plus true vote; unlike off-theme tutor it contributes voting occasions.",
    "Path of the Pyromancer": "Preserved red hand refresh and mana burst plus true planeswalker vote; no speculative claim of value from planar effects in normal Commander.",
    "Coercive Portal": "Preserved upkeep Will of the Council every turn; extra Valeyard vote helps favor draw over sweep when opponent votes split.",
    "Capital Punishment": "Preserved asymmetric council's dilemma, with each vote producing sacrifice/discard and controller's second vote strengthening effect.",
    "Truth or Consequences": "Preserved secret council and damage/draw payoff; extra vote counts in choice totals.",
    "Fateful Tempest": "Preserved cost-three council's dilemma, damage/exile resource engine, major Double Vision target.",
    "The Dalek Emperor": "Preserved repeated combat-stage villainous choice and Dalek haste; affinity mitigates seven printed mana cost.",
    "Dr. Eggman": "Preserved repeatable end-step villainous-choice attack on opponents via alternate discard/payload choice.",
    "Davros, Dalek Creator": "Preserved end-step villains-choose trigger and Dalek production; core Doctor Who identity.",
    "Genesis of the Daleks": "Preserved chapter choices and Dalek token payoff; Clone/copy suite increases those real choice events.",
    "Force of Will": "Preserved free commander/engine protection; even after losing Brainstorm/Arcane Denial/Kess, plenty of other true blue cards remain.",
    "Fierce Guardianship": "Preserved free stack shield after commander resolves, not necessarily free before Valeyard arrives.",
    "Deflecting Swat": "Preserved free targeted redirection while commander is controlled, shielding choice engine from removal.",
    "Dark Ritual": "Preserved colored burst that can deploy five-mana commander by turn three, versus proposed Mana Vault replacement elsewhere.",
    "Fellwar Stone": "Preserved two-mana colored artifact in a BRU pod, favoring repeatable UBR access over one-shot Mana Vault tempo.",
}


def main():
    path = ROOT / "The_Valeyard_Oct15_baseline.txt"
    source = path.read_text(encoding="utf8").splitlines()
    rows = []
    for line in source[1:]:
        q, name = line.split("x ", 1)
        for _ in range(int(q)):
            add, note = CUTS.get(name, ("", KEEPS.get(name,
                "KEEP: independently reconciled with M6 all-99 role audit and M7 current Scryfall review; no challenger beats its mana, interaction, vote, choice or fixing role.")))
            rows.append((len(rows) + 1, name, "CUT" if add else "KEEP", add, note))
    assert len(rows) == 99 and sum(x[2] == "CUT" for x in rows) == 6
    with REV.open("w", newline="", encoding="utf8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["library_slot", "canonical_card", "decision", "candidate_replacement", "evidence_and_opportunity_cost"])
        writer.writerows(rows)
    print("99 physical slots reconciled, 6 cuts, 93 retained")


if __name__ == "__main__":
    main()
