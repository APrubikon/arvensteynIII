from src.data import DBModelMdt
from src.MainLayout import *
from PyQt6.QtWidgets import (
                             QHBoxLayout,
                             QVBoxLayout,
                             QScrollArea,
                             QWidget,
                             QGridLayout,
                             QSpacerItem,
                             QSizePolicy,
                             QTextEdit,
                             QCompleter,
                             QDataWidgetMapper
                             )

from PyQt6 import QtCore
from PyQt6.QtCore import Qt

Anreden = ["Frau", "Herr", "Frau Dr.", "Herr Dr.", "Frau Prof. Dr.", "Herr Prof. Dr."]
Positionen = ["Geschäftsführerin", "Geschäftsführer", "Mitglied des Vorstands"]
Bundeslaender = ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg',
                 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen',
                 'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen']
Staaten = ["Deutschland", "EU (außer Deutschland)", "Außerhalb EU"]




mapper = QDataWidgetMapper()
mapper.setModel(DBModelMdt())


def setMapper(indexMdt):
    for i in range(DBModelMdt.rowCount()):
        if DBModelMdt.record(i).value(0) == indexMdt:
            mapper.setCurrentIndex(i)


class EditMdt(MainWindow):
    def __init__(self):
        super(EditMdt, self).__init__()


        self.setWindowTitle("Stammblatt Mandanten bearbeiten")


        # setup searchfield
        self.searchLayout = QVBoxLayout()
        self.searchLabel_mdt = ArveLabel('notice', "Bitte Mandanten auswählen...")
        self.searchLine_mdt = InputArve('hier eingeben')
        self.search_button = ArvenButton("ausgewählten Mandanten bearbeiten")

        self.searchLayout.addWidget(self.searchLabel_mdt)
        self.searchLayout.addWidget(self.searchLine_mdt)
        self.searchLayout.addWidget(self.search_button)
        self.searchLayout.addSpacerItem(self.spacerV)

        self.completer_search = QCompleter()
        self.completer_search.setModel(DBModelMdt)
        self.completer_search.setCompletionColumn(1)

        self.completer_search.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.searchLine_mdt.setCompleter(self.completer_search)

        # setup field for data-editing
        self.scrollSpace = QScrollArea()
        self.scrollWidget = QWidget()
        self.scrollGrid = QGridLayout(self.scrollWidget)
        self.scrollSpace.setWidgetResizable(True)

        self.block_a = GrundDaten()
        self.block_b = Sitz()
        self.block_c = GesVertretung()
        self.block_e = Berufsrecht()
        self.block_f = Abrechnung()
        self.block_g = Options()
        self.scrollGrid.addWidget(self.block_a, 0, 0)
        self.scrollGrid.addWidget(self.block_b, 1, 0)
        self.scrollGrid.addWidget(self.block_c, 2, 0)
        self.scrollGrid.addWidget(self.block_e, 0, 1)
        self.scrollGrid.addWidget(self.block_f, 1, 1)
        self.scrollGrid.addWidget(self.block_g, 2, 1)

        self.MdtNrInt = None

        self.MainHorizontalLayout = QHBoxLayout()

        self.MainVerticalLayout.addLayout(self.MainHorizontalLayout)

        ### SIGNALS
        self.completer_search.activated[QtCore.QModelIndex].connect(self.indexmap)
        self.search_button.clicked.connect(self.sendIndex)

        self.block_c.AddToAdressBook.clicked.connect(self.addGV)

        self.addSearchfield(searchable=True)
        # must be last line in constructor
        self.scrollSpace.setWidget(self.scrollWidget)



    # extract MdtIndex for search
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def indexmap(self, index):
        self.MdtNrInt = index.sibling(index.row(), 0).data()
    # send index to query for identifyijng contents
    def sendIndex(self):
        if self.MdtNrInt != None:
            self.addSearchfield(searchable=False)
            setMapper(self.MdtNrInt)
            self.block_a.InternStatusDB()
            self.block_a.AkquiseStatusDB()
        else:
            self.searchLine_mdt.clear()

    def addSearchfield(self, searchable):
        if searchable == True:
            self.MainHorizontalLayout.addLayout(self.searchLayout, 1)
            self.MainHorizontalLayout.addWidget(self.scrollSpace, 3)
            self.block_a.setDisabled(True)
            self.block_b.setDisabled(True)
            self.block_c.setDisabled(True)
            self.block_e.setDisabled(True)
            self.block_f.setDisabled(True)

        if searchable == False:
            self.MainHorizontalLayout.removeItem(self.searchLayout)
            self.block_a.setDisabled(False)
            self.block_b.setDisabled(False)
            self.block_c.setDisabled(False)
            self.block_e.setDisabled(False)
            self.block_f.setDisabled(False)

    def addGV(self):
        Bezug = {'prozess':"neu", 'Unternehmen': self.block_a.NameMdt.text()}
        # dict to call #args for prozess, unternehmen
        print(Bezug)
        from Arvensteyn import Switch
        Switch.conference_call(self=Switch, extension=5, **Bezug)


