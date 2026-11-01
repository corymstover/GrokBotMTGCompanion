#!/usr/bin/env python3
"""Fail-closed two-chapter War of the Spark chronology supplement.

This adds browsable, fully source-identified events without rewriting the
v3.00-certified chronology corpus. `--live` independently checks every short
quote on the official Wizards pages; default/--check work offline in CI.

  python3 scripts/audit_war_spark_chapter_gap.py
  python3 scripts/audit_war_spark_chapter_gap.py --check
  python3 scripts/audit_war_spark_chapter_gap.py --live
  python3 scripts/audit_war_spark_chapter_gap.py --compare DO:kaya_commissioned DO:golgari_rescue
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

from audit_lore_pack_c5 import TextOnly, normalize
import source_event_sequences as seq

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "data/lore_research/war_spark_chapter_gap_spec_2026-11-01.json"
OUT = ROOT / "data/lore_research/war_spark_chapter_gap_2026-11-01.json"


def verify(value, message: str) -> None:
    if not value:
        raise ValueError("War of the Spark chapter-gap: " + message)


def build() -> dict:
    spec_bytes = SPEC.read_bytes()
    spec = json.loads(spec_bytes)
    verify(spec["schema"] == "war-spark-chapter-gap-spec/v1" and
           spec["status"] == "PRELIMINARY_SOURCE_LOCAL_RESEARCH", "invalid spec scope")
    pack_rel = spec["source_pack"]
    verify(pack_rel == "data/lore_research/pack_p5_war_spark_ravnica_2026-10-30.json",
           "source pack cannot be silently substituted")
    pack_bytes = (ROOT / pack_rel).read_bytes()
    pack = json.loads(pack_bytes)
    verify(pack["pack_id"] == "pack_p5_war_spark_ravnica" and
           pack["status"].startswith("PRELIMINARY_RESEARCH"), "unexpected research pack")
    verify({s["source_id"] for s in spec["strands"]} == {"wr_path_opulent", "wr_desperate"},
           "both omitted official chapters required")

    events, edges, strands, sources = [], [], [], {}
    seen = set()
    for strand in spec["strands"]:
        sid = strand["id"]
        src = pack["source_register"][strand["source_id"]]
        verify(src["url"].startswith("https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-")
               and src["kind"] == "official_story_episode", "source is not registered official Wizards story")
        sources[strand["source_id"]] = {k: src[k] for k in ("title", "url", "published")}
        ids = set()
        for event in strand["events"]:
            verify(event["id"].startswith(sid + ":") and event["id"] not in seen and event["label"],
                   "duplicated or empty event")
            seen.add(event["id"])
            ids.add(event["id"])
            events.append({**event, "strand": sid, "certainty": "HISTORICAL_SOURCE_ACCOUNT"})
        for edge in strand["edges"]:
            verify(edge["earlier"] in ids and edge["later"] in ids and
                   edge["earlier"] != edge["later"] and edge["quote"] and edge["note"],
                   "unsupported cross-strand or empty edge")
            edges.append({**edge, "relation": "BEFORE", "certainty": "HISTORICAL_SOURCE_ACCOUNT",
                          "source_id": strand["source_id"], "source_url": src["url"],
                          "source_title": src["title"],
                          "quote_sha256": hashlib.sha256(seq.canon(edge["quote"]).encode()).hexdigest()})
        strands.append({"id": sid, "title": strand["title"], "source_id": strand["source_id"],
                        "certainty": "HISTORICAL_SOURCE_ACCOUNT", "limitation": strand["limitation"],
                        "events": len(ids), "strict_edges": len(strand["edges"])})
    verify(len(events) == 10 and len(edges) == 8 and len(strands) == 2, "unexpected bounded batch size")
    precedes = seq.closure(seen, edges)
    verify(sum(map(len, precedes.values())) == 20, "non-chain or contradictory bounded ordering")
    verify("not" in spec["scope"].lower() or "neither" in spec["scope"].lower(),
           "scope must explicitly reject implied ordering")
    for left, right in spec["explicitly_unknown_pairs"]:
        verify(left in seen or left.startswith(("Y:", "W:")), "unknown proof endpoint")
        verify(right in seen or right.startswith(("Y:", "W:")), "unknown proof endpoint")
        verify(not (left in seen and right in seen and
                    any(n["strand"] == left.split(":")[0] for n in events if n["id"] == right)),
               "within-strand pair may have a strict proof")

    output = {"schema": "war-spark-chapter-gap-audit/v1", "status": spec["status"],
              "reviewed_on": "2026-11-01", "scope": spec["scope"],
              "source_pack": pack_rel, "source_pack_sha256": hashlib.sha256(pack_bytes).hexdigest(),
              "spec_sha256": hashlib.sha256(spec_bytes).hexdigest(), "sources": sources,
              "strands": strands, "nodes": events, "edges": edges, "precedes": precedes,
              "counts": {"new_strands": 2, "new_events": 10, "new_strict_edges": 8,
                         "new_source_local_pairs": 20, "official_pages": 2, "live_verifiable_quotes": 8},
              "excluded_from_certified_v300_graph_and_packet": True,
              "explicitly_unknown_pairs": spec["explicitly_unknown_pairs"]}
    output["content_sha256"] = seq.digest(output)
    return output


def proof(data: dict, left: str, right: str) -> dict:
    if left in {n["id"] for n in data["nodes"]} and right in {n["id"] for n in data["nodes"]}:
        return seq.proof(data, left, right)
    if (left, right) in [tuple(x) for x in data["explicitly_unknown_pairs"]] or \
            (right, left) in [tuple(x) for x in data["explicitly_unknown_pairs"]]:
        return {"result": "UNKNOWN", "left": left, "right": right, "proof": [],
                "confidence": "UNRESOLVED", "limitation": "No cited cross-ledger ordering exists."}
    raise ValueError("unknown event ID or unregistered cross-ledger comparison")


def live_check(data: dict, fetch=None) -> dict:
    def default_fetch(url):
        with urlopen(Request(url, headers={"User-Agent": "MTG-Multiverse-Companion-source-review/1.0"}), timeout=25) as response:
            return response.read().decode("utf-8", errors="replace")
    fetch = fetch or default_fetch
    pages = {}
    for source_id, source in data["sources"].items():
        reader = TextOnly()
        reader.feed(fetch(source["url"]))
        pages[source_id] = normalize(" ".join(reader.parts))
    for edge in data["edges"]:
        verify(normalize(edge["quote"]) in pages[edge["source_id"]],
               "official live quotation absent: " + edge["earlier"] + " → " + edge["later"])
    return {"status": "PASS", "official_pages": len(pages), "quotes": len(data["edges"])}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--compare", nargs=2, metavar=("EARLIER", "LATER"))
    args = parser.parse_args()
    data = build()
    serialized = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        verify(OUT.is_file() and OUT.read_text(encoding="utf-8") == serialized,
               "committed source evidence stale")
    else:
        OUT.write_text(serialized, encoding="utf-8")
    if args.live:
        print("Live original-source verification:", live_check(data))
    if args.compare:
        print(json.dumps(proof(data, *args.compare), indent=2))
    else:
        print("PASS War of the Spark supplement:", data["counts"], "(not the certified core)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
