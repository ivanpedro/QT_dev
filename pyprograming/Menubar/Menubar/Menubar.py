
import sys
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (QMainWindow, QApplication, QMenu,
                             QAction, QPushButton, QMessageBox,
                             QWidget)
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Inecsoft")
        self.setWindowIcon(QIcon('icons/icon.png'))

        #main menu
        #create menu
        self.menuBar()
        mainMenu = self.menuBar()

        #create bottoms in the main menu
        bottom_file = mainMenu.addMenu('&File')
        bottom_edit = mainMenu.addMenu('&Edit')
        bottom_search = mainMenu.addMenu('&Search')
        bottom_view = mainMenu.addMenu('&View')
        bottom_tool = mainMenu.addAction('&Tools')
        bottom_plot = mainMenu.addMenu('&Plot')

        #create menu bottom
        new_Menu = QMenu('New', self)
        
        #create sub categories menu for new  and define characteristics for the new file bottom
        btn_new_file = QAction(QIcon('icons/icon.png'),'New File', self)
        btn_new_file.setShortcut("Ctrl+Shift+N")
        btn_new_file.setStatusTip('create new file')
        btn_new_file.triggered.connect(self.closeEvent)

        btn_new_project = QAction(QIcon('icons/icon.png'),'Project', self)
        btn_new_project.setShortcut("Ctrl+Shift+P")
        btn_new_project.setStatusTip('create new file')
        btn_new_project.triggered.connect(self.closeEvent)
 
        new_Menu.addAction(btn_new_file)
        new_Menu.addAction(btn_new_project)

        #declare  bottoms in the submenu for  bottom_file
                
        btn_open = QAction(QIcon('icons/icon.png'),'Open', self)
        btn_save = QAction(QIcon('icons/icon.png'),'Save', self)
        btn_print = QAction(QIcon('icons/icon.png'),'Print', self)
        btn_import = QAction(QIcon('icons/icon.png'),'Import File', self)
        btn_export = QAction(QIcon('icons/icon.png'),'Export File', self)
        btn_exit = QAction(QIcon('icons/icon.png'),'Exit', self) 
        #behabiour of bottom for bottom_file
        btn_exit.setShortcut('Ctrl+Q')
        btn_exit.setStatusTip('Exit program')
        btn_exit.triggered.connect(self.closeEvent)
       
        #add submenu bottoms for bottom_file or bottom menu

        bottom_file.addMenu(new_Menu)
        bottom_file.addAction(btn_open)
        bottom_file.addAction(btn_save)
        bottom_file.addAction(btn_print)
        bottom_file.addAction(btn_exit)
       

        #declare single action bottoms in the submenu for  bottom_edit
        btn_undo = QAction(QIcon('icons/icon.png'),'Undo', self)
        #behabiour of bottom 
        btn_undo.setShortcut('Ctrl+Z')
        btn_undo.setStatusTip('Step Back')
        #btn_undo.setIcon(QIcon('icons/icon.png'))
        btn_undo.triggered.connect(self.undo)
        
        btn_Redo = QAction(QIcon('icons/icon.png'),'Redo', self)
        btn_Redo.setShortcut("Ctrl+R")
        btn_Redo.setStatusTip('Step forward')
        btn_Redo.setToolTip('Step forward')
        btn_Redo.triggered.connect(self.closeEvent)
        #btn_Redo.triggered.connect(QCoreApplication.instance().undoAction())
        
        btn_cut = QAction(QIcon('icons/icon.png'),'Cut', self)        
        btn_copy = QAction(QIcon('icons/icon.png'),'Copy', self)
        #self.btn_copy.clicked.connect(self.lineEdit_in_num3.copy)
        btn_paste = QAction(QIcon('icons/icon.png'),'Paste', self)
        btn_delete = QAction(QIcon('icons/icon.png'),'Delete', self)
        btn_select_all = QAction(QIcon('icons/icon.png'),'Select All', self) 


        #add submenu bottoms for bottom_edit

        bottom_edit.addAction(btn_undo)
        bottom_edit.addAction(btn_Redo)
        bottom_edit.addAction(btn_cut)
        bottom_edit.addAction(btn_copy)
        bottom_edit.addAction(btn_paste)
        bottom_edit.addAction(btn_delete)
        bottom_edit.addAction(btn_select_all)
        
        self.home()

    def home(self):
        #bottom
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.closeEvent)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractAction = QAction(QIcon('icons/icon.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.closeEvent)
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        
        self.show()

    def closeEvent(self, event):
        choice = QMessageBox.question(self, 'Exit Program',
                                      'Are you sure you want Exit Program?',
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            #event.accept()
            sys.exit()
        else:
            #event.ignore()
            pass

    def undo(self):

        if not stack:
            return
        previous = stack.pop()
        previous.undo()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