class GrundDaten(QWidget):
    def __init__(self):
        super(GrundDaten, self).__init__()


        self.VBox = QVBoxLayout(self)
        self.HBox2 = QHBoxLayout()
        self.HBox3 = QHBoxLayout()
        self.HBox4 = QHBoxLayout()
        self.Titel = ArveLabel('header', 'Grunddaten')

        self.NameMdt = InputArve("Name bzw. Firma des Mandanten")
        self.NameMdt.setToolTip("Änderung nur durch Administrator")
        self.NameMdt.setBaseSize(350, 35)
        self.MdtNrLabel = ArveLabel("notice", "Mandantennummer:")
        self.spacerV = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Minimum,
                                   vPolicy=QSizePolicy.Policy.Expanding)

        self.MdtNrLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.MdtNr = InputArve("Mandantennummer")
        self.MdtNr.setReadOnly(True)
        self.MdtNr.setStyleSheet(
            "border: 1px #8f8f91; border-radius:4px; background-color:rgb(241,241,241); color:darkred")


        self.MVP = InputArve("Mandantenverantwortlicher Partner")
        self.MVP.setToolTip("Änderung nur durch Administrator")
        self.MVP.setReadOnly(True)
        self.MVPLabel = ArveLabel("notice", "Mandantenverantwortlich:")
        self.MVPLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.AkquiseData = ''
        self.InternData = ''
        self.Intern = ArveCheck("Interner Mandant", False)
        self.Akquise = ArveCheck("Akquise - noch kein Mandatsvertrag", False)

        self.VBox.addWidget(self.Titel)

        self.VBox.addWidget(self.NameMdt)
        self.HBox2.addWidget(self.MdtNrLabel)
        self.HBox2.addWidget(self.MdtNr)
        self.HBox3.addWidget(self.MVPLabel)
        self.HBox3.addWidget(self.MVP)
        self.HBox4.addWidget(self.Intern)
        self.HBox4.addWidget(self.Akquise)
        self.VBox.addLayout(self.HBox2)
        self.VBox.addLayout(self.HBox3)
        self.VBox.addLayout(self.HBox4)
        self.VBox.addSpacerItem(self.spacerV)

        self.Intern.stateChanged.connect(self.InternStatus)
        self.Akquise.stateChanged.connect(self.AkquiseStatus)

        self.InternStatus()
        self.AkquiseStatus()

        self.InternStatusDB()
        self.AkquiseStatusDB()

        self.MdtNr.textChanged.connect(self.InternStatusDB)
        self.MdtNr.textChanged.connect(self.AkquiseStatusDB)

        mapper.addMapping(self.NameMdt, 1)
        mapper.addMapping(self.MdtNr, 34)
        mapper.addMapping(self.MVP, 33)

    def InternStatus(self):
        if not self.Intern.isChecked():
            self.InternData = "Regulär"
  
        else:
            self.InternData = "Intern"

        #DBModelIndex = DBModelMdt.index(mapper.currentIndex(), 6)
        #DBModelMdt.setData(DBModelIndex, self.InternData)


    def InternStatusDB(self):  # get content from db in checkbox
        if DBModelMdt.index(mapper.currentIndex(), 6).data() == "Intern":
            self.Intern.setChecked(True)
        elif DBModelMdt.index(mapper.currentIndex(), 6).data() == None:
            intern = "Regulär"
            DBModelIndex = DBModelMdt.index(mapper.currentIndex(), 6)
            DBModelMdt.setData(DBModelIndex, intern)

