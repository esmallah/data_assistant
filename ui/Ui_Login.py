# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mengx/Desktop/Final Project Test/Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Login_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 376)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(120, 260, 80, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet("QPushButton {\n"
"  border-radius:5px;\n"
"  background-color: white; \n"
"  color: #00cec9; \n"
"  border: 2px solid #00cec9;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background-color: #00cec9;\n"
"  color: white;\n"
"}")
        self.btnLogin.setObjectName("btnLogin")
        self.btnRegis = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegis.setGeometry(QtCore.QRect(120, 300, 80, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegis.setFont(font)
        self.btnRegis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegis.setStyleSheet("QPushButton {\n"
"  border-radius:5px;\n"
"  background-color: white; \n"
"  color: #00cec9; \n"
"  border: 2px solid #00cec9;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background-color: #00cec9;\n"
"  color: white;\n"
"}")
        self.btnRegis.setObjectName("btnRegis")
        self.txtUser = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUser.setGeometry(QtCore.QRect(80, 150, 171, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtUser.setFont(font)
        self.txtUser.setStyleSheet("border-radius:5px;\n"
"border: 2px solid #00b894;\n"
"background-color: #55efc4;")
        self.txtUser.setObjectName("txtUser")
        self.txtPass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPass.setGeometry(QtCore.QRect(80, 200, 171, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtPass.setFont(font)
        self.txtPass.setStyleSheet("border-radius:5px;\n"
"border: 2px solid #00b894;\n"
"background-color: #55efc4;")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#00b894;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.txtUser.setPlaceholderText('Enter Username')
        self.txtPass.setPlaceholderText('Enter Password')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.btnRegis.setText(_translate("MainWindow", "Register"))
        self.label.setText(_translate("MainWindow", "Login"))

