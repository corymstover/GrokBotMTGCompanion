#!/usr/bin/env python3
"""Pack A genealogy dispute evidence matrix (Batch 13, 2026-10-30).

Owner-facing research artifact. Every quote is verified verbatim (whitespace/quote
normalised) against the cached official Wizards page, and its sha256 is stored so
CI can check integrity without the git-excluded story cache.

This script does NOT resolve disputes and does NOT change any pack grade.
`official_resolution` is filled only where an official source itself states the
answer; otherwise it is null. `owner_decision` is always left empty for Cory.

Usage: python3 scripts/build_pack_a_dispute_matrix.py [--check]
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LR = ROOT / "data/lore_research"
OUT = LR / "pack_a_genealogy_disputes_2026-10-30.json"
MD = ROOT / "research/PACK_A_GENEALOGY_DISPUTES_2026-10-30.md"
sys.path.insert(0, str(ROOT / "scripts"))


def norm(s: str) -> str:
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip()

PACKS = ["pack_a_ugin_bolas_evidence", "pack_a_elder_dragon_war_extension",
         "pack_a_tarkir_card_scenes", "pack_a5_ugin_allies"]

# Voice tags: what kind of speaker makes the statement.
#   EDITORIAL           Wizards article/card-preview prose outside the fiction
#   NARRATOR_UGIN       first-person narration by Ugin (Chronicle of Bolas)
#   NARRATOR_BOLAS      first-person narration by Bolas (self-serving by design)
#   STORY_NARRATION     third-person story narration
#   CHARACTER_DIALOGUE  a character speaking in-story
# Stance: SUPPORTS / CONTESTS / QUALIFIES / CONTEXT relative to the question.
E = lambda page, quote, voice, stance, note="": dict(page=page, quote=quote, voice=voice, stance=stance, note=note)

DISPUTES = [
 dict(id="GD1", topic="Are Ugin and Nicol Bolas twins?", claims=["A001", "A013"],
  question="Does official text establish Ugin and Bolas as twins, given Bolas's in-story denial?",
  evidence=[
   E("ugin-planeswalker", "He's as cunning and powerful as his twin, Nicol Bolas, but luckily much less interested in world domination.", "EDITORIAL", "SUPPORTS"),
   E("chronicle-bolas-twins-2018-06-13", "Two small egg-stones tumble groundward, like an afterthought.", "STORY_NARRATION", "SUPPORTS", "Hatching scene: the last two egg-stones fall together."),
   E("chronicle-bolas-first-lesson-2018-06-20", "\"You are the twins, Nicol and Ugin.\"", "CHARACTER_DIALOGUE", "SUPPORTS", "Spoken by their older brother Arcades."),
   E("chronicle-bolas-whispers-treachery-2018-07-11", "He wasn't my twin, after all, just a wingbeat sibling who wasn't any too respectful of Nicol and me regardless.", "NARRATOR_UGIN", "SUPPORTS", "Ugin contrasts Chromium (sibling) with his twin."),
   E("chronicle-bolas-perspectives-2018-08-08", "You're a liar when you say you aren't twin to Ugin. You were born together and fell together. Isn't that right?\"", "CHARACTER_DIALOGUE", "CONTEXT", "Yasova paraphrases what she was told."),
   E("chronicle-bolas-perspectives-2018-08-08", "\"Of course that's not right! Who told you that?\"", "NARRATOR_BOLAS", "CONTESTS", "Bolas's reply; it is unclear whether he denies twinship, 'fell together', or both."),
   E("tarkir-dragonstorm-episode-6-how-wretched-love", "As Ugin raised his head, so did his olive-gold twin, the latter as perfect as polished bronze.", "STORY_NARRATION", "SUPPORTS", "Third-person narration in 2025 story."),
  ],
  official_resolution=dict(statement="Wizards editorial (Ugin planeswalker page) and third-person story narration (Chronicle 'The Twins'; Tarkir: Dragonstorm ep. 6) call them twins. The only contrary voice is Bolas's own in-story reply, whose scope is ambiguous.", resolves="SUPPORTS_A001_AS_GRADED", source_pages=["ugin-planeswalker", "tarkir-dragonstorm-episode-6-how-wretched-love"]),
  options_for_owner=["Keep A001 CANON_CONFIRMED and record Bolas's reply as narrator dissent", "Add a CANON_DISPUTED note limited to Bolas's perspective"]),
 dict(id="GD2", topic="Are Ugin and Bolas Elder Dragons, and is the Ur-Dragon their progenitor?", claims=["A001", "A013"],
  question="Official text calls Bolas an Elder Dragon and says Elder Dragons were spawned by the Ur-Dragon. Does any source state that the Ur-Dragon is the twins' parent?",
  evidence=[
   E("returning-legends-modern-horizons-2-2021-06-10", "Piru was one of the Elder Dragons, creatures spawned by the Ur-Dragon when Dominaria was young.", "EDITORIAL", "CONTEXT", "Defines Elder Dragons as Ur-Dragon spawn, but names only Piru here."),
   E("war-spark-ravnica-ashes-2019-06-12", "I'd been told that sword had already killed a major demon, a God-Eternal, and even an Elder Dragon like Nicol Bolas.", "CHARACTER_DIALOGUE", "SUPPORTS", "Calls Bolas an Elder Dragon (first-person story voice)."),
   E("planeswalkers-guide-fate-reforged-2015-01-07", "The Battle of the Elder Dragons After a rivalry that spanned eons, Nicol Bolas and Ugin—two of the most powerful Planeswalkers the Multiverse has ever known—finally clashed in the sky above Tarkir.", "EDITORIAL", "SUPPORTS", "Section header frames the Ugin–Bolas battle as one of Elder Dragons."),
   E("chronicle-bolas-perspectives-2018-08-08", "Of all the elder dragons and their children, only Chromium Rhuell, Arcades Sabboth, Palladia-Mors, and that vexatious beast Vaevictis Asmadi had survived.", "NARRATOR_BOLAS", "QUALIFIES", "Bolas speaks of 'elder dragons and their children' as a group apart from himself; he does not label himself."),
   E("chronicle-bolas-things-unseen-2018-06-27", "The expanding realm of our brother Arcades dwelt far away from the mountain of our birth.", "NARRATOR_UGIN", "CONTEXT", "Birth is placed at a mountain; no parent is named in the cached Chronicle."),
  ],
  official_resolution=None,
  unresolved_because="No cached official source names the twins' parent. Deriving 'Ur-Dragon is Ugin/Bolas's parent' would chain two statements (Bolas is an Elder Dragon + Elder Dragons were spawned by the Ur-Dragon), which this project does not do without an explicit source. The Chronicle never mentions the Ur-Dragon (checked: 0 hits across its 8 cached chapters).",
  options_for_owner=["Leave the twins' parentage unknown", "Accept the two-step inference as CANON_IMPLIED with that limitation stated", "Seek the Chronicle of Bolas novel/other official text (not cached)"]),
 dict(id="GD3", topic="Elder Dragon War survivor roster", claims=["A003", "A018"],
  question="Bolas names four survivors; Wizards editorial adds Piru. Which roster is authoritative?",
  evidence=[
   E("chronicle-bolas-perspectives-2018-08-08", "Of all the elder dragons and their children, only Chromium Rhuell, Arcades Sabboth, Palladia-Mors, and that vexatious beast Vaevictis Asmadi had survived.", "NARRATOR_BOLAS", "CONTESTS", "Four names, Piru absent, under the word 'only'."),
   E("returning-legends-modern-horizons-2-2021-06-10", "Piru and Chromium were among the very few Elder Dragons who survived the Elder Dragon War instigated by Nicol Bolas.", "EDITORIAL", "SUPPORTS", "Adds Piru; 'very few' gives no total."),
  ],
  official_resolution=None,
  unresolved_because="The sources conflict over Piru. Neither gives an exhaustive count. Bolas's narration is graded self-serving by design (A003 CANON_DISPUTED). MH2 is later editorial prose but does not say it corrects the Chronicle. The time frames may also differ: Bolas speaks of the moment he returned to Dominaria.",
  options_for_owner=["Treat roster as open (current state: A003 DISPUTED, A018 CONFIRMED)", "Treat MH2 as superseding and annotate A003", "Record as continuity conflict without preference"]),
 dict(id="GD4", topic="Vaevictis Asmadi's descendants as raiders", claims=["A014"],
  question="Is the raiders' lineage only their own claim, or does the narrator corroborate it?",
  evidence=[
   E("chronicle-bolas-blood-and-fire-2018-07-18", "\"We are the descendants of Vaevictis Asmadi and may raid where we wish!\"", "CHARACTER_DIALOGUE", "SUPPORTS", "Raiders' self-identification."),
   E("chronicle-bolas-blood-and-fire-2018-07-18", "Vaevictis was a bully, and his descendants were bullies who would rip apart the harmonious kingdom for the sport of it.", "NARRATOR_UGIN", "SUPPORTS", "Narrator restates the lineage in his own voice."),
  ],
  official_resolution=None,
  unresolved_because="Both statements sit inside the same framed Chronicle chapter. Neither is independent of that frame, and no source traces each raider's generation.",
  options_for_owner=["Keep A014 limitation as written", "Amend limitation to note Ugin's narratorial corroboration"]),
 dict(id="GD5", topic="Piru, Chromium and Crosis lineage", claims=["A019", "A018"],
  question="Is Crosis a direct child of Piru and Chromium, and how is Piru related to the Chronicle siblings?",
  evidence=[
   E("returning-legends-modern-horizons-2-2021-06-10", "With her mate, Chromium Rhuell, she birthed whole nations of dragons, including none other than the Primeval Dragon Crosis, the Purger.", "EDITORIAL", "QUALIFIES", "'Birthed whole nations … including' does not state generation."),
   E("chronicle-bolas-twins-2018-06-13", "Yet Chromium Rhuell can't help but wonder what has become of the last ones, these younger siblings, especially when no tremor of impact shakes the ground.", "STORY_NARRATION", "CONTEXT", "Chromium is a sibling of the twins; Piru does not appear in any cached Chronicle chapter."),
  ],
  official_resolution=None,
  unresolved_because="The generation is unstated. Piru's relation to Ugin and Bolas is not stated; it would have to be inferred from 'Elder Dragon', which this project does not do.",
  options_for_owner=["Keep 'ancestor_of' wording (generation unknown)", "Leave Piru–twins relation explicitly unknown"]),
 dict(id="GD6", topic="Rith's family: Palladia-Mors and Darigaaz", claims=["A023", "A024"],
  question="What official parentage or sibling links exist for the Primeval Dragons?",
  evidence=[
   E("legends-youll-find-dominaria-united-2022-09-01", "Rith, daughter of Palladia-Mors, was one of the five ancient Primeval Dragons who ruled Dominaria sometime after the Elder Dragon War.", "EDITORIAL", "SUPPORTS"),
   E("legends-youll-find-dominaria-united-2022-09-01", "Darigaaz recently reincarnated once again, and his psychic connection to his sister caused Rith to stir from her slumber.", "EDITORIAL", "SUPPORTS", "Darigaaz–Rith sibling link is stated but is not yet a Pack A claim."),
   E("returning-legends-modern-horizons-2-2021-06-10", "With her mate, Chromium Rhuell, she birthed whole nations of dragons, including none other than the Primeval Dragon Crosis, the Purger.", "EDITORIAL", "CONTEXT", "Crosis descends from Piru and Chromium; Rith is Palladia-Mors's daughter. No source links the two lines."),
  ],
  official_resolution=None,
  unresolved_because="Parentage is stated only for Rith (Palladia-Mors) and Crosis (Piru + Chromium, generation unstated). No cached source names parents for Darigaaz, Dromar or Treva. 'Sister' does not establish whether Darigaaz shares Rith's mother.",
  proposed_claim_not_applied=dict(subject="darigaaz", predicate="sibling_of", object="rith", proposed_grade="CANON_CONFIRMED", source="legends-youll-find-dominaria-united-2022-09-01"),
  options_for_owner=["Add the Darigaaz–Rith sibling claim to Pack A2", "Leave as research note"]),
 dict(id="GD7", topic="Chromium Rhuell's fate: banished vs murdered", claims=["A020", "A018"],
  question="Two editorial biographies give different ends for Chromium. Are they sequential or conflicting?",
  evidence=[
   E("returning-legends-modern-horizons-2-2021-06-10", "Dakkon banished Chromium and slew Piru with his cursed sword.", "EDITORIAL", "CONTEXT"),
   E("legendary-characters-commander-legends-part-1-2020-10-30", "A recurring evil in Dominarian history, he was instrumental in the fall of the Sarpadian Empires, the destruction of the Glacier Kingdom of Storgard, the murder of the elder dragon Chromium Rhuell, and the cataclysmic rebirth of the Primeval Dragons.", "EDITORIAL", "CONTEXT", "'he' = Tevesh Szat."),
  ],
  official_resolution=None,
  unresolved_because="Neither source orders the banishment and the murder. They may be sequential (banished, then later murdered), but no cached source says so.",
  options_for_owner=["Record both as unordered events", "Seek an official source ordering them"]),
]

# Non-genealogy Pack A disputes: carried over verbatim from pack grades for completeness.
OTHER_DISPUTED = ["A004", "A011", "A012", "U016"]


def find_page(pages, key):
    hits = [p for p in pages.values() if p["url"].rstrip("/").endswith(key)]
    if len(hits) != 1:
        raise SystemExit(f"page key {key!r} matched {len(hits)} cached pages")
    return hits[0]


def claims_index():
    out = {}
    for p in PACKS:
        for c in json.loads((LR / f"{p}_2026-10-30.json").read_text())["claims"]:
            out[c["id"]] = dict(pack=p, **{k: c.get(k) for k in ("subject", "predicate", "object", "grade", "source_ids", "summary", "limitation")})
    return out


def build(pages):
    ci = claims_index()
    rows = []
    for d in DISPUTES:
        row = dict(d)
        row["claim_records"] = {c: ci[c] for c in d["claims"]}
        ev = []
        for e in d["evidence"]:
            p = find_page(pages, e["page"])
            if norm(e["quote"]) not in norm(p["text"]):
                raise SystemExit(f"{d['id']}: quote not on page {e['page']}: {e['quote'][:60]}")
            ev.append(dict(e, source_url=p["url"], quote_sha256=hashlib.sha256(norm(e["quote"]).encode()).hexdigest()))
        row["evidence"] = ev
        row["owner_decision"] = ""
        rows.append(row)
    other = [dict(id=c, **ci[c], owner_decision="") for c in OTHER_DISPUTED]
    return {
        "schema": "pack-a-genealogy-disputes/v1",
        "status": "PRELIMINARY_RESEARCH_FOR_OWNER",
        "generated": "2026-10-30",
        "rules": [
            "Quotes are verbatim from cached official Wizards pages and are hash-checked.",
            "No pack grade is changed. official_resolution is set only where an official source itself states the answer.",
            "owner_decision is intentionally blank for Cory.",
            "No two-step genealogical inference is asserted.",
        ],
        "counts": {"disputes": len(rows), "evidence_quotes": sum(len(r["evidence"]) for r in rows),
                   "officially_resolved": sum(1 for r in rows if r["official_resolution"]),
                   "open": sum(1 for r in rows if not r["official_resolution"]),
                   "other_disputed_claims": len(other)},
        "disputes": rows,
        "other_pack_a_disputed_claims": other,
    }


def render_md(doc):
    L = ["# Pack A genealogy disputes: evidence matrix for the owner (2026-10-30)", "",
         f"Status: **{doc['status']}**. Built by `scripts/build_pack_a_dispute_matrix.py`; artifact `data/lore_research/pack_a_genealogy_disputes_2026-10-30.json`.", "",
         "No grade changed. The **Owner decision** cell is blank on purpose.", "",
         f"{doc['counts']['disputes']} disputes, {doc['counts']['evidence_quotes']} verbatim quotes. {doc['counts']['officially_resolved']} has an official statement that answers it; {doc['counts']['open']} stay open.", ""]
    for r in doc["disputes"]:
        L += [f"## {r['id']}: {r['topic']}", "", f"Claims: {', '.join(c + ' (' + r['claim_records'][c]['grade'] + ')' for c in r['claims'])}", "",
              f"**Question.** {r['question']}", "", "| Stance | Voice | Quote | Source | Note |", "|---|---|---|---|---|"]
        for e in r["evidence"]:
            L.append(f"| {e['stance']} | {e['voice']} | “{e['quote'].replace('|', '/')}” | [{e['page']}]({e['source_url']}) | {e['note']} |")
        res = r["official_resolution"]
        L += ["", "**Official resolution:** " + (res["statement"] if res else "none. " + r["unresolved_because"]), "",
              "**Options for the owner:** " + "; ".join(r["options_for_owner"]) + ".", "", "**Owner decision:** _(blank)_", ""]
    L += ["## Other Pack A disputed or open claims (not genealogy)", "", "| Claim | Grade | Summary | Limitation |", "|---|---|---|---|"]
    for c in doc["other_pack_a_disputed_claims"]:
        L.append(f"| {c['id']} | {c['grade']} | {c['summary']} | {c['limitation']} |")
    return "\n".join(L) + "\n"


def main():
    if "--check" in sys.argv:
        doc = json.loads(OUT.read_text())
        try:
            pages = __import__("build_card_lore_links").load_pages()
        except SystemExit:
            pages = None
        if pages is not None and build(pages) != doc:
            raise SystemExit("dispute matrix stale; rebuild")
        for r in doc["disputes"]:
            for e in r["evidence"]:
                assert hashlib.sha256(norm(e["quote"]).encode()).hexdigest() == e["quote_sha256"]
        assert MD.read_text() == render_md(doc), "markdown out of date"
        print("dispute matrix OK", doc["counts"])
        return
    import build_card_lore_links as b
    doc = build(b.load_pages())
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    MD.write_text(render_md(doc))
    print(json.dumps(doc["counts"]))


if __name__ == "__main__":
    main()
