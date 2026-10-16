"""Bot cycle 53: deck labels keep the full deck name on rebuild.

build_grixis.py rewrites grixis/decks/*.md without front matter, and the rebuild chain runs build_crossrefs.py and
build_packages.py before front_matter.py restores it. Deck labels used to fall back to the file slug in that window,
so EDH Packages.md lost the full names ("nicol-bolas" instead of "Nicol Bolas (Grixis)")."""
import re
import tempfile
from pathlib import Path

from _helpers import ROOT, skip

import build_crossrefs as bx
import front_matter as fm

SLUG_LABEL = re.compile(r"\[([a-z0-9-]+)\]\((?:grixis/)?decks/\1\.md\)")


def _strip_fm(text):
    m = fm.FM.match(text)
    return text[m.end():] if m else text


def test_label_without_front_matter_uses_commander_name():
    src = ROOT / "grixis" / "decks" / "nicol-bolas.md"
    if not src.exists():
        skip("fixture deck page missing")
    with tempfile.TemporaryDirectory() as td:
        page = Path(td) / "grixis" / "decks" / "nicol-bolas.md"
        page.parent.mkdir(parents=True)
        page.write_text(_strip_fm(src.read_text(encoding="utf-8")), encoding="utf-8")
        meta = bx.meta_of(page)
        assert meta.get("kind") == "grixis"
        assert bx.deck_label("grixis/decks/nicol-bolas.md", meta) == "Nicol Bolas (Grixis)"


def test_label_with_front_matter_unchanged():
    src = ROOT / "grixis" / "decks" / "nicol-bolas.md"
    if not src.exists():
        skip("fixture deck page missing")
    assert bx.deck_label("grixis/decks/nicol-bolas.md", bx.meta_of(src)) == "Nicol Bolas (Grixis)"


def test_non_deck_page_without_front_matter_has_no_meta():
    with tempfile.TemporaryDirectory() as td:
        page = Path(td) / "notes.md"
        page.write_text("# Notes\n\n- **[Nicol Bolas](x)**\n", encoding="utf-8")
        assert bx.meta_of(page) == {}


def test_edh_packages_has_no_slug_only_deck_labels():
    pk = ROOT / "EDH Packages.md"
    if not pk.exists():
        skip("EDH Packages.md missing")
    bad = SLUG_LABEL.findall(pk.read_text(encoding="utf-8"))
    assert not bad, f"slug-only deck labels in EDH Packages.md: {sorted(set(bad))[:5]}"


def test_deck_packages_json_labels_are_names():
    import json
    dp = ROOT / "data" / "deck_packages.json"
    if not dp.exists():
        skip("data/deck_packages.json missing")
    text = json.dumps(json.loads(dp.read_text(encoding="utf-8")))
    labels = re.findall(r'"label": "([^"]+)"', text)
    slugs = [x for x in labels if re.fullmatch(r"[a-z0-9-]+", x)]
    assert not slugs, f"slug-only labels in data/deck_packages.json: {slugs[:5]}"
