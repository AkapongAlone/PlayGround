# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoThreadAndHaveThread.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 123)
        MainWindow.setMinimumSize(QtCore.QSize(636, 123))
        MainWindow.setMaximumSize(QtCore.QSize(636, 123))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_nothread = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nothread.setGeometry(QtCore.QRect(50, 20, 151, 61))
        self.btn_nothread.setObjectName("btn_nothread")
        self.btn_havethread = QtWidgets.QPushButton(self.centralwidget)
        self.btn_havethread.setGeometry(QtCore.QRect(440, 20, 151, 61))
        self.btn_havethread.setObjectName("btn_havethread")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(240, 50, 181, 23))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setObjectName("progressBar")
        self.lb_result = QtWidgets.QLabel(self.centralwidget)
        self.lb_result.setGeometry(QtCore.QRect(270, 20, 91, 16))
        self.lb_result.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_result.setObjectName("lb_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_nothread.setText(_translate("MainWindow", "ไม่มี Thread"))
        self.btn_havethread.setText(_translate("MainWindow", "มี Thread"))
        self.lb_result.setText(_translate("MainWindow", "label"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

