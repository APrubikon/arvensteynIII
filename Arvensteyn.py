from PyQt6.QtWidgets import QApplication, QProgressBar, QSystemTrayIcon, QMenu, QMainWindow, QStackedWidget
import sys  # Only needed for access to command line arguments
from PyQt6.QtCore import pyqtSignal, pyqtSlot, QLocale

from src.desktop import Desktop
from src.ArvensteynMenu import Tray

from src.EditMdt import EditMdt
from src.InputHumans import Human, Human_Selection
from src.auftraege import MainFrameAuftraege
from src.auxiliary_gui import ProxyStyle
from src.Login import Login
from src.Timesheet import Timeframe, New_Entry
from src.Rechnungslauf import Rechnungslauf
from security import LeistungenMasterView
from src.data import Leistungen
from src.testtable import Testtable
from src.korrektur import Korrekturfile
from src.variables import workdays


def singleton():
    apps = QApplication.topLevelWidgets()
    for i in apps:
        i.close()


class Switch:
    def __init__(self):
        pass

    def pageNr(self, extension: int):

        if extension == 0:
            self.modul1 = EditMdt()
            self.modul1.show()
            self.modul1.setFocus()


        elif extension == 1:
            singleton()
            #self.modul_trayII = Tray(init=1)
            #self.modul_trayII.show()
            self.modul2 = Desktop()
            self.modul2.showMaximized()

        elif extension == 2:
            singleton()
            self.modul3 = EditMdt()
            self.modul3.showMaximized()

        elif extension == 3:
            singleton()
            self.modul4 = MainFrameAuftraege()
            self.modul4.showMaximized()

        elif extension == 4:
            singleton()
            self.modul5 = Timeframe()
            self.modul5.showMaximized()
        else:
            pass

    def conference_call1(self, extension: int, prozess: str, Aktenbezug: int, Unternehmen: int):
        if extension == 5:
            # no singleton!

            print(prozess, Unternehmen, Aktenbezug)
            self.modul6 = Desktop()
            self.modul6.show()
        else:
            pass

    def conference_call2(self, **kwargs):
        self.modul7 = New_Entry(**kwargs)
        self.modul7.show()
        self.modul7.setFocus()



def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    QLocale.setDefault(QLocale(QLocale.Language.German))

    modul_trayII = Tray(init=1)
    modul_trayII.show()

    Switch.pageNr(self=Switch(), extension=0)


    try:
        sys.exit(app.exec())

    except:
        print("Exiting")


if __name__ == '__main__':
    main()
