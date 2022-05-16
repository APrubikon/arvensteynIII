from src.MainLayout import *
from PyQt6.QtWidgets import (QVBoxLayout,
                             QHBoxLayout,
                             QTableView,
                             QAbstractItemView,
                             QScrollArea,
                             QCalendarWidget,
                             QTextEdit,
                             QSpinBox)
from PyQt6 import QtCore
from PyQt6.QtSql import (
                            QSqlRelationalTableModel,
                            QSqlRelation)
from PyQt6.QtCore import pyqtSlot, QPoint
from datetime import date, datetime, timedelta

from src.data import LastFiles, PreviousEntriesFileProxy, Leistungen, DBModelAuftraege
from src.InputHumans import Human
from src.auftraege import SearchfieldAuftraege
from src.config import last_files_update, currentConfig

from src.auxiliary_gui import EmptyDelegate
from src.variables import *
from src.Leistunngserfassung import New_Entry


delegate = EmptyDelegate()



class Timeframe(MainWindow):
    def __init__(self):
        super(Timeframe, self).__init__()
        self.setWindowTitle("Zeiterfassung - Startseite")

        self.block_a = SearchfieldAuftraege()
        self.block_b = CurrentFiles()
        #self.block_c = CurrentAffairs()

        self.block_a.ergebnisListe.doubleClicked.connect(self.openTimeSheet)
        self.block_b.last_files.doubleClicked.connect(self.openTimeSheet)

        self.MainHBlock = QHBoxLayout()
        self.VBlock = QVBoxLayout()
        self.VBlock1 = QVBoxLayout()
        self.VBlock.addWidget(self.block_a)
        self.VBlock.addWidget(self.block_b)
        
        self.VBlock1.addSpacerItem(self.spacerV)  
        #self.VBlock1.addWidget(self.block_c)
      

        self.MainHBlock.addLayout(self.VBlock, 1)
        self.MainHBlock.addLayout(self.VBlock1, 2)

        self.MainVerticalLayout.addLayout(self.MainHBlock)

    def openTimeSheet(self, index):
        print(index)

        if not index.sibling(index.row(), 0).data() is None:
            self.AuftrIndex = index.sibling(index.row(), 0).data()
        else:
            self.AuftrIndex = ''

        if not index.sibling(index.row(), 4).data() is None:
            self.az = index.sibling(index.row(), 4).data()
        else:
            self.az = ''
        if not index.sibling(index.row(), 1).data() is None:
            self.mdt = index.sibling(index.row(), 1).data()
        else:
            self.mdt = ''
        if not index.sibling(index.row(), 5).data() is None:
            self.auftrag = index.sibling(index.row(), 5).data()
        else:
            self.auftrag = ''

        self.packet = {'file': self.AuftrIndex, 'az': self.az, 'mdt': self.mdt, 'auftrag': self.auftrag}

        last_files_update(self.az)


        New_Entry(**self.packet).show()

class CurrentFiles(ArvenWidget):
    def __init__(self):
        super(CurrentFiles, self).__init__(framed="not")

        self.last_files = ArvenTable()
        self.last_files.setItemDelegateForColumn(5, delegate)
        self.last_files.setItemDelegateForColumn(4, delegate)
        self.last_files.setStyleSheet("border-style: solid; border-radius: 4px; border-color: lightgray")
        model = DBModelAuftraege()
        model.filter_last_files()
        self.last_files.setModel(model)
        for i in range(0, 20):
            self.last_files.setColumnHidden(i, True)
        self.last_files.setColumnHidden(5, False)
        self.last_files.setColumnHidden(4, False)
        self.last_files.setColumnHidden(1, False)
        self.last_files.verticalHeader().hide()
        self.last_files.horizontalHeader().setStretchLastSection(True)
        self.last_files.horizontalHeader().hide()
        self.last_files.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.last_files.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.last_files.setWordWrap(True)
        self.last_files.resizeRowsToContents()

        self.last_files.setItemDelegateForColumn(1, delegate)
        self.last_files.setItemDelegateForColumn(4, delegate)
        self.last_files.setItemDelegateForColumn(5, delegate)

        self.title = ArveLabel("header", "Meine zuletzt verwendeten Akten")

        self.VBox = QVBoxLayout()
        self.VBox.addWidget(self.title)
        self.VBox.addWidget(self.last_files)

        self.setLayout(self.VBox)


class CurrentAffairs(ArvenWidget):
    def __init__(self):
        super(CurrentAffairs, self).__init__("not")

        pass




































































































































































































