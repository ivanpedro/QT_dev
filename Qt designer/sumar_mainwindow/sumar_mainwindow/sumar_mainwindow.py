
import sys
from PyQt5.Qt import pyqtSignal

from PyQt5.QtGui import QIcon
from sumar import *
from PyQt5.QtWidgets import (QMainWindow, QApplication, QMenu,
                             QAction, QPushButton, QMessageBox,
                             QWidget)
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QCoreApplication

#class ventana(QMainWindow):
#    def __init__(self):
#        super().__init__()

#        self.initUI()
#        self.show()

#    def initUI(self):

#        self.ui = Ui_MainWindow()
#        self.ui.setupUi(self)
#        self.ui.pbtn_sumar.clicked.connect(self.mostrarsum)

#    def mostrarsum(self):
#        if len(self.ui.lineEdit_in_num1.text()) !=0:
#            a = int (self.ui.lineEdit_in_num1.text())

#        else:
#            a =0
#        if len(self.ui.lineEdit_in_num2.text()) !=0:
#            b = int(self.ui.lineEdit_in_num2.text())

#        else:
#            b =0

#        sum= a+b
#        self.ui.lineEdit_in_num3.setText( str(sum))
       

class ventana(QMainWindow):
    def __init__(self, parent=None):
        super(ventana, self).__init__(parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pbtn_sumar.clicked.connect(self.mostrarsum)
        
        self.show()

    def mostrarsum(self):
        if len(self.ui.lineEdit_in_num1.text()) !=0:
            a = int (self.ui.lineEdit_in_num1.text())

        else:
            a =0
        if len(self.ui.lineEdit_in_num2.text()) !=0:
            b = int(self.ui.lineEdit_in_num2.text())

        else:
            b =0

        sum= a+b
        self.ui.lineEdit_in_num3.setText( str(sum))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = ventana()
    sys.exit(app.exec_())