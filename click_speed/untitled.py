# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(320, 240)
        Form.setMinimumSize(QtCore.QSize(320, 240))
        Form.setMaximumSize(QtCore.QSize(320, 240))

        #클릭버튼
        self.click_button = QtWidgets.QPushButton(Form)
        self.click_button.setGeometry(QtCore.QRect(110, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(20)
        self.click_button.setFont(font)
        self.click_button.setObjectName("click_button")

        #숫자표시 라벨
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(95, 20, 130, 50))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        #time left 라벨
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 190, 90, 30))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        #남은 시간 라벨
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

        self.click_button.clicked.connect(self.count_func)

    def count_func(self):
        """self.time_flow()"""
        global count
        count += 1
        self.label.setNum(count)

    """
    def time_flow(self):
        while str(self.label_3.text()) == "0":
            global time_left
            time_left -= 1
            self.label_3.setNum(time_left)

        print("done")
    """
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.click_button.setText(_translate("Form", "Click!"))
        self.label.setText(_translate("Form", "CLICK COUNT"))
        self.label_2.setText(_translate("Form", "time left :"))
        self.label_3.setText(_translate("Form", "10"))


if __name__ == "__main__":
    count = 0
    time_left = 10
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

