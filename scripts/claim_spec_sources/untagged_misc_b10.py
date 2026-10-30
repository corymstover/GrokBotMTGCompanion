from mv import spec
C,I="CANON_CONFIRMED","CANON_IMPLIED"
spec("pack_p5_untagged_misc_b10","","magic_origins_and_ravnica_vignettes_2015_2019",
"Batch 10 extraction from remaining untagged Magic Story pages: Jace's Origin, the Magic Origins planes primer, the Jund vignette "
"'All Cairns Lead to Jund', and three Guilds of Ravnica / Ravnica Allegiance guild vignettes. PRELIMINARY_RESEARCH; targeted, "
"not exhaustive; not owner approved.",
{"mb_jace":"jaces-origin-absent-minds-2015-06-24","mb_worlds":"worlds-magic-origins-2015-07-09","mb_jund":"all-cairns-jund-2015-11-04",
 "mb_fog":"under-cover-fog-2018-10-10","mb_death":"deaths-precious-moments-2018-11-07","mb_simic":"principles-unnatural-selection-2019-02-06"},
[("alhammarret","Character","Alhammarret"),("jace_beleren","Character","Jace Beleren"),("eldrazi_titans","Concept","Eldrazi titans"),
 ("zendikar","Plane","Zendikar"),("rakdos","Character","Rakdos"),("rakdos_cult","Faction","Cult of Rakdos"),
 ("meren","Character","Meren of Clan Nel Toth"),("nel_toth","Faction","Clan Nel Toth"),("kael","Character","Kael"),
 ("lazav","Character","Lazav"),("house_dimir","Faction","House Dimir"),("vraska","Character","Vraska"),("golgari","Faction","Golgari Swarm"),
 ("zegana","Character","Zegana"),("simic_combine","Faction","Simic Combine")],
[
("MB001","alhammarret","mentored","jace_beleren",I,[("mb_jace","He’d spent two years as the sphinx’s apprentice, learning the full abilities"),
   ("mb_jace","Even purely out of self-interest, Alhammarret had to covet a planeswalker apprentice.")],
 "The sphinx Alhammarret took the young Jace Beleren as his apprentice for two years (Jace's past, on Vryn).",
 "The apprentice sentence names 'the sphinx'; the sphinx is identified as Alhammarret by the neighbouring sentence."),
("MB002","eldrazi_titans","trapped_on","zendikar",C,[("mb_worlds","Six thousand years ago, three Planeswalkers lured the three Eldrazi titans—horrific, world-devouring entities—to Zendikar, and trapped them there.")],
 "In the past, three Planeswalkers lured the three Eldrazi titans to Zendikar and trapped them there.",
 "Primer page; the three Planeswalkers are not named in this sentence."),
("MB003","rakdos","leader_of","rakdos_cult",I,[("mb_worlds","Rakdos, aligned with black and red mana, is an endless carnival of depraved revelry. Their leader is an ancient demon named Rakdos")],
 "The demon Rakdos leads the Rakdos guild (Magic Origins primer, 2015).","'Rakdos' in the first sentence names the guild; 'Their leader' refers back to it."),
("MB004","meren","member_of","nel_toth",C,[("mb_jund","You are Meren, shaman apprentice of the Nel Toth.")],
 "Meren is a shaman apprentice of Clan Nel Toth on Jund."),
("MB005","kael","mentored","meren",I,[("mb_jund","She scanned the familiar faces of the Circle, finding her master, Kael, sitting tall and proud, watching closely.")],
 "Kael is Meren's master in the Circle of Nel Toth.","Point-of-view narration; 'She' is the viewpoint character Meren."),
("MB006","lazav","leader_of","house_dimir",C,[("mb_fog","Lazav the Mastermind, Guildmaster of House Dimir?")],
 "Lazav is Guildmaster of House Dimir (Guilds of Ravnica, 2018).","Spoken as a question by a character recognising him."),
("MB007","vraska","leader_of","golgari",I,[("mb_death","Vraska, our guildmaster, is worried the Boros will use this as another excuse to infiltrate the undercity")],
 "Vraska is guildmaster of the Golgari (Guilds of Ravnica, 2018).","First-person Golgari narrator; the guild is identified by context (the undercity, 'the Golgari guildhall'), not named in the quote."),
("MB008","zegana","leader_of","simic_combine",I,[("mb_simic","She looks so much like Utopian Speaker Zegana—a younger, more petulant version of our leader"),
   ("mb_simic","Perhaps it is a good thing knowing that our Combine is not fragile enough")],
 "Utopian Speaker Zegana leads the Simic Combine (Ravnica Allegiance, 2019).","First-person Simic narrator; 'our leader' and 'our Combine' are the narrator's guild."),
],
["Targeted. Read for relations but not graded: magosi-steps-2020-09-10, hunger-2020-09-25, unbowed-part-1, testing-dark-waters, clans-legions, "
 "bound-and-bonded, ledger-hidden-fortunes (relations mostly among unnamed or one-off characters)."])
