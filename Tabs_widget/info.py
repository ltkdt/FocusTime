import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QTextCursor

class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#121212;color:#ffffff")

        mainLayout = QVBoxLayout()

        self.textEditor = QTextEdit()
        mainLayout.addWidget(self.textEditor)

        self.textEditor.setHtml(
            '''
            <h1>FocusTime</h1>
            <pre> This is mainly a pomodoro app. There are 3 modes :
 - Pomodoro : you start with a work session that last for 25
 minutes followed by a 5-minute time break. Repeat that.
 - Todo : A simple todo list. 
 - Tracker : track the number of pomodoro sessions you have each day on a graph
This is version 1.0.0 
Upcoming features:
 - Tags for to-do
 - Assign a session with a task, track the number of time spend on that task
Github: https://github.com/ks5-dev/FocusTime
             </pre>
            '''
        )

        self.setLayout(mainLayout)

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Info()
    demo.show()
    sys.exit(app.exec())
'''