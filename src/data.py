from PyQt6.QtSql import (QSqlDatabase,
                         QSqlRelationalTableModel,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlTableModel,
                         QSqlDriver,
                         QSqlQuery,
                         QSqlRecord,
                         QSqlQueryModel
                         )

from PyQt6.QtCore import Qt, QSortFilterProxyModel, QRegularExpression , QVariant , QModelIndex
from src.config import currentConfig
from src.db import dbopen

db = dbopen()


class DBModelMdt(QSqlRelationalTableModel):
    def __init__(self):
        super(DBModelMdt, self).__init__()
        self.setTable("arvensteyn_dev22.mandanten")
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setSort(0, Qt.SortOrder.AscendingOrder)
        self.setRelation(3, QSqlRelation("arvensteyn_dev22.partner", "partnerid", "name"))
        self.select()

    def filter_mandantid(self, mandantid):
        filter = f"""'mandantid' = {mandantid}"""
        self.setFilter(filter)

class MandantListe(QSqlQueryModel):
    def __init__(self):
        super(MandantListe, self).__init__()
        query = (f"""select arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid FROM arvensteyn_dev22.mandanten ORDER BY arvensteyn_dev22.mandanten.name ASC""")
        self.setQuery(query)

    def filter_by_name(self, input_name):
        query = f"""select arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid FROM arvensteyn_dev22.mandanten WHERE arvensteyn_dev22.mandanten.name LIKE '%{input_name}%' 
        ORDER BY arvensteyn_dev22.mandanten.name ASC"""
        self.setQuery(query)


class MandantEditmodel(QSqlRelationalTableModel):
    def __init__(self,  mandantid='NULL'):
        super(MandantEditmodel, self).__init__()
        self.setTable("arvensteyn_dev22.mandanten")
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setSort(1, Qt.SortOrder.AscendingOrder)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)
        self.setRelation(3, QSqlRelation("arvensteyn_dev22.partner", "partnerid", "name"))
        filter = (f"""arvensteyn_dev22.mandanten.mandantid = {mandantid}""")
        self.setFilter(filter)
        self.select()

        print(self.lastError().text())

    def update_re(self, newperson):
        query = QSqlQuery(f"""Update arvensteyn_dev22.mandanten SET rechnungsempfaenger = {newperson}""")
        if not self.setQuery(query):
            print(self.lastError().text())





class GV_model(QSqlTableModel):
    def __init__(self, gv_index):
        super(GV_model, self).__init__()

        self.setTable("arvensteyn_dev22.humans")
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)

        filter = (f"""arvensteyn_dev22.humans.index = {gv_index}""")
        self.setFilter(filter)
        self.select()


        print(self.lastError().text())


class REE_model(QSqlTableModel):
    def __init__(self, re_index):
        super(REE_model, self).__init__()

        self.setTable("arvensteyn_dev22.humans")
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setSort(1, Qt.SortOrder.AscendingOrder)
        filter = (f"""arvensteyn_dev22.humans.index = {re_index}""")
        self.setFilter(filter)
        self.select()

        print(self.lastError().text())


class MandantEditmodel_GV(QSqlRelationalTableModel):
    def __init__(self, mandantid='NULL'):
        super(MandantEditmodel_GV, self).__init__()
        self.setTable("arvensteyn_dev22.mandanten")
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setSort(1, Qt.SortOrder.AscendingOrder)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)
        self.setRelation(6, QSqlRelation("arvensteyn_dev22.humans", "index", "full_name"))
        filter = (f"""arvensteyn_dev22.mandanten.mandantid = {mandantid}""")
        self.setFilter(filter)
        self.select()




