"""Batch 8 fill 1 (2026-10-30): verbatim-quoted claims for LCI episode 2 and BLB episode 4 + guide part 2.
Applied once to the generator scripts via patch_spec; kept as an authoring record."""
from patch_spec import patch
C,I="CANON_CONFIRMED","CANON_IMPLIED"
patch("lci.py", pages={"lci_ep2":"the-lost-caverns-of-ixalan-episode-2"},
 claims=[
 ("LC013","inti","aided","huatli",C,[("lci_ep2","She and nineteen of her fellow warriors reported to Inti and Caparocti, Imperial officers sent by the emperor to aid Huatli in her mission.")],
  "Inti is one of the Imperial officers sent by the emperor to aid Huatli's expedition.",None,"lci_expedition_2023"),
 ("LC014","amalia","aided","kellan",C,[("lci_ep2","Amalia had misjudged just enough that the man almost fell as well."),("lci_ep2","\"I'm in your debt,\" he said, bowing politely."),("lci_ep2","I'll take responsibility for him. We've lost too many—perhaps he can help.")],
  "Amalia saves Kellan from a fall and vouches for him to Vito.",None,"lci_expedition_2023"),
 ("LC015","kellan","originated_from","eldraine",C,[("lci_ep2","\"Where did you come from?\" Bartolomé asked."),("lci_ep2","\"Eldraine,\" Kellan replied.")],
  "Kellan tells the vampire expedition he came from Eldraine.","He says he came from Eldraine; the passage does not state where he was born."),
 ],
 remaining=("\"Episode 2 is not cited\",","\"Episode 2 is only lightly modelled (Wayta's point of view is not graded)\","))
patch("lci.py", ents=[("eldraine","Plane","Eldraine")])
patch("blb.py", pages={"blb_ep4":"episode-4-soothsaying-and-stormcalling","blb_guide2":"planeswalkers-guide-to-bloomburrow-part-2"},
 ents=[("coffey","Character","Coffey"),("hugs","Character","Hugs"),("gev","Character","Gev"),("ratfolk_valley","Faction","Ratfolk of Valley"),("valley","Place","Valley")],
 claims=[
 ("BL013","coffey","aided","mabel",C,[("blb_ep4","These strangers are not like the others,\" he said, a slight wheeze in his soft voice. \"The River brought them to us. We must offer them hospitality."),("blb_ep4","Perhaps we might even assist in your quest. Yes?")],
  "The ratfolk elder Coffey takes Mabel's party in and offers help with their quest.",None),
 ("BL014","cruelclaw","allied_with","maha",C,[("blb_ep4","He led his band through the swamp, pilfering what supplies he pleased, the Night Owl wreaking havoc in his wake.")],
  "Cruelclaw's band travels with the Night Owl (Maha).","Coffey's account; Maha is identified as 'the Night Owl'."),
 ("BL015","gev","friend_of","hugs",C,[("blb_ep4","It is as well, because now I have the job to remove the so-many stickers from the fur of my friend Hugs.")],
  "Gev calls Hugs his friend."),
 ("BL016","coffey","member_of","ratfolk_valley",C,[("blb_ep4","We're lorekeepers,\" Coffey replied, breathing like a leaky bellows. \"We preserve the history of Bloomburrow and Valley within it.")],
  "Coffey speaks for the ratfolk lorekeepers."),
 ("BL017","ratfolk_valley","guardian_of","valley",I,[("blb_guide2","Ratfolk are the secret-keepers of Valley, collectors of relics and knowledge from as early as the foundation of Valley itself.")],
  "The ratfolk are Valley's secret-keepers.","'Secret-keepers' guard Valley's relics and knowledge, not its territory."),
 ("BL018","valley","located_on","bloomburrow",C,[("blb_ep4","We preserve the history of Bloomburrow and Valley within it.")],
  "Valley lies within Bloomburrow."),
 ],
 remaining=("\"Guide Part 2 is not cited\",\"Hugs, Gev and Finneas are not modelled\"","\"Guide Part 2 is only lightly modelled\",\"Finneas is not modelled\""))
