"""Batch 10 authoring record: append reviewed-no-claim entries for untagged pages read in full.

Idempotent (skips URLs already listed). Run from the repo root with .cache/story/text22 present.
Each entry is a GrokBot reading note, not an owner approval and not a certification."""
import csv, hashlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
REG = ROOT / "data/lore_research/reviewed_no_claim.json"
TXT = ROOT / ".cache/story/text22"
ENTRIES = {
    "a-planeswalkers-guide-to-new-phyrexia": ("INDEX_OR_LANDING_PAGE",
        "Wrap-up landing page for the five-week Planeswalker's Guide to New Phyrexia: concept art captions and card flavor quotes "
        "pointing to the guide sections, which are cited separately (pack_p5_untagged_nph_guides)."),
    "making-kaladesh-2016-11-09": ("DESIGN_OR_PROCESS_ARTICLE",
        "Creative-team article on how the Kaladesh world was designed; behind-the-scenes process, not story text."),
    "naming-nameless-brandon-sanderson-2018-12-12": ("DESIGN_OR_PROCESS_ARTICLE",
        "Interview with Brandon Sanderson about writing the Children of the Nameless novella; the novella itself is not this page."),
    "magic-origins-new-era-2015-06-03": ("INDEX_OR_LANDING_PAGE",
        "Magic Origins series introduction: one-line arcs for five Planeswalkers with links to their origin stories."),
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