# ToDo: use setData to write status to model
    def AkquiseStatus(self):
        if not self.Akquise.isChecked():
            self.AkquiseData = "Mandatiert"
        else:
            self.AkquiseData = "Akquise"

# ToDo: Anpassen der Spalten in DB

        DBModelIndex = DBModelMdt.index(mapper.currentIndex(), 7)
        DBModelMdt.setData(DBModelIndex, self.AkquiseData)


# get content from db in checkbox
# ToDo: Anpassen der Spalten in DB
    def AkquiseStatusDB(self):
        if DBModelMdt.index(mapper.currentIndex(), 7).data() == "Akquise":
            self.Akquise.setChecked(True)
        else:
            pass



class Sitz(QWidget):
    def __init__(self):
        super(Sitz, self).__init__()
        self.SitzLabel = ArveLabel("header", "Sitz des Mandanten")
        self.Sitz1 = InputArve("Straße")
        self.Sitz2 = InputArve("Hausnummer")
        self.Sitz2.adjustSize()
        self.Sitz3 = InputArve("PLZ")
        self.Sitz4 = InputArve("Ort")
        self.Sitz5 = ComboArve("Bundesland")
        self.Sitz5.addItems(Bundeslaender)
        self.Sitz6 = ComboArve("Staat")
        self.Sitz6.addItems(Staaten)
        self.spacerV = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Minimum,
                                   vPolicy=QSizePolicy.Policy.Expanding)
        self.HBox = QHBoxLayout()

        self.HBox.addWidget(self.Sitz1, 2)
        self.HBox.addWidget(self.Sitz2, 1)

        self.VBox = QVBoxLayout(self)
        self.VBox.addWidget(self.SitzLabel)
        self.VBox.addLayout(self.HBox)
        self.VBox.addWidget(self.Sitz3)
        self.VBox.addWidget(self.Sitz4)
        self.VBox.addWidget(self.Sitz5)
        self.VBox.addWidget(self.Sitz6)
        self.VBox.addSpacerItem(self.spacerV)

# mapping der widgets
# ToDo: Anpassen der Spalten in Db
        #mapper.addMapping(self.Sitz1, )
        #mapper.addMapping(self.Sitz2, )
        #mapper.addMapping(self.Sitz3, )
        #mapper.addMapping(self.Sitz4, )
        mapper.addMapping(self.Sitz5, 8)                # problem: Combobox
        #mapper.addMapping(self.Sitz6, )                # problem: Combobox


class GesVertretung(QWidget):
    def __init__(self):
        super(GesVertretung, self).__init__()

        self.GVlabel = ArveLabel("header", "Gesetzliche Vertretung des Mandanten")
        self.GVdisplay = InputArve("Gesetzlicher Vertreter")
        self.GVPosition = ComboArve("Position des gesetzlichen Vertreters")
        self.GVPosition.addItems(Positionen)
        self.GVcheck = ArveCheck("Mandant ist natürliche Person", False)
        self.AddToAdressBook = ArvenButton("Zum Adressbuch hinzufügen")
        self.setFromAdressBook = ArvenButton("Aus dem Adressbuch auswählen")
        self.spacerV = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Minimum,
                                   vPolicy=QSizePolicy.Policy.Expanding)

        self.GVVBox = QVBoxLayout(self)

        self.GVVBox.addWidget(self.GVlabel)
        self.GVVBox.addWidget(self.GVcheck)
        self.GVVBox.addWidget(self.GVdisplay)
        self.GVVBox.addWidget(self.GVPosition)
        self.GVVBox.addWidget(self.setFromAdressBook)
        self.GVVBox.addWidget(self.AddToAdressBook)

        self.REcheck = ArveCheck("Abweichender Rechnungsempfänger", True)
        self.REcheck.stateChanged.connect(self.hideRE)
        self.RE_display = InputArve("Rechnungsempfänger")
        self.REE_AddToAdressBook = ArvenButton("Zum Adressbuch hinzufügen")
        self.REE_setFromAdressBook = ArvenButton("Aus dem Adressbuch auswählen")
        self.spacerV = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Minimum,
                                   vPolicy=QSizePolicy.Policy.Expanding)




        self.REVBox = QVBoxLayout()

        self.REVBox.addWidget(self.REcheck)
        self.REVBox.addWidget(self.RE_display)
        self.REVBox.addWidget(self.REE_setFromAdressBook)
        self.REVBox.addWidget(self.REE_AddToAdressBook)
        self.REVBox.addSpacerItem(self.spacerV)

        self.GVVBox.addLayout(self.REVBox)

    def hideRE(self):
        if not self.REcheck.isChecked():
            self.REE_AddToAdressBook.setDisabled(True)
            self.REE_setFromAdressBook.setDisabled(True)
            self.abwRE = 0
        else:
            self.REE_AddToAdressBook.setDisabled(False)
            self.REE_setFromAdressBook.setDisabled(False)
            self.abwRE = 1

