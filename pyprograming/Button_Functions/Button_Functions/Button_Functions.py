
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5 import QtGui, QtCore


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("inecsoft!")
        self.setWindowIcon(QIcon('pythonlogo.png'))
        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)
        self.show()

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()
    
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()