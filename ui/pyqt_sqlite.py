#!/usr/bin/python3

# This software is distributed under the GNU Lesser General Public License (https://www.gnu.org/licenses/lgpl-3.0.en.html)
# WARNING: This is not a software to be used in production. I write this software for teaching purposes.  
# TO DO: There lots of things to be done. This is experimental software and will never finish. But I will do the followings first:
# 1) Save SQL Query as view - done 2017/04/11
# 2) Modify Table is not implemented. Will implement whenever I find time
# 3) Editing SQLite parameters
# 4) Creating Index
# 5) SQL syntax highlight
# 6) Currently all changes done on database. Write Changes, Revert Changes
# 7) ….
# 8) Those features queried by users

import sys
import os

from PyQt5 import QtWidgets, QtCore, QtGui, Qt, QtSql, uic

from apps.pyqt_sqlite.ui import ModifyTableDialog,TYPE_DICT,addUi

from functools import partial
ui_path = os.path.dirname(os.path.abspath(__file__))
mainwindowUi = uic.loadUiType(os.path.join(ui_path, "mainwindow.ui"))[0]

#mainwindowUi = uic.loadUiType("main_window.ui")[0]

app = QtWidgets.QApplication(sys.argv)

__appname__='PyQt SqLite Database Browser'
class SqliteWindow(QtWidgets.QMainWindow, mainwindowUi):
    selectedTable=None
    work_directory=os.path.dirname(os.path.realpath(__file__))
    current_database_file=''
    current_database=None   
    
    def __init__(self, *args):
        super(SqliteWindow, self).__init__(*args)
        
        QtCore.QCoreApplication.setOrganizationName("mbaser")
        QtCore.QCoreApplication.setOrganizationDomain("foo.org")
        QtCore.QCoreApplication.setApplicationVersion("0.0.1")
        self.current_database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.setupUi(self)
        self.tree_model=QtGui.QStandardItemModel()
        
        self.treeView.setModel(self.tree_model)
        self.settings=QtCore.QSettings()
        
        self.recent_files=self.settings.value('recent_files',[])
        self.update_recent_files()
        
    
    def setTitle(self, title=None):
        t_str="PyQt SqLite"
        if title:
            t_str += ' [%s]' % title
        self.setWindowTitle(t_str)
    
    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        QtWidgets.QMessageBox.about(self, "About this software","This software is written for teaching purposes. Don't use in production!!! My purpose is to demonstrate how PyQt widgets can be used to develop software.\n\n Main developer: Mustafa Baser <mbaser@mail.com>")
    
    @QtCore.pyqtSlot()
    def on_commandLinkButton_clicked(self):
        dialog=ModifyTableDialog(self)
        dialog.exec_()

    @QtCore.pyqtSlot()
    def on_commandLinkButton_3_clicked(self):
        if self.selectedTable:
            result=QtWidgets.QMessageBox.question(self, "Warning",
                                                     "You are just deleting %s %s. You will lost all the data in %s. Dou you want to delete?" % (
                                                     self.selectedTable[1],
                                                     self.selectedTable[0],
                                                     self.selectedTable[0]
                                                   ))
        if result==QtWidgets.QMessageBox.Yes:
            self.current_database.exec("DROP %s `%s`" % (self.selectedTable[0], self.selectedTable[1]))
            if not self.error_check(self.current_database):
                self.update_tables_table()
        
    @QtCore.pyqtSlot('QModelIndex', int)
    def on_treeView_expanded(self, ind):
        pass

        
    @QtCore.pyqtSlot('QModelIndex')
    def on_treeView_clicked(self, ind):   

        item=self.tree_model.itemFromIndex(ind.sibling(0,0))
        
        if hasattr(item,"tableType"):
            self.selectedTable=(item.tableType,ind.sibling(ind.row(),0).data())
            self.commandLinkButton_2.setEnabled(True)
            self.commandLinkButton_3.setEnabled(True)
        else:
            self.commandLinkButton_2.setEnabled(False)
            self.commandLinkButton_3.setEnabled(False)

        
    def update_tables_table(self):
        self.tree_model.clear()
        self.tree_model.setHorizontalHeaderLabels(['Name', 'Type','Schema'])
        for typ in ('table','view'):
            q=self.current_database.exec("SELECT name FROM sqlite_master WHERE type = '%s'" % typ)
            self.error_check(self.current_database)
            tables=[]
            while q.next():
                tables.append(q.value(0))
            
            tab_par = QtGui.QStandardItem('%ss (%d)' % (typ.title(),len(tables)))
            
            for tb in tables:
                if typ=='table': c_icon="sc_inserttable.png"
                else: c_icon="sc_dbviewtablenames.png"
                self.comboBox.addItem(QtGui.QIcon("icons/"+c_icon), tb)
                tb_name=QtGui.QStandardItem(tb)
                tb_name.tableType=typ
                tb_type=QtGui.QStandardItem(typ.title())
                q=self.current_database.exec("SELECT sql FROM sqlite_master WHERE tbl_name = '%s' AND type = '%s'" % (tb,typ))
                tb_schema_str=''
                if q.next():
                    tb_schema_str=q.value(0)
                    tb_schema_str=tb_schema_str.replace("\n", " ")
                    tb_schema_str=tb_schema_str.replace("\t", " ")
               
                tb_schema=QtGui.QStandardItem(tb_schema_str)
                
                driver=self.current_database.driver()
                rec=driver.record(tb)
                for i in range(rec.count()):
                    col_name=QtGui.QStandardItem(rec.field(i).name())
                    type_id=rec.field(i).type()
                    if type_id in TYPE_DICT: type_str=TYPE_DICT[type_id]
                    else: type_str=str(type_id)
                    col_type=QtGui.QStandardItem(type_str)
                
                    tb_name.appendRow([col_name, col_type])
                    
                tab_par.appendRow([tb_name, tb_type, tb_schema])
                
            self.tree_model.appendRow(tab_par)
            

    def error_check(self, model):
        
        error = model.lastError()
        if error.isValid():
            self.show_warning(error.text())
            return True
            
        
    
    @QtCore.pyqtSlot()    
    def on_queryExecButton_pressed(self):
        self.queryTableView.setModel(QtSql.QSqlQueryModel())
        query = self.queryTextEdit.toPlainText()
        model = self.queryTableView.model()
        model.setQuery(query)
        self.error_check(model)

        
        
    @QtCore.pyqtSlot(str)    
    def on_comboBox_currentIndexChanged(self,tbl_name):
        if tbl_name:
            model = QtSql.QSqlTableModel()
            model.setTable('"'+tbl_name+'"')
            model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            model.select()

            self.error_check(model)
            self.tableView.setModel(model)

    def show_warning(self, text):
        QtWidgets.QMessageBox.warning(self, "Info", "Could not execute query. Error message from database engine is:\n"+ text)
    
    
    @QtCore.pyqtSlot()    
    def on_newRecordButton_pressed(self):
        model = self.tableView.model()
        model.submitAll()
        result=model.insertRows(model.rowCount(), 1)
        if not result:
            self.error_check(model)
        
    @QtCore.pyqtSlot()    
    def on_reloadTableButton_pressed(self):
        self.tableView.model().select()

    @QtCore.pyqtSlot()    
    def on_deleteRecordButton_pressed(self):
        model = self.tableView.model()
        model.removeRow(self.tableView.currentIndex().row())
        model.select()

    @QtCore.pyqtSlot()
    def on_actionClose_triggered(self):
        self.closeDatabase()

    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()
        
        
    @QtCore.pyqtSlot()
    def on_actionNew_triggered(self):
        save_file_dialog=QtWidgets.QFileDialog.getSaveFileName(self, "Name of new database", self.work_directory)
        if save_file_dialog[0]:
            self.loadDatabase(save_file_dialog[0])


    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        self.fileDialog = QtWidgets.QFileDialog(self)
        self.fileDialog.setDirectory(self.work_directory)
        
        result=self.fileDialog.getOpenFileName()
       
        if result[0]:
            self.loadDatabase(result[0])
    
    @QtCore.pyqtSlot()
    def on_saveQueryAsView_pressed(self):
        
        model = self.queryTableView.model()
        
        if model:
            if model.rowCount():
                view_name, result = QtWidgets.QInputDialog.getText(self, __appname__, 'Enter vieww name:')
                if result:
                    query = self.queryTextEdit.toPlainText()            
                    query = 'CREATE VIEW {0} AS\n{1}'.format(view_name, query)
                    if not self.execute_query(query):
                        self.update_tables_table()
        
    def closeDatabase(self):
        if self.current_database:
            if self.current_database.isOpen():
                self.tree_model.clear()
                self.comboBox.clear()
                tbm=self.tableView.model()
                tbm.clear()
                
                self.current_database.close()
                self.setTitle()
                self.commandLinkButton.setEnabled(False)
                self.actionClose.setEnabled(False)
            print('Clearing "Execute SQL Widgets"')
            #clear "Execute SQL Widgets"
            self.queryTextEdit.clear()
            tableModel=self.queryTableView.model()
            if tableModel:
                tableModel.clear()
            
            self.queryTableView.setModel(None)
            self.queryResultText.clear() 

    def loadDatabase(self, db_file, *args):
        self.closeDatabase()
        self.tree_model.removeRows(0, self.tree_model.rowCount())
        self.work_directory=os.path.dirname(db_file)
        self.current_database_file=os.path.basename(db_file)
        self.current_database.setDatabaseName(db_file)
        if self.current_database.open():
            self.commandLinkButton.setEnabled(True)
            self.actionClose.setEnabled(True)
            self.setTitle(db_file)
            self.update_tables_table()
            
            if db_file in self.recent_files:
                self.recent_files.remove(db_file)
                
            self.recent_files.insert(0,db_file)
            self.update_recent_files()

            
    def update_recent_files(self):
        self.menuOpen_Recent.clear()
        for i, rc in enumerate(self.recent_files):
            recent_file_action=QtWidgets.QAction('&%d %s' % (i+1, rc), self, triggered=partial(self.loadDatabase, rc))
            self.menuOpen_Recent.addAction(recent_file_action)

    def execute_query(self, query):
        self.current_database.exec(query)

        return self.error_check(self.current_database)

    def closeEvent(self, event):
        
        self.settings.setValue('recent_files', self.recent_files)
        self.closeDatabase()

main = SqliteWindow()
main.show()
sys.exit(app.exec_())
