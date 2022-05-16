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

from PyQt6.QtCore import Qt, QSortFilterProxyModel, QRegularExpression
from src.config import currentConfig
from src.db import DB

db = DB()

class DBModelMdt(QSqlRelationalTableModel):
    def __init__(self):
        super(DBModelMdt, self).__init__()
        self.setTable("arvensteyn_dev22.mandanten")
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setSort(0, Qt.SortOrder.AscendingOrder)
        self.setRelation(3, QSqlRelation("arvensteyn_dev22.partner", "partnerid", "name"))
        self.select()
        db.close()

class DBModelHumans(QSqlTableModel):
    def __init__(self):
        super(DBModelHumans, self).__init__()
        self.setTable("arvensteyn_dev22.humans")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.setSort(0, Qt.SortOrder.AscendingOrder)
        #self.select()
        db.close()

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

        self.select()
        if not self.select() == True:
            print(f"""{self.lastError().text()}""")


        db.close()

    def filter_last_files(self):
        self.list_of_files = currentConfig.getcurrentfiles(self=currentConfig())
        mesh = "') OR (\"az\" = '".join(self.list_of_files)
        Filter = f"""("az" = '{mesh}')"""
        self.setFilter(Filter)

class DBModel1(QSqlTableModel):
    def __init__(self):
        super(DBModel1, self).__init__()
        self.setTable('arvensteyn_dev22.mitglieder')
        #self.select()
        db.close()
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

        self.setSourceModel(DBModelAuftraege())
        filter = QRegularExpression(f"""^{file}$""")
        self.setFilterKeyColumn(0)
        self.setFilterRegularExpression(filter)

class FFindfromAZ(QSortFilterProxyModel):
    def __init__(self, file):
        super(FFindfromAZ, self).__init__()

        self.setSourceModel(DBModelAuftraege())
        filter = f"""{file}"""
        self.setFilterKeyColumn(4)
        self.setFilterFixedString(filter)

        if self.rowCount() == 1:
            auftrag = self.index(0, 5).data()
            AuftrIndex = self.index(0, 0).data()
            mdt = self.index(0, 1).data()
            packet = {'file': AuftrIndex, 'az': file, 'mdt': mdt, 'auftrag': auftrag}
            from src.Leistunngserfassung import New_Entry
            New_Entry(**packet).show()

        else:
            from Arvensteyn import Switch
            Switch.pageNr(self=Switch(), extension=4)


class Partner(QSqlTableModel):
    def __init__(self):
        super(Partner, self).__init__()

        self.setTable("arvensteyn_dev22.partner")
        self.select()
        db.close()

class Partner_curr(QSortFilterProxyModel):
    def __init__(self, mvp_id):
        super(Partner_curr, self).__init__()
        self.setSourceModel(Partner())

        filter = f"""{mvp_id}"""
        self.setFilterKeyColumn(0)
        self.setFilterFixedString(filter)
        print(self.index(0, 2).data())


class Leistungen(QSqlRelationalTableModel):
    def __init__(self):
        super(Leistungen, self).__init__()
        self.setTable("arvensteyn_dev22.leistungen")
        self.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setRelation(13, QSqlRelation("arvensteyn_dev22.auftraege", "id", "az"))
        self.setRelation(3, QSqlRelation("arvensteyn_dev22.mandanten", "mandantid", "name"))
        self.select()
        db.close()


        self.ra = currentConfig.getcurrent_ra(self=currentConfig())

    def leistungserfassung(self, file:int, ra:int, lbeschreibung:str, duration:int, abrb:str, l_datum:str, stamp:str):

        self.neue_leistung = self.record()
        self.neue_leistung.setGenerated(0, False)
        self.neue_leistung.setValue(1, ra)
        self.neue_leistung.setValue(2, lbeschreibung)
        self.neue_leistung.setValue(4, duration)
        self.neue_leistung.setValue(5, abrb)
        self.neue_leistung.setValue(6, l_datum)
        self.neue_leistung.setValue(9, stamp)
        self.neue_leistung.setValue(13, file)
        self.neue_leistung.setValue(11, 'false')
        if not self.insertRecord(-1, self.neue_leistung):
            print(self.lastError().text())




class Auftragsauswahl(QSortFilterProxyModel):
    def __init__(self, MdtName):
        super(Auftragsauswahl, self).__init__()
        self.setSourceModel(DBModelAuftraege())
        filter = QRegularExpression(f"""^{MdtName}$""")
        self.setFilterKeyColumn(1)
        self.setFilterRegularExpression(filter)


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

###
#(f"""SELECT
#     arvensteyn_dev22.mandanten.name, arvensteyn_dev22.mandanten.mandantid,
#     arvensteyn_dev22.mandanten.mdt_id_lz, arvensteyn_dev22.leistungen.lbeschreibung,
#     arvensteyn_dev22.leistungen.minutes, arvensteyn_dev22.auftraege.auftragsbezeichnung,
#     arvensteyn_dev22.auftraege.az, arvensteyn_dev22.leistungen.l_datum
#     FROM
#     arvensteyn_dev22.mandanten
#     INNER JOIN arvensteyn_dev22.auftraege ON arvensteyn_dev22.auftraege.mdt =
#     arvensteyn_dev22.mandanten.mandantid AND arvensteyn_dev22.mandanten.mvp = {mvp}
#     INNER JOIN arvensteyn_dev22.leistungen ON arvensteyn_dev22.leistungen.auftrag =
#     arvensteyn_dev22.auftraege.id AND arvensteyn_dev22.leistungen.l_datum
#     BETWEEN '{start}' AND '{end}'
#     ORDER BY
#     arvensteyn_dev22.mandanten.mandantid""")  ###