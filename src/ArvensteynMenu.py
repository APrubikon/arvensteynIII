
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import pyqtSlot
from src.config import currentConfig
from src.data import FFindfromAZ



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

        self.list = currentConfig.getcurrentfiles(self=currentConfig())

        for item in self.list:
            self.MainMenu1.addAction(str(item))

        for action in self.MainMenu1.actions():
            action.triggered.connect(lambda checked, a=action.text(): self.quickOpen(a))

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


    @pyqtSlot()
    def quickOpen(self, item:str):
        FFindfromAZ(file=item)

    def Desktop(self):
        from src.desktop import Desktop
        Desktop().showMaximized()

    def quit(self):
        app = QApplication.instance()
        print("outta here finally")
        app.quit()








