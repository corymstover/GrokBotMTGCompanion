from mv import spec
C,I="CANON_CONFIRMED","CANON_IMPLIED"
spec("pack_p5_untagged_isd_guides","","innistrad_2011",
"Batch 10 extraction from the untagged 2011 'Planeswalker's Guide to Innistrad' features (official Wizards). "
"PRELIMINARY_RESEARCH; targeted, not exhaustive; not owner approved.",
{"ig_intro":"planeswalkers-guide-innistrad-introduction-2011-08-24","ig_gav":"planeswalkers-guide-innistrad-gavony-and-humans-2011-09-28",
 "ig_kes":"planeswalkers-guide-innistrad-kessig-and-werewolves-2011-10-05","ig_neph":"planeswalkers-guide-innistrad-nephalia-and-undead-2011-10-19",
 "ig_sten":"planeswalkers-guide-innistrad-stensia-and-vampires-2011-11-02"},
[("thraben","Place","Thraben"),("gavony","Place","Gavony"),("avacyn","Character","Avacyn"),("church_of_avacyn","Faction","Church of Avacyn"),
 ("innistrad","Plane","Innistrad"),("edgar_markov","Character","Edgar Markov"),("sorin_markov","Character","Sorin Markov"),
 ("markov_manor","Place","Markov Manor"),("olivia_voldaren","Character","Olivia Voldaren"),("elgaud_grounds","Place","Elgaud Grounds"),("nephalia","Place","Nephalia")],
[
("IG001","thraben","located_in","gavony",C,[("ig_gav","It is home to Thraben, the plane's largest city.")],
 "Thraben, Innistrad's largest city, is in Gavony.","'It' is Gavony, the province this guide section covers."),
("IG002","avacyn","resided_in","thraben",C,[("ig_gav","Thraben houses the Cathedral of Avacyn, where the archangel herself resided before vanishing.")],
 "Avacyn resided at the Cathedral of Avacyn in Thraben before vanishing (Innistrad 2011)."),
("IG003","church_of_avacyn","religion_of","innistrad",C,[("ig_intro","Humanity's true religion on Innistrad is the Church of Avacyn.")],
 "The Church of Avacyn is humanity's religion on Innistrad."),
("IG004","avacyn","disappeared_from","innistrad",C,[("ig_kes","Ever since Avacyn went missing last year, the church at Thraben has kept the truth of her disappearance from Innistrad's denizens.")],
 "Avacyn went missing, and the church at Thraben hid her disappearance (Innistrad 2011)."),
("IG005","edgar_markov","grandparent_of","sorin_markov",C,[("ig_sten","Markov Manor is the home of Edgar Markov, grandfather of Sorin Markov.")],
 "Edgar Markov is Sorin Markov's grandfather."),
("IG006","edgar_markov","resides_in","markov_manor",C,[("ig_sten","Markov Manor is the home of Edgar Markov, grandfather of Sorin Markov.")],
 "Markov Manor is Edgar Markov's home in Stensia."),
("IG007","church_of_avacyn","founded","elgaud_grounds",C,[("ig_neph","A contingent of the Avacyn Church long ago established a small fort here known as the Elgaud Grounds where new cathars are trained")],
 "A contingent of the Church of Avacyn long ago established the Elgaud Grounds fort, where new cathars are trained."),
],
["Targeted. Olivia Voldaren's invented holiday (Stensia) not yet graded."])
