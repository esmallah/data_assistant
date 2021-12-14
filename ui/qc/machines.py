from setting import *
from memory import conn,cursor,Select_lists,Show_tables
from .parts import PartsDataEntry
class Load_machines (QFrame):

    def __init__(self, parent=None, db=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.hbox = QHBoxLayout()
        self.table_list = QComboBox(self)
        #______add button        
        button_dailyReport = QPushButton('enter daily report', self)
        button_dailyReport.setToolTip('This is an example button')
        button_dailyReport.move(100,70)
        button_dailyReport.clicked.connect(self.insert_item)
        self.layout.addWidget(button_dailyReport)
    #___________date picker
        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        #self.menuBar().setCornerWidget(self.dateedit, QtCore.Qt.TopLeftCorner)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.layout.addWidget(self.dateedit)
    #___________add data entry
        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.layout.addLayout(windowLayout)

        button_daily_save = QPushButton('submit', self)
        button_daily_save.setToolTip('for save data')
        button_daily_save.move(100,70)
        button_daily_save.clicked.connect(self.insert_item)

        self.layout.addWidget(button_daily_save)
        self.setLayout(self.layout)
        
        self.show()
    
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(6, 3)
        #layout.setColumnStretch(6, 3)
        list_strucure=['shift1_1','shift1_2','shift1_3','shift1_4','shift1_5','shift1_6',]
        for i in list_strucure:
            for l in range(len(list_strucure)):
                layout.addWidget(QLabel(i),l,0)

#        for i in range(20):
        for b in range(15):
            for l in range(15):
                layout.addWidget(QLineEdit(),b,l)        
        self.horizontalGroupBox.setLayout(layout)
    def insert_item(self):
        item=Select_lists.get_lest_items()
        #self.combo_item.activated[str].connect()
        #layoutV.addWidget(self.combo)
        #self.layout.addWidget(self.combo_item)
        machines=Select_lists.get_lest_machines()
        #machines, okPressed = QInputDialog.getItem(self, "Get item","Color:", machines, 0, False)
        item, okPressed = QInputDialog.getItem(self, "Get machine","number:", item, 0, False)

        if okPressed and item:
            print(item)
        if okPressed and machines:
            print (machines)

    def refreshCB(self):
        self.combo3.clear()
        self.combo4.clear()
        self.combo5.clear()
        self.combo6.clear()
