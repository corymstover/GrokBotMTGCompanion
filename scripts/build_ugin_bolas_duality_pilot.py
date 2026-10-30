#!/usr/bin/env python3
"""Build the UNAPPROVED Phase 6 Pilot 1 proposal: Ugin & Nicol Bolas -- Elder Dragon Duality.

Card choice, story order and grading are authored here (no silent fill-ins).
Printing facts (UUID, illustration id, artist, printed flavor) are read from an
explicit, dated modern Scryfall default-cards snapshot -- never the frozen Grixis
lock. Running it rewrites only the four pilot draft files under
data/lore_decks/drafts/. It never touches approvals, locks or Grixis data.

    python3 scripts/build_ugin_bolas_duality_pilot.py --default-bulk PATH.jsonl.gz
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "data/lore_decks/drafts"
STEM = "ugin_bolas_elder_dragon_duality"
STATUS = "UNAPPROVED PROPOSAL - awaiting Cory's review; not approved, not locked, not certified"
TIERS = ("DIRECT_DEPICTION", "CANON_REFERENCE", "LORE_INSPIRED", "MECHANICAL_SYMBOL")

W = "https://magic.wizards.com/en/"
SOURCES = {
    "chronicle_twins": W + "news/magic-story/chronicle-bolas-twins-2018-06-13",
    "chronicle_unwritten": W + "news/magic-story/chronicle-bolas-unwritten-now-2018-08-15",
    "chronicle_familiar": W + "news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01",
    "fate_reforged_guide": W + "news/magic-story/planeswalkers-guide-fate-reforged-2015-01-07",
    "reforged_chain": W + "news/feature/reforged-chain-2015-01-21",
    "journey_nexus": W + "news/feature/journey-nexus-2014-12-10",
    "tarkir_plane": W + "story/tarkir-plane",
    "sarkhan_profile": W + "story/sarkhan-vol-planeswalker",
    "dmu_notes": W + "news/feature/dominaria-united-release-notes-2022-08-26",
    "m19_design": W + "news/making-magic/more-odds-ends-core-set-2019-2018-08-06",
    "mh2_legends": W + "news/feature/returning-legends-modern-horizons-2-2021-06-10",
    "amonkhet_plane": W + "story/amonkhet-plane",
    "devastation_info_3": W + "news/making-magic/devastation-information-part-3-2017-07-17",
    "hou_story": W + "news/magic-story/hour-devastation-2017-07-26",
    "more_war_games": W + "news/making-magic/more-war-games-2019-04-29",
    "war_games": W + "news/making-magic/even-more-war-games-2019-05-06",
    "war_ashes": W + "news/magic-story/war-spark-ravnica-ashes-2019-06-12",
    "tdm7": W + "news/magic-story/tarkir-dragonstorm-episode-7-return",
    "scryfall_card_text": "scryfall-snapshot:printed_flavor_or_name",
}

# (name, set, collector, tier, source_id, claim_ids, why)
ACTS = [
    ("I. Twin Elder Dragons of Dominaria and the Elder Dragon War",
     ["Pack A A001-A002", "Pack A2 A013-A024"], [
        ("Nicol Bolas", "a25", "209", "CANON_REFERENCE", "chronicle_twins", ["A001", "A002"],
         "The original Elder Dragon card; printed flavor 'Dominaria's most ancient evil.' Bolas and Ugin hatched as twins on Dominaria."),
        ("The Elder Dragon War", "dmu", "121", "CANON_REFERENCE", "dmu_notes", ["A017"],
         "Names the war Bolas instigated among the elder dragons. Not certified as a literal battlefield reconstruction."),
        ("Crosis, the Purger", "inv", "242", "CANON_REFERENCE", "mh2_legends", ["A019"],
         "Grixis-coloured primeval descendant of the elder dragon lineage (Piru line, Pack A2)."),
        ("Ghostfire", "fut", "115", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: only those gifted with the eye of Ugin, the spirit dragon, can see his fiery breath. Colourless red spell."),
        ("Fraying Omnipotence", "m19", "97", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: the Mending unravelled Nicol Bolas's power. Bridges the ancient god-like Bolas to the post-Mending schemer."),
    ]),
    ("II. Alara: the Conflux scheme", ["Pack A source A007 context"], [
        ("Nicol Bolas, Planeswalker", "con", "120", "CANON_REFERENCE", "reforged_chain", [],
         "Pack A4 exact-art match (NAMED_CHARACTER_ART_IN_STORY): the Bolas portrait used in the Ugin/Bolas duel coverage."),
        ("Slave of Bolas", "arb", "136", "CANON_REFERENCE", "scryfall_card_text", [],
         "Named after Bolas; flavor: Bolas does not distinguish servants and victims."),
        ("Soul Manipulation", "arb", "29", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Nicol Bolas quote; Grixis counter/recursion of the Conflux era."),
        ("Countersquall", "ddh", "59", "CANON_REFERENCE", "scryfall_card_text", [],
         "Duel Decks: Ajani vs. Nicol Bolas printing; flavor states Bolas's creed of power."),
        ("Mana Drain", "j16", "2", "CANON_REFERENCE", "scryfall_card_text", [],
         "Judge printing with a Nicol Bolas quote: 'Power is wasted on the weak.' Not a Game Changer."),
        ("Magmaquake", "m13", "140", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Nicol Bolas threat; the M13 Bolas planeswalker-deck era."),
        ("Augur of Bolas", "war", "41", "CANON_REFERENCE", "scryfall_card_text", [],
         "War of the Spark printing: 'There is no future save the one my master wills.'"),
        ("Disciple of Bolas", "m13", "88", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed 'Lord Bolas' quote; sacrifice-for-cards servant."),
    ]),
    ("III. Zendikar: Ugin's hedrons and the Eldrazi prison", ["Pack A A005 context"], [
        ("Hedron Archive", "bfz", "223", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Ugin dialogue about the hedrons' true purpose."),
        ("Perilous Vault", "m15", "224", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: Ugin arranged Zendikar's hedrons to direct leylines."),
        ("Ugin's Insight", "bfz", "87", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Ugin quote on the three Eldrazi titans."),
        ("Dispel", "bfz", "76", "CANON_REFERENCE", "scryfall_card_text", [],
         "BFZ printing contrasting Ugin's stasis plan with destruction of the Eldrazi."),
        ("Ugin's Binding", "mh3", "76", "LORE_INSPIRED", "scryfall_card_text", [],
         "Named Ugin binding magic (devoid, colourless spell for Ugin, Eye of the Storms). Card name only; no scene claimed."),
    ]),
    ("IV. Tarkir: the duel, the fall, and the reforged timeline", ["Pack A A005-A006", "Pack A3/A4"], [
        ("Crux of Fate", "frf", "65", "DIRECT_DEPICTION", "reforged_chain", ["A005"],
         "Pack A4 exact-art match: official story art caption of the Ugin-Bolas battle."),
        ("Ugin's Nexus", "ktk", "227", "CANON_REFERENCE", "chronicle_familiar", [],
         "Pack A4: official story device (the nexus Sarkhan uses to reach the past)."),
        ("Ugin, the Spirit Dragon", "frf", "1", "CANON_REFERENCE", "reforged_chain", ["A005", "A006"],
         "Pack A4 exact Raymond Swanland art (not the ugin/1 promo art). Ugin survives in the reforged timeline."),
        ("Bitter Revelation", "ktk", "65", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Sorin quote at Ugin's tomb in the original Khans timeline."),
        ("Witness of the Ages", "ktk", "228", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: it strode through the clash of dragons and the fall of Ugin."),
        ("Fearsome Awakening", "frf", "69", "CANON_REFERENCE", "scryfall_card_text", [],
         "Fate Reforged printing tying the dragon tempests to Ugin; reanimates a dragon."),
        ("Sarkhan the Mad", "roe", "214", "CANON_REFERENCE", "sarkhan_profile", [],
         "Official profile: Sarkhan swore fealty to Bolas and went mad before returning to Tarkir."),
        ("Sarkhan, the Dragonspeaker", "ktk", "119", "CANON_REFERENCE", "sarkhan_profile", [],
         "Official profile: Sarkhan travelled back and saved Ugin from death at Bolas's hands."),
        ("Dragonlord Silumgar", "dtk", "220", "CANON_REFERENCE", "tarkir_plane", ["A006"],
         "Official Tarkir page: Ugin's survival produced the dragonlord timeline; Silumgar is the Grixis-adjacent UB dragonlord."),
        ("Dragonlord Kolaghan", "dtk", "218", "CANON_REFERENCE", "tarkir_plane", ["A006"],
         "Same consequence; Kolaghan is the BR dragonlord."),
    ]),
    ("V. Amonkhet: the God-Pharaoh and the Hour of Devastation", ["new pilot sources"], [
        ("Nicol Bolas, God-Pharaoh", "hou", "140", "CANON_REFERENCE", "amonkhet_plane", [],
         "Official Amonkhet page: the God-Pharaoh is Nicol Bolas."),
        ("The Scarab God", "hou", "145", "CANON_REFERENCE", "devastation_info_3", [],
         "Bolas warped one of Amonkhet's gods to raise the Eternal army (official design article)."),
        ("The Locust God", "hou", "139", "CANON_REFERENCE", "devastation_info_3", [],
         "Bolas's god tasked with devouring the Hekma barrier."),
        ("The Scorpion God", "hou", "146", "CANON_REFERENCE", "devastation_info_3", [],
         "Bolas's god tasked with killing the other five gods."),
        ("Hour of Devastation", "hou", "97", "DIRECT_DEPICTION", "hou_story", [],
         "Art is captioned in the official 'Hour of Devastation' story at Bolas's arrival in the ruined plaza."),
        ("Jace's Defeat", "hou", "38", "DIRECT_DEPICTION", "hou_story", [],
         "Captioned in the official story as Bolas crushes Jace's mind."),
        ("Liliana's Defeat", "hou", "68", "DIRECT_DEPICTION", "hou_story", [],
         "Captioned in the official story as Liliana leaves at Bolas's offer."),
        ("Chandra's Defeat", "hou", "86", "DIRECT_DEPICTION", "hou_story", [],
         "Captioned in the official story as Chandra flees Bolas."),
        ("Doomfall", "hou", "62", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Nicol Bolas quote: 'This place has outlived its usefulness.'"),
        ("Neheb, the Eternal", "hou", "104", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Nicol Bolas quote: 'This is what glory looks like.'"),
        ("Wasp of the Bitter End", "hou", "206", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: a chorus of wings heralds the return of Nicol Bolas."),
        ("Visage of Bolas", "hou", "208", "LORE_INSPIRED", "scryfall_card_text", [],
         "Named Bolas monument; Grixis mana. Card name only (no printed flavor)."),
        ("Nicol Bolas, the Deceiver", "hou", "205", "CANON_REFERENCE", "amonkhet_plane", [],
         "Bolas at the moment of the Hours."),
        ("Tezzeret, Agent of Bolas", "mbs", "97", "CANON_REFERENCE", "hou_story", [],
         "Official HOU story ends with Tezzeret calling Bolas 'master' and running his errands."),
    ]),
    ("VI. War of the Spark: the Elderspell, the fall, the prison", ["Pack A A008"], [
        ("Nicol Bolas, Dragon-God", "war", "207", "CANON_REFERENCE", "war_ashes", [],
         "Bolas empowered by the Elderspell on Ravnica."),
        ("Bolas's Citadel", "war", "79", "CANON_REFERENCE", "war_ashes", [],
         "The Citadel atop which Bolas falls. Game Changer (counted; bracket 3)."),
        ("Commence the Endgame", "war", "45", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Nicol Bolas quote: 'Even gods shall kneel.'"),
        ("Command the Dreadhorde", "war", "82", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: Liliana seized the reins of Bolas's army."),
        ("Spark Harvest", "war", "105", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: Domri's harvested spark fuels Bolas's ascension."),
        ("God-Eternal Kefnet", "war", "53", "CANON_REFERENCE", "more_war_games", [],
         "Official: Bolas remade the slain Amonkhet gods as God-Eternals."),
        ("God-Eternal Bontu", "war", "92", "CANON_REFERENCE", "war_ashes", [],
         "Official story: Bontu bites Bolas and harvests the sparks of the Elderspell."),
        ("Liliana, Dreadhorde General", "war", "97", "CANON_REFERENCE", "war_ashes", [],
         "Liliana commands the Dreadhorde, then turns the God-Eternals on Bolas."),
        ("Liliana's Triumph", "war", "98", "DIRECT_DEPICTION", "war_ashes", [],
         "Art captioned in the official 'Ashes' story at the moment Bontu harvests Bolas's sparks."),
        ("Finale of Revelation", "war", "51", "CANON_REFERENCE", "scryfall_card_text", ["A008"],
         "Printed flavor: Ugin saw Bolas's gem as the key to his brother's imprisonment."),
        ("Ugin, the Ineffable", "war", "2", "CANON_REFERENCE", "war_games", ["A008"],
         "Ugin at the end of the war; he holds Bolas in the Meditation Realm."),
        ("Ugin's Conjurant", "war", "3", "LORE_INSPIRED", "scryfall_card_text", [],
         "Named Ugin construct; colourless spell. Card name only."),
        ("Sarkhan's Catharsis", "war", "144", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed Sarkhan quote turning on Bolas."),
        ("No Escape", "war", "63", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: Jace surmised they were walking into Bolas's trap."),
    ]),
    ("VII. Tarkir Dragonstorm: Ugin's later fate", ["Pack A A009-A010"], [
        ("Ugin, Eye of the Storms", "tdm", "1", "CANON_REFERENCE", "tdm7", ["A009", "A010"],
         "Ugin in the Dragonstorm era. A011 (his status afterwards) remains OPEN_QUESTION."),
        ("Dracogenesis", "tdm", "402", "CANON_REFERENCE", "scryfall_card_text", [],
         "Showcase printing chosen for its Ugin flavor: the dragonstorms weakened with his death and raged with his life."),
        ("Watcher of the Wayside", "tdm", "249", "CANON_REFERENCE", "scryfall_card_text", [],
         "Printed flavor: the golem survived dragonlords, khans and Ugin himself."),
    ]),
]

STORY_LANDS = [
    ("Tomb of the Spirit Dragon", "ktk", "245", "CANON_REFERENCE", "journey_nexus", [],
     "Pack A4 STORY_LOCATION_ART_CAPTION: Ugin's tomb in the original timeline."),
    ("Crucible of the Spirit Dragon", "frf", "167", "CANON_REFERENCE", "chronicle_familiar", [],
     "Pack A4 STORY_LOCATION_ART_CAPTION."),
    ("Haven of the Spirit Dragon", "dtk", "249", "LORE_INSPIRED", "scryfall_card_text", [],
     "Named Ugin site in the reforged timeline; recurs Ugin and dragons."),
    ("Maelstrom of the Spirit Dragon", "tdm", "260", "LORE_INSPIRED", "scryfall_card_text", [],
     "Named Dragonstorm-era Ugin site."),
    ("Ugin's Labyrinth", "mh3", "233", "LORE_INSPIRED", "scryfall_card_text", [],
     "Named Ugin site; can imprint the seven-mana Ugins."),
    ("Cinder Barrens", "hou", "209", "CANON_REFERENCE", "scryfall_card_text", [],
     "HOU printing with a Nicol Bolas quote: 'it is all mine.'"),
    ("Crumbling Necropolis", "ala", "222", "LORE_INSPIRED", "scryfall_card_text", [],
     "Grixis shard of Alara, the world Bolas fed on."),
    ("Interplanar Beacon", "war", "247", "LORE_INSPIRED", "scryfall_card_text", [],
     "Bolas's planeswalker lure on Ravnica; theme, not a scene claim."),
]

PLAYABILITY = ["Sol Ring", "Arcane Signet", "Talisman of Dominance", "Talisman of Creativity",
               "Talisman of Indulgence", "Command Tower", "Watery Grave", "Blood Crypt",
               "Steam Vents", "Drowned Catacomb", "Dragonskull Summit", "Sulfur Falls",
               "Underground River", "Sulfurous Springs", "Shivan Reef"]
BASICS = {"Island": 6, "Swamp": 6, "Mountain": 5}
COMMANDER = ("Nicol Bolas, the Ravager // Nicol Bolas, the Arisen", "m19", "218", "CANON_REFERENCE",
             "m19_design", [], "Grixis Elder Dragon commander; transforms into the Arisen. Ugin is colourless and lives in the 99.")

UNREPRESENTABLE = [
    "Yasova Dragonclaw (G/U-R) and Sarkhan, Dragonstorm era green-identity cards cannot enter a Grixis identity deck.",
    "Sarkhan Unbroken (GUR) is outside UBR identity.",
    "Piru, the Volatile and The Ur-Dragon are outside UBR identity; the Piru lineage is represented only by Crosis.",
    "Arcades Sabboth, Chromium and Palladia-Mors (Pack A2 siblings) are outside UBR identity.",
]
CAVEATS = [
    "A003/A004 (who struck first; Ugin's perspective) are CANON_DISPUTED and are not asserted by any card here.",
    "A011 (Ugin's status after Lorwyn Eclipsed episode 2) is an OPEN_QUESTION; Ugin, Eye of the Storms only marks the Dragonstorm era.",
    "A012 Reality Fracture material is ALTERNATE_CONTINUITY and is excluded.",
    "Printed flavor proves what Wizards printed on the card, not that the illustration depicts a specific story scene.",
    "DIRECT_DEPICTION is used only where an official story captions that art at that event (or Pack A4's exact-art match).",
]


def printings(bulk):
    out = {}
    opener = gzip.open if str(bulk).endswith(".gz") else open
    with opener(bulk, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip().rstrip(",")
            if not line or line in "[]":
                continue
            c = json.loads(line)
            if c.get("lang") != "en" or "paper" not in c.get("games", []) or c.get("layout") == "art_series":
                continue
            out.setdefault(c["name"], []).append(c)
    return out


def flavor(c):
    if c.get("flavor_text"):
        return c["flavor_text"]
    return " / ".join(f["flavor_text"] for f in c.get("card_faces", []) if f.get("flavor_text"))


def pick(cands, name, set_code=None, cn=None):
    if not cands:
        raise SystemExit("not in snapshot: " + name)
    if set_code:
        hit = [c for c in cands if c["set"] == set_code and c["collector_number"] == cn]
        if not hit:
            raise SystemExit(f"printing not found: {name} {set_code}/{cn}")
        return hit[0]
    normal = [c for c in cands if not c.get("promo") and c.get("border_color") == "black"
              and not c.get("full_art") and c["set_type"] in ("core", "expansion", "commander", "masters")]
    normal.sort(key=lambda c: (c["released_at"], c["set"], c["collector_number"]))
    # Deterministic: the earliest ordinary printing (stable, recognisable art).
    return (normal or sorted(cands, key=lambda c: c["released_at"]))[0]


def record(c, tier, source_id, claims, why, beat):
    ill = c.get("illustration_id") or (c.get("card_faces") or [{}])[0].get("illustration_id")
    legal = c.get("legalities", {}).get("commander")
    return {"name": c["name"], "beat": beat, "tier": tier, "source_id": source_id,
            "source": SOURCES[source_id], "pack_a_claims": claims, "why": why,
            "printing": {"set": c["set"], "collector_number": c["collector_number"], "id": c["id"],
                          "oracle_id": c.get("oracle_id"), "illustration_id": ill,
                          "artist": c.get("artist"), "released_at": c["released_at"],
                          "printed_flavor": flavor(c), "commander_legality": legal,
                          "color_identity": c.get("color_identity"),
                          "type_line": c.get("type_line"),
                          "game_changer": bool(c.get("game_changer"))}}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--default-bulk", required=True, type=Path)
    ap.add_argument("--snapshot-id", default="snap-20261029-40848334824-1")
    args = ap.parse_args(argv)
    raw = args.default_bulk.read_bytes()
    bulk_sha = hashlib.sha256(raw).hexdigest()
    db = printings(args.default_bulk)

    cards = [record(pick(db.get(COMMANDER[0]), COMMANDER[0], COMMANDER[1], COMMANDER[2]),
                    *COMMANDER[3:6], COMMANDER[6], "commander")]
    beats = []
    for title, keys, rows in ACTS:
        spec_cards = []
        for name, s, cn, tier, sid, claims, why in rows:
            r = record(pick(db.get(name), name, s, cn), tier, sid, claims, why, title)
            cards.append(r)
            spec_cards.append({"name": name, "why": why, "evidence": tier, "source": SOURCES[sid],
                               "printing": {"set": s, "collector": cn}})
        beats.append({"title": title, "lore_keys": keys, "cards": spec_cards})
    land_cards = []
    for name, s, cn, tier, sid, claims, why in STORY_LANDS:
        cards.append(record(pick(db.get(name), name, s, cn), tier, sid, claims, why, "story lands"))
        land_cards.append({"name": name, "why": why, "evidence": tier, "source": SOURCES[sid],
                           "printing": {"set": s, "collector": cn}})
    beats.append({"title": "Story lands: tombs, crucibles and the Grixis shard", "lore_keys": ["Pack A4"],
                  "cards": land_cards})
    play = []
    for name in PLAYABILITY:
        c = pick(db.get(name), name)
        cards.append(record(c, "MECHANICAL_SYMBOL", "scryfall_card_text", [],
                            "Mana/fixing for a UUBBRR commander; no story claim.", "playability"))
        play.append({"name": name, "why": "Mana/fixing for a UUBBRR commander; no story claim (MECHANICAL_SYMBOL)."})

    for c in cards:
        if c["printing"]["commander_legality"] != "legal":
            raise SystemExit("not Commander-legal in snapshot: " + c["name"])
        if not set(c["printing"]["color_identity"]) <= {"U", "B", "R"}:
            raise SystemExit("outside UBR identity: " + c["name"])

    lines = []
    for c in cards:
        p = c["printing"]
        tag = " [Commander]" if c["beat"] == "commander" else ""
        lines.append(f"1x {c['name']} ({p['set']}) {p['collector_number']}{tag}")
    lines += [f"{q}x {n}" for n, q in BASICS.items()]
    decklist = "\n".join(lines) + "\n"
    import_list = "\n".join([f"1x {c['name'].split(' // ')[0]}" for c in cards] +
                            [f"{q}x {n}" for n, q in BASICS.items()]) + "\n"
    deck_sha = hashlib.sha256(decklist.encode()).hexdigest()
    tiers = {t: sum(1 for c in cards if c["tier"] == t) for t in TIERS}
    total = len(cards) + sum(BASICS.values())

    spec = {
        "schema": "lore_story_deck_draft/v1",
        "theme": "Ugin & Nicol Bolas - Elder Dragon Duality (Phase 6 Pilot 1)",
        "status": STATUS,
        "approval": {"approved": False, "locked": False, "certified": False, "owner": "Cory"},
        "commander": COMMANDER[0],
        "narrator_note": "Bolas leads (Grixis); his colourless twin Ugin runs through every act in the 99. The deck walks their shared story from the Dominarian hatching to Ugin's Dragonstorm-era fate.",
        "story_sources": sorted(set(v for v in SOURCES.values() if v.startswith("https://"))),
        "canon_caveats": CAVEATS,
        "unrepresentable_in_identity": UNREPRESENTABLE,
        "beats": beats,
        "playability": play,
        "basics": BASICS,
        "archidekt_tags": ["Story: Ugin & Bolas Duality", "Grixis Elder Dragon", "Unapproved Lore Pilot"],
        "snapshot": {"id": args.snapshot_id, "default_cards_file": args.default_bulk.name,
                     "default_cards_sha256": bulk_sha},
        "raw_decklist_sha256": deck_sha,
        "counts": {"total": total, "named_cards": len(cards), "basics": sum(BASICS.values()),
                   "tiers": tiers},
    }
    evidence = {"theme": spec["theme"], "status": STATUS, "raw_sha256": deck_sha,
                "snapshot": spec["snapshot"], "tier_definitions": {
                    "DIRECT_DEPICTION": "Official Wizards story captions this exact art at the event, or Pack A4 exact-art scene match.",
                    "CANON_REFERENCE": "Card is the character/object/event, or its printed text or an official article ties it to Ugin/Bolas canon.",
                    "LORE_INSPIRED": "Named or thematic link only; no scene or event asserted.",
                    "MECHANICAL_SYMBOL": "Included for function; no story claim."},
                "cards": cards}
    DRAFTS.mkdir(parents=True, exist_ok=True)
    (DRAFTS / f"{STEM}_proposal.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (DRAFTS / f"{STEM}_printing_evidence.json").write_text(json.dumps(evidence, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (DRAFTS / f"{STEM}_decklist.txt").write_text(decklist, encoding="utf-8")
    (DRAFTS / f"{STEM}_archidekt_import.txt").write_text(import_list, encoding="utf-8")
    print(json.dumps({"total": total, "tiers": tiers, "sha256": deck_sha}, indent=1))


if __name__ == "__main__":
    main()
