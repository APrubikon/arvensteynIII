from src.MainLayout import *
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QCompleter,
    QDataWidgetMapper,
    QAbstractItemView
)

from PyQt6 import QtCore
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from datetime import date

today_date = date.today()
Jahr = today_date.strftime("%y")

from src.auxiliary_gui import EmptyDelegate
from src.data import DBModelMdt, DBModelAuftraege, Auftragsauswahl, PreviousEntriesFileProxy



mapper = QDataWidgetMapper()
mapper.setModel(DBModelAuftraege())


def setMapper(current):
    mapper.setCurrentIndex(current.row())
    print(mapper.currentIndex())
    print(current)


class MainFrameAuftraege(MainWindow):
    def __init__(self):
        super(MainFrameAuftraege, self).__init__()

        self.setWindowTitle("Aufträge bearbeiten")

        self.mainHBox = QHBoxLayout()
        self.block_a = SearchfieldAuftraege()
        self.block_b = DatenAuftraege()

        self.mainHBox.addWidget(self.block_a, 1)
        self.mainHBox.addWidget(self.block_b, 2)

        self.MainVerticalLayout.addLayout(self.mainHBox)




class SearchfieldAuftraege(ArvenWidget):
    def __init__(self):
        super(SearchfieldAuftraege, self).__init__(framed="framed")

        self.searchMode1 = ArvenRadio("Mandant nach Namen auswählen", "checked")
        self.searchMode1.toggled.connect(self.searchModeSelect)

        self.searchMode2 = ArvenRadio("Mandant nach Nummer auswählen", "not")
        self.searchMode2.toggled.connect(self.searchModeSelect)

        self.searchModes = QHBoxLayout()
        self.searchModes.addWidget(self.searchMode1)
        self.searchModes.addWidget(self.searchMode2)

        self.search_line = InputArve("Bitte Mandanten auswählen")
        self.completer = QCompleter()
        self.completer.setModel(DBModelMdt())
        self.completer.setCompletionColumn(1)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)

        self.completer.activated[QtCore.QModelIndex].connect(self.indexmap)

        self.ergebnisListe = ArvenTable()
        self.ergebnisListe.clicked.connect(setMapper)
        self.ergebnisListe.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ergebnisListe.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)


        self.vBox = QVBoxLayout(self)
        self.vBox.addLayout(self.searchModes)
        self.vBox.addWidget(self.search_line)
        self.vBox.addWidget(self.ergebnisListe)
        self.searchModeSelect()

    def searchModeSelect(self):
        if self.searchMode2.isChecked():
            self.search_line.clear()
            self.search_line.setPlaceholderText("Mandant nach Nummer auswählen")
            limit = QRegularExpression("[0-9]*")
            limiter = QRegularExpressionValidator(limit)
            self.search_line.setValidator(limiter)
            self.search_line.setCompleter(self.completer)
            self.completer.setCompletionColumn(0)

        else:
            self.search_line.clear()
            self.search_line.setCompleter(self.completer)
            self.completer.setCompletionColumn(1)
            self.search_line.setPlaceholderText("Bitte Mandanten auswählen")
            self.search_line.setValidator(None)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def indexmap(self, index):
        self.MdtNrInt:int = index.sibling(index.row(), 0).data()
        self.MdtName:str = index.sibling(index.row(), 1).data()
        self.Auftragsliste(self.MdtName)


    def Auftragsliste(self, MdtName:str):
        self.ergebnisListe.setModel(Auftragsauswahl(MdtName))
        for i in range(0, 20):
            self.ergebnisListe.setColumnHidden(i, True)
            self.ergebnisListe.setItemDelegate(EmptyDelegate())
        self.ergebnisListe.setColumnHidden(5, False)
        self.ergebnisListe.setColumnHidden(4, False)
        self.ergebnisListe.verticalHeader().hide()
        self.ergebnisListe.horizontalHeader().setStretchLastSection(True)
        self.ergebnisListe.horizontalHeader().hide()
        self.ergebnisListe.setWordWrap(True)


class DatenAuftraege(ArvenWidget):
    def __init__(self):
        super(DatenAuftraege, self).__init__(framed="not")

        self.VBox = QVBoxLayout(self)
        self.HBox = QHBoxLayout()
        self.HBox1 = QHBoxLayout()
        self.HBox2 = QHBoxLayout()
        self.HBox3 = QHBoxLayout()
        self.HBox4 = QHBoxLayout()
        self.HBox5 = QHBoxLayout()

        self.Auftragsjahr = Jahr

        self.Auftragsname = InputArve("Auftragsbezeichnung")
        self.Auftragsnummer = InputArve("Auftragsnummer")
        self.Auftragsnummer.setReadOnly(True)
        self.Gegner = InputArve("Gegner")
        self.AddGegner = ArvenButton("Gegner zur Datenbank hinzufügen")
        self.Gegner2 = InputArve("weiterer Gegner")
        self.AddGegner2 = ArvenButton("weiteren Gegner zur Datenbank hinzufügen")
        self.Gegner3 = InputArve("sonstiger Beteiligter")
        self.AddGegner3 = ArvenButton("sonstigen Beteiligten zur Datenbank hinzufügen")

        self.kollisionAuftr = ComboArve("Auftragsbezogene Kollisionsprüfung")
        self.Gerichte = ComboArve("Gericht")
        self.gerichtAz = InputArve("Gerichtliches Az.")
        self.streitwert = InputArve("Streitwert")
        limit = QRegularExpression("[0-9]*")
        limiter = QRegularExpressionValidator(limit)
        self.streitwert.setValidator(limiter)

        self.addRae = ArvenButton("Gegnerische Rechtsanwälte hinzufügen")

        mapper.addMapping(self.Auftragsname, 5)
        mapper.addMapping(self.Auftragsnummer, 4)
        self.HBox.addWidget(self.Auftragsname, 2)
        self.HBox.addWidget(self.Auftragsnummer, 1)
        self.HBox1.addWidget(self.Gegner, 2)
        self.HBox1.addWidget(self.AddGegner, 1)
        self.HBox2.addWidget(self.Gegner2, 2)
        self.HBox2.addWidget(self.AddGegner2, 1)
        self.HBox3.addWidget(self.Gegner3, 2)
        self.HBox3.addWidget(self.AddGegner3, 1)

        self.VBox.addLayout(self.HBox)
        self.VBox.addLayout(self.HBox1)
        self.VBox.addLayout(self.HBox2)
        self.VBox.addLayout(self.HBox3)
        self.VBox.addWidget(self.kollisionAuftr)
        self.VBox.addWidget(self.Gerichte)
        self.VBox.addWidget(self.streitwert)

        self.VBox.addSpacerItem(self.spacerV)
