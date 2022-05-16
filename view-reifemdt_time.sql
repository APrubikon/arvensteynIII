select 
arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid, arvensteyn_dev22.mandanten.mdt_id_lz, arvensteyn_dev22.leistungen.lbeschreibung, arvensteyn_dev22.leistungen.minutes, arvensteyn_dev22.auftraege.auftragsbezeichnung, arvensteyn_dev22.auftraege.az, arvensteyn_dev22.leistungen.l_datum 
from 
arvensteyn_dev22.mandanten
inner join arvensteyn_dev22.auftraege on arvensteyn_dev22.auftraege.mdt = arvensteyn_dev22.mandanten.mandantid
inner join arvensteyn_dev22.leistungen on arvensteyn_dev22.leistungen.auftrag = arvensteyn_dev22.auftraege.id and arvensteyn_dev22.leistungen.l_datum between '2022-05-01' aND '2022-05-31'
order by
arvensteyn_dev22.mandanten.mandantid

