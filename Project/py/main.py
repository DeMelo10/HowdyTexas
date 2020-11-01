# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bruno/Desktop/Bruno/My Codes/Python/Algoritmos/AT3/Project/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(31, 35, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fr_top = QtWidgets.QFrame(self.centralwidget)
        self.fr_top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_top.setObjectName("fr_top")
        self.verticalLayout.addWidget(self.fr_top)
        self.fr_content = QtWidgets.QFrame(self.centralwidget)
        self.fr_content.setMinimumSize(QtCore.QSize(0, 35))
        self.fr_content.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fr_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content.setObjectName("fr_content")
        self.fr_search = QtWidgets.QFrame(self.fr_content)
        self.fr_search.setGeometry(QtCore.QRect(150, 230, 500, 60))
        self.fr_search.setMinimumSize(QtCore.QSize(500, 0))
        self.fr_search.setMaximumSize(QtCore.QSize(600, 70))
        self.fr_search.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_search.setObjectName("fr_search")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fr_search)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ld_search = QtWidgets.QLineEdit(self.fr_search)
        self.ld_search.setMinimumSize(QtCore.QSize(0, 40))
        self.ld_search.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ld_search.setFont(font)
        self.ld_search.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    border: 2px solid rgb(0, 139, 209);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_search.setObjectName("ld_search")
        self.horizontalLayout_3.addWidget(self.ld_search)
        self.btn_search = QtWidgets.QPushButton(self.fr_search)
        self.btn_search.setMinimumSize(QtCore.QSize(90, 32))
        self.btn_search.setMaximumSize(QtCore.QSize(100, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(0, 139, 209);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 130, 215);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 122, 209);\n"
"}")
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_3.addWidget(self.btn_search)
        self.lb_logo = QtWidgets.QLabel(self.fr_content)
        self.lb_logo.setGeometry(QtCore.QRect(282, 150, 235, 50))
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lb_logo.setFont(font)
        self.lb_logo.setStyleSheet("color: rgb(255,255,255);")
        self.lb_logo.setObjectName("lb_logo")
        self.fr_logo = QtWidgets.QFrame(self.fr_content)
        self.fr_logo.setGeometry(QtCore.QRect(340, 20, 120, 120))
        self.fr_logo.setStyleSheet("background-image: url(:/logo/texas2.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.fr_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_logo.setObjectName("fr_logo")
        self.fr_result = QtWidgets.QFrame(self.fr_content)
        self.fr_result.setGeometry(QtCore.QRect(115, 300, 570, 190))
        self.fr_result.setMinimumSize(QtCore.QSize(540, 190))
        self.fr_result.setStyleSheet("border-radius: 5px;\n"
"padding: 5px;\n"
"background-color: rgb(47, 47, 47);\n"
"color: rgb(200,200,200);")
        self.fr_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_result.setObjectName("fr_result")
        self.lb_result = QtWidgets.QLabel(self.fr_result)
        self.lb_result.setGeometry(QtCore.QRect(17, 30, 535, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lb_result.setFont(font)
        self.lb_result.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lb_result.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_result.setObjectName("lb_result")
        self.btn_close = QtWidgets.QPushButton(self.fr_result)
        self.btn_close.setGeometry(QtCore.QRect(540, 10, 20, 20))
        self.btn_close.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_close.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/close/close.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"        background-color: rgb(52,52,52);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35,35,35);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.verticalLayout.addWidget(self.fr_content)
        self.fr_button = QtWidgets.QFrame(self.centralwidget)
        self.fr_button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.fr_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_button.setObjectName("fr_button")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_button)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_credits = QtWidgets.QLabel(self.fr_button)
        self.lb_credits.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-right: 5px;")
        self.lb_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_credits.setObjectName("lb_credits")
        self.horizontalLayout.addWidget(self.lb_credits)
        self.verticalLayout.addWidget(self.fr_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ld_search, self.btn_search)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Howdy Texas"))
        self.ld_search.setPlaceholderText(_translate("MainWindow", "Ex: distance between the 7th and 21th intersection."))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.lb_logo.setText(_translate("MainWindow", "Howdy Texas"))
        self.lb_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search result</span></p><p align=\"center\">Please, <span style=\" font-weight:600;\">enter</span> the <span style=\" font-weight:600;\">numbers of the crossroads</span> you want to search for!</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.lb_credits.setText(_translate("MainWindow", "<html><head/><body><p>Developed by <span style=\" font-weight:600;\">Bruno Melo</span> and <span style=\" font-weight:600;\">Felipe Tabosa</span>.</p></body></html>"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

