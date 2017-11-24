
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMainWindow, QMessageBox) 

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        """
        setGeometry() does two things: it locates the window on the screen and sets it size. The first two 
        parameters are the x and y positions of the window. The third is the width and the fourth is the height
        of the window. In fact, it combines the resize() and move() methods in one method. The last method sets
        the application icon. To do this, we have created a QIcon object. The QIcon receives the path to our icon
        to be displayed.

        """
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Inecsoft!")
        self.setWindowIcon(QIcon('icon.png'))
        self.home()


    def home(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        #This static method sets a font used to render tooltips.
        # We use a 10px SansSerif font.

        btn = QPushButton("Quit", self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(100,100)
        btn.move(100,100)
        self.show()

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
			#or sys.exit()
        else:
            event.ignore()
			#or pass
        
def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()

"""
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import QFont    


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

"""