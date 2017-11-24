
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QPushButton, QMessageBox
from PyQt5 import QtGui, QtCore

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Inecsoft")
        self.setWindowIcon(QIcon('pythonlogo.png'))

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
        btn_new_file = QAction('New File', self)
        btn_new_file.setShortcut("Ctrl+Shift+N")
        btn_new_file.setStatusTip('create new file')
        btn_new_file.triggered.connect(self.close_application)

        btn_new_project = QAction('Project', self)
        btn_new_project.setShortcut("Ctrl+Shift+P")
        btn_new_project.setStatusTip('create new file')
        btn_new_project.triggered.connect(self.close_application)
 
        new_Menu.addAction(btn_new_file)
        new_Menu.addAction(btn_new_project)

        #declare  bottoms in the submenu for  bottom_file
                
        btn_open = QAction('Open', self)
        btn_save = QAction('Save', self)
        btn_print = QAction('Print', self)
        btn_import = QAction('Import File', self)
        btn_export = QAction('Export File', self)
        btn_exit = QAction('Exit', self) 
        #behabiour of bottom for bottom_file
        btn_exit.setShortcut('Ctrl+Q')
        btn_exit.setStatusTip('Exit program')
        btn_exit.triggered.connect(self.close_application)
       
        #add submenu bottoms for bottom_file or bottom menu

        bottom_file.addMenu(new_Menu)
        bottom_file.addAction(btn_open)
        bottom_file.addAction(btn_save)
        bottom_file.addAction(btn_print)
        bottom_file.addAction(btn_exit)
       

        #declare single action bottoms in the submenu for  bottom_edit
        btn_undo = QAction('Undo', self)
        #behabiour of bottom 
        btn_undo.setShortcut('Ctrl+Z')
        btn_undo.setStatusTip('Step Back')
        btn_exit.triggered.connect(self.undo)

        btn_Redo = QAction('Redo', self)
        btn_cut = QAction('Cut', self)        
        btn_copy = QAction('Copy', self)
        btn_paste = QAction('Paste', self)
        btn_delete = QAction('Delete', self)
        btn_select_all = QAction('Select All', self) 


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
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractAction = QAction(QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        
        self.show()

    def close_application(self):
        choice = QMessageBox.question(self, 'Exit Program',
                                      'Are you sure you want Exit Program?',
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def undo(self):

        if not stack:
            return
        previous = stack.pop()
        previous.undo()

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()