from src.MainLayout import *
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QScrollArea,
    QWidget,
    QTextEdit,
    QDataWidgetMapper,
    QCalendarWidget
)

from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from src.data import DBModelHumans

mapper_human = QDataWidgetMapper()
mapper_human.setModel(DBModelHumans())


class Human(MainWindow):
    def __init__(self, prozess: str, unternehmen: str):

        super(Human, self).__init__()
        self.setWindowTitle("Arvensteyn - Adressbuch")
        print(f"""{prozess}, {unternehmen}""")

        self.Unternehmen = unternehmen


        self.ButtonZurueck.hide()
        self.center()
        self.setBaseSize(800, 800)

        self.zurueck = ArvenButton("abbrechen")
        self.verticalLayout_3.addWidget(self.zurueck)
        self.zurueck.clicked.connect(self.closing)
        self.Titel = ArveLabel("header", "")
        self.VBox = QVBoxLayout()
        self.HBox1 = QHBoxLayout()
        self.HBox2 = QHBoxLayout()
        self.HBox3 = QHBoxLayout()
        self.HBox4 = QHBoxLayout()
        self.HBox5 = QHBoxLayout()
        self.HBox6 = QHBoxLayout()
        self.HBox7 = QHBoxLayout()

        self.scrollSpace = QScrollArea()
        self.scrollWidget = QWidget()
        self.scrollGrid = QHBoxLayout(self.scrollWidget)
        self.scrollSpace.setWidgetResizable(True)
        self.block_a = HumanWidgets()

        self.scrollGrid.addSpacerItem(self.spacerH)
        self.scrollGrid.addLayout(self.VBox)
        self.scrollGrid.addSpacerItem(self.spacerH)

        self.MainVerticalLayout.addWidget(self.Titel)
        self.MainVerticalLayout.addWidget(self.scrollSpace)

        self.scrollSpace.setWidget(self.scrollWidget)
        self.Prozessschritt(prozess=prozess, unternehmen=unternehmen)

        # ToDo!

        self.block_a.ButtonAdd.clicked.connect(self.human_cleanup)

    def human_cleanup(self):
        Human = {
            "nachname": self.block_a.Nachname.text(),
            "vorname": self.block_a.Vorname.text(),
            "anrede": self.block_a.Anrede.currentText(),  ## ToDo
            "titel": self.block_a.Anrede.currentText(),
            "unternehmen": self.block_a.Arbeitgeber.text(),
            "stellung": self.block_a.Position.text(),
            "strasse": self.block_a.Adresse1.text(),
            "hausnummer": self.block_a.Adresse2.text(),
            "telefon": self.block_a.Telefon.text(),
            "telefon1": self.block_a.Telefon1.text(),
            "telefon2": self.block_a.Telefon2.text(),
            "mobil": self.block_a.Mobil.text(),
            "fax": self.block_a.Fax.text(),
            "email": self.block_a.Email.text(),
            "email2": self.block_a.Email.text(),  # ToDo
            "rel_mdt": self.Unternehmen,
            "rel_auftr": self.Auftragsbezug,
            "kommentar": self.block_a.Kommentare.toPlainText(),
            "kompl_name": f"""{self.block_a.Anrede.currentText()} {self.block_a.Vorname.text()} {self.block_a.Nachname.text()}"""
        }

        from src.data import welcome
        welcome(Human)

    def closing(self):
        self.close()

    def Prozessschritt(self, prozess: str, unternehmen: str) -> object:
        if prozess == "neu":
            self.Titel.setText("Neuen Eintrag im Adressbuch anlegen")

            self.HBox1.addWidget(self.block_a.Vorname)
            self.HBox1.addWidget(self.block_a.Nachname)
            self.VBox.addLayout(self.HBox1)
            self.HBox7.addWidget(self.block_a.Anrede)
            self.HBox7.addWidget(self.block_a.Titel)
            self.VBox.addLayout(self.HBox7)
            self.VBox.addWidget(self.block_a.Arbeitgeber)
            self.VBox.addWidget(self.block_a.Position)
            self.HBox2.addWidget(self.block_a.Adresse1)
            self.HBox2.addWidget(self.block_a.Adresse2)
            self.VBox.addLayout(self.HBox2)
            self.HBox3.addWidget(self.block_a.PLZ)
            self.HBox3.addWidget(self.block_a.Ort)
            self.VBox.addLayout(self.HBox3)
            self.HBox4.addWidget(self.block_a.Telefon, 2)
            self.HBox4.addWidget(self.block_a.extraTelefon1, 1)
            self.VBox.addLayout(self.HBox4)
            self.HBox5.addWidget(self.block_a.Telefon1, 2)
            self.HBox5.addWidget(self.block_a.extraTelefon2, 1)
            self.VBox.addLayout(self.HBox4)
            self.block_a.Telefon1.hide()
            self.block_a.extraTelefon2.hide()
            self.block_a.Telefon2.hide()
            self.VBox.addWidget(self.block_a.Telefon2)
            self.VBox.addLayout(self.HBox5)

            self.VBox.addWidget(self.block_a.Telefon2)

            self.VBox.addLayout(self.HBox4)
            self.VBox.addLayout(self.HBox4)
            self.VBox.addWidget(self.block_a.Mobil)
            self.VBox.addWidget(self.block_a.Fax)
            self.VBox.addWidget(self.block_a.Email)
            self.VBox.addWidget(self.block_a.Kommentare)

            self.VBox.addWidget(self.block_a.PersAddBook)
            self.VBox.addWidget(self.block_a.ButtonAdd)

            self.VBox.addSpacerItem(self.spacerV)

            self.block_a.extraTelefon1.clicked.connect(self.extraTelefon1)
            self.block_a.extraTelefon2.clicked.connect(self.extraTelefon2)

            self.block_a.Arbeitgeber.setText(unternehmen)

        if prozess == "bearbeitung":
            self.Titel.setText("Eintrag im Adressbuch bearbeiten")
            # ToDo: Layout for new entry in separate class, compose

    def extraTelefon1(self):
        self.block_a.extraTelefon2.show()
        self.block_a.Telefon1.show()

    def extraTelefon2(self):
        self.block_a.Telefon2.show()


