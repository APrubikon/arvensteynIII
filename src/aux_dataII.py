from PyQt6.QtSql import QSqlRelationalTableModel
from PyQt6.QtCore import Qt, QVariant



class LeistungenTableModel(QSqlRelationalTableModel):
    def __init__(self, *args, **kwargs):
        super(QSqlRelationalTableModel, self).__init__(*args, **kwargs)
        self.booleanSet = [9,10, 13]  # columns with checkboxes
        self.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.setHeaderData(2, Qt.Orientation.Horizontal, "Leistungsbeschreibung")
        self.setHeaderData(4, Qt.Orientation.Horizontal, "Tag der Leistung")
        self.setHeaderData(5, Qt.Orientation.Horizontal, "Dauer der Leistung")
        self.setHeaderData(13, Qt.Orientation.Horizontal, "€")

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        value = super(QSqlRelationalTableModel, self).data(index)

        if index.column() in self.booleanSet:

            if role == Qt.ItemDataRole.CheckStateRole:
                return Qt.CheckState.Unchecked if value == 0 else Qt.CheckState.Checked
            else:
                return QVariant()
        return QSqlRelationalTableModel.data(self, index, role)

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if not index.isValid():
            return False
        if index.column() in self.booleanSet:
            if role == Qt.ItemDataRole.CheckStateRole:
                val = 0 if value == Qt.CheckState.Unchecked else 1

                self.dataChanged.emit(index, index, (role,))
                return super(QSqlRelationalTableModel,self).setData(index, val, Qt.ItemDataRole.CheckStateRole)
            else:
                return False

        return super(QSqlRelationalTableModel,self).setData(index, value, Qt.ItemDataRole.EditRole)

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        if index.column() in self.booleanSet:
            fl = Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable
            return fl
        else:
            return super(QSqlRelationalTableModel,self).flags(index)

















