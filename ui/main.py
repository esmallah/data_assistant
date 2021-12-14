import sys, sqlite3
from sqlite3 import Error
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from  Ui_Login import *
from Ui_Register import *
from Ui_Manage import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Login_Window()
        self.ui.setupUi(self)
        self.ui.btnRegis.clicked.connect(self.open_regis)
        self.ui.btnLogin.clicked.connect(self.check_login)
        self.ui.txtUser.setText('MENGX')
        self.ui.txtPass.setText('123')
        self.show

    def open_regis(self):
        self.a = Regis_Window()
        self.a.show()
        self.hide()

    def open_manage(self):
        self.a = Manage_Window()
        self.a.show()
        self.hide()


    def check_login(self):
        conn = sqlite3.connect('mydb.db')
        usr = self.ui.txtUser.text()
        pas = self.ui.txtPass.text()
        sql = "select * from User where usr='"+ usr +"' and pass='"+ pas +"'"
        cur = conn.cursor()
        result = cur.execute(sql)
        if(len(result.fetchall())>0):
            self.open_manage()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No Username or Password')
            msg.setWindowTitle('Error')
            msg.exec_()
        conn.close()

class Regis_Window(QMainWindow):
    def __init__(self):
        super(Regis_Window, self).__init__()
        self.ui = Register_Window()
        self.ui.setupUi(self)
        self.ui.btnRegis.setEnabled(False)
        self.ui.btnRegis.clicked.connect(self.regis)
        self.ui.txtUser.textChanged.connect(self.ckeck_bank_text)
        self.ui.txtEmail.textChanged.connect(self.ckeck_bank_text)
        self.ui.txtFname.textChanged.connect(self.ckeck_bank_text)
        self.ui.txtLname.textChanged.connect(self.ckeck_bank_text)
        self.ui.txtPass.textChanged.connect(self.ckeck_bank_text)
        self.ui.txtCpass.textChanged.connect(self.ckeck_pass)
        self.ui.txtUser.setFocusPolicy(Qt.StrongFocus)
        self.ui.btnCancel.clicked.connect(self.open_login)
        self.show()


    def open_login(self):
        self.a = MainWindow()
        self.a.show()
        self.hide()
        
    def ckeck_bank_text(self):
        usr = self.ui.txtUser.text()
        email = self.ui.txtEmail.text()
        fname = self.ui.txtFname.text()
        lname = self.ui.txtLname.text()
        pas = self.ui.txtPass.text()
        cpas = self.ui.txtCpass.text()
        if(usr == '' or email == '' or fname == '' or lname == '' or pas == '' or cpas == ''):
            self.ui.btnRegis.setEnabled(False)
        else:
            self.ui.btnRegis.setEnabled(True) 
    
    def ckeck_pass(self):
        if(self.ui.txtPass.text() == self.ui.txtCpass.text()):
            self.ui.txtCpass.setStyleSheet('background-color:#4cd137;color:#ffffff')
            self.ui.btnRegis.setEnabled(True)
        else:
            self.ui.txtCpass.setStyleSheet('background-color:red;color:#ffffff')
            self.ui.btnRegis.setEnabled(False)

    def regis(self):
        usr = self.ui.txtUser.text()
        email = self.ui.txtEmail.text()
        fname = self.ui.txtFname.text()
        lname = self.ui.txtLname.text()
        pas = self.ui.txtPass.text()
        cpas = self.ui.txtCpass.text()
        sql = "insert into User values('"+ usr +"','"+ email +"','"+ fname +"','"+ lname +"','"+ pas +"')"
        try:
            conn = sqlite3.connect('mydb.db')
            with conn:
                cur = conn.cursor()
                cur.execute(sql)
            print('Regis Compleate')
            self.open_login()
        except Error as e:
            print(e)
            msg = QMessageBox()
            msg.critical(
                self, 'Error',  "'%s'" % e,
                QMessageBox.Ok, 
                QMessageBox.Ok
            )
        finally:
            conn.close()



