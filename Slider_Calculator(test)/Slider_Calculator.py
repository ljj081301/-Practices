# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Slider_Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 500)
        MainWindow.setMinimumSize(QtCore.QSize(640, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #중앙 슬라이더
        self.sl_result = QtWidgets.QSlider(self.centralwidget)
        self.sl_result.setGeometry(QtCore.QRect(260, 70, 121, 311))
        self.sl_result.setOrientation(QtCore.Qt.Vertical)
        self.sl_result.setMinimum(0)
        self.sl_result.setMaximum(200)
        self.sl_result.setObjectName("sl_result")

        #왼쪽 슬라이더
        self.sl_1 = QtWidgets.QSlider(self.centralwidget)
        self.sl_1.setGeometry(QtCore.QRect(90, 100, 61, 241))
        self.sl_1.setOrientation(QtCore.Qt.Vertical)
        self.sl_1.setMinimum(0)
        self.sl_1.setMaximum(100)
        self.sl_1.setObjectName("sl_1")

        #오른쪽 슬라이더
        self.sl_2 = QtWidgets.QSlider(self.centralwidget)
        self.sl_2.setGeometry(QtCore.QRect(490, 100, 61, 241))
        self.sl_2.setOrientation(QtCore.Qt.Vertical)
        self.sl_2.setMinimum(0)
        self.sl_2.setMaximum(100)
        self.sl_2.setObjectName("sl_2")

        #중앙 버튼
        self.calcul_button = QtWidgets.QPushButton(self.centralwidget)
        self.calcul_button.setGeometry(QtCore.QRect(250, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어")
        font.setPointSize(20)
        self.calcul_button.setFont(font)
        self.calcul_button.setToolTipDuration(-1)
        self.calcul_button.setObjectName("calcul_button")

        #왼쪽의 화살표
        self.left = QtWidgets.QLabel(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(190, 200, 61, 41))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.left.setFont(font)
        self.left.setAlignment(QtCore.Qt.AlignCenter)
        self.left.setObjectName("left")

        #오른쪽의 화살표
        self.right = QtWidgets.QLabel(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(400, 200, 61, 41))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.right.setFont(font)
        self.right.setAlignment(QtCore.Qt.AlignCenter)
        self.right.setObjectName("right")

        #왼쪽 슬라이더 값 표시
        self.text_1 = QtWidgets.QLabel(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(70, 350, 101, 51))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.text_1.setFont(font)
        self.text_1.setAlignment(QtCore.Qt.AlignCenter)
        self.text_1.setObjectName("text_1")

        #오른쪽 슬라이더 값 표시
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(470, 350, 101, 51))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.text_2.setFont(font)
        self.text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.text_2.setObjectName("text_2")

        #중앙 슬랑디ㅓ 값 표시
        self.text_result = QtWidgets.QLabel(self.centralwidget)
        self.text_result.setGeometry(QtCore.QRect(260, 400, 121, 51))
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(20)
        self.text_result.setFont(font)
        self.text_result.setAlignment(QtCore.Qt.AlignCenter)
        self.text_result.setObjectName("text_result")

        #메뉴바
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        #상태바
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #이벤트
        self.retranslateUi(MainWindow)
        self.sl_1.valueChanged['int'].connect(self.text_1.setNum)
        self.sl_2.valueChanged['int'].connect(self.text_2.setNum)
        self.calcul_button.clicked.connect(lambda : self.calcul())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Slider Calculator"))
        self.calcul_button.setText(_translate("MainWindow", "Done!"))
        self.left.setText(_translate("MainWindow", "→"))
        self.right.setText(_translate("MainWindow", "←"))
        self.text_1.setText(_translate("MainWindow", "Value 1"))
        self.text_2.setText(_translate("MainWindow", "Value 2"))
        self.text_result.setText(_translate("MainWindow", "Result"))

    def calcul(self):
        first = int(self.text_1.text())
        second = int(self.text_2.text())
        self.text_result.setNum(first+second)
        self.sl_result.setValue(int(self.text_result.text()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

