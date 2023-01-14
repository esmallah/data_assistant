
from PyQt5.QtWidgets import QApplication

import sys

from config.ui.login import Login #for developing mode only

def main():
    app = QApplication(sys.argv)
    #ex = AppWindow()    
    ex = Login()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()