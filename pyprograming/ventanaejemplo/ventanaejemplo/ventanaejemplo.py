import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QAction, QPushButton, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QMetaObject

class ventanaejemplo(QWidget):
    def __init__(self, parent= None):
        QWidget.__init__(self, parent)

        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Ventana de ejemplo')
        quit = QPushButton('Cerrar', self)
        quit.setGeometry(10,10,70,40)
        #senal = 'clicked()' -> self.connect() -> slot='quit()'
        self.connect(quit, pyqtSignal('clicked()'), QGuiApplication, ptqtSlot('quit()'))
        #QMetaObject.connectSlotsByName(quit, QtCore.pyqtSignal(quit('clicked()')),QtCore.pyqtSlot('quit()' )       


app = QApplication(sys.argv)
ve = ventanaejemplo()
ve.show()
sys.exit(app.exec_())