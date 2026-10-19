#!/usr/bin/env python3
"""Fail-closed M6 individual-deck deep-review tracking; no deck mutation.

Validates progress *structure*. This cannot validate strategic judgment or live
external canonical authority; those must be independently reviewed per deck.
"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/"data/grixis/m6/single_deck_depth_tracker.json"
REG=ROOT/"data/grixis/registry.json"
BASIS="grixis/M6 Commander-First Single-Deck Review Standard.md"
VALID={"PENDING","IN_PROGRESS","BLOCKED","DEEP_REVIEW_COMPLETE"}
HEADINGS=(
 "## Commander identity and natural ceiling",
 "## Full 100-card role audit",
 "## Candidate pool and competing cuts",
 "## Oracle, legality and rules",
 "## Finite sequencing and adversarial scenarios",
 "## Conclusions and unresolved evidence",
 "## Source and test receipts",
)
def load(path):return json.loads(Path(path).read_text(encoding="utf-8"))
def validate(ledger,registry):
    p=ledger["process"];entries=ledger["decks"];reg=registry["decks"]
    assert ledger["schema_version"]==1
    assert ledger["authority"]["source_approved_locked"]==62
    assert ledger["authority"]["historical_m6_4_authored_source_reviews"]==62
    assert ledger["authority"]["canonical_deck_changes_allowed"] is False
    assert ledger["authority"]["formal_independent_pass_c_allowed"] is False
    assert p["mode"]=="SEQUENTIAL_SINGLE_DECK"
    assert p["required_protocol"]==BASIS
    assert len(entries)==p["total"]==62 and len(reg)==62
    assert len({e["tracker_deck_id"] for e in entries})==62
    assert len({e["canonical_deck_id"] for e in entries})==62
    assert set(e["engineering_deck_id"] for e in entries)==set(reg)
    assert all(e["tracker_index"]==i for i,e in enumerate(entries))
    completed=0;unfinished=[];active=[]
    for e in entries:
        assert e["status"] in VALID
        eng=reg[e["engineering_deck_id"]]
        assert e["baseline_approved_sha256"]==eng["source"]["recorded_sha256"]
        assert e["baseline_engineering_logical_sha"]==eng["current_canonical_hash"]
        assert e["commander_names_in_engineering"]==eng["commanders"]
        if e["source_identity_discrepancy"]=="NONE":
            assert e["tracker_deck_id"]==e["canonical_deck_id"]==e["engineering_deck_id"]
            assert e["source_identity_issue"] is None
        else:
            assert e["source_identity_issue"] and e["source_identity_discrepancy"] in ("IDENTIFIER_ALIAS_NEEDS_CONFIRMATION","COMMANDER_IDENTITY_CONFLICT")
            if e["source_identity_discrepancy"]=="COMMANDER_IDENTITY_CONFLICT":
                assert e["canonical_deck_id"]=="Goben__Gene_Splice_Savant"
                assert e["engineering_deck_id"]=="Norman_Osborn_Green_Goblin"
        if e["status"]=="DEEP_REVIEW_COMPLETE":
            assert not unfinished, "No later entry may be completed before earlier unfinished deck"
            assert e["deep_review_evidence_path"] and e["completed_at_commit"] and e["ci_run_url"]
            assert re.fullmatch(r"[0-9a-f]{40}",e["completed_at_commit"])
            assert e["ci_run_url"].startswith("https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/")
            artifact=ROOT/e["deep_review_evidence_path"]
            assert artifact.is_file() and str(artifact.resolve()).startswith(str((ROOT/"data/grixis/m6/deep_reviews").resolve()))
            content=artifact.read_text(encoding="utf-8")
            assert e["baseline_approved_sha256"] in content and e["tracker_deck_id"] in content
            assert all(h in content for h in HEADINGS)
            if e["source_identity_discrepancy"]=="COMMANDER_IDENTITY_CONFLICT":
                assert "Goben" in content and "Norman" in content and "resolved" in content.lower()
            assert e["blocker"] is None
            completed+=1
        else:
            unfinished.append(e)
            assert e["deep_review_evidence_path"] is None
            assert e["completed_at_commit"] is None
            assert e["ci_run_url"] is None
            if e["status"] in {"IN_PROGRESS","BLOCKED"}:
                active.append(e)
                if e["status"]=="BLOCKED":assert e["blocker"]
                else:assert e["blocker"] is None
            else:
                assert e["blocker"] is None
    assert p["deep_review_complete_count"]==completed
    assert len(active)<=1
    if unfinished:
        assert p["next_tracker_deck_id"]==unfinished[0]["tracker_deck_id"]
        assert p["active_tracker_deck_id"]==(active[0]["tracker_deck_id"] if active else None)
        if active:assert active[0]["tracker_deck_id"]==unfinished[0]["tracker_deck_id"]
        assert p["ready_for_grokbot_pass_c"] is False
        assert all(e["status"]=="PENDING" for e in unfinished[1:])
    else:
        assert p["next_tracker_deck_id"] is None and p["active_tracker_deck_id"] is None
        assert p["ready_for_grokbot_pass_c"] is True
        assert completed==62
    assert p["completed_reviews_are_distinct_from_m6_4_authored_coverage"] is True
    return completed
def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--check",action="store_true")
    args=cli.parse_args()
    if not args.check:cli.error("Pass --check")
    n=validate(load(LEDGER),load(REG))
    print(f"PASS: deep commander-first single-deck reviews {n}/62; historical M6.4 62/62; Pass C not implied.")
if __name__=="__main__":main()
