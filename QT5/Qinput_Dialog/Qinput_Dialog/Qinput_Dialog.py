
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.show()
        
    def initUI(self):      
        #create push button, position, connection with a funsion
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        #create line Edit, position
        self.le = QLineEdit(self)
        self.le.move(130, 22)
        
        #create window, set title, and show
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        
        
        
    def showDialog(self):
        #text stores writen input text
        #in_dialog is the window
        
        text, in_dialog = QInputDialog.getText(self, 'ventana Dialogo', 
            'Enter your name:')
        
        if in_dialog:
            self.le.setText(str(text))
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())