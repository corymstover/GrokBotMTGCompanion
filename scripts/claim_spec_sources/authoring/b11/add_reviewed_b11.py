"""Batch 11 authoring record: append reviewed-no-claim entries for untagged pages read in full.

Idempotent (skips URLs already listed). Run from the repo root with .cache/story/text22 present.
ENTRIES values are (reason, note) or (reason, note, duplicate_of_page_key). Each entry is a GrokBot reading
note, not an owner approval and not a certification."""
import csv, hashlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
REG = ROOT / "data/lore_research/reviewed_no_claim.json"
TXT = ROOT / ".cache/story/text22"
ENTRIES = {
    "bound-and-bonded-2018-11-14": ("NO_EXTRACTABLE_RELATION",
        "Ravnica Allegiance-era vignette told by an unnamed first-person narrator about friends Ambrellin, Savaryn, Kellim and the "
        "orphan Bazda; the Orzhov appear only as setting (cathedrals, a destroyed basilica), and the only relations are between "
        "story-original characters with no graph entity, faction membership or leadership stated. Not graded in Batch 11."),
    "ledger-hidden-fortunes-2019-02-20": ("NO_EXTRACTABLE_RELATION",
        "Epistolary Orzhov tithe-collection ledger kept by an unnamed collector (tithe percentages, property inventories, a "
        "rumoured Vitu-Ghazi vulnerability); it names no character-to-faction or leadership relation for a graph entity. "
        "Not graded in Batch 11."),
    "choosing-your-battles-part-3": ("DESIGN_OR_PROCESS_ARTICLE",
        "Mark Rosewater Making Magic column (2023-04-24) explaining how March of the Machine battle cards were designed; card "
        "design commentary, not story canon."),
    "its-time-talk-commander-2016-edition-2016-10-26": ("PRODUCT_OR_PROMO_NOTE",
        "Commander 2016 product overview listing the decks and their legendary creatures with deck art; no story narrative."),
    "krenko-mob-boss-2012-07-18": ("DUPLICATE_PAGE",
        "Second URL for the same 'Krenko, Mob Boss' story; the text matches krenko-mob-boss-2012-07-16 word for word apart from the "
        "page date and the trailing related-links block.", "krenko-mob-boss-2012-07-16"),
    "threadbare-2012-07-23": ("NO_EXTRACTABLE_RELATION",
        "First-person monologue of the Stuffy Doll card's living doll on an unnamed quest; it names no other character, faction or "
        "place it could be linked to, so no relation claim is graded."),
    "blessed-life-2012-07-24": ("NO_EXTRACTABLE_RELATION",
        "Innistrad soldier story (Brenalt, Mattias, an unnamed inquisitor). The only named groups and places (the Fourth Legion, "
        "Greenfield, River's Glen) appear in passing with no stated leader, membership or location relation to a graph entity."),
    "cowardice-hero-2014-01-22": ("NO_EXTRACTABLE_RELATION",
        "Theros story narrated by the unnamed stepson of the 'hero' Vinack; the relations are to unnamed family and farmhands, and the "
        "named gods (Athreos, Mogis) and the scholar Zerili appear only in passing, so no graph relation is graded."),
    "nature-identity-2014-01-15-0": ("DUPLICATE_PAGE",
        "Second URL for 'The Nature of Identity'; the story text matches nature-identity-2014-01-15.", "nature-identity-2014-01-15"),
    "path-or-horizon-2014-05-07-0": ("DUPLICATE_PAGE",
        "Second URL for 'The Path or the Horizon'; the story text matches path-or-horizon-2014-05-07.", "path-or-horizon-2014-05-07"),
}


def main(argv):
    only = set(argv) or None
    rows = {r["url"].rstrip("/").rsplit("/", 1)[-1]: r for r in csv.DictReader((ROOT / "data/primary_sources.csv").open(encoding="utf-8"))}
    reg = json.loads(REG.read_text(encoding="utf-8"))
    have = {e["page_key"] for e in reg["entries"]}
    n = 0
    for key, val in ENTRIES.items():
        if key in have or (only and key not in only):
            continue
        reason, note = val[0], val[1]
        r = rows[key]
        e = {"url": r["url"].rstrip("/"), "page_key": key, "arc": r["arc"], "reviewer": "GrokBot",
             "reviewed_on": "2026-10-30", "reason": reason, "note": note,
             "cached_text_sha256": hashlib.sha256((TXT / f"{key}.txt").read_bytes()).hexdigest()}
        if len(val) > 2:
            e["duplicate_of"] = rows[val[2]]["url"].rstrip("/")
        reg["entries"].append(e)
        n += 1
    REG.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("added", n, "total", len(reg["entries"]))


if __name__ == "__main__":
    main(sys.argv[1:])
