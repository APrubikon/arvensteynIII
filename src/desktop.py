from PyQt6.QtWidgets import (QHBoxLayout,
                             QVBoxLayout,
                             QFileDialog)

from src.MainLayout import MainWindow, ArvenButton, InputArve, ComboArve, ArveLabel
from src.config import currentConfig
from src.EditMdt import EditMdt

tier = currentConfig.getcurrent_tier(currentConfig())


class Desktop(MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arvensteyn - Tools")

        self.ButtonZurueck.hide()

        # HBox 1 is Layout for main-Buttons
        self.HBox1 = QHBoxLayout()
        self.Button_Aktenverwaltung = ArvenButton("Aktenverwaltung")
        self.Button_Aktenverwaltung.setMinimumHeight(60)
        self.Button_Aktenverwaltung.setCheckable(True)
        self.Button_Aktenverwaltung.setChecked(False)
        self.Button_Aktenverwaltung.clicked.connect(self.menu_Aktenverwaltung)

        self.HBox1.addWidget(self.Button_Aktenverwaltung)

        self.VBox1 = QVBoxLayout()
        self.VBox1.addSpacerItem(self.spacerV)
        self.Button_NeuMdt = ArvenButton("Neuen Mandanten anlegen")
        self.VBox1.addWidget(self.Button_NeuMdt)

        self.Button_MdtEdit = ArvenButton("Mandanten bearbeiten")
        self.Button_MdtEdit.clicked.connect(self.openMdtListe)
        self.VBox1.addWidget(self.Button_MdtEdit)

        self.Button_Akten = ArvenButton("Aufträge bearbeiten")
        self.Button_Akten.clicked.connect(self.openAuftragliste)
        self.VBox1.addWidget(self.Button_Akten)
        self.VBox1.addSpacerItem(self.spacerV)

        # HBox1
        self.HBox1.addLayout(self.VBox1)

        self.Button_Zeiterfassung = ArvenButton("Zeiterfassung")
        self.Button_Zeiterfassung.setMinimumHeight(60)
        self.Button_Zeiterfassung.setCheckable(True)
        self.Button_Zeiterfassung.clicked.connect(self.openZeiterfassung)
        self.HBox1.addWidget(self.Button_Zeiterfassung)

        self.VBox2 = QVBoxLayout()
        self.VBox2.addSpacerItem(self.spacerV)
        self.Button_Timesheets = ArvenButton('timesheets')
        self.VBox2.addWidget(self.Button_Timesheets)

        self.Button_overview = ArvenButton("Übersicht")
        self.VBox2.addWidget(self.Button_overview)
        self.VBox2.addSpacerItem(self.spacerV)

        self.HBox1.addLayout(self.VBox2)

        self.MainVerticalLayout.addLayout(self.HBox1)
        self.menu_Aktenverwaltung()
        self.menu_Zeiterfassung()

        self.HBox2 = QHBoxLayout()
        self.Button_Rechnungslauf = ArvenButton("Rechnungslauf")
        self.Button_Rechnungslauf.setMinimumHeight(60)
        self.Button_Rechnungslauf.setCheckable(True)
        self.Button_Rechnungslauf.clicked.connect(self.openRechnungslauf)
        self.HBox2.addWidget(self.Button_Rechnungslauf)

        self.MainVerticalLayout.addLayout(self.HBox2)
        self.MainVerticalLayout.addSpacerItem(self.spacerH)
        

    def menu_Aktenverwaltung(self):
        menuList1 = [self.Button_NeuMdt, self.Button_MdtEdit, self.Button_Akten]
        if not self.Button_Aktenverwaltung.isChecked():
            for i in menuList1:
                i.hide()
            self.Button_Zeiterfassung.setDisabled(False)
        else:
            for i in menuList1:
                i.show()
            self.Button_Zeiterfassung.setDisabled(True)

    def menu_Zeiterfassung(self):
        menuList2 = [self.Button_Timesheets, self.Button_overview]
        if not self.Button_Zeiterfassung.isChecked():
            for i in menuList2:
                i.hide()
            self.Button_Aktenverwaltung.setDisabled(False)
        else:
            for i in menuList2:
                i.show()
            self.Button_Aktenverwaltung.setDisabled(True)

    def openMdtListe(self):
        MdtListe = EditMdt()
        MdtListe.showMaximized()
        self.close()

    def openAuftragliste(self):
        from Arvensteyn import Switch
        Switch.pageNr(self=Switch, extension=3)

    def openZeiterfassung(self):
        from Arvensteyn import  Switch
        Switch.pageNr(self=Switch, extension=4)
        
    def openRechnungslauf(self):
        self.close()
        from src.Rechnungslauf import Rechnungslauf
        Rechnungslauf().showMaximized()