class DBModelHumans(QSqlTableModel):
    def __init__(self):
        super(DBModelHumans, self).__init__()
        self.setTable("arvensteyn_dev22.humans")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.setSort(0, Qt.SortOrder.AscendingOrder)

    def welcome_human(self, name_full, name_prefix, name_first, name_last, birthday, organization, title, role,
                      work_address1, work_city1, work_zip1, work_phone_1, work_phone_2, work_phone_3, 
                      work_fax, mobile_phone_1, work_email_1, note, url):
        list = [name_prefix, name_first, name_last, birthday, organization, title, role,
                      work_address1, work_city1, work_zip1, work_phone_1, work_phone_2, work_phone_3,
                      work_fax, mobile_phone_1, work_email_1, note, url]
        new_human = self.record()
        new_human.setGenerated(0, False)
        new_human.setValue(2, name_full)
        new_human.setValue(3, name_prefix)
        new_human.setValue(4, name_first)
        new_human.setValue(6, name_last)
        new_human.setValue(9, birthday)
        new_human.setValue(11, organization)
        new_human.setValue(12, title)
        new_human.setValue(13, role)
        new_human.setValue(31, work_address1)
        new_human.setValue(32, work_city1)
        new_human.setValue(33, work_zip1)
        new_human.setValue(49, work_phone_1)
        new_human.setValue(50, work_phone_2)
        new_human.setValue(51, work_phone_3)
        new_human.setValue(55, work_fax)
        new_human.setValue(58, mobile_phone_1)
        new_human.setValue(64, work_email_1)
        new_human.setValue(70, note)
        new_human.setValue(72, url)


        if not self.insertRecord(-1, new_human):
            print(self.lastError().text())

        #lastval = QSqlQuery()
        #lastval.exec("select lastval()")
        #lastval.next()
        #val = lastval.value(0)
        #return val
        #


                                                                                         
class DBModelAuftraege(QSqlRelationalTableModel):
    def __init__(self):
        super(DBModelAuftraege, self).__init__()

        self.setTable('arvensteyn_dev22.auftraege')
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setSort(0, Qt.SortOrder.DescendingOrder)
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)
        self.setRelation(1, QSqlRelation('arvensteyn_dev22.mandanten', 'mandantid', 'name'))
        self.setRelation(6, QSqlRelation('arvensteyn_dev22.gegner', 'id', 'gegner_name'))
        self.setRelation(7, QSqlRelation('arvensteyn_dev22.gegner', 'id', 'gegner_name'))
        self.setRelation(8, QSqlRelation('arvensteyn_dev22.gegner', 'id', 'gegner_name'))
        self.setRelation(9, QSqlRelation('arvensteyn_dev22.humans', 'index', 'full_name'))

        #self.select()
        if not self.select() == True:
            print(f"""{self.lastError().text()}""")

class HumanSearch(QSqlQueryModel):
    def __init__(self):
        super(HumanSearch, self).__init__()
        query = f"""SELECT max(index) FROM arvensteyn_dev22.humans"""
        self.setQuery(query)
        print(self.rowCount())
        self.new_index = self.index(0, 0).data()
        self.result()

    def result(self):
        return self.new_index

class DBModel1(QSqlTableModel):
    def __init__(self):
        super(DBModel1, self).__init__()
        self.setTable('arvensteyn_dev22.mitglieder')
        #self.select()

        self.role = ''
        self.setSort(0, Qt.SortOrder.AscendingOrder)

    def checkKey(self, Mitglied, Passtry):
        query1 = QSqlQuery()
        query1.exec(
            f"""SELECT mitgliedernr, beruf, role, auth FROM arvensteyn_dev22.mitglieder WHERE mitglied = '{Mitglied}';""")

        while query1.next():
            self.Beruf = query1.value('beruf')
            self.role = query1.value('role')
            self.Auth = query1.value('auth')
            self.ID = query1.value('mitgliedernr')
            print(Mitglied, self.Auth, Passtry, self.ID)

        from src.config import Anmeldung
        Anmeldung(ID=self.ID, Kopfzeile=Mitglied, Role=self.role, Profession=self.Beruf)

        from src.Login import Login
        if self.Auth == Passtry:

            Login.entry(self=Login, permission="granted")

        else:
            Login.entry(self=Login, permission="denied")

class Personen(QSqlTableModel):
    def __init__(self):
        super(Personen, self).__init__()

        self.setTable('arvensteyn_dev22.humans')
        self.select()

    def welcome(self, **kwargs):
        pass







