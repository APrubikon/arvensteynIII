
from PyQt6.QtWidgets import QApplication, QProgressBar, QSystemTrayIcon, QMenu, QMainWindow, QStackedWidget
import sys

from src.MainLayout import *

class Window1(MainWindow):
    def __init__(self):
        super(Window1, self).__init__()
        self._w2 = None
        self.button = ArvenButton("press")
        self.button.setParent(self)
        self.button.clicked.connect(self.open)

    def open(self):
        if self._w2 is None:

            self._w2 = Window2(parent=self)
        self._w2.show()





class Window2(MainWindow):
    def __init__(self, parent=None):
        super(Window2, self).__init__()
        label = ArveLabel("notice", "Hello")
        label.setParent(self)














def main():
    app = QApplication(sys.argv)
    #app.setQuitOnLastWindowClosed(False)

    w = Window1()
    w.show()

    try:
        sys.exit(app.exec())

    except:
        print("Exiting")


if __name__ == '__main__':
    main()