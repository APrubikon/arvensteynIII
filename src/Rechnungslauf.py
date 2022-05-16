from src.MainLayout import *
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QScrollArea
)

from PyQt6.QtCore import Qt, pyqtSignal
from src.variables import *
from src.auxiliary_gui import EmptyDelegate
from src.data import DBModel1, Partner, Partner_curr, ReifeMandanten, ReifeAkten, ReifeFruechtchen
from src.config import currentConfig
from src.korrektur import Korrekturfile

bearbeiter = currentConfig.getcurrent_ra(currentConfig())


class Rechnungslauf(MainWindow):
    def __init__(self):
        super(Rechnungslauf, self).__init__()
        self._rcwin = None
        self.setWindowTitle("Rechnungslauf")

        # create selection widgets

        self.mvp_auswahl = ComboArve("Mandantenverantwortlichen Partner auswählen")
        self.zeitraum = ArveLabel("header", "Zeitraum für Rechnungslauf von")
        self.zeitraum.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.startday = ArvenDate()
        self.startday.setDate(firstpreviousM)
        self.bis = ArveLabel("header", "bis")
        self.bis.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.endday = ArvenDate()
        self.endday.setDate(lastpreviousM)

        
        # set layout for selection widgets

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.mvp_auswahl)
        self.hbox.addWidget(self.zeitraum)
        self.hbox.addWidget(self.startday)
        self.hbox.addWidget(self.bis)
        self.hbox.addWidget(self.endday)
        self.hbox.addSpacerItem(self.spacerH)
        self.MainVerticalLayout.addLayout(self.hbox)

        # create table for mdt per time
        self.label_mdt = ArveLabel("header", "Mandanten mit abzurechnenden Leistungen")
        self.label_files = ArveLabel("header", "Bitte Akten für Leistungsnachweis auswählen")
        self.label_ueberblick = ArveLabel("header", "Überblick")
        self.mdt_rechnungslauf = ArvenTable()
        #self.sel_mdt_id = pyqtSignal(self.mdt_rechnungslauf.model().index(index, 0).data())


        self.mdt_rechnungslauf.doubleClicked.connect(self.fetch_files_mdt)

        #create table for files per mdt and overview, layouts
        self.files_rechnungslauf = ArvenTable()
        self.files_rechnungslauf.doubleClicked.connect(self.open_review)
        self.scroll_uebersicht = QScrollArea()
        self.scroll_uebersicht.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.hbox2 = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox3 = QVBoxLayout()
        self.vbox1.addWidget(self.distanz)
        self.vbox1.addWidget(self.label_mdt)
        self.vbox1.addWidget(self.mdt_rechnungslauf)
        self.vbox2.addWidget(self.distanz)
        self.vbox2.addWidget(self.label_files)
        self.vbox2.addWidget(self.files_rechnungslauf)
        self.vbox3.addWidget(self.distanz)
        self.vbox3.addWidget(self.label_ueberblick)
        self.vbox3.addWidget(self.scroll_uebersicht)

        self.hbox2.addLayout(self.vbox1)
        self.hbox2.addLayout(self.vbox2)
        self.hbox2.addLayout(self.vbox3)

        self.MainVerticalLayout.addLayout(self.hbox2)



        self.setMVP()

    def setMVP(self):
        # todo change to tier
        if bearbeiter == 13:
            self.mvp_auswahl.setModel(Partner())
            self.mvp_auswahl.setModelColumn(2)
            self.mvp_auswahl.activated.connect(self.fetch_mvp)
        else:
            self.mvp_auswahl.setModel(Partner_curr(mvp_id=bearbeiter))
            self.mvp_auswahl.setModelColumn(2)
            self.fetch_reife_mdt(bearbeiter)

    def fetch_mvp(self, index):
        # convert modelindex to mvp_index
        self.fetch_reife_mdt(self.mvp_auswahl.model().index(index, 0).data())

    def fetch_reife_mdt(self, mvp_index):
        self.mdt_rechnungslauf.setModel(ReifeMandanten(self.startday.date().toString('yyyy-MM-dd'),
                                                   self.endday.date().toString('yyyy-MM-dd'), mvp_index))

        self.mdt_rechnungslauf.setColumnHidden(1,True)
        self.mdt_rechnungslauf.setColumnHidden(2, True)
        self.mdt_rechnungslauf.setColumnHidden(3, True)
        self.mdt_rechnungslauf.setItemDelegate(EmptyDelegate())

    def fetch_files_mdt(self, index):
        self.MdtNrInt:int = index.sibling(index.row(), 1).data()

        self.files_rechnungslauf.setModel(ReifeAkten(self.startday.date().toString('yyyy-MM-dd'),
                                                   self.endday.date().toString('yyyy-MM-dd'), self.MdtNrInt))

        self.files_rechnungslauf.setItemDelegate(EmptyDelegate())
        self.files_rechnungslauf.setColumnHidden(1, True)
        self.files_rechnungslauf.setColumnHidden(2, True)










    def fetchfruechtchen(self, mvp_index, mdt):

        self.files_rechnungslauf.setModel(ReifeFruechtchen(self.startday.date().toString('yyyy-MM-dd'),
                                                           self.endday.date().toString('yyyy-MM-dd'), mvp_index, mdt))




    def open_review(self):
        if self._rcwin is None:

            self._rcwin = Korrekturfile('hanno')

        self._rcwin.show()


