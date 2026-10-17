#!/usr/bin/env python3
"""One-shot recorder for Cory's explicit 2026-10-17 M5 acceptance.

Milestone acceptance is evidence-layer authority only. This script must not
change a canonical deck, promote a challenger, decide a swap, approve a deck,
or lock a deck.
"""
from __future__ import annotations

import json
from pathlib import Path

ACCEPTED_AT = "2026-10-17T14:34:41Z"
CORPUS_COMMIT = "fcd28daff7d3f7b091de04299699645ba7e47aa2"
SNAPSHOT = "birthday-20261017-6e5c604e1459"
SUMMARY_SHA256 = "sha256:dfa23cab773832927eb0a0877f8b425581efe1b2e51dcd32b90c53a66d549046"
DELTA_SHA256 = "sha256:8272791232ed31f2d5d0f02bb750dd1e8396745d18bc27d4f8384e82b585bb91"
PROVENANCE_BLOB_SHA1 = "7442fa72e12a14f628cd9907670c25bdcbc37853"


def update_registry() -> None:
    path = Path("data/grixis/registry.json")
    registry = json.loads(path.read_text(encoding="utf-8"))
    m5 = registry["program"]["milestones"]["M5"]
    if m5.get("status") not in {"in_progress", "complete_pending_acceptance", "accepted"}:
        raise SystemExit(f"unexpected M5 state: {m5.get('status')}")
    m5.update(
        {
            "status": "accepted",
            "accepted_by": "corymstover",
            "accepted_date": "2026-10-17",
            "accepted_at": ACCEPTED_AT,
            "acceptance_evidence": (
                "In-chat acceptance by Cory on 2026-10-17 at 14:34:41 UTC: "
                "'Accept M5 and proceed'. Acceptance followed ChatGPT's independent "
                "Cycle 74b validation of the Lift-corrected Birthday M5 corpus. "
                f"Accepted evidence corpus: commit {CORPUS_COMMIT}; snapshot {SNAPSHOT}; "
                f"summary {SUMMARY_SHA256}; provenance blob sha1:{PROVENANCE_BLOB_SHA1}; "
                f"delta {DELTA_SHA256}."
            ),
            "scope_verbatim": "Accept M5 and proceed",
            "scope_note": (
                "Milestone acceptance only. It accepts the Lift-corrected Birthday M5 "
                "evidence corpus for downstream refinement. It approves no card swap, "
                "challenger, canonical decklist change, deck state, deck approval or lock. "
                "data/grixis/birthday_m5/summary.json intentionally remains "
                "accepted_by_cory=false because generated evidence cannot self-accept; "
                "this registry entry is the human acceptance authority."
            ),
        }
    )
    m5.pop("pending_note", None)
    path.write_text(json.dumps(registry, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def update_authority_model() -> None:
    path = Path("grixis/Grixis Authority Model.md")
    text = path.read_text(encoding="utf-8")
    historical = (
        "*Bot cycle 62:* M5 is **exploratory**: non-authoritative evidence only, with no "
        "list changes and no promoted challengers (`program.milestones.M5.pending_note`). "
        "Candidates were regenerated on the corrected blueprints."
    )
    accepted = (
        "*ChatGPT cycle 75 (Cory, 2026-10-17T14:34:41Z):* **M5 accepted.** Cory explicitly "
        "said `Accept M5 and proceed` after independent review of the Lift-corrected Birthday "
        "corpus at commit `fcd28daff7d3f7b091de04299699645ba7e47aa2` / snapshot "
        "`birthday-20261017-6e5c604e1459`. Acceptance is evidence-layer authority only: it "
        "approves no swap, challenger, canonical list, deck state, approval, or lock. The "
        "generated Birthday summary deliberately remains non-self-accepting; "
        "`program.milestones.M5` is the human acceptance record.\n\n"
    )
    if accepted.strip() not in text:
        if historical not in text:
            raise SystemExit("M5 authority-model insertion marker missing")
        text = text.replace(historical, accepted + historical, 1)
    old = "7. ⏳ Cory's acceptance (`program.milestones.M5`)."
    new = (
        "7. ✅ **Cory's acceptance** (`program.milestones.M5`): accepted "
        "2026-10-17T14:34:41Z after the Lift-corrected Birthday rebuild and independent "
        "Cycle 74b review. This accepts M5 evidence only; no swap or deck is approved."
    )
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise SystemExit("M5 criterion-7 marker missing")
    path.write_text(text, encoding="utf-8")


def update_log() -> None:
    path = Path("Update Log.md")
    text = path.read_text(encoding="utf-8")
    toc = "- [2026-10-17 — ChatGPT cycle 75 (M5 accepted)](#2026-10-17--chatgpt-cycle-75-m5-accepted)\n"
    if toc not in text:
        text = text.replace("## Contents\n", "## Contents\n" + toc, 1)
    section = """## 2026-10-17 — ChatGPT cycle 75 (M5 accepted)

- **Summary:** recorded Cory's explicit `Accept M5 and proceed` acceptance of M5 at 2026-10-17T14:34:41Z after ChatGPT independently validated the Lift-corrected Birthday M5 corpus (`fcd28daff7d3f7b091de04299699645ba7e47aa2`, snapshot `birthday-20261017-6e5c604e1459`). M5 acceptance is evidence-layer authority only: no swap, challenger, canonical decklist, deck state, approval, or lock changed.
- **Files:** `data/grixis/registry.json`, `grixis/Grixis Authority Model.md`, `Update Log.md`.
- **Reason:** close the explicit M5 human gate before the agreed post-M5 Birthday prerequisites and M6 architecture.

"""
    first = "## 2026-10-16 — Bot cycle 63 (M2 and M4 accepted)"
    if section not in text:
        if first not in text:
            raise SystemExit("Update Log insertion marker missing")
        text = text.replace(first, section + first, 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_registry()
    update_authority_model()
    update_log()
    print("recorded Cory M5 acceptance without changing deck authority")


if __name__ == "__main__":
    main()
