from config.setting import *
from .qc import *

from config.memory import conn,cursor,Select_lists,Show_tables
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

        self.layout = QVBoxLayout(self)               
        #self.layout = QVBoxLayout(self)
        #layoutV = QVBoxLayout()
               
        #____________tabs
        self.reports=QC_reports(self)
        self.Load_machines=Load_machines(self)
        self.PartsDataEntry=PartsDataEntry()        
        self.tabs = QTabWidget()
        
        self.tabs.addTab(self.Load_machines,'machine load')
        self.tabs.addTab(self.PartsDataEntry,'daily report')
        self.tabs.addTab(self.reports,'reports')
        self.tabs.setCurrentWidget(self.Load_machines)

        self.tabs.setTabPosition(QTabWidget.South)
        self.layout.addWidget(self.tabs)
        #self.setLayout(self.layout)

        #____________add combo box
        
        #self.setLayout(layoutV)
        
    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()

    def goMainWindow(self):
        self.cams = Login()
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
        super(Window_qc, self).changeEvent(event)

    def retranslateUi(self):
        self.Load_machines.setText(QtWidgets.QApplication.translate('machine load', 'user page for data entry and get reports [Window2].'))
        self.PartsDataEntry.setText(QtWidgets.QApplication.translate('daily report', 'user page for data entry and get reports [Window2].'))
        self.reports.setText(QtWidgets.QApplication.translate('reports', 'user page for data entry and get reports [Window2].'))
