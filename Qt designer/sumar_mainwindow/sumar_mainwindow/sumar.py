# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sumar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbtn_sumar = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_sumar.setGeometry(QtCore.QRect(230, 290, 75, 23))
        self.pbtn_sumar.setObjectName("pbtn_sumar")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(40, 90, 111, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 220, 71, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_in_num1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_in_num1.setGeometry(QtCore.QRect(210, 90, 113, 20))
        self.lineEdit_in_num1.setObjectName("lineEdit_in_num1")
        self.lineEdit_in_num2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_in_num2.setGeometry(QtCore.QRect(210, 150, 113, 20))
        self.lineEdit_in_num2.setObjectName("lineEdit_in_num2")
        self.lineEdit_in_num3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_in_num3.setGeometry(QtCore.QRect(210, 220, 113, 20))
        self.lineEdit_in_num3.setObjectName("lineEdit_in_num3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.pbtn_sumar.clicked.connect(self.lineEdit_in_num3.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inecsoft"))
        self.pbtn_sumar.setText(_translate("MainWindow", "sumar"))
        self.label_1.setText(_translate("MainWindow", "Enter primer numero:"))
        self.label_2.setText(_translate("MainWindow", "Enter segundo numero:"))
        self.label_3.setText(_translate("MainWindow", "Resultado:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

