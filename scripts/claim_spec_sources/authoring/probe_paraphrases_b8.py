import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts")); import mv_ask as A
Q=[("Who killed the Buried Lord?","MV016"),("Who beheaded the Buried Lord?","MV016"),("Who was the Buried Lord killed by?","MV016"),
("Who killed Isperia?","WR001"),("Who murdered Isperia?","WR001"),
("Who leads the Omenseekers?","KH020"),("Who is the leader of the Omenseekers?","KH020"),("Who runs the Omenseekers?","KH020"),
("Who is Killian Lu's father?","SX017"),("Who is Killian's father?","SX017"),("Who are Killian Lu's parents?","SX017"),
("Who is Torens's brother?","MV023"),("Who are Torens's siblings?","MV023"),
("Who is Vadrik's husband?","MV021"),("Who is Vadrik's spouse?","MV021"),
("Who mentored Melantha?","TS025"),("Who was Melantha's mentor?","TS025"),
("Who defeated Xenagos?","TS033"),
("Who leads the Tuskeri?","KH016"),("Who leads Tynthal?","TS030"),("Who governs Tynthal?","TS030"),
("Who attacked Thraben?","MV014"),("Who is Gisa's brother?","MV015"),("Who are Gisa's siblings?","MV015"),
("Who imprisoned Pia Nalaar?","KLD011"),("Who leads the Consulate?","AER016"),("Who leads the Sun Empire?","XLN023"),("Who founded the Sun Empire?","XLN024"),
("Who is Khrad's father?","DF021"),("Who are Khrad's parents?","DF021"),("Who leads the Brazen Coalition?","XLN019"),("Who captains the Brazen Coalition?","XLN019"),
("Who guards the Immortal Sun?","XLN021"),("Who mentored Kopala?","XLN027"),("Who leads the Telu set?","DF022"),
("Who is Inga Rune-Eyes?","KH020"),("Who is Zimone's friend?","SX012"),("Who are Zimone's friends?","SX012"),("Who fought Lukka?","SX015"),
("Who is Leinore's sister?","MV022"),("Who did Kaya meet?","KH021"),("Who serves Ephara?","TS034"),("Who worships Elenda?","XLN032"),
("Who leads the Izzet?","WR"),("Who is the leader of the Golgari?","WR")]
for q,c in Q:
    env=A.ask(q); rows=[r for v in env.get("result",{}).get("relations_by_status",{}).values() for r in v]
    hit=[r for r in rows if r["claim"].startswith(c)]
    print(env["confidence"][:9].ljust(9), "OK " if hit else "-- ", q, "|", hit[0]["claim"]+" "+hit[0]["node"] if hit else [r["claim"] for r in rows][:4])
