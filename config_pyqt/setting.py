import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import PyQt6

from PyQt6.QtCore  import pyqtSlot,QSize
import sys
import time

from PyQt6 import QtGui, QtCore,QtWidgets
from PyQt6.QtCore  import pyqtSlot,QSize,Qt

#from main import Ui_MainWindow,Login
from PyQt6.QtWidgets import (
    QFileDialog,
    QFrame,
    QTabWidget,
    QInputDialog,
    QMessageBox,
    QLabel,QPushButton,QDialog,QStyle,QSizePolicy,
    QVBoxLayout,QHBoxLayout,QComboBox,QGridLayout,
    QApplication, QMainWindow,QLineEdit,QDialogButtonBox, QFormLayout,QGroupBox,
    QMenu, QMenuBar, QSpinBox, QTextEdit,QTableWidget,QTableWidgetItem
)


