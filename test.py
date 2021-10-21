# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delivery.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
conn = sqlite3.connect("spmanager.db")
cursor = conn.cursor()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(773, 621)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 20, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 210, 701, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(40, 550, 331, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 91, 17))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 19, 291, 61))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 70, 691, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(70, 20, 151, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(80, 30, 171, 25))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        #list1 = ['First Item','Second Item','Third Item']
        #self.comboBox.addItems(list1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(540, 540, 181, 81))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_2.setGeometry(QtCore.QRect(5, 20, 141, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(8, 50, 131, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        def customer_names(self):
            self.conn = conn
            self.cursor = cursor
            self.cursor.execute("SELECT  customer_name FROM customers ORDER BY customer_name")
            self.sql =cursor.fetchall()
        customer_names(self)
        self.names =[]
        for i in self.sql:
            self.names.append(i[0])
        self.comboBox.addItems(self.names)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HI-SPECS INNOVATIVE DELIVERY NOTE"))
        self.label.setText(_translate("Form", "DELIVERY NOTE"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Qnty"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Item"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Description"))
        self.label_4.setText(_translate("Form", "Comment"))
        self.label_3.setText(_translate("Form", "Date:"))
        self.label_2.setText(_translate("Form", "Name:"))
        self.comboBox.setItemText(0, _translate("Form", "customer"))
        self.comboBox_2.setItemText(0, _translate("Form", "Print & Record"))
        self.comboBox_2.setItemText(1, _translate("Form", "Print"))
        self.comboBox_2.setItemText(2, _translate("Form", "Record"))
        self.comboBox_2.setItemText(3, _translate("Form", "Email"))
        self.pushButton.setText(_translate("Form", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
