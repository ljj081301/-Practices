# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import time
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(320, 240)
        Form.setMinimumSize(QtCore.QSize(320, 240))
        Form.setMaximumSize(QtCore.QSize(320, 240))

        #스타트버튼
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(110, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(20)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")

        #클릭버튼
        self.click_button = QtWidgets.QPushButton(Form)
        self.click_button.setGeometry(QtCore.QRect(110, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(20)
        self.click_button.setFont(font)
        self.click_button.setObjectName("click_button")
        self.click_button.hide()

        #숫자표시 라벨
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(85, 20, 160, 50))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        #숫자기록 라벨
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 190, 155, 30))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        #"/s" 라벨
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 90, 30))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.start_button.clicked.connect(self.start)
        self.click_button.clicked.connect(self.count_func)

    def start(self):
        self.start_button.hide()
        self.click_button.show()
        Thread(target=self.time_start).start()
        Thread(target=self.calcul_speed).start()
        

    def count_func(self):
        global click_count
        click_count += 1
        self.label.setNum(click_count)
        
    def time_start(self):
        global click_count, time_count

        while time_count != 10:
            print(time_count)
            time_count += 1
            time.sleep(1)

        self.click_button.hide()
        time.sleep(2)
        self.start_button.show()
        self.label.setText("CLICK COUNT")
        self.label_2.setNum(0)
        click_count = 0
        time_count = 0

        return click_count, time_count
    
    def calcul_speed(self):
        global time_count, click_count, time_count
        print("실행됨")
        while time_count != 10:
            speed = click_count/time_count
            self.label_2.setNum(speed)
            time.sleep(0.5)


    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Click Speed Check"))
        self.start_button.setText(_translate("Form", "Start!"))
        self.click_button.setText(_translate("Form", "Click!"))
        self.label.setText(_translate("Form", "CLICK COUNT"))
        self.label_2.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "/s"))


if __name__ == "__main__":
    click_count = 0
    time_count = 0
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

