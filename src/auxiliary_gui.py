from PyQt6.QtCore import pyqtSignal, pyqtSlot, QEvent, QObject, QPoint
from PyQt6.QtGui import QPixmap, QMouseEvent
from PyQt6.QtWidgets import QLabel, QMainWindow, QItemDelegate

class EmptyDelegate(QItemDelegate):
    def __init__(self):
        super(EmptyDelegate, self).__init__()

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None