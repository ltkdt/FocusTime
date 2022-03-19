import sys
from PyQt6.QtWidgets import (QMainWindow, QTabWidget, QHBoxLayout,
QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy)
from PyQt6.QtGui import QFont,QIcon
from PyQt6 import QtGui
from PyQt6.QtCore import QTimer, QDateTime, QTime, Qt
import json
from itertools import islice
from datetime import date

from pomodoro import Pomodoro
from todo import Todo,AddTaskWindow
from chart import Chart



with open('data.json', 'r') as f:
    data = json.load(f)
dates = data["Dates"]

if len(dates) > 10:
    #Avoid having too many unnecessary dates in data.json    
    del dates[next(islice(dates, 0, None))]
with open('data.json', 'w') as f:
        json.dump(data,f)

#This function will be called to add a pomodoro session to today

def changeWhiteText(list_widget):
    for i in list_widget:
        i.setStyleSheet("color:#ffffff")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FocusTime")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(700,700, 800, 500)
        
        self.setStyleSheet("background-color:#121212")
		
		# Switch buttons for each tab
        self.btn_1 = QPushButton('Pomodoro', self)
        self.btn_2 = QPushButton('Todo', self)
        self.btn_3 = QPushButton('Statistic', self)
        
        changeWhiteText([self.btn_1,self.btn_2,self.btn_3])

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)

        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # ----------------- 
    # Handling switching buttons

    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)
	
	# ----------------- 
    # Handling tabs & Create instance of corresponding applications

    def ui1(self):
        return Pomodoro()

    def ui2(self):
        return Todo()
        
    def ui3(self):
        return Chart()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())