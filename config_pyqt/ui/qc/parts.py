from config_pyqt.setting import *

class PartsDataEntry(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(PartsDataEntry, self).__init__()
        self.createFormGroupBox()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.formGroupBoxCt)

        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("dailty report")
        
    def createFormGroupBox(self):
            self.formGroupBox = QGroupBox("the weigt")
            

            layoutFormW = QFormLayout()
            layoutFormW.addRow(QLabel("weight1:"), QLineEdit())
            layoutFormW.addRow(QLabel("weight2:"), QLineEdit())

            layoutFormW.addRow(QLabel("Country:"), QComboBox())
            layoutFormW.addRow(QLabel("Age:"), QSpinBox())

            self.formGroupBoxCt = QGroupBox("the ct")            
            layoutCt = QFormLayout()
            layoutCt.addRow(QLabel("weight1:"), QLineEdit())
            layoutCt.addRow(QLabel("weight2:"), QLineEdit())

            layoutCt.addRow(QLabel("Country:"), QComboBox())
            layoutCt.addRow(QLabel("Age:"), QSpinBox())
            self.formGroupBox.setLayout(layoutFormW)

            self.formGroupBoxCt.setLayout(layoutCt)
