from src.variables import workdays
from PyQt6 import Qt6
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QApplication
import sys
from PyQt6.QtCharts import QBarSet, QStackedBarSeries, QChart, QChartView
y1 = [5, 5, 7, 4.25, 3.5, 8, 8, 1, 6, 2]
x = workdays()
y2 = []
for i in y1:
    y2.append(8-i)

class TestIllu():
    def __init__(self):
        self.set1 = ()

        self.set1 = QBarSet('non billable')
        self.set2 = QBarSet('billable')

        self.set1.append(y1)
        self.set2.append(y2)

        self.series = QStackedBarSeries()
        self.series.append(self.set1)
        self.series.append(self.set2)


        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle('Auslastung')

        self.cv = QChartView(self.chart)
        #self.cv.setRenderHint

class TestBed(QWidget):
    def __init__(self):
        super(TestBed, self).__init__()

        vb = QHBoxLayout()
        self.setLayout(vb)
        chart = TestIllu()
        vb.addWidget(chart)



def main():
    app = QApplication(sys.argv)

    w = TestBed()
    w.show()
    try:
        sys.exit(app.exec())

    except:
        print("Exiting")


if __name__ == '__main__':
    main()





    index integer nn
    warning text
    full_name text
    name_prefix text
    name_first text
    name_middle text
    name_last text
    name_postfix text
    nickname text
    birthday date
    photo bytea #todo
    organization text
    title text
    role_ text
    logo_url text
    mailer text
    home_address_1 text
    home_city_1 text
    home_state_1 text
    home_zip_1 integer
    home_country_1 text#
    home_address_2 text
    home_city_2 text
    home_state_2 text
    home_zip_2 integer
    home_country text
    home_address_3 text
    home_city_3 text
    home_state_3 text
    home_zip_3 integer
    home_country_2 text
    work_address_1 text
    work_city_1 text
    work_state_1 text
    work_zip_1 integer
    work_country_1 text
    work_address_2 text
    work_city_2 text
    work_state_2 text
    work_zip_2 integer
    work_country_2 text
    work_address_3 text
    work_city_3 text
    work_state_3 text
    work_zip_3 integer
    work_country_3 text
    home_phone_1 text
    home_phone_2 text
    home_phone_3 text
    work_phone_1 text
    work_phone_2 text
    work_phone_3 text
    home_fax_1 text
    home_fax_2 text
    home_fax_3 text
    work_fax_1 text
    work_fax_2 text
    work_fax_3 text
    mobile_phone_1 text
    mobile_phone_2 text
    mobile_phone_3 text
    home_email_1 text
    home_email_2 text
    home_email_3 text
    work_email_1 text
    work_email_2 text
    work_email_3 text
    geocode text
    timezone text
    agent text
    note text
    rev text
    url text
    uidaim text
    icq text
    msn text
    yahoo text
    jabber text
    skype text
    gadugadu text
    groupwise text
    mandantid integer
    ges_vertreter boolean
    CONSTRAINT humans_pkey PRIMARY KEY (index)