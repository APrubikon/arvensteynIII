from PyQt6 import uic, QtGui
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QLineEdit,
                             QLabel,
                             QSizePolicy,
                             QComboBox,
                             QPushButton,
                             QSpacerItem,
                             QCheckBox,
                             QRadioButton,
                             QDateEdit,
                             QSpinBox,
                             QTableView,
                             QAbstractItemView
                             )
from PyQt6.QtCore import Qt, QLocale

import datetime

today = datetime.datetime.today()
today = today.strftime("%d.%m.%Y")

from src.config import currentConfig as curr


class MainWindow(QWidget, curr):
    def __init__(self):
        super().__init__()
        self.setObjectName("frame")
        # open main layout
        self.ui = uic.loadUi('/Users/Shared/PycharmProjects/arvensteynIII/gui/QWidgetVorlage.ui', self)

        self.quitSc = QShortcut(QKeySequence('command+Q'), self)
        self.quitSc.activated.connect(self.quit)

        kopfzeile = f"""{self.Beruf} {self.Name}"""
        self.Kopfzeile.setText(kopfzeile)
        self.Kopfzeile.setStyleSheet("font: bold;")

        self.setStyleSheet("background-color:white")
        pixmap = QtGui.QPixmap('/Users/Shared/PycharmProjects/arvensteynIII/gui/g2046-2.png')
        self.labelLogo.setPixmap(pixmap)

        self.Arve = QtGui.QIcon("/Users/Shared/PycharmProjects/arvensteynIII/gui/g2045-3t.png")
        self.ButtonZurueck.setIcon(self.Arve)
        self.labelDatum.setText(today)
        self.distanz = ArveLabel("notice", "")

        self.spacerV = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Minimum,
                                   vPolicy=QSizePolicy.Policy.Expanding)
        self.spacerH = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Expanding,
                                   vPolicy=QSizePolicy.Policy.Minimum)

        self.ButtonZurueck.clicked.connect(self.returnDesktop)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def returnDesktop(self):
        apps = QApplication.topLevelWidgets()
        for i in apps:
            i.close()
        from src.desktop import Desktop
        Desktop().showMaximized()





    def quit(self):
        app = QApplication.instance()
        print("outta here")
        app.quit()


class ArvenButton(QPushButton):
    def __init__(self, Text):
        super().__init__()

        self.setupbt(Text)

    def setupbt(self, Text):
        self.setFlat(False)
        self.setText(Text)
        self.Arve = QtGui.QIcon("/Users/Shared/PycharmProjects/arvensteynIII/gui/g2045-3t.png")
        self.setIcon(self.Arve)
        self.setGeometry(200, 100, 60, 35)

        self.setMinimumHeight(33)

        Buttonstyle = 'QPushButton {border-radius:4px; background-color: ' \
                      'qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); ' \
                      'color: rgb(9, 58, 112)}'\
                      'QPushButton:pressed {background-color: qlineargradient' \
                      '(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); color: rgb(9, 58, 112)}'

        self.setStyleSheet(Buttonstyle)


class InputArve(QLineEdit):
    def __init__(self, placeholder):
        super().__init__()

        self.setupInput(placeholder)

    def setupInput(self, placeholder):
        self.setMinimumHeight(35)
        self.setPlaceholderText(placeholder)
        self.adjustSize()
        self.setStyleSheet("border: 1px #8f8f91; border-radius:4px; background-color:rgb(241,241,241)")


class ComboArve(QComboBox):
    def __init__(self, placeholder):
        super().__init__()

        self.setupInput(placeholder)

    def setupInput(self, placeholder):
        self.setMinimumHeight(35)
        self.acceptDrops()
        self.setPlaceholderText(placeholder)
        self.adjustSize()
        styled = "QComboBox { combobox-popup: 0; }" \
                 "QComboBox {border: 1px gray; border-radius: 4px; padding: 1px 18px 1px 3px; min-width: 6em;} " \
                 "ComboBox:editable {background: white;}" \
                 "QComboBox:!editable, QComboBox::drop-down:editable {background: rgb(241,241,241)}" \
                 "QComboBox::down-arrow {image: url(/Users/Shared/PycharmProjects/arvensteynIII/gui/g2045-3t.png)}" \
                 "QComboBox: {selection-background-color: rgb(255, 0, 0); selection-color: rgb(0, 0, 0);}"

        self.setStyleSheet(styled)
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.ColorGroup.All, QtGui.QPalette.ColorRole.PlaceholderText,
                     QtGui.QColor(50, 50, 50, 127))
        self.setPalette(pal)


