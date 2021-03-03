import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        hlay = QHBoxLayout(self)
        self.treeview = QTreeView()
        self.listview = QListView()
        hlay.addWidget(self.treeview)
        hlay.addWidget(self.listview)

        path = QDir.rootPath()

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.listview.setModel(self.fileModel)

        self.treeview.setRootIndex(self.dirModel.index(path))
        self.listview.setRootIndex(self.fileModel.index(path))

        self.treeview.clicked.connect(self.on_clicked)

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.fileModel.setRootPath(path))


class Model:
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None
        self.fileContent = ""

    def isValid( self, fileName ):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False

    def setFileName( self, fileName ):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        if self.isValid( fileName ):
            self.fileName = fileName
            self.fileContents = open( fileName, 'r' ).read()
        else:
            self.fileContents = ""
            self.fileName = ""
            
    def getFileName( self ):
        '''
        Returns the name of the file name member.
        '''
        return self.fileName

    def getFileContents( self ):
        '''
        Returns the contents of the file if it exists, otherwise
        returns an empty string.
        '''
        return self.fileContents
    
    def writeDoc( self, text ):
        '''
        Writes the string that is passed as argument to a
        a text file with name equal to the name of the file
        that was read, plus the suffix ".bak"
        '''
        if self.isValid( self.fileName ):
            fileName = self.fileName + ".bak"
            file = open( fileName, 'w' )
            file.write( text )
            file.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())