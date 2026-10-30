"""Batch 9 authoring record: append reviewed-no-claim entries for untagged pages read in full.

Idempotent (skips URLs already listed). Run from the repo root with .cache/story/text22 present.
Each entry is a GrokBot reading note, not an owner approval and not a certification."""
import csv, hashlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
REG = ROOT / "data/lore_research/reviewed_no_claim.json"
TXT = ROOT / ".cache/story/text22"
PROFILE = ("Undated official Planeswalker profile blurb, read in full. It describes personality, powers or "
           "backstory only and names no other character, faction or plane, so there is no relation to grade.")
DND = ("Dungeons & Dragons adventure download page for Adventures in the Forgotten Realms: a short setup blurb plus "
       "character-sheet downloads. Not Magic story text with graded relations.")
ENTRIES = {
    **{f"{n}-planeswalker": ("NO_EXTRACTABLE_RELATION", PROFILE) for n in
       "arlinn-kord ashiok chandra-nalaar davriel-cane dovin-baan garruk-wildspeaker gideon-jura grist jace-beleren kasmina kaya "
       "kiora koth liliana-vess mu-yanling nicol-bolas nissa-revane ob-nixilis oko ral-zarek saheeli-rai tamiyo teyo-verada "
       "tezzeret wrenn".split()},
    "planeswalkers-guide-innistrad-2011-11-02": ("INDEX_OR_LANDING_PAGE",
        "Cached page is only the title and byline (15 words); the guide body is not in the cached text."),
    "lore-core-set-2021-cards-2020-06-16": ("INDEX_OR_LANDING_PAGE",
        "Landing blurb for a daily card-lore series (82 words); the lore entries themselves are not in the cached text."),
    "magic-story-shadows-over-innistrad-e-book-collection-2016-06-01": ("PRODUCT_OR_PROMO_NOTE",
        "E-book download note for the Shadows over Innistrad stories; no story text."),
    "rorecas-tale-2008-03-19": ("INDEX_OR_LANDING_PAGE",
        "Intro to Richard Garfield's 1994 Pocket Player's Guide story; the story pages are page images and the cached text holds only navigation links."),
    **{s: ("PRODUCT_OR_PROMO_NOTE", DND) for s in
       ("scarlet-flames-2021-06-30", "hidden-page-2021-07-07", "verdant-tomb-2021-07-14", "deepest-night-2021-07-21", "cyan-depths-2021-07-28")},
}


def main(argv):
    only = set(argv) or None
    rows = {r["url"].rstrip("/").rsplit("/", 1)[-1]: r for r in csv.DictReader((ROOT / "data/primary_sources.csv").open(encoding="utf-8"))}
    reg = json.loads(REG.read_text(encoding="utf-8"))
    have = {e["page_key"] for e in reg["entries"]}
    n = 0
    for key, (reason, note) in ENTRIES.items():
        if key in have or (only and key not in only):
            continue
        r = rows[key]
        reg["entries"].append({"url": r["url"].rstrip("/"), "page_key": key, "arc": r["arc"], "reviewer": "GrokBot",
                               "reviewed_on": "2026-10-30", "reason": reason, "note": note,
                               "cached_text_sha256": hashlib.sha256((TXT / f"{key}.txt").read_bytes()).hexdigest()})
        n += 1
    REG.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("added", n, "total", len(reg["entries"]))


if __name__ == "__main__":
    main(sys.argv[1:])
