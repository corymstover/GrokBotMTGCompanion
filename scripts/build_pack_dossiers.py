#!/usr/bin/env python3
"""Phase 4 L244: per-family dossiers for Packs A, B and C, derived only from committed claim packs.

For each family it publishes: a stage sequence (ordered by the earliest *publication* date of the cited
Wizards sources -- explicitly NOT an asserted in-universe chronology), verbatim relative in-universe
phrases, a relationship map (claim edges with grades), a source bibliography, explicit uncertainties
(non-CONFIRMED claims, limitations, pack 'remaining/unknowns'), and lore-deck CANDIDATES (anchored
legendary creatures, Commander legality as of the pinned Oct 29 oracle snapshot). Nothing here is
owner approved; candidates are UNAPPROVED proposals.
"""
import argparse, collections, gzip, hashlib, json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LR = ROOT / "data/lore_research"
OUT = LR / "pack_dossiers_2026-10-30.json"
MD = ROOT / "research/PACK_ABC_DOSSIERS.md"
NAMES = {"A": "Ugin, Nicol Bolas and the Elder Dragons", "B": "Thran, Yawgmoth, Old Phyrexia and the Brothers' War",
         "C": "Dominaria, the Weatherlight, the Legacy and the Phyrexian invasions"}
ORACLE = ROOT / ".cache/multiverse/oracle-cards-20261029090202.jsonl.gz"
FAMILIES = {
    "A": ["pack_a_ugin_bolas_evidence", "pack_a_elder_dragon_war_extension", "pack_a_tarkir_card_scenes", "pack_a5_ugin_allies"],
    "B": ["pack_b_thran_yawgmoth_brothers_war"],
    "C": ["pack_c_weatherlight_invasion_new_phyrexia", "pack_c2_return_to_dominaria",
          "pack_c3_assault_on_new_phyrexia", "pack_c4_march_of_the_machine"],
}
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def jload(p):
    return json.loads(Path(p).read_text())


def pub_date(src):
    if src.get("published"):
        return src["published"]
    m = DATE_RE.search(src.get("url", ""))
    return "-".join(m.groups()) if m else None


def stage_of(c):
    return c.get("chronology_stage") or c.get("event_stage") or c.get("stage") or "unstaged"


def oracle_index(ids):
    idx = {}
    if not ORACLE.exists():
        return None
    with gzip.open(ORACLE, "rt") as f:
        for line in f:
            r = json.loads(line)
            if r.get("oracle_id") in ids:
                idx[r["oracle_id"]] = {"type_line": r.get("type_line", ""),
                                       "commander": (r.get("legalities") or {}).get("commander"),
                                       "color_identity": "".join(r.get("color_identity") or [])}
    return idx


