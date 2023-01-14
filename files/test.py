import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.label = QLabel("",self)
        self.label.move(100, 100)

        self.button = QPushButton('click', self)
        self.button.move(100, 50)
        self.button.clicked.connect(self.on_click)

        self.setGeometry(500, 150, 200, 200)
        self.show()    

    def on_click(self):
        self.label.setText("Hello")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.on_click()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())