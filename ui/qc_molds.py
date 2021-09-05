from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QLineEdit,QPushButton,QDialog,QStyle,QSizePolicy,QVBoxLayout,QHBoxLayout
from PyQt5 import QtGui, QtCore,QtWidgets
from interface import Ui_MainWindow

from PyQt5.QtCore  import pyqtSlot,QSize

class Window2(QDialog):
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
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)
        
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.label1 )
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Login()
        self.cams.show()
        self.close()    
