from PyQt6.QtSql import QSqlQueryModel, QSqlQuery
from PyQt6.QtCore import Qt
from src.config import currentConfig

from PyQt6.QtCore import QTimer











class EditableQueryModel(QSqlQueryModel):
    def __init__(self, file):
        super(EditableQueryModel, self).__init__()
        self.editables = {3 : 'l_datum', 4 : 'minutes',
                          5 : 'lbeschreibung'}
        ra = currentConfig.getcurrent_ra(self=currentConfig())
        self.query = QSqlQuery(f"""SELECT                                                                                                                    
                          arvensteyn_dev22.mandanten.mandantid,
                          arvensteyn_dev22.mandanten.name,
                          arvensteyn_dev22.mandanten.mvp,
                          arvensteyn_dev22.mandanten.internal,
                          arvensteyn_dev22.mandanten.akquise,
                          arvensteyn_dev22.mandanten.ges_vertreter,
                          arvensteyn_dev22.mandanten.rechnungsempfaenger,
                          arvensteyn_dev22.mandanten.sitz_strasse,
                          arvensteyn_dev22.mandanten.sitz_hausnr,
                          arvensteyn_dev22.mandanten.sitz_PLZ,
                          arvensteyn_dev22.mandanten.sitz_ort,
                          arvensteyn_dev22.mandanten.sitz_bundesland,
                          arvensteyn_dev22.mandanten.sitz_staat,
                          arvensteyn_dev22.mandanten.rvg,
                          arvensteyn_dev22.mandanten.stundensatz1,
                          arvensteyn_dev22.mandanten.stundensatz2,
                          arvensteyn_dev22.mandanten.bemerkungen,
                          arvensteyn_dev22.mandanten.mv_vv_vers,
                          arvensteyn_dev22.mandanten.mv_vv_ablage,
                          arvensteyn_dev22.mandanten.gwg,
                          arvensteyn_dev22.mandanten.mdtbez_kollision,
                          arvensteyn_dev22.mandanten.mvp_anteil,
                          arvensteyn_dev22.mandanten.mdt_id_lz,
                          arvensteyn_dev22.mandanten.gv_position,
                          arvensteyn_dev22.mandanten.elektr_rechnung,
                          arvensteyn_dev22.humans.
                          arvensteyn_dev22.humans.
                          arvensteyn_dev22.partner.
                          arvensteyn_dev22.partner.
                          arvensteyn_dev22.gegner.
                          arvensteyn_dev22.gegner
                          
                          
                    
,
                                                              
                                                           );
                          
                          
                          arvensteyn_dev22.auftraege.auftragsbezeichnung, 
                          arvensteyn_dev22.auftraege.az, arvensteyn_dev22.leistungen.l_datum, 
                          arvensteyn_dev22.leistungen.minutes, arvensteyn_dev22.leistungen.lbeschreibung, 
                          arvensteyn_dev22.leistungen.id                     
                          FROM arvensteyn_dev22.leistungen                                                                                                 
                          INNER JOIN arvensteyn_dev22.auftraege ON arvensteyn_dev22.auftraege.id =
                          arvensteyn_dev22.leistungen.auftrag                                                                
                          INNER JOIN arvensteyn_dev22.mandanten ON arvensteyn_dev22.mandanten.mandantid  = 
                          arvensteyn_dev22.auftraege.mdt AND arvensteyn_dev22.leistungen.auftrag = {file}
                          AND arvensteyn_dev22.leistungen.ra = {ra}                                                           
                          """)
        self.setQuery(self.query)
        print(self.lastError().text())


    def flags(self, index):
        fl = QSqlQueryModel.flags(self, index)
        if index.column() in self.editables:              ## todo, columns
            fl |= Qt.ItemFlag.ItemIsEditable
        return fl

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            mycolumn = index.column()
            myfilter = index.sibling(index.row(), 6).data(Qt.ItemDataRole.DisplayRole)
            src_index = self.createIndex(index.row(), index.column())
            if mycolumn == 3:
                value = value.toPyDate()
            if mycolumn in self.editables:
                filter_col = self.editables[mycolumn]
                filter_value = self.index(index.row(), mycolumn).data()
                query = f"""Update arvensteyn_dev22.leistungen SET {filter_col} = '{value}' WHERE 
                id = {myfilter}"""
                q = QSqlQuery(query)
                q.exec()
                if q.exec() is False:
                    self.dataChanged.emit(index, index, [])
                    print("submachinelearning")# <---
                    return True
                return False





                if result:
                    self.query.exec()
                else:
                    print(self.query.lastError().text())
                self.dataChanged.emit(src_index, src_index)
                return result
        return super(QSqlQueryModel, self).setData(index, value, role)


