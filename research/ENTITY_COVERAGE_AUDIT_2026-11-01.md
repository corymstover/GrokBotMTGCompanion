# Registered Multiverse planes, regions, factions, artifacts and character audit

**2026-11-01 · source-graded coverage and explicit gaps, NOT a complete canon census.**

**839 registered entities** across the five audited node types; **4** without a direct cited claim and **139** with only qualified direct claims.

| Graph type | Registered | With direct claim | No direct claim | Qualified-only | One confirmed direct claim |
| --- | ---: | ---: | ---: | ---: | ---: |
| Plane | 33 | 33 | 0 | 1 | 0 |
| Place | 112 | 109 | 3 | 14 | 65 |
| Faction | 156 | 156 | 0 | 28 | 68 |
| Object | 54 | 53 | 1 | 9 | 19 |
| Character | 484 | 484 | 0 | 87 | 157 |

## Review priority (connectivity is not canonical importance)

These IDs have no direct cited relation or only qualified direct claims. The machine JSON records **every** registered node, each distinct direct claim ID, grade, official URL and the reason for any coverage gap.

- **Bablovia** (`plane:bablovia`, Plane): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 10; 5 direct claims
- **Calamity Beasts** (`faction:calamity_beasts`, Faction): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 6; 3 direct claims
- **River Heralds** (`faction:river_heralds`, Faction): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 6; 3 direct claims
- **Dina** (`character:dina`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 6; 2 direct claims
- **Koma** (`character:koma`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 6; 2 direct claims
- **The Belligerent** (`artifact:the_belligerent`, Object): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 2 direct claims
- **Alhammarret** (`character:alhammarret`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 2 direct claims
- **Atarka** (`character:atarka`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 2 direct claims
- **Breeches** (`character:breeches`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 1 direct claims
- **Hapatra** (`character:hapatra`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 1 direct claims
- **Krenko** (`character:krenko`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 1 direct claims
- **Phenax** (`character:phenax`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 2 direct claims
- **Ruric Thar** (`character:ruric_thar`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 1 direct claims
- **Silumgar** (`character:silumgar`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 5; 2 direct claims
- **Order of the Holly Leaf** (`faction:blb_order_holly_leaf`, Faction): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 4; 2 direct claims
- **Prismari College** (`faction:prismari_college`, Faction): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 4; 2 direct claims
- **Izoni** (`character:izoni`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 4; 1 direct claims
- **Javy** (`character:javy`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 4; 2 direct claims
- **King Glarb** (`character:king_glarb`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 4; 2 direct claims
- **Njala** (`character:njala`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 4; 2 direct claims
- **Ureni** (`character:ureni`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 4; 1 direct claims
- **Wildsear, Season of Flames** (`character:blb_wildsear`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 4; 2 direct claims
- **Cori Mountain Monastery** (`place:cori_mountain_monastery`, Place): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 3; 1 direct claims
- **Furnace Layer** (`place:furnace_layer`, Place): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 3; 1 direct claims
- **Glen Elendra** (`place:glen_elendra`, Place): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 3; 1 direct claims
- **Murasa** (`place:murasa`, Place): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 3; 1 direct claims
- **Sea Gate** (`place:sea_gate`, Place): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 3; 1 direct claims
- **Chronomaton** (`artifact:chronomaton`, Object): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 3; 1 direct claims
- **Anthousa** (`character:anthousa`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 3; 1 direct claims
- **Arni Brokenbrow** (`character:arni_brokenbrow`, Character): ONLY_QUALIFIED_DIRECT_CLAIMS; graph degree 3; 1 direct claims

## Hard boundaries

- Graph registration is a curated inventory, not the universe of all MTG planes, regions, factions, objects or people.
- One direct claim is not a complete biography, regional survey, faction membership or object history.
- An officially cited disputed, implied or alternate-continuity claim is not automatically CANON_CONFIRMED.
- Graph degree ranks only local research connectivity, never canonical historical importance.
- This audit inventories evidence and gaps; it does not create unsupported lore edges or resolve contradictions.

Rebuild: `python3 scripts/audit_entity_coverage.py`; verify: `python3 scripts/audit_entity_coverage.py --check`. A listed gap is an **actionable source-research question**, not permission to invent the missing relation.
