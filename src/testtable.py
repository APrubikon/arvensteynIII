from src.MainLayout import *
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QCompleter,
    QDataWidgetMapper,
    QTableView,
    QAbstractItemView
)

from PyQt6 import QtCore
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from datetime import date

today_date = date.today()
Jahr = today_date.strftime("%y")

from src.auxiliary_gui import EmptyDelegate
from src.data import *


class Testtable(MainWindow):
    def __init__(self):
        super(Testtable, self).__init__()

        self.testtable = ArvenTable()
        self.Layout = QHBoxLayout()
        self.Layout.addWidget(self.testtable)
        self.setLayout(self.Layout)

        self.testtable.setModel(LastFiles())
        self.MainVerticalLayout.addLayout(self.Layout)