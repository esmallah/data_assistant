from config_pyqt.setting import *
from db import conn,cursor,Select_lists,Show_tables
class QC_reports(QFrame):

    def __init__(self, parent=None, db=None):
        super().__init__(parent)
        self.title = 'PyQt5 layout - pythonspot.com'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.layout = QVBoxLayout(self)

        self.hbox = QHBoxLayout()
        self.table_list = QComboBox(self)

        #self.db.text_factory = str
        
        self.result = '''
            SELECT
            table_schema || '.' || table_name
            FROM
                information_schema.tables
            WHERE
                table_type = 'BASE TABLE'
            AND
                table_schema NOT IN ('pg_catalog', 'information_schema');
                  
            '''
        cursor.execute(self.result)
        self.result=cursor.fetchall() 
        print("test",self.result)

        #if len(self.result)>0:
        self.table_names = sorted(list(zip(*self.result))[0])
         
        self.table_list.addItems(self.table_names)
        self.table_list.setCurrentText('yt_load_machine')
        self.hbox.addWidget(self.table_list)

        self.tableWidget = QTableWidget()
        self.setData()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        self.layout.addLayout(self.hbox)
        self.layout.addWidget(self.tableWidget)

        self.table_list.currentTextChanged.connect(self.select_list)

    def select_list(self):
        self.tableWidget.clear()
        if cursor:
            self.setData()
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

    def setData(self):
        self.current_table = self.table_list.currentText()
        view_query = """select * from {}""".format(self.current_table)
        cursor.execute(view_query)
        view=cursor.fetchall()

        col_name_query = """select name FROM PRAGMA table_info('{}')""".format(self.current_table)

        cursor.execute(col_name_query)
        col_name=cursor.fetchall()
        self.current_data = {}
        header = []
        for c in col_name:
            header.append(c[0])
            self.current_data[c[0]] = []
        row_cnt = 0
        for d in view:
            row_cnt += 1
            for i in range(len(self.current_data.keys())):
                self.current_data[list(self.current_data.keys())[i]].append(d[i])

        self.tableWidget.setRowCount(row_cnt)
        self.tableWidget.setColumnCount(len(self.current_data))

        for n in range(len(header)):
            for m in range(row_cnt):
                item = self.current_data[header[n]][m]
                self.tableWidget.setItem(m, n, QTableWidgetItem(str(item)))
        self.tableWidget.setHorizontalHeaderLabels(header)

    def connectDB(self, db):
        cursor = db
        self.select_list()
