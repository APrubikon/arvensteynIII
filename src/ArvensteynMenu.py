
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PyQt6.QtGui import QIcon, QAction
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSlot, QModelIndex, pyqtSignal, Qt
from src.QuickConnect import quickconnect
from src.data import MostRecentFiles
from src.desktop import Desktop



class Tray(QSystemTrayIcon):
    def __init__(self, init:int):
        super(Tray, self).__init__()
        icon = QIcon("/Users/Shared/PycharmProjects/arvensteynIII/gui/g2045-3w.png")

        self.setIcon(icon)
        self.setVisible(True)

        # Create the menu
        self.Main_Menu = QMenu()
        self.MainMenu1 = QMenu("Zeiterfassung")
        self.MainMenu2 = QAction("Aktenverwaltung")
        self.MainMenu3 = QAction("Arvensteyn Desktop")
        #self.MainMenu4 = QAction("Arvensteyn Login")
        self.MainMenu5 = QAction("Quit")
        #self.MainMenu4.triggered.connect(self.Login)
        self.MainMenu5.triggered.connect(self.quit)
        self.MainMenu3.triggered.connect(self.Desktop)

        self.list = MostRecentFiles()
        self.indexlist = []



        for i in range(self.list.rowCount()):
            az = self.list.index(i, 1)
            self.indexlist.append(az)

       # dynamic population of Menu with previously used filenumbers
        for item in self.indexlist:
            timesheet = self.MainMenu1.addAction(item.data(Qt.ItemDataRole.DisplayRole))
            timesheet.triggered.connect(lambda triggered, a=item : self.quickOpen(a))

        if init == 0:
            self.Main_Menu.addAction(self.MainMenu4)
            self.Main_Menu.addAction(self.MainMenu5)

            self.setContextMenu(self.Main_Menu)
            self.show()

        if init == 1:
            self.Main_Menu.addMenu(self.MainMenu1)
            self.Main_Menu.addAction(self.MainMenu2)
            self.Main_Menu.addAction(self.MainMenu3)
            self.Main_Menu.addAction(self.MainMenu5)
            self.setContextMenu(self.Main_Menu)


    @pyqtSlot(QtCore.QModelIndex)
    def quickOpen(self, item):
        quickconnect(item)

    def Desktop(self):
        desktop =  Desktop()
        desktop.showMaximized()
        desktop.setFocus()

    def quit(self):
        app = QApplication.instance()
        print("outta here finally")
        app.quit()








