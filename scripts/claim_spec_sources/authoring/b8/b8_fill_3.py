# applied once: KLD/AER remaining 3 pages
from patch_spec import patch
C,I="CANON_CONFIRMED","CANON_IMPLIED"
patch("kld.py",
 pages={"kld_born_aether":"born-aether-2016-09-21","kld_time_innovation":"time-innovation-2016-08-31","aer_quiet_moments":"quiet-moments-2016-12-07"},
 ents=[("yahenni","Character","Yahenni"),("depala","Character","Depala"),("mitul","Character","Mitul")],
 claims=[
 ("KLD010","consulate","imprisoned","pia_nalaar",C,[("kld_born_aether","Pia Nalaar was captured, you know."),("kld_born_aether","I don't know where the Consulate would take prisoners of Pia's standing.")],
  "Yahenni tells Chandra and Nissa that Pia was captured and taken prisoner by the Consulate."),
 ("KLD011","yahenni","friend_of","depala",C,[("kld_born_aether","My dear friend and ace pilot Depala")],
  "Yahenni calls the pilot Depala a dear friend."),
 ("KLD012","yahenni","aided","chandra_nalaar",I,[("kld_born_aether","Pia Nalaar's daughter looks at me with genuine surprise."),("kld_born_aether","three unexpected guests arrive seeking dangerous knowledge")],
  "Chandra (with Nissa) comes to Yahenni's party seeking information about her captured mother.",
  "The recap says the guests seek dangerous knowledge; whether Yahenni's information counts as help is an editorial reading."),
 ("KLD013","mitul","serves","rashmi",C,[("kld_time_innovation","Her vedalken assistant, Mitul, placed the tool on her palm.")],
  "Mitul is Rashmi's vedalken lab assistant."),
 ("KLD014","rashmi","created","aether_kaladesh",I,[("kld_time_innovation","Her groundbreaking aether condenser")],
  "Rashmi invented a groundbreaking aether condenser to power her matter-transportation device.",
  "Modelled against the generic aether concept node; the condenser itself is not a separate entity."),
 ("AER016","tezzeret","leader_of","consulate",C,[("aer_quiet_moments","With Tezzeret still maintaining control and leadership of the Consulate")],
  "During the Aether Revolt crackdown, Tezzeret controls and leads the Consulate."),
 ("AER017","gatewatch","aided","renegades_kaladesh",C,[("aer_quiet_moments","aiding Pia and the renegades where they could, seeking out information on Tezzeret's plans")],
  "The Gatewatch hides in Ghirapur and aids Pia and the renegades."),
 ],
 remaining=("Time for Innovation, Born of Aether, Quiet Moments and the Planeswalker's Guide are only lightly modelled or uncited","Time for Innovation, Born of Aether and Quiet Moments are only lightly modelled (a few claims each)"))
