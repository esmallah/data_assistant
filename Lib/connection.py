#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtSql
from PyQt5.QtWidgets import (QMainWindow, QTableView, QApplication, QAbstractItemView)
from PyQt5.QtCore import Qt
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 150)

        self.createConnection()
        self.fillTable()
        self.createModel()
        self.initUI()

    def createConnection(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("region.db")
        if not self.db.open():
            print("Cannot establish a database connection")
            return False

    def fillTable(self):
        self.db.transaction()
        q = QtSql.QSqlQuery()
        q.exec_("DROP TABLE IF EXISTS regions;")
        q.exec_("CREATE TABLE regions (regionId INT PRIMARY KEY, region TEXT);")
        q.exec_("INSERT INTO regions VALUES (1, 'Bristol');")
        q.exec_("INSERT INTO regions VALUES (2, 'Scotland' );")
        q.exec_("INSERT INTO regions VALUES (2, 'Boumemoth' );")
        
        q.exec_("DROP TABLE IF EXISTS agent;")
        q.exec_("CREATE TABLE agent (name TEXT, address TEXT, phone INT,region INT );")
        q.exec_("INSERT INTO agent VALUES ('Tylor William', '106 Uxbridge Street Burton-on-Trent Staffordshire', 440989576410,1);")
        q.exec_("INSERT INTO agent VALUES ('Mac Flats', '106 Uxbridge Street Burton-on-Trent Staffordshire', 440989576410,2);")
        q.exec_("INSERT INTO agent VALUES ('Jameson & mackay', '106 Uxbridge Street Burton-on-Trent Staffordshire', 440989576410,2);")
        q.exec_("INSERT INTO agent VALUES ('Nicol Estate', '106 Uxbridge Street Burton-on-Trent Staffordshire', 440989576410,1);")
        q.exec_("INSERT INTO agent VALUES ('Tylor William', '106 Uxbridge Street Burton-on-Trent Staffordshire', 440989576410,3);")
        self.db.commit()

    def createModel(self):
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable("agent")

        self.model.setHeaderData(0, Qt.Horizontal, "name")
        self.model.setHeaderData(1, Qt.Horizontal, "address")
        self.model.setHeaderData(2, Qt.Horizontal, "phone")
        self.model.setHeaderData(2, Qt.Horizontal, "region")
        self.model.setRelation(2, QtSql.QSqlRelation("regions", "regionId", "region"))

        self.model.select()


    def initUI(self):
        self.view = QTableView()
        self.view.setModel(self.model)

        mode = QAbstractItemView.SingleSelection
        self.view.setSelectionMode(mode)

        self.setCentralWidget(self.view) 

    def closeEvent(self, e):
        if (self.db.open()):
            self.db.close()

def main():
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()