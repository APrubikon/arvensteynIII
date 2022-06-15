from PyQt6.QtWidgets import QWidget, QLineEdit, QDataWidgetMapper, QVBoxLayout, QPushButton
from PyQt6.QtSql import QSqlQuery, QSqlRelationalTableModel, QSqlRelation, QSqlTableModel

class EditClient(QWidget):
    def __init__(self, clientnr:int):
        super(EditClient, self).__init__()

        self.example_client_name = QLineEdit()
        self.example_representative_display = QLineEdit()
        self.example_representative_display.setReadOnly(True)
        self.add_representative = QPushButton()
        self.add_representative.clicked.connect(self.open_form2)

        # bunch of other input widgets

        self.example_layout = QVBoxLayout()
        self.example_layout.addWidget(self.example_client_name)
        self.example_layout.addWidget(self.example_representative_display)
        self.example_layout.addWidget(self.add_representative)
        self.setLayout(self.example_layout)

        self.mapper = QDataWidgetMapper()
        self.client_model = QSqlRelationalTableModel()

        self.client_model.setTable("clients")
        self.client_model.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.client_model.setJoinMode(QSqlRelationalTableModel.JoinMode.LeftJoin)
        self.client_model.setRelation(3, QSqlRelation("humans", "human_id", "name")) # humanid = 0, name = 1
        self.client_model.select()

        self.mapper.setModel(self.client_model)
        self.mapper.addMapping(self.example_client_name, 1)

        ## clientnr is selected in another function which should not be relevant here. It is passed into this class)
        self.mapper.setCurrentIndex(clientnr)

    def open_form2(self):
        self.form2 = New_Representative()


class New_Representative(QWidget):
    def __init__(self):
        super(New_Representative, self).__init__()

        self.person_model = QSqlTableModel()
        

        self.example_person = QLineEdit()
        # another bunch of input widgets here
        self.add_person = QPushButton()
        self.add_person.clicked.connect(self.add_new_person)

        self.person_layout = QVBoxLayout()
        self.person_layout.addWidget(self.example_person)
        self.person_layout.addWidget(self.add_person)
        self.setLayout(self.person_layout)

    def add_person(self):
        new_human = self.person_model.record()
        new_human.setGenerated(0, False) # index of new person is generated by Postgresql
        new_human.setValue(1, self.example_person.text())
        if not self.person_model.insertRecord(-1, new_human):
            print(self.person_model.lastError().text())


    def get_last_index(self):
        lastval = QSqlQuery()
        lastval.exec("select lastval()")
        lastval.next()
        val = lastval.value(0)
        return val







