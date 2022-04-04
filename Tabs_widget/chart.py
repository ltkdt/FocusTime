from linecache import lazycache
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QCheckBox, QLineEdit)
import json
import itertools
import pyqtgraph as pg


with open('data.json', 'r') as f:
    data = json.load(f)

dates = data["Dates"]

class Chart(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Chart, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('#121212')
        self.setCentralWidget(self.graphWidget)
        
        dates = data["Dates"].keys()
        dict_dates = dict(enumerate(dates))
        sessions = list(data["Dates"].values())

        #Display string in x axis
        ticks = [list(zip(range(len(dates)), dates))]
        xax = self.graphWidget.getAxis('bottom')
        xax.setTicks(ticks)

        pen = pg.mkPen(color="#aaff00", width = 5)
        
        self.graphWidget.plot(list(dict_dates.keys()), sessions,pen=pen)

'''
def main():
    app = QApplication(sys.argv)
    main = Chart()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
'''

    