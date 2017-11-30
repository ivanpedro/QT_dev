
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtCore    
from PyQt5.QtWidgets import (QAction, QPushButton, QCheckBox, QMainWindow,
                            QApplication, QMessageBox)

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Inecsoft")
        self.setWindowIcon(QIcon('pythonlogo.png'))

        extractAction = QAction("&Quit App!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractAction = QAction(QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.setStatusTip('icon image')
        extractAction.triggered.connect(self.close_application)
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        checkBox = QCheckBox('Enlarge Window', self)
        checkBox.setStatusTip('enlarge window')
        checkBox.setToolTip('This checkbox <b>Enlarges the window</b>')
        checkBox.move(100, 25)
        # toggle make the check box checked by default
        #checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)
        #depending on what you want the default to be.
        #checkBox.toggle()
        self.show()

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
        


    def close_application(self):
        choice = QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


