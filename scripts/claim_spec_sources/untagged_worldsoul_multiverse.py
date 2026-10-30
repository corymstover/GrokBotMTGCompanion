from mv import spec
C,I="CANON_CONFIRMED","CANON_IMPLIED"
spec("pack_p5_untagged_worldsoul_multiverse","","worldsoul_ravnica_2019_known_multiverse_2008_orzhov_feature_2013",
"Batch 11 extraction from In Praise of the Worldsoul parts 1-3 (Ravnica), The Known Multiverse (2008 planes primer) and the 2013 "
"Behind the Black Sun Orzhov feature. Claims are as of each page. PRELIMINARY_RESEARCH; targeted, not exhaustive; not owner approved.",
{"w1":"in-praise-of-the-worldsoul-part-1","w2":"in-praise-of-the-worldsoul-part-2","w3":"in-praise-of-the-worldsoul-part-3",
 "km":"known-mutliverse-2008-03-19","bbs":"behind-black-sun-2013-03-25"},
[("ruzi","Character","Ruzi"),("cecilee","Character","Cecilee"),("kuma","Character","Kuma"),("selesnya_conclave","Faction","Selesnya Conclave"),
 ("nikya","Character","Nikya"),("gruul_clans","Faction","Gruul Clans"),("massacre_girl","Character","Massacre Girl"),("rakdos_cult","Faction","Rakdos Cult"),
 ("karn","Character","Karn"),("mirrodin","Plane","Mirrodin"),("memnarch","Character","Memnarch"),("yawgmoth","Character","Yawgmoth"),
 ("old_phyrexia","Plane","Phyrexia"),("dyfed","Character","Dyfed"),("serra","Character","Serra"),("serras_realm","Plane","Serra's Realm"),
 ("teysa_karlov","Character","Teysa Karlov"),("obzedat","Faction","Obzedat")],
[
("WSM001","ruzi","member_of","selesnya_conclave",C,[("w1","As Master Trainer, Ruzi taught the youngest Selesnyans and their wolves to become Wolf Riders.")],"Ruzi is the Selesnya Master Trainer of Wolf Riders."),
("WSM002","ruzi","bonded_with","kuma",C,[("w1","the three of them—Cecilee, Ruzi, and his wolf Kuma—had been inseparable")],"Kuma is Ruzi's wolf."),
("WSM003","cecilee","sibling_of","ruzi",C,[("w2","Cecilee named the child after her brother, Ruzi")],"Cecilee is Ruzi's sister."),
("WSM004","nikya","member_of","gruul_clans",I,[("w2","She explained that Nikya claimed the boy as kin and demanded he be raised as Gruul.")],"Nikya claims the child as kin and demands he be raised Gruul.","Nikya's Gruul membership is inferred from her demand."),
("WSM005","massacre_girl","member_of","rakdos_cult",C,[("w2","She didn't know the woman was a for-hire Rakdos killer who called herself Massacre Girl.")],"Massacre Girl is a for-hire Rakdos killer (as of this story)."),
("WSM006","massacre_girl","attacked","selesnya_conclave",I,[("w3","The two surprised Massacre Girl and her men as they searched the bodies for anything valuable."),("w3","Ruzi glimpsed the bodies of his fellows Selesnyans near the desecrated guild-tree.")],
 "Massacre Girl and her men are found among the Selesnyan dead at the desecrated guild-tree.","The page implies, but these lines do not state, that she carried out the killings."),
("WSM007","karn","created","mirrodin",C,[("km","The artificial, metal plane of Mirrodin was created by the planeswalker Karn.")],"Karn created Mirrodin (as of 2008)."),
("WSM008","karn","created","memnarch",I,[("km","Karn also created an artifact warden to watch over the plane while he explored the multiverse."),("km","Karn transformed the remains of Memnarch into the metal sphere they had once been: the Mirari.")],
 "Karn created an artifact warden for Mirrodin, which became Memnarch (as of 2008).","The warden-to-Memnarch identity is implied across sentences."),
("WSM009","dyfed","brought","yawgmoth",C,[("km","the planeswalker Dyfed took Yawgmoth to Phyrexia shortly after its creator and master had died")],"Dyfed took Yawgmoth to Phyrexia during the Thran decline."),
("WSM010","yawgmoth","trapped_on","old_phyrexia",C,[("km","The Thran were defeated, but not before the portal was closed, trapping Yawgmoth and the Phyrexians in their plane.")],"Yawgmoth and the Phyrexians were trapped in Phyrexia when the portal closed."),
("WSM011","serra","created","serras_realm",C,[("km","This artificial plane was created by the planeswalker Serra to exemplify her love of peace and law.")],"Serra created Serra's Realm."),
("WSM012","obzedat","commanded","teysa_karlov",I,[("bbs","I have come from the ghost halls of the Obzedat with a message for Teysa Karlov."),("bbs","Teysa Karlov must find the correct route and complete the maze at all costs.")],
 "A messenger from the Obzedat tells Teysa Karlov she must complete the maze (2013 feature).","Rendered as a command from the Obzedat; the feature frames it as a message."),
],[])
