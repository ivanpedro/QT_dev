
import sys

from limpiar import Ui_Dialog
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class MiFormulario(QDialog):
#    def __init__(self): 
#        super(MiFormulario, self).__init__()

#    def __init__(self, parent=None):
#        super(MiFormulario, self).__init__(parent)
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUi(self):
        
        # Set up the user interface from Designer.
        ui = Ui_Dialog()
        ui.setupUi(self)

if __name__== "__main__":
    app = QtGui.QGuiApplication(sys.argv)
    myapp = MiFormulario()

    
    myapp.show()
    sys.exit(app.exec_())

#import sys
#from PyQt5.QtWidgets import QApplication, QDialog
#from limpiar import *
#
#
#if __name__== "__main__":
#    app = QApplication(sys.argv)
#    window = QDialog()
#    ui = Ui_Dialog()
#    ui.setupUi(window)
#    
#    window.show()
#    sys.exit(app.exec_())