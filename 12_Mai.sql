select 
Distinct a.mandanten.name, a.mandanten.mandantid, a.mandanten.mvp, a.leistungen.rechnungslauf_ok, SUM(a.leistungen.minutes)
from 
(select arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid, arvensteyn_dev22.mandanten.mvp, SUM(arvensteyn_dev22.leistungen.minutes from 
arvensteyn_dev22.mandanten
inner join arvensteyn_dev22.auftraege on arvensteyn_dev22.auftraege.mdt = arvensteyn_dev22.mandanten.mandantid
inner join arvensteyn_dev22.leistungen on arvensteyn_dev22.leistungen.auftrag = arvensteyn_dev22.auftraege.id
GRoup by
arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid, arvensteyn_dev22.mandanten.mdt_id_lz, arvensteyn_dev22.leistungen.rechnungslauf_ok
having 
arvensteyn_dev22.mandanten.mvp = 11 AND rechnungslauf_ok = 'false'
order by
arvensteyn_dev22.mandanten.mandantid) as a
where a.l_datum Between '2022-05-01' AND '2022-05-11'

