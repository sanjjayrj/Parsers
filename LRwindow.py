# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LRwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LRwindow(object):
    def setupUi(self, LRwindow):
        LRwindow.setObjectName("LRwindow")
        LRwindow.resize(1119, 831)
        self.centralwidget = QtWidgets.QWidget(LRwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.I_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.I_Table.setGeometry(QtCore.QRect(50, 60, 361, 601))
        self.I_Table.setObjectName("I_Table")
        self.I_Table.setColumnCount(2)
        self.I_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.I_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.I_Table.setHorizontalHeaderItem(1, item)
        self.parse_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.parse_Table.setGeometry(QtCore.QRect(470, 60, 601, 601))
        self.parse_Table.setObjectName("parse_Table")
        self.parse_Table.setColumnCount(0)
        self.parse_Table.setRowCount(0)
        self.ResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(360, 700, 321, 51))
        self.ResultLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.ResultLabel.setObjectName("ResultLabel")
        LRwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LRwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 26))
        self.menubar.setObjectName("menubar")
        LRwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LRwindow)
        self.statusbar.setObjectName("statusbar")
        LRwindow.setStatusBar(self.statusbar)

        self.retranslateUi(LRwindow)
        QtCore.QMetaObject.connectSlotsByName(LRwindow)

    def retranslateUi(self, LRwindow):
        _translate = QtCore.QCoreApplication.translate
        LRwindow.setWindowTitle(_translate("LRwindow", "MainWindow"))
        item = self.I_Table.horizontalHeaderItem(0)
        item.setText(_translate("LRwindow", "State"))
        item = self.I_Table.horizontalHeaderItem(1)
        item.setText(_translate("LRwindow", "ItemSet"))
        self.ResultLabel.setText(_translate("LRwindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LRwindow = QtWidgets.QMainWindow()
    ui = Ui_LRwindow()
    ui.setupUi(LRwindow)
    LRwindow.show()
    sys.exit(app.exec_())

