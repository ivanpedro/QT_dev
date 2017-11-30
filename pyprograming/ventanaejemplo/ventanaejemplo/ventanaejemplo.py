import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QAction, QPushButton, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QMetaObject

class ventanaejemplo(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Ventana de ejemplo')
        quit = QPushButton('Cerrar', self)
        quit.setGeometry(10,10,70,40)
        #senal = 'clicked()' -> self.connect() -> slot='quit()'
        quit.clicked.connect(self.cerrar)
    
    def cerrar(self):
        choice = QMessageBox.question(self, 'Cerrar ventana',"Seguro quieres cerrar!",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

app = QApplication(sys.argv)
ve = ventanaejemplo()
ve.show()
sys.exit(app.exec_())