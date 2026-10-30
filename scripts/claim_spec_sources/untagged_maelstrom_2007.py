from mv import spec
C,I="CANON_CONFIRMED","CANON_IMPLIED"
spec("pack_p5_untagged_maelstrom_2007","","tempest_rath_2007_retold",
"Batch 10 extraction from the untagged 2007 web stories 'Maelstrom' and 'Torrent' (Starke's betrayal of Sisay, Tempest-era Rath). "
"PRELIMINARY_RESEARCH; targeted, not exhaustive; not owner approved.",
{"ml_mael":"maelstrom","ml_torr":"torrent"},
[("starke","Character","Starke"),("volrath","Character","Volrath"),("maraxus","Character","Maraxus"),
 ("starkes_daughter","Character","Starke's daughter (unnamed in these stories)"),("sisay","Character","Captain Sisay"),
 ("weatherlight","Object","Weatherlight (skyship)"),("gerrard","Character","Gerrard Capashen")],
[
("ML001","volrath","imprisoned","starkes_daughter",C,[("ml_mael","This servant, Volrath, is holding Starke's daughter prisoner.")],
 "In the past (Tempest era), Volrath held Starke's daughter prisoner."),
("ML002","starke","serves","volrath;maraxus",C,[("ml_torr","Volrath and Maraxus still refused to free him from servitude and still refused to free his daughter.")],
 "In the past (Tempest era), Starke was held in servitude by Volrath and Maraxus."),
("ML003","starke","betrayed","sisay",C,[("ml_torr","They had taken Sisay—and Starke had helped them."),
   ("ml_torr","He had gained nothing by betraying Sisay")],
 "In the past (Tempest era), Starke betrayed Sisay and helped her captors take her."),
("ML004","sisay","captain_of","weatherlight",I,[("ml_mael","Sisay of the Weatherlight said to the Talruum minotaur"),
   ("ml_torr","Captain Sisay, however—who would serve Starke's purposes just as well—was still around.")],
 "In the past (Tempest era), Sisay was captain of the Weatherlight.","'Captain' and 'of the Weatherlight' come from separate sentences in the two stories."),
("ML005","starke","lured","gerrard",I,[("ml_torr","he had deliberately placed a sigil in Sisay's kidnapping letter to bring Gerrard to Crovax's estate")],
 "In the past (Tempest era), Starke secretly signalled in Sisay's kidnapping letter to bring Gerrard to Crovax's estate.",
 "The sentence's 'he' is Starke from the surrounding narration."),
],
["Targeted. Crovax and the Talruum minotaur guard are mentioned but not graded."])