class Berufsrecht(QWidget):
    def __init__(self):
        super(Berufsrecht, self).__init__()
        self.BerufsrechtLabel = ArveLabel("header", "Berufsrechtliche Sorgfalt")
        self.KollisionMdt = ComboArve("Mandantenbezogene Kollision")
        self.GeldwaescheG = ComboArve("Geldwäschegesetz")
        self.Drittwirkung = ComboArve("Schutzwirkung zugunsten Dritter (Konzernunternehmen)")

        self.VBox = QVBoxLayout(self)

        self.VBox.addWidget(self.BerufsrechtLabel)
        self.VBox.addWidget(self.KollisionMdt)
        self.VBox.addWidget(self.GeldwaescheG)
        self.VBox.addWidget(self.Drittwirkung)
        self.spacerV = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Minimum,
                                   vPolicy=QSizePolicy.Policy.Expanding)
        self.VBox.addSpacerItem(self.spacerV)


class Abrechnung(QWidget):
    def __init__(self):
        super(Abrechnung, self).__init__()

        self.AbrechnungLabel1 = ArveLabel('header', 'Vergütung')
        self.Rahmenvertrag = ArveCheck('Rahmenvertrag', True)
        self.Stundensatz1 = InputArve("Stundensatz")
        self.Stundensatz2 = InputArve("Stundensatz 2")
        self.Stundensatz2.setDisabled(True)
        self.MVPAnteil = InputArve('Anteil des MVP in %')
        self.SonstigesVerguetung = QTextEdit()
        self.SonstigesVerguetung.setFixedHeight(100)
        self.SonstigesVerguetung.setStyleSheet("background-color:rgb(241, 241, 241); border-radius:4px;")
        self.SonstigesVerguetung.setPlaceholderText("Anmerkungen zur Abrechnung")

        self.VBox = QVBoxLayout(self)
        self.VBox.addWidget(self.AbrechnungLabel1)
        self.VBox.addWidget(self.Rahmenvertrag)
        self.VBox.addWidget(self.Stundensatz1)
        self.VBox.addWidget(self.Stundensatz2)
        self.VBox.addWidget(self.MVPAnteil)
        self.VBox.addWidget(self.SonstigesVerguetung)

class Options(QWidget):
    def __init__(self):
        super(Options, self).__init__()

        self.title = ArveLabel("header", "Optionen")
        self.MVneu = ArvenButton("Mandatsvertrag erstellen")
        self.VVneu = ArvenButton("Vergütungsvereinbarung erstellen")
        self.MV_VV_versand = ArveCheck("Mandatsvertrag und Vergütungsvereinbarung versendet", False)
        self.MV_VV_ablage = ArveCheck("Mandatsvertrag und Vergütungsvereinbarung unterschrieben abgelegt", False)
        self.spacerV = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Minimum,
                                   vPolicy=QSizePolicy.Policy.Expanding)
        self.VBox = QVBoxLayout(self)
        self.VBox.addWidget(self.title)
        self.VBox.addWidget(self.MVneu)
        self.VBox.addWidget(self.VVneu)
        self.VBox.addWidget(self.MV_VV_versand)
        self.VBox.addWidget(self.MV_VV_ablage)
        self.VBox.addSpacerItem(self.spacerV)



