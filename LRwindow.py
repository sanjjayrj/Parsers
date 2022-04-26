# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LRwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import bgimage_rs

class Ui_LRwindow(object):
    def setupUi(self, LRwindow):
        LRwindow.setObjectName("LRwindow")
        LRwindow.resize(1258, 841)
        self.centralwidget = QtWidgets.QWidget(LRwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.I_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.I_Table.setGeometry(QtCore.QRect(50, 60, 421, 601))
        self.I_Table.setObjectName("I_Table")
        self.I_Table.setColumnCount(2)
        self.I_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.I_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.I_Table.setHorizontalHeaderItem(1, item)
        self.parse_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.parse_Table.setGeometry(QtCore.QRect(540, 60, 651, 601))
        self.parse_Table.setAutoFillBackground(False)
        self.parse_Table.setShowGrid(True)
        self.parse_Table.setObjectName("parse_Table")
        self.parse_Table.setColumnCount(0)
        self.parse_Table.setRowCount(0)
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(40, 20, 351, 60))
        self.ResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(450, 700, 351, 60))
        self.ResultLabel.setStyleSheet("font: 16pt \"Courier New\";\n"
"color: qconicalgradient(cx:0.045, cy:0.528409, angle:180.3, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.ResultLabel.setObjectName("ResultLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 30, 461, 16))
        self.label.setStyleSheet("font: 75 11pt \"Consolas\";\n"
"text-decoration: underline;\n"
"color: rgb(225, 225, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 321, 16))
        self.label_2.setStyleSheet("font: 75 11pt \"Consolas\";\n"
"text-decoration: underline;\n"
"color: rgb(225, 225, 255);")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1271, 831))
        self.frame.setStyleSheet("background-image: url(:/bgImage/graphics.webp);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.I_Table.raise_()
        self.parse_Table.raise_()
        self.ResultLabel.raise_()
        self.label.raise_()
        self.label_2.raise_()
        LRwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LRwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1258, 26))
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
        self.ResultLabel.setText(_translate("LRwindow", "AAAAAAAAAAAAAAA"))
        self.label.setText(_translate("LRwindow", "Parse Table"))
        self.label_2.setText(_translate("LRwindow", "Cannonical Form"))
        self.TitleLabel.setText(_translate("LRwindow", "Title"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LRwindow = QtWidgets.QMainWindow()
    ui = Ui_LRwindow()
    ui.setupUi(LRwindow)
    LRwindow.show()
    sys.exit(app.exec_())