class ArveLabel(QLabel):
    def __init__(self, stylus, Text):
        super().__init__()

        self.setText(Text)
        self.setFontStyle(stylus)

    def setFontStyle(self, stylus):
        if stylus == 'header':
            Stylesheet = """background-color: rgb(255,255,255); font: bold;"""
            self.setStyleSheet(Stylesheet)
        elif stylus == 'notice':
            Stylesheet = """background-color: rgb(255,255,255);"""
            self.setStyleSheet(Stylesheet)


class ArveCheck(QCheckBox):
    def __init__(self, Text, Status):
        super(ArveCheck, self).__init__()

        self.setText(Text)
        if Status == True:
            self.setChecked(True)
        elif Status == False:
            self.setChecked(False)
        else:
            self.setChecked(False)


class ArvenWidget(QWidget):
    def __init__(self, framed):
        super(ArvenWidget, self).__init__()
        self.spacerV = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Minimum,
                                   vPolicy=QSizePolicy.Policy.Expanding)
        self.spacerH = QSpacerItem(10, 10, hPolicy=QSizePolicy.Policy.Expanding,
                                   vPolicy=QSizePolicy.Policy.Minimum)

        self.framing(framed)

    def framing(self, framed):
        if framed == "framed":
            borderstyle = "border-style:solid; border-color:lightgray; border-width:1px; border-radius:4px;"
            self.setStyleSheet(borderstyle)
        elif framed == "not":
            borderstyle = "border-style:none; border-color:lightgray; border-width:1px; border-radius:4px;"
            self.setStyleSheet(borderstyle)


class ArvenRadio(QRadioButton):
    def __init__(self, text, status):
        super(ArvenRadio, self).__init__()

        borderstyle = "border-style:none; border-color:lightgray; border-width:1px; border-radius:4px;"
        self.setStyleSheet(borderstyle)

        self.setText(text)

        if status == "checked":
            self.setChecked(True)
        else:
            self.setChecked(False)


class ArvenDate(QDateEdit):
    def __init__(self):
        super(ArvenDate, self).__init__()
        self.setMinimumHeight(35)
        self.adjustSize()
        self.setLocale(QLocale(QLocale.Language.German, QLocale.Country.Germany))
        self.setCalendarPopup(False)
        self.setStyleSheet("background-color:rgb(241, 241, 241); border-width:1px")
        self.setDate(datetime.datetime.today())
        self.setDisplayFormat("dd. MMMM yyyy")

class StringBox(QSpinBox):
    def __init__(self, strings, parent=None):
        super(StringBox, self).__init__(parent)
        self.setStrings(strings)
        self.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.setMinimumHeight(35)

    def strings(self):
        return self._strings

    def setStrings(self, strings):
        self._strings = tuple(strings)
        self._values = dict(zip(strings, range(len(strings))))
        self.setRange(0, len(strings) - 1)

    def textFromValue(self, value):
        return self._strings[value]

    def valueFromText(self, text):
        return self._values[text]



class ArvenTable(QTableView):
    def __init__(self):
        super(ArvenTable, self).__init__()
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setStyleSheet("QTableView {border-style:solid; border-color:lightgray; border-width:1px; "
                           "border-radius:4px; gridline-color:white}"
                           "QTableView::item{border-top-style: solid; border-top: 1px; border-top-color: lightgray; "
                           "border-bottom: 1px; border-bottom-style:solid; border-bottom-color: lightgray}")
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.horizontalHeader().setStretchLastSection(True)
