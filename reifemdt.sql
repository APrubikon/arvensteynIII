select 
DIstinct arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid, arvensteyn_dev22.mandanten.mdt_id_lz, SUM(arvensteyn_dev22.leistungen.minutes)
from 
arvensteyn_dev22.mandanten

inner join arvensteyn_dev22.auftraege on arvensteyn_dev22.auftraege.mdt = arvensteyn_dev22.mandanten.mandantid
inner join arvensteyn_dev22.leistungen on arvensteyn_dev22.leistungen.auftrag = arvensteyn_dev22.auftraege.id
GRoup by
arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid, arvensteyn_dev22.mandanten.mdt_id_lz
order by
arvensteyn_dev22.mandanten.mandantid