class Manage_Window(QMainWindow):
    def __init__(self):
        super(Manage_Window, self).__init__()
        self.ui = ManageUser_Window()
        self.ui.setupUi(self)
        self.ui.txtUser.setFocusPolicy(Qt.StrongFocus)
        self.ui.twgUser.cellClicked.connect(self.click)
        self.ui.btnCancel.clicked.connect(self.Load)
        self.ui.btnRemove.clicked.connect(lambda: self.Add_edit_remove("Remove"))
        self.ui.btnEdit.clicked.connect(lambda: self.call_btn(1))
        self.ui.btnAdd.clicked.connect(lambda: self.call_btn(2))
        self.ui.BtnSave.clicked.connect(self.call_Add_edit)
        self.showdata()
        self.show()


    def showdata(self):
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        sql = "SELECT * from User"
        cur.execute(sql)
        table = cur.fetchall()
        conn.close()
        rowno = 0
        self.ui.twgUser.setRowCount(len(table))
        for tuple in table:
            colno = 0
            for columns in tuple:
                onecolumn = QTableWidgetItem(columns)
                self.ui.twgUser.setItem(rowno, colno, onecolumn)
                colno +=1
            rowno += 1

    def click(self):
        row = self.ui.twgUser.currentRow()
        self.ui.txtUser.setText(self.ui.twgUser.item(row,0).text())
        self.ui.txtEmail.setText(self.ui.twgUser.item(row,1).text())
        self.ui.txtFname.setText(self.ui.twgUser.item(row,2).text())
        self.ui.txtLname.setText(self.ui.twgUser.item(row,3).text())
        self.ui.txtPass.setText(self.ui.twgUser.item(row,4).text())
        self.ui.btnEdit.setEnabled(True)
        self.ui.btnRemove.setEnabled(True)
        self.ui.btnAdd.setEnabled(False)
    
    def Load(self):
        self.ui.btnEdit.setEnabled(False)
        self.ui.btnRemove.setEnabled(False)
        self.ui.BtnSave.setEnabled(False)
        self.ui.btnAdd.setEnabled(True)
        self.ui.btnCancel.setEnabled(True)

        self.ui.txtPass.setEnabled(False)
        self.ui.txtUser.setEnabled(False)
        self.ui.txtEmail.setEnabled(False)
        self.ui.txtFname.setEnabled(False)
        self.ui.txtLname.setEnabled(False)

        self.ui.txtUser.setText('')
        self.ui.txtEmail.setText('')
        self.ui.txtFname.setText('')
        self.ui.txtLname.setText('')
        self.ui.txtPass.setText('')

    def Execute(self, sql, x):
        if x == 1:
            info = 'Add Complete'
        elif x == 2:
            info = 'Edit Complete'
        else:
            info = 'Remove Complete'
        try:
            conn = sqlite3.connect('mydb.db')
            with conn:
                cur = conn.cursor()
                cur.execute(sql)
            msg = QMessageBox()
            msg.information(
            self,'Info',"%s" % info,QMessageBox.Ok,QMessageBox.Ok
        )
        except Error as e:
            print(e)
            msg = QMessageBox()
            msg.critical(
                self, 'Error',  "%s" % e,
                QMessageBox.Ok, 
                QMessageBox.Ok
            )
        finally:
            conn.close()   
        self.showdata()
        self.Load()

    def call_btn(self, x):
        if x == 1:
            self.ui.txtUser.setEnabled(False)
        else:
            self.ui.txtUser.setEnabled(True)
            self.ui.btnAdd.setEnabled(False)
        self.ui.txtPass.setEnabled(True)
        self.ui.txtEmail.setEnabled(True)
        self.ui.txtFname.setEnabled(True)
        self.ui.txtLname.setEnabled(True)
        self.ui.BtnSave.setEnabled(True)
        self.ui.btnEdit.setEnabled(False)
        self.ui.btnRemove.setEnabled(False)

    def call_Add_edit(self):
        if self.ui.txtUser.isEnabled() :
           stat = 'Add'
        else:
             stat = 'Edit'
        self.Add_edit_remove(stat)
        
    def Add_edit_remove(self, x):
        usr = self.ui.txtUser.text()
        fname = self.ui.txtFname.text()
        lname = self.ui.txtLname.text()
        email = self.ui.txtEmail.text()
        pas = self.ui.txtPass.text()
        print(x)
        if x == "Edit":
            print('1')
            sql = " update User set email='"+ email +"', fname='"+ fname +"', lname='"+ lname +"', pass='"+ pas +"' where usr='"+ usr +"'"
            self.Execute(sql,2)
        elif x == "Add":
            sql = "insert into User values('"+ usr +"','"+ email +"','"+ fname +"','"+ lname +"','"+ pas +"')"
            self.Execute(sql,1)
            print('2')
        elif x == "Remove":
            sql = "DELETE FROM User WHERE usr='"+ self.ui.txtUser.text() +"'"
            self.Execute(sql,3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())