def build():
    anchors = jload(LR / "claim_card_anchors_2026-10-30.json")["anchors"]
    dates = jload(LR / "in_universe_dates_2026-10-30.json")["dates"]
    files = {f: f"{f}_2026-10-30.json" for fam in FAMILIES.values() for f in fam}
    need = {a["oracle_id"] for a in anchors if a["pack"] in files.values()}
    oi = oracle_index(need)
    if oi is None:
        sys.exit("oracle snapshot cache absent")
    global_reg = {}
    for f in sorted(LR.glob("pack_*_2026-10-30.json")):
        d = jload(f)
        if isinstance(d, dict) and isinstance(d.get("source_register"), dict) and "claims" in d:
            for sid, s in d["source_register"].items():
                global_reg.setdefault(sid, (f.name, s))
    fams = {}
    for fam, packs in FAMILIES.items():
        claims, bib, unc_notes = [], {}, []
        for p in packs:
            d = jload(LR / files[p])
            for sid, s in d["source_register"].items():
                bib[sid] = {"title": s.get("title"), "url": s.get("url"), "published": pub_date(s),
                            "kind": s.get("kind"), "pack": files[p]}
            for c in d["claims"]:
                claims.append(dict(c, _pack=files[p]))
            for k in ("remaining", "unverified_next", "unknowns"):
                v = d.get(k)
                if v:
                    unc_notes.append({"pack": files[p], "field": k, "items": v})
        cross = []
        for c in claims:
            for sid in c.get("source_ids", []):
                if sid not in bib and sid in global_reg:
                    src_pack, s = global_reg[sid]
                    bib[sid] = {"title": s.get("title"), "url": s.get("url"), "published": pub_date(s),
                                "kind": s.get("kind"), "pack": src_pack, "cross_pack": True}
                if sid in bib and bib[sid].get("cross_pack"):
                    cross.append({"claim": c["id"], "claim_pack": c["_pack"], "source_id": sid, "register_pack": bib[sid]["pack"]})
        cids = {c["id"] for c in claims}
        stages = collections.OrderedDict()
        for c in claims:
            st = stages.setdefault(stage_of(c), {"claims": [], "pub": []})
            st["claims"].append(c["id"])
            st["pub"] += [bib[s]["published"] for s in c.get("source_ids", []) if s in bib and bib[s]["published"]]
        seq = sorted(({"stage": k, "earliest_cited_publication": min(v["pub"]) if v["pub"] else None,
                       "claims": v["claims"]} for k, v in stages.items()),
                     key=lambda x: (x["earliest_cited_publication"] is None, x["earliest_cited_publication"] or "", x["stage"]))
        rel = [{"claim": c["id"], "subject": c["subject"], "predicate": c["predicate"], "object": c["object"],
                "grade": c["grade"], "stage": stage_of(c), "source_ids": c.get("source_ids", [])} for c in claims]
        grades = collections.Counter(c["grade"] for c in claims)
        uncertain = [{"claim": c["id"], "grade": c["grade"], "limitation": c.get("limitation", "")}
                     for c in claims if c["grade"] != "CANON_CONFIRMED"]
        limited = sum(1 for c in claims if c.get("limitation"))
        fam_anchors = [a for a in anchors if a["claim"] in cids]
        cand = collections.defaultdict(lambda: {"claims": set(), "tiers": set()})
        for a in fam_anchors:
            o = oi.get(a["oracle_id"], {})
            tl = o.get("type_line", "")
            if "Legendary" in tl and "Creature" in tl.split("//")[0]:
                k = (a["card"], a["oracle_id"])
                cand[k]["claims"].add(a["claim"]); cand[k]["tiers"].add(a["tier"])
                cand[k]["o"] = o
        cands = sorted(({"card": k[0], "oracle_id": k[1], "type_line": v["o"]["type_line"],
                         "color_identity": v["o"]["color_identity"] or "C",
                         "commander_legal_in_snapshot": v["o"]["commander"] == "legal",
                         "anchored_claims": sorted(v["claims"]), "anchor_tiers": sorted(v["tiers"])}
                        for k, v in cand.items()), key=lambda x: (-len(x["anchored_claims"]), x["card"]))
        fams[fam] = {
            "packs": [files[p] for p in packs],
            "claim_count": len(claims), "grade_counts": dict(sorted(grades.items())),
            "stage_sequence": seq,
            "in_universe_relative_phrases": [d for d in dates if d["claim"] in cids],
            "relationship_map": rel,
            "bibliography": dict(sorted(bib.items())),
            "uncertainties": {"non_confirmed_claims": uncertain, "claims_with_limitation": limited,
                              "pack_open_items": unc_notes,
                              "cross_pack_citations": cross},
            "card_representations": {"ART_IN_CITED_SOURCE": sorted({a["card"] for a in fam_anchors if a["tier"] == "ART_IN_CITED_SOURCE"}),
                                     "anchor_pairs": len(fam_anchors)},
            "lore_deck_commander_candidates": cands,
        }
    body = {"schema": "pack-dossiers/v1", "status": "PRELIMINARY_RESEARCH",
            "not": "owner approved; candidates are UNAPPROVED proposals; no deck is built or certified",
            "stage_sequence_basis": "ordered by earliest publication date of cited Wizards sources (publication order), "
                                    "NOT an asserted in-universe chronology; in-universe time appears only as verbatim relative phrases",
            "legality_basis": "Commander legality from Scryfall oracle-cards snapshot 2026-10-29 (.cache/multiverse); not current-rules certified",
            "families": fams}
    body["content_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    return body


def render_md(body):
    L = ["# Pack A/B/C dossiers (generated)", "",
         "Generated by `scripts/build_pack_dossiers.py` from the committed claim packs; data in "
         "[`pack_dossiers_2026-10-30.json`](../data/lore_research/pack_dossiers_2026-10-30.json). "
         "**Status: PRELIMINARY_RESEARCH. Not owner approved. Commander candidates are UNAPPROVED proposals; no deck is built.**", "",
         f"- Stage order: {body['stage_sequence_basis']}.", f"- Legality: {body['legality_basis']}.", ""]
    for k, f in body["families"].items():
        L += [f"## Pack {k}: {NAMES[k]}", "",
              f"- Claims: {f['claim_count']} ({', '.join(f'{g} {n}' for g, n in f['grade_counts'].items())}); "
              f"{f['uncertainties']['claims_with_limitation']} carry a stated limitation.",
              f"- Bibliography: {len(f['bibliography'])} Wizards sources. Cross-pack citations: "
              + (", ".join(f"{x['claim']}→{x['source_id']} ({x['register_pack']})" for x in f['uncertainties']['cross_pack_citations']) or "none") + ".",
              f"- Stages (publication order): " + "; ".join(f"`{x['stage']}` ({x['earliest_cited_publication'] or 'undated source'}, {len(x['claims'])})" for x in f["stage_sequence"]) + ".",
              f"- Verbatim relative in-universe phrases: " + ("; ".join(f"{d['claim']}: “{d['value']}”" for d in f["in_universe_relative_phrases"]) or "none") + ".",
              f"- Non-CONFIRMED claims: " + ("; ".join(f"{u['claim']} {u['grade']}" for u in f["uncertainties"]["non_confirmed_claims"]) or "none") + ".",
              f"- Card art credited on a cited source: " + (", ".join(f["card_representations"]["ART_IN_CITED_SOURCE"]) or "none") + ".",
              f"- Commander candidates ({len(f['lore_deck_commander_candidates'])}, legal in snapshot marked ✓): "
              + ", ".join(f"{c['card']} [{c['color_identity']}]{' ✓' if c['commander_legal_in_snapshot'] else ''} ({len(c['anchored_claims'])})"
                          for c in f["lore_deck_commander_candidates"][:15]) + ("…" if len(f["lore_deck_commander_candidates"]) > 15 else "") + ".", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    body = build()
    text = json.dumps(body, indent=1, sort_keys=True) + "\n"
    if a.check:
        ok = OUT.exists() and OUT.read_text() == text and MD.exists() and MD.read_text() == render_md(body)
        print("PASS pack dossiers current" if ok else "FAIL pack dossiers stale"); sys.exit(0 if ok else 1)
    OUT.write_text(text); MD.write_text(render_md(body)); print("wrote", OUT.relative_to(ROOT), MD.relative_to(ROOT))
    for k, f in body["families"].items():
        print(k, f["claim_count"], f["grade_counts"], "stages", len(f["stage_sequence"]), "phrases", len(f["in_universe_relative_phrases"]),
              "bib", len(f["bibliography"]), "cands", len(f["lore_deck_commander_candidates"]), "art", len(f["card_representations"]["ART_IN_CITED_SOURCE"]))


if __name__ == "__main__":
    main()
