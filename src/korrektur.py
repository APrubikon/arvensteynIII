from src.MainLayout import *
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout
)

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from src.variables import *
from src.auxiliary_gui import EmptyDelegate
from src.data import DBModel1, Partner, Partner_curr, ReifeMandanten, ReifeAkten, ReifeFruechtchen
from src.config import currentConfig

bearbeiter = currentConfig.getcurrent_ra(currentConfig())


class Korrekturfile(MainWindow):
    def __init__(self, auftrag):
        super(Korrekturfile, self).__init__()


        self.setWindowTitle(auftrag)
        self.setWindowModality(Qt.WindowModality.NonModal)

        self.Hbox = QHBoxLayout()
        self.warning = ArveLabel("header", "Achtung:")
        self.warningtext = ArveLabel("notice", "Hier vorgenommene Änderungen werden direkt in der Datenbank gespeichert"
                                               " und sind maßgeblich für die Rechnung an den Mandanten.")
        self.empty = ArveLabel("notice", "")
        self.rechnungslauf = ArvenTable()

        self.vbox_central = QVBoxLayout()
        self.vbox_central.addWidget(self.warning)
        self.vbox_central.addWidget(self.warningtext)
        self.vbox_central.addWidget(self.empty)
        self.vbox_central.addWidget(self.rechnungslauf)

        self.MainVerticalLayout.addLayout(self.Hbox)

        #self.Hbox.addSpacerItem(self.spacerH)
        self.Hbox.addLayout(self.vbox_central)
        #self.Hbox.addSpacerItem(self.spacerH)

        self.vbox_right = QVBoxLayout()
        self.freigabe = ArvenButton("Leistungsaufstellung für Rechnung freigeben")
        self.mdt = ArveLabel('notice', 'a')
        self.auftrag = ArveLabel('notice', 'b')
        self.zeitraum = ArveLabel('notice', 'aaa')
        self.gesamt = ArveLabel('notice', '')
        self.stdsatz = ArveLabel('notice', '')
        self.formular = QFormLayout()
        self.formular.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        self.formular.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.formular.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        self.formular.addRow("<b>Mandant:</b>", self.mdt)
        self.formular.addRow("<b>Auftrag:</b>", self.auftrag)
        self.formular.addRow("<b>Abrechnungszeitraum:</b>", self.zeitraum)

        self.vbox_right.addWidget(self.empty)
        self.vbox_right.addWidget(self.empty)

        self.vbox_right.addLayout(self.formular)
        self.vbox_right.addSpacerItem(self.spacerV)
        self.vbox_right.addWidget(self.freigabe)
        self.Hbox.addLayout(self.vbox_right)
        




        self.mdt = ArveLabel('notice', '')
        self.mdt = ArveLabel('notice', '')
        self.mdt = ArveLabel('notice', '')

