from PyQt6.QtSql import (QSqlDatabase,
                         QSqlRelationalTableModel,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlTableModel,
                         QSqlDriver,
                         QSqlQuery,
                         QSqlRecord)
from PyQt6.QtWidgets import QMessageBox


class DB(QSqlDatabase):
    def __init__(self):
        super(DB, self).__init__()

        db = QSqlDatabase.addDatabase('QPSQL')

        db.setHostName('ella.db.elephantsql.com')
        db.setDatabaseName('ddtxjske')
        db.setUserName('ddtxjske')
        db.setPassword('C1QY08PhSjH1eEtXgB4ymfCnYj5TYnNE')

#if ConnectionError:
#    QMessageBox.critical(
#        None,
#        "QTableView Example - Error!",
#        "Database Error")
#else:
#    pass
#
#
        #ToDo: check to see if internet connection is available

        if not db.open():
            QMessageBox.critical(
                None,
                "QTableView Example - Error!",
                "Database Error: %s" % db.lastError().databaseText(),
            )

        print("db0open")