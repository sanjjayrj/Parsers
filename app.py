# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from lr_parser import lr_parser
from LRwindow import Ui_LRwindow
import bgimage_rs
from slr_parser import slr_parser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1038, 699)
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTerminals = QtWidgets.QLabel(self.centralwidget)
        self.labelTerminals.setGeometry(QtCore.QRect(50, 50, 281, 16))
        self.labelTerminals.setStyleSheet("font: 75 11pt \"Consolas\";\n"
"text-decoration: underline;\n"
"color: rgb(225, 225, 255);")
        self.labelTerminals.setObjectName("labelTerminals")
        self.TerminalsTB = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TerminalsTB.setGeometry(QtCore.QRect(40, 80, 421, 61))
        self.TerminalsTB.setWhatsThis("")
        self.TerminalsTB.setObjectName("TerminalsTB")
        self.nLabel = QtWidgets.QLabel(self.centralwidget)
        self.nLabel.setGeometry(QtCore.QRect(50, 170, 271, 16))
        self.nLabel.setStyleSheet("font: 75 11pt \"Consolas\";\n"
"text-decoration: underline;\n"
"color: rgb(225, 225, 255);")
        self.nLabel.setObjectName("nLabel")
        self.ProductionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProductionLabel.setGeometry(QtCore.QRect(580, 50, 300, 16))
        self.ProductionLabel.setStyleSheet("font: 75 11pt \"Consolas\";\n"
"text-decoration: underline;\n"
"color: rgb(225, 225, 255);")
        self.ProductionLabel.setObjectName("ProductionLabel")
        self.Productions = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Productions.setGeometry(QtCore.QRect(570, 80, 421, 201))
        self.Productions.setObjectName("Productions")
        self.StartsymbolLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartsymbolLabel.setGeometry(QtCore.QRect(50, 230, 281, 16))
        self.StartsymbolLabel.setStyleSheet("font: 75 11pt \"Consolas\";\n"
"text-decoration: underline;\n"
"color: rgb(225, 225, 255);")
        self.StartsymbolLabel.setObjectName("StartsymbolLabel")
        self.StartSymbol = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.StartSymbol.setGeometry(QtCore.QRect(40, 250, 421, 31))
        self.StartSymbol.setObjectName("StartSymbol")
        self.LL_0 = QtWidgets.QPushButton(self.centralwidget)
        self.LL_0.setGeometry(QtCore.QRect(60, 440, 221, 71))
        self.LL_0.setObjectName("LL_0")
        self.LL_1 = QtWidgets.QPushButton(self.centralwidget)
        self.LL_1.setGeometry(QtCore.QRect(760, 440, 221, 71))
        self.LL_1.setObjectName("LL_1")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(450, 550, 93, 28))
        self.clearButton.setStyleSheet("")
        self.clearButton.setObjectName("clearButton")
        self.Querry = QtWidgets.QLabel(self.centralwidget)
        self.Querry.setGeometry(QtCore.QRect(470, 310, 131, 20))
        self.Querry.setStyleSheet("font: 75 11pt \"Consolas\";\n"
"text-decoration: underline;\n"
"color: rgb(225, 225, 255);")
        self.Querry.setObjectName("Querry")
        self.StartSymbol_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.StartSymbol_2.setGeometry(QtCore.QRect(300, 340, 431, 31))
        self.StartSymbol_2.setObjectName("StartSymbol_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 1041, 681))
        self.frame.setStyleSheet("background-image: url(:/bgImage/graphics.webp);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nSpin = QtWidgets.QSpinBox(self.frame)
        self.nSpin.setGeometry(QtCore.QRect(320, 170, 42, 22))
        self.nSpin.setObjectName("nSpin")
        self.frame.raise_()
        self.labelTerminals.raise_()
        self.TerminalsTB.raise_()
        self.nLabel.raise_()
        self.ProductionLabel.raise_()
        self.Productions.raise_()
        self.StartsymbolLabel.raise_()
        self.StartSymbol.raise_()
        self.LL_0.raise_()
        self.LL_1.raise_()
        self.clearButton.raise_()
        self.Querry.raise_()
        self.StartSymbol_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #################################################################
        self.LL_0.clicked.connect(self.onLL_0)
        self.LL_1.clicked.connect(self.onLL_1)
        self.clearButton.clicked.connect(self.clearLabels)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTerminals.setText(_translate("MainWindow", "Enter Terminals"))
        self.TerminalsTB.setPlaceholderText(_translate("MainWindow", "seperated by \' , \'"))
        self.nLabel.setText(_translate("MainWindow", "Enter number of Terminals"))
        self.ProductionLabel.setText(_translate("MainWindow", "Enter Productions line by line"))
        self.Productions.setPlaceholderText(_translate("MainWindow", "non-terminal -> production|production"))
        self.StartsymbolLabel.setText(_translate("MainWindow", "Enter Start Symbol"))
        self.LL_0.setText(_translate("MainWindow", "LR(0)"))
        self.LL_1.setText(_translate("MainWindow", "SLR(1)"))
        self.clearButton.setText(_translate("MainWindow", "Clear Input"))
        self.Querry.setText(_translate("MainWindow", "Enter Query"))

    def clearLabels(self):
        self.TerminalsTB.setPlainText("")
        self.Productions.setPlainText("")
        self.StartSymbol.setPlainText("")
        self.StartSymbol_2.setPlainText("")
        self.nSpin.setValue(0)

    def onLL_1(self):
        try:

            prod = self.Productions.toPlainText()
            term = self.TerminalsTB.toPlainText()
            num_term = self.nSpin.value()
            start_sym = self.StartSymbol.toPlainText()
            query = self.StartSymbol_2.toPlainText()

            #prod = "E -> E+T | T \n T -> T*F | F \n F -> (E) | #"
            #term = "+,(,),*,@,#"
            #num_term = 6
            #start_sym = "E"
            #query = "#+#*#"

            out = slr_parser(prod, term, num_term, start_sym, query)
            I, parseTable, accepted = out[0], out[1], out[2]
            symbols = out[3]
            print(symbols)

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LRwindow()
            self.ui.setupUi(self.window)

            self.ui.I_Table.setColumnWidth(0, 50)
            self.ui.I_Table.setColumnWidth(1, 306)

            # -----------------------Cannonical--------------------------------------------------------
            new = []
            for count, i in enumerate(I):
                # print(count + 1, i)
                temp = [prod[0] + " -> " + prod[1] for prod in i]
                new.append(temp)

            self.ui.I_Table.setRowCount(len(new))
            self.ui.I_Table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.ui.I_Table.verticalHeader().setVisible(False)
            row = 0
            for i in range(len(new)):
                self.ui.I_Table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                self.ui.I_Table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(new[i])))
                row += 1

            # ----------------------------Result Label-------------------------------------------------------------
            if (accepted):
                self.ui.ResultLabel.setText("Query is accepted! ")
            else:
                self.ui.ResultLabel.setText("Query is not accepted! ")
            self.window.show()

            # ----------------------Parse Table---------------------------------------------------------------------

            # words = symbols.

            self.ui.parse_Table.setRowCount(len(parseTable))
            self.ui.parse_Table.setColumnCount(len(parseTable[0]))
            self.ui.parse_Table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.ui.parse_Table.setHorizontalHeaderLabels(symbols)

            #for i in range(len(parseTable)):
            #    self.ui.parse_Table.setColumnWidth(i, 601//len(parseTable))


            self.ui.parse_Table.resizeColumnsToContents()
            self.ui.parse_Table.resizeRowsToContents
            self.ui.I_Table.resizeColumnsToContents()
            self.ui.I_Table.resizeRowsToContents

            for i in range(len(parseTable)):
                for j in range(len(parseTable[i])):
                    self.ui.parse_Table.setItem(i, j, QtWidgets.QTableWidgetItem(str(parseTable[i][j])))
                    self.ui.parse_Table.setItem(i, j, QtWidgets.QTableWidgetItem(str(parseTable[i][j])))

            print(parseTable)



        except Exception as e:
            print(e)
            print('Error!')
            msg2 = QMessageBox()
            msg2.setWindowTitle("Invalid Input")
            msg2.setIcon(QMessageBox.Warning)
            msg2.setText("   Invalid Input!  ")
            x = msg2.exec_()

    def onLL_0(self):
        try:

            prod = self.Productions.toPlainText()
            term = self.TerminalsTB.toPlainText()
            num_term = self.nSpin.value()
            start_sym = self.StartSymbol.toPlainText()
            query = self.StartSymbol_2.toPlainText()

            #prod = "E -> E+T | T \n T -> T*F | F \n F -> (E) | #"
            #term = "+,(,),*,@,#"
            #num_term = 6
            #start_sym = "E"
            #query = "#+#*#"

            out = lr_parser(prod, term, num_term, start_sym, query)
            I, parseTable, accepted = out[0], out[1], out[2]
            symbols = out[3]
            print(symbols)

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LRwindow()
            self.ui.setupUi(self.window)

            self.ui.I_Table.setColumnWidth(0, 50)
            self.ui.I_Table.setColumnWidth(1, 306)

            # -----------------------Cannonical--------------------------------------------------------
            new = []
            for count, i in enumerate(I):
                # print(count + 1, i)
                temp = [prod[0] + " -> " + prod[1] for prod in i]
                new.append(temp)

            self.ui.I_Table.setRowCount(len(new))
            self.ui.I_Table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.ui.I_Table.verticalHeader().setVisible(False)
            row = 0
            for i in range(len(new)):
                self.ui.I_Table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
                self.ui.I_Table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(new[i])))
                row += 1

            # ----------------------------Result Label-------------------------------------------------------------
            if (accepted):
                self.ui.ResultLabel.setText("Query is accepted! ")
            else:
                self.ui.ResultLabel.setText("Query is not accepted! ")
            self.window.show()

            # ----------------------Parse Table---------------------------------------------------------------------

            # words = symbols.

            self.ui.parse_Table.setRowCount(len(parseTable))
            self.ui.parse_Table.setColumnCount(len(parseTable[0]))
            self.ui.parse_Table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.ui.parse_Table.setHorizontalHeaderLabels(symbols)

            #for i in range(len(parseTable)):
            #    self.ui.parse_Table.setColumnWidth(i, 601//len(parseTable))


            self.ui.parse_Table.resizeColumnsToContents()
            self.ui.parse_Table.resizeRowsToContents
            self.ui.I_Table.resizeColumnsToContents()
            self.ui.I_Table.resizeRowsToContents

            for i in range(len(parseTable)):
                for j in range(len(parseTable[i])):
                    self.ui.parse_Table.setItem(i, j, QtWidgets.QTableWidgetItem(str(parseTable[i][j])))
                    self.ui.parse_Table.setItem(i, j, QtWidgets.QTableWidgetItem(str(parseTable[i][j])))

            print(parseTable)



        except Exception as e:
            print(e)
            print('Error!')
            msg2 = QMessageBox()
            msg2.setWindowTitle("Invalid Input")
            msg2.setIcon(QMessageBox.Warning)
            msg2.setText("   Invalid Input!  ")
            x = msg2.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

