from config_pyqt.setting import *
from .admin_window import AppWindow
class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "App"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.buttonWindow1 = QPushButton('Control Panel', self)
        self.buttonWindow1.move(100, 100)
        self.buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        self.lineEdit1 = QLineEdit("admin page [Window1].", self)
        self.lineEdit1.setGeometry(250, 100, 400, 30)

        self.buttonWindow2 = QPushButton('database Screen', self)
        self.buttonWindow2.move(100, 200)
        self.buttonWindow2.clicked.connect(self.buttonWindow2_onClick)        
        self.lineEdit2 = QLineEdit("admin page for control the database [Window2].", self)
        self.lineEdit2.setGeometry(250, 200, 400, 30)

        self.buttonWindow3 = QPushButton('QC Screen', self)
        self.buttonWindow3.move(100, 200)
        self.buttonWindow3.clicked.connect(self.buttonWindow3_onClick)        
        self.lineEdit3 = QLineEdit("user page for data entry and get reports [Window3].", self)
        self.lineEdit3.setGeometry(250, 200, 400, 30)


        self.combo = QtWidgets.QComboBox(self)
        self.combo.currentIndexChanged.connect(self.change_func)
        self.trans = QtCore.QTranslator(self)

        self.v_layout = QtWidgets.QVBoxLayout(self)
        self.v_layout.addWidget(self.combo)
        
        options = ([('English', ''), ('عربي', 'eng-ar' ),])
        
        for i, (text, lang) in enumerate(options):
            self.combo.addItem(text)
            self.combo.setItemData(i, lang)
        self.retranslateUi()

        self.show()


    @pyqtSlot()
    def buttonWindow1_onClick(self):
        
        self.cams = AppWindow() 
        self.cams.show()
        self.close()
        
    @pyqtSlot()
    def buttonWindow2_onClick(self):
        from ui import SqliteWindow
        self.cams = SqliteWindow(self.lineEdit2.text()) 
        self.cams.show()
        self.close()
        
    @pyqtSlot()
    def buttonWindow3_onClick(self):
        from ui import Window_qc
        self.cams = Window_qc(self.lineEdit2.text()) 
        self.cams.show()
        self.close()
    #______________________translation
    @QtCore.pyqtSlot(int)
    def change_func(self, index):
        data = self.combo.itemData(index)
        if data:
            self.trans.load(data)
            QtWidgets.QApplication.instance().installTranslator(self.trans)
        else:
            QtWidgets.QApplication.instance().removeTranslator(self.trans)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi()
        super(Login, self).changeEvent(event)

    def retranslateUi(self):
        self.buttonWindow1.setText(QtWidgets.QApplication.translate('Login', 'Control Panel'))
        self.lineEdit1.setText(QtWidgets.QApplication.translate('Login', 'admin page [Window1]'))
        self.buttonWindow3.setText(QtWidgets.QApplication.translate('Login', 'QC Screen'))
        self.lineEdit3.setText(QtWidgets.QApplication.translate('daily report', 'user page for data entry and get reports [Window2].'))
