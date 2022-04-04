import imp
from linecache import lazycache
import sys
from PyQt6.QtWidgets import (QApplication, QComboBox,
 QWidget, QPushButton, QLabel,QGridLayout ,QVBoxLayout, QHBoxLayout, QCheckBox, QLineEdit, QSpacerItem)
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QRect
import json
import functools

with open('data.json', 'r') as f:
    data = json.load(f)

pair = data["Attached"]
def handle_tag_pair(task,tag):
    pair[task] = tag
    with open('data.json', 'w') as f:
        json.dump(data,f)

#This windows is shown the add button is clicked
class AddTaskWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("AddTask")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(700,700, 300, 200)

        self.setStyleSheet("background-color:#121212")
        self.layout = QVBoxLayout()
        self.lineEdit = QLineEdit()
        self.lineEdit.setStyleSheet("color: #ffffff")

        self.tags_select = QComboBox()
        self.tags_select.setStyleSheet("color:#ffffff")
        for j in data["Tags"]:
            self.tags_select.addItem(j)

        self.AddTasks = QPushButton("Submit")
        self.AddTasks.setStyleSheet("color: #ffffff")
        self.AddTasks.pressed.connect(self.checkTaskAdded)

        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.tags_select)
        self.layout.addWidget(self.AddTasks)
        self.setLayout(self.layout)
            
    #Check if the input for the task is valid (not empty, not duplicate)
    def checkTaskAdded(self):
        cur_tag = str(self.tags_select.currentText())
        if cur_tag != "No tag" and cur_tag!="Delete tag" and cur_tag!="New tag":
            handle_tag_pair(self.lineEdit.text(),cur_tag)

        inputTasked = self.lineEdit.text()
        if len(inputTasked) != "" and inputTasked not in data["Tasks"]:
            data["Tasks"].append(inputTasked)
            with open('data.json', 'w') as f:
                json.dump(data,f)
            self.lineEdit.setText("")
        else:
            self.lineEdit.setText("Invalid, task is already added or is empty")


class Todo(QWidget):
    def __init__(self):
        super().__init__()
        self.openAddTask = None
        '''
        self.setWindowTitle("FocusTime")
        self.setWindowIcon(QIcon("logo.png"))
        self.setGeometry(700,700, 600, 400)
        self.setFixedSize(600,400)
        '''
        self.setStyleSheet("background-color:#121212; color:#ffffff")

        self.widget_display()

    def widget_display(self):
        self.vbox = QVBoxLayout()
        self.layout = QGridLayout()        
        
        
        for i in data["Tasks"]:
            hbox = QHBoxLayout()
            
            temp_label = QLabel()
            temp_label.setText(i)
            temp_checkbox = QCheckBox()
            temp_checkbox.setStyleSheet("background-color : #ffffff")
            temp_checkbox.setMaximumWidth(25)
            spacer = QSpacerItem(15,125)

            temp_tag_label = QLabel()
            temp_tag_label.setText(pair[i])
            

            temp_checkbox.pressed.connect(functools.partial(self.Checked,i,temp_checkbox,temp_label))

            hbox.addWidget(temp_label)
            hbox.addItem(spacer)
            hbox.addWidget(temp_tag_label)
            hbox.addWidget(temp_checkbox)
            hbox.addItem(spacer)
            self.vbox.addLayout(hbox)

        self.layout.addLayout(self.vbox,0,0,10,4)
        self.AddTaskButton = QPushButton("New task")
        self.AddTaskButton.setStyleSheet("border-radius : 50; color:#121212; background-color:#aaff00")
        self.AddTaskButton.pressed.connect(self.AddTask)
        self.layout.addWidget(self.AddTaskButton,11,5)

        self.setLayout(self.layout)

    def Checked(self, tasknames, checkbox,label):
        data["Tasks"].remove(tasknames)
        with open('data.json', 'w') as f:
            json.dump(data,f)

        checkbox.setEnabled(False)
        label.setStyleSheet("color:#ffffff; text-decoration: line-through")
    
    def AddTask(self):
        if self.openAddTask is None:
            self.openAddTask = AddTaskWindow()
        self.openAddTask.show()
'''
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
'''

#test