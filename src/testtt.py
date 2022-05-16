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