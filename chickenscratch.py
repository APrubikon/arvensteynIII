#import matplo
#
#
#SELECT SUM(amount) as amount_sum, date FROM table GROUP BY date;

from PyQt6.QtWidgets import QApplication, QProgressBar, QSystemTrayIcon, QMenu, QMainWindow, QStackedWidget, QWidget, QHBoxLayout
import sys

from src.variables import workdays
import pyqtgraph as pg
import numpy as np
import datetime, time


class Testbed():
    def __init__(self):

        # creating a pyqtgraph plot window
        window = pg.plot()
        box = QHBoxLayout()

        # icon for plot window
        #icon = QIcon("logo.png")

        # setting icon to the plot window
        #window.setWindowIcon(icon)

        # setting window geometry
        # left = 100, top = 100
        # width = 600, height = 500
        window.setGeometry(100, 100, 800, 300)

        # title for the plot window
        title = "Auslastung Monat"

        # setting window title to plot window
        window.setWindowTitle(title)

        # create list for y-axis
        x = workdays()
        y1 = [5, 5, 7, 6, 3, 8, 8, 1, 6, 2, 5, 5, 7, 8, 3, 8, 7, 1, 6, 2, 3, 4]
        y2 = []
        for i in range(len(workdays())):
            y2.append(8)

        print(x)




        # create horizontal list i.e x-axis
        x = workdays()

        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = blue
        bargraph = pg.BarGraphItem(x=x,
                                   height=y2,
                                   width=0.6,
                                   brush= '#f6f7fa')
       # pg.BarGraphItem(x0=start, , width=stintlist[t + 1]['StintLength'], height=0.6,

        # add item to plot window
        # adding bargraph item to the window
        window.addItem(bargraph)
        window.setBackground('white')


        # setting scale of the bar graph
        # bargraph.scale(600, 30)

        #box.addItem(window)

        #self.setLayout(box)





















def main():
    app = QApplication(sys.argv)

    Testbed()

    try:
        sys.exit(app.exec())



    except:
        print("Exiting")


if __name__ == '__main__':
    main()