from src.MainLayout import *
from PyQt6.QtWidgets import QTableView, QAbstractItemView
from src.data import Leistungen




class LeistungenMasterView(MainWindow):
    def __init__(self):
        super(LeistungenMasterView, self).__init__()



        self.masterview = QTableView()
        self.masterview.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.masterview.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.model = Leistungen()
        self.masterview.setModel(self.model)

        self.MainVerticalLayout.addWidget(self.masterview)

        self.model.insertRowIntoTable()


