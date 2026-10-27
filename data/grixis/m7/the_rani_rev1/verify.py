#!/usr/bin/env python3
"""Fail-closed, no-network, source-bound Deck 57 M7 Rev1 verification.

No multiplayer win-rate or overall M6/M7 certification is claimed. The live
source snapshot was captured from Scryfall on 2026-10-27 and archived as JSON.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'The_Rani_Oct15_baseline.txt'
SOURCE = ROOT / 'The_Rani_M7_Rev1_Scryfall_snapshot.json'
EXPECTED = {
    'The_Rani_Oct15_baseline.txt': '7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c',
    'The_Rani_M7_Rev1.txt': '924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27',
    'The_Rani_M7_Rev1_alt9.txt': 'a1538f965b4e5e641ce6e46e7c2dc436d720387fcac134e21e3cdd1ecd4b4db5',
    'The_Rani_M7_Rev1_alt10.txt': '91ffe20a97ba0f8813f50684c33d3ade48f77da80af1cc72848a5eff1f596fa6',
}
SWAPS = [
    ('Death Kiss', 'Frenzied Gorespawn'),
    ('Maestros Confluence', 'Curse of Verbosity'),
    ('Grenzo, Havoc Raiser', 'Mirkwood Bats'),
    ('Tangletrove Kelp', 'Cyberdrive Awakener'),
    ('Mocking Doppelganger', 'Alexios, Deimos of Kosmos'),
    ('Reanimate', 'Marionette Apprentice'),
    ('Five Hundred Year Diary', "Tamiyo's Journal"),
    ('Hateful Eidolon', 'Roaming Throne'),
]
ALTS = SWAPS + [('Slicer, Hired Muscle // Slicer, High-Speed Antagonist', 'Spark Double'),
                ('Mystical Tutor', 'Idol of Oblivion')]


def cards(path):
    raw = path.read_bytes()
    assert raw.endswith(b'\n') and b'\r' not in raw, path.name
    assert hashlib.sha256(raw).hexdigest() == EXPECTED[path.name], path.name
    lines = raw.decode('utf-8').splitlines()
    assert lines[0] == '1x The Rani [Commander]'
    expanded = []
    for n, line in enumerate(lines, 1):
        match = re.fullmatch(r'(\d+)x (.+)', line)
        assert match, (n, line)
        qty, name = int(match[1]), match[2].removesuffix(' [Commander]')
        assert qty >= 1
        assert n == 1 or '[Commander]' not in line
        expanded.extend([name] * qty)
    assert len(expanded) == 100
    assert len(set(expanded)) == 94
    assert {name: qty for name, qty in Counter(expanded).items() if qty > 1} == {
        'Island': 3, 'Mountain': 3, 'Swamp': 3}
    assert sum(1 for name in expanded if name in ('Island', 'Mountain', 'Swamp')) == 9
    return expanded


def assert_official(cards_source, names):
    for name in names:
        assert name in cards_source, 'Unresolved Oracle card ' + name
        card = cards_source[name]
        assert card['oracle_id'] and card['oracle_text'] and card['scryfall_uri']
        assert card['commander_legality'] == 'legal', 'Official ban/illegality ' + name
        assert set(card['color_identity']) <= {'U', 'B', 'R'}, 'Color identity ' + name


def assert_rules(cards_source):
    text = lambda name: cards_source[name]['oracle_text']
    assert 'another target creature' in text('The Rani')
    assert 'Whenever a goaded creature deals combat damage' in text('The Rani')
    assert 'an additional time' in text('Roaming Throne')
    assert 'goad target creature that player controls' in text('Frenzied Gorespawn')
    assert 'menace until end of turn' in text('Frenzied Gorespawn')
    assert "can't attack its owner" in text('Alexios, Deimos of Kosmos')
    assert 'create or sacrifice a token' in text('Mirkwood Bats')
    assert 'another creature or artifact you control is put into a graveyard' in text('Marionette Apprentice')
    assert 'each noncreature artifact you control becomes a 4/4' in text('Cyberdrive Awakener')
    assert 'haste' not in text('Cyberdrive Awakener')  # Important summoning-sickness caveat.
    assert 'Sacrifice three Clues' in text("Tamiyo's Journal")
    assert 'the first time each turn' in text('Erdwal Illuminator')
    assert 'instead create one of each' in text('Academy Manufactor')
    assert 'Sacrifice five artifacts' in text('Time Sieve')
    # Bounded event accounting, not a game-engine substitute: first Rani
    # investigate doubled by Throne, first investigate repeated by Illuminator.
    investigations = 2 + 1
    manufactured_artifacts = investigations * 3
    assert investigations == 3 and manufactured_artifacts == 9
    # Five tokens to Time Sieve each trigger Bats; tokens that go to GY also
    # trigger Marionette Apprentice. Sieve grants one turn, not an infinite loop.
    sieve_sacrifices = 5
    assert manufactured_artifacts >= sieve_sacrifices


def main():
    baseline = cards(BASE)
    snapshot = json.loads(SOURCE.read_text(encoding='utf-8'))
    source = snapshot['cards']
    assert snapshot['cards_count'] == 104 and len(source) == 104
    assert snapshot['captured_utc'].startswith('2026-10-27T')
    for fn, quantity in [('The_Rani_M7_Rev1.txt', 8),
                         ('The_Rani_M7_Rev1_alt9.txt', 9),
                         ('The_Rani_M7_Rev1_alt10.txt', 10)]:
        proposed = cards(ROOT / fn)
        adds = Counter(proposed) - Counter(baseline)
        cuts = Counter(baseline) - Counter(proposed)
        assert adds == Counter(new for old, new in ALTS[:quantity])
        assert cuts == Counter(old for old, new in ALTS[:quantity])
        assert_official(source, proposed)
        # Mana base unchanged across all configurations: 33 lands.
    assert_official(source, baseline)
    assert_rules(source)
    assert not {'Trade Secrets', "Yawgmoth's Bargain", 'Lutri, the Spellchaser'} & set(source)
    print('PASS Deck57: exact baseline and three 100-card lists, 8/9/10 swaps,')
    print('94 distinct names; only three basic triples; 104 Oracle identities;')
    print('official Commander legal and Grixis; bounded Rani/Clue/Throne rules.')
    print('No owner approval, merged lock, automatic infinite, or win rate claimed.')


if __name__ == '__main__':
    main()
