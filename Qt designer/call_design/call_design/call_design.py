
    
import sys
from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5 import QtCore,  QtWidgets, QtGui
from limpiar import *

class Window(QDialog):
   def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        
#    def __init__(self):
#        super(Window, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.show()

   
if __name__== "__main__":

        

    app = QApplication(sys.argv)
    GUI = Window()
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