class HumanWidgets(ArvenWidget):
    def __init__(self):
        super(HumanWidgets, self).__init__(framed="framed")

        Anreden = ["Frau", "Herr"]
        Titel = ["Dr.", "Prof. Dr."]
        limit = QRegularExpression("[0-9]*")
        limiter = QRegularExpressionValidator(limit)

        self.PersAddBook = ArveCheck("Zu meinem persönlichen Adressbuch hinzufügen", False)
        self.Nachname = InputArve("Name")
        self.Nachname.setFixedWidth(250)
        self.Vorname = InputArve("Vorname")
        self.Vorname.setFixedWidth(250)
        self.Anrede = ComboArve("Anrede auswählen")
        self.Anrede.addItems(Anreden)
        self.Titel = ComboArve("Titel auswählen")
        self.Titel.addItems(Titel)
        self.Arbeitgeber = InputArve("Unternehmen")
        self.Position = InputArve("Position im Unternehmen")
        self.Adresse1 = InputArve("Straße")
        self.Adresse2 = InputArve("Hausnummer")
        self.Adresse2.setFixedWidth(100)
        self.PLZ = InputArve("PLZ")
        self.PLZ.setFixedWidth(100)
        self.Ort = InputArve("Ort")
        self.Telefon = InputArve("Telefon")
        self.Telefon.setValidator(limiter)
        self.Telefon.setToolTip(
            "Deutsche Telefonnummern bitte ohne Länderkennziffer aber mit Vorwahl eingeben")
        self.extraTelefon1 = ArvenButton("weitere Telefonnummer hinzufügen")

        self.Telefon1 = InputArve("Telefon")
        self.Telefon1.setValidator(limiter)
        self.Telefon1.setToolTip(
            "Deutsche Telefonnummern bitte ohne Länderkennziffer aber mit Vorwahl eingeben")
        self.extraTelefon2 = ArvenButton("weitere Telefonnummer hinzufügen")

        self.Telefon2 = InputArve("Telefon")
        self.Telefon2.setValidator(limiter)
        self.Telefon2.setToolTip(
            "Deutsche Telefonnummern bitte ohne Länderkennziffer aber mit Vorwahl eingeben")

        self.Mobil = InputArve("Mobiltelefon")
        self.Mobil.setToolTip("Deutsche Mobilnummern bitte ohne Länderkennziffer aber mit Vorwahl eingeben")
        self.Mobil.setValidator(limiter)
        self.Fax = InputArve("Faxnummer")
        self.Fax.setValidator(limiter)
        self.Fax.setToolTip("Deutsche Faxnummern bitte ohne Länderkennziffer aber mit Vorwahl eingeben")
        self.Email = InputArve("E-Mail-Adresse")
        self.Kommentare = QTextEdit()
        self.Kommentare.setStyleSheet("border-radius:4px; background-color: rgb(241,241,241);")
        self.Kommentare.setPlaceholderText("Anmerkungen zu dem Kontakt")

        self.NeuesAnschreiben = ArvenButton("Neues Anschreiben in MS Word anlegen")
        self.ButtonAdd = ArvenButton("Zum Adressbuch hinzufügen")
