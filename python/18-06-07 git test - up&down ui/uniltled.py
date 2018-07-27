# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import random, time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #창 제목, 크기
        MainWindow.setObjectName("Up&Down Game")
        MainWindow.setMinimumSize(QtCore.QSize(420, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))

        #메인 위젯, 레이아웃 생성
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(2, 2, 410, 110))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #메인텍스트
        self.main_text = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(28)
        self.main_text.setFont(font)
        self.main_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_text.setAlignment(QtCore.Qt.AlignCenter)
        self.main_text.setObjectName("main_text")
        self.verticalLayout_2.addWidget(self.main_text)

        #보조텍스트
        self.help_text = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(12)
        self.help_text.setFont(font)
        self.help_text.setAlignment(QtCore.Qt.AlignCenter)
        self.help_text.setObjectName("help_text")
        self.verticalLayout_2.addWidget(self.help_text)

        #아래 레이아웃
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 270, 400, 80))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        #오른쪽 숫자
        self.up_num = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(18)
        self.up_num.setFont(font)
        self.up_num.setAlignment(QtCore.Qt.AlignCenter)
        self.up_num.setObjectName("up_num")
        self.horizontalLayout_3.addWidget(self.up_num)
        self.up_num.hide()

        #<
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label.hide()

        #정답 숫자
        self.answer = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(28)
        self.answer.setFont(font)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")
        self.horizontalLayout_3.addWidget(self.answer)
        self.answer.hide()

        #<
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_2.hide()

        #왼쪽 숫자
        self.down_num = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(18)
        self.down_num.setFont(font)
        self.down_num.setAlignment(QtCore.Qt.AlignCenter)
        self.down_num.setObjectName("down_num")
        self.horizontalLayout_3.addWidget(self.down_num)
        self.down_num.hide()

        #레이아웃
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 130, 400, 100))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        #텍스트 에디터
        self.input_text = QtWidgets.QTextEdit(self.widget2)
        self.input_text.setObjectName("input_text")
        self.verticalLayout_4.addWidget(self.input_text)
        self.input_text.hide()

        #버튼
        self.ok_button = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setFamily("210 Gulim")
        font.setPointSize(16)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        self.verticalLayout_4.addWidget(self.ok_button)

        #메뉴바,상태창 등등
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #글자 변경, 시그널
        self.retranslateUi(MainWindow)
        self.ok_button.clicked.connect(self.change)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #파츠별 글자
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_text.setText(_translate("MainWindow", "Up&Down Game"))
        self.help_text.setText(_translate("MainWindow", "press start"))
        self.up_num.setText(_translate("MainWindow", "?"))
        self.label.setText(_translate("MainWindow", "<"))
        self.answer.setText(_translate("MainWindow", "?"))
        self.label_2.setText(_translate("MainWindow", "<"))
        self.down_num.setText(_translate("MainWindow", "?"))
        self.ok_button.setText(_translate("MainWindow", "start "))

    #시작버튼 클릭후 ui 전환
    def change(self):

        self.input_text.show()
        self.down_num.show()
        self.label.show()
        self.label_2.show()
        self.answer.show()
        self.up_num.show()
        self.main_text.setText("")
        self.ok_button.setText("OK")
        self.help_text.setText("1~99 사이의 숫자를 맞추는 게임입니다.\n숫자를 입력하고 ok버튼을 누르세요.\n기회는 7번입니다.")

        #기초 변수 설정
        end_stat = False
        count = 7
        com_num = str(random.randrange(1,100))
        usr_num = self.input_text.toPlainText() 

        self.ok_button.clicked.connect(lambda : self.game_start(end_stat, count, usr_num, com_num)) 
        print(count, com_num, usr_num)

    def game_start(self, end_stat, count, usr_num, com_num):

        self.input_text.clear()

        if usr_num > com_num:
            count += -1
            self.main_text.setText("Down!")
            self.help_text.setText("남은기회 %s번"%count)
            self.up_num.setText("%s"%usr_num)

        elif usr_num < com_num:
            count += -1
            self.main_text.setText("Up!")
            self.help_text.setText("남은기회 %s번"%count)
            self.down_num.setText("%s"%usr_num)

        elif usr_num == com_num:
            end_stat = True
            count += -1

        #성공시 end_stat True 상태
        if end_stat == True:
            self.main_text.setText("Congratulations!")
            self.help_text.setText("정답은 %s이었습니다.\n%s번만에 맞추셨습니다."%(com_num, 7 - count))
            self.answer.setText("%s"%usr_num)
            count = 7 #아래의 if문 무시를 위함
        
        #기회 모두 소모시 count = 0
        if count <= 0:
            self.main_text.setText("YOU FILED...")
            self.help_text.setText("정답은 %s이었습니다."%com_num)
            self.answer.setText("%s"%com_num)
        
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