class EditableMdtModel(QSqlQueryModel):
    def __init__(self, mandantid=None):
        super(EditableMdtModel, self).__init__()
        self.mandantid = mandantid
        self.query = QSqlQuery(f"""SELECT                                                                                                                    
                          arvensteyn_dev22.mandanten.mandantid,
                          arvensteyn_dev22.mandanten.name,
                          arvensteyn_dev22.mandanten.mvp,
                          arvensteyn_dev22.mandanten.internal,
                          arvensteyn_dev22.mandanten.akquise,
                          arvensteyn_dev22.mandanten.ges_vertreter,
                          arvensteyn_dev22.mandanten.rechnungsempfaenger,
                          arvensteyn_dev22.mandanten.sitz_strasse,
                          arvensteyn_dev22.mandanten.sitz_hausnr,
                          arvensteyn_dev22.mandanten."sitz_PLZ",
                          arvensteyn_dev22.mandanten.sitz_ort,
                          arvensteyn_dev22.mandanten.sitz_bundesland,
                          arvensteyn_dev22.mandanten.sitz_staat,
                          arvensteyn_dev22.mandanten.rvg,
                          arvensteyn_dev22.mandanten.stundensatz1,
                          arvensteyn_dev22.mandanten.stundensatz2,
                          arvensteyn_dev22.mandanten.bemerkungen,
                          arvensteyn_dev22.mandanten.mv_vv_vers,
                          arvensteyn_dev22.mandanten.mv_vv_ablage,
                          arvensteyn_dev22.mandanten.gwg,
                          arvensteyn_dev22.mandanten.mdtbez_kollision,
                          arvensteyn_dev22.mandanten.mvp_anteil,
                          arvensteyn_dev22.mandanten.mdt_id_lz,
                          arvensteyn_dev22.mandanten.gv_position,
                          arvensteyn_dev22.mandanten.elektr_rechnung,
                          arvensteyn_dev22.partner.partnerid,
                          arvensteyn_dev22.partner.name
                                                  
                          FROM
                          arvensteyn_dev22.mandanten
                          INNER JOIN 
                          arvensteyn_dev22.partner ON arvensteyn_dev22.partner.partnerid = arvensteyn_dev22.mandanten.mvp

                          WHERE
                          arvensteyn_dev22.mandanten.mandantid = {self.mandantid};                                                                                                                                                                      
                          """)
        if not self.setQuery(self.query):
            #todo setup notice dialog.
            print(self.lastError().text())

    def flags(self, index):
        fl = QSqlQueryModel.flags(self, index)
        fl |= Qt.ItemFlag.ItemIsEditable
        return fl

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            mycolumn = index.column()
           # myfilter = index.sibling(index.row(), 6).data(Qt.ItemDataRole.DisplayRole)
            src_index = self.createIndex(index.row(), index.column())
           # todo convert birthday
            if mycolumn == 3:
                value = value.toPyDate()
            if mycolumn in self.columnCount():
                filter_col = self.record().fieldName(mycolumn)
                filter_value = self.index(index.row(), mycolumn).data()
                query = f"""Update arvensteyn_dev22.mandanten SET {filter_col} = '{value}' WHERE 
                mandantid = {self.mandantid}"""
                q = QSqlQuery(query)
                q.exec()
                if q.exec() is False:
                    self.dataChanged.emit(index, index, [])
                    print("submachinelearning")  # <---
                    return True
                return False

                if result:
                    self.query.exec()
                else:
                    print(self.query.lastError().text())
                self.dataChanged.emit(src_index, src_index)
                return result
        return super(QSqlQueryModel, self).setData(index, value, role)
