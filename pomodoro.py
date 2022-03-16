from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont,QIcon
from PyQt6.QtCore import QTimer, Qt, QUrl
import json
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from itertools import islice
from datetime import date
from playsound import playsound

from numpy import add
with open('data.json', 'r') as f:
    data = json.load(f)
dates = data["Dates"]
if len(dates) > 10:
    print(True)
    del dates[next(islice(dates, 0, None))]
with open('data.json', 'w') as f:
        json.dump(data,f)

def add_data_today(flag = True):
    today = date.today()
    month = str(today.strftime("%m"))
    day = str(today.strftime("%d"))
    if flag:
        with open('data.json', 'r') as f:
            data = json.load(f)
            dates = data["Dates"]
            
            if "{d}-{m}".format(d=day,m=month) in dates:
                dates["{d}-{m}".format(d=day,m=month)] += 1
                with open('data.json', 'w') as f:
                    json.dump(data,f)
            else:
                dates["{d}-{m}".format(d=day,m=month)] = 1
                with open('data.json', 'w') as f:
                    json.dump(data,f)

class Pomodoro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FocusTime")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(700,700, 600, 400)
        self.setStyleSheet("background-color:#121212")

        self.counter = 0
        self.minute ="00"
        self.second = "00"
        self.count = "00"
        self.startWatch = False
        
        self.num_sessions = 0

        timer = QTimer(self)
        timer.timeout.connect(self.Clock)
        timer.start(100)


        self.widget_display()

    def widget_display(self):
        self.layout = QVBoxLayout()

        self.CurTime = QLabel("00:00:00")
        self.CurTime.setStyleSheet("color:#aaff00")
        self.CurTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CurTime.setFont(QFont('LCD', 35))


        self.StartButton = QPushButton("Start a pomodoro session",self)
        self.StartButton.setStyleSheet("color:#ffffff")
        self.StartButton.clicked.connect(lambda: self.onPomodoroSession())

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.ResetButton = QPushButton("Stop a pomodoro session",self)
        
        self.ResetButton.setStyleSheet("color:#ffffff")
        self.ResetButton.clicked.connect(lambda: self.onPomodoroReset())
        
        self.layout.addWidget(self.CurTime)
        self.layout.addWidget(self.StartButton)
        self.layout.addItem(self.verticalSpacer)
        self.layout.addWidget(self.ResetButton)
        
        self.setLayout(self.layout)
        
    def onPomodoroSession(self):
        #Disable the button from getting clicked
        #QTimer.singleShot(5000, lambda: self.StartButton.setDisabled(False))
        self.startWatch = True
        self.StartButton.setEnabled(False)
    def onPomodoroReset(self):
        self.startWatch = False
        self.StartButton.setEnabled(True)
        # Reset all counter variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        # Set the initial values for the stop watch
        self.CurTime.setText("00:00:00")


    def Clock(self):
        if self.num_sessions % 2 == 0:
            self.showCounter("25")
        else:
            self.showCounter("05")
        # Check the value of startWatch  variable to start or stop the Stop Watch
        
        #while True:
        '''
            for i in range(4):
                self.showCounter(2)
                self.showCounter(1)
            self.showCounter(3)
            '''
    def showCounter(self,stop):
        if self.startWatch:
        
            self.counter += 1

            # Count and set the time counter value
            cnt = int((self.counter/10 - int(self.counter/10))*10)
            self.count = '0' + str(cnt)

            # Set the second value
            if int(self.counter/10) < 10 :
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))
                # Set the minute value
                if self.counter / 10 == 60.0 :
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10 :
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)
            text = self.minute + ':' + self.second + ':' + self.count
        # Display the stop watch values in the label
            self.CurTime.setText(text)
            
            if self.minute == stop:
                self.onPomodoroReset()
                playsound("sound.wav")
                
                self.num_sessions += 1
                if self.num_sessions % 2 == 1:
                    add_data_today()
                    self.StartButton.setText("Start a breaktime")
                else :
                    add_data_today(flag=False)
                    self.StartButton.setText("Start a pomodoro session")
            
    
    def placeholder(self):
        pass
           

'''
app = QApplication(sys.argv)
window = Pomodoro()
window.show()
sys.exit(app.exec())
'''