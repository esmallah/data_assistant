
from PyQt5 import QtGui, QtCore,QtWidgets
#from main import Ui_MainWindow,Login
from PyQt5.QtWidgets import (
    QFileDialog,
    QFrame,
    QTabWidget,
    QVBoxLayout,
    QMessageBox,
    QLabel,QPushButton,QDialog,QStyle,QSizePolicy,
    QVBoxLayout,QHBoxLayout,QComboBox,QLabel
)
from memory import Select_lists
from PyQt5.QtCore  import pyqtSlot,QSize
from memory import conn,cursor
class Window_qc(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QC Molds')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.label1 = QLabel(value)

        #dimention
        self.top = 50
        self.left = 100
        self.width = 1200
        self.height = 600
        self.InitUI()
    def InitUI(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))
        
        layoutV = QVBoxLayout()
        
        #push buttons for enter data
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        #add combo box
        self.combo = QComboBox(self)
        self.combo = QComboBox(self)

        self.combo.move(50, 50)
        self.qlabel = QLabel(self)
        self.qlabel.move(50,16)
        
        self.combo.addItems(Select_lists.get_lest())

        self.combo.activated[str].connect(self.onChanged)
        layoutV.addWidget(self.combo)

        layoutH = QHBoxLayout()
        layoutH.addWidget(self.label1 )
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)
        
    def pm_Combo(self):
        
        #self.sql=cursor.fetchall()
        #conn.commit()
        print("_____________test",Select_lists.get_lest())

         #=cursor.fetchall()
        #self.names =[]
        #for i in self.sql:
        #    self.names.append(i[0])
        #conn.close()

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()

    def goMainWindow(self):
        self.cams = Login()
        self.cams.show()
        self.close()    