def welcome(human):
    new_human = QSqlQuery()
    l = list(human.keys())

    # Major ToDo: Datenbank und Controller aneinander anpassen '
    sql = """INSERT INTO arvensteyn_dev22.humans(
	nachname, vorname, anrede, titel, unternehmen, stellung, strasse, hausnummer, telefon, 
	telefon1, telefon2, mobil, fax, email, email2, rel_mdt, rel_auftr, kommentar, kompl_name)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    new_human.prepare(sql)

    for field, value in human.items():
        new_human.addBindValue(value)
    if new_human.exec() == True:
        print("tadaaa")
    else:
        print(new_human.boundValues())
        print(f"""last Error {new_human.lastError().text()}""")


class LastFiles(QSortFilterProxyModel):
    def __init__(self):
        super(LastFiles, self).__init__()
        self.setSourceModel(DBModelAuftraege())
        self.filter_last_files()

    def filter_last_files(self):
        self.list_of_files = currentConfig.getcurrentfiles(self=currentConfig())
        mesh = "') OR (\"az\" = '".join(self.list_of_files)
        Filter = f"""("az" = '{mesh}')"""
        self.setFilterKeyColumn(4)
        self.setFilterFixedString(Filter)



class PreviousEntriesFileProxy(QSortFilterProxyModel):
    def __init__(self, file):
        super(PreviousEntriesFileProxy, self).__init__()
        self.setSourceModel(Leistungen())

        filter = f"""{file}"""

        self.setFilterKeyColumn(13)

        self.setFilterFixedString(filter)


class Partner(QSqlTableModel):
    def __init__(self):
        super(Partner, self).__init__()

        self.setTable("arvensteyn_dev22.partner")
        self.select()


class Partner_curr(QSortFilterProxyModel):
    def __init__(self, mvp_id):
        super(Partner_curr, self).__init__()
        self.setSourceModel(Partner())

        filter = f"""{mvp_id}"""
        self.setFilterKeyColumn(0)
        self.setFilterFixedString(filter)
        print(self.index(0, 2).data())


class Leistungen(QSqlRelationalTableModel):
    def __init__(self, dataObj = None):
        super(Leistungen, self).__init__()

        self.setTable("arvensteyn_dev22.leistungen")
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.InnerJoin)
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setRelation(13, QSqlRelation("arvensteyn_dev22.auftraege", "id", "az"))
        #self.setRelation(2, QSqlRelation("arvensteyn_dev22.mandanten", "mandantid", "name"))
        self.setRelation(1, QSqlRelation("arvensteyn_dev22.mitglieder", "mitgliedernr", "mitglied"))
        self.select()

        
    def leistungserfassung(self, file:int, ra:int, lbeschreibung:str, duration:int, abrb:str, l_datum:str, stamp:str):

        self.neue_leistung = self.record()
        self.neue_leistung.setGenerated(0, False)
        self.neue_leistung.setValue(1, ra)
        self.neue_leistung.setValue(2, lbeschreibung)
        self.neue_leistung.setValue(4, duration)
        self.neue_leistung.setValue(13, abrb)
        self.neue_leistung.setValue(5, l_datum)
        self.neue_leistung.setValue(8, stamp)
        self.neue_leistung.setValue(13, file)
        self.neue_leistung.setValue(11, 'true')
        if not self.insertRecord(-1, self.neue_leistung):
            print(self.lastError().text())

    def ra_filter(self, file):
        filter = f"""auftrag = {file} AND ra = {self.ra}"""
        self.setFilter(filter)
        print(self.lastError().text())

class MostRecentFiles(QSqlQueryModel):
    def __init__(self):
        super(MostRecentFiles, self).__init__()
        self.ra = currentConfig.getcurrent_ra(self=currentConfig())

        query = QSqlQuery(f"""select
                          arvensteyn_dev22.auftraege.id, arvensteyn_dev22.auftraege.az,
                          arvensteyn_dev22.mandanten.name, arvensteyn_dev22.auftraege.auftragsbezeichnung   
                          from 
                          arvensteyn_dev22.auftraege
                          inner join arvensteyn_dev22.leistungen ON arvensteyn_dev22.leistungen.auftrag = 
                          arvensteyn_dev22.auftraege.id AND arvensteyn_dev22.leistungen.ra = {self.ra}
                          inner join arvensteyn_dev22.mandanten ON arvensteyn_dev22.auftraege.mdt = 
                          arvensteyn_dev22.mandanten.mandantid
                          group by arvensteyn_dev22.auftraege.id, arvensteyn_dev22.mandanten.name LIMIT 10""")

        self.setQuery(query)


class Auftragsauswahl(QSqlQueryModel):
    def __init__(self, MdtName):
        super(Auftragsauswahl, self).__init__()

        query = QSqlQuery(f"""SELECT
                          arvensteyn_dev22.auftraege.az, arvensteyn_dev22.auftraege.auftragsbezeichnung, 
                          arvensteyn_dev22.auftraege.auftragsjahr, arvensteyn_dev22.mandanten.name, 
                          arvensteyn_dev22.auftraege.id
                          FROM 
                          arvensteyn_dev22.auftraege
                          INNER JOIN arvensteyn_dev22.mandanten ON arvensteyn_dev22.mandanten.mandantid = 
                          arvensteyn_dev22.auftraege.mdt AND arvensteyn_dev22.mandanten.name = '{MdtName}'""")
        self.setQuery(query)

        print(self.lastError().text())

class Gerichte(QSqlTableModel):
    def __init__(self):
        super(Gerichte, self).__init__()
        self.setTable('arvensteyn_dev22.gerichte')
        self.select()
        print(self.rowCount())


class QuickAuftragsauswahl(QSqlQueryModel):
    def __init__(self, Az):
        super(QuickAuftragsauswahl, self).__init__()

        query = QSqlQuery(f"""SELECT                                                                              
                          arvensteyn_dev22.auftraege.az, arvensteyn_dev22.auftraege.auftragsbezeichnung,          
                          arvensteyn_dev22.auftraege.auftragsjahr, arvensteyn_dev22.mandanten.name,               
                          arvensteyn_dev22.auftraege.id                                                           
                          FROM                                                                                    
                          arvensteyn_dev22.auftraege                                                              
                          INNER JOIN arvensteyn_dev22.mandanten ON arvensteyn_dev22.mandanten.mandantid =         
                          arvensteyn_dev22.auftraege.mdt AND arvensteyn_dev22.auftraege.az = '{Az}'""")
        self.setQuery(query)

        print(self.lastError().text())



class ReifeMandanten(QSqlQueryModel):
    def __init__(self, start, end, mvp):
        super(ReifeMandanten, self).__init__()

        query = QSqlQuery(f"""SELECT                                                                            
                          DISTINCT arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid,       
                          arvensteyn_dev22.mandanten.mdt_id_lz                                                  
                          FROM                                                                                  
                          arvensteyn_dev22.mandanten                                                            
                          INNER JOIN arvensteyn_dev22.auftraege ON arvensteyn_dev22.auftraege.mdt =             
                          arvensteyn_dev22.mandanten.mandantid AND arvensteyn_dev22.mandanten.mvp = {mvp}       
                          INNER JOIN arvensteyn_dev22.leistungen ON arvensteyn_dev22.leistungen.auftrag =       
                          arvensteyn_dev22.auftraege.id AND arvensteyn_dev22.leistungen.l_datum                 
                          BETWEEN '{start}' AND '{end}' AND arvensteyn_dev22.leistungen.rechnungslauf_ok = 'false'                                                        
                         """)
        self.setQuery(query)

        print(self.lastError().text())




class ReifeAkten(QSqlTableModel):
    def __init__(self, start, end, mdt_id):
        super(ReifeAkten, self).__init__()
        self.query = QSqlQuery(f"""select 
        DISTINCT arvensteyn_dev22.auftraege.auftragsbezeichnung, arvensteyn_dev22.auftraege.id, arvensteyn_dev22.auftraege.az                              
        FROM                                                                                  
        arvensteyn_dev22.mandanten                                                            
        INNER JOIN arvensteyn_dev22.auftraege ON arvensteyn_dev22.auftraege.mdt = arvensteyn_dev22.mandanten.mandantid 
        AND arvensteyn_dev22.mandanten.mandantid = {mdt_id}       
        INNER JOIN arvensteyn_dev22.leistungen ON arvensteyn_dev22.leistungen.auftrag = arvensteyn_dev22.auftraege.id 
        AND arvensteyn_dev22.leistungen.l_datum BETWEEN '{start}' AND '{end}' 
        AND arvensteyn_dev22.leistungen.rechnungslauf_ok = 'false'""")

        self.setQuery(self.query)
        print(self.lastError().text())



class ReifeFruechtchen(QSortFilterProxyModel):
    def __init__(self, start, end, mvp, mdt):
        super(ReifeFruechtchen, self).__init__()
        self.setSourceModel(ReifeAkten(start= start, end=end, mvp=mvp))

        Filter = f"""{mdt}"""
        self.setFilterKeyColumn(1)
        self.setFilterFixedString(Filter